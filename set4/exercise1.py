"""All about IO."""


import json
import os
from threading import local
from tkinter import W
import py
import requests
import inspect
import sys
import re

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print(
        f"""
    Be careful that your relative paths are
    relative to where you think they are
    LOCAL: {LOCAL}
    CWD: "CWD
    """
    )


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    # Open JSON file, convert data to a dictionary & store it in variable "contents"
    mode = "r"
    with open((LOCAL + "\lazyduck.json"), mode, encoding="utf-8") as some_details:
        some_details = json.load(some_details)

        # get required data and store in variables
        lastName = some_details["results"][0]["name"]["last"]
        password = some_details["results"][0]["login"]["password"]
        postcode = some_details["results"][0]["location"]["postcode"]
        id_value = some_details["results"][0]["id"]["value"]

        # converting "postcode" & "id_value" into ints
        postcode = int(postcode)
        id_value = int(id_value)

        # add "postcode" & "id_value"
        postcodePlusID = postcode + id_value

        # print(lastName, password, postcodePlusID)

    return {
        "lastName": lastName,
        "password": password,
        "postcodePlusID": postcodePlusID,
    }


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20
    The generator takes a single argument, length (`wordlength`) of the word.
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &wordlength=
    """
    startNum = 3
    stopNum = 21
    stepNum = 2

    pyramid = []

    # counting up from startNum to stopNum, with incraments of stepNum
    for wordLength in range(startNum, stopNum, stepNum):

        # importing a random word & decoding it from bites to a string (length of word == wordLength variable), then adding it to the list
        word = requests.get(f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={wordLength}")
        word = word.text
        pyramid.append(word)

        # counting back down from stopNum to startNum with the same increments as before (stepNum is negative as we are counting backwards)
        if wordLength >= stopNum - stepNum:
            for negWordLength in range(stopNum - 1, startNum, -stepNum):

                # importing a random world & decoding... length of word == negWordLength.
                word = requests.get(f"https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={negWordLength}")
                word = word.text
                pyramid.append(word)

    return pyramid


def pokedex(low=1, high=5):
    """Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    heightList = []

    # put the height of each pokemon within the range specified into a list
    for id in range(low, high):
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        r = requests.get(url)
        if r.status_code is 200:
            data = json.loads(r.text)
            height = data["height"]

            heightList.append(height)

        else:
            return "Data not found"

    # Find the ID of the tallest pokemon in the range
    tallest_value = max(heightList)
    tallest_index = heightList.index(tallest_value)

    tallest_id = tallest_index + low

    # pull the required info of the tallest pokemon and return it in a dict.
    url = f"https://pokeapi.co/api/v2/pokemon/{tallest_id}"
    r = requests.get(url)
    if r.status_code is 200:
            data = json.loads(r.text)
            pokename = data["name"]
            pokeweight = data["weight"]
            pokeheight = data["height"]
    
    return {"name": pokename, "weight": pokeweight, "height": pokeheight}


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the Set4 directory.

    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.

    NOTE: this function doesn't return anything. It has the _side effect_ of modifying the file system
    """
    with open(LOCAL + "/Trispokedovetiles(laser).gcode", "r", encoding="utf-8") as gcode:
        data = gcode.read()
        count = data.count('M10 P1')

    # write the answer to a file called 'lasers.pew' in the Set4 dir
    with open(LOCAL + "\lasers.pew", "w", encoding="utf-8") as pew_num:
        pew_num.write(f"{count}")


if __name__ == "__main__":
    print(get_some_details())

    wp = wordy_pyramid()
    [print(f"{word} {len(word)}") for word in wp]

    print(pokedex(low=3, high=7))

    diarist()

    in_root = os.path.isfile("lasers.pew")
    in_set4 = os.path.isfile("set4/lasers.pew")
    if not in_set4 and not in_root:
        print("diarist did not create lasers.pew")
    elif not in_set4 and in_root:
        print(
            "diarist did create lasers.pew, but in the me folder, it should be in the set4 folder"
        )
    elif in_set4:
        print("lasers.pew is in the right place")

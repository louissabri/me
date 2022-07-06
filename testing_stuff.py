from set8.quiz import fizz_buzz


def FizzBuzz():

    list = []

    for i in range(100):
        
        if i % 3 == 0:
            list.append("Fizz")

        elif i % 5 == 0:
            list.append("Buzz")
        
        else:
            list.append(i)

    return(list)

print(FizzBuzz())
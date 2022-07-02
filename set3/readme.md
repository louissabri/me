TODO: Reflect on what you learned this week and what is still unclear.

29/06/22 12:48 I can't get loop_ranger to work with a while loop & in the interest of time I am going to move on but I would like to come back to this and work it out.

 list = []

    for i in range(start, stop, step):

        list.append(i)
        
    return list

    list = []
    while start is not stop:

        list.append(start + step)

    return list

14:11 I'm stuck on stubborn_asker, it seems to me that i've got it working perfectly when I run the program, yet the tests are not happy with me. I'm not sure where I'm getting it wrong.

17:30 I went through the solution posted on the website and managed to get it working (with some tweaking, for some reason it didn't work when I copied the code from the video directly)

I've deleted my old code that wasn't working which as a bit silly because now I don't know what I was doing wrong and can't learn from it. Ah well. I know the right way now.

17:43 I breezed through the final two exercises! Completed them quickly. On to the next! 

30/06/2022 00:04 working through these exercises one by one has been super cool, I love seeing how the stuff I learned earlier translates. Kudos to you btw Ben, the pacing feels really good I feel like I'm challenged just enough by each new exercise to keep it interesting, without being completely stuck every time I start something new.

30/06/2022 11:25 Getting stuck into this binary search, I want to finish it before I have to leave for campus at 1300.

Right off the bat I see how the guessing game applies to this. It looks like I was applying a binary search by default whenever I played the guessing game of last exercise. Cool.

I'm planning on re using a lot of code from the advanced guessing game. I'm wondering if I should make the lower/upper bounds automatically generated, or let the user input them. Same with the actual number. Could be fun to turn the tables and make the computer guess a number that the user already knows.

2/07/2022 3:40 I think I got the binary search to work, but every time I run the test I get stuck in a loop of histograms popping up. It actually crashed my VSC lol.

I got it working! I found the error: Originally I had my while loop set up as

while guess != actual number

as in while the current guess does not equal the actual number. This makes sense (I guess that's why I used it in the first place) but I believe that the program was freaking out and taking way longer than it should because it was allowing a situation where low > high to happen, then shitting itself and dying.

I changed the while loop to

while low <= high in order to fix this and now it works!

(if I'm completely honest I don't *fully* understand why this this is right now and I don't intend to look into it until morning. I just remembered Louis mentioning that he came across this problem and that changing the while loop was how he solved it.)
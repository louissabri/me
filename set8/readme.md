TODO: Reflect on what you learned this week and what is still unclear.

I hate this stupid last question on the quiz. Trying to troubleshoot and work out what is going wrong will update at some point with more info.

New approach, I originally dove into this head first writing random bits of code without planning anything out. Have now taken a step back and am planning how to solve the problem with a pen and paper

it worked! I have got 32/34 of the tests passing as of now, with the only ones not passing being the capitalisation & full stopping parts of the test. There will be some little quirk to sort out, I will look into it now.

Strangely, I am getting two different errors depending on whether the "dict_cache.json" file exists.

If the file DOES exist (i.e. if I have run the program before & it has thus alread generated the file) I get False, raw <built-in method capitalize of str object at 0x000001F34479D320>.

If the file DOES NOT exist I get local variable 'myDict' referenced before assignment, raw <built-in method capitalize of str object at 0x0000022360877D70>.

I GOT IT I GOT IT YAYAYAYAYAYYAYAYY

It was throwing this error because when I was capitalising the first letter of the paragraph with .capitalize, I forgot to include the () on the end: 

    para.capitalize instead of para.capitalize()

This has been an epic journey but the sense of accomplishment I feel now is amazing. Very cool. Thanks Ben.
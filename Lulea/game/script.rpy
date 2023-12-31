define p = Character("[p_name]")
define e = Character("Eileen")
image snow1 = Fixed(SnowBlossom("gui/snow1.png", 50, xspeed=(20,50), yspeed=(100,200), start=10))
image snow2 = Fixed(SnowBlossom("gui/snow2.png", 50, xspeed=(20,50), yspeed=(100,200), start=10))
define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
"""

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    text _("Choississez vite !") xalign 0.5 yalign 0.55 size 30 bold 1 outlines [(absolute(2), "#000", absolute(1), absolute(1))]
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.50 ysize 25 xmaximum 600 at alpha_dissolve

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ health = 100

label test:
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'c'
    $ food = 0

    show snow1
    show snow2

    $ p_name = renpy.input("What's your name?", length = 20)
    show eileen happy with vpunch # or hpunch
    #scene b with Fade(2)
    show eileen happy
    p "AHHHHHHHHH"
    hide eileen happy
    show screen countdown
    menu:
        "BEEP":
            hide screen countdown
            jump a

        "BOOP":
            hide screen countdown
            jump b

label a:
    p "You said BEEP"
    $ food = 0
    menu:
        "1":
            jump b
        
        "2" if food == 1:
            jump c

label b:
    p "You said BOOP"
    return

label c:
    e "Bruh ?"
    return
"""
label start:
    return
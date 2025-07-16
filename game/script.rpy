define juniper = Character("Juniper", color="#336380" )
define honey = Character("Honey", color="#faf5c4")
define hilda = Character("Hilda", color="#134f0b")
define peach = Character("Peach", color="#efd5a5")
define jax = Character("Jax", color="#ab4b4e")
define player = Character("[foxName]", color="#11d0d4")

image woods = "treesbackground.png"
image normal_fox = "normal_fox.png"
image hilda = "deer.png"
image jax = "evilbunny.png"
image scared_fox = "scared_fox.png"
image honey = "bee.png"
image juniper = "riverotter.png"
image peach = "dog.png"

start label 
    scene woods 
    "this story takes place in a little forest"
    "this isn't an ordinary forest though"
    "this is forest town!"
    "all of the woodland creatures (and some more!) call this town home"
    "we would show you around..." 
    "but it's really early in the morning, nobody's up yet!"
    "for now, get to meet the fox you'll be spending today with!!"
    show normal_fox 
    python:
        foxName = renpy.input("choose my name!")
        foxName = name.strip() or "Flora"
    player "nice to meet you! my name's [foxName]"
    player "i guess we should get to know each other while we wait for the town to wake up"
    player "let's start with you! what do you want to know about me?"
    menu: 
        "what's your favorite food?":
        jump food 
        "what does the fox say?":
        jump song 
    label food 
        player "i really like eating berries!"
        jump continue 

    label song 
        player "i am fluent in some human and fox languages!"
        player "but i know that's not the answear you wanted haha :)"
        jump continue 
    label continue
        player "anyways, that's enough about me, let's hear about you!"
        player "who's your favorite artist?"
        python:
            favArtist = renpy.input("i should probably clarify that it's, like, a music related artist")
            favArtist = name.strip() or "Mozart"
        player "ooh! i love [favArtist]!"
        "*chattering in the distance*"
        player "look at the time! it looks like things will be open now!"
        player "let's go to the record store first! maybe we'll find a [favArtist] album!"
        hide normal_fox
        pause 0.5
        show hilda 
        hilda "hello! i have a special announcement to make!"
        hide hilda 
        show normal_fox 
        player "i bet it's a lifetime supply of berries!"
        player "...but i guess that doesn't make sense for a record store"
        hide normal_fox
        show hilda 
        hilda "we are giving away tickets to [favArtist]'s concert right here in Forest Town... tonight!"
        hilda "what you, our contestants, must do is do the scavenger hunt!"
        hilda "good luck!"
        hide hilda 
        pause 0.5
        show jax
            x align (1.0, 0.0)
        jax "HA. luck. I don't need luck. I'm the best and NOTHING will get in my way"
        show normal_fox 
            x align (0.0, 0.0)
        player "i didn't know you were a [favArtist] fan!"
        jax "I'm not even a fan. I'm the BEST ticket scalper EVER. I'm going to win those tickets and sell them for thousands of dollars."
        hide normal_fox
        show scared_fox
            x align (0.0, 0.0)
        player "but... that's not fair to all the other fans"
        jax "Well life's not fair kid. And you don't stand a chance"
        player "how do you know i won't beat you though? i might be a lot better than you"
        jax "Tell me kid, what's your favorite soda?"
        player "uhhhh i don't know-"
        jax "LIVE WILD EXTREME ENERGY SODA"
        jax "live. wild. energy. soda. the drink of the gods"
        jax "1,000 grams of caffeine and ... not one... not two... but THREE cups of sugar"
        jax "AND THEIR SECRET RECIPE SECRET SUBSTANCE"
        jax "It's sooooooo secret"
        jax "Like suuuuuuuuper secret"
        pause 0.5 
        player "..."
        player "that sounds really bad for you, jax"
        player "and that 'secret substance' is probably-"
        jax "You're just a pathetic loser, loser"
        jax "I'm going to do what a winner does, win"
        jax "(and maybe cheat a little)"
        jax "NOT-SO-GOODBYE"
        hide jax 
        hide scared_fox
        show normal_fox
        player "i guess we'll have to win now"
        hide normal_fox
        pause 0.5
        player "and win we did"
        player "not only did we get the [favArtist] tickets..."
        show normal_fox
        show honey
            x align (1.0, 0.0)
        player "... we made lots of friends!"
        player "we met Honey, the coffee shop owner"
        honey "buzz buzz buzz buzz (i love making matcha lattes!)"
        hide honey 
        pause 0.5
        show juniper 
            x align (1.0, 0.0)
        player "and Juniper, the quiet reader!"
        juniper "...hi..."
        juniper "...i opened a bookstore last year..."
        player "yeah you did!!"
        hide juniper 
        pause 0.5 
        show peach
            x align (1.0, 0.0)
        player "and who can forget meeting [favArtist]'s backup singer, Peach!"
        peach "*holds sign saying i'm on vocal rest*"
        hide peach
        show normal_fox
            x align (0.5, 0.0)
        player "i had such a good time with you! i hope i see you again soon!"


        





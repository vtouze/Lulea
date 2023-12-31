﻿define p = Character("[p_name]")
define e = Character("Eileen")
define s = Character("Sven")
define a = Character("Anja")
define l = Character("Liv")
define unknown = Character("???")
define v = Character("Viggo")
define g = Character("Garde")
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
    $ p_name = renpy.input("What's your name?", length = 20)
    #show image bivouac dans une foret enneigé
    #show image intérieur du bivouac --> enfant dos au père
    p "Hej fiston ! Il faut qu'on avance, on est plus très loin de Lulea."
    s "Hmm ! J'ai tellement froid. J'ai plus la force."
    p "Je sais Sven. C'est très complqiué en ce moment mais il faut absolument qu'on aille à Lulea. C'est notre seule chance d'enfin pouvoir vivre en paix, de vivre plutot que de survivre."
    p "Allez ! Allons y !"
    #Sort du bivouac avec Sven avec une carte
    p "On devrait passer par le sud, c'est par là bas."

    ############
    #image seules dans la foret à marcher
    #image d'une vieille station essence
    p "Regarde ! Une station essence ! Il y aura peut etre des choses à récupérer."*
    p "Elle est vraiment en ruine par contre."
    s "Tu crois qu'on arrivera à trouver quelque chose ?"
    p "Il le faut !"
    #entre dans la station
    #image choix entre l'arrière boutique, la boutique ou la caisse
        Arrière boutique : 
                p "J'ai pas l'impression qu'il y est grand chose..."
                s "Papa, j'ai trouvé quelque chose !"
                s "Je crois que c'est une sorte de ration ! Elle a vraiment l'air vieille"
                p "Super, Sven !"
                #Choix : la manger, lui donner, la garder
                La manger : 
                    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
                    s "Je comprends."
                Lui donner : 
                    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
                    s "Merci papa." # +1
                La garder : 
                    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
                    s "Ok papa, ça me parait juste."
        Boutique : 
                p "J'ai l'impression que tout a été dévalisé. Ca ne m'étonne pas vraiment."
                s "Papa, viens"
                p "Qu'est ce qu'il y a ?"
                p "Oh, c'est tragique. Il n'a pas l'air d'avoir grand chose sur lui."
                s "Regarde Papa, il y a une sorte de petit écusson de loup. T'as une idée de ce que sa pourrait etre ?"
                p "Je n'en ai auccune idée, c'est la première fois que je le vois."
        Caisse :
                p "Tout est completement désolé ici, je ne pense pas que fouiller la caisse soit grandement utile."
                s "Essaye peut etre les tiroirs on ne sait jamais."
                p "Bra ! Bien joué Sven ! Je crois que j'ai trouver un bandage. Ca nous saura peut etre utile plus tard."
#Coup de feu
s "C'était quoi ça, papa ?"
p "C'est surement un coup de feu, au nord de la ville"
s "Qu'est ce qu'on fait ?"
#Aller vers le bruit - Rejoindre le quartier pavillonaire (s'éloigner)
        Eloignement :
                p "Viens Sven ! On va essayer de se réfugier dans le quartier pavillonaire."
                #passe par une ruelle avec le logo loup et un texte écrit "C'est ainsi que finissent les parasites" --> "Så här hamnar parasiter"
                s "Pourquoi ils ont fait ça papa ?"
                p "Je crois qu'il faut préférer ne jamais les rencontrer."
                p "Aller viens, on va se réfugier dans cette maison le temps que ça se calme."
        Rejoindre le bruit :
                p "Aller viens Sven, il faut qu'on aille voir."
                s "Mais Papa, c'est dangereux, ils sont armés, il y a peut etre des morts !"
                p "Sven, on a plus rien. On ne peut pas vivre éternellement comme ça. Il faut qu'on récupère des ressources, tu comprends ça ?"
                s "Oui, papa"
                p "Aller, rejoignons cette maison, on les attendra ici."

#Rencontre avec les humanistes
p "On devrait etre en sécurité ici."
s "J'ai un mauvais pressentiment. Je ne me sens pas bien ici."
p "Ecoute, il faut que tu te calmes, tout va bien. Je suis la pour te protéger."
p "Allons fouillé la maison."
#choix : cuisine - chambre
        Cuisine :
                p "Allons voir la cuisine. Il y aura surement de la nourriture."
                #fouille les tirois
                p "Oh, j'ai trouvé une conserve de légumes. Elle a l'air toujours bonne."
                s "J'ai tellement faim papa, je peux la prendre ?"
                #choix : la garder - la manger - la donner
                    La manger : 
                            p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
                            s "Je comprends."
                    Lui donner : 
                            p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
                            s "Merci papa." # +1
                    La garder : 
                            p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
                            s "Ok papa, ça me parait juste."
p "Il nous suffit d'attendre encore un peu de temps."
#Bruit de rechargement, gachette...
a "Qui êtes vous ?"
p "Doucement Sven, tout va bien se passer"
p "On...On est simplement des survivants comme vous."
a "Qu'est ce qui vous amène ici ?"
p "On ne fait que passer."
a "Où voulez vous aller ?"
#choix : mentir - avouer
        Mentir : 
                p "Je vous les dis, on ne fait que passer. On veut simplement trouver un abris, un groupe, un endroit où vivre en paix"
        Avouer :
                p "On veut se rendre à Lulea. Apparamment ils ont réussi à reconstruire un village, tout le monde y vit en paix."
                a "Ah ! Lulea ! Quel mesnonge. Je ne sais pas où est ce que vous avez entendu ça mais ce sont des vrais tyrans. Ils n'ont aucune pitié. Ils sont simplement égoiste et sont près à faire des guerres à n'importe qui pour récupérer un infime partie de ressource. Ce sont juste des anguianires pret à tout. Croyez moi, vous n'aver pas envie d'aller là-bas"
                a "Vous avez vu leur logo, un loup affamé. Ils en sont fiers. Ils le mettent partoout pour faire peur aux groupes avoisinants. Et ils y arrivent. On est les seuls a vraiment leur faire tête mais c'est de plus compliqué chaque de jour de se battre conntre eux. C'est une véritable armée bien orgnaisée. Et nous on est de plus en plus vulnérable. On ne peut pas les laisser faire et on est les seul à pouvoir le faire."
                p "Vous me demandez de vous rejoindre là ?"
                a "Vous vous dites surement que vous vous en foutez de tout ce qui se passe ici mais depuis que vous etes arrivés ici. Vous etes constamment survéillé et vous ne pouvez plus sortir d'ici. Ils controlent les frontières de cette région et sont comme les prédateurs attendant gentiment leur proies de bien vouloir se présenter sous leurs yeux."
                a "Vous etes fichus ici, comme nous, comme nous tous. Vous ne pouvez plus rien faire, vous comprenez ? Vous devez absolument vous joindre à nous à moins que vous etes pret à sacrifier votre fils."
                #choix : ne rien dire - dire que ce n'est pas votre fils (chronométré)
                        Pas votre fils :
                                    p "Ce n'est pas mon fils. C'est simplement un enfant que j'ai trouvé sur ma route. J'essaie de le protéger comme je peux."
                                    a "Ok, ça n'a pas vraiment d'immportance"
                a "Alors, etes vous pret à nous rejoindre le temps de se battre contre eux, je peux vous amener à notre camp, si vous le voulez ?"
                #choix : les rejoindre - rester seuls
                        Rester seuls : 
                                    p "Je préfére protéger Sven, je ne peux pas vous aider, je suis désolé"
                                    a "Vous faites une grave erreur, vous le savez ?"
                                    p "Peut etre, mais je n'ai pas envie de l'envoyer dans une guerre de clans sans réel motivation et où la fin reste prévisible."
                                    a "Comme vous le voulez. Allez les gars, on peut y aller."

                                    p "Je ne pouvais pas nous laisser embarquer dans une guerre futile. On n'avoit pas le choix, tu comprends ?"
                                    a "Et si la femme avit raison, peut etre qu'ils nous ont déja repérer et qu'ils nous suivent en ce moment. Et si nous ne pouvons plus sortir d'ici ? Et si ils sont aussi terrifiants que le femme le disait ? Tu veux toujours qu'on les rejoingnre. Je ne veux pas etre méchant papa."
                                    p "Du calme Sven, tout va bien. On ne sait pas tout sur cette histoire. Qui te dis qu'elle disait vraiment la vérité. Ils sont en guerre, Sven. On ne peut pas croire n'importe qui. Ils recherchaient peut etre simplement des gens naifs perdus pour rejoindre leur cause sans qu'ils en aient la moindre motivation."
                                    p "Tout va bien. Du moment qu'on est que tous les deux. Rien ne peux nous arriver, d'accord ? Aller en route, le soleil se couche, il faut qu'on aille trouver un abri pour passer la nuit. Allons-y !"

                                    #image seuls à marcher
                                    p "Allez on peut se poser ici."
                                    #image feu de camp
                                    p "Ca va Sven ? T'as l'air ailleur ?"
                                    s "C'est juste que je pense toujours à ce que la femme a dit. Et si on avait fait le mauvais choix, on si on était déja condamné."
                                    p "Mais non Sven, tout va bien, on est encore tous les deux. Et ça c'est le plus important. Aller, il est tard allons se coucher !"

                                    #bruit étrange, réveil père, punch
                                    #sort du bivouac
                                    p "Liv, c'est toi mon amour ?"
                                    l "Tu me manques tellement [p_name] !"
                                    p "Je suis si perdu sans toi. J'en ai marre de tout ça."
                                    p "Je ne sais pas si tous les choix que j'ai pu faire ont été raisonnable ou pas. J'ai peur d'avoir condamné la vie de ce pauvre petit garçon."
                                    l "Tu as de la peine, pour ce garçon ? Ce n'est même pas ton enfant. Tu nous a oubliés ? Nous, ta vrai famille, moi et Arvid ?"
                                    p "Non mon coeur, je ne vous oublierais jamais. Vous etes tous pour moi. Chaque jour, chaque minutes, chaque secondes je pense à vous. Je suis perdu sans vous. Je n'en peux plus"
                                    l "Tu n'en crois pas un mot. Je te vois chaque jour, à t'occuper de cet enfant minable. Tu ne veux pas te l'avouer mais c'est trop tard. Tu ne peux rien y faire. Rejoins nous, ta famille, on a tellement envie de te revoir. Tu préfères cet enfant ou Arvid ? Chosis !"
                                    p "Bien sur que je préfère Arvid, chérie. C'est mon enfant, c'est ce dont j'ai été le plus fier."
                                    l "Alors, rejoins nous, rejoins ta femme et ton fils. On veut juste te revoir parmis nous."
                                    #l s'enfui au loin
                                    p "Reviens chéri !"
                                    #chemins successifs --> 4 séléctions de chemins puis fin
                                    p "Chéri, j'en peux plus je veux te revoir !"
                                    l "Rejoins nous"
                                    #Game Over Screen "Fin" --> bouton retour au menu principal
                        
                        Les rejoindre :
                                    p "Je ne crois qu'on a pas vraiment le choix."
                                    a "Bienvenue, chez les Upplyst <les éclairés>"
                                    a "Ok, allons y maintenant, le soleil commence à se coucher."
                                    #image du clan puis du père et du fils marchant dans la foret

                                    a "Nous voici au camp des Upplyst. On a eu des moments compliqués depuis la guerre avec Lulea"
                                    a "Je vous laisse libre de découvrir le camp. Je dois m'occuper de d'autres affaires importantes"
                                    p "Ok, merci pour votre amaibilité..."
                                    a "Anja, je m'appelle Anja"
                                    p "Förtrollad ! Enchanté Anja !"
                                    a "A plus tard !"

                                    p "Alors Sven, qu'est ce que t'en penses d'ici ?"
                                    s "Je suis content qu'on est réussit à trouver des gens. Même si ça n'a pas l'air d'etre la grande forme, je me sens déja un peu mieux ici."
                                    p "Je suis content de l'entendre, on est mieux qu'ici que seul dans la forêt à mon avis."
                                    #donner ou non de la nourriture
                                        Oui : 
                                            p "Tiens Sven tu en a besoin."
                                            s "Merci papa"
                                            p "On a besoin de force pour ce qui va nous arriver."

                                    s "Farbror ! Oncle Viggo !"
                                    p "Quoi ?"
                                    v "Ca me fait tellement plaisir de te voir la Sven ! Qu'est ce que tu as grandi !"
                                    s "Viggo, voici [p_name], il s'est occupé de moi depuis tout ce temps."
                                    v "Qui êtes vous ?"
                                    p "Je suis un simple survivant. Au début de...tout ça, j'ai trouvé Sven seul dans sa cabane dans les bois alors que je passais par là pour trouver des ressources."
                                    p "Et puis il était si jeune, si faible, que j'était obliger dans l'accompagné avec moi."
                                    v "C'est vrai qu'il s'est occupé de toi Sven ?"
                                    s "Oui, oncle !"
                                    v "Tu as l'air si fragile, si maigre."
                                    p "Oui, on n'a eu pas mal de problèmes pendant la route, ça a été difficile de trouver assez de ressource pour nous deux mais on est finalement là."
                                    v "Méfie toi des inconnus Sven, cette personne peut etre très dangereux."
                                    p "Qu'est ce que vous dites là ?"
                                    v "Sven, je n'ai pas confiance en cet homme, les gens sont étrange ces temps ci et peuvent se changer en un rien de temps."
                                    s "Nan, je te jure Oncle, [p_name] est vraiment gentil, il m'a aidé tout ce temps."
                                    s "De toute façon, on a une bonne nouvelle, on va rester ici avec toi. [p_name] a prévu de rester ici quelques temps."
                                    p "En parlant de ça Sven, j'ai bien réfléchi et je pense que l'on doit vraiment se rendre à Luluea. On doit absolument tenter d'aller là bas, en voyant se camp, je suis en train de plus en plus me dire que l'on est pas forcément dans le camp qui va le plus durée."
                                    s "Mais on est bien ici, et puis il y a Viggo, je ne peux pa partir sans lui !"
                                    p "Je suis désolé Sven, mais j'ai vraiment un mauvais pressentiment avec cet endroit. Je ne pense pas qu'on ait réellement le choix."
                                    s "Et Viggo alors ?"
                                    p "Je suis désolé Sven, mais on peut pas le prendre avec nous, il nous ralentirait et nous voudrais probblement pas sortir d'ici, il n'a pas l'air d'avoir le physique adéquat pour rejoindre Lulea."
                                    p "Je suis désolé Sven mais il faut que tu fasse un choix, soit ici avec Viggo soit avec moi à Lulea. Chosit !"
                                    s "..."
                                    #choix : rester - partir avec
                                        Rester :
                                                s "Je suis désolé [p_name] mais je préfère rester avec Viggo. J'en ai marre de partir tous les matins à la recherche d'un paradis que l'on trouveras jamais. Je suis fattiué de tout ça. Je n'ai plus envie, je n'en ai plus la force. Désolé [p_name]."
                                                #choix rester avec eux - partir quand même
                                                        Rester :
                                                                p "Je préfère rester avec toi même si tu préfère rester ici."
                                                                p "Dès que je t'ai vu la première fois je me suis dis que j'allais de protéger jusqu'à ma mort et j'ai pas envie de m'arreter maintenant."
                                                                s "Super Viggo et [p_name] réunis."
                                                                p "Je vraiment peur de ce qui risque de se passer..."
                                                                #image de guerre avec le camp totalement détruit avec le cadavre de Viggo, de Sven et de pname
                                                        Partir :
                                                                p "Bon, ça se finit aujourd'hui. Je suis triste que ça se finisse comme ça mais c'est ton choix et je le respecte. Bonne chance, Sven. Prenez bien soin de lui, Viggo. Adieu Sven !"
                                                                #########################
                                        Partir :
                                                s "Désolé Viggo mais je dois partir avec [p_name]. J'ai très confiance en lui et il m'a traitée de la meilleure manière qu'il a pu."
                                                v "Sache que tu fais le mauvais choix Sven, tu ne peux pas faire confiance à des inconnus surtout par ces temps ci."
                                                s "Mais ce n'est pas un inconnu Viggo, c'est mon père."
                                                p "Allons y Sven, il faut qu'on se dépche avant qu'il n'y arrive quelque chose."

                                                #image seuls dans une foret
                                                p "Pour se rendre à Lulea, il faut qu'on traverse la ville de Kiruna et trouver des ressources."
                                                p "On a le choix entre trois lieux : le cinéma, le quartier résidentiel et le supermarché."
                                                #choix : cinema - quartier - supermarché
                                                        Quartier :
                                                                p "Allons se rendre dans le quartier, on trouveras surement des restes."

                                                                #image quartiers puis intérieur maison
                                                                p "Je viens de trouver une conserve de thon."
                                                                #choix : la garder - la manger - la donner
                                                                    La manger : 
                                                                            p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
                                                                            s "Je comprends."
                                                                    Lui donner : 
                                                                            p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
                                                                            s "Merci papa." # +1
                                                                    La garder : 
                                                                            p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
                                                                            s "Ok papa, ça me parait juste."
                                                                p "Je crois qu'on a tout fouillé, on peut s'en aller et rejoindre Lulea. Enfin !"

                                                        Cinéma :
                                                                p "On peut aller au cinéma. Les gens se ruent plus facilement dans les maisons et supermachés plutot que les cinémas."

                                                                #intérieur cinéma
                                                                s "Ouah, c'est immense !"
                                                                p "Tu n'es jamais allé au cinéma ?"
                                                                s "Ja, j'y suis déja allé mais c'était il y a longtemps et j'était très jeune. Je ne m'en souviens plus trop."
                                                                p "C'est quoi ton film préféré ?"
                                                                s "Gordon och Paddy ! Il est hyper drole, c'est l'histoire d'un détective qui est trop débile pour résoudre la moindre enquete."
                                                                p "Ca doit etre rigolo !"
                                                                s "C'est le meilleur film de tous les temps, de toute la création de l'univers. Et toi c'est quoi ton film préféré ?"
                                                                p "Midsommar à coup sur mais il est un peu trop violent pour toi, c'est pas vraiment pour les enfants."
                                                                s "Ohh."
                                                                p "Mais je te le montrerais quand tu seras plus grand. Je suis sure que tu l'adoreras."
                                                                p "..."
                                                                p "Bon allons fouiller les lieux."
                                                                s "J'ai pas l'impression qu'il y est grand chose ici."
                                                                p "Tu as peut etre raison. Au moins ça ma fait plaisir un peu du passé et de touts ces vieux souvenirs."
                                                                s "Oui moi aussi !"
                                                                p "Allez, prenons la route vers Lulea, je veux savoir ce qui s'y passe."

                                                        Supermarché :
                                                                p "On peut aller au supermaché, peut etre que des choses n'ont pas encore été volé là bas."

                                                                #image supermarché
                                                                s "C'est si vide ici."
                                                                p "Tout a déja été fouillé à mon avis."
                                                                #bruit de coup de feu (assaut)
                                                                p "Cache toi Sven !"
                                                                s "Papa j'ai peur !"
                                                                p "Ca va aller, ca va aller !"
                                                                s "Qu'est ce qu'on fait ?"
                                                                #choix : confrontation - fuite
                                                                        Confrontation : 
                                                                                p "On peut pas fuire, on est obligé de se battre."
                                                                                p "Ok, tu va te cacher et moi je vais m'en occuper avec le pistolet."
                                                                                p "Surtout, tu ne bouges pas de ta cachette, ok ?"
                                                                                s "Ok, papa."
                                                                                
                                                                                #coup de feu
                                                                                p "Ok, il en reste plus qu'un." 
                                                                                #coup de feu
                                                                                p "AHHHH"
                                                                                p "Il m'a eu."
                                                                                p "Il me faut un bandage !"
                                                                                #menu : oui / non
                                                                                Non :
                                                                                    #image mort joueur
                                                                                    #image bandit trouve l'enfant
                                                                                    #image enfant dans le camp sanguinaire ##################

                                                                                Oui :
                                                                                    p "Heureusement que j'en ai récupéré !"
                                                                                    p "Allez va mourir !"
                                                                                    #coup de feu
                                                                                    p "C'est bon, je l'ai eu."
                                                                                    p "Tu peux sortir Sven, ils sont plus là."

                                                                                    s "Ca va aller papa ?"
                                                                                    p "Oui, Sven ne t'inquiète pas. Ce n'est qu'une égratinure. C'est vraiment dangereux ici, il faut absolument qu'on trouve Lulea le plus vite possible. Aller en route !"
                                                                                    #Continue avec même label que fuite echec et fuite réussite
                                                                        Fuite :
                                                                                p "Il faut q'on s'enfuire, on ne peut pas aller à la confrontation."
                                                                                p "A trois on cours."
                                                                                p "1"
                                                                                p "2"
                                                                                p "3 GO !"
                                                                                #choix chronométré rapide
                                                                                        Echec : 
                                                                                                p "Ok, tu va te cacher et moi je vais m'en occuper avec le pistolet."
                                                                                                p "Surtout, tu ne bouges pas de ta cachette, ok ?"
                                                                                                s "Ok, papa."
                                                                                
                                                                                                #coup de feu
                                                                                                p "Ok, il en reste plus qu'un." 
                                                                                                #coup de feu
                                                                                                p "AHHHH"
                                                                                                p "Il m'a eu."
                                                                                                p "Il me faut un bandage !"
                                                                                                #menu : oui / non
                                                                                                Non :
                                                                                                        #image mort joueur
                                                                                                        #image bandit trouve l'enfant
                                                                                                        #image enfant dans le camp sanguinaire ##################

                                                                                                Oui :
                                                                                                        p "Heureusement que j'en ai récupéré !"
                                                                                                        p "Allez va mourir !"
                                                                                                        #coup de feu
                                                                                                        p "C'est bon, je l'ai eu."
                                                                                                        p "Tu peux sortir Sven, ils sont plus là."

                                                                                                        s "Ca va aller papa ?"
                                                                                                        p "Oui, Sven ne t'inquiète pas. Ce n'est qu'une égratinure. C'est vraiment dangereux ici, il faut absolument qu'on trouve Lulea le plus vite possible. Aller en route !"
                                        #Reparte vers Lulea
                                        p "On doit plus etre très loin de Lulea."
                                        s "T'es sur que c'est toujours une bonne idée papa ?"
                                        p "Je pense que c'est la meilleure que nous ayons pour l'instant."

                                        #image de la ville forteresse avec le logo de loup
                                        #donner ou non de la nourriture
                                        Oui : 
                                            p "Tiens Sven tu en a besoin."
                                            s "Merci papa"
                                            p "On a besoin de force pour ce qui va nous arriver."
                                        
                                        p "T'es pret Sven ?"
                                        s "Oui papa"

                                        #image à la porte
                                        #toc toc
                                        g "Qui êtes vous ?"
                                        p "On est simplement des survivants. On ne veut faire de mal à personne. J'ai entendu dire qu'il y a avait un camp ici et nous vouons seulement nous joindre à vous. Nous sommes prets à travailler énormément pour gagner une place dans votre groupe. Nous ne sommes pas malades, nous sommes à l'aise physiquement. Mon fils est très oéissant et ne vous causera aucun problème."
                                        g "Bien, savez vous qui nous sommes ?"
                                        p "Je n'en sais que très peu à votre sujet."
                                        g "Avez vous déja vu notre symbole"
                                        #non - oui
                                                Non :
                                                        p "Non c'est la première fois."
                                                        g "Et bien il faudrait que l'on le montre davantage..."
                                                        g "Nous sommes les Sköll. En hommage au dieu, grand dévoreur du Soleil."
                                                        g "Savez vous ce que ça implique de nous rejoindre ?"
                                                        g "Nous ne voulons que les meilleurs. Si vous ne faites pas partis des meilleurs, on vous fait disparaitre, c'est compris ?"
                                                                        



















                                    


                                    

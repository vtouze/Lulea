define p = Character("[p_name]")
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


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
"""
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
    show snow1
    show snow2
    play music "audio/backgroundMusic.mp3" loop
    $ p_name = renpy.input("What's your name?", length = 20)
    #show image bivouac dans une foret enneigé
    #show image intérieur du bivouac --> enfant dos au père
    p "Hej fiston ! Il faut qu'on avance, on est plus très loin de Lulea."
    s "Hmm ! J'ai tellement froid. J'ai plus la force."
    p "Je sais Sven. C'est très complqiué en ce moment mais il faut absolument qu'on aille à Lulea. C'est notre seule chance d'enfin pouvoir vivre en paix, de vivre plutot que de survivre."
    p "Allez ! Allons y !"
    #Sort du bivouac avec Sven avec une carte
    p "On devrait passer par le sud, c'est par là bas."

    #image seules dans la foret à marcher
    #image d'une vieille station essence
    p "Regarde ! Une station essence ! Il y aura peut etre des choses à récupérer."
    p "Elle est vraiment en ruine par contre."
    s "Tu crois qu'on arrivera à trouver quelque chose ?"
    p "Il le faut !"

    #entre dans la station
    #image choix entre l'arrière boutique, la boutique ou la caisse
    menu:
        "Arrière boutique":
            jump backStore
        
        "Boutique":
            jump store
        
        "Caisse":
            jump cashRegister
label backStore:
    p "J'ai pas l'impression qu'il y est grand chose..."
    s "Papa, j'ai trouvé quelque chose !"
    s "Je crois que c'est une sorte de ration ! Elle a vraiment l'air vieille"
    p "Super, Sven !"
    #Choix : la manger, lui donner, la garder
    menu:
        "La manger":
            jump eat1
        "Donner à Sven":
            jump giveS1
        "La garder":
            jump keep1
label eat1:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump firstShot

label giveS1:
    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
    s "Merci papa." # +1    
    jump firstShot


label keep1:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
    s "Ok papa, ça me parait juste."    
    jump firstShot


label store: 
    p "J'ai l'impression que tout a été dévalisé. Ca ne m'étonne pas vraiment."
    s "Papa, viens"
    p "Qu'est ce qu'il y a ?"
    p "Oh, c'est tragique. Il n'a pas l'air d'avoir grand chose sur lui."
    s "Regarde Papa, il y a une sorte de petit écusson de loup. T'as une idée de ce que sa pourrait etre ?"
    p "Je n'en ai auccune idée, c'est la première fois que je le vois."
    jump firstShot

label cashRegister:
    p "Tout est completement désolé ici, je ne pense pas que fouiller la caisse soit grandement utile."
    s "Essaye peut etre les tiroirs on ne sait jamais."
    p "Bra ! Bien joué Sven ! Je crois que j'ai trouver un bandage. Ca nous saura peut etre utile plus tard."
    jump firstShot

label firstShot:
    play sound "audio/shotFire2.mp3"
    s "C'était quoi ça, papa ?"
    p "C'est surement un coup de feu, au nord de la ville"
    s "Qu'est ce qu'on fait ?"
    menu:
        "S'éloigner du bruit":
            jump distanceNoise
        "Rejoindre le bruit":
            jump joinNoise

label distanceNoise:
    p "Viens Sven ! On va essayer de se réfugier dans le quartier pavillonaire."
    #passe par une ruelle avec le logo loup et un texte écrit "C'est ainsi que finissent les parasites" --> "Så här hamnar parasiter"
    s "Pourquoi ils ont fait ça papa ?"
    p "Je crois qu'il faut préférer ne jamais les rencontrer."
    p "Aller viens, on va se réfugier dans cette maison le temps que ça se calme."
    jump house

label joinNoise:
    p "Aller viens Sven, il faut qu'on aille voir."
    s "Mais Papa, c'est dangereux, ils sont armés, il y a peut etre des morts !"
    p "Sven, on a plus rien. On ne peut pas vivre éternellement comme ça. Il faut qu'on récupère des ressources, tu comprends ça ?"
    s "Oui, papa"
    p "Aller, rejoignons cette maison, on les attendra ici."
    jump house

label house:
    #Rencontre avec les humanistes
    p "On devrait etre en sécurité ici."
    s "J'ai un mauvais pressentiment. Je ne me sens pas bien ici."
    p "Ecoute, il faut que tu te calmes, tout va bien. Je suis la pour te protéger."
    p "Allons fouillé la maison."
    #choix : cuisine - chambre
    menu:
        "Cuisine":
            jump kitchen
        "Chambre":
            jump bedroom
        "Garage":
            jump shed

label kitchen:
    p "Allons voir la cuisine. Il y aura surement de la nourriture."
    #fouille les tirois
    p "Oh, j'ai trouvé une conserve de légumes. Elle a l'air toujours bonne."
    s "J'ai tellement faim papa, je peux la prendre ?"
    #choix : la garder - la manger - la donner
    menu:
        "La manger":
            jump eat2
        "Donner à Sven":
            jump giveS2
        "La garder":
            jump keep2

label eat2:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump firstMeeting

label giveS2: 
    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
    s "Merci papa." # +1
    jump firstMeeting

label keep2:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
    s "Ok papa, ça me parait juste."
    jump firstMeeting

label bedroom:
    p "Allons voir la chambre. On pourra surement trouver quelque chose."
    #fouille les tiroirs
    p "Oh, je viens de trouver un banadage. Ca pourra toujours etre utile."
    jump firstMeeting

label shed:
    p "J'ai pas l'impression qu'il y est grand chose."
    p "Juste de simples babioles sans valeur."
    s "Oh un jouet ! Papa regarde !"
    p "Non pas le temps Sven. On peut pas le prendre."
    jump firstMeeting

label firstMeeting:
    p "Maintenant, il nous suffit seulement d'attendre encore un peu."
    play sound "audio/reload.mp3"
    a "Qui êtes vous ?"
    p "Doucement Sven, tout va bien se passer"
    p "On...On est simplement des survivants comme vous."
    a "Qu'est ce qui vous amène ici ?"
    p "On ne fait que passer."
    a "Où voulez vous aller ?"
    #choix : mentir - avouer
    menu:
        "Mentir":
            jump lie1
        "Dire la vérité":
            jump truth1

label lie1:
    p "Je vous les dis, on ne fait que passer. On veut simplement trouver un abris, un groupe, un endroit où vivre en paix"
    a "Vous savez, il y a un groupe très dangereux qui rodent dans les parages. Ils s'appellent les Sköll. Je sais pas si vous en avez déja entendu parler mais ce sont des vrais tyrans. Ils n'ont aucune pitié. Ils sont simplement égoiste et sont pret à faire des guerres à n'importe qui pour récupérer ne serait ce qu'une infime partie de ressources. Ce sont juste des sanguinaires pret à tout pour survivre."
    a "Ils controlent absolument toute la zone, toute la région. Ils font peur à tous les groupes avoisinants, ils répendant la terreur sur toute ces terres. On est les seuls a vraiment leur faire tete mais c'est de plus en plus compliqué chaque jour de se battre contre eux. C'est une véritable armée bien organisée. Et nous, nous sommes de plus en plus vulnérable. On ne peut pas les laisser faire et on est les seuls à pouvoir le faire."
    jump proposal

label truth1:
    p "On veut se rendre à Lulea. Apparamment ils ont réussi à reconstruire un village, tout le monde y vit en paix."
    a "Ah ! Lulea ! Quel mensonge. Je ne sais pas où est ce que vous avez entendu ça mais ce sont des vrais tyrans. Ils n'ont aucune pitié. Ils sont simplement égoiste et sont près à faire des guerres à n'importe qui pour récupérer un infime partie de ressource. Ce sont juste des anguianires pret à tout. Croyez moi, vous n'aver pas envie d'aller là-bas"
    a "Vous avez vu leur logo, un loup affamé. Ils en sont fiers. Ils le mettent partout pour faire peur aux groupes avoisinants. Et ils y arrivent. On est les seuls a vraiment leur faire tête mais c'est de plus compliqué chaque de jour de se battre conntre eux. C'est une véritable armée bien orgnaisée. Et nous on est de plus en plus vulnérable. On ne peut pas les laisser faire et on est les seul à pouvoir le faire."
    jump proposal

label proposal:
    p "Vous me demandez de vous rejoindre là ?"
    a "Vous vous dites surement que vous vous en foutez de tout ce qui se passe ici mais depuis que vous etes arrivés ici. Vous etes constamment survéillé et vous ne pouvez plus sortir d'ici. Ils controlent les frontières de cette région et sont comme les prédateurs attendant gentiment leur proies de bien vouloir se présenter sous leurs yeux."
    a "Vous etes fichus ici, comme nous, comme nous tous. Vous ne pouvez plus rien faire, vous comprenez ? Vous devez absolument vous joindre à nous à moins que vous etes pret à sacrifier votre fils."
    #choix : ne rien dire - dire que ce n'est pas votre fils (chronométré)
    menu:
        "Dire que ce n'est pas votre fils":
            jump tellNotMySon
        "Ne rien dire":
            jump proposal2

label tellNotMySon:
    p "Ce n'est pas mon fils. C'est simplement un enfant que j'ai trouvé sur ma route. J'essaie de le protéger comme je peux."
    a "Ok, ça n'a pas vraiment d'immportance"
    jump proposal2

label proposal2:
    a "Alors, etes vous pret à nous rejoindre le temps de se battre contre eux, je peux vous amener à notre camp, si vous le voulez ?"
    #choix : les rejoindre - rester seuls
    menu:
        "Rester seuls":
            jump stayAlone1
        "Les rejoindre":
            jump joinThem1

label stayAlone1:
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
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    #Game Over Screen "Fin" --> bouton retour au menu principal

label joinThem1:
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
    menu:
        "Donner de la nourriture à Sven":
            jump giveS3
        "Ne rien faire":
            jump upplystCamp

label giveS3:
    p "Tiens Sven tu en a besoin."
    s "Merci papa"
    p "On a besoin de force pour ce qui va nous arriver."
    jump upplystCamp

label upplystCamp:
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
    menu:
        "Rester au camp":
            jump svenStayAtCamp
        "Partir avec [p_name]":
            jump leaveWithPlayer

label svenStayAtCamp:
    s "Je suis désolé [p_name] mais je préfère rester avec Viggo. J'en ai marre de partir tous les matins à la recherche d'un paradis que l'on trouveras jamais. Je suis fattiué de tout ça. Je n'ai plus envie, je n'en ai plus la force. Désolé [p_name]."
    #choix rester avec eux - partir quand même
    menu:
        "Rester au camp avec Sven":
            jump stayAtCampWithSven
        
        "Partir sans Sven":
            jump leaveWithoutSven

label stayAtCampWithSven:
    p "Je préfère rester avec toi même si tu préfère rester ici."
    p "Dès que je t'ai vu la première fois je me suis dis que j'allais de protéger jusqu'à ma mort et j'ai pas envie de m'arreter maintenant."
    s "Super Viggo et [p_name] réunis."
    p "Je vraiment peur de ce qui risque de se passer..."
    #image de guerre avec le camp totalement détruit avec le cadavre de Viggo, de Sven et de pname

label leaveWithoutSven:
    p "Bon, ça se finit aujourd'hui. Je suis triste que ça se finisse comme ça mais c'est ton choix et je le respecte. Bonne chance, Sven. Prenez bien soin de lui, Viggo. Adieu Sven !"
    #########################
                                                                
    #image seul dans la foret
    p "Bon , pour ce rendre à Lulea, il faut que je traverse la ville de Kiruna pour trouver des ressources."
    p "J'ai le choix entre deux lieux : le quartier pavillonaire ou le supermarché."
    #choix : quartier - supermarché
    menu:
        "Se rendre au quartier":
            jump neighborhoodAlone
        
        "Se rendre au supermarché":
            jump supermarketAlone

label neighborhoodAlone:
    p "Allons se rendre dans le quartier pavillonaire, je trouverais surement des restes."

    #image intérieur maison
    p "Oh, je viens de trouver quelque chose, je crois que c'est une conserve de thon. C'est mieux que rien."
    #choix : la garder - la manger
    menu:
        "La manger":
            jump eat3
        "La garder":
            jump keep3

label eat3:
    p "Je crois que j'ai bien besoin de manger. Avec tout ce que j'ai donné à Sven sans rien avoir en retour, je pense que je peux me permettre."
    jump endNeighborhoodAlone

label keep3:
    p "Je pense que ça serait mieux de la garder. On ne sait jamais ce qui peut se passer."
    jump endNeighborhoodAlone

label endNeighborhoodAlone:
    p "Je pense que j'ai tout fouillé ici. Je peux essayer de me rendre à Lulea maintenant."
    jump endSituationAlone

label supermarketAlone:
    p "Je peux peut etre tenter d'aller au supermarché, peut etre tout n'a pas été encore volé."
                                                                                        
    #image supermarché
    p "Tout est si vide ici."
    p "Tout a déja été fouillé à mon avis."
    play sound "audio/shotFireMultiple.wav"
    p "Oh putain des autres survivants !"
    p "Qu'est ce que je fait ?"
    #choix : confrontation - fuite
    menu:
        "Aller à la confrontation":
            jump confrontationAlone
        "Fuire":
            jump fleeAlone

label confrontationAlone:
    p "Je peut pas fuire, je suis obligé de me battre."
    p "Ok, je vais m'en occuper avec mon pistolet."
                                                                                
    play sound "audio/fireShot.mp3"
    p "Ok, il en reste plus qu'un." 
    play sound "audio/fireShot.mp3"
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    #menu : oui / non
    menu:
        "Utiliser un bandage":
            jump bandageAlone
        "Ne rien faire":
            jump noBandageAlone

label noBandageAlone:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    #image mort joueur ##################

label bandageAlone:
    p "Heureusement que j'en ai récupéré !"
    p "Allez va mourir !"
    play sound "audio/fireShot.mp3"
    p "C'est bon, je l'ai eu."
    p "Putain il m'a bien touché. C'est vraiment dangereux ici, il faut absolument que je trouve Lulea le plus vite possible. Aller [p_name], c'est presque fini !"
    #Continue avec même label que fuite echec et fuite réussite
    jump endSituationAlone
label fleeAlone:
    p "Il faut que je tente de m'enfuir, je ne peut pas aller à la confrontation."
    p "A trois je cours."
    p "1"
    p "2"
    p "3 GO !"
    #choix chronométré rapide
    menu:
        "Courir":
            jump endSituationAlone
        "Ne pas courir":
            jump failureEndSupermarketAlone

label failureEndSupermarketAlone:
    p "Putain, ils sont vraiment à l'affut. Je suis obliger maintenant d'aller à la confrontation."                                                                                
    play sound "audio/fireShot.mp3"
    p "Ok, il en reste plus qu'un." 
    play sound "audio/fireShot.mp3"
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    #menu : oui / non
    menu:
        "Utiliser un bandage":
            jump bandageAlone
        "Ne rien faire":
            jump noBandageAlone

label endSituationAlone:
    #Repart seul vers Lulea                                                                             
    p "Je doit plus etre très loin de Lulea."
    p "Même si c'est surement pas un paradis, je pense que c'est la meilleure option que j'ai pour l'instant."

    #image de la ville forteresse avec le logo de loup
    #donner ou non de la nourriture"

    #image à la porte
    play sound "audio/knock.mp3"
    g "Qui êtes vous ?"
    p "Je suis simplement un survivant. Je ne veut faire de mal à personne. J'ai entendu dire qu'il y a avait un camp ici et je veut seulement me joindre à vous. Je suis pret à travailler énormément pour gagner une place dans votre groupe. Je ne suis pas malade et je suis à l'aise physiquement."
    g "Bien, savez vous qui nous sommes ?"
    p "Je n'en sais que très peu à votre sujet."
    g "Avez vous déja vu notre symbole"
    #non - oui
    menu :
        "Non":
            jump noSymbolAlone
        "Oui":
            jump symboleAlone

label noSymbolAlone:  
    p "Non c'est la première fois."
    g "Et bien il faudrait que l'on le montre davantage..."
    g "Nous sommes les Sköll. En hommage au dieu, grand dévoreur du Soleil."
    g "Savez vous ce que ça implique de nous rejoindre ?"
    g "Nous ne voulons que les meilleurs. Si vous ne faites pas partis des meilleurs, on vous fait disparaitre, c'est compris ?"
    p "Je comprends."
    jump proposalAlone

label symboleAlone:
    p "Oui je l'ai déja vu quelque fois."
    g "Le grand Sköll, dévoreur du Soleil nous protège de la désolation et nous guide ces temps ci."
    g "Vous savez, on n'est pas ici pour devenir amis-amis avec tout le monde. Nous voulons simplement survivre et sommes pret à tout pour arriver à nos objectifs, compris ?"
    p "Je comprends."
    jump proposalAlone

label proposalAlone:
    g "Alors, etes vous toujours pret à nous rejoindre ?"
    #choix : les rejoindre - rester seul - repartir chez les Upplyst
    menu:
        "Les rejoindre":
            jump joinThemAlone
        
        "Repartir chez les Upplyst":
            jump restartUpplystAlone
        
        "Rester seul":
            jump endStayAlone1
        
label joinThemAlone:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "C'est ce dont j'ai toujours rever. Je peux enfin rejoindre ce groupe, après tout ce temps à errer, à etre proche de la mort chaque seconde de mon existence."
    #image joueur prisonier dans le camp
    #image sven meurt dans la guerre dans le camp humaniste

label restartUpplystAlone:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je crois qu'il serait mieux de rejoindre les Upplyst."
    p "Je pense que rejoindre ce groupe peut etre très dangereux. Je ne sais pas si je peux vraiment faire confiance à ces gens là."
    #image seul dans la foret
    #image joueur camp humanite
    #image joueur mort guerre humaniste

label endStayAlone1:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "J'en ai marre de tout ça. Je n'en peux plus de cette guerre sans queue ni tête. Je ne suis pas sur que j'ai vraiment quelque chose à jouer là dedans."
    p "Je pense qu'il serait que je part de tout ça et que je retente l'aventure tout seul. Comme quand tout ceci à commencé."
    p "Je ne sais pas encore où est ce que je vais aller mais c'est indéniablement la meilleure option que j'ai."
    #image joueur seul dans la foret
    #image joueur meurt dans le bivouac

label leaveWithPlayer:
    s "Désolé Viggo mais je dois partir avec [p_name]. J'ai très confiance en lui et il m'a traitée de la meilleure manière qu'il a pu."
    v "Sache que tu fais le mauvais choix Sven, tu ne peux pas faire confiance à des inconnus surtout par ces temps ci."
    s "Mais ce n'est pas un inconnu Viggo, c'est mon père."
    p "Allons y Sven, il faut qu'on se dépeche avant qu'il n'y arrive quelque chose."

    #image seuls dans une foret
    p "Pour se rendre à Lulea, il faut qu'on traverse la ville de Kiruna et trouver des ressources."
    p "On a le choix entre trois lieux : le cinéma, le quartier résidentiel et le supermarché."
    #choix : cinema - quartier - supermarché
    menu:
        "Se rendre au quartier":
            jump neighborhood
        
        "Se rendre au supermarché":
            jump supermarket
        
        "Se rendre au cinéma":
            jump movieTheater

label neighborhood:
    p "Allons se rendre dans le quartier, on trouveras surement des restes."

    #image quartiers puis intérieur maison
    p "Je viens de trouver une conserve de thon."
    #choix : la garder - la manger - la donner
    menu:
        "La manger":
            jump eat4
        "La garder":
            jump keep4
        "La donner":
            jump giveS4

label eat4:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dure pour moi. Je préférais la prendre. Sans etre en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump endNeighborhood

label giveS4:
    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
    s "Merci papa." # +1
    jump endNeighborhood

label keep4:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer"
    s "Ok papa, ça me parait juste."
    jump endNeighborhood

label endNeighborhood:
    p "Je crois qu'on a tout fouillé, on peut s'en aller et rejoindre Lulea. Enfin !"
    jump endSituation

label movieTheater:
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
    jump endSituation

label supermarket:
    p "On peut aller au supermaché, peut etre que des choses n'ont pas encore été volé là bas."

    #image supermarché
    s "C'est si vide ici."
    p "Tout a déja été fouillé à mon avis."
    play sound "audio/shotFireMultiple.wav"
    p "Cache toi Sven !"
    s "Papa j'ai peur !"
    p "Ca va aller, ca va aller !"
    s "Qu'est ce qu'on fait ?"
    #choix : confrontation - fuite
    menu:
        "Aller à la confrontation":
            jump confrontation
        "Fuire":
            jump flee

label confrontation:
    p "On peut pas fuire, on est obligé de se battre."
    p "Ok, tu va te cacher et moi je vais m'en occuper avec le pistolet."
    p "Surtout, tu ne bouges pas de ta cachette, ok ?"
    s "Ok, papa."
                                                                                
    play sound "audio/fireShot.mp3"
    p "Ok, il en reste plus qu'un." 
    play sound "audio/fireShot.mp3"
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    #menu : oui / non
    menu:
        "Utiliser un bandage":
            jump bandage
        "Ne rien faire":
            jump noBandage

label noBandage: 
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    #image mort joueur
    #image bandit trouve l'enfant
    #image enfant dans le camp sanguinaire ##################

label bandage:
    p "Heureusement que j'en ai récupéré !"
    p "Allez va mourir !"
    play sound "audio/fireShot.mp3"
    p "C'est bon, je l'ai eu."
    p "Tu peux sortir Sven, ils sont plus là."

    s "Ca va aller papa ?"
    p "Oui, Sven ne t'inquiète pas. Ce n'est qu'une égratinure. C'est vraiment dangereux ici, il faut absolument qu'on trouve Lulea le plus vite possible. Aller en route !"
    #Continue avec même label que fuite echec et fuite réussite
    jump endSituation

label flee:
    p "Il faut q'on s'enfuire, on ne peut pas aller à la confrontation."
    p "A trois on cours."
    p "1"
    p "2"
    p "3 GO !"
    #choix chronométré rapide
    menu:
        "Courir":
            jump endSituation
        "Ne pas courir":
            jump failureEndSupermarket

label failureEndSupermarket:
    p "Ok, tu va te cacher et moi je vais m'en occuper avec le pistolet."
    p "Surtout, tu ne bouges pas de ta cachette, ok ?"
    s "Ok, papa."
                                                                                
    play sound "audio/fireShot.mp3"
    p "Ok, il en reste plus qu'un." 
    play sound "audio/fireShot.mp3"
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    #menu : oui / non
    menu:
        "Utiliser un bandage":
            jump bandage
        "Ne rien faire":
            jump noBandage

label endSituation:
    #Reparte vers Lulea
    p "On doit plus etre très loin de Lulea."
    s "T'es sur que c'est toujours une bonne idée papa ?"
    p "Je pense que c'est la meilleure que nous ayons pour l'instant."

    #image de la ville forteresse avec le logo de loup
    #donner ou non de la nourriture
    menu :
        "Donner de la nourriture à Sven":
            jump giveS5
        "Ne rien faire":
            jump secondMeeting

label giveS5:
    p "Tiens Sven tu en a besoin."
    s "Merci papa"
    p "On a besoin de force pour ce qui va nous arriver."
    jump secondMeeting

label secondMeeting:    
    p "T'es pret Sven ?"
    s "Oui papa"

    #image à la porte
    play sound "audio/knock.mp3"
    g "Qui êtes vous ?"
    p "On est simplement des survivants. On ne veut faire de mal à personne. J'ai entendu dire qu'il y a avait un camp ici et nous vouons seulement nous joindre à vous. Nous sommes prets à travailler énormément pour gagner une place dans votre groupe. Nous ne sommes pas malades, nous sommes à l'aise physiquement. Mon fils est très oéissant et ne vous causera aucun problème."
    g "Bien, savez vous qui nous sommes ?"
    p "Je n'en sais que très peu à votre sujet."
    g "Avez vous déja vu notre symbole"
    #non - oui
    menu:
        "Non":
            jump noSymbol
        "Oui":
            jump symbol

label noSymbol:
    p "Non c'est la première fois."
    g "Et bien il faudrait que l'on le montre davantage..."
    g "Nous sommes les Sköll. En hommage au dieu, grand dévoreur du Soleil."
    g "Savez vous ce que ça implique de nous rejoindre ?"
    g "Nous ne voulons que les meilleurs. Si vous ne faites pas partis des meilleurs, on vous fait disparaitre, c'est compris ?"
    p "Je comprends."
    jump proposal4

label symbol:
    p "Oui je l'ai déja vu quelque fois."
    g "Le grand Sköll, dévoreur du Soleil nous protège de la désolation et nous guide ces temps ci."
    g "Vous savez, on n'est pas ici pour devenir amis-amis avec tout le monde. Nous voulons simplement survivre et sommes pret à tout pour arriver à nos objectifs, compris ?"
    p "Je comprends."
    jump proposal4

label proposal4:
    g "Cependant, nous ne pouvons prendre qu'une seule personne ici. Nous voulons s'assurer de chaque entrée dans ce groupe et les former comme il le faut. Nous n'avons pas le temps de s'occuper de deux tetes fragiles."
    p "Vous etes surs ? On peut tout les deux vous aider grandement on à le sens de..."
    g "La ferme et choisissez ! Je n'ai pas de temps à perdre avec vous !"
    #choix : abandonner Sven - amener Sven au camp - repartir chez humanistes - rester seuls
    menu:
        "Les rejoindre et abandonner Sven":
            jump abandonSven
        
        "Forcer Sven à les rejoindre":
            jump svenJoinThem
        
        "Repartir chez les Upplyst":
            jump restartUpplyst
        
        "Rester seuls":
            jump endStayAlone2

label abandonSven:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je suis désolé Sven mais j'ai fait tous ce que j'ai pu pour te protéger jusque là. J'ai fait énormément de sacrifice pour ta survie mais... j'en ai peux plus. Je suis fatigué Sven. Je ne veux plus survivre comme ça."
    p "Lulea a toujours été mon objectif avant même que je te rencontre et je n'ai pas envie de le laisser filer."
    s "Tu veux m'abandonner ici, tout seul. Mais je ne survivrais jamais sans toi."
    p "Ne te sous estime pas Sven. Tu es capable de bien plus. Je l'ai vu tout ce temps. Tu as beaucoup grandi et j'en suis fuire."
    s "Mais qu'est ce que u racontes ? Je ne peux rien faire sans toi. Je ne peux pas survivre comme ça."
    p "Je suis désolé Sven mais je ne peux plus."
    p "Adieu Sven !"
    #image Sven seul dans la foret
    #image joueur prisonier dans le camp
    #image sven chez les humaniste
    #image sven meurt dans la guerre dans le camp humaniste

label svenJoinThem:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Sven, je pense qu'il est temps de se séparer. Mon objecctif a toujours été de te protéger et je crois que ma mission s'arrete ici. Rejoinds les, tu auras une vie bien meilleure, j'en suis sur."
    s "Mais papa, je ne peux rien faire sans toi, je ne peux pas survivre sans toi."
    p "Tu ne seras plus tout seul Sven, tu vivras mieux, bien mieux."
    s "Mais je ne veux pas ! Je veux rester avec toi papa ! Je m'en fiche de rester avec des inconnus, je veux continuer avec toi !"
    p "C'est difficle Sven mais on ne peut plus vivre comme ça. Ces derniers temps ont été compliqué et nous ne pouvons pas survivre comme ça très longtemps. On a pas le choix, il faut que tu ailles là bas."
    s "Et toi qu'est ce que tu vas faire ?"
    p "Ne t'inquiète pas pour moi, je m'en sortirais. Je réussirai toujours à m'en sortir comme on l'a toujours fait, d'accord ?"
    s "Oui papa."
    p "Au revoir Sven, tu me manqueras beaucoup !"
    s "Moi aussi"
    s "Papa."
    #image joueur seul dans la foret
    #image sven prisonier dans le camp
    #image joueur mort seul dans le bivouac

label restartUpplyst:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je crois qu'il serait mieux que l'on rejoingne les Upplyst Sven."
    s "Mais papa, c'était ton objectif de venir ici, tu avais dis que c'était comme un petit paradis."
    p "Je sais Sven, mais rejoindre ce groupe peut etre très dangereux. Je ne sais pas s'il on peut vraiment faire confiance à ces gens là."
    p "Et, j'ai trop peur de te perdre, mon objectif est de te protéger et il ne va pas s'arreter aujourd'hui."
    s "On pourra rejoindre oncle Viggo alors ?"
    p "Oui Sven, on pourra rejoindre Viggo."
    #image sven et jour dans la foret
    #rejoingne le camp humaniste
    #image morts pendant la guerre dans le camp humaniste

label endStayAlone2:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je n'ai marre de tout ça Sven. Je n'en peux plus de cette guerre sans queue ni tête. Je ne crois pas que l'on est vraiment quelque chose à jouer."
    p "Je pense qu'il serait mieux qu'on part de tout ça et qu'on tente l'avanture à deux. Comme on l'a toujours fait."
    s "Mais où est ce que va aller alors ?"
    p "Je ne sais pas encore mais ça sera bien mieux qu'ici, tu ne trouves pas ?"
    s "Je ne sais pas, ces derniers temps ont été si compliqué que je ne sais pas si l'on peut toujours survivre comme ça."
    p "C'est notre meilleur option, Sven, crois moi."
    #image seuls dans la foret
    #image seuls dans le bivouac
    #image morts dans le bivouac

                                    


                                    

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


image gasStation = "gasStation.png"
image playerProfile = "playerProfile.png"
image sven = "sven.png"
image pathForest = "pathForest.png"
image house = "house.png"
image alley = "alley.png"
image upplystCamp = "upplystCamp.png"
image upplystCampWar = "upplystCampWar.png"

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    text _("Choississez vite !") xalign 0.5 yalign 0.55 size 30 bold 1 outlines [(absolute(2), "#000", absolute(1), absolute(1))]
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.90 ysize 25 xmaximum 300 at alpha_dissolve

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
    $ health = 100

label start:
    $ food = 0
    $ foodGiven = 0
    $ heal = 0
    with dissolve
    show snow1
    show snow2
    play music "audio/backgroundMusic.mp3" loop
    $ p_name = renpy.input("Quel est votre prénom ?", length = 20)
    scene campfire with dissolve
    show snow1
    show snow2
    p "Hej fiston ! Il faut qu'on avance, on est plus très loin de Luleå."
    s "Hmm ! J'ai tellement froid. J'ai plus la force."
    p "Je sais Sven. C'est très compliqué en ce moment mais, il faut absolument qu'on aille à Luleå. C'est notre seule chance d'enfin pouvoir vivre en paix, de vivre plutôt que de survivre."
    p "Allez ! Allons y !"
    p "On devrait passer par le sud, c'est par là-bas."

    scene pathForest with dissolve
    show snow1
    show snow2
    hide campfire
    p "..."
    scene gasStation with dissolve
    show snow1
    show snow2
    hide pathForest

    p "Regarde ! Une station essence ! Il y aura peut être des choses à récupérer."
    p "Elle est vraiment en ruine par contre."
    s "Tu crois qu'on arrivera à trouver quelque chose ?"
    p "Il le faut !"

    menu:
        "Arrière boutique":
            jump backStore
        
        "Boutique":
            jump store
        
        "Caisse":
            jump cashRegister
label backStore:
    p "Je n'ai pas l'impression qu'il y est grand-chose..."
    s "Papa, j'ai trouvé quelque chose !"
    s "Je crois que c'est une sorte de ration ! Elle a vraiment l'air vieille."
    play sound "audio/fillBag.mp3"
    p "Super, Sven !"
    $ food += 1
    menu:
        "La manger":
            jump eat1
        "Donner à Sven":
            jump giveS1
        "La garder":
            jump keep1
label eat1:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dur pour moi. Je préférais la prendre. Sans être en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump firstShot

label giveS1:
    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
    s "Merci papa."
    $ foodGiven += 1
    $ food -= 1   
    jump firstShot


label keep1:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer."
    s "Ok papa, ça me parait juste."    
    jump firstShot


label store: 
    p "J'ai l'impression que tout a été dévalisé. Ça ne m'étonne pas vraiment."
    s "Papa, viens !"
    p "Qu'est-ce qu'il y a ?"
    p "Oh, c'est tragique. Il n'a pas l'air d'avoir grand-chose sur lui."
    s "Regarde Papa, il y a une sorte de petit écusson de loup. T'as une idée de ce que ça pourrait être ?"
    p "Je n'en ai aucune idée, c'est la première fois que je le vois."
    s "Oh, Papa, regarde sur lui ! Une conserve !"
    p "Grym Sven ! Génial, bien joué."
    play sound "audio/fillBag.mp3"
    $ food += 1
    menu:
        "La manger":
            jump eat1
        "Donner à Sven":
            jump giveS1
        "La garder":
            jump keep1

label cashRegister:
    p "Tout est complètement désolé ici, je ne pense pas que fouiller la caisse soit grandement utile."
    s "Essaye peut être les tiroirs, on ne sait jamais."
    p "Bra ! Bien joué Sven ! Je crois que j'ai trouvé un bandage. Ça nous saura peut être utile plus tard."
    play sound "audio/fillBag.mp3"
    $ heal += 1
    jump firstShot

label firstShot:
    play sound "audio/shotFire2.mp3"
    with hpunch
    s "C'était quoi ça, papa ?"
    p "C'est sûrement un coup de feu, au nord de la ville."
    s "Qu'est-ce qu'on fait ?"
    menu:
        "S'éloigner du bruit":
            jump distanceNoise
        "Rejoindre le bruit":
            jump joinNoise

label distanceNoise:
    scene alley with dissolve
    hide gasStation
    p "Viens Sven ! On va essayer de se réfugier dans le quartier pavillonnaire."
    s "Pourquoi ils ont fait ça papa ?"
    p "Je crois qu'il faut préférer ne jamais les rencontrer."
    p "On va se réfugier dans cette maison le temps que ça se calme."
    jump house

label joinNoise:
    p "Viens Sven, il faut qu'on aille voir."
    s "Mais Papa, c'est dangereux, ils sont armés, il y a peut-être des morts !"
    p "Sven, on n'a plus rien. On ne peut pas vivre éternellement comme ça. Il faut qu'on récupère des ressources, tu comprends ça ?"
    s "Oui, papa."
    p "Rejoignons cette maison, on les attendra ici."
    jump house

label house:
    scene house with dissolve
    hide alley
    p "On devrait être en sécurité ici."
    s "J'ai un mauvais pressentiment. Je ne me sens pas bien ici."
    p "Écoute, il faut que tu te calmes, tout va bien. Je suis là pour te protéger."
    p "Allons fouiller la maison."
    menu:
        "Cuisine":
            jump kitchen
        "Chambre":
            jump bedroom
        "Garage":
            jump shed

label kitchen:
    p "Allons voir la cuisine. Il y aura sûrement de la nourriture."
    p "Oh, j'ai trouvé une conserve de légumes. Elle a l'air toujours bonne."
    s "J'ai tellement faim papa, je peux la prendre ?"
    play sound "audio/fillBag.mp3"
    $ food += 1
    menu:
        "La manger":
            jump eat2
        "Donner à Sven":
            jump giveS2
        "La garder":
            jump keep2

label eat2:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver. C'est encore plus dur pour moi. Je préférais la prendre. Sans être en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump firstMeeting

label giveS2: 
    p "Tu peux la manger, Sven. Tu en a beaucoup plus besoin que moi."
    s "Merci papa."
    $ food -= 1
    $ foodGiven += 1   
    jump firstMeeting

label keep2:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer."
    s "Ok papa, ça me parait juste."
    jump firstMeeting

label bedroom:
    p "Allons voir la chambre. On pourra sûrement trouver quelque chose."
    p "Oh, je viens de trouver un bandage. Ça pourra toujours être utile."
    $ heal += 1
    play sound "audio/fillBag.mp3"
    jump firstMeeting

label shed:
    p "Je n'ai pas l'impression qu'il y ait grand-chose."
    p "Juste de simples babioles sans valeur."
    s "Oh un jouet ! Papa regarde !"
    p "Non pas le temps Sven. On ne peut pas le prendre."
    jump firstMeeting

label firstMeeting:
    p "Maintenant, il nous suffit seulement d'attendre encore un peu."
    play sound "audio/reload.mp3"
    a "Qui êtes-vous ?"
    p "Doucement Sven, tout va bien se passer."
    p "On...on est simplement des survivants comme vous."
    a "Qu'est-ce qui vous amène ici ?"
    p "On ne fait que passer."
    a "Où voulez-vous aller ?"
    menu:
        "Mentir":
            jump lie1
        "Dire la vérité":
            jump truth1

label lie1:
    p "Je vous les dis, on ne fait que passer. On veut simplement trouver un abri, un groupe, un endroit où vivre en paix."
    a "Vous savez, il y a un groupe très dangereux qui rôde dans les parages. Ils s'appellent les Sköll. Je ne sais pas si vous en avez déjà entendu parler, mais ce sont des vrais tyrans." 
    a "Ils n'ont aucune pitié. Ils sont simplement égoïstes et sont prêts à faire des guerres à n'importe qui pour récupérer ne serait ce qu'une infime partie de ressources." 
    a "Ce sont juste des sanguinaires prêts à tout pour survivre."
    a "Ils contrôlent absolument toute la zone, toute la région. Ils font peur à tous les groupes avoisinants, ils rependant la terreur sur toutes ces terres." 
    a "On est les seuls à vraiment leur faire tête, mais c'est de plus en plus compliqué chaque jour de se battre contre eux. C'est une véritable armée bien organisée. Et nous, nous sommes de plus en plus vulnérables."
    a "On ne peut pas les laisser faire et on est les seuls à pouvoir le faire."
    jump proposal

label truth1:
    p "On veut se rendre à Luleå. Apparamment, ils ont réussi à reconstruire un village, tout le monde y vit en paix."
    a "Ah ! Luleå ! Quel mensonge. Je ne sais pas où est ce que vous avez entendu ça, mais ce sont des vrais tyrans. Ils n'ont aucune pitié." 
    a "Ils sont simplement égoïstes et sont prêts à faire des guerres à n'importe qui pour récupérer une infime partie de ressource." 
    a "Ce sont juste des sanguinaires prêts à tout. Croyez-moi, vous n'avez pas envie d'aller là-bas."
    a "Vous avez vu leur logo, un loup affamé. Ils en sont fiers. Ils le mettent partout pour faire peur aux groupes avoisinants. Et ils y arrivent." 
    a "On est les seuls à vraiment leur faire tête, mais c'est de plus en plus compliqué chaque jour de se battre contre eux. C'est une véritable armée bien organisée. Et nous, nous sommes de plus en plus vulnérables." 
    a "On ne peut pas les laisser faire et on est les seuls à pouvoir le faire."
    jump proposal

label proposal:
    p "Vous me demandez de vous rejoindre là ?"
    a "Vous vous dites sûrement que vous vous en foutez de tout ce qui se passe ici, mais depuis que vous êtes arrivés ici." 
    a "Vous êtes constamment surveillé et vous ne pouvez plus sortir d'ici." 
    a "Ils contrôlent les frontières de cette région et sont comme les prédateurs attendant gentiment leurs proies de bien vouloir se présenter sous leurs yeux."
    a "Vous êtes fichus ici, comme nous, comme nous tous. Vous ne pouvez plus rien faire, vous comprenez ?" 
    a "Vous devez absolument vous joindre à nous à moins que vous êtes prêt à sacrifier votre fils."
    menu:
        "Dire que ce n'est pas votre fils":
            jump tellNotMySon
        "Ne rien dire":
            jump proposal2

label tellNotMySon:
    p "Ce n'est pas mon fils. C'est simplement un enfant que j'ai trouvé sur ma route. J'essaie de le protéger comme je peux."
    a "Ok, ça n'a pas vraiment d'importance."
    jump proposal2

label proposal2:
    a "Alors, êtes-vous prêt à nous rejoindre le temps de se battre contre eux, je peux vous amener à notre camp, si vous le voulez ?"
    menu:
        "Rester seuls":
            jump stayAlone1
        "Les rejoindre":
            jump joinThem1

label stayAlone1:
    p "Je préfère protéger Sven, je ne peux pas vous aider, je suis désolé."
    a "Vous faites une grave erreur, vous le savez ?"
    p "Peut-être, mais je n'ai pas envie de l'envoyer dans une guerre de clans sans réelle motivation et où la fin reste prévisible."
    a "Comme vous le voulez. Allez les gars, on peut y aller."

    p "Je ne pouvais pas nous laisser embarquer dans une guerre futile. On n'avait  pas le choix, tu comprends ?"
    s "Et si la femme avait raison, peut-être qu'ils nous ont déjà repérer et qu'ils nous suivent en ce moment. Et si nous ne pouvons plus sortir d'ici ?" 
    s "Et s'ils sont aussi terrifiants que la femme le disait ? Tu veux toujours qu'on les rejoigne. Je ne veux pas être méchant papa."
    p "Du calme Sven, tout va bien. On ne sait pas tout sur cette histoire. Qui te dis qu'elle disait vraiment la vérité. Ils sont en guerre, Sven." 
    p "On ne peut pas croire n'importe qui. Ils recherchaient peut-être simplement des gens naïfs perdus pour rejoindre leur cause sans qu'ils n'en aient la moindre motivation."
    p "Tout va bien. Du moment qu'on est que tous les deux. Rien ne peut nous arriver, d'accord ?" 
    p "Allez en route, le soleil se couche, il faut qu'on aille trouver un abri pour passer la nuit. Allons-y !"

    scene campfire with dissolve
    hide house
    p "Allez, on peut se poser ici."
    p "Ça va, Sven ? T'as l'air ailleurs ?"
    s "C'est juste que je pense toujours à ce que la femme a dit. Et si on avait fait le mauvais choix, et si on était déjà condamné."
    p "Mais non Sven, tout va bien, on est encore tous les deux. Et ça, c'est le plus important. Aller, il est tard allons se coucher !"

    play sound "audio/breathe.mp3"
    with hpunch
    p "Liv, c'est toi mon amour ?"
    l "Tu me manques tellement [p_name] !"
    p "Je suis si perdu sans toi. J'en ai marre de tout ça."
    p "Je ne sais pas si tous les choix que j'ai pu faire ont été raisonnable ou pas. J'ai peur d'avoir condamné la vie de ce pauvre petit garçon."
    l "Tu as de la peine, pour ce garçon ? Ce n'est même pas ton enfant. Tu nous a oubliés ? Nous, ta vraie famille, moi et Arvid ?"
    p "Non mon cœur, je ne vous oublierais jamais. Vous êtes tous pour moi. Chaque jour, chaque minute, chaque seconde, je pense à vous." 
    p "Je suis perdu sans vous. Je n'en peux plus."
    l "Tu n'en crois pas un mot. Je te vois chaque jour, à t'occuper de cet enfant minable. Tu ne veux pas te l'avouer, mais c'est trop tard. Tu ne peux rien y faire." 
    l "Rejoins-nous, ta famille, on a tellement envie de te revoir. Tu préfères cet enfant ou Arvid ? Choisit !"
    p "Bien sûr que je préfère Arvid, chérie. C'est mon enfant, c'est ce dont j'ai été le plus fier."
    l "Alors, rejoins-nous, rejoins ta femme et ton fils. On veut juste te revoir parmi nous."
    p "Reviens chéri !"
    p "Chéri, j'en peux plus je veux te revoir !"
    l "Rejoins-nous !"
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    unknown "Vous avez tenté de rejoindre votre famille or sans vous, Sven ne peut pas survivre. Vous l'avez ainsi condamné à une mort d'une horrible souffrance."
    menu:
        "Menu principal":
            return

label joinThem1:
    scene house with dissolve
    p "Je ne crois qu'on n'a pas vraiment le choix."
    a "Bienvenue, chez les Upplyst."
    a "Ok, allons-y maintenant, le soleil commence à se coucher."

    scene upplystCamp with dissolve
    hide house
    a "Nous voici au camp des Upplyst. On a eu des moments compliqués depuis la guerre avec Luleå."
    a "Je vous laisse libre de découvrir le camp. Je dois m'occuper d'autres affaires importantes."
    p "Ok, merci pour votre amabilité..."
    a "Anja, je m'appelle Anja."
    p "Förtrollad ! Enchanté Anja !"
    a "À plus tard !"

    p "Alors Sven, qu'est ce que t'en penses d'ici ?"
    s "Je suis content qu'on ait réussi à trouver des gens. Même si ça n'a pas l'air d'être la grande forme, je me sens déjà un peu mieux ici."
    p "Je suis content de l'entendre, on est mieux ici que seul dans la forêt à mon avis."
    p "Cependant, j'ai l'impression qu'il y a beaucoup plus de personnes que de ressources disponibles, je ne sais s'ils ont va pouvoir rester ici très longtemps."
    if food >= 1:
        menu:
            "Donner de la nourriture à Sven":
                jump giveS3
            "Ne rien faire":
                jump upplystCamp
    if food == 0:
        jump upplystCamp

label giveS3:
    p "Tiens Sven, tu en a besoin."
    s "Merci papa."
    p "On a besoin de force pour ce qui va nous arriver."
    $ foodGiven += 1
    jump upplystCamp

label upplystCamp:
    s "Farbror ! Oncle Viggo !"
    p "Quoi ?"
    v "Ça me fait tellement plaisir de te voir la Sven ! Qu'est-ce que tu as grandi !"
    s "Viggo, voici [p_name], il s'est occupé de moi depuis tout ce temps."
    v "Qui êtes-vous ?"
    p "Je suis un simple survivant. Au début de...tout ça, j'ai trouvé Sven seul dans sa cabane dans les bois alors que je passais par là pour trouver des ressources."
    p "Et puis il était si jeune, si faible, que j'étais obligé dans l'accompagné avec moi."
    v "C'est vrai qu'il s'est occupé de toi Sven ?"
    s "Oui, oncle !"
    v "Tu as l'air si fragile, si maigre."
    p "Oui, on n'a eu pas mal de problèmes pendant la route, ça a été difficile de trouver assez de ressource pour nous deux, mais on est finalement là."
    v "Méfie-toi des inconnus Sven, cette personne peut-être très dangereuse"
    p "Qu'est-ce que vous dites là ?"
    v "Sven, je n'ai pas confiance en cet homme, les gens sont étranges ces temps-ci et peuvent se changer en un rien de temps."
    s "Nan, je te jure Oncle, [p_name] est vraiment gentil, il m'a aidé tout ce temps."
    s "De toute façon, on a une bonne nouvelle, on va rester ici avec toi. [p_name] a prévu de rester ici quelques temps."
    p "En parlant de ça Sven, j'ai bien réfléchi et je pense que l'on doit vraiment se rendre à Luleå." 
    p "On doit absolument tenter d'aller là-bas, en voyant ce camp, je suis en train de plus en plus me dire que l'on n'est pas forcément dans le camp qui va le plus durée."
    s "Mais on est bien ici, et puis il y a Viggo, je ne peux pas partir sans lui !"
    p "Je suis désolé, Sven, mais j'ai vraiment un mauvais pressentiment avec cet endroit. Je ne pense pas qu'on ait réellement le choix."
    s "Et oncle Viggo alors ?"
    p "Je suis désolé, Sven, mais on ne peut pas le prendre avec nous, il nous ralentirait et ne voudrait probablement pas sortir d'ici." 
    p "Il n'a pas l'air d'avoir le physique adéquat pour rejoindre Luleå."
    p "Je suis désolé, Sven, mais il faut que tu fasses un choix, soit ici avec Viggo soit avec moi à Luleå. Chosit !"
    s "..."
    if foodGiven >= 1:
        jump leaveWithPlayer
    if foodGiven == 0:
        jump svenStayAtCamp

label svenStayAtCamp:
    s "Je suis désolé [p_name] mais je préfère rester avec Viggo. J'en ai marre de partir tous les matins à la recherche d'un paradis que l'on trouvera jamais." 
    s "Je suis fatigué de tout ça. Je n'ai plus envie, je n'en ai plus la force. Désolé [p_name]."
    menu:
        "Rester au camp avec Sven":
            jump stayAtCampWithSven
        
        "Partir sans Sven":
            jump leaveWithoutSven

label stayAtCampWithSven:
    p "Je préfère rester avec toi-même si tu préfères rester ici."
    p "Dès que je t'ai vu la première fois, je me suis dit que j'allais de protéger jusqu'à ma mort et je n'ai pas envie de m'arrêter maintenant."
    s "Super Viggo et [p_name] réunis."
    p "J'ai vraiment peur de ce qui risque de se passer..."
    scene upplystCampWar with dissolve
    hide upplystCamp
    unknown "À être rester avec les Upplyst, vous vous êtes trouver au mauvais endroit lors de la lourde attaque du groupe de Luleå."
    unknown "Vous avez ainsi tous péri, Viggo, Sven, vous et le reste du camp des Upplyst. Pourquoi êtes vous donc rester ici ?"
    menu:
        "Menu principal":
            return
    return

label leaveWithoutSven:
    scene upplystCamp with dissolve
    p "Bon, ça se finit aujourd'hui. Je suis triste que ça se finisse comme ça, mais c'est ton choix et je le respecte. Bonne chance, Sven. Prenez bien soin de lui, Viggo. Adieu Sven !"

    p "Bon, pour se rendre à Luleå, il faut que je traverse la ville de Kiruna pour trouver des ressources."
    p "J'ai le choix entre deux lieux : le quartier pavillonnaire ou le supermarché."
    menu:
        "Se rendre au quartier":
            jump neighborhoodAlone
        
        "Se rendre au supermarché":
            jump supermarketAlone

label neighborhoodAlone:
    p "Allons se rendre dans le quartier pavillonnaire, je trouverais sûrement des restes."

    #image intérieur maison
    p "Oh, je viens de trouver quelque chose, je crois que c'est une conserve de thon. C'est mieux que rien."
    $ food += 1
    play sound "audio/fillBag.mp3"
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
    p "Je pense que j'ai tout fouillé ici. Je peux essayer de me rendre à Luleå maintenant."
    jump endSituationAlone

label supermarketAlone:
    p "Je peux peut-être tenter d'aller au supermarché, peux être tout n'a pas été encore volé."
                                                                                        
    p "Tout est si vide ici."
    p "Tout a déjà été fouillé à mon avis."
    play sound "audio/shotFireMultiple.wav"
    with hpunch
    p "Fan ! Des autres survivants !"
    p "Qu'est-ce que je fais ?"
    menu:
        "Aller à la confrontation":
            jump confrontationAlone
        "Fuire":
            jump fleeAlone

label confrontationAlone:
    p "Je ne peux pas fuir, je suis obligé de me battre."
    p "Ok, je vais m'en occuper avec mon pistolet."
                                                                                
    play sound "audio/shotFire.mp3"
    with hpunch
    p "Ok, il en reste plus qu'un." 
    play sound "audio/shotFire.mp3"
    with hpunch
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    menu:
        "Utiliser un bandage" if heal >= 1:
            jump bandageAlone
        "Ne rien faire":
            jump noBandageAlone

label noBandageAlone:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    unknown "Vous êtes mort au combat, seul. Triste sort. Vous avez perdu tous vos proches avant de mourir. En voilà, une belle mort."
    menu:
        "Menu principal":
            return

label bandageAlone:
    $ heal -= 1
    p "Heureusement que j'en ai récupéré !"
    p "Allez, va mourir !"
    play sound "audio/shotFire.mp3"
    with hpunch
    p "C'est bon, je l'ai eu."
    p "Fan ! Il m'a bien touché. C'est vraiment dangereux ici, il faut absolument que je trouve Luleå le plus vite possible. Aller [p_name], c'est presque fini !"
    jump endSituationAlone

label fleeAlone:
    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'failureEndSupermarketAlone'
    p "Il faut que je tente de m'enfuir, je ne peux pas aller à la confrontation."
    p "À trois, je cours."
    p "1"
    p "2"
    p "3 GO !"
    show screen countdown
    menu:
        "Courir":
            hide screen countdown
            jump endSituationAlone

label failureEndSupermarketAlone:
    p "Fan ! Ils sont vraiment à l'affût. Je suis obligé maintenant d'aller à la confrontation."                                                                                
    play sound "audio/shotFire.mp3"
    with hpunch
    p "Ok, il en reste plus qu'un." 
    play sound "audio/shotFire.mp3"
    with hpunch
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    menu:
        "Utiliser un bandage" if heal >= 1:
            jump bandageAlone
        "Ne rien faire":
            jump noBandageAlone

label endSituationAlone:
    p "Je dois plus être très loin de Luleå."
    p "Même si ce n'est sûrement pas un paradis, je pense que c'est la meilleure option que j'ai pour l'instant."

    play sound "audio/knock.mp3"
    with vpunch
    g "Qui êtes-vous ?"
    p "Je suis simplement un survivant. Je ne veux faire de mal à personne. J'ai entendu dire qu'il y a avait un camp ici et je veux seulement me joindre à vous." 
    p "Je suis prêt à travailler énormément pour gagner une place dans votre groupe. Je ne suis pas malade et je suis à l'aise physiquement."
    g "Bien, savez-vous qui nous sommes ?"
    p "Je n'en sais que très peu à votre sujet."
    g "Avez-vous déjà vu notre symbole ?"
    menu :
        "Non":
            jump noSymbolAlone
        "Oui":
            jump symboleAlone

label noSymbolAlone:  
    p "Non, c'est la première fois."
    g "Et bien, il faudrait que l'on le montre davantage..."
    g "Nous sommes les Sköll. En hommage au dieu, grand dévoreur du Soleil."
    g "Savez-vous ce que ça implique de nous rejoindre ?"
    g "Nous ne voulons que les meilleurs. Si vous ne faites pas partie des meilleurs, on vous fait disparaître, c'est compris ?"
    p "Je comprends."
    jump proposalAlone

label symboleAlone:
    p "Oui, je l'ai déjà vu quelques fois."
    g "Le grand Sköll, dévoreur du Soleil nous protège de la désolation et nous guide ces temps-ci."
    g "Vous savez, on n'est pas ici pour devenir amis-amis avec tout le monde." 
    g "Nous voulons simplement survivre et sommes prêts à tout pour arriver à nos objectifs, compris ?"
    p "Je comprends."
    jump proposalAlone

label proposalAlone:
    g "À moins que vous préfériez rejoindre les Upplyst ?"
    g "Ah, ces ploucs, ces bons à rien. Ils sont bien drôles à voir, à essayer de sauver tout le monde. Ils sont si mignons et naïfs."
    g "Voilà ce que mène la gentillesse dans ce monde...la pauvreté. À vouloir sauver tout le monde, ils ne sauvent en réaliste personne."
    g "Comment peut-on survivre en aidant les gens dans un monde comme celui-ci. Ils sont si stupides à rêver à leur paradis où tout le monde est égal et vit en paix."
    g "Ça ne peut pas exister et ça n'existera jamais." 
    g "On ne peut pas sauver tout le monde et eux s'obstinent encore à le faire en voyant pourtant les résultats désastreux que ça leur offre. Bon..."
    g "Alors, êtes-vous toujours prêt à nous rejoindre ?"
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
    p "C'est ce dont j'ai toujours rêvé. Je peux enfin rejoindre ce groupe, après tout ce temps à errer, à être proche de la mort chaque seconde de mon existence."

    unknown "Enfin ! Vous avez réussi à atteindre votre objectif, le fameux village de Luleå. Vous avez bien mérité votre place."
    unknown "Cependant, vous avez donné votre confiance trop rapidement à n'importe qui. Ce groupe est sournois et vous vous en êtes rendu compte trop tard."
    unknown "Le groupe vous a capturé et vous a fait prisonnier." 
    unknown "Vous n'êtes qu'un esclave parmi tant d'autres à espérer chaque seconde de votre existence de vivre comme autrefois."
    menu:
        "Menu principal":
            return

label restartUpplystAlone:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je crois qu'il serait mieux de rejoindre les Upplyst."
    p "Je pense que rejoindre ce groupe peut être très dangereux. Je ne sais pas si je peux vraiment faire confiance à ces gens-là."

    unknown "Vous avez décidé de rejoindre les Upplyst, bon choix. Enfin...vous avez une bonne morale. Vous êtes prêt à donner à votre prochain."
    unknown "Cependant, est ce qu'avoir une bonne morale vous fait survivre ? Je suis navré de vous le dire, mais non."
    unknown "En rejoignant le camp, vous êtes tombé nez à nez sur une lourde attaque du groupe de Luleå sur le camp. Tuant ainsi la quasi-totalité de ses membres, et vous compris."
    menu:
        "Menu principal":
            return

label endStayAlone1:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "J'en ai marre de tout ça. Je n'en peux plus de cette guerre sans queue ni tête. Je ne suis pas sûr que j'ai vraiment quelque chose à jouer là-dedans."
    p "Je pense qu'il serait que je pars de tout ça et que je retente l'aventure tout seul. Comme quand tout ceci à commencé."
    p " Je ne sais pas encore où est ce que je vais aller, mais c'est indéniablement la meilleure option que j'ai."

    unknown "Vous avez décidé de finir seul. Très bon choix ! Vous avez préféré faire confiance seulement à vous-même."
    unknown "Vous êtes courageux ! Cependant, ne vous souvenez plus à quel point ces temps-ci était difficile. À quel point il était difficile de survivre sans réel but."
    unknown "Croyez-vous vraiment que vous aurez eu le mental nécessaire ? Bien évidemment que non. Vous êtes mort seul dans votre bivouac sans personne pour vous pleurer."
    menu:
        "Menu principal":
            return

label leaveWithPlayer:
    s "Désolé Viggo, mais je dois partir avec [p_name]. J'ai très confiance en lui et il m'a traitée de la meilleure manière qu'il a pu."
    v "Sache que tu fais le mauvais choix Sven, tu ne peux pas faire confiance à des inconnus surtout par ces temps-ci."
    s "Mais ce n'est pas un inconnu Viggo, c'est mon père."
    p "Allons y Sven, il faut qu'on se dépêche avant qu'il n'y arrive quelque chose."

    p "Pour se rendre à Luleå, il faut qu'on traverse la ville de Kiruna et trouver des ressources."
    p "On a le choix entre trois lieux : le cinéma, le quartier résidentiel et le supermarché."
    menu:
        "Se rendre au quartier":
            jump neighborhood
        
        "Se rendre au supermarché":
            jump supermarket
        
        "Se rendre au cinéma":
            jump movieTheater

label neighborhood:
    p "Allons se rendre dans le quartier, on trouvera sûrement des restes."

    p "Je viens de trouver une conserve de thon."
    $ food += 1
    menu:
        "La manger":
            jump eat4
        "La garder":
            jump keep4
        "La donner":
            jump giveS4

label eat4:
    p "Je suis désolé fiston, mais avec tout ce qui m'est arriver." 
    p "C'est encore plus dur pour moi. Je préférais la prendre. Sans être en bonne forme, je ne pourrais plus de protéger, tu comprends ?"
    s "Je comprends."
    jump endNeighborhood

label giveS4:
    p "Tu peux la manger, Sven. Tu en as beaucoup plus besoin que moi."
    s "Merci papa."
    $ food -= 1
    $ foodGiven += 1
    jump endNeighborhood

label keep4:
    p "Je pense qui serait mieux de la garder. On ne sait jamais ce qui peut se passer."
    s "Ok papa, ça me parait juste."
    jump endNeighborhood

label endNeighborhood:
    p "Je crois qu'on a tout fouillé, on peut s'en aller et rejoindre Luleå. Enfin !"
    jump endSituation

label movieTheater:
    p "On peut aller au cinéma. Les gens se ruent plus facilement dans les maisons et supermarché plutôt que les cinémas."

    s "Ouah, c'est immense !"
    p "Tu n'es jamais allé au cinéma ?"
    s "Ja, j'y suis déjà allé, mais c'était il y a longtemps et j'étais très jeune. Je ne m'en souviens plus trop."
    p "C'est quoi ton film préféré ?"
    s "Gordon och Paddy ! Il est hyper drôle, c'est l'histoire d'un détective qui est trop débile pour résoudre la moindre enquête."
    p "Ça doit être rigolo !"
    s "C'est le meilleur film de tous les temps, de toute la création de l'univers. Et toi, c'est quoi ton film préféré ?"
    p "Midsommar à coup sûr, mais il est un peu trop violent pour toi, ce n'est pas vraiment pour les enfants."
    s "Ohh..."
    p "Mais je te le montrerais quand tu seras plus grand. Je suis sûre que tu l'adoreras."
    p "..."
    p "Bon allons fouiller les lieux."
    s "Je n'ai pas l'impression qu'il y est grand-chose ici."
    p "Tu as peut-être raison. Au moins, ça m'a fait plaisir un peu du passé et de tous ces vieux souvenirs."
    s "Oui, moi aussi !"
    p "Allez, prenons la route vers Luleå, je veux savoir ce qui s'y passe."
    jump endSituation

label supermarket:
    p "On peut aller au supermarché, peut-être que des choses n'ont pas encore été volé là-bas."

    s "C'est si vide ici."
    p "Tout a déjà été fouillé à mon avis."
    play sound "audio/shotFireMultiple.wav"
    with hpunch
    p "Cache-toi Sven !"
    s "Papa, j'ai peur !"
    p "Ça va aller, ça va aller !"
    s "Qu'est-ce qu'on fait ?"
    menu:
        "Aller à la confrontation":
            jump confrontation
        "Fuire":
            jump flee

label confrontation:
    p "On ne peut pas fuir, on est obligé de se battre."
    p "Ok, tu vas te cacher et moi, je vais m'en occuper avec le pistolet."
    p "Surtout, tu ne bouges pas de ta cachette, ok ?"
    s "Ok, papa."
                                                                                
    play sound "audio/shotFire.mp3"
    with hpunch
    p "Ok, il en reste plus qu'un." 
    play sound "audio/shotFire.mp3"
    with hpunch
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    menu:
        "Utiliser un bandage" if heal >= 1:
            jump bandage
        "Ne rien faire":
            jump noBandage

label noBandage: 
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    unknow "Le danger peut venir n'importe quand, et vous en avez souffert. Vous êtes mort en laissant Sven devenir prisonnier par ses survivants."
    unknow "Ne vous inquiétez pas, il ne souffrira plus très longtemps."
    menu:
        "Menu principal":
            return

label bandage:
    $ heal -= 1
    p "Heureusement que j'en ai récupéré !"
    p "Allez va mourir !"
    play sound "audio/shotFire.mp3"
    with hpunch
    p "C'est bon, je l'ai eu."
    p "Tu peux sortir Sven, ils ne sont plus là."

    s "Ça va aller papa ?"
    p "Oui, Sven ne t'inquiète pas. Ce n'est qu'une égratignure. C'est vraiment dangereux ici, il faut absolument qu'on trouve Luleå le plus vite possible." 
    p "Allez en route !"
    jump endSituation

label flee:
    $ time = 1
    $ timer_range = 1
    $ timer_jump = 'failureEndSupermarket'
    p "Il faut qu'on s'enfuie, on ne peut pas aller à la confrontation."
    p "À trois, on court."
    p "1"
    p "2"
    p "3 GO !"
    show screen countdown
    menu:
        "Courir":
            hide screen countdown
            jump endSituation

label failureEndSupermarket:
    p "Ok, tu vas te cacher et moi, je vais m'en occuper avec le pistolet."
    p "Surtout, tu ne bouges pas de ta cachette, ok ?"
    s "Ok, papa."
                                                                                
    play sound "audio/shotFire.mp3"
    with hpunch
    p "Ok, il en reste plus qu'un." 
    play sound "audio/shotFire.mp3"
    with hpunch
    p "AHHHH"
    p "Il m'a eu."
    p "Il me faut un bandage !"
    menu:
        "Utiliser un bandage" if heal >= 1:
            jump bandage
        "Ne rien faire":
            jump noBandage

label endSituation:
    p "On doit plus être très loin de Luleå."
    s "T'es sûr que c'est toujours une bonne idée papa ?"
    p "Je pense que c'est la meilleure que nous ayons pour l'instant."

    menu :
        "Donner de la nourriture à Sven":
            jump giveS5
        "Ne rien faire":
            jump secondMeeting

label giveS5:
    p "Tiens Sven, tu en as besoin."
    s "Merci papa."
    p "On a besoin de force pour ce qui va nous arriver."
    $ foodGiven += 1
    jump secondMeeting

label secondMeeting:    
    p "T'es prêt Sven ?"
    s "Oui papa."

    play sound "audio/knock.mp3"
    with vpunch
    g "Qui êtes-vous ?"
    p "On est simplement des survivants. On ne veut faire de mal à personne." 
    p "J'ai entendu dire qu'il y a avait un camp ici et nous vouons seulement nous joindre à vous. Nous sommes prêts à travailler énormément pour gagner une place dans votre groupe." 
    p "Nous ne sommes pas malades, nous sommes à l'aise physiquement. Mon fils est très obéissant et ne vous causera aucun problème."
    g "Bien, savez-vous qui nous sommes ?"
    p "Je n'en sais que très peu à votre sujet."
    g "Avez-vous déjà vu notre symbole ?"
    menu:
        "Non":
            jump noSymbol
        "Oui":
            jump symbol

label noSymbol:
    p "Non, c'est la première fois."
    g "Et bien, il faudrait que l'on le montre davantage..."
    g "Nous sommes les Sköll. En hommage au dieu, grand dévoreur du Soleil."
    g "Savez-vous ce que ça implique de nous rejoindre ?"
    g "Nous ne voulons que les meilleurs. Si vous ne faites pas partie des meilleurs, on vous fait disparaître, c'est compris ?"
    p "Je comprends."
    jump proposal4

label symbol:
    p "Oui, je l'ai déjà vu quelques fois."
    g "Le grand Sköll, dévoreur du Soleil nous protège de la désolation et nous guide ces temps-ci."
    g "Vous savez, on n'est pas ici pour devenir amis-amis avec tout le monde. Nous voulons simplement survivre et sommes prêts à tout pour arriver à nos objectifs, compris ?"
    p "Je comprends."
    jump proposal4

label proposal4:
    g "Cependant, nous ne pouvons prendre qu'une seule personne ici. Nous voulons s'assurer de chaque entrée dans ce groupe et les former comme il le faut." 
    g "Nous n'avons pas le temps de s'occuper de deux têtes fragiles."
    s "Papa et si on retournait au camp des Upplyst ?"
    g "Ah, ces ploucs, ces bons à rien. Ils sont bien drôles à voir, à essayer de sauver tout le monde. Ils sont si mignons et naïfs."
    g "Voilà ce que mène la gentillesse dans ce monde...la pauvreté. À vouloir sauver tout le monde, ils ne sauvent en réaliste personne."
    g "Comment peut-on survivre en aidant les gens dans un monde comme celui-ci. Ils sont si stupides à rêver à leur paradis où tout le monde est égal et vit en paix."
    g "Ça ne peut pas exister et ça n'existera jamais." 
    g "On ne peut pas sauver tout le monde et eux s'obstinent encore à le faire en voyant pourtant les résultats désastreux que ça leur offre. Bon..."
    p "Vous êtes sûr de ne pouvoir prendre qu'une seule personne ? On peut tous les deux vous aider grandement, on a le sens de..."
    g "La ferme et choisissez ! Je n'ai pas de temps à perdre avec vous !"
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
    p "Je suis désolé, Sven, mais j'ai fait tout ce que j'ai pu pour te protéger jusque-là. J'ai fait énormément de sacrifice pour ta survie, mais... j'en ai peu plus." 
    p "Je suis fatigué, Sven. Je ne veux plus survivre comme ça."
    p "Luleå a toujours été mon objectif avant même que je te rencontre et je n'ai pas envie de le laisser filer."
    s "Tu veux m'abandonner ici, tout seul. Mais je ne survivrais jamais sans toi."
    p "Ne te sous-estime pas Sven. Tu es capable de bien plus. Je l'ai vu tout ce temps. Tu as beaucoup grandi et j'en suis fière."
    s "Mais qu'est-ce que tu racontes ? Je ne peux rien faire sans toi. Je ne peux pas survivre comme ça."
    p "Je suis désolé, Sven, mais je ne peux plus."
    p "Adieu Sven !"

    unknow "Vous avez réussi à faire un choix difficile. Je vous félicite ! Dorénavant, vous êtes devenus un simple pion de ce groupe sanguinaire."
    unknow "Vous souffrez énormément chaque jour, mais il semble que ce fût la meilleure option pour vous."
    unknow "En revanche, pour Sven, vous vous imaginez qu'il n'a pas survit très longtemps. Il n'a même pas réussi à aller jusqu'au camp des Upplyst."
    menu:
        "Menu principal":
            return

label svenJoinThem:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Sven, je pense qu'il est temps de se séparer. Mon objectif a toujours été de te protéger et je crois que ma mission s'arrête ici." 
    p "Rejoins les, tu auras une vie bien meilleure, j'en suis sûr."
    s "Mais papa, je ne peux rien faire sans toi, je ne peux pas survivre sans toi."
    p "Tu ne seras plus tout seul Sven, tu vivras mieux, bien mieux."
    s "Mais je ne veux pas ! Je veux rester avec toi papa ! Je m'en fiche de rester avec des inconnus, je veux continuer avec toi !"
    p "C'est difficile Sven, mais on ne peut plus vivre comme ça. Ces derniers temps ont été compliqué et nous ne pouvons pas survivre comme ça très longtemps." 
    p "On n'a pas le choix, il faut que tu ailles là-bas."
    s "Et toi qu'est ce que tu vas faire ?"
    p "Ne t'inquiète pas pour moi, je m'en sortirais. Je réussirai toujours à m'en sortir comme on l'a toujours fait, d'accord ?"
    s "Oui papa."
    p "Au revoir Sven, tu me manqueras beaucoup !"
    s "Moi aussi..."
    s "Papa."

    unknow "Vous avez décidé de laisser votre place à Sven. Vous avez beaucoup de courage. Vous rendez vous compte que vous lui avez tout donné."
    unknow "Et qu'est-ce que vous avez vous ? Rien ! Vous mourrez seul dans votre bivouac."
    menu:
        "Menu principal":
            return

label restartUpplyst:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je crois qu'il serait mieux que l'on rejoigne les Upplyst Sven."
    s "Mais papa, c'était ton objectif de venir ici, tu avais dit que c'était comme un petit paradis."
    p "Je sais Sven, mais rejoindre ce groupe peut être très dangereux. Je ne sais pas s'il on peut vraiment faire confiance à ces gens-là."
    p "Et j'ai trop peur de te perdre, mon objectif est de te protéger et il ne va pas s'arrêter aujourd'hui."
    s "On pourra rejoindre oncle Viggo alors ?"
    p "Oui Sven, on pourra rejoindre Viggo."

    unknown "Vous avez décidé de rejoindre les Upplyst, bon choix. Enfin...vous avez une bonne morale. Vous êtes prêt à donner à votre prochain."
    unknown "Cependant, est ce qu'avoir une bonne morale vous fait survivre ? Je suis navré de vous le dire, mais non."
    unknown "En rejoignant le camp, vous êtes tombé nez à nez sur une lourde attaque du groupe de Luleå sur le camp. Tuant ainsi la quasi-totalité de ses membres, et vous compris."
    menu:
        "Menu principal":
            return

label endStayAlone2:
    stop music fadeout 0.5
    play music "audio/endingMusic.mp3" loop
    p "Je n'ai marre de tout ça Sven. Je n'en peux plus de cette guerre sans queue ni tête. Je ne crois pas que l'on est vraiment quelque chose à jouer."
    p "Je pense qu'il serait mieux qu'on part de tout ça et qu'on tente l'aventure à deux. Comme on l'a toujours fait."
    s "Mais où est ce que va aller alors ?"
    p "Je ne sais pas encore, mais ça sera bien mieux qu'ici, tu ne trouves pas ?"
    s "Je ne sais pas, ces derniers temps ont été si compliqué que je ne sais pas si l'on peut toujours survivre comme ça."
    p "C'est notre meilleure option, Sven, crois moi."

    unknown "Vous avez décidé de finir seuls. Très bon choix ! Vous avez préféré faire confiance seulement à vous-même et Sven."
    unknown "Vous êtes courageux ! Cependant, ne vous souvenez plus à quel point ces temps-ci était difficile. À quel point il était difficile de survivre sans réel but."
    unknown "Croyez-vous vraiment que vous aurez eu le mental nécessaire ? Bien évidemment que non. Vous mourrez seul avec Sven à vos côtés en vous mettant face à votre échec."
    menu:
        "Menu principal":
            return
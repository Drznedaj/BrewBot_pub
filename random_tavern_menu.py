import requests
import random
import math

#print(requests.get('http://archive.wizards.com/dnd/tavern/Welcome.asp').text)

aAdjective = ["Angry","Blissful","Brave","Bright","Comfortable","Courageous","Emerald","Fair","Gray","Pale","Fiery","Goodly","Happy","Home of the","Laughing","Lonesome","Lovely","Massacred","Motley","Pious","Purple","Sad","Sign of the","Simple","Sorrowful","Stalwart","Stately","Weary","Whisky","Whispering","Silly","Adventuring"]

aRoot = ["Maiden","Gnome","Master","Warrior","Jug","Glass","Brewery","Inn","Hostelry","Tavern","Hero","Castle","Dragon","Unicorn","Pony","Cup","Plate","Beard","Sword","Bow","Axe","Devil","Blackguard","Giant","Fiend","Shield","Tankard","Ranger","Cloud","Fisher","God","Elf","Dwarf","Orc","Bed","Bear","Lion","Moose","Gargoyle"]

aGender = ["Male","Female"]

aRace = ["human","elf","tiefling","gnome","halfling","dwarf","half-orc","half-ogre","half-elf"]

aLevel = ["1st-level","2nd-level","3rd-level","4th-level","5th-level","6th-level","7th-level","8th-level","9th-level","10th-level"]

aClass = ["NPC commoner","fighter","ranger","cleric","barbarian","rogue","bard","sorcerer","NPC warrior","NPC aristocrat"]

aClientele = ["a bard performing for drinks","a bewildered barbarian","a couple on a date","a few anonymous drunks","a fighter looking for trouble","a group of dicing rogues","a group of elves sipping wine","a press-gang collecting drunks","a ranger looking for her wolf","a rogue secretly emptying purses","a snobby aristocrat","a sorcerer selling spells","a wizard deep in his cups","adventurers planing their next move","an assassin secretly biding his time","carnies out on the town","cleric of Pelor preaching in corner","cloaked figure in corner","company of drunken adventurers","company of stalwart adventurers","dwarf buying rounds for the house","gang of half-orc street toughs","grim paladins on crusade","group of singing halflings","guardsmen on a stake-out","halfling tourists","humans gnawing turkey legs","party of rowdy dwarves","soft-spoken traveling monks","town guard captain having a meal","youngsters on a lark"]
aClientele1 = ["A bard performing for drinks","A bewildered barbarian","A couple on a date","A few anonymous drunks","A fighter looking for trouble","A group of dicing rogues","A group of elves sipping wine","A press-gang collecting drunks","A ranger looking for her wolf","A rogue secretly emptying purses","A snobby aristocrat","A sorcerer selling spells","A wizard deep in his cups","Adventurers planing their next move","An assassin secretly biding his time","Carnies out on the town","Cleric of Pelor preaching in corner","Cloaked figure in corner","Company of drunken adventurers","Company of stalwart adventurers","Dwarf buying rounds for the house","Gang of half-orc street toughs","Grim paladins on crusade","Group of singing halflings","Guardsmen on a stake-out","Halfling tourists","Humans gnawing turkey legs","Party of rowdy dwarves","Soft-spoken traveling monks","Town guard captain having a meal","Youngsters on a lark"]

aRumors = ["Thieves have stolen the crown jewels.","A dragon has flown into a town and demanded tribute.","The tomb of an old wizard has been discovered.","Wealthy merchants are being killed in their homes.","The statue in the town square was found to be a petrified paladin.","A caravan of important goods is about to leave for a trip through a dangerous area.","Cultists are kidnapping potential sacrifices.","Goblins riding spider eaters have been attacking the outskirts of a town.","Local bandits have joined forces with a tribe of bugbears.","A blackguard is organizing monsters in an area.","A gate to the Lower Planes threatens to bring more demons to the world.","Miners have accidentally released something awful that once was buried deep.","A wizards guild challenges the ruling council.","Racial tensions between humans and elves are rising.","A mysterious fog has brought ghosts into town.","The holy symbol of a high priest is missing.","An evil wizard has developed a new type of golem.","Someone in town is a werewolf.","Slavers continue to raid a local community.","A fire elemental has escaped from a wizards lab.","Bugbears are demanding a toll on a well-traveled bridge.","A mirror of opposition has created an evil duplicate of a hero.","Two orc tribes wage a bloody war.","New construction reveals a previously unknown underground tomb.","A nearby kingdom has launched an invasion.","Two well-known heroes will soon fight a duel.","An ancient sword must be recovered to defeat a ravaging -monster.","A prophecy foretells of coming doom unless an artifact is -recovered.","Ogres have kidnaped the mayors daughter.","A wizard is buried in a trap-filled tomb with her powerful magic items.","An enchanter is compelling others to steal for him.","A shapechanged mind flayer is gathering mentally controlled servitors.","A plague brought by wererats threatens a community.","The keys to disarming all the magic traps in a wizards tower have gonemissing.","Sahuagin are being driven out of the sea to attack coastal -villages.","Gravediggers have discovered a huge, ghoul-filled catacomb under the cemetery.","A wizard needs a particularly rare spell component found only in the deep jungle.","A map showing the location of an ancient magic forge is discovered.","Various monsters have long preyed upon people from within the sewers of a major city.","An emissary going into a hostile kingdom needs an escort.","Vampires are preying upon a small town.","A haunted tower is reputed to be filled with treasure.","Barbarians have torn up a village in a violent rage.","Giants are stealing cattle from local farmers.","Unexplained snowstorms have brought winter wolves into an otherwise peaceful area.","A lonely mountain pass is guarded by a powerful sphinx denying all passage.","Evil mercenaries are constructing a fortress not far from the community.","An antidote to a magic poison must be found before the duke dies.","A druid needs help defending her grove against goblins.","An ancient curse is turning innocent people into evil murderers.","Gargoyles are killing giant eagles in the mountains.","Mysterious merchants sell faulty magic items in town and then attempt to slink away.","A recently recovered artifact causes arcane spellcasters powers to go awry.","An evil noble has put a price on a good nobles head.","Adventurers exploring a dungeon have not returned in a week.","The funeral for a good fighter was disrupted by enemies he made while alive.","Colossal vermin are straying out of the desert to attack settlements.","An evil tyrant has outlawed unsanctioned magic use.","A huge dire wolf, apparently immune to magic, is organizing the wolves in the wood.","A community of gnomes has built a flying ship.","An island at the center of the lake is actually the top of a strange, submerged fortress.","Buried below the Tree of the World lies the Master Clock of Time.","A child has wandered into a vast necropolis, and dusk approaches quickly.","All the dwarves in an underground city have disappeared.","A strange green smoke billows out of a cave near a mysterious ruin.","Mysterious groaning sounds come from a haunted wood atnight.","Thieves steal a great treasure and flee into Mordenkainens magnificent mansion.","A sorcerer attempted to travel ethereally but disappeared completely in the process.","A paladins quest for atonement led her to a troll lair too well-defended for her to tackle alone.","A kingdom known for its wizards prepares for war.","The high priest is an illusion.","A new noble seeks to clear a patch of wilderness of all monsters.","A bulette is tearing apart viable farmland.","A infestation of stirges drives yuan-ti closer to civilized lands.","Treants in the woods are threatened by a huge fire of mysterious origin.","Clerics who have resurrected a long-dead hero discovered shes not what they thought.","A sorrowful bard tells a tavern tale of his imprisoned companions.","Evil nobles have created an adventurers guild to monitor and control adventurers.","A halfling caravan must pass through an ankheg-infested wilderness.","All the doors in the kings castle are suddenly arcane locked and fire trapped.","An innocent man, about to be hanged, pleads for someone to help him.","The tomb of a powerful wizard, filled with magic items, has sunk into the swamp.","Someone is sabotaging wagons and carts to come apart when they travel at high speed.","A certain type of frogs, found only in an isolated valley, fall like rain on a major city.","A jealous rival threatens to stop a well-attended wedding.","A woman who mysteriously vanished years ago has been seen walking on the surface of a lake.","An earthquake has uncovered a previously unknown dungeon.","A wronged half-elf needs a champion to fight for her in a gladiatorial trial.","At the eye of the storm that tears across the land lies a floating citadel.","People grow suspicious of half-orcmerchants peddling gold dragon parts in the market.","An absentminded wizard has let her rod of wonder fall into the wrong hands.","Undead shadows vex a large library, especially an old storeroom long left undisturbed.","The door into an abandoned house in the middle of town is in fact a magic portal.","Barge pirates have made a deal with a covey of hags and exact a high toll to use the river.","Two parts of a magic item are in the hands of bitter enemies the third piece is lost.","A clutch of wyverns is preying upon sheep as well as shepherds.","Evil clerics gather in secret to summon a monstrous god to the world.","A major city faces a siege by a force of humans, duergar, and gnolls.","A huge gemstone supposedly lies within an ancient ruined monastery.","Lizardfolk riding dragon turtles sell their services as mercenaries to the highest bidder."]

aAccommodations = ["Poor (a place on the floor near the hearth and a flea-ridden blanket amongst the riff-raff) for 1 sp/day","Common (a placed on a raised, heated floor, blanket and pillow, amongst higher-class company) for 3 sp/day","Good (a small private room with one bed, some amenities and a covered chamber pot) for 5 sp/day","Noble (a large private room with large bed, private bath with hot water on request, snacks on request, and private chamber pot in a separate chamber) for 1 gp/day"]

aSubmenu13A = ["Bacon","Ham","Beef steak","Kippers","Smoked sausage","Blood pudding","Fried perch","Hash","Meatballs","1A"]

aSubmenu13B = ["Pork chop","Chicken half","Leg of mutton","Rabbit stew","Sausage","Veal sweetbreads","Lamb stew","1A"]

aSubmenu13C = ["Beef steak","Whole duck","Pork liver","Mixed grill","Stuffed trout","Lamb chop","Broiled catfish","1A"]

aSubmenu1A = ["Dog stew","Cat cutlet","Frog legs","Octopus","Wyvern shank","Monkey brain","Triceratops steak","Basilisk tail","Bulette fin","Darkmantle","Eagle breast","Owlbear chop","Wild boar headcheese","Giant toad tongue","Shark filet"]

aMenu14 = ["Chicken eggs","Duck eggs","Goose eggs","Sharp cheese","Soft cheese","Curds","14A"]

aSubmenu14A = ["Hippogriff egg","Griffin-milk cheese","Gnomes yogurt","Deep dwarven blue cheese","Dragon turtle omelet","Quail eggs"]

aMenu15 = ["Carrots","Turnips","Potato","Taro","Yams","Onions","Cabbage","Leeks","Collard greens","Broccoli","Spinach","Corn","Chick peas","Peas","Succotash","Green beans","Lentils","Broad beans","Black beans","15A"]

aSubmenu15A = ["Udoroot frond","Giant bean","Assassin vine leaf","Shrieker steak","Pumpkin","Okra","Seaweed","Artichoke"]

aMenu16 = ["Apple","Pear","Peach","Dates","Strawberries","Raspberries","Blackberries","Blueberries","Currants","Raisins","Melon","Stewed prunes","16A"]

aSubmenu16A = ["Assassin vine berries","Coconut","Pomegranite","Banana","Guava","Black apple","Underdark glowfruit","Sea-grapes","Breadfruit"]

aMenu17 = ["Coarse rye bread","Nut bread","Rice","Millet","Flatbread","Corn pone","Mush","Oatmeal","17A"]

aSubmenu17A = ["Wild rice","Sunflower loaf","Goblin bannock","Centaur rye","Sea oats","Tahini","Pine nuts","Marzipan"]

aMenu18 = ["Berry pie","Apple pie","Raisin pie","Pecan pie","Mince pie","Rhubarb pie","Plain cake","Walnut cake","Fruitcake","Spice bread","Custard","Plum pudding","Rice pudding","Applesauce","18A"]

aSubmenu18A = ["Wood-elven crisp cakes","Crème brulée","Sherbet","Honey-cake","Spiced, stuffed pumpkin","Chocolate torte","Toffee","Vanilla fudge"]

aMealCost = [1,2,4,8]

aExoticCost = [0,2,4,6]

aCostSuffix = ["sp","sp","sp","sp"]

aExoticChance = [0,5,15,35]

aBreakfast = [0,"test1","test2","test3","test4","test5"]

aLunch = [0,"test1","test2","test3","test4"]

aSupper = [0,"test1","test2","test3","test4","test5"]

aSnack = [0,"test1","test2","test3"]

def generatetavern():

    aCostSuffix[0] = "sp"
    aCostSuffix[1] = "sp"
    aCostSuffix[2] = "sp"
    aCostSuffix[3] = "sp"

    wAdjective = math.floor(random.random() * len(aAdjective))
    wRoot = math.floor(random.random() * aRoot.__len__())
    wGender = math.floor(random.random() * aGender.__len__())
    wRace = math.floor(random.random() * aRace.__len__())
    wLevel = math.floor(random.random() * aLevel.__len__())
    wClass = math.floor(random.random() * aClass.__len__())
    wClientele1 = math.floor(random.random() * aClientele.__len__())
    wClientele2 = math.floor(random.random() * aClientele.__len__())

    while (wClientele2 == wClientele1):
        wClientele2 = math.floor(random.random() * aClientele.__len__())


    #wRumors 1,2,3 or random
    wRumors = 4

    while (wRumors == 4):
        wRumors = math.floor((random.random() * 3) + 1)


    wRumors1 = math.floor(random.random() * aRumors.__len__())
    wRumors2 = math.floor(random.random() * aRumors.__len__())
    wRumors3 = math.floor(random.random() * aRumors.__len__())

    while (wRumors2 == wRumors1):
        wRumors2 = math.floor(random.random() * aRumors.__len__())


    while (wRumors3 == wRumors1 or wRumors3 == wRumors2):
        wRumors3 = math.floor(random.random() * aRumors.__len__())


    #wAccommodations poor, common, good, noble or random
    wAccommodations = 4

    while (wAccommodations == 4):
        wAccommodations = math.floor(random.random() * aAccommodations.__len__())


    wSubmenu13A = math.floor(random.random() * aSubmenu13A.__len__())
    wSubmenu13B = math.floor(random.random() * aSubmenu13B.__len__())
    wSubmenu13C = math.floor(random.random() * aSubmenu13C.__len__())
    wSubmenu1A = math.floor(random.random() * aSubmenu1A.__len__())
    wSubmenu14A = math.floor(random.random() * aSubmenu14A.__len__())
    wSubmenu15A = math.floor(random.random() * aSubmenu15A.__len__())
    wSubmenu16A = math.floor(random.random() * aSubmenu16A.__len__())
    wSubmenu17A = math.floor(random.random() * aSubmenu17A.__len__())
    wSubmenu18A = math.floor(random.random() * aSubmenu18A.__len__())

    aSubmenu13A[aSubmenu13A.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13B[aSubmenu13B.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13C[aSubmenu13C.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aMenu14[aMenu14.__len__() - 1] = aSubmenu14A[wSubmenu14A]
    aMenu15[aMenu15.__len__() - 1] = aSubmenu15A[wSubmenu15A]
    aMenu16[aMenu16.__len__() - 1] = aSubmenu16A[wSubmenu16A]
    aMenu17[aMenu17.__len__() - 1] = aSubmenu17A[wSubmenu17A]
    aMenu18[aMenu18.__len__() - 1] = aSubmenu18A[wSubmenu18A]

    wSubmenu13AX1 = math.floor((random.random() * aSubmenu13A.__len__()) + 1) 
    xSubmenu13AX1 = math.floor(random.random() * aSubmenu13A.__len__()) 
    wMenu14aX1 = math.floor((random.random() * aMenu14.__len__()) + 1) 
    xMenu14aX1 = math.floor(random.random() * aMenu14.__len__()) 
    wMenu14bX1 = math.floor((random.random() * aMenu14.__len__()) + 1) 
    xMenu14bX1 = math.floor(random.random() * aMenu14.__len__()) 

    while (wMenu14bX1 == wMenu14aX1):
        wMenu14bX1 = math.floor((random.random() * aMenu14.__len__()) + 1) 

    while (xMenu14bX1 == xMenu14aX1):
        xMenu14bX1 = math.floor(random.random() * aMenu14.__len__()) 
    

    wMenu16X1 = math.floor((random.random() * aMenu16.__len__()) + 1) 
    xMenu16X1 = math.floor(random.random() * aMenu16.__len__()) 
    wMenu17X1 = math.floor((random.random() * aMenu17.__len__()) + 1) 
    xMenu17X1 = math.floor(random.random() * aMenu17.__len__()) 

    wMeatX1 = math.floor((random.random() * 100) + 1)
    wDairyaX1 = math.floor((random.random() * 100) + 1)
    wDairybX1 = math.floor((random.random() * 100) + 1)
    wFruitX1 = math.floor((random.random() * 100) + 1)
    wGrainX1 = math.floor((random.random() * 100) + 1)

    aBreakfast[0] = aMealCost[wAccommodations]
    aBreakfast[1] = aSubmenu13A[xSubmenu13AX1]
    aBreakfast[2] = aMenu14[xMenu14aX1]
    aBreakfast[3] = aMenu14[xMenu14bX1]
    aBreakfast[4] = aMenu16[xMenu16X1]
    aBreakfast[5] = aMenu17[xMenu17X1]

    if (wSubmenu13AX1 == aSubmenu13A.__len__() and wMeatX1 <= aExoticChance[wAccommodations]):
        aBreakfast[1] = aSubmenu13A[aSubmenu13A.__len__() - 1]
        aBreakfast[0] = aBreakfast[0] + aExoticCost[wAccommodations]
            

    if (wMenu14aX1 == aMenu14.__len__() and wDairyaX1 <= aExoticChance[wAccommodations]): 
        aBreakfast[2] = aSubmenu14A[aSubmenu14A.__len__() - 1]
        aBreakfast[0] = aBreakfast[0] + aExoticCost[wAccommodations]
            

    if (wMenu14bX1 == aMenu14.__len__() and wDairybX1 <= aExoticChance[wAccommodations]):
        aBreakfast[3] = aSubmenu14A[aSubmenu14A.__len__() - 1]
        aBreakfast[0] = aBreakfast[0] + aExoticCost[wAccommodations]
            

    if (wMenu16X1 == aMenu16.__len__() and wFruitX1 <= aExoticChance[wAccommodations]):
        aBreakfast[4] = aSubmenu16A[aSubmenu16A.__len__() - 1]
        aBreakfast[0] = aBreakfast[0] + aExoticCost[wAccommodations]
        

    if (wMenu17X1 == aMenu17.__len__() and wGrainX1 <= aExoticChance[wAccommodations]):
        aBreakfast[5] = aSubmenu17A[aSubmenu17A.__len__() - 1]
        aBreakfast[0] = aBreakfast[0] + aExoticCost[wAccommodations]
            

    wSubmenu13A = math.floor(random.random() * aSubmenu13A.__len__())
    wSubmenu13B = math.floor(random.random() * aSubmenu13B.__len__())
    wSubmenu13C = math.floor(random.random() * aSubmenu13C.__len__())
    wSubmenu1A = math.floor(random.random() * aSubmenu1A.__len__())
    wSubmenu14A = math.floor(random.random() * aSubmenu14A.__len__())
    wSubmenu15A = math.floor(random.random() * aSubmenu15A.__len__())
    wSubmenu16A = math.floor(random.random() * aSubmenu16A.__len__())
    wSubmenu17A = math.floor(random.random() * aSubmenu17A.__len__())
    wSubmenu18A = math.floor(random.random() * aSubmenu18A.__len__())

    aSubmenu13A[aSubmenu13A.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13B[aSubmenu13B.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13C[aSubmenu13C.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aMenu14[aMenu14.__len__() - 1] = aSubmenu14A[wSubmenu14A]
    aMenu15[aMenu15.__len__() - 1] = aSubmenu15A[wSubmenu15A]
    aMenu16[aMenu16.__len__() - 1] = aSubmenu16A[wSubmenu16A]
    aMenu17[aMenu17.__len__() - 1] = aSubmenu17A[wSubmenu17A]
    aMenu18[aMenu18.__len__() - 1] = aSubmenu18A[wSubmenu18A]

    wSubmenu13BX2 = math.floor((random.random() * aSubmenu13B.__len__()) + 1)
    xSubmenu13BX2 = math.floor(random.random() * aSubmenu13B.__len__())
    wMenu14X2 = math.floor((random.random() * aMenu14.__len__()) + 1)
    xMenu14X2 = math.floor(random.random() * aMenu14.__len__())
    wMenu15X2 = math.floor((random.random() * aMenu15.__len__()) + 1)
    xMenu15X2 = math.floor(random.random() * aMenu15.__len__())
    wMenu17X2 = math.floor((random.random() * aMenu17.__len__()) + 1)
    xMenu17X2 = math.floor(random.random() * aMenu17.__len__())

    wMeatX2 = math.floor((random.random() * 100) + 1)
    wDairyX2 = math.floor((random.random() * 100) + 1)
    wVegetableX2 = math.floor((random.random() * 100) + 1)
    wGrainX2 = math.floor((random.random() * 100) + 1)

    aLunch[0] = aMealCost[wAccommodations]
    aLunch[1] = aSubmenu13B[xSubmenu13BX2]
    aLunch[2] = aMenu14[xMenu14X2]
    aLunch[3] = aMenu15[xMenu15X2]
    aLunch[4] = aMenu16[xMenu17X2]


    if (wSubmenu13BX2 == aSubmenu13B.__len__() and wMeatX2 <= aExoticChance[wAccommodations]):
        aLunch[1] = aSubmenu13B[aSubmenu13B.__len__() - 1]
        aLunch[0] = aLunch[0] + aExoticCost[wAccommodations]
            

    if (wMenu14X2 == aMenu14.__len__() and wDairyX2 <= aExoticChance[wAccommodations]):
        aLunch[2] = aMenu14[aMenu14.__len__() - 1]
        aLunch[0] = aLunch[0] + aExoticCost[wAccommodations]
            

    if (wMenu15X2 == aMenu15.__len__() and wVegetableX2 <= aExoticChance[wAccommodations]):
        aLunch[3] = aMenu15[aMenu15.__len__() - 1]
        aLunch[0] = aLunch[0] + aExoticCost[wAccommodations]
            

    if (wMenu17X2 == aMenu17.__len__() and wGrainX2 <= aExoticChance[wAccommodations]):
        aLunch[4] = aMenu17[aMenu17.__len__() - 1]
        aLunch[0] = aLunch[0] + aExoticCost[wAccommodations]
            

    wSubmenu13A = math.floor(random.random() * aSubmenu13A.__len__())
    wSubmenu13B = math.floor(random.random() * aSubmenu13B.__len__())
    wSubmenu13C = math.floor(random.random() * aSubmenu13C.__len__())
    wSubmenu1A = math.floor(random.random() * aSubmenu1A.__len__())
    wSubmenu14A = math.floor(random.random() * aSubmenu14A.__len__())
    wSubmenu15A = math.floor(random.random() * aSubmenu15A.__len__())
    wSubmenu16A = math.floor(random.random() * aSubmenu16A.__len__())
    wSubmenu17A = math.floor(random.random() * aSubmenu17A.__len__())
    wSubmenu18A = math.floor(random.random() * aSubmenu18A.__len__())

    aSubmenu13A[aSubmenu13A.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13B[aSubmenu13B.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13C[aSubmenu13C.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aMenu14[aMenu14.__len__() - 1] = aSubmenu14A[wSubmenu14A]
    aMenu15[aMenu15.__len__() - 1] = aSubmenu15A[wSubmenu15A]
    aMenu16[aMenu16.__len__() - 1] = aSubmenu16A[wSubmenu16A]
    aMenu17[aMenu17.__len__() - 1] = aSubmenu17A[wSubmenu17A]
    aMenu18[aMenu18.__len__() - 1] = aSubmenu18A[wSubmenu18A]

    wSubmenu13CX3 = math.floor((random.random() * aSubmenu13C.__len__()) + 1)
    xSubmenu13CX3 = math.floor(random.random() * aSubmenu13C.__len__())

    wMenu15aX3 = math.floor((random.random() * aMenu15.__len__()) + 1)
    xMenu15aX3 = math.floor(random.random() * aMenu15.__len__())

    wMenu15bX3 = math.floor((random.random() * aMenu15.__len__()) + 1)
    xMenu15bX3 = math.floor(random.random() * aMenu15.__len__())

    while (wMenu15bX3 == wMenu15aX3):
        wMenu15bX3 = math.floor((random.random() * aMenu15.__len__()) + 1)
    

    while (xMenu15bX3 == xMenu15aX3):
        xMenu15bX3 = math.floor(random.random() * aMenu15.__len__())
    

    wMenu17X3 = math.floor((random.random() * aMenu17.__len__()) + 1)
    xMenu17X3 = math.floor(random.random() * aMenu17.__len__())

    wMenu18X3 = math.floor((random.random() * aMenu18.__len__()) + 1)
    xMenu18X3 = math.floor(random.random() * aMenu18.__len__())

    wMeatX3 = math.floor((random.random() * 100) + 1)
    wVegetableaX3 = math.floor((random.random() * 100) + 1)
    wVegetablebX3 = math.floor((random.random() * 100) + 1)
    wGrainX3 = math.floor((random.random() * 100) + 1)
    wDesertX3 = math.floor((random.random() * 100) + 1)

    aSupper[0] = aMealCost[wAccommodations]
    aSupper[1] = aSubmenu13C[xSubmenu13CX3]
    aSupper[2] = aMenu15[xMenu15aX3]
    aSupper[3] = aMenu15[xMenu15bX3]
    aSupper[4] = aMenu17[xMenu17X3]
    aSupper[5] = aMenu18[xMenu18X3]


    if (wSubmenu13CX3 == aSubmenu13C.__len__() and wMeatX3 <= aExoticChance[wAccommodations]):
        aSupper[1] = aSubmenu13C[aSubmenu13C.__len__() - 1]
        aSupper[0] = aSupper[0] + aExoticCost[wAccommodations]
            

    if (wMenu15aX3 == aMenu15.__len__() and wVegetableaX3 <= aExoticChance[wAccommodations]):
        aSupper[2] = aMenu15[aMenu15.__len__() - 1]
        aSupper[0] = aSupper[0] + aExoticCost[wAccommodations]
            

    if (wMenu15bX3 == aMenu15.__len__() and wVegetablebX3 <= aExoticChance[wAccommodations]):
        aSupper[3] = aMenu15[aMenu15.__len__() - 1]
        aSupper[0] = aSupper[0] + aExoticCost[wAccommodations]
            

    if (wMenu17X3 == aMenu17.__len__() and wGrainX3 <= aExoticChance[wAccommodations]):
        aSupper[4] = aMenu17[aMenu17.__len__() - 1]
        aSupper[0] = aSupper[0] + aExoticCost[wAccommodations]
            

    if (wMenu18X3 == aMenu15.__len__() and wDesertX3 <= aExoticChance[wAccommodations]):
        aSupper[5] = aMenu18[aMenu18.__len__() - 1]
        aSupper[0] = aSupper[0] + aExoticCost[wAccommodations]
            

    wSubmenu13A = math.floor(random.random() * aSubmenu13A.__len__())
    wSubmenu13B = math.floor(random.random() * aSubmenu13B.__len__())
    wSubmenu13C = math.floor(random.random() * aSubmenu13C.__len__())
    wSubmenu1A = math.floor(random.random() * aSubmenu1A.__len__())
    wSubmenu14A = math.floor(random.random() * aSubmenu14A.__len__())
    wSubmenu15A = math.floor(random.random() * aSubmenu15A.__len__())
    wSubmenu16A = math.floor(random.random() * aSubmenu16A.__len__())
    wSubmenu17A = math.floor(random.random() * aSubmenu17A.__len__())
    wSubmenu18A = math.floor(random.random() * aSubmenu18A.__len__())

    aSubmenu13A[aSubmenu13A.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13B[aSubmenu13B.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aSubmenu13C[aSubmenu13C.__len__() - 1] = aSubmenu1A[wSubmenu1A]
    aMenu14[aMenu14.__len__() - 1] = aSubmenu14A[wSubmenu14A]
    aMenu15[aMenu15.__len__() - 1] = aSubmenu15A[wSubmenu15A]
    aMenu16[aMenu16.__len__() - 1] = aSubmenu16A[wSubmenu16A]
    aMenu17[aMenu17.__len__() - 1] = aSubmenu17A[wSubmenu17A]
    aMenu18[aMenu18.__len__() - 1] = aSubmenu18A[wSubmenu18A]

    wMenu14X4 = math.floor((random.random() * aMenu14.__len__()) + 1)
    xMenu14X4 = math.floor(random.random() * aMenu14.__len__())

    wMenu16X4 = math.floor((random.random() * aMenu16.__len__()) + 1)
    xMenu16X4 = math.floor(random.random() * aMenu16.__len__())

    wMenu17X4 = math.floor((random.random() * aMenu17.__len__()) + 1)
    xMenu17X4 = math.floor(random.random() * aMenu17.__len__())

    wDairyX4 = math.floor((random.random() * 100) + 1)
    wFruitX4 = math.floor((random.random() * 100) + 1)
    wGrainX4 = math.floor((random.random() * 100) + 1)

    aSnack[0] = aMealCost[wAccommodations]
    aSnack[1] = aMenu14[xMenu14X4]
    aSnack[2] = aMenu16[xMenu16X4]
    aSnack[3] = aMenu17[xMenu17X4]


    if (wMenu14X4 == aMenu14.__len__() and wDairyX4 <= aExoticChance[wAccommodations]):
        aSnack[2] = aMenu14[aMenu14.__len__() - 1]
        aSnack[0] = aSnack[0] + aExoticCost[wAccommodations]
            

    if (wMenu16X4 == aMenu16.__len__() and wFruitX4 <= aExoticChance[wAccommodations]):
        aSnack[2] = aMenu16[aMenu16.__len__() - 1]
        aSnack[0] = aSnack[0] + aExoticCost[wAccommodations]
            

    if (wMenu17X4 == aMenu17.__len__() and wGrainX4 <= aExoticChance[wAccommodations]):
        aSnack[2] = aMenu17[aMenu17.__len__() - 1]
        aSnack[0] = aSnack[0] + aExoticCost[wAccommodations]
            

    aBreakfast[0] = math.floor(aBreakfast[0] * 1.5)
    aLunch[0] = math.floor(aLunch[0] * 2)
    aSupper[0] = math.floor(aSupper[0] * 2.5)
    aSnack[0] = math.floor(aSnack[0] * 1)

    if (aBreakfast[0] >= 10):
        aBreakfast[0] = math.floor((aBreakfast[0] + 5)/ 10) 
        aCostSuffix[0] = "gp" 

    if (aLunch[0] >= 10):
        aLunch[0] = math.floor((aLunch[0] + 5) / 10) 
        aCostSuffix[1] = "gp"
            
    if (aSupper[0] >= 10):
        aSupper[0] = math.floor((aSupper[0] + 5) / 10) 
        aCostSuffix[2] = "gp"
            

    if (aSnack[0] >= 10):
        aSnack[0] = math.floor((aSnack[0] + 5) / 10) 
        aCostSuffix[3] = "gp"

    print("Welcome to the "+aAdjective[wAdjective]+" "+aRoot[wRoot])
    print('Today\'s Menu')
    print('Breakfast')
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(aBreakfast[1],aBreakfast[2],aBreakfast[3],aBreakfast[4],aBreakfast[5],aBreakfast[0],aCostSuffix[0]))
    print('Lunch')
    print('{}\n{}\n{}\n{}\n{}\n{}\n'.format(aLunch[1],aLunch[2],aLunch[3],aLunch[4],aLunch[0],aCostSuffix[1]))
    print('Supper')
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(aSupper[1],aSupper[2],aSupper[3],aSupper[4],aSupper[5],aSupper[0],aCostSuffix[2]))
    print('Snack')
    print('{}\n{}\n{}\n{}\n{}\n'.format(aSnack[1],aSnack[2],aSnack[3],aSnack[0],aCostSuffix[3]))

generatetavern()

#==========================================================================================================================================

from __future__ import barry_as_FLUFL
import time
import random

print()
nAme=input("What's your nickname? : ")

while True:
    print('Arulana, 19345 A.D')
    time.sleep(1.3)
    print(f"gurad : {nAme}, go to the King's room. It's the king's royal command.")
    time.sleep(1.6)
    print("(at king's room)")
    time.sleep(1.4)
    print(f"king : I need your help, so I called you, {nAme}.")
    time.sleep(1.4)
    print("king : ......")
    time.sleep(1.5)
    print("king : the Devil's seal has been lifted ")
    time.sleep(1.3)
    print("king : can you kill the Devil?")
    time.sleep(1.2)
    while True:
        try:
            canyou=int(input("""Will you kill the Devil?
            1. Yes, I cant't
            2. No, I cant
            (choose one job!You can choose a number!)
            =>  """))
        except:
            print("Enter a number again, please!")
            continue
        else:
            if canyou > 2 or canyou < 0:
                print("Try again, numbers between 1-7")
            else:
                break
    if canyou == 1:
        print("king : oh... thank you....I will give you a reward if you kill the Devil.. and choose a job..")
        time.sleep(1.3)
        break
    if canyou == 2:
        print("king : ok...")
        time.sleep(2.3)
        print('A few month later..')
        time.sleep(1.4)
        print("you are kill by monster...")
        time.sleep(1.3)
        print('will you revive or just die..')
        while True:
            try:
                willyou=int(input("""Will you revive or not?
                1. Yes
                2. No
                (choose one job!You can choose a number!)
                =>  """))
            except:
                print("Enter a number again, please!")
                continue
            else:
                if willyou > 2 or willyou < 0:
                    print("Try again, numbers between 1-7")
                else:
                    break
                if willyou==1:
                    print("you revived")
                if willyou == 2:
                    break
    if willyou ==2 or canyou == 1:
        if willyou == 2:
            ('ok your dead')
            print('you will exit game in 5')
            time.sleep(1)
            print('                   4')
            time.sleep(1)
            print("                3")
            time.sleep(1)
            print("             2")
            time.sleep(1)
            print("          1")
            time.sleep(0.5)
            print("you exited the game")
            time.sleep(0.5)
            exit()
        if canyou==1:
            print("king : oh... thank you....I will give you a reward if you kill the Devil.. and choose a job..")
            time.sleep(0.3)
            break


while True:
    try:
        jOb=int(input("""What's your job?
        1. knight
        2. sorcerer
        3. healer
        4. berserker
        5. shooter
        6. fighter
        7. troubadour
        (choose one job!You can choose a number!)
        =>  """))
    except:
        print("Enter a number again, please!")
        continue
    else:
        if jOb > 7 or jOb < 0:
            print("Try again, numbers between 1-7")
        else:
            break

iTems=["bread","map"]


if jOb == 1:
    iTems.append("old wooden sword")
    iTems.append("knight's Old Clothes Set")
    
elif jOb == 2:
    iTems.append("old wooden wand")
    iTems.append("sorcerer's Old Clothes Set")

elif jOb == 3:
    iTems.append("old wooden healing wand")
    iTems.append("healer's Old Clothes Set")

elif jOb == 4:
    iTems.append("old wooden ax")
    iTems.append("Berserker's Old Clothes Set")

elif jOb == 5:
   iTems.append("old wooden gun")
   iTems.append("Shooter's Old Clothes Set")

elif jOb == 6:
    iTems.append("old wooden gauntlet")
    iTems.append("fighter's Old Clothes Set")

elif jOb == 7:
    iTems.append("old wooden guitar")
    iTems.append("troubadour's Old Clothes Set")


jOob = []

if jOb == 1:
    jOob.append('knight')
elif jOb == 2:
    jOob.append('sorcerer')
elif jOb == 3:
    jOob.append('healer')
elif jOb == 4:
    jOob.append('Berserker')
elif jOb == 5:
    jOob.append('Shooter')
elif jOb == 6:
    jOob.append('fighter')
elif jOb == 7:
    jOob.append('troubadour')

levels=0
nowexp=0
maxexp=100
fullhp=1500
hp=fullhp
fullmp=300
mp=fullmp
gold=100
n= '['+nAme+']'
characterState={"name" :  n, "job" : jOob, "items" : iTems, "levels" : levels, "Hp":hp,"Mp":mp,"golds":gold}

print()
print("=====================================================================================================================================================================")
print('||',characterState,'||')
print('||                                                                                                                                                                 ||')
print("=====================================================================================================================================================================")
print()

#==========================================================
import random

mAp =0 
while True:
    while True:
        try:
            todo=int(input("""Choose what to do?
            1. open map
            2. see state
            (You can choose a number(1 or 2)!)
            =>  """))
        except: 
            print("Enter a number again, please!")
            continue
        else:
            if todo > 2 or todo < 0:
                print("Try again, numbers between 1 or 2")
            else:
                break

    if todo == 1:
        while True:
            try:
                mAp=int(input("""Choose where to go?
                1. green garden
                2. dark cave
                3. flaming mountain
                4. frozen sea
                5. corrupted wastes 
                6. thick wetland
                7. village
                8. store
                (You can choose a number(1 to 8)!)
                =>  """))
            except: 
                print("Enter a number again, please!")
                continue
            else:
                if mAp > 8 or mAp < 0:
                    print("Try again, numbers between 1-8")
                else:
                    break

    mon=('')

    class Monster:
        def __init__(self,risk):
            self.risk = risk 

        def monsterdam(self,damage):
            self.damage = damage
            if self.damage >= 1000:
                return "??? class"
            elif self.damage >= 950:
                return "SS class"
            elif self.damage >= 800:
                return "S class"
            elif self.damage >= 750:
                return "A class"
            elif self.damage >= 550:
                return "B class"
            elif self.damage >= 450:
                return "C class"
            elif self.damage >= 350:
                return "D class"
            elif self.damage >= 250:
                return "E class"
            elif self.damage >= 150:
                return "F class"
            elif self.damage <= 150:
                return "- class"

            skilldam = self.damage
        
    golampunching= skilldam=150
    throwing_stones=skilldam=750

    punching=skilldam=50
    javelinthrow=skilldam=100

    axing=skilldam=600
    crushing=skilldam=950

    flamingfire=skilldam=250
    soalfire=skilldam=500

    launchweb=skilldam=200
    bitting=skilldam=500

    posionshot=skilldam=50

    watershot=skilldam=10
    tailspin=skilldam=5

    bodyheadbutt=skilldam=300
    tailspin=skilldam=650

    tridentthorw=skilldam=350
    callthewave=skilldam=550
    
    calldevil=skilldam=450
    lockinthedark=skilldam=750

    bodyslap=skilldam=50

    fire=skilldam=250
    water=skilldam=250
    dark=skilldam=450
    light=skilldam=450

    toungesmash=skilldam=350
    watercannon=skilldam=500

    golamskill=['punching(150)','Throwing_stones(750)']
    gobulinskill=['punching(50)','javelin throw(100)']
    orkskill=['axing(600)','crushing(950)']
    corruptedfireskill=['flaming fire(250)','soal fire(500)']
    spiderskill=['launch web(200)','biting(500)']
    posionousmushroomskill=['posion shot(50)']
    fishskill=['water shot(10)','tailspin(5)']
    storgfishskill=['body headbutt(300)','tailspin(650)']
    fishman=['trident throw(350)','call the waves(550)']
    shadowskill=['call devil(450)','lock in the dark(750)']
    slimeskill=['body slap(50)']
    whichskill=['fire magic(250)','water magic(250)','dark magic(450)','lightmagic(450)']
    frogskill=['tongue smash(350)','water cannon(500)']
    villagerskil=['talk(-800)','hello~(-450)']
    traderskill=['trade(0)']

    knight =['sword swing(d:100,m:-20)','continuous slash(d:650,m:-75)']
    sorcerer=['fire magic(d:110,m:-15)','Meteor(d:750,m:-80)']
    healer=['punching(d:50,m:-5),heal(h:+400,m:-45)','rod of asclepius(d:750,h:+600,m:-100)']
    Berserker=['swing ax(d:110,m:-20)','blocking(Nullifies the next attack,m:-35)','throw ax(d:600,m:-60']
    Shooter=['shoot assault rifle(d:100~300,m:-45)','shoot pistol(d:55,m:-5)','shoot sniper rifle(d:999,m:-95)']
    fighter=['punch(d:100,m:-5)','kiking(d:300,m:-30)','Knee kick(d:400,m:-40)']
    troubadour=['shooting a note(d:115,m:-20)','healing song((h:+500,m:-50)','harmony of beats(h:-100,m:+75,)']       

    if mAp == 1:
        mon=random.choice(["golam","golam","gobulin","ork","gobulin","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 2:
        mon=random.choice(["golam","corrupted fire","spider","poisonous mushroom","gobulin","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 3:
        mon=random.choice(["golam","gobulin","ork","corrupted fire","gobulin","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 4:
        mon=random.choice(["golam","gobulin","ork","fish","storg fish","fishman","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 5:
        mon=random.choice(["golam","gobulin","ork","shadow","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 6:
        mon=random.choice(["golam","gobulin","ork","slime","which","frog","poisonous mushroom","gobulin","gobulin"])
        print('you met',mon)
    if mAp == 7:
        mon=random.choice(["villager","trader","gobulin","villager","trader","villager","trader"])
        print('you met',mon)
    if mAp == 8:
        mon=random.choice(["trader"])
        print('you met',mon)

    monsterhp=0

    if mon == 'golam':
        monsterhp=2500
    if mon == 'gobulin':
        monsterhp=300
    if mon == 'ork':
        monsterhp = 1500
    if mon == "corrupted fire":
        monsterhp=150
    if mon == "spider":
        monsterhp=250
    if mon == "poisonous mushroom":
        monsterhp=50
    if mon == 'fish':
        monsterhp=50
    if mon == 'strong fish':
        monsterhp=500
    if mon == 'fishman':
        monsterhp=2000
    if mon == 'shadow':
        monsterhp=700
    if mon == 'slime':
        monsterhp=2000
    if mon=='frog':
        monsterhp = 150
    if mon=='which':
        monsterhp = 3000
    if mon == 'villager':
        monsterhp=3500
    if mon == 'trader':
        monsterhp =3500
    if mon == 'gardian':
        monsterhp = 100000000



    turn = 2    
    yn = 0

    if todo == 1:
        if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':
            while True:
                try:
                    yn =int(input("""will you fight?
                    1. yes
                    2. no
                    you can enter a number(1 to 2)
                    => """))
                except: 
                    print("Enter a number again, please!")
                    continue
                else:
                    if yn < 0 or yn > 2:
                        print("Try again, numbers between 1-2")
                    else:
                        break  

    if todo == 1:
        if mon == 'trader':
            if yn ==2:
                while True:
                    try:
                        yn =int(input("""will you see a store?
                        1. yes
                        2. no
                        you can enter a number(1 to 2)
                        => """))
                    except: 
                        print("Enter a number again, please!")
                        continue
                    else:
                        if yn <1 or yn>2:
                            print("Try again, numbers between 1-2")
                        else:
                            break  

            while True:
                try:
                    buysell =int(input(f"""will you sell or buy or do nothing(you have {gold}gold)
                    1. sell
                    2. buy
                    3.do nothing
                    you can enter a number(1 to 3)
                    => """))
                except: 
                    print("Enter a number again, please!")
                    continue
                else:
                    if yn <1 or yn>2:
                        print("Try again, numbers between 1-2")
                    else:
                        break  
                    
            if buysell==2:
                if jOb == 1:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10

            if buysell==2:
                if jOb == 2:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10                       

            if buysell==2:
                if jOb == 3:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10

            if buysell==2:
                if jOb == 4:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                                    break
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10
                                    break                                                                       

            if buysell==2:
                if jOb == 5:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10

            if buysell==2:
                if jOb == 6:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10

            if buysell==2:
                if jOb == 7:
                    while True:
                        try:
                            buything=int(input("""what do you want?
                            1.mp potion(+40)(10 gold)
                            2.hp potion(+700)(10 gold)
                            3.iron sword(dmg +100)(50 gold)
                            4.full flate armor(hp +300)(70 gold)
                            5.flame sword(dmg +350)(110 gold)
                            6.oruganuum gobulin's armor(hp +700)(350 gold)
                            7.great sword(dmg +430)(200 gold)
                            8.ork's armor(hp +1000)(550 gold)
                            9.poniard(dmg +500)(180 gold)
                            10.great armor(hp+ 1300)(600 gold)
                            11.ork's knife(dmg +600)(300 gold)
                            12.guard's armor(hp +)
                            13.excuter's sword(dmg)
                            14.Xkalrliver(dmg +13000)(50000 gold)
                            15.king's armor(hp+ 50000)(60000 gold)                            
                            you can enter a number(1 to 3)
                            => """))
                        except: 
                            print("Enter a number again, please!")
                            continue
                        else:
                            if yn <1 or yn>15:
                                print("Try again, numbers between 1-15")
                            else:
                                break  
                            if buything==1:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last mp =>',mp)
                                    mp+=40
                                    print('your mp =>',mp)
                                    gold-=10
                            if buything==2:
                                if gold < 10:
                                    print("you can't buy")
                                else:
                                    print('your last hp =>',hp)
                                    hp+=700
                                    print('your mp =>',mp)
                                    gold-=10


    knight =['sword swing(d:100,m:-20)','continuous slash(d:650,m:-75)']
    sorcerer=['fire magic(d:110,m:-15)','Meteor(d:750,m:-80)']
    healer=['punching(d:50,m:-5),heal(h:+400,m:-45)','rod of asclepius(d:750,h:+600,m:-100)']
    Berserker=['swing ax(d:110,m:-20)','blocking(Nullifies the next attack,m:-35)','throw ax(d:600,m:-60']
    Shooter=['shoot assault rifle(d:100~300,m:-45)','shoot pistol(d:55,m:-5)','shoot sniper rifle(d:999,m:-95)']
    fighter=['punch(d:100,m:-5)','kiking(d:300,m:-30)','Knee kick(d:400,m:-40)']
    troubadour=['shooting a note(d:115,m:-20)','healing song((h:+500,m:-50)','harmony of beats(h:-100,m:+75,)']   


    while True:
        if todo == 1:
            if yn==1:
                if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':
                    if turn == 2:
                        if jOb == 1:
                            while True:
                                try:
                                    attcktodo=int(input("""Choose what to do?
                                    1. sword swing (d:100,m:-20)
                                    2. continuous slash (d:650,m:-75)
                                    (You can choose a number(1 or 2)!)
                                    =>  """))
                                except:
                                    print("Enter a number again, please!")
                                    continue
                                else:
                                    if attcktodo > 2 or attcktodo < 0:
                                        print("Try again, numbers between 1-2")
                                    else:
                                        break
            
                            if attcktodo == 1:
                                if mp >= 20:
                                    print()
                                    print('you swoung sword to', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-100
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-20
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp <= 20:
                                    print('you don\'t have mp!')
                                    turn = 1
                            elif attcktodo == 2:
                                if mp >= 75:
                                    print()
                                    print(f'you slashed the {mon} consecutively')
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-650
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-75
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp <= 75:
                                    print('you don\'t have mp!')
                                    turn = 1


        if todo == 1:
            if yn == 1:
                if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':
                    if turn == 2:
                        if jOb == 2:
                            while True:
                                try:
                                    attcktodo=int(input("""Choose what to do?
                                    1. fire magic (d:110,m:-15)
                                    2. meteor (d:750,m:-80)
                                    (You can choose a number(1 or 2)!)
                                    =>  """))
                                except:
                                    print("Enter a number again, please!")
                                    continue
                                else:
                                    if attcktodo > 2 or attcktodo < 0:
                                        print("Try again, numbers between 1-2")
                                    else:
                                        break
            
                            if attcktodo == 1:
                                if mp >= 15:
                                    print()
                                    print('you lanuched fire magic to', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-110
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-15
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 15:
                                    print('you don\'t have mp!')
                                    turn = 1
                            elif attcktodo == 2:
                                if mp >= 80:
                                    print()
                                    print(f'you lanuched meteor to {mon}')
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-750
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-80
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 80:
                                    print('you don\'t have mp!')
                                    turn = 1

        if todo == 1:
            if yn == 1:   
                if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':         
                    if turn == 2:
                        if jOb == 3:
                            while True:
                                try:
                                    attcktodo=int(input("""Choose what to do?
                                    1. punching (d:50,m:-5)
                                    2. heal (h:+400,m:-45)
                                    3. rod of asclepius (d:750,h:+600,m:-100)
                                    (You can choose a number(1 or 3)!)
                                    =>  """))
                                except:
                                    print("Enter a number again, please!")
                                    continue
                                else:
                                    if attcktodo > 3 or attcktodo < 0:
                                        print("Try again, numbers between 1-3")
                                    else:
                                        break
            
                            if attcktodo == 1:
                                if mp >= 5:
                                    print()
                                    print('you punched', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-50
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1            
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-5
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                    if mp < 5:
                                        print('you don\'t have mp!')
                                        turn = 1
                            elif attcktodo == 2:
                                if mp >= 45:
                                    print()
                                    print(f'you healed {nAme}')
                                    print('your last hp =>',hp)
                                    hp = hp+400
                                    print(f"{nAme}\'s healed hp =>",hp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-45
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 45:
                                    print('you don\'t have mp!')
                                    turn = 1
                            elif attcktodo == 3:
                                if mp >= 100:
                                    print(f'you attacked {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-750
                                    print('last hp =>',monsterhp)
                                    print()
                                    print(f'you healed {nAme}')
                                    print('your last hp =>',hp)
                                    print()
                                    hp = hp+600
                                    print(f"{nAme}\'s healed hp =>",hp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-100
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 100:
                                    print('you don\'t have mp!')
                                    turn = 1

        if todo == 1:
                if yn == 1:  
                    if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':          
                        if turn == 2:
                            if jOb == 4:
                                while True:
                                    try:
                                        attcktodo=int(input("""Choose what to do?
                                        1. swing ax (d:110,m:-20)
                                        2. throw ax (d:600,m:-60)
                                        (You can choose a number(1 or 3)!)
                                        =>  """))
                                    except:
                                        print("Enter a number again, please!")
                                        continue
                                    else:
                                        if attcktodo > 2 or attcktodo < 0:
                                            print("Try again, numbers between 1-2")
                                        else:
                                            break
            
                                if attcktodo == 1:
                                    print()
                                    print('you swoung ax to', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-110
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-20
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 20:
                                    print('you don\'t have mp!')
                                    turn = 1

                                elif attcktodo == 2:
                                    print()
                                    print(f'you throwed ax to {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp = monsterhp-600
                                    print('last hp =>',monsterhp)
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-60
                                    print('last mp =>',mp)
                                    turn = 1
                                    time.sleep(0.8)
                                if mp < 60:
                                    print('you don\'t have mp!')
                                    turn = 1

        if todo == 1:
                if yn == 1:  
                    if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':          
                        if turn == 2:
                            if jOb == 5:
                                while True:
                                    try:
                                        attcktodo=int(input("""Choose what to do?
                                        1. shoot assault rifle (d:100~300,m:-45)
                                        2. shoot pistol(d:55,m:-5)
                                        3. shoot sniper rifle(d:999,m:-95)
                                        (You can choose a number(1 or 3)!)
                                        =>  """))
                                    except:
                                        print("Enter a number again, please!")
                                        continue
                                    else:
                                        if attcktodo > 3 or attcktodo < 0:
                                            print("Try again, numbers between 1-3")
                                        else:
                                            break
            
                                if attcktodo == 1:
                                    print()
                                    print('you shooted assault rifle to', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-random.choice([100,200,300])
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-45
                                    print('last mp =>',mp)                        
                                    time.sleep(0.8)
                                if mp < 45:
                                    print('you don\'t have mp!')
                                    turn = 1

                                elif attcktodo == 2:
                                    print()
                                    print(f'you shooted pistol to {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp = monsterhp - 55
                                    print('last hp =>',monsterhp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-5
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 100:
                                    print('you don\'t have mp!')
                                    turn = 1
                                if mp < 5:
                                    print('you don\'t have mp!')
                                    turn = 1
                                elif attcktodo == 3:
                                    print()
                                    print(f'you shooted sniper rifle to {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp = monsterhp - 999
                                    print('last hp =>',monsterhp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-95
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 95:
                                    print('you don\'t have mp!')
                                    turn = 1

        if todo == 1:
                if yn == 1:    
                    if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':        
                        if turn == 2:
                            if jOb == 6:
                                while True:
                                    try:
                                        attcktodo=int(input("""Choose what to do?
                                        1. punch(d:100,m:-5)
                                        2. kiking(d:300,m:-30)
                                        3. Knee kick(d:400,m:-40)
                                        (You can choose a number(1 or 3)!)
                                        =>  """))
                                    except:
                                        print("Enter a number again, please!")
                                        continue
                                    else:
                                        if attcktodo > 3 or attcktodo < 0:
                                            print("Try again, numbers between 1-3")
                                        else:
                                            break
            
                                if attcktodo == 1:
                                    print()
                                    print('you punched', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-100
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-5
                                    print('last mp =>',mp)                        
                                    time.sleep(0.8)
                                if mp < 5:
                                    print('you don\'t have mp!')
                                    turn = 1

                                elif attcktodo == 2:
                                    print()
                                    print(f'you kicked {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp = monsterhp - 55
                                    print('last hp =>',monsterhp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-30
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 30:
                                    print('you don\'t have mp!')
                                    turn = 1
                                elif attcktodo == 3:
                                    print()
                                    print(f'you knee kicked {mon}')
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp = monsterhp - 400
                                    print('last hp =>',monsterhp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-40
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 40:
                                    print('you don\'t have mp!')
                                    turn = 1


        if todo == 1:
                if yn == 1:
                    if mon =="golam" or 'gobulin' or 'ork' or 'corruptedfire' or 'spider' or 'posionousmushroom' or 'fish' or 'storgfish' or 'fishman' or 'shadow' or 'slime' or 'which' or 'frog':            
                        if turn == 2:
                            if jOb == 7:
                                while True:
                                    try:
                                        attcktodo=int(input("""Choose what to do?
                                        1. shooting a note(d:115,m:-20)
                                        2. healing song((h:+500,m:-50)
                                        3. harmony of beats(h:-100,m:+100,)
                                        (You can choose a number(1 or 3)!)
                                        =>  """))
                                    except:
                                        print("Enter a number again, please!")
                                        continue
                                    else:
                                        if attcktodo > 3 or attcktodo < 0:
                                            print("Try again, numbers between 1-3")
                                        else:
                                            break
                                            
                                if attcktodo == 1:
                                    print()
                                    print('you shooted note to', mon)
                                    print()
                                    print(f"{mon}\'s full hp =>",monsterhp)
                                    monsterhp=monsterhp-115
                                    print('last hp =>',monsterhp)
                                    print()
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-20
                                    print('last mp =>',mp)                        
                                    time.sleep(0.8)
                                if mp < 20:
                                    print('you don\'t have mp!')
                                    turn = 1
                                elif attcktodo == 2:
                                    print()
                                    print(f'you sang music of heal to {nAme}')
                                    print(f"{nAme}\'s last hp =>",hp)
                                    hp = hp + 500
                                    print('last hp =>',hp)
                                    turn = 1
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp-50
                                    print('last mp =>',mp)
                                    time.sleep(0.8)
                                if mp < 50:
                                    print('you don\'t have mp!')
                                    turn = 1
                                elif attcktodo == 3:
                                    print('you filled the mp in exchange for your hp')
                                    print()
                                    print(f"{nAme}\'s full hp =>",hp)
                                    hp=hp-100
                                    print('last hp =>',hp)
                                    print()
                                    print(f"{nAme}\'s full mp =>",mp)
                                    mp=mp+100
                                    print('last mp =>',mp)  
                                    turn=1                          
                                    time.sleep(0.8)

# knight =['sword swing(d:100,m:-20)','continuous slash(d:650,m:-75)']
# sorcerer=['fire magic(d:110,m:-15)','Meteor(d:750,m:-80)']
# healer=['punching(d:50,m:-5),heal(h:+400,m:-45)','rod of asclepius(d:750,h:+600,m:-100)']
# Berserker=['swing ax(d:110,m:-20)','blocking(Nullifies the next attack,m:-35)','throw ax(d:600,m:-60']
# Shooter=['shoot assault rifle(d:100~300,m:-45)','shoot pistol(d:55,m:-5)','shoot sniper rifle(d:999,m:-95)']
# fighter=['punch(d:100,m:-5)','kiking(d:300,m:-30)','Knee kick(d:400,m:-40)']
# troubadour=['shooting a note(d:115,m:-20)','healing song((h:+500,m:-50)','harmony of beats(h:-100,m:+100,)']   

        levelupdebufdamg=0

        if yn == 1:
            if turn == 1:
                if mon == "golam":
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('golam punched you!! (damage 150)')
                        hp=hp-(150+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)                 
                    elif gola == 2:
                        print('golam throwed rock to you!! (damage 750)')
                        hp=hp-(750+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('oh! you dodged golam\'s attack')
                        turn=2
                        print('last hp =>',hp)

                if mon == 'gobulin':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('gobulin punched you(damage 50)')
                        hp = hp -(50+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('gobulin throwed javelin to you!!(damage 100)')
                        hp = hp -(100+levelupdebufdamg)
                        turn = 2
                        print('last hp =>',hp)
                    else:
                        print('oh!! you dodged gobulin\'s attack')
                        turn = 2 
                        print('last hp =>',hp)

                if mon == 'ork':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('ork swoung ax to you!!(damage 650)')
                        hp=hp-(600+levelupdebufdamg)
                        turn = 2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('ork curshed you!!(damage 950)')
                        hp = hp-(950+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('oh!! you dodged ork\'s attack')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'corrupted fire':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('corruptedfire launched flaming fire to you!!(damage 250)' )
                        hp = hp-(250+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('corruptedfire launched soul fire to you(damage 500)')
                        hp = hp-(500+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('oh!! you dodged corruptedfire\'s attack' )
                        turn =2
                        print('last hp =>',hp)
        
                if mon == 'spider':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('spider lanched web to you!!(damage 200)')
                        hp =hp-(200+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('spider bitted you!!(damage 500)')
                        hp=hp-(500+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged spider\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'poisonous mushroom':
                    gola=random.choice([1,2])
                    if gola == 1:
                        print('poisonous mushroom shotted posion to you!!(damage 50)')
                        hp=hp-(50+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged poisonous mushroom\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'fish':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('fish shot water to you!!(damage 10)')
                        hp =hp-(10+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('fish spin!!(damage 50)')
                        hp=hp-(50+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged fish\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'strong fish':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('the strong fish hit you with it\'s body!!(damage 300)')
                        hp =hp-(300+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('strong fish hit!!(damage 650)')
                        hp=hp-(650+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged strong fish\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'fishman':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('fish man throw trident to you!!(damage 350)')
                        hp =hp-(350+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('fish man called the waves!!(damage 550)')
                        hp=hp-(550+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged fishman\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'shadow':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('shadow called demon!!(damage 450)')
                        hp =hp-(450+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('you are locked an the dark!!(damage 750)')
                        hp=hp-(750+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged shadow\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'slime':
                    gola=random.choice([1,2])
                    if gola == 1:
                        print('slime hit you with body!!(damage 350)')
                        hp =hp-(350+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged slime\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'which':
                    gola=random.choice([1,2,3,4,5])
                    if gola == 1:
                        print('which spelled fire magic!!(damage 250)')
                        hp =hp-(250+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('which spelled water magic!!(damage 250)')
                        hp=hp-(250+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 3:
                        print('which spelled dark magic!!(damage 450)')
                        hp=hp-(450+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    elif gola == 4:
                        print('which spelled light magic!!(damage 450)')
                        hp=hp-(450+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged which\'s attack!!')
                        turn =2
                        print('last hp =>',hp)

                if mon == 'frog':
                    gola=random.choice([1,2,3])
                    if gola == 1:
                        print('shadow called demon!!(damage 350)')
                        hp =hp-(350+levelupdebufdamg)
                        turn=2
                        print('last hp =>',hp)
                    elif gola == 2:
                        print('you are locked an the dark!!(damage 500)')
                        hp=hp-(500+levelupdebufdamg)
                        turn =2
                        print('last hp =>',hp)
                    else:
                        print('you dodged shadow\'s attack!!')
                        turn =2
                        print('last hp =>',hp)





# golamskill=['punching(150)','Throwing_stones(750)']
# gobulinskill=['punching(50)','javelin throw(100)']
# orkskill=['axing(600)','crushing(950)']
# corruptedfireskill=['flaming fire(250)','soal fire(500)']
# spiderskill=['launch web(200)','biting(500)']
# posionousmushroomskill=['posion shot(50)']
# fishskill=['water shot(10)','tailspin(5)']
# storgfishskill=['body headbutt(300)','tailspin(650)']
# fishman=['trident throw(350)','call the waves(550)']
# shadowskill=['call devil(450)','lock in the dark(750)']
# slimeskill=['body slap(50)']
# whichskill=['fire magic(250)','water magic(250)','dark magic(450)','lightmagic(450)']
# frogskill=['tongue smash(350)','water cannon(500)']
# villagerskil=['talk(-800)','hello~(-450)']
# traderskill=['trade(0)']


        if yn == 2:
            while True:
                try:
                    thenwhat=int(input("""then what will you do?
                    1. go sleep
                    2. eat bread 
                    3. open a map
                    4. see inventory
                    choose a number(1-4)
                    => """))
                except:
                    print("Enter a number again, please!")
                    continue
                else:
                    if thenwhat > 4 or thenwhat < 0:
                        print('Try again, numbers between 1-4')
                    else:
                        break    
            if thenwhat == 1:
                print('you slept for long time')
                if hp <= 1500:
                    print("you have full hp")
                if hp > 1500:
                    print('you slept for long time')
                    print('last hp =>',hp)
                    sleephealhp=int(1500-hp)
                    hp+=sleephealhp
                    print('your now hp =>',hp)

            if thenwhat == 3:
                while True:
                    try:
                        mAp=int(input("""Choose where to go?
                        1. green garden
                        2. dark cave
                        3. flaming mountain
                        4. frozen sea
                        5. corrupted wastes 
                        6. thick wetland
                        7. village
                        8. store
                        (You can choose a number(1 to 8)!)
                        =>  """))
                    except: 
                        print("Enter a number again, please!")
                        continue
                    else:
                        if mAp > 8 or mAp < 0:
                            print("Try again, numbers between 1-8")
                        else:
                            break
                        continue
            
        
        if todo==2:                                
            characterState={"name" :  n, "job" : jOob, "items" : iTems, "levels" : levels, "Hp":hp,"Mp":mp,"golds":gold}
            print()
            print("=====================================================================================================================================================================")
            print('||',characterState,'||')
            print('||                                                                                                                                                                 ||')
            print("=====================================================================================================================================================================")
            print()
            break

        if hp <= 0 or monsterhp <= 0:
            if monsterhp <= 0:
                print()
                print(f'you kill {mon}')
                if mon == 'golam':
                    print(f'exp + 50')
                    nowexp = nowexp + 50
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'gobulin':
                    print(f'exp + 20')
                    nowexp = nowexp + 20
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'ork':
                    print(f'exp + 250')
                    nowexp = nowexp + 250
                    print(f'your now exp {nowexp}')
                    break
                if mon == "corrupted fire":
                    print(f'exp + 60')
                    nowexp = nowexp + 60
                    print(f'your now exp {nowexp}')
                    break
                if mon == "spider":
                    print(f'exp + 30')
                    nowexp = nowexp + 30
                    print(f'your now exp {nowexp}')
                    break
                if mon == "poisonous mushroom":
                    print(f'exp + 10')
                    nowexp = nowexp + 10
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'fish':
                    print(f'exp + 5')
                    nowexp = nowexp + 5
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'strong fish':
                    print(f'exp + 45')
                    nowexp = nowexp + 45
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'fishman':
                    print(f'exp + 60')
                    nowexp = nowexp + 60
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'shadow':
                    print(f'exp + 70')
                    nowexp = nowexp + 70
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'slime':
                    print(f'exp + 35')
                    nowexp = nowexp + 35
                    print(f'your now exp {nowexp}')
                    break
                if mon=='frog':
                    print(f'exp + 10')
                    nowexp = nowexp + 10
                    print(f'your now exp {nowexp}')
                    break
                if mon=='which':
                    print(f'exp + 100')
                    nowexp = nowexp + 100
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'villager':
                    print(f'exp + 0')
                    nowexp = nowexp + 0
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'trader':
                    print(f'exp + 0')
                    nowexp = nowexp + 0
                    print(f'your now exp {nowexp}')
                    break
                if mon == 'gardian':
                    print(f'exp + 1000000000000000000000000000000000')
                    nowexp = nowexp + 1000000000000000000000000000000000
                    print(f'your now exp {nowexp}')
                    break

            if nowexp >= maxexp:
                levels+=1
                                            

                
            if levels+1:
                print("")
                print("𝓛𝓔𝓥𝓔𝓛 𝓤𝓟!!")
                print("")
                nowexp=0
                maxexp+=200
                print('monsters has been more stronger!!(damage +100)')
                levelupdebufdamg=levelupdebufdamg+100
                print("monsters has been more stronger!!(hp +200)")
                levelupdebufmonhp=200
                monsterhp+=levelupdebufmonhp
                fullhp=fullhp+500
                if hp >= fullhp:
                    print("you have full hp")
                if hp < fullhp:
                    print('last hp =>',hp)
                    healhp=int(fullhp-hp)
                    hp+=healhp
                    print('your now hp =>',hp)


                break
            elif hp <= 0:
                print()
                print(f'you are dead by {mon}')
                hp=1500
                mp=150
                break
    


    if levels == 50:
        break                

    
golamskill=['punching(150)','Throwing_stones(750)']
gobulinskill=['punching(50)','javelin throw(100)']
orkskill=['axing(600)','crushing(950)']
corruptedfireskill=['flaming fire(250)','soal fire(500)']
spiderskill=['launch web(200)','biting(500)']
posionousmushroomskill=['posion shot(50)']
fishskill=['water shot(10)','tailspin(5)']
storgfishskill=['body headbutt(300)','tailspin(650)']
fishman=['trident throw(350)','call the waves(550)']
shadowskill=['call devil(450)','lock in the dark(750)']
slimeskill=['body slap(50)']
whichskill=['fire magic(250)','water magic(250)','dark magic(450)','lightmagic(450)']
frogskill=['tongue smash(350)','water cannon(500)']
villagerskil=['talk(-800)','hello~(-450)']
traderskill=['trade(0)']
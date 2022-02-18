import sys, pygame
from pygame import *

#Global Variables


pygame.display.init()
pygame.font.init()

#Display screen
SCREEN = pygame.display.set_mode((700,500))

#I might make the window scalable meaning the player can adjust the window
WINDOW_SCREEN = pygame.display.get_window_size()


#Init text
myfont = pygame.font.SysFont('freesansbold.ttf', 30)
textFont = pygame.font.SysFont('freesansbold.ttf', 28)

#Colors
white = (255,255,255)
black = (0,0,0)

#Texts that will be used often
choice = myfont.render("What do you do?", False, white)
instruct = myfont.render("Press a Letter on your keyboard", False, white)
enterToExit = textFont.render("PRESS ANY KEY TO EXIT.",False,white)
enterToProgress = textFont.render("PRESS ANY KEY TO CONTINUE", False, white)
toBeContinued = textFont.render("TO BE CONTINUED?", False, white)

#Mouse shenanigans
MOUSE = pygame.mouse

class States: 

    def __init__(self, isFirstTimeWest, isRetuned):
        self.isFirstimeWest = isFirstTimeWest
        self.isReturned = isRetuned
        self.keyRetrived = False
        self.attemptCount = 0
        self.keyLock = False
        self.hasWeapon = False

    def theKeyRetrived(self):
        self.keyRetrived = True
    
    def isKeyAvail(self):
        return self.keyRetrived

    def increaseAttempt(self):
        self.attemptCount += 1

    def checkAttempt(self):
        return self.attemptCount
    
    def returnedSetTrue(self):
        self.isReturned = True
    
    def resetAttemptCount (self):
        self.attemptCount = 0

    def firstTimeWestSetFalse(self):
        self. isFirstimeWest = False
    
    def checkKeyLockState(self):
        return self.keyLock

    def setKeyLockTrue(self):
        self.keyLock = True
    
    def setKeyLockFalse(self):
        self.keyLock = False
    
    def isWeaponPresent(self):
        return self.hasWeapon
    
    def weaponIsPresent(self):
        self.hasWeapon = True
    
    def weaponType (self, weapon):
        self.weaponType = weapon

    def whatWeaponType(self):
        return self.weaponType

    
funcStates = States(True, False)


def main():
    
    #The text themselves MAIN MENU
    textTitle = myfont.render("ADVENTURE CALL ", False, white)
    textTitle1 = myfont.render("STARRING YOU AND FALCONHOOF ", False, white)
    startButton = myfont.render("CLICK HERE TO START", False, white)

    mainMenu = 1

    while (mainMenu):
        
        SCREEN.fill((0,0,0))

        SCREEN.blit(textTitle, (WINDOW_SCREEN[0]/ 5 , WINDOW_SCREEN[1]/4))
        SCREEN.blit(textTitle1, (WINDOW_SCREEN[0]/ 5, WINDOW_SCREEN[1]/ 3))
        SCREEN.blit(startButton, (WINDOW_SCREEN[0]/5, WINDOW_SCREEN[1]/ 1.5))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if (MOUSE.get_pos()[0] > WINDOW_SCREEN[0]/5 and
                    WINDOW_SCREEN[0]/5 + 200 > MOUSE.get_pos()[0]):
                    if (MOUSE.get_pos()[1] > WINDOW_SCREEN[1]/2 and
                        WINDOW_SCREEN[1]/1.4 > MOUSE.get_pos()[1]):
                        firstSlide()


        pygame.display.update()
        

def firstSlide():

    textLine1 = textFont.render("You are in the dark castle of the grey halls with no memory whatsoever", 
                             False, white)
    textLine2 = textFont.render("You fell cold and scared and you want to escape", False, white)
    textLine3 = textFont.render("To the East is a hallway that leads to the Armory", False, white)
    textLine4 = textFont.render("To the West leads to the bedroom", False, white)
    textLine5 = textFont.render("And to the North leads to the outside", False, white)

    altMessage = textFont.render("Hi, there! You're back! Here are the options again.", False, white)

    altEastMessage = textFont.render("You have a weapon already...", False, white)

    choiceA = textFont.render("A. Go West", False, white)
    choiceB = textFont.render("B. Go East", False, white)
    choiceC = textFont.render("C. Go North", False, white)

    first = 1
    bringMessage = False

    while(first):
    
        SCREEN.fill(black)

        
        if  not (funcStates.isReturned):
            SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20 , 90))
            SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))
            SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/ 20, 150))
            SCREEN.blit (textLine4, (WINDOW_SCREEN[0]/ 20, 180))
            SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/ 20, 210))

        else:
            SCREEN.blit(altMessage, (WINDOW_SCREEN[0]/20, 60))
            SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 90))
            SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 120))
            SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 150))
          
        if (bringMessage):
            SCREEN.blit(altEastMessage, (WINDOW_SCREEN[0]/20, 170)) 

        SCREEN.blit(choice, (WINDOW_SCREEN[0]/ 20, 300))
        SCREEN.blit(instruct,(WINDOW_SCREEN[0]/20, 325))
        
        SCREEN.blit(choiceA, (WINDOW_SCREEN[0]/20, 375))
        SCREEN.blit(choiceB, (WINDOW_SCREEN[0]/20,400))
        SCREEN.blit(choiceC, (WINDOW_SCREEN[0]/20, 425))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if(funcStates.isFirstimeWest):
                        west()
                    else:
                        westA()

                if event.key == pygame.K_b:

                    if (funcStates.isWeaponPresent() != True):

                        if (funcStates.isKeyAvail()):
                            eastInArm() 
                        else:
                            east()
                    else:
                        bringMessage = True
                
                if event.key == pygame.K_c:

                    if not (funcStates.isWeaponPresent()):
                        noWeaponEnding()

                    else:
                        endingPrompt()

        
        pygame.display.update()

"""BEDROOM SCENE """

def west():

    textLine1 = textFont.render("You enter the bedroom. You smell the perfume of lavender.", False, white)
    textLine2 = textFont.render("You realized you saw a princess wearing a blue gown, crying.", False, white)
    textLine3 = textFont.render("She looked up, saw you and said: ", False, white)
    textLine4 = textFont.render("\"Oh! Traveller! You have scared me! What is it that you want?\"", False, white)

    choiceA = textFont.render("A. Ask why you are in the castle of Grey Walls", False, white)
    choiceB = textFont.render("B. Assault her legally", False, white)
    choiceC = textFont.render("C. Ask why she was crying", False, white)

    westSlide = 1

    while(westSlide):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/ 20, 100))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 130))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 160))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 190))

        SCREEN.blit(choice, (WINDOW_SCREEN[0]/20, 300))
        SCREEN.blit(instruct, (WINDOW_SCREEN[0]/20, 325))

        SCREEN.blit(choiceA, (WINDOW_SCREEN[0]/20, 375))
        SCREEN.blit(choiceB, (WINDOW_SCREEN[0]/20, 400))
        SCREEN.blit(choiceC, (WINDOW_SCREEN[0]/20, 425))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    westA()
                if event.key== pygame.K_b:
                    gameOverPedo()
                if event.key == pygame.K_c:
                    gameOverBored()


    
        pygame.display.update()

def westA(badMoment = False):

    textLine1 = textFont.render("The Princess said, \"You don't know? You were sent in the brig for ", False, white)
    textLine2 = textFont.render(" tresspassing. Oh wait, I forgot. GUARDS! THE BASTARD IS HERE!\"", False, white)
    textLine3 = textFont.render("You panicked and pancicked that you even strangled the young hag ", False, white)
    textLine4 = textFont.render("to sleep. However, on her neck, you saw a necklace with a key on it.", False,white)
    textLine5 = textFont.render("You take it off and keep it.",False, white)
    textLine6 = textFont.render("You got yourself a key of the armory, you arse!",False,white)

    altMessage = textFont.render("Oh! You're back! Don't worry, she's still asleep", False, white)

    altMessageFromC = textFont.render ("I hope you become stronger, traveller!", False,white)

    funcStates.theKeyRetrived()

    choiceA = textFont.render("A. Sleep with the Princess",False,white)
    choiceB = textFont.render("B. Go back to the main hall",False,white)
    choiceC = textFont.render("C. Commit Suicide",False,white)

    westSlideA = 1

    while (westSlideA):
        SCREEN.fill(black)

        if (funcStates.isFirstimeWest):
            SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
            SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
            SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 120))
            SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))
            SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 180))
            SCREEN.blit(textLine6, (WINDOW_SCREEN[0]/20, 210))
        else:
            SCREEN.blit(altMessage, (WINDOW_SCREEN[0]/20, 60))

        if (badMoment):
            SCREEN.blit(altMessageFromC, (WINDOW_SCREEN[0]/20, 90))


        SCREEN.blit(choice, (WINDOW_SCREEN[0]/20,300))
        SCREEN.blit(instruct, (WINDOW_SCREEN[0]/20, 325))

        SCREEN.blit(choiceA, (WINDOW_SCREEN[0]/20, 375))
        SCREEN.blit(choiceB, (WINDOW_SCREEN[0]/20, 400))
        SCREEN.blit(choiceC, (WINDOW_SCREEN[0]/20, 425))

        for event in pygame.event.get():

            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    gameOverPrincess()
                
                if event.key == pygame.K_b:
                    funcStates.returnedSetTrue()
                    funcStates.firstTimeWestSetFalse()
                    firstSlide()
                
                if event.key == pygame.K_c:
                    funcStates.firstTimeWestSetFalse()
                    suicideMoment()
                

        pygame.display.update()


"""GAME OVER SCENARIOS AND MISC."""


def gameOverPedo():
    gameOverPe = 1

    textLine1 = textFont.render("You forcefully held both of her arms and pinned her to bed. However...",False,white)
    textLine2 = textFont.render("\"This is the FBI! We have you surrounded!\"", False, white)
    textLine3 = textFont.render("You were startled by the suddent call of freedom",False, white)
    textLine4 = textFont.render("and they pinned you down instead.", False, white)
    lessonLine = textFont.render("LESSON: NO TO ASSAULT!", False,white)



    while (gameOverPe):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20,120))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))

        SCREEN.blit(lessonLine, (WINDOW_SCREEN[0]/20, 200))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 270))

        for event in pygame.event.get():

            if event.type == QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()


def gameOverBored():
    gameOverBor = 1

    textLine1 = textFont.render("The Princess said, \"Oh Nothing. I was paid to cry. In fact...\"", False,white)
    textLine2 = textFont.render("She went on describing her past careers", False, white)
    textLine3 = textFont.render("From how she escaped her father's ballsack, and into the depressing", False,white)
    textLine4 = textFont.render("grim world, how she was once an otaku nut-head, and became a ", False, white)
    textLine5 = textFont.render("yandere once in her life, and to how she had the role as the princess", False,white)
    textLine6 = textFont. render("The story was done but then you realized you were sleeping the ", False,white)
    textLine7 = textFont.render("the whole time. The Princess then shot you with a SPAS12", False,white)

    lessonLine = textFont.render("LESSON: ALWAYS LISTEN",False,white)

    while(gameOverBor):

        SCREEN.fill((0,0,0))

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 30))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20,90))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine6, (WINDOW_SCREEN[0]/20,180))
        SCREEN.blit(textLine7, (WINDOW_SCREEN[0]/20, 210))

        SCREEN.blit(lessonLine, (WINDOW_SCREEN[0]/20, 300))
        SCREEN.blit(enterToExit,(WINDOW_SCREEN[0]/20, 330))
       

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def gameOverPrincess():

    gameOverPr = 1

    textLine1 = textFont.render("You are becoming horny, seeing the princess' body.", False,white)
    textLine2 = textFont.render("You took off your clothes and you start to grab her.",False,white)
    textLine3 = textFont.render("But, out of the blue, the FBI invaded the castle.",False,white)
    textLine4 = textFont.render("You got taken away from the castle and to pedo jail.",False,white)

    endMessage = textFont.render("LESSON: DON'T BE A PEDO.",False,white)

    while(gameOverPr):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20,100))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 130))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 160))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 190))

        SCREEN.blit(endMessage, (WINDOW_SCREEN[0]/20, 270))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 300))

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def suicideMoment():

    suicideTime = 1

    textLine1 = textFont.render("Oh! So you wanna die, eh?", False,white)
    textLine2 = textFont.render("Man, you're really a wuss, you know that?", False, white)
    textLine3 = textFont.render("I don't know why you'd do it, maybe because you're so called \"friends\'", False,white)
    textLine4 = textFont.render("are doing a lot better than you ain't it?", False,white)
    textLine5 = textFont.render("Or, maybe, you're favorite fictional character died for nothing?", False, white)
    textLine6 = textFont.render("Whatever maybe, you'd always take the easy way out...", False, white)

    funFact = textFont.render("Oh! Fun fact: THIS IS A GAME STUPID! YOU'RE NOT REALLY DEAD!", False,white)

    getOutOfHere = textFont.render("Press any key to quit moping", False,white)

    while (suicideTime):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 180))
        SCREEN.blit(textLine6, (WINDOW_SCREEN[0]/20, 210))

        SCREEN.blit(funFact, (WINDOW_SCREEN[0]/20, 240))

        SCREEN.blit(getOutOfHere, (WINDOW_SCREEN[0]/20, 300))



        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                westA(True)

        pygame.display.update()


"""END OF THE BED ROOM SCENE"""



"""Armory when the key is not retrived"""

def east(cryNow = False):
    time = 30
    pygame.time.set_timer(NUMEVENTS - 1, 1000)

    isShowCry = False
    eastSlideArmDoorA = 1

    textLine1 = textFont.render("You are infront of a wooden door.", False, white)
    textLine2 = textFont.render("However, you juggled the handle but it doesn't open...", False, white)

    firstMessage = textFont.render("You waited but nothing happened...", False, white)
    secondMessage = textFont.render("You are wasting your time...nothing happened", False,white)
    thirdMessage = textFont.render("Are you that stubborn? Nothing happened!", False, white)

    cryMessage = textFont.render("You rolled down on the floor and cried. Nothing happens", False, white)

    choiceA = textFont.render("A. Go back.", False, white)
    choiceB = textFont.render("B. Wait.", False, white)
    choiceC = textFont.render("C. Lie down on the floor and cry.", False, white)

    while(eastSlideArmDoorA):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 100))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 130))

        SCREEN.blit(choice, (WINDOW_SCREEN[0]/20, 300))
        SCREEN.blit(instruct, (WINDOW_SCREEN[0]/20, 325))

        if (funcStates.checkAttempt() > 0):

            if(funcStates.checkAttempt() < 5):
                SCREEN.blit(firstMessage, (WINDOW_SCREEN[0]/20, 160))
            elif (funcStates.checkAttempt() >= 5 and funcStates.checkAttempt() < 10):
                SCREEN.blit(secondMessage, (WINDOW_SCREEN[0]/20, 160))
            elif (funcStates.checkAttempt() >= 10 and funcStates.checkAttempt() < 15):
                SCREEN.blit(thirdMessage, (WINDOW_SCREEN[0]/20, 160))
            else:
                waitingGameEnd()
        
        if (funcStates.checkAttempt() > 0):
            SCREEN.blit(textFont.render("Number of attempts: "+ str(funcStates.checkAttempt()), False, white), (WINDOW_SCREEN[0]/20, 210))

        if (isShowCry and time > 0):
            SCREEN.blit(cryMessage, (WINDOW_SCREEN[0]/20, 230))
            

        SCREEN.blit(choiceA, (WINDOW_SCREEN[0]/20, 375))
        SCREEN.blit(choiceB, (WINDOW_SCREEN[0]/20, 400))
        SCREEN.blit(choiceC, (WINDOW_SCREEN[0]/20, 425))

        
        for event in pygame.event.get():
            
            if isShowCry and time > 0:
                time -= 1
                print(time)
            
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    funcStates.returnedSetTrue()
                    funcStates.resetAttemptCount()
                    firstSlide()
                
                if event.key == pygame.K_b:
                    funcStates.increaseAttempt()
                
                if event.key == pygame.K_c:
                    isShowCry = True
                       

        pygame.display.update()


def waitingGameEnd():
    gameOver = 1

    textLine1 = textFont.render("The producer of the show decided to cancel the show", False, white)
    textLine2 = textFont.render("on the spot. You are now left on the black void of", False,white)
    textLine3 = textFont.render("nothingness... and a debt to pay my bills.", False,white)

    lessonLine = textFont.render("LESSON: DON'T WAIT TOO MUCH!", False,white)
    while (gameOver):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 160))

        SCREEN.blit(lessonLine, (WINDOW_SCREEN[0]/20, 300))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 375))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

"""ARMORY WHEN THE KEY IS RETRIVED"""

def eastInArm():
    eastSlideInArm = 1

    textLine1 = textFont.render("You see the door and opened it...",False, white)
    textLine2 = textFont.render("It actually leads to the armory!", False, white)
    textLine3 = textFont.render("From there you found a sword, itak, and an AK-47", False, white)

    promptLine = textFont.render("Which one of them are you going to choose?", False, white)

    choiceA = textFont.render("A. AK-47", False, white)
    choiceB = textFont.render("B. Itak", False,white)
    choiceC = textFont.render("C. Sword", False,white)

    while (eastSlideInArm):

        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 160))

        SCREEN.blit(promptLine,(WINDOW_SCREEN[0]/20, 300))
        SCREEN.blit(instruct, (WINDOW_SCREEN[0]/20, 325))

        SCREEN.blit(choiceA, (WINDOW_SCREEN[0]/20, 375))
        SCREEN.blit(choiceB, (WINDOW_SCREEN[0]/20, 400))
        SCREEN.blit(choiceC, (WINDOW_SCREEN[0]/20, 425))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                funcStates.weaponIsPresent()
                if event.key == pygame.K_a:
                    funcStates.weaponType("AK-47")
                    ak47()
                
                if event.key == pygame.K_b:
                    funcStates.weaponType("ITAK")
                    itak()
                
                if event.key == pygame.K_c:
                    funcStates.weaponType("SWORD")
                    sword()

        pygame.display.update()

def ak47():

    loop = 1

    textLine1 = textFont.render("You picked up the AK-47.", False, white)
    textLine2 = textFont.render("You feel the dead Soviets are cheering for you...", False, white)


    while (loop):

        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))

        SCREEN.blit(enterToProgress, (WINDOW_SCREEN[0]/20, 200))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                firstSlide()

        pygame.display.update()


def itak():

   loop = 1
   
   textLine1 = textFont.render("You picked up the itak.", False, white) 
   textLine2 = textFont.render("You feel the dead Filipinos are cheering for you...", False, white)
   
   while (loop):

        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))

        SCREEN.blit(enterToProgress, (WINDOW_SCREEN[0]/20, 200))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                firstSlide()

        pygame.display.update()

def sword():


   loop = 1
   
   textLine1 = textFont.render("You picked up the sword.", False, white) 
   textLine2 = textFont.render("No one's cheering for you...except your own dead/alive mom", False, white)
   
   while (loop):

        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))

        SCREEN.blit(enterToProgress, (WINDOW_SCREEN[0]/20, 200))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                firstSlide()

        pygame.display.update()


def endingPrompt():
    slide = 1

    textLine1 = textFont.render("You stepped outside of the castle doors.", False,white)
    textLine2 = textFont.render("You saw hordes of men who donned in armor and swords.", False,white)
    textLine3 = textFont.render("There are arcehmen, swordsmen, spearmen, and hot chicks with guns.", False, white)
    
    textLine4 = textFont.render("You picked up a weapon from the armory, mind you...", False, white)

    while (slide):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 180))

        SCREEN.blit(enterToProgress, (WINDOW_SCREEN[0]/20, 210))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (funcStates.whatWeaponType() == "AK-47"):
                    akEnding()
                elif (funcStates.whatWeaponType() == "ITAK"):
                    itakEnding()
                elif (funcStates.whatWeaponType() == "SWORD"):
                    swordEnding()
        
        pygame.display.update()
                    
"""ENDINGS """ 
def noWeaponEnding():

    northSlide = 1

    textLine1 = textFont.render("You opened the gate, leading to the outside.", False,white)
    textLine2 = textFont.render("However...you were slain and shot dead...", False, white)
    textLine3 = textFont.render("...by the producers of the show.", False, white)

    lessonLine = textFont.render("LESSON: EASY THINGS ARE NOT \"ALWAYS\" THE SOLUTION", False, white)

    while (northSlide):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 150))

        SCREEN.blit(lessonLine, (WINDOW_SCREEN[0]/20, 200))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 270))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    

def akEnding():
    northSlideEnd1 = 1

    textLine1 = textFont.render("You brought out your AK-47 and began blasting.", False, white)
    textLine2 = textFont.render("You suddenly hear the C&C Soviet theme as you screm", False, white)
    textLine3 = textFont.render("the name of Mother Russa as you plow down the worthless bastards.", False, white)
    textLine4 = textFont.render("From then on, you rode on your T-34 and off you go with the", False, white)
    textLine5 = textFont.render("red flag in your hand...", False, white)

    while (northSlideEnd1):
        SCREEN.fill(black)

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 180))

        SCREEN.blit(toBeContinued, (WINDOW_SCREEN[0]/20, 300))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 340))

        for event in pygame.event.get():

            if event.type == QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def itakEnding ():

    northSlideEnd2 = 1

    textLine1 = textFont.render("You brought out the itak and began slashing through.", False, white)
    textLine2 = textFont.render("Slashing and dicing, you shouted the name of your people.", False, white)
    textLine3 = textFont.render("Then, your dead Filipino ancestors raised up from the dead.", False, white)
    textLine4 = textFont.render("They toled you to get to the beaches because the Spaniards", False, white)
    textLine5 = textFont.render("are coming again to colonize you...", False, white)

    while (northSlideEnd2):
        SCREEN.fill((0,0,0))

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 180))

        SCREEN.blit(toBeContinued, (WINDOW_SCREEN[0]/20, 300))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 340))

        for event in pygame.event.get():

            if event.type == QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()

def swordEnding ():

    northSlideEnd3 = 1

    textLine1 = textFont.render("You brought out your sword and began dashing through. ", False, white)
    textLine2 = textFont.render("You closed your eyes, hoping you killed one of them.", False, white)
    textLine3 = textFont.render("Suddenly, the sword instatly broke. You were worried.", False, white)
    textLine4 = textFont.render("You looked at the handle, only to see it was made in China.", False, white)
    textLine5 = textFont.render("You shivered and cower in fear for the worse... ", False, white)

    while (northSlideEnd3):
        SCREEN.fill((0,0,0))

        SCREEN.blit(textLine1, (WINDOW_SCREEN[0]/20, 60))
        SCREEN.blit(textLine2, (WINDOW_SCREEN[0]/20, 90))
        SCREEN.blit(textLine3, (WINDOW_SCREEN[0]/20, 120))
        SCREEN.blit(textLine4, (WINDOW_SCREEN[0]/20, 150))
        SCREEN.blit(textLine5, (WINDOW_SCREEN[0]/20, 180))

        SCREEN.blit(toBeContinued, (WINDOW_SCREEN[0]/20, 300))

        SCREEN.blit(enterToExit, (WINDOW_SCREEN[0]/20, 340))


        for event in pygame.event.get():

            if event.type == QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()

    

if (__name__ == "__main__"):
    main()

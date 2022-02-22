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
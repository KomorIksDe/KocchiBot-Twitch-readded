from time import time
from random import randint

start = int(time())

def getUpTime():
    global start
    seconds = int(time()) - start
    minutes = int(seconds/60)
    hours   = int(minutes/60)
    seconds = seconds - hours*3600 - minutes*60
    
    return "Stream has been live for: {}h {}m {}s.".format(hours, minutes, seconds)


def randomizePhrase():
    phrases = [
        "I'm engaged",
        "I'm not attracted to 3D men",
        "I've run out of ideas",
        "I'll find someone who'll fill this list with a lot of FUNNY phrases eventually",
		"Please save me from the suffer",
		"Haha nihilist M E M E S",
		"I take part in elite's things you kno'",
		"One more phrase to make sure it's working correctly"
    ]
    
    return phrases[randint(0, len(phrases)-1)]


def lookForCapsLock(message):
    capsCounter = 0
    
    if(len(message) > 10):
        for char in message:
            if char == char.upper():
                capsCounter += 1
        if float(capsCounter)/float(len(message)) > 0.6:
            return True
        else:
            return False
    else:
        return False


def lookForSwears(message):
    swearsCounter = 0
    swears = [
        "kurwa",
        "chuj"
    ]
    
    for element in message.split():
        for swear in swears:
            if element.lower() == swear:
                swearsCounter += 1
    if swearsCounter > 5:
        return True
    else:
        return False

    
def lookForLongMsg(message):
    if(len(message) > 480):
        return True
    else:
        return False
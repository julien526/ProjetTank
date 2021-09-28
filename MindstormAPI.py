import threading
from time import sleep
import CommandTank as cd
from pynput import keyboard


tank = cd.Connecter(cd.MAC)

#Get called when a key is press
def keyPressHandler(key):
    name = key.char
    print(name)
    
    if(name == 'w'):
        cd.Move(100, tank)
        
    if(name == 's'):
        cd.Move (-100, tank)
        
    if(name == 'a'):
        print("Turn left")
        cd.TurnLeft(100, tank)
        
    if(name == 'd'):
        print('Turn right')
        cd.TurnRight(100, tank)        
        
    if (name == 'q'):
        cd.stop(cd.ALL_MOTORS, tank)
        raise Exception("stop that shit")
        
#Get called when a key is release
def keyReleaseHandler(key):
    name = key.char
    print(name)
    
    if (name == 'w' or name == 'd' or name == 's' or name == 'a'):
        print('Arret')
        cd.stop(cd.ALL_MOTORS, tank)



with keyboard.Listener(
        on_press=keyPressHandler,
        on_release=keyReleaseHandler) as listener:
    listener.join()







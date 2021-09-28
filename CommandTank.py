import ev3_dc as ev3
from ev3_dc.ev3 import EV3
from ev3_dc.sound import TRIAD

#Constant
global device
MAC = "00:16:53:48:91:73"
ALL_MOTORS = [15]
FRONT_MOTORS = [ev3.PORT_C, ev3.PORT_D,]
BACK_MOTORS = [ev3.PORT_A, ev3.PORT_B]
LEFT_SIDE_MOTORS = [ev3.PORT_A, ev3.PORT_C]
RIGHT_SIDE_MOTORS = [ev3.PORT_B, ev3.PORT_D]


#Connexion to the mindstorm controller
def Connecter(MAC):
    my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=MAC)
    my_ev3.verbosity = 1
    return my_ev3
    

#Start chosen motor for undefined period of time
def Start(speed, motorlist, device):
    
    motors = 0
    for m in motorlist:
        motors += m

    opStart = b''.join((
        ev3.opOutput_Power,
        ev3.LCX(0),
        ev3.LCX(motors),
        ev3.LCX(speed),
        ev3.opOutput_Start,
        ev3.LCX(0),
        ev3.LCX(motors)
    ))
    device.send_direct_cmd(opStart)

#Stop chosen motor
def stop(motorlist, device):
    
    motors = 0
    for m in motorlist:
        motors += m

    device.send_direct_cmd(
        b''.join((
            ev3.opOutput_Stop,
            ev3.LCX(0),
            ev3.LCX(motors),
            ev3.LCX(0)
        ))
    )

#Move foward if speed positive and backward if negative
def Move(speed,device):
    print("Reculer" if speed < 0 else "Avancer")
    Start(-speed,FRONT_MOTORS,device)
    Start(speed,BACK_MOTORS,device)
    
#Turn left
def TurnLeft(speed,device):
    print('Tourne à droite')
    Start(speed, [RIGHT_SIDE_MOTORS[0]], device)
    Start(-speed, [RIGHT_SIDE_MOTORS[1]], device)    
 
#Turn right    
def TurnRight(speed,device):
    print('Tourne à droite')
    Start(speed, [LEFT_SIDE_MOTORS[0]], device)
    Start(-speed, [LEFT_SIDE_MOTORS[1]], device)


#Prueba Final robot levantado a 90 grados
from time import *
from adafruit_servokit import Servokit #en estas dos lineas importamos 

#establecer canales respecto a la cantidad de canales del servo 
#8 para servo FeatherWing de 8x12 bit PWM, 16 pata Sheld/Hat/Bonnet
kit = Servokit(channels=16)

#Se colocan los angulos iniciales de todos los servos 
kit.servo[0].angle=0 #servo conectado al canal 0 a 0 grados 
kit.servo[1].angle=0 #servo conectado al canal 1 a 0 grados 
kit.servo[2].angle=0 #servo conectado al canal 2 a 0 grados 
kit.servo[3].angle=0 #servo conectado al canal 3 a 0 grados 
kit.servo[4].angle=0 #servo conectado al canal 4 a 0 grados 
kit.servo[5].angle=0 #servo conectado al canal 5 a 0 grados

def servo1():
	kit.servo[0].angle=0 #servo1 conectado en el canal 0 se posiciona a 0 grados 

def servo2():
	kit.servo[1].angle=90 #servo2 conectado en el canal 1 se posiciona a 90 grados 

def servo3():
	kit.servo[5].angle=90 #servo5 conectado en el canal 1 se posiciona a 90 grados 

def servo4():
	kit.servo[2].angle=0 #servo4 conectado en el canal 2 se posiciona a 0 grados 

def servo5():
	kit.servo[3].angle=0 #servo5 conectado en el canal 3 se posiciona a 0 grados 

def servo6():
	kit.servo[4].angle=0 #servo6 conectado en el canal 4 se posiciona a 0 grados 

#Se crea un bucle 
while True:
	servo1()
	sleep(0.5)
	servo2()
	sleep(0.5)
	servo3()
	sleep(0.5)
	servo4()
	sleep(0.5)
	servo5()
	sleep(0.5)
	servo6()
	sleep(0.5)
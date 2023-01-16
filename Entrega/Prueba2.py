#Prueba 2 conexion de todos los servomotores 
import time 
from adafruit_servokit import Servokit #en estas dos lineas importamos las librerias 

#establecer canales respecto a la cantidad de canales del servo 
#8 para servo FeatherWing de 8x12 bit PWM, 16 para Sheld/Hat/Bonnet
kit = Servokit(channels=16)

#servo1
kit.servo[0].angle=0 #mover el servo conectado al canal 0 a 0 grados 
kit.continuous_servo[1].throttle=1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[1].throttle=-1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia atras
time.sleep(1)
kit.servo[0].angle=0 #mover el servo conectado al canal 0 a 0 grados 
kit.continuous_servo[1].throttle=0 #detiene el servo de rotación continua conectado al canal 1 

#servo2
kit.servo[2].angle=0 #mover el servo conectado al canal 2 a 0 grados 
kit.continuous_servo[1].throttle=1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[1].throttle=-1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia atras
time.sleep(1)
kit.servo[2].angle=0 #mover el servo conectado al canal 2 a 0 grados 
kit.continuous_servo[1].throttle=0 #detiene el servo de rotación continua conectado al canal 1 

#servo4
kit.servo[3].angle=90 #mover el servo conectado al canal 3 a 90 grados 
kit.continuous_servo[2].throttle=1 #iniciar el servo de rotación continua conectado al canal 2 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[2].throttle=-1 #iniciar el servo de rotación continua conectado al canal 2 a toda velocidad hacia atras
time.sleep(1)
kit.servo[3].angle=0 #mover el servo conectado al canal 3 a 0 grados 
kit.continuous_servo[2].throttle=0 #detiene el servo de rotación continua conectado al canal 2 

#servo5
kit.servo[4].angle=90 #mover el servo conectado al canal 4 a 90 grados 
kit.continuous_servo[3].throttle=1 #iniciar el servo de rotación continua conectado al canal 3 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[3].throttle=-1 #iniciar el servo de rotación continua conectado al canal 3 a toda velocidad hacia atras
time.sleep(1)
kit.servo[4].angle=0 #mover el servo conectado al canal 4 a 0 grados 
kit.continuous_servo[3].throttle=0 #detiene el servo de rotación continua conectado al canal 3 

#servo6
kit.servo[5].angle=90 #mover el servo conectado al canal 5 a 90 grados 
kit.continuous_servo[4].throttle=1 #iniciar el servo de rotación continua conectado al canal 4 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[4].throttle=-1 #iniciar el servo de rotación continua conectado al canal 4 a toda velocidad hacia atras
time.sleep(1)
kit.servo[5].angle=0 #mover el servo conectado al canal 5 a 0 grados 
kit.continuous_servo[4].throttle=0 #detiene el servo de rotación continua conectado al canal 4
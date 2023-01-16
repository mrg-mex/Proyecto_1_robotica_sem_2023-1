#Prueba 1 del servomotor 0 ubicado en el canal 0 con continuacion del servo 1 ubicado en el canal 1
import time 
from adafruit_servokit import Servokit #en estas dos lineas importamos las librerias  

#establecer canales respecto a la cantidad de canales del servo 
#8 para servo FeatherWing de 8x12 bit PWM, 16 para Sheld/Hat/Bonnet
kit = Servokit(channels=16) #nuestro caso fue de 16

kit.servo[0].angle=180 #mover el servo conectado al canal 0 a 180 grados 
kit.continuous_servo[1].throttle=1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia adelante
time.sleep(1) #tiempo de espera 
kit.continuous_servo[1].throttle=-1 #iniciar el servo de rotación continua conectado al canal 1 a toda velocidad hacia atras
time.sleep(1)
kit.servo[0].angle=0 #mover el servo conectado al canal 0 a 0 grados 
kit.continuous_servo[1].throttle=0 #detiene el servo de rotación continua conectado al canal 1 

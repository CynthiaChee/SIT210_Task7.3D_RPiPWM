import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 18
LED = 7

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

def distance():
    GPIO.output(TRIG, False)
    print("Measuring distance...")
    time.sleep(1)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start = time.time()
    stop = time.time()
    
    while GPIO.input(ECHO) == 0:
        start = time.time()
    
    while GPIO.input(ECHO) == 1:
        stop = time.time()
        
    timeelapsed = stop - start
    distance = (timeelapsed * 34300)/2
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("%.1f cm" %dist)
            
            GPIO.output(LED,GPIO.HIGH)
            time.sleep(dist/10)
            GPIO.output(LED,GPIO.LOW)
            time.sleep(dist/10)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Stop")
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
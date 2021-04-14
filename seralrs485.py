import serial
import serial.rs485
import time
import RPi.GPIO as GPIO


TXDEN_1=7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TXDEN_1, GPIO.OUT, initial=GPIO.HIGH)


ser=serial.rs485.RS485(port='/dev/ttySC0',baudrate=9600,timeout=5,parity=serial.PARITY_EVEN)
ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=False, 
                                            rts_level_for_rx=False,
                                            delay_before_tx=0.0,
                                            delay_before_rx=-0.0)                                            

SendFrame =b'\x01\x03\x00\x02\x00\x01\x25\xCA'
#SendFrame='\x01\x06\x00\x09\x00\x01\x98\x08' #0x0898
#SendFrame ='\x01\x06\x00\x06\x00\x0A\xE9\xCC'  #0AE8 #0xCA29 #0xCCE9 write reg 6

#SendFrame='\x01\x03\x00\x00\x00\x0e\xc4\x0e' #0x0EC4

while True:
	GPIO.output(TXDEN_1, GPIO.HIGH)
    ser.write(SendFrame)
    GPIO.output(TXDEN_1, GPIO.LOW) #read
    coming_data = ser.inWaiting()
    print "comming_data:",coming_data
    x=ser.read(ser.inWaiting())
    print repr(x)
    print "ok"
    time.sleep(2)

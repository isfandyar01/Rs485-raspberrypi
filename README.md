MODBUS RS485 Raspberry Pi
INTRODUCTION TO Rs485/Modbus RTU:
RS-485 is an asynchronous serial communication protocol which doesn't not require clock. It uses a technique called differential signal to transfer binary data from one device to another.
Differential signal method works by creating a differential voltage by using a positive and negative 5V. It provides a Half-Duplex communication when using two wires and Full-Duplex requires 4 fours wires. 
 
Data Packet of Rs485:
Modbus RTU encodes data as binary and uses big-endian encoding for 16-bit values. This means that the most significant byte of a 16-bit word is sent first.
Lets suppose that we want to read register 1 of our modbus slave 
our data packet will look like this
slave id (repeats own id) 
| function code (repeats requested code) 
| | address of first register to read (2 bytes)
| | | number of registers to read 
| | | | checksum(2bytes) 
| | | | | 
01 03 00 01 00 01 D5 CA
The reply from slave will look like this
Slave id
| Function code
| | number of bytes of data
| | | the value of register (2bytes)
| | | |
| | | | checksum (2bytes)
| | | | |
01 03 02 00 01 25 CA
Raspberry Pi Rs485 Modbus:
Now we will see how to do rs485 Modbus protocol in raspberry pi without use of any library of Modbus 
What we will use instead is rs485 section of serial python library. 
 
Components required: 
1: Raspberry pi raspbian installed
2: Usb to rs485
3: Max485 ttl to rs485
4:pymodbus slave software: https://sourceforge.net/projects/pymodslave/
Usb to rs485
Max485 module
Wiring:
Max485 to raspberry pi:
Make sure DE and RE of max485 are shorted together
MAX485 Raspberry Pi
DI      GPIO14
DE RE   GPIO4
R0      GPIO15(RX)
VCC     5V
GND     GND
Usb rs485 with max485:
Usb485 Max485
A      A
B       B
Programming Raspberry Pi as Master using Python
Enabling the UART (Serial Port) pins in Raspberry Pi: only bold
Before using UART pins in Raspberry Pi, it needs to be enabled. Follow the steps below to enable the UART (Serial) Pins in Raspberry Pi board.
1. Open a terminal and type sudo raspi-config
2. Select Interfacing options
3. And then select serial
4. Then click on 'No' (This is used to disable Linux UART console)
5. After that exit the raspi-config
6. Reboot the Pi
Now Serial port is ready to be used.

Open Terminal and install these libraries:
sudo apt-get update 
sudo apt-get install python-pip 
sudo apt-get install python-pil 
sudo pip install RPi.GPIO 
sudo apt-get install python-serial 
sudo pip install serial 
sudo pip install pyserial



Connect usb to rs485 to your pc or laptop 
 
Open pymodbus slave software on your pc or laptop
go to option modbus rtu and select following settings:
Click on holding register tab and make sure hex is selected:
Click on connect and you will see registers
Write any value on address 1
Make connection of max485 with raspberry pi as shown in table above 
also make connection of usb and max485 as shown in table above
After all the connections are made run the python file


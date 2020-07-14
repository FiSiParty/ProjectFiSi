from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.compat import iteritems
import struct
import paho.mqtt.client as mqtt 
import time
import configparser
import os

def main():
    path = 'config.ini'
    section = get_section(path) #Array
    ad1 = get_setting(path, section[0], "register" )
    ans = int(ad1)
    a = connect(ans)
    config = configparser.ConfigParser()
    config['The result'] = {"Answer": a}
    with open('result.ini','w') as configfile:
        config.write(configfile)
    print("a = ", a)
    
    #function = get_setting(path, section[0], "function" )
    #print(function)
    #datatype = get_setting(path, section[0], "data type" )
    #print(datatype)
    

    
   
def connect(ad1):
    client = ModbusSerialClient(
        method='rtu',
        port='COM4',
        baudrate=9600,
        timeout=3,
        parity='N',
        stopbits=1,
        bytesize=8
    )
      
    if client.connect():
        #ad1=int(input("address1: ")) # Address input normal
        register = int(ad1)
        try:
            result1 = client.read_input_registers(address=register-1,count=1,unit=1)  #Uint32/1
            result2 = client.read_input_registers(address=register,count=1,unit=1)   #Uint32/2
            r = result2.registers + result1.registers #[Uint32/2, Uint32/1]
        except AttributeError:
            connect(ad1)
       
        b=struct.pack('HH',r[0],r[1]) 
        ans=struct.unpack('f',b)[0]
        ans = '%.2f'%ans

        allans = ans
        print('Ans: ',allans)
        client.close()
        return allans
    
    else:
        print('Cannot connect to the Modbus Server/Slave')
        

def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, sett):
   
    config = get_config(path)
    value = config.get(section, sett)
    msg = "{section} {sett} = {value}".format(
        section=section, sett=sett, value=value)
    return value

def get_section(path):
    config = get_config(path)
    sect = config.sections()
    return sect

main()
    

#!/usr/bin/python3
import sys
import serial
import struct
import time
from cobs import cobs # smart binary serial encoding and decoding

ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=3)

zeroByte = b'\x00' # COBS 1-byte delimiter is hex zero as a (binary) bytes character
cnt=0
errCnt=0
N_FLOATS=3
expectedBytes = 4*N_FLOATS # it's useful to to know what's being sent from Arduino
tNow=time.perf_counter()

while True:
    try:
        # COBS ensures the zero-byte is *only* used as the packet-end delimiter
        str = ser.read_until( zeroByte ) # read until the COBS packet ending delimiter is found
        n=len(str)
        print( "\nn={0}, str={1}".format(n,str) )
        if n>0:
            tNow=time.perf_counter()
            decodeStr = str[0:(n-1)] # take everything except the trailing zero byte, b'\x00'
            res = cobs.decode( decodeStr ) # recover binary data encoded on Arduino
            n_binary = len(res)
            
            if (n_binary==expectedBytes):
                cnt+=1
                tLast=tNow
                tNow=time.perf_counter()
                eTime=tNow-tLast
                                
                # python data types: https://docs.python.org/3/library/struct.html#format-characters
                num = struct.unpack('fff',res)
                print( "cnt={0}, errCnt={1}, eTime={2:0.5f}, n_binary={3}, num={4}".format(cnt,errCnt,eTime,n_binary,num) )
            else:
                errCnt+=1
                
    except KeyboardInterrupt as err:
        print("caught keyboard ctrl-c:".format(err))
        print("exiting.")
        exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])

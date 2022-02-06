import time
import sys
from pySerialTransfer import pySerialTransfer as txfer

list_ = [2, 4]
received_list = False
list_size = 0
rec_list_ = list()

str_ = '\x01he\x00llo\xf1 - is it \x7f you I\'m looking for?'
received_string = False
str_size = 0
rec_str_ = ''

def echo_callback():
    '''
    Callback function that will automatically be called by link.tick() whenever
    a packet with ID of 0 is successfully parsed.
    '''
    
    global received_string
    global rec_str_
    received_string = True
    ###################################################################
    # Parse response string
    ###################################################################
    print ('echo_callback')
    rec_str_   = link.rx_obj(obj_type=type(str_),
        obj_byte_size=40) #str_size)
    print("echo_callback got a message of length {}".format(len(rec_str_)))
    
def list_callback():
    global received_list
    global rec_list_
    print ('list_callback')
    received_list = True
    ###################################################################
    # Parse response list
    ###################################################################
    rec_list_  = link.rx_obj(obj_type=type(list_),
                                obj_byte_size=list_size,
                                list_format='i')
    print("list_callback got a message of length {}".format(len(rec_list_)))
    
'''
list of callback functions to be called during tick. The index of the function
reference within this list must correspond to the packet ID. For instance, if
you want to call the function hi() when you parse a packet with an ID of 0, you
would write the callback list with "hi" being in the 0th place of the list:
'''
callback_list = [ echo_callback, list_callback ]

if __name__ == '__main__':
    print('loopback_callback.py')
    try:
        global link
        link = txfer.SerialTransfer('/dev/ttyAMA1')
        link.set_callbacks(callback_list)
        link.open()
        time.sleep(2) # allow some time for the Arduino to completely reset
        rxMsgCnt = 0;
        
        while True:
            ###################################################################
            # Send a string
            ###################################################################
            str_size = link.tx_obj(str_)
            link.send(str_size, 0)
            print('Sent string data size {}, contents {}'.format(str_size, str_))

            ###################################################################
            # Send a list
            ###################################################################
            list_size = link.tx_obj(list_)
            link.send(list_size, 1)
            print('Sent list data size {}'.format(list_size))

            ###################################################################
            # Wait for a response and report any errors while receiving packets
            ###################################################################
            while True:
                link.tick()
                if received_string == True:
                    print("string callback received: {}".format(rec_str_))
                    received_string = False
                    rxMsgCnt += 1
                    if (rec_str_ != str_):
                        print('received & send strings mismatched')
                elif received_list == True:
                    print("list callback ran")
                    received_list = False
                    rxMsgCnt += 1
                    if (rec_list_ != list_):
                        print('received & send strings mismatched')
                
                if rxMsgCnt == 2:
                    rxMsgCnt = 0
                    break

                time.sleep(0.1)

            if link.status < 0:
                if link.status == txfer.CRC_ERROR:
                    print('ERROR: CRC_ERROR')
                elif link.status == txfer.PAYLOAD_ERROR:
                    print('ERROR: PAYLOAD_ERROR')
                elif link.status == txfer.STOP_BYTE_ERROR:
                    print('ERROR: STOP_BYTE_ERROR')
                else:
                    print('ERROR: {}'.format(link.status))

            if str_ != rec_str_:
                print("received string does not match sent string")
            if len(rec_list_) != len(list_):
                print("Incorrect length in received list, expected {}, received {}".format(len(list_), len(rec_list_)))
            for i in range(len(list_)):
                if list_[i] != rec_list_[i]:
                    print('Mismatched list receive data: expected {}, received {}'.format(list_[i], rec_list_[i]))

            time.sleep(0.5)
    
    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass
    
    except:
        import traceback
        traceback.print_exc()
        
        try:
            link.close()
        except:
            pass


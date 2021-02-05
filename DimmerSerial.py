import serial
import time;

class Dimmer_Serial:

    def __init__(self, port, id_dimmer):
        self.id = id_dimmer
        self.port = port

    def __del__(self):
        self.serial.close()

    def set(self, value):
        with serial.Serial( self.port, 115200 ) as ser:
            ser.write("{}:{}#".format( self.id, value ).encode("ascii"))
            ser.flush()



if __name__ == '__main__':

    try:
        print("Piou piou")

        with serial.Serial("/dev/ttyUSB0", 115200) as ser:
            ser.write( b"A:0#" )
            ser.flush()

        #ser = serial.Serial( "/dev/ttyUSB0", 115200 ) 
        ##time.sleep(1)
        ##ser.setDTR(0)
        ##time.sleep(1)
        #print(ser.isOpen())
        #
        #ser.write("A:50#".encode("ascii"))
        #ser.write("B:25#".encode("ascii"))
        #ser.flush()

        #ser.close()
    except:
        print("Error occured during serial communication")
        ser.close()
        raise

import serial, sys, glob
import inquirer
from utils.Logger import Logger

class SerialPort:

    def __init__(self) -> None:
        self.ser = None

    def search(self):

        if sys.platform.startswith('win'): # Windows
            return ['COM{0:1.0f}'.format(ii) for ii in range(1,256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            return glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'): # MAC
            return glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Machine Not pyserial Compatible')

    def readLine(self):
        # read Arduino serial data
        ser_bytes = self.ser.readline()
        # decode data to utf-8
        decoded_bytes = ser_bytes.decode('utf-8')
        # Remove all break lines characters
        return (decoded_bytes.replace('\r','')).replace('\n','')

    def close(self):

        if self.ser is not None:
            self.ser.close()

        self.ser = None

        Logger.info("Connection Closed")

    def connect(self, baudrate=9600):

        ports = self.search()

        questions = [
            inquirer.List('size',
                message="Which port do you want to connect to?",
                choices=ports,
            )
        ]

        answers = inquirer.prompt(questions)

        port = answers["size"]

        Logger.info("Connecting")

        try:
            # match baud on Arduino
            self.ser = serial.Serial(port, baudrate=baudrate)
            self.ser.flush() # clear the port

            Logger.info("Connected")
        except serial.SerialException:
            raise EnvironmentError('Not possible to connect. Maybe the port is been used')

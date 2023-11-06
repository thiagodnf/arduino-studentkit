import serial, sys, glob
import inquirer
import logging

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

    def close(self):

        if self.ser is not None:
            self.ser.close()

        self.ser = None

        logging.info("Connection Closed")

    def connect(self, baudrate=9600):

        logging.info("Connecting")

        ports = self.search()

        questions = [
            inquirer.List('size',
                message="Which port do you want to connect to?",
                choices=ports,
            )
        ]

        answers = inquirer.prompt(questions)

        port = answers["size"]

        try:
            # match baud on Arduino
            self.ser = serial.Serial(port, baudrate=baudrate)
            self.ser.flush() # clear the port
            print(self.ser.name)
            logging.info("Connected")
        except:
            raise EnvironmentError('Not possible to connect')

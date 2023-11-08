import threading

from SerialPort import SerialPort
from Radar import Radar
from utils.Logger import Logger

serialPort = None
radar = None

def collectData(name):

    if serialPort is None:
        return

    while True:
        line = serialPort.readLine()
        parts = list(map(int, line.split(",")))
        radar.plot(parts[0], parts[1])

if __name__ == "__main__":

    Logger.init()

    serialPort = SerialPort()
    serialPort.connect()

    x = threading.Thread(target=collectData, args=(1,))
    x.start()

    radar = Radar()
    radar.show()

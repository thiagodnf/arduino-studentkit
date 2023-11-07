
from SerialPort import SerialPort
from Radar import Radar

def callback(args):
    print(args)

if __name__ == "__main__":

    radar = Radar()

    radar.on("needleMoved", callback)

    radar.show()

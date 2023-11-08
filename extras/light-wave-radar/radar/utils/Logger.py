import logging

class Logger:

    @staticmethod
    def init():
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S", encoding='utf-8')

    @staticmethod
    def info(text):
        logging.info(text)

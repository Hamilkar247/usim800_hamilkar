# from ATRequests import requests
from usim800_hamilkar.Sms import sms
from usim800_hamilkar.Communicate import  communicate
from usim800_hamilkar.Request import request
from usim800_hamilkar.Info import info
import serial

class sim800(communicate):
    TIMMEOUT = 1

    def __init__(self, baudrate, path):
        self.port = serial.Serial(path, baudrate, timeout=sim800.TIMMEOUT)
        super().__init__(self.port)
        self.requests = request(self.port)
        self.info = info(self.port)
        self.sms = sms(self.port)


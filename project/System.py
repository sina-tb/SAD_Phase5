from Server import Server
from WebApp import TkinterBaseInterface

class System:
    def __init__(self):
        self._server = Server()
        self._interface = TkinterBaseInterface()

    def run(self):
        print('==>> in System::run')
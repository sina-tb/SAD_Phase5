from Back_end.Server import Server
from WebApps.TkinterBaseInterface import TkinterBaseInterface
import WebApps.manual as manual

class System:
    def __init__(self):
        self._server = Server()
        self._interface = TkinterBaseInterface()
        self._status = manual.PageStatus.HOME_PAGE

    def run(self):
        self._interface.show_page(self._status)
        command = self._interface.get_command()
        print(command._header)
        print(command._body)

    def logout(self):
        return

    def request_new_package(self):
        pass

    def select_package(self):
        pass

    def show_last_status_of_requests(self):
        pass

    def show_profile(self):
        pass

    def show_message(self):
        pass

    def fill_prerequisites(self):
        pass
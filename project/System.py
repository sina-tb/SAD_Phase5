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

    def logout(self, command):
        self._status = manual.PageStatus.CLOSE_PROGRAM
        self._interface.show_page(self._status)
        return

    def request_new_package(self, command):
        self._status = manual.PageStatus.REQUEST_NEW_PACKGE
        self._interface.show_page(self._status)

    def fill_prerequisites(self, command):
        package_id = command._body['package_id']
        self._status = manual.PageStatus.FILL_PREREQUISITES
        self._interface.show_page(self._status)

    def show_message(self, command):
        prerequisities = command._body['prerequisities']
        self._status = manual.PageStatus.SUCCESSFULL_ADD_REQUEST_MESSAGE
        self._interface.show_page(self._status)

    def return_to_home(self, command):
        self._status = manual.PageStatus.HOME_PAGE
        self._interface.show_page(self._status)

    def return_to_select_package(self, command):
        self._status = manual.PageStatus.REQUEST_NEW_PACKGE
        self._interface.show_page(self._status)

    def show_last_status_of_requests(self, command):
        pass

    def show_profile(self, command):
        pass
from Back_end.Server import Server
from WebApps.TkinterBaseInterface import TkinterBaseInterface
import WebApps.manual as manual

class User:
    def __init__(self, name):
        self._name = name

class System:
    def __init__(self):
        self._server = Server()
        self._interface = TkinterBaseInterface(self)
        self._user = User('Ghasemi')

    def start(self):
        self.return_to_home()
        self._interface.root.mainloop()

    def run_command(self, command):
        print(command._header)
        print(command._body)
        if command._header == 'logout':
            self.logout()
        elif command._header == 'request_new_package':
            self.request_new_package()
        elif command._header == 'fill_prerequisites':
            self.fill_prerequisites(command)
        elif command._header == 'show_message':
            self.show_message(command)
        elif command._header == 'return_to_home':
            self.return_to_home()
        elif command._header == 'return_to_select_package':
            self.return_to_select_package()
        elif command._header == 'show_last_status_of_requests':
            self.show_last_status_of_requests()
        elif command._header == 'show_profile':
            self.show_profile()
        self._interface.root.mainloop()

    def logout(self):
        self._status = manual.PageStatus.CLOSE_PROGRAM
        self._interface.root.destroy()
        return

    def request_new_package(self):
        self._status = manual.PageStatus.REQUEST_NEW_PACKGE
        list_of_packages = self._server.get_packages()
        self._interface.package_page_handler(list_of_packages)

    def fill_prerequisites(self, command):
        package_id = command._body['package_id']
        prerequisities = self._server.get_prerequisities(package_id)
        self._status = manual.PageStatus.FILL_PREREQUISITES
        self._interface.prerequisites_page_handler(prerequisities)

    def show_message(self, command):
        # prerequisities = command._body['prerequisities']
        # package_id = command._body['package_id']
        supporter = self._server.finalize_request_and_get_package(command._body)
        self._status = manual.PageStatus.SUCCESSFULL_ADD_REQUEST_MESSAGE
        message = 'username : ' + self._user._name + '\n'
        message += 'supporter : ' + supporter + '\n'
        for key in command._body:
            message += key + ' : ' + str(command._body[key]) + '\n'
        self._interface.successful_message_page(message)

    def return_to_home(self):
        self._status = manual.PageStatus.HOME_PAGE
        self._interface.home_page_handler()

    def return_to_select_package(self):
        self._status = manual.PageStatus.REQUEST_NEW_PACKGE
        self._interface.show_page(self._status)

    def show_last_status_of_requests(self):
        self._status = manual.PageStatus.HOME_PAGE
        self._interface.show_page(self._status)
        return

    def show_profile(self):
        self._status = manual.PageStatus.HOME_PAGE
        self._interface.show_page(self._status)
        return
import manual

class Command:
    def __init__(self, header, body):
        self._header = header # str
        self._body = body # dict of dicts

class TkinterBaseInterface:
    def __init__(self):
        print('==>> in init::TkinterBaseInterface')
    
    def show_page(self, status):
        # status is page you show
        pass

    def get_command(self):
        command1 = Command(header='', # command you give to us like system class functions except run and __init__
                           body={'options':{}}) # options of command
        
        return command1
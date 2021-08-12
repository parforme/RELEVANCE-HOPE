import threading

# Base class for modules
class Module(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def initModule(self):
        self.moduleName = 'base'

    def run(self):
        print("Base class run method, please override it.")


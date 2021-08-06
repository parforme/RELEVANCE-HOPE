from hsys import module

class dummyModule(module.Module):
    def __init__(self):
        super(dummyModule, self).__init__()
        print("Constructor of dummy module called.")
        
    def initModule(self):
        print("Initializing dummy module.")
        # run the thread of this module
        self.start()
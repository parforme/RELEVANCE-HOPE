# please define the import of each module and initialize it properly
import json
import importlib
import modules.dummyModule as dummyModule
import modules.dummyModuleRecv as dummyModuleRecv

moduleInstances = []

# instantiate and add your module here
def loadModules():
    moduleInstances.append(dummyModule.dummyModule())
    moduleInstances.append(dummyModuleRecv.dummyModuleRecv())

def initModules():
    for mod in moduleInstances:
        mod.initModule()

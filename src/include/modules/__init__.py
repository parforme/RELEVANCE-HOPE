# please define the import of each module and initialize it properly
import json
import importlib
import modules.dummyModule as dummyModule
import modules.dummyModuleRecv as dummyModuleRecv
import modules.dummyModuleFER as dummyModuleFER
import modules.ferPrediction as ferPrediction

moduleInstances = []

# instantiate and add your module here
def loadModules():
    moduleInstances.append(dummyModule.dummyModule())
    moduleInstances.append(dummyModuleRecv.dummyModuleRecv())
    #moduleInstances.append(dummyModuleFER.dummyModuleFER())  <-- TODO: refactor to sys tests
    moduleInstances.append(ferPrediction.ferPrediction())

def initModules(configFilesPath):
    for mod in moduleInstances:
        mod.initModule(configFilesPath)

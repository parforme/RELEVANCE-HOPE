# please define the import of each module and initialize it properly
import json
import importlib
import modules.dummyModule as dummyModule

moduleInstances = []

def loadModules():
    moduleInstances.append(dummyModule.dummyModule())

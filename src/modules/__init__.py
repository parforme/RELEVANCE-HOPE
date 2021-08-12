# please define the import of each module and initialize it properly
import json
import importlib

modList = []
moduleInstances = []

def loadModules():
    with open("modules/mod.json") as jsonfile:
        parsedModList = json.load(jsonfile)
        jsonfile.close()
    for mod in parsedModList['modules']:
        print(f"Loading module: {mod['name']}")
        modList.append(getattr(importlib.import_module('modules.' + mod['name'] + '.' + mod['className']), mod['className']))

def initModules():
    for mod in modList:
        class_ = mod
        moduleInstances.append(class_())  
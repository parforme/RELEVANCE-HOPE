from hsys import module
import sys
import hsys

# importing the modules will automatically load the modules BUT not instantiate them
import modules

def main(argv):
    modules.loadModules()
    modules.initModules()


if __name__ == "__main__":
    main(sys.argv)
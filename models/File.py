import configparser, os


class File:
    config = configparser.ConfigParser()
    ROOT_DIR = (os.path.dirname(os.path.abspath(__file__)))[0:-7]

    def __init__(self, path=ROOT_DIR):
        self.path = path

    def getProp(self, property):
        f = open(str(self.path) + "/config.conf", "r+")

        for line in f:
            if line.startswith(property):
                f.close()
                return line[len(property) + 1:]
        f.close()
        return None

    def printFile(self):
        f = open(str(self.path) + "/config.conf", "r+")

        for line in f:
            if not (line.startswith('#') or line.startswith(' ')):
                print(line, end="")
        f.close()

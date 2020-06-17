import configparser
import os


class FileInfos:
    config = configparser.ConfigParser()
    ROOT_DIR = (os.path.dirname(os.path.abspath(__file__)))[0:-7]

    def __init__(self, path=ROOT_DIR):
        self.path = path

        self.width = self.get_property("width")
        self.width = self.control_var(self.width, 400, 1000, 800)

        self.height = self.get_property("height")
        self.height = self.control_var(self.height, 400, 1000, 600)

        self.cellSize = self.get_property("cellSize")
        self.cellSize = self.control_var(self.cellSize, 5, 50, 10)

        self.numberOfCellGenerate = self.get_property("numberOfCellGenerate")
        self.numberOfCellGenerate = self.control_var(self.numberOfCellGenerate, 50, 2000, 750)

        self.speed = self.get_property("speed")
        self.speed = self.control_var(self.speed, 50, 1000, 250)

    def get_property(self, prop):
        f = open(str(self.path) + "/config.conf", "r+")

        for line in f:
            if line.startswith(prop):
                f.close()
                return int(line[len(prop) + 1:])
        f.close()
        return None

    def print_file(self):
        f = open(str(self.path) + "/config.conf", "r+")

        for line in f:
            if not (line.startswith('#') or line.startswith(' ')):
                print(line, end="")
        f.close()

    def control_var(self, var, bornInf, bornSup, defValue: int):
        if (var is not None) and (bornInf < var < bornSup):
            return var
        else:
            print("set default value " + str(defValue))
            return defValue


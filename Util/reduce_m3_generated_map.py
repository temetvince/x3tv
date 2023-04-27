import os
import shutil
import sys
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def pick_file():
    Tk().withdraw()
    return filedialog.askopenfilename()


def main():
    file_str = str(Path(pick_file()))
    tree = ET.parse(file_str)
    root = tree.getroot()

    for child in root:
        child.attrib['size'] = "50000000"

        for line in child.findall('o'):
            item = line.attrib['t']

            if item == "2" or item == "4":
                continue

            if item == "18":
                x = int(line.attrib['x'])
                y = int(line.attrib['y'])
                z = int(line.attrib['z'])

                x *= 2
                y *= 2
                z *= 2

                line.attrib['x'] = str(x)
                line.attrib['y'] = str(y)
                line.attrib['z'] = str(z)

                continue

            child.remove(line)
    
    tree.write(file_str)


if __name__ == '__main__':
    sys.exit(main())

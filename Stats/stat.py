import sys
sys.path
sys.path.append('/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/GeneralUtilities/PickleDict/')
sys.path.append('/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/')
# sys.path.append('/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/My_Data_Classes.py')

from GeneralUtilities.PickleDict.PickleDictLoader import PickleDictLoader
from PythonCode.Utilities.utilities import Utilities
from PythonCode.Utilities import My_Data_Classes


if __name__ == "__main__":
    loader = PickleDictLoader(pickle_path="/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/category_dict.pkl")
    category_dict = loader.get_loaded_dict()
    for key, value in category_dict.items():
        print(key)
        print(value)

# how to import local python file into another python file
# trying to import these files to use these classes but get this error


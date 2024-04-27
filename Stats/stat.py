import sys
# Add the parent directory to the Python path
sys.path.append('/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/')

from GeneralUtilities.PickleDict.PickleDictLoader import PickleDictLoader
from PythonCode.Utilities.My_Data_Classes import CategoryInfo
from PythonCode.Utilities.utilities import Utilities

if __name__ == "__main__":
    # Your code here

    loader = PickleDictLoader(pickle_path="/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/category_dict.pkl")
    category_dict = loader.get_loaded_dict()
    for key, value in category_dict.items():
        print(key)
        print(value)

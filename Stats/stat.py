import sys
import json
# Add the parent directory to the Python path
sys.path.append('/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/')

from GeneralUtilities.PickleDict.PickleDictLoader import PickleDictLoader
from PythonCode.Utilities.My_Data_Classes import CategoryInfo
#from PythonCode.Utilities.utilities import Utilities

if __name__ == "__main__":
    # loader = PickleDictLoader(pickle_path="/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/category_dict.pkl")
    # category_dict = loader.get_loaded_dict()
    
    with open("/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/Stats/proc_cat_data.json", "r") as cat_file:
        category_dict = json.load(cat_file)
        # print(category_dict)
    
    judes_dict = {}

    for outer_key, inner_keys in category_dict.items():
        # print(outer_key)
        for inner_key, inner_values in inner_keys.items():
            if inner_key == "titles":
                judes_dict[outer_key] = inner_values
                print(judes_dict)
    with open("judesData.json", 'w') as file:
        json.dump(judes_dict, file, indent=4)


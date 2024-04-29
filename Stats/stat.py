import sys
import json
import os
import warnings
import time
from dataclasses import dataclass, field, asdict
from typing import List
from random import randint


# Add the parent directory to the Python path
sys.path.append('/home/portal/425 Project/COSC425-DATA-FORK/')

from GeneralUtilities.PickleDict.PickleDictLoader import PickleDictLoader
from PythonCode.Utilities.My_Data_Classes import CategoryInfo
from PythonCode.Utilities.utilities import Utilities

@dataclass
class AvgCitationsData:
        titles: List[str] = field(default_factory=list)
        tc_count: int = 0

if __name__ == "__main__":
    # loader = PickleDictLoader(pickle_path="/mnt/linuxlab/home/jmaggitti1/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/category_dict.pkl")
    # category_dict = loader.get_loaded_dict()
    split_files_dir = "/home/portal/425 Project/COSC425-DATA-FORK/PythonCode/Utilities/split_files"
    
    with open("/home/portal/425 Project/COSC425-DATA-FORK/Stats/proc_cat_data.json", "r") as cat_file:
        category_dict = json.load(cat_file)
        # print(category_dict)
    
    judes_dict = {}
    avg = 0

    # count = 0
    for outer_key, inner_keys in category_dict.items():
        # if count > 0:
        #     break
        # print(outer_key)
        for inner_key, inner_values in inner_keys.items():
            if inner_key == "titles":
                judes_dict[outer_key] = AvgCitationsData()
                # print(judes_dict.items())
                # print("\n\n")
                # print("\n\n")
                for title in inner_values:
                    judes_dict[outer_key].titles.append(title)
                    judes_dict[outer_key].tc_count = randint(50, 100)

        # count += 1
    # print(judes_dict)
    for category_Name, value in judes_dict.items():
 
        # print(value.tc_count)
        # print("\n")
        print(len(value.titles))
        print(value.titles)
        print(value.tc_count)
        avg = (value.tc_count / len(value.titles))
        print(f"Avergae Citations for {category_Name} = {avg}\n")

    request = ["title"]

    utils = Utilities()

    for filename in os.listdir(split_files_dir):
        file_path = os.path.join(split_files_dir, filename)
        with open(file_path, "r") as current_file:
            entry_text = current_file.read()
            for key, value in judes_dict.items():
                for title in value.titles:
                    if title in entry_text:
                        value.tc_count = randint(50, 100)
                        print(f'{entry_text}\n')
                        print(title)
                        attr_to_get = ['totalCitations']
                        attr_rec = utils.get_attributes(entry_text=entry_text, attributes=attr_to_get)
                        print(attr_rec)
                        print(f'Paper: {title}')
                        for key, val in attr_rec.items():
                            authors = val[1] if val[0] else None
                        if authors:
                            print(authors)




    # with open("judesData.json", 'w') as file:
    #     json.dump(judes_dict, file, indent=4)


import os
import sys
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
from removeOneFile import removeOne, checkFileTimeAfter

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def removeList(l_filepath):
    l_success = []
    l_fail = []
    for filepath in l_filepath:
        if removeOne(filepath):
            l_success.append(filepath)
        else:
            l_fail.append(filepath)

    return(l_success, l_fail)

def removeListAfter(l_filepath, s_datetime):
    l_success = []
    l_fail = []
    for filepath in l_filepath:
        if checkFileTimeAfter(filepath, s_datetime):
            if removeOne(filepath):
                l_success.append(filepath)
            else:
                l_fail.append(filepath)
        else:
            l_fail.append(filepath)

    return(l_success, l_fail)


def main():
    l_filepath = ["test1", "test2"]
    # (l_success, l_fail) = removeList(l_filepath)
    s_datetime = "2024-03-23 12:00:00"
    (l_success, l_fail) = removeListAfter(l_filepath, s_datetime)

    
if __name__ == "__main__":
    main()

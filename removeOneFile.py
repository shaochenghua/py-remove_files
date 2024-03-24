import os
import sys
from datetime import datetime
from os.path import getctime, getmtime
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def removeOne(filepath):
    if not os.path.isfile(filepath):
        logger.warning("cannot find file %s", filepath)
        return False
    
    try:
        os.remove(filepath)
        logger.info("removed file %s", filepath)
        return True
    except Exception as e:
        logger.error("failed to remove file at %s with error %s", filepath, e)
        return False

def checkFileTimeAfter(filepath, s_datetime):
    # time must be in "2023-09-15 01:01:01" format
    if not os.path.isfile(filepath):
        logger.warning("cannot find file %s", filepath)
        return False

    try:
        datetime_ref = datetime.strptime(s_datetime, "%Y-%m-%d %H:%M:%S")
        unixtime_file = getmtime(filepath) ## get file creation time in unix time format
        datetime_file = datetime.fromtimestamp(unixtime_file) ## convert unix time format to Python datetime format
        logger.info("creation time for %s is %s", filepath, str(datetime_file))
    except Exception as e:
        logger.error("failed to convert threshhold time or file creation time with error %s", e)
        return False
        
    if datetime_file >= datetime_ref:
        return True
    else:
        return False

    
def main():
    filepath = "test"
    if checkFileTimeAfter(filepath, "2023-03-23 09:00:00"):
        print(removeOne(filepath))


if __name__ == "__main__":
    main()
    

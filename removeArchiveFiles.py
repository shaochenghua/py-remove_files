import os
import sys
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
from removeListFiles import removeList, removeListAfter
from wwpdb.io.locator.PathInfo import PathInfo

def getFilePath(dep_id, site_id):
    # choose site_id from WWPDB_DEPLOY_PRODUCTION_RU, WWPDB_DEPLOY_LEGACY_RU, WWPDB_DEPLOY_DEPGRP1_RU, WWPDB_DEPLOY_TEST_RU
    try:
        if site_id:
            onedep_path = PathInfo(siteId=site_id)  #specify site id
        else:
            onedep_path = PathInfo()  #use the server site id
    except Exception as e:
        logger.warning("OneDep module PathInfo doesn't work with error %s", e)
        return None
    try:
        filepath = onedep_path.getModelPdbxFilePath(dep_id)
    except Exception as e:
        logger.error("cannot find filepath for %s" % dep_id)
        return None
    
    if not os.path.isfile(filepath):
        logger.error("cannot find filepath for %s" % dep_id)
        return None

    return filepath

def report(filepath, l_):
    with open(filepath, 'w') as file:
        for each in l_:
            file.write(each)
            file.write('\n')
            
def getIdList(filepath):
    with open(filepath) as file:
        return file.read().splitlines()
            
def main():
    l_dep_id = getIdList("id.list")
    logger.info("read id list %s", l_dep_id)
    l_filepath = []
    site_id = None
    for dep_id in l_dep_id:
        filepath = getFilePath(dep_id, site_id)
        if filepath:
            l_filepath.append(filepath)

    s_datetime = "2024-03-23 10:00:00"
    (l_success, l_fail) = removeListAfter(l_filepath, s_datetime)
    report("success.list", l_success)
    report("fail.list", l_fail)


if __name__ == "__main__":
    main()
    
        
                          

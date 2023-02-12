import os
from pathlib import Path

local_template_folder = '' # str(Path(__file__).parent.absolute()) + str('/Templates')
local_imgs_folder = '' # str(Path(__file__).parent.absolute()) + str('/imgs')

def createFolderDir():  
    try:
        print('strat folder verification...')
        if not os.path.isdir(str(Path(__file__).parent.absolute()) + str('/Templates')):
            print('DIR Templates DOES NOT EXISTS.')
            os.makedirs(str(Path(__file__).parent.absolute()) + str('/Templates'))
            print('DIR Templates SUCCESSFULLY CREATED.')
        if not os.path.isdir(str(Path(__file__).parent.absolute()) + str('/imgs')):
            print('DIR imgs DOES NOT EXISTS.')
            os.makedirs(str(Path(__file__).parent.absolute()) + str('/imgs'))
            print('DIR imgs SUCCESSFULLY CREATED.')       

        
    except Exception as err:
        print('error: ', err)
        pass
        
# createFolderDir()
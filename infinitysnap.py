##Author: Likhith Garapati

import random
import os
import time

def infinitysnap(path):
    print('Script written by Likhith Garapati')
    all_files=[]

    for root,dirs,files in os.walk(path):
        for filename in files:
            file=os.path.join(root,filename)
            abs_path=os.path.abspath(file)
            all_files.append(abs_path)

    random.shuffle(all_files)

    for i in range(len(all_files)//2):
        os.remove(all_files[i])
    time.sleep(5)
    print('Infinity Snap Completed......')

path="E:\\snaptest"##enter your drive or folder path
infinitysnap(path)

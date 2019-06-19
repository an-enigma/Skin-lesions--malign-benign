import numpy as np
import json
import shutil
import os,sys
r="ISIC_0000000"
def inc(p):
    o=str(p)
    qq=o.split("_")
    p=str(int(qq[1])+1)
    while(len(p)<7):
        p="0"+p
    ww=str(qq[0])+ "_" + p
    return ww
for i in range(78):
    r=inc(r)
    #print(r)
    with open( r + ".json") as json_file:
        data = json.load(json_file)
        if(data["meta"]["clinical"]["benign_malignant"]=="benign"):
            na=r+".jpg"
            shutil.copy(na, 'benign')
            print("0")
        else:
            na=r+".jpg"
            shutil.copy(na, 'malign')
            print("1")
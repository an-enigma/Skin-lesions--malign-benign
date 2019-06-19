import h5py
import sys,os
import keras
import cv2
import imageio
import numpy as np
from keras.models import load_model
from PIL import Image
#import visvis as vv

img=sys.argv[1]
roi=imageio.imread(str(img))
tup=(127,127)
imgr = cv2.resize(roi, tup, interpolation = cv2.INTER_AREA)
pred=[]
pred.append(imgr)
pre=np.asarray(pred)
model=load_model('lesions.h5')
p=model.predict(pre)
print(p)
janstr=""
if(p[0][0]<0.4):
    im =Image.open(img)
    im.show()
    print("it's Benign skin lesion")
    janstr="it's Benign skin lesion"
elif(p[0][0]>0.6):
    im =Image.open(img)
    im.show()
    print("it's a Malign lesion")
    janstr="it's a Malign lesion"
print(janstr)

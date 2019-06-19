# Skin-lesions-- classified as malign or benign
This is a simple neural network which classifies skin lesions as malign or benign with the help of data set containing images of skin lesions, using tensorflow. 

# Principle 
This neural network classifies the image of a skin lesion as benign or malign using a labeled dataset and is an example of supervised learning. The model is trained using Keras, a high level Python neural networks library running on top of Tensorflow. 

# Dataset
The dataset consists of around 80 images along with there JSON files in the Dataset folder. The JSON files contains the description of the respective image and we parse it using the dis.py script in the Processed data folder. According to the script the images are separated into two folders malign and benign. After that they are copied to the files classif1 and classif2. 

# Procedure
After processing the data we build the training model using keras and tensorflow in the script neuralclsf.py and the remaining libraries for that can be installed using the command pip install requirements.txt

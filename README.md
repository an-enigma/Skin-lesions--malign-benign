# Skin-lesions-- classified as malign or benign
This is a simple neural network which classifies skin lesions as malign or benign with the help of data set containing images of skin lesions, using tensorflow. 

# Principle 
This neural network classifies the image of a skin lesion as benign or malign using a labeled dataset and is an example of supervised learning. The model is trained using Keras, a high level Python neural networks library running on top of Tensorflow. 

# Dataset
The dataset consists of around 80 images along with there JSON files in the Dataset folder. The JSON files contains the description of the respective image and I parsed it using the dis.py script in the Processed data folder. According to the script the images are separated into two folders malign and benign. After that they are copied to the files classif1 and classif2. 

# Procedure
After processing the data I built the training model using keras and tensorflow in the script neuralclsf.py and the remaining libraries for that can be installed using the command (requirements.txt is present above)

pip install requirements.txt

While going through many methods which could be used to solve this problem like SVM, Naive Bayes or logistic regression I landed at neural networks because they give best results if we have many features. I have used balanced Architecture for the neural network using Keras library of Tensorflow. For optimisers choice I used Adam as they gave the best results in my testing. Hence I built the training model which is the script neuralclsf.py .
After that to test the model I made the modelf.py script which when run in the following manner will classify if the skin lesion is malign or benign from the image passed as an argument. Run the test model as follows

python3 modelf.py ISCI_0000076.jpg                              



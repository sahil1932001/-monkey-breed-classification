# monkey-breed-classification

## problem statement : I have to build a web application that can easily classify the monkeys breeds when user input the monkey images

There are about 200 breeds, or types, of monkey are there. Scientists divide them into two groups, Old World monkeys and New World monkeys. In this project I collected the images of 10 different types of breeds of monkeys.

I divided the images of monkeys into training set and validation set. training data contains images of 10 different breeds of monkey for training purpose. 
and validation set also contains the images of 10 different breeds of monkeys for testing purpose.
I have one txt file that contains the labels, names and count of training and validation data of 10 different breeds.

![Screenshot 2022-12-15 133937](https://user-images.githubusercontent.com/95639758/207806554-9642927b-8a59-4664-8bf5-12bf29d8468b.png)

From above figure we can conclude that all the classes are almost equally distributed, this is good news as the model will not be biased towards any class and learning will be pure.

I have done all the scaling and preprocessing that are required.and our images size is.

After that I use CNN(convolutional neural network) model for training the data. I used 2 convolutional layer and 2 pooling layers and fully connected layer.
I got an accuracy of 80% which is good.
after that i loaded the model and made web application using Flask.
In below image you can se how web application looks like.




















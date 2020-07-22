# Capstone Project on Dog Breed Identifier

### Table of Content
- [Summary](#summary)
- [Metrics](#metrics)
- [Setup the environment](#setup)
- [Running the application](#run)
- [Use the application](#usage)
- [Application Screenshot](#screen)
- [Reflection](#reflect)
- [Improvement](#improve)

## Summary <a name="summary"></a>
In the project, I built and trained a neural network model with CNN (Convolutional Neural Networks) transfer learning, using 8351 dog images of 133 breeds. CNN is a type of deep neural networks, which is commonly used to analyze image data. Typically, a CNN architecture consists of convolutional layers, activation function, pooling layers, fully connected layers and normalization layers. Transfer learning is a technique that allows a model developed for a task to be reused as the starting point for another task. The trained model can be used by a web or mobile application to process real-world, user-supplied images. Given an image of a dog, the algorithm will predict the breed of the dog. If an image of a human is supplied, the code will identify the most resembling dog breed.

This project has two parts which are intended to be run on different environment.

## 1. Jupyter Notebook
The file `dog_app.ipynb` contains a detailed work done on the project. <br>
>_Note: The Project Definition, Analysis, and Conclusion sections are added in the notebook itself._

Running the notebook produces the file `weights.best.Inception.hdf5` (among other files) under the folder **saved_models**, which is a required input file for the web application. A version of this file from prior execution is already been included in the repository.

## Metrics <a name="metrics"></a>
The main metric of interested is the prediction accuracy, expressed as a percentage.

During training, loss is used, although it's a little too abstract for human consumption. The number of epochs and the training time per epoch are also output, which are quite important when running the notebook. All of these metrics are of little interest to the end user, who just wants to see the results.

Another metric of concern is the amount of data that is moved around in each epoch. Even though the notebook runs without error on my local PC, in practice it's too slow to be usable. This is of little interest to the end user, but computational expense places limits on what can be done.

## 2. Web application
The web application uses prebuilt models for making predictions. This is a lightweight operation and intended to be run local PC.

## Setup the environment <a name="setup"></a>

First we'll need to set up the Python environment. Open a conda terminal, and copy/paste in this one-liner:

```
$ conda create -n dog python=3.6 tensorflow keras flask opencv pillow numpy
```

This may take awhile.  When it completes, activate the new environment:

```
$ conda activate dog
```

## Running the Application <a name="run"></a>

It's assumed that the Git repository has already been cloned.  If not, do so now.

```
$ git clone https://github.com/Brijesh-Chandra/Dog-Breed-Identifier.git
```

The app also requires the [Inception bottleneck features](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogInceptionV3Data.npz), which is quite a large file.  Download it to the **bottleneck_features** folder.

Now we're ready to start the web server. From the project's root directory run the following commands:

```
$ cd Dog-Breed-Identifier/web_app
$ python run.py
```

The server will initialize, and then provide a link, similar to this:

```
Using TensorFlow backend.
 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:3001/ (Press CTRL+C to quit)
 ```

Then open a browser and copy/paste the link onto the address bar.

>_Note: The application will run with newer versions of python and tensorflow, but there will be a lot of runtime warnings. And loading of the application may take some time._

## How to use? <a name="usage"></a>

To use the website, follow the instructions on the landing page.

## Application Screenshot <a name="screen"></a>
<img src='result_screenshot.png'>

## Reflection <a name="reflect"></a>
The results using the InceptionV3 model are surprisingly good. A dog show judge working from photos alone could probably do better, but the network probably does better than the average layman. Also, easily forgotten because it's way back at the beginning, the ResNet50 got a perfect score at dog detection.

The big lesson for me in this project is that, "cheating" is OK, and cheaters actually do prosper. I created a network from scratch, toiling away for a substantial amount of time, with only modest success. Then I tried augmenting the data and got an instant performance boost. It felt like cheating. Then I abandoned that effort, and used transfer learning from someone else's pre-trained network and got really good results. That's more like stealing. It's all so sick and wrong!

With an accuracy of over 75%, there's only so much room for improvement. The next type of cheating I would like to engage in is the use of brightness/contrast normalization (which could be considered data science) and bounding boxes (calling that "data science" would be a bit of a stretch). But image processing and learning OpenCV seem like fodder for another course.



This is a really fun project, and I intend to keep working on it.

## Improvement <a name="improve"></a>
There are several improvements I would like to make:

- Reduce the number of breeds. In practical terms, quite a few of these breeds exist only in dog shows.
- Introduce an 'other' classification to contain the obscure breeds as well as mutts.
- Add the dimensions gender, height, weight, and age (and probably some others) to the training data, and also allow the user to supply them. For the training data, it could contain whichever of these is available. The occasional puppy aside, if you know the breed and the gender, with the help of a dog book you can impute the rest. When predicting, the user would likewise be able to supply whichever of these data points is known. This enhancement would require a change in network architecture.
- Preprocess the user input data, to coerce it into the assumptions listed in the Problem Statement:
  - If a dog is detected, but also 1 or more human faces are detected, exclude their bounding box from consideration.
  - If multiple dogs are detected, assume the subject is the dog with the largest bounding box.
  - Center/enlarge the subject, possibly with a small margin.
  - Note that this preprocessing does not apply to training data. It might help, or it might hurt performance. Some experimentation is called for.
- Add a lot more training data. This is a big data problem, but the supplied training data is pretty small.

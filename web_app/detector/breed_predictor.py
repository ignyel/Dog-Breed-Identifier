from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Sequential
import keras.applications.inception_v3 as inception_v3
from PIL import ImageFile
import numpy as np

from .dog_names import dog_names
from .dog_detector import initialize_dog_detector, dog_detector, path_to_tensor
from .face_detector import initialize_face_detector, face_detector

app = None


def initialize(the_app):
    global app
    app = the_app
    app.config['INCEPTION_MODEL'] = inception_v3.InceptionV3(
        weights='imagenet', include_top=False)
    app.config['INCEPTION_CLASSIFIER'] = get_inception_model()
    initialize_face_detector(app)
    initialize_dog_detector(app)


def get_inception_model():
    Inception_model = Sequential()
    Inception_model.add(GlobalAveragePooling2D(input_shape=[5, 5, 2048]))
    Inception_model.add(Dense(133, activation='softmax'))
    Inception_model.load_weights('../saved_models/weights.best.Inception.hdf5')
    return Inception_model


def extract_InceptionV3(tensor):
    model = app.config['INCEPTION_MODEL']
    return model.predict(inception_v3.preprocess_input(tensor))


def predict_breed(img_path):
    feature = extract_InceptionV3(path_to_tensor(img_path))
    model = app.config['INCEPTION_CLASSIFIER']
    pred = model.predict(feature)
    return dog_names[np.argmax(pred)]


def what_is_it(img_path):
    species = "unknown"
    breed = "unknown"
    if dog_detector(img_path):
        species = "dog"
        breed = predict_breed(img_path)
    elif face_detector(img_path):
        species = "human"
        breed = predict_breed(img_path)
    print(f"Species: {species}, Breed: {breed}")
    return (species, breed)

import cv2

app = None


def initialize_face_detector(the_app):
    global app
    app = the_app
    app.config['FACE_CASCADE'] = cv2.CascadeClassifier(
        '../haarcascades/haarcascade_frontalface_alt.xml')


def face_detector(img_path):
    global app
    face_cascade = app.config['FACE_CASCADE']
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0

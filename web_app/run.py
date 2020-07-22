import os, datetime
from werkzeug.utils import secure_filename
from flask import Flask, render_template, send_from_directory, make_response, request, redirect, url_for
from detector import initialize, what_is_it

UPLOAD_FOLDER = 'static/input'
ALLOWED_EXTENSIONS = set(['bmp', 'gif', 'jpeg', 'jpg', 'png'])

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
initialize(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    try:
        file = request.files['input-photo']
    except:
        file = None

    if file and allowed_file(file.filename):
        format = "%Y%m%dT%H%M%S"
        now = datetime.datetime.utcnow().strftime(format)
        filename = now + '_' + file.filename
        filename = secure_filename(filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        file_uploaded = True

    else:
        filepath = None
        file_uploaded = False

    return file_uploaded, filepath, filename


@app.route('/results', methods=["POST"])
def results():
    file_uploaded, filepath, filename = upload_file()

    if file_uploaded:
        species, breed = what_is_it(filepath)
        return render_template('results.html',
                               filename=filename,
                               species=species,
                               breed=breed)

@app.route('/')
def landing_page():
    return render_template('input.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    # Do not edit.
    app.run(debug=False, threaded=False)

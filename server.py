import json
from werkzeug.utils import secure_filename
import pandas as pd
import parse_util
from flask_cors import CORS
from flask import Flask, request, jsonify

ALLOWED_EXTENSIONS = set(['json', 'xls', 'xlsx'])

app = Flask(__name__)
CORS(app)


def allowed_file(filename):
    # this has changed from the original example because the original did not work for me
    return str(filename).split('.')[-1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Hello!, new domain!'


@app.route('/index', methods=['GET', 'POST'])
def index():
    return '<h1>This is index!<h1>'


@app.route('/getjson', methods=['GET', 'POST'])
def get_json():
    return jsonify(parse_util.return_json_from_db())


@app.route('/setjson', methods=['GET', 'POST'])
def set_json():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if allowed_file(filename):
            return jsonify(parse_util.update_json_in_db(file))
        return jsonify(json.dumps({'msg': 'are you trying to fuck up my server? send me only json/xls/xlsx files!'}))
    else:
        return jsonify(json.dumps({'msg': 'dude this is POST only!@'}))


@app.route('/compare', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if allowed_file(filename):
            data_xls = pd.read_excel(f)
            return data_xls.to_html()
            student_dict = parse_util.parse_xls(f)
            return student_dict
        else:
            return jsonify(json.dumps({'msg': 'False', 'error': 'this file extension is not supported'}))
    return jsonify(json.dumps({'msg': 'dude this is POST only!@'}))


if __name__ == '__main__':
    app.run()

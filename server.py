import json
from os import environ

from flask import Flask, request, jsonify

import parse_util

ALLOWED_EXTENSIONS = set(['json', 'xls','xlsx'])

app = Flask(__name__)


def allowed_file(filename):
    # this has changed from the original example because the original did not work for me
    return str(filename).split('.')[-1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Hello!'

@app.route('/compare', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        if allowed_file(filename):
            student_dict = parse_util.parse_xls(file)
            print student_dict
            return jsonify(student_dict)
        else:
            return jsonify(json.dumps({'msg': 'False', 'error': 'this file extension is not supported'}))
    return jsonify(json.dumps({'msg': 'True'}))


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
    else:
        return jsonify(json.dumps({'msg': 'False'}))



if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



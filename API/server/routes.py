from flask import Flask , request , render_template ,jsonify, url_for
from parse_util import api_handler
import os

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)


@app.route("/getdbjson",methods=['GET'])
def demo():
    json = api_handler().return_json_from_db()
    if json is None:
        dict = {'msg':'True'}
        return json.dumps({'msg':'True'})
    else:
        return jsonify(json)



@app.route("/parsexls",methods=['POST'])
def parsexls():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print '**found file', file.filename
            # for browser, add 'redirect' function on top of 'url_for'

    return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            '''


@app.route("/setjson",methods=['POST'])
def demo2():
    return 'bla'

def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='192.168.1.7',port=8674)
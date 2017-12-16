from flask import Flask, request, render_template, jsonify, url_for
import parse_util
import os

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)


@app.route("/getdbjson", methods=['GET'])
def demo():
    json = parse_util.return_json_from_db()
    if json is None:
        dict = {'msg': 'True'}
        return json.dumps({'msg': 'True'})
    else:
        return jsonify(json)


@app.route("/parsexls", methods=['POST'])
def parsexls():
    print 'ssss'
    if request.method == 'POST':
        print 'this is post'
        return 'ffs'
        file = request.files['file']
        if file and allowed_file(file.filename):
            print '**found file', file.filename
            with open('text.xlsx', 'w') as f:
                print 'file opened'
                f.write(file.read())
                # for browser, add 'redirect' function on top of 'url_for'
    elif request.method == 'GET':
        return 'this is get'
    return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
              <p><input type=file name=file>
                 <input type=submit value=Upload>
            </form>
            '''


@app.route("/setjson", methods=['POST'])
def demo2():
    return 'bla'


def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.11', port=8674)

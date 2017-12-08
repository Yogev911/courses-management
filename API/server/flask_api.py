from flask import Flask , request , render_template ,jsonify

app = Flask(__name__)


@app.route("/yogev",methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        text = 'You are using POST'
        # json_res =
        return render_template('shopping.html', output=text)
    return render_template('profile.html', output='hello')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',port=8674)
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<username>', methods=['GET'])
def login(username):
    return "hello " + username

@app.route("/multiply/<n>/<m>")
def multiply(n, m):
    return "{} * {} gives {}".format(n, m, float(n) * float(m))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151, debug=True)
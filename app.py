from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True

@app.router("/")
def hello_world():
    return "<p> Hello World!</p>"


if __name__ == "__main__":
    app.run(debug=True)

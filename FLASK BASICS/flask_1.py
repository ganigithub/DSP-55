from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is my website. My first flask appliction.<h1>"

if __name__=='__main__':
    app.run(debug=True)

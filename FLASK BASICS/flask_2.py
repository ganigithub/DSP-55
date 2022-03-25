from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is my home page.<h1>"

@app.route('/about')
def about():
    return 'This is about us page. This is a tech company.'

@app.route('/contactus')
def contactus():
    return '<h1>office no: +91 7483298374</h1>'

@app.route('/description')
def description():
    return '<h1>Hello everyone! This is our new tech company website</h1>'



if __name__=='__main__':
    app.run(debug=True)

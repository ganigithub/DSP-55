from flask import Flask, render_template
app = Flask(__name__)

content = [
{"Author": "Ganesh", "title" : "Blog 1",
"content": "Data Science", "date": "29th Jan"},
{"Author": "Ganesh", "title" : "Blog 2",
"content": "Machine Learning", "date": "30th Jan"}
]


@app.route('/')
def home():
    return render_template("home2.html", posts = content)  #we are passing content in posts

@app.route('/about')
def about():
    return "<h1>This about us page. We are a tech campany<h1>"

if __name__=='__main__':
    app.run(debug=True)

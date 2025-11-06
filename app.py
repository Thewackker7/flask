from flask import Flask,render_template,url_for
app=Flask(__name__)
posts=[{'author':'Haro Aso.',
        'title':'Alice in border land',
        'date_published':'December 10, 2020'},

        {'author':'George R. R. Martin',
        'title':'Game Of Thrones',
        'date_published':'August 1996.'}
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html',title="About")

@app.route("/bitch")
def bitch():
    return "hello bitch"

if __name__ == "__main__":
    app.run(debug=True)
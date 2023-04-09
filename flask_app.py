from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
    {
    'id':1,
    'title':'Business Analyst',
    'location':'Bengluru, India',
    'salary':'$120,000'
    },
    {
    'id':2,
    'title':'Data Analyst',
    'location':'Remote',
    'salary':'$120,000'
    },
]

@app.route("/")
def app_portfolio():
    return render_template('home.html',jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

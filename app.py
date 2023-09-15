from flask import Flask, render_template

app = Flask(__name__)

participants = [
    {
        'id': 1,
        'name': "Arnav Balpande",
        'rank': 1,
        'score': 100,
    },
    {
        'id': 2,
        'name': "Riya Kashikar",
        'rank': 2,
        'score': 10,
    },
]


@app.route('/')
def home():
  return render_template('home.html', participants=participants)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

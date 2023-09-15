from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

profileLinks = [
    "https://leetcode.com/arnavhax/", "https://leetcode.com/Anirudha_Shekdar/"
]


def makeParticipants(profileLinks):
  participants = []
  for k in profileLinks:
    response = requests.get(k)
    soup = BeautifulSoup(response.content, "html.parser")
    entity = {}

  participants = [
      {
          'username': "Arnav Balpande",
          'score': 100,
      },
      {
          'username': "Riya Kashikar",
          'score': 10,
      },
  ]

  return participants


app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html',
                         participants=makeParticipants(profileLinks))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

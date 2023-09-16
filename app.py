from flask import Flask, render_template
import requests
import json

profileLinks = [
    "arnavhax", "Anirudha_Shekdar",
    "BeNeatCo", "hazsyl1",
    "dulhaniaa", "yuvrajzanwar",
    "shrivastavapa",
    "prathameshratthe",
    "jatinbaheti",
    "Priyanshi_0912",
  "aalok2025",
  "VedantM2204",
  "krdande2",
  "Kartik_V",
  "sujalagrawal1885"
]


def makeParticipants(profileLinks):
  participants = []
  for k in profileLinks:
    entity = {}
    url="https://leetcode-stats-api.herokuapp.com/"+k
    username = ''
    score = 0
    response = requests.get(url)
    entity = {}
    easy_solved =0
    medium_solved=0
    hard_solved=0
    if response.status_code == 200:
      data = json.loads(response.text)
      easy_solved = int(data["easySolved"])
      medium_solved=int(data["mediumSolved"])
      hard_solved=int(data["hardSolved"])
    entity['score']=easy_solved+medium_solved*3+hard_solved*5
    entity['username']=k
    participants.append(entity)
      
  return participants


app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html',
                         participants=sorted(makeParticipants(profileLinks),
                                             key=lambda i: i['score'],
                                             reverse=True))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

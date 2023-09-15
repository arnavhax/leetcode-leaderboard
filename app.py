from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

profileLinks = [
    "https://leetcode.com/arnavhax/", "https://leetcode.com/Anirudha_Shekdar/",
    "https://leetcode.com/BeNeatCo/", "https://leetcode.com/hazsyl1/",
    "https://leetcode.com/dulhaniaa/", "https://leetcode.com/yuvrajzanwar/",
    "https://leetcode.com/shrivastavapa/",
    "https://leetcode.com/prathameshratthe/",
    "https://leetcode.com/jatinbaheti/",
    "https://leetcode.com/Priyanshi_0912/", "https://leetcode.com/aalok2025/"
]


def makeParticipants(profileLinks):
  participants = []
  for k in profileLinks:
    entity = {}
    username = ''
    score = 0
    response = requests.get(k)
    soup = BeautifulSoup(response.content, "html.parser")
    entity = {}
    questions = soup.findAll(
        'span',
        class_=
        'mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1'
    )
    for i in range(len(questions)):
      if (questions[i] is not None):
        if (i == 0):
          score += int(questions[i].text)
        if (i == 1):
          score += int(questions[i].text) * 3
        if (i == 2):
          score += int(questions[i].text) * 5
    entity['score'] = score
    un = soup.find(
        'div',
        class_=
        'text-label-1 dark:text-dark-label-1 break-all text-base font-semibold'
    )
    if (un is not None):
      entity['username'] = un.text
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

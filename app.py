import os
import datetime
import random
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html>'
    page += """<style>
body {
  background-image: url(https://cdn.kapwing.com/final_6185b58933771d00365cedcd_760615.gif);
  background-repeat: repeat-x;
  background-position: right;
  height: 1750;
}
</style><head><title>REFRESH PLEASE!</title></head>"""
    page += '<body><h1>Countdown</h1>'
    page += '<span title="A lot to process.. I know..">' + definetime() + " left until 2023" + "</span>"
    page += '</h1></br>'
    page += '<img src="' + imageswitch() + '"></img style="padding 40px">'
    page += "</br></br>Greetings from Dennis Oosterom && Coen Luijten</br>"
    page += '</body></html>'
    return page


def definetime():

    # days until date.
    today = datetime.date.today()
    future = datetime.date(2023,1,1)
    diff = future - today

    # hours, minutes, seconds, microseconds
    dt = datetime.datetime.now()
    minutes = dt + datetime.timedelta(days=diff.days)
    print(minutes , dt)
    return str(datetime.datetime.combine(minutes, datetime.time.min) - dt)

def imageswitch():
    awesomepictures = ["https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/404-wall.jpg", "https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/done.jpg", "https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/onedoesnotsimply.jpg", "https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/painful.jpg", "https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/onedoesnotsimply.jpg", "https://raw.githubusercontent.com/CLStrike/cicd-buzz/master/girl.jpg"]

    b = random.randint(0, 4)
    return str(awesomepictures[b])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
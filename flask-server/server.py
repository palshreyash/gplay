from flask import Flask
from autoscraper import AutoScraper
from flask import jsonify

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url="https://play.google.com/store/apps"
    wanted_list = ["Instagram","Snapchat"]
    scraper = AutoScraper()
    result = scraper.build(url,wanted_list)
    return jsonify({"appname":result})


@app.route("/show")
def show():
    return {"members":["members1","members2","members3"]}


if __name__ == "__main__":
    app.run(debug=True)
    
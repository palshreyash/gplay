from flask import Flask
from flask import jsonify
import time
from selenium import webdriver

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url="https://play.google.com/store/apps"
    driver = webdriver.Chrome("/Users/shrey/Downloads/chromedriver_mac_arm64/chromedriver")
    driver.get(url)
    time.sleep(10)
    SCROLL_PAUSE_TIME = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(SCROLL_PAUSE_TIME)
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    links_games = []
    elems = driver.find_element_by_xpath("//a[@href]")
    for elem in elems:
        if "details?id" in elem.get_attribute("href"):
            links_games.append(elem.get_attribute("href"))
    links_games = list(dict.fromkeys(links_games))
    list_all_elements = []
    for iteration in links_games:
        driver.get(iteration)
        time.sleep(2)
        name = driver.find_element_by_tag_name("h1")
        star = 0 
        try:
            star = float(driver.find_element_by_class_name("jILTFe").text)
        except:
            star = 0
        img = driver.find_element_by_xpath("//img[contains(@class,'T75of cN0oRe fFmL2e')]").get_attribute("src")
        list_elements = [name.text.encode('ascii','ignore'),img.encode('ascii','ignore'),star]
        list_all_elements.append(list_elements)
        return jsonify({"appinfo":list_all_elements})
        
    # result = scraper.build(url,wanted_list)
    # return jsonify({"appname":result})


@app.route("/show")
def show():
    return {"members":["members1","members2","members3"]}


if __name__ == "__main__":
    app.run(debug=True)
    
from bs4 import BeautifulSoup
import requests
# import sys

# Array.from(document.querySelector('div.list-wrap').querySelectorAll('a'), a => a.textContent.trim())
titles = set(open("titles.txt").read().lower().split("\n"))

# You can use this but I recommend titles file instead as this will get Romanji names, which Mangapill doesn't have for everything
# def get_user_reading():
#    username = sys.argv[1] if len(sys.argv) > 1 else "user"
#    res = requests.get(f"https://anilist.co/user/{username}/mangalist")
#    soup = BeautifulSoup(res.text, "html.parser")
#    reading = soup.find("div", class_="list-wrap")
#    return {title.text.strip() for title in reading.find_all("div", class_="title")}[1:] # Returns all but first result as that just says title


def get_mangapill_recents():
    res = requests.get("https://mangapill.com/chapters")
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find("div", class_="grid").find_all("a", class_="text-secondary")
    recents = set()
    for each in divs:
        recents.update(each.text.strip().lower().split("\n"))
    return recents


def comparison():
    intersection = titles.intersection(get_mangapill_recents())
    # intersection = get_user_reading().intersection(get_mangapill_recents())
    return str("New releases: " + ", ".join([each.title() for each in intersection])) if intersection else "No elements"


print(comparison())

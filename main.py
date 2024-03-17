from bs4 import BeautifulSoup
from requests import get
from argparse import ArgumentParser
from json import dumps, loads, JSONDecodeError
from datetime import datetime, timedelta

# Array.from(document.querySelector('div.list-wrap').querySelectorAll('a'), a => a.textContent.trim())
titles = set(open("titles.txt").read().lower().split("\n"))
current_time = datetime.now()

parser = ArgumentParser(description="Tracker for recently released manga chapters")
parser.add_argument("-u","--user", help="Specifies Anilist user", default="", type=str)
parser.add_argument("-t", "--ttl", help="Decides whether to use TTL mode or not", action='store_false')
args = parser.parse_args()

# You can use this but I recommend titles file instead as this will get Romanji names, which Mangapill doesn't have for everything
def get_user_reading():
   res = get(f"https://anilist.co/user/{args.user}/mangalist")
   soup = BeautifulSoup(res.text, "html.parser")
   reading = soup.find("div", class_="list-wrap")
   # Returns all but first result as that just says title
   return {title.text.strip() for i, title in enumerate(reading.find_all("div", class_="title")) if i != 0}


def get_mangapill_recents():
    res = get("https://mangapill.com/chapters")
    soup = BeautifulSoup(res.text, "html.parser")
    divs = soup.find("div", class_="grid").find_all("a", class_="text-secondary")
    recents = set()
    for each in divs:
        recents.update(each.text.strip().lower().split("\n"))
    return recents


def update_recently_found(recently_found: list, intersection):
    recently_found += [[title, current_time.strftime('%Y-%m-%d %H:%M:%S')] for title in intersection]

    with open('recents.json','w') as file:
        file.write(dumps(recently_found))


def get_recently_found():
    with open('recents.json') as file:
        try:
            recently_found = loads(file.read())
        except JSONDecodeError:
            recently_found = []
    mangapill = get_mangapill_recents()

    for index, each in reversed(list(enumerate(recently_found))):
        if current_time - datetime.strptime(each[1], '%Y-%m-%d %H:%M:%S') >= timedelta(hours=48):
            recently_found.pop(index)
        elif each[0] in mangapill:
            mangapill.remove(each[0])

    intersection = titles.intersection(mangapill)

    update_recently_found(recently_found, intersection)

    print("New releases: " + ", ".join([each.title() for each in intersection]) if intersection else "No elements")


def comparison():
    if args.user:
        intersection = get_user_reading().intersection(get_mangapill_recents())
    else:
        intersection = titles.intersection(get_mangapill_recents())
    print("New releases: " + ", ".join([each.title() for each in intersection]) if intersection else "No elements")


if args.ttl:
    get_recently_found()
else:
    comparison()

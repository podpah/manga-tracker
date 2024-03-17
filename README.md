# manga-tracker
Manga tracker that allows you to check for new chapter releases

# Usage
You can run the script through the CLI:
```console
python main.py
``` 

Or through the .bat file (uses venv):
```console
runner.bat
```
Helpful to run on start up if you want to keep up with new releases

You can add your username to check your Anilist profile (line 12 for default or add -u flag) for what you are currently reading, but this will get the names in Romanji which Mangapill doesn't always have, so I suggest running the bookmarklet.js or:
```js
Array.from(document.querySelector('div.list-wrap').querySelectorAll('a'), a => a.textContent.trim())
```
And updating the titles.txt file. The bookmarklet already copies the list to your titles and removes the array structure

# Flags
Flag | Fullhand | Param | Help
--- | --- | --- | ---
-u | --user |  Anilist username | Anilist username if you want to check releases against it (not recommended). You can also specify it on line 12 as a default
-t | --ttl | No param | Decides whether to use TTL mode or not.  Default is yes but to change it, change store_false to store_true on line 13. TTL mode doesn't notify you of anything that has been found in the last 48 hours.

# Limitations
This only checks for the 120 latest releases on Mangapill, not if your manga has had new chapters
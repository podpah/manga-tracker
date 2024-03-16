# manga-tracker
Manga tracker that allows you to check for new chapter releases

# Usage
You can run the script through the CLI:
```console
python main.py
```
You can also specify a usernarme if you want to use Anilist to get your list of currents by adding it after main.py or by specifying a default on line 11

Or through the .bat file (uses venv):
```cmd
runner.bat
```
Helpful to run on start up if you want to keep up with new releases

You can uncomment the code to check your Anilist profile for what you are currently reading, but this will get the names in Romanji which Mangapill doesn't always have, so I suggest running the bookmarklet.js or:
```js
Array.from(document.querySelector('div.list-wrap').querySelectorAll('a'), a => a.textContent.trim())
```
And updating the titles.txt file. The bookmarklet already copies the list to your titles and removes the array structure

# Limitations
This only checks for the 120 latest releases on Mangapill, not if your manga has had new chapters
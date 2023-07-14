# genshin-scraper
Scraping <a href="https://genshin-impact.fandom.com/wiki/Albedo/Voice-Overs">Genshin impact characters</a> - Textual Data, Audio
Data using Scrapy Python.

```
Disclaimer: I don't promote illegal activity by stealing data from other websites, if the author and the rightful owner will disallow the usage of this program, please open an issue and I will remove this project immediately. Thank you.
```

### How to use
1. Clone this project
2. install requirements `pip install -r requirements.txt`
3. run `python main.py`

### Json Output
```json
[
{"name": "Albedo", "title": "Hello", "text": "I am Albedo, Chief Alchemist of the Knights of Favonius. You carry the aura of the stars, interesting... I would like to study you, if you do not mind. I'm certain we will have many opportunities to be alone in the future.", "path": "output/Albedo/VO Albedo Hello.ogg"},
{"name": "Albedo", "title": "Hello", "text": "What a view... How about a quick break so I can sketch this beautiful scenery?", "path": "output/Albedo/VO Albedo Chat - Still Life.ogg"},
{"name": "Albedo", "title": "Chat: Still Life", "text": "\"The truth of this world\"... *sigh* What could it be?", "path": "output/Albedo/VO Albedo Chat - Investigation.ogg"}
]
```
<h3>Audio Output</h3>
<audio controls>
  <source src="assets/VO Albedo Hello.ogg" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


### To add soon:
- detailed scraping if they are needed: (Lores, etc...)
- More voice suport (china, korea, japan)

### Goal of this project:
- to provide textual and audio data to use in machine learning and AI for "entertainment" purposes only.
- Textual data can be feed on GPT models for conversational or story generation.
- Audio data can be feed on Voice cloning AI models.
>Please note: You don't have the right to own all the assets that you have scraped from the websites that are used. All rights belong to Mihoyo Company.
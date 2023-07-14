from scrapy.utils.project import get_project_settings
import scrapy
import sys
import os
import threading
import requests


class GenshinSpider(scrapy.Spider):
    name = "genshin"
    allowed_domains = ["genshin-impact.fandom.com"]
    start_urls = ["https://genshin-impact.fandom.com/wiki/Voice_Actor"]

    def parse(self, response):
        self.output = self.settings.get('OUTPUT')

        # Get character
        table = response.css("table.wikitable")[0]

        character_names = table.css("tr td:nth-child(1) a::text").getall()
        eng_va_names = table.css("tr td:nth-child(2) a::text").getall()
        ch_va_names = table.css("tr td:nth-child(3) a::text").getall()
        ja_va_names = table.css("tr td:nth-child(4) a::text").getall()
        ko_va_names = table.css("tr td:nth-child(5) a::text").getall()

        dict_data = []

        for indx, name in enumerate(character_names):
            dict_data.append(
                {
                    "name": name,
                    "eng_va": eng_va_names[indx],
                    "ch_va": ch_va_names[indx],
                    "ko_va": ko_va_names[indx],
                    "ja_va": ja_va_names[indx],
                }
            )

        voice_url = "https://genshin-impact.fandom.com/wiki/{character}/Voice-Overs"

        for indx, data in enumerate(dict_data):
            yield scrapy.Request(
                url=voice_url.format(character=data["name"]),
                callback=self.getCharVoice,
                meta=dict_data[indx],
            )

    def getCharVoice(self, response):
        name = response.meta.get("name")
        voices_url = response.css("table.wikitable tr td span.audio-button a::attr(href)").getall()
        voices_file_name = response.css("table.wikitable tr td span.audio-button a::attr(title)").getall()
        title = response.css('table.wikitable tr th span[lang="en"]::text').getall()
        text = response.css('table.wikitable tr td span[lang="en"]::text').getall()

        output_folder = f'{self.output.split("/")[0]}/{name}/'
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        print(voices_url)

        threads = []
        for indx, text in enumerate(text):
            url = voices_url[indx]
            path = output_folder + voices_file_name[indx]
            t = threading.Thread(target=self.download, args=(path, url))
            t.start()
            threads.append(t)

            yield {"name": name, "title": title[indx], "text": text, "path": path}

        for t in threads:
            t.join()

        pass

    def download(self, path, url):
        with open(path, "wb") as f:
            f.write(requests.get(url).content)

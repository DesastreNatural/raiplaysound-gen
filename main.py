import requests

BASE_URL = "https://www.raiplaysound.it/"
exceptions = ["/programmi/radioscuola.json"]

class Genre:
    def __init__(self,json_elem):
        self.title = json_elem.get("title",json_elem.get("unique_name",""))
        self.path_id = json_elem.get("path_id")
        self.image_url = json_elem.get("image")
    def __str__(self):
        return f"{self.title}: {self.path_id}"

class Podcast:
    def __init__(self,json_elem):
        self.name = json_elem.get("name",json_elem.get("title",""))
        self.title = json_elem.get("title",json_elem.get("unique_name",""))
        self.description = json_elem.get("description","")
        self.path_id = json_elem.get("path_id","")
        self.image_url = json_elem.get("image","")
        self.social_image_url = json_elem.get("social_image","")
        self.onair_date = json_elem.get("onair_date","")
        self.create_date = json_elem.get("create_date","")
        self.update_date = json_elem.get("update_date","")
        self.year = json_elem.get("year","")
    def __str__(self):
        return f"{self.name}: {self.path_id}"

class PodcastEpisode:
    def __init__(self,json_elem):
        self.path_id = json_elem.get("path_id","")
        self.title = json_elem.get("title",json_elem.get("unique_name",""))
        self.toptitle = json_elem.get("toptitle","")
        self.subtitle = json_elem.get("subtitle","")
        self.image_url = json_elem.get("image","")
        self.duration = json_elem.get("path_id","")
        self.create_date = json_elem.get("create_date","")
        self.literal_duration = json_elem.get("literal_duration","")
        self.duration_small_format = json_elem.get("duration_small_format","")
        self.literal_publication_date = json_elem.get("literal_publication_date","")
        self.audio_link = json_elem["audio"].get("url","")
    def __str__(self):
        return f"{self.title}: {self.path_id}"

def gen_url(endpoint_id):
    return BASE_URL + endpoint_id

def get_generi():
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(gen_url("generi.json"),headers=headers)
    data = r.json()
    return [Genre(i) for i in data["block"]["cards"]]

def get_episode_data(path_id):
    r = requests.get(gen_url(path_id))
    data = r.json()
    return data["block"]["cards"][0]

def get_episode_list_from_podcast(path_id):
    if path_id not in exceptions:
        print(gen_url(path_id))
        r = requests.get(gen_url(path_id))
        if r.status_code == 200:
            data = r.json()
            if "block" in data:
                return [PodcastEpisode(i) for i in data.get("block",{}).get("cards") if "block" in data]
            else:
                return []
        else:
            return False
    return []

def get_podcast_list_from_genre(path_id):
    r = requests.get(gen_url(path_id))
    data = r.json()
    return [Podcast(i) for i in data["blocks"][0]["cards"]]

import argparse

def main():
    parser = argparse.ArgumentParser(description='Genera un feed rss da un programma RaiPlaySound')
    parser.add_argument('nomeprogramma')
    args = parser.parse_args()
    url = f"/programmi/{args.nomeprogramma}.json"
    episodes = get_episode_list_from_podcast(url)
    if episodes == False:
        print("Sei sicuro che il programma esista? :/")
    elif episodes == []:
        print("Problemi durante il download dei dati :(")
    else:
        for z in episodes:
            print(z)


if __name__ == '__main__':
    main()

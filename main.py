import argparse

from podcast import get_episode_list_from_podcast
from generator import generate_rss_from_podcast_data

def main():
    parser = argparse.ArgumentParser(description='Genera un feed rss da un programma RaiPlaySound')
    parser.add_argument('nomeprogramma')
    args = parser.parse_args()
    url = f"/programmi/{args.nomeprogramma}.json"
    podcast = get_episode_list_from_podcast(url)
    if podcast == False:
        print("Sei sicuro che il programma esista? :/")
    elif podcast == []:
        print("Problemi durante il download dei dati :(")
    else:
        generate_rss_from_podcast_data(podcast,f"{args.nomeprogramma}.xml")


if __name__ == '__main__':
    main()

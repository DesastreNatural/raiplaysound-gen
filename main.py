import os
import argparse

from podcast import get_episode_list_from_podcast
from generator import generate_rss_from_podcast_data

def main():
    parser = argparse.ArgumentParser(description='Genera un feed rss da un programma RaiPlaySound')
    parser.add_argument('nomeprogramma')
    parser.add_argument('--base-output-dir', dest='basedir', type=str, default='',
                    help='definisce una cartella dove andare a salvare il file XML (di default nella cartella dove viene eseguito)')
    args = parser.parse_args()
    url = f"/programmi/{args.nomeprogramma}.json"
    
    podcast = get_episode_list_from_podcast(url)
    if podcast == False:
        print("Sei sicuro che il programma esista? :/")
    elif podcast == []:
        print("Problemi durante il download dei dati :(")
    else:
        generate_rss_from_podcast_data(podcast,os.path.join(args.basedir,f"{args.nomeprogramma}.xml"))


if __name__ == '__main__':
    main()

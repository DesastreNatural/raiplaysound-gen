from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

def generate_rss_from_podcast_data(podcast,path):
    (info,episodes) = podcast
    fg = FeedGenerator()
    fg.id(info.link)
    fg.title(info.title)
    fg.link(href=info.link, rel='alternate' )
    fg.logo(info.image_url)
    fg.subtitle(info.description)
    fg.language('it')
    fg.load_extension('podcast')
    for episode in episodes:
        entry = fg.add_entry()
        entry.id(episode.audio_link)
        entry.title(episode.toptitle)
        entry.description(episode.subtitle)
        entry.enclosure(episode.audio_link, 0, 'audio/mpeg')
        entry.published(datetime.strptime(episode.create_date, '%d-%m-%Y').replace(tzinfo=timezone.utc))
    fg.rss_str(pretty=True)
    fg.rss_file(path)

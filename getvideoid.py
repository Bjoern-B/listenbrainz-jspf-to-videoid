from ytmusicapi import YTMusic
from pprint import pprint
import json
yt = YTMusic('browser.json')

# Datei einlesen
with open("Weekly Exploration for Bjoern_B, week of 2025-09-01 Mon.jspf", "r", encoding="utf-8") as f:
    jspf_data = json.load(f)

# Tracks liegen in playlist -> track
tracks = jspf_data.get("playlist", {}).get("track", [])

track_infos = []
durations = []
titles = []

# Ausgabe: Titel, Album, Creator
for track in tracks:
    title = track.get("title", "Unbekannt")
    album = track.get("album", "Unbekannt")
    creator = track.get("creator", "Unbekannt")

    duration_ms = track.get("duration")
    duration_s = None

    if isinstance(duration_ms, (int, float)):
        duration_s = round(duration_ms / 1000)

    #print(f"{title} | {album} | {creator} | {duration_s if duration_s is not None else 'Unbekannt'}")


    # Zu Listen hinzufügen
    titles.append(title)
    track_infos.append((title, album, creator))
    durations.append(duration_s if duration_s is not None else "Unbekannt")

# Optional: Listen ausgeben
#print(titles)
#print(track_infos)
#print(durations)


#titles = ['Shape of You', 'Watermelon Sugar', 'Crazy in Love', 'Skyfall', 'Crab Rave', 'Ghost', 'Unwritten', 'Runaway', 'The Code', 'I Love It', 'Don’t Stop Believin’', 'A Bar Song (Tipsy)', 'That’s So True', 'Sarà perché ti amo', 'Say My Name (remix)', 'Baller', 'Symphony', 'Lighter', 'Rolling in the Deep', 'Creep', 'Outside', 'her', 'Just Dance', 'Black Sheep', 'Violet', 'Barbie Girl', 'Forever Young', 'Feel It Still', 'Geronimo', 'Pompeii', 'Down With the Sickness', 'from me to u', 'You Spin Me Round (Like a Record)', 'Sweet Child o’ Mine', 'Steve’s Lava Chicken', 'Blood // Water', 'Mystical Magical', 'In the End', 'did i tell u that i miss u', 'On My Way', 'Video Games', 'End of Time', 'Before You Go', 'Dangerous', 'GigaChad Theme - Phonk House Version', 'Last Friday Night (T.G.I.F.)', 'Lost on You', 'edamame', 'ただ君に晴れ', 'Born With a Broken Heart']
#track_infos = [('Shape of You', '÷', 'Ed Sheeran'), ('Watermelon Sugar', 'Fine Line', 'Harry Styles'), ('Crazy in Love', 'Dangerously in Love', 'Beyoncé feat. Jay‐Z'), ('Skyfall', 'Glastonbury 2016', 'Adele'), ('Crab Rave', 'Crab Rave', 'Noisestorm'), ('Ghost', 'Ghost', 'Confetti'), ('Unwritten', 'Unwritten', 'Natasha Bedingfield'), ('Runaway', 'All My Demons Greeting Me as a Friend', 'AURORA'), ('The Code', 'The Code', 'Nemo'), ('I Love It', 'Icona Pop', 'Icona Pop feat. Charli XCX'), ('Don’t Stop Believin’', 'Escape', 'Journey'), ('A Bar Song (Tipsy)', 'Where I’ve Been, isn’t Where I’m Going', 'Shaboozey'), ('That’s So True', 'The Secret of Us (deluxe)', 'Gracie Abrams'), ('Sarà perché ti amo', 'Parla col cuore', 'Ricchi e Poveri'), ('Say My Name (remix)', 'Say My Name (remix)', 'Morgan Seatree feat. Florence + the Machine'), ('Baller', 'Bittersüß', 'Abor & Tynna'), ('Symphony', 'So Good', 'Clean Bandit feat. Zara Larsson'), ('Lighter', 'Lighter', 'Kyle Alessandro'), ('Rolling in the Deep', '21', 'Adele'), ('Creep', 'Pablo Honey', 'Radiohead'), ('Outside', 'Motion', 'Calvin Harris feat. Ellie Goulding'), ('her', 'her', 'JVKE'), ('Just Dance', 'The Fame', 'Lady Gaga featuring Colby O’Donis'), ('Black Sheep', 'Fantasies: Expanded Edition', 'Metric'), ('Violet', 'Spin the Globe', 'Connor Price & Killa'), ('Barbie Girl', 'Aquarium', 'Aqua'), ('Forever Young', 'Forever Young', 'Alphaville'), ('Feel It Still', 'Woodstock', 'Portugal. The Man'), ('Geronimo', 'Bombs Away', 'Sheppard'), ('Pompeii', 'Bad Blood', 'Bastille'), ('Down With the Sickness', 'The Sickness', 'Disturbed'), ('from me to u', 'METAL FORTH', 'BABYMETAL feat. Poppy'), ('You Spin Me Round (Like a Record)', '“Youthquake”', 'Dead or Alive'), ('Sweet Child o’ Mine', 'Appetite for Destruction', 'Guns N’ Roses'), ('Steve’s Lava Chicken', 'A Minecraft Movie: Original Motion Picture Soundtrack', 'Jack Black'), ('Blood // Water', 'blood // water', 'grandson'), ('Mystical Magical', 'American Heart', 'Benson Boone'), ('In the End', 'Hybrid Theory', 'Linkin Park'), ('did i tell u that i miss u', 'did i tell u that i miss u', 'adore'), ('On My Way', 'World of Walker', 'Alan Walker, Sabrina Carpenter & Farruko'), ('Video Games', 'Born to Die', 'Lana Del Rey'), ('End of Time', 'End of Time', 'K‐391, Alan Walker & Ahrix'), ('Before You Go', 'Divinely Uninspired to a Hellish Extent (Extended Edition)', 'Lewis Capaldi'), ('Dangerous', 'Listen', 'David Guetta feat. Sam Martin'), ('GigaChad Theme - Phonk House Version', 'GigaChad Theme (Phonk House Version)', 'g3ox_em'), ('Last Friday Night (T.G.I.F.)', 'Teenage Dream', 'Katy Perry'), ('Lost on You', 'Lost on You', 'LP'), ('edamame', 'eat ya veggies', 'bbno$ feat. Rich Brian'), ('ただ君に晴れ', '負け犬にアンコールはいらない', 'ヨルシカ'), ('Born With a Broken Heart', 'FUNNY little FEARS', 'Damiano David')]
#durations = [234, 174, 236, 286, 161, 169, 258, 249, 180, 155, 250, 171, 166, 242, 168, 159, 213, 176, 228, 237, 227, 172, 242, 296, 122, 195, 226, 162, 219, 214, 279, 205, 195, 356, 34, 215, 166, 216, 118, 194, 282, 188, 215, 204, 146, 231, 267, 134, 199, 209]

def find_videoid_by_title_and_duration(search_results, title, duration, tolerance=2):
    # First, try exact match
    for track in search_results:
        if track.get("title") == title and track.get("duration_seconds") == duration:
            return track.get("videoId")
    # If not found, try with tolerance
    for track in search_results:
        track_title = track.get("title")
        track_duration = track.get("duration_seconds")
        if (
            track_title == title
            and track_duration is not None
            and abs(track_duration - duration) <= tolerance
        ):
            return track.get("videoId")
    # Last, check if title is a substring (case-insensitive) with duration tolerance
    for track in search_results:
        track_title = track.get("title", "")
        track_duration = track.get("duration_seconds")
        if (
            title.lower() in track_title.lower()
            and track_duration is not None
            and abs(track_duration - duration) <= tolerance
        ):
            return track.get("videoId")
    # If still nothing, return the first videoId if available
    if search_results:
        return search_results[0].get("videoId")
    return None

videoids = []

for (title, album, creator), duration in zip(track_infos, durations):
    # Build the search query
    song_query = f"{title} {album} {creator}"
    # Search for the song
    search_results = yt.search(song_query, limit=5, filter='songs')
    # Find the videoId
    videoid = find_videoid_by_title_and_duration(search_results, title, duration)
    videoids.append(videoid)
    print(f"{title}: {videoid}")

# Optional: print all videoids
print(videoids)

def write_videoids_to_file(videoids, filename="to-dl.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for vid in videoids:
            if vid:  # Only write non-empty videoids
                f.write(f"{vid}\n")

# Call the function after collecting videoids
write_videoids_to_file(videoids)
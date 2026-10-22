def add_song(songs):
    """Asks the user for song details and adds a new song dictionary to the list."""
    title = input("Enter song title: ")
    artist = input("Enter artist: ")
    
    try:
        minutes = int(input("Enter duration (minutes): "))
        seconds = int(input("Enter duration (seconds): "))
    except ValueError:
        print("Invalid input for duration. Please enter numbers.")
        return

    total_seconds = (minutes * 60) + seconds
    
    new_song = {
        "title": title,
        "artist": artist,
        "duration": total_seconds,
        "plays": 0
    }
    
    songs.append(new_song)
    print(f"\nSuccessfully added '{title}' by {artist}!")


def record_listen(songs):
    """Searches for a song by title and increments its play count by 1."""
    if not songs:
        print("\nYour song library is empty. Add some songs first!")
        return

    title = input("Enter a song title: ")
    found = False
    
    for song in songs:
        if song["title"].lower() == title.lower():
            song["plays"] += 1
            print(f"\nRecorded a listen for '{song['title']}'! Total plays: {song['plays']}")
            found = True
            break
            
    if not found:
        print(f"\nError: Song '{title}' does not exist in your library.")


def generate_wrapped(songs):
    """Calculates and displays listening statistics and your most-played song."""
    if not songs:
        print("\nYour song library is empty. Add some songs first!")
        return

    total_songs = len(songs)
    total_plays = sum(song["plays"] for song in songs)
    
    if total_plays == 0:
        print("\n========== YOUR SPOTIFY WRAPPED ==========")
        print(f"\nTotal Songs: {total_songs}")
        print("Total Plays: 0")
        print("Total Listening Time: 0 minutes")
        print("\nYour Most Played Song:")
        print("No plays recorded yet!")
        print("\n==========================================")
        return

    total_listening_seconds = sum(song["duration"] * song["plays"] for song in songs)
    total_listening_minutes = total_listening_seconds // 60

    most_played = max(songs, key=lambda s: s["plays"])

    print("\n========== YOUR SPOTIFY WRAPPED ==========")
    print(f"\nTotal Songs: {total_songs}")
    print(f"Total Plays: {total_plays}")
    print(f"Total Listening Time: {total_listening_minutes} minutes")
    print(f"\nYour Most Played Song:")
    print(f"{most_played['title']} - {most_played['artist']} ({most_played['plays']} plays)")
    print("\n==========================================")
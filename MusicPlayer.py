import os

class Playlist:
    def __init__(self, name, genre):

        self.name = name
        self.genre = genre


def create_playlists():
    name = input("Enter playlist name: ")
    genre = input("Enter genre: ")
    playlist = Playlist(name, genre)
    return playlist

def search_playlists(playlists, name):
    matching_playlists = [p for p in playlists if name.lower() in p.name.lower()]
    if matching_playlists:
        print("Matching playlists:")
        for i, playlist in enumerate(matching_playlists):
            print(f"{i+1}. {playlist.name} ({playlist.genre})")
    else:
        print("No playlists found with that name.")


def add_rating(playlist,ratings):
    rating = int(input("Enter ratings between 1-5:"))
    if rating <=5:
       ratings.append(rating)
       print("Rating added")
       print(ratings)
    else:
       print("Invalid rating")

# Initializing empty playlists list
playlists = []
ratings = []


# Main loop
while True:
    print("\nMenu:")
    print("1. Create playlist")
    print("2. Search playlists")
    print("3. Add rating")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        playlist = create_playlists()
        playlists.append(playlist)
        print(f"Playlist '{playlist.name}' created.")

    elif choice == '2':
        name = input("Enter playlist name to search: ")
        search_playlists(playlists, name)

    elif choice == '3':
        if not playlists:
            print("No playlists created yet.")
        else:
            for i, playlist in enumerate(playlists):
                print(f"{i+1}. {playlist.name} ({playlist.genre})")
            choice = int(input("Enter the number of the playlist to rate: "))
            if choice<=1 and  choice <=len(playlists):
                add_rating(playlist,ratings)

            else:
                print("Invalid playlist number.")


    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

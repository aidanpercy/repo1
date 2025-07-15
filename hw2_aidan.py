# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}


user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid vallue. Please enter a number."

def main_menu():
    while True:
        print("1: A list of unique artists in the top 10 most played songs")
        print("2: Song details by ranking")
        print("3: Songs by an artist")
        print("4: Songs ordered by length")
        print("0: Exit")
        choice = input("Enter what you would like to browse:")
        if choice == "1":
            unique_artists = set()
            for song in spotify.values():
                for artist in song["artists"]:
                    unique_artists.add(artist)
            output = ", ".join(sorted(unique_artists))
            print(output)
        elif choice == "2":
            choice_2 = input("Enter the ranking you're interested in (between 1 and 10): ")
            try:
                num = int(choice_2)
            except ValueError:
                print("Invalid input. Please enter a number.")
                return
            if num > 10 or num < 1:
                print("Ranking out of range.")
                return
            else:
                print(f"{choice_2}: {spotify[num]["title"]} by {', '.join(spotify[num]["artists"])}")
        elif choice == "3":
            choice_3 = input("Enter the name of the artist you're interested in: ")
            no_case_choice_3 = choice_3.lower()
            songs_by_artist = []
            for song in spotify.values():
                for artist in song["artists"]:
                    if no_case_choice_3 == artist.lower():
                        songs_by_artist.append((rank, song["title"]))
            if not songs_by_artist:
                print(f"No songs were found by {choice_3}")
            else:
                for song in songs_by_artist:
                    print(f"{"rank"}: {"title"}")
        elif choice == "0":
            exit()

main_menu()
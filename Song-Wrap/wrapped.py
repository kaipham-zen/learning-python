from __future__ import annotations
from song import Song, StreamingHistory
import numpy as np
import math

def check_password(username: str, password: str)-> bool:
    '''
    Verify the authentication of the user
    
    @parameters
    - username: the input username
    - password: the input password

    @returns
    - bool: whether the password and username are correct
    '''
    #create a path to access user information
    filename = "user_info/" + username + ".txt"

    #check if username existed
    try:
        f = open(filename,"r")
    except FileNotFoundError:
        print(f"No {username} found :((")
        return False

    #test if password is correct
    file_password = f.readline().strip()
    f.close()

    #check if password correct
    if (password == file_password):
        print("Login successful :))")
        return True
    else:
        print("Username and password do not match :((")
        return False

def extract_song_details(filename: str, month: int, year: int) -> list[Song]:
    """
    Create list of Song objects within a specified month and year
    where a Song object is identified by name, artist, genre and song duration

    @parameters
    - filename (str): The name of the file containing song details.
    - month: (int): month for which the songs need to be extracted from
    - year(int): year for which the songs need to be extracted from

    @returns 
    - list[Songs]: A list of Song objects.
    """
    f = open(filename,"r")
    #create list of songs
    songs = []

    #skip the first line that contain password
    line = f.readline() 

    #read each line until there is no more line (length of line = 0)
    line = f.readline()
    while len(line) != 0:
        #split the line to get the date via list
        line_list = line.split(",")
        line_month = line_list[5].split("-")[1]
        line_year = line_list[5].split("-")[2]
        
        #print line if years and months are matching
        if int(line_month) == month and int(line_year) == year:
            #create song object
            song_object = StreamingHistory(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4],line_list[5])
            
            #add the created object into a list
            songs.append(song_object)
        line = f.readline()
    f.close()
    return songs
    
def count_streams(songs: list, data_type: str) -> dict[Song]:
    """
    Counts the number of streaming times for each unique song, artist, or genre.
    Iterates over a list of Song objects and counts the occurrences of a 
    specified data type (song, artist, or genre). 
    The resulting counts are stored in a dictionary
        - key: the name of the song, artist, or genre
        - value: the number of streaming times. 
    If a key already exists in the dictionary, its value is incremented by one.

    @parameters
    - songs (list[Song]): A list of Song objects.
    - data_type (str): The type of data to count (song, artist, or genre).

    @returns 
    - dict[Song]: A dictionary with the unique song, artist, or genre as keys and the 
                   corresponding streaming counts as values.
    """
    streaming_data = {}

    #itereate through every song object in songs list
    for song in songs:
        #check what is data type input [song, artist, genre]
        if data_type == "song":
            key = song.song_name
        elif data_type == "artist":
            key = song.artist
        elif data_type == "genre":
            key = song.genre

        #if key not in streaming data, count as 1, else increment by 1
        if key not in streaming_data:
            streaming_data[key] = 1
        else:
            streaming_data[key] += 1
    return streaming_data

def favorite_streams(streaming_data: dict) -> set(Song):
    #create array store counts of streaming time
    streaming_array = np.array([value for value in streaming_data.values()])
    #get average streaming time
    average_streaming_time = streaming_array.mean()
    #get set of identical favorite streaming key based on the count larger than average count among all streams
    favorites = {key for key,value in streaming_data.items() if value>=average_streaming_time}
    return favorites

def find_most_frequent(streaming_data: dict) -> tuple(str, int):
    """
    Identifies the most frequently streamed song, artist, or genre.

    Examines a dictionary of streaming data, where keys represent unique 
    songs, artists, or genres, and values represent the number of streaming times. 
    Return the key-value pair with the highest number of streaming times.

    @parameters 
    - streaming_data (dict): A dictionary containing the streaming data.

    @returns 
    - tuple(str, int): A tuple containing the key (song, artist, or genre) 
                      and its corresponding number of streaming times.
    """
    #find the maximum values in list values of streaming_data dictionary, exit if none
    try:
        highest_frequency = max(streaming_data.values())
    except ValueError:
        exit()

    #loop through every key in dictionary
    for key in streaming_data:
        #check if the value of the key stored in dictionary equal to the highest frequency
        if streaming_data[key] == highest_frequency:
            #return tuple with matching key and highest_frequency
            return (key,highest_frequency)

def calculate_streaming_seconds(song_array) -> int:
    """
    Calculates the total streaming seconds for the songs in the list
    by iterating through each.

    @parameters
    - songs (list[Song]): the list of songs

    @returns 
    - int: The total streaming seconds
    """
    #create array store all song duration
    song_array = np.array(song_array)
    #return total streaming
    return np.sum(song_array)

def wrapped(key:str, top:tuple) -> None:
    '''
    Print top song/artist/genre in the specified format
    '''
    print(key + " "*(8-len(key)) + top[0] + " "*(32-len(top[0])) + "{:04d}".format(top[1]))

def wrapped_favorite(key:str, favorites:set) -> None:
    print(key)
    for favorite in favorites:
        print(" "*6 + "- " + favorite)

def total_streaming_convert(total_stream: int) -> str:
    '''
    Seconds to DD:HH:MM:SS format
    '''
    DD = total_stream // 86400
    HH = (total_stream%86400)//3600
    MM = ((total_stream%86400)%3600)//60
    SS = ((total_stream%86400)%3600)%60
    #return in DD:HH:MM:SS format
    return f"{DD:02d}:{HH:02d}:{MM:02d}:{SS:02d}"

def print_wrapped_wall(top_song: tuple(str, int), top_artist: tuple(str, int), 
                      top_genre: tuple(str, int), total_duration: int,
                      actual_streaming_time: int,
                      favorite_songs: set, favorite_artists: set,
                      favorite_genres: set) -> None:
    """
    Displays the Music Wrapped Wall.

    @parameters
    - top_song (tuple(str, int)): the name of top song and its streaming frequency.
    - top_artist (tuple(str, int)): the name of top artist and its streaming frequency.
    - top_genre (tuple(str, int)): the name of top genre and its streaming frequency.
    - total_duration (int): The total duration seconds.
    - actual_streaming_time (int): Actual streaming time in seconds
    - favorite_songs (set(str)): name of favorite songs that has played more than average count among all songs
    - favorite_artists (set(str)): name of favorite artists that has played more than average count among all artists
    - favorite_genre (set(str)): name of favorite genre that has played more than average count among all genres

    """
    #display banner for the Wrapped Wall
    print("*"*52 + "\n" + "MONTHLY MUSIC WRAPPED WALL\n" + "*"*52)
    print("Top" + " "*5 + "Name" + " "*28 + "Stream Times")
    #print the most streamed song, artist and genre using defined function wrapped(key,top)
    wrapped("Song", top_song)
    wrapped("Artist", top_artist)
    wrapped("Genre", top_genre)
    
    print("*"*52)
    wrapped_favorite("Favorite Songs", favorite_songs)
    wrapped_favorite("Favorite Artists", favorite_artists)
    wrapped_favorite("Favorite Genres", favorite_genres)
    print("*"*52)

    #print total duration of all songs
    total_duration_time = total_streaming_convert(total_duration)
    print("Total duration" + " "*26 + total_duration_time)

    #print actual streaming time
    actual_streaming_time = total_streaming_convert(actual_streaming_time)
    print("Actual streaming" + " "*24 + actual_streaming_time)


def main():
    '''
    Where your main program will run
    '''
    # Display the welcoming message
    print("Welcome to USYD MUSIC!")

    #global variable to count attempts
    attempts = 0 

    # Prompting for username and password until reached 3 using while loop
    while attempts != 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        attempts += 1
        
        # if username and password are matched, break the while loop
        if check_password(username, password):
            break
        else:
            print()
    # Check whether 3 limited attempts has been reached
    else:
        print("Maximum of 3 attempts has been reached. You will be temporarily disabled from logging in :((")
        exit()
    
    print()
    
    # Prompt for specified month, check if month input correctly
    while True:
        try:
            month = int(input("Specify the month that you want to display: "))
            #break the loop if month between 1 and 12
            if month in range(1,13,1): 
                break
            #if month is integer but out of range
            print("Month must be between 1 and 12, inclusively :((")
        #print error for month input
        except ValueError:
            print("Month must be an integer :((")

    # Prompt for specified year, check if year input correctly
    while True:
        try:
            year = int(input("Specify the year that you want to display: "))
            #check if year larger than 2000
            if year >= 2000:
                break
            #print error if year less than 2000
            print("Year must be larger than 2000 :((")
        #print error if year is not integer
        except ValueError:
            print("Year must be an integer :((")
    print()

    # Extract the song details
    filename = "user_info/" + username + ".txt"
    songs = extract_song_details(filename,month,year)
    song_duration = [song.duration for song in songs]

    # get streaming data
    streaming_song = count_streams(songs, "song")
    streaming_artist = count_streams(songs, "artist")
    streaming_genre = count_streams(songs, "genre")

    # Compute the most streaming song, artist and genre 
    top_song = find_most_frequent(streaming_song)
    top_artist = find_most_frequent(streaming_artist)
    top_genre = find_most_frequent(streaming_genre)

    # Get favorite songs, artists and genre   
    favorite_songs = favorite_streams(streaming_song)
    favorite_artists = favorite_streams(streaming_artist)
    favorite_genres = favorite_streams(streaming_genre)

    #calculate total duration of songs list in integer
    total_duration = calculate_streaming_seconds(song_duration)

    #get actual_streaming_time
    actual_streaming_time = StreamingHistory.total_streaming_time
    
    # Display the Wrapped Wall
    print_wrapped_wall(top_song, top_artist, top_genre, total_duration, actual_streaming_time, favorite_songs, favorite_artists, favorite_genres)


if __name__ == '__main__':
    main()
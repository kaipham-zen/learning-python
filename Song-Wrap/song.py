from __future__ import annotations
class Song:
    def __init__(self, name: str, artist: str, genre: str, duration: str):
        '''
        Initialises a Song object given an artist name, a song genre, 
        and song duration.

        @Attributes:
        - song_name: The name of the song
        - artist: The name of the song's artist
        - genre: The genre of the song
        - duration: The duration of the song in seconds converted from mm:ss

        @Parameters:
        - name (str): The name of the song.
        - artist (str): The name of the artist who performed or composed the song.
        - genre (str): The genre of the song (e.g., pop, rock, classical).
        - duration (str): The duration of the song in a string format, typically in 
                        the form of 'minutes:seconds' (e.g., '03:45').

        '''
        self.song_name = name
        self.artist = artist
        self.genre = genre
        #call set_duration func that set duration to integer
        self.set_duration(duration)

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.song_name == other.song_name and self.artist == other.artist
        return False
    
    def __repr__(self):
        return f"{self.song_name}, {self.artist}, {self.genre}"
    
    def get_name(self) -> str:
        '''
        Returns the name of the song
        '''
        return self.song_name
    
    def get_artist(self) -> str:
        '''
        Returns artist of the song
        '''
        return self.artist

    
    def get_genre(self) -> str:
        '''
        Returns the value of the instance attribute `genre`.
        '''
        return self.genre

    
    def set_duration(self, duration: str) -> None:
        '''
        Converts the given song's duration to seconds
        And sets the duration of the song.

        @Parameters:
        - duration (str): The duration of the song in string format mm:ss.

        '''
        #list that seperates mm and ss
        duration = duration.strip().split(":")

        #convert to seconds
        duration = int(duration[0])*60 + int(duration[1])

        #set duration of song object
        self.duration = duration

    
    def get_duration(self) -> int:
        '''
        Returns the duration of the song in seconds.
        '''
        return self.duration

    def is_same(self, check_song: Song) -> bool:
        '''
        Checks whether two Song objects are identical.
        If their name and artist are the same, returns True.
        Otherwise, returns False.

        @parameters:
        - check_song (Song): The Song object to compare with.

        '''
        if self.song_name == check_song.song_name and self.artist == check_song.artist:
            return True
        return False

    
    def has_same_artist(self, check_song: Song) -> bool:
        '''
        Checks whether two Song objects have the same artist.
        If their attribute artist are identical, returns True.
        Otherwise, returns False.

        @parameters:
        - check_song (Song): The Song object to compare with.
        '''
        if self.artist == check_song.artist:
            return True
        return False

    
    def has_same_genre(self, check_song: Song) -> bool:
        '''
        Checks whether two Song objects have the same genre.
        If their attribute genre are identical, returns True.
        Otherwise, returns False.

        @parameters:
        - check_song(Song): The Song object to compare with.
        '''
        if self.genre == check_song.genre:
            return True
        return False


    def get_longest(self, check_song: Song) -> Song | None:
        '''
        Compares the durations of two Song objects
        Returns the one with the longer duration.

        @parameters:
        - check_song(Song): The Song object to compare with.
        '''
        #if the song object has longer duration than the check song, return song object
        if self.duration > check_song.duration:
            return self
        #else if the song object has shorter duration, return the check song
        elif self.duration < check_song.duration:
            return check_song
        #else if their durations are tied, return None
        else:
            return None

class StreamingHistory(Song):
    '''
    Streaming Time History of Songs
    '''
    #class variable to store historical actual streaming time
    total_streaming_time = 0

    def __init__(self,name,artist,genre,duration,streaming_time,date):
        super().__init__(name,artist,genre,duration)
        self._date = date
        self._streaming_time = self.set_streaming_time(streaming_time)
        StreamingHistory.total_streaming_time += self.streaming_time
    
    def __repr__(self):
        # Represent an history object of how much time user listen to the particular song on which date
        return f"{self.song_name}, {self.artist}, Streamed in {self._streaming_time}s on {self.date}"
    
    def set_streaming_time(self, streaming_time: str) -> None:
        '''
        Converts the given song's streaming time to seconds
        And sets the streaming time of the song.

        @Parameters:
        - streaming_time (str): The streaming time of the song in string format mm:ss.

        '''
        #list that seperates mm and ss
        streaming_time = streaming_time.strip().split(":")

        #convert to seconds
        streaming_time = int(streaming_time[0])*60 + int(streaming_time[1])

        #set streaming_time of song object
        self.streaming_time = streaming_time

if __name__ == '__main__':
    pass
    
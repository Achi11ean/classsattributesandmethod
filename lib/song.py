#!/usr/bin/env python3


class Song:
    count = 0 
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        if artist not in Song.artists:
            Song.artists.append(artist)

        if genre not in Song.genres:
            Song.genres.append(genre)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else: 
            Song.artist_count[artist] = 1 


    @classmethod
    def song_count(cls):
        return cls.count
    @classmethod
    def all_artists(cls):
        return cls.artists
    @classmethod
    def all_genres(cls):
        return cls.genres


song = Song("99 Problems", "Jay Z", "Rap")
print(Song.song_count())
print(Song.all_artists())
print(Song.all_genres())
    

class Account:
    acc_list = []
    def __init__(self, name, ID, albums = [], playlists = []):
        self.name = name
        self.ID = ID
        self.friends = []
        self.albums = albums
        self.playlists = playlists
        self.posts = []
        self.feed = []
        Account.acc_list.append(self)
    
    def new_album(self, album):
        self.albums.append(albums)
    def new_playlist(self, playlist):
        self.playlists.append(playlist)

    def new_friend(self, other):
        """
        """
        other.friends.append(self)
        self.friends.append(other)

    def follow(self, playlist):
        """
        playlist.add_follower(self)
        self.playlists.append(playlist)
        """
        playlist.add_follower(self)
        self.playlists.append(playlist)
    def post(self, p):
        self.posts.append(p)
        #call view function for all friends to add to feed
    def add_to_feed(self, new_p):
        self.feed.append(new_p)

    def tune_in(self, other):
        """
        tune into the other fuckers song listening
        """
    def get_current_song(self):
        """
        returns [the current song playing, tick]
        """
class Post:
    def __init__(self, song, content):
        self.song = song
        self.content = content
    def edit(self, new_content):
        self.content = new_content

class AccountStatus:
    def __init__(self):
        self.playing_song = False
        self.current_song = None
        self.time_stamp = 0

class Song:
    def __init__(self, title, genre, artist, length):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.length

class SongList:
    def __init__(self, name, listofsongs = []):
        self.name = name
        self.listofsongs = listofsongs
    def add_song(self, song):
        self.listofsongs.append(song)
    def clear(self):
        self.listofsongs = []

class Album(SongList):
    def __init__(self, name, artist, listofsongs):
        self.artist = artist
        SongList.__init__(self, name, listofsongs)

class PlayList(SongList):
    def __init__(self, name, listofsongs = []):
        self.follower_count = 0
        self.follower_list = []
        SongList.__init__(self, name, listofsongs)
    def add_follower(self, account):
        self.follower_count += 1
        self.follower_list.append(account)

    

from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MediaType(Enum):
    CD = "CD"
    MP3 = "MP3"
    TAPE = "TAPE"


############################################
# Definition of Classes
############################################

class music_MusicLibrary:

    def __init__(self, name: str, music_MusicLibrary: set["music_Artist"] = None):
        self.name = name
        self.music_MusicLibrary = music_MusicLibrary if music_MusicLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def music_MusicLibrary(self):
        return self.__music_MusicLibrary

    @music_MusicLibrary.setter
    def music_MusicLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_MusicLibrary__music_MusicLibrary", None)
        self.__music_MusicLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "music_Artist"):
                    opp_val = getattr(item, "music_Artist", None)
                    
                    if opp_val == self:
                        setattr(item, "music_Artist", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "music_Artist"):
                    opp_val = getattr(item, "music_Artist", None)
                    
                    setattr(item, "music_Artist", self)
                    

class music_Work:

    def __init__(self, name: str, whenMade: str, notes: str, mediaTypes: str, Work: "music_Artist" = None, works: "music_Artist" = None):
        self.name = name
        self.whenMade = whenMade
        self.notes = notes
        self.mediaTypes = mediaTypes
        self.Work = Work
        self.works = works
        
    @property
    def whenMade(self) -> str:
        return self.__whenMade

    @whenMade.setter
    def whenMade(self, whenMade: str):
        self.__whenMade = whenMade

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mediaTypes(self) -> str:
        return self.__mediaTypes

    @mediaTypes.setter
    def mediaTypes(self, mediaTypes: str):
        self.__mediaTypes = mediaTypes

    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def Work(self):
        return self.__Work

    @Work.setter
    def Work(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_Work__Work", None)
        self.__Work = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performer"):
                opp_val = getattr(old_value, "performer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performer"):
                opp_val = getattr(value, "performer", None)
                if opp_val is None:
                    setattr(value, "performer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def works(self):
        return self.__works

    @works.setter
    def works(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_Work__works", None)
        self.__works = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artist"):
                opp_val = getattr(old_value, "Artist", None)
                if opp_val == self:
                    setattr(old_value, "Artist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artist"):
                opp_val = getattr(value, "Artist", None)
                setattr(value, "Artist", self)

class music_Artist:

    def __init__(self, name: str, notes: str, performer: set["music_Work"] = None, music_Artist: "music_MusicLibrary" = None, Artist: "music_Work" = None):
        self.name = name
        self.notes = notes
        self.performer = performer if performer is not None else set()
        self.music_Artist = music_Artist
        self.Artist = Artist
        
    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def performer(self):
        return self.__performer

    @performer.setter
    def performer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_Artist__performer", None)
        self.__performer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Work"):
                    opp_val = getattr(item, "Work", None)
                    
                    if opp_val == self:
                        setattr(item, "Work", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Work"):
                    opp_val = getattr(item, "Work", None)
                    
                    setattr(item, "Work", self)
                    

    @property
    def Artist(self):
        return self.__Artist

    @Artist.setter
    def Artist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_Artist__Artist", None)
        self.__Artist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "works"):
                opp_val = getattr(old_value, "works", None)
                if opp_val == self:
                    setattr(old_value, "works", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "works"):
                opp_val = getattr(value, "works", None)
                setattr(value, "works", self)

    @property
    def music_Artist(self):
        return self.__music_Artist

    @music_Artist.setter
    def music_Artist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_music_Artist__music_Artist", None)
        self.__music_Artist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "music_MusicLibrary"):
                opp_val = getattr(old_value, "music_MusicLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "music_MusicLibrary"):
                opp_val = getattr(value, "music_MusicLibrary", None)
                if opp_val is None:
                    setattr(value, "music_MusicLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def printState(self):
        # TODO: Implement printState method
        pass

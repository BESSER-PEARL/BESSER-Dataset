from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class State(Enum):
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"


############################################
# Definition of Classes
############################################

class MediaPlayer_BaseObject:

    def __init__(self, id: int, propertyChangeSupport: str):
        self.id = id
        self.propertyChangeSupport = propertyChangeSupport
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def propertyChangeSupport(self) -> str:
        return self.__propertyChangeSupport

    @propertyChangeSupport.setter
    def propertyChangeSupport(self, propertyChangeSupport: str):
        self.__propertyChangeSupport = propertyChangeSupport

    def addPropertyChangeListener(self, listener: str):
        # TODO: Implement addPropertyChangeListener method
        pass

    def removePropertyChangeListener(self, listener: str):
        # TODO: Implement removePropertyChangeListener method
        pass

class MediaPlayer_PlayLayer:

    def __init__(self, MediaPlayer_PlayLayer: set["MediaPlayer_MediaApi"] = None, MediaPlayer_PlayLayer9: "MediaPlayer_Library" = None):
        self.MediaPlayer_PlayLayer = MediaPlayer_PlayLayer if MediaPlayer_PlayLayer is not None else set()
        self.MediaPlayer_PlayLayer9 = MediaPlayer_PlayLayer9
        
    @property
    def MediaPlayer_PlayLayer(self):
        return self.__MediaPlayer_PlayLayer

    @MediaPlayer_PlayLayer.setter
    def MediaPlayer_PlayLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_PlayLayer__MediaPlayer_PlayLayer", None)
        self.__MediaPlayer_PlayLayer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaPlayer_MediaApi7"):
                    opp_val = getattr(item, "MediaPlayer_MediaApi7", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaPlayer_MediaApi7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaPlayer_MediaApi7"):
                    opp_val = getattr(item, "MediaPlayer_MediaApi7", None)
                    
                    setattr(item, "MediaPlayer_MediaApi7", self)
                    

    @property
    def MediaPlayer_PlayLayer9(self):
        return self.__MediaPlayer_PlayLayer9

    @MediaPlayer_PlayLayer9.setter
    def MediaPlayer_PlayLayer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_PlayLayer__MediaPlayer_PlayLayer9", None)
        self.__MediaPlayer_PlayLayer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_Library"):
                opp_val = getattr(old_value, "MediaPlayer_Library", None)
                if opp_val == self:
                    setattr(old_value, "MediaPlayer_Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_Library"):
                opp_val = getattr(value, "MediaPlayer_Library", None)
                setattr(value, "MediaPlayer_Library", self)

    def unregisterApi(self, unregisterMe: str):
        # TODO: Implement unregisterApi method
        pass

    def registerApi(self, addMe: str):
        # TODO: Implement registerApi method
        pass

class MediaPlayer_MediaApi(ABC):

    def __init__(self, MediaPlayer_MediaApi: set["MediaPlayer_MediaObject"] = None, MediaPlayer_MediaApi4: set["MediaPlayer_MediaObject"] = None, MediaPlayer_MediaApi7: "MediaPlayer_PlayLayer" = None):
        self.MediaPlayer_MediaApi = MediaPlayer_MediaApi if MediaPlayer_MediaApi is not None else set()
        self.MediaPlayer_MediaApi4 = MediaPlayer_MediaApi4 if MediaPlayer_MediaApi4 is not None else set()
        self.MediaPlayer_MediaApi7 = MediaPlayer_MediaApi7
        
    @property
    def MediaPlayer_MediaApi7(self):
        return self.__MediaPlayer_MediaApi7

    @MediaPlayer_MediaApi7.setter
    def MediaPlayer_MediaApi7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaApi__MediaPlayer_MediaApi7", None)
        self.__MediaPlayer_MediaApi7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_PlayLayer"):
                opp_val = getattr(old_value, "MediaPlayer_PlayLayer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_PlayLayer"):
                opp_val = getattr(value, "MediaPlayer_PlayLayer", None)
                if opp_val is None:
                    setattr(value, "MediaPlayer_PlayLayer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaPlayer_MediaApi(self):
        return self.__MediaPlayer_MediaApi

    @MediaPlayer_MediaApi.setter
    def MediaPlayer_MediaApi(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaApi__MediaPlayer_MediaApi", None)
        self.__MediaPlayer_MediaApi = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaPlayer_MediaObject2"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject2", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaPlayer_MediaObject2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaPlayer_MediaObject2"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject2", None)
                    
                    setattr(item, "MediaPlayer_MediaObject2", self)
                    

    @property
    def MediaPlayer_MediaApi4(self):
        return self.__MediaPlayer_MediaApi4

    @MediaPlayer_MediaApi4.setter
    def MediaPlayer_MediaApi4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaApi__MediaPlayer_MediaApi4", None)
        self.__MediaPlayer_MediaApi4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaPlayer_MediaObject5"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaPlayer_MediaObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaPlayer_MediaObject5"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject5", None)
                    
                    setattr(item, "MediaPlayer_MediaObject5", self)
                    

    def pause(self, pauseMe: str):
        # TODO: Implement pause method
        pass

    def stop(self, stopMe: str):
        # TODO: Implement stop method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def play(self, playMe: str):
        # TODO: Implement play method
        pass

    def canPlay(self, media: str) -> bool:
        # TODO: Implement canPlay method
        pass

    def dispose(self):
        # TODO: Implement dispose method
        pass

    def updateMediaObjectInfo(self, updateMe: str):
        # TODO: Implement updateMediaObjectInfo method
        pass

class BaseObject:

    pass
class MediaPlayer_MediaObject(BaseObject):

    def __init__(self, location: str, title: str, artist: str, year: int, state: str, album: str, MediaPlayer_MediaObject2: "MediaPlayer_MediaApi" = None, MediaPlayer_MediaObject5: "MediaPlayer_MediaApi" = None, MediaPlayer_MediaObject: "MediaPlayer_Playlist" = None, MediaPlayer_MediaObject12: "MediaPlayer_Library" = None):
        self.location = location
        self.title = title
        self.artist = artist
        self.year = year
        self.state = state
        self.album = album
        self.MediaPlayer_MediaObject2 = MediaPlayer_MediaObject2
        self.MediaPlayer_MediaObject5 = MediaPlayer_MediaObject5
        self.MediaPlayer_MediaObject = MediaPlayer_MediaObject
        self.MediaPlayer_MediaObject12 = MediaPlayer_MediaObject12
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def artist(self) -> str:
        return self.__artist

    @artist.setter
    def artist(self, artist: str):
        self.__artist = artist

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def album(self) -> str:
        return self.__album

    @album.setter
    def album(self, album: str):
        self.__album = album

    @property
    def MediaPlayer_MediaObject2(self):
        return self.__MediaPlayer_MediaObject2

    @MediaPlayer_MediaObject2.setter
    def MediaPlayer_MediaObject2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaObject__MediaPlayer_MediaObject2", None)
        self.__MediaPlayer_MediaObject2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_MediaApi"):
                opp_val = getattr(old_value, "MediaPlayer_MediaApi", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_MediaApi"):
                opp_val = getattr(value, "MediaPlayer_MediaApi", None)
                if opp_val is None:
                    setattr(value, "MediaPlayer_MediaApi", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaPlayer_MediaObject5(self):
        return self.__MediaPlayer_MediaObject5

    @MediaPlayer_MediaObject5.setter
    def MediaPlayer_MediaObject5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaObject__MediaPlayer_MediaObject5", None)
        self.__MediaPlayer_MediaObject5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_MediaApi4"):
                opp_val = getattr(old_value, "MediaPlayer_MediaApi4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_MediaApi4"):
                opp_val = getattr(value, "MediaPlayer_MediaApi4", None)
                if opp_val is None:
                    setattr(value, "MediaPlayer_MediaApi4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaPlayer_MediaObject(self):
        return self.__MediaPlayer_MediaObject

    @MediaPlayer_MediaObject.setter
    def MediaPlayer_MediaObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaObject__MediaPlayer_MediaObject", None)
        self.__MediaPlayer_MediaObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_Playlist"):
                opp_val = getattr(old_value, "MediaPlayer_Playlist", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_Playlist"):
                opp_val = getattr(value, "MediaPlayer_Playlist", None)
                if opp_val is None:
                    setattr(value, "MediaPlayer_Playlist", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaPlayer_MediaObject12(self):
        return self.__MediaPlayer_MediaObject12

    @MediaPlayer_MediaObject12.setter
    def MediaPlayer_MediaObject12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_MediaObject__MediaPlayer_MediaObject12", None)
        self.__MediaPlayer_MediaObject12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaPlayer_Library11"):
                opp_val = getattr(old_value, "MediaPlayer_Library11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaPlayer_Library11"):
                opp_val = getattr(value, "MediaPlayer_Library11", None)
                if opp_val is None:
                    setattr(value, "MediaPlayer_Library11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MediaPlayer_Library(BaseObject):

    pass
class MediaPlayer_Playlist(BaseObject):

    def __init__(self, name: str, repeat: bool, MediaPlayer_Playlist: set["MediaPlayer_MediaObject"] = None):
        self.name = name
        self.repeat = repeat
        self.MediaPlayer_Playlist = MediaPlayer_Playlist if MediaPlayer_Playlist is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def repeat(self) -> bool:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: bool):
        self.__repeat = repeat

    @property
    def MediaPlayer_Playlist(self):
        return self.__MediaPlayer_Playlist

    @MediaPlayer_Playlist.setter
    def MediaPlayer_Playlist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPlayer_Playlist__MediaPlayer_Playlist", None)
        self.__MediaPlayer_Playlist = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaPlayer_MediaObject"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaPlayer_MediaObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaPlayer_MediaObject"):
                    opp_val = getattr(item, "MediaPlayer_MediaObject", None)
                    
                    setattr(item, "MediaPlayer_MediaObject", self)
                    

    def shuffle(self):
        # TODO: Implement shuffle method
        pass

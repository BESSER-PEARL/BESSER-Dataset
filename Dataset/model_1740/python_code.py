from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SourceType(Enum):
    CD = "CD"
    CASSETTE = "CASSETTE"
    HDD = "HDD"
    OTHER = "OTHER"


############################################
# Definition of Classes
############################################

class MediaSource:

    pass
class MediaLibrary_Store(MediaSource):

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MediaLibrary_ExternalSource(MediaSource):

    def __init__(self, sourceType: str):
        self.sourceType = sourceType
        
    @property
    def sourceType(self) -> str:
        return self.__sourceType

    @sourceType.setter
    def sourceType(self, sourceType: str):
        self.__sourceType = sourceType

class DurationArtifact:

    pass
class MediaLibrary_MusicTrack(DurationArtifact):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class MediaLibrary_Video(DurationArtifact):

    def __init__(self, fps: str):
        self.fps = fps
        
    @property
    def fps(self) -> str:
        return self.__fps

    @fps.setter
    def fps(self, fps: str):
        self.__fps = fps

class MediaLibrary_AudioBook(DurationArtifact):

    def __init__(self, currentPosition: int):
        self.currentPosition = currentPosition
        
    @property
    def currentPosition(self) -> int:
        return self.__currentPosition

    @currentPosition.setter
    def currentPosition(self, currentPosition: int):
        self.__currentPosition = currentPosition

class Artifact:

    pass
class MediaLibrary_Image(Artifact):

    def __init__(self, dateTaken: str):
        self.dateTaken = dateTaken
        
    @property
    def dateTaken(self) -> str:
        return self.__dateTaken

    @dateTaken.setter
    def dateTaken(self, dateTaken: str):
        self.__dateTaken = dateTaken

class MediaLibrary_Ebook(Artifact):

    def __init__(self, pages: int):
        self.pages = pages
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

class MediaLibrary_DurationArtifact(Artifact):

    def __init__(self, duration: int):
        self.duration = duration
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class Device:

    pass
class MediaLibrary_Smartphone(Device):

    pass
class MediaLibrary_Computer(Device):

    pass
class MediaLibrary_EReader(Device):

    def __init__(self, videoEnabled: str, audioEnabled: str):
        self.videoEnabled = videoEnabled
        self.audioEnabled = audioEnabled
        
    @property
    def videoEnabled(self) -> str:
        return self.__videoEnabled

    @videoEnabled.setter
    def videoEnabled(self, videoEnabled: str):
        self.__videoEnabled = videoEnabled

    @property
    def audioEnabled(self) -> str:
        return self.__audioEnabled

    @audioEnabled.setter
    def audioEnabled(self, audioEnabled: str):
        self.__audioEnabled = audioEnabled

class MediaLibrary_Tablet(Device):

    pass
class MediaLibrary_MediaCollection:

    def __init__(self, name: str, collections: set["MediaLibrary_Device"] = None, MediaLibrary_MediaCollection: "MediaLibrary_Library" = None, MediaLibrary_MediaCollection10: set["MediaLibrary_Artifact"] = None, hostOf: "MediaLibrary_Device" = None, MediaCollection: "MediaLibrary_Device" = None, MediaCollection17: "MediaLibrary_Device" = None):
        self.name = name
        self.collections = collections if collections is not None else set()
        self.MediaLibrary_MediaCollection = MediaLibrary_MediaCollection
        self.MediaLibrary_MediaCollection10 = MediaLibrary_MediaCollection10 if MediaLibrary_MediaCollection10 is not None else set()
        self.hostOf = hostOf
        self.MediaCollection = MediaCollection
        self.MediaCollection17 = MediaCollection17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MediaCollection17(self):
        return self.__MediaCollection17

    @MediaCollection17.setter
    def MediaCollection17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__MediaCollection17", None)
        self.__MediaCollection17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syncedDevices"):
                opp_val = getattr(old_value, "syncedDevices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syncedDevices"):
                opp_val = getattr(value, "syncedDevices", None)
                if opp_val is None:
                    setattr(value, "syncedDevices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaLibrary_MediaCollection10(self):
        return self.__MediaLibrary_MediaCollection10

    @MediaLibrary_MediaCollection10.setter
    def MediaLibrary_MediaCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection10", None)
        self.__MediaLibrary_MediaCollection10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaLibrary_Artifact11"):
                    opp_val = getattr(item, "MediaLibrary_Artifact11", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaLibrary_Artifact11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaLibrary_Artifact11"):
                    opp_val = getattr(item, "MediaLibrary_Artifact11", None)
                    
                    setattr(item, "MediaLibrary_Artifact11", self)
                    

    @property
    def hostOf(self):
        return self.__hostOf

    @hostOf.setter
    def hostOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__hostOf", None)
        self.__hostOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Device"):
                opp_val = getattr(old_value, "Device", None)
                if opp_val == self:
                    setattr(old_value, "Device", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Device"):
                opp_val = getattr(value, "Device", None)
                setattr(value, "Device", self)

    @property
    def MediaCollection(self):
        return self.__MediaCollection

    @MediaCollection.setter
    def MediaCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__MediaCollection", None)
        self.__MediaCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "host"):
                opp_val = getattr(old_value, "host", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "host"):
                opp_val = getattr(value, "host", None)
                if opp_val is None:
                    setattr(value, "host", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaLibrary_MediaCollection(self):
        return self.__MediaLibrary_MediaCollection

    @MediaLibrary_MediaCollection.setter
    def MediaLibrary_MediaCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__MediaLibrary_MediaCollection", None)
        self.__MediaLibrary_MediaCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaLibrary_Library8"):
                opp_val = getattr(old_value, "MediaLibrary_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaLibrary_Library8"):
                opp_val = getattr(value, "MediaLibrary_Library8", None)
                if opp_val is None:
                    setattr(value, "MediaLibrary_Library8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def collections(self):
        return self.__collections

    @collections.setter
    def collections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_MediaCollection__collections", None)
        self.__collections = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device14"):
                    opp_val = getattr(item, "Device14", None)
                    
                    if opp_val == self:
                        setattr(item, "Device14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device14"):
                    opp_val = getattr(item, "Device14", None)
                    
                    setattr(item, "Device14", self)
                    

class MediaLibrary_Artifact(ABC):

    def __init__(self, author: str, name: str, MediaLibrary_Artifact: "MediaLibrary_Ecosystem" = None, MediaLibrary_Artifact11: "MediaLibrary_MediaCollection" = None, contents: "MediaLibrary_MediaSource" = None, Artifact: "MediaLibrary_MediaSource" = None):
        self.author = author
        self.name = name
        self.MediaLibrary_Artifact = MediaLibrary_Artifact
        self.MediaLibrary_Artifact11 = MediaLibrary_Artifact11
        self.contents = contents
        self.Artifact = Artifact
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def MediaLibrary_Artifact(self):
        return self.__MediaLibrary_Artifact

    @MediaLibrary_Artifact.setter
    def MediaLibrary_Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Artifact__MediaLibrary_Artifact", None)
        self.__MediaLibrary_Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaLibrary_Ecosystem6"):
                opp_val = getattr(old_value, "MediaLibrary_Ecosystem6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaLibrary_Ecosystem6"):
                opp_val = getattr(value, "MediaLibrary_Ecosystem6", None)
                if opp_val is None:
                    setattr(value, "MediaLibrary_Ecosystem6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MediaLibrary_Artifact11(self):
        return self.__MediaLibrary_Artifact11

    @MediaLibrary_Artifact11.setter
    def MediaLibrary_Artifact11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Artifact__MediaLibrary_Artifact11", None)
        self.__MediaLibrary_Artifact11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaLibrary_MediaCollection10"):
                opp_val = getattr(old_value, "MediaLibrary_MediaCollection10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaLibrary_MediaCollection10"):
                opp_val = getattr(value, "MediaLibrary_MediaCollection10", None)
                if opp_val is None:
                    setattr(value, "MediaLibrary_MediaCollection10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Artifact__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaSource"):
                opp_val = getattr(old_value, "MediaSource", None)
                if opp_val == self:
                    setattr(old_value, "MediaSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaSource"):
                opp_val = getattr(value, "MediaSource", None)
                setattr(value, "MediaSource", self)

    @property
    def Artifact(self):
        return self.__Artifact

    @Artifact.setter
    def Artifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Artifact__Artifact", None)
        self.__Artifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "origin"):
                opp_val = getattr(old_value, "origin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "origin"):
                opp_val = getattr(value, "origin", None)
                if opp_val is None:
                    setattr(value, "origin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MediaLibrary_MediaSource(ABC):

    pass
class MediaLibrary_Device(ABC):

    def __init__(self, MACAddress: str, resolutionWidth: int, resolutionHeight: int, MediaLibrary_Device: "MediaLibrary_Ecosystem" = None, Device: "MediaLibrary_MediaCollection" = None, Device14: "MediaLibrary_MediaCollection" = None, host: set["MediaLibrary_MediaCollection"] = None, syncedDevices: set["MediaLibrary_MediaCollection"] = None):
        self.MACAddress = MACAddress
        self.resolutionWidth = resolutionWidth
        self.resolutionHeight = resolutionHeight
        self.MediaLibrary_Device = MediaLibrary_Device
        self.Device = Device
        self.Device14 = Device14
        self.host = host if host is not None else set()
        self.syncedDevices = syncedDevices if syncedDevices is not None else set()
        
    @property
    def MACAddress(self) -> str:
        return self.__MACAddress

    @MACAddress.setter
    def MACAddress(self, MACAddress: str):
        self.__MACAddress = MACAddress

    @property
    def resolutionWidth(self) -> int:
        return self.__resolutionWidth

    @resolutionWidth.setter
    def resolutionWidth(self, resolutionWidth: int):
        self.__resolutionWidth = resolutionWidth

    @property
    def resolutionHeight(self) -> int:
        return self.__resolutionHeight

    @resolutionHeight.setter
    def resolutionHeight(self, resolutionHeight: int):
        self.__resolutionHeight = resolutionHeight

    @property
    def syncedDevices(self):
        return self.__syncedDevices

    @syncedDevices.setter
    def syncedDevices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Device__syncedDevices", None)
        self.__syncedDevices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaCollection17"):
                    opp_val = getattr(item, "MediaCollection17", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaCollection17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaCollection17"):
                    opp_val = getattr(item, "MediaCollection17", None)
                    
                    setattr(item, "MediaCollection17", self)
                    

    @property
    def Device14(self):
        return self.__Device14

    @Device14.setter
    def Device14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Device__Device14", None)
        self.__Device14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "collections"):
                opp_val = getattr(old_value, "collections", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "collections"):
                opp_val = getattr(value, "collections", None)
                if opp_val is None:
                    setattr(value, "collections", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Device(self):
        return self.__Device

    @Device.setter
    def Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Device__Device", None)
        self.__Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hostOf"):
                opp_val = getattr(old_value, "hostOf", None)
                if opp_val == self:
                    setattr(old_value, "hostOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hostOf"):
                opp_val = getattr(value, "hostOf", None)
                setattr(value, "hostOf", self)

    @property
    def MediaLibrary_Device(self):
        return self.__MediaLibrary_Device

    @MediaLibrary_Device.setter
    def MediaLibrary_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Device__MediaLibrary_Device", None)
        self.__MediaLibrary_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaLibrary_Ecosystem2"):
                opp_val = getattr(old_value, "MediaLibrary_Ecosystem2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaLibrary_Ecosystem2"):
                opp_val = getattr(value, "MediaLibrary_Ecosystem2", None)
                if opp_val is None:
                    setattr(value, "MediaLibrary_Ecosystem2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Device__host", None)
        self.__host = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaCollection"):
                    opp_val = getattr(item, "MediaCollection", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaCollection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaCollection"):
                    opp_val = getattr(item, "MediaCollection", None)
                    
                    setattr(item, "MediaCollection", self)
                    

class MediaLibrary_Library:

    def __init__(self, name: str, MediaLibrary_Library: "MediaLibrary_Ecosystem" = None, MediaLibrary_Library8: set["MediaLibrary_MediaCollection"] = None):
        self.name = name
        self.MediaLibrary_Library = MediaLibrary_Library
        self.MediaLibrary_Library8 = MediaLibrary_Library8 if MediaLibrary_Library8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MediaLibrary_Library8(self):
        return self.__MediaLibrary_Library8

    @MediaLibrary_Library8.setter
    def MediaLibrary_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Library__MediaLibrary_Library8", None)
        self.__MediaLibrary_Library8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaLibrary_MediaCollection"):
                    opp_val = getattr(item, "MediaLibrary_MediaCollection", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaLibrary_MediaCollection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaLibrary_MediaCollection"):
                    opp_val = getattr(item, "MediaLibrary_MediaCollection", None)
                    
                    setattr(item, "MediaLibrary_MediaCollection", self)
                    

    @property
    def MediaLibrary_Library(self):
        return self.__MediaLibrary_Library

    @MediaLibrary_Library.setter
    def MediaLibrary_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaLibrary_Library__MediaLibrary_Library", None)
        self.__MediaLibrary_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaLibrary_Ecosystem"):
                opp_val = getattr(old_value, "MediaLibrary_Ecosystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaLibrary_Ecosystem"):
                opp_val = getattr(value, "MediaLibrary_Ecosystem", None)
                if opp_val is None:
                    setattr(value, "MediaLibrary_Ecosystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MediaLibrary_Ecosystem:

    pass
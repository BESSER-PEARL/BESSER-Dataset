from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SourceType(Enum):
    HDD = "HDD"
    OTHER = "OTHER"
    CD = "CD"
    DVD = "DVD"
    VHS = "VHS"
    CASSETTE = "CASSETTE"


############################################
# Definition of Classes
############################################

class MediaSource:

    pass
class MediaLibrary_Store(MediaSource):

    pass
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

    pass
class MediaLibrary_Video(DurationArtifact):

    pass
class MediaLibrary_AudioBook(DurationArtifact):

    pass
class Artifact:

    pass
class MediaLibrary_Ebook(Artifact):

    pass
class MediaLibrary_Image(Artifact):

    pass
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
class NamedElement:

    pass
class MediaLibrary_MediaCollection(NamedElement):

    pass
class MediaLibrary_Artifact(NamedElement):

    pass
class MediaLibrary_MediaSource(NamedElement):

    pass
class MediaLibrary_Device(NamedElement):

    pass
class MediaLibrary_Library(NamedElement):

    pass
class MediaLibrary_Ecosystem:

    pass
class MediaLibrary_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

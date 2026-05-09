from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SourceType(Enum):
    CD = "CD"
    DVD = "DVD"
    VHS = "VHS"
    CASSETTE = "CASSETTE"
    HDD = "HDD"
    OTHER = "OTHER"


############################################
# Definition of Classes
############################################

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
class MediaLibrary_Image(Artifact):

    pass
class MediaLibrary_Ebook(Artifact):

    pass
class MediaLibrary_DurationArtifact(Artifact):

    def __init__(self, duration: int):
        self.duration = duration
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration


class MediaSource:

    pass
class MediaLibrary_Store(MediaSource):

    pass
class MediaLibrary_ExternalSource(MediaSource):

    def __init__(self, sourceType: str):
        self.sourceType = sourceType
        
        pass
    @property
    def sourceType(self):
        return self.__sourceType

    @sourceType.setter
    def sourceType(self, sourceType: str):
        self.__sourceType = sourceType


class NamedElement:

    pass
class MediaLibrary_Artifact(NamedElement):

    pass
class MediaLibrary_MediaCollection(NamedElement):

    pass
class MediaLibrary_MediaSource(NamedElement):

    pass
class MediaLibrary_Device(NamedElement):

    pass
class MediaLibrary_Library(NamedElement):

    pass
class MediaLibrary_Ecosystem:

    pass
class Device:

    pass
class MediaLibrary_Computer(Device):

    pass
class MediaLibrary_Smartphone(Device):

    pass
class MediaLibrary_EReader(Device):

    def __init__(self, videoEnabled: str, audioEnabled: str):
        self.videoEnabled = videoEnabled
        self.audioEnabled = audioEnabled
        
        pass
    @property
    def audioEnabled(self):
        return self.__audioEnabled

    @audioEnabled.setter
    def audioEnabled(self, audioEnabled: str):
        self.__audioEnabled = audioEnabled


    @property
    def videoEnabled(self):
        return self.__videoEnabled

    @videoEnabled.setter
    def videoEnabled(self, videoEnabled: str):
        self.__videoEnabled = videoEnabled


class MediaLibrary_Tablet(Device):

    pass
class MediaLibrary_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


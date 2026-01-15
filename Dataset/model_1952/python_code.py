from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MediaSourceType(Enum):
    ExternalArtifact = "ExternalArtifact"
    MediaStore = "MediaStore"
class DeviceType(Enum):
    Computer = "Computer"
    Smartphone = "Smartphone"
    Tablet = "Tablet"


############################################
# Definition of Classes
############################################

class MediaArtifact:

    pass
class mode_AudioBook(MediaArtifact):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class mode_Music(MediaArtifact):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class mode_EBook(MediaArtifact):

    pass
class mode_Video(MediaArtifact):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class mode_MediaCollection:

    def __init__(self, name: str, collection: set["mode_MediaArtifact"] = None, synchronisedCollections: set["mode_Device"] = None, ownedCollections: "mode_User" = None, MediaCollection10: "mode_MediaArtifact" = None, mode_MediaCollection: "mode_MediaLibrary" = None, MediaCollection: "mode_User" = None, MediaCollection12: "mode_Device" = None):
        self.name = name
        self.collection = collection if collection is not None else set()
        self.synchronisedCollections = synchronisedCollections if synchronisedCollections is not None else set()
        self.ownedCollections = ownedCollections
        self.MediaCollection10 = MediaCollection10
        self.mode_MediaCollection = mode_MediaCollection
        self.MediaCollection = MediaCollection
        self.MediaCollection12 = MediaCollection12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ownedCollections(self):
        return self.__ownedCollections

    @ownedCollections.setter
    def ownedCollections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__ownedCollections", None)
        self.__ownedCollections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User"):
                opp_val = getattr(old_value, "User", None)
                if opp_val == self:
                    setattr(old_value, "User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User"):
                opp_val = getattr(value, "User", None)
                setattr(value, "User", self)

    @property
    def MediaCollection10(self):
        return self.__MediaCollection10

    @MediaCollection10.setter
    def MediaCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__MediaCollection10", None)
        self.__MediaCollection10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mediaArtifacts"):
                opp_val = getattr(old_value, "mediaArtifacts", None)
                if opp_val == self:
                    setattr(old_value, "mediaArtifacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mediaArtifacts"):
                opp_val = getattr(value, "mediaArtifacts", None)
                setattr(value, "mediaArtifacts", self)

    @property
    def MediaCollection12(self):
        return self.__MediaCollection12

    @MediaCollection12.setter
    def MediaCollection12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__MediaCollection12", None)
        self.__MediaCollection12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synchronisedDevices"):
                opp_val = getattr(old_value, "synchronisedDevices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synchronisedDevices"):
                opp_val = getattr(value, "synchronisedDevices", None)
                if opp_val is None:
                    setattr(value, "synchronisedDevices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def synchronisedCollections(self):
        return self.__synchronisedCollections

    @synchronisedCollections.setter
    def synchronisedCollections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__synchronisedCollections", None)
        self.__synchronisedCollections = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Device"):
                    opp_val = getattr(item, "Device", None)
                    
                    if opp_val == self:
                        setattr(item, "Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Device"):
                    opp_val = getattr(item, "Device", None)
                    
                    setattr(item, "Device", self)
                    

    @property
    def MediaCollection(self):
        return self.__MediaCollection

    @MediaCollection.setter
    def MediaCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__MediaCollection", None)
        self.__MediaCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedUser"):
                opp_val = getattr(old_value, "ownedUser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedUser"):
                opp_val = getattr(value, "ownedUser", None)
                if opp_val is None:
                    setattr(value, "ownedUser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def collection(self):
        return self.__collection

    @collection.setter
    def collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__collection", None)
        self.__collection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaArtifact"):
                    opp_val = getattr(item, "MediaArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaArtifact"):
                    opp_val = getattr(item, "MediaArtifact", None)
                    
                    setattr(item, "MediaArtifact", self)
                    

    @property
    def mode_MediaCollection(self):
        return self.__mode_MediaCollection

    @mode_MediaCollection.setter
    def mode_MediaCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaCollection__mode_MediaCollection", None)
        self.__mode_MediaCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mode_MediaLibrary4"):
                opp_val = getattr(old_value, "mode_MediaLibrary4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mode_MediaLibrary4"):
                opp_val = getattr(value, "mode_MediaLibrary4", None)
                if opp_val is None:
                    setattr(value, "mode_MediaLibrary4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mode_User:

    def __init__(self, name: str, User: "mode_MediaCollection" = None, mode_User: "mode_MediaLibrary" = None, ownedUser: set["mode_MediaCollection"] = None):
        self.name = name
        self.User = User
        self.mode_User = mode_User
        self.ownedUser = ownedUser if ownedUser is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mode_User(self):
        return self.__mode_User

    @mode_User.setter
    def mode_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_User__mode_User", None)
        self.__mode_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mode_MediaLibrary2"):
                opp_val = getattr(old_value, "mode_MediaLibrary2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mode_MediaLibrary2"):
                opp_val = getattr(value, "mode_MediaLibrary2", None)
                if opp_val is None:
                    setattr(value, "mode_MediaLibrary2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def User(self):
        return self.__User

    @User.setter
    def User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_User__User", None)
        self.__User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedCollections"):
                opp_val = getattr(old_value, "ownedCollections", None)
                if opp_val == self:
                    setattr(old_value, "ownedCollections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedCollections"):
                opp_val = getattr(value, "ownedCollections", None)
                setattr(value, "ownedCollections", self)

    @property
    def ownedUser(self):
        return self.__ownedUser

    @ownedUser.setter
    def ownedUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_User__ownedUser", None)
        self.__ownedUser = value if value is not None else set()
        
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
                    

class mode_Device:

    def __init__(self, name: str, type: str, Device: "mode_MediaCollection" = None, mode_Device: "mode_MediaLibrary" = None, synchronisedDevices: set["mode_MediaCollection"] = None):
        self.name = name
        self.type = type
        self.Device = Device
        self.mode_Device = mode_Device
        self.synchronisedDevices = synchronisedDevices if synchronisedDevices is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def synchronisedDevices(self):
        return self.__synchronisedDevices

    @synchronisedDevices.setter
    def synchronisedDevices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_Device__synchronisedDevices", None)
        self.__synchronisedDevices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MediaCollection12"):
                    opp_val = getattr(item, "MediaCollection12", None)
                    
                    if opp_val == self:
                        setattr(item, "MediaCollection12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MediaCollection12"):
                    opp_val = getattr(item, "MediaCollection12", None)
                    
                    setattr(item, "MediaCollection12", self)
                    

    @property
    def Device(self):
        return self.__Device

    @Device.setter
    def Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_Device__Device", None)
        self.__Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "synchronisedCollections"):
                opp_val = getattr(old_value, "synchronisedCollections", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "synchronisedCollections"):
                opp_val = getattr(value, "synchronisedCollections", None)
                if opp_val is None:
                    setattr(value, "synchronisedCollections", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mode_Device(self):
        return self.__mode_Device

    @mode_Device.setter
    def mode_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_Device__mode_Device", None)
        self.__mode_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mode_MediaLibrary"):
                opp_val = getattr(old_value, "mode_MediaLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mode_MediaLibrary"):
                opp_val = getattr(value, "mode_MediaLibrary", None)
                if opp_val is None:
                    setattr(value, "mode_MediaLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mode_MediaArtifact(ABC):

    def __init__(self, identifier: str, name: str, source: str, MediaArtifact: "mode_MediaCollection" = None, mediaArtifacts: "mode_MediaCollection" = None):
        self.identifier = identifier
        self.name = name
        self.source = source
        self.MediaArtifact = MediaArtifact
        self.mediaArtifacts = mediaArtifacts
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mediaArtifacts(self):
        return self.__mediaArtifacts

    @mediaArtifacts.setter
    def mediaArtifacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaArtifact__mediaArtifacts", None)
        self.__mediaArtifacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaCollection10"):
                opp_val = getattr(old_value, "MediaCollection10", None)
                if opp_val == self:
                    setattr(old_value, "MediaCollection10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaCollection10"):
                opp_val = getattr(value, "MediaCollection10", None)
                setattr(value, "MediaCollection10", self)

    @property
    def MediaArtifact(self):
        return self.__MediaArtifact

    @MediaArtifact.setter
    def MediaArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mode_MediaArtifact__MediaArtifact", None)
        self.__MediaArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "collection"):
                opp_val = getattr(old_value, "collection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "collection"):
                opp_val = getattr(value, "collection", None)
                if opp_val is None:
                    setattr(value, "collection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mode_MediaLibrary:

    pass
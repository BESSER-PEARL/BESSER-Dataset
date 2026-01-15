from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DAAP_COMM_CST(Enum):
    MAX_USER_CONNECTIONS_PER_SESSION = "MAX_USER_CONNECTIONS_PER_SESSION"
    MAX_USER_SIMULTANEOUS_CONNECTION = "MAX_USER_SIMULTANEOUS_CONNECTION"
    MAX_SIMULTATNEOUS_CONNECTIONS = "MAX_SIMULTATNEOUS_CONNECTIONS"
class DAAP_CONNECTION_KIND(Enum):
    USER = "USER"
    DB = "DB"


############################################
# Definition of Classes
############################################

class ezdaap_EZDaapIntelPropertyElem:

    def __init__(self, license: str, ezdaap_EZDaapIntelPropertyElem: set["ezdaap_EZDaapArtist"] = None):
        self.license = license
        self.ezdaap_EZDaapIntelPropertyElem = ezdaap_EZDaapIntelPropertyElem if ezdaap_EZDaapIntelPropertyElem is not None else set()
        
    @property
    def license(self) -> str:
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license

    @property
    def ezdaap_EZDaapIntelPropertyElem(self):
        return self.__ezdaap_EZDaapIntelPropertyElem

    @ezdaap_EZDaapIntelPropertyElem.setter
    def ezdaap_EZDaapIntelPropertyElem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapIntelPropertyElem__ezdaap_EZDaapIntelPropertyElem", None)
        self.__ezdaap_EZDaapIntelPropertyElem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapArtist20"):
                    opp_val = getattr(item, "ezdaap_EZDaapArtist20", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapArtist20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapArtist20"):
                    opp_val = getattr(item, "ezdaap_EZDaapArtist20", None)
                    
                    setattr(item, "ezdaap_EZDaapArtist20", self)
                    

class EZDaapLibraryUnit:

    pass
class ezdaap_EZDaapElem(EZDaapLibraryUnit):

    pass
class ezdaap_EZDaapLibraryUnit(ABC):

    def __init__(self, name: str, ezdaap_EZDaapLibraryUnit: "ezdaap_EZDaapLibrary" = None):
        self.name = name
        self.ezdaap_EZDaapLibraryUnit = ezdaap_EZDaapLibraryUnit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ezdaap_EZDaapLibraryUnit(self):
        return self.__ezdaap_EZDaapLibraryUnit

    @ezdaap_EZDaapLibraryUnit.setter
    def ezdaap_EZDaapLibraryUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapLibraryUnit__ezdaap_EZDaapLibraryUnit", None)
        self.__ezdaap_EZDaapLibraryUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ezdaap_EZDaapLibrary18"):
                opp_val = getattr(old_value, "ezdaap_EZDaapLibrary18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ezdaap_EZDaapLibrary18"):
                opp_val = getattr(value, "ezdaap_EZDaapLibrary18", None)
                if opp_val is None:
                    setattr(value, "ezdaap_EZDaapLibrary18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EZDaapIntelPropertyElem:

    pass
class EZDaapElem:

    pass
class ezdaap_EZDaapManager:

    pass
class ezdaap_EZDaapDictionary:

    pass
class ezdaap_EZDaapSong(EZDaapIntelPropertyElem, EZDaapElem):

    pass
class ezdaap_EZDaapPlayList(EZDaapElem):

    pass
class ezdaap_EZDaapLibrary(EZDaapLibraryUnit):

    pass
class ezdaap_EZDaapITunesInstance:

    def __init__(self, revID: int, id: str, sessionID: int, serverName: str, ezdaap_EZDaapITunesInstance6: set["ezdaap_EZDaapAlbum"] = None, ezdaap_EZDaapITunesInstance8: set["ezdaap_EZDaapArtist"] = None, ezdaap_EZDaapITunesInstance: set["ezdaap_EZDaapLibrary"] = None, ezdaap_EZDaapITunesInstance2: set["ezdaap_EZDaapPlayList"] = None, ezdaap_EZDaapITunesInstance4: set["ezdaap_EZDaapSong"] = None, ezdaap_EZDaapITunesInstance10: "ezdaap_EZDaapManager" = None):
        self.revID = revID
        self.id = id
        self.sessionID = sessionID
        self.serverName = serverName
        self.ezdaap_EZDaapITunesInstance6 = ezdaap_EZDaapITunesInstance6 if ezdaap_EZDaapITunesInstance6 is not None else set()
        self.ezdaap_EZDaapITunesInstance8 = ezdaap_EZDaapITunesInstance8 if ezdaap_EZDaapITunesInstance8 is not None else set()
        self.ezdaap_EZDaapITunesInstance = ezdaap_EZDaapITunesInstance if ezdaap_EZDaapITunesInstance is not None else set()
        self.ezdaap_EZDaapITunesInstance2 = ezdaap_EZDaapITunesInstance2 if ezdaap_EZDaapITunesInstance2 is not None else set()
        self.ezdaap_EZDaapITunesInstance4 = ezdaap_EZDaapITunesInstance4 if ezdaap_EZDaapITunesInstance4 is not None else set()
        self.ezdaap_EZDaapITunesInstance10 = ezdaap_EZDaapITunesInstance10
        
    @property
    def revID(self) -> int:
        return self.__revID

    @revID.setter
    def revID(self, revID: int):
        self.__revID = revID

    @property
    def sessionID(self) -> int:
        return self.__sessionID

    @sessionID.setter
    def sessionID(self, sessionID: int):
        self.__sessionID = sessionID

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def serverName(self) -> str:
        return self.__serverName

    @serverName.setter
    def serverName(self, serverName: str):
        self.__serverName = serverName

    @property
    def ezdaap_EZDaapITunesInstance8(self):
        return self.__ezdaap_EZDaapITunesInstance8

    @ezdaap_EZDaapITunesInstance8.setter
    def ezdaap_EZDaapITunesInstance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance8", None)
        self.__ezdaap_EZDaapITunesInstance8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapArtist"):
                    opp_val = getattr(item, "ezdaap_EZDaapArtist", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapArtist", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapArtist"):
                    opp_val = getattr(item, "ezdaap_EZDaapArtist", None)
                    
                    setattr(item, "ezdaap_EZDaapArtist", self)
                    

    @property
    def ezdaap_EZDaapITunesInstance2(self):
        return self.__ezdaap_EZDaapITunesInstance2

    @ezdaap_EZDaapITunesInstance2.setter
    def ezdaap_EZDaapITunesInstance2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance2", None)
        self.__ezdaap_EZDaapITunesInstance2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapPlayList"):
                    opp_val = getattr(item, "ezdaap_EZDaapPlayList", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapPlayList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapPlayList"):
                    opp_val = getattr(item, "ezdaap_EZDaapPlayList", None)
                    
                    setattr(item, "ezdaap_EZDaapPlayList", self)
                    

    @property
    def ezdaap_EZDaapITunesInstance4(self):
        return self.__ezdaap_EZDaapITunesInstance4

    @ezdaap_EZDaapITunesInstance4.setter
    def ezdaap_EZDaapITunesInstance4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance4", None)
        self.__ezdaap_EZDaapITunesInstance4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapSong"):
                    opp_val = getattr(item, "ezdaap_EZDaapSong", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapSong", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapSong"):
                    opp_val = getattr(item, "ezdaap_EZDaapSong", None)
                    
                    setattr(item, "ezdaap_EZDaapSong", self)
                    

    @property
    def ezdaap_EZDaapITunesInstance10(self):
        return self.__ezdaap_EZDaapITunesInstance10

    @ezdaap_EZDaapITunesInstance10.setter
    def ezdaap_EZDaapITunesInstance10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance10", None)
        self.__ezdaap_EZDaapITunesInstance10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ezdaap_EZDaapManager"):
                opp_val = getattr(old_value, "ezdaap_EZDaapManager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ezdaap_EZDaapManager"):
                opp_val = getattr(value, "ezdaap_EZDaapManager", None)
                if opp_val is None:
                    setattr(value, "ezdaap_EZDaapManager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ezdaap_EZDaapITunesInstance(self):
        return self.__ezdaap_EZDaapITunesInstance

    @ezdaap_EZDaapITunesInstance.setter
    def ezdaap_EZDaapITunesInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance", None)
        self.__ezdaap_EZDaapITunesInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapLibrary"):
                    opp_val = getattr(item, "ezdaap_EZDaapLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapLibrary"):
                    opp_val = getattr(item, "ezdaap_EZDaapLibrary", None)
                    
                    setattr(item, "ezdaap_EZDaapLibrary", self)
                    

    @property
    def ezdaap_EZDaapITunesInstance6(self):
        return self.__ezdaap_EZDaapITunesInstance6

    @ezdaap_EZDaapITunesInstance6.setter
    def ezdaap_EZDaapITunesInstance6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ezdaap_EZDaapITunesInstance__ezdaap_EZDaapITunesInstance6", None)
        self.__ezdaap_EZDaapITunesInstance6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ezdaap_EZDaapAlbum"):
                    opp_val = getattr(item, "ezdaap_EZDaapAlbum", None)
                    
                    if opp_val == self:
                        setattr(item, "ezdaap_EZDaapAlbum", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ezdaap_EZDaapAlbum"):
                    opp_val = getattr(item, "ezdaap_EZDaapAlbum", None)
                    
                    setattr(item, "ezdaap_EZDaapAlbum", self)
                    

class ezdaap_EZDaapArtist:

    pass
class ezdaap_EZDaapAlbum(EZDaapIntelPropertyElem, EZDaapElem):

    pass
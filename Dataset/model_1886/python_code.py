from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class JSFVersion(Enum):
    UNKNOWN = "UNKNOWN"
    v1_1 = "v1_1"
    v1_2 = "v1_2"


############################################
# Definition of Classes
############################################

class JSFLibrary:

    pass
class jsflibraryregistry_JSFLibrary:

    def __init__(self, ID: str, Name: str, JSFVersion: str, Deployed: bool, Implementation: bool, JSFLibrary: set["jsflibraryregistry_ArchiveFile"] = None, jsflibraryregistry_JSFLibrary: "jsflibraryregistry_JSFLibraryRegistry" = None, JSFLibrary5: "jsflibraryregistry_ArchiveFile" = None):
        self.ID = ID
        self.Name = Name
        self.JSFVersion = JSFVersion
        self.Deployed = Deployed
        self.Implementation = Implementation
        self.JSFLibrary = JSFLibrary if JSFLibrary is not None else set()
        self.jsflibraryregistry_JSFLibrary = jsflibraryregistry_JSFLibrary
        self.JSFLibrary5 = JSFLibrary5
        
    @property
    def JSFVersion(self) -> str:
        return self.__JSFVersion

    @JSFVersion.setter
    def JSFVersion(self, JSFVersion: str):
        self.__JSFVersion = JSFVersion

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Implementation(self) -> bool:
        return self.__Implementation

    @Implementation.setter
    def Implementation(self, Implementation: bool):
        self.__Implementation = Implementation

    @property
    def Deployed(self) -> bool:
        return self.__Deployed

    @Deployed.setter
    def Deployed(self, Deployed: bool):
        self.__Deployed = Deployed

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def JSFLibrary5(self):
        return self.__JSFLibrary5

    @JSFLibrary5.setter
    def JSFLibrary5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_JSFLibrary__JSFLibrary5", None)
        self.__JSFLibrary5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArchiveFiles"):
                opp_val = getattr(old_value, "ArchiveFiles", None)
                if opp_val == self:
                    setattr(old_value, "ArchiveFiles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArchiveFiles"):
                opp_val = getattr(value, "ArchiveFiles", None)
                setattr(value, "ArchiveFiles", self)

    @property
    def JSFLibrary(self):
        return self.__JSFLibrary

    @JSFLibrary.setter
    def JSFLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_JSFLibrary__JSFLibrary", None)
        self.__JSFLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArchiveFile"):
                    opp_val = getattr(item, "ArchiveFile", None)
                    
                    if opp_val == self:
                        setattr(item, "ArchiveFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArchiveFile"):
                    opp_val = getattr(item, "ArchiveFile", None)
                    
                    setattr(item, "ArchiveFile", self)
                    

    @property
    def jsflibraryregistry_JSFLibrary(self):
        return self.__jsflibraryregistry_JSFLibrary

    @jsflibraryregistry_JSFLibrary.setter
    def jsflibraryregistry_JSFLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_JSFLibrary__jsflibraryregistry_JSFLibrary", None)
        self.__jsflibraryregistry_JSFLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsflibraryregistry_JSFLibraryRegistry"):
                opp_val = getattr(old_value, "jsflibraryregistry_JSFLibraryRegistry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsflibraryregistry_JSFLibraryRegistry"):
                opp_val = getattr(value, "jsflibraryregistry_JSFLibraryRegistry", None)
                if opp_val is None:
                    setattr(value, "jsflibraryregistry_JSFLibraryRegistry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

    def copyTo(self, baseDestLocation: str) -> bool:
        # TODO: Implement copyTo method
        pass

    def containsArchiveFile(self, fullPath: str) -> bool:
        # TODO: Implement containsArchiveFile method
        pass

    def getWorkingCopy(self) -> str:
        # TODO: Implement getWorkingCopy method
        pass

    def updateValues(self, otherLibrary: str):
        # TODO: Implement updateValues method
        pass

class jsflibraryregistry_ArchiveFile:

    def __init__(self, RelativeToWorkspace: bool, SourceLocation: str, RelativeDestLocation: str, ArchiveFile: "jsflibraryregistry_JSFLibrary" = None, ArchiveFiles: "jsflibraryregistry_JSFLibrary" = None):
        self.RelativeToWorkspace = RelativeToWorkspace
        self.SourceLocation = SourceLocation
        self.RelativeDestLocation = RelativeDestLocation
        self.ArchiveFile = ArchiveFile
        self.ArchiveFiles = ArchiveFiles
        
    @property
    def SourceLocation(self) -> str:
        return self.__SourceLocation

    @SourceLocation.setter
    def SourceLocation(self, SourceLocation: str):
        self.__SourceLocation = SourceLocation

    @property
    def RelativeDestLocation(self) -> str:
        return self.__RelativeDestLocation

    @RelativeDestLocation.setter
    def RelativeDestLocation(self, RelativeDestLocation: str):
        self.__RelativeDestLocation = RelativeDestLocation

    @property
    def RelativeToWorkspace(self) -> bool:
        return self.__RelativeToWorkspace

    @RelativeToWorkspace.setter
    def RelativeToWorkspace(self, RelativeToWorkspace: bool):
        self.__RelativeToWorkspace = RelativeToWorkspace

    @property
    def ArchiveFiles(self):
        return self.__ArchiveFiles

    @ArchiveFiles.setter
    def ArchiveFiles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_ArchiveFile__ArchiveFiles", None)
        self.__ArchiveFiles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JSFLibrary5"):
                opp_val = getattr(old_value, "JSFLibrary5", None)
                if opp_val == self:
                    setattr(old_value, "JSFLibrary5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JSFLibrary5"):
                opp_val = getattr(value, "JSFLibrary5", None)
                setattr(value, "JSFLibrary5", self)

    @property
    def ArchiveFile(self):
        return self.__ArchiveFile

    @ArchiveFile.setter
    def ArchiveFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_ArchiveFile__ArchiveFile", None)
        self.__ArchiveFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JSFLibrary"):
                opp_val = getattr(old_value, "JSFLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JSFLibrary"):
                opp_val = getattr(value, "JSFLibrary", None)
                if opp_val is None:
                    setattr(value, "JSFLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def exists(self) -> bool:
        # TODO: Implement exists method
        pass

    def hashCode(self) -> int:
        # TODO: Implement hashCode method
        pass

    def getResolvedSourceLocation(self) -> str:
        # TODO: Implement getResolvedSourceLocation method
        pass

    def getPath(self) -> str:
        # TODO: Implement getPath method
        pass

    def getName(self) -> str:
        # TODO: Implement getName method
        pass

    def copyTo(self, baseDestLocation: str) -> bool:
        # TODO: Implement copyTo method
        pass

    def equals(self, object: str) -> bool:
        # TODO: Implement equals method
        pass

class jsflibraryregistry_PluginProvidedJSFLibrary(JSFLibrary):

    def __init__(self, pluginID: str, Label: str, jsflibraryregistry_PluginProvidedJSFLibrary: "jsflibraryregistry_JSFLibraryRegistry" = None):
        self.pluginID = pluginID
        self.Label = Label
        self.jsflibraryregistry_PluginProvidedJSFLibrary = jsflibraryregistry_PluginProvidedJSFLibrary
        
    @property
    def Label(self) -> str:
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label

    @property
    def pluginID(self) -> str:
        return self.__pluginID

    @pluginID.setter
    def pluginID(self, pluginID: str):
        self.__pluginID = pluginID

    @property
    def jsflibraryregistry_PluginProvidedJSFLibrary(self):
        return self.__jsflibraryregistry_PluginProvidedJSFLibrary

    @jsflibraryregistry_PluginProvidedJSFLibrary.setter
    def jsflibraryregistry_PluginProvidedJSFLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_PluginProvidedJSFLibrary__jsflibraryregistry_PluginProvidedJSFLibrary", None)
        self.__jsflibraryregistry_PluginProvidedJSFLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jsflibraryregistry_JSFLibraryRegistry2"):
                opp_val = getattr(old_value, "jsflibraryregistry_JSFLibraryRegistry2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jsflibraryregistry_JSFLibraryRegistry2"):
                opp_val = getattr(value, "jsflibraryregistry_JSFLibraryRegistry2", None)
                if opp_val is None:
                    setattr(value, "jsflibraryregistry_JSFLibraryRegistry2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jsflibraryregistry_JSFLibraryRegistry:

    def __init__(self, DefaultImplementationID: str, jsflibraryregistry_JSFLibraryRegistry2: set["jsflibraryregistry_PluginProvidedJSFLibrary"] = None, jsflibraryregistry_JSFLibraryRegistry: set["jsflibraryregistry_JSFLibrary"] = None):
        self.DefaultImplementationID = DefaultImplementationID
        self.jsflibraryregistry_JSFLibraryRegistry2 = jsflibraryregistry_JSFLibraryRegistry2 if jsflibraryregistry_JSFLibraryRegistry2 is not None else set()
        self.jsflibraryregistry_JSFLibraryRegistry = jsflibraryregistry_JSFLibraryRegistry if jsflibraryregistry_JSFLibraryRegistry is not None else set()
        
    @property
    def DefaultImplementationID(self) -> str:
        return self.__DefaultImplementationID

    @DefaultImplementationID.setter
    def DefaultImplementationID(self, DefaultImplementationID: str):
        self.__DefaultImplementationID = DefaultImplementationID

    @property
    def jsflibraryregistry_JSFLibraryRegistry(self):
        return self.__jsflibraryregistry_JSFLibraryRegistry

    @jsflibraryregistry_JSFLibraryRegistry.setter
    def jsflibraryregistry_JSFLibraryRegistry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_JSFLibraryRegistry__jsflibraryregistry_JSFLibraryRegistry", None)
        self.__jsflibraryregistry_JSFLibraryRegistry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jsflibraryregistry_JSFLibrary"):
                    opp_val = getattr(item, "jsflibraryregistry_JSFLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "jsflibraryregistry_JSFLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jsflibraryregistry_JSFLibrary"):
                    opp_val = getattr(item, "jsflibraryregistry_JSFLibrary", None)
                    
                    setattr(item, "jsflibraryregistry_JSFLibrary", self)
                    

    @property
    def jsflibraryregistry_JSFLibraryRegistry2(self):
        return self.__jsflibraryregistry_JSFLibraryRegistry2

    @jsflibraryregistry_JSFLibraryRegistry2.setter
    def jsflibraryregistry_JSFLibraryRegistry2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jsflibraryregistry_JSFLibraryRegistry__jsflibraryregistry_JSFLibraryRegistry2", None)
        self.__jsflibraryregistry_JSFLibraryRegistry2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary"):
                    opp_val = getattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary"):
                    opp_val = getattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary", None)
                    
                    setattr(item, "jsflibraryregistry_PluginProvidedJSFLibrary", self)
                    

    def getNonImplJSFLibraries(self) -> str:
        # TODO: Implement getNonImplJSFLibraries method
        pass

    def getAllJSFLibraries(self) -> str:
        # TODO: Implement getAllJSFLibraries method
        pass

    def getImplJSFLibraries(self) -> str:
        # TODO: Implement getImplJSFLibraries method
        pass

    def addJSFLibrary(self, library: str) -> bool:
        # TODO: Implement addJSFLibrary method
        pass

    def getJSFLibrariesByName(self, name: str) -> str:
        # TODO: Implement getJSFLibrariesByName method
        pass

    def getJSFLibraryByID(self, ID: str) -> str:
        # TODO: Implement getJSFLibraryByID method
        pass

    def getDefaultImplementation(self) -> str:
        # TODO: Implement getDefaultImplementation method
        pass

    def setDefaultImplementation(self, implementation: str):
        # TODO: Implement setDefaultImplementation method
        pass

    def removeJSFLibrary(self, library: str) -> bool:
        # TODO: Implement removeJSFLibrary method
        pass

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
class jsflibraryregistry_ArchiveFile:

    def __init__(self, RelativeToWorkspace: bool, SourceLocation: str, RelativeDestLocation: str, ArchiveFile: "jsflibraryregistry_JSFLibrary" = None, ArchiveFiles: "jsflibraryregistry_JSFLibrary" = None):
        self.RelativeToWorkspace = RelativeToWorkspace
        self.SourceLocation = SourceLocation
        self.RelativeDestLocation = RelativeDestLocation
        self.ArchiveFile = ArchiveFile
        self.ArchiveFiles = ArchiveFiles
        
        pass
    @property
    def SourceLocation(self):
        return self.__SourceLocation

    @SourceLocation.setter
    def SourceLocation(self, SourceLocation: str):
        self.__SourceLocation = SourceLocation


    @property
    def RelativeToWorkspace(self):
        return self.__RelativeToWorkspace

    @RelativeToWorkspace.setter
    def RelativeToWorkspace(self, RelativeToWorkspace: bool):
        self.__RelativeToWorkspace = RelativeToWorkspace


    @property
    def RelativeDestLocation(self):
        return self.__RelativeDestLocation

    @RelativeDestLocation.setter
    def RelativeDestLocation(self, RelativeDestLocation: str):
        self.__RelativeDestLocation = RelativeDestLocation


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

    def getResolvedSourceLocation(self) :
        # TODO: Implement getResolvedSourceLocation method
        pass

    def getName(self) :
        # TODO: Implement getName method
        pass

    def copyTo(self, jsflibraryregistry_baseDestLocation) :
        # TODO: Implement copyTo method
        pass

    def hashCode(self) :
        # TODO: Implement hashCode method
        pass

    def exists(self) :
        # TODO: Implement exists method
        pass

    def equals(self, jsflibraryregistry_object) :
        # TODO: Implement equals method
        pass

    def getPath(self) :
        # TODO: Implement getPath method
        pass

class jsflibraryregistry_PluginProvidedJSFLibrary(JSFLibrary):

    def __init__(self, pluginID: str, Label: str, jsflibraryregistry_PluginProvidedJSFLibrary: "jsflibraryregistry_JSFLibraryRegistry" = None):
        self.pluginID = pluginID
        self.Label = Label
        self.jsflibraryregistry_PluginProvidedJSFLibrary = jsflibraryregistry_PluginProvidedJSFLibrary
        
        pass
    @property
    def pluginID(self):
        return self.__pluginID

    @pluginID.setter
    def pluginID(self, pluginID: str):
        self.__pluginID = pluginID


    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label


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

class jsflibraryregistry_JSFLibrary:

    def __init__(self, ID: str, Name: str, JSFVersion: str, Deployed: bool, Implementation: bool, jsflibraryregistry_JSFLibrary: "jsflibraryregistry_JSFLibraryRegistry" = None, JSFLibrary: set["jsflibraryregistry_ArchiveFile"] = None, JSFLibrary5: "jsflibraryregistry_ArchiveFile" = None):
        self.ID = ID
        self.Name = Name
        self.JSFVersion = JSFVersion
        self.Deployed = Deployed
        self.Implementation = Implementation
        self.jsflibraryregistry_JSFLibrary = jsflibraryregistry_JSFLibrary
        self.JSFLibrary = JSFLibrary if JSFLibrary is not None else set()
        self.JSFLibrary5 = JSFLibrary5
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def Implementation(self):
        return self.__Implementation

    @Implementation.setter
    def Implementation(self, Implementation: bool):
        self.__Implementation = Implementation


    @property
    def Deployed(self):
        return self.__Deployed

    @Deployed.setter
    def Deployed(self, Deployed: bool):
        self.__Deployed = Deployed


    @property
    def JSFVersion(self):
        return self.__JSFVersion

    @JSFVersion.setter
    def JSFVersion(self, JSFVersion: str):
        self.__JSFVersion = JSFVersion


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

    def updateValues(self, jsflibraryregistry_otherLibrary):
        # TODO: Implement updateValues method
        pass

    def containsArchiveFile(self, jsflibraryregistry_fullPath) :
        # TODO: Implement containsArchiveFile method
        pass

    def copyTo(self, jsflibraryregistry_baseDestLocation) :
        # TODO: Implement copyTo method
        pass

    def getWorkingCopy(self) :
        # TODO: Implement getWorkingCopy method
        pass

    def getLabel(self) :
        # TODO: Implement getLabel method
        pass

class jsflibraryregistry_JSFLibraryRegistry:

    def __init__(self, DefaultImplementationID: str, jsflibraryregistry_JSFLibraryRegistry: set["jsflibraryregistry_JSFLibrary"] = None, jsflibraryregistry_JSFLibraryRegistry2: set["jsflibraryregistry_PluginProvidedJSFLibrary"] = None):
        self.DefaultImplementationID = DefaultImplementationID
        self.jsflibraryregistry_JSFLibraryRegistry = jsflibraryregistry_JSFLibraryRegistry if jsflibraryregistry_JSFLibraryRegistry is not None else set()
        self.jsflibraryregistry_JSFLibraryRegistry2 = jsflibraryregistry_JSFLibraryRegistry2 if jsflibraryregistry_JSFLibraryRegistry2 is not None else set()
        
        pass
    @property
    def DefaultImplementationID(self):
        return self.__DefaultImplementationID

    @DefaultImplementationID.setter
    def DefaultImplementationID(self, DefaultImplementationID: str):
        self.__DefaultImplementationID = DefaultImplementationID


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
                    

    def getImplJSFLibraries(self) :
        # TODO: Implement getImplJSFLibraries method
        pass

    def getJSFLibrariesByName(self, jsflibraryregistry_name) :
        # TODO: Implement getJSFLibrariesByName method
        pass

    def setDefaultImplementation(self, jsflibraryregistry_implementation):
        # TODO: Implement setDefaultImplementation method
        pass

    def addJSFLibrary(self, jsflibraryregistry_library) :
        # TODO: Implement addJSFLibrary method
        pass

    def removeJSFLibrary(self, jsflibraryregistry_library) :
        # TODO: Implement removeJSFLibrary method
        pass

    def getJSFLibraryByID(self, jsflibraryregistry_ID) :
        # TODO: Implement getJSFLibraryByID method
        pass

    def getNonImplJSFLibraries(self) :
        # TODO: Implement getNonImplJSFLibraries method
        pass

    def getAllJSFLibraries(self) :
        # TODO: Implement getAllJSFLibraries method
        pass

    def getDefaultImplementation(self) :
        # TODO: Implement getDefaultImplementation method
        pass

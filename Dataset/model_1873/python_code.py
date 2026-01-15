from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LibrarySourceType(Enum):
    ZipFile = "ZipFile"
    Folder = "Folder"
    JavascriptFile = "JavascriptFile"


############################################
# Definition of Classes
############################################

class basic_CoreVersionDefault:

    def __init__(self, version: str, facet: str, coreLib: str):
        self.version = version
        self.facet = facet
        self.coreLib = coreLib
        
    @property
    def coreLib(self) -> str:
        return self.__coreLib

    @coreLib.setter
    def coreLib(self, coreLib: str):
        self.__coreLib = coreLib

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def facet(self) -> str:
        return self.__facet

    @facet.setter
    def facet(self, facet: str):
        self.__facet = facet

class basic_Parameter:

    def __init__(self, description: str, name: str, type: str, basic_Parameter: "basic_Event" = None):
        self.description = description
        self.name = name
        self.type = type
        self.basic_Parameter = basic_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def basic_Parameter(self):
        return self.__basic_Parameter

    @basic_Parameter.setter
    def basic_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Parameter__basic_Parameter", None)
        self.__basic_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_Event"):
                opp_val = getattr(old_value, "basic_Event", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_Event"):
                opp_val = getattr(value, "basic_Event", None)
                if opp_val is None:
                    setattr(value, "basic_Event", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basic_LibrarySource:

    def __init__(self, type: str, path: str, inclusions: str, exclusions: str, basic_LibrarySource: "basic_Library" = None, basic_LibrarySource6: set["basic_File"] = None):
        self.type = type
        self.path = path
        self.inclusions = inclusions
        self.exclusions = exclusions
        self.basic_LibrarySource = basic_LibrarySource
        self.basic_LibrarySource6 = basic_LibrarySource6 if basic_LibrarySource6 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def exclusions(self) -> str:
        return self.__exclusions

    @exclusions.setter
    def exclusions(self, exclusions: str):
        self.__exclusions = exclusions

    @property
    def inclusions(self) -> str:
        return self.__inclusions

    @inclusions.setter
    def inclusions(self, inclusions: str):
        self.__inclusions = inclusions

    @property
    def basic_LibrarySource(self):
        return self.__basic_LibrarySource

    @basic_LibrarySource.setter
    def basic_LibrarySource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_LibrarySource__basic_LibrarySource", None)
        self.__basic_LibrarySource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_Library"):
                opp_val = getattr(old_value, "basic_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_Library"):
                opp_val = getattr(value, "basic_Library", None)
                if opp_val is None:
                    setattr(value, "basic_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic_LibrarySource6(self):
        return self.__basic_LibrarySource6

    @basic_LibrarySource6.setter
    def basic_LibrarySource6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_LibrarySource__basic_LibrarySource6", None)
        self.__basic_LibrarySource6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_File7"):
                    opp_val = getattr(item, "basic_File7", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_File7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_File7"):
                    opp_val = getattr(item, "basic_File7", None)
                    
                    setattr(item, "basic_File7", self)
                    

class basic_Library:

    def __init__(self, name: str, builtin: bool, versions: str, senchaTouchVersions: str, basic_Library: set["basic_LibrarySource"] = None):
        self.name = name
        self.builtin = builtin
        self.versions = versions
        self.senchaTouchVersions = senchaTouchVersions
        self.basic_Library = basic_Library if basic_Library is not None else set()
        
    @property
    def builtin(self) -> bool:
        return self.__builtin

    @builtin.setter
    def builtin(self, builtin: bool):
        self.__builtin = builtin

    @property
    def senchaTouchVersions(self) -> str:
        return self.__senchaTouchVersions

    @senchaTouchVersions.setter
    def senchaTouchVersions(self, senchaTouchVersions: str):
        self.__senchaTouchVersions = senchaTouchVersions

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def versions(self) -> str:
        return self.__versions

    @versions.setter
    def versions(self, versions: str):
        self.__versions = versions

    @property
    def basic_Library(self):
        return self.__basic_Library

    @basic_Library.setter
    def basic_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Library__basic_Library", None)
        self.__basic_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_LibrarySource"):
                    opp_val = getattr(item, "basic_LibrarySource", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_LibrarySource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_LibrarySource"):
                    opp_val = getattr(item, "basic_LibrarySource", None)
                    
                    setattr(item, "basic_LibrarySource", self)
                    

class basic_ExecutionEnvironment:

    def __init__(self, name: str, builtin: bool, versions: str, corePath: str, coreType: str, libraries: str, facet: str):
        self.name = name
        self.builtin = builtin
        self.versions = versions
        self.corePath = corePath
        self.coreType = coreType
        self.libraries = libraries
        self.facet = facet
        
    @property
    def builtin(self) -> bool:
        return self.__builtin

    @builtin.setter
    def builtin(self, builtin: bool):
        self.__builtin = builtin

    @property
    def corePath(self) -> str:
        return self.__corePath

    @corePath.setter
    def corePath(self, corePath: str):
        self.__corePath = corePath

    @property
    def coreType(self) -> str:
        return self.__coreType

    @coreType.setter
    def coreType(self, coreType: str):
        self.__coreType = coreType

    @property
    def facet(self) -> str:
        return self.__facet

    @facet.setter
    def facet(self, facet: str):
        self.__facet = facet

    @property
    def versions(self) -> str:
        return self.__versions

    @versions.setter
    def versions(self, versions: str):
        self.__versions = versions

    @property
    def libraries(self) -> str:
        return self.__libraries

    @libraries.setter
    def libraries(self, libraries: str):
        self.__libraries = libraries

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class basic_ExtJSProject:

    def __init__(self, name: str, basic_ExtJSProject: set["basic_File"] = None):
        self.name = name
        self.basic_ExtJSProject = basic_ExtJSProject if basic_ExtJSProject is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basic_ExtJSProject(self):
        return self.__basic_ExtJSProject

    @basic_ExtJSProject.setter
    def basic_ExtJSProject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_ExtJSProject__basic_ExtJSProject", None)
        self.__basic_ExtJSProject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_File"):
                    opp_val = getattr(item, "basic_File", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_File", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_File"):
                    opp_val = getattr(item, "basic_File", None)
                    
                    setattr(item, "basic_File", self)
                    

class Alias:

    pass
class basic_Plugin(Alias):

    pass
class basic_Widget(Alias):

    pass
class basic_Feature(Alias):

    pass
class basic_Layout(Alias):

    pass
class basic_File:

    def __init__(self, name: str, basic_File: "basic_ExtJSProject" = None, basic_File2: set["basic_Alias"] = None, basic_File7: "basic_LibrarySource" = None):
        self.name = name
        self.basic_File = basic_File
        self.basic_File2 = basic_File2 if basic_File2 is not None else set()
        self.basic_File7 = basic_File7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basic_File2(self):
        return self.__basic_File2

    @basic_File2.setter
    def basic_File2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_File__basic_File2", None)
        self.__basic_File2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_Alias"):
                    opp_val = getattr(item, "basic_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_Alias"):
                    opp_val = getattr(item, "basic_Alias", None)
                    
                    setattr(item, "basic_Alias", self)
                    

    @property
    def basic_File7(self):
        return self.__basic_File7

    @basic_File7.setter
    def basic_File7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_File__basic_File7", None)
        self.__basic_File7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_LibrarySource6"):
                opp_val = getattr(old_value, "basic_LibrarySource6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_LibrarySource6"):
                opp_val = getattr(value, "basic_LibrarySource6", None)
                if opp_val is None:
                    setattr(value, "basic_LibrarySource6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic_File(self):
        return self.__basic_File

    @basic_File.setter
    def basic_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_File__basic_File", None)
        self.__basic_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_ExtJSProject"):
                opp_val = getattr(old_value, "basic_ExtJSProject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_ExtJSProject"):
                opp_val = getattr(value, "basic_ExtJSProject", None)
                if opp_val is None:
                    setattr(value, "basic_ExtJSProject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def addAlias(self, sourceStart: int, name: str, sourceEnd: int, type: str):
        # TODO: Implement addAlias method
        pass

    def cleanAliases(self):
        # TODO: Implement cleanAliases method
        pass

class TypeItem:

    pass
class basic_Event(TypeItem):

    def __init__(self, name: str, description: str, basic_Event: set["basic_Parameter"] = None):
        self.name = name
        self.description = description
        self.basic_Event = basic_Event if basic_Event is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basic_Event(self):
        return self.__basic_Event

    @basic_Event.setter
    def basic_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Event__basic_Event", None)
        self.__basic_Event = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_Parameter"):
                    opp_val = getattr(item, "basic_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_Parameter"):
                    opp_val = getattr(item, "basic_Parameter", None)
                    
                    setattr(item, "basic_Parameter", self)
                    

class basic_Alias(TypeItem):

    def __init__(self, rawName: str, name: str, basic_Alias: "basic_File" = None):
        self.rawName = rawName
        self.name = name
        self.basic_Alias = basic_Alias
        
    @property
    def rawName(self) -> str:
        return self.__rawName

    @rawName.setter
    def rawName(self, rawName: str):
        self.__rawName = rawName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basic_Alias(self):
        return self.__basic_Alias

    @basic_Alias.setter
    def basic_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_Alias__basic_Alias", None)
        self.__basic_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_File2"):
                opp_val = getattr(old_value, "basic_File2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_File2"):
                opp_val = getattr(value, "basic_File2", None)
                if opp_val is None:
                    setattr(value, "basic_File2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basic_TypeItem(ABC):

    def __init__(self, sourceStart: int, sourceEnd: int, typeName: str):
        self.sourceStart = sourceStart
        self.sourceEnd = sourceEnd
        self.typeName = typeName
        
    @property
    def sourceStart(self) -> int:
        return self.__sourceStart

    @sourceStart.setter
    def sourceStart(self, sourceStart: int):
        self.__sourceStart = sourceStart

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def sourceEnd(self) -> int:
        return self.__sourceEnd

    @sourceEnd.setter
    def sourceEnd(self, sourceEnd: int):
        self.__sourceEnd = sourceEnd

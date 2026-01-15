from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StatusType(Enum):
    installed = "installed"
    not_installed = "not_installed"
    half_configured = "half_configured"
    half_installed = "half_installed"
    unpacked = "unpacked"
    config_files = "config_files"
class VersionType(Enum):
    eq = "eq"
    ge = "ge"
    le = "le"
    lt = "lt"
    llt = "llt"
    gt = "gt"
    ggt = "ggt"
class PriorityType(Enum):
    standard = "standard"
    required = "required"
    important = "important"
    optional = "optional"
    extra = "extra"


############################################
# Definition of Classes
############################################

class Conflict:

    pass
class mancoosimm_OrConflict(Conflict):

    pass
class mancoosimm_AndConflict(Conflict):

    pass
class mancoosimm_SingleConflict(Conflict):

    def __init__(self, value: str, version: str, singleConflict: "mancoosimm_Conflict" = None, SingleConflict: "mancoosimm_Conflict" = None):
        self.value = value
        self.version = version
        self.singleConflict = singleConflict
        self.SingleConflict = SingleConflict
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def SingleConflict(self):
        return self.__SingleConflict

    @SingleConflict.setter
    def SingleConflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SingleConflict__SingleConflict", None)
        self.__SingleConflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conflict282"):
                opp_val = getattr(old_value, "conflict282", None)
                if opp_val == self:
                    setattr(old_value, "conflict282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conflict282"):
                opp_val = getattr(value, "conflict282", None)
                setattr(value, "conflict282", self)

    @property
    def singleConflict(self):
        return self.__singleConflict

    @singleConflict.setter
    def singleConflict(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SingleConflict__singleConflict", None)
        self.__singleConflict = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conflict"):
                opp_val = getattr(old_value, "Conflict", None)
                if opp_val == self:
                    setattr(old_value, "Conflict", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conflict"):
                opp_val = getattr(value, "Conflict", None)
                setattr(value, "Conflict", self)

class mancoosimm_SharedLibrary:

    def __init__(self, name: str, version: str, SharedLibrary: "mancoosimm_LibraryCache" = None, mancoosimm_SharedLibrary: "mancoosimm_File" = None, sharedLibraries: "mancoosimm_LibraryCache" = None):
        self.name = name
        self.version = version
        self.SharedLibrary = SharedLibrary
        self.mancoosimm_SharedLibrary = mancoosimm_SharedLibrary
        self.sharedLibraries = sharedLibraries
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def SharedLibrary(self):
        return self.__SharedLibrary

    @SharedLibrary.setter
    def SharedLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SharedLibrary__SharedLibrary", None)
        self.__SharedLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryCache"):
                opp_val = getattr(old_value, "libraryCache", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryCache"):
                opp_val = getattr(value, "libraryCache", None)
                if opp_val is None:
                    setattr(value, "libraryCache", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sharedLibraries(self):
        return self.__sharedLibraries

    @sharedLibraries.setter
    def sharedLibraries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SharedLibrary__sharedLibraries", None)
        self.__sharedLibraries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LibraryCache233"):
                opp_val = getattr(old_value, "LibraryCache233", None)
                if opp_val == self:
                    setattr(old_value, "LibraryCache233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LibraryCache233"):
                opp_val = getattr(value, "LibraryCache233", None)
                setattr(value, "LibraryCache233", self)

    @property
    def mancoosimm_SharedLibrary(self):
        return self.__mancoosimm_SharedLibrary

    @mancoosimm_SharedLibrary.setter
    def mancoosimm_SharedLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SharedLibrary__mancoosimm_SharedLibrary", None)
        self.__mancoosimm_SharedLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_File231"):
                opp_val = getattr(old_value, "mancoosimm_File231", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_File231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_File231"):
                opp_val = getattr(value, "mancoosimm_File231", None)
                setattr(value, "mancoosimm_File231", self)

class mancoosimm_MimeType:

    def __init__(self, extension: str, name: str, MimeType: "mancoosimm_MimeTypeHandlerCache" = None, MimeType210: "mancoosimm_MimeTypeHandler" = None, type: set["mancoosimm_MimeTypeHandler"] = None, mimeTypes: "mancoosimm_MimeTypeHandlerCache" = None):
        self.extension = extension
        self.name = name
        self.MimeType = MimeType
        self.MimeType210 = MimeType210
        self.type = type if type is not None else set()
        self.mimeTypes = mimeTypes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def mimeTypes(self):
        return self.__mimeTypes

    @mimeTypes.setter
    def mimeTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__mimeTypes", None)
        self.__mimeTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MimeTypeHandlerCache216"):
                opp_val = getattr(old_value, "MimeTypeHandlerCache216", None)
                if opp_val == self:
                    setattr(old_value, "MimeTypeHandlerCache216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MimeTypeHandlerCache216"):
                opp_val = getattr(value, "MimeTypeHandlerCache216", None)
                setattr(value, "MimeTypeHandlerCache216", self)

    @property
    def MimeType210(self):
        return self.__MimeType210

    @MimeType210.setter
    def MimeType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__MimeType210", None)
        self.__MimeType210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mimeTypeHandlers"):
                opp_val = getattr(old_value, "mimeTypeHandlers", None)
                if opp_val == self:
                    setattr(old_value, "mimeTypeHandlers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mimeTypeHandlers"):
                opp_val = getattr(value, "mimeTypeHandlers", None)
                setattr(value, "mimeTypeHandlers", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MimeTypeHandler214"):
                    opp_val = getattr(item, "MimeTypeHandler214", None)
                    
                    if opp_val == self:
                        setattr(item, "MimeTypeHandler214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MimeTypeHandler214"):
                    opp_val = getattr(item, "MimeTypeHandler214", None)
                    
                    setattr(item, "MimeTypeHandler214", self)
                    

    @property
    def MimeType(self):
        return self.__MimeType

    @MimeType.setter
    def MimeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__MimeType", None)
        self.__MimeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cache206"):
                opp_val = getattr(old_value, "cache206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cache206"):
                opp_val = getattr(value, "cache206", None)
                if opp_val is None:
                    setattr(value, "cache206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_MimeTypeHandler:

    pass
class File:

    pass
class mancoosimm_InformationFile(File):

    pass
class mancoosimm_Boot:

    pass
class mancoosimm_Menu:

    pass
class mancoosimm_GConf:

    pass
class mancoosimm_XFontCache:

    def __init__(self, location: str, XFontCache: "mancoosimm_Environment" = None, xfontCache: set["mancoosimm_XFont"] = None, xfontCaches: "mancoosimm_Environment" = None, XFontCache221: "mancoosimm_XFont" = None):
        self.location = location
        self.XFontCache = XFontCache
        self.xfontCache = xfontCache if xfontCache is not None else set()
        self.xfontCaches = xfontCaches
        self.XFontCache221 = XFontCache221
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def XFontCache221(self):
        return self.__XFontCache221

    @XFontCache221.setter
    def XFontCache221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__XFontCache221", None)
        self.__XFontCache221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xfonts"):
                opp_val = getattr(old_value, "xfonts", None)
                if opp_val == self:
                    setattr(old_value, "xfonts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xfonts"):
                opp_val = getattr(value, "xfonts", None)
                setattr(value, "xfonts", self)

    @property
    def xfontCache(self):
        return self.__xfontCache

    @xfontCache.setter
    def xfontCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__xfontCache", None)
        self.__xfontCache = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XFont"):
                    opp_val = getattr(item, "XFont", None)
                    
                    if opp_val == self:
                        setattr(item, "XFont", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XFont"):
                    opp_val = getattr(item, "XFont", None)
                    
                    setattr(item, "XFont", self)
                    

    @property
    def xfontCaches(self):
        return self.__xfontCaches

    @xfontCaches.setter
    def xfontCaches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__xfontCaches", None)
        self.__xfontCaches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment219"):
                opp_val = getattr(old_value, "Environment219", None)
                if opp_val == self:
                    setattr(old_value, "Environment219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment219"):
                opp_val = getattr(value, "Environment219", None)
                setattr(value, "Environment219", self)

    @property
    def XFontCache(self):
        return self.__XFontCache

    @XFontCache.setter
    def XFontCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__XFontCache", None)
        self.__XFontCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "env126"):
                opp_val = getattr(old_value, "env126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env126"):
                opp_val = getattr(value, "env126", None)
                if opp_val is None:
                    setattr(value, "env126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_ModuleCache:

    def __init__(self, version: str, ModuleCache: "mancoosimm_Environment" = None, moduleCache236: "mancoosimm_Environment" = None, ModuleCache241: "mancoosimm_Module" = None, moduleCache: set["mancoosimm_Module"] = None):
        self.version = version
        self.ModuleCache = ModuleCache
        self.moduleCache236 = moduleCache236
        self.ModuleCache241 = ModuleCache241
        self.moduleCache = moduleCache if moduleCache is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def ModuleCache(self):
        return self.__ModuleCache

    @ModuleCache.setter
    def ModuleCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__ModuleCache", None)
        self.__ModuleCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "env124"):
                opp_val = getattr(old_value, "env124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env124"):
                opp_val = getattr(value, "env124", None)
                if opp_val is None:
                    setattr(value, "env124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ModuleCache241(self):
        return self.__ModuleCache241

    @ModuleCache241.setter
    def ModuleCache241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__ModuleCache241", None)
        self.__ModuleCache241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modules"):
                opp_val = getattr(old_value, "modules", None)
                if opp_val == self:
                    setattr(old_value, "modules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modules"):
                opp_val = getattr(value, "modules", None)
                setattr(value, "modules", self)

    @property
    def moduleCache236(self):
        return self.__moduleCache236

    @moduleCache236.setter
    def moduleCache236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__moduleCache236", None)
        self.__moduleCache236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment237"):
                opp_val = getattr(old_value, "Environment237", None)
                if opp_val == self:
                    setattr(old_value, "Environment237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment237"):
                opp_val = getattr(value, "Environment237", None)
                setattr(value, "Environment237", self)

    @property
    def moduleCache(self):
        return self.__moduleCache

    @moduleCache.setter
    def moduleCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__moduleCache", None)
        self.__moduleCache = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    if opp_val == self:
                        setattr(item, "Module", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    setattr(item, "Module", self)
                    

class mancoosimm_IconCache:

    def __init__(self, mtime: str, IconCache: "mancoosimm_Environment" = None, iconCache: "mancoosimm_Environment" = None, mancoosimm_IconCache: "mancoosimm_File" = None):
        self.mtime = mtime
        self.IconCache = IconCache
        self.iconCache = iconCache
        self.mancoosimm_IconCache = mancoosimm_IconCache
        
    @property
    def mtime(self) -> str:
        return self.__mtime

    @mtime.setter
    def mtime(self, mtime: str):
        self.__mtime = mtime

    @property
    def IconCache(self):
        return self.__IconCache

    @IconCache.setter
    def IconCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_IconCache__IconCache", None)
        self.__IconCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "env111"):
                opp_val = getattr(old_value, "env111", None)
                if opp_val == self:
                    setattr(old_value, "env111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env111"):
                opp_val = getattr(value, "env111", None)
                setattr(value, "env111", self)

    @property
    def mancoosimm_IconCache(self):
        return self.__mancoosimm_IconCache

    @mancoosimm_IconCache.setter
    def mancoosimm_IconCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_IconCache__mancoosimm_IconCache", None)
        self.__mancoosimm_IconCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_File197"):
                opp_val = getattr(old_value, "mancoosimm_File197", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_File197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_File197"):
                opp_val = getattr(value, "mancoosimm_File197", None)
                setattr(value, "mancoosimm_File197", self)

    @property
    def iconCache(self):
        return self.__iconCache

    @iconCache.setter
    def iconCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_IconCache__iconCache", None)
        self.__iconCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment195"):
                opp_val = getattr(old_value, "Environment195", None)
                if opp_val == self:
                    setattr(old_value, "Environment195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment195"):
                opp_val = getattr(value, "Environment195", None)
                setattr(value, "Environment195", self)

class mancoosimm_LibraryCache:

    pass
class mancoosimm_MimeTypeHandlerCache:

    pass
class mancoosimm_DesktopDB:

    pass
class mancoosimm_NotInv:

    pass
class mancoosimm_OrInv:

    pass
class mancoosimm_AndInv:

    pass
class Dependence:

    pass
class mancoosimm_SingleDep(Dependence):

    def __init__(self, version: str, value: str, SingleDep: "mancoosimm_Dependence" = None, singleDep: "mancoosimm_Dependence" = None):
        self.version = version
        self.value = value
        self.SingleDep = SingleDep
        self.singleDep = singleDep
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def SingleDep(self):
        return self.__SingleDep

    @SingleDep.setter
    def SingleDep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SingleDep__SingleDep", None)
        self.__SingleDep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependence66"):
                opp_val = getattr(old_value, "dependence66", None)
                if opp_val == self:
                    setattr(old_value, "dependence66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependence66"):
                opp_val = getattr(value, "dependence66", None)
                setattr(value, "dependence66", self)

    @property
    def singleDep(self):
        return self.__singleDep

    @singleDep.setter
    def singleDep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SingleDep__singleDep", None)
        self.__singleDep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dependence78"):
                opp_val = getattr(old_value, "Dependence78", None)
                if opp_val == self:
                    setattr(old_value, "Dependence78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dependence78"):
                opp_val = getattr(value, "Dependence78", None)
                setattr(value, "Dependence78", self)

class mancoosimm_OrDep(Dependence):

    pass
class mancoosimm_AndDep(Dependence):

    pass
class InstalledPackage:

    pass
class mancoosimm_BinPackage(InstalledPackage):

    pass
class UnpackedPackage:

    pass
class mancoosimm_Conflict(ABC):

    pass
class mancoosimm_DocumentationFile(File):

    pass
class mancoosimm_VirtualPackage(InstalledPackage):

    pass
class mancoosimm_Dependence(ABC):

    pass
class mancoosimm_SrcPackage(InstalledPackage):

    pass
class Package:

    pass
class mancoosimm_HalfInstalledReinstRequiredPackage(Package):

    def __init__(self, maintainer: str, checkSum: str, description: str, section: str, tag: str, priority: str, uploaders: str, mancoosimm_HalfInstalledReinstRequiredPackage: "mancoosimm_Configuration" = None):
        self.maintainer = maintainer
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.priority = priority
        self.uploaders = uploaders
        self.mancoosimm_HalfInstalledReinstRequiredPackage = mancoosimm_HalfInstalledReinstRequiredPackage
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

    @property
    def mancoosimm_HalfInstalledReinstRequiredPackage(self):
        return self.__mancoosimm_HalfInstalledReinstRequiredPackage

    @mancoosimm_HalfInstalledReinstRequiredPackage.setter
    def mancoosimm_HalfInstalledReinstRequiredPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_HalfInstalledReinstRequiredPackage__mancoosimm_HalfInstalledReinstRequiredPackage", None)
        self.__mancoosimm_HalfInstalledReinstRequiredPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration17"):
                opp_val = getattr(old_value, "mancoosimm_Configuration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration17"):
                opp_val = getattr(value, "mancoosimm_Configuration17", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_Configuration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_HalfConfiguredReinstRequiredPackage(UnpackedPackage):

    pass
class mancoosimm_HalfInstalledPackage(Package):

    def __init__(self, maintainer: str, checkSum: str, description: str, section: str, tag: str, priority: str, uploaders: str, mancoosimm_HalfInstalledPackage: "mancoosimm_Configuration" = None):
        self.maintainer = maintainer
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.priority = priority
        self.uploaders = uploaders
        self.mancoosimm_HalfInstalledPackage = mancoosimm_HalfInstalledPackage
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def mancoosimm_HalfInstalledPackage(self):
        return self.__mancoosimm_HalfInstalledPackage

    @mancoosimm_HalfInstalledPackage.setter
    def mancoosimm_HalfInstalledPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_HalfInstalledPackage__mancoosimm_HalfInstalledPackage", None)
        self.__mancoosimm_HalfInstalledPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration13"):
                opp_val = getattr(old_value, "mancoosimm_Configuration13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration13"):
                opp_val = getattr(value, "mancoosimm_Configuration13", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_Configuration13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_HalfConfiguredPackage(UnpackedPackage):

    pass
class mancoosimm_UnpackedPackage(Package):

    def __init__(self, maintainer: str, checkSum: str, description: str, section: str, tag: str, priority: str, uploaders: str, mancoosimm_UnpackedPackage: "mancoosimm_Configuration" = None, mancoosimm_UnpackedPackage49: set["mancoosimm_File"] = None):
        self.maintainer = maintainer
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.priority = priority
        self.uploaders = uploaders
        self.mancoosimm_UnpackedPackage = mancoosimm_UnpackedPackage
        self.mancoosimm_UnpackedPackage49 = mancoosimm_UnpackedPackage49 if mancoosimm_UnpackedPackage49 is not None else set()
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

    @property
    def mancoosimm_UnpackedPackage(self):
        return self.__mancoosimm_UnpackedPackage

    @mancoosimm_UnpackedPackage.setter
    def mancoosimm_UnpackedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_UnpackedPackage__mancoosimm_UnpackedPackage", None)
        self.__mancoosimm_UnpackedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration9"):
                opp_val = getattr(old_value, "mancoosimm_Configuration9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration9"):
                opp_val = getattr(value, "mancoosimm_Configuration9", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_Configuration9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_UnpackedPackage49(self):
        return self.__mancoosimm_UnpackedPackage49

    @mancoosimm_UnpackedPackage49.setter
    def mancoosimm_UnpackedPackage49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_UnpackedPackage__mancoosimm_UnpackedPackage49", None)
        self.__mancoosimm_UnpackedPackage49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_File50"):
                    opp_val = getattr(item, "mancoosimm_File50", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_File50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_File50"):
                    opp_val = getattr(item, "mancoosimm_File50", None)
                    
                    setattr(item, "mancoosimm_File50", self)
                    

class mancoosimm_ConfigFilesPackage(Package):

    def __init__(self, maintainer: str, checkSum: str, description: str, section: str, tag: str, priority: str, uploaders: str, mancoosimm_ConfigFilesPackage: "mancoosimm_Configuration" = None):
        self.maintainer = maintainer
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.priority = priority
        self.uploaders = uploaders
        self.mancoosimm_ConfigFilesPackage = mancoosimm_ConfigFilesPackage
        
    @property
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def mancoosimm_ConfigFilesPackage(self):
        return self.__mancoosimm_ConfigFilesPackage

    @mancoosimm_ConfigFilesPackage.setter
    def mancoosimm_ConfigFilesPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ConfigFilesPackage__mancoosimm_ConfigFilesPackage", None)
        self.__mancoosimm_ConfigFilesPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration7"):
                opp_val = getattr(old_value, "mancoosimm_Configuration7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration7"):
                opp_val = getattr(value, "mancoosimm_Configuration7", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_Configuration7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_NotInstalledPackage(Package):

    pass
class mancoosimm_InstalledPackage(Package):

    def __init__(self, installedSize: int, maintainer: str, fileSize: int, checkSum: str, description: str, section: str, tag: str, uploaders: str, priority: str, mancoosimm_InstalledPackage: "mancoosimm_Configuration" = None, mancoosimm_InstalledPackage22: "mancoosimm_SrcPackage" = None, mancoosimm_InstalledPackage24: "mancoosimm_Dependence" = None, mancoosimm_InstalledPackage27: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage25: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage30: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage28: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage33: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage31: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage36: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage34: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage38: "mancoosimm_VirtualPackage" = None, mancoosimm_InstalledPackage41: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage39: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage43: set["mancoosimm_File"] = None, pkg45: set["mancoosimm_DocumentationFile"] = None, mancoosimm_InstalledPackage47: "mancoosimm_Conflict" = None, mancoosimm_InstalledPackage61: "mancoosimm_VirtualPackage" = None, InstalledPackage: "mancoosimm_DocumentationFile" = None):
        self.installedSize = installedSize
        self.maintainer = maintainer
        self.fileSize = fileSize
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.uploaders = uploaders
        self.priority = priority
        self.mancoosimm_InstalledPackage = mancoosimm_InstalledPackage
        self.mancoosimm_InstalledPackage22 = mancoosimm_InstalledPackage22
        self.mancoosimm_InstalledPackage24 = mancoosimm_InstalledPackage24
        self.mancoosimm_InstalledPackage27 = mancoosimm_InstalledPackage27
        self.mancoosimm_InstalledPackage25 = mancoosimm_InstalledPackage25 if mancoosimm_InstalledPackage25 is not None else set()
        self.mancoosimm_InstalledPackage30 = mancoosimm_InstalledPackage30
        self.mancoosimm_InstalledPackage28 = mancoosimm_InstalledPackage28 if mancoosimm_InstalledPackage28 is not None else set()
        self.mancoosimm_InstalledPackage33 = mancoosimm_InstalledPackage33
        self.mancoosimm_InstalledPackage31 = mancoosimm_InstalledPackage31 if mancoosimm_InstalledPackage31 is not None else set()
        self.mancoosimm_InstalledPackage36 = mancoosimm_InstalledPackage36
        self.mancoosimm_InstalledPackage34 = mancoosimm_InstalledPackage34 if mancoosimm_InstalledPackage34 is not None else set()
        self.mancoosimm_InstalledPackage38 = mancoosimm_InstalledPackage38
        self.mancoosimm_InstalledPackage41 = mancoosimm_InstalledPackage41
        self.mancoosimm_InstalledPackage39 = mancoosimm_InstalledPackage39 if mancoosimm_InstalledPackage39 is not None else set()
        self.mancoosimm_InstalledPackage43 = mancoosimm_InstalledPackage43 if mancoosimm_InstalledPackage43 is not None else set()
        self.pkg45 = pkg45 if pkg45 is not None else set()
        self.mancoosimm_InstalledPackage47 = mancoosimm_InstalledPackage47
        self.mancoosimm_InstalledPackage61 = mancoosimm_InstalledPackage61
        self.InstalledPackage = InstalledPackage
        
    @property
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def fileSize(self) -> int:
        return self.__fileSize

    @fileSize.setter
    def fileSize(self, fileSize: int):
        self.__fileSize = fileSize

    @property
    def installedSize(self) -> int:
        return self.__installedSize

    @installedSize.setter
    def installedSize(self, installedSize: int):
        self.__installedSize = installedSize

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def pkg45(self):
        return self.__pkg45

    @pkg45.setter
    def pkg45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__pkg45", None)
        self.__pkg45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DocumentationFile"):
                    opp_val = getattr(item, "DocumentationFile", None)
                    
                    if opp_val == self:
                        setattr(item, "DocumentationFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DocumentationFile"):
                    opp_val = getattr(item, "DocumentationFile", None)
                    
                    setattr(item, "DocumentationFile", self)
                    

    @property
    def mancoosimm_InstalledPackage43(self):
        return self.__mancoosimm_InstalledPackage43

    @mancoosimm_InstalledPackage43.setter
    def mancoosimm_InstalledPackage43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage43", None)
        self.__mancoosimm_InstalledPackage43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_File"):
                    opp_val = getattr(item, "mancoosimm_File", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_File", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_File"):
                    opp_val = getattr(item, "mancoosimm_File", None)
                    
                    setattr(item, "mancoosimm_File", self)
                    

    @property
    def mancoosimm_InstalledPackage31(self):
        return self.__mancoosimm_InstalledPackage31

    @mancoosimm_InstalledPackage31.setter
    def mancoosimm_InstalledPackage31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage31", None)
        self.__mancoosimm_InstalledPackage31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage33"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage33", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage33"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage33", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage33", self)
                    

    @property
    def mancoosimm_InstalledPackage34(self):
        return self.__mancoosimm_InstalledPackage34

    @mancoosimm_InstalledPackage34.setter
    def mancoosimm_InstalledPackage34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage34", None)
        self.__mancoosimm_InstalledPackage34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage36"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage36", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage36"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage36", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage36", self)
                    

    @property
    def mancoosimm_InstalledPackage61(self):
        return self.__mancoosimm_InstalledPackage61

    @mancoosimm_InstalledPackage61.setter
    def mancoosimm_InstalledPackage61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage61", None)
        self.__mancoosimm_InstalledPackage61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_VirtualPackage60"):
                opp_val = getattr(old_value, "mancoosimm_VirtualPackage60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_VirtualPackage60"):
                opp_val = getattr(value, "mancoosimm_VirtualPackage60", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_VirtualPackage60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def InstalledPackage(self):
        return self.__InstalledPackage

    @InstalledPackage.setter
    def InstalledPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__InstalledPackage", None)
        self.__InstalledPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentationFiles"):
                opp_val = getattr(old_value, "documentationFiles", None)
                if opp_val == self:
                    setattr(old_value, "documentationFiles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentationFiles"):
                opp_val = getattr(value, "documentationFiles", None)
                setattr(value, "documentationFiles", self)

    @property
    def mancoosimm_InstalledPackage28(self):
        return self.__mancoosimm_InstalledPackage28

    @mancoosimm_InstalledPackage28.setter
    def mancoosimm_InstalledPackage28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage28", None)
        self.__mancoosimm_InstalledPackage28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage30"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage30", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage30"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage30", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage30", self)
                    

    @property
    def mancoosimm_InstalledPackage33(self):
        return self.__mancoosimm_InstalledPackage33

    @mancoosimm_InstalledPackage33.setter
    def mancoosimm_InstalledPackage33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage33", None)
        self.__mancoosimm_InstalledPackage33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage31"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage31"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage31", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage22(self):
        return self.__mancoosimm_InstalledPackage22

    @mancoosimm_InstalledPackage22.setter
    def mancoosimm_InstalledPackage22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage22", None)
        self.__mancoosimm_InstalledPackage22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SrcPackage"):
                opp_val = getattr(old_value, "mancoosimm_SrcPackage", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SrcPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SrcPackage"):
                opp_val = getattr(value, "mancoosimm_SrcPackage", None)
                setattr(value, "mancoosimm_SrcPackage", self)

    @property
    def mancoosimm_InstalledPackage24(self):
        return self.__mancoosimm_InstalledPackage24

    @mancoosimm_InstalledPackage24.setter
    def mancoosimm_InstalledPackage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage24", None)
        self.__mancoosimm_InstalledPackage24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Dependence"):
                opp_val = getattr(old_value, "mancoosimm_Dependence", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Dependence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Dependence"):
                opp_val = getattr(value, "mancoosimm_Dependence", None)
                setattr(value, "mancoosimm_Dependence", self)

    @property
    def mancoosimm_InstalledPackage(self):
        return self.__mancoosimm_InstalledPackage

    @mancoosimm_InstalledPackage.setter
    def mancoosimm_InstalledPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage", None)
        self.__mancoosimm_InstalledPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration"):
                opp_val = getattr(old_value, "mancoosimm_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration"):
                opp_val = getattr(value, "mancoosimm_Configuration", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage39(self):
        return self.__mancoosimm_InstalledPackage39

    @mancoosimm_InstalledPackage39.setter
    def mancoosimm_InstalledPackage39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage39", None)
        self.__mancoosimm_InstalledPackage39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage41"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage41", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage41"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage41", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage41", self)
                    

    @property
    def mancoosimm_InstalledPackage41(self):
        return self.__mancoosimm_InstalledPackage41

    @mancoosimm_InstalledPackage41.setter
    def mancoosimm_InstalledPackage41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage41", None)
        self.__mancoosimm_InstalledPackage41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage39"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage39"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage39", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage47(self):
        return self.__mancoosimm_InstalledPackage47

    @mancoosimm_InstalledPackage47.setter
    def mancoosimm_InstalledPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage47", None)
        self.__mancoosimm_InstalledPackage47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Conflict"):
                opp_val = getattr(old_value, "mancoosimm_Conflict", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Conflict", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Conflict"):
                opp_val = getattr(value, "mancoosimm_Conflict", None)
                setattr(value, "mancoosimm_Conflict", self)

    @property
    def mancoosimm_InstalledPackage38(self):
        return self.__mancoosimm_InstalledPackage38

    @mancoosimm_InstalledPackage38.setter
    def mancoosimm_InstalledPackage38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage38", None)
        self.__mancoosimm_InstalledPackage38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_VirtualPackage"):
                opp_val = getattr(old_value, "mancoosimm_VirtualPackage", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_VirtualPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_VirtualPackage"):
                opp_val = getattr(value, "mancoosimm_VirtualPackage", None)
                setattr(value, "mancoosimm_VirtualPackage", self)

    @property
    def mancoosimm_InstalledPackage36(self):
        return self.__mancoosimm_InstalledPackage36

    @mancoosimm_InstalledPackage36.setter
    def mancoosimm_InstalledPackage36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage36", None)
        self.__mancoosimm_InstalledPackage36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage34"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage34"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage34", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage27(self):
        return self.__mancoosimm_InstalledPackage27

    @mancoosimm_InstalledPackage27.setter
    def mancoosimm_InstalledPackage27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage27", None)
        self.__mancoosimm_InstalledPackage27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage25"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage25"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage25", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage30(self):
        return self.__mancoosimm_InstalledPackage30

    @mancoosimm_InstalledPackage30.setter
    def mancoosimm_InstalledPackage30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage30", None)
        self.__mancoosimm_InstalledPackage30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage28"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage28"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage28", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage25(self):
        return self.__mancoosimm_InstalledPackage25

    @mancoosimm_InstalledPackage25.setter
    def mancoosimm_InstalledPackage25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage25", None)
        self.__mancoosimm_InstalledPackage25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage27"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage27", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage27"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage27", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage27", self)
                    

class NamedElement:

    pass
class mancoosimm_Atom(NamedElement):

    pass
class mancoosimm_Invariant(NamedElement):

    pass
class mancoosimm_SkeeperCatalog(NamedElement):

    pass
class mancoosimm_Package(NamedElement):

    def __init__(self, version: str, architecture: str, mancoosimm_Package: "mancoosimm_Configuration" = None, pkg: "mancoosimm_PackageSetting" = None, mancoosimm_Package69: "mancoosimm_Dependence" = None, Package: "mancoosimm_PackageSetting" = None, mancoosimm_Package285: "mancoosimm_Conflict" = None):
        self.version = version
        self.architecture = architecture
        self.mancoosimm_Package = mancoosimm_Package
        self.pkg = pkg
        self.mancoosimm_Package69 = mancoosimm_Package69
        self.Package = Package
        self.mancoosimm_Package285 = mancoosimm_Package285
        
    @property
    def architecture(self) -> str:
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def mancoosimm_Package285(self):
        return self.__mancoosimm_Package285

    @mancoosimm_Package285.setter
    def mancoosimm_Package285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__mancoosimm_Package285", None)
        self.__mancoosimm_Package285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Conflict284"):
                opp_val = getattr(old_value, "mancoosimm_Conflict284", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Conflict284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Conflict284"):
                opp_val = getattr(value, "mancoosimm_Conflict284", None)
                setattr(value, "mancoosimm_Conflict284", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageSettings"):
                opp_val = getattr(old_value, "packageSettings", None)
                if opp_val == self:
                    setattr(old_value, "packageSettings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageSettings"):
                opp_val = getattr(value, "packageSettings", None)
                setattr(value, "packageSettings", self)

    @property
    def mancoosimm_Package69(self):
        return self.__mancoosimm_Package69

    @mancoosimm_Package69.setter
    def mancoosimm_Package69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__mancoosimm_Package69", None)
        self.__mancoosimm_Package69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Dependence68"):
                opp_val = getattr(old_value, "mancoosimm_Dependence68", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Dependence68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Dependence68"):
                opp_val = getattr(value, "mancoosimm_Dependence68", None)
                setattr(value, "mancoosimm_Dependence68", self)

    @property
    def pkg(self):
        return self.__pkg

    @pkg.setter
    def pkg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__pkg", None)
        self.__pkg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageSetting"):
                opp_val = getattr(old_value, "PackageSetting", None)
                if opp_val == self:
                    setattr(old_value, "PackageSetting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageSetting"):
                opp_val = getattr(value, "PackageSetting", None)
                setattr(value, "PackageSetting", self)

    @property
    def mancoosimm_Package(self):
        return self.__mancoosimm_Package

    @mancoosimm_Package.setter
    def mancoosimm_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__mancoosimm_Package", None)
        self.__mancoosimm_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Configuration19"):
                opp_val = getattr(old_value, "mancoosimm_Configuration19", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Configuration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration19"):
                opp_val = getattr(value, "mancoosimm_Configuration19", None)
                setattr(value, "mancoosimm_Configuration19", self)

class mancoosimm_EmacsPackage(NamedElement):

    pass
class mancoosimm_SGMLCatalog(NamedElement):

    pass
class mancoosimm_Alternative(NamedElement):

    pass
class mancoosimm_Group(NamedElement):

    pass
class mancoosimm_XFont(NamedElement):

    pass
class mancoosimm_SkeeperDocument(NamedElement):

    pass
class mancoosimm_User(NamedElement):

    pass
class mancoosimm_MenuEntry(NamedElement):

    pass
class mancoosimm_ApplicationMenuCatalog(NamedElement):

    pass
class mancoosimm_Environment(NamedElement):

    pass
class mancoosimm_PackageSetting(NamedElement):

    pass
class mancoosimm_FileSystem(NamedElement):

    pass
class mancoosimm_File(NamedElement):

    def __init__(self, extension: str, description: str, size: int, suid: bool, guid: bool, permission: str, location: str, isMissing: bool, checkSum: str, isDirectory: bool, mancoosimm_File: "mancoosimm_InstalledPackage" = None, mancoosimm_File50: "mancoosimm_UnpackedPackage" = None, File: "mancoosimm_FileSystem" = None, mancoosimm_File135: "mancoosimm_FileSystem" = None, mancoosimm_File137: "mancoosimm_GConf" = None, mancoosimm_File140: "mancoosimm_GConf" = None, mancoosimm_File154: "mancoosimm_MenuEntry" = None, mancoosimm_File161: "mancoosimm_Service" = None, root: "mancoosimm_FileSystem" = None, File168: "mancoosimm_File" = None, parent: set["mancoosimm_File"] = None, File171: "mancoosimm_File" = None, childs: "mancoosimm_File" = None, mancoosimm_File173: "mancoosimm_User" = None, mancoosimm_File175: "mancoosimm_Group" = None, files: set["mancoosimm_PackageSetting"] = None, mancoosimm_File180: "mancoosimm_Alternative" = None, mancoosimm_File183: "mancoosimm_Alternative" = None, File189: "mancoosimm_PackageSetting" = None, mancoosimm_File197: "mancoosimm_IconCache" = None, mancoosimm_File208: "mancoosimm_MimeTypeHandler" = None, mancoosimm_File201: "mancoosimm_DesktopDB" = None, mancoosimm_File223: "mancoosimm_XFont" = None, mancoosimm_File225: "mancoosimm_LibraryCache" = None, mancoosimm_File231: "mancoosimm_SharedLibrary" = None, mancoosimm_File239: "mancoosimm_Module" = None, mancoosimm_File247: "mancoosimm_SGMLDocument" = None, mancoosimm_File250: "mancoosimm_SGMLDocument" = None, mancoosimm_File256: "mancoosimm_SkeeperDocument" = None, mancoosimm_File259: "mancoosimm_SkeeperDocument" = None, mancoosimm_File261: "mancoosimm_EmacsPackage" = None, mancoosimm_File271: "mancoosimm_User" = None):
        self.extension = extension
        self.description = description
        self.size = size
        self.suid = suid
        self.guid = guid
        self.permission = permission
        self.location = location
        self.isMissing = isMissing
        self.checkSum = checkSum
        self.isDirectory = isDirectory
        self.mancoosimm_File = mancoosimm_File
        self.mancoosimm_File50 = mancoosimm_File50
        self.File = File
        self.mancoosimm_File135 = mancoosimm_File135
        self.mancoosimm_File137 = mancoosimm_File137
        self.mancoosimm_File140 = mancoosimm_File140
        self.mancoosimm_File154 = mancoosimm_File154
        self.mancoosimm_File161 = mancoosimm_File161
        self.root = root
        self.File168 = File168
        self.parent = parent if parent is not None else set()
        self.File171 = File171
        self.childs = childs
        self.mancoosimm_File173 = mancoosimm_File173
        self.mancoosimm_File175 = mancoosimm_File175
        self.files = files if files is not None else set()
        self.mancoosimm_File180 = mancoosimm_File180
        self.mancoosimm_File183 = mancoosimm_File183
        self.File189 = File189
        self.mancoosimm_File197 = mancoosimm_File197
        self.mancoosimm_File208 = mancoosimm_File208
        self.mancoosimm_File201 = mancoosimm_File201
        self.mancoosimm_File223 = mancoosimm_File223
        self.mancoosimm_File225 = mancoosimm_File225
        self.mancoosimm_File231 = mancoosimm_File231
        self.mancoosimm_File239 = mancoosimm_File239
        self.mancoosimm_File247 = mancoosimm_File247
        self.mancoosimm_File250 = mancoosimm_File250
        self.mancoosimm_File256 = mancoosimm_File256
        self.mancoosimm_File259 = mancoosimm_File259
        self.mancoosimm_File261 = mancoosimm_File261
        self.mancoosimm_File271 = mancoosimm_File271
        
    @property
    def isMissing(self) -> bool:
        return self.__isMissing

    @isMissing.setter
    def isMissing(self, isMissing: bool):
        self.__isMissing = isMissing

    @property
    def guid(self) -> bool:
        return self.__guid

    @guid.setter
    def guid(self, guid: bool):
        self.__guid = guid

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def permission(self) -> str:
        return self.__permission

    @permission.setter
    def permission(self, permission: str):
        self.__permission = permission

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def suid(self) -> bool:
        return self.__suid

    @suid.setter
    def suid(self, suid: bool):
        self.__suid = suid

    @property
    def isDirectory(self) -> bool:
        return self.__isDirectory

    @isDirectory.setter
    def isDirectory(self, isDirectory: bool):
        self.__isDirectory = isDirectory

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def mancoosimm_File223(self):
        return self.__mancoosimm_File223

    @mancoosimm_File223.setter
    def mancoosimm_File223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File223", None)
        self.__mancoosimm_File223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_XFont"):
                opp_val = getattr(old_value, "mancoosimm_XFont", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_XFont"):
                opp_val = getattr(value, "mancoosimm_XFont", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_XFont", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File135(self):
        return self.__mancoosimm_File135

    @mancoosimm_File135.setter
    def mancoosimm_File135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File135", None)
        self.__mancoosimm_File135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_FileSystem"):
                opp_val = getattr(old_value, "mancoosimm_FileSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_FileSystem"):
                opp_val = getattr(value, "mancoosimm_FileSystem", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_FileSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File225(self):
        return self.__mancoosimm_File225

    @mancoosimm_File225.setter
    def mancoosimm_File225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File225", None)
        self.__mancoosimm_File225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_LibraryCache"):
                opp_val = getattr(old_value, "mancoosimm_LibraryCache", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_LibraryCache"):
                opp_val = getattr(value, "mancoosimm_LibraryCache", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_LibraryCache", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File261(self):
        return self.__mancoosimm_File261

    @mancoosimm_File261.setter
    def mancoosimm_File261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File261", None)
        self.__mancoosimm_File261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_EmacsPackage"):
                opp_val = getattr(old_value, "mancoosimm_EmacsPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_EmacsPackage"):
                opp_val = getattr(value, "mancoosimm_EmacsPackage", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_EmacsPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File180(self):
        return self.__mancoosimm_File180

    @mancoosimm_File180.setter
    def mancoosimm_File180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File180", None)
        self.__mancoosimm_File180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Alternative"):
                opp_val = getattr(old_value, "mancoosimm_Alternative", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Alternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Alternative"):
                opp_val = getattr(value, "mancoosimm_Alternative", None)
                setattr(value, "mancoosimm_Alternative", self)

    @property
    def File(self):
        return self.__File

    @File.setter
    def File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File", None)
        self.__File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fs"):
                opp_val = getattr(old_value, "fs", None)
                if opp_val == self:
                    setattr(old_value, "fs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fs"):
                opp_val = getattr(value, "fs", None)
                setattr(value, "fs", self)

    @property
    def mancoosimm_File161(self):
        return self.__mancoosimm_File161

    @mancoosimm_File161.setter
    def mancoosimm_File161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File161", None)
        self.__mancoosimm_File161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Service160"):
                opp_val = getattr(old_value, "mancoosimm_Service160", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Service160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Service160"):
                opp_val = getattr(value, "mancoosimm_Service160", None)
                setattr(value, "mancoosimm_Service160", self)

    @property
    def mancoosimm_File197(self):
        return self.__mancoosimm_File197

    @mancoosimm_File197.setter
    def mancoosimm_File197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File197", None)
        self.__mancoosimm_File197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_IconCache"):
                opp_val = getattr(old_value, "mancoosimm_IconCache", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_IconCache", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_IconCache"):
                opp_val = getattr(value, "mancoosimm_IconCache", None)
                setattr(value, "mancoosimm_IconCache", self)

    @property
    def mancoosimm_File183(self):
        return self.__mancoosimm_File183

    @mancoosimm_File183.setter
    def mancoosimm_File183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File183", None)
        self.__mancoosimm_File183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Alternative182"):
                opp_val = getattr(old_value, "mancoosimm_Alternative182", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Alternative182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Alternative182"):
                opp_val = getattr(value, "mancoosimm_Alternative182", None)
                setattr(value, "mancoosimm_Alternative182", self)

    @property
    def mancoosimm_File(self):
        return self.__mancoosimm_File

    @mancoosimm_File.setter
    def mancoosimm_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File", None)
        self.__mancoosimm_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage43"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage43"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage43", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File239(self):
        return self.__mancoosimm_File239

    @mancoosimm_File239.setter
    def mancoosimm_File239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File239", None)
        self.__mancoosimm_File239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Module"):
                opp_val = getattr(old_value, "mancoosimm_Module", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Module"):
                opp_val = getattr(value, "mancoosimm_Module", None)
                setattr(value, "mancoosimm_Module", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File168"):
                    opp_val = getattr(item, "File168", None)
                    
                    if opp_val == self:
                        setattr(item, "File168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File168"):
                    opp_val = getattr(item, "File168", None)
                    
                    setattr(item, "File168", self)
                    

    @property
    def mancoosimm_File250(self):
        return self.__mancoosimm_File250

    @mancoosimm_File250.setter
    def mancoosimm_File250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File250", None)
        self.__mancoosimm_File250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SGMLDocument249"):
                opp_val = getattr(old_value, "mancoosimm_SGMLDocument249", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SGMLDocument249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SGMLDocument249"):
                opp_val = getattr(value, "mancoosimm_SGMLDocument249", None)
                setattr(value, "mancoosimm_SGMLDocument249", self)

    @property
    def mancoosimm_File256(self):
        return self.__mancoosimm_File256

    @mancoosimm_File256.setter
    def mancoosimm_File256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File256", None)
        self.__mancoosimm_File256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SkeeperDocument255"):
                opp_val = getattr(old_value, "mancoosimm_SkeeperDocument255", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SkeeperDocument255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SkeeperDocument255"):
                opp_val = getattr(value, "mancoosimm_SkeeperDocument255", None)
                setattr(value, "mancoosimm_SkeeperDocument255", self)

    @property
    def mancoosimm_File175(self):
        return self.__mancoosimm_File175

    @mancoosimm_File175.setter
    def mancoosimm_File175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File175", None)
        self.__mancoosimm_File175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Group"):
                opp_val = getattr(old_value, "mancoosimm_Group", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Group"):
                opp_val = getattr(value, "mancoosimm_Group", None)
                setattr(value, "mancoosimm_Group", self)

    @property
    def mancoosimm_File271(self):
        return self.__mancoosimm_File271

    @mancoosimm_File271.setter
    def mancoosimm_File271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File271", None)
        self.__mancoosimm_File271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_User270"):
                opp_val = getattr(old_value, "mancoosimm_User270", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_User270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_User270"):
                opp_val = getattr(value, "mancoosimm_User270", None)
                setattr(value, "mancoosimm_User270", self)

    @property
    def mancoosimm_File50(self):
        return self.__mancoosimm_File50

    @mancoosimm_File50.setter
    def mancoosimm_File50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File50", None)
        self.__mancoosimm_File50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_UnpackedPackage49"):
                opp_val = getattr(old_value, "mancoosimm_UnpackedPackage49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_UnpackedPackage49"):
                opp_val = getattr(value, "mancoosimm_UnpackedPackage49", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_UnpackedPackage49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__files", None)
        self.__files = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PackageSetting177"):
                    opp_val = getattr(item, "PackageSetting177", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageSetting177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageSetting177"):
                    opp_val = getattr(item, "PackageSetting177", None)
                    
                    setattr(item, "PackageSetting177", self)
                    

    @property
    def childs(self):
        return self.__childs

    @childs.setter
    def childs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__childs", None)
        self.__childs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File171"):
                opp_val = getattr(old_value, "File171", None)
                if opp_val == self:
                    setattr(old_value, "File171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File171"):
                opp_val = getattr(value, "File171", None)
                setattr(value, "File171", self)

    @property
    def mancoosimm_File247(self):
        return self.__mancoosimm_File247

    @mancoosimm_File247.setter
    def mancoosimm_File247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File247", None)
        self.__mancoosimm_File247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SGMLDocument246"):
                opp_val = getattr(old_value, "mancoosimm_SGMLDocument246", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SGMLDocument246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SGMLDocument246"):
                opp_val = getattr(value, "mancoosimm_SGMLDocument246", None)
                setattr(value, "mancoosimm_SGMLDocument246", self)

    @property
    def File189(self):
        return self.__File189

    @File189.setter
    def File189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File189", None)
        self.__File189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pkgSettings"):
                opp_val = getattr(old_value, "pkgSettings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pkgSettings"):
                opp_val = getattr(value, "pkgSettings", None)
                if opp_val is None:
                    setattr(value, "pkgSettings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def File171(self):
        return self.__File171

    @File171.setter
    def File171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File171", None)
        self.__File171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childs"):
                opp_val = getattr(old_value, "childs", None)
                if opp_val == self:
                    setattr(old_value, "childs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childs"):
                opp_val = getattr(value, "childs", None)
                setattr(value, "childs", self)

    @property
    def mancoosimm_File208(self):
        return self.__mancoosimm_File208

    @mancoosimm_File208.setter
    def mancoosimm_File208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File208", None)
        self.__mancoosimm_File208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_MimeTypeHandler"):
                opp_val = getattr(old_value, "mancoosimm_MimeTypeHandler", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_MimeTypeHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_MimeTypeHandler"):
                opp_val = getattr(value, "mancoosimm_MimeTypeHandler", None)
                setattr(value, "mancoosimm_MimeTypeHandler", self)

    @property
    def mancoosimm_File259(self):
        return self.__mancoosimm_File259

    @mancoosimm_File259.setter
    def mancoosimm_File259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File259", None)
        self.__mancoosimm_File259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SkeeperDocument258"):
                opp_val = getattr(old_value, "mancoosimm_SkeeperDocument258", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SkeeperDocument258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SkeeperDocument258"):
                opp_val = getattr(value, "mancoosimm_SkeeperDocument258", None)
                setattr(value, "mancoosimm_SkeeperDocument258", self)

    @property
    def mancoosimm_File201(self):
        return self.__mancoosimm_File201

    @mancoosimm_File201.setter
    def mancoosimm_File201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File201", None)
        self.__mancoosimm_File201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_DesktopDB"):
                opp_val = getattr(old_value, "mancoosimm_DesktopDB", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_DesktopDB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_DesktopDB"):
                opp_val = getattr(value, "mancoosimm_DesktopDB", None)
                setattr(value, "mancoosimm_DesktopDB", self)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__root", None)
        self.__root = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileSystem165"):
                opp_val = getattr(old_value, "FileSystem165", None)
                if opp_val == self:
                    setattr(old_value, "FileSystem165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileSystem165"):
                opp_val = getattr(value, "FileSystem165", None)
                setattr(value, "FileSystem165", self)

    @property
    def mancoosimm_File154(self):
        return self.__mancoosimm_File154

    @mancoosimm_File154.setter
    def mancoosimm_File154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File154", None)
        self.__mancoosimm_File154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_MenuEntry"):
                opp_val = getattr(old_value, "mancoosimm_MenuEntry", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_MenuEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_MenuEntry"):
                opp_val = getattr(value, "mancoosimm_MenuEntry", None)
                setattr(value, "mancoosimm_MenuEntry", self)

    @property
    def mancoosimm_File173(self):
        return self.__mancoosimm_File173

    @mancoosimm_File173.setter
    def mancoosimm_File173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File173", None)
        self.__mancoosimm_File173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_User"):
                opp_val = getattr(old_value, "mancoosimm_User", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_User"):
                opp_val = getattr(value, "mancoosimm_User", None)
                setattr(value, "mancoosimm_User", self)

    @property
    def mancoosimm_File137(self):
        return self.__mancoosimm_File137

    @mancoosimm_File137.setter
    def mancoosimm_File137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File137", None)
        self.__mancoosimm_File137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_GConf"):
                opp_val = getattr(old_value, "mancoosimm_GConf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_GConf"):
                opp_val = getattr(value, "mancoosimm_GConf", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_GConf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def File168(self):
        return self.__File168

    @File168.setter
    def File168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File168", None)
        self.__File168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File231(self):
        return self.__mancoosimm_File231

    @mancoosimm_File231.setter
    def mancoosimm_File231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File231", None)
        self.__mancoosimm_File231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SharedLibrary"):
                opp_val = getattr(old_value, "mancoosimm_SharedLibrary", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SharedLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SharedLibrary"):
                opp_val = getattr(value, "mancoosimm_SharedLibrary", None)
                setattr(value, "mancoosimm_SharedLibrary", self)

    @property
    def mancoosimm_File140(self):
        return self.__mancoosimm_File140

    @mancoosimm_File140.setter
    def mancoosimm_File140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File140", None)
        self.__mancoosimm_File140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_GConf139"):
                opp_val = getattr(old_value, "mancoosimm_GConf139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_GConf139"):
                opp_val = getattr(value, "mancoosimm_GConf139", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_GConf139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mancoosimm_Module(NamedElement):

    pass
class mancoosimm_Service(NamedElement):

    pass
class mancoosimm_SGMLDocument(NamedElement):

    pass
class mancoosimm_Configuration(NamedElement):

    def __init__(self, creationTime: str, systemType: str, mancoosimm_Configuration: set["mancoosimm_InstalledPackage"] = None, mancoosimm_Configuration5: set["mancoosimm_NotInstalledPackage"] = None, mancoosimm_Configuration7: set["mancoosimm_ConfigFilesPackage"] = None, mancoosimm_Configuration9: set["mancoosimm_UnpackedPackage"] = None, mancoosimm_Configuration11: set["mancoosimm_HalfConfiguredPackage"] = None, mancoosimm_Configuration13: set["mancoosimm_HalfInstalledPackage"] = None, mancoosimm_Configuration15: set["mancoosimm_HalfConfiguredReinstRequiredPackage"] = None, mancoosimm_Configuration17: set["mancoosimm_HalfInstalledReinstRequiredPackage"] = None, mancoosimm_Configuration19: "mancoosimm_Package" = None, configuration: "mancoosimm_FileSystem" = None, configuration2: "mancoosimm_Environment" = None, Configuration: "mancoosimm_Environment" = None, Configuration133: "mancoosimm_FileSystem" = None):
        self.creationTime = creationTime
        self.systemType = systemType
        self.mancoosimm_Configuration = mancoosimm_Configuration if mancoosimm_Configuration is not None else set()
        self.mancoosimm_Configuration5 = mancoosimm_Configuration5 if mancoosimm_Configuration5 is not None else set()
        self.mancoosimm_Configuration7 = mancoosimm_Configuration7 if mancoosimm_Configuration7 is not None else set()
        self.mancoosimm_Configuration9 = mancoosimm_Configuration9 if mancoosimm_Configuration9 is not None else set()
        self.mancoosimm_Configuration11 = mancoosimm_Configuration11 if mancoosimm_Configuration11 is not None else set()
        self.mancoosimm_Configuration13 = mancoosimm_Configuration13 if mancoosimm_Configuration13 is not None else set()
        self.mancoosimm_Configuration15 = mancoosimm_Configuration15 if mancoosimm_Configuration15 is not None else set()
        self.mancoosimm_Configuration17 = mancoosimm_Configuration17 if mancoosimm_Configuration17 is not None else set()
        self.mancoosimm_Configuration19 = mancoosimm_Configuration19
        self.configuration = configuration
        self.configuration2 = configuration2
        self.Configuration = Configuration
        self.Configuration133 = Configuration133
        
    @property
    def systemType(self) -> str:
        return self.__systemType

    @systemType.setter
    def systemType(self, systemType: str):
        self.__systemType = systemType

    @property
    def creationTime(self) -> str:
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: str):
        self.__creationTime = creationTime

    @property
    def mancoosimm_Configuration17(self):
        return self.__mancoosimm_Configuration17

    @mancoosimm_Configuration17.setter
    def mancoosimm_Configuration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration17", None)
        self.__mancoosimm_Configuration17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage", None)
                    
                    setattr(item, "mancoosimm_HalfInstalledReinstRequiredPackage", self)
                    

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__configuration", None)
        self.__configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileSystem"):
                opp_val = getattr(old_value, "FileSystem", None)
                if opp_val == self:
                    setattr(old_value, "FileSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileSystem"):
                opp_val = getattr(value, "FileSystem", None)
                setattr(value, "FileSystem", self)

    @property
    def mancoosimm_Configuration13(self):
        return self.__mancoosimm_Configuration13

    @mancoosimm_Configuration13.setter
    def mancoosimm_Configuration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration13", None)
        self.__mancoosimm_Configuration13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_HalfInstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfInstalledPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_HalfInstalledPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_HalfInstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfInstalledPackage", None)
                    
                    setattr(item, "mancoosimm_HalfInstalledPackage", self)
                    

    @property
    def mancoosimm_Configuration5(self):
        return self.__mancoosimm_Configuration5

    @mancoosimm_Configuration5.setter
    def mancoosimm_Configuration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration5", None)
        self.__mancoosimm_Configuration5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_NotInstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_NotInstalledPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_NotInstalledPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_NotInstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_NotInstalledPackage", None)
                    
                    setattr(item, "mancoosimm_NotInstalledPackage", self)
                    

    @property
    def mancoosimm_Configuration(self):
        return self.__mancoosimm_Configuration

    @mancoosimm_Configuration.setter
    def mancoosimm_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration", None)
        self.__mancoosimm_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage", self)
                    

    @property
    def Configuration(self):
        return self.__Configuration

    @Configuration.setter
    def Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__Configuration", None)
        self.__Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "environment"):
                opp_val = getattr(old_value, "environment", None)
                if opp_val == self:
                    setattr(old_value, "environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "environment"):
                opp_val = getattr(value, "environment", None)
                setattr(value, "environment", self)

    @property
    def mancoosimm_Configuration11(self):
        return self.__mancoosimm_Configuration11

    @mancoosimm_Configuration11.setter
    def mancoosimm_Configuration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration11", None)
        self.__mancoosimm_Configuration11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_HalfConfiguredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfConfiguredPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_HalfConfiguredPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_HalfConfiguredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfConfiguredPackage", None)
                    
                    setattr(item, "mancoosimm_HalfConfiguredPackage", self)
                    

    @property
    def Configuration133(self):
        return self.__Configuration133

    @Configuration133.setter
    def Configuration133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__Configuration133", None)
        self.__Configuration133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fileSystem"):
                opp_val = getattr(old_value, "fileSystem", None)
                if opp_val == self:
                    setattr(old_value, "fileSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fileSystem"):
                opp_val = getattr(value, "fileSystem", None)
                setattr(value, "fileSystem", self)

    @property
    def configuration2(self):
        return self.__configuration2

    @configuration2.setter
    def configuration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__configuration2", None)
        self.__configuration2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment"):
                opp_val = getattr(old_value, "Environment", None)
                if opp_val == self:
                    setattr(old_value, "Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment"):
                opp_val = getattr(value, "Environment", None)
                setattr(value, "Environment", self)

    @property
    def mancoosimm_Configuration19(self):
        return self.__mancoosimm_Configuration19

    @mancoosimm_Configuration19.setter
    def mancoosimm_Configuration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration19", None)
        self.__mancoosimm_Configuration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Package"):
                opp_val = getattr(old_value, "mancoosimm_Package", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Package"):
                opp_val = getattr(value, "mancoosimm_Package", None)
                setattr(value, "mancoosimm_Package", self)

    @property
    def mancoosimm_Configuration7(self):
        return self.__mancoosimm_Configuration7

    @mancoosimm_Configuration7.setter
    def mancoosimm_Configuration7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration7", None)
        self.__mancoosimm_Configuration7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_ConfigFilesPackage"):
                    opp_val = getattr(item, "mancoosimm_ConfigFilesPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_ConfigFilesPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_ConfigFilesPackage"):
                    opp_val = getattr(item, "mancoosimm_ConfigFilesPackage", None)
                    
                    setattr(item, "mancoosimm_ConfigFilesPackage", self)
                    

    @property
    def mancoosimm_Configuration9(self):
        return self.__mancoosimm_Configuration9

    @mancoosimm_Configuration9.setter
    def mancoosimm_Configuration9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration9", None)
        self.__mancoosimm_Configuration9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_UnpackedPackage"):
                    opp_val = getattr(item, "mancoosimm_UnpackedPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_UnpackedPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_UnpackedPackage"):
                    opp_val = getattr(item, "mancoosimm_UnpackedPackage", None)
                    
                    setattr(item, "mancoosimm_UnpackedPackage", self)
                    

    @property
    def mancoosimm_Configuration15(self):
        return self.__mancoosimm_Configuration15

    @mancoosimm_Configuration15.setter
    def mancoosimm_Configuration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration15", None)
        self.__mancoosimm_Configuration15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage"):
                    opp_val = getattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage", None)
                    
                    setattr(item, "mancoosimm_HalfConfiguredReinstRequiredPackage", self)
                    

class mancoosimm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

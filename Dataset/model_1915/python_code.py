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
    config_files = "config_files"
    unpacked = "unpacked"
class PriorityType(Enum):
    standard = "standard"
    required = "required"
    important = "important"
    optional = "optional"
    extra = "extra"
class VersionType(Enum):
    eq = "eq"
    ge = "ge"
    le = "le"
    lt = "lt"
    llt = "llt"
    gt = "gt"
    ggt = "ggt"


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

    def __init__(self, version: str, value: str, singleConflict: "mancoosimm_Conflict" = None, SingleConflict: "mancoosimm_Conflict" = None):
        self.version = version
        self.value = value
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
            if hasattr(old_value, "conflict278"):
                opp_val = getattr(old_value, "conflict278", None)
                if opp_val == self:
                    setattr(old_value, "conflict278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conflict278"):
                opp_val = getattr(value, "conflict278", None)
                setattr(value, "conflict278", self)

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
    def mancoosimm_SharedLibrary(self):
        return self.__mancoosimm_SharedLibrary

    @mancoosimm_SharedLibrary.setter
    def mancoosimm_SharedLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_SharedLibrary__mancoosimm_SharedLibrary", None)
        self.__mancoosimm_SharedLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_File227"):
                opp_val = getattr(old_value, "mancoosimm_File227", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_File227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_File227"):
                opp_val = getattr(value, "mancoosimm_File227", None)
                setattr(value, "mancoosimm_File227", self)

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
            if hasattr(old_value, "LibraryCache229"):
                opp_val = getattr(old_value, "LibraryCache229", None)
                if opp_val == self:
                    setattr(old_value, "LibraryCache229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LibraryCache229"):
                opp_val = getattr(value, "LibraryCache229", None)
                setattr(value, "LibraryCache229", self)

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

class mancoosimm_MimeType:

    def __init__(self, name: str, extension: str, MimeType: "mancoosimm_MimeTypeHandlerCache" = None, MimeType206: "mancoosimm_MimeTypeHandler" = None, type: set["mancoosimm_MimeTypeHandler"] = None, mimeTypes: "mancoosimm_MimeTypeHandlerCache" = None):
        self.name = name
        self.extension = extension
        self.MimeType = MimeType
        self.MimeType206 = MimeType206
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
    def MimeType206(self):
        return self.__MimeType206

    @MimeType206.setter
    def MimeType206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__MimeType206", None)
        self.__MimeType206 = value
        
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
    def MimeType(self):
        return self.__MimeType

    @MimeType.setter
    def MimeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_MimeType__MimeType", None)
        self.__MimeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cache202"):
                opp_val = getattr(old_value, "cache202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cache202"):
                opp_val = getattr(value, "cache202", None)
                if opp_val is None:
                    setattr(value, "cache202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "MimeTypeHandlerCache212"):
                opp_val = getattr(old_value, "MimeTypeHandlerCache212", None)
                if opp_val == self:
                    setattr(old_value, "MimeTypeHandlerCache212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MimeTypeHandlerCache212"):
                opp_val = getattr(value, "MimeTypeHandlerCache212", None)
                setattr(value, "MimeTypeHandlerCache212", self)

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
                if hasattr(item, "MimeTypeHandler210"):
                    opp_val = getattr(item, "MimeTypeHandler210", None)
                    
                    if opp_val == self:
                        setattr(item, "MimeTypeHandler210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MimeTypeHandler210"):
                    opp_val = getattr(item, "MimeTypeHandler210", None)
                    
                    setattr(item, "MimeTypeHandler210", self)
                    

class mancoosimm_MimeTypeHandler:

    pass
class File:

    pass
class mancoosimm_InformationFile(File):

    pass
class mancoosimm_Boot:

    pass
class mancoosimm_XFontCache:

    def __init__(self, location: str, XFontCache: "mancoosimm_Environment" = None, xfontCache: set["mancoosimm_XFont"] = None, xfontCaches: "mancoosimm_Environment" = None, XFontCache217: "mancoosimm_XFont" = None):
        self.location = location
        self.XFontCache = XFontCache
        self.xfontCache = xfontCache if xfontCache is not None else set()
        self.xfontCaches = xfontCaches
        self.XFontCache217 = XFontCache217
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
            if hasattr(old_value, "env122"):
                opp_val = getattr(old_value, "env122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env122"):
                opp_val = getattr(value, "env122", None)
                if opp_val is None:
                    setattr(value, "env122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def XFontCache217(self):
        return self.__XFontCache217

    @XFontCache217.setter
    def XFontCache217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__XFontCache217", None)
        self.__XFontCache217 = value
        
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
    def xfontCaches(self):
        return self.__xfontCaches

    @xfontCaches.setter
    def xfontCaches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_XFontCache__xfontCaches", None)
        self.__xfontCaches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment215"):
                opp_val = getattr(old_value, "Environment215", None)
                if opp_val == self:
                    setattr(old_value, "Environment215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment215"):
                opp_val = getattr(value, "Environment215", None)
                setattr(value, "Environment215", self)

class mancoosimm_ModuleCache:

    def __init__(self, version: str, ModuleCache: "mancoosimm_Environment" = None, moduleCache: set["mancoosimm_Module"] = None, moduleCache232: "mancoosimm_Environment" = None, ModuleCache237: "mancoosimm_Module" = None):
        self.version = version
        self.ModuleCache = ModuleCache
        self.moduleCache = moduleCache if moduleCache is not None else set()
        self.moduleCache232 = moduleCache232
        self.ModuleCache237 = ModuleCache237
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def moduleCache232(self):
        return self.__moduleCache232

    @moduleCache232.setter
    def moduleCache232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__moduleCache232", None)
        self.__moduleCache232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment233"):
                opp_val = getattr(old_value, "Environment233", None)
                if opp_val == self:
                    setattr(old_value, "Environment233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment233"):
                opp_val = getattr(value, "Environment233", None)
                setattr(value, "Environment233", self)

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
            if hasattr(old_value, "env120"):
                opp_val = getattr(old_value, "env120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env120"):
                opp_val = getattr(value, "env120", None)
                if opp_val is None:
                    setattr(value, "env120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ModuleCache237(self):
        return self.__ModuleCache237

    @ModuleCache237.setter
    def ModuleCache237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_ModuleCache__ModuleCache237", None)
        self.__ModuleCache237 = value
        
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
                    

class mancoosimm_Menu:

    pass
class mancoosimm_GConf:

    pass
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
    def iconCache(self):
        return self.__iconCache

    @iconCache.setter
    def iconCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_IconCache__iconCache", None)
        self.__iconCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Environment191"):
                opp_val = getattr(old_value, "Environment191", None)
                if opp_val == self:
                    setattr(old_value, "Environment191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Environment191"):
                opp_val = getattr(value, "Environment191", None)
                setattr(value, "Environment191", self)

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
            if hasattr(old_value, "env107"):
                opp_val = getattr(old_value, "env107", None)
                if opp_val == self:
                    setattr(old_value, "env107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "env107"):
                opp_val = getattr(value, "env107", None)
                setattr(value, "env107", self)

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
            if hasattr(old_value, "mancoosimm_File193"):
                opp_val = getattr(old_value, "mancoosimm_File193", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_File193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_File193"):
                opp_val = getattr(value, "mancoosimm_File193", None)
                setattr(value, "mancoosimm_File193", self)

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
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "Dependence74"):
                opp_val = getattr(old_value, "Dependence74", None)
                if opp_val == self:
                    setattr(old_value, "Dependence74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dependence74"):
                opp_val = getattr(value, "Dependence74", None)
                setattr(value, "Dependence74", self)

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
            if hasattr(old_value, "dependence62"):
                opp_val = getattr(old_value, "dependence62", None)
                if opp_val == self:
                    setattr(old_value, "dependence62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependence62"):
                opp_val = getattr(value, "dependence62", None)
                setattr(value, "dependence62", self)

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
class mancoosimm_HalfConfiguredPackage(UnpackedPackage):

    pass
class Package:

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
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

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
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

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

class mancoosimm_UnpackedPackage(Package):

    def __init__(self, priority: str, uploaders: str, maintainer: str, checkSum: str, description: str, section: str, tag: str, mancoosimm_UnpackedPackage: "mancoosimm_Configuration" = None, mancoosimm_UnpackedPackage45: set["mancoosimm_File"] = None):
        self.priority = priority
        self.uploaders = uploaders
        self.maintainer = maintainer
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.mancoosimm_UnpackedPackage = mancoosimm_UnpackedPackage
        self.mancoosimm_UnpackedPackage45 = mancoosimm_UnpackedPackage45 if mancoosimm_UnpackedPackage45 is not None else set()
        
    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def section(self) -> str:
        return self.__section

    @section.setter
    def section(self, section: str):
        self.__section = section

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
    def mancoosimm_UnpackedPackage45(self):
        return self.__mancoosimm_UnpackedPackage45

    @mancoosimm_UnpackedPackage45.setter
    def mancoosimm_UnpackedPackage45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_UnpackedPackage__mancoosimm_UnpackedPackage45", None)
        self.__mancoosimm_UnpackedPackage45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_File46"):
                    opp_val = getattr(item, "mancoosimm_File46", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_File46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_File46"):
                    opp_val = getattr(item, "mancoosimm_File46", None)
                    
                    setattr(item, "mancoosimm_File46", self)
                    

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

class mancoosimm_InstalledPackage(Package):

    def __init__(self, installedSize: int, maintainer: str, fileSize: int, checkSum: str, description: str, section: str, tag: str, priority: str, uploaders: str, mancoosimm_InstalledPackage: "mancoosimm_Configuration" = None, mancoosimm_InstalledPackage23: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage21: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage26: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage24: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage29: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage27: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage18: "mancoosimm_SrcPackage" = None, mancoosimm_InstalledPackage20: "mancoosimm_Dependence" = None, mancoosimm_InstalledPackage32: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage30: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage34: "mancoosimm_VirtualPackage" = None, mancoosimm_InstalledPackage37: "mancoosimm_InstalledPackage" = None, mancoosimm_InstalledPackage35: set["mancoosimm_InstalledPackage"] = None, mancoosimm_InstalledPackage39: set["mancoosimm_File"] = None, pkg41: set["mancoosimm_DocumentationFile"] = None, mancoosimm_InstalledPackage43: "mancoosimm_Conflict" = None, mancoosimm_InstalledPackage57: "mancoosimm_VirtualPackage" = None, InstalledPackage: "mancoosimm_DocumentationFile" = None):
        self.installedSize = installedSize
        self.maintainer = maintainer
        self.fileSize = fileSize
        self.checkSum = checkSum
        self.description = description
        self.section = section
        self.tag = tag
        self.priority = priority
        self.uploaders = uploaders
        self.mancoosimm_InstalledPackage = mancoosimm_InstalledPackage
        self.mancoosimm_InstalledPackage23 = mancoosimm_InstalledPackage23
        self.mancoosimm_InstalledPackage21 = mancoosimm_InstalledPackage21 if mancoosimm_InstalledPackage21 is not None else set()
        self.mancoosimm_InstalledPackage26 = mancoosimm_InstalledPackage26
        self.mancoosimm_InstalledPackage24 = mancoosimm_InstalledPackage24 if mancoosimm_InstalledPackage24 is not None else set()
        self.mancoosimm_InstalledPackage29 = mancoosimm_InstalledPackage29
        self.mancoosimm_InstalledPackage27 = mancoosimm_InstalledPackage27 if mancoosimm_InstalledPackage27 is not None else set()
        self.mancoosimm_InstalledPackage18 = mancoosimm_InstalledPackage18
        self.mancoosimm_InstalledPackage20 = mancoosimm_InstalledPackage20
        self.mancoosimm_InstalledPackage32 = mancoosimm_InstalledPackage32
        self.mancoosimm_InstalledPackage30 = mancoosimm_InstalledPackage30 if mancoosimm_InstalledPackage30 is not None else set()
        self.mancoosimm_InstalledPackage34 = mancoosimm_InstalledPackage34
        self.mancoosimm_InstalledPackage37 = mancoosimm_InstalledPackage37
        self.mancoosimm_InstalledPackage35 = mancoosimm_InstalledPackage35 if mancoosimm_InstalledPackage35 is not None else set()
        self.mancoosimm_InstalledPackage39 = mancoosimm_InstalledPackage39 if mancoosimm_InstalledPackage39 is not None else set()
        self.pkg41 = pkg41 if pkg41 is not None else set()
        self.mancoosimm_InstalledPackage43 = mancoosimm_InstalledPackage43
        self.mancoosimm_InstalledPackage57 = mancoosimm_InstalledPackage57
        self.InstalledPackage = InstalledPackage
        
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
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def installedSize(self) -> int:
        return self.__installedSize

    @installedSize.setter
    def installedSize(self, installedSize: int):
        self.__installedSize = installedSize

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

    @property
    def fileSize(self) -> int:
        return self.__fileSize

    @fileSize.setter
    def fileSize(self, fileSize: int):
        self.__fileSize = fileSize

    @property
    def mancoosimm_InstalledPackage32(self):
        return self.__mancoosimm_InstalledPackage32

    @mancoosimm_InstalledPackage32.setter
    def mancoosimm_InstalledPackage32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage32", None)
        self.__mancoosimm_InstalledPackage32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage30"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage30"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage30", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage34(self):
        return self.__mancoosimm_InstalledPackage34

    @mancoosimm_InstalledPackage34.setter
    def mancoosimm_InstalledPackage34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage34", None)
        self.__mancoosimm_InstalledPackage34 = value
        
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
    def mancoosimm_InstalledPackage24(self):
        return self.__mancoosimm_InstalledPackage24

    @mancoosimm_InstalledPackage24.setter
    def mancoosimm_InstalledPackage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage24", None)
        self.__mancoosimm_InstalledPackage24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage26"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage26", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage26"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage26", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage26", self)
                    

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
    def mancoosimm_InstalledPackage37(self):
        return self.__mancoosimm_InstalledPackage37

    @mancoosimm_InstalledPackage37.setter
    def mancoosimm_InstalledPackage37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage37", None)
        self.__mancoosimm_InstalledPackage37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage35"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage35"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage35", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage35", set([self]))
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
    def mancoosimm_InstalledPackage23(self):
        return self.__mancoosimm_InstalledPackage23

    @mancoosimm_InstalledPackage23.setter
    def mancoosimm_InstalledPackage23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage23", None)
        self.__mancoosimm_InstalledPackage23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage21"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage21"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage21", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage27(self):
        return self.__mancoosimm_InstalledPackage27

    @mancoosimm_InstalledPackage27.setter
    def mancoosimm_InstalledPackage27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage27", None)
        self.__mancoosimm_InstalledPackage27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage29"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage29", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage29"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage29", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage29", self)
                    

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
    def mancoosimm_InstalledPackage21(self):
        return self.__mancoosimm_InstalledPackage21

    @mancoosimm_InstalledPackage21.setter
    def mancoosimm_InstalledPackage21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage21", None)
        self.__mancoosimm_InstalledPackage21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage23"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage23", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage23"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage23", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage23", self)
                    

    @property
    def mancoosimm_InstalledPackage18(self):
        return self.__mancoosimm_InstalledPackage18

    @mancoosimm_InstalledPackage18.setter
    def mancoosimm_InstalledPackage18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage18", None)
        self.__mancoosimm_InstalledPackage18 = value
        
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
    def mancoosimm_InstalledPackage30(self):
        return self.__mancoosimm_InstalledPackage30

    @mancoosimm_InstalledPackage30.setter
    def mancoosimm_InstalledPackage30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage30", None)
        self.__mancoosimm_InstalledPackage30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage32"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage32", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage32"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage32", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage32", self)
                    

    @property
    def mancoosimm_InstalledPackage26(self):
        return self.__mancoosimm_InstalledPackage26

    @mancoosimm_InstalledPackage26.setter
    def mancoosimm_InstalledPackage26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage26", None)
        self.__mancoosimm_InstalledPackage26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage24"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage24"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage24", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage35(self):
        return self.__mancoosimm_InstalledPackage35

    @mancoosimm_InstalledPackage35.setter
    def mancoosimm_InstalledPackage35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage35", None)
        self.__mancoosimm_InstalledPackage35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mancoosimm_InstalledPackage37"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage37", None)
                    
                    if opp_val == self:
                        setattr(item, "mancoosimm_InstalledPackage37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mancoosimm_InstalledPackage37"):
                    opp_val = getattr(item, "mancoosimm_InstalledPackage37", None)
                    
                    setattr(item, "mancoosimm_InstalledPackage37", self)
                    

    @property
    def mancoosimm_InstalledPackage57(self):
        return self.__mancoosimm_InstalledPackage57

    @mancoosimm_InstalledPackage57.setter
    def mancoosimm_InstalledPackage57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage57", None)
        self.__mancoosimm_InstalledPackage57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_VirtualPackage56"):
                opp_val = getattr(old_value, "mancoosimm_VirtualPackage56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_VirtualPackage56"):
                opp_val = getattr(value, "mancoosimm_VirtualPackage56", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_VirtualPackage56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_InstalledPackage43(self):
        return self.__mancoosimm_InstalledPackage43

    @mancoosimm_InstalledPackage43.setter
    def mancoosimm_InstalledPackage43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage43", None)
        self.__mancoosimm_InstalledPackage43 = value
        
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
    def pkg41(self):
        return self.__pkg41

    @pkg41.setter
    def pkg41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__pkg41", None)
        self.__pkg41 = value if value is not None else set()
        
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
    def mancoosimm_InstalledPackage20(self):
        return self.__mancoosimm_InstalledPackage20

    @mancoosimm_InstalledPackage20.setter
    def mancoosimm_InstalledPackage20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage20", None)
        self.__mancoosimm_InstalledPackage20 = value
        
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
    def mancoosimm_InstalledPackage29(self):
        return self.__mancoosimm_InstalledPackage29

    @mancoosimm_InstalledPackage29.setter
    def mancoosimm_InstalledPackage29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_InstalledPackage__mancoosimm_InstalledPackage29", None)
        self.__mancoosimm_InstalledPackage29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_InstalledPackage27"):
                opp_val = getattr(old_value, "mancoosimm_InstalledPackage27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_InstalledPackage27"):
                opp_val = getattr(value, "mancoosimm_InstalledPackage27", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_InstalledPackage27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class mancoosimm_Environment(NamedElement):

    pass
class mancoosimm_SkeeperDocument(NamedElement):

    pass
class mancoosimm_Group(NamedElement):

    pass
class mancoosimm_Invariant(NamedElement):

    pass
class mancoosimm_ApplicationMenuCatalog(NamedElement):

    pass
class mancoosimm_Atom(NamedElement):

    pass
class mancoosimm_SGMLCatalog(NamedElement):

    pass
class mancoosimm_Alternative(NamedElement):

    pass
class mancoosimm_Service(NamedElement):

    pass
class mancoosimm_Module(NamedElement):

    pass
class mancoosimm_File(NamedElement):

    def __init__(self, size: int, extension: str, description: str, checkSum: str, isDirectory: bool, suid: bool, guid: bool, permission: str, location: str, isMissing: bool, mancoosimm_File: "mancoosimm_InstalledPackage" = None, mancoosimm_File46: "mancoosimm_UnpackedPackage" = None, File: "mancoosimm_FileSystem" = None, mancoosimm_File131: "mancoosimm_FileSystem" = None, mancoosimm_File133: "mancoosimm_GConf" = None, mancoosimm_File136: "mancoosimm_GConf" = None, mancoosimm_File150: "mancoosimm_MenuEntry" = None, mancoosimm_File157: "mancoosimm_Service" = None, File164: "mancoosimm_File" = None, root: "mancoosimm_FileSystem" = None, files: set["mancoosimm_PackageSetting"] = None, parent: set["mancoosimm_File"] = None, File167: "mancoosimm_File" = None, childs: "mancoosimm_File" = None, mancoosimm_File169: "mancoosimm_User" = None, mancoosimm_File171: "mancoosimm_Group" = None, mancoosimm_File176: "mancoosimm_Alternative" = None, mancoosimm_File179: "mancoosimm_Alternative" = None, File185: "mancoosimm_PackageSetting" = None, mancoosimm_File193: "mancoosimm_IconCache" = None, mancoosimm_File204: "mancoosimm_MimeTypeHandler" = None, mancoosimm_File197: "mancoosimm_DesktopDB" = None, mancoosimm_File219: "mancoosimm_XFont" = None, mancoosimm_File221: "mancoosimm_LibraryCache" = None, mancoosimm_File227: "mancoosimm_SharedLibrary" = None, mancoosimm_File235: "mancoosimm_Module" = None, mancoosimm_File243: "mancoosimm_SGMLDocument" = None, mancoosimm_File246: "mancoosimm_SGMLDocument" = None, mancoosimm_File252: "mancoosimm_SkeeperDocument" = None, mancoosimm_File255: "mancoosimm_SkeeperDocument" = None, mancoosimm_File257: "mancoosimm_EmacsPackage" = None, mancoosimm_File267: "mancoosimm_User" = None):
        self.size = size
        self.extension = extension
        self.description = description
        self.checkSum = checkSum
        self.isDirectory = isDirectory
        self.suid = suid
        self.guid = guid
        self.permission = permission
        self.location = location
        self.isMissing = isMissing
        self.mancoosimm_File = mancoosimm_File
        self.mancoosimm_File46 = mancoosimm_File46
        self.File = File
        self.mancoosimm_File131 = mancoosimm_File131
        self.mancoosimm_File133 = mancoosimm_File133
        self.mancoosimm_File136 = mancoosimm_File136
        self.mancoosimm_File150 = mancoosimm_File150
        self.mancoosimm_File157 = mancoosimm_File157
        self.File164 = File164
        self.root = root
        self.files = files if files is not None else set()
        self.parent = parent if parent is not None else set()
        self.File167 = File167
        self.childs = childs
        self.mancoosimm_File169 = mancoosimm_File169
        self.mancoosimm_File171 = mancoosimm_File171
        self.mancoosimm_File176 = mancoosimm_File176
        self.mancoosimm_File179 = mancoosimm_File179
        self.File185 = File185
        self.mancoosimm_File193 = mancoosimm_File193
        self.mancoosimm_File204 = mancoosimm_File204
        self.mancoosimm_File197 = mancoosimm_File197
        self.mancoosimm_File219 = mancoosimm_File219
        self.mancoosimm_File221 = mancoosimm_File221
        self.mancoosimm_File227 = mancoosimm_File227
        self.mancoosimm_File235 = mancoosimm_File235
        self.mancoosimm_File243 = mancoosimm_File243
        self.mancoosimm_File246 = mancoosimm_File246
        self.mancoosimm_File252 = mancoosimm_File252
        self.mancoosimm_File255 = mancoosimm_File255
        self.mancoosimm_File257 = mancoosimm_File257
        self.mancoosimm_File267 = mancoosimm_File267
        
    @property
    def suid(self) -> bool:
        return self.__suid

    @suid.setter
    def suid(self, suid: bool):
        self.__suid = suid

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def permission(self) -> str:
        return self.__permission

    @permission.setter
    def permission(self, permission: str):
        self.__permission = permission

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def isMissing(self) -> bool:
        return self.__isMissing

    @isMissing.setter
    def isMissing(self, isMissing: bool):
        self.__isMissing = isMissing

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def guid(self) -> bool:
        return self.__guid

    @guid.setter
    def guid(self, guid: bool):
        self.__guid = guid

    @property
    def isDirectory(self) -> bool:
        return self.__isDirectory

    @isDirectory.setter
    def isDirectory(self, isDirectory: bool):
        self.__isDirectory = isDirectory

    @property
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def mancoosimm_File235(self):
        return self.__mancoosimm_File235

    @mancoosimm_File235.setter
    def mancoosimm_File235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File235", None)
        self.__mancoosimm_File235 = value
        
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
    def mancoosimm_File267(self):
        return self.__mancoosimm_File267

    @mancoosimm_File267.setter
    def mancoosimm_File267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File267", None)
        self.__mancoosimm_File267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_User266"):
                opp_val = getattr(old_value, "mancoosimm_User266", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_User266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_User266"):
                opp_val = getattr(value, "mancoosimm_User266", None)
                setattr(value, "mancoosimm_User266", self)

    @property
    def mancoosimm_File133(self):
        return self.__mancoosimm_File133

    @mancoosimm_File133.setter
    def mancoosimm_File133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File133", None)
        self.__mancoosimm_File133 = value
        
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
    def File167(self):
        return self.__File167

    @File167.setter
    def File167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File167", None)
        self.__File167 = value
        
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
    def mancoosimm_File46(self):
        return self.__mancoosimm_File46

    @mancoosimm_File46.setter
    def mancoosimm_File46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File46", None)
        self.__mancoosimm_File46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_UnpackedPackage45"):
                opp_val = getattr(old_value, "mancoosimm_UnpackedPackage45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_UnpackedPackage45"):
                opp_val = getattr(value, "mancoosimm_UnpackedPackage45", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_UnpackedPackage45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mancoosimm_File257(self):
        return self.__mancoosimm_File257

    @mancoosimm_File257.setter
    def mancoosimm_File257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File257", None)
        self.__mancoosimm_File257 = value
        
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
    def childs(self):
        return self.__childs

    @childs.setter
    def childs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__childs", None)
        self.__childs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File167"):
                opp_val = getattr(old_value, "File167", None)
                if opp_val == self:
                    setattr(old_value, "File167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File167"):
                opp_val = getattr(value, "File167", None)
                setattr(value, "File167", self)

    @property
    def mancoosimm_File171(self):
        return self.__mancoosimm_File171

    @mancoosimm_File171.setter
    def mancoosimm_File171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File171", None)
        self.__mancoosimm_File171 = value
        
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
    def mancoosimm_File193(self):
        return self.__mancoosimm_File193

    @mancoosimm_File193.setter
    def mancoosimm_File193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File193", None)
        self.__mancoosimm_File193 = value
        
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
    def mancoosimm_File197(self):
        return self.__mancoosimm_File197

    @mancoosimm_File197.setter
    def mancoosimm_File197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File197", None)
        self.__mancoosimm_File197 = value
        
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
    def File185(self):
        return self.__File185

    @File185.setter
    def File185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File185", None)
        self.__File185 = value
        
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
    def mancoosimm_File255(self):
        return self.__mancoosimm_File255

    @mancoosimm_File255.setter
    def mancoosimm_File255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File255", None)
        self.__mancoosimm_File255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SkeeperDocument254"):
                opp_val = getattr(old_value, "mancoosimm_SkeeperDocument254", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SkeeperDocument254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SkeeperDocument254"):
                opp_val = getattr(value, "mancoosimm_SkeeperDocument254", None)
                setattr(value, "mancoosimm_SkeeperDocument254", self)

    @property
    def mancoosimm_File179(self):
        return self.__mancoosimm_File179

    @mancoosimm_File179.setter
    def mancoosimm_File179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File179", None)
        self.__mancoosimm_File179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Alternative178"):
                opp_val = getattr(old_value, "mancoosimm_Alternative178", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Alternative178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Alternative178"):
                opp_val = getattr(value, "mancoosimm_Alternative178", None)
                setattr(value, "mancoosimm_Alternative178", self)

    @property
    def mancoosimm_File176(self):
        return self.__mancoosimm_File176

    @mancoosimm_File176.setter
    def mancoosimm_File176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File176", None)
        self.__mancoosimm_File176 = value
        
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
    def File164(self):
        return self.__File164

    @File164.setter
    def File164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__File164", None)
        self.__File164 = value
        
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
    def mancoosimm_File204(self):
        return self.__mancoosimm_File204

    @mancoosimm_File204.setter
    def mancoosimm_File204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File204", None)
        self.__mancoosimm_File204 = value
        
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
    def mancoosimm_File(self):
        return self.__mancoosimm_File

    @mancoosimm_File.setter
    def mancoosimm_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File", None)
        self.__mancoosimm_File = value
        
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
                if hasattr(item, "PackageSetting173"):
                    opp_val = getattr(item, "PackageSetting173", None)
                    
                    if opp_val == self:
                        setattr(item, "PackageSetting173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PackageSetting173"):
                    opp_val = getattr(item, "PackageSetting173", None)
                    
                    setattr(item, "PackageSetting173", self)
                    

    @property
    def mancoosimm_File252(self):
        return self.__mancoosimm_File252

    @mancoosimm_File252.setter
    def mancoosimm_File252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File252", None)
        self.__mancoosimm_File252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SkeeperDocument251"):
                opp_val = getattr(old_value, "mancoosimm_SkeeperDocument251", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SkeeperDocument251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SkeeperDocument251"):
                opp_val = getattr(value, "mancoosimm_SkeeperDocument251", None)
                setattr(value, "mancoosimm_SkeeperDocument251", self)

    @property
    def mancoosimm_File136(self):
        return self.__mancoosimm_File136

    @mancoosimm_File136.setter
    def mancoosimm_File136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File136", None)
        self.__mancoosimm_File136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_GConf135"):
                opp_val = getattr(old_value, "mancoosimm_GConf135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_GConf135"):
                opp_val = getattr(value, "mancoosimm_GConf135", None)
                if opp_val is None:
                    setattr(value, "mancoosimm_GConf135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "FileSystem161"):
                opp_val = getattr(old_value, "FileSystem161", None)
                if opp_val == self:
                    setattr(old_value, "FileSystem161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileSystem161"):
                opp_val = getattr(value, "FileSystem161", None)
                setattr(value, "FileSystem161", self)

    @property
    def mancoosimm_File221(self):
        return self.__mancoosimm_File221

    @mancoosimm_File221.setter
    def mancoosimm_File221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File221", None)
        self.__mancoosimm_File221 = value
        
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
    def mancoosimm_File227(self):
        return self.__mancoosimm_File227

    @mancoosimm_File227.setter
    def mancoosimm_File227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File227", None)
        self.__mancoosimm_File227 = value
        
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
    def mancoosimm_File246(self):
        return self.__mancoosimm_File246

    @mancoosimm_File246.setter
    def mancoosimm_File246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File246", None)
        self.__mancoosimm_File246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SGMLDocument245"):
                opp_val = getattr(old_value, "mancoosimm_SGMLDocument245", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SGMLDocument245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SGMLDocument245"):
                opp_val = getattr(value, "mancoosimm_SGMLDocument245", None)
                setattr(value, "mancoosimm_SGMLDocument245", self)

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
                if hasattr(item, "File164"):
                    opp_val = getattr(item, "File164", None)
                    
                    if opp_val == self:
                        setattr(item, "File164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File164"):
                    opp_val = getattr(item, "File164", None)
                    
                    setattr(item, "File164", self)
                    

    @property
    def mancoosimm_File169(self):
        return self.__mancoosimm_File169

    @mancoosimm_File169.setter
    def mancoosimm_File169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File169", None)
        self.__mancoosimm_File169 = value
        
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
    def mancoosimm_File157(self):
        return self.__mancoosimm_File157

    @mancoosimm_File157.setter
    def mancoosimm_File157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File157", None)
        self.__mancoosimm_File157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Service156"):
                opp_val = getattr(old_value, "mancoosimm_Service156", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Service156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Service156"):
                opp_val = getattr(value, "mancoosimm_Service156", None)
                setattr(value, "mancoosimm_Service156", self)

    @property
    def mancoosimm_File243(self):
        return self.__mancoosimm_File243

    @mancoosimm_File243.setter
    def mancoosimm_File243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File243", None)
        self.__mancoosimm_File243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_SGMLDocument242"):
                opp_val = getattr(old_value, "mancoosimm_SGMLDocument242", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_SGMLDocument242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_SGMLDocument242"):
                opp_val = getattr(value, "mancoosimm_SGMLDocument242", None)
                setattr(value, "mancoosimm_SGMLDocument242", self)

    @property
    def mancoosimm_File131(self):
        return self.__mancoosimm_File131

    @mancoosimm_File131.setter
    def mancoosimm_File131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File131", None)
        self.__mancoosimm_File131 = value
        
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
    def mancoosimm_File219(self):
        return self.__mancoosimm_File219

    @mancoosimm_File219.setter
    def mancoosimm_File219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File219", None)
        self.__mancoosimm_File219 = value
        
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
    def mancoosimm_File150(self):
        return self.__mancoosimm_File150

    @mancoosimm_File150.setter
    def mancoosimm_File150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_File__mancoosimm_File150", None)
        self.__mancoosimm_File150 = value
        
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

class mancoosimm_PackageSetting(NamedElement):

    pass
class mancoosimm_SkeeperCatalog(NamedElement):

    pass
class mancoosimm_SGMLDocument(NamedElement):

    pass
class mancoosimm_MenuEntry(NamedElement):

    pass
class mancoosimm_Package(NamedElement):

    def __init__(self, architecture: str, version: str, pkg: "mancoosimm_PackageSetting" = None, mancoosimm_Package: "mancoosimm_Configuration" = None, mancoosimm_Package65: "mancoosimm_Dependence" = None, Package: "mancoosimm_PackageSetting" = None, mancoosimm_Package281: "mancoosimm_Conflict" = None):
        self.architecture = architecture
        self.version = version
        self.pkg = pkg
        self.mancoosimm_Package = mancoosimm_Package
        self.mancoosimm_Package65 = mancoosimm_Package65
        self.Package = Package
        self.mancoosimm_Package281 = mancoosimm_Package281
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def architecture(self) -> str:
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture

    @property
    def mancoosimm_Package65(self):
        return self.__mancoosimm_Package65

    @mancoosimm_Package65.setter
    def mancoosimm_Package65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__mancoosimm_Package65", None)
        self.__mancoosimm_Package65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Dependence64"):
                opp_val = getattr(old_value, "mancoosimm_Dependence64", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Dependence64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Dependence64"):
                opp_val = getattr(value, "mancoosimm_Dependence64", None)
                setattr(value, "mancoosimm_Dependence64", self)

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
            if hasattr(old_value, "mancoosimm_Configuration15"):
                opp_val = getattr(old_value, "mancoosimm_Configuration15", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Configuration15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Configuration15"):
                opp_val = getattr(value, "mancoosimm_Configuration15", None)
                setattr(value, "mancoosimm_Configuration15", self)

    @property
    def mancoosimm_Package281(self):
        return self.__mancoosimm_Package281

    @mancoosimm_Package281.setter
    def mancoosimm_Package281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Package__mancoosimm_Package281", None)
        self.__mancoosimm_Package281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mancoosimm_Conflict280"):
                opp_val = getattr(old_value, "mancoosimm_Conflict280", None)
                if opp_val == self:
                    setattr(old_value, "mancoosimm_Conflict280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mancoosimm_Conflict280"):
                opp_val = getattr(value, "mancoosimm_Conflict280", None)
                setattr(value, "mancoosimm_Conflict280", self)

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

class mancoosimm_EmacsPackage(NamedElement):

    pass
class mancoosimm_User(NamedElement):

    pass
class mancoosimm_FileSystem(NamedElement):

    pass
class mancoosimm_XFont(NamedElement):

    pass
class mancoosimm_Configuration(NamedElement):

    def __init__(self, creationTime: str, systemType: str, mancoosimm_Configuration: set["mancoosimm_InstalledPackage"] = None, mancoosimm_Configuration5: set["mancoosimm_NotInstalledPackage"] = None, mancoosimm_Configuration7: set["mancoosimm_ConfigFilesPackage"] = None, configuration: "mancoosimm_FileSystem" = None, configuration2: "mancoosimm_Environment" = None, mancoosimm_Configuration9: set["mancoosimm_UnpackedPackage"] = None, mancoosimm_Configuration11: set["mancoosimm_HalfConfiguredPackage"] = None, mancoosimm_Configuration13: set["mancoosimm_HalfInstalledPackage"] = None, mancoosimm_Configuration15: "mancoosimm_Package" = None, Configuration: "mancoosimm_Environment" = None, Configuration129: "mancoosimm_FileSystem" = None):
        self.creationTime = creationTime
        self.systemType = systemType
        self.mancoosimm_Configuration = mancoosimm_Configuration if mancoosimm_Configuration is not None else set()
        self.mancoosimm_Configuration5 = mancoosimm_Configuration5 if mancoosimm_Configuration5 is not None else set()
        self.mancoosimm_Configuration7 = mancoosimm_Configuration7 if mancoosimm_Configuration7 is not None else set()
        self.configuration = configuration
        self.configuration2 = configuration2
        self.mancoosimm_Configuration9 = mancoosimm_Configuration9 if mancoosimm_Configuration9 is not None else set()
        self.mancoosimm_Configuration11 = mancoosimm_Configuration11 if mancoosimm_Configuration11 is not None else set()
        self.mancoosimm_Configuration13 = mancoosimm_Configuration13 if mancoosimm_Configuration13 is not None else set()
        self.mancoosimm_Configuration15 = mancoosimm_Configuration15
        self.Configuration = Configuration
        self.Configuration129 = Configuration129
        
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
    def mancoosimm_Configuration15(self):
        return self.__mancoosimm_Configuration15

    @mancoosimm_Configuration15.setter
    def mancoosimm_Configuration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__mancoosimm_Configuration15", None)
        self.__mancoosimm_Configuration15 = value
        
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
    def Configuration129(self):
        return self.__Configuration129

    @Configuration129.setter
    def Configuration129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mancoosimm_Configuration__Configuration129", None)
        self.__Configuration129 = value
        
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
    def maintainer(self) -> str:
        return self.__maintainer

    @maintainer.setter
    def maintainer(self, maintainer: str):
        self.__maintainer = maintainer

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
    def checkSum(self) -> str:
        return self.__checkSum

    @checkSum.setter
    def checkSum(self, checkSum: str):
        self.__checkSum = checkSum

    @property
    def uploaders(self) -> str:
        return self.__uploaders

    @uploaders.setter
    def uploaders(self, uploaders: str):
        self.__uploaders = uploaders

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
class mancoosimm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

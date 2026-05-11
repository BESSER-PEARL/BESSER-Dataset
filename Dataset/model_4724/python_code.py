from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TAnnotatable:

    pass
class TSignature:

    pass
class TMember:

    pass
class basic_TFieldDefinition(TMember):

    pass
class basic_TMethodDefinition(TMember):

    pass
class basic_TMethodSignature(TSignature):

    pass
class TAbstractType:

    pass
class basic_TInterface(TAbstractType):

    pass
class basic_TClass(TAbstractType):

    pass
class basic_TAnnotationType(TAbstractType):

    pass
class basic_TAnnotatable(ABC):

    pass
class TElementWithId:

    pass
class basic_TMethod(TElementWithId):

    def __init__(self, tName: str, TMethod: "basic_TMethodSignature" = None, methods: "basic_TypeGraph" = None, method: set["basic_TMethodSignature"] = None, TMethod88: "basic_TypeGraph" = None):
        self.tName = tName
        self.TMethod = TMethod
        self.methods = methods
        self.method = method if method is not None else set()
        self.TMethod88 = TMethod88
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TMethod(self):
        return self.__TMethod

    @TMethod.setter
    def TMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__TMethod", None)
        self.__TMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "signatures49"):
                opp_val = getattr(old_value, "signatures49", None)
                if opp_val == self:
                    setattr(old_value, "signatures49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "signatures49"):
                opp_val = getattr(value, "signatures49", None)
                setattr(value, "signatures49", self)

    @property
    def TMethod88(self):
        return self.__TMethod88

    @TMethod88.setter
    def TMethod88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__TMethod88", None)
        self.__TMethod88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pg87"):
                opp_val = getattr(old_value, "pg87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pg87"):
                opp_val = getattr(value, "pg87", None)
                if opp_val is None:
                    setattr(value, "pg87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraph30"):
                opp_val = getattr(old_value, "TypeGraph30", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraph30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraph30"):
                opp_val = getattr(value, "TypeGraph30", None)
                setattr(value, "TypeGraph30", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__method", None)
        self.__method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMethodSignature"):
                    opp_val = getattr(item, "TMethodSignature", None)
                    
                    if opp_val == self:
                        setattr(item, "TMethodSignature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMethodSignature"):
                    opp_val = getattr(item, "TMethodSignature", None)
                    
                    setattr(item, "TMethodSignature", self)
                    

class basic_TAbstractType(TAnnotatable, TElementWithId):

    def __init__(self, tLib: bool, tName: str, basic_TAbstractType56: "basic_TMethodSignature" = None, basic_TAbstractType77: "basic_TParameter" = None, basic_TAbstractType: "basic_TFieldSignature" = None, TAbstractType: "basic_TMember" = None, TAbstractType68: "basic_TPackage" = None, basic_TAbstractType47: "basic_TMethodDefinition" = None, TAbstractType100: "basic_TypeGraph" = None, ownedTypes: "basic_TypeGraph" = None, ownedTypes114: "basic_TPackage" = None, basic_TAbstractType117: set["basic_TSignature"] = None, definedBy: set["basic_TMember"] = None):
        self.tLib = tLib
        self.tName = tName
        self.basic_TAbstractType56 = basic_TAbstractType56
        self.basic_TAbstractType77 = basic_TAbstractType77
        self.basic_TAbstractType = basic_TAbstractType
        self.TAbstractType = TAbstractType
        self.TAbstractType68 = TAbstractType68
        self.basic_TAbstractType47 = basic_TAbstractType47
        self.TAbstractType100 = TAbstractType100
        self.ownedTypes = ownedTypes
        self.ownedTypes114 = ownedTypes114
        self.basic_TAbstractType117 = basic_TAbstractType117 if basic_TAbstractType117 is not None else set()
        self.definedBy = definedBy if definedBy is not None else set()
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def tLib(self):
        return self.__tLib

    @tLib.setter
    def tLib(self, tLib: bool):
        self.__tLib = tLib


    @property
    def basic_TAbstractType56(self):
        return self.__basic_TAbstractType56

    @basic_TAbstractType56.setter
    def basic_TAbstractType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType56", None)
        self.__basic_TAbstractType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TMethodSignature55"):
                opp_val = getattr(old_value, "basic_TMethodSignature55", None)
                if opp_val == self:
                    setattr(old_value, "basic_TMethodSignature55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TMethodSignature55"):
                opp_val = getattr(value, "basic_TMethodSignature55", None)
                setattr(value, "basic_TMethodSignature55", self)

    @property
    def basic_TAbstractType(self):
        return self.__basic_TAbstractType

    @basic_TAbstractType.setter
    def basic_TAbstractType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType", None)
        self.__basic_TAbstractType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TFieldSignature"):
                opp_val = getattr(old_value, "basic_TFieldSignature", None)
                if opp_val == self:
                    setattr(old_value, "basic_TFieldSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TFieldSignature"):
                opp_val = getattr(value, "basic_TFieldSignature", None)
                setattr(value, "basic_TFieldSignature", self)

    @property
    def basic_TAbstractType117(self):
        return self.__basic_TAbstractType117

    @basic_TAbstractType117.setter
    def basic_TAbstractType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType117", None)
        self.__basic_TAbstractType117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TSignature"):
                    opp_val = getattr(item, "basic_TSignature", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TSignature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TSignature"):
                    opp_val = getattr(item, "basic_TSignature", None)
                    
                    setattr(item, "basic_TSignature", self)
                    

    @property
    def TAbstractType(self):
        return self.__TAbstractType

    @TAbstractType.setter
    def TAbstractType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__TAbstractType", None)
        self.__TAbstractType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defines"):
                opp_val = getattr(old_value, "defines", None)
                if opp_val == self:
                    setattr(old_value, "defines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defines"):
                opp_val = getattr(value, "defines", None)
                setattr(value, "defines", self)

    @property
    def TAbstractType68(self):
        return self.__TAbstractType68

    @TAbstractType68.setter
    def TAbstractType68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__TAbstractType68", None)
        self.__TAbstractType68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def definedBy(self):
        return self.__definedBy

    @definedBy.setter
    def definedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__definedBy", None)
        self.__definedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMember119"):
                    opp_val = getattr(item, "TMember119", None)
                    
                    if opp_val == self:
                        setattr(item, "TMember119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMember119"):
                    opp_val = getattr(item, "TMember119", None)
                    
                    setattr(item, "TMember119", self)
                    

    @property
    def basic_TAbstractType77(self):
        return self.__basic_TAbstractType77

    @basic_TAbstractType77.setter
    def basic_TAbstractType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType77", None)
        self.__basic_TAbstractType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TParameter"):
                opp_val = getattr(old_value, "basic_TParameter", None)
                if opp_val == self:
                    setattr(old_value, "basic_TParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TParameter"):
                opp_val = getattr(value, "basic_TParameter", None)
                setattr(value, "basic_TParameter", self)

    @property
    def ownedTypes114(self):
        return self.__ownedTypes114

    @ownedTypes114.setter
    def ownedTypes114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__ownedTypes114", None)
        self.__ownedTypes114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPackage115"):
                opp_val = getattr(old_value, "TPackage115", None)
                if opp_val == self:
                    setattr(old_value, "TPackage115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPackage115"):
                opp_val = getattr(value, "TPackage115", None)
                setattr(value, "TPackage115", self)

    @property
    def TAbstractType100(self):
        return self.__TAbstractType100

    @TAbstractType100.setter
    def TAbstractType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__TAbstractType100", None)
        self.__TAbstractType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pg99"):
                opp_val = getattr(old_value, "pg99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pg99"):
                opp_val = getattr(value, "pg99", None)
                if opp_val is None:
                    setattr(value, "pg99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedTypes(self):
        return self.__ownedTypes

    @ownedTypes.setter
    def ownedTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__ownedTypes", None)
        self.__ownedTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraph112"):
                opp_val = getattr(old_value, "TypeGraph112", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraph112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraph112"):
                opp_val = getattr(value, "TypeGraph112", None)
                setattr(value, "TypeGraph112", self)

    @property
    def basic_TAbstractType47(self):
        return self.__basic_TAbstractType47

    @basic_TAbstractType47.setter
    def basic_TAbstractType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType47", None)
        self.__basic_TAbstractType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TMethodDefinition"):
                opp_val = getattr(old_value, "basic_TMethodDefinition", None)
                if opp_val == self:
                    setattr(old_value, "basic_TMethodDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TMethodDefinition"):
                opp_val = getattr(value, "basic_TMethodDefinition", None)
                setattr(value, "basic_TMethodDefinition", self)

class basic_TAnnotation(TElementWithId):

    pass
class basic_TSignature(TAnnotatable, TElementWithId):

    pass
class basic_TPackage(TAnnotatable, TElementWithId):

    def __init__(self, tName: str, packages: "basic_TypeGraph" = None, TPackage: "basic_TPackage" = None, parent: set["basic_TPackage"] = None, TPackage63: "basic_TPackage" = None, subpackage: "basic_TPackage" = None, basic_TPackage: set["basic_TClass"] = None, basic_TPackage66: set["basic_TInterface"] = None, package: set["basic_TAbstractType"] = None, basic_TPackage70: "basic_TypeGraph" = None, TPackage85: "basic_TypeGraph" = None, TPackage115: "basic_TAbstractType" = None):
        self.tName = tName
        self.packages = packages
        self.TPackage = TPackage
        self.parent = parent if parent is not None else set()
        self.TPackage63 = TPackage63
        self.subpackage = subpackage
        self.basic_TPackage = basic_TPackage if basic_TPackage is not None else set()
        self.basic_TPackage66 = basic_TPackage66 if basic_TPackage66 is not None else set()
        self.package = package if package is not None else set()
        self.basic_TPackage70 = basic_TPackage70
        self.TPackage85 = TPackage85
        self.TPackage115 = TPackage115
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def basic_TPackage(self):
        return self.__basic_TPackage

    @basic_TPackage.setter
    def basic_TPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__basic_TPackage", None)
        self.__basic_TPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TClass"):
                    opp_val = getattr(item, "basic_TClass", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TClass"):
                    opp_val = getattr(item, "basic_TClass", None)
                    
                    setattr(item, "basic_TClass", self)
                    

    @property
    def basic_TPackage70(self):
        return self.__basic_TPackage70

    @basic_TPackage70.setter
    def basic_TPackage70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__basic_TPackage70", None)
        self.__basic_TPackage70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TypeGraph"):
                opp_val = getattr(old_value, "basic_TypeGraph", None)
                if opp_val == self:
                    setattr(old_value, "basic_TypeGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TypeGraph"):
                opp_val = getattr(value, "basic_TypeGraph", None)
                setattr(value, "basic_TypeGraph", self)

    @property
    def subpackage(self):
        return self.__subpackage

    @subpackage.setter
    def subpackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__subpackage", None)
        self.__subpackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPackage63"):
                opp_val = getattr(old_value, "TPackage63", None)
                if opp_val == self:
                    setattr(old_value, "TPackage63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPackage63"):
                opp_val = getattr(value, "TPackage63", None)
                setattr(value, "TPackage63", self)

    @property
    def TPackage63(self):
        return self.__TPackage63

    @TPackage63.setter
    def TPackage63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__TPackage63", None)
        self.__TPackage63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subpackage"):
                opp_val = getattr(old_value, "subpackage", None)
                if opp_val == self:
                    setattr(old_value, "subpackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subpackage"):
                opp_val = getattr(value, "subpackage", None)
                setattr(value, "subpackage", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TAbstractType68"):
                    opp_val = getattr(item, "TAbstractType68", None)
                    
                    if opp_val == self:
                        setattr(item, "TAbstractType68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TAbstractType68"):
                    opp_val = getattr(item, "TAbstractType68", None)
                    
                    setattr(item, "TAbstractType68", self)
                    

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraph58"):
                opp_val = getattr(old_value, "TypeGraph58", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraph58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraph58"):
                opp_val = getattr(value, "TypeGraph58", None)
                setattr(value, "TypeGraph58", self)

    @property
    def TPackage(self):
        return self.__TPackage

    @TPackage.setter
    def TPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__TPackage", None)
        self.__TPackage = value
        
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
    def TPackage115(self):
        return self.__TPackage115

    @TPackage115.setter
    def TPackage115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__TPackage115", None)
        self.__TPackage115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTypes114"):
                opp_val = getattr(old_value, "ownedTypes114", None)
                if opp_val == self:
                    setattr(old_value, "ownedTypes114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTypes114"):
                opp_val = getattr(value, "ownedTypes114", None)
                setattr(value, "ownedTypes114", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPackage"):
                    opp_val = getattr(item, "TPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "TPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPackage"):
                    opp_val = getattr(item, "TPackage", None)
                    
                    setattr(item, "TPackage", self)
                    

    @property
    def TPackage85(self):
        return self.__TPackage85

    @TPackage85.setter
    def TPackage85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__TPackage85", None)
        self.__TPackage85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pg"):
                opp_val = getattr(old_value, "pg", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pg"):
                opp_val = getattr(value, "pg", None)
                if opp_val is None:
                    setattr(value, "pg", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic_TPackage66(self):
        return self.__basic_TPackage66

    @basic_TPackage66.setter
    def basic_TPackage66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__basic_TPackage66", None)
        self.__basic_TPackage66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TInterface"):
                    opp_val = getattr(item, "basic_TInterface", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TInterface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TInterface"):
                    opp_val = getattr(item, "basic_TInterface", None)
                    
                    setattr(item, "basic_TInterface", self)
                    

class basic_TypeGraph(TElementWithId):

    def __init__(self, tName: str, TypeGraph58: "basic_TPackage" = None, TypeGraph30: "basic_TMethod" = None, TypeGraph: "basic_TField" = None, basic_TypeGraph: "basic_TPackage" = None, pg: set["basic_TPackage"] = None, pg87: set["basic_TMethod"] = None, pg90: set["basic_TField"] = None, basic_TypeGraph93: set["basic_TClass"] = None, basic_TypeGraph96: set["basic_TInterface"] = None, pg99: set["basic_TAbstractType"] = None, basic_TypeGraph102: set["basic_TAnnotationType"] = None, TypeGraph112: "basic_TAbstractType" = None):
        self.tName = tName
        self.TypeGraph58 = TypeGraph58
        self.TypeGraph30 = TypeGraph30
        self.TypeGraph = TypeGraph
        self.basic_TypeGraph = basic_TypeGraph
        self.pg = pg if pg is not None else set()
        self.pg87 = pg87 if pg87 is not None else set()
        self.pg90 = pg90 if pg90 is not None else set()
        self.basic_TypeGraph93 = basic_TypeGraph93 if basic_TypeGraph93 is not None else set()
        self.basic_TypeGraph96 = basic_TypeGraph96 if basic_TypeGraph96 is not None else set()
        self.pg99 = pg99 if pg99 is not None else set()
        self.basic_TypeGraph102 = basic_TypeGraph102 if basic_TypeGraph102 is not None else set()
        self.TypeGraph112 = TypeGraph112
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TypeGraph58(self):
        return self.__TypeGraph58

    @TypeGraph58.setter
    def TypeGraph58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__TypeGraph58", None)
        self.__TypeGraph58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packages"):
                opp_val = getattr(old_value, "packages", None)
                if opp_val == self:
                    setattr(old_value, "packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packages"):
                opp_val = getattr(value, "packages", None)
                setattr(value, "packages", self)

    @property
    def pg87(self):
        return self.__pg87

    @pg87.setter
    def pg87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__pg87", None)
        self.__pg87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMethod88"):
                    opp_val = getattr(item, "TMethod88", None)
                    
                    if opp_val == self:
                        setattr(item, "TMethod88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMethod88"):
                    opp_val = getattr(item, "TMethod88", None)
                    
                    setattr(item, "TMethod88", self)
                    

    @property
    def TypeGraph(self):
        return self.__TypeGraph

    @TypeGraph.setter
    def TypeGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__TypeGraph", None)
        self.__TypeGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fields"):
                opp_val = getattr(old_value, "fields", None)
                if opp_val == self:
                    setattr(old_value, "fields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fields"):
                opp_val = getattr(value, "fields", None)
                setattr(value, "fields", self)

    @property
    def basic_TypeGraph93(self):
        return self.__basic_TypeGraph93

    @basic_TypeGraph93.setter
    def basic_TypeGraph93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph93", None)
        self.__basic_TypeGraph93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TClass94"):
                    opp_val = getattr(item, "basic_TClass94", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TClass94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TClass94"):
                    opp_val = getattr(item, "basic_TClass94", None)
                    
                    setattr(item, "basic_TClass94", self)
                    

    @property
    def basic_TypeGraph96(self):
        return self.__basic_TypeGraph96

    @basic_TypeGraph96.setter
    def basic_TypeGraph96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph96", None)
        self.__basic_TypeGraph96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TInterface97"):
                    opp_val = getattr(item, "basic_TInterface97", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TInterface97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TInterface97"):
                    opp_val = getattr(item, "basic_TInterface97", None)
                    
                    setattr(item, "basic_TInterface97", self)
                    

    @property
    def basic_TypeGraph(self):
        return self.__basic_TypeGraph

    @basic_TypeGraph.setter
    def basic_TypeGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph", None)
        self.__basic_TypeGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TPackage70"):
                opp_val = getattr(old_value, "basic_TPackage70", None)
                if opp_val == self:
                    setattr(old_value, "basic_TPackage70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TPackage70"):
                opp_val = getattr(value, "basic_TPackage70", None)
                setattr(value, "basic_TPackage70", self)

    @property
    def TypeGraph112(self):
        return self.__TypeGraph112

    @TypeGraph112.setter
    def TypeGraph112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__TypeGraph112", None)
        self.__TypeGraph112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTypes"):
                opp_val = getattr(old_value, "ownedTypes", None)
                if opp_val == self:
                    setattr(old_value, "ownedTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTypes"):
                opp_val = getattr(value, "ownedTypes", None)
                setattr(value, "ownedTypes", self)

    @property
    def pg99(self):
        return self.__pg99

    @pg99.setter
    def pg99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__pg99", None)
        self.__pg99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TAbstractType100"):
                    opp_val = getattr(item, "TAbstractType100", None)
                    
                    if opp_val == self:
                        setattr(item, "TAbstractType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TAbstractType100"):
                    opp_val = getattr(item, "TAbstractType100", None)
                    
                    setattr(item, "TAbstractType100", self)
                    

    @property
    def TypeGraph30(self):
        return self.__TypeGraph30

    @TypeGraph30.setter
    def TypeGraph30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__TypeGraph30", None)
        self.__TypeGraph30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def pg90(self):
        return self.__pg90

    @pg90.setter
    def pg90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__pg90", None)
        self.__pg90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TField91"):
                    opp_val = getattr(item, "TField91", None)
                    
                    if opp_val == self:
                        setattr(item, "TField91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TField91"):
                    opp_val = getattr(item, "TField91", None)
                    
                    setattr(item, "TField91", self)
                    

    @property
    def pg(self):
        return self.__pg

    @pg.setter
    def pg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__pg", None)
        self.__pg = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPackage85"):
                    opp_val = getattr(item, "TPackage85", None)
                    
                    if opp_val == self:
                        setattr(item, "TPackage85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPackage85"):
                    opp_val = getattr(item, "TPackage85", None)
                    
                    setattr(item, "TPackage85", self)
                    

    @property
    def basic_TypeGraph102(self):
        return self.__basic_TypeGraph102

    @basic_TypeGraph102.setter
    def basic_TypeGraph102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph102", None)
        self.__basic_TypeGraph102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TAnnotationType"):
                    opp_val = getattr(item, "basic_TAnnotationType", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TAnnotationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TAnnotationType"):
                    opp_val = getattr(item, "basic_TAnnotationType", None)
                    
                    setattr(item, "basic_TAnnotationType", self)
                    

class basic_TParameter(TElementWithId):

    pass
class basic_TMember(TAnnotatable, TElementWithId):

    pass
class basic_TParameterList(TElementWithId):

    pass
class basic_TAccess(TElementWithId):

    pass
class basic_TFieldSignature(TSignature):

    pass
class basic_TField(TElementWithId):

    def __init__(self, tName: str, field: set["basic_TFieldSignature"] = None, fields: "basic_TypeGraph" = None, TField: "basic_TFieldSignature" = None, TField91: "basic_TypeGraph" = None):
        self.tName = tName
        self.field = field if field is not None else set()
        self.fields = fields
        self.TField = TField
        self.TField91 = TField91
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TField(self):
        return self.__TField

    @TField.setter
    def TField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__TField", None)
        self.__TField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "signatures"):
                opp_val = getattr(old_value, "signatures", None)
                if opp_val == self:
                    setattr(old_value, "signatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "signatures"):
                opp_val = getattr(value, "signatures", None)
                setattr(value, "signatures", self)

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__field", None)
        self.__field = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TFieldSignature"):
                    opp_val = getattr(item, "TFieldSignature", None)
                    
                    if opp_val == self:
                        setattr(item, "TFieldSignature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TFieldSignature"):
                    opp_val = getattr(item, "TFieldSignature", None)
                    
                    setattr(item, "TFieldSignature", self)
                    

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraph"):
                opp_val = getattr(old_value, "TypeGraph", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraph"):
                opp_val = getattr(value, "TypeGraph", None)
                setattr(value, "TypeGraph", self)

    @property
    def TField91(self):
        return self.__TField91

    @TField91.setter
    def TField91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__TField91", None)
        self.__TField91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pg90"):
                opp_val = getattr(old_value, "pg90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pg90"):
                opp_val = getattr(value, "pg90", None)
                if opp_val is None:
                    setattr(value, "pg90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basic_TElementWithId(ABC):

    def __init__(self, ID: int):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID


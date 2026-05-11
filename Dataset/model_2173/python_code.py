from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypeGraphBasic_TypeGraph:

    def __init__(self, tName: str, TypeGraphBasic_TypeGraph71: set["TypeGraphBasic_TMethod"] = None, TypeGraphBasic_TypeGraph: set["TypeGraphBasic_TPackage"] = None, TypeGraphBasic_TypeGraph73: set["TypeGraphBasic_TField"] = None, TypeGraphBasic_TypeGraph75: set["TypeGraphBasic_TClass"] = None):
        self.tName = tName
        self.TypeGraphBasic_TypeGraph71 = TypeGraphBasic_TypeGraph71 if TypeGraphBasic_TypeGraph71 is not None else set()
        self.TypeGraphBasic_TypeGraph = TypeGraphBasic_TypeGraph if TypeGraphBasic_TypeGraph is not None else set()
        self.TypeGraphBasic_TypeGraph73 = TypeGraphBasic_TypeGraph73 if TypeGraphBasic_TypeGraph73 is not None else set()
        self.TypeGraphBasic_TypeGraph75 = TypeGraphBasic_TypeGraph75 if TypeGraphBasic_TypeGraph75 is not None else set()
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TypeGraphBasic_TypeGraph73(self):
        return self.__TypeGraphBasic_TypeGraph73

    @TypeGraphBasic_TypeGraph73.setter
    def TypeGraphBasic_TypeGraph73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph73", None)
        self.__TypeGraphBasic_TypeGraph73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TField"):
                    opp_val = getattr(item, "TypeGraphBasic_TField", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TField"):
                    opp_val = getattr(item, "TypeGraphBasic_TField", None)
                    
                    setattr(item, "TypeGraphBasic_TField", self)
                    

    @property
    def TypeGraphBasic_TypeGraph(self):
        return self.__TypeGraphBasic_TypeGraph

    @TypeGraphBasic_TypeGraph.setter
    def TypeGraphBasic_TypeGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph", None)
        self.__TypeGraphBasic_TypeGraph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TPackage"):
                    opp_val = getattr(item, "TypeGraphBasic_TPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TPackage"):
                    opp_val = getattr(item, "TypeGraphBasic_TPackage", None)
                    
                    setattr(item, "TypeGraphBasic_TPackage", self)
                    

    @property
    def TypeGraphBasic_TypeGraph71(self):
        return self.__TypeGraphBasic_TypeGraph71

    @TypeGraphBasic_TypeGraph71.setter
    def TypeGraphBasic_TypeGraph71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph71", None)
        self.__TypeGraphBasic_TypeGraph71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TMethod"):
                    opp_val = getattr(item, "TypeGraphBasic_TMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TMethod"):
                    opp_val = getattr(item, "TypeGraphBasic_TMethod", None)
                    
                    setattr(item, "TypeGraphBasic_TMethod", self)
                    

    @property
    def TypeGraphBasic_TypeGraph75(self):
        return self.__TypeGraphBasic_TypeGraph75

    @TypeGraphBasic_TypeGraph75.setter
    def TypeGraphBasic_TypeGraph75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph75", None)
        self.__TypeGraphBasic_TypeGraph75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TClass76"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass76", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TClass76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TClass76"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass76", None)
                    
                    setattr(item, "TypeGraphBasic_TClass76", self)
                    

class TypeGraphBasic_TParameter:

    pass
class TypeGraphBasic_TParameterList:

    pass
class TypeGraphBasic_TMethod:

    def __init__(self, tName: str, TypeGraphBasic_TMethod: "TypeGraphBasic_TypeGraph" = None, method: set["TypeGraphBasic_TMethodSignature"] = None, TMethod: "TypeGraphBasic_TMethodSignature" = None):
        self.tName = tName
        self.TypeGraphBasic_TMethod = TypeGraphBasic_TMethod
        self.method = method if method is not None else set()
        self.TMethod = TMethod
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TypeGraphBasic_TMethod(self):
        return self.__TypeGraphBasic_TMethod

    @TypeGraphBasic_TMethod.setter
    def TypeGraphBasic_TMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__TypeGraphBasic_TMethod", None)
        self.__TypeGraphBasic_TMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph71"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph71"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph71", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TMethod(self):
        return self.__TMethod

    @TMethod.setter
    def TMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__TMethod", None)
        self.__TMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "signatures43"):
                opp_val = getattr(old_value, "signatures43", None)
                if opp_val == self:
                    setattr(old_value, "signatures43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "signatures43"):
                opp_val = getattr(value, "signatures43", None)
                setattr(value, "signatures43", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__method", None)
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
                    

class TSignature:

    pass
class TypeGraphBasic_TMethodSignature(TSignature):

    pass
class TMember:

    pass
class TypeGraphBasic_TMethodDefinition(TMember):

    pass
class TypeGraphBasic_TFieldDefinition(TMember):

    pass
class TypeGraphBasic_TFieldSignature(TSignature):

    pass
class TypeGraphBasic_TField:

    def __init__(self, tName: str, field: set["TypeGraphBasic_TFieldSignature"] = None, TField: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TField: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.field = field if field is not None else set()
        self.TField = TField
        self.TypeGraphBasic_TField = TypeGraphBasic_TField
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TypeGraphBasic_TField(self):
        return self.__TypeGraphBasic_TField

    @TypeGraphBasic_TField.setter
    def TypeGraphBasic_TField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TField__TypeGraphBasic_TField", None)
        self.__TypeGraphBasic_TField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph73"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph73"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph73", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TField(self):
        return self.__TField

    @TField.setter
    def TField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TField__TField", None)
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
        old_value = getattr(self, f"_TypeGraphBasic_TField__field", None)
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
                    

class TypeGraphBasic_TMember(ABC):

    pass
class TypeGraphBasic_TSignature(ABC):

    pass
class TypeGraphBasic_TPackage:

    def __init__(self, tName: str, TPackage: "TypeGraphBasic_TClass" = None, package: set["TypeGraphBasic_TClass"] = None, TPackage52: "TypeGraphBasic_TPackage" = None, parent: set["TypeGraphBasic_TPackage"] = None, TPackage55: "TypeGraphBasic_TPackage" = None, subpackage: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TPackage: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.TPackage = TPackage
        self.package = package if package is not None else set()
        self.TPackage52 = TPackage52
        self.parent = parent if parent is not None else set()
        self.TPackage55 = TPackage55
        self.subpackage = subpackage
        self.TypeGraphBasic_TPackage = TypeGraphBasic_TPackage
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TPackage(self):
        return self.__TPackage

    @TPackage.setter
    def TPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TPackage", None)
        self.__TPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedClasses"):
                opp_val = getattr(old_value, "containedClasses", None)
                if opp_val == self:
                    setattr(old_value, "containedClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedClasses"):
                opp_val = getattr(value, "containedClasses", None)
                setattr(value, "containedClasses", self)

    @property
    def subpackage(self):
        return self.__subpackage

    @subpackage.setter
    def subpackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__subpackage", None)
        self.__subpackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPackage55"):
                opp_val = getattr(old_value, "TPackage55", None)
                if opp_val == self:
                    setattr(old_value, "TPackage55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPackage55"):
                opp_val = getattr(value, "TPackage55", None)
                setattr(value, "TPackage55", self)

    @property
    def TPackage52(self):
        return self.__TPackage52

    @TPackage52.setter
    def TPackage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TPackage52", None)
        self.__TPackage52 = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPackage52"):
                    opp_val = getattr(item, "TPackage52", None)
                    
                    if opp_val == self:
                        setattr(item, "TPackage52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPackage52"):
                    opp_val = getattr(item, "TPackage52", None)
                    
                    setattr(item, "TPackage52", self)
                    

    @property
    def TypeGraphBasic_TPackage(self):
        return self.__TypeGraphBasic_TPackage

    @TypeGraphBasic_TPackage.setter
    def TypeGraphBasic_TPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TypeGraphBasic_TPackage", None)
        self.__TypeGraphBasic_TPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TPackage55(self):
        return self.__TPackage55

    @TPackage55.setter
    def TPackage55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TPackage55", None)
        self.__TPackage55 = value
        
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
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TClass49"):
                    opp_val = getattr(item, "TClass49", None)
                    
                    if opp_val == self:
                        setattr(item, "TClass49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TClass49"):
                    opp_val = getattr(item, "TClass49", None)
                    
                    setattr(item, "TClass49", self)
                    

class TypeGraphBasic_TClass:

    def __init__(self, tName: str, containedClasses: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass: set["TypeGraphBasic_TSignature"] = None, TypeGraphBasic_TClass3: set["TypeGraphBasic_TMember"] = None, TClass: "TypeGraphBasic_TClass" = None, childClasses: "TypeGraphBasic_TClass" = None, TClass8: "TypeGraphBasic_TClass" = None, parentClass: set["TypeGraphBasic_TClass"] = None, TypeGraphBasic_TClass21: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TClass41: "TypeGraphBasic_TMethodDefinition" = None, TClass49: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass62: "TypeGraphBasic_TParameter" = None, TypeGraphBasic_TClass76: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.containedClasses = containedClasses
        self.TypeGraphBasic_TClass = TypeGraphBasic_TClass if TypeGraphBasic_TClass is not None else set()
        self.TypeGraphBasic_TClass3 = TypeGraphBasic_TClass3 if TypeGraphBasic_TClass3 is not None else set()
        self.TClass = TClass
        self.childClasses = childClasses
        self.TClass8 = TClass8
        self.parentClass = parentClass if parentClass is not None else set()
        self.TypeGraphBasic_TClass21 = TypeGraphBasic_TClass21
        self.TypeGraphBasic_TClass41 = TypeGraphBasic_TClass41
        self.TClass49 = TClass49
        self.TypeGraphBasic_TClass62 = TypeGraphBasic_TClass62
        self.TypeGraphBasic_TClass76 = TypeGraphBasic_TClass76
        
        pass
    @property
    def tName(self):
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName


    @property
    def TClass(self):
        return self.__TClass

    @TClass.setter
    def TClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TClass", None)
        self.__TClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childClasses"):
                opp_val = getattr(old_value, "childClasses", None)
                if opp_val == self:
                    setattr(old_value, "childClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childClasses"):
                opp_val = getattr(value, "childClasses", None)
                setattr(value, "childClasses", self)

    @property
    def containedClasses(self):
        return self.__containedClasses

    @containedClasses.setter
    def containedClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__containedClasses", None)
        self.__containedClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPackage"):
                opp_val = getattr(old_value, "TPackage", None)
                if opp_val == self:
                    setattr(old_value, "TPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPackage"):
                opp_val = getattr(value, "TPackage", None)
                setattr(value, "TPackage", self)

    @property
    def TypeGraphBasic_TClass41(self):
        return self.__TypeGraphBasic_TClass41

    @TypeGraphBasic_TClass41.setter
    def TypeGraphBasic_TClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass41", None)
        self.__TypeGraphBasic_TClass41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TMethodDefinition"):
                opp_val = getattr(old_value, "TypeGraphBasic_TMethodDefinition", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraphBasic_TMethodDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TMethodDefinition"):
                opp_val = getattr(value, "TypeGraphBasic_TMethodDefinition", None)
                setattr(value, "TypeGraphBasic_TMethodDefinition", self)

    @property
    def TypeGraphBasic_TClass21(self):
        return self.__TypeGraphBasic_TClass21

    @TypeGraphBasic_TClass21.setter
    def TypeGraphBasic_TClass21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass21", None)
        self.__TypeGraphBasic_TClass21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TFieldSignature"):
                opp_val = getattr(old_value, "TypeGraphBasic_TFieldSignature", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraphBasic_TFieldSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TFieldSignature"):
                opp_val = getattr(value, "TypeGraphBasic_TFieldSignature", None)
                setattr(value, "TypeGraphBasic_TFieldSignature", self)

    @property
    def childClasses(self):
        return self.__childClasses

    @childClasses.setter
    def childClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__childClasses", None)
        self.__childClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TClass"):
                opp_val = getattr(old_value, "TClass", None)
                if opp_val == self:
                    setattr(old_value, "TClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TClass"):
                opp_val = getattr(value, "TClass", None)
                setattr(value, "TClass", self)

    @property
    def TClass49(self):
        return self.__TClass49

    @TClass49.setter
    def TClass49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TClass49", None)
        self.__TClass49 = value
        
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
    def TypeGraphBasic_TClass76(self):
        return self.__TypeGraphBasic_TClass76

    @TypeGraphBasic_TClass76.setter
    def TypeGraphBasic_TClass76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass76", None)
        self.__TypeGraphBasic_TClass76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph75"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph75"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph75", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass(self):
        return self.__TypeGraphBasic_TClass

    @TypeGraphBasic_TClass.setter
    def TypeGraphBasic_TClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass", None)
        self.__TypeGraphBasic_TClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TSignature"):
                    opp_val = getattr(item, "TypeGraphBasic_TSignature", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TSignature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TSignature"):
                    opp_val = getattr(item, "TypeGraphBasic_TSignature", None)
                    
                    setattr(item, "TypeGraphBasic_TSignature", self)
                    

    @property
    def parentClass(self):
        return self.__parentClass

    @parentClass.setter
    def parentClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__parentClass", None)
        self.__parentClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TClass8"):
                    opp_val = getattr(item, "TClass8", None)
                    
                    if opp_val == self:
                        setattr(item, "TClass8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TClass8"):
                    opp_val = getattr(item, "TClass8", None)
                    
                    setattr(item, "TClass8", self)
                    

    @property
    def TypeGraphBasic_TClass3(self):
        return self.__TypeGraphBasic_TClass3

    @TypeGraphBasic_TClass3.setter
    def TypeGraphBasic_TClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass3", None)
        self.__TypeGraphBasic_TClass3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TMember"):
                    opp_val = getattr(item, "TypeGraphBasic_TMember", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TMember"):
                    opp_val = getattr(item, "TypeGraphBasic_TMember", None)
                    
                    setattr(item, "TypeGraphBasic_TMember", self)
                    

    @property
    def TClass8(self):
        return self.__TClass8

    @TClass8.setter
    def TClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TClass8", None)
        self.__TClass8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentClass"):
                opp_val = getattr(old_value, "parentClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentClass"):
                opp_val = getattr(value, "parentClass", None)
                if opp_val is None:
                    setattr(value, "parentClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass62(self):
        return self.__TypeGraphBasic_TClass62

    @TypeGraphBasic_TClass62.setter
    def TypeGraphBasic_TClass62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass62", None)
        self.__TypeGraphBasic_TClass62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TParameter"):
                opp_val = getattr(old_value, "TypeGraphBasic_TParameter", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraphBasic_TParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TParameter"):
                opp_val = getattr(value, "TypeGraphBasic_TParameter", None)
                setattr(value, "TypeGraphBasic_TParameter", self)

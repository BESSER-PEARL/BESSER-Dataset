from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypeGraphBasic_TypeGraph:

    def __init__(self, tName: str, TypeGraphBasic_TypeGraph: set["TypeGraphBasic_TPackage"] = None, TypeGraphBasic_TypeGraph59: set["TypeGraphBasic_TMethod"] = None, TypeGraphBasic_TypeGraph61: set["TypeGraphBasic_TField"] = None, TypeGraphBasic_TypeGraph63: set["TypeGraphBasic_TClass"] = None):
        self.tName = tName
        self.TypeGraphBasic_TypeGraph = TypeGraphBasic_TypeGraph if TypeGraphBasic_TypeGraph is not None else set()
        self.TypeGraphBasic_TypeGraph59 = TypeGraphBasic_TypeGraph59 if TypeGraphBasic_TypeGraph59 is not None else set()
        self.TypeGraphBasic_TypeGraph61 = TypeGraphBasic_TypeGraph61 if TypeGraphBasic_TypeGraph61 is not None else set()
        self.TypeGraphBasic_TypeGraph63 = TypeGraphBasic_TypeGraph63 if TypeGraphBasic_TypeGraph63 is not None else set()
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

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
    def TypeGraphBasic_TypeGraph63(self):
        return self.__TypeGraphBasic_TypeGraph63

    @TypeGraphBasic_TypeGraph63.setter
    def TypeGraphBasic_TypeGraph63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph63", None)
        self.__TypeGraphBasic_TypeGraph63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TClass64"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass64", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TClass64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TClass64"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass64", None)
                    
                    setattr(item, "TypeGraphBasic_TClass64", self)
                    

    @property
    def TypeGraphBasic_TypeGraph59(self):
        return self.__TypeGraphBasic_TypeGraph59

    @TypeGraphBasic_TypeGraph59.setter
    def TypeGraphBasic_TypeGraph59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph59", None)
        self.__TypeGraphBasic_TypeGraph59 = value if value is not None else set()
        
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
    def TypeGraphBasic_TypeGraph61(self):
        return self.__TypeGraphBasic_TypeGraph61

    @TypeGraphBasic_TypeGraph61.setter
    def TypeGraphBasic_TypeGraph61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph61", None)
        self.__TypeGraphBasic_TypeGraph61 = value if value is not None else set()
        
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
                    

class TypeGraphBasic_TMethod:

    def __init__(self, tName: str, method: set["TypeGraphBasic_TMethodSignature"] = None, TMethod: "TypeGraphBasic_TMethodSignature" = None, TypeGraphBasic_TMethod: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.method = method if method is not None else set()
        self.TMethod = TMethod
        self.TypeGraphBasic_TMethod = TypeGraphBasic_TMethod
        
    @property
    def tName(self) -> str:
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
    def TypeGraphBasic_TMethod(self):
        return self.__TypeGraphBasic_TMethod

    @TypeGraphBasic_TMethod.setter
    def TypeGraphBasic_TMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__TypeGraphBasic_TMethod", None)
        self.__TypeGraphBasic_TMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph59"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph59"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph59", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class TMember:

    pass
class TypeGraphBasic_TMethodDefinition(TMember):

    pass
class TypeGraphBasic_TFieldDefinition(TMember):

    pass
class TypeGraphBasic_TField:

    def __init__(self, tName: str, field: set["TypeGraphBasic_TFieldSignature"] = None, TField: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TField: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.field = field if field is not None else set()
        self.TField = TField
        self.TypeGraphBasic_TField = TypeGraphBasic_TField
        
    @property
    def tName(self) -> str:
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
    def TypeGraphBasic_TField(self):
        return self.__TypeGraphBasic_TField

    @TypeGraphBasic_TField.setter
    def TypeGraphBasic_TField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TField__TypeGraphBasic_TField", None)
        self.__TypeGraphBasic_TField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph61"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph61"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph61", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class TSignature:

    pass
class TypeGraphBasic_TMethodSignature(TSignature):

    pass
class TypeGraphBasic_TFieldSignature(TSignature):

    pass
class TypeGraphBasic_TPackage:

    def __init__(self, tName: str, TPackage: "TypeGraphBasic_TClass" = None, TPackage53: "TypeGraphBasic_TPackage" = None, parent: set["TypeGraphBasic_TPackage"] = None, TPackage56: "TypeGraphBasic_TPackage" = None, subpackage: "TypeGraphBasic_TPackage" = None, package: set["TypeGraphBasic_TClass"] = None, TypeGraphBasic_TPackage: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.TPackage = TPackage
        self.TPackage53 = TPackage53
        self.parent = parent if parent is not None else set()
        self.TPackage56 = TPackage56
        self.subpackage = subpackage
        self.package = package if package is not None else set()
        self.TypeGraphBasic_TPackage = TypeGraphBasic_TPackage
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

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
                if hasattr(item, "TClass50"):
                    opp_val = getattr(item, "TClass50", None)
                    
                    if opp_val == self:
                        setattr(item, "TClass50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TClass50"):
                    opp_val = getattr(item, "TClass50", None)
                    
                    setattr(item, "TClass50", self)
                    

    @property
    def TPackage56(self):
        return self.__TPackage56

    @TPackage56.setter
    def TPackage56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TPackage56", None)
        self.__TPackage56 = value
        
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
                if hasattr(item, "TPackage53"):
                    opp_val = getattr(item, "TPackage53", None)
                    
                    if opp_val == self:
                        setattr(item, "TPackage53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPackage53"):
                    opp_val = getattr(item, "TPackage53", None)
                    
                    setattr(item, "TPackage53", self)
                    

    @property
    def TPackage53(self):
        return self.__TPackage53

    @TPackage53.setter
    def TPackage53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__TPackage53", None)
        self.__TPackage53 = value
        
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
    def subpackage(self):
        return self.__subpackage

    @subpackage.setter
    def subpackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__subpackage", None)
        self.__subpackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPackage56"):
                opp_val = getattr(old_value, "TPackage56", None)
                if opp_val == self:
                    setattr(old_value, "TPackage56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPackage56"):
                opp_val = getattr(value, "TPackage56", None)
                setattr(value, "TPackage56", self)

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

class TypeGraphBasic_TSignature(ABC):

    pass
class TypeGraphBasic_TClass:

    def __init__(self, tName: str, TypeGraphBasic_TClass8: set["TypeGraphBasic_TMember"] = None, TClass: "TypeGraphBasic_TClass" = None, childClasses: "TypeGraphBasic_TClass" = None, TClass4: "TypeGraphBasic_TClass" = None, parentClass: set["TypeGraphBasic_TClass"] = None, TypeGraphBasic_TClass: set["TypeGraphBasic_TSignature"] = None, containedClasses: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass21: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TClass41: "TypeGraphBasic_TMethodDefinition" = None, TypeGraphBasic_TClass48: "TypeGraphBasic_TMethodSignature" = None, TClass50: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass64: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.TypeGraphBasic_TClass8 = TypeGraphBasic_TClass8 if TypeGraphBasic_TClass8 is not None else set()
        self.TClass = TClass
        self.childClasses = childClasses
        self.TClass4 = TClass4
        self.parentClass = parentClass if parentClass is not None else set()
        self.TypeGraphBasic_TClass = TypeGraphBasic_TClass if TypeGraphBasic_TClass is not None else set()
        self.containedClasses = containedClasses
        self.TypeGraphBasic_TClass21 = TypeGraphBasic_TClass21
        self.TypeGraphBasic_TClass41 = TypeGraphBasic_TClass41
        self.TypeGraphBasic_TClass48 = TypeGraphBasic_TClass48
        self.TClass50 = TClass50
        self.TypeGraphBasic_TClass64 = TypeGraphBasic_TClass64
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

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
                if hasattr(item, "TClass4"):
                    opp_val = getattr(item, "TClass4", None)
                    
                    if opp_val == self:
                        setattr(item, "TClass4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TClass4"):
                    opp_val = getattr(item, "TClass4", None)
                    
                    setattr(item, "TClass4", self)
                    

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
    def TypeGraphBasic_TClass48(self):
        return self.__TypeGraphBasic_TClass48

    @TypeGraphBasic_TClass48.setter
    def TypeGraphBasic_TClass48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass48", None)
        self.__TypeGraphBasic_TClass48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TMethodSignature"):
                opp_val = getattr(old_value, "TypeGraphBasic_TMethodSignature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TMethodSignature"):
                opp_val = getattr(value, "TypeGraphBasic_TMethodSignature", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TMethodSignature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def TClass4(self):
        return self.__TClass4

    @TClass4.setter
    def TClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TClass4", None)
        self.__TClass4 = value
        
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
    def TypeGraphBasic_TClass64(self):
        return self.__TypeGraphBasic_TClass64

    @TypeGraphBasic_TClass64.setter
    def TypeGraphBasic_TClass64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass64", None)
        self.__TypeGraphBasic_TClass64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph63"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph63"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph63", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def TypeGraphBasic_TClass8(self):
        return self.__TypeGraphBasic_TClass8

    @TypeGraphBasic_TClass8.setter
    def TypeGraphBasic_TClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass8", None)
        self.__TypeGraphBasic_TClass8 = value if value is not None else set()
        
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
    def TClass50(self):
        return self.__TClass50

    @TClass50.setter
    def TClass50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TClass50", None)
        self.__TClass50 = value
        
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

class TypeGraphBasic_TMember(ABC):

    pass
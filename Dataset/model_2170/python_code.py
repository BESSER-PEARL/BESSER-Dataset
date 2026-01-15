from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypeGraphBasic_TypeGraph:

    def __init__(self, tName: str, TypeGraphBasic_TypeGraph: set["TypeGraphBasic_TPackage"] = None, TypeGraphBasic_TypeGraph83: set["TypeGraphBasic_TMethod"] = None, TypeGraphBasic_TypeGraph85: set["TypeGraphBasic_TField"] = None, TypeGraphBasic_TypeGraph87: set["TypeGraphBasic_TClass"] = None):
        self.tName = tName
        self.TypeGraphBasic_TypeGraph = TypeGraphBasic_TypeGraph if TypeGraphBasic_TypeGraph is not None else set()
        self.TypeGraphBasic_TypeGraph83 = TypeGraphBasic_TypeGraph83 if TypeGraphBasic_TypeGraph83 is not None else set()
        self.TypeGraphBasic_TypeGraph85 = TypeGraphBasic_TypeGraph85 if TypeGraphBasic_TypeGraph85 is not None else set()
        self.TypeGraphBasic_TypeGraph87 = TypeGraphBasic_TypeGraph87 if TypeGraphBasic_TypeGraph87 is not None else set()
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def TypeGraphBasic_TypeGraph85(self):
        return self.__TypeGraphBasic_TypeGraph85

    @TypeGraphBasic_TypeGraph85.setter
    def TypeGraphBasic_TypeGraph85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph85", None)
        self.__TypeGraphBasic_TypeGraph85 = value if value is not None else set()
        
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
    def TypeGraphBasic_TypeGraph83(self):
        return self.__TypeGraphBasic_TypeGraph83

    @TypeGraphBasic_TypeGraph83.setter
    def TypeGraphBasic_TypeGraph83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph83", None)
        self.__TypeGraphBasic_TypeGraph83 = value if value is not None else set()
        
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
    def TypeGraphBasic_TypeGraph87(self):
        return self.__TypeGraphBasic_TypeGraph87

    @TypeGraphBasic_TypeGraph87.setter
    def TypeGraphBasic_TypeGraph87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph87", None)
        self.__TypeGraphBasic_TypeGraph87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TClass88"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass88", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TClass88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TClass88"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass88", None)
                    
                    setattr(item, "TypeGraphBasic_TClass88", self)
                    

class TypeGraphBasic_TMethod:

    def __init__(self, tName: str, 39: set["TypeGraphBasic_TMethodSignature"] = None, 64: "TypeGraphBasic_TMethodSignature" = None, TypeGraphBasic_TMethod: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.39 = 39 if 39 is not None else set()
        self.64 = 64
        self.TypeGraphBasic_TMethod = TypeGraphBasic_TMethod
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def 64(self):
        return self.__64

    @64.setter
    def 64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__64", None)
        self.__64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "63"):
                opp_val = getattr(old_value, "63", None)
                if opp_val == self:
                    setattr(old_value, "63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "63"):
                opp_val = getattr(value, "63", None)
                setattr(value, "63", self)

    @property
    def 39(self):
        return self.__39

    @39.setter
    def 39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TMethod__39", None)
        self.__39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "40"):
                    opp_val = getattr(item, "40", None)
                    
                    if opp_val == self:
                        setattr(item, "40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "40"):
                    opp_val = getattr(item, "40", None)
                    
                    setattr(item, "40", self)
                    

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
            if hasattr(old_value, "TypeGraphBasic_TypeGraph83"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph83"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph83", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def __init__(self, tName: str, 14: set["TypeGraphBasic_TFieldSignature"] = None, 32: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TField: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.14 = 14 if 14 is not None else set()
        self.32 = 32
        self.TypeGraphBasic_TField = TypeGraphBasic_TField
        
    @property
    def tName(self) -> str:
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
            if hasattr(old_value, "TypeGraphBasic_TypeGraph85"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph85"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph85", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 32(self):
        return self.__32

    @32.setter
    def 32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TField__32", None)
        self.__32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "31"):
                opp_val = getattr(old_value, "31", None)
                if opp_val == self:
                    setattr(old_value, "31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "31"):
                opp_val = getattr(value, "31", None)
                setattr(value, "31", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TField__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

class TypeGraphBasic_TMember(ABC):

    pass
class TypeGraphBasic_TPackage:

    def __init__(self, tName: str, 10: "TypeGraphBasic_TClass" = None, 71: set["TypeGraphBasic_TClass"] = None, 76: "TypeGraphBasic_TPackage" = None, 75: set["TypeGraphBasic_TPackage"] = None, 80: "TypeGraphBasic_TPackage" = None, 79: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TPackage: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.10 = 10
        self.71 = 71 if 71 is not None else set()
        self.76 = 76
        self.75 = 75 if 75 is not None else set()
        self.80 = 80
        self.79 = 79
        self.TypeGraphBasic_TPackage = TypeGraphBasic_TPackage
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def 75(self):
        return self.__75

    @75.setter
    def 75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__75", None)
        self.__75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "76"):
                    opp_val = getattr(item, "76", None)
                    
                    if opp_val == self:
                        setattr(item, "76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "76"):
                    opp_val = getattr(item, "76", None)
                    
                    setattr(item, "76", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    @property
    def 80(self):
        return self.__80

    @80.setter
    def 80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__80", None)
        self.__80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "79"):
                opp_val = getattr(old_value, "79", None)
                if opp_val == self:
                    setattr(old_value, "79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "79"):
                opp_val = getattr(value, "79", None)
                setattr(value, "79", self)

    @property
    def 79(self):
        return self.__79

    @79.setter
    def 79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__79", None)
        self.__79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "80"):
                opp_val = getattr(old_value, "80", None)
                if opp_val == self:
                    setattr(old_value, "80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "80"):
                opp_val = getattr(value, "80", None)
                setattr(value, "80", self)

    @property
    def 76(self):
        return self.__76

    @76.setter
    def 76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__76", None)
        self.__76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "75"):
                opp_val = getattr(old_value, "75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "75"):
                opp_val = getattr(value, "75", None)
                if opp_val is None:
                    setattr(value, "75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def 71(self):
        return self.__71

    @71.setter
    def 71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__71", None)
        self.__71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "72"):
                    opp_val = getattr(item, "72", None)
                    
                    if opp_val == self:
                        setattr(item, "72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "72"):
                    opp_val = getattr(item, "72", None)
                    
                    setattr(item, "72", self)
                    

class TypeGraphBasic_TSignature(ABC):

    pass
class TypeGraphBasic_TClass:

    def __init__(self, tName: str, 2: "TypeGraphBasic_TClass" = None, 6: "TypeGraphBasic_TClass" = None, 5: set["TypeGraphBasic_TClass"] = None, TypeGraphBasic_TClass: set["TypeGraphBasic_TSignature"] = None, 9: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass12: set["TypeGraphBasic_TMember"] = None, : "TypeGraphBasic_TClass" = None, TypeGraphBasic_TClass34: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TClass61: "TypeGraphBasic_TMethodDefinition" = None, TypeGraphBasic_TClass69: "TypeGraphBasic_TMethodSignature" = None, 72: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass88: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.2 = 2
        self.6 = 6
        self.5 = 5 if 5 is not None else set()
        self.TypeGraphBasic_TClass = TypeGraphBasic_TClass if TypeGraphBasic_TClass is not None else set()
        self.9 = 9
        self.TypeGraphBasic_TClass12 = TypeGraphBasic_TClass12 if TypeGraphBasic_TClass12 is not None else set()
        self. = 
        self.TypeGraphBasic_TClass34 = TypeGraphBasic_TClass34
        self.TypeGraphBasic_TClass61 = TypeGraphBasic_TClass61
        self.TypeGraphBasic_TClass69 = TypeGraphBasic_TClass69
        self.72 = 72
        self.TypeGraphBasic_TClass88 = TypeGraphBasic_TClass88
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "2"):
                opp_val = getattr(old_value, "2", None)
                if opp_val == self:
                    setattr(old_value, "2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "2"):
                opp_val = getattr(value, "2", None)
                setattr(value, "2", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 72(self):
        return self.__72

    @72.setter
    def 72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__72", None)
        self.__72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "71"):
                opp_val = getattr(old_value, "71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "71"):
                opp_val = getattr(value, "71", None)
                if opp_val is None:
                    setattr(value, "71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__2", None)
        self.__2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def TypeGraphBasic_TClass61(self):
        return self.__TypeGraphBasic_TClass61

    @TypeGraphBasic_TClass61.setter
    def TypeGraphBasic_TClass61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass61", None)
        self.__TypeGraphBasic_TClass61 = value
        
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
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__5", None)
        self.__5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    if opp_val == self:
                        setattr(item, "6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    setattr(item, "6", self)
                    

    @property
    def TypeGraphBasic_TClass12(self):
        return self.__TypeGraphBasic_TClass12

    @TypeGraphBasic_TClass12.setter
    def TypeGraphBasic_TClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass12", None)
        self.__TypeGraphBasic_TClass12 = value if value is not None else set()
        
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
    def TypeGraphBasic_TClass34(self):
        return self.__TypeGraphBasic_TClass34

    @TypeGraphBasic_TClass34.setter
    def TypeGraphBasic_TClass34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass34", None)
        self.__TypeGraphBasic_TClass34 = value
        
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
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                if opp_val is None:
                    setattr(value, "5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass88(self):
        return self.__TypeGraphBasic_TClass88

    @TypeGraphBasic_TClass88.setter
    def TypeGraphBasic_TClass88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass88", None)
        self.__TypeGraphBasic_TClass88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph87"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph87"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph87", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph87", set([self]))
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
    def TypeGraphBasic_TClass69(self):
        return self.__TypeGraphBasic_TClass69

    @TypeGraphBasic_TClass69.setter
    def TypeGraphBasic_TClass69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass69", None)
        self.__TypeGraphBasic_TClass69 = value
        
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

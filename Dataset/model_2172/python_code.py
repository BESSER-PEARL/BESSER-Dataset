from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TypeGraphBasic_TypeGraph:

    def __init__(self, tName: str, TypeGraphBasic_TypeGraph: set["TypeGraphBasic_TPackage"] = None, TypeGraphBasic_TypeGraph98: set["TypeGraphBasic_TMethod"] = None, TypeGraphBasic_TypeGraph100: set["TypeGraphBasic_TField"] = None, TypeGraphBasic_TypeGraph102: set["TypeGraphBasic_TClass"] = None):
        self.tName = tName
        self.TypeGraphBasic_TypeGraph = TypeGraphBasic_TypeGraph if TypeGraphBasic_TypeGraph is not None else set()
        self.TypeGraphBasic_TypeGraph98 = TypeGraphBasic_TypeGraph98 if TypeGraphBasic_TypeGraph98 is not None else set()
        self.TypeGraphBasic_TypeGraph100 = TypeGraphBasic_TypeGraph100 if TypeGraphBasic_TypeGraph100 is not None else set()
        self.TypeGraphBasic_TypeGraph102 = TypeGraphBasic_TypeGraph102 if TypeGraphBasic_TypeGraph102 is not None else set()
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def TypeGraphBasic_TypeGraph98(self):
        return self.__TypeGraphBasic_TypeGraph98

    @TypeGraphBasic_TypeGraph98.setter
    def TypeGraphBasic_TypeGraph98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph98", None)
        self.__TypeGraphBasic_TypeGraph98 = value if value is not None else set()
        
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
    def TypeGraphBasic_TypeGraph102(self):
        return self.__TypeGraphBasic_TypeGraph102

    @TypeGraphBasic_TypeGraph102.setter
    def TypeGraphBasic_TypeGraph102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph102", None)
        self.__TypeGraphBasic_TypeGraph102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphBasic_TClass103"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass103", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphBasic_TClass103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphBasic_TClass103"):
                    opp_val = getattr(item, "TypeGraphBasic_TClass103", None)
                    
                    setattr(item, "TypeGraphBasic_TClass103", self)
                    

    @property
    def TypeGraphBasic_TypeGraph100(self):
        return self.__TypeGraphBasic_TypeGraph100

    @TypeGraphBasic_TypeGraph100.setter
    def TypeGraphBasic_TypeGraph100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TypeGraph__TypeGraphBasic_TypeGraph100", None)
        self.__TypeGraphBasic_TypeGraph100 = value if value is not None else set()
        
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
                    

class TypeGraphBasic_TParameter:

    pass
class TypeGraphBasic_TParameterList:

    pass
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
            if hasattr(old_value, "TypeGraphBasic_TypeGraph98"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph98"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph98", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class TMember:

    pass
class TypeGraphBasic_TMethodDefinition(TMember):

    pass
class TypeGraphBasic_TFieldDefinition(TMember):

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
            if hasattr(old_value, "TypeGraphBasic_TypeGraph100"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph100"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph100", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph100", set([self]))
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
class TypeGraphBasic_TSignature(ABC):

    pass
class TypeGraphBasic_TPackage:

    def __init__(self, tName: str, 1: "TypeGraphBasic_TClass" = None, 70: set["TypeGraphBasic_TClass"] = None, 75: "TypeGraphBasic_TPackage" = None, 74: set["TypeGraphBasic_TPackage"] = None, 79: "TypeGraphBasic_TPackage" = None, 78: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TPackage: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self.1 = 1
        self.70 = 70 if 70 is not None else set()
        self.75 = 75
        self.74 = 74 if 74 is not None else set()
        self.79 = 79
        self.78 = 78
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
        self.__75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "74"):
                opp_val = getattr(old_value, "74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "74"):
                opp_val = getattr(value, "74", None)
                if opp_val is None:
                    setattr(value, "74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 78(self):
        return self.__78

    @78.setter
    def 78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__78", None)
        self.__78 = value
        
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
    def 74(self):
        return self.__74

    @74.setter
    def 74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__74", None)
        self.__74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "75"):
                    opp_val = getattr(item, "75", None)
                    
                    if opp_val == self:
                        setattr(item, "75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "75"):
                    opp_val = getattr(item, "75", None)
                    
                    setattr(item, "75", self)
                    

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
            if hasattr(old_value, "78"):
                opp_val = getattr(old_value, "78", None)
                if opp_val == self:
                    setattr(old_value, "78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "78"):
                opp_val = getattr(value, "78", None)
                setattr(value, "78", self)

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
    def 70(self):
        return self.__70

    @70.setter
    def 70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__70", None)
        self.__70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "71"):
                    opp_val = getattr(item, "71", None)
                    
                    if opp_val == self:
                        setattr(item, "71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "71"):
                    opp_val = getattr(item, "71", None)
                    
                    setattr(item, "71", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TPackage__1", None)
        self.__1 = value
        
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

class TypeGraphBasic_TClass:

    def __init__(self, tName: str, : "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass: set["TypeGraphBasic_TSignature"] = None, TypeGraphBasic_TClass4: set["TypeGraphBasic_TMember"] = None, 8: "TypeGraphBasic_TClass" = None, 7: "TypeGraphBasic_TClass" = None, 12: "TypeGraphBasic_TClass" = None, 11: set["TypeGraphBasic_TClass"] = None, 71: "TypeGraphBasic_TPackage" = None, TypeGraphBasic_TClass34: "TypeGraphBasic_TFieldSignature" = None, TypeGraphBasic_TClass61: "TypeGraphBasic_TMethodDefinition" = None, TypeGraphBasic_TClass89: "TypeGraphBasic_TParameter" = None, TypeGraphBasic_TClass103: "TypeGraphBasic_TypeGraph" = None):
        self.tName = tName
        self. = 
        self.TypeGraphBasic_TClass = TypeGraphBasic_TClass if TypeGraphBasic_TClass is not None else set()
        self.TypeGraphBasic_TClass4 = TypeGraphBasic_TClass4 if TypeGraphBasic_TClass4 is not None else set()
        self.8 = 8
        self.7 = 7
        self.12 = 12
        self.11 = 11 if 11 is not None else set()
        self.71 = 71
        self.TypeGraphBasic_TClass34 = TypeGraphBasic_TClass34
        self.TypeGraphBasic_TClass61 = TypeGraphBasic_TClass61
        self.TypeGraphBasic_TClass89 = TypeGraphBasic_TClass89
        self.TypeGraphBasic_TClass103 = TypeGraphBasic_TClass103
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

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
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "11"):
                opp_val = getattr(old_value, "11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "11"):
                opp_val = getattr(value, "11", None)
                if opp_val is None:
                    setattr(value, "11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass103(self):
        return self.__TypeGraphBasic_TClass103

    @TypeGraphBasic_TClass103.setter
    def TypeGraphBasic_TClass103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass103", None)
        self.__TypeGraphBasic_TClass103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphBasic_TypeGraph102"):
                opp_val = getattr(old_value, "TypeGraphBasic_TypeGraph102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphBasic_TypeGraph102"):
                opp_val = getattr(value, "TypeGraphBasic_TypeGraph102", None)
                if opp_val is None:
                    setattr(value, "TypeGraphBasic_TypeGraph102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass4(self):
        return self.__TypeGraphBasic_TClass4

    @TypeGraphBasic_TClass4.setter
    def TypeGraphBasic_TClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass4", None)
        self.__TypeGraphBasic_TClass4 = value if value is not None else set()
        
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
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "8"):
                opp_val = getattr(old_value, "8", None)
                if opp_val == self:
                    setattr(old_value, "8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "8"):
                opp_val = getattr(value, "8", None)
                setattr(value, "8", self)

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
            if hasattr(old_value, "1"):
                opp_val = getattr(old_value, "1", None)
                if opp_val == self:
                    setattr(old_value, "1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "1"):
                opp_val = getattr(value, "1", None)
                setattr(value, "1", self)

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
    def 71(self):
        return self.__71

    @71.setter
    def 71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__71", None)
        self.__71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "70"):
                opp_val = getattr(old_value, "70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "70"):
                opp_val = getattr(value, "70", None)
                if opp_val is None:
                    setattr(value, "70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeGraphBasic_TClass89(self):
        return self.__TypeGraphBasic_TClass89

    @TypeGraphBasic_TClass89.setter
    def TypeGraphBasic_TClass89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__TypeGraphBasic_TClass89", None)
        self.__TypeGraphBasic_TClass89 = value
        
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
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphBasic_TClass__11", None)
        self.__11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    if opp_val == self:
                        setattr(item, "12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    setattr(item, "12", self)
                    

class TSignature:

    pass
class TypeGraphBasic_TFieldSignature(TSignature):

    pass
class TypeGraphBasic_TMethodSignature(TSignature):

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TAnnotatable:

    pass
class TSignature:

    pass
class basic_TMethodSignature(TSignature):

    pass
class TMember:

    pass
class basic_TMethodDefinition(TMember):

    pass
class basic_TFieldDefinition(TMember):

    pass
class basic_TFieldSignature(TSignature):

    pass
class basic_TElementWithId(ABC):

    def __init__(self, ID: int):
        self.ID = ID
        
    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

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
class basic_TAbstractType(TAnnotatable, TElementWithId):

    def __init__(self, tName: str, tLib: bool, basic_TAbstractType: "basic_TFieldSignature" = None, 51: "basic_TMember" = None, basic_TAbstractType84: "basic_TMethodDefinition" = None, basic_TAbstractType94: "basic_TMethodSignature" = None, 111: "basic_TPackage" = None, basic_TAbstractType123: "basic_TParameter" = None, 147: "basic_TypeGraph" = None, 162: "basic_TypeGraph" = None, 165: "basic_TPackage" = None, basic_TAbstractType168: set["basic_TSignature"] = None, 170: set["basic_TMember"] = None):
        self.tName = tName
        self.tLib = tLib
        self.basic_TAbstractType = basic_TAbstractType
        self.51 = 51
        self.basic_TAbstractType84 = basic_TAbstractType84
        self.basic_TAbstractType94 = basic_TAbstractType94
        self.111 = 111
        self.basic_TAbstractType123 = basic_TAbstractType123
        self.147 = 147
        self.162 = 162
        self.165 = 165
        self.basic_TAbstractType168 = basic_TAbstractType168 if basic_TAbstractType168 is not None else set()
        self.170 = 170 if 170 is not None else set()
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def tLib(self) -> bool:
        return self.__tLib

    @tLib.setter
    def tLib(self, tLib: bool):
        self.__tLib = tLib

    @property
    def 51(self):
        return self.__51

    @51.setter
    def 51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__51", None)
        self.__51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "50"):
                opp_val = getattr(old_value, "50", None)
                if opp_val == self:
                    setattr(old_value, "50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "50"):
                opp_val = getattr(value, "50", None)
                setattr(value, "50", self)

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
    def 162(self):
        return self.__162

    @162.setter
    def 162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__162", None)
        self.__162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "163"):
                opp_val = getattr(old_value, "163", None)
                if opp_val == self:
                    setattr(old_value, "163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "163"):
                opp_val = getattr(value, "163", None)
                setattr(value, "163", self)

    @property
    def 147(self):
        return self.__147

    @147.setter
    def 147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__147", None)
        self.__147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "146"):
                opp_val = getattr(old_value, "146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "146"):
                opp_val = getattr(value, "146", None)
                if opp_val is None:
                    setattr(value, "146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 111(self):
        return self.__111

    @111.setter
    def 111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__111", None)
        self.__111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "110"):
                opp_val = getattr(old_value, "110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "110"):
                opp_val = getattr(value, "110", None)
                if opp_val is None:
                    setattr(value, "110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 165(self):
        return self.__165

    @165.setter
    def 165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__165", None)
        self.__165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "166"):
                opp_val = getattr(old_value, "166", None)
                if opp_val == self:
                    setattr(old_value, "166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "166"):
                opp_val = getattr(value, "166", None)
                setattr(value, "166", self)

    @property
    def basic_TAbstractType84(self):
        return self.__basic_TAbstractType84

    @basic_TAbstractType84.setter
    def basic_TAbstractType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType84", None)
        self.__basic_TAbstractType84 = value
        
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

    @property
    def basic_TAbstractType123(self):
        return self.__basic_TAbstractType123

    @basic_TAbstractType123.setter
    def basic_TAbstractType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType123", None)
        self.__basic_TAbstractType123 = value
        
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
    def basic_TAbstractType94(self):
        return self.__basic_TAbstractType94

    @basic_TAbstractType94.setter
    def basic_TAbstractType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType94", None)
        self.__basic_TAbstractType94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basic_TMethodSignature93"):
                opp_val = getattr(old_value, "basic_TMethodSignature93", None)
                if opp_val == self:
                    setattr(old_value, "basic_TMethodSignature93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TMethodSignature93"):
                opp_val = getattr(value, "basic_TMethodSignature93", None)
                setattr(value, "basic_TMethodSignature93", self)

    @property
    def 170(self):
        return self.__170

    @170.setter
    def 170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__170", None)
        self.__170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "171"):
                    opp_val = getattr(item, "171", None)
                    
                    if opp_val == self:
                        setattr(item, "171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "171"):
                    opp_val = getattr(item, "171", None)
                    
                    setattr(item, "171", self)
                    

    @property
    def basic_TAbstractType168(self):
        return self.__basic_TAbstractType168

    @basic_TAbstractType168.setter
    def basic_TAbstractType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TAbstractType__basic_TAbstractType168", None)
        self.__basic_TAbstractType168 = value if value is not None else set()
        
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
                    

class basic_TPackage(TAnnotatable, TElementWithId):

    def __init__(self, tName: str, 96: "basic_TypeGraph" = None, 101: "basic_TPackage" = None, 100: set["basic_TPackage"] = None, 105: "basic_TPackage" = None, 104: "basic_TPackage" = None, basic_TPackage: set["basic_TClass"] = None, basic_TPackage108: set["basic_TInterface"] = None, 110: set["basic_TAbstractType"] = None, basic_TPackage113: "basic_TypeGraph" = None, 132: "basic_TypeGraph" = None, 166: "basic_TAbstractType" = None):
        self.tName = tName
        self.96 = 96
        self.101 = 101
        self.100 = 100 if 100 is not None else set()
        self.105 = 105
        self.104 = 104
        self.basic_TPackage = basic_TPackage if basic_TPackage is not None else set()
        self.basic_TPackage108 = basic_TPackage108 if basic_TPackage108 is not None else set()
        self.110 = 110 if 110 is not None else set()
        self.basic_TPackage113 = basic_TPackage113
        self.132 = 132
        self.166 = 166
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def 110(self):
        return self.__110

    @110.setter
    def 110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__110", None)
        self.__110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "111"):
                    opp_val = getattr(item, "111", None)
                    
                    if opp_val == self:
                        setattr(item, "111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "111"):
                    opp_val = getattr(item, "111", None)
                    
                    setattr(item, "111", self)
                    

    @property
    def 104(self):
        return self.__104

    @104.setter
    def 104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__104", None)
        self.__104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "105"):
                opp_val = getattr(old_value, "105", None)
                if opp_val == self:
                    setattr(old_value, "105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "105"):
                opp_val = getattr(value, "105", None)
                setattr(value, "105", self)

    @property
    def 166(self):
        return self.__166

    @166.setter
    def 166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__166", None)
        self.__166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "165"):
                opp_val = getattr(old_value, "165", None)
                if opp_val == self:
                    setattr(old_value, "165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "165"):
                opp_val = getattr(value, "165", None)
                setattr(value, "165", self)

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
    def 101(self):
        return self.__101

    @101.setter
    def 101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__101", None)
        self.__101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "100"):
                opp_val = getattr(old_value, "100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "100"):
                opp_val = getattr(value, "100", None)
                if opp_val is None:
                    setattr(value, "100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic_TPackage108(self):
        return self.__basic_TPackage108

    @basic_TPackage108.setter
    def basic_TPackage108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__basic_TPackage108", None)
        self.__basic_TPackage108 = value if value is not None else set()
        
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
                    

    @property
    def 100(self):
        return self.__100

    @100.setter
    def 100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__100", None)
        self.__100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "101"):
                    opp_val = getattr(item, "101", None)
                    
                    if opp_val == self:
                        setattr(item, "101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "101"):
                    opp_val = getattr(item, "101", None)
                    
                    setattr(item, "101", self)
                    

    @property
    def 132(self):
        return self.__132

    @132.setter
    def 132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__132", None)
        self.__132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "131"):
                opp_val = getattr(old_value, "131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "131"):
                opp_val = getattr(value, "131", None)
                if opp_val is None:
                    setattr(value, "131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basic_TPackage113(self):
        return self.__basic_TPackage113

    @basic_TPackage113.setter
    def basic_TPackage113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__basic_TPackage113", None)
        self.__basic_TPackage113 = value
        
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
    def 96(self):
        return self.__96

    @96.setter
    def 96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__96", None)
        self.__96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "97"):
                opp_val = getattr(old_value, "97", None)
                if opp_val == self:
                    setattr(old_value, "97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "97"):
                opp_val = getattr(value, "97", None)
                setattr(value, "97", self)

    @property
    def 105(self):
        return self.__105

    @105.setter
    def 105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TPackage__105", None)
        self.__105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "104"):
                opp_val = getattr(old_value, "104", None)
                if opp_val == self:
                    setattr(old_value, "104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "104"):
                opp_val = getattr(value, "104", None)
                setattr(value, "104", self)

class basic_TMethod(TElementWithId):

    def __init__(self, tName: str, 59: "basic_TypeGraph" = None, 62: set["basic_TMethodSignature"] = None, 87: "basic_TMethodSignature" = None, 135: "basic_TypeGraph" = None):
        self.tName = tName
        self.59 = 59
        self.62 = 62 if 62 is not None else set()
        self.87 = 87
        self.135 = 135
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def 59(self):
        return self.__59

    @59.setter
    def 59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__59", None)
        self.__59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "60"):
                opp_val = getattr(old_value, "60", None)
                if opp_val == self:
                    setattr(old_value, "60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "60"):
                opp_val = getattr(value, "60", None)
                setattr(value, "60", self)

    @property
    def 87(self):
        return self.__87

    @87.setter
    def 87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__87", None)
        self.__87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "86"):
                opp_val = getattr(old_value, "86", None)
                if opp_val == self:
                    setattr(old_value, "86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "86"):
                opp_val = getattr(value, "86", None)
                setattr(value, "86", self)

    @property
    def 135(self):
        return self.__135

    @135.setter
    def 135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__135", None)
        self.__135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "134"):
                opp_val = getattr(old_value, "134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "134"):
                opp_val = getattr(value, "134", None)
                if opp_val is None:
                    setattr(value, "134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 62(self):
        return self.__62

    @62.setter
    def 62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TMethod__62", None)
        self.__62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "63"):
                    opp_val = getattr(item, "63", None)
                    
                    if opp_val == self:
                        setattr(item, "63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "63"):
                    opp_val = getattr(item, "63", None)
                    
                    setattr(item, "63", self)
                    

class basic_TField(TElementWithId):

    def __init__(self, tName: str, 26: set["basic_TFieldSignature"] = None, 29: "basic_TypeGraph" = None, 47: "basic_TFieldSignature" = None, 138: "basic_TypeGraph" = None):
        self.tName = tName
        self.26 = 26 if 26 is not None else set()
        self.29 = 29
        self.47 = 47
        self.138 = 138
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def 138(self):
        return self.__138

    @138.setter
    def 138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__138", None)
        self.__138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "137"):
                opp_val = getattr(old_value, "137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "137"):
                opp_val = getattr(value, "137", None)
                if opp_val is None:
                    setattr(value, "137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 47(self):
        return self.__47

    @47.setter
    def 47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__47", None)
        self.__47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "46"):
                opp_val = getattr(old_value, "46", None)
                if opp_val == self:
                    setattr(old_value, "46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "46"):
                opp_val = getattr(value, "46", None)
                setattr(value, "46", self)

    @property
    def 29(self):
        return self.__29

    @29.setter
    def 29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__29", None)
        self.__29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "30"):
                opp_val = getattr(old_value, "30", None)
                if opp_val == self:
                    setattr(old_value, "30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "30"):
                opp_val = getattr(value, "30", None)
                setattr(value, "30", self)

    @property
    def 26(self):
        return self.__26

    @26.setter
    def 26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TField__26", None)
        self.__26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "27"):
                    opp_val = getattr(item, "27", None)
                    
                    if opp_val == self:
                        setattr(item, "27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "27"):
                    opp_val = getattr(item, "27", None)
                    
                    setattr(item, "27", self)
                    

class basic_TSignature(TAnnotatable, TElementWithId):

    pass
class basic_TypeGraph(TElementWithId):

    def __init__(self, tName: str, 30: "basic_TField" = None, 97: "basic_TPackage" = None, 60: "basic_TMethod" = None, 134: set["basic_TMethod"] = None, basic_TypeGraph: "basic_TPackage" = None, 131: set["basic_TPackage"] = None, 137: set["basic_TField"] = None, basic_TypeGraph140: set["basic_TClass"] = None, basic_TypeGraph143: set["basic_TInterface"] = None, 146: set["basic_TAbstractType"] = None, basic_TypeGraph149: set["basic_TAnnotationType"] = None, 163: "basic_TAbstractType" = None):
        self.tName = tName
        self.30 = 30
        self.97 = 97
        self.60 = 60
        self.134 = 134 if 134 is not None else set()
        self.basic_TypeGraph = basic_TypeGraph
        self.131 = 131 if 131 is not None else set()
        self.137 = 137 if 137 is not None else set()
        self.basic_TypeGraph140 = basic_TypeGraph140 if basic_TypeGraph140 is not None else set()
        self.basic_TypeGraph143 = basic_TypeGraph143 if basic_TypeGraph143 is not None else set()
        self.146 = 146 if 146 is not None else set()
        self.basic_TypeGraph149 = basic_TypeGraph149 if basic_TypeGraph149 is not None else set()
        self.163 = 163
        
    @property
    def tName(self) -> str:
        return self.__tName

    @tName.setter
    def tName(self, tName: str):
        self.__tName = tName

    @property
    def basic_TypeGraph140(self):
        return self.__basic_TypeGraph140

    @basic_TypeGraph140.setter
    def basic_TypeGraph140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph140", None)
        self.__basic_TypeGraph140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TClass141"):
                    opp_val = getattr(item, "basic_TClass141", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TClass141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TClass141"):
                    opp_val = getattr(item, "basic_TClass141", None)
                    
                    setattr(item, "basic_TClass141", self)
                    

    @property
    def 131(self):
        return self.__131

    @131.setter
    def 131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__131", None)
        self.__131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "132"):
                    opp_val = getattr(item, "132", None)
                    
                    if opp_val == self:
                        setattr(item, "132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "132"):
                    opp_val = getattr(item, "132", None)
                    
                    setattr(item, "132", self)
                    

    @property
    def 137(self):
        return self.__137

    @137.setter
    def 137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__137", None)
        self.__137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "138"):
                    opp_val = getattr(item, "138", None)
                    
                    if opp_val == self:
                        setattr(item, "138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "138"):
                    opp_val = getattr(item, "138", None)
                    
                    setattr(item, "138", self)
                    

    @property
    def 163(self):
        return self.__163

    @163.setter
    def 163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__163", None)
        self.__163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "162"):
                opp_val = getattr(old_value, "162", None)
                if opp_val == self:
                    setattr(old_value, "162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "162"):
                opp_val = getattr(value, "162", None)
                setattr(value, "162", self)

    @property
    def basic_TypeGraph149(self):
        return self.__basic_TypeGraph149

    @basic_TypeGraph149.setter
    def basic_TypeGraph149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph149", None)
        self.__basic_TypeGraph149 = value if value is not None else set()
        
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
                    

    @property
    def 146(self):
        return self.__146

    @146.setter
    def 146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__146", None)
        self.__146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "147"):
                    opp_val = getattr(item, "147", None)
                    
                    if opp_val == self:
                        setattr(item, "147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "147"):
                    opp_val = getattr(item, "147", None)
                    
                    setattr(item, "147", self)
                    

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
            if hasattr(old_value, "basic_TPackage113"):
                opp_val = getattr(old_value, "basic_TPackage113", None)
                if opp_val == self:
                    setattr(old_value, "basic_TPackage113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basic_TPackage113"):
                opp_val = getattr(value, "basic_TPackage113", None)
                setattr(value, "basic_TPackage113", self)

    @property
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__30", None)
        self.__30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    @property
    def 134(self):
        return self.__134

    @134.setter
    def 134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__134", None)
        self.__134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "135"):
                    opp_val = getattr(item, "135", None)
                    
                    if opp_val == self:
                        setattr(item, "135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "135"):
                    opp_val = getattr(item, "135", None)
                    
                    setattr(item, "135", self)
                    

    @property
    def 97(self):
        return self.__97

    @97.setter
    def 97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__97", None)
        self.__97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "96"):
                opp_val = getattr(old_value, "96", None)
                if opp_val == self:
                    setattr(old_value, "96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "96"):
                opp_val = getattr(value, "96", None)
                setattr(value, "96", self)

    @property
    def 60(self):
        return self.__60

    @60.setter
    def 60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__60", None)
        self.__60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "59"):
                opp_val = getattr(old_value, "59", None)
                if opp_val == self:
                    setattr(old_value, "59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "59"):
                opp_val = getattr(value, "59", None)
                setattr(value, "59", self)

    @property
    def basic_TypeGraph143(self):
        return self.__basic_TypeGraph143

    @basic_TypeGraph143.setter
    def basic_TypeGraph143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basic_TypeGraph__basic_TypeGraph143", None)
        self.__basic_TypeGraph143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basic_TInterface144"):
                    opp_val = getattr(item, "basic_TInterface144", None)
                    
                    if opp_val == self:
                        setattr(item, "basic_TInterface144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basic_TInterface144"):
                    opp_val = getattr(item, "basic_TInterface144", None)
                    
                    setattr(item, "basic_TInterface144", self)
                    

class basic_TMember(TAnnotatable, TElementWithId):

    pass
class basic_TParameterList(TElementWithId):

    pass
class basic_TParameter(TElementWithId):

    pass
class basic_TAnnotation(TElementWithId):

    pass
class basic_TAccess(TElementWithId):

    pass
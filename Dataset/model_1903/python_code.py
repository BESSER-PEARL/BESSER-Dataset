from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionType(Enum):
    FRONT = "FRONT"
    BEHIND = "BEHIND"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class Mode(Enum):
    OFF = "OFF"
    ON = "ON"
class Where(Enum):
    INDOOR = "INDOOR"
    OUTDOOR = "OUTDOOR"
class TypePrimitif(Enum):
    boolType = "boolType"
    realType = "realType"
    intType = "intType"
    stringType = "stringType"
class EBool(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


############################################
# Definition of Classes
############################################

class ConnectionType:

    pass
class drn_Wifi(ConnectionType):

    pass
class drn_Bluetooth(ConnectionType):

    pass
class drn_Element:

    def __init__(self, name: str, drn_Element: "drn_Definition" = None, drn_Element63: "drn_TypeGeneric" = None):
        self.name = name
        self.drn_Element = drn_Element
        self.drn_Element63 = drn_Element63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Element(self):
        return self.__drn_Element

    @drn_Element.setter
    def drn_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Element__drn_Element", None)
        self.__drn_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Definition52"):
                opp_val = getattr(old_value, "drn_Definition52", None)
                if opp_val == self:
                    setattr(old_value, "drn_Definition52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Definition52"):
                opp_val = getattr(value, "drn_Definition52", None)
                setattr(value, "drn_Definition52", self)

    @property
    def drn_Element63(self):
        return self.__drn_Element63

    @drn_Element63.setter
    def drn_Element63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Element__drn_Element63", None)
        self.__drn_Element63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_TypeGeneric62"):
                opp_val = getattr(old_value, "drn_TypeGeneric62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_TypeGeneric62"):
                opp_val = getattr(value, "drn_TypeGeneric62", None)
                if opp_val is None:
                    setattr(value, "drn_TypeGeneric62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_Definition:

    def __init__(self, real: str, int: str, bool: str, text: str, drn_Definition: "drn_Declaration" = None, drn_Definition52: "drn_Element" = None, drn_Definition60: "drn_RefDevice" = None):
        self.real = real
        self.int = int
        self.bool = bool
        self.text = text
        self.drn_Definition = drn_Definition
        self.drn_Definition52 = drn_Definition52
        self.drn_Definition60 = drn_Definition60
        
    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

    @property
    def int(self) -> str:
        return self.__int

    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def real(self) -> str:
        return self.__real

    @real.setter
    def real(self, real: str):
        self.__real = real

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def drn_Definition52(self):
        return self.__drn_Definition52

    @drn_Definition52.setter
    def drn_Definition52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Definition__drn_Definition52", None)
        self.__drn_Definition52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Element"):
                opp_val = getattr(old_value, "drn_Element", None)
                if opp_val == self:
                    setattr(old_value, "drn_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Element"):
                opp_val = getattr(value, "drn_Element", None)
                setattr(value, "drn_Element", self)

    @property
    def drn_Definition(self):
        return self.__drn_Definition

    @drn_Definition.setter
    def drn_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Definition__drn_Definition", None)
        self.__drn_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Declaration50"):
                opp_val = getattr(old_value, "drn_Declaration50", None)
                if opp_val == self:
                    setattr(old_value, "drn_Declaration50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Declaration50"):
                opp_val = getattr(value, "drn_Declaration50", None)
                setattr(value, "drn_Declaration50", self)

    @property
    def drn_Definition60(self):
        return self.__drn_Definition60

    @drn_Definition60.setter
    def drn_Definition60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Definition__drn_Definition60", None)
        self.__drn_Definition60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefDevice59"):
                opp_val = getattr(old_value, "drn_RefDevice59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefDevice59"):
                opp_val = getattr(value, "drn_RefDevice59", None)
                if opp_val is None:
                    setattr(value, "drn_RefDevice59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_RefDevice:

    def __init__(self, mode: str, drn_RefDevice: "drn_With" = None, drn_RefDevice56: "drn_Device" = None, drn_RefDevice59: set["drn_Definition"] = None):
        self.mode = mode
        self.drn_RefDevice = drn_RefDevice
        self.drn_RefDevice56 = drn_RefDevice56
        self.drn_RefDevice59 = drn_RefDevice59 if drn_RefDevice59 is not None else set()
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def drn_RefDevice(self):
        return self.__drn_RefDevice

    @drn_RefDevice.setter
    def drn_RefDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_RefDevice__drn_RefDevice", None)
        self.__drn_RefDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_With54"):
                opp_val = getattr(old_value, "drn_With54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_With54"):
                opp_val = getattr(value, "drn_With54", None)
                if opp_val is None:
                    setattr(value, "drn_With54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_RefDevice56(self):
        return self.__drn_RefDevice56

    @drn_RefDevice56.setter
    def drn_RefDevice56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_RefDevice__drn_RefDevice56", None)
        self.__drn_RefDevice56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Device57"):
                opp_val = getattr(old_value, "drn_Device57", None)
                if opp_val == self:
                    setattr(old_value, "drn_Device57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Device57"):
                opp_val = getattr(value, "drn_Device57", None)
                setattr(value, "drn_Device57", self)

    @property
    def drn_RefDevice59(self):
        return self.__drn_RefDevice59

    @drn_RefDevice59.setter
    def drn_RefDevice59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_RefDevice__drn_RefDevice59", None)
        self.__drn_RefDevice59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Definition60"):
                    opp_val = getattr(item, "drn_Definition60", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Definition60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Definition60"):
                    opp_val = getattr(item, "drn_Definition60", None)
                    
                    setattr(item, "drn_Definition60", self)
                    

class DepXYZ_IMPL:

    pass
class drn_Flip(DepXYZ_IMPL):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_Declaration:

    def __init__(self, typePrimitif: str, name: str, drn_Declaration: "drn_Device" = None, drn_Declaration47: "drn_TypeGeneric" = None, drn_Declaration50: "drn_Definition" = None):
        self.typePrimitif = typePrimitif
        self.name = name
        self.drn_Declaration = drn_Declaration
        self.drn_Declaration47 = drn_Declaration47
        self.drn_Declaration50 = drn_Declaration50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typePrimitif(self) -> str:
        return self.__typePrimitif

    @typePrimitif.setter
    def typePrimitif(self, typePrimitif: str):
        self.__typePrimitif = typePrimitif

    @property
    def drn_Declaration50(self):
        return self.__drn_Declaration50

    @drn_Declaration50.setter
    def drn_Declaration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Declaration__drn_Declaration50", None)
        self.__drn_Declaration50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Definition"):
                opp_val = getattr(old_value, "drn_Definition", None)
                if opp_val == self:
                    setattr(old_value, "drn_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Definition"):
                opp_val = getattr(value, "drn_Definition", None)
                setattr(value, "drn_Definition", self)

    @property
    def drn_Declaration(self):
        return self.__drn_Declaration

    @drn_Declaration.setter
    def drn_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Declaration__drn_Declaration", None)
        self.__drn_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Device45"):
                opp_val = getattr(old_value, "drn_Device45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Device45"):
                opp_val = getattr(value, "drn_Device45", None)
                if opp_val is None:
                    setattr(value, "drn_Device45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Declaration47(self):
        return self.__drn_Declaration47

    @drn_Declaration47.setter
    def drn_Declaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Declaration__drn_Declaration47", None)
        self.__drn_Declaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_TypeGeneric48"):
                opp_val = getattr(old_value, "drn_TypeGeneric48", None)
                if opp_val == self:
                    setattr(old_value, "drn_TypeGeneric48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_TypeGeneric48"):
                opp_val = getattr(value, "drn_TypeGeneric48", None)
                setattr(value, "drn_TypeGeneric48", self)

class DepYZ_IMPL:

    pass
class drn_CARREYZ(DepYZ_IMPL):

    def __init__(self, coteCST: int):
        self.coteCST = coteCST
        
    @property
    def coteCST(self) -> int:
        return self.__coteCST

    @coteCST.setter
    def coteCST(self, coteCST: int):
        self.__coteCST = coteCST

class drn_CERCLEYZ(DepYZ_IMPL):

    def __init__(self, rayonCST: int):
        self.rayonCST = rayonCST
        
    @property
    def rayonCST(self) -> int:
        return self.__rayonCST

    @rayonCST.setter
    def rayonCST(self, rayonCST: int):
        self.__rayonCST = rayonCST

class DepXZ_IMPL:

    pass
class drn_CARREXZ(DepXZ_IMPL):

    def __init__(self, coteCST: int):
        self.coteCST = coteCST
        
    @property
    def coteCST(self) -> int:
        return self.__coteCST

    @coteCST.setter
    def coteCST(self, coteCST: int):
        self.__coteCST = coteCST

class drn_CERCLEXZ(DepXZ_IMPL):

    def __init__(self, rayonCST: int):
        self.rayonCST = rayonCST
        
    @property
    def rayonCST(self) -> int:
        return self.__rayonCST

    @rayonCST.setter
    def rayonCST(self, rayonCST: int):
        self.__rayonCST = rayonCST

class DepX_Impl:

    pass
class drn_RIGHT(DepX_Impl):

    pass
class drn_LEFT(DepX_Impl):

    pass
class DepXY_IMPL:

    pass
class drn_CARREXY(DepXY_IMPL):

    def __init__(self, coteCST: int):
        self.coteCST = coteCST
        
    @property
    def coteCST(self) -> int:
        return self.__coteCST

    @coteCST.setter
    def coteCST(self, coteCST: int):
        self.__coteCST = coteCST

class drn_CERCLEXY(DepXY_IMPL):

    def __init__(self, rayonCST: int):
        self.rayonCST = rayonCST
        
    @property
    def rayonCST(self) -> int:
        return self.__rayonCST

    @rayonCST.setter
    def rayonCST(self, rayonCST: int):
        self.__rayonCST = rayonCST

class DepZ_Impl:

    pass
class drn_DOWN(DepZ_Impl):

    pass
class drn_UP(DepZ_Impl):

    pass
class Movement:

    pass
class drn_Land(Movement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_Wait(Movement):

    def __init__(self, name: str, tempsCST: int):
        self.name = name
        self.tempsCST = tempsCST
        
    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_DepYZ_IMPL(Movement):

    def __init__(self, name: str, tempsCST: int):
        self.name = name
        self.tempsCST = tempsCST
        
    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_DepXYZ_IMPL(Movement):

    pass
class drn_DepXZ_IMPL(Movement):

    def __init__(self, name: str, tempsCST: int):
        self.name = name
        self.tempsCST = tempsCST
        
    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_DepXY_IMPL(Movement):

    def __init__(self, name: str, tempsCST: int):
        self.name = name
        self.tempsCST = tempsCST
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

class drn_TakeOff(Movement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_With:

    def __init__(self, name: str, drn_With: "drn_Expression" = None, drn_With54: set["drn_RefDevice"] = None):
        self.name = name
        self.drn_With = drn_With
        self.drn_With54 = drn_With54 if drn_With54 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_With54(self):
        return self.__drn_With54

    @drn_With54.setter
    def drn_With54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_With__drn_With54", None)
        self.__drn_With54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_RefDevice"):
                    opp_val = getattr(item, "drn_RefDevice", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_RefDevice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_RefDevice"):
                    opp_val = getattr(item, "drn_RefDevice", None)
                    
                    setattr(item, "drn_RefDevice", self)
                    

    @property
    def drn_With(self):
        return self.__drn_With

    @drn_With.setter
    def drn_With(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_With__drn_With", None)
        self.__drn_With = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Expression25"):
                opp_val = getattr(old_value, "drn_Expression25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Expression25"):
                opp_val = getattr(value, "drn_Expression25", None)
                if opp_val is None:
                    setattr(value, "drn_Expression25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_Movement:

    pass
class drn_Expression:

    def __init__(self, repeatCST: int, drn_Expression: "drn_Assignement" = None, drn_Expression23: "drn_Movement" = None, drn_Expression25: set["drn_With"] = None, drn_Expression28: "drn_Expression" = None, drn_Expression26: set["drn_Expression"] = None):
        self.repeatCST = repeatCST
        self.drn_Expression = drn_Expression
        self.drn_Expression23 = drn_Expression23
        self.drn_Expression25 = drn_Expression25 if drn_Expression25 is not None else set()
        self.drn_Expression28 = drn_Expression28
        self.drn_Expression26 = drn_Expression26 if drn_Expression26 is not None else set()
        
    @property
    def repeatCST(self) -> int:
        return self.__repeatCST

    @repeatCST.setter
    def repeatCST(self, repeatCST: int):
        self.__repeatCST = repeatCST

    @property
    def drn_Expression26(self):
        return self.__drn_Expression26

    @drn_Expression26.setter
    def drn_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression26", None)
        self.__drn_Expression26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Expression28"):
                    opp_val = getattr(item, "drn_Expression28", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Expression28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Expression28"):
                    opp_val = getattr(item, "drn_Expression28", None)
                    
                    setattr(item, "drn_Expression28", self)
                    

    @property
    def drn_Expression23(self):
        return self.__drn_Expression23

    @drn_Expression23.setter
    def drn_Expression23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression23", None)
        self.__drn_Expression23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Movement"):
                opp_val = getattr(old_value, "drn_Movement", None)
                if opp_val == self:
                    setattr(old_value, "drn_Movement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Movement"):
                opp_val = getattr(value, "drn_Movement", None)
                setattr(value, "drn_Movement", self)

    @property
    def drn_Expression25(self):
        return self.__drn_Expression25

    @drn_Expression25.setter
    def drn_Expression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression25", None)
        self.__drn_Expression25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_With"):
                    opp_val = getattr(item, "drn_With", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_With", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_With"):
                    opp_val = getattr(item, "drn_With", None)
                    
                    setattr(item, "drn_With", self)
                    

    @property
    def drn_Expression28(self):
        return self.__drn_Expression28

    @drn_Expression28.setter
    def drn_Expression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression28", None)
        self.__drn_Expression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Expression26"):
                opp_val = getattr(old_value, "drn_Expression26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Expression26"):
                opp_val = getattr(value, "drn_Expression26", None)
                if opp_val is None:
                    setattr(value, "drn_Expression26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Expression(self):
        return self.__drn_Expression

    @drn_Expression.setter
    def drn_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression", None)
        self.__drn_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Assignement21"):
                opp_val = getattr(old_value, "drn_Assignement21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Assignement21"):
                opp_val = getattr(value, "drn_Assignement21", None)
                if opp_val is None:
                    setattr(value, "drn_Assignement21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DepY_Impl:

    pass
class drn_BACKWARD(DepY_Impl):

    pass
class drn_FORWARD(DepY_Impl):

    pass
class drn_DepZ_Impl(Movement):

    def __init__(self, name: str, distanceCST: int, tempsCST: int, drn_DepZ_Impl: "drn_And" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepZ_Impl = drn_DepZ_Impl
        
    @property
    def distanceCST(self) -> int:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: int):
        self.__distanceCST = distanceCST

    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_DepZ_Impl(self):
        return self.__drn_DepZ_Impl

    @drn_DepZ_Impl.setter
    def drn_DepZ_Impl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepZ_Impl__drn_DepZ_Impl", None)
        self.__drn_DepZ_Impl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_And43"):
                opp_val = getattr(old_value, "drn_And43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And43"):
                opp_val = getattr(value, "drn_And43", None)
                if opp_val is None:
                    setattr(value, "drn_And43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_DepY_Impl(Movement):

    def __init__(self, name: str, distanceCST: int, tempsCST: int, drn_DepY_Impl: "drn_And" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepY_Impl = drn_DepY_Impl
        
    @property
    def distanceCST(self) -> int:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: int):
        self.__distanceCST = distanceCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def drn_DepY_Impl(self):
        return self.__drn_DepY_Impl

    @drn_DepY_Impl.setter
    def drn_DepY_Impl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepY_Impl__drn_DepY_Impl", None)
        self.__drn_DepY_Impl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_And41"):
                opp_val = getattr(old_value, "drn_And41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And41"):
                opp_val = getattr(value, "drn_And41", None)
                if opp_val is None:
                    setattr(value, "drn_And41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_DepX_Impl(Movement):

    def __init__(self, name: str, distanceCST: int, tempsCST: int, drn_DepX_Impl: "drn_And" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepX_Impl = drn_DepX_Impl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def distanceCST(self) -> int:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: int):
        self.__distanceCST = distanceCST

    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def drn_DepX_Impl(self):
        return self.__drn_DepX_Impl

    @drn_DepX_Impl.setter
    def drn_DepX_Impl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepX_Impl__drn_DepX_Impl", None)
        self.__drn_DepX_Impl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_And39"):
                opp_val = getattr(old_value, "drn_And39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And39"):
                opp_val = getattr(value, "drn_And39", None)
                if opp_val is None:
                    setattr(value, "drn_And39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_Rotate(Movement):

    def __init__(self, name: str, angleCST: str, tempsCST: int, drn_Rotate: "drn_And" = None):
        self.name = name
        self.angleCST = angleCST
        self.tempsCST = tempsCST
        self.drn_Rotate = drn_Rotate
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def angleCST(self) -> str:
        return self.__angleCST

    @angleCST.setter
    def angleCST(self, angleCST: str):
        self.__angleCST = angleCST

    @property
    def tempsCST(self) -> int:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: int):
        self.__tempsCST = tempsCST

    @property
    def drn_Rotate(self):
        return self.__drn_Rotate

    @drn_Rotate.setter
    def drn_Rotate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Rotate__drn_Rotate", None)
        self.__drn_Rotate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_And"):
                opp_val = getattr(old_value, "drn_And", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And"):
                opp_val = getattr(value, "drn_And", None)
                if opp_val is None:
                    setattr(value, "drn_And", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_And(Movement):

    def __init__(self, name: str, drn_And: set["drn_Rotate"] = None, drn_And39: set["drn_DepX_Impl"] = None, drn_And41: set["drn_DepY_Impl"] = None, drn_And43: set["drn_DepZ_Impl"] = None):
        self.name = name
        self.drn_And = drn_And if drn_And is not None else set()
        self.drn_And39 = drn_And39 if drn_And39 is not None else set()
        self.drn_And41 = drn_And41 if drn_And41 is not None else set()
        self.drn_And43 = drn_And43 if drn_And43 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_And(self):
        return self.__drn_And

    @drn_And.setter
    def drn_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And", None)
        self.__drn_And = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Rotate"):
                    opp_val = getattr(item, "drn_Rotate", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Rotate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Rotate"):
                    opp_val = getattr(item, "drn_Rotate", None)
                    
                    setattr(item, "drn_Rotate", self)
                    

    @property
    def drn_And41(self):
        return self.__drn_And41

    @drn_And41.setter
    def drn_And41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And41", None)
        self.__drn_And41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_DepY_Impl"):
                    opp_val = getattr(item, "drn_DepY_Impl", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_DepY_Impl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_DepY_Impl"):
                    opp_val = getattr(item, "drn_DepY_Impl", None)
                    
                    setattr(item, "drn_DepY_Impl", self)
                    

    @property
    def drn_And43(self):
        return self.__drn_And43

    @drn_And43.setter
    def drn_And43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And43", None)
        self.__drn_And43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_DepZ_Impl"):
                    opp_val = getattr(item, "drn_DepZ_Impl", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_DepZ_Impl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_DepZ_Impl"):
                    opp_val = getattr(item, "drn_DepZ_Impl", None)
                    
                    setattr(item, "drn_DepZ_Impl", self)
                    

    @property
    def drn_And39(self):
        return self.__drn_And39

    @drn_And39.setter
    def drn_And39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And39", None)
        self.__drn_And39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_DepX_Impl"):
                    opp_val = getattr(item, "drn_DepX_Impl", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_DepX_Impl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_DepX_Impl"):
                    opp_val = getattr(item, "drn_DepX_Impl", None)
                    
                    setattr(item, "drn_DepX_Impl", self)
                    

class drn_RefPartLib(Movement):

    pass
class drn_ConnectionType:

    def __init__(self, name: str, adress: str, drn_ConnectionType: "drn_Configuration" = None):
        self.name = name
        self.adress = adress
        self.drn_ConnectionType = drn_ConnectionType
        
    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_ConnectionType(self):
        return self.__drn_ConnectionType

    @drn_ConnectionType.setter
    def drn_ConnectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_ConnectionType__drn_ConnectionType", None)
        self.__drn_ConnectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Configuration14"):
                opp_val = getattr(old_value, "drn_Configuration14", None)
                if opp_val == self:
                    setattr(old_value, "drn_Configuration14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Configuration14"):
                opp_val = getattr(value, "drn_Configuration14", None)
                setattr(value, "drn_Configuration14", self)

class drn_Device:

    def __init__(self, name: str, drn_Device: "drn_Configuration" = None, drn_Device45: set["drn_Declaration"] = None, drn_Device57: "drn_RefDevice" = None):
        self.name = name
        self.drn_Device = drn_Device
        self.drn_Device45 = drn_Device45 if drn_Device45 is not None else set()
        self.drn_Device57 = drn_Device57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Device(self):
        return self.__drn_Device

    @drn_Device.setter
    def drn_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Device__drn_Device", None)
        self.__drn_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Configuration12"):
                opp_val = getattr(old_value, "drn_Configuration12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Configuration12"):
                opp_val = getattr(value, "drn_Configuration12", None)
                if opp_val is None:
                    setattr(value, "drn_Configuration12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Device45(self):
        return self.__drn_Device45

    @drn_Device45.setter
    def drn_Device45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Device__drn_Device45", None)
        self.__drn_Device45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Declaration"):
                    opp_val = getattr(item, "drn_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Declaration"):
                    opp_val = getattr(item, "drn_Declaration", None)
                    
                    setattr(item, "drn_Declaration", self)
                    

    @property
    def drn_Device57(self):
        return self.__drn_Device57

    @drn_Device57.setter
    def drn_Device57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Device__drn_Device57", None)
        self.__drn_Device57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefDevice56"):
                opp_val = getattr(old_value, "drn_RefDevice56", None)
                if opp_val == self:
                    setattr(old_value, "drn_RefDevice56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefDevice56"):
                opp_val = getattr(value, "drn_RefDevice56", None)
                setattr(value, "drn_RefDevice56", self)

class drn_TypeGeneric:

    def __init__(self, name: str, drn_TypeGeneric: "drn_Configuration" = None, drn_TypeGeneric48: "drn_Declaration" = None, drn_TypeGeneric62: set["drn_Element"] = None):
        self.name = name
        self.drn_TypeGeneric = drn_TypeGeneric
        self.drn_TypeGeneric48 = drn_TypeGeneric48
        self.drn_TypeGeneric62 = drn_TypeGeneric62 if drn_TypeGeneric62 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_TypeGeneric(self):
        return self.__drn_TypeGeneric

    @drn_TypeGeneric.setter
    def drn_TypeGeneric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_TypeGeneric__drn_TypeGeneric", None)
        self.__drn_TypeGeneric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Configuration10"):
                opp_val = getattr(old_value, "drn_Configuration10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Configuration10"):
                opp_val = getattr(value, "drn_Configuration10", None)
                if opp_val is None:
                    setattr(value, "drn_Configuration10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_TypeGeneric48(self):
        return self.__drn_TypeGeneric48

    @drn_TypeGeneric48.setter
    def drn_TypeGeneric48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_TypeGeneric__drn_TypeGeneric48", None)
        self.__drn_TypeGeneric48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Declaration47"):
                opp_val = getattr(old_value, "drn_Declaration47", None)
                if opp_val == self:
                    setattr(old_value, "drn_Declaration47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Declaration47"):
                opp_val = getattr(value, "drn_Declaration47", None)
                setattr(value, "drn_Declaration47", self)

    @property
    def drn_TypeGeneric62(self):
        return self.__drn_TypeGeneric62

    @drn_TypeGeneric62.setter
    def drn_TypeGeneric62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_TypeGeneric__drn_TypeGeneric62", None)
        self.__drn_TypeGeneric62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Element63"):
                    opp_val = getattr(item, "drn_Element63", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Element63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Element63"):
                    opp_val = getattr(item, "drn_Element63", None)
                    
                    setattr(item, "drn_Element63", self)
                    

class drn_RefPart(Movement):

    pass
class Surface:

    pass
class drn_MaxHeight(Surface):

    pass
class drn_MaxWidth(Surface):

    pass
class drn_MaxLength(Surface):

    pass
class InitialPosition:

    pass
class drn_InitialPositionX(InitialPosition):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class drn_InitialPositionY(InitialPosition):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class drn_InitialDirection(InitialPosition):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Limit:

    pass
class drn_MaxSpeed(Limit):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class drn_InitialPosition(Limit):

    pass
class drn_Surface(Limit):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class drn_Limit:

    def __init__(self, name: str, drn_Limit: "drn_Context" = None):
        self.name = name
        self.drn_Limit = drn_Limit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Limit(self):
        return self.__drn_Limit

    @drn_Limit.setter
    def drn_Limit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Limit__drn_Limit", None)
        self.__drn_Limit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Context19"):
                opp_val = getattr(old_value, "drn_Context19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Context19"):
                opp_val = getattr(value, "drn_Context19", None)
                if opp_val is None:
                    setattr(value, "drn_Context19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_Assignement:

    def __init__(self, name: str, drn_Assignement: "drn_Model" = None, drn_Assignement17: "drn_Library" = None, drn_Assignement36: "drn_RefPartLib" = None, drn_Assignement21: set["drn_Expression"] = None, drn_Assignement31: "drn_RefPart" = None):
        self.name = name
        self.drn_Assignement = drn_Assignement
        self.drn_Assignement17 = drn_Assignement17
        self.drn_Assignement36 = drn_Assignement36
        self.drn_Assignement21 = drn_Assignement21 if drn_Assignement21 is not None else set()
        self.drn_Assignement31 = drn_Assignement31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Assignement17(self):
        return self.__drn_Assignement17

    @drn_Assignement17.setter
    def drn_Assignement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement17", None)
        self.__drn_Assignement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Library16"):
                opp_val = getattr(old_value, "drn_Library16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Library16"):
                opp_val = getattr(value, "drn_Library16", None)
                if opp_val is None:
                    setattr(value, "drn_Library16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Assignement21(self):
        return self.__drn_Assignement21

    @drn_Assignement21.setter
    def drn_Assignement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement21", None)
        self.__drn_Assignement21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Expression"):
                    opp_val = getattr(item, "drn_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Expression"):
                    opp_val = getattr(item, "drn_Expression", None)
                    
                    setattr(item, "drn_Expression", self)
                    

    @property
    def drn_Assignement31(self):
        return self.__drn_Assignement31

    @drn_Assignement31.setter
    def drn_Assignement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement31", None)
        self.__drn_Assignement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefPart30"):
                opp_val = getattr(old_value, "drn_RefPart30", None)
                if opp_val == self:
                    setattr(old_value, "drn_RefPart30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefPart30"):
                opp_val = getattr(value, "drn_RefPart30", None)
                setattr(value, "drn_RefPart30", self)

    @property
    def drn_Assignement(self):
        return self.__drn_Assignement

    @drn_Assignement.setter
    def drn_Assignement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement", None)
        self.__drn_Assignement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Model6"):
                opp_val = getattr(old_value, "drn_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Model6"):
                opp_val = getattr(value, "drn_Model6", None)
                if opp_val is None:
                    setattr(value, "drn_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Assignement36(self):
        return self.__drn_Assignement36

    @drn_Assignement36.setter
    def drn_Assignement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement36", None)
        self.__drn_Assignement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefPartLib35"):
                opp_val = getattr(old_value, "drn_RefPartLib35", None)
                if opp_val == self:
                    setattr(old_value, "drn_RefPartLib35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefPartLib35"):
                opp_val = getattr(value, "drn_RefPartLib35", None)
                setattr(value, "drn_RefPartLib35", self)

class drn_Context:

    def __init__(self, name: str, where: str, drn_Context: "drn_Model" = None, drn_Context19: set["drn_Limit"] = None):
        self.name = name
        self.where = where
        self.drn_Context = drn_Context
        self.drn_Context19 = drn_Context19 if drn_Context19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def where(self) -> str:
        return self.__where

    @where.setter
    def where(self, where: str):
        self.__where = where

    @property
    def drn_Context19(self):
        return self.__drn_Context19

    @drn_Context19.setter
    def drn_Context19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Context__drn_Context19", None)
        self.__drn_Context19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Limit"):
                    opp_val = getattr(item, "drn_Limit", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Limit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Limit"):
                    opp_val = getattr(item, "drn_Limit", None)
                    
                    setattr(item, "drn_Limit", self)
                    

    @property
    def drn_Context(self):
        return self.__drn_Context

    @drn_Context.setter
    def drn_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Context__drn_Context", None)
        self.__drn_Context = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Model4"):
                opp_val = getattr(old_value, "drn_Model4", None)
                if opp_val == self:
                    setattr(old_value, "drn_Model4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Model4"):
                opp_val = getattr(value, "drn_Model4", None)
                setattr(value, "drn_Model4", self)

class Root:

    pass
class drn_Configuration(Root):

    def __init__(self, name: str, drn_Configuration: "drn_Model" = None, drn_Configuration10: set["drn_TypeGeneric"] = None, drn_Configuration12: set["drn_Device"] = None, drn_Configuration14: "drn_ConnectionType" = None):
        self.name = name
        self.drn_Configuration = drn_Configuration
        self.drn_Configuration10 = drn_Configuration10 if drn_Configuration10 is not None else set()
        self.drn_Configuration12 = drn_Configuration12 if drn_Configuration12 is not None else set()
        self.drn_Configuration14 = drn_Configuration14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Configuration10(self):
        return self.__drn_Configuration10

    @drn_Configuration10.setter
    def drn_Configuration10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Configuration__drn_Configuration10", None)
        self.__drn_Configuration10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_TypeGeneric"):
                    opp_val = getattr(item, "drn_TypeGeneric", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_TypeGeneric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_TypeGeneric"):
                    opp_val = getattr(item, "drn_TypeGeneric", None)
                    
                    setattr(item, "drn_TypeGeneric", self)
                    

    @property
    def drn_Configuration(self):
        return self.__drn_Configuration

    @drn_Configuration.setter
    def drn_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Configuration__drn_Configuration", None)
        self.__drn_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Model"):
                opp_val = getattr(old_value, "drn_Model", None)
                if opp_val == self:
                    setattr(old_value, "drn_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Model"):
                opp_val = getattr(value, "drn_Model", None)
                setattr(value, "drn_Model", self)

    @property
    def drn_Configuration14(self):
        return self.__drn_Configuration14

    @drn_Configuration14.setter
    def drn_Configuration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Configuration__drn_Configuration14", None)
        self.__drn_Configuration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_ConnectionType"):
                opp_val = getattr(old_value, "drn_ConnectionType", None)
                if opp_val == self:
                    setattr(old_value, "drn_ConnectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_ConnectionType"):
                opp_val = getattr(value, "drn_ConnectionType", None)
                setattr(value, "drn_ConnectionType", self)

    @property
    def drn_Configuration12(self):
        return self.__drn_Configuration12

    @drn_Configuration12.setter
    def drn_Configuration12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Configuration__drn_Configuration12", None)
        self.__drn_Configuration12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Device"):
                    opp_val = getattr(item, "drn_Device", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Device"):
                    opp_val = getattr(item, "drn_Device", None)
                    
                    setattr(item, "drn_Device", self)
                    

class drn_Library(Root):

    def __init__(self, name: str, drn_Library: "drn_Model" = None, drn_Library16: set["drn_Assignement"] = None, drn_Library33: "drn_RefPartLib" = None):
        self.name = name
        self.drn_Library = drn_Library
        self.drn_Library16 = drn_Library16 if drn_Library16 is not None else set()
        self.drn_Library33 = drn_Library33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Library(self):
        return self.__drn_Library

    @drn_Library.setter
    def drn_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Library__drn_Library", None)
        self.__drn_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Model2"):
                opp_val = getattr(old_value, "drn_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Model2"):
                opp_val = getattr(value, "drn_Model2", None)
                if opp_val is None:
                    setattr(value, "drn_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Library16(self):
        return self.__drn_Library16

    @drn_Library16.setter
    def drn_Library16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Library__drn_Library16", None)
        self.__drn_Library16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Assignement17"):
                    opp_val = getattr(item, "drn_Assignement17", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Assignement17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Assignement17"):
                    opp_val = getattr(item, "drn_Assignement17", None)
                    
                    setattr(item, "drn_Assignement17", self)
                    

    @property
    def drn_Library33(self):
        return self.__drn_Library33

    @drn_Library33.setter
    def drn_Library33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Library__drn_Library33", None)
        self.__drn_Library33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefPartLib"):
                opp_val = getattr(old_value, "drn_RefPartLib", None)
                if opp_val == self:
                    setattr(old_value, "drn_RefPartLib", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefPartLib"):
                opp_val = getattr(value, "drn_RefPartLib", None)
                setattr(value, "drn_RefPartLib", self)

class drn_Model(Root):

    pass
class drn_Root:

    pass
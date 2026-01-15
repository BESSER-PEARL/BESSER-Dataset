from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Mode(Enum):
    OFF = "OFF"
    ON = "ON"
class ColorLed(Enum):
    BLUE = "BLUE"
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    WHITE = "WHITE"
class EBool(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


############################################
# Definition of Classes
############################################

class Option:

    pass
class drn_LedBlink(Option):

    def __init__(self, color: str, blink_per_secCST: str, drn_LedBlink: "drn_Parametre" = None):
        self.color = color
        self.blink_per_secCST = blink_per_secCST
        self.drn_LedBlink = drn_LedBlink
        
    @property
    def blink_per_secCST(self) -> str:
        return self.__blink_per_secCST

    @blink_per_secCST.setter
    def blink_per_secCST(self, blink_per_secCST: str):
        self.__blink_per_secCST = blink_per_secCST

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def drn_LedBlink(self):
        return self.__drn_LedBlink

    @drn_LedBlink.setter
    def drn_LedBlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_LedBlink__drn_LedBlink", None)
        self.__drn_LedBlink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre89"):
                opp_val = getattr(old_value, "drn_Parametre89", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre89"):
                opp_val = getattr(value, "drn_Parametre89", None)
                setattr(value, "drn_Parametre89", self)

class drn_CameraFront(Option):

    def __init__(self, mode: str):
        self.mode = mode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

class drn_CameraBottom(Option):

    def __init__(self, mode: str):
        self.mode = mode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

class drn_Led_Impl(Option):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class drn_Option:

    def __init__(self, name: str, drn_Option: "drn_With" = None):
        self.name = name
        self.drn_Option = drn_Option
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Option(self):
        return self.__drn_Option

    @drn_Option.setter
    def drn_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Option__drn_Option", None)
        self.__drn_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_With87"):
                opp_val = getattr(old_value, "drn_With87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_With87"):
                opp_val = getattr(value, "drn_With87", None)
                if opp_val is None:
                    setattr(value, "drn_With87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DepXZ_IMPL:

    pass
class drn_DepXZ(DepXZ_IMPL):

    def __init__(self, name: str, distanceCST: str, tempsCST: str, drn_DepXZ: "drn_Parametre" = None, drn_DepXZ71: "drn_Parametre" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepXZ = drn_DepXZ
        self.drn_DepXZ71 = drn_DepXZ71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def drn_DepXZ71(self):
        return self.__drn_DepXZ71

    @drn_DepXZ71.setter
    def drn_DepXZ71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXZ__drn_DepXZ71", None)
        self.__drn_DepXZ71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre72"):
                opp_val = getattr(old_value, "drn_Parametre72", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre72"):
                opp_val = getattr(value, "drn_Parametre72", None)
                setattr(value, "drn_Parametre72", self)

    @property
    def drn_DepXZ(self):
        return self.__drn_DepXZ

    @drn_DepXZ.setter
    def drn_DepXZ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXZ__drn_DepXZ", None)
        self.__drn_DepXZ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre69"):
                opp_val = getattr(old_value, "drn_Parametre69", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre69"):
                opp_val = getattr(value, "drn_Parametre69", None)
                setattr(value, "drn_Parametre69", self)

class DepXYZ_IMPL:

    pass
class drn_Flip(DepXYZ_IMPL):

    pass
class drn_DepXYZ(DepXYZ_IMPL):

    def __init__(self, distanceCST: str, tempsCST: str, drn_DepXYZ: "drn_Parametre" = None, drn_DepXYZ76: "drn_Parametre" = None):
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepXYZ = drn_DepXYZ
        self.drn_DepXYZ76 = drn_DepXYZ76
        
    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def drn_DepXYZ(self):
        return self.__drn_DepXYZ

    @drn_DepXYZ.setter
    def drn_DepXYZ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXYZ__drn_DepXYZ", None)
        self.__drn_DepXYZ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre74"):
                opp_val = getattr(old_value, "drn_Parametre74", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre74"):
                opp_val = getattr(value, "drn_Parametre74", None)
                setattr(value, "drn_Parametre74", self)

    @property
    def drn_DepXYZ76(self):
        return self.__drn_DepXYZ76

    @drn_DepXYZ76.setter
    def drn_DepXYZ76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXYZ__drn_DepXYZ76", None)
        self.__drn_DepXYZ76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre77"):
                opp_val = getattr(old_value, "drn_Parametre77", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre77"):
                opp_val = getattr(value, "drn_Parametre77", None)
                setattr(value, "drn_Parametre77", self)

class DepX_Impl:

    pass
class drn_RIGHT(DepX_Impl):

    pass
class drn_LEFT(DepX_Impl):

    pass
class DepYZ_IMPL:

    pass
class drn_CERCLEYZ(DepYZ_IMPL):

    def __init__(self, rayonCST: str, drn_CERCLEYZ: "drn_Parametre" = None):
        self.rayonCST = rayonCST
        self.drn_CERCLEYZ = drn_CERCLEYZ
        
    @property
    def rayonCST(self) -> str:
        return self.__rayonCST

    @rayonCST.setter
    def rayonCST(self, rayonCST: str):
        self.__rayonCST = rayonCST

    @property
    def drn_CERCLEYZ(self):
        return self.__drn_CERCLEYZ

    @drn_CERCLEYZ.setter
    def drn_CERCLEYZ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_CERCLEYZ__drn_CERCLEYZ", None)
        self.__drn_CERCLEYZ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre65"):
                opp_val = getattr(old_value, "drn_Parametre65", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre65"):
                opp_val = getattr(value, "drn_Parametre65", None)
                setattr(value, "drn_Parametre65", self)

class drn_CARREYZ(DepYZ_IMPL):

    def __init__(self, coteCST: str, drn_CARREYZ: "drn_Parametre" = None):
        self.coteCST = coteCST
        self.drn_CARREYZ = drn_CARREYZ
        
    @property
    def coteCST(self) -> str:
        return self.__coteCST

    @coteCST.setter
    def coteCST(self, coteCST: str):
        self.__coteCST = coteCST

    @property
    def drn_CARREYZ(self):
        return self.__drn_CARREYZ

    @drn_CARREYZ.setter
    def drn_CARREYZ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_CARREYZ__drn_CARREYZ", None)
        self.__drn_CARREYZ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre67"):
                opp_val = getattr(old_value, "drn_Parametre67", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre67"):
                opp_val = getattr(value, "drn_Parametre67", None)
                setattr(value, "drn_Parametre67", self)

class drn_DepYZ(DepYZ_IMPL):

    def __init__(self, distanceCST: str, drn_DepYZ: "drn_Parametre" = None):
        self.distanceCST = distanceCST
        self.drn_DepYZ = drn_DepYZ
        
    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def drn_DepYZ(self):
        return self.__drn_DepYZ

    @drn_DepYZ.setter
    def drn_DepYZ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepYZ__drn_DepYZ", None)
        self.__drn_DepYZ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre63"):
                opp_val = getattr(old_value, "drn_Parametre63", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre63"):
                opp_val = getattr(value, "drn_Parametre63", None)
                setattr(value, "drn_Parametre63", self)

class DepXY_IMPL:

    pass
class drn_CERCLEXY(DepXY_IMPL):

    def __init__(self, rayonCST: str, drn_CERCLEXY: "drn_Parametre" = None):
        self.rayonCST = rayonCST
        self.drn_CERCLEXY = drn_CERCLEXY
        
    @property
    def rayonCST(self) -> str:
        return self.__rayonCST

    @rayonCST.setter
    def rayonCST(self, rayonCST: str):
        self.__rayonCST = rayonCST

    @property
    def drn_CERCLEXY(self):
        return self.__drn_CERCLEXY

    @drn_CERCLEXY.setter
    def drn_CERCLEXY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_CERCLEXY__drn_CERCLEXY", None)
        self.__drn_CERCLEXY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre57"):
                opp_val = getattr(old_value, "drn_Parametre57", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre57"):
                opp_val = getattr(value, "drn_Parametre57", None)
                setattr(value, "drn_Parametre57", self)

class drn_CARREXY(DepXY_IMPL):

    def __init__(self, coteCST: str, drn_CARREXY: "drn_Parametre" = None):
        self.coteCST = coteCST
        self.drn_CARREXY = drn_CARREXY
        
    @property
    def coteCST(self) -> str:
        return self.__coteCST

    @coteCST.setter
    def coteCST(self, coteCST: str):
        self.__coteCST = coteCST

    @property
    def drn_CARREXY(self):
        return self.__drn_CARREXY

    @drn_CARREXY.setter
    def drn_CARREXY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_CARREXY__drn_CARREXY", None)
        self.__drn_CARREXY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre59"):
                opp_val = getattr(old_value, "drn_Parametre59", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre59"):
                opp_val = getattr(value, "drn_Parametre59", None)
                setattr(value, "drn_Parametre59", self)

class drn_DepXY(DepXY_IMPL):

    def __init__(self, distanceCST: str, drn_DepXY: "drn_Parametre" = None):
        self.distanceCST = distanceCST
        self.drn_DepXY = drn_DepXY
        
    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def drn_DepXY(self):
        return self.__drn_DepXY

    @drn_DepXY.setter
    def drn_DepXY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXY__drn_DepXY", None)
        self.__drn_DepXY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre55"):
                opp_val = getattr(old_value, "drn_Parametre55", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre55"):
                opp_val = getattr(value, "drn_Parametre55", None)
                setattr(value, "drn_Parametre55", self)

class DepZ_Impl:

    pass
class drn_UP(DepZ_Impl):

    pass
class drn_DOWN(DepZ_Impl):

    pass
class Expression:

    pass
class drn_Land(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_DepYZ_IMPL(Expression):

    def __init__(self, name: str, tempsCST: str, drn_DepYZ_IMPL: "drn_Parametre" = None):
        self.name = name
        self.tempsCST = tempsCST
        self.drn_DepYZ_IMPL = drn_DepYZ_IMPL
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def drn_DepYZ_IMPL(self):
        return self.__drn_DepYZ_IMPL

    @drn_DepYZ_IMPL.setter
    def drn_DepYZ_IMPL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepYZ_IMPL__drn_DepYZ_IMPL", None)
        self.__drn_DepYZ_IMPL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre61"):
                opp_val = getattr(old_value, "drn_Parametre61", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre61"):
                opp_val = getattr(value, "drn_Parametre61", None)
                setattr(value, "drn_Parametre61", self)

class drn_TakeOff(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_Rotate(Expression):

    def __init__(self, name: str, angleCST: str, tempsCST: str, drn_Rotate: "drn_And" = None, drn_Rotate79: "drn_Parametre" = None, drn_Rotate82: "drn_Parametre" = None):
        self.name = name
        self.angleCST = angleCST
        self.tempsCST = tempsCST
        self.drn_Rotate = drn_Rotate
        self.drn_Rotate79 = drn_Rotate79
        self.drn_Rotate82 = drn_Rotate82
        
    @property
    def angleCST(self) -> str:
        return self.__angleCST

    @angleCST.setter
    def angleCST(self, angleCST: str):
        self.__angleCST = angleCST

    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Rotate79(self):
        return self.__drn_Rotate79

    @drn_Rotate79.setter
    def drn_Rotate79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Rotate__drn_Rotate79", None)
        self.__drn_Rotate79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre80"):
                opp_val = getattr(old_value, "drn_Parametre80", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre80"):
                opp_val = getattr(value, "drn_Parametre80", None)
                setattr(value, "drn_Parametre80", self)

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

    @property
    def drn_Rotate82(self):
        return self.__drn_Rotate82

    @drn_Rotate82.setter
    def drn_Rotate82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Rotate__drn_Rotate82", None)
        self.__drn_Rotate82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre83"):
                opp_val = getattr(old_value, "drn_Parametre83", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre83"):
                opp_val = getattr(value, "drn_Parametre83", None)
                setattr(value, "drn_Parametre83", self)

class drn_And(Expression):

    def __init__(self, name: str, drn_And24: set["drn_DepX_Impl"] = None, drn_And26: set["drn_DepY_Impl"] = None, drn_And28: set["drn_DepXZ_IMPL"] = None, drn_And30: set["drn_DepXY_IMPL"] = None, drn_And32: set["drn_DepZ_Impl"] = None, drn_And: set["drn_Rotate"] = None):
        self.name = name
        self.drn_And24 = drn_And24 if drn_And24 is not None else set()
        self.drn_And26 = drn_And26 if drn_And26 is not None else set()
        self.drn_And28 = drn_And28 if drn_And28 is not None else set()
        self.drn_And30 = drn_And30 if drn_And30 is not None else set()
        self.drn_And32 = drn_And32 if drn_And32 is not None else set()
        self.drn_And = drn_And if drn_And is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_And28(self):
        return self.__drn_And28

    @drn_And28.setter
    def drn_And28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And28", None)
        self.__drn_And28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_DepXZ_IMPL"):
                    opp_val = getattr(item, "drn_DepXZ_IMPL", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_DepXZ_IMPL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_DepXZ_IMPL"):
                    opp_val = getattr(item, "drn_DepXZ_IMPL", None)
                    
                    setattr(item, "drn_DepXZ_IMPL", self)
                    

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
    def drn_And30(self):
        return self.__drn_And30

    @drn_And30.setter
    def drn_And30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And30", None)
        self.__drn_And30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_DepXY_IMPL"):
                    opp_val = getattr(item, "drn_DepXY_IMPL", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_DepXY_IMPL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_DepXY_IMPL"):
                    opp_val = getattr(item, "drn_DepXY_IMPL", None)
                    
                    setattr(item, "drn_DepXY_IMPL", self)
                    

    @property
    def drn_And32(self):
        return self.__drn_And32

    @drn_And32.setter
    def drn_And32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And32", None)
        self.__drn_And32 = value if value is not None else set()
        
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
    def drn_And24(self):
        return self.__drn_And24

    @drn_And24.setter
    def drn_And24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And24", None)
        self.__drn_And24 = value if value is not None else set()
        
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
                    

    @property
    def drn_And26(self):
        return self.__drn_And26

    @drn_And26.setter
    def drn_And26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_And__drn_And26", None)
        self.__drn_And26 = value if value is not None else set()
        
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
                    

class drn_Wait(Expression):

    def __init__(self, name: str, tempsCST: str, drn_Wait: "drn_Parametre" = None):
        self.name = name
        self.tempsCST = tempsCST
        self.drn_Wait = drn_Wait
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def drn_Wait(self):
        return self.__drn_Wait

    @drn_Wait.setter
    def drn_Wait(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Wait__drn_Wait", None)
        self.__drn_Wait = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre85"):
                opp_val = getattr(old_value, "drn_Parametre85", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre85"):
                opp_val = getattr(value, "drn_Parametre85", None)
                setattr(value, "drn_Parametre85", self)

class drn_DepXYZ_IMPL(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drn_With:

    def __init__(self, name: str, drn_With: "drn_Expression" = None, drn_With87: set["drn_Option"] = None):
        self.name = name
        self.drn_With = drn_With
        self.drn_With87 = drn_With87 if drn_With87 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "drn_Expression15"):
                opp_val = getattr(old_value, "drn_Expression15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Expression15"):
                opp_val = getattr(value, "drn_Expression15", None)
                if opp_val is None:
                    setattr(value, "drn_Expression15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_With87(self):
        return self.__drn_With87

    @drn_With87.setter
    def drn_With87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_With__drn_With87", None)
        self.__drn_With87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Option"):
                    opp_val = getattr(item, "drn_Option", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Option"):
                    opp_val = getattr(item, "drn_Option", None)
                    
                    setattr(item, "drn_Option", self)
                    

class DepY_Impl:

    pass
class drn_BACKWARD(DepY_Impl):

    pass
class drn_FORWARD(DepY_Impl):

    pass
class drn_DepZ_Impl(Expression):

    def __init__(self, name: str, distanceCST: str, tempsCST: str, drn_DepZ_Impl: "drn_And" = None, drn_DepZ_Impl46: "drn_Parametre" = None, drn_DepZ_Impl49: "drn_Parametre" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepZ_Impl = drn_DepZ_Impl
        self.drn_DepZ_Impl46 = drn_DepZ_Impl46
        self.drn_DepZ_Impl49 = drn_DepZ_Impl49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def drn_DepZ_Impl49(self):
        return self.__drn_DepZ_Impl49

    @drn_DepZ_Impl49.setter
    def drn_DepZ_Impl49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepZ_Impl__drn_DepZ_Impl49", None)
        self.__drn_DepZ_Impl49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre50"):
                opp_val = getattr(old_value, "drn_Parametre50", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre50"):
                opp_val = getattr(value, "drn_Parametre50", None)
                setattr(value, "drn_Parametre50", self)

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
            if hasattr(old_value, "drn_And32"):
                opp_val = getattr(old_value, "drn_And32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And32"):
                opp_val = getattr(value, "drn_And32", None)
                if opp_val is None:
                    setattr(value, "drn_And32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_DepZ_Impl46(self):
        return self.__drn_DepZ_Impl46

    @drn_DepZ_Impl46.setter
    def drn_DepZ_Impl46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepZ_Impl__drn_DepZ_Impl46", None)
        self.__drn_DepZ_Impl46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre47"):
                opp_val = getattr(old_value, "drn_Parametre47", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre47"):
                opp_val = getattr(value, "drn_Parametre47", None)
                setattr(value, "drn_Parametre47", self)

class drn_DepXY_IMPL(Expression):

    def __init__(self, name: str, tempsCST: str, drn_DepXY_IMPL: "drn_And" = None, drn_DepXY_IMPL52: "drn_Parametre" = None):
        self.name = name
        self.tempsCST = tempsCST
        self.drn_DepXY_IMPL = drn_DepXY_IMPL
        self.drn_DepXY_IMPL52 = drn_DepXY_IMPL52
        
    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_DepXY_IMPL(self):
        return self.__drn_DepXY_IMPL

    @drn_DepXY_IMPL.setter
    def drn_DepXY_IMPL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXY_IMPL__drn_DepXY_IMPL", None)
        self.__drn_DepXY_IMPL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_And30"):
                opp_val = getattr(old_value, "drn_And30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And30"):
                opp_val = getattr(value, "drn_And30", None)
                if opp_val is None:
                    setattr(value, "drn_And30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_DepXY_IMPL52(self):
        return self.__drn_DepXY_IMPL52

    @drn_DepXY_IMPL52.setter
    def drn_DepXY_IMPL52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepXY_IMPL__drn_DepXY_IMPL52", None)
        self.__drn_DepXY_IMPL52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre53"):
                opp_val = getattr(old_value, "drn_Parametre53", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre53"):
                opp_val = getattr(value, "drn_Parametre53", None)
                setattr(value, "drn_Parametre53", self)

class drn_DepXZ_IMPL(Expression):

    pass
class drn_DepY_Impl(Expression):

    def __init__(self, name: str, distanceCST: str, tempsCST: str, drn_DepY_Impl: "drn_And" = None, drn_DepY_Impl34: "drn_Parametre" = None, drn_DepY_Impl37: "drn_Parametre" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepY_Impl = drn_DepY_Impl
        self.drn_DepY_Impl34 = drn_DepY_Impl34
        self.drn_DepY_Impl37 = drn_DepY_Impl37
        
    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def drn_DepY_Impl34(self):
        return self.__drn_DepY_Impl34

    @drn_DepY_Impl34.setter
    def drn_DepY_Impl34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepY_Impl__drn_DepY_Impl34", None)
        self.__drn_DepY_Impl34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre35"):
                opp_val = getattr(old_value, "drn_Parametre35", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre35"):
                opp_val = getattr(value, "drn_Parametre35", None)
                setattr(value, "drn_Parametre35", self)

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
            if hasattr(old_value, "drn_And26"):
                opp_val = getattr(old_value, "drn_And26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And26"):
                opp_val = getattr(value, "drn_And26", None)
                if opp_val is None:
                    setattr(value, "drn_And26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_DepY_Impl37(self):
        return self.__drn_DepY_Impl37

    @drn_DepY_Impl37.setter
    def drn_DepY_Impl37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepY_Impl__drn_DepY_Impl37", None)
        self.__drn_DepY_Impl37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre38"):
                opp_val = getattr(old_value, "drn_Parametre38", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre38"):
                opp_val = getattr(value, "drn_Parametre38", None)
                setattr(value, "drn_Parametre38", self)

class drn_DepX_Impl(Expression):

    def __init__(self, name: str, distanceCST: str, tempsCST: str, drn_DepX_Impl: "drn_And" = None, drn_DepX_Impl40: "drn_Parametre" = None, drn_DepX_Impl43: "drn_Parametre" = None):
        self.name = name
        self.distanceCST = distanceCST
        self.tempsCST = tempsCST
        self.drn_DepX_Impl = drn_DepX_Impl
        self.drn_DepX_Impl40 = drn_DepX_Impl40
        self.drn_DepX_Impl43 = drn_DepX_Impl43
        
    @property
    def tempsCST(self) -> str:
        return self.__tempsCST

    @tempsCST.setter
    def tempsCST(self, tempsCST: str):
        self.__tempsCST = tempsCST

    @property
    def distanceCST(self) -> str:
        return self.__distanceCST

    @distanceCST.setter
    def distanceCST(self, distanceCST: str):
        self.__distanceCST = distanceCST

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "drn_And24"):
                opp_val = getattr(old_value, "drn_And24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_And24"):
                opp_val = getattr(value, "drn_And24", None)
                if opp_val is None:
                    setattr(value, "drn_And24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_DepX_Impl40(self):
        return self.__drn_DepX_Impl40

    @drn_DepX_Impl40.setter
    def drn_DepX_Impl40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepX_Impl__drn_DepX_Impl40", None)
        self.__drn_DepX_Impl40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre41"):
                opp_val = getattr(old_value, "drn_Parametre41", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre41"):
                opp_val = getattr(value, "drn_Parametre41", None)
                setattr(value, "drn_Parametre41", self)

    @property
    def drn_DepX_Impl43(self):
        return self.__drn_DepX_Impl43

    @drn_DepX_Impl43.setter
    def drn_DepX_Impl43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_DepX_Impl__drn_DepX_Impl43", None)
        self.__drn_DepX_Impl43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre44"):
                opp_val = getattr(old_value, "drn_Parametre44", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre44"):
                opp_val = getattr(value, "drn_Parametre44", None)
                setattr(value, "drn_Parametre44", self)

class drn_Context:

    pass
class drn_Model:

    pass
class drn_Expression:

    def __init__(self, repeatCST: str, drn_Expression: "drn_Assignement" = None, drn_Expression12: "drn_Parametre" = None, drn_Expression15: set["drn_With"] = None, drn_Expression18: "drn_Expression" = None, drn_Expression16: set["drn_Expression"] = None):
        self.repeatCST = repeatCST
        self.drn_Expression = drn_Expression
        self.drn_Expression12 = drn_Expression12
        self.drn_Expression15 = drn_Expression15 if drn_Expression15 is not None else set()
        self.drn_Expression18 = drn_Expression18
        self.drn_Expression16 = drn_Expression16 if drn_Expression16 is not None else set()
        
    @property
    def repeatCST(self) -> str:
        return self.__repeatCST

    @repeatCST.setter
    def repeatCST(self, repeatCST: str):
        self.__repeatCST = repeatCST

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
            if hasattr(old_value, "drn_Assignement10"):
                opp_val = getattr(old_value, "drn_Assignement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Assignement10"):
                opp_val = getattr(value, "drn_Assignement10", None)
                if opp_val is None:
                    setattr(value, "drn_Assignement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Expression12(self):
        return self.__drn_Expression12

    @drn_Expression12.setter
    def drn_Expression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression12", None)
        self.__drn_Expression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Parametre13"):
                opp_val = getattr(old_value, "drn_Parametre13", None)
                if opp_val == self:
                    setattr(old_value, "drn_Parametre13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Parametre13"):
                opp_val = getattr(value, "drn_Parametre13", None)
                setattr(value, "drn_Parametre13", self)

    @property
    def drn_Expression15(self):
        return self.__drn_Expression15

    @drn_Expression15.setter
    def drn_Expression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression15", None)
        self.__drn_Expression15 = value if value is not None else set()
        
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
    def drn_Expression16(self):
        return self.__drn_Expression16

    @drn_Expression16.setter
    def drn_Expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression16", None)
        self.__drn_Expression16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Expression18"):
                    opp_val = getattr(item, "drn_Expression18", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Expression18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Expression18"):
                    opp_val = getattr(item, "drn_Expression18", None)
                    
                    setattr(item, "drn_Expression18", self)
                    

    @property
    def drn_Expression18(self):
        return self.__drn_Expression18

    @drn_Expression18.setter
    def drn_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Expression__drn_Expression18", None)
        self.__drn_Expression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Expression16"):
                opp_val = getattr(old_value, "drn_Expression16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Expression16"):
                opp_val = getattr(value, "drn_Expression16", None)
                if opp_val is None:
                    setattr(value, "drn_Expression16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_Parametre:

    def __init__(self, name: str, drn_Parametre: "drn_Assignement" = None, drn_Parametre13: "drn_Expression" = None, drn_Parametre35: "drn_DepY_Impl" = None, drn_Parametre38: "drn_DepY_Impl" = None, drn_Parametre41: "drn_DepX_Impl" = None, drn_Parametre53: "drn_DepXY_IMPL" = None, drn_Parametre55: "drn_DepXY" = None, drn_Parametre57: "drn_CERCLEXY" = None, drn_Parametre59: "drn_CARREXY" = None, drn_Parametre61: "drn_DepYZ_IMPL" = None, drn_Parametre44: "drn_DepX_Impl" = None, drn_Parametre47: "drn_DepZ_Impl" = None, drn_Parametre50: "drn_DepZ_Impl" = None, drn_Parametre69: "drn_DepXZ" = None, drn_Parametre72: "drn_DepXZ" = None, drn_Parametre74: "drn_DepXYZ" = None, drn_Parametre77: "drn_DepXYZ" = None, drn_Parametre80: "drn_Rotate" = None, drn_Parametre63: "drn_DepYZ" = None, drn_Parametre65: "drn_CERCLEYZ" = None, drn_Parametre67: "drn_CARREYZ" = None, drn_Parametre89: "drn_LedBlink" = None, drn_Parametre83: "drn_Rotate" = None, drn_Parametre85: "drn_Wait" = None):
        self.name = name
        self.drn_Parametre = drn_Parametre
        self.drn_Parametre13 = drn_Parametre13
        self.drn_Parametre35 = drn_Parametre35
        self.drn_Parametre38 = drn_Parametre38
        self.drn_Parametre41 = drn_Parametre41
        self.drn_Parametre53 = drn_Parametre53
        self.drn_Parametre55 = drn_Parametre55
        self.drn_Parametre57 = drn_Parametre57
        self.drn_Parametre59 = drn_Parametre59
        self.drn_Parametre61 = drn_Parametre61
        self.drn_Parametre44 = drn_Parametre44
        self.drn_Parametre47 = drn_Parametre47
        self.drn_Parametre50 = drn_Parametre50
        self.drn_Parametre69 = drn_Parametre69
        self.drn_Parametre72 = drn_Parametre72
        self.drn_Parametre74 = drn_Parametre74
        self.drn_Parametre77 = drn_Parametre77
        self.drn_Parametre80 = drn_Parametre80
        self.drn_Parametre63 = drn_Parametre63
        self.drn_Parametre65 = drn_Parametre65
        self.drn_Parametre67 = drn_Parametre67
        self.drn_Parametre89 = drn_Parametre89
        self.drn_Parametre83 = drn_Parametre83
        self.drn_Parametre85 = drn_Parametre85
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Parametre77(self):
        return self.__drn_Parametre77

    @drn_Parametre77.setter
    def drn_Parametre77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre77", None)
        self.__drn_Parametre77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXYZ76"):
                opp_val = getattr(old_value, "drn_DepXYZ76", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXYZ76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXYZ76"):
                opp_val = getattr(value, "drn_DepXYZ76", None)
                setattr(value, "drn_DepXYZ76", self)

    @property
    def drn_Parametre53(self):
        return self.__drn_Parametre53

    @drn_Parametre53.setter
    def drn_Parametre53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre53", None)
        self.__drn_Parametre53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXY_IMPL52"):
                opp_val = getattr(old_value, "drn_DepXY_IMPL52", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXY_IMPL52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXY_IMPL52"):
                opp_val = getattr(value, "drn_DepXY_IMPL52", None)
                setattr(value, "drn_DepXY_IMPL52", self)

    @property
    def drn_Parametre83(self):
        return self.__drn_Parametre83

    @drn_Parametre83.setter
    def drn_Parametre83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre83", None)
        self.__drn_Parametre83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Rotate82"):
                opp_val = getattr(old_value, "drn_Rotate82", None)
                if opp_val == self:
                    setattr(old_value, "drn_Rotate82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Rotate82"):
                opp_val = getattr(value, "drn_Rotate82", None)
                setattr(value, "drn_Rotate82", self)

    @property
    def drn_Parametre41(self):
        return self.__drn_Parametre41

    @drn_Parametre41.setter
    def drn_Parametre41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre41", None)
        self.__drn_Parametre41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepX_Impl40"):
                opp_val = getattr(old_value, "drn_DepX_Impl40", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepX_Impl40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepX_Impl40"):
                opp_val = getattr(value, "drn_DepX_Impl40", None)
                setattr(value, "drn_DepX_Impl40", self)

    @property
    def drn_Parametre57(self):
        return self.__drn_Parametre57

    @drn_Parametre57.setter
    def drn_Parametre57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre57", None)
        self.__drn_Parametre57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_CERCLEXY"):
                opp_val = getattr(old_value, "drn_CERCLEXY", None)
                if opp_val == self:
                    setattr(old_value, "drn_CERCLEXY", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_CERCLEXY"):
                opp_val = getattr(value, "drn_CERCLEXY", None)
                setattr(value, "drn_CERCLEXY", self)

    @property
    def drn_Parametre67(self):
        return self.__drn_Parametre67

    @drn_Parametre67.setter
    def drn_Parametre67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre67", None)
        self.__drn_Parametre67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_CARREYZ"):
                opp_val = getattr(old_value, "drn_CARREYZ", None)
                if opp_val == self:
                    setattr(old_value, "drn_CARREYZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_CARREYZ"):
                opp_val = getattr(value, "drn_CARREYZ", None)
                setattr(value, "drn_CARREYZ", self)

    @property
    def drn_Parametre35(self):
        return self.__drn_Parametre35

    @drn_Parametre35.setter
    def drn_Parametre35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre35", None)
        self.__drn_Parametre35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepY_Impl34"):
                opp_val = getattr(old_value, "drn_DepY_Impl34", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepY_Impl34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepY_Impl34"):
                opp_val = getattr(value, "drn_DepY_Impl34", None)
                setattr(value, "drn_DepY_Impl34", self)

    @property
    def drn_Parametre65(self):
        return self.__drn_Parametre65

    @drn_Parametre65.setter
    def drn_Parametre65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre65", None)
        self.__drn_Parametre65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_CERCLEYZ"):
                opp_val = getattr(old_value, "drn_CERCLEYZ", None)
                if opp_val == self:
                    setattr(old_value, "drn_CERCLEYZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_CERCLEYZ"):
                opp_val = getattr(value, "drn_CERCLEYZ", None)
                setattr(value, "drn_CERCLEYZ", self)

    @property
    def drn_Parametre50(self):
        return self.__drn_Parametre50

    @drn_Parametre50.setter
    def drn_Parametre50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre50", None)
        self.__drn_Parametre50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepZ_Impl49"):
                opp_val = getattr(old_value, "drn_DepZ_Impl49", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepZ_Impl49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepZ_Impl49"):
                opp_val = getattr(value, "drn_DepZ_Impl49", None)
                setattr(value, "drn_DepZ_Impl49", self)

    @property
    def drn_Parametre47(self):
        return self.__drn_Parametre47

    @drn_Parametre47.setter
    def drn_Parametre47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre47", None)
        self.__drn_Parametre47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepZ_Impl46"):
                opp_val = getattr(old_value, "drn_DepZ_Impl46", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepZ_Impl46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepZ_Impl46"):
                opp_val = getattr(value, "drn_DepZ_Impl46", None)
                setattr(value, "drn_DepZ_Impl46", self)

    @property
    def drn_Parametre44(self):
        return self.__drn_Parametre44

    @drn_Parametre44.setter
    def drn_Parametre44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre44", None)
        self.__drn_Parametre44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepX_Impl43"):
                opp_val = getattr(old_value, "drn_DepX_Impl43", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepX_Impl43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepX_Impl43"):
                opp_val = getattr(value, "drn_DepX_Impl43", None)
                setattr(value, "drn_DepX_Impl43", self)

    @property
    def drn_Parametre(self):
        return self.__drn_Parametre

    @drn_Parametre.setter
    def drn_Parametre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre", None)
        self.__drn_Parametre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Assignement8"):
                opp_val = getattr(old_value, "drn_Assignement8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Assignement8"):
                opp_val = getattr(value, "drn_Assignement8", None)
                if opp_val is None:
                    setattr(value, "drn_Assignement8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drn_Parametre72(self):
        return self.__drn_Parametre72

    @drn_Parametre72.setter
    def drn_Parametre72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre72", None)
        self.__drn_Parametre72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXZ71"):
                opp_val = getattr(old_value, "drn_DepXZ71", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXZ71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXZ71"):
                opp_val = getattr(value, "drn_DepXZ71", None)
                setattr(value, "drn_DepXZ71", self)

    @property
    def drn_Parametre38(self):
        return self.__drn_Parametre38

    @drn_Parametre38.setter
    def drn_Parametre38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre38", None)
        self.__drn_Parametre38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepY_Impl37"):
                opp_val = getattr(old_value, "drn_DepY_Impl37", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepY_Impl37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepY_Impl37"):
                opp_val = getattr(value, "drn_DepY_Impl37", None)
                setattr(value, "drn_DepY_Impl37", self)

    @property
    def drn_Parametre63(self):
        return self.__drn_Parametre63

    @drn_Parametre63.setter
    def drn_Parametre63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre63", None)
        self.__drn_Parametre63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepYZ"):
                opp_val = getattr(old_value, "drn_DepYZ", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepYZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepYZ"):
                opp_val = getattr(value, "drn_DepYZ", None)
                setattr(value, "drn_DepYZ", self)

    @property
    def drn_Parametre85(self):
        return self.__drn_Parametre85

    @drn_Parametre85.setter
    def drn_Parametre85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre85", None)
        self.__drn_Parametre85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Wait"):
                opp_val = getattr(old_value, "drn_Wait", None)
                if opp_val == self:
                    setattr(old_value, "drn_Wait", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Wait"):
                opp_val = getattr(value, "drn_Wait", None)
                setattr(value, "drn_Wait", self)

    @property
    def drn_Parametre61(self):
        return self.__drn_Parametre61

    @drn_Parametre61.setter
    def drn_Parametre61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre61", None)
        self.__drn_Parametre61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepYZ_IMPL"):
                opp_val = getattr(old_value, "drn_DepYZ_IMPL", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepYZ_IMPL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepYZ_IMPL"):
                opp_val = getattr(value, "drn_DepYZ_IMPL", None)
                setattr(value, "drn_DepYZ_IMPL", self)

    @property
    def drn_Parametre55(self):
        return self.__drn_Parametre55

    @drn_Parametre55.setter
    def drn_Parametre55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre55", None)
        self.__drn_Parametre55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXY"):
                opp_val = getattr(old_value, "drn_DepXY", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXY", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXY"):
                opp_val = getattr(value, "drn_DepXY", None)
                setattr(value, "drn_DepXY", self)

    @property
    def drn_Parametre59(self):
        return self.__drn_Parametre59

    @drn_Parametre59.setter
    def drn_Parametre59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre59", None)
        self.__drn_Parametre59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_CARREXY"):
                opp_val = getattr(old_value, "drn_CARREXY", None)
                if opp_val == self:
                    setattr(old_value, "drn_CARREXY", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_CARREXY"):
                opp_val = getattr(value, "drn_CARREXY", None)
                setattr(value, "drn_CARREXY", self)

    @property
    def drn_Parametre13(self):
        return self.__drn_Parametre13

    @drn_Parametre13.setter
    def drn_Parametre13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre13", None)
        self.__drn_Parametre13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Expression12"):
                opp_val = getattr(old_value, "drn_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "drn_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Expression12"):
                opp_val = getattr(value, "drn_Expression12", None)
                setattr(value, "drn_Expression12", self)

    @property
    def drn_Parametre74(self):
        return self.__drn_Parametre74

    @drn_Parametre74.setter
    def drn_Parametre74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre74", None)
        self.__drn_Parametre74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXYZ"):
                opp_val = getattr(old_value, "drn_DepXYZ", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXYZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXYZ"):
                opp_val = getattr(value, "drn_DepXYZ", None)
                setattr(value, "drn_DepXYZ", self)

    @property
    def drn_Parametre89(self):
        return self.__drn_Parametre89

    @drn_Parametre89.setter
    def drn_Parametre89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre89", None)
        self.__drn_Parametre89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_LedBlink"):
                opp_val = getattr(old_value, "drn_LedBlink", None)
                if opp_val == self:
                    setattr(old_value, "drn_LedBlink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_LedBlink"):
                opp_val = getattr(value, "drn_LedBlink", None)
                setattr(value, "drn_LedBlink", self)

    @property
    def drn_Parametre69(self):
        return self.__drn_Parametre69

    @drn_Parametre69.setter
    def drn_Parametre69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre69", None)
        self.__drn_Parametre69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_DepXZ"):
                opp_val = getattr(old_value, "drn_DepXZ", None)
                if opp_val == self:
                    setattr(old_value, "drn_DepXZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_DepXZ"):
                opp_val = getattr(value, "drn_DepXZ", None)
                setattr(value, "drn_DepXZ", self)

    @property
    def drn_Parametre80(self):
        return self.__drn_Parametre80

    @drn_Parametre80.setter
    def drn_Parametre80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Parametre__drn_Parametre80", None)
        self.__drn_Parametre80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Rotate79"):
                opp_val = getattr(old_value, "drn_Rotate79", None)
                if opp_val == self:
                    setattr(old_value, "drn_Rotate79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Rotate79"):
                opp_val = getattr(value, "drn_Rotate79", None)
                setattr(value, "drn_Rotate79", self)

class Limit:

    pass
class drn_Hmax(Limit):

    pass
class drn_Vmax(Limit):

    pass
class drn_Limit:

    def __init__(self, name: str, value: str, drn_Limit: "drn_Context" = None):
        self.name = name
        self.value = value
        self.drn_Limit = drn_Limit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "drn_Context6"):
                opp_val = getattr(old_value, "drn_Context6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Context6"):
                opp_val = getattr(value, "drn_Context6", None)
                if opp_val is None:
                    setattr(value, "drn_Context6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drn_RefPart(Expression):

    def __init__(self, params: str, drn_RefPart: "drn_Model" = None, drn_RefPart20: "drn_Assignement" = None):
        self.params = params
        self.drn_RefPart = drn_RefPart
        self.drn_RefPart20 = drn_RefPart20
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def drn_RefPart(self):
        return self.__drn_RefPart

    @drn_RefPart.setter
    def drn_RefPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_RefPart__drn_RefPart", None)
        self.__drn_RefPart = value
        
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

    @property
    def drn_RefPart20(self):
        return self.__drn_RefPart20

    @drn_RefPart20.setter
    def drn_RefPart20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_RefPart__drn_RefPart20", None)
        self.__drn_RefPart20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_Assignement21"):
                opp_val = getattr(old_value, "drn_Assignement21", None)
                if opp_val == self:
                    setattr(old_value, "drn_Assignement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_Assignement21"):
                opp_val = getattr(value, "drn_Assignement21", None)
                setattr(value, "drn_Assignement21", self)

class drn_Assignement:

    def __init__(self, name: str, drn_Assignement: "drn_Model" = None, drn_Assignement8: set["drn_Parametre"] = None, drn_Assignement10: set["drn_Expression"] = None, drn_Assignement21: "drn_RefPart" = None):
        self.name = name
        self.drn_Assignement = drn_Assignement
        self.drn_Assignement8 = drn_Assignement8 if drn_Assignement8 is not None else set()
        self.drn_Assignement10 = drn_Assignement10 if drn_Assignement10 is not None else set()
        self.drn_Assignement21 = drn_Assignement21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def drn_Assignement10(self):
        return self.__drn_Assignement10

    @drn_Assignement10.setter
    def drn_Assignement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement10", None)
        self.__drn_Assignement10 = value if value is not None else set()
        
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
    def drn_Assignement(self):
        return self.__drn_Assignement

    @drn_Assignement.setter
    def drn_Assignement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement", None)
        self.__drn_Assignement = value
        
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
    def drn_Assignement21(self):
        return self.__drn_Assignement21

    @drn_Assignement21.setter
    def drn_Assignement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement21", None)
        self.__drn_Assignement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drn_RefPart20"):
                opp_val = getattr(old_value, "drn_RefPart20", None)
                if opp_val == self:
                    setattr(old_value, "drn_RefPart20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drn_RefPart20"):
                opp_val = getattr(value, "drn_RefPart20", None)
                setattr(value, "drn_RefPart20", self)

    @property
    def drn_Assignement8(self):
        return self.__drn_Assignement8

    @drn_Assignement8.setter
    def drn_Assignement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drn_Assignement__drn_Assignement8", None)
        self.__drn_Assignement8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drn_Parametre"):
                    opp_val = getattr(item, "drn_Parametre", None)
                    
                    if opp_val == self:
                        setattr(item, "drn_Parametre", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drn_Parametre"):
                    opp_val = getattr(item, "drn_Parametre", None)
                    
                    setattr(item, "drn_Parametre", self)
                    

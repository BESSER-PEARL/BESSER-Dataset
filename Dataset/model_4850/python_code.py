from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    Red = "Red"
    Black = "Black"
    White = "White"
    Grey = "Grey"
    Green = "Green"


############################################
# Definition of Classes
############################################

class aml_Feature:

    def __init__(self, name: str, value: str, aml_Feature25: "aml_Entity" = None, aml_Feature: "aml_PriceRule" = None):
        self.name = name
        self.value = value
        self.aml_Feature25 = aml_Feature25
        self.aml_Feature = aml_Feature
        
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
    def aml_Feature25(self):
        return self.__aml_Feature25

    @aml_Feature25.setter
    def aml_Feature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Feature__aml_Feature25", None)
        self.__aml_Feature25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Entity24"):
                opp_val = getattr(old_value, "aml_Entity24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Entity24"):
                opp_val = getattr(value, "aml_Entity24", None)
                if opp_val is None:
                    setattr(value, "aml_Entity24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aml_Feature(self):
        return self.__aml_Feature

    @aml_Feature.setter
    def aml_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_Feature__aml_Feature", None)
        self.__aml_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_PriceRule21"):
                opp_val = getattr(old_value, "aml_PriceRule21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_PriceRule21"):
                opp_val = getattr(value, "aml_PriceRule21", None)
                if opp_val is None:
                    setattr(value, "aml_PriceRule21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_LengthFeature:

    def __init__(self, name: str, value: float, aml_LengthFeature: "aml_Cable" = None):
        self.name = name
        self.value = value
        self.aml_LengthFeature = aml_LengthFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def aml_LengthFeature(self):
        return self.__aml_LengthFeature

    @aml_LengthFeature.setter
    def aml_LengthFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_LengthFeature__aml_LengthFeature", None)
        self.__aml_LengthFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Cable17"):
                opp_val = getattr(old_value, "aml_Cable17", None)
                if opp_val == self:
                    setattr(old_value, "aml_Cable17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Cable17"):
                opp_val = getattr(value, "aml_Cable17", None)
                setattr(value, "aml_Cable17", self)

class aml_SpeedFeature:

    def __init__(self, name: str, value: float, aml_SpeedFeature: "aml_Drive" = None):
        self.name = name
        self.value = value
        self.aml_SpeedFeature = aml_SpeedFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def aml_SpeedFeature(self):
        return self.__aml_SpeedFeature

    @aml_SpeedFeature.setter
    def aml_SpeedFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_SpeedFeature__aml_SpeedFeature", None)
        self.__aml_SpeedFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Drive10"):
                opp_val = getattr(old_value, "aml_Drive10", None)
                if opp_val == self:
                    setattr(old_value, "aml_Drive10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Drive10"):
                opp_val = getattr(value, "aml_Drive10", None)
                setattr(value, "aml_Drive10", self)

class aml_SizeFeature:

    def __init__(self, name: str, value: int, aml_SizeFeature: "aml_Drive" = None):
        self.name = name
        self.value = value
        self.aml_SizeFeature = aml_SizeFeature
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aml_SizeFeature(self):
        return self.__aml_SizeFeature

    @aml_SizeFeature.setter
    def aml_SizeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_SizeFeature__aml_SizeFeature", None)
        self.__aml_SizeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Drive8"):
                opp_val = getattr(old_value, "aml_Drive8", None)
                if opp_val == self:
                    setattr(old_value, "aml_Drive8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Drive8"):
                opp_val = getattr(value, "aml_Drive8", None)
                setattr(value, "aml_Drive8", self)

class aml_TypeFeature:

    def __init__(self, name: str, value: str, aml_TypeFeature: "aml_Drive" = None):
        self.name = name
        self.value = value
        self.aml_TypeFeature = aml_TypeFeature
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aml_TypeFeature(self):
        return self.__aml_TypeFeature

    @aml_TypeFeature.setter
    def aml_TypeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_TypeFeature__aml_TypeFeature", None)
        self.__aml_TypeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Drive"):
                opp_val = getattr(old_value, "aml_Drive", None)
                if opp_val == self:
                    setattr(old_value, "aml_Drive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Drive"):
                opp_val = getattr(value, "aml_Drive", None)
                setattr(value, "aml_Drive", self)

class aml_NetWorkFeature:

    def __init__(self, name: str, value: str, aml_NetWorkFeature: "aml_Cable" = None):
        self.name = name
        self.value = value
        self.aml_NetWorkFeature = aml_NetWorkFeature
        
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
    def aml_NetWorkFeature(self):
        return self.__aml_NetWorkFeature

    @aml_NetWorkFeature.setter
    def aml_NetWorkFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_NetWorkFeature__aml_NetWorkFeature", None)
        self.__aml_NetWorkFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Cable15"):
                opp_val = getattr(old_value, "aml_Cable15", None)
                if opp_val == self:
                    setattr(old_value, "aml_Cable15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Cable15"):
                opp_val = getattr(value, "aml_Cable15", None)
                setattr(value, "aml_Cable15", self)

class aml_ColorFeature:

    def __init__(self, name: str, value: str, aml_ColorFeature: "aml_Cable" = None):
        self.name = name
        self.value = value
        self.aml_ColorFeature = aml_ColorFeature
        
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
    def aml_ColorFeature(self):
        return self.__aml_ColorFeature

    @aml_ColorFeature.setter
    def aml_ColorFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ColorFeature__aml_ColorFeature", None)
        self.__aml_ColorFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Cable"):
                opp_val = getattr(old_value, "aml_Cable", None)
                if opp_val == self:
                    setattr(old_value, "aml_Cable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Cable"):
                opp_val = getattr(value, "aml_Cable", None)
                setattr(value, "aml_Cable", self)

class aml_FormFeature:

    def __init__(self, name: str, value: int, aml_FormFeature: "aml_Drive" = None):
        self.name = name
        self.value = value
        self.aml_FormFeature = aml_FormFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def aml_FormFeature(self):
        return self.__aml_FormFeature

    @aml_FormFeature.setter
    def aml_FormFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_FormFeature__aml_FormFeature", None)
        self.__aml_FormFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Drive12"):
                opp_val = getattr(old_value, "aml_Drive12", None)
                if opp_val == self:
                    setattr(old_value, "aml_Drive12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Drive12"):
                opp_val = getattr(value, "aml_Drive12", None)
                setattr(value, "aml_Drive12", self)

class SuperEntity:

    pass
class aml_Cable(SuperEntity):

    pass
class aml_Drive(SuperEntity):

    pass
class aml_MaxFeature:

    def __init__(self, name: str, value: int, aml_MaxFeature: "aml_MinMax" = None):
        self.name = name
        self.value = value
        self.aml_MaxFeature = aml_MaxFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def aml_MaxFeature(self):
        return self.__aml_MaxFeature

    @aml_MaxFeature.setter
    def aml_MaxFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_MaxFeature__aml_MaxFeature", None)
        self.__aml_MaxFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MinMax5"):
                opp_val = getattr(old_value, "aml_MinMax5", None)
                if opp_val == self:
                    setattr(old_value, "aml_MinMax5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MinMax5"):
                opp_val = getattr(value, "aml_MinMax5", None)
                setattr(value, "aml_MinMax5", self)

class aml_ProductPUIDFeature:

    def __init__(self, name: str, values: int, aml_ProductPUIDFeature: "aml_MinMax" = None):
        self.name = name
        self.values = values
        self.aml_ProductPUIDFeature = aml_ProductPUIDFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def values(self) -> int:
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values

    @property
    def aml_ProductPUIDFeature(self):
        return self.__aml_ProductPUIDFeature

    @aml_ProductPUIDFeature.setter
    def aml_ProductPUIDFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_ProductPUIDFeature__aml_ProductPUIDFeature", None)
        self.__aml_ProductPUIDFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MinMax3"):
                opp_val = getattr(old_value, "aml_MinMax3", None)
                if opp_val == self:
                    setattr(old_value, "aml_MinMax3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MinMax3"):
                opp_val = getattr(value, "aml_MinMax3", None)
                setattr(value, "aml_MinMax3", self)

class aml_TargetGroupFeature:

    def __init__(self, name: str, value: str, aml_TargetGroupFeature: "aml_MinMax" = None):
        self.name = name
        self.value = value
        self.aml_TargetGroupFeature = aml_TargetGroupFeature
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aml_TargetGroupFeature(self):
        return self.__aml_TargetGroupFeature

    @aml_TargetGroupFeature.setter
    def aml_TargetGroupFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_TargetGroupFeature__aml_TargetGroupFeature", None)
        self.__aml_TargetGroupFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_MinMax"):
                opp_val = getattr(old_value, "aml_MinMax", None)
                if opp_val == self:
                    setattr(old_value, "aml_MinMax", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_MinMax"):
                opp_val = getattr(value, "aml_MinMax", None)
                setattr(value, "aml_MinMax", self)

class AbstractElements:

    pass
class aml_SuperEntity(AbstractElements):

    pass
class aml_PriceRule(AbstractElements):

    pass
class aml_Entity(AbstractElements):

    pass
class aml_MinMax(AbstractElements):

    pass
class aml_AbstractElements:

    def __init__(self, name: str, aml_AbstractElements: "aml_Aml" = None):
        self.name = name
        self.aml_AbstractElements = aml_AbstractElements
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aml_AbstractElements(self):
        return self.__aml_AbstractElements

    @aml_AbstractElements.setter
    def aml_AbstractElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aml_AbstractElements__aml_AbstractElements", None)
        self.__aml_AbstractElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aml_Aml"):
                opp_val = getattr(old_value, "aml_Aml", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aml_Aml"):
                opp_val = getattr(value, "aml_Aml", None)
                if opp_val is None:
                    setattr(value, "aml_Aml", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aml_Aml:

    pass
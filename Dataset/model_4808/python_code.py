from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Sex(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


############################################
# Definition of Classes
############################################

class model_EStringToStringMapEntry:

    pass
class model_ObjectWithMap:

    pass
class model_Node:

    def __init__(self, label: str, Node: "model_Node" = None, source: "model_Node" = None, Node46: "model_Node" = None, target: "model_Node" = None, model_Node: "model_Node" = None, model_Node47: set["model_Node"] = None, model_Node51: "model_Node" = None, model_Node49: set["model_Node"] = None, model_Node54: "model_Node" = None, model_Node52: "model_Node" = None):
        self.label = label
        self.Node = Node
        self.source = source
        self.Node46 = Node46
        self.target = target
        self.model_Node = model_Node
        self.model_Node47 = model_Node47 if model_Node47 is not None else set()
        self.model_Node51 = model_Node51
        self.model_Node49 = model_Node49 if model_Node49 is not None else set()
        self.model_Node54 = model_Node54
        self.model_Node52 = model_Node52
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)

    @property
    def model_Node(self):
        return self.__model_Node

    @model_Node.setter
    def model_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node", None)
        self.__model_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node47"):
                opp_val = getattr(old_value, "model_Node47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node47"):
                opp_val = getattr(value, "model_Node47", None)
                if opp_val is None:
                    setattr(value, "model_Node47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Node49(self):
        return self.__model_Node49

    @model_Node49.setter
    def model_Node49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node49", None)
        self.__model_Node49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Node51"):
                    opp_val = getattr(item, "model_Node51", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Node51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Node51"):
                    opp_val = getattr(item, "model_Node51", None)
                    
                    setattr(item, "model_Node51", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def model_Node47(self):
        return self.__model_Node47

    @model_Node47.setter
    def model_Node47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node47", None)
        self.__model_Node47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Node"):
                    opp_val = getattr(item, "model_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Node"):
                    opp_val = getattr(item, "model_Node", None)
                    
                    setattr(item, "model_Node", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__target", None)
        self.__target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node46"):
                opp_val = getattr(old_value, "Node46", None)
                if opp_val == self:
                    setattr(old_value, "Node46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node46"):
                opp_val = getattr(value, "Node46", None)
                setattr(value, "Node46", self)

    @property
    def model_Node52(self):
        return self.__model_Node52

    @model_Node52.setter
    def model_Node52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node52", None)
        self.__model_Node52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node54"):
                opp_val = getattr(old_value, "model_Node54", None)
                if opp_val == self:
                    setattr(old_value, "model_Node54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node54"):
                opp_val = getattr(value, "model_Node54", None)
                setattr(value, "model_Node54", self)

    @property
    def model_Node51(self):
        return self.__model_Node51

    @model_Node51.setter
    def model_Node51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node51", None)
        self.__model_Node51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node49"):
                opp_val = getattr(old_value, "model_Node49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node49"):
                opp_val = getattr(value, "model_Node49", None)
                if opp_val is None:
                    setattr(value, "model_Node49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node46(self):
        return self.__Node46

    @Node46.setter
    def Node46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__Node46", None)
        self.__Node46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if opp_val == self:
                    setattr(old_value, "target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                setattr(value, "target", self)

    @property
    def model_Node54(self):
        return self.__model_Node54

    @model_Node54.setter
    def model_Node54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node54", None)
        self.__model_Node54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node52"):
                opp_val = getattr(old_value, "model_Node52", None)
                if opp_val == self:
                    setattr(old_value, "model_Node52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node52"):
                opp_val = getattr(value, "model_Node52", None)
                setattr(value, "model_Node52", self)

class AbstractType:

    pass
class model_ConcreteTypeTwo(AbstractType):

    def __init__(self, propTypeTwo: str):
        self.propTypeTwo = propTypeTwo
        
    @property
    def propTypeTwo(self) -> str:
        return self.__propTypeTwo

    @propTypeTwo.setter
    def propTypeTwo(self, propTypeTwo: str):
        self.__propTypeTwo = propTypeTwo

class model_ConcreteTypeOne(AbstractType):

    def __init__(self, propTypeOne: str):
        self.propTypeOne = propTypeOne
        
    @property
    def propTypeOne(self) -> str:
        return self.__propTypeOne

    @propTypeOne.setter
    def propTypeOne(self, propTypeOne: str):
        self.__propTypeOne = propTypeOne

class model_AbstractType(ABC):

    def __init__(self, name: str, model_AbstractType: "model_Container" = None, model_AbstractType41: "model_AbstractType" = None, model_AbstractType39: set["model_AbstractType"] = None):
        self.name = name
        self.model_AbstractType = model_AbstractType
        self.model_AbstractType41 = model_AbstractType41
        self.model_AbstractType39 = model_AbstractType39 if model_AbstractType39 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_AbstractType41(self):
        return self.__model_AbstractType41

    @model_AbstractType41.setter
    def model_AbstractType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractType__model_AbstractType41", None)
        self.__model_AbstractType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractType39"):
                opp_val = getattr(old_value, "model_AbstractType39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractType39"):
                opp_val = getattr(value, "model_AbstractType39", None)
                if opp_val is None:
                    setattr(value, "model_AbstractType39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_AbstractType(self):
        return self.__model_AbstractType

    @model_AbstractType.setter
    def model_AbstractType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractType__model_AbstractType", None)
        self.__model_AbstractType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Container"):
                opp_val = getattr(old_value, "model_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Container"):
                opp_val = getattr(value, "model_Container", None)
                if opp_val is None:
                    setattr(value, "model_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_AbstractType39(self):
        return self.__model_AbstractType39

    @model_AbstractType39.setter
    def model_AbstractType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractType__model_AbstractType39", None)
        self.__model_AbstractType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_AbstractType41"):
                    opp_val = getattr(item, "model_AbstractType41", None)
                    
                    if opp_val == self:
                        setattr(item, "model_AbstractType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_AbstractType41"):
                    opp_val = getattr(item, "model_AbstractType41", None)
                    
                    setattr(item, "model_AbstractType41", self)
                    

class model_Container:

    pass
class model_ETypes:

    def __init__(self, eByteArray: str, eChar: str, eDate: date, eFloat: float, eLong: str, eShort: str, uris: str, eString: str, eStrings: str, eBoolean: bool, eBooleans: str, eInt: int, eInts: int, doubleValue: str, eDouble: float, eDoubles: str, eBigDecimal: str, eBigInteger: str, eByte: str):
        self.eByteArray = eByteArray
        self.eChar = eChar
        self.eDate = eDate
        self.eFloat = eFloat
        self.eLong = eLong
        self.eShort = eShort
        self.uris = uris
        self.eString = eString
        self.eStrings = eStrings
        self.eBoolean = eBoolean
        self.eBooleans = eBooleans
        self.eInt = eInt
        self.eInts = eInts
        self.doubleValue = doubleValue
        self.eDouble = eDouble
        self.eDoubles = eDoubles
        self.eBigDecimal = eBigDecimal
        self.eBigInteger = eBigInteger
        self.eByte = eByte
        
    @property
    def eShort(self) -> str:
        return self.__eShort

    @eShort.setter
    def eShort(self, eShort: str):
        self.__eShort = eShort

    @property
    def eInts(self) -> int:
        return self.__eInts

    @eInts.setter
    def eInts(self, eInts: int):
        self.__eInts = eInts

    @property
    def doubleValue(self) -> str:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: str):
        self.__doubleValue = doubleValue

    @property
    def eBoolean(self) -> bool:
        return self.__eBoolean

    @eBoolean.setter
    def eBoolean(self, eBoolean: bool):
        self.__eBoolean = eBoolean

    @property
    def eByteArray(self) -> str:
        return self.__eByteArray

    @eByteArray.setter
    def eByteArray(self, eByteArray: str):
        self.__eByteArray = eByteArray

    @property
    def eStrings(self) -> str:
        return self.__eStrings

    @eStrings.setter
    def eStrings(self, eStrings: str):
        self.__eStrings = eStrings

    @property
    def eBigDecimal(self) -> str:
        return self.__eBigDecimal

    @eBigDecimal.setter
    def eBigDecimal(self, eBigDecimal: str):
        self.__eBigDecimal = eBigDecimal

    @property
    def eBooleans(self) -> str:
        return self.__eBooleans

    @eBooleans.setter
    def eBooleans(self, eBooleans: str):
        self.__eBooleans = eBooleans

    @property
    def uris(self) -> str:
        return self.__uris

    @uris.setter
    def uris(self, uris: str):
        self.__uris = uris

    @property
    def eFloat(self) -> float:
        return self.__eFloat

    @eFloat.setter
    def eFloat(self, eFloat: float):
        self.__eFloat = eFloat

    @property
    def eDate(self) -> date:
        return self.__eDate

    @eDate.setter
    def eDate(self, eDate: date):
        self.__eDate = eDate

    @property
    def eInt(self) -> int:
        return self.__eInt

    @eInt.setter
    def eInt(self, eInt: int):
        self.__eInt = eInt

    @property
    def eByte(self) -> str:
        return self.__eByte

    @eByte.setter
    def eByte(self, eByte: str):
        self.__eByte = eByte

    @property
    def eBigInteger(self) -> str:
        return self.__eBigInteger

    @eBigInteger.setter
    def eBigInteger(self, eBigInteger: str):
        self.__eBigInteger = eBigInteger

    @property
    def eString(self) -> str:
        return self.__eString

    @eString.setter
    def eString(self, eString: str):
        self.__eString = eString

    @property
    def eDouble(self) -> float:
        return self.__eDouble

    @eDouble.setter
    def eDouble(self, eDouble: float):
        self.__eDouble = eDouble

    @property
    def eLong(self) -> str:
        return self.__eLong

    @eLong.setter
    def eLong(self, eLong: str):
        self.__eLong = eLong

    @property
    def eDoubles(self) -> str:
        return self.__eDoubles

    @eDoubles.setter
    def eDoubles(self, eDoubles: str):
        self.__eDoubles = eDoubles

    @property
    def eChar(self) -> str:
        return self.__eChar

    @eChar.setter
    def eChar(self, eChar: str):
        self.__eChar = eChar

class model_TargetObject:

    def __init__(self, singleAttribute: str, arrayAttribute: str, model_TargetObject: "model_PrimaryObject" = None, model_TargetObject13: "model_PrimaryObject" = None, model_TargetObject16: "model_PrimaryObject" = None, model_TargetObject19: "model_PrimaryObject" = None, model_TargetObject22: "model_PrimaryObject" = None, model_TargetObject25: "model_PrimaryObject" = None, model_TargetObject28: "model_PrimaryObject" = None, model_TargetObject31: "model_PrimaryObject" = None, model_TargetObject34: "model_PrimaryObject" = None, model_TargetObject37: "model_PrimaryObject" = None):
        self.singleAttribute = singleAttribute
        self.arrayAttribute = arrayAttribute
        self.model_TargetObject = model_TargetObject
        self.model_TargetObject13 = model_TargetObject13
        self.model_TargetObject16 = model_TargetObject16
        self.model_TargetObject19 = model_TargetObject19
        self.model_TargetObject22 = model_TargetObject22
        self.model_TargetObject25 = model_TargetObject25
        self.model_TargetObject28 = model_TargetObject28
        self.model_TargetObject31 = model_TargetObject31
        self.model_TargetObject34 = model_TargetObject34
        self.model_TargetObject37 = model_TargetObject37
        
    @property
    def singleAttribute(self) -> str:
        return self.__singleAttribute

    @singleAttribute.setter
    def singleAttribute(self, singleAttribute: str):
        self.__singleAttribute = singleAttribute

    @property
    def arrayAttribute(self) -> str:
        return self.__arrayAttribute

    @arrayAttribute.setter
    def arrayAttribute(self, arrayAttribute: str):
        self.__arrayAttribute = arrayAttribute

    @property
    def model_TargetObject37(self):
        return self.__model_TargetObject37

    @model_TargetObject37.setter
    def model_TargetObject37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject37", None)
        self.__model_TargetObject37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject36"):
                opp_val = getattr(old_value, "model_PrimaryObject36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject36"):
                opp_val = getattr(value, "model_PrimaryObject36", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject34(self):
        return self.__model_TargetObject34

    @model_TargetObject34.setter
    def model_TargetObject34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject34", None)
        self.__model_TargetObject34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject33"):
                opp_val = getattr(old_value, "model_PrimaryObject33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject33"):
                opp_val = getattr(value, "model_PrimaryObject33", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject16(self):
        return self.__model_TargetObject16

    @model_TargetObject16.setter
    def model_TargetObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject16", None)
        self.__model_TargetObject16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject15"):
                opp_val = getattr(old_value, "model_PrimaryObject15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject15"):
                opp_val = getattr(value, "model_PrimaryObject15", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject19(self):
        return self.__model_TargetObject19

    @model_TargetObject19.setter
    def model_TargetObject19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject19", None)
        self.__model_TargetObject19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject18"):
                opp_val = getattr(old_value, "model_PrimaryObject18", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject18"):
                opp_val = getattr(value, "model_PrimaryObject18", None)
                setattr(value, "model_PrimaryObject18", self)

    @property
    def model_TargetObject31(self):
        return self.__model_TargetObject31

    @model_TargetObject31.setter
    def model_TargetObject31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject31", None)
        self.__model_TargetObject31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject30"):
                opp_val = getattr(old_value, "model_PrimaryObject30", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject30"):
                opp_val = getattr(value, "model_PrimaryObject30", None)
                setattr(value, "model_PrimaryObject30", self)

    @property
    def model_TargetObject(self):
        return self.__model_TargetObject

    @model_TargetObject.setter
    def model_TargetObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject", None)
        self.__model_TargetObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject"):
                opp_val = getattr(old_value, "model_PrimaryObject", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject"):
                opp_val = getattr(value, "model_PrimaryObject", None)
                setattr(value, "model_PrimaryObject", self)

    @property
    def model_TargetObject25(self):
        return self.__model_TargetObject25

    @model_TargetObject25.setter
    def model_TargetObject25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject25", None)
        self.__model_TargetObject25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject24"):
                opp_val = getattr(old_value, "model_PrimaryObject24", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject24"):
                opp_val = getattr(value, "model_PrimaryObject24", None)
                setattr(value, "model_PrimaryObject24", self)

    @property
    def model_TargetObject22(self):
        return self.__model_TargetObject22

    @model_TargetObject22.setter
    def model_TargetObject22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject22", None)
        self.__model_TargetObject22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject21"):
                opp_val = getattr(old_value, "model_PrimaryObject21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject21"):
                opp_val = getattr(value, "model_PrimaryObject21", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject28(self):
        return self.__model_TargetObject28

    @model_TargetObject28.setter
    def model_TargetObject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject28", None)
        self.__model_TargetObject28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject27"):
                opp_val = getattr(old_value, "model_PrimaryObject27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject27"):
                opp_val = getattr(value, "model_PrimaryObject27", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject13(self):
        return self.__model_TargetObject13

    @model_TargetObject13.setter
    def model_TargetObject13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject13", None)
        self.__model_TargetObject13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject12"):
                opp_val = getattr(old_value, "model_PrimaryObject12", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject12"):
                opp_val = getattr(value, "model_PrimaryObject12", None)
                setattr(value, "model_PrimaryObject12", self)

class model_PrimaryObject:

    def __init__(self, name: str, idAttribute: str, unsettableAttribute: str, unsettableAttributeWithNonNullDefault: str, featureMapReferenceCollection: str, featureMapAttributeType1: str, featureMapAttributeType2: str, featureMapAttributeCollection: str, model_PrimaryObject: "model_TargetObject" = None, model_PrimaryObject10: "model_PrimaryObject" = None, model_PrimaryObject8: "model_PrimaryObject" = None, model_PrimaryObject12: "model_TargetObject" = None, model_PrimaryObject15: set["model_TargetObject"] = None, model_PrimaryObject18: "model_TargetObject" = None, model_PrimaryObject21: set["model_TargetObject"] = None, model_PrimaryObject24: "model_TargetObject" = None, model_PrimaryObject27: set["model_TargetObject"] = None, model_PrimaryObject30: "model_TargetObject" = None, model_PrimaryObject33: set["model_TargetObject"] = None, model_PrimaryObject36: set["model_TargetObject"] = None):
        self.name = name
        self.idAttribute = idAttribute
        self.unsettableAttribute = unsettableAttribute
        self.unsettableAttributeWithNonNullDefault = unsettableAttributeWithNonNullDefault
        self.featureMapReferenceCollection = featureMapReferenceCollection
        self.featureMapAttributeType1 = featureMapAttributeType1
        self.featureMapAttributeType2 = featureMapAttributeType2
        self.featureMapAttributeCollection = featureMapAttributeCollection
        self.model_PrimaryObject = model_PrimaryObject
        self.model_PrimaryObject10 = model_PrimaryObject10
        self.model_PrimaryObject8 = model_PrimaryObject8
        self.model_PrimaryObject12 = model_PrimaryObject12
        self.model_PrimaryObject15 = model_PrimaryObject15 if model_PrimaryObject15 is not None else set()
        self.model_PrimaryObject18 = model_PrimaryObject18
        self.model_PrimaryObject21 = model_PrimaryObject21 if model_PrimaryObject21 is not None else set()
        self.model_PrimaryObject24 = model_PrimaryObject24
        self.model_PrimaryObject27 = model_PrimaryObject27 if model_PrimaryObject27 is not None else set()
        self.model_PrimaryObject30 = model_PrimaryObject30
        self.model_PrimaryObject33 = model_PrimaryObject33 if model_PrimaryObject33 is not None else set()
        self.model_PrimaryObject36 = model_PrimaryObject36 if model_PrimaryObject36 is not None else set()
        
    @property
    def featureMapAttributeType1(self) -> str:
        return self.__featureMapAttributeType1

    @featureMapAttributeType1.setter
    def featureMapAttributeType1(self, featureMapAttributeType1: str):
        self.__featureMapAttributeType1 = featureMapAttributeType1

    @property
    def featureMapAttributeType2(self) -> str:
        return self.__featureMapAttributeType2

    @featureMapAttributeType2.setter
    def featureMapAttributeType2(self, featureMapAttributeType2: str):
        self.__featureMapAttributeType2 = featureMapAttributeType2

    @property
    def featureMapAttributeCollection(self) -> str:
        return self.__featureMapAttributeCollection

    @featureMapAttributeCollection.setter
    def featureMapAttributeCollection(self, featureMapAttributeCollection: str):
        self.__featureMapAttributeCollection = featureMapAttributeCollection

    @property
    def idAttribute(self) -> str:
        return self.__idAttribute

    @idAttribute.setter
    def idAttribute(self, idAttribute: str):
        self.__idAttribute = idAttribute

    @property
    def unsettableAttributeWithNonNullDefault(self) -> str:
        return self.__unsettableAttributeWithNonNullDefault

    @unsettableAttributeWithNonNullDefault.setter
    def unsettableAttributeWithNonNullDefault(self, unsettableAttributeWithNonNullDefault: str):
        self.__unsettableAttributeWithNonNullDefault = unsettableAttributeWithNonNullDefault

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def unsettableAttribute(self) -> str:
        return self.__unsettableAttribute

    @unsettableAttribute.setter
    def unsettableAttribute(self, unsettableAttribute: str):
        self.__unsettableAttribute = unsettableAttribute

    @property
    def featureMapReferenceCollection(self) -> str:
        return self.__featureMapReferenceCollection

    @featureMapReferenceCollection.setter
    def featureMapReferenceCollection(self, featureMapReferenceCollection: str):
        self.__featureMapReferenceCollection = featureMapReferenceCollection

    @property
    def model_PrimaryObject12(self):
        return self.__model_PrimaryObject12

    @model_PrimaryObject12.setter
    def model_PrimaryObject12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject12", None)
        self.__model_PrimaryObject12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject13"):
                opp_val = getattr(old_value, "model_TargetObject13", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject13"):
                opp_val = getattr(value, "model_TargetObject13", None)
                setattr(value, "model_TargetObject13", self)

    @property
    def model_PrimaryObject10(self):
        return self.__model_PrimaryObject10

    @model_PrimaryObject10.setter
    def model_PrimaryObject10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject10", None)
        self.__model_PrimaryObject10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject8"):
                opp_val = getattr(old_value, "model_PrimaryObject8", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject8"):
                opp_val = getattr(value, "model_PrimaryObject8", None)
                setattr(value, "model_PrimaryObject8", self)

    @property
    def model_PrimaryObject36(self):
        return self.__model_PrimaryObject36

    @model_PrimaryObject36.setter
    def model_PrimaryObject36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject36", None)
        self.__model_PrimaryObject36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject37"):
                    opp_val = getattr(item, "model_TargetObject37", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject37"):
                    opp_val = getattr(item, "model_TargetObject37", None)
                    
                    setattr(item, "model_TargetObject37", self)
                    

    @property
    def model_PrimaryObject33(self):
        return self.__model_PrimaryObject33

    @model_PrimaryObject33.setter
    def model_PrimaryObject33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject33", None)
        self.__model_PrimaryObject33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject34"):
                    opp_val = getattr(item, "model_TargetObject34", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject34"):
                    opp_val = getattr(item, "model_TargetObject34", None)
                    
                    setattr(item, "model_TargetObject34", self)
                    

    @property
    def model_PrimaryObject21(self):
        return self.__model_PrimaryObject21

    @model_PrimaryObject21.setter
    def model_PrimaryObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject21", None)
        self.__model_PrimaryObject21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject22"):
                    opp_val = getattr(item, "model_TargetObject22", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject22"):
                    opp_val = getattr(item, "model_TargetObject22", None)
                    
                    setattr(item, "model_TargetObject22", self)
                    

    @property
    def model_PrimaryObject15(self):
        return self.__model_PrimaryObject15

    @model_PrimaryObject15.setter
    def model_PrimaryObject15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject15", None)
        self.__model_PrimaryObject15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject16"):
                    opp_val = getattr(item, "model_TargetObject16", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject16"):
                    opp_val = getattr(item, "model_TargetObject16", None)
                    
                    setattr(item, "model_TargetObject16", self)
                    

    @property
    def model_PrimaryObject30(self):
        return self.__model_PrimaryObject30

    @model_PrimaryObject30.setter
    def model_PrimaryObject30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject30", None)
        self.__model_PrimaryObject30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject31"):
                opp_val = getattr(old_value, "model_TargetObject31", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject31"):
                opp_val = getattr(value, "model_TargetObject31", None)
                setattr(value, "model_TargetObject31", self)

    @property
    def model_PrimaryObject24(self):
        return self.__model_PrimaryObject24

    @model_PrimaryObject24.setter
    def model_PrimaryObject24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject24", None)
        self.__model_PrimaryObject24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject25"):
                opp_val = getattr(old_value, "model_TargetObject25", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject25"):
                opp_val = getattr(value, "model_TargetObject25", None)
                setattr(value, "model_TargetObject25", self)

    @property
    def model_PrimaryObject18(self):
        return self.__model_PrimaryObject18

    @model_PrimaryObject18.setter
    def model_PrimaryObject18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject18", None)
        self.__model_PrimaryObject18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject19"):
                opp_val = getattr(old_value, "model_TargetObject19", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject19"):
                opp_val = getattr(value, "model_TargetObject19", None)
                setattr(value, "model_TargetObject19", self)

    @property
    def model_PrimaryObject(self):
        return self.__model_PrimaryObject

    @model_PrimaryObject.setter
    def model_PrimaryObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject", None)
        self.__model_PrimaryObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject"):
                opp_val = getattr(old_value, "model_TargetObject", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject"):
                opp_val = getattr(value, "model_TargetObject", None)
                setattr(value, "model_TargetObject", self)

    @property
    def model_PrimaryObject27(self):
        return self.__model_PrimaryObject27

    @model_PrimaryObject27.setter
    def model_PrimaryObject27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject27", None)
        self.__model_PrimaryObject27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject28"):
                    opp_val = getattr(item, "model_TargetObject28", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject28"):
                    opp_val = getattr(item, "model_TargetObject28", None)
                    
                    setattr(item, "model_TargetObject28", self)
                    

    @property
    def model_PrimaryObject8(self):
        return self.__model_PrimaryObject8

    @model_PrimaryObject8.setter
    def model_PrimaryObject8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject8", None)
        self.__model_PrimaryObject8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject10"):
                opp_val = getattr(old_value, "model_PrimaryObject10", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject10"):
                opp_val = getattr(value, "model_PrimaryObject10", None)
                setattr(value, "model_PrimaryObject10", self)

class model_Address:

    def __init__(self, addId: str, city: str, street: str, number: str, model_Address: "model_User" = None):
        self.addId = addId
        self.city = city
        self.street = street
        self.number = number
        self.model_Address = model_Address
        
    @property
    def addId(self) -> str:
        return self.__addId

    @addId.setter
    def addId(self, addId: str):
        self.__addId = addId

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def model_Address(self):
        return self.__model_Address

    @model_Address.setter
    def model_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Address__model_Address", None)
        self.__model_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_User6"):
                opp_val = getattr(old_value, "model_User6", None)
                if opp_val == self:
                    setattr(old_value, "model_User6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_User6"):
                opp_val = getattr(value, "model_User6", None)
                setattr(value, "model_User6", self)

class model_User:

    def __init__(self, userId: str, name: str, birthDate: date, sex: str, model_User: "model_User" = None, model_User0: set["model_User"] = None, model_User4: "model_User" = None, model_User2: "model_User" = None, model_User6: "model_Address" = None):
        self.userId = userId
        self.name = name
        self.birthDate = birthDate
        self.sex = sex
        self.model_User = model_User
        self.model_User0 = model_User0 if model_User0 is not None else set()
        self.model_User4 = model_User4
        self.model_User2 = model_User2
        self.model_User6 = model_User6
        
    @property
    def birthDate(self) -> date:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def model_User2(self):
        return self.__model_User2

    @model_User2.setter
    def model_User2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User2", None)
        self.__model_User2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_User4"):
                opp_val = getattr(old_value, "model_User4", None)
                if opp_val == self:
                    setattr(old_value, "model_User4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_User4"):
                opp_val = getattr(value, "model_User4", None)
                setattr(value, "model_User4", self)

    @property
    def model_User0(self):
        return self.__model_User0

    @model_User0.setter
    def model_User0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User0", None)
        self.__model_User0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    if opp_val == self:
                        setattr(item, "model_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    setattr(item, "model_User", self)
                    

    @property
    def model_User4(self):
        return self.__model_User4

    @model_User4.setter
    def model_User4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User4", None)
        self.__model_User4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_User2"):
                opp_val = getattr(old_value, "model_User2", None)
                if opp_val == self:
                    setattr(old_value, "model_User2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_User2"):
                opp_val = getattr(value, "model_User2", None)
                setattr(value, "model_User2", self)

    @property
    def model_User(self):
        return self.__model_User

    @model_User.setter
    def model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User", None)
        self.__model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_User0"):
                opp_val = getattr(old_value, "model_User0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_User0"):
                opp_val = getattr(value, "model_User0", None)
                if opp_val is None:
                    setattr(value, "model_User0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_User6(self):
        return self.__model_User6

    @model_User6.setter
    def model_User6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User6", None)
        self.__model_User6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Address"):
                opp_val = getattr(old_value, "model_Address", None)
                if opp_val == self:
                    setattr(old_value, "model_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Address"):
                opp_val = getattr(value, "model_Address", None)
                setattr(value, "model_Address", self)

from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class muddle_BooleanType(PrimitiveType):

    pass
class muddle_RealType(PrimitiveType):

    pass
class muddle_StringType(PrimitiveType):

    pass
class muddle_IntegerType(PrimitiveType):

    pass
class MuddleElementType:

    pass
class muddle_LinkElementType(MuddleElementType):

    pass
class muddle_Feature:

    def __init__(self, name: str, many: bool, primary: bool, runtime: bool, muddle_Feature: "muddle_Type" = None, features: "muddle_MuddleElementType" = None, feature: set["muddle_Slot"] = None, Feature: "muddle_Slot" = None, Feature18: "muddle_MuddleElementType" = None, muddle_Feature26: "muddle_LinkElementType" = None, muddle_Feature29: "muddle_LinkElementType" = None, muddle_Feature32: "muddle_LinkElementType" = None, muddle_Feature35: "muddle_LinkElementType" = None):
        self.name = name
        self.many = many
        self.primary = primary
        self.runtime = runtime
        self.muddle_Feature = muddle_Feature
        self.features = features
        self.feature = feature if feature is not None else set()
        self.Feature = Feature
        self.Feature18 = Feature18
        self.muddle_Feature26 = muddle_Feature26
        self.muddle_Feature29 = muddle_Feature29
        self.muddle_Feature32 = muddle_Feature32
        self.muddle_Feature35 = muddle_Feature35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def runtime(self) -> bool:
        return self.__runtime

    @runtime.setter
    def runtime(self, runtime: bool):
        self.__runtime = runtime

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slots"):
                opp_val = getattr(old_value, "slots", None)
                if opp_val == self:
                    setattr(old_value, "slots", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slots"):
                opp_val = getattr(value, "slots", None)
                setattr(value, "slots", self)

    @property
    def muddle_Feature(self):
        return self.__muddle_Feature

    @muddle_Feature.setter
    def muddle_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature", None)
        self.__muddle_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_Type10"):
                opp_val = getattr(old_value, "muddle_Type10", None)
                if opp_val == self:
                    setattr(old_value, "muddle_Type10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_Type10"):
                opp_val = getattr(value, "muddle_Type10", None)
                setattr(value, "muddle_Type10", self)

    @property
    def muddle_Feature32(self):
        return self.__muddle_Feature32

    @muddle_Feature32.setter
    def muddle_Feature32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature32", None)
        self.__muddle_Feature32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType31"):
                opp_val = getattr(old_value, "muddle_LinkElementType31", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType31"):
                opp_val = getattr(value, "muddle_LinkElementType31", None)
                setattr(value, "muddle_LinkElementType31", self)

    @property
    def muddle_Feature35(self):
        return self.__muddle_Feature35

    @muddle_Feature35.setter
    def muddle_Feature35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature35", None)
        self.__muddle_Feature35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType34"):
                opp_val = getattr(old_value, "muddle_LinkElementType34", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType34"):
                opp_val = getattr(value, "muddle_LinkElementType34", None)
                setattr(value, "muddle_LinkElementType34", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Slot14"):
                    opp_val = getattr(item, "Slot14", None)
                    
                    if opp_val == self:
                        setattr(item, "Slot14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slot14"):
                    opp_val = getattr(item, "Slot14", None)
                    
                    setattr(item, "Slot14", self)
                    

    @property
    def Feature18(self):
        return self.__Feature18

    @Feature18.setter
    def Feature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__Feature18", None)
        self.__Feature18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningType"):
                opp_val = getattr(old_value, "owningType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningType"):
                opp_val = getattr(value, "owningType", None)
                if opp_val is None:
                    setattr(value, "owningType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def muddle_Feature29(self):
        return self.__muddle_Feature29

    @muddle_Feature29.setter
    def muddle_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature29", None)
        self.__muddle_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType28"):
                opp_val = getattr(old_value, "muddle_LinkElementType28", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType28"):
                opp_val = getattr(value, "muddle_LinkElementType28", None)
                setattr(value, "muddle_LinkElementType28", self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MuddleElementType12"):
                opp_val = getattr(old_value, "MuddleElementType12", None)
                if opp_val == self:
                    setattr(old_value, "MuddleElementType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MuddleElementType12"):
                opp_val = getattr(value, "MuddleElementType12", None)
                setattr(value, "MuddleElementType12", self)

    @property
    def muddle_Feature26(self):
        return self.__muddle_Feature26

    @muddle_Feature26.setter
    def muddle_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature26", None)
        self.__muddle_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType"):
                opp_val = getattr(old_value, "muddle_LinkElementType", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType"):
                opp_val = getattr(value, "muddle_LinkElementType", None)
                setattr(value, "muddle_LinkElementType", self)

class Type:

    pass
class muddle_PrimitiveType(Type):

    pass
class muddle_MuddleElementType(Type):

    pass
class muddle_Slot:

    def __init__(self, values: str, Slot: "muddle_MuddleElement" = None, slots7: "muddle_MuddleElement" = None, Slot14: "muddle_Feature" = None, slots: "muddle_Feature" = None):
        self.values = values
        self.Slot = Slot
        self.slots7 = slots7
        self.Slot14 = Slot14
        self.slots = slots
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def Slot(self):
        return self.__Slot

    @Slot.setter
    def Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__Slot", None)
        self.__Slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningElement"):
                opp_val = getattr(old_value, "owningElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningElement"):
                opp_val = getattr(value, "owningElement", None)
                if opp_val is None:
                    setattr(value, "owningElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def slots7(self):
        return self.__slots7

    @slots7.setter
    def slots7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__slots7", None)
        self.__slots7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MuddleElement8"):
                opp_val = getattr(old_value, "MuddleElement8", None)
                if opp_val == self:
                    setattr(old_value, "MuddleElement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MuddleElement8"):
                opp_val = getattr(value, "MuddleElement8", None)
                setattr(value, "MuddleElement8", self)

    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__slots", None)
        self.__slots = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature"):
                opp_val = getattr(old_value, "Feature", None)
                if opp_val == self:
                    setattr(old_value, "Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature"):
                opp_val = getattr(value, "Feature", None)
                setattr(value, "Feature", self)

    @property
    def Slot14(self):
        return self.__Slot14

    @Slot14.setter
    def Slot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__Slot14", None)
        self.__Slot14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class muddle_MuddleElement:

    def __init__(self, id: str, MuddleElement: "muddle_Muddle" = None, owningElement: set["muddle_Slot"] = None, instances: "muddle_MuddleElementType" = None, elements: "muddle_Muddle" = None, MuddleElement8: "muddle_Slot" = None, MuddleElement16: "muddle_MuddleElementType" = None):
        self.id = id
        self.MuddleElement = MuddleElement
        self.owningElement = owningElement if owningElement is not None else set()
        self.instances = instances
        self.elements = elements
        self.MuddleElement8 = MuddleElement8
        self.MuddleElement16 = MuddleElement16
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Muddle"):
                opp_val = getattr(old_value, "Muddle", None)
                if opp_val == self:
                    setattr(old_value, "Muddle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Muddle"):
                opp_val = getattr(value, "Muddle", None)
                setattr(value, "Muddle", self)

    @property
    def MuddleElement8(self):
        return self.__MuddleElement8

    @MuddleElement8.setter
    def MuddleElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__MuddleElement8", None)
        self.__MuddleElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slots7"):
                opp_val = getattr(old_value, "slots7", None)
                if opp_val == self:
                    setattr(old_value, "slots7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slots7"):
                opp_val = getattr(value, "slots7", None)
                setattr(value, "slots7", self)

    @property
    def MuddleElement(self):
        return self.__MuddleElement

    @MuddleElement.setter
    def MuddleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__MuddleElement", None)
        self.__MuddleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle"):
                opp_val = getattr(old_value, "muddle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle"):
                opp_val = getattr(value, "muddle", None)
                if opp_val is None:
                    setattr(value, "muddle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MuddleElement16(self):
        return self.__MuddleElement16

    @MuddleElement16.setter
    def MuddleElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__MuddleElement16", None)
        self.__MuddleElement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningElement(self):
        return self.__owningElement

    @owningElement.setter
    def owningElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__owningElement", None)
        self.__owningElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Slot"):
                    opp_val = getattr(item, "Slot", None)
                    
                    if opp_val == self:
                        setattr(item, "Slot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slot"):
                    opp_val = getattr(item, "Slot", None)
                    
                    setattr(item, "Slot", self)
                    

    @property
    def instances(self):
        return self.__instances

    @instances.setter
    def instances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__instances", None)
        self.__instances = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MuddleElementType"):
                opp_val = getattr(old_value, "MuddleElementType", None)
                if opp_val == self:
                    setattr(old_value, "MuddleElementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MuddleElementType"):
                opp_val = getattr(value, "MuddleElementType", None)
                setattr(value, "MuddleElementType", self)

class muddle_Type(ABC):

    def __init__(self, name: str, muddle_Type: "muddle_Muddle" = None, muddle_Type10: "muddle_Feature" = None):
        self.name = name
        self.muddle_Type = muddle_Type
        self.muddle_Type10 = muddle_Type10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def muddle_Type10(self):
        return self.__muddle_Type10

    @muddle_Type10.setter
    def muddle_Type10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Type__muddle_Type10", None)
        self.__muddle_Type10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_Feature"):
                opp_val = getattr(old_value, "muddle_Feature", None)
                if opp_val == self:
                    setattr(old_value, "muddle_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_Feature"):
                opp_val = getattr(value, "muddle_Feature", None)
                setattr(value, "muddle_Feature", self)

    @property
    def muddle_Type(self):
        return self.__muddle_Type

    @muddle_Type.setter
    def muddle_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Type__muddle_Type", None)
        self.__muddle_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_Muddle"):
                opp_val = getattr(old_value, "muddle_Muddle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_Muddle"):
                opp_val = getattr(value, "muddle_Muddle", None)
                if opp_val is None:
                    setattr(value, "muddle_Muddle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class muddle_Muddle:

    pass
from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class muddle_RealType(PrimitiveType):

    pass
class muddle_StringType(PrimitiveType):

    pass
class muddle_BooleanType(PrimitiveType):

    pass
class muddle_IntegerType(PrimitiveType):

    pass
class Type:

    pass
class muddle_PrimitiveType(Type):

    pass
class MuddleElementType:

    pass
class muddle_LinkElementType(MuddleElementType):

    pass
class muddle_Feature:

    def __init__(self, many: bool, primary: bool, runtime: bool, name: str, muddle_Feature: "muddle_Type" = None, features: "muddle_MuddleElementType" = None, Feature: "muddle_Slot" = None, muddle_Feature27: "muddle_LinkElementType" = None, muddle_Feature30: "muddle_LinkElementType" = None, feature: set["muddle_Slot"] = None, Feature19: "muddle_MuddleElementType" = None, muddle_Feature33: "muddle_LinkElementType" = None, muddle_Feature36: "muddle_LinkElementType" = None):
        self.many = many
        self.primary = primary
        self.runtime = runtime
        self.name = name
        self.muddle_Feature = muddle_Feature
        self.features = features
        self.Feature = Feature
        self.muddle_Feature27 = muddle_Feature27
        self.muddle_Feature30 = muddle_Feature30
        self.feature = feature if feature is not None else set()
        self.Feature19 = Feature19
        self.muddle_Feature33 = muddle_Feature33
        self.muddle_Feature36 = muddle_Feature36
        
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
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Feature19(self):
        return self.__Feature19

    @Feature19.setter
    def Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__Feature19", None)
        self.__Feature19 = value
        
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
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MuddleElementType13"):
                opp_val = getattr(old_value, "MuddleElementType13", None)
                if opp_val == self:
                    setattr(old_value, "MuddleElementType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MuddleElementType13"):
                opp_val = getattr(value, "MuddleElementType13", None)
                setattr(value, "MuddleElementType13", self)

    @property
    def muddle_Feature33(self):
        return self.__muddle_Feature33

    @muddle_Feature33.setter
    def muddle_Feature33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature33", None)
        self.__muddle_Feature33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType32"):
                opp_val = getattr(old_value, "muddle_LinkElementType32", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType32"):
                opp_val = getattr(value, "muddle_LinkElementType32", None)
                setattr(value, "muddle_LinkElementType32", self)

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
    def muddle_Feature30(self):
        return self.__muddle_Feature30

    @muddle_Feature30.setter
    def muddle_Feature30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature30", None)
        self.__muddle_Feature30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType29"):
                opp_val = getattr(old_value, "muddle_LinkElementType29", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType29"):
                opp_val = getattr(value, "muddle_LinkElementType29", None)
                setattr(value, "muddle_LinkElementType29", self)

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
            if hasattr(old_value, "muddle_Type11"):
                opp_val = getattr(old_value, "muddle_Type11", None)
                if opp_val == self:
                    setattr(old_value, "muddle_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_Type11"):
                opp_val = getattr(value, "muddle_Type11", None)
                setattr(value, "muddle_Type11", self)

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
                if hasattr(item, "Slot15"):
                    opp_val = getattr(item, "Slot15", None)
                    
                    if opp_val == self:
                        setattr(item, "Slot15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slot15"):
                    opp_val = getattr(item, "Slot15", None)
                    
                    setattr(item, "Slot15", self)
                    

    @property
    def muddle_Feature27(self):
        return self.__muddle_Feature27

    @muddle_Feature27.setter
    def muddle_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature27", None)
        self.__muddle_Feature27 = value
        
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

    @property
    def muddle_Feature36(self):
        return self.__muddle_Feature36

    @muddle_Feature36.setter
    def muddle_Feature36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Feature__muddle_Feature36", None)
        self.__muddle_Feature36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_LinkElementType35"):
                opp_val = getattr(old_value, "muddle_LinkElementType35", None)
                if opp_val == self:
                    setattr(old_value, "muddle_LinkElementType35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_LinkElementType35"):
                opp_val = getattr(value, "muddle_LinkElementType35", None)
                setattr(value, "muddle_LinkElementType35", self)

class muddle_MuddleElementStyle:

    def __init__(self, color: str, shape: str, width: float, height: float, borderWidth: float, labelFontSize: int, x: float, y: float, muddle_MuddleElementStyle: "muddle_MuddleElement" = None):
        self.color = color
        self.shape = shape
        self.width = width
        self.height = height
        self.borderWidth = borderWidth
        self.labelFontSize = labelFontSize
        self.x = x
        self.y = y
        self.muddle_MuddleElementStyle = muddle_MuddleElementStyle
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def borderWidth(self) -> float:
        return self.__borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: float):
        self.__borderWidth = borderWidth

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def labelFontSize(self) -> int:
        return self.__labelFontSize

    @labelFontSize.setter
    def labelFontSize(self, labelFontSize: int):
        self.__labelFontSize = labelFontSize

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def muddle_MuddleElementStyle(self):
        return self.__muddle_MuddleElementStyle

    @muddle_MuddleElementStyle.setter
    def muddle_MuddleElementStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElementStyle__muddle_MuddleElementStyle", None)
        self.__muddle_MuddleElementStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_MuddleElement"):
                opp_val = getattr(old_value, "muddle_MuddleElement", None)
                if opp_val == self:
                    setattr(old_value, "muddle_MuddleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_MuddleElement"):
                opp_val = getattr(value, "muddle_MuddleElement", None)
                setattr(value, "muddle_MuddleElement", self)

class muddle_MuddleElementType(Type):

    pass
class muddle_Slot:

    def __init__(self, values: str, Slot: "muddle_MuddleElement" = None, slots: "muddle_Feature" = None, slots8: "muddle_MuddleElement" = None, Slot15: "muddle_Feature" = None):
        self.values = values
        self.Slot = Slot
        self.slots = slots
        self.slots8 = slots8
        self.Slot15 = Slot15
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def slots8(self):
        return self.__slots8

    @slots8.setter
    def slots8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__slots8", None)
        self.__slots8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MuddleElement9"):
                opp_val = getattr(old_value, "MuddleElement9", None)
                if opp_val == self:
                    setattr(old_value, "MuddleElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MuddleElement9"):
                opp_val = getattr(value, "MuddleElement9", None)
                setattr(value, "MuddleElement9", self)

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
    def Slot15(self):
        return self.__Slot15

    @Slot15.setter
    def Slot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Slot__Slot15", None)
        self.__Slot15 = value
        
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

    def __init__(self, id: str, MuddleElement: "muddle_Muddle" = None, owningElement: set["muddle_Slot"] = None, instances: "muddle_MuddleElementType" = None, elements: "muddle_Muddle" = None, muddle_MuddleElement: "muddle_MuddleElementStyle" = None, MuddleElement9: "muddle_Slot" = None, MuddleElement17: "muddle_MuddleElementType" = None):
        self.id = id
        self.MuddleElement = MuddleElement
        self.owningElement = owningElement if owningElement is not None else set()
        self.instances = instances
        self.elements = elements
        self.muddle_MuddleElement = muddle_MuddleElement
        self.MuddleElement9 = MuddleElement9
        self.MuddleElement17 = MuddleElement17
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def muddle_MuddleElement(self):
        return self.__muddle_MuddleElement

    @muddle_MuddleElement.setter
    def muddle_MuddleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__muddle_MuddleElement", None)
        self.__muddle_MuddleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "muddle_MuddleElementStyle"):
                opp_val = getattr(old_value, "muddle_MuddleElementStyle", None)
                if opp_val == self:
                    setattr(old_value, "muddle_MuddleElementStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "muddle_MuddleElementStyle"):
                opp_val = getattr(value, "muddle_MuddleElementStyle", None)
                setattr(value, "muddle_MuddleElementStyle", self)

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
    def MuddleElement9(self):
        return self.__MuddleElement9

    @MuddleElement9.setter
    def MuddleElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__MuddleElement9", None)
        self.__MuddleElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slots8"):
                opp_val = getattr(old_value, "slots8", None)
                if opp_val == self:
                    setattr(old_value, "slots8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slots8"):
                opp_val = getattr(value, "slots8", None)
                setattr(value, "slots8", self)

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
    def MuddleElement17(self):
        return self.__MuddleElement17

    @MuddleElement17.setter
    def MuddleElement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_MuddleElement__MuddleElement17", None)
        self.__MuddleElement17 = value
        
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

class muddle_Type(ABC):

    def __init__(self, name: str, muddle_Type: "muddle_Muddle" = None, muddle_Type11: "muddle_Feature" = None):
        self.name = name
        self.muddle_Type = muddle_Type
        self.muddle_Type11 = muddle_Type11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def muddle_Type11(self):
        return self.__muddle_Type11

    @muddle_Type11.setter
    def muddle_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_muddle_Type__muddle_Type11", None)
        self.__muddle_Type11 = value
        
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
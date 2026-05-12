from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FontOption(Enum):
    ITALIC = "ITALIC"
    BOLD = "BOLD"
    UNDERLINE = "UNDERLINE"
    STRIKE = "STRIKE"


############################################
# Definition of Classes
############################################

class Styling_EObject:

    pass
class Parameter:

    pass
class Styling_BooleanParameter(Parameter):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class Styling_EObjectParameter(Parameter):

    pass
class Styling_IntParameter(Parameter):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Styling_Parameter(ABC):

    def __init__(self, name: str, Styling_Parameter: "Styling_OperationPattern" = None):
        self.name = name
        self.Styling_Parameter = Styling_Parameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Styling_Parameter(self):
        return self.__Styling_Parameter

    @Styling_Parameter.setter
    def Styling_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Parameter__Styling_Parameter", None)
        self.__Styling_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_OperationPattern"):
                opp_val = getattr(old_value, "Styling_OperationPattern", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_OperationPattern"):
                opp_val = getattr(value, "Styling_OperationPattern", None)
                if opp_val is None:
                    setattr(value, "Styling_OperationPattern", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getObjectValue(self) :
        # TODO: Implement getObjectValue method
        pass

class Styling_StringParameter(Parameter):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Pattern:

    pass
class Styling_OperationPattern(Pattern):

    def __init__(self, operation: str, Styling_OperationPattern: set["Styling_Parameter"] = None):
        self.operation = operation
        self.Styling_OperationPattern = Styling_OperationPattern if Styling_OperationPattern is not None else set()
        
        pass
    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation


    @property
    def Styling_OperationPattern(self):
        return self.__Styling_OperationPattern

    @Styling_OperationPattern.setter
    def Styling_OperationPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_OperationPattern__Styling_OperationPattern", None)
        self.__Styling_OperationPattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Styling_Parameter"):
                    opp_val = getattr(item, "Styling_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Styling_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Styling_Parameter"):
                    opp_val = getattr(item, "Styling_Parameter", None)
                    
                    setattr(item, "Styling_Parameter", self)
                    

class Styling_ModelPattern(Pattern):

    def __init__(self, attributeName: str):
        self.attributeName = attributeName
        
        pass
    @property
    def attributeName(self):
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName


class Styling_ConstantPattern(Pattern):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Styling_Styling:

    pass
class Styling_Icon:

    def __init__(self, image: str, Styling_Icon: "Styling_CaseStyle" = None):
        self.image = image
        self.Styling_Icon = Styling_Icon
        
        pass
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image


    @property
    def Styling_Icon(self):
        return self.__Styling_Icon

    @Styling_Icon.setter
    def Styling_Icon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Icon__Styling_Icon", None)
        self.__Styling_Icon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_CaseStyle11"):
                opp_val = getattr(old_value, "Styling_CaseStyle11", None)
                if opp_val == self:
                    setattr(old_value, "Styling_CaseStyle11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_CaseStyle11"):
                opp_val = getattr(value, "Styling_CaseStyle11", None)
                setattr(value, "Styling_CaseStyle11", self)

class Styling_Style:

    def __init__(self, appliedFonts: str, color: str, Styling_Style: "Styling_Segment" = None):
        self.appliedFonts = appliedFonts
        self.color = color
        self.Styling_Style = Styling_Style
        
        pass
    @property
    def appliedFonts(self):
        return self.__appliedFonts

    @appliedFonts.setter
    def appliedFonts(self, appliedFonts: str):
        self.__appliedFonts = appliedFonts


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def Styling_Style(self):
        return self.__Styling_Style

    @Styling_Style.setter
    def Styling_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Style__Styling_Style", None)
        self.__Styling_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Segment"):
                opp_val = getattr(old_value, "Styling_Segment", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Segment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Segment"):
                opp_val = getattr(value, "Styling_Segment", None)
                setattr(value, "Styling_Segment", self)

class Styling_Segment:

    def __init__(self, Styling_Segment: "Styling_Style" = None, Styling_Segment6: "Styling_Pattern" = None, Styling_Segment9: "Styling_CaseStyle" = None):
        self.Styling_Segment = Styling_Segment
        self.Styling_Segment6 = Styling_Segment6
        self.Styling_Segment9 = Styling_Segment9
        
        pass
    @property
    def Styling_Segment6(self):
        return self.__Styling_Segment6

    @Styling_Segment6.setter
    def Styling_Segment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Segment__Styling_Segment6", None)
        self.__Styling_Segment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Pattern"):
                opp_val = getattr(old_value, "Styling_Pattern", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Pattern"):
                opp_val = getattr(value, "Styling_Pattern", None)
                setattr(value, "Styling_Pattern", self)

    @property
    def Styling_Segment9(self):
        return self.__Styling_Segment9

    @Styling_Segment9.setter
    def Styling_Segment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Segment__Styling_Segment9", None)
        self.__Styling_Segment9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_CaseStyle8"):
                opp_val = getattr(old_value, "Styling_CaseStyle8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_CaseStyle8"):
                opp_val = getattr(value, "Styling_CaseStyle8", None)
                if opp_val is None:
                    setattr(value, "Styling_CaseStyle8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Styling_Segment(self):
        return self.__Styling_Segment

    @Styling_Segment.setter
    def Styling_Segment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Segment__Styling_Segment", None)
        self.__Styling_Segment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Style"):
                opp_val = getattr(old_value, "Styling_Style", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Style"):
                opp_val = getattr(value, "Styling_Style", None)
                setattr(value, "Styling_Style", self)

    def getColor(self) :
        # TODO: Implement getColor method
        pass

    def setColor(self, Styling_color):
        # TODO: Implement setColor method
        pass

    def getFont(self) :
        # TODO: Implement getFont method
        pass

class Styling_IPredicate:

    pass
class CaseStyle:

    pass
class Styling_StylingPredicate(CaseStyle):

    pass
class Styling_Default(CaseStyle):

    pass
class Styling_Pattern(ABC):

    def __init__(self, Styling_Pattern: "Styling_Segment" = None):
        self.Styling_Pattern = Styling_Pattern
        
        pass
    @property
    def Styling_Pattern(self):
        return self.__Styling_Pattern

    @Styling_Pattern.setter
    def Styling_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_Pattern__Styling_Pattern", None)
        self.__Styling_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Segment6"):
                opp_val = getattr(old_value, "Styling_Segment6", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Segment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Segment6"):
                opp_val = getattr(value, "Styling_Segment6", None)
                setattr(value, "Styling_Segment6", self)

    def getPatternValue(self, Styling_object) :
        # TODO: Implement getPatternValue method
        pass

    def getPattern(self) :
        # TODO: Implement getPattern method
        pass

class Styling_CaseStyle(ABC):

    def __init__(self, Styling_CaseStyle: "Styling_StylingModel" = None, Styling_CaseStyle8: set["Styling_Segment"] = None, Styling_CaseStyle11: "Styling_Icon" = None):
        self.Styling_CaseStyle = Styling_CaseStyle
        self.Styling_CaseStyle8 = Styling_CaseStyle8 if Styling_CaseStyle8 is not None else set()
        self.Styling_CaseStyle11 = Styling_CaseStyle11
        
        pass
    @property
    def Styling_CaseStyle8(self):
        return self.__Styling_CaseStyle8

    @Styling_CaseStyle8.setter
    def Styling_CaseStyle8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_CaseStyle__Styling_CaseStyle8", None)
        self.__Styling_CaseStyle8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Styling_Segment9"):
                    opp_val = getattr(item, "Styling_Segment9", None)
                    
                    if opp_val == self:
                        setattr(item, "Styling_Segment9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Styling_Segment9"):
                    opp_val = getattr(item, "Styling_Segment9", None)
                    
                    setattr(item, "Styling_Segment9", self)
                    

    @property
    def Styling_CaseStyle11(self):
        return self.__Styling_CaseStyle11

    @Styling_CaseStyle11.setter
    def Styling_CaseStyle11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_CaseStyle__Styling_CaseStyle11", None)
        self.__Styling_CaseStyle11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Icon"):
                opp_val = getattr(old_value, "Styling_Icon", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Icon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Icon"):
                opp_val = getattr(value, "Styling_Icon", None)
                setattr(value, "Styling_Icon", self)

    @property
    def Styling_CaseStyle(self):
        return self.__Styling_CaseStyle

    @Styling_CaseStyle.setter
    def Styling_CaseStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_CaseStyle__Styling_CaseStyle", None)
        self.__Styling_CaseStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_StylingModel"):
                opp_val = getattr(old_value, "Styling_StylingModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_StylingModel"):
                opp_val = getattr(value, "Styling_StylingModel", None)
                if opp_val is None:
                    setattr(value, "Styling_StylingModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getImage(self) :
        # TODO: Implement getImage method
        pass

    def getStyledString(self, Styling_object) :
        # TODO: Implement getStyledString method
        pass

class Styling_StylingModel:

    def __init__(self, modeName: str, Styling_StylingModel: set["Styling_CaseStyle"] = None, Styling_StylingModel2: "Styling_Default" = None, Styling_StylingModel13: "Styling_Styling" = None):
        self.modeName = modeName
        self.Styling_StylingModel = Styling_StylingModel if Styling_StylingModel is not None else set()
        self.Styling_StylingModel2 = Styling_StylingModel2
        self.Styling_StylingModel13 = Styling_StylingModel13
        
        pass
    @property
    def modeName(self):
        return self.__modeName

    @modeName.setter
    def modeName(self, modeName: str):
        self.__modeName = modeName


    @property
    def Styling_StylingModel13(self):
        return self.__Styling_StylingModel13

    @Styling_StylingModel13.setter
    def Styling_StylingModel13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_StylingModel__Styling_StylingModel13", None)
        self.__Styling_StylingModel13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Styling"):
                opp_val = getattr(old_value, "Styling_Styling", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Styling"):
                opp_val = getattr(value, "Styling_Styling", None)
                if opp_val is None:
                    setattr(value, "Styling_Styling", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Styling_StylingModel(self):
        return self.__Styling_StylingModel

    @Styling_StylingModel.setter
    def Styling_StylingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_StylingModel__Styling_StylingModel", None)
        self.__Styling_StylingModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Styling_CaseStyle"):
                    opp_val = getattr(item, "Styling_CaseStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "Styling_CaseStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Styling_CaseStyle"):
                    opp_val = getattr(item, "Styling_CaseStyle", None)
                    
                    setattr(item, "Styling_CaseStyle", self)
                    

    @property
    def Styling_StylingModel2(self):
        return self.__Styling_StylingModel2

    @Styling_StylingModel2.setter
    def Styling_StylingModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Styling_StylingModel__Styling_StylingModel2", None)
        self.__Styling_StylingModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Styling_Default"):
                opp_val = getattr(old_value, "Styling_Default", None)
                if opp_val == self:
                    setattr(old_value, "Styling_Default", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Styling_Default"):
                opp_val = getattr(value, "Styling_Default", None)
                setattr(value, "Styling_Default", self)

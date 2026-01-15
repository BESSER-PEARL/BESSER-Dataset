from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LayoutType(Enum):
    SINGLE_COLUMN = "SINGLE_COLUMN"
    TWO_COLUMNS = "TWO_COLUMNS"
    LEFT_BAR = "LEFT_BAR"
    RIGHT_BAR = "RIGHT_BAR"
    THREE_COLUMNS = "THREE_COLUMNS"


############################################
# Definition of Classes
############################################

class ContainerView:

    pass
class classLayout2Frontend_InputForm(ContainerView):

    pass
class classLayout2Frontend_IterationContainer(ContainerView):

    pass
class classLayout2Frontend_StaticContainer(ContainerView):

    pass
class classLayout2Frontend_ElementView(ABC):

    def __init__(self, name: str, displayName: str, description: str, classLayout2Frontend_ElementView: "classLayout2Frontend_PageView" = None, classLayout2Frontend_ElementView29: "classLayout2Frontend_ContainerView" = None):
        self.name = name
        self.displayName = displayName
        self.description = description
        self.classLayout2Frontend_ElementView = classLayout2Frontend_ElementView
        self.classLayout2Frontend_ElementView29 = classLayout2Frontend_ElementView29
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classLayout2Frontend_ElementView29(self):
        return self.__classLayout2Frontend_ElementView29

    @classLayout2Frontend_ElementView29.setter
    def classLayout2Frontend_ElementView29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_ElementView__classLayout2Frontend_ElementView29", None)
        self.__classLayout2Frontend_ElementView29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_ContainerView28"):
                opp_val = getattr(old_value, "classLayout2Frontend_ContainerView28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_ContainerView28"):
                opp_val = getattr(value, "classLayout2Frontend_ContainerView28", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_ContainerView28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classLayout2Frontend_ElementView(self):
        return self.__classLayout2Frontend_ElementView

    @classLayout2Frontend_ElementView.setter
    def classLayout2Frontend_ElementView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_ElementView__classLayout2Frontend_ElementView", None)
        self.__classLayout2Frontend_ElementView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_PageView21"):
                opp_val = getattr(old_value, "classLayout2Frontend_PageView21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_PageView21"):
                opp_val = getattr(value, "classLayout2Frontend_PageView21", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_PageView21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Input:

    pass
class classLayout2Frontend_FileUpload(Input):

    pass
class classLayout2Frontend_Selection(Input):

    pass
class classLayout2Frontend_InputText(Input):

    def __init__(self, multiline: bool):
        self.multiline = multiline
        
    @property
    def multiline(self) -> bool:
        return self.__multiline

    @multiline.setter
    def multiline(self, multiline: bool):
        self.__multiline = multiline

class classLayout2Frontend_IterationFilter:

    pass
class AtomicView:

    pass
class classLayout2Frontend_Input(AtomicView):

    def __init__(self, label: str, classLayout2Frontend_Input: "classLayout2Frontend_IterationFilter" = None):
        self.label = label
        self.classLayout2Frontend_Input = classLayout2Frontend_Input
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def classLayout2Frontend_Input(self):
        return self.__classLayout2Frontend_Input

    @classLayout2Frontend_Input.setter
    def classLayout2Frontend_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Input__classLayout2Frontend_Input", None)
        self.__classLayout2Frontend_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_IterationFilter"):
                opp_val = getattr(old_value, "classLayout2Frontend_IterationFilter", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_IterationFilter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_IterationFilter"):
                opp_val = getattr(value, "classLayout2Frontend_IterationFilter", None)
                setattr(value, "classLayout2Frontend_IterationFilter", self)

class classLayout2Frontend_Output(AtomicView):

    pass
class Output:

    pass
class classLayout2Frontend_TextArea(Output):

    def __init__(self, value: str, isTitle: bool):
        self.value = value
        self.isTitle = isTitle
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def isTitle(self) -> bool:
        return self.__isTitle

    @isTitle.setter
    def isTitle(self, isTitle: bool):
        self.__isTitle = isTitle

class classLayout2Frontend_Image(Output):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

class Selection:

    pass
class classLayout2Frontend_Dropdownlist(Selection):

    pass
class classLayout2Frontend_List(Selection):

    def __init__(self, multiple: bool):
        self.multiple = multiple
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

class classLayout2Frontend_CheckList(Selection):

    pass
class classLayout2Frontend_RadioButtonGroup(Selection):

    pass
class classLayout2Frontend_Autocomplete(Selection):

    def __init__(self, multiple: bool):
        self.multiple = multiple
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

class ElementView:

    pass
class classLayout2Frontend_AtomicView(ElementView):

    pass
class PropertyType:

    pass
class classLayout2Frontend_Enumeration(PropertyType):

    pass
class classLayout2Frontend_PrimitiveType(PropertyType):

    pass
class classLayout2Frontend_EntityModelElement(ABC):

    def __init__(self, name: str, description: str, displayName: str, classLayout2Frontend_EntityModelElement: "classLayout2Frontend_EntitiesModel" = None):
        self.name = name
        self.description = description
        self.displayName = displayName
        self.classLayout2Frontend_EntityModelElement = classLayout2Frontend_EntityModelElement
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def classLayout2Frontend_EntityModelElement(self):
        return self.__classLayout2Frontend_EntityModelElement

    @classLayout2Frontend_EntityModelElement.setter
    def classLayout2Frontend_EntityModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_EntityModelElement__classLayout2Frontend_EntityModelElement", None)
        self.__classLayout2Frontend_EntityModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_EntitiesModel10"):
                opp_val = getattr(old_value, "classLayout2Frontend_EntitiesModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_EntitiesModel10"):
                opp_val = getattr(value, "classLayout2Frontend_EntitiesModel10", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_EntitiesModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classLayout2Frontend_SiteView:

    def __init__(self, name: str, templateName: str, templateColor: str, displayName: str, classLayout2Frontend_SiteView: "classLayout2Frontend_Project" = None, classLayout2Frontend_SiteView23: set["classLayout2Frontend_PageView"] = None):
        self.name = name
        self.templateName = templateName
        self.templateColor = templateColor
        self.displayName = displayName
        self.classLayout2Frontend_SiteView = classLayout2Frontend_SiteView
        self.classLayout2Frontend_SiteView23 = classLayout2Frontend_SiteView23 if classLayout2Frontend_SiteView23 is not None else set()
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def templateName(self) -> str:
        return self.__templateName

    @templateName.setter
    def templateName(self, templateName: str):
        self.__templateName = templateName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def templateColor(self) -> str:
        return self.__templateColor

    @templateColor.setter
    def templateColor(self, templateColor: str):
        self.__templateColor = templateColor

    @property
    def classLayout2Frontend_SiteView(self):
        return self.__classLayout2Frontend_SiteView

    @classLayout2Frontend_SiteView.setter
    def classLayout2Frontend_SiteView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_SiteView__classLayout2Frontend_SiteView", None)
        self.__classLayout2Frontend_SiteView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Project2"):
                opp_val = getattr(old_value, "classLayout2Frontend_Project2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Project2"):
                opp_val = getattr(value, "classLayout2Frontend_Project2", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_Project2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classLayout2Frontend_SiteView23(self):
        return self.__classLayout2Frontend_SiteView23

    @classLayout2Frontend_SiteView23.setter
    def classLayout2Frontend_SiteView23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_SiteView__classLayout2Frontend_SiteView23", None)
        self.__classLayout2Frontend_SiteView23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_PageView24"):
                    opp_val = getattr(item, "classLayout2Frontend_PageView24", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_PageView24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_PageView24"):
                    opp_val = getattr(item, "classLayout2Frontend_PageView24", None)
                    
                    setattr(item, "classLayout2Frontend_PageView24", self)
                    

class classLayout2Frontend_EntitiesModel:

    def __init__(self, name: str, classLayout2Frontend_EntitiesModel: "classLayout2Frontend_Project" = None, classLayout2Frontend_EntitiesModel10: set["classLayout2Frontend_EntityModelElement"] = None):
        self.name = name
        self.classLayout2Frontend_EntitiesModel = classLayout2Frontend_EntitiesModel
        self.classLayout2Frontend_EntitiesModel10 = classLayout2Frontend_EntitiesModel10 if classLayout2Frontend_EntitiesModel10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classLayout2Frontend_EntitiesModel(self):
        return self.__classLayout2Frontend_EntitiesModel

    @classLayout2Frontend_EntitiesModel.setter
    def classLayout2Frontend_EntitiesModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_EntitiesModel__classLayout2Frontend_EntitiesModel", None)
        self.__classLayout2Frontend_EntitiesModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Project"):
                opp_val = getattr(old_value, "classLayout2Frontend_Project", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Project"):
                opp_val = getattr(value, "classLayout2Frontend_Project", None)
                setattr(value, "classLayout2Frontend_Project", self)

    @property
    def classLayout2Frontend_EntitiesModel10(self):
        return self.__classLayout2Frontend_EntitiesModel10

    @classLayout2Frontend_EntitiesModel10.setter
    def classLayout2Frontend_EntitiesModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_EntitiesModel__classLayout2Frontend_EntitiesModel10", None)
        self.__classLayout2Frontend_EntitiesModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_EntityModelElement"):
                    opp_val = getattr(item, "classLayout2Frontend_EntityModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_EntityModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_EntityModelElement"):
                    opp_val = getattr(item, "classLayout2Frontend_EntityModelElement", None)
                    
                    setattr(item, "classLayout2Frontend_EntityModelElement", self)
                    

class EntityModelElement:

    pass
class classLayout2Frontend_StructuralFeature(EntityModelElement):

    def __init__(self, required: bool, classLayout2Frontend_StructuralFeature: "classLayout2Frontend_Entity" = None, classLayout2Frontend_StructuralFeature18: "classLayout2Frontend_AtomicView" = None):
        self.required = required
        self.classLayout2Frontend_StructuralFeature = classLayout2Frontend_StructuralFeature
        self.classLayout2Frontend_StructuralFeature18 = classLayout2Frontend_StructuralFeature18
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def classLayout2Frontend_StructuralFeature18(self):
        return self.__classLayout2Frontend_StructuralFeature18

    @classLayout2Frontend_StructuralFeature18.setter
    def classLayout2Frontend_StructuralFeature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_StructuralFeature__classLayout2Frontend_StructuralFeature18", None)
        self.__classLayout2Frontend_StructuralFeature18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_AtomicView"):
                opp_val = getattr(old_value, "classLayout2Frontend_AtomicView", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_AtomicView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_AtomicView"):
                opp_val = getattr(value, "classLayout2Frontend_AtomicView", None)
                setattr(value, "classLayout2Frontend_AtomicView", self)

    @property
    def classLayout2Frontend_StructuralFeature(self):
        return self.__classLayout2Frontend_StructuralFeature

    @classLayout2Frontend_StructuralFeature.setter
    def classLayout2Frontend_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_StructuralFeature__classLayout2Frontend_StructuralFeature", None)
        self.__classLayout2Frontend_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Entity15"):
                opp_val = getattr(old_value, "classLayout2Frontend_Entity15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Entity15"):
                opp_val = getattr(value, "classLayout2Frontend_Entity15", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_Entity15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classLayout2Frontend_Literal(EntityModelElement):

    def __init__(self, value: int, classLayout2Frontend_Literal: "classLayout2Frontend_Enumeration" = None):
        self.value = value
        self.classLayout2Frontend_Literal = classLayout2Frontend_Literal
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def classLayout2Frontend_Literal(self):
        return self.__classLayout2Frontend_Literal

    @classLayout2Frontend_Literal.setter
    def classLayout2Frontend_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Literal__classLayout2Frontend_Literal", None)
        self.__classLayout2Frontend_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Enumeration"):
                opp_val = getattr(old_value, "classLayout2Frontend_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Enumeration"):
                opp_val = getattr(value, "classLayout2Frontend_Enumeration", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classLayout2Frontend_PropertyType(EntityModelElement):

    pass
class classLayout2Frontend_Entity(EntityModelElement):

    def __init__(self, isAbstract: bool, classLayout2Frontend_Entity: "classLayout2Frontend_Association" = None, classLayout2Frontend_Entity13: "classLayout2Frontend_Entity" = None, classLayout2Frontend_Entity11: "classLayout2Frontend_Entity" = None, classLayout2Frontend_Entity15: set["classLayout2Frontend_StructuralFeature"] = None, classLayout2Frontend_Entity32: "classLayout2Frontend_ContainerView" = None):
        self.isAbstract = isAbstract
        self.classLayout2Frontend_Entity = classLayout2Frontend_Entity
        self.classLayout2Frontend_Entity13 = classLayout2Frontend_Entity13
        self.classLayout2Frontend_Entity11 = classLayout2Frontend_Entity11
        self.classLayout2Frontend_Entity15 = classLayout2Frontend_Entity15 if classLayout2Frontend_Entity15 is not None else set()
        self.classLayout2Frontend_Entity32 = classLayout2Frontend_Entity32
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def classLayout2Frontend_Entity11(self):
        return self.__classLayout2Frontend_Entity11

    @classLayout2Frontend_Entity11.setter
    def classLayout2Frontend_Entity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entity__classLayout2Frontend_Entity11", None)
        self.__classLayout2Frontend_Entity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Entity13"):
                opp_val = getattr(old_value, "classLayout2Frontend_Entity13", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_Entity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Entity13"):
                opp_val = getattr(value, "classLayout2Frontend_Entity13", None)
                setattr(value, "classLayout2Frontend_Entity13", self)

    @property
    def classLayout2Frontend_Entity15(self):
        return self.__classLayout2Frontend_Entity15

    @classLayout2Frontend_Entity15.setter
    def classLayout2Frontend_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entity__classLayout2Frontend_Entity15", None)
        self.__classLayout2Frontend_Entity15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_StructuralFeature"):
                    opp_val = getattr(item, "classLayout2Frontend_StructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_StructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_StructuralFeature"):
                    opp_val = getattr(item, "classLayout2Frontend_StructuralFeature", None)
                    
                    setattr(item, "classLayout2Frontend_StructuralFeature", self)
                    

    @property
    def classLayout2Frontend_Entity(self):
        return self.__classLayout2Frontend_Entity

    @classLayout2Frontend_Entity.setter
    def classLayout2Frontend_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entity__classLayout2Frontend_Entity", None)
        self.__classLayout2Frontend_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Association"):
                opp_val = getattr(old_value, "classLayout2Frontend_Association", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Association"):
                opp_val = getattr(value, "classLayout2Frontend_Association", None)
                setattr(value, "classLayout2Frontend_Association", self)

    @property
    def classLayout2Frontend_Entity32(self):
        return self.__classLayout2Frontend_Entity32

    @classLayout2Frontend_Entity32.setter
    def classLayout2Frontend_Entity32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entity__classLayout2Frontend_Entity32", None)
        self.__classLayout2Frontend_Entity32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_ContainerView31"):
                opp_val = getattr(old_value, "classLayout2Frontend_ContainerView31", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_ContainerView31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_ContainerView31"):
                opp_val = getattr(value, "classLayout2Frontend_ContainerView31", None)
                setattr(value, "classLayout2Frontend_ContainerView31", self)

    @property
    def classLayout2Frontend_Entity13(self):
        return self.__classLayout2Frontend_Entity13

    @classLayout2Frontend_Entity13.setter
    def classLayout2Frontend_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entity__classLayout2Frontend_Entity13", None)
        self.__classLayout2Frontend_Entity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Entity11"):
                opp_val = getattr(old_value, "classLayout2Frontend_Entity11", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_Entity11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Entity11"):
                opp_val = getattr(value, "classLayout2Frontend_Entity11", None)
                setattr(value, "classLayout2Frontend_Entity11", self)

class StructuralFeature:

    pass
class classLayout2Frontend_Property(StructuralFeature):

    def __init__(self, defaultValue: str, classLayout2Frontend_Property: "classLayout2Frontend_PropertyType" = None):
        self.defaultValue = defaultValue
        self.classLayout2Frontend_Property = classLayout2Frontend_Property
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def classLayout2Frontend_Property(self):
        return self.__classLayout2Frontend_Property

    @classLayout2Frontend_Property.setter
    def classLayout2Frontend_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Property__classLayout2Frontend_Property", None)
        self.__classLayout2Frontend_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_PropertyType"):
                opp_val = getattr(old_value, "classLayout2Frontend_PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_PropertyType"):
                opp_val = getattr(value, "classLayout2Frontend_PropertyType", None)
                setattr(value, "classLayout2Frontend_PropertyType", self)

class classLayout2Frontend_Association(StructuralFeature):

    def __init__(self, many: bool, classLayout2Frontend_Association: "classLayout2Frontend_Entity" = None):
        self.many = many
        self.classLayout2Frontend_Association = classLayout2Frontend_Association
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def classLayout2Frontend_Association(self):
        return self.__classLayout2Frontend_Association

    @classLayout2Frontend_Association.setter
    def classLayout2Frontend_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Association__classLayout2Frontend_Association", None)
        self.__classLayout2Frontend_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Entity"):
                opp_val = getattr(old_value, "classLayout2Frontend_Entity", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Entity"):
                opp_val = getattr(value, "classLayout2Frontend_Entity", None)
                setattr(value, "classLayout2Frontend_Entity", self)

class Association:

    pass
class classLayout2Frontend_Reference(Association):

    pass
class classLayout2Frontend_Composition(Association):

    pass
class classLayout2Frontend_ContainerView(ElementView):

    pass
class classLayout2Frontend_PageView:

    def __init__(self, layoutType: str, name: str, classLayout2Frontend_PageView: "classLayout2Frontend_Project" = None, classLayout2Frontend_PageView21: set["classLayout2Frontend_ElementView"] = None, classLayout2Frontend_PageView24: "classLayout2Frontend_SiteView" = None):
        self.layoutType = layoutType
        self.name = name
        self.classLayout2Frontend_PageView = classLayout2Frontend_PageView
        self.classLayout2Frontend_PageView21 = classLayout2Frontend_PageView21 if classLayout2Frontend_PageView21 is not None else set()
        self.classLayout2Frontend_PageView24 = classLayout2Frontend_PageView24
        
    @property
    def layoutType(self) -> str:
        return self.__layoutType

    @layoutType.setter
    def layoutType(self, layoutType: str):
        self.__layoutType = layoutType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classLayout2Frontend_PageView21(self):
        return self.__classLayout2Frontend_PageView21

    @classLayout2Frontend_PageView21.setter
    def classLayout2Frontend_PageView21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_PageView__classLayout2Frontend_PageView21", None)
        self.__classLayout2Frontend_PageView21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_ElementView"):
                    opp_val = getattr(item, "classLayout2Frontend_ElementView", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_ElementView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_ElementView"):
                    opp_val = getattr(item, "classLayout2Frontend_ElementView", None)
                    
                    setattr(item, "classLayout2Frontend_ElementView", self)
                    

    @property
    def classLayout2Frontend_PageView(self):
        return self.__classLayout2Frontend_PageView

    @classLayout2Frontend_PageView.setter
    def classLayout2Frontend_PageView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_PageView__classLayout2Frontend_PageView", None)
        self.__classLayout2Frontend_PageView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_Project4"):
                opp_val = getattr(old_value, "classLayout2Frontend_Project4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_Project4"):
                opp_val = getattr(value, "classLayout2Frontend_Project4", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_Project4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classLayout2Frontend_PageView24(self):
        return self.__classLayout2Frontend_PageView24

    @classLayout2Frontend_PageView24.setter
    def classLayout2Frontend_PageView24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_PageView__classLayout2Frontend_PageView24", None)
        self.__classLayout2Frontend_PageView24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_SiteView23"):
                opp_val = getattr(old_value, "classLayout2Frontend_SiteView23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_SiteView23"):
                opp_val = getattr(value, "classLayout2Frontend_SiteView23", None)
                if opp_val is None:
                    setattr(value, "classLayout2Frontend_SiteView23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classLayout2Frontend_Project:

    def __init__(self, name: str, classLayout2Frontend_Project2: set["classLayout2Frontend_SiteView"] = None, classLayout2Frontend_Project4: set["classLayout2Frontend_PageView"] = None, classLayout2Frontend_Project6: set["classLayout2Frontend_ContainerView"] = None, classLayout2Frontend_Project: "classLayout2Frontend_EntitiesModel" = None):
        self.name = name
        self.classLayout2Frontend_Project2 = classLayout2Frontend_Project2 if classLayout2Frontend_Project2 is not None else set()
        self.classLayout2Frontend_Project4 = classLayout2Frontend_Project4 if classLayout2Frontend_Project4 is not None else set()
        self.classLayout2Frontend_Project6 = classLayout2Frontend_Project6 if classLayout2Frontend_Project6 is not None else set()
        self.classLayout2Frontend_Project = classLayout2Frontend_Project
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classLayout2Frontend_Project6(self):
        return self.__classLayout2Frontend_Project6

    @classLayout2Frontend_Project6.setter
    def classLayout2Frontend_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Project__classLayout2Frontend_Project6", None)
        self.__classLayout2Frontend_Project6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_ContainerView"):
                    opp_val = getattr(item, "classLayout2Frontend_ContainerView", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_ContainerView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_ContainerView"):
                    opp_val = getattr(item, "classLayout2Frontend_ContainerView", None)
                    
                    setattr(item, "classLayout2Frontend_ContainerView", self)
                    

    @property
    def classLayout2Frontend_Project(self):
        return self.__classLayout2Frontend_Project

    @classLayout2Frontend_Project.setter
    def classLayout2Frontend_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Project__classLayout2Frontend_Project", None)
        self.__classLayout2Frontend_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classLayout2Frontend_EntitiesModel"):
                opp_val = getattr(old_value, "classLayout2Frontend_EntitiesModel", None)
                if opp_val == self:
                    setattr(old_value, "classLayout2Frontend_EntitiesModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classLayout2Frontend_EntitiesModel"):
                opp_val = getattr(value, "classLayout2Frontend_EntitiesModel", None)
                setattr(value, "classLayout2Frontend_EntitiesModel", self)

    @property
    def classLayout2Frontend_Project4(self):
        return self.__classLayout2Frontend_Project4

    @classLayout2Frontend_Project4.setter
    def classLayout2Frontend_Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Project__classLayout2Frontend_Project4", None)
        self.__classLayout2Frontend_Project4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_PageView"):
                    opp_val = getattr(item, "classLayout2Frontend_PageView", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_PageView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_PageView"):
                    opp_val = getattr(item, "classLayout2Frontend_PageView", None)
                    
                    setattr(item, "classLayout2Frontend_PageView", self)
                    

    @property
    def classLayout2Frontend_Project2(self):
        return self.__classLayout2Frontend_Project2

    @classLayout2Frontend_Project2.setter
    def classLayout2Frontend_Project2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Project__classLayout2Frontend_Project2", None)
        self.__classLayout2Frontend_Project2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classLayout2Frontend_SiteView"):
                    opp_val = getattr(item, "classLayout2Frontend_SiteView", None)
                    
                    if opp_val == self:
                        setattr(item, "classLayout2Frontend_SiteView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classLayout2Frontend_SiteView"):
                    opp_val = getattr(item, "classLayout2Frontend_SiteView", None)
                    
                    setattr(item, "classLayout2Frontend_SiteView", self)
                    

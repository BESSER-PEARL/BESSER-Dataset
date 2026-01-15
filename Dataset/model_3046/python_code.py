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

class classLayout2Frontend_Views_PageView:

    def __init__(self, name: str, layoutType: str, classLayout2Frontend_Views_PageView: set["ElementView"] = None):
        self.name = name
        self.layoutType = layoutType
        self.classLayout2Frontend_Views_PageView = classLayout2Frontend_Views_PageView if classLayout2Frontend_Views_PageView is not None else set()
        
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
    def classLayout2Frontend_Views_PageView(self):
        return self.__classLayout2Frontend_Views_PageView

    @classLayout2Frontend_Views_PageView.setter
    def classLayout2Frontend_Views_PageView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Views_PageView__classLayout2Frontend_Views_PageView", None)
        self.__classLayout2Frontend_Views_PageView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementView25"):
                    opp_val = getattr(item, "ElementView25", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementView25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementView25"):
                    opp_val = getattr(item, "ElementView25", None)
                    
                    setattr(item, "ElementView25", self)
                    

class Output:

    pass
class classLayout2Frontend_Views_Image(Output):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

class classLayout2Frontend_Views_TextArea(Output):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Input:

    pass
class classLayout2Frontend_Views_Selection(Input):

    pass
class classLayout2Frontend_Views_FileUpload(Input):

    pass
class classLayout2Frontend_Views_InputText(Input):

    def __init__(self, multiline: bool, Input: "classLayout2Frontend_Views_IterationFilter"):
        self.multiline = multiline
        
    @property
    def multiline(self) -> bool:
        return self.__multiline

    @multiline.setter
    def multiline(self, multiline: bool):
        self.__multiline = multiline

class Selection:

    pass
class classLayout2Frontend_Views_RadioButtonGroup(Selection):

    pass
class classLayout2Frontend_Views_Autocomplete(Selection):

    def __init__(self, multiple: bool):
        self.multiple = multiple
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

class classLayout2Frontend_Views_List(Selection):

    def __init__(self, multiple: bool):
        self.multiple = multiple
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

class classLayout2Frontend_Views_CheckList(Selection):

    pass
class classLayout2Frontend_Views_Dropdownlist(Selection):

    pass
class classLayout2Frontend_Views_IterationFilter:

    pass
class classLayout2Frontend_Views_ElementView(ABC):

    def __init__(self, name: str, dsisplayName: str, description: str):
        self.name = name
        self.dsisplayName = dsisplayName
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsisplayName(self) -> str:
        return self.__dsisplayName

    @dsisplayName.setter
    def dsisplayName(self, dsisplayName: str):
        self.__dsisplayName = dsisplayName

class ElementView:

    pass
class classLayout2Frontend_Views_AtomicView(ElementView):

    pass
class classLayout2Frontend_Views_ContainerView(ElementView):

    pass
class AtomicView:

    pass
class classLayout2Frontend_Views_Output(AtomicView):

    pass
class classLayout2Frontend_Views_Input(AtomicView):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class IterationFilter:

    pass
class Literal:

    pass
class PropertyType:

    pass
class classLayout2Frontend_Entities_Enumeration(PropertyType):

    pass
class classLayout2Frontend_Entities_PrimitiveType(PropertyType):

    pass
class classLayout2Frontend_Views_SiteView:

    def __init__(self, name: str, templateName: str, templateColor: str, displayName: str, classLayout2Frontend_Views_SiteView: set["PageView"] = None):
        self.name = name
        self.templateName = templateName
        self.templateColor = templateColor
        self.displayName = displayName
        self.classLayout2Frontend_Views_SiteView = classLayout2Frontend_Views_SiteView if classLayout2Frontend_Views_SiteView is not None else set()
        
    @property
    def templateColor(self) -> str:
        return self.__templateColor

    @templateColor.setter
    def templateColor(self, templateColor: str):
        self.__templateColor = templateColor

    @property
    def templateName(self) -> str:
        return self.__templateName

    @templateName.setter
    def templateName(self, templateName: str):
        self.__templateName = templateName

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
    def classLayout2Frontend_Views_SiteView(self):
        return self.__classLayout2Frontend_Views_SiteView

    @classLayout2Frontend_Views_SiteView.setter
    def classLayout2Frontend_Views_SiteView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Views_SiteView__classLayout2Frontend_Views_SiteView", None)
        self.__classLayout2Frontend_Views_SiteView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PageView16"):
                    opp_val = getattr(item, "PageView16", None)
                    
                    if opp_val == self:
                        setattr(item, "PageView16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageView16"):
                    opp_val = getattr(item, "PageView16", None)
                    
                    setattr(item, "PageView16", self)
                    

class StructuralFeature:

    pass
class classLayout2Frontend_Entities_Property(StructuralFeature):

    def __init__(self, defaultValue: str, classLayout2Frontend_Entities_Property: "PropertyType" = None, StructuralFeature: "classLayout2Frontend_Entities_Entity", StructuralFeature22: "classLayout2Frontend_Views_AtomicView"):
        self.defaultValue = defaultValue
        self.classLayout2Frontend_Entities_Property = classLayout2Frontend_Entities_Property
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def classLayout2Frontend_Entities_Property(self):
        return self.__classLayout2Frontend_Entities_Property

    @classLayout2Frontend_Entities_Property.setter
    def classLayout2Frontend_Entities_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entities_Property__classLayout2Frontend_Entities_Property", None)
        self.__classLayout2Frontend_Entities_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PropertyType"):
                opp_val = getattr(old_value, "PropertyType", None)
                if opp_val == self:
                    setattr(old_value, "PropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PropertyType"):
                opp_val = getattr(value, "PropertyType", None)
                setattr(value, "PropertyType", self)

class classLayout2Frontend_Entities_Association(StructuralFeature):

    def __init__(self, many: bool, classLayout2Frontend_Entities_Association: "Entity" = None, StructuralFeature: "classLayout2Frontend_Entities_Entity", StructuralFeature22: "classLayout2Frontend_Views_AtomicView"):
        self.many = many
        self.classLayout2Frontend_Entities_Association = classLayout2Frontend_Entities_Association
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def classLayout2Frontend_Entities_Association(self):
        return self.__classLayout2Frontend_Entities_Association

    @classLayout2Frontend_Entities_Association.setter
    def classLayout2Frontend_Entities_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entities_Association__classLayout2Frontend_Entities_Association", None)
        self.__classLayout2Frontend_Entities_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

class classLayout2Frontend_Entities_EntityModelElement(ABC):

    def __init__(self, name: str, description: str, displayName: str):
        self.name = name
        self.description = description
        self.displayName = displayName
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

class EntityModelElement:

    pass
class classLayout2Frontend_Entities_StructuralFeature(EntityModelElement):

    def __init__(self, required: bool, EntityModelElement: "classLayout2Frontend_Entities_EntitiesModel"):
        self.required = required
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

class classLayout2Frontend_Entities_Literal(EntityModelElement):

    def __init__(self, value: int, EntityModelElement: "classLayout2Frontend_Entities_EntitiesModel"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class classLayout2Frontend_Entities_PropertyType(EntityModelElement):

    pass
class classLayout2Frontend_Entities_EntitiesModel:

    def __init__(self, name: str, classLayout2Frontend_Entities_EntitiesModel: set["EntityModelElement"] = None):
        self.name = name
        self.classLayout2Frontend_Entities_EntitiesModel = classLayout2Frontend_Entities_EntitiesModel if classLayout2Frontend_Entities_EntitiesModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classLayout2Frontend_Entities_EntitiesModel(self):
        return self.__classLayout2Frontend_Entities_EntitiesModel

    @classLayout2Frontend_Entities_EntitiesModel.setter
    def classLayout2Frontend_Entities_EntitiesModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entities_EntitiesModel__classLayout2Frontend_Entities_EntitiesModel", None)
        self.__classLayout2Frontend_Entities_EntitiesModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityModelElement"):
                    opp_val = getattr(item, "EntityModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityModelElement"):
                    opp_val = getattr(item, "EntityModelElement", None)
                    
                    setattr(item, "EntityModelElement", self)
                    

class ContainerView:

    pass
class classLayout2Frontend_Views_InputForm(ContainerView):

    pass
class classLayout2Frontend_Views_StaticContainer(ContainerView):

    pass
class classLayout2Frontend_Views_IterationContainer(ContainerView):

    pass
class classLayout2Frontend_Entities_Entity(EntityModelElement):

    def __init__(self, isAbstract: bool, classLayout2Frontend_Entities_Entity: "Entity" = None, classLayout2Frontend_Entities_Entity12: set["StructuralFeature"] = None, EntityModelElement: "classLayout2Frontend_Entities_EntitiesModel"):
        self.isAbstract = isAbstract
        self.classLayout2Frontend_Entities_Entity = classLayout2Frontend_Entities_Entity
        self.classLayout2Frontend_Entities_Entity12 = classLayout2Frontend_Entities_Entity12 if classLayout2Frontend_Entities_Entity12 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def classLayout2Frontend_Entities_Entity(self):
        return self.__classLayout2Frontend_Entities_Entity

    @classLayout2Frontend_Entities_Entity.setter
    def classLayout2Frontend_Entities_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entities_Entity__classLayout2Frontend_Entities_Entity", None)
        self.__classLayout2Frontend_Entities_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity10"):
                opp_val = getattr(old_value, "Entity10", None)
                if opp_val == self:
                    setattr(old_value, "Entity10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity10"):
                opp_val = getattr(value, "Entity10", None)
                setattr(value, "Entity10", self)

    @property
    def classLayout2Frontend_Entities_Entity12(self):
        return self.__classLayout2Frontend_Entities_Entity12

    @classLayout2Frontend_Entities_Entity12.setter
    def classLayout2Frontend_Entities_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classLayout2Frontend_Entities_Entity__classLayout2Frontend_Entities_Entity12", None)
        self.__classLayout2Frontend_Entities_Entity12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralFeature"):
                    opp_val = getattr(item, "StructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralFeature"):
                    opp_val = getattr(item, "StructuralFeature", None)
                    
                    setattr(item, "StructuralFeature", self)
                    

class Association:

    pass
class classLayout2Frontend_Entities_Reference(Association):

    pass
class classLayout2Frontend_Entities_Composition(Association):

    pass
class Entity:

    pass
class PageView:

    pass
class SiteView:

    pass
class EntitiesModel:

    pass
class classLayout2Frontend_Project:

    def __init__(self, name: str, classLayout2Frontend_Project: "EntitiesModel" = None, classLayout2Frontend_Project2: set["SiteView"] = None, classLayout2Frontend_Project4: set["PageView"] = None, classLayout2Frontend_Project6: set["ContainerView"] = None):
        self.name = name
        self.classLayout2Frontend_Project = classLayout2Frontend_Project
        self.classLayout2Frontend_Project2 = classLayout2Frontend_Project2 if classLayout2Frontend_Project2 is not None else set()
        self.classLayout2Frontend_Project4 = classLayout2Frontend_Project4 if classLayout2Frontend_Project4 is not None else set()
        self.classLayout2Frontend_Project6 = classLayout2Frontend_Project6 if classLayout2Frontend_Project6 is not None else set()
        
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
                if hasattr(item, "ContainerView"):
                    opp_val = getattr(item, "ContainerView", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerView"):
                    opp_val = getattr(item, "ContainerView", None)
                    
                    setattr(item, "ContainerView", self)
                    

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
                if hasattr(item, "SiteView"):
                    opp_val = getattr(item, "SiteView", None)
                    
                    if opp_val == self:
                        setattr(item, "SiteView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SiteView"):
                    opp_val = getattr(item, "SiteView", None)
                    
                    setattr(item, "SiteView", self)
                    

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
            if hasattr(old_value, "EntitiesModel"):
                opp_val = getattr(old_value, "EntitiesModel", None)
                if opp_val == self:
                    setattr(old_value, "EntitiesModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntitiesModel"):
                opp_val = getattr(value, "EntitiesModel", None)
                setattr(value, "EntitiesModel", self)

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
                if hasattr(item, "PageView"):
                    opp_val = getattr(item, "PageView", None)
                    
                    if opp_val == self:
                        setattr(item, "PageView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageView"):
                    opp_val = getattr(item, "PageView", None)
                    
                    setattr(item, "PageView", self)
                    

from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Cardinality(Enum):
    Optional = "Optional"
    Required = "Required"
    Many = "Many"
class AuthenticationKeyTypes(Enum):
    Email = "Email"
    ScreenName = "ScreenName"
    Username = "Username"
class DateDetails(Enum):
    DateOnly = "DateOnly"
    TimeOnly = "TimeOnly"
    DateAndTime = "DateAndTime"
class AjaxTechnologies(Enum):
    None = "None"
    jQuery = "jQuery"
    AngularJS = "AngularJS"
class InputTechnologies(Enum):
    Html = "Html"
    jQueryUI = "jQueryUI"
class OperationResultTypes(Enum):
    None = "None"
    File = "File"
class PageTopMenuOptions(Enum):
    NeverInclude = "NeverInclude"
    AlwaysInclude = "AlwaysInclude"
    IncludeWhenAuthenticated = "IncludeWhenAuthenticated"
class CollectionDisplayOptions(Enum):
    LineDirection = "LineDirection"
    PageDirection = "PageDirection"
class FrameworkTechnologies(Enum):
    JSF = "JSF"
    CakePHP = "CakePHP"
    CodeIgniter = "CodeIgniter"
    Kohana = "Kohana"
    Laravel = "Laravel"
    Symfony = "Symfony"
class OrmTechnologies(Enum):
    JPA = "JPA"
    DataMapper = "DataMapper"
    Idiorm = "Idiorm"
    Kohana = "Kohana"
    DoctrineORM = "DoctrineORM"
    DoctrineODM = "DoctrineODM"
class isHasChoices(Enum):
    isA = "isA"
    hasA = "hasA"
class DatabaseTechnologies(Enum):
    MySql = "MySql"
    Oracle = "Oracle"
class IndexDisplayOption(Enum):
    Grid = "Grid"
    PageDirection = "PageDirection"
    LineDirection = "LineDirection"


############################################
# Definition of Classes
############################################

class InlineAction:

    pass
class website_SelectAction(InlineAction):

    pass
class Path:

    pass
class website_ParameterReference(Path):

    def __init__(self, name: str, website_ParameterReference: "website_SelectionParameter" = None):
        self.name = name
        self.website_ParameterReference = website_ParameterReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_ParameterReference(self):
        return self.__website_ParameterReference

    @website_ParameterReference.setter
    def website_ParameterReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ParameterReference__website_ParameterReference", None)
        self.__website_ParameterReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_SelectionParameter293"):
                opp_val = getattr(old_value, "website_SelectionParameter293", None)
                if opp_val == self:
                    setattr(old_value, "website_SelectionParameter293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_SelectionParameter293"):
                opp_val = getattr(value, "website_SelectionParameter293", None)
                setattr(value, "website_SelectionParameter293", self)

class website_RouteParameterReference(Path):

    def __init__(self, name: str, website_RouteParameterReference: "website_Attribute" = None):
        self.name = name
        self.website_RouteParameterReference = website_RouteParameterReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_RouteParameterReference(self):
        return self.__website_RouteParameterReference

    @website_RouteParameterReference.setter
    def website_RouteParameterReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_RouteParameterReference__website_RouteParameterReference", None)
        self.__website_RouteParameterReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute291"):
                opp_val = getattr(old_value, "website_Attribute291", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute291"):
                opp_val = getattr(value, "website_Attribute291", None)
                setattr(value, "website_Attribute291", self)

class website_CurrentUserReference(Path):

    pass
class website_FeatureReference(Path):

    def __init__(self, name: str, website_FeatureReference: "website_Feature" = None):
        self.name = name
        self.website_FeatureReference = website_FeatureReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_FeatureReference(self):
        return self.__website_FeatureReference

    @website_FeatureReference.setter
    def website_FeatureReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FeatureReference__website_FeatureReference", None)
        self.__website_FeatureReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Feature289"):
                opp_val = getattr(old_value, "website_Feature289", None)
                if opp_val == self:
                    setattr(old_value, "website_Feature289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Feature289"):
                opp_val = getattr(value, "website_Feature289", None)
                setattr(value, "website_Feature289", self)

class website_ModelReference(Path):

    pass
class website_FeatureSupportAction(InlineAction):

    def __init__(self, confirmMessage: str, uriElement: str, fileExtension: str, website_FeatureSupportAction: "website_BusinessOperation" = None):
        self.confirmMessage = confirmMessage
        self.uriElement = uriElement
        self.fileExtension = fileExtension
        self.website_FeatureSupportAction = website_FeatureSupportAction
        
    @property
    def fileExtension(self) -> str:
        return self.__fileExtension

    @fileExtension.setter
    def fileExtension(self, fileExtension: str):
        self.__fileExtension = fileExtension

    @property
    def uriElement(self) -> str:
        return self.__uriElement

    @uriElement.setter
    def uriElement(self, uriElement: str):
        self.__uriElement = uriElement

    @property
    def confirmMessage(self) -> str:
        return self.__confirmMessage

    @confirmMessage.setter
    def confirmMessage(self, confirmMessage: str):
        self.__confirmMessage = confirmMessage

    @property
    def website_FeatureSupportAction(self):
        return self.__website_FeatureSupportAction

    @website_FeatureSupportAction.setter
    def website_FeatureSupportAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FeatureSupportAction__website_FeatureSupportAction", None)
        self.__website_FeatureSupportAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_BusinessOperation285"):
                opp_val = getattr(old_value, "website_BusinessOperation285", None)
                if opp_val == self:
                    setattr(old_value, "website_BusinessOperation285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_BusinessOperation285"):
                opp_val = getattr(value, "website_BusinessOperation285", None)
                setattr(value, "website_BusinessOperation285", self)

class website_DeleteAction(InlineAction):

    def __init__(self, confirmMessage: str, uriElement: str, website_DeleteAction: "website_Page" = None):
        self.confirmMessage = confirmMessage
        self.uriElement = uriElement
        self.website_DeleteAction = website_DeleteAction
        
    @property
    def confirmMessage(self) -> str:
        return self.__confirmMessage

    @confirmMessage.setter
    def confirmMessage(self, confirmMessage: str):
        self.__confirmMessage = confirmMessage

    @property
    def uriElement(self) -> str:
        return self.__uriElement

    @uriElement.setter
    def uriElement(self, uriElement: str):
        self.__uriElement = uriElement

    @property
    def website_DeleteAction(self):
        return self.__website_DeleteAction

    @website_DeleteAction.setter
    def website_DeleteAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DeleteAction__website_DeleteAction", None)
        self.__website_DeleteAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Page283"):
                opp_val = getattr(old_value, "website_Page283", None)
                if opp_val == self:
                    setattr(old_value, "website_Page283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Page283"):
                opp_val = getattr(value, "website_Page283", None)
                setattr(value, "website_Page283", self)

class website_InlineActionContainer(ABC):

    pass
class AuthenticationUnit:

    pass
class website_AuthenticationUnit(ABC):

    pass
class ImageUnit:

    pass
class website_SliderUnit(ImageUnit):

    def __init__(self, styleClass: str, contentClass: str):
        self.styleClass = styleClass
        self.contentClass = contentClass
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

class website_GalleryUnit(ImageUnit):

    def __init__(self, styleClass: str, contentClass: str, website_GalleryUnit: "website_ImageManipulation" = None):
        self.styleClass = styleClass
        self.contentClass = contentClass
        self.website_GalleryUnit = website_GalleryUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def website_GalleryUnit(self):
        return self.__website_GalleryUnit

    @website_GalleryUnit.setter
    def website_GalleryUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_GalleryUnit__website_GalleryUnit", None)
        self.__website_GalleryUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ImageManipulation271"):
                opp_val = getattr(old_value, "website_ImageManipulation271", None)
                if opp_val == self:
                    setattr(old_value, "website_ImageManipulation271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ImageManipulation271"):
                opp_val = getattr(value, "website_ImageManipulation271", None)
                setattr(value, "website_ImageManipulation271", self)

class ChildPath:

    pass
class website_ChildPathAttribute(ChildPath):

    def __init__(self, name: str, website_ChildPathAttribute: "website_Attribute" = None):
        self.name = name
        self.website_ChildPathAttribute = website_ChildPathAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_ChildPathAttribute(self):
        return self.__website_ChildPathAttribute

    @website_ChildPathAttribute.setter
    def website_ChildPathAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ChildPathAttribute__website_ChildPathAttribute", None)
        self.__website_ChildPathAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute264"):
                opp_val = getattr(old_value, "website_Attribute264", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute264"):
                opp_val = getattr(value, "website_Attribute264", None)
                setattr(value, "website_Attribute264", self)

class CollectionUnit:

    pass
class FeaturePath:

    pass
class website_FeaturePathAttribute(FeaturePath):

    def __init__(self, name: str, website_FeaturePathAttribute: "website_Attribute" = None):
        self.name = name
        self.website_FeaturePathAttribute = website_FeaturePathAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_FeaturePathAttribute(self):
        return self.__website_FeaturePathAttribute

    @website_FeaturePathAttribute.setter
    def website_FeaturePathAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FeaturePathAttribute__website_FeaturePathAttribute", None)
        self.__website_FeaturePathAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute256"):
                opp_val = getattr(old_value, "website_Attribute256", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute256"):
                opp_val = getattr(value, "website_Attribute256", None)
                setattr(value, "website_Attribute256", self)

class website_FeaturePath(ABC):

    pass
class ControlUnit:

    pass
class website_SearchUnit(ControlUnit):

    def __init__(self, styleClass: str, website_SearchUnit: "website_IndexUnit" = None):
        self.styleClass = styleClass
        self.website_SearchUnit = website_SearchUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def website_SearchUnit(self):
        return self.__website_SearchUnit

    @website_SearchUnit.setter
    def website_SearchUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_SearchUnit__website_SearchUnit", None)
        self.__website_SearchUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_IndexUnit"):
                opp_val = getattr(old_value, "website_IndexUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_IndexUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_IndexUnit"):
                opp_val = getattr(value, "website_IndexUnit", None)
                setattr(value, "website_IndexUnit", self)

class EditUnit:

    pass
class website_CreateUnit(EditUnit):

    def __init__(self, styleClass: str):
        self.styleClass = styleClass
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

class DataUnit:

    pass
class website_SingletonUnit(ABC):

    pass
class website_SelectableUnit(ABC):

    pass
class SingletonUnit:

    pass
class DynamicUnit:

    pass
class website_ControlUnit(DynamicUnit):

    def __init__(self, contentClass: str, submitLabel: str, cancelLabel: str, website_ControlUnit: "website_Page" = None):
        self.contentClass = contentClass
        self.submitLabel = submitLabel
        self.cancelLabel = cancelLabel
        self.website_ControlUnit = website_ControlUnit
        
    @property
    def cancelLabel(self) -> str:
        return self.__cancelLabel

    @cancelLabel.setter
    def cancelLabel(self, cancelLabel: str):
        self.__cancelLabel = cancelLabel

    @property
    def submitLabel(self) -> str:
        return self.__submitLabel

    @submitLabel.setter
    def submitLabel(self, submitLabel: str):
        self.__submitLabel = submitLabel

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def website_ControlUnit(self):
        return self.__website_ControlUnit

    @website_ControlUnit.setter
    def website_ControlUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ControlUnit__website_ControlUnit", None)
        self.__website_ControlUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Page243"):
                opp_val = getattr(old_value, "website_Page243", None)
                if opp_val == self:
                    setattr(old_value, "website_Page243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Page243"):
                opp_val = getattr(value, "website_Page243", None)
                setattr(value, "website_Page243", self)

class website_DataUnit(DynamicUnit):

    pass
class website_ImageUnit(DynamicUnit, CollectionUnit):

    def __init__(self, missingImagePath: str, showTime: int, transitionTime: int, website_ImageUnit: "website_Selection" = None, website_ImageUnit248: "website_FeaturePath" = None, website_ImageUnit250: "website_FeaturePath" = None, website_ImageUnit253: "website_ImageManipulation" = None):
        self.missingImagePath = missingImagePath
        self.showTime = showTime
        self.transitionTime = transitionTime
        self.website_ImageUnit = website_ImageUnit
        self.website_ImageUnit248 = website_ImageUnit248
        self.website_ImageUnit250 = website_ImageUnit250
        self.website_ImageUnit253 = website_ImageUnit253
        
    @property
    def missingImagePath(self) -> str:
        return self.__missingImagePath

    @missingImagePath.setter
    def missingImagePath(self, missingImagePath: str):
        self.__missingImagePath = missingImagePath

    @property
    def transitionTime(self) -> int:
        return self.__transitionTime

    @transitionTime.setter
    def transitionTime(self, transitionTime: int):
        self.__transitionTime = transitionTime

    @property
    def showTime(self) -> int:
        return self.__showTime

    @showTime.setter
    def showTime(self, showTime: int):
        self.__showTime = showTime

    @property
    def website_ImageUnit250(self):
        return self.__website_ImageUnit250

    @website_ImageUnit250.setter
    def website_ImageUnit250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageUnit__website_ImageUnit250", None)
        self.__website_ImageUnit250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeaturePath251"):
                opp_val = getattr(old_value, "website_FeaturePath251", None)
                if opp_val == self:
                    setattr(old_value, "website_FeaturePath251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeaturePath251"):
                opp_val = getattr(value, "website_FeaturePath251", None)
                setattr(value, "website_FeaturePath251", self)

    @property
    def website_ImageUnit248(self):
        return self.__website_ImageUnit248

    @website_ImageUnit248.setter
    def website_ImageUnit248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageUnit__website_ImageUnit248", None)
        self.__website_ImageUnit248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeaturePath"):
                opp_val = getattr(old_value, "website_FeaturePath", None)
                if opp_val == self:
                    setattr(old_value, "website_FeaturePath", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeaturePath"):
                opp_val = getattr(value, "website_FeaturePath", None)
                setattr(value, "website_FeaturePath", self)

    @property
    def website_ImageUnit(self):
        return self.__website_ImageUnit

    @website_ImageUnit.setter
    def website_ImageUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageUnit__website_ImageUnit", None)
        self.__website_ImageUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection246"):
                opp_val = getattr(old_value, "website_Selection246", None)
                if opp_val == self:
                    setattr(old_value, "website_Selection246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection246"):
                opp_val = getattr(value, "website_Selection246", None)
                setattr(value, "website_Selection246", self)

    @property
    def website_ImageUnit253(self):
        return self.__website_ImageUnit253

    @website_ImageUnit253.setter
    def website_ImageUnit253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageUnit__website_ImageUnit253", None)
        self.__website_ImageUnit253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ImageManipulation254"):
                opp_val = getattr(old_value, "website_ImageManipulation254", None)
                if opp_val == self:
                    setattr(old_value, "website_ImageManipulation254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ImageManipulation254"):
                opp_val = getattr(value, "website_ImageManipulation254", None)
                setattr(value, "website_ImageManipulation254", self)

class website_EditUnit(SingletonUnit, DynamicUnit):

    def __init__(self, confirmLabel: str, cancelLabel: str, contentClass: str, customiseValues: bool, website_EditUnit: "website_Selection" = None, website_EditUnit222: "website_Label" = None, website_EditUnit225: "website_Predicate" = None, website_EditUnit228: "website_Page" = None, website_EditUnit231: "website_Page" = None):
        self.confirmLabel = confirmLabel
        self.cancelLabel = cancelLabel
        self.contentClass = contentClass
        self.customiseValues = customiseValues
        self.website_EditUnit = website_EditUnit
        self.website_EditUnit222 = website_EditUnit222
        self.website_EditUnit225 = website_EditUnit225
        self.website_EditUnit228 = website_EditUnit228
        self.website_EditUnit231 = website_EditUnit231
        
    @property
    def confirmLabel(self) -> str:
        return self.__confirmLabel

    @confirmLabel.setter
    def confirmLabel(self, confirmLabel: str):
        self.__confirmLabel = confirmLabel

    @property
    def customiseValues(self) -> bool:
        return self.__customiseValues

    @customiseValues.setter
    def customiseValues(self, customiseValues: bool):
        self.__customiseValues = customiseValues

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def cancelLabel(self) -> str:
        return self.__cancelLabel

    @cancelLabel.setter
    def cancelLabel(self, cancelLabel: str):
        self.__cancelLabel = cancelLabel

    @property
    def website_EditUnit228(self):
        return self.__website_EditUnit228

    @website_EditUnit228.setter
    def website_EditUnit228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EditUnit__website_EditUnit228", None)
        self.__website_EditUnit228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Page229"):
                opp_val = getattr(old_value, "website_Page229", None)
                if opp_val == self:
                    setattr(old_value, "website_Page229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Page229"):
                opp_val = getattr(value, "website_Page229", None)
                setattr(value, "website_Page229", self)

    @property
    def website_EditUnit231(self):
        return self.__website_EditUnit231

    @website_EditUnit231.setter
    def website_EditUnit231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EditUnit__website_EditUnit231", None)
        self.__website_EditUnit231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Page232"):
                opp_val = getattr(old_value, "website_Page232", None)
                if opp_val == self:
                    setattr(old_value, "website_Page232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Page232"):
                opp_val = getattr(value, "website_Page232", None)
                setattr(value, "website_Page232", self)

    @property
    def website_EditUnit225(self):
        return self.__website_EditUnit225

    @website_EditUnit225.setter
    def website_EditUnit225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EditUnit__website_EditUnit225", None)
        self.__website_EditUnit225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Predicate226"):
                opp_val = getattr(old_value, "website_Predicate226", None)
                if opp_val == self:
                    setattr(old_value, "website_Predicate226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Predicate226"):
                opp_val = getattr(value, "website_Predicate226", None)
                setattr(value, "website_Predicate226", self)

    @property
    def website_EditUnit(self):
        return self.__website_EditUnit

    @website_EditUnit.setter
    def website_EditUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EditUnit__website_EditUnit", None)
        self.__website_EditUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection220"):
                opp_val = getattr(old_value, "website_Selection220", None)
                if opp_val == self:
                    setattr(old_value, "website_Selection220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection220"):
                opp_val = getattr(value, "website_Selection220", None)
                setattr(value, "website_Selection220", self)

    @property
    def website_EditUnit222(self):
        return self.__website_EditUnit222

    @website_EditUnit222.setter
    def website_EditUnit222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EditUnit__website_EditUnit222", None)
        self.__website_EditUnit222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Label223"):
                opp_val = getattr(old_value, "website_Label223", None)
                if opp_val == self:
                    setattr(old_value, "website_Label223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Label223"):
                opp_val = getattr(value, "website_Label223", None)
                setattr(value, "website_Label223", self)

class SelectableUnit:

    pass
class website_DetailsUnit(SingletonUnit, DataUnit, SelectableUnit):

    def __init__(self, onlyDisplayWhenNotEmpty: bool, omitFieldLabels: bool, styleClass: str, contentClass: str):
        self.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty
        self.omitFieldLabels = omitFieldLabels
        self.styleClass = styleClass
        self.contentClass = contentClass
        
    @property
    def omitFieldLabels(self) -> bool:
        return self.__omitFieldLabels

    @omitFieldLabels.setter
    def omitFieldLabels(self, omitFieldLabels: bool):
        self.__omitFieldLabels = omitFieldLabels

    @property
    def onlyDisplayWhenNotEmpty(self) -> bool:
        return self.__onlyDisplayWhenNotEmpty

    @onlyDisplayWhenNotEmpty.setter
    def onlyDisplayWhenNotEmpty(self, onlyDisplayWhenNotEmpty: bool):
        self.__onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty

    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

class website_MapUnit(SelectableUnit, EditUnit):

    def __init__(self, readOnly: bool, defaultZoomLevel: int, styleClass: str, website_MapUnit: "website_LocationAttribute" = None, website_MapUnit235: "website_Attribute" = None):
        self.readOnly = readOnly
        self.defaultZoomLevel = defaultZoomLevel
        self.styleClass = styleClass
        self.website_MapUnit = website_MapUnit
        self.website_MapUnit235 = website_MapUnit235
        
    @property
    def defaultZoomLevel(self) -> int:
        return self.__defaultZoomLevel

    @defaultZoomLevel.setter
    def defaultZoomLevel(self, defaultZoomLevel: int):
        self.__defaultZoomLevel = defaultZoomLevel

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def website_MapUnit(self):
        return self.__website_MapUnit

    @website_MapUnit.setter
    def website_MapUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_MapUnit__website_MapUnit", None)
        self.__website_MapUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LocationAttribute"):
                opp_val = getattr(old_value, "website_LocationAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_LocationAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LocationAttribute"):
                opp_val = getattr(value, "website_LocationAttribute", None)
                setattr(value, "website_LocationAttribute", self)

    @property
    def website_MapUnit235(self):
        return self.__website_MapUnit235

    @website_MapUnit235.setter
    def website_MapUnit235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_MapUnit__website_MapUnit235", None)
        self.__website_MapUnit235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute236"):
                opp_val = getattr(old_value, "website_Attribute236", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute236"):
                opp_val = getattr(value, "website_Attribute236", None)
                setattr(value, "website_Attribute236", self)

class website_CreateUpdateUnit(SelectableUnit, EditUnit):

    def __init__(self, styleClass: str, createUriElement: str, clearLabel: str):
        self.styleClass = styleClass
        self.createUriElement = createUriElement
        self.clearLabel = clearLabel
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def createUriElement(self) -> str:
        return self.__createUriElement

    @createUriElement.setter
    def createUriElement(self, createUriElement: str):
        self.__createUriElement = createUriElement

    @property
    def clearLabel(self) -> str:
        return self.__clearLabel

    @clearLabel.setter
    def clearLabel(self, clearLabel: str):
        self.__clearLabel = clearLabel

class website_CollectionUnit(SelectableUnit):

    def __init__(self, emptyMessage: str, defaultPaginationSize: int, nextNpages: int, previousNpages: int, nextPageLabel: str, previousPageLabel: str, useDisabledPageLinks: bool, useFirstLastPageLinks: bool, firstPageLabel: str, lastPageLabel: str, website_CollectionUnit: set["website_EntityOrView"] = None, website_CollectionUnit208: "website_Feature" = None, website_CollectionUnit211: "website_Selection" = None, website_CollectionUnit214: set["website_Filter"] = None, website_CollectionUnit217: "website_Filter" = None):
        self.emptyMessage = emptyMessage
        self.defaultPaginationSize = defaultPaginationSize
        self.nextNpages = nextNpages
        self.previousNpages = previousNpages
        self.nextPageLabel = nextPageLabel
        self.previousPageLabel = previousPageLabel
        self.useDisabledPageLinks = useDisabledPageLinks
        self.useFirstLastPageLinks = useFirstLastPageLinks
        self.firstPageLabel = firstPageLabel
        self.lastPageLabel = lastPageLabel
        self.website_CollectionUnit = website_CollectionUnit if website_CollectionUnit is not None else set()
        self.website_CollectionUnit208 = website_CollectionUnit208
        self.website_CollectionUnit211 = website_CollectionUnit211
        self.website_CollectionUnit214 = website_CollectionUnit214 if website_CollectionUnit214 is not None else set()
        self.website_CollectionUnit217 = website_CollectionUnit217
        
    @property
    def previousNpages(self) -> int:
        return self.__previousNpages

    @previousNpages.setter
    def previousNpages(self, previousNpages: int):
        self.__previousNpages = previousNpages

    @property
    def useDisabledPageLinks(self) -> bool:
        return self.__useDisabledPageLinks

    @useDisabledPageLinks.setter
    def useDisabledPageLinks(self, useDisabledPageLinks: bool):
        self.__useDisabledPageLinks = useDisabledPageLinks

    @property
    def nextPageLabel(self) -> str:
        return self.__nextPageLabel

    @nextPageLabel.setter
    def nextPageLabel(self, nextPageLabel: str):
        self.__nextPageLabel = nextPageLabel

    @property
    def nextNpages(self) -> int:
        return self.__nextNpages

    @nextNpages.setter
    def nextNpages(self, nextNpages: int):
        self.__nextNpages = nextNpages

    @property
    def useFirstLastPageLinks(self) -> bool:
        return self.__useFirstLastPageLinks

    @useFirstLastPageLinks.setter
    def useFirstLastPageLinks(self, useFirstLastPageLinks: bool):
        self.__useFirstLastPageLinks = useFirstLastPageLinks

    @property
    def firstPageLabel(self) -> str:
        return self.__firstPageLabel

    @firstPageLabel.setter
    def firstPageLabel(self, firstPageLabel: str):
        self.__firstPageLabel = firstPageLabel

    @property
    def previousPageLabel(self) -> str:
        return self.__previousPageLabel

    @previousPageLabel.setter
    def previousPageLabel(self, previousPageLabel: str):
        self.__previousPageLabel = previousPageLabel

    @property
    def lastPageLabel(self) -> str:
        return self.__lastPageLabel

    @lastPageLabel.setter
    def lastPageLabel(self, lastPageLabel: str):
        self.__lastPageLabel = lastPageLabel

    @property
    def defaultPaginationSize(self) -> int:
        return self.__defaultPaginationSize

    @defaultPaginationSize.setter
    def defaultPaginationSize(self, defaultPaginationSize: int):
        self.__defaultPaginationSize = defaultPaginationSize

    @property
    def emptyMessage(self) -> str:
        return self.__emptyMessage

    @emptyMessage.setter
    def emptyMessage(self, emptyMessage: str):
        self.__emptyMessage = emptyMessage

    @property
    def website_CollectionUnit211(self):
        return self.__website_CollectionUnit211

    @website_CollectionUnit211.setter
    def website_CollectionUnit211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_CollectionUnit__website_CollectionUnit211", None)
        self.__website_CollectionUnit211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection212"):
                opp_val = getattr(old_value, "website_Selection212", None)
                if opp_val == self:
                    setattr(old_value, "website_Selection212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection212"):
                opp_val = getattr(value, "website_Selection212", None)
                setattr(value, "website_Selection212", self)

    @property
    def website_CollectionUnit214(self):
        return self.__website_CollectionUnit214

    @website_CollectionUnit214.setter
    def website_CollectionUnit214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_CollectionUnit__website_CollectionUnit214", None)
        self.__website_CollectionUnit214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Filter215"):
                    opp_val = getattr(item, "website_Filter215", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Filter215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Filter215"):
                    opp_val = getattr(item, "website_Filter215", None)
                    
                    setattr(item, "website_Filter215", self)
                    

    @property
    def website_CollectionUnit217(self):
        return self.__website_CollectionUnit217

    @website_CollectionUnit217.setter
    def website_CollectionUnit217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_CollectionUnit__website_CollectionUnit217", None)
        self.__website_CollectionUnit217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Filter218"):
                opp_val = getattr(old_value, "website_Filter218", None)
                if opp_val == self:
                    setattr(old_value, "website_Filter218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Filter218"):
                opp_val = getattr(value, "website_Filter218", None)
                setattr(value, "website_Filter218", self)

    @property
    def website_CollectionUnit(self):
        return self.__website_CollectionUnit

    @website_CollectionUnit.setter
    def website_CollectionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_CollectionUnit__website_CollectionUnit", None)
        self.__website_CollectionUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_EntityOrView206"):
                    opp_val = getattr(item, "website_EntityOrView206", None)
                    
                    if opp_val == self:
                        setattr(item, "website_EntityOrView206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_EntityOrView206"):
                    opp_val = getattr(item, "website_EntityOrView206", None)
                    
                    setattr(item, "website_EntityOrView206", self)
                    

    @property
    def website_CollectionUnit208(self):
        return self.__website_CollectionUnit208

    @website_CollectionUnit208.setter
    def website_CollectionUnit208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_CollectionUnit__website_CollectionUnit208", None)
        self.__website_CollectionUnit208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Feature209"):
                opp_val = getattr(old_value, "website_Feature209", None)
                if opp_val == self:
                    setattr(old_value, "website_Feature209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Feature209"):
                opp_val = getattr(value, "website_Feature209", None)
                setattr(value, "website_Feature209", self)

class website_UpdateUnit(SelectableUnit, EditUnit):

    def __init__(self, styleClass: str):
        self.styleClass = styleClass
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

class website_ChildPath(ABC):

    pass
class website_AssociationReference(ABC):

    def __init__(self, name: str, website_AssociationReference: "website_Association" = None, website_AssociationReference194: "website_Label" = None, partOf197: "website_ChildPath" = None, AssociationReference: "website_ChildPath" = None):
        self.name = name
        self.website_AssociationReference = website_AssociationReference
        self.website_AssociationReference194 = website_AssociationReference194
        self.partOf197 = partOf197
        self.AssociationReference = AssociationReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_AssociationReference(self):
        return self.__website_AssociationReference

    @website_AssociationReference.setter
    def website_AssociationReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationReference__website_AssociationReference", None)
        self.__website_AssociationReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Association192"):
                opp_val = getattr(old_value, "website_Association192", None)
                if opp_val == self:
                    setattr(old_value, "website_Association192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Association192"):
                opp_val = getattr(value, "website_Association192", None)
                setattr(value, "website_Association192", self)

    @property
    def website_AssociationReference194(self):
        return self.__website_AssociationReference194

    @website_AssociationReference194.setter
    def website_AssociationReference194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationReference__website_AssociationReference194", None)
        self.__website_AssociationReference194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Label195"):
                opp_val = getattr(old_value, "website_Label195", None)
                if opp_val == self:
                    setattr(old_value, "website_Label195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Label195"):
                opp_val = getattr(value, "website_Label195", None)
                setattr(value, "website_Label195", self)

    @property
    def AssociationReference(self):
        return self.__AssociationReference

    @AssociationReference.setter
    def AssociationReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationReference__AssociationReference", None)
        self.__AssociationReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childFeature"):
                opp_val = getattr(old_value, "childFeature", None)
                if opp_val == self:
                    setattr(old_value, "childFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childFeature"):
                opp_val = getattr(value, "childFeature", None)
                setattr(value, "childFeature", self)

    @property
    def partOf197(self):
        return self.__partOf197

    @partOf197.setter
    def partOf197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationReference__partOf197", None)
        self.__partOf197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildPath"):
                opp_val = getattr(old_value, "ChildPath", None)
                if opp_val == self:
                    setattr(old_value, "ChildPath", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildPath"):
                opp_val = getattr(value, "ChildPath", None)
                setattr(value, "ChildPath", self)

class InterfaceField:

    pass
class website_DateField(InterfaceField):

    def __init__(self, details: str, format: str):
        self.details = details
        self.format = format
        
    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class website_CaptchaField(InterfaceField):

    pass
class website_DataTypeField(InterfaceField):

    def __init__(self, obfuscateFormFields: bool, encrypt: bool, interfaceType: str, website_DataTypeField: "website_DataType" = None):
        self.obfuscateFormFields = obfuscateFormFields
        self.encrypt = encrypt
        self.interfaceType = interfaceType
        self.website_DataTypeField = website_DataTypeField
        
    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def encrypt(self) -> bool:
        return self.__encrypt

    @encrypt.setter
    def encrypt(self, encrypt: bool):
        self.__encrypt = encrypt

    @property
    def obfuscateFormFields(self) -> bool:
        return self.__obfuscateFormFields

    @obfuscateFormFields.setter
    def obfuscateFormFields(self, obfuscateFormFields: bool):
        self.__obfuscateFormFields = obfuscateFormFields

    @property
    def website_DataTypeField(self):
        return self.__website_DataTypeField

    @website_DataTypeField.setter
    def website_DataTypeField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DataTypeField__website_DataTypeField", None)
        self.__website_DataTypeField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataType200"):
                opp_val = getattr(old_value, "website_DataType200", None)
                if opp_val == self:
                    setattr(old_value, "website_DataType200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataType200"):
                opp_val = getattr(value, "website_DataType200", None)
                setattr(value, "website_DataType200", self)

class UnitFeature:

    pass
class website_UnitElement(UnitFeature):

    def __init__(self, name: str, obfuscateFormFields: bool, placeholder: str, validationPattern: str, website_UnitElement: "website_Attribute" = None, website_UnitElement181: "website_Expression" = None):
        self.name = name
        self.obfuscateFormFields = obfuscateFormFields
        self.placeholder = placeholder
        self.validationPattern = validationPattern
        self.website_UnitElement = website_UnitElement
        self.website_UnitElement181 = website_UnitElement181
        
    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def obfuscateFormFields(self) -> bool:
        return self.__obfuscateFormFields

    @obfuscateFormFields.setter
    def obfuscateFormFields(self, obfuscateFormFields: bool):
        self.__obfuscateFormFields = obfuscateFormFields

    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_UnitElement181(self):
        return self.__website_UnitElement181

    @website_UnitElement181.setter
    def website_UnitElement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitElement__website_UnitElement181", None)
        self.__website_UnitElement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Expression182"):
                opp_val = getattr(old_value, "website_Expression182", None)
                if opp_val == self:
                    setattr(old_value, "website_Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Expression182"):
                opp_val = getattr(value, "website_Expression182", None)
                setattr(value, "website_Expression182", self)

    @property
    def website_UnitElement(self):
        return self.__website_UnitElement

    @website_UnitElement.setter
    def website_UnitElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitElement__website_UnitElement", None)
        self.__website_UnitElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute179"):
                opp_val = getattr(old_value, "website_Attribute179", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute179"):
                opp_val = getattr(value, "website_Attribute179", None)
                setattr(value, "website_Attribute179", self)

class AssociationReference:

    pass
class website_ChildPathAssociation(AssociationReference, ChildPath):

    def __init__(self, isSourceAssociation: bool, website_ChildPathAssociation: "website_EntityOrView" = None, website_ChildPathAssociation268: "website_EntityOrView" = None):
        self.isSourceAssociation = isSourceAssociation
        self.website_ChildPathAssociation = website_ChildPathAssociation
        self.website_ChildPathAssociation268 = website_ChildPathAssociation268
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def website_ChildPathAssociation268(self):
        return self.__website_ChildPathAssociation268

    @website_ChildPathAssociation268.setter
    def website_ChildPathAssociation268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ChildPathAssociation__website_ChildPathAssociation268", None)
        self.__website_ChildPathAssociation268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView269"):
                opp_val = getattr(old_value, "website_EntityOrView269", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView269"):
                opp_val = getattr(value, "website_EntityOrView269", None)
                setattr(value, "website_EntityOrView269", self)

    @property
    def website_ChildPathAssociation(self):
        return self.__website_ChildPathAssociation

    @website_ChildPathAssociation.setter
    def website_ChildPathAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ChildPathAssociation__website_ChildPathAssociation", None)
        self.__website_ChildPathAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView266"):
                opp_val = getattr(old_value, "website_EntityOrView266", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView266"):
                opp_val = getattr(value, "website_EntityOrView266", None)
                setattr(value, "website_EntityOrView266", self)

class website_FeaturePathAssociation(AssociationReference, FeaturePath):

    def __init__(self, isSourceAssociation: bool, website_FeaturePathAssociation: "website_EntityOrView" = None, website_FeaturePathAssociation260: "website_EntityOrView" = None):
        self.isSourceAssociation = isSourceAssociation
        self.website_FeaturePathAssociation = website_FeaturePathAssociation
        self.website_FeaturePathAssociation260 = website_FeaturePathAssociation260
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def website_FeaturePathAssociation260(self):
        return self.__website_FeaturePathAssociation260

    @website_FeaturePathAssociation260.setter
    def website_FeaturePathAssociation260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FeaturePathAssociation__website_FeaturePathAssociation260", None)
        self.__website_FeaturePathAssociation260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView261"):
                opp_val = getattr(old_value, "website_EntityOrView261", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView261"):
                opp_val = getattr(value, "website_EntityOrView261", None)
                setattr(value, "website_EntityOrView261", self)

    @property
    def website_FeaturePathAssociation(self):
        return self.__website_FeaturePathAssociation

    @website_FeaturePathAssociation.setter
    def website_FeaturePathAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FeaturePathAssociation__website_FeaturePathAssociation", None)
        self.__website_FeaturePathAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView258"):
                opp_val = getattr(old_value, "website_EntityOrView258", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView258"):
                opp_val = getattr(value, "website_EntityOrView258", None)
                setattr(value, "website_EntityOrView258", self)

class InlineActionContainer:

    pass
class website_ImageIndexUnit(InlineActionContainer, ImageUnit):

    def __init__(self, styleClass: str, contentClass: str):
        self.styleClass = styleClass
        self.contentClass = contentClass
        
    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

class website_IndexUnit(InlineActionContainer, DataUnit, CollectionUnit):

    def __init__(self, displayOption: str, omitColumnLabels: bool, styleClass: str, contentClass: str, rowClasses: str, website_IndexUnit: "website_SearchUnit" = None):
        self.displayOption = displayOption
        self.omitColumnLabels = omitColumnLabels
        self.styleClass = styleClass
        self.contentClass = contentClass
        self.rowClasses = rowClasses
        self.website_IndexUnit = website_IndexUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def rowClasses(self) -> str:
        return self.__rowClasses

    @rowClasses.setter
    def rowClasses(self, rowClasses: str):
        self.__rowClasses = rowClasses

    @property
    def omitColumnLabels(self) -> bool:
        return self.__omitColumnLabels

    @omitColumnLabels.setter
    def omitColumnLabels(self, omitColumnLabels: bool):
        self.__omitColumnLabels = omitColumnLabels

    @property
    def displayOption(self) -> str:
        return self.__displayOption

    @displayOption.setter
    def displayOption(self, displayOption: str):
        self.__displayOption = displayOption

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def website_IndexUnit(self):
        return self.__website_IndexUnit

    @website_IndexUnit.setter
    def website_IndexUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_IndexUnit__website_IndexUnit", None)
        self.__website_IndexUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_SearchUnit"):
                opp_val = getattr(old_value, "website_SearchUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_SearchUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_SearchUnit"):
                opp_val = getattr(value, "website_SearchUnit", None)
                setattr(value, "website_SearchUnit", self)

class UnitField:

    pass
class website_UnitFeature(InlineActionContainer, UnitField):

    def __init__(self, onlyDisplayWhenNotEmpty: bool, displayLabel: str, required: bool, nullDisplayValue: str, footer: str, autofocus: bool, headerClass: str, inputClass: str, displayClass: str, footerClass: str, website_UnitFeature: "website_Expression" = None):
        self.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty
        self.displayLabel = displayLabel
        self.required = required
        self.nullDisplayValue = nullDisplayValue
        self.footer = footer
        self.autofocus = autofocus
        self.headerClass = headerClass
        self.inputClass = inputClass
        self.displayClass = displayClass
        self.footerClass = footerClass
        self.website_UnitFeature = website_UnitFeature
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def footer(self) -> str:
        return self.__footer

    @footer.setter
    def footer(self, footer: str):
        self.__footer = footer

    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def displayClass(self) -> str:
        return self.__displayClass

    @displayClass.setter
    def displayClass(self, displayClass: str):
        self.__displayClass = displayClass

    @property
    def nullDisplayValue(self) -> str:
        return self.__nullDisplayValue

    @nullDisplayValue.setter
    def nullDisplayValue(self, nullDisplayValue: str):
        self.__nullDisplayValue = nullDisplayValue

    @property
    def autofocus(self) -> bool:
        return self.__autofocus

    @autofocus.setter
    def autofocus(self, autofocus: bool):
        self.__autofocus = autofocus

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def onlyDisplayWhenNotEmpty(self) -> bool:
        return self.__onlyDisplayWhenNotEmpty

    @onlyDisplayWhenNotEmpty.setter
    def onlyDisplayWhenNotEmpty(self, onlyDisplayWhenNotEmpty: bool):
        self.__onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty

    @property
    def displayLabel(self) -> str:
        return self.__displayLabel

    @displayLabel.setter
    def displayLabel(self, displayLabel: str):
        self.__displayLabel = displayLabel

    @property
    def website_UnitFeature(self):
        return self.__website_UnitFeature

    @website_UnitFeature.setter
    def website_UnitFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitFeature__website_UnitFeature", None)
        self.__website_UnitFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Expression177"):
                opp_val = getattr(old_value, "website_Expression177", None)
                if opp_val == self:
                    setattr(old_value, "website_Expression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Expression177"):
                opp_val = getattr(value, "website_Expression177", None)
                setattr(value, "website_Expression177", self)

class ContentUnit:

    pass
class website_CreateSitemapUnit(ContentUnit):

    def __init__(self, deployedURL: str, filename: str, styleClass: str, contentClass: str):
        self.deployedURL = deployedURL
        self.filename = filename
        self.styleClass = styleClass
        self.contentClass = contentClass
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def deployedURL(self) -> str:
        return self.__deployedURL

    @deployedURL.setter
    def deployedURL(self, deployedURL: str):
        self.__deployedURL = deployedURL

class website_DynamicUnit(ContentUnit):

    def __init__(self, header: str, footer: str, headerClass: str, controlClass: str, footerClass: str, errorClass: str, displayedOn172: set["website_UnitField"] = None, website_DynamicUnit174: set["website_UnitSupportAction"] = None, website_DynamicUnit: set["website_EntityOrView"] = None, DynamicUnit: "website_UnitField" = None, website_DynamicUnit287: "website_ModelReference" = None):
        self.header = header
        self.footer = footer
        self.headerClass = headerClass
        self.controlClass = controlClass
        self.footerClass = footerClass
        self.errorClass = errorClass
        self.displayedOn172 = displayedOn172 if displayedOn172 is not None else set()
        self.website_DynamicUnit174 = website_DynamicUnit174 if website_DynamicUnit174 is not None else set()
        self.website_DynamicUnit = website_DynamicUnit if website_DynamicUnit is not None else set()
        self.DynamicUnit = DynamicUnit
        self.website_DynamicUnit287 = website_DynamicUnit287
        
    @property
    def footer(self) -> str:
        return self.__footer

    @footer.setter
    def footer(self, footer: str):
        self.__footer = footer

    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def controlClass(self) -> str:
        return self.__controlClass

    @controlClass.setter
    def controlClass(self, controlClass: str):
        self.__controlClass = controlClass

    @property
    def errorClass(self) -> str:
        return self.__errorClass

    @errorClass.setter
    def errorClass(self, errorClass: str):
        self.__errorClass = errorClass

    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def displayedOn172(self):
        return self.__displayedOn172

    @displayedOn172.setter
    def displayedOn172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DynamicUnit__displayedOn172", None)
        self.__displayedOn172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnitField"):
                    opp_val = getattr(item, "UnitField", None)
                    
                    if opp_val == self:
                        setattr(item, "UnitField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnitField"):
                    opp_val = getattr(item, "UnitField", None)
                    
                    setattr(item, "UnitField", self)
                    

    @property
    def DynamicUnit(self):
        return self.__DynamicUnit

    @DynamicUnit.setter
    def DynamicUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DynamicUnit__DynamicUnit", None)
        self.__DynamicUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "displayFields"):
                opp_val = getattr(old_value, "displayFields", None)
                if opp_val == self:
                    setattr(old_value, "displayFields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "displayFields"):
                opp_val = getattr(value, "displayFields", None)
                setattr(value, "displayFields", self)

    @property
    def website_DynamicUnit(self):
        return self.__website_DynamicUnit

    @website_DynamicUnit.setter
    def website_DynamicUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DynamicUnit__website_DynamicUnit", None)
        self.__website_DynamicUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_EntityOrView170"):
                    opp_val = getattr(item, "website_EntityOrView170", None)
                    
                    if opp_val == self:
                        setattr(item, "website_EntityOrView170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_EntityOrView170"):
                    opp_val = getattr(item, "website_EntityOrView170", None)
                    
                    setattr(item, "website_EntityOrView170", self)
                    

    @property
    def website_DynamicUnit287(self):
        return self.__website_DynamicUnit287

    @website_DynamicUnit287.setter
    def website_DynamicUnit287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DynamicUnit__website_DynamicUnit287", None)
        self.__website_DynamicUnit287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ModelReference"):
                opp_val = getattr(old_value, "website_ModelReference", None)
                if opp_val == self:
                    setattr(old_value, "website_ModelReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ModelReference"):
                opp_val = getattr(value, "website_ModelReference", None)
                setattr(value, "website_ModelReference", self)

    @property
    def website_DynamicUnit174(self):
        return self.__website_DynamicUnit174

    @website_DynamicUnit174.setter
    def website_DynamicUnit174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DynamicUnit__website_DynamicUnit174", None)
        self.__website_DynamicUnit174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_UnitSupportAction"):
                    opp_val = getattr(item, "website_UnitSupportAction", None)
                    
                    if opp_val == self:
                        setattr(item, "website_UnitSupportAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_UnitSupportAction"):
                    opp_val = getattr(item, "website_UnitSupportAction", None)
                    
                    setattr(item, "website_UnitSupportAction", self)
                    

class website_StaticUnit(ContentUnit):

    def __init__(self, content: str, styleClass: str, contentClass: str):
        self.content = content
        self.styleClass = styleClass
        self.contentClass = contentClass
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def contentClass(self) -> str:
        return self.__contentClass

    @contentClass.setter
    def contentClass(self, contentClass: str):
        self.__contentClass = contentClass

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class website_UnitContainer(ABC):

    pass
class website_QueryParameter:

    def __init__(self, value: str, website_QueryParameter: "website_Query" = None, website_QueryParameter165: "website_FilterParameter" = None):
        self.value = value
        self.website_QueryParameter = website_QueryParameter
        self.website_QueryParameter165 = website_QueryParameter165
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def website_QueryParameter(self):
        return self.__website_QueryParameter

    @website_QueryParameter.setter
    def website_QueryParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_QueryParameter__website_QueryParameter", None)
        self.__website_QueryParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Query163"):
                opp_val = getattr(old_value, "website_Query163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Query163"):
                opp_val = getattr(value, "website_Query163", None)
                if opp_val is None:
                    setattr(value, "website_Query163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_QueryParameter165(self):
        return self.__website_QueryParameter165

    @website_QueryParameter165.setter
    def website_QueryParameter165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_QueryParameter__website_QueryParameter165", None)
        self.__website_QueryParameter165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FilterParameter166"):
                opp_val = getattr(old_value, "website_FilterParameter166", None)
                if opp_val == self:
                    setattr(old_value, "website_FilterParameter166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FilterParameter166"):
                opp_val = getattr(value, "website_FilterParameter166", None)
                setattr(value, "website_FilterParameter166", self)

class website_UnitField(ABC):

    def __init__(self, title: str, collectionDisplayOption: str, collectionAllowAdd: bool, collectionAllowRemove: bool, maximumDisplaySize: int, dateFormat: str, UnitField: "website_DynamicUnit" = None, displayFields: "website_DynamicUnit" = None, website_UnitField: "website_InterfaceField" = None):
        self.title = title
        self.collectionDisplayOption = collectionDisplayOption
        self.collectionAllowAdd = collectionAllowAdd
        self.collectionAllowRemove = collectionAllowRemove
        self.maximumDisplaySize = maximumDisplaySize
        self.dateFormat = dateFormat
        self.UnitField = UnitField
        self.displayFields = displayFields
        self.website_UnitField = website_UnitField
        
    @property
    def maximumDisplaySize(self) -> int:
        return self.__maximumDisplaySize

    @maximumDisplaySize.setter
    def maximumDisplaySize(self, maximumDisplaySize: int):
        self.__maximumDisplaySize = maximumDisplaySize

    @property
    def collectionAllowAdd(self) -> bool:
        return self.__collectionAllowAdd

    @collectionAllowAdd.setter
    def collectionAllowAdd(self, collectionAllowAdd: bool):
        self.__collectionAllowAdd = collectionAllowAdd

    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

    @property
    def collectionDisplayOption(self) -> str:
        return self.__collectionDisplayOption

    @collectionDisplayOption.setter
    def collectionDisplayOption(self, collectionDisplayOption: str):
        self.__collectionDisplayOption = collectionDisplayOption

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def collectionAllowRemove(self) -> bool:
        return self.__collectionAllowRemove

    @collectionAllowRemove.setter
    def collectionAllowRemove(self, collectionAllowRemove: bool):
        self.__collectionAllowRemove = collectionAllowRemove

    @property
    def UnitField(self):
        return self.__UnitField

    @UnitField.setter
    def UnitField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitField__UnitField", None)
        self.__UnitField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "displayedOn172"):
                opp_val = getattr(old_value, "displayedOn172", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "displayedOn172"):
                opp_val = getattr(value, "displayedOn172", None)
                if opp_val is None:
                    setattr(value, "displayedOn172", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def displayFields(self):
        return self.__displayFields

    @displayFields.setter
    def displayFields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitField__displayFields", None)
        self.__displayFields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicUnit"):
                opp_val = getattr(old_value, "DynamicUnit", None)
                if opp_val == self:
                    setattr(old_value, "DynamicUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicUnit"):
                opp_val = getattr(value, "DynamicUnit", None)
                setattr(value, "DynamicUnit", self)

    @property
    def website_UnitField(self):
        return self.__website_UnitField

    @website_UnitField.setter
    def website_UnitField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitField__website_UnitField", None)
        self.__website_UnitField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_InterfaceField"):
                opp_val = getattr(old_value, "website_InterfaceField", None)
                if opp_val == self:
                    setattr(old_value, "website_InterfaceField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_InterfaceField"):
                opp_val = getattr(value, "website_InterfaceField", None)
                setattr(value, "website_InterfaceField", self)

class website_Query:

    pass
class MenuEntry:

    pass
class website_MenuFeature(MenuEntry):

    pass
class Menu:

    pass
class website_DynamicMenu(Menu):

    pass
class website_StaticMenu(Menu):

    pass
class website_MenuEntry(ABC):

    def __init__(self, requiresRole: str, MenuEntry: "website_Menu" = None, entries: "website_Menu" = None):
        self.requiresRole = requiresRole
        self.MenuEntry = MenuEntry
        self.entries = entries
        
    @property
    def requiresRole(self) -> str:
        return self.__requiresRole

    @requiresRole.setter
    def requiresRole(self, requiresRole: str):
        self.__requiresRole = requiresRole

    @property
    def entries(self):
        return self.__entries

    @entries.setter
    def entries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_MenuEntry__entries", None)
        self.__entries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Menu"):
                opp_val = getattr(old_value, "Menu", None)
                if opp_val == self:
                    setattr(old_value, "Menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Menu"):
                opp_val = getattr(value, "Menu", None)
                setattr(value, "Menu", self)

    @property
    def MenuEntry(self):
        return self.__MenuEntry

    @MenuEntry.setter
    def MenuEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_MenuEntry__MenuEntry", None)
        self.__MenuEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf137"):
                opp_val = getattr(old_value, "partOf137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf137"):
                opp_val = getattr(value, "partOf137", None)
                if opp_val is None:
                    setattr(value, "partOf137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class website_PageLink:

    pass
class UnitContainer:

    pass
class website_UnitAssociation(UnitFeature, AssociationReference, UnitContainer):

    def __init__(self, isSourceAssociation: bool, website_UnitAssociation: "website_EntityOrView" = None, website_UnitAssociation186: "website_EntityOrView" = None, website_UnitAssociation189: "website_Selection" = None):
        self.isSourceAssociation = isSourceAssociation
        self.website_UnitAssociation = website_UnitAssociation
        self.website_UnitAssociation186 = website_UnitAssociation186
        self.website_UnitAssociation189 = website_UnitAssociation189
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def website_UnitAssociation(self):
        return self.__website_UnitAssociation

    @website_UnitAssociation.setter
    def website_UnitAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitAssociation__website_UnitAssociation", None)
        self.__website_UnitAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView184"):
                opp_val = getattr(old_value, "website_EntityOrView184", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView184"):
                opp_val = getattr(value, "website_EntityOrView184", None)
                setattr(value, "website_EntityOrView184", self)

    @property
    def website_UnitAssociation186(self):
        return self.__website_UnitAssociation186

    @website_UnitAssociation186.setter
    def website_UnitAssociation186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitAssociation__website_UnitAssociation186", None)
        self.__website_UnitAssociation186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView187"):
                opp_val = getattr(old_value, "website_EntityOrView187", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView187"):
                opp_val = getattr(value, "website_EntityOrView187", None)
                setattr(value, "website_EntityOrView187", self)

    @property
    def website_UnitAssociation189(self):
        return self.__website_UnitAssociation189

    @website_UnitAssociation189.setter
    def website_UnitAssociation189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitAssociation__website_UnitAssociation189", None)
        self.__website_UnitAssociation189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection190"):
                opp_val = getattr(old_value, "website_Selection190", None)
                if opp_val == self:
                    setattr(old_value, "website_Selection190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection190"):
                opp_val = getattr(value, "website_Selection190", None)
                setattr(value, "website_Selection190", self)

class ImageFilter:

    pass
class website_ThumbnailFilter(ImageFilter):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class website_ImageFilter(ABC):

    pass
class website_Order:

    pass
class website_Predicate:

    pass
class EncapsulatedFeature:

    pass
class ViewFeature:

    pass
class website_EncapsulatedFeature(ViewFeature):

    def __init__(self, displayLabel: str, alias: str, columnName: str):
        self.displayLabel = displayLabel
        self.alias = alias
        self.columnName = columnName
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def displayLabel(self) -> str:
        return self.__displayLabel

    @displayLabel.setter
    def displayLabel(self, displayLabel: str):
        self.__displayLabel = displayLabel

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

class EntityAssociation:

    pass
class website_AssociationWithContainment(EntityAssociation):

    def __init__(self, sourceVisible: bool):
        self.sourceVisible = sourceVisible
        
    @property
    def sourceVisible(self) -> bool:
        return self.__sourceVisible

    @sourceVisible.setter
    def sourceVisible(self, sourceVisible: bool):
        self.__sourceVisible = sourceVisible

class website_AssociationWithoutContainment(EntityAssociation):

    def __init__(self, targetCardinality: str, targetUnique: bool):
        self.targetCardinality = targetCardinality
        self.targetUnique = targetUnique
        
    @property
    def targetCardinality(self) -> str:
        return self.__targetCardinality

    @targetCardinality.setter
    def targetCardinality(self, targetCardinality: str):
        self.__targetCardinality = targetCardinality

    @property
    def targetUnique(self) -> bool:
        return self.__targetUnique

    @targetUnique.setter
    def targetUnique(self, targetUnique: bool):
        self.__targetUnique = targetUnique

class website_AssociationKey:

    def __init__(self, targetColumnName: str, website_AssociationKey: "website_EntityFeature" = None, website_AssociationKey86: "website_EntityFeature" = None, AssociationKey: "website_EntityAssociation" = None, keys: "website_EntityAssociation" = None):
        self.targetColumnName = targetColumnName
        self.website_AssociationKey = website_AssociationKey
        self.website_AssociationKey86 = website_AssociationKey86
        self.AssociationKey = AssociationKey
        self.keys = keys
        
    @property
    def targetColumnName(self) -> str:
        return self.__targetColumnName

    @targetColumnName.setter
    def targetColumnName(self, targetColumnName: str):
        self.__targetColumnName = targetColumnName

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationKey__keys", None)
        self.__keys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityAssociation83"):
                opp_val = getattr(old_value, "EntityAssociation83", None)
                if opp_val == self:
                    setattr(old_value, "EntityAssociation83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityAssociation83"):
                opp_val = getattr(value, "EntityAssociation83", None)
                setattr(value, "EntityAssociation83", self)

    @property
    def AssociationKey(self):
        return self.__AssociationKey

    @AssociationKey.setter
    def AssociationKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationKey__AssociationKey", None)
        self.__AssociationKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keyFor"):
                opp_val = getattr(old_value, "keyFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keyFor"):
                opp_val = getattr(value, "keyFor", None)
                if opp_val is None:
                    setattr(value, "keyFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_AssociationKey(self):
        return self.__website_AssociationKey

    @website_AssociationKey.setter
    def website_AssociationKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationKey__website_AssociationKey", None)
        self.__website_AssociationKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityFeature"):
                opp_val = getattr(old_value, "website_EntityFeature", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityFeature"):
                opp_val = getattr(value, "website_EntityFeature", None)
                setattr(value, "website_EntityFeature", self)

    @property
    def website_AssociationKey86(self):
        return self.__website_AssociationKey86

    @website_AssociationKey86.setter
    def website_AssociationKey86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_AssociationKey__website_AssociationKey86", None)
        self.__website_AssociationKey86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityFeature87"):
                opp_val = getattr(old_value, "website_EntityFeature87", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityFeature87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityFeature87"):
                opp_val = getattr(value, "website_EntityFeature87", None)
                setattr(value, "website_EntityFeature87", self)

class Association:

    pass
class ResourceAttribute:

    pass
class website_ImageAttribute(ResourceAttribute):

    pass
class website_FileAttribute(ResourceAttribute):

    pass
class PathElement:

    pass
class website_DatePathElement(PathElement):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class website_StaticPathElement(PathElement):

    def __init__(self, element: str):
        self.element = element
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

class website_PathElement(ABC):

    pass
class EntityAttribute:

    pass
class website_LocationAttribute(EntityAttribute):

    pass
class website_DateAttribute(EntityAttribute):

    def __init__(self, details: str, format: str):
        self.details = details
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

class website_UrlAttribute(EntityAttribute):

    def __init__(self, displayValue: str):
        self.displayValue = displayValue
        
    @property
    def displayValue(self) -> str:
        return self.__displayValue

    @displayValue.setter
    def displayValue(self, displayValue: str):
        self.__displayValue = displayValue

class website_DataTypeAttribute(EntityAttribute):

    def __init__(self, obfuscateFormFields: bool, caseInsensitive: bool, encrypt: bool, website_DataTypeAttribute: "website_DataType" = None):
        self.obfuscateFormFields = obfuscateFormFields
        self.caseInsensitive = caseInsensitive
        self.encrypt = encrypt
        self.website_DataTypeAttribute = website_DataTypeAttribute
        
    @property
    def encrypt(self) -> bool:
        return self.__encrypt

    @encrypt.setter
    def encrypt(self, encrypt: bool):
        self.__encrypt = encrypt

    @property
    def obfuscateFormFields(self) -> bool:
        return self.__obfuscateFormFields

    @obfuscateFormFields.setter
    def obfuscateFormFields(self, obfuscateFormFields: bool):
        self.__obfuscateFormFields = obfuscateFormFields

    @property
    def caseInsensitive(self) -> bool:
        return self.__caseInsensitive

    @caseInsensitive.setter
    def caseInsensitive(self, caseInsensitive: bool):
        self.__caseInsensitive = caseInsensitive

    @property
    def website_DataTypeAttribute(self):
        return self.__website_DataTypeAttribute

    @website_DataTypeAttribute.setter
    def website_DataTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DataTypeAttribute__website_DataTypeAttribute", None)
        self.__website_DataTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataType"):
                opp_val = getattr(old_value, "website_DataType", None)
                if opp_val == self:
                    setattr(old_value, "website_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataType"):
                opp_val = getattr(value, "website_DataType", None)
                setattr(value, "website_DataType", self)

class Attribute:

    pass
class website_EncapsulatedAttribute(EncapsulatedFeature, Attribute):

    def __init__(self, name: str, cardinality: str, website_EncapsulatedAttribute: "website_Attribute" = None):
        self.name = name
        self.cardinality = cardinality
        self.website_EncapsulatedAttribute = website_EncapsulatedAttribute
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def website_EncapsulatedAttribute(self):
        return self.__website_EncapsulatedAttribute

    @website_EncapsulatedAttribute.setter
    def website_EncapsulatedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAttribute__website_EncapsulatedAttribute", None)
        self.__website_EncapsulatedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute94"):
                opp_val = getattr(old_value, "website_Attribute94", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute94"):
                opp_val = getattr(value, "website_Attribute94", None)
                setattr(value, "website_Attribute94", self)

class EntityFeature:

    pass
class website_EntityAttribute(EntityFeature, Attribute):

    def __init__(self, primaryKey: bool, containerUnique: bool, persistentType: str, ormType: str, interfaceType: str):
        self.primaryKey = primaryKey
        self.containerUnique = containerUnique
        self.persistentType = persistentType
        self.ormType = ormType
        self.interfaceType = interfaceType
        
    @property
    def primaryKey(self) -> bool:
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey

    @property
    def ormType(self) -> str:
        return self.__ormType

    @ormType.setter
    def ormType(self, ormType: str):
        self.__ormType = ormType

    @property
    def persistentType(self) -> str:
        return self.__persistentType

    @persistentType.setter
    def persistentType(self, persistentType: str):
        self.__persistentType = persistentType

    @property
    def containerUnique(self) -> bool:
        return self.__containerUnique

    @containerUnique.setter
    def containerUnique(self, containerUnique: bool):
        self.__containerUnique = containerUnique

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

class website_ResourceAttribute(EntityAttribute):

    def __init__(self, maximumUploadSize: int, validUploadMimeTypes: str, validUploadExtensions: str, uploadsWithinWebsite: bool, website_ResourceAttribute: set["website_PathElement"] = None):
        self.maximumUploadSize = maximumUploadSize
        self.validUploadMimeTypes = validUploadMimeTypes
        self.validUploadExtensions = validUploadExtensions
        self.uploadsWithinWebsite = uploadsWithinWebsite
        self.website_ResourceAttribute = website_ResourceAttribute if website_ResourceAttribute is not None else set()
        
    @property
    def validUploadMimeTypes(self) -> str:
        return self.__validUploadMimeTypes

    @validUploadMimeTypes.setter
    def validUploadMimeTypes(self, validUploadMimeTypes: str):
        self.__validUploadMimeTypes = validUploadMimeTypes

    @property
    def validUploadExtensions(self) -> str:
        return self.__validUploadExtensions

    @validUploadExtensions.setter
    def validUploadExtensions(self, validUploadExtensions: str):
        self.__validUploadExtensions = validUploadExtensions

    @property
    def uploadsWithinWebsite(self) -> bool:
        return self.__uploadsWithinWebsite

    @uploadsWithinWebsite.setter
    def uploadsWithinWebsite(self, uploadsWithinWebsite: bool):
        self.__uploadsWithinWebsite = uploadsWithinWebsite

    @property
    def maximumUploadSize(self) -> int:
        return self.__maximumUploadSize

    @maximumUploadSize.setter
    def maximumUploadSize(self, maximumUploadSize: int):
        self.__maximumUploadSize = maximumUploadSize

    @property
    def website_ResourceAttribute(self):
        return self.__website_ResourceAttribute

    @website_ResourceAttribute.setter
    def website_ResourceAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ResourceAttribute__website_ResourceAttribute", None)
        self.__website_ResourceAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_PathElement"):
                    opp_val = getattr(item, "website_PathElement", None)
                    
                    if opp_val == self:
                        setattr(item, "website_PathElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_PathElement"):
                    opp_val = getattr(item, "website_PathElement", None)
                    
                    setattr(item, "website_PathElement", self)
                    

class EntityOrView:

    pass
class website_View(EntityOrView):

    pass
class website_Entity(EntityOrView):

    pass
class website_EntityAssociation(EntityFeature, Association):

    def __init__(self, bidirectional: bool, pivotTableName: str, targetFeatureName: str, targetPrimaryKey: bool, targetDisplayLabel: str, targetHeaderClass: str, targetInputClass: str, targetDisplayClass: str, targetFooterClass: str, EntityAssociation: "website_Entity" = None, website_EntityAssociation: "website_ModelLabelAssociation" = None, keyFor: set["website_AssociationKey"] = None, associationEnds: "website_Entity" = None, EntityAssociation83: "website_AssociationKey" = None):
        self.bidirectional = bidirectional
        self.pivotTableName = pivotTableName
        self.targetFeatureName = targetFeatureName
        self.targetPrimaryKey = targetPrimaryKey
        self.targetDisplayLabel = targetDisplayLabel
        self.targetHeaderClass = targetHeaderClass
        self.targetInputClass = targetInputClass
        self.targetDisplayClass = targetDisplayClass
        self.targetFooterClass = targetFooterClass
        self.EntityAssociation = EntityAssociation
        self.website_EntityAssociation = website_EntityAssociation
        self.keyFor = keyFor if keyFor is not None else set()
        self.associationEnds = associationEnds
        self.EntityAssociation83 = EntityAssociation83
        
    @property
    def targetDisplayLabel(self) -> str:
        return self.__targetDisplayLabel

    @targetDisplayLabel.setter
    def targetDisplayLabel(self, targetDisplayLabel: str):
        self.__targetDisplayLabel = targetDisplayLabel

    @property
    def targetPrimaryKey(self) -> bool:
        return self.__targetPrimaryKey

    @targetPrimaryKey.setter
    def targetPrimaryKey(self, targetPrimaryKey: bool):
        self.__targetPrimaryKey = targetPrimaryKey

    @property
    def pivotTableName(self) -> str:
        return self.__pivotTableName

    @pivotTableName.setter
    def pivotTableName(self, pivotTableName: str):
        self.__pivotTableName = pivotTableName

    @property
    def bidirectional(self) -> bool:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: bool):
        self.__bidirectional = bidirectional

    @property
    def targetFooterClass(self) -> str:
        return self.__targetFooterClass

    @targetFooterClass.setter
    def targetFooterClass(self, targetFooterClass: str):
        self.__targetFooterClass = targetFooterClass

    @property
    def targetFeatureName(self) -> str:
        return self.__targetFeatureName

    @targetFeatureName.setter
    def targetFeatureName(self, targetFeatureName: str):
        self.__targetFeatureName = targetFeatureName

    @property
    def targetDisplayClass(self) -> str:
        return self.__targetDisplayClass

    @targetDisplayClass.setter
    def targetDisplayClass(self, targetDisplayClass: str):
        self.__targetDisplayClass = targetDisplayClass

    @property
    def targetHeaderClass(self) -> str:
        return self.__targetHeaderClass

    @targetHeaderClass.setter
    def targetHeaderClass(self, targetHeaderClass: str):
        self.__targetHeaderClass = targetHeaderClass

    @property
    def targetInputClass(self) -> str:
        return self.__targetInputClass

    @targetInputClass.setter
    def targetInputClass(self, targetInputClass: str):
        self.__targetInputClass = targetInputClass

    @property
    def keyFor(self):
        return self.__keyFor

    @keyFor.setter
    def keyFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityAssociation__keyFor", None)
        self.__keyFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationKey"):
                    opp_val = getattr(item, "AssociationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationKey"):
                    opp_val = getattr(item, "AssociationKey", None)
                    
                    setattr(item, "AssociationKey", self)
                    

    @property
    def EntityAssociation(self):
        return self.__EntityAssociation

    @EntityAssociation.setter
    def EntityAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityAssociation__EntityAssociation", None)
        self.__EntityAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetEntity"):
                opp_val = getattr(old_value, "targetEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetEntity"):
                opp_val = getattr(value, "targetEntity", None)
                if opp_val is None:
                    setattr(value, "targetEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EntityAssociation83(self):
        return self.__EntityAssociation83

    @EntityAssociation83.setter
    def EntityAssociation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityAssociation__EntityAssociation83", None)
        self.__EntityAssociation83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keys"):
                opp_val = getattr(old_value, "keys", None)
                if opp_val == self:
                    setattr(old_value, "keys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keys"):
                opp_val = getattr(value, "keys", None)
                setattr(value, "keys", self)

    @property
    def website_EntityAssociation(self):
        return self.__website_EntityAssociation

    @website_EntityAssociation.setter
    def website_EntityAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityAssociation__website_EntityAssociation", None)
        self.__website_EntityAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ModelLabelAssociation"):
                opp_val = getattr(old_value, "website_ModelLabelAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_ModelLabelAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ModelLabelAssociation"):
                opp_val = getattr(value, "website_ModelLabelAssociation", None)
                setattr(value, "website_ModelLabelAssociation", self)

    @property
    def associationEnds(self):
        return self.__associationEnds

    @associationEnds.setter
    def associationEnds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityAssociation__associationEnds", None)
        self.__associationEnds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity81"):
                opp_val = getattr(old_value, "Entity81", None)
                if opp_val == self:
                    setattr(old_value, "Entity81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity81"):
                opp_val = getattr(value, "Entity81", None)
                setattr(value, "Entity81", self)

class ModelLabelFeature:

    pass
class website_ModelLabelAssociation(ModelLabelFeature):

    def __init__(self, isSourceAssociation: bool, website_ModelLabelAssociation: "website_EntityAssociation" = None, website_ModelLabelAssociation72: "website_ModelLabel" = None):
        self.isSourceAssociation = isSourceAssociation
        self.website_ModelLabelAssociation = website_ModelLabelAssociation
        self.website_ModelLabelAssociation72 = website_ModelLabelAssociation72
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def website_ModelLabelAssociation72(self):
        return self.__website_ModelLabelAssociation72

    @website_ModelLabelAssociation72.setter
    def website_ModelLabelAssociation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabelAssociation__website_ModelLabelAssociation72", None)
        self.__website_ModelLabelAssociation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ModelLabel"):
                opp_val = getattr(old_value, "website_ModelLabel", None)
                if opp_val == self:
                    setattr(old_value, "website_ModelLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ModelLabel"):
                opp_val = getattr(value, "website_ModelLabel", None)
                setattr(value, "website_ModelLabel", self)

    @property
    def website_ModelLabelAssociation(self):
        return self.__website_ModelLabelAssociation

    @website_ModelLabelAssociation.setter
    def website_ModelLabelAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabelAssociation__website_ModelLabelAssociation", None)
        self.__website_ModelLabelAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityAssociation"):
                opp_val = getattr(old_value, "website_EntityAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityAssociation"):
                opp_val = getattr(value, "website_EntityAssociation", None)
                setattr(value, "website_EntityAssociation", self)

class website_ModelLabelAttribute(ModelLabelFeature):

    def __init__(self, dateFormat: str, website_ModelLabelAttribute: "website_Attribute" = None):
        self.dateFormat = dateFormat
        self.website_ModelLabelAttribute = website_ModelLabelAttribute
        
    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

    @property
    def website_ModelLabelAttribute(self):
        return self.__website_ModelLabelAttribute

    @website_ModelLabelAttribute.setter
    def website_ModelLabelAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabelAttribute__website_ModelLabelAttribute", None)
        self.__website_ModelLabelAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute69"):
                opp_val = getattr(old_value, "website_Attribute69", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute69"):
                opp_val = getattr(value, "website_Attribute69", None)
                setattr(value, "website_Attribute69", self)

class website_ModelLabelFeature(ABC):

    pass
class website_Label(ABC):

    pass
class website_EncapsulatedAssociation(EncapsulatedFeature, Association):

    def __init__(self, name: str, isSourceAssociation: bool, cardinality: str, EncapsulatedAssociation: "website_Association" = None, website_EncapsulatedAssociation101: "website_Entity" = None, encapsulatedBy: "website_Association" = None, website_EncapsulatedAssociation: "website_EncapsulatedAssociation" = None, website_EncapsulatedAssociation96: "website_EncapsulatedAssociation" = None, website_EncapsulatedAssociation99: "website_Entity" = None, website_EncapsulatedAssociation104: "website_ViewAssociation" = None):
        self.name = name
        self.isSourceAssociation = isSourceAssociation
        self.cardinality = cardinality
        self.EncapsulatedAssociation = EncapsulatedAssociation
        self.website_EncapsulatedAssociation101 = website_EncapsulatedAssociation101
        self.encapsulatedBy = encapsulatedBy
        self.website_EncapsulatedAssociation = website_EncapsulatedAssociation
        self.website_EncapsulatedAssociation96 = website_EncapsulatedAssociation96
        self.website_EncapsulatedAssociation99 = website_EncapsulatedAssociation99
        self.website_EncapsulatedAssociation104 = website_EncapsulatedAssociation104
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def website_EncapsulatedAssociation104(self):
        return self.__website_EncapsulatedAssociation104

    @website_EncapsulatedAssociation104.setter
    def website_EncapsulatedAssociation104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__website_EncapsulatedAssociation104", None)
        self.__website_EncapsulatedAssociation104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ViewAssociation"):
                opp_val = getattr(old_value, "website_ViewAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_ViewAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ViewAssociation"):
                opp_val = getattr(value, "website_ViewAssociation", None)
                setattr(value, "website_ViewAssociation", self)

    @property
    def website_EncapsulatedAssociation(self):
        return self.__website_EncapsulatedAssociation

    @website_EncapsulatedAssociation.setter
    def website_EncapsulatedAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__website_EncapsulatedAssociation", None)
        self.__website_EncapsulatedAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EncapsulatedAssociation96"):
                opp_val = getattr(old_value, "website_EncapsulatedAssociation96", None)
                if opp_val == self:
                    setattr(old_value, "website_EncapsulatedAssociation96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EncapsulatedAssociation96"):
                opp_val = getattr(value, "website_EncapsulatedAssociation96", None)
                setattr(value, "website_EncapsulatedAssociation96", self)

    @property
    def website_EncapsulatedAssociation99(self):
        return self.__website_EncapsulatedAssociation99

    @website_EncapsulatedAssociation99.setter
    def website_EncapsulatedAssociation99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__website_EncapsulatedAssociation99", None)
        self.__website_EncapsulatedAssociation99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Entity"):
                opp_val = getattr(old_value, "website_Entity", None)
                if opp_val == self:
                    setattr(old_value, "website_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Entity"):
                opp_val = getattr(value, "website_Entity", None)
                setattr(value, "website_Entity", self)

    @property
    def encapsulatedBy(self):
        return self.__encapsulatedBy

    @encapsulatedBy.setter
    def encapsulatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__encapsulatedBy", None)
        self.__encapsulatedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def EncapsulatedAssociation(self):
        return self.__EncapsulatedAssociation

    @EncapsulatedAssociation.setter
    def EncapsulatedAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__EncapsulatedAssociation", None)
        self.__EncapsulatedAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EncapsulatedAssociation101(self):
        return self.__website_EncapsulatedAssociation101

    @website_EncapsulatedAssociation101.setter
    def website_EncapsulatedAssociation101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__website_EncapsulatedAssociation101", None)
        self.__website_EncapsulatedAssociation101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Entity102"):
                opp_val = getattr(old_value, "website_Entity102", None)
                if opp_val == self:
                    setattr(old_value, "website_Entity102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Entity102"):
                opp_val = getattr(value, "website_Entity102", None)
                setattr(value, "website_Entity102", self)

    @property
    def website_EncapsulatedAssociation96(self):
        return self.__website_EncapsulatedAssociation96

    @website_EncapsulatedAssociation96.setter
    def website_EncapsulatedAssociation96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EncapsulatedAssociation__website_EncapsulatedAssociation96", None)
        self.__website_EncapsulatedAssociation96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EncapsulatedAssociation"):
                opp_val = getattr(old_value, "website_EncapsulatedAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_EncapsulatedAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EncapsulatedAssociation"):
                opp_val = getattr(value, "website_EncapsulatedAssociation", None)
                setattr(value, "website_EncapsulatedAssociation", self)

class website_Expression:

    pass
class Label:

    pass
class Feature:

    pass
class website_ViewFeature(Feature):

    pass
class website_Association(Feature):

    def __init__(self, pseudo: bool, inputClass: str, serializationMaxDepth: int, website_Association: "website_EntityOrView" = None, website_Association54: "website_EntityOrView" = None, association: set["website_EncapsulatedAssociation"] = None, website_Association59: "website_EntityOrView" = None, website_Association62: "website_EntityOrView" = None, Association: "website_EncapsulatedAssociation" = None, website_Association117: "website_Selection" = None, website_Association192: "website_AssociationReference" = None):
        self.pseudo = pseudo
        self.inputClass = inputClass
        self.serializationMaxDepth = serializationMaxDepth
        self.website_Association = website_Association
        self.website_Association54 = website_Association54
        self.association = association if association is not None else set()
        self.website_Association59 = website_Association59
        self.website_Association62 = website_Association62
        self.Association = Association
        self.website_Association117 = website_Association117
        self.website_Association192 = website_Association192
        
    @property
    def serializationMaxDepth(self) -> int:
        return self.__serializationMaxDepth

    @serializationMaxDepth.setter
    def serializationMaxDepth(self, serializationMaxDepth: int):
        self.__serializationMaxDepth = serializationMaxDepth

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def pseudo(self) -> bool:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo: bool):
        self.__pseudo = pseudo

    @property
    def website_Association54(self):
        return self.__website_Association54

    @website_Association54.setter
    def website_Association54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association54", None)
        self.__website_Association54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView53"):
                opp_val = getattr(old_value, "website_EntityOrView53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView53"):
                opp_val = getattr(value, "website_EntityOrView53", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Association62(self):
        return self.__website_Association62

    @website_Association62.setter
    def website_Association62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association62", None)
        self.__website_Association62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView63"):
                opp_val = getattr(old_value, "website_EntityOrView63", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView63"):
                opp_val = getattr(value, "website_EntityOrView63", None)
                setattr(value, "website_EntityOrView63", self)

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EncapsulatedAssociation"):
                    opp_val = getattr(item, "EncapsulatedAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "EncapsulatedAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EncapsulatedAssociation"):
                    opp_val = getattr(item, "EncapsulatedAssociation", None)
                    
                    setattr(item, "EncapsulatedAssociation", self)
                    

    @property
    def website_Association117(self):
        return self.__website_Association117

    @website_Association117.setter
    def website_Association117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association117", None)
        self.__website_Association117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection116"):
                opp_val = getattr(old_value, "website_Selection116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection116"):
                opp_val = getattr(value, "website_Selection116", None)
                if opp_val is None:
                    setattr(value, "website_Selection116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Association192(self):
        return self.__website_Association192

    @website_Association192.setter
    def website_Association192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association192", None)
        self.__website_Association192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_AssociationReference"):
                opp_val = getattr(old_value, "website_AssociationReference", None)
                if opp_val == self:
                    setattr(old_value, "website_AssociationReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_AssociationReference"):
                opp_val = getattr(value, "website_AssociationReference", None)
                setattr(value, "website_AssociationReference", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "encapsulatedBy"):
                opp_val = getattr(old_value, "encapsulatedBy", None)
                if opp_val == self:
                    setattr(old_value, "encapsulatedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encapsulatedBy"):
                opp_val = getattr(value, "encapsulatedBy", None)
                setattr(value, "encapsulatedBy", self)

    @property
    def website_Association59(self):
        return self.__website_Association59

    @website_Association59.setter
    def website_Association59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association59", None)
        self.__website_Association59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView60"):
                opp_val = getattr(old_value, "website_EntityOrView60", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView60"):
                opp_val = getattr(value, "website_EntityOrView60", None)
                setattr(value, "website_EntityOrView60", self)

    @property
    def website_Association(self):
        return self.__website_Association

    @website_Association.setter
    def website_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Association__website_Association", None)
        self.__website_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView51"):
                opp_val = getattr(old_value, "website_EntityOrView51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView51"):
                opp_val = getattr(value, "website_EntityOrView51", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class website_Feature(ABC):

    def __init__(self, serializationExpose: bool, headerClass: str, displayClass: str, footerClass: str, title: str, collectionAllowAdd: bool, collectionAllowRemove: bool, nullDisplayValue: str, encodeUriKey: bool, serializationGroups: str, website_Feature43: "website_EntityOrView" = None, website_Feature46: "website_EntityOrView" = None, website_Feature: "website_EntityOrView" = None, website_Feature35: "website_EntityOrView" = None, website_Feature38: "website_EntityOrView" = None, website_Feature113: "website_Selection" = None, website_Feature209: "website_CollectionUnit" = None, website_Feature289: "website_FeatureReference" = None):
        self.serializationExpose = serializationExpose
        self.headerClass = headerClass
        self.displayClass = displayClass
        self.footerClass = footerClass
        self.title = title
        self.collectionAllowAdd = collectionAllowAdd
        self.collectionAllowRemove = collectionAllowRemove
        self.nullDisplayValue = nullDisplayValue
        self.encodeUriKey = encodeUriKey
        self.serializationGroups = serializationGroups
        self.website_Feature43 = website_Feature43
        self.website_Feature46 = website_Feature46
        self.website_Feature = website_Feature
        self.website_Feature35 = website_Feature35
        self.website_Feature38 = website_Feature38
        self.website_Feature113 = website_Feature113
        self.website_Feature209 = website_Feature209
        self.website_Feature289 = website_Feature289
        
    @property
    def encodeUriKey(self) -> bool:
        return self.__encodeUriKey

    @encodeUriKey.setter
    def encodeUriKey(self, encodeUriKey: bool):
        self.__encodeUriKey = encodeUriKey

    @property
    def displayClass(self) -> str:
        return self.__displayClass

    @displayClass.setter
    def displayClass(self, displayClass: str):
        self.__displayClass = displayClass

    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def serializationExpose(self) -> bool:
        return self.__serializationExpose

    @serializationExpose.setter
    def serializationExpose(self, serializationExpose: bool):
        self.__serializationExpose = serializationExpose

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def collectionAllowRemove(self) -> bool:
        return self.__collectionAllowRemove

    @collectionAllowRemove.setter
    def collectionAllowRemove(self, collectionAllowRemove: bool):
        self.__collectionAllowRemove = collectionAllowRemove

    @property
    def serializationGroups(self) -> str:
        return self.__serializationGroups

    @serializationGroups.setter
    def serializationGroups(self, serializationGroups: str):
        self.__serializationGroups = serializationGroups

    @property
    def collectionAllowAdd(self) -> bool:
        return self.__collectionAllowAdd

    @collectionAllowAdd.setter
    def collectionAllowAdd(self, collectionAllowAdd: bool):
        self.__collectionAllowAdd = collectionAllowAdd

    @property
    def nullDisplayValue(self) -> str:
        return self.__nullDisplayValue

    @nullDisplayValue.setter
    def nullDisplayValue(self, nullDisplayValue: str):
        self.__nullDisplayValue = nullDisplayValue

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def website_Feature35(self):
        return self.__website_Feature35

    @website_Feature35.setter
    def website_Feature35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature35", None)
        self.__website_Feature35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView34"):
                opp_val = getattr(old_value, "website_EntityOrView34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView34"):
                opp_val = getattr(value, "website_EntityOrView34", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature38(self):
        return self.__website_Feature38

    @website_Feature38.setter
    def website_Feature38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature38", None)
        self.__website_Feature38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView37"):
                opp_val = getattr(old_value, "website_EntityOrView37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView37"):
                opp_val = getattr(value, "website_EntityOrView37", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature113(self):
        return self.__website_Feature113

    @website_Feature113.setter
    def website_Feature113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature113", None)
        self.__website_Feature113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Selection"):
                opp_val = getattr(old_value, "website_Selection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Selection"):
                opp_val = getattr(value, "website_Selection", None)
                if opp_val is None:
                    setattr(value, "website_Selection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature43(self):
        return self.__website_Feature43

    @website_Feature43.setter
    def website_Feature43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature43", None)
        self.__website_Feature43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView42"):
                opp_val = getattr(old_value, "website_EntityOrView42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView42"):
                opp_val = getattr(value, "website_EntityOrView42", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature209(self):
        return self.__website_Feature209

    @website_Feature209.setter
    def website_Feature209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature209", None)
        self.__website_Feature209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_CollectionUnit208"):
                opp_val = getattr(old_value, "website_CollectionUnit208", None)
                if opp_val == self:
                    setattr(old_value, "website_CollectionUnit208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_CollectionUnit208"):
                opp_val = getattr(value, "website_CollectionUnit208", None)
                setattr(value, "website_CollectionUnit208", self)

    @property
    def website_Feature46(self):
        return self.__website_Feature46

    @website_Feature46.setter
    def website_Feature46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature46", None)
        self.__website_Feature46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView45"):
                opp_val = getattr(old_value, "website_EntityOrView45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView45"):
                opp_val = getattr(value, "website_EntityOrView45", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature(self):
        return self.__website_Feature

    @website_Feature.setter
    def website_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature", None)
        self.__website_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView32"):
                opp_val = getattr(old_value, "website_EntityOrView32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView32"):
                opp_val = getattr(value, "website_EntityOrView32", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Feature289(self):
        return self.__website_Feature289

    @website_Feature289.setter
    def website_Feature289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Feature__website_Feature289", None)
        self.__website_Feature289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeatureReference"):
                opp_val = getattr(old_value, "website_FeatureReference", None)
                if opp_val == self:
                    setattr(old_value, "website_FeatureReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeatureReference"):
                opp_val = getattr(value, "website_FeatureReference", None)
                setattr(value, "website_FeatureReference", self)

class DataType:

    pass
class website_EnumerationType(DataType):

    pass
class Classifier:

    pass
class website_DataType(Classifier):

    def __init__(self, persistentType: str, ormType: str, interfaceType: str, placeholder: str, validationPattern: str, website_DataType: "website_DataTypeAttribute" = None, website_DataType158: "website_FilterParameter" = None, website_DataType200: "website_DataTypeField" = None):
        self.persistentType = persistentType
        self.ormType = ormType
        self.interfaceType = interfaceType
        self.placeholder = placeholder
        self.validationPattern = validationPattern
        self.website_DataType = website_DataType
        self.website_DataType158 = website_DataType158
        self.website_DataType200 = website_DataType200
        
    @property
    def persistentType(self) -> str:
        return self.__persistentType

    @persistentType.setter
    def persistentType(self, persistentType: str):
        self.__persistentType = persistentType

    @property
    def ormType(self) -> str:
        return self.__ormType

    @ormType.setter
    def ormType(self, ormType: str):
        self.__ormType = ormType

    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def website_DataType200(self):
        return self.__website_DataType200

    @website_DataType200.setter
    def website_DataType200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DataType__website_DataType200", None)
        self.__website_DataType200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataTypeField"):
                opp_val = getattr(old_value, "website_DataTypeField", None)
                if opp_val == self:
                    setattr(old_value, "website_DataTypeField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataTypeField"):
                opp_val = getattr(value, "website_DataTypeField", None)
                setattr(value, "website_DataTypeField", self)

    @property
    def website_DataType158(self):
        return self.__website_DataType158

    @website_DataType158.setter
    def website_DataType158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DataType__website_DataType158", None)
        self.__website_DataType158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FilterParameter157"):
                opp_val = getattr(old_value, "website_FilterParameter157", None)
                if opp_val == self:
                    setattr(old_value, "website_FilterParameter157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FilterParameter157"):
                opp_val = getattr(value, "website_FilterParameter157", None)
                setattr(value, "website_FilterParameter157", self)

    @property
    def website_DataType(self):
        return self.__website_DataType

    @website_DataType.setter
    def website_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_DataType__website_DataType", None)
        self.__website_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataTypeAttribute"):
                opp_val = getattr(old_value, "website_DataTypeAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_DataTypeAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataTypeAttribute"):
                opp_val = getattr(value, "website_DataTypeAttribute", None)
                setattr(value, "website_DataTypeAttribute", self)

class NamedDisplayElement:

    pass
class website_EditStaticTextMenuEntry(NamedDisplayElement, MenuEntry):

    pass
class website_ActionMenuEntry(NamedDisplayElement, MenuEntry):

    pass
class website_ContentUnit(NamedDisplayElement):

    def __init__(self, createDefaultUriElement: bool, requiresRole: str, purposeSummary: str, uriElement: str, alternative: str, omitCaption: bool, captionClass: str, website_ContentUnit: "website_ActionMenuEntry" = None, ContentUnit: "website_UnitContainer" = None, units: "website_UnitContainer" = None):
        self.createDefaultUriElement = createDefaultUriElement
        self.requiresRole = requiresRole
        self.purposeSummary = purposeSummary
        self.uriElement = uriElement
        self.alternative = alternative
        self.omitCaption = omitCaption
        self.captionClass = captionClass
        self.website_ContentUnit = website_ContentUnit
        self.ContentUnit = ContentUnit
        self.units = units
        
    @property
    def createDefaultUriElement(self) -> bool:
        return self.__createDefaultUriElement

    @createDefaultUriElement.setter
    def createDefaultUriElement(self, createDefaultUriElement: bool):
        self.__createDefaultUriElement = createDefaultUriElement

    @property
    def omitCaption(self) -> bool:
        return self.__omitCaption

    @omitCaption.setter
    def omitCaption(self, omitCaption: bool):
        self.__omitCaption = omitCaption

    @property
    def captionClass(self) -> str:
        return self.__captionClass

    @captionClass.setter
    def captionClass(self, captionClass: str):
        self.__captionClass = captionClass

    @property
    def uriElement(self) -> str:
        return self.__uriElement

    @uriElement.setter
    def uriElement(self, uriElement: str):
        self.__uriElement = uriElement

    @property
    def alternative(self) -> str:
        return self.__alternative

    @alternative.setter
    def alternative(self, alternative: str):
        self.__alternative = alternative

    @property
    def purposeSummary(self) -> str:
        return self.__purposeSummary

    @purposeSummary.setter
    def purposeSummary(self, purposeSummary: str):
        self.__purposeSummary = purposeSummary

    @property
    def requiresRole(self) -> str:
        return self.__requiresRole

    @requiresRole.setter
    def requiresRole(self, requiresRole: str):
        self.__requiresRole = requiresRole

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ContentUnit__units", None)
        self.__units = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnitContainer"):
                opp_val = getattr(old_value, "UnitContainer", None)
                if opp_val == self:
                    setattr(old_value, "UnitContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnitContainer"):
                opp_val = getattr(value, "UnitContainer", None)
                setattr(value, "UnitContainer", self)

    @property
    def ContentUnit(self):
        return self.__ContentUnit

    @ContentUnit.setter
    def ContentUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ContentUnit__ContentUnit", None)
        self.__ContentUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "displayedOn"):
                opp_val = getattr(old_value, "displayedOn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "displayedOn"):
                opp_val = getattr(value, "displayedOn", None)
                if opp_val is None:
                    setattr(value, "displayedOn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_ContentUnit(self):
        return self.__website_ContentUnit

    @website_ContentUnit.setter
    def website_ContentUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ContentUnit__website_ContentUnit", None)
        self.__website_ContentUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ActionMenuEntry"):
                opp_val = getattr(old_value, "website_ActionMenuEntry", None)
                if opp_val == self:
                    setattr(old_value, "website_ActionMenuEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ActionMenuEntry"):
                opp_val = getattr(value, "website_ActionMenuEntry", None)
                setattr(value, "website_ActionMenuEntry", self)

class website_EnumerationLiteral(NamedDisplayElement):

    pass
class website_InterfaceField(NamedDisplayElement, UnitField):

    def __init__(self, inputClass: str, placeholder: str, validationPattern: str, required: bool, defaultValue: str, website_InterfaceField: "website_UnitField" = None):
        self.inputClass = inputClass
        self.placeholder = placeholder
        self.validationPattern = validationPattern
        self.required = required
        self.defaultValue = defaultValue
        self.website_InterfaceField = website_InterfaceField
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def website_InterfaceField(self):
        return self.__website_InterfaceField

    @website_InterfaceField.setter
    def website_InterfaceField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_InterfaceField__website_InterfaceField", None)
        self.__website_InterfaceField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_UnitField"):
                opp_val = getattr(old_value, "website_UnitField", None)
                if opp_val == self:
                    setattr(old_value, "website_UnitField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_UnitField"):
                opp_val = getattr(value, "website_UnitField", None)
                setattr(value, "website_UnitField", self)

class website_InlineAction(NamedDisplayElement):

    def __init__(self, disable: bool, requiresRole: str, header: str, footer: str, headerClass: str, footerClass: str, InlineAction: "website_InlineActionContainer" = None, actions: "website_InlineActionContainer" = None, website_InlineAction: "website_Predicate" = None, website_InlineAction278: "website_Predicate" = None):
        self.disable = disable
        self.requiresRole = requiresRole
        self.header = header
        self.footer = footer
        self.headerClass = headerClass
        self.footerClass = footerClass
        self.InlineAction = InlineAction
        self.actions = actions
        self.website_InlineAction = website_InlineAction
        self.website_InlineAction278 = website_InlineAction278
        
    @property
    def requiresRole(self) -> str:
        return self.__requiresRole

    @requiresRole.setter
    def requiresRole(self, requiresRole: str):
        self.__requiresRole = requiresRole

    @property
    def disable(self) -> bool:
        return self.__disable

    @disable.setter
    def disable(self, disable: bool):
        self.__disable = disable

    @property
    def footer(self) -> str:
        return self.__footer

    @footer.setter
    def footer(self, footer: str):
        self.__footer = footer

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def website_InlineAction278(self):
        return self.__website_InlineAction278

    @website_InlineAction278.setter
    def website_InlineAction278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_InlineAction__website_InlineAction278", None)
        self.__website_InlineAction278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Predicate279"):
                opp_val = getattr(old_value, "website_Predicate279", None)
                if opp_val == self:
                    setattr(old_value, "website_Predicate279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Predicate279"):
                opp_val = getattr(value, "website_Predicate279", None)
                setattr(value, "website_Predicate279", self)

    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_InlineAction__actions", None)
        self.__actions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InlineActionContainer"):
                opp_val = getattr(old_value, "InlineActionContainer", None)
                if opp_val == self:
                    setattr(old_value, "InlineActionContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InlineActionContainer"):
                opp_val = getattr(value, "InlineActionContainer", None)
                setattr(value, "InlineActionContainer", self)

    @property
    def website_InlineAction(self):
        return self.__website_InlineAction

    @website_InlineAction.setter
    def website_InlineAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_InlineAction__website_InlineAction", None)
        self.__website_InlineAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Predicate276"):
                opp_val = getattr(old_value, "website_Predicate276", None)
                if opp_val == self:
                    setattr(old_value, "website_Predicate276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Predicate276"):
                opp_val = getattr(value, "website_Predicate276", None)
                setattr(value, "website_Predicate276", self)

    @property
    def InlineAction(self):
        return self.__InlineAction

    @InlineAction.setter
    def InlineAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_InlineAction__InlineAction", None)
        self.__InlineAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedBy273"):
                opp_val = getattr(old_value, "usedBy273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedBy273"):
                opp_val = getattr(value, "usedBy273", None)
                if opp_val is None:
                    setattr(value, "usedBy273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class website_UnitSupportAction(NamedDisplayElement):

    def __init__(self, disable: bool, confirmMessage: str, website_UnitSupportAction: "website_DynamicUnit" = None):
        self.disable = disable
        self.confirmMessage = confirmMessage
        self.website_UnitSupportAction = website_UnitSupportAction
        
    @property
    def confirmMessage(self) -> str:
        return self.__confirmMessage

    @confirmMessage.setter
    def confirmMessage(self, confirmMessage: str):
        self.__confirmMessage = confirmMessage

    @property
    def disable(self) -> bool:
        return self.__disable

    @disable.setter
    def disable(self, disable: bool):
        self.__disable = disable

    @property
    def website_UnitSupportAction(self):
        return self.__website_UnitSupportAction

    @website_UnitSupportAction.setter
    def website_UnitSupportAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_UnitSupportAction__website_UnitSupportAction", None)
        self.__website_UnitSupportAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DynamicUnit174"):
                opp_val = getattr(old_value, "website_DynamicUnit174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DynamicUnit174"):
                opp_val = getattr(value, "website_DynamicUnit174", None)
                if opp_val is None:
                    setattr(value, "website_DynamicUnit174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class website_ViewAssociation(ViewFeature, Association, NamedDisplayElement):

    def __init__(self, cardinality: str, website_ViewAssociation: "website_EncapsulatedAssociation" = None):
        self.cardinality = cardinality
        self.website_ViewAssociation = website_ViewAssociation
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def website_ViewAssociation(self):
        return self.__website_ViewAssociation

    @website_ViewAssociation.setter
    def website_ViewAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ViewAssociation__website_ViewAssociation", None)
        self.__website_ViewAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EncapsulatedAssociation104"):
                opp_val = getattr(old_value, "website_EncapsulatedAssociation104", None)
                if opp_val == self:
                    setattr(old_value, "website_EncapsulatedAssociation104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EncapsulatedAssociation104"):
                opp_val = getattr(value, "website_EncapsulatedAssociation104", None)
                setattr(value, "website_EncapsulatedAssociation104", self)

class website_Filter(NamedDisplayElement):

    pass
class website_EntityFeature(NamedDisplayElement, Feature):

    def __init__(self, cardinality: str, unique: bool, ordered: bool, booleanIsHasChoice: str, singletonName: str, pluralisedName: str, columnName: str, EntityFeature: "website_Entity" = None, entityFeatures: "website_Entity" = None, website_EntityFeature: "website_AssociationKey" = None, website_EntityFeature87: "website_AssociationKey" = None):
        self.cardinality = cardinality
        self.unique = unique
        self.ordered = ordered
        self.booleanIsHasChoice = booleanIsHasChoice
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.columnName = columnName
        self.EntityFeature = EntityFeature
        self.entityFeatures = entityFeatures
        self.website_EntityFeature = website_EntityFeature
        self.website_EntityFeature87 = website_EntityFeature87
        
    @property
    def singletonName(self) -> str:
        return self.__singletonName

    @singletonName.setter
    def singletonName(self, singletonName: str):
        self.__singletonName = singletonName

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def booleanIsHasChoice(self) -> str:
        return self.__booleanIsHasChoice

    @booleanIsHasChoice.setter
    def booleanIsHasChoice(self, booleanIsHasChoice: str):
        self.__booleanIsHasChoice = booleanIsHasChoice

    @property
    def pluralisedName(self) -> str:
        return self.__pluralisedName

    @pluralisedName.setter
    def pluralisedName(self, pluralisedName: str):
        self.__pluralisedName = pluralisedName

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def EntityFeature(self):
        return self.__EntityFeature

    @EntityFeature.setter
    def EntityFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityFeature__EntityFeature", None)
        self.__EntityFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf74"):
                opp_val = getattr(old_value, "partOf74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf74"):
                opp_val = getattr(value, "partOf74", None)
                if opp_val is None:
                    setattr(value, "partOf74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EntityFeature(self):
        return self.__website_EntityFeature

    @website_EntityFeature.setter
    def website_EntityFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityFeature__website_EntityFeature", None)
        self.__website_EntityFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_AssociationKey"):
                opp_val = getattr(old_value, "website_AssociationKey", None)
                if opp_val == self:
                    setattr(old_value, "website_AssociationKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_AssociationKey"):
                opp_val = getattr(value, "website_AssociationKey", None)
                setattr(value, "website_AssociationKey", self)

    @property
    def entityFeatures(self):
        return self.__entityFeatures

    @entityFeatures.setter
    def entityFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityFeature__entityFeatures", None)
        self.__entityFeatures = value
        
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

    @property
    def website_EntityFeature87(self):
        return self.__website_EntityFeature87

    @website_EntityFeature87.setter
    def website_EntityFeature87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityFeature__website_EntityFeature87", None)
        self.__website_EntityFeature87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_AssociationKey86"):
                opp_val = getattr(old_value, "website_AssociationKey86", None)
                if opp_val == self:
                    setattr(old_value, "website_AssociationKey86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_AssociationKey86"):
                opp_val = getattr(value, "website_AssociationKey86", None)
                setattr(value, "website_AssociationKey86", self)

class NamedElement:

    pass
class website_FilterParameter(NamedElement):

    def __init__(self, defaultValue: str, placeholder: str, website_FilterParameter: "website_SelectionParameter" = None, website_FilterParameter157: "website_DataType" = None, FilterParameter: "website_Filter" = None, parameters154: "website_Filter" = None, website_FilterParameter166: "website_QueryParameter" = None):
        self.defaultValue = defaultValue
        self.placeholder = placeholder
        self.website_FilterParameter = website_FilterParameter
        self.website_FilterParameter157 = website_FilterParameter157
        self.FilterParameter = FilterParameter
        self.parameters154 = parameters154
        self.website_FilterParameter166 = website_FilterParameter166
        
    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def website_FilterParameter157(self):
        return self.__website_FilterParameter157

    @website_FilterParameter157.setter
    def website_FilterParameter157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FilterParameter__website_FilterParameter157", None)
        self.__website_FilterParameter157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataType158"):
                opp_val = getattr(old_value, "website_DataType158", None)
                if opp_val == self:
                    setattr(old_value, "website_DataType158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataType158"):
                opp_val = getattr(value, "website_DataType158", None)
                setattr(value, "website_DataType158", self)

    @property
    def website_FilterParameter166(self):
        return self.__website_FilterParameter166

    @website_FilterParameter166.setter
    def website_FilterParameter166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FilterParameter__website_FilterParameter166", None)
        self.__website_FilterParameter166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_QueryParameter165"):
                opp_val = getattr(old_value, "website_QueryParameter165", None)
                if opp_val == self:
                    setattr(old_value, "website_QueryParameter165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_QueryParameter165"):
                opp_val = getattr(value, "website_QueryParameter165", None)
                setattr(value, "website_QueryParameter165", self)

    @property
    def website_FilterParameter(self):
        return self.__website_FilterParameter

    @website_FilterParameter.setter
    def website_FilterParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FilterParameter__website_FilterParameter", None)
        self.__website_FilterParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_SelectionParameter"):
                opp_val = getattr(old_value, "website_SelectionParameter", None)
                if opp_val == self:
                    setattr(old_value, "website_SelectionParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_SelectionParameter"):
                opp_val = getattr(value, "website_SelectionParameter", None)
                setattr(value, "website_SelectionParameter", self)

    @property
    def FilterParameter(self):
        return self.__FilterParameter

    @FilterParameter.setter
    def FilterParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FilterParameter__FilterParameter", None)
        self.__FilterParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf150"):
                opp_val = getattr(old_value, "partOf150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf150"):
                opp_val = getattr(value, "partOf150", None)
                if opp_val is None:
                    setattr(value, "partOf150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters154(self):
        return self.__parameters154

    @parameters154.setter
    def parameters154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_FilterParameter__parameters154", None)
        self.__parameters154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Filter"):
                opp_val = getattr(old_value, "Filter", None)
                if opp_val == self:
                    setattr(old_value, "Filter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Filter"):
                opp_val = getattr(value, "Filter", None)
                setattr(value, "Filter", self)

class website_BusinessOperation(NamedElement):

    def __init__(self, resultType: str, resultMimeType: str, website_BusinessOperation125: set["website_Service"] = None, website_BusinessOperation: "website_Service" = None, website_BusinessOperation285: "website_FeatureSupportAction" = None):
        self.resultType = resultType
        self.resultMimeType = resultMimeType
        self.website_BusinessOperation125 = website_BusinessOperation125 if website_BusinessOperation125 is not None else set()
        self.website_BusinessOperation = website_BusinessOperation
        self.website_BusinessOperation285 = website_BusinessOperation285
        
    @property
    def resultType(self) -> str:
        return self.__resultType

    @resultType.setter
    def resultType(self, resultType: str):
        self.__resultType = resultType

    @property
    def resultMimeType(self) -> str:
        return self.__resultMimeType

    @resultMimeType.setter
    def resultMimeType(self, resultMimeType: str):
        self.__resultMimeType = resultMimeType

    @property
    def website_BusinessOperation(self):
        return self.__website_BusinessOperation

    @website_BusinessOperation.setter
    def website_BusinessOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_BusinessOperation__website_BusinessOperation", None)
        self.__website_BusinessOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Service109"):
                opp_val = getattr(old_value, "website_Service109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Service109"):
                opp_val = getattr(value, "website_Service109", None)
                if opp_val is None:
                    setattr(value, "website_Service109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_BusinessOperation285(self):
        return self.__website_BusinessOperation285

    @website_BusinessOperation285.setter
    def website_BusinessOperation285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_BusinessOperation__website_BusinessOperation285", None)
        self.__website_BusinessOperation285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeatureSupportAction"):
                opp_val = getattr(old_value, "website_FeatureSupportAction", None)
                if opp_val == self:
                    setattr(old_value, "website_FeatureSupportAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeatureSupportAction"):
                opp_val = getattr(value, "website_FeatureSupportAction", None)
                setattr(value, "website_FeatureSupportAction", self)

    @property
    def website_BusinessOperation125(self):
        return self.__website_BusinessOperation125

    @website_BusinessOperation125.setter
    def website_BusinessOperation125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_BusinessOperation__website_BusinessOperation125", None)
        self.__website_BusinessOperation125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Service126"):
                    opp_val = getattr(item, "website_Service126", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Service126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Service126"):
                    opp_val = getattr(item, "website_Service126", None)
                    
                    setattr(item, "website_Service126", self)
                    

class website_Selection(NamedElement):

    def __init__(self, distinct: bool, limit: int, selected: bool, Selection: "website_Service" = None, selections: "website_Service" = None, website_Selection: set["website_Feature"] = None, formalFor: set["website_SelectionParameter"] = None, website_Selection116: set["website_Association"] = None, website_Selection119: "website_Predicate" = None, website_Selection121: set["website_Order"] = None, Selection123: "website_SelectionParameter" = None, website_Selection146: "website_DynamicMenu" = None, website_Selection152: "website_Filter" = None, website_Selection190: "website_UnitAssociation" = None, website_Selection212: "website_CollectionUnit" = None, website_Selection220: "website_EditUnit" = None, website_Selection238: "website_DataUnit" = None, website_Selection246: "website_ImageUnit" = None):
        self.distinct = distinct
        self.limit = limit
        self.selected = selected
        self.Selection = Selection
        self.selections = selections
        self.website_Selection = website_Selection if website_Selection is not None else set()
        self.formalFor = formalFor if formalFor is not None else set()
        self.website_Selection116 = website_Selection116 if website_Selection116 is not None else set()
        self.website_Selection119 = website_Selection119
        self.website_Selection121 = website_Selection121 if website_Selection121 is not None else set()
        self.Selection123 = Selection123
        self.website_Selection146 = website_Selection146
        self.website_Selection152 = website_Selection152
        self.website_Selection190 = website_Selection190
        self.website_Selection212 = website_Selection212
        self.website_Selection220 = website_Selection220
        self.website_Selection238 = website_Selection238
        self.website_Selection246 = website_Selection246
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def Selection(self):
        return self.__Selection

    @Selection.setter
    def Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__Selection", None)
        self.__Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedBy"):
                opp_val = getattr(old_value, "usedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedBy"):
                opp_val = getattr(value, "usedBy", None)
                if opp_val is None:
                    setattr(value, "usedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Selection246(self):
        return self.__website_Selection246

    @website_Selection246.setter
    def website_Selection246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection246", None)
        self.__website_Selection246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ImageUnit"):
                opp_val = getattr(old_value, "website_ImageUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_ImageUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ImageUnit"):
                opp_val = getattr(value, "website_ImageUnit", None)
                setattr(value, "website_ImageUnit", self)

    @property
    def website_Selection190(self):
        return self.__website_Selection190

    @website_Selection190.setter
    def website_Selection190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection190", None)
        self.__website_Selection190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_UnitAssociation189"):
                opp_val = getattr(old_value, "website_UnitAssociation189", None)
                if opp_val == self:
                    setattr(old_value, "website_UnitAssociation189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_UnitAssociation189"):
                opp_val = getattr(value, "website_UnitAssociation189", None)
                setattr(value, "website_UnitAssociation189", self)

    @property
    def website_Selection238(self):
        return self.__website_Selection238

    @website_Selection238.setter
    def website_Selection238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection238", None)
        self.__website_Selection238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DataUnit"):
                opp_val = getattr(old_value, "website_DataUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_DataUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DataUnit"):
                opp_val = getattr(value, "website_DataUnit", None)
                setattr(value, "website_DataUnit", self)

    @property
    def website_Selection152(self):
        return self.__website_Selection152

    @website_Selection152.setter
    def website_Selection152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection152", None)
        self.__website_Selection152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Filter"):
                opp_val = getattr(old_value, "website_Filter", None)
                if opp_val == self:
                    setattr(old_value, "website_Filter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Filter"):
                opp_val = getattr(value, "website_Filter", None)
                setattr(value, "website_Filter", self)

    @property
    def formalFor(self):
        return self.__formalFor

    @formalFor.setter
    def formalFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__formalFor", None)
        self.__formalFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SelectionParameter"):
                    opp_val = getattr(item, "SelectionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "SelectionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SelectionParameter"):
                    opp_val = getattr(item, "SelectionParameter", None)
                    
                    setattr(item, "SelectionParameter", self)
                    

    @property
    def website_Selection212(self):
        return self.__website_Selection212

    @website_Selection212.setter
    def website_Selection212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection212", None)
        self.__website_Selection212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_CollectionUnit211"):
                opp_val = getattr(old_value, "website_CollectionUnit211", None)
                if opp_val == self:
                    setattr(old_value, "website_CollectionUnit211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_CollectionUnit211"):
                opp_val = getattr(value, "website_CollectionUnit211", None)
                setattr(value, "website_CollectionUnit211", self)

    @property
    def selections(self):
        return self.__selections

    @selections.setter
    def selections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__selections", None)
        self.__selections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service111"):
                opp_val = getattr(old_value, "Service111", None)
                if opp_val == self:
                    setattr(old_value, "Service111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service111"):
                opp_val = getattr(value, "Service111", None)
                setattr(value, "Service111", self)

    @property
    def website_Selection116(self):
        return self.__website_Selection116

    @website_Selection116.setter
    def website_Selection116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection116", None)
        self.__website_Selection116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Association117"):
                    opp_val = getattr(item, "website_Association117", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Association117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Association117"):
                    opp_val = getattr(item, "website_Association117", None)
                    
                    setattr(item, "website_Association117", self)
                    

    @property
    def website_Selection(self):
        return self.__website_Selection

    @website_Selection.setter
    def website_Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection", None)
        self.__website_Selection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature113"):
                    opp_val = getattr(item, "website_Feature113", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature113"):
                    opp_val = getattr(item, "website_Feature113", None)
                    
                    setattr(item, "website_Feature113", self)
                    

    @property
    def website_Selection121(self):
        return self.__website_Selection121

    @website_Selection121.setter
    def website_Selection121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection121", None)
        self.__website_Selection121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Order"):
                    opp_val = getattr(item, "website_Order", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Order", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Order"):
                    opp_val = getattr(item, "website_Order", None)
                    
                    setattr(item, "website_Order", self)
                    

    @property
    def website_Selection119(self):
        return self.__website_Selection119

    @website_Selection119.setter
    def website_Selection119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection119", None)
        self.__website_Selection119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Predicate"):
                opp_val = getattr(old_value, "website_Predicate", None)
                if opp_val == self:
                    setattr(old_value, "website_Predicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Predicate"):
                opp_val = getattr(value, "website_Predicate", None)
                setattr(value, "website_Predicate", self)

    @property
    def website_Selection220(self):
        return self.__website_Selection220

    @website_Selection220.setter
    def website_Selection220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection220", None)
        self.__website_Selection220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EditUnit"):
                opp_val = getattr(old_value, "website_EditUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_EditUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EditUnit"):
                opp_val = getattr(value, "website_EditUnit", None)
                setattr(value, "website_EditUnit", self)

    @property
    def Selection123(self):
        return self.__Selection123

    @Selection123.setter
    def Selection123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__Selection123", None)
        self.__Selection123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def website_Selection146(self):
        return self.__website_Selection146

    @website_Selection146.setter
    def website_Selection146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Selection__website_Selection146", None)
        self.__website_Selection146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DynamicMenu145"):
                opp_val = getattr(old_value, "website_DynamicMenu145", None)
                if opp_val == self:
                    setattr(old_value, "website_DynamicMenu145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DynamicMenu145"):
                opp_val = getattr(value, "website_DynamicMenu145", None)
                setattr(value, "website_DynamicMenu145", self)

class website_SelectionParameter(NamedElement):

    def __init__(self, optional: bool, defaultValue: str, SelectionParameter: "website_Selection" = None, parameters: "website_Selection" = None, website_SelectionParameter: "website_FilterParameter" = None, website_SelectionParameter293: "website_ParameterReference" = None):
        self.optional = optional
        self.defaultValue = defaultValue
        self.SelectionParameter = SelectionParameter
        self.parameters = parameters
        self.website_SelectionParameter = website_SelectionParameter
        self.website_SelectionParameter293 = website_SelectionParameter293
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def website_SelectionParameter(self):
        return self.__website_SelectionParameter

    @website_SelectionParameter.setter
    def website_SelectionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_SelectionParameter__website_SelectionParameter", None)
        self.__website_SelectionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FilterParameter"):
                opp_val = getattr(old_value, "website_FilterParameter", None)
                if opp_val == self:
                    setattr(old_value, "website_FilterParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FilterParameter"):
                opp_val = getattr(value, "website_FilterParameter", None)
                setattr(value, "website_FilterParameter", self)

    @property
    def website_SelectionParameter293(self):
        return self.__website_SelectionParameter293

    @website_SelectionParameter293.setter
    def website_SelectionParameter293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_SelectionParameter__website_SelectionParameter293", None)
        self.__website_SelectionParameter293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ParameterReference"):
                opp_val = getattr(old_value, "website_ParameterReference", None)
                if opp_val == self:
                    setattr(old_value, "website_ParameterReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ParameterReference"):
                opp_val = getattr(value, "website_ParameterReference", None)
                setattr(value, "website_ParameterReference", self)

    @property
    def SelectionParameter(self):
        return self.__SelectionParameter

    @SelectionParameter.setter
    def SelectionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_SelectionParameter__SelectionParameter", None)
        self.__SelectionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalFor"):
                opp_val = getattr(old_value, "formalFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalFor"):
                opp_val = getattr(value, "formalFor", None)
                if opp_val is None:
                    setattr(value, "formalFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_SelectionParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selection123"):
                opp_val = getattr(old_value, "Selection123", None)
                if opp_val == self:
                    setattr(old_value, "Selection123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selection123"):
                opp_val = getattr(value, "Selection123", None)
                setattr(value, "Selection123", self)

class website_NamedDisplayElement(NamedElement):

    def __init__(self, displayLabel: str):
        self.displayLabel = displayLabel
        
    @property
    def displayLabel(self) -> str:
        return self.__displayLabel

    @displayLabel.setter
    def displayLabel(self, displayLabel: str):
        self.__displayLabel = displayLabel

class website_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class website_ModelLabel(Label, NamedElement):

    def __init__(self, format: str, ModelLabel: "website_EntityOrView" = None, labels: "website_EntityOrView" = None, partOf: set["website_ModelLabelFeature"] = None, ModelLabel67: "website_ModelLabelFeature" = None, website_ModelLabel: "website_ModelLabelAssociation" = None):
        self.format = format
        self.ModelLabel = ModelLabel
        self.labels = labels
        self.partOf = partOf if partOf is not None else set()
        self.ModelLabel67 = ModelLabel67
        self.website_ModelLabel = website_ModelLabel
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def ModelLabel67(self):
        return self.__ModelLabel67

    @ModelLabel67.setter
    def ModelLabel67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabel__ModelLabel67", None)
        self.__ModelLabel67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabel__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityOrView"):
                opp_val = getattr(old_value, "EntityOrView", None)
                if opp_val == self:
                    setattr(old_value, "EntityOrView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityOrView"):
                opp_val = getattr(value, "EntityOrView", None)
                setattr(value, "EntityOrView", self)

    @property
    def website_ModelLabel(self):
        return self.__website_ModelLabel

    @website_ModelLabel.setter
    def website_ModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabel__website_ModelLabel", None)
        self.__website_ModelLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ModelLabelAssociation72"):
                opp_val = getattr(old_value, "website_ModelLabelAssociation72", None)
                if opp_val == self:
                    setattr(old_value, "website_ModelLabelAssociation72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ModelLabelAssociation72"):
                opp_val = getattr(value, "website_ModelLabelAssociation72", None)
                setattr(value, "website_ModelLabelAssociation72", self)

    @property
    def ModelLabel(self):
        return self.__ModelLabel

    @ModelLabel.setter
    def ModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabel__ModelLabel", None)
        self.__ModelLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labelFor"):
                opp_val = getattr(old_value, "labelFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labelFor"):
                opp_val = getattr(value, "labelFor", None)
                if opp_val is None:
                    setattr(value, "labelFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def partOf(self):
        return self.__partOf

    @partOf.setter
    def partOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ModelLabel__partOf", None)
        self.__partOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelLabelFeature"):
                    opp_val = getattr(item, "ModelLabelFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelLabelFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelLabelFeature"):
                    opp_val = getattr(item, "ModelLabelFeature", None)
                    
                    setattr(item, "ModelLabelFeature", self)
                    

class Authentication:

    pass
class website_CasAuthentication(Authentication):

    pass
class website_LocalAuthenticationSystem(Authentication):

    def __init__(self, useEmailActivation: bool, sendWelcomeEmail: bool, authenticationKey: str, useCaptcha: bool, allowRememberMe: bool, allowSelfRegistration: bool, trackLoginAttempts: bool, website_LocalAuthenticationSystem25: "website_RegistrationUnit" = None, website_LocalAuthenticationSystem27: "website_LoginUnit" = None, website_LocalAuthenticationSystem: "website_EntityOrView" = None, website_LocalAuthenticationSystem29: "website_ForgottenPasswordUnit" = None):
        self.useEmailActivation = useEmailActivation
        self.sendWelcomeEmail = sendWelcomeEmail
        self.authenticationKey = authenticationKey
        self.useCaptcha = useCaptcha
        self.allowRememberMe = allowRememberMe
        self.allowSelfRegistration = allowSelfRegistration
        self.trackLoginAttempts = trackLoginAttempts
        self.website_LocalAuthenticationSystem25 = website_LocalAuthenticationSystem25
        self.website_LocalAuthenticationSystem27 = website_LocalAuthenticationSystem27
        self.website_LocalAuthenticationSystem = website_LocalAuthenticationSystem
        self.website_LocalAuthenticationSystem29 = website_LocalAuthenticationSystem29
        
    @property
    def allowRememberMe(self) -> bool:
        return self.__allowRememberMe

    @allowRememberMe.setter
    def allowRememberMe(self, allowRememberMe: bool):
        self.__allowRememberMe = allowRememberMe

    @property
    def trackLoginAttempts(self) -> bool:
        return self.__trackLoginAttempts

    @trackLoginAttempts.setter
    def trackLoginAttempts(self, trackLoginAttempts: bool):
        self.__trackLoginAttempts = trackLoginAttempts

    @property
    def sendWelcomeEmail(self) -> bool:
        return self.__sendWelcomeEmail

    @sendWelcomeEmail.setter
    def sendWelcomeEmail(self, sendWelcomeEmail: bool):
        self.__sendWelcomeEmail = sendWelcomeEmail

    @property
    def useEmailActivation(self) -> bool:
        return self.__useEmailActivation

    @useEmailActivation.setter
    def useEmailActivation(self, useEmailActivation: bool):
        self.__useEmailActivation = useEmailActivation

    @property
    def authenticationKey(self) -> str:
        return self.__authenticationKey

    @authenticationKey.setter
    def authenticationKey(self, authenticationKey: str):
        self.__authenticationKey = authenticationKey

    @property
    def allowSelfRegistration(self) -> bool:
        return self.__allowSelfRegistration

    @allowSelfRegistration.setter
    def allowSelfRegistration(self, allowSelfRegistration: bool):
        self.__allowSelfRegistration = allowSelfRegistration

    @property
    def useCaptcha(self) -> bool:
        return self.__useCaptcha

    @useCaptcha.setter
    def useCaptcha(self, useCaptcha: bool):
        self.__useCaptcha = useCaptcha

    @property
    def website_LocalAuthenticationSystem27(self):
        return self.__website_LocalAuthenticationSystem27

    @website_LocalAuthenticationSystem27.setter
    def website_LocalAuthenticationSystem27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_LocalAuthenticationSystem__website_LocalAuthenticationSystem27", None)
        self.__website_LocalAuthenticationSystem27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LoginUnit"):
                opp_val = getattr(old_value, "website_LoginUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_LoginUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LoginUnit"):
                opp_val = getattr(value, "website_LoginUnit", None)
                setattr(value, "website_LoginUnit", self)

    @property
    def website_LocalAuthenticationSystem29(self):
        return self.__website_LocalAuthenticationSystem29

    @website_LocalAuthenticationSystem29.setter
    def website_LocalAuthenticationSystem29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_LocalAuthenticationSystem__website_LocalAuthenticationSystem29", None)
        self.__website_LocalAuthenticationSystem29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ForgottenPasswordUnit"):
                opp_val = getattr(old_value, "website_ForgottenPasswordUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_ForgottenPasswordUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ForgottenPasswordUnit"):
                opp_val = getattr(value, "website_ForgottenPasswordUnit", None)
                setattr(value, "website_ForgottenPasswordUnit", self)

    @property
    def website_LocalAuthenticationSystem25(self):
        return self.__website_LocalAuthenticationSystem25

    @website_LocalAuthenticationSystem25.setter
    def website_LocalAuthenticationSystem25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_LocalAuthenticationSystem__website_LocalAuthenticationSystem25", None)
        self.__website_LocalAuthenticationSystem25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_RegistrationUnit"):
                opp_val = getattr(old_value, "website_RegistrationUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_RegistrationUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_RegistrationUnit"):
                opp_val = getattr(value, "website_RegistrationUnit", None)
                setattr(value, "website_RegistrationUnit", self)

    @property
    def website_LocalAuthenticationSystem(self):
        return self.__website_LocalAuthenticationSystem

    @website_LocalAuthenticationSystem.setter
    def website_LocalAuthenticationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_LocalAuthenticationSystem__website_LocalAuthenticationSystem", None)
        self.__website_LocalAuthenticationSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView23"):
                opp_val = getattr(old_value, "website_EntityOrView23", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView23"):
                opp_val = getattr(value, "website_EntityOrView23", None)
                setattr(value, "website_EntityOrView23", self)

class website_Attribute(Feature, Label):

    def __init__(self, placeholder: str, validationPattern: str, inputClass: str, website_Attribute: "website_Authentication" = None, website_Attribute49: "website_EntityOrView" = None, website_Attribute56: "website_Expression" = None, website_Attribute69: "website_ModelLabelAttribute" = None, website_Attribute94: "website_EncapsulatedAttribute" = None, website_Attribute179: "website_UnitElement" = None, website_Attribute236: "website_MapUnit" = None, website_Attribute256: "website_FeaturePathAttribute" = None, website_Attribute264: "website_ChildPathAttribute" = None, website_Attribute291: "website_RouteParameterReference" = None):
        self.placeholder = placeholder
        self.validationPattern = validationPattern
        self.inputClass = inputClass
        self.website_Attribute = website_Attribute
        self.website_Attribute49 = website_Attribute49
        self.website_Attribute56 = website_Attribute56
        self.website_Attribute69 = website_Attribute69
        self.website_Attribute94 = website_Attribute94
        self.website_Attribute179 = website_Attribute179
        self.website_Attribute236 = website_Attribute236
        self.website_Attribute256 = website_Attribute256
        self.website_Attribute264 = website_Attribute264
        self.website_Attribute291 = website_Attribute291
        
    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def website_Attribute291(self):
        return self.__website_Attribute291

    @website_Attribute291.setter
    def website_Attribute291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute291", None)
        self.__website_Attribute291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_RouteParameterReference"):
                opp_val = getattr(old_value, "website_RouteParameterReference", None)
                if opp_val == self:
                    setattr(old_value, "website_RouteParameterReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_RouteParameterReference"):
                opp_val = getattr(value, "website_RouteParameterReference", None)
                setattr(value, "website_RouteParameterReference", self)

    @property
    def website_Attribute(self):
        return self.__website_Attribute

    @website_Attribute.setter
    def website_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute", None)
        self.__website_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Authentication21"):
                opp_val = getattr(old_value, "website_Authentication21", None)
                if opp_val == self:
                    setattr(old_value, "website_Authentication21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Authentication21"):
                opp_val = getattr(value, "website_Authentication21", None)
                setattr(value, "website_Authentication21", self)

    @property
    def website_Attribute236(self):
        return self.__website_Attribute236

    @website_Attribute236.setter
    def website_Attribute236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute236", None)
        self.__website_Attribute236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_MapUnit235"):
                opp_val = getattr(old_value, "website_MapUnit235", None)
                if opp_val == self:
                    setattr(old_value, "website_MapUnit235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_MapUnit235"):
                opp_val = getattr(value, "website_MapUnit235", None)
                setattr(value, "website_MapUnit235", self)

    @property
    def website_Attribute94(self):
        return self.__website_Attribute94

    @website_Attribute94.setter
    def website_Attribute94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute94", None)
        self.__website_Attribute94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EncapsulatedAttribute"):
                opp_val = getattr(old_value, "website_EncapsulatedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_EncapsulatedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EncapsulatedAttribute"):
                opp_val = getattr(value, "website_EncapsulatedAttribute", None)
                setattr(value, "website_EncapsulatedAttribute", self)

    @property
    def website_Attribute264(self):
        return self.__website_Attribute264

    @website_Attribute264.setter
    def website_Attribute264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute264", None)
        self.__website_Attribute264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ChildPathAttribute"):
                opp_val = getattr(old_value, "website_ChildPathAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_ChildPathAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ChildPathAttribute"):
                opp_val = getattr(value, "website_ChildPathAttribute", None)
                setattr(value, "website_ChildPathAttribute", self)

    @property
    def website_Attribute256(self):
        return self.__website_Attribute256

    @website_Attribute256.setter
    def website_Attribute256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute256", None)
        self.__website_Attribute256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeaturePathAttribute"):
                opp_val = getattr(old_value, "website_FeaturePathAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_FeaturePathAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeaturePathAttribute"):
                opp_val = getattr(value, "website_FeaturePathAttribute", None)
                setattr(value, "website_FeaturePathAttribute", self)

    @property
    def website_Attribute56(self):
        return self.__website_Attribute56

    @website_Attribute56.setter
    def website_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute56", None)
        self.__website_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Expression"):
                opp_val = getattr(old_value, "website_Expression", None)
                if opp_val == self:
                    setattr(old_value, "website_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Expression"):
                opp_val = getattr(value, "website_Expression", None)
                setattr(value, "website_Expression", self)

    @property
    def website_Attribute69(self):
        return self.__website_Attribute69

    @website_Attribute69.setter
    def website_Attribute69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute69", None)
        self.__website_Attribute69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ModelLabelAttribute"):
                opp_val = getattr(old_value, "website_ModelLabelAttribute", None)
                if opp_val == self:
                    setattr(old_value, "website_ModelLabelAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ModelLabelAttribute"):
                opp_val = getattr(value, "website_ModelLabelAttribute", None)
                setattr(value, "website_ModelLabelAttribute", self)

    @property
    def website_Attribute49(self):
        return self.__website_Attribute49

    @website_Attribute49.setter
    def website_Attribute49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute49", None)
        self.__website_Attribute49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView48"):
                opp_val = getattr(old_value, "website_EntityOrView48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView48"):
                opp_val = getattr(value, "website_EntityOrView48", None)
                if opp_val is None:
                    setattr(value, "website_EntityOrView48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Attribute179(self):
        return self.__website_Attribute179

    @website_Attribute179.setter
    def website_Attribute179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Attribute__website_Attribute179", None)
        self.__website_Attribute179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_UnitElement"):
                opp_val = getattr(old_value, "website_UnitElement", None)
                if opp_val == self:
                    setattr(old_value, "website_UnitElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_UnitElement"):
                opp_val = getattr(value, "website_UnitElement", None)
                setattr(value, "website_UnitElement", self)

class website_ForgottenPasswordUnit(ControlUnit, AuthenticationUnit):

    def __init__(self, styleClass: str, website_ForgottenPasswordUnit: "website_LocalAuthenticationSystem" = None):
        self.styleClass = styleClass
        self.website_ForgottenPasswordUnit = website_ForgottenPasswordUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def website_ForgottenPasswordUnit(self):
        return self.__website_ForgottenPasswordUnit

    @website_ForgottenPasswordUnit.setter
    def website_ForgottenPasswordUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ForgottenPasswordUnit__website_ForgottenPasswordUnit", None)
        self.__website_ForgottenPasswordUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LocalAuthenticationSystem29"):
                opp_val = getattr(old_value, "website_LocalAuthenticationSystem29", None)
                if opp_val == self:
                    setattr(old_value, "website_LocalAuthenticationSystem29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LocalAuthenticationSystem29"):
                opp_val = getattr(value, "website_LocalAuthenticationSystem29", None)
                setattr(value, "website_LocalAuthenticationSystem29", self)

class website_LoginUnit(ControlUnit, AuthenticationUnit):

    def __init__(self, logoutUriElement: str, styleClass: str, website_LoginUnit: "website_LocalAuthenticationSystem" = None):
        self.logoutUriElement = logoutUriElement
        self.styleClass = styleClass
        self.website_LoginUnit = website_LoginUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def logoutUriElement(self) -> str:
        return self.__logoutUriElement

    @logoutUriElement.setter
    def logoutUriElement(self, logoutUriElement: str):
        self.__logoutUriElement = logoutUriElement

    @property
    def website_LoginUnit(self):
        return self.__website_LoginUnit

    @website_LoginUnit.setter
    def website_LoginUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_LoginUnit__website_LoginUnit", None)
        self.__website_LoginUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LocalAuthenticationSystem27"):
                opp_val = getattr(old_value, "website_LocalAuthenticationSystem27", None)
                if opp_val == self:
                    setattr(old_value, "website_LocalAuthenticationSystem27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LocalAuthenticationSystem27"):
                opp_val = getattr(value, "website_LocalAuthenticationSystem27", None)
                setattr(value, "website_LocalAuthenticationSystem27", self)

class website_RegistrationUnit(ControlUnit, AuthenticationUnit):

    def __init__(self, styleClass: str, website_RegistrationUnit: "website_LocalAuthenticationSystem" = None):
        self.styleClass = styleClass
        self.website_RegistrationUnit = website_RegistrationUnit
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def website_RegistrationUnit(self):
        return self.__website_RegistrationUnit

    @website_RegistrationUnit.setter
    def website_RegistrationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_RegistrationUnit__website_RegistrationUnit", None)
        self.__website_RegistrationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LocalAuthenticationSystem25"):
                opp_val = getattr(old_value, "website_LocalAuthenticationSystem25", None)
                if opp_val == self:
                    setattr(old_value, "website_LocalAuthenticationSystem25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LocalAuthenticationSystem25"):
                opp_val = getattr(value, "website_LocalAuthenticationSystem25", None)
                setattr(value, "website_LocalAuthenticationSystem25", self)

class website_Authentication(ABC):

    def __init__(self, loginLabel: str, logoutLabel: str, Authentication: "website_WebsiteProperties" = None, authentication: "website_WebsiteProperties" = None, website_Authentication: "website_EntityOrView" = None, website_Authentication21: "website_Attribute" = None):
        self.loginLabel = loginLabel
        self.logoutLabel = logoutLabel
        self.Authentication = Authentication
        self.authentication = authentication
        self.website_Authentication = website_Authentication
        self.website_Authentication21 = website_Authentication21
        
    @property
    def logoutLabel(self) -> str:
        return self.__logoutLabel

    @logoutLabel.setter
    def logoutLabel(self, logoutLabel: str):
        self.__logoutLabel = logoutLabel

    @property
    def loginLabel(self) -> str:
        return self.__loginLabel

    @loginLabel.setter
    def loginLabel(self, loginLabel: str):
        self.__loginLabel = loginLabel

    @property
    def authentication(self):
        return self.__authentication

    @authentication.setter
    def authentication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Authentication__authentication", None)
        self.__authentication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebsiteProperties"):
                opp_val = getattr(old_value, "WebsiteProperties", None)
                if opp_val == self:
                    setattr(old_value, "WebsiteProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebsiteProperties"):
                opp_val = getattr(value, "WebsiteProperties", None)
                setattr(value, "WebsiteProperties", self)

    @property
    def website_Authentication21(self):
        return self.__website_Authentication21

    @website_Authentication21.setter
    def website_Authentication21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Authentication__website_Authentication21", None)
        self.__website_Authentication21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Attribute"):
                opp_val = getattr(old_value, "website_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "website_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Attribute"):
                opp_val = getattr(value, "website_Attribute", None)
                setattr(value, "website_Attribute", self)

    @property
    def Authentication(self):
        return self.__Authentication

    @Authentication.setter
    def Authentication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Authentication__Authentication", None)
        self.__Authentication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authenticates"):
                opp_val = getattr(old_value, "authenticates", None)
                if opp_val == self:
                    setattr(old_value, "authenticates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authenticates"):
                opp_val = getattr(value, "authenticates", None)
                setattr(value, "authenticates", self)

    @property
    def website_Authentication(self):
        return self.__website_Authentication

    @website_Authentication.setter
    def website_Authentication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Authentication__website_Authentication", None)
        self.__website_Authentication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EntityOrView19"):
                opp_val = getattr(old_value, "website_EntityOrView19", None)
                if opp_val == self:
                    setattr(old_value, "website_EntityOrView19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EntityOrView19"):
                opp_val = getattr(value, "website_EntityOrView19", None)
                setattr(value, "website_EntityOrView19", self)

class website_ImageManipulation(NamedElement):

    def __init__(self, jpegQuality: int, website_ImageManipulation: "website_WebGenModel" = None, website_ImageManipulation128: set["website_ImageFilter"] = None, website_ImageManipulation254: "website_ImageUnit" = None, website_ImageManipulation271: "website_GalleryUnit" = None):
        self.jpegQuality = jpegQuality
        self.website_ImageManipulation = website_ImageManipulation
        self.website_ImageManipulation128 = website_ImageManipulation128 if website_ImageManipulation128 is not None else set()
        self.website_ImageManipulation254 = website_ImageManipulation254
        self.website_ImageManipulation271 = website_ImageManipulation271
        
    @property
    def jpegQuality(self) -> int:
        return self.__jpegQuality

    @jpegQuality.setter
    def jpegQuality(self, jpegQuality: int):
        self.__jpegQuality = jpegQuality

    @property
    def website_ImageManipulation(self):
        return self.__website_ImageManipulation

    @website_ImageManipulation.setter
    def website_ImageManipulation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageManipulation__website_ImageManipulation", None)
        self.__website_ImageManipulation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebGenModel12"):
                opp_val = getattr(old_value, "website_WebGenModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebGenModel12"):
                opp_val = getattr(value, "website_WebGenModel12", None)
                if opp_val is None:
                    setattr(value, "website_WebGenModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_ImageManipulation128(self):
        return self.__website_ImageManipulation128

    @website_ImageManipulation128.setter
    def website_ImageManipulation128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageManipulation__website_ImageManipulation128", None)
        self.__website_ImageManipulation128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_ImageFilter"):
                    opp_val = getattr(item, "website_ImageFilter", None)
                    
                    if opp_val == self:
                        setattr(item, "website_ImageFilter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_ImageFilter"):
                    opp_val = getattr(item, "website_ImageFilter", None)
                    
                    setattr(item, "website_ImageFilter", self)
                    

    @property
    def website_ImageManipulation254(self):
        return self.__website_ImageManipulation254

    @website_ImageManipulation254.setter
    def website_ImageManipulation254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageManipulation__website_ImageManipulation254", None)
        self.__website_ImageManipulation254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ImageUnit253"):
                opp_val = getattr(old_value, "website_ImageUnit253", None)
                if opp_val == self:
                    setattr(old_value, "website_ImageUnit253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ImageUnit253"):
                opp_val = getattr(value, "website_ImageUnit253", None)
                setattr(value, "website_ImageUnit253", self)

    @property
    def website_ImageManipulation271(self):
        return self.__website_ImageManipulation271

    @website_ImageManipulation271.setter
    def website_ImageManipulation271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_ImageManipulation__website_ImageManipulation271", None)
        self.__website_ImageManipulation271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_GalleryUnit"):
                opp_val = getattr(old_value, "website_GalleryUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_GalleryUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_GalleryUnit"):
                opp_val = getattr(value, "website_GalleryUnit", None)
                setattr(value, "website_GalleryUnit", self)

class website_EntityOrView(Classifier):

    def __init__(self, singletonName: str, pluralisedName: str, tableName: str, autoKeyName: str, autoKeyPersistentType: str, autoKeyGenerationStrategy: str, serializationExcludeAll: bool, implementsUserInterface: bool, website_EntityOrView: "website_WebGenModel" = None, website_EntityOrView19: "website_Authentication" = None, website_EntityOrView23: "website_LocalAuthenticationSystem" = None, labelFor: set["website_ModelLabel"] = None, website_EntityOrView42: set["website_Feature"] = None, website_EntityOrView32: set["website_Feature"] = None, website_EntityOrView34: set["website_Feature"] = None, website_EntityOrView37: set["website_Feature"] = None, serves: set["website_Service"] = None, website_EntityOrView45: set["website_Feature"] = None, website_EntityOrView48: set["website_Attribute"] = None, website_EntityOrView51: set["website_Association"] = None, website_EntityOrView53: set["website_Association"] = None, website_EntityOrView60: "website_Association" = None, website_EntityOrView63: "website_Association" = None, EntityOrView: "website_ModelLabel" = None, website_EntityOrView89: "website_View" = None, EntityOrView106: "website_Service" = None, website_EntityOrView143: "website_DynamicMenu" = None, website_EntityOrView170: "website_DynamicUnit" = None, website_EntityOrView184: "website_UnitAssociation" = None, website_EntityOrView187: "website_UnitAssociation" = None, website_EntityOrView206: "website_CollectionUnit" = None, website_EntityOrView202: "website_SelectableUnit" = None, website_EntityOrView204: "website_SingletonUnit" = None, website_EntityOrView266: "website_ChildPathAssociation" = None, website_EntityOrView269: "website_ChildPathAssociation" = None, website_EntityOrView258: "website_FeaturePathAssociation" = None, website_EntityOrView261: "website_FeaturePathAssociation" = None, website_EntityOrView295: "website_CurrentUserReference" = None):
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.tableName = tableName
        self.autoKeyName = autoKeyName
        self.autoKeyPersistentType = autoKeyPersistentType
        self.autoKeyGenerationStrategy = autoKeyGenerationStrategy
        self.serializationExcludeAll = serializationExcludeAll
        self.implementsUserInterface = implementsUserInterface
        self.website_EntityOrView = website_EntityOrView
        self.website_EntityOrView19 = website_EntityOrView19
        self.website_EntityOrView23 = website_EntityOrView23
        self.labelFor = labelFor if labelFor is not None else set()
        self.website_EntityOrView42 = website_EntityOrView42 if website_EntityOrView42 is not None else set()
        self.website_EntityOrView32 = website_EntityOrView32 if website_EntityOrView32 is not None else set()
        self.website_EntityOrView34 = website_EntityOrView34 if website_EntityOrView34 is not None else set()
        self.website_EntityOrView37 = website_EntityOrView37 if website_EntityOrView37 is not None else set()
        self.serves = serves if serves is not None else set()
        self.website_EntityOrView45 = website_EntityOrView45 if website_EntityOrView45 is not None else set()
        self.website_EntityOrView48 = website_EntityOrView48 if website_EntityOrView48 is not None else set()
        self.website_EntityOrView51 = website_EntityOrView51 if website_EntityOrView51 is not None else set()
        self.website_EntityOrView53 = website_EntityOrView53 if website_EntityOrView53 is not None else set()
        self.website_EntityOrView60 = website_EntityOrView60
        self.website_EntityOrView63 = website_EntityOrView63
        self.EntityOrView = EntityOrView
        self.website_EntityOrView89 = website_EntityOrView89
        self.EntityOrView106 = EntityOrView106
        self.website_EntityOrView143 = website_EntityOrView143
        self.website_EntityOrView170 = website_EntityOrView170
        self.website_EntityOrView184 = website_EntityOrView184
        self.website_EntityOrView187 = website_EntityOrView187
        self.website_EntityOrView206 = website_EntityOrView206
        self.website_EntityOrView202 = website_EntityOrView202
        self.website_EntityOrView204 = website_EntityOrView204
        self.website_EntityOrView266 = website_EntityOrView266
        self.website_EntityOrView269 = website_EntityOrView269
        self.website_EntityOrView258 = website_EntityOrView258
        self.website_EntityOrView261 = website_EntityOrView261
        self.website_EntityOrView295 = website_EntityOrView295
        
    @property
    def autoKeyName(self) -> str:
        return self.__autoKeyName

    @autoKeyName.setter
    def autoKeyName(self, autoKeyName: str):
        self.__autoKeyName = autoKeyName

    @property
    def serializationExcludeAll(self) -> bool:
        return self.__serializationExcludeAll

    @serializationExcludeAll.setter
    def serializationExcludeAll(self, serializationExcludeAll: bool):
        self.__serializationExcludeAll = serializationExcludeAll

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def implementsUserInterface(self) -> bool:
        return self.__implementsUserInterface

    @implementsUserInterface.setter
    def implementsUserInterface(self, implementsUserInterface: bool):
        self.__implementsUserInterface = implementsUserInterface

    @property
    def autoKeyPersistentType(self) -> str:
        return self.__autoKeyPersistentType

    @autoKeyPersistentType.setter
    def autoKeyPersistentType(self, autoKeyPersistentType: str):
        self.__autoKeyPersistentType = autoKeyPersistentType

    @property
    def autoKeyGenerationStrategy(self) -> str:
        return self.__autoKeyGenerationStrategy

    @autoKeyGenerationStrategy.setter
    def autoKeyGenerationStrategy(self, autoKeyGenerationStrategy: str):
        self.__autoKeyGenerationStrategy = autoKeyGenerationStrategy

    @property
    def singletonName(self) -> str:
        return self.__singletonName

    @singletonName.setter
    def singletonName(self, singletonName: str):
        self.__singletonName = singletonName

    @property
    def pluralisedName(self) -> str:
        return self.__pluralisedName

    @pluralisedName.setter
    def pluralisedName(self, pluralisedName: str):
        self.__pluralisedName = pluralisedName

    @property
    def website_EntityOrView202(self):
        return self.__website_EntityOrView202

    @website_EntityOrView202.setter
    def website_EntityOrView202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView202", None)
        self.__website_EntityOrView202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_SelectableUnit"):
                opp_val = getattr(old_value, "website_SelectableUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_SelectableUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_SelectableUnit"):
                opp_val = getattr(value, "website_SelectableUnit", None)
                setattr(value, "website_SelectableUnit", self)

    @property
    def website_EntityOrView42(self):
        return self.__website_EntityOrView42

    @website_EntityOrView42.setter
    def website_EntityOrView42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView42", None)
        self.__website_EntityOrView42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature43"):
                    opp_val = getattr(item, "website_Feature43", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature43"):
                    opp_val = getattr(item, "website_Feature43", None)
                    
                    setattr(item, "website_Feature43", self)
                    

    @property
    def website_EntityOrView187(self):
        return self.__website_EntityOrView187

    @website_EntityOrView187.setter
    def website_EntityOrView187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView187", None)
        self.__website_EntityOrView187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_UnitAssociation186"):
                opp_val = getattr(old_value, "website_UnitAssociation186", None)
                if opp_val == self:
                    setattr(old_value, "website_UnitAssociation186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_UnitAssociation186"):
                opp_val = getattr(value, "website_UnitAssociation186", None)
                setattr(value, "website_UnitAssociation186", self)

    @property
    def website_EntityOrView204(self):
        return self.__website_EntityOrView204

    @website_EntityOrView204.setter
    def website_EntityOrView204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView204", None)
        self.__website_EntityOrView204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_SingletonUnit"):
                opp_val = getattr(old_value, "website_SingletonUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_SingletonUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_SingletonUnit"):
                opp_val = getattr(value, "website_SingletonUnit", None)
                setattr(value, "website_SingletonUnit", self)

    @property
    def website_EntityOrView184(self):
        return self.__website_EntityOrView184

    @website_EntityOrView184.setter
    def website_EntityOrView184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView184", None)
        self.__website_EntityOrView184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_UnitAssociation"):
                opp_val = getattr(old_value, "website_UnitAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_UnitAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_UnitAssociation"):
                opp_val = getattr(value, "website_UnitAssociation", None)
                setattr(value, "website_UnitAssociation", self)

    @property
    def website_EntityOrView258(self):
        return self.__website_EntityOrView258

    @website_EntityOrView258.setter
    def website_EntityOrView258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView258", None)
        self.__website_EntityOrView258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeaturePathAssociation"):
                opp_val = getattr(old_value, "website_FeaturePathAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_FeaturePathAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeaturePathAssociation"):
                opp_val = getattr(value, "website_FeaturePathAssociation", None)
                setattr(value, "website_FeaturePathAssociation", self)

    @property
    def website_EntityOrView295(self):
        return self.__website_EntityOrView295

    @website_EntityOrView295.setter
    def website_EntityOrView295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView295", None)
        self.__website_EntityOrView295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_CurrentUserReference"):
                opp_val = getattr(old_value, "website_CurrentUserReference", None)
                if opp_val == self:
                    setattr(old_value, "website_CurrentUserReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_CurrentUserReference"):
                opp_val = getattr(value, "website_CurrentUserReference", None)
                setattr(value, "website_CurrentUserReference", self)

    @property
    def website_EntityOrView48(self):
        return self.__website_EntityOrView48

    @website_EntityOrView48.setter
    def website_EntityOrView48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView48", None)
        self.__website_EntityOrView48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Attribute49"):
                    opp_val = getattr(item, "website_Attribute49", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Attribute49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Attribute49"):
                    opp_val = getattr(item, "website_Attribute49", None)
                    
                    setattr(item, "website_Attribute49", self)
                    

    @property
    def website_EntityOrView60(self):
        return self.__website_EntityOrView60

    @website_EntityOrView60.setter
    def website_EntityOrView60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView60", None)
        self.__website_EntityOrView60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Association59"):
                opp_val = getattr(old_value, "website_Association59", None)
                if opp_val == self:
                    setattr(old_value, "website_Association59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Association59"):
                opp_val = getattr(value, "website_Association59", None)
                setattr(value, "website_Association59", self)

    @property
    def EntityOrView106(self):
        return self.__EntityOrView106

    @EntityOrView106.setter
    def EntityOrView106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__EntityOrView106", None)
        self.__EntityOrView106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "servedBy"):
                opp_val = getattr(old_value, "servedBy", None)
                if opp_val == self:
                    setattr(old_value, "servedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "servedBy"):
                opp_val = getattr(value, "servedBy", None)
                setattr(value, "servedBy", self)

    @property
    def website_EntityOrView19(self):
        return self.__website_EntityOrView19

    @website_EntityOrView19.setter
    def website_EntityOrView19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView19", None)
        self.__website_EntityOrView19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Authentication"):
                opp_val = getattr(old_value, "website_Authentication", None)
                if opp_val == self:
                    setattr(old_value, "website_Authentication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Authentication"):
                opp_val = getattr(value, "website_Authentication", None)
                setattr(value, "website_Authentication", self)

    @property
    def serves(self):
        return self.__serves

    @serves.setter
    def serves(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__serves", None)
        self.__serves = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

    @property
    def website_EntityOrView266(self):
        return self.__website_EntityOrView266

    @website_EntityOrView266.setter
    def website_EntityOrView266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView266", None)
        self.__website_EntityOrView266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ChildPathAssociation"):
                opp_val = getattr(old_value, "website_ChildPathAssociation", None)
                if opp_val == self:
                    setattr(old_value, "website_ChildPathAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ChildPathAssociation"):
                opp_val = getattr(value, "website_ChildPathAssociation", None)
                setattr(value, "website_ChildPathAssociation", self)

    @property
    def website_EntityOrView63(self):
        return self.__website_EntityOrView63

    @website_EntityOrView63.setter
    def website_EntityOrView63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView63", None)
        self.__website_EntityOrView63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Association62"):
                opp_val = getattr(old_value, "website_Association62", None)
                if opp_val == self:
                    setattr(old_value, "website_Association62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Association62"):
                opp_val = getattr(value, "website_Association62", None)
                setattr(value, "website_Association62", self)

    @property
    def website_EntityOrView53(self):
        return self.__website_EntityOrView53

    @website_EntityOrView53.setter
    def website_EntityOrView53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView53", None)
        self.__website_EntityOrView53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Association54"):
                    opp_val = getattr(item, "website_Association54", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Association54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Association54"):
                    opp_val = getattr(item, "website_Association54", None)
                    
                    setattr(item, "website_Association54", self)
                    

    @property
    def website_EntityOrView269(self):
        return self.__website_EntityOrView269

    @website_EntityOrView269.setter
    def website_EntityOrView269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView269", None)
        self.__website_EntityOrView269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ChildPathAssociation268"):
                opp_val = getattr(old_value, "website_ChildPathAssociation268", None)
                if opp_val == self:
                    setattr(old_value, "website_ChildPathAssociation268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ChildPathAssociation268"):
                opp_val = getattr(value, "website_ChildPathAssociation268", None)
                setattr(value, "website_ChildPathAssociation268", self)

    @property
    def website_EntityOrView89(self):
        return self.__website_EntityOrView89

    @website_EntityOrView89.setter
    def website_EntityOrView89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView89", None)
        self.__website_EntityOrView89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_View"):
                opp_val = getattr(old_value, "website_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_View"):
                opp_val = getattr(value, "website_View", None)
                if opp_val is None:
                    setattr(value, "website_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EntityOrView(self):
        return self.__website_EntityOrView

    @website_EntityOrView.setter
    def website_EntityOrView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView", None)
        self.__website_EntityOrView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebGenModel10"):
                opp_val = getattr(old_value, "website_WebGenModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebGenModel10"):
                opp_val = getattr(value, "website_WebGenModel10", None)
                if opp_val is None:
                    setattr(value, "website_WebGenModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EntityOrView23(self):
        return self.__website_EntityOrView23

    @website_EntityOrView23.setter
    def website_EntityOrView23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView23", None)
        self.__website_EntityOrView23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_LocalAuthenticationSystem"):
                opp_val = getattr(old_value, "website_LocalAuthenticationSystem", None)
                if opp_val == self:
                    setattr(old_value, "website_LocalAuthenticationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_LocalAuthenticationSystem"):
                opp_val = getattr(value, "website_LocalAuthenticationSystem", None)
                setattr(value, "website_LocalAuthenticationSystem", self)

    @property
    def website_EntityOrView170(self):
        return self.__website_EntityOrView170

    @website_EntityOrView170.setter
    def website_EntityOrView170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView170", None)
        self.__website_EntityOrView170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DynamicUnit"):
                opp_val = getattr(old_value, "website_DynamicUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DynamicUnit"):
                opp_val = getattr(value, "website_DynamicUnit", None)
                if opp_val is None:
                    setattr(value, "website_DynamicUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EntityOrView143(self):
        return self.__website_EntityOrView143

    @website_EntityOrView143.setter
    def website_EntityOrView143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView143", None)
        self.__website_EntityOrView143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DynamicMenu"):
                opp_val = getattr(old_value, "website_DynamicMenu", None)
                if opp_val == self:
                    setattr(old_value, "website_DynamicMenu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DynamicMenu"):
                opp_val = getattr(value, "website_DynamicMenu", None)
                setattr(value, "website_DynamicMenu", self)

    @property
    def labelFor(self):
        return self.__labelFor

    @labelFor.setter
    def labelFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__labelFor", None)
        self.__labelFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelLabel"):
                    opp_val = getattr(item, "ModelLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelLabel"):
                    opp_val = getattr(item, "ModelLabel", None)
                    
                    setattr(item, "ModelLabel", self)
                    

    @property
    def website_EntityOrView32(self):
        return self.__website_EntityOrView32

    @website_EntityOrView32.setter
    def website_EntityOrView32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView32", None)
        self.__website_EntityOrView32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature"):
                    opp_val = getattr(item, "website_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature"):
                    opp_val = getattr(item, "website_Feature", None)
                    
                    setattr(item, "website_Feature", self)
                    

    @property
    def website_EntityOrView261(self):
        return self.__website_EntityOrView261

    @website_EntityOrView261.setter
    def website_EntityOrView261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView261", None)
        self.__website_EntityOrView261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_FeaturePathAssociation260"):
                opp_val = getattr(old_value, "website_FeaturePathAssociation260", None)
                if opp_val == self:
                    setattr(old_value, "website_FeaturePathAssociation260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_FeaturePathAssociation260"):
                opp_val = getattr(value, "website_FeaturePathAssociation260", None)
                setattr(value, "website_FeaturePathAssociation260", self)

    @property
    def website_EntityOrView206(self):
        return self.__website_EntityOrView206

    @website_EntityOrView206.setter
    def website_EntityOrView206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView206", None)
        self.__website_EntityOrView206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_CollectionUnit"):
                opp_val = getattr(old_value, "website_CollectionUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_CollectionUnit"):
                opp_val = getattr(value, "website_CollectionUnit", None)
                if opp_val is None:
                    setattr(value, "website_CollectionUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_EntityOrView34(self):
        return self.__website_EntityOrView34

    @website_EntityOrView34.setter
    def website_EntityOrView34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView34", None)
        self.__website_EntityOrView34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature35"):
                    opp_val = getattr(item, "website_Feature35", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature35"):
                    opp_val = getattr(item, "website_Feature35", None)
                    
                    setattr(item, "website_Feature35", self)
                    

    @property
    def EntityOrView(self):
        return self.__EntityOrView

    @EntityOrView.setter
    def EntityOrView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__EntityOrView", None)
        self.__EntityOrView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labels"):
                opp_val = getattr(old_value, "labels", None)
                if opp_val == self:
                    setattr(old_value, "labels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labels"):
                opp_val = getattr(value, "labels", None)
                setattr(value, "labels", self)

    @property
    def website_EntityOrView37(self):
        return self.__website_EntityOrView37

    @website_EntityOrView37.setter
    def website_EntityOrView37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView37", None)
        self.__website_EntityOrView37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature38"):
                    opp_val = getattr(item, "website_Feature38", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature38"):
                    opp_val = getattr(item, "website_Feature38", None)
                    
                    setattr(item, "website_Feature38", self)
                    

    @property
    def website_EntityOrView51(self):
        return self.__website_EntityOrView51

    @website_EntityOrView51.setter
    def website_EntityOrView51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView51", None)
        self.__website_EntityOrView51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Association"):
                    opp_val = getattr(item, "website_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Association"):
                    opp_val = getattr(item, "website_Association", None)
                    
                    setattr(item, "website_Association", self)
                    

    @property
    def website_EntityOrView45(self):
        return self.__website_EntityOrView45

    @website_EntityOrView45.setter
    def website_EntityOrView45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_EntityOrView__website_EntityOrView45", None)
        self.__website_EntityOrView45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "website_Feature46"):
                    opp_val = getattr(item, "website_Feature46", None)
                    
                    if opp_val == self:
                        setattr(item, "website_Feature46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "website_Feature46"):
                    opp_val = getattr(item, "website_Feature46", None)
                    
                    setattr(item, "website_Feature46", self)
                    

class website_Menu(NamedDisplayElement):

    def __init__(self, omitCaption: bool, captionClass: str, styleClass: str, layoutClass: str, website_Menu: "website_WebGenModel" = None, website_Menu16: "website_WebsiteProperties" = None, website_Menu134: "website_Page" = None, partOf137: set["website_MenuEntry"] = None, Menu: "website_MenuEntry" = None):
        self.omitCaption = omitCaption
        self.captionClass = captionClass
        self.styleClass = styleClass
        self.layoutClass = layoutClass
        self.website_Menu = website_Menu
        self.website_Menu16 = website_Menu16
        self.website_Menu134 = website_Menu134
        self.partOf137 = partOf137 if partOf137 is not None else set()
        self.Menu = Menu
        
    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def captionClass(self) -> str:
        return self.__captionClass

    @captionClass.setter
    def captionClass(self, captionClass: str):
        self.__captionClass = captionClass

    @property
    def omitCaption(self) -> bool:
        return self.__omitCaption

    @omitCaption.setter
    def omitCaption(self, omitCaption: bool):
        self.__omitCaption = omitCaption

    @property
    def layoutClass(self) -> str:
        return self.__layoutClass

    @layoutClass.setter
    def layoutClass(self, layoutClass: str):
        self.__layoutClass = layoutClass

    @property
    def website_Menu134(self):
        return self.__website_Menu134

    @website_Menu134.setter
    def website_Menu134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Menu__website_Menu134", None)
        self.__website_Menu134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Page133"):
                opp_val = getattr(old_value, "website_Page133", None)
                if opp_val == self:
                    setattr(old_value, "website_Page133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Page133"):
                opp_val = getattr(value, "website_Page133", None)
                setattr(value, "website_Page133", self)

    @property
    def partOf137(self):
        return self.__partOf137

    @partOf137.setter
    def partOf137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Menu__partOf137", None)
        self.__partOf137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MenuEntry"):
                    opp_val = getattr(item, "MenuEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "MenuEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MenuEntry"):
                    opp_val = getattr(item, "MenuEntry", None)
                    
                    setattr(item, "MenuEntry", self)
                    

    @property
    def Menu(self):
        return self.__Menu

    @Menu.setter
    def Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Menu__Menu", None)
        self.__Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entries"):
                opp_val = getattr(old_value, "entries", None)
                if opp_val == self:
                    setattr(old_value, "entries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entries"):
                opp_val = getattr(value, "entries", None)
                setattr(value, "entries", self)

    @property
    def website_Menu(self):
        return self.__website_Menu

    @website_Menu.setter
    def website_Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Menu__website_Menu", None)
        self.__website_Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebGenModel8"):
                opp_val = getattr(old_value, "website_WebGenModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebGenModel8"):
                opp_val = getattr(value, "website_WebGenModel8", None)
                if opp_val is None:
                    setattr(value, "website_WebGenModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def website_Menu16(self):
        return self.__website_Menu16

    @website_Menu16.setter
    def website_Menu16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Menu__website_Menu16", None)
        self.__website_Menu16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebsiteProperties15"):
                opp_val = getattr(old_value, "website_WebsiteProperties15", None)
                if opp_val == self:
                    setattr(old_value, "website_WebsiteProperties15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebsiteProperties15"):
                opp_val = getattr(value, "website_WebsiteProperties15", None)
                setattr(value, "website_WebsiteProperties15", self)

class website_Page(UnitContainer, NamedDisplayElement):

    def __init__(self, authenticated: bool, uriElement: str, topMenuOption: str, topMenuRank: int, navigationLabel: str, styleClass: str, website_Page: "website_WebGenModel" = None, website_Page130: "website_PageLink" = None, targetPage: set["website_PageLink"] = None, website_Page133: "website_Menu" = None, Page: "website_PageLink" = None, website_Page229: "website_EditUnit" = None, website_Page232: "website_EditUnit" = None, website_Page243: "website_ControlUnit" = None, website_Page283: "website_DeleteAction" = None):
        self.authenticated = authenticated
        self.uriElement = uriElement
        self.topMenuOption = topMenuOption
        self.topMenuRank = topMenuRank
        self.navigationLabel = navigationLabel
        self.styleClass = styleClass
        self.website_Page = website_Page
        self.website_Page130 = website_Page130
        self.targetPage = targetPage if targetPage is not None else set()
        self.website_Page133 = website_Page133
        self.Page = Page
        self.website_Page229 = website_Page229
        self.website_Page232 = website_Page232
        self.website_Page243 = website_Page243
        self.website_Page283 = website_Page283
        
    @property
    def uriElement(self) -> str:
        return self.__uriElement

    @uriElement.setter
    def uriElement(self, uriElement: str):
        self.__uriElement = uriElement

    @property
    def navigationLabel(self) -> str:
        return self.__navigationLabel

    @navigationLabel.setter
    def navigationLabel(self, navigationLabel: str):
        self.__navigationLabel = navigationLabel

    @property
    def authenticated(self) -> bool:
        return self.__authenticated

    @authenticated.setter
    def authenticated(self, authenticated: bool):
        self.__authenticated = authenticated

    @property
    def topMenuRank(self) -> int:
        return self.__topMenuRank

    @topMenuRank.setter
    def topMenuRank(self, topMenuRank: int):
        self.__topMenuRank = topMenuRank

    @property
    def topMenuOption(self) -> str:
        return self.__topMenuOption

    @topMenuOption.setter
    def topMenuOption(self, topMenuOption: str):
        self.__topMenuOption = topMenuOption

    @property
    def styleClass(self) -> str:
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childPages"):
                opp_val = getattr(old_value, "childPages", None)
                if opp_val == self:
                    setattr(old_value, "childPages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childPages"):
                opp_val = getattr(value, "childPages", None)
                setattr(value, "childPages", self)

    @property
    def website_Page283(self):
        return self.__website_Page283

    @website_Page283.setter
    def website_Page283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page283", None)
        self.__website_Page283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_DeleteAction"):
                opp_val = getattr(old_value, "website_DeleteAction", None)
                if opp_val == self:
                    setattr(old_value, "website_DeleteAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_DeleteAction"):
                opp_val = getattr(value, "website_DeleteAction", None)
                setattr(value, "website_DeleteAction", self)

    @property
    def targetPage(self):
        return self.__targetPage

    @targetPage.setter
    def targetPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__targetPage", None)
        self.__targetPage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PageLink"):
                    opp_val = getattr(item, "PageLink", None)
                    
                    if opp_val == self:
                        setattr(item, "PageLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageLink"):
                    opp_val = getattr(item, "PageLink", None)
                    
                    setattr(item, "PageLink", self)
                    

    @property
    def website_Page130(self):
        return self.__website_Page130

    @website_Page130.setter
    def website_Page130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page130", None)
        self.__website_Page130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_PageLink"):
                opp_val = getattr(old_value, "website_PageLink", None)
                if opp_val == self:
                    setattr(old_value, "website_PageLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_PageLink"):
                opp_val = getattr(value, "website_PageLink", None)
                setattr(value, "website_PageLink", self)

    @property
    def website_Page133(self):
        return self.__website_Page133

    @website_Page133.setter
    def website_Page133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page133", None)
        self.__website_Page133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Menu134"):
                opp_val = getattr(old_value, "website_Menu134", None)
                if opp_val == self:
                    setattr(old_value, "website_Menu134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Menu134"):
                opp_val = getattr(value, "website_Menu134", None)
                setattr(value, "website_Menu134", self)

    @property
    def website_Page243(self):
        return self.__website_Page243

    @website_Page243.setter
    def website_Page243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page243", None)
        self.__website_Page243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_ControlUnit"):
                opp_val = getattr(old_value, "website_ControlUnit", None)
                if opp_val == self:
                    setattr(old_value, "website_ControlUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_ControlUnit"):
                opp_val = getattr(value, "website_ControlUnit", None)
                setattr(value, "website_ControlUnit", self)

    @property
    def website_Page232(self):
        return self.__website_Page232

    @website_Page232.setter
    def website_Page232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page232", None)
        self.__website_Page232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EditUnit231"):
                opp_val = getattr(old_value, "website_EditUnit231", None)
                if opp_val == self:
                    setattr(old_value, "website_EditUnit231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EditUnit231"):
                opp_val = getattr(value, "website_EditUnit231", None)
                setattr(value, "website_EditUnit231", self)

    @property
    def website_Page229(self):
        return self.__website_Page229

    @website_Page229.setter
    def website_Page229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page229", None)
        self.__website_Page229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_EditUnit228"):
                opp_val = getattr(old_value, "website_EditUnit228", None)
                if opp_val == self:
                    setattr(old_value, "website_EditUnit228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_EditUnit228"):
                opp_val = getattr(value, "website_EditUnit228", None)
                setattr(value, "website_EditUnit228", self)

    @property
    def website_Page(self):
        return self.__website_Page

    @website_Page.setter
    def website_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_Page__website_Page", None)
        self.__website_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebGenModel6"):
                opp_val = getattr(old_value, "website_WebGenModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebGenModel6"):
                opp_val = getattr(value, "website_WebGenModel6", None)
                if opp_val is None:
                    setattr(value, "website_WebGenModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class website_WebsiteProperties:

    def __init__(self, databaseTechnology: str, databasePrefix: str, databaseHost: str, databaseName: str, databasePort: str, databaseUsername: str, databasePassword: str, siteTitle: str, developmentVersion: bool, baseURL: str, rewriteURLs: bool, webmasterEmail: str, copyrightText: str, metaDescription: str, projectName: str, testProjectName: str, defaultDateFormat: str, defaultTimeFormat: str, defaultDateTimeFormat: str, defaultMaximumUploadSize: int, ormTechnology: str, timestampCreation: bool, timestampUpdates: bool, frameworkTechnology: str, inputTechnology: str, ajaxTechnology: str, captchaSiteKey: str, captchaSecretKey: str, textEditorURL: str, responsiveTopMenu: bool, topNavigationId: str, siteTemplate: str, staticUnitsEditable: bool, website_WebsiteProperties: "website_WebGenModel" = None, authenticates: "website_Authentication" = None, website_WebsiteProperties15: "website_Menu" = None, WebsiteProperties: "website_Authentication" = None):
        self.databaseTechnology = databaseTechnology
        self.databasePrefix = databasePrefix
        self.databaseHost = databaseHost
        self.databaseName = databaseName
        self.databasePort = databasePort
        self.databaseUsername = databaseUsername
        self.databasePassword = databasePassword
        self.siteTitle = siteTitle
        self.developmentVersion = developmentVersion
        self.baseURL = baseURL
        self.rewriteURLs = rewriteURLs
        self.webmasterEmail = webmasterEmail
        self.copyrightText = copyrightText
        self.metaDescription = metaDescription
        self.projectName = projectName
        self.testProjectName = testProjectName
        self.defaultDateFormat = defaultDateFormat
        self.defaultTimeFormat = defaultTimeFormat
        self.defaultDateTimeFormat = defaultDateTimeFormat
        self.defaultMaximumUploadSize = defaultMaximumUploadSize
        self.ormTechnology = ormTechnology
        self.timestampCreation = timestampCreation
        self.timestampUpdates = timestampUpdates
        self.frameworkTechnology = frameworkTechnology
        self.inputTechnology = inputTechnology
        self.ajaxTechnology = ajaxTechnology
        self.captchaSiteKey = captchaSiteKey
        self.captchaSecretKey = captchaSecretKey
        self.textEditorURL = textEditorURL
        self.responsiveTopMenu = responsiveTopMenu
        self.topNavigationId = topNavigationId
        self.siteTemplate = siteTemplate
        self.staticUnitsEditable = staticUnitsEditable
        self.website_WebsiteProperties = website_WebsiteProperties
        self.authenticates = authenticates
        self.website_WebsiteProperties15 = website_WebsiteProperties15
        self.WebsiteProperties = WebsiteProperties
        
    @property
    def siteTitle(self) -> str:
        return self.__siteTitle

    @siteTitle.setter
    def siteTitle(self, siteTitle: str):
        self.__siteTitle = siteTitle

    @property
    def databasePrefix(self) -> str:
        return self.__databasePrefix

    @databasePrefix.setter
    def databasePrefix(self, databasePrefix: str):
        self.__databasePrefix = databasePrefix

    @property
    def textEditorURL(self) -> str:
        return self.__textEditorURL

    @textEditorURL.setter
    def textEditorURL(self, textEditorURL: str):
        self.__textEditorURL = textEditorURL

    @property
    def testProjectName(self) -> str:
        return self.__testProjectName

    @testProjectName.setter
    def testProjectName(self, testProjectName: str):
        self.__testProjectName = testProjectName

    @property
    def webmasterEmail(self) -> str:
        return self.__webmasterEmail

    @webmasterEmail.setter
    def webmasterEmail(self, webmasterEmail: str):
        self.__webmasterEmail = webmasterEmail

    @property
    def timestampCreation(self) -> bool:
        return self.__timestampCreation

    @timestampCreation.setter
    def timestampCreation(self, timestampCreation: bool):
        self.__timestampCreation = timestampCreation

    @property
    def databasePort(self) -> str:
        return self.__databasePort

    @databasePort.setter
    def databasePort(self, databasePort: str):
        self.__databasePort = databasePort

    @property
    def ormTechnology(self) -> str:
        return self.__ormTechnology

    @ormTechnology.setter
    def ormTechnology(self, ormTechnology: str):
        self.__ormTechnology = ormTechnology

    @property
    def captchaSiteKey(self) -> str:
        return self.__captchaSiteKey

    @captchaSiteKey.setter
    def captchaSiteKey(self, captchaSiteKey: str):
        self.__captchaSiteKey = captchaSiteKey

    @property
    def captchaSecretKey(self) -> str:
        return self.__captchaSecretKey

    @captchaSecretKey.setter
    def captchaSecretKey(self, captchaSecretKey: str):
        self.__captchaSecretKey = captchaSecretKey

    @property
    def projectName(self) -> str:
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName

    @property
    def staticUnitsEditable(self) -> bool:
        return self.__staticUnitsEditable

    @staticUnitsEditable.setter
    def staticUnitsEditable(self, staticUnitsEditable: bool):
        self.__staticUnitsEditable = staticUnitsEditable

    @property
    def timestampUpdates(self) -> bool:
        return self.__timestampUpdates

    @timestampUpdates.setter
    def timestampUpdates(self, timestampUpdates: bool):
        self.__timestampUpdates = timestampUpdates

    @property
    def databaseHost(self) -> str:
        return self.__databaseHost

    @databaseHost.setter
    def databaseHost(self, databaseHost: str):
        self.__databaseHost = databaseHost

    @property
    def defaultDateTimeFormat(self) -> str:
        return self.__defaultDateTimeFormat

    @defaultDateTimeFormat.setter
    def defaultDateTimeFormat(self, defaultDateTimeFormat: str):
        self.__defaultDateTimeFormat = defaultDateTimeFormat

    @property
    def copyrightText(self) -> str:
        return self.__copyrightText

    @copyrightText.setter
    def copyrightText(self, copyrightText: str):
        self.__copyrightText = copyrightText

    @property
    def defaultDateFormat(self) -> str:
        return self.__defaultDateFormat

    @defaultDateFormat.setter
    def defaultDateFormat(self, defaultDateFormat: str):
        self.__defaultDateFormat = defaultDateFormat

    @property
    def developmentVersion(self) -> bool:
        return self.__developmentVersion

    @developmentVersion.setter
    def developmentVersion(self, developmentVersion: bool):
        self.__developmentVersion = developmentVersion

    @property
    def rewriteURLs(self) -> bool:
        return self.__rewriteURLs

    @rewriteURLs.setter
    def rewriteURLs(self, rewriteURLs: bool):
        self.__rewriteURLs = rewriteURLs

    @property
    def databaseTechnology(self) -> str:
        return self.__databaseTechnology

    @databaseTechnology.setter
    def databaseTechnology(self, databaseTechnology: str):
        self.__databaseTechnology = databaseTechnology

    @property
    def siteTemplate(self) -> str:
        return self.__siteTemplate

    @siteTemplate.setter
    def siteTemplate(self, siteTemplate: str):
        self.__siteTemplate = siteTemplate

    @property
    def databaseName(self) -> str:
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName

    @property
    def ajaxTechnology(self) -> str:
        return self.__ajaxTechnology

    @ajaxTechnology.setter
    def ajaxTechnology(self, ajaxTechnology: str):
        self.__ajaxTechnology = ajaxTechnology

    @property
    def databaseUsername(self) -> str:
        return self.__databaseUsername

    @databaseUsername.setter
    def databaseUsername(self, databaseUsername: str):
        self.__databaseUsername = databaseUsername

    @property
    def metaDescription(self) -> str:
        return self.__metaDescription

    @metaDescription.setter
    def metaDescription(self, metaDescription: str):
        self.__metaDescription = metaDescription

    @property
    def topNavigationId(self) -> str:
        return self.__topNavigationId

    @topNavigationId.setter
    def topNavigationId(self, topNavigationId: str):
        self.__topNavigationId = topNavigationId

    @property
    def defaultTimeFormat(self) -> str:
        return self.__defaultTimeFormat

    @defaultTimeFormat.setter
    def defaultTimeFormat(self, defaultTimeFormat: str):
        self.__defaultTimeFormat = defaultTimeFormat

    @property
    def defaultMaximumUploadSize(self) -> int:
        return self.__defaultMaximumUploadSize

    @defaultMaximumUploadSize.setter
    def defaultMaximumUploadSize(self, defaultMaximumUploadSize: int):
        self.__defaultMaximumUploadSize = defaultMaximumUploadSize

    @property
    def inputTechnology(self) -> str:
        return self.__inputTechnology

    @inputTechnology.setter
    def inputTechnology(self, inputTechnology: str):
        self.__inputTechnology = inputTechnology

    @property
    def databasePassword(self) -> str:
        return self.__databasePassword

    @databasePassword.setter
    def databasePassword(self, databasePassword: str):
        self.__databasePassword = databasePassword

    @property
    def frameworkTechnology(self) -> str:
        return self.__frameworkTechnology

    @frameworkTechnology.setter
    def frameworkTechnology(self, frameworkTechnology: str):
        self.__frameworkTechnology = frameworkTechnology

    @property
    def baseURL(self) -> str:
        return self.__baseURL

    @baseURL.setter
    def baseURL(self, baseURL: str):
        self.__baseURL = baseURL

    @property
    def responsiveTopMenu(self) -> bool:
        return self.__responsiveTopMenu

    @responsiveTopMenu.setter
    def responsiveTopMenu(self, responsiveTopMenu: bool):
        self.__responsiveTopMenu = responsiveTopMenu

    @property
    def WebsiteProperties(self):
        return self.__WebsiteProperties

    @WebsiteProperties.setter
    def WebsiteProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_WebsiteProperties__WebsiteProperties", None)
        self.__WebsiteProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authentication"):
                opp_val = getattr(old_value, "authentication", None)
                if opp_val == self:
                    setattr(old_value, "authentication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authentication"):
                opp_val = getattr(value, "authentication", None)
                setattr(value, "authentication", self)

    @property
    def website_WebsiteProperties(self):
        return self.__website_WebsiteProperties

    @website_WebsiteProperties.setter
    def website_WebsiteProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_WebsiteProperties__website_WebsiteProperties", None)
        self.__website_WebsiteProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_WebGenModel"):
                opp_val = getattr(old_value, "website_WebGenModel", None)
                if opp_val == self:
                    setattr(old_value, "website_WebGenModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_WebGenModel"):
                opp_val = getattr(value, "website_WebGenModel", None)
                setattr(value, "website_WebGenModel", self)

    @property
    def website_WebsiteProperties15(self):
        return self.__website_WebsiteProperties15

    @website_WebsiteProperties15.setter
    def website_WebsiteProperties15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_WebsiteProperties__website_WebsiteProperties15", None)
        self.__website_WebsiteProperties15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "website_Menu16"):
                opp_val = getattr(old_value, "website_Menu16", None)
                if opp_val == self:
                    setattr(old_value, "website_Menu16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "website_Menu16"):
                opp_val = getattr(value, "website_Menu16", None)
                setattr(value, "website_Menu16", self)

    @property
    def authenticates(self):
        return self.__authenticates

    @authenticates.setter
    def authenticates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_website_WebsiteProperties__authenticates", None)
        self.__authenticates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Authentication"):
                opp_val = getattr(old_value, "Authentication", None)
                if opp_val == self:
                    setattr(old_value, "Authentication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Authentication"):
                opp_val = getattr(value, "Authentication", None)
                setattr(value, "Authentication", self)

class website_WebGenModel:

    pass
class website_Service(NamedElement):

    pass
class website_Classifier(NamedDisplayElement):

    pass
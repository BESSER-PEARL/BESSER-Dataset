from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ButtonType(Enum):
    button = "button"
    submit = "submit"
    reset = "reset"
    workaround = "workaround"
class MethodType(Enum):
    workaround = "workaround"
    get = "get"
    post = "post"
    put = "put"
    patch = "patch"
    head = "head"
    delete = "delete"
class TargetType(Enum):
    workaround = "workaround"
    self = "self"
    blank = "blank"
    parent = "parent"
    top = "top"
    framename = "framename"
class HTMLTag(Enum):
    workaround = "workaround"
    button = "button"
    input = "input"
    a = "a"
    form = "form"
    img = "img"
    p = "p"
class EventType(Enum):
    workaround = "workaround"
    onSubmit = "onSubmit"
    onError = "onError"
    onLoad = "onLoad"
class InputType(Enum):
    workaround = "workaround"
    text = "text"
    radio = "radio"
    checkbox = "checkbox"


############################################
# Definition of Classes
############################################

class Input:

    pass
class PHPMVC_extPHP_RadioButton(Input):

    pass
class PHPMVC_extPHP_Checkbox(Input):

    pass
class PHPMVC_extPHP_TextField(Input):

    pass
class HTMLElement:

    pass
class PHPMVC_extPHP_Text(HTMLElement):

    def __init__(self, language: str, content: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.language = language
        self.content = content
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class PHPMVC_extPHP_Image(HTMLElement):

    def __init__(self, source: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.source = source
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class PHPMVC_extPHP_Button(HTMLElement):

    def __init__(self, disabled: bool, type: str, content: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.disabled = disabled
        self.type = type
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def disabled(self) -> bool:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: bool):
        self.__disabled = disabled

class PHPMVC_extPHP_Anchor(HTMLElement):

    def __init__(self, target: str, hypRef: str, content: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.target = target
        self.hypRef = hypRef
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def hypRef(self) -> str:
        return self.__hypRef

    @hypRef.setter
    def hypRef(self, hypRef: str):
        self.__hypRef = hypRef

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class PHPMVC_extPHP_Form(HTMLElement):

    def __init__(self, action: str, method: str, target: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.action = action
        self.method = method
        self.target = target
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class PHPMVC_extPHP_Input(HTMLElement):

    def __init__(self, type: str, value: str, HTMLElement: "PHPMVC_extPHP_HTMLElement"):
        self.type = type
        self.value = value
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Event:

    pass
class PHPMVC_coreMVC_ViewComponent(ABC):

    def __init__(self, name: str, PHPMVC_coreMVC_ViewComponent: set["Event"] = None):
        self.name = name
        self.PHPMVC_coreMVC_ViewComponent = PHPMVC_coreMVC_ViewComponent if PHPMVC_coreMVC_ViewComponent is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_ViewComponent(self):
        return self.__PHPMVC_coreMVC_ViewComponent

    @PHPMVC_coreMVC_ViewComponent.setter
    def PHPMVC_coreMVC_ViewComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_ViewComponent__PHPMVC_coreMVC_ViewComponent", None)
        self.__PHPMVC_coreMVC_ViewComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

class PHPMVC_coreMVC_Method:

    def __init__(self, name: str, PHPMVC_coreMVC_Method: set["Attribute"] = None, PHPMVC_coreMVC_Method18: set["Attribute"] = None):
        self.name = name
        self.PHPMVC_coreMVC_Method = PHPMVC_coreMVC_Method if PHPMVC_coreMVC_Method is not None else set()
        self.PHPMVC_coreMVC_Method18 = PHPMVC_coreMVC_Method18 if PHPMVC_coreMVC_Method18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_Method18(self):
        return self.__PHPMVC_coreMVC_Method18

    @PHPMVC_coreMVC_Method18.setter
    def PHPMVC_coreMVC_Method18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_Method__PHPMVC_coreMVC_Method18", None)
        self.__PHPMVC_coreMVC_Method18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute19"):
                    opp_val = getattr(item, "Attribute19", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute19"):
                    opp_val = getattr(item, "Attribute19", None)
                    
                    setattr(item, "Attribute19", self)
                    

    @property
    def PHPMVC_coreMVC_Method(self):
        return self.__PHPMVC_coreMVC_Method

    @PHPMVC_coreMVC_Method.setter
    def PHPMVC_coreMVC_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_Method__PHPMVC_coreMVC_Method", None)
        self.__PHPMVC_coreMVC_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute16"):
                    opp_val = getattr(item, "Attribute16", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute16"):
                    opp_val = getattr(item, "Attribute16", None)
                    
                    setattr(item, "Attribute16", self)
                    

class Method:

    pass
class PHPMVC_coreMVC_Event:

    def __init__(self, type: str, handler: str):
        self.type = type
        self.handler = handler
        
    @property
    def handler(self) -> str:
        return self.__handler

    @handler.setter
    def handler(self, handler: str):
        self.__handler = handler

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class ViewComponent:

    pass
class PHPMVC_extPHP_HTMLElement(ViewComponent):

    def __init__(self, isPairedTag: bool, isEmpty: bool, tagName: str, PHPMVC_extPHP_HTMLElement: set["HTMLElement"] = None, ViewComponent: "PHPMVC_coreMVC_View"):
        self.isPairedTag = isPairedTag
        self.isEmpty = isEmpty
        self.tagName = tagName
        self.PHPMVC_extPHP_HTMLElement = PHPMVC_extPHP_HTMLElement if PHPMVC_extPHP_HTMLElement is not None else set()
        
    @property
    def isEmpty(self) -> bool:
        return self.__isEmpty

    @isEmpty.setter
    def isEmpty(self, isEmpty: bool):
        self.__isEmpty = isEmpty

    @property
    def isPairedTag(self) -> bool:
        return self.__isPairedTag

    @isPairedTag.setter
    def isPairedTag(self, isPairedTag: bool):
        self.__isPairedTag = isPairedTag

    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def PHPMVC_extPHP_HTMLElement(self):
        return self.__PHPMVC_extPHP_HTMLElement

    @PHPMVC_extPHP_HTMLElement.setter
    def PHPMVC_extPHP_HTMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_extPHP_HTMLElement__PHPMVC_extPHP_HTMLElement", None)
        self.__PHPMVC_extPHP_HTMLElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTMLElement"):
                    opp_val = getattr(item, "HTMLElement", None)
                    
                    if opp_val == self:
                        setattr(item, "HTMLElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTMLElement"):
                    opp_val = getattr(item, "HTMLElement", None)
                    
                    setattr(item, "HTMLElement", self)
                    

class Identifier:

    pass
class MVCClass:

    pass
class PHPMVC_coreMVC_View(MVCClass):

    pass
class PHPMVC_coreMVC_Model(MVCClass):

    pass
class PHPMVC_coreMVC_Attribute:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PHPMVC_coreMVC_Controller(MVCClass):

    pass
class PHPMVC_coreMVC_MVCClass(ABC):

    def __init__(self, name: str, PHPMVC_coreMVC_MVCClass: set["Attribute"] = None):
        self.name = name
        self.PHPMVC_coreMVC_MVCClass = PHPMVC_coreMVC_MVCClass if PHPMVC_coreMVC_MVCClass is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_MVCClass(self):
        return self.__PHPMVC_coreMVC_MVCClass

    @PHPMVC_coreMVC_MVCClass.setter
    def PHPMVC_coreMVC_MVCClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_MVCClass__PHPMVC_coreMVC_MVCClass", None)
        self.__PHPMVC_coreMVC_MVCClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

class Controller:

    pass
class PHPMVC_coreMVC_PackageController:

    def __init__(self, name: str, PHPMVC_coreMVC_PackageController: set["Controller"] = None):
        self.name = name
        self.PHPMVC_coreMVC_PackageController = PHPMVC_coreMVC_PackageController if PHPMVC_coreMVC_PackageController is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_PackageController(self):
        return self.__PHPMVC_coreMVC_PackageController

    @PHPMVC_coreMVC_PackageController.setter
    def PHPMVC_coreMVC_PackageController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_PackageController__PHPMVC_coreMVC_PackageController", None)
        self.__PHPMVC_coreMVC_PackageController = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Controller"):
                    opp_val = getattr(item, "Controller", None)
                    
                    if opp_val == self:
                        setattr(item, "Controller", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Controller"):
                    opp_val = getattr(item, "Controller", None)
                    
                    setattr(item, "Controller", self)
                    

class View:

    pass
class PHPMVC_coreMVC_PackageView:

    def __init__(self, name: str, PHPMVC_coreMVC_PackageView: set["View"] = None):
        self.name = name
        self.PHPMVC_coreMVC_PackageView = PHPMVC_coreMVC_PackageView if PHPMVC_coreMVC_PackageView is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_PackageView(self):
        return self.__PHPMVC_coreMVC_PackageView

    @PHPMVC_coreMVC_PackageView.setter
    def PHPMVC_coreMVC_PackageView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_PackageView__PHPMVC_coreMVC_PackageView", None)
        self.__PHPMVC_coreMVC_PackageView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    if opp_val == self:
                        setattr(item, "View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    setattr(item, "View", self)
                    

class Model:

    pass
class Attribute:

    pass
class PHPMVC_coreMVC_Identifier(Attribute):

    def __init__(self, isAutoincremental: bool, Attribute19: "PHPMVC_coreMVC_Method", Attribute: "PHPMVC_coreMVC_MVCClass", Attribute16: "PHPMVC_coreMVC_Method"):
        self.isAutoincremental = isAutoincremental
        
    @property
    def isAutoincremental(self) -> bool:
        return self.__isAutoincremental

    @isAutoincremental.setter
    def isAutoincremental(self, isAutoincremental: bool):
        self.__isAutoincremental = isAutoincremental

class PackageController:

    pass
class PackageView:

    pass
class PackageModel:

    pass
class PHPMVC_coreMVC_Application:

    def __init__(self, name: str, routes: str, type: str, locale: str, PHPMVC_coreMVC_Application: "PackageModel" = None, PHPMVC_coreMVC_Application2: "PackageView" = None, PHPMVC_coreMVC_Application4: "PackageController" = None):
        self.name = name
        self.routes = routes
        self.type = type
        self.locale = locale
        self.PHPMVC_coreMVC_Application = PHPMVC_coreMVC_Application
        self.PHPMVC_coreMVC_Application2 = PHPMVC_coreMVC_Application2
        self.PHPMVC_coreMVC_Application4 = PHPMVC_coreMVC_Application4
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def locale(self) -> str:
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def routes(self) -> str:
        return self.__routes

    @routes.setter
    def routes(self, routes: str):
        self.__routes = routes

    @property
    def PHPMVC_coreMVC_Application(self):
        return self.__PHPMVC_coreMVC_Application

    @PHPMVC_coreMVC_Application.setter
    def PHPMVC_coreMVC_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_Application__PHPMVC_coreMVC_Application", None)
        self.__PHPMVC_coreMVC_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageModel"):
                opp_val = getattr(old_value, "PackageModel", None)
                if opp_val == self:
                    setattr(old_value, "PackageModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageModel"):
                opp_val = getattr(value, "PackageModel", None)
                setattr(value, "PackageModel", self)

    @property
    def PHPMVC_coreMVC_Application2(self):
        return self.__PHPMVC_coreMVC_Application2

    @PHPMVC_coreMVC_Application2.setter
    def PHPMVC_coreMVC_Application2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_Application__PHPMVC_coreMVC_Application2", None)
        self.__PHPMVC_coreMVC_Application2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageView"):
                opp_val = getattr(old_value, "PackageView", None)
                if opp_val == self:
                    setattr(old_value, "PackageView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageView"):
                opp_val = getattr(value, "PackageView", None)
                setattr(value, "PackageView", self)

    @property
    def PHPMVC_coreMVC_Application4(self):
        return self.__PHPMVC_coreMVC_Application4

    @PHPMVC_coreMVC_Application4.setter
    def PHPMVC_coreMVC_Application4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_Application__PHPMVC_coreMVC_Application4", None)
        self.__PHPMVC_coreMVC_Application4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageController"):
                opp_val = getattr(old_value, "PackageController", None)
                if opp_val == self:
                    setattr(old_value, "PackageController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageController"):
                opp_val = getattr(value, "PackageController", None)
                setattr(value, "PackageController", self)

class PHPMVC_coreMVC_PackageModel:

    def __init__(self, name: str, PHPMVC_coreMVC_PackageModel: set["Model"] = None):
        self.name = name
        self.PHPMVC_coreMVC_PackageModel = PHPMVC_coreMVC_PackageModel if PHPMVC_coreMVC_PackageModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PHPMVC_coreMVC_PackageModel(self):
        return self.__PHPMVC_coreMVC_PackageModel

    @PHPMVC_coreMVC_PackageModel.setter
    def PHPMVC_coreMVC_PackageModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PHPMVC_coreMVC_PackageModel__PHPMVC_coreMVC_PackageModel", None)
        self.__PHPMVC_coreMVC_PackageModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model"):
                    opp_val = getattr(item, "Model", None)
                    
                    if opp_val == self:
                        setattr(item, "Model", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model"):
                    opp_val = getattr(item, "Model", None)
                    
                    setattr(item, "Model", self)
                    

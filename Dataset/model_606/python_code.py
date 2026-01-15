from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    VARCHAR = "VARCHAR"
    BIGINTEGER = "BIGINTEGER"
    DOUBLE = "DOUBLE"
    OID = "OID"
    VOID = "VOID"
class Operation(Enum):
    _create = "_create"
    read = "read"
    update = "update"
    delete = "delete"
    readONE = "readONE"
    readALL = "readALL"
    forward = "forward"


############################################
# Definition of Classes
############################################

class SMVC_SupportedOperation:

    def __init__(self, operationKind: str, url: str, SMVC_SupportedOperation: "SMVC_List" = None):
        self.operationKind = operationKind
        self.url = url
        self.SMVC_SupportedOperation = SMVC_SupportedOperation
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def operationKind(self) -> str:
        return self.__operationKind

    @operationKind.setter
    def operationKind(self, operationKind: str):
        self.__operationKind = operationKind

    @property
    def SMVC_SupportedOperation(self):
        return self.__SMVC_SupportedOperation

    @SMVC_SupportedOperation.setter
    def SMVC_SupportedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_SupportedOperation__SMVC_SupportedOperation", None)
        self.__SMVC_SupportedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_List"):
                opp_val = getattr(old_value, "SMVC_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_List"):
                opp_val = getattr(value, "SMVC_List", None)
                if opp_val is None:
                    setattr(value, "SMVC_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EntityComponent:

    pass
class SMVC_Form(EntityComponent):

    pass
class SMVC_List(EntityComponent):

    pass
class Component:

    pass
class SMVC_EntityComponent(Component):

    pass
class SMVC_Component(ABC):

    pass
class SMVC_View:

    def __init__(self, text: str, SMVC_View: "SMVC_Page" = None, SMVC_View28: set["SMVC_Component"] = None):
        self.text = text
        self.SMVC_View = SMVC_View
        self.SMVC_View28 = SMVC_View28 if SMVC_View28 is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def SMVC_View28(self):
        return self.__SMVC_View28

    @SMVC_View28.setter
    def SMVC_View28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_View__SMVC_View28", None)
        self.__SMVC_View28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Component"):
                    opp_val = getattr(item, "SMVC_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Component"):
                    opp_val = getattr(item, "SMVC_Component", None)
                    
                    setattr(item, "SMVC_Component", self)
                    

    @property
    def SMVC_View(self):
        return self.__SMVC_View

    @SMVC_View.setter
    def SMVC_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_View__SMVC_View", None)
        self.__SMVC_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Page26"):
                opp_val = getattr(old_value, "SMVC_Page26", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Page26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Page26"):
                opp_val = getattr(value, "SMVC_Page26", None)
                setattr(value, "SMVC_Page26", self)

class SMVC_Link:

    def __init__(self, url: str, SMVC_Link: "SMVC_Page" = None):
        self.url = url
        self.SMVC_Link = SMVC_Link
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def SMVC_Link(self):
        return self.__SMVC_Link

    @SMVC_Link.setter
    def SMVC_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Link__SMVC_Link", None)
        self.__SMVC_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Page24"):
                opp_val = getattr(old_value, "SMVC_Page24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Page24"):
                opp_val = getattr(value, "SMVC_Page24", None)
                if opp_val is None:
                    setattr(value, "SMVC_Page24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SMVC_Attribute:

    def __init__(self, name: str, type: str, label: bool, multiValued: bool, SMVC_Attribute: "SMVC_Entity" = None, SMVC_Attribute21: "SMVC_Entity" = None):
        self.name = name
        self.type = type
        self.label = label
        self.multiValued = multiValued
        self.SMVC_Attribute = SMVC_Attribute
        self.SMVC_Attribute21 = SMVC_Attribute21
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> bool:
        return self.__label

    @label.setter
    def label(self, label: bool):
        self.__label = label

    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def SMVC_Attribute(self):
        return self.__SMVC_Attribute

    @SMVC_Attribute.setter
    def SMVC_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Attribute__SMVC_Attribute", None)
        self.__SMVC_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Entity19"):
                opp_val = getattr(old_value, "SMVC_Entity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Entity19"):
                opp_val = getattr(value, "SMVC_Entity19", None)
                if opp_val is None:
                    setattr(value, "SMVC_Entity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SMVC_Attribute21(self):
        return self.__SMVC_Attribute21

    @SMVC_Attribute21.setter
    def SMVC_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Attribute__SMVC_Attribute21", None)
        self.__SMVC_Attribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Entity22"):
                opp_val = getattr(old_value, "SMVC_Entity22", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Entity22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Entity22"):
                opp_val = getattr(value, "SMVC_Entity22", None)
                setattr(value, "SMVC_Entity22", self)

class Controller:

    pass
class SMVC_EntityController(Controller):

    def __init__(self, returnKOURL: str, returnOKURL: str, SMVC_EntityController: "SMVC_DataAccessObject" = None):
        self.returnKOURL = returnKOURL
        self.returnOKURL = returnOKURL
        self.SMVC_EntityController = SMVC_EntityController
        
    @property
    def returnKOURL(self) -> str:
        return self.__returnKOURL

    @returnKOURL.setter
    def returnKOURL(self, returnKOURL: str):
        self.__returnKOURL = returnKOURL

    @property
    def returnOKURL(self) -> str:
        return self.__returnOKURL

    @returnOKURL.setter
    def returnOKURL(self, returnOKURL: str):
        self.__returnOKURL = returnOKURL

    @property
    def SMVC_EntityController(self):
        return self.__SMVC_EntityController

    @SMVC_EntityController.setter
    def SMVC_EntityController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_EntityController__SMVC_EntityController", None)
        self.__SMVC_EntityController = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_DataAccessObject14"):
                opp_val = getattr(old_value, "SMVC_DataAccessObject14", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_DataAccessObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_DataAccessObject14"):
                opp_val = getattr(value, "SMVC_DataAccessObject14", None)
                setattr(value, "SMVC_DataAccessObject14", self)

class SMVC_Page:

    def __init__(self, title: str, SMVC_Page: "SMVC_Controller" = None, SMVC_Page24: set["SMVC_Link"] = None, SMVC_Page26: "SMVC_View" = None):
        self.title = title
        self.SMVC_Page = SMVC_Page
        self.SMVC_Page24 = SMVC_Page24 if SMVC_Page24 is not None else set()
        self.SMVC_Page26 = SMVC_Page26
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def SMVC_Page(self):
        return self.__SMVC_Page

    @SMVC_Page.setter
    def SMVC_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Page__SMVC_Page", None)
        self.__SMVC_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Controller12"):
                opp_val = getattr(old_value, "SMVC_Controller12", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Controller12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Controller12"):
                opp_val = getattr(value, "SMVC_Controller12", None)
                setattr(value, "SMVC_Controller12", self)

    @property
    def SMVC_Page24(self):
        return self.__SMVC_Page24

    @SMVC_Page24.setter
    def SMVC_Page24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Page__SMVC_Page24", None)
        self.__SMVC_Page24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Link"):
                    opp_val = getattr(item, "SMVC_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Link"):
                    opp_val = getattr(item, "SMVC_Link", None)
                    
                    setattr(item, "SMVC_Link", self)
                    

    @property
    def SMVC_Page26(self):
        return self.__SMVC_Page26

    @SMVC_Page26.setter
    def SMVC_Page26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Page__SMVC_Page26", None)
        self.__SMVC_Page26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_View"):
                opp_val = getattr(old_value, "SMVC_View", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_View"):
                opp_val = getattr(value, "SMVC_View", None)
                setattr(value, "SMVC_View", self)

class SMVC_Entity:

    def __init__(self, name: str, SMVC_Entity: "SMVC_SMVCApplication" = None, SMVC_Entity17: "SMVC_DataAccessObject" = None, SMVC_Entity19: set["SMVC_Attribute"] = None, SMVC_Entity22: "SMVC_Attribute" = None, SMVC_Entity30: "SMVC_EntityComponent" = None):
        self.name = name
        self.SMVC_Entity = SMVC_Entity
        self.SMVC_Entity17 = SMVC_Entity17
        self.SMVC_Entity19 = SMVC_Entity19 if SMVC_Entity19 is not None else set()
        self.SMVC_Entity22 = SMVC_Entity22
        self.SMVC_Entity30 = SMVC_Entity30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SMVC_Entity(self):
        return self.__SMVC_Entity

    @SMVC_Entity.setter
    def SMVC_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Entity__SMVC_Entity", None)
        self.__SMVC_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_SMVCApplication7"):
                opp_val = getattr(old_value, "SMVC_SMVCApplication7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_SMVCApplication7"):
                opp_val = getattr(value, "SMVC_SMVCApplication7", None)
                if opp_val is None:
                    setattr(value, "SMVC_SMVCApplication7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SMVC_Entity30(self):
        return self.__SMVC_Entity30

    @SMVC_Entity30.setter
    def SMVC_Entity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Entity__SMVC_Entity30", None)
        self.__SMVC_Entity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_EntityComponent"):
                opp_val = getattr(old_value, "SMVC_EntityComponent", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_EntityComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_EntityComponent"):
                opp_val = getattr(value, "SMVC_EntityComponent", None)
                setattr(value, "SMVC_EntityComponent", self)

    @property
    def SMVC_Entity19(self):
        return self.__SMVC_Entity19

    @SMVC_Entity19.setter
    def SMVC_Entity19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Entity__SMVC_Entity19", None)
        self.__SMVC_Entity19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Attribute"):
                    opp_val = getattr(item, "SMVC_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Attribute"):
                    opp_val = getattr(item, "SMVC_Attribute", None)
                    
                    setattr(item, "SMVC_Attribute", self)
                    

    @property
    def SMVC_Entity17(self):
        return self.__SMVC_Entity17

    @SMVC_Entity17.setter
    def SMVC_Entity17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Entity__SMVC_Entity17", None)
        self.__SMVC_Entity17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_DataAccessObject16"):
                opp_val = getattr(old_value, "SMVC_DataAccessObject16", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_DataAccessObject16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_DataAccessObject16"):
                opp_val = getattr(value, "SMVC_DataAccessObject16", None)
                setattr(value, "SMVC_DataAccessObject16", self)

    @property
    def SMVC_Entity22(self):
        return self.__SMVC_Entity22

    @SMVC_Entity22.setter
    def SMVC_Entity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Entity__SMVC_Entity22", None)
        self.__SMVC_Entity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Attribute21"):
                opp_val = getattr(old_value, "SMVC_Attribute21", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Attribute21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Attribute21"):
                opp_val = getattr(value, "SMVC_Attribute21", None)
                setattr(value, "SMVC_Attribute21", self)

class SMVC_DataAccessObject:

    def __init__(self, name: str, showDirectInstancesOnly: bool, SMVC_DataAccessObject: "SMVC_SMVCApplication" = None, SMVC_DataAccessObject14: "SMVC_EntityController" = None, SMVC_DataAccessObject16: "SMVC_Entity" = None):
        self.name = name
        self.showDirectInstancesOnly = showDirectInstancesOnly
        self.SMVC_DataAccessObject = SMVC_DataAccessObject
        self.SMVC_DataAccessObject14 = SMVC_DataAccessObject14
        self.SMVC_DataAccessObject16 = SMVC_DataAccessObject16
        
    @property
    def showDirectInstancesOnly(self) -> bool:
        return self.__showDirectInstancesOnly

    @showDirectInstancesOnly.setter
    def showDirectInstancesOnly(self, showDirectInstancesOnly: bool):
        self.__showDirectInstancesOnly = showDirectInstancesOnly

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SMVC_DataAccessObject(self):
        return self.__SMVC_DataAccessObject

    @SMVC_DataAccessObject.setter
    def SMVC_DataAccessObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_DataAccessObject__SMVC_DataAccessObject", None)
        self.__SMVC_DataAccessObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_SMVCApplication5"):
                opp_val = getattr(old_value, "SMVC_SMVCApplication5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_SMVCApplication5"):
                opp_val = getattr(value, "SMVC_SMVCApplication5", None)
                if opp_val is None:
                    setattr(value, "SMVC_SMVCApplication5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SMVC_DataAccessObject14(self):
        return self.__SMVC_DataAccessObject14

    @SMVC_DataAccessObject14.setter
    def SMVC_DataAccessObject14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_DataAccessObject__SMVC_DataAccessObject14", None)
        self.__SMVC_DataAccessObject14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_EntityController"):
                opp_val = getattr(old_value, "SMVC_EntityController", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_EntityController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_EntityController"):
                opp_val = getattr(value, "SMVC_EntityController", None)
                setattr(value, "SMVC_EntityController", self)

    @property
    def SMVC_DataAccessObject16(self):
        return self.__SMVC_DataAccessObject16

    @SMVC_DataAccessObject16.setter
    def SMVC_DataAccessObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_DataAccessObject__SMVC_DataAccessObject16", None)
        self.__SMVC_DataAccessObject16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Entity17"):
                opp_val = getattr(old_value, "SMVC_Entity17", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Entity17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Entity17"):
                opp_val = getattr(value, "SMVC_Entity17", None)
                setattr(value, "SMVC_Entity17", self)

class SMVC_Controller:

    def __init__(self, url: str, operation: str, SMVC_Controller: "SMVC_SMVCApplication" = None, SMVC_Controller3: "SMVC_SMVCApplication" = None, SMVC_Controller10: "SMVC_Controller" = None, SMVC_Controller8: set["SMVC_Controller"] = None, SMVC_Controller12: "SMVC_Page" = None):
        self.url = url
        self.operation = operation
        self.SMVC_Controller = SMVC_Controller
        self.SMVC_Controller3 = SMVC_Controller3
        self.SMVC_Controller10 = SMVC_Controller10
        self.SMVC_Controller8 = SMVC_Controller8 if SMVC_Controller8 is not None else set()
        self.SMVC_Controller12 = SMVC_Controller12
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def SMVC_Controller10(self):
        return self.__SMVC_Controller10

    @SMVC_Controller10.setter
    def SMVC_Controller10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Controller__SMVC_Controller10", None)
        self.__SMVC_Controller10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Controller8"):
                opp_val = getattr(old_value, "SMVC_Controller8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Controller8"):
                opp_val = getattr(value, "SMVC_Controller8", None)
                if opp_val is None:
                    setattr(value, "SMVC_Controller8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SMVC_Controller3(self):
        return self.__SMVC_Controller3

    @SMVC_Controller3.setter
    def SMVC_Controller3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Controller__SMVC_Controller3", None)
        self.__SMVC_Controller3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_SMVCApplication2"):
                opp_val = getattr(old_value, "SMVC_SMVCApplication2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_SMVCApplication2"):
                opp_val = getattr(value, "SMVC_SMVCApplication2", None)
                if opp_val is None:
                    setattr(value, "SMVC_SMVCApplication2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SMVC_Controller12(self):
        return self.__SMVC_Controller12

    @SMVC_Controller12.setter
    def SMVC_Controller12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Controller__SMVC_Controller12", None)
        self.__SMVC_Controller12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Page"):
                opp_val = getattr(old_value, "SMVC_Page", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Page"):
                opp_val = getattr(value, "SMVC_Page", None)
                setattr(value, "SMVC_Page", self)

    @property
    def SMVC_Controller(self):
        return self.__SMVC_Controller

    @SMVC_Controller.setter
    def SMVC_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Controller__SMVC_Controller", None)
        self.__SMVC_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_SMVCApplication"):
                opp_val = getattr(old_value, "SMVC_SMVCApplication", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_SMVCApplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_SMVCApplication"):
                opp_val = getattr(value, "SMVC_SMVCApplication", None)
                setattr(value, "SMVC_SMVCApplication", self)

    @property
    def SMVC_Controller8(self):
        return self.__SMVC_Controller8

    @SMVC_Controller8.setter
    def SMVC_Controller8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_Controller__SMVC_Controller8", None)
        self.__SMVC_Controller8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Controller10"):
                    opp_val = getattr(item, "SMVC_Controller10", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Controller10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Controller10"):
                    opp_val = getattr(item, "SMVC_Controller10", None)
                    
                    setattr(item, "SMVC_Controller10", self)
                    

class SMVC_SMVCApplication:

    def __init__(self, name: str, SMVC_SMVCApplication5: set["SMVC_DataAccessObject"] = None, SMVC_SMVCApplication: "SMVC_Controller" = None, SMVC_SMVCApplication2: set["SMVC_Controller"] = None, SMVC_SMVCApplication7: set["SMVC_Entity"] = None):
        self.name = name
        self.SMVC_SMVCApplication5 = SMVC_SMVCApplication5 if SMVC_SMVCApplication5 is not None else set()
        self.SMVC_SMVCApplication = SMVC_SMVCApplication
        self.SMVC_SMVCApplication2 = SMVC_SMVCApplication2 if SMVC_SMVCApplication2 is not None else set()
        self.SMVC_SMVCApplication7 = SMVC_SMVCApplication7 if SMVC_SMVCApplication7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SMVC_SMVCApplication5(self):
        return self.__SMVC_SMVCApplication5

    @SMVC_SMVCApplication5.setter
    def SMVC_SMVCApplication5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_SMVCApplication__SMVC_SMVCApplication5", None)
        self.__SMVC_SMVCApplication5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_DataAccessObject"):
                    opp_val = getattr(item, "SMVC_DataAccessObject", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_DataAccessObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_DataAccessObject"):
                    opp_val = getattr(item, "SMVC_DataAccessObject", None)
                    
                    setattr(item, "SMVC_DataAccessObject", self)
                    

    @property
    def SMVC_SMVCApplication7(self):
        return self.__SMVC_SMVCApplication7

    @SMVC_SMVCApplication7.setter
    def SMVC_SMVCApplication7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_SMVCApplication__SMVC_SMVCApplication7", None)
        self.__SMVC_SMVCApplication7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Entity"):
                    opp_val = getattr(item, "SMVC_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Entity"):
                    opp_val = getattr(item, "SMVC_Entity", None)
                    
                    setattr(item, "SMVC_Entity", self)
                    

    @property
    def SMVC_SMVCApplication2(self):
        return self.__SMVC_SMVCApplication2

    @SMVC_SMVCApplication2.setter
    def SMVC_SMVCApplication2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_SMVCApplication__SMVC_SMVCApplication2", None)
        self.__SMVC_SMVCApplication2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMVC_Controller3"):
                    opp_val = getattr(item, "SMVC_Controller3", None)
                    
                    if opp_val == self:
                        setattr(item, "SMVC_Controller3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMVC_Controller3"):
                    opp_val = getattr(item, "SMVC_Controller3", None)
                    
                    setattr(item, "SMVC_Controller3", self)
                    

    @property
    def SMVC_SMVCApplication(self):
        return self.__SMVC_SMVCApplication

    @SMVC_SMVCApplication.setter
    def SMVC_SMVCApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMVC_SMVCApplication__SMVC_SMVCApplication", None)
        self.__SMVC_SMVCApplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SMVC_Controller"):
                opp_val = getattr(old_value, "SMVC_Controller", None)
                if opp_val == self:
                    setattr(old_value, "SMVC_Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SMVC_Controller"):
                opp_val = getattr(value, "SMVC_Controller", None)
                setattr(value, "SMVC_Controller", self)

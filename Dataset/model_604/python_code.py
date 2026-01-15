from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InputDataType(Enum):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    PASSWORD = "PASSWORD"
    EMAIL = "EMAIL"
    TEL = "TEL"
    DATE = "DATE"
    TIME = "TIME"
    FILE = "FILE"
class ActionMethodParameterType(Enum):
    INTEGER = "INTEGER"
    STRING = "STRING"
class RequestType(Enum):
    REGULAR_HTTP = "REGULAR_HTTP"
    AJAX = "AJAX"
class ActionMethodReturnType(Enum):
    View = "View"
    PartialView = "PartialView"
    RedirectToAction = "RedirectToAction"
    Json = "Json"
    Content = "Content"
class Cardinality(Enum):
    MANY_TO_MANY = "MANY_TO_MANY"
    ONE_TO_MANY = "ONE_TO_MANY"
    ONE_TO_ONE = "ONE_TO_ONE"
class ModelPropertyType(Enum):
    BOOLEAN = "BOOLEAN"
    DATETIME = "DATETIME"
    INTEGER = "INTEGER"
    STRING = "STRING"
    DOUBLE = "DOUBLE"
class MultipleChoiceType(Enum):
    CHECKBOX_GROUP = "CHECKBOX_GROUP"
    DROPDOWN_LIST = "DROPDOWN_LIST"
    RADIO_BUTTON = "RADIO_BUTTON"
class ModelOperation(Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
class ButtonType(Enum):
    SUBMIT = "SUBMIT"
    RESET = "RESET"
class ModelCardinality(Enum):
    ONE = "ONE"
    ALL = "ALL"


############################################
# Definition of Classes
############################################

class ryz_PresentationFormElementToPropertyKey:

    pass
class ryz_Header:

    def __init__(self, name: str, labelText: str, ryz_Header: "ryz_Table" = None):
        self.name = name
        self.labelText = labelText
        self.ryz_Header = ryz_Header
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ryz_Header(self):
        return self.__ryz_Header

    @ryz_Header.setter
    def ryz_Header(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Header__ryz_Header", None)
        self.__ryz_Header = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Table"):
                opp_val = getattr(old_value, "ryz_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Table"):
                opp_val = getattr(value, "ryz_Table", None)
                if opp_val is None:
                    setattr(value, "ryz_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ryz_Choice:

    def __init__(self, text: str, value: str, selected: str, ryz_Choice: "ryz_MultipleChoice" = None):
        self.text = text
        self.value = value
        self.selected = selected
        self.ryz_Choice = ryz_Choice
        
    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ryz_Choice(self):
        return self.__ryz_Choice

    @ryz_Choice.setter
    def ryz_Choice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Choice__ryz_Choice", None)
        self.__ryz_Choice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_MultipleChoice"):
                opp_val = getattr(old_value, "ryz_MultipleChoice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_MultipleChoice"):
                opp_val = getattr(value, "ryz_MultipleChoice", None)
                if opp_val is None:
                    setattr(value, "ryz_MultipleChoice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PresentationFormElement:

    pass
class ryz_Button(PresentationFormElement):

    def __init__(self, buttonType: str):
        self.buttonType = buttonType
        
    @property
    def buttonType(self) -> str:
        return self.__buttonType

    @buttonType.setter
    def buttonType(self, buttonType: str):
        self.__buttonType = buttonType

class ryz_Input(PresentationFormElement):

    def __init__(self, inputDataType: str, isReadOnly: bool, isHidden: bool):
        self.inputDataType = inputDataType
        self.isReadOnly = isReadOnly
        self.isHidden = isHidden
        
    @property
    def isHidden(self) -> bool:
        return self.__isHidden

    @isHidden.setter
    def isHidden(self, isHidden: bool):
        self.__isHidden = isHidden

    @property
    def inputDataType(self) -> str:
        return self.__inputDataType

    @inputDataType.setter
    def inputDataType(self, inputDataType: str):
        self.__inputDataType = inputDataType

    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

class ryz_MultipleChoice(PresentationFormElement):

    def __init__(self, multipleChoiceType: str, multipleSelection: bool, ryz_MultipleChoice: set["ryz_Choice"] = None):
        self.multipleChoiceType = multipleChoiceType
        self.multipleSelection = multipleSelection
        self.ryz_MultipleChoice = ryz_MultipleChoice if ryz_MultipleChoice is not None else set()
        
    @property
    def multipleChoiceType(self) -> str:
        return self.__multipleChoiceType

    @multipleChoiceType.setter
    def multipleChoiceType(self, multipleChoiceType: str):
        self.__multipleChoiceType = multipleChoiceType

    @property
    def multipleSelection(self) -> bool:
        return self.__multipleSelection

    @multipleSelection.setter
    def multipleSelection(self, multipleSelection: bool):
        self.__multipleSelection = multipleSelection

    @property
    def ryz_MultipleChoice(self):
        return self.__ryz_MultipleChoice

    @ryz_MultipleChoice.setter
    def ryz_MultipleChoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_MultipleChoice__ryz_MultipleChoice", None)
        self.__ryz_MultipleChoice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_Choice"):
                    opp_val = getattr(item, "ryz_Choice", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_Choice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_Choice"):
                    opp_val = getattr(item, "ryz_Choice", None)
                    
                    setattr(item, "ryz_Choice", self)
                    

class ryz_PresentationFormElement(ABC):

    def __init__(self, labelText: str, ryz_PresentationFormElement: "ryz_PresentationForm" = None, ryz_PresentationFormElement96: "ryz_PresentationFormElementToPropertyKey" = None):
        self.labelText = labelText
        self.ryz_PresentationFormElement = ryz_PresentationFormElement
        self.ryz_PresentationFormElement96 = ryz_PresentationFormElement96
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def ryz_PresentationFormElement(self):
        return self.__ryz_PresentationFormElement

    @ryz_PresentationFormElement.setter
    def ryz_PresentationFormElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_PresentationFormElement__ryz_PresentationFormElement", None)
        self.__ryz_PresentationFormElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_PresentationForm"):
                opp_val = getattr(old_value, "ryz_PresentationForm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_PresentationForm"):
                opp_val = getattr(value, "ryz_PresentationForm", None)
                if opp_val is None:
                    setattr(value, "ryz_PresentationForm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_PresentationFormElement96(self):
        return self.__ryz_PresentationFormElement96

    @ryz_PresentationFormElement96.setter
    def ryz_PresentationFormElement96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_PresentationFormElement__ryz_PresentationFormElement96", None)
        self.__ryz_PresentationFormElement96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_PresentationFormElementToPropertyKey95"):
                opp_val = getattr(old_value, "ryz_PresentationFormElementToPropertyKey95", None)
                if opp_val == self:
                    setattr(old_value, "ryz_PresentationFormElementToPropertyKey95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_PresentationFormElementToPropertyKey95"):
                opp_val = getattr(value, "ryz_PresentationFormElementToPropertyKey95", None)
                setattr(value, "ryz_PresentationFormElementToPropertyKey95", self)

class PresentationElement:

    pass
class ryz_Link(PresentationElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class ryz_Table(PresentationElement):

    pass
class ryz_PresentationForm(PresentationElement):

    pass
class HelperForSendingRequest:

    pass
class ryz_Form(HelperForSendingRequest):

    pass
class ryz_ActionLink(HelperForSendingRequest):

    pass
class MainComponentRelation:

    pass
class ryz_ControllerToViewRelation(MainComponentRelation):

    pass
class ryz_FormElementToPropertyKeyRelation(MainComponentRelation):

    pass
class ryz_ControllerToModelRelation(MainComponentRelation):

    def __init__(self, modelCardinality: str, modelOperation: str, ryz_ControllerToModelRelation: "ryz_ActionMethod" = None, ryz_ControllerToModelRelation48: "ryz_Model" = None, ryz_ControllerToModelRelation51: set["ryz_Property"] = None):
        self.modelCardinality = modelCardinality
        self.modelOperation = modelOperation
        self.ryz_ControllerToModelRelation = ryz_ControllerToModelRelation
        self.ryz_ControllerToModelRelation48 = ryz_ControllerToModelRelation48
        self.ryz_ControllerToModelRelation51 = ryz_ControllerToModelRelation51 if ryz_ControllerToModelRelation51 is not None else set()
        
    @property
    def modelOperation(self) -> str:
        return self.__modelOperation

    @modelOperation.setter
    def modelOperation(self, modelOperation: str):
        self.__modelOperation = modelOperation

    @property
    def modelCardinality(self) -> str:
        return self.__modelCardinality

    @modelCardinality.setter
    def modelCardinality(self, modelCardinality: str):
        self.__modelCardinality = modelCardinality

    @property
    def ryz_ControllerToModelRelation48(self):
        return self.__ryz_ControllerToModelRelation48

    @ryz_ControllerToModelRelation48.setter
    def ryz_ControllerToModelRelation48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ControllerToModelRelation__ryz_ControllerToModelRelation48", None)
        self.__ryz_ControllerToModelRelation48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model49"):
                opp_val = getattr(old_value, "ryz_Model49", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model49"):
                opp_val = getattr(value, "ryz_Model49", None)
                setattr(value, "ryz_Model49", self)

    @property
    def ryz_ControllerToModelRelation51(self):
        return self.__ryz_ControllerToModelRelation51

    @ryz_ControllerToModelRelation51.setter
    def ryz_ControllerToModelRelation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ControllerToModelRelation__ryz_ControllerToModelRelation51", None)
        self.__ryz_ControllerToModelRelation51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_Property52"):
                    opp_val = getattr(item, "ryz_Property52", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_Property52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_Property52"):
                    opp_val = getattr(item, "ryz_Property52", None)
                    
                    setattr(item, "ryz_Property52", self)
                    

    @property
    def ryz_ControllerToModelRelation(self):
        return self.__ryz_ControllerToModelRelation

    @ryz_ControllerToModelRelation.setter
    def ryz_ControllerToModelRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ControllerToModelRelation__ryz_ControllerToModelRelation", None)
        self.__ryz_ControllerToModelRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ActionMethod46"):
                opp_val = getattr(old_value, "ryz_ActionMethod46", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ActionMethod46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ActionMethod46"):
                opp_val = getattr(value, "ryz_ActionMethod46", None)
                setattr(value, "ryz_ActionMethod46", self)

class ryz_ViewToModelRelation(MainComponentRelation):

    def __init__(self, modelcardinality: str, ryz_ViewToModelRelation: "ryz_AbstractView" = None, ryz_ViewToModelRelation65: "ryz_Model" = None, ryz_ViewToModelRelation68: set["ryz_Property"] = None):
        self.modelcardinality = modelcardinality
        self.ryz_ViewToModelRelation = ryz_ViewToModelRelation
        self.ryz_ViewToModelRelation65 = ryz_ViewToModelRelation65
        self.ryz_ViewToModelRelation68 = ryz_ViewToModelRelation68 if ryz_ViewToModelRelation68 is not None else set()
        
    @property
    def modelcardinality(self) -> str:
        return self.__modelcardinality

    @modelcardinality.setter
    def modelcardinality(self, modelcardinality: str):
        self.__modelcardinality = modelcardinality

    @property
    def ryz_ViewToModelRelation68(self):
        return self.__ryz_ViewToModelRelation68

    @ryz_ViewToModelRelation68.setter
    def ryz_ViewToModelRelation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ViewToModelRelation__ryz_ViewToModelRelation68", None)
        self.__ryz_ViewToModelRelation68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_Property69"):
                    opp_val = getattr(item, "ryz_Property69", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_Property69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_Property69"):
                    opp_val = getattr(item, "ryz_Property69", None)
                    
                    setattr(item, "ryz_Property69", self)
                    

    @property
    def ryz_ViewToModelRelation(self):
        return self.__ryz_ViewToModelRelation

    @ryz_ViewToModelRelation.setter
    def ryz_ViewToModelRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ViewToModelRelation__ryz_ViewToModelRelation", None)
        self.__ryz_ViewToModelRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_AbstractView63"):
                opp_val = getattr(old_value, "ryz_AbstractView63", None)
                if opp_val == self:
                    setattr(old_value, "ryz_AbstractView63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_AbstractView63"):
                opp_val = getattr(value, "ryz_AbstractView63", None)
                setattr(value, "ryz_AbstractView63", self)

    @property
    def ryz_ViewToModelRelation65(self):
        return self.__ryz_ViewToModelRelation65

    @ryz_ViewToModelRelation65.setter
    def ryz_ViewToModelRelation65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ViewToModelRelation__ryz_ViewToModelRelation65", None)
        self.__ryz_ViewToModelRelation65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model66"):
                opp_val = getattr(old_value, "ryz_Model66", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model66"):
                opp_val = getattr(value, "ryz_Model66", None)
                setattr(value, "ryz_Model66", self)

class ryz_ViewToControllerRelation(MainComponentRelation):

    pass
class AbstractView:

    pass
class ryz_View(AbstractView):

    pass
class ryz_Layout(AbstractView):

    pass
class MainComponent:

    pass
class ryz_HelperForSendingRequest(ABC):

    def __init__(self, requestType: str, httpMethod: str, text: str, ryz_HelperForSendingRequest: "ryz_AbstractView" = None, ryz_HelperForSendingRequest35: "ryz_ViewToControllerRelation" = None, helperforsendingrequest56: set["ryz_PresentationElement"] = None, helperforsendingrequest: set["ryz_UseCase"] = None, HelperForSendingRequest83: "ryz_PresentationElement" = None, HelperForSendingRequest: "ryz_UseCase" = None, ryz_HelperForSendingRequest88: "ryz_FormElementToPropertyKeyRelation" = None):
        self.requestType = requestType
        self.httpMethod = httpMethod
        self.text = text
        self.ryz_HelperForSendingRequest = ryz_HelperForSendingRequest
        self.ryz_HelperForSendingRequest35 = ryz_HelperForSendingRequest35
        self.helperforsendingrequest56 = helperforsendingrequest56 if helperforsendingrequest56 is not None else set()
        self.helperforsendingrequest = helperforsendingrequest if helperforsendingrequest is not None else set()
        self.HelperForSendingRequest83 = HelperForSendingRequest83
        self.HelperForSendingRequest = HelperForSendingRequest
        self.ryz_HelperForSendingRequest88 = ryz_HelperForSendingRequest88
        
    @property
    def httpMethod(self) -> str:
        return self.__httpMethod

    @httpMethod.setter
    def httpMethod(self, httpMethod: str):
        self.__httpMethod = httpMethod

    @property
    def requestType(self) -> str:
        return self.__requestType

    @requestType.setter
    def requestType(self, requestType: str):
        self.__requestType = requestType

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ryz_HelperForSendingRequest88(self):
        return self.__ryz_HelperForSendingRequest88

    @ryz_HelperForSendingRequest88.setter
    def ryz_HelperForSendingRequest88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__ryz_HelperForSendingRequest88", None)
        self.__ryz_HelperForSendingRequest88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_FormElementToPropertyKeyRelation"):
                opp_val = getattr(old_value, "ryz_FormElementToPropertyKeyRelation", None)
                if opp_val == self:
                    setattr(old_value, "ryz_FormElementToPropertyKeyRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_FormElementToPropertyKeyRelation"):
                opp_val = getattr(value, "ryz_FormElementToPropertyKeyRelation", None)
                setattr(value, "ryz_FormElementToPropertyKeyRelation", self)

    @property
    def HelperForSendingRequest(self):
        return self.__HelperForSendingRequest

    @HelperForSendingRequest.setter
    def HelperForSendingRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__HelperForSendingRequest", None)
        self.__HelperForSendingRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usecase77"):
                opp_val = getattr(old_value, "usecase77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usecase77"):
                opp_val = getattr(value, "usecase77", None)
                if opp_val is None:
                    setattr(value, "usecase77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HelperForSendingRequest83(self):
        return self.__HelperForSendingRequest83

    @HelperForSendingRequest83.setter
    def HelperForSendingRequest83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__HelperForSendingRequest83", None)
        self.__HelperForSendingRequest83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "presentationelement"):
                opp_val = getattr(old_value, "presentationelement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "presentationelement"):
                opp_val = getattr(value, "presentationelement", None)
                if opp_val is None:
                    setattr(value, "presentationelement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_HelperForSendingRequest(self):
        return self.__ryz_HelperForSendingRequest

    @ryz_HelperForSendingRequest.setter
    def ryz_HelperForSendingRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__ryz_HelperForSendingRequest", None)
        self.__ryz_HelperForSendingRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_AbstractView19"):
                opp_val = getattr(old_value, "ryz_AbstractView19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_AbstractView19"):
                opp_val = getattr(value, "ryz_AbstractView19", None)
                if opp_val is None:
                    setattr(value, "ryz_AbstractView19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helperforsendingrequest(self):
        return self.__helperforsendingrequest

    @helperforsendingrequest.setter
    def helperforsendingrequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__helperforsendingrequest", None)
        self.__helperforsendingrequest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase54"):
                    opp_val = getattr(item, "UseCase54", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase54"):
                    opp_val = getattr(item, "UseCase54", None)
                    
                    setattr(item, "UseCase54", self)
                    

    @property
    def helperforsendingrequest56(self):
        return self.__helperforsendingrequest56

    @helperforsendingrequest56.setter
    def helperforsendingrequest56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__helperforsendingrequest56", None)
        self.__helperforsendingrequest56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PresentationElement"):
                    opp_val = getattr(item, "PresentationElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PresentationElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PresentationElement"):
                    opp_val = getattr(item, "PresentationElement", None)
                    
                    setattr(item, "PresentationElement", self)
                    

    @property
    def ryz_HelperForSendingRequest35(self):
        return self.__ryz_HelperForSendingRequest35

    @ryz_HelperForSendingRequest35.setter
    def ryz_HelperForSendingRequest35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_HelperForSendingRequest__ryz_HelperForSendingRequest35", None)
        self.__ryz_HelperForSendingRequest35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToControllerRelation"):
                opp_val = getattr(old_value, "ryz_ViewToControllerRelation", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ViewToControllerRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToControllerRelation"):
                opp_val = getattr(value, "ryz_ViewToControllerRelation", None)
                setattr(value, "ryz_ViewToControllerRelation", self)

class ryz_Partial(AbstractView):

    pass
class ryz_Model(MainComponent):

    def __init__(self, isAbstract: bool, ryz_Model: "ryz_ModelPackage" = None, ryz_Model10: set["ryz_Property"] = None, ryz_Model13: "ryz_Model" = None, ryz_Model11: "ryz_Model" = None, ryz_Model15: set["ryz_TableKey"] = None, ryz_Model26: "ryz_ModelAssociation" = None, ryz_Model29: "ryz_ModelAssociation" = None, ryz_Model41: "ryz_ViewToControllerRelation" = None, ryz_Model49: "ryz_ControllerToModelRelation" = None, ryz_Model66: "ryz_ViewToModelRelation" = None, ryz_Model91: "ryz_FormElementToPropertyKeyRelation" = None):
        self.isAbstract = isAbstract
        self.ryz_Model = ryz_Model
        self.ryz_Model10 = ryz_Model10 if ryz_Model10 is not None else set()
        self.ryz_Model13 = ryz_Model13
        self.ryz_Model11 = ryz_Model11
        self.ryz_Model15 = ryz_Model15 if ryz_Model15 is not None else set()
        self.ryz_Model26 = ryz_Model26
        self.ryz_Model29 = ryz_Model29
        self.ryz_Model41 = ryz_Model41
        self.ryz_Model49 = ryz_Model49
        self.ryz_Model66 = ryz_Model66
        self.ryz_Model91 = ryz_Model91
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def ryz_Model26(self):
        return self.__ryz_Model26

    @ryz_Model26.setter
    def ryz_Model26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model26", None)
        self.__ryz_Model26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ModelAssociation25"):
                opp_val = getattr(old_value, "ryz_ModelAssociation25", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ModelAssociation25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ModelAssociation25"):
                opp_val = getattr(value, "ryz_ModelAssociation25", None)
                setattr(value, "ryz_ModelAssociation25", self)

    @property
    def ryz_Model29(self):
        return self.__ryz_Model29

    @ryz_Model29.setter
    def ryz_Model29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model29", None)
        self.__ryz_Model29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ModelAssociation28"):
                opp_val = getattr(old_value, "ryz_ModelAssociation28", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ModelAssociation28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ModelAssociation28"):
                opp_val = getattr(value, "ryz_ModelAssociation28", None)
                setattr(value, "ryz_ModelAssociation28", self)

    @property
    def ryz_Model49(self):
        return self.__ryz_Model49

    @ryz_Model49.setter
    def ryz_Model49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model49", None)
        self.__ryz_Model49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ControllerToModelRelation48"):
                opp_val = getattr(old_value, "ryz_ControllerToModelRelation48", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ControllerToModelRelation48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ControllerToModelRelation48"):
                opp_val = getattr(value, "ryz_ControllerToModelRelation48", None)
                setattr(value, "ryz_ControllerToModelRelation48", self)

    @property
    def ryz_Model11(self):
        return self.__ryz_Model11

    @ryz_Model11.setter
    def ryz_Model11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model11", None)
        self.__ryz_Model11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model13"):
                opp_val = getattr(old_value, "ryz_Model13", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model13"):
                opp_val = getattr(value, "ryz_Model13", None)
                setattr(value, "ryz_Model13", self)

    @property
    def ryz_Model66(self):
        return self.__ryz_Model66

    @ryz_Model66.setter
    def ryz_Model66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model66", None)
        self.__ryz_Model66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToModelRelation65"):
                opp_val = getattr(old_value, "ryz_ViewToModelRelation65", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ViewToModelRelation65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToModelRelation65"):
                opp_val = getattr(value, "ryz_ViewToModelRelation65", None)
                setattr(value, "ryz_ViewToModelRelation65", self)

    @property
    def ryz_Model(self):
        return self.__ryz_Model

    @ryz_Model.setter
    def ryz_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model", None)
        self.__ryz_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ModelPackage"):
                opp_val = getattr(old_value, "ryz_ModelPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ModelPackage"):
                opp_val = getattr(value, "ryz_ModelPackage", None)
                if opp_val is None:
                    setattr(value, "ryz_ModelPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_Model41(self):
        return self.__ryz_Model41

    @ryz_Model41.setter
    def ryz_Model41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model41", None)
        self.__ryz_Model41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToControllerRelation40"):
                opp_val = getattr(old_value, "ryz_ViewToControllerRelation40", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ViewToControllerRelation40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToControllerRelation40"):
                opp_val = getattr(value, "ryz_ViewToControllerRelation40", None)
                setattr(value, "ryz_ViewToControllerRelation40", self)

    @property
    def ryz_Model91(self):
        return self.__ryz_Model91

    @ryz_Model91.setter
    def ryz_Model91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model91", None)
        self.__ryz_Model91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_FormElementToPropertyKeyRelation90"):
                opp_val = getattr(old_value, "ryz_FormElementToPropertyKeyRelation90", None)
                if opp_val == self:
                    setattr(old_value, "ryz_FormElementToPropertyKeyRelation90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_FormElementToPropertyKeyRelation90"):
                opp_val = getattr(value, "ryz_FormElementToPropertyKeyRelation90", None)
                setattr(value, "ryz_FormElementToPropertyKeyRelation90", self)

    @property
    def ryz_Model10(self):
        return self.__ryz_Model10

    @ryz_Model10.setter
    def ryz_Model10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model10", None)
        self.__ryz_Model10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_Property"):
                    opp_val = getattr(item, "ryz_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_Property"):
                    opp_val = getattr(item, "ryz_Property", None)
                    
                    setattr(item, "ryz_Property", self)
                    

    @property
    def ryz_Model13(self):
        return self.__ryz_Model13

    @ryz_Model13.setter
    def ryz_Model13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model13", None)
        self.__ryz_Model13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model11"):
                opp_val = getattr(old_value, "ryz_Model11", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model11"):
                opp_val = getattr(value, "ryz_Model11", None)
                setattr(value, "ryz_Model11", self)

    @property
    def ryz_Model15(self):
        return self.__ryz_Model15

    @ryz_Model15.setter
    def ryz_Model15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Model__ryz_Model15", None)
        self.__ryz_Model15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_TableKey"):
                    opp_val = getattr(item, "ryz_TableKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_TableKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_TableKey"):
                    opp_val = getattr(item, "ryz_TableKey", None)
                    
                    setattr(item, "ryz_TableKey", self)
                    

class ComponentPackage:

    pass
class ryz_ModelPackage(ComponentPackage):

    pass
class ryz_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ryz_Controller(MainComponent):

    pass
class ryz_ControllerPackage(ComponentPackage):

    pass
class ryz_AbstractView(MainComponent):

    pass
class ryz_ViewPackage(ComponentPackage):

    pass
class NamedElement:

    pass
class ryz_ModelAssociation(NamedElement):

    def __init__(self, cardinality: str, isRequired: bool, principalRoleName: str, dependentRoleName: str, ryz_ModelAssociation: "ryz_ModelPackage" = None, ryz_ModelAssociation25: "ryz_Model" = None, ryz_ModelAssociation28: "ryz_Model" = None):
        self.cardinality = cardinality
        self.isRequired = isRequired
        self.principalRoleName = principalRoleName
        self.dependentRoleName = dependentRoleName
        self.ryz_ModelAssociation = ryz_ModelAssociation
        self.ryz_ModelAssociation25 = ryz_ModelAssociation25
        self.ryz_ModelAssociation28 = ryz_ModelAssociation28
        
    @property
    def principalRoleName(self) -> str:
        return self.__principalRoleName

    @principalRoleName.setter
    def principalRoleName(self, principalRoleName: str):
        self.__principalRoleName = principalRoleName

    @property
    def dependentRoleName(self) -> str:
        return self.__dependentRoleName

    @dependentRoleName.setter
    def dependentRoleName(self, dependentRoleName: str):
        self.__dependentRoleName = dependentRoleName

    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def ryz_ModelAssociation25(self):
        return self.__ryz_ModelAssociation25

    @ryz_ModelAssociation25.setter
    def ryz_ModelAssociation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ModelAssociation__ryz_ModelAssociation25", None)
        self.__ryz_ModelAssociation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model26"):
                opp_val = getattr(old_value, "ryz_Model26", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model26"):
                opp_val = getattr(value, "ryz_Model26", None)
                setattr(value, "ryz_Model26", self)

    @property
    def ryz_ModelAssociation28(self):
        return self.__ryz_ModelAssociation28

    @ryz_ModelAssociation28.setter
    def ryz_ModelAssociation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ModelAssociation__ryz_ModelAssociation28", None)
        self.__ryz_ModelAssociation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model29"):
                opp_val = getattr(old_value, "ryz_Model29", None)
                if opp_val == self:
                    setattr(old_value, "ryz_Model29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model29"):
                opp_val = getattr(value, "ryz_Model29", None)
                setattr(value, "ryz_Model29", self)

    @property
    def ryz_ModelAssociation(self):
        return self.__ryz_ModelAssociation

    @ryz_ModelAssociation.setter
    def ryz_ModelAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ModelAssociation__ryz_ModelAssociation", None)
        self.__ryz_ModelAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ModelPackage6"):
                opp_val = getattr(old_value, "ryz_ModelPackage6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ModelPackage6"):
                opp_val = getattr(value, "ryz_ModelPackage6", None)
                if opp_val is None:
                    setattr(value, "ryz_ModelPackage6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ryz_PresentationElement(NamedElement):

    pass
class ryz_Property(NamedElement):

    def __init__(self, type: str, isRequired: bool, ryz_Property: "ryz_Model" = None, ryz_Property44: "ryz_ViewToControllerRelation" = None, ryz_Property52: "ryz_ControllerToModelRelation" = None, ryz_Property69: "ryz_ViewToModelRelation" = None, ryz_Property99: "ryz_PresentationFormElementToPropertyKey" = None):
        self.type = type
        self.isRequired = isRequired
        self.ryz_Property = ryz_Property
        self.ryz_Property44 = ryz_Property44
        self.ryz_Property52 = ryz_Property52
        self.ryz_Property69 = ryz_Property69
        self.ryz_Property99 = ryz_Property99
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def ryz_Property99(self):
        return self.__ryz_Property99

    @ryz_Property99.setter
    def ryz_Property99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Property__ryz_Property99", None)
        self.__ryz_Property99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_PresentationFormElementToPropertyKey98"):
                opp_val = getattr(old_value, "ryz_PresentationFormElementToPropertyKey98", None)
                if opp_val == self:
                    setattr(old_value, "ryz_PresentationFormElementToPropertyKey98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_PresentationFormElementToPropertyKey98"):
                opp_val = getattr(value, "ryz_PresentationFormElementToPropertyKey98", None)
                setattr(value, "ryz_PresentationFormElementToPropertyKey98", self)

    @property
    def ryz_Property52(self):
        return self.__ryz_Property52

    @ryz_Property52.setter
    def ryz_Property52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Property__ryz_Property52", None)
        self.__ryz_Property52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ControllerToModelRelation51"):
                opp_val = getattr(old_value, "ryz_ControllerToModelRelation51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ControllerToModelRelation51"):
                opp_val = getattr(value, "ryz_ControllerToModelRelation51", None)
                if opp_val is None:
                    setattr(value, "ryz_ControllerToModelRelation51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_Property69(self):
        return self.__ryz_Property69

    @ryz_Property69.setter
    def ryz_Property69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Property__ryz_Property69", None)
        self.__ryz_Property69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToModelRelation68"):
                opp_val = getattr(old_value, "ryz_ViewToModelRelation68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToModelRelation68"):
                opp_val = getattr(value, "ryz_ViewToModelRelation68", None)
                if opp_val is None:
                    setattr(value, "ryz_ViewToModelRelation68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_Property(self):
        return self.__ryz_Property

    @ryz_Property.setter
    def ryz_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Property__ryz_Property", None)
        self.__ryz_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model10"):
                opp_val = getattr(old_value, "ryz_Model10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model10"):
                opp_val = getattr(value, "ryz_Model10", None)
                if opp_val is None:
                    setattr(value, "ryz_Model10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_Property44(self):
        return self.__ryz_Property44

    @ryz_Property44.setter
    def ryz_Property44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Property__ryz_Property44", None)
        self.__ryz_Property44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToControllerRelation43"):
                opp_val = getattr(old_value, "ryz_ViewToControllerRelation43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToControllerRelation43"):
                opp_val = getattr(value, "ryz_ViewToControllerRelation43", None)
                if opp_val is None:
                    setattr(value, "ryz_ViewToControllerRelation43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ryz_TableKey(NamedElement):

    def __init__(self, type: str, isRequired: bool, isPrimaryKey: bool, isForeignKey: bool, ryz_TableKey: "ryz_Model" = None, ryz_TableKey102: "ryz_PresentationFormElementToPropertyKey" = None):
        self.type = type
        self.isRequired = isRequired
        self.isPrimaryKey = isPrimaryKey
        self.isForeignKey = isForeignKey
        self.ryz_TableKey = ryz_TableKey
        self.ryz_TableKey102 = ryz_TableKey102
        
    @property
    def isForeignKey(self) -> bool:
        return self.__isForeignKey

    @isForeignKey.setter
    def isForeignKey(self, isForeignKey: bool):
        self.__isForeignKey = isForeignKey

    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ryz_TableKey102(self):
        return self.__ryz_TableKey102

    @ryz_TableKey102.setter
    def ryz_TableKey102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_TableKey__ryz_TableKey102", None)
        self.__ryz_TableKey102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_PresentationFormElementToPropertyKey101"):
                opp_val = getattr(old_value, "ryz_PresentationFormElementToPropertyKey101", None)
                if opp_val == self:
                    setattr(old_value, "ryz_PresentationFormElementToPropertyKey101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_PresentationFormElementToPropertyKey101"):
                opp_val = getattr(value, "ryz_PresentationFormElementToPropertyKey101", None)
                setattr(value, "ryz_PresentationFormElementToPropertyKey101", self)

    @property
    def ryz_TableKey(self):
        return self.__ryz_TableKey

    @ryz_TableKey.setter
    def ryz_TableKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_TableKey__ryz_TableKey", None)
        self.__ryz_TableKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Model15"):
                opp_val = getattr(old_value, "ryz_Model15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Model15"):
                opp_val = getattr(value, "ryz_Model15", None)
                if opp_val is None:
                    setattr(value, "ryz_Model15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ryz_MainComponent(NamedElement):

    pass
class ryz_UseCase(NamedElement):

    pass
class ryz_ActionMethod(NamedElement):

    def __init__(self, returns: str, httpMethod: str, ryz_ActionMethod: "ryz_Controller" = None, ryz_ActionMethod31: set["ryz_Parameter"] = None, actionmethod: set["ryz_UseCase"] = None, ryz_ActionMethod38: "ryz_ViewToControllerRelation" = None, ryz_ActionMethod46: "ryz_ControllerToModelRelation" = None, ryz_ActionMethod58: "ryz_ControllerToViewRelation" = None, ActionMethod: "ryz_UseCase" = None):
        self.returns = returns
        self.httpMethod = httpMethod
        self.ryz_ActionMethod = ryz_ActionMethod
        self.ryz_ActionMethod31 = ryz_ActionMethod31 if ryz_ActionMethod31 is not None else set()
        self.actionmethod = actionmethod if actionmethod is not None else set()
        self.ryz_ActionMethod38 = ryz_ActionMethod38
        self.ryz_ActionMethod46 = ryz_ActionMethod46
        self.ryz_ActionMethod58 = ryz_ActionMethod58
        self.ActionMethod = ActionMethod
        
    @property
    def returns(self) -> str:
        return self.__returns

    @returns.setter
    def returns(self, returns: str):
        self.__returns = returns

    @property
    def httpMethod(self) -> str:
        return self.__httpMethod

    @httpMethod.setter
    def httpMethod(self, httpMethod: str):
        self.__httpMethod = httpMethod

    @property
    def ryz_ActionMethod(self):
        return self.__ryz_ActionMethod

    @ryz_ActionMethod.setter
    def ryz_ActionMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ryz_ActionMethod", None)
        self.__ryz_ActionMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_Controller23"):
                opp_val = getattr(old_value, "ryz_Controller23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_Controller23"):
                opp_val = getattr(value, "ryz_Controller23", None)
                if opp_val is None:
                    setattr(value, "ryz_Controller23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_ActionMethod58(self):
        return self.__ryz_ActionMethod58

    @ryz_ActionMethod58.setter
    def ryz_ActionMethod58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ryz_ActionMethod58", None)
        self.__ryz_ActionMethod58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ControllerToViewRelation"):
                opp_val = getattr(old_value, "ryz_ControllerToViewRelation", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ControllerToViewRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ControllerToViewRelation"):
                opp_val = getattr(value, "ryz_ControllerToViewRelation", None)
                setattr(value, "ryz_ControllerToViewRelation", self)

    @property
    def actionmethod(self):
        return self.__actionmethod

    @actionmethod.setter
    def actionmethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__actionmethod", None)
        self.__actionmethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase"):
                    opp_val = getattr(item, "UseCase", None)
                    
                    setattr(item, "UseCase", self)
                    

    @property
    def ActionMethod(self):
        return self.__ActionMethod

    @ActionMethod.setter
    def ActionMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ActionMethod", None)
        self.__ActionMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usecase79"):
                opp_val = getattr(old_value, "usecase79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usecase79"):
                opp_val = getattr(value, "usecase79", None)
                if opp_val is None:
                    setattr(value, "usecase79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ryz_ActionMethod38(self):
        return self.__ryz_ActionMethod38

    @ryz_ActionMethod38.setter
    def ryz_ActionMethod38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ryz_ActionMethod38", None)
        self.__ryz_ActionMethod38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ViewToControllerRelation37"):
                opp_val = getattr(old_value, "ryz_ViewToControllerRelation37", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ViewToControllerRelation37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ViewToControllerRelation37"):
                opp_val = getattr(value, "ryz_ViewToControllerRelation37", None)
                setattr(value, "ryz_ViewToControllerRelation37", self)

    @property
    def ryz_ActionMethod31(self):
        return self.__ryz_ActionMethod31

    @ryz_ActionMethod31.setter
    def ryz_ActionMethod31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ryz_ActionMethod31", None)
        self.__ryz_ActionMethod31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ryz_Parameter"):
                    opp_val = getattr(item, "ryz_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ryz_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ryz_Parameter"):
                    opp_val = getattr(item, "ryz_Parameter", None)
                    
                    setattr(item, "ryz_Parameter", self)
                    

    @property
    def ryz_ActionMethod46(self):
        return self.__ryz_ActionMethod46

    @ryz_ActionMethod46.setter
    def ryz_ActionMethod46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_ActionMethod__ryz_ActionMethod46", None)
        self.__ryz_ActionMethod46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ControllerToModelRelation"):
                opp_val = getattr(old_value, "ryz_ControllerToModelRelation", None)
                if opp_val == self:
                    setattr(old_value, "ryz_ControllerToModelRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ControllerToModelRelation"):
                opp_val = getattr(value, "ryz_ControllerToModelRelation", None)
                setattr(value, "ryz_ControllerToModelRelation", self)

class ryz_Parameter(NamedElement):

    def __init__(self, type: str, isNullable: bool, isList: bool, ryz_Parameter: "ryz_ActionMethod" = None):
        self.type = type
        self.isNullable = isNullable
        self.isList = isList
        self.ryz_Parameter = ryz_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

    @property
    def isNullable(self) -> bool:
        return self.__isNullable

    @isNullable.setter
    def isNullable(self, isNullable: bool):
        self.__isNullable = isNullable

    @property
    def ryz_Parameter(self):
        return self.__ryz_Parameter

    @ryz_Parameter.setter
    def ryz_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ryz_Parameter__ryz_Parameter", None)
        self.__ryz_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ryz_ActionMethod31"):
                opp_val = getattr(old_value, "ryz_ActionMethod31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ryz_ActionMethod31"):
                opp_val = getattr(value, "ryz_ActionMethod31", None)
                if opp_val is None:
                    setattr(value, "ryz_ActionMethod31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ryz_MainComponentRelation(NamedElement):

    pass
class ryz_Actor(NamedElement):

    pass
class ryz_UseCasePackage(NamedElement):

    pass
class ryz_Project(NamedElement):

    pass
class Package:

    pass
class ryz_UseCaseActorPackage(Package):

    pass
class ryz_MvcPackage(Package):

    pass
class ryz_ComponentPackage(Package):

    pass
class ryz_Package(NamedElement):

    pass
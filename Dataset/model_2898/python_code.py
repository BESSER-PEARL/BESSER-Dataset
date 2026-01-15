from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PropertyNameLiteral(Enum):
    STYLE = "STYLE"
    PATH = "PATH"
    LABEL_PROVIDER = "LABEL_PROVIDER"
    CSS_ITEM = "CSS_ITEM"
    TOOLTIP = "TOOLTIP"
    RESOURCE_KEY = "RESOURCE_KEY"
    TYPE = "TYPE"
    COLUMNS = "COLUMNS"
class ContentElementLiteral(Enum):
    TEXT = "TEXT"
    BUTTON = "BUTTON"
    LABEL = "LABEL"
    LIST = "LIST"
    IMAGE = "IMAGE"
class ContainerElementLiteral(Enum):
    LAYOUT = "LAYOUT"
    SCREEN = "SCREEN"
class UIElementReceiverKey(Enum):
    SELECTION = "SELECTION"
    VALUES_ = "VALUES_"
    ON_SELECTION = "ON_SELECTION"
    TEXT = "TEXT"


############################################
# Definition of Classes
############################################

class domainmodel_SystemModule:

    pass
class BusinessModule:

    pass
class domainmodel_BusinessFeatures(BusinessModule):

    pass
class domainmodel_BusinessFeatureType:

    pass
class SystemModule:

    pass
class domainmodel_BusinessModule(SystemModule):

    pass
class domainmodel_UIModule(SystemModule):

    pass
class domainmodel_UIFeature:

    pass
class UIFeature:

    pass
class domainmodel_MainFeature(UIFeature):

    pass
class domainmodel_ScreenModule:

    pass
class domainmodel_ControllerElement:

    pass
class domainmodel_UIActionFeature:

    pass
class domainmodel_BusinessFeature:

    def __init__(self, name: str, connectPoint1: str, connectEnd: str, domainmodel_BusinessFeature: "domainmodel_InterfaceMethodCall" = None, domainmodel_BusinessFeature105: "domainmodel_BusinessFeatureType" = None, domainmodel_BusinessFeature108: "domainmodel_BusinessFeature" = None, domainmodel_BusinessFeature106: "domainmodel_BusinessFeature" = None, domainmodel_BusinessFeature110: "domainmodel_BusinessFeatures" = None):
        self.name = name
        self.connectPoint1 = connectPoint1
        self.connectEnd = connectEnd
        self.domainmodel_BusinessFeature = domainmodel_BusinessFeature
        self.domainmodel_BusinessFeature105 = domainmodel_BusinessFeature105
        self.domainmodel_BusinessFeature108 = domainmodel_BusinessFeature108
        self.domainmodel_BusinessFeature106 = domainmodel_BusinessFeature106
        self.domainmodel_BusinessFeature110 = domainmodel_BusinessFeature110
        
    @property
    def connectEnd(self) -> str:
        return self.__connectEnd

    @connectEnd.setter
    def connectEnd(self, connectEnd: str):
        self.__connectEnd = connectEnd

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def connectPoint1(self) -> str:
        return self.__connectPoint1

    @connectPoint1.setter
    def connectPoint1(self, connectPoint1: str):
        self.__connectPoint1 = connectPoint1

    @property
    def domainmodel_BusinessFeature(self):
        return self.__domainmodel_BusinessFeature

    @domainmodel_BusinessFeature.setter
    def domainmodel_BusinessFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BusinessFeature__domainmodel_BusinessFeature", None)
        self.__domainmodel_BusinessFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceMethodCall"):
                opp_val = getattr(old_value, "domainmodel_InterfaceMethodCall", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceMethodCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceMethodCall"):
                opp_val = getattr(value, "domainmodel_InterfaceMethodCall", None)
                setattr(value, "domainmodel_InterfaceMethodCall", self)

    @property
    def domainmodel_BusinessFeature110(self):
        return self.__domainmodel_BusinessFeature110

    @domainmodel_BusinessFeature110.setter
    def domainmodel_BusinessFeature110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BusinessFeature__domainmodel_BusinessFeature110", None)
        self.__domainmodel_BusinessFeature110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BusinessFeatures"):
                opp_val = getattr(old_value, "domainmodel_BusinessFeatures", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BusinessFeatures"):
                opp_val = getattr(value, "domainmodel_BusinessFeatures", None)
                if opp_val is None:
                    setattr(value, "domainmodel_BusinessFeatures", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_BusinessFeature106(self):
        return self.__domainmodel_BusinessFeature106

    @domainmodel_BusinessFeature106.setter
    def domainmodel_BusinessFeature106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BusinessFeature__domainmodel_BusinessFeature106", None)
        self.__domainmodel_BusinessFeature106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BusinessFeature108"):
                opp_val = getattr(old_value, "domainmodel_BusinessFeature108", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BusinessFeature108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BusinessFeature108"):
                opp_val = getattr(value, "domainmodel_BusinessFeature108", None)
                setattr(value, "domainmodel_BusinessFeature108", self)

    @property
    def domainmodel_BusinessFeature108(self):
        return self.__domainmodel_BusinessFeature108

    @domainmodel_BusinessFeature108.setter
    def domainmodel_BusinessFeature108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BusinessFeature__domainmodel_BusinessFeature108", None)
        self.__domainmodel_BusinessFeature108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BusinessFeature106"):
                opp_val = getattr(old_value, "domainmodel_BusinessFeature106", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BusinessFeature106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BusinessFeature106"):
                opp_val = getattr(value, "domainmodel_BusinessFeature106", None)
                setattr(value, "domainmodel_BusinessFeature106", self)

    @property
    def domainmodel_BusinessFeature105(self):
        return self.__domainmodel_BusinessFeature105

    @domainmodel_BusinessFeature105.setter
    def domainmodel_BusinessFeature105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BusinessFeature__domainmodel_BusinessFeature105", None)
        self.__domainmodel_BusinessFeature105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BusinessFeatureType"):
                opp_val = getattr(old_value, "domainmodel_BusinessFeatureType", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BusinessFeatureType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BusinessFeatureType"):
                opp_val = getattr(value, "domainmodel_BusinessFeatureType", None)
                setattr(value, "domainmodel_BusinessFeatureType", self)

class domainmodel_InterfaceMethodCallParameters:

    pass
class domainmodel_InterfaceMethodCallParameter:

    def __init__(self, parameterType: str, domainmodel_InterfaceMethodCallParameter: "domainmodel_MethodParameter" = None, domainmodel_InterfaceMethodCallParameter89: "domainmodel_InterfaceMethodCallParameters" = None):
        self.parameterType = parameterType
        self.domainmodel_InterfaceMethodCallParameter = domainmodel_InterfaceMethodCallParameter
        self.domainmodel_InterfaceMethodCallParameter89 = domainmodel_InterfaceMethodCallParameter89
        
    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

    @property
    def domainmodel_InterfaceMethodCallParameter89(self):
        return self.__domainmodel_InterfaceMethodCallParameter89

    @domainmodel_InterfaceMethodCallParameter89.setter
    def domainmodel_InterfaceMethodCallParameter89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceMethodCallParameter__domainmodel_InterfaceMethodCallParameter89", None)
        self.__domainmodel_InterfaceMethodCallParameter89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceMethodCallParameters"):
                opp_val = getattr(old_value, "domainmodel_InterfaceMethodCallParameters", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceMethodCallParameters"):
                opp_val = getattr(value, "domainmodel_InterfaceMethodCallParameters", None)
                if opp_val is None:
                    setattr(value, "domainmodel_InterfaceMethodCallParameters", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_InterfaceMethodCallParameter(self):
        return self.__domainmodel_InterfaceMethodCallParameter

    @domainmodel_InterfaceMethodCallParameter.setter
    def domainmodel_InterfaceMethodCallParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceMethodCallParameter__domainmodel_InterfaceMethodCallParameter", None)
        self.__domainmodel_InterfaceMethodCallParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_MethodParameter87"):
                opp_val = getattr(old_value, "domainmodel_MethodParameter87", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_MethodParameter87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_MethodParameter87"):
                opp_val = getattr(value, "domainmodel_MethodParameter87", None)
                setattr(value, "domainmodel_MethodParameter87", self)

class domainmodel_SetActionReceiver:

    pass
class domainmodel_MainFeatureOption:

    def __init__(self, name: str, domainmodel_MainFeatureOption: "domainmodel_MainFeature" = None):
        self.name = name
        self.domainmodel_MainFeatureOption = domainmodel_MainFeatureOption
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_MainFeatureOption(self):
        return self.__domainmodel_MainFeatureOption

    @domainmodel_MainFeatureOption.setter
    def domainmodel_MainFeatureOption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MainFeatureOption__domainmodel_MainFeatureOption", None)
        self.__domainmodel_MainFeatureOption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_MainFeature"):
                opp_val = getattr(old_value, "domainmodel_MainFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_MainFeature"):
                opp_val = getattr(value, "domainmodel_MainFeature", None)
                if opp_val is None:
                    setattr(value, "domainmodel_MainFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SetActionReceiver:

    pass
class domainmodel_SetRestCallReceiver(SetActionReceiver):

    pass
class domainmodel_SetRestCallReceiverParameters:

    pass
class domainmodel_SetRestCallReceiverParameter:

    pass
class SetRestCallReceiverParameter:

    pass
class domainmodel_SetRestCallReceiverIDParameter(SetRestCallReceiverParameter):

    def __init__(self, parameterType: str):
        self.parameterType = parameterType
        
    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

class domainmodel_SetRestCallReceiverReturnTypeParameter(SetRestCallReceiverParameter):

    pass
class domainmodel_SetRestCallReceiverURLParameter(SetRestCallReceiverParameter):

    def __init__(self, parameterType: str):
        self.parameterType = parameterType
        
    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

class domainmodel_ScreenFeature(UIFeature):

    def __init__(self, name: str, domainmodel_ScreenFeature: "domainmodel_NavigateToAction" = None, domainmodel_ScreenFeature101: set["domainmodel_ScreenModule"] = None):
        self.name = name
        self.domainmodel_ScreenFeature = domainmodel_ScreenFeature
        self.domainmodel_ScreenFeature101 = domainmodel_ScreenFeature101 if domainmodel_ScreenFeature101 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_ScreenFeature101(self):
        return self.__domainmodel_ScreenFeature101

    @domainmodel_ScreenFeature101.setter
    def domainmodel_ScreenFeature101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ScreenFeature__domainmodel_ScreenFeature101", None)
        self.__domainmodel_ScreenFeature101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_ScreenModule"):
                    opp_val = getattr(item, "domainmodel_ScreenModule", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_ScreenModule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_ScreenModule"):
                    opp_val = getattr(item, "domainmodel_ScreenModule", None)
                    
                    setattr(item, "domainmodel_ScreenModule", self)
                    

    @property
    def domainmodel_ScreenFeature(self):
        return self.__domainmodel_ScreenFeature

    @domainmodel_ScreenFeature.setter
    def domainmodel_ScreenFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ScreenFeature__domainmodel_ScreenFeature", None)
        self.__domainmodel_ScreenFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_NavigateToAction"):
                opp_val = getattr(old_value, "domainmodel_NavigateToAction", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_NavigateToAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_NavigateToAction"):
                opp_val = getattr(value, "domainmodel_NavigateToAction", None)
                setattr(value, "domainmodel_NavigateToAction", self)

class UIActionFeature:

    pass
class domainmodel_ExecuteAction(UIActionFeature):

    pass
class domainmodel_InterfaceMethodCall(UIActionFeature):

    pass
class domainmodel_NavigateToAction(UIActionFeature):

    pass
class domainmodel_ScreenModelParameters:

    pass
class domainmodel_ScreenModelParameter:

    def __init__(self, modelFeatureValue: str, domainmodel_ScreenModelParameter: "domainmodel_ModelFeature" = None, domainmodel_ScreenModelParameter67: "domainmodel_ScreenModelParameters" = None):
        self.modelFeatureValue = modelFeatureValue
        self.domainmodel_ScreenModelParameter = domainmodel_ScreenModelParameter
        self.domainmodel_ScreenModelParameter67 = domainmodel_ScreenModelParameter67
        
    @property
    def modelFeatureValue(self) -> str:
        return self.__modelFeatureValue

    @modelFeatureValue.setter
    def modelFeatureValue(self, modelFeatureValue: str):
        self.__modelFeatureValue = modelFeatureValue

    @property
    def domainmodel_ScreenModelParameter(self):
        return self.__domainmodel_ScreenModelParameter

    @domainmodel_ScreenModelParameter.setter
    def domainmodel_ScreenModelParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ScreenModelParameter__domainmodel_ScreenModelParameter", None)
        self.__domainmodel_ScreenModelParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ModelFeature65"):
                opp_val = getattr(old_value, "domainmodel_ModelFeature65", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ModelFeature65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ModelFeature65"):
                opp_val = getattr(value, "domainmodel_ModelFeature65", None)
                setattr(value, "domainmodel_ModelFeature65", self)

    @property
    def domainmodel_ScreenModelParameter67(self):
        return self.__domainmodel_ScreenModelParameter67

    @domainmodel_ScreenModelParameter67.setter
    def domainmodel_ScreenModelParameter67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ScreenModelParameter__domainmodel_ScreenModelParameter67", None)
        self.__domainmodel_ScreenModelParameter67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ScreenModelParameters"):
                opp_val = getattr(old_value, "domainmodel_ScreenModelParameters", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ScreenModelParameters"):
                opp_val = getattr(value, "domainmodel_ScreenModelParameters", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ScreenModelParameters", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_ValidatorRules:

    pass
class domainmodel_ValidatorRule:

    def __init__(self, stringRule: str, domainmodel_ValidatorRule: "domainmodel_ValidatorFeature" = None, domainmodel_ValidatorRule58: "domainmodel_ValidatorRules" = None):
        self.stringRule = stringRule
        self.domainmodel_ValidatorRule = domainmodel_ValidatorRule
        self.domainmodel_ValidatorRule58 = domainmodel_ValidatorRule58
        
    @property
    def stringRule(self) -> str:
        return self.__stringRule

    @stringRule.setter
    def stringRule(self, stringRule: str):
        self.__stringRule = stringRule

    @property
    def domainmodel_ValidatorRule(self):
        return self.__domainmodel_ValidatorRule

    @domainmodel_ValidatorRule.setter
    def domainmodel_ValidatorRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorRule__domainmodel_ValidatorRule", None)
        self.__domainmodel_ValidatorRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidatorFeature56"):
                opp_val = getattr(old_value, "domainmodel_ValidatorFeature56", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ValidatorFeature56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidatorFeature56"):
                opp_val = getattr(value, "domainmodel_ValidatorFeature56", None)
                setattr(value, "domainmodel_ValidatorFeature56", self)

    @property
    def domainmodel_ValidatorRule58(self):
        return self.__domainmodel_ValidatorRule58

    @domainmodel_ValidatorRule58.setter
    def domainmodel_ValidatorRule58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorRule__domainmodel_ValidatorRule58", None)
        self.__domainmodel_ValidatorRule58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidatorRules"):
                opp_val = getattr(old_value, "domainmodel_ValidatorRules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidatorRules"):
                opp_val = getattr(value, "domainmodel_ValidatorRules", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ValidatorRules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_InitActionFeature:

    pass
class domainmodel_BindSource:

    pass
class BindSource:

    pass
class domainmodel_BindEnumSource(BindSource):

    def __init__(self, enumType: str):
        self.enumType = enumType
        
    @property
    def enumType(self) -> str:
        return self.__enumType

    @enumType.setter
    def enumType(self, enumType: str):
        self.__enumType = enumType

class domainmodel_SetUIElementReceiver(SetActionReceiver):

    def __init__(self, uiKey: str, domainmodel_SetUIElementReceiver: "domainmodel_ValidateAction" = None, domainmodel_SetUIElementReceiver46: "domainmodel_AttachAction" = None, domainmodel_SetUIElementReceiver53: "domainmodel_BindAction" = None, domainmodel_SetUIElementReceiver80: "domainmodel_ViewElement" = None):
        self.uiKey = uiKey
        self.domainmodel_SetUIElementReceiver = domainmodel_SetUIElementReceiver
        self.domainmodel_SetUIElementReceiver46 = domainmodel_SetUIElementReceiver46
        self.domainmodel_SetUIElementReceiver53 = domainmodel_SetUIElementReceiver53
        self.domainmodel_SetUIElementReceiver80 = domainmodel_SetUIElementReceiver80
        
    @property
    def uiKey(self) -> str:
        return self.__uiKey

    @uiKey.setter
    def uiKey(self, uiKey: str):
        self.__uiKey = uiKey

    @property
    def domainmodel_SetUIElementReceiver46(self):
        return self.__domainmodel_SetUIElementReceiver46

    @domainmodel_SetUIElementReceiver46.setter
    def domainmodel_SetUIElementReceiver46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_SetUIElementReceiver__domainmodel_SetUIElementReceiver46", None)
        self.__domainmodel_SetUIElementReceiver46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_AttachAction45"):
                opp_val = getattr(old_value, "domainmodel_AttachAction45", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_AttachAction45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_AttachAction45"):
                opp_val = getattr(value, "domainmodel_AttachAction45", None)
                setattr(value, "domainmodel_AttachAction45", self)

    @property
    def domainmodel_SetUIElementReceiver(self):
        return self.__domainmodel_SetUIElementReceiver

    @domainmodel_SetUIElementReceiver.setter
    def domainmodel_SetUIElementReceiver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_SetUIElementReceiver__domainmodel_SetUIElementReceiver", None)
        self.__domainmodel_SetUIElementReceiver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidateAction42"):
                opp_val = getattr(old_value, "domainmodel_ValidateAction42", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ValidateAction42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidateAction42"):
                opp_val = getattr(value, "domainmodel_ValidateAction42", None)
                setattr(value, "domainmodel_ValidateAction42", self)

    @property
    def domainmodel_SetUIElementReceiver53(self):
        return self.__domainmodel_SetUIElementReceiver53

    @domainmodel_SetUIElementReceiver53.setter
    def domainmodel_SetUIElementReceiver53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_SetUIElementReceiver__domainmodel_SetUIElementReceiver53", None)
        self.__domainmodel_SetUIElementReceiver53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BindAction52"):
                opp_val = getattr(old_value, "domainmodel_BindAction52", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BindAction52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BindAction52"):
                opp_val = getattr(value, "domainmodel_BindAction52", None)
                setattr(value, "domainmodel_BindAction52", self)

    @property
    def domainmodel_SetUIElementReceiver80(self):
        return self.__domainmodel_SetUIElementReceiver80

    @domainmodel_SetUIElementReceiver80.setter
    def domainmodel_SetUIElementReceiver80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_SetUIElementReceiver__domainmodel_SetUIElementReceiver80", None)
        self.__domainmodel_SetUIElementReceiver80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ViewElement81"):
                opp_val = getattr(old_value, "domainmodel_ViewElement81", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ViewElement81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ViewElement81"):
                opp_val = getattr(value, "domainmodel_ViewElement81", None)
                setattr(value, "domainmodel_ViewElement81", self)

class domainmodel_ValidatorFeature:

    def __init__(self, name: str, domainmodel_ValidatorFeature: "domainmodel_ValidateAction" = None, domainmodel_ValidatorFeature56: "domainmodel_ValidatorRule" = None, domainmodel_ValidatorFeature60: "domainmodel_ValidatorRules" = None, domainmodel_ValidatorFeature63: "domainmodel_ValidatorModule" = None):
        self.name = name
        self.domainmodel_ValidatorFeature = domainmodel_ValidatorFeature
        self.domainmodel_ValidatorFeature56 = domainmodel_ValidatorFeature56
        self.domainmodel_ValidatorFeature60 = domainmodel_ValidatorFeature60
        self.domainmodel_ValidatorFeature63 = domainmodel_ValidatorFeature63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_ValidatorFeature56(self):
        return self.__domainmodel_ValidatorFeature56

    @domainmodel_ValidatorFeature56.setter
    def domainmodel_ValidatorFeature56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorFeature__domainmodel_ValidatorFeature56", None)
        self.__domainmodel_ValidatorFeature56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidatorRule"):
                opp_val = getattr(old_value, "domainmodel_ValidatorRule", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ValidatorRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidatorRule"):
                opp_val = getattr(value, "domainmodel_ValidatorRule", None)
                setattr(value, "domainmodel_ValidatorRule", self)

    @property
    def domainmodel_ValidatorFeature(self):
        return self.__domainmodel_ValidatorFeature

    @domainmodel_ValidatorFeature.setter
    def domainmodel_ValidatorFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorFeature__domainmodel_ValidatorFeature", None)
        self.__domainmodel_ValidatorFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidateAction"):
                opp_val = getattr(old_value, "domainmodel_ValidateAction", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ValidateAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidateAction"):
                opp_val = getattr(value, "domainmodel_ValidateAction", None)
                setattr(value, "domainmodel_ValidateAction", self)

    @property
    def domainmodel_ValidatorFeature60(self):
        return self.__domainmodel_ValidatorFeature60

    @domainmodel_ValidatorFeature60.setter
    def domainmodel_ValidatorFeature60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorFeature__domainmodel_ValidatorFeature60", None)
        self.__domainmodel_ValidatorFeature60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidatorRules61"):
                opp_val = getattr(old_value, "domainmodel_ValidatorRules61", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ValidatorRules61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidatorRules61"):
                opp_val = getattr(value, "domainmodel_ValidatorRules61", None)
                setattr(value, "domainmodel_ValidatorRules61", self)

    @property
    def domainmodel_ValidatorFeature63(self):
        return self.__domainmodel_ValidatorFeature63

    @domainmodel_ValidatorFeature63.setter
    def domainmodel_ValidatorFeature63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ValidatorFeature__domainmodel_ValidatorFeature63", None)
        self.__domainmodel_ValidatorFeature63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ValidatorModule"):
                opp_val = getattr(old_value, "domainmodel_ValidatorModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ValidatorModule"):
                opp_val = getattr(value, "domainmodel_ValidatorModule", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ValidatorModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class InitActionFeature:

    pass
class domainmodel_SetAction(UIActionFeature, InitActionFeature):

    pass
class domainmodel_BindAction(InitActionFeature):

    def __init__(self, attribute: str, domainmodel_BindAction: "domainmodel_BindSource" = None, domainmodel_BindAction52: "domainmodel_SetUIElementReceiver" = None):
        self.attribute = attribute
        self.domainmodel_BindAction = domainmodel_BindAction
        self.domainmodel_BindAction52 = domainmodel_BindAction52
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def domainmodel_BindAction52(self):
        return self.__domainmodel_BindAction52

    @domainmodel_BindAction52.setter
    def domainmodel_BindAction52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BindAction__domainmodel_BindAction52", None)
        self.__domainmodel_BindAction52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_SetUIElementReceiver53"):
                opp_val = getattr(old_value, "domainmodel_SetUIElementReceiver53", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_SetUIElementReceiver53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_SetUIElementReceiver53"):
                opp_val = getattr(value, "domainmodel_SetUIElementReceiver53", None)
                setattr(value, "domainmodel_SetUIElementReceiver53", self)

    @property
    def domainmodel_BindAction(self):
        return self.__domainmodel_BindAction

    @domainmodel_BindAction.setter
    def domainmodel_BindAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_BindAction__domainmodel_BindAction", None)
        self.__domainmodel_BindAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BindSource50"):
                opp_val = getattr(old_value, "domainmodel_BindSource50", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BindSource50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BindSource50"):
                opp_val = getattr(value, "domainmodel_BindSource50", None)
                setattr(value, "domainmodel_BindSource50", self)

class domainmodel_AttachAction(InitActionFeature):

    pass
class domainmodel_ValidateAction(InitActionFeature):

    pass
class domainmodel_ViewElement:

    def __init__(self, name: str, domainmodel_ViewElement: "domainmodel_ContainerElement" = None, domainmodel_ViewElement37: set["domainmodel_ElementFeature"] = None, domainmodel_ViewElement39: "domainmodel_ViewModule" = None, domainmodel_ViewElement81: "domainmodel_SetUIElementReceiver" = None):
        self.name = name
        self.domainmodel_ViewElement = domainmodel_ViewElement
        self.domainmodel_ViewElement37 = domainmodel_ViewElement37 if domainmodel_ViewElement37 is not None else set()
        self.domainmodel_ViewElement39 = domainmodel_ViewElement39
        self.domainmodel_ViewElement81 = domainmodel_ViewElement81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_ViewElement(self):
        return self.__domainmodel_ViewElement

    @domainmodel_ViewElement.setter
    def domainmodel_ViewElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ViewElement__domainmodel_ViewElement", None)
        self.__domainmodel_ViewElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ContainerElement"):
                opp_val = getattr(old_value, "domainmodel_ContainerElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ContainerElement"):
                opp_val = getattr(value, "domainmodel_ContainerElement", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ContainerElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_ViewElement81(self):
        return self.__domainmodel_ViewElement81

    @domainmodel_ViewElement81.setter
    def domainmodel_ViewElement81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ViewElement__domainmodel_ViewElement81", None)
        self.__domainmodel_ViewElement81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_SetUIElementReceiver80"):
                opp_val = getattr(old_value, "domainmodel_SetUIElementReceiver80", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_SetUIElementReceiver80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_SetUIElementReceiver80"):
                opp_val = getattr(value, "domainmodel_SetUIElementReceiver80", None)
                setattr(value, "domainmodel_SetUIElementReceiver80", self)

    @property
    def domainmodel_ViewElement39(self):
        return self.__domainmodel_ViewElement39

    @domainmodel_ViewElement39.setter
    def domainmodel_ViewElement39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ViewElement__domainmodel_ViewElement39", None)
        self.__domainmodel_ViewElement39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ViewModule"):
                opp_val = getattr(old_value, "domainmodel_ViewModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ViewModule"):
                opp_val = getattr(value, "domainmodel_ViewModule", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ViewModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_ViewElement37(self):
        return self.__domainmodel_ViewElement37

    @domainmodel_ViewElement37.setter
    def domainmodel_ViewElement37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ViewElement__domainmodel_ViewElement37", None)
        self.__domainmodel_ViewElement37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_ElementFeature"):
                    opp_val = getattr(item, "domainmodel_ElementFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_ElementFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_ElementFeature"):
                    opp_val = getattr(item, "domainmodel_ElementFeature", None)
                    
                    setattr(item, "domainmodel_ElementFeature", self)
                    

class ViewElement:

    pass
class domainmodel_ContainerElement(ViewElement):

    def __init__(self, container: str, domainmodel_ContainerElement: set["domainmodel_ViewElement"] = None):
        self.container = container
        self.domainmodel_ContainerElement = domainmodel_ContainerElement if domainmodel_ContainerElement is not None else set()
        
    @property
    def container(self) -> str:
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container

    @property
    def domainmodel_ContainerElement(self):
        return self.__domainmodel_ContainerElement

    @domainmodel_ContainerElement.setter
    def domainmodel_ContainerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ContainerElement__domainmodel_ContainerElement", None)
        self.__domainmodel_ContainerElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_ViewElement"):
                    opp_val = getattr(item, "domainmodel_ViewElement", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_ViewElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_ViewElement"):
                    opp_val = getattr(item, "domainmodel_ViewElement", None)
                    
                    setattr(item, "domainmodel_ViewElement", self)
                    

class domainmodel_ContentElement(ViewElement):

    def __init__(self, contentElement: str):
        self.contentElement = contentElement
        
    @property
    def contentElement(self) -> str:
        return self.__contentElement

    @contentElement.setter
    def contentElement(self, contentElement: str):
        self.__contentElement = contentElement

class domainmodel_ElementFeature:

    def __init__(self, propertyName: str, propertyValue: str, domainmodel_ElementFeature: "domainmodel_ViewElement" = None):
        self.propertyName = propertyName
        self.propertyValue = propertyValue
        self.domainmodel_ElementFeature = domainmodel_ElementFeature
        
    @property
    def propertyValue(self) -> str:
        return self.__propertyValue

    @propertyValue.setter
    def propertyValue(self, propertyValue: str):
        self.__propertyValue = propertyValue

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def domainmodel_ElementFeature(self):
        return self.__domainmodel_ElementFeature

    @domainmodel_ElementFeature.setter
    def domainmodel_ElementFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ElementFeature__domainmodel_ElementFeature", None)
        self.__domainmodel_ElementFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ViewElement37"):
                opp_val = getattr(old_value, "domainmodel_ViewElement37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ViewElement37"):
                opp_val = getattr(value, "domainmodel_ViewElement37", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ViewElement37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ControllerElement:

    pass
class domainmodel_ValidatorModule(ControllerElement):

    pass
class domainmodel_UIActionModule(ControllerElement):

    def __init__(self, name: str, domainmodel_UIActionModule: "domainmodel_AttachAction" = None, domainmodel_UIActionModule73: "domainmodel_ExecuteAction" = None, domainmodel_UIActionModule98: set["domainmodel_UIActionFeature"] = None):
        self.name = name
        self.domainmodel_UIActionModule = domainmodel_UIActionModule
        self.domainmodel_UIActionModule73 = domainmodel_UIActionModule73
        self.domainmodel_UIActionModule98 = domainmodel_UIActionModule98 if domainmodel_UIActionModule98 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_UIActionModule98(self):
        return self.__domainmodel_UIActionModule98

    @domainmodel_UIActionModule98.setter
    def domainmodel_UIActionModule98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_UIActionModule__domainmodel_UIActionModule98", None)
        self.__domainmodel_UIActionModule98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_UIActionFeature"):
                    opp_val = getattr(item, "domainmodel_UIActionFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_UIActionFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_UIActionFeature"):
                    opp_val = getattr(item, "domainmodel_UIActionFeature", None)
                    
                    setattr(item, "domainmodel_UIActionFeature", self)
                    

    @property
    def domainmodel_UIActionModule(self):
        return self.__domainmodel_UIActionModule

    @domainmodel_UIActionModule.setter
    def domainmodel_UIActionModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_UIActionModule__domainmodel_UIActionModule", None)
        self.__domainmodel_UIActionModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_AttachAction"):
                opp_val = getattr(old_value, "domainmodel_AttachAction", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_AttachAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_AttachAction"):
                opp_val = getattr(value, "domainmodel_AttachAction", None)
                setattr(value, "domainmodel_AttachAction", self)

    @property
    def domainmodel_UIActionModule73(self):
        return self.__domainmodel_UIActionModule73

    @domainmodel_UIActionModule73.setter
    def domainmodel_UIActionModule73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_UIActionModule__domainmodel_UIActionModule73", None)
        self.__domainmodel_UIActionModule73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ExecuteAction"):
                opp_val = getattr(old_value, "domainmodel_ExecuteAction", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ExecuteAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ExecuteAction"):
                opp_val = getattr(value, "domainmodel_ExecuteAction", None)
                setattr(value, "domainmodel_ExecuteAction", self)

class domainmodel_InitActionModule(ControllerElement):

    pass
class domainmodel_ModelFeature:

    def __init__(self, name: str, domainmodel_ModelFeature: "domainmodel_EntryParametersModule" = None, domainmodel_ModelFeature31: "domainmodel_Type" = None, domainmodel_ModelFeature34: "domainmodel_ModelModule" = None, domainmodel_ModelFeature48: "domainmodel_BindSource" = None, domainmodel_ModelFeature65: "domainmodel_ScreenModelParameter" = None, domainmodel_ModelFeature83: "domainmodel_SetAction" = None):
        self.name = name
        self.domainmodel_ModelFeature = domainmodel_ModelFeature
        self.domainmodel_ModelFeature31 = domainmodel_ModelFeature31
        self.domainmodel_ModelFeature34 = domainmodel_ModelFeature34
        self.domainmodel_ModelFeature48 = domainmodel_ModelFeature48
        self.domainmodel_ModelFeature65 = domainmodel_ModelFeature65
        self.domainmodel_ModelFeature83 = domainmodel_ModelFeature83
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_ModelFeature31(self):
        return self.__domainmodel_ModelFeature31

    @domainmodel_ModelFeature31.setter
    def domainmodel_ModelFeature31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature31", None)
        self.__domainmodel_ModelFeature31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type32"):
                opp_val = getattr(old_value, "domainmodel_Type32", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type32"):
                opp_val = getattr(value, "domainmodel_Type32", None)
                setattr(value, "domainmodel_Type32", self)

    @property
    def domainmodel_ModelFeature65(self):
        return self.__domainmodel_ModelFeature65

    @domainmodel_ModelFeature65.setter
    def domainmodel_ModelFeature65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature65", None)
        self.__domainmodel_ModelFeature65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ScreenModelParameter"):
                opp_val = getattr(old_value, "domainmodel_ScreenModelParameter", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_ScreenModelParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ScreenModelParameter"):
                opp_val = getattr(value, "domainmodel_ScreenModelParameter", None)
                setattr(value, "domainmodel_ScreenModelParameter", self)

    @property
    def domainmodel_ModelFeature48(self):
        return self.__domainmodel_ModelFeature48

    @domainmodel_ModelFeature48.setter
    def domainmodel_ModelFeature48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature48", None)
        self.__domainmodel_ModelFeature48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_BindSource"):
                opp_val = getattr(old_value, "domainmodel_BindSource", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_BindSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_BindSource"):
                opp_val = getattr(value, "domainmodel_BindSource", None)
                setattr(value, "domainmodel_BindSource", self)

    @property
    def domainmodel_ModelFeature34(self):
        return self.__domainmodel_ModelFeature34

    @domainmodel_ModelFeature34.setter
    def domainmodel_ModelFeature34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature34", None)
        self.__domainmodel_ModelFeature34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_ModelModule"):
                opp_val = getattr(old_value, "domainmodel_ModelModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_ModelModule"):
                opp_val = getattr(value, "domainmodel_ModelModule", None)
                if opp_val is None:
                    setattr(value, "domainmodel_ModelModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_ModelFeature(self):
        return self.__domainmodel_ModelFeature

    @domainmodel_ModelFeature.setter
    def domainmodel_ModelFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature", None)
        self.__domainmodel_ModelFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_EntryParametersModule"):
                opp_val = getattr(old_value, "domainmodel_EntryParametersModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_EntryParametersModule"):
                opp_val = getattr(value, "domainmodel_EntryParametersModule", None)
                if opp_val is None:
                    setattr(value, "domainmodel_EntryParametersModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_ModelFeature83(self):
        return self.__domainmodel_ModelFeature83

    @domainmodel_ModelFeature83.setter
    def domainmodel_ModelFeature83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_ModelFeature__domainmodel_ModelFeature83", None)
        self.__domainmodel_ModelFeature83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_SetAction"):
                opp_val = getattr(old_value, "domainmodel_SetAction", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_SetAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_SetAction"):
                opp_val = getattr(value, "domainmodel_SetAction", None)
                setattr(value, "domainmodel_SetAction", self)

class ScreenModule:

    pass
class domainmodel_ControllerModule(ScreenModule):

    pass
class domainmodel_ViewModule(ScreenModule):

    pass
class domainmodel_ModelModule(ScreenModule):

    pass
class domainmodel_EntryParametersModule(ScreenModule):

    pass
class domainmodel_InterfaceOperationsUsageRule:

    pass
class domainmodel_InterfaceOperationUsageRule:

    def __init__(self, name: str, domainmodel_InterfaceOperationUsageRule: "domainmodel_InterfaceDeclaration" = None, domainmodel_InterfaceOperationUsageRule21: "domainmodel_InterfaceOperationsUsageRule" = None):
        self.name = name
        self.domainmodel_InterfaceOperationUsageRule = domainmodel_InterfaceOperationUsageRule
        self.domainmodel_InterfaceOperationUsageRule21 = domainmodel_InterfaceOperationUsageRule21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_InterfaceOperationUsageRule(self):
        return self.__domainmodel_InterfaceOperationUsageRule

    @domainmodel_InterfaceOperationUsageRule.setter
    def domainmodel_InterfaceOperationUsageRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceOperationUsageRule__domainmodel_InterfaceOperationUsageRule", None)
        self.__domainmodel_InterfaceOperationUsageRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceDeclaration19"):
                opp_val = getattr(old_value, "domainmodel_InterfaceDeclaration19", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceDeclaration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceDeclaration19"):
                opp_val = getattr(value, "domainmodel_InterfaceDeclaration19", None)
                setattr(value, "domainmodel_InterfaceDeclaration19", self)

    @property
    def domainmodel_InterfaceOperationUsageRule21(self):
        return self.__domainmodel_InterfaceOperationUsageRule21

    @domainmodel_InterfaceOperationUsageRule21.setter
    def domainmodel_InterfaceOperationUsageRule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceOperationUsageRule__domainmodel_InterfaceOperationUsageRule21", None)
        self.__domainmodel_InterfaceOperationUsageRule21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceOperationsUsageRule"):
                opp_val = getattr(old_value, "domainmodel_InterfaceOperationsUsageRule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceOperationsUsageRule"):
                opp_val = getattr(value, "domainmodel_InterfaceOperationsUsageRule", None)
                if opp_val is None:
                    setattr(value, "domainmodel_InterfaceOperationsUsageRule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BusinessFeatureType:

    pass
class domainmodel_InterfaceOperation:

    def __init__(self, restOperation: str, domainmodel_InterfaceOperation: "domainmodel_MethodCall" = None, domainmodel_InterfaceOperation14: "domainmodel_Type" = None, domainmodel_InterfaceOperation17: "domainmodel_InterfaceDeclaration" = None):
        self.restOperation = restOperation
        self.domainmodel_InterfaceOperation = domainmodel_InterfaceOperation
        self.domainmodel_InterfaceOperation14 = domainmodel_InterfaceOperation14
        self.domainmodel_InterfaceOperation17 = domainmodel_InterfaceOperation17
        
    @property
    def restOperation(self) -> str:
        return self.__restOperation

    @restOperation.setter
    def restOperation(self, restOperation: str):
        self.__restOperation = restOperation

    @property
    def domainmodel_InterfaceOperation(self):
        return self.__domainmodel_InterfaceOperation

    @domainmodel_InterfaceOperation.setter
    def domainmodel_InterfaceOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceOperation__domainmodel_InterfaceOperation", None)
        self.__domainmodel_InterfaceOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_MethodCall12"):
                opp_val = getattr(old_value, "domainmodel_MethodCall12", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_MethodCall12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_MethodCall12"):
                opp_val = getattr(value, "domainmodel_MethodCall12", None)
                setattr(value, "domainmodel_MethodCall12", self)

    @property
    def domainmodel_InterfaceOperation14(self):
        return self.__domainmodel_InterfaceOperation14

    @domainmodel_InterfaceOperation14.setter
    def domainmodel_InterfaceOperation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceOperation__domainmodel_InterfaceOperation14", None)
        self.__domainmodel_InterfaceOperation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type15"):
                opp_val = getattr(old_value, "domainmodel_Type15", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type15"):
                opp_val = getattr(value, "domainmodel_Type15", None)
                setattr(value, "domainmodel_Type15", self)

    @property
    def domainmodel_InterfaceOperation17(self):
        return self.__domainmodel_InterfaceOperation17

    @domainmodel_InterfaceOperation17.setter
    def domainmodel_InterfaceOperation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceOperation__domainmodel_InterfaceOperation17", None)
        self.__domainmodel_InterfaceOperation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceDeclaration"):
                opp_val = getattr(old_value, "domainmodel_InterfaceDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceDeclaration"):
                opp_val = getattr(value, "domainmodel_InterfaceDeclaration", None)
                if opp_val is None:
                    setattr(value, "domainmodel_InterfaceDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_MethodCall:

    def __init__(self, name: str, domainmodel_MethodCall12: "domainmodel_InterfaceOperation" = None, domainmodel_MethodCall: "domainmodel_MethodParameters" = None, domainmodel_MethodCall93: "domainmodel_InterfaceMethodCall" = None):
        self.name = name
        self.domainmodel_MethodCall12 = domainmodel_MethodCall12
        self.domainmodel_MethodCall = domainmodel_MethodCall
        self.domainmodel_MethodCall93 = domainmodel_MethodCall93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_MethodCall93(self):
        return self.__domainmodel_MethodCall93

    @domainmodel_MethodCall93.setter
    def domainmodel_MethodCall93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodCall__domainmodel_MethodCall93", None)
        self.__domainmodel_MethodCall93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceMethodCall92"):
                opp_val = getattr(old_value, "domainmodel_InterfaceMethodCall92", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceMethodCall92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceMethodCall92"):
                opp_val = getattr(value, "domainmodel_InterfaceMethodCall92", None)
                setattr(value, "domainmodel_InterfaceMethodCall92", self)

    @property
    def domainmodel_MethodCall(self):
        return self.__domainmodel_MethodCall

    @domainmodel_MethodCall.setter
    def domainmodel_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodCall__domainmodel_MethodCall", None)
        self.__domainmodel_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_MethodParameters10"):
                opp_val = getattr(old_value, "domainmodel_MethodParameters10", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_MethodParameters10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_MethodParameters10"):
                opp_val = getattr(value, "domainmodel_MethodParameters10", None)
                setattr(value, "domainmodel_MethodParameters10", self)

    @property
    def domainmodel_MethodCall12(self):
        return self.__domainmodel_MethodCall12

    @domainmodel_MethodCall12.setter
    def domainmodel_MethodCall12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodCall__domainmodel_MethodCall12", None)
        self.__domainmodel_MethodCall12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceOperation"):
                opp_val = getattr(old_value, "domainmodel_InterfaceOperation", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceOperation"):
                opp_val = getattr(value, "domainmodel_InterfaceOperation", None)
                setattr(value, "domainmodel_InterfaceOperation", self)

class domainmodel_MethodParameters:

    pass
class domainmodel_MethodParameter:

    def __init__(self, name: str, domainmodel_MethodParameter: "domainmodel_Type" = None, domainmodel_MethodParameter8: "domainmodel_MethodParameters" = None, domainmodel_MethodParameter87: "domainmodel_InterfaceMethodCallParameter" = None):
        self.name = name
        self.domainmodel_MethodParameter = domainmodel_MethodParameter
        self.domainmodel_MethodParameter8 = domainmodel_MethodParameter8
        self.domainmodel_MethodParameter87 = domainmodel_MethodParameter87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_MethodParameter(self):
        return self.__domainmodel_MethodParameter

    @domainmodel_MethodParameter.setter
    def domainmodel_MethodParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodParameter__domainmodel_MethodParameter", None)
        self.__domainmodel_MethodParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type6"):
                opp_val = getattr(old_value, "domainmodel_Type6", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type6"):
                opp_val = getattr(value, "domainmodel_Type6", None)
                setattr(value, "domainmodel_Type6", self)

    @property
    def domainmodel_MethodParameter87(self):
        return self.__domainmodel_MethodParameter87

    @domainmodel_MethodParameter87.setter
    def domainmodel_MethodParameter87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodParameter__domainmodel_MethodParameter87", None)
        self.__domainmodel_MethodParameter87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceMethodCallParameter"):
                opp_val = getattr(old_value, "domainmodel_InterfaceMethodCallParameter", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceMethodCallParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceMethodCallParameter"):
                opp_val = getattr(value, "domainmodel_InterfaceMethodCallParameter", None)
                setattr(value, "domainmodel_InterfaceMethodCallParameter", self)

    @property
    def domainmodel_MethodParameter8(self):
        return self.__domainmodel_MethodParameter8

    @domainmodel_MethodParameter8.setter
    def domainmodel_MethodParameter8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_MethodParameter__domainmodel_MethodParameter8", None)
        self.__domainmodel_MethodParameter8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_MethodParameters"):
                opp_val = getattr(old_value, "domainmodel_MethodParameters", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_MethodParameters"):
                opp_val = getattr(value, "domainmodel_MethodParameters", None)
                if opp_val is None:
                    setattr(value, "domainmodel_MethodParameters", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_Feature:

    def __init__(self, name: str, mappingOption: str, mapName: str, domainmodel_Feature: "domainmodel_Type" = None, domainmodel_Feature4: "domainmodel_DomainEntity" = None):
        self.name = name
        self.mappingOption = mappingOption
        self.mapName = mapName
        self.domainmodel_Feature = domainmodel_Feature
        self.domainmodel_Feature4 = domainmodel_Feature4
        
    @property
    def mapName(self) -> str:
        return self.__mapName

    @mapName.setter
    def mapName(self, mapName: str):
        self.__mapName = mapName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mappingOption(self) -> str:
        return self.__mappingOption

    @mappingOption.setter
    def mappingOption(self, mappingOption: str):
        self.__mappingOption = mappingOption

    @property
    def domainmodel_Feature(self):
        return self.__domainmodel_Feature

    @domainmodel_Feature.setter
    def domainmodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature", None)
        self.__domainmodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type"):
                opp_val = getattr(old_value, "domainmodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type"):
                opp_val = getattr(value, "domainmodel_Type", None)
                setattr(value, "domainmodel_Type", self)

    @property
    def domainmodel_Feature4(self):
        return self.__domainmodel_Feature4

    @domainmodel_Feature4.setter
    def domainmodel_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature4", None)
        self.__domainmodel_Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_DomainEntity"):
                opp_val = getattr(old_value, "domainmodel_DomainEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_DomainEntity"):
                opp_val = getattr(value, "domainmodel_DomainEntity", None)
                if opp_val is None:
                    setattr(value, "domainmodel_DomainEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_AbstractNamespaceElement:

    pass
class AbstractElement:

    pass
class domainmodel_SystemDefinition(AbstractElement):

    pass
class domainmodel_NamespaceDeclaration(AbstractElement):

    pass
class Type:

    pass
class AbstractNamespaceElement:

    pass
class domainmodel_DataType(AbstractNamespaceElement, Type):

    def __init__(self, name: str, mappedType: str, initValue: str):
        self.name = name
        self.mappedType = mappedType
        self.initValue = initValue
        
    @property
    def initValue(self) -> str:
        return self.__initValue

    @initValue.setter
    def initValue(self, initValue: str):
        self.__initValue = initValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mappedType(self) -> str:
        return self.__mappedType

    @mappedType.setter
    def mappedType(self, mappedType: str):
        self.__mappedType = mappedType

class domainmodel_DomainRepository(AbstractNamespaceElement, BusinessFeatureType):

    def __init__(self, name: str, domainmodel_DomainRepository: "domainmodel_DomainEntity" = None, domainmodel_DomainRepository27: "domainmodel_InterfaceOperationsUsageRule" = None):
        self.name = name
        self.domainmodel_DomainRepository = domainmodel_DomainRepository
        self.domainmodel_DomainRepository27 = domainmodel_DomainRepository27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_DomainRepository(self):
        return self.__domainmodel_DomainRepository

    @domainmodel_DomainRepository.setter
    def domainmodel_DomainRepository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_DomainRepository__domainmodel_DomainRepository", None)
        self.__domainmodel_DomainRepository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_DomainEntity25"):
                opp_val = getattr(old_value, "domainmodel_DomainEntity25", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_DomainEntity25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_DomainEntity25"):
                opp_val = getattr(value, "domainmodel_DomainEntity25", None)
                setattr(value, "domainmodel_DomainEntity25", self)

    @property
    def domainmodel_DomainRepository27(self):
        return self.__domainmodel_DomainRepository27

    @domainmodel_DomainRepository27.setter
    def domainmodel_DomainRepository27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_DomainRepository__domainmodel_DomainRepository27", None)
        self.__domainmodel_DomainRepository27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceOperationsUsageRule28"):
                opp_val = getattr(old_value, "domainmodel_InterfaceOperationsUsageRule28", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceOperationsUsageRule28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceOperationsUsageRule28"):
                opp_val = getattr(value, "domainmodel_InterfaceOperationsUsageRule28", None)
                setattr(value, "domainmodel_InterfaceOperationsUsageRule28", self)

class domainmodel_DomainEntity(AbstractNamespaceElement, Type):

    def __init__(self, name: str, domainmodel_DomainEntity: set["domainmodel_Feature"] = None, domainmodel_DomainEntity25: "domainmodel_DomainRepository" = None):
        self.name = name
        self.domainmodel_DomainEntity = domainmodel_DomainEntity if domainmodel_DomainEntity is not None else set()
        self.domainmodel_DomainEntity25 = domainmodel_DomainEntity25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_DomainEntity25(self):
        return self.__domainmodel_DomainEntity25

    @domainmodel_DomainEntity25.setter
    def domainmodel_DomainEntity25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_DomainEntity__domainmodel_DomainEntity25", None)
        self.__domainmodel_DomainEntity25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_DomainRepository"):
                opp_val = getattr(old_value, "domainmodel_DomainRepository", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_DomainRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_DomainRepository"):
                opp_val = getattr(value, "domainmodel_DomainRepository", None)
                setattr(value, "domainmodel_DomainRepository", self)

    @property
    def domainmodel_DomainEntity(self):
        return self.__domainmodel_DomainEntity

    @domainmodel_DomainEntity.setter
    def domainmodel_DomainEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_DomainEntity__domainmodel_DomainEntity", None)
        self.__domainmodel_DomainEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_Feature4"):
                    opp_val = getattr(item, "domainmodel_Feature4", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_Feature4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_Feature4"):
                    opp_val = getattr(item, "domainmodel_Feature4", None)
                    
                    setattr(item, "domainmodel_Feature4", self)
                    

class domainmodel_StatelessComponent(AbstractNamespaceElement, BusinessFeatureType):

    def __init__(self, name: str, domainmodel_StatelessComponent: "domainmodel_InterfaceOperationsUsageRule" = None):
        self.name = name
        self.domainmodel_StatelessComponent = domainmodel_StatelessComponent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_StatelessComponent(self):
        return self.__domainmodel_StatelessComponent

    @domainmodel_StatelessComponent.setter
    def domainmodel_StatelessComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_StatelessComponent__domainmodel_StatelessComponent", None)
        self.__domainmodel_StatelessComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceOperationsUsageRule23"):
                opp_val = getattr(old_value, "domainmodel_InterfaceOperationsUsageRule23", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceOperationsUsageRule23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceOperationsUsageRule23"):
                opp_val = getattr(value, "domainmodel_InterfaceOperationsUsageRule23", None)
                setattr(value, "domainmodel_InterfaceOperationsUsageRule23", self)

class domainmodel_InterfaceDeclaration(AbstractNamespaceElement, BusinessFeatureType):

    def __init__(self, name: str, domainmodel_InterfaceDeclaration: set["domainmodel_InterfaceOperation"] = None, domainmodel_InterfaceDeclaration19: "domainmodel_InterfaceOperationUsageRule" = None):
        self.name = name
        self.domainmodel_InterfaceDeclaration = domainmodel_InterfaceDeclaration if domainmodel_InterfaceDeclaration is not None else set()
        self.domainmodel_InterfaceDeclaration19 = domainmodel_InterfaceDeclaration19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_InterfaceDeclaration19(self):
        return self.__domainmodel_InterfaceDeclaration19

    @domainmodel_InterfaceDeclaration19.setter
    def domainmodel_InterfaceDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceDeclaration__domainmodel_InterfaceDeclaration19", None)
        self.__domainmodel_InterfaceDeclaration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_InterfaceOperationUsageRule"):
                opp_val = getattr(old_value, "domainmodel_InterfaceOperationUsageRule", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_InterfaceOperationUsageRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_InterfaceOperationUsageRule"):
                opp_val = getattr(value, "domainmodel_InterfaceOperationUsageRule", None)
                setattr(value, "domainmodel_InterfaceOperationUsageRule", self)

    @property
    def domainmodel_InterfaceDeclaration(self):
        return self.__domainmodel_InterfaceDeclaration

    @domainmodel_InterfaceDeclaration.setter
    def domainmodel_InterfaceDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_InterfaceDeclaration__domainmodel_InterfaceDeclaration", None)
        self.__domainmodel_InterfaceDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_InterfaceOperation17"):
                    opp_val = getattr(item, "domainmodel_InterfaceOperation17", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_InterfaceOperation17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_InterfaceOperation17"):
                    opp_val = getattr(item, "domainmodel_InterfaceOperation17", None)
                    
                    setattr(item, "domainmodel_InterfaceOperation17", self)
                    

class domainmodel_Import(AbstractNamespaceElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainmodel_Type:

    pass
class domainmodel_AbstractElement:

    def __init__(self, name: str, domainmodel_AbstractElement: "domainmodel_Domainmodel" = None):
        self.name = name
        self.domainmodel_AbstractElement = domainmodel_AbstractElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_AbstractElement(self):
        return self.__domainmodel_AbstractElement

    @domainmodel_AbstractElement.setter
    def domainmodel_AbstractElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_AbstractElement__domainmodel_AbstractElement", None)
        self.__domainmodel_AbstractElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Domainmodel"):
                opp_val = getattr(old_value, "domainmodel_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Domainmodel"):
                opp_val = getattr(value, "domainmodel_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_Domainmodel:

    pass
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GestureKind(Enum):
    tap = "tap"
    swipe = "swipe"
    longpress = "longpress"
class RESTVerb(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
class ActionVerb(Enum):
    edit = "edit"
    display = "display"
    add = "add"
class UIActionKind(Enum):
    navigate = "navigate"
    delete = "delete"
    performaction = "performaction"
class ScreenKind(Enum):
    DefaultList = "DefaultList"
    DefaultDetails = "DefaultDetails"


############################################
# Definition of Classes
############################################

class applauseDsl_AttributeReference:

    pass
class applauseDsl_EntityMemberCallTail:

    pass
class Expression:

    pass
class applauseDsl_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class applauseDsl_EntityMemberCall(Expression):

    pass
class applauseDsl_Expression:

    pass
class applauseDsl_UIComponentMemberCall:

    pass
class applauseDsl_UIComponentMemberDeclaration:

    def __init__(self, name: str, applauseDsl_UIComponentMemberDeclaration73: "applauseDsl_UIComponentOrDataType" = None, applauseDsl_UIComponentMemberDeclaration: "applauseDsl_ListItemCellDeclaration" = None, applauseDsl_UIComponentMemberDeclaration71: "applauseDsl_UIComponentDeclaration" = None, applauseDsl_UIComponentMemberDeclaration89: "applauseDsl_UIComponentMemberCall" = None, applauseDsl_UIComponentMemberDeclaration92: "applauseDsl_UIComponentMemberCall" = None):
        self.name = name
        self.applauseDsl_UIComponentMemberDeclaration73 = applauseDsl_UIComponentMemberDeclaration73
        self.applauseDsl_UIComponentMemberDeclaration = applauseDsl_UIComponentMemberDeclaration
        self.applauseDsl_UIComponentMemberDeclaration71 = applauseDsl_UIComponentMemberDeclaration71
        self.applauseDsl_UIComponentMemberDeclaration89 = applauseDsl_UIComponentMemberDeclaration89
        self.applauseDsl_UIComponentMemberDeclaration92 = applauseDsl_UIComponentMemberDeclaration92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_UIComponentMemberDeclaration73(self):
        return self.__applauseDsl_UIComponentMemberDeclaration73

    @applauseDsl_UIComponentMemberDeclaration73.setter
    def applauseDsl_UIComponentMemberDeclaration73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration73", None)
        self.__applauseDsl_UIComponentMemberDeclaration73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIComponentOrDataType"):
                opp_val = getattr(old_value, "applauseDsl_UIComponentOrDataType", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIComponentOrDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIComponentOrDataType"):
                opp_val = getattr(value, "applauseDsl_UIComponentOrDataType", None)
                setattr(value, "applauseDsl_UIComponentOrDataType", self)

    @property
    def applauseDsl_UIComponentMemberDeclaration71(self):
        return self.__applauseDsl_UIComponentMemberDeclaration71

    @applauseDsl_UIComponentMemberDeclaration71.setter
    def applauseDsl_UIComponentMemberDeclaration71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration71", None)
        self.__applauseDsl_UIComponentMemberDeclaration71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIComponentDeclaration"):
                opp_val = getattr(old_value, "applauseDsl_UIComponentDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIComponentDeclaration"):
                opp_val = getattr(value, "applauseDsl_UIComponentDeclaration", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_UIComponentDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_UIComponentMemberDeclaration(self):
        return self.__applauseDsl_UIComponentMemberDeclaration

    @applauseDsl_UIComponentMemberDeclaration.setter
    def applauseDsl_UIComponentMemberDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration", None)
        self.__applauseDsl_UIComponentMemberDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ListItemCellDeclaration69"):
                opp_val = getattr(old_value, "applauseDsl_ListItemCellDeclaration69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ListItemCellDeclaration69"):
                opp_val = getattr(value, "applauseDsl_ListItemCellDeclaration69", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_ListItemCellDeclaration69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_UIComponentMemberDeclaration92(self):
        return self.__applauseDsl_UIComponentMemberDeclaration92

    @applauseDsl_UIComponentMemberDeclaration92.setter
    def applauseDsl_UIComponentMemberDeclaration92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration92", None)
        self.__applauseDsl_UIComponentMemberDeclaration92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIComponentMemberCall91"):
                opp_val = getattr(old_value, "applauseDsl_UIComponentMemberCall91", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIComponentMemberCall91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIComponentMemberCall91"):
                opp_val = getattr(value, "applauseDsl_UIComponentMemberCall91", None)
                setattr(value, "applauseDsl_UIComponentMemberCall91", self)

    @property
    def applauseDsl_UIComponentMemberDeclaration89(self):
        return self.__applauseDsl_UIComponentMemberDeclaration89

    @applauseDsl_UIComponentMemberDeclaration89.setter
    def applauseDsl_UIComponentMemberDeclaration89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIComponentMemberDeclaration__applauseDsl_UIComponentMemberDeclaration89", None)
        self.__applauseDsl_UIComponentMemberDeclaration89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIComponentMemberCall88"):
                opp_val = getattr(old_value, "applauseDsl_UIComponentMemberCall88", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIComponentMemberCall88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIComponentMemberCall88"):
                opp_val = getattr(value, "applauseDsl_UIComponentMemberCall88", None)
                setattr(value, "applauseDsl_UIComponentMemberCall88", self)

class UIActionSpecification:

    pass
class applauseDsl_UIActionDeleteAction(UIActionSpecification):

    pass
class applauseDsl_UIActionNavigateAction(UIActionSpecification):

    def __init__(self, actionVerb: str, applauseDsl_UIActionNavigateAction: "applauseDsl_Screen" = None, applauseDsl_UIActionNavigateAction67: "applauseDsl_ReferrableElement" = None):
        self.actionVerb = actionVerb
        self.applauseDsl_UIActionNavigateAction = applauseDsl_UIActionNavigateAction
        self.applauseDsl_UIActionNavigateAction67 = applauseDsl_UIActionNavigateAction67
        
    @property
    def actionVerb(self) -> str:
        return self.__actionVerb

    @actionVerb.setter
    def actionVerb(self, actionVerb: str):
        self.__actionVerb = actionVerb

    @property
    def applauseDsl_UIActionNavigateAction(self):
        return self.__applauseDsl_UIActionNavigateAction

    @applauseDsl_UIActionNavigateAction.setter
    def applauseDsl_UIActionNavigateAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIActionNavigateAction__applauseDsl_UIActionNavigateAction", None)
        self.__applauseDsl_UIActionNavigateAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Screen65"):
                opp_val = getattr(old_value, "applauseDsl_Screen65", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Screen65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Screen65"):
                opp_val = getattr(value, "applauseDsl_Screen65", None)
                setattr(value, "applauseDsl_Screen65", self)

    @property
    def applauseDsl_UIActionNavigateAction67(self):
        return self.__applauseDsl_UIActionNavigateAction67

    @applauseDsl_UIActionNavigateAction67.setter
    def applauseDsl_UIActionNavigateAction67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIActionNavigateAction__applauseDsl_UIActionNavigateAction67", None)
        self.__applauseDsl_UIActionNavigateAction67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ReferrableElement"):
                opp_val = getattr(old_value, "applauseDsl_ReferrableElement", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ReferrableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ReferrableElement"):
                opp_val = getattr(value, "applauseDsl_ReferrableElement", None)
                setattr(value, "applauseDsl_ReferrableElement", self)

class applauseDsl_UIActionSpecification:

    pass
class applauseDsl_ReferrableElement:

    def __init__(self, name: str, applauseDsl_ReferrableElement: "applauseDsl_UIActionNavigateAction" = None):
        self.name = name
        self.applauseDsl_ReferrableElement = applauseDsl_ReferrableElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_ReferrableElement(self):
        return self.__applauseDsl_ReferrableElement

    @applauseDsl_ReferrableElement.setter
    def applauseDsl_ReferrableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ReferrableElement__applauseDsl_ReferrableElement", None)
        self.__applauseDsl_ReferrableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIActionNavigateAction67"):
                opp_val = getattr(old_value, "applauseDsl_UIActionNavigateAction67", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIActionNavigateAction67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIActionNavigateAction67"):
                opp_val = getattr(value, "applauseDsl_UIActionNavigateAction67", None)
                setattr(value, "applauseDsl_UIActionNavigateAction67", self)

class applauseDsl_UIComponentMemberConfiguration:

    pass
class applauseDsl_UIComponentOrDataType:

    pass
class applauseDsl_RESTMethodCall:

    pass
class applauseDsl_ScreenListItemCell:

    pass
class applauseDsl_ScreenSectionItems:

    pass
class applauseDsl_UIAction:

    def __init__(self, title: str, icon: str, gesture: str, order: int, applauseDsl_UIAction: "applauseDsl_Screen" = None, applauseDsl_UIAction61: "applauseDsl_ScreenListItemCell" = None, applauseDsl_UIAction63: "applauseDsl_UIActionSpecification" = None):
        self.title = title
        self.icon = icon
        self.gesture = gesture
        self.order = order
        self.applauseDsl_UIAction = applauseDsl_UIAction
        self.applauseDsl_UIAction61 = applauseDsl_UIAction61
        self.applauseDsl_UIAction63 = applauseDsl_UIAction63
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def gesture(self) -> str:
        return self.__gesture

    @gesture.setter
    def gesture(self, gesture: str):
        self.__gesture = gesture

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def applauseDsl_UIAction61(self):
        return self.__applauseDsl_UIAction61

    @applauseDsl_UIAction61.setter
    def applauseDsl_UIAction61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIAction__applauseDsl_UIAction61", None)
        self.__applauseDsl_UIAction61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScreenListItemCell60"):
                opp_val = getattr(old_value, "applauseDsl_ScreenListItemCell60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScreenListItemCell60"):
                opp_val = getattr(value, "applauseDsl_ScreenListItemCell60", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_ScreenListItemCell60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_UIAction(self):
        return self.__applauseDsl_UIAction

    @applauseDsl_UIAction.setter
    def applauseDsl_UIAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIAction__applauseDsl_UIAction", None)
        self.__applauseDsl_UIAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Screen43"):
                opp_val = getattr(old_value, "applauseDsl_Screen43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Screen43"):
                opp_val = getattr(value, "applauseDsl_Screen43", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Screen43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_UIAction63(self):
        return self.__applauseDsl_UIAction63

    @applauseDsl_UIAction63.setter
    def applauseDsl_UIAction63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_UIAction__applauseDsl_UIAction63", None)
        self.__applauseDsl_UIAction63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIActionSpecification"):
                opp_val = getattr(old_value, "applauseDsl_UIActionSpecification", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIActionSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIActionSpecification"):
                opp_val = getattr(value, "applauseDsl_UIActionSpecification", None)
                setattr(value, "applauseDsl_UIActionSpecification", self)

class applauseDsl_ScreenSection:

    def __init__(self, title: str, applauseDsl_ScreenSection: "applauseDsl_Screen" = None, applauseDsl_ScreenSection45: "applauseDsl_DataSourceCall" = None, applauseDsl_ScreenSection48: "applauseDsl_ScreenSectionItems" = None):
        self.title = title
        self.applauseDsl_ScreenSection = applauseDsl_ScreenSection
        self.applauseDsl_ScreenSection45 = applauseDsl_ScreenSection45
        self.applauseDsl_ScreenSection48 = applauseDsl_ScreenSection48
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def applauseDsl_ScreenSection45(self):
        return self.__applauseDsl_ScreenSection45

    @applauseDsl_ScreenSection45.setter
    def applauseDsl_ScreenSection45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ScreenSection__applauseDsl_ScreenSection45", None)
        self.__applauseDsl_ScreenSection45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSourceCall46"):
                opp_val = getattr(old_value, "applauseDsl_DataSourceCall46", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSourceCall46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSourceCall46"):
                opp_val = getattr(value, "applauseDsl_DataSourceCall46", None)
                setattr(value, "applauseDsl_DataSourceCall46", self)

    @property
    def applauseDsl_ScreenSection(self):
        return self.__applauseDsl_ScreenSection

    @applauseDsl_ScreenSection.setter
    def applauseDsl_ScreenSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ScreenSection__applauseDsl_ScreenSection", None)
        self.__applauseDsl_ScreenSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Screen41"):
                opp_val = getattr(old_value, "applauseDsl_Screen41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Screen41"):
                opp_val = getattr(value, "applauseDsl_Screen41", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Screen41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_ScreenSection48(self):
        return self.__applauseDsl_ScreenSection48

    @applauseDsl_ScreenSection48.setter
    def applauseDsl_ScreenSection48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ScreenSection__applauseDsl_ScreenSection48", None)
        self.__applauseDsl_ScreenSection48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScreenSectionItems"):
                opp_val = getattr(old_value, "applauseDsl_ScreenSectionItems", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScreenSectionItems", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScreenSectionItems"):
                opp_val = getattr(value, "applauseDsl_ScreenSectionItems", None)
                setattr(value, "applauseDsl_ScreenSectionItems", self)

class applauseDsl_DataSourceCall:

    def __init__(self, name: str, applauseDsl_DataSourceCall: "applauseDsl_Screen" = None, applauseDsl_DataSourceCall46: "applauseDsl_ScreenSection" = None, applauseDsl_DataSourceCall76: "applauseDsl_RESTMethodCall" = None, applauseDsl_DataSourceCall81: "applauseDsl_DataSource" = None):
        self.name = name
        self.applauseDsl_DataSourceCall = applauseDsl_DataSourceCall
        self.applauseDsl_DataSourceCall46 = applauseDsl_DataSourceCall46
        self.applauseDsl_DataSourceCall76 = applauseDsl_DataSourceCall76
        self.applauseDsl_DataSourceCall81 = applauseDsl_DataSourceCall81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_DataSourceCall(self):
        return self.__applauseDsl_DataSourceCall

    @applauseDsl_DataSourceCall.setter
    def applauseDsl_DataSourceCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceCall__applauseDsl_DataSourceCall", None)
        self.__applauseDsl_DataSourceCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Screen39"):
                opp_val = getattr(old_value, "applauseDsl_Screen39", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Screen39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Screen39"):
                opp_val = getattr(value, "applauseDsl_Screen39", None)
                setattr(value, "applauseDsl_Screen39", self)

    @property
    def applauseDsl_DataSourceCall81(self):
        return self.__applauseDsl_DataSourceCall81

    @applauseDsl_DataSourceCall81.setter
    def applauseDsl_DataSourceCall81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceCall__applauseDsl_DataSourceCall81", None)
        self.__applauseDsl_DataSourceCall81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSource82"):
                opp_val = getattr(old_value, "applauseDsl_DataSource82", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSource82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSource82"):
                opp_val = getattr(value, "applauseDsl_DataSource82", None)
                setattr(value, "applauseDsl_DataSource82", self)

    @property
    def applauseDsl_DataSourceCall76(self):
        return self.__applauseDsl_DataSourceCall76

    @applauseDsl_DataSourceCall76.setter
    def applauseDsl_DataSourceCall76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceCall__applauseDsl_DataSourceCall76", None)
        self.__applauseDsl_DataSourceCall76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_RESTMethodCall75"):
                opp_val = getattr(old_value, "applauseDsl_RESTMethodCall75", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_RESTMethodCall75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_RESTMethodCall75"):
                opp_val = getattr(value, "applauseDsl_RESTMethodCall75", None)
                setattr(value, "applauseDsl_RESTMethodCall75", self)

    @property
    def applauseDsl_DataSourceCall46(self):
        return self.__applauseDsl_DataSourceCall46

    @applauseDsl_DataSourceCall46.setter
    def applauseDsl_DataSourceCall46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceCall__applauseDsl_DataSourceCall46", None)
        self.__applauseDsl_DataSourceCall46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScreenSection45"):
                opp_val = getattr(old_value, "applauseDsl_ScreenSection45", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScreenSection45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScreenSection45"):
                opp_val = getattr(value, "applauseDsl_ScreenSection45", None)
                setattr(value, "applauseDsl_ScreenSection45", self)

class UrlFragment:

    pass
class applauseDsl_Variable(UrlFragment):

    pass
class applauseDsl_UrlPathFragment(UrlFragment):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RESTURL:

    pass
class applauseDsl_RelativeRESTURL(RESTURL):

    pass
class ReferrableElement:

    pass
class applauseDsl_LoopVariable(ReferrableElement):

    pass
class applauseDsl_DataSourceBodySpecification:

    pass
class applauseDsl_RESTURL:

    pass
class applauseDsl_RESTSpecification:

    def __init__(self, verb: str, applauseDsl_RESTSpecification: "applauseDsl_DataSourceAccessMethod" = None, applauseDsl_RESTSpecification20: "applauseDsl_RESTURL" = None, applauseDsl_RESTSpecification22: "applauseDsl_DataSourceBodySpecification" = None):
        self.verb = verb
        self.applauseDsl_RESTSpecification = applauseDsl_RESTSpecification
        self.applauseDsl_RESTSpecification20 = applauseDsl_RESTSpecification20
        self.applauseDsl_RESTSpecification22 = applauseDsl_RESTSpecification22
        
    @property
    def verb(self) -> str:
        return self.__verb

    @verb.setter
    def verb(self, verb: str):
        self.__verb = verb

    @property
    def applauseDsl_RESTSpecification22(self):
        return self.__applauseDsl_RESTSpecification22

    @applauseDsl_RESTSpecification22.setter
    def applauseDsl_RESTSpecification22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_RESTSpecification__applauseDsl_RESTSpecification22", None)
        self.__applauseDsl_RESTSpecification22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSourceBodySpecification"):
                opp_val = getattr(old_value, "applauseDsl_DataSourceBodySpecification", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSourceBodySpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSourceBodySpecification"):
                opp_val = getattr(value, "applauseDsl_DataSourceBodySpecification", None)
                setattr(value, "applauseDsl_DataSourceBodySpecification", self)

    @property
    def applauseDsl_RESTSpecification(self):
        return self.__applauseDsl_RESTSpecification

    @applauseDsl_RESTSpecification.setter
    def applauseDsl_RESTSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_RESTSpecification__applauseDsl_RESTSpecification", None)
        self.__applauseDsl_RESTSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSourceAccessMethod18"):
                opp_val = getattr(old_value, "applauseDsl_DataSourceAccessMethod18", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSourceAccessMethod18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSourceAccessMethod18"):
                opp_val = getattr(value, "applauseDsl_DataSourceAccessMethod18", None)
                setattr(value, "applauseDsl_DataSourceAccessMethod18", self)

    @property
    def applauseDsl_RESTSpecification20(self):
        return self.__applauseDsl_RESTSpecification20

    @applauseDsl_RESTSpecification20.setter
    def applauseDsl_RESTSpecification20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_RESTSpecification__applauseDsl_RESTSpecification20", None)
        self.__applauseDsl_RESTSpecification20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_RESTURL"):
                opp_val = getattr(old_value, "applauseDsl_RESTURL", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_RESTURL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_RESTURL"):
                opp_val = getattr(value, "applauseDsl_RESTURL", None)
                setattr(value, "applauseDsl_RESTURL", self)

class applauseDsl_Parameter(ReferrableElement):

    pass
class applauseDsl_DataSourceAccessMethod:

    def __init__(self, name: str, returnsMany: bool, applauseDsl_DataSourceAccessMethod: "applauseDsl_DataSource" = None, applauseDsl_DataSourceAccessMethod16: set["applauseDsl_Parameter"] = None, applauseDsl_DataSourceAccessMethod18: "applauseDsl_RESTSpecification" = None, applauseDsl_DataSourceAccessMethod79: "applauseDsl_RESTMethodCall" = None):
        self.name = name
        self.returnsMany = returnsMany
        self.applauseDsl_DataSourceAccessMethod = applauseDsl_DataSourceAccessMethod
        self.applauseDsl_DataSourceAccessMethod16 = applauseDsl_DataSourceAccessMethod16 if applauseDsl_DataSourceAccessMethod16 is not None else set()
        self.applauseDsl_DataSourceAccessMethod18 = applauseDsl_DataSourceAccessMethod18
        self.applauseDsl_DataSourceAccessMethod79 = applauseDsl_DataSourceAccessMethod79
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnsMany(self) -> bool:
        return self.__returnsMany

    @returnsMany.setter
    def returnsMany(self, returnsMany: bool):
        self.__returnsMany = returnsMany

    @property
    def applauseDsl_DataSourceAccessMethod(self):
        return self.__applauseDsl_DataSourceAccessMethod

    @applauseDsl_DataSourceAccessMethod.setter
    def applauseDsl_DataSourceAccessMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod", None)
        self.__applauseDsl_DataSourceAccessMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSource14"):
                opp_val = getattr(old_value, "applauseDsl_DataSource14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSource14"):
                opp_val = getattr(value, "applauseDsl_DataSource14", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_DataSource14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_DataSourceAccessMethod79(self):
        return self.__applauseDsl_DataSourceAccessMethod79

    @applauseDsl_DataSourceAccessMethod79.setter
    def applauseDsl_DataSourceAccessMethod79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod79", None)
        self.__applauseDsl_DataSourceAccessMethod79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_RESTMethodCall78"):
                opp_val = getattr(old_value, "applauseDsl_RESTMethodCall78", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_RESTMethodCall78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_RESTMethodCall78"):
                opp_val = getattr(value, "applauseDsl_RESTMethodCall78", None)
                setattr(value, "applauseDsl_RESTMethodCall78", self)

    @property
    def applauseDsl_DataSourceAccessMethod16(self):
        return self.__applauseDsl_DataSourceAccessMethod16

    @applauseDsl_DataSourceAccessMethod16.setter
    def applauseDsl_DataSourceAccessMethod16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod16", None)
        self.__applauseDsl_DataSourceAccessMethod16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Parameter"):
                    opp_val = getattr(item, "applauseDsl_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Parameter"):
                    opp_val = getattr(item, "applauseDsl_Parameter", None)
                    
                    setattr(item, "applauseDsl_Parameter", self)
                    

    @property
    def applauseDsl_DataSourceAccessMethod18(self):
        return self.__applauseDsl_DataSourceAccessMethod18

    @applauseDsl_DataSourceAccessMethod18.setter
    def applauseDsl_DataSourceAccessMethod18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_DataSourceAccessMethod__applauseDsl_DataSourceAccessMethod18", None)
        self.__applauseDsl_DataSourceAccessMethod18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_RESTSpecification"):
                opp_val = getattr(old_value, "applauseDsl_RESTSpecification", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_RESTSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_RESTSpecification"):
                opp_val = getattr(value, "applauseDsl_RESTSpecification", None)
                setattr(value, "applauseDsl_RESTSpecification", self)

class applauseDsl_AbsoluteRESTURL(RESTURL):

    def __init__(self, port: int, applauseDsl_AbsoluteRESTURL: "applauseDsl_DataSource" = None, applauseDsl_AbsoluteRESTURL32: "applauseDsl_UrlFragment" = None):
        self.port = port
        self.applauseDsl_AbsoluteRESTURL = applauseDsl_AbsoluteRESTURL
        self.applauseDsl_AbsoluteRESTURL32 = applauseDsl_AbsoluteRESTURL32
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def applauseDsl_AbsoluteRESTURL(self):
        return self.__applauseDsl_AbsoluteRESTURL

    @applauseDsl_AbsoluteRESTURL.setter
    def applauseDsl_AbsoluteRESTURL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_AbsoluteRESTURL__applauseDsl_AbsoluteRESTURL", None)
        self.__applauseDsl_AbsoluteRESTURL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSource"):
                opp_val = getattr(old_value, "applauseDsl_DataSource", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSource"):
                opp_val = getattr(value, "applauseDsl_DataSource", None)
                setattr(value, "applauseDsl_DataSource", self)

    @property
    def applauseDsl_AbsoluteRESTURL32(self):
        return self.__applauseDsl_AbsoluteRESTURL32

    @applauseDsl_AbsoluteRESTURL32.setter
    def applauseDsl_AbsoluteRESTURL32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_AbsoluteRESTURL__applauseDsl_AbsoluteRESTURL32", None)
        self.__applauseDsl_AbsoluteRESTURL32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UrlFragment33"):
                opp_val = getattr(old_value, "applauseDsl_UrlFragment33", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UrlFragment33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UrlFragment33"):
                opp_val = getattr(value, "applauseDsl_UrlFragment33", None)
                setattr(value, "applauseDsl_UrlFragment33", self)

class PlatformMapping:

    pass
class applauseDsl_TypeMapping(PlatformMapping):

    def __init__(self, simpleName: str, applauseDsl_TypeMapping: "applauseDsl_DataType" = None):
        self.simpleName = simpleName
        self.applauseDsl_TypeMapping = applauseDsl_TypeMapping
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def applauseDsl_TypeMapping(self):
        return self.__applauseDsl_TypeMapping

    @applauseDsl_TypeMapping.setter
    def applauseDsl_TypeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeMapping__applauseDsl_TypeMapping", None)
        self.__applauseDsl_TypeMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataType"):
                opp_val = getattr(old_value, "applauseDsl_DataType", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataType"):
                opp_val = getattr(value, "applauseDsl_DataType", None)
                setattr(value, "applauseDsl_DataType", self)

class applauseDsl_PlatformMapping:

    pass
class applauseDsl_UrlFragment:

    pass
class applauseDsl_Attribute:

    def __init__(self, many: bool, name: str, applauseDsl_Attribute: "applauseDsl_Entity" = None, applauseDsl_Attribute6: "applauseDsl_Type" = None, applauseDsl_Attribute94: "applauseDsl_EntityMemberCall" = None, applauseDsl_Attribute99: "applauseDsl_EntityMemberCallTail" = None, applauseDsl_Attribute104: "applauseDsl_AttributeReference" = None):
        self.many = many
        self.name = name
        self.applauseDsl_Attribute = applauseDsl_Attribute
        self.applauseDsl_Attribute6 = applauseDsl_Attribute6
        self.applauseDsl_Attribute94 = applauseDsl_Attribute94
        self.applauseDsl_Attribute99 = applauseDsl_Attribute99
        self.applauseDsl_Attribute104 = applauseDsl_Attribute104
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_Attribute99(self):
        return self.__applauseDsl_Attribute99

    @applauseDsl_Attribute99.setter
    def applauseDsl_Attribute99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Attribute__applauseDsl_Attribute99", None)
        self.__applauseDsl_Attribute99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_EntityMemberCallTail98"):
                opp_val = getattr(old_value, "applauseDsl_EntityMemberCallTail98", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_EntityMemberCallTail98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_EntityMemberCallTail98"):
                opp_val = getattr(value, "applauseDsl_EntityMemberCallTail98", None)
                setattr(value, "applauseDsl_EntityMemberCallTail98", self)

    @property
    def applauseDsl_Attribute6(self):
        return self.__applauseDsl_Attribute6

    @applauseDsl_Attribute6.setter
    def applauseDsl_Attribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Attribute__applauseDsl_Attribute6", None)
        self.__applauseDsl_Attribute6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Type"):
                opp_val = getattr(old_value, "applauseDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Type"):
                opp_val = getattr(value, "applauseDsl_Type", None)
                setattr(value, "applauseDsl_Type", self)

    @property
    def applauseDsl_Attribute(self):
        return self.__applauseDsl_Attribute

    @applauseDsl_Attribute.setter
    def applauseDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Attribute__applauseDsl_Attribute", None)
        self.__applauseDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Entity4"):
                opp_val = getattr(old_value, "applauseDsl_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity4"):
                opp_val = getattr(value, "applauseDsl_Entity4", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_Attribute104(self):
        return self.__applauseDsl_Attribute104

    @applauseDsl_Attribute104.setter
    def applauseDsl_Attribute104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Attribute__applauseDsl_Attribute104", None)
        self.__applauseDsl_Attribute104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_AttributeReference"):
                opp_val = getattr(old_value, "applauseDsl_AttributeReference", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_AttributeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_AttributeReference"):
                opp_val = getattr(value, "applauseDsl_AttributeReference", None)
                setattr(value, "applauseDsl_AttributeReference", self)

    @property
    def applauseDsl_Attribute94(self):
        return self.__applauseDsl_Attribute94

    @applauseDsl_Attribute94.setter
    def applauseDsl_Attribute94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Attribute__applauseDsl_Attribute94", None)
        self.__applauseDsl_Attribute94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_EntityMemberCall"):
                opp_val = getattr(old_value, "applauseDsl_EntityMemberCall", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_EntityMemberCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_EntityMemberCall"):
                opp_val = getattr(value, "applauseDsl_EntityMemberCall", None)
                setattr(value, "applauseDsl_EntityMemberCall", self)

class UIComponentOrDataType:

    pass
class Type:

    pass
class applauseDsl_Entity(Type):

    def __init__(self, abstract: bool, applauseDsl_Entity: "applauseDsl_Entity" = None, applauseDsl_Entity1: "applauseDsl_Entity" = None, applauseDsl_Entity4: set["applauseDsl_Attribute"] = None, applauseDsl_Entity12: "applauseDsl_DataSource" = None):
        self.abstract = abstract
        self.applauseDsl_Entity = applauseDsl_Entity
        self.applauseDsl_Entity1 = applauseDsl_Entity1
        self.applauseDsl_Entity4 = applauseDsl_Entity4 if applauseDsl_Entity4 is not None else set()
        self.applauseDsl_Entity12 = applauseDsl_Entity12
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def applauseDsl_Entity1(self):
        return self.__applauseDsl_Entity1

    @applauseDsl_Entity1.setter
    def applauseDsl_Entity1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity1", None)
        self.__applauseDsl_Entity1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Entity"):
                opp_val = getattr(old_value, "applauseDsl_Entity", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity"):
                opp_val = getattr(value, "applauseDsl_Entity", None)
                setattr(value, "applauseDsl_Entity", self)

    @property
    def applauseDsl_Entity12(self):
        return self.__applauseDsl_Entity12

    @applauseDsl_Entity12.setter
    def applauseDsl_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity12", None)
        self.__applauseDsl_Entity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSource11"):
                opp_val = getattr(old_value, "applauseDsl_DataSource11", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSource11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSource11"):
                opp_val = getattr(value, "applauseDsl_DataSource11", None)
                setattr(value, "applauseDsl_DataSource11", self)

    @property
    def applauseDsl_Entity(self):
        return self.__applauseDsl_Entity

    @applauseDsl_Entity.setter
    def applauseDsl_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity", None)
        self.__applauseDsl_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Entity1"):
                opp_val = getattr(old_value, "applauseDsl_Entity1", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Entity1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity1"):
                opp_val = getattr(value, "applauseDsl_Entity1", None)
                setattr(value, "applauseDsl_Entity1", self)

    @property
    def applauseDsl_Entity4(self):
        return self.__applauseDsl_Entity4

    @applauseDsl_Entity4.setter
    def applauseDsl_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity4", None)
        self.__applauseDsl_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Attribute"):
                    opp_val = getattr(item, "applauseDsl_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Attribute"):
                    opp_val = getattr(item, "applauseDsl_Attribute", None)
                    
                    setattr(item, "applauseDsl_Attribute", self)
                    

class applauseDsl_DataType(UIComponentOrDataType, Type):

    pass
class NamedElement:

    pass
class applauseDsl_DataSource(NamedElement):

    pass
class applauseDsl_Platform(NamedElement):

    pass
class applauseDsl_Screen(NamedElement):

    def __init__(self, kind: str, title: str, applauseDsl_Screen: "applauseDsl_Parameter" = None, applauseDsl_Screen39: "applauseDsl_DataSourceCall" = None, applauseDsl_Screen41: set["applauseDsl_ScreenSection"] = None, applauseDsl_Screen43: set["applauseDsl_UIAction"] = None, applauseDsl_Screen65: "applauseDsl_UIActionNavigateAction" = None):
        self.kind = kind
        self.title = title
        self.applauseDsl_Screen = applauseDsl_Screen
        self.applauseDsl_Screen39 = applauseDsl_Screen39
        self.applauseDsl_Screen41 = applauseDsl_Screen41 if applauseDsl_Screen41 is not None else set()
        self.applauseDsl_Screen43 = applauseDsl_Screen43 if applauseDsl_Screen43 is not None else set()
        self.applauseDsl_Screen65 = applauseDsl_Screen65
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def applauseDsl_Screen43(self):
        return self.__applauseDsl_Screen43

    @applauseDsl_Screen43.setter
    def applauseDsl_Screen43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Screen__applauseDsl_Screen43", None)
        self.__applauseDsl_Screen43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_UIAction"):
                    opp_val = getattr(item, "applauseDsl_UIAction", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_UIAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_UIAction"):
                    opp_val = getattr(item, "applauseDsl_UIAction", None)
                    
                    setattr(item, "applauseDsl_UIAction", self)
                    

    @property
    def applauseDsl_Screen65(self):
        return self.__applauseDsl_Screen65

    @applauseDsl_Screen65.setter
    def applauseDsl_Screen65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Screen__applauseDsl_Screen65", None)
        self.__applauseDsl_Screen65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_UIActionNavigateAction"):
                opp_val = getattr(old_value, "applauseDsl_UIActionNavigateAction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_UIActionNavigateAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_UIActionNavigateAction"):
                opp_val = getattr(value, "applauseDsl_UIActionNavigateAction", None)
                setattr(value, "applauseDsl_UIActionNavigateAction", self)

    @property
    def applauseDsl_Screen41(self):
        return self.__applauseDsl_Screen41

    @applauseDsl_Screen41.setter
    def applauseDsl_Screen41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Screen__applauseDsl_Screen41", None)
        self.__applauseDsl_Screen41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_ScreenSection"):
                    opp_val = getattr(item, "applauseDsl_ScreenSection", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_ScreenSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_ScreenSection"):
                    opp_val = getattr(item, "applauseDsl_ScreenSection", None)
                    
                    setattr(item, "applauseDsl_ScreenSection", self)
                    

    @property
    def applauseDsl_Screen(self):
        return self.__applauseDsl_Screen

    @applauseDsl_Screen.setter
    def applauseDsl_Screen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Screen__applauseDsl_Screen", None)
        self.__applauseDsl_Screen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter37"):
                opp_val = getattr(old_value, "applauseDsl_Parameter37", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter37"):
                opp_val = getattr(value, "applauseDsl_Parameter37", None)
                setattr(value, "applauseDsl_Parameter37", self)

    @property
    def applauseDsl_Screen39(self):
        return self.__applauseDsl_Screen39

    @applauseDsl_Screen39.setter
    def applauseDsl_Screen39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Screen__applauseDsl_Screen39", None)
        self.__applauseDsl_Screen39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_DataSourceCall"):
                opp_val = getattr(old_value, "applauseDsl_DataSourceCall", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_DataSourceCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_DataSourceCall"):
                opp_val = getattr(value, "applauseDsl_DataSourceCall", None)
                setattr(value, "applauseDsl_DataSourceCall", self)

class applauseDsl_ListItemCellDeclaration(NamedElement):

    pass
class applauseDsl_UIComponentDeclaration(NamedElement, UIComponentOrDataType):

    pass
class applauseDsl_Type(NamedElement):

    pass
class applauseDsl_NamedElement:

    def __init__(self, name: str, applauseDsl_NamedElement: "applauseDsl_Model" = None):
        self.name = name
        self.applauseDsl_NamedElement = applauseDsl_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_NamedElement(self):
        return self.__applauseDsl_NamedElement

    @applauseDsl_NamedElement.setter
    def applauseDsl_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_NamedElement__applauseDsl_NamedElement", None)
        self.__applauseDsl_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Model"):
                opp_val = getattr(old_value, "applauseDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Model"):
                opp_val = getattr(value, "applauseDsl_Model", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class applauseDsl_Model:

    pass
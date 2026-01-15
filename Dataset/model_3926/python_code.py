from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SerializationFormat(Enum):
    XML = "XML"
    JSON = "JSON"
class CellType(Enum):
    default = "default"
    value1 = "value1"
    value2 = "value2"
    subtitle = "subtitle"
class TableViewStyle(Enum):
    Plain = "Plain"
    Grouped = "Grouped"
class CellAccessory(Enum):
    None = "None"
    Link = "Link"
    Detail = "Detail"
    Check = "Check"


############################################
# Definition of Classes
############################################

class ProviderConstruction:

    pass
class applauseDsl_ComplexProviderConstruction(ProviderConstruction):

    pass
class CollectionFunction:

    pass
class applauseDsl_StringSplit(CollectionFunction):

    pass
class StringFunction:

    pass
class applauseDsl_StringUrlConform(StringFunction):

    pass
class applauseDsl_StringReplace(StringFunction):

    pass
class applauseDsl_StringConcat(StringFunction):

    pass
class applauseDsl_SimpleProviderConstruction(ProviderConstruction):

    pass
class applauseDsl_ViewAction:

    pass
class ViewContentElement:

    pass
class applauseDsl_Cell(ViewContentElement):

    def __init__(self, type: str, accessory: str, applauseDsl_Cell: "applauseDsl_Section" = None, applauseDsl_Cell67: "applauseDsl_ScalarExpression" = None, applauseDsl_Cell70: "applauseDsl_ScalarExpression" = None, applauseDsl_Cell73: "applauseDsl_ScalarExpression" = None, applauseDsl_Cell76: "applauseDsl_ViewAction" = None):
        self.type = type
        self.accessory = accessory
        self.applauseDsl_Cell = applauseDsl_Cell
        self.applauseDsl_Cell67 = applauseDsl_Cell67
        self.applauseDsl_Cell70 = applauseDsl_Cell70
        self.applauseDsl_Cell73 = applauseDsl_Cell73
        self.applauseDsl_Cell76 = applauseDsl_Cell76
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def accessory(self) -> str:
        return self.__accessory

    @accessory.setter
    def accessory(self, accessory: str):
        self.__accessory = accessory

    @property
    def applauseDsl_Cell(self):
        return self.__applauseDsl_Cell

    @applauseDsl_Cell.setter
    def applauseDsl_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Cell__applauseDsl_Cell", None)
        self.__applauseDsl_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Section65"):
                opp_val = getattr(old_value, "applauseDsl_Section65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Section65"):
                opp_val = getattr(value, "applauseDsl_Section65", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Section65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_Cell67(self):
        return self.__applauseDsl_Cell67

    @applauseDsl_Cell67.setter
    def applauseDsl_Cell67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Cell__applauseDsl_Cell67", None)
        self.__applauseDsl_Cell67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression68"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression68", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression68"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression68", None)
                setattr(value, "applauseDsl_ScalarExpression68", self)

    @property
    def applauseDsl_Cell70(self):
        return self.__applauseDsl_Cell70

    @applauseDsl_Cell70.setter
    def applauseDsl_Cell70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Cell__applauseDsl_Cell70", None)
        self.__applauseDsl_Cell70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression71"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression71", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression71"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression71", None)
                setattr(value, "applauseDsl_ScalarExpression71", self)

    @property
    def applauseDsl_Cell76(self):
        return self.__applauseDsl_Cell76

    @applauseDsl_Cell76.setter
    def applauseDsl_Cell76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Cell__applauseDsl_Cell76", None)
        self.__applauseDsl_Cell76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewAction"):
                opp_val = getattr(old_value, "applauseDsl_ViewAction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewAction"):
                opp_val = getattr(value, "applauseDsl_ViewAction", None)
                setattr(value, "applauseDsl_ViewAction", self)

    @property
    def applauseDsl_Cell73(self):
        return self.__applauseDsl_Cell73

    @applauseDsl_Cell73.setter
    def applauseDsl_Cell73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Cell__applauseDsl_Cell73", None)
        self.__applauseDsl_Cell73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression74"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression74", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression74"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression74", None)
                setattr(value, "applauseDsl_ScalarExpression74", self)

class applauseDsl_ViewContentElement:

    pass
class applauseDsl_Section(ViewContentElement):

    pass
class ViewAction:

    pass
class applauseDsl_ExternalOpen(ViewAction):

    pass
class applauseDsl_Selector(ViewAction):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class applauseDsl_Tab:

    pass
class View:

    pass
class applauseDsl_CustomView(View):

    def __init__(self, className: str):
        self.className = className
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

class applauseDsl_TabView(View):

    pass
class applauseDsl_ProjectClass:

    def __init__(self, name: str, applauseDsl_ProjectClass: "applauseDsl_CustomContentProviderImplementation" = None):
        self.name = name
        self.applauseDsl_ProjectClass = applauseDsl_ProjectClass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_ProjectClass(self):
        return self.__applauseDsl_ProjectClass

    @applauseDsl_ProjectClass.setter
    def applauseDsl_ProjectClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ProjectClass__applauseDsl_ProjectClass", None)
        self.__applauseDsl_ProjectClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_CustomContentProviderImplementation"):
                opp_val = getattr(old_value, "applauseDsl_CustomContentProviderImplementation", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_CustomContentProviderImplementation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_CustomContentProviderImplementation"):
                opp_val = getattr(value, "applauseDsl_CustomContentProviderImplementation", None)
                setattr(value, "applauseDsl_CustomContentProviderImplementation", self)

class ContentProviderImplementation:

    pass
class applauseDsl_CustomContentProviderImplementation(ContentProviderImplementation):

    pass
class applauseDsl_FetchingContentProviderImplementation(ContentProviderImplementation):

    def __init__(self, format: str, applauseDsl_FetchingContentProviderImplementation: "applauseDsl_ScalarExpression" = None, applauseDsl_FetchingContentProviderImplementation35: "applauseDsl_ScalarExpression" = None):
        self.format = format
        self.applauseDsl_FetchingContentProviderImplementation = applauseDsl_FetchingContentProviderImplementation
        self.applauseDsl_FetchingContentProviderImplementation35 = applauseDsl_FetchingContentProviderImplementation35
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def applauseDsl_FetchingContentProviderImplementation35(self):
        return self.__applauseDsl_FetchingContentProviderImplementation35

    @applauseDsl_FetchingContentProviderImplementation35.setter
    def applauseDsl_FetchingContentProviderImplementation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_FetchingContentProviderImplementation__applauseDsl_FetchingContentProviderImplementation35", None)
        self.__applauseDsl_FetchingContentProviderImplementation35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression36"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression36", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression36"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression36", None)
                setattr(value, "applauseDsl_ScalarExpression36", self)

    @property
    def applauseDsl_FetchingContentProviderImplementation(self):
        return self.__applauseDsl_FetchingContentProviderImplementation

    @applauseDsl_FetchingContentProviderImplementation.setter
    def applauseDsl_FetchingContentProviderImplementation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_FetchingContentProviderImplementation__applauseDsl_FetchingContentProviderImplementation", None)
        self.__applauseDsl_FetchingContentProviderImplementation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression33"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression33", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression33"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression33", None)
                setattr(value, "applauseDsl_ScalarExpression33", self)

class applauseDsl_ContentProviderImplementation:

    pass
class applauseDsl_TableView(View):

    def __init__(self, style: str, applauseDsl_TableView: set["applauseDsl_Parameter"] = None, applauseDsl_TableView53: "applauseDsl_ScalarExpression" = None, applauseDsl_TableView56: "applauseDsl_ScalarExpression" = None, applauseDsl_TableView59: set["applauseDsl_Section"] = None):
        self.style = style
        self.applauseDsl_TableView = applauseDsl_TableView if applauseDsl_TableView is not None else set()
        self.applauseDsl_TableView53 = applauseDsl_TableView53
        self.applauseDsl_TableView56 = applauseDsl_TableView56
        self.applauseDsl_TableView59 = applauseDsl_TableView59 if applauseDsl_TableView59 is not None else set()
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def applauseDsl_TableView59(self):
        return self.__applauseDsl_TableView59

    @applauseDsl_TableView59.setter
    def applauseDsl_TableView59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TableView__applauseDsl_TableView59", None)
        self.__applauseDsl_TableView59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Section"):
                    opp_val = getattr(item, "applauseDsl_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Section"):
                    opp_val = getattr(item, "applauseDsl_Section", None)
                    
                    setattr(item, "applauseDsl_Section", self)
                    

    @property
    def applauseDsl_TableView56(self):
        return self.__applauseDsl_TableView56

    @applauseDsl_TableView56.setter
    def applauseDsl_TableView56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TableView__applauseDsl_TableView56", None)
        self.__applauseDsl_TableView56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression57"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression57", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression57"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression57", None)
                setattr(value, "applauseDsl_ScalarExpression57", self)

    @property
    def applauseDsl_TableView53(self):
        return self.__applauseDsl_TableView53

    @applauseDsl_TableView53.setter
    def applauseDsl_TableView53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TableView__applauseDsl_TableView53", None)
        self.__applauseDsl_TableView53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression54"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression54", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression54"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression54", None)
                setattr(value, "applauseDsl_ScalarExpression54", self)

    @property
    def applauseDsl_TableView(self):
        return self.__applauseDsl_TableView

    @applauseDsl_TableView.setter
    def applauseDsl_TableView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TableView__applauseDsl_TableView", None)
        self.__applauseDsl_TableView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Parameter51"):
                    opp_val = getattr(item, "applauseDsl_Parameter51", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Parameter51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Parameter51"):
                    opp_val = getattr(item, "applauseDsl_Parameter51", None)
                    
                    setattr(item, "applauseDsl_Parameter51", self)
                    

class Type:

    pass
class applauseDsl_Entity(Type):

    def __init__(self, runtimeType: bool, applauseDsl_Entity21: set["applauseDsl_Property"] = None, applauseDsl_Entity: "applauseDsl_Entity" = None, applauseDsl_Entity18: "applauseDsl_Entity" = None):
        self.runtimeType = runtimeType
        self.applauseDsl_Entity21 = applauseDsl_Entity21 if applauseDsl_Entity21 is not None else set()
        self.applauseDsl_Entity = applauseDsl_Entity
        self.applauseDsl_Entity18 = applauseDsl_Entity18
        
    @property
    def runtimeType(self) -> bool:
        return self.__runtimeType

    @runtimeType.setter
    def runtimeType(self, runtimeType: bool):
        self.__runtimeType = runtimeType

    @property
    def applauseDsl_Entity21(self):
        return self.__applauseDsl_Entity21

    @applauseDsl_Entity21.setter
    def applauseDsl_Entity21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity21", None)
        self.__applauseDsl_Entity21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Property"):
                    opp_val = getattr(item, "applauseDsl_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Property"):
                    opp_val = getattr(item, "applauseDsl_Property", None)
                    
                    setattr(item, "applauseDsl_Property", self)
                    

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
            if hasattr(old_value, "applauseDsl_Entity18"):
                opp_val = getattr(old_value, "applauseDsl_Entity18", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Entity18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity18"):
                opp_val = getattr(value, "applauseDsl_Entity18", None)
                setattr(value, "applauseDsl_Entity18", self)

    @property
    def applauseDsl_Entity18(self):
        return self.__applauseDsl_Entity18

    @applauseDsl_Entity18.setter
    def applauseDsl_Entity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Entity__applauseDsl_Entity18", None)
        self.__applauseDsl_Entity18 = value
        
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

class applauseDsl_SimpleType(Type):

    def __init__(self, platformType: str):
        self.platformType = platformType
        
    @property
    def platformType(self) -> str:
        return self.__platformType

    @platformType.setter
    def platformType(self, platformType: str):
        self.__platformType = platformType

class ModelElement:

    pass
class applauseDsl_View(ModelElement):

    pass
class applauseDsl_ContentProvider(ModelElement):

    def __init__(self, storing: bool, many: bool, applauseDsl_ContentProvider: "applauseDsl_Parameter" = None, applauseDsl_ContentProvider28: "applauseDsl_Type" = None, applauseDsl_ContentProvider31: "applauseDsl_ContentProviderImplementation" = None, applauseDsl_ContentProvider105: "applauseDsl_ComplexProviderConstruction" = None):
        self.storing = storing
        self.many = many
        self.applauseDsl_ContentProvider = applauseDsl_ContentProvider
        self.applauseDsl_ContentProvider28 = applauseDsl_ContentProvider28
        self.applauseDsl_ContentProvider31 = applauseDsl_ContentProvider31
        self.applauseDsl_ContentProvider105 = applauseDsl_ContentProvider105
        
    @property
    def storing(self) -> bool:
        return self.__storing

    @storing.setter
    def storing(self, storing: bool):
        self.__storing = storing

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def applauseDsl_ContentProvider(self):
        return self.__applauseDsl_ContentProvider

    @applauseDsl_ContentProvider.setter
    def applauseDsl_ContentProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider", None)
        self.__applauseDsl_ContentProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter26"):
                opp_val = getattr(old_value, "applauseDsl_Parameter26", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter26"):
                opp_val = getattr(value, "applauseDsl_Parameter26", None)
                setattr(value, "applauseDsl_Parameter26", self)

    @property
    def applauseDsl_ContentProvider31(self):
        return self.__applauseDsl_ContentProvider31

    @applauseDsl_ContentProvider31.setter
    def applauseDsl_ContentProvider31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider31", None)
        self.__applauseDsl_ContentProvider31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ContentProviderImplementation"):
                opp_val = getattr(old_value, "applauseDsl_ContentProviderImplementation", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ContentProviderImplementation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ContentProviderImplementation"):
                opp_val = getattr(value, "applauseDsl_ContentProviderImplementation", None)
                setattr(value, "applauseDsl_ContentProviderImplementation", self)

    @property
    def applauseDsl_ContentProvider28(self):
        return self.__applauseDsl_ContentProvider28

    @applauseDsl_ContentProvider28.setter
    def applauseDsl_ContentProvider28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider28", None)
        self.__applauseDsl_ContentProvider28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Type29"):
                opp_val = getattr(old_value, "applauseDsl_Type29", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Type29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Type29"):
                opp_val = getattr(value, "applauseDsl_Type29", None)
                setattr(value, "applauseDsl_Type29", self)

    @property
    def applauseDsl_ContentProvider105(self):
        return self.__applauseDsl_ContentProvider105

    @applauseDsl_ContentProvider105.setter
    def applauseDsl_ContentProvider105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider105", None)
        self.__applauseDsl_ContentProvider105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ComplexProviderConstruction"):
                opp_val = getattr(old_value, "applauseDsl_ComplexProviderConstruction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ComplexProviderConstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ComplexProviderConstruction"):
                opp_val = getattr(value, "applauseDsl_ComplexProviderConstruction", None)
                setattr(value, "applauseDsl_ComplexProviderConstruction", self)

class applauseDsl_ViewCall(ViewAction):

    pass
class applauseDsl_CollectionExpression:

    pass
class applauseDsl_ScalarExpression:

    pass
class applauseDsl_Expression:

    pass
class CollectionExpression:

    pass
class ScalarExpression:

    pass
class Expression:

    pass
class applauseDsl_StringFunction(ScalarExpression, Expression):

    pass
class applauseDsl_CollectionFunction(Expression, CollectionExpression):

    pass
class applauseDsl_CollectionLiteral(Expression, CollectionExpression):

    pass
class applauseDsl_StringLiteral(ScalarExpression, Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class applauseDsl_ObjectReference(ScalarExpression, Expression, CollectionExpression):

    pass
class applauseDsl_ProviderConstruction:

    pass
class applauseDsl_ModelElement:

    def __init__(self, name: str, applauseDsl_ModelElement: "applauseDsl_Model" = None):
        self.name = name
        self.applauseDsl_ModelElement = applauseDsl_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_ModelElement(self):
        return self.__applauseDsl_ModelElement

    @applauseDsl_ModelElement.setter
    def applauseDsl_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ModelElement__applauseDsl_ModelElement", None)
        self.__applauseDsl_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Model2"):
                opp_val = getattr(old_value, "applauseDsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Model2"):
                opp_val = getattr(value, "applauseDsl_Model2", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class applauseDsl_Application:

    def __init__(self, name: str, applauseDsl_Application: "applauseDsl_Model" = None, applauseDsl_Application14: "applauseDsl_ScalarExpression" = None, applauseDsl_Application17: "applauseDsl_ViewCall" = None):
        self.name = name
        self.applauseDsl_Application = applauseDsl_Application
        self.applauseDsl_Application14 = applauseDsl_Application14
        self.applauseDsl_Application17 = applauseDsl_Application17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_Application(self):
        return self.__applauseDsl_Application

    @applauseDsl_Application.setter
    def applauseDsl_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application", None)
        self.__applauseDsl_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Model"):
                opp_val = getattr(old_value, "applauseDsl_Model", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Model"):
                opp_val = getattr(value, "applauseDsl_Model", None)
                setattr(value, "applauseDsl_Model", self)

    @property
    def applauseDsl_Application17(self):
        return self.__applauseDsl_Application17

    @applauseDsl_Application17.setter
    def applauseDsl_Application17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application17", None)
        self.__applauseDsl_Application17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewCall"):
                opp_val = getattr(old_value, "applauseDsl_ViewCall", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewCall"):
                opp_val = getattr(value, "applauseDsl_ViewCall", None)
                setattr(value, "applauseDsl_ViewCall", self)

    @property
    def applauseDsl_Application14(self):
        return self.__applauseDsl_Application14

    @applauseDsl_Application14.setter
    def applauseDsl_Application14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application14", None)
        self.__applauseDsl_Application14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression15"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression15", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression15"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression15", None)
                setattr(value, "applauseDsl_ScalarExpression15", self)

class applauseDsl_Model:

    pass
class PropertyPathPart:

    pass
class applauseDsl_Property(PropertyPathPart):

    def __init__(self, derived: bool, applauseDsl_Property: "applauseDsl_Entity" = None, applauseDsl_Property23: "applauseDsl_TypeDescription" = None):
        self.derived = derived
        self.applauseDsl_Property = applauseDsl_Property
        self.applauseDsl_Property23 = applauseDsl_Property23
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def applauseDsl_Property23(self):
        return self.__applauseDsl_Property23

    @applauseDsl_Property23.setter
    def applauseDsl_Property23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Property__applauseDsl_Property23", None)
        self.__applauseDsl_Property23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_TypeDescription24"):
                opp_val = getattr(old_value, "applauseDsl_TypeDescription24", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_TypeDescription24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_TypeDescription24"):
                opp_val = getattr(value, "applauseDsl_TypeDescription24", None)
                setattr(value, "applauseDsl_TypeDescription24", self)

    @property
    def applauseDsl_Property(self):
        return self.__applauseDsl_Property

    @applauseDsl_Property.setter
    def applauseDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Property__applauseDsl_Property", None)
        self.__applauseDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Entity21"):
                opp_val = getattr(old_value, "applauseDsl_Entity21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity21"):
                opp_val = getattr(value, "applauseDsl_Entity21", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Entity21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class applauseDsl_CollectionIterator(PropertyPathPart):

    pass
class applauseDsl_Parameter(PropertyPathPart):

    pass
class applauseDsl_Type(ModelElement):

    pass
class applauseDsl_TypeDescription:

    def __init__(self, many: bool, applauseDsl_TypeDescription: "applauseDsl_Type" = None, applauseDsl_TypeDescription24: "applauseDsl_Property" = None, applauseDsl_TypeDescription5: "applauseDsl_Parameter" = None):
        self.many = many
        self.applauseDsl_TypeDescription = applauseDsl_TypeDescription
        self.applauseDsl_TypeDescription24 = applauseDsl_TypeDescription24
        self.applauseDsl_TypeDescription5 = applauseDsl_TypeDescription5
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def applauseDsl_TypeDescription(self):
        return self.__applauseDsl_TypeDescription

    @applauseDsl_TypeDescription.setter
    def applauseDsl_TypeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription", None)
        self.__applauseDsl_TypeDescription = value
        
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
    def applauseDsl_TypeDescription24(self):
        return self.__applauseDsl_TypeDescription24

    @applauseDsl_TypeDescription24.setter
    def applauseDsl_TypeDescription24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription24", None)
        self.__applauseDsl_TypeDescription24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Property23"):
                opp_val = getattr(old_value, "applauseDsl_Property23", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Property23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Property23"):
                opp_val = getattr(value, "applauseDsl_Property23", None)
                setattr(value, "applauseDsl_Property23", self)

    @property
    def applauseDsl_TypeDescription5(self):
        return self.__applauseDsl_TypeDescription5

    @applauseDsl_TypeDescription5.setter
    def applauseDsl_TypeDescription5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription5", None)
        self.__applauseDsl_TypeDescription5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter"):
                opp_val = getattr(old_value, "applauseDsl_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter"):
                opp_val = getattr(value, "applauseDsl_Parameter", None)
                setattr(value, "applauseDsl_Parameter", self)

class applauseDsl_PropertyPathPart:

    def __init__(self, name: str, applauseDsl_PropertyPathPart: "applauseDsl_ObjectReference" = None):
        self.name = name
        self.applauseDsl_PropertyPathPart = applauseDsl_PropertyPathPart
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_PropertyPathPart(self):
        return self.__applauseDsl_PropertyPathPart

    @applauseDsl_PropertyPathPart.setter
    def applauseDsl_PropertyPathPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_PropertyPathPart__applauseDsl_PropertyPathPart", None)
        self.__applauseDsl_PropertyPathPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ObjectReference"):
                opp_val = getattr(old_value, "applauseDsl_ObjectReference", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ObjectReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ObjectReference"):
                opp_val = getattr(value, "applauseDsl_ObjectReference", None)
                setattr(value, "applauseDsl_ObjectReference", self)

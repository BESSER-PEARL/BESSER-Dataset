from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Device(Enum):
    iphone = "iphone"
    ipad = "ipad"
    android4 = "android4"
    android2 = "android2"


############################################
# Definition of Classes
############################################

class appBuilderDSL_Feature:

    def __init__(self, many: bool, name: str, appBuilderDSL_Feature: "appBuilderDSL_Entity" = None, appBuilderDSL_Feature110: "appBuilderDSL_Type" = None):
        self.many = many
        self.name = name
        self.appBuilderDSL_Feature = appBuilderDSL_Feature
        self.appBuilderDSL_Feature110 = appBuilderDSL_Feature110
        
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
    def appBuilderDSL_Feature(self):
        return self.__appBuilderDSL_Feature

    @appBuilderDSL_Feature.setter
    def appBuilderDSL_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Feature__appBuilderDSL_Feature", None)
        self.__appBuilderDSL_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Entity108"):
                opp_val = getattr(old_value, "appBuilderDSL_Entity108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Entity108"):
                opp_val = getattr(value, "appBuilderDSL_Entity108", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_Entity108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Feature110(self):
        return self.__appBuilderDSL_Feature110

    @appBuilderDSL_Feature110.setter
    def appBuilderDSL_Feature110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Feature__appBuilderDSL_Feature110", None)
        self.__appBuilderDSL_Feature110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Type"):
                opp_val = getattr(old_value, "appBuilderDSL_Type", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Type"):
                opp_val = getattr(value, "appBuilderDSL_Type", None)
                setattr(value, "appBuilderDSL_Type", self)

class Type:

    pass
class appBuilderDSL_Entity(Type):

    pass
class appBuilderDSL_DataType(Type):

    pass
class appBuilderDSL_Type:

    def __init__(self, name: str, appBuilderDSL_Type: "appBuilderDSL_Feature" = None):
        self.name = name
        self.appBuilderDSL_Type = appBuilderDSL_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Type(self):
        return self.__appBuilderDSL_Type

    @appBuilderDSL_Type.setter
    def appBuilderDSL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Type__appBuilderDSL_Type", None)
        self.__appBuilderDSL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Feature110"):
                opp_val = getattr(old_value, "appBuilderDSL_Feature110", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Feature110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Feature110"):
                opp_val = getattr(value, "appBuilderDSL_Feature110", None)
                setattr(value, "appBuilderDSL_Feature110", self)

class appBuilderDSL_Import:

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class appBuilderDSL_Expression:

    def __init__(self, terms: str, appBuilderDSL_Expression: "appBuilderDSL_DynamicValue" = None):
        self.terms = terms
        self.appBuilderDSL_Expression = appBuilderDSL_Expression
        
    @property
    def terms(self) -> str:
        return self.__terms

    @terms.setter
    def terms(self, terms: str):
        self.__terms = terms

    @property
    def appBuilderDSL_Expression(self):
        return self.__appBuilderDSL_Expression

    @appBuilderDSL_Expression.setter
    def appBuilderDSL_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Expression__appBuilderDSL_Expression", None)
        self.__appBuilderDSL_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_DynamicValue"):
                opp_val = getattr(old_value, "appBuilderDSL_DynamicValue", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_DynamicValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_DynamicValue"):
                opp_val = getattr(value, "appBuilderDSL_DynamicValue", None)
                setattr(value, "appBuilderDSL_DynamicValue", self)

class Value:

    pass
class appBuilderDSL_Value:

    pass
class Layout:

    pass
class appBuilderDSL_RowLayout(Layout):

    pass
class appBuilderDSL_GridLayout(Layout):

    def __init__(self, columns: int):
        self.columns = columns
        
    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

class Control:

    pass
class appBuilderDSL_Text(Control):

    def __init__(self, name: str, appBuilderDSL_Text: "appBuilderDSL_Value" = None, appBuilderDSL_Text94: "appBuilderDSL_Value" = None):
        self.name = name
        self.appBuilderDSL_Text = appBuilderDSL_Text
        self.appBuilderDSL_Text94 = appBuilderDSL_Text94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Text94(self):
        return self.__appBuilderDSL_Text94

    @appBuilderDSL_Text94.setter
    def appBuilderDSL_Text94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Text__appBuilderDSL_Text94", None)
        self.__appBuilderDSL_Text94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value95"):
                opp_val = getattr(old_value, "appBuilderDSL_Value95", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value95"):
                opp_val = getattr(value, "appBuilderDSL_Value95", None)
                setattr(value, "appBuilderDSL_Value95", self)

    @property
    def appBuilderDSL_Text(self):
        return self.__appBuilderDSL_Text

    @appBuilderDSL_Text.setter
    def appBuilderDSL_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Text__appBuilderDSL_Text", None)
        self.__appBuilderDSL_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value92"):
                opp_val = getattr(old_value, "appBuilderDSL_Value92", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value92"):
                opp_val = getattr(value, "appBuilderDSL_Value92", None)
                setattr(value, "appBuilderDSL_Value92", self)

class appBuilderDSL_Button(Control):

    def __init__(self, name: str, appBuilderDSL_Button: "appBuilderDSL_Value" = None, appBuilderDSL_Button99: "appBuilderDSL_Value" = None):
        self.name = name
        self.appBuilderDSL_Button = appBuilderDSL_Button
        self.appBuilderDSL_Button99 = appBuilderDSL_Button99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Button99(self):
        return self.__appBuilderDSL_Button99

    @appBuilderDSL_Button99.setter
    def appBuilderDSL_Button99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Button__appBuilderDSL_Button99", None)
        self.__appBuilderDSL_Button99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value100"):
                opp_val = getattr(old_value, "appBuilderDSL_Value100", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value100"):
                opp_val = getattr(value, "appBuilderDSL_Value100", None)
                setattr(value, "appBuilderDSL_Value100", self)

    @property
    def appBuilderDSL_Button(self):
        return self.__appBuilderDSL_Button

    @appBuilderDSL_Button.setter
    def appBuilderDSL_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Button__appBuilderDSL_Button", None)
        self.__appBuilderDSL_Button = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value97"):
                opp_val = getattr(old_value, "appBuilderDSL_Value97", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value97"):
                opp_val = getattr(value, "appBuilderDSL_Value97", None)
                setattr(value, "appBuilderDSL_Value97", self)

class appBuilderDSL_ScreenLayout(Control):

    pass
class appBuilderDSL_Label(Control):

    def __init__(self, name: str, appBuilderDSL_Label: "appBuilderDSL_Value" = None):
        self.name = name
        self.appBuilderDSL_Label = appBuilderDSL_Label
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Label(self):
        return self.__appBuilderDSL_Label

    @appBuilderDSL_Label.setter
    def appBuilderDSL_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Label__appBuilderDSL_Label", None)
        self.__appBuilderDSL_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value102"):
                opp_val = getattr(old_value, "appBuilderDSL_Value102", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value102"):
                opp_val = getattr(value, "appBuilderDSL_Value102", None)
                setattr(value, "appBuilderDSL_Value102", self)

class appBuilderDSL_Layout(Control):

    def __init__(self, type: str, appBuilderDSL_Layout: "appBuilderDSL_View" = None, appBuilderDSL_Layout79: set["appBuilderDSL_Control"] = None, appBuilderDSL_Layout104: "appBuilderDSL_CompositeScreen" = None):
        self.type = type
        self.appBuilderDSL_Layout = appBuilderDSL_Layout
        self.appBuilderDSL_Layout79 = appBuilderDSL_Layout79 if appBuilderDSL_Layout79 is not None else set()
        self.appBuilderDSL_Layout104 = appBuilderDSL_Layout104
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def appBuilderDSL_Layout104(self):
        return self.__appBuilderDSL_Layout104

    @appBuilderDSL_Layout104.setter
    def appBuilderDSL_Layout104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Layout__appBuilderDSL_Layout104", None)
        self.__appBuilderDSL_Layout104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_CompositeScreen"):
                opp_val = getattr(old_value, "appBuilderDSL_CompositeScreen", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_CompositeScreen"):
                opp_val = getattr(value, "appBuilderDSL_CompositeScreen", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_CompositeScreen", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Layout79(self):
        return self.__appBuilderDSL_Layout79

    @appBuilderDSL_Layout79.setter
    def appBuilderDSL_Layout79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Layout__appBuilderDSL_Layout79", None)
        self.__appBuilderDSL_Layout79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appBuilderDSL_Control80"):
                    opp_val = getattr(item, "appBuilderDSL_Control80", None)
                    
                    if opp_val == self:
                        setattr(item, "appBuilderDSL_Control80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appBuilderDSL_Control80"):
                    opp_val = getattr(item, "appBuilderDSL_Control80", None)
                    
                    setattr(item, "appBuilderDSL_Control80", self)
                    

    @property
    def appBuilderDSL_Layout(self):
        return self.__appBuilderDSL_Layout

    @appBuilderDSL_Layout.setter
    def appBuilderDSL_Layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Layout__appBuilderDSL_Layout", None)
        self.__appBuilderDSL_Layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_View77"):
                opp_val = getattr(old_value, "appBuilderDSL_View77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_View77"):
                opp_val = getattr(value, "appBuilderDSL_View77", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_View77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class appBuilderDSL_List(Control):

    def __init__(self, name: str, appBuilderDSL_List: "appBuilderDSL_Value" = None, appBuilderDSL_List85: "appBuilderDSL_Value" = None, appBuilderDSL_List88: "appBuilderDSL_Value" = None):
        self.name = name
        self.appBuilderDSL_List = appBuilderDSL_List
        self.appBuilderDSL_List85 = appBuilderDSL_List85
        self.appBuilderDSL_List88 = appBuilderDSL_List88
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_List85(self):
        return self.__appBuilderDSL_List85

    @appBuilderDSL_List85.setter
    def appBuilderDSL_List85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_List__appBuilderDSL_List85", None)
        self.__appBuilderDSL_List85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value86"):
                opp_val = getattr(old_value, "appBuilderDSL_Value86", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value86"):
                opp_val = getattr(value, "appBuilderDSL_Value86", None)
                setattr(value, "appBuilderDSL_Value86", self)

    @property
    def appBuilderDSL_List(self):
        return self.__appBuilderDSL_List

    @appBuilderDSL_List.setter
    def appBuilderDSL_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_List__appBuilderDSL_List", None)
        self.__appBuilderDSL_List = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value"):
                opp_val = getattr(old_value, "appBuilderDSL_Value", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value"):
                opp_val = getattr(value, "appBuilderDSL_Value", None)
                setattr(value, "appBuilderDSL_Value", self)

    @property
    def appBuilderDSL_List88(self):
        return self.__appBuilderDSL_List88

    @appBuilderDSL_List88.setter
    def appBuilderDSL_List88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_List__appBuilderDSL_List88", None)
        self.__appBuilderDSL_List88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Value89"):
                opp_val = getattr(old_value, "appBuilderDSL_Value89", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Value89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Value89"):
                opp_val = getattr(value, "appBuilderDSL_Value89", None)
                setattr(value, "appBuilderDSL_Value89", self)

class SetInstructionAssignment:

    pass
class appBuilderDSL_ControlValue(SetInstructionAssignment):

    def __init__(self, controlAccess: str, appBuilderDSL_ControlValue: "appBuilderDSL_Control" = None):
        self.controlAccess = controlAccess
        self.appBuilderDSL_ControlValue = appBuilderDSL_ControlValue
        
    @property
    def controlAccess(self) -> str:
        return self.__controlAccess

    @controlAccess.setter
    def controlAccess(self, controlAccess: str):
        self.__controlAccess = controlAccess

    @property
    def appBuilderDSL_ControlValue(self):
        return self.__appBuilderDSL_ControlValue

    @appBuilderDSL_ControlValue.setter
    def appBuilderDSL_ControlValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_ControlValue__appBuilderDSL_ControlValue", None)
        self.__appBuilderDSL_ControlValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Control72"):
                opp_val = getattr(old_value, "appBuilderDSL_Control72", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Control72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Control72"):
                opp_val = getattr(value, "appBuilderDSL_Control72", None)
                setattr(value, "appBuilderDSL_Control72", self)

class appBuilderDSL_DynamicValue(Value, SetInstructionAssignment):

    def __init__(self, variableName: str, type: str, appBuilderDSL_DynamicValue: "appBuilderDSL_Expression" = None):
        self.variableName = variableName
        self.type = type
        self.appBuilderDSL_DynamicValue = appBuilderDSL_DynamicValue
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def appBuilderDSL_DynamicValue(self):
        return self.__appBuilderDSL_DynamicValue

    @appBuilderDSL_DynamicValue.setter
    def appBuilderDSL_DynamicValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_DynamicValue__appBuilderDSL_DynamicValue", None)
        self.__appBuilderDSL_DynamicValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Expression"):
                opp_val = getattr(old_value, "appBuilderDSL_Expression", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Expression"):
                opp_val = getattr(value, "appBuilderDSL_Expression", None)
                setattr(value, "appBuilderDSL_Expression", self)

class appBuilderDSL_RestCall(SetInstructionAssignment):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class appBuilderDSL_SetInstructionAssignment:

    pass
class Instruction:

    pass
class appBuilderDSL_ExecuteAction(Instruction):

    pass
class appBuilderDSL_Navigate(Instruction):

    def __init__(self, params: str, appBuilderDSL_Navigate: "appBuilderDSL_Screen" = None):
        self.params = params
        self.appBuilderDSL_Navigate = appBuilderDSL_Navigate
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def appBuilderDSL_Navigate(self):
        return self.__appBuilderDSL_Navigate

    @appBuilderDSL_Navigate.setter
    def appBuilderDSL_Navigate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Navigate__appBuilderDSL_Navigate", None)
        self.__appBuilderDSL_Navigate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Screen68"):
                opp_val = getattr(old_value, "appBuilderDSL_Screen68", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Screen68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Screen68"):
                opp_val = getattr(value, "appBuilderDSL_Screen68", None)
                setattr(value, "appBuilderDSL_Screen68", self)

class appBuilderDSL_SetInstruction(Instruction):

    def __init__(self, modelAccess: str, appBuilderDSL_SetInstruction: "appBuilderDSL_Attribute" = None, appBuilderDSL_SetInstruction66: "appBuilderDSL_SetInstructionAssignment" = None):
        self.modelAccess = modelAccess
        self.appBuilderDSL_SetInstruction = appBuilderDSL_SetInstruction
        self.appBuilderDSL_SetInstruction66 = appBuilderDSL_SetInstruction66
        
    @property
    def modelAccess(self) -> str:
        return self.__modelAccess

    @modelAccess.setter
    def modelAccess(self, modelAccess: str):
        self.__modelAccess = modelAccess

    @property
    def appBuilderDSL_SetInstruction66(self):
        return self.__appBuilderDSL_SetInstruction66

    @appBuilderDSL_SetInstruction66.setter
    def appBuilderDSL_SetInstruction66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_SetInstruction__appBuilderDSL_SetInstruction66", None)
        self.__appBuilderDSL_SetInstruction66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_SetInstructionAssignment"):
                opp_val = getattr(old_value, "appBuilderDSL_SetInstructionAssignment", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_SetInstructionAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_SetInstructionAssignment"):
                opp_val = getattr(value, "appBuilderDSL_SetInstructionAssignment", None)
                setattr(value, "appBuilderDSL_SetInstructionAssignment", self)

    @property
    def appBuilderDSL_SetInstruction(self):
        return self.__appBuilderDSL_SetInstruction

    @appBuilderDSL_SetInstruction.setter
    def appBuilderDSL_SetInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_SetInstruction__appBuilderDSL_SetInstruction", None)
        self.__appBuilderDSL_SetInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Attribute64"):
                opp_val = getattr(old_value, "appBuilderDSL_Attribute64", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Attribute64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Attribute64"):
                opp_val = getattr(value, "appBuilderDSL_Attribute64", None)
                setattr(value, "appBuilderDSL_Attribute64", self)

class Action:

    pass
class appBuilderDSL_UiAction(Action):

    def __init__(self, name: str, appBuilderDSL_UiAction: set["appBuilderDSL_Instruction"] = None):
        self.name = name
        self.appBuilderDSL_UiAction = appBuilderDSL_UiAction if appBuilderDSL_UiAction is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_UiAction(self):
        return self.__appBuilderDSL_UiAction

    @appBuilderDSL_UiAction.setter
    def appBuilderDSL_UiAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_UiAction__appBuilderDSL_UiAction", None)
        self.__appBuilderDSL_UiAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appBuilderDSL_Instruction62"):
                    opp_val = getattr(item, "appBuilderDSL_Instruction62", None)
                    
                    if opp_val == self:
                        setattr(item, "appBuilderDSL_Instruction62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appBuilderDSL_Instruction62"):
                    opp_val = getattr(item, "appBuilderDSL_Instruction62", None)
                    
                    setattr(item, "appBuilderDSL_Instruction62", self)
                    

class ConditionExpression:

    pass
class appBuilderDSL_CompositeConditionExpression(ConditionExpression):

    pass
class appBuilderDSL_SimpleConditionExpression(ConditionExpression):

    def __init__(self, variableName: str):
        self.variableName = variableName
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class appBuilderDSL_ConditionExpression:

    pass
class DataBinding:

    pass
class appBuilderDSL_EnumDataBinding(DataBinding):

    def __init__(self, enumClassName: str):
        self.enumClassName = enumClassName
        
    @property
    def enumClassName(self) -> str:
        return self.__enumClassName

    @enumClassName.setter
    def enumClassName(self, enumClassName: str):
        self.__enumClassName = enumClassName

class appBuilderDSL_SimpleDataBinding(DataBinding):

    def __init__(self, modelAccess: str, appBuilderDSL_SimpleDataBinding: "appBuilderDSL_Attribute" = None):
        self.modelAccess = modelAccess
        self.appBuilderDSL_SimpleDataBinding = appBuilderDSL_SimpleDataBinding
        
    @property
    def modelAccess(self) -> str:
        return self.__modelAccess

    @modelAccess.setter
    def modelAccess(self, modelAccess: str):
        self.__modelAccess = modelAccess

    @property
    def appBuilderDSL_SimpleDataBinding(self):
        return self.__appBuilderDSL_SimpleDataBinding

    @appBuilderDSL_SimpleDataBinding.setter
    def appBuilderDSL_SimpleDataBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_SimpleDataBinding__appBuilderDSL_SimpleDataBinding", None)
        self.__appBuilderDSL_SimpleDataBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Attribute53"):
                opp_val = getattr(old_value, "appBuilderDSL_Attribute53", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Attribute53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Attribute53"):
                opp_val = getattr(value, "appBuilderDSL_Attribute53", None)
                setattr(value, "appBuilderDSL_Attribute53", self)

class appBuilderDSL_Control:

    pass
class appBuilderDSL_Condition:

    def __init__(self, name: str, appBuilderDSL_Condition: "appBuilderDSL_ValidationBinding" = None, appBuilderDSL_Condition56: "appBuilderDSL_Validator" = None, appBuilderDSL_Condition58: "appBuilderDSL_ConditionExpression" = None, appBuilderDSL_Condition60: "appBuilderDSL_CompositeConditionExpression" = None):
        self.name = name
        self.appBuilderDSL_Condition = appBuilderDSL_Condition
        self.appBuilderDSL_Condition56 = appBuilderDSL_Condition56
        self.appBuilderDSL_Condition58 = appBuilderDSL_Condition58
        self.appBuilderDSL_Condition60 = appBuilderDSL_Condition60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Condition56(self):
        return self.__appBuilderDSL_Condition56

    @appBuilderDSL_Condition56.setter
    def appBuilderDSL_Condition56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Condition__appBuilderDSL_Condition56", None)
        self.__appBuilderDSL_Condition56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Validator55"):
                opp_val = getattr(old_value, "appBuilderDSL_Validator55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Validator55"):
                opp_val = getattr(value, "appBuilderDSL_Validator55", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_Validator55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Condition(self):
        return self.__appBuilderDSL_Condition

    @appBuilderDSL_Condition.setter
    def appBuilderDSL_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Condition__appBuilderDSL_Condition", None)
        self.__appBuilderDSL_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_ValidationBinding40"):
                opp_val = getattr(old_value, "appBuilderDSL_ValidationBinding40", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_ValidationBinding40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_ValidationBinding40"):
                opp_val = getattr(value, "appBuilderDSL_ValidationBinding40", None)
                setattr(value, "appBuilderDSL_ValidationBinding40", self)

    @property
    def appBuilderDSL_Condition60(self):
        return self.__appBuilderDSL_Condition60

    @appBuilderDSL_Condition60.setter
    def appBuilderDSL_Condition60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Condition__appBuilderDSL_Condition60", None)
        self.__appBuilderDSL_Condition60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_CompositeConditionExpression"):
                opp_val = getattr(old_value, "appBuilderDSL_CompositeConditionExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_CompositeConditionExpression"):
                opp_val = getattr(value, "appBuilderDSL_CompositeConditionExpression", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_CompositeConditionExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Condition58(self):
        return self.__appBuilderDSL_Condition58

    @appBuilderDSL_Condition58.setter
    def appBuilderDSL_Condition58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Condition__appBuilderDSL_Condition58", None)
        self.__appBuilderDSL_Condition58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_ConditionExpression"):
                opp_val = getattr(old_value, "appBuilderDSL_ConditionExpression", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_ConditionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_ConditionExpression"):
                opp_val = getattr(value, "appBuilderDSL_ConditionExpression", None)
                setattr(value, "appBuilderDSL_ConditionExpression", self)

class appBuilderDSL_Instruction:

    pass
class appBuilderDSL_ValidationBinding:

    def __init__(self, controlAccess: str, appBuilderDSL_ValidationBinding: "appBuilderDSL_InitAction" = None, appBuilderDSL_ValidationBinding40: "appBuilderDSL_Condition" = None, appBuilderDSL_ValidationBinding42: "appBuilderDSL_Control" = None):
        self.controlAccess = controlAccess
        self.appBuilderDSL_ValidationBinding = appBuilderDSL_ValidationBinding
        self.appBuilderDSL_ValidationBinding40 = appBuilderDSL_ValidationBinding40
        self.appBuilderDSL_ValidationBinding42 = appBuilderDSL_ValidationBinding42
        
    @property
    def controlAccess(self) -> str:
        return self.__controlAccess

    @controlAccess.setter
    def controlAccess(self, controlAccess: str):
        self.__controlAccess = controlAccess

    @property
    def appBuilderDSL_ValidationBinding(self):
        return self.__appBuilderDSL_ValidationBinding

    @appBuilderDSL_ValidationBinding.setter
    def appBuilderDSL_ValidationBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_ValidationBinding__appBuilderDSL_ValidationBinding", None)
        self.__appBuilderDSL_ValidationBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_InitAction36"):
                opp_val = getattr(old_value, "appBuilderDSL_InitAction36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_InitAction36"):
                opp_val = getattr(value, "appBuilderDSL_InitAction36", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_InitAction36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_ValidationBinding40(self):
        return self.__appBuilderDSL_ValidationBinding40

    @appBuilderDSL_ValidationBinding40.setter
    def appBuilderDSL_ValidationBinding40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_ValidationBinding__appBuilderDSL_ValidationBinding40", None)
        self.__appBuilderDSL_ValidationBinding40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Condition"):
                opp_val = getattr(old_value, "appBuilderDSL_Condition", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Condition"):
                opp_val = getattr(value, "appBuilderDSL_Condition", None)
                setattr(value, "appBuilderDSL_Condition", self)

    @property
    def appBuilderDSL_ValidationBinding42(self):
        return self.__appBuilderDSL_ValidationBinding42

    @appBuilderDSL_ValidationBinding42.setter
    def appBuilderDSL_ValidationBinding42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_ValidationBinding__appBuilderDSL_ValidationBinding42", None)
        self.__appBuilderDSL_ValidationBinding42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Control"):
                opp_val = getattr(old_value, "appBuilderDSL_Control", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Control", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Control"):
                opp_val = getattr(value, "appBuilderDSL_Control", None)
                setattr(value, "appBuilderDSL_Control", self)

class appBuilderDSL_UiListenerBinding:

    def __init__(self, controlAccess: str, appBuilderDSL_UiListenerBinding: "appBuilderDSL_InitAction" = None, appBuilderDSL_UiListenerBinding44: "appBuilderDSL_Action" = None, appBuilderDSL_UiListenerBinding47: "appBuilderDSL_Control" = None):
        self.controlAccess = controlAccess
        self.appBuilderDSL_UiListenerBinding = appBuilderDSL_UiListenerBinding
        self.appBuilderDSL_UiListenerBinding44 = appBuilderDSL_UiListenerBinding44
        self.appBuilderDSL_UiListenerBinding47 = appBuilderDSL_UiListenerBinding47
        
    @property
    def controlAccess(self) -> str:
        return self.__controlAccess

    @controlAccess.setter
    def controlAccess(self, controlAccess: str):
        self.__controlAccess = controlAccess

    @property
    def appBuilderDSL_UiListenerBinding(self):
        return self.__appBuilderDSL_UiListenerBinding

    @appBuilderDSL_UiListenerBinding.setter
    def appBuilderDSL_UiListenerBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_UiListenerBinding__appBuilderDSL_UiListenerBinding", None)
        self.__appBuilderDSL_UiListenerBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_InitAction34"):
                opp_val = getattr(old_value, "appBuilderDSL_InitAction34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_InitAction34"):
                opp_val = getattr(value, "appBuilderDSL_InitAction34", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_InitAction34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_UiListenerBinding44(self):
        return self.__appBuilderDSL_UiListenerBinding44

    @appBuilderDSL_UiListenerBinding44.setter
    def appBuilderDSL_UiListenerBinding44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_UiListenerBinding__appBuilderDSL_UiListenerBinding44", None)
        self.__appBuilderDSL_UiListenerBinding44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Action45"):
                opp_val = getattr(old_value, "appBuilderDSL_Action45", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Action45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Action45"):
                opp_val = getattr(value, "appBuilderDSL_Action45", None)
                setattr(value, "appBuilderDSL_Action45", self)

    @property
    def appBuilderDSL_UiListenerBinding47(self):
        return self.__appBuilderDSL_UiListenerBinding47

    @appBuilderDSL_UiListenerBinding47.setter
    def appBuilderDSL_UiListenerBinding47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_UiListenerBinding__appBuilderDSL_UiListenerBinding47", None)
        self.__appBuilderDSL_UiListenerBinding47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Control48"):
                opp_val = getattr(old_value, "appBuilderDSL_Control48", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Control48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Control48"):
                opp_val = getattr(value, "appBuilderDSL_Control48", None)
                setattr(value, "appBuilderDSL_Control48", self)

class appBuilderDSL_DataBinding:

    def __init__(self, controlAccess: str, appBuilderDSL_DataBinding: "appBuilderDSL_InitAction" = None, appBuilderDSL_DataBinding50: "appBuilderDSL_Control" = None):
        self.controlAccess = controlAccess
        self.appBuilderDSL_DataBinding = appBuilderDSL_DataBinding
        self.appBuilderDSL_DataBinding50 = appBuilderDSL_DataBinding50
        
    @property
    def controlAccess(self) -> str:
        return self.__controlAccess

    @controlAccess.setter
    def controlAccess(self, controlAccess: str):
        self.__controlAccess = controlAccess

    @property
    def appBuilderDSL_DataBinding50(self):
        return self.__appBuilderDSL_DataBinding50

    @appBuilderDSL_DataBinding50.setter
    def appBuilderDSL_DataBinding50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_DataBinding__appBuilderDSL_DataBinding50", None)
        self.__appBuilderDSL_DataBinding50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Control51"):
                opp_val = getattr(old_value, "appBuilderDSL_Control51", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Control51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Control51"):
                opp_val = getattr(value, "appBuilderDSL_Control51", None)
                setattr(value, "appBuilderDSL_Control51", self)

    @property
    def appBuilderDSL_DataBinding(self):
        return self.__appBuilderDSL_DataBinding

    @appBuilderDSL_DataBinding.setter
    def appBuilderDSL_DataBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_DataBinding__appBuilderDSL_DataBinding", None)
        self.__appBuilderDSL_DataBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_InitAction32"):
                opp_val = getattr(old_value, "appBuilderDSL_InitAction32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_InitAction32"):
                opp_val = getattr(value, "appBuilderDSL_InitAction32", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_InitAction32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class appBuilderDSL_Action:

    pass
class appBuilderDSL_Validator:

    pass
class appBuilderDSL_InitAction:

    pass
class appBuilderDSL_Attribute:

    def __init__(self, name: str, type: str, appBuilderDSL_Attribute: "appBuilderDSL_EntryParameters" = None, appBuilderDSL_Attribute53: "appBuilderDSL_SimpleDataBinding" = None, appBuilderDSL_Attribute64: "appBuilderDSL_SetInstruction" = None, appBuilderDSL_Attribute75: "appBuilderDSL_Model" = None):
        self.name = name
        self.type = type
        self.appBuilderDSL_Attribute = appBuilderDSL_Attribute
        self.appBuilderDSL_Attribute53 = appBuilderDSL_Attribute53
        self.appBuilderDSL_Attribute64 = appBuilderDSL_Attribute64
        self.appBuilderDSL_Attribute75 = appBuilderDSL_Attribute75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def appBuilderDSL_Attribute(self):
        return self.__appBuilderDSL_Attribute

    @appBuilderDSL_Attribute.setter
    def appBuilderDSL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Attribute__appBuilderDSL_Attribute", None)
        self.__appBuilderDSL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_EntryParameters24"):
                opp_val = getattr(old_value, "appBuilderDSL_EntryParameters24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_EntryParameters24"):
                opp_val = getattr(value, "appBuilderDSL_EntryParameters24", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_EntryParameters24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Attribute75(self):
        return self.__appBuilderDSL_Attribute75

    @appBuilderDSL_Attribute75.setter
    def appBuilderDSL_Attribute75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Attribute__appBuilderDSL_Attribute75", None)
        self.__appBuilderDSL_Attribute75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Model74"):
                opp_val = getattr(old_value, "appBuilderDSL_Model74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Model74"):
                opp_val = getattr(value, "appBuilderDSL_Model74", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_Model74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Attribute53(self):
        return self.__appBuilderDSL_Attribute53

    @appBuilderDSL_Attribute53.setter
    def appBuilderDSL_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Attribute__appBuilderDSL_Attribute53", None)
        self.__appBuilderDSL_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_SimpleDataBinding"):
                opp_val = getattr(old_value, "appBuilderDSL_SimpleDataBinding", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_SimpleDataBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_SimpleDataBinding"):
                opp_val = getattr(value, "appBuilderDSL_SimpleDataBinding", None)
                setattr(value, "appBuilderDSL_SimpleDataBinding", self)

    @property
    def appBuilderDSL_Attribute64(self):
        return self.__appBuilderDSL_Attribute64

    @appBuilderDSL_Attribute64.setter
    def appBuilderDSL_Attribute64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Attribute__appBuilderDSL_Attribute64", None)
        self.__appBuilderDSL_Attribute64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_SetInstruction"):
                opp_val = getattr(old_value, "appBuilderDSL_SetInstruction", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_SetInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_SetInstruction"):
                opp_val = getattr(value, "appBuilderDSL_SetInstruction", None)
                setattr(value, "appBuilderDSL_SetInstruction", self)

class appBuilderDSL_Controller:

    pass
class appBuilderDSL_View:

    pass
class appBuilderDSL_Model:

    pass
class appBuilderDSL_EntryParameters:

    pass
class Screen:

    pass
class appBuilderDSL_CompositeScreen(Screen):

    pass
class appBuilderDSL_SimpleScreen(Screen):

    pass
class appBuilderDSL_Screen:

    def __init__(self, name: str, appBuilderDSL_Screen: "appBuilderDSL_Ui" = None, appBuilderDSL_Screen15: "appBuilderDSL_Main" = None, appBuilderDSL_Screen68: "appBuilderDSL_Navigate" = None, appBuilderDSL_Screen82: "appBuilderDSL_ScreenLayout" = None):
        self.name = name
        self.appBuilderDSL_Screen = appBuilderDSL_Screen
        self.appBuilderDSL_Screen15 = appBuilderDSL_Screen15
        self.appBuilderDSL_Screen68 = appBuilderDSL_Screen68
        self.appBuilderDSL_Screen82 = appBuilderDSL_Screen82
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_Screen15(self):
        return self.__appBuilderDSL_Screen15

    @appBuilderDSL_Screen15.setter
    def appBuilderDSL_Screen15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Screen__appBuilderDSL_Screen15", None)
        self.__appBuilderDSL_Screen15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Main14"):
                opp_val = getattr(old_value, "appBuilderDSL_Main14", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Main14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Main14"):
                opp_val = getattr(value, "appBuilderDSL_Main14", None)
                setattr(value, "appBuilderDSL_Main14", self)

    @property
    def appBuilderDSL_Screen(self):
        return self.__appBuilderDSL_Screen

    @appBuilderDSL_Screen.setter
    def appBuilderDSL_Screen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Screen__appBuilderDSL_Screen", None)
        self.__appBuilderDSL_Screen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Ui12"):
                opp_val = getattr(old_value, "appBuilderDSL_Ui12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Ui12"):
                opp_val = getattr(value, "appBuilderDSL_Ui12", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_Ui12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def appBuilderDSL_Screen82(self):
        return self.__appBuilderDSL_Screen82

    @appBuilderDSL_Screen82.setter
    def appBuilderDSL_Screen82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Screen__appBuilderDSL_Screen82", None)
        self.__appBuilderDSL_Screen82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_ScreenLayout"):
                opp_val = getattr(old_value, "appBuilderDSL_ScreenLayout", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_ScreenLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_ScreenLayout"):
                opp_val = getattr(value, "appBuilderDSL_ScreenLayout", None)
                setattr(value, "appBuilderDSL_ScreenLayout", self)

    @property
    def appBuilderDSL_Screen68(self):
        return self.__appBuilderDSL_Screen68

    @appBuilderDSL_Screen68.setter
    def appBuilderDSL_Screen68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Screen__appBuilderDSL_Screen68", None)
        self.__appBuilderDSL_Screen68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Navigate"):
                opp_val = getattr(old_value, "appBuilderDSL_Navigate", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Navigate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Navigate"):
                opp_val = getattr(value, "appBuilderDSL_Navigate", None)
                setattr(value, "appBuilderDSL_Navigate", self)

class appBuilderDSL_Main:

    def __init__(self, appName: str, appVersion: str, devices: str, generalStyle: str, appBuilderDSL_Main: "appBuilderDSL_Ui" = None, appBuilderDSL_Main14: "appBuilderDSL_Screen" = None):
        self.appName = appName
        self.appVersion = appVersion
        self.devices = devices
        self.generalStyle = generalStyle
        self.appBuilderDSL_Main = appBuilderDSL_Main
        self.appBuilderDSL_Main14 = appBuilderDSL_Main14
        
    @property
    def generalStyle(self) -> str:
        return self.__generalStyle

    @generalStyle.setter
    def generalStyle(self, generalStyle: str):
        self.__generalStyle = generalStyle

    @property
    def devices(self) -> str:
        return self.__devices

    @devices.setter
    def devices(self, devices: str):
        self.__devices = devices

    @property
    def appVersion(self) -> str:
        return self.__appVersion

    @appVersion.setter
    def appVersion(self, appVersion: str):
        self.__appVersion = appVersion

    @property
    def appName(self) -> str:
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName

    @property
    def appBuilderDSL_Main14(self):
        return self.__appBuilderDSL_Main14

    @appBuilderDSL_Main14.setter
    def appBuilderDSL_Main14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Main__appBuilderDSL_Main14", None)
        self.__appBuilderDSL_Main14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Screen15"):
                opp_val = getattr(old_value, "appBuilderDSL_Screen15", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Screen15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Screen15"):
                opp_val = getattr(value, "appBuilderDSL_Screen15", None)
                setattr(value, "appBuilderDSL_Screen15", self)

    @property
    def appBuilderDSL_Main(self):
        return self.__appBuilderDSL_Main

    @appBuilderDSL_Main.setter
    def appBuilderDSL_Main(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_Main__appBuilderDSL_Main", None)
        self.__appBuilderDSL_Main = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_Ui7"):
                opp_val = getattr(old_value, "appBuilderDSL_Ui7", None)
                if opp_val == self:
                    setattr(old_value, "appBuilderDSL_Ui7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_Ui7"):
                opp_val = getattr(value, "appBuilderDSL_Ui7", None)
                setattr(value, "appBuilderDSL_Ui7", self)

class Service:

    pass
class appBuilderDSL_InstanceService(Service):

    def __init__(self, instanceName: str):
        self.instanceName = instanceName
        
    @property
    def instanceName(self) -> str:
        return self.__instanceName

    @instanceName.setter
    def instanceName(self, instanceName: str):
        self.__instanceName = instanceName

class appBuilderDSL_Service:

    pass
class appBuilderDSL_Ui:

    pass
class appBuilderDSL_Business:

    pass
class AbstractElement:

    pass
class appBuilderDSL_System(AbstractElement):

    pass
class appBuilderDSL_NamespaceDeclation(AbstractElement):

    pass
class appBuilderDSL_AbstractElement:

    def __init__(self, name: str, appBuilderDSL_AbstractElement: "appBuilderDSL_AppBuilder" = None):
        self.name = name
        self.appBuilderDSL_AbstractElement = appBuilderDSL_AbstractElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def appBuilderDSL_AbstractElement(self):
        return self.__appBuilderDSL_AbstractElement

    @appBuilderDSL_AbstractElement.setter
    def appBuilderDSL_AbstractElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appBuilderDSL_AbstractElement__appBuilderDSL_AbstractElement", None)
        self.__appBuilderDSL_AbstractElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appBuilderDSL_AppBuilder"):
                opp_val = getattr(old_value, "appBuilderDSL_AppBuilder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appBuilderDSL_AppBuilder"):
                opp_val = getattr(value, "appBuilderDSL_AppBuilder", None)
                if opp_val is None:
                    setattr(value, "appBuilderDSL_AppBuilder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class appBuilderDSL_AppBuilder:

    pass
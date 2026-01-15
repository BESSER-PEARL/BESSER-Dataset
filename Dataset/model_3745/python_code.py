from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DynamicValueType(Enum):
    LiteralText = "LiteralText"
    ScriptText = "ScriptText"
    VariableName = "VariableName"
    Custom = "Custom"
class InputType(Enum):
    Value = "Value"
    Variable = "Variable"
class DebugLevel(Enum):
    Warn = "Warn"
    Error = "Error"
    Info = "Info"
    Debug = "Debug"
class OutputType(Enum):
    Default = "Default"
    Error = "Error"
    Choice = "Choice"


############################################
# Definition of Classes
############################################

class CallSource1:

    pass
class core_call_CallSource2(CallSource1):

    pass
class SafiCall:

    pass
class core_call_CallSource1(ABC):

    pass
class CallConsumer1:

    pass
class core_call_CallConsumer2(CallConsumer1):

    pass
class core_call_CallConsumer1(ABC):

    pass
class core_initiator_InitiatorInfo(ABC):

    pass
class saflet_core_Variable:

    pass
class Finally:

    pass
class SafletContext:

    pass
class SafletEnvironment:

    pass
class core_scripting_ScriptScopeFactory(ABC):

    pass
class Initiator:

    pass
class SafletScriptEnvironment:

    pass
class core_scripting_RhinoSafletScriptEnvironment(SafletScriptEnvironment):

    pass
class core_scripting_ScriptScope(ABC):

    def __init__(self, scopeObject: str):
        self.scopeObject = scopeObject
        
    @property
    def scopeObject(self) -> str:
        return self.__scopeObject

    @scopeObject.setter
    def scopeObject(self, scopeObject: str):
        self.__scopeObject = scopeObject

    def removeObjectFromScope(self, name: str):
        # TODO: Implement removeObjectFromScope method
        pass

    def getScopedObject(self, name: str) -> str:
        # TODO: Implement getScopedObject method
        pass

    def updateVariablesFromScope(self, safletEnvironment: str, variables: str, isDebug: bool):
        # TODO: Implement updateVariablesFromScope method
        pass

    def exposeObjectToScript(self, value: str, name: str):
        # TODO: Implement exposeObjectToScript method
        pass

class core_scripting_SafletScriptEnvironment(ABC):

    pass
class core_scripting_SafletScript(ABC):

    def __init__(self, name: str, scriptText: str):
        self.name = name
        self.scriptText = scriptText
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scriptText(self) -> str:
        return self.__scriptText

    @scriptText.setter
    def scriptText(self, scriptText: str):
        self.__scriptText = scriptText

    def execute(self, scope: str) -> str:
        # TODO: Implement execute method
        pass

class core_scripting_SafletScriptFactory(ABC):

    def __init__(self, core_scripting_SafletScriptFactory: "SafletScript" = None):
        self.core_scripting_SafletScriptFactory = core_scripting_SafletScriptFactory
        
    @property
    def core_scripting_SafletScriptFactory(self):
        return self.__core_scripting_SafletScriptFactory

    @core_scripting_SafletScriptFactory.setter
    def core_scripting_SafletScriptFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_scripting_SafletScriptFactory__core_scripting_SafletScriptFactory", None)
        self.__core_scripting_SafletScriptFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletScript150"):
                opp_val = getattr(old_value, "SafletScript150", None)
                if opp_val == self:
                    setattr(old_value, "SafletScript150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletScript150"):
                opp_val = getattr(value, "SafletScript150", None)
                setattr(value, "SafletScript150", self)

    def getSafletScript(self, name: str, scriptText: str) -> str:
        # TODO: Implement getSafletScript method
        pass

class ScriptScopeFactory:

    pass
class core_scripting_RhinoScriptScopeFactory(ScriptScopeFactory):

    pass
class SafletScriptFactory:

    pass
class core_scripting_RhinoSafletScriptFactory(SafletScriptFactory):

    pass
class ScriptScope:

    pass
class core_scripting_RhinoScriptScope(ScriptScope):

    pass
class SafletScript:

    pass
class core_scripting_RhinoSafletScript(SafletScript):

    def __init__(self, rhinoScript: str, SafletScript: "core_scripting_SafletScriptEnvironment", SafletScript150: "core_scripting_SafletScriptFactory"):
        self.rhinoScript = rhinoScript
        
    @property
    def rhinoScript(self) -> str:
        return self.__rhinoScript

    @rhinoScript.setter
    def rhinoScript(self, rhinoScript: str):
        self.__rhinoScript = rhinoScript

class core_actionstep_Heavyweight(ABC):

    pass
class QueryParamMapping:

    pass
class core_actionstep_DBQueryParamId:

    def __init__(self, id: str, index: int):
        self.id = id
        self.index = index
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

class SetColMapping:

    pass
class GetColMapping:

    pass
class DBResultSetId:

    pass
class DBQueryParamId:

    pass
class DBQueryId:

    pass
class DBConnectionId:

    pass
class actionstep_Heavyweight:

    pass
class actionstep_ActionStep:

    pass
class core_actionstep_UpdatetRow(actionstep_ActionStep, actionstep_Heavyweight):

    pass
class core_actionstep_ExecuteQuery(actionstep_ActionStep, actionstep_Heavyweight):

    def __init__(self, resultSetName: str, core_actionstep_ExecuteQuery: "DBQueryId" = None, core_actionstep_ExecuteQuery60: "DBResultSetId" = None):
        self.resultSetName = resultSetName
        self.core_actionstep_ExecuteQuery = core_actionstep_ExecuteQuery
        self.core_actionstep_ExecuteQuery60 = core_actionstep_ExecuteQuery60
        
    @property
    def resultSetName(self) -> str:
        return self.__resultSetName

    @resultSetName.setter
    def resultSetName(self, resultSetName: str):
        self.__resultSetName = resultSetName

    @property
    def core_actionstep_ExecuteQuery60(self):
        return self.__core_actionstep_ExecuteQuery60

    @core_actionstep_ExecuteQuery60.setter
    def core_actionstep_ExecuteQuery60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ExecuteQuery__core_actionstep_ExecuteQuery60", None)
        self.__core_actionstep_ExecuteQuery60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBResultSetId"):
                opp_val = getattr(old_value, "DBResultSetId", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId"):
                opp_val = getattr(value, "DBResultSetId", None)
                setattr(value, "DBResultSetId", self)

    @property
    def core_actionstep_ExecuteQuery(self):
        return self.__core_actionstep_ExecuteQuery

    @core_actionstep_ExecuteQuery.setter
    def core_actionstep_ExecuteQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ExecuteQuery__core_actionstep_ExecuteQuery", None)
        self.__core_actionstep_ExecuteQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId58"):
                opp_val = getattr(old_value, "DBQueryId58", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId58"):
                opp_val = getattr(value, "DBQueryId58", None)
                setattr(value, "DBQueryId58", self)

class core_actionstep_RunQuery(actionstep_ActionStep, actionstep_Heavyweight):

    def __init__(self, resultSetName: str, scrollable: bool, readOnly: bool, core_actionstep_RunQuery119: "DBQueryId" = None, core_actionstep_RunQuery: "DBConnectionId" = None, core_actionstep_RunQuery130: "DynamicValue" = None, core_actionstep_RunQuery122: set["QueryParamMapping"] = None, core_actionstep_RunQuery124: "DBResultSetId" = None, core_actionstep_RunQuery127: "DynamicValue" = None):
        self.resultSetName = resultSetName
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.core_actionstep_RunQuery119 = core_actionstep_RunQuery119
        self.core_actionstep_RunQuery = core_actionstep_RunQuery
        self.core_actionstep_RunQuery130 = core_actionstep_RunQuery130
        self.core_actionstep_RunQuery122 = core_actionstep_RunQuery122 if core_actionstep_RunQuery122 is not None else set()
        self.core_actionstep_RunQuery124 = core_actionstep_RunQuery124
        self.core_actionstep_RunQuery127 = core_actionstep_RunQuery127
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def scrollable(self) -> bool:
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable

    @property
    def resultSetName(self) -> str:
        return self.__resultSetName

    @resultSetName.setter
    def resultSetName(self, resultSetName: str):
        self.__resultSetName = resultSetName

    @property
    def core_actionstep_RunQuery124(self):
        return self.__core_actionstep_RunQuery124

    @core_actionstep_RunQuery124.setter
    def core_actionstep_RunQuery124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery124", None)
        self.__core_actionstep_RunQuery124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBResultSetId125"):
                opp_val = getattr(old_value, "DBResultSetId125", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId125"):
                opp_val = getattr(value, "DBResultSetId125", None)
                setattr(value, "DBResultSetId125", self)

    @property
    def core_actionstep_RunQuery(self):
        return self.__core_actionstep_RunQuery

    @core_actionstep_RunQuery.setter
    def core_actionstep_RunQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery", None)
        self.__core_actionstep_RunQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBConnectionId117"):
                opp_val = getattr(old_value, "DBConnectionId117", None)
                if opp_val == self:
                    setattr(old_value, "DBConnectionId117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBConnectionId117"):
                opp_val = getattr(value, "DBConnectionId117", None)
                setattr(value, "DBConnectionId117", self)

    @property
    def core_actionstep_RunQuery127(self):
        return self.__core_actionstep_RunQuery127

    @core_actionstep_RunQuery127.setter
    def core_actionstep_RunQuery127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery127", None)
        self.__core_actionstep_RunQuery127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue128"):
                opp_val = getattr(old_value, "DynamicValue128", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue128"):
                opp_val = getattr(value, "DynamicValue128", None)
                setattr(value, "DynamicValue128", self)

    @property
    def core_actionstep_RunQuery122(self):
        return self.__core_actionstep_RunQuery122

    @core_actionstep_RunQuery122.setter
    def core_actionstep_RunQuery122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery122", None)
        self.__core_actionstep_RunQuery122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryParamMapping"):
                    opp_val = getattr(item, "QueryParamMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryParamMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryParamMapping"):
                    opp_val = getattr(item, "QueryParamMapping", None)
                    
                    setattr(item, "QueryParamMapping", self)
                    

    @property
    def core_actionstep_RunQuery119(self):
        return self.__core_actionstep_RunQuery119

    @core_actionstep_RunQuery119.setter
    def core_actionstep_RunQuery119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery119", None)
        self.__core_actionstep_RunQuery119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId120"):
                opp_val = getattr(old_value, "DBQueryId120", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId120"):
                opp_val = getattr(value, "DBQueryId120", None)
                setattr(value, "DBQueryId120", self)

    @property
    def core_actionstep_RunQuery130(self):
        return self.__core_actionstep_RunQuery130

    @core_actionstep_RunQuery130.setter
    def core_actionstep_RunQuery130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery130", None)
        self.__core_actionstep_RunQuery130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue131"):
                opp_val = getattr(old_value, "DynamicValue131", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue131"):
                opp_val = getattr(value, "DynamicValue131", None)
                setattr(value, "DynamicValue131", self)

    def refreshParams(self, qry: str):
        # TODO: Implement refreshParams method
        pass

class core_actionstep_OpenDBConnection(actionstep_ActionStep, actionstep_Heavyweight):

    pass
class actionstep_core_EStringToStringMapEntry:

    pass
class actionstep_core_EObject:

    pass
class core_actionstep_Output:

    def __init__(self, name: str, outputType: str, core_actionstep_Output: "ActionStep" = None, ActionStep27: "ActionStep" = None):
        self.name = name
        self.outputType = outputType
        self.core_actionstep_Output = core_actionstep_Output
        self.ActionStep27 = ActionStep27
        
    @property
    def outputType(self) -> str:
        return self.__outputType

    @outputType.setter
    def outputType(self, outputType: str):
        self.__outputType = outputType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def core_actionstep_Output(self):
        return self.__core_actionstep_Output

    @core_actionstep_Output.setter
    def core_actionstep_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Output__core_actionstep_Output", None)
        self.__core_actionstep_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionStep"):
                opp_val = getattr(old_value, "ActionStep", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep"):
                opp_val = getattr(value, "ActionStep", None)
                setattr(value, "ActionStep", self)

    @property
    def ActionStep27(self):
        return self.__ActionStep27

    @ActionStep27.setter
    def ActionStep27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Output__ActionStep27", None)
        self.__ActionStep27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actionstep28"):
                opp_val = getattr(old_value, "actionstep28", None)
                if opp_val == self:
                    setattr(old_value, "actionstep28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actionstep28"):
                opp_val = getattr(value, "actionstep28", None)
                setattr(value, "actionstep28", self)

class actionstep_ParameterizedActionstep:

    pass
class initiator_Initiator:

    pass
class core_actionstep_ParameterizedInitiator(initiator_Initiator, actionstep_ParameterizedActionstep):

    def __init__(self):
        
    def getOutputMap(self):
        # TODO: Implement getOutputMap method
        pass

class OutputParameter:

    pass
class InputItem:

    pass
class core_actionstep_OutputParameter(InputItem):

    pass
class CaseItem:

    pass
class core_actionstep_InputItem(CaseItem):

    def __init__(self, parameterName: str, required: bool, CaseItem: "core_actionstep_Choice"):
        self.parameterName = parameterName
        self.required = required
        
    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

class Item:

    pass
class core_actionstep_GetColMapping(Item):

    def __init__(self, getAsDatatype: str, core_actionstep_GetColMapping: "DynamicValue" = None, core_actionstep_GetColMapping109: "DynamicValue" = None):
        self.getAsDatatype = getAsDatatype
        self.core_actionstep_GetColMapping = core_actionstep_GetColMapping
        self.core_actionstep_GetColMapping109 = core_actionstep_GetColMapping109
        
    @property
    def getAsDatatype(self) -> str:
        return self.__getAsDatatype

    @getAsDatatype.setter
    def getAsDatatype(self, getAsDatatype: str):
        self.__getAsDatatype = getAsDatatype

    @property
    def core_actionstep_GetColMapping109(self):
        return self.__core_actionstep_GetColMapping109

    @core_actionstep_GetColMapping109.setter
    def core_actionstep_GetColMapping109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColMapping__core_actionstep_GetColMapping109", None)
        self.__core_actionstep_GetColMapping109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue110"):
                opp_val = getattr(old_value, "DynamicValue110", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue110"):
                opp_val = getattr(value, "DynamicValue110", None)
                setattr(value, "DynamicValue110", self)

    @property
    def core_actionstep_GetColMapping(self):
        return self.__core_actionstep_GetColMapping

    @core_actionstep_GetColMapping.setter
    def core_actionstep_GetColMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColMapping__core_actionstep_GetColMapping", None)
        self.__core_actionstep_GetColMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue107"):
                opp_val = getattr(old_value, "DynamicValue107", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue107"):
                opp_val = getattr(value, "DynamicValue107", None)
                setattr(value, "DynamicValue107", self)

class core_actionstep_QueryParamMapping(Item):

    def __init__(self, setAsDatatype: str, core_actionstep_QueryParamMapping: "DBQueryParamId" = None, core_actionstep_QueryParamMapping135: "DynamicValue" = None):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_QueryParamMapping = core_actionstep_QueryParamMapping
        self.core_actionstep_QueryParamMapping135 = core_actionstep_QueryParamMapping135
        
    @property
    def setAsDatatype(self) -> str:
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype

    @property
    def core_actionstep_QueryParamMapping135(self):
        return self.__core_actionstep_QueryParamMapping135

    @core_actionstep_QueryParamMapping135.setter
    def core_actionstep_QueryParamMapping135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_QueryParamMapping__core_actionstep_QueryParamMapping135", None)
        self.__core_actionstep_QueryParamMapping135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue136"):
                opp_val = getattr(old_value, "DynamicValue136", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue136"):
                opp_val = getattr(value, "DynamicValue136", None)
                setattr(value, "DynamicValue136", self)

    @property
    def core_actionstep_QueryParamMapping(self):
        return self.__core_actionstep_QueryParamMapping

    @core_actionstep_QueryParamMapping.setter
    def core_actionstep_QueryParamMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_QueryParamMapping__core_actionstep_QueryParamMapping", None)
        self.__core_actionstep_QueryParamMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryParamId133"):
                opp_val = getattr(old_value, "DBQueryParamId133", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryParamId133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryParamId133"):
                opp_val = getattr(value, "DBQueryParamId133", None)
                setattr(value, "DBQueryParamId133", self)

class core_actionstep_SetColMapping(Item):

    def __init__(self, setAsDatatype: str, core_actionstep_SetColMapping: "DynamicValue" = None, core_actionstep_SetColMapping114: "DynamicValue" = None):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_SetColMapping = core_actionstep_SetColMapping
        self.core_actionstep_SetColMapping114 = core_actionstep_SetColMapping114
        
    @property
    def setAsDatatype(self) -> str:
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype

    @property
    def core_actionstep_SetColMapping114(self):
        return self.__core_actionstep_SetColMapping114

    @core_actionstep_SetColMapping114.setter
    def core_actionstep_SetColMapping114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColMapping__core_actionstep_SetColMapping114", None)
        self.__core_actionstep_SetColMapping114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue115"):
                opp_val = getattr(old_value, "DynamicValue115", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue115"):
                opp_val = getattr(value, "DynamicValue115", None)
                setattr(value, "DynamicValue115", self)

    @property
    def core_actionstep_SetColMapping(self):
        return self.__core_actionstep_SetColMapping

    @core_actionstep_SetColMapping.setter
    def core_actionstep_SetColMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColMapping__core_actionstep_SetColMapping", None)
        self.__core_actionstep_SetColMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue112"):
                opp_val = getattr(old_value, "DynamicValue112", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue112"):
                opp_val = getattr(value, "DynamicValue112", None)
                setattr(value, "DynamicValue112", self)

class core_actionstep_CaseItem(Item):

    pass
class DynamicValue:

    pass
class ActionStep:

    pass
class core_initiator_Initiator(ActionStep):

    def __init__(self, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        
    def beginProcessing(self):
        # TODO: Implement beginProcessing method
        pass

    def initialize(self, context: str):
        # TODO: Implement initialize method
        pass

    def acceptsRequest(self, context: str) -> bool:
        # TODO: Implement acceptsRequest method
        pass

class core_actionstep_SetColValues(ActionStep):

    pass
class core_actionstep_DebugLog(ActionStep):

    def __init__(self, debugLevel: str, core_actionstep_DebugLog: "DynamicValue" = None, core_actionstep_DebugLog36: "DynamicValue" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.debugLevel = debugLevel
        self.core_actionstep_DebugLog = core_actionstep_DebugLog
        self.core_actionstep_DebugLog36 = core_actionstep_DebugLog36
        
    @property
    def debugLevel(self) -> str:
        return self.__debugLevel

    @debugLevel.setter
    def debugLevel(self, debugLevel: str):
        self.__debugLevel = debugLevel

    @property
    def core_actionstep_DebugLog36(self):
        return self.__core_actionstep_DebugLog36

    @core_actionstep_DebugLog36.setter
    def core_actionstep_DebugLog36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_DebugLog__core_actionstep_DebugLog36", None)
        self.__core_actionstep_DebugLog36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue37"):
                opp_val = getattr(old_value, "DynamicValue37", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue37"):
                opp_val = getattr(value, "DynamicValue37", None)
                setattr(value, "DynamicValue37", self)

    @property
    def core_actionstep_DebugLog(self):
        return self.__core_actionstep_DebugLog

    @core_actionstep_DebugLog.setter
    def core_actionstep_DebugLog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_DebugLog__core_actionstep_DebugLog", None)
        self.__core_actionstep_DebugLog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue34"):
                opp_val = getattr(old_value, "DynamicValue34", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue34"):
                opp_val = getattr(value, "DynamicValue34", None)
                setattr(value, "DynamicValue34", self)

class core_actionstep_SetColValue(ActionStep):

    def __init__(self, setAsDatatype: str, core_actionstep_SetColValue81: "DynamicValue" = None, core_actionstep_SetColValue: "DBResultSetId" = None, core_actionstep_SetColValue78: "DynamicValue" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_SetColValue81 = core_actionstep_SetColValue81
        self.core_actionstep_SetColValue = core_actionstep_SetColValue
        self.core_actionstep_SetColValue78 = core_actionstep_SetColValue78
        
    @property
    def setAsDatatype(self) -> str:
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype

    @property
    def core_actionstep_SetColValue78(self):
        return self.__core_actionstep_SetColValue78

    @core_actionstep_SetColValue78.setter
    def core_actionstep_SetColValue78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColValue__core_actionstep_SetColValue78", None)
        self.__core_actionstep_SetColValue78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue79"):
                opp_val = getattr(old_value, "DynamicValue79", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue79"):
                opp_val = getattr(value, "DynamicValue79", None)
                setattr(value, "DynamicValue79", self)

    @property
    def core_actionstep_SetColValue(self):
        return self.__core_actionstep_SetColValue

    @core_actionstep_SetColValue.setter
    def core_actionstep_SetColValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColValue__core_actionstep_SetColValue", None)
        self.__core_actionstep_SetColValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBResultSetId76"):
                opp_val = getattr(old_value, "DBResultSetId76", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId76"):
                opp_val = getattr(value, "DBResultSetId76", None)
                setattr(value, "DBResultSetId76", self)

    @property
    def core_actionstep_SetColValue81(self):
        return self.__core_actionstep_SetColValue81

    @core_actionstep_SetColValue81.setter
    def core_actionstep_SetColValue81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColValue__core_actionstep_SetColValue81", None)
        self.__core_actionstep_SetColValue81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue82"):
                opp_val = getattr(old_value, "DynamicValue82", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue82"):
                opp_val = getattr(value, "DynamicValue82", None)
                setattr(value, "DynamicValue82", self)

class core_actionstep_MoveToFirstRow(ActionStep):

    pass
class core_actionstep_GetColValues(ActionStep):

    pass
class core_actionstep_OpenQuery(ActionStep):

    def __init__(self, useCache: bool, scrollable: bool, readOnly: bool, scrollMode: str, holdabilityMode: str, core_actionstep_OpenQuery43: "DBConnectionId" = None, core_actionstep_OpenQuery: "DBQueryId" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.useCache = useCache
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.scrollMode = scrollMode
        self.holdabilityMode = holdabilityMode
        self.core_actionstep_OpenQuery43 = core_actionstep_OpenQuery43
        self.core_actionstep_OpenQuery = core_actionstep_OpenQuery
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def useCache(self) -> bool:
        return self.__useCache

    @useCache.setter
    def useCache(self, useCache: bool):
        self.__useCache = useCache

    @property
    def scrollable(self) -> bool:
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable

    @property
    def scrollMode(self) -> str:
        return self.__scrollMode

    @scrollMode.setter
    def scrollMode(self, scrollMode: str):
        self.__scrollMode = scrollMode

    @property
    def holdabilityMode(self) -> str:
        return self.__holdabilityMode

    @holdabilityMode.setter
    def holdabilityMode(self, holdabilityMode: str):
        self.__holdabilityMode = holdabilityMode

    @property
    def core_actionstep_OpenQuery43(self):
        return self.__core_actionstep_OpenQuery43

    @core_actionstep_OpenQuery43.setter
    def core_actionstep_OpenQuery43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_OpenQuery__core_actionstep_OpenQuery43", None)
        self.__core_actionstep_OpenQuery43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBConnectionId44"):
                opp_val = getattr(old_value, "DBConnectionId44", None)
                if opp_val == self:
                    setattr(old_value, "DBConnectionId44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBConnectionId44"):
                opp_val = getattr(value, "DBConnectionId44", None)
                setattr(value, "DBConnectionId44", self)

    @property
    def core_actionstep_OpenQuery(self):
        return self.__core_actionstep_OpenQuery

    @core_actionstep_OpenQuery.setter
    def core_actionstep_OpenQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_OpenQuery__core_actionstep_OpenQuery", None)
        self.__core_actionstep_OpenQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId"):
                opp_val = getattr(old_value, "DBQueryId", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId"):
                opp_val = getattr(value, "DBQueryId", None)
                setattr(value, "DBQueryId", self)

class core_actionstep_InsertRow(ActionStep):

    pass
class core_actionstep_InvokeSaflet(ActionStep):

    def __init__(self, labelText: str, core_actionstep_InvokeSaflet: "DynamicValue" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.labelText = labelText
        self.core_actionstep_InvokeSaflet = core_actionstep_InvokeSaflet
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def core_actionstep_InvokeSaflet(self):
        return self.__core_actionstep_InvokeSaflet

    @core_actionstep_InvokeSaflet.setter
    def core_actionstep_InvokeSaflet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_InvokeSaflet__core_actionstep_InvokeSaflet", None)
        self.__core_actionstep_InvokeSaflet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue32"):
                opp_val = getattr(old_value, "DynamicValue32", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue32"):
                opp_val = getattr(value, "DynamicValue32", None)
                setattr(value, "DynamicValue32", self)

class core_actionstep_Finally(ActionStep):

    pass
class core_actionstep_GetColValue(ActionStep):

    def __init__(self, getAsDatatype: str, core_actionstep_GetColValue66: "DynamicValue" = None, core_actionstep_GetColValue: "DBResultSetId" = None, core_actionstep_GetColValue69: "DynamicValue" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.getAsDatatype = getAsDatatype
        self.core_actionstep_GetColValue66 = core_actionstep_GetColValue66
        self.core_actionstep_GetColValue = core_actionstep_GetColValue
        self.core_actionstep_GetColValue69 = core_actionstep_GetColValue69
        
    @property
    def getAsDatatype(self) -> str:
        return self.__getAsDatatype

    @getAsDatatype.setter
    def getAsDatatype(self, getAsDatatype: str):
        self.__getAsDatatype = getAsDatatype

    @property
    def core_actionstep_GetColValue66(self):
        return self.__core_actionstep_GetColValue66

    @core_actionstep_GetColValue66.setter
    def core_actionstep_GetColValue66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColValue__core_actionstep_GetColValue66", None)
        self.__core_actionstep_GetColValue66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue67"):
                opp_val = getattr(old_value, "DynamicValue67", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue67"):
                opp_val = getattr(value, "DynamicValue67", None)
                setattr(value, "DynamicValue67", self)

    @property
    def core_actionstep_GetColValue(self):
        return self.__core_actionstep_GetColValue

    @core_actionstep_GetColValue.setter
    def core_actionstep_GetColValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColValue__core_actionstep_GetColValue", None)
        self.__core_actionstep_GetColValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBResultSetId64"):
                opp_val = getattr(old_value, "DBResultSetId64", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId64"):
                opp_val = getattr(value, "DBResultSetId64", None)
                setattr(value, "DBResultSetId64", self)

    @property
    def core_actionstep_GetColValue69(self):
        return self.__core_actionstep_GetColValue69

    @core_actionstep_GetColValue69.setter
    def core_actionstep_GetColValue69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColValue__core_actionstep_GetColValue69", None)
        self.__core_actionstep_GetColValue69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue70"):
                opp_val = getattr(old_value, "DynamicValue70", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue70"):
                opp_val = getattr(value, "DynamicValue70", None)
                setattr(value, "DynamicValue70", self)

class core_actionstep_IfThen(ActionStep):

    pass
class core_actionstep_MoveToLastRow(ActionStep):

    pass
class core_actionstep_NextRow(ActionStep):

    pass
class core_actionstep_MoveToRow(ActionStep):

    pass
class core_actionstep_ExecuteScript(ActionStep):

    pass
class core_actionstep_ParameterizedActionstep(ActionStep):

    pass
class core_actionstep_PreviousRow(ActionStep):

    pass
class core_actionstep_SetQueryParam(ActionStep):

    def __init__(self, paramDatatype: str, core_actionstep_SetQueryParam: "DynamicValue" = None, core_actionstep_SetQueryParam48: "DBQueryParamId" = None, core_actionstep_SetQueryParam50: "DBQueryId" = None, actionstep164: "core_saflet_Saflet", actionstep28: "core_actionstep_Output", ActionStep141: "core_actionstep_Item", ActionStep138: "core_actionstep_Item", ActionStep: "core_actionstep_Output"):
        self.paramDatatype = paramDatatype
        self.core_actionstep_SetQueryParam = core_actionstep_SetQueryParam
        self.core_actionstep_SetQueryParam48 = core_actionstep_SetQueryParam48
        self.core_actionstep_SetQueryParam50 = core_actionstep_SetQueryParam50
        
    @property
    def paramDatatype(self) -> str:
        return self.__paramDatatype

    @paramDatatype.setter
    def paramDatatype(self, paramDatatype: str):
        self.__paramDatatype = paramDatatype

    @property
    def core_actionstep_SetQueryParam50(self):
        return self.__core_actionstep_SetQueryParam50

    @core_actionstep_SetQueryParam50.setter
    def core_actionstep_SetQueryParam50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetQueryParam__core_actionstep_SetQueryParam50", None)
        self.__core_actionstep_SetQueryParam50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId51"):
                opp_val = getattr(old_value, "DBQueryId51", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId51"):
                opp_val = getattr(value, "DBQueryId51", None)
                setattr(value, "DBQueryId51", self)

    @property
    def core_actionstep_SetQueryParam48(self):
        return self.__core_actionstep_SetQueryParam48

    @core_actionstep_SetQueryParam48.setter
    def core_actionstep_SetQueryParam48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetQueryParam__core_actionstep_SetQueryParam48", None)
        self.__core_actionstep_SetQueryParam48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryParamId"):
                opp_val = getattr(old_value, "DBQueryParamId", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryParamId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryParamId"):
                opp_val = getattr(value, "DBQueryParamId", None)
                setattr(value, "DBQueryParamId", self)

    @property
    def core_actionstep_SetQueryParam(self):
        return self.__core_actionstep_SetQueryParam

    @core_actionstep_SetQueryParam.setter
    def core_actionstep_SetQueryParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetQueryParam__core_actionstep_SetQueryParam", None)
        self.__core_actionstep_SetQueryParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue46"):
                opp_val = getattr(old_value, "DynamicValue46", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue46"):
                opp_val = getattr(value, "DynamicValue46", None)
                setattr(value, "DynamicValue46", self)

class core_actionstep_CloseDBConnection(ActionStep):

    pass
class core_actionstep_ExecuteUpdate(ActionStep):

    pass
class core_actionstep_Choice(ActionStep):

    pass
class core_actionstep_MoveToInsertRow(ActionStep):

    pass
class core_actionstep_DeleteRow(ActionStep):

    pass
class core_actionstep_Assignment(ActionStep):

    pass
class Saflet:

    pass
class Output:

    pass
class core_PlatformDisposition(ABC):

    def __init__(self, platformID: str, platformDependant: bool):
        self.platformID = platformID
        self.platformDependant = platformDependant
        
    @property
    def platformID(self) -> str:
        return self.__platformID

    @platformID.setter
    def platformID(self, platformID: str):
        self.__platformID = platformID

    @property
    def platformDependant(self) -> bool:
        return self.__platformDependant

    @platformDependant.setter
    def platformDependant(self, platformDependant: bool):
        self.__platformDependant = platformDependant

class core_ThreadSensitive:

    def __init__(self):
        
    def cleanup(self):
        # TODO: Implement cleanup method
        pass

class core_ProductIdentifiable(ABC):

    def __init__(self, productId: str):
        self.productId = productId
        
    @property
    def productId(self) -> str:
        return self.__productId

    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId

class PlatformDisposition:

    pass
class ThreadSensitive:

    pass
class core_saflet_SafletContext(ThreadSensitive):

    def __init__(self, sessionVariables: str, exceptions: str, core_saflet_SafletContext174: set["saflet_core_Variable"] = None, core_saflet_SafletContext: "Saflet" = None):
        self.sessionVariables = sessionVariables
        self.exceptions = exceptions
        self.core_saflet_SafletContext174 = core_saflet_SafletContext174 if core_saflet_SafletContext174 is not None else set()
        self.core_saflet_SafletContext = core_saflet_SafletContext
        
    @property
    def exceptions(self) -> str:
        return self.__exceptions

    @exceptions.setter
    def exceptions(self, exceptions: str):
        self.__exceptions = exceptions

    @property
    def sessionVariables(self) -> str:
        return self.__sessionVariables

    @sessionVariables.setter
    def sessionVariables(self, sessionVariables: str):
        self.__sessionVariables = sessionVariables

    @property
    def core_saflet_SafletContext(self):
        return self.__core_saflet_SafletContext

    @core_saflet_SafletContext.setter
    def core_saflet_SafletContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_SafletContext__core_saflet_SafletContext", None)
        self.__core_saflet_SafletContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Saflet172"):
                opp_val = getattr(old_value, "Saflet172", None)
                if opp_val == self:
                    setattr(old_value, "Saflet172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Saflet172"):
                opp_val = getattr(value, "Saflet172", None)
                setattr(value, "Saflet172", self)

    @property
    def core_saflet_SafletContext174(self):
        return self.__core_saflet_SafletContext174

    @core_saflet_SafletContext174.setter
    def core_saflet_SafletContext174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_SafletContext__core_saflet_SafletContext174", None)
        self.__core_saflet_SafletContext174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "saflet_core_Variable"):
                    opp_val = getattr(item, "saflet_core_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "saflet_core_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "saflet_core_Variable"):
                    opp_val = getattr(item, "saflet_core_Variable", None)
                    
                    setattr(item, "saflet_core_Variable", self)
                    

    def getVariable(self, name: str) -> str:
        # TODO: Implement getVariable method
        pass

    def removeVariable(self, name: str) -> str:
        # TODO: Implement removeVariable method
        pass

    def merge(self, context: str):
        # TODO: Implement merge method
        pass

    def preHandoffPrep(self, call: str):
        # TODO: Implement preHandoffPrep method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def setSessionVar(self, name: str, value: str):
        # TODO: Implement setSessionVar method
        pass

    def getVariableRawValue(self, name: str) -> str:
        # TODO: Implement getVariableRawValue method
        pass

    def getSessionVar(self, name: str) -> str:
        # TODO: Implement getSessionVar method
        pass

    def addOrUpdateVariable(self, v: str):
        # TODO: Implement addOrUpdateVariable method
        pass

    def addException(self, e: str):
        # TODO: Implement addException method
        pass

    def setVariableRawValue(self, value: str, name: str):
        # TODO: Implement setVariableRawValue method
        pass

class core_actionstep_DBQueryId(ThreadSensitive):

    def __init__(self, id: str, jdbcStatement: str):
        self.id = id
        self.jdbcStatement = jdbcStatement
        
    @property
    def jdbcStatement(self) -> str:
        return self.__jdbcStatement

    @jdbcStatement.setter
    def jdbcStatement(self, jdbcStatement: str):
        self.__jdbcStatement = jdbcStatement

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class core_call_SafiCall(PlatformDisposition, ThreadSensitive):

    def __init__(self, uuid: str, name: str):
        self.uuid = uuid
        self.name = name
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class core_actionstep_DynamicValue(ThreadSensitive):

    def __init__(self, text: str, type: str, core_actionstep_DynamicValue: "actionstep_core_EObject" = None, core_actionstep_DynamicValue22: set["actionstep_core_EStringToStringMapEntry"] = None):
        self.text = text
        self.type = type
        self.core_actionstep_DynamicValue = core_actionstep_DynamicValue
        self.core_actionstep_DynamicValue22 = core_actionstep_DynamicValue22 if core_actionstep_DynamicValue22 is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def core_actionstep_DynamicValue22(self):
        return self.__core_actionstep_DynamicValue22

    @core_actionstep_DynamicValue22.setter
    def core_actionstep_DynamicValue22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_DynamicValue__core_actionstep_DynamicValue22", None)
        self.__core_actionstep_DynamicValue22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actionstep_core_EStringToStringMapEntry"):
                    opp_val = getattr(item, "actionstep_core_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "actionstep_core_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actionstep_core_EStringToStringMapEntry"):
                    opp_val = getattr(item, "actionstep_core_EStringToStringMapEntry", None)
                    
                    setattr(item, "actionstep_core_EStringToStringMapEntry", self)
                    

    @property
    def core_actionstep_DynamicValue(self):
        return self.__core_actionstep_DynamicValue

    @core_actionstep_DynamicValue.setter
    def core_actionstep_DynamicValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_DynamicValue__core_actionstep_DynamicValue", None)
        self.__core_actionstep_DynamicValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actionstep_core_EObject"):
                opp_val = getattr(old_value, "actionstep_core_EObject", None)
                if opp_val == self:
                    setattr(old_value, "actionstep_core_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actionstep_core_EObject"):
                opp_val = getattr(value, "actionstep_core_EObject", None)
                setattr(value, "actionstep_core_EObject", self)

class core_actionstep_Item(ThreadSensitive):

    def __init__(self, labelText: str, core_actionstep_Item: "ActionStep" = None, core_actionstep_Item140: "ActionStep" = None):
        self.labelText = labelText
        self.core_actionstep_Item = core_actionstep_Item
        self.core_actionstep_Item140 = core_actionstep_Item140
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def core_actionstep_Item(self):
        return self.__core_actionstep_Item

    @core_actionstep_Item.setter
    def core_actionstep_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Item__core_actionstep_Item", None)
        self.__core_actionstep_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionStep138"):
                opp_val = getattr(old_value, "ActionStep138", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep138"):
                opp_val = getattr(value, "ActionStep138", None)
                setattr(value, "ActionStep138", self)

    @property
    def core_actionstep_Item140(self):
        return self.__core_actionstep_Item140

    @core_actionstep_Item140.setter
    def core_actionstep_Item140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Item__core_actionstep_Item140", None)
        self.__core_actionstep_Item140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionStep141"):
                opp_val = getattr(old_value, "ActionStep141", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep141"):
                opp_val = getattr(value, "ActionStep141", None)
                setattr(value, "ActionStep141", self)

class core_actionstep_DBResultSetId(ThreadSensitive):

    def __init__(self, name: str, id: str, jDBCResultSet: str):
        self.name = name
        self.id = id
        self.jDBCResultSet = jDBCResultSet
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jDBCResultSet(self) -> str:
        return self.__jDBCResultSet

    @jDBCResultSet.setter
    def jDBCResultSet(self, jDBCResultSet: str):
        self.__jDBCResultSet = jDBCResultSet

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class core_saflet_SafletEnvironment(ThreadSensitive):

    def __init__(self):
        
    def setGlobalVariableValue(self, name: str, value: str):
        # TODO: Implement setGlobalVariableValue method
        pass

    def getSaflet(self, path: str, coreServerId: int) -> str:
        # TODO: Implement getSaflet method
        pass

    def getGlobalVariableValue(self, name: str) -> str:
        # TODO: Implement getGlobalVariableValue method
        pass

    def getGlobalVariable(self, name: str) -> str:
        # TODO: Implement getGlobalVariable method
        pass

    def getGlobalExecutor(self) -> str:
        # TODO: Implement getGlobalExecutor method
        pass

class core_saflet_Saflet(PlatformDisposition, ThreadSensitive):

    def __init__(self, version: str, description: str, id: int, active: bool, name: str, core_saflet_Saflet: "Initiator" = None, core_saflet_Saflet160: "ScriptScope" = None, ActionStep163: set["ActionStep"] = None, core_saflet_Saflet166: "SafletScriptEnvironment" = None, core_saflet_Saflet168: "SafletEnvironment" = None, core_saflet_Saflet158: "SafletContext" = None, core_saflet_Saflet170: "Finally" = None):
        self.version = version
        self.description = description
        self.id = id
        self.active = active
        self.name = name
        self.core_saflet_Saflet = core_saflet_Saflet
        self.core_saflet_Saflet160 = core_saflet_Saflet160
        self.ActionStep163 = ActionStep163 if ActionStep163 is not None else set()
        self.core_saflet_Saflet166 = core_saflet_Saflet166
        self.core_saflet_Saflet168 = core_saflet_Saflet168
        self.core_saflet_Saflet158 = core_saflet_Saflet158
        self.core_saflet_Saflet170 = core_saflet_Saflet170
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

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
    def core_saflet_Saflet158(self):
        return self.__core_saflet_Saflet158

    @core_saflet_Saflet158.setter
    def core_saflet_Saflet158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet158", None)
        self.__core_saflet_Saflet158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletContext"):
                opp_val = getattr(old_value, "SafletContext", None)
                if opp_val == self:
                    setattr(old_value, "SafletContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletContext"):
                opp_val = getattr(value, "SafletContext", None)
                setattr(value, "SafletContext", self)

    @property
    def core_saflet_Saflet166(self):
        return self.__core_saflet_Saflet166

    @core_saflet_Saflet166.setter
    def core_saflet_Saflet166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet166", None)
        self.__core_saflet_Saflet166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletScriptEnvironment"):
                opp_val = getattr(old_value, "SafletScriptEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "SafletScriptEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletScriptEnvironment"):
                opp_val = getattr(value, "SafletScriptEnvironment", None)
                setattr(value, "SafletScriptEnvironment", self)

    @property
    def core_saflet_Saflet168(self):
        return self.__core_saflet_Saflet168

    @core_saflet_Saflet168.setter
    def core_saflet_Saflet168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet168", None)
        self.__core_saflet_Saflet168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SafletEnvironment"):
                opp_val = getattr(old_value, "SafletEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "SafletEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletEnvironment"):
                opp_val = getattr(value, "SafletEnvironment", None)
                setattr(value, "SafletEnvironment", self)

    @property
    def core_saflet_Saflet(self):
        return self.__core_saflet_Saflet

    @core_saflet_Saflet.setter
    def core_saflet_Saflet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet", None)
        self.__core_saflet_Saflet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Initiator"):
                opp_val = getattr(old_value, "Initiator", None)
                if opp_val == self:
                    setattr(old_value, "Initiator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Initiator"):
                opp_val = getattr(value, "Initiator", None)
                setattr(value, "Initiator", self)

    @property
    def core_saflet_Saflet160(self):
        return self.__core_saflet_Saflet160

    @core_saflet_Saflet160.setter
    def core_saflet_Saflet160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet160", None)
        self.__core_saflet_Saflet160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptScope161"):
                opp_val = getattr(old_value, "ScriptScope161", None)
                if opp_val == self:
                    setattr(old_value, "ScriptScope161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptScope161"):
                opp_val = getattr(value, "ScriptScope161", None)
                setattr(value, "ScriptScope161", self)

    @property
    def ActionStep163(self):
        return self.__ActionStep163

    @ActionStep163.setter
    def ActionStep163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__ActionStep163", None)
        self.__ActionStep163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actionstep164"):
                    opp_val = getattr(item, "actionstep164", None)
                    
                    if opp_val == self:
                        setattr(item, "actionstep164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actionstep164"):
                    opp_val = getattr(item, "actionstep164", None)
                    
                    setattr(item, "actionstep164", self)
                    

    @property
    def core_saflet_Saflet170(self):
        return self.__core_saflet_Saflet170

    @core_saflet_Saflet170.setter
    def core_saflet_Saflet170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet170", None)
        self.__core_saflet_Saflet170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Finally"):
                opp_val = getattr(old_value, "Finally", None)
                if opp_val == self:
                    setattr(old_value, "Finally", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Finally"):
                opp_val = getattr(value, "Finally", None)
                setattr(value, "Finally", self)

    def getActionStep(self, name: str) -> str:
        # TODO: Implement getActionStep method
        pass

    def addActionStep(self, actionstep: str):
        # TODO: Implement addActionStep method
        pass

    def initializeScriptableObjects(self):
        # TODO: Implement initializeScriptableObjects method
        pass

    def getScript(self, name: str) -> str:
        # TODO: Implement getScript method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def addScript(self, scriptText: str, name: str) -> str:
        # TODO: Implement addScript method
        pass

class core_actionstep_DBConnectionId(ThreadSensitive):

    def __init__(self, id: str, jdbcConnection: str):
        self.id = id
        self.jdbcConnection = jdbcConnection
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jdbcConnection(self) -> str:
        return self.__jdbcConnection

    @jdbcConnection.setter
    def jdbcConnection(self, jdbcConnection: str):
        self.__jdbcConnection = jdbcConnection

class ProductIdentifiable:

    pass
class core_actionstep_ActionStep(ProductIdentifiable, PlatformDisposition, ThreadSensitive):

    def __init__(self, paused: bool, active: bool, name: str, Saflet: "Saflet" = None, core_actionstep_ActionStep: "Output" = None, Output: set["Output"] = None, core_actionstep_ActionStep5: "Output" = None):
        self.paused = paused
        self.active = active
        self.name = name
        self.Saflet = Saflet
        self.core_actionstep_ActionStep = core_actionstep_ActionStep
        self.Output = Output if Output is not None else set()
        self.core_actionstep_ActionStep5 = core_actionstep_ActionStep5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def paused(self) -> bool:
        return self.__paused

    @paused.setter
    def paused(self, paused: bool):
        self.__paused = paused

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def core_actionstep_ActionStep(self):
        return self.__core_actionstep_ActionStep

    @core_actionstep_ActionStep.setter
    def core_actionstep_ActionStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__core_actionstep_ActionStep", None)
        self.__core_actionstep_ActionStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output3"):
                opp_val = getattr(old_value, "Output3", None)
                if opp_val == self:
                    setattr(old_value, "Output3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output3"):
                opp_val = getattr(value, "Output3", None)
                setattr(value, "Output3", self)

    @property
    def Saflet(self):
        return self.__Saflet

    @Saflet.setter
    def Saflet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__Saflet", None)
        self.__Saflet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "saflet"):
                opp_val = getattr(old_value, "saflet", None)
                if opp_val == self:
                    setattr(old_value, "saflet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "saflet"):
                opp_val = getattr(value, "saflet", None)
                setattr(value, "saflet", self)

    @property
    def core_actionstep_ActionStep5(self):
        return self.__core_actionstep_ActionStep5

    @core_actionstep_ActionStep5.setter
    def core_actionstep_ActionStep5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__core_actionstep_ActionStep5", None)
        self.__core_actionstep_ActionStep5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output6"):
                opp_val = getattr(old_value, "Output6", None)
                if opp_val == self:
                    setattr(old_value, "Output6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output6"):
                opp_val = getattr(value, "Output6", None)
                setattr(value, "Output6", self)

    @property
    def Output(self):
        return self.__Output

    @Output.setter
    def Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__Output", None)
        self.__Output = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actionstep"):
                    opp_val = getattr(item, "actionstep", None)
                    
                    if opp_val == self:
                        setattr(item, "actionstep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actionstep"):
                    opp_val = getattr(item, "actionstep", None)
                    
                    setattr(item, "actionstep", self)
                    

    def resolveDynamicValue(self, dynamicValue: str, context: str) -> str:
        # TODO: Implement resolveDynamicValue method
        pass

    def handleException(self, e: str, context: str):
        # TODO: Implement handleException method
        pass

    def createDefaultOutputs(self):
        # TODO: Implement createDefaultOutputs method
        pass

    def executeScript(self, scriptName: str, scriptText: str) -> str:
        # TODO: Implement executeScript method
        pass

    def beginProcessing(self, context: str):
        # TODO: Implement beginProcessing method
        pass

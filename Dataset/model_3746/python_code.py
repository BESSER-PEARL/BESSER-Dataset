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
class OutputType(Enum):
    Default = "Default"
    Error = "Error"
    Choice = "Choice"
class InputType(Enum):
    Value = "Value"
    Variable = "Variable"
class DebugLevel(Enum):
    Debug = "Debug"
    Warn = "Warn"
    Error = "Error"
    Info = "Info"


############################################
# Definition of Classes
############################################

class GetColMapping:

    pass
class DBQueryId:

    pass
class DBQueryParamId:

    pass
class DBConnectionId:

    pass
class actionstep_Heavyweight:

    pass
class actionstep_ActionStep:

    pass
class core_actionstep_OpenDBConnection(actionstep_ActionStep, actionstep_Heavyweight):

    pass
class actionstep_core_EStringToStringMapEntry:

    pass
class actionstep_core_EObject:

    pass
class core_actionstep_Output:

    def __init__(self, name: str, outputType: str, core_actionstep_Output: "ActionStep" = None, outputs: "ActionStep" = None):
        self.name = name
        self.outputType = outputType
        self.core_actionstep_Output = core_actionstep_Output
        self.outputs = outputs
        
        pass
    @property
    def outputType(self):
        return self.__outputType

    @outputType.setter
    def outputType(self, outputType: str):
        self.__outputType = outputType


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def outputs(self):
        return self.__outputs

    @outputs.setter
    def outputs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Output__outputs", None)
        self.__outputs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionStep27"):
                opp_val = getattr(old_value, "ActionStep27", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep27"):
                opp_val = getattr(value, "ActionStep27", None)
                setattr(value, "ActionStep27", self)

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

class DynamicValue:

    pass
class ActionStep:

    pass
class core_actionstep_CloseDBConnection(ActionStep):

    pass
class core_actionstep_InvokeSaflet(ActionStep):

    def __init__(self, labelText: str, core_actionstep_InvokeSaflet: "DynamicValue" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.labelText = labelText
        self.core_actionstep_InvokeSaflet = core_actionstep_InvokeSaflet
        
        pass
    @property
    def labelText(self):
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
            if hasattr(old_value, "DynamicValue31"):
                opp_val = getattr(old_value, "DynamicValue31", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue31"):
                opp_val = getattr(value, "DynamicValue31", None)
                setattr(value, "DynamicValue31", self)

class core_actionstep_OpenQuery(ActionStep):

    def __init__(self, useCache: bool, scrollable: bool, readOnly: bool, scrollMode: str, holdabilityMode: str, core_actionstep_OpenQuery: "DBQueryId" = None, core_actionstep_OpenQuery42: "DBConnectionId" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.useCache = useCache
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.scrollMode = scrollMode
        self.holdabilityMode = holdabilityMode
        self.core_actionstep_OpenQuery = core_actionstep_OpenQuery
        self.core_actionstep_OpenQuery42 = core_actionstep_OpenQuery42
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def scrollMode(self):
        return self.__scrollMode

    @scrollMode.setter
    def scrollMode(self, scrollMode: str):
        self.__scrollMode = scrollMode


    @property
    def scrollable(self):
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable


    @property
    def holdabilityMode(self):
        return self.__holdabilityMode

    @holdabilityMode.setter
    def holdabilityMode(self, holdabilityMode: str):
        self.__holdabilityMode = holdabilityMode


    @property
    def useCache(self):
        return self.__useCache

    @useCache.setter
    def useCache(self, useCache: bool):
        self.__useCache = useCache


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

    @property
    def core_actionstep_OpenQuery42(self):
        return self.__core_actionstep_OpenQuery42

    @core_actionstep_OpenQuery42.setter
    def core_actionstep_OpenQuery42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_OpenQuery__core_actionstep_OpenQuery42", None)
        self.__core_actionstep_OpenQuery42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBConnectionId43"):
                opp_val = getattr(old_value, "DBConnectionId43", None)
                if opp_val == self:
                    setattr(old_value, "DBConnectionId43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBConnectionId43"):
                opp_val = getattr(value, "DBConnectionId43", None)
                setattr(value, "DBConnectionId43", self)

class core_actionstep_ExecuteUpdate(ActionStep):

    pass
class core_actionstep_GetColValues(ActionStep):

    pass
class core_actionstep_ExecuteScript(ActionStep):

    pass
class core_actionstep_Choice(ActionStep):

    pass
class core_actionstep_SetQueryParam(ActionStep):

    def __init__(self, paramDatatype: str, core_actionstep_SetQueryParam: "DynamicValue" = None, core_actionstep_SetQueryParam47: "DBQueryParamId" = None, core_actionstep_SetQueryParam49: "DBQueryId" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.paramDatatype = paramDatatype
        self.core_actionstep_SetQueryParam = core_actionstep_SetQueryParam
        self.core_actionstep_SetQueryParam47 = core_actionstep_SetQueryParam47
        self.core_actionstep_SetQueryParam49 = core_actionstep_SetQueryParam49
        
        pass
    @property
    def paramDatatype(self):
        return self.__paramDatatype

    @paramDatatype.setter
    def paramDatatype(self, paramDatatype: str):
        self.__paramDatatype = paramDatatype


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
            if hasattr(old_value, "DynamicValue45"):
                opp_val = getattr(old_value, "DynamicValue45", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue45"):
                opp_val = getattr(value, "DynamicValue45", None)
                setattr(value, "DynamicValue45", self)

    @property
    def core_actionstep_SetQueryParam47(self):
        return self.__core_actionstep_SetQueryParam47

    @core_actionstep_SetQueryParam47.setter
    def core_actionstep_SetQueryParam47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetQueryParam__core_actionstep_SetQueryParam47", None)
        self.__core_actionstep_SetQueryParam47 = value
        
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
    def core_actionstep_SetQueryParam49(self):
        return self.__core_actionstep_SetQueryParam49

    @core_actionstep_SetQueryParam49.setter
    def core_actionstep_SetQueryParam49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetQueryParam__core_actionstep_SetQueryParam49", None)
        self.__core_actionstep_SetQueryParam49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId50"):
                opp_val = getattr(old_value, "DBQueryId50", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId50"):
                opp_val = getattr(value, "DBQueryId50", None)
                setattr(value, "DBQueryId50", self)

class core_actionstep_IfThen(ActionStep):

    pass
class core_actionstep_DebugLog(ActionStep):

    def __init__(self, debugLevel: str, core_actionstep_DebugLog: "DynamicValue" = None, core_actionstep_DebugLog35: "DynamicValue" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.debugLevel = debugLevel
        self.core_actionstep_DebugLog = core_actionstep_DebugLog
        self.core_actionstep_DebugLog35 = core_actionstep_DebugLog35
        
        pass
    @property
    def debugLevel(self):
        return self.__debugLevel

    @debugLevel.setter
    def debugLevel(self, debugLevel: str):
        self.__debugLevel = debugLevel


    @property
    def core_actionstep_DebugLog35(self):
        return self.__core_actionstep_DebugLog35

    @core_actionstep_DebugLog35.setter
    def core_actionstep_DebugLog35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_DebugLog__core_actionstep_DebugLog35", None)
        self.__core_actionstep_DebugLog35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue36"):
                opp_val = getattr(old_value, "DynamicValue36", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue36"):
                opp_val = getattr(value, "DynamicValue36", None)
                setattr(value, "DynamicValue36", self)

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
            if hasattr(old_value, "DynamicValue33"):
                opp_val = getattr(old_value, "DynamicValue33", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue33"):
                opp_val = getattr(value, "DynamicValue33", None)
                setattr(value, "DynamicValue33", self)

class core_actionstep_Assignment(ActionStep):

    pass
class actionstep_ParameterizedActionstep:

    pass
class initiator_Initiator:

    pass
class core_actionstep_ParameterizedInitiator(actionstep_ParameterizedActionstep, initiator_Initiator):

    def __init__(self):
        
        pass
    def getOutputMap(self):
        # TODO: Implement getOutputMap method
        pass

class OutputParameter:

    pass
class InputItem:

    pass
class core_actionstep_ParameterizedActionstep(ActionStep):

    pass
class CaseItem:

    pass
class core_actionstep_InputItem(CaseItem):

    def __init__(self, parameterName: str, required: bool, CaseItem: "core_actionstep_Choice" = None):
        self.parameterName = parameterName
        self.required = required
        
        pass
    @property
    def parameterName(self):
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName


    @property
    def required(self):
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required


class Item:

    pass
class core_actionstep_CaseItem(Item):

    pass
class core_PlatformDisposition(ABC):

    def __init__(self, platformID: str, platformDependant: bool):
        self.platformID = platformID
        self.platformDependant = platformDependant
        
        pass
    @property
    def platformDependant(self):
        return self.__platformDependant

    @platformDependant.setter
    def platformDependant(self, platformDependant: bool):
        self.__platformDependant = platformDependant


    @property
    def platformID(self):
        return self.__platformID

    @platformID.setter
    def platformID(self, platformID: str):
        self.__platformID = platformID


class core_ThreadSensitive:

    def __init__(self):
        
        pass
    def cleanup(self):
        # TODO: Implement cleanup method
        pass

class core_ProductIdentifiable(ABC):

    def __init__(self, productId: str):
        self.productId = productId
        
        pass
    @property
    def productId(self):
        return self.__productId

    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId


class Saflet:

    pass
class Output:

    pass
class PlatformDisposition:

    pass
class ThreadSensitive:

    pass
class core_actionstep_DynamicValue(ThreadSensitive):

    def __init__(self, text: str, type: str, core_actionstep_DynamicValue: "actionstep_core_EObject" = None, core_actionstep_DynamicValue22: set["actionstep_core_EStringToStringMapEntry"] = None):
        self.text = text
        self.type = type
        self.core_actionstep_DynamicValue = core_actionstep_DynamicValue
        self.core_actionstep_DynamicValue22 = core_actionstep_DynamicValue22 if core_actionstep_DynamicValue22 is not None else set()
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def type(self):
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

class ProductIdentifiable:

    pass
class core_actionstep_ActionStep(ProductIdentifiable, ThreadSensitive, PlatformDisposition):

    def __init__(self, paused: bool, active: bool, name: str, parent: set["Output"] = None, actionsteps: "Saflet" = None, core_actionstep_ActionStep: "Output" = None, core_actionstep_ActionStep5: "Output" = None):
        self.paused = paused
        self.active = active
        self.name = name
        self.parent = parent if parent is not None else set()
        self.actionsteps = actionsteps
        self.core_actionstep_ActionStep = core_actionstep_ActionStep
        self.core_actionstep_ActionStep5 = core_actionstep_ActionStep5
        
        pass
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def paused(self):
        return self.__paused

    @paused.setter
    def paused(self, paused: bool):
        self.__paused = paused


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
    def actionsteps(self):
        return self.__actionsteps

    @actionsteps.setter
    def actionsteps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__actionsteps", None)
        self.__actionsteps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Saflet"):
                opp_val = getattr(old_value, "Saflet", None)
                if opp_val == self:
                    setattr(old_value, "Saflet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Saflet"):
                opp_val = getattr(value, "Saflet", None)
                setattr(value, "Saflet", self)

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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ActionStep__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Output"):
                    opp_val = getattr(item, "Output", None)
                    
                    if opp_val == self:
                        setattr(item, "Output", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Output"):
                    opp_val = getattr(item, "Output", None)
                    
                    setattr(item, "Output", self)
                    

    def executeScript(self, core_scriptName, core_scriptText) :
        # TODO: Implement executeScript method
        pass

    def handleException(self, core_e, core_context):
        # TODO: Implement handleException method
        pass

    def beginProcessing(self, core_context):
        # TODO: Implement beginProcessing method
        pass

    def resolveDynamicValue(self, core_dynamicValue, core_context) :
        # TODO: Implement resolveDynamicValue method
        pass

    def createDefaultOutputs(self):
        # TODO: Implement createDefaultOutputs method
        pass

class core_initiator_InitiatorInfo(ABC):

    pass
class core_initiator_Initiator(ActionStep):

    def __init__(self, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        
        pass
    def acceptsRequest(self, core_context) :
        # TODO: Implement acceptsRequest method
        pass

    def beginProcessing(self):
        # TODO: Implement beginProcessing method
        pass

    def initialize(self, core_context):
        # TODO: Implement initialize method
        pass

class CallConsumer1:

    pass
class core_call_CallConsumer2(CallConsumer1):

    pass
class core_call_CallConsumer1(ABC):

    pass
class CallSource1:

    pass
class core_call_CallSource2(CallSource1):

    pass
class SafiCall:

    pass
class core_call_CallSource1(ABC):

    pass
class core_call_SafiCall(ThreadSensitive, PlatformDisposition):

    def __init__(self, uuid: str, name: str):
        self.uuid = uuid
        self.name = name
        
        pass
    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class core_saflet_SafletContext(ThreadSensitive):

    def __init__(self, exceptions: str, sessionVariables: str, core_saflet_SafletContext: "Saflet" = None, core_saflet_SafletContext172: set["saflet_core_Variable"] = None):
        self.exceptions = exceptions
        self.sessionVariables = sessionVariables
        self.core_saflet_SafletContext = core_saflet_SafletContext
        self.core_saflet_SafletContext172 = core_saflet_SafletContext172 if core_saflet_SafletContext172 is not None else set()
        
        pass
    @property
    def exceptions(self):
        return self.__exceptions

    @exceptions.setter
    def exceptions(self, exceptions: str):
        self.__exceptions = exceptions


    @property
    def sessionVariables(self):
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
            if hasattr(old_value, "Saflet170"):
                opp_val = getattr(old_value, "Saflet170", None)
                if opp_val == self:
                    setattr(old_value, "Saflet170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Saflet170"):
                opp_val = getattr(value, "Saflet170", None)
                setattr(value, "Saflet170", self)

    @property
    def core_saflet_SafletContext172(self):
        return self.__core_saflet_SafletContext172

    @core_saflet_SafletContext172.setter
    def core_saflet_SafletContext172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_SafletContext__core_saflet_SafletContext172", None)
        self.__core_saflet_SafletContext172 = value if value is not None else set()
        
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
                    

    def merge(self, core_context):
        # TODO: Implement merge method
        pass

    def getVariableRawValue(self, core_name) :
        # TODO: Implement getVariableRawValue method
        pass

    def addOrUpdateVariable(self, core_v):
        # TODO: Implement addOrUpdateVariable method
        pass

    def preHandoffPrep(self, core_call):
        # TODO: Implement preHandoffPrep method
        pass

    def removeVariable(self, core_name) :
        # TODO: Implement removeVariable method
        pass

    def getSessionVar(self, core_name) :
        # TODO: Implement getSessionVar method
        pass

    def setSessionVar(self, core_value, core_name):
        # TODO: Implement setSessionVar method
        pass

    def addException(self, core_e):
        # TODO: Implement addException method
        pass

    def getVariable(self, core_name) :
        # TODO: Implement getVariable method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def setVariableRawValue(self, core_name, core_value):
        # TODO: Implement setVariableRawValue method
        pass

class Finally:

    pass
class SafletEnvironment:

    pass
class core_saflet_SafletEnvironment(ThreadSensitive):

    def __init__(self):
        
        pass
    def getGlobalExecutor(self) :
        # TODO: Implement getGlobalExecutor method
        pass

    def getGlobalVariableValue(self, core_name) :
        # TODO: Implement getGlobalVariableValue method
        pass

    def setGlobalVariableValue(self, core_name, core_value):
        # TODO: Implement setGlobalVariableValue method
        pass

    def getSaflet(self, core_coreServerId, core_path) :
        # TODO: Implement getSaflet method
        pass

    def getGlobalVariable(self, core_name) :
        # TODO: Implement getGlobalVariable method
        pass

class saflet_core_Variable:

    pass
class core_saflet_Saflet(ThreadSensitive, PlatformDisposition):

    def __init__(self, active: bool, name: str, version: str, description: str, id: int, core_saflet_Saflet: "Initiator" = None, core_saflet_Saflet157: "SafletContext" = None, core_saflet_Saflet159: "ScriptScope" = None, saflet: set["ActionStep"] = None, core_saflet_Saflet164: "SafletScriptEnvironment" = None, core_saflet_Saflet166: "SafletEnvironment" = None, core_saflet_Saflet168: "Finally" = None):
        self.active = active
        self.name = name
        self.version = version
        self.description = description
        self.id = id
        self.core_saflet_Saflet = core_saflet_Saflet
        self.core_saflet_Saflet157 = core_saflet_Saflet157
        self.core_saflet_Saflet159 = core_saflet_Saflet159
        self.saflet = saflet if saflet is not None else set()
        self.core_saflet_Saflet164 = core_saflet_Saflet164
        self.core_saflet_Saflet166 = core_saflet_Saflet166
        self.core_saflet_Saflet168 = core_saflet_Saflet168
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def saflet(self):
        return self.__saflet

    @saflet.setter
    def saflet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__saflet", None)
        self.__saflet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionStep162"):
                    opp_val = getattr(item, "ActionStep162", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionStep162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionStep162"):
                    opp_val = getattr(item, "ActionStep162", None)
                    
                    setattr(item, "ActionStep162", self)
                    

    @property
    def core_saflet_Saflet157(self):
        return self.__core_saflet_Saflet157

    @core_saflet_Saflet157.setter
    def core_saflet_Saflet157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet157", None)
        self.__core_saflet_Saflet157 = value
        
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
    def core_saflet_Saflet168(self):
        return self.__core_saflet_Saflet168

    @core_saflet_Saflet168.setter
    def core_saflet_Saflet168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet168", None)
        self.__core_saflet_Saflet168 = value
        
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
    def core_saflet_Saflet159(self):
        return self.__core_saflet_Saflet159

    @core_saflet_Saflet159.setter
    def core_saflet_Saflet159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet159", None)
        self.__core_saflet_Saflet159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptScope160"):
                opp_val = getattr(old_value, "ScriptScope160", None)
                if opp_val == self:
                    setattr(old_value, "ScriptScope160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptScope160"):
                opp_val = getattr(value, "ScriptScope160", None)
                setattr(value, "ScriptScope160", self)

    @property
    def core_saflet_Saflet164(self):
        return self.__core_saflet_Saflet164

    @core_saflet_Saflet164.setter
    def core_saflet_Saflet164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_saflet_Saflet__core_saflet_Saflet164", None)
        self.__core_saflet_Saflet164 = value
        
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

    def initializeScriptableObjects(self):
        # TODO: Implement initializeScriptableObjects method
        pass

    def getActionStep(self, core_name) :
        # TODO: Implement getActionStep method
        pass

    def addActionStep(self, core_actionstep):
        # TODO: Implement addActionStep method
        pass

    def addScript(self, core_scriptText, core_name) :
        # TODO: Implement addScript method
        pass

    def getScript(self, core_name) :
        # TODO: Implement getScript method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class core_scripting_ScriptScopeFactory(ABC):

    pass
class SafletContext:

    pass
class Initiator:

    pass
class core_scripting_SafletScript(ABC):

    def __init__(self, name: str, scriptText: str):
        self.name = name
        self.scriptText = scriptText
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scriptText(self):
        return self.__scriptText

    @scriptText.setter
    def scriptText(self, scriptText: str):
        self.__scriptText = scriptText


    def execute(self, core_scope) :
        # TODO: Implement execute method
        pass

class core_actionstep_Finally(ActionStep):

    pass
class core_actionstep_OutputParameter(InputItem):

    pass
class core_actionstep_Heavyweight(ABC):

    pass
class core_scripting_ScriptScope(ABC):

    def __init__(self, scopeObject: str):
        self.scopeObject = scopeObject
        
        pass
    @property
    def scopeObject(self):
        return self.__scopeObject

    @scopeObject.setter
    def scopeObject(self, scopeObject: str):
        self.__scopeObject = scopeObject


    def updateVariablesFromScope(self, core_isDebug, core_variables, core_safletEnvironment):
        # TODO: Implement updateVariablesFromScope method
        pass

    def getScopedObject(self, core_name) :
        # TODO: Implement getScopedObject method
        pass

    def exposeObjectToScript(self, core_name, core_value):
        # TODO: Implement exposeObjectToScript method
        pass

    def removeObjectFromScope(self, core_name):
        # TODO: Implement removeObjectFromScope method
        pass

class SafletScriptEnvironment:

    pass
class core_scripting_RhinoSafletScriptEnvironment(SafletScriptEnvironment):

    pass
class core_scripting_SafletScriptFactory(ABC):

    def __init__(self, core_scripting_SafletScriptFactory: "SafletScript" = None):
        self.core_scripting_SafletScriptFactory = core_scripting_SafletScriptFactory
        
        pass
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
            if hasattr(old_value, "SafletScript149"):
                opp_val = getattr(old_value, "SafletScript149", None)
                if opp_val == self:
                    setattr(old_value, "SafletScript149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SafletScript149"):
                opp_val = getattr(value, "SafletScript149", None)
                setattr(value, "SafletScript149", self)

    def getSafletScript(self, core_name, core_scriptText) :
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

    def __init__(self, rhinoScript: str, SafletScript149: "core_scripting_SafletScriptFactory" = None, SafletScript: "core_scripting_SafletScriptEnvironment" = None):
        self.rhinoScript = rhinoScript
        
        pass
    @property
    def rhinoScript(self):
        return self.__rhinoScript

    @rhinoScript.setter
    def rhinoScript(self, rhinoScript: str):
        self.__rhinoScript = rhinoScript


class core_scripting_SafletScriptEnvironment(ABC):

    pass
class core_actionstep_Item(ThreadSensitive):

    def __init__(self, labelText: str, core_actionstep_Item: "ActionStep" = None, core_actionstep_Item139: "ActionStep" = None):
        self.labelText = labelText
        self.core_actionstep_Item = core_actionstep_Item
        self.core_actionstep_Item139 = core_actionstep_Item139
        
        pass
    @property
    def labelText(self):
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
            if hasattr(old_value, "ActionStep137"):
                opp_val = getattr(old_value, "ActionStep137", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep137"):
                opp_val = getattr(value, "ActionStep137", None)
                setattr(value, "ActionStep137", self)

    @property
    def core_actionstep_Item139(self):
        return self.__core_actionstep_Item139

    @core_actionstep_Item139.setter
    def core_actionstep_Item139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_Item__core_actionstep_Item139", None)
        self.__core_actionstep_Item139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionStep140"):
                opp_val = getattr(old_value, "ActionStep140", None)
                if opp_val == self:
                    setattr(old_value, "ActionStep140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionStep140"):
                opp_val = getattr(value, "ActionStep140", None)
                setattr(value, "ActionStep140", self)

class core_actionstep_QueryParamMapping(Item):

    def __init__(self, setAsDatatype: str, core_actionstep_QueryParamMapping: "DBQueryParamId" = None, core_actionstep_QueryParamMapping134: "DynamicValue" = None):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_QueryParamMapping = core_actionstep_QueryParamMapping
        self.core_actionstep_QueryParamMapping134 = core_actionstep_QueryParamMapping134
        
        pass
    @property
    def setAsDatatype(self):
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype


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
            if hasattr(old_value, "DBQueryParamId132"):
                opp_val = getattr(old_value, "DBQueryParamId132", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryParamId132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryParamId132"):
                opp_val = getattr(value, "DBQueryParamId132", None)
                setattr(value, "DBQueryParamId132", self)

    @property
    def core_actionstep_QueryParamMapping134(self):
        return self.__core_actionstep_QueryParamMapping134

    @core_actionstep_QueryParamMapping134.setter
    def core_actionstep_QueryParamMapping134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_QueryParamMapping__core_actionstep_QueryParamMapping134", None)
        self.__core_actionstep_QueryParamMapping134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue135"):
                opp_val = getattr(old_value, "DynamicValue135", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue135"):
                opp_val = getattr(value, "DynamicValue135", None)
                setattr(value, "DynamicValue135", self)

class QueryParamMapping:

    pass
class core_actionstep_RunQuery(actionstep_ActionStep, actionstep_Heavyweight):

    def __init__(self, resultSetName: str, scrollable: bool, readOnly: bool, core_actionstep_RunQuery: "DBConnectionId" = None, core_actionstep_RunQuery118: "DBQueryId" = None, core_actionstep_RunQuery121: set["QueryParamMapping"] = None, core_actionstep_RunQuery129: "DynamicValue" = None, core_actionstep_RunQuery123: "DBResultSetId" = None, core_actionstep_RunQuery126: "DynamicValue" = None):
        self.resultSetName = resultSetName
        self.scrollable = scrollable
        self.readOnly = readOnly
        self.core_actionstep_RunQuery = core_actionstep_RunQuery
        self.core_actionstep_RunQuery118 = core_actionstep_RunQuery118
        self.core_actionstep_RunQuery121 = core_actionstep_RunQuery121 if core_actionstep_RunQuery121 is not None else set()
        self.core_actionstep_RunQuery129 = core_actionstep_RunQuery129
        self.core_actionstep_RunQuery123 = core_actionstep_RunQuery123
        self.core_actionstep_RunQuery126 = core_actionstep_RunQuery126
        
        pass
    @property
    def resultSetName(self):
        return self.__resultSetName

    @resultSetName.setter
    def resultSetName(self, resultSetName: str):
        self.__resultSetName = resultSetName


    @property
    def scrollable(self):
        return self.__scrollable

    @scrollable.setter
    def scrollable(self, scrollable: bool):
        self.__scrollable = scrollable


    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def core_actionstep_RunQuery118(self):
        return self.__core_actionstep_RunQuery118

    @core_actionstep_RunQuery118.setter
    def core_actionstep_RunQuery118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery118", None)
        self.__core_actionstep_RunQuery118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBQueryId119"):
                opp_val = getattr(old_value, "DBQueryId119", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId119"):
                opp_val = getattr(value, "DBQueryId119", None)
                setattr(value, "DBQueryId119", self)

    @property
    def core_actionstep_RunQuery121(self):
        return self.__core_actionstep_RunQuery121

    @core_actionstep_RunQuery121.setter
    def core_actionstep_RunQuery121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery121", None)
        self.__core_actionstep_RunQuery121 = value if value is not None else set()
        
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
    def core_actionstep_RunQuery(self):
        return self.__core_actionstep_RunQuery

    @core_actionstep_RunQuery.setter
    def core_actionstep_RunQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery", None)
        self.__core_actionstep_RunQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBConnectionId116"):
                opp_val = getattr(old_value, "DBConnectionId116", None)
                if opp_val == self:
                    setattr(old_value, "DBConnectionId116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBConnectionId116"):
                opp_val = getattr(value, "DBConnectionId116", None)
                setattr(value, "DBConnectionId116", self)

    @property
    def core_actionstep_RunQuery123(self):
        return self.__core_actionstep_RunQuery123

    @core_actionstep_RunQuery123.setter
    def core_actionstep_RunQuery123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery123", None)
        self.__core_actionstep_RunQuery123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DBResultSetId124"):
                opp_val = getattr(old_value, "DBResultSetId124", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId124"):
                opp_val = getattr(value, "DBResultSetId124", None)
                setattr(value, "DBResultSetId124", self)

    @property
    def core_actionstep_RunQuery129(self):
        return self.__core_actionstep_RunQuery129

    @core_actionstep_RunQuery129.setter
    def core_actionstep_RunQuery129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery129", None)
        self.__core_actionstep_RunQuery129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue130"):
                opp_val = getattr(old_value, "DynamicValue130", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue130"):
                opp_val = getattr(value, "DynamicValue130", None)
                setattr(value, "DynamicValue130", self)

    @property
    def core_actionstep_RunQuery126(self):
        return self.__core_actionstep_RunQuery126

    @core_actionstep_RunQuery126.setter
    def core_actionstep_RunQuery126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_RunQuery__core_actionstep_RunQuery126", None)
        self.__core_actionstep_RunQuery126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue127"):
                opp_val = getattr(old_value, "DynamicValue127", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue127"):
                opp_val = getattr(value, "DynamicValue127", None)
                setattr(value, "DynamicValue127", self)

    def refreshParams(self, core_qry):
        # TODO: Implement refreshParams method
        pass

class core_actionstep_GetColMapping(Item):

    def __init__(self, getAsDatatype: str, core_actionstep_GetColMapping108: "DynamicValue" = None, core_actionstep_GetColMapping: "DynamicValue" = None):
        self.getAsDatatype = getAsDatatype
        self.core_actionstep_GetColMapping108 = core_actionstep_GetColMapping108
        self.core_actionstep_GetColMapping = core_actionstep_GetColMapping
        
        pass
    @property
    def getAsDatatype(self):
        return self.__getAsDatatype

    @getAsDatatype.setter
    def getAsDatatype(self, getAsDatatype: str):
        self.__getAsDatatype = getAsDatatype


    @property
    def core_actionstep_GetColMapping108(self):
        return self.__core_actionstep_GetColMapping108

    @core_actionstep_GetColMapping108.setter
    def core_actionstep_GetColMapping108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColMapping__core_actionstep_GetColMapping108", None)
        self.__core_actionstep_GetColMapping108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue109"):
                opp_val = getattr(old_value, "DynamicValue109", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue109"):
                opp_val = getattr(value, "DynamicValue109", None)
                setattr(value, "DynamicValue109", self)

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
            if hasattr(old_value, "DynamicValue106"):
                opp_val = getattr(old_value, "DynamicValue106", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue106"):
                opp_val = getattr(value, "DynamicValue106", None)
                setattr(value, "DynamicValue106", self)

class core_actionstep_DBResultSetId(ThreadSensitive):

    def __init__(self, name: str, id: str, jDBCResultSet: str):
        self.name = name
        self.id = id
        self.jDBCResultSet = jDBCResultSet
        
        pass
    @property
    def jDBCResultSet(self):
        return self.__jDBCResultSet

    @jDBCResultSet.setter
    def jDBCResultSet(self, jDBCResultSet: str):
        self.__jDBCResultSet = jDBCResultSet


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class core_actionstep_DBQueryParamId:

    def __init__(self, id: str, index: int):
        self.id = id
        self.index = index
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


class core_actionstep_SetColMapping(Item):

    def __init__(self, setAsDatatype: str, core_actionstep_SetColMapping: "DynamicValue" = None, core_actionstep_SetColMapping113: "DynamicValue" = None):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_SetColMapping = core_actionstep_SetColMapping
        self.core_actionstep_SetColMapping113 = core_actionstep_SetColMapping113
        
        pass
    @property
    def setAsDatatype(self):
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype


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
            if hasattr(old_value, "DynamicValue111"):
                opp_val = getattr(old_value, "DynamicValue111", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue111"):
                opp_val = getattr(value, "DynamicValue111", None)
                setattr(value, "DynamicValue111", self)

    @property
    def core_actionstep_SetColMapping113(self):
        return self.__core_actionstep_SetColMapping113

    @core_actionstep_SetColMapping113.setter
    def core_actionstep_SetColMapping113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColMapping__core_actionstep_SetColMapping113", None)
        self.__core_actionstep_SetColMapping113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue114"):
                opp_val = getattr(old_value, "DynamicValue114", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue114"):
                opp_val = getattr(value, "DynamicValue114", None)
                setattr(value, "DynamicValue114", self)

class core_actionstep_DeleteRow(ActionStep):

    pass
class core_actionstep_MoveToLastRow(ActionStep):

    pass
class core_actionstep_DBQueryId(ThreadSensitive):

    def __init__(self, id: str, jdbcStatement: str):
        self.id = id
        self.jdbcStatement = jdbcStatement
        
        pass
    @property
    def jdbcStatement(self):
        return self.__jdbcStatement

    @jdbcStatement.setter
    def jdbcStatement(self, jdbcStatement: str):
        self.__jdbcStatement = jdbcStatement


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class core_actionstep_DBConnectionId(ThreadSensitive):

    def __init__(self, id: str, jdbcConnection: str):
        self.id = id
        self.jdbcConnection = jdbcConnection
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def jdbcConnection(self):
        return self.__jdbcConnection

    @jdbcConnection.setter
    def jdbcConnection(self, jdbcConnection: str):
        self.__jdbcConnection = jdbcConnection


class core_actionstep_PreviousRow(ActionStep):

    pass
class core_actionstep_MoveToFirstRow(ActionStep):

    pass
class core_actionstep_InsertRow(ActionStep):

    pass
class core_actionstep_MoveToInsertRow(ActionStep):

    pass
class core_actionstep_MoveToRow(ActionStep):

    pass
class core_actionstep_UpdatetRow(actionstep_ActionStep, actionstep_Heavyweight):

    pass
class SetColMapping:

    pass
class core_actionstep_SetColValues(ActionStep):

    pass
class core_actionstep_GetColValue(ActionStep):

    def __init__(self, getAsDatatype: str, core_actionstep_GetColValue: "DBResultSetId" = None, core_actionstep_GetColValue65: "DynamicValue" = None, core_actionstep_GetColValue68: "DynamicValue" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.getAsDatatype = getAsDatatype
        self.core_actionstep_GetColValue = core_actionstep_GetColValue
        self.core_actionstep_GetColValue65 = core_actionstep_GetColValue65
        self.core_actionstep_GetColValue68 = core_actionstep_GetColValue68
        
        pass
    @property
    def getAsDatatype(self):
        return self.__getAsDatatype

    @getAsDatatype.setter
    def getAsDatatype(self, getAsDatatype: str):
        self.__getAsDatatype = getAsDatatype


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
            if hasattr(old_value, "DBResultSetId63"):
                opp_val = getattr(old_value, "DBResultSetId63", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId63"):
                opp_val = getattr(value, "DBResultSetId63", None)
                setattr(value, "DBResultSetId63", self)

    @property
    def core_actionstep_GetColValue65(self):
        return self.__core_actionstep_GetColValue65

    @core_actionstep_GetColValue65.setter
    def core_actionstep_GetColValue65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColValue__core_actionstep_GetColValue65", None)
        self.__core_actionstep_GetColValue65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue66"):
                opp_val = getattr(old_value, "DynamicValue66", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue66"):
                opp_val = getattr(value, "DynamicValue66", None)
                setattr(value, "DynamicValue66", self)

    @property
    def core_actionstep_GetColValue68(self):
        return self.__core_actionstep_GetColValue68

    @core_actionstep_GetColValue68.setter
    def core_actionstep_GetColValue68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_GetColValue__core_actionstep_GetColValue68", None)
        self.__core_actionstep_GetColValue68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue69"):
                opp_val = getattr(old_value, "DynamicValue69", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue69"):
                opp_val = getattr(value, "DynamicValue69", None)
                setattr(value, "DynamicValue69", self)

class core_actionstep_NextRow(ActionStep):

    pass
class DBResultSetId:

    pass
class core_actionstep_ExecuteQuery(actionstep_ActionStep, actionstep_Heavyweight):

    def __init__(self, resultSetName: str, core_actionstep_ExecuteQuery: "DBQueryId" = None, core_actionstep_ExecuteQuery59: "DBResultSetId" = None):
        self.resultSetName = resultSetName
        self.core_actionstep_ExecuteQuery = core_actionstep_ExecuteQuery
        self.core_actionstep_ExecuteQuery59 = core_actionstep_ExecuteQuery59
        
        pass
    @property
    def resultSetName(self):
        return self.__resultSetName

    @resultSetName.setter
    def resultSetName(self, resultSetName: str):
        self.__resultSetName = resultSetName


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
            if hasattr(old_value, "DBQueryId57"):
                opp_val = getattr(old_value, "DBQueryId57", None)
                if opp_val == self:
                    setattr(old_value, "DBQueryId57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBQueryId57"):
                opp_val = getattr(value, "DBQueryId57", None)
                setattr(value, "DBQueryId57", self)

    @property
    def core_actionstep_ExecuteQuery59(self):
        return self.__core_actionstep_ExecuteQuery59

    @core_actionstep_ExecuteQuery59.setter
    def core_actionstep_ExecuteQuery59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_ExecuteQuery__core_actionstep_ExecuteQuery59", None)
        self.__core_actionstep_ExecuteQuery59 = value
        
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

class core_actionstep_SetColValue(ActionStep):

    def __init__(self, setAsDatatype: str, core_actionstep_SetColValue: "DBResultSetId" = None, core_actionstep_SetColValue77: "DynamicValue" = None, core_actionstep_SetColValue80: "DynamicValue" = None, ActionStep: "core_actionstep_Output" = None, ActionStep162: "core_saflet_Saflet" = None, ActionStep137: "core_actionstep_Item" = None, ActionStep140: "core_actionstep_Item" = None, ActionStep27: "core_actionstep_Output" = None):
        self.setAsDatatype = setAsDatatype
        self.core_actionstep_SetColValue = core_actionstep_SetColValue
        self.core_actionstep_SetColValue77 = core_actionstep_SetColValue77
        self.core_actionstep_SetColValue80 = core_actionstep_SetColValue80
        
        pass
    @property
    def setAsDatatype(self):
        return self.__setAsDatatype

    @setAsDatatype.setter
    def setAsDatatype(self, setAsDatatype: str):
        self.__setAsDatatype = setAsDatatype


    @property
    def core_actionstep_SetColValue80(self):
        return self.__core_actionstep_SetColValue80

    @core_actionstep_SetColValue80.setter
    def core_actionstep_SetColValue80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColValue__core_actionstep_SetColValue80", None)
        self.__core_actionstep_SetColValue80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue81"):
                opp_val = getattr(old_value, "DynamicValue81", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue81"):
                opp_val = getattr(value, "DynamicValue81", None)
                setattr(value, "DynamicValue81", self)

    @property
    def core_actionstep_SetColValue77(self):
        return self.__core_actionstep_SetColValue77

    @core_actionstep_SetColValue77.setter
    def core_actionstep_SetColValue77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_actionstep_SetColValue__core_actionstep_SetColValue77", None)
        self.__core_actionstep_SetColValue77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue78"):
                opp_val = getattr(old_value, "DynamicValue78", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue78"):
                opp_val = getattr(value, "DynamicValue78", None)
                setattr(value, "DynamicValue78", self)

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
            if hasattr(old_value, "DBResultSetId75"):
                opp_val = getattr(old_value, "DBResultSetId75", None)
                if opp_val == self:
                    setattr(old_value, "DBResultSetId75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DBResultSetId75"):
                opp_val = getattr(value, "DBResultSetId75", None)
                setattr(value, "DBResultSetId75", self)

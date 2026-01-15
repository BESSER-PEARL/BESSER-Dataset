from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class executionTrace_StoryPatternConstraintViolated:

    pass
class executionTrace_StoryPatternConstraintHolds:

    pass
class executionTrace_StoryPatternConstraintEvaluation(ABC):

    pass
class executionTrace_StoryPatternObjectConstraintViolated:

    pass
class executionTrace_StoryPatternObjectConstraintHolds:

    pass
class executionTrace_VariableCreated:

    pass
class executionTrace_StoryPatternObjectConstraintEvaluation(ABC):

    pass
class executionTrace_VariableChanged:

    def __init__(self, oldValue: str):
        self.oldValue = oldValue
        
    @property
    def oldValue(self) -> str:
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

class executionTrace_VariableDeleted:

    pass
class executionTrace_InstanceObjectDeletion:

    pass
class executionTrace_InstanceObjectCreation:

    pass
class executionTrace_InstanceLinkDeletion:

    pass
class executionTrace_InstanceLinkCreation:

    pass
class executionTrace_LinkCheck(ABC):

    def __init__(self, targetObject: str):
        self.targetObject = targetObject
        
    @property
    def targetObject(self) -> str:
        return self.__targetObject

    @targetObject.setter
    def targetObject(self, targetObject: str):
        self.__targetObject = targetObject

class executionTrace_TraversingLink:

    pass
class executionTrace_LinkCheckFailed:

    pass
class executionTrace_LinkCheckSuccessful:

    pass
class executionTrace_StoryPatternMatching:

    def __init__(self, successful: bool):
        self.successful = successful
        
    @property
    def successful(self) -> bool:
        return self.__successful

    @successful.setter
    def successful(self, successful: bool):
        self.__successful = successful

class executionTrace_StoryPatternInitialization:

    pass
class Execution:

    pass
class executionTrace_VariableModification(Execution):

    def __init__(self, variableName: str, value: str):
        self.variableName = variableName
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class executionTrace_InstanceObjectModification(Execution):

    def __init__(self, instanceObject: str):
        self.instanceObject = instanceObject
        
    @property
    def instanceObject(self) -> str:
        return self.__instanceObject

    @instanceObject.setter
    def instanceObject(self, instanceObject: str):
        self.__instanceObject = instanceObject

class executionTrace_InstanceLinkModification(Execution):

    def __init__(self, sourceInstanceObject: str, targetInstanceObject: str):
        self.sourceInstanceObject = sourceInstanceObject
        self.targetInstanceObject = targetInstanceObject
        
    @property
    def sourceInstanceObject(self) -> str:
        return self.__sourceInstanceObject

    @sourceInstanceObject.setter
    def sourceInstanceObject(self, sourceInstanceObject: str):
        self.__sourceInstanceObject = sourceInstanceObject

    @property
    def targetInstanceObject(self) -> str:
        return self.__targetInstanceObject

    @targetInstanceObject.setter
    def targetInstanceObject(self, targetInstanceObject: str):
        self.__targetInstanceObject = targetInstanceObject

class executionTrace_StoryPatternLinkExecution(Execution):

    def __init__(self, sourceObject: str):
        self.sourceObject = sourceObject
        
    @property
    def sourceObject(self) -> str:
        return self.__sourceObject

    @sourceObject.setter
    def sourceObject(self, sourceObject: str):
        self.__sourceObject = sourceObject

class executionTrace_AttributeValueSet(Execution):

    def __init__(self, instanceObject: str, newValue: str):
        self.instanceObject = instanceObject
        self.newValue = newValue
        
    @property
    def instanceObject(self) -> str:
        return self.__instanceObject

    @instanceObject.setter
    def instanceObject(self, instanceObject: str):
        self.__instanceObject = instanceObject

    @property
    def newValue(self) -> str:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

class executionTrace_ExpressionEvaluation(Execution):

    def __init__(self, result: str):
        self.result = result
        
    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, result: str):
        self.__result = result

class executionTrace_ActivityEdgeTraversal(Execution):

    pass
class executionTrace_ActivityNodeExecution(Execution):

    pass
class executionTrace_StoryPatternExecution(Execution):

    pass
class executionTrace_ActivityExecution(Execution):

    pass
class executionTrace_StoryPatternObjectBindingRevoked:

    def __init__(self, previousValue: str):
        self.previousValue = previousValue
        
    @property
    def previousValue(self) -> str:
        return self.__previousValue

    @previousValue.setter
    def previousValue(self, previousValue: str):
        self.__previousValue = previousValue

class executionTrace_StoryPatternObjectNotBound:

    pass
class executionTrace_StoryPatternObjectBound:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class executionTrace_StoryPatternObjectExecution(Execution):

    pass
class executionTrace_StoryPatternApplication:

    pass
class executionTrace_Execution(ABC):

    def __init__(self, executionStartedTimeStamp: str, executionFinishedTimeStamp: str, executionTime: str, executionTimeMsec: str, Execution: "executionTrace_Execution" = None, container: set["executionTrace_Execution"] = None, executionTrace_Execution: "executionTrace_ExecutionTrace" = None, Execution5: "executionTrace_Execution" = None, elements: "executionTrace_Execution" = None):
        self.executionStartedTimeStamp = executionStartedTimeStamp
        self.executionFinishedTimeStamp = executionFinishedTimeStamp
        self.executionTime = executionTime
        self.executionTimeMsec = executionTimeMsec
        self.Execution = Execution
        self.container = container if container is not None else set()
        self.executionTrace_Execution = executionTrace_Execution
        self.Execution5 = Execution5
        self.elements = elements
        
    @property
    def executionFinishedTimeStamp(self) -> str:
        return self.__executionFinishedTimeStamp

    @executionFinishedTimeStamp.setter
    def executionFinishedTimeStamp(self, executionFinishedTimeStamp: str):
        self.__executionFinishedTimeStamp = executionFinishedTimeStamp

    @property
    def executionTime(self) -> str:
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: str):
        self.__executionTime = executionTime

    @property
    def executionStartedTimeStamp(self) -> str:
        return self.__executionStartedTimeStamp

    @executionStartedTimeStamp.setter
    def executionStartedTimeStamp(self, executionStartedTimeStamp: str):
        self.__executionStartedTimeStamp = executionStartedTimeStamp

    @property
    def executionTimeMsec(self) -> str:
        return self.__executionTimeMsec

    @executionTimeMsec.setter
    def executionTimeMsec(self, executionTimeMsec: str):
        self.__executionTimeMsec = executionTimeMsec

    @property
    def executionTrace_Execution(self):
        return self.__executionTrace_Execution

    @executionTrace_Execution.setter
    def executionTrace_Execution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_Execution__executionTrace_Execution", None)
        self.__executionTrace_Execution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executionTrace_ExecutionTrace"):
                opp_val = getattr(old_value, "executionTrace_ExecutionTrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executionTrace_ExecutionTrace"):
                opp_val = getattr(value, "executionTrace_ExecutionTrace", None)
                if opp_val is None:
                    setattr(value, "executionTrace_ExecutionTrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_Execution__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Execution"):
                    opp_val = getattr(item, "Execution", None)
                    
                    if opp_val == self:
                        setattr(item, "Execution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Execution"):
                    opp_val = getattr(item, "Execution", None)
                    
                    setattr(item, "Execution", self)
                    

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_Execution__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Execution5"):
                opp_val = getattr(old_value, "Execution5", None)
                if opp_val == self:
                    setattr(old_value, "Execution5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Execution5"):
                opp_val = getattr(value, "Execution5", None)
                setattr(value, "Execution5", self)

    @property
    def Execution(self):
        return self.__Execution

    @Execution.setter
    def Execution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_Execution__Execution", None)
        self.__Execution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Execution5(self):
        return self.__Execution5

    @Execution5.setter
    def Execution5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_Execution__Execution5", None)
        self.__Execution5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

class executionTrace_ExecutionTrace:

    def __init__(self, totalExecutionTimeMsec: str, description: str, totalExecutionTime: str, executionTrace_ExecutionTrace: set["executionTrace_Execution"] = None):
        self.totalExecutionTimeMsec = totalExecutionTimeMsec
        self.description = description
        self.totalExecutionTime = totalExecutionTime
        self.executionTrace_ExecutionTrace = executionTrace_ExecutionTrace if executionTrace_ExecutionTrace is not None else set()
        
    @property
    def totalExecutionTime(self) -> str:
        return self.__totalExecutionTime

    @totalExecutionTime.setter
    def totalExecutionTime(self, totalExecutionTime: str):
        self.__totalExecutionTime = totalExecutionTime

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def totalExecutionTimeMsec(self) -> str:
        return self.__totalExecutionTimeMsec

    @totalExecutionTimeMsec.setter
    def totalExecutionTimeMsec(self, totalExecutionTimeMsec: str):
        self.__totalExecutionTimeMsec = totalExecutionTimeMsec

    @property
    def executionTrace_ExecutionTrace(self):
        return self.__executionTrace_ExecutionTrace

    @executionTrace_ExecutionTrace.setter
    def executionTrace_ExecutionTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executionTrace_ExecutionTrace__executionTrace_ExecutionTrace", None)
        self.__executionTrace_ExecutionTrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "executionTrace_Execution"):
                    opp_val = getattr(item, "executionTrace_Execution", None)
                    
                    if opp_val == self:
                        setattr(item, "executionTrace_Execution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "executionTrace_Execution"):
                    opp_val = getattr(item, "executionTrace_Execution", None)
                    
                    setattr(item, "executionTrace_Execution", self)
                    

class executionTrace_MapEntry:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

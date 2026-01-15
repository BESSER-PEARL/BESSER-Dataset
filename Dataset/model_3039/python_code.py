from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DependentAction:

    pass
class actions_GetPropertyAction(DependentAction):

    pass
class DataElement:

    pass
class FeatureVersion:

    pass
class ITimeConsumer:

    pass
class DataLeaf:

    pass
class IFeature:

    pass
class IArithmetricFunction:

    pass
class DataBag:

    pass
class IDataNodeFunction:

    pass
class IValueFunction:

    pass
class actions_Term:

    pass
class ReconfigurationAction:

    pass
class actions_RemoveBagAction(ReconfigurationAction):

    pass
class actions_SetDataAction(ReconfigurationAction):

    pass
class PostGenerationAction:

    pass
class actions_DeactivateFeatureAction(PostGenerationAction, ReconfigurationAction):

    pass
class actions_ActivateFeatureAction(PostGenerationAction, ReconfigurationAction):

    pass
class actions_SetPropertyAction(PostGenerationAction):

    pass
class actions_DependentAction(PostGenerationAction):

    pass
class actions_PostGenerationSequence(PostGenerationAction):

    pass
class Action:

    pass
class actions_PostGenerationAction(Action):

    pass
class PreGenerationAction:

    pass
class actions_PreGenerationSequence(PreGenerationAction):

    pass
class actions_ReconfigurationAction(PreGenerationAction):

    pass
class actions_TermAction(PreGenerationAction, PostGenerationAction, ReconfigurationAction):

    pass
class actions_GetDataAction(PreGenerationAction):

    pass
class actions_FailAction(PreGenerationAction, PostGenerationAction):

    pass
class actions_ThrowAction(PreGenerationAction):

    def __init__(self, eventID: str):
        self.eventID = eventID
        
    @property
    def eventID(self) -> str:
        return self.__eventID

    @eventID.setter
    def eventID(self, eventID: str):
        self.__eventID = eventID

class actions_GetRealTimeAction(PreGenerationAction, DependentAction):

    def __init__(self, timeHint: str):
        self.timeHint = timeHint
        
    @property
    def timeHint(self) -> str:
        return self.__timeHint

    @timeHint.setter
    def timeHint(self, timeHint: str):
        self.__timeHint = timeHint

class actions_TimeAction(PreGenerationAction):

    def __init__(self, time: int, actions_TimeAction: "ITimeConsumer" = None):
        self.time = time
        self.actions_TimeAction = actions_TimeAction
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def actions_TimeAction(self):
        return self.__actions_TimeAction

    @actions_TimeAction.setter
    def actions_TimeAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_TimeAction__actions_TimeAction", None)
        self.__actions_TimeAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ITimeConsumer"):
                opp_val = getattr(old_value, "ITimeConsumer", None)
                if opp_val == self:
                    setattr(old_value, "ITimeConsumer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ITimeConsumer"):
                opp_val = getattr(value, "ITimeConsumer", None)
                setattr(value, "ITimeConsumer", self)

class actions_GetFeatureStateAction(PreGenerationAction, DependentAction):

    pass
class ILogicFunction:

    pass
class rules_IRealTimeConsumer:

    pass
class IContextVariable:

    pass
class actions_PreGenerationAction(Action):

    pass
class core_ITopLevelElement:

    pass
class core_AbstractModelElement:

    pass
class actions_TimedConditionAction(core_ITopLevelElement, core_AbstractModelElement, rules_IRealTimeConsumer):

    def __init__(self, frequency: int, actions_TimedConditionAction: "actions_PreGenerationAction" = None, actions_TimedConditionAction10: "ILogicFunction" = None):
        self.frequency = frequency
        self.actions_TimedConditionAction = actions_TimedConditionAction
        self.actions_TimedConditionAction10 = actions_TimedConditionAction10
        
    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: int):
        self.__frequency = frequency

    @property
    def actions_TimedConditionAction(self):
        return self.__actions_TimedConditionAction

    @actions_TimedConditionAction.setter
    def actions_TimedConditionAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_TimedConditionAction__actions_TimedConditionAction", None)
        self.__actions_TimedConditionAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions_PreGenerationAction8"):
                opp_val = getattr(old_value, "actions_PreGenerationAction8", None)
                if opp_val == self:
                    setattr(old_value, "actions_PreGenerationAction8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions_PreGenerationAction8"):
                opp_val = getattr(value, "actions_PreGenerationAction8", None)
                setattr(value, "actions_PreGenerationAction8", self)

    @property
    def actions_TimedConditionAction10(self):
        return self.__actions_TimedConditionAction10

    @actions_TimedConditionAction10.setter
    def actions_TimedConditionAction10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actions_TimedConditionAction__actions_TimedConditionAction10", None)
        self.__actions_TimedConditionAction10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ILogicFunction"):
                opp_val = getattr(old_value, "ILogicFunction", None)
                if opp_val == self:
                    setattr(old_value, "ILogicFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ILogicFunction"):
                opp_val = getattr(value, "ILogicFunction", None)
                setattr(value, "ILogicFunction", self)

class actions_EObject:

    pass
class actions_StandAloneAction(core_ITopLevelElement, core_AbstractModelElement):

    pass
class actions_ActionReference(PreGenerationAction):

    pass
class actions_Action(ABC):

    pass
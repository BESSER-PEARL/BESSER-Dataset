from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class call_CallSource1:

    pass
class actionstep_ParameterizedInitiator:

    pass
class actionpak1_IncomingCall2(call_CallSource1, actionstep_ParameterizedInitiator):

    def __init__(self, callName: str):
        self.callName = callName
        
    @property
    def callName(self) -> str:
        return self.__callName

    @callName.setter
    def callName(self, callName: str):
        self.__callName = callName

class ParameterizedInitiator:

    pass
class actionpak1_CustomInitiator(ParameterizedInitiator):

    pass
class DynamicValue:

    pass
class ActionStep:

    pass
class actionpak1_UnscheduleSaflet(ActionStep):

    pass
class actionpak1_ActionstepTest(ActionStep):

    pass
class ParameterizedActionstep:

    pass
class actionpak1_ScheduleSaflet(ParameterizedActionstep):

    pass
class actionpak1_InvokeSaflet2(ParameterizedActionstep):

    def __init__(self, labelText: str, actionpak1_InvokeSaflet2: "DynamicValue" = None):
        self.labelText = labelText
        self.actionpak1_InvokeSaflet2 = actionpak1_InvokeSaflet2
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def actionpak1_InvokeSaflet2(self):
        return self.__actionpak1_InvokeSaflet2

    @actionpak1_InvokeSaflet2.setter
    def actionpak1_InvokeSaflet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_actionpak1_InvokeSaflet2__actionpak1_InvokeSaflet2", None)
        self.__actionpak1_InvokeSaflet2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DynamicValue2"):
                opp_val = getattr(old_value, "DynamicValue2", None)
                if opp_val == self:
                    setattr(old_value, "DynamicValue2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DynamicValue2"):
                opp_val = getattr(value, "DynamicValue2", None)
                setattr(value, "DynamicValue2", self)

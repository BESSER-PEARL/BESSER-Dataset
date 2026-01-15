from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Trigger:

    pass
class StateMachine_TriggerExpression(Trigger):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class Guard:

    pass
class StateMachine_GuardExpression(Guard):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class Action:

    pass
class StateMachine_ActionExpression(Action):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class StateMachine_TurnoutDesiredDirection:

    pass
class StateMachine_RouteElement:

    pass
class StateMachine_TrackElement:

    pass
class StateMachine_Turnout:

    pass
class StateMachine_Signal:

    pass
class TriggerExpression:

    pass
class StateMachine_SignalAllowedSpeedChanged(TriggerExpression):

    def __init__(self, newAllowedSpeed: str, StateMachine_SignalAllowedSpeedChanged: "StateMachine_Signal" = None):
        self.newAllowedSpeed = newAllowedSpeed
        self.StateMachine_SignalAllowedSpeedChanged = StateMachine_SignalAllowedSpeedChanged
        
    @property
    def newAllowedSpeed(self) -> str:
        return self.__newAllowedSpeed

    @newAllowedSpeed.setter
    def newAllowedSpeed(self, newAllowedSpeed: str):
        self.__newAllowedSpeed = newAllowedSpeed

    @property
    def StateMachine_SignalAllowedSpeedChanged(self):
        return self.__StateMachine_SignalAllowedSpeedChanged

    @StateMachine_SignalAllowedSpeedChanged.setter
    def StateMachine_SignalAllowedSpeedChanged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_SignalAllowedSpeedChanged__StateMachine_SignalAllowedSpeedChanged", None)
        self.__StateMachine_SignalAllowedSpeedChanged = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Signal59"):
                opp_val = getattr(old_value, "StateMachine_Signal59", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Signal59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Signal59"):
                opp_val = getattr(value, "StateMachine_Signal59", None)
                setattr(value, "StateMachine_Signal59", self)

class StateMachine_TrainTrackElementChanged(TriggerExpression):

    pass
class StateMachine_TurnoutDirectionChanged(TriggerExpression):

    def __init__(self, newTurnoutDirection: str, StateMachine_TurnoutDirectionChanged: "StateMachine_Turnout" = None):
        self.newTurnoutDirection = newTurnoutDirection
        self.StateMachine_TurnoutDirectionChanged = StateMachine_TurnoutDirectionChanged
        
    @property
    def newTurnoutDirection(self) -> str:
        return self.__newTurnoutDirection

    @newTurnoutDirection.setter
    def newTurnoutDirection(self, newTurnoutDirection: str):
        self.__newTurnoutDirection = newTurnoutDirection

    @property
    def StateMachine_TurnoutDirectionChanged(self):
        return self.__StateMachine_TurnoutDirectionChanged

    @StateMachine_TurnoutDirectionChanged.setter
    def StateMachine_TurnoutDirectionChanged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_TurnoutDirectionChanged__StateMachine_TurnoutDirectionChanged", None)
        self.__StateMachine_TurnoutDirectionChanged = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Turnout61"):
                opp_val = getattr(old_value, "StateMachine_Turnout61", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Turnout61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Turnout61"):
                opp_val = getattr(value, "StateMachine_Turnout61", None)
                setattr(value, "StateMachine_Turnout61", self)

class StateMachine_TrainHeadingSpeedChanged(TriggerExpression):

    def __init__(self, newHeadingSpeed: str, StateMachine_TrainHeadingSpeedChanged: "StateMachine_Train" = None):
        self.newHeadingSpeed = newHeadingSpeed
        self.StateMachine_TrainHeadingSpeedChanged = StateMachine_TrainHeadingSpeedChanged
        
    @property
    def newHeadingSpeed(self) -> str:
        return self.__newHeadingSpeed

    @newHeadingSpeed.setter
    def newHeadingSpeed(self, newHeadingSpeed: str):
        self.__newHeadingSpeed = newHeadingSpeed

    @property
    def StateMachine_TrainHeadingSpeedChanged(self):
        return self.__StateMachine_TrainHeadingSpeedChanged

    @StateMachine_TrainHeadingSpeedChanged.setter
    def StateMachine_TrainHeadingSpeedChanged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_TrainHeadingSpeedChanged__StateMachine_TrainHeadingSpeedChanged", None)
        self.__StateMachine_TrainHeadingSpeedChanged = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Train52"):
                opp_val = getattr(old_value, "StateMachine_Train52", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Train52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Train52"):
                opp_val = getattr(value, "StateMachine_Train52", None)
                setattr(value, "StateMachine_Train52", self)

class StateMachine_Train:

    pass
class ActionExpression:

    pass
class StateMachine_ChangeTurnoutDirection(ActionExpression):

    def __init__(self, newTurnoutDirection: str, StateMachine_ChangeTurnoutDirection: "StateMachine_Turnout" = None):
        self.newTurnoutDirection = newTurnoutDirection
        self.StateMachine_ChangeTurnoutDirection = StateMachine_ChangeTurnoutDirection
        
    @property
    def newTurnoutDirection(self) -> str:
        return self.__newTurnoutDirection

    @newTurnoutDirection.setter
    def newTurnoutDirection(self, newTurnoutDirection: str):
        self.__newTurnoutDirection = newTurnoutDirection

    @property
    def StateMachine_ChangeTurnoutDirection(self):
        return self.__StateMachine_ChangeTurnoutDirection

    @StateMachine_ChangeTurnoutDirection.setter
    def StateMachine_ChangeTurnoutDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_ChangeTurnoutDirection__StateMachine_ChangeTurnoutDirection", None)
        self.__StateMachine_ChangeTurnoutDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Turnout"):
                opp_val = getattr(old_value, "StateMachine_Turnout", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Turnout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Turnout"):
                opp_val = getattr(value, "StateMachine_Turnout", None)
                setattr(value, "StateMachine_Turnout", self)

class StateMachine_ChangeTrainCurrentTrackElement(ActionExpression):

    pass
class StateMachine_ChangeSignalAllowedSpeed(ActionExpression):

    def __init__(self, newAllowedSpeed: str, StateMachine_ChangeSignalAllowedSpeed: "StateMachine_Signal" = None):
        self.newAllowedSpeed = newAllowedSpeed
        self.StateMachine_ChangeSignalAllowedSpeed = StateMachine_ChangeSignalAllowedSpeed
        
    @property
    def newAllowedSpeed(self) -> str:
        return self.__newAllowedSpeed

    @newAllowedSpeed.setter
    def newAllowedSpeed(self, newAllowedSpeed: str):
        self.__newAllowedSpeed = newAllowedSpeed

    @property
    def StateMachine_ChangeSignalAllowedSpeed(self):
        return self.__StateMachine_ChangeSignalAllowedSpeed

    @StateMachine_ChangeSignalAllowedSpeed.setter
    def StateMachine_ChangeSignalAllowedSpeed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_ChangeSignalAllowedSpeed__StateMachine_ChangeSignalAllowedSpeed", None)
        self.__StateMachine_ChangeSignalAllowedSpeed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Signal"):
                opp_val = getattr(old_value, "StateMachine_Signal", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Signal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Signal"):
                opp_val = getattr(value, "StateMachine_Signal", None)
                setattr(value, "StateMachine_Signal", self)

class StateMachine_ChangeTrainHeadingSpeed(ActionExpression):

    def __init__(self, newHeadingSpeed: str, StateMachine_ChangeTrainHeadingSpeed: "StateMachine_Train" = None):
        self.newHeadingSpeed = newHeadingSpeed
        self.StateMachine_ChangeTrainHeadingSpeed = StateMachine_ChangeTrainHeadingSpeed
        
    @property
    def newHeadingSpeed(self) -> str:
        return self.__newHeadingSpeed

    @newHeadingSpeed.setter
    def newHeadingSpeed(self, newHeadingSpeed: str):
        self.__newHeadingSpeed = newHeadingSpeed

    @property
    def StateMachine_ChangeTrainHeadingSpeed(self):
        return self.__StateMachine_ChangeTrainHeadingSpeed

    @StateMachine_ChangeTrainHeadingSpeed.setter
    def StateMachine_ChangeTrainHeadingSpeed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_ChangeTrainHeadingSpeed__StateMachine_ChangeTrainHeadingSpeed", None)
        self.__StateMachine_ChangeTrainHeadingSpeed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Train"):
                opp_val = getattr(old_value, "StateMachine_Train", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Train", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Train"):
                opp_val = getattr(value, "StateMachine_Train", None)
                setattr(value, "StateMachine_Train", self)

class StateMachine_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class GuardExpression:

    pass
class StateMachine_TrainCurrentHeadingSpeed(GuardExpression):

    def __init__(self, currentHeadingSpeed: str, StateMachine_TrainCurrentHeadingSpeed: "StateMachine_Train" = None):
        self.currentHeadingSpeed = currentHeadingSpeed
        self.StateMachine_TrainCurrentHeadingSpeed = StateMachine_TrainCurrentHeadingSpeed
        
    @property
    def currentHeadingSpeed(self) -> str:
        return self.__currentHeadingSpeed

    @currentHeadingSpeed.setter
    def currentHeadingSpeed(self, currentHeadingSpeed: str):
        self.__currentHeadingSpeed = currentHeadingSpeed

    @property
    def StateMachine_TrainCurrentHeadingSpeed(self):
        return self.__StateMachine_TrainCurrentHeadingSpeed

    @StateMachine_TrainCurrentHeadingSpeed.setter
    def StateMachine_TrainCurrentHeadingSpeed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_TrainCurrentHeadingSpeed__StateMachine_TrainCurrentHeadingSpeed", None)
        self.__StateMachine_TrainCurrentHeadingSpeed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Train41"):
                opp_val = getattr(old_value, "StateMachine_Train41", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Train41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Train41"):
                opp_val = getattr(value, "StateMachine_Train41", None)
                setattr(value, "StateMachine_Train41", self)

class StateMachine_SignalCurrentAllowedSpeed(GuardExpression):

    def __init__(self, currentAllowedSpeed: str, StateMachine_SignalCurrentAllowedSpeed: "StateMachine_Signal" = None):
        self.currentAllowedSpeed = currentAllowedSpeed
        self.StateMachine_SignalCurrentAllowedSpeed = StateMachine_SignalCurrentAllowedSpeed
        
    @property
    def currentAllowedSpeed(self) -> str:
        return self.__currentAllowedSpeed

    @currentAllowedSpeed.setter
    def currentAllowedSpeed(self, currentAllowedSpeed: str):
        self.__currentAllowedSpeed = currentAllowedSpeed

    @property
    def StateMachine_SignalCurrentAllowedSpeed(self):
        return self.__StateMachine_SignalCurrentAllowedSpeed

    @StateMachine_SignalCurrentAllowedSpeed.setter
    def StateMachine_SignalCurrentAllowedSpeed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_SignalCurrentAllowedSpeed__StateMachine_SignalCurrentAllowedSpeed", None)
        self.__StateMachine_SignalCurrentAllowedSpeed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Signal50"):
                opp_val = getattr(old_value, "StateMachine_Signal50", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Signal50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Signal50"):
                opp_val = getattr(value, "StateMachine_Signal50", None)
                setattr(value, "StateMachine_Signal50", self)

class StateMachine_TurnoutCurrentDirection(GuardExpression):

    def __init__(self, currentTurnoutDirection: str, StateMachine_TurnoutCurrentDirection: "StateMachine_Turnout" = None):
        self.currentTurnoutDirection = currentTurnoutDirection
        self.StateMachine_TurnoutCurrentDirection = StateMachine_TurnoutCurrentDirection
        
    @property
    def currentTurnoutDirection(self) -> str:
        return self.__currentTurnoutDirection

    @currentTurnoutDirection.setter
    def currentTurnoutDirection(self, currentTurnoutDirection: str):
        self.__currentTurnoutDirection = currentTurnoutDirection

    @property
    def StateMachine_TurnoutCurrentDirection(self):
        return self.__StateMachine_TurnoutCurrentDirection

    @StateMachine_TurnoutCurrentDirection.setter
    def StateMachine_TurnoutCurrentDirection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_TurnoutCurrentDirection__StateMachine_TurnoutCurrentDirection", None)
        self.__StateMachine_TurnoutCurrentDirection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Turnout48"):
                opp_val = getattr(old_value, "StateMachine_Turnout48", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Turnout48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Turnout48"):
                opp_val = getattr(value, "StateMachine_Turnout48", None)
                setattr(value, "StateMachine_Turnout48", self)

class StateMachine_TrainCurrentlyStandsOn(GuardExpression):

    pass
class StateMachine_TurnoutHasDesiredDirection(GuardExpression):

    pass
class StateMachine_NextTrackElementIs(GuardExpression):

    pass
class StateMachine_RDMElement:

    pass
class State:

    pass
class StateMachine_CompositeState(State):

    pass
class NamedElement:

    pass
class StateMachine_State(NamedElement):

    def __init__(self, isInitial: bool, isActive: bool, StateMachine_State: "StateMachine_StateMachine" = None, StateMachine_State13: "StateMachine_StateMachine" = None, sourceState: set["StateMachine_Transition"] = None, targetState: set["StateMachine_Transition"] = None, State: "StateMachine_Transition" = None, State21: "StateMachine_Transition" = None):
        self.isInitial = isInitial
        self.isActive = isActive
        self.StateMachine_State = StateMachine_State
        self.StateMachine_State13 = StateMachine_State13
        self.sourceState = sourceState if sourceState is not None else set()
        self.targetState = targetState if targetState is not None else set()
        self.State = State
        self.State21 = State21
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def State21(self):
        return self.__State21

    @State21.setter
    def State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__State21", None)
        self.__State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def StateMachine_State(self):
        return self.__StateMachine_State

    @StateMachine_State.setter
    def StateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State", None)
        self.__StateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine2"):
                opp_val = getattr(old_value, "StateMachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine2"):
                opp_val = getattr(value, "StateMachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "StateMachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sourceState(self):
        return self.__sourceState

    @sourceState.setter
    def sourceState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__sourceState", None)
        self.__sourceState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def targetState(self):
        return self.__targetState

    @targetState.setter
    def targetState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__targetState", None)
        self.__targetState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    setattr(item, "Transition18", self)
                    

    @property
    def StateMachine_State13(self):
        return self.__StateMachine_State13

    @StateMachine_State13.setter
    def StateMachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State13", None)
        self.__StateMachine_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine12"):
                opp_val = getattr(old_value, "StateMachine_StateMachine12", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_StateMachine12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine12"):
                opp_val = getattr(value, "StateMachine_StateMachine12", None)
                setattr(value, "StateMachine_StateMachine12", self)

class StateMachine_Trigger(NamedElement):

    pass
class StateMachine_Transition(NamedElement):

    def __init__(self, isFireable: bool, isEnabled: bool, StateMachine_Transition: "StateMachine_StateMachine" = None, Transition: "StateMachine_State" = None, Transition18: "StateMachine_State" = None, outgoingTransitions: "StateMachine_State" = None, incomingTransitions: "StateMachine_State" = None, StateMachine_Transition23: "StateMachine_Trigger" = None, StateMachine_Transition26: set["StateMachine_Guard"] = None, StateMachine_Transition29: set["StateMachine_Action"] = None):
        self.isFireable = isFireable
        self.isEnabled = isEnabled
        self.StateMachine_Transition = StateMachine_Transition
        self.Transition = Transition
        self.Transition18 = Transition18
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.StateMachine_Transition23 = StateMachine_Transition23
        self.StateMachine_Transition26 = StateMachine_Transition26 if StateMachine_Transition26 is not None else set()
        self.StateMachine_Transition29 = StateMachine_Transition29 if StateMachine_Transition29 is not None else set()
        
    @property
    def isEnabled(self) -> bool:
        return self.__isEnabled

    @isEnabled.setter
    def isEnabled(self, isEnabled: bool):
        self.__isEnabled = isEnabled

    @property
    def isFireable(self) -> bool:
        return self.__isFireable

    @isFireable.setter
    def isFireable(self, isFireable: bool):
        self.__isFireable = isFireable

    @property
    def StateMachine_Transition29(self):
        return self.__StateMachine_Transition29

    @StateMachine_Transition29.setter
    def StateMachine_Transition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition29", None)
        self.__StateMachine_Transition29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Action30"):
                    opp_val = getattr(item, "StateMachine_Action30", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Action30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Action30"):
                    opp_val = getattr(item, "StateMachine_Action30", None)
                    
                    setattr(item, "StateMachine_Action30", self)
                    

    @property
    def StateMachine_Transition26(self):
        return self.__StateMachine_Transition26

    @StateMachine_Transition26.setter
    def StateMachine_Transition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition26", None)
        self.__StateMachine_Transition26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Guard27"):
                    opp_val = getattr(item, "StateMachine_Guard27", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Guard27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Guard27"):
                    opp_val = getattr(item, "StateMachine_Guard27", None)
                    
                    setattr(item, "StateMachine_Guard27", self)
                    

    @property
    def Transition18(self):
        return self.__Transition18

    @Transition18.setter
    def Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition18", None)
        self.__Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetState"):
                opp_val = getattr(old_value, "targetState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetState"):
                opp_val = getattr(value, "targetState", None)
                if opp_val is None:
                    setattr(value, "targetState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Transition23(self):
        return self.__StateMachine_Transition23

    @StateMachine_Transition23.setter
    def StateMachine_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition23", None)
        self.__StateMachine_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Trigger24"):
                opp_val = getattr(old_value, "StateMachine_Trigger24", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Trigger24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Trigger24"):
                opp_val = getattr(value, "StateMachine_Trigger24", None)
                setattr(value, "StateMachine_Trigger24", self)

    @property
    def StateMachine_Transition(self):
        return self.__StateMachine_Transition

    @StateMachine_Transition.setter
    def StateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition", None)
        self.__StateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine4"):
                opp_val = getattr(old_value, "StateMachine_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine4"):
                opp_val = getattr(value, "StateMachine_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "StateMachine_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceState"):
                opp_val = getattr(old_value, "sourceState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceState"):
                opp_val = getattr(value, "sourceState", None)
                if opp_val is None:
                    setattr(value, "sourceState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State21"):
                opp_val = getattr(old_value, "State21", None)
                if opp_val == self:
                    setattr(old_value, "State21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State21"):
                opp_val = getattr(value, "State21", None)
                setattr(value, "State21", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

class StateMachine_Guard(NamedElement):

    pass
class StateMachine_Action(NamedElement):

    pass
class StateMachine_StateMachine(NamedElement):

    pass
class StateMachine_StateMachineBehavioralModel:

    pass
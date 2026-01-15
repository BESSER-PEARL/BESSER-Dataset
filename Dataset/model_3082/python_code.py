from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class reqLanguage_Time:

    def __init__(self, value: int, timeUnit: str, reqLanguage_Time: "reqLanguage_TimingConstraint" = None):
        self.value = value
        self.timeUnit = timeUnit
        self.reqLanguage_Time = reqLanguage_Time
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def reqLanguage_Time(self):
        return self.__reqLanguage_Time

    @reqLanguage_Time.setter
    def reqLanguage_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Time__reqLanguage_Time", None)
        self.__reqLanguage_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_TimingConstraint88"):
                opp_val = getattr(old_value, "reqLanguage_TimingConstraint88", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_TimingConstraint88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_TimingConstraint88"):
                opp_val = getattr(value, "reqLanguage_TimingConstraint88", None)
                setattr(value, "reqLanguage_TimingConstraint88", self)

class reqLanguage_User:

    def __init__(self, user: str, name: str):
        self.user = user
        self.name = name
        
    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class reqLanguage_Actor:

    def __init__(self, actor: str, name: str):
        self.actor = actor
        self.name = name
        
    @property
    def actor(self) -> str:
        return self.__actor

    @actor.setter
    def actor(self, actor: str):
        self.__actor = actor

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class reqLanguage_NoTransition:

    pass
class reqLanguage_OutTransition:

    pass
class reqLanguage_Transition:

    pass
class reqLanguage_Function:

    def __init__(self, name: str, type: str, function: str, reqLanguage_Function: "reqLanguage_MainFunctions" = None):
        self.name = name
        self.type = type
        self.function = function
        self.reqLanguage_Function = reqLanguage_Function
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def reqLanguage_Function(self):
        return self.__reqLanguage_Function

    @reqLanguage_Function.setter
    def reqLanguage_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Function__reqLanguage_Function", None)
        self.__reqLanguage_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainFunctions68"):
                opp_val = getattr(old_value, "reqLanguage_MainFunctions68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainFunctions68"):
                opp_val = getattr(value, "reqLanguage_MainFunctions68", None)
                if opp_val is None:
                    setattr(value, "reqLanguage_MainFunctions68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reqLanguage_MainFunctions:

    pass
class reqLanguage_MainStateTransition:

    pass
class reqLanguage_Attribute:

    def __init__(self, attribute: str, name: str, type: str, reqLanguage_Attribute: "reqLanguage_MainAttributes" = None):
        self.attribute = attribute
        self.name = name
        self.type = type
        self.reqLanguage_Attribute = reqLanguage_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def reqLanguage_Attribute(self):
        return self.__reqLanguage_Attribute

    @reqLanguage_Attribute.setter
    def reqLanguage_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Attribute__reqLanguage_Attribute", None)
        self.__reqLanguage_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainAttributes64"):
                opp_val = getattr(old_value, "reqLanguage_MainAttributes64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainAttributes64"):
                opp_val = getattr(value, "reqLanguage_MainAttributes64", None)
                if opp_val is None:
                    setattr(value, "reqLanguage_MainAttributes64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reqLanguage_MainAttributes:

    pass
class reqLanguage_MainComposition:

    pass
class reqLanguage_Action:

    def __init__(self, action: str, name: str, reqLanguage_Action60: "reqLanguage_MainStateTransition" = None, reqLanguage_Action: "reqLanguage_MainFunction" = None, reqLanguage_Action79: "reqLanguage_Parameter" = None, reqLanguage_Action82: "reqLanguage_Value" = None, reqLanguage_Action85: "reqLanguage_EObject" = None):
        self.action = action
        self.name = name
        self.reqLanguage_Action60 = reqLanguage_Action60
        self.reqLanguage_Action = reqLanguage_Action
        self.reqLanguage_Action79 = reqLanguage_Action79
        self.reqLanguage_Action82 = reqLanguage_Action82
        self.reqLanguage_Action85 = reqLanguage_Action85
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reqLanguage_Action(self):
        return self.__reqLanguage_Action

    @reqLanguage_Action.setter
    def reqLanguage_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Action__reqLanguage_Action", None)
        self.__reqLanguage_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainFunction47"):
                opp_val = getattr(old_value, "reqLanguage_MainFunction47", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainFunction47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainFunction47"):
                opp_val = getattr(value, "reqLanguage_MainFunction47", None)
                setattr(value, "reqLanguage_MainFunction47", self)

    @property
    def reqLanguage_Action79(self):
        return self.__reqLanguage_Action79

    @reqLanguage_Action79.setter
    def reqLanguage_Action79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Action__reqLanguage_Action79", None)
        self.__reqLanguage_Action79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Parameter80"):
                opp_val = getattr(old_value, "reqLanguage_Parameter80", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Parameter80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Parameter80"):
                opp_val = getattr(value, "reqLanguage_Parameter80", None)
                setattr(value, "reqLanguage_Parameter80", self)

    @property
    def reqLanguage_Action85(self):
        return self.__reqLanguage_Action85

    @reqLanguage_Action85.setter
    def reqLanguage_Action85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Action__reqLanguage_Action85", None)
        self.__reqLanguage_Action85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject86"):
                opp_val = getattr(old_value, "reqLanguage_EObject86", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject86"):
                opp_val = getattr(value, "reqLanguage_EObject86", None)
                setattr(value, "reqLanguage_EObject86", self)

    @property
    def reqLanguage_Action60(self):
        return self.__reqLanguage_Action60

    @reqLanguage_Action60.setter
    def reqLanguage_Action60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Action__reqLanguage_Action60", None)
        self.__reqLanguage_Action60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainStateTransition59"):
                opp_val = getattr(old_value, "reqLanguage_MainStateTransition59", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainStateTransition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainStateTransition59"):
                opp_val = getattr(value, "reqLanguage_MainStateTransition59", None)
                setattr(value, "reqLanguage_MainStateTransition59", self)

    @property
    def reqLanguage_Action82(self):
        return self.__reqLanguage_Action82

    @reqLanguage_Action82.setter
    def reqLanguage_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Action__reqLanguage_Action82", None)
        self.__reqLanguage_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Value83"):
                opp_val = getattr(old_value, "reqLanguage_Value83", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Value83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Value83"):
                opp_val = getattr(value, "reqLanguage_Value83", None)
                setattr(value, "reqLanguage_Value83", self)

class reqLanguage_Parameter:

    def __init__(self, parameter: str, name: str, reqLanguage_Parameter40: "reqLanguage_ParameterState" = None, reqLanguage_Parameter: "reqLanguage_ActorEvent" = None, reqLanguage_Parameter80: "reqLanguage_Action" = None):
        self.parameter = parameter
        self.name = name
        self.reqLanguage_Parameter40 = reqLanguage_Parameter40
        self.reqLanguage_Parameter = reqLanguage_Parameter
        self.reqLanguage_Parameter80 = reqLanguage_Parameter80
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reqLanguage_Parameter40(self):
        return self.__reqLanguage_Parameter40

    @reqLanguage_Parameter40.setter
    def reqLanguage_Parameter40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Parameter__reqLanguage_Parameter40", None)
        self.__reqLanguage_Parameter40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_ParameterState"):
                opp_val = getattr(old_value, "reqLanguage_ParameterState", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_ParameterState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_ParameterState"):
                opp_val = getattr(value, "reqLanguage_ParameterState", None)
                setattr(value, "reqLanguage_ParameterState", self)

    @property
    def reqLanguage_Parameter(self):
        return self.__reqLanguage_Parameter

    @reqLanguage_Parameter.setter
    def reqLanguage_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Parameter__reqLanguage_Parameter", None)
        self.__reqLanguage_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_ActorEvent35"):
                opp_val = getattr(old_value, "reqLanguage_ActorEvent35", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_ActorEvent35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_ActorEvent35"):
                opp_val = getattr(value, "reqLanguage_ActorEvent35", None)
                setattr(value, "reqLanguage_ActorEvent35", self)

    @property
    def reqLanguage_Parameter80(self):
        return self.__reqLanguage_Parameter80

    @reqLanguage_Parameter80.setter
    def reqLanguage_Parameter80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Parameter__reqLanguage_Parameter80", None)
        self.__reqLanguage_Parameter80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Action79"):
                opp_val = getattr(old_value, "reqLanguage_Action79", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Action79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Action79"):
                opp_val = getattr(value, "reqLanguage_Action79", None)
                setattr(value, "reqLanguage_Action79", self)

class reqLanguage_ActorEvent:

    def __init__(self, action: str, reqLanguage_ActorEvent: "reqLanguage_EObject" = None, reqLanguage_ActorEvent35: "reqLanguage_Parameter" = None):
        self.action = action
        self.reqLanguage_ActorEvent = reqLanguage_ActorEvent
        self.reqLanguage_ActorEvent35 = reqLanguage_ActorEvent35
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def reqLanguage_ActorEvent35(self):
        return self.__reqLanguage_ActorEvent35

    @reqLanguage_ActorEvent35.setter
    def reqLanguage_ActorEvent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_ActorEvent__reqLanguage_ActorEvent35", None)
        self.__reqLanguage_ActorEvent35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Parameter"):
                opp_val = getattr(old_value, "reqLanguage_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Parameter"):
                opp_val = getattr(value, "reqLanguage_Parameter", None)
                setattr(value, "reqLanguage_Parameter", self)

    @property
    def reqLanguage_ActorEvent(self):
        return self.__reqLanguage_ActorEvent

    @reqLanguage_ActorEvent.setter
    def reqLanguage_ActorEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_ActorEvent__reqLanguage_ActorEvent", None)
        self.__reqLanguage_ActorEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject33"):
                opp_val = getattr(old_value, "reqLanguage_EObject33", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject33"):
                opp_val = getattr(value, "reqLanguage_EObject33", None)
                setattr(value, "reqLanguage_EObject33", self)

class reqLanguage_MainFunction:

    pass
class reqLanguage_ParameterState:

    pass
class reqLanguage_State:

    def __init__(self, state: str, name: str, reqLanguage_State: "reqLanguage_StateEvent" = None):
        self.state = state
        self.name = name
        self.reqLanguage_State = reqLanguage_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def reqLanguage_State(self):
        return self.__reqLanguage_State

    @reqLanguage_State.setter
    def reqLanguage_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_State__reqLanguage_State", None)
        self.__reqLanguage_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_StateEvent38"):
                opp_val = getattr(old_value, "reqLanguage_StateEvent38", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_StateEvent38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_StateEvent38"):
                opp_val = getattr(value, "reqLanguage_StateEvent38", None)
                setattr(value, "reqLanguage_StateEvent38", self)

class reqLanguage_System:

    def __init__(self, system: str, name: str, reqLanguage_System: "reqLanguage_StateEvent" = None, reqLanguage_System49: "reqLanguage_MainComposition" = None, reqLanguage_System62: "reqLanguage_MainAttributes" = None, reqLanguage_System52: "reqLanguage_MainComposition" = None, reqLanguage_System54: "reqLanguage_MainStateTransition" = None, reqLanguage_System66: "reqLanguage_MainFunctions" = None):
        self.system = system
        self.name = name
        self.reqLanguage_System = reqLanguage_System
        self.reqLanguage_System49 = reqLanguage_System49
        self.reqLanguage_System62 = reqLanguage_System62
        self.reqLanguage_System52 = reqLanguage_System52
        self.reqLanguage_System54 = reqLanguage_System54
        self.reqLanguage_System66 = reqLanguage_System66
        
    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reqLanguage_System49(self):
        return self.__reqLanguage_System49

    @reqLanguage_System49.setter
    def reqLanguage_System49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System49", None)
        self.__reqLanguage_System49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainComposition"):
                opp_val = getattr(old_value, "reqLanguage_MainComposition", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainComposition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainComposition"):
                opp_val = getattr(value, "reqLanguage_MainComposition", None)
                setattr(value, "reqLanguage_MainComposition", self)

    @property
    def reqLanguage_System(self):
        return self.__reqLanguage_System

    @reqLanguage_System.setter
    def reqLanguage_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System", None)
        self.__reqLanguage_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_StateEvent"):
                opp_val = getattr(old_value, "reqLanguage_StateEvent", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_StateEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_StateEvent"):
                opp_val = getattr(value, "reqLanguage_StateEvent", None)
                setattr(value, "reqLanguage_StateEvent", self)

    @property
    def reqLanguage_System52(self):
        return self.__reqLanguage_System52

    @reqLanguage_System52.setter
    def reqLanguage_System52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System52", None)
        self.__reqLanguage_System52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainComposition51"):
                opp_val = getattr(old_value, "reqLanguage_MainComposition51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainComposition51"):
                opp_val = getattr(value, "reqLanguage_MainComposition51", None)
                if opp_val is None:
                    setattr(value, "reqLanguage_MainComposition51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqLanguage_System62(self):
        return self.__reqLanguage_System62

    @reqLanguage_System62.setter
    def reqLanguage_System62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System62", None)
        self.__reqLanguage_System62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainAttributes"):
                opp_val = getattr(old_value, "reqLanguage_MainAttributes", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainAttributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainAttributes"):
                opp_val = getattr(value, "reqLanguage_MainAttributes", None)
                setattr(value, "reqLanguage_MainAttributes", self)

    @property
    def reqLanguage_System54(self):
        return self.__reqLanguage_System54

    @reqLanguage_System54.setter
    def reqLanguage_System54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System54", None)
        self.__reqLanguage_System54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainStateTransition"):
                opp_val = getattr(old_value, "reqLanguage_MainStateTransition", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainStateTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainStateTransition"):
                opp_val = getattr(value, "reqLanguage_MainStateTransition", None)
                setattr(value, "reqLanguage_MainStateTransition", self)

    @property
    def reqLanguage_System66(self):
        return self.__reqLanguage_System66

    @reqLanguage_System66.setter
    def reqLanguage_System66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_System__reqLanguage_System66", None)
        self.__reqLanguage_System66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_MainFunctions"):
                opp_val = getattr(old_value, "reqLanguage_MainFunctions", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_MainFunctions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_MainFunctions"):
                opp_val = getattr(value, "reqLanguage_MainFunctions", None)
                setattr(value, "reqLanguage_MainFunctions", self)

class reqLanguage_StateEvent:

    pass
class reqLanguage_PrefixCondition:

    def __init__(self, prefixFixedSyntax: str, reqLanguage_PrefixCondition: "reqLanguage_EObject" = None, reqLanguage_PrefixCondition20: "reqLanguage_Operator" = None, reqLanguage_PrefixCondition22: "reqLanguage_Value" = None, reqLanguage_PrefixCondition24: "reqLanguage_TimingConstraint" = None):
        self.prefixFixedSyntax = prefixFixedSyntax
        self.reqLanguage_PrefixCondition = reqLanguage_PrefixCondition
        self.reqLanguage_PrefixCondition20 = reqLanguage_PrefixCondition20
        self.reqLanguage_PrefixCondition22 = reqLanguage_PrefixCondition22
        self.reqLanguage_PrefixCondition24 = reqLanguage_PrefixCondition24
        
    @property
    def prefixFixedSyntax(self) -> str:
        return self.__prefixFixedSyntax

    @prefixFixedSyntax.setter
    def prefixFixedSyntax(self, prefixFixedSyntax: str):
        self.__prefixFixedSyntax = prefixFixedSyntax

    @property
    def reqLanguage_PrefixCondition24(self):
        return self.__reqLanguage_PrefixCondition24

    @reqLanguage_PrefixCondition24.setter
    def reqLanguage_PrefixCondition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixCondition__reqLanguage_PrefixCondition24", None)
        self.__reqLanguage_PrefixCondition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_TimingConstraint"):
                opp_val = getattr(old_value, "reqLanguage_TimingConstraint", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_TimingConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_TimingConstraint"):
                opp_val = getattr(value, "reqLanguage_TimingConstraint", None)
                setattr(value, "reqLanguage_TimingConstraint", self)

    @property
    def reqLanguage_PrefixCondition20(self):
        return self.__reqLanguage_PrefixCondition20

    @reqLanguage_PrefixCondition20.setter
    def reqLanguage_PrefixCondition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixCondition__reqLanguage_PrefixCondition20", None)
        self.__reqLanguage_PrefixCondition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Operator"):
                opp_val = getattr(old_value, "reqLanguage_Operator", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Operator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Operator"):
                opp_val = getattr(value, "reqLanguage_Operator", None)
                setattr(value, "reqLanguage_Operator", self)

    @property
    def reqLanguage_PrefixCondition(self):
        return self.__reqLanguage_PrefixCondition

    @reqLanguage_PrefixCondition.setter
    def reqLanguage_PrefixCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixCondition__reqLanguage_PrefixCondition", None)
        self.__reqLanguage_PrefixCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject18"):
                opp_val = getattr(old_value, "reqLanguage_EObject18", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject18"):
                opp_val = getattr(value, "reqLanguage_EObject18", None)
                setattr(value, "reqLanguage_EObject18", self)

    @property
    def reqLanguage_PrefixCondition22(self):
        return self.__reqLanguage_PrefixCondition22

    @reqLanguage_PrefixCondition22.setter
    def reqLanguage_PrefixCondition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixCondition__reqLanguage_PrefixCondition22", None)
        self.__reqLanguage_PrefixCondition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Value"):
                opp_val = getattr(old_value, "reqLanguage_Value", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Value"):
                opp_val = getattr(value, "reqLanguage_Value", None)
                setattr(value, "reqLanguage_Value", self)

class reqLanguage_PrefixState:

    def __init__(self, prefixFixedSyntax: str, reqLanguage_PrefixState: "reqLanguage_EObject" = None):
        self.prefixFixedSyntax = prefixFixedSyntax
        self.reqLanguage_PrefixState = reqLanguage_PrefixState
        
    @property
    def prefixFixedSyntax(self) -> str:
        return self.__prefixFixedSyntax

    @prefixFixedSyntax.setter
    def prefixFixedSyntax(self, prefixFixedSyntax: str):
        self.__prefixFixedSyntax = prefixFixedSyntax

    @property
    def reqLanguage_PrefixState(self):
        return self.__reqLanguage_PrefixState

    @reqLanguage_PrefixState.setter
    def reqLanguage_PrefixState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixState__reqLanguage_PrefixState", None)
        self.__reqLanguage_PrefixState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject16"):
                opp_val = getattr(old_value, "reqLanguage_EObject16", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject16"):
                opp_val = getattr(value, "reqLanguage_EObject16", None)
                setattr(value, "reqLanguage_EObject16", self)

class reqLanguage_PrefixRightOperand:

    def __init__(self, operator: str, reqLanguage_PrefixRightOperand: "reqLanguage_Prefix" = None, reqLanguage_PrefixRightOperand13: "reqLanguage_EObject" = None):
        self.operator = operator
        self.reqLanguage_PrefixRightOperand = reqLanguage_PrefixRightOperand
        self.reqLanguage_PrefixRightOperand13 = reqLanguage_PrefixRightOperand13
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def reqLanguage_PrefixRightOperand(self):
        return self.__reqLanguage_PrefixRightOperand

    @reqLanguage_PrefixRightOperand.setter
    def reqLanguage_PrefixRightOperand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixRightOperand__reqLanguage_PrefixRightOperand", None)
        self.__reqLanguage_PrefixRightOperand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Prefix11"):
                opp_val = getattr(old_value, "reqLanguage_Prefix11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Prefix11"):
                opp_val = getattr(value, "reqLanguage_Prefix11", None)
                if opp_val is None:
                    setattr(value, "reqLanguage_Prefix11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reqLanguage_PrefixRightOperand13(self):
        return self.__reqLanguage_PrefixRightOperand13

    @reqLanguage_PrefixRightOperand13.setter
    def reqLanguage_PrefixRightOperand13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixRightOperand__reqLanguage_PrefixRightOperand13", None)
        self.__reqLanguage_PrefixRightOperand13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject14"):
                opp_val = getattr(old_value, "reqLanguage_EObject14", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject14"):
                opp_val = getattr(value, "reqLanguage_EObject14", None)
                setattr(value, "reqLanguage_EObject14", self)

class reqLanguage_ParamEvent:

    def __init__(self, action: str, reqLanguage_ParamEvent: "reqLanguage_EObject" = None, reqLanguage_ParamEvent30: "reqLanguage_Value" = None):
        self.action = action
        self.reqLanguage_ParamEvent = reqLanguage_ParamEvent
        self.reqLanguage_ParamEvent30 = reqLanguage_ParamEvent30
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def reqLanguage_ParamEvent(self):
        return self.__reqLanguage_ParamEvent

    @reqLanguage_ParamEvent.setter
    def reqLanguage_ParamEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_ParamEvent__reqLanguage_ParamEvent", None)
        self.__reqLanguage_ParamEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject28"):
                opp_val = getattr(old_value, "reqLanguage_EObject28", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject28"):
                opp_val = getattr(value, "reqLanguage_EObject28", None)
                setattr(value, "reqLanguage_EObject28", self)

    @property
    def reqLanguage_ParamEvent30(self):
        return self.__reqLanguage_ParamEvent30

    @reqLanguage_ParamEvent30.setter
    def reqLanguage_ParamEvent30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_ParamEvent__reqLanguage_ParamEvent30", None)
        self.__reqLanguage_ParamEvent30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Value31"):
                opp_val = getattr(old_value, "reqLanguage_Value31", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Value31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Value31"):
                opp_val = getattr(value, "reqLanguage_Value31", None)
                setattr(value, "reqLanguage_Value31", self)

class reqLanguage_PrefixEvent:

    def __init__(self, prefixFixedSyntax: str, reqLanguage_PrefixEvent: "reqLanguage_EObject" = None):
        self.prefixFixedSyntax = prefixFixedSyntax
        self.reqLanguage_PrefixEvent = reqLanguage_PrefixEvent
        
    @property
    def prefixFixedSyntax(self) -> str:
        return self.__prefixFixedSyntax

    @prefixFixedSyntax.setter
    def prefixFixedSyntax(self, prefixFixedSyntax: str):
        self.__prefixFixedSyntax = prefixFixedSyntax

    @property
    def reqLanguage_PrefixEvent(self):
        return self.__reqLanguage_PrefixEvent

    @reqLanguage_PrefixEvent.setter
    def reqLanguage_PrefixEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_PrefixEvent__reqLanguage_PrefixEvent", None)
        self.__reqLanguage_PrefixEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_EObject26"):
                opp_val = getattr(old_value, "reqLanguage_EObject26", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_EObject26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_EObject26"):
                opp_val = getattr(value, "reqLanguage_EObject26", None)
                setattr(value, "reqLanguage_EObject26", self)

class reqLanguage_TimingConstraint:

    def __init__(self, timingConstraint: str, minmax: str, reqLanguage_TimingConstraint: "reqLanguage_PrefixCondition" = None, reqLanguage_TimingConstraint88: "reqLanguage_Time" = None):
        self.timingConstraint = timingConstraint
        self.minmax = minmax
        self.reqLanguage_TimingConstraint = reqLanguage_TimingConstraint
        self.reqLanguage_TimingConstraint88 = reqLanguage_TimingConstraint88
        
    @property
    def minmax(self) -> str:
        return self.__minmax

    @minmax.setter
    def minmax(self, minmax: str):
        self.__minmax = minmax

    @property
    def timingConstraint(self) -> str:
        return self.__timingConstraint

    @timingConstraint.setter
    def timingConstraint(self, timingConstraint: str):
        self.__timingConstraint = timingConstraint

    @property
    def reqLanguage_TimingConstraint88(self):
        return self.__reqLanguage_TimingConstraint88

    @reqLanguage_TimingConstraint88.setter
    def reqLanguage_TimingConstraint88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_TimingConstraint__reqLanguage_TimingConstraint88", None)
        self.__reqLanguage_TimingConstraint88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Time"):
                opp_val = getattr(old_value, "reqLanguage_Time", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Time", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Time"):
                opp_val = getattr(value, "reqLanguage_Time", None)
                setattr(value, "reqLanguage_Time", self)

    @property
    def reqLanguage_TimingConstraint(self):
        return self.__reqLanguage_TimingConstraint

    @reqLanguage_TimingConstraint.setter
    def reqLanguage_TimingConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_TimingConstraint__reqLanguage_TimingConstraint", None)
        self.__reqLanguage_TimingConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_PrefixCondition24"):
                opp_val = getattr(old_value, "reqLanguage_PrefixCondition24", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_PrefixCondition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_PrefixCondition24"):
                opp_val = getattr(value, "reqLanguage_PrefixCondition24", None)
                setattr(value, "reqLanguage_PrefixCondition24", self)

class reqLanguage_Value:

    def __init__(self, val: str, value: int, reqLanguage_Value: "reqLanguage_PrefixCondition" = None, reqLanguage_Value31: "reqLanguage_ParamEvent" = None, reqLanguage_Value83: "reqLanguage_Action" = None):
        self.val = val
        self.value = value
        self.reqLanguage_Value = reqLanguage_Value
        self.reqLanguage_Value31 = reqLanguage_Value31
        self.reqLanguage_Value83 = reqLanguage_Value83
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def reqLanguage_Value31(self):
        return self.__reqLanguage_Value31

    @reqLanguage_Value31.setter
    def reqLanguage_Value31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Value__reqLanguage_Value31", None)
        self.__reqLanguage_Value31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_ParamEvent30"):
                opp_val = getattr(old_value, "reqLanguage_ParamEvent30", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_ParamEvent30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_ParamEvent30"):
                opp_val = getattr(value, "reqLanguage_ParamEvent30", None)
                setattr(value, "reqLanguage_ParamEvent30", self)

    @property
    def reqLanguage_Value(self):
        return self.__reqLanguage_Value

    @reqLanguage_Value.setter
    def reqLanguage_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Value__reqLanguage_Value", None)
        self.__reqLanguage_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_PrefixCondition22"):
                opp_val = getattr(old_value, "reqLanguage_PrefixCondition22", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_PrefixCondition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_PrefixCondition22"):
                opp_val = getattr(value, "reqLanguage_PrefixCondition22", None)
                setattr(value, "reqLanguage_PrefixCondition22", self)

    @property
    def reqLanguage_Value83(self):
        return self.__reqLanguage_Value83

    @reqLanguage_Value83.setter
    def reqLanguage_Value83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Value__reqLanguage_Value83", None)
        self.__reqLanguage_Value83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Action82"):
                opp_val = getattr(old_value, "reqLanguage_Action82", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Action82"):
                opp_val = getattr(value, "reqLanguage_Action82", None)
                setattr(value, "reqLanguage_Action82", self)

class reqLanguage_Operator:

    def __init__(self, operator: str, reqLanguage_Operator: "reqLanguage_PrefixCondition" = None):
        self.operator = operator
        self.reqLanguage_Operator = reqLanguage_Operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def reqLanguage_Operator(self):
        return self.__reqLanguage_Operator

    @reqLanguage_Operator.setter
    def reqLanguage_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_Operator__reqLanguage_Operator", None)
        self.__reqLanguage_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_PrefixCondition20"):
                opp_val = getattr(old_value, "reqLanguage_PrefixCondition20", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_PrefixCondition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_PrefixCondition20"):
                opp_val = getattr(value, "reqLanguage_PrefixCondition20", None)
                setattr(value, "reqLanguage_PrefixCondition20", self)

class reqLanguage_Requirement:

    pass
class reqLanguage_Model:

    pass
class reqLanguage_EObject:

    pass
class reqLanguage_Prefix:

    pass
class reqLanguage_ReqID:

    def __init__(self, reqID: str, name: str, reqLanguage_ReqID: "reqLanguage_Requirement" = None):
        self.reqID = reqID
        self.name = name
        self.reqLanguage_ReqID = reqLanguage_ReqID
        
    @property
    def reqID(self) -> str:
        return self.__reqID

    @reqID.setter
    def reqID(self, reqID: str):
        self.__reqID = reqID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reqLanguage_ReqID(self):
        return self.__reqLanguage_ReqID

    @reqLanguage_ReqID.setter
    def reqLanguage_ReqID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reqLanguage_ReqID__reqLanguage_ReqID", None)
        self.__reqLanguage_ReqID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reqLanguage_Requirement2"):
                opp_val = getattr(old_value, "reqLanguage_Requirement2", None)
                if opp_val == self:
                    setattr(old_value, "reqLanguage_Requirement2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reqLanguage_Requirement2"):
                opp_val = getattr(value, "reqLanguage_Requirement2", None)
                setattr(value, "reqLanguage_Requirement2", self)

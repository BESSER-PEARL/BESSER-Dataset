from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class zhu_TriggersSeparated:

    def __init__(self, firstTrigger: str, followingTriggers: str, zhu_TriggersSeparated: "zhu_Triggers" = None):
        self.firstTrigger = firstTrigger
        self.followingTriggers = followingTriggers
        self.zhu_TriggersSeparated = zhu_TriggersSeparated
        
    @property
    def firstTrigger(self) -> str:
        return self.__firstTrigger

    @firstTrigger.setter
    def firstTrigger(self, firstTrigger: str):
        self.__firstTrigger = firstTrigger

    @property
    def followingTriggers(self) -> str:
        return self.__followingTriggers

    @followingTriggers.setter
    def followingTriggers(self, followingTriggers: str):
        self.__followingTriggers = followingTriggers

    @property
    def zhu_TriggersSeparated(self):
        return self.__zhu_TriggersSeparated

    @zhu_TriggersSeparated.setter
    def zhu_TriggersSeparated(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_TriggersSeparated__zhu_TriggersSeparated", None)
        self.__zhu_TriggersSeparated = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Triggers37"):
                opp_val = getattr(old_value, "zhu_Triggers37", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Triggers37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Triggers37"):
                opp_val = getattr(value, "zhu_Triggers37", None)
                setattr(value, "zhu_Triggers37", self)

class zhu_StatesSeparated:

    pass
class zhu_Triggers:

    pass
class zhu_State:

    def __init__(self, name: str, zhu_State32: "zhu_StatesSeparated" = None, zhu_State35: "zhu_StatesSeparated" = None, zhu_State: "zhu_Transition" = None, zhu_State25: "zhu_Transition" = None):
        self.name = name
        self.zhu_State32 = zhu_State32
        self.zhu_State35 = zhu_State35
        self.zhu_State = zhu_State
        self.zhu_State25 = zhu_State25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zhu_State25(self):
        return self.__zhu_State25

    @zhu_State25.setter
    def zhu_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_State__zhu_State25", None)
        self.__zhu_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Transition24"):
                opp_val = getattr(old_value, "zhu_Transition24", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Transition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Transition24"):
                opp_val = getattr(value, "zhu_Transition24", None)
                setattr(value, "zhu_Transition24", self)

    @property
    def zhu_State35(self):
        return self.__zhu_State35

    @zhu_State35.setter
    def zhu_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_State__zhu_State35", None)
        self.__zhu_State35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_StatesSeparated34"):
                opp_val = getattr(old_value, "zhu_StatesSeparated34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_StatesSeparated34"):
                opp_val = getattr(value, "zhu_StatesSeparated34", None)
                if opp_val is None:
                    setattr(value, "zhu_StatesSeparated34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zhu_State32(self):
        return self.__zhu_State32

    @zhu_State32.setter
    def zhu_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_State__zhu_State32", None)
        self.__zhu_State32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_StatesSeparated31"):
                opp_val = getattr(old_value, "zhu_StatesSeparated31", None)
                if opp_val == self:
                    setattr(old_value, "zhu_StatesSeparated31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_StatesSeparated31"):
                opp_val = getattr(value, "zhu_StatesSeparated31", None)
                setattr(value, "zhu_StatesSeparated31", self)

    @property
    def zhu_State(self):
        return self.__zhu_State

    @zhu_State.setter
    def zhu_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_State__zhu_State", None)
        self.__zhu_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Transition22"):
                opp_val = getattr(old_value, "zhu_Transition22", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Transition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Transition22"):
                opp_val = getattr(value, "zhu_Transition22", None)
                setattr(value, "zhu_Transition22", self)

class zhu_Transition:

    def __init__(self, guard: str, behaviour: str, zhu_Transition: "zhu_Transitions" = None, zhu_Transition20: "zhu_Transitions" = None, zhu_Transition22: "zhu_State" = None, zhu_Transition24: "zhu_State" = None, zhu_Transition27: "zhu_Triggers" = None):
        self.guard = guard
        self.behaviour = behaviour
        self.zhu_Transition = zhu_Transition
        self.zhu_Transition20 = zhu_Transition20
        self.zhu_Transition22 = zhu_Transition22
        self.zhu_Transition24 = zhu_Transition24
        self.zhu_Transition27 = zhu_Transition27
        
    @property
    def behaviour(self) -> str:
        return self.__behaviour

    @behaviour.setter
    def behaviour(self, behaviour: str):
        self.__behaviour = behaviour

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def zhu_Transition20(self):
        return self.__zhu_Transition20

    @zhu_Transition20.setter
    def zhu_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Transition__zhu_Transition20", None)
        self.__zhu_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Transitions19"):
                opp_val = getattr(old_value, "zhu_Transitions19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Transitions19"):
                opp_val = getattr(value, "zhu_Transitions19", None)
                if opp_val is None:
                    setattr(value, "zhu_Transitions19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zhu_Transition24(self):
        return self.__zhu_Transition24

    @zhu_Transition24.setter
    def zhu_Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Transition__zhu_Transition24", None)
        self.__zhu_Transition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_State25"):
                opp_val = getattr(old_value, "zhu_State25", None)
                if opp_val == self:
                    setattr(old_value, "zhu_State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_State25"):
                opp_val = getattr(value, "zhu_State25", None)
                setattr(value, "zhu_State25", self)

    @property
    def zhu_Transition(self):
        return self.__zhu_Transition

    @zhu_Transition.setter
    def zhu_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Transition__zhu_Transition", None)
        self.__zhu_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Transitions17"):
                opp_val = getattr(old_value, "zhu_Transitions17", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Transitions17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Transitions17"):
                opp_val = getattr(value, "zhu_Transitions17", None)
                setattr(value, "zhu_Transitions17", self)

    @property
    def zhu_Transition22(self):
        return self.__zhu_Transition22

    @zhu_Transition22.setter
    def zhu_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Transition__zhu_Transition22", None)
        self.__zhu_Transition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_State"):
                opp_val = getattr(old_value, "zhu_State", None)
                if opp_val == self:
                    setattr(old_value, "zhu_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_State"):
                opp_val = getattr(value, "zhu_State", None)
                setattr(value, "zhu_State", self)

    @property
    def zhu_Transition27(self):
        return self.__zhu_Transition27

    @zhu_Transition27.setter
    def zhu_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Transition__zhu_Transition27", None)
        self.__zhu_Transition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Triggers"):
                opp_val = getattr(old_value, "zhu_Triggers", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Triggers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Triggers"):
                opp_val = getattr(value, "zhu_Triggers", None)
                setattr(value, "zhu_Triggers", self)

class zhu_Transitions:

    pass
class zhu_Region:

    def __init__(self, name: str, zhu_Region8: "zhu_States" = None, zhu_Region12: "zhu_Region" = None, zhu_Region10: set["zhu_Region"] = None, zhu_Region14: "zhu_Transitions" = None, zhu_Region: "zhu_TopRegion" = None):
        self.name = name
        self.zhu_Region8 = zhu_Region8
        self.zhu_Region12 = zhu_Region12
        self.zhu_Region10 = zhu_Region10 if zhu_Region10 is not None else set()
        self.zhu_Region14 = zhu_Region14
        self.zhu_Region = zhu_Region
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zhu_Region12(self):
        return self.__zhu_Region12

    @zhu_Region12.setter
    def zhu_Region12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Region__zhu_Region12", None)
        self.__zhu_Region12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Region10"):
                opp_val = getattr(old_value, "zhu_Region10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Region10"):
                opp_val = getattr(value, "zhu_Region10", None)
                if opp_val is None:
                    setattr(value, "zhu_Region10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zhu_Region10(self):
        return self.__zhu_Region10

    @zhu_Region10.setter
    def zhu_Region10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Region__zhu_Region10", None)
        self.__zhu_Region10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "zhu_Region12"):
                    opp_val = getattr(item, "zhu_Region12", None)
                    
                    if opp_val == self:
                        setattr(item, "zhu_Region12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "zhu_Region12"):
                    opp_val = getattr(item, "zhu_Region12", None)
                    
                    setattr(item, "zhu_Region12", self)
                    

    @property
    def zhu_Region14(self):
        return self.__zhu_Region14

    @zhu_Region14.setter
    def zhu_Region14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Region__zhu_Region14", None)
        self.__zhu_Region14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_Transitions15"):
                opp_val = getattr(old_value, "zhu_Transitions15", None)
                if opp_val == self:
                    setattr(old_value, "zhu_Transitions15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_Transitions15"):
                opp_val = getattr(value, "zhu_Transitions15", None)
                setattr(value, "zhu_Transitions15", self)

    @property
    def zhu_Region(self):
        return self.__zhu_Region

    @zhu_Region.setter
    def zhu_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Region__zhu_Region", None)
        self.__zhu_Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_TopRegion4"):
                opp_val = getattr(old_value, "zhu_TopRegion4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_TopRegion4"):
                opp_val = getattr(value, "zhu_TopRegion4", None)
                if opp_val is None:
                    setattr(value, "zhu_TopRegion4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def zhu_Region8(self):
        return self.__zhu_Region8

    @zhu_Region8.setter
    def zhu_Region8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zhu_Region__zhu_Region8", None)
        self.__zhu_Region8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zhu_States9"):
                opp_val = getattr(old_value, "zhu_States9", None)
                if opp_val == self:
                    setattr(old_value, "zhu_States9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zhu_States9"):
                opp_val = getattr(value, "zhu_States9", None)
                setattr(value, "zhu_States9", self)

class zhu_States:

    pass
class zhu_TopRegion:

    pass
class zhu_StateMachine:

    pass
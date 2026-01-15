from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm_Observation:

    def __init__(self, time: str, sm_Observation: "sm_StateMachine" = None, sm_Observation16: "sm_State" = None, sm_Observation30: "sm_State" = None, sm_Observation33: "sm_StateMachine" = None):
        self.time = time
        self.sm_Observation = sm_Observation
        self.sm_Observation16 = sm_Observation16
        self.sm_Observation30 = sm_Observation30
        self.sm_Observation33 = sm_Observation33
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def sm_Observation(self):
        return self.__sm_Observation

    @sm_Observation.setter
    def sm_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__sm_Observation", None)
        self.__sm_Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine10"):
                opp_val = getattr(old_value, "sm_StateMachine10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine10"):
                opp_val = getattr(value, "sm_StateMachine10", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_Observation33(self):
        return self.__sm_Observation33

    @sm_Observation33.setter
    def sm_Observation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__sm_Observation33", None)
        self.__sm_Observation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine34"):
                opp_val = getattr(old_value, "sm_StateMachine34", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine34"):
                opp_val = getattr(value, "sm_StateMachine34", None)
                setattr(value, "sm_StateMachine34", self)

    @property
    def sm_Observation30(self):
        return self.__sm_Observation30

    @sm_Observation30.setter
    def sm_Observation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__sm_Observation30", None)
        self.__sm_Observation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State31"):
                opp_val = getattr(old_value, "sm_State31", None)
                if opp_val == self:
                    setattr(old_value, "sm_State31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State31"):
                opp_val = getattr(value, "sm_State31", None)
                setattr(value, "sm_State31", self)

    @property
    def sm_Observation16(self):
        return self.__sm_Observation16

    @sm_Observation16.setter
    def sm_Observation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Observation__sm_Observation16", None)
        self.__sm_Observation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State15"):
                opp_val = getattr(old_value, "sm_State15", None)
                if opp_val == self:
                    setattr(old_value, "sm_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State15"):
                opp_val = getattr(value, "sm_State15", None)
                setattr(value, "sm_State15", self)

class sm_Transition:

    def __init__(self, name: str, sm_Transition: "sm_StateMachine" = None, sm_Transition21: "sm_State" = None, sm_Transition24: "sm_State" = None, sm_Transition27: "sm_StateMachine" = None):
        self.name = name
        self.sm_Transition = sm_Transition
        self.sm_Transition21 = sm_Transition21
        self.sm_Transition24 = sm_Transition24
        self.sm_Transition27 = sm_Transition27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_Transition21(self):
        return self.__sm_Transition21

    @sm_Transition21.setter
    def sm_Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition21", None)
        self.__sm_Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State22"):
                opp_val = getattr(old_value, "sm_State22", None)
                if opp_val == self:
                    setattr(old_value, "sm_State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State22"):
                opp_val = getattr(value, "sm_State22", None)
                setattr(value, "sm_State22", self)

    @property
    def sm_Transition(self):
        return self.__sm_Transition

    @sm_Transition.setter
    def sm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition", None)
        self.__sm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine8"):
                opp_val = getattr(old_value, "sm_StateMachine8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine8"):
                opp_val = getattr(value, "sm_StateMachine8", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_Transition24(self):
        return self.__sm_Transition24

    @sm_Transition24.setter
    def sm_Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition24", None)
        self.__sm_Transition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State25"):
                opp_val = getattr(old_value, "sm_State25", None)
                if opp_val == self:
                    setattr(old_value, "sm_State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State25"):
                opp_val = getattr(value, "sm_State25", None)
                setattr(value, "sm_State25", self)

    @property
    def sm_Transition27(self):
        return self.__sm_Transition27

    @sm_Transition27.setter
    def sm_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Transition__sm_Transition27", None)
        self.__sm_Transition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine28"):
                opp_val = getattr(old_value, "sm_StateMachine28", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine28"):
                opp_val = getattr(value, "sm_StateMachine28", None)
                setattr(value, "sm_StateMachine28", self)

class sm_State:

    def __init__(self, name: str, sm_State: "sm_StateMachine" = None, sm_State3: "sm_StateMachine" = None, sm_State6: "sm_StateMachine" = None, sm_State12: set["sm_StateMachine"] = None, sm_State15: "sm_Observation" = None, sm_State18: "sm_StateMachine" = None, sm_State22: "sm_Transition" = None, sm_State25: "sm_Transition" = None, sm_State31: "sm_Observation" = None):
        self.name = name
        self.sm_State = sm_State
        self.sm_State3 = sm_State3
        self.sm_State6 = sm_State6
        self.sm_State12 = sm_State12 if sm_State12 is not None else set()
        self.sm_State15 = sm_State15
        self.sm_State18 = sm_State18
        self.sm_State22 = sm_State22
        self.sm_State25 = sm_State25
        self.sm_State31 = sm_State31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_State3(self):
        return self.__sm_State3

    @sm_State3.setter
    def sm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State3", None)
        self.__sm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine2"):
                opp_val = getattr(old_value, "sm_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine2"):
                opp_val = getattr(value, "sm_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State25(self):
        return self.__sm_State25

    @sm_State25.setter
    def sm_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State25", None)
        self.__sm_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition24"):
                opp_val = getattr(old_value, "sm_Transition24", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition24"):
                opp_val = getattr(value, "sm_Transition24", None)
                setattr(value, "sm_Transition24", self)

    @property
    def sm_State31(self):
        return self.__sm_State31

    @sm_State31.setter
    def sm_State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State31", None)
        self.__sm_State31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Observation30"):
                opp_val = getattr(old_value, "sm_Observation30", None)
                if opp_val == self:
                    setattr(old_value, "sm_Observation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Observation30"):
                opp_val = getattr(value, "sm_Observation30", None)
                setattr(value, "sm_Observation30", self)

    @property
    def sm_State15(self):
        return self.__sm_State15

    @sm_State15.setter
    def sm_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State15", None)
        self.__sm_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Observation16"):
                opp_val = getattr(old_value, "sm_Observation16", None)
                if opp_val == self:
                    setattr(old_value, "sm_Observation16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Observation16"):
                opp_val = getattr(value, "sm_Observation16", None)
                setattr(value, "sm_Observation16", self)

    @property
    def sm_State12(self):
        return self.__sm_State12

    @sm_State12.setter
    def sm_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State12", None)
        self.__sm_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_StateMachine13"):
                    opp_val = getattr(item, "sm_StateMachine13", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_StateMachine13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_StateMachine13"):
                    opp_val = getattr(item, "sm_StateMachine13", None)
                    
                    setattr(item, "sm_StateMachine13", self)
                    

    @property
    def sm_State(self):
        return self.__sm_State

    @sm_State.setter
    def sm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State", None)
        self.__sm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine"):
                opp_val = getattr(old_value, "sm_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine"):
                opp_val = getattr(value, "sm_StateMachine", None)
                setattr(value, "sm_StateMachine", self)

    @property
    def sm_State22(self):
        return self.__sm_State22

    @sm_State22.setter
    def sm_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State22", None)
        self.__sm_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition21"):
                opp_val = getattr(old_value, "sm_Transition21", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition21"):
                opp_val = getattr(value, "sm_Transition21", None)
                setattr(value, "sm_Transition21", self)

    @property
    def sm_State6(self):
        return self.__sm_State6

    @sm_State6.setter
    def sm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State6", None)
        self.__sm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine5"):
                opp_val = getattr(old_value, "sm_StateMachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine5"):
                opp_val = getattr(value, "sm_StateMachine5", None)
                if opp_val is None:
                    setattr(value, "sm_StateMachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_State18(self):
        return self.__sm_State18

    @sm_State18.setter
    def sm_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_State__sm_State18", None)
        self.__sm_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_StateMachine19"):
                opp_val = getattr(old_value, "sm_StateMachine19", None)
                if opp_val == self:
                    setattr(old_value, "sm_StateMachine19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_StateMachine19"):
                opp_val = getattr(value, "sm_StateMachine19", None)
                setattr(value, "sm_StateMachine19", self)

class sm_StateMachine:

    def __init__(self, name: str, sm_StateMachine: "sm_State" = None, sm_StateMachine2: set["sm_State"] = None, sm_StateMachine5: set["sm_State"] = None, sm_StateMachine8: set["sm_Transition"] = None, sm_StateMachine10: set["sm_Observation"] = None, sm_StateMachine13: "sm_State" = None, sm_StateMachine19: "sm_State" = None, sm_StateMachine34: "sm_Observation" = None, sm_StateMachine28: "sm_Transition" = None):
        self.name = name
        self.sm_StateMachine = sm_StateMachine
        self.sm_StateMachine2 = sm_StateMachine2 if sm_StateMachine2 is not None else set()
        self.sm_StateMachine5 = sm_StateMachine5 if sm_StateMachine5 is not None else set()
        self.sm_StateMachine8 = sm_StateMachine8 if sm_StateMachine8 is not None else set()
        self.sm_StateMachine10 = sm_StateMachine10 if sm_StateMachine10 is not None else set()
        self.sm_StateMachine13 = sm_StateMachine13
        self.sm_StateMachine19 = sm_StateMachine19
        self.sm_StateMachine34 = sm_StateMachine34
        self.sm_StateMachine28 = sm_StateMachine28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sm_StateMachine10(self):
        return self.__sm_StateMachine10

    @sm_StateMachine10.setter
    def sm_StateMachine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine10", None)
        self.__sm_StateMachine10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_Observation"):
                    opp_val = getattr(item, "sm_Observation", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_Observation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_Observation"):
                    opp_val = getattr(item, "sm_Observation", None)
                    
                    setattr(item, "sm_Observation", self)
                    

    @property
    def sm_StateMachine(self):
        return self.__sm_StateMachine

    @sm_StateMachine.setter
    def sm_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine", None)
        self.__sm_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State"):
                opp_val = getattr(old_value, "sm_State", None)
                if opp_val == self:
                    setattr(old_value, "sm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State"):
                opp_val = getattr(value, "sm_State", None)
                setattr(value, "sm_State", self)

    @property
    def sm_StateMachine28(self):
        return self.__sm_StateMachine28

    @sm_StateMachine28.setter
    def sm_StateMachine28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine28", None)
        self.__sm_StateMachine28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Transition27"):
                opp_val = getattr(old_value, "sm_Transition27", None)
                if opp_val == self:
                    setattr(old_value, "sm_Transition27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Transition27"):
                opp_val = getattr(value, "sm_Transition27", None)
                setattr(value, "sm_Transition27", self)

    @property
    def sm_StateMachine2(self):
        return self.__sm_StateMachine2

    @sm_StateMachine2.setter
    def sm_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine2", None)
        self.__sm_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State3"):
                    opp_val = getattr(item, "sm_State3", None)
                    
                    setattr(item, "sm_State3", self)
                    

    @property
    def sm_StateMachine8(self):
        return self.__sm_StateMachine8

    @sm_StateMachine8.setter
    def sm_StateMachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine8", None)
        self.__sm_StateMachine8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_Transition"):
                    opp_val = getattr(item, "sm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_Transition"):
                    opp_val = getattr(item, "sm_Transition", None)
                    
                    setattr(item, "sm_Transition", self)
                    

    @property
    def sm_StateMachine5(self):
        return self.__sm_StateMachine5

    @sm_StateMachine5.setter
    def sm_StateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine5", None)
        self.__sm_StateMachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sm_State6"):
                    opp_val = getattr(item, "sm_State6", None)
                    
                    if opp_val == self:
                        setattr(item, "sm_State6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sm_State6"):
                    opp_val = getattr(item, "sm_State6", None)
                    
                    setattr(item, "sm_State6", self)
                    

    @property
    def sm_StateMachine19(self):
        return self.__sm_StateMachine19

    @sm_StateMachine19.setter
    def sm_StateMachine19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine19", None)
        self.__sm_StateMachine19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State18"):
                opp_val = getattr(old_value, "sm_State18", None)
                if opp_val == self:
                    setattr(old_value, "sm_State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State18"):
                opp_val = getattr(value, "sm_State18", None)
                setattr(value, "sm_State18", self)

    @property
    def sm_StateMachine13(self):
        return self.__sm_StateMachine13

    @sm_StateMachine13.setter
    def sm_StateMachine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine13", None)
        self.__sm_StateMachine13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_State12"):
                opp_val = getattr(old_value, "sm_State12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_State12"):
                opp_val = getattr(value, "sm_State12", None)
                if opp_val is None:
                    setattr(value, "sm_State12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_StateMachine34(self):
        return self.__sm_StateMachine34

    @sm_StateMachine34.setter
    def sm_StateMachine34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_StateMachine__sm_StateMachine34", None)
        self.__sm_StateMachine34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Observation33"):
                opp_val = getattr(old_value, "sm_Observation33", None)
                if opp_val == self:
                    setattr(old_value, "sm_Observation33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Observation33"):
                opp_val = getattr(value, "sm_Observation33", None)
                setattr(value, "sm_Observation33", self)

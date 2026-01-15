from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsa_FSA:

    def __init__(self, temporalFormula: str, fsa_FSA: "fsa_State" = None, fsa_FSA7: set["fsa_Transition"] = None, fsa_FSA10: "fsa_State" = None, fsa_FSA13: set["fsa_State"] = None):
        self.temporalFormula = temporalFormula
        self.fsa_FSA = fsa_FSA
        self.fsa_FSA7 = fsa_FSA7 if fsa_FSA7 is not None else set()
        self.fsa_FSA10 = fsa_FSA10
        self.fsa_FSA13 = fsa_FSA13 if fsa_FSA13 is not None else set()
        
    @property
    def temporalFormula(self) -> str:
        return self.__temporalFormula

    @temporalFormula.setter
    def temporalFormula(self, temporalFormula: str):
        self.__temporalFormula = temporalFormula

    @property
    def fsa_FSA7(self):
        return self.__fsa_FSA7

    @fsa_FSA7.setter
    def fsa_FSA7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_FSA__fsa_FSA7", None)
        self.__fsa_FSA7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsa_Transition8"):
                    opp_val = getattr(item, "fsa_Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "fsa_Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsa_Transition8"):
                    opp_val = getattr(item, "fsa_Transition8", None)
                    
                    setattr(item, "fsa_Transition8", self)
                    

    @property
    def fsa_FSA10(self):
        return self.__fsa_FSA10

    @fsa_FSA10.setter
    def fsa_FSA10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_FSA__fsa_FSA10", None)
        self.__fsa_FSA10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_State11"):
                opp_val = getattr(old_value, "fsa_State11", None)
                if opp_val == self:
                    setattr(old_value, "fsa_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_State11"):
                opp_val = getattr(value, "fsa_State11", None)
                setattr(value, "fsa_State11", self)

    @property
    def fsa_FSA(self):
        return self.__fsa_FSA

    @fsa_FSA.setter
    def fsa_FSA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_FSA__fsa_FSA", None)
        self.__fsa_FSA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_State"):
                opp_val = getattr(old_value, "fsa_State", None)
                if opp_val == self:
                    setattr(old_value, "fsa_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_State"):
                opp_val = getattr(value, "fsa_State", None)
                setattr(value, "fsa_State", self)

    @property
    def fsa_FSA13(self):
        return self.__fsa_FSA13

    @fsa_FSA13.setter
    def fsa_FSA13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_FSA__fsa_FSA13", None)
        self.__fsa_FSA13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsa_State14"):
                    opp_val = getattr(item, "fsa_State14", None)
                    
                    if opp_val == self:
                        setattr(item, "fsa_State14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsa_State14"):
                    opp_val = getattr(item, "fsa_State14", None)
                    
                    setattr(item, "fsa_State14", self)
                    

class fsa_State:

    def __init__(self, temporalProperties: str, name: str, final: bool, fsa_State2: "fsa_Transition" = None, fsa_State5: "fsa_Transition" = None, fsa_State: "fsa_FSA" = None, fsa_State11: "fsa_FSA" = None, fsa_State14: "fsa_FSA" = None):
        self.temporalProperties = temporalProperties
        self.name = name
        self.final = final
        self.fsa_State2 = fsa_State2
        self.fsa_State5 = fsa_State5
        self.fsa_State = fsa_State
        self.fsa_State11 = fsa_State11
        self.fsa_State14 = fsa_State14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def temporalProperties(self) -> str:
        return self.__temporalProperties

    @temporalProperties.setter
    def temporalProperties(self, temporalProperties: str):
        self.__temporalProperties = temporalProperties

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def fsa_State14(self):
        return self.__fsa_State14

    @fsa_State14.setter
    def fsa_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State14", None)
        self.__fsa_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA13"):
                opp_val = getattr(old_value, "fsa_FSA13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA13"):
                opp_val = getattr(value, "fsa_FSA13", None)
                if opp_val is None:
                    setattr(value, "fsa_FSA13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsa_State5(self):
        return self.__fsa_State5

    @fsa_State5.setter
    def fsa_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State5", None)
        self.__fsa_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_Transition4"):
                opp_val = getattr(old_value, "fsa_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "fsa_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_Transition4"):
                opp_val = getattr(value, "fsa_Transition4", None)
                setattr(value, "fsa_Transition4", self)

    @property
    def fsa_State11(self):
        return self.__fsa_State11

    @fsa_State11.setter
    def fsa_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State11", None)
        self.__fsa_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA10"):
                opp_val = getattr(old_value, "fsa_FSA10", None)
                if opp_val == self:
                    setattr(old_value, "fsa_FSA10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA10"):
                opp_val = getattr(value, "fsa_FSA10", None)
                setattr(value, "fsa_FSA10", self)

    @property
    def fsa_State2(self):
        return self.__fsa_State2

    @fsa_State2.setter
    def fsa_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State2", None)
        self.__fsa_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_Transition"):
                opp_val = getattr(old_value, "fsa_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsa_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_Transition"):
                opp_val = getattr(value, "fsa_Transition", None)
                setattr(value, "fsa_Transition", self)

    @property
    def fsa_State(self):
        return self.__fsa_State

    @fsa_State.setter
    def fsa_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_State__fsa_State", None)
        self.__fsa_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA"):
                opp_val = getattr(old_value, "fsa_FSA", None)
                if opp_val == self:
                    setattr(old_value, "fsa_FSA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA"):
                opp_val = getattr(value, "fsa_FSA", None)
                setattr(value, "fsa_FSA", self)

class fsa_Transition:

    def __init__(self, description: str, fsa_Transition: "fsa_State" = None, fsa_Transition4: "fsa_State" = None, fsa_Transition8: "fsa_FSA" = None):
        self.description = description
        self.fsa_Transition = fsa_Transition
        self.fsa_Transition4 = fsa_Transition4
        self.fsa_Transition8 = fsa_Transition8
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def fsa_Transition4(self):
        return self.__fsa_Transition4

    @fsa_Transition4.setter
    def fsa_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__fsa_Transition4", None)
        self.__fsa_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_State5"):
                opp_val = getattr(old_value, "fsa_State5", None)
                if opp_val == self:
                    setattr(old_value, "fsa_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_State5"):
                opp_val = getattr(value, "fsa_State5", None)
                setattr(value, "fsa_State5", self)

    @property
    def fsa_Transition8(self):
        return self.__fsa_Transition8

    @fsa_Transition8.setter
    def fsa_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__fsa_Transition8", None)
        self.__fsa_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_FSA7"):
                opp_val = getattr(old_value, "fsa_FSA7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_FSA7"):
                opp_val = getattr(value, "fsa_FSA7", None)
                if opp_val is None:
                    setattr(value, "fsa_FSA7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsa_Transition(self):
        return self.__fsa_Transition

    @fsa_Transition.setter
    def fsa_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsa_Transition__fsa_Transition", None)
        self.__fsa_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsa_State2"):
                opp_val = getattr(old_value, "fsa_State2", None)
                if opp_val == self:
                    setattr(old_value, "fsa_State2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsa_State2"):
                opp_val = getattr(value, "fsa_State2", None)
                setattr(value, "fsa_State2", self)

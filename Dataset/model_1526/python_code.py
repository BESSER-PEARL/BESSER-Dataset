from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsmtest_ConditionDeclaration:

    pass
class fsmtest_PostconditionDeclaration:

    pass
class fsmtest_PreconditionDeclaration:

    pass
class fsmtest_SeedDeclaration:

    def __init__(self, val: int, fsmtest_SeedDeclaration: "fsmtest_RandomTest" = None):
        self.val = val
        self.fsmtest_SeedDeclaration = fsmtest_SeedDeclaration
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

    @property
    def fsmtest_SeedDeclaration(self):
        return self.__fsmtest_SeedDeclaration

    @fsmtest_SeedDeclaration.setter
    def fsmtest_SeedDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SeedDeclaration__fsmtest_SeedDeclaration", None)
        self.__fsmtest_SeedDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_RandomTest11"):
                opp_val = getattr(old_value, "fsmtest_RandomTest11", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_RandomTest11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_RandomTest11"):
                opp_val = getattr(value, "fsmtest_RandomTest11", None)
                setattr(value, "fsmtest_RandomTest11", self)

class fsmtest_LoopsDeclaration:

    def __init__(self, val: int, fsmtest_LoopsDeclaration: "fsmtest_RandomTest" = None):
        self.val = val
        self.fsmtest_LoopsDeclaration = fsmtest_LoopsDeclaration
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

    @property
    def fsmtest_LoopsDeclaration(self):
        return self.__fsmtest_LoopsDeclaration

    @fsmtest_LoopsDeclaration.setter
    def fsmtest_LoopsDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_LoopsDeclaration__fsmtest_LoopsDeclaration", None)
        self.__fsmtest_LoopsDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_RandomTest9"):
                opp_val = getattr(old_value, "fsmtest_RandomTest9", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_RandomTest9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_RandomTest9"):
                opp_val = getattr(value, "fsmtest_RandomTest9", None)
                setattr(value, "fsmtest_RandomTest9", self)

class fsmtest_StateDeclaration:

    def __init__(self, name: str, fsmtest_StateDeclaration14: "fsmtest_TransitionDeclaration" = None, fsmtest_StateDeclaration: "fsmtest_FsmDefinition" = None, fsmtest_StateDeclaration34: set["fsmtest_ConditionDeclaration"] = None, fsmtest_StateDeclaration37: set["fsmtest_TransitionDeclaration"] = None):
        self.name = name
        self.fsmtest_StateDeclaration14 = fsmtest_StateDeclaration14
        self.fsmtest_StateDeclaration = fsmtest_StateDeclaration
        self.fsmtest_StateDeclaration34 = fsmtest_StateDeclaration34 if fsmtest_StateDeclaration34 is not None else set()
        self.fsmtest_StateDeclaration37 = fsmtest_StateDeclaration37 if fsmtest_StateDeclaration37 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmtest_StateDeclaration34(self):
        return self.__fsmtest_StateDeclaration34

    @fsmtest_StateDeclaration34.setter
    def fsmtest_StateDeclaration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_StateDeclaration__fsmtest_StateDeclaration34", None)
        self.__fsmtest_StateDeclaration34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_ConditionDeclaration35"):
                    opp_val = getattr(item, "fsmtest_ConditionDeclaration35", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_ConditionDeclaration35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_ConditionDeclaration35"):
                    opp_val = getattr(item, "fsmtest_ConditionDeclaration35", None)
                    
                    setattr(item, "fsmtest_ConditionDeclaration35", self)
                    

    @property
    def fsmtest_StateDeclaration14(self):
        return self.__fsmtest_StateDeclaration14

    @fsmtest_StateDeclaration14.setter
    def fsmtest_StateDeclaration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_StateDeclaration__fsmtest_StateDeclaration14", None)
        self.__fsmtest_StateDeclaration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_TransitionDeclaration"):
                opp_val = getattr(old_value, "fsmtest_TransitionDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_TransitionDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_TransitionDeclaration"):
                opp_val = getattr(value, "fsmtest_TransitionDeclaration", None)
                setattr(value, "fsmtest_TransitionDeclaration", self)

    @property
    def fsmtest_StateDeclaration37(self):
        return self.__fsmtest_StateDeclaration37

    @fsmtest_StateDeclaration37.setter
    def fsmtest_StateDeclaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_StateDeclaration__fsmtest_StateDeclaration37", None)
        self.__fsmtest_StateDeclaration37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_TransitionDeclaration38"):
                    opp_val = getattr(item, "fsmtest_TransitionDeclaration38", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_TransitionDeclaration38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_TransitionDeclaration38"):
                    opp_val = getattr(item, "fsmtest_TransitionDeclaration38", None)
                    
                    setattr(item, "fsmtest_TransitionDeclaration38", self)
                    

    @property
    def fsmtest_StateDeclaration(self):
        return self.__fsmtest_StateDeclaration

    @fsmtest_StateDeclaration.setter
    def fsmtest_StateDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_StateDeclaration__fsmtest_StateDeclaration", None)
        self.__fsmtest_StateDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_FsmDefinition4"):
                opp_val = getattr(old_value, "fsmtest_FsmDefinition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_FsmDefinition4"):
                opp_val = getattr(value, "fsmtest_FsmDefinition4", None)
                if opp_val is None:
                    setattr(value, "fsmtest_FsmDefinition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsmtest_TransitionDeclaration:

    def __init__(self, name: str, fsmtest_TransitionDeclaration: "fsmtest_StateDeclaration" = None, fsmtest_TransitionDeclaration16: "fsmtest_SignalDeclaration" = None, fsmtest_TransitionDeclaration38: "fsmtest_StateDeclaration" = None, fsmtest_TransitionDeclaration19: set["fsmtest_GuardDeclaration"] = None, fsmtest_TransitionDeclaration22: set["fsmtest_PreconditionDeclaration"] = None, fsmtest_TransitionDeclaration24: set["fsmtest_PostconditionDeclaration"] = None):
        self.name = name
        self.fsmtest_TransitionDeclaration = fsmtest_TransitionDeclaration
        self.fsmtest_TransitionDeclaration16 = fsmtest_TransitionDeclaration16
        self.fsmtest_TransitionDeclaration38 = fsmtest_TransitionDeclaration38
        self.fsmtest_TransitionDeclaration19 = fsmtest_TransitionDeclaration19 if fsmtest_TransitionDeclaration19 is not None else set()
        self.fsmtest_TransitionDeclaration22 = fsmtest_TransitionDeclaration22 if fsmtest_TransitionDeclaration22 is not None else set()
        self.fsmtest_TransitionDeclaration24 = fsmtest_TransitionDeclaration24 if fsmtest_TransitionDeclaration24 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmtest_TransitionDeclaration24(self):
        return self.__fsmtest_TransitionDeclaration24

    @fsmtest_TransitionDeclaration24.setter
    def fsmtest_TransitionDeclaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration24", None)
        self.__fsmtest_TransitionDeclaration24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_PostconditionDeclaration"):
                    opp_val = getattr(item, "fsmtest_PostconditionDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_PostconditionDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_PostconditionDeclaration"):
                    opp_val = getattr(item, "fsmtest_PostconditionDeclaration", None)
                    
                    setattr(item, "fsmtest_PostconditionDeclaration", self)
                    

    @property
    def fsmtest_TransitionDeclaration22(self):
        return self.__fsmtest_TransitionDeclaration22

    @fsmtest_TransitionDeclaration22.setter
    def fsmtest_TransitionDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration22", None)
        self.__fsmtest_TransitionDeclaration22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_PreconditionDeclaration"):
                    opp_val = getattr(item, "fsmtest_PreconditionDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_PreconditionDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_PreconditionDeclaration"):
                    opp_val = getattr(item, "fsmtest_PreconditionDeclaration", None)
                    
                    setattr(item, "fsmtest_PreconditionDeclaration", self)
                    

    @property
    def fsmtest_TransitionDeclaration(self):
        return self.__fsmtest_TransitionDeclaration

    @fsmtest_TransitionDeclaration.setter
    def fsmtest_TransitionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration", None)
        self.__fsmtest_TransitionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_StateDeclaration14"):
                opp_val = getattr(old_value, "fsmtest_StateDeclaration14", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_StateDeclaration14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_StateDeclaration14"):
                opp_val = getattr(value, "fsmtest_StateDeclaration14", None)
                setattr(value, "fsmtest_StateDeclaration14", self)

    @property
    def fsmtest_TransitionDeclaration19(self):
        return self.__fsmtest_TransitionDeclaration19

    @fsmtest_TransitionDeclaration19.setter
    def fsmtest_TransitionDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration19", None)
        self.__fsmtest_TransitionDeclaration19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_GuardDeclaration20"):
                    opp_val = getattr(item, "fsmtest_GuardDeclaration20", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_GuardDeclaration20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_GuardDeclaration20"):
                    opp_val = getattr(item, "fsmtest_GuardDeclaration20", None)
                    
                    setattr(item, "fsmtest_GuardDeclaration20", self)
                    

    @property
    def fsmtest_TransitionDeclaration38(self):
        return self.__fsmtest_TransitionDeclaration38

    @fsmtest_TransitionDeclaration38.setter
    def fsmtest_TransitionDeclaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration38", None)
        self.__fsmtest_TransitionDeclaration38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_StateDeclaration37"):
                opp_val = getattr(old_value, "fsmtest_StateDeclaration37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_StateDeclaration37"):
                opp_val = getattr(value, "fsmtest_StateDeclaration37", None)
                if opp_val is None:
                    setattr(value, "fsmtest_StateDeclaration37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmtest_TransitionDeclaration16(self):
        return self.__fsmtest_TransitionDeclaration16

    @fsmtest_TransitionDeclaration16.setter
    def fsmtest_TransitionDeclaration16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_TransitionDeclaration__fsmtest_TransitionDeclaration16", None)
        self.__fsmtest_TransitionDeclaration16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_SignalDeclaration17"):
                opp_val = getattr(old_value, "fsmtest_SignalDeclaration17", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_SignalDeclaration17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_SignalDeclaration17"):
                opp_val = getattr(value, "fsmtest_SignalDeclaration17", None)
                setattr(value, "fsmtest_SignalDeclaration17", self)

class fsmtest_SignalDeclaration:

    def __init__(self, port: str, signame: str, intVal: int, strVal: str, fsmtest_SignalDeclaration: "fsmtest_GuardDeclaration" = None, fsmtest_SignalDeclaration17: "fsmtest_TransitionDeclaration" = None, fsmtest_SignalDeclaration32: "fsmtest_PostconditionDeclaration" = None, fsmtest_SignalDeclaration26: "fsmtest_ConditionDeclaration" = None, fsmtest_SignalDeclaration29: "fsmtest_PreconditionDeclaration" = None):
        self.port = port
        self.signame = signame
        self.intVal = intVal
        self.strVal = strVal
        self.fsmtest_SignalDeclaration = fsmtest_SignalDeclaration
        self.fsmtest_SignalDeclaration17 = fsmtest_SignalDeclaration17
        self.fsmtest_SignalDeclaration32 = fsmtest_SignalDeclaration32
        self.fsmtest_SignalDeclaration26 = fsmtest_SignalDeclaration26
        self.fsmtest_SignalDeclaration29 = fsmtest_SignalDeclaration29
        
    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def intVal(self) -> int:
        return self.__intVal

    @intVal.setter
    def intVal(self, intVal: int):
        self.__intVal = intVal

    @property
    def signame(self) -> str:
        return self.__signame

    @signame.setter
    def signame(self, signame: str):
        self.__signame = signame

    @property
    def strVal(self) -> str:
        return self.__strVal

    @strVal.setter
    def strVal(self, strVal: str):
        self.__strVal = strVal

    @property
    def fsmtest_SignalDeclaration26(self):
        return self.__fsmtest_SignalDeclaration26

    @fsmtest_SignalDeclaration26.setter
    def fsmtest_SignalDeclaration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SignalDeclaration__fsmtest_SignalDeclaration26", None)
        self.__fsmtest_SignalDeclaration26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_ConditionDeclaration"):
                opp_val = getattr(old_value, "fsmtest_ConditionDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_ConditionDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_ConditionDeclaration"):
                opp_val = getattr(value, "fsmtest_ConditionDeclaration", None)
                setattr(value, "fsmtest_ConditionDeclaration", self)

    @property
    def fsmtest_SignalDeclaration29(self):
        return self.__fsmtest_SignalDeclaration29

    @fsmtest_SignalDeclaration29.setter
    def fsmtest_SignalDeclaration29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SignalDeclaration__fsmtest_SignalDeclaration29", None)
        self.__fsmtest_SignalDeclaration29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_PreconditionDeclaration28"):
                opp_val = getattr(old_value, "fsmtest_PreconditionDeclaration28", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_PreconditionDeclaration28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_PreconditionDeclaration28"):
                opp_val = getattr(value, "fsmtest_PreconditionDeclaration28", None)
                setattr(value, "fsmtest_PreconditionDeclaration28", self)

    @property
    def fsmtest_SignalDeclaration17(self):
        return self.__fsmtest_SignalDeclaration17

    @fsmtest_SignalDeclaration17.setter
    def fsmtest_SignalDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SignalDeclaration__fsmtest_SignalDeclaration17", None)
        self.__fsmtest_SignalDeclaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_TransitionDeclaration16"):
                opp_val = getattr(old_value, "fsmtest_TransitionDeclaration16", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_TransitionDeclaration16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_TransitionDeclaration16"):
                opp_val = getattr(value, "fsmtest_TransitionDeclaration16", None)
                setattr(value, "fsmtest_TransitionDeclaration16", self)

    @property
    def fsmtest_SignalDeclaration32(self):
        return self.__fsmtest_SignalDeclaration32

    @fsmtest_SignalDeclaration32.setter
    def fsmtest_SignalDeclaration32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SignalDeclaration__fsmtest_SignalDeclaration32", None)
        self.__fsmtest_SignalDeclaration32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_PostconditionDeclaration31"):
                opp_val = getattr(old_value, "fsmtest_PostconditionDeclaration31", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_PostconditionDeclaration31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_PostconditionDeclaration31"):
                opp_val = getattr(value, "fsmtest_PostconditionDeclaration31", None)
                setattr(value, "fsmtest_PostconditionDeclaration31", self)

    @property
    def fsmtest_SignalDeclaration(self):
        return self.__fsmtest_SignalDeclaration

    @fsmtest_SignalDeclaration.setter
    def fsmtest_SignalDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_SignalDeclaration__fsmtest_SignalDeclaration", None)
        self.__fsmtest_SignalDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_GuardDeclaration"):
                opp_val = getattr(old_value, "fsmtest_GuardDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_GuardDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_GuardDeclaration"):
                opp_val = getattr(value, "fsmtest_GuardDeclaration", None)
                setattr(value, "fsmtest_GuardDeclaration", self)

class fsmtest_GuardDeclaration:

    pass
class fsmtest_RandomTest:

    def __init__(self, name: str, fsmtest_RandomTest: "fsmtest_Model" = None, fsmtest_RandomTest6: "fsmtest_FsmDefinition" = None, fsmtest_RandomTest9: "fsmtest_LoopsDeclaration" = None, fsmtest_RandomTest11: "fsmtest_SeedDeclaration" = None):
        self.name = name
        self.fsmtest_RandomTest = fsmtest_RandomTest
        self.fsmtest_RandomTest6 = fsmtest_RandomTest6
        self.fsmtest_RandomTest9 = fsmtest_RandomTest9
        self.fsmtest_RandomTest11 = fsmtest_RandomTest11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmtest_RandomTest(self):
        return self.__fsmtest_RandomTest

    @fsmtest_RandomTest.setter
    def fsmtest_RandomTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_RandomTest__fsmtest_RandomTest", None)
        self.__fsmtest_RandomTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_Model2"):
                opp_val = getattr(old_value, "fsmtest_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_Model2"):
                opp_val = getattr(value, "fsmtest_Model2", None)
                if opp_val is None:
                    setattr(value, "fsmtest_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmtest_RandomTest11(self):
        return self.__fsmtest_RandomTest11

    @fsmtest_RandomTest11.setter
    def fsmtest_RandomTest11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_RandomTest__fsmtest_RandomTest11", None)
        self.__fsmtest_RandomTest11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_SeedDeclaration"):
                opp_val = getattr(old_value, "fsmtest_SeedDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_SeedDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_SeedDeclaration"):
                opp_val = getattr(value, "fsmtest_SeedDeclaration", None)
                setattr(value, "fsmtest_SeedDeclaration", self)

    @property
    def fsmtest_RandomTest9(self):
        return self.__fsmtest_RandomTest9

    @fsmtest_RandomTest9.setter
    def fsmtest_RandomTest9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_RandomTest__fsmtest_RandomTest9", None)
        self.__fsmtest_RandomTest9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_LoopsDeclaration"):
                opp_val = getattr(old_value, "fsmtest_LoopsDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_LoopsDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_LoopsDeclaration"):
                opp_val = getattr(value, "fsmtest_LoopsDeclaration", None)
                setattr(value, "fsmtest_LoopsDeclaration", self)

    @property
    def fsmtest_RandomTest6(self):
        return self.__fsmtest_RandomTest6

    @fsmtest_RandomTest6.setter
    def fsmtest_RandomTest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_RandomTest__fsmtest_RandomTest6", None)
        self.__fsmtest_RandomTest6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_FsmDefinition7"):
                opp_val = getattr(old_value, "fsmtest_FsmDefinition7", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_FsmDefinition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_FsmDefinition7"):
                opp_val = getattr(value, "fsmtest_FsmDefinition7", None)
                setattr(value, "fsmtest_FsmDefinition7", self)

class fsmtest_FsmDefinition:

    def __init__(self, name: str, fsmtest_FsmDefinition: "fsmtest_Model" = None, fsmtest_FsmDefinition4: set["fsmtest_StateDeclaration"] = None, fsmtest_FsmDefinition7: "fsmtest_RandomTest" = None):
        self.name = name
        self.fsmtest_FsmDefinition = fsmtest_FsmDefinition
        self.fsmtest_FsmDefinition4 = fsmtest_FsmDefinition4 if fsmtest_FsmDefinition4 is not None else set()
        self.fsmtest_FsmDefinition7 = fsmtest_FsmDefinition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmtest_FsmDefinition4(self):
        return self.__fsmtest_FsmDefinition4

    @fsmtest_FsmDefinition4.setter
    def fsmtest_FsmDefinition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_FsmDefinition__fsmtest_FsmDefinition4", None)
        self.__fsmtest_FsmDefinition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmtest_StateDeclaration"):
                    opp_val = getattr(item, "fsmtest_StateDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmtest_StateDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmtest_StateDeclaration"):
                    opp_val = getattr(item, "fsmtest_StateDeclaration", None)
                    
                    setattr(item, "fsmtest_StateDeclaration", self)
                    

    @property
    def fsmtest_FsmDefinition7(self):
        return self.__fsmtest_FsmDefinition7

    @fsmtest_FsmDefinition7.setter
    def fsmtest_FsmDefinition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_FsmDefinition__fsmtest_FsmDefinition7", None)
        self.__fsmtest_FsmDefinition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_RandomTest6"):
                opp_val = getattr(old_value, "fsmtest_RandomTest6", None)
                if opp_val == self:
                    setattr(old_value, "fsmtest_RandomTest6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_RandomTest6"):
                opp_val = getattr(value, "fsmtest_RandomTest6", None)
                setattr(value, "fsmtest_RandomTest6", self)

    @property
    def fsmtest_FsmDefinition(self):
        return self.__fsmtest_FsmDefinition

    @fsmtest_FsmDefinition.setter
    def fsmtest_FsmDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmtest_FsmDefinition__fsmtest_FsmDefinition", None)
        self.__fsmtest_FsmDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmtest_Model"):
                opp_val = getattr(old_value, "fsmtest_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmtest_Model"):
                opp_val = getattr(value, "fsmtest_Model", None)
                if opp_val is None:
                    setattr(value, "fsmtest_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsmtest_Model:

    pass
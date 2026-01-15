from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RootOut:

    pass
class RootIn:

    pass
class traces_E(RootOut):

    def __init__(self, name: str, traces_E: "traces_R2_Trace" = None, traces_E27: "traces_D" = None, traces_E22: "traces_D" = None):
        self.name = name
        self.traces_E = traces_E
        self.traces_E27 = traces_E27
        self.traces_E22 = traces_E22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_E27(self):
        return self.__traces_E27

    @traces_E27.setter
    def traces_E27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_E__traces_E27", None)
        self.__traces_E27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_D28"):
                opp_val = getattr(old_value, "traces_D28", None)
                if opp_val == self:
                    setattr(old_value, "traces_D28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_D28"):
                opp_val = getattr(value, "traces_D28", None)
                setattr(value, "traces_D28", self)

    @property
    def traces_E(self):
        return self.__traces_E

    @traces_E.setter
    def traces_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_E__traces_E", None)
        self.__traces_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_R2_Trace11"):
                opp_val = getattr(old_value, "traces_R2_Trace11", None)
                if opp_val == self:
                    setattr(old_value, "traces_R2_Trace11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_R2_Trace11"):
                opp_val = getattr(value, "traces_R2_Trace11", None)
                setattr(value, "traces_R2_Trace11", self)

    @property
    def traces_E22(self):
        return self.__traces_E22

    @traces_E22.setter
    def traces_E22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_E__traces_E22", None)
        self.__traces_E22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_D21"):
                opp_val = getattr(old_value, "traces_D21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_D21"):
                opp_val = getattr(value, "traces_D21", None)
                if opp_val is None:
                    setattr(value, "traces_D21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traces_B(RootIn):

    def __init__(self, name: str, traces_B14: "traces_A" = None, traces_B: "traces_R2_Trace" = None, traces_B18: "traces_A" = None):
        self.name = name
        self.traces_B14 = traces_B14
        self.traces_B = traces_B
        self.traces_B18 = traces_B18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_B(self):
        return self.__traces_B

    @traces_B.setter
    def traces_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_B__traces_B", None)
        self.__traces_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_R2_Trace"):
                opp_val = getattr(old_value, "traces_R2_Trace", None)
                if opp_val == self:
                    setattr(old_value, "traces_R2_Trace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_R2_Trace"):
                opp_val = getattr(value, "traces_R2_Trace", None)
                setattr(value, "traces_R2_Trace", self)

    @property
    def traces_B14(self):
        return self.__traces_B14

    @traces_B14.setter
    def traces_B14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_B__traces_B14", None)
        self.__traces_B14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_A13"):
                opp_val = getattr(old_value, "traces_A13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_A13"):
                opp_val = getattr(value, "traces_A13", None)
                if opp_val is None:
                    setattr(value, "traces_A13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traces_B18(self):
        return self.__traces_B18

    @traces_B18.setter
    def traces_B18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_B__traces_B18", None)
        self.__traces_B18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_A19"):
                opp_val = getattr(old_value, "traces_A19", None)
                if opp_val == self:
                    setattr(old_value, "traces_A19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_A19"):
                opp_val = getattr(value, "traces_A19", None)
                setattr(value, "traces_A19", self)

class traces_C(RootIn):

    def __init__(self, name: str, traces_C: "traces_A" = None):
        self.name = name
        self.traces_C = traces_C
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_C(self):
        return self.__traces_C

    @traces_C.setter
    def traces_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_C__traces_C", None)
        self.__traces_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_A16"):
                opp_val = getattr(old_value, "traces_A16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_A16"):
                opp_val = getattr(value, "traces_A16", None)
                if opp_val is None:
                    setattr(value, "traces_A16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traces_RootOut(ABC):

    pass
class traces_RootIn(ABC):

    pass
class traces_Trace(ABC):

    pass
class traces_D(RootOut):

    def __init__(self, name: str, traces_D: "traces_R1_Trace" = None, traces_D8: "traces_R1_Trace" = None, traces_D25: "traces_D" = None, traces_D23: "traces_D" = None, traces_D28: "traces_E" = None, traces_D21: set["traces_E"] = None):
        self.name = name
        self.traces_D = traces_D
        self.traces_D8 = traces_D8
        self.traces_D25 = traces_D25
        self.traces_D23 = traces_D23
        self.traces_D28 = traces_D28
        self.traces_D21 = traces_D21 if traces_D21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_D8(self):
        return self.__traces_D8

    @traces_D8.setter
    def traces_D8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D8", None)
        self.__traces_D8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_R1_Trace7"):
                opp_val = getattr(old_value, "traces_R1_Trace7", None)
                if opp_val == self:
                    setattr(old_value, "traces_R1_Trace7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_R1_Trace7"):
                opp_val = getattr(value, "traces_R1_Trace7", None)
                setattr(value, "traces_R1_Trace7", self)

    @property
    def traces_D21(self):
        return self.__traces_D21

    @traces_D21.setter
    def traces_D21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D21", None)
        self.__traces_D21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_E22"):
                    opp_val = getattr(item, "traces_E22", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_E22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_E22"):
                    opp_val = getattr(item, "traces_E22", None)
                    
                    setattr(item, "traces_E22", self)
                    

    @property
    def traces_D25(self):
        return self.__traces_D25

    @traces_D25.setter
    def traces_D25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D25", None)
        self.__traces_D25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_D23"):
                opp_val = getattr(old_value, "traces_D23", None)
                if opp_val == self:
                    setattr(old_value, "traces_D23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_D23"):
                opp_val = getattr(value, "traces_D23", None)
                setattr(value, "traces_D23", self)

    @property
    def traces_D23(self):
        return self.__traces_D23

    @traces_D23.setter
    def traces_D23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D23", None)
        self.__traces_D23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_D25"):
                opp_val = getattr(old_value, "traces_D25", None)
                if opp_val == self:
                    setattr(old_value, "traces_D25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_D25"):
                opp_val = getattr(value, "traces_D25", None)
                setattr(value, "traces_D25", self)

    @property
    def traces_D(self):
        return self.__traces_D

    @traces_D.setter
    def traces_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D", None)
        self.__traces_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_R1_Trace5"):
                opp_val = getattr(old_value, "traces_R1_Trace5", None)
                if opp_val == self:
                    setattr(old_value, "traces_R1_Trace5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_R1_Trace5"):
                opp_val = getattr(value, "traces_R1_Trace5", None)
                setattr(value, "traces_R1_Trace5", self)

    @property
    def traces_D28(self):
        return self.__traces_D28

    @traces_D28.setter
    def traces_D28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_D__traces_D28", None)
        self.__traces_D28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_E27"):
                opp_val = getattr(old_value, "traces_E27", None)
                if opp_val == self:
                    setattr(old_value, "traces_E27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_E27"):
                opp_val = getattr(value, "traces_E27", None)
                setattr(value, "traces_E27", self)

class traces_A(RootIn):

    def __init__(self, name: str, traces_A: "traces_R1_Trace" = None, traces_A13: set["traces_B"] = None, traces_A16: set["traces_C"] = None, traces_A19: "traces_B" = None):
        self.name = name
        self.traces_A = traces_A
        self.traces_A13 = traces_A13 if traces_A13 is not None else set()
        self.traces_A16 = traces_A16 if traces_A16 is not None else set()
        self.traces_A19 = traces_A19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traces_A(self):
        return self.__traces_A

    @traces_A.setter
    def traces_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_A__traces_A", None)
        self.__traces_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_R1_Trace"):
                opp_val = getattr(old_value, "traces_R1_Trace", None)
                if opp_val == self:
                    setattr(old_value, "traces_R1_Trace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_R1_Trace"):
                opp_val = getattr(value, "traces_R1_Trace", None)
                setattr(value, "traces_R1_Trace", self)

    @property
    def traces_A16(self):
        return self.__traces_A16

    @traces_A16.setter
    def traces_A16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_A__traces_A16", None)
        self.__traces_A16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_C"):
                    opp_val = getattr(item, "traces_C", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_C"):
                    opp_val = getattr(item, "traces_C", None)
                    
                    setattr(item, "traces_C", self)
                    

    @property
    def traces_A19(self):
        return self.__traces_A19

    @traces_A19.setter
    def traces_A19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_A__traces_A19", None)
        self.__traces_A19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_B18"):
                opp_val = getattr(old_value, "traces_B18", None)
                if opp_val == self:
                    setattr(old_value, "traces_B18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_B18"):
                opp_val = getattr(value, "traces_B18", None)
                setattr(value, "traces_B18", self)

    @property
    def traces_A13(self):
        return self.__traces_A13

    @traces_A13.setter
    def traces_A13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_A__traces_A13", None)
        self.__traces_A13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traces_B14"):
                    opp_val = getattr(item, "traces_B14", None)
                    
                    if opp_val == self:
                        setattr(item, "traces_B14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traces_B14"):
                    opp_val = getattr(item, "traces_B14", None)
                    
                    setattr(item, "traces_B14", self)
                    

class Trace:

    pass
class traces_R2_Trace(Trace):

    pass
class traces_R1_Trace(Trace):

    pass
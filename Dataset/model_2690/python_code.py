from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class cycle_C:

    pass
class cycle_B:

    def __init__(self, x: float, y: float, cycle_B: "cycle_A" = None, cycle_B2: "cycle_A" = None, cycle_B5: "cycle_C" = None):
        self.x = x
        self.y = y
        self.cycle_B = cycle_B
        self.cycle_B2 = cycle_B2
        self.cycle_B5 = cycle_B5
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def cycle_B2(self):
        return self.__cycle_B2

    @cycle_B2.setter
    def cycle_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_B__cycle_B2", None)
        self.__cycle_B2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cycle_A3"):
                opp_val = getattr(old_value, "cycle_A3", None)
                if opp_val == self:
                    setattr(old_value, "cycle_A3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cycle_A3"):
                opp_val = getattr(value, "cycle_A3", None)
                setattr(value, "cycle_A3", self)

    @property
    def cycle_B(self):
        return self.__cycle_B

    @cycle_B.setter
    def cycle_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_B__cycle_B", None)
        self.__cycle_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cycle_A"):
                opp_val = getattr(old_value, "cycle_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cycle_A"):
                opp_val = getattr(value, "cycle_A", None)
                if opp_val is None:
                    setattr(value, "cycle_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cycle_B5(self):
        return self.__cycle_B5

    @cycle_B5.setter
    def cycle_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_B__cycle_B5", None)
        self.__cycle_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cycle_C"):
                opp_val = getattr(old_value, "cycle_C", None)
                if opp_val == self:
                    setattr(old_value, "cycle_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cycle_C"):
                opp_val = getattr(value, "cycle_C", None)
                setattr(value, "cycle_C", self)

class cycle_A:

    def __init__(self, i: int, j: int, cycle_A: set["cycle_B"] = None, cycle_A3: "cycle_B" = None, cycle_A8: "cycle_C" = None):
        self.i = i
        self.j = j
        self.cycle_A = cycle_A if cycle_A is not None else set()
        self.cycle_A3 = cycle_A3
        self.cycle_A8 = cycle_A8
        
    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def j(self) -> int:
        return self.__j

    @j.setter
    def j(self, j: int):
        self.__j = j

    @property
    def cycle_A3(self):
        return self.__cycle_A3

    @cycle_A3.setter
    def cycle_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_A__cycle_A3", None)
        self.__cycle_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cycle_B2"):
                opp_val = getattr(old_value, "cycle_B2", None)
                if opp_val == self:
                    setattr(old_value, "cycle_B2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cycle_B2"):
                opp_val = getattr(value, "cycle_B2", None)
                setattr(value, "cycle_B2", self)

    @property
    def cycle_A(self):
        return self.__cycle_A

    @cycle_A.setter
    def cycle_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_A__cycle_A", None)
        self.__cycle_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cycle_B"):
                    opp_val = getattr(item, "cycle_B", None)
                    
                    if opp_val == self:
                        setattr(item, "cycle_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cycle_B"):
                    opp_val = getattr(item, "cycle_B", None)
                    
                    setattr(item, "cycle_B", self)
                    

    @property
    def cycle_A8(self):
        return self.__cycle_A8

    @cycle_A8.setter
    def cycle_A8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cycle_A__cycle_A8", None)
        self.__cycle_A8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cycle_C7"):
                opp_val = getattr(old_value, "cycle_C7", None)
                if opp_val == self:
                    setattr(old_value, "cycle_C7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cycle_C7"):
                opp_val = getattr(value, "cycle_C7", None)
                setattr(value, "cycle_C7", self)

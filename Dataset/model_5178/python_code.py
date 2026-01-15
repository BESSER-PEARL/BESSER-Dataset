from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class pmtest_C(A):

    pass
class pmtest_B(A):

    pass
class pmtest_D:

    def __init__(self, j: int, pmtest_D: "pmtest_A" = None):
        self.j = j
        self.pmtest_D = pmtest_D
        
    @property
    def j(self) -> int:
        return self.__j

    @j.setter
    def j(self, j: int):
        self.__j = j

    @property
    def pmtest_D(self):
        return self.__pmtest_D

    @pmtest_D.setter
    def pmtest_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_D__pmtest_D", None)
        self.__pmtest_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pmtest_A"):
                opp_val = getattr(old_value, "pmtest_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pmtest_A"):
                opp_val = getattr(value, "pmtest_A", None)
                if opp_val is None:
                    setattr(value, "pmtest_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pmtest_A:

    def __init__(self, i: int, A: "pmtest_A" = None, s: set["pmtest_A"] = None, A4: "pmtest_A" = None, t: set["pmtest_A"] = None, pmtest_A: set["pmtest_D"] = None):
        self.i = i
        self.A = A
        self.s = s if s is not None else set()
        self.A4 = A4
        self.t = t if t is not None else set()
        self.pmtest_A = pmtest_A if pmtest_A is not None else set()
        
    @property
    def i(self) -> int:
        return self.__i

    @i.setter
    def i(self, i: int):
        self.__i = i

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_A__s", None)
        self.__s = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A"):
                    opp_val = getattr(item, "A", None)
                    
                    if opp_val == self:
                        setattr(item, "A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A"):
                    opp_val = getattr(item, "A", None)
                    
                    setattr(item, "A", self)
                    

    @property
    def pmtest_A(self):
        return self.__pmtest_A

    @pmtest_A.setter
    def pmtest_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_A__pmtest_A", None)
        self.__pmtest_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pmtest_D"):
                    opp_val = getattr(item, "pmtest_D", None)
                    
                    if opp_val == self:
                        setattr(item, "pmtest_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pmtest_D"):
                    opp_val = getattr(item, "pmtest_D", None)
                    
                    setattr(item, "pmtest_D", self)
                    

    @property
    def A4(self):
        return self.__A4

    @A4.setter
    def A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_A__A4", None)
        self.__A4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "t"):
                opp_val = getattr(old_value, "t", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "t"):
                opp_val = getattr(value, "t", None)
                if opp_val is None:
                    setattr(value, "t", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_A__A", None)
        self.__A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "s"):
                opp_val = getattr(old_value, "s", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "s"):
                opp_val = getattr(value, "s", None)
                if opp_val is None:
                    setattr(value, "s", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pmtest_A__t", None)
        self.__t = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A4"):
                    opp_val = getattr(item, "A4", None)
                    
                    if opp_val == self:
                        setattr(item, "A4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A4"):
                    opp_val = getattr(item, "A4", None)
                    
                    setattr(item, "A4", self)
                    

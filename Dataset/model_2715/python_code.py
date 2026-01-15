from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class errorkref_M:

    def __init__(self, id: str, errorkref_M: set["errorkref_I"] = None):
        self.id = id
        self.errorkref_M = errorkref_M if errorkref_M is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errorkref_M(self):
        return self.__errorkref_M

    @errorkref_M.setter
    def errorkref_M(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_M__errorkref_M", None)
        self.__errorkref_M = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errorkref_I"):
                    opp_val = getattr(item, "errorkref_I", None)
                    
                    if opp_val == self:
                        setattr(item, "errorkref_I", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errorkref_I"):
                    opp_val = getattr(item, "errorkref_I", None)
                    
                    setattr(item, "errorkref_I", self)
                    

class errorkref_I:

    def __init__(self, name: str, errorkref_I: "errorkref_M" = None):
        self.name = name
        self.errorkref_I = errorkref_I
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errorkref_I(self):
        return self.__errorkref_I

    @errorkref_I.setter
    def errorkref_I(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_I__errorkref_I", None)
        self.__errorkref_I = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_M"):
                opp_val = getattr(old_value, "errorkref_M", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_M"):
                opp_val = getattr(value, "errorkref_M", None)
                if opp_val is None:
                    setattr(value, "errorkref_M", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errorkref_J:

    def __init__(self, id: str, errorkref_J: "errorkref_E" = None):
        self.id = id
        self.errorkref_J = errorkref_J
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errorkref_J(self):
        return self.__errorkref_J

    @errorkref_J.setter
    def errorkref_J(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_J__errorkref_J", None)
        self.__errorkref_J = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_E"):
                opp_val = getattr(old_value, "errorkref_E", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_E"):
                opp_val = getattr(value, "errorkref_E", None)
                if opp_val is None:
                    setattr(value, "errorkref_E", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errorkref_K:

    def __init__(self, ids: str, errorkref_K: "errorkref_G" = None):
        self.ids = ids
        self.errorkref_K = errorkref_K
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def errorkref_K(self):
        return self.__errorkref_K

    @errorkref_K.setter
    def errorkref_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_K__errorkref_K", None)
        self.__errorkref_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_G20"):
                opp_val = getattr(old_value, "errorkref_G20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_G20"):
                opp_val = getattr(value, "errorkref_G20", None)
                if opp_val is None:
                    setattr(value, "errorkref_G20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class M:

    pass
class errorkref_Q:

    def __init__(self, id: str, errorkref_Q: "errorkref_F" = None):
        self.id = id
        self.errorkref_Q = errorkref_Q
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errorkref_Q(self):
        return self.__errorkref_Q

    @errorkref_Q.setter
    def errorkref_Q(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_Q__errorkref_Q", None)
        self.__errorkref_Q = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_F18"):
                opp_val = getattr(old_value, "errorkref_F18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_F18"):
                opp_val = getattr(value, "errorkref_F18", None)
                if opp_val is None:
                    setattr(value, "errorkref_F18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class E:

    pass
class G:

    pass
class D:

    pass
class errorkref_E(D):

    pass
class errorkref_N:

    def __init__(self, id: str, errorkref_N: "errorkref_D" = None):
        self.id = id
        self.errorkref_N = errorkref_N
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errorkref_N(self):
        return self.__errorkref_N

    @errorkref_N.setter
    def errorkref_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_N__errorkref_N", None)
        self.__errorkref_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_D15"):
                opp_val = getattr(old_value, "errorkref_D15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_D15"):
                opp_val = getattr(value, "errorkref_D15", None)
                if opp_val is None:
                    setattr(value, "errorkref_D15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errorkref_F(E):

    pass
class B:

    pass
class errorkref_G(M):

    pass
class errorkref_B:

    def __init__(self, id: str, errorkref_B: "errorkref_A" = None, errorkref_B8: "errorkref_G" = None, errorkref_B23: "errorkref_L1" = None):
        self.id = id
        self.errorkref_B = errorkref_B
        self.errorkref_B8 = errorkref_B8
        self.errorkref_B23 = errorkref_B23
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def errorkref_B(self):
        return self.__errorkref_B

    @errorkref_B.setter
    def errorkref_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_B__errorkref_B", None)
        self.__errorkref_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_A6"):
                opp_val = getattr(old_value, "errorkref_A6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_A6"):
                opp_val = getattr(value, "errorkref_A6", None)
                if opp_val is None:
                    setattr(value, "errorkref_A6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def errorkref_B8(self):
        return self.__errorkref_B8

    @errorkref_B8.setter
    def errorkref_B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_B__errorkref_B8", None)
        self.__errorkref_B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_G"):
                opp_val = getattr(old_value, "errorkref_G", None)
                if opp_val == self:
                    setattr(old_value, "errorkref_G", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_G"):
                opp_val = getattr(value, "errorkref_G", None)
                setattr(value, "errorkref_G", self)

    @property
    def errorkref_B23(self):
        return self.__errorkref_B23

    @errorkref_B23.setter
    def errorkref_B23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_B__errorkref_B23", None)
        self.__errorkref_B23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_L122"):
                opp_val = getattr(old_value, "errorkref_L122", None)
                if opp_val == self:
                    setattr(old_value, "errorkref_L122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_L122"):
                opp_val = getattr(value, "errorkref_L122", None)
                setattr(value, "errorkref_L122", self)

class errorkref_L1:

    def __init__(self, since: str, errorkref_L1: "errorkref_C" = None, errorkref_L122: "errorkref_B" = None, errorkref_L125: "errorkref_G" = None):
        self.since = since
        self.errorkref_L1 = errorkref_L1
        self.errorkref_L122 = errorkref_L122
        self.errorkref_L125 = errorkref_L125
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def errorkref_L125(self):
        return self.__errorkref_L125

    @errorkref_L125.setter
    def errorkref_L125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_L1__errorkref_L125", None)
        self.__errorkref_L125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_G26"):
                opp_val = getattr(old_value, "errorkref_G26", None)
                if opp_val == self:
                    setattr(old_value, "errorkref_G26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_G26"):
                opp_val = getattr(value, "errorkref_G26", None)
                setattr(value, "errorkref_G26", self)

    @property
    def errorkref_L1(self):
        return self.__errorkref_L1

    @errorkref_L1.setter
    def errorkref_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_L1__errorkref_L1", None)
        self.__errorkref_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_C4"):
                opp_val = getattr(old_value, "errorkref_C4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_C4"):
                opp_val = getattr(value, "errorkref_C4", None)
                if opp_val is None:
                    setattr(value, "errorkref_C4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def errorkref_L122(self):
        return self.__errorkref_L122

    @errorkref_L122.setter
    def errorkref_L122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_L1__errorkref_L122", None)
        self.__errorkref_L122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_B23"):
                opp_val = getattr(old_value, "errorkref_B23", None)
                if opp_val == self:
                    setattr(old_value, "errorkref_B23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_B23"):
                opp_val = getattr(value, "errorkref_B23", None)
                setattr(value, "errorkref_B23", self)

class errorkref_D(G):

    pass
class errorkref_A(B):

    def __init__(self, name: str, errorkref_A: "errorkref_C" = None, errorkref_A6: set["errorkref_B"] = None):
        self.name = name
        self.errorkref_A = errorkref_A
        self.errorkref_A6 = errorkref_A6 if errorkref_A6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def errorkref_A6(self):
        return self.__errorkref_A6

    @errorkref_A6.setter
    def errorkref_A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_A__errorkref_A6", None)
        self.__errorkref_A6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errorkref_B"):
                    opp_val = getattr(item, "errorkref_B", None)
                    
                    if opp_val == self:
                        setattr(item, "errorkref_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errorkref_B"):
                    opp_val = getattr(item, "errorkref_B", None)
                    
                    setattr(item, "errorkref_B", self)
                    

    @property
    def errorkref_A(self):
        return self.__errorkref_A

    @errorkref_A.setter
    def errorkref_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errorkref_A__errorkref_A", None)
        self.__errorkref_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errorkref_C"):
                opp_val = getattr(old_value, "errorkref_C", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errorkref_C"):
                opp_val = getattr(value, "errorkref_C", None)
                if opp_val is None:
                    setattr(value, "errorkref_C", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errorkref_C:

    pass
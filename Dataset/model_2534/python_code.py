from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test101_M:

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class test101_Q:

    def __init__(self, id: str, test101_Q: "test101_F" = None):
        self.id = id
        self.test101_Q = test101_Q
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test101_Q(self):
        return self.__test101_Q

    @test101_Q.setter
    def test101_Q(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_Q__test101_Q", None)
        self.__test101_Q = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_F18"):
                opp_val = getattr(old_value, "test101_F18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_F18"):
                opp_val = getattr(value, "test101_F18", None)
                if opp_val is None:
                    setattr(value, "test101_F18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class E:

    pass
class test101_J:

    def __init__(self, id: str, test101_J: "test101_E" = None):
        self.id = id
        self.test101_J = test101_J
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test101_J(self):
        return self.__test101_J

    @test101_J.setter
    def test101_J(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_J__test101_J", None)
        self.__test101_J = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_E"):
                opp_val = getattr(old_value, "test101_E", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_E"):
                opp_val = getattr(value, "test101_E", None)
                if opp_val is None:
                    setattr(value, "test101_E", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class D:

    pass
class test101_E(D):

    pass
class test101_N:

    def __init__(self, id: str, test101_N: "test101_D" = None):
        self.id = id
        self.test101_N = test101_N
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test101_N(self):
        return self.__test101_N

    @test101_N.setter
    def test101_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_N__test101_N", None)
        self.__test101_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_D15"):
                opp_val = getattr(old_value, "test101_D15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_D15"):
                opp_val = getattr(value, "test101_D15", None)
                if opp_val is None:
                    setattr(value, "test101_D15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test101_K:

    def __init__(self, ids: str, test101_K: "test101_G" = None):
        self.ids = ids
        self.test101_K = test101_K
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def test101_K(self):
        return self.__test101_K

    @test101_K.setter
    def test101_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_K__test101_K", None)
        self.__test101_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_G22"):
                opp_val = getattr(old_value, "test101_G22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_G22"):
                opp_val = getattr(value, "test101_G22", None)
                if opp_val is None:
                    setattr(value, "test101_G22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test101_I:

    def __init__(self, name: str, test101_I: "test101_G" = None):
        self.name = name
        self.test101_I = test101_I
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test101_I(self):
        return self.__test101_I

    @test101_I.setter
    def test101_I(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_I__test101_I", None)
        self.__test101_I = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_G20"):
                opp_val = getattr(old_value, "test101_G20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_G20"):
                opp_val = getattr(value, "test101_G20", None)
                if opp_val is None:
                    setattr(value, "test101_G20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class M:

    pass
class test101_G(M):

    pass
class test101_B:

    def __init__(self, id: str, test101_B: "test101_A" = None, test101_B8: "test101_G" = None, test101_B25: "test101_L1" = None):
        self.id = id
        self.test101_B = test101_B
        self.test101_B8 = test101_B8
        self.test101_B25 = test101_B25
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test101_B(self):
        return self.__test101_B

    @test101_B.setter
    def test101_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_B__test101_B", None)
        self.__test101_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_A6"):
                opp_val = getattr(old_value, "test101_A6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_A6"):
                opp_val = getattr(value, "test101_A6", None)
                if opp_val is None:
                    setattr(value, "test101_A6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test101_B8(self):
        return self.__test101_B8

    @test101_B8.setter
    def test101_B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_B__test101_B8", None)
        self.__test101_B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_G"):
                opp_val = getattr(old_value, "test101_G", None)
                if opp_val == self:
                    setattr(old_value, "test101_G", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_G"):
                opp_val = getattr(value, "test101_G", None)
                setattr(value, "test101_G", self)

    @property
    def test101_B25(self):
        return self.__test101_B25

    @test101_B25.setter
    def test101_B25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_B__test101_B25", None)
        self.__test101_B25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_L124"):
                opp_val = getattr(old_value, "test101_L124", None)
                if opp_val == self:
                    setattr(old_value, "test101_L124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_L124"):
                opp_val = getattr(value, "test101_L124", None)
                setattr(value, "test101_L124", self)

class B:

    pass
class test101_F(E):

    pass
class G:

    pass
class test101_A(B):

    def __init__(self, name: str, test101_A: "test101_C" = None, test101_A6: set["test101_B"] = None):
        self.name = name
        self.test101_A = test101_A
        self.test101_A6 = test101_A6 if test101_A6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test101_A6(self):
        return self.__test101_A6

    @test101_A6.setter
    def test101_A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_A__test101_A6", None)
        self.__test101_A6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test101_B"):
                    opp_val = getattr(item, "test101_B", None)
                    
                    if opp_val == self:
                        setattr(item, "test101_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test101_B"):
                    opp_val = getattr(item, "test101_B", None)
                    
                    setattr(item, "test101_B", self)
                    

    @property
    def test101_A(self):
        return self.__test101_A

    @test101_A.setter
    def test101_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_A__test101_A", None)
        self.__test101_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_C"):
                opp_val = getattr(old_value, "test101_C", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_C"):
                opp_val = getattr(value, "test101_C", None)
                if opp_val is None:
                    setattr(value, "test101_C", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test101_C:

    pass
class test101_L1:

    def __init__(self, since: str, test101_L1: "test101_C" = None, test101_L124: "test101_B" = None, test101_L127: "test101_G" = None):
        self.since = since
        self.test101_L1 = test101_L1
        self.test101_L124 = test101_L124
        self.test101_L127 = test101_L127
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def test101_L127(self):
        return self.__test101_L127

    @test101_L127.setter
    def test101_L127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_L1__test101_L127", None)
        self.__test101_L127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_G28"):
                opp_val = getattr(old_value, "test101_G28", None)
                if opp_val == self:
                    setattr(old_value, "test101_G28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_G28"):
                opp_val = getattr(value, "test101_G28", None)
                setattr(value, "test101_G28", self)

    @property
    def test101_L1(self):
        return self.__test101_L1

    @test101_L1.setter
    def test101_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_L1__test101_L1", None)
        self.__test101_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_C4"):
                opp_val = getattr(old_value, "test101_C4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_C4"):
                opp_val = getattr(value, "test101_C4", None)
                if opp_val is None:
                    setattr(value, "test101_C4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test101_L124(self):
        return self.__test101_L124

    @test101_L124.setter
    def test101_L124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test101_L1__test101_L124", None)
        self.__test101_L124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test101_B25"):
                opp_val = getattr(old_value, "test101_B25", None)
                if opp_val == self:
                    setattr(old_value, "test101_B25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test101_B25"):
                opp_val = getattr(value, "test101_B25", None)
                setattr(value, "test101_B25", self)

class test101_D(G):

    pass
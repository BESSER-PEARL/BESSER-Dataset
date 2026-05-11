from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mnoq_M:

    def __init__(self, x: int, M: "mnoq_N" = None, mms: set["mnoq_N"] = None, mnoq_M: "mnoq_O" = None):
        self.x = x
        self.M = M
        self.mms = mms if mms is not None else set()
        self.mnoq_M = mnoq_M
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def mnoq_M(self):
        return self.__mnoq_M

    @mnoq_M.setter
    def mnoq_M(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__mnoq_M", None)
        self.__mnoq_M = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_O"):
                opp_val = getattr(old_value, "mnoq_O", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_O", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_O"):
                opp_val = getattr(value, "mnoq_O", None)
                setattr(value, "mnoq_O", self)

    @property
    def mms(self):
        return self.__mms

    @mms.setter
    def mms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__mms", None)
        self.__mms = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "N5"):
                    opp_val = getattr(item, "N5", None)
                    
                    if opp_val == self:
                        setattr(item, "N5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "N5"):
                    opp_val = getattr(item, "N5", None)
                    
                    setattr(item, "N5", self)
                    

    @property
    def M(self):
        return self.__M

    @M.setter
    def M(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__M", None)
        self.__M = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nns"):
                opp_val = getattr(old_value, "nns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nns"):
                opp_val = getattr(value, "nns", None)
                if opp_val is None:
                    setattr(value, "nns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mnoq_N:

    def __init__(self, x: int, N: "mnoq_Q" = None, nns: set["mnoq_M"] = None, ns: set["mnoq_Q"] = None, mnoq_N: "mnoq_Foo" = None, N5: "mnoq_M" = None):
        self.x = x
        self.N = N
        self.nns = nns if nns is not None else set()
        self.ns = ns if ns is not None else set()
        self.mnoq_N = mnoq_N
        self.N5 = N5
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def N5(self):
        return self.__N5

    @N5.setter
    def N5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__N5", None)
        self.__N5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mms"):
                opp_val = getattr(old_value, "mms", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mms"):
                opp_val = getattr(value, "mms", None)
                if opp_val is None:
                    setattr(value, "mms", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def N(self):
        return self.__N

    @N.setter
    def N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__N", None)
        self.__N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qs"):
                opp_val = getattr(old_value, "qs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qs"):
                opp_val = getattr(value, "qs", None)
                if opp_val is None:
                    setattr(value, "qs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ns(self):
        return self.__ns

    @ns.setter
    def ns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__ns", None)
        self.__ns = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Q"):
                    opp_val = getattr(item, "Q", None)
                    
                    if opp_val == self:
                        setattr(item, "Q", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Q"):
                    opp_val = getattr(item, "Q", None)
                    
                    setattr(item, "Q", self)
                    

    @property
    def nns(self):
        return self.__nns

    @nns.setter
    def nns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__nns", None)
        self.__nns = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "M"):
                    opp_val = getattr(item, "M", None)
                    
                    if opp_val == self:
                        setattr(item, "M", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "M"):
                    opp_val = getattr(item, "M", None)
                    
                    setattr(item, "M", self)
                    

    @property
    def mnoq_N(self):
        return self.__mnoq_N

    @mnoq_N.setter
    def mnoq_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__mnoq_N", None)
        self.__mnoq_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_Foo"):
                opp_val = getattr(old_value, "mnoq_Foo", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_Foo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_Foo"):
                opp_val = getattr(value, "mnoq_Foo", None)
                setattr(value, "mnoq_Foo", self)

class mnoq_Q:

    def __init__(self, x: int, qs: set["mnoq_N"] = None, Q: "mnoq_N" = None):
        self.x = x
        self.qs = qs if qs is not None else set()
        self.Q = Q
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def Q(self):
        return self.__Q

    @Q.setter
    def Q(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_Q__Q", None)
        self.__Q = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ns"):
                opp_val = getattr(old_value, "ns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ns"):
                opp_val = getattr(value, "ns", None)
                if opp_val is None:
                    setattr(value, "ns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qs(self):
        return self.__qs

    @qs.setter
    def qs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_Q__qs", None)
        self.__qs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "N"):
                    opp_val = getattr(item, "N", None)
                    
                    if opp_val == self:
                        setattr(item, "N", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "N"):
                    opp_val = getattr(item, "N", None)
                    
                    setattr(item, "N", self)
                    

class mnoq_O:

    def __init__(self, x: int, mnoq_O: "mnoq_M" = None):
        self.x = x
        self.mnoq_O = mnoq_O
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def mnoq_O(self):
        return self.__mnoq_O

    @mnoq_O.setter
    def mnoq_O(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_O__mnoq_O", None)
        self.__mnoq_O = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_M"):
                opp_val = getattr(old_value, "mnoq_M", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_M", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_M"):
                opp_val = getattr(value, "mnoq_M", None)
                setattr(value, "mnoq_M", self)

class mnoq_Foo:

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FaultyRelations_C:

    def __init__(self, u: int, C: "FaultyRelations_A" = None, C4: "FaultyRelations_B" = None, AC: set["FaultyRelations_A"] = None, BC: set["FaultyRelations_B"] = None):
        self.u = u
        self.C = C
        self.C4 = C4
        self.AC = AC if AC is not None else set()
        self.BC = BC if BC is not None else set()
        
    @property
    def u(self) -> int:
        return self.__u

    @u.setter
    def u(self, u: int):
        self.__u = u

    @property
    def AC(self):
        return self.__AC

    @AC.setter
    def AC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_C__AC", None)
        self.__AC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A6"):
                    opp_val = getattr(item, "A6", None)
                    
                    if opp_val == self:
                        setattr(item, "A6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A6"):
                    opp_val = getattr(item, "A6", None)
                    
                    setattr(item, "A6", self)
                    

    @property
    def C4(self):
        return self.__C4

    @C4.setter
    def C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_C__C4", None)
        self.__C4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CB"):
                opp_val = getattr(old_value, "CB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CB"):
                opp_val = getattr(value, "CB", None)
                if opp_val is None:
                    setattr(value, "CB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_C__C", None)
        self.__C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CA"):
                opp_val = getattr(old_value, "CA", None)
                if opp_val == self:
                    setattr(old_value, "CA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CA"):
                opp_val = getattr(value, "CA", None)
                setattr(value, "CA", self)

    @property
    def BC(self):
        return self.__BC

    @BC.setter
    def BC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_C__BC", None)
        self.__BC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B8"):
                    opp_val = getattr(item, "B8", None)
                    
                    if opp_val == self:
                        setattr(item, "B8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B8"):
                    opp_val = getattr(item, "B8", None)
                    
                    setattr(item, "B8", self)
                    

class FaultyRelations_B:

    def __init__(self, x: int, y: int, B: "FaultyRelations_A" = None, AB: set["FaultyRelations_A"] = None, CB: set["FaultyRelations_C"] = None, B8: "FaultyRelations_C" = None):
        self.x = x
        self.y = y
        self.B = B
        self.AB = AB if AB is not None else set()
        self.CB = CB if CB is not None else set()
        self.B8 = B8
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def AB(self):
        return self.__AB

    @AB.setter
    def AB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_B__AB", None)
        self.__AB = value if value is not None else set()
        
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
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BA"):
                opp_val = getattr(old_value, "BA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BA"):
                opp_val = getattr(value, "BA", None)
                if opp_val is None:
                    setattr(value, "BA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CB(self):
        return self.__CB

    @CB.setter
    def CB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_B__CB", None)
        self.__CB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C4"):
                    opp_val = getattr(item, "C4", None)
                    
                    if opp_val == self:
                        setattr(item, "C4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C4"):
                    opp_val = getattr(item, "C4", None)
                    
                    setattr(item, "C4", self)
                    

    @property
    def B8(self):
        return self.__B8

    @B8.setter
    def B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_B__B8", None)
        self.__B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BC"):
                opp_val = getattr(old_value, "BC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BC"):
                opp_val = getattr(value, "BC", None)
                if opp_val is None:
                    setattr(value, "BC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FaultyRelations_A:

    def __init__(self, v: int, w: bool, BA: set["FaultyRelations_B"] = None, CA: "FaultyRelations_C" = None, A: "FaultyRelations_B" = None, A6: "FaultyRelations_C" = None):
        self.v = v
        self.w = w
        self.BA = BA if BA is not None else set()
        self.CA = CA
        self.A = A
        self.A6 = A6
        
    @property
    def w(self) -> bool:
        return self.__w

    @w.setter
    def w(self, w: bool):
        self.__w = w

    @property
    def v(self) -> int:
        return self.__v

    @v.setter
    def v(self, v: int):
        self.__v = v

    @property
    def BA(self):
        return self.__BA

    @BA.setter
    def BA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_A__BA", None)
        self.__BA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    if opp_val == self:
                        setattr(item, "B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    setattr(item, "B", self)
                    

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_A__A", None)
        self.__A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AB"):
                opp_val = getattr(old_value, "AB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AB"):
                opp_val = getattr(value, "AB", None)
                if opp_val is None:
                    setattr(value, "AB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def A6(self):
        return self.__A6

    @A6.setter
    def A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_A__A6", None)
        self.__A6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AC"):
                opp_val = getattr(old_value, "AC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AC"):
                opp_val = getattr(value, "AC", None)
                if opp_val is None:
                    setattr(value, "AC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CA(self):
        return self.__CA

    @CA.setter
    def CA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyRelations_A__CA", None)
        self.__CA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C"):
                opp_val = getattr(old_value, "C", None)
                if opp_val == self:
                    setattr(old_value, "C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C"):
                opp_val = getattr(value, "C", None)
                setattr(value, "C", self)

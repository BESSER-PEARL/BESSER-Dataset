from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FaultyUMLmodel4_C:

    def __init__(self, u: int, C4: "FaultyUMLmodel4_B" = None, AC: set["FaultyUMLmodel4_A"] = None, BC: set["FaultyUMLmodel4_B"] = None, DC: set["FaultyUMLmodel4_D"] = None, C11: "FaultyUMLmodel4_D" = None, C: "FaultyUMLmodel4_A" = None):
        self.u = u
        self.C4 = C4
        self.AC = AC if AC is not None else set()
        self.BC = BC if BC is not None else set()
        self.DC = DC if DC is not None else set()
        self.C11 = C11
        self.C = C
        
    @property
    def u(self) -> int:
        return self.__u

    @u.setter
    def u(self, u: int):
        self.__u = u

    @property
    def C11(self):
        return self.__C11

    @C11.setter
    def C11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__C11", None)
        self.__C11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CD"):
                opp_val = getattr(old_value, "CD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CD"):
                opp_val = getattr(value, "CD", None)
                if opp_val is None:
                    setattr(value, "CD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def C4(self):
        return self.__C4

    @C4.setter
    def C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__C4", None)
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
    def DC(self):
        return self.__DC

    @DC.setter
    def DC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__DC", None)
        self.__DC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "D"):
                    opp_val = getattr(item, "D", None)
                    
                    if opp_val == self:
                        setattr(item, "D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "D"):
                    opp_val = getattr(item, "D", None)
                    
                    setattr(item, "D", self)
                    

    @property
    def BC(self):
        return self.__BC

    @BC.setter
    def BC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__BC", None)
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
                    

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__C", None)
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
    def AC(self):
        return self.__AC

    @AC.setter
    def AC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_C__AC", None)
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
                    

class FaultyUMLmodel4_B:

    def __init__(self, x: int, y: int, AB: set["FaultyUMLmodel4_A"] = None, CB: set["FaultyUMLmodel4_C"] = None, B8: "FaultyUMLmodel4_C" = None, B: "FaultyUMLmodel4_A" = None):
        self.x = x
        self.y = y
        self.AB = AB if AB is not None else set()
        self.CB = CB if CB is not None else set()
        self.B8 = B8
        self.B = B
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def B8(self):
        return self.__B8

    @B8.setter
    def B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_B__B8", None)
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

    @property
    def AB(self):
        return self.__AB

    @AB.setter
    def AB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_B__AB", None)
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
    def CB(self):
        return self.__CB

    @CB.setter
    def CB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_B__CB", None)
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
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_B__B", None)
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

class FaultyUMLmodel4_D:

    def __init__(self, z: bool, D: "FaultyUMLmodel4_C" = None, CD: set["FaultyUMLmodel4_C"] = None):
        self.z = z
        self.D = D
        self.CD = CD if CD is not None else set()
        
    @property
    def z(self) -> bool:
        return self.__z

    @z.setter
    def z(self, z: bool):
        self.__z = z

    @property
    def D(self):
        return self.__D

    @D.setter
    def D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_D__D", None)
        self.__D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DC"):
                opp_val = getattr(old_value, "DC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DC"):
                opp_val = getattr(value, "DC", None)
                if opp_val is None:
                    setattr(value, "DC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CD(self):
        return self.__CD

    @CD.setter
    def CD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_D__CD", None)
        self.__CD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C11"):
                    opp_val = getattr(item, "C11", None)
                    
                    if opp_val == self:
                        setattr(item, "C11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C11"):
                    opp_val = getattr(item, "C11", None)
                    
                    setattr(item, "C11", self)
                    

class FaultyUMLmodel4_A:

    def __init__(self, v: int, w: bool, A: "FaultyUMLmodel4_B" = None, A6: "FaultyUMLmodel4_C" = None, BA: set["FaultyUMLmodel4_B"] = None, CA: "FaultyUMLmodel4_C" = None):
        self.v = v
        self.w = w
        self.A = A
        self.A6 = A6
        self.BA = BA if BA is not None else set()
        self.CA = CA
        
    @property
    def v(self) -> int:
        return self.__v

    @v.setter
    def v(self, v: int):
        self.__v = v

    @property
    def w(self) -> bool:
        return self.__w

    @w.setter
    def w(self, w: bool):
        self.__w = w

    @property
    def BA(self):
        return self.__BA

    @BA.setter
    def BA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_A__BA", None)
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
        old_value = getattr(self, f"_FaultyUMLmodel4_A__A", None)
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
    def CA(self):
        return self.__CA

    @CA.setter
    def CA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_A__CA", None)
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

    @property
    def A6(self):
        return self.__A6

    @A6.setter
    def A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultyUMLmodel4_A__A6", None)
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

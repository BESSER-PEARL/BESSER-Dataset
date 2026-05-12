from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class exo6_Triangle:

    pass


class exo6_Point:

    def __init__(self, abcisse: C, ordonnee: C, polygone11: set["exo6_Polygone"] = None):
        self.abcisse = abcisse
        self.ordonnee = ordonnee
        self.polygone11 = polygone11 if polygone11 is not None else set()
        
        pass
    @property
    def ordonnee(self):
        return self.__ordonnee
    @ordonnee.setter
    def ordonnee(self, ordonnee: C):
        self.__ordonnee = ordonnee

    @property
    def abcisse(self):
        return self.__abcisse
    @abcisse.setter
    def abcisse(self, abcisse: C):
        self.__abcisse = abcisse

    @property
    def polygone11(self):
        return self.__polygone11
    @polygone11.setter
    def polygone11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo6_Point__polygone11", None)
        self.__polygone11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "point10"):
                    opp_val = getattr(item, "point10", None)
                    
                    if opp_val == self:
                        setattr(item, "point10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "point10"):
                    opp_val = getattr(item, "point10", None)
                    
                    setattr(item, "point10", self)
                    



class exo6_Polygone:

    def __init__(self, sommets: model2_C, point10: "exo6_Point" = None):
        self.sommets = sommets
        self.point10 = point10
        
        pass
    @property
    def sommets(self):
        return self.__sommets
    @sommets.setter
    def sommets(self, sommets: model2_C):
        self.__sommets = sommets

    @property
    def point10(self):
        return self.__point10
    @point10.setter
    def point10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo6_Polygone__point10", None)
        self.__point10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "polygone11"):
                opp_val = getattr(old_value, "polygone11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "polygone11"):
                opp_val = getattr(value, "polygone11", None)
                if opp_val is None:
                    setattr(value, "polygone11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class model2_R:

    pass


class model2_B:

    def __init__(self, attB: int, c4: set["model2_C"] = None, a8: "model2_A" = None):
        self.attB = attB
        self.c4 = c4 if c4 is not None else set()
        self.a8 = a8
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a8(self):
        return self.__a8
    @a8.setter
    def a8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model2_B__a8", None)
        self.__a8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b9"):
                opp_val = getattr(old_value, "b9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b9"):
                opp_val = getattr(value, "b9", None)
                if opp_val is None:
                    setattr(value, "b9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model2_B__c4", None)
        self.__c4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b5"):
                    opp_val = getattr(item, "b5", None)
                    
                    if opp_val == self:
                        setattr(item, "b5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b5"):
                    opp_val = getattr(item, "b5", None)
                    
                    setattr(item, "b5", self)
                    



class model2_Y:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY



class model2_A:

    def __init__(self, attA: str, r6: "model2_R" = None, b9: set["model2_B"] = None):
        self.attA = attA
        self.r6 = r6
        self.b9 = b9 if b9 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b9(self):
        return self.__b9
    @b9.setter
    def b9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model2_A__b9", None)
        self.__b9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a8"):
                    opp_val = getattr(item, "a8", None)
                    
                    if opp_val == self:
                        setattr(item, "a8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a8"):
                    opp_val = getattr(item, "a8", None)
                    
                    setattr(item, "a8", self)
                    

    @property
    def r6(self):
        return self.__r6
    @r6.setter
    def r6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model2_A__r6", None)
        self.__r6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR7"):
                opp_val = getattr(old_value, "aR7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR7"):
                opp_val = getattr(value, "aR7", None)
                if opp_val is None:
                    setattr(value, "aR7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class model2_Z:

    pass


class model2_C:

    def __init__(self, attC1: int, attC2: bool, b5: "model2_B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b5 = b5
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def b5(self):
        return self.__b5
    @b5.setter
    def b5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model2_C__b5", None)
        self.__b5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c4"):
                opp_val = getattr(old_value, "c4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c4"):
                opp_val = getattr(value, "c4", None)
                if opp_val is None:
                    setattr(value, "c4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class model2_C2:

    pass


class model2_C1:

    pass


class C:

    def __init__(self, attC1: int, attC2: bool, b3: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b3 = b3
        
        pass
    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b3", None)
        self.__b3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c2"):
                opp_val = getattr(old_value, "c2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c2"):
                opp_val = getattr(value, "c2", None)
                if opp_val is None:
                    setattr(value, "c2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, attB: int, a1: "A" = None, c2: set["C"] = None):
        self.attB = attB
        self.a1 = a1
        self.c2 = c2 if c2 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c2", None)
        self.__c2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    if opp_val == self:
                        setattr(item, "b3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    setattr(item, "b3", self)
                    

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a1", None)
        self.__a1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b0"):
                opp_val = getattr(old_value, "b0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b0"):
                opp_val = getattr(value, "b0", None)
                if opp_val is None:
                    setattr(value, "b0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A:

    def __init__(self, attA: str, b0: set["B"] = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b0", None)
        self.__b0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    if opp_val == self:
                        setattr(item, "a1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    setattr(item, "a1", self)
                    


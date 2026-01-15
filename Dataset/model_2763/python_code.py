from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simplek_B:

    def __init__(self, name: str, simplek_B: "simplek_Content" = None):
        self.name = name
        self.simplek_B = simplek_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplek_B(self):
        return self.__simplek_B

    @simplek_B.setter
    def simplek_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplek_B__simplek_B", None)
        self.__simplek_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplek_Content4"):
                opp_val = getattr(old_value, "simplek_Content4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplek_Content4"):
                opp_val = getattr(value, "simplek_Content4", None)
                if opp_val is None:
                    setattr(value, "simplek_Content4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplek_A:

    def __init__(self, name: str, simplek_A: "simplek_Content" = None):
        self.name = name
        self.simplek_A = simplek_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplek_A(self):
        return self.__simplek_A

    @simplek_A.setter
    def simplek_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplek_A__simplek_A", None)
        self.__simplek_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplek_Content2"):
                opp_val = getattr(old_value, "simplek_Content2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplek_Content2"):
                opp_val = getattr(value, "simplek_Content2", None)
                if opp_val is None:
                    setattr(value, "simplek_Content2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplek_Content:

    def __init__(self, name: str, simplek_Content: "simplek_Base" = None, simplek_Content2: set["simplek_A"] = None, simplek_Content4: set["simplek_B"] = None):
        self.name = name
        self.simplek_Content = simplek_Content
        self.simplek_Content2 = simplek_Content2 if simplek_Content2 is not None else set()
        self.simplek_Content4 = simplek_Content4 if simplek_Content4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplek_Content4(self):
        return self.__simplek_Content4

    @simplek_Content4.setter
    def simplek_Content4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplek_Content__simplek_Content4", None)
        self.__simplek_Content4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplek_B"):
                    opp_val = getattr(item, "simplek_B", None)
                    
                    if opp_val == self:
                        setattr(item, "simplek_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplek_B"):
                    opp_val = getattr(item, "simplek_B", None)
                    
                    setattr(item, "simplek_B", self)
                    

    @property
    def simplek_Content2(self):
        return self.__simplek_Content2

    @simplek_Content2.setter
    def simplek_Content2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplek_Content__simplek_Content2", None)
        self.__simplek_Content2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplek_A"):
                    opp_val = getattr(item, "simplek_A", None)
                    
                    if opp_val == self:
                        setattr(item, "simplek_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplek_A"):
                    opp_val = getattr(item, "simplek_A", None)
                    
                    setattr(item, "simplek_A", self)
                    

    @property
    def simplek_Content(self):
        return self.__simplek_Content

    @simplek_Content.setter
    def simplek_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplek_Content__simplek_Content", None)
        self.__simplek_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplek_Base"):
                opp_val = getattr(old_value, "simplek_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplek_Base"):
                opp_val = getattr(value, "simplek_Base", None)
                if opp_val is None:
                    setattr(value, "simplek_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplek_Base:

    pass
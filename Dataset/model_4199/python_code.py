from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class a_Greeting:

    def __init__(self, name: str, a_Greeting: "a_PackageDeclaration" = None):
        self.name = name
        self.a_Greeting = a_Greeting
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def a_Greeting(self):
        return self.__a_Greeting

    @a_Greeting.setter
    def a_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_Greeting__a_Greeting", None)
        self.__a_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_PackageDeclaration2"):
                opp_val = getattr(old_value, "a_PackageDeclaration2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_PackageDeclaration2"):
                opp_val = getattr(value, "a_PackageDeclaration2", None)
                if opp_val is None:
                    setattr(value, "a_PackageDeclaration2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class a_PackageDeclaration:

    def __init__(self, name: str, a_PackageDeclaration: "a_Model" = None, a_PackageDeclaration2: set["a_Greeting"] = None):
        self.name = name
        self.a_PackageDeclaration = a_PackageDeclaration
        self.a_PackageDeclaration2 = a_PackageDeclaration2 if a_PackageDeclaration2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def a_PackageDeclaration(self):
        return self.__a_PackageDeclaration

    @a_PackageDeclaration.setter
    def a_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_PackageDeclaration__a_PackageDeclaration", None)
        self.__a_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_Model"):
                opp_val = getattr(old_value, "a_Model", None)
                if opp_val == self:
                    setattr(old_value, "a_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_Model"):
                opp_val = getattr(value, "a_Model", None)
                setattr(value, "a_Model", self)

    @property
    def a_PackageDeclaration2(self):
        return self.__a_PackageDeclaration2

    @a_PackageDeclaration2.setter
    def a_PackageDeclaration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_PackageDeclaration__a_PackageDeclaration2", None)
        self.__a_PackageDeclaration2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a_Greeting"):
                    opp_val = getattr(item, "a_Greeting", None)
                    
                    if opp_val == self:
                        setattr(item, "a_Greeting", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a_Greeting"):
                    opp_val = getattr(item, "a_Greeting", None)
                    
                    setattr(item, "a_Greeting", self)
                    

class a_Model:

    pass
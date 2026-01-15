from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloScoping_FieldReference:

    pass
class helloScoping_Field:

    def __init__(self, name: str, helloScoping_Field: "helloScoping_Greeting" = None, helloScoping_Field10: "helloScoping_FieldReference" = None):
        self.name = name
        self.helloScoping_Field = helloScoping_Field
        self.helloScoping_Field10 = helloScoping_Field10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloScoping_Field10(self):
        return self.__helloScoping_Field10

    @helloScoping_Field10.setter
    def helloScoping_Field10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Field__helloScoping_Field10", None)
        self.__helloScoping_Field10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloScoping_FieldReference9"):
                opp_val = getattr(old_value, "helloScoping_FieldReference9", None)
                if opp_val == self:
                    setattr(old_value, "helloScoping_FieldReference9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloScoping_FieldReference9"):
                opp_val = getattr(value, "helloScoping_FieldReference9", None)
                setattr(value, "helloScoping_FieldReference9", self)

    @property
    def helloScoping_Field(self):
        return self.__helloScoping_Field

    @helloScoping_Field.setter
    def helloScoping_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Field__helloScoping_Field", None)
        self.__helloScoping_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloScoping_Greeting5"):
                opp_val = getattr(old_value, "helloScoping_Greeting5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloScoping_Greeting5"):
                opp_val = getattr(value, "helloScoping_Greeting5", None)
                if opp_val is None:
                    setattr(value, "helloScoping_Greeting5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class helloScoping_Greeting:

    def __init__(self, name: str, helloScoping_Greeting: "helloScoping_Model" = None, helloScoping_Greeting3: "helloScoping_Greeting" = None, helloScoping_Greeting1: "helloScoping_Greeting" = None, helloScoping_Greeting5: set["helloScoping_Field"] = None, helloScoping_Greeting7: set["helloScoping_FieldReference"] = None):
        self.name = name
        self.helloScoping_Greeting = helloScoping_Greeting
        self.helloScoping_Greeting3 = helloScoping_Greeting3
        self.helloScoping_Greeting1 = helloScoping_Greeting1
        self.helloScoping_Greeting5 = helloScoping_Greeting5 if helloScoping_Greeting5 is not None else set()
        self.helloScoping_Greeting7 = helloScoping_Greeting7 if helloScoping_Greeting7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloScoping_Greeting(self):
        return self.__helloScoping_Greeting

    @helloScoping_Greeting.setter
    def helloScoping_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Greeting__helloScoping_Greeting", None)
        self.__helloScoping_Greeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloScoping_Model"):
                opp_val = getattr(old_value, "helloScoping_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloScoping_Model"):
                opp_val = getattr(value, "helloScoping_Model", None)
                if opp_val is None:
                    setattr(value, "helloScoping_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def helloScoping_Greeting7(self):
        return self.__helloScoping_Greeting7

    @helloScoping_Greeting7.setter
    def helloScoping_Greeting7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Greeting__helloScoping_Greeting7", None)
        self.__helloScoping_Greeting7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloScoping_FieldReference"):
                    opp_val = getattr(item, "helloScoping_FieldReference", None)
                    
                    if opp_val == self:
                        setattr(item, "helloScoping_FieldReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloScoping_FieldReference"):
                    opp_val = getattr(item, "helloScoping_FieldReference", None)
                    
                    setattr(item, "helloScoping_FieldReference", self)
                    

    @property
    def helloScoping_Greeting1(self):
        return self.__helloScoping_Greeting1

    @helloScoping_Greeting1.setter
    def helloScoping_Greeting1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Greeting__helloScoping_Greeting1", None)
        self.__helloScoping_Greeting1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloScoping_Greeting3"):
                opp_val = getattr(old_value, "helloScoping_Greeting3", None)
                if opp_val == self:
                    setattr(old_value, "helloScoping_Greeting3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloScoping_Greeting3"):
                opp_val = getattr(value, "helloScoping_Greeting3", None)
                setattr(value, "helloScoping_Greeting3", self)

    @property
    def helloScoping_Greeting5(self):
        return self.__helloScoping_Greeting5

    @helloScoping_Greeting5.setter
    def helloScoping_Greeting5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Greeting__helloScoping_Greeting5", None)
        self.__helloScoping_Greeting5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloScoping_Field"):
                    opp_val = getattr(item, "helloScoping_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "helloScoping_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloScoping_Field"):
                    opp_val = getattr(item, "helloScoping_Field", None)
                    
                    setattr(item, "helloScoping_Field", self)
                    

    @property
    def helloScoping_Greeting3(self):
        return self.__helloScoping_Greeting3

    @helloScoping_Greeting3.setter
    def helloScoping_Greeting3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloScoping_Greeting__helloScoping_Greeting3", None)
        self.__helloScoping_Greeting3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloScoping_Greeting1"):
                opp_val = getattr(old_value, "helloScoping_Greeting1", None)
                if opp_val == self:
                    setattr(old_value, "helloScoping_Greeting1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloScoping_Greeting1"):
                opp_val = getattr(value, "helloScoping_Greeting1", None)
                setattr(value, "helloScoping_Greeting1", self)

class helloScoping_Model:

    pass
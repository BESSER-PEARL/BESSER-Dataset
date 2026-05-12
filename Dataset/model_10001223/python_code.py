from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class JValueJSONPrintVisitor:

    pass


class JValueVisitor_Interface:

    pass


class Contexte:

    pass


class Retraction:

    pass


class Protraction:

    pass


class Wait:

    pass


class State_Interface:

    pass


class JValue_Interface:

    pass


class JArray:

    def __init__(self, value: str, value4: set["JValue_Interface"] = None):
        self.value = value
        self.value4 = value4 if value4 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def value4(self):
        return self.__value4
    @value4.setter
    def value4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JArray__value4", None)
        self.__value4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jArray5"):
                    opp_val = getattr(item, "jArray5", None)
                    
                    if opp_val == self:
                        setattr(item, "jArray5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jArray5"):
                    opp_val = getattr(item, "jArray5", None)
                    
                    setattr(item, "jArray5", self)
                    



class JNull:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value



class JStr:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value



class JNum:

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value



class JBool:

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: bool):
        self.__value = value



class JMember:

    def __init__(self, nom: str, JObject_JMember_11: "JObject" = None, jValue2: "JValue_Interface" = None):
        self.nom = nom
        self.JObject_JMember_11 = JObject_JMember_11
        self.jValue2 = jValue2
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def JObject_JMember_11(self):
        return self.__JObject_JMember_11
    @JObject_JMember_11.setter
    def JObject_JMember_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JMember__JObject_JMember_11", None)
        self.__JObject_JMember_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JObject_JMember_00"):
                opp_val = getattr(old_value, "JObject_JMember_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JObject_JMember_00"):
                opp_val = getattr(value, "JObject_JMember_00", None)
                if opp_val is None:
                    setattr(value, "JObject_JMember_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jValue2(self):
        return self.__jValue2
    @jValue2.setter
    def jValue2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JMember__jValue2", None)
        self.__jValue2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jMember3"):
                opp_val = getattr(old_value, "jMember3", None)
                if opp_val == self:
                    setattr(old_value, "jMember3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jMember3"):
                opp_val = getattr(value, "jMember3", None)
                setattr(value, "jMember3", self)



class JObject:

    pass

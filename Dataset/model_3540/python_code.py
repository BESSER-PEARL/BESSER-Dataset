from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class emapvselistentry_NewEClass3:

    def __init__(self, key: str, value: str, emapvselistentry_NewEClass3: "emapvselistentry_NewEClass1" = None):
        self.key = key
        self.value = value
        self.emapvselistentry_NewEClass3 = emapvselistentry_NewEClass3
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def emapvselistentry_NewEClass3(self):
        return self.__emapvselistentry_NewEClass3

    @emapvselistentry_NewEClass3.setter
    def emapvselistentry_NewEClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapvselistentry_NewEClass3__emapvselistentry_NewEClass3", None)
        self.__emapvselistentry_NewEClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapvselistentry_NewEClass12"):
                opp_val = getattr(old_value, "emapvselistentry_NewEClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapvselistentry_NewEClass12"):
                opp_val = getattr(value, "emapvselistentry_NewEClass12", None)
                if opp_val is None:
                    setattr(value, "emapvselistentry_NewEClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emapvselistentry_NewEClass2:

    def __init__(self, key: str, value: str, emapvselistentry_NewEClass2: "emapvselistentry_NewEClass1" = None):
        self.key = key
        self.value = value
        self.emapvselistentry_NewEClass2 = emapvselistentry_NewEClass2
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emapvselistentry_NewEClass2(self):
        return self.__emapvselistentry_NewEClass2

    @emapvselistentry_NewEClass2.setter
    def emapvselistentry_NewEClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapvselistentry_NewEClass2__emapvselistentry_NewEClass2", None)
        self.__emapvselistentry_NewEClass2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapvselistentry_NewEClass1"):
                opp_val = getattr(old_value, "emapvselistentry_NewEClass1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapvselistentry_NewEClass1"):
                opp_val = getattr(value, "emapvselistentry_NewEClass1", None)
                if opp_val is None:
                    setattr(value, "emapvselistentry_NewEClass1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emapvselistentry_NewEClass1:

    pass
class emapvselistentry_NewEClass5:

    def __init__(self, key: str, value: str, emapvselistentry_NewEClass5: "emapvselistentry_NewEClass1" = None):
        self.key = key
        self.value = value
        self.emapvselistentry_NewEClass5 = emapvselistentry_NewEClass5
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emapvselistentry_NewEClass5(self):
        return self.__emapvselistentry_NewEClass5

    @emapvselistentry_NewEClass5.setter
    def emapvselistentry_NewEClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapvselistentry_NewEClass5__emapvselistentry_NewEClass5", None)
        self.__emapvselistentry_NewEClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapvselistentry_NewEClass16"):
                opp_val = getattr(old_value, "emapvselistentry_NewEClass16", None)
                if opp_val == self:
                    setattr(old_value, "emapvselistentry_NewEClass16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapvselistentry_NewEClass16"):
                opp_val = getattr(value, "emapvselistentry_NewEClass16", None)
                setattr(value, "emapvselistentry_NewEClass16", self)

class emapvselistentry_NewEClass4:

    def __init__(self, key: str, value: str, emapvselistentry_NewEClass4: "emapvselistentry_NewEClass1" = None):
        self.key = key
        self.value = value
        self.emapvselistentry_NewEClass4 = emapvselistentry_NewEClass4
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emapvselistentry_NewEClass4(self):
        return self.__emapvselistentry_NewEClass4

    @emapvselistentry_NewEClass4.setter
    def emapvselistentry_NewEClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emapvselistentry_NewEClass4__emapvselistentry_NewEClass4", None)
        self.__emapvselistentry_NewEClass4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emapvselistentry_NewEClass14"):
                opp_val = getattr(old_value, "emapvselistentry_NewEClass14", None)
                if opp_val == self:
                    setattr(old_value, "emapvselistentry_NewEClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emapvselistentry_NewEClass14"):
                opp_val = getattr(value, "emapvselistentry_NewEClass14", None)
                setattr(value, "emapvselistentry_NewEClass14", self)

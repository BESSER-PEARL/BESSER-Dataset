from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class attributes_A:

    def __init__(self, id: str, d: str, name: str, b: str, c: str, comment: str, attributes_A: "attributes_R" = None):
        self.id = id
        self.d = d
        self.name = name
        self.b = b
        self.c = c
        self.comment = comment
        self.attributes_A = attributes_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def d(self) -> str:
        return self.__d

    @d.setter
    def d(self, d: str):
        self.__d = d

    @property
    def attributes_A(self):
        return self.__attributes_A

    @attributes_A.setter
    def attributes_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attributes_A__attributes_A", None)
        self.__attributes_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes_R"):
                opp_val = getattr(old_value, "attributes_R", None)
                if opp_val == self:
                    setattr(old_value, "attributes_R", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes_R"):
                opp_val = getattr(value, "attributes_R", None)
                setattr(value, "attributes_R", self)

class attributes_EStringToStringMapEntry:

    pass
class attributes_DocumentRoot:

    def __init__(self, mixed: str, comment: str, attributes_DocumentRoot: set["attributes_EStringToStringMapEntry"] = None, attributes_DocumentRoot3: set["attributes_EStringToStringMapEntry"] = None):
        self.mixed = mixed
        self.comment = comment
        self.attributes_DocumentRoot = attributes_DocumentRoot if attributes_DocumentRoot is not None else set()
        self.attributes_DocumentRoot3 = attributes_DocumentRoot3 if attributes_DocumentRoot3 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def attributes_DocumentRoot3(self):
        return self.__attributes_DocumentRoot3

    @attributes_DocumentRoot3.setter
    def attributes_DocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attributes_DocumentRoot__attributes_DocumentRoot3", None)
        self.__attributes_DocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attributes_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "attributes_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "attributes_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attributes_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "attributes_EStringToStringMapEntry4", None)
                    
                    setattr(item, "attributes_EStringToStringMapEntry4", self)
                    

    @property
    def attributes_DocumentRoot(self):
        return self.__attributes_DocumentRoot

    @attributes_DocumentRoot.setter
    def attributes_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attributes_DocumentRoot__attributes_DocumentRoot", None)
        self.__attributes_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attributes_EStringToStringMapEntry"):
                    opp_val = getattr(item, "attributes_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "attributes_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attributes_EStringToStringMapEntry"):
                    opp_val = getattr(item, "attributes_EStringToStringMapEntry", None)
                    
                    setattr(item, "attributes_EStringToStringMapEntry", self)
                    

class attributes_R:

    def __init__(self, name: str, attributes_R: "attributes_A" = None):
        self.name = name
        self.attributes_R = attributes_R
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attributes_R(self):
        return self.__attributes_R

    @attributes_R.setter
    def attributes_R(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attributes_R__attributes_R", None)
        self.__attributes_R = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes_A"):
                opp_val = getattr(old_value, "attributes_A", None)
                if opp_val == self:
                    setattr(old_value, "attributes_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes_A"):
                opp_val = getattr(value, "attributes_A", None)
                setattr(value, "attributes_A", self)

from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Type:

    def __init__(self, name: str, myDsl_Type9: "myDsl_Property" = None, myDsl_Type: "myDsl_Model" = None):
        self.name = name
        self.myDsl_Type9 = myDsl_Type9
        self.myDsl_Type = myDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model2"):
                opp_val = getattr(old_value, "myDsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model2"):
                opp_val = getattr(value, "myDsl_Model2", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Type9(self):
        return self.__myDsl_Type9

    @myDsl_Type9.setter
    def myDsl_Type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type9", None)
        self.__myDsl_Type9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Property8"):
                opp_val = getattr(old_value, "myDsl_Property8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Property8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Property8"):
                opp_val = getattr(value, "myDsl_Property8", None)
                setattr(value, "myDsl_Property8", self)

class myDsl_Import:

    def __init__(self, importURI: str, myDsl_Import: "myDsl_Model" = None):
        self.importURI = importURI
        self.myDsl_Import = myDsl_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def myDsl_Import(self):
        return self.__myDsl_Import

    @myDsl_Import.setter
    def myDsl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Import__myDsl_Import", None)
        self.__myDsl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Property:

    def __init__(self, name: str, many: bool, myDsl_Property: "myDsl_Entity" = None, myDsl_Property8: "myDsl_Type" = None):
        self.name = name
        self.many = many
        self.myDsl_Property = myDsl_Property
        self.myDsl_Property8 = myDsl_Property8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def myDsl_Property(self):
        return self.__myDsl_Property

    @myDsl_Property.setter
    def myDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property", None)
        self.__myDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity6"):
                opp_val = getattr(old_value, "myDsl_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity6"):
                opp_val = getattr(value, "myDsl_Entity6", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Property8(self):
        return self.__myDsl_Property8

    @myDsl_Property8.setter
    def myDsl_Property8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property8", None)
        self.__myDsl_Property8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type9"):
                opp_val = getattr(old_value, "myDsl_Type9", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type9"):
                opp_val = getattr(value, "myDsl_Type9", None)
                setattr(value, "myDsl_Type9", self)

class Type:

    pass
class myDsl_Entity(Type):

    pass
class myDsl_SimpleType(Type):

    pass
class myDsl_Model:

    pass
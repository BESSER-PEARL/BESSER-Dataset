from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Type:

    def __init__(self, name: str, doesReferenceModelClass: bool, isCollection: bool, fullName: str, Data_Type: "Data_Attribute" = None):
        self.name = name
        self.doesReferenceModelClass = doesReferenceModelClass
        self.isCollection = isCollection
        self.fullName = fullName
        self.Data_Type = Data_Type
        
    @property
    def isCollection(self) -> bool:
        return self.__isCollection

    @isCollection.setter
    def isCollection(self, isCollection: bool):
        self.__isCollection = isCollection

    @property
    def doesReferenceModelClass(self) -> bool:
        return self.__doesReferenceModelClass

    @doesReferenceModelClass.setter
    def doesReferenceModelClass(self, doesReferenceModelClass: bool):
        self.__doesReferenceModelClass = doesReferenceModelClass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def Data_Type(self):
        return self.__Data_Type

    @Data_Type.setter
    def Data_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Type__Data_Type", None)
        self.__Data_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Attribute4"):
                opp_val = getattr(old_value, "Data_Attribute4", None)
                if opp_val == self:
                    setattr(old_value, "Data_Attribute4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Attribute4"):
                opp_val = getattr(value, "Data_Attribute4", None)
                setattr(value, "Data_Attribute4", self)

class Data_Attribute:

    def __init__(self, name: str, Data_Attribute: "Data_Class" = None, Data_Attribute4: "Data_Type" = None):
        self.name = name
        self.Data_Attribute = Data_Attribute
        self.Data_Attribute4 = Data_Attribute4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Attribute(self):
        return self.__Data_Attribute

    @Data_Attribute.setter
    def Data_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribute__Data_Attribute", None)
        self.__Data_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Class2"):
                opp_val = getattr(old_value, "Data_Class2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Class2"):
                opp_val = getattr(value, "Data_Class2", None)
                if opp_val is None:
                    setattr(value, "Data_Class2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Data_Attribute4(self):
        return self.__Data_Attribute4

    @Data_Attribute4.setter
    def Data_Attribute4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Attribute__Data_Attribute4", None)
        self.__Data_Attribute4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Type"):
                opp_val = getattr(old_value, "Data_Type", None)
                if opp_val == self:
                    setattr(old_value, "Data_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Type"):
                opp_val = getattr(value, "Data_Type", None)
                setattr(value, "Data_Type", self)

class Data_Class:

    def __init__(self, name: str, Data_Class: "Data_Model" = None, Data_Class2: set["Data_Attribute"] = None):
        self.name = name
        self.Data_Class = Data_Class
        self.Data_Class2 = Data_Class2 if Data_Class2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Class(self):
        return self.__Data_Class

    @Data_Class.setter
    def Data_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class", None)
        self.__Data_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Model"):
                opp_val = getattr(old_value, "Data_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Model"):
                opp_val = getattr(value, "Data_Model", None)
                if opp_val is None:
                    setattr(value, "Data_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Data_Class2(self):
        return self.__Data_Class2

    @Data_Class2.setter
    def Data_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class2", None)
        self.__Data_Class2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Attribute"):
                    opp_val = getattr(item, "Data_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Attribute"):
                    opp_val = getattr(item, "Data_Attribute", None)
                    
                    setattr(item, "Data_Attribute", self)
                    

class Data_Model:

    pass
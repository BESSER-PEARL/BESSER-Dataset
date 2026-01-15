from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Data_Parameter:

    def __init__(self, name: str, type: str, Data_Parameter: "Data_Method" = None):
        self.name = name
        self.type = type
        self.Data_Parameter = Data_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Parameter(self):
        return self.__Data_Parameter

    @Data_Parameter.setter
    def Data_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Parameter__Data_Parameter", None)
        self.__Data_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Method6"):
                opp_val = getattr(old_value, "Data_Method6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Method6"):
                opp_val = getattr(value, "Data_Method6", None)
                if opp_val is None:
                    setattr(value, "Data_Method6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Data_Method:

    def __init__(self, return: str, encapsulation: str, name: str, Data_Method: "Data_Class" = None, Data_Method6: set["Data_Parameter"] = None):
        self.return = return
        self.encapsulation = encapsulation
        self.name = name
        self.Data_Method = Data_Method
        self.Data_Method6 = Data_Method6 if Data_Method6 is not None else set()
        
    @property
    def encapsulation(self) -> str:
        return self.__encapsulation

    @encapsulation.setter
    def encapsulation(self, encapsulation: str):
        self.__encapsulation = encapsulation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def Data_Method(self):
        return self.__Data_Method

    @Data_Method.setter
    def Data_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Method__Data_Method", None)
        self.__Data_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_Class4"):
                opp_val = getattr(old_value, "Data_Class4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_Class4"):
                opp_val = getattr(value, "Data_Class4", None)
                if opp_val is None:
                    setattr(value, "Data_Class4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Data_Method6(self):
        return self.__Data_Method6

    @Data_Method6.setter
    def Data_Method6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Method__Data_Method6", None)
        self.__Data_Method6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Parameter"):
                    opp_val = getattr(item, "Data_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Parameter"):
                    opp_val = getattr(item, "Data_Parameter", None)
                    
                    setattr(item, "Data_Parameter", self)
                    

class Data_Attribute:

    def __init__(self, name: str, type: str, encapsulation: str, Data_Attribute: "Data_Class" = None):
        self.name = name
        self.type = type
        self.encapsulation = encapsulation
        self.Data_Attribute = Data_Attribute
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def encapsulation(self) -> str:
        return self.__encapsulation

    @encapsulation.setter
    def encapsulation(self, encapsulation: str):
        self.__encapsulation = encapsulation

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

class Data_Class:

    def __init__(self, name: str, Data_Class: "Data_Model" = None, Data_Class2: set["Data_Attribute"] = None, Data_Class4: set["Data_Method"] = None):
        self.name = name
        self.Data_Class = Data_Class
        self.Data_Class2 = Data_Class2 if Data_Class2 is not None else set()
        self.Data_Class4 = Data_Class4 if Data_Class4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data_Class4(self):
        return self.__Data_Class4

    @Data_Class4.setter
    def Data_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Class__Data_Class4", None)
        self.__Data_Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data_Method"):
                    opp_val = getattr(item, "Data_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Data_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data_Method"):
                    opp_val = getattr(item, "Data_Method", None)
                    
                    setattr(item, "Data_Method", self)
                    

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

class Data_Model:

    pass
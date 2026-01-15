from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class classdiagram_Attribute:

    def __init__(self, name: str, classdiagram_Attribute5: "classdiagram_Class" = None, classdiagram_Attribute: "classdiagram_ClassDiagram" = None):
        self.name = name
        self.classdiagram_Attribute5 = classdiagram_Attribute5
        self.classdiagram_Attribute = classdiagram_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Attribute5(self):
        return self.__classdiagram_Attribute5

    @classdiagram_Attribute5.setter
    def classdiagram_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute5", None)
        self.__classdiagram_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class4"):
                opp_val = getattr(old_value, "classdiagram_Class4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class4"):
                opp_val = getattr(value, "classdiagram_Class4", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Class4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Attribute(self):
        return self.__classdiagram_Attribute

    @classdiagram_Attribute.setter
    def classdiagram_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute", None)
        self.__classdiagram_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_ClassDiagram2"):
                opp_val = getattr(old_value, "classdiagram_ClassDiagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_ClassDiagram2"):
                opp_val = getattr(value, "classdiagram_ClassDiagram2", None)
                if opp_val is None:
                    setattr(value, "classdiagram_ClassDiagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Class:

    def __init__(self, name: str, classdiagram_Class4: set["classdiagram_Attribute"] = None, classdiagram_Class: "classdiagram_ClassDiagram" = None):
        self.name = name
        self.classdiagram_Class4 = classdiagram_Class4 if classdiagram_Class4 is not None else set()
        self.classdiagram_Class = classdiagram_Class
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Class(self):
        return self.__classdiagram_Class

    @classdiagram_Class.setter
    def classdiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class", None)
        self.__classdiagram_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_ClassDiagram"):
                opp_val = getattr(old_value, "classdiagram_ClassDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_ClassDiagram"):
                opp_val = getattr(value, "classdiagram_ClassDiagram", None)
                if opp_val is None:
                    setattr(value, "classdiagram_ClassDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Class4(self):
        return self.__classdiagram_Class4

    @classdiagram_Class4.setter
    def classdiagram_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class4", None)
        self.__classdiagram_Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Attribute5"):
                    opp_val = getattr(item, "classdiagram_Attribute5", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Attribute5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Attribute5"):
                    opp_val = getattr(item, "classdiagram_Attribute5", None)
                    
                    setattr(item, "classdiagram_Attribute5", self)
                    

class classdiagram_ClassDiagram:

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class class_Attribute:

    def __init__(self, id: str, class_Attribute: "class_Clazz" = None):
        self.id = id
        self.class_Attribute = class_Attribute
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class_Attribute(self):
        return self.__class_Attribute

    @class_Attribute.setter
    def class_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Attribute__class_Attribute", None)
        self.__class_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Clazz4"):
                opp_val = getattr(old_value, "class_Clazz4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Clazz4"):
                opp_val = getattr(value, "class_Clazz4", None)
                if opp_val is None:
                    setattr(value, "class_Clazz4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class class_Association:

    def __init__(self, id: str, class_Association: "class_ClassDiagram" = None, class_Association12: "class_Clazz" = None, class_Association9: "class_Clazz" = None):
        self.id = id
        self.class_Association = class_Association
        self.class_Association12 = class_Association12
        self.class_Association9 = class_Association9
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class_Association12(self):
        return self.__class_Association12

    @class_Association12.setter
    def class_Association12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Association__class_Association12", None)
        self.__class_Association12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Clazz13"):
                opp_val = getattr(old_value, "class_Clazz13", None)
                if opp_val == self:
                    setattr(old_value, "class_Clazz13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Clazz13"):
                opp_val = getattr(value, "class_Clazz13", None)
                setattr(value, "class_Clazz13", self)

    @property
    def class_Association(self):
        return self.__class_Association

    @class_Association.setter
    def class_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Association__class_Association", None)
        self.__class_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_ClassDiagram2"):
                opp_val = getattr(old_value, "class_ClassDiagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_ClassDiagram2"):
                opp_val = getattr(value, "class_ClassDiagram2", None)
                if opp_val is None:
                    setattr(value, "class_ClassDiagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class_Association9(self):
        return self.__class_Association9

    @class_Association9.setter
    def class_Association9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Association__class_Association9", None)
        self.__class_Association9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Clazz10"):
                opp_val = getattr(old_value, "class_Clazz10", None)
                if opp_val == self:
                    setattr(old_value, "class_Clazz10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Clazz10"):
                opp_val = getattr(value, "class_Clazz10", None)
                setattr(value, "class_Clazz10", self)

class class_Clazz:

    def __init__(self, id: str, class_Clazz: "class_ClassDiagram" = None, class_Clazz4: set["class_Attribute"] = None, class_Clazz7: "class_Clazz" = None, class_Clazz5: "class_Clazz" = None, class_Clazz13: "class_Association" = None, class_Clazz10: "class_Association" = None):
        self.id = id
        self.class_Clazz = class_Clazz
        self.class_Clazz4 = class_Clazz4 if class_Clazz4 is not None else set()
        self.class_Clazz7 = class_Clazz7
        self.class_Clazz5 = class_Clazz5
        self.class_Clazz13 = class_Clazz13
        self.class_Clazz10 = class_Clazz10
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class_Clazz(self):
        return self.__class_Clazz

    @class_Clazz.setter
    def class_Clazz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz", None)
        self.__class_Clazz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_ClassDiagram"):
                opp_val = getattr(old_value, "class_ClassDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_ClassDiagram"):
                opp_val = getattr(value, "class_ClassDiagram", None)
                if opp_val is None:
                    setattr(value, "class_ClassDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class_Clazz7(self):
        return self.__class_Clazz7

    @class_Clazz7.setter
    def class_Clazz7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz7", None)
        self.__class_Clazz7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Clazz5"):
                opp_val = getattr(old_value, "class_Clazz5", None)
                if opp_val == self:
                    setattr(old_value, "class_Clazz5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Clazz5"):
                opp_val = getattr(value, "class_Clazz5", None)
                setattr(value, "class_Clazz5", self)

    @property
    def class_Clazz4(self):
        return self.__class_Clazz4

    @class_Clazz4.setter
    def class_Clazz4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz4", None)
        self.__class_Clazz4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_Attribute"):
                    opp_val = getattr(item, "class_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "class_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_Attribute"):
                    opp_val = getattr(item, "class_Attribute", None)
                    
                    setattr(item, "class_Attribute", self)
                    

    @property
    def class_Clazz10(self):
        return self.__class_Clazz10

    @class_Clazz10.setter
    def class_Clazz10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz10", None)
        self.__class_Clazz10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Association9"):
                opp_val = getattr(old_value, "class_Association9", None)
                if opp_val == self:
                    setattr(old_value, "class_Association9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Association9"):
                opp_val = getattr(value, "class_Association9", None)
                setattr(value, "class_Association9", self)

    @property
    def class_Clazz5(self):
        return self.__class_Clazz5

    @class_Clazz5.setter
    def class_Clazz5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz5", None)
        self.__class_Clazz5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Clazz7"):
                opp_val = getattr(old_value, "class_Clazz7", None)
                if opp_val == self:
                    setattr(old_value, "class_Clazz7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Clazz7"):
                opp_val = getattr(value, "class_Clazz7", None)
                setattr(value, "class_Clazz7", self)

    @property
    def class_Clazz13(self):
        return self.__class_Clazz13

    @class_Clazz13.setter
    def class_Clazz13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_Clazz__class_Clazz13", None)
        self.__class_Clazz13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_Association12"):
                opp_val = getattr(old_value, "class_Association12", None)
                if opp_val == self:
                    setattr(old_value, "class_Association12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_Association12"):
                opp_val = getattr(value, "class_Association12", None)
                setattr(value, "class_Association12", self)

class class_ClassDiagram:

    def __init__(self, id: str, class_ClassDiagram: set["class_Clazz"] = None, class_ClassDiagram2: set["class_Association"] = None):
        self.id = id
        self.class_ClassDiagram = class_ClassDiagram if class_ClassDiagram is not None else set()
        self.class_ClassDiagram2 = class_ClassDiagram2 if class_ClassDiagram2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def class_ClassDiagram2(self):
        return self.__class_ClassDiagram2

    @class_ClassDiagram2.setter
    def class_ClassDiagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_ClassDiagram__class_ClassDiagram2", None)
        self.__class_ClassDiagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_Association"):
                    opp_val = getattr(item, "class_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "class_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_Association"):
                    opp_val = getattr(item, "class_Association", None)
                    
                    setattr(item, "class_Association", self)
                    

    @property
    def class_ClassDiagram(self):
        return self.__class_ClassDiagram

    @class_ClassDiagram.setter
    def class_ClassDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_ClassDiagram__class_ClassDiagram", None)
        self.__class_ClassDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_Clazz"):
                    opp_val = getattr(item, "class_Clazz", None)
                    
                    if opp_val == self:
                        setattr(item, "class_Clazz", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_Clazz"):
                    opp_val = getattr(item, "class_Clazz", None)
                    
                    setattr(item, "class_Clazz", self)
                    

from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Property:

    def __init__(self, name: str, myDsl_Property: "myDsl_Entity" = None, myDsl_Property5: "myDsl_Type" = None):
        self.name = name
        self.myDsl_Property = myDsl_Property
        self.myDsl_Property5 = myDsl_Property5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "myDsl_Entity"):
                opp_val = getattr(old_value, "myDsl_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity"):
                opp_val = getattr(value, "myDsl_Entity", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Property5(self):
        return self.__myDsl_Property5

    @myDsl_Property5.setter
    def myDsl_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Property__myDsl_Property5", None)
        self.__myDsl_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type"):
                opp_val = getattr(old_value, "myDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type"):
                opp_val = getattr(value, "myDsl_Type", None)
                setattr(value, "myDsl_Type", self)

class Type:

    pass
class myDsl_Datatype(Type):

    pass
class myDsl_Entity(Type):

    pass
class Element:

    pass
class myDsl_Type(Element):

    def __init__(self, name: str, myDsl_Type: "myDsl_Property" = None):
        self.name = name
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
            if hasattr(old_value, "myDsl_Property5"):
                opp_val = getattr(old_value, "myDsl_Property5", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Property5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Property5"):
                opp_val = getattr(value, "myDsl_Property5", None)
                setattr(value, "myDsl_Property5", self)

class myDsl_Namespace(Element):

    def __init__(self, name: str, myDsl_Namespace: set["myDsl_Element"] = None):
        self.name = name
        self.myDsl_Namespace = myDsl_Namespace if myDsl_Namespace is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Namespace(self):
        return self.__myDsl_Namespace

    @myDsl_Namespace.setter
    def myDsl_Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Namespace__myDsl_Namespace", None)
        self.__myDsl_Namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Element2"):
                    opp_val = getattr(item, "myDsl_Element2", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Element2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Element2"):
                    opp_val = getattr(item, "myDsl_Element2", None)
                    
                    setattr(item, "myDsl_Element2", self)
                    

class myDsl_Import(Element):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class myDsl_Element:

    pass
class myDsl_File:

    pass
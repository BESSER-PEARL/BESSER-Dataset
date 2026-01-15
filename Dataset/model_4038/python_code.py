from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classdiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TypedElement:

    pass
class classdiagram_Operation(TypedElement):

    pass
class classdiagram_Attribute(TypedElement):

    pass
class NamedElement:

    pass
class classdiagram_TypedElement(NamedElement):

    def __init__(self, public: bool, classdiagram_TypedElement: "classdiagram_Class" = None):
        self.public = public
        self.classdiagram_TypedElement = classdiagram_TypedElement
        
    @property
    def public(self) -> bool:
        return self.__public

    @public.setter
    def public(self, public: bool):
        self.__public = public

    @property
    def classdiagram_TypedElement(self):
        return self.__classdiagram_TypedElement

    @classdiagram_TypedElement.setter
    def classdiagram_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_TypedElement__classdiagram_TypedElement", None)
        self.__classdiagram_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class34"):
                opp_val = getattr(old_value, "classdiagram_Class34", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class34"):
                opp_val = getattr(value, "classdiagram_Class34", None)
                setattr(value, "classdiagram_Class34", self)

class classdiagram_Association(NamedElement):

    pass
class classdiagram_Dependency:

    def __init__(self, name: str, classdiagram_Dependency: "classdiagram_ClassDiagram" = None, Dependency: "classdiagram_Class" = None, Dependency10: "classdiagram_Class" = None, dependenciesAsDependee: "classdiagram_Class" = None, dependenciesAsDepender: "classdiagram_Class" = None):
        self.name = name
        self.classdiagram_Dependency = classdiagram_Dependency
        self.Dependency = Dependency
        self.Dependency10 = Dependency10
        self.dependenciesAsDependee = dependenciesAsDependee
        self.dependenciesAsDepender = dependenciesAsDepender
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dependenciesAsDepender(self):
        return self.__dependenciesAsDepender

    @dependenciesAsDepender.setter
    def dependenciesAsDepender(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__dependenciesAsDepender", None)
        self.__dependenciesAsDepender = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class32"):
                opp_val = getattr(old_value, "Class32", None)
                if opp_val == self:
                    setattr(old_value, "Class32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class32"):
                opp_val = getattr(value, "Class32", None)
                setattr(value, "Class32", self)

    @property
    def Dependency10(self):
        return self.__Dependency10

    @Dependency10.setter
    def Dependency10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__Dependency10", None)
        self.__Dependency10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "depender"):
                opp_val = getattr(old_value, "depender", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "depender"):
                opp_val = getattr(value, "depender", None)
                if opp_val is None:
                    setattr(value, "depender", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependenciesAsDependee(self):
        return self.__dependenciesAsDependee

    @dependenciesAsDependee.setter
    def dependenciesAsDependee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__dependenciesAsDependee", None)
        self.__dependenciesAsDependee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class30"):
                opp_val = getattr(old_value, "Class30", None)
                if opp_val == self:
                    setattr(old_value, "Class30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class30"):
                opp_val = getattr(value, "Class30", None)
                setattr(value, "Class30", self)

    @property
    def classdiagram_Dependency(self):
        return self.__classdiagram_Dependency

    @classdiagram_Dependency.setter
    def classdiagram_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__classdiagram_Dependency", None)
        self.__classdiagram_Dependency = value
        
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

    @property
    def Dependency(self):
        return self.__Dependency

    @Dependency.setter
    def Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__Dependency", None)
        self.__Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependee"):
                opp_val = getattr(old_value, "dependee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependee"):
                opp_val = getattr(value, "dependee", None)
                if opp_val is None:
                    setattr(value, "dependee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Class(NamedElement):

    pass
class classdiagram_ClassDiagram:

    pass
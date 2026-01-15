from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class classdiagram_TypedElement(NamedElement):

    def __init__(self, public: bool, classdiagram_TypedElement: "classdiagram_Typeable" = None):
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
            if hasattr(old_value, "classdiagram_Typeable42"):
                opp_val = getattr(old_value, "classdiagram_Typeable42", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Typeable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Typeable42"):
                opp_val = getattr(value, "classdiagram_Typeable42", None)
                setattr(value, "classdiagram_Typeable42", self)

class classdiagram_Typeable(NamedElement):

    pass
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
class Typeable:

    pass
class classdiagram_Composition(NamedElement):

    def __init__(self, multiplicity: str, classdiagram_Composition: "classdiagram_ClassDiagram" = None, Composition: "classdiagram_Class" = None, Composition31: "classdiagram_Class" = None, compositionsAsConstituent: "classdiagram_Class" = None, compositionsAsComposite: "classdiagram_Class" = None):
        self.multiplicity = multiplicity
        self.classdiagram_Composition = classdiagram_Composition
        self.Composition = Composition
        self.Composition31 = Composition31
        self.compositionsAsConstituent = compositionsAsConstituent
        self.compositionsAsComposite = compositionsAsComposite
        
    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def compositionsAsConstituent(self):
        return self.__compositionsAsConstituent

    @compositionsAsConstituent.setter
    def compositionsAsConstituent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Composition__compositionsAsConstituent", None)
        self.__compositionsAsConstituent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class48"):
                opp_val = getattr(old_value, "Class48", None)
                if opp_val == self:
                    setattr(old_value, "Class48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class48"):
                opp_val = getattr(value, "Class48", None)
                setattr(value, "Class48", self)

    @property
    def Composition(self):
        return self.__Composition

    @Composition.setter
    def Composition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Composition__Composition", None)
        self.__Composition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constituent"):
                opp_val = getattr(old_value, "constituent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constituent"):
                opp_val = getattr(value, "constituent", None)
                if opp_val is None:
                    setattr(value, "constituent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compositionsAsComposite(self):
        return self.__compositionsAsComposite

    @compositionsAsComposite.setter
    def compositionsAsComposite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Composition__compositionsAsComposite", None)
        self.__compositionsAsComposite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class50"):
                opp_val = getattr(old_value, "Class50", None)
                if opp_val == self:
                    setattr(old_value, "Class50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class50"):
                opp_val = getattr(value, "Class50", None)
                setattr(value, "Class50", self)

    @property
    def classdiagram_Composition(self):
        return self.__classdiagram_Composition

    @classdiagram_Composition.setter
    def classdiagram_Composition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Composition__classdiagram_Composition", None)
        self.__classdiagram_Composition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_ClassDiagram8"):
                opp_val = getattr(old_value, "classdiagram_ClassDiagram8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_ClassDiagram8"):
                opp_val = getattr(value, "classdiagram_ClassDiagram8", None)
                if opp_val is None:
                    setattr(value, "classdiagram_ClassDiagram8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Composition31(self):
        return self.__Composition31

    @Composition31.setter
    def Composition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Composition__Composition31", None)
        self.__Composition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composite"):
                opp_val = getattr(old_value, "composite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composite"):
                opp_val = getattr(value, "composite", None)
                if opp_val is None:
                    setattr(value, "composite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_DataType(Typeable):

    pass
class classdiagram_Association(NamedElement):

    def __init__(self, multiplicity: str, classdiagram_Association: "classdiagram_ClassDiagram" = None, Association: "classdiagram_Class" = None, Association28: "classdiagram_Class" = None, associationsAsSource: "classdiagram_Class" = None, associationsAsTarget: "classdiagram_Class" = None):
        self.multiplicity = multiplicity
        self.classdiagram_Association = classdiagram_Association
        self.Association = Association
        self.Association28 = Association28
        self.associationsAsSource = associationsAsSource
        self.associationsAsTarget = associationsAsTarget
        
    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def associationsAsSource(self):
        return self.__associationsAsSource

    @associationsAsSource.setter
    def associationsAsSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__associationsAsSource", None)
        self.__associationsAsSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class44"):
                opp_val = getattr(old_value, "Class44", None)
                if opp_val == self:
                    setattr(old_value, "Class44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class44"):
                opp_val = getattr(value, "Class44", None)
                setattr(value, "Class44", self)

    @property
    def classdiagram_Association(self):
        return self.__classdiagram_Association

    @classdiagram_Association.setter
    def classdiagram_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association", None)
        self.__classdiagram_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_ClassDiagram4"):
                opp_val = getattr(old_value, "classdiagram_ClassDiagram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_ClassDiagram4"):
                opp_val = getattr(value, "classdiagram_ClassDiagram4", None)
                if opp_val is None:
                    setattr(value, "classdiagram_ClassDiagram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def associationsAsTarget(self):
        return self.__associationsAsTarget

    @associationsAsTarget.setter
    def associationsAsTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__associationsAsTarget", None)
        self.__associationsAsTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class46"):
                opp_val = getattr(old_value, "Class46", None)
                if opp_val == self:
                    setattr(old_value, "Class46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class46"):
                opp_val = getattr(value, "Class46", None)
                setattr(value, "Class46", self)

    @property
    def Association28(self):
        return self.__Association28

    @Association28.setter
    def Association28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__Association28", None)
        self.__Association28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classdiagram_Dependency:

    def __init__(self, name: str, classdiagram_Dependency: "classdiagram_ClassDiagram" = None, Dependency: "classdiagram_Class" = None, Dependency14: "classdiagram_Class" = None, dependenciesAsDependee: "classdiagram_Class" = None, dependenciesAsDepender: "classdiagram_Class" = None):
        self.name = name
        self.classdiagram_Dependency = classdiagram_Dependency
        self.Dependency = Dependency
        self.Dependency14 = Dependency14
        self.dependenciesAsDependee = dependenciesAsDependee
        self.dependenciesAsDepender = dependenciesAsDepender
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Class38"):
                opp_val = getattr(old_value, "Class38", None)
                if opp_val == self:
                    setattr(old_value, "Class38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class38"):
                opp_val = getattr(value, "Class38", None)
                setattr(value, "Class38", self)

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

    @property
    def Dependency14(self):
        return self.__Dependency14

    @Dependency14.setter
    def Dependency14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__Dependency14", None)
        self.__Dependency14 = value
        
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
    def dependenciesAsDepender(self):
        return self.__dependenciesAsDepender

    @dependenciesAsDepender.setter
    def dependenciesAsDepender(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Dependency__dependenciesAsDepender", None)
        self.__dependenciesAsDepender = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class40"):
                opp_val = getattr(old_value, "Class40", None)
                if opp_val == self:
                    setattr(old_value, "Class40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class40"):
                opp_val = getattr(value, "Class40", None)
                setattr(value, "Class40", self)

class classdiagram_Class(Typeable):

    pass
class classdiagram_ClassDiagram:

    pass
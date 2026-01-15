from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Classifier:

    pass
class CLASS_Class(Classifier):

    def __init__(self, isAbstract: bool, CLASS_Class: "CLASS_Class" = None, CLASS_Class1: "CLASS_Class" = None, owner: set["CLASS_Attribute"] = None, Class: "CLASS_Attribute" = None):
        self.isAbstract = isAbstract
        self.CLASS_Class = CLASS_Class
        self.CLASS_Class1 = CLASS_Class1
        self.owner = owner if owner is not None else set()
        self.Class = Class
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def CLASS_Class1(self):
        return self.__CLASS_Class1

    @CLASS_Class1.setter
    def CLASS_Class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Class__CLASS_Class1", None)
        self.__CLASS_Class1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CLASS_Class"):
                opp_val = getattr(old_value, "CLASS_Class", None)
                if opp_val == self:
                    setattr(old_value, "CLASS_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CLASS_Class"):
                opp_val = getattr(value, "CLASS_Class", None)
                setattr(value, "CLASS_Class", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def CLASS_Class(self):
        return self.__CLASS_Class

    @CLASS_Class.setter
    def CLASS_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Class__CLASS_Class", None)
        self.__CLASS_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CLASS_Class1"):
                opp_val = getattr(old_value, "CLASS_Class1", None)
                if opp_val == self:
                    setattr(old_value, "CLASS_Class1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CLASS_Class1"):
                opp_val = getattr(value, "CLASS_Class1", None)
                setattr(value, "CLASS_Class1", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Class__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

class CLASS_DataType(Classifier):

    pass
class NamedElement:

    pass
class CLASS_Attribute(NamedElement):

    def __init__(self, multiValued: bool, Attribute: "CLASS_Class" = None, CLASS_Attribute: "CLASS_Classifier" = None, attributes: "CLASS_Class" = None):
        self.multiValued = multiValued
        self.Attribute = Attribute
        self.CLASS_Attribute = CLASS_Attribute
        self.attributes = attributes
        
    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def CLASS_Attribute(self):
        return self.__CLASS_Attribute

    @CLASS_Attribute.setter
    def CLASS_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Attribute__CLASS_Attribute", None)
        self.__CLASS_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CLASS_Classifier"):
                opp_val = getattr(old_value, "CLASS_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "CLASS_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CLASS_Classifier"):
                opp_val = getattr(value, "CLASS_Classifier", None)
                setattr(value, "CLASS_Classifier", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CLASS_Classifier(NamedElement):

    pass
class CLASS_System:

    def __init__(self, name: str, System: "CLASS_NamedElement" = None, system: set["CLASS_NamedElement"] = None):
        self.name = name
        self.System = System
        self.system = system if system is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_System__system", None)
        self.__system = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    setattr(item, "NamedElement", self)
                    

    @property
    def System(self):
        return self.__System

    @System.setter
    def System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_System__System", None)
        self.__System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

class CLASS_NamedElement:

    def __init__(self, name: str, elements: "CLASS_System" = None, NamedElement: "CLASS_System" = None):
        self.name = name
        self.elements = elements
        self.NamedElement = NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NamedElement(self):
        return self.__NamedElement

    @NamedElement.setter
    def NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_NamedElement__NamedElement", None)
        self.__NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system"):
                opp_val = getattr(old_value, "system", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system"):
                opp_val = getattr(value, "system", None)
                if opp_val is None:
                    setattr(value, "system", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CLASS_NamedElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

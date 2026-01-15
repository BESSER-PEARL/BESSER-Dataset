from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class KIND(Enum):
    OTHER = "OTHER"
    PERSISTENT = "PERSISTENT"


############################################
# Definition of Classes
############################################

class umlMM__Package:

    def __init__(self, name: str, namespace: set["umlMM__Classifier"] = None, namespace2: set["umlMM__Association"] = None, containsPackage: "umlMM__dummy" = None, Package: "umlMM__Classifier" = None, Package22: "umlMM__Association" = None, Package29: "umlMM__dummy" = None):
        self.name = name
        self.namespace = namespace if namespace is not None else set()
        self.namespace2 = namespace2 if namespace2 is not None else set()
        self.containsPackage = containsPackage
        self.Package = Package
        self.Package22 = Package22
        self.Package29 = Package29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__namespace", None)
        self.__namespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

    @property
    def namespace2(self):
        return self.__namespace2

    @namespace2.setter
    def namespace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__namespace2", None)
        self.__namespace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    if opp_val == self:
                        setattr(item, "Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    setattr(item, "Association", self)
                    

    @property
    def Package29(self):
        return self.__Package29

    @Package29.setter
    def Package29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__Package29", None)
        self.__Package29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy28"):
                opp_val = getattr(old_value, "dummy28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy28"):
                opp_val = getattr(value, "dummy28", None)
                if opp_val is None:
                    setattr(value, "dummy28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containsPackage(self):
        return self.__containsPackage

    @containsPackage.setter
    def containsPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__containsPackage", None)
        self.__containsPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dummy"):
                opp_val = getattr(old_value, "dummy", None)
                if opp_val == self:
                    setattr(old_value, "dummy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dummy"):
                opp_val = getattr(value, "dummy", None)
                setattr(value, "dummy", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classifier"):
                opp_val = getattr(old_value, "classifier", None)
                if opp_val == self:
                    setattr(old_value, "classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classifier"):
                opp_val = getattr(value, "classifier", None)
                setattr(value, "classifier", self)

    @property
    def Package22(self):
        return self.__Package22

    @Package22.setter
    def Package22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Package__Package22", None)
        self.__Package22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if opp_val == self:
                    setattr(old_value, "association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                setattr(value, "association", self)

class umlMM__Attribute:

    def __init__(self, name: str, Attribute: "umlMM__Class" = None, attribute: "umlMM__Class" = None, typeOf: "umlMM__Classifier" = None, Attribute19: "umlMM__Classifier" = None):
        self.name = name
        self.Attribute = Attribute
        self.attribute = attribute
        self.typeOf = typeOf
        self.Attribute19 = Attribute19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeOf(self):
        return self.__typeOf

    @typeOf.setter
    def typeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Attribute__typeOf", None)
        self.__typeOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier17"):
                opp_val = getattr(old_value, "Classifier17", None)
                if opp_val == self:
                    setattr(old_value, "Classifier17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier17"):
                opp_val = getattr(value, "Classifier17", None)
                setattr(value, "Classifier17", self)

    @property
    def Attribute19(self):
        return self.__Attribute19

    @Attribute19.setter
    def Attribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Attribute__Attribute19", None)
        self.__Attribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Attribute__Attribute", None)
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

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class15"):
                opp_val = getattr(old_value, "Class15", None)
                if opp_val == self:
                    setattr(old_value, "Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class15"):
                opp_val = getattr(value, "Class15", None)
                setattr(value, "Class15", self)

class Classifier:

    pass
class umlMM__PrimitiveDataType(Classifier):

    pass
class umlMM__Class(Classifier):

    def __init__(self, kind: str, owner: set["umlMM__Attribute"] = None, Class9: "umlMM__Class" = None, general: set["umlMM__Class"] = None, source: set["umlMM__Association"] = None, destination: set["umlMM__Association"] = None, Class15: "umlMM__Attribute" = None, Class: "umlMM__Class" = None, subclass: "umlMM__Class" = None, Class24: "umlMM__Association" = None, Class26: "umlMM__Association" = None):
        self.kind = kind
        self.owner = owner if owner is not None else set()
        self.Class9 = Class9
        self.general = general if general is not None else set()
        self.source = source if source is not None else set()
        self.destination = destination if destination is not None else set()
        self.Class15 = Class15
        self.Class = Class
        self.subclass = subclass
        self.Class24 = Class24
        self.Class26 = Class26
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association11"):
                    opp_val = getattr(item, "Association11", None)
                    
                    if opp_val == self:
                        setattr(item, "Association11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association11"):
                    opp_val = getattr(item, "Association11", None)
                    
                    setattr(item, "Association11", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subclass"):
                opp_val = getattr(old_value, "subclass", None)
                if opp_val == self:
                    setattr(old_value, "subclass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subclass"):
                opp_val = getattr(value, "subclass", None)
                setattr(value, "subclass", self)

    @property
    def subclass(self):
        return self.__subclass

    @subclass.setter
    def subclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__subclass", None)
        self.__subclass = value
        
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
    def general(self):
        return self.__general

    @general.setter
    def general(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__general", None)
        self.__general = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class9"):
                    opp_val = getattr(item, "Class9", None)
                    
                    if opp_val == self:
                        setattr(item, "Class9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class9"):
                    opp_val = getattr(item, "Class9", None)
                    
                    setattr(item, "Class9", self)
                    

    @property
    def Class24(self):
        return self.__Class24

    @Class24.setter
    def Class24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__Class24", None)
        self.__Class24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceOf"):
                opp_val = getattr(old_value, "sourceOf", None)
                if opp_val == self:
                    setattr(old_value, "sourceOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceOf"):
                opp_val = getattr(value, "sourceOf", None)
                setattr(value, "sourceOf", self)

    @property
    def Class15(self):
        return self.__Class15

    @Class15.setter
    def Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__Class15", None)
        self.__Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

    @property
    def Class26(self):
        return self.__Class26

    @Class26.setter
    def Class26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__Class26", None)
        self.__Class26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destinationOf"):
                opp_val = getattr(old_value, "destinationOf", None)
                if opp_val == self:
                    setattr(old_value, "destinationOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destinationOf"):
                opp_val = getattr(value, "destinationOf", None)
                setattr(value, "destinationOf", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__owner", None)
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
                    

    @property
    def Class9(self):
        return self.__Class9

    @Class9.setter
    def Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__Class9", None)
        self.__Class9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "general"):
                opp_val = getattr(old_value, "general", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "general"):
                opp_val = getattr(value, "general", None)
                if opp_val is None:
                    setattr(value, "general", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Class__destination", None)
        self.__destination = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association13"):
                    opp_val = getattr(item, "Association13", None)
                    
                    if opp_val == self:
                        setattr(item, "Association13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association13"):
                    opp_val = getattr(item, "Association13", None)
                    
                    setattr(item, "Association13", self)
                    

class umlMM__dummy:

    pass
class umlMM__Association:

    def __init__(self, name: str, Association: "umlMM__Package" = None, Association11: "umlMM__Class" = None, Association13: "umlMM__Class" = None, association: "umlMM__Package" = None, sourceOf: "umlMM__Class" = None, destinationOf: "umlMM__Class" = None):
        self.name = name
        self.Association = Association
        self.Association11 = Association11
        self.Association13 = Association13
        self.association = association
        self.sourceOf = sourceOf
        self.destinationOf = destinationOf
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Association13(self):
        return self.__Association13

    @Association13.setter
    def Association13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__Association13", None)
        self.__Association13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destination"):
                opp_val = getattr(old_value, "destination", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destination"):
                opp_val = getattr(value, "destination", None)
                if opp_val is None:
                    setattr(value, "destination", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Association11(self):
        return self.__Association11

    @Association11.setter
    def Association11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__Association11", None)
        self.__Association11 = value
        
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
    def sourceOf(self):
        return self.__sourceOf

    @sourceOf.setter
    def sourceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__sourceOf", None)
        self.__sourceOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class24"):
                opp_val = getattr(old_value, "Class24", None)
                if opp_val == self:
                    setattr(old_value, "Class24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class24"):
                opp_val = getattr(value, "Class24", None)
                setattr(value, "Class24", self)

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__association", None)
        self.__association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package22"):
                opp_val = getattr(old_value, "Package22", None)
                if opp_val == self:
                    setattr(old_value, "Package22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package22"):
                opp_val = getattr(value, "Package22", None)
                setattr(value, "Package22", self)

    @property
    def destinationOf(self):
        return self.__destinationOf

    @destinationOf.setter
    def destinationOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__destinationOf", None)
        self.__destinationOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class26"):
                opp_val = getattr(old_value, "Class26", None)
                if opp_val == self:
                    setattr(old_value, "Class26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class26"):
                opp_val = getattr(value, "Class26", None)
                setattr(value, "Class26", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace2"):
                opp_val = getattr(old_value, "namespace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace2"):
                opp_val = getattr(value, "namespace2", None)
                if opp_val is None:
                    setattr(value, "namespace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umlMM__Classifier(ABC):

    def __init__(self, name: str, Classifier: "umlMM__Package" = None, Classifier17: "umlMM__Attribute" = None, classifier: "umlMM__Package" = None, type: set["umlMM__Attribute"] = None):
        self.name = name
        self.Classifier = Classifier
        self.Classifier17 = Classifier17
        self.classifier = classifier
        self.type = type if type is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                if opp_val is None:
                    setattr(value, "namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classifier(self):
        return self.__classifier

    @classifier.setter
    def classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Classifier__classifier", None)
        self.__classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    @property
    def Classifier17(self):
        return self.__Classifier17

    @Classifier17.setter
    def Classifier17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Classifier__Classifier17", None)
        self.__Classifier17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeOf"):
                opp_val = getattr(old_value, "typeOf", None)
                if opp_val == self:
                    setattr(old_value, "typeOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeOf"):
                opp_val = getattr(value, "typeOf", None)
                setattr(value, "typeOf", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM__Classifier__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute19"):
                    opp_val = getattr(item, "Attribute19", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute19"):
                    opp_val = getattr(item, "Attribute19", None)
                    
                    setattr(item, "Attribute19", self)
                    

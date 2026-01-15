from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class umlMM_dummy:

    pass
class umlMM_Attribute:

    def __init__(self, name: str, attribute: "umlMM_Class" = None, typeOf: "umlMM_Classifier" = None, Attribute: "umlMM_Class" = None, Attribute18: "umlMM_Classifier" = None):
        self.name = name
        self.attribute = attribute
        self.typeOf = typeOf
        self.Attribute = Attribute
        self.Attribute18 = Attribute18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Attribute__Attribute", None)
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
        old_value = getattr(self, f"_umlMM_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class14"):
                opp_val = getattr(old_value, "Class14", None)
                if opp_val == self:
                    setattr(old_value, "Class14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class14"):
                opp_val = getattr(value, "Class14", None)
                setattr(value, "Class14", self)

    @property
    def typeOf(self):
        return self.__typeOf

    @typeOf.setter
    def typeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Attribute__typeOf", None)
        self.__typeOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier16"):
                opp_val = getattr(old_value, "Classifier16", None)
                if opp_val == self:
                    setattr(old_value, "Classifier16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier16"):
                opp_val = getattr(value, "Classifier16", None)
                setattr(value, "Classifier16", self)

    @property
    def Attribute18(self):
        return self.__Attribute18

    @Attribute18.setter
    def Attribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Attribute__Attribute18", None)
        self.__Attribute18 = value
        
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

class Classifier:

    pass
class umlMM_PrimitiveDataType(Classifier):

    pass
class umlMM_Class(Classifier):

    def __init__(self, kind: str, source: set["umlMM_Association"] = None, destination: set["umlMM_Association"] = None, Class14: "umlMM_Attribute" = None, owner: set["umlMM_Attribute"] = None, Class: "umlMM_Class" = None, subclass: "umlMM_Class" = None, Class8: "umlMM_Class" = None, general: set["umlMM_Class"] = None, Class23: "umlMM_Association" = None, Class25: "umlMM_Association" = None):
        self.kind = kind
        self.source = source if source is not None else set()
        self.destination = destination if destination is not None else set()
        self.Class14 = Class14
        self.owner = owner if owner is not None else set()
        self.Class = Class
        self.subclass = subclass
        self.Class8 = Class8
        self.general = general if general is not None else set()
        self.Class23 = Class23
        self.Class25 = Class25
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Class8(self):
        return self.__Class8

    @Class8.setter
    def Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class8", None)
        self.__Class8 = value
        
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
    def Class23(self):
        return self.__Class23

    @Class23.setter
    def Class23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class23", None)
        self.__Class23 = value
        
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__owner", None)
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
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class", None)
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
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__destination", None)
        self.__destination = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association12"):
                    opp_val = getattr(item, "Association12", None)
                    
                    if opp_val == self:
                        setattr(item, "Association12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association12"):
                    opp_val = getattr(item, "Association12", None)
                    
                    setattr(item, "Association12", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association10"):
                    opp_val = getattr(item, "Association10", None)
                    
                    if opp_val == self:
                        setattr(item, "Association10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association10"):
                    opp_val = getattr(item, "Association10", None)
                    
                    setattr(item, "Association10", self)
                    

    @property
    def general(self):
        return self.__general

    @general.setter
    def general(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__general", None)
        self.__general = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class8"):
                    opp_val = getattr(item, "Class8", None)
                    
                    if opp_val == self:
                        setattr(item, "Class8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class8"):
                    opp_val = getattr(item, "Class8", None)
                    
                    setattr(item, "Class8", self)
                    

    @property
    def Class14(self):
        return self.__Class14

    @Class14.setter
    def Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class14", None)
        self.__Class14 = value
        
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
    def subclass(self):
        return self.__subclass

    @subclass.setter
    def subclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__subclass", None)
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
    def Class25(self):
        return self.__Class25

    @Class25.setter
    def Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class25", None)
        self.__Class25 = value
        
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

class umlMM_Association:

    def __init__(self, name: str, Association: "umlMM_Package" = None, Association10: "umlMM_Class" = None, Association12: "umlMM_Class" = None, association: "umlMM_Package" = None, sourceOf: "umlMM_Class" = None, destinationOf: "umlMM_Class" = None):
        self.name = name
        self.Association = Association
        self.Association10 = Association10
        self.Association12 = Association12
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
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__association", None)
        self.__association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package21"):
                opp_val = getattr(old_value, "Package21", None)
                if opp_val == self:
                    setattr(old_value, "Package21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package21"):
                opp_val = getattr(value, "Package21", None)
                setattr(value, "Package21", self)

    @property
    def Association10(self):
        return self.__Association10

    @Association10.setter
    def Association10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__Association10", None)
        self.__Association10 = value
        
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
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__Association", None)
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

    @property
    def sourceOf(self):
        return self.__sourceOf

    @sourceOf.setter
    def sourceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__sourceOf", None)
        self.__sourceOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class23"):
                opp_val = getattr(old_value, "Class23", None)
                if opp_val == self:
                    setattr(old_value, "Class23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class23"):
                opp_val = getattr(value, "Class23", None)
                setattr(value, "Class23", self)

    @property
    def destinationOf(self):
        return self.__destinationOf

    @destinationOf.setter
    def destinationOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__destinationOf", None)
        self.__destinationOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class25"):
                opp_val = getattr(old_value, "Class25", None)
                if opp_val == self:
                    setattr(old_value, "Class25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class25"):
                opp_val = getattr(value, "Class25", None)
                setattr(value, "Class25", self)

    @property
    def Association12(self):
        return self.__Association12

    @Association12.setter
    def Association12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Association__Association12", None)
        self.__Association12 = value
        
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

class umlMM_Classifier(ABC):

    def __init__(self, name: str, Classifier: "umlMM_Package" = None, Classifier16: "umlMM_Attribute" = None, type: set["umlMM_Attribute"] = None, classifier: "umlMM_Package" = None):
        self.name = name
        self.Classifier = Classifier
        self.Classifier16 = Classifier16
        self.type = type if type is not None else set()
        self.classifier = classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classifier(self):
        return self.__classifier

    @classifier.setter
    def classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Classifier__classifier", None)
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
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Classifier__Classifier", None)
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
    def Classifier16(self):
        return self.__Classifier16

    @Classifier16.setter
    def Classifier16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Classifier__Classifier16", None)
        self.__Classifier16 = value
        
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
        old_value = getattr(self, f"_umlMM_Classifier__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute18"):
                    opp_val = getattr(item, "Attribute18", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute18"):
                    opp_val = getattr(item, "Attribute18", None)
                    
                    setattr(item, "Attribute18", self)
                    

class umlMM_Package:

    def __init__(self, name: str, namespace: set["umlMM_Classifier"] = None, namespace2: set["umlMM_Association"] = None, umlMM_Package: "umlMM_dummy" = None, Package: "umlMM_Classifier" = None, Package21: "umlMM_Association" = None):
        self.name = name
        self.namespace = namespace if namespace is not None else set()
        self.namespace2 = namespace2 if namespace2 is not None else set()
        self.umlMM_Package = umlMM_Package
        self.Package = Package
        self.Package21 = Package21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Package21(self):
        return self.__Package21

    @Package21.setter
    def Package21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__Package21", None)
        self.__Package21 = value
        
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

    @property
    def namespace2(self):
        return self.__namespace2

    @namespace2.setter
    def namespace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__namespace2", None)
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
    def umlMM_Package(self):
        return self.__umlMM_Package

    @umlMM_Package.setter
    def umlMM_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__umlMM_Package", None)
        self.__umlMM_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlMM_dummy"):
                opp_val = getattr(old_value, "umlMM_dummy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlMM_dummy"):
                opp_val = getattr(value, "umlMM_dummy", None)
                if opp_val is None:
                    setattr(value, "umlMM_dummy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__Package", None)
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
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__namespace", None)
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
                    

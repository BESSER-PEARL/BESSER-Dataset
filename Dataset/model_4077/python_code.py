from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class umlMM_Attribute:

    def __init__(self, name: str, typeOf: "umlMM_Classifier" = None, attribute: "umlMM_Class" = None, Attribute17: "umlMM_Classifier" = None, Attribute: "umlMM_Class" = None):
        self.name = name
        self.typeOf = typeOf
        self.attribute = attribute
        self.Attribute17 = Attribute17
        self.Attribute = Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute17(self):
        return self.__Attribute17

    @Attribute17.setter
    def Attribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Attribute__Attribute17", None)
        self.__Attribute17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if opp_val == self:
                    setattr(old_value, "type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                setattr(value, "type", self)

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
            if hasattr(old_value, "Owner"):
                opp_val = getattr(old_value, "Owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owner"):
                opp_val = getattr(value, "Owner", None)
                if opp_val is None:
                    setattr(value, "Owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Classifier13"):
                opp_val = getattr(old_value, "Classifier13", None)
                if opp_val == self:
                    setattr(old_value, "Classifier13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier13"):
                opp_val = getattr(value, "Classifier13", None)
                setattr(value, "Classifier13", self)

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
class umlMM_Class(Classifier):

    def __init__(self, kind: str, Class15: "umlMM_Attribute" = None, Class: "umlMM_Associaton" = None, Class6: "umlMM_Associaton" = None, destination: set["umlMM_Associaton"] = None, source: set["umlMM_Associaton"] = None, Owner: set["umlMM_Attribute"] = None):
        self.kind = kind
        self.Class15 = Class15
        self.Class = Class
        self.Class6 = Class6
        self.destination = destination if destination is not None else set()
        self.source = source if source is not None else set()
        self.Owner = Owner if Owner is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
                if hasattr(item, "Associaton8"):
                    opp_val = getattr(item, "Associaton8", None)
                    
                    if opp_val == self:
                        setattr(item, "Associaton8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Associaton8"):
                    opp_val = getattr(item, "Associaton8", None)
                    
                    setattr(item, "Associaton8", self)
                    

    @property
    def Class15(self):
        return self.__Class15

    @Class15.setter
    def Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class15", None)
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
    def Owner(self):
        return self.__Owner

    @Owner.setter
    def Owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Owner", None)
        self.__Owner = value if value is not None else set()
        
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
                if hasattr(item, "Associaton10"):
                    opp_val = getattr(item, "Associaton10", None)
                    
                    if opp_val == self:
                        setattr(item, "Associaton10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Associaton10"):
                    opp_val = getattr(item, "Associaton10", None)
                    
                    setattr(item, "Associaton10", self)
                    

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
    def Class6(self):
        return self.__Class6

    @Class6.setter
    def Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Class__Class6", None)
        self.__Class6 = value
        
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

class umlMM_Classifier:

    def __init__(self, name: str, Classifier13: "umlMM_Attribute" = None, type: "umlMM_Attribute" = None, classifier: "umlMM_Package" = None, Classifier: "umlMM_Package" = None):
        self.name = name
        self.Classifier13 = Classifier13
        self.type = type
        self.classifier = classifier
        self.Classifier = Classifier
        
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
            if hasattr(old_value, "Package19"):
                opp_val = getattr(old_value, "Package19", None)
                if opp_val == self:
                    setattr(old_value, "Package19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package19"):
                opp_val = getattr(value, "Package19", None)
                setattr(value, "Package19", self)

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
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Classifier__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute17"):
                opp_val = getattr(old_value, "Attribute17", None)
                if opp_val == self:
                    setattr(old_value, "Attribute17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute17"):
                opp_val = getattr(value, "Attribute17", None)
                setattr(value, "Attribute17", self)

    @property
    def Classifier13(self):
        return self.__Classifier13

    @Classifier13.setter
    def Classifier13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Classifier__Classifier13", None)
        self.__Classifier13 = value
        
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

class umlMM_Associaton:

    def __init__(self, name: str, Associaton: "umlMM_Package" = None, Association: "umlMM_Package" = None, destinationOf: "umlMM_Class" = None, sourceOf: "umlMM_Class" = None, Associaton8: "umlMM_Class" = None, Associaton10: "umlMM_Class" = None):
        self.name = name
        self.Associaton = Associaton
        self.Association = Association
        self.destinationOf = destinationOf
        self.sourceOf = sourceOf
        self.Associaton8 = Associaton8
        self.Associaton10 = Associaton10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__Association", None)
        self.__Association = value
        
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
    def Associaton10(self):
        return self.__Associaton10

    @Associaton10.setter
    def Associaton10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__Associaton10", None)
        self.__Associaton10 = value
        
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
    def Associaton(self):
        return self.__Associaton

    @Associaton.setter
    def Associaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__Associaton", None)
        self.__Associaton = value
        
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
    def Associaton8(self):
        return self.__Associaton8

    @Associaton8.setter
    def Associaton8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__Associaton8", None)
        self.__Associaton8 = value
        
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
    def sourceOf(self):
        return self.__sourceOf

    @sourceOf.setter
    def sourceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__sourceOf", None)
        self.__sourceOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class6"):
                opp_val = getattr(old_value, "Class6", None)
                if opp_val == self:
                    setattr(old_value, "Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class6"):
                opp_val = getattr(value, "Class6", None)
                setattr(value, "Class6", self)

    @property
    def destinationOf(self):
        return self.__destinationOf

    @destinationOf.setter
    def destinationOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Associaton__destinationOf", None)
        self.__destinationOf = value
        
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

class umlMM_Package:

    def __init__(self, name: str, Package19: "umlMM_Classifier" = None, namespace: set["umlMM_Associaton"] = None, namespace2: set["umlMM_Classifier"] = None, Package: "umlMM_Associaton" = None):
        self.name = name
        self.Package19 = Package19
        self.namespace = namespace if namespace is not None else set()
        self.namespace2 = namespace2 if namespace2 is not None else set()
        self.Package = Package
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

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
                if hasattr(item, "Associaton"):
                    opp_val = getattr(item, "Associaton", None)
                    
                    if opp_val == self:
                        setattr(item, "Associaton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Associaton"):
                    opp_val = getattr(item, "Associaton", None)
                    
                    setattr(item, "Associaton", self)
                    

    @property
    def Package19(self):
        return self.__Package19

    @Package19.setter
    def Package19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlMM_Package__Package19", None)
        self.__Package19 = value
        
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

class umlMM_Datatype(Classifier):

    pass
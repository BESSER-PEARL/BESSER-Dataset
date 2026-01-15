from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class umlMM_Attribute:

    def __init__(self, name: str, Attribute: "umlMM_Class" = None, typeOf: "umlMM_Classifier" = None, attribute: "umlMM_Class" = None, Attribute17: "umlMM_Classifier" = None):
        self.name = name
        self.Attribute = Attribute
        self.typeOf = typeOf
        self.attribute = attribute
        self.Attribute17 = Attribute17
        
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

class umlMM_Classifier:

    def __init__(self, name: str, Classifier: "umlMM_Package" = None, Classifier13: "umlMM_Attribute" = None, type: "umlMM_Attribute" = None, classifier: "umlMM_Package" = None):
        self.name = name
        self.Classifier = Classifier
        self.Classifier13 = Classifier13
        self.type = type
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

    def __init__(self, name: str, Association: "umlMM_Package" = None, destinationOf: "umlMM_Class" = None, sourceOf: "umlMM_Class" = None, Associaton8: "umlMM_Class" = None, Associaton: "umlMM_Package" = None, Associaton10: "umlMM_Class" = None):
        self.name = name
        self.Association = Association
        self.destinationOf = destinationOf
        self.sourceOf = sourceOf
        self.Associaton8 = Associaton8
        self.Associaton = Associaton
        self.Associaton10 = Associaton10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class umlMM_Package:

    def __init__(self, name: str, Package: "umlMM_Associaton" = None, namespace: set["umlMM_Associaton"] = None, namespace2: set["umlMM_Classifier"] = None, Package19: "umlMM_Classifier" = None):
        self.name = name
        self.Package = Package
        self.namespace = namespace if namespace is not None else set()
        self.namespace2 = namespace2 if namespace2 is not None else set()
        self.Package19 = Package19
        
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

class Classifier:

    pass
class umlMM_Datatype(Classifier):

    pass
class umlMM_Class(Classifier):

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_PrimaryObject:

    def __init__(self, unsettableAttributeWithDefault: str, id: int, name: str, unsettableAttribute: str, featureMapReferenceCollection: str, featureMapAttributeType1: str, featureMapAttributeType2: str, featureMapAttributeCollection: str, model_PrimaryObject: "model_TargetObject" = None, model_PrimaryObject27: "model_TargetObject" = None, model_PrimaryObject33: "model_TargetObject" = None, model_PrimaryObject36: set["model_TargetObject"] = None, model_PrimaryObject30: set["model_TargetObject"] = None, model_PrimaryObject39: "model_TargetObject" = None, model_PrimaryObject42: set["model_TargetObject"] = None, model_PrimaryObject45: set["model_TargetObject"] = None, model_PrimaryObject48: set["model_TargetObject"] = None):
        self.unsettableAttributeWithDefault = unsettableAttributeWithDefault
        self.id = id
        self.name = name
        self.unsettableAttribute = unsettableAttribute
        self.featureMapReferenceCollection = featureMapReferenceCollection
        self.featureMapAttributeType1 = featureMapAttributeType1
        self.featureMapAttributeType2 = featureMapAttributeType2
        self.featureMapAttributeCollection = featureMapAttributeCollection
        self.model_PrimaryObject = model_PrimaryObject
        self.model_PrimaryObject27 = model_PrimaryObject27
        self.model_PrimaryObject33 = model_PrimaryObject33
        self.model_PrimaryObject36 = model_PrimaryObject36 if model_PrimaryObject36 is not None else set()
        self.model_PrimaryObject30 = model_PrimaryObject30 if model_PrimaryObject30 is not None else set()
        self.model_PrimaryObject39 = model_PrimaryObject39
        self.model_PrimaryObject42 = model_PrimaryObject42 if model_PrimaryObject42 is not None else set()
        self.model_PrimaryObject45 = model_PrimaryObject45 if model_PrimaryObject45 is not None else set()
        self.model_PrimaryObject48 = model_PrimaryObject48 if model_PrimaryObject48 is not None else set()
        
    @property
    def featureMapAttributeCollection(self) -> str:
        return self.__featureMapAttributeCollection

    @featureMapAttributeCollection.setter
    def featureMapAttributeCollection(self, featureMapAttributeCollection: str):
        self.__featureMapAttributeCollection = featureMapAttributeCollection

    @property
    def featureMapAttributeType2(self) -> str:
        return self.__featureMapAttributeType2

    @featureMapAttributeType2.setter
    def featureMapAttributeType2(self, featureMapAttributeType2: str):
        self.__featureMapAttributeType2 = featureMapAttributeType2

    @property
    def featureMapAttributeType1(self) -> str:
        return self.__featureMapAttributeType1

    @featureMapAttributeType1.setter
    def featureMapAttributeType1(self, featureMapAttributeType1: str):
        self.__featureMapAttributeType1 = featureMapAttributeType1

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureMapReferenceCollection(self) -> str:
        return self.__featureMapReferenceCollection

    @featureMapReferenceCollection.setter
    def featureMapReferenceCollection(self, featureMapReferenceCollection: str):
        self.__featureMapReferenceCollection = featureMapReferenceCollection

    @property
    def unsettableAttribute(self) -> str:
        return self.__unsettableAttribute

    @unsettableAttribute.setter
    def unsettableAttribute(self, unsettableAttribute: str):
        self.__unsettableAttribute = unsettableAttribute

    @property
    def unsettableAttributeWithDefault(self) -> str:
        return self.__unsettableAttributeWithDefault

    @unsettableAttributeWithDefault.setter
    def unsettableAttributeWithDefault(self, unsettableAttributeWithDefault: str):
        self.__unsettableAttributeWithDefault = unsettableAttributeWithDefault

    @property
    def model_PrimaryObject27(self):
        return self.__model_PrimaryObject27

    @model_PrimaryObject27.setter
    def model_PrimaryObject27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject27", None)
        self.__model_PrimaryObject27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject28"):
                opp_val = getattr(old_value, "model_TargetObject28", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject28"):
                opp_val = getattr(value, "model_TargetObject28", None)
                setattr(value, "model_TargetObject28", self)

    @property
    def model_PrimaryObject36(self):
        return self.__model_PrimaryObject36

    @model_PrimaryObject36.setter
    def model_PrimaryObject36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject36", None)
        self.__model_PrimaryObject36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject37"):
                    opp_val = getattr(item, "model_TargetObject37", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject37"):
                    opp_val = getattr(item, "model_TargetObject37", None)
                    
                    setattr(item, "model_TargetObject37", self)
                    

    @property
    def model_PrimaryObject33(self):
        return self.__model_PrimaryObject33

    @model_PrimaryObject33.setter
    def model_PrimaryObject33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject33", None)
        self.__model_PrimaryObject33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject34"):
                opp_val = getattr(old_value, "model_TargetObject34", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject34"):
                opp_val = getattr(value, "model_TargetObject34", None)
                setattr(value, "model_TargetObject34", self)

    @property
    def model_PrimaryObject42(self):
        return self.__model_PrimaryObject42

    @model_PrimaryObject42.setter
    def model_PrimaryObject42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject42", None)
        self.__model_PrimaryObject42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject43"):
                    opp_val = getattr(item, "model_TargetObject43", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject43"):
                    opp_val = getattr(item, "model_TargetObject43", None)
                    
                    setattr(item, "model_TargetObject43", self)
                    

    @property
    def model_PrimaryObject30(self):
        return self.__model_PrimaryObject30

    @model_PrimaryObject30.setter
    def model_PrimaryObject30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject30", None)
        self.__model_PrimaryObject30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject31"):
                    opp_val = getattr(item, "model_TargetObject31", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject31"):
                    opp_val = getattr(item, "model_TargetObject31", None)
                    
                    setattr(item, "model_TargetObject31", self)
                    

    @property
    def model_PrimaryObject48(self):
        return self.__model_PrimaryObject48

    @model_PrimaryObject48.setter
    def model_PrimaryObject48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject48", None)
        self.__model_PrimaryObject48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject49"):
                    opp_val = getattr(item, "model_TargetObject49", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject49"):
                    opp_val = getattr(item, "model_TargetObject49", None)
                    
                    setattr(item, "model_TargetObject49", self)
                    

    @property
    def model_PrimaryObject45(self):
        return self.__model_PrimaryObject45

    @model_PrimaryObject45.setter
    def model_PrimaryObject45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject45", None)
        self.__model_PrimaryObject45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject46"):
                    opp_val = getattr(item, "model_TargetObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject46"):
                    opp_val = getattr(item, "model_TargetObject46", None)
                    
                    setattr(item, "model_TargetObject46", self)
                    

    @property
    def model_PrimaryObject39(self):
        return self.__model_PrimaryObject39

    @model_PrimaryObject39.setter
    def model_PrimaryObject39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject39", None)
        self.__model_PrimaryObject39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject40"):
                opp_val = getattr(old_value, "model_TargetObject40", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject40"):
                opp_val = getattr(value, "model_TargetObject40", None)
                setattr(value, "model_TargetObject40", self)

    @property
    def model_PrimaryObject(self):
        return self.__model_PrimaryObject

    @model_PrimaryObject.setter
    def model_PrimaryObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject", None)
        self.__model_PrimaryObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject"):
                opp_val = getattr(old_value, "model_TargetObject", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject"):
                opp_val = getattr(value, "model_TargetObject", None)
                setattr(value, "model_TargetObject", self)

class model_TargetObject:

    def __init__(self, id: int, singleAttribute: str, arrayAttribute: str, model_TargetObject: "model_PrimaryObject" = None, model_TargetObject28: "model_PrimaryObject" = None, model_TargetObject37: "model_PrimaryObject" = None, model_TargetObject31: "model_PrimaryObject" = None, model_TargetObject34: "model_PrimaryObject" = None, model_TargetObject49: "model_PrimaryObject" = None, model_TargetObject40: "model_PrimaryObject" = None, model_TargetObject43: "model_PrimaryObject" = None, model_TargetObject46: "model_PrimaryObject" = None):
        self.id = id
        self.singleAttribute = singleAttribute
        self.arrayAttribute = arrayAttribute
        self.model_TargetObject = model_TargetObject
        self.model_TargetObject28 = model_TargetObject28
        self.model_TargetObject37 = model_TargetObject37
        self.model_TargetObject31 = model_TargetObject31
        self.model_TargetObject34 = model_TargetObject34
        self.model_TargetObject49 = model_TargetObject49
        self.model_TargetObject40 = model_TargetObject40
        self.model_TargetObject43 = model_TargetObject43
        self.model_TargetObject46 = model_TargetObject46
        
    @property
    def singleAttribute(self) -> str:
        return self.__singleAttribute

    @singleAttribute.setter
    def singleAttribute(self, singleAttribute: str):
        self.__singleAttribute = singleAttribute

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def arrayAttribute(self) -> str:
        return self.__arrayAttribute

    @arrayAttribute.setter
    def arrayAttribute(self, arrayAttribute: str):
        self.__arrayAttribute = arrayAttribute

    @property
    def model_TargetObject40(self):
        return self.__model_TargetObject40

    @model_TargetObject40.setter
    def model_TargetObject40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject40", None)
        self.__model_TargetObject40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject39"):
                opp_val = getattr(old_value, "model_PrimaryObject39", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject39"):
                opp_val = getattr(value, "model_PrimaryObject39", None)
                setattr(value, "model_PrimaryObject39", self)

    @property
    def model_TargetObject46(self):
        return self.__model_TargetObject46

    @model_TargetObject46.setter
    def model_TargetObject46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject46", None)
        self.__model_TargetObject46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject45"):
                opp_val = getattr(old_value, "model_PrimaryObject45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject45"):
                opp_val = getattr(value, "model_PrimaryObject45", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject28(self):
        return self.__model_TargetObject28

    @model_TargetObject28.setter
    def model_TargetObject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject28", None)
        self.__model_TargetObject28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject27"):
                opp_val = getattr(old_value, "model_PrimaryObject27", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject27"):
                opp_val = getattr(value, "model_PrimaryObject27", None)
                setattr(value, "model_PrimaryObject27", self)

    @property
    def model_TargetObject31(self):
        return self.__model_TargetObject31

    @model_TargetObject31.setter
    def model_TargetObject31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject31", None)
        self.__model_TargetObject31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject30"):
                opp_val = getattr(old_value, "model_PrimaryObject30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject30"):
                opp_val = getattr(value, "model_PrimaryObject30", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject49(self):
        return self.__model_TargetObject49

    @model_TargetObject49.setter
    def model_TargetObject49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject49", None)
        self.__model_TargetObject49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject48"):
                opp_val = getattr(old_value, "model_PrimaryObject48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject48"):
                opp_val = getattr(value, "model_PrimaryObject48", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject37(self):
        return self.__model_TargetObject37

    @model_TargetObject37.setter
    def model_TargetObject37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject37", None)
        self.__model_TargetObject37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject36"):
                opp_val = getattr(old_value, "model_PrimaryObject36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject36"):
                opp_val = getattr(value, "model_PrimaryObject36", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject43(self):
        return self.__model_TargetObject43

    @model_TargetObject43.setter
    def model_TargetObject43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject43", None)
        self.__model_TargetObject43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject42"):
                opp_val = getattr(old_value, "model_PrimaryObject42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject42"):
                opp_val = getattr(value, "model_PrimaryObject42", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject34(self):
        return self.__model_TargetObject34

    @model_TargetObject34.setter
    def model_TargetObject34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject34", None)
        self.__model_TargetObject34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject33"):
                opp_val = getattr(old_value, "model_PrimaryObject33", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject33"):
                opp_val = getattr(value, "model_PrimaryObject33", None)
                setattr(value, "model_PrimaryObject33", self)

    @property
    def model_TargetObject(self):
        return self.__model_TargetObject

    @model_TargetObject.setter
    def model_TargetObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject", None)
        self.__model_TargetObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject"):
                opp_val = getattr(old_value, "model_PrimaryObject", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject"):
                opp_val = getattr(value, "model_PrimaryObject", None)
                setattr(value, "model_PrimaryObject", self)

class model_MappedLibrary:

    def __init__(self, books: str, model_MappedLibrary: "model_Location" = None, model_MappedLibrary20: set["model_Book"] = None, model_MappedLibrary23: set["model_Book"] = None):
        self.books = books
        self.model_MappedLibrary = model_MappedLibrary
        self.model_MappedLibrary20 = model_MappedLibrary20 if model_MappedLibrary20 is not None else set()
        self.model_MappedLibrary23 = model_MappedLibrary23 if model_MappedLibrary23 is not None else set()
        
    @property
    def books(self) -> str:
        return self.__books

    @books.setter
    def books(self, books: str):
        self.__books = books

    @property
    def model_MappedLibrary23(self):
        return self.__model_MappedLibrary23

    @model_MappedLibrary23.setter
    def model_MappedLibrary23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary23", None)
        self.__model_MappedLibrary23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book24"):
                    opp_val = getattr(item, "model_Book24", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book24"):
                    opp_val = getattr(item, "model_Book24", None)
                    
                    setattr(item, "model_Book24", self)
                    

    @property
    def model_MappedLibrary(self):
        return self.__model_MappedLibrary

    @model_MappedLibrary.setter
    def model_MappedLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary", None)
        self.__model_MappedLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Location18"):
                opp_val = getattr(old_value, "model_Location18", None)
                if opp_val == self:
                    setattr(old_value, "model_Location18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location18"):
                opp_val = getattr(value, "model_Location18", None)
                setattr(value, "model_Location18", self)

    @property
    def model_MappedLibrary20(self):
        return self.__model_MappedLibrary20

    @model_MappedLibrary20.setter
    def model_MappedLibrary20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary20", None)
        self.__model_MappedLibrary20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book21"):
                    opp_val = getattr(item, "model_Book21", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book21"):
                    opp_val = getattr(item, "model_Book21", None)
                    
                    setattr(item, "model_Book21", self)
                    

class model_ETypes:

    def __init__(self, eBoolean: bool, eByte: str, eByteArray: str, eChar: str, eBigDecimal: str, eBigInteger: str, uris: str, eDate: date, eDouble: float, eFloat: float, eInt: int, eLong: str, eShort: str, eString: str):
        self.eBoolean = eBoolean
        self.eByte = eByte
        self.eByteArray = eByteArray
        self.eChar = eChar
        self.eBigDecimal = eBigDecimal
        self.eBigInteger = eBigInteger
        self.uris = uris
        self.eDate = eDate
        self.eDouble = eDouble
        self.eFloat = eFloat
        self.eInt = eInt
        self.eLong = eLong
        self.eShort = eShort
        self.eString = eString
        
    @property
    def eDouble(self) -> float:
        return self.__eDouble

    @eDouble.setter
    def eDouble(self, eDouble: float):
        self.__eDouble = eDouble

    @property
    def eShort(self) -> str:
        return self.__eShort

    @eShort.setter
    def eShort(self, eShort: str):
        self.__eShort = eShort

    @property
    def eBigDecimal(self) -> str:
        return self.__eBigDecimal

    @eBigDecimal.setter
    def eBigDecimal(self, eBigDecimal: str):
        self.__eBigDecimal = eBigDecimal

    @property
    def eInt(self) -> int:
        return self.__eInt

    @eInt.setter
    def eInt(self, eInt: int):
        self.__eInt = eInt

    @property
    def eLong(self) -> str:
        return self.__eLong

    @eLong.setter
    def eLong(self, eLong: str):
        self.__eLong = eLong

    @property
    def eFloat(self) -> float:
        return self.__eFloat

    @eFloat.setter
    def eFloat(self, eFloat: float):
        self.__eFloat = eFloat

    @property
    def eDate(self) -> date:
        return self.__eDate

    @eDate.setter
    def eDate(self, eDate: date):
        self.__eDate = eDate

    @property
    def eByte(self) -> str:
        return self.__eByte

    @eByte.setter
    def eByte(self, eByte: str):
        self.__eByte = eByte

    @property
    def eBoolean(self) -> bool:
        return self.__eBoolean

    @eBoolean.setter
    def eBoolean(self, eBoolean: bool):
        self.__eBoolean = eBoolean

    @property
    def eChar(self) -> str:
        return self.__eChar

    @eChar.setter
    def eChar(self, eChar: str):
        self.__eChar = eChar

    @property
    def eString(self) -> str:
        return self.__eString

    @eString.setter
    def eString(self, eString: str):
        self.__eString = eString

    @property
    def eByteArray(self) -> str:
        return self.__eByteArray

    @eByteArray.setter
    def eByteArray(self, eByteArray: str):
        self.__eByteArray = eByteArray

    @property
    def uris(self) -> str:
        return self.__uris

    @uris.setter
    def uris(self, uris: str):
        self.__uris = uris

    @property
    def eBigInteger(self) -> str:
        return self.__eBigInteger

    @eBigInteger.setter
    def eBigInteger(self, eBigInteger: str):
        self.__eBigInteger = eBigInteger

class model_Location:

    def __init__(self, address: str, id: str, model_Location: "model_Library" = None, model_Location15: "model_Book" = None, model_Location18: "model_MappedLibrary" = None):
        self.address = address
        self.id = id
        self.model_Location = model_Location
        self.model_Location15 = model_Location15
        self.model_Location18 = model_Location18
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def model_Location15(self):
        return self.__model_Location15

    @model_Location15.setter
    def model_Location15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location15", None)
        self.__model_Location15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Book16"):
                opp_val = getattr(old_value, "model_Book16", None)
                if opp_val == self:
                    setattr(old_value, "model_Book16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Book16"):
                opp_val = getattr(value, "model_Book16", None)
                setattr(value, "model_Book16", self)

    @property
    def model_Location(self):
        return self.__model_Location

    @model_Location.setter
    def model_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location", None)
        self.__model_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library10"):
                opp_val = getattr(old_value, "model_Library10", None)
                if opp_val == self:
                    setattr(old_value, "model_Library10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library10"):
                opp_val = getattr(value, "model_Library10", None)
                setattr(value, "model_Library10", self)

    @property
    def model_Location18(self):
        return self.__model_Location18

    @model_Location18.setter
    def model_Location18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location18", None)
        self.__model_Location18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary"):
                opp_val = getattr(old_value, "model_MappedLibrary", None)
                if opp_val == self:
                    setattr(old_value, "model_MappedLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary"):
                opp_val = getattr(value, "model_MappedLibrary", None)
                setattr(value, "model_MappedLibrary", self)

class model_Library:

    pass
class model_BNode:

    def __init__(self, id: int, model_BNode: "model_BNode" = None, model_BNode6: set["model_BNode"] = None):
        self.id = id
        self.model_BNode = model_BNode
        self.model_BNode6 = model_BNode6 if model_BNode6 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def model_BNode(self):
        return self.__model_BNode

    @model_BNode.setter
    def model_BNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BNode__model_BNode", None)
        self.__model_BNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BNode6"):
                opp_val = getattr(old_value, "model_BNode6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BNode6"):
                opp_val = getattr(value, "model_BNode6", None)
                if opp_val is None:
                    setattr(value, "model_BNode6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_BNode6(self):
        return self.__model_BNode6

    @model_BNode6.setter
    def model_BNode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BNode__model_BNode6", None)
        self.__model_BNode6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_BNode"):
                    opp_val = getattr(item, "model_BNode", None)
                    
                    if opp_val == self:
                        setattr(item, "model_BNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_BNode"):
                    opp_val = getattr(item, "model_BNode", None)
                    
                    setattr(item, "model_BNode", self)
                    

class model_Book:

    def __init__(self, title: str, tags: str, data: str, Book: "model_Person" = None, books: set["model_Person"] = None, model_Book13: "model_Library" = None, model_Book: "model_Library" = None, model_Book16: "model_Location" = None, model_Book21: "model_MappedLibrary" = None, model_Book24: "model_MappedLibrary" = None):
        self.title = title
        self.tags = tags
        self.data = data
        self.Book = Book
        self.books = books if books is not None else set()
        self.model_Book13 = model_Book13
        self.model_Book = model_Book
        self.model_Book16 = model_Book16
        self.model_Book21 = model_Book21
        self.model_Book24 = model_Book24
        
    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def model_Book13(self):
        return self.__model_Book13

    @model_Book13.setter
    def model_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book13", None)
        self.__model_Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library12"):
                opp_val = getattr(old_value, "model_Library12", None)
                if opp_val == self:
                    setattr(old_value, "model_Library12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library12"):
                opp_val = getattr(value, "model_Library12", None)
                setattr(value, "model_Library12", self)

    @property
    def model_Book(self):
        return self.__model_Book

    @model_Book.setter
    def model_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book", None)
        self.__model_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library"):
                opp_val = getattr(old_value, "model_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library"):
                opp_val = getattr(value, "model_Library", None)
                if opp_val is None:
                    setattr(value, "model_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book16(self):
        return self.__model_Book16

    @model_Book16.setter
    def model_Book16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book16", None)
        self.__model_Book16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Location15"):
                opp_val = getattr(old_value, "model_Location15", None)
                if opp_val == self:
                    setattr(old_value, "model_Location15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location15"):
                opp_val = getattr(value, "model_Location15", None)
                setattr(value, "model_Location15", self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book21(self):
        return self.__model_Book21

    @model_Book21.setter
    def model_Book21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book21", None)
        self.__model_Book21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary20"):
                opp_val = getattr(old_value, "model_MappedLibrary20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary20"):
                opp_val = getattr(value, "model_MappedLibrary20", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book24(self):
        return self.__model_Book24

    @model_Book24.setter
    def model_Book24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book24", None)
        self.__model_Book24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary23"):
                opp_val = getattr(old_value, "model_MappedLibrary23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary23"):
                opp_val = getattr(value, "model_MappedLibrary23", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_BookBNode:

    def __init__(self, title: str, model_BookBNode: "model_PersonBNode" = None, model_BookBNode4: set["model_PersonBNode"] = None):
        self.title = title
        self.model_BookBNode = model_BookBNode
        self.model_BookBNode4 = model_BookBNode4 if model_BookBNode4 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def model_BookBNode(self):
        return self.__model_BookBNode

    @model_BookBNode.setter
    def model_BookBNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookBNode__model_BookBNode", None)
        self.__model_BookBNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PersonBNode"):
                opp_val = getattr(old_value, "model_PersonBNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PersonBNode"):
                opp_val = getattr(value, "model_PersonBNode", None)
                if opp_val is None:
                    setattr(value, "model_PersonBNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_BookBNode4(self):
        return self.__model_BookBNode4

    @model_BookBNode4.setter
    def model_BookBNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BookBNode__model_BookBNode4", None)
        self.__model_BookBNode4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_PersonBNode5"):
                    opp_val = getattr(item, "model_PersonBNode5", None)
                    
                    if opp_val == self:
                        setattr(item, "model_PersonBNode5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_PersonBNode5"):
                    opp_val = getattr(item, "model_PersonBNode5", None)
                    
                    setattr(item, "model_PersonBNode5", self)
                    

class model_PersonBNode:

    def __init__(self, name: str, model_PersonBNode: set["model_BookBNode"] = None, model_PersonBNode5: "model_BookBNode" = None):
        self.name = name
        self.model_PersonBNode = model_PersonBNode if model_PersonBNode is not None else set()
        self.model_PersonBNode5 = model_PersonBNode5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_PersonBNode(self):
        return self.__model_PersonBNode

    @model_PersonBNode.setter
    def model_PersonBNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PersonBNode__model_PersonBNode", None)
        self.__model_PersonBNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_BookBNode"):
                    opp_val = getattr(item, "model_BookBNode", None)
                    
                    if opp_val == self:
                        setattr(item, "model_BookBNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_BookBNode"):
                    opp_val = getattr(item, "model_BookBNode", None)
                    
                    setattr(item, "model_BookBNode", self)
                    

    @property
    def model_PersonBNode5(self):
        return self.__model_PersonBNode5

    @model_PersonBNode5.setter
    def model_PersonBNode5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PersonBNode__model_PersonBNode5", None)
        self.__model_PersonBNode5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BookBNode4"):
                opp_val = getattr(old_value, "model_BookBNode4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BookBNode4"):
                opp_val = getattr(value, "model_BookBNode4", None)
                if opp_val is None:
                    setattr(value, "model_BookBNode4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Person:

    def __init__(self, name: str, authors: set["model_Book"] = None, Person: "model_Book" = None):
        self.name = name
        self.authors = authors if authors is not None else set()
        self.Person = Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                if opp_val is None:
                    setattr(value, "books", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

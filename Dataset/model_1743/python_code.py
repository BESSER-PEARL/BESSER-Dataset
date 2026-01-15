from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_TargetObject:

    def __init__(self, singleAttribute: str, arrayAttribute: str, model_TargetObject31: "model_PrimaryObject" = None, model_TargetObject: "model_PrimaryObject" = None, model_TargetObject22: "model_PrimaryObject" = None, model_TargetObject25: "model_PrimaryObject" = None, model_TargetObject28: "model_PrimaryObject" = None, model_TargetObject34: "model_PrimaryObject" = None, model_TargetObject37: "model_PrimaryObject" = None, model_TargetObject40: "model_PrimaryObject" = None):
        self.singleAttribute = singleAttribute
        self.arrayAttribute = arrayAttribute
        self.model_TargetObject31 = model_TargetObject31
        self.model_TargetObject = model_TargetObject
        self.model_TargetObject22 = model_TargetObject22
        self.model_TargetObject25 = model_TargetObject25
        self.model_TargetObject28 = model_TargetObject28
        self.model_TargetObject34 = model_TargetObject34
        self.model_TargetObject37 = model_TargetObject37
        self.model_TargetObject40 = model_TargetObject40
        
    @property
    def singleAttribute(self) -> str:
        return self.__singleAttribute

    @singleAttribute.setter
    def singleAttribute(self, singleAttribute: str):
        self.__singleAttribute = singleAttribute

    @property
    def arrayAttribute(self) -> str:
        return self.__arrayAttribute

    @arrayAttribute.setter
    def arrayAttribute(self, arrayAttribute: str):
        self.__arrayAttribute = arrayAttribute

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject33"):
                opp_val = getattr(value, "model_PrimaryObject33", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject33", set([self]))
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject27"):
                opp_val = getattr(value, "model_PrimaryObject27", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TargetObject22(self):
        return self.__model_TargetObject22

    @model_TargetObject22.setter
    def model_TargetObject22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject22", None)
        self.__model_TargetObject22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject21"):
                opp_val = getattr(old_value, "model_PrimaryObject21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject21"):
                opp_val = getattr(value, "model_PrimaryObject21", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject30"):
                opp_val = getattr(value, "model_PrimaryObject30", None)
                setattr(value, "model_PrimaryObject30", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject39"):
                opp_val = getattr(value, "model_PrimaryObject39", None)
                if opp_val is None:
                    setattr(value, "model_PrimaryObject39", set([self]))
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
    def model_TargetObject25(self):
        return self.__model_TargetObject25

    @model_TargetObject25.setter
    def model_TargetObject25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TargetObject__model_TargetObject25", None)
        self.__model_TargetObject25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PrimaryObject24"):
                opp_val = getattr(old_value, "model_PrimaryObject24", None)
                if opp_val == self:
                    setattr(old_value, "model_PrimaryObject24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PrimaryObject24"):
                opp_val = getattr(value, "model_PrimaryObject24", None)
                setattr(value, "model_PrimaryObject24", self)

class model_PrimaryObject:

    def __init__(self, name: str, featureMapAttributeCollection: str, featureMapReferenceCollection: str, featureMapAttributeType1: str, featureMapAttributeType2: str, model_PrimaryObject30: "model_TargetObject" = None, model_PrimaryObject: "model_TargetObject" = None, model_PrimaryObject21: set["model_TargetObject"] = None, model_PrimaryObject24: "model_TargetObject" = None, model_PrimaryObject27: set["model_TargetObject"] = None, model_PrimaryObject33: set["model_TargetObject"] = None, model_PrimaryObject36: set["model_TargetObject"] = None, model_PrimaryObject39: set["model_TargetObject"] = None):
        self.name = name
        self.featureMapAttributeCollection = featureMapAttributeCollection
        self.featureMapReferenceCollection = featureMapReferenceCollection
        self.featureMapAttributeType1 = featureMapAttributeType1
        self.featureMapAttributeType2 = featureMapAttributeType2
        self.model_PrimaryObject30 = model_PrimaryObject30
        self.model_PrimaryObject = model_PrimaryObject
        self.model_PrimaryObject21 = model_PrimaryObject21 if model_PrimaryObject21 is not None else set()
        self.model_PrimaryObject24 = model_PrimaryObject24
        self.model_PrimaryObject27 = model_PrimaryObject27 if model_PrimaryObject27 is not None else set()
        self.model_PrimaryObject33 = model_PrimaryObject33 if model_PrimaryObject33 is not None else set()
        self.model_PrimaryObject36 = model_PrimaryObject36 if model_PrimaryObject36 is not None else set()
        self.model_PrimaryObject39 = model_PrimaryObject39 if model_PrimaryObject39 is not None else set()
        
    @property
    def featureMapReferenceCollection(self) -> str:
        return self.__featureMapReferenceCollection

    @featureMapReferenceCollection.setter
    def featureMapReferenceCollection(self, featureMapReferenceCollection: str):
        self.__featureMapReferenceCollection = featureMapReferenceCollection

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureMapAttributeType1(self) -> str:
        return self.__featureMapAttributeType1

    @featureMapAttributeType1.setter
    def featureMapAttributeType1(self, featureMapAttributeType1: str):
        self.__featureMapAttributeType1 = featureMapAttributeType1

    @property
    def model_PrimaryObject30(self):
        return self.__model_PrimaryObject30

    @model_PrimaryObject30.setter
    def model_PrimaryObject30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject30", None)
        self.__model_PrimaryObject30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject31"):
                opp_val = getattr(old_value, "model_TargetObject31", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject31"):
                opp_val = getattr(value, "model_TargetObject31", None)
                setattr(value, "model_TargetObject31", self)

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
        self.__model_PrimaryObject33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject34"):
                    opp_val = getattr(item, "model_TargetObject34", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject34"):
                    opp_val = getattr(item, "model_TargetObject34", None)
                    
                    setattr(item, "model_TargetObject34", self)
                    

    @property
    def model_PrimaryObject27(self):
        return self.__model_PrimaryObject27

    @model_PrimaryObject27.setter
    def model_PrimaryObject27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject27", None)
        self.__model_PrimaryObject27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject28"):
                    opp_val = getattr(item, "model_TargetObject28", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject28"):
                    opp_val = getattr(item, "model_TargetObject28", None)
                    
                    setattr(item, "model_TargetObject28", self)
                    

    @property
    def model_PrimaryObject21(self):
        return self.__model_PrimaryObject21

    @model_PrimaryObject21.setter
    def model_PrimaryObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject21", None)
        self.__model_PrimaryObject21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject22"):
                    opp_val = getattr(item, "model_TargetObject22", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject22"):
                    opp_val = getattr(item, "model_TargetObject22", None)
                    
                    setattr(item, "model_TargetObject22", self)
                    

    @property
    def model_PrimaryObject39(self):
        return self.__model_PrimaryObject39

    @model_PrimaryObject39.setter
    def model_PrimaryObject39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject39", None)
        self.__model_PrimaryObject39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_TargetObject40"):
                    opp_val = getattr(item, "model_TargetObject40", None)
                    
                    if opp_val == self:
                        setattr(item, "model_TargetObject40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_TargetObject40"):
                    opp_val = getattr(item, "model_TargetObject40", None)
                    
                    setattr(item, "model_TargetObject40", self)
                    

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

    @property
    def model_PrimaryObject24(self):
        return self.__model_PrimaryObject24

    @model_PrimaryObject24.setter
    def model_PrimaryObject24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PrimaryObject__model_PrimaryObject24", None)
        self.__model_PrimaryObject24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TargetObject25"):
                opp_val = getattr(old_value, "model_TargetObject25", None)
                if opp_val == self:
                    setattr(old_value, "model_TargetObject25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TargetObject25"):
                opp_val = getattr(value, "model_TargetObject25", None)
                setattr(value, "model_TargetObject25", self)

class model_MappedLibrary:

    def __init__(self, books: str, model_MappedLibrary: "model_Location" = None, model_MappedLibrary14: set["model_Book"] = None, model_MappedLibrary17: set["model_Book"] = None):
        self.books = books
        self.model_MappedLibrary = model_MappedLibrary
        self.model_MappedLibrary14 = model_MappedLibrary14 if model_MappedLibrary14 is not None else set()
        self.model_MappedLibrary17 = model_MappedLibrary17 if model_MappedLibrary17 is not None else set()
        
    @property
    def books(self) -> str:
        return self.__books

    @books.setter
    def books(self, books: str):
        self.__books = books

    @property
    def model_MappedLibrary17(self):
        return self.__model_MappedLibrary17

    @model_MappedLibrary17.setter
    def model_MappedLibrary17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary17", None)
        self.__model_MappedLibrary17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book18"):
                    opp_val = getattr(item, "model_Book18", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book18"):
                    opp_val = getattr(item, "model_Book18", None)
                    
                    setattr(item, "model_Book18", self)
                    

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
            if hasattr(old_value, "model_Location12"):
                opp_val = getattr(old_value, "model_Location12", None)
                if opp_val == self:
                    setattr(old_value, "model_Location12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location12"):
                opp_val = getattr(value, "model_Location12", None)
                setattr(value, "model_Location12", self)

    @property
    def model_MappedLibrary14(self):
        return self.__model_MappedLibrary14

    @model_MappedLibrary14.setter
    def model_MappedLibrary14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MappedLibrary__model_MappedLibrary14", None)
        self.__model_MappedLibrary14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book15"):
                    opp_val = getattr(item, "model_Book15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book15"):
                    opp_val = getattr(item, "model_Book15", None)
                    
                    setattr(item, "model_Book15", self)
                    

class model_ETypes:

    def __init__(self, eBigDecimal: str, eBigInteger: str, eBoolean: bool, eByte: str, eByteArray: str, eChar: str, eDate: date, eDouble: float, eFloat: float, eInt: int, eLong: str, eShort: str, eString: str, uris: str):
        self.eBigDecimal = eBigDecimal
        self.eBigInteger = eBigInteger
        self.eBoolean = eBoolean
        self.eByte = eByte
        self.eByteArray = eByteArray
        self.eChar = eChar
        self.eDate = eDate
        self.eDouble = eDouble
        self.eFloat = eFloat
        self.eInt = eInt
        self.eLong = eLong
        self.eShort = eShort
        self.eString = eString
        self.uris = uris
        
    @property
    def eChar(self) -> str:
        return self.__eChar

    @eChar.setter
    def eChar(self, eChar: str):
        self.__eChar = eChar

    @property
    def uris(self) -> str:
        return self.__uris

    @uris.setter
    def uris(self, uris: str):
        self.__uris = uris

    @property
    def eString(self) -> str:
        return self.__eString

    @eString.setter
    def eString(self, eString: str):
        self.__eString = eString

    @property
    def eByte(self) -> str:
        return self.__eByte

    @eByte.setter
    def eByte(self, eByte: str):
        self.__eByte = eByte

    @property
    def eDate(self) -> date:
        return self.__eDate

    @eDate.setter
    def eDate(self, eDate: date):
        self.__eDate = eDate

    @property
    def eDouble(self) -> float:
        return self.__eDouble

    @eDouble.setter
    def eDouble(self, eDouble: float):
        self.__eDouble = eDouble

    @property
    def eLong(self) -> str:
        return self.__eLong

    @eLong.setter
    def eLong(self, eLong: str):
        self.__eLong = eLong

    @property
    def eShort(self) -> str:
        return self.__eShort

    @eShort.setter
    def eShort(self, eShort: str):
        self.__eShort = eShort

    @property
    def eByteArray(self) -> str:
        return self.__eByteArray

    @eByteArray.setter
    def eByteArray(self, eByteArray: str):
        self.__eByteArray = eByteArray

    @property
    def eBigDecimal(self) -> str:
        return self.__eBigDecimal

    @eBigDecimal.setter
    def eBigDecimal(self, eBigDecimal: str):
        self.__eBigDecimal = eBigDecimal

    @property
    def eBoolean(self) -> bool:
        return self.__eBoolean

    @eBoolean.setter
    def eBoolean(self, eBoolean: bool):
        self.__eBoolean = eBoolean

    @property
    def eInt(self) -> int:
        return self.__eInt

    @eInt.setter
    def eInt(self, eInt: int):
        self.__eInt = eInt

    @property
    def eBigInteger(self) -> str:
        return self.__eBigInteger

    @eBigInteger.setter
    def eBigInteger(self, eBigInteger: str):
        self.__eBigInteger = eBigInteger

    @property
    def eFloat(self) -> float:
        return self.__eFloat

    @eFloat.setter
    def eFloat(self, eFloat: float):
        self.__eFloat = eFloat

class model_Location:

    def __init__(self, address: str, id: str, model_Location12: "model_MappedLibrary" = None, model_Location: "model_Library" = None, model_Location9: "model_Book" = None):
        self.address = address
        self.id = id
        self.model_Location12 = model_Location12
        self.model_Location = model_Location
        self.model_Location9 = model_Location9
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

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
            if hasattr(old_value, "model_Library4"):
                opp_val = getattr(old_value, "model_Library4", None)
                if opp_val == self:
                    setattr(old_value, "model_Library4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library4"):
                opp_val = getattr(value, "model_Library4", None)
                setattr(value, "model_Library4", self)

    @property
    def model_Location12(self):
        return self.__model_Location12

    @model_Location12.setter
    def model_Location12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location12", None)
        self.__model_Location12 = value
        
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

    @property
    def model_Location9(self):
        return self.__model_Location9

    @model_Location9.setter
    def model_Location9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Location__model_Location9", None)
        self.__model_Location9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Book10"):
                opp_val = getattr(old_value, "model_Book10", None)
                if opp_val == self:
                    setattr(old_value, "model_Book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Book10"):
                opp_val = getattr(value, "model_Book10", None)
                setattr(value, "model_Book10", self)

class model_Library:

    pass
class model_Book:

    def __init__(self, title: str, tags: str, data: str, Book: "model_Person" = None, books: set["model_Person"] = None, model_Book: "model_Library" = None, model_Book7: "model_Library" = None, model_Book10: "model_Location" = None, model_Book15: "model_MappedLibrary" = None, model_Book18: "model_MappedLibrary" = None):
        self.title = title
        self.tags = tags
        self.data = data
        self.Book = Book
        self.books = books if books is not None else set()
        self.model_Book = model_Book
        self.model_Book7 = model_Book7
        self.model_Book10 = model_Book10
        self.model_Book15 = model_Book15
        self.model_Book18 = model_Book18
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

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
    def model_Book18(self):
        return self.__model_Book18

    @model_Book18.setter
    def model_Book18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book18", None)
        self.__model_Book18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary17"):
                opp_val = getattr(old_value, "model_MappedLibrary17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary17"):
                opp_val = getattr(value, "model_MappedLibrary17", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book15(self):
        return self.__model_Book15

    @model_Book15.setter
    def model_Book15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book15", None)
        self.__model_Book15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappedLibrary14"):
                opp_val = getattr(old_value, "model_MappedLibrary14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappedLibrary14"):
                opp_val = getattr(value, "model_MappedLibrary14", None)
                if opp_val is None:
                    setattr(value, "model_MappedLibrary14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Book10(self):
        return self.__model_Book10

    @model_Book10.setter
    def model_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book10", None)
        self.__model_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Location9"):
                opp_val = getattr(old_value, "model_Location9", None)
                if opp_val == self:
                    setattr(old_value, "model_Location9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Location9"):
                opp_val = getattr(value, "model_Location9", None)
                setattr(value, "model_Location9", self)

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
    def model_Book7(self):
        return self.__model_Book7

    @model_Book7.setter
    def model_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book7", None)
        self.__model_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library6"):
                opp_val = getattr(old_value, "model_Library6", None)
                if opp_val == self:
                    setattr(old_value, "model_Library6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library6"):
                opp_val = getattr(value, "model_Library6", None)
                setattr(value, "model_Library6", self)

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
                    

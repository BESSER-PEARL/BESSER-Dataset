from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class source_ClassDiagram:

    pass
class source_PrimitiveDataType:

    def __init__(self, name: str, source_PrimitiveDataType21: "source_ClassDiagram" = None, source_PrimitiveDataType: "source_Attribute" = None):
        self.name = name
        self.source_PrimitiveDataType21 = source_PrimitiveDataType21
        self.source_PrimitiveDataType = source_PrimitiveDataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source_PrimitiveDataType21(self):
        return self.__source_PrimitiveDataType21

    @source_PrimitiveDataType21.setter
    def source_PrimitiveDataType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_PrimitiveDataType__source_PrimitiveDataType21", None)
        self.__source_PrimitiveDataType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_ClassDiagram20"):
                opp_val = getattr(old_value, "source_ClassDiagram20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_ClassDiagram20"):
                opp_val = getattr(value, "source_ClassDiagram20", None)
                if opp_val is None:
                    setattr(value, "source_ClassDiagram20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source_PrimitiveDataType(self):
        return self.__source_PrimitiveDataType

    @source_PrimitiveDataType.setter
    def source_PrimitiveDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_PrimitiveDataType__source_PrimitiveDataType", None)
        self.__source_PrimitiveDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Attribute13"):
                opp_val = getattr(old_value, "source_Attribute13", None)
                if opp_val == self:
                    setattr(old_value, "source_Attribute13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Attribute13"):
                opp_val = getattr(value, "source_Attribute13", None)
                setattr(value, "source_Attribute13", self)

class source_Association:

    def __init__(self, leftMultiplicity: int, name: str, source_Association: "source_Class" = None, source_Association7: "source_Class" = None, source_Association18: "source_ClassDiagram" = None):
        self.leftMultiplicity = leftMultiplicity
        self.name = name
        self.source_Association = source_Association
        self.source_Association7 = source_Association7
        self.source_Association18 = source_Association18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def leftMultiplicity(self) -> int:
        return self.__leftMultiplicity

    @leftMultiplicity.setter
    def leftMultiplicity(self, leftMultiplicity: int):
        self.__leftMultiplicity = leftMultiplicity

    @property
    def source_Association(self):
        return self.__source_Association

    @source_Association.setter
    def source_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Association__source_Association", None)
        self.__source_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class5"):
                opp_val = getattr(old_value, "source_Class5", None)
                if opp_val == self:
                    setattr(old_value, "source_Class5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class5"):
                opp_val = getattr(value, "source_Class5", None)
                setattr(value, "source_Class5", self)

    @property
    def source_Association18(self):
        return self.__source_Association18

    @source_Association18.setter
    def source_Association18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Association__source_Association18", None)
        self.__source_Association18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_ClassDiagram17"):
                opp_val = getattr(old_value, "source_ClassDiagram17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_ClassDiagram17"):
                opp_val = getattr(value, "source_ClassDiagram17", None)
                if opp_val is None:
                    setattr(value, "source_ClassDiagram17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source_Association7(self):
        return self.__source_Association7

    @source_Association7.setter
    def source_Association7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Association__source_Association7", None)
        self.__source_Association7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class8"):
                opp_val = getattr(old_value, "source_Class8", None)
                if opp_val == self:
                    setattr(old_value, "source_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class8"):
                opp_val = getattr(value, "source_Class8", None)
                setattr(value, "source_Class8", self)

class source_Attribute:

    def __init__(self, name: str, is_primary: bool, source_Attribute10: "source_Class" = None, source_Attribute: "source_Class" = None, source_Attribute13: "source_PrimitiveDataType" = None):
        self.name = name
        self.is_primary = is_primary
        self.source_Attribute10 = source_Attribute10
        self.source_Attribute = source_Attribute
        self.source_Attribute13 = source_Attribute13
        
    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: bool):
        self.__is_primary = is_primary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source_Attribute13(self):
        return self.__source_Attribute13

    @source_Attribute13.setter
    def source_Attribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Attribute__source_Attribute13", None)
        self.__source_Attribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_PrimitiveDataType"):
                opp_val = getattr(old_value, "source_PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "source_PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_PrimitiveDataType"):
                opp_val = getattr(value, "source_PrimitiveDataType", None)
                setattr(value, "source_PrimitiveDataType", self)

    @property
    def source_Attribute(self):
        return self.__source_Attribute

    @source_Attribute.setter
    def source_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Attribute__source_Attribute", None)
        self.__source_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class3"):
                opp_val = getattr(old_value, "source_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class3"):
                opp_val = getattr(value, "source_Class3", None)
                if opp_val is None:
                    setattr(value, "source_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source_Attribute10(self):
        return self.__source_Attribute10

    @source_Attribute10.setter
    def source_Attribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Attribute__source_Attribute10", None)
        self.__source_Attribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class11"):
                opp_val = getattr(old_value, "source_Class11", None)
                if opp_val == self:
                    setattr(old_value, "source_Class11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class11"):
                opp_val = getattr(value, "source_Class11", None)
                setattr(value, "source_Class11", self)

class source_Class:

    def __init__(self, name: str, source_Class5: "source_Association" = None, source_Class8: "source_Association" = None, source_Class11: "source_Attribute" = None, source_Class: "source_Class" = None, source_Class0: "source_Class" = None, source_Class3: set["source_Attribute"] = None, source_Class15: "source_ClassDiagram" = None):
        self.name = name
        self.source_Class5 = source_Class5
        self.source_Class8 = source_Class8
        self.source_Class11 = source_Class11
        self.source_Class = source_Class
        self.source_Class0 = source_Class0
        self.source_Class3 = source_Class3 if source_Class3 is not None else set()
        self.source_Class15 = source_Class15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source_Class15(self):
        return self.__source_Class15

    @source_Class15.setter
    def source_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class15", None)
        self.__source_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_ClassDiagram"):
                opp_val = getattr(old_value, "source_ClassDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_ClassDiagram"):
                opp_val = getattr(value, "source_ClassDiagram", None)
                if opp_val is None:
                    setattr(value, "source_ClassDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source_Class5(self):
        return self.__source_Class5

    @source_Class5.setter
    def source_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class5", None)
        self.__source_Class5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Association"):
                opp_val = getattr(old_value, "source_Association", None)
                if opp_val == self:
                    setattr(old_value, "source_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Association"):
                opp_val = getattr(value, "source_Association", None)
                setattr(value, "source_Association", self)

    @property
    def source_Class3(self):
        return self.__source_Class3

    @source_Class3.setter
    def source_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class3", None)
        self.__source_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "source_Attribute"):
                    opp_val = getattr(item, "source_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "source_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "source_Attribute"):
                    opp_val = getattr(item, "source_Attribute", None)
                    
                    setattr(item, "source_Attribute", self)
                    

    @property
    def source_Class8(self):
        return self.__source_Class8

    @source_Class8.setter
    def source_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class8", None)
        self.__source_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Association7"):
                opp_val = getattr(old_value, "source_Association7", None)
                if opp_val == self:
                    setattr(old_value, "source_Association7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Association7"):
                opp_val = getattr(value, "source_Association7", None)
                setattr(value, "source_Association7", self)

    @property
    def source_Class11(self):
        return self.__source_Class11

    @source_Class11.setter
    def source_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class11", None)
        self.__source_Class11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Attribute10"):
                opp_val = getattr(old_value, "source_Attribute10", None)
                if opp_val == self:
                    setattr(old_value, "source_Attribute10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Attribute10"):
                opp_val = getattr(value, "source_Attribute10", None)
                setattr(value, "source_Attribute10", self)

    @property
    def source_Class0(self):
        return self.__source_Class0

    @source_Class0.setter
    def source_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class0", None)
        self.__source_Class0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class"):
                opp_val = getattr(old_value, "source_Class", None)
                if opp_val == self:
                    setattr(old_value, "source_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class"):
                opp_val = getattr(value, "source_Class", None)
                setattr(value, "source_Class", self)

    @property
    def source_Class(self):
        return self.__source_Class

    @source_Class.setter
    def source_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Class__source_Class", None)
        self.__source_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_Class0"):
                opp_val = getattr(old_value, "source_Class0", None)
                if opp_val == self:
                    setattr(old_value, "source_Class0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_Class0"):
                opp_val = getattr(value, "source_Class0", None)
                setattr(value, "source_Class0", self)

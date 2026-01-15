from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class datatypes_Field:

    def __init__(self, many: bool, name: str, datatypes_Field: "datatypes_ComplexType" = None, datatypes_Field8: "datatypes_DataType" = None):
        self.many = many
        self.name = name
        self.datatypes_Field = datatypes_Field
        self.datatypes_Field8 = datatypes_Field8
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatypes_Field8(self):
        return self.__datatypes_Field8

    @datatypes_Field8.setter
    def datatypes_Field8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_Field__datatypes_Field8", None)
        self.__datatypes_Field8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_DataType"):
                opp_val = getattr(old_value, "datatypes_DataType", None)
                if opp_val == self:
                    setattr(old_value, "datatypes_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_DataType"):
                opp_val = getattr(value, "datatypes_DataType", None)
                setattr(value, "datatypes_DataType", self)

    @property
    def datatypes_Field(self):
        return self.__datatypes_Field

    @datatypes_Field.setter
    def datatypes_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_Field__datatypes_Field", None)
        self.__datatypes_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_ComplexType6"):
                opp_val = getattr(old_value, "datatypes_ComplexType6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_ComplexType6"):
                opp_val = getattr(value, "datatypes_ComplexType6", None)
                if opp_val is None:
                    setattr(value, "datatypes_ComplexType6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataType:

    pass
class datatypes_ComplexType(DataType):

    pass
class datatypes_SimpleType(DataType):

    pass
class AbstractElement:

    pass
class datatypes_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class datatypes_DataType(AbstractElement):

    def __init__(self, name: str, datatypes_DataType: "datatypes_Field" = None):
        self.name = name
        self.datatypes_DataType = datatypes_DataType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatypes_DataType(self):
        return self.__datatypes_DataType

    @datatypes_DataType.setter
    def datatypes_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataType__datatypes_DataType", None)
        self.__datatypes_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_Field8"):
                opp_val = getattr(old_value, "datatypes_Field8", None)
                if opp_val == self:
                    setattr(old_value, "datatypes_Field8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_Field8"):
                opp_val = getattr(value, "datatypes_Field8", None)
                setattr(value, "datatypes_Field8", self)

class datatypes_DataTypeLibrary(AbstractElement):

    def __init__(self, name: str, datatypes_DataTypeLibrary: set["datatypes_AbstractElement"] = None):
        self.name = name
        self.datatypes_DataTypeLibrary = datatypes_DataTypeLibrary if datatypes_DataTypeLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatypes_DataTypeLibrary(self):
        return self.__datatypes_DataTypeLibrary

    @datatypes_DataTypeLibrary.setter
    def datatypes_DataTypeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataTypeLibrary__datatypes_DataTypeLibrary", None)
        self.__datatypes_DataTypeLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datatypes_AbstractElement2"):
                    opp_val = getattr(item, "datatypes_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "datatypes_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datatypes_AbstractElement2"):
                    opp_val = getattr(item, "datatypes_AbstractElement2", None)
                    
                    setattr(item, "datatypes_AbstractElement2", self)
                    

class datatypes_AbstractElement:

    pass
class datatypes_TypeModel:

    pass
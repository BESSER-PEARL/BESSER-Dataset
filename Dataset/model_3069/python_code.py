from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RestStatusCode(Enum):
    INFORMATIONAL = "INFORMATIONAL"
    SUCCESS = "SUCCESS"
    REDIRECTION = "REDIRECTION"
    CLIENT_ERROR = "CLIENT_ERROR"
    SERVER_ERROR = "SERVER_ERROR"
    NETWORK_ERROR = "NETWORK_ERROR"


############################################
# Definition of Classes
############################################

class myDsl_BaseException:

    def __init__(self, errorCode: str, message: str, myDsl_BaseException: "myDsl_ExceptionMapper" = None):
        self.errorCode = errorCode
        self.message = message
        self.myDsl_BaseException = myDsl_BaseException
        
    @property
    def errorCode(self) -> str:
        return self.__errorCode

    @errorCode.setter
    def errorCode(self, errorCode: str):
        self.__errorCode = errorCode

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def myDsl_BaseException(self):
        return self.__myDsl_BaseException

    @myDsl_BaseException.setter
    def myDsl_BaseException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_BaseException__myDsl_BaseException", None)
        self.__myDsl_BaseException = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExceptionMapper154"):
                opp_val = getattr(old_value, "myDsl_ExceptionMapper154", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExceptionMapper154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExceptionMapper154"):
                opp_val = getattr(value, "myDsl_ExceptionMapper154", None)
                setattr(value, "myDsl_ExceptionMapper154", self)

class myDsl_RestException:

    def __init__(self, statusCode: str, message: str, myDsl_RestException152: "myDsl_ExceptionMapper" = None, myDsl_RestException: "myDsl_RestExceptionList" = None):
        self.statusCode = statusCode
        self.message = message
        self.myDsl_RestException152 = myDsl_RestException152
        self.myDsl_RestException = myDsl_RestException
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def statusCode(self) -> str:
        return self.__statusCode

    @statusCode.setter
    def statusCode(self, statusCode: str):
        self.__statusCode = statusCode

    @property
    def myDsl_RestException(self):
        return self.__myDsl_RestException

    @myDsl_RestException.setter
    def myDsl_RestException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestException__myDsl_RestException", None)
        self.__myDsl_RestException = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestExceptionList149"):
                opp_val = getattr(old_value, "myDsl_RestExceptionList149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestExceptionList149"):
                opp_val = getattr(value, "myDsl_RestExceptionList149", None)
                if opp_val is None:
                    setattr(value, "myDsl_RestExceptionList149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_RestException152(self):
        return self.__myDsl_RestException152

    @myDsl_RestException152.setter
    def myDsl_RestException152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestException__myDsl_RestException152", None)
        self.__myDsl_RestException152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExceptionMapper151"):
                opp_val = getattr(old_value, "myDsl_ExceptionMapper151", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExceptionMapper151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExceptionMapper151"):
                opp_val = getattr(value, "myDsl_ExceptionMapper151", None)
                setattr(value, "myDsl_ExceptionMapper151", self)

class myDsl_RestExceptionList:

    pass
class myDsl_DataModelMethodConclusion:

    pass
class myDsl_RestModelMethodConclusion:

    pass
class myDsl_Block:

    def __init__(self, code: str, myDsl_Block: "myDsl_Resource" = None, myDsl_Block47: "myDsl_Resource" = None, myDsl_Block76: "myDsl_Service" = None, myDsl_Block81: "myDsl_Service" = None, myDsl_Block59: "myDsl_Resource" = None, myDsl_Block65: "myDsl_Resource" = None, myDsl_Block105: "myDsl_ValidationService" = None, myDsl_Block111: "myDsl_DataAccessObject" = None, myDsl_Block90: "myDsl_Service" = None, myDsl_Block96: "myDsl_Service" = None, myDsl_Block132: "myDsl_DataAccessObject" = None, myDsl_Block117: "myDsl_DataAccessObject" = None, myDsl_Block126: "myDsl_DataAccessObject" = None):
        self.code = code
        self.myDsl_Block = myDsl_Block
        self.myDsl_Block47 = myDsl_Block47
        self.myDsl_Block76 = myDsl_Block76
        self.myDsl_Block81 = myDsl_Block81
        self.myDsl_Block59 = myDsl_Block59
        self.myDsl_Block65 = myDsl_Block65
        self.myDsl_Block105 = myDsl_Block105
        self.myDsl_Block111 = myDsl_Block111
        self.myDsl_Block90 = myDsl_Block90
        self.myDsl_Block96 = myDsl_Block96
        self.myDsl_Block132 = myDsl_Block132
        self.myDsl_Block117 = myDsl_Block117
        self.myDsl_Block126 = myDsl_Block126
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def myDsl_Block111(self):
        return self.__myDsl_Block111

    @myDsl_Block111.setter
    def myDsl_Block111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block111", None)
        self.__myDsl_Block111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject110"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject110", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject110"):
                opp_val = getattr(value, "myDsl_DataAccessObject110", None)
                setattr(value, "myDsl_DataAccessObject110", self)

    @property
    def myDsl_Block81(self):
        return self.__myDsl_Block81

    @myDsl_Block81.setter
    def myDsl_Block81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block81", None)
        self.__myDsl_Block81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service80"):
                opp_val = getattr(old_value, "myDsl_Service80", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service80"):
                opp_val = getattr(value, "myDsl_Service80", None)
                setattr(value, "myDsl_Service80", self)

    @property
    def myDsl_Block96(self):
        return self.__myDsl_Block96

    @myDsl_Block96.setter
    def myDsl_Block96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block96", None)
        self.__myDsl_Block96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service95"):
                opp_val = getattr(old_value, "myDsl_Service95", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service95"):
                opp_val = getattr(value, "myDsl_Service95", None)
                setattr(value, "myDsl_Service95", self)

    @property
    def myDsl_Block105(self):
        return self.__myDsl_Block105

    @myDsl_Block105.setter
    def myDsl_Block105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block105", None)
        self.__myDsl_Block105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ValidationService104"):
                opp_val = getattr(old_value, "myDsl_ValidationService104", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ValidationService104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ValidationService104"):
                opp_val = getattr(value, "myDsl_ValidationService104", None)
                setattr(value, "myDsl_ValidationService104", self)

    @property
    def myDsl_Block126(self):
        return self.__myDsl_Block126

    @myDsl_Block126.setter
    def myDsl_Block126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block126", None)
        self.__myDsl_Block126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject125"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject125", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject125"):
                opp_val = getattr(value, "myDsl_DataAccessObject125", None)
                setattr(value, "myDsl_DataAccessObject125", self)

    @property
    def myDsl_Block59(self):
        return self.__myDsl_Block59

    @myDsl_Block59.setter
    def myDsl_Block59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block59", None)
        self.__myDsl_Block59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource58"):
                opp_val = getattr(old_value, "myDsl_Resource58", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource58"):
                opp_val = getattr(value, "myDsl_Resource58", None)
                setattr(value, "myDsl_Resource58", self)

    @property
    def myDsl_Block65(self):
        return self.__myDsl_Block65

    @myDsl_Block65.setter
    def myDsl_Block65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block65", None)
        self.__myDsl_Block65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource64"):
                opp_val = getattr(old_value, "myDsl_Resource64", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource64"):
                opp_val = getattr(value, "myDsl_Resource64", None)
                setattr(value, "myDsl_Resource64", self)

    @property
    def myDsl_Block132(self):
        return self.__myDsl_Block132

    @myDsl_Block132.setter
    def myDsl_Block132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block132", None)
        self.__myDsl_Block132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject131"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject131", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject131"):
                opp_val = getattr(value, "myDsl_DataAccessObject131", None)
                setattr(value, "myDsl_DataAccessObject131", self)

    @property
    def myDsl_Block76(self):
        return self.__myDsl_Block76

    @myDsl_Block76.setter
    def myDsl_Block76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block76", None)
        self.__myDsl_Block76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service75"):
                opp_val = getattr(old_value, "myDsl_Service75", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service75"):
                opp_val = getattr(value, "myDsl_Service75", None)
                setattr(value, "myDsl_Service75", self)

    @property
    def myDsl_Block90(self):
        return self.__myDsl_Block90

    @myDsl_Block90.setter
    def myDsl_Block90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block90", None)
        self.__myDsl_Block90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service89"):
                opp_val = getattr(old_value, "myDsl_Service89", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service89"):
                opp_val = getattr(value, "myDsl_Service89", None)
                setattr(value, "myDsl_Service89", self)

    @property
    def myDsl_Block117(self):
        return self.__myDsl_Block117

    @myDsl_Block117.setter
    def myDsl_Block117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block117", None)
        self.__myDsl_Block117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject116"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject116", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject116"):
                opp_val = getattr(value, "myDsl_DataAccessObject116", None)
                setattr(value, "myDsl_DataAccessObject116", self)

    @property
    def myDsl_Block(self):
        return self.__myDsl_Block

    @myDsl_Block.setter
    def myDsl_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block", None)
        self.__myDsl_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource42"):
                opp_val = getattr(old_value, "myDsl_Resource42", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource42"):
                opp_val = getattr(value, "myDsl_Resource42", None)
                setattr(value, "myDsl_Resource42", self)

    @property
    def myDsl_Block47(self):
        return self.__myDsl_Block47

    @myDsl_Block47.setter
    def myDsl_Block47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Block__myDsl_Block47", None)
        self.__myDsl_Block47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource46"):
                opp_val = getattr(old_value, "myDsl_Resource46", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource46"):
                opp_val = getattr(value, "myDsl_Resource46", None)
                setattr(value, "myDsl_Resource46", self)

class myDsl_ValidationService:

    pass
class myDsl_Feature:

    def __init__(self, many: bool, name: str, myDsl_Feature19: "myDsl_RestModel" = None, myDsl_Feature: "myDsl_DataModel" = None, myDsl_Feature28: "myDsl_Type" = None):
        self.many = many
        self.name = name
        self.myDsl_Feature19 = myDsl_Feature19
        self.myDsl_Feature = myDsl_Feature
        self.myDsl_Feature28 = myDsl_Feature28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def myDsl_Feature19(self):
        return self.__myDsl_Feature19

    @myDsl_Feature19.setter
    def myDsl_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature19", None)
        self.__myDsl_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModel18"):
                opp_val = getattr(old_value, "myDsl_RestModel18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModel18"):
                opp_val = getattr(value, "myDsl_RestModel18", None)
                if opp_val is None:
                    setattr(value, "myDsl_RestModel18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Feature(self):
        return self.__myDsl_Feature

    @myDsl_Feature.setter
    def myDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature", None)
        self.__myDsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel14"):
                opp_val = getattr(old_value, "myDsl_DataModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel14"):
                opp_val = getattr(value, "myDsl_DataModel14", None)
                if opp_val is None:
                    setattr(value, "myDsl_DataModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Feature28(self):
        return self.__myDsl_Feature28

    @myDsl_Feature28.setter
    def myDsl_Feature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature28", None)
        self.__myDsl_Feature28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type29"):
                opp_val = getattr(old_value, "myDsl_Type29", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type29"):
                opp_val = getattr(value, "myDsl_Type29", None)
                setattr(value, "myDsl_Type29", self)

class Type:

    pass
class myDsl_DataModel(Type):

    def __init__(self, id: str, myDsl_DataModel23: "myDsl_Transformation" = None, myDsl_DataModel: "myDsl_DataModel" = None, myDsl_DataModel11: "myDsl_DataModel" = None, myDsl_DataModel14: set["myDsl_Feature"] = None, myDsl_DataModel73: "myDsl_Service" = None, myDsl_DataModel108: "myDsl_DataAccessObject" = None, myDsl_DataModel87: "myDsl_Service" = None, myDsl_DataModel123: "myDsl_DataAccessObject" = None, myDsl_DataModel138: "myDsl_DataModelMethodConclusion" = None):
        self.id = id
        self.myDsl_DataModel23 = myDsl_DataModel23
        self.myDsl_DataModel = myDsl_DataModel
        self.myDsl_DataModel11 = myDsl_DataModel11
        self.myDsl_DataModel14 = myDsl_DataModel14 if myDsl_DataModel14 is not None else set()
        self.myDsl_DataModel73 = myDsl_DataModel73
        self.myDsl_DataModel108 = myDsl_DataModel108
        self.myDsl_DataModel87 = myDsl_DataModel87
        self.myDsl_DataModel123 = myDsl_DataModel123
        self.myDsl_DataModel138 = myDsl_DataModel138
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_DataModel138(self):
        return self.__myDsl_DataModel138

    @myDsl_DataModel138.setter
    def myDsl_DataModel138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel138", None)
        self.__myDsl_DataModel138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion137"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion137", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion137"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion137", None)
                setattr(value, "myDsl_DataModelMethodConclusion137", self)

    @property
    def myDsl_DataModel87(self):
        return self.__myDsl_DataModel87

    @myDsl_DataModel87.setter
    def myDsl_DataModel87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel87", None)
        self.__myDsl_DataModel87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service86"):
                opp_val = getattr(old_value, "myDsl_Service86", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service86"):
                opp_val = getattr(value, "myDsl_Service86", None)
                setattr(value, "myDsl_Service86", self)

    @property
    def myDsl_DataModel23(self):
        return self.__myDsl_DataModel23

    @myDsl_DataModel23.setter
    def myDsl_DataModel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel23", None)
        self.__myDsl_DataModel23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Transformation22"):
                opp_val = getattr(old_value, "myDsl_Transformation22", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Transformation22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Transformation22"):
                opp_val = getattr(value, "myDsl_Transformation22", None)
                setattr(value, "myDsl_Transformation22", self)

    @property
    def myDsl_DataModel123(self):
        return self.__myDsl_DataModel123

    @myDsl_DataModel123.setter
    def myDsl_DataModel123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel123", None)
        self.__myDsl_DataModel123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject122"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject122", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject122"):
                opp_val = getattr(value, "myDsl_DataAccessObject122", None)
                setattr(value, "myDsl_DataAccessObject122", self)

    @property
    def myDsl_DataModel14(self):
        return self.__myDsl_DataModel14

    @myDsl_DataModel14.setter
    def myDsl_DataModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel14", None)
        self.__myDsl_DataModel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Feature"):
                    opp_val = getattr(item, "myDsl_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Feature"):
                    opp_val = getattr(item, "myDsl_Feature", None)
                    
                    setattr(item, "myDsl_Feature", self)
                    

    @property
    def myDsl_DataModel73(self):
        return self.__myDsl_DataModel73

    @myDsl_DataModel73.setter
    def myDsl_DataModel73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel73", None)
        self.__myDsl_DataModel73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service72"):
                opp_val = getattr(old_value, "myDsl_Service72", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Service72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service72"):
                opp_val = getattr(value, "myDsl_Service72", None)
                setattr(value, "myDsl_Service72", self)

    @property
    def myDsl_DataModel(self):
        return self.__myDsl_DataModel

    @myDsl_DataModel.setter
    def myDsl_DataModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel", None)
        self.__myDsl_DataModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel11"):
                opp_val = getattr(old_value, "myDsl_DataModel11", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel11"):
                opp_val = getattr(value, "myDsl_DataModel11", None)
                setattr(value, "myDsl_DataModel11", self)

    @property
    def myDsl_DataModel108(self):
        return self.__myDsl_DataModel108

    @myDsl_DataModel108.setter
    def myDsl_DataModel108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel108", None)
        self.__myDsl_DataModel108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataAccessObject107"):
                opp_val = getattr(old_value, "myDsl_DataAccessObject107", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataAccessObject107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataAccessObject107"):
                opp_val = getattr(value, "myDsl_DataAccessObject107", None)
                setattr(value, "myDsl_DataAccessObject107", self)

    @property
    def myDsl_DataModel11(self):
        return self.__myDsl_DataModel11

    @myDsl_DataModel11.setter
    def myDsl_DataModel11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataModel__myDsl_DataModel11", None)
        self.__myDsl_DataModel11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel"):
                opp_val = getattr(old_value, "myDsl_DataModel", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel"):
                opp_val = getattr(value, "myDsl_DataModel", None)
                setattr(value, "myDsl_DataModel", self)

class myDsl_RestModel(Type):

    def __init__(self, id: str, self: str, myDsl_RestModel: "myDsl_RestModel" = None, myDsl_RestModel15: "myDsl_RestModel" = None, myDsl_RestModel18: set["myDsl_Feature"] = None, myDsl_RestModel26: "myDsl_Transformation" = None, myDsl_RestModel53: "myDsl_Resource" = None, myDsl_RestModel38: "myDsl_Resource" = None, myDsl_RestModel102: "myDsl_ValidationService" = None, myDsl_RestModel144: "myDsl_RestModelMethodConclusion" = None):
        self.id = id
        self.self = self
        self.myDsl_RestModel = myDsl_RestModel
        self.myDsl_RestModel15 = myDsl_RestModel15
        self.myDsl_RestModel18 = myDsl_RestModel18 if myDsl_RestModel18 is not None else set()
        self.myDsl_RestModel26 = myDsl_RestModel26
        self.myDsl_RestModel53 = myDsl_RestModel53
        self.myDsl_RestModel38 = myDsl_RestModel38
        self.myDsl_RestModel102 = myDsl_RestModel102
        self.myDsl_RestModel144 = myDsl_RestModel144
        
    @property
    def self(self) -> str:
        return self.__self

    @self.setter
    def self(self, self: str):
        self.__self = self

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_RestModel144(self):
        return self.__myDsl_RestModel144

    @myDsl_RestModel144.setter
    def myDsl_RestModel144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel144", None)
        self.__myDsl_RestModel144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModelMethodConclusion143"):
                opp_val = getattr(old_value, "myDsl_RestModelMethodConclusion143", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModelMethodConclusion143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModelMethodConclusion143"):
                opp_val = getattr(value, "myDsl_RestModelMethodConclusion143", None)
                setattr(value, "myDsl_RestModelMethodConclusion143", self)

    @property
    def myDsl_RestModel53(self):
        return self.__myDsl_RestModel53

    @myDsl_RestModel53.setter
    def myDsl_RestModel53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel53", None)
        self.__myDsl_RestModel53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource52"):
                opp_val = getattr(old_value, "myDsl_Resource52", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource52"):
                opp_val = getattr(value, "myDsl_Resource52", None)
                setattr(value, "myDsl_Resource52", self)

    @property
    def myDsl_RestModel38(self):
        return self.__myDsl_RestModel38

    @myDsl_RestModel38.setter
    def myDsl_RestModel38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel38", None)
        self.__myDsl_RestModel38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource37"):
                opp_val = getattr(old_value, "myDsl_Resource37", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource37"):
                opp_val = getattr(value, "myDsl_Resource37", None)
                setattr(value, "myDsl_Resource37", self)

    @property
    def myDsl_RestModel26(self):
        return self.__myDsl_RestModel26

    @myDsl_RestModel26.setter
    def myDsl_RestModel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel26", None)
        self.__myDsl_RestModel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Transformation25"):
                opp_val = getattr(old_value, "myDsl_Transformation25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Transformation25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Transformation25"):
                opp_val = getattr(value, "myDsl_Transformation25", None)
                setattr(value, "myDsl_Transformation25", self)

    @property
    def myDsl_RestModel102(self):
        return self.__myDsl_RestModel102

    @myDsl_RestModel102.setter
    def myDsl_RestModel102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel102", None)
        self.__myDsl_RestModel102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ValidationService101"):
                opp_val = getattr(old_value, "myDsl_ValidationService101", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ValidationService101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ValidationService101"):
                opp_val = getattr(value, "myDsl_ValidationService101", None)
                setattr(value, "myDsl_ValidationService101", self)

    @property
    def myDsl_RestModel18(self):
        return self.__myDsl_RestModel18

    @myDsl_RestModel18.setter
    def myDsl_RestModel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel18", None)
        self.__myDsl_RestModel18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Feature19"):
                    opp_val = getattr(item, "myDsl_Feature19", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Feature19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Feature19"):
                    opp_val = getattr(item, "myDsl_Feature19", None)
                    
                    setattr(item, "myDsl_Feature19", self)
                    

    @property
    def myDsl_RestModel(self):
        return self.__myDsl_RestModel

    @myDsl_RestModel.setter
    def myDsl_RestModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel", None)
        self.__myDsl_RestModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModel15"):
                opp_val = getattr(old_value, "myDsl_RestModel15", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModel15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModel15"):
                opp_val = getattr(value, "myDsl_RestModel15", None)
                setattr(value, "myDsl_RestModel15", self)

    @property
    def myDsl_RestModel15(self):
        return self.__myDsl_RestModel15

    @myDsl_RestModel15.setter
    def myDsl_RestModel15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_RestModel__myDsl_RestModel15", None)
        self.__myDsl_RestModel15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModel"):
                opp_val = getattr(old_value, "myDsl_RestModel", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModel"):
                opp_val = getattr(value, "myDsl_RestModel", None)
                setattr(value, "myDsl_RestModel", self)

class myDsl_PrimitiveType(Type):

    pass
class myDsl_Transformation:

    pass
class myDsl_ModelMapper(Type):

    pass
class myDsl_Type:

    def __init__(self, name: str, myDsl_Type: "myDsl_DomainModel" = None, myDsl_Type29: "myDsl_Feature" = None):
        self.name = name
        self.myDsl_Type = myDsl_Type
        self.myDsl_Type29 = myDsl_Type29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type29(self):
        return self.__myDsl_Type29

    @myDsl_Type29.setter
    def myDsl_Type29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type29", None)
        self.__myDsl_Type29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Feature28"):
                opp_val = getattr(old_value, "myDsl_Feature28", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature28"):
                opp_val = getattr(value, "myDsl_Feature28", None)
                setattr(value, "myDsl_Feature28", self)

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DomainModel"):
                opp_val = getattr(old_value, "myDsl_DomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DomainModel"):
                opp_val = getattr(value, "myDsl_DomainModel", None)
                if opp_val is None:
                    setattr(value, "myDsl_DomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_DomainModel:

    pass
class myDsl_ExceptionMapper:

    def __init__(self, name: str, myDsl_ExceptionMapper: "myDsl_RestAPI" = None, myDsl_ExceptionMapper35: "myDsl_Resource" = None, myDsl_ExceptionMapper151: "myDsl_RestException" = None, myDsl_ExceptionMapper154: "myDsl_BaseException" = None):
        self.name = name
        self.myDsl_ExceptionMapper = myDsl_ExceptionMapper
        self.myDsl_ExceptionMapper35 = myDsl_ExceptionMapper35
        self.myDsl_ExceptionMapper151 = myDsl_ExceptionMapper151
        self.myDsl_ExceptionMapper154 = myDsl_ExceptionMapper154
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_ExceptionMapper154(self):
        return self.__myDsl_ExceptionMapper154

    @myDsl_ExceptionMapper154.setter
    def myDsl_ExceptionMapper154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExceptionMapper__myDsl_ExceptionMapper154", None)
        self.__myDsl_ExceptionMapper154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_BaseException"):
                opp_val = getattr(old_value, "myDsl_BaseException", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_BaseException", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_BaseException"):
                opp_val = getattr(value, "myDsl_BaseException", None)
                setattr(value, "myDsl_BaseException", self)

    @property
    def myDsl_ExceptionMapper(self):
        return self.__myDsl_ExceptionMapper

    @myDsl_ExceptionMapper.setter
    def myDsl_ExceptionMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExceptionMapper__myDsl_ExceptionMapper", None)
        self.__myDsl_ExceptionMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestAPI10"):
                opp_val = getattr(old_value, "myDsl_RestAPI10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestAPI10"):
                opp_val = getattr(value, "myDsl_RestAPI10", None)
                if opp_val is None:
                    setattr(value, "myDsl_RestAPI10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_ExceptionMapper35(self):
        return self.__myDsl_ExceptionMapper35

    @myDsl_ExceptionMapper35.setter
    def myDsl_ExceptionMapper35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExceptionMapper__myDsl_ExceptionMapper35", None)
        self.__myDsl_ExceptionMapper35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource34"):
                opp_val = getattr(old_value, "myDsl_Resource34", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Resource34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource34"):
                opp_val = getattr(value, "myDsl_Resource34", None)
                setattr(value, "myDsl_Resource34", self)

    @property
    def myDsl_ExceptionMapper151(self):
        return self.__myDsl_ExceptionMapper151

    @myDsl_ExceptionMapper151.setter
    def myDsl_ExceptionMapper151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ExceptionMapper__myDsl_ExceptionMapper151", None)
        self.__myDsl_ExceptionMapper151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestException152"):
                opp_val = getattr(old_value, "myDsl_RestException152", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestException152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestException152"):
                opp_val = getattr(value, "myDsl_RestException152", None)
                setattr(value, "myDsl_RestException152", self)

class myDsl_DataAccessObject:

    def __init__(self, name: str, findby: str, deleteby: str, updateby: str, myDsl_DataAccessObject: "myDsl_RestAPI" = None, myDsl_DataAccessObject70: "myDsl_Service" = None, myDsl_DataAccessObject107: "myDsl_DataModel" = None, myDsl_DataAccessObject110: "myDsl_Block" = None, myDsl_DataAccessObject113: "myDsl_DataModelMethodConclusion" = None, myDsl_DataAccessObject128: "myDsl_DataModelMethodConclusion" = None, myDsl_DataAccessObject131: "myDsl_Block" = None, myDsl_DataAccessObject134: "myDsl_RestExceptionList" = None, myDsl_DataAccessObject116: "myDsl_Block" = None, myDsl_DataAccessObject119: "myDsl_DataModelMethodConclusion" = None, myDsl_DataAccessObject122: "myDsl_DataModel" = None, myDsl_DataAccessObject125: "myDsl_Block" = None):
        self.name = name
        self.findby = findby
        self.deleteby = deleteby
        self.updateby = updateby
        self.myDsl_DataAccessObject = myDsl_DataAccessObject
        self.myDsl_DataAccessObject70 = myDsl_DataAccessObject70
        self.myDsl_DataAccessObject107 = myDsl_DataAccessObject107
        self.myDsl_DataAccessObject110 = myDsl_DataAccessObject110
        self.myDsl_DataAccessObject113 = myDsl_DataAccessObject113
        self.myDsl_DataAccessObject128 = myDsl_DataAccessObject128
        self.myDsl_DataAccessObject131 = myDsl_DataAccessObject131
        self.myDsl_DataAccessObject134 = myDsl_DataAccessObject134
        self.myDsl_DataAccessObject116 = myDsl_DataAccessObject116
        self.myDsl_DataAccessObject119 = myDsl_DataAccessObject119
        self.myDsl_DataAccessObject122 = myDsl_DataAccessObject122
        self.myDsl_DataAccessObject125 = myDsl_DataAccessObject125
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def updateby(self) -> str:
        return self.__updateby

    @updateby.setter
    def updateby(self, updateby: str):
        self.__updateby = updateby

    @property
    def findby(self) -> str:
        return self.__findby

    @findby.setter
    def findby(self, findby: str):
        self.__findby = findby

    @property
    def deleteby(self) -> str:
        return self.__deleteby

    @deleteby.setter
    def deleteby(self, deleteby: str):
        self.__deleteby = deleteby

    @property
    def myDsl_DataAccessObject116(self):
        return self.__myDsl_DataAccessObject116

    @myDsl_DataAccessObject116.setter
    def myDsl_DataAccessObject116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject116", None)
        self.__myDsl_DataAccessObject116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block117"):
                opp_val = getattr(old_value, "myDsl_Block117", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block117"):
                opp_val = getattr(value, "myDsl_Block117", None)
                setattr(value, "myDsl_Block117", self)

    @property
    def myDsl_DataAccessObject134(self):
        return self.__myDsl_DataAccessObject134

    @myDsl_DataAccessObject134.setter
    def myDsl_DataAccessObject134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject134", None)
        self.__myDsl_DataAccessObject134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestExceptionList135"):
                opp_val = getattr(old_value, "myDsl_RestExceptionList135", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestExceptionList135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestExceptionList135"):
                opp_val = getattr(value, "myDsl_RestExceptionList135", None)
                setattr(value, "myDsl_RestExceptionList135", self)

    @property
    def myDsl_DataAccessObject128(self):
        return self.__myDsl_DataAccessObject128

    @myDsl_DataAccessObject128.setter
    def myDsl_DataAccessObject128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject128", None)
        self.__myDsl_DataAccessObject128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion129"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion129", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion129"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion129", None)
                setattr(value, "myDsl_DataModelMethodConclusion129", self)

    @property
    def myDsl_DataAccessObject122(self):
        return self.__myDsl_DataAccessObject122

    @myDsl_DataAccessObject122.setter
    def myDsl_DataAccessObject122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject122", None)
        self.__myDsl_DataAccessObject122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel123"):
                opp_val = getattr(old_value, "myDsl_DataModel123", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel123"):
                opp_val = getattr(value, "myDsl_DataModel123", None)
                setattr(value, "myDsl_DataModel123", self)

    @property
    def myDsl_DataAccessObject119(self):
        return self.__myDsl_DataAccessObject119

    @myDsl_DataAccessObject119.setter
    def myDsl_DataAccessObject119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject119", None)
        self.__myDsl_DataAccessObject119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion120"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion120", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion120"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion120", None)
                setattr(value, "myDsl_DataModelMethodConclusion120", self)

    @property
    def myDsl_DataAccessObject107(self):
        return self.__myDsl_DataAccessObject107

    @myDsl_DataAccessObject107.setter
    def myDsl_DataAccessObject107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject107", None)
        self.__myDsl_DataAccessObject107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel108"):
                opp_val = getattr(old_value, "myDsl_DataModel108", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel108"):
                opp_val = getattr(value, "myDsl_DataModel108", None)
                setattr(value, "myDsl_DataModel108", self)

    @property
    def myDsl_DataAccessObject131(self):
        return self.__myDsl_DataAccessObject131

    @myDsl_DataAccessObject131.setter
    def myDsl_DataAccessObject131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject131", None)
        self.__myDsl_DataAccessObject131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block132"):
                opp_val = getattr(old_value, "myDsl_Block132", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block132"):
                opp_val = getattr(value, "myDsl_Block132", None)
                setattr(value, "myDsl_Block132", self)

    @property
    def myDsl_DataAccessObject(self):
        return self.__myDsl_DataAccessObject

    @myDsl_DataAccessObject.setter
    def myDsl_DataAccessObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject", None)
        self.__myDsl_DataAccessObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestAPI8"):
                opp_val = getattr(old_value, "myDsl_RestAPI8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestAPI8"):
                opp_val = getattr(value, "myDsl_RestAPI8", None)
                if opp_val is None:
                    setattr(value, "myDsl_RestAPI8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_DataAccessObject70(self):
        return self.__myDsl_DataAccessObject70

    @myDsl_DataAccessObject70.setter
    def myDsl_DataAccessObject70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject70", None)
        self.__myDsl_DataAccessObject70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Service69"):
                opp_val = getattr(old_value, "myDsl_Service69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Service69"):
                opp_val = getattr(value, "myDsl_Service69", None)
                if opp_val is None:
                    setattr(value, "myDsl_Service69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_DataAccessObject125(self):
        return self.__myDsl_DataAccessObject125

    @myDsl_DataAccessObject125.setter
    def myDsl_DataAccessObject125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject125", None)
        self.__myDsl_DataAccessObject125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block126"):
                opp_val = getattr(old_value, "myDsl_Block126", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block126"):
                opp_val = getattr(value, "myDsl_Block126", None)
                setattr(value, "myDsl_Block126", self)

    @property
    def myDsl_DataAccessObject113(self):
        return self.__myDsl_DataAccessObject113

    @myDsl_DataAccessObject113.setter
    def myDsl_DataAccessObject113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject113", None)
        self.__myDsl_DataAccessObject113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion114"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion114", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion114"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion114", None)
                setattr(value, "myDsl_DataModelMethodConclusion114", self)

    @property
    def myDsl_DataAccessObject110(self):
        return self.__myDsl_DataAccessObject110

    @myDsl_DataAccessObject110.setter
    def myDsl_DataAccessObject110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_DataAccessObject__myDsl_DataAccessObject110", None)
        self.__myDsl_DataAccessObject110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block111"):
                opp_val = getattr(old_value, "myDsl_Block111", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block111"):
                opp_val = getattr(value, "myDsl_Block111", None)
                setattr(value, "myDsl_Block111", self)

class myDsl_Service:

    def __init__(self, name: str, findby: str, updateby: str, deleteby: str, myDsl_Service: "myDsl_RestAPI" = None, myDsl_Service32: "myDsl_Resource" = None, myDsl_Service69: set["myDsl_DataAccessObject"] = None, myDsl_Service72: "myDsl_DataModel" = None, myDsl_Service75: "myDsl_Block" = None, myDsl_Service78: "myDsl_DataModelMethodConclusion" = None, myDsl_Service80: "myDsl_Block" = None, myDsl_Service83: "myDsl_DataModelMethodConclusion" = None, myDsl_Service98: "myDsl_RestExceptionList" = None, myDsl_Service86: "myDsl_DataModel" = None, myDsl_Service89: "myDsl_Block" = None, myDsl_Service92: "myDsl_DataModelMethodConclusion" = None, myDsl_Service95: "myDsl_Block" = None):
        self.name = name
        self.findby = findby
        self.updateby = updateby
        self.deleteby = deleteby
        self.myDsl_Service = myDsl_Service
        self.myDsl_Service32 = myDsl_Service32
        self.myDsl_Service69 = myDsl_Service69 if myDsl_Service69 is not None else set()
        self.myDsl_Service72 = myDsl_Service72
        self.myDsl_Service75 = myDsl_Service75
        self.myDsl_Service78 = myDsl_Service78
        self.myDsl_Service80 = myDsl_Service80
        self.myDsl_Service83 = myDsl_Service83
        self.myDsl_Service98 = myDsl_Service98
        self.myDsl_Service86 = myDsl_Service86
        self.myDsl_Service89 = myDsl_Service89
        self.myDsl_Service92 = myDsl_Service92
        self.myDsl_Service95 = myDsl_Service95
        
    @property
    def deleteby(self) -> str:
        return self.__deleteby

    @deleteby.setter
    def deleteby(self, deleteby: str):
        self.__deleteby = deleteby

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def updateby(self) -> str:
        return self.__updateby

    @updateby.setter
    def updateby(self, updateby: str):
        self.__updateby = updateby

    @property
    def findby(self) -> str:
        return self.__findby

    @findby.setter
    def findby(self, findby: str):
        self.__findby = findby

    @property
    def myDsl_Service86(self):
        return self.__myDsl_Service86

    @myDsl_Service86.setter
    def myDsl_Service86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service86", None)
        self.__myDsl_Service86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel87"):
                opp_val = getattr(old_value, "myDsl_DataModel87", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel87"):
                opp_val = getattr(value, "myDsl_DataModel87", None)
                setattr(value, "myDsl_DataModel87", self)

    @property
    def myDsl_Service78(self):
        return self.__myDsl_Service78

    @myDsl_Service78.setter
    def myDsl_Service78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service78", None)
        self.__myDsl_Service78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion", None)
                setattr(value, "myDsl_DataModelMethodConclusion", self)

    @property
    def myDsl_Service32(self):
        return self.__myDsl_Service32

    @myDsl_Service32.setter
    def myDsl_Service32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service32", None)
        self.__myDsl_Service32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Resource31"):
                opp_val = getattr(old_value, "myDsl_Resource31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Resource31"):
                opp_val = getattr(value, "myDsl_Resource31", None)
                if opp_val is None:
                    setattr(value, "myDsl_Resource31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Service72(self):
        return self.__myDsl_Service72

    @myDsl_Service72.setter
    def myDsl_Service72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service72", None)
        self.__myDsl_Service72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModel73"):
                opp_val = getattr(old_value, "myDsl_DataModel73", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModel73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModel73"):
                opp_val = getattr(value, "myDsl_DataModel73", None)
                setattr(value, "myDsl_DataModel73", self)

    @property
    def myDsl_Service80(self):
        return self.__myDsl_Service80

    @myDsl_Service80.setter
    def myDsl_Service80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service80", None)
        self.__myDsl_Service80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block81"):
                opp_val = getattr(old_value, "myDsl_Block81", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block81"):
                opp_val = getattr(value, "myDsl_Block81", None)
                setattr(value, "myDsl_Block81", self)

    @property
    def myDsl_Service95(self):
        return self.__myDsl_Service95

    @myDsl_Service95.setter
    def myDsl_Service95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service95", None)
        self.__myDsl_Service95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block96"):
                opp_val = getattr(old_value, "myDsl_Block96", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block96"):
                opp_val = getattr(value, "myDsl_Block96", None)
                setattr(value, "myDsl_Block96", self)

    @property
    def myDsl_Service98(self):
        return self.__myDsl_Service98

    @myDsl_Service98.setter
    def myDsl_Service98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service98", None)
        self.__myDsl_Service98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestExceptionList99"):
                opp_val = getattr(old_value, "myDsl_RestExceptionList99", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestExceptionList99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestExceptionList99"):
                opp_val = getattr(value, "myDsl_RestExceptionList99", None)
                setattr(value, "myDsl_RestExceptionList99", self)

    @property
    def myDsl_Service69(self):
        return self.__myDsl_Service69

    @myDsl_Service69.setter
    def myDsl_Service69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service69", None)
        self.__myDsl_Service69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_DataAccessObject70"):
                    opp_val = getattr(item, "myDsl_DataAccessObject70", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_DataAccessObject70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_DataAccessObject70"):
                    opp_val = getattr(item, "myDsl_DataAccessObject70", None)
                    
                    setattr(item, "myDsl_DataAccessObject70", self)
                    

    @property
    def myDsl_Service89(self):
        return self.__myDsl_Service89

    @myDsl_Service89.setter
    def myDsl_Service89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service89", None)
        self.__myDsl_Service89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block90"):
                opp_val = getattr(old_value, "myDsl_Block90", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block90"):
                opp_val = getattr(value, "myDsl_Block90", None)
                setattr(value, "myDsl_Block90", self)

    @property
    def myDsl_Service92(self):
        return self.__myDsl_Service92

    @myDsl_Service92.setter
    def myDsl_Service92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service92", None)
        self.__myDsl_Service92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion93"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion93", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion93"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion93", None)
                setattr(value, "myDsl_DataModelMethodConclusion93", self)

    @property
    def myDsl_Service(self):
        return self.__myDsl_Service

    @myDsl_Service.setter
    def myDsl_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service", None)
        self.__myDsl_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestAPI6"):
                opp_val = getattr(old_value, "myDsl_RestAPI6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestAPI6"):
                opp_val = getattr(value, "myDsl_RestAPI6", None)
                if opp_val is None:
                    setattr(value, "myDsl_RestAPI6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Service83(self):
        return self.__myDsl_Service83

    @myDsl_Service83.setter
    def myDsl_Service83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service83", None)
        self.__myDsl_Service83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_DataModelMethodConclusion84"):
                opp_val = getattr(old_value, "myDsl_DataModelMethodConclusion84", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_DataModelMethodConclusion84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_DataModelMethodConclusion84"):
                opp_val = getattr(value, "myDsl_DataModelMethodConclusion84", None)
                setattr(value, "myDsl_DataModelMethodConclusion84", self)

    @property
    def myDsl_Service75(self):
        return self.__myDsl_Service75

    @myDsl_Service75.setter
    def myDsl_Service75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Service__myDsl_Service75", None)
        self.__myDsl_Service75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block76"):
                opp_val = getattr(old_value, "myDsl_Block76", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block76"):
                opp_val = getattr(value, "myDsl_Block76", None)
                setattr(value, "myDsl_Block76", self)

class myDsl_Resource:

    def __init__(self, findby: str, updateby: str, name: str, deleteby: str, myDsl_Resource: "myDsl_RestAPI" = None, myDsl_Resource40: "myDsl_ValidationService" = None, myDsl_Resource42: "myDsl_Block" = None, myDsl_Resource44: "myDsl_RestModelMethodConclusion" = None, myDsl_Resource46: "myDsl_Block" = None, myDsl_Resource49: "myDsl_RestModelMethodConclusion" = None, myDsl_Resource52: "myDsl_RestModel" = None, myDsl_Resource55: "myDsl_ValidationService" = None, myDsl_Resource31: set["myDsl_Service"] = None, myDsl_Resource34: "myDsl_ExceptionMapper" = None, myDsl_Resource37: "myDsl_RestModel" = None, myDsl_Resource58: "myDsl_Block" = None, myDsl_Resource61: "myDsl_RestModelMethodConclusion" = None, myDsl_Resource64: "myDsl_Block" = None, myDsl_Resource67: "myDsl_RestExceptionList" = None):
        self.findby = findby
        self.updateby = updateby
        self.name = name
        self.deleteby = deleteby
        self.myDsl_Resource = myDsl_Resource
        self.myDsl_Resource40 = myDsl_Resource40
        self.myDsl_Resource42 = myDsl_Resource42
        self.myDsl_Resource44 = myDsl_Resource44
        self.myDsl_Resource46 = myDsl_Resource46
        self.myDsl_Resource49 = myDsl_Resource49
        self.myDsl_Resource52 = myDsl_Resource52
        self.myDsl_Resource55 = myDsl_Resource55
        self.myDsl_Resource31 = myDsl_Resource31 if myDsl_Resource31 is not None else set()
        self.myDsl_Resource34 = myDsl_Resource34
        self.myDsl_Resource37 = myDsl_Resource37
        self.myDsl_Resource58 = myDsl_Resource58
        self.myDsl_Resource61 = myDsl_Resource61
        self.myDsl_Resource64 = myDsl_Resource64
        self.myDsl_Resource67 = myDsl_Resource67
        
    @property
    def deleteby(self) -> str:
        return self.__deleteby

    @deleteby.setter
    def deleteby(self, deleteby: str):
        self.__deleteby = deleteby

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def findby(self) -> str:
        return self.__findby

    @findby.setter
    def findby(self, findby: str):
        self.__findby = findby

    @property
    def updateby(self) -> str:
        return self.__updateby

    @updateby.setter
    def updateby(self, updateby: str):
        self.__updateby = updateby

    @property
    def myDsl_Resource61(self):
        return self.__myDsl_Resource61

    @myDsl_Resource61.setter
    def myDsl_Resource61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource61", None)
        self.__myDsl_Resource61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModelMethodConclusion62"):
                opp_val = getattr(old_value, "myDsl_RestModelMethodConclusion62", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModelMethodConclusion62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModelMethodConclusion62"):
                opp_val = getattr(value, "myDsl_RestModelMethodConclusion62", None)
                setattr(value, "myDsl_RestModelMethodConclusion62", self)

    @property
    def myDsl_Resource40(self):
        return self.__myDsl_Resource40

    @myDsl_Resource40.setter
    def myDsl_Resource40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource40", None)
        self.__myDsl_Resource40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ValidationService"):
                opp_val = getattr(old_value, "myDsl_ValidationService", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ValidationService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ValidationService"):
                opp_val = getattr(value, "myDsl_ValidationService", None)
                setattr(value, "myDsl_ValidationService", self)

    @property
    def myDsl_Resource31(self):
        return self.__myDsl_Resource31

    @myDsl_Resource31.setter
    def myDsl_Resource31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource31", None)
        self.__myDsl_Resource31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Service32"):
                    opp_val = getattr(item, "myDsl_Service32", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Service32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Service32"):
                    opp_val = getattr(item, "myDsl_Service32", None)
                    
                    setattr(item, "myDsl_Service32", self)
                    

    @property
    def myDsl_Resource42(self):
        return self.__myDsl_Resource42

    @myDsl_Resource42.setter
    def myDsl_Resource42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource42", None)
        self.__myDsl_Resource42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block"):
                opp_val = getattr(old_value, "myDsl_Block", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block"):
                opp_val = getattr(value, "myDsl_Block", None)
                setattr(value, "myDsl_Block", self)

    @property
    def myDsl_Resource46(self):
        return self.__myDsl_Resource46

    @myDsl_Resource46.setter
    def myDsl_Resource46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource46", None)
        self.__myDsl_Resource46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block47"):
                opp_val = getattr(old_value, "myDsl_Block47", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block47"):
                opp_val = getattr(value, "myDsl_Block47", None)
                setattr(value, "myDsl_Block47", self)

    @property
    def myDsl_Resource49(self):
        return self.__myDsl_Resource49

    @myDsl_Resource49.setter
    def myDsl_Resource49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource49", None)
        self.__myDsl_Resource49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModelMethodConclusion50"):
                opp_val = getattr(old_value, "myDsl_RestModelMethodConclusion50", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModelMethodConclusion50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModelMethodConclusion50"):
                opp_val = getattr(value, "myDsl_RestModelMethodConclusion50", None)
                setattr(value, "myDsl_RestModelMethodConclusion50", self)

    @property
    def myDsl_Resource64(self):
        return self.__myDsl_Resource64

    @myDsl_Resource64.setter
    def myDsl_Resource64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource64", None)
        self.__myDsl_Resource64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block65"):
                opp_val = getattr(old_value, "myDsl_Block65", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block65"):
                opp_val = getattr(value, "myDsl_Block65", None)
                setattr(value, "myDsl_Block65", self)

    @property
    def myDsl_Resource44(self):
        return self.__myDsl_Resource44

    @myDsl_Resource44.setter
    def myDsl_Resource44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource44", None)
        self.__myDsl_Resource44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModelMethodConclusion"):
                opp_val = getattr(old_value, "myDsl_RestModelMethodConclusion", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModelMethodConclusion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModelMethodConclusion"):
                opp_val = getattr(value, "myDsl_RestModelMethodConclusion", None)
                setattr(value, "myDsl_RestModelMethodConclusion", self)

    @property
    def myDsl_Resource(self):
        return self.__myDsl_Resource

    @myDsl_Resource.setter
    def myDsl_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource", None)
        self.__myDsl_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestAPI4"):
                opp_val = getattr(old_value, "myDsl_RestAPI4", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestAPI4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestAPI4"):
                opp_val = getattr(value, "myDsl_RestAPI4", None)
                setattr(value, "myDsl_RestAPI4", self)

    @property
    def myDsl_Resource52(self):
        return self.__myDsl_Resource52

    @myDsl_Resource52.setter
    def myDsl_Resource52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource52", None)
        self.__myDsl_Resource52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModel53"):
                opp_val = getattr(old_value, "myDsl_RestModel53", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModel53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModel53"):
                opp_val = getattr(value, "myDsl_RestModel53", None)
                setattr(value, "myDsl_RestModel53", self)

    @property
    def myDsl_Resource55(self):
        return self.__myDsl_Resource55

    @myDsl_Resource55.setter
    def myDsl_Resource55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource55", None)
        self.__myDsl_Resource55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ValidationService56"):
                opp_val = getattr(old_value, "myDsl_ValidationService56", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ValidationService56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ValidationService56"):
                opp_val = getattr(value, "myDsl_ValidationService56", None)
                setattr(value, "myDsl_ValidationService56", self)

    @property
    def myDsl_Resource58(self):
        return self.__myDsl_Resource58

    @myDsl_Resource58.setter
    def myDsl_Resource58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource58", None)
        self.__myDsl_Resource58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Block59"):
                opp_val = getattr(old_value, "myDsl_Block59", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Block59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Block59"):
                opp_val = getattr(value, "myDsl_Block59", None)
                setattr(value, "myDsl_Block59", self)

    @property
    def myDsl_Resource37(self):
        return self.__myDsl_Resource37

    @myDsl_Resource37.setter
    def myDsl_Resource37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource37", None)
        self.__myDsl_Resource37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestModel38"):
                opp_val = getattr(old_value, "myDsl_RestModel38", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestModel38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestModel38"):
                opp_val = getattr(value, "myDsl_RestModel38", None)
                setattr(value, "myDsl_RestModel38", self)

    @property
    def myDsl_Resource34(self):
        return self.__myDsl_Resource34

    @myDsl_Resource34.setter
    def myDsl_Resource34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource34", None)
        self.__myDsl_Resource34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ExceptionMapper35"):
                opp_val = getattr(old_value, "myDsl_ExceptionMapper35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ExceptionMapper35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ExceptionMapper35"):
                opp_val = getattr(value, "myDsl_ExceptionMapper35", None)
                setattr(value, "myDsl_ExceptionMapper35", self)

    @property
    def myDsl_Resource67(self):
        return self.__myDsl_Resource67

    @myDsl_Resource67.setter
    def myDsl_Resource67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Resource__myDsl_Resource67", None)
        self.__myDsl_Resource67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_RestExceptionList"):
                opp_val = getattr(old_value, "myDsl_RestExceptionList", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_RestExceptionList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_RestExceptionList"):
                opp_val = getattr(value, "myDsl_RestExceptionList", None)
                setattr(value, "myDsl_RestExceptionList", self)

class myDsl_RestAPI:

    pass
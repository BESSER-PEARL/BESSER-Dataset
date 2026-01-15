from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Java_Annotation:

    def __init__(self, sentenceText: str, type: str):
        self.sentenceText = sentenceText
        self.type = type
        
    @property
    def sentenceText(self) -> str:
        return self.__sentenceText

    @sentenceText.setter
    def sentenceText(self, sentenceText: str):
        self.__sentenceText = sentenceText

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Java_Statement(ABC):

    pass
class Java_Parameter:

    def __init__(self, defaultValue: str, name: str, Java_Parameter: "Type" = None):
        self.defaultValue = defaultValue
        self.name = name
        self.Java_Parameter = Java_Parameter
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Java_Parameter(self):
        return self.__Java_Parameter

    @Java_Parameter.setter
    def Java_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Parameter__Java_Parameter", None)
        self.__Java_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type23"):
                opp_val = getattr(old_value, "Type23", None)
                if opp_val == self:
                    setattr(old_value, "Type23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type23"):
                opp_val = getattr(value, "Type23", None)
                setattr(value, "Type23", self)

class Annotation:

    pass
class Statement:

    pass
class Java_VariableDeclaration(Statement):

    def __init__(self, variableName: str, Java_VariableDeclaration: "Type" = None, Statement: "Java_Method"):
        self.variableName = variableName
        self.Java_VariableDeclaration = Java_VariableDeclaration
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def Java_VariableDeclaration(self):
        return self.__Java_VariableDeclaration

    @Java_VariableDeclaration.setter
    def Java_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_VariableDeclaration__Java_VariableDeclaration", None)
        self.__Java_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type30"):
                opp_val = getattr(old_value, "Type30", None)
                if opp_val == self:
                    setattr(old_value, "Type30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type30"):
                opp_val = getattr(value, "Type30", None)
                setattr(value, "Type30", self)

class Java_MethodCall(Statement):

    def __init__(self, methodName: str, variableName: str, Statement: "Java_Method"):
        self.methodName = methodName
        self.variableName = variableName
        
    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class Java_Assignment(Statement):

    def __init__(self, objectId: str, fieldName: str, variableExpr: str, Statement: "Java_Method"):
        self.objectId = objectId
        self.fieldName = fieldName
        self.variableExpr = variableExpr
        
    @property
    def objectId(self) -> str:
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId

    @property
    def variableExpr(self) -> str:
        return self.__variableExpr

    @variableExpr.setter
    def variableExpr(self, variableExpr: str):
        self.__variableExpr = variableExpr

    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

class Java_Return(Statement):

    def __init__(self, objectId: str, fieldName: str, Statement: "Java_Method"):
        self.objectId = objectId
        self.fieldName = fieldName
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def objectId(self) -> str:
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId

class Parameter:

    pass
class Java_Field:

    def __init__(self, name: str, isPublic: bool, isProtected: bool, isPrivate: bool, isStatic: bool, Java_Field: "Type" = None, 027: "Class" = None):
        self.name = name
        self.isPublic = isPublic
        self.isProtected = isProtected
        self.isPrivate = isPrivate
        self.isStatic = isStatic
        self.Java_Field = Java_Field
        self.027 = 027
        
    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def isPrivate(self) -> bool:
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def isProtected(self) -> bool:
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: bool):
        self.__isProtected = isProtected

    @property
    def 027(self):
        return self.__027

    @027.setter
    def 027(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Field__027", None)
        self.__027 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#28"):
                opp_val = getattr(old_value, "#28", None)
                if opp_val == self:
                    setattr(old_value, "#28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#28"):
                opp_val = getattr(value, "#28", None)
                setattr(value, "#28", self)

    @property
    def Java_Field(self):
        return self.__Java_Field

    @Java_Field.setter
    def Java_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Field__Java_Field", None)
        self.__Java_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type25"):
                opp_val = getattr(old_value, "Type25", None)
                if opp_val == self:
                    setattr(old_value, "Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type25"):
                opp_val = getattr(value, "Type25", None)
                setattr(value, "Type25", self)

class Method:

    pass
class Field:

    pass
class Class:

    pass
class Interface:

    pass
class Java_MethodSignature:

    def __init__(self, name: str, isPublic: bool, isProtected: bool, isPrivate: bool, isStatic: bool, Java_MethodSignature: "Type" = None, Java_MethodSignature18: set["Parameter"] = None):
        self.name = name
        self.isPublic = isPublic
        self.isProtected = isProtected
        self.isPrivate = isPrivate
        self.isStatic = isStatic
        self.Java_MethodSignature = Java_MethodSignature
        self.Java_MethodSignature18 = Java_MethodSignature18 if Java_MethodSignature18 is not None else set()
        
    @property
    def isPrivate(self) -> bool:
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate

    @property
    def isProtected(self) -> bool:
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: bool):
        self.__isProtected = isProtected

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Java_MethodSignature(self):
        return self.__Java_MethodSignature

    @Java_MethodSignature.setter
    def Java_MethodSignature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodSignature__Java_MethodSignature", None)
        self.__Java_MethodSignature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

    @property
    def Java_MethodSignature18(self):
        return self.__Java_MethodSignature18

    @Java_MethodSignature18.setter
    def Java_MethodSignature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodSignature__Java_MethodSignature18", None)
        self.__Java_MethodSignature18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class MethodSignature:

    pass
class Java_Method(MethodSignature):

    pass
class Java_Type(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ObjectType:

    pass
class Java_Interface(ObjectType):

    pass
class Java_Class(ObjectType):

    def __init__(self, isPublic: bool, isStatic: bool, Java_Class: set["Interface"] = None, Java_Class6: "Class" = None, 08: set["Field"] = None, Java_Class11: set["Method"] = None, #: "Java_Package"):
        self.isPublic = isPublic
        self.isStatic = isStatic
        self.Java_Class = Java_Class if Java_Class is not None else set()
        self.Java_Class6 = Java_Class6
        self.08 = 08 if 08 is not None else set()
        self.Java_Class11 = Java_Class11 if Java_Class11 is not None else set()
        
    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def 08(self):
        return self.__08

    @08.setter
    def 08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__08", None)
        self.__08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    if opp_val == self:
                        setattr(item, "#9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#9"):
                    opp_val = getattr(item, "#9", None)
                    
                    setattr(item, "#9", self)
                    

    @property
    def Java_Class11(self):
        return self.__Java_Class11

    @Java_Class11.setter
    def Java_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__Java_Class11", None)
        self.__Java_Class11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def Java_Class(self):
        return self.__Java_Class

    @Java_Class.setter
    def Java_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__Java_Class", None)
        self.__Java_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    setattr(item, "Interface", self)
                    

    @property
    def Java_Class6(self):
        return self.__Java_Class6

    @Java_Class6.setter
    def Java_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__Java_Class6", None)
        self.__Java_Class6 = value
        
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

class Java_Package:

    def __init__(self, name: str, 0: set["ObjectType"] = None):
        self.name = name
        self.0 = 0 if 0 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Package__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class Package:

    pass
class Type:

    pass
class Java_ObjectType(Type):

    pass
class Java_VoidType(Type):

    pass
class Java_PrimitiveType(Type):

    pass
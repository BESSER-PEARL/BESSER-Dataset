from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Java_Statement(ABC):

    pass
class Java_Annotation:

    def __init__(self, sentenceText: str, type: str):
        self.sentenceText = sentenceText
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def sentenceText(self):
        return self.__sentenceText

    @sentenceText.setter
    def sentenceText(self, sentenceText: str):
        self.__sentenceText = sentenceText


class Class:

    pass
class Interface:

    pass
class Package:

    pass
class Type:

    pass
class Java_ObjectType(Type):

    pass
class Java_PrimitiveType(Type):

    pass
class Java_VoidType(Type):

    pass
class Java_Field:

    def __init__(self, name: str, isPublic: bool, isProtected: bool, isPrivate: bool, isStatic: bool, Java_Field: "Type" = None, field: "Class" = None):
        self.name = name
        self.isPublic = isPublic
        self.isProtected = isProtected
        self.isPrivate = isPrivate
        self.isStatic = isStatic
        self.Java_Field = Java_Field
        self.field = field
        
        pass
    @property
    def isProtected(self):
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: bool):
        self.__isProtected = isProtected


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic


    @property
    def isPrivate(self):
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate


    @property
    def isPublic(self):
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Field__field", None)
        self.__field = value
        
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
    def Java_Field(self):
        return self.__Java_Field

    @Java_Field.setter
    def Java_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Field__Java_Field", None)
        self.__Java_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type22"):
                opp_val = getattr(old_value, "Type22", None)
                if opp_val == self:
                    setattr(old_value, "Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type22"):
                opp_val = getattr(value, "Type22", None)
                setattr(value, "Type22", self)

class Java_Parameter:

    def __init__(self, name: str, defaultValue: str, Java_Parameter: "Type" = None):
        self.name = name
        self.defaultValue = defaultValue
        self.Java_Parameter = Java_Parameter
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def name(self):
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
            if hasattr(old_value, "Type20"):
                opp_val = getattr(old_value, "Type20", None)
                if opp_val == self:
                    setattr(old_value, "Type20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type20"):
                opp_val = getattr(value, "Type20", None)
                setattr(value, "Type20", self)

class Annotation:

    pass
class Statement:

    pass
class Java_VariableDeclaration(Statement):

    def __init__(self, variableName: str, Java_VariableDeclaration: "Type" = None, Statement: "Java_Method" = None):
        self.variableName = variableName
        self.Java_VariableDeclaration = Java_VariableDeclaration
        
        pass
    @property
    def variableName(self):
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
            if hasattr(old_value, "Type26"):
                opp_val = getattr(old_value, "Type26", None)
                if opp_val == self:
                    setattr(old_value, "Type26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type26"):
                opp_val = getattr(value, "Type26", None)
                setattr(value, "Type26", self)

class Java_MethodCall(Statement):

    def __init__(self, variableName: str, methodName: str, Statement: "Java_Method" = None):
        self.variableName = variableName
        self.methodName = methodName
        
        pass
    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def variableName(self):
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName


class Java_Assignment(Statement):

    def __init__(self, objectId: str, fieldName: str, variableExpr: str, Statement: "Java_Method" = None):
        self.objectId = objectId
        self.fieldName = fieldName
        self.variableExpr = variableExpr
        
        pass
    @property
    def objectId(self):
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId


    @property
    def variableExpr(self):
        return self.__variableExpr

    @variableExpr.setter
    def variableExpr(self, variableExpr: str):
        self.__variableExpr = variableExpr


    @property
    def fieldName(self):
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName


class Java_Return(Statement):

    def __init__(self, objectId: str, fieldName: str, Statement: "Java_Method" = None):
        self.objectId = objectId
        self.fieldName = fieldName
        
        pass
    @property
    def objectId(self):
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId


    @property
    def fieldName(self):
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName


class Parameter:

    pass
class Java_MethodSignature:

    def __init__(self, name: str, isPublic: bool, isProtected: bool, isPrivate: bool, isStatic: bool, Java_MethodSignature: "Type" = None, Java_MethodSignature15: set["Parameter"] = None):
        self.name = name
        self.isPublic = isPublic
        self.isProtected = isProtected
        self.isPrivate = isPrivate
        self.isStatic = isStatic
        self.Java_MethodSignature = Java_MethodSignature
        self.Java_MethodSignature15 = Java_MethodSignature15 if Java_MethodSignature15 is not None else set()
        
        pass
    @property
    def isProtected(self):
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: bool):
        self.__isProtected = isProtected


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isPublic(self):
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic


    @property
    def isPrivate(self):
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic


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
    def Java_MethodSignature15(self):
        return self.__Java_MethodSignature15

    @Java_MethodSignature15.setter
    def Java_MethodSignature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_MethodSignature__Java_MethodSignature15", None)
        self.__Java_MethodSignature15 = value if value is not None else set()
        
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
class Method:

    pass
class Field:

    pass
class Java_Type(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ObjectType:

    pass
class Java_Class(ObjectType):

    def __init__(self, isPublic: bool, isStatic: bool, Java_Class4: "Class" = None, owner6: set["Field"] = None, Java_Class8: set["Method"] = None, Java_Class: set["Interface"] = None, ObjectType: "Java_Package" = None):
        self.isPublic = isPublic
        self.isStatic = isStatic
        self.Java_Class4 = Java_Class4
        self.owner6 = owner6 if owner6 is not None else set()
        self.Java_Class8 = Java_Class8 if Java_Class8 is not None else set()
        self.Java_Class = Java_Class if Java_Class is not None else set()
        
        pass
    @property
    def isPublic(self):
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic


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
    def owner6(self):
        return self.__owner6

    @owner6.setter
    def owner6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__owner6", None)
        self.__owner6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    if opp_val == self:
                        setattr(item, "Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    setattr(item, "Field", self)
                    

    @property
    def Java_Class8(self):
        return self.__Java_Class8

    @Java_Class8.setter
    def Java_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__Java_Class8", None)
        self.__Java_Class8 = value if value is not None else set()
        
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
    def Java_Class4(self):
        return self.__Java_Class4

    @Java_Class4.setter
    def Java_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Class__Java_Class4", None)
        self.__Java_Class4 = value
        
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

class Java_Interface(ObjectType):

    pass
class Java_Package:

    def __init__(self, name: str, owner: set["ObjectType"] = None):
        self.name = name
        self.owner = owner if owner is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java_Package__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectType"):
                    opp_val = getattr(item, "ObjectType", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectType"):
                    opp_val = getattr(item, "ObjectType", None)
                    
                    setattr(item, "ObjectType", self)
                    

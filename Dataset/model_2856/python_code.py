from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ConstantExpression:

    pass
class simplejava_StringExpression(ConstantExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class simplejava_IntegerExpression(ConstantExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class simplejava_BooleanExpression(ConstantExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class simplejava_NullExpression(ConstantExpression):

    pass
class GenericExpression:

    pass
class simplejava_ConstantExpression(GenericExpression):

    pass
class simplejava_VariableExpression(GenericExpression):

    pass
class simplejava_UnaryExpression(GenericExpression):

    def __init__(self, type: str, simplejava_UnaryExpression: "simplejava_GenericExpression" = None):
        self.type = type
        self.simplejava_UnaryExpression = simplejava_UnaryExpression
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simplejava_UnaryExpression(self):
        return self.__simplejava_UnaryExpression

    @simplejava_UnaryExpression.setter
    def simplejava_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_UnaryExpression__simplejava_UnaryExpression", None)
        self.__simplejava_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_GenericExpression74"):
                opp_val = getattr(old_value, "simplejava_GenericExpression74", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression74"):
                opp_val = getattr(value, "simplejava_GenericExpression74", None)
                setattr(value, "simplejava_GenericExpression74", self)

class simplejava_ParanthesisOrBinaryExpression(GenericExpression):

    def __init__(self, type: str, simplejava_ParanthesisOrBinaryExpression: "simplejava_IfStatement" = None, simplejava_ParanthesisOrBinaryExpression59: "simplejava_WhileStatement" = None, simplejava_ParanthesisOrBinaryExpression78: "simplejava_GenericExpression" = None, simplejava_ParanthesisOrBinaryExpression81: "simplejava_GenericExpression" = None):
        self.type = type
        self.simplejava_ParanthesisOrBinaryExpression = simplejava_ParanthesisOrBinaryExpression
        self.simplejava_ParanthesisOrBinaryExpression59 = simplejava_ParanthesisOrBinaryExpression59
        self.simplejava_ParanthesisOrBinaryExpression78 = simplejava_ParanthesisOrBinaryExpression78
        self.simplejava_ParanthesisOrBinaryExpression81 = simplejava_ParanthesisOrBinaryExpression81
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simplejava_ParanthesisOrBinaryExpression59(self):
        return self.__simplejava_ParanthesisOrBinaryExpression59

    @simplejava_ParanthesisOrBinaryExpression59.setter
    def simplejava_ParanthesisOrBinaryExpression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression59", None)
        self.__simplejava_ParanthesisOrBinaryExpression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_WhileStatement"):
                opp_val = getattr(old_value, "simplejava_WhileStatement", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_WhileStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_WhileStatement"):
                opp_val = getattr(value, "simplejava_WhileStatement", None)
                setattr(value, "simplejava_WhileStatement", self)

    @property
    def simplejava_ParanthesisOrBinaryExpression78(self):
        return self.__simplejava_ParanthesisOrBinaryExpression78

    @simplejava_ParanthesisOrBinaryExpression78.setter
    def simplejava_ParanthesisOrBinaryExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression78", None)
        self.__simplejava_ParanthesisOrBinaryExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_GenericExpression79"):
                opp_val = getattr(old_value, "simplejava_GenericExpression79", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression79"):
                opp_val = getattr(value, "simplejava_GenericExpression79", None)
                setattr(value, "simplejava_GenericExpression79", self)

    @property
    def simplejava_ParanthesisOrBinaryExpression(self):
        return self.__simplejava_ParanthesisOrBinaryExpression

    @simplejava_ParanthesisOrBinaryExpression.setter
    def simplejava_ParanthesisOrBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression", None)
        self.__simplejava_ParanthesisOrBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_IfStatement"):
                opp_val = getattr(old_value, "simplejava_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_IfStatement"):
                opp_val = getattr(value, "simplejava_IfStatement", None)
                setattr(value, "simplejava_IfStatement", self)

    @property
    def simplejava_ParanthesisOrBinaryExpression81(self):
        return self.__simplejava_ParanthesisOrBinaryExpression81

    @simplejava_ParanthesisOrBinaryExpression81.setter
    def simplejava_ParanthesisOrBinaryExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression81", None)
        self.__simplejava_ParanthesisOrBinaryExpression81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_GenericExpression82"):
                opp_val = getattr(old_value, "simplejava_GenericExpression82", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression82"):
                opp_val = getattr(value, "simplejava_GenericExpression82", None)
                setattr(value, "simplejava_GenericExpression82", self)

class simplejava_GenericExpression:

    pass
class SimpleVariableDeclaration:

    pass
class SimpleStatement:

    pass
class simplejava_SimpleVariableDeclaration(SimpleStatement):

    pass
class simplejava_SimpleStatement:

    pass
class simplejava_Statement:

    pass
class Statement:

    pass
class simplejava_MethodBlock(Statement):

    def __init__(self, generated: bool, simplejava_MethodBlock23: set["simplejava_Statement"] = None, simplejava_MethodBlock: "simplejava_Method" = None, simplejava_MethodBlock36: "simplejava_IfStatement" = None, simplejava_MethodBlock39: "simplejava_IfStatement" = None):
        self.generated = generated
        self.simplejava_MethodBlock23 = simplejava_MethodBlock23 if simplejava_MethodBlock23 is not None else set()
        self.simplejava_MethodBlock = simplejava_MethodBlock
        self.simplejava_MethodBlock36 = simplejava_MethodBlock36
        self.simplejava_MethodBlock39 = simplejava_MethodBlock39
        
    @property
    def generated(self) -> bool:
        return self.__generated

    @generated.setter
    def generated(self, generated: bool):
        self.__generated = generated

    @property
    def simplejava_MethodBlock23(self):
        return self.__simplejava_MethodBlock23

    @simplejava_MethodBlock23.setter
    def simplejava_MethodBlock23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock23", None)
        self.__simplejava_MethodBlock23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_Statement"):
                    opp_val = getattr(item, "simplejava_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_Statement"):
                    opp_val = getattr(item, "simplejava_Statement", None)
                    
                    setattr(item, "simplejava_Statement", self)
                    

    @property
    def simplejava_MethodBlock39(self):
        return self.__simplejava_MethodBlock39

    @simplejava_MethodBlock39.setter
    def simplejava_MethodBlock39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock39", None)
        self.__simplejava_MethodBlock39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_IfStatement38"):
                opp_val = getattr(old_value, "simplejava_IfStatement38", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_IfStatement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_IfStatement38"):
                opp_val = getattr(value, "simplejava_IfStatement38", None)
                setattr(value, "simplejava_IfStatement38", self)

    @property
    def simplejava_MethodBlock(self):
        return self.__simplejava_MethodBlock

    @simplejava_MethodBlock.setter
    def simplejava_MethodBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock", None)
        self.__simplejava_MethodBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method21"):
                opp_val = getattr(old_value, "simplejava_Method21", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Method21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method21"):
                opp_val = getattr(value, "simplejava_Method21", None)
                setattr(value, "simplejava_Method21", self)

    @property
    def simplejava_MethodBlock36(self):
        return self.__simplejava_MethodBlock36

    @simplejava_MethodBlock36.setter
    def simplejava_MethodBlock36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock36", None)
        self.__simplejava_MethodBlock36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_IfStatement35"):
                opp_val = getattr(old_value, "simplejava_IfStatement35", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_IfStatement35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_IfStatement35"):
                opp_val = getattr(value, "simplejava_IfStatement35", None)
                setattr(value, "simplejava_IfStatement35", self)

class simplejava_WhileStatement(Statement):

    pass
class simplejava_MethodCall(Statement, GenericExpression):

    def __init__(self, thisObject: bool, methodName: str, simplejava_MethodCall: "simplejava_Parameter" = None, simplejava_MethodCall68: "simplejava_Method" = None, simplejava_MethodCall71: set["simplejava_GenericExpression"] = None):
        self.thisObject = thisObject
        self.methodName = methodName
        self.simplejava_MethodCall = simplejava_MethodCall
        self.simplejava_MethodCall68 = simplejava_MethodCall68
        self.simplejava_MethodCall71 = simplejava_MethodCall71 if simplejava_MethodCall71 is not None else set()
        
    @property
    def thisObject(self) -> bool:
        return self.__thisObject

    @thisObject.setter
    def thisObject(self, thisObject: bool):
        self.__thisObject = thisObject

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def simplejava_MethodCall(self):
        return self.__simplejava_MethodCall

    @simplejava_MethodCall.setter
    def simplejava_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodCall__simplejava_MethodCall", None)
        self.__simplejava_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Parameter66"):
                opp_val = getattr(old_value, "simplejava_Parameter66", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Parameter66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Parameter66"):
                opp_val = getattr(value, "simplejava_Parameter66", None)
                setattr(value, "simplejava_Parameter66", self)

    @property
    def simplejava_MethodCall71(self):
        return self.__simplejava_MethodCall71

    @simplejava_MethodCall71.setter
    def simplejava_MethodCall71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodCall__simplejava_MethodCall71", None)
        self.__simplejava_MethodCall71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_GenericExpression72"):
                    opp_val = getattr(item, "simplejava_GenericExpression72", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_GenericExpression72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_GenericExpression72"):
                    opp_val = getattr(item, "simplejava_GenericExpression72", None)
                    
                    setattr(item, "simplejava_GenericExpression72", self)
                    

    @property
    def simplejava_MethodCall68(self):
        return self.__simplejava_MethodCall68

    @simplejava_MethodCall68.setter
    def simplejava_MethodCall68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodCall__simplejava_MethodCall68", None)
        self.__simplejava_MethodCall68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method69"):
                opp_val = getattr(old_value, "simplejava_Method69", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Method69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method69"):
                opp_val = getattr(value, "simplejava_Method69", None)
                setattr(value, "simplejava_Method69", self)

class simplejava_ForInStatement(Statement):

    pass
class simplejava_ReturnStatement(Statement):

    pass
class simplejava_ForStatement(Statement):

    pass
class simplejava_Assignment(SimpleStatement, Statement):

    pass
class simplejava_IfStatement(Statement):

    pass
class simplejava_VariableDeclaration(SimpleVariableDeclaration, Statement):

    pass
class simplejava_ClassDeclaration:

    def __init__(self, name: str, simplejava_ClassDeclaration6: set["simplejava_Parameter"] = None, simplejava_ClassDeclaration8: set["simplejava_Method"] = None, simplejava_ClassDeclaration: "simplejava_SimpleJava" = None, simplejava_ClassDeclaration13: "simplejava_Type" = None):
        self.name = name
        self.simplejava_ClassDeclaration6 = simplejava_ClassDeclaration6 if simplejava_ClassDeclaration6 is not None else set()
        self.simplejava_ClassDeclaration8 = simplejava_ClassDeclaration8 if simplejava_ClassDeclaration8 is not None else set()
        self.simplejava_ClassDeclaration = simplejava_ClassDeclaration
        self.simplejava_ClassDeclaration13 = simplejava_ClassDeclaration13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplejava_ClassDeclaration13(self):
        return self.__simplejava_ClassDeclaration13

    @simplejava_ClassDeclaration13.setter
    def simplejava_ClassDeclaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ClassDeclaration__simplejava_ClassDeclaration13", None)
        self.__simplejava_ClassDeclaration13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Type12"):
                opp_val = getattr(old_value, "simplejava_Type12", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Type12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Type12"):
                opp_val = getattr(value, "simplejava_Type12", None)
                setattr(value, "simplejava_Type12", self)

    @property
    def simplejava_ClassDeclaration8(self):
        return self.__simplejava_ClassDeclaration8

    @simplejava_ClassDeclaration8.setter
    def simplejava_ClassDeclaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ClassDeclaration__simplejava_ClassDeclaration8", None)
        self.__simplejava_ClassDeclaration8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_Method"):
                    opp_val = getattr(item, "simplejava_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_Method"):
                    opp_val = getattr(item, "simplejava_Method", None)
                    
                    setattr(item, "simplejava_Method", self)
                    

    @property
    def simplejava_ClassDeclaration(self):
        return self.__simplejava_ClassDeclaration

    @simplejava_ClassDeclaration.setter
    def simplejava_ClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ClassDeclaration__simplejava_ClassDeclaration", None)
        self.__simplejava_ClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_SimpleJava4"):
                opp_val = getattr(old_value, "simplejava_SimpleJava4", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_SimpleJava4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_SimpleJava4"):
                opp_val = getattr(value, "simplejava_SimpleJava4", None)
                setattr(value, "simplejava_SimpleJava4", self)

    @property
    def simplejava_ClassDeclaration6(self):
        return self.__simplejava_ClassDeclaration6

    @simplejava_ClassDeclaration6.setter
    def simplejava_ClassDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ClassDeclaration__simplejava_ClassDeclaration6", None)
        self.__simplejava_ClassDeclaration6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_Parameter"):
                    opp_val = getattr(item, "simplejava_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_Parameter"):
                    opp_val = getattr(item, "simplejava_Parameter", None)
                    
                    setattr(item, "simplejava_Parameter", self)
                    

class simplejava_Import:

    def __init__(self, imported: str, simplejava_Import: "simplejava_SimpleJava" = None):
        self.imported = imported
        self.simplejava_Import = simplejava_Import
        
    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported: str):
        self.__imported = imported

    @property
    def simplejava_Import(self):
        return self.__simplejava_Import

    @simplejava_Import.setter
    def simplejava_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Import__simplejava_Import", None)
        self.__simplejava_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_SimpleJava2"):
                opp_val = getattr(old_value, "simplejava_SimpleJava2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_SimpleJava2"):
                opp_val = getattr(value, "simplejava_SimpleJava2", None)
                if opp_val is None:
                    setattr(value, "simplejava_SimpleJava2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplejava_PackageDeclaration:

    def __init__(self, name: str, simplejava_PackageDeclaration: "simplejava_SimpleJava" = None):
        self.name = name
        self.simplejava_PackageDeclaration = simplejava_PackageDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplejava_PackageDeclaration(self):
        return self.__simplejava_PackageDeclaration

    @simplejava_PackageDeclaration.setter
    def simplejava_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_PackageDeclaration__simplejava_PackageDeclaration", None)
        self.__simplejava_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_SimpleJava"):
                opp_val = getattr(old_value, "simplejava_SimpleJava", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_SimpleJava", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_SimpleJava"):
                opp_val = getattr(value, "simplejava_SimpleJava", None)
                setattr(value, "simplejava_SimpleJava", self)

class simplejava_SimpleJava:

    pass
class simplejava_Type:

    def __init__(self, typeName: str, simplejava_Type: "simplejava_Parameter" = None, simplejava_Type12: "simplejava_ClassDeclaration" = None, simplejava_Type16: "simplejava_Method" = None):
        self.typeName = typeName
        self.simplejava_Type = simplejava_Type
        self.simplejava_Type12 = simplejava_Type12
        self.simplejava_Type16 = simplejava_Type16
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def simplejava_Type(self):
        return self.__simplejava_Type

    @simplejava_Type.setter
    def simplejava_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type", None)
        self.__simplejava_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Parameter10"):
                opp_val = getattr(old_value, "simplejava_Parameter10", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Parameter10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Parameter10"):
                opp_val = getattr(value, "simplejava_Parameter10", None)
                setattr(value, "simplejava_Parameter10", self)

    @property
    def simplejava_Type12(self):
        return self.__simplejava_Type12

    @simplejava_Type12.setter
    def simplejava_Type12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type12", None)
        self.__simplejava_Type12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ClassDeclaration13"):
                opp_val = getattr(old_value, "simplejava_ClassDeclaration13", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_ClassDeclaration13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ClassDeclaration13"):
                opp_val = getattr(value, "simplejava_ClassDeclaration13", None)
                setattr(value, "simplejava_ClassDeclaration13", self)

    @property
    def simplejava_Type16(self):
        return self.__simplejava_Type16

    @simplejava_Type16.setter
    def simplejava_Type16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type16", None)
        self.__simplejava_Type16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method15"):
                opp_val = getattr(old_value, "simplejava_Method15", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Method15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method15"):
                opp_val = getattr(value, "simplejava_Method15", None)
                setattr(value, "simplejava_Method15", self)

class simplejava_Method:

    def __init__(self, static: bool, name: str, simplejava_Method: "simplejava_ClassDeclaration" = None, simplejava_Method15: "simplejava_Type" = None, simplejava_Method18: set["simplejava_Parameter"] = None, simplejava_Method21: "simplejava_MethodBlock" = None, simplejava_Method69: "simplejava_MethodCall" = None):
        self.static = static
        self.name = name
        self.simplejava_Method = simplejava_Method
        self.simplejava_Method15 = simplejava_Method15
        self.simplejava_Method18 = simplejava_Method18 if simplejava_Method18 is not None else set()
        self.simplejava_Method21 = simplejava_Method21
        self.simplejava_Method69 = simplejava_Method69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def simplejava_Method(self):
        return self.__simplejava_Method

    @simplejava_Method.setter
    def simplejava_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method", None)
        self.__simplejava_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ClassDeclaration8"):
                opp_val = getattr(old_value, "simplejava_ClassDeclaration8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ClassDeclaration8"):
                opp_val = getattr(value, "simplejava_ClassDeclaration8", None)
                if opp_val is None:
                    setattr(value, "simplejava_ClassDeclaration8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplejava_Method18(self):
        return self.__simplejava_Method18

    @simplejava_Method18.setter
    def simplejava_Method18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method18", None)
        self.__simplejava_Method18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_Parameter19"):
                    opp_val = getattr(item, "simplejava_Parameter19", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_Parameter19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_Parameter19"):
                    opp_val = getattr(item, "simplejava_Parameter19", None)
                    
                    setattr(item, "simplejava_Parameter19", self)
                    

    @property
    def simplejava_Method15(self):
        return self.__simplejava_Method15

    @simplejava_Method15.setter
    def simplejava_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method15", None)
        self.__simplejava_Method15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Type16"):
                opp_val = getattr(old_value, "simplejava_Type16", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Type16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Type16"):
                opp_val = getattr(value, "simplejava_Type16", None)
                setattr(value, "simplejava_Type16", self)

    @property
    def simplejava_Method69(self):
        return self.__simplejava_Method69

    @simplejava_Method69.setter
    def simplejava_Method69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method69", None)
        self.__simplejava_Method69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_MethodCall68"):
                opp_val = getattr(old_value, "simplejava_MethodCall68", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_MethodCall68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_MethodCall68"):
                opp_val = getattr(value, "simplejava_MethodCall68", None)
                setattr(value, "simplejava_MethodCall68", self)

    @property
    def simplejava_Method21(self):
        return self.__simplejava_Method21

    @simplejava_Method21.setter
    def simplejava_Method21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method21", None)
        self.__simplejava_Method21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_MethodBlock"):
                opp_val = getattr(old_value, "simplejava_MethodBlock", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_MethodBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_MethodBlock"):
                opp_val = getattr(value, "simplejava_MethodBlock", None)
                setattr(value, "simplejava_MethodBlock", self)

class simplejava_Parameter:

    def __init__(self, name: str, simplejava_Parameter: "simplejava_ClassDeclaration" = None, simplejava_Parameter10: "simplejava_Type" = None, simplejava_Parameter25: "simplejava_VariableDeclaration" = None, simplejava_Parameter19: "simplejava_Method" = None, simplejava_Parameter51: "simplejava_ForInStatement" = None, simplejava_Parameter29: "simplejava_Assignment" = None, simplejava_Parameter66: "simplejava_MethodCall" = None, simplejava_Parameter76: "simplejava_VariableExpression" = None):
        self.name = name
        self.simplejava_Parameter = simplejava_Parameter
        self.simplejava_Parameter10 = simplejava_Parameter10
        self.simplejava_Parameter25 = simplejava_Parameter25
        self.simplejava_Parameter19 = simplejava_Parameter19
        self.simplejava_Parameter51 = simplejava_Parameter51
        self.simplejava_Parameter29 = simplejava_Parameter29
        self.simplejava_Parameter66 = simplejava_Parameter66
        self.simplejava_Parameter76 = simplejava_Parameter76
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplejava_Parameter29(self):
        return self.__simplejava_Parameter29

    @simplejava_Parameter29.setter
    def simplejava_Parameter29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter29", None)
        self.__simplejava_Parameter29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Assignment"):
                opp_val = getattr(old_value, "simplejava_Assignment", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Assignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Assignment"):
                opp_val = getattr(value, "simplejava_Assignment", None)
                setattr(value, "simplejava_Assignment", self)

    @property
    def simplejava_Parameter76(self):
        return self.__simplejava_Parameter76

    @simplejava_Parameter76.setter
    def simplejava_Parameter76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter76", None)
        self.__simplejava_Parameter76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_VariableExpression"):
                opp_val = getattr(old_value, "simplejava_VariableExpression", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_VariableExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_VariableExpression"):
                opp_val = getattr(value, "simplejava_VariableExpression", None)
                setattr(value, "simplejava_VariableExpression", self)

    @property
    def simplejava_Parameter25(self):
        return self.__simplejava_Parameter25

    @simplejava_Parameter25.setter
    def simplejava_Parameter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter25", None)
        self.__simplejava_Parameter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_VariableDeclaration"):
                opp_val = getattr(old_value, "simplejava_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_VariableDeclaration"):
                opp_val = getattr(value, "simplejava_VariableDeclaration", None)
                setattr(value, "simplejava_VariableDeclaration", self)

    @property
    def simplejava_Parameter(self):
        return self.__simplejava_Parameter

    @simplejava_Parameter.setter
    def simplejava_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter", None)
        self.__simplejava_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ClassDeclaration6"):
                opp_val = getattr(old_value, "simplejava_ClassDeclaration6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ClassDeclaration6"):
                opp_val = getattr(value, "simplejava_ClassDeclaration6", None)
                if opp_val is None:
                    setattr(value, "simplejava_ClassDeclaration6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplejava_Parameter51(self):
        return self.__simplejava_Parameter51

    @simplejava_Parameter51.setter
    def simplejava_Parameter51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter51", None)
        self.__simplejava_Parameter51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ForInStatement"):
                opp_val = getattr(old_value, "simplejava_ForInStatement", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_ForInStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ForInStatement"):
                opp_val = getattr(value, "simplejava_ForInStatement", None)
                setattr(value, "simplejava_ForInStatement", self)

    @property
    def simplejava_Parameter66(self):
        return self.__simplejava_Parameter66

    @simplejava_Parameter66.setter
    def simplejava_Parameter66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter66", None)
        self.__simplejava_Parameter66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_MethodCall"):
                opp_val = getattr(old_value, "simplejava_MethodCall", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_MethodCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_MethodCall"):
                opp_val = getattr(value, "simplejava_MethodCall", None)
                setattr(value, "simplejava_MethodCall", self)

    @property
    def simplejava_Parameter19(self):
        return self.__simplejava_Parameter19

    @simplejava_Parameter19.setter
    def simplejava_Parameter19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter19", None)
        self.__simplejava_Parameter19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method18"):
                opp_val = getattr(old_value, "simplejava_Method18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method18"):
                opp_val = getattr(value, "simplejava_Method18", None)
                if opp_val is None:
                    setattr(value, "simplejava_Method18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplejava_Parameter10(self):
        return self.__simplejava_Parameter10

    @simplejava_Parameter10.setter
    def simplejava_Parameter10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter10", None)
        self.__simplejava_Parameter10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Type"):
                opp_val = getattr(old_value, "simplejava_Type", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Type"):
                opp_val = getattr(value, "simplejava_Type", None)
                setattr(value, "simplejava_Type", self)

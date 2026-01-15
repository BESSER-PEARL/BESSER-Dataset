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
class simplejava_VariableExpression(GenericExpression):

    pass
class simplejava_ConstantExpression(GenericExpression):

    pass
class simplejava_ParanthesisOrBinaryExpression(GenericExpression):

    def __init__(self, type: str, simplejava_ParanthesisOrBinaryExpression60: "simplejava_WhileStatement" = None, simplejava_ParanthesisOrBinaryExpression: "simplejava_IfStatement" = None, simplejava_ParanthesisOrBinaryExpression83: "simplejava_GenericExpression" = None, simplejava_ParanthesisOrBinaryExpression86: "simplejava_GenericExpression" = None):
        self.type = type
        self.simplejava_ParanthesisOrBinaryExpression60 = simplejava_ParanthesisOrBinaryExpression60
        self.simplejava_ParanthesisOrBinaryExpression = simplejava_ParanthesisOrBinaryExpression
        self.simplejava_ParanthesisOrBinaryExpression83 = simplejava_ParanthesisOrBinaryExpression83
        self.simplejava_ParanthesisOrBinaryExpression86 = simplejava_ParanthesisOrBinaryExpression86
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simplejava_ParanthesisOrBinaryExpression86(self):
        return self.__simplejava_ParanthesisOrBinaryExpression86

    @simplejava_ParanthesisOrBinaryExpression86.setter
    def simplejava_ParanthesisOrBinaryExpression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression86", None)
        self.__simplejava_ParanthesisOrBinaryExpression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_GenericExpression87"):
                opp_val = getattr(old_value, "simplejava_GenericExpression87", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression87"):
                opp_val = getattr(value, "simplejava_GenericExpression87", None)
                setattr(value, "simplejava_GenericExpression87", self)

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
    def simplejava_ParanthesisOrBinaryExpression83(self):
        return self.__simplejava_ParanthesisOrBinaryExpression83

    @simplejava_ParanthesisOrBinaryExpression83.setter
    def simplejava_ParanthesisOrBinaryExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression83", None)
        self.__simplejava_ParanthesisOrBinaryExpression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_GenericExpression84"):
                opp_val = getattr(old_value, "simplejava_GenericExpression84", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression84"):
                opp_val = getattr(value, "simplejava_GenericExpression84", None)
                setattr(value, "simplejava_GenericExpression84", self)

    @property
    def simplejava_ParanthesisOrBinaryExpression60(self):
        return self.__simplejava_ParanthesisOrBinaryExpression60

    @simplejava_ParanthesisOrBinaryExpression60.setter
    def simplejava_ParanthesisOrBinaryExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ParanthesisOrBinaryExpression__simplejava_ParanthesisOrBinaryExpression60", None)
        self.__simplejava_ParanthesisOrBinaryExpression60 = value
        
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
            if hasattr(old_value, "simplejava_GenericExpression79"):
                opp_val = getattr(old_value, "simplejava_GenericExpression79", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_GenericExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_GenericExpression79"):
                opp_val = getattr(value, "simplejava_GenericExpression79", None)
                setattr(value, "simplejava_GenericExpression79", self)

class simplejava_ConstructorCall(GenericExpression):

    pass
class SimpleVariableDeclaration:

    pass
class SimpleStatement:

    pass
class simplejava_SimpleVariableDeclaration(SimpleStatement):

    pass
class simplejava_SimpleStatement:

    pass
class simplejava_GenericExpression:

    pass
class Parameter:

    pass
class simplejava_Attribute(Parameter):

    pass
class simplejava_SimpleParameter(Parameter):

    pass
class simplejava_Type:

    def __init__(self, typeName: str, isVoid: bool, simplejava_Type: "simplejava_Parameter" = None, simplejava_Type13: "simplejava_ClassDeclaration" = None, simplejava_Type17: "simplejava_Method" = None, simplejava_Type75: "simplejava_ConstructorCall" = None):
        self.typeName = typeName
        self.isVoid = isVoid
        self.simplejava_Type = simplejava_Type
        self.simplejava_Type13 = simplejava_Type13
        self.simplejava_Type17 = simplejava_Type17
        self.simplejava_Type75 = simplejava_Type75
        
    @property
    def isVoid(self) -> bool:
        return self.__isVoid

    @isVoid.setter
    def isVoid(self, isVoid: bool):
        self.__isVoid = isVoid

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def simplejava_Type17(self):
        return self.__simplejava_Type17

    @simplejava_Type17.setter
    def simplejava_Type17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type17", None)
        self.__simplejava_Type17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method16"):
                opp_val = getattr(old_value, "simplejava_Method16", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Method16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method16"):
                opp_val = getattr(value, "simplejava_Method16", None)
                setattr(value, "simplejava_Method16", self)

    @property
    def simplejava_Type13(self):
        return self.__simplejava_Type13

    @simplejava_Type13.setter
    def simplejava_Type13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type13", None)
        self.__simplejava_Type13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ClassDeclaration14"):
                opp_val = getattr(old_value, "simplejava_ClassDeclaration14", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_ClassDeclaration14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ClassDeclaration14"):
                opp_val = getattr(value, "simplejava_ClassDeclaration14", None)
                setattr(value, "simplejava_ClassDeclaration14", self)

    @property
    def simplejava_Type75(self):
        return self.__simplejava_Type75

    @simplejava_Type75.setter
    def simplejava_Type75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Type__simplejava_Type75", None)
        self.__simplejava_Type75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_ConstructorCall"):
                opp_val = getattr(old_value, "simplejava_ConstructorCall", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_ConstructorCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_ConstructorCall"):
                opp_val = getattr(value, "simplejava_ConstructorCall", None)
                setattr(value, "simplejava_ConstructorCall", self)

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

class simplejava_Method:

    def __init__(self, static: bool, name: str, simplejava_Method21: "simplejava_MethodBlock" = None, simplejava_Method: "simplejava_ClassDeclaration" = None, simplejava_Method16: "simplejava_Type" = None, simplejava_Method19: set["simplejava_SimpleParameter"] = None, simplejava_Method70: "simplejava_MethodCall" = None):
        self.static = static
        self.name = name
        self.simplejava_Method21 = simplejava_Method21
        self.simplejava_Method = simplejava_Method
        self.simplejava_Method16 = simplejava_Method16
        self.simplejava_Method19 = simplejava_Method19 if simplejava_Method19 is not None else set()
        self.simplejava_Method70 = simplejava_Method70
        
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

    @property
    def simplejava_Method16(self):
        return self.__simplejava_Method16

    @simplejava_Method16.setter
    def simplejava_Method16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method16", None)
        self.__simplejava_Method16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Type17"):
                opp_val = getattr(old_value, "simplejava_Type17", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Type17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Type17"):
                opp_val = getattr(value, "simplejava_Type17", None)
                setattr(value, "simplejava_Type17", self)

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
    def simplejava_Method70(self):
        return self.__simplejava_Method70

    @simplejava_Method70.setter
    def simplejava_Method70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method70", None)
        self.__simplejava_Method70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_MethodCall69"):
                opp_val = getattr(old_value, "simplejava_MethodCall69", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_MethodCall69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_MethodCall69"):
                opp_val = getattr(value, "simplejava_MethodCall69", None)
                setattr(value, "simplejava_MethodCall69", self)

    @property
    def simplejava_Method19(self):
        return self.__simplejava_Method19

    @simplejava_Method19.setter
    def simplejava_Method19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Method__simplejava_Method19", None)
        self.__simplejava_Method19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_SimpleParameter"):
                    opp_val = getattr(item, "simplejava_SimpleParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_SimpleParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_SimpleParameter"):
                    opp_val = getattr(item, "simplejava_SimpleParameter", None)
                    
                    setattr(item, "simplejava_SimpleParameter", self)
                    

class simplejava_Parameter:

    def __init__(self, name: str, simplejava_Parameter: "simplejava_ClassDeclaration" = None, simplejava_Parameter10: "simplejava_Type" = None, simplejava_Parameter67: "simplejava_MethodCall" = None, simplejava_Parameter30: "simplejava_Assignment" = None, simplejava_Parameter81: "simplejava_VariableExpression" = None):
        self.name = name
        self.simplejava_Parameter = simplejava_Parameter
        self.simplejava_Parameter10 = simplejava_Parameter10
        self.simplejava_Parameter67 = simplejava_Parameter67
        self.simplejava_Parameter30 = simplejava_Parameter30
        self.simplejava_Parameter81 = simplejava_Parameter81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplejava_Parameter67(self):
        return self.__simplejava_Parameter67

    @simplejava_Parameter67.setter
    def simplejava_Parameter67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter67", None)
        self.__simplejava_Parameter67 = value
        
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
    def simplejava_Parameter30(self):
        return self.__simplejava_Parameter30

    @simplejava_Parameter30.setter
    def simplejava_Parameter30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter30", None)
        self.__simplejava_Parameter30 = value
        
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
    def simplejava_Parameter81(self):
        return self.__simplejava_Parameter81

    @simplejava_Parameter81.setter
    def simplejava_Parameter81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_Parameter__simplejava_Parameter81", None)
        self.__simplejava_Parameter81 = value
        
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

class simplejava_ClassDeclaration:

    def __init__(self, name: str, simplejava_ClassDeclaration: "simplejava_SimpleJava" = None, simplejava_ClassDeclaration6: set["simplejava_Parameter"] = None, simplejava_ClassDeclaration8: set["simplejava_Method"] = None, simplejava_ClassDeclaration14: "simplejava_Type" = None):
        self.name = name
        self.simplejava_ClassDeclaration = simplejava_ClassDeclaration
        self.simplejava_ClassDeclaration6 = simplejava_ClassDeclaration6 if simplejava_ClassDeclaration6 is not None else set()
        self.simplejava_ClassDeclaration8 = simplejava_ClassDeclaration8 if simplejava_ClassDeclaration8 is not None else set()
        self.simplejava_ClassDeclaration14 = simplejava_ClassDeclaration14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplejava_ClassDeclaration14(self):
        return self.__simplejava_ClassDeclaration14

    @simplejava_ClassDeclaration14.setter
    def simplejava_ClassDeclaration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_ClassDeclaration__simplejava_ClassDeclaration14", None)
        self.__simplejava_ClassDeclaration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Type13"):
                opp_val = getattr(old_value, "simplejava_Type13", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Type13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Type13"):
                opp_val = getattr(value, "simplejava_Type13", None)
                setattr(value, "simplejava_Type13", self)

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
class simplejava_Statement:

    pass
class Statement:

    pass
class simplejava_Assignment(Statement, SimpleStatement):

    pass
class simplejava_WhileStatement(Statement):

    pass
class simplejava_VariableDeclaration(Statement, SimpleVariableDeclaration):

    pass
class simplejava_MethodCall(Statement, GenericExpression):

    def __init__(self, thisObject: bool, methodName: str, simplejava_MethodCall: "simplejava_Parameter" = None, simplejava_MethodCall69: "simplejava_Method" = None, simplejava_MethodCall72: set["simplejava_GenericExpression"] = None):
        self.thisObject = thisObject
        self.methodName = methodName
        self.simplejava_MethodCall = simplejava_MethodCall
        self.simplejava_MethodCall69 = simplejava_MethodCall69
        self.simplejava_MethodCall72 = simplejava_MethodCall72 if simplejava_MethodCall72 is not None else set()
        
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
            if hasattr(old_value, "simplejava_Parameter67"):
                opp_val = getattr(old_value, "simplejava_Parameter67", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Parameter67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Parameter67"):
                opp_val = getattr(value, "simplejava_Parameter67", None)
                setattr(value, "simplejava_Parameter67", self)

    @property
    def simplejava_MethodCall69(self):
        return self.__simplejava_MethodCall69

    @simplejava_MethodCall69.setter
    def simplejava_MethodCall69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodCall__simplejava_MethodCall69", None)
        self.__simplejava_MethodCall69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_Method70"):
                opp_val = getattr(old_value, "simplejava_Method70", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_Method70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_Method70"):
                opp_val = getattr(value, "simplejava_Method70", None)
                setattr(value, "simplejava_Method70", self)

    @property
    def simplejava_MethodCall72(self):
        return self.__simplejava_MethodCall72

    @simplejava_MethodCall72.setter
    def simplejava_MethodCall72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodCall__simplejava_MethodCall72", None)
        self.__simplejava_MethodCall72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplejava_GenericExpression73"):
                    opp_val = getattr(item, "simplejava_GenericExpression73", None)
                    
                    if opp_val == self:
                        setattr(item, "simplejava_GenericExpression73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplejava_GenericExpression73"):
                    opp_val = getattr(item, "simplejava_GenericExpression73", None)
                    
                    setattr(item, "simplejava_GenericExpression73", self)
                    

class simplejava_ReturnStatement(Statement):

    pass
class simplejava_IfStatement(Statement):

    pass
class simplejava_ForStatement(Statement):

    pass
class simplejava_ForInStatement(Statement):

    pass
class simplejava_MethodBlock(Statement):

    def __init__(self, generated: bool, simplejava_MethodBlock: "simplejava_Method" = None, simplejava_MethodBlock23: set["simplejava_Statement"] = None, simplejava_MethodBlock37: "simplejava_IfStatement" = None, simplejava_MethodBlock40: "simplejava_IfStatement" = None):
        self.generated = generated
        self.simplejava_MethodBlock = simplejava_MethodBlock
        self.simplejava_MethodBlock23 = simplejava_MethodBlock23 if simplejava_MethodBlock23 is not None else set()
        self.simplejava_MethodBlock37 = simplejava_MethodBlock37
        self.simplejava_MethodBlock40 = simplejava_MethodBlock40
        
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
    def simplejava_MethodBlock37(self):
        return self.__simplejava_MethodBlock37

    @simplejava_MethodBlock37.setter
    def simplejava_MethodBlock37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock37", None)
        self.__simplejava_MethodBlock37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_IfStatement36"):
                opp_val = getattr(old_value, "simplejava_IfStatement36", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_IfStatement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_IfStatement36"):
                opp_val = getattr(value, "simplejava_IfStatement36", None)
                setattr(value, "simplejava_IfStatement36", self)

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
    def simplejava_MethodBlock40(self):
        return self.__simplejava_MethodBlock40

    @simplejava_MethodBlock40.setter
    def simplejava_MethodBlock40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplejava_MethodBlock__simplejava_MethodBlock40", None)
        self.__simplejava_MethodBlock40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplejava_IfStatement39"):
                opp_val = getattr(old_value, "simplejava_IfStatement39", None)
                if opp_val == self:
                    setattr(old_value, "simplejava_IfStatement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplejava_IfStatement39"):
                opp_val = getattr(value, "simplejava_IfStatement39", None)
                setattr(value, "simplejava_IfStatement39", self)

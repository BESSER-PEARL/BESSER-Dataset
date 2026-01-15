from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class IndexTerminal:

    pass
class express_IntLiteral(IndexTerminal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class express_VarLiteral(IndexTerminal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class express_Index:

    pass
class VarOrAttrib:

    pass
class express_IndexedVar(VarOrAttrib):

    pass
class express_AttributeVar(VarOrAttrib):

    pass
class express_SimpleVar(VarOrAttrib):

    def __init__(self, name: str, express_SimpleVar: "express_IndexedVar" = None):
        self.name = name
        self.express_SimpleVar = express_SimpleVar
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_SimpleVar(self):
        return self.__express_SimpleVar

    @express_SimpleVar.setter
    def express_SimpleVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_SimpleVar__express_SimpleVar", None)
        self.__express_SimpleVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_IndexedVar"):
                opp_val = getattr(old_value, "express_IndexedVar", None)
                if opp_val == self:
                    setattr(old_value, "express_IndexedVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_IndexedVar"):
                opp_val = getattr(value, "express_IndexedVar", None)
                setattr(value, "express_IndexedVar", self)

class express_VarOrAttrib:

    pass
class Index:

    pass
class express_IndexTerminal(Index):

    pass
class express_CaseAction:

    def __init__(self, value: str, express_CaseAction: "express_CaseStatement" = None, express_CaseAction103: "express_Statement" = None):
        self.value = value
        self.express_CaseAction = express_CaseAction
        self.express_CaseAction103 = express_CaseAction103
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def express_CaseAction(self):
        return self.__express_CaseAction

    @express_CaseAction.setter
    def express_CaseAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CaseAction__express_CaseAction", None)
        self.__express_CaseAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_CaseStatement"):
                opp_val = getattr(old_value, "express_CaseStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_CaseStatement"):
                opp_val = getattr(value, "express_CaseStatement", None)
                if opp_val is None:
                    setattr(value, "express_CaseStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_CaseAction103(self):
        return self.__express_CaseAction103

    @express_CaseAction103.setter
    def express_CaseAction103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CaseAction__express_CaseAction103", None)
        self.__express_CaseAction103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Statement104"):
                opp_val = getattr(old_value, "express_Statement104", None)
                if opp_val == self:
                    setattr(old_value, "express_Statement104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Statement104"):
                opp_val = getattr(value, "express_Statement104", None)
                setattr(value, "express_Statement104", self)

class Statement:

    pass
class express_CaseStatement(Statement):

    def __init__(self, variable: str, express_CaseStatement100: set["express_Statement"] = None, express_CaseStatement: set["express_CaseAction"] = None):
        self.variable = variable
        self.express_CaseStatement100 = express_CaseStatement100 if express_CaseStatement100 is not None else set()
        self.express_CaseStatement = express_CaseStatement if express_CaseStatement is not None else set()
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def express_CaseStatement100(self):
        return self.__express_CaseStatement100

    @express_CaseStatement100.setter
    def express_CaseStatement100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CaseStatement__express_CaseStatement100", None)
        self.__express_CaseStatement100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Statement101"):
                    opp_val = getattr(item, "express_Statement101", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Statement101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Statement101"):
                    opp_val = getattr(item, "express_Statement101", None)
                    
                    setattr(item, "express_Statement101", self)
                    

    @property
    def express_CaseStatement(self):
        return self.__express_CaseStatement

    @express_CaseStatement.setter
    def express_CaseStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CaseStatement__express_CaseStatement", None)
        self.__express_CaseStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_CaseAction"):
                    opp_val = getattr(item, "express_CaseAction", None)
                    
                    if opp_val == self:
                        setattr(item, "express_CaseAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_CaseAction"):
                    opp_val = getattr(item, "express_CaseAction", None)
                    
                    setattr(item, "express_CaseAction", self)
                    

class express_EscapeStatement(Statement):

    pass
class express_ReturnStatement(Statement):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class express_IfStatement(Statement):

    pass
class express_RepeatStatement(Statement):

    def __init__(self, idx: str, start: str, end: str, express_RepeatStatement: set["express_Statement"] = None):
        self.idx = idx
        self.start = start
        self.end = end
        self.express_RepeatStatement = express_RepeatStatement if express_RepeatStatement is not None else set()
        
    @property
    def idx(self) -> str:
        return self.__idx

    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def express_RepeatStatement(self):
        return self.__express_RepeatStatement

    @express_RepeatStatement.setter
    def express_RepeatStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_RepeatStatement__express_RepeatStatement", None)
        self.__express_RepeatStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Statement120"):
                    opp_val = getattr(item, "express_Statement120", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Statement120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Statement120"):
                    opp_val = getattr(item, "express_Statement120", None)
                    
                    setattr(item, "express_Statement120", self)
                    

class express_Assignment(Statement):

    def __init__(self, expression: str, express_Assignment: "express_VarOrAttrib" = None):
        self.expression = expression
        self.express_Assignment = express_Assignment
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def express_Assignment(self):
        return self.__express_Assignment

    @express_Assignment.setter
    def express_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Assignment__express_Assignment", None)
        self.__express_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_VarOrAttrib"):
                opp_val = getattr(old_value, "express_VarOrAttrib", None)
                if opp_val == self:
                    setattr(old_value, "express_VarOrAttrib", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_VarOrAttrib"):
                opp_val = getattr(value, "express_VarOrAttrib", None)
                setattr(value, "express_VarOrAttrib", self)

class express_SequenceStatement(Statement):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class express_LiteralType:

    def __init__(self, name: str, express_LiteralType: "express_EnumType" = None):
        self.name = name
        self.express_LiteralType = express_LiteralType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_LiteralType(self):
        return self.__express_LiteralType

    @express_LiteralType.setter
    def express_LiteralType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LiteralType__express_LiteralType", None)
        self.__express_LiteralType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_EnumType"):
                opp_val = getattr(old_value, "express_EnumType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_EnumType"):
                opp_val = getattr(value, "express_EnumType", None)
                if opp_val is None:
                    setattr(value, "express_EnumType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BuiltInType:

    pass
class express_BinaryType(BuiltInType):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class express_LogicalType(BuiltInType):

    pass
class express_BooleanType(BuiltInType):

    pass
class express_StringType(BuiltInType):

    def __init__(self, size: int, fixed: bool):
        self.size = size
        self.fixed = fixed
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def fixed(self) -> bool:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: bool):
        self.__fixed = fixed

class express_IntegerType(BuiltInType):

    pass
class express_NumberType(BuiltInType):

    pass
class express_RealType(BuiltInType):

    pass
class DataType:

    pass
class express_EnumType(DataType):

    pass
class express_SelectType(DataType):

    pass
class express_ReferenceType(DataType):

    pass
class express_BuiltInType(DataType):

    pass
class express_Intervall:

    def __init__(self, expression: str, express_Intervall: "express_WhereRule" = None):
        self.expression = expression
        self.express_Intervall = express_Intervall
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def express_Intervall(self):
        return self.__express_Intervall

    @express_Intervall.setter
    def express_Intervall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Intervall__express_Intervall", None)
        self.__express_Intervall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_WhereRule84"):
                opp_val = getattr(old_value, "express_WhereRule84", None)
                if opp_val == self:
                    setattr(old_value, "express_WhereRule84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_WhereRule84"):
                opp_val = getattr(value, "express_WhereRule84", None)
                setattr(value, "express_WhereRule84", self)

class express_FormalParam:

    def __init__(self, paramName: str, express_FormalParam: "express_ParameterList" = None, express_FormalParam81: "express_DataType" = None):
        self.paramName = paramName
        self.express_FormalParam = express_FormalParam
        self.express_FormalParam81 = express_FormalParam81
        
    @property
    def paramName(self) -> str:
        return self.__paramName

    @paramName.setter
    def paramName(self, paramName: str):
        self.__paramName = paramName

    @property
    def express_FormalParam(self):
        return self.__express_FormalParam

    @express_FormalParam.setter
    def express_FormalParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FormalParam__express_FormalParam", None)
        self.__express_FormalParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ParameterList79"):
                opp_val = getattr(old_value, "express_ParameterList79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ParameterList79"):
                opp_val = getattr(value, "express_ParameterList79", None)
                if opp_val is None:
                    setattr(value, "express_ParameterList79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_FormalParam81(self):
        return self.__express_FormalParam81

    @express_FormalParam81.setter
    def express_FormalParam81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FormalParam__express_FormalParam81", None)
        self.__express_FormalParam81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType82"):
                opp_val = getattr(old_value, "express_DataType82", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType82"):
                opp_val = getattr(value, "express_DataType82", None)
                setattr(value, "express_DataType82", self)

class express_CollectionType(DataType):

    def __init__(self, name: str, lowerBound: int, upperBound: int, many: bool, opt: bool, unique: bool, express_CollectionType: "express_Attribute" = None, express_CollectionType90: "express_Attribute" = None, express_CollectionType93: "express_DataType" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.opt = opt
        self.unique = unique
        self.express_CollectionType = express_CollectionType
        self.express_CollectionType90 = express_CollectionType90
        self.express_CollectionType93 = express_CollectionType93
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def opt(self) -> bool:
        return self.__opt

    @opt.setter
    def opt(self, opt: bool):
        self.__opt = opt

    @property
    def express_CollectionType90(self):
        return self.__express_CollectionType90

    @express_CollectionType90.setter
    def express_CollectionType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CollectionType__express_CollectionType90", None)
        self.__express_CollectionType90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Attribute91"):
                opp_val = getattr(old_value, "express_Attribute91", None)
                if opp_val == self:
                    setattr(old_value, "express_Attribute91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Attribute91"):
                opp_val = getattr(value, "express_Attribute91", None)
                setattr(value, "express_Attribute91", self)

    @property
    def express_CollectionType(self):
        return self.__express_CollectionType

    @express_CollectionType.setter
    def express_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CollectionType__express_CollectionType", None)
        self.__express_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Attribute88"):
                opp_val = getattr(old_value, "express_Attribute88", None)
                if opp_val == self:
                    setattr(old_value, "express_Attribute88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Attribute88"):
                opp_val = getattr(value, "express_Attribute88", None)
                setattr(value, "express_Attribute88", self)

    @property
    def express_CollectionType93(self):
        return self.__express_CollectionType93

    @express_CollectionType93.setter
    def express_CollectionType93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_CollectionType__express_CollectionType93", None)
        self.__express_CollectionType93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType94"):
                opp_val = getattr(old_value, "express_DataType94", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType94"):
                opp_val = getattr(value, "express_DataType94", None)
                setattr(value, "express_DataType94", self)

class express_GenericType(DataType):

    def __init__(self, typelabel: str):
        self.typelabel = typelabel
        
    @property
    def typelabel(self) -> str:
        return self.__typelabel

    @typelabel.setter
    def typelabel(self, typelabel: str):
        self.__typelabel = typelabel

class express_ParameterList:

    pass
class express_FunctionExpression:

    def __init__(self, name: str, express_FunctionExpression: "express_ParameterList" = None, express_FunctionExpression55: "express_DataType" = None, express_FunctionExpression58: set["express_LocalVar"] = None, express_FunctionExpression61: set["express_Statement"] = None):
        self.name = name
        self.express_FunctionExpression = express_FunctionExpression
        self.express_FunctionExpression55 = express_FunctionExpression55
        self.express_FunctionExpression58 = express_FunctionExpression58 if express_FunctionExpression58 is not None else set()
        self.express_FunctionExpression61 = express_FunctionExpression61 if express_FunctionExpression61 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_FunctionExpression(self):
        return self.__express_FunctionExpression

    @express_FunctionExpression.setter
    def express_FunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FunctionExpression__express_FunctionExpression", None)
        self.__express_FunctionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ParameterList"):
                opp_val = getattr(old_value, "express_ParameterList", None)
                if opp_val == self:
                    setattr(old_value, "express_ParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ParameterList"):
                opp_val = getattr(value, "express_ParameterList", None)
                setattr(value, "express_ParameterList", self)

    @property
    def express_FunctionExpression61(self):
        return self.__express_FunctionExpression61

    @express_FunctionExpression61.setter
    def express_FunctionExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FunctionExpression__express_FunctionExpression61", None)
        self.__express_FunctionExpression61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Statement62"):
                    opp_val = getattr(item, "express_Statement62", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Statement62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Statement62"):
                    opp_val = getattr(item, "express_Statement62", None)
                    
                    setattr(item, "express_Statement62", self)
                    

    @property
    def express_FunctionExpression55(self):
        return self.__express_FunctionExpression55

    @express_FunctionExpression55.setter
    def express_FunctionExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FunctionExpression__express_FunctionExpression55", None)
        self.__express_FunctionExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType56"):
                opp_val = getattr(old_value, "express_DataType56", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType56"):
                opp_val = getattr(value, "express_DataType56", None)
                setattr(value, "express_DataType56", self)

    @property
    def express_FunctionExpression58(self):
        return self.__express_FunctionExpression58

    @express_FunctionExpression58.setter
    def express_FunctionExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_FunctionExpression__express_FunctionExpression58", None)
        self.__express_FunctionExpression58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_LocalVar59"):
                    opp_val = getattr(item, "express_LocalVar59", None)
                    
                    if opp_val == self:
                        setattr(item, "express_LocalVar59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_LocalVar59"):
                    opp_val = getattr(item, "express_LocalVar59", None)
                    
                    setattr(item, "express_LocalVar59", self)
                    

class express_Line:

    def __init__(self, text: str, express_Line52: "express_LocalVar" = None, express_Line: "express_ConstantVal" = None, express_Line112: "express_IfStatement" = None):
        self.text = text
        self.express_Line52 = express_Line52
        self.express_Line = express_Line
        self.express_Line112 = express_Line112
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def express_Line52(self):
        return self.__express_Line52

    @express_Line52.setter
    def express_Line52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Line__express_Line52", None)
        self.__express_Line52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_LocalVar51"):
                opp_val = getattr(old_value, "express_LocalVar51", None)
                if opp_val == self:
                    setattr(old_value, "express_LocalVar51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_LocalVar51"):
                opp_val = getattr(value, "express_LocalVar51", None)
                setattr(value, "express_LocalVar51", self)

    @property
    def express_Line(self):
        return self.__express_Line

    @express_Line.setter
    def express_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Line__express_Line", None)
        self.__express_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ConstantVal46"):
                opp_val = getattr(old_value, "express_ConstantVal46", None)
                if opp_val == self:
                    setattr(old_value, "express_ConstantVal46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ConstantVal46"):
                opp_val = getattr(value, "express_ConstantVal46", None)
                setattr(value, "express_ConstantVal46", self)

    @property
    def express_Line112(self):
        return self.__express_Line112

    @express_Line112.setter
    def express_Line112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Line__express_Line112", None)
        self.__express_Line112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_IfStatement"):
                opp_val = getattr(old_value, "express_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "express_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_IfStatement"):
                opp_val = getattr(value, "express_IfStatement", None)
                setattr(value, "express_IfStatement", self)

class express_Statement:

    pass
class express_LocalVar:

    def __init__(self, varname: str, express_LocalVar48: "express_DataType" = None, express_LocalVar: "express_Rule" = None, express_LocalVar51: "express_Line" = None, express_LocalVar59: "express_FunctionExpression" = None, express_LocalVar74: "express_Function" = None):
        self.varname = varname
        self.express_LocalVar48 = express_LocalVar48
        self.express_LocalVar = express_LocalVar
        self.express_LocalVar51 = express_LocalVar51
        self.express_LocalVar59 = express_LocalVar59
        self.express_LocalVar74 = express_LocalVar74
        
    @property
    def varname(self) -> str:
        return self.__varname

    @varname.setter
    def varname(self, varname: str):
        self.__varname = varname

    @property
    def express_LocalVar59(self):
        return self.__express_LocalVar59

    @express_LocalVar59.setter
    def express_LocalVar59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LocalVar__express_LocalVar59", None)
        self.__express_LocalVar59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_FunctionExpression58"):
                opp_val = getattr(old_value, "express_FunctionExpression58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_FunctionExpression58"):
                opp_val = getattr(value, "express_FunctionExpression58", None)
                if opp_val is None:
                    setattr(value, "express_FunctionExpression58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_LocalVar74(self):
        return self.__express_LocalVar74

    @express_LocalVar74.setter
    def express_LocalVar74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LocalVar__express_LocalVar74", None)
        self.__express_LocalVar74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Function73"):
                opp_val = getattr(old_value, "express_Function73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Function73"):
                opp_val = getattr(value, "express_Function73", None)
                if opp_val is None:
                    setattr(value, "express_Function73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_LocalVar48(self):
        return self.__express_LocalVar48

    @express_LocalVar48.setter
    def express_LocalVar48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LocalVar__express_LocalVar48", None)
        self.__express_LocalVar48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType49"):
                opp_val = getattr(old_value, "express_DataType49", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType49"):
                opp_val = getattr(value, "express_DataType49", None)
                setattr(value, "express_DataType49", self)

    @property
    def express_LocalVar(self):
        return self.__express_LocalVar

    @express_LocalVar.setter
    def express_LocalVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LocalVar__express_LocalVar", None)
        self.__express_LocalVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Rule36"):
                opp_val = getattr(old_value, "express_Rule36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Rule36"):
                opp_val = getattr(value, "express_Rule36", None)
                if opp_val is None:
                    setattr(value, "express_Rule36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_LocalVar51(self):
        return self.__express_LocalVar51

    @express_LocalVar51.setter
    def express_LocalVar51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_LocalVar__express_LocalVar51", None)
        self.__express_LocalVar51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Line52"):
                opp_val = getattr(old_value, "express_Line52", None)
                if opp_val == self:
                    setattr(old_value, "express_Line52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Line52"):
                opp_val = getattr(value, "express_Line52", None)
                setattr(value, "express_Line52", self)

class express_ConstantVal:

    def __init__(self, name: str, express_ConstantVal: "express_Rule" = None, express_ConstantVal43: "express_DataType" = None, express_ConstantVal46: "express_Line" = None, express_ConstantVal71: "express_Function" = None):
        self.name = name
        self.express_ConstantVal = express_ConstantVal
        self.express_ConstantVal43 = express_ConstantVal43
        self.express_ConstantVal46 = express_ConstantVal46
        self.express_ConstantVal71 = express_ConstantVal71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_ConstantVal43(self):
        return self.__express_ConstantVal43

    @express_ConstantVal43.setter
    def express_ConstantVal43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ConstantVal__express_ConstantVal43", None)
        self.__express_ConstantVal43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType44"):
                opp_val = getattr(old_value, "express_DataType44", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType44"):
                opp_val = getattr(value, "express_DataType44", None)
                setattr(value, "express_DataType44", self)

    @property
    def express_ConstantVal(self):
        return self.__express_ConstantVal

    @express_ConstantVal.setter
    def express_ConstantVal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ConstantVal__express_ConstantVal", None)
        self.__express_ConstantVal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Rule34"):
                opp_val = getattr(old_value, "express_Rule34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Rule34"):
                opp_val = getattr(value, "express_Rule34", None)
                if opp_val is None:
                    setattr(value, "express_Rule34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_ConstantVal46(self):
        return self.__express_ConstantVal46

    @express_ConstantVal46.setter
    def express_ConstantVal46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ConstantVal__express_ConstantVal46", None)
        self.__express_ConstantVal46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Line"):
                opp_val = getattr(old_value, "express_Line", None)
                if opp_val == self:
                    setattr(old_value, "express_Line", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Line"):
                opp_val = getattr(value, "express_Line", None)
                setattr(value, "express_Line", self)

    @property
    def express_ConstantVal71(self):
        return self.__express_ConstantVal71

    @express_ConstantVal71.setter
    def express_ConstantVal71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ConstantVal__express_ConstantVal71", None)
        self.__express_ConstantVal71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Function70"):
                opp_val = getattr(old_value, "express_Function70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Function70"):
                opp_val = getattr(value, "express_Function70", None)
                if opp_val is None:
                    setattr(value, "express_Function70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class express_TypeNameList:

    def __init__(self, type: str, express_TypeNameList: "express_Rule" = None):
        self.type = type
        self.express_TypeNameList = express_TypeNameList
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def express_TypeNameList(self):
        return self.__express_TypeNameList

    @express_TypeNameList.setter
    def express_TypeNameList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_TypeNameList__express_TypeNameList", None)
        self.__express_TypeNameList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Rule32"):
                opp_val = getattr(old_value, "express_Rule32", None)
                if opp_val == self:
                    setattr(old_value, "express_Rule32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Rule32"):
                opp_val = getattr(value, "express_Rule32", None)
                setattr(value, "express_Rule32", self)

class express_Reference:

    def __init__(self, qualifier: str, name: str, optional: bool, self: bool, express_Reference: "express_Entity" = None):
        self.qualifier = qualifier
        self.name = name
        self.optional = optional
        self.self = self
        self.express_Reference = express_Reference
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def self(self) -> bool:
        return self.__self

    @self.setter
    def self(self, self: bool):
        self.__self = self

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def express_Reference(self):
        return self.__express_Reference

    @express_Reference.setter
    def express_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Reference__express_Reference", None)
        self.__express_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity30"):
                opp_val = getattr(old_value, "express_Entity30", None)
                if opp_val == self:
                    setattr(old_value, "express_Entity30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity30"):
                opp_val = getattr(value, "express_Entity30", None)
                setattr(value, "express_Entity30", self)

class express_UniqueRule:

    def __init__(self, name: str, attribute: str, express_UniqueRule: "express_Entity" = None):
        self.name = name
        self.attribute = attribute
        self.express_UniqueRule = express_UniqueRule
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_UniqueRule(self):
        return self.__express_UniqueRule

    @express_UniqueRule.setter
    def express_UniqueRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_UniqueRule__express_UniqueRule", None)
        self.__express_UniqueRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity22"):
                opp_val = getattr(old_value, "express_Entity22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity22"):
                opp_val = getattr(value, "express_Entity22", None)
                if opp_val is None:
                    setattr(value, "express_Entity22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class express_Attribute:

    def __init__(self, self: bool, qualifier: str, name: str, optional: bool, expression: str, express_Attribute: "express_Entity" = None, express_Attribute24: "express_DataType" = None, express_Attribute28: "express_Attribute" = None, express_Attribute26: "express_Attribute" = None, express_Attribute88: "express_CollectionType" = None, express_Attribute91: "express_CollectionType" = None):
        self.self = self
        self.qualifier = qualifier
        self.name = name
        self.optional = optional
        self.expression = expression
        self.express_Attribute = express_Attribute
        self.express_Attribute24 = express_Attribute24
        self.express_Attribute28 = express_Attribute28
        self.express_Attribute26 = express_Attribute26
        self.express_Attribute88 = express_Attribute88
        self.express_Attribute91 = express_Attribute91
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def self(self) -> bool:
        return self.__self

    @self.setter
    def self(self, self: bool):
        self.__self = self

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_Attribute28(self):
        return self.__express_Attribute28

    @express_Attribute28.setter
    def express_Attribute28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute28", None)
        self.__express_Attribute28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Attribute26"):
                opp_val = getattr(old_value, "express_Attribute26", None)
                if opp_val == self:
                    setattr(old_value, "express_Attribute26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Attribute26"):
                opp_val = getattr(value, "express_Attribute26", None)
                setattr(value, "express_Attribute26", self)

    @property
    def express_Attribute26(self):
        return self.__express_Attribute26

    @express_Attribute26.setter
    def express_Attribute26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute26", None)
        self.__express_Attribute26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Attribute28"):
                opp_val = getattr(old_value, "express_Attribute28", None)
                if opp_val == self:
                    setattr(old_value, "express_Attribute28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Attribute28"):
                opp_val = getattr(value, "express_Attribute28", None)
                setattr(value, "express_Attribute28", self)

    @property
    def express_Attribute(self):
        return self.__express_Attribute

    @express_Attribute.setter
    def express_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute", None)
        self.__express_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity20"):
                opp_val = getattr(old_value, "express_Entity20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity20"):
                opp_val = getattr(value, "express_Entity20", None)
                if opp_val is None:
                    setattr(value, "express_Entity20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Attribute24(self):
        return self.__express_Attribute24

    @express_Attribute24.setter
    def express_Attribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute24", None)
        self.__express_Attribute24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType25"):
                opp_val = getattr(old_value, "express_DataType25", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType25"):
                opp_val = getattr(value, "express_DataType25", None)
                setattr(value, "express_DataType25", self)

    @property
    def express_Attribute91(self):
        return self.__express_Attribute91

    @express_Attribute91.setter
    def express_Attribute91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute91", None)
        self.__express_Attribute91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_CollectionType90"):
                opp_val = getattr(old_value, "express_CollectionType90", None)
                if opp_val == self:
                    setattr(old_value, "express_CollectionType90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_CollectionType90"):
                opp_val = getattr(value, "express_CollectionType90", None)
                setattr(value, "express_CollectionType90", self)

    @property
    def express_Attribute88(self):
        return self.__express_Attribute88

    @express_Attribute88.setter
    def express_Attribute88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Attribute__express_Attribute88", None)
        self.__express_Attribute88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_CollectionType"):
                opp_val = getattr(old_value, "express_CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "express_CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_CollectionType"):
                opp_val = getattr(value, "express_CollectionType", None)
                setattr(value, "express_CollectionType", self)

class express_DataType:

    pass
class ExpressConcept:

    pass
class express_WhereRule:

    def __init__(self, name: str, expression: str, express_WhereRule: "express_ExpressConcept" = None, express_WhereRule41: "express_Rule" = None, express_WhereRule84: "express_Intervall" = None):
        self.name = name
        self.expression = expression
        self.express_WhereRule = express_WhereRule
        self.express_WhereRule41 = express_WhereRule41
        self.express_WhereRule84 = express_WhereRule84
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_WhereRule(self):
        return self.__express_WhereRule

    @express_WhereRule.setter
    def express_WhereRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_WhereRule__express_WhereRule", None)
        self.__express_WhereRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ExpressConcept"):
                opp_val = getattr(old_value, "express_ExpressConcept", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ExpressConcept"):
                opp_val = getattr(value, "express_ExpressConcept", None)
                if opp_val is None:
                    setattr(value, "express_ExpressConcept", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_WhereRule41(self):
        return self.__express_WhereRule41

    @express_WhereRule41.setter
    def express_WhereRule41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_WhereRule__express_WhereRule41", None)
        self.__express_WhereRule41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Rule40"):
                opp_val = getattr(old_value, "express_Rule40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Rule40"):
                opp_val = getattr(value, "express_Rule40", None)
                if opp_val is None:
                    setattr(value, "express_Rule40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_WhereRule84(self):
        return self.__express_WhereRule84

    @express_WhereRule84.setter
    def express_WhereRule84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_WhereRule__express_WhereRule84", None)
        self.__express_WhereRule84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Intervall"):
                opp_val = getattr(old_value, "express_Intervall", None)
                if opp_val == self:
                    setattr(old_value, "express_Intervall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Intervall"):
                opp_val = getattr(value, "express_Intervall", None)
                setattr(value, "express_Intervall", self)

class express_ExpressConcept:

    def __init__(self, name: str, express_ExpressConcept: set["express_WhereRule"] = None, express_ExpressConcept86: "express_ReferenceType" = None, express_ExpressConcept97: "express_SelectType" = None):
        self.name = name
        self.express_ExpressConcept = express_ExpressConcept if express_ExpressConcept is not None else set()
        self.express_ExpressConcept86 = express_ExpressConcept86
        self.express_ExpressConcept97 = express_ExpressConcept97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_ExpressConcept(self):
        return self.__express_ExpressConcept

    @express_ExpressConcept.setter
    def express_ExpressConcept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ExpressConcept__express_ExpressConcept", None)
        self.__express_ExpressConcept = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_WhereRule"):
                    opp_val = getattr(item, "express_WhereRule", None)
                    
                    if opp_val == self:
                        setattr(item, "express_WhereRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_WhereRule"):
                    opp_val = getattr(item, "express_WhereRule", None)
                    
                    setattr(item, "express_WhereRule", self)
                    

    @property
    def express_ExpressConcept97(self):
        return self.__express_ExpressConcept97

    @express_ExpressConcept97.setter
    def express_ExpressConcept97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ExpressConcept__express_ExpressConcept97", None)
        self.__express_ExpressConcept97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_SelectType"):
                opp_val = getattr(old_value, "express_SelectType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_SelectType"):
                opp_val = getattr(value, "express_SelectType", None)
                if opp_val is None:
                    setattr(value, "express_SelectType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_ExpressConcept86(self):
        return self.__express_ExpressConcept86

    @express_ExpressConcept86.setter
    def express_ExpressConcept86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_ExpressConcept__express_ExpressConcept86", None)
        self.__express_ExpressConcept86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ReferenceType"):
                opp_val = getattr(old_value, "express_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "express_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ReferenceType"):
                opp_val = getattr(value, "express_ReferenceType", None)
                setattr(value, "express_ReferenceType", self)

class express_Rule:

    def __init__(self, name: str, express_Rule: "express_Schema" = None, express_Rule32: "express_TypeNameList" = None, express_Rule34: set["express_ConstantVal"] = None, express_Rule36: set["express_LocalVar"] = None, express_Rule38: set["express_Statement"] = None, express_Rule40: set["express_WhereRule"] = None):
        self.name = name
        self.express_Rule = express_Rule
        self.express_Rule32 = express_Rule32
        self.express_Rule34 = express_Rule34 if express_Rule34 is not None else set()
        self.express_Rule36 = express_Rule36 if express_Rule36 is not None else set()
        self.express_Rule38 = express_Rule38 if express_Rule38 is not None else set()
        self.express_Rule40 = express_Rule40 if express_Rule40 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_Rule32(self):
        return self.__express_Rule32

    @express_Rule32.setter
    def express_Rule32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule32", None)
        self.__express_Rule32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_TypeNameList"):
                opp_val = getattr(old_value, "express_TypeNameList", None)
                if opp_val == self:
                    setattr(old_value, "express_TypeNameList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_TypeNameList"):
                opp_val = getattr(value, "express_TypeNameList", None)
                setattr(value, "express_TypeNameList", self)

    @property
    def express_Rule(self):
        return self.__express_Rule

    @express_Rule.setter
    def express_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule", None)
        self.__express_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Schema6"):
                opp_val = getattr(old_value, "express_Schema6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Schema6"):
                opp_val = getattr(value, "express_Schema6", None)
                if opp_val is None:
                    setattr(value, "express_Schema6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Rule36(self):
        return self.__express_Rule36

    @express_Rule36.setter
    def express_Rule36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule36", None)
        self.__express_Rule36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_LocalVar"):
                    opp_val = getattr(item, "express_LocalVar", None)
                    
                    if opp_val == self:
                        setattr(item, "express_LocalVar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_LocalVar"):
                    opp_val = getattr(item, "express_LocalVar", None)
                    
                    setattr(item, "express_LocalVar", self)
                    

    @property
    def express_Rule40(self):
        return self.__express_Rule40

    @express_Rule40.setter
    def express_Rule40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule40", None)
        self.__express_Rule40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_WhereRule41"):
                    opp_val = getattr(item, "express_WhereRule41", None)
                    
                    if opp_val == self:
                        setattr(item, "express_WhereRule41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_WhereRule41"):
                    opp_val = getattr(item, "express_WhereRule41", None)
                    
                    setattr(item, "express_WhereRule41", self)
                    

    @property
    def express_Rule34(self):
        return self.__express_Rule34

    @express_Rule34.setter
    def express_Rule34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule34", None)
        self.__express_Rule34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_ConstantVal"):
                    opp_val = getattr(item, "express_ConstantVal", None)
                    
                    if opp_val == self:
                        setattr(item, "express_ConstantVal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_ConstantVal"):
                    opp_val = getattr(item, "express_ConstantVal", None)
                    
                    setattr(item, "express_ConstantVal", self)
                    

    @property
    def express_Rule38(self):
        return self.__express_Rule38

    @express_Rule38.setter
    def express_Rule38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Rule__express_Rule38", None)
        self.__express_Rule38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Statement"):
                    opp_val = getattr(item, "express_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Statement"):
                    opp_val = getattr(item, "express_Statement", None)
                    
                    setattr(item, "express_Statement", self)
                    

class express_Function:

    def __init__(self, name: str, express_Function: "express_Schema" = None, express_Function76: set["express_Statement"] = None, express_Function64: "express_ParameterList" = None, express_Function67: "express_DataType" = None, express_Function70: set["express_ConstantVal"] = None, express_Function73: set["express_LocalVar"] = None):
        self.name = name
        self.express_Function = express_Function
        self.express_Function76 = express_Function76 if express_Function76 is not None else set()
        self.express_Function64 = express_Function64
        self.express_Function67 = express_Function67
        self.express_Function70 = express_Function70 if express_Function70 is not None else set()
        self.express_Function73 = express_Function73 if express_Function73 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_Function76(self):
        return self.__express_Function76

    @express_Function76.setter
    def express_Function76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function76", None)
        self.__express_Function76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Statement77"):
                    opp_val = getattr(item, "express_Statement77", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Statement77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Statement77"):
                    opp_val = getattr(item, "express_Statement77", None)
                    
                    setattr(item, "express_Statement77", self)
                    

    @property
    def express_Function73(self):
        return self.__express_Function73

    @express_Function73.setter
    def express_Function73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function73", None)
        self.__express_Function73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_LocalVar74"):
                    opp_val = getattr(item, "express_LocalVar74", None)
                    
                    if opp_val == self:
                        setattr(item, "express_LocalVar74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_LocalVar74"):
                    opp_val = getattr(item, "express_LocalVar74", None)
                    
                    setattr(item, "express_LocalVar74", self)
                    

    @property
    def express_Function(self):
        return self.__express_Function

    @express_Function.setter
    def express_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function", None)
        self.__express_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Schema4"):
                opp_val = getattr(old_value, "express_Schema4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Schema4"):
                opp_val = getattr(value, "express_Schema4", None)
                if opp_val is None:
                    setattr(value, "express_Schema4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Function70(self):
        return self.__express_Function70

    @express_Function70.setter
    def express_Function70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function70", None)
        self.__express_Function70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_ConstantVal71"):
                    opp_val = getattr(item, "express_ConstantVal71", None)
                    
                    if opp_val == self:
                        setattr(item, "express_ConstantVal71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_ConstantVal71"):
                    opp_val = getattr(item, "express_ConstantVal71", None)
                    
                    setattr(item, "express_ConstantVal71", self)
                    

    @property
    def express_Function64(self):
        return self.__express_Function64

    @express_Function64.setter
    def express_Function64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function64", None)
        self.__express_Function64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_ParameterList65"):
                opp_val = getattr(old_value, "express_ParameterList65", None)
                if opp_val == self:
                    setattr(old_value, "express_ParameterList65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_ParameterList65"):
                opp_val = getattr(value, "express_ParameterList65", None)
                setattr(value, "express_ParameterList65", self)

    @property
    def express_Function67(self):
        return self.__express_Function67

    @express_Function67.setter
    def express_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Function__express_Function67", None)
        self.__express_Function67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_DataType68"):
                opp_val = getattr(old_value, "express_DataType68", None)
                if opp_val == self:
                    setattr(old_value, "express_DataType68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_DataType68"):
                opp_val = getattr(value, "express_DataType68", None)
                setattr(value, "express_DataType68", self)

class express_Entity(ExpressConcept):

    def __init__(self, abstract: bool, express_Entity12: "express_Entity" = None, express_Entity10: set["express_Entity"] = None, express_Entity: "express_Schema" = None, express_Entity15: "express_Entity" = None, express_Entity13: set["express_Entity"] = None, express_Entity18: "express_Entity" = None, express_Entity16: set["express_Entity"] = None, express_Entity20: set["express_Attribute"] = None, express_Entity22: set["express_UniqueRule"] = None, express_Entity30: "express_Reference" = None):
        self.abstract = abstract
        self.express_Entity12 = express_Entity12
        self.express_Entity10 = express_Entity10 if express_Entity10 is not None else set()
        self.express_Entity = express_Entity
        self.express_Entity15 = express_Entity15
        self.express_Entity13 = express_Entity13 if express_Entity13 is not None else set()
        self.express_Entity18 = express_Entity18
        self.express_Entity16 = express_Entity16 if express_Entity16 is not None else set()
        self.express_Entity20 = express_Entity20 if express_Entity20 is not None else set()
        self.express_Entity22 = express_Entity22 if express_Entity22 is not None else set()
        self.express_Entity30 = express_Entity30
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def express_Entity20(self):
        return self.__express_Entity20

    @express_Entity20.setter
    def express_Entity20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity20", None)
        self.__express_Entity20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Attribute"):
                    opp_val = getattr(item, "express_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Attribute"):
                    opp_val = getattr(item, "express_Attribute", None)
                    
                    setattr(item, "express_Attribute", self)
                    

    @property
    def express_Entity13(self):
        return self.__express_Entity13

    @express_Entity13.setter
    def express_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity13", None)
        self.__express_Entity13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Entity15"):
                    opp_val = getattr(item, "express_Entity15", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Entity15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Entity15"):
                    opp_val = getattr(item, "express_Entity15", None)
                    
                    setattr(item, "express_Entity15", self)
                    

    @property
    def express_Entity12(self):
        return self.__express_Entity12

    @express_Entity12.setter
    def express_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity12", None)
        self.__express_Entity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity10"):
                opp_val = getattr(old_value, "express_Entity10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity10"):
                opp_val = getattr(value, "express_Entity10", None)
                if opp_val is None:
                    setattr(value, "express_Entity10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Entity18(self):
        return self.__express_Entity18

    @express_Entity18.setter
    def express_Entity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity18", None)
        self.__express_Entity18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity16"):
                opp_val = getattr(old_value, "express_Entity16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity16"):
                opp_val = getattr(value, "express_Entity16", None)
                if opp_val is None:
                    setattr(value, "express_Entity16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Entity16(self):
        return self.__express_Entity16

    @express_Entity16.setter
    def express_Entity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity16", None)
        self.__express_Entity16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Entity18"):
                    opp_val = getattr(item, "express_Entity18", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Entity18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Entity18"):
                    opp_val = getattr(item, "express_Entity18", None)
                    
                    setattr(item, "express_Entity18", self)
                    

    @property
    def express_Entity10(self):
        return self.__express_Entity10

    @express_Entity10.setter
    def express_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity10", None)
        self.__express_Entity10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Entity12"):
                    opp_val = getattr(item, "express_Entity12", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Entity12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Entity12"):
                    opp_val = getattr(item, "express_Entity12", None)
                    
                    setattr(item, "express_Entity12", self)
                    

    @property
    def express_Entity22(self):
        return self.__express_Entity22

    @express_Entity22.setter
    def express_Entity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity22", None)
        self.__express_Entity22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_UniqueRule"):
                    opp_val = getattr(item, "express_UniqueRule", None)
                    
                    if opp_val == self:
                        setattr(item, "express_UniqueRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_UniqueRule"):
                    opp_val = getattr(item, "express_UniqueRule", None)
                    
                    setattr(item, "express_UniqueRule", self)
                    

    @property
    def express_Entity(self):
        return self.__express_Entity

    @express_Entity.setter
    def express_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity", None)
        self.__express_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Schema2"):
                opp_val = getattr(old_value, "express_Schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Schema2"):
                opp_val = getattr(value, "express_Schema2", None)
                if opp_val is None:
                    setattr(value, "express_Schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def express_Entity30(self):
        return self.__express_Entity30

    @express_Entity30.setter
    def express_Entity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity30", None)
        self.__express_Entity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Reference"):
                opp_val = getattr(old_value, "express_Reference", None)
                if opp_val == self:
                    setattr(old_value, "express_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Reference"):
                opp_val = getattr(value, "express_Reference", None)
                setattr(value, "express_Reference", self)

    @property
    def express_Entity15(self):
        return self.__express_Entity15

    @express_Entity15.setter
    def express_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Entity__express_Entity15", None)
        self.__express_Entity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "express_Entity13"):
                opp_val = getattr(old_value, "express_Entity13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "express_Entity13"):
                opp_val = getattr(value, "express_Entity13", None)
                if opp_val is None:
                    setattr(value, "express_Entity13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class express_Type(ExpressConcept):

    pass
class express_Schema:

    def __init__(self, name: str, express_Schema: set["express_Type"] = None, express_Schema2: set["express_Entity"] = None, express_Schema4: set["express_Function"] = None, express_Schema6: set["express_Rule"] = None):
        self.name = name
        self.express_Schema = express_Schema if express_Schema is not None else set()
        self.express_Schema2 = express_Schema2 if express_Schema2 is not None else set()
        self.express_Schema4 = express_Schema4 if express_Schema4 is not None else set()
        self.express_Schema6 = express_Schema6 if express_Schema6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def express_Schema2(self):
        return self.__express_Schema2

    @express_Schema2.setter
    def express_Schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Schema__express_Schema2", None)
        self.__express_Schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Entity"):
                    opp_val = getattr(item, "express_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Entity"):
                    opp_val = getattr(item, "express_Entity", None)
                    
                    setattr(item, "express_Entity", self)
                    

    @property
    def express_Schema6(self):
        return self.__express_Schema6

    @express_Schema6.setter
    def express_Schema6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Schema__express_Schema6", None)
        self.__express_Schema6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Rule"):
                    opp_val = getattr(item, "express_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Rule"):
                    opp_val = getattr(item, "express_Rule", None)
                    
                    setattr(item, "express_Rule", self)
                    

    @property
    def express_Schema(self):
        return self.__express_Schema

    @express_Schema.setter
    def express_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Schema__express_Schema", None)
        self.__express_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Type"):
                    opp_val = getattr(item, "express_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Type"):
                    opp_val = getattr(item, "express_Type", None)
                    
                    setattr(item, "express_Type", self)
                    

    @property
    def express_Schema4(self):
        return self.__express_Schema4

    @express_Schema4.setter
    def express_Schema4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_Schema__express_Schema4", None)
        self.__express_Schema4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "express_Function"):
                    opp_val = getattr(item, "express_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "express_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "express_Function"):
                    opp_val = getattr(item, "express_Function", None)
                    
                    setattr(item, "express_Function", self)
                    

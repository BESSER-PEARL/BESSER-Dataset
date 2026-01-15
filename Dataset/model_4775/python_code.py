from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class VarBlock:

    pass
class limp_NoVarBlock(VarBlock):

    pass
class limp_SomeVarBlock(VarBlock):

    pass
class limp_ExprList:

    pass
class Else:

    pass
class limp_NoElse(Else):

    pass
class limp_ElseIf(Else):

    pass
class limp_ElseBlock(Else):

    pass
class AttributeBlock:

    pass
class limp_NoAttributeBlock(AttributeBlock):

    pass
class limp_SomeAttributeBlock(AttributeBlock):

    pass
class Type:

    pass
class limp_EnumType(Type):

    pass
class limp_NamedType(Type):

    pass
class limp_BoolType(Type):

    pass
class limp_RealType(Type):

    pass
class limp_RecordType(Type):

    pass
class limp_ArrayType(Type):

    pass
class limp_StringType(Type):

    pass
class limp_AbstractType(Type):

    pass
class limp_TupleType(Type):

    pass
class limp_IntegerType(Type):

    pass
class limp_VoidType(Type):

    pass
class limp_RecordFieldExpr:

    def __init__(self, fieldName: str, limp_RecordFieldExpr: "limp_RecordExpr" = None, limp_RecordFieldExpr116: "limp_Expr" = None):
        self.fieldName = fieldName
        self.limp_RecordFieldExpr = limp_RecordFieldExpr
        self.limp_RecordFieldExpr116 = limp_RecordFieldExpr116
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def limp_RecordFieldExpr(self):
        return self.__limp_RecordFieldExpr

    @limp_RecordFieldExpr.setter
    def limp_RecordFieldExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordFieldExpr__limp_RecordFieldExpr", None)
        self.__limp_RecordFieldExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_RecordExpr114"):
                opp_val = getattr(old_value, "limp_RecordExpr114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_RecordExpr114"):
                opp_val = getattr(value, "limp_RecordExpr114", None)
                if opp_val is None:
                    setattr(value, "limp_RecordExpr114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def limp_RecordFieldExpr116(self):
        return self.__limp_RecordFieldExpr116

    @limp_RecordFieldExpr116.setter
    def limp_RecordFieldExpr116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordFieldExpr__limp_RecordFieldExpr116", None)
        self.__limp_RecordFieldExpr116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr117"):
                opp_val = getattr(old_value, "limp_Expr117", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr117"):
                opp_val = getattr(value, "limp_Expr117", None)
                setattr(value, "limp_Expr117", self)

class Expr:

    pass
class limp_RealLiteralExpr(Expr):

    def __init__(self, realVal: str):
        self.realVal = realVal
        
    @property
    def realVal(self) -> str:
        return self.__realVal

    @realVal.setter
    def realVal(self, realVal: str):
        self.__realVal = realVal

class limp_ChoiceExpr(Expr):

    pass
class limp_IntegerWildCardExpr(Expr):

    pass
class limp_IdExpr(Expr):

    pass
class limp_FreshVariable(Expr):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class limp_IntegerLiteralExpr(Expr):

    def __init__(self, intVal: str):
        self.intVal = intVal
        
    @property
    def intVal(self) -> str:
        return self.__intVal

    @intVal.setter
    def intVal(self, intVal: str):
        self.__intVal = intVal

class limp_UnaryNegationExpr(Expr):

    pass
class limp_ArrayAccessExpr(Expr):

    pass
class limp_RecordExpr(Expr):

    pass
class limp_StringLiteralExpr(Expr):

    def __init__(self, stringVal: str):
        self.stringVal = stringVal
        
    @property
    def stringVal(self) -> str:
        return self.__stringVal

    @stringVal.setter
    def stringVal(self, stringVal: str):
        self.__stringVal = stringVal

class limp_BinaryExpr(Expr):

    def __init__(self, op: str, limp_BinaryExpr: "limp_Expr" = None, limp_BinaryExpr154: "limp_Expr" = None):
        self.op = op
        self.limp_BinaryExpr = limp_BinaryExpr
        self.limp_BinaryExpr154 = limp_BinaryExpr154
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def limp_BinaryExpr154(self):
        return self.__limp_BinaryExpr154

    @limp_BinaryExpr154.setter
    def limp_BinaryExpr154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_BinaryExpr__limp_BinaryExpr154", None)
        self.__limp_BinaryExpr154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr155"):
                opp_val = getattr(old_value, "limp_Expr155", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr155"):
                opp_val = getattr(value, "limp_Expr155", None)
                setattr(value, "limp_Expr155", self)

    @property
    def limp_BinaryExpr(self):
        return self.__limp_BinaryExpr

    @limp_BinaryExpr.setter
    def limp_BinaryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_BinaryExpr__limp_BinaryExpr", None)
        self.__limp_BinaryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr152"):
                opp_val = getattr(old_value, "limp_Expr152", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr152"):
                opp_val = getattr(value, "limp_Expr152", None)
                setattr(value, "limp_Expr152", self)

class limp_IfThenElseExpr(Expr):

    pass
class limp_FcnCallExpr(Expr):

    pass
class limp_ArrayUpdateExpr(Expr):

    pass
class limp_RecordAccessExpr(Expr):

    def __init__(self, field: str, limp_RecordAccessExpr: "limp_Expr" = None):
        self.field = field
        self.limp_RecordAccessExpr = limp_RecordAccessExpr
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def limp_RecordAccessExpr(self):
        return self.__limp_RecordAccessExpr

    @limp_RecordAccessExpr.setter
    def limp_RecordAccessExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordAccessExpr__limp_RecordAccessExpr", None)
        self.__limp_RecordAccessExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr161"):
                opp_val = getattr(old_value, "limp_Expr161", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr161"):
                opp_val = getattr(value, "limp_Expr161", None)
                setattr(value, "limp_Expr161", self)

class limp_UnaryMinusExpr(Expr):

    pass
class limp_BooleanLiteralExpr(Expr):

    def __init__(self, boolVal: str):
        self.boolVal = boolVal
        
    @property
    def boolVal(self) -> str:
        return self.__boolVal

    @boolVal.setter
    def boolVal(self, boolVal: str):
        self.__boolVal = boolVal

class limp_InitExpr(Expr):

    pass
class limp_RecordUpdateExpr(Expr):

    def __init__(self, field: str, limp_RecordUpdateExpr: "limp_Expr" = None, limp_RecordUpdateExpr165: "limp_Expr" = None):
        self.field = field
        self.limp_RecordUpdateExpr = limp_RecordUpdateExpr
        self.limp_RecordUpdateExpr165 = limp_RecordUpdateExpr165
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def limp_RecordUpdateExpr(self):
        return self.__limp_RecordUpdateExpr

    @limp_RecordUpdateExpr.setter
    def limp_RecordUpdateExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordUpdateExpr__limp_RecordUpdateExpr", None)
        self.__limp_RecordUpdateExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr163"):
                opp_val = getattr(old_value, "limp_Expr163", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr163"):
                opp_val = getattr(value, "limp_Expr163", None)
                setattr(value, "limp_Expr163", self)

    @property
    def limp_RecordUpdateExpr165(self):
        return self.__limp_RecordUpdateExpr165

    @limp_RecordUpdateExpr165.setter
    def limp_RecordUpdateExpr165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordUpdateExpr__limp_RecordUpdateExpr165", None)
        self.__limp_RecordUpdateExpr165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr166"):
                opp_val = getattr(old_value, "limp_Expr166", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr166"):
                opp_val = getattr(value, "limp_Expr166", None)
                setattr(value, "limp_Expr166", self)

class limp_SecondInit(Expr):

    pass
class limp_ArrayExpr(Expr):

    pass
class limp_FunctionRef:

    pass
class limp_Equation:

    pass
class Attribute:

    pass
class limp_Postcondition(Attribute):

    def __init__(self, name: str, limp_Postcondition: "limp_Expr" = None):
        self.name = name
        self.limp_Postcondition = limp_Postcondition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_Postcondition(self):
        return self.__limp_Postcondition

    @limp_Postcondition.setter
    def limp_Postcondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_Postcondition__limp_Postcondition", None)
        self.__limp_Postcondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr60"):
                opp_val = getattr(old_value, "limp_Expr60", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr60"):
                opp_val = getattr(value, "limp_Expr60", None)
                setattr(value, "limp_Expr60", self)

class limp_Precondition(Attribute):

    def __init__(self, name: str, limp_Precondition: "limp_Expr" = None):
        self.name = name
        self.limp_Precondition = limp_Precondition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_Precondition(self):
        return self.__limp_Precondition

    @limp_Precondition.setter
    def limp_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_Precondition__limp_Precondition", None)
        self.__limp_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Expr58"):
                opp_val = getattr(old_value, "limp_Expr58", None)
                if opp_val == self:
                    setattr(old_value, "limp_Expr58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Expr58"):
                opp_val = getattr(value, "limp_Expr58", None)
                setattr(value, "limp_Expr58", self)

class limp_Attribute:

    pass
class limp_Else:

    pass
class limp_IdList:

    pass
class Equation:

    pass
class Statement:

    pass
class limp_ForStatement(Statement):

    pass
class limp_LabelStatement(Statement):

    def __init__(self, name: str, limp_LabelStatement: "limp_GotoStatement" = None):
        self.name = name
        self.limp_LabelStatement = limp_LabelStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_LabelStatement(self):
        return self.__limp_LabelStatement

    @limp_LabelStatement.setter
    def limp_LabelStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LabelStatement__limp_LabelStatement", None)
        self.__limp_LabelStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_GotoStatement"):
                opp_val = getattr(old_value, "limp_GotoStatement", None)
                if opp_val == self:
                    setattr(old_value, "limp_GotoStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_GotoStatement"):
                opp_val = getattr(value, "limp_GotoStatement", None)
                setattr(value, "limp_GotoStatement", self)

class limp_GotoStatement(Statement):

    pass
class limp_IfThenElseStatement(Statement):

    pass
class limp_ContinueStatement(Statement):

    pass
class limp_BreakStatement(Statement):

    pass
class limp_ReturnStatement(Statement):

    pass
class limp_AssignmentStatement(Statement, Equation):

    pass
class limp_WhileStatement(Statement):

    pass
class limp_VoidStatement(Statement, Equation):

    pass
class limp_Statement:

    pass
class limp_Uses(Attribute):

    pass
class limp_Define(Attribute):

    pass
class limp_DefineUseRef:

    pass
class limp_RecordFieldType:

    def __init__(self, fieldName: str, limp_RecordFieldType36: "limp_Type" = None, limp_RecordFieldType: "limp_RecordTypeDef" = None):
        self.fieldName = fieldName
        self.limp_RecordFieldType36 = limp_RecordFieldType36
        self.limp_RecordFieldType = limp_RecordFieldType
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def limp_RecordFieldType36(self):
        return self.__limp_RecordFieldType36

    @limp_RecordFieldType36.setter
    def limp_RecordFieldType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordFieldType__limp_RecordFieldType36", None)
        self.__limp_RecordFieldType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Type37"):
                opp_val = getattr(old_value, "limp_Type37", None)
                if opp_val == self:
                    setattr(old_value, "limp_Type37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Type37"):
                opp_val = getattr(value, "limp_Type37", None)
                setattr(value, "limp_Type37", self)

    @property
    def limp_RecordFieldType(self):
        return self.__limp_RecordFieldType

    @limp_RecordFieldType.setter
    def limp_RecordFieldType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_RecordFieldType__limp_RecordFieldType", None)
        self.__limp_RecordFieldType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_RecordTypeDef"):
                opp_val = getattr(old_value, "limp_RecordTypeDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_RecordTypeDef"):
                opp_val = getattr(value, "limp_RecordTypeDef", None)
                if opp_val is None:
                    setattr(value, "limp_RecordTypeDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VariableRef:

    pass
class limp_EnumValue(VariableRef):

    pass
class TypeDeclaration:

    pass
class limp_TypeAlias(TypeDeclaration):

    pass
class limp_RecordTypeDef(TypeDeclaration):

    pass
class limp_EnumTypeDef(TypeDeclaration):

    pass
class limp_LocalArg(VariableRef):

    pass
class limp_InputArg(VariableRef):

    pass
class limp_VariableRef:

    def __init__(self, name: str, limp_VariableRef: "limp_IdList" = None, limp_VariableRef178: "limp_InitExpr" = None, limp_VariableRef180: "limp_SecondInit" = None, limp_VariableRef182: "limp_IdExpr" = None):
        self.name = name
        self.limp_VariableRef = limp_VariableRef
        self.limp_VariableRef178 = limp_VariableRef178
        self.limp_VariableRef180 = limp_VariableRef180
        self.limp_VariableRef182 = limp_VariableRef182
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_VariableRef180(self):
        return self.__limp_VariableRef180

    @limp_VariableRef180.setter
    def limp_VariableRef180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_VariableRef__limp_VariableRef180", None)
        self.__limp_VariableRef180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_SecondInit"):
                opp_val = getattr(old_value, "limp_SecondInit", None)
                if opp_val == self:
                    setattr(old_value, "limp_SecondInit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_SecondInit"):
                opp_val = getattr(value, "limp_SecondInit", None)
                setattr(value, "limp_SecondInit", self)

    @property
    def limp_VariableRef182(self):
        return self.__limp_VariableRef182

    @limp_VariableRef182.setter
    def limp_VariableRef182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_VariableRef__limp_VariableRef182", None)
        self.__limp_VariableRef182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_IdExpr"):
                opp_val = getattr(old_value, "limp_IdExpr", None)
                if opp_val == self:
                    setattr(old_value, "limp_IdExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_IdExpr"):
                opp_val = getattr(value, "limp_IdExpr", None)
                setattr(value, "limp_IdExpr", self)

    @property
    def limp_VariableRef(self):
        return self.__limp_VariableRef

    @limp_VariableRef.setter
    def limp_VariableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_VariableRef__limp_VariableRef", None)
        self.__limp_VariableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_IdList105"):
                opp_val = getattr(old_value, "limp_IdList105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_IdList105"):
                opp_val = getattr(value, "limp_IdList105", None)
                if opp_val is None:
                    setattr(value, "limp_IdList105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def limp_VariableRef178(self):
        return self.__limp_VariableRef178

    @limp_VariableRef178.setter
    def limp_VariableRef178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_VariableRef__limp_VariableRef178", None)
        self.__limp_VariableRef178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_InitExpr"):
                opp_val = getattr(old_value, "limp_InitExpr", None)
                if opp_val == self:
                    setattr(old_value, "limp_InitExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_InitExpr"):
                opp_val = getattr(value, "limp_InitExpr", None)
                setattr(value, "limp_InitExpr", self)

class limp_Expr:

    pass
class limp_AbstractTypeDef(TypeDeclaration):

    pass
class limp_Type:

    pass
class limp_ArrayTypeDef(TypeDeclaration):

    def __init__(self, size: str, limp_ArrayTypeDef: "limp_Type" = None, limp_ArrayTypeDef107: "limp_ArrayExpr" = None, limp_ArrayTypeDef129: "limp_ArrayType" = None):
        self.size = size
        self.limp_ArrayTypeDef = limp_ArrayTypeDef
        self.limp_ArrayTypeDef107 = limp_ArrayTypeDef107
        self.limp_ArrayTypeDef129 = limp_ArrayTypeDef129
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def limp_ArrayTypeDef(self):
        return self.__limp_ArrayTypeDef

    @limp_ArrayTypeDef.setter
    def limp_ArrayTypeDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ArrayTypeDef__limp_ArrayTypeDef", None)
        self.__limp_ArrayTypeDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_Type"):
                opp_val = getattr(old_value, "limp_Type", None)
                if opp_val == self:
                    setattr(old_value, "limp_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_Type"):
                opp_val = getattr(value, "limp_Type", None)
                setattr(value, "limp_Type", self)

    @property
    def limp_ArrayTypeDef129(self):
        return self.__limp_ArrayTypeDef129

    @limp_ArrayTypeDef129.setter
    def limp_ArrayTypeDef129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ArrayTypeDef__limp_ArrayTypeDef129", None)
        self.__limp_ArrayTypeDef129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_ArrayType"):
                opp_val = getattr(old_value, "limp_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "limp_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_ArrayType"):
                opp_val = getattr(value, "limp_ArrayType", None)
                setattr(value, "limp_ArrayType", self)

    @property
    def limp_ArrayTypeDef107(self):
        return self.__limp_ArrayTypeDef107

    @limp_ArrayTypeDef107.setter
    def limp_ArrayTypeDef107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ArrayTypeDef__limp_ArrayTypeDef107", None)
        self.__limp_ArrayTypeDef107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_ArrayExpr"):
                opp_val = getattr(old_value, "limp_ArrayExpr", None)
                if opp_val == self:
                    setattr(old_value, "limp_ArrayExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_ArrayExpr"):
                opp_val = getattr(value, "limp_ArrayExpr", None)
                setattr(value, "limp_ArrayExpr", self)

class limp_OutputArg(VariableRef):

    pass
class limp_InputArgList:

    pass
class FunctionRef:

    pass
class limp_StatementBlock:

    pass
class limp_EquationBlock:

    pass
class limp_VarBlock:

    pass
class limp_AttributeBlock:

    pass
class limp_OutputArgList:

    pass
class Declaration:

    pass
class limp_ExternalProcedure(Declaration, FunctionRef):

    def __init__(self, name: str, limp_ExternalProcedure: "limp_InputArgList" = None, limp_ExternalProcedure7: "limp_OutputArgList" = None, limp_ExternalProcedure9: "limp_AttributeBlock" = None):
        self.name = name
        self.limp_ExternalProcedure = limp_ExternalProcedure
        self.limp_ExternalProcedure7 = limp_ExternalProcedure7
        self.limp_ExternalProcedure9 = limp_ExternalProcedure9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_ExternalProcedure(self):
        return self.__limp_ExternalProcedure

    @limp_ExternalProcedure.setter
    def limp_ExternalProcedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ExternalProcedure__limp_ExternalProcedure", None)
        self.__limp_ExternalProcedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_InputArgList5"):
                opp_val = getattr(old_value, "limp_InputArgList5", None)
                if opp_val == self:
                    setattr(old_value, "limp_InputArgList5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_InputArgList5"):
                opp_val = getattr(value, "limp_InputArgList5", None)
                setattr(value, "limp_InputArgList5", self)

    @property
    def limp_ExternalProcedure7(self):
        return self.__limp_ExternalProcedure7

    @limp_ExternalProcedure7.setter
    def limp_ExternalProcedure7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ExternalProcedure__limp_ExternalProcedure7", None)
        self.__limp_ExternalProcedure7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_OutputArgList"):
                opp_val = getattr(old_value, "limp_OutputArgList", None)
                if opp_val == self:
                    setattr(old_value, "limp_OutputArgList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_OutputArgList"):
                opp_val = getattr(value, "limp_OutputArgList", None)
                setattr(value, "limp_OutputArgList", self)

    @property
    def limp_ExternalProcedure9(self):
        return self.__limp_ExternalProcedure9

    @limp_ExternalProcedure9.setter
    def limp_ExternalProcedure9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ExternalProcedure__limp_ExternalProcedure9", None)
        self.__limp_ExternalProcedure9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_AttributeBlock"):
                opp_val = getattr(old_value, "limp_AttributeBlock", None)
                if opp_val == self:
                    setattr(old_value, "limp_AttributeBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_AttributeBlock"):
                opp_val = getattr(value, "limp_AttributeBlock", None)
                setattr(value, "limp_AttributeBlock", self)

class limp_LocalProcedure(Declaration, FunctionRef):

    def __init__(self, name: str, limp_LocalProcedure: "limp_InputArgList" = None, limp_LocalProcedure22: "limp_OutputArgList" = None, limp_LocalProcedure25: "limp_VarBlock" = None, limp_LocalProcedure28: "limp_AttributeBlock" = None, limp_LocalProcedure31: "limp_StatementBlock" = None):
        self.name = name
        self.limp_LocalProcedure = limp_LocalProcedure
        self.limp_LocalProcedure22 = limp_LocalProcedure22
        self.limp_LocalProcedure25 = limp_LocalProcedure25
        self.limp_LocalProcedure28 = limp_LocalProcedure28
        self.limp_LocalProcedure31 = limp_LocalProcedure31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_LocalProcedure25(self):
        return self.__limp_LocalProcedure25

    @limp_LocalProcedure25.setter
    def limp_LocalProcedure25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalProcedure__limp_LocalProcedure25", None)
        self.__limp_LocalProcedure25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_VarBlock26"):
                opp_val = getattr(old_value, "limp_VarBlock26", None)
                if opp_val == self:
                    setattr(old_value, "limp_VarBlock26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_VarBlock26"):
                opp_val = getattr(value, "limp_VarBlock26", None)
                setattr(value, "limp_VarBlock26", self)

    @property
    def limp_LocalProcedure22(self):
        return self.__limp_LocalProcedure22

    @limp_LocalProcedure22.setter
    def limp_LocalProcedure22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalProcedure__limp_LocalProcedure22", None)
        self.__limp_LocalProcedure22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_OutputArgList23"):
                opp_val = getattr(old_value, "limp_OutputArgList23", None)
                if opp_val == self:
                    setattr(old_value, "limp_OutputArgList23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_OutputArgList23"):
                opp_val = getattr(value, "limp_OutputArgList23", None)
                setattr(value, "limp_OutputArgList23", self)

    @property
    def limp_LocalProcedure28(self):
        return self.__limp_LocalProcedure28

    @limp_LocalProcedure28.setter
    def limp_LocalProcedure28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalProcedure__limp_LocalProcedure28", None)
        self.__limp_LocalProcedure28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_AttributeBlock29"):
                opp_val = getattr(old_value, "limp_AttributeBlock29", None)
                if opp_val == self:
                    setattr(old_value, "limp_AttributeBlock29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_AttributeBlock29"):
                opp_val = getattr(value, "limp_AttributeBlock29", None)
                setattr(value, "limp_AttributeBlock29", self)

    @property
    def limp_LocalProcedure(self):
        return self.__limp_LocalProcedure

    @limp_LocalProcedure.setter
    def limp_LocalProcedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalProcedure__limp_LocalProcedure", None)
        self.__limp_LocalProcedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_InputArgList20"):
                opp_val = getattr(old_value, "limp_InputArgList20", None)
                if opp_val == self:
                    setattr(old_value, "limp_InputArgList20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_InputArgList20"):
                opp_val = getattr(value, "limp_InputArgList20", None)
                setattr(value, "limp_InputArgList20", self)

    @property
    def limp_LocalProcedure31(self):
        return self.__limp_LocalProcedure31

    @limp_LocalProcedure31.setter
    def limp_LocalProcedure31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalProcedure__limp_LocalProcedure31", None)
        self.__limp_LocalProcedure31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_StatementBlock"):
                opp_val = getattr(old_value, "limp_StatementBlock", None)
                if opp_val == self:
                    setattr(old_value, "limp_StatementBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_StatementBlock"):
                opp_val = getattr(value, "limp_StatementBlock", None)
                setattr(value, "limp_StatementBlock", self)

class limp_TypeDeclaration(Declaration):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class limp_ConstantDeclaration(Declaration, VariableRef):

    pass
class limp_Import(Declaration):

    def __init__(self, importURI: str):
        self.importURI = importURI
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

class limp_LocalFunction(Declaration, FunctionRef):

    def __init__(self, name: str, limp_LocalFunction: "limp_InputArgList" = None, limp_LocalFunction13: "limp_OutputArg" = None, limp_LocalFunction16: "limp_VarBlock" = None, limp_LocalFunction18: "limp_EquationBlock" = None):
        self.name = name
        self.limp_LocalFunction = limp_LocalFunction
        self.limp_LocalFunction13 = limp_LocalFunction13
        self.limp_LocalFunction16 = limp_LocalFunction16
        self.limp_LocalFunction18 = limp_LocalFunction18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_LocalFunction13(self):
        return self.__limp_LocalFunction13

    @limp_LocalFunction13.setter
    def limp_LocalFunction13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalFunction__limp_LocalFunction13", None)
        self.__limp_LocalFunction13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_OutputArg14"):
                opp_val = getattr(old_value, "limp_OutputArg14", None)
                if opp_val == self:
                    setattr(old_value, "limp_OutputArg14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_OutputArg14"):
                opp_val = getattr(value, "limp_OutputArg14", None)
                setattr(value, "limp_OutputArg14", self)

    @property
    def limp_LocalFunction(self):
        return self.__limp_LocalFunction

    @limp_LocalFunction.setter
    def limp_LocalFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalFunction__limp_LocalFunction", None)
        self.__limp_LocalFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_InputArgList11"):
                opp_val = getattr(old_value, "limp_InputArgList11", None)
                if opp_val == self:
                    setattr(old_value, "limp_InputArgList11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_InputArgList11"):
                opp_val = getattr(value, "limp_InputArgList11", None)
                setattr(value, "limp_InputArgList11", self)

    @property
    def limp_LocalFunction18(self):
        return self.__limp_LocalFunction18

    @limp_LocalFunction18.setter
    def limp_LocalFunction18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalFunction__limp_LocalFunction18", None)
        self.__limp_LocalFunction18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_EquationBlock"):
                opp_val = getattr(old_value, "limp_EquationBlock", None)
                if opp_val == self:
                    setattr(old_value, "limp_EquationBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_EquationBlock"):
                opp_val = getattr(value, "limp_EquationBlock", None)
                setattr(value, "limp_EquationBlock", self)

    @property
    def limp_LocalFunction16(self):
        return self.__limp_LocalFunction16

    @limp_LocalFunction16.setter
    def limp_LocalFunction16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_LocalFunction__limp_LocalFunction16", None)
        self.__limp_LocalFunction16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_VarBlock"):
                opp_val = getattr(old_value, "limp_VarBlock", None)
                if opp_val == self:
                    setattr(old_value, "limp_VarBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_VarBlock"):
                opp_val = getattr(value, "limp_VarBlock", None)
                setattr(value, "limp_VarBlock", self)

class limp_GlobalDeclaration(Declaration, VariableRef):

    pass
class limp_ExternalFunction(Declaration, FunctionRef):

    def __init__(self, name: str, limp_ExternalFunction: "limp_InputArgList" = None, limp_ExternalFunction3: "limp_OutputArg" = None):
        self.name = name
        self.limp_ExternalFunction = limp_ExternalFunction
        self.limp_ExternalFunction3 = limp_ExternalFunction3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def limp_ExternalFunction3(self):
        return self.__limp_ExternalFunction3

    @limp_ExternalFunction3.setter
    def limp_ExternalFunction3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ExternalFunction__limp_ExternalFunction3", None)
        self.__limp_ExternalFunction3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_OutputArg"):
                opp_val = getattr(old_value, "limp_OutputArg", None)
                if opp_val == self:
                    setattr(old_value, "limp_OutputArg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_OutputArg"):
                opp_val = getattr(value, "limp_OutputArg", None)
                setattr(value, "limp_OutputArg", self)

    @property
    def limp_ExternalFunction(self):
        return self.__limp_ExternalFunction

    @limp_ExternalFunction.setter
    def limp_ExternalFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_limp_ExternalFunction__limp_ExternalFunction", None)
        self.__limp_ExternalFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "limp_InputArgList"):
                opp_val = getattr(old_value, "limp_InputArgList", None)
                if opp_val == self:
                    setattr(old_value, "limp_InputArgList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "limp_InputArgList"):
                opp_val = getattr(value, "limp_InputArgList", None)
                setattr(value, "limp_InputArgList", self)

class limp_Comment(Declaration):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class limp_Declaration:

    pass
class limp_Specification:

    pass
from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class GenericExpression:

    pass
class swrtj_BooleanExpression(GenericExpression):

    pass
class Parameter:

    pass
class swrtj_FormalParameter(Parameter):

    pass
class swrtj_Expression(GenericExpression):

    def __init__(self, sign: str, operatorList: str, swrtj_Expression: set["swrtj_DottedExpression"] = None):
        self.sign = sign
        self.operatorList = operatorList
        self.swrtj_Expression = swrtj_Expression if swrtj_Expression is not None else set()
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def operatorList(self) -> str:
        return self.__operatorList

    @operatorList.setter
    def operatorList(self, operatorList: str):
        self.__operatorList = operatorList

    @property
    def swrtj_Expression(self):
        return self.__swrtj_Expression

    @swrtj_Expression.setter
    def swrtj_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Expression__swrtj_Expression", None)
        self.__swrtj_Expression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swrtj_DottedExpression161"):
                    opp_val = getattr(item, "swrtj_DottedExpression161", None)
                    
                    if opp_val == self:
                        setattr(item, "swrtj_DottedExpression161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swrtj_DottedExpression161"):
                    opp_val = getattr(item, "swrtj_DottedExpression161", None)
                    
                    setattr(item, "swrtj_DottedExpression161", self)
                    

class swrtj_LocalParameter(Parameter):

    pass
class Method:

    pass
class swrtj_ProvidedMethod(Method):

    def __init__(self, isSynchronized: bool, swrtj_ProvidedMethod: "swrtj_Block" = None, swrtj_ProvidedMethod153: "swrtj_ReturnStatement" = None):
        self.isSynchronized = isSynchronized
        self.swrtj_ProvidedMethod = swrtj_ProvidedMethod
        self.swrtj_ProvidedMethod153 = swrtj_ProvidedMethod153
        
    @property
    def isSynchronized(self) -> bool:
        return self.__isSynchronized

    @isSynchronized.setter
    def isSynchronized(self, isSynchronized: bool):
        self.__isSynchronized = isSynchronized

    @property
    def swrtj_ProvidedMethod(self):
        return self.__swrtj_ProvidedMethod

    @swrtj_ProvidedMethod.setter
    def swrtj_ProvidedMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_ProvidedMethod__swrtj_ProvidedMethod", None)
        self.__swrtj_ProvidedMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Block151"):
                opp_val = getattr(old_value, "swrtj_Block151", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Block151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Block151"):
                opp_val = getattr(value, "swrtj_Block151", None)
                setattr(value, "swrtj_Block151", self)

    @property
    def swrtj_ProvidedMethod153(self):
        return self.__swrtj_ProvidedMethod153

    @swrtj_ProvidedMethod153.setter
    def swrtj_ProvidedMethod153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_ProvidedMethod__swrtj_ProvidedMethod153", None)
        self.__swrtj_ProvidedMethod153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_ReturnStatement154"):
                opp_val = getattr(old_value, "swrtj_ReturnStatement154", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_ReturnStatement154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_ReturnStatement154"):
                opp_val = getattr(value, "swrtj_ReturnStatement154", None)
                setattr(value, "swrtj_ReturnStatement154", self)

class swrtj_RequiredMethod(Method):

    pass
class Field:

    pass
class swrtj_RequiredField(Field):

    pass
class swrtj_FieldDeclaration(Field):

    def __init__(self, modifier: str):
        self.modifier = modifier
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

class TraitOperation:

    pass
class swrtj_TraitAlias(TraitOperation):

    pass
class swrtj_TraitMethodRename(TraitOperation):

    pass
class swrtj_TraitFieldRename(TraitOperation):

    pass
class swrtj_TraitExclude(TraitOperation):

    pass
class RecordOperation:

    pass
class swrtj_RecordRename(RecordOperation):

    pass
class swrtj_RecordExclude(RecordOperation):

    pass
class Message:

    pass
class swrtj_FieldAccess(Message):

    pass
class swrtj_MethodInvocation(Message):

    pass
class Start:

    pass
class swrtj_BooleanConstant(Start):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class swrtj_StringConstant(Start):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class swrtj_ParameterAssignment(Start):

    pass
class swrtj_Input(Start):

    def __init__(self, input: bool):
        self.input = input
        
    @property
    def input(self) -> bool:
        return self.__input

    @input.setter
    def input(self, input: bool):
        self.__input = input

class swrtj_ConstructorInvocation(Start):

    pass
class swrtj_Number(Start):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class swrtj_This(Start):

    def __init__(self, this: bool):
        self.this = this
        
    @property
    def this(self) -> bool:
        return self.__this

    @this.setter
    def this(self, this: bool):
        self.__this = this

class swrtj_Args(Start):

    def __init__(self, args: bool):
        self.args = args
        
    @property
    def args(self) -> bool:
        return self.__args

    @args.setter
    def args(self, args: bool):
        self.__args = args

class swrtj_ParameterReference(Start):

    pass
class swrtj_NestedExpression(Start):

    pass
class swrtj_Output(Start):

    def __init__(self, output: bool):
        self.output = output
        
    @property
    def output(self) -> bool:
        return self.__output

    @output.setter
    def output(self, output: bool):
        self.__output = output

class swrtj_Cast(Start):

    pass
class swrtj_Null(Start):

    def __init__(self, null: bool):
        self.null = null
        
    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

class swrtj_Message:

    pass
class swrtj_Start:

    pass
class swrtj_DottedExpression:

    pass
class swrtj_CompareOperator:

    def __init__(self, operator: str, swrtj_CompareOperator: "swrtj_SimpleComparation" = None):
        self.operator = operator
        self.swrtj_CompareOperator = swrtj_CompareOperator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def swrtj_CompareOperator(self):
        return self.__swrtj_CompareOperator

    @swrtj_CompareOperator.setter
    def swrtj_CompareOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_CompareOperator__swrtj_CompareOperator", None)
        self.__swrtj_CompareOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_SimpleComparation85"):
                opp_val = getattr(old_value, "swrtj_SimpleComparation85", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_SimpleComparation85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_SimpleComparation85"):
                opp_val = getattr(value, "swrtj_SimpleComparation85", None)
                setattr(value, "swrtj_SimpleComparation85", self)

class Statement:

    pass
class swrtj_WhileStatement(Statement):

    pass
class swrtj_IfThenElseStatement(Statement):

    pass
class swrtj_ExpressionStatement(Statement):

    pass
class swrtj_Statement:

    pass
class swrtj_GenericExpression:

    pass
class swrtj_ReturnStatement:

    pass
class AtomicBooleanExpression:

    pass
class swrtj_NestedBooleanExpression(AtomicBooleanExpression):

    pass
class swrtj_SimpleComparation(AtomicBooleanExpression):

    pass
class swrtj_AtomicBooleanExpression:

    def __init__(self, negated: bool, swrtj_AtomicBooleanExpression: "swrtj_BooleanExpression" = None):
        self.negated = negated
        self.swrtj_AtomicBooleanExpression = swrtj_AtomicBooleanExpression
        
    @property
    def negated(self) -> bool:
        return self.__negated

    @negated.setter
    def negated(self, negated: bool):
        self.__negated = negated

    @property
    def swrtj_AtomicBooleanExpression(self):
        return self.__swrtj_AtomicBooleanExpression

    @swrtj_AtomicBooleanExpression.setter
    def swrtj_AtomicBooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_AtomicBooleanExpression__swrtj_AtomicBooleanExpression", None)
        self.__swrtj_AtomicBooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_BooleanExpression"):
                opp_val = getattr(old_value, "swrtj_BooleanExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_BooleanExpression"):
                opp_val = getattr(value, "swrtj_BooleanExpression", None)
                if opp_val is None:
                    setattr(value, "swrtj_BooleanExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swrtj_BooleanOperator:

    def __init__(self, operator: str, swrtj_BooleanOperator: "swrtj_BooleanExpression" = None):
        self.operator = operator
        self.swrtj_BooleanOperator = swrtj_BooleanOperator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def swrtj_BooleanOperator(self):
        return self.__swrtj_BooleanOperator

    @swrtj_BooleanOperator.setter
    def swrtj_BooleanOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_BooleanOperator__swrtj_BooleanOperator", None)
        self.__swrtj_BooleanOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_BooleanExpression157"):
                opp_val = getattr(old_value, "swrtj_BooleanExpression157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_BooleanExpression157"):
                opp_val = getattr(value, "swrtj_BooleanExpression157", None)
                if opp_val is None:
                    setattr(value, "swrtj_BooleanExpression157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swrtj_FieldName:

    def __init__(self, name: str, swrtj_FieldName: "swrtj_Field" = None, swrtj_FieldName127: "swrtj_RecordExclude" = None, swrtj_FieldName129: "swrtj_RecordRename" = None, swrtj_FieldName120: "swrtj_FieldAccess" = None, swrtj_FieldName132: "swrtj_RecordRename" = None, swrtj_FieldName146: "swrtj_TraitFieldRename" = None, swrtj_FieldName149: "swrtj_TraitFieldRename" = None):
        self.name = name
        self.swrtj_FieldName = swrtj_FieldName
        self.swrtj_FieldName127 = swrtj_FieldName127
        self.swrtj_FieldName129 = swrtj_FieldName129
        self.swrtj_FieldName120 = swrtj_FieldName120
        self.swrtj_FieldName132 = swrtj_FieldName132
        self.swrtj_FieldName146 = swrtj_FieldName146
        self.swrtj_FieldName149 = swrtj_FieldName149
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swrtj_FieldName127(self):
        return self.__swrtj_FieldName127

    @swrtj_FieldName127.setter
    def swrtj_FieldName127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName127", None)
        self.__swrtj_FieldName127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_RecordExclude"):
                opp_val = getattr(old_value, "swrtj_RecordExclude", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_RecordExclude", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_RecordExclude"):
                opp_val = getattr(value, "swrtj_RecordExclude", None)
                setattr(value, "swrtj_RecordExclude", self)

    @property
    def swrtj_FieldName129(self):
        return self.__swrtj_FieldName129

    @swrtj_FieldName129.setter
    def swrtj_FieldName129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName129", None)
        self.__swrtj_FieldName129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_RecordRename"):
                opp_val = getattr(old_value, "swrtj_RecordRename", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_RecordRename", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_RecordRename"):
                opp_val = getattr(value, "swrtj_RecordRename", None)
                setattr(value, "swrtj_RecordRename", self)

    @property
    def swrtj_FieldName146(self):
        return self.__swrtj_FieldName146

    @swrtj_FieldName146.setter
    def swrtj_FieldName146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName146", None)
        self.__swrtj_FieldName146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitFieldRename"):
                opp_val = getattr(old_value, "swrtj_TraitFieldRename", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitFieldRename", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitFieldRename"):
                opp_val = getattr(value, "swrtj_TraitFieldRename", None)
                setattr(value, "swrtj_TraitFieldRename", self)

    @property
    def swrtj_FieldName149(self):
        return self.__swrtj_FieldName149

    @swrtj_FieldName149.setter
    def swrtj_FieldName149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName149", None)
        self.__swrtj_FieldName149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitFieldRename148"):
                opp_val = getattr(old_value, "swrtj_TraitFieldRename148", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitFieldRename148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitFieldRename148"):
                opp_val = getattr(value, "swrtj_TraitFieldRename148", None)
                setattr(value, "swrtj_TraitFieldRename148", self)

    @property
    def swrtj_FieldName(self):
        return self.__swrtj_FieldName

    @swrtj_FieldName.setter
    def swrtj_FieldName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName", None)
        self.__swrtj_FieldName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Field41"):
                opp_val = getattr(old_value, "swrtj_Field41", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Field41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Field41"):
                opp_val = getattr(value, "swrtj_Field41", None)
                setattr(value, "swrtj_Field41", self)

    @property
    def swrtj_FieldName120(self):
        return self.__swrtj_FieldName120

    @swrtj_FieldName120.setter
    def swrtj_FieldName120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName120", None)
        self.__swrtj_FieldName120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_FieldAccess"):
                opp_val = getattr(old_value, "swrtj_FieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_FieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_FieldAccess"):
                opp_val = getattr(value, "swrtj_FieldAccess", None)
                setattr(value, "swrtj_FieldAccess", self)

    @property
    def swrtj_FieldName132(self):
        return self.__swrtj_FieldName132

    @swrtj_FieldName132.setter
    def swrtj_FieldName132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_FieldName__swrtj_FieldName132", None)
        self.__swrtj_FieldName132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_RecordRename131"):
                opp_val = getattr(old_value, "swrtj_RecordRename131", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_RecordRename131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_RecordRename131"):
                opp_val = getattr(value, "swrtj_RecordRename131", None)
                setattr(value, "swrtj_RecordRename131", self)

class swrtj_Type:

    def __init__(self, primitiveType: str, swrtj_Type44: "swrtj_Method" = None, swrtj_Type: "swrtj_Field" = None, swrtj_Type58: "swrtj_Parameter" = None, swrtj_Type60: "swrtj_Interface" = None, swrtj_Type108: "swrtj_Cast" = None):
        self.primitiveType = primitiveType
        self.swrtj_Type44 = swrtj_Type44
        self.swrtj_Type = swrtj_Type
        self.swrtj_Type58 = swrtj_Type58
        self.swrtj_Type60 = swrtj_Type60
        self.swrtj_Type108 = swrtj_Type108
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def swrtj_Type44(self):
        return self.__swrtj_Type44

    @swrtj_Type44.setter
    def swrtj_Type44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Type__swrtj_Type44", None)
        self.__swrtj_Type44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Method43"):
                opp_val = getattr(old_value, "swrtj_Method43", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Method43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Method43"):
                opp_val = getattr(value, "swrtj_Method43", None)
                setattr(value, "swrtj_Method43", self)

    @property
    def swrtj_Type60(self):
        return self.__swrtj_Type60

    @swrtj_Type60.setter
    def swrtj_Type60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Type__swrtj_Type60", None)
        self.__swrtj_Type60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Interface61"):
                opp_val = getattr(old_value, "swrtj_Interface61", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Interface61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Interface61"):
                opp_val = getattr(value, "swrtj_Interface61", None)
                setattr(value, "swrtj_Interface61", self)

    @property
    def swrtj_Type(self):
        return self.__swrtj_Type

    @swrtj_Type.setter
    def swrtj_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Type__swrtj_Type", None)
        self.__swrtj_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Field39"):
                opp_val = getattr(old_value, "swrtj_Field39", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Field39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Field39"):
                opp_val = getattr(value, "swrtj_Field39", None)
                setattr(value, "swrtj_Field39", self)

    @property
    def swrtj_Type58(self):
        return self.__swrtj_Type58

    @swrtj_Type58.setter
    def swrtj_Type58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Type__swrtj_Type58", None)
        self.__swrtj_Type58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Parameter57"):
                opp_val = getattr(old_value, "swrtj_Parameter57", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Parameter57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Parameter57"):
                opp_val = getattr(value, "swrtj_Parameter57", None)
                setattr(value, "swrtj_Parameter57", self)

    @property
    def swrtj_Type108(self):
        return self.__swrtj_Type108

    @swrtj_Type108.setter
    def swrtj_Type108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Type__swrtj_Type108", None)
        self.__swrtj_Type108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Cast"):
                opp_val = getattr(old_value, "swrtj_Cast", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Cast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Cast"):
                opp_val = getattr(value, "swrtj_Cast", None)
                setattr(value, "swrtj_Cast", self)

class TraitElement:

    pass
class swrtj_TraitElement:

    pass
class BaseTrait:

    pass
class swrtj_TraitName(BaseTrait):

    pass
class swrtj_NestedTraitExpression(BaseTrait):

    pass
class swrtj_AnonimousTrait(BaseTrait):

    pass
class swrtj_TraitOperation:

    pass
class swrtj_BaseTrait:

    pass
class swrtj_Field(TraitElement):

    pass
class BaseRecord:

    pass
class swrtj_RecordName(BaseRecord):

    pass
class swrtj_NestedRecordExpression(BaseRecord):

    pass
class swrtj_AnonimousRecord(BaseRecord):

    pass
class swrtj_RecordOperation:

    pass
class swrtj_Parameter:

    def __init__(self, name: str, swrtj_Parameter: "swrtj_Method" = None, swrtj_Parameter51: "swrtj_Constructor" = None, swrtj_Parameter57: "swrtj_Type" = None, swrtj_Parameter64: "swrtj_Block" = None, swrtj_Parameter101: "swrtj_ParameterReference" = None, swrtj_Parameter122: "swrtj_ParameterAssignment" = None):
        self.name = name
        self.swrtj_Parameter = swrtj_Parameter
        self.swrtj_Parameter51 = swrtj_Parameter51
        self.swrtj_Parameter57 = swrtj_Parameter57
        self.swrtj_Parameter64 = swrtj_Parameter64
        self.swrtj_Parameter101 = swrtj_Parameter101
        self.swrtj_Parameter122 = swrtj_Parameter122
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swrtj_Parameter57(self):
        return self.__swrtj_Parameter57

    @swrtj_Parameter57.setter
    def swrtj_Parameter57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter57", None)
        self.__swrtj_Parameter57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Type58"):
                opp_val = getattr(old_value, "swrtj_Type58", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Type58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Type58"):
                opp_val = getattr(value, "swrtj_Type58", None)
                setattr(value, "swrtj_Type58", self)

    @property
    def swrtj_Parameter101(self):
        return self.__swrtj_Parameter101

    @swrtj_Parameter101.setter
    def swrtj_Parameter101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter101", None)
        self.__swrtj_Parameter101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_ParameterReference"):
                opp_val = getattr(old_value, "swrtj_ParameterReference", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_ParameterReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_ParameterReference"):
                opp_val = getattr(value, "swrtj_ParameterReference", None)
                setattr(value, "swrtj_ParameterReference", self)

    @property
    def swrtj_Parameter64(self):
        return self.__swrtj_Parameter64

    @swrtj_Parameter64.setter
    def swrtj_Parameter64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter64", None)
        self.__swrtj_Parameter64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Block63"):
                opp_val = getattr(old_value, "swrtj_Block63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Block63"):
                opp_val = getattr(value, "swrtj_Block63", None)
                if opp_val is None:
                    setattr(value, "swrtj_Block63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swrtj_Parameter51(self):
        return self.__swrtj_Parameter51

    @swrtj_Parameter51.setter
    def swrtj_Parameter51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter51", None)
        self.__swrtj_Parameter51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Constructor50"):
                opp_val = getattr(old_value, "swrtj_Constructor50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Constructor50"):
                opp_val = getattr(value, "swrtj_Constructor50", None)
                if opp_val is None:
                    setattr(value, "swrtj_Constructor50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swrtj_Parameter(self):
        return self.__swrtj_Parameter

    @swrtj_Parameter.setter
    def swrtj_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter", None)
        self.__swrtj_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Method48"):
                opp_val = getattr(old_value, "swrtj_Method48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Method48"):
                opp_val = getattr(value, "swrtj_Method48", None)
                if opp_val is None:
                    setattr(value, "swrtj_Method48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swrtj_Parameter122(self):
        return self.__swrtj_Parameter122

    @swrtj_Parameter122.setter
    def swrtj_Parameter122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Parameter__swrtj_Parameter122", None)
        self.__swrtj_Parameter122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_ParameterAssignment"):
                opp_val = getattr(old_value, "swrtj_ParameterAssignment", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_ParameterAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_ParameterAssignment"):
                opp_val = getattr(value, "swrtj_ParameterAssignment", None)
                setattr(value, "swrtj_ParameterAssignment", self)

class swrtj_MethodName:

    def __init__(self, name: str, swrtj_MethodName: "swrtj_Method" = None, swrtj_MethodName115: "swrtj_MethodInvocation" = None, swrtj_MethodName134: "swrtj_TraitExclude" = None, swrtj_MethodName136: "swrtj_TraitAlias" = None, swrtj_MethodName139: "swrtj_TraitAlias" = None, swrtj_MethodName144: "swrtj_TraitMethodRename" = None, swrtj_MethodName141: "swrtj_TraitMethodRename" = None):
        self.name = name
        self.swrtj_MethodName = swrtj_MethodName
        self.swrtj_MethodName115 = swrtj_MethodName115
        self.swrtj_MethodName134 = swrtj_MethodName134
        self.swrtj_MethodName136 = swrtj_MethodName136
        self.swrtj_MethodName139 = swrtj_MethodName139
        self.swrtj_MethodName144 = swrtj_MethodName144
        self.swrtj_MethodName141 = swrtj_MethodName141
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swrtj_MethodName(self):
        return self.__swrtj_MethodName

    @swrtj_MethodName.setter
    def swrtj_MethodName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName", None)
        self.__swrtj_MethodName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Method46"):
                opp_val = getattr(old_value, "swrtj_Method46", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Method46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Method46"):
                opp_val = getattr(value, "swrtj_Method46", None)
                setattr(value, "swrtj_Method46", self)

    @property
    def swrtj_MethodName144(self):
        return self.__swrtj_MethodName144

    @swrtj_MethodName144.setter
    def swrtj_MethodName144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName144", None)
        self.__swrtj_MethodName144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitMethodRename143"):
                opp_val = getattr(old_value, "swrtj_TraitMethodRename143", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitMethodRename143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitMethodRename143"):
                opp_val = getattr(value, "swrtj_TraitMethodRename143", None)
                setattr(value, "swrtj_TraitMethodRename143", self)

    @property
    def swrtj_MethodName115(self):
        return self.__swrtj_MethodName115

    @swrtj_MethodName115.setter
    def swrtj_MethodName115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName115", None)
        self.__swrtj_MethodName115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_MethodInvocation"):
                opp_val = getattr(old_value, "swrtj_MethodInvocation", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_MethodInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_MethodInvocation"):
                opp_val = getattr(value, "swrtj_MethodInvocation", None)
                setattr(value, "swrtj_MethodInvocation", self)

    @property
    def swrtj_MethodName141(self):
        return self.__swrtj_MethodName141

    @swrtj_MethodName141.setter
    def swrtj_MethodName141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName141", None)
        self.__swrtj_MethodName141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitMethodRename"):
                opp_val = getattr(old_value, "swrtj_TraitMethodRename", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitMethodRename", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitMethodRename"):
                opp_val = getattr(value, "swrtj_TraitMethodRename", None)
                setattr(value, "swrtj_TraitMethodRename", self)

    @property
    def swrtj_MethodName134(self):
        return self.__swrtj_MethodName134

    @swrtj_MethodName134.setter
    def swrtj_MethodName134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName134", None)
        self.__swrtj_MethodName134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitExclude"):
                opp_val = getattr(old_value, "swrtj_TraitExclude", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitExclude", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitExclude"):
                opp_val = getattr(value, "swrtj_TraitExclude", None)
                setattr(value, "swrtj_TraitExclude", self)

    @property
    def swrtj_MethodName136(self):
        return self.__swrtj_MethodName136

    @swrtj_MethodName136.setter
    def swrtj_MethodName136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName136", None)
        self.__swrtj_MethodName136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitAlias"):
                opp_val = getattr(old_value, "swrtj_TraitAlias", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitAlias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitAlias"):
                opp_val = getattr(value, "swrtj_TraitAlias", None)
                setattr(value, "swrtj_TraitAlias", self)

    @property
    def swrtj_MethodName139(self):
        return self.__swrtj_MethodName139

    @swrtj_MethodName139.setter
    def swrtj_MethodName139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_MethodName__swrtj_MethodName139", None)
        self.__swrtj_MethodName139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_TraitAlias138"):
                opp_val = getattr(old_value, "swrtj_TraitAlias138", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_TraitAlias138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_TraitAlias138"):
                opp_val = getattr(value, "swrtj_TraitAlias138", None)
                setattr(value, "swrtj_TraitAlias138", self)

class swrtj_Constructor:

    def __init__(self, name: str, swrtj_Constructor: "swrtj_Class" = None, swrtj_Constructor50: set["swrtj_Parameter"] = None, swrtj_Constructor53: "swrtj_Block" = None):
        self.name = name
        self.swrtj_Constructor = swrtj_Constructor
        self.swrtj_Constructor50 = swrtj_Constructor50 if swrtj_Constructor50 is not None else set()
        self.swrtj_Constructor53 = swrtj_Constructor53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swrtj_Constructor50(self):
        return self.__swrtj_Constructor50

    @swrtj_Constructor50.setter
    def swrtj_Constructor50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Constructor__swrtj_Constructor50", None)
        self.__swrtj_Constructor50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swrtj_Parameter51"):
                    opp_val = getattr(item, "swrtj_Parameter51", None)
                    
                    if opp_val == self:
                        setattr(item, "swrtj_Parameter51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swrtj_Parameter51"):
                    opp_val = getattr(item, "swrtj_Parameter51", None)
                    
                    setattr(item, "swrtj_Parameter51", self)
                    

    @property
    def swrtj_Constructor(self):
        return self.__swrtj_Constructor

    @swrtj_Constructor.setter
    def swrtj_Constructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Constructor__swrtj_Constructor", None)
        self.__swrtj_Constructor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Class18"):
                opp_val = getattr(old_value, "swrtj_Class18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Class18"):
                opp_val = getattr(value, "swrtj_Class18", None)
                if opp_val is None:
                    setattr(value, "swrtj_Class18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swrtj_Constructor53(self):
        return self.__swrtj_Constructor53

    @swrtj_Constructor53.setter
    def swrtj_Constructor53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Constructor__swrtj_Constructor53", None)
        self.__swrtj_Constructor53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_Block54"):
                opp_val = getattr(old_value, "swrtj_Block54", None)
                if opp_val == self:
                    setattr(old_value, "swrtj_Block54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_Block54"):
                opp_val = getattr(value, "swrtj_Block54", None)
                setattr(value, "swrtj_Block54", self)

class swrtj_TraitExpression:

    pass
class swrtj_RecordExpression:

    pass
class swrtj_Method(TraitElement):

    pass
class Element:

    pass
class swrtj_Trait(Element):

    pass
class swrtj_Class(Element):

    pass
class swrtj_Record(Element):

    pass
class swrtj_Interface(Element):

    pass
class swrtj_Element:

    def __init__(self, construct: str, name: str, swrtj_Element: "swrtj_File" = None):
        self.construct = construct
        self.name = name
        self.swrtj_Element = swrtj_Element
        
    @property
    def construct(self) -> str:
        return self.__construct

    @construct.setter
    def construct(self, construct: str):
        self.__construct = construct

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swrtj_Element(self):
        return self.__swrtj_Element

    @swrtj_Element.setter
    def swrtj_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Element__swrtj_Element", None)
        self.__swrtj_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_File2"):
                opp_val = getattr(old_value, "swrtj_File2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_File2"):
                opp_val = getattr(value, "swrtj_File2", None)
                if opp_val is None:
                    setattr(value, "swrtj_File2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swrtj_Import:

    def __init__(self, importURI: str, swrtj_Import: "swrtj_File" = None):
        self.importURI = importURI
        self.swrtj_Import = swrtj_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def swrtj_Import(self):
        return self.__swrtj_Import

    @swrtj_Import.setter
    def swrtj_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swrtj_Import__swrtj_Import", None)
        self.__swrtj_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swrtj_File"):
                opp_val = getattr(old_value, "swrtj_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swrtj_File"):
                opp_val = getattr(value, "swrtj_File", None)
                if opp_val is None:
                    setattr(value, "swrtj_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swrtj_File:

    pass
class swrtj_BaseRecord:

    pass
class swrtj_Block:

    pass
class swrtj_Program(Element):

    pass
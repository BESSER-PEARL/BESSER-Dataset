from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RegExp:

    pass
class cal_RegExpBinary(RegExp):

    def __init__(self, operator: str, cal_RegExpBinary: "cal_RegExp" = None, cal_RegExpBinary274: "cal_RegExp" = None):
        self.operator = operator
        self.cal_RegExpBinary = cal_RegExpBinary
        self.cal_RegExpBinary274 = cal_RegExpBinary274
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def cal_RegExpBinary274(self):
        return self.__cal_RegExpBinary274

    @cal_RegExpBinary274.setter
    def cal_RegExpBinary274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_RegExpBinary__cal_RegExpBinary274", None)
        self.__cal_RegExpBinary274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_RegExp275"):
                opp_val = getattr(old_value, "cal_RegExp275", None)
                if opp_val == self:
                    setattr(old_value, "cal_RegExp275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_RegExp275"):
                opp_val = getattr(value, "cal_RegExp275", None)
                setattr(value, "cal_RegExp275", self)

    @property
    def cal_RegExpBinary(self):
        return self.__cal_RegExpBinary

    @cal_RegExpBinary.setter
    def cal_RegExpBinary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_RegExpBinary__cal_RegExpBinary", None)
        self.__cal_RegExpBinary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_RegExp272"):
                opp_val = getattr(old_value, "cal_RegExp272", None)
                if opp_val == self:
                    setattr(old_value, "cal_RegExp272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_RegExp272"):
                opp_val = getattr(value, "cal_RegExp272", None)
                setattr(value, "cal_RegExp272", self)

class cal_AnnotationArgument:

    def __init__(self, name: str, value: str, cal_AnnotationArgument: "cal_AstAnnotation" = None):
        self.name = name
        self.value = value
        self.cal_AnnotationArgument = cal_AnnotationArgument
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def cal_AnnotationArgument(self):
        return self.__cal_AnnotationArgument

    @cal_AnnotationArgument.setter
    def cal_AnnotationArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AnnotationArgument__cal_AnnotationArgument", None)
        self.__cal_AnnotationArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAnnotation270"):
                opp_val = getattr(old_value, "cal_AstAnnotation270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAnnotation270"):
                opp_val = getattr(value, "cal_AstAnnotation270", None)
                if opp_val is None:
                    setattr(value, "cal_AstAnnotation270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_RegExpTag(RegExp):

    pass
class cal_RegExpUnary(RegExp):

    def __init__(self, unaryOperator: str, cal_RegExpUnary: "cal_RegExp" = None):
        self.unaryOperator = unaryOperator
        self.cal_RegExpUnary = cal_RegExpUnary
        
    @property
    def unaryOperator(self) -> str:
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator

    @property
    def cal_RegExpUnary(self):
        return self.__cal_RegExpUnary

    @cal_RegExpUnary.setter
    def cal_RegExpUnary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_RegExpUnary__cal_RegExpUnary", None)
        self.__cal_RegExpUnary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_RegExp277"):
                opp_val = getattr(old_value, "cal_RegExp277", None)
                if opp_val == self:
                    setattr(old_value, "cal_RegExp277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_RegExp277"):
                opp_val = getattr(value, "cal_RegExp277", None)
                setattr(value, "cal_RegExp277", self)

class AstType:

    pass
class cal_AstTypeDouble(AstType):

    pass
class cal_AstTypeFloat(AstType):

    pass
class cal_AstTypeHalf(AstType):

    pass
class cal_AstTypeInt(AstType):

    pass
class cal_AstTypeBool(AstType):

    pass
class cal_AstTypeUint(AstType):

    pass
class cal_AstTypeString(AstType):

    pass
class cal_AstTypeList(AstType):

    pass
class cal_Generator:

    pass
class ExpressionLiteral:

    pass
class cal_ExpressionInteger(ExpressionLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cal_ExpressionFloat(ExpressionLiteral):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class cal_ExpressionString(ExpressionLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cal_ExpressionBoolean(ExpressionLiteral):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class AstExpression:

    pass
class cal_ExpressionIf(AstExpression):

    pass
class cal_ExpressionBinary(AstExpression):

    def __init__(self, operator: str, cal_ExpressionBinary: "cal_AstExpression" = None, cal_ExpressionBinary283: "cal_AstExpression" = None):
        self.operator = operator
        self.cal_ExpressionBinary = cal_ExpressionBinary
        self.cal_ExpressionBinary283 = cal_ExpressionBinary283
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def cal_ExpressionBinary(self):
        return self.__cal_ExpressionBinary

    @cal_ExpressionBinary.setter
    def cal_ExpressionBinary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_ExpressionBinary__cal_ExpressionBinary", None)
        self.__cal_ExpressionBinary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression281"):
                opp_val = getattr(old_value, "cal_AstExpression281", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression281"):
                opp_val = getattr(value, "cal_AstExpression281", None)
                setattr(value, "cal_AstExpression281", self)

    @property
    def cal_ExpressionBinary283(self):
        return self.__cal_ExpressionBinary283

    @cal_ExpressionBinary283.setter
    def cal_ExpressionBinary283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_ExpressionBinary__cal_ExpressionBinary283", None)
        self.__cal_ExpressionBinary283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression284"):
                opp_val = getattr(old_value, "cal_AstExpression284", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression284"):
                opp_val = getattr(value, "cal_AstExpression284", None)
                setattr(value, "cal_AstExpression284", self)

class cal_ExpressionIndex(AstExpression):

    pass
class cal_ExpressionList(AstExpression):

    pass
class cal_ExpressionUnary(AstExpression):

    def __init__(self, unaryOperator: str, cal_ExpressionUnary: "cal_AstExpression" = None):
        self.unaryOperator = unaryOperator
        self.cal_ExpressionUnary = cal_ExpressionUnary
        
    @property
    def unaryOperator(self) -> str:
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator

    @property
    def cal_ExpressionUnary(self):
        return self.__cal_ExpressionUnary

    @cal_ExpressionUnary.setter
    def cal_ExpressionUnary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_ExpressionUnary__cal_ExpressionUnary", None)
        self.__cal_ExpressionUnary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression286"):
                opp_val = getattr(old_value, "cal_AstExpression286", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression286"):
                opp_val = getattr(value, "cal_AstExpression286", None)
                setattr(value, "cal_AstExpression286", self)

class cal_ExpressionLiteral(AstExpression):

    pass
class cal_ExpressionVariable(AstExpression):

    pass
class cal_ExpressionCall(AstExpression):

    pass
class cal_ExpressionElsif:

    pass
class cal_StatementElsif:

    pass
class cal_VariableReference:

    pass
class Statement:

    pass
class cal_StatementForeach(Statement):

    pass
class cal_StatementAssign(Statement):

    pass
class cal_StatementCall(Statement):

    pass
class cal_StatementWhile(Statement):

    pass
class cal_StatementIf(Statement):

    pass
class cal_Guard:

    pass
class cal_OutputPattern:

    pass
class cal_InputPattern:

    pass
class cal_ExternalTarget:

    pass
class cal_AstTransition:

    pass
class cal_Fsm:

    pass
class cal_AstState:

    def __init__(self, name: str, node: str, cal_AstState: "cal_ScheduleFsm" = None, cal_AstState97: "cal_Fsm" = None, cal_AstState100: "cal_AstTransition" = None, cal_AstState106: "cal_AstTransition" = None, cal_AstState120: "cal_ExternalTarget" = None, cal_AstState114: "cal_ExternalTarget" = None, cal_AstState117: "cal_ExternalTarget" = None):
        self.name = name
        self.node = node
        self.cal_AstState = cal_AstState
        self.cal_AstState97 = cal_AstState97
        self.cal_AstState100 = cal_AstState100
        self.cal_AstState106 = cal_AstState106
        self.cal_AstState120 = cal_AstState120
        self.cal_AstState114 = cal_AstState114
        self.cal_AstState117 = cal_AstState117
        
    @property
    def node(self) -> str:
        return self.__node

    @node.setter
    def node(self, node: str):
        self.__node = node

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstState97(self):
        return self.__cal_AstState97

    @cal_AstState97.setter
    def cal_AstState97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState97", None)
        self.__cal_AstState97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Fsm96"):
                opp_val = getattr(old_value, "cal_Fsm96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Fsm96"):
                opp_val = getattr(value, "cal_Fsm96", None)
                if opp_val is None:
                    setattr(value, "cal_Fsm96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstState120(self):
        return self.__cal_AstState120

    @cal_AstState120.setter
    def cal_AstState120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState120", None)
        self.__cal_AstState120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExternalTarget119"):
                opp_val = getattr(old_value, "cal_ExternalTarget119", None)
                if opp_val == self:
                    setattr(old_value, "cal_ExternalTarget119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExternalTarget119"):
                opp_val = getattr(value, "cal_ExternalTarget119", None)
                setattr(value, "cal_ExternalTarget119", self)

    @property
    def cal_AstState114(self):
        return self.__cal_AstState114

    @cal_AstState114.setter
    def cal_AstState114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState114", None)
        self.__cal_AstState114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExternalTarget113"):
                opp_val = getattr(old_value, "cal_ExternalTarget113", None)
                if opp_val == self:
                    setattr(old_value, "cal_ExternalTarget113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExternalTarget113"):
                opp_val = getattr(value, "cal_ExternalTarget113", None)
                setattr(value, "cal_ExternalTarget113", self)

    @property
    def cal_AstState100(self):
        return self.__cal_AstState100

    @cal_AstState100.setter
    def cal_AstState100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState100", None)
        self.__cal_AstState100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition99"):
                opp_val = getattr(old_value, "cal_AstTransition99", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTransition99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition99"):
                opp_val = getattr(value, "cal_AstTransition99", None)
                setattr(value, "cal_AstTransition99", self)

    @property
    def cal_AstState106(self):
        return self.__cal_AstState106

    @cal_AstState106.setter
    def cal_AstState106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState106", None)
        self.__cal_AstState106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition105"):
                opp_val = getattr(old_value, "cal_AstTransition105", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTransition105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition105"):
                opp_val = getattr(value, "cal_AstTransition105", None)
                setattr(value, "cal_AstTransition105", self)

    @property
    def cal_AstState117(self):
        return self.__cal_AstState117

    @cal_AstState117.setter
    def cal_AstState117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState117", None)
        self.__cal_AstState117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExternalTarget116"):
                opp_val = getattr(old_value, "cal_ExternalTarget116", None)
                if opp_val == self:
                    setattr(old_value, "cal_ExternalTarget116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExternalTarget116"):
                opp_val = getattr(value, "cal_ExternalTarget116", None)
                setattr(value, "cal_ExternalTarget116", self)

    @property
    def cal_AstState(self):
        return self.__cal_AstState

    @cal_AstState.setter
    def cal_AstState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState", None)
        self.__cal_AstState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ScheduleFsm90"):
                opp_val = getattr(old_value, "cal_ScheduleFsm90", None)
                if opp_val == self:
                    setattr(old_value, "cal_ScheduleFsm90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ScheduleFsm90"):
                opp_val = getattr(value, "cal_ScheduleFsm90", None)
                setattr(value, "cal_ScheduleFsm90", self)

class cal_Inequality:

    pass
class cal_AstTag:

    def __init__(self, identifiers: str, cal_AstTag: "cal_Inequality" = None, cal_AstTag103: "cal_AstTransition" = None, cal_AstTag132: "cal_AstAction" = None, cal_AstTag279: "cal_RegExpTag" = None):
        self.identifiers = identifiers
        self.cal_AstTag = cal_AstTag
        self.cal_AstTag103 = cal_AstTag103
        self.cal_AstTag132 = cal_AstTag132
        self.cal_AstTag279 = cal_AstTag279
        
    @property
    def identifiers(self) -> str:
        return self.__identifiers

    @identifiers.setter
    def identifiers(self, identifiers: str):
        self.__identifiers = identifiers

    @property
    def cal_AstTag103(self):
        return self.__cal_AstTag103

    @cal_AstTag103.setter
    def cal_AstTag103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag103", None)
        self.__cal_AstTag103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition102"):
                opp_val = getattr(old_value, "cal_AstTransition102", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTransition102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition102"):
                opp_val = getattr(value, "cal_AstTransition102", None)
                setattr(value, "cal_AstTransition102", self)

    @property
    def cal_AstTag279(self):
        return self.__cal_AstTag279

    @cal_AstTag279.setter
    def cal_AstTag279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag279", None)
        self.__cal_AstTag279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_RegExpTag"):
                opp_val = getattr(old_value, "cal_RegExpTag", None)
                if opp_val == self:
                    setattr(old_value, "cal_RegExpTag", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_RegExpTag"):
                opp_val = getattr(value, "cal_RegExpTag", None)
                setattr(value, "cal_RegExpTag", self)

    @property
    def cal_AstTag(self):
        return self.__cal_AstTag

    @cal_AstTag.setter
    def cal_AstTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag", None)
        self.__cal_AstTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Inequality"):
                opp_val = getattr(old_value, "cal_Inequality", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Inequality"):
                opp_val = getattr(value, "cal_Inequality", None)
                if opp_val is None:
                    setattr(value, "cal_Inequality", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstTag132(self):
        return self.__cal_AstTag132

    @cal_AstTag132.setter
    def cal_AstTag132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag132", None)
        self.__cal_AstTag132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction131"):
                opp_val = getattr(old_value, "cal_AstAction131", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstAction131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction131"):
                opp_val = getattr(value, "cal_AstAction131", None)
                setattr(value, "cal_AstAction131", self)

class cal_Statement:

    pass
class cal_AstExpression:

    pass
class cal_Priority:

    pass
class cal_RegExp:

    pass
class cal_ScheduleFsm:

    pass
class cal_LocalFsm:

    def __init__(self, name: str, cal_LocalFsm: "cal_AstActor" = None, cal_LocalFsm125: "cal_Fsm" = None, cal_LocalFsm111: "cal_ExternalTarget" = None):
        self.name = name
        self.cal_LocalFsm = cal_LocalFsm
        self.cal_LocalFsm125 = cal_LocalFsm125
        self.cal_LocalFsm111 = cal_LocalFsm111
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_LocalFsm111(self):
        return self.__cal_LocalFsm111

    @cal_LocalFsm111.setter
    def cal_LocalFsm111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_LocalFsm__cal_LocalFsm111", None)
        self.__cal_LocalFsm111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExternalTarget110"):
                opp_val = getattr(old_value, "cal_ExternalTarget110", None)
                if opp_val == self:
                    setattr(old_value, "cal_ExternalTarget110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExternalTarget110"):
                opp_val = getattr(value, "cal_ExternalTarget110", None)
                setattr(value, "cal_ExternalTarget110", self)

    @property
    def cal_LocalFsm(self):
        return self.__cal_LocalFsm

    @cal_LocalFsm.setter
    def cal_LocalFsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_LocalFsm__cal_LocalFsm", None)
        self.__cal_LocalFsm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor46"):
                opp_val = getattr(old_value, "cal_AstActor46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor46"):
                opp_val = getattr(value, "cal_AstActor46", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_LocalFsm125(self):
        return self.__cal_LocalFsm125

    @cal_LocalFsm125.setter
    def cal_LocalFsm125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_LocalFsm__cal_LocalFsm125", None)
        self.__cal_LocalFsm125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Fsm126"):
                opp_val = getattr(old_value, "cal_Fsm126", None)
                if opp_val == self:
                    setattr(old_value, "cal_Fsm126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Fsm126"):
                opp_val = getattr(value, "cal_Fsm126", None)
                setattr(value, "cal_Fsm126", self)

class cal_AstAction:

    pass
class cal_AstPort:

    def __init__(self, name: str, cal_AstPort: "cal_AstActor" = None, cal_AstPort30: "cal_AstActor" = None, cal_AstPort54: set["cal_AstAnnotation"] = None, cal_AstPort57: "cal_AstType" = None, cal_AstPort147: "cal_InputPattern" = None, cal_AstPort156: "cal_OutputPattern" = None):
        self.name = name
        self.cal_AstPort = cal_AstPort
        self.cal_AstPort30 = cal_AstPort30
        self.cal_AstPort54 = cal_AstPort54 if cal_AstPort54 is not None else set()
        self.cal_AstPort57 = cal_AstPort57
        self.cal_AstPort147 = cal_AstPort147
        self.cal_AstPort156 = cal_AstPort156
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstPort156(self):
        return self.__cal_AstPort156

    @cal_AstPort156.setter
    def cal_AstPort156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort156", None)
        self.__cal_AstPort156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_OutputPattern155"):
                opp_val = getattr(old_value, "cal_OutputPattern155", None)
                if opp_val == self:
                    setattr(old_value, "cal_OutputPattern155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_OutputPattern155"):
                opp_val = getattr(value, "cal_OutputPattern155", None)
                setattr(value, "cal_OutputPattern155", self)

    @property
    def cal_AstPort(self):
        return self.__cal_AstPort

    @cal_AstPort.setter
    def cal_AstPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort", None)
        self.__cal_AstPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor27"):
                opp_val = getattr(old_value, "cal_AstActor27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor27"):
                opp_val = getattr(value, "cal_AstActor27", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstPort54(self):
        return self.__cal_AstPort54

    @cal_AstPort54.setter
    def cal_AstPort54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort54", None)
        self.__cal_AstPort54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation55"):
                    opp_val = getattr(item, "cal_AstAnnotation55", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation55"):
                    opp_val = getattr(item, "cal_AstAnnotation55", None)
                    
                    setattr(item, "cal_AstAnnotation55", self)
                    

    @property
    def cal_AstPort147(self):
        return self.__cal_AstPort147

    @cal_AstPort147.setter
    def cal_AstPort147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort147", None)
        self.__cal_AstPort147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_InputPattern146"):
                opp_val = getattr(old_value, "cal_InputPattern146", None)
                if opp_val == self:
                    setattr(old_value, "cal_InputPattern146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_InputPattern146"):
                opp_val = getattr(value, "cal_InputPattern146", None)
                setattr(value, "cal_InputPattern146", self)

    @property
    def cal_AstPort30(self):
        return self.__cal_AstPort30

    @cal_AstPort30.setter
    def cal_AstPort30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort30", None)
        self.__cal_AstPort30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor29"):
                opp_val = getattr(old_value, "cal_AstActor29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor29"):
                opp_val = getattr(value, "cal_AstActor29", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstPort57(self):
        return self.__cal_AstPort57

    @cal_AstPort57.setter
    def cal_AstPort57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort57", None)
        self.__cal_AstPort57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType58"):
                opp_val = getattr(old_value, "cal_AstType58", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType58"):
                opp_val = getattr(value, "cal_AstType58", None)
                setattr(value, "cal_AstType58", self)

class cal_AstType:

    pass
class cal_Variable:

    def __init__(self, constant: bool, name: str, cal_Variable: "cal_AstUnit" = None, cal_Variable19: "cal_AstType" = None, cal_Variable21: set["cal_AstExpression"] = None, cal_Variable25: "cal_AstActor" = None, cal_Variable44: "cal_AstActor" = None, cal_Variable14: "cal_AstExpression" = None, cal_Variable16: set["cal_AstAnnotation"] = None, cal_Variable70: "cal_Function" = None, cal_Variable79: "cal_AstProcedure" = None, cal_Variable82: "cal_AstProcedure" = None, cal_Variable64: "cal_Function" = None, cal_Variable141: "cal_AstAction" = None, cal_Variable150: "cal_InputPattern" = None, cal_Variable179: "cal_StatementForeach" = None, cal_Variable248: "cal_Generator" = None, cal_Variable268: "cal_VariableReference" = None):
        self.constant = constant
        self.name = name
        self.cal_Variable = cal_Variable
        self.cal_Variable19 = cal_Variable19
        self.cal_Variable21 = cal_Variable21 if cal_Variable21 is not None else set()
        self.cal_Variable25 = cal_Variable25
        self.cal_Variable44 = cal_Variable44
        self.cal_Variable14 = cal_Variable14
        self.cal_Variable16 = cal_Variable16 if cal_Variable16 is not None else set()
        self.cal_Variable70 = cal_Variable70
        self.cal_Variable79 = cal_Variable79
        self.cal_Variable82 = cal_Variable82
        self.cal_Variable64 = cal_Variable64
        self.cal_Variable141 = cal_Variable141
        self.cal_Variable150 = cal_Variable150
        self.cal_Variable179 = cal_Variable179
        self.cal_Variable248 = cal_Variable248
        self.cal_Variable268 = cal_Variable268
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_Variable79(self):
        return self.__cal_Variable79

    @cal_Variable79.setter
    def cal_Variable79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable79", None)
        self.__cal_Variable79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure78"):
                opp_val = getattr(old_value, "cal_AstProcedure78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure78"):
                opp_val = getattr(value, "cal_AstProcedure78", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable82(self):
        return self.__cal_Variable82

    @cal_Variable82.setter
    def cal_Variable82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable82", None)
        self.__cal_Variable82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure81"):
                opp_val = getattr(old_value, "cal_AstProcedure81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure81"):
                opp_val = getattr(value, "cal_AstProcedure81", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable(self):
        return self.__cal_Variable

    @cal_Variable.setter
    def cal_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable", None)
        self.__cal_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstUnit12"):
                opp_val = getattr(old_value, "cal_AstUnit12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstUnit12"):
                opp_val = getattr(value, "cal_AstUnit12", None)
                if opp_val is None:
                    setattr(value, "cal_AstUnit12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable268(self):
        return self.__cal_Variable268

    @cal_Variable268.setter
    def cal_Variable268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable268", None)
        self.__cal_Variable268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_VariableReference267"):
                opp_val = getattr(old_value, "cal_VariableReference267", None)
                if opp_val == self:
                    setattr(old_value, "cal_VariableReference267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_VariableReference267"):
                opp_val = getattr(value, "cal_VariableReference267", None)
                setattr(value, "cal_VariableReference267", self)

    @property
    def cal_Variable44(self):
        return self.__cal_Variable44

    @cal_Variable44.setter
    def cal_Variable44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable44", None)
        self.__cal_Variable44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor43"):
                opp_val = getattr(old_value, "cal_AstActor43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor43"):
                opp_val = getattr(value, "cal_AstActor43", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable14(self):
        return self.__cal_Variable14

    @cal_Variable14.setter
    def cal_Variable14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable14", None)
        self.__cal_Variable14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression"):
                opp_val = getattr(old_value, "cal_AstExpression", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression"):
                opp_val = getattr(value, "cal_AstExpression", None)
                setattr(value, "cal_AstExpression", self)

    @property
    def cal_Variable70(self):
        return self.__cal_Variable70

    @cal_Variable70.setter
    def cal_Variable70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable70", None)
        self.__cal_Variable70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Function69"):
                opp_val = getattr(old_value, "cal_Function69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Function69"):
                opp_val = getattr(value, "cal_Function69", None)
                if opp_val is None:
                    setattr(value, "cal_Function69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable141(self):
        return self.__cal_Variable141

    @cal_Variable141.setter
    def cal_Variable141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable141", None)
        self.__cal_Variable141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction140"):
                opp_val = getattr(old_value, "cal_AstAction140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction140"):
                opp_val = getattr(value, "cal_AstAction140", None)
                if opp_val is None:
                    setattr(value, "cal_AstAction140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable21(self):
        return self.__cal_Variable21

    @cal_Variable21.setter
    def cal_Variable21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable21", None)
        self.__cal_Variable21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstExpression22"):
                    opp_val = getattr(item, "cal_AstExpression22", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstExpression22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstExpression22"):
                    opp_val = getattr(item, "cal_AstExpression22", None)
                    
                    setattr(item, "cal_AstExpression22", self)
                    

    @property
    def cal_Variable16(self):
        return self.__cal_Variable16

    @cal_Variable16.setter
    def cal_Variable16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable16", None)
        self.__cal_Variable16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation17"):
                    opp_val = getattr(item, "cal_AstAnnotation17", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation17"):
                    opp_val = getattr(item, "cal_AstAnnotation17", None)
                    
                    setattr(item, "cal_AstAnnotation17", self)
                    

    @property
    def cal_Variable64(self):
        return self.__cal_Variable64

    @cal_Variable64.setter
    def cal_Variable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable64", None)
        self.__cal_Variable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Function63"):
                opp_val = getattr(old_value, "cal_Function63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Function63"):
                opp_val = getattr(value, "cal_Function63", None)
                if opp_val is None:
                    setattr(value, "cal_Function63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable19(self):
        return self.__cal_Variable19

    @cal_Variable19.setter
    def cal_Variable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable19", None)
        self.__cal_Variable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType"):
                opp_val = getattr(old_value, "cal_AstType", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType"):
                opp_val = getattr(value, "cal_AstType", None)
                setattr(value, "cal_AstType", self)

    @property
    def cal_Variable248(self):
        return self.__cal_Variable248

    @cal_Variable248.setter
    def cal_Variable248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable248", None)
        self.__cal_Variable248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Generator247"):
                opp_val = getattr(old_value, "cal_Generator247", None)
                if opp_val == self:
                    setattr(old_value, "cal_Generator247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Generator247"):
                opp_val = getattr(value, "cal_Generator247", None)
                setattr(value, "cal_Generator247", self)

    @property
    def cal_Variable179(self):
        return self.__cal_Variable179

    @cal_Variable179.setter
    def cal_Variable179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable179", None)
        self.__cal_Variable179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_StatementForeach"):
                opp_val = getattr(old_value, "cal_StatementForeach", None)
                if opp_val == self:
                    setattr(old_value, "cal_StatementForeach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_StatementForeach"):
                opp_val = getattr(value, "cal_StatementForeach", None)
                setattr(value, "cal_StatementForeach", self)

    @property
    def cal_Variable25(self):
        return self.__cal_Variable25

    @cal_Variable25.setter
    def cal_Variable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable25", None)
        self.__cal_Variable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor24"):
                opp_val = getattr(old_value, "cal_AstActor24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor24"):
                opp_val = getattr(value, "cal_AstActor24", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Variable150(self):
        return self.__cal_Variable150

    @cal_Variable150.setter
    def cal_Variable150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Variable__cal_Variable150", None)
        self.__cal_Variable150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_InputPattern149"):
                opp_val = getattr(old_value, "cal_InputPattern149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_InputPattern149"):
                opp_val = getattr(value, "cal_InputPattern149", None)
                if opp_val is None:
                    setattr(value, "cal_InputPattern149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstProcedure:

    def __init__(self, name: str, cal_AstProcedure: "cal_AstUnit" = None, cal_AstProcedure36: "cal_AstActor" = None, cal_AstProcedure75: set["cal_AstAnnotation"] = None, cal_AstProcedure78: set["cal_Variable"] = None, cal_AstProcedure81: set["cal_Variable"] = None, cal_AstProcedure84: set["cal_Statement"] = None, cal_AstProcedure174: "cal_StatementCall" = None):
        self.name = name
        self.cal_AstProcedure = cal_AstProcedure
        self.cal_AstProcedure36 = cal_AstProcedure36
        self.cal_AstProcedure75 = cal_AstProcedure75 if cal_AstProcedure75 is not None else set()
        self.cal_AstProcedure78 = cal_AstProcedure78 if cal_AstProcedure78 is not None else set()
        self.cal_AstProcedure81 = cal_AstProcedure81 if cal_AstProcedure81 is not None else set()
        self.cal_AstProcedure84 = cal_AstProcedure84 if cal_AstProcedure84 is not None else set()
        self.cal_AstProcedure174 = cal_AstProcedure174
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstProcedure174(self):
        return self.__cal_AstProcedure174

    @cal_AstProcedure174.setter
    def cal_AstProcedure174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure174", None)
        self.__cal_AstProcedure174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_StatementCall"):
                opp_val = getattr(old_value, "cal_StatementCall", None)
                if opp_val == self:
                    setattr(old_value, "cal_StatementCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_StatementCall"):
                opp_val = getattr(value, "cal_StatementCall", None)
                setattr(value, "cal_StatementCall", self)

    @property
    def cal_AstProcedure(self):
        return self.__cal_AstProcedure

    @cal_AstProcedure.setter
    def cal_AstProcedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure", None)
        self.__cal_AstProcedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstUnit10"):
                opp_val = getattr(old_value, "cal_AstUnit10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstUnit10"):
                opp_val = getattr(value, "cal_AstUnit10", None)
                if opp_val is None:
                    setattr(value, "cal_AstUnit10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstProcedure36(self):
        return self.__cal_AstProcedure36

    @cal_AstProcedure36.setter
    def cal_AstProcedure36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure36", None)
        self.__cal_AstProcedure36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor35"):
                opp_val = getattr(old_value, "cal_AstActor35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor35"):
                opp_val = getattr(value, "cal_AstActor35", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstProcedure78(self):
        return self.__cal_AstProcedure78

    @cal_AstProcedure78.setter
    def cal_AstProcedure78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure78", None)
        self.__cal_AstProcedure78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Variable79"):
                    opp_val = getattr(item, "cal_Variable79", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Variable79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Variable79"):
                    opp_val = getattr(item, "cal_Variable79", None)
                    
                    setattr(item, "cal_Variable79", self)
                    

    @property
    def cal_AstProcedure75(self):
        return self.__cal_AstProcedure75

    @cal_AstProcedure75.setter
    def cal_AstProcedure75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure75", None)
        self.__cal_AstProcedure75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation76"):
                    opp_val = getattr(item, "cal_AstAnnotation76", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation76"):
                    opp_val = getattr(item, "cal_AstAnnotation76", None)
                    
                    setattr(item, "cal_AstAnnotation76", self)
                    

    @property
    def cal_AstProcedure81(self):
        return self.__cal_AstProcedure81

    @cal_AstProcedure81.setter
    def cal_AstProcedure81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure81", None)
        self.__cal_AstProcedure81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Variable82"):
                    opp_val = getattr(item, "cal_Variable82", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Variable82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Variable82"):
                    opp_val = getattr(item, "cal_Variable82", None)
                    
                    setattr(item, "cal_Variable82", self)
                    

    @property
    def cal_AstProcedure84(self):
        return self.__cal_AstProcedure84

    @cal_AstProcedure84.setter
    def cal_AstProcedure84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure84", None)
        self.__cal_AstProcedure84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Statement"):
                    opp_val = getattr(item, "cal_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Statement"):
                    opp_val = getattr(item, "cal_Statement", None)
                    
                    setattr(item, "cal_Statement", self)
                    

class cal_Function:

    def __init__(self, name: str, cal_Function: "cal_AstUnit" = None, cal_Function33: "cal_AstActor" = None, cal_Function60: set["cal_AstAnnotation"] = None, cal_Function69: set["cal_Variable"] = None, cal_Function72: "cal_AstExpression" = None, cal_Function63: set["cal_Variable"] = None, cal_Function66: "cal_AstType" = None, cal_Function217: "cal_ExpressionCall" = None):
        self.name = name
        self.cal_Function = cal_Function
        self.cal_Function33 = cal_Function33
        self.cal_Function60 = cal_Function60 if cal_Function60 is not None else set()
        self.cal_Function69 = cal_Function69 if cal_Function69 is not None else set()
        self.cal_Function72 = cal_Function72
        self.cal_Function63 = cal_Function63 if cal_Function63 is not None else set()
        self.cal_Function66 = cal_Function66
        self.cal_Function217 = cal_Function217
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_Function66(self):
        return self.__cal_Function66

    @cal_Function66.setter
    def cal_Function66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function66", None)
        self.__cal_Function66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType67"):
                opp_val = getattr(old_value, "cal_AstType67", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType67"):
                opp_val = getattr(value, "cal_AstType67", None)
                setattr(value, "cal_AstType67", self)

    @property
    def cal_Function60(self):
        return self.__cal_Function60

    @cal_Function60.setter
    def cal_Function60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function60", None)
        self.__cal_Function60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation61"):
                    opp_val = getattr(item, "cal_AstAnnotation61", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation61"):
                    opp_val = getattr(item, "cal_AstAnnotation61", None)
                    
                    setattr(item, "cal_AstAnnotation61", self)
                    

    @property
    def cal_Function33(self):
        return self.__cal_Function33

    @cal_Function33.setter
    def cal_Function33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function33", None)
        self.__cal_Function33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor32"):
                opp_val = getattr(old_value, "cal_AstActor32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor32"):
                opp_val = getattr(value, "cal_AstActor32", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Function217(self):
        return self.__cal_Function217

    @cal_Function217.setter
    def cal_Function217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function217", None)
        self.__cal_Function217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExpressionCall216"):
                opp_val = getattr(old_value, "cal_ExpressionCall216", None)
                if opp_val == self:
                    setattr(old_value, "cal_ExpressionCall216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExpressionCall216"):
                opp_val = getattr(value, "cal_ExpressionCall216", None)
                setattr(value, "cal_ExpressionCall216", self)

    @property
    def cal_Function72(self):
        return self.__cal_Function72

    @cal_Function72.setter
    def cal_Function72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function72", None)
        self.__cal_Function72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression73"):
                opp_val = getattr(old_value, "cal_AstExpression73", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression73"):
                opp_val = getattr(value, "cal_AstExpression73", None)
                setattr(value, "cal_AstExpression73", self)

    @property
    def cal_Function63(self):
        return self.__cal_Function63

    @cal_Function63.setter
    def cal_Function63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function63", None)
        self.__cal_Function63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Variable64"):
                    opp_val = getattr(item, "cal_Variable64", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Variable64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Variable64"):
                    opp_val = getattr(item, "cal_Variable64", None)
                    
                    setattr(item, "cal_Variable64", self)
                    

    @property
    def cal_Function(self):
        return self.__cal_Function

    @cal_Function.setter
    def cal_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function", None)
        self.__cal_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstUnit8"):
                opp_val = getattr(old_value, "cal_AstUnit8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstUnit8"):
                opp_val = getattr(value, "cal_AstUnit8", None)
                if opp_val is None:
                    setattr(value, "cal_AstUnit8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_Function69(self):
        return self.__cal_Function69

    @cal_Function69.setter
    def cal_Function69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Function__cal_Function69", None)
        self.__cal_Function69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Variable70"):
                    opp_val = getattr(item, "cal_Variable70", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Variable70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Variable70"):
                    opp_val = getattr(item, "cal_Variable70", None)
                    
                    setattr(item, "cal_Variable70", self)
                    

class cal_AstUnit:

    pass
class cal_AstActor:

    pass
class cal_AstAnnotation:

    def __init__(self, name: str, cal_AstAnnotation: "cal_AstEntity" = None, cal_AstAnnotation55: "cal_AstPort" = None, cal_AstAnnotation61: "cal_Function" = None, cal_AstAnnotation17: "cal_Variable" = None, cal_AstAnnotation76: "cal_AstProcedure" = None, cal_AstAnnotation129: "cal_AstAction" = None, cal_AstAnnotation212: "cal_Statement" = None, cal_AstAnnotation214: "cal_ExpressionCall" = None, cal_AstAnnotation270: set["cal_AnnotationArgument"] = None):
        self.name = name
        self.cal_AstAnnotation = cal_AstAnnotation
        self.cal_AstAnnotation55 = cal_AstAnnotation55
        self.cal_AstAnnotation61 = cal_AstAnnotation61
        self.cal_AstAnnotation17 = cal_AstAnnotation17
        self.cal_AstAnnotation76 = cal_AstAnnotation76
        self.cal_AstAnnotation129 = cal_AstAnnotation129
        self.cal_AstAnnotation212 = cal_AstAnnotation212
        self.cal_AstAnnotation214 = cal_AstAnnotation214
        self.cal_AstAnnotation270 = cal_AstAnnotation270 if cal_AstAnnotation270 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstAnnotation214(self):
        return self.__cal_AstAnnotation214

    @cal_AstAnnotation214.setter
    def cal_AstAnnotation214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation214", None)
        self.__cal_AstAnnotation214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_ExpressionCall"):
                opp_val = getattr(old_value, "cal_ExpressionCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_ExpressionCall"):
                opp_val = getattr(value, "cal_ExpressionCall", None)
                if opp_val is None:
                    setattr(value, "cal_ExpressionCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation76(self):
        return self.__cal_AstAnnotation76

    @cal_AstAnnotation76.setter
    def cal_AstAnnotation76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation76", None)
        self.__cal_AstAnnotation76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure75"):
                opp_val = getattr(old_value, "cal_AstProcedure75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure75"):
                opp_val = getattr(value, "cal_AstProcedure75", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation129(self):
        return self.__cal_AstAnnotation129

    @cal_AstAnnotation129.setter
    def cal_AstAnnotation129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation129", None)
        self.__cal_AstAnnotation129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction128"):
                opp_val = getattr(old_value, "cal_AstAction128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction128"):
                opp_val = getattr(value, "cal_AstAction128", None)
                if opp_val is None:
                    setattr(value, "cal_AstAction128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation61(self):
        return self.__cal_AstAnnotation61

    @cal_AstAnnotation61.setter
    def cal_AstAnnotation61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation61", None)
        self.__cal_AstAnnotation61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Function60"):
                opp_val = getattr(old_value, "cal_Function60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Function60"):
                opp_val = getattr(value, "cal_Function60", None)
                if opp_val is None:
                    setattr(value, "cal_Function60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation212(self):
        return self.__cal_AstAnnotation212

    @cal_AstAnnotation212.setter
    def cal_AstAnnotation212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation212", None)
        self.__cal_AstAnnotation212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Statement211"):
                opp_val = getattr(old_value, "cal_Statement211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Statement211"):
                opp_val = getattr(value, "cal_Statement211", None)
                if opp_val is None:
                    setattr(value, "cal_Statement211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation17(self):
        return self.__cal_AstAnnotation17

    @cal_AstAnnotation17.setter
    def cal_AstAnnotation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation17", None)
        self.__cal_AstAnnotation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_Variable16"):
                opp_val = getattr(old_value, "cal_Variable16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_Variable16"):
                opp_val = getattr(value, "cal_Variable16", None)
                if opp_val is None:
                    setattr(value, "cal_Variable16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation270(self):
        return self.__cal_AstAnnotation270

    @cal_AstAnnotation270.setter
    def cal_AstAnnotation270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation270", None)
        self.__cal_AstAnnotation270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AnnotationArgument"):
                    opp_val = getattr(item, "cal_AnnotationArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AnnotationArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AnnotationArgument"):
                    opp_val = getattr(item, "cal_AnnotationArgument", None)
                    
                    setattr(item, "cal_AnnotationArgument", self)
                    

    @property
    def cal_AstAnnotation(self):
        return self.__cal_AstAnnotation

    @cal_AstAnnotation.setter
    def cal_AstAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation", None)
        self.__cal_AstAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstEntity2"):
                opp_val = getattr(old_value, "cal_AstEntity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstEntity2"):
                opp_val = getattr(value, "cal_AstEntity2", None)
                if opp_val is None:
                    setattr(value, "cal_AstEntity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation55(self):
        return self.__cal_AstAnnotation55

    @cal_AstAnnotation55.setter
    def cal_AstAnnotation55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation55", None)
        self.__cal_AstAnnotation55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstPort54"):
                opp_val = getattr(old_value, "cal_AstPort54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstPort54"):
                opp_val = getattr(value, "cal_AstPort54", None)
                if opp_val is None:
                    setattr(value, "cal_AstPort54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_Import:

    def __init__(self, importedNamespace: str, cal_Import: "cal_AstEntity" = None):
        self.importedNamespace = importedNamespace
        self.cal_Import = cal_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def cal_Import(self):
        return self.__cal_Import

    @cal_Import.setter
    def cal_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_Import__cal_Import", None)
        self.__cal_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstEntity"):
                opp_val = getattr(old_value, "cal_AstEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstEntity"):
                opp_val = getattr(value, "cal_AstEntity", None)
                if opp_val is None:
                    setattr(value, "cal_AstEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstEntity:

    def __init__(self, package: str, name: str, cal_AstEntity: set["cal_Import"] = None, cal_AstEntity2: set["cal_AstAnnotation"] = None, cal_AstEntity4: "cal_AstActor" = None, cal_AstEntity6: "cal_AstUnit" = None):
        self.package = package
        self.name = name
        self.cal_AstEntity = cal_AstEntity if cal_AstEntity is not None else set()
        self.cal_AstEntity2 = cal_AstEntity2 if cal_AstEntity2 is not None else set()
        self.cal_AstEntity4 = cal_AstEntity4
        self.cal_AstEntity6 = cal_AstEntity6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def cal_AstEntity2(self):
        return self.__cal_AstEntity2

    @cal_AstEntity2.setter
    def cal_AstEntity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstEntity__cal_AstEntity2", None)
        self.__cal_AstEntity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation"):
                    opp_val = getattr(item, "cal_AstAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation"):
                    opp_val = getattr(item, "cal_AstAnnotation", None)
                    
                    setattr(item, "cal_AstAnnotation", self)
                    

    @property
    def cal_AstEntity(self):
        return self.__cal_AstEntity

    @cal_AstEntity.setter
    def cal_AstEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstEntity__cal_AstEntity", None)
        self.__cal_AstEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_Import"):
                    opp_val = getattr(item, "cal_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_Import"):
                    opp_val = getattr(item, "cal_Import", None)
                    
                    setattr(item, "cal_Import", self)
                    

    @property
    def cal_AstEntity4(self):
        return self.__cal_AstEntity4

    @cal_AstEntity4.setter
    def cal_AstEntity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstEntity__cal_AstEntity4", None)
        self.__cal_AstEntity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor"):
                opp_val = getattr(old_value, "cal_AstActor", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor"):
                opp_val = getattr(value, "cal_AstActor", None)
                setattr(value, "cal_AstActor", self)

    @property
    def cal_AstEntity6(self):
        return self.__cal_AstEntity6

    @cal_AstEntity6.setter
    def cal_AstEntity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstEntity__cal_AstEntity6", None)
        self.__cal_AstEntity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstUnit"):
                opp_val = getattr(old_value, "cal_AstUnit", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstUnit"):
                opp_val = getattr(value, "cal_AstUnit", None)
                setattr(value, "cal_AstUnit", self)

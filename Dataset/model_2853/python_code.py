from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AstAction:

    pass
class cal_AstInitialize(AstAction):

    pass
class cal_AstAnnotationArgument:

    def __init__(self, name: str, value: str, cal_AstAnnotationArgument: "cal_AstAnnotation" = None):
        self.name = name
        self.value = value
        self.cal_AstAnnotationArgument = cal_AstAnnotationArgument
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstAnnotationArgument(self):
        return self.__cal_AstAnnotationArgument

    @cal_AstAnnotationArgument.setter
    def cal_AstAnnotationArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotationArgument__cal_AstAnnotationArgument", None)
        self.__cal_AstAnnotationArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAnnotation297"):
                opp_val = getattr(old_value, "cal_AstAnnotation297", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAnnotation297"):
                opp_val = getattr(value, "cal_AstAnnotation297", None)
                if opp_val is None:
                    setattr(value, "cal_AstAnnotation297", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstGenerator:

    pass
class cal_AstTypeParam:

    def __init__(self, name: str, cal_AstTypeParam: "cal_AstTypeParameterList" = None, cal_AstTypeParam285: "cal_AstExpression" = None, cal_AstTypeParam288: "cal_AstType" = None):
        self.name = name
        self.cal_AstTypeParam = cal_AstTypeParam
        self.cal_AstTypeParam285 = cal_AstTypeParam285
        self.cal_AstTypeParam288 = cal_AstTypeParam288
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstTypeParam288(self):
        return self.__cal_AstTypeParam288

    @cal_AstTypeParam288.setter
    def cal_AstTypeParam288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeParam__cal_AstTypeParam288", None)
        self.__cal_AstTypeParam288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType289"):
                opp_val = getattr(old_value, "cal_AstType289", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType289"):
                opp_val = getattr(value, "cal_AstType289", None)
                setattr(value, "cal_AstType289", self)

    @property
    def cal_AstTypeParam285(self):
        return self.__cal_AstTypeParam285

    @cal_AstTypeParam285.setter
    def cal_AstTypeParam285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeParam__cal_AstTypeParam285", None)
        self.__cal_AstTypeParam285 = value
        
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

    @property
    def cal_AstTypeParam(self):
        return self.__cal_AstTypeParam

    @cal_AstTypeParam.setter
    def cal_AstTypeParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeParam__cal_AstTypeParam", None)
        self.__cal_AstTypeParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeParameterList283"):
                opp_val = getattr(old_value, "cal_AstTypeParameterList283", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeParameterList283"):
                opp_val = getattr(value, "cal_AstTypeParameterList283", None)
                if opp_val is None:
                    setattr(value, "cal_AstTypeParameterList283", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstTypeParameterList:

    pass
class AstExpressionLiteral:

    pass
class cal_AstExpressionInteger(AstExpressionLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cal_AstExpressionFloat(AstExpressionLiteral):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class cal_AstExpressionString(AstExpressionLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class cal_AstExpressionBoolean(AstExpressionLiteral):

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
class cal_AstExpressionList(AstExpression):

    pass
class cal_AstExpressionLiteral(AstExpression):

    pass
class cal_AstExpressionIf(AstExpression):

    pass
class cal_AstExpressionBinary(AstExpression):

    def __init__(self, operator: str, cal_AstExpressionBinary: "cal_AstExpression" = None, cal_AstExpressionBinary301: "cal_AstExpression" = None):
        self.operator = operator
        self.cal_AstExpressionBinary = cal_AstExpressionBinary
        self.cal_AstExpressionBinary301 = cal_AstExpressionBinary301
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def cal_AstExpressionBinary301(self):
        return self.__cal_AstExpressionBinary301

    @cal_AstExpressionBinary301.setter
    def cal_AstExpressionBinary301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstExpressionBinary__cal_AstExpressionBinary301", None)
        self.__cal_AstExpressionBinary301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression302"):
                opp_val = getattr(old_value, "cal_AstExpression302", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression302"):
                opp_val = getattr(value, "cal_AstExpression302", None)
                setattr(value, "cal_AstExpression302", self)

    @property
    def cal_AstExpressionBinary(self):
        return self.__cal_AstExpressionBinary

    @cal_AstExpressionBinary.setter
    def cal_AstExpressionBinary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstExpressionBinary__cal_AstExpressionBinary", None)
        self.__cal_AstExpressionBinary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression299"):
                opp_val = getattr(old_value, "cal_AstExpression299", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression299"):
                opp_val = getattr(value, "cal_AstExpression299", None)
                setattr(value, "cal_AstExpression299", self)

class cal_AstExpressionVariable(AstExpression):

    pass
class cal_AstExpressionUnary(AstExpression):

    def __init__(self, unaryOperator: str, cal_AstExpressionUnary: "cal_AstExpression" = None):
        self.unaryOperator = unaryOperator
        self.cal_AstExpressionUnary = cal_AstExpressionUnary
        
    @property
    def unaryOperator(self) -> str:
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator

    @property
    def cal_AstExpressionUnary(self):
        return self.__cal_AstExpressionUnary

    @cal_AstExpressionUnary.setter
    def cal_AstExpressionUnary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstExpressionUnary__cal_AstExpressionUnary", None)
        self.__cal_AstExpressionUnary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression304"):
                opp_val = getattr(old_value, "cal_AstExpression304", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression304"):
                opp_val = getattr(value, "cal_AstExpression304", None)
                setattr(value, "cal_AstExpression304", self)

class cal_AstExpressionCall(AstExpression):

    pass
class cal_AstOutputPattern:

    pass
class cal_AstForeachGenerator:

    pass
class cal_AstMemberAccess:

    def __init__(self, name: str, cal_AstMemberAccess: "cal_AstStatementAssign" = None, cal_AstMemberAccess264: "cal_AstExpressionVariable" = None, cal_AstMemberAccess294: set["cal_AstExpression"] = None):
        self.name = name
        self.cal_AstMemberAccess = cal_AstMemberAccess
        self.cal_AstMemberAccess264 = cal_AstMemberAccess264
        self.cal_AstMemberAccess294 = cal_AstMemberAccess294 if cal_AstMemberAccess294 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstMemberAccess294(self):
        return self.__cal_AstMemberAccess294

    @cal_AstMemberAccess294.setter
    def cal_AstMemberAccess294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstMemberAccess__cal_AstMemberAccess294", None)
        self.__cal_AstMemberAccess294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstExpression295"):
                    opp_val = getattr(item, "cal_AstExpression295", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstExpression295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstExpression295"):
                    opp_val = getattr(item, "cal_AstExpression295", None)
                    
                    setattr(item, "cal_AstExpression295", self)
                    

    @property
    def cal_AstMemberAccess264(self):
        return self.__cal_AstMemberAccess264

    @cal_AstMemberAccess264.setter
    def cal_AstMemberAccess264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstMemberAccess__cal_AstMemberAccess264", None)
        self.__cal_AstMemberAccess264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpressionVariable263"):
                opp_val = getattr(old_value, "cal_AstExpressionVariable263", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpressionVariable263"):
                opp_val = getattr(value, "cal_AstExpressionVariable263", None)
                if opp_val is None:
                    setattr(value, "cal_AstExpressionVariable263", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstMemberAccess(self):
        return self.__cal_AstMemberAccess

    @cal_AstMemberAccess.setter
    def cal_AstMemberAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstMemberAccess__cal_AstMemberAccess", None)
        self.__cal_AstMemberAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstStatementAssign194"):
                opp_val = getattr(old_value, "cal_AstStatementAssign194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstStatementAssign194"):
                opp_val = getattr(value, "cal_AstStatementAssign194", None)
                if opp_val is None:
                    setattr(value, "cal_AstStatementAssign194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstVariableReference:

    pass
class AstStatement:

    pass
class cal_AstStatementBlock(AstStatement):

    pass
class cal_AstStatementForeach(AstStatement):

    pass
class cal_AstStatementIf(AstStatement):

    pass
class cal_AstStatementWhile(AstStatement):

    pass
class cal_AstStatementCall(AstStatement):

    pass
class cal_AstStatementAssign(AstStatement):

    pass
class AstExternalProcedure:

    pass
class cal_AstExternalFunction:

    pass
class cal_AstInputPattern:

    pass
class cal_AstTransition:

    pass
class cal_AstState:

    def __init__(self, name: str, cal_AstState: "cal_AstSchedule" = None, cal_AstState145: "cal_AstTransition" = None, cal_AstState151: "cal_AstTransition" = None):
        self.name = name
        self.cal_AstState = cal_AstState
        self.cal_AstState145 = cal_AstState145
        self.cal_AstState151 = cal_AstState151
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstState145(self):
        return self.__cal_AstState145

    @cal_AstState145.setter
    def cal_AstState145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState145", None)
        self.__cal_AstState145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition144"):
                opp_val = getattr(old_value, "cal_AstTransition144", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTransition144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition144"):
                opp_val = getattr(value, "cal_AstTransition144", None)
                setattr(value, "cal_AstTransition144", self)

    @property
    def cal_AstState151(self):
        return self.__cal_AstState151

    @cal_AstState151.setter
    def cal_AstState151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstState__cal_AstState151", None)
        self.__cal_AstState151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition150"):
                opp_val = getattr(old_value, "cal_AstTransition150", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTransition150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition150"):
                opp_val = getattr(value, "cal_AstTransition150", None)
                setattr(value, "cal_AstTransition150", self)

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
            if hasattr(old_value, "cal_AstSchedule140"):
                opp_val = getattr(old_value, "cal_AstSchedule140", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstSchedule140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstSchedule140"):
                opp_val = getattr(value, "cal_AstSchedule140", None)
                setattr(value, "cal_AstSchedule140", self)

class cal_AstInequality:

    pass
class cal_AstTag:

    def __init__(self, identifiers: str, cal_AstTag: "cal_AstInequality" = None, cal_AstTag148: "cal_AstTransition" = None, cal_AstTag157: "cal_AstAction" = None):
        self.identifiers = identifiers
        self.cal_AstTag = cal_AstTag
        self.cal_AstTag148 = cal_AstTag148
        self.cal_AstTag157 = cal_AstTag157
        
    @property
    def identifiers(self) -> str:
        return self.__identifiers

    @identifiers.setter
    def identifiers(self, identifiers: str):
        self.__identifiers = identifiers

    @property
    def cal_AstTag157(self):
        return self.__cal_AstTag157

    @cal_AstTag157.setter
    def cal_AstTag157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag157", None)
        self.__cal_AstTag157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction156"):
                opp_val = getattr(old_value, "cal_AstAction156", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstAction156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction156"):
                opp_val = getattr(value, "cal_AstAction156", None)
                setattr(value, "cal_AstAction156", self)

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
            if hasattr(old_value, "cal_AstInequality"):
                opp_val = getattr(old_value, "cal_AstInequality", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstInequality"):
                opp_val = getattr(value, "cal_AstInequality", None)
                if opp_val is None:
                    setattr(value, "cal_AstInequality", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstTag148(self):
        return self.__cal_AstTag148

    @cal_AstTag148.setter
    def cal_AstTag148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTag__cal_AstTag148", None)
        self.__cal_AstTag148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTransition147"):
                opp_val = getattr(old_value, "cal_AstTransition147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTransition147"):
                opp_val = getattr(value, "cal_AstTransition147", None)
                if opp_val is None:
                    setattr(value, "cal_AstTransition147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstExternalProcedure:

    pass
class cal_AstStatement:

    pass
class cal_AstTypeDefinitionParameter:

    pass
class cal_AstPriority:

    pass
class cal_AstSchedule:

    pass
class cal_AstAction:

    pass
class cal_AstProcedure(AstExternalProcedure):

    def __init__(self, name: str, cal_AstProcedure: "cal_AstActor" = None, cal_AstProcedure125: set["cal_AstAnnotation"] = None, cal_AstProcedure128: set["cal_AstVariable"] = None, cal_AstProcedure131: set["cal_AstVariable"] = None, cal_AstProcedure134: set["cal_AstStatement"] = None, cal_AstProcedure199: "cal_AstStatementCall" = None):
        self.name = name
        self.cal_AstProcedure = cal_AstProcedure
        self.cal_AstProcedure125 = cal_AstProcedure125 if cal_AstProcedure125 is not None else set()
        self.cal_AstProcedure128 = cal_AstProcedure128 if cal_AstProcedure128 is not None else set()
        self.cal_AstProcedure131 = cal_AstProcedure131 if cal_AstProcedure131 is not None else set()
        self.cal_AstProcedure134 = cal_AstProcedure134 if cal_AstProcedure134 is not None else set()
        self.cal_AstProcedure199 = cal_AstProcedure199
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstProcedure199(self):
        return self.__cal_AstProcedure199

    @cal_AstProcedure199.setter
    def cal_AstProcedure199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure199", None)
        self.__cal_AstProcedure199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstStatementCall"):
                opp_val = getattr(old_value, "cal_AstStatementCall", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstStatementCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstStatementCall"):
                opp_val = getattr(value, "cal_AstStatementCall", None)
                setattr(value, "cal_AstStatementCall", self)

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
            if hasattr(old_value, "cal_AstActor105"):
                opp_val = getattr(old_value, "cal_AstActor105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor105"):
                opp_val = getattr(value, "cal_AstActor105", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstProcedure125(self):
        return self.__cal_AstProcedure125

    @cal_AstProcedure125.setter
    def cal_AstProcedure125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure125", None)
        self.__cal_AstProcedure125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation126"):
                    opp_val = getattr(item, "cal_AstAnnotation126", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation126"):
                    opp_val = getattr(item, "cal_AstAnnotation126", None)
                    
                    setattr(item, "cal_AstAnnotation126", self)
                    

    @property
    def cal_AstProcedure131(self):
        return self.__cal_AstProcedure131

    @cal_AstProcedure131.setter
    def cal_AstProcedure131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure131", None)
        self.__cal_AstProcedure131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable132"):
                    opp_val = getattr(item, "cal_AstVariable132", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable132"):
                    opp_val = getattr(item, "cal_AstVariable132", None)
                    
                    setattr(item, "cal_AstVariable132", self)
                    

    @property
    def cal_AstProcedure134(self):
        return self.__cal_AstProcedure134

    @cal_AstProcedure134.setter
    def cal_AstProcedure134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure134", None)
        self.__cal_AstProcedure134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstStatement"):
                    opp_val = getattr(item, "cal_AstStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstStatement"):
                    opp_val = getattr(item, "cal_AstStatement", None)
                    
                    setattr(item, "cal_AstStatement", self)
                    

    @property
    def cal_AstProcedure128(self):
        return self.__cal_AstProcedure128

    @cal_AstProcedure128.setter
    def cal_AstProcedure128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstProcedure__cal_AstProcedure128", None)
        self.__cal_AstProcedure128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable129"):
                    opp_val = getattr(item, "cal_AstVariable129", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable129"):
                    opp_val = getattr(item, "cal_AstVariable129", None)
                    
                    setattr(item, "cal_AstVariable129", self)
                    

class AstExternalFunction:

    pass
class cal_AstStructure:

    pass
class cal_AstActorVariable:

    def __init__(self, name: str, cal_AstActorVariable38: "cal_AstEntity" = None, cal_AstActorVariable41: set["cal_AstAssignParameter"] = None, cal_AstActorVariable55: "cal_AstActorVariableReference" = None, cal_AstActorVariable: "cal_AstNetwork" = None):
        self.name = name
        self.cal_AstActorVariable38 = cal_AstActorVariable38
        self.cal_AstActorVariable41 = cal_AstActorVariable41 if cal_AstActorVariable41 is not None else set()
        self.cal_AstActorVariable55 = cal_AstActorVariable55
        self.cal_AstActorVariable = cal_AstActorVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstActorVariable41(self):
        return self.__cal_AstActorVariable41

    @cal_AstActorVariable41.setter
    def cal_AstActorVariable41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstActorVariable__cal_AstActorVariable41", None)
        self.__cal_AstActorVariable41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAssignParameter"):
                    opp_val = getattr(item, "cal_AstAssignParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAssignParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAssignParameter"):
                    opp_val = getattr(item, "cal_AstAssignParameter", None)
                    
                    setattr(item, "cal_AstAssignParameter", self)
                    

    @property
    def cal_AstActorVariable38(self):
        return self.__cal_AstActorVariable38

    @cal_AstActorVariable38.setter
    def cal_AstActorVariable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstActorVariable__cal_AstActorVariable38", None)
        self.__cal_AstActorVariable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstEntity39"):
                opp_val = getattr(old_value, "cal_AstEntity39", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstEntity39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstEntity39"):
                opp_val = getattr(value, "cal_AstEntity39", None)
                setattr(value, "cal_AstEntity39", self)

    @property
    def cal_AstActorVariable55(self):
        return self.__cal_AstActorVariable55

    @cal_AstActorVariable55.setter
    def cal_AstActorVariable55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstActorVariable__cal_AstActorVariable55", None)
        self.__cal_AstActorVariable55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActorVariableReference54"):
                opp_val = getattr(old_value, "cal_AstActorVariableReference54", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstActorVariableReference54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActorVariableReference54"):
                opp_val = getattr(value, "cal_AstActorVariableReference54", None)
                setattr(value, "cal_AstActorVariableReference54", self)

    @property
    def cal_AstActorVariable(self):
        return self.__cal_AstActorVariable

    @cal_AstActorVariable.setter
    def cal_AstActorVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstActorVariable__cal_AstActorVariable", None)
        self.__cal_AstActorVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNetwork34"):
                opp_val = getattr(old_value, "cal_AstNetwork34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNetwork34"):
                opp_val = getattr(value, "cal_AstNetwork34", None)
                if opp_val is None:
                    setattr(value, "cal_AstNetwork34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstType:

    def __init__(self, builtin: str, cal_AstType: "cal_AstVariable" = None, cal_AstType95: "cal_AstFunction" = None, cal_AstType77: "cal_AstTypeName" = None, cal_AstType123: "cal_AstPort" = None, cal_AstType266: "cal_AstTypeParameterList" = None, cal_AstType268: set["cal_AstExpression"] = None, cal_AstType271: "cal_AstTypeName" = None, cal_AstType275: "cal_AstType" = None, cal_AstType273: set["cal_AstType"] = None, cal_AstType278: "cal_AstType" = None, cal_AstType276: set["cal_AstType"] = None, cal_AstType280: set["cal_AstVariable"] = None, cal_AstType289: "cal_AstTypeParam" = None):
        self.builtin = builtin
        self.cal_AstType = cal_AstType
        self.cal_AstType95 = cal_AstType95
        self.cal_AstType77 = cal_AstType77
        self.cal_AstType123 = cal_AstType123
        self.cal_AstType266 = cal_AstType266
        self.cal_AstType268 = cal_AstType268 if cal_AstType268 is not None else set()
        self.cal_AstType271 = cal_AstType271
        self.cal_AstType275 = cal_AstType275
        self.cal_AstType273 = cal_AstType273 if cal_AstType273 is not None else set()
        self.cal_AstType278 = cal_AstType278
        self.cal_AstType276 = cal_AstType276 if cal_AstType276 is not None else set()
        self.cal_AstType280 = cal_AstType280 if cal_AstType280 is not None else set()
        self.cal_AstType289 = cal_AstType289
        
    @property
    def builtin(self) -> str:
        return self.__builtin

    @builtin.setter
    def builtin(self, builtin: str):
        self.__builtin = builtin

    @property
    def cal_AstType278(self):
        return self.__cal_AstType278

    @cal_AstType278.setter
    def cal_AstType278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType278", None)
        self.__cal_AstType278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType276"):
                opp_val = getattr(old_value, "cal_AstType276", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType276"):
                opp_val = getattr(value, "cal_AstType276", None)
                if opp_val is None:
                    setattr(value, "cal_AstType276", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstType275(self):
        return self.__cal_AstType275

    @cal_AstType275.setter
    def cal_AstType275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType275", None)
        self.__cal_AstType275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType273"):
                opp_val = getattr(old_value, "cal_AstType273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType273"):
                opp_val = getattr(value, "cal_AstType273", None)
                if opp_val is None:
                    setattr(value, "cal_AstType273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstType271(self):
        return self.__cal_AstType271

    @cal_AstType271.setter
    def cal_AstType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType271", None)
        self.__cal_AstType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeName272"):
                opp_val = getattr(old_value, "cal_AstTypeName272", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeName272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeName272"):
                opp_val = getattr(value, "cal_AstTypeName272", None)
                setattr(value, "cal_AstTypeName272", self)

    @property
    def cal_AstType123(self):
        return self.__cal_AstType123

    @cal_AstType123.setter
    def cal_AstType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType123", None)
        self.__cal_AstType123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstPort122"):
                opp_val = getattr(old_value, "cal_AstPort122", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstPort122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstPort122"):
                opp_val = getattr(value, "cal_AstPort122", None)
                setattr(value, "cal_AstPort122", self)

    @property
    def cal_AstType266(self):
        return self.__cal_AstType266

    @cal_AstType266.setter
    def cal_AstType266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType266", None)
        self.__cal_AstType266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeParameterList"):
                opp_val = getattr(old_value, "cal_AstTypeParameterList", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeParameterList"):
                opp_val = getattr(value, "cal_AstTypeParameterList", None)
                setattr(value, "cal_AstTypeParameterList", self)

    @property
    def cal_AstType289(self):
        return self.__cal_AstType289

    @cal_AstType289.setter
    def cal_AstType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType289", None)
        self.__cal_AstType289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeParam288"):
                opp_val = getattr(old_value, "cal_AstTypeParam288", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeParam288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeParam288"):
                opp_val = getattr(value, "cal_AstTypeParam288", None)
                setattr(value, "cal_AstTypeParam288", self)

    @property
    def cal_AstType77(self):
        return self.__cal_AstType77

    @cal_AstType77.setter
    def cal_AstType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType77", None)
        self.__cal_AstType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeName76"):
                opp_val = getattr(old_value, "cal_AstTypeName76", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeName76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeName76"):
                opp_val = getattr(value, "cal_AstTypeName76", None)
                setattr(value, "cal_AstTypeName76", self)

    @property
    def cal_AstType273(self):
        return self.__cal_AstType273

    @cal_AstType273.setter
    def cal_AstType273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType273", None)
        self.__cal_AstType273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstType275"):
                    opp_val = getattr(item, "cal_AstType275", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstType275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstType275"):
                    opp_val = getattr(item, "cal_AstType275", None)
                    
                    setattr(item, "cal_AstType275", self)
                    

    @property
    def cal_AstType268(self):
        return self.__cal_AstType268

    @cal_AstType268.setter
    def cal_AstType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType268", None)
        self.__cal_AstType268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstExpression269"):
                    opp_val = getattr(item, "cal_AstExpression269", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstExpression269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstExpression269"):
                    opp_val = getattr(item, "cal_AstExpression269", None)
                    
                    setattr(item, "cal_AstExpression269", self)
                    

    @property
    def cal_AstType280(self):
        return self.__cal_AstType280

    @cal_AstType280.setter
    def cal_AstType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType280", None)
        self.__cal_AstType280 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable281"):
                    opp_val = getattr(item, "cal_AstVariable281", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable281"):
                    opp_val = getattr(item, "cal_AstVariable281", None)
                    
                    setattr(item, "cal_AstVariable281", self)
                    

    @property
    def cal_AstType276(self):
        return self.__cal_AstType276

    @cal_AstType276.setter
    def cal_AstType276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType276", None)
        self.__cal_AstType276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstType278"):
                    opp_val = getattr(item, "cal_AstType278", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstType278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstType278"):
                    opp_val = getattr(item, "cal_AstType278", None)
                    
                    setattr(item, "cal_AstType278", self)
                    

    @property
    def cal_AstType(self):
        return self.__cal_AstType

    @cal_AstType.setter
    def cal_AstType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType", None)
        self.__cal_AstType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstVariable66"):
                opp_val = getattr(old_value, "cal_AstVariable66", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstVariable66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstVariable66"):
                opp_val = getattr(value, "cal_AstVariable66", None)
                setattr(value, "cal_AstVariable66", self)

    @property
    def cal_AstType95(self):
        return self.__cal_AstType95

    @cal_AstType95.setter
    def cal_AstType95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstType__cal_AstType95", None)
        self.__cal_AstType95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstFunction94"):
                opp_val = getattr(old_value, "cal_AstFunction94", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstFunction94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstFunction94"):
                opp_val = getattr(value, "cal_AstFunction94", None)
                setattr(value, "cal_AstFunction94", self)

class cal_AstConnectionAttribute:

    def __init__(self, name: str, cal_AstConnectionAttribute: "cal_AstConnection" = None, cal_AstConnectionAttribute57: "cal_AstExpression" = None):
        self.name = name
        self.cal_AstConnectionAttribute = cal_AstConnectionAttribute
        self.cal_AstConnectionAttribute57 = cal_AstConnectionAttribute57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstConnectionAttribute(self):
        return self.__cal_AstConnectionAttribute

    @cal_AstConnectionAttribute.setter
    def cal_AstConnectionAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnectionAttribute__cal_AstConnectionAttribute", None)
        self.__cal_AstConnectionAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstConnection52"):
                opp_val = getattr(old_value, "cal_AstConnection52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstConnection52"):
                opp_val = getattr(value, "cal_AstConnection52", None)
                if opp_val is None:
                    setattr(value, "cal_AstConnection52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstConnectionAttribute57(self):
        return self.__cal_AstConnectionAttribute57

    @cal_AstConnectionAttribute57.setter
    def cal_AstConnectionAttribute57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnectionAttribute__cal_AstConnectionAttribute57", None)
        self.__cal_AstConnectionAttribute57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression58"):
                opp_val = getattr(old_value, "cal_AstExpression58", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression58"):
                opp_val = getattr(value, "cal_AstExpression58", None)
                setattr(value, "cal_AstExpression58", self)

class cal_AstActorVariableReference:

    pass
class cal_AstConnection:

    def __init__(self, outPort: str, inPort: str, cal_AstConnection: "cal_AstStructure" = None, cal_AstConnection47: "cal_AstActorVariableReference" = None, cal_AstConnection49: "cal_AstActorVariableReference" = None, cal_AstConnection52: set["cal_AstConnectionAttribute"] = None):
        self.outPort = outPort
        self.inPort = inPort
        self.cal_AstConnection = cal_AstConnection
        self.cal_AstConnection47 = cal_AstConnection47
        self.cal_AstConnection49 = cal_AstConnection49
        self.cal_AstConnection52 = cal_AstConnection52 if cal_AstConnection52 is not None else set()
        
    @property
    def outPort(self) -> str:
        return self.__outPort

    @outPort.setter
    def outPort(self, outPort: str):
        self.__outPort = outPort

    @property
    def inPort(self) -> str:
        return self.__inPort

    @inPort.setter
    def inPort(self, inPort: str):
        self.__inPort = inPort

    @property
    def cal_AstConnection52(self):
        return self.__cal_AstConnection52

    @cal_AstConnection52.setter
    def cal_AstConnection52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnection__cal_AstConnection52", None)
        self.__cal_AstConnection52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstConnectionAttribute"):
                    opp_val = getattr(item, "cal_AstConnectionAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstConnectionAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstConnectionAttribute"):
                    opp_val = getattr(item, "cal_AstConnectionAttribute", None)
                    
                    setattr(item, "cal_AstConnectionAttribute", self)
                    

    @property
    def cal_AstConnection(self):
        return self.__cal_AstConnection

    @cal_AstConnection.setter
    def cal_AstConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnection__cal_AstConnection", None)
        self.__cal_AstConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstStructure45"):
                opp_val = getattr(old_value, "cal_AstStructure45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstStructure45"):
                opp_val = getattr(value, "cal_AstStructure45", None)
                if opp_val is None:
                    setattr(value, "cal_AstStructure45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstConnection47(self):
        return self.__cal_AstConnection47

    @cal_AstConnection47.setter
    def cal_AstConnection47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnection__cal_AstConnection47", None)
        self.__cal_AstConnection47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActorVariableReference"):
                opp_val = getattr(old_value, "cal_AstActorVariableReference", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstActorVariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActorVariableReference"):
                opp_val = getattr(value, "cal_AstActorVariableReference", None)
                setattr(value, "cal_AstActorVariableReference", self)

    @property
    def cal_AstConnection49(self):
        return self.__cal_AstConnection49

    @cal_AstConnection49.setter
    def cal_AstConnection49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstConnection__cal_AstConnection49", None)
        self.__cal_AstConnection49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActorVariableReference50"):
                opp_val = getattr(old_value, "cal_AstActorVariableReference50", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstActorVariableReference50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActorVariableReference50"):
                opp_val = getattr(value, "cal_AstActorVariableReference50", None)
                setattr(value, "cal_AstActorVariableReference50", self)

class cal_AstExpression:

    pass
class cal_AstAssignParameter:

    def __init__(self, name: str, cal_AstAssignParameter: "cal_AstActorVariable" = None, cal_AstAssignParameter43: "cal_AstExpression" = None):
        self.name = name
        self.cal_AstAssignParameter = cal_AstAssignParameter
        self.cal_AstAssignParameter43 = cal_AstAssignParameter43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstAssignParameter(self):
        return self.__cal_AstAssignParameter

    @cal_AstAssignParameter.setter
    def cal_AstAssignParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAssignParameter__cal_AstAssignParameter", None)
        self.__cal_AstAssignParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActorVariable41"):
                opp_val = getattr(old_value, "cal_AstActorVariable41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActorVariable41"):
                opp_val = getattr(value, "cal_AstActorVariable41", None)
                if opp_val is None:
                    setattr(value, "cal_AstActorVariable41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAssignParameter43(self):
        return self.__cal_AstAssignParameter43

    @cal_AstAssignParameter43.setter
    def cal_AstAssignParameter43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAssignParameter__cal_AstAssignParameter43", None)
        self.__cal_AstAssignParameter43 = value
        
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

class cal_AstEntity:

    pass
class AstUnit:

    pass
class AstPackage:

    pass
class AstAbstractActor:

    pass
class cal_AstActor(AstAbstractActor):

    pass
class cal_AstExternalActor(AstAbstractActor):

    pass
class cal_AstNetwork(AstAbstractActor):

    pass
class cal_AstPort:

    def __init__(self, name: str, cal_AstPort: "cal_AstAbstractActor" = None, cal_AstPort30: "cal_AstAbstractActor" = None, cal_AstPort119: set["cal_AstAnnotation"] = None, cal_AstPort122: "cal_AstType" = None, cal_AstPort173: "cal_AstInputPattern" = None, cal_AstPort182: "cal_AstOutputPattern" = None):
        self.name = name
        self.cal_AstPort = cal_AstPort
        self.cal_AstPort30 = cal_AstPort30
        self.cal_AstPort119 = cal_AstPort119 if cal_AstPort119 is not None else set()
        self.cal_AstPort122 = cal_AstPort122
        self.cal_AstPort173 = cal_AstPort173
        self.cal_AstPort182 = cal_AstPort182
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstPort122(self):
        return self.__cal_AstPort122

    @cal_AstPort122.setter
    def cal_AstPort122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort122", None)
        self.__cal_AstPort122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType123"):
                opp_val = getattr(old_value, "cal_AstType123", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType123"):
                opp_val = getattr(value, "cal_AstType123", None)
                setattr(value, "cal_AstType123", self)

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
            if hasattr(old_value, "cal_AstAbstractActor27"):
                opp_val = getattr(old_value, "cal_AstAbstractActor27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAbstractActor27"):
                opp_val = getattr(value, "cal_AstAbstractActor27", None)
                if opp_val is None:
                    setattr(value, "cal_AstAbstractActor27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstPort173(self):
        return self.__cal_AstPort173

    @cal_AstPort173.setter
    def cal_AstPort173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort173", None)
        self.__cal_AstPort173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstInputPattern172"):
                opp_val = getattr(old_value, "cal_AstInputPattern172", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstInputPattern172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstInputPattern172"):
                opp_val = getattr(value, "cal_AstInputPattern172", None)
                setattr(value, "cal_AstInputPattern172", self)

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
            if hasattr(old_value, "cal_AstAbstractActor29"):
                opp_val = getattr(old_value, "cal_AstAbstractActor29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAbstractActor29"):
                opp_val = getattr(value, "cal_AstAbstractActor29", None)
                if opp_val is None:
                    setattr(value, "cal_AstAbstractActor29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstPort182(self):
        return self.__cal_AstPort182

    @cal_AstPort182.setter
    def cal_AstPort182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort182", None)
        self.__cal_AstPort182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstOutputPattern181"):
                opp_val = getattr(old_value, "cal_AstOutputPattern181", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstOutputPattern181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstOutputPattern181"):
                opp_val = getattr(value, "cal_AstOutputPattern181", None)
                setattr(value, "cal_AstOutputPattern181", self)

    @property
    def cal_AstPort119(self):
        return self.__cal_AstPort119

    @cal_AstPort119.setter
    def cal_AstPort119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstPort__cal_AstPort119", None)
        self.__cal_AstPort119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation120"):
                    opp_val = getattr(item, "cal_AstAnnotation120", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation120"):
                    opp_val = getattr(item, "cal_AstAnnotation120", None)
                    
                    setattr(item, "cal_AstAnnotation120", self)
                    

class cal_AstAbstractActor:

    def __init__(self, name: str, cal_AstAbstractActor: "cal_AstEntity" = None, cal_AstAbstractActor24: set["cal_AstVariable"] = None, cal_AstAbstractActor27: set["cal_AstPort"] = None, cal_AstAbstractActor29: set["cal_AstPort"] = None):
        self.name = name
        self.cal_AstAbstractActor = cal_AstAbstractActor
        self.cal_AstAbstractActor24 = cal_AstAbstractActor24 if cal_AstAbstractActor24 is not None else set()
        self.cal_AstAbstractActor27 = cal_AstAbstractActor27 if cal_AstAbstractActor27 is not None else set()
        self.cal_AstAbstractActor29 = cal_AstAbstractActor29 if cal_AstAbstractActor29 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstAbstractActor24(self):
        return self.__cal_AstAbstractActor24

    @cal_AstAbstractActor24.setter
    def cal_AstAbstractActor24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAbstractActor__cal_AstAbstractActor24", None)
        self.__cal_AstAbstractActor24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable25"):
                    opp_val = getattr(item, "cal_AstVariable25", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable25"):
                    opp_val = getattr(item, "cal_AstVariable25", None)
                    
                    setattr(item, "cal_AstVariable25", self)
                    

    @property
    def cal_AstAbstractActor(self):
        return self.__cal_AstAbstractActor

    @cal_AstAbstractActor.setter
    def cal_AstAbstractActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAbstractActor__cal_AstAbstractActor", None)
        self.__cal_AstAbstractActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstEntity22"):
                opp_val = getattr(old_value, "cal_AstEntity22", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstEntity22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstEntity22"):
                opp_val = getattr(value, "cal_AstEntity22", None)
                setattr(value, "cal_AstEntity22", self)

    @property
    def cal_AstAbstractActor29(self):
        return self.__cal_AstAbstractActor29

    @cal_AstAbstractActor29.setter
    def cal_AstAbstractActor29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAbstractActor__cal_AstAbstractActor29", None)
        self.__cal_AstAbstractActor29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstPort30"):
                    opp_val = getattr(item, "cal_AstPort30", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstPort30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstPort30"):
                    opp_val = getattr(item, "cal_AstPort30", None)
                    
                    setattr(item, "cal_AstPort30", self)
                    

    @property
    def cal_AstAbstractActor27(self):
        return self.__cal_AstAbstractActor27

    @cal_AstAbstractActor27.setter
    def cal_AstAbstractActor27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAbstractActor__cal_AstAbstractActor27", None)
        self.__cal_AstAbstractActor27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstPort"):
                    opp_val = getattr(item, "cal_AstPort", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstPort"):
                    opp_val = getattr(item, "cal_AstPort", None)
                    
                    setattr(item, "cal_AstPort", self)
                    

class cal_AstTypeName:

    def __init__(self, name: str, cal_AstTypeName: "cal_AstNamespace" = None, cal_AstTypeName83: "cal_AstTypeDefinitionParameter" = None, cal_AstTypeName71: set["cal_AstTypeDefinitionParameter"] = None, cal_AstTypeName73: set["cal_AstFunction"] = None, cal_AstTypeName76: "cal_AstType" = None, cal_AstTypeName272: "cal_AstType" = None):
        self.name = name
        self.cal_AstTypeName = cal_AstTypeName
        self.cal_AstTypeName83 = cal_AstTypeName83
        self.cal_AstTypeName71 = cal_AstTypeName71 if cal_AstTypeName71 is not None else set()
        self.cal_AstTypeName73 = cal_AstTypeName73 if cal_AstTypeName73 is not None else set()
        self.cal_AstTypeName76 = cal_AstTypeName76
        self.cal_AstTypeName272 = cal_AstTypeName272
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstTypeName(self):
        return self.__cal_AstTypeName

    @cal_AstTypeName.setter
    def cal_AstTypeName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName", None)
        self.__cal_AstTypeName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNamespace14"):
                opp_val = getattr(old_value, "cal_AstNamespace14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace14"):
                opp_val = getattr(value, "cal_AstNamespace14", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstTypeName83(self):
        return self.__cal_AstTypeName83

    @cal_AstTypeName83.setter
    def cal_AstTypeName83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName83", None)
        self.__cal_AstTypeName83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeDefinitionParameter82"):
                opp_val = getattr(old_value, "cal_AstTypeDefinitionParameter82", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeDefinitionParameter82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeDefinitionParameter82"):
                opp_val = getattr(value, "cal_AstTypeDefinitionParameter82", None)
                setattr(value, "cal_AstTypeDefinitionParameter82", self)

    @property
    def cal_AstTypeName71(self):
        return self.__cal_AstTypeName71

    @cal_AstTypeName71.setter
    def cal_AstTypeName71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName71", None)
        self.__cal_AstTypeName71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstTypeDefinitionParameter"):
                    opp_val = getattr(item, "cal_AstTypeDefinitionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstTypeDefinitionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstTypeDefinitionParameter"):
                    opp_val = getattr(item, "cal_AstTypeDefinitionParameter", None)
                    
                    setattr(item, "cal_AstTypeDefinitionParameter", self)
                    

    @property
    def cal_AstTypeName272(self):
        return self.__cal_AstTypeName272

    @cal_AstTypeName272.setter
    def cal_AstTypeName272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName272", None)
        self.__cal_AstTypeName272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType271"):
                opp_val = getattr(old_value, "cal_AstType271", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType271"):
                opp_val = getattr(value, "cal_AstType271", None)
                setattr(value, "cal_AstType271", self)

    @property
    def cal_AstTypeName73(self):
        return self.__cal_AstTypeName73

    @cal_AstTypeName73.setter
    def cal_AstTypeName73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName73", None)
        self.__cal_AstTypeName73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstFunction74"):
                    opp_val = getattr(item, "cal_AstFunction74", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstFunction74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstFunction74"):
                    opp_val = getattr(item, "cal_AstFunction74", None)
                    
                    setattr(item, "cal_AstFunction74", self)
                    

    @property
    def cal_AstTypeName76(self):
        return self.__cal_AstTypeName76

    @cal_AstTypeName76.setter
    def cal_AstTypeName76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstTypeName__cal_AstTypeName76", None)
        self.__cal_AstTypeName76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType77"):
                opp_val = getattr(old_value, "cal_AstType77", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType77"):
                opp_val = getattr(value, "cal_AstType77", None)
                setattr(value, "cal_AstType77", self)

class cal_AstAnnotation:

    def __init__(self, name: str, cal_AstAnnotation: "cal_AstNamespace" = None, cal_AstAnnotation20: "cal_AstEntity" = None, cal_AstAnnotation64: "cal_AstVariable" = None, cal_AstAnnotation89: "cal_AstFunction" = None, cal_AstAnnotation120: "cal_AstPort" = None, cal_AstAnnotation126: "cal_AstProcedure" = None, cal_AstAnnotation154: "cal_AstAction" = None, cal_AstAnnotation297: set["cal_AstAnnotationArgument"] = None):
        self.name = name
        self.cal_AstAnnotation = cal_AstAnnotation
        self.cal_AstAnnotation20 = cal_AstAnnotation20
        self.cal_AstAnnotation64 = cal_AstAnnotation64
        self.cal_AstAnnotation89 = cal_AstAnnotation89
        self.cal_AstAnnotation120 = cal_AstAnnotation120
        self.cal_AstAnnotation126 = cal_AstAnnotation126
        self.cal_AstAnnotation154 = cal_AstAnnotation154
        self.cal_AstAnnotation297 = cal_AstAnnotation297 if cal_AstAnnotation297 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstAnnotation126(self):
        return self.__cal_AstAnnotation126

    @cal_AstAnnotation126.setter
    def cal_AstAnnotation126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation126", None)
        self.__cal_AstAnnotation126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure125"):
                opp_val = getattr(old_value, "cal_AstProcedure125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure125"):
                opp_val = getattr(value, "cal_AstProcedure125", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation297(self):
        return self.__cal_AstAnnotation297

    @cal_AstAnnotation297.setter
    def cal_AstAnnotation297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation297", None)
        self.__cal_AstAnnotation297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotationArgument"):
                    opp_val = getattr(item, "cal_AstAnnotationArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotationArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotationArgument"):
                    opp_val = getattr(item, "cal_AstAnnotationArgument", None)
                    
                    setattr(item, "cal_AstAnnotationArgument", self)
                    

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
            if hasattr(old_value, "cal_AstNamespace12"):
                opp_val = getattr(old_value, "cal_AstNamespace12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace12"):
                opp_val = getattr(value, "cal_AstNamespace12", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation64(self):
        return self.__cal_AstAnnotation64

    @cal_AstAnnotation64.setter
    def cal_AstAnnotation64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation64", None)
        self.__cal_AstAnnotation64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstVariable63"):
                opp_val = getattr(old_value, "cal_AstVariable63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstVariable63"):
                opp_val = getattr(value, "cal_AstVariable63", None)
                if opp_val is None:
                    setattr(value, "cal_AstVariable63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation89(self):
        return self.__cal_AstAnnotation89

    @cal_AstAnnotation89.setter
    def cal_AstAnnotation89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation89", None)
        self.__cal_AstAnnotation89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstFunction88"):
                opp_val = getattr(old_value, "cal_AstFunction88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstFunction88"):
                opp_val = getattr(value, "cal_AstFunction88", None)
                if opp_val is None:
                    setattr(value, "cal_AstFunction88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation120(self):
        return self.__cal_AstAnnotation120

    @cal_AstAnnotation120.setter
    def cal_AstAnnotation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation120", None)
        self.__cal_AstAnnotation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstPort119"):
                opp_val = getattr(old_value, "cal_AstPort119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstPort119"):
                opp_val = getattr(value, "cal_AstPort119", None)
                if opp_val is None:
                    setattr(value, "cal_AstPort119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation154(self):
        return self.__cal_AstAnnotation154

    @cal_AstAnnotation154.setter
    def cal_AstAnnotation154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation154", None)
        self.__cal_AstAnnotation154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction153"):
                opp_val = getattr(old_value, "cal_AstAction153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction153"):
                opp_val = getattr(value, "cal_AstAction153", None)
                if opp_val is None:
                    setattr(value, "cal_AstAction153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstAnnotation20(self):
        return self.__cal_AstAnnotation20

    @cal_AstAnnotation20.setter
    def cal_AstAnnotation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstAnnotation__cal_AstAnnotation20", None)
        self.__cal_AstAnnotation20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstEntity19"):
                opp_val = getattr(old_value, "cal_AstEntity19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstEntity19"):
                opp_val = getattr(value, "cal_AstEntity19", None)
                if opp_val is None:
                    setattr(value, "cal_AstEntity19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_EObject:

    pass
class cal_AstVariable:

    def __init__(self, constant: bool, name: str, cal_AstVariable: "cal_AstNamespace" = None, cal_AstVariable25: "cal_AstAbstractActor" = None, cal_AstVariable32: "cal_AstNetwork" = None, cal_AstVariable60: "cal_AstExpression" = None, cal_AstVariable63: set["cal_AstAnnotation"] = None, cal_AstVariable66: "cal_AstType" = None, cal_AstVariable68: set["cal_AstExpression"] = None, cal_AstVariable80: "cal_AstTypeDefinitionParameter" = None, cal_AstVariable86: "cal_AstFunction" = None, cal_AstVariable92: "cal_AstFunction" = None, cal_AstVariable98: "cal_AstFunction" = None, cal_AstVariable113: "cal_AstActor" = None, cal_AstVariable129: "cal_AstProcedure" = None, cal_AstVariable132: "cal_AstProcedure" = None, cal_AstVariable167: "cal_AstAction" = None, cal_AstVariable176: "cal_AstInputPattern" = None, cal_AstVariable206: "cal_AstStatementForeach" = None, cal_AstVariable217: "cal_AstStatementBlock" = None, cal_AstVariable212: "cal_AstForeachGenerator" = None, cal_AstVariable281: "cal_AstType" = None, cal_AstVariable253: "cal_AstGenerator" = None, cal_AstVariable292: "cal_AstVariableReference" = None):
        self.constant = constant
        self.name = name
        self.cal_AstVariable = cal_AstVariable
        self.cal_AstVariable25 = cal_AstVariable25
        self.cal_AstVariable32 = cal_AstVariable32
        self.cal_AstVariable60 = cal_AstVariable60
        self.cal_AstVariable63 = cal_AstVariable63 if cal_AstVariable63 is not None else set()
        self.cal_AstVariable66 = cal_AstVariable66
        self.cal_AstVariable68 = cal_AstVariable68 if cal_AstVariable68 is not None else set()
        self.cal_AstVariable80 = cal_AstVariable80
        self.cal_AstVariable86 = cal_AstVariable86
        self.cal_AstVariable92 = cal_AstVariable92
        self.cal_AstVariable98 = cal_AstVariable98
        self.cal_AstVariable113 = cal_AstVariable113
        self.cal_AstVariable129 = cal_AstVariable129
        self.cal_AstVariable132 = cal_AstVariable132
        self.cal_AstVariable167 = cal_AstVariable167
        self.cal_AstVariable176 = cal_AstVariable176
        self.cal_AstVariable206 = cal_AstVariable206
        self.cal_AstVariable217 = cal_AstVariable217
        self.cal_AstVariable212 = cal_AstVariable212
        self.cal_AstVariable281 = cal_AstVariable281
        self.cal_AstVariable253 = cal_AstVariable253
        self.cal_AstVariable292 = cal_AstVariable292
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def cal_AstVariable167(self):
        return self.__cal_AstVariable167

    @cal_AstVariable167.setter
    def cal_AstVariable167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable167", None)
        self.__cal_AstVariable167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAction166"):
                opp_val = getattr(old_value, "cal_AstAction166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAction166"):
                opp_val = getattr(value, "cal_AstAction166", None)
                if opp_val is None:
                    setattr(value, "cal_AstAction166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable86(self):
        return self.__cal_AstVariable86

    @cal_AstVariable86.setter
    def cal_AstVariable86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable86", None)
        self.__cal_AstVariable86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstFunction85"):
                opp_val = getattr(old_value, "cal_AstFunction85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstFunction85"):
                opp_val = getattr(value, "cal_AstFunction85", None)
                if opp_val is None:
                    setattr(value, "cal_AstFunction85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable292(self):
        return self.__cal_AstVariable292

    @cal_AstVariable292.setter
    def cal_AstVariable292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable292", None)
        self.__cal_AstVariable292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstVariableReference291"):
                opp_val = getattr(old_value, "cal_AstVariableReference291", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstVariableReference291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstVariableReference291"):
                opp_val = getattr(value, "cal_AstVariableReference291", None)
                setattr(value, "cal_AstVariableReference291", self)

    @property
    def cal_AstVariable253(self):
        return self.__cal_AstVariable253

    @cal_AstVariable253.setter
    def cal_AstVariable253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable253", None)
        self.__cal_AstVariable253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstGenerator252"):
                opp_val = getattr(old_value, "cal_AstGenerator252", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstGenerator252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstGenerator252"):
                opp_val = getattr(value, "cal_AstGenerator252", None)
                setattr(value, "cal_AstGenerator252", self)

    @property
    def cal_AstVariable206(self):
        return self.__cal_AstVariable206

    @cal_AstVariable206.setter
    def cal_AstVariable206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable206", None)
        self.__cal_AstVariable206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstStatementForeach205"):
                opp_val = getattr(old_value, "cal_AstStatementForeach205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstStatementForeach205"):
                opp_val = getattr(value, "cal_AstStatementForeach205", None)
                if opp_val is None:
                    setattr(value, "cal_AstStatementForeach205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable25(self):
        return self.__cal_AstVariable25

    @cal_AstVariable25.setter
    def cal_AstVariable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable25", None)
        self.__cal_AstVariable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstAbstractActor24"):
                opp_val = getattr(old_value, "cal_AstAbstractActor24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstAbstractActor24"):
                opp_val = getattr(value, "cal_AstAbstractActor24", None)
                if opp_val is None:
                    setattr(value, "cal_AstAbstractActor24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable217(self):
        return self.__cal_AstVariable217

    @cal_AstVariable217.setter
    def cal_AstVariable217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable217", None)
        self.__cal_AstVariable217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstStatementBlock"):
                opp_val = getattr(old_value, "cal_AstStatementBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstStatementBlock"):
                opp_val = getattr(value, "cal_AstStatementBlock", None)
                if opp_val is None:
                    setattr(value, "cal_AstStatementBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable80(self):
        return self.__cal_AstVariable80

    @cal_AstVariable80.setter
    def cal_AstVariable80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable80", None)
        self.__cal_AstVariable80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeDefinitionParameter79"):
                opp_val = getattr(old_value, "cal_AstTypeDefinitionParameter79", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstTypeDefinitionParameter79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeDefinitionParameter79"):
                opp_val = getattr(value, "cal_AstTypeDefinitionParameter79", None)
                setattr(value, "cal_AstTypeDefinitionParameter79", self)

    @property
    def cal_AstVariable32(self):
        return self.__cal_AstVariable32

    @cal_AstVariable32.setter
    def cal_AstVariable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable32", None)
        self.__cal_AstVariable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNetwork"):
                opp_val = getattr(old_value, "cal_AstNetwork", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNetwork"):
                opp_val = getattr(value, "cal_AstNetwork", None)
                if opp_val is None:
                    setattr(value, "cal_AstNetwork", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable98(self):
        return self.__cal_AstVariable98

    @cal_AstVariable98.setter
    def cal_AstVariable98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable98", None)
        self.__cal_AstVariable98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstFunction97"):
                opp_val = getattr(old_value, "cal_AstFunction97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstFunction97"):
                opp_val = getattr(value, "cal_AstFunction97", None)
                if opp_val is None:
                    setattr(value, "cal_AstFunction97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable129(self):
        return self.__cal_AstVariable129

    @cal_AstVariable129.setter
    def cal_AstVariable129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable129", None)
        self.__cal_AstVariable129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure128"):
                opp_val = getattr(old_value, "cal_AstProcedure128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure128"):
                opp_val = getattr(value, "cal_AstProcedure128", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable63(self):
        return self.__cal_AstVariable63

    @cal_AstVariable63.setter
    def cal_AstVariable63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable63", None)
        self.__cal_AstVariable63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation64"):
                    opp_val = getattr(item, "cal_AstAnnotation64", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation64"):
                    opp_val = getattr(item, "cal_AstAnnotation64", None)
                    
                    setattr(item, "cal_AstAnnotation64", self)
                    

    @property
    def cal_AstVariable60(self):
        return self.__cal_AstVariable60

    @cal_AstVariable60.setter
    def cal_AstVariable60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable60", None)
        self.__cal_AstVariable60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression61"):
                opp_val = getattr(old_value, "cal_AstExpression61", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression61"):
                opp_val = getattr(value, "cal_AstExpression61", None)
                setattr(value, "cal_AstExpression61", self)

    @property
    def cal_AstVariable212(self):
        return self.__cal_AstVariable212

    @cal_AstVariable212.setter
    def cal_AstVariable212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable212", None)
        self.__cal_AstVariable212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstForeachGenerator211"):
                opp_val = getattr(old_value, "cal_AstForeachGenerator211", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstForeachGenerator211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstForeachGenerator211"):
                opp_val = getattr(value, "cal_AstForeachGenerator211", None)
                setattr(value, "cal_AstForeachGenerator211", self)

    @property
    def cal_AstVariable176(self):
        return self.__cal_AstVariable176

    @cal_AstVariable176.setter
    def cal_AstVariable176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable176", None)
        self.__cal_AstVariable176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstInputPattern175"):
                opp_val = getattr(old_value, "cal_AstInputPattern175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstInputPattern175"):
                opp_val = getattr(value, "cal_AstInputPattern175", None)
                if opp_val is None:
                    setattr(value, "cal_AstInputPattern175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable68(self):
        return self.__cal_AstVariable68

    @cal_AstVariable68.setter
    def cal_AstVariable68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable68", None)
        self.__cal_AstVariable68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstExpression69"):
                    opp_val = getattr(item, "cal_AstExpression69", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstExpression69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstExpression69"):
                    opp_val = getattr(item, "cal_AstExpression69", None)
                    
                    setattr(item, "cal_AstExpression69", self)
                    

    @property
    def cal_AstVariable113(self):
        return self.__cal_AstVariable113

    @cal_AstVariable113.setter
    def cal_AstVariable113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable113", None)
        self.__cal_AstVariable113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor112"):
                opp_val = getattr(old_value, "cal_AstActor112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor112"):
                opp_val = getattr(value, "cal_AstActor112", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable66(self):
        return self.__cal_AstVariable66

    @cal_AstVariable66.setter
    def cal_AstVariable66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable66", None)
        self.__cal_AstVariable66 = value
        
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
    def cal_AstVariable(self):
        return self.__cal_AstVariable

    @cal_AstVariable.setter
    def cal_AstVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable", None)
        self.__cal_AstVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNamespace8"):
                opp_val = getattr(old_value, "cal_AstNamespace8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace8"):
                opp_val = getattr(value, "cal_AstNamespace8", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable92(self):
        return self.__cal_AstVariable92

    @cal_AstVariable92.setter
    def cal_AstVariable92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable92", None)
        self.__cal_AstVariable92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstFunction91"):
                opp_val = getattr(old_value, "cal_AstFunction91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstFunction91"):
                opp_val = getattr(value, "cal_AstFunction91", None)
                if opp_val is None:
                    setattr(value, "cal_AstFunction91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable281(self):
        return self.__cal_AstVariable281

    @cal_AstVariable281.setter
    def cal_AstVariable281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable281", None)
        self.__cal_AstVariable281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType280"):
                opp_val = getattr(old_value, "cal_AstType280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType280"):
                opp_val = getattr(value, "cal_AstType280", None)
                if opp_val is None:
                    setattr(value, "cal_AstType280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstVariable132(self):
        return self.__cal_AstVariable132

    @cal_AstVariable132.setter
    def cal_AstVariable132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstVariable__cal_AstVariable132", None)
        self.__cal_AstVariable132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstProcedure131"):
                opp_val = getattr(old_value, "cal_AstProcedure131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstProcedure131"):
                opp_val = getattr(value, "cal_AstProcedure131", None)
                if opp_val is None:
                    setattr(value, "cal_AstProcedure131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstFunction(AstExternalFunction):

    def __init__(self, name: str, cal_AstFunction: "cal_AstNamespace" = None, cal_AstFunction85: set["cal_AstVariable"] = None, cal_AstFunction88: set["cal_AstAnnotation"] = None, cal_AstFunction91: set["cal_AstVariable"] = None, cal_AstFunction94: "cal_AstType" = None, cal_AstFunction97: set["cal_AstVariable"] = None, cal_AstFunction100: "cal_AstExpression" = None, cal_AstFunction103: "cal_AstActor" = None, cal_AstFunction74: "cal_AstTypeName" = None, cal_AstFunction235: "cal_AstExpressionCall" = None):
        self.name = name
        self.cal_AstFunction = cal_AstFunction
        self.cal_AstFunction85 = cal_AstFunction85 if cal_AstFunction85 is not None else set()
        self.cal_AstFunction88 = cal_AstFunction88 if cal_AstFunction88 is not None else set()
        self.cal_AstFunction91 = cal_AstFunction91 if cal_AstFunction91 is not None else set()
        self.cal_AstFunction94 = cal_AstFunction94
        self.cal_AstFunction97 = cal_AstFunction97 if cal_AstFunction97 is not None else set()
        self.cal_AstFunction100 = cal_AstFunction100
        self.cal_AstFunction103 = cal_AstFunction103
        self.cal_AstFunction74 = cal_AstFunction74
        self.cal_AstFunction235 = cal_AstFunction235
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstFunction103(self):
        return self.__cal_AstFunction103

    @cal_AstFunction103.setter
    def cal_AstFunction103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction103", None)
        self.__cal_AstFunction103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstActor"):
                opp_val = getattr(old_value, "cal_AstActor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstActor"):
                opp_val = getattr(value, "cal_AstActor", None)
                if opp_val is None:
                    setattr(value, "cal_AstActor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstFunction85(self):
        return self.__cal_AstFunction85

    @cal_AstFunction85.setter
    def cal_AstFunction85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction85", None)
        self.__cal_AstFunction85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable86"):
                    opp_val = getattr(item, "cal_AstVariable86", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable86"):
                    opp_val = getattr(item, "cal_AstVariable86", None)
                    
                    setattr(item, "cal_AstVariable86", self)
                    

    @property
    def cal_AstFunction88(self):
        return self.__cal_AstFunction88

    @cal_AstFunction88.setter
    def cal_AstFunction88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction88", None)
        self.__cal_AstFunction88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstAnnotation89"):
                    opp_val = getattr(item, "cal_AstAnnotation89", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstAnnotation89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstAnnotation89"):
                    opp_val = getattr(item, "cal_AstAnnotation89", None)
                    
                    setattr(item, "cal_AstAnnotation89", self)
                    

    @property
    def cal_AstFunction100(self):
        return self.__cal_AstFunction100

    @cal_AstFunction100.setter
    def cal_AstFunction100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction100", None)
        self.__cal_AstFunction100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpression101"):
                opp_val = getattr(old_value, "cal_AstExpression101", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpression101"):
                opp_val = getattr(value, "cal_AstExpression101", None)
                setattr(value, "cal_AstExpression101", self)

    @property
    def cal_AstFunction91(self):
        return self.__cal_AstFunction91

    @cal_AstFunction91.setter
    def cal_AstFunction91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction91", None)
        self.__cal_AstFunction91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable92"):
                    opp_val = getattr(item, "cal_AstVariable92", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable92"):
                    opp_val = getattr(item, "cal_AstVariable92", None)
                    
                    setattr(item, "cal_AstVariable92", self)
                    

    @property
    def cal_AstFunction74(self):
        return self.__cal_AstFunction74

    @cal_AstFunction74.setter
    def cal_AstFunction74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction74", None)
        self.__cal_AstFunction74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstTypeName73"):
                opp_val = getattr(old_value, "cal_AstTypeName73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstTypeName73"):
                opp_val = getattr(value, "cal_AstTypeName73", None)
                if opp_val is None:
                    setattr(value, "cal_AstTypeName73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstFunction(self):
        return self.__cal_AstFunction

    @cal_AstFunction.setter
    def cal_AstFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction", None)
        self.__cal_AstFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNamespace6"):
                opp_val = getattr(old_value, "cal_AstNamespace6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace6"):
                opp_val = getattr(value, "cal_AstNamespace6", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstFunction97(self):
        return self.__cal_AstFunction97

    @cal_AstFunction97.setter
    def cal_AstFunction97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction97", None)
        self.__cal_AstFunction97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable98"):
                    opp_val = getattr(item, "cal_AstVariable98", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable98"):
                    opp_val = getattr(item, "cal_AstVariable98", None)
                    
                    setattr(item, "cal_AstVariable98", self)
                    

    @property
    def cal_AstFunction94(self):
        return self.__cal_AstFunction94

    @cal_AstFunction94.setter
    def cal_AstFunction94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction94", None)
        self.__cal_AstFunction94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstType95"):
                opp_val = getattr(old_value, "cal_AstType95", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstType95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstType95"):
                opp_val = getattr(value, "cal_AstType95", None)
                setattr(value, "cal_AstType95", self)

    @property
    def cal_AstFunction235(self):
        return self.__cal_AstFunction235

    @cal_AstFunction235.setter
    def cal_AstFunction235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstFunction__cal_AstFunction235", None)
        self.__cal_AstFunction235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstExpressionCall"):
                opp_val = getattr(old_value, "cal_AstExpressionCall", None)
                if opp_val == self:
                    setattr(old_value, "cal_AstExpressionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstExpressionCall"):
                opp_val = getattr(value, "cal_AstExpressionCall", None)
                setattr(value, "cal_AstExpressionCall", self)

class cal_Import:

    def __init__(self, importedNamespace: str, cal_Import: "cal_AstNamespace" = None):
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
            if hasattr(old_value, "cal_AstNamespace2"):
                opp_val = getattr(old_value, "cal_AstNamespace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace2"):
                opp_val = getattr(value, "cal_AstNamespace2", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cal_AstUnit:

    pass
class AstTop:

    pass
class cal_AstNamespace(AstTop, AstPackage, AstUnit):

    def __init__(self, name: str, cal_AstNamespace: set["cal_AstEntity"] = None, cal_AstNamespace2: set["cal_Import"] = None, cal_AstNamespace4: set["cal_AstUnit"] = None, cal_AstNamespace6: set["cal_AstFunction"] = None, cal_AstNamespace8: set["cal_AstVariable"] = None, cal_AstNamespace10: set["cal_EObject"] = None, cal_AstNamespace12: set["cal_AstAnnotation"] = None, cal_AstNamespace14: set["cal_AstTypeName"] = None, cal_AstNamespace17: "cal_AstNamespace" = None, cal_AstNamespace15: set["cal_AstNamespace"] = None):
        self.name = name
        self.cal_AstNamespace = cal_AstNamespace if cal_AstNamespace is not None else set()
        self.cal_AstNamespace2 = cal_AstNamespace2 if cal_AstNamespace2 is not None else set()
        self.cal_AstNamespace4 = cal_AstNamespace4 if cal_AstNamespace4 is not None else set()
        self.cal_AstNamespace6 = cal_AstNamespace6 if cal_AstNamespace6 is not None else set()
        self.cal_AstNamespace8 = cal_AstNamespace8 if cal_AstNamespace8 is not None else set()
        self.cal_AstNamespace10 = cal_AstNamespace10 if cal_AstNamespace10 is not None else set()
        self.cal_AstNamespace12 = cal_AstNamespace12 if cal_AstNamespace12 is not None else set()
        self.cal_AstNamespace14 = cal_AstNamespace14 if cal_AstNamespace14 is not None else set()
        self.cal_AstNamespace17 = cal_AstNamespace17
        self.cal_AstNamespace15 = cal_AstNamespace15 if cal_AstNamespace15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cal_AstNamespace12(self):
        return self.__cal_AstNamespace12

    @cal_AstNamespace12.setter
    def cal_AstNamespace12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace12", None)
        self.__cal_AstNamespace12 = value if value is not None else set()
        
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
    def cal_AstNamespace6(self):
        return self.__cal_AstNamespace6

    @cal_AstNamespace6.setter
    def cal_AstNamespace6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace6", None)
        self.__cal_AstNamespace6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstFunction"):
                    opp_val = getattr(item, "cal_AstFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstFunction"):
                    opp_val = getattr(item, "cal_AstFunction", None)
                    
                    setattr(item, "cal_AstFunction", self)
                    

    @property
    def cal_AstNamespace10(self):
        return self.__cal_AstNamespace10

    @cal_AstNamespace10.setter
    def cal_AstNamespace10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace10", None)
        self.__cal_AstNamespace10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_EObject"):
                    opp_val = getattr(item, "cal_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_EObject"):
                    opp_val = getattr(item, "cal_EObject", None)
                    
                    setattr(item, "cal_EObject", self)
                    

    @property
    def cal_AstNamespace14(self):
        return self.__cal_AstNamespace14

    @cal_AstNamespace14.setter
    def cal_AstNamespace14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace14", None)
        self.__cal_AstNamespace14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstTypeName"):
                    opp_val = getattr(item, "cal_AstTypeName", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstTypeName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstTypeName"):
                    opp_val = getattr(item, "cal_AstTypeName", None)
                    
                    setattr(item, "cal_AstTypeName", self)
                    

    @property
    def cal_AstNamespace4(self):
        return self.__cal_AstNamespace4

    @cal_AstNamespace4.setter
    def cal_AstNamespace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace4", None)
        self.__cal_AstNamespace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstUnit"):
                    opp_val = getattr(item, "cal_AstUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstUnit"):
                    opp_val = getattr(item, "cal_AstUnit", None)
                    
                    setattr(item, "cal_AstUnit", self)
                    

    @property
    def cal_AstNamespace2(self):
        return self.__cal_AstNamespace2

    @cal_AstNamespace2.setter
    def cal_AstNamespace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace2", None)
        self.__cal_AstNamespace2 = value if value is not None else set()
        
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
    def cal_AstNamespace(self):
        return self.__cal_AstNamespace

    @cal_AstNamespace.setter
    def cal_AstNamespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace", None)
        self.__cal_AstNamespace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstEntity"):
                    opp_val = getattr(item, "cal_AstEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstEntity"):
                    opp_val = getattr(item, "cal_AstEntity", None)
                    
                    setattr(item, "cal_AstEntity", self)
                    

    @property
    def cal_AstNamespace17(self):
        return self.__cal_AstNamespace17

    @cal_AstNamespace17.setter
    def cal_AstNamespace17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace17", None)
        self.__cal_AstNamespace17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cal_AstNamespace15"):
                opp_val = getattr(old_value, "cal_AstNamespace15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cal_AstNamespace15"):
                opp_val = getattr(value, "cal_AstNamespace15", None)
                if opp_val is None:
                    setattr(value, "cal_AstNamespace15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cal_AstNamespace8(self):
        return self.__cal_AstNamespace8

    @cal_AstNamespace8.setter
    def cal_AstNamespace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace8", None)
        self.__cal_AstNamespace8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstVariable"):
                    opp_val = getattr(item, "cal_AstVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstVariable"):
                    opp_val = getattr(item, "cal_AstVariable", None)
                    
                    setattr(item, "cal_AstVariable", self)
                    

    @property
    def cal_AstNamespace15(self):
        return self.__cal_AstNamespace15

    @cal_AstNamespace15.setter
    def cal_AstNamespace15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cal_AstNamespace__cal_AstNamespace15", None)
        self.__cal_AstNamespace15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cal_AstNamespace17"):
                    opp_val = getattr(item, "cal_AstNamespace17", None)
                    
                    if opp_val == self:
                        setattr(item, "cal_AstNamespace17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cal_AstNamespace17"):
                    opp_val = getattr(item, "cal_AstNamespace17", None)
                    
                    setattr(item, "cal_AstNamespace17", self)
                    

class cal_AstPackage(AstTop):

    pass
class cal_AstTop:

    pass
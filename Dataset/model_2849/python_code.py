from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EqualityOperator(Enum):
    EQ = "EQ"
    NE = "NE"
class ImportVisibilityIndicator(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
class AssignmentOperator(Enum):
    MINUSASSIGN = "MINUSASSIGN"
    STARASSIGN = "STARASSIGN"
    SLASHASSIGN = "SLASHASSIGN"
    REMASSIGN = "REMASSIGN"
    ANSASSIGN = "ANSASSIGN"
    ORASSIGN = "ORASSIGN"
    XORASSIGN = "XORASSIGN"
    LSHIFTASSIGN = "LSHIFTASSIGN"
    RSHIFTASSIGN = "RSHIFTASSIGN"
    URSHIFTASSIGN = "URSHIFTASSIGN"
    ASSIGN = "ASSIGN"
    PLUSASSIGN = "PLUSASSIGN"
class ShiftOperator(Enum):
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    URSHIFT = "URSHIFT"
class AffixOperator(Enum):
    INCR = "INCR"
    DECR = "DECR"
class RelationalOperator(Enum):
    LT = "LT"
    GT = "GT"
    LE = "LE"
    GE = "GE"
class ClassificationOperator(Enum):
    INSTANCEOF = "INSTANCEOF"
    HASTYPE = "HASTYPE"
class MultiplicativeOperator(Enum):
    REM = "REM"
    STAR = "STAR"
    SLASH = "SLASH"
class ParameterDirection(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class LinkOperation(Enum):
    CREATE_LINK = "CREATE_LINK"
    DESTROY_LINK = "DESTROY_LINK"
    CLEAR_ASSOC = "CLEAR_ASSOC"
class NumericUnaryOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
class AdditiveOperator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"


############################################
# Definition of Classes
############################################

class alf_ReclassifyAllClause:

    pass
class alf_ClassificationToClause:

    pass
class alf_ClassificationFromClause:

    pass
class alf_ClassificationClause:

    pass
class alf_SimpleAcceptStatementCompletion:

    pass
class alf_AcceptClause:

    pass
class alf_AcceptBlock:

    pass
class alf_CompoundAcceptStatementCompletion:

    pass
class alf_LoopVariableDefinition:

    pass
class alf_ForControl:

    pass
class alf_NonEmptyStatementSequence:

    pass
class alf_SwitchCase:

    pass
class alf_SwitchDefaultClause:

    pass
class alf_SwitchClause:

    pass
class alf_NonFinalClause:

    pass
class alf_ConcurrentClauses:

    pass
class alf_FinalClause:

    pass
class alf_SequentialClauses:

    pass
class alf_LocalNameDeclarationStatementCompletion:

    pass
class alf_Annotations:

    pass
class Statement:

    pass
class alf_SwitchStatement(Statement):

    pass
class alf_IfStatement(Statement):

    pass
class alf_BlockStatement(Statement):

    pass
class alf_ClassifyStatement(Statement):

    pass
class alf_EmptyStatement(Statement):

    pass
class alf_LocalNameDeclarationStatement(Statement):

    pass
class alf_WhileStatement(Statement):

    pass
class alf_LocalNameDeclarationOrExpressionStatement(Statement):

    pass
class alf_AcceptStatement(Statement):

    pass
class alf_DoStatement(Statement):

    pass
class alf_ForStatement(Statement):

    pass
class alf_ReturnStatement(Statement):

    pass
class alf_BreakStatement(Statement):

    pass
class alf_AnnotatedStatement(Statement):

    pass
class alf_InLineStatement(Statement):

    def __init__(self, id: str, alf_InLineStatement: "alf_Name" = None):
        self.id = id
        self.alf_InLineStatement = alf_InLineStatement
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alf_InLineStatement(self):
        return self.__alf_InLineStatement

    @alf_InLineStatement.setter
    def alf_InLineStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_InLineStatement__alf_InLineStatement", None)
        self.__alf_InLineStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name652"):
                opp_val = getattr(old_value, "alf_Name652", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name652", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name652"):
                opp_val = getattr(value, "alf_Name652", None)
                setattr(value, "alf_Name652", self)

class alf_NameList:

    pass
class alf_Annotation:

    def __init__(self, id: str, alf_Annotation: "alf_Annotations" = None, alf_Annotation647: "alf_NameList" = None):
        self.id = id
        self.alf_Annotation = alf_Annotation
        self.alf_Annotation647 = alf_Annotation647
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alf_Annotation(self):
        return self.__alf_Annotation

    @alf_Annotation.setter
    def alf_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Annotation__alf_Annotation", None)
        self.__alf_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Annotations645"):
                opp_val = getattr(old_value, "alf_Annotations645", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Annotations645"):
                opp_val = getattr(value, "alf_Annotations645", None)
                if opp_val is None:
                    setattr(value, "alf_Annotations645", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_Annotation647(self):
        return self.__alf_Annotation647

    @alf_Annotation647.setter
    def alf_Annotation647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Annotation__alf_Annotation647", None)
        self.__alf_Annotation647 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameList"):
                opp_val = getattr(old_value, "alf_NameList", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameList"):
                opp_val = getattr(value, "alf_NameList", None)
                setattr(value, "alf_NameList", self)

class alf_Statement:

    pass
class alf_DocumentedStatement:

    def __init__(self, comment: str, alf_DocumentedStatement: "alf_StatementSequence" = None, alf_DocumentedStatement636: "alf_Statement" = None, alf_DocumentedStatement721: "alf_NonEmptyStatementSequence" = None):
        self.comment = comment
        self.alf_DocumentedStatement = alf_DocumentedStatement
        self.alf_DocumentedStatement636 = alf_DocumentedStatement636
        self.alf_DocumentedStatement721 = alf_DocumentedStatement721
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_DocumentedStatement636(self):
        return self.__alf_DocumentedStatement636

    @alf_DocumentedStatement636.setter
    def alf_DocumentedStatement636(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement636", None)
        self.__alf_DocumentedStatement636 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Statement"):
                opp_val = getattr(old_value, "alf_Statement", None)
                if opp_val == self:
                    setattr(old_value, "alf_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Statement"):
                opp_val = getattr(value, "alf_Statement", None)
                setattr(value, "alf_Statement", self)

    @property
    def alf_DocumentedStatement721(self):
        return self.__alf_DocumentedStatement721

    @alf_DocumentedStatement721.setter
    def alf_DocumentedStatement721(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement721", None)
        self.__alf_DocumentedStatement721 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NonEmptyStatementSequence720"):
                opp_val = getattr(old_value, "alf_NonEmptyStatementSequence720", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NonEmptyStatementSequence720"):
                opp_val = getattr(value, "alf_NonEmptyStatementSequence720", None)
                if opp_val is None:
                    setattr(value, "alf_NonEmptyStatementSequence720", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_DocumentedStatement(self):
        return self.__alf_DocumentedStatement

    @alf_DocumentedStatement.setter
    def alf_DocumentedStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement", None)
        self.__alf_DocumentedStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StatementSequence"):
                opp_val = getattr(old_value, "alf_StatementSequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StatementSequence"):
                opp_val = getattr(value, "alf_StatementSequence", None)
                if opp_val is None:
                    setattr(value, "alf_StatementSequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_StatementSequence:

    pass
class alf_ConditionalOrExpression:

    pass
class ExpressionCompletion:

    pass
class alf_AssignmentExpressionCompletion(ExpressionCompletion):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class alf_ConditionalExpressionCompletion(ExpressionCompletion):

    pass
class alf_ConditionalExpression:

    pass
class alf_ConditionalOrExpressionCompletion:

    pass
class alf_ConditionalAndExpressionCompletion:

    pass
class alf_ConditionalAndExpression:

    pass
class alf_InclusiveOrExpressionCompletion:

    pass
class alf_InclusiveOrExpression:

    pass
class alf_ExclusiveOrExpressionCompletion:

    pass
class alf_ExclusiveOrExpression:

    pass
class alf_AndExpressionCompletion:

    pass
class alf_AndExpression:

    pass
class alf_ClassificationExpression:

    pass
class alf_EqualityExpressionCompletion:

    def __init__(self, operator: str, alf_EqualityExpressionCompletion580: "alf_AndExpressionCompletion" = None, alf_EqualityExpressionCompletion: "alf_ClassificationExpressionCompletion" = None, alf_EqualityExpressionCompletion572: set["alf_ClassificationExpression"] = None):
        self.operator = operator
        self.alf_EqualityExpressionCompletion580 = alf_EqualityExpressionCompletion580
        self.alf_EqualityExpressionCompletion = alf_EqualityExpressionCompletion
        self.alf_EqualityExpressionCompletion572 = alf_EqualityExpressionCompletion572 if alf_EqualityExpressionCompletion572 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_EqualityExpressionCompletion580(self):
        return self.__alf_EqualityExpressionCompletion580

    @alf_EqualityExpressionCompletion580.setter
    def alf_EqualityExpressionCompletion580(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpressionCompletion__alf_EqualityExpressionCompletion580", None)
        self.__alf_EqualityExpressionCompletion580 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AndExpressionCompletion579"):
                opp_val = getattr(old_value, "alf_AndExpressionCompletion579", None)
                if opp_val == self:
                    setattr(old_value, "alf_AndExpressionCompletion579", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AndExpressionCompletion579"):
                opp_val = getattr(value, "alf_AndExpressionCompletion579", None)
                setattr(value, "alf_AndExpressionCompletion579", self)

    @property
    def alf_EqualityExpressionCompletion572(self):
        return self.__alf_EqualityExpressionCompletion572

    @alf_EqualityExpressionCompletion572.setter
    def alf_EqualityExpressionCompletion572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpressionCompletion__alf_EqualityExpressionCompletion572", None)
        self.__alf_EqualityExpressionCompletion572 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_ClassificationExpression573"):
                    opp_val = getattr(item, "alf_ClassificationExpression573", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_ClassificationExpression573", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_ClassificationExpression573"):
                    opp_val = getattr(item, "alf_ClassificationExpression573", None)
                    
                    setattr(item, "alf_ClassificationExpression573", self)
                    

    @property
    def alf_EqualityExpressionCompletion(self):
        return self.__alf_EqualityExpressionCompletion

    @alf_EqualityExpressionCompletion.setter
    def alf_EqualityExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpressionCompletion__alf_EqualityExpressionCompletion", None)
        self.__alf_EqualityExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpressionCompletion570"):
                opp_val = getattr(old_value, "alf_ClassificationExpressionCompletion570", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpressionCompletion570", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpressionCompletion570"):
                opp_val = getattr(value, "alf_ClassificationExpressionCompletion570", None)
                setattr(value, "alf_ClassificationExpressionCompletion570", self)

class alf_EqualityExpression:

    pass
class alf_ClassificationExpressionCompletion:

    def __init__(self, operator: str, alf_ClassificationExpressionCompletion: "alf_ClassificationExpression" = None, alf_ClassificationExpressionCompletion559: "alf_RelationalExpressionCompletion" = None, alf_ClassificationExpressionCompletion562: "alf_QualifiedName" = None, alf_ClassificationExpressionCompletion568: "alf_EqualityExpression" = None, alf_ClassificationExpressionCompletion570: "alf_EqualityExpressionCompletion" = None):
        self.operator = operator
        self.alf_ClassificationExpressionCompletion = alf_ClassificationExpressionCompletion
        self.alf_ClassificationExpressionCompletion559 = alf_ClassificationExpressionCompletion559
        self.alf_ClassificationExpressionCompletion562 = alf_ClassificationExpressionCompletion562
        self.alf_ClassificationExpressionCompletion568 = alf_ClassificationExpressionCompletion568
        self.alf_ClassificationExpressionCompletion570 = alf_ClassificationExpressionCompletion570
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_ClassificationExpressionCompletion568(self):
        return self.__alf_ClassificationExpressionCompletion568

    @alf_ClassificationExpressionCompletion568.setter
    def alf_ClassificationExpressionCompletion568(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpressionCompletion__alf_ClassificationExpressionCompletion568", None)
        self.__alf_ClassificationExpressionCompletion568 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EqualityExpression567"):
                opp_val = getattr(old_value, "alf_EqualityExpression567", None)
                if opp_val == self:
                    setattr(old_value, "alf_EqualityExpression567", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EqualityExpression567"):
                opp_val = getattr(value, "alf_EqualityExpression567", None)
                setattr(value, "alf_EqualityExpression567", self)

    @property
    def alf_ClassificationExpressionCompletion559(self):
        return self.__alf_ClassificationExpressionCompletion559

    @alf_ClassificationExpressionCompletion559.setter
    def alf_ClassificationExpressionCompletion559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpressionCompletion__alf_ClassificationExpressionCompletion559", None)
        self.__alf_ClassificationExpressionCompletion559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpressionCompletion560"):
                opp_val = getattr(old_value, "alf_RelationalExpressionCompletion560", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpressionCompletion560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpressionCompletion560"):
                opp_val = getattr(value, "alf_RelationalExpressionCompletion560", None)
                setattr(value, "alf_RelationalExpressionCompletion560", self)

    @property
    def alf_ClassificationExpressionCompletion570(self):
        return self.__alf_ClassificationExpressionCompletion570

    @alf_ClassificationExpressionCompletion570.setter
    def alf_ClassificationExpressionCompletion570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpressionCompletion__alf_ClassificationExpressionCompletion570", None)
        self.__alf_ClassificationExpressionCompletion570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EqualityExpressionCompletion"):
                opp_val = getattr(old_value, "alf_EqualityExpressionCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_EqualityExpressionCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EqualityExpressionCompletion"):
                opp_val = getattr(value, "alf_EqualityExpressionCompletion", None)
                setattr(value, "alf_EqualityExpressionCompletion", self)

    @property
    def alf_ClassificationExpressionCompletion(self):
        return self.__alf_ClassificationExpressionCompletion

    @alf_ClassificationExpressionCompletion.setter
    def alf_ClassificationExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpressionCompletion__alf_ClassificationExpressionCompletion", None)
        self.__alf_ClassificationExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpression557"):
                opp_val = getattr(old_value, "alf_ClassificationExpression557", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpression557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpression557"):
                opp_val = getattr(value, "alf_ClassificationExpression557", None)
                setattr(value, "alf_ClassificationExpression557", self)

    @property
    def alf_ClassificationExpressionCompletion562(self):
        return self.__alf_ClassificationExpressionCompletion562

    @alf_ClassificationExpressionCompletion562.setter
    def alf_ClassificationExpressionCompletion562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpressionCompletion__alf_ClassificationExpressionCompletion562", None)
        self.__alf_ClassificationExpressionCompletion562 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedName563"):
                opp_val = getattr(old_value, "alf_QualifiedName563", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedName563", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedName563"):
                opp_val = getattr(value, "alf_QualifiedName563", None)
                setattr(value, "alf_QualifiedName563", self)

class alf_ShiftExpressionCompletion:

    def __init__(self, operator: str, alf_ShiftExpressionCompletion542: set["alf_AdditiveExpression"] = None, alf_ShiftExpressionCompletion550: "alf_RelationalExpressionCompletion" = None, alf_ShiftExpressionCompletion: "alf_ShiftExpression" = None, alf_ShiftExpressionCompletion539: "alf_AdditiveExpressionCompletion" = None):
        self.operator = operator
        self.alf_ShiftExpressionCompletion542 = alf_ShiftExpressionCompletion542 if alf_ShiftExpressionCompletion542 is not None else set()
        self.alf_ShiftExpressionCompletion550 = alf_ShiftExpressionCompletion550
        self.alf_ShiftExpressionCompletion = alf_ShiftExpressionCompletion
        self.alf_ShiftExpressionCompletion539 = alf_ShiftExpressionCompletion539
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_ShiftExpressionCompletion(self):
        return self.__alf_ShiftExpressionCompletion

    @alf_ShiftExpressionCompletion.setter
    def alf_ShiftExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpressionCompletion__alf_ShiftExpressionCompletion", None)
        self.__alf_ShiftExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression537"):
                opp_val = getattr(old_value, "alf_ShiftExpression537", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpression537", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression537"):
                opp_val = getattr(value, "alf_ShiftExpression537", None)
                setattr(value, "alf_ShiftExpression537", self)

    @property
    def alf_ShiftExpressionCompletion542(self):
        return self.__alf_ShiftExpressionCompletion542

    @alf_ShiftExpressionCompletion542.setter
    def alf_ShiftExpressionCompletion542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpressionCompletion__alf_ShiftExpressionCompletion542", None)
        self.__alf_ShiftExpressionCompletion542 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_AdditiveExpression543"):
                    opp_val = getattr(item, "alf_AdditiveExpression543", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_AdditiveExpression543", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_AdditiveExpression543"):
                    opp_val = getattr(item, "alf_AdditiveExpression543", None)
                    
                    setattr(item, "alf_AdditiveExpression543", self)
                    

    @property
    def alf_ShiftExpressionCompletion550(self):
        return self.__alf_ShiftExpressionCompletion550

    @alf_ShiftExpressionCompletion550.setter
    def alf_ShiftExpressionCompletion550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpressionCompletion__alf_ShiftExpressionCompletion550", None)
        self.__alf_ShiftExpressionCompletion550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpressionCompletion549"):
                opp_val = getattr(old_value, "alf_RelationalExpressionCompletion549", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpressionCompletion549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpressionCompletion549"):
                opp_val = getattr(value, "alf_RelationalExpressionCompletion549", None)
                setattr(value, "alf_RelationalExpressionCompletion549", self)

    @property
    def alf_ShiftExpressionCompletion539(self):
        return self.__alf_ShiftExpressionCompletion539

    @alf_ShiftExpressionCompletion539.setter
    def alf_ShiftExpressionCompletion539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpressionCompletion__alf_ShiftExpressionCompletion539", None)
        self.__alf_ShiftExpressionCompletion539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AdditiveExpressionCompletion540"):
                opp_val = getattr(old_value, "alf_AdditiveExpressionCompletion540", None)
                if opp_val == self:
                    setattr(old_value, "alf_AdditiveExpressionCompletion540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AdditiveExpressionCompletion540"):
                opp_val = getattr(value, "alf_AdditiveExpressionCompletion540", None)
                setattr(value, "alf_AdditiveExpressionCompletion540", self)

class alf_RelationalExpressionCompletion:

    def __init__(self, relationalOperator: str, alf_RelationalExpressionCompletion: "alf_RelationalExpression" = None, alf_RelationalExpressionCompletion549: "alf_ShiftExpressionCompletion" = None, alf_RelationalExpressionCompletion552: "alf_ShiftExpression" = None, alf_RelationalExpressionCompletion560: "alf_ClassificationExpressionCompletion" = None):
        self.relationalOperator = relationalOperator
        self.alf_RelationalExpressionCompletion = alf_RelationalExpressionCompletion
        self.alf_RelationalExpressionCompletion549 = alf_RelationalExpressionCompletion549
        self.alf_RelationalExpressionCompletion552 = alf_RelationalExpressionCompletion552
        self.alf_RelationalExpressionCompletion560 = alf_RelationalExpressionCompletion560
        
    @property
    def relationalOperator(self) -> str:
        return self.__relationalOperator

    @relationalOperator.setter
    def relationalOperator(self, relationalOperator: str):
        self.__relationalOperator = relationalOperator

    @property
    def alf_RelationalExpressionCompletion552(self):
        return self.__alf_RelationalExpressionCompletion552

    @alf_RelationalExpressionCompletion552.setter
    def alf_RelationalExpressionCompletion552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpressionCompletion__alf_RelationalExpressionCompletion552", None)
        self.__alf_RelationalExpressionCompletion552 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression553"):
                opp_val = getattr(old_value, "alf_ShiftExpression553", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpression553", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression553"):
                opp_val = getattr(value, "alf_ShiftExpression553", None)
                setattr(value, "alf_ShiftExpression553", self)

    @property
    def alf_RelationalExpressionCompletion549(self):
        return self.__alf_RelationalExpressionCompletion549

    @alf_RelationalExpressionCompletion549.setter
    def alf_RelationalExpressionCompletion549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpressionCompletion__alf_RelationalExpressionCompletion549", None)
        self.__alf_RelationalExpressionCompletion549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpressionCompletion550"):
                opp_val = getattr(old_value, "alf_ShiftExpressionCompletion550", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpressionCompletion550", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpressionCompletion550"):
                opp_val = getattr(value, "alf_ShiftExpressionCompletion550", None)
                setattr(value, "alf_ShiftExpressionCompletion550", self)

    @property
    def alf_RelationalExpressionCompletion560(self):
        return self.__alf_RelationalExpressionCompletion560

    @alf_RelationalExpressionCompletion560.setter
    def alf_RelationalExpressionCompletion560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpressionCompletion__alf_RelationalExpressionCompletion560", None)
        self.__alf_RelationalExpressionCompletion560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpressionCompletion559"):
                opp_val = getattr(old_value, "alf_ClassificationExpressionCompletion559", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpressionCompletion559", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpressionCompletion559"):
                opp_val = getattr(value, "alf_ClassificationExpressionCompletion559", None)
                setattr(value, "alf_ClassificationExpressionCompletion559", self)

    @property
    def alf_RelationalExpressionCompletion(self):
        return self.__alf_RelationalExpressionCompletion

    @alf_RelationalExpressionCompletion.setter
    def alf_RelationalExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpressionCompletion__alf_RelationalExpressionCompletion", None)
        self.__alf_RelationalExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpression547"):
                opp_val = getattr(old_value, "alf_RelationalExpression547", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression547", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression547"):
                opp_val = getattr(value, "alf_RelationalExpression547", None)
                setattr(value, "alf_RelationalExpression547", self)

class alf_RelationalExpression:

    pass
class alf_ShiftExpression:

    pass
class alf_AdditiveExpressionCompletion:

    def __init__(self, operator: str, alf_AdditiveExpressionCompletion: "alf_AdditiveExpression" = None, alf_AdditiveExpressionCompletion529: "alf_MultiplicativeExpressionCompletion" = None, alf_AdditiveExpressionCompletion532: set["alf_MultiplicativeExpression"] = None, alf_AdditiveExpressionCompletion540: "alf_ShiftExpressionCompletion" = None):
        self.operator = operator
        self.alf_AdditiveExpressionCompletion = alf_AdditiveExpressionCompletion
        self.alf_AdditiveExpressionCompletion529 = alf_AdditiveExpressionCompletion529
        self.alf_AdditiveExpressionCompletion532 = alf_AdditiveExpressionCompletion532 if alf_AdditiveExpressionCompletion532 is not None else set()
        self.alf_AdditiveExpressionCompletion540 = alf_AdditiveExpressionCompletion540
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_AdditiveExpressionCompletion(self):
        return self.__alf_AdditiveExpressionCompletion

    @alf_AdditiveExpressionCompletion.setter
    def alf_AdditiveExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpressionCompletion__alf_AdditiveExpressionCompletion", None)
        self.__alf_AdditiveExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AdditiveExpression527"):
                opp_val = getattr(old_value, "alf_AdditiveExpression527", None)
                if opp_val == self:
                    setattr(old_value, "alf_AdditiveExpression527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AdditiveExpression527"):
                opp_val = getattr(value, "alf_AdditiveExpression527", None)
                setattr(value, "alf_AdditiveExpression527", self)

    @property
    def alf_AdditiveExpressionCompletion540(self):
        return self.__alf_AdditiveExpressionCompletion540

    @alf_AdditiveExpressionCompletion540.setter
    def alf_AdditiveExpressionCompletion540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpressionCompletion__alf_AdditiveExpressionCompletion540", None)
        self.__alf_AdditiveExpressionCompletion540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpressionCompletion539"):
                opp_val = getattr(old_value, "alf_ShiftExpressionCompletion539", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpressionCompletion539", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpressionCompletion539"):
                opp_val = getattr(value, "alf_ShiftExpressionCompletion539", None)
                setattr(value, "alf_ShiftExpressionCompletion539", self)

    @property
    def alf_AdditiveExpressionCompletion532(self):
        return self.__alf_AdditiveExpressionCompletion532

    @alf_AdditiveExpressionCompletion532.setter
    def alf_AdditiveExpressionCompletion532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpressionCompletion__alf_AdditiveExpressionCompletion532", None)
        self.__alf_AdditiveExpressionCompletion532 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_MultiplicativeExpression533"):
                    opp_val = getattr(item, "alf_MultiplicativeExpression533", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_MultiplicativeExpression533", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_MultiplicativeExpression533"):
                    opp_val = getattr(item, "alf_MultiplicativeExpression533", None)
                    
                    setattr(item, "alf_MultiplicativeExpression533", self)
                    

    @property
    def alf_AdditiveExpressionCompletion529(self):
        return self.__alf_AdditiveExpressionCompletion529

    @alf_AdditiveExpressionCompletion529.setter
    def alf_AdditiveExpressionCompletion529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpressionCompletion__alf_AdditiveExpressionCompletion529", None)
        self.__alf_AdditiveExpressionCompletion529 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicativeExpressionCompletion530"):
                opp_val = getattr(old_value, "alf_MultiplicativeExpressionCompletion530", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicativeExpressionCompletion530", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicativeExpressionCompletion530"):
                opp_val = getattr(value, "alf_MultiplicativeExpressionCompletion530", None)
                setattr(value, "alf_MultiplicativeExpressionCompletion530", self)

class alf_AdditiveExpression:

    pass
class alf_MultiplicativeExpressionCompletion:

    def __init__(self, operator: str, alf_MultiplicativeExpressionCompletion: "alf_MultiplicativeExpression" = None, alf_MultiplicativeExpressionCompletion530: "alf_AdditiveExpressionCompletion" = None, alf_MultiplicativeExpressionCompletion522: set["alf_UnaryExpression"] = None):
        self.operator = operator
        self.alf_MultiplicativeExpressionCompletion = alf_MultiplicativeExpressionCompletion
        self.alf_MultiplicativeExpressionCompletion530 = alf_MultiplicativeExpressionCompletion530
        self.alf_MultiplicativeExpressionCompletion522 = alf_MultiplicativeExpressionCompletion522 if alf_MultiplicativeExpressionCompletion522 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_MultiplicativeExpressionCompletion(self):
        return self.__alf_MultiplicativeExpressionCompletion

    @alf_MultiplicativeExpressionCompletion.setter
    def alf_MultiplicativeExpressionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpressionCompletion__alf_MultiplicativeExpressionCompletion", None)
        self.__alf_MultiplicativeExpressionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicativeExpression520"):
                opp_val = getattr(old_value, "alf_MultiplicativeExpression520", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicativeExpression520", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicativeExpression520"):
                opp_val = getattr(value, "alf_MultiplicativeExpression520", None)
                setattr(value, "alf_MultiplicativeExpression520", self)

    @property
    def alf_MultiplicativeExpressionCompletion522(self):
        return self.__alf_MultiplicativeExpressionCompletion522

    @alf_MultiplicativeExpressionCompletion522.setter
    def alf_MultiplicativeExpressionCompletion522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpressionCompletion__alf_MultiplicativeExpressionCompletion522", None)
        self.__alf_MultiplicativeExpressionCompletion522 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_UnaryExpression523"):
                    opp_val = getattr(item, "alf_UnaryExpression523", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_UnaryExpression523", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_UnaryExpression523"):
                    opp_val = getattr(item, "alf_UnaryExpression523", None)
                    
                    setattr(item, "alf_UnaryExpression523", self)
                    

    @property
    def alf_MultiplicativeExpressionCompletion530(self):
        return self.__alf_MultiplicativeExpressionCompletion530

    @alf_MultiplicativeExpressionCompletion530.setter
    def alf_MultiplicativeExpressionCompletion530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpressionCompletion__alf_MultiplicativeExpressionCompletion530", None)
        self.__alf_MultiplicativeExpressionCompletion530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AdditiveExpressionCompletion529"):
                opp_val = getattr(old_value, "alf_AdditiveExpressionCompletion529", None)
                if opp_val == self:
                    setattr(old_value, "alf_AdditiveExpressionCompletion529", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AdditiveExpressionCompletion529"):
                opp_val = getattr(value, "alf_AdditiveExpressionCompletion529", None)
                setattr(value, "alf_AdditiveExpressionCompletion529", self)

class alf_MultiplicativeExpression:

    pass
class alf_CastCompletion:

    pass
class NonNameUnaryExpression:

    pass
class alf_PostfixOperation:

    def __init__(self, operator: str, alf_PostfixOperation: "alf_PostfixExpressionCompletion" = None):
        self.operator = operator
        self.alf_PostfixOperation = alf_PostfixOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_PostfixOperation(self):
        return self.__alf_PostfixOperation

    @alf_PostfixOperation.setter
    def alf_PostfixOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PostfixOperation__alf_PostfixOperation", None)
        self.__alf_PostfixOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PostfixExpressionCompletion479"):
                opp_val = getattr(old_value, "alf_PostfixExpressionCompletion479", None)
                if opp_val == self:
                    setattr(old_value, "alf_PostfixExpressionCompletion479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PostfixExpressionCompletion479"):
                opp_val = getattr(value, "alf_PostfixExpressionCompletion479", None)
                setattr(value, "alf_PostfixExpressionCompletion479", self)

class alf_NonNamePostfixOrCastExpression(NonNameUnaryExpression):

    def __init__(self, any: bool, alf_NonNamePostfixOrCastExpression: "alf_PostfixOrCastExpression" = None, alf_NonNamePostfixOrCastExpression490: "alf_CastCompletion" = None, alf_NonNamePostfixOrCastExpression492: "alf_QualifiedNameWithoutBinding" = None, alf_NonNamePostfixOrCastExpression495: "alf_PostfixExpressionCompletion" = None, alf_NonNamePostfixOrCastExpression498: "alf_NameToExpressionCompletion" = None, alf_NonNamePostfixOrCastExpression501: "alf_PostfixExpressionCompletion" = None, alf_NonNamePostfixOrCastExpression504: "alf_NonNameExpression" = None, alf_NonNamePostfixOrCastExpression507: "alf_BaseExpression" = None):
        self.any = any
        self.alf_NonNamePostfixOrCastExpression = alf_NonNamePostfixOrCastExpression
        self.alf_NonNamePostfixOrCastExpression490 = alf_NonNamePostfixOrCastExpression490
        self.alf_NonNamePostfixOrCastExpression492 = alf_NonNamePostfixOrCastExpression492
        self.alf_NonNamePostfixOrCastExpression495 = alf_NonNamePostfixOrCastExpression495
        self.alf_NonNamePostfixOrCastExpression498 = alf_NonNamePostfixOrCastExpression498
        self.alf_NonNamePostfixOrCastExpression501 = alf_NonNamePostfixOrCastExpression501
        self.alf_NonNamePostfixOrCastExpression504 = alf_NonNamePostfixOrCastExpression504
        self.alf_NonNamePostfixOrCastExpression507 = alf_NonNamePostfixOrCastExpression507
        
    @property
    def any(self) -> bool:
        return self.__any

    @any.setter
    def any(self, any: bool):
        self.__any = any

    @property
    def alf_NonNamePostfixOrCastExpression495(self):
        return self.__alf_NonNamePostfixOrCastExpression495

    @alf_NonNamePostfixOrCastExpression495.setter
    def alf_NonNamePostfixOrCastExpression495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression495", None)
        self.__alf_NonNamePostfixOrCastExpression495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PostfixExpressionCompletion496"):
                opp_val = getattr(old_value, "alf_PostfixExpressionCompletion496", None)
                if opp_val == self:
                    setattr(old_value, "alf_PostfixExpressionCompletion496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PostfixExpressionCompletion496"):
                opp_val = getattr(value, "alf_PostfixExpressionCompletion496", None)
                setattr(value, "alf_PostfixExpressionCompletion496", self)

    @property
    def alf_NonNamePostfixOrCastExpression490(self):
        return self.__alf_NonNamePostfixOrCastExpression490

    @alf_NonNamePostfixOrCastExpression490.setter
    def alf_NonNamePostfixOrCastExpression490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression490", None)
        self.__alf_NonNamePostfixOrCastExpression490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_CastCompletion"):
                opp_val = getattr(old_value, "alf_CastCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_CastCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_CastCompletion"):
                opp_val = getattr(value, "alf_CastCompletion", None)
                setattr(value, "alf_CastCompletion", self)

    @property
    def alf_NonNamePostfixOrCastExpression501(self):
        return self.__alf_NonNamePostfixOrCastExpression501

    @alf_NonNamePostfixOrCastExpression501.setter
    def alf_NonNamePostfixOrCastExpression501(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression501", None)
        self.__alf_NonNamePostfixOrCastExpression501 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PostfixExpressionCompletion502"):
                opp_val = getattr(old_value, "alf_PostfixExpressionCompletion502", None)
                if opp_val == self:
                    setattr(old_value, "alf_PostfixExpressionCompletion502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PostfixExpressionCompletion502"):
                opp_val = getattr(value, "alf_PostfixExpressionCompletion502", None)
                setattr(value, "alf_PostfixExpressionCompletion502", self)

    @property
    def alf_NonNamePostfixOrCastExpression507(self):
        return self.__alf_NonNamePostfixOrCastExpression507

    @alf_NonNamePostfixOrCastExpression507.setter
    def alf_NonNamePostfixOrCastExpression507(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression507", None)
        self.__alf_NonNamePostfixOrCastExpression507 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_BaseExpression508"):
                opp_val = getattr(old_value, "alf_BaseExpression508", None)
                if opp_val == self:
                    setattr(old_value, "alf_BaseExpression508", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_BaseExpression508"):
                opp_val = getattr(value, "alf_BaseExpression508", None)
                setattr(value, "alf_BaseExpression508", self)

    @property
    def alf_NonNamePostfixOrCastExpression504(self):
        return self.__alf_NonNamePostfixOrCastExpression504

    @alf_NonNamePostfixOrCastExpression504.setter
    def alf_NonNamePostfixOrCastExpression504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression504", None)
        self.__alf_NonNamePostfixOrCastExpression504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NonNameExpression505"):
                opp_val = getattr(old_value, "alf_NonNameExpression505", None)
                if opp_val == self:
                    setattr(old_value, "alf_NonNameExpression505", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NonNameExpression505"):
                opp_val = getattr(value, "alf_NonNameExpression505", None)
                setattr(value, "alf_NonNameExpression505", self)

    @property
    def alf_NonNamePostfixOrCastExpression(self):
        return self.__alf_NonNamePostfixOrCastExpression

    @alf_NonNamePostfixOrCastExpression.setter
    def alf_NonNamePostfixOrCastExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression", None)
        self.__alf_NonNamePostfixOrCastExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PostfixOrCastExpression"):
                opp_val = getattr(old_value, "alf_PostfixOrCastExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_PostfixOrCastExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PostfixOrCastExpression"):
                opp_val = getattr(value, "alf_PostfixOrCastExpression", None)
                setattr(value, "alf_PostfixOrCastExpression", self)

    @property
    def alf_NonNamePostfixOrCastExpression492(self):
        return self.__alf_NonNamePostfixOrCastExpression492

    @alf_NonNamePostfixOrCastExpression492.setter
    def alf_NonNamePostfixOrCastExpression492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression492", None)
        self.__alf_NonNamePostfixOrCastExpression492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithoutBinding493"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithoutBinding493", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithoutBinding493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithoutBinding493"):
                opp_val = getattr(value, "alf_QualifiedNameWithoutBinding493", None)
                setattr(value, "alf_QualifiedNameWithoutBinding493", self)

    @property
    def alf_NonNamePostfixOrCastExpression498(self):
        return self.__alf_NonNamePostfixOrCastExpression498

    @alf_NonNamePostfixOrCastExpression498.setter
    def alf_NonNamePostfixOrCastExpression498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NonNamePostfixOrCastExpression__alf_NonNamePostfixOrCastExpression498", None)
        self.__alf_NonNamePostfixOrCastExpression498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameToExpressionCompletion499"):
                opp_val = getattr(old_value, "alf_NameToExpressionCompletion499", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameToExpressionCompletion499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameToExpressionCompletion499"):
                opp_val = getattr(value, "alf_NameToExpressionCompletion499", None)
                setattr(value, "alf_NameToExpressionCompletion499", self)

class CastCompletion:

    pass
class UnaryExpression:

    pass
class alf_NonPostfixNonCastUnaryExpression(NonNameUnaryExpression, UnaryExpression):

    pass
class alf_PostfixOrCastExpression(CastCompletion, UnaryExpression):

    pass
class NonPostfixNonCastUnaryExpression:

    pass
class alf_BitStringComplementExpression(NonPostfixNonCastUnaryExpression, CastCompletion):

    pass
class alf_NumericUnaryExpression(NonPostfixNonCastUnaryExpression):

    def __init__(self, operator: str, alf_NumericUnaryExpression: "alf_UnaryExpression" = None):
        self.operator = operator
        self.alf_NumericUnaryExpression = alf_NumericUnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_NumericUnaryExpression(self):
        return self.__alf_NumericUnaryExpression

    @alf_NumericUnaryExpression.setter
    def alf_NumericUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NumericUnaryExpression__alf_NumericUnaryExpression", None)
        self.__alf_NumericUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_UnaryExpression514"):
                opp_val = getattr(old_value, "alf_UnaryExpression514", None)
                if opp_val == self:
                    setattr(old_value, "alf_UnaryExpression514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_UnaryExpression514"):
                opp_val = getattr(value, "alf_UnaryExpression514", None)
                setattr(value, "alf_UnaryExpression514", self)

class alf_IsolationExpression(NonPostfixNonCastUnaryExpression, CastCompletion):

    pass
class alf_BooleanNegationExpression(NonPostfixNonCastUnaryExpression, CastCompletion):

    pass
class alf_PrefixExpression(NonPostfixNonCastUnaryExpression):

    def __init__(self, operator: str, alf_PrefixExpression: "alf_PrimaryExpression" = None):
        self.operator = operator
        self.alf_PrefixExpression = alf_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def alf_PrefixExpression(self):
        return self.__alf_PrefixExpression

    @alf_PrefixExpression.setter
    def alf_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PrefixExpression__alf_PrefixExpression", None)
        self.__alf_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PrimaryExpression481"):
                opp_val = getattr(old_value, "alf_PrimaryExpression481", None)
                if opp_val == self:
                    setattr(old_value, "alf_PrimaryExpression481", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PrimaryExpression481"):
                opp_val = getattr(value, "alf_PrimaryExpression481", None)
                setattr(value, "alf_PrimaryExpression481", self)

class alf_EObject:

    pass
class alf_MultiplicityIndicator:

    pass
class alf_SequenceElement:

    pass
class alf_SequenceElementListCompletion:

    pass
class alf_SequenceElements:

    pass
class alf_IndexedNamedExpression:

    pass
class alf_IndexedNamedExpressionListCompletion:

    pass
class alf_LinkOperationTuple:

    pass
class alf_NamedExpression:

    pass
class alf_PositionalTupleExpressionListCompletion:

    pass
class alf_PositionalTupleExpressionList:

    pass
class alf_NamedTupleExpressionList:

    pass
class BaseExpression:

    pass
class alf_SuperInvocationExpression(BaseExpression):

    pass
class alf_SequenceAnyExpression(BaseExpression):

    pass
class alf_InstanceCreationOrSequenceConstructionExpression(BaseExpression):

    pass
class alf_LiteralExpression(BaseExpression):

    pass
class alf_Index:

    pass
class alf_SequenceOperationOrReductionOrExpansion:

    def __init__(self, isReduce: bool, isOrdered: bool, id: str, alf_SequenceOperationOrReductionOrExpansion: "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index" = None, alf_SequenceOperationOrReductionOrExpansion462: "alf_EObject" = None, alf_SequenceOperationOrReductionOrExpansion464: "alf_Tuple" = None, alf_SequenceOperationOrReductionOrExpansion467: "alf_TemplateBinding" = None, alf_SequenceOperationOrReductionOrExpansion470: "alf_Name" = None, alf_SequenceOperationOrReductionOrExpansion473: "alf_Expression" = None):
        self.isReduce = isReduce
        self.isOrdered = isOrdered
        self.id = id
        self.alf_SequenceOperationOrReductionOrExpansion = alf_SequenceOperationOrReductionOrExpansion
        self.alf_SequenceOperationOrReductionOrExpansion462 = alf_SequenceOperationOrReductionOrExpansion462
        self.alf_SequenceOperationOrReductionOrExpansion464 = alf_SequenceOperationOrReductionOrExpansion464
        self.alf_SequenceOperationOrReductionOrExpansion467 = alf_SequenceOperationOrReductionOrExpansion467
        self.alf_SequenceOperationOrReductionOrExpansion470 = alf_SequenceOperationOrReductionOrExpansion470
        self.alf_SequenceOperationOrReductionOrExpansion473 = alf_SequenceOperationOrReductionOrExpansion473
        
    @property
    def isReduce(self) -> bool:
        return self.__isReduce

    @isReduce.setter
    def isReduce(self, isReduce: bool):
        self.__isReduce = isReduce

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def alf_SequenceOperationOrReductionOrExpansion(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion

    @alf_SequenceOperationOrReductionOrExpansion.setter
    def alf_SequenceOperationOrReductionOrExpansion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion", None)
        self.__alf_SequenceOperationOrReductionOrExpansion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338"):
                opp_val = getattr(old_value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338", None)
                if opp_val == self:
                    setattr(old_value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338"):
                opp_val = getattr(value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338", None)
                setattr(value, "alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index338", self)

    @property
    def alf_SequenceOperationOrReductionOrExpansion464(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion464

    @alf_SequenceOperationOrReductionOrExpansion464.setter
    def alf_SequenceOperationOrReductionOrExpansion464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion464", None)
        self.__alf_SequenceOperationOrReductionOrExpansion464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Tuple465"):
                opp_val = getattr(old_value, "alf_Tuple465", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple465"):
                opp_val = getattr(value, "alf_Tuple465", None)
                setattr(value, "alf_Tuple465", self)

    @property
    def alf_SequenceOperationOrReductionOrExpansion473(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion473

    @alf_SequenceOperationOrReductionOrExpansion473.setter
    def alf_SequenceOperationOrReductionOrExpansion473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion473", None)
        self.__alf_SequenceOperationOrReductionOrExpansion473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression474"):
                opp_val = getattr(old_value, "alf_Expression474", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression474"):
                opp_val = getattr(value, "alf_Expression474", None)
                setattr(value, "alf_Expression474", self)

    @property
    def alf_SequenceOperationOrReductionOrExpansion467(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion467

    @alf_SequenceOperationOrReductionOrExpansion467.setter
    def alf_SequenceOperationOrReductionOrExpansion467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion467", None)
        self.__alf_SequenceOperationOrReductionOrExpansion467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateBinding468"):
                opp_val = getattr(old_value, "alf_TemplateBinding468", None)
                if opp_val == self:
                    setattr(old_value, "alf_TemplateBinding468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding468"):
                opp_val = getattr(value, "alf_TemplateBinding468", None)
                setattr(value, "alf_TemplateBinding468", self)

    @property
    def alf_SequenceOperationOrReductionOrExpansion462(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion462

    @alf_SequenceOperationOrReductionOrExpansion462.setter
    def alf_SequenceOperationOrReductionOrExpansion462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion462", None)
        self.__alf_SequenceOperationOrReductionOrExpansion462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EObject"):
                opp_val = getattr(old_value, "alf_EObject", None)
                if opp_val == self:
                    setattr(old_value, "alf_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EObject"):
                opp_val = getattr(value, "alf_EObject", None)
                setattr(value, "alf_EObject", self)

    @property
    def alf_SequenceOperationOrReductionOrExpansion470(self):
        return self.__alf_SequenceOperationOrReductionOrExpansion470

    @alf_SequenceOperationOrReductionOrExpansion470.setter
    def alf_SequenceOperationOrReductionOrExpansion470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationOrReductionOrExpansion__alf_SequenceOperationOrReductionOrExpansion470", None)
        self.__alf_SequenceOperationOrReductionOrExpansion470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name471"):
                opp_val = getattr(old_value, "alf_Name471", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name471"):
                opp_val = getattr(value, "alf_Name471", None)
                setattr(value, "alf_Name471", self)

class alf_FeatureInvocation:

    pass
class alf_Tuple:

    pass
class alf_ThisExpression(BaseExpression):

    pass
class alf_ClassExtentExpressionCompletion:

    pass
class alf_LinkOperationCompletion:

    def __init__(self, linkOperation: str, alf_LinkOperationCompletion: "alf_NameToPrimaryExpression" = None, alf_LinkOperationCompletion393: "alf_LinkOperationTuple" = None):
        self.linkOperation = linkOperation
        self.alf_LinkOperationCompletion = alf_LinkOperationCompletion
        self.alf_LinkOperationCompletion393 = alf_LinkOperationCompletion393
        
    @property
    def linkOperation(self) -> str:
        return self.__linkOperation

    @linkOperation.setter
    def linkOperation(self, linkOperation: str):
        self.__linkOperation = linkOperation

    @property
    def alf_LinkOperationCompletion(self):
        return self.__alf_LinkOperationCompletion

    @alf_LinkOperationCompletion.setter
    def alf_LinkOperationCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationCompletion__alf_LinkOperationCompletion", None)
        self.__alf_LinkOperationCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameToPrimaryExpression324"):
                opp_val = getattr(old_value, "alf_NameToPrimaryExpression324", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameToPrimaryExpression324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameToPrimaryExpression324"):
                opp_val = getattr(value, "alf_NameToPrimaryExpression324", None)
                setattr(value, "alf_NameToPrimaryExpression324", self)

    @property
    def alf_LinkOperationCompletion393(self):
        return self.__alf_LinkOperationCompletion393

    @alf_LinkOperationCompletion393.setter
    def alf_LinkOperationCompletion393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationCompletion__alf_LinkOperationCompletion393", None)
        self.__alf_LinkOperationCompletion393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LinkOperationTuple"):
                opp_val = getattr(old_value, "alf_LinkOperationTuple", None)
                if opp_val == self:
                    setattr(old_value, "alf_LinkOperationTuple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LinkOperationTuple"):
                opp_val = getattr(value, "alf_LinkOperationTuple", None)
                setattr(value, "alf_LinkOperationTuple", self)

class alf_PrimaryExpressionCompletion:

    pass
class alf_ParenthesizedExpression:

    pass
class alf_BaseExpression:

    pass
class alf_NameOrPrimaryExpression:

    pass
class alf_Feature:

    pass
class alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index:

    pass
class alf_BehaviorInvocation:

    pass
class alf_SequenceConstructionExpressionCompletion:

    pass
class alf_NameToPrimaryExpression:

    pass
class alf_NameToExpressionCompletion:

    pass
class alf_NonNameUnaryExpression:

    pass
class alf_NonNameExpression:

    pass
class alf_ExpressionCompletion:

    pass
class alf_UnaryExpression:

    pass
class alf_PrimaryExpression:

    pass
class alf_PostfixExpressionCompletion:

    pass
class alf_PrimaryToExpressionCompletion:

    pass
class TemplateBinding:

    pass
class alf_PositionalTemplateBinding(TemplateBinding):

    pass
class alf_ColonQualifiedNameCompletionWithoutBinding:

    pass
class alf_QualifiedNameWithoutBinding:

    pass
class InitializationExpression:

    pass
class alf_InstanceInitializationExpression(InitializationExpression):

    pass
class alf_SequenceInitializationExpression(InitializationExpression):

    def __init__(self, isNew: bool, alf_SequenceInitializationExpression: "alf_SequenceElements" = None, alf_SequenceInitializationExpression456: "alf_SequenceElements" = None, alf_SequenceInitializationExpression454: "alf_SequenceElement" = None):
        self.isNew = isNew
        self.alf_SequenceInitializationExpression = alf_SequenceInitializationExpression
        self.alf_SequenceInitializationExpression456 = alf_SequenceInitializationExpression456
        self.alf_SequenceInitializationExpression454 = alf_SequenceInitializationExpression454
        
    @property
    def isNew(self) -> bool:
        return self.__isNew

    @isNew.setter
    def isNew(self, isNew: bool):
        self.__isNew = isNew

    @property
    def alf_SequenceInitializationExpression454(self):
        return self.__alf_SequenceInitializationExpression454

    @alf_SequenceInitializationExpression454.setter
    def alf_SequenceInitializationExpression454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceInitializationExpression__alf_SequenceInitializationExpression454", None)
        self.__alf_SequenceInitializationExpression454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceElement453"):
                opp_val = getattr(old_value, "alf_SequenceElement453", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceElement453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceElement453"):
                opp_val = getattr(value, "alf_SequenceElement453", None)
                setattr(value, "alf_SequenceElement453", self)

    @property
    def alf_SequenceInitializationExpression(self):
        return self.__alf_SequenceInitializationExpression

    @alf_SequenceInitializationExpression.setter
    def alf_SequenceInitializationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceInitializationExpression__alf_SequenceInitializationExpression", None)
        self.__alf_SequenceInitializationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceElements446"):
                opp_val = getattr(old_value, "alf_SequenceElements446", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceElements446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceElements446"):
                opp_val = getattr(value, "alf_SequenceElements446", None)
                setattr(value, "alf_SequenceElements446", self)

    @property
    def alf_SequenceInitializationExpression456(self):
        return self.__alf_SequenceInitializationExpression456

    @alf_SequenceInitializationExpression456.setter
    def alf_SequenceInitializationExpression456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceInitializationExpression__alf_SequenceInitializationExpression456", None)
        self.__alf_SequenceInitializationExpression456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceElements457"):
                opp_val = getattr(old_value, "alf_SequenceElements457", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceElements457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceElements457"):
                opp_val = getattr(value, "alf_SequenceElements457", None)
                setattr(value, "alf_SequenceElements457", self)

class alf_Expression(InitializationExpression):

    pass
class alf_TemplateParameterSubstitution:

    pass
class alf_NamedTemplateBinding(TemplateBinding):

    pass
class alf_ColonQualifiedNameCompletion:

    pass
class alf_UnqualifiedName:

    pass
class alf_TemplateBinding:

    pass
class UnqualifiedName:

    pass
class alf_NameBinding(UnqualifiedName):

    pass
class alf_RedefinitionClause:

    pass
class OperationDefinitionOrStub:

    pass
class alf_OperationDeclaration(OperationDefinitionOrStub):

    def __init__(self, isAbstract: bool, alf_OperationDeclaration: "alf_Name" = None, alf_OperationDeclaration246: "alf_FormalParameters" = None, alf_OperationDeclaration249: "alf_TypePart" = None, alf_OperationDeclaration252: "alf_RedefinitionClause" = None, alf_OperationDeclaration254: "alf_Block" = None):
        self.isAbstract = isAbstract
        self.alf_OperationDeclaration = alf_OperationDeclaration
        self.alf_OperationDeclaration246 = alf_OperationDeclaration246
        self.alf_OperationDeclaration249 = alf_OperationDeclaration249
        self.alf_OperationDeclaration252 = alf_OperationDeclaration252
        self.alf_OperationDeclaration254 = alf_OperationDeclaration254
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_OperationDeclaration254(self):
        return self.__alf_OperationDeclaration254

    @alf_OperationDeclaration254.setter
    def alf_OperationDeclaration254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration254", None)
        self.__alf_OperationDeclaration254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Block255"):
                opp_val = getattr(old_value, "alf_Block255", None)
                if opp_val == self:
                    setattr(old_value, "alf_Block255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Block255"):
                opp_val = getattr(value, "alf_Block255", None)
                setattr(value, "alf_Block255", self)

    @property
    def alf_OperationDeclaration252(self):
        return self.__alf_OperationDeclaration252

    @alf_OperationDeclaration252.setter
    def alf_OperationDeclaration252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration252", None)
        self.__alf_OperationDeclaration252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RedefinitionClause"):
                opp_val = getattr(old_value, "alf_RedefinitionClause", None)
                if opp_val == self:
                    setattr(old_value, "alf_RedefinitionClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RedefinitionClause"):
                opp_val = getattr(value, "alf_RedefinitionClause", None)
                setattr(value, "alf_RedefinitionClause", self)

    @property
    def alf_OperationDeclaration(self):
        return self.__alf_OperationDeclaration

    @alf_OperationDeclaration.setter
    def alf_OperationDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration", None)
        self.__alf_OperationDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name244"):
                opp_val = getattr(old_value, "alf_Name244", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name244"):
                opp_val = getattr(value, "alf_Name244", None)
                setattr(value, "alf_Name244", self)

    @property
    def alf_OperationDeclaration246(self):
        return self.__alf_OperationDeclaration246

    @alf_OperationDeclaration246.setter
    def alf_OperationDeclaration246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration246", None)
        self.__alf_OperationDeclaration246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_FormalParameters247"):
                opp_val = getattr(old_value, "alf_FormalParameters247", None)
                if opp_val == self:
                    setattr(old_value, "alf_FormalParameters247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_FormalParameters247"):
                opp_val = getattr(value, "alf_FormalParameters247", None)
                setattr(value, "alf_FormalParameters247", self)

    @property
    def alf_OperationDeclaration249(self):
        return self.__alf_OperationDeclaration249

    @alf_OperationDeclaration249.setter
    def alf_OperationDeclaration249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration249", None)
        self.__alf_OperationDeclaration249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart250"):
                opp_val = getattr(old_value, "alf_TypePart250", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart250"):
                opp_val = getattr(value, "alf_TypePart250", None)
                setattr(value, "alf_TypePart250", self)

class alf_SignalReceptionDeclaration:

    pass
class ActiveFeatureDefinitionOrStub:

    pass
class alf_SignalReceptionDefinitionOrStub(ActiveFeatureDefinitionOrStub):

    pass
class alf_ReceptionDefinition(ActiveFeatureDefinitionOrStub):

    pass
class alf_MultiplicityRange:

    pass
class alf_Multiplicity:

    def __init__(self, isOrdered: bool, isNonUnique: bool, isSequence: bool, alf_Multiplicity235: "alf_MultiplicityRange" = None, alf_Multiplicity: "alf_TypePart" = None):
        self.isOrdered = isOrdered
        self.isNonUnique = isNonUnique
        self.isSequence = isSequence
        self.alf_Multiplicity235 = alf_Multiplicity235
        self.alf_Multiplicity = alf_Multiplicity
        
    @property
    def isNonUnique(self) -> bool:
        return self.__isNonUnique

    @isNonUnique.setter
    def isNonUnique(self, isNonUnique: bool):
        self.__isNonUnique = isNonUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def isSequence(self) -> bool:
        return self.__isSequence

    @isSequence.setter
    def isSequence(self, isSequence: bool):
        self.__isSequence = isSequence

    @property
    def alf_Multiplicity235(self):
        return self.__alf_Multiplicity235

    @alf_Multiplicity235.setter
    def alf_Multiplicity235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Multiplicity__alf_Multiplicity235", None)
        self.__alf_Multiplicity235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicityRange"):
                opp_val = getattr(old_value, "alf_MultiplicityRange", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicityRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicityRange"):
                opp_val = getattr(value, "alf_MultiplicityRange", None)
                setattr(value, "alf_MultiplicityRange", self)

    @property
    def alf_Multiplicity(self):
        return self.__alf_Multiplicity

    @alf_Multiplicity.setter
    def alf_Multiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Multiplicity__alf_Multiplicity", None)
        self.__alf_Multiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart230"):
                opp_val = getattr(old_value, "alf_TypePart230", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart230"):
                opp_val = getattr(value, "alf_TypePart230", None)
                setattr(value, "alf_TypePart230", self)

class alf_TypeName:

    def __init__(self, any: bool, alf_TypeName: "alf_TypePart" = None, alf_TypeName232: "alf_QualifiedName" = None, alf_TypeName675: "alf_LocalNameDeclarationStatement" = None):
        self.any = any
        self.alf_TypeName = alf_TypeName
        self.alf_TypeName232 = alf_TypeName232
        self.alf_TypeName675 = alf_TypeName675
        
    @property
    def any(self) -> bool:
        return self.__any

    @any.setter
    def any(self, any: bool):
        self.__any = any

    @property
    def alf_TypeName(self):
        return self.__alf_TypeName

    @alf_TypeName.setter
    def alf_TypeName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_TypeName__alf_TypeName", None)
        self.__alf_TypeName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart228"):
                opp_val = getattr(old_value, "alf_TypePart228", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart228"):
                opp_val = getattr(value, "alf_TypePart228", None)
                setattr(value, "alf_TypePart228", self)

    @property
    def alf_TypeName232(self):
        return self.__alf_TypeName232

    @alf_TypeName232.setter
    def alf_TypeName232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_TypeName__alf_TypeName232", None)
        self.__alf_TypeName232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedName233"):
                opp_val = getattr(old_value, "alf_QualifiedName233", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedName233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedName233"):
                opp_val = getattr(value, "alf_QualifiedName233", None)
                setattr(value, "alf_QualifiedName233", self)

    @property
    def alf_TypeName675(self):
        return self.__alf_TypeName675

    @alf_TypeName675.setter
    def alf_TypeName675(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_TypeName__alf_TypeName675", None)
        self.__alf_TypeName675 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LocalNameDeclarationStatement674"):
                opp_val = getattr(old_value, "alf_LocalNameDeclarationStatement674", None)
                if opp_val == self:
                    setattr(old_value, "alf_LocalNameDeclarationStatement674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LocalNameDeclarationStatement674"):
                opp_val = getattr(value, "alf_LocalNameDeclarationStatement674", None)
                setattr(value, "alf_LocalNameDeclarationStatement674", self)

class alf_UnlimitedNaturalLiteral:

    def __init__(self, star: bool, alf_UnlimitedNaturalLiteral: "alf_MultiplicityRange" = None, alf_UnlimitedNaturalLiteral241: "alf_INTEGER_LITERAL" = None):
        self.star = star
        self.alf_UnlimitedNaturalLiteral = alf_UnlimitedNaturalLiteral
        self.alf_UnlimitedNaturalLiteral241 = alf_UnlimitedNaturalLiteral241
        
    @property
    def star(self) -> bool:
        return self.__star

    @star.setter
    def star(self, star: bool):
        self.__star = star

    @property
    def alf_UnlimitedNaturalLiteral(self):
        return self.__alf_UnlimitedNaturalLiteral

    @alf_UnlimitedNaturalLiteral.setter
    def alf_UnlimitedNaturalLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnlimitedNaturalLiteral__alf_UnlimitedNaturalLiteral", None)
        self.__alf_UnlimitedNaturalLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicityRange239"):
                opp_val = getattr(old_value, "alf_MultiplicityRange239", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicityRange239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicityRange239"):
                opp_val = getattr(value, "alf_MultiplicityRange239", None)
                setattr(value, "alf_MultiplicityRange239", self)

    @property
    def alf_UnlimitedNaturalLiteral241(self):
        return self.__alf_UnlimitedNaturalLiteral241

    @alf_UnlimitedNaturalLiteral241.setter
    def alf_UnlimitedNaturalLiteral241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnlimitedNaturalLiteral__alf_UnlimitedNaturalLiteral241", None)
        self.__alf_UnlimitedNaturalLiteral241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_INTEGER_LITERAL242"):
                opp_val = getattr(old_value, "alf_INTEGER_LITERAL242", None)
                if opp_val == self:
                    setattr(old_value, "alf_INTEGER_LITERAL242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_INTEGER_LITERAL242"):
                opp_val = getattr(value, "alf_INTEGER_LITERAL242", None)
                setattr(value, "alf_INTEGER_LITERAL242", self)

class alf_PropertyDeclaration:

    def __init__(self, isComposite: bool, alf_PropertyDeclaration216: "alf_AttributeDefinition" = None, alf_PropertyDeclaration222: "alf_Name" = None, alf_PropertyDeclaration: "alf_PropertyDefinition" = None, alf_PropertyDeclaration225: "alf_TypePart" = None):
        self.isComposite = isComposite
        self.alf_PropertyDeclaration216 = alf_PropertyDeclaration216
        self.alf_PropertyDeclaration222 = alf_PropertyDeclaration222
        self.alf_PropertyDeclaration = alf_PropertyDeclaration
        self.alf_PropertyDeclaration225 = alf_PropertyDeclaration225
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def alf_PropertyDeclaration225(self):
        return self.__alf_PropertyDeclaration225

    @alf_PropertyDeclaration225.setter
    def alf_PropertyDeclaration225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyDeclaration__alf_PropertyDeclaration225", None)
        self.__alf_PropertyDeclaration225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart226"):
                opp_val = getattr(old_value, "alf_TypePart226", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart226"):
                opp_val = getattr(value, "alf_TypePart226", None)
                setattr(value, "alf_TypePart226", self)

    @property
    def alf_PropertyDeclaration216(self):
        return self.__alf_PropertyDeclaration216

    @alf_PropertyDeclaration216.setter
    def alf_PropertyDeclaration216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyDeclaration__alf_PropertyDeclaration216", None)
        self.__alf_PropertyDeclaration216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AttributeDefinition"):
                opp_val = getattr(old_value, "alf_AttributeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_AttributeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AttributeDefinition"):
                opp_val = getattr(value, "alf_AttributeDefinition", None)
                setattr(value, "alf_AttributeDefinition", self)

    @property
    def alf_PropertyDeclaration(self):
        return self.__alf_PropertyDeclaration

    @alf_PropertyDeclaration.setter
    def alf_PropertyDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyDeclaration__alf_PropertyDeclaration", None)
        self.__alf_PropertyDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PropertyDefinition214"):
                opp_val = getattr(old_value, "alf_PropertyDefinition214", None)
                if opp_val == self:
                    setattr(old_value, "alf_PropertyDefinition214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PropertyDefinition214"):
                opp_val = getattr(value, "alf_PropertyDefinition214", None)
                setattr(value, "alf_PropertyDefinition214", self)

    @property
    def alf_PropertyDeclaration222(self):
        return self.__alf_PropertyDeclaration222

    @alf_PropertyDeclaration222.setter
    def alf_PropertyDeclaration222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyDeclaration__alf_PropertyDeclaration222", None)
        self.__alf_PropertyDeclaration222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name223"):
                opp_val = getattr(old_value, "alf_Name223", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name223"):
                opp_val = getattr(value, "alf_Name223", None)
                setattr(value, "alf_Name223", self)

class alf_InitializationExpression:

    pass
class alf_AttributeInitializer:

    pass
class FeatureDefinitionOrStub:

    pass
class alf_OperationDefinitionOrStub(FeatureDefinitionOrStub):

    pass
class alf_AttributeDefinition(FeatureDefinitionOrStub):

    pass
class alf_TypePart:

    pass
class alf_FormalParameter:

    def __init__(self, comment: str, parameterDirection: str, alf_FormalParameter: "alf_FormalParameterList" = None, alf_FormalParameter205: "alf_StereotypeAnnotations" = None, alf_FormalParameter208: "alf_Name" = None, alf_FormalParameter211: "alf_TypePart" = None):
        self.comment = comment
        self.parameterDirection = parameterDirection
        self.alf_FormalParameter = alf_FormalParameter
        self.alf_FormalParameter205 = alf_FormalParameter205
        self.alf_FormalParameter208 = alf_FormalParameter208
        self.alf_FormalParameter211 = alf_FormalParameter211
        
    @property
    def parameterDirection(self) -> str:
        return self.__parameterDirection

    @parameterDirection.setter
    def parameterDirection(self, parameterDirection: str):
        self.__parameterDirection = parameterDirection

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_FormalParameter211(self):
        return self.__alf_FormalParameter211

    @alf_FormalParameter211.setter
    def alf_FormalParameter211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_FormalParameter__alf_FormalParameter211", None)
        self.__alf_FormalParameter211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart212"):
                opp_val = getattr(old_value, "alf_TypePart212", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart212"):
                opp_val = getattr(value, "alf_TypePart212", None)
                setattr(value, "alf_TypePart212", self)

    @property
    def alf_FormalParameter208(self):
        return self.__alf_FormalParameter208

    @alf_FormalParameter208.setter
    def alf_FormalParameter208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_FormalParameter__alf_FormalParameter208", None)
        self.__alf_FormalParameter208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name209"):
                opp_val = getattr(old_value, "alf_Name209", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name209"):
                opp_val = getattr(value, "alf_Name209", None)
                setattr(value, "alf_Name209", self)

    @property
    def alf_FormalParameter205(self):
        return self.__alf_FormalParameter205

    @alf_FormalParameter205.setter
    def alf_FormalParameter205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_FormalParameter__alf_FormalParameter205", None)
        self.__alf_FormalParameter205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations206"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations206", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations206"):
                opp_val = getattr(value, "alf_StereotypeAnnotations206", None)
                setattr(value, "alf_StereotypeAnnotations206", self)

    @property
    def alf_FormalParameter(self):
        return self.__alf_FormalParameter

    @alf_FormalParameter.setter
    def alf_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_FormalParameter__alf_FormalParameter", None)
        self.__alf_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_FormalParameterList203"):
                opp_val = getattr(old_value, "alf_FormalParameterList203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_FormalParameterList203"):
                opp_val = getattr(value, "alf_FormalParameterList203", None)
                if opp_val is None:
                    setattr(value, "alf_FormalParameterList203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_FormalParameterList:

    pass
class alf_FormalParameters:

    pass
class alf_ActivityDeclaration:

    pass
class alf_EnumerationBody:

    pass
class alf_EnumerationDeclaration:

    pass
class alf_SignalDeclaration:

    def __init__(self, isAbstract: bool, alf_SignalDeclaration177: "alf_SignalDefinitionOrStub" = None, alf_SignalDeclaration: "alf_ClassifierSignature" = None, alf_SignalDeclaration172: "alf_SignalDefinition" = None):
        self.isAbstract = isAbstract
        self.alf_SignalDeclaration177 = alf_SignalDeclaration177
        self.alf_SignalDeclaration = alf_SignalDeclaration
        self.alf_SignalDeclaration172 = alf_SignalDeclaration172
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_SignalDeclaration172(self):
        return self.__alf_SignalDeclaration172

    @alf_SignalDeclaration172.setter
    def alf_SignalDeclaration172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SignalDeclaration__alf_SignalDeclaration172", None)
        self.__alf_SignalDeclaration172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SignalDefinition"):
                opp_val = getattr(old_value, "alf_SignalDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_SignalDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SignalDefinition"):
                opp_val = getattr(value, "alf_SignalDefinition", None)
                setattr(value, "alf_SignalDefinition", self)

    @property
    def alf_SignalDeclaration(self):
        return self.__alf_SignalDeclaration

    @alf_SignalDeclaration.setter
    def alf_SignalDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SignalDeclaration__alf_SignalDeclaration", None)
        self.__alf_SignalDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature170"):
                opp_val = getattr(old_value, "alf_ClassifierSignature170", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature170"):
                opp_val = getattr(value, "alf_ClassifierSignature170", None)
                setattr(value, "alf_ClassifierSignature170", self)

    @property
    def alf_SignalDeclaration177(self):
        return self.__alf_SignalDeclaration177

    @alf_SignalDeclaration177.setter
    def alf_SignalDeclaration177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SignalDeclaration__alf_SignalDeclaration177", None)
        self.__alf_SignalDeclaration177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SignalDefinitionOrStub"):
                opp_val = getattr(old_value, "alf_SignalDefinitionOrStub", None)
                if opp_val == self:
                    setattr(old_value, "alf_SignalDefinitionOrStub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SignalDefinitionOrStub"):
                opp_val = getattr(value, "alf_SignalDefinitionOrStub", None)
                setattr(value, "alf_SignalDefinitionOrStub", self)

class alf_EnumerationLiteralName:

    def __init__(self, comment: str, alf_EnumerationLiteralName: "alf_EnumerationBody" = None, alf_EnumerationLiteralName167: "alf_Name" = None):
        self.comment = comment
        self.alf_EnumerationLiteralName = alf_EnumerationLiteralName
        self.alf_EnumerationLiteralName167 = alf_EnumerationLiteralName167
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_EnumerationLiteralName167(self):
        return self.__alf_EnumerationLiteralName167

    @alf_EnumerationLiteralName167.setter
    def alf_EnumerationLiteralName167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EnumerationLiteralName__alf_EnumerationLiteralName167", None)
        self.__alf_EnumerationLiteralName167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name168"):
                opp_val = getattr(old_value, "alf_Name168", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name168"):
                opp_val = getattr(value, "alf_Name168", None)
                setattr(value, "alf_Name168", self)

    @property
    def alf_EnumerationLiteralName(self):
        return self.__alf_EnumerationLiteralName

    @alf_EnumerationLiteralName.setter
    def alf_EnumerationLiteralName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EnumerationLiteralName__alf_EnumerationLiteralName", None)
        self.__alf_EnumerationLiteralName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EnumerationBody165"):
                opp_val = getattr(old_value, "alf_EnumerationBody165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EnumerationBody165"):
                opp_val = getattr(value, "alf_EnumerationBody165", None)
                if opp_val is None:
                    setattr(value, "alf_EnumerationBody165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_PropertyDefinition:

    pass
class alf_StructuredMember:

    def __init__(self, comment: str, isPublic: bool, alf_StructuredMember: "alf_StructuredBody" = None, alf_StructuredMember134: "alf_StereotypeAnnotations" = None, alf_StructuredMember137: "alf_PropertyDefinition" = None):
        self.comment = comment
        self.isPublic = isPublic
        self.alf_StructuredMember = alf_StructuredMember
        self.alf_StructuredMember134 = alf_StructuredMember134
        self.alf_StructuredMember137 = alf_StructuredMember137
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def isPublic(self) -> bool:
        return self.__isPublic

    @isPublic.setter
    def isPublic(self, isPublic: bool):
        self.__isPublic = isPublic

    @property
    def alf_StructuredMember137(self):
        return self.__alf_StructuredMember137

    @alf_StructuredMember137.setter
    def alf_StructuredMember137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_StructuredMember__alf_StructuredMember137", None)
        self.__alf_StructuredMember137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PropertyDefinition"):
                opp_val = getattr(old_value, "alf_PropertyDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_PropertyDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PropertyDefinition"):
                opp_val = getattr(value, "alf_PropertyDefinition", None)
                setattr(value, "alf_PropertyDefinition", self)

    @property
    def alf_StructuredMember(self):
        return self.__alf_StructuredMember

    @alf_StructuredMember.setter
    def alf_StructuredMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_StructuredMember__alf_StructuredMember", None)
        self.__alf_StructuredMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StructuredBody132"):
                opp_val = getattr(old_value, "alf_StructuredBody132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StructuredBody132"):
                opp_val = getattr(value, "alf_StructuredBody132", None)
                if opp_val is None:
                    setattr(value, "alf_StructuredBody132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_StructuredMember134(self):
        return self.__alf_StructuredMember134

    @alf_StructuredMember134.setter
    def alf_StructuredMember134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_StructuredMember__alf_StructuredMember134", None)
        self.__alf_StructuredMember134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations135"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations135", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations135"):
                opp_val = getattr(value, "alf_StereotypeAnnotations135", None)
                setattr(value, "alf_StereotypeAnnotations135", self)

class alf_AssociationDeclaration:

    def __init__(self, isAbstract: bool, alf_AssociationDeclaration: "alf_ClassifierSignature" = None, alf_AssociationDeclaration141: "alf_AssociationDefinition" = None, alf_AssociationDeclaration146: "alf_AssociationDefinitionOrStub" = None):
        self.isAbstract = isAbstract
        self.alf_AssociationDeclaration = alf_AssociationDeclaration
        self.alf_AssociationDeclaration141 = alf_AssociationDeclaration141
        self.alf_AssociationDeclaration146 = alf_AssociationDeclaration146
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_AssociationDeclaration141(self):
        return self.__alf_AssociationDeclaration141

    @alf_AssociationDeclaration141.setter
    def alf_AssociationDeclaration141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssociationDeclaration__alf_AssociationDeclaration141", None)
        self.__alf_AssociationDeclaration141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AssociationDefinition"):
                opp_val = getattr(old_value, "alf_AssociationDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_AssociationDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AssociationDefinition"):
                opp_val = getattr(value, "alf_AssociationDefinition", None)
                setattr(value, "alf_AssociationDefinition", self)

    @property
    def alf_AssociationDeclaration146(self):
        return self.__alf_AssociationDeclaration146

    @alf_AssociationDeclaration146.setter
    def alf_AssociationDeclaration146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssociationDeclaration__alf_AssociationDeclaration146", None)
        self.__alf_AssociationDeclaration146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AssociationDefinitionOrStub"):
                opp_val = getattr(old_value, "alf_AssociationDefinitionOrStub", None)
                if opp_val == self:
                    setattr(old_value, "alf_AssociationDefinitionOrStub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AssociationDefinitionOrStub"):
                opp_val = getattr(value, "alf_AssociationDefinitionOrStub", None)
                setattr(value, "alf_AssociationDefinitionOrStub", self)

    @property
    def alf_AssociationDeclaration(self):
        return self.__alf_AssociationDeclaration

    @alf_AssociationDeclaration.setter
    def alf_AssociationDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssociationDeclaration__alf_AssociationDeclaration", None)
        self.__alf_AssociationDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature139"):
                opp_val = getattr(old_value, "alf_ClassifierSignature139", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature139"):
                opp_val = getattr(value, "alf_ClassifierSignature139", None)
                setattr(value, "alf_ClassifierSignature139", self)

class alf_DataTypeDeclaration:

    def __init__(self, isAbstract: bool, alf_DataTypeDeclaration: "alf_ClassifierSignature" = None, alf_DataTypeDeclaration123: "alf_DataTypeDefinition" = None, alf_DataTypeDeclaration127: "alf_DataTypeDefinitionOrStub" = None):
        self.isAbstract = isAbstract
        self.alf_DataTypeDeclaration = alf_DataTypeDeclaration
        self.alf_DataTypeDeclaration123 = alf_DataTypeDeclaration123
        self.alf_DataTypeDeclaration127 = alf_DataTypeDeclaration127
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_DataTypeDeclaration127(self):
        return self.__alf_DataTypeDeclaration127

    @alf_DataTypeDeclaration127.setter
    def alf_DataTypeDeclaration127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DataTypeDeclaration__alf_DataTypeDeclaration127", None)
        self.__alf_DataTypeDeclaration127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_DataTypeDefinitionOrStub"):
                opp_val = getattr(old_value, "alf_DataTypeDefinitionOrStub", None)
                if opp_val == self:
                    setattr(old_value, "alf_DataTypeDefinitionOrStub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_DataTypeDefinitionOrStub"):
                opp_val = getattr(value, "alf_DataTypeDefinitionOrStub", None)
                setattr(value, "alf_DataTypeDefinitionOrStub", self)

    @property
    def alf_DataTypeDeclaration(self):
        return self.__alf_DataTypeDeclaration

    @alf_DataTypeDeclaration.setter
    def alf_DataTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DataTypeDeclaration__alf_DataTypeDeclaration", None)
        self.__alf_DataTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature121"):
                opp_val = getattr(old_value, "alf_ClassifierSignature121", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature121"):
                opp_val = getattr(value, "alf_ClassifierSignature121", None)
                setattr(value, "alf_ClassifierSignature121", self)

    @property
    def alf_DataTypeDeclaration123(self):
        return self.__alf_DataTypeDeclaration123

    @alf_DataTypeDeclaration123.setter
    def alf_DataTypeDeclaration123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DataTypeDeclaration__alf_DataTypeDeclaration123", None)
        self.__alf_DataTypeDeclaration123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_DataTypeDefinition"):
                opp_val = getattr(old_value, "alf_DataTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_DataTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_DataTypeDefinition"):
                opp_val = getattr(value, "alf_DataTypeDefinition", None)
                setattr(value, "alf_DataTypeDefinition", self)

class alf_ActiveClassMemberDefinition:

    pass
class alf_StructuredBody:

    pass
class alf_ActiveClassBody:

    pass
class alf_ActiveClassDeclaration:

    def __init__(self, isAbstract: bool, alf_ActiveClassDeclaration99: "alf_ActiveClassDefinitionOrStub" = None, alf_ActiveClassDeclaration: "alf_ClassifierSignature" = None, alf_ActiveClassDeclaration95: "alf_ActiveClassDefinition" = None):
        self.isAbstract = isAbstract
        self.alf_ActiveClassDeclaration99 = alf_ActiveClassDeclaration99
        self.alf_ActiveClassDeclaration = alf_ActiveClassDeclaration
        self.alf_ActiveClassDeclaration95 = alf_ActiveClassDeclaration95
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_ActiveClassDeclaration95(self):
        return self.__alf_ActiveClassDeclaration95

    @alf_ActiveClassDeclaration95.setter
    def alf_ActiveClassDeclaration95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassDeclaration__alf_ActiveClassDeclaration95", None)
        self.__alf_ActiveClassDeclaration95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActiveClassDefinition"):
                opp_val = getattr(old_value, "alf_ActiveClassDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_ActiveClassDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActiveClassDefinition"):
                opp_val = getattr(value, "alf_ActiveClassDefinition", None)
                setattr(value, "alf_ActiveClassDefinition", self)

    @property
    def alf_ActiveClassDeclaration(self):
        return self.__alf_ActiveClassDeclaration

    @alf_ActiveClassDeclaration.setter
    def alf_ActiveClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassDeclaration__alf_ActiveClassDeclaration", None)
        self.__alf_ActiveClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature93"):
                opp_val = getattr(old_value, "alf_ClassifierSignature93", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature93"):
                opp_val = getattr(value, "alf_ClassifierSignature93", None)
                setattr(value, "alf_ClassifierSignature93", self)

    @property
    def alf_ActiveClassDeclaration99(self):
        return self.__alf_ActiveClassDeclaration99

    @alf_ActiveClassDeclaration99.setter
    def alf_ActiveClassDeclaration99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassDeclaration__alf_ActiveClassDeclaration99", None)
        self.__alf_ActiveClassDeclaration99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActiveClassDefinitionOrStub"):
                opp_val = getattr(old_value, "alf_ActiveClassDefinitionOrStub", None)
                if opp_val == self:
                    setattr(old_value, "alf_ActiveClassDefinitionOrStub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActiveClassDefinitionOrStub"):
                opp_val = getattr(value, "alf_ActiveClassDefinitionOrStub", None)
                setattr(value, "alf_ActiveClassDefinitionOrStub", self)

class alf_Block:

    pass
class alf_BehaviorClause:

    pass
class alf_ActiveClassMember:

    def __init__(self, comment: str, alf_ActiveClassMember: "alf_ActiveClassBody" = None, alf_ActiveClassMember113: "alf_StereotypeAnnotations" = None, alf_ActiveClassMember116: "alf_VisibilityIndicator" = None, alf_ActiveClassMember119: "alf_ActiveClassMemberDefinition" = None):
        self.comment = comment
        self.alf_ActiveClassMember = alf_ActiveClassMember
        self.alf_ActiveClassMember113 = alf_ActiveClassMember113
        self.alf_ActiveClassMember116 = alf_ActiveClassMember116
        self.alf_ActiveClassMember119 = alf_ActiveClassMember119
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_ActiveClassMember(self):
        return self.__alf_ActiveClassMember

    @alf_ActiveClassMember.setter
    def alf_ActiveClassMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassMember__alf_ActiveClassMember", None)
        self.__alf_ActiveClassMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActiveClassBody104"):
                opp_val = getattr(old_value, "alf_ActiveClassBody104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActiveClassBody104"):
                opp_val = getattr(value, "alf_ActiveClassBody104", None)
                if opp_val is None:
                    setattr(value, "alf_ActiveClassBody104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_ActiveClassMember113(self):
        return self.__alf_ActiveClassMember113

    @alf_ActiveClassMember113.setter
    def alf_ActiveClassMember113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassMember__alf_ActiveClassMember113", None)
        self.__alf_ActiveClassMember113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations114"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations114", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations114"):
                opp_val = getattr(value, "alf_StereotypeAnnotations114", None)
                setattr(value, "alf_StereotypeAnnotations114", self)

    @property
    def alf_ActiveClassMember116(self):
        return self.__alf_ActiveClassMember116

    @alf_ActiveClassMember116.setter
    def alf_ActiveClassMember116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassMember__alf_ActiveClassMember116", None)
        self.__alf_ActiveClassMember116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_VisibilityIndicator117"):
                opp_val = getattr(old_value, "alf_VisibilityIndicator117", None)
                if opp_val == self:
                    setattr(old_value, "alf_VisibilityIndicator117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_VisibilityIndicator117"):
                opp_val = getattr(value, "alf_VisibilityIndicator117", None)
                setattr(value, "alf_VisibilityIndicator117", self)

    @property
    def alf_ActiveClassMember119(self):
        return self.__alf_ActiveClassMember119

    @alf_ActiveClassMember119.setter
    def alf_ActiveClassMember119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ActiveClassMember__alf_ActiveClassMember119", None)
        self.__alf_ActiveClassMember119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActiveClassMemberDefinition"):
                opp_val = getattr(old_value, "alf_ActiveClassMemberDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_ActiveClassMemberDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActiveClassMemberDefinition"):
                opp_val = getattr(value, "alf_ActiveClassMemberDefinition", None)
                setattr(value, "alf_ActiveClassMemberDefinition", self)

class ClassifierDefinitionOrStub:

    pass
class alf_DataTypeDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_EnumerationDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_AssociationDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_ActivityDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_SignalDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_ActiveClassDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_ClassDefinitionOrStub(ClassifierDefinitionOrStub):

    pass
class alf_ClassBody:

    pass
class ClassifierDefinition:

    pass
class alf_EnumerationDefinition(ClassifierDefinition):

    pass
class alf_AssociationDefinition(ClassifierDefinition):

    pass
class alf_DataTypeDefinition(ClassifierDefinition):

    pass
class alf_SignalDefinition(ClassifierDefinition):

    pass
class alf_ActivityDefinition(ClassifierDefinition):

    pass
class alf_ActiveClassDefinition(ClassifierDefinition):

    pass
class alf_ClassDefinition(ClassifierDefinition):

    pass
class ActiveClassMemberDefinition:

    pass
class alf_ActiveFeatureDefinitionOrStub(ActiveClassMemberDefinition):

    pass
class alf_ClassDeclaration:

    def __init__(self, isAbstract: bool, alf_ClassDeclaration: "alf_ClassifierSignature" = None, alf_ClassDeclaration75: "alf_ClassDefinition" = None, alf_ClassDeclaration79: "alf_ClassDefinitionOrStub" = None):
        self.isAbstract = isAbstract
        self.alf_ClassDeclaration = alf_ClassDeclaration
        self.alf_ClassDeclaration75 = alf_ClassDeclaration75
        self.alf_ClassDeclaration79 = alf_ClassDeclaration79
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def alf_ClassDeclaration79(self):
        return self.__alf_ClassDeclaration79

    @alf_ClassDeclaration79.setter
    def alf_ClassDeclaration79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassDeclaration__alf_ClassDeclaration79", None)
        self.__alf_ClassDeclaration79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassDefinitionOrStub"):
                opp_val = getattr(old_value, "alf_ClassDefinitionOrStub", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassDefinitionOrStub", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassDefinitionOrStub"):
                opp_val = getattr(value, "alf_ClassDefinitionOrStub", None)
                setattr(value, "alf_ClassDefinitionOrStub", self)

    @property
    def alf_ClassDeclaration75(self):
        return self.__alf_ClassDeclaration75

    @alf_ClassDeclaration75.setter
    def alf_ClassDeclaration75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassDeclaration__alf_ClassDeclaration75", None)
        self.__alf_ClassDeclaration75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassDefinition"):
                opp_val = getattr(old_value, "alf_ClassDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassDefinition"):
                opp_val = getattr(value, "alf_ClassDefinition", None)
                setattr(value, "alf_ClassDefinition", self)

    @property
    def alf_ClassDeclaration(self):
        return self.__alf_ClassDeclaration

    @alf_ClassDeclaration.setter
    def alf_ClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassDeclaration__alf_ClassDeclaration", None)
        self.__alf_ClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature73"):
                opp_val = getattr(old_value, "alf_ClassifierSignature73", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature73"):
                opp_val = getattr(value, "alf_ClassifierSignature73", None)
                setattr(value, "alf_ClassifierSignature73", self)

class alf_ClassMemberDefinition(ActiveClassMemberDefinition):

    pass
class alf_ClassMember:

    def __init__(self, comment: str, alf_ClassMember: "alf_ClassBody" = None, alf_ClassMember86: "alf_StereotypeAnnotations" = None, alf_ClassMember89: "alf_VisibilityIndicator" = None, alf_ClassMember91: "alf_ClassMemberDefinition" = None):
        self.comment = comment
        self.alf_ClassMember = alf_ClassMember
        self.alf_ClassMember86 = alf_ClassMember86
        self.alf_ClassMember89 = alf_ClassMember89
        self.alf_ClassMember91 = alf_ClassMember91
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_ClassMember91(self):
        return self.__alf_ClassMember91

    @alf_ClassMember91.setter
    def alf_ClassMember91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassMember__alf_ClassMember91", None)
        self.__alf_ClassMember91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassMemberDefinition"):
                opp_val = getattr(old_value, "alf_ClassMemberDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassMemberDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassMemberDefinition"):
                opp_val = getattr(value, "alf_ClassMemberDefinition", None)
                setattr(value, "alf_ClassMemberDefinition", self)

    @property
    def alf_ClassMember86(self):
        return self.__alf_ClassMember86

    @alf_ClassMember86.setter
    def alf_ClassMember86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassMember__alf_ClassMember86", None)
        self.__alf_ClassMember86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations87"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations87", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations87"):
                opp_val = getattr(value, "alf_StereotypeAnnotations87", None)
                setattr(value, "alf_StereotypeAnnotations87", self)

    @property
    def alf_ClassMember(self):
        return self.__alf_ClassMember

    @alf_ClassMember.setter
    def alf_ClassMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassMember__alf_ClassMember", None)
        self.__alf_ClassMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassBody84"):
                opp_val = getattr(old_value, "alf_ClassBody84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassBody84"):
                opp_val = getattr(value, "alf_ClassBody84", None)
                if opp_val is None:
                    setattr(value, "alf_ClassBody84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_ClassMember89(self):
        return self.__alf_ClassMember89

    @alf_ClassMember89.setter
    def alf_ClassMember89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassMember__alf_ClassMember89", None)
        self.__alf_ClassMember89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_VisibilityIndicator"):
                opp_val = getattr(old_value, "alf_VisibilityIndicator", None)
                if opp_val == self:
                    setattr(old_value, "alf_VisibilityIndicator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_VisibilityIndicator"):
                opp_val = getattr(value, "alf_VisibilityIndicator", None)
                setattr(value, "alf_VisibilityIndicator", self)

class alf_SpecializationClause:

    pass
class alf_TemplateParameters:

    pass
class alf_ClassifierSignature:

    pass
class ClassMemberDefinition:

    pass
class alf_FeatureDefinitionOrStub(ClassMemberDefinition):

    pass
class alf_PackagedElementDefinition:

    pass
class PackagedElementDefinition:

    pass
class alf_ClassifierDefinitionOrStub(ClassMemberDefinition, PackagedElementDefinition):

    pass
class alf_PackageDefinitionOrStub(PackagedElementDefinition):

    pass
class alf_ClassifierTemplateParameter:

    def __init__(self, comment: str, alf_ClassifierTemplateParameter: "alf_TemplateParameters" = None, alf_ClassifierTemplateParameter65: "alf_Name" = None, alf_ClassifierTemplateParameter68: "alf_QualifiedName" = None):
        self.comment = comment
        self.alf_ClassifierTemplateParameter = alf_ClassifierTemplateParameter
        self.alf_ClassifierTemplateParameter65 = alf_ClassifierTemplateParameter65
        self.alf_ClassifierTemplateParameter68 = alf_ClassifierTemplateParameter68
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_ClassifierTemplateParameter(self):
        return self.__alf_ClassifierTemplateParameter

    @alf_ClassifierTemplateParameter.setter
    def alf_ClassifierTemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassifierTemplateParameter__alf_ClassifierTemplateParameter", None)
        self.__alf_ClassifierTemplateParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateParameters63"):
                opp_val = getattr(old_value, "alf_TemplateParameters63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateParameters63"):
                opp_val = getattr(value, "alf_TemplateParameters63", None)
                if opp_val is None:
                    setattr(value, "alf_TemplateParameters63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_ClassifierTemplateParameter68(self):
        return self.__alf_ClassifierTemplateParameter68

    @alf_ClassifierTemplateParameter68.setter
    def alf_ClassifierTemplateParameter68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassifierTemplateParameter__alf_ClassifierTemplateParameter68", None)
        self.__alf_ClassifierTemplateParameter68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedName69"):
                opp_val = getattr(old_value, "alf_QualifiedName69", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedName69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedName69"):
                opp_val = getattr(value, "alf_QualifiedName69", None)
                setattr(value, "alf_QualifiedName69", self)

    @property
    def alf_ClassifierTemplateParameter65(self):
        return self.__alf_ClassifierTemplateParameter65

    @alf_ClassifierTemplateParameter65.setter
    def alf_ClassifierTemplateParameter65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassifierTemplateParameter__alf_ClassifierTemplateParameter65", None)
        self.__alf_ClassifierTemplateParameter65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name66"):
                opp_val = getattr(old_value, "alf_Name66", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name66"):
                opp_val = getattr(value, "alf_Name66", None)
                setattr(value, "alf_Name66", self)

class alf_PackageBody:

    pass
class NamespaceDefinition:

    pass
class alf_ClassifierDefinition(NamespaceDefinition):

    pass
class alf_PackageDefinition(NamespaceDefinition):

    pass
class alf_PackageDeclaration:

    pass
class alf_PackagedElement:

    def __init__(self, comment: str, importVisibilityIndicator: str, alf_PackagedElement: "alf_PackageBody" = None, alf_PackagedElement52: "alf_StereotypeAnnotations" = None, alf_PackagedElement55: "alf_PackagedElementDefinition" = None):
        self.comment = comment
        self.importVisibilityIndicator = importVisibilityIndicator
        self.alf_PackagedElement = alf_PackagedElement
        self.alf_PackagedElement52 = alf_PackagedElement52
        self.alf_PackagedElement55 = alf_PackagedElement55
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def importVisibilityIndicator(self) -> str:
        return self.__importVisibilityIndicator

    @importVisibilityIndicator.setter
    def importVisibilityIndicator(self, importVisibilityIndicator: str):
        self.__importVisibilityIndicator = importVisibilityIndicator

    @property
    def alf_PackagedElement55(self):
        return self.__alf_PackagedElement55

    @alf_PackagedElement55.setter
    def alf_PackagedElement55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PackagedElement__alf_PackagedElement55", None)
        self.__alf_PackagedElement55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PackagedElementDefinition"):
                opp_val = getattr(old_value, "alf_PackagedElementDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_PackagedElementDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PackagedElementDefinition"):
                opp_val = getattr(value, "alf_PackagedElementDefinition", None)
                setattr(value, "alf_PackagedElementDefinition", self)

    @property
    def alf_PackagedElement52(self):
        return self.__alf_PackagedElement52

    @alf_PackagedElement52.setter
    def alf_PackagedElement52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PackagedElement__alf_PackagedElement52", None)
        self.__alf_PackagedElement52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations53"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations53", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations53"):
                opp_val = getattr(value, "alf_StereotypeAnnotations53", None)
                setattr(value, "alf_StereotypeAnnotations53", self)

    @property
    def alf_PackagedElement(self):
        return self.__alf_PackagedElement

    @alf_PackagedElement.setter
    def alf_PackagedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PackagedElement__alf_PackagedElement", None)
        self.__alf_PackagedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PackageBody50"):
                opp_val = getattr(old_value, "alf_PackageBody50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PackageBody50"):
                opp_val = getattr(value, "alf_PackageBody50", None)
                if opp_val is None:
                    setattr(value, "alf_PackageBody50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_AliasDefinition:

    pass
class alf_ImportReferenceQualifiedNameCompletion:

    pass
class alf_VisibilityIndicator:

    def __init__(self, PUBLIC: str, PRIVATE: str, PROTECTED: str, alf_VisibilityIndicator: "alf_ClassMember" = None, alf_VisibilityIndicator117: "alf_ActiveClassMember" = None):
        self.PUBLIC = PUBLIC
        self.PRIVATE = PRIVATE
        self.PROTECTED = PROTECTED
        self.alf_VisibilityIndicator = alf_VisibilityIndicator
        self.alf_VisibilityIndicator117 = alf_VisibilityIndicator117
        
    @property
    def PROTECTED(self) -> str:
        return self.__PROTECTED

    @PROTECTED.setter
    def PROTECTED(self, PROTECTED: str):
        self.__PROTECTED = PROTECTED

    @property
    def PUBLIC(self) -> str:
        return self.__PUBLIC

    @PUBLIC.setter
    def PUBLIC(self, PUBLIC: str):
        self.__PUBLIC = PUBLIC

    @property
    def PRIVATE(self) -> str:
        return self.__PRIVATE

    @PRIVATE.setter
    def PRIVATE(self, PRIVATE: str):
        self.__PRIVATE = PRIVATE

    @property
    def alf_VisibilityIndicator117(self):
        return self.__alf_VisibilityIndicator117

    @alf_VisibilityIndicator117.setter
    def alf_VisibilityIndicator117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_VisibilityIndicator__alf_VisibilityIndicator117", None)
        self.__alf_VisibilityIndicator117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActiveClassMember116"):
                opp_val = getattr(old_value, "alf_ActiveClassMember116", None)
                if opp_val == self:
                    setattr(old_value, "alf_ActiveClassMember116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActiveClassMember116"):
                opp_val = getattr(value, "alf_ActiveClassMember116", None)
                setattr(value, "alf_ActiveClassMember116", self)

    @property
    def alf_VisibilityIndicator(self):
        return self.__alf_VisibilityIndicator

    @alf_VisibilityIndicator.setter
    def alf_VisibilityIndicator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_VisibilityIndicator__alf_VisibilityIndicator", None)
        self.__alf_VisibilityIndicator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassMember89"):
                opp_val = getattr(old_value, "alf_ClassMember89", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassMember89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassMember89"):
                opp_val = getattr(value, "alf_ClassMember89", None)
                setattr(value, "alf_ClassMember89", self)

class ImportReferenceQualifiedNameCompletion:

    pass
class alf_ColonQualifiedNameCompletionOfImportReference(ImportReferenceQualifiedNameCompletion):

    def __init__(self, star: bool, alf_ColonQualifiedNameCompletionOfImportReference: set["alf_Name"] = None, alf_ColonQualifiedNameCompletionOfImportReference33: "alf_AliasDefinition" = None):
        self.star = star
        self.alf_ColonQualifiedNameCompletionOfImportReference = alf_ColonQualifiedNameCompletionOfImportReference if alf_ColonQualifiedNameCompletionOfImportReference is not None else set()
        self.alf_ColonQualifiedNameCompletionOfImportReference33 = alf_ColonQualifiedNameCompletionOfImportReference33
        
    @property
    def star(self) -> bool:
        return self.__star

    @star.setter
    def star(self, star: bool):
        self.__star = star

    @property
    def alf_ColonQualifiedNameCompletionOfImportReference(self):
        return self.__alf_ColonQualifiedNameCompletionOfImportReference

    @alf_ColonQualifiedNameCompletionOfImportReference.setter
    def alf_ColonQualifiedNameCompletionOfImportReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ColonQualifiedNameCompletionOfImportReference__alf_ColonQualifiedNameCompletionOfImportReference", None)
        self.__alf_ColonQualifiedNameCompletionOfImportReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_Name31"):
                    opp_val = getattr(item, "alf_Name31", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_Name31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_Name31"):
                    opp_val = getattr(item, "alf_Name31", None)
                    
                    setattr(item, "alf_Name31", self)
                    

    @property
    def alf_ColonQualifiedNameCompletionOfImportReference33(self):
        return self.__alf_ColonQualifiedNameCompletionOfImportReference33

    @alf_ColonQualifiedNameCompletionOfImportReference33.setter
    def alf_ColonQualifiedNameCompletionOfImportReference33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ColonQualifiedNameCompletionOfImportReference__alf_ColonQualifiedNameCompletionOfImportReference33", None)
        self.__alf_ColonQualifiedNameCompletionOfImportReference33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AliasDefinition34"):
                opp_val = getattr(old_value, "alf_AliasDefinition34", None)
                if opp_val == self:
                    setattr(old_value, "alf_AliasDefinition34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AliasDefinition34"):
                opp_val = getattr(value, "alf_AliasDefinition34", None)
                setattr(value, "alf_AliasDefinition34", self)

class alf_TaggedValue:

    pass
class TaggedValues:

    pass
class alf_QualifiedNameList(TaggedValues):

    pass
class alf_TaggedValueList(TaggedValues):

    pass
class alf_TaggedValues:

    pass
class alf_QualifiedName:

    pass
class alf_ImportReference:

    def __init__(self, star: bool, alf_ImportReference: "alf_ImportDeclaration" = None, alf_ImportReference24: "alf_Name" = None, alf_ImportReference27: "alf_ImportReferenceQualifiedNameCompletion" = None, alf_ImportReference29: "alf_AliasDefinition" = None):
        self.star = star
        self.alf_ImportReference = alf_ImportReference
        self.alf_ImportReference24 = alf_ImportReference24
        self.alf_ImportReference27 = alf_ImportReference27
        self.alf_ImportReference29 = alf_ImportReference29
        
    @property
    def star(self) -> bool:
        return self.__star

    @star.setter
    def star(self, star: bool):
        self.__star = star

    @property
    def alf_ImportReference29(self):
        return self.__alf_ImportReference29

    @alf_ImportReference29.setter
    def alf_ImportReference29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportReference__alf_ImportReference29", None)
        self.__alf_ImportReference29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AliasDefinition"):
                opp_val = getattr(old_value, "alf_AliasDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_AliasDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AliasDefinition"):
                opp_val = getattr(value, "alf_AliasDefinition", None)
                setattr(value, "alf_AliasDefinition", self)

    @property
    def alf_ImportReference24(self):
        return self.__alf_ImportReference24

    @alf_ImportReference24.setter
    def alf_ImportReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportReference__alf_ImportReference24", None)
        self.__alf_ImportReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Name25"):
                opp_val = getattr(old_value, "alf_Name25", None)
                if opp_val == self:
                    setattr(old_value, "alf_Name25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Name25"):
                opp_val = getattr(value, "alf_Name25", None)
                setattr(value, "alf_Name25", self)

    @property
    def alf_ImportReference(self):
        return self.__alf_ImportReference

    @alf_ImportReference.setter
    def alf_ImportReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportReference__alf_ImportReference", None)
        self.__alf_ImportReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ImportDeclaration22"):
                opp_val = getattr(old_value, "alf_ImportDeclaration22", None)
                if opp_val == self:
                    setattr(old_value, "alf_ImportDeclaration22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ImportDeclaration22"):
                opp_val = getattr(value, "alf_ImportDeclaration22", None)
                setattr(value, "alf_ImportDeclaration22", self)

    @property
    def alf_ImportReference27(self):
        return self.__alf_ImportReference27

    @alf_ImportReference27.setter
    def alf_ImportReference27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportReference__alf_ImportReference27", None)
        self.__alf_ImportReference27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ImportReferenceQualifiedNameCompletion"):
                opp_val = getattr(old_value, "alf_ImportReferenceQualifiedNameCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_ImportReferenceQualifiedNameCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ImportReferenceQualifiedNameCompletion"):
                opp_val = getattr(value, "alf_ImportReferenceQualifiedNameCompletion", None)
                setattr(value, "alf_ImportReferenceQualifiedNameCompletion", self)

class alf_Name:

    def __init__(self, id: str, alf_Name: "alf_TaggedValue" = None, alf_Name31: "alf_ColonQualifiedNameCompletionOfImportReference" = None, alf_Name37: "alf_AliasDefinition" = None, alf_Name25: "alf_ImportReference" = None, alf_Name39: "alf_PackageDeclaration" = None, alf_Name66: "alf_ClassifierTemplateParameter" = None, alf_Name57: "alf_ClassifierSignature" = None, alf_Name111: "alf_BehaviorClause" = None, alf_Name168: "alf_EnumerationLiteralName" = None, alf_Name151: "alf_EnumerationDeclaration" = None, alf_Name182: "alf_ActivityDeclaration" = None, alf_Name223: "alf_PropertyDeclaration" = None, alf_Name209: "alf_FormalParameter" = None, alf_Name262: "alf_SignalReceptionDeclaration" = None, alf_Name244: "alf_OperationDeclaration" = None, alf_Name279: "alf_NameBinding" = None, alf_Name294: "alf_TemplateParameterSubstitution" = None, alf_Name283: "alf_QualifiedNameWithoutBinding" = None, alf_Name288: "alf_ColonQualifiedNameCompletionWithoutBinding" = None, alf_Name355: "alf_Feature" = None, alf_Name369: "alf_NamedExpression" = None, alf_Name396: "alf_LinkOperationTuple" = None, alf_Name424: "alf_IndexedNamedExpression" = None, alf_Name471: "alf_SequenceOperationOrReductionOrExpansion" = None, alf_Name650: "alf_NameList" = None, alf_Name652: "alf_InLineStatement" = None, alf_Name662: "alf_LocalNameDeclarationOrExpressionStatement" = None, alf_Name672: "alf_LocalNameDeclarationStatement" = None, alf_Name740: "alf_LoopVariableDefinition" = None, alf_Name773: "alf_AcceptClause" = None):
        self.id = id
        self.alf_Name = alf_Name
        self.alf_Name31 = alf_Name31
        self.alf_Name37 = alf_Name37
        self.alf_Name25 = alf_Name25
        self.alf_Name39 = alf_Name39
        self.alf_Name66 = alf_Name66
        self.alf_Name57 = alf_Name57
        self.alf_Name111 = alf_Name111
        self.alf_Name168 = alf_Name168
        self.alf_Name151 = alf_Name151
        self.alf_Name182 = alf_Name182
        self.alf_Name223 = alf_Name223
        self.alf_Name209 = alf_Name209
        self.alf_Name262 = alf_Name262
        self.alf_Name244 = alf_Name244
        self.alf_Name279 = alf_Name279
        self.alf_Name294 = alf_Name294
        self.alf_Name283 = alf_Name283
        self.alf_Name288 = alf_Name288
        self.alf_Name355 = alf_Name355
        self.alf_Name369 = alf_Name369
        self.alf_Name396 = alf_Name396
        self.alf_Name424 = alf_Name424
        self.alf_Name471 = alf_Name471
        self.alf_Name650 = alf_Name650
        self.alf_Name652 = alf_Name652
        self.alf_Name662 = alf_Name662
        self.alf_Name672 = alf_Name672
        self.alf_Name740 = alf_Name740
        self.alf_Name773 = alf_Name773
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alf_Name650(self):
        return self.__alf_Name650

    @alf_Name650.setter
    def alf_Name650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name650", None)
        self.__alf_Name650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameList649"):
                opp_val = getattr(old_value, "alf_NameList649", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameList649"):
                opp_val = getattr(value, "alf_NameList649", None)
                if opp_val is None:
                    setattr(value, "alf_NameList649", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_Name294(self):
        return self.__alf_Name294

    @alf_Name294.setter
    def alf_Name294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name294", None)
        self.__alf_Name294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateParameterSubstitution293"):
                opp_val = getattr(old_value, "alf_TemplateParameterSubstitution293", None)
                if opp_val == self:
                    setattr(old_value, "alf_TemplateParameterSubstitution293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateParameterSubstitution293"):
                opp_val = getattr(value, "alf_TemplateParameterSubstitution293", None)
                setattr(value, "alf_TemplateParameterSubstitution293", self)

    @property
    def alf_Name168(self):
        return self.__alf_Name168

    @alf_Name168.setter
    def alf_Name168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name168", None)
        self.__alf_Name168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EnumerationLiteralName167"):
                opp_val = getattr(old_value, "alf_EnumerationLiteralName167", None)
                if opp_val == self:
                    setattr(old_value, "alf_EnumerationLiteralName167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EnumerationLiteralName167"):
                opp_val = getattr(value, "alf_EnumerationLiteralName167", None)
                setattr(value, "alf_EnumerationLiteralName167", self)

    @property
    def alf_Name182(self):
        return self.__alf_Name182

    @alf_Name182.setter
    def alf_Name182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name182", None)
        self.__alf_Name182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ActivityDeclaration"):
                opp_val = getattr(old_value, "alf_ActivityDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_ActivityDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ActivityDeclaration"):
                opp_val = getattr(value, "alf_ActivityDeclaration", None)
                setattr(value, "alf_ActivityDeclaration", self)

    @property
    def alf_Name31(self):
        return self.__alf_Name31

    @alf_Name31.setter
    def alf_Name31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name31", None)
        self.__alf_Name31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ColonQualifiedNameCompletionOfImportReference"):
                opp_val = getattr(old_value, "alf_ColonQualifiedNameCompletionOfImportReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ColonQualifiedNameCompletionOfImportReference"):
                opp_val = getattr(value, "alf_ColonQualifiedNameCompletionOfImportReference", None)
                if opp_val is None:
                    setattr(value, "alf_ColonQualifiedNameCompletionOfImportReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_Name396(self):
        return self.__alf_Name396

    @alf_Name396.setter
    def alf_Name396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name396", None)
        self.__alf_Name396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LinkOperationTuple395"):
                opp_val = getattr(old_value, "alf_LinkOperationTuple395", None)
                if opp_val == self:
                    setattr(old_value, "alf_LinkOperationTuple395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LinkOperationTuple395"):
                opp_val = getattr(value, "alf_LinkOperationTuple395", None)
                setattr(value, "alf_LinkOperationTuple395", self)

    @property
    def alf_Name223(self):
        return self.__alf_Name223

    @alf_Name223.setter
    def alf_Name223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name223", None)
        self.__alf_Name223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PropertyDeclaration222"):
                opp_val = getattr(old_value, "alf_PropertyDeclaration222", None)
                if opp_val == self:
                    setattr(old_value, "alf_PropertyDeclaration222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PropertyDeclaration222"):
                opp_val = getattr(value, "alf_PropertyDeclaration222", None)
                setattr(value, "alf_PropertyDeclaration222", self)

    @property
    def alf_Name652(self):
        return self.__alf_Name652

    @alf_Name652.setter
    def alf_Name652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name652", None)
        self.__alf_Name652 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InLineStatement"):
                opp_val = getattr(old_value, "alf_InLineStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_InLineStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InLineStatement"):
                opp_val = getattr(value, "alf_InLineStatement", None)
                setattr(value, "alf_InLineStatement", self)

    @property
    def alf_Name244(self):
        return self.__alf_Name244

    @alf_Name244.setter
    def alf_Name244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name244", None)
        self.__alf_Name244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_OperationDeclaration"):
                opp_val = getattr(old_value, "alf_OperationDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_OperationDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_OperationDeclaration"):
                opp_val = getattr(value, "alf_OperationDeclaration", None)
                setattr(value, "alf_OperationDeclaration", self)

    @property
    def alf_Name369(self):
        return self.__alf_Name369

    @alf_Name369.setter
    def alf_Name369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name369", None)
        self.__alf_Name369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NamedExpression368"):
                opp_val = getattr(old_value, "alf_NamedExpression368", None)
                if opp_val == self:
                    setattr(old_value, "alf_NamedExpression368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NamedExpression368"):
                opp_val = getattr(value, "alf_NamedExpression368", None)
                setattr(value, "alf_NamedExpression368", self)

    @property
    def alf_Name355(self):
        return self.__alf_Name355

    @alf_Name355.setter
    def alf_Name355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name355", None)
        self.__alf_Name355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Feature354"):
                opp_val = getattr(old_value, "alf_Feature354", None)
                if opp_val == self:
                    setattr(old_value, "alf_Feature354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Feature354"):
                opp_val = getattr(value, "alf_Feature354", None)
                setattr(value, "alf_Feature354", self)

    @property
    def alf_Name39(self):
        return self.__alf_Name39

    @alf_Name39.setter
    def alf_Name39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name39", None)
        self.__alf_Name39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PackageDeclaration"):
                opp_val = getattr(old_value, "alf_PackageDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_PackageDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PackageDeclaration"):
                opp_val = getattr(value, "alf_PackageDeclaration", None)
                setattr(value, "alf_PackageDeclaration", self)

    @property
    def alf_Name279(self):
        return self.__alf_Name279

    @alf_Name279.setter
    def alf_Name279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name279", None)
        self.__alf_Name279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameBinding278"):
                opp_val = getattr(old_value, "alf_NameBinding278", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameBinding278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameBinding278"):
                opp_val = getattr(value, "alf_NameBinding278", None)
                setattr(value, "alf_NameBinding278", self)

    @property
    def alf_Name662(self):
        return self.__alf_Name662

    @alf_Name662.setter
    def alf_Name662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name662", None)
        self.__alf_Name662 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LocalNameDeclarationOrExpressionStatement661"):
                opp_val = getattr(old_value, "alf_LocalNameDeclarationOrExpressionStatement661", None)
                if opp_val == self:
                    setattr(old_value, "alf_LocalNameDeclarationOrExpressionStatement661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LocalNameDeclarationOrExpressionStatement661"):
                opp_val = getattr(value, "alf_LocalNameDeclarationOrExpressionStatement661", None)
                setattr(value, "alf_LocalNameDeclarationOrExpressionStatement661", self)

    @property
    def alf_Name151(self):
        return self.__alf_Name151

    @alf_Name151.setter
    def alf_Name151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name151", None)
        self.__alf_Name151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EnumerationDeclaration"):
                opp_val = getattr(old_value, "alf_EnumerationDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_EnumerationDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EnumerationDeclaration"):
                opp_val = getattr(value, "alf_EnumerationDeclaration", None)
                setattr(value, "alf_EnumerationDeclaration", self)

    @property
    def alf_Name25(self):
        return self.__alf_Name25

    @alf_Name25.setter
    def alf_Name25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name25", None)
        self.__alf_Name25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ImportReference24"):
                opp_val = getattr(old_value, "alf_ImportReference24", None)
                if opp_val == self:
                    setattr(old_value, "alf_ImportReference24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ImportReference24"):
                opp_val = getattr(value, "alf_ImportReference24", None)
                setattr(value, "alf_ImportReference24", self)

    @property
    def alf_Name(self):
        return self.__alf_Name

    @alf_Name.setter
    def alf_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name", None)
        self.__alf_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TaggedValue15"):
                opp_val = getattr(old_value, "alf_TaggedValue15", None)
                if opp_val == self:
                    setattr(old_value, "alf_TaggedValue15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TaggedValue15"):
                opp_val = getattr(value, "alf_TaggedValue15", None)
                setattr(value, "alf_TaggedValue15", self)

    @property
    def alf_Name262(self):
        return self.__alf_Name262

    @alf_Name262.setter
    def alf_Name262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name262", None)
        self.__alf_Name262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SignalReceptionDeclaration"):
                opp_val = getattr(old_value, "alf_SignalReceptionDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_SignalReceptionDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SignalReceptionDeclaration"):
                opp_val = getattr(value, "alf_SignalReceptionDeclaration", None)
                setattr(value, "alf_SignalReceptionDeclaration", self)

    @property
    def alf_Name66(self):
        return self.__alf_Name66

    @alf_Name66.setter
    def alf_Name66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name66", None)
        self.__alf_Name66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierTemplateParameter65"):
                opp_val = getattr(old_value, "alf_ClassifierTemplateParameter65", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierTemplateParameter65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierTemplateParameter65"):
                opp_val = getattr(value, "alf_ClassifierTemplateParameter65", None)
                setattr(value, "alf_ClassifierTemplateParameter65", self)

    @property
    def alf_Name57(self):
        return self.__alf_Name57

    @alf_Name57.setter
    def alf_Name57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name57", None)
        self.__alf_Name57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassifierSignature"):
                opp_val = getattr(old_value, "alf_ClassifierSignature", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassifierSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassifierSignature"):
                opp_val = getattr(value, "alf_ClassifierSignature", None)
                setattr(value, "alf_ClassifierSignature", self)

    @property
    def alf_Name471(self):
        return self.__alf_Name471

    @alf_Name471.setter
    def alf_Name471(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name471", None)
        self.__alf_Name471 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceOperationOrReductionOrExpansion470"):
                opp_val = getattr(old_value, "alf_SequenceOperationOrReductionOrExpansion470", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceOperationOrReductionOrExpansion470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceOperationOrReductionOrExpansion470"):
                opp_val = getattr(value, "alf_SequenceOperationOrReductionOrExpansion470", None)
                setattr(value, "alf_SequenceOperationOrReductionOrExpansion470", self)

    @property
    def alf_Name37(self):
        return self.__alf_Name37

    @alf_Name37.setter
    def alf_Name37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name37", None)
        self.__alf_Name37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AliasDefinition36"):
                opp_val = getattr(old_value, "alf_AliasDefinition36", None)
                if opp_val == self:
                    setattr(old_value, "alf_AliasDefinition36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AliasDefinition36"):
                opp_val = getattr(value, "alf_AliasDefinition36", None)
                setattr(value, "alf_AliasDefinition36", self)

    @property
    def alf_Name672(self):
        return self.__alf_Name672

    @alf_Name672.setter
    def alf_Name672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name672", None)
        self.__alf_Name672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LocalNameDeclarationStatement"):
                opp_val = getattr(old_value, "alf_LocalNameDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_LocalNameDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LocalNameDeclarationStatement"):
                opp_val = getattr(value, "alf_LocalNameDeclarationStatement", None)
                setattr(value, "alf_LocalNameDeclarationStatement", self)

    @property
    def alf_Name424(self):
        return self.__alf_Name424

    @alf_Name424.setter
    def alf_Name424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name424", None)
        self.__alf_Name424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_IndexedNamedExpression423"):
                opp_val = getattr(old_value, "alf_IndexedNamedExpression423", None)
                if opp_val == self:
                    setattr(old_value, "alf_IndexedNamedExpression423", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_IndexedNamedExpression423"):
                opp_val = getattr(value, "alf_IndexedNamedExpression423", None)
                setattr(value, "alf_IndexedNamedExpression423", self)

    @property
    def alf_Name209(self):
        return self.__alf_Name209

    @alf_Name209.setter
    def alf_Name209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name209", None)
        self.__alf_Name209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_FormalParameter208"):
                opp_val = getattr(old_value, "alf_FormalParameter208", None)
                if opp_val == self:
                    setattr(old_value, "alf_FormalParameter208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_FormalParameter208"):
                opp_val = getattr(value, "alf_FormalParameter208", None)
                setattr(value, "alf_FormalParameter208", self)

    @property
    def alf_Name773(self):
        return self.__alf_Name773

    @alf_Name773.setter
    def alf_Name773(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name773", None)
        self.__alf_Name773 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AcceptClause772"):
                opp_val = getattr(old_value, "alf_AcceptClause772", None)
                if opp_val == self:
                    setattr(old_value, "alf_AcceptClause772", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AcceptClause772"):
                opp_val = getattr(value, "alf_AcceptClause772", None)
                setattr(value, "alf_AcceptClause772", self)

    @property
    def alf_Name111(self):
        return self.__alf_Name111

    @alf_Name111.setter
    def alf_Name111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name111", None)
        self.__alf_Name111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_BehaviorClause110"):
                opp_val = getattr(old_value, "alf_BehaviorClause110", None)
                if opp_val == self:
                    setattr(old_value, "alf_BehaviorClause110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_BehaviorClause110"):
                opp_val = getattr(value, "alf_BehaviorClause110", None)
                setattr(value, "alf_BehaviorClause110", self)

    @property
    def alf_Name740(self):
        return self.__alf_Name740

    @alf_Name740.setter
    def alf_Name740(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name740", None)
        self.__alf_Name740 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LoopVariableDefinition739"):
                opp_val = getattr(old_value, "alf_LoopVariableDefinition739", None)
                if opp_val == self:
                    setattr(old_value, "alf_LoopVariableDefinition739", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LoopVariableDefinition739"):
                opp_val = getattr(value, "alf_LoopVariableDefinition739", None)
                setattr(value, "alf_LoopVariableDefinition739", self)

    @property
    def alf_Name283(self):
        return self.__alf_Name283

    @alf_Name283.setter
    def alf_Name283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name283", None)
        self.__alf_Name283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithoutBinding"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithoutBinding", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithoutBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithoutBinding"):
                opp_val = getattr(value, "alf_QualifiedNameWithoutBinding", None)
                setattr(value, "alf_QualifiedNameWithoutBinding", self)

    @property
    def alf_Name288(self):
        return self.__alf_Name288

    @alf_Name288.setter
    def alf_Name288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Name__alf_Name288", None)
        self.__alf_Name288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ColonQualifiedNameCompletionWithoutBinding287"):
                opp_val = getattr(old_value, "alf_ColonQualifiedNameCompletionWithoutBinding287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ColonQualifiedNameCompletionWithoutBinding287"):
                opp_val = getattr(value, "alf_ColonQualifiedNameCompletionWithoutBinding287", None)
                if opp_val is None:
                    setattr(value, "alf_ColonQualifiedNameCompletionWithoutBinding287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_PRIMITIVE_LITERAL:

    def __init__(self, value: str, alf_PRIMITIVE_LITERAL: "alf_TaggedValue" = None, alf_PRIMITIVE_LITERAL342: "alf_LiteralExpression" = None):
        self.value = value
        self.alf_PRIMITIVE_LITERAL = alf_PRIMITIVE_LITERAL
        self.alf_PRIMITIVE_LITERAL342 = alf_PRIMITIVE_LITERAL342
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def alf_PRIMITIVE_LITERAL342(self):
        return self.__alf_PRIMITIVE_LITERAL342

    @alf_PRIMITIVE_LITERAL342.setter
    def alf_PRIMITIVE_LITERAL342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PRIMITIVE_LITERAL__alf_PRIMITIVE_LITERAL342", None)
        self.__alf_PRIMITIVE_LITERAL342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LiteralExpression"):
                opp_val = getattr(old_value, "alf_LiteralExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_LiteralExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LiteralExpression"):
                opp_val = getattr(value, "alf_LiteralExpression", None)
                setattr(value, "alf_LiteralExpression", self)

    @property
    def alf_PRIMITIVE_LITERAL(self):
        return self.__alf_PRIMITIVE_LITERAL

    @alf_PRIMITIVE_LITERAL.setter
    def alf_PRIMITIVE_LITERAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PRIMITIVE_LITERAL__alf_PRIMITIVE_LITERAL", None)
        self.__alf_PRIMITIVE_LITERAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TaggedValue17"):
                opp_val = getattr(old_value, "alf_TaggedValue17", None)
                if opp_val == self:
                    setattr(old_value, "alf_TaggedValue17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TaggedValue17"):
                opp_val = getattr(value, "alf_TaggedValue17", None)
                setattr(value, "alf_TaggedValue17", self)

class alf_ImportDeclaration:

    def __init__(self, visibility: str, alf_ImportDeclaration: "alf_UnitDefinition" = None, alf_ImportDeclaration22: "alf_ImportReference" = None):
        self.visibility = visibility
        self.alf_ImportDeclaration = alf_ImportDeclaration
        self.alf_ImportDeclaration22 = alf_ImportDeclaration22
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def alf_ImportDeclaration22(self):
        return self.__alf_ImportDeclaration22

    @alf_ImportDeclaration22.setter
    def alf_ImportDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportDeclaration__alf_ImportDeclaration22", None)
        self.__alf_ImportDeclaration22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ImportReference"):
                opp_val = getattr(old_value, "alf_ImportReference", None)
                if opp_val == self:
                    setattr(old_value, "alf_ImportReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ImportReference"):
                opp_val = getattr(value, "alf_ImportReference", None)
                setattr(value, "alf_ImportReference", self)

    @property
    def alf_ImportDeclaration(self):
        return self.__alf_ImportDeclaration

    @alf_ImportDeclaration.setter
    def alf_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ImportDeclaration__alf_ImportDeclaration", None)
        self.__alf_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_UnitDefinition2"):
                opp_val = getattr(old_value, "alf_UnitDefinition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_UnitDefinition2"):
                opp_val = getattr(value, "alf_UnitDefinition2", None)
                if opp_val is None:
                    setattr(value, "alf_UnitDefinition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_NamespaceDeclaration:

    pass
class alf_UnitDefinition:

    def __init__(self, comment: str, alf_UnitDefinition4: "alf_StereotypeAnnotations" = None, alf_UnitDefinition6: "alf_NamespaceDefinition" = None, alf_UnitDefinition: "alf_NamespaceDeclaration" = None, alf_UnitDefinition2: set["alf_ImportDeclaration"] = None):
        self.comment = comment
        self.alf_UnitDefinition4 = alf_UnitDefinition4
        self.alf_UnitDefinition6 = alf_UnitDefinition6
        self.alf_UnitDefinition = alf_UnitDefinition
        self.alf_UnitDefinition2 = alf_UnitDefinition2 if alf_UnitDefinition2 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_UnitDefinition(self):
        return self.__alf_UnitDefinition

    @alf_UnitDefinition.setter
    def alf_UnitDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnitDefinition__alf_UnitDefinition", None)
        self.__alf_UnitDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NamespaceDeclaration"):
                opp_val = getattr(old_value, "alf_NamespaceDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "alf_NamespaceDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NamespaceDeclaration"):
                opp_val = getattr(value, "alf_NamespaceDeclaration", None)
                setattr(value, "alf_NamespaceDeclaration", self)

    @property
    def alf_UnitDefinition6(self):
        return self.__alf_UnitDefinition6

    @alf_UnitDefinition6.setter
    def alf_UnitDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnitDefinition__alf_UnitDefinition6", None)
        self.__alf_UnitDefinition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NamespaceDefinition"):
                opp_val = getattr(old_value, "alf_NamespaceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "alf_NamespaceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NamespaceDefinition"):
                opp_val = getattr(value, "alf_NamespaceDefinition", None)
                setattr(value, "alf_NamespaceDefinition", self)

    @property
    def alf_UnitDefinition2(self):
        return self.__alf_UnitDefinition2

    @alf_UnitDefinition2.setter
    def alf_UnitDefinition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnitDefinition__alf_UnitDefinition2", None)
        self.__alf_UnitDefinition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_ImportDeclaration"):
                    opp_val = getattr(item, "alf_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_ImportDeclaration"):
                    opp_val = getattr(item, "alf_ImportDeclaration", None)
                    
                    setattr(item, "alf_ImportDeclaration", self)
                    

    @property
    def alf_UnitDefinition4(self):
        return self.__alf_UnitDefinition4

    @alf_UnitDefinition4.setter
    def alf_UnitDefinition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnitDefinition__alf_UnitDefinition4", None)
        self.__alf_UnitDefinition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_StereotypeAnnotations"):
                opp_val = getattr(old_value, "alf_StereotypeAnnotations", None)
                if opp_val == self:
                    setattr(old_value, "alf_StereotypeAnnotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StereotypeAnnotations"):
                opp_val = getattr(value, "alf_StereotypeAnnotations", None)
                setattr(value, "alf_StereotypeAnnotations", self)

class alf_StereotypeAnnotation:

    pass
class NUMBER_LITERAL:

    pass
class alf_UNLIMITED_NATURAL(NUMBER_LITERAL):

    pass
class alf_INTEGER_LITERAL(NUMBER_LITERAL):

    pass
class PRIMITIVE_LITERAL:

    pass
class alf_STRING_LITERAL(PRIMITIVE_LITERAL):

    pass
class alf_NUMBER_LITERAL(PRIMITIVE_LITERAL):

    pass
class alf_BOOLEAN_LITERAL(PRIMITIVE_LITERAL):

    pass
class alf_NamespaceDefinition:

    pass
class alf_StereotypeAnnotations:

    pass
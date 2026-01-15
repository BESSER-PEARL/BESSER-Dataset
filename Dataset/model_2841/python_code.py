from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SelectOrRejectOperator(Enum):
    SELECT = "SELECT"
    REJECT = "REJECT"
class ParameterDirection(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class BooleanValue(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
class AnnotationKind(Enum):
    ISOLATED = "ISOLATED"
    DETERMINED = "DETERMINED"
    ASSURED = "ASSURED"
    PARALLEL = "PARALLEL"
class LinkOperationKind(Enum):
    CREATE = "CREATE"
    DESTROY = "DESTROY"
    CLEAR = "CLEAR"
    DESTROY_OBJECT = "DESTROY_OBJECT"
class AssignmentOperator(Enum):
    ASSIGN = "ASSIGN"
    PLUSASSIGN = "PLUSASSIGN"
    MINUSASSIGN = "MINUSASSIGN"
    MULTASSIGN = "MULTASSIGN"
    MODASSIGN = "MODASSIGN"
    DIVASSIGN = "DIVASSIGN"
    ANDASSIGN = "ANDASSIGN"
    ORASSIGN = "ORASSIGN"
    XORASSIGN = "XORASSIGN"
    LSHIFTASSIGN = "LSHIFTASSIGN"
    RSHIFTASSIGN = "RSHIFTASSIGN"
    URSHIFTASSIGN = "URSHIFTASSIGN"
class ForAllOrExistsOrOneOperator(Enum):
    FORALL = "FORALL"
    EXISTS = "EXISTS"
    ONE = "ONE"
class CollectOrIterateOperator(Enum):
    COLLECT = "COLLECT"
    ITERATE = "ITERATE"


############################################
# Definition of Classes
############################################

class alf_VariableDeclarationCompletion:

    def __init__(self, multiplicityIndicator: bool, variableName: str, alf_VariableDeclarationCompletion: "alf_InvocationOrAssignementOrDeclarationStatement" = None, alf_VariableDeclarationCompletion323: "alf_AssignmentCompletion" = None):
        self.multiplicityIndicator = multiplicityIndicator
        self.variableName = variableName
        self.alf_VariableDeclarationCompletion = alf_VariableDeclarationCompletion
        self.alf_VariableDeclarationCompletion323 = alf_VariableDeclarationCompletion323
        
    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def alf_VariableDeclarationCompletion323(self):
        return self.__alf_VariableDeclarationCompletion323

    @alf_VariableDeclarationCompletion323.setter
    def alf_VariableDeclarationCompletion323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_VariableDeclarationCompletion__alf_VariableDeclarationCompletion323", None)
        self.__alf_VariableDeclarationCompletion323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AssignmentCompletion324"):
                opp_val = getattr(old_value, "alf_AssignmentCompletion324", None)
                if opp_val == self:
                    setattr(old_value, "alf_AssignmentCompletion324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AssignmentCompletion324"):
                opp_val = getattr(value, "alf_AssignmentCompletion324", None)
                setattr(value, "alf_AssignmentCompletion324", self)

    @property
    def alf_VariableDeclarationCompletion(self):
        return self.__alf_VariableDeclarationCompletion

    @alf_VariableDeclarationCompletion.setter
    def alf_VariableDeclarationCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_VariableDeclarationCompletion__alf_VariableDeclarationCompletion", None)
        self.__alf_VariableDeclarationCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement309"):
                opp_val = getattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement309", None)
                if opp_val == self:
                    setattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InvocationOrAssignementOrDeclarationStatement309"):
                opp_val = getattr(value, "alf_InvocationOrAssignementOrDeclarationStatement309", None)
                setattr(value, "alf_InvocationOrAssignementOrDeclarationStatement309", self)

class alf_ReclassifyAllClause:

    pass
class alf_ClassificationToClause:

    pass
class alf_ClassificationFromClause:

    pass
class alf_ClassificationClause:

    pass
class alf_AcceptBlock:

    pass
class alf_CompoundAcceptStatementCompletion:

    pass
class alf_SimpleAcceptStatementCompletion:

    pass
class alf_AcceptClause:

    def __init__(self, name: str, alf_AcceptClause: "alf_AcceptStatement" = None, alf_AcceptClause280: "alf_AcceptBlock" = None, alf_AcceptClause285: "alf_QualifiedNameList" = None):
        self.name = name
        self.alf_AcceptClause = alf_AcceptClause
        self.alf_AcceptClause280 = alf_AcceptClause280
        self.alf_AcceptClause285 = alf_AcceptClause285
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_AcceptClause280(self):
        return self.__alf_AcceptClause280

    @alf_AcceptClause280.setter
    def alf_AcceptClause280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AcceptClause__alf_AcceptClause280", None)
        self.__alf_AcceptClause280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AcceptBlock279"):
                opp_val = getattr(old_value, "alf_AcceptBlock279", None)
                if opp_val == self:
                    setattr(old_value, "alf_AcceptBlock279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AcceptBlock279"):
                opp_val = getattr(value, "alf_AcceptBlock279", None)
                setattr(value, "alf_AcceptBlock279", self)

    @property
    def alf_AcceptClause285(self):
        return self.__alf_AcceptClause285

    @alf_AcceptClause285.setter
    def alf_AcceptClause285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AcceptClause__alf_AcceptClause285", None)
        self.__alf_AcceptClause285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameList286"):
                opp_val = getattr(old_value, "alf_QualifiedNameList286", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameList286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameList286"):
                opp_val = getattr(value, "alf_QualifiedNameList286", None)
                setattr(value, "alf_QualifiedNameList286", self)

    @property
    def alf_AcceptClause(self):
        return self.__alf_AcceptClause

    @alf_AcceptClause.setter
    def alf_AcceptClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AcceptClause__alf_AcceptClause", None)
        self.__alf_AcceptClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AcceptStatement"):
                opp_val = getattr(old_value, "alf_AcceptStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_AcceptStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AcceptStatement"):
                opp_val = getattr(value, "alf_AcceptStatement", None)
                setattr(value, "alf_AcceptStatement", self)

class alf_LoopVariableDefinition:

    def __init__(self, name: str, alf_LoopVariableDefinition: "alf_ForControl" = None, alf_LoopVariableDefinition261: "alf_Expression" = None, alf_LoopVariableDefinition264: "alf_Expression" = None):
        self.name = name
        self.alf_LoopVariableDefinition = alf_LoopVariableDefinition
        self.alf_LoopVariableDefinition261 = alf_LoopVariableDefinition261
        self.alf_LoopVariableDefinition264 = alf_LoopVariableDefinition264
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_LoopVariableDefinition261(self):
        return self.__alf_LoopVariableDefinition261

    @alf_LoopVariableDefinition261.setter
    def alf_LoopVariableDefinition261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition261", None)
        self.__alf_LoopVariableDefinition261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression262"):
                opp_val = getattr(old_value, "alf_Expression262", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression262"):
                opp_val = getattr(value, "alf_Expression262", None)
                setattr(value, "alf_Expression262", self)

    @property
    def alf_LoopVariableDefinition(self):
        return self.__alf_LoopVariableDefinition

    @alf_LoopVariableDefinition.setter
    def alf_LoopVariableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition", None)
        self.__alf_LoopVariableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ForControl259"):
                opp_val = getattr(old_value, "alf_ForControl259", None)
                if opp_val == self:
                    setattr(old_value, "alf_ForControl259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ForControl259"):
                opp_val = getattr(value, "alf_ForControl259", None)
                setattr(value, "alf_ForControl259", self)

    @property
    def alf_LoopVariableDefinition264(self):
        return self.__alf_LoopVariableDefinition264

    @alf_LoopVariableDefinition264.setter
    def alf_LoopVariableDefinition264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition264", None)
        self.__alf_LoopVariableDefinition264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression265"):
                opp_val = getattr(old_value, "alf_Expression265", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression265"):
                opp_val = getattr(value, "alf_Expression265", None)
                setattr(value, "alf_Expression265", self)

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
class alf_Annotation:

    def __init__(self, kind: str, args: str, alf_Annotation: "alf_AnnotatedStatement" = None):
        self.kind = kind
        self.args = args
        self.alf_Annotation = alf_Annotation
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def args(self) -> str:
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args

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
            if hasattr(old_value, "alf_AnnotatedStatement"):
                opp_val = getattr(old_value, "alf_AnnotatedStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_AnnotatedStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AnnotatedStatement"):
                opp_val = getattr(value, "alf_AnnotatedStatement", None)
                setattr(value, "alf_AnnotatedStatement", self)

class Statement:

    pass
class alf_BlockStatement(Statement):

    pass
class alf_AcceptStatement(Statement):

    pass
class alf_IfStatement(Statement):

    pass
class alf_AnnotatedStatement(Statement):

    pass
class alf_ReturnStatement(Statement):

    pass
class alf_ThisInvocationStatement(Statement):

    pass
class alf_DoStatement(Statement):

    pass
class alf_InstanceCreationInvocationStatement(Statement):

    pass
class alf_ClassifyStatement(Statement):

    pass
class alf_WhileStatement(Statement):

    pass
class alf_ForStatement(Statement):

    pass
class alf_SwitchStatement(Statement):

    pass
class alf_BreakStatement(Statement):

    pass
class alf_EmptyStatement(Statement):

    pass
class alf_InvocationOrAssignementOrDeclarationStatement(Statement):

    pass
class alf_SuperInvocationStatement(Statement):

    pass
class alf_LocalNameDeclarationStatement(Statement):

    def __init__(self, varName: str, multiplicityIndicator: bool, alf_LocalNameDeclarationStatement: "alf_QualifiedNameWithBinding" = None, alf_LocalNameDeclarationStatement207: "alf_Expression" = None):
        self.varName = varName
        self.multiplicityIndicator = multiplicityIndicator
        self.alf_LocalNameDeclarationStatement = alf_LocalNameDeclarationStatement
        self.alf_LocalNameDeclarationStatement207 = alf_LocalNameDeclarationStatement207
        
    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def alf_LocalNameDeclarationStatement207(self):
        return self.__alf_LocalNameDeclarationStatement207

    @alf_LocalNameDeclarationStatement207.setter
    def alf_LocalNameDeclarationStatement207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LocalNameDeclarationStatement__alf_LocalNameDeclarationStatement207", None)
        self.__alf_LocalNameDeclarationStatement207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression208"):
                opp_val = getattr(old_value, "alf_Expression208", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression208"):
                opp_val = getattr(value, "alf_Expression208", None)
                setattr(value, "alf_Expression208", self)

    @property
    def alf_LocalNameDeclarationStatement(self):
        return self.__alf_LocalNameDeclarationStatement

    @alf_LocalNameDeclarationStatement.setter
    def alf_LocalNameDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LocalNameDeclarationStatement__alf_LocalNameDeclarationStatement", None)
        self.__alf_LocalNameDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding205"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding205", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding205"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding205", None)
                setattr(value, "alf_QualifiedNameWithBinding205", self)

class alf_InlineStatement(Statement):

    def __init__(self, langageName: str, body: str):
        self.langageName = langageName
        self.body = body
        
    @property
    def langageName(self) -> str:
        return self.__langageName

    @langageName.setter
    def langageName(self, langageName: str):
        self.__langageName = langageName

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class alf_DocumentedStatement:

    def __init__(self, comment: str, alf_DocumentedStatement: "alf_StatementSequence" = None, alf_DocumentedStatement200: "alf_Statement" = None, alf_DocumentedStatement243: "alf_NonEmptyStatementSequence" = None):
        self.comment = comment
        self.alf_DocumentedStatement = alf_DocumentedStatement
        self.alf_DocumentedStatement200 = alf_DocumentedStatement200
        self.alf_DocumentedStatement243 = alf_DocumentedStatement243
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_DocumentedStatement200(self):
        return self.__alf_DocumentedStatement200

    @alf_DocumentedStatement200.setter
    def alf_DocumentedStatement200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement200", None)
        self.__alf_DocumentedStatement200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Statement201"):
                opp_val = getattr(old_value, "alf_Statement201", None)
                if opp_val == self:
                    setattr(old_value, "alf_Statement201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Statement201"):
                opp_val = getattr(value, "alf_Statement201", None)
                setattr(value, "alf_Statement201", self)

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
            if hasattr(old_value, "alf_StatementSequence194"):
                opp_val = getattr(old_value, "alf_StatementSequence194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StatementSequence194"):
                opp_val = getattr(value, "alf_StatementSequence194", None)
                if opp_val is None:
                    setattr(value, "alf_StatementSequence194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_DocumentedStatement243(self):
        return self.__alf_DocumentedStatement243

    @alf_DocumentedStatement243.setter
    def alf_DocumentedStatement243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement243", None)
        self.__alf_DocumentedStatement243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NonEmptyStatementSequence242"):
                opp_val = getattr(old_value, "alf_NonEmptyStatementSequence242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NonEmptyStatementSequence242"):
                opp_val = getattr(value, "alf_NonEmptyStatementSequence242", None)
                if opp_val is None:
                    setattr(value, "alf_NonEmptyStatementSequence242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_StatementSequence:

    pass
class alf_ClassExtentExpression:

    pass
class alf_SequenceElement:

    pass
class alf_PartialSequenceConstructionCompletion:

    pass
class alf_AccessCompletion:

    pass
class alf_SequenceConstructionCompletion:

    def __init__(self, multiplicityIndicator: bool, alf_SequenceConstructionCompletion: "alf_InstanceCreationExpression" = None, alf_SequenceConstructionCompletion184: "alf_SequenceConstructionExpression" = None):
        self.multiplicityIndicator = multiplicityIndicator
        self.alf_SequenceConstructionCompletion = alf_SequenceConstructionCompletion
        self.alf_SequenceConstructionCompletion184 = alf_SequenceConstructionCompletion184
        
    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

    @property
    def alf_SequenceConstructionCompletion184(self):
        return self.__alf_SequenceConstructionCompletion184

    @alf_SequenceConstructionCompletion184.setter
    def alf_SequenceConstructionCompletion184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionCompletion__alf_SequenceConstructionCompletion184", None)
        self.__alf_SequenceConstructionCompletion184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceConstructionExpression185"):
                opp_val = getattr(old_value, "alf_SequenceConstructionExpression185", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceConstructionExpression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceConstructionExpression185"):
                opp_val = getattr(value, "alf_SequenceConstructionExpression185", None)
                setattr(value, "alf_SequenceConstructionExpression185", self)

    @property
    def alf_SequenceConstructionCompletion(self):
        return self.__alf_SequenceConstructionCompletion

    @alf_SequenceConstructionCompletion.setter
    def alf_SequenceConstructionCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionCompletion__alf_SequenceConstructionCompletion", None)
        self.__alf_SequenceConstructionCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InstanceCreationExpression167"):
                opp_val = getattr(old_value, "alf_InstanceCreationExpression167", None)
                if opp_val == self:
                    setattr(old_value, "alf_InstanceCreationExpression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InstanceCreationExpression167"):
                opp_val = getattr(value, "alf_InstanceCreationExpression167", None)
                setattr(value, "alf_InstanceCreationExpression167", self)

class alf_NonLiteralValueSpecification:

    pass
class SequenceExpansionExpression:

    pass
class alf_IsUniqueOperation(SequenceExpansionExpression):

    def __init__(self, name: str, alf_IsUniqueOperation: "alf_Expression" = None):
        self.name = name
        self.alf_IsUniqueOperation = alf_IsUniqueOperation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_IsUniqueOperation(self):
        return self.__alf_IsUniqueOperation

    @alf_IsUniqueOperation.setter
    def alf_IsUniqueOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_IsUniqueOperation__alf_IsUniqueOperation", None)
        self.__alf_IsUniqueOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression146"):
                opp_val = getattr(old_value, "alf_Expression146", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression146"):
                opp_val = getattr(value, "alf_Expression146", None)
                setattr(value, "alf_Expression146", self)

class alf_CollectOrIterateOperation(SequenceExpansionExpression):

    def __init__(self, op: str, expr1: str, expr2: str, expr3: str, expr4: str):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.expr4 = expr4
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expr3(self) -> str:
        return self.__expr3

    @expr3.setter
    def expr3(self, expr3: str):
        self.__expr3 = expr3

    @property
    def expr1(self) -> str:
        return self.__expr1

    @expr1.setter
    def expr1(self, expr1: str):
        self.__expr1 = expr1

    @property
    def expr2(self) -> str:
        return self.__expr2

    @expr2.setter
    def expr2(self, expr2: str):
        self.__expr2 = expr2

    @property
    def expr4(self) -> str:
        return self.__expr4

    @expr4.setter
    def expr4(self, expr4: str):
        self.__expr4 = expr4

class alf_ForAllOrExistsOrOneOperation(SequenceExpansionExpression):

    def __init__(self, op: str, expr1: str, expr2: str, expr3: str, expr4: str):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.expr4 = expr4
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expr1(self) -> str:
        return self.__expr1

    @expr1.setter
    def expr1(self, expr1: str):
        self.__expr1 = expr1

    @property
    def expr2(self) -> str:
        return self.__expr2

    @expr2.setter
    def expr2(self, expr2: str):
        self.__expr2 = expr2

    @property
    def expr3(self) -> str:
        return self.__expr3

    @expr3.setter
    def expr3(self, expr3: str):
        self.__expr3 = expr3

    @property
    def expr4(self) -> str:
        return self.__expr4

    @expr4.setter
    def expr4(self, expr4: str):
        self.__expr4 = expr4

class alf_SelectOrRejectOperation(SequenceExpansionExpression):

    def __init__(self, op: str, expr1: str, expr2: str, expr3: str, expr4: str):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.expr4 = expr4
        
    @property
    def expr1(self) -> str:
        return self.__expr1

    @expr1.setter
    def expr1(self, expr1: str):
        self.__expr1 = expr1

    @property
    def expr3(self) -> str:
        return self.__expr3

    @expr3.setter
    def expr3(self, expr3: str):
        self.__expr3 = expr3

    @property
    def expr4(self) -> str:
        return self.__expr4

    @expr4.setter
    def expr4(self, expr4: str):
        self.__expr4 = expr4

    @property
    def expr2(self) -> str:
        return self.__expr2

    @expr2.setter
    def expr2(self, expr2: str):
        self.__expr2 = expr2

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class alf_LinkOperationTupleElement:

    def __init__(self, objectOrRole: str, alf_LinkOperationTupleElement128: "alf_Expression" = None, alf_LinkOperationTupleElement131: "alf_ValueSpecification" = None, alf_LinkOperationTupleElement: "alf_LinkOperationTuple" = None):
        self.objectOrRole = objectOrRole
        self.alf_LinkOperationTupleElement128 = alf_LinkOperationTupleElement128
        self.alf_LinkOperationTupleElement131 = alf_LinkOperationTupleElement131
        self.alf_LinkOperationTupleElement = alf_LinkOperationTupleElement
        
    @property
    def objectOrRole(self) -> str:
        return self.__objectOrRole

    @objectOrRole.setter
    def objectOrRole(self, objectOrRole: str):
        self.__objectOrRole = objectOrRole

    @property
    def alf_LinkOperationTupleElement131(self):
        return self.__alf_LinkOperationTupleElement131

    @alf_LinkOperationTupleElement131.setter
    def alf_LinkOperationTupleElement131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationTupleElement__alf_LinkOperationTupleElement131", None)
        self.__alf_LinkOperationTupleElement131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ValueSpecification132"):
                opp_val = getattr(old_value, "alf_ValueSpecification132", None)
                if opp_val == self:
                    setattr(old_value, "alf_ValueSpecification132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ValueSpecification132"):
                opp_val = getattr(value, "alf_ValueSpecification132", None)
                setattr(value, "alf_ValueSpecification132", self)

    @property
    def alf_LinkOperationTupleElement128(self):
        return self.__alf_LinkOperationTupleElement128

    @alf_LinkOperationTupleElement128.setter
    def alf_LinkOperationTupleElement128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationTupleElement__alf_LinkOperationTupleElement128", None)
        self.__alf_LinkOperationTupleElement128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression129"):
                opp_val = getattr(old_value, "alf_Expression129", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression129"):
                opp_val = getattr(value, "alf_Expression129", None)
                setattr(value, "alf_Expression129", self)

    @property
    def alf_LinkOperationTupleElement(self):
        return self.__alf_LinkOperationTupleElement

    @alf_LinkOperationTupleElement.setter
    def alf_LinkOperationTupleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationTupleElement__alf_LinkOperationTupleElement", None)
        self.__alf_LinkOperationTupleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LinkOperationTuple126"):
                opp_val = getattr(old_value, "alf_LinkOperationTuple126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LinkOperationTuple126"):
                opp_val = getattr(value, "alf_LinkOperationTuple126", None)
                if opp_val is None:
                    setattr(value, "alf_LinkOperationTuple126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_ValueSpecification:

    pass
class alf_LinkOperationTuple:

    pass
class alf_OperationCallExpressionWithoutDot:

    def __init__(self, operationName: str, alf_OperationCallExpressionWithoutDot: "alf_Tuple" = None, alf_OperationCallExpressionWithoutDot117: "alf_SuffixExpression" = None, alf_OperationCallExpressionWithoutDot157: "alf_SuperInvocationExpression" = None):
        self.operationName = operationName
        self.alf_OperationCallExpressionWithoutDot = alf_OperationCallExpressionWithoutDot
        self.alf_OperationCallExpressionWithoutDot117 = alf_OperationCallExpressionWithoutDot117
        self.alf_OperationCallExpressionWithoutDot157 = alf_OperationCallExpressionWithoutDot157
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def alf_OperationCallExpressionWithoutDot117(self):
        return self.__alf_OperationCallExpressionWithoutDot117

    @alf_OperationCallExpressionWithoutDot117.setter
    def alf_OperationCallExpressionWithoutDot117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpressionWithoutDot__alf_OperationCallExpressionWithoutDot117", None)
        self.__alf_OperationCallExpressionWithoutDot117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression118"):
                opp_val = getattr(old_value, "alf_SuffixExpression118", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression118"):
                opp_val = getattr(value, "alf_SuffixExpression118", None)
                setattr(value, "alf_SuffixExpression118", self)

    @property
    def alf_OperationCallExpressionWithoutDot157(self):
        return self.__alf_OperationCallExpressionWithoutDot157

    @alf_OperationCallExpressionWithoutDot157.setter
    def alf_OperationCallExpressionWithoutDot157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpressionWithoutDot__alf_OperationCallExpressionWithoutDot157", None)
        self.__alf_OperationCallExpressionWithoutDot157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuperInvocationExpression"):
                opp_val = getattr(old_value, "alf_SuperInvocationExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuperInvocationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuperInvocationExpression"):
                opp_val = getattr(value, "alf_SuperInvocationExpression", None)
                setattr(value, "alf_SuperInvocationExpression", self)

    @property
    def alf_OperationCallExpressionWithoutDot(self):
        return self.__alf_OperationCallExpressionWithoutDot

    @alf_OperationCallExpressionWithoutDot.setter
    def alf_OperationCallExpressionWithoutDot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpressionWithoutDot__alf_OperationCallExpressionWithoutDot", None)
        self.__alf_OperationCallExpressionWithoutDot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Tuple115"):
                opp_val = getattr(old_value, "alf_Tuple115", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple115"):
                opp_val = getattr(value, "alf_Tuple115", None)
                setattr(value, "alf_Tuple115", self)

class SuffixExpression:

    pass
class alf_SequenceExpansionExpression(SuffixExpression):

    pass
class alf_SequenceOperationExpression(SuffixExpression):

    def __init__(self, operationName: str, alf_SequenceOperationExpression: "alf_Tuple" = None, alf_SequenceOperationExpression136: "alf_SuffixExpression" = None):
        self.operationName = operationName
        self.alf_SequenceOperationExpression = alf_SequenceOperationExpression
        self.alf_SequenceOperationExpression136 = alf_SequenceOperationExpression136
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def alf_SequenceOperationExpression(self):
        return self.__alf_SequenceOperationExpression

    @alf_SequenceOperationExpression.setter
    def alf_SequenceOperationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationExpression__alf_SequenceOperationExpression", None)
        self.__alf_SequenceOperationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Tuple134"):
                opp_val = getattr(old_value, "alf_Tuple134", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple134"):
                opp_val = getattr(value, "alf_Tuple134", None)
                setattr(value, "alf_Tuple134", self)

    @property
    def alf_SequenceOperationExpression136(self):
        return self.__alf_SequenceOperationExpression136

    @alf_SequenceOperationExpression136.setter
    def alf_SequenceOperationExpression136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceOperationExpression__alf_SequenceOperationExpression136", None)
        self.__alf_SequenceOperationExpression136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression137"):
                opp_val = getattr(old_value, "alf_SuffixExpression137", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression137"):
                opp_val = getattr(value, "alf_SuffixExpression137", None)
                setattr(value, "alf_SuffixExpression137", self)

class alf_SequenceReductionExpression(SuffixExpression):

    def __init__(self, isOrdered: bool, alf_SequenceReductionExpression: "alf_QualifiedNameWithBinding" = None, alf_SequenceReductionExpression141: "alf_SuffixExpression" = None):
        self.isOrdered = isOrdered
        self.alf_SequenceReductionExpression = alf_SequenceReductionExpression
        self.alf_SequenceReductionExpression141 = alf_SequenceReductionExpression141
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def alf_SequenceReductionExpression(self):
        return self.__alf_SequenceReductionExpression

    @alf_SequenceReductionExpression.setter
    def alf_SequenceReductionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceReductionExpression__alf_SequenceReductionExpression", None)
        self.__alf_SequenceReductionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding139"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding139", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding139"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding139", None)
                setattr(value, "alf_QualifiedNameWithBinding139", self)

    @property
    def alf_SequenceReductionExpression141(self):
        return self.__alf_SequenceReductionExpression141

    @alf_SequenceReductionExpression141.setter
    def alf_SequenceReductionExpression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceReductionExpression__alf_SequenceReductionExpression141", None)
        self.__alf_SequenceReductionExpression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression142"):
                opp_val = getattr(old_value, "alf_SuffixExpression142", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression142"):
                opp_val = getattr(value, "alf_SuffixExpression142", None)
                setattr(value, "alf_SuffixExpression142", self)

class alf_PropertyCallExpression(SuffixExpression):

    def __init__(self, propertyName: str, alf_PropertyCallExpression: "alf_Expression" = None, alf_PropertyCallExpression122: "alf_SuffixExpression" = None):
        self.propertyName = propertyName
        self.alf_PropertyCallExpression = alf_PropertyCallExpression
        self.alf_PropertyCallExpression122 = alf_PropertyCallExpression122
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def alf_PropertyCallExpression122(self):
        return self.__alf_PropertyCallExpression122

    @alf_PropertyCallExpression122.setter
    def alf_PropertyCallExpression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyCallExpression__alf_PropertyCallExpression122", None)
        self.__alf_PropertyCallExpression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression123"):
                opp_val = getattr(old_value, "alf_SuffixExpression123", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression123"):
                opp_val = getattr(value, "alf_SuffixExpression123", None)
                setattr(value, "alf_SuffixExpression123", self)

    @property
    def alf_PropertyCallExpression(self):
        return self.__alf_PropertyCallExpression

    @alf_PropertyCallExpression.setter
    def alf_PropertyCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyCallExpression__alf_PropertyCallExpression", None)
        self.__alf_PropertyCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression120"):
                opp_val = getattr(old_value, "alf_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression120"):
                opp_val = getattr(value, "alf_Expression120", None)
                setattr(value, "alf_Expression120", self)

class alf_LinkOperationExpression(SuffixExpression):

    def __init__(self, kind: str, alf_LinkOperationExpression: "alf_LinkOperationTuple" = None):
        self.kind = kind
        self.alf_LinkOperationExpression = alf_LinkOperationExpression
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def alf_LinkOperationExpression(self):
        return self.__alf_LinkOperationExpression

    @alf_LinkOperationExpression.setter
    def alf_LinkOperationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationExpression__alf_LinkOperationExpression", None)
        self.__alf_LinkOperationExpression = value
        
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

class alf_OperationCallExpression(SuffixExpression):

    def __init__(self, operationName: str, alf_OperationCallExpression: "alf_Tuple" = None, alf_OperationCallExpression112: "alf_SuffixExpression" = None, alf_OperationCallExpression160: "alf_SuperInvocationExpression" = None):
        self.operationName = operationName
        self.alf_OperationCallExpression = alf_OperationCallExpression
        self.alf_OperationCallExpression112 = alf_OperationCallExpression112
        self.alf_OperationCallExpression160 = alf_OperationCallExpression160
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def alf_OperationCallExpression160(self):
        return self.__alf_OperationCallExpression160

    @alf_OperationCallExpression160.setter
    def alf_OperationCallExpression160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpression__alf_OperationCallExpression160", None)
        self.__alf_OperationCallExpression160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuperInvocationExpression159"):
                opp_val = getattr(old_value, "alf_SuperInvocationExpression159", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuperInvocationExpression159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuperInvocationExpression159"):
                opp_val = getattr(value, "alf_SuperInvocationExpression159", None)
                setattr(value, "alf_SuperInvocationExpression159", self)

    @property
    def alf_OperationCallExpression(self):
        return self.__alf_OperationCallExpression

    @alf_OperationCallExpression.setter
    def alf_OperationCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpression__alf_OperationCallExpression", None)
        self.__alf_OperationCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Tuple110"):
                opp_val = getattr(old_value, "alf_Tuple110", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple110"):
                opp_val = getattr(value, "alf_Tuple110", None)
                setattr(value, "alf_Tuple110", self)

    @property
    def alf_OperationCallExpression112(self):
        return self.__alf_OperationCallExpression112

    @alf_OperationCallExpression112.setter
    def alf_OperationCallExpression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpression__alf_OperationCallExpression112", None)
        self.__alf_OperationCallExpression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression113"):
                opp_val = getattr(old_value, "alf_SuffixExpression113", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression113"):
                opp_val = getattr(value, "alf_SuffixExpression113", None)
                setattr(value, "alf_SuffixExpression113", self)

class alf_PrimaryExpression:

    pass
class alf_UnaryExpression:

    def __init__(self, op: str, alf_UnaryExpression: "alf_MultiplicativeExpression" = None, alf_UnaryExpression106: "alf_PrimaryExpression" = None):
        self.op = op
        self.alf_UnaryExpression = alf_UnaryExpression
        self.alf_UnaryExpression106 = alf_UnaryExpression106
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_UnaryExpression106(self):
        return self.__alf_UnaryExpression106

    @alf_UnaryExpression106.setter
    def alf_UnaryExpression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnaryExpression__alf_UnaryExpression106", None)
        self.__alf_UnaryExpression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PrimaryExpression"):
                opp_val = getattr(old_value, "alf_PrimaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_PrimaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PrimaryExpression"):
                opp_val = getattr(value, "alf_PrimaryExpression", None)
                setattr(value, "alf_PrimaryExpression", self)

    @property
    def alf_UnaryExpression(self):
        return self.__alf_UnaryExpression

    @alf_UnaryExpression.setter
    def alf_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnaryExpression__alf_UnaryExpression", None)
        self.__alf_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicativeExpression104"):
                opp_val = getattr(old_value, "alf_MultiplicativeExpression104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicativeExpression104"):
                opp_val = getattr(value, "alf_MultiplicativeExpression104", None)
                if opp_val is None:
                    setattr(value, "alf_MultiplicativeExpression104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_MultiplicativeExpression:

    def __init__(self, op: str, alf_MultiplicativeExpression: "alf_AdditiveExpression" = None, alf_MultiplicativeExpression104: set["alf_UnaryExpression"] = None):
        self.op = op
        self.alf_MultiplicativeExpression = alf_MultiplicativeExpression
        self.alf_MultiplicativeExpression104 = alf_MultiplicativeExpression104 if alf_MultiplicativeExpression104 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_MultiplicativeExpression(self):
        return self.__alf_MultiplicativeExpression

    @alf_MultiplicativeExpression.setter
    def alf_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpression__alf_MultiplicativeExpression", None)
        self.__alf_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AdditiveExpression102"):
                opp_val = getattr(old_value, "alf_AdditiveExpression102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AdditiveExpression102"):
                opp_val = getattr(value, "alf_AdditiveExpression102", None)
                if opp_val is None:
                    setattr(value, "alf_AdditiveExpression102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_MultiplicativeExpression104(self):
        return self.__alf_MultiplicativeExpression104

    @alf_MultiplicativeExpression104.setter
    def alf_MultiplicativeExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpression__alf_MultiplicativeExpression104", None)
        self.__alf_MultiplicativeExpression104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_UnaryExpression"):
                    opp_val = getattr(item, "alf_UnaryExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_UnaryExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_UnaryExpression"):
                    opp_val = getattr(item, "alf_UnaryExpression", None)
                    
                    setattr(item, "alf_UnaryExpression", self)
                    

class alf_AdditiveExpression:

    def __init__(self, op: str, alf_AdditiveExpression: "alf_ShiftExpression" = None, alf_AdditiveExpression102: set["alf_MultiplicativeExpression"] = None):
        self.op = op
        self.alf_AdditiveExpression = alf_AdditiveExpression
        self.alf_AdditiveExpression102 = alf_AdditiveExpression102 if alf_AdditiveExpression102 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_AdditiveExpression(self):
        return self.__alf_AdditiveExpression

    @alf_AdditiveExpression.setter
    def alf_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpression__alf_AdditiveExpression", None)
        self.__alf_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression100"):
                opp_val = getattr(old_value, "alf_ShiftExpression100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression100"):
                opp_val = getattr(value, "alf_ShiftExpression100", None)
                if opp_val is None:
                    setattr(value, "alf_ShiftExpression100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_AdditiveExpression102(self):
        return self.__alf_AdditiveExpression102

    @alf_AdditiveExpression102.setter
    def alf_AdditiveExpression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpression__alf_AdditiveExpression102", None)
        self.__alf_AdditiveExpression102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_MultiplicativeExpression"):
                    opp_val = getattr(item, "alf_MultiplicativeExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_MultiplicativeExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_MultiplicativeExpression"):
                    opp_val = getattr(item, "alf_MultiplicativeExpression", None)
                    
                    setattr(item, "alf_MultiplicativeExpression", self)
                    

class alf_ShiftExpression:

    def __init__(self, op: str, alf_ShiftExpression: "alf_RelationalExpression" = None, alf_ShiftExpression98: "alf_RelationalExpression" = None, alf_ShiftExpression100: set["alf_AdditiveExpression"] = None):
        self.op = op
        self.alf_ShiftExpression = alf_ShiftExpression
        self.alf_ShiftExpression98 = alf_ShiftExpression98
        self.alf_ShiftExpression100 = alf_ShiftExpression100 if alf_ShiftExpression100 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_ShiftExpression98(self):
        return self.__alf_ShiftExpression98

    @alf_ShiftExpression98.setter
    def alf_ShiftExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpression__alf_ShiftExpression98", None)
        self.__alf_ShiftExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpression97"):
                opp_val = getattr(old_value, "alf_RelationalExpression97", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression97"):
                opp_val = getattr(value, "alf_RelationalExpression97", None)
                setattr(value, "alf_RelationalExpression97", self)

    @property
    def alf_ShiftExpression(self):
        return self.__alf_ShiftExpression

    @alf_ShiftExpression.setter
    def alf_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpression__alf_ShiftExpression", None)
        self.__alf_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpression95"):
                opp_val = getattr(old_value, "alf_RelationalExpression95", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression95"):
                opp_val = getattr(value, "alf_RelationalExpression95", None)
                setattr(value, "alf_RelationalExpression95", self)

    @property
    def alf_ShiftExpression100(self):
        return self.__alf_ShiftExpression100

    @alf_ShiftExpression100.setter
    def alf_ShiftExpression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpression__alf_ShiftExpression100", None)
        self.__alf_ShiftExpression100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_AdditiveExpression"):
                    opp_val = getattr(item, "alf_AdditiveExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_AdditiveExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_AdditiveExpression"):
                    opp_val = getattr(item, "alf_AdditiveExpression", None)
                    
                    setattr(item, "alf_AdditiveExpression", self)
                    

class alf_RelationalExpression:

    def __init__(self, op: str, alf_RelationalExpression: "alf_ClassificationExpression" = None, alf_RelationalExpression95: "alf_ShiftExpression" = None, alf_RelationalExpression97: "alf_ShiftExpression" = None):
        self.op = op
        self.alf_RelationalExpression = alf_RelationalExpression
        self.alf_RelationalExpression95 = alf_RelationalExpression95
        self.alf_RelationalExpression97 = alf_RelationalExpression97
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_RelationalExpression97(self):
        return self.__alf_RelationalExpression97

    @alf_RelationalExpression97.setter
    def alf_RelationalExpression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpression__alf_RelationalExpression97", None)
        self.__alf_RelationalExpression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression98"):
                opp_val = getattr(old_value, "alf_ShiftExpression98", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression98"):
                opp_val = getattr(value, "alf_ShiftExpression98", None)
                setattr(value, "alf_ShiftExpression98", self)

    @property
    def alf_RelationalExpression95(self):
        return self.__alf_RelationalExpression95

    @alf_RelationalExpression95.setter
    def alf_RelationalExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpression__alf_RelationalExpression95", None)
        self.__alf_RelationalExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression"):
                opp_val = getattr(old_value, "alf_ShiftExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression"):
                opp_val = getattr(value, "alf_ShiftExpression", None)
                setattr(value, "alf_ShiftExpression", self)

    @property
    def alf_RelationalExpression(self):
        return self.__alf_RelationalExpression

    @alf_RelationalExpression.setter
    def alf_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpression__alf_RelationalExpression", None)
        self.__alf_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpression90"):
                opp_val = getattr(old_value, "alf_ClassificationExpression90", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpression90"):
                opp_val = getattr(value, "alf_ClassificationExpression90", None)
                setattr(value, "alf_ClassificationExpression90", self)

class alf_ClassificationExpression:

    def __init__(self, op: str, alf_ClassificationExpression: "alf_EqualityExpression" = None, alf_ClassificationExpression90: "alf_RelationalExpression" = None, alf_ClassificationExpression92: "alf_NameExpression" = None):
        self.op = op
        self.alf_ClassificationExpression = alf_ClassificationExpression
        self.alf_ClassificationExpression90 = alf_ClassificationExpression90
        self.alf_ClassificationExpression92 = alf_ClassificationExpression92
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_ClassificationExpression92(self):
        return self.__alf_ClassificationExpression92

    @alf_ClassificationExpression92.setter
    def alf_ClassificationExpression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpression__alf_ClassificationExpression92", None)
        self.__alf_ClassificationExpression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameExpression93"):
                opp_val = getattr(old_value, "alf_NameExpression93", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameExpression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameExpression93"):
                opp_val = getattr(value, "alf_NameExpression93", None)
                setattr(value, "alf_NameExpression93", self)

    @property
    def alf_ClassificationExpression(self):
        return self.__alf_ClassificationExpression

    @alf_ClassificationExpression.setter
    def alf_ClassificationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpression__alf_ClassificationExpression", None)
        self.__alf_ClassificationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_EqualityExpression88"):
                opp_val = getattr(old_value, "alf_EqualityExpression88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EqualityExpression88"):
                opp_val = getattr(value, "alf_EqualityExpression88", None)
                if opp_val is None:
                    setattr(value, "alf_EqualityExpression88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_ClassificationExpression90(self):
        return self.__alf_ClassificationExpression90

    @alf_ClassificationExpression90.setter
    def alf_ClassificationExpression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpression__alf_ClassificationExpression90", None)
        self.__alf_ClassificationExpression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpression"):
                opp_val = getattr(old_value, "alf_RelationalExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression"):
                opp_val = getattr(value, "alf_RelationalExpression", None)
                setattr(value, "alf_RelationalExpression", self)

class alf_EqualityExpression:

    def __init__(self, op: str, alf_EqualityExpression: "alf_AndExpression" = None, alf_EqualityExpression88: set["alf_ClassificationExpression"] = None):
        self.op = op
        self.alf_EqualityExpression = alf_EqualityExpression
        self.alf_EqualityExpression88 = alf_EqualityExpression88 if alf_EqualityExpression88 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_EqualityExpression88(self):
        return self.__alf_EqualityExpression88

    @alf_EqualityExpression88.setter
    def alf_EqualityExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpression__alf_EqualityExpression88", None)
        self.__alf_EqualityExpression88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_ClassificationExpression"):
                    opp_val = getattr(item, "alf_ClassificationExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_ClassificationExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_ClassificationExpression"):
                    opp_val = getattr(item, "alf_ClassificationExpression", None)
                    
                    setattr(item, "alf_ClassificationExpression", self)
                    

    @property
    def alf_EqualityExpression(self):
        return self.__alf_EqualityExpression

    @alf_EqualityExpression.setter
    def alf_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpression__alf_EqualityExpression", None)
        self.__alf_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AndExpression86"):
                opp_val = getattr(old_value, "alf_AndExpression86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AndExpression86"):
                opp_val = getattr(value, "alf_AndExpression86", None)
                if opp_val is None:
                    setattr(value, "alf_AndExpression86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_AndExpression:

    pass
class alf_ExclusiveOrExpression:

    pass
class alf_InclusiveOrExpression:

    pass
class alf_ConditionalAndExpression:

    pass
class alf_Tuple:

    pass
class alf_QualifiedNamePath:

    pass
class alf_ConditionalOrExpression:

    pass
class Expression:

    pass
class alf_ConditionalTestExpression(Expression):

    pass
class SequenceElement:

    pass
class alf_SequenceConstructionExpression(SequenceElement):

    pass
class alf_TupleElement:

    pass
class alf_NamedTemplateBinding:

    def __init__(self, formal: str, alf_NamedTemplateBinding: "alf_TemplateBinding" = None, alf_NamedTemplateBinding57: "alf_QualifiedNameWithBinding" = None):
        self.formal = formal
        self.alf_NamedTemplateBinding = alf_NamedTemplateBinding
        self.alf_NamedTemplateBinding57 = alf_NamedTemplateBinding57
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def alf_NamedTemplateBinding(self):
        return self.__alf_NamedTemplateBinding

    @alf_NamedTemplateBinding.setter
    def alf_NamedTemplateBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NamedTemplateBinding__alf_NamedTemplateBinding", None)
        self.__alf_NamedTemplateBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateBinding55"):
                opp_val = getattr(old_value, "alf_TemplateBinding55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding55"):
                opp_val = getattr(value, "alf_TemplateBinding55", None)
                if opp_val is None:
                    setattr(value, "alf_TemplateBinding55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_NamedTemplateBinding57(self):
        return self.__alf_NamedTemplateBinding57

    @alf_NamedTemplateBinding57.setter
    def alf_NamedTemplateBinding57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NamedTemplateBinding__alf_NamedTemplateBinding57", None)
        self.__alf_NamedTemplateBinding57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding58"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding58", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding58"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding58", None)
                setattr(value, "alf_QualifiedNameWithBinding58", self)

class alf_TemplateBinding:

    pass
class alf_UnqualifiedName:

    def __init__(self, name: str, alf_UnqualifiedName: "alf_QualifiedNamePath" = None, alf_UnqualifiedName53: "alf_TemplateBinding" = None):
        self.name = name
        self.alf_UnqualifiedName = alf_UnqualifiedName
        self.alf_UnqualifiedName53 = alf_UnqualifiedName53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_UnqualifiedName53(self):
        return self.__alf_UnqualifiedName53

    @alf_UnqualifiedName53.setter
    def alf_UnqualifiedName53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnqualifiedName__alf_UnqualifiedName53", None)
        self.__alf_UnqualifiedName53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateBinding"):
                opp_val = getattr(old_value, "alf_TemplateBinding", None)
                if opp_val == self:
                    setattr(old_value, "alf_TemplateBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding"):
                opp_val = getattr(value, "alf_TemplateBinding", None)
                setattr(value, "alf_TemplateBinding", self)

    @property
    def alf_UnqualifiedName(self):
        return self.__alf_UnqualifiedName

    @alf_UnqualifiedName.setter
    def alf_UnqualifiedName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnqualifiedName__alf_UnqualifiedName", None)
        self.__alf_UnqualifiedName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNamePath51"):
                opp_val = getattr(old_value, "alf_QualifiedNamePath51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNamePath51"):
                opp_val = getattr(value, "alf_QualifiedNamePath51", None)
                if opp_val is None:
                    setattr(value, "alf_QualifiedNamePath51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_SequenceConstructionOrAccessCompletion:

    def __init__(self, multiplicityIndicator: bool, alf_SequenceConstructionOrAccessCompletion: "alf_NameExpression" = None, alf_SequenceConstructionOrAccessCompletion172: "alf_AccessCompletion" = None, alf_SequenceConstructionOrAccessCompletion174: "alf_PartialSequenceConstructionCompletion" = None, alf_SequenceConstructionOrAccessCompletion176: "alf_SequenceConstructionExpression" = None):
        self.multiplicityIndicator = multiplicityIndicator
        self.alf_SequenceConstructionOrAccessCompletion = alf_SequenceConstructionOrAccessCompletion
        self.alf_SequenceConstructionOrAccessCompletion172 = alf_SequenceConstructionOrAccessCompletion172
        self.alf_SequenceConstructionOrAccessCompletion174 = alf_SequenceConstructionOrAccessCompletion174
        self.alf_SequenceConstructionOrAccessCompletion176 = alf_SequenceConstructionOrAccessCompletion176
        
    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

    @property
    def alf_SequenceConstructionOrAccessCompletion172(self):
        return self.__alf_SequenceConstructionOrAccessCompletion172

    @alf_SequenceConstructionOrAccessCompletion172.setter
    def alf_SequenceConstructionOrAccessCompletion172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion172", None)
        self.__alf_SequenceConstructionOrAccessCompletion172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AccessCompletion"):
                opp_val = getattr(old_value, "alf_AccessCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_AccessCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AccessCompletion"):
                opp_val = getattr(value, "alf_AccessCompletion", None)
                setattr(value, "alf_AccessCompletion", self)

    @property
    def alf_SequenceConstructionOrAccessCompletion(self):
        return self.__alf_SequenceConstructionOrAccessCompletion

    @alf_SequenceConstructionOrAccessCompletion.setter
    def alf_SequenceConstructionOrAccessCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion", None)
        self.__alf_SequenceConstructionOrAccessCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameExpression46"):
                opp_val = getattr(old_value, "alf_NameExpression46", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameExpression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameExpression46"):
                opp_val = getattr(value, "alf_NameExpression46", None)
                setattr(value, "alf_NameExpression46", self)

    @property
    def alf_SequenceConstructionOrAccessCompletion176(self):
        return self.__alf_SequenceConstructionOrAccessCompletion176

    @alf_SequenceConstructionOrAccessCompletion176.setter
    def alf_SequenceConstructionOrAccessCompletion176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion176", None)
        self.__alf_SequenceConstructionOrAccessCompletion176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceConstructionExpression"):
                opp_val = getattr(old_value, "alf_SequenceConstructionExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceConstructionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceConstructionExpression"):
                opp_val = getattr(value, "alf_SequenceConstructionExpression", None)
                setattr(value, "alf_SequenceConstructionExpression", self)

    @property
    def alf_SequenceConstructionOrAccessCompletion174(self):
        return self.__alf_SequenceConstructionOrAccessCompletion174

    @alf_SequenceConstructionOrAccessCompletion174.setter
    def alf_SequenceConstructionOrAccessCompletion174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion174", None)
        self.__alf_SequenceConstructionOrAccessCompletion174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_PartialSequenceConstructionCompletion"):
                opp_val = getattr(old_value, "alf_PartialSequenceConstructionCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_PartialSequenceConstructionCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_PartialSequenceConstructionCompletion"):
                opp_val = getattr(value, "alf_PartialSequenceConstructionCompletion", None)
                setattr(value, "alf_PartialSequenceConstructionCompletion", self)

class alf_NUMBER_LITERAL_WITHOUT_SUFFIX:

    def __init__(self, value: str, alf_NUMBER_LITERAL_WITHOUT_SUFFIX: "alf_MultiplicityRange" = None, alf_NUMBER_LITERAL_WITHOUT_SUFFIX28: "alf_MultiplicityRange" = None):
        self.value = value
        self.alf_NUMBER_LITERAL_WITHOUT_SUFFIX = alf_NUMBER_LITERAL_WITHOUT_SUFFIX
        self.alf_NUMBER_LITERAL_WITHOUT_SUFFIX28 = alf_NUMBER_LITERAL_WITHOUT_SUFFIX28
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def alf_NUMBER_LITERAL_WITHOUT_SUFFIX(self):
        return self.__alf_NUMBER_LITERAL_WITHOUT_SUFFIX

    @alf_NUMBER_LITERAL_WITHOUT_SUFFIX.setter
    def alf_NUMBER_LITERAL_WITHOUT_SUFFIX(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NUMBER_LITERAL_WITHOUT_SUFFIX__alf_NUMBER_LITERAL_WITHOUT_SUFFIX", None)
        self.__alf_NUMBER_LITERAL_WITHOUT_SUFFIX = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicityRange25"):
                opp_val = getattr(old_value, "alf_MultiplicityRange25", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicityRange25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicityRange25"):
                opp_val = getattr(value, "alf_MultiplicityRange25", None)
                setattr(value, "alf_MultiplicityRange25", self)

    @property
    def alf_NUMBER_LITERAL_WITHOUT_SUFFIX28(self):
        return self.__alf_NUMBER_LITERAL_WITHOUT_SUFFIX28

    @alf_NUMBER_LITERAL_WITHOUT_SUFFIX28.setter
    def alf_NUMBER_LITERAL_WITHOUT_SUFFIX28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NUMBER_LITERAL_WITHOUT_SUFFIX__alf_NUMBER_LITERAL_WITHOUT_SUFFIX28", None)
        self.__alf_NUMBER_LITERAL_WITHOUT_SUFFIX28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_MultiplicityRange27"):
                opp_val = getattr(old_value, "alf_MultiplicityRange27", None)
                if opp_val == self:
                    setattr(old_value, "alf_MultiplicityRange27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicityRange27"):
                opp_val = getattr(value, "alf_MultiplicityRange27", None)
                setattr(value, "alf_MultiplicityRange27", self)

class NonLiteralValueSpecification:

    pass
class NUMBER_LITERAL:

    pass
class alf_UNLIMITED_LITERAL(NUMBER_LITERAL):

    pass
class alf_INTEGER_LITERAL(NUMBER_LITERAL):

    pass
class LITERAL:

    pass
class alf_STRING_LITERAL(LITERAL):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class alf_NUMBER_LITERAL(LITERAL):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class alf_BOOLEAN_LITERAL(LITERAL):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class alf_SuffixExpression:

    pass
class ValueSpecification:

    pass
class alf_NameExpression(ValueSpecification, NonLiteralValueSpecification):

    def __init__(self, prefixOp: str, postfixOp: str, id: str, alf_NameExpression46: "alf_SequenceConstructionOrAccessCompletion" = None, alf_NameExpression48: "alf_SuffixExpression" = None, alf_NameExpression: "alf_QualifiedNamePath" = None, alf_NameExpression44: "alf_Tuple" = None, alf_NameExpression93: "alf_ClassificationExpression" = None, alf_NameExpression307: "alf_InvocationOrAssignementOrDeclarationStatement" = None):
        self.prefixOp = prefixOp
        self.postfixOp = postfixOp
        self.id = id
        self.alf_NameExpression46 = alf_NameExpression46
        self.alf_NameExpression48 = alf_NameExpression48
        self.alf_NameExpression = alf_NameExpression
        self.alf_NameExpression44 = alf_NameExpression44
        self.alf_NameExpression93 = alf_NameExpression93
        self.alf_NameExpression307 = alf_NameExpression307
        
    @property
    def postfixOp(self) -> str:
        return self.__postfixOp

    @postfixOp.setter
    def postfixOp(self, postfixOp: str):
        self.__postfixOp = postfixOp

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def prefixOp(self) -> str:
        return self.__prefixOp

    @prefixOp.setter
    def prefixOp(self, prefixOp: str):
        self.__prefixOp = prefixOp

    @property
    def alf_NameExpression48(self):
        return self.__alf_NameExpression48

    @alf_NameExpression48.setter
    def alf_NameExpression48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression48", None)
        self.__alf_NameExpression48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression49"):
                opp_val = getattr(old_value, "alf_SuffixExpression49", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression49"):
                opp_val = getattr(value, "alf_SuffixExpression49", None)
                setattr(value, "alf_SuffixExpression49", self)

    @property
    def alf_NameExpression46(self):
        return self.__alf_NameExpression46

    @alf_NameExpression46.setter
    def alf_NameExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression46", None)
        self.__alf_NameExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceConstructionOrAccessCompletion"):
                opp_val = getattr(old_value, "alf_SequenceConstructionOrAccessCompletion", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceConstructionOrAccessCompletion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceConstructionOrAccessCompletion"):
                opp_val = getattr(value, "alf_SequenceConstructionOrAccessCompletion", None)
                setattr(value, "alf_SequenceConstructionOrAccessCompletion", self)

    @property
    def alf_NameExpression44(self):
        return self.__alf_NameExpression44

    @alf_NameExpression44.setter
    def alf_NameExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression44", None)
        self.__alf_NameExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Tuple"):
                opp_val = getattr(old_value, "alf_Tuple", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple"):
                opp_val = getattr(value, "alf_Tuple", None)
                setattr(value, "alf_Tuple", self)

    @property
    def alf_NameExpression93(self):
        return self.__alf_NameExpression93

    @alf_NameExpression93.setter
    def alf_NameExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression93", None)
        self.__alf_NameExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpression92"):
                opp_val = getattr(old_value, "alf_ClassificationExpression92", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpression92"):
                opp_val = getattr(value, "alf_ClassificationExpression92", None)
                setattr(value, "alf_ClassificationExpression92", self)

    @property
    def alf_NameExpression307(self):
        return self.__alf_NameExpression307

    @alf_NameExpression307.setter
    def alf_NameExpression307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression307", None)
        self.__alf_NameExpression307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement"):
                opp_val = getattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InvocationOrAssignementOrDeclarationStatement"):
                opp_val = getattr(value, "alf_InvocationOrAssignementOrDeclarationStatement", None)
                setattr(value, "alf_InvocationOrAssignementOrDeclarationStatement", self)

    @property
    def alf_NameExpression(self):
        return self.__alf_NameExpression

    @alf_NameExpression.setter
    def alf_NameExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression", None)
        self.__alf_NameExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNamePath"):
                opp_val = getattr(old_value, "alf_QualifiedNamePath", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNamePath", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNamePath"):
                opp_val = getattr(value, "alf_QualifiedNamePath", None)
                setattr(value, "alf_QualifiedNamePath", self)

class alf_ParenthesizedExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_InstanceCreationExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_SuperInvocationExpression(ValueSpecification, NonLiteralValueSpecification):

    def __init__(self, className: str, alf_SuperInvocationExpression: "alf_OperationCallExpressionWithoutDot" = None, alf_SuperInvocationExpression159: "alf_OperationCallExpression" = None, alf_SuperInvocationExpression314: "alf_SuperInvocationStatement" = None):
        self.className = className
        self.alf_SuperInvocationExpression = alf_SuperInvocationExpression
        self.alf_SuperInvocationExpression159 = alf_SuperInvocationExpression159
        self.alf_SuperInvocationExpression314 = alf_SuperInvocationExpression314
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def alf_SuperInvocationExpression314(self):
        return self.__alf_SuperInvocationExpression314

    @alf_SuperInvocationExpression314.setter
    def alf_SuperInvocationExpression314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SuperInvocationExpression__alf_SuperInvocationExpression314", None)
        self.__alf_SuperInvocationExpression314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuperInvocationStatement"):
                opp_val = getattr(old_value, "alf_SuperInvocationStatement", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuperInvocationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuperInvocationStatement"):
                opp_val = getattr(value, "alf_SuperInvocationStatement", None)
                setattr(value, "alf_SuperInvocationStatement", self)

    @property
    def alf_SuperInvocationExpression159(self):
        return self.__alf_SuperInvocationExpression159

    @alf_SuperInvocationExpression159.setter
    def alf_SuperInvocationExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SuperInvocationExpression__alf_SuperInvocationExpression159", None)
        self.__alf_SuperInvocationExpression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_OperationCallExpression160"):
                opp_val = getattr(old_value, "alf_OperationCallExpression160", None)
                if opp_val == self:
                    setattr(old_value, "alf_OperationCallExpression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_OperationCallExpression160"):
                opp_val = getattr(value, "alf_OperationCallExpression160", None)
                setattr(value, "alf_OperationCallExpression160", self)

    @property
    def alf_SuperInvocationExpression(self):
        return self.__alf_SuperInvocationExpression

    @alf_SuperInvocationExpression.setter
    def alf_SuperInvocationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SuperInvocationExpression__alf_SuperInvocationExpression", None)
        self.__alf_SuperInvocationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_OperationCallExpressionWithoutDot157"):
                opp_val = getattr(old_value, "alf_OperationCallExpressionWithoutDot157", None)
                if opp_val == self:
                    setattr(old_value, "alf_OperationCallExpressionWithoutDot157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_OperationCallExpressionWithoutDot157"):
                opp_val = getattr(value, "alf_OperationCallExpressionWithoutDot157", None)
                setattr(value, "alf_OperationCallExpressionWithoutDot157", self)

class alf_ThisExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_NullExpression(ValueSpecification):

    pass
class alf_LITERAL(ValueSpecification):

    pass
class alf_Statement:

    pass
class alf_AssignmentCompletion:

    def __init__(self, op: str, alf_AssignmentCompletion: "alf_Test" = None, alf_AssignmentCompletion312: "alf_InvocationOrAssignementOrDeclarationStatement" = None, alf_AssignmentCompletion319: "alf_ThisInvocationStatement" = None, alf_AssignmentCompletion324: "alf_VariableDeclarationCompletion" = None, alf_AssignmentCompletion326: "alf_Expression" = None):
        self.op = op
        self.alf_AssignmentCompletion = alf_AssignmentCompletion
        self.alf_AssignmentCompletion312 = alf_AssignmentCompletion312
        self.alf_AssignmentCompletion319 = alf_AssignmentCompletion319
        self.alf_AssignmentCompletion324 = alf_AssignmentCompletion324
        self.alf_AssignmentCompletion326 = alf_AssignmentCompletion326
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_AssignmentCompletion326(self):
        return self.__alf_AssignmentCompletion326

    @alf_AssignmentCompletion326.setter
    def alf_AssignmentCompletion326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion326", None)
        self.__alf_AssignmentCompletion326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression327"):
                opp_val = getattr(old_value, "alf_Expression327", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression327"):
                opp_val = getattr(value, "alf_Expression327", None)
                setattr(value, "alf_Expression327", self)

    @property
    def alf_AssignmentCompletion(self):
        return self.__alf_AssignmentCompletion

    @alf_AssignmentCompletion.setter
    def alf_AssignmentCompletion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion", None)
        self.__alf_AssignmentCompletion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Test35"):
                opp_val = getattr(old_value, "alf_Test35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Test35"):
                opp_val = getattr(value, "alf_Test35", None)
                if opp_val is None:
                    setattr(value, "alf_Test35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_AssignmentCompletion324(self):
        return self.__alf_AssignmentCompletion324

    @alf_AssignmentCompletion324.setter
    def alf_AssignmentCompletion324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion324", None)
        self.__alf_AssignmentCompletion324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_VariableDeclarationCompletion323"):
                opp_val = getattr(old_value, "alf_VariableDeclarationCompletion323", None)
                if opp_val == self:
                    setattr(old_value, "alf_VariableDeclarationCompletion323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_VariableDeclarationCompletion323"):
                opp_val = getattr(value, "alf_VariableDeclarationCompletion323", None)
                setattr(value, "alf_VariableDeclarationCompletion323", self)

    @property
    def alf_AssignmentCompletion319(self):
        return self.__alf_AssignmentCompletion319

    @alf_AssignmentCompletion319.setter
    def alf_AssignmentCompletion319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion319", None)
        self.__alf_AssignmentCompletion319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ThisInvocationStatement318"):
                opp_val = getattr(old_value, "alf_ThisInvocationStatement318", None)
                if opp_val == self:
                    setattr(old_value, "alf_ThisInvocationStatement318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ThisInvocationStatement318"):
                opp_val = getattr(value, "alf_ThisInvocationStatement318", None)
                setattr(value, "alf_ThisInvocationStatement318", self)

    @property
    def alf_AssignmentCompletion312(self):
        return self.__alf_AssignmentCompletion312

    @alf_AssignmentCompletion312.setter
    def alf_AssignmentCompletion312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion312", None)
        self.__alf_AssignmentCompletion312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement311"):
                opp_val = getattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement311", None)
                if opp_val == self:
                    setattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InvocationOrAssignementOrDeclarationStatement311"):
                opp_val = getattr(value, "alf_InvocationOrAssignementOrDeclarationStatement311", None)
                setattr(value, "alf_InvocationOrAssignementOrDeclarationStatement311", self)

class alf_Expression(SequenceElement):

    pass
class alf_Test:

    pass
class alf_QualifiedNameList:

    pass
class alf_QualifiedNameWithBinding:

    def __init__(self, id: str, alf_QualifiedNameWithBinding: "alf_TypeName" = None, alf_QualifiedNameWithBinding58: "alf_NamedTemplateBinding" = None, alf_QualifiedNameWithBinding60: "alf_TemplateBinding" = None, alf_QualifiedNameWithBinding64: "alf_QualifiedNameWithBinding" = None, alf_QualifiedNameWithBinding62: "alf_QualifiedNameWithBinding" = None, alf_QualifiedNameWithBinding139: "alf_SequenceReductionExpression" = None, alf_QualifiedNameWithBinding162: "alf_InstanceCreationExpression" = None, alf_QualifiedNameWithBinding205: "alf_LocalNameDeclarationStatement" = None, alf_QualifiedNameWithBinding305: "alf_QualifiedNameList" = None):
        self.id = id
        self.alf_QualifiedNameWithBinding = alf_QualifiedNameWithBinding
        self.alf_QualifiedNameWithBinding58 = alf_QualifiedNameWithBinding58
        self.alf_QualifiedNameWithBinding60 = alf_QualifiedNameWithBinding60
        self.alf_QualifiedNameWithBinding64 = alf_QualifiedNameWithBinding64
        self.alf_QualifiedNameWithBinding62 = alf_QualifiedNameWithBinding62
        self.alf_QualifiedNameWithBinding139 = alf_QualifiedNameWithBinding139
        self.alf_QualifiedNameWithBinding162 = alf_QualifiedNameWithBinding162
        self.alf_QualifiedNameWithBinding205 = alf_QualifiedNameWithBinding205
        self.alf_QualifiedNameWithBinding305 = alf_QualifiedNameWithBinding305
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alf_QualifiedNameWithBinding62(self):
        return self.__alf_QualifiedNameWithBinding62

    @alf_QualifiedNameWithBinding62.setter
    def alf_QualifiedNameWithBinding62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding62", None)
        self.__alf_QualifiedNameWithBinding62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding64"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding64", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding64"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding64", None)
                setattr(value, "alf_QualifiedNameWithBinding64", self)

    @property
    def alf_QualifiedNameWithBinding58(self):
        return self.__alf_QualifiedNameWithBinding58

    @alf_QualifiedNameWithBinding58.setter
    def alf_QualifiedNameWithBinding58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding58", None)
        self.__alf_QualifiedNameWithBinding58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NamedTemplateBinding57"):
                opp_val = getattr(old_value, "alf_NamedTemplateBinding57", None)
                if opp_val == self:
                    setattr(old_value, "alf_NamedTemplateBinding57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NamedTemplateBinding57"):
                opp_val = getattr(value, "alf_NamedTemplateBinding57", None)
                setattr(value, "alf_NamedTemplateBinding57", self)

    @property
    def alf_QualifiedNameWithBinding64(self):
        return self.__alf_QualifiedNameWithBinding64

    @alf_QualifiedNameWithBinding64.setter
    def alf_QualifiedNameWithBinding64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding64", None)
        self.__alf_QualifiedNameWithBinding64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding62"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding62", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding62"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding62", None)
                setattr(value, "alf_QualifiedNameWithBinding62", self)

    @property
    def alf_QualifiedNameWithBinding60(self):
        return self.__alf_QualifiedNameWithBinding60

    @alf_QualifiedNameWithBinding60.setter
    def alf_QualifiedNameWithBinding60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding60", None)
        self.__alf_QualifiedNameWithBinding60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateBinding61"):
                opp_val = getattr(old_value, "alf_TemplateBinding61", None)
                if opp_val == self:
                    setattr(old_value, "alf_TemplateBinding61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding61"):
                opp_val = getattr(value, "alf_TemplateBinding61", None)
                setattr(value, "alf_TemplateBinding61", self)

    @property
    def alf_QualifiedNameWithBinding305(self):
        return self.__alf_QualifiedNameWithBinding305

    @alf_QualifiedNameWithBinding305.setter
    def alf_QualifiedNameWithBinding305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding305", None)
        self.__alf_QualifiedNameWithBinding305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameList304"):
                opp_val = getattr(old_value, "alf_QualifiedNameList304", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameList304"):
                opp_val = getattr(value, "alf_QualifiedNameList304", None)
                if opp_val is None:
                    setattr(value, "alf_QualifiedNameList304", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_QualifiedNameWithBinding(self):
        return self.__alf_QualifiedNameWithBinding

    @alf_QualifiedNameWithBinding.setter
    def alf_QualifiedNameWithBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding", None)
        self.__alf_QualifiedNameWithBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypeName30"):
                opp_val = getattr(old_value, "alf_TypeName30", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypeName30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypeName30"):
                opp_val = getattr(value, "alf_TypeName30", None)
                setattr(value, "alf_TypeName30", self)

    @property
    def alf_QualifiedNameWithBinding205(self):
        return self.__alf_QualifiedNameWithBinding205

    @alf_QualifiedNameWithBinding205.setter
    def alf_QualifiedNameWithBinding205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding205", None)
        self.__alf_QualifiedNameWithBinding205 = value
        
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
    def alf_QualifiedNameWithBinding139(self):
        return self.__alf_QualifiedNameWithBinding139

    @alf_QualifiedNameWithBinding139.setter
    def alf_QualifiedNameWithBinding139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding139", None)
        self.__alf_QualifiedNameWithBinding139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceReductionExpression"):
                opp_val = getattr(old_value, "alf_SequenceReductionExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceReductionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceReductionExpression"):
                opp_val = getattr(value, "alf_SequenceReductionExpression", None)
                setattr(value, "alf_SequenceReductionExpression", self)

    @property
    def alf_QualifiedNameWithBinding162(self):
        return self.__alf_QualifiedNameWithBinding162

    @alf_QualifiedNameWithBinding162.setter
    def alf_QualifiedNameWithBinding162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding162", None)
        self.__alf_QualifiedNameWithBinding162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InstanceCreationExpression"):
                opp_val = getattr(old_value, "alf_InstanceCreationExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_InstanceCreationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InstanceCreationExpression"):
                opp_val = getattr(value, "alf_InstanceCreationExpression", None)
                setattr(value, "alf_InstanceCreationExpression", self)

class NUMBER_LITERAL_WITHOUT_SUFFIX:

    pass
class alf_UNLIMITED_LITERAL_WITHOUT_SUFFIX(NUMBER_LITERAL_WITHOUT_SUFFIX):

    pass
class alf_INTEGER_LITERAL_WITHOUT_SUFFIX(NUMBER_LITERAL_WITHOUT_SUFFIX):

    pass
class alf_Operations:

    def __init__(self, imports: str, alf_Operations: set["alf_OperationDefinitionOrStub"] = None):
        self.imports = imports
        self.alf_Operations = alf_Operations if alf_Operations is not None else set()
        
    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def alf_Operations(self):
        return self.__alf_Operations

    @alf_Operations.setter
    def alf_Operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Operations__alf_Operations", None)
        self.__alf_Operations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alf_OperationDefinitionOrStub"):
                    opp_val = getattr(item, "alf_OperationDefinitionOrStub", None)
                    
                    if opp_val == self:
                        setattr(item, "alf_OperationDefinitionOrStub", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alf_OperationDefinitionOrStub"):
                    opp_val = getattr(item, "alf_OperationDefinitionOrStub", None)
                    
                    setattr(item, "alf_OperationDefinitionOrStub", self)
                    

class alf_MultiplicityRange:

    pass
class alf_Multiplicity:

    def __init__(self, ordered: bool, nonUnique: bool, sequence: bool, alf_Multiplicity: "alf_TypePart" = None, alf_Multiplicity23: "alf_MultiplicityRange" = None):
        self.ordered = ordered
        self.nonUnique = nonUnique
        self.sequence = sequence
        self.alf_Multiplicity = alf_Multiplicity
        self.alf_Multiplicity23 = alf_Multiplicity23
        
    @property
    def nonUnique(self) -> bool:
        return self.__nonUnique

    @nonUnique.setter
    def nonUnique(self, nonUnique: bool):
        self.__nonUnique = nonUnique

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def sequence(self) -> bool:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: bool):
        self.__sequence = sequence

    @property
    def alf_Multiplicity23(self):
        return self.__alf_Multiplicity23

    @alf_Multiplicity23.setter
    def alf_Multiplicity23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_Multiplicity__alf_Multiplicity23", None)
        self.__alf_Multiplicity23 = value
        
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
            if hasattr(old_value, "alf_TypePart21"):
                opp_val = getattr(old_value, "alf_TypePart21", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart21"):
                opp_val = getattr(value, "alf_TypePart21", None)
                setattr(value, "alf_TypePart21", self)

class alf_TypeName:

    pass
class alf_FormalParameter:

    def __init__(self, direction: str, name: str, alf_FormalParameter: "alf_FormalParameterList" = None, alf_FormalParameter16: "alf_TypePart" = None):
        self.direction = direction
        self.name = name
        self.alf_FormalParameter = alf_FormalParameter
        self.alf_FormalParameter16 = alf_FormalParameter16
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "alf_FormalParameterList14"):
                opp_val = getattr(old_value, "alf_FormalParameterList14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_FormalParameterList14"):
                opp_val = getattr(value, "alf_FormalParameterList14", None)
                if opp_val is None:
                    setattr(value, "alf_FormalParameterList14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_FormalParameter16(self):
        return self.__alf_FormalParameter16

    @alf_FormalParameter16.setter
    def alf_FormalParameter16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_FormalParameter__alf_FormalParameter16", None)
        self.__alf_FormalParameter16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart17"):
                opp_val = getattr(old_value, "alf_TypePart17", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart17"):
                opp_val = getattr(value, "alf_TypePart17", None)
                setattr(value, "alf_TypePart17", self)

class alf_FormalParameterList:

    pass
class alf_RedefinitionClause:

    pass
class alf_TypePart:

    pass
class alf_FormalParameters:

    pass
class alf_Block:

    pass
class alf_OperationDeclaration:

    def __init__(self, name: str, alf_OperationDeclaration: "alf_OperationDefinitionOrStub" = None, alf_OperationDeclaration6: "alf_FormalParameters" = None, alf_OperationDeclaration8: "alf_TypePart" = None, alf_OperationDeclaration10: "alf_RedefinitionClause" = None):
        self.name = name
        self.alf_OperationDeclaration = alf_OperationDeclaration
        self.alf_OperationDeclaration6 = alf_OperationDeclaration6
        self.alf_OperationDeclaration8 = alf_OperationDeclaration8
        self.alf_OperationDeclaration10 = alf_OperationDeclaration10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_OperationDeclaration10(self):
        return self.__alf_OperationDeclaration10

    @alf_OperationDeclaration10.setter
    def alf_OperationDeclaration10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration10", None)
        self.__alf_OperationDeclaration10 = value
        
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
    def alf_OperationDeclaration6(self):
        return self.__alf_OperationDeclaration6

    @alf_OperationDeclaration6.setter
    def alf_OperationDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration6", None)
        self.__alf_OperationDeclaration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_FormalParameters"):
                opp_val = getattr(old_value, "alf_FormalParameters", None)
                if opp_val == self:
                    setattr(old_value, "alf_FormalParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_FormalParameters"):
                opp_val = getattr(value, "alf_FormalParameters", None)
                setattr(value, "alf_FormalParameters", self)

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
            if hasattr(old_value, "alf_OperationDefinitionOrStub2"):
                opp_val = getattr(old_value, "alf_OperationDefinitionOrStub2", None)
                if opp_val == self:
                    setattr(old_value, "alf_OperationDefinitionOrStub2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_OperationDefinitionOrStub2"):
                opp_val = getattr(value, "alf_OperationDefinitionOrStub2", None)
                setattr(value, "alf_OperationDefinitionOrStub2", self)

    @property
    def alf_OperationDeclaration8(self):
        return self.__alf_OperationDeclaration8

    @alf_OperationDeclaration8.setter
    def alf_OperationDeclaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationDeclaration__alf_OperationDeclaration8", None)
        self.__alf_OperationDeclaration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TypePart"):
                opp_val = getattr(old_value, "alf_TypePart", None)
                if opp_val == self:
                    setattr(old_value, "alf_TypePart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TypePart"):
                opp_val = getattr(value, "alf_TypePart", None)
                setattr(value, "alf_TypePart", self)

class alf_OperationDefinitionOrStub:

    pass
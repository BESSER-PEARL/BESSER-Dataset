from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ForAllOrExistsOrOneOperator(Enum):
    FORALL = "FORALL"
    EXISTS = "EXISTS"
    ONE = "ONE"
class SelectOrRejectOperator(Enum):
    SELECT = "SELECT"
    REJECT = "REJECT"
class CollectOrIterateOperator(Enum):
    COLLECT = "COLLECT"
    ITERATE = "ITERATE"
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
class AnnotationKind(Enum):
    ISOLATED = "ISOLATED"
    DETERMINED = "DETERMINED"
    ASSURED = "ASSURED"
    PARALLEL = "PARALLEL"
class LinkOperationKind(Enum):
    CLEAR = "CLEAR"
    CREATE = "CREATE"
    DESTROY = "DESTROY"
class BooleanValue(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


############################################
# Definition of Classes
############################################

class alf_VariableDeclarationCompletion:

    def __init__(self, multiplicityIndicator: bool, variableName: str, alf_VariableDeclarationCompletion: "alf_InvocationOrAssignementOrDeclarationStatement" = None, alf_VariableDeclarationCompletion289: "alf_AssignmentCompletion" = None):
        self.multiplicityIndicator = multiplicityIndicator
        self.variableName = variableName
        self.alf_VariableDeclarationCompletion = alf_VariableDeclarationCompletion
        self.alf_VariableDeclarationCompletion289 = alf_VariableDeclarationCompletion289
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

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
            if hasattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement275"):
                opp_val = getattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement275", None)
                if opp_val == self:
                    setattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InvocationOrAssignementOrDeclarationStatement275"):
                opp_val = getattr(value, "alf_InvocationOrAssignementOrDeclarationStatement275", None)
                setattr(value, "alf_InvocationOrAssignementOrDeclarationStatement275", self)

    @property
    def alf_VariableDeclarationCompletion289(self):
        return self.__alf_VariableDeclarationCompletion289

    @alf_VariableDeclarationCompletion289.setter
    def alf_VariableDeclarationCompletion289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_VariableDeclarationCompletion__alf_VariableDeclarationCompletion289", None)
        self.__alf_VariableDeclarationCompletion289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AssignmentCompletion290"):
                opp_val = getattr(old_value, "alf_AssignmentCompletion290", None)
                if opp_val == self:
                    setattr(old_value, "alf_AssignmentCompletion290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AssignmentCompletion290"):
                opp_val = getattr(value, "alf_AssignmentCompletion290", None)
                setattr(value, "alf_AssignmentCompletion290", self)

class alf_ReclassifyAllClause:

    pass
class alf_ClassificationToClause:

    pass
class alf_ClassificationFromClause:

    pass
class alf_ClassificationClause:

    pass
class alf_QualifiedNameList:

    pass
class alf_AcceptBlock:

    pass
class alf_CompoundAcceptStatementCompletion:

    pass
class alf_SimpleAcceptStatementCompletion:

    pass
class alf_AcceptClause:

    def __init__(self, name: str, alf_AcceptClause: "alf_AcceptStatement" = None, alf_AcceptClause247: "alf_AcceptBlock" = None, alf_AcceptClause252: "alf_QualifiedNameList" = None):
        self.name = name
        self.alf_AcceptClause = alf_AcceptClause
        self.alf_AcceptClause247 = alf_AcceptClause247
        self.alf_AcceptClause252 = alf_AcceptClause252
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_AcceptClause252(self):
        return self.__alf_AcceptClause252

    @alf_AcceptClause252.setter
    def alf_AcceptClause252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AcceptClause__alf_AcceptClause252", None)
        self.__alf_AcceptClause252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameList"):
                opp_val = getattr(old_value, "alf_QualifiedNameList", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameList"):
                opp_val = getattr(value, "alf_QualifiedNameList", None)
                setattr(value, "alf_QualifiedNameList", self)

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

    @property
    def alf_AcceptClause247(self):
        return self.__alf_AcceptClause247

    @alf_AcceptClause247.setter
    def alf_AcceptClause247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AcceptClause__alf_AcceptClause247", None)
        self.__alf_AcceptClause247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_AcceptBlock246"):
                opp_val = getattr(old_value, "alf_AcceptBlock246", None)
                if opp_val == self:
                    setattr(old_value, "alf_AcceptBlock246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AcceptBlock246"):
                opp_val = getattr(value, "alf_AcceptBlock246", None)
                setattr(value, "alf_AcceptBlock246", self)

class alf_NonEmptyStatementSequence:

    pass
class alf_SwitchCase:

    pass
class alf_SwitchDefaultClause:

    pass
class alf_SwitchClause:

    pass
class alf_LoopVariableDefinition:

    def __init__(self, name: str, alf_LoopVariableDefinition: "alf_ForControl" = None, alf_LoopVariableDefinition222: "alf_Expression" = None, alf_LoopVariableDefinition225: "alf_Expression" = None, alf_LoopVariableDefinition228: "alf_QualifiedNameWithBinding" = None, alf_LoopVariableDefinition231: "alf_Expression" = None):
        self.name = name
        self.alf_LoopVariableDefinition = alf_LoopVariableDefinition
        self.alf_LoopVariableDefinition222 = alf_LoopVariableDefinition222
        self.alf_LoopVariableDefinition225 = alf_LoopVariableDefinition225
        self.alf_LoopVariableDefinition228 = alf_LoopVariableDefinition228
        self.alf_LoopVariableDefinition231 = alf_LoopVariableDefinition231
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_LoopVariableDefinition228(self):
        return self.__alf_LoopVariableDefinition228

    @alf_LoopVariableDefinition228.setter
    def alf_LoopVariableDefinition228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition228", None)
        self.__alf_LoopVariableDefinition228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding229"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding229", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding229"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding229", None)
                setattr(value, "alf_QualifiedNameWithBinding229", self)

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
            if hasattr(old_value, "alf_ForControl220"):
                opp_val = getattr(old_value, "alf_ForControl220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ForControl220"):
                opp_val = getattr(value, "alf_ForControl220", None)
                if opp_val is None:
                    setattr(value, "alf_ForControl220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_LoopVariableDefinition231(self):
        return self.__alf_LoopVariableDefinition231

    @alf_LoopVariableDefinition231.setter
    def alf_LoopVariableDefinition231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition231", None)
        self.__alf_LoopVariableDefinition231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression232"):
                opp_val = getattr(old_value, "alf_Expression232", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression232"):
                opp_val = getattr(value, "alf_Expression232", None)
                setattr(value, "alf_Expression232", self)

    @property
    def alf_LoopVariableDefinition225(self):
        return self.__alf_LoopVariableDefinition225

    @alf_LoopVariableDefinition225.setter
    def alf_LoopVariableDefinition225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition225", None)
        self.__alf_LoopVariableDefinition225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression226"):
                opp_val = getattr(old_value, "alf_Expression226", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression226"):
                opp_val = getattr(value, "alf_Expression226", None)
                setattr(value, "alf_Expression226", self)

    @property
    def alf_LoopVariableDefinition222(self):
        return self.__alf_LoopVariableDefinition222

    @alf_LoopVariableDefinition222.setter
    def alf_LoopVariableDefinition222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LoopVariableDefinition__alf_LoopVariableDefinition222", None)
        self.__alf_LoopVariableDefinition222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression223"):
                opp_val = getattr(old_value, "alf_Expression223", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression223"):
                opp_val = getattr(value, "alf_Expression223", None)
                setattr(value, "alf_Expression223", self)

class alf_ForControl:

    pass
class alf_NonFinalClause:

    pass
class alf_ConcurrentClauses:

    pass
class alf_FinalClause:

    pass
class alf_SequentialClauses:

    pass
class alf_PartialSequenceConstructionCompletion:

    pass
class alf_AccessCompletion:

    pass
class alf_Annotation:

    def __init__(self, kind: str, args: str, alf_Annotation: "alf_AnnotatedStatement" = None):
        self.kind = kind
        self.args = args
        self.alf_Annotation = alf_Annotation
        
    @property
    def args(self) -> str:
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
class alf_InvocationOrAssignementOrDeclarationStatement(Statement):

    pass
class alf_ClassifyStatement(Statement):

    pass
class alf_EmptyStatement(Statement):

    pass
class alf_AnnotatedStatement(Statement):

    pass
class alf_SuperInvocationStatement(Statement):

    pass
class alf_SwitchStatement(Statement):

    pass
class alf_LocalNameDeclarationStatement(Statement):

    def __init__(self, varName: str, multiplicityIndicator: bool, alf_LocalNameDeclarationStatement: "alf_QualifiedNameWithBinding" = None, alf_LocalNameDeclarationStatement168: "alf_SequenceElement" = None):
        self.varName = varName
        self.multiplicityIndicator = multiplicityIndicator
        self.alf_LocalNameDeclarationStatement = alf_LocalNameDeclarationStatement
        self.alf_LocalNameDeclarationStatement168 = alf_LocalNameDeclarationStatement168
        
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
    def alf_LocalNameDeclarationStatement168(self):
        return self.__alf_LocalNameDeclarationStatement168

    @alf_LocalNameDeclarationStatement168.setter
    def alf_LocalNameDeclarationStatement168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LocalNameDeclarationStatement__alf_LocalNameDeclarationStatement168", None)
        self.__alf_LocalNameDeclarationStatement168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceElement169"):
                opp_val = getattr(old_value, "alf_SequenceElement169", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceElement169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceElement169"):
                opp_val = getattr(value, "alf_SequenceElement169", None)
                setattr(value, "alf_SequenceElement169", self)

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
            if hasattr(old_value, "alf_QualifiedNameWithBinding166"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding166", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding166"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding166", None)
                setattr(value, "alf_QualifiedNameWithBinding166", self)

class alf_ReturnStatement(Statement):

    pass
class alf_AcceptStatement(Statement):

    pass
class alf_BlockStatement(Statement):

    pass
class alf_WhileStatement(Statement):

    pass
class alf_InstanceCreationInvocationStatement(Statement):

    pass
class alf_ForStatement(Statement):

    pass
class alf_DoStatement(Statement):

    pass
class alf_ThisInvocationStatement(Statement):

    pass
class alf_BreakStatement(Statement):

    pass
class alf_IfStatement(Statement):

    pass
class alf_InlineStatement(Statement):

    def __init__(self, langageName: str, body: str):
        self.langageName = langageName
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def langageName(self) -> str:
        return self.__langageName

    @langageName.setter
    def langageName(self, langageName: str):
        self.__langageName = langageName

class alf_DocumentedStatement:

    def __init__(self, comment: str, alf_DocumentedStatement: "alf_StatementSequence" = None, alf_DocumentedStatement157: "alf_Statement" = None, alf_DocumentedStatement204: "alf_NonEmptyStatementSequence" = None):
        self.comment = comment
        self.alf_DocumentedStatement = alf_DocumentedStatement
        self.alf_DocumentedStatement157 = alf_DocumentedStatement157
        self.alf_DocumentedStatement204 = alf_DocumentedStatement204
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def alf_DocumentedStatement157(self):
        return self.__alf_DocumentedStatement157

    @alf_DocumentedStatement157.setter
    def alf_DocumentedStatement157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement157", None)
        self.__alf_DocumentedStatement157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Statement158"):
                opp_val = getattr(old_value, "alf_Statement158", None)
                if opp_val == self:
                    setattr(old_value, "alf_Statement158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Statement158"):
                opp_val = getattr(value, "alf_Statement158", None)
                setattr(value, "alf_Statement158", self)

    @property
    def alf_DocumentedStatement204(self):
        return self.__alf_DocumentedStatement204

    @alf_DocumentedStatement204.setter
    def alf_DocumentedStatement204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_DocumentedStatement__alf_DocumentedStatement204", None)
        self.__alf_DocumentedStatement204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NonEmptyStatementSequence203"):
                opp_val = getattr(old_value, "alf_NonEmptyStatementSequence203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NonEmptyStatementSequence203"):
                opp_val = getattr(value, "alf_NonEmptyStatementSequence203", None)
                if opp_val is None:
                    setattr(value, "alf_NonEmptyStatementSequence203", set([self]))
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
            if hasattr(old_value, "alf_StatementSequence155"):
                opp_val = getattr(old_value, "alf_StatementSequence155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_StatementSequence155"):
                opp_val = getattr(value, "alf_StatementSequence155", None)
                if opp_val is None:
                    setattr(value, "alf_StatementSequence155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_StatementSequence:

    pass
class alf_SequenceElement:

    pass
class alf_InstanceCreationTupleElement:

    def __init__(self, role: str, alf_InstanceCreationTupleElement: "alf_InstanceCreationTuple" = None, alf_InstanceCreationTupleElement133: "alf_Expression" = None):
        self.role = role
        self.alf_InstanceCreationTupleElement = alf_InstanceCreationTupleElement
        self.alf_InstanceCreationTupleElement133 = alf_InstanceCreationTupleElement133
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def alf_InstanceCreationTupleElement(self):
        return self.__alf_InstanceCreationTupleElement

    @alf_InstanceCreationTupleElement.setter
    def alf_InstanceCreationTupleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_InstanceCreationTupleElement__alf_InstanceCreationTupleElement", None)
        self.__alf_InstanceCreationTupleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InstanceCreationTuple131"):
                opp_val = getattr(old_value, "alf_InstanceCreationTuple131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InstanceCreationTuple131"):
                opp_val = getattr(value, "alf_InstanceCreationTuple131", None)
                if opp_val is None:
                    setattr(value, "alf_InstanceCreationTuple131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_InstanceCreationTupleElement133(self):
        return self.__alf_InstanceCreationTupleElement133

    @alf_InstanceCreationTupleElement133.setter
    def alf_InstanceCreationTupleElement133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_InstanceCreationTupleElement__alf_InstanceCreationTupleElement133", None)
        self.__alf_InstanceCreationTupleElement133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression134"):
                opp_val = getattr(old_value, "alf_Expression134", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression134"):
                opp_val = getattr(value, "alf_Expression134", None)
                setattr(value, "alf_Expression134", self)

class alf_InstanceCreationTuple:

    pass
class alf_NonLiteralValueSpecification:

    pass
class SequenceExpansionExpression:

    pass
class alf_CollectOrIterateOperation(SequenceExpansionExpression):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class alf_IsUniqueOperation(SequenceExpansionExpression):

    pass
class alf_ForAllOrExistsOrOneOperation(SequenceExpansionExpression):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class alf_SelectOrRejectOperation(SequenceExpansionExpression):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class SuffixExpression:

    pass
class alf_SequenceReductionExpression(SuffixExpression):

    def __init__(self, isOrdered: bool, alf_SequenceReductionExpression: "alf_QualifiedNameWithBinding" = None, alf_SequenceReductionExpression102: "alf_SuffixExpression" = None):
        self.isOrdered = isOrdered
        self.alf_SequenceReductionExpression = alf_SequenceReductionExpression
        self.alf_SequenceReductionExpression102 = alf_SequenceReductionExpression102
        
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
            if hasattr(old_value, "alf_QualifiedNameWithBinding100"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding100", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding100"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding100", None)
                setattr(value, "alf_QualifiedNameWithBinding100", self)

    @property
    def alf_SequenceReductionExpression102(self):
        return self.__alf_SequenceReductionExpression102

    @alf_SequenceReductionExpression102.setter
    def alf_SequenceReductionExpression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceReductionExpression__alf_SequenceReductionExpression102", None)
        self.__alf_SequenceReductionExpression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression103"):
                opp_val = getattr(old_value, "alf_SuffixExpression103", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression103"):
                opp_val = getattr(value, "alf_SuffixExpression103", None)
                setattr(value, "alf_SuffixExpression103", self)

class alf_SequenceOperationExpression(SuffixExpression):

    pass
class alf_ClassExtentExpression(SuffixExpression):

    pass
class alf_SequenceExpansionExpression(SuffixExpression):

    def __init__(self, name: str, alf_SequenceExpansionExpression: "alf_Expression" = None, alf_SequenceExpansionExpression107: "alf_SuffixExpression" = None):
        self.name = name
        self.alf_SequenceExpansionExpression = alf_SequenceExpansionExpression
        self.alf_SequenceExpansionExpression107 = alf_SequenceExpansionExpression107
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_SequenceExpansionExpression(self):
        return self.__alf_SequenceExpansionExpression

    @alf_SequenceExpansionExpression.setter
    def alf_SequenceExpansionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceExpansionExpression__alf_SequenceExpansionExpression", None)
        self.__alf_SequenceExpansionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression105"):
                opp_val = getattr(old_value, "alf_Expression105", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression105"):
                opp_val = getattr(value, "alf_Expression105", None)
                setattr(value, "alf_Expression105", self)

    @property
    def alf_SequenceExpansionExpression107(self):
        return self.__alf_SequenceExpansionExpression107

    @alf_SequenceExpansionExpression107.setter
    def alf_SequenceExpansionExpression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceExpansionExpression__alf_SequenceExpansionExpression107", None)
        self.__alf_SequenceExpansionExpression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression108"):
                opp_val = getattr(old_value, "alf_SuffixExpression108", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression108"):
                opp_val = getattr(value, "alf_SuffixExpression108", None)
                setattr(value, "alf_SuffixExpression108", self)

class alf_OperationCallExpression(SuffixExpression):

    def __init__(self, operationName: str, alf_OperationCallExpression: "alf_Tuple" = None, alf_OperationCallExpression75: "alf_SuffixExpression" = None):
        self.operationName = operationName
        self.alf_OperationCallExpression = alf_OperationCallExpression
        self.alf_OperationCallExpression75 = alf_OperationCallExpression75
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def alf_OperationCallExpression75(self):
        return self.__alf_OperationCallExpression75

    @alf_OperationCallExpression75.setter
    def alf_OperationCallExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_OperationCallExpression__alf_OperationCallExpression75", None)
        self.__alf_OperationCallExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression76"):
                opp_val = getattr(old_value, "alf_SuffixExpression76", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression76"):
                opp_val = getattr(value, "alf_SuffixExpression76", None)
                setattr(value, "alf_SuffixExpression76", self)

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
            if hasattr(old_value, "alf_Tuple73"):
                opp_val = getattr(old_value, "alf_Tuple73", None)
                if opp_val == self:
                    setattr(old_value, "alf_Tuple73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Tuple73"):
                opp_val = getattr(value, "alf_Tuple73", None)
                setattr(value, "alf_Tuple73", self)

class alf_LinkOperationTupleElement:

    def __init__(self, role: str, alf_LinkOperationTupleElement: "alf_LinkOperationTuple" = None, alf_LinkOperationTupleElement86: "alf_Expression" = None, alf_LinkOperationTupleElement89: "alf_Expression" = None):
        self.role = role
        self.alf_LinkOperationTupleElement = alf_LinkOperationTupleElement
        self.alf_LinkOperationTupleElement86 = alf_LinkOperationTupleElement86
        self.alf_LinkOperationTupleElement89 = alf_LinkOperationTupleElement89
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def alf_LinkOperationTupleElement89(self):
        return self.__alf_LinkOperationTupleElement89

    @alf_LinkOperationTupleElement89.setter
    def alf_LinkOperationTupleElement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationTupleElement__alf_LinkOperationTupleElement89", None)
        self.__alf_LinkOperationTupleElement89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression90"):
                opp_val = getattr(old_value, "alf_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression90"):
                opp_val = getattr(value, "alf_Expression90", None)
                setattr(value, "alf_Expression90", self)

    @property
    def alf_LinkOperationTupleElement86(self):
        return self.__alf_LinkOperationTupleElement86

    @alf_LinkOperationTupleElement86.setter
    def alf_LinkOperationTupleElement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_LinkOperationTupleElement__alf_LinkOperationTupleElement86", None)
        self.__alf_LinkOperationTupleElement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_Expression87"):
                opp_val = getattr(old_value, "alf_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression87"):
                opp_val = getattr(value, "alf_Expression87", None)
                setattr(value, "alf_Expression87", self)

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
            if hasattr(old_value, "alf_LinkOperationTuple84"):
                opp_val = getattr(old_value, "alf_LinkOperationTuple84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LinkOperationTuple84"):
                opp_val = getattr(value, "alf_LinkOperationTuple84", None)
                if opp_val is None:
                    setattr(value, "alf_LinkOperationTuple84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_LinkOperationTuple:

    pass
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

class alf_PropertyCallExpression(SuffixExpression):

    def __init__(self, propertyName: str, alf_PropertyCallExpression: "alf_Expression" = None, alf_PropertyCallExpression80: "alf_SuffixExpression" = None):
        self.propertyName = propertyName
        self.alf_PropertyCallExpression = alf_PropertyCallExpression
        self.alf_PropertyCallExpression80 = alf_PropertyCallExpression80
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

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
            if hasattr(old_value, "alf_Expression78"):
                opp_val = getattr(old_value, "alf_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "alf_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Expression78"):
                opp_val = getattr(value, "alf_Expression78", None)
                setattr(value, "alf_Expression78", self)

    @property
    def alf_PropertyCallExpression80(self):
        return self.__alf_PropertyCallExpression80

    @alf_PropertyCallExpression80.setter
    def alf_PropertyCallExpression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_PropertyCallExpression__alf_PropertyCallExpression80", None)
        self.__alf_PropertyCallExpression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression81"):
                opp_val = getattr(old_value, "alf_SuffixExpression81", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression81"):
                opp_val = getattr(value, "alf_SuffixExpression81", None)
                setattr(value, "alf_SuffixExpression81", self)

class alf_ShiftExpression:

    def __init__(self, op: str, alf_ShiftExpression61: "alf_RelationalExpression" = None, alf_ShiftExpression63: set["alf_AdditiveExpression"] = None, alf_ShiftExpression: "alf_RelationalExpression" = None):
        self.op = op
        self.alf_ShiftExpression61 = alf_ShiftExpression61
        self.alf_ShiftExpression63 = alf_ShiftExpression63 if alf_ShiftExpression63 is not None else set()
        self.alf_ShiftExpression = alf_ShiftExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_ShiftExpression61(self):
        return self.__alf_ShiftExpression61

    @alf_ShiftExpression61.setter
    def alf_ShiftExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpression__alf_ShiftExpression61", None)
        self.__alf_ShiftExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_RelationalExpression60"):
                opp_val = getattr(old_value, "alf_RelationalExpression60", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression60"):
                opp_val = getattr(value, "alf_RelationalExpression60", None)
                setattr(value, "alf_RelationalExpression60", self)

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
            if hasattr(old_value, "alf_RelationalExpression58"):
                opp_val = getattr(old_value, "alf_RelationalExpression58", None)
                if opp_val == self:
                    setattr(old_value, "alf_RelationalExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_RelationalExpression58"):
                opp_val = getattr(value, "alf_RelationalExpression58", None)
                setattr(value, "alf_RelationalExpression58", self)

    @property
    def alf_ShiftExpression63(self):
        return self.__alf_ShiftExpression63

    @alf_ShiftExpression63.setter
    def alf_ShiftExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ShiftExpression__alf_ShiftExpression63", None)
        self.__alf_ShiftExpression63 = value if value is not None else set()
        
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
                    

class alf_ValueSpecification:

    pass
class alf_PrimaryExpression:

    pass
class alf_UnaryExpression:

    def __init__(self, op: str, alf_UnaryExpression: "alf_MultiplicativeExpression" = None, alf_UnaryExpression69: "alf_PrimaryExpression" = None):
        self.op = op
        self.alf_UnaryExpression = alf_UnaryExpression
        self.alf_UnaryExpression69 = alf_UnaryExpression69
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "alf_MultiplicativeExpression67"):
                opp_val = getattr(old_value, "alf_MultiplicativeExpression67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_MultiplicativeExpression67"):
                opp_val = getattr(value, "alf_MultiplicativeExpression67", None)
                if opp_val is None:
                    setattr(value, "alf_MultiplicativeExpression67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_UnaryExpression69(self):
        return self.__alf_UnaryExpression69

    @alf_UnaryExpression69.setter
    def alf_UnaryExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnaryExpression__alf_UnaryExpression69", None)
        self.__alf_UnaryExpression69 = value
        
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

class alf_MultiplicativeExpression:

    def __init__(self, op: str, alf_MultiplicativeExpression: "alf_AdditiveExpression" = None, alf_MultiplicativeExpression67: set["alf_UnaryExpression"] = None):
        self.op = op
        self.alf_MultiplicativeExpression = alf_MultiplicativeExpression
        self.alf_MultiplicativeExpression67 = alf_MultiplicativeExpression67 if alf_MultiplicativeExpression67 is not None else set()
        
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
            if hasattr(old_value, "alf_AdditiveExpression65"):
                opp_val = getattr(old_value, "alf_AdditiveExpression65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AdditiveExpression65"):
                opp_val = getattr(value, "alf_AdditiveExpression65", None)
                if opp_val is None:
                    setattr(value, "alf_AdditiveExpression65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_MultiplicativeExpression67(self):
        return self.__alf_MultiplicativeExpression67

    @alf_MultiplicativeExpression67.setter
    def alf_MultiplicativeExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_MultiplicativeExpression__alf_MultiplicativeExpression67", None)
        self.__alf_MultiplicativeExpression67 = value if value is not None else set()
        
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

    def __init__(self, op: str, alf_AdditiveExpression: "alf_ShiftExpression" = None, alf_AdditiveExpression65: set["alf_MultiplicativeExpression"] = None):
        self.op = op
        self.alf_AdditiveExpression = alf_AdditiveExpression
        self.alf_AdditiveExpression65 = alf_AdditiveExpression65 if alf_AdditiveExpression65 is not None else set()
        
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
            if hasattr(old_value, "alf_ShiftExpression63"):
                opp_val = getattr(old_value, "alf_ShiftExpression63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression63"):
                opp_val = getattr(value, "alf_ShiftExpression63", None)
                if opp_val is None:
                    setattr(value, "alf_ShiftExpression63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_AdditiveExpression65(self):
        return self.__alf_AdditiveExpression65

    @alf_AdditiveExpression65.setter
    def alf_AdditiveExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AdditiveExpression__alf_AdditiveExpression65", None)
        self.__alf_AdditiveExpression65 = value if value is not None else set()
        
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
                    

class alf_ConditionalAndExpression:

    pass
class alf_RelationalExpression:

    def __init__(self, op: str, alf_RelationalExpression: "alf_ClassificationExpression" = None, alf_RelationalExpression60: "alf_ShiftExpression" = None, alf_RelationalExpression58: "alf_ShiftExpression" = None):
        self.op = op
        self.alf_RelationalExpression = alf_RelationalExpression
        self.alf_RelationalExpression60 = alf_RelationalExpression60
        self.alf_RelationalExpression58 = alf_RelationalExpression58
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "alf_ClassificationExpression53"):
                opp_val = getattr(old_value, "alf_ClassificationExpression53", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpression53"):
                opp_val = getattr(value, "alf_ClassificationExpression53", None)
                setattr(value, "alf_ClassificationExpression53", self)

    @property
    def alf_RelationalExpression58(self):
        return self.__alf_RelationalExpression58

    @alf_RelationalExpression58.setter
    def alf_RelationalExpression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpression__alf_RelationalExpression58", None)
        self.__alf_RelationalExpression58 = value
        
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
    def alf_RelationalExpression60(self):
        return self.__alf_RelationalExpression60

    @alf_RelationalExpression60.setter
    def alf_RelationalExpression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_RelationalExpression__alf_RelationalExpression60", None)
        self.__alf_RelationalExpression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ShiftExpression61"):
                opp_val = getattr(old_value, "alf_ShiftExpression61", None)
                if opp_val == self:
                    setattr(old_value, "alf_ShiftExpression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ShiftExpression61"):
                opp_val = getattr(value, "alf_ShiftExpression61", None)
                setattr(value, "alf_ShiftExpression61", self)

class alf_ClassificationExpression:

    def __init__(self, op: str, alf_ClassificationExpression: "alf_EqualityExpression" = None, alf_ClassificationExpression53: "alf_RelationalExpression" = None, alf_ClassificationExpression55: "alf_NameExpression" = None):
        self.op = op
        self.alf_ClassificationExpression = alf_ClassificationExpression
        self.alf_ClassificationExpression53 = alf_ClassificationExpression53
        self.alf_ClassificationExpression55 = alf_ClassificationExpression55
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_ClassificationExpression53(self):
        return self.__alf_ClassificationExpression53

    @alf_ClassificationExpression53.setter
    def alf_ClassificationExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpression__alf_ClassificationExpression53", None)
        self.__alf_ClassificationExpression53 = value
        
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

    @property
    def alf_ClassificationExpression55(self):
        return self.__alf_ClassificationExpression55

    @alf_ClassificationExpression55.setter
    def alf_ClassificationExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_ClassificationExpression__alf_ClassificationExpression55", None)
        self.__alf_ClassificationExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NameExpression56"):
                opp_val = getattr(old_value, "alf_NameExpression56", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameExpression56"):
                opp_val = getattr(value, "alf_NameExpression56", None)
                setattr(value, "alf_NameExpression56", self)

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
            if hasattr(old_value, "alf_EqualityExpression51"):
                opp_val = getattr(old_value, "alf_EqualityExpression51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_EqualityExpression51"):
                opp_val = getattr(value, "alf_EqualityExpression51", None)
                if opp_val is None:
                    setattr(value, "alf_EqualityExpression51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_EqualityExpression:

    def __init__(self, op: str, alf_EqualityExpression: "alf_AndExpression" = None, alf_EqualityExpression51: set["alf_ClassificationExpression"] = None):
        self.op = op
        self.alf_EqualityExpression = alf_EqualityExpression
        self.alf_EqualityExpression51 = alf_EqualityExpression51 if alf_EqualityExpression51 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "alf_AndExpression49"):
                opp_val = getattr(old_value, "alf_AndExpression49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_AndExpression49"):
                opp_val = getattr(value, "alf_AndExpression49", None)
                if opp_val is None:
                    setattr(value, "alf_AndExpression49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_EqualityExpression51(self):
        return self.__alf_EqualityExpression51

    @alf_EqualityExpression51.setter
    def alf_EqualityExpression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_EqualityExpression__alf_EqualityExpression51", None)
        self.__alf_EqualityExpression51 = value if value is not None else set()
        
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
                    

class alf_AndExpression:

    pass
class alf_ExclusiveOrExpression:

    pass
class alf_QualifiedNameWithBinding:

    def __init__(self, id: str, alf_QualifiedNameWithBinding23: "alf_TemplateBinding" = None, alf_QualifiedNameWithBinding27: "alf_QualifiedNameWithBinding" = None, alf_QualifiedNameWithBinding25: "alf_QualifiedNameWithBinding" = None, alf_QualifiedNameWithBinding: "alf_NamedTemplateBinding" = None, alf_QualifiedNameWithBinding92: "alf_SequenceOperationExpression" = None, alf_QualifiedNameWithBinding100: "alf_SequenceReductionExpression" = None, alf_QualifiedNameWithBinding122: "alf_SuperInvocationExpression" = None, alf_QualifiedNameWithBinding124: "alf_InstanceCreationExpression" = None, alf_QualifiedNameWithBinding166: "alf_LocalNameDeclarationStatement" = None, alf_QualifiedNameWithBinding229: "alf_LoopVariableDefinition" = None, alf_QualifiedNameWithBinding271: "alf_QualifiedNameList" = None):
        self.id = id
        self.alf_QualifiedNameWithBinding23 = alf_QualifiedNameWithBinding23
        self.alf_QualifiedNameWithBinding27 = alf_QualifiedNameWithBinding27
        self.alf_QualifiedNameWithBinding25 = alf_QualifiedNameWithBinding25
        self.alf_QualifiedNameWithBinding = alf_QualifiedNameWithBinding
        self.alf_QualifiedNameWithBinding92 = alf_QualifiedNameWithBinding92
        self.alf_QualifiedNameWithBinding100 = alf_QualifiedNameWithBinding100
        self.alf_QualifiedNameWithBinding122 = alf_QualifiedNameWithBinding122
        self.alf_QualifiedNameWithBinding124 = alf_QualifiedNameWithBinding124
        self.alf_QualifiedNameWithBinding166 = alf_QualifiedNameWithBinding166
        self.alf_QualifiedNameWithBinding229 = alf_QualifiedNameWithBinding229
        self.alf_QualifiedNameWithBinding271 = alf_QualifiedNameWithBinding271
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def alf_QualifiedNameWithBinding100(self):
        return self.__alf_QualifiedNameWithBinding100

    @alf_QualifiedNameWithBinding100.setter
    def alf_QualifiedNameWithBinding100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding100", None)
        self.__alf_QualifiedNameWithBinding100 = value
        
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
    def alf_QualifiedNameWithBinding122(self):
        return self.__alf_QualifiedNameWithBinding122

    @alf_QualifiedNameWithBinding122.setter
    def alf_QualifiedNameWithBinding122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding122", None)
        self.__alf_QualifiedNameWithBinding122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuperInvocationExpression121"):
                opp_val = getattr(old_value, "alf_SuperInvocationExpression121", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuperInvocationExpression121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuperInvocationExpression121"):
                opp_val = getattr(value, "alf_SuperInvocationExpression121", None)
                setattr(value, "alf_SuperInvocationExpression121", self)

    @property
    def alf_QualifiedNameWithBinding27(self):
        return self.__alf_QualifiedNameWithBinding27

    @alf_QualifiedNameWithBinding27.setter
    def alf_QualifiedNameWithBinding27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding27", None)
        self.__alf_QualifiedNameWithBinding27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding25"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding25", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding25"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding25", None)
                setattr(value, "alf_QualifiedNameWithBinding25", self)

    @property
    def alf_QualifiedNameWithBinding124(self):
        return self.__alf_QualifiedNameWithBinding124

    @alf_QualifiedNameWithBinding124.setter
    def alf_QualifiedNameWithBinding124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding124", None)
        self.__alf_QualifiedNameWithBinding124 = value
        
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

    @property
    def alf_QualifiedNameWithBinding229(self):
        return self.__alf_QualifiedNameWithBinding229

    @alf_QualifiedNameWithBinding229.setter
    def alf_QualifiedNameWithBinding229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding229", None)
        self.__alf_QualifiedNameWithBinding229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_LoopVariableDefinition228"):
                opp_val = getattr(old_value, "alf_LoopVariableDefinition228", None)
                if opp_val == self:
                    setattr(old_value, "alf_LoopVariableDefinition228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_LoopVariableDefinition228"):
                opp_val = getattr(value, "alf_LoopVariableDefinition228", None)
                setattr(value, "alf_LoopVariableDefinition228", self)

    @property
    def alf_QualifiedNameWithBinding23(self):
        return self.__alf_QualifiedNameWithBinding23

    @alf_QualifiedNameWithBinding23.setter
    def alf_QualifiedNameWithBinding23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding23", None)
        self.__alf_QualifiedNameWithBinding23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_TemplateBinding24"):
                opp_val = getattr(old_value, "alf_TemplateBinding24", None)
                if opp_val == self:
                    setattr(old_value, "alf_TemplateBinding24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding24"):
                opp_val = getattr(value, "alf_TemplateBinding24", None)
                setattr(value, "alf_TemplateBinding24", self)

    @property
    def alf_QualifiedNameWithBinding271(self):
        return self.__alf_QualifiedNameWithBinding271

    @alf_QualifiedNameWithBinding271.setter
    def alf_QualifiedNameWithBinding271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding271", None)
        self.__alf_QualifiedNameWithBinding271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameList270"):
                opp_val = getattr(old_value, "alf_QualifiedNameList270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameList270"):
                opp_val = getattr(value, "alf_QualifiedNameList270", None)
                if opp_val is None:
                    setattr(value, "alf_QualifiedNameList270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alf_QualifiedNameWithBinding92(self):
        return self.__alf_QualifiedNameWithBinding92

    @alf_QualifiedNameWithBinding92.setter
    def alf_QualifiedNameWithBinding92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding92", None)
        self.__alf_QualifiedNameWithBinding92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceOperationExpression"):
                opp_val = getattr(old_value, "alf_SequenceOperationExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceOperationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceOperationExpression"):
                opp_val = getattr(value, "alf_SequenceOperationExpression", None)
                setattr(value, "alf_SequenceOperationExpression", self)

    @property
    def alf_QualifiedNameWithBinding166(self):
        return self.__alf_QualifiedNameWithBinding166

    @alf_QualifiedNameWithBinding166.setter
    def alf_QualifiedNameWithBinding166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding166", None)
        self.__alf_QualifiedNameWithBinding166 = value
        
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
    def alf_QualifiedNameWithBinding(self):
        return self.__alf_QualifiedNameWithBinding

    @alf_QualifiedNameWithBinding.setter
    def alf_QualifiedNameWithBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding", None)
        self.__alf_QualifiedNameWithBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_NamedTemplateBinding21"):
                opp_val = getattr(old_value, "alf_NamedTemplateBinding21", None)
                if opp_val == self:
                    setattr(old_value, "alf_NamedTemplateBinding21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NamedTemplateBinding21"):
                opp_val = getattr(value, "alf_NamedTemplateBinding21", None)
                setattr(value, "alf_NamedTemplateBinding21", self)

    @property
    def alf_QualifiedNameWithBinding25(self):
        return self.__alf_QualifiedNameWithBinding25

    @alf_QualifiedNameWithBinding25.setter
    def alf_QualifiedNameWithBinding25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_QualifiedNameWithBinding__alf_QualifiedNameWithBinding25", None)
        self.__alf_QualifiedNameWithBinding25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding27"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding27", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding27"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding27", None)
                setattr(value, "alf_QualifiedNameWithBinding27", self)

class alf_InclusiveOrExpression:

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

    def __init__(self, formal: str, alf_NamedTemplateBinding: "alf_TemplateBinding" = None, alf_NamedTemplateBinding21: "alf_QualifiedNameWithBinding" = None):
        self.formal = formal
        self.alf_NamedTemplateBinding = alf_NamedTemplateBinding
        self.alf_NamedTemplateBinding21 = alf_NamedTemplateBinding21
        
    @property
    def formal(self) -> str:
        return self.__formal

    @formal.setter
    def formal(self, formal: str):
        self.__formal = formal

    @property
    def alf_NamedTemplateBinding21(self):
        return self.__alf_NamedTemplateBinding21

    @alf_NamedTemplateBinding21.setter
    def alf_NamedTemplateBinding21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NamedTemplateBinding__alf_NamedTemplateBinding21", None)
        self.__alf_NamedTemplateBinding21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_QualifiedNameWithBinding"):
                opp_val = getattr(old_value, "alf_QualifiedNameWithBinding", None)
                if opp_val == self:
                    setattr(old_value, "alf_QualifiedNameWithBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNameWithBinding"):
                opp_val = getattr(value, "alf_QualifiedNameWithBinding", None)
                setattr(value, "alf_QualifiedNameWithBinding", self)

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
            if hasattr(old_value, "alf_TemplateBinding19"):
                opp_val = getattr(old_value, "alf_TemplateBinding19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_TemplateBinding19"):
                opp_val = getattr(value, "alf_TemplateBinding19", None)
                if opp_val is None:
                    setattr(value, "alf_TemplateBinding19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_TemplateBinding:

    pass
class alf_UnqualifiedName:

    def __init__(self, name: str, alf_UnqualifiedName: "alf_QualifiedNamePath" = None, alf_UnqualifiedName17: "alf_TemplateBinding" = None):
        self.name = name
        self.alf_UnqualifiedName = alf_UnqualifiedName
        self.alf_UnqualifiedName17 = alf_UnqualifiedName17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alf_UnqualifiedName17(self):
        return self.__alf_UnqualifiedName17

    @alf_UnqualifiedName17.setter
    def alf_UnqualifiedName17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_UnqualifiedName__alf_UnqualifiedName17", None)
        self.__alf_UnqualifiedName17 = value
        
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
            if hasattr(old_value, "alf_QualifiedNamePath15"):
                opp_val = getattr(old_value, "alf_QualifiedNamePath15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_QualifiedNamePath15"):
                opp_val = getattr(value, "alf_QualifiedNamePath15", None)
                if opp_val is None:
                    setattr(value, "alf_QualifiedNamePath15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_SuffixExpression:

    pass
class alf_SequenceConstructionOrAccessCompletion:

    def __init__(self, multiplicityIndicator: bool, alf_SequenceConstructionOrAccessCompletion: "alf_NameExpression" = None, alf_SequenceConstructionOrAccessCompletion136: "alf_AccessCompletion" = None, alf_SequenceConstructionOrAccessCompletion138: "alf_PartialSequenceConstructionCompletion" = None, alf_SequenceConstructionOrAccessCompletion140: "alf_SequenceConstructionExpression" = None):
        self.multiplicityIndicator = multiplicityIndicator
        self.alf_SequenceConstructionOrAccessCompletion = alf_SequenceConstructionOrAccessCompletion
        self.alf_SequenceConstructionOrAccessCompletion136 = alf_SequenceConstructionOrAccessCompletion136
        self.alf_SequenceConstructionOrAccessCompletion138 = alf_SequenceConstructionOrAccessCompletion138
        self.alf_SequenceConstructionOrAccessCompletion140 = alf_SequenceConstructionOrAccessCompletion140
        
    @property
    def multiplicityIndicator(self) -> bool:
        return self.__multiplicityIndicator

    @multiplicityIndicator.setter
    def multiplicityIndicator(self, multiplicityIndicator: bool):
        self.__multiplicityIndicator = multiplicityIndicator

    @property
    def alf_SequenceConstructionOrAccessCompletion138(self):
        return self.__alf_SequenceConstructionOrAccessCompletion138

    @alf_SequenceConstructionOrAccessCompletion138.setter
    def alf_SequenceConstructionOrAccessCompletion138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion138", None)
        self.__alf_SequenceConstructionOrAccessCompletion138 = value
        
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
            if hasattr(old_value, "alf_NameExpression11"):
                opp_val = getattr(old_value, "alf_NameExpression11", None)
                if opp_val == self:
                    setattr(old_value, "alf_NameExpression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_NameExpression11"):
                opp_val = getattr(value, "alf_NameExpression11", None)
                setattr(value, "alf_NameExpression11", self)

    @property
    def alf_SequenceConstructionOrAccessCompletion136(self):
        return self.__alf_SequenceConstructionOrAccessCompletion136

    @alf_SequenceConstructionOrAccessCompletion136.setter
    def alf_SequenceConstructionOrAccessCompletion136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion136", None)
        self.__alf_SequenceConstructionOrAccessCompletion136 = value
        
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
    def alf_SequenceConstructionOrAccessCompletion140(self):
        return self.__alf_SequenceConstructionOrAccessCompletion140

    @alf_SequenceConstructionOrAccessCompletion140.setter
    def alf_SequenceConstructionOrAccessCompletion140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_SequenceConstructionOrAccessCompletion__alf_SequenceConstructionOrAccessCompletion140", None)
        self.__alf_SequenceConstructionOrAccessCompletion140 = value
        
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

class alf_Tuple:

    pass
class alf_QualifiedNamePath:

    pass
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
class alf_NUMBER_LITERAL(LITERAL):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class alf_STRING_LITERAL(LITERAL):

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

class ValueSpecification:

    pass
class alf_NameExpression(ValueSpecification, NonLiteralValueSpecification):

    def __init__(self, prefixOp: str, id: str, postfixOp: str, alf_NameExpression: "alf_QualifiedNamePath" = None, alf_NameExpression9: "alf_Tuple" = None, alf_NameExpression11: "alf_SequenceConstructionOrAccessCompletion" = None, alf_NameExpression13: "alf_SuffixExpression" = None, alf_NameExpression56: "alf_ClassificationExpression" = None, alf_NameExpression273: "alf_InvocationOrAssignementOrDeclarationStatement" = None):
        self.prefixOp = prefixOp
        self.id = id
        self.postfixOp = postfixOp
        self.alf_NameExpression = alf_NameExpression
        self.alf_NameExpression9 = alf_NameExpression9
        self.alf_NameExpression11 = alf_NameExpression11
        self.alf_NameExpression13 = alf_NameExpression13
        self.alf_NameExpression56 = alf_NameExpression56
        self.alf_NameExpression273 = alf_NameExpression273
        
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
    def alf_NameExpression11(self):
        return self.__alf_NameExpression11

    @alf_NameExpression11.setter
    def alf_NameExpression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression11", None)
        self.__alf_NameExpression11 = value
        
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
    def alf_NameExpression56(self):
        return self.__alf_NameExpression56

    @alf_NameExpression56.setter
    def alf_NameExpression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression56", None)
        self.__alf_NameExpression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ClassificationExpression55"):
                opp_val = getattr(old_value, "alf_ClassificationExpression55", None)
                if opp_val == self:
                    setattr(old_value, "alf_ClassificationExpression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ClassificationExpression55"):
                opp_val = getattr(value, "alf_ClassificationExpression55", None)
                setattr(value, "alf_ClassificationExpression55", self)

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

    @property
    def alf_NameExpression9(self):
        return self.__alf_NameExpression9

    @alf_NameExpression9.setter
    def alf_NameExpression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression9", None)
        self.__alf_NameExpression9 = value
        
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
    def alf_NameExpression273(self):
        return self.__alf_NameExpression273

    @alf_NameExpression273.setter
    def alf_NameExpression273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression273", None)
        self.__alf_NameExpression273 = value
        
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
    def alf_NameExpression13(self):
        return self.__alf_NameExpression13

    @alf_NameExpression13.setter
    def alf_NameExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_NameExpression__alf_NameExpression13", None)
        self.__alf_NameExpression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SuffixExpression"):
                opp_val = getattr(old_value, "alf_SuffixExpression", None)
                if opp_val == self:
                    setattr(old_value, "alf_SuffixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SuffixExpression"):
                opp_val = getattr(value, "alf_SuffixExpression", None)
                setattr(value, "alf_SuffixExpression", self)

class alf_InstanceCreationExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_NullExpression(ValueSpecification):

    pass
class alf_ParenthesizedExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_ThisExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_SuperInvocationExpression(ValueSpecification, NonLiteralValueSpecification):

    pass
class alf_LITERAL(ValueSpecification):

    pass
class alf_Block:

    pass
class alf_Statement:

    pass
class alf_AssignmentCompletion:

    def __init__(self, op: str, alf_AssignmentCompletion: "alf_Test" = None, alf_AssignmentCompletion278: "alf_InvocationOrAssignementOrDeclarationStatement" = None, alf_AssignmentCompletion285: "alf_ThisInvocationStatement" = None, alf_AssignmentCompletion290: "alf_VariableDeclarationCompletion" = None, alf_AssignmentCompletion292: "alf_SequenceElement" = None):
        self.op = op
        self.alf_AssignmentCompletion = alf_AssignmentCompletion
        self.alf_AssignmentCompletion278 = alf_AssignmentCompletion278
        self.alf_AssignmentCompletion285 = alf_AssignmentCompletion285
        self.alf_AssignmentCompletion290 = alf_AssignmentCompletion290
        self.alf_AssignmentCompletion292 = alf_AssignmentCompletion292
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def alf_AssignmentCompletion278(self):
        return self.__alf_AssignmentCompletion278

    @alf_AssignmentCompletion278.setter
    def alf_AssignmentCompletion278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion278", None)
        self.__alf_AssignmentCompletion278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement277"):
                opp_val = getattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement277", None)
                if opp_val == self:
                    setattr(old_value, "alf_InvocationOrAssignementOrDeclarationStatement277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_InvocationOrAssignementOrDeclarationStatement277"):
                opp_val = getattr(value, "alf_InvocationOrAssignementOrDeclarationStatement277", None)
                setattr(value, "alf_InvocationOrAssignementOrDeclarationStatement277", self)

    @property
    def alf_AssignmentCompletion290(self):
        return self.__alf_AssignmentCompletion290

    @alf_AssignmentCompletion290.setter
    def alf_AssignmentCompletion290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion290", None)
        self.__alf_AssignmentCompletion290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_VariableDeclarationCompletion289"):
                opp_val = getattr(old_value, "alf_VariableDeclarationCompletion289", None)
                if opp_val == self:
                    setattr(old_value, "alf_VariableDeclarationCompletion289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_VariableDeclarationCompletion289"):
                opp_val = getattr(value, "alf_VariableDeclarationCompletion289", None)
                setattr(value, "alf_VariableDeclarationCompletion289", self)

    @property
    def alf_AssignmentCompletion285(self):
        return self.__alf_AssignmentCompletion285

    @alf_AssignmentCompletion285.setter
    def alf_AssignmentCompletion285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion285", None)
        self.__alf_AssignmentCompletion285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_ThisInvocationStatement284"):
                opp_val = getattr(old_value, "alf_ThisInvocationStatement284", None)
                if opp_val == self:
                    setattr(old_value, "alf_ThisInvocationStatement284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_ThisInvocationStatement284"):
                opp_val = getattr(value, "alf_ThisInvocationStatement284", None)
                setattr(value, "alf_ThisInvocationStatement284", self)

    @property
    def alf_AssignmentCompletion292(self):
        return self.__alf_AssignmentCompletion292

    @alf_AssignmentCompletion292.setter
    def alf_AssignmentCompletion292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alf_AssignmentCompletion__alf_AssignmentCompletion292", None)
        self.__alf_AssignmentCompletion292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alf_SequenceElement293"):
                opp_val = getattr(old_value, "alf_SequenceElement293", None)
                if opp_val == self:
                    setattr(old_value, "alf_SequenceElement293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_SequenceElement293"):
                opp_val = getattr(value, "alf_SequenceElement293", None)
                setattr(value, "alf_SequenceElement293", self)

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
            if hasattr(old_value, "alf_Test2"):
                opp_val = getattr(old_value, "alf_Test2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alf_Test2"):
                opp_val = getattr(value, "alf_Test2", None)
                if opp_val is None:
                    setattr(value, "alf_Test2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class alf_Expression(SequenceElement):

    pass
class alf_Test:

    pass
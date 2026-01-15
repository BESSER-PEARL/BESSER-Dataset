from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class InvokerRight(Enum):
    CURRENT_USER = "CURRENT_USER"
    DEFINER = "DEFINER"


############################################
# Definition of Classes
############################################

class plSql_NameDeclaration:

    def __init__(self, name: str, plSql_NameDeclaration: "plSql_Name" = None):
        self.name = name
        self.plSql_NameDeclaration = plSql_NameDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def plSql_NameDeclaration(self):
        return self.__plSql_NameDeclaration

    @plSql_NameDeclaration.setter
    def plSql_NameDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_NameDeclaration__plSql_NameDeclaration", None)
        self.__plSql_NameDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Name127"):
                opp_val = getattr(old_value, "plSql_Name127", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Name127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Name127"):
                opp_val = getattr(value, "plSql_Name127", None)
                setattr(value, "plSql_Name127", self)

class plSql_Name:

    pass
class plSql_QualifiedName:

    pass
class LoopStatement:

    pass
class plSql_ForLoopStatement(LoopStatement):

    pass
class plSql_WhileLoopStatement(LoopStatement):

    pass
class plSql_BasicLoopStatement(LoopStatement):

    pass
class plSql_IfStatementElseBranch:

    pass
class plSql_IfStatementElsifBranch:

    pass
class FetchStatementIntoClause:

    pass
class plSql_FetchStatementBulkIntoClause(FetchStatementIntoClause):

    pass
class plSql_FetchStatementSingleIntoClause(FetchStatementIntoClause):

    pass
class plSql_FetchStatementIntoClause:

    pass
class plSql_Label:

    def __init__(self, name: str, plSql_Label: "plSql_Statement" = None, plSql_Label90: "plSql_GotoStatement" = None):
        self.name = name
        self.plSql_Label = plSql_Label
        self.plSql_Label90 = plSql_Label90
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def plSql_Label90(self):
        return self.__plSql_Label90

    @plSql_Label90.setter
    def plSql_Label90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Label__plSql_Label90", None)
        self.__plSql_Label90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_GotoStatement"):
                opp_val = getattr(old_value, "plSql_GotoStatement", None)
                if opp_val == self:
                    setattr(old_value, "plSql_GotoStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_GotoStatement"):
                opp_val = getattr(value, "plSql_GotoStatement", None)
                setattr(value, "plSql_GotoStatement", self)

    @property
    def plSql_Label(self):
        return self.__plSql_Label

    @plSql_Label.setter
    def plSql_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Label__plSql_Label", None)
        self.__plSql_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Statement47"):
                opp_val = getattr(old_value, "plSql_Statement47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Statement47"):
                opp_val = getattr(value, "plSql_Statement47", None)
                if opp_val is None:
                    setattr(value, "plSql_Statement47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class plSql_CaseStatementElseBranch:

    pass
class plSql_CaseStatementWhenBranch:

    pass
class AssignmentTarget:

    pass
class plSql_VariableAssignmentTarget(AssignmentTarget):

    pass
class plSql_AssignmentTarget:

    pass
class Statement:

    pass
class plSql_ExitStatement(Statement):

    def __init__(self, labelName: str, plSql_ExitStatement: "plSql_Expression" = None):
        self.labelName = labelName
        self.plSql_ExitStatement = plSql_ExitStatement
        
    @property
    def labelName(self) -> str:
        return self.__labelName

    @labelName.setter
    def labelName(self, labelName: str):
        self.__labelName = labelName

    @property
    def plSql_ExitStatement(self):
        return self.__plSql_ExitStatement

    @plSql_ExitStatement.setter
    def plSql_ExitStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ExitStatement__plSql_ExitStatement", None)
        self.__plSql_ExitStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Expression79"):
                opp_val = getattr(old_value, "plSql_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Expression79"):
                opp_val = getattr(value, "plSql_Expression79", None)
                setattr(value, "plSql_Expression79", self)

class plSql_CloseStatement(Statement):

    pass
class plSql_RaiseStatement(Statement):

    def __init__(self, exceptionName: str):
        self.exceptionName = exceptionName
        
    @property
    def exceptionName(self) -> str:
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName

class plSql_FetchStatement(Statement):

    pass
class plSql_BlockStatement(Statement):

    pass
class plSql_GotoStatement(Statement):

    pass
class plSql_ContinueStatement(Statement):

    def __init__(self, labelName: str, plSql_ContinueStatement: "plSql_Expression" = None):
        self.labelName = labelName
        self.plSql_ContinueStatement = plSql_ContinueStatement
        
    @property
    def labelName(self) -> str:
        return self.__labelName

    @labelName.setter
    def labelName(self, labelName: str):
        self.__labelName = labelName

    @property
    def plSql_ContinueStatement(self):
        return self.__plSql_ContinueStatement

    @plSql_ContinueStatement.setter
    def plSql_ContinueStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ContinueStatement__plSql_ContinueStatement", None)
        self.__plSql_ContinueStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Expression77"):
                opp_val = getattr(old_value, "plSql_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Expression77"):
                opp_val = getattr(value, "plSql_Expression77", None)
                setattr(value, "plSql_Expression77", self)

class plSql_LoopStatement(Statement):

    def __init__(self, endLabel: str, plSql_LoopStatement: set["plSql_Statement"] = None):
        self.endLabel = endLabel
        self.plSql_LoopStatement = plSql_LoopStatement if plSql_LoopStatement is not None else set()
        
    @property
    def endLabel(self) -> str:
        return self.__endLabel

    @endLabel.setter
    def endLabel(self, endLabel: str):
        self.__endLabel = endLabel

    @property
    def plSql_LoopStatement(self):
        return self.__plSql_LoopStatement

    @plSql_LoopStatement.setter
    def plSql_LoopStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_LoopStatement__plSql_LoopStatement", None)
        self.__plSql_LoopStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plSql_Statement110"):
                    opp_val = getattr(item, "plSql_Statement110", None)
                    
                    if opp_val == self:
                        setattr(item, "plSql_Statement110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plSql_Statement110"):
                    opp_val = getattr(item, "plSql_Statement110", None)
                    
                    setattr(item, "plSql_Statement110", self)
                    

class plSql_IfStatement(Statement):

    pass
class plSql_ReturnStatement(Statement):

    pass
class plSql_NullStatement(Statement):

    pass
class plSql_CaseStatement(Statement):

    def __init__(self, endLabel: str, plSql_CaseStatement: "plSql_Expression" = None, plSql_CaseStatement62: set["plSql_CaseStatementWhenBranch"] = None, plSql_CaseStatement64: "plSql_CaseStatementElseBranch" = None):
        self.endLabel = endLabel
        self.plSql_CaseStatement = plSql_CaseStatement
        self.plSql_CaseStatement62 = plSql_CaseStatement62 if plSql_CaseStatement62 is not None else set()
        self.plSql_CaseStatement64 = plSql_CaseStatement64
        
    @property
    def endLabel(self) -> str:
        return self.__endLabel

    @endLabel.setter
    def endLabel(self, endLabel: str):
        self.__endLabel = endLabel

    @property
    def plSql_CaseStatement(self):
        return self.__plSql_CaseStatement

    @plSql_CaseStatement.setter
    def plSql_CaseStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_CaseStatement__plSql_CaseStatement", None)
        self.__plSql_CaseStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Expression60"):
                opp_val = getattr(old_value, "plSql_Expression60", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Expression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Expression60"):
                opp_val = getattr(value, "plSql_Expression60", None)
                setattr(value, "plSql_Expression60", self)

    @property
    def plSql_CaseStatement62(self):
        return self.__plSql_CaseStatement62

    @plSql_CaseStatement62.setter
    def plSql_CaseStatement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_CaseStatement__plSql_CaseStatement62", None)
        self.__plSql_CaseStatement62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plSql_CaseStatementWhenBranch"):
                    opp_val = getattr(item, "plSql_CaseStatementWhenBranch", None)
                    
                    if opp_val == self:
                        setattr(item, "plSql_CaseStatementWhenBranch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plSql_CaseStatementWhenBranch"):
                    opp_val = getattr(item, "plSql_CaseStatementWhenBranch", None)
                    
                    setattr(item, "plSql_CaseStatementWhenBranch", self)
                    

    @property
    def plSql_CaseStatement64(self):
        return self.__plSql_CaseStatement64

    @plSql_CaseStatement64.setter
    def plSql_CaseStatement64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_CaseStatement__plSql_CaseStatement64", None)
        self.__plSql_CaseStatement64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_CaseStatementElseBranch"):
                opp_val = getattr(old_value, "plSql_CaseStatementElseBranch", None)
                if opp_val == self:
                    setattr(old_value, "plSql_CaseStatementElseBranch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_CaseStatementElseBranch"):
                opp_val = getattr(value, "plSql_CaseStatementElseBranch", None)
                setattr(value, "plSql_CaseStatementElseBranch", self)

class plSql_AssignmentStatement(Statement):

    pass
class FunctionContent:

    pass
class plSql_FunctionImplementation(FunctionContent):

    pass
class plSql_VariableRef:

    def __init__(self, isHostRef: bool, plSql_VariableRef: "plSql_VariableRefExpression" = None, plSql_VariableRef53: "plSql_VariableAssignmentTarget" = None, plSql_VariableRef81: "plSql_FetchStatement" = None, plSql_VariableRef75: "plSql_CloseStatement" = None, plSql_VariableRef86: "plSql_FetchStatementIntoClause" = None, plSql_VariableRef123: "plSql_QualifiedName" = None):
        self.isHostRef = isHostRef
        self.plSql_VariableRef = plSql_VariableRef
        self.plSql_VariableRef53 = plSql_VariableRef53
        self.plSql_VariableRef81 = plSql_VariableRef81
        self.plSql_VariableRef75 = plSql_VariableRef75
        self.plSql_VariableRef86 = plSql_VariableRef86
        self.plSql_VariableRef123 = plSql_VariableRef123
        
    @property
    def isHostRef(self) -> bool:
        return self.__isHostRef

    @isHostRef.setter
    def isHostRef(self, isHostRef: bool):
        self.__isHostRef = isHostRef

    @property
    def plSql_VariableRef81(self):
        return self.__plSql_VariableRef81

    @plSql_VariableRef81.setter
    def plSql_VariableRef81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef81", None)
        self.__plSql_VariableRef81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_FetchStatement"):
                opp_val = getattr(old_value, "plSql_FetchStatement", None)
                if opp_val == self:
                    setattr(old_value, "plSql_FetchStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_FetchStatement"):
                opp_val = getattr(value, "plSql_FetchStatement", None)
                setattr(value, "plSql_FetchStatement", self)

    @property
    def plSql_VariableRef(self):
        return self.__plSql_VariableRef

    @plSql_VariableRef.setter
    def plSql_VariableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef", None)
        self.__plSql_VariableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_VariableRefExpression"):
                opp_val = getattr(old_value, "plSql_VariableRefExpression", None)
                if opp_val == self:
                    setattr(old_value, "plSql_VariableRefExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_VariableRefExpression"):
                opp_val = getattr(value, "plSql_VariableRefExpression", None)
                setattr(value, "plSql_VariableRefExpression", self)

    @property
    def plSql_VariableRef53(self):
        return self.__plSql_VariableRef53

    @plSql_VariableRef53.setter
    def plSql_VariableRef53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef53", None)
        self.__plSql_VariableRef53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_VariableAssignmentTarget"):
                opp_val = getattr(old_value, "plSql_VariableAssignmentTarget", None)
                if opp_val == self:
                    setattr(old_value, "plSql_VariableAssignmentTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_VariableAssignmentTarget"):
                opp_val = getattr(value, "plSql_VariableAssignmentTarget", None)
                setattr(value, "plSql_VariableAssignmentTarget", self)

    @property
    def plSql_VariableRef123(self):
        return self.__plSql_VariableRef123

    @plSql_VariableRef123.setter
    def plSql_VariableRef123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef123", None)
        self.__plSql_VariableRef123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_QualifiedName"):
                opp_val = getattr(old_value, "plSql_QualifiedName", None)
                if opp_val == self:
                    setattr(old_value, "plSql_QualifiedName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_QualifiedName"):
                opp_val = getattr(value, "plSql_QualifiedName", None)
                setattr(value, "plSql_QualifiedName", self)

    @property
    def plSql_VariableRef86(self):
        return self.__plSql_VariableRef86

    @plSql_VariableRef86.setter
    def plSql_VariableRef86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef86", None)
        self.__plSql_VariableRef86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_FetchStatementIntoClause85"):
                opp_val = getattr(old_value, "plSql_FetchStatementIntoClause85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_FetchStatementIntoClause85"):
                opp_val = getattr(value, "plSql_FetchStatementIntoClause85", None)
                if opp_val is None:
                    setattr(value, "plSql_FetchStatementIntoClause85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def plSql_VariableRef75(self):
        return self.__plSql_VariableRef75

    @plSql_VariableRef75.setter
    def plSql_VariableRef75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableRef__plSql_VariableRef75", None)
        self.__plSql_VariableRef75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_CloseStatement"):
                opp_val = getattr(old_value, "plSql_CloseStatement", None)
                if opp_val == self:
                    setattr(old_value, "plSql_CloseStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_CloseStatement"):
                opp_val = getattr(value, "plSql_CloseStatement", None)
                setattr(value, "plSql_CloseStatement", self)

class Expression:

    pass
class plSql_VariableRefExpression(Expression):

    pass
class plSql_NullLiteralExpression(Expression):

    pass
class plSql_StringLiteralExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class plSql_BooleanLiteralExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class plSql_IntLiteralExpression(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class plSql_VariableValue:

    pass
class ItemDeclaration:

    pass
class plSql_Statement:

    pass
class plSql_StatementBody:

    def __init__(self, endName: str, plSql_StatementBody: "plSql_ProcedureImplementation" = None, plSql_StatementBody37: set["plSql_Statement"] = None, plSql_StatementBody35: "plSql_FunctionImplementation" = None, plSql_StatementBody58: "plSql_BlockStatement" = None):
        self.endName = endName
        self.plSql_StatementBody = plSql_StatementBody
        self.plSql_StatementBody37 = plSql_StatementBody37 if plSql_StatementBody37 is not None else set()
        self.plSql_StatementBody35 = plSql_StatementBody35
        self.plSql_StatementBody58 = plSql_StatementBody58
        
    @property
    def endName(self) -> str:
        return self.__endName

    @endName.setter
    def endName(self, endName: str):
        self.__endName = endName

    @property
    def plSql_StatementBody37(self):
        return self.__plSql_StatementBody37

    @plSql_StatementBody37.setter
    def plSql_StatementBody37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_StatementBody__plSql_StatementBody37", None)
        self.__plSql_StatementBody37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plSql_Statement"):
                    opp_val = getattr(item, "plSql_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "plSql_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plSql_Statement"):
                    opp_val = getattr(item, "plSql_Statement", None)
                    
                    setattr(item, "plSql_Statement", self)
                    

    @property
    def plSql_StatementBody58(self):
        return self.__plSql_StatementBody58

    @plSql_StatementBody58.setter
    def plSql_StatementBody58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_StatementBody__plSql_StatementBody58", None)
        self.__plSql_StatementBody58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_BlockStatement57"):
                opp_val = getattr(old_value, "plSql_BlockStatement57", None)
                if opp_val == self:
                    setattr(old_value, "plSql_BlockStatement57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_BlockStatement57"):
                opp_val = getattr(value, "plSql_BlockStatement57", None)
                setattr(value, "plSql_BlockStatement57", self)

    @property
    def plSql_StatementBody(self):
        return self.__plSql_StatementBody

    @plSql_StatementBody.setter
    def plSql_StatementBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_StatementBody__plSql_StatementBody", None)
        self.__plSql_StatementBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ProcedureImplementation30"):
                opp_val = getattr(old_value, "plSql_ProcedureImplementation30", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ProcedureImplementation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ProcedureImplementation30"):
                opp_val = getattr(value, "plSql_ProcedureImplementation30", None)
                setattr(value, "plSql_ProcedureImplementation30", self)

    @property
    def plSql_StatementBody35(self):
        return self.__plSql_StatementBody35

    @plSql_StatementBody35.setter
    def plSql_StatementBody35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_StatementBody__plSql_StatementBody35", None)
        self.__plSql_StatementBody35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_FunctionImplementation34"):
                opp_val = getattr(old_value, "plSql_FunctionImplementation34", None)
                if opp_val == self:
                    setattr(old_value, "plSql_FunctionImplementation34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_FunctionImplementation34"):
                opp_val = getattr(value, "plSql_FunctionImplementation34", None)
                setattr(value, "plSql_FunctionImplementation34", self)

class plSql_DeclareSection:

    pass
class ProcedureContent:

    pass
class plSql_ExternalProcedureDeclaration(ProcedureContent):

    pass
class plSql_ProcedureImplementation(ProcedureContent):

    pass
class Pragma:

    pass
class plSql_PragmaTimestamp(Pragma):

    def __init__(self, timestamp: str):
        self.timestamp = timestamp
        
    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

class plSql_PragmaRestrictReferences(Pragma):

    def __init__(self, restrictions: str):
        self.restrictions = restrictions
        
    @property
    def restrictions(self) -> str:
        return self.__restrictions

    @restrictions.setter
    def restrictions(self, restrictions: str):
        self.__restrictions = restrictions

class FunctionClause:

    pass
class plSql_DeterministicClause(FunctionClause):

    pass
class plSql_PipelinedClause(FunctionClause):

    pass
class plSql_ResultCacheClause(FunctionClause):

    def __init__(self, dataSources: str):
        self.dataSources = dataSources
        
    @property
    def dataSources(self) -> str:
        return self.__dataSources

    @dataSources.setter
    def dataSources(self, dataSources: str):
        self.__dataSources = dataSources

class plSql_FunctionInvokerRightsClause(FunctionClause):

    def __init__(self, right: str):
        self.right = right
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

class plSql_Expression:

    pass
class plSql_ParameterValue:

    pass
class plSql_FunctionContent:

    pass
class plSql_FunctionClause:

    pass
class Item:

    pass
class plSql_Pragma(Item):

    pass
class plSql_ItemDeclaration(Item):

    pass
class plSql_ProcedureDeclaration(Item):

    def __init__(self, name: str, plSql_ProcedureDeclaration: "plSql_ParameterSequence" = None):
        self.name = name
        self.plSql_ProcedureDeclaration = plSql_ProcedureDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def plSql_ProcedureDeclaration(self):
        return self.__plSql_ProcedureDeclaration

    @plSql_ProcedureDeclaration.setter
    def plSql_ProcedureDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ProcedureDeclaration__plSql_ProcedureDeclaration", None)
        self.__plSql_ProcedureDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ParameterSequence10"):
                opp_val = getattr(old_value, "plSql_ParameterSequence10", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ParameterSequence10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ParameterSequence10"):
                opp_val = getattr(value, "plSql_ParameterSequence10", None)
                setattr(value, "plSql_ParameterSequence10", self)

class plSql_Item:

    pass
class plSql_ProcedureContent:

    pass
class plSql_ProcedureInvokerRightsClause:

    def __init__(self, right: str, plSql_ProcedureInvokerRightsClause: "plSql_Procedure" = None, plSql_ProcedureInvokerRightsClause6: "plSql_Package" = None):
        self.right = right
        self.plSql_ProcedureInvokerRightsClause = plSql_ProcedureInvokerRightsClause
        self.plSql_ProcedureInvokerRightsClause6 = plSql_ProcedureInvokerRightsClause6
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

    @property
    def plSql_ProcedureInvokerRightsClause(self):
        return self.__plSql_ProcedureInvokerRightsClause

    @plSql_ProcedureInvokerRightsClause.setter
    def plSql_ProcedureInvokerRightsClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ProcedureInvokerRightsClause__plSql_ProcedureInvokerRightsClause", None)
        self.__plSql_ProcedureInvokerRightsClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Procedure2"):
                opp_val = getattr(old_value, "plSql_Procedure2", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Procedure2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Procedure2"):
                opp_val = getattr(value, "plSql_Procedure2", None)
                setattr(value, "plSql_Procedure2", self)

    @property
    def plSql_ProcedureInvokerRightsClause6(self):
        return self.__plSql_ProcedureInvokerRightsClause6

    @plSql_ProcedureInvokerRightsClause6.setter
    def plSql_ProcedureInvokerRightsClause6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ProcedureInvokerRightsClause__plSql_ProcedureInvokerRightsClause6", None)
        self.__plSql_ProcedureInvokerRightsClause6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_Package"):
                opp_val = getattr(old_value, "plSql_Package", None)
                if opp_val == self:
                    setattr(old_value, "plSql_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_Package"):
                opp_val = getattr(value, "plSql_Package", None)
                setattr(value, "plSql_Package", self)

class plSql_ParameterSequence:

    pass
class NameDeclaration:

    pass
class plSql_ParameterDeclaration(NameDeclaration):

    def __init__(self, behavior: str, dataType: str, plSql_ParameterDeclaration: "plSql_ParameterSequence" = None, plSql_ParameterDeclaration24: "plSql_ParameterValue" = None):
        self.behavior = behavior
        self.dataType = dataType
        self.plSql_ParameterDeclaration = plSql_ParameterDeclaration
        self.plSql_ParameterDeclaration24 = plSql_ParameterDeclaration24
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def plSql_ParameterDeclaration24(self):
        return self.__plSql_ParameterDeclaration24

    @plSql_ParameterDeclaration24.setter
    def plSql_ParameterDeclaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ParameterDeclaration__plSql_ParameterDeclaration24", None)
        self.__plSql_ParameterDeclaration24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ParameterValue"):
                opp_val = getattr(old_value, "plSql_ParameterValue", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ParameterValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ParameterValue"):
                opp_val = getattr(value, "plSql_ParameterValue", None)
                setattr(value, "plSql_ParameterValue", self)

    @property
    def plSql_ParameterDeclaration(self):
        return self.__plSql_ParameterDeclaration

    @plSql_ParameterDeclaration.setter
    def plSql_ParameterDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_ParameterDeclaration__plSql_ParameterDeclaration", None)
        self.__plSql_ParameterDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ParameterSequence22"):
                opp_val = getattr(old_value, "plSql_ParameterSequence22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ParameterSequence22"):
                opp_val = getattr(value, "plSql_ParameterSequence22", None)
                if opp_val is None:
                    setattr(value, "plSql_ParameterSequence22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class plSql_ProcedureDefinition(NameDeclaration, Item):

    pass
class plSql_VariableDeclaration(NameDeclaration, ItemDeclaration):

    def __init__(self, isConstant: bool, dataType: str, isNotNull: bool, plSql_VariableDeclaration: "plSql_VariableValue" = None):
        self.isConstant = isConstant
        self.dataType = dataType
        self.isNotNull = isNotNull
        self.plSql_VariableDeclaration = plSql_VariableDeclaration
        
    @property
    def isConstant(self) -> bool:
        return self.__isConstant

    @isConstant.setter
    def isConstant(self, isConstant: bool):
        self.__isConstant = isConstant

    @property
    def isNotNull(self) -> bool:
        return self.__isNotNull

    @isNotNull.setter
    def isNotNull(self, isNotNull: bool):
        self.__isNotNull = isNotNull

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def plSql_VariableDeclaration(self):
        return self.__plSql_VariableDeclaration

    @plSql_VariableDeclaration.setter
    def plSql_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_VariableDeclaration__plSql_VariableDeclaration", None)
        self.__plSql_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_VariableValue"):
                opp_val = getattr(old_value, "plSql_VariableValue", None)
                if opp_val == self:
                    setattr(old_value, "plSql_VariableValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_VariableValue"):
                opp_val = getattr(value, "plSql_VariableValue", None)
                setattr(value, "plSql_VariableValue", self)

class plSql_LoopVariableDeclaration(NameDeclaration):

    pass
class CompilationUnit:

    pass
class plSql_Function(NameDeclaration, CompilationUnit):

    def __init__(self, schemaName: str, returnType: str, plSql_Function: "plSql_ParameterSequence" = None, plSql_Function18: set["plSql_FunctionClause"] = None, plSql_Function20: "plSql_FunctionContent" = None):
        self.schemaName = schemaName
        self.returnType = returnType
        self.plSql_Function = plSql_Function
        self.plSql_Function18 = plSql_Function18 if plSql_Function18 is not None else set()
        self.plSql_Function20 = plSql_Function20
        
    @property
    def schemaName(self) -> str:
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def plSql_Function(self):
        return self.__plSql_Function

    @plSql_Function.setter
    def plSql_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Function__plSql_Function", None)
        self.__plSql_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ParameterSequence16"):
                opp_val = getattr(old_value, "plSql_ParameterSequence16", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ParameterSequence16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ParameterSequence16"):
                opp_val = getattr(value, "plSql_ParameterSequence16", None)
                setattr(value, "plSql_ParameterSequence16", self)

    @property
    def plSql_Function18(self):
        return self.__plSql_Function18

    @plSql_Function18.setter
    def plSql_Function18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Function__plSql_Function18", None)
        self.__plSql_Function18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plSql_FunctionClause"):
                    opp_val = getattr(item, "plSql_FunctionClause", None)
                    
                    if opp_val == self:
                        setattr(item, "plSql_FunctionClause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plSql_FunctionClause"):
                    opp_val = getattr(item, "plSql_FunctionClause", None)
                    
                    setattr(item, "plSql_FunctionClause", self)
                    

    @property
    def plSql_Function20(self):
        return self.__plSql_Function20

    @plSql_Function20.setter
    def plSql_Function20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Function__plSql_Function20", None)
        self.__plSql_Function20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_FunctionContent"):
                opp_val = getattr(old_value, "plSql_FunctionContent", None)
                if opp_val == self:
                    setattr(old_value, "plSql_FunctionContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_FunctionContent"):
                opp_val = getattr(value, "plSql_FunctionContent", None)
                setattr(value, "plSql_FunctionContent", self)

class plSql_Package(NameDeclaration, CompilationUnit):

    def __init__(self, schemaName: str, endName: str, plSql_Package: "plSql_ProcedureInvokerRightsClause" = None, plSql_Package8: set["plSql_Item"] = None):
        self.schemaName = schemaName
        self.endName = endName
        self.plSql_Package = plSql_Package
        self.plSql_Package8 = plSql_Package8 if plSql_Package8 is not None else set()
        
    @property
    def endName(self) -> str:
        return self.__endName

    @endName.setter
    def endName(self, endName: str):
        self.__endName = endName

    @property
    def schemaName(self) -> str:
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName

    @property
    def plSql_Package8(self):
        return self.__plSql_Package8

    @plSql_Package8.setter
    def plSql_Package8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Package__plSql_Package8", None)
        self.__plSql_Package8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plSql_Item"):
                    opp_val = getattr(item, "plSql_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "plSql_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plSql_Item"):
                    opp_val = getattr(item, "plSql_Item", None)
                    
                    setattr(item, "plSql_Item", self)
                    

    @property
    def plSql_Package(self):
        return self.__plSql_Package

    @plSql_Package.setter
    def plSql_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Package__plSql_Package", None)
        self.__plSql_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ProcedureInvokerRightsClause6"):
                opp_val = getattr(old_value, "plSql_ProcedureInvokerRightsClause6", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ProcedureInvokerRightsClause6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ProcedureInvokerRightsClause6"):
                opp_val = getattr(value, "plSql_ProcedureInvokerRightsClause6", None)
                setattr(value, "plSql_ProcedureInvokerRightsClause6", self)

class plSql_Procedure(NameDeclaration, CompilationUnit):

    def __init__(self, schemaName: str, plSql_Procedure: "plSql_ParameterSequence" = None, plSql_Procedure2: "plSql_ProcedureInvokerRightsClause" = None, plSql_Procedure4: "plSql_ProcedureContent" = None):
        self.schemaName = schemaName
        self.plSql_Procedure = plSql_Procedure
        self.plSql_Procedure2 = plSql_Procedure2
        self.plSql_Procedure4 = plSql_Procedure4
        
    @property
    def schemaName(self) -> str:
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName

    @property
    def plSql_Procedure(self):
        return self.__plSql_Procedure

    @plSql_Procedure.setter
    def plSql_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Procedure__plSql_Procedure", None)
        self.__plSql_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ParameterSequence"):
                opp_val = getattr(old_value, "plSql_ParameterSequence", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ParameterSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ParameterSequence"):
                opp_val = getattr(value, "plSql_ParameterSequence", None)
                setattr(value, "plSql_ParameterSequence", self)

    @property
    def plSql_Procedure2(self):
        return self.__plSql_Procedure2

    @plSql_Procedure2.setter
    def plSql_Procedure2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Procedure__plSql_Procedure2", None)
        self.__plSql_Procedure2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ProcedureInvokerRightsClause"):
                opp_val = getattr(old_value, "plSql_ProcedureInvokerRightsClause", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ProcedureInvokerRightsClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ProcedureInvokerRightsClause"):
                opp_val = getattr(value, "plSql_ProcedureInvokerRightsClause", None)
                setattr(value, "plSql_ProcedureInvokerRightsClause", self)

    @property
    def plSql_Procedure4(self):
        return self.__plSql_Procedure4

    @plSql_Procedure4.setter
    def plSql_Procedure4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plSql_Procedure__plSql_Procedure4", None)
        self.__plSql_Procedure4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plSql_ProcedureContent"):
                opp_val = getattr(old_value, "plSql_ProcedureContent", None)
                if opp_val == self:
                    setattr(old_value, "plSql_ProcedureContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plSql_ProcedureContent"):
                opp_val = getattr(value, "plSql_ProcedureContent", None)
                setattr(value, "plSql_ProcedureContent", self)

class plSql_CompilationUnit:

    pass
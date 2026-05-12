from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RWOperation(Enum):
    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"
class TargetElement(Enum):
    ALIAS = "ALIAS"
    INDEX = "INDEX"
    VIEW = "VIEW"
    TABLE = "TABLE"
class DropRange(Enum):
    RESTRICT = "RESTRICT"
    CASCADE = "CASCADE"
class CursorType(Enum):
    NOTSCROLL = "NOTSCROLL"
    SCROLL = "SCROLL"
    DYNSCROLL = "DYNSCROLL"
class ShareMode(Enum):
    SHARE = "SHARE"
    EXCLUSIVE = "EXCLUSIVE"
class TargetItem(Enum):
    ALL = "ALL"
    CURRENT = "CURRENT"
    ALLSQL = "ALLSQL"
class OpenUsingType(Enum):
    NONE = "NONE"
    DESCRIPTOR = "DESCRIPTOR"
    VARIABLE = "VARIABLE"
class IsolationLevel(Enum):
    NONE = "NONE"
    SERIALIZABLE = "SERIALIZABLE"
    NO_COMMIT = "NO_COMMIT"
    READ_UNCOMMITTED = "READ_UNCOMMITTED"
    READ_COMMITTED = "READ_COMMITTED"
    REPEATABLE_READ = "REPEATABLE_READ"
class StatementType(Enum):
    DML = "DML"
    DDL = "DDL"
    DBL = "DBL"
class UsingType(Enum):
    NONE = "NONE"
    NAMES = "NAMES"
    SYSTEM_NAMES = "SYSTEM_NAMES"
    LABELS = "LABELS"
    ANY = "ANY"
    BOTH = "BOTH"
    ALL = "ALL"
class FetchPosition(Enum):
    PRIOR = "PRIOR"
    FIRST = "FIRST"
    LAST = "LAST"
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    CURRENT = "CURRENT"
    RELATIVE = "RELATIVE"
    NEXT = "NEXT"


############################################
# Definition of Classes
############################################

class syntax_dbl_MultipleRowFetchClause:

    def __init__(self, descriptor: str, rowsNumber: str, usingDescriptor: bool):
        self.descriptor = descriptor
        self.rowsNumber = rowsNumber
        self.usingDescriptor = usingDescriptor
        
        pass
    @property
    def usingDescriptor(self):
        return self.__usingDescriptor

    @usingDescriptor.setter
    def usingDescriptor(self, usingDescriptor: bool):
        self.__usingDescriptor = usingDescriptor


    @property
    def descriptor(self):
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor


    @property
    def rowsNumber(self):
        return self.__rowsNumber

    @rowsNumber.setter
    def rowsNumber(self, rowsNumber: str):
        self.__rowsNumber = rowsNumber


class syntax_dbl_IntoClause:

    def __init__(self, descriptorName: str, using: str):
        self.descriptorName = descriptorName
        self.using = using
        
        pass
    @property
    def descriptorName(self):
        return self.__descriptorName

    @descriptorName.setter
    def descriptorName(self, descriptorName: str):
        self.__descriptorName = descriptorName


    @property
    def using(self):
        return self.__using

    @using.setter
    def using(self, using: str):
        self.__using = using


class MultipleRowFetchClause:

    pass
class BindingStatement:

    pass
class syntax_dbl_DescribeStatement(BindingStatement):

    def __init__(self, statementName: str, syntax_dbl_DescribeStatement: "IntoClause" = None):
        self.statementName = statementName
        self.syntax_dbl_DescribeStatement = syntax_dbl_DescribeStatement
        
        pass
    @property
    def statementName(self):
        return self.__statementName

    @statementName.setter
    def statementName(self, statementName: str):
        self.__statementName = statementName


    @property
    def syntax_dbl_DescribeStatement(self):
        return self.__syntax_dbl_DescribeStatement

    @syntax_dbl_DescribeStatement.setter
    def syntax_dbl_DescribeStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_dbl_DescribeStatement__syntax_dbl_DescribeStatement", None)
        self.__syntax_dbl_DescribeStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntoClause"):
                opp_val = getattr(old_value, "IntoClause", None)
                if opp_val == self:
                    setattr(old_value, "IntoClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntoClause"):
                opp_val = getattr(value, "IntoClause", None)
                setattr(value, "IntoClause", self)

class syntax_dbl_SetTransactionStatement(BindingStatement):

    def __init__(self, isolationLevel: str, rwOperation: str):
        self.isolationLevel = isolationLevel
        self.rwOperation = rwOperation
        
        pass
    @property
    def isolationLevel(self):
        return self.__isolationLevel

    @isolationLevel.setter
    def isolationLevel(self, isolationLevel: str):
        self.__isolationLevel = isolationLevel


    @property
    def rwOperation(self):
        return self.__rwOperation

    @rwOperation.setter
    def rwOperation(self, rwOperation: str):
        self.__rwOperation = rwOperation


class syntax_dbl_FetchStatement(BindingStatement):

    def __init__(self, cursorName: str, into: str, position: str, relativePosition: str, syntax_dbl_FetchStatement: "MultipleRowFetchClause" = None):
        self.cursorName = cursorName
        self.into = into
        self.position = position
        self.relativePosition = relativePosition
        self.syntax_dbl_FetchStatement = syntax_dbl_FetchStatement
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def cursorName(self):
        return self.__cursorName

    @cursorName.setter
    def cursorName(self, cursorName: str):
        self.__cursorName = cursorName


    @property
    def into(self):
        return self.__into

    @into.setter
    def into(self, into: str):
        self.__into = into


    @property
    def relativePosition(self):
        return self.__relativePosition

    @relativePosition.setter
    def relativePosition(self, relativePosition: str):
        self.__relativePosition = relativePosition


    @property
    def syntax_dbl_FetchStatement(self):
        return self.__syntax_dbl_FetchStatement

    @syntax_dbl_FetchStatement.setter
    def syntax_dbl_FetchStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_dbl_FetchStatement__syntax_dbl_FetchStatement", None)
        self.__syntax_dbl_FetchStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultipleRowFetchClause"):
                opp_val = getattr(old_value, "MultipleRowFetchClause", None)
                if opp_val == self:
                    setattr(old_value, "MultipleRowFetchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultipleRowFetchClause"):
                opp_val = getattr(value, "MultipleRowFetchClause", None)
                setattr(value, "MultipleRowFetchClause", self)

class syntax_dbl_DeclareCursorStatement(BindingStatement):

    def __init__(self, cursorName: str, cursorType: str, forQuery: str, forStatementName: str, hold: bool):
        self.cursorName = cursorName
        self.cursorType = cursorType
        self.forQuery = forQuery
        self.forStatementName = forStatementName
        self.hold = hold
        
        pass
    @property
    def cursorType(self):
        return self.__cursorType

    @cursorType.setter
    def cursorType(self, cursorType: str):
        self.__cursorType = cursorType


    @property
    def cursorName(self):
        return self.__cursorName

    @cursorName.setter
    def cursorName(self, cursorName: str):
        self.__cursorName = cursorName


    @property
    def hold(self):
        return self.__hold

    @hold.setter
    def hold(self, hold: bool):
        self.__hold = hold


    @property
    def forStatementName(self):
        return self.__forStatementName

    @forStatementName.setter
    def forStatementName(self, forStatementName: str):
        self.__forStatementName = forStatementName


    @property
    def forQuery(self):
        return self.__forQuery

    @forQuery.setter
    def forQuery(self, forQuery: str):
        self.__forQuery = forQuery


class QueryExpressionBody:

    pass
class syntax_dml_ExtendedQueryExpressionBody(QueryExpressionBody):

    def __init__(self, optimizeRecordsNumber: int):
        self.optimizeRecordsNumber = optimizeRecordsNumber
        
        pass
    @property
    def optimizeRecordsNumber(self):
        return self.__optimizeRecordsNumber

    @optimizeRecordsNumber.setter
    def optimizeRecordsNumber(self, optimizeRecordsNumber: int):
        self.__optimizeRecordsNumber = optimizeRecordsNumber


class QuerySelect:

    pass
class dml_ExtendedQueryExpressionBody:

    pass
class syntax_dml_ExtendedQuerySelect(QuerySelect, dml_ExtendedQueryExpressionBody):

    pass
class ddl_syntax_IndexDef:

    pass
class ddl_syntax_TableColumnDef:

    pass
class syntax_QueryParserRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class syntax_dbl_OpenStatement(BindingStatement):

    def __init__(self, cursor: str, using: str, usingType: str):
        self.cursor = cursor
        self.using = using
        self.usingType = usingType
        
        pass
    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor: str):
        self.__cursor = cursor


    @property
    def usingType(self):
        return self.__usingType

    @usingType.setter
    def usingType(self, usingType: str):
        self.__usingType = usingType


    @property
    def using(self):
        return self.__using

    @using.setter
    def using(self, using: str):
        self.__using = using


class syntax_dbl_CloseStatement(BindingStatement):

    def __init__(self, cursor: str):
        self.cursor = cursor
        
        pass
    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor: str):
        self.__cursor = cursor


class syntax_dbl_PrepareStatement(BindingStatement):

    def __init__(self, from_: str, statementName: str, syntax_dbl_PrepareStatement: "IntoClause" = None):
        self.from_ = from_
        self.statementName = statementName
        self.syntax_dbl_PrepareStatement = syntax_dbl_PrepareStatement
        
        pass
    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def statementName(self):
        return self.__statementName

    @statementName.setter
    def statementName(self, statementName: str):
        self.__statementName = statementName


    @property
    def syntax_dbl_PrepareStatement(self):
        return self.__syntax_dbl_PrepareStatement

    @syntax_dbl_PrepareStatement.setter
    def syntax_dbl_PrepareStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_dbl_PrepareStatement__syntax_dbl_PrepareStatement", None)
        self.__syntax_dbl_PrepareStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntoClause35"):
                opp_val = getattr(old_value, "IntoClause35", None)
                if opp_val == self:
                    setattr(old_value, "IntoClause35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntoClause35"):
                opp_val = getattr(value, "IntoClause35", None)
                setattr(value, "IntoClause35", self)

class syntax_dbl_ExecuteStatement(BindingStatement):

    def __init__(self, statementName: str):
        self.statementName = statementName
        
        pass
    @property
    def statementName(self):
        return self.__statementName

    @statementName.setter
    def statementName(self, statementName: str):
        self.__statementName = statementName


class syntax_dbl_ExecuteImmediateStatement(BindingStatement):

    def __init__(self, variable: str):
        self.variable = variable
        
        pass
    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable


class IntoClause:

    pass
class ddl_syntax_QualifiedName:

    pass
class DefinitionStatement:

    pass
class syntax_ddl_CreateViewStatement(DefinitionStatement):

    def __init__(self, fields: str, query: str, syntax_ddl_CreateViewStatement: "ddl_syntax_QualifiedName" = None):
        self.fields = fields
        self.query = query
        self.syntax_ddl_CreateViewStatement = syntax_ddl_CreateViewStatement
        
        pass
    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query


    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, fields: str):
        self.__fields = fields


    @property
    def syntax_ddl_CreateViewStatement(self):
        return self.__syntax_ddl_CreateViewStatement

    @syntax_ddl_CreateViewStatement.setter
    def syntax_ddl_CreateViewStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_CreateViewStatement__syntax_ddl_CreateViewStatement", None)
        self.__syntax_ddl_CreateViewStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName25"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName25", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName25"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName25", None)
                setattr(value, "ddl_syntax_QualifiedName25", self)

class syntax_ddl_DropStatement(DefinitionStatement):

    def __init__(self, range: str, target: str, syntax_ddl_DropStatement: "ddl_syntax_QualifiedName" = None):
        self.range = range
        self.target = target
        self.syntax_ddl_DropStatement = syntax_ddl_DropStatement
        
        pass
    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range


    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def syntax_ddl_DropStatement(self):
        return self.__syntax_ddl_DropStatement

    @syntax_ddl_DropStatement.setter
    def syntax_ddl_DropStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_DropStatement__syntax_ddl_DropStatement", None)
        self.__syntax_ddl_DropStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName27"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName27", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName27"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName27", None)
                setattr(value, "ddl_syntax_QualifiedName27", self)

class syntax_ddl_RollbackStatement(DefinitionStatement):

    def __init__(self, hold: bool):
        self.hold = hold
        
        pass
    @property
    def hold(self):
        return self.__hold

    @hold.setter
    def hold(self, hold: bool):
        self.__hold = hold


class syntax_ddl_CreateAliasStatement(DefinitionStatement):

    pass
class syntax_ddl_RenameStatement(DefinitionStatement):

    def __init__(self, newName: str, system: str, target: str, syntax_ddl_RenameStatement: "ddl_syntax_QualifiedName" = None):
        self.newName = newName
        self.system = system
        self.target = target
        self.syntax_ddl_RenameStatement = syntax_ddl_RenameStatement
        
        pass
    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system


    @property
    def newName(self):
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName


    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def syntax_ddl_RenameStatement(self):
        return self.__syntax_ddl_RenameStatement

    @syntax_ddl_RenameStatement.setter
    def syntax_ddl_RenameStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_RenameStatement__syntax_ddl_RenameStatement", None)
        self.__syntax_ddl_RenameStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName31"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName31", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName31"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName31", None)
                setattr(value, "ddl_syntax_QualifiedName31", self)

class syntax_ddl_CommitStatement(DefinitionStatement):

    def __init__(self, hold: bool):
        self.hold = hold
        
        pass
    @property
    def hold(self):
        return self.__hold

    @hold.setter
    def hold(self, hold: bool):
        self.__hold = hold


class syntax_ddl_CreateIndexStatement(DefinitionStatement):

    def __init__(self, unique: bool, syntax_ddl_CreateIndexStatement: "ddl_syntax_QualifiedName" = None, syntax_ddl_CreateIndexStatement16: "ddl_syntax_QualifiedName" = None, syntax_ddl_CreateIndexStatement19: "ddl_syntax_IndexDef" = None):
        self.unique = unique
        self.syntax_ddl_CreateIndexStatement = syntax_ddl_CreateIndexStatement
        self.syntax_ddl_CreateIndexStatement16 = syntax_ddl_CreateIndexStatement16
        self.syntax_ddl_CreateIndexStatement19 = syntax_ddl_CreateIndexStatement19
        
        pass
    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def syntax_ddl_CreateIndexStatement(self):
        return self.__syntax_ddl_CreateIndexStatement

    @syntax_ddl_CreateIndexStatement.setter
    def syntax_ddl_CreateIndexStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_CreateIndexStatement__syntax_ddl_CreateIndexStatement", None)
        self.__syntax_ddl_CreateIndexStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName14"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName14", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName14"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName14", None)
                setattr(value, "ddl_syntax_QualifiedName14", self)

    @property
    def syntax_ddl_CreateIndexStatement19(self):
        return self.__syntax_ddl_CreateIndexStatement19

    @syntax_ddl_CreateIndexStatement19.setter
    def syntax_ddl_CreateIndexStatement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_CreateIndexStatement__syntax_ddl_CreateIndexStatement19", None)
        self.__syntax_ddl_CreateIndexStatement19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_IndexDef"):
                opp_val = getattr(old_value, "ddl_syntax_IndexDef", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_IndexDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_IndexDef"):
                opp_val = getattr(value, "ddl_syntax_IndexDef", None)
                setattr(value, "ddl_syntax_IndexDef", self)

    @property
    def syntax_ddl_CreateIndexStatement16(self):
        return self.__syntax_ddl_CreateIndexStatement16

    @syntax_ddl_CreateIndexStatement16.setter
    def syntax_ddl_CreateIndexStatement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_CreateIndexStatement__syntax_ddl_CreateIndexStatement16", None)
        self.__syntax_ddl_CreateIndexStatement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName17"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName17", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName17"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName17", None)
                setattr(value, "ddl_syntax_QualifiedName17", self)

class syntax_ddl_CreateTableStatement(DefinitionStatement):

    pass
class syntax_ddl_ReleaseStatement(DefinitionStatement):

    def __init__(self, serverName: str):
        self.serverName = serverName
        
        pass
    @property
    def serverName(self):
        return self.__serverName

    @serverName.setter
    def serverName(self, serverName: str):
        self.__serverName = serverName


class syntax_ddl_LockTableStatement(DefinitionStatement):

    def __init__(self, allowRead: bool, shareMode: str, syntax_ddl_LockTableStatement: "ddl_syntax_QualifiedName" = None):
        self.allowRead = allowRead
        self.shareMode = shareMode
        self.syntax_ddl_LockTableStatement = syntax_ddl_LockTableStatement
        
        pass
    @property
    def shareMode(self):
        return self.__shareMode

    @shareMode.setter
    def shareMode(self, shareMode: str):
        self.__shareMode = shareMode


    @property
    def allowRead(self):
        return self.__allowRead

    @allowRead.setter
    def allowRead(self, allowRead: bool):
        self.__allowRead = allowRead


    @property
    def syntax_ddl_LockTableStatement(self):
        return self.__syntax_ddl_LockTableStatement

    @syntax_ddl_LockTableStatement.setter
    def syntax_ddl_LockTableStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_LockTableStatement__syntax_ddl_LockTableStatement", None)
        self.__syntax_ddl_LockTableStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName29"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName29", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName29"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName29", None)
                setattr(value, "ddl_syntax_QualifiedName29", self)

class syntax_ddl_SetConnectionStatement(DefinitionStatement):

    def __init__(self, databaseName: str):
        self.databaseName = databaseName
        
        pass
    @property
    def databaseName(self):
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName


class syntax_ddl_DisconnectStatement(DefinitionStatement):

    def __init__(self, target: str):
        self.target = target
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


class syntax_ddl_ConnectStatement(DefinitionStatement):

    def __init__(self, pwd: str, reset: bool, to: str, user: str):
        self.pwd = pwd
        self.reset = reset
        self.to = to
        self.user = user
        
        pass
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user: str):
        self.__user = user


    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to


    @property
    def reset(self):
        return self.__reset

    @reset.setter
    def reset(self, reset: bool):
        self.__reset = reset


    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, pwd: str):
        self.__pwd = pwd


class syntax_ddl_CallStatement(DefinitionStatement):

    def __init__(self, parms: str, syntax_ddl_CallStatement: "ddl_syntax_QualifiedName" = None):
        self.parms = parms
        self.syntax_ddl_CallStatement = syntax_ddl_CallStatement
        
        pass
    @property
    def parms(self):
        return self.__parms

    @parms.setter
    def parms(self, parms: str):
        self.__parms = parms


    @property
    def syntax_ddl_CallStatement(self):
        return self.__syntax_ddl_CallStatement

    @syntax_ddl_CallStatement.setter
    def syntax_ddl_CallStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_ddl_CallStatement__syntax_ddl_CallStatement", None)
        self.__syntax_ddl_CallStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ddl_syntax_QualifiedName"):
                opp_val = getattr(old_value, "ddl_syntax_QualifiedName", None)
                if opp_val == self:
                    setattr(old_value, "ddl_syntax_QualifiedName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ddl_syntax_QualifiedName"):
                opp_val = getattr(value, "ddl_syntax_QualifiedName", None)
                setattr(value, "ddl_syntax_QualifiedName", self)

class syntax_SQLObjectNameHelper(ABC):

    pass
class syntax_QueryWriterRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class syntax_NameHelperRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class SQLObjectNameHelper:

    pass
class Service:

    pass
class Plugin:

    pass
class syntax_StatementWriter(Service, Plugin):

    pass
class syntax_StatementParser(Service, Plugin):

    pass
class syntax_NameHelper(Service, Plugin, SQLObjectNameHelper):

    def __init__(self, syntax_NameHelper: "syntax_StatementWriter" = None):
        self.syntax_NameHelper = syntax_NameHelper
        
        pass
    @property
    def syntax_NameHelper(self):
        return self.__syntax_NameHelper

    @syntax_NameHelper.setter
    def syntax_NameHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_NameHelper__syntax_NameHelper", None)
        self.__syntax_NameHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_StatementWriter"):
                opp_val = getattr(old_value, "syntax_StatementWriter", None)
                if opp_val == self:
                    setattr(old_value, "syntax_StatementWriter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_StatementWriter"):
                opp_val = getattr(value, "syntax_StatementWriter", None)
                setattr(value, "syntax_StatementWriter", self)

    def resolveContainers(self, syntax_query):
        # TODO: Implement resolveContainers method
        pass

class syntax_EmbeddedStatement(ABC):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class syntax_DefinitionWriterRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class syntax_BindingStatement(ABC):

    def __init__(self, syntax_BindingStatement: "syntax_BindingParseResult" = None):
        self.syntax_BindingStatement = syntax_BindingStatement
        
        pass
    @property
    def syntax_BindingStatement(self):
        return self.__syntax_BindingStatement

    @syntax_BindingStatement.setter
    def syntax_BindingStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_BindingStatement__syntax_BindingStatement", None)
        self.__syntax_BindingStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_BindingParseResult"):
                opp_val = getattr(old_value, "syntax_BindingParseResult", None)
                if opp_val == self:
                    setattr(old_value, "syntax_BindingParseResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_BindingParseResult"):
                opp_val = getattr(value, "syntax_BindingParseResult", None)
                setattr(value, "syntax_BindingParseResult", self)

    def getStatementType(self) :
        # TODO: Implement getStatementType method
        pass

class syntax_BindingParseResult:

    pass
class syntax_BindingParserRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class StatementWriter:

    pass
class syntax_QueryWriter(StatementWriter):

    def __init__(self):
        
        pass
    def writeQuery(self, syntax_statement) :
        # TODO: Implement writeQuery method
        pass

class syntax_DefinitionWriter(StatementWriter):

    def __init__(self):
        
        pass
    def insertData(self, syntax_table) :
        # TODO: Implement insertData method
        pass

    def createSchema(self, syntax_schema, syntax_name) :
        # TODO: Implement createSchema method
        pass

    def selectData(self, syntax_table) :
        # TODO: Implement selectData method
        pass

    def createIndex(self, syntax_name, syntax_table, syntax_index) :
        # TODO: Implement createIndex method
        pass

    def dropIndex(self, syntax_index) :
        # TODO: Implement dropIndex method
        pass

    def deleteData(self, syntax_table) :
        # TODO: Implement deleteData method
        pass

    def dropSchema(self, syntax_schema, syntax_ignoreFailOnNonEmpty) :
        # TODO: Implement dropSchema method
        pass

    def dropView(self, syntax_view) :
        # TODO: Implement dropView method
        pass

    def dropTable(self, syntax_table) :
        # TODO: Implement dropTable method
        pass

    def createView(self, syntax_schema, syntax_name, syntax_view) :
        # TODO: Implement createView method
        pass

    def createTable(self, syntax_name, syntax_schema, syntax_table) :
        # TODO: Implement createTable method
        pass

class syntax_DefinitionStatement(ABC):

    def __init__(self, syntax_DefinitionStatement: "syntax_DefinitionParseResult" = None):
        self.syntax_DefinitionStatement = syntax_DefinitionStatement
        
        pass
    @property
    def syntax_DefinitionStatement(self):
        return self.__syntax_DefinitionStatement

    @syntax_DefinitionStatement.setter
    def syntax_DefinitionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syntax_DefinitionStatement__syntax_DefinitionStatement", None)
        self.__syntax_DefinitionStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_DefinitionParseResult"):
                opp_val = getattr(old_value, "syntax_DefinitionParseResult", None)
                if opp_val == self:
                    setattr(old_value, "syntax_DefinitionParseResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_DefinitionParseResult"):
                opp_val = getattr(value, "syntax_DefinitionParseResult", None)
                setattr(value, "syntax_DefinitionParseResult", self)

    def getStatementType(self) :
        # TODO: Implement getStatementType method
        pass

class syntax_DefinitionParseResult:

    pass
class syntax_DefinitionParseError:

    pass
class syntax_DefinitionParserRegistry(ABC):

    def __init__(self):
        
        pass
    def lookup(self, syntax_connectionConfig) :
        # TODO: Implement lookup method
        pass

class StatementParser:

    pass
class syntax_QueryParser(StatementParser):

    def __init__(self):
        
        pass
    def parseQuery(self, syntax_sql) :
        # TODO: Implement parseQuery method
        pass

class syntax_DefinitionParser(StatementParser):

    def __init__(self):
        
        pass
    def parseDefinition(self, syntax_sql) :
        # TODO: Implement parseDefinition method
        pass

class syntax_BindingParser(StatementParser):

    def __init__(self):
        
        pass
    def parseBinding(self, syntax_sql) :
        # TODO: Implement parseBinding method
        pass

class syntax_BindingParseError:

    pass
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationKind(Enum):
    ONLY_ONE = "ONLY_ONE"
    ZERO_OR_ONE = "ZERO_OR_ONE"
    ZERO_OR_MANY = "ZERO_OR_MANY"
    ONE_OR_MANY = "ONE_OR_MANY"


############################################
# Definition of Classes
############################################

class rdb_ERDInfo:

    def __init__(self, autoLayout: bool, version: str):
        self.autoLayout = autoLayout
        self.version = version
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def autoLayout(self) -> bool:
        return self.__autoLayout

    @autoLayout.setter
    def autoLayout(self, autoLayout: bool):
        self.__autoLayout = autoLayout

class Table:

    pass
class rdb_View(Table):

    pass
class rdb_UserComment:

    def __init__(self, comment: str, rdb_UserComment: "rdb_Table" = None):
        self.comment = comment
        self.rdb_UserComment = rdb_UserComment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def rdb_UserComment(self):
        return self.__rdb_UserComment

    @rdb_UserComment.setter
    def rdb_UserComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_UserComment__rdb_UserComment", None)
        self.__rdb_UserComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Table"):
                opp_val = getattr(old_value, "rdb_Table", None)
                if opp_val == self:
                    setattr(old_value, "rdb_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Table"):
                opp_val = getattr(value, "rdb_Table", None)
                setattr(value, "rdb_Table", self)

class rdb_Table:

    def __init__(self, comment: str, name: str, constraints: str, logicalName: str, Table: "rdb_DB" = None, table: set["rdb_Column"] = None, rdb_Table: "rdb_UserComment" = None, Table11: "rdb_Column" = None, tables: "rdb_DB" = None, target: set["rdb_Relation"] = None, source: set["rdb_Relation"] = None, Table13: "rdb_Relation" = None, Table15: "rdb_Relation" = None, rdb_Table19: "rdb_View" = None):
        self.comment = comment
        self.name = name
        self.constraints = constraints
        self.logicalName = logicalName
        self.Table = Table
        self.table = table if table is not None else set()
        self.rdb_Table = rdb_Table
        self.Table11 = Table11
        self.tables = tables
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Table13 = Table13
        self.Table15 = Table15
        self.rdb_Table19 = rdb_Table19
        
    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def logicalName(self) -> str:
        return self.__logicalName

    @logicalName.setter
    def logicalName(self, logicalName: str):
        self.__logicalName = logicalName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def Table11(self):
        return self.__Table11

    @Table11.setter
    def Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__Table11", None)
        self.__Table11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation8"):
                    opp_val = getattr(item, "Relation8", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation8"):
                    opp_val = getattr(item, "Relation8", None)
                    
                    setattr(item, "Relation8", self)
                    

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db"):
                opp_val = getattr(old_value, "db", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db"):
                opp_val = getattr(value, "db", None)
                if opp_val is None:
                    setattr(value, "db", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Table15(self):
        return self.__Table15

    @Table15.setter
    def Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__Table15", None)
        self.__Table15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingLinks"):
                opp_val = getattr(old_value, "incomingLinks", None)
                if opp_val == self:
                    setattr(old_value, "incomingLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingLinks"):
                opp_val = getattr(value, "incomingLinks", None)
                setattr(value, "incomingLinks", self)

    @property
    def Table13(self):
        return self.__Table13

    @Table13.setter
    def Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__Table13", None)
        self.__Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingLinks"):
                opp_val = getattr(old_value, "outgoingLinks", None)
                if opp_val == self:
                    setattr(old_value, "outgoingLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingLinks"):
                opp_val = getattr(value, "outgoingLinks", None)
                setattr(value, "outgoingLinks", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation6"):
                    opp_val = getattr(item, "Relation6", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation6"):
                    opp_val = getattr(item, "Relation6", None)
                    
                    setattr(item, "Relation6", self)
                    

    @property
    def rdb_Table19(self):
        return self.__rdb_Table19

    @rdb_Table19.setter
    def rdb_Table19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__rdb_Table19", None)
        self.__rdb_Table19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_View"):
                opp_val = getattr(old_value, "rdb_View", None)
                if opp_val == self:
                    setattr(old_value, "rdb_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_View"):
                opp_val = getattr(value, "rdb_View", None)
                setattr(value, "rdb_View", self)

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB"):
                opp_val = getattr(old_value, "DB", None)
                if opp_val == self:
                    setattr(old_value, "DB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB"):
                opp_val = getattr(value, "DB", None)
                setattr(value, "DB", self)

    @property
    def rdb_Table(self):
        return self.__rdb_Table

    @rdb_Table.setter
    def rdb_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__rdb_Table", None)
        self.__rdb_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_UserComment"):
                opp_val = getattr(old_value, "rdb_UserComment", None)
                if opp_val == self:
                    setattr(old_value, "rdb_UserComment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_UserComment"):
                opp_val = getattr(value, "rdb_UserComment", None)
                setattr(value, "rdb_UserComment", self)

class ERDInfo:

    pass
class rdb_DB(ERDInfo):

    def __init__(self, key: str, url: str, id: str, sid: str, comment: str, dbType: str, db: set["rdb_Table"] = None, db2: set["rdb_Relation"] = None, DB: "rdb_Table" = None, DB17: "rdb_Relation" = None):
        self.key = key
        self.url = url
        self.id = id
        self.sid = sid
        self.comment = comment
        self.dbType = dbType
        self.db = db if db is not None else set()
        self.db2 = db2 if db2 is not None else set()
        self.DB = DB
        self.DB17 = DB17
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def dbType(self) -> str:
        return self.__dbType

    @dbType.setter
    def dbType(self, dbType: str):
        self.__dbType = dbType

    @property
    def sid(self) -> str:
        return self.__sid

    @sid.setter
    def sid(self, sid: str):
        self.__sid = sid

    @property
    def DB(self):
        return self.__DB

    @DB.setter
    def DB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_DB__DB", None)
        self.__DB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables"):
                opp_val = getattr(old_value, "tables", None)
                if opp_val == self:
                    setattr(old_value, "tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables"):
                opp_val = getattr(value, "tables", None)
                setattr(value, "tables", self)

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_DB__db", None)
        self.__db = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    

    @property
    def DB17(self):
        return self.__DB17

    @DB17.setter
    def DB17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_DB__DB17", None)
        self.__DB17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "references"):
                opp_val = getattr(old_value, "references", None)
                if opp_val == self:
                    setattr(old_value, "references", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "references"):
                opp_val = getattr(value, "references", None)
                setattr(value, "references", self)

    @property
    def db2(self):
        return self.__db2

    @db2.setter
    def db2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_DB__db2", None)
        self.__db2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relation"):
                    opp_val = getattr(item, "Relation", None)
                    
                    setattr(item, "Relation", self)
                    

class rdb_Column:

    def __init__(self, field: str, type: str, null: str, default: str, extra: str, logicalField: str, key: str, comment: str, Column: "rdb_Table" = None, columns: "rdb_Table" = None):
        self.field = field
        self.type = type
        self.null = null
        self.default = default
        self.extra = extra
        self.logicalField = logicalField
        self.key = key
        self.comment = comment
        self.Column = Column
        self.columns = columns
        
    @property
    def logicalField(self) -> str:
        return self.__logicalField

    @logicalField.setter
    def logicalField(self, logicalField: str):
        self.__logicalField = logicalField

    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def extra(self) -> str:
        return self.__extra

    @extra.setter
    def extra(self, extra: str):
        self.__extra = extra

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table11"):
                opp_val = getattr(old_value, "Table11", None)
                if opp_val == self:
                    setattr(old_value, "Table11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table11"):
                opp_val = getattr(value, "Table11", None)
                setattr(value, "Table11", self)

class rdb_Relation:

    def __init__(self, bendpoint: str, comment: str, constraint_name: str, source_kind: str, target_kind: str, column_name: str, referenced_column_name: str, Relation: "rdb_DB" = None, Relation6: "rdb_Table" = None, Relation8: "rdb_Table" = None, references: "rdb_DB" = None, outgoingLinks: "rdb_Table" = None, incomingLinks: "rdb_Table" = None):
        self.bendpoint = bendpoint
        self.comment = comment
        self.constraint_name = constraint_name
        self.source_kind = source_kind
        self.target_kind = target_kind
        self.column_name = column_name
        self.referenced_column_name = referenced_column_name
        self.Relation = Relation
        self.Relation6 = Relation6
        self.Relation8 = Relation8
        self.references = references
        self.outgoingLinks = outgoingLinks
        self.incomingLinks = incomingLinks
        
    @property
    def constraint_name(self) -> str:
        return self.__constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name: str):
        self.__constraint_name = constraint_name

    @property
    def column_name(self) -> str:
        return self.__column_name

    @column_name.setter
    def column_name(self, column_name: str):
        self.__column_name = column_name

    @property
    def referenced_column_name(self) -> str:
        return self.__referenced_column_name

    @referenced_column_name.setter
    def referenced_column_name(self, referenced_column_name: str):
        self.__referenced_column_name = referenced_column_name

    @property
    def target_kind(self) -> str:
        return self.__target_kind

    @target_kind.setter
    def target_kind(self, target_kind: str):
        self.__target_kind = target_kind

    @property
    def source_kind(self) -> str:
        return self.__source_kind

    @source_kind.setter
    def source_kind(self, source_kind: str):
        self.__source_kind = source_kind

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def bendpoint(self) -> str:
        return self.__bendpoint

    @bendpoint.setter
    def bendpoint(self, bendpoint: str):
        self.__bendpoint = bendpoint

    @property
    def Relation8(self):
        return self.__Relation8

    @Relation8.setter
    def Relation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__Relation8", None)
        self.__Relation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__Relation", None)
        self.__Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db2"):
                opp_val = getattr(old_value, "db2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db2"):
                opp_val = getattr(value, "db2", None)
                if opp_val is None:
                    setattr(value, "db2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def references(self):
        return self.__references

    @references.setter
    def references(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__references", None)
        self.__references = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB17"):
                opp_val = getattr(old_value, "DB17", None)
                if opp_val == self:
                    setattr(old_value, "DB17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB17"):
                opp_val = getattr(value, "DB17", None)
                setattr(value, "DB17", self)

    @property
    def outgoingLinks(self):
        return self.__outgoingLinks

    @outgoingLinks.setter
    def outgoingLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__outgoingLinks", None)
        self.__outgoingLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table13"):
                opp_val = getattr(old_value, "Table13", None)
                if opp_val == self:
                    setattr(old_value, "Table13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table13"):
                opp_val = getattr(value, "Table13", None)
                setattr(value, "Table13", self)

    @property
    def Relation6(self):
        return self.__Relation6

    @Relation6.setter
    def Relation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__Relation6", None)
        self.__Relation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingLinks(self):
        return self.__incomingLinks

    @incomingLinks.setter
    def incomingLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Relation__incomingLinks", None)
        self.__incomingLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table15"):
                opp_val = getattr(old_value, "Table15", None)
                if opp_val == self:
                    setattr(old_value, "Table15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table15"):
                opp_val = getattr(value, "Table15", None)
                setattr(value, "Table15", self)

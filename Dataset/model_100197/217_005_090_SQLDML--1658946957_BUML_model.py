####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
SQLDML_LocatedElement = Class(name="SQLDML_LocatedElement", is_abstract=True)
SQLDML_Statement = Class(name="SQLDML_Statement", is_abstract=True)
SQLDML_ViewStatement = Class(name="SQLDML_ViewStatement")
SQLDML_SQLRoot = Class(name="SQLDML_SQLRoot")
LocatedElement = Class(name="LocatedElement")
Statement = Class(name="Statement")
SQLDML_QueryStmt = Class(name="SQLDML_QueryStmt", is_abstract=True)
Table = Class(name="Table")
ColumnExp = Class(name="ColumnExp")
QueryStmt = Class(name="QueryStmt")
SQLDML_InsertStmt = Class(name="SQLDML_InsertStmt")
Expression = Class(name="Expression")
SQLDML_Table = Class(name="SQLDML_Table")
NamedElement = Class(name="NamedElement")
SQLDML_WhereClause = Class(name="SQLDML_WhereClause")
WhereClause = Class(name="WhereClause")
SQLDML_QueryStmtCol = Class(name="SQLDML_QueryStmtCol")
SQLDML_QueryStmtAllCol = Class(name="SQLDML_QueryStmtAllCol")
SQLDML_NamedElement = Class(name="SQLDML_NamedElement", is_abstract=True)
SQLDML_OrExp = Class(name="SQLDML_OrExp")
BinaryExp = Class(name="BinaryExp")
SQLDML_AndExp = Class(name="SQLDML_AndExp")
SQLDML_NotExp = Class(name="SQLDML_NotExp")
SQLDML_Expression = Class(name="SQLDML_Expression", is_abstract=True)
SQLDML_BinaryExp = Class(name="SQLDML_BinaryExp", is_abstract=True)
SQLDML_InExp = Class(name="SQLDML_InExp")
Predicate = Class(name="Predicate")
SQLDML_LikeExp = Class(name="SQLDML_LikeExp")
StringValueExp = Class(name="StringValueExp")
SQLDML_ColumnExp = Class(name="SQLDML_ColumnExp")
DataType = Class(name="DataType")
SQLDML_OperationExp = Class(name="SQLDML_OperationExp")
SQLDML_Predicate = Class(name="SQLDML_Predicate", is_abstract=True)
SQLDML_QueryPredicate = Class(name="SQLDML_QueryPredicate")
SQLDML_ListExp = Class(name="SQLDML_ListExp")
SQLDML_ValueExp = Class(name="SQLDML_ValueExp", is_abstract=True)
SQLDML_StringValueExp = Class(name="SQLDML_StringValueExp")
ValueExp = Class(name="ValueExp")
SQLDML_IntegerValueExp = Class(name="SQLDML_IntegerValueExp")
SQLDML_FunctionExp = Class(name="SQLDML_FunctionExp")
SQLDML_DataType = Class(name="SQLDML_DataType")

# SQLDML_LocatedElement class attributes and methods
SQLDML_LocatedElement_location: Property = Property(name="location", type=StringType)
SQLDML_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
SQLDML_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
SQLDML_LocatedElement.attributes={SQLDML_LocatedElement_commentsAfter, SQLDML_LocatedElement_commentsBefore, SQLDML_LocatedElement_location}

# SQLDML_Statement class attributes and methods

# SQLDML_ViewStatement class attributes and methods
SQLDML_ViewStatement_name: Property = Property(name="name", type=StringType)
SQLDML_ViewStatement.attributes={SQLDML_ViewStatement_name}

# SQLDML_SQLRoot class attributes and methods

# LocatedElement class attributes and methods

# Statement class attributes and methods

# SQLDML_QueryStmt class attributes and methods

# Table class attributes and methods

# ColumnExp class attributes and methods

# QueryStmt class attributes and methods

# SQLDML_InsertStmt class attributes and methods
SQLDML_InsertStmt_tableName: Property = Property(name="tableName", type=StringType)
SQLDML_InsertStmt.attributes={SQLDML_InsertStmt_tableName}

# Expression class attributes and methods

# SQLDML_Table class attributes and methods
SQLDML_Table_alias: Property = Property(name="alias", type=StringType)
SQLDML_Table.attributes={SQLDML_Table_alias}

# NamedElement class attributes and methods

# SQLDML_WhereClause class attributes and methods

# WhereClause class attributes and methods

# SQLDML_QueryStmtCol class attributes and methods

# SQLDML_QueryStmtAllCol class attributes and methods

# SQLDML_NamedElement class attributes and methods
SQLDML_NamedElement_name: Property = Property(name="name", type=StringType)
SQLDML_NamedElement.attributes={SQLDML_NamedElement_name}

# SQLDML_OrExp class attributes and methods

# BinaryExp class attributes and methods

# SQLDML_AndExp class attributes and methods

# SQLDML_NotExp class attributes and methods
SQLDML_NotExp_opName: Property = Property(name="opName", type=StringType)
SQLDML_NotExp.attributes={SQLDML_NotExp_opName}

# SQLDML_Expression class attributes and methods

# SQLDML_BinaryExp class attributes and methods
SQLDML_BinaryExp_opName: Property = Property(name="opName", type=StringType)
SQLDML_BinaryExp.attributes={SQLDML_BinaryExp_opName}

# SQLDML_InExp class attributes and methods
SQLDML_InExp_columnName: Property = Property(name="columnName", type=StringType)
SQLDML_InExp.attributes={SQLDML_InExp_columnName}

# Predicate class attributes and methods

# SQLDML_LikeExp class attributes and methods
SQLDML_LikeExp_columnName: Property = Property(name="columnName", type=StringType)
SQLDML_LikeExp.attributes={SQLDML_LikeExp_columnName}

# StringValueExp class attributes and methods

# SQLDML_ColumnExp class attributes and methods
SQLDML_ColumnExp_alias: Property = Property(name="alias", type=StringType)
SQLDML_ColumnExp.attributes={SQLDML_ColumnExp_alias}

# DataType class attributes and methods

# SQLDML_OperationExp class attributes and methods
SQLDML_OperationExp_optName: Property = Property(name="optName", type=StringType)
SQLDML_OperationExp.attributes={SQLDML_OperationExp_optName}

# SQLDML_Predicate class attributes and methods

# SQLDML_QueryPredicate class attributes and methods

# SQLDML_ListExp class attributes and methods

# SQLDML_ValueExp class attributes and methods

# SQLDML_StringValueExp class attributes and methods
SQLDML_StringValueExp_aValue: Property = Property(name="aValue", type=StringType)
SQLDML_StringValueExp.attributes={SQLDML_StringValueExp_aValue}

# ValueExp class attributes and methods

# SQLDML_IntegerValueExp class attributes and methods
SQLDML_IntegerValueExp_aValue: Property = Property(name="aValue", type=StringType)
SQLDML_IntegerValueExp.attributes={SQLDML_IntegerValueExp_aValue}

# SQLDML_FunctionExp class attributes and methods
SQLDML_FunctionExp_name: Property = Property(name="name", type=StringType)
SQLDML_FunctionExp.attributes={SQLDML_FunctionExp_name}

# SQLDML_DataType class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="Statement", type=SQLDML_SQLRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_SQLRoot", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables5: BinaryAssociation = BinaryAssociation(
    name="tables5",
    ends={
        Property(name="Table", type=SQLDML_QueryStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_QueryStmt", type=Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="ColumnExp", type=SQLDML_ViewStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_ViewStatement", type=ColumnExp, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
query2: BinaryAssociation = BinaryAssociation(
    name="query2",
    ends={
        Property(name="QueryStmt", type=SQLDML_ViewStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_ViewStatement3", type=QueryStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values4: BinaryAssociation = BinaryAssociation(
    name="values4",
    ends={
        Property(name="Expression", type=SQLDML_InsertStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_InsertStmt", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition6: BinaryAssociation = BinaryAssociation(
    name="condition6",
    ends={
        Property(name="WhereClause", type=SQLDML_QueryStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_QueryStmt7", type=WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns8: BinaryAssociation = BinaryAssociation(
    name="columns8",
    ends={
        Property(name="Expression9", type=SQLDML_QueryStmtCol, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_QueryStmtCol", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="Expression11", type=SQLDML_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_WhereClause", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp12: BinaryAssociation = BinaryAssociation(
    name="leftExp12",
    ends={
        Property(name="Expression13", type=SQLDML_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_BinaryExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp14: BinaryAssociation = BinaryAssociation(
    name="rightExp14",
    ends={
        Property(name="Expression16", type=SQLDML_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_BinaryExp15", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements23: BinaryAssociation = BinaryAssociation(
    name="elements23",
    ends={
        Property(name="Predicate", type=SQLDML_InExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_InExp", type=Predicate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExp17: BinaryAssociation = BinaryAssociation(
    name="valueExp17",
    ends={
        Property(name="Expression18", type=SQLDML_NotExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_NotExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unused19: BinaryAssociation = BinaryAssociation(
    name="unused19",
    ends={
        Property(name="Expression21", type=SQLDML_NotExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_NotExp20", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression22: BinaryAssociation = BinaryAssociation(
    name="expression22",
    ends={
        Property(name="StringValueExp", type=SQLDML_LikeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_LikeExp", type=StringValueExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
query24: BinaryAssociation = BinaryAssociation(
    name="query24",
    ends={
        Property(name="QueryStmt25", type=SQLDML_QueryPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_QueryPredicate", type=QueryStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements29: BinaryAssociation = BinaryAssociation(
    name="elements29",
    ends={
        Property(name="Expression30", type=SQLDML_ListExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_ListExp", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="DataType", type=SQLDML_ColumnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_ColumnExp", type=DataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="DataType28", type=SQLDML_ValueExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_ValueExp", type=DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments31: BinaryAssociation = BinaryAssociation(
    name="arguments31",
    ends={
        Property(name="Expression32", type=SQLDML_FunctionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDML_FunctionExp", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SQLDML_Statement_LocatedElement = Generalization(general=LocatedElement, specific=SQLDML_Statement)
gen_SQLDML_ViewStatement_Statement = Generalization(general=Statement, specific=SQLDML_ViewStatement)
gen_SQLDML_SQLRoot_LocatedElement = Generalization(general=LocatedElement, specific=SQLDML_SQLRoot)
gen_SQLDML_QueryStmt_Statement = Generalization(general=Statement, specific=SQLDML_QueryStmt)
gen_SQLDML_InsertStmt_Statement = Generalization(general=Statement, specific=SQLDML_InsertStmt)
gen_SQLDML_Table_NamedElement = Generalization(general=NamedElement, specific=SQLDML_Table)
gen_SQLDML_WhereClause_LocatedElement = Generalization(general=LocatedElement, specific=SQLDML_WhereClause)
gen_SQLDML_QueryStmtCol_QueryStmt = Generalization(general=QueryStmt, specific=SQLDML_QueryStmtCol)
gen_SQLDML_QueryStmtAllCol_QueryStmt = Generalization(general=QueryStmt, specific=SQLDML_QueryStmtAllCol)
gen_SQLDML_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=SQLDML_NamedElement)
gen_SQLDML_OrExp_BinaryExp = Generalization(general=BinaryExp, specific=SQLDML_OrExp)
gen_SQLDML_AndExp_BinaryExp = Generalization(general=BinaryExp, specific=SQLDML_AndExp)
gen_SQLDML_NotExp_Expression = Generalization(general=Expression, specific=SQLDML_NotExp)
gen_SQLDML_Expression_LocatedElement = Generalization(general=LocatedElement, specific=SQLDML_Expression)
gen_SQLDML_BinaryExp_Expression = Generalization(general=Expression, specific=SQLDML_BinaryExp)
gen_SQLDML_InExp_Expression = Generalization(general=Expression, specific=SQLDML_InExp)
gen_SQLDML_LikeExp_Expression = Generalization(general=Expression, specific=SQLDML_LikeExp)
gen_SQLDML_ColumnExp_Predicate = Generalization(general=Predicate, specific=SQLDML_ColumnExp)
gen_SQLDML_ColumnExp_NamedElement = Generalization(general=NamedElement, specific=SQLDML_ColumnExp)
gen_SQLDML_OperationExp_BinaryExp = Generalization(general=BinaryExp, specific=SQLDML_OperationExp)
gen_SQLDML_Predicate_Expression = Generalization(general=Expression, specific=SQLDML_Predicate)
gen_SQLDML_QueryPredicate_Expression = Generalization(general=Expression, specific=SQLDML_QueryPredicate)
gen_SQLDML_ListExp_Predicate = Generalization(general=Predicate, specific=SQLDML_ListExp)
gen_SQLDML_ValueExp_Predicate = Generalization(general=Predicate, specific=SQLDML_ValueExp)
gen_SQLDML_StringValueExp_ValueExp = Generalization(general=ValueExp, specific=SQLDML_StringValueExp)
gen_SQLDML_IntegerValueExp_ValueExp = Generalization(general=ValueExp, specific=SQLDML_IntegerValueExp)
gen_SQLDML_FunctionExp_Predicate = Generalization(general=Predicate, specific=SQLDML_FunctionExp)
gen_SQLDML_DataType_NamedElement = Generalization(general=NamedElement, specific=SQLDML_DataType)

# Domain Model
domain_model = DomainModel(
    name="SQLDML",
    types={SQLDML_LocatedElement, SQLDML_Statement, SQLDML_ViewStatement, SQLDML_SQLRoot, LocatedElement, Statement, SQLDML_QueryStmt, Table, ColumnExp, QueryStmt, SQLDML_InsertStmt, Expression, SQLDML_Table, NamedElement, SQLDML_WhereClause, WhereClause, SQLDML_QueryStmtCol, SQLDML_QueryStmtAllCol, SQLDML_NamedElement, SQLDML_OrExp, BinaryExp, SQLDML_AndExp, SQLDML_NotExp, SQLDML_Expression, SQLDML_BinaryExp, SQLDML_InExp, Predicate, SQLDML_LikeExp, StringValueExp, SQLDML_ColumnExp, DataType, SQLDML_OperationExp, SQLDML_Predicate, SQLDML_QueryPredicate, SQLDML_ListExp, SQLDML_ValueExp, SQLDML_StringValueExp, ValueExp, SQLDML_IntegerValueExp, SQLDML_FunctionExp, SQLDML_DataType},
    associations={statements0, tables5, columns1, query2, values4, condition6, columns8, expression10, leftExp12, rightExp14, elements23, valueExp17, unused19, expression22, query24, elements29, type26, type27, arguments31},
    generalizations={gen_SQLDML_Statement_LocatedElement, gen_SQLDML_ViewStatement_Statement, gen_SQLDML_SQLRoot_LocatedElement, gen_SQLDML_QueryStmt_Statement, gen_SQLDML_InsertStmt_Statement, gen_SQLDML_Table_NamedElement, gen_SQLDML_WhereClause_LocatedElement, gen_SQLDML_QueryStmtCol_QueryStmt, gen_SQLDML_QueryStmtAllCol_QueryStmt, gen_SQLDML_NamedElement_LocatedElement, gen_SQLDML_OrExp_BinaryExp, gen_SQLDML_AndExp_BinaryExp, gen_SQLDML_NotExp_Expression, gen_SQLDML_Expression_LocatedElement, gen_SQLDML_BinaryExp_Expression, gen_SQLDML_InExp_Expression, gen_SQLDML_LikeExp_Expression, gen_SQLDML_ColumnExp_Predicate, gen_SQLDML_ColumnExp_NamedElement, gen_SQLDML_OperationExp_BinaryExp, gen_SQLDML_Predicate_Expression, gen_SQLDML_QueryPredicate_Expression, gen_SQLDML_ListExp_Predicate, gen_SQLDML_ValueExp_Predicate, gen_SQLDML_StringValueExp_ValueExp, gen_SQLDML_IntegerValueExp_ValueExp, gen_SQLDML_FunctionExp_Predicate, gen_SQLDML_DataType_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
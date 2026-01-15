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

# Enumerations
XFunction: Enumeration = Enumeration(
    name="XFunction",
    literals={
            EnumerationLiteral(name="xin"),
			EnumerationLiteral(name="xnotin"),
			EnumerationLiteral(name="xeq"),
			EnumerationLiteral(name="xnoteq"),
			EnumerationLiteral(name="xls"),
			EnumerationLiteral(name="xgt"),
			EnumerationLiteral(name="xlsr"),
			EnumerationLiteral(name="xgtl"),
			EnumerationLiteral(name="xbwn"),
			EnumerationLiteral(name="xbwnc"),
			EnumerationLiteral(name="xbwnl"),
			EnumerationLiteral(name="xbwnr")
    }
)

# Classes
sql_Model = Class(name="sql::Model")
sql_SelectQuery = Class(name="sql::SelectQuery")
sql_OrOrderByColumn = Class(name="sql::OrOrderByColumn")
sql_Select = Class(name="sql::Select")
SelectQuery = Class(name="SelectQuery")
sql_OrColumn = Class(name="sql::OrColumn")
sql_OrTable = Class(name="sql::OrTable")
sql_OrExpr = Class(name="sql::OrExpr")
sql_OrGroupByColumn = Class(name="sql::OrGroupByColumn")
sql_SelectSubSet = Class(name="sql::SelectSubSet")
sql_ColumnOrAlias = Class(name="sql::ColumnOrAlias")
OrColumn = Class(name="OrColumn")
sql_Operands = Class(name="sql::Operands")
sql_DbObjectName = Class(name="sql::DbObjectName")
sql_DbObjectNameAll = Class(name="sql::DbObjectNameAll")
sql_FromTable = Class(name="sql::FromTable")
OrTable = Class(name="OrTable")
sql_TableOrAlias = Class(name="sql::TableOrAlias")
sql_FromTableJoin = Class(name="sql::FromTableJoin")
sql_TableFull = Class(name="sql::TableFull")
sql_ColumnFull = Class(name="sql::ColumnFull")
sql_SubQueryOperand = Class(name="sql::SubQueryOperand")
ColumnFull = Class(name="ColumnFull")
TableFull = Class(name="TableFull")
sql_OrderByColumnFull = Class(name="sql::OrderByColumnFull")
OrOrderByColumn = Class(name="OrOrderByColumn")
sql_GroupByColumnFull = Class(name="sql::GroupByColumnFull")
OrGroupByColumn = Class(name="OrGroupByColumn")
sql_FullExpression = Class(name="sql::FullExpression")
OrExpr = Class(name="OrExpr")
sql_ExprGroup = Class(name="sql::ExprGroup")
sql_XExpr = Class(name="sql::XExpr")
sql_InOper = Class(name="sql::InOper")
sql_Between = Class(name="sql::Between")
sql_Like = Class(name="sql::Like")
sql_Comparison = Class(name="sql::Comparison")
sql_Prms = Class(name="sql::Prms")
sql_JRParameter = Class(name="sql::JRParameter")
Prms = Class(name="Prms")
sql_LikeOperand = Class(name="sql::LikeOperand")
sql_OpFunction = Class(name="sql::OpFunction")
sql_OpFunctionCast = Class(name="sql::OpFunctionCast")
sql_OperandList = Class(name="sql::OperandList")
sql_POperand = Class(name="sql::POperand")
OpFunctionArgAgregate = Class(name="OpFunctionArgAgregate")
sql_Operand = Class(name="sql::Operand")
sql_ColumnOperand = Class(name="sql::ColumnOperand")
sql_SQLCaseOperand = Class(name="sql::SQLCaseOperand")
sql_ExpOperand = Class(name="sql::ExpOperand")
sql_ScalarOperand = Class(name="sql::ScalarOperand")
sql_OpFunctionArg = Class(name="sql::OpFunctionArg")
sql_OpFunctionArgOperand = Class(name="sql::OpFunctionArgOperand")
OpFunctionArg = Class(name="OpFunctionArg")
sql_OpFunctionArgAgregate = Class(name="sql::OpFunctionArgAgregate")
OperandList = Class(name="OperandList")
sql_SQLCaseWhens = Class(name="sql::SQLCaseWhens")
sql_SqlCaseWhen = Class(name="sql::SqlCaseWhen")
SQLCaseWhens = Class(name="SQLCaseWhens")
sql_Plus = Class(name="sql::Plus")
Operands = Class(name="Operands")
sql_Minus = Class(name="sql::Minus")
sql_Star = Class(name="sql::Star")
sql_Col = Class(name="sql::Col")
sql_tbls = Class(name="sql::tbls")
sql_OpList = Class(name="sql::OpList")
sql_Div = Class(name="sql::Div")
sql_Concat = Class(name="sql::Concat")
sql_OpFList = Class(name="sql::OpFList")
sql_WhenList = Class(name="sql::WhenList")

# sql_Model class attributes and methods

# sql_SelectQuery class attributes and methods

# sql_OrOrderByColumn class attributes and methods

# sql_Select class attributes and methods
sql_Select_select: Property = Property(name="select", type=StringType)
sql_Select.attributes={sql_Select_select}

# SelectQuery class attributes and methods

# sql_OrColumn class attributes and methods

# sql_OrTable class attributes and methods

# sql_OrExpr class attributes and methods

# sql_OrGroupByColumn class attributes and methods

# sql_SelectSubSet class attributes and methods
sql_SelectSubSet_op: Property = Property(name="op", type=StringType)
sql_SelectSubSet_all: Property = Property(name="all", type=StringType)
sql_SelectSubSet.attributes={sql_SelectSubSet_op, sql_SelectSubSet_all}

# sql_ColumnOrAlias class attributes and methods
sql_ColumnOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_ColumnOrAlias_allCols: Property = Property(name="allCols", type=StringType)
sql_ColumnOrAlias.attributes={sql_ColumnOrAlias_allCols, sql_ColumnOrAlias_alias}

# OrColumn class attributes and methods

# sql_Operands class attributes and methods

# sql_DbObjectName class attributes and methods
sql_DbObjectName_dbname: Property = Property(name="dbname", type=StringType)
sql_DbObjectName.attributes={sql_DbObjectName_dbname}

# sql_DbObjectNameAll class attributes and methods
sql_DbObjectNameAll_dbname: Property = Property(name="dbname", type=StringType)
sql_DbObjectNameAll.attributes={sql_DbObjectNameAll_dbname}

# sql_FromTable class attributes and methods

# OrTable class attributes and methods

# sql_TableOrAlias class attributes and methods
sql_TableOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_TableOrAlias.attributes={sql_TableOrAlias_alias}

# sql_FromTableJoin class attributes and methods
sql_FromTableJoin_join: Property = Property(name="join", type=StringType)
sql_FromTableJoin.attributes={sql_FromTableJoin_join}

# sql_TableFull class attributes and methods

# sql_ColumnFull class attributes and methods

# sql_SubQueryOperand class attributes and methods

# ColumnFull class attributes and methods

# TableFull class attributes and methods

# sql_OrderByColumnFull class attributes and methods
sql_OrderByColumnFull_colOrderInt: Property = Property(name="colOrderInt", type=IntegerType)
sql_OrderByColumnFull_direction: Property = Property(name="direction", type=StringType)
sql_OrderByColumnFull.attributes={sql_OrderByColumnFull_colOrderInt, sql_OrderByColumnFull_direction}

# OrOrderByColumn class attributes and methods

# sql_GroupByColumnFull class attributes and methods

# OrGroupByColumn class attributes and methods

# sql_FullExpression class attributes and methods
sql_FullExpression_c: Property = Property(name="c", type=StringType)
sql_FullExpression_notPrm: Property = Property(name="notPrm", type=StringType)
sql_FullExpression_isnull: Property = Property(name="isnull", type=StringType)
sql_FullExpression.attributes={sql_FullExpression_c, sql_FullExpression_notPrm, sql_FullExpression_isnull}

# OrExpr class attributes and methods

# sql_ExprGroup class attributes and methods

# sql_XExpr class attributes and methods
sql_XExpr_xf: Property = Property(name="xf", type=StringType)
sql_XExpr.attributes={sql_XExpr_xf}

# sql_InOper class attributes and methods
sql_InOper_op: Property = Property(name="op", type=StringType)
sql_InOper.attributes={sql_InOper_op}

# sql_Between class attributes and methods
sql_Between_opBetween: Property = Property(name="opBetween", type=StringType)
sql_Between.attributes={sql_Between_opBetween}

# sql_Like class attributes and methods
sql_Like_opLike: Property = Property(name="opLike", type=StringType)
sql_Like.attributes={sql_Like_opLike}

# sql_Comparison class attributes and methods
sql_Comparison_operator: Property = Property(name="operator", type=StringType)
sql_Comparison_subOperator: Property = Property(name="subOperator", type=StringType)
sql_Comparison.attributes={sql_Comparison_subOperator, sql_Comparison_operator}

# sql_Prms class attributes and methods

# sql_JRParameter class attributes and methods
sql_JRParameter_jrprm: Property = Property(name="jrprm", type=StringType)
sql_JRParameter.attributes={sql_JRParameter_jrprm}

# Prms class attributes and methods

# sql_LikeOperand class attributes and methods
sql_LikeOperand_op2: Property = Property(name="op2", type=StringType)
sql_LikeOperand.attributes={sql_LikeOperand_op2}

# sql_OpFunction class attributes and methods
sql_OpFunction_fname: Property = Property(name="fname", type=StringType)
sql_OpFunction.attributes={sql_OpFunction_fname}

# sql_OpFunctionCast class attributes and methods
sql_OpFunctionCast_type: Property = Property(name="type", type=StringType)
sql_OpFunctionCast_p: Property = Property(name="p", type=IntegerType)
sql_OpFunctionCast_p2: Property = Property(name="p2", type=IntegerType)
sql_OpFunctionCast.attributes={sql_OpFunctionCast_p2, sql_OpFunctionCast_p, sql_OpFunctionCast_type}

# sql_OperandList class attributes and methods

# sql_POperand class attributes and methods
sql_POperand_prm: Property = Property(name="prm", type=StringType)
sql_POperand.attributes={sql_POperand_prm}

# OpFunctionArgAgregate class attributes and methods

# sql_Operand class attributes and methods

# sql_ColumnOperand class attributes and methods

# sql_SQLCaseOperand class attributes and methods

# sql_ExpOperand class attributes and methods
sql_ExpOperand_prm: Property = Property(name="prm", type=StringType)
sql_ExpOperand.attributes={sql_ExpOperand_prm}

# sql_ScalarOperand class attributes and methods
sql_ScalarOperand_soint: Property = Property(name="soint", type=IntegerType)
sql_ScalarOperand_sostr: Property = Property(name="sostr", type=StringType)
sql_ScalarOperand_sodbl: Property = Property(name="sodbl", type=StringType)
sql_ScalarOperand_sodate: Property = Property(name="sodate", type=DateType)
sql_ScalarOperand_sotime: Property = Property(name="sotime", type=DateType)
sql_ScalarOperand_sodt: Property = Property(name="sodt", type=DateType)
sql_ScalarOperand.attributes={sql_ScalarOperand_sodbl, sql_ScalarOperand_sotime, sql_ScalarOperand_sostr, sql_ScalarOperand_soint, sql_ScalarOperand_sodate, sql_ScalarOperand_sodt}

# sql_OpFunctionArg class attributes and methods

# sql_OpFunctionArgOperand class attributes and methods

# OpFunctionArg class attributes and methods

# sql_OpFunctionArgAgregate class attributes and methods

# OperandList class attributes and methods

# sql_SQLCaseWhens class attributes and methods

# sql_SqlCaseWhen class attributes and methods

# SQLCaseWhens class attributes and methods

# sql_Plus class attributes and methods

# Operands class attributes and methods

# sql_Minus class attributes and methods

# sql_Star class attributes and methods

# sql_Col class attributes and methods

# sql_tbls class attributes and methods

# sql_OpList class attributes and methods

# sql_Div class attributes and methods

# sql_Concat class attributes and methods

# sql_OpFList class attributes and methods

# sql_WhenList class attributes and methods

# Relationships
query0: BinaryAssociation = BinaryAssociation(
    name="query0",
    ends={
        Property(name="sql_SelectQuery", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderByEntry1: BinaryAssociation = BinaryAssociation(
    name="orderByEntry1",
    ends={
        Property(name="sql_OrOrderByColumn", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model2", type=sql_OrOrderByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query3: BinaryAssociation = BinaryAssociation(
    name="query3",
    ends={
        Property(name="sql_Select", type=sql_SelectSubSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectSubSet", type=sql_Select, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op4: BinaryAssociation = BinaryAssociation(
    name="op4",
    ends={
        Property(name="sql_SelectSubSet6", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select5", type=sql_SelectSubSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols7: BinaryAssociation = BinaryAssociation(
    name="cols7",
    ends={
        Property(name="sql_OrColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select8", type=sql_OrColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbl9: BinaryAssociation = BinaryAssociation(
    name="tbl9",
    ends={
        Property(name="sql_OrTable", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select10", type=sql_OrTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression11: BinaryAssociation = BinaryAssociation(
    name="whereExpression11",
    ends={
        Property(name="sql_OrExpr", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select12", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
havingEntry15: BinaryAssociation = BinaryAssociation(
    name="havingEntry15",
    ends={
        Property(name="sql_OrExpr17", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select16", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries18: BinaryAssociation = BinaryAssociation(
    name="entries18",
    ends={
        Property(name="sql_ColumnOrAlias", type=sql_OrColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrColumn19", type=sql_ColumnOrAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce20: BinaryAssociation = BinaryAssociation(
    name="ce20",
    ends={
        Property(name="sql_Operands", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias21", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias22: BinaryAssociation = BinaryAssociation(
    name="colAlias22",
    ends={
        Property(name="sql_DbObjectName", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias23", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dbAllCols24: BinaryAssociation = BinaryAssociation(
    name="dbAllCols24",
    ends={
        Property(name="sql_DbObjectNameAll", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias25", type=sql_DbObjectNameAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByEntry13: BinaryAssociation = BinaryAssociation(
    name="groupByEntry13",
    ends={
        Property(name="sql_OrGroupByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select14", type=sql_OrGroupByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries26: BinaryAssociation = BinaryAssociation(
    name="entries26",
    ends={
        Property(name="sql_FromTable", type=sql_OrTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrTable27", type=sql_FromTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table28: BinaryAssociation = BinaryAssociation(
    name="table28",
    ends={
        Property(name="sql_TableOrAlias", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable29", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fjoin30: BinaryAssociation = BinaryAssociation(
    name="fjoin30",
    ends={
        Property(name="sql_FromTableJoin", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable31", type=sql_FromTableJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onTable32: BinaryAssociation = BinaryAssociation(
    name="onTable32",
    ends={
        Property(name="sql_TableOrAlias34", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin33", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinExpr35: BinaryAssociation = BinaryAssociation(
    name="joinExpr35",
    ends={
        Property(name="sql_OrExpr37", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin36", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq40: BinaryAssociation = BinaryAssociation(
    name="sq40",
    ends={
        Property(name="sql_SubQueryOperand", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias41", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tblAlias42: BinaryAssociation = BinaryAssociation(
    name="tblAlias42",
    ends={
        Property(name="sql_DbObjectName44", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias43", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries45: BinaryAssociation = BinaryAssociation(
    name="entries45",
    ends={
        Property(name="sql_OrderByColumnFull", type=sql_OrOrderByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrOrderByColumn46", type=sql_OrderByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colOrder47: BinaryAssociation = BinaryAssociation(
    name="colOrder47",
    ends={
        Property(name="sql_ColumnFull", type=sql_OrderByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByColumnFull48", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tfull38: BinaryAssociation = BinaryAssociation(
    name="tfull38",
    ends={
        Property(name="sql_TableFull", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias39", type=sql_TableFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries49: BinaryAssociation = BinaryAssociation(
    name="entries49",
    ends={
        Property(name="sql_GroupByColumnFull", type=sql_OrGroupByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrGroupByColumn50", type=sql_GroupByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colGrBy51: BinaryAssociation = BinaryAssociation(
    name="colGrBy51",
    ends={
        Property(name="sql_ColumnFull53", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull52", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries54: BinaryAssociation = BinaryAssociation(
    name="entries54",
    ends={
        Property(name="sql_FullExpression", type=sql_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrExpr55", type=sql_FullExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
efrag57: BinaryAssociation = BinaryAssociation(
    name="efrag57",
    ends={
        Property(name="sql_FullExpression58", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression56", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expgroup59: BinaryAssociation = BinaryAssociation(
    name="expgroup59",
    ends={
        Property(name="sql_ExprGroup", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression60", type=sql_ExprGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp62: BinaryAssociation = BinaryAssociation(
    name="exp62",
    ends={
        Property(name="sql_FullExpression63", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression61", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xexp64: BinaryAssociation = BinaryAssociation(
    name="xexp64",
    ends={
        Property(name="sql_XExpr", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression65", type=sql_XExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op166: BinaryAssociation = BinaryAssociation(
    name="op166",
    ends={
        Property(name="sql_Operands68", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression67", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in69: BinaryAssociation = BinaryAssociation(
    name="in69",
    ends={
        Property(name="sql_InOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression70", type=sql_InOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
between71: BinaryAssociation = BinaryAssociation(
    name="between71",
    ends={
        Property(name="sql_Between", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression72", type=sql_Between, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
like73: BinaryAssociation = BinaryAssociation(
    name="like73",
    ends={
        Property(name="sql_Like", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression74", type=sql_Like, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comp75: BinaryAssociation = BinaryAssociation(
    name="comp75",
    ends={
        Property(name="sql_Comparison", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression76", type=sql_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col80: BinaryAssociation = BinaryAssociation(
    name="col80",
    ends={
        Property(name="sql_Operands82", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr81", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prm83: BinaryAssociation = BinaryAssociation(
    name="prm83",
    ends={
        Property(name="sql_Prms", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr84", type=sql_Prms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries85: BinaryAssociation = BinaryAssociation(
    name="entries85",
    ends={
        Property(name="sql_JRParameter", type=sql_Prms, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Prms86", type=sql_JRParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op287: BinaryAssociation = BinaryAssociation(
    name="op287",
    ends={
        Property(name="sql_Operands89", type=sql_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Comparison88", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr77: BinaryAssociation = BinaryAssociation(
    name="expr77",
    ends={
        Property(name="sql_OrExpr79", type=sql_ExprGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExprGroup78", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op290: BinaryAssociation = BinaryAssociation(
    name="op290",
    ends={
        Property(name="sql_LikeOperand", type=sql_Like, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Like91", type=sql_LikeOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fop292: BinaryAssociation = BinaryAssociation(
    name="fop292",
    ends={
        Property(name="sql_OpFunction", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand93", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast94: BinaryAssociation = BinaryAssociation(
    name="fcast94",
    ends={
        Property(name="sql_OpFunctionCast", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand95", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op296: BinaryAssociation = BinaryAssociation(
    name="op296",
    ends={
        Property(name="sql_Operands98", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between97", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op399: BinaryAssociation = BinaryAssociation(
    name="op399",
    ends={
        Property(name="sql_Operands101", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between100", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sqlcase129: BinaryAssociation = BinaryAssociation(
    name="sqlcase129",
    ends={
        Property(name="sql_SQLCaseOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand130", type=sql_SQLCaseOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList105: BinaryAssociation = BinaryAssociation(
    name="opList105",
    ends={
        Property(name="sql_OperandList", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper106", type=sql_OperandList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1107: BinaryAssociation = BinaryAssociation(
    name="op1107",
    ends={
        Property(name="sql_Operand", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands108", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left110: BinaryAssociation = BinaryAssociation(
    name="left110",
    ends={
        Property(name="sql_Operands111", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands109", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right112: BinaryAssociation = BinaryAssociation(
    name="right112",
    ends={
        Property(name="sql_Operand114", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands113", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column115: BinaryAssociation = BinaryAssociation(
    name="column115",
    ends={
        Property(name="sql_ColumnOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand116", type=sql_ColumnOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xop118: BinaryAssociation = BinaryAssociation(
    name="xop118",
    ends={
        Property(name="sql_Operand119", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand117", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subq120: BinaryAssociation = BinaryAssociation(
    name="subq120",
    ends={
        Property(name="sql_SubQueryOperand122", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand121", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast123: BinaryAssociation = BinaryAssociation(
    name="fcast123",
    ends={
        Property(name="sql_OpFunctionCast125", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand124", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func126: BinaryAssociation = BinaryAssociation(
    name="func126",
    ends={
        Property(name="sql_OpFunction128", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand127", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery102: BinaryAssociation = BinaryAssociation(
    name="subquery102",
    ends={
        Property(name="sql_SubQueryOperand104", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper103", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param131: BinaryAssociation = BinaryAssociation(
    name="param131",
    ends={
        Property(name="sql_POperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand132", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfull143: BinaryAssociation = BinaryAssociation(
    name="cfull143",
    ends={
        Property(name="sql_ColumnFull145", type=sql_ColumnOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOperand144", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eparam133: BinaryAssociation = BinaryAssociation(
    name="eparam133",
    ends={
        Property(name="sql_ExpOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand134", type=sql_ExpOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scalar135: BinaryAssociation = BinaryAssociation(
    name="scalar135",
    ends={
        Property(name="sql_ScalarOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand136", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args137: BinaryAssociation = BinaryAssociation(
    name="args137",
    ends={
        Property(name="sql_OpFunctionArg", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction138", type=sql_OpFunctionArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op139: BinaryAssociation = BinaryAssociation(
    name="op139",
    ends={
        Property(name="sql_OpFunctionArgAgregate", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionArgOperand", type=sql_OpFunctionArgAgregate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op140: BinaryAssociation = BinaryAssociation(
    name="op140",
    ends={
        Property(name="sql_Operands142", type=sql_OpFunctionCast, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionCast141", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eexp159: BinaryAssociation = BinaryAssociation(
    name="eexp159",
    ends={
        Property(name="sql_Operands161", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen160", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sel146: BinaryAssociation = BinaryAssociation(
    name="sel146",
    ends={
        Property(name="sql_SelectQuery148", type=sql_SubQueryOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SubQueryOperand147", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr149: BinaryAssociation = BinaryAssociation(
    name="expr149",
    ends={
        Property(name="sql_OrExpr151", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand150", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when152: BinaryAssociation = BinaryAssociation(
    name="when152",
    ends={
        Property(name="sql_SQLCaseWhens", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand153", type=sql_SQLCaseWhens, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr154: BinaryAssociation = BinaryAssociation(
    name="expr154",
    ends={
        Property(name="sql_OrExpr155", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
texp156: BinaryAssociation = BinaryAssociation(
    name="texp156",
    ends={
        Property(name="sql_Operands158", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen157", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries162: BinaryAssociation = BinaryAssociation(
    name="entries162",
    ends={
        Property(name="sql_DbObjectName163", type=sql_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Col", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries164: BinaryAssociation = BinaryAssociation(
    name="entries164",
    ends={
        Property(name="sql_DbObjectName165", type=sql_tbls, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_tbls", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries166: BinaryAssociation = BinaryAssociation(
    name="entries166",
    ends={
        Property(name="sql_ScalarOperand167", type=sql_OpList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpList", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries168: BinaryAssociation = BinaryAssociation(
    name="entries168",
    ends={
        Property(name="sql_OpFunctionArgOperand169", type=sql_OpFList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFList", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries170: BinaryAssociation = BinaryAssociation(
    name="entries170",
    ends={
        Property(name="sql_SqlCaseWhen171", type=sql_WhenList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WhenList", type=sql_SqlCaseWhen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sql_Select_SelectQuery = Generalization(general=SelectQuery, specific=sql_Select)
gen_sql_ColumnOrAlias_OrColumn = Generalization(general=OrColumn, specific=sql_ColumnOrAlias)
gen_sql_FromTable_OrTable = Generalization(general=OrTable, specific=sql_FromTable)
gen_sql_DbObjectName_ColumnFull = Generalization(general=ColumnFull, specific=sql_DbObjectName)
gen_sql_DbObjectName_TableFull = Generalization(general=TableFull, specific=sql_DbObjectName)
gen_sql_OrderByColumnFull_OrOrderByColumn = Generalization(general=OrOrderByColumn, specific=sql_OrderByColumnFull)
gen_sql_GroupByColumnFull_OrGroupByColumn = Generalization(general=OrGroupByColumn, specific=sql_GroupByColumnFull)
gen_sql_FullExpression_OrExpr = Generalization(general=OrExpr, specific=sql_FullExpression)
gen_sql_JRParameter_Prms = Generalization(general=Prms, specific=sql_JRParameter)
gen_sql_Operands_OpFunctionArgAgregate = Generalization(general=OpFunctionArgAgregate, specific=sql_Operands)
gen_sql_OpFunctionArgOperand_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFunctionArgOperand)
gen_sql_ScalarOperand_OperandList = Generalization(general=OperandList, specific=sql_ScalarOperand)
gen_sql_SqlCaseWhen_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_SqlCaseWhen)
gen_sql_Plus_Operands = Generalization(general=Operands, specific=sql_Plus)
gen_sql_Minus_Operands = Generalization(general=Operands, specific=sql_Minus)
gen_sql_Col_ColumnFull = Generalization(general=ColumnFull, specific=sql_Col)
gen_sql_tbls_TableFull = Generalization(general=TableFull, specific=sql_tbls)
gen_sql_OpList_OperandList = Generalization(general=OperandList, specific=sql_OpList)
gen_sql_Star_Operands = Generalization(general=Operands, specific=sql_Star)
gen_sql_Div_Operands = Generalization(general=Operands, specific=sql_Div)
gen_sql_Concat_Operands = Generalization(general=Operands, specific=sql_Concat)
gen_sql_OpFList_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFList)
gen_sql_WhenList_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_WhenList)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Model, sql_SelectQuery, sql_OrOrderByColumn, sql_Select, SelectQuery, sql_OrColumn, sql_OrTable, sql_OrExpr, sql_OrGroupByColumn, sql_SelectSubSet, sql_ColumnOrAlias, OrColumn, sql_Operands, sql_DbObjectName, sql_DbObjectNameAll, sql_FromTable, OrTable, sql_TableOrAlias, sql_FromTableJoin, sql_TableFull, sql_ColumnFull, sql_SubQueryOperand, ColumnFull, TableFull, sql_OrderByColumnFull, OrOrderByColumn, sql_GroupByColumnFull, OrGroupByColumn, sql_FullExpression, OrExpr, sql_ExprGroup, sql_XExpr, sql_InOper, sql_Between, sql_Like, sql_Comparison, sql_Prms, sql_JRParameter, Prms, sql_LikeOperand, sql_OpFunction, sql_OpFunctionCast, sql_OperandList, sql_POperand, OpFunctionArgAgregate, sql_Operand, sql_ColumnOperand, sql_SQLCaseOperand, sql_ExpOperand, sql_ScalarOperand, sql_OpFunctionArg, sql_OpFunctionArgOperand, OpFunctionArg, sql_OpFunctionArgAgregate, OperandList, sql_SQLCaseWhens, sql_SqlCaseWhen, SQLCaseWhens, sql_Plus, Operands, sql_Minus, sql_Star, sql_Col, sql_tbls, sql_OpList, sql_Div, sql_Concat, sql_OpFList, sql_WhenList, XFunction},
    associations={query0, orderByEntry1, query3, op4, cols7, tbl9, whereExpression11, havingEntry15, entries18, ce20, colAlias22, dbAllCols24, groupByEntry13, entries26, table28, fjoin30, onTable32, joinExpr35, sq40, tblAlias42, entries45, colOrder47, tfull38, entries49, colGrBy51, entries54, efrag57, expgroup59, exp62, xexp64, op166, in69, between71, like73, comp75, col80, prm83, entries85, op287, expr77, op290, fop292, fcast94, op296, op399, sqlcase129, opList105, op1107, left110, right112, column115, xop118, subq120, fcast123, func126, subquery102, param131, cfull143, eparam133, scalar135, args137, op139, op140, eexp159, sel146, expr149, when152, expr154, texp156, entries162, entries164, entries166, entries168, entries170},
    generalizations={gen_sql_Select_SelectQuery, gen_sql_ColumnOrAlias_OrColumn, gen_sql_FromTable_OrTable, gen_sql_DbObjectName_ColumnFull, gen_sql_DbObjectName_TableFull, gen_sql_OrderByColumnFull_OrOrderByColumn, gen_sql_GroupByColumnFull_OrGroupByColumn, gen_sql_FullExpression_OrExpr, gen_sql_JRParameter_Prms, gen_sql_Operands_OpFunctionArgAgregate, gen_sql_OpFunctionArgOperand_OpFunctionArg, gen_sql_ScalarOperand_OperandList, gen_sql_SqlCaseWhen_SQLCaseWhens, gen_sql_Plus_Operands, gen_sql_Minus_Operands, gen_sql_Col_ColumnFull, gen_sql_tbls_TableFull, gen_sql_OpList_OperandList, gen_sql_Star_Operands, gen_sql_Div_Operands, gen_sql_Concat_Operands, gen_sql_OpFList_OpFunctionArg, gen_sql_WhenList_SQLCaseWhens},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
EXTRACT_VALUES: Enumeration = Enumeration(
    name="EXTRACT_VALUES",
    literals={
            EnumerationLiteral(name="hms"),
			EnumerationLiteral(name="hs"),
			EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="m"),
			EnumerationLiteral(name="h"),
			EnumerationLiteral(name="day"),
			EnumerationLiteral(name="week"),
			EnumerationLiteral(name="month"),
			EnumerationLiteral(name="quart"),
			EnumerationLiteral(name="year"),
			EnumerationLiteral(name="micros"),
			EnumerationLiteral(name="minMicro"),
			EnumerationLiteral(name="minSec"),
			EnumerationLiteral(name="hmin"),
			EnumerationLiteral(name="dms"),
			EnumerationLiteral(name="ds"),
			EnumerationLiteral(name="daymin"),
			EnumerationLiteral(name="dayh"),
			EnumerationLiteral(name="yearMonth")
    }
)

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
sql_SelectSubSet = Class(name="sql::SelectSubSet")
sql_Select = Class(name="sql::Select")
SelectQuery = Class(name="SelectQuery")
sql_Model = Class(name="sql::Model")
sql_SelectQuery = Class(name="sql::SelectQuery")
sql_FetchFirst = Class(name="sql::FetchFirst")
sql_IntegerValue = Class(name="sql::IntegerValue")
sql_Offset = Class(name="sql::Offset")
sql_Limit = Class(name="sql::Limit")
sql_OrOrderByColumn = Class(name="sql::OrOrderByColumn")
PivotForClause = Class(name="PivotForClause")
sql_OrColumn = Class(name="sql::OrColumn")
sql_OrTable = Class(name="sql::OrTable")
sql_OrExpr = Class(name="sql::OrExpr")
sql_OrGroupByColumn = Class(name="sql::OrGroupByColumn")
sql_ColumnFull = Class(name="sql::ColumnFull")
sql_FromTable = Class(name="sql::FromTable")
OrTable = Class(name="OrTable")
sql_TableOrAlias = Class(name="sql::TableOrAlias")
sql_FromTableJoin = Class(name="sql::FromTableJoin")
sql_ColumnOrAlias = Class(name="sql::ColumnOrAlias")
OrColumn = Class(name="OrColumn")
sql_Operands = Class(name="sql::Operands")
sql_DbObjectName = Class(name="sql::DbObjectName")
sql_DbObjectNameAll = Class(name="sql::DbObjectNameAll")
sql_PivotFunctions = Class(name="sql::PivotFunctions")
sql_PivotForClause = Class(name="sql::PivotForClause")
sql_PivotInClause = Class(name="sql::PivotInClause")
sql_TableFull = Class(name="sql::TableFull")
sql_SubQueryOperand = Class(name="sql::SubQueryOperand")
sql_PivotTable = Class(name="sql::PivotTable")
sql_UnpivotTable = Class(name="sql::UnpivotTable")
sql_UnpivotInClauseArg = Class(name="sql::UnpivotInClauseArg")
UnpivotInClauseArgs = Class(name="UnpivotInClauseArgs")
sql_Pivots = Class(name="sql::Pivots")
PivotColumns = Class(name="PivotColumns")
sql_PivotCol = Class(name="sql::PivotCol")
PivotFunction = Class(name="PivotFunction")
sql_PivotFunction = Class(name="sql::PivotFunction")
sql_UnpivotInClauseArgs = Class(name="sql::UnpivotInClauseArgs")
sql_PivotColumns = Class(name="sql::PivotColumns")
sql_UnpivotInClause = Class(name="sql::UnpivotInClause")
sql_GroupByColumnFull = Class(name="sql::GroupByColumnFull")
OrGroupByColumn = Class(name="OrGroupByColumn")
sql_OpFunction = Class(name="sql::OpFunction")
Pivots = Class(name="Pivots")
ColumnFull = Class(name="ColumnFull")
PivotCol = Class(name="PivotCol")
TableFull = Class(name="TableFull")
sql_OrderByColumnFull = Class(name="sql::OrderByColumnFull")
OrOrderByColumn = Class(name="OrOrderByColumn")
sql_XExpr = Class(name="sql::XExpr")
sql_InOper = Class(name="sql::InOper")
sql_ExistsOper = Class(name="sql::ExistsOper")
sql_Between = Class(name="sql::Between")
sql_FullExpression = Class(name="sql::FullExpression")
OrExpr = Class(name="OrExpr")
sql_ExprGroup = Class(name="sql::ExprGroup")
sql_Prms = Class(name="sql::Prms")
sql_JRParameter = Class(name="sql::JRParameter")
Prms = Class(name="Prms")
sql_Like = Class(name="sql::Like")
sql_Comparison = Class(name="sql::Comparison")
sql_POperand = Class(name="sql::POperand")
sql_LikeOperand = Class(name="sql::LikeOperand")
sql_OpFunctionCast = Class(name="sql::OpFunctionCast")
OpFunctionArgAgregate = Class(name="OpFunctionArgAgregate")
sql_Operand = Class(name="sql::Operand")
sql_OperandListGroup = Class(name="sql::OperandListGroup")
sql_OperandList = Class(name="sql::OperandList")
sql_AnalyticClause = Class(name="sql::AnalyticClause")
sql_ColumnOperand = Class(name="sql::ColumnOperand")
sql_SQLCaseOperand = Class(name="sql::SQLCaseOperand")
sql_ExpOperand = Class(name="sql::ExpOperand")
sql_ScalarOperand = Class(name="sql::ScalarOperand")
sql_FunctionExtract = Class(name="sql::FunctionExtract")
sql_OpFunctionArg = Class(name="sql::OpFunctionArg")
sql_FunctionAnalytical = Class(name="sql::FunctionAnalytical")
sql_OrderByClauseArgs = Class(name="sql::OrderByClauseArgs")
sql_QueryPartitionClause = Class(name="sql::QueryPartitionClause")
sql_OrderByClause = Class(name="sql::OrderByClause")
sql_WindowingClause = Class(name="sql::WindowingClause")
sql_WindowingClauseBetween = Class(name="sql::WindowingClauseBetween")
WindowingClause = Class(name="WindowingClause")
sql_WindowingClauseOperandPreceding = Class(name="sql::WindowingClauseOperandPreceding")
sql_WindowingClauseOperandFollowing = Class(name="sql::WindowingClauseOperandFollowing")
sql_AnalyticExprArg = Class(name="sql::AnalyticExprArg")
sql_OrderByClauseArg = Class(name="sql::OrderByClauseArg")
OrderByClauseArgs = Class(name="OrderByClauseArgs")
sql_AnalyticExprArgs = Class(name="sql::AnalyticExprArgs")
QueryPartitionClause = Class(name="QueryPartitionClause")
AnalyticExprArgs = Class(name="AnalyticExprArgs")
sql_OpFunctionArgOperand = Class(name="sql::OpFunctionArgOperand")
OpFunctionArg = Class(name="OpFunctionArg")
sql_OpFunctionArgAgregate = Class(name="sql::OpFunctionArgAgregate")
OperandList = Class(name="OperandList")
sql_SQLCaseWhens = Class(name="sql::SQLCaseWhens")
sql_SqlCaseWhen = Class(name="sql::SqlCaseWhen")
SQLCaseWhens = Class(name="SQLCaseWhens")
sql_UnipivotInClause = Class(name="sql::UnipivotInClause")
UnpivotInClause = Class(name="UnpivotInClause")
sql_Col = Class(name="sql::Col")
Operands = Class(name="Operands")
sql_uicargs = Class(name="sql::uicargs")
sql_pvcs = Class(name="sql::pvcs")
sql_pcols = Class(name="sql::pcols")
sql_tbls = Class(name="sql::tbls")
sql_OpList = Class(name="sql::OpList")
sql_Plus = Class(name="sql::Plus")
sql_Minus = Class(name="sql::Minus")
sql_Star = Class(name="sql::Star")
sql_Div = Class(name="sql::Div")
sql_Concat = Class(name="sql::Concat")
sql_OBCArgs = Class(name="sql::OBCArgs")
sql_AExpArgs = Class(name="sql::AExpArgs")
sql_OpFList = Class(name="sql::OpFList")
sql_WhenList = Class(name="sql::WhenList")

# sql_SelectSubSet class attributes and methods
sql_SelectSubSet_op: Property = Property(name="op", type=StringType)
sql_SelectSubSet_all: Property = Property(name="all", type=StringType)
sql_SelectSubSet.attributes={sql_SelectSubSet_op, sql_SelectSubSet_all}

# sql_Select class attributes and methods
sql_Select_select: Property = Property(name="select", type=StringType)
sql_Select.attributes={sql_Select_select}

# SelectQuery class attributes and methods

# sql_Model class attributes and methods

# sql_SelectQuery class attributes and methods

# sql_FetchFirst class attributes and methods
sql_FetchFirst_row: Property = Property(name="row", type=StringType)
sql_FetchFirst.attributes={sql_FetchFirst_row}

# sql_IntegerValue class attributes and methods
sql_IntegerValue_integer: Property = Property(name="integer", type=IntegerType)
sql_IntegerValue.attributes={sql_IntegerValue_integer}

# sql_Offset class attributes and methods
sql_Offset_offset: Property = Property(name="offset", type=IntegerType)
sql_Offset.attributes={sql_Offset_offset}

# sql_Limit class attributes and methods
sql_Limit_l1: Property = Property(name="l1", type=IntegerType)
sql_Limit.attributes={sql_Limit_l1}

# sql_OrOrderByColumn class attributes and methods

# PivotForClause class attributes and methods

# sql_OrColumn class attributes and methods

# sql_OrTable class attributes and methods

# sql_OrExpr class attributes and methods

# sql_OrGroupByColumn class attributes and methods

# sql_ColumnFull class attributes and methods

# sql_FromTable class attributes and methods

# OrTable class attributes and methods

# sql_TableOrAlias class attributes and methods
sql_TableOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_TableOrAlias.attributes={sql_TableOrAlias_alias}

# sql_FromTableJoin class attributes and methods
sql_FromTableJoin_join: Property = Property(name="join", type=StringType)
sql_FromTableJoin.attributes={sql_FromTableJoin_join}

# sql_ColumnOrAlias class attributes and methods
sql_ColumnOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_ColumnOrAlias_allCols: Property = Property(name="allCols", type=StringType)
sql_ColumnOrAlias.attributes={sql_ColumnOrAlias_alias, sql_ColumnOrAlias_allCols}

# OrColumn class attributes and methods

# sql_Operands class attributes and methods

# sql_DbObjectName class attributes and methods
sql_DbObjectName_dbname: Property = Property(name="dbname", type=StringType)
sql_DbObjectName.attributes={sql_DbObjectName_dbname}

# sql_DbObjectNameAll class attributes and methods
sql_DbObjectNameAll_dbname: Property = Property(name="dbname", type=StringType)
sql_DbObjectNameAll.attributes={sql_DbObjectNameAll_dbname}

# sql_PivotFunctions class attributes and methods
sql_PivotFunctions_abc: Property = Property(name="abc", type=StringType)
sql_PivotFunctions.attributes={sql_PivotFunctions_abc}

# sql_PivotForClause class attributes and methods

# sql_PivotInClause class attributes and methods
sql_PivotInClause_pinany: Property = Property(name="pinany", type=StringType)
sql_PivotInClause.attributes={sql_PivotInClause_pinany}

# sql_TableFull class attributes and methods

# sql_SubQueryOperand class attributes and methods

# sql_PivotTable class attributes and methods

# sql_UnpivotTable class attributes and methods

# sql_UnpivotInClauseArg class attributes and methods

# UnpivotInClauseArgs class attributes and methods

# sql_Pivots class attributes and methods

# PivotColumns class attributes and methods

# sql_PivotCol class attributes and methods

# PivotFunction class attributes and methods

# sql_PivotFunction class attributes and methods

# sql_UnpivotInClauseArgs class attributes and methods

# sql_PivotColumns class attributes and methods

# sql_UnpivotInClause class attributes and methods

# sql_GroupByColumnFull class attributes and methods

# OrGroupByColumn class attributes and methods

# sql_OpFunction class attributes and methods
sql_OpFunction_fname: Property = Property(name="fname", type=StringType)
sql_OpFunction.attributes={sql_OpFunction_fname}

# Pivots class attributes and methods

# ColumnFull class attributes and methods

# PivotCol class attributes and methods

# TableFull class attributes and methods

# sql_OrderByColumnFull class attributes and methods
sql_OrderByColumnFull_colOrderInt: Property = Property(name="colOrderInt", type=IntegerType)
sql_OrderByColumnFull_direction: Property = Property(name="direction", type=StringType)
sql_OrderByColumnFull.attributes={sql_OrderByColumnFull_direction, sql_OrderByColumnFull_colOrderInt}

# OrOrderByColumn class attributes and methods

# sql_XExpr class attributes and methods
sql_XExpr_xf: Property = Property(name="xf", type=StringType)
sql_XExpr.attributes={sql_XExpr_xf}

# sql_InOper class attributes and methods
sql_InOper_op: Property = Property(name="op", type=StringType)
sql_InOper.attributes={sql_InOper_op}

# sql_ExistsOper class attributes and methods
sql_ExistsOper_op: Property = Property(name="op", type=StringType)
sql_ExistsOper.attributes={sql_ExistsOper_op}

# sql_Between class attributes and methods
sql_Between_opBetween: Property = Property(name="opBetween", type=StringType)
sql_Between.attributes={sql_Between_opBetween}

# sql_FullExpression class attributes and methods
sql_FullExpression_isnull: Property = Property(name="isnull", type=StringType)
sql_FullExpression_c: Property = Property(name="c", type=StringType)
sql_FullExpression_notPrm: Property = Property(name="notPrm", type=StringType)
sql_FullExpression.attributes={sql_FullExpression_isnull, sql_FullExpression_c, sql_FullExpression_notPrm}

# OrExpr class attributes and methods

# sql_ExprGroup class attributes and methods
sql_ExprGroup_isnot: Property = Property(name="isnot", type=StringType)
sql_ExprGroup.attributes={sql_ExprGroup_isnot}

# sql_Prms class attributes and methods

# sql_JRParameter class attributes and methods
sql_JRParameter_jrprm: Property = Property(name="jrprm", type=StringType)
sql_JRParameter.attributes={sql_JRParameter_jrprm}

# Prms class attributes and methods

# sql_Like class attributes and methods
sql_Like_opLike: Property = Property(name="opLike", type=StringType)
sql_Like.attributes={sql_Like_opLike}

# sql_Comparison class attributes and methods
sql_Comparison_operator: Property = Property(name="operator", type=StringType)
sql_Comparison_subOperator: Property = Property(name="subOperator", type=StringType)
sql_Comparison.attributes={sql_Comparison_subOperator, sql_Comparison_operator}

# sql_POperand class attributes and methods
sql_POperand_prm: Property = Property(name="prm", type=StringType)
sql_POperand.attributes={sql_POperand_prm}

# sql_LikeOperand class attributes and methods
sql_LikeOperand_op2: Property = Property(name="op2", type=StringType)
sql_LikeOperand.attributes={sql_LikeOperand_op2}

# sql_OpFunctionCast class attributes and methods
sql_OpFunctionCast_type: Property = Property(name="type", type=StringType)
sql_OpFunctionCast_p: Property = Property(name="p", type=IntegerType)
sql_OpFunctionCast_p2: Property = Property(name="p2", type=IntegerType)
sql_OpFunctionCast.attributes={sql_OpFunctionCast_p2, sql_OpFunctionCast_p, sql_OpFunctionCast_type}

# OpFunctionArgAgregate class attributes and methods

# sql_Operand class attributes and methods

# sql_OperandListGroup class attributes and methods

# sql_OperandList class attributes and methods

# sql_AnalyticClause class attributes and methods

# sql_ColumnOperand class attributes and methods
sql_ColumnOperand_ora: Property = Property(name="ora", type=StringType)
sql_ColumnOperand.attributes={sql_ColumnOperand_ora}

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
sql_ScalarOperand.attributes={sql_ScalarOperand_sodate, sql_ScalarOperand_sotime, sql_ScalarOperand_sodt, sql_ScalarOperand_sostr, sql_ScalarOperand_sodbl, sql_ScalarOperand_soint}

# sql_FunctionExtract class attributes and methods
sql_FunctionExtract_v: Property = Property(name="v", type=StringType)
sql_FunctionExtract.attributes={sql_FunctionExtract_v}

# sql_OpFunctionArg class attributes and methods

# sql_FunctionAnalytical class attributes and methods

# sql_OrderByClauseArgs class attributes and methods

# sql_QueryPartitionClause class attributes and methods

# sql_OrderByClause class attributes and methods

# sql_WindowingClause class attributes and methods

# sql_WindowingClauseBetween class attributes and methods

# WindowingClause class attributes and methods

# sql_WindowingClauseOperandPreceding class attributes and methods

# sql_WindowingClauseOperandFollowing class attributes and methods

# sql_AnalyticExprArg class attributes and methods

# sql_OrderByClauseArg class attributes and methods

# OrderByClauseArgs class attributes and methods

# sql_AnalyticExprArgs class attributes and methods

# QueryPartitionClause class attributes and methods

# AnalyticExprArgs class attributes and methods

# sql_OpFunctionArgOperand class attributes and methods

# OpFunctionArg class attributes and methods

# sql_OpFunctionArgAgregate class attributes and methods

# OperandList class attributes and methods

# sql_SQLCaseWhens class attributes and methods

# sql_SqlCaseWhen class attributes and methods

# SQLCaseWhens class attributes and methods

# sql_UnipivotInClause class attributes and methods
sql_UnipivotInClause_op: Property = Property(name="op", type=StringType)
sql_UnipivotInClause.attributes={sql_UnipivotInClause_op}

# UnpivotInClause class attributes and methods

# sql_Col class attributes and methods

# Operands class attributes and methods

# sql_uicargs class attributes and methods

# sql_pvcs class attributes and methods

# sql_pcols class attributes and methods

# sql_tbls class attributes and methods

# sql_OpList class attributes and methods

# sql_Plus class attributes and methods

# sql_Minus class attributes and methods

# sql_Star class attributes and methods

# sql_Div class attributes and methods

# sql_Concat class attributes and methods

# sql_OBCArgs class attributes and methods

# sql_AExpArgs class attributes and methods

# sql_OpFList class attributes and methods

# sql_WhenList class attributes and methods

# Relationships
l22: BinaryAssociation = BinaryAssociation(
    name="l22",
    ends={
        Property(name="sql_IntegerValue3", type=sql_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Limit", type=sql_IntegerValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query4: BinaryAssociation = BinaryAssociation(
    name="query4",
    ends={
        Property(name="sql_Select", type=sql_SelectSubSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectSubSet", type=sql_Select, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op5: BinaryAssociation = BinaryAssociation(
    name="op5",
    ends={
        Property(name="sql_SelectSubSet7", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select6", type=sql_SelectSubSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query0: BinaryAssociation = BinaryAssociation(
    name="query0",
    ends={
        Property(name="sql_SelectQuery", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fetchFirst1: BinaryAssociation = BinaryAssociation(
    name="fetchFirst1",
    ends={
        Property(name="sql_IntegerValue", type=sql_FetchFirst, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FetchFirst", type=sql_IntegerValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
havingEntry16: BinaryAssociation = BinaryAssociation(
    name="havingEntry16",
    ends={
        Property(name="sql_Select17", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sql_OrExpr18", type=sql_Select, multiplicity=Multiplicity(1, 1))
    }
)
orderByEntry19: BinaryAssociation = BinaryAssociation(
    name="orderByEntry19",
    ends={
        Property(name="sql_OrOrderByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select20", type=sql_OrOrderByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lim21: BinaryAssociation = BinaryAssociation(
    name="lim21",
    ends={
        Property(name="sql_Limit23", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select22", type=sql_Limit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset24: BinaryAssociation = BinaryAssociation(
    name="offset24",
    ends={
        Property(name="sql_Offset", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select25", type=sql_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fetchFirst26: BinaryAssociation = BinaryAssociation(
    name="fetchFirst26",
    ends={
        Property(name="sql_FetchFirst28", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select27", type=sql_FetchFirst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cols8: BinaryAssociation = BinaryAssociation(
    name="cols8",
    ends={
        Property(name="sql_OrColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select9", type=sql_OrColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbl10: BinaryAssociation = BinaryAssociation(
    name="tbl10",
    ends={
        Property(name="sql_OrTable", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select11", type=sql_OrTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression12: BinaryAssociation = BinaryAssociation(
    name="whereExpression12",
    ends={
        Property(name="sql_OrExpr", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select13", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByEntry14: BinaryAssociation = BinaryAssociation(
    name="groupByEntry14",
    ends={
        Property(name="sql_OrGroupByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select15", type=sql_OrGroupByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries37: BinaryAssociation = BinaryAssociation(
    name="entries37",
    ends={
        Property(name="sql_FromTable", type=sql_OrTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrTable38", type=sql_FromTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table39: BinaryAssociation = BinaryAssociation(
    name="table39",
    ends={
        Property(name="sql_TableOrAlias", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable40", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fjoin41: BinaryAssociation = BinaryAssociation(
    name="fjoin41",
    ends={
        Property(name="sql_FromTableJoin", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable42", type=sql_FromTableJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries29: BinaryAssociation = BinaryAssociation(
    name="entries29",
    ends={
        Property(name="sql_ColumnOrAlias", type=sql_OrColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrColumn30", type=sql_ColumnOrAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce31: BinaryAssociation = BinaryAssociation(
    name="ce31",
    ends={
        Property(name="sql_Operands", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias32", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias33: BinaryAssociation = BinaryAssociation(
    name="colAlias33",
    ends={
        Property(name="sql_DbObjectName", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias34", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dbAllCols35: BinaryAssociation = BinaryAssociation(
    name="dbAllCols35",
    ends={
        Property(name="sql_DbObjectNameAll", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias36", type=sql_DbObjectNameAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpivot55: BinaryAssociation = BinaryAssociation(
    name="unpivot55",
    ends={
        Property(name="sql_UnpivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias56", type=sql_UnpivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tblAlias57: BinaryAssociation = BinaryAssociation(
    name="tblAlias57",
    ends={
        Property(name="sql_DbObjectName59", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias58", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfun60: BinaryAssociation = BinaryAssociation(
    name="pfun60",
    ends={
        Property(name="sql_PivotFunctions", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable61", type=sql_PivotFunctions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor62: BinaryAssociation = BinaryAssociation(
    name="pfor62",
    ends={
        Property(name="sql_PivotForClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable63", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pin64: BinaryAssociation = BinaryAssociation(
    name="pin64",
    ends={
        Property(name="sql_PivotInClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable65", type=sql_PivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTable43: BinaryAssociation = BinaryAssociation(
    name="onTable43",
    ends={
        Property(name="sql_TableOrAlias45", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin44", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinExpr46: BinaryAssociation = BinaryAssociation(
    name="joinExpr46",
    ends={
        Property(name="sql_OrExpr48", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin47", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tfull49: BinaryAssociation = BinaryAssociation(
    name="tfull49",
    ends={
        Property(name="sql_TableFull", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias50", type=sql_TableFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq51: BinaryAssociation = BinaryAssociation(
    name="sq51",
    ends={
        Property(name="sql_SubQueryOperand", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias52", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pivot53: BinaryAssociation = BinaryAssociation(
    name="pivot53",
    ends={
        Property(name="sql_PivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias54", type=sql_PivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inop76: BinaryAssociation = BinaryAssociation(
    name="inop76",
    ends={
        Property(name="sql_UnpivotInClause", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable77", type=sql_UnpivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols78: BinaryAssociation = BinaryAssociation(
    name="pcols78",
    ends={
        Property(name="sql_PivotColumns79", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfuls80: BinaryAssociation = BinaryAssociation(
    name="cfuls80",
    ends={
        Property(name="sql_PivotColumns82", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg81", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq66: BinaryAssociation = BinaryAssociation(
    name="sq66",
    ends={
        Property(name="sql_SubQueryOperand68", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause67", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args69: BinaryAssociation = BinaryAssociation(
    name="args69",
    ends={
        Property(name="sql_UnpivotInClauseArgs", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause70", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols71: BinaryAssociation = BinaryAssociation(
    name="pcols71",
    ends={
        Property(name="sql_PivotColumns", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable72", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor73: BinaryAssociation = BinaryAssociation(
    name="pfor73",
    ends={
        Property(name="sql_PivotForClause75", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable74", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colOrder85: BinaryAssociation = BinaryAssociation(
    name="colOrder85",
    ends={
        Property(name="sql_ColumnFull", type=sql_OrderByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByColumnFull86", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries87: BinaryAssociation = BinaryAssociation(
    name="entries87",
    ends={
        Property(name="sql_GroupByColumnFull", type=sql_OrGroupByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrGroupByColumn88", type=sql_GroupByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colGrBy89: BinaryAssociation = BinaryAssociation(
    name="colGrBy89",
    ends={
        Property(name="sql_ColumnFull91", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull90", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gbFunction92: BinaryAssociation = BinaryAssociation(
    name="gbFunction92",
    ends={
        Property(name="sql_OpFunction", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull93", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries83: BinaryAssociation = BinaryAssociation(
    name="entries83",
    ends={
        Property(name="sql_OrderByColumnFull", type=sql_OrOrderByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrOrderByColumn84", type=sql_OrderByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp102: BinaryAssociation = BinaryAssociation(
    name="exp102",
    ends={
        Property(name="sql_FullExpression103", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression101", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xexp104: BinaryAssociation = BinaryAssociation(
    name="xexp104",
    ends={
        Property(name="sql_XExpr", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression105", type=sql_XExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in106: BinaryAssociation = BinaryAssociation(
    name="in106",
    ends={
        Property(name="sql_InOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression107", type=sql_InOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exists108: BinaryAssociation = BinaryAssociation(
    name="exists108",
    ends={
        Property(name="sql_ExistsOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression109", type=sql_ExistsOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1110: BinaryAssociation = BinaryAssociation(
    name="op1110",
    ends={
        Property(name="sql_Operands112", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression111", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
between113: BinaryAssociation = BinaryAssociation(
    name="between113",
    ends={
        Property(name="sql_Between", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression114", type=sql_Between, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries94: BinaryAssociation = BinaryAssociation(
    name="entries94",
    ends={
        Property(name="sql_FullExpression", type=sql_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrExpr95", type=sql_FullExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
efrag97: BinaryAssociation = BinaryAssociation(
    name="efrag97",
    ends={
        Property(name="sql_FullExpression98", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression96", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expgroup99: BinaryAssociation = BinaryAssociation(
    name="expgroup99",
    ends={
        Property(name="sql_ExprGroup", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression100", type=sql_ExprGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col122: BinaryAssociation = BinaryAssociation(
    name="col122",
    ends={
        Property(name="sql_Operands124", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr123", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prm125: BinaryAssociation = BinaryAssociation(
    name="prm125",
    ends={
        Property(name="sql_Prms", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr126", type=sql_Prms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries127: BinaryAssociation = BinaryAssociation(
    name="entries127",
    ends={
        Property(name="sql_JRParameter", type=sql_Prms, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Prms128", type=sql_JRParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
like115: BinaryAssociation = BinaryAssociation(
    name="like115",
    ends={
        Property(name="sql_Like", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression116", type=sql_Like, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comp117: BinaryAssociation = BinaryAssociation(
    name="comp117",
    ends={
        Property(name="sql_Comparison", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression118", type=sql_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr119: BinaryAssociation = BinaryAssociation(
    name="expr119",
    ends={
        Property(name="sql_OrExpr121", type=sql_ExprGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExprGroup120", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fparam139: BinaryAssociation = BinaryAssociation(
    name="fparam139",
    ends={
        Property(name="sql_POperand", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand140", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2141: BinaryAssociation = BinaryAssociation(
    name="op2141",
    ends={
        Property(name="sql_Operands143", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between142", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op3144: BinaryAssociation = BinaryAssociation(
    name="op3144",
    ends={
        Property(name="sql_Operands146", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between145", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2129: BinaryAssociation = BinaryAssociation(
    name="op2129",
    ends={
        Property(name="sql_Operands131", type=sql_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Comparison130", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2132: BinaryAssociation = BinaryAssociation(
    name="op2132",
    ends={
        Property(name="sql_LikeOperand", type=sql_Like, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Like133", type=sql_LikeOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fop2134: BinaryAssociation = BinaryAssociation(
    name="fop2134",
    ends={
        Property(name="sql_OpFunction136", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand135", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast137: BinaryAssociation = BinaryAssociation(
    name="fcast137",
    ends={
        Property(name="sql_OpFunctionCast", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand138", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opGroup158: BinaryAssociation = BinaryAssociation(
    name="opGroup158",
    ends={
        Property(name="sql_OperandList", type=sql_OperandListGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OperandListGroup159", type=sql_OperandList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1160: BinaryAssociation = BinaryAssociation(
    name="op1160",
    ends={
        Property(name="sql_Operand", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands161", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left163: BinaryAssociation = BinaryAssociation(
    name="left163",
    ends={
        Property(name="sql_Operands164", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands162", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery147: BinaryAssociation = BinaryAssociation(
    name="subquery147",
    ends={
        Property(name="sql_SubQueryOperand149", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper148", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList150: BinaryAssociation = BinaryAssociation(
    name="opList150",
    ends={
        Property(name="sql_OperandListGroup", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper151", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery152: BinaryAssociation = BinaryAssociation(
    name="subquery152",
    ends={
        Property(name="sql_SubQueryOperand154", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper153", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList155: BinaryAssociation = BinaryAssociation(
    name="opList155",
    ends={
        Property(name="sql_OperandListGroup157", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper156", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right165: BinaryAssociation = BinaryAssociation(
    name="right165",
    ends={
        Property(name="sql_Operand167", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands166", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anClause200: BinaryAssociation = BinaryAssociation(
    name="anClause200",
    ends={
        Property(name="sql_AnalyticClause", type=sql_FunctionAnalytical, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionAnalytical201", type=sql_AnalyticClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func181: BinaryAssociation = BinaryAssociation(
    name="func181",
    ends={
        Property(name="sql_OpFunction183", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand182", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column168: BinaryAssociation = BinaryAssociation(
    name="column168",
    ends={
        Property(name="sql_ColumnOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand169", type=sql_ColumnOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sqlcase184: BinaryAssociation = BinaryAssociation(
    name="sqlcase184",
    ends={
        Property(name="sql_SQLCaseOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand185", type=sql_SQLCaseOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xop171: BinaryAssociation = BinaryAssociation(
    name="xop171",
    ends={
        Property(name="sql_Operand172", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand170", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param186: BinaryAssociation = BinaryAssociation(
    name="param186",
    ends={
        Property(name="sql_POperand188", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand187", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subq173: BinaryAssociation = BinaryAssociation(
    name="subq173",
    ends={
        Property(name="sql_SubQueryOperand175", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand174", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast176: BinaryAssociation = BinaryAssociation(
    name="fcast176",
    ends={
        Property(name="sql_OpFunctionCast178", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand177", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eparam189: BinaryAssociation = BinaryAssociation(
    name="eparam189",
    ends={
        Property(name="sql_ExpOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand190", type=sql_ExpOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scalar191: BinaryAssociation = BinaryAssociation(
    name="scalar191",
    ends={
        Property(name="sql_ScalarOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand192", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args193: BinaryAssociation = BinaryAssociation(
    name="args193",
    ends={
        Property(name="sql_OpFunctionArg", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction194", type=sql_OpFunctionArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fan195: BinaryAssociation = BinaryAssociation(
    name="fan195",
    ends={
        Property(name="sql_FunctionAnalytical", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction196", type=sql_FunctionAnalytical, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand197: BinaryAssociation = BinaryAssociation(
    name="operand197",
    ends={
        Property(name="sql_Operands199", type=sql_FunctionExtract, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionExtract198", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fext179: BinaryAssociation = BinaryAssociation(
    name="fext179",
    ends={
        Property(name="sql_FunctionExtract", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand180", type=sql_FunctionExtract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abc202: BinaryAssociation = BinaryAssociation(
    name="abc202",
    ends={
        Property(name="sql_QueryPartitionClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause203", type=sql_QueryPartitionClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obc204: BinaryAssociation = BinaryAssociation(
    name="obc204",
    ends={
        Property(name="sql_OrderByClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause205", type=sql_OrderByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
winc206: BinaryAssociation = BinaryAssociation(
    name="winc206",
    ends={
        Property(name="sql_WindowingClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause207", type=sql_WindowingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoP208: BinaryAssociation = BinaryAssociation(
    name="wcoP208",
    ends={
        Property(name="sql_WindowingClauseOperandPreceding", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoF209: BinaryAssociation = BinaryAssociation(
    name="wcoF209",
    ends={
        Property(name="sql_WindowingClauseOperandFollowing", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween210", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp211: BinaryAssociation = BinaryAssociation(
    name="exp211",
    ends={
        Property(name="sql_AnalyticExprArg", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandFollowing212", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr213: BinaryAssociation = BinaryAssociation(
    name="expr213",
    ends={
        Property(name="sql_AnalyticExprArg215", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandPreceding214", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op229: BinaryAssociation = BinaryAssociation(
    name="op229",
    ends={
        Property(name="sql_OpFunctionCast230", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sql_Operands231", type=sql_OpFunctionCast, multiplicity=Multiplicity(1, 1))
    }
)
args216: BinaryAssociation = BinaryAssociation(
    name="args216",
    ends={
        Property(name="sql_OrderByClauseArgs", type=sql_OrderByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClause217", type=sql_OrderByClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col218: BinaryAssociation = BinaryAssociation(
    name="col218",
    ends={
        Property(name="sql_AnalyticExprArg219", type=sql_OrderByClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClauseArg", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args220: BinaryAssociation = BinaryAssociation(
    name="args220",
    ends={
        Property(name="sql_AnalyticExprArgs", type=sql_QueryPartitionClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_QueryPartitionClause221", type=sql_AnalyticExprArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ce222: BinaryAssociation = BinaryAssociation(
    name="ce222",
    ends={
        Property(name="sql_Operands224", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg223", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias225: BinaryAssociation = BinaryAssociation(
    name="colAlias225",
    ends={
        Property(name="sql_DbObjectName227", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg226", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op228: BinaryAssociation = BinaryAssociation(
    name="op228",
    ends={
        Property(name="sql_OpFunctionArgAgregate", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionArgOperand", type=sql_OpFunctionArgAgregate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfull232: BinaryAssociation = BinaryAssociation(
    name="cfull232",
    ends={
        Property(name="sql_ColumnFull234", type=sql_ColumnOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOperand233", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sel235: BinaryAssociation = BinaryAssociation(
    name="sel235",
    ends={
        Property(name="sql_SelectQuery237", type=sql_SubQueryOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SubQueryOperand236", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr238: BinaryAssociation = BinaryAssociation(
    name="expr238",
    ends={
        Property(name="sql_OrExpr240", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand239", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when241: BinaryAssociation = BinaryAssociation(
    name="when241",
    ends={
        Property(name="sql_SQLCaseWhens", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand242", type=sql_SQLCaseWhens, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr243: BinaryAssociation = BinaryAssociation(
    name="expr243",
    ends={
        Property(name="sql_OrExpr244", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
texp245: BinaryAssociation = BinaryAssociation(
    name="texp245",
    ends={
        Property(name="sql_Operands247", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen246", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eexp248: BinaryAssociation = BinaryAssociation(
    name="eexp248",
    ends={
        Property(name="sql_Operands250", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen249", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries251: BinaryAssociation = BinaryAssociation(
    name="entries251",
    ends={
        Property(name="sql_DbObjectName252", type=sql_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Col", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args253: BinaryAssociation = BinaryAssociation(
    name="args253",
    ends={
        Property(name="sql_UnpivotInClauseArgs254", type=sql_UnipivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnipivotInClause", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries255: BinaryAssociation = BinaryAssociation(
    name="entries255",
    ends={
        Property(name="sql_UnpivotInClauseArg256", type=sql_uicargs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_uicargs", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries257: BinaryAssociation = BinaryAssociation(
    name="entries257",
    ends={
        Property(name="sql_PivotCol", type=sql_pvcs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pvcs", type=sql_PivotCol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries258: BinaryAssociation = BinaryAssociation(
    name="entries258",
    ends={
        Property(name="sql_DbObjectName259", type=sql_pcols, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pcols", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries260: BinaryAssociation = BinaryAssociation(
    name="entries260",
    ends={
        Property(name="sql_DbObjectName261", type=sql_tbls, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_tbls", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries262: BinaryAssociation = BinaryAssociation(
    name="entries262",
    ends={
        Property(name="sql_ScalarOperand263", type=sql_OpList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpList", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries264: BinaryAssociation = BinaryAssociation(
    name="entries264",
    ends={
        Property(name="sql_OrderByClauseArg265", type=sql_OBCArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OBCArgs", type=sql_OrderByClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries266: BinaryAssociation = BinaryAssociation(
    name="entries266",
    ends={
        Property(name="sql_AnalyticExprArg267", type=sql_AExpArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AExpArgs", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries268: BinaryAssociation = BinaryAssociation(
    name="entries268",
    ends={
        Property(name="sql_OpFunctionArgOperand269", type=sql_OpFList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFList", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries270: BinaryAssociation = BinaryAssociation(
    name="entries270",
    ends={
        Property(name="sql_SqlCaseWhen271", type=sql_WhenList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WhenList", type=sql_SqlCaseWhen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sql_Select_SelectQuery = Generalization(general=SelectQuery, specific=sql_Select)
gen_sql_OrColumn_PivotForClause = Generalization(general=PivotForClause, specific=sql_OrColumn)
gen_sql_ColumnFull_PivotForClause = Generalization(general=PivotForClause, specific=sql_ColumnFull)
gen_sql_FromTable_OrTable = Generalization(general=OrTable, specific=sql_FromTable)
gen_sql_ColumnOrAlias_OrColumn = Generalization(general=OrColumn, specific=sql_ColumnOrAlias)
gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_UnpivotInClauseArg)
gen_sql_Pivots_PivotColumns = Generalization(general=PivotColumns, specific=sql_Pivots)
gen_sql_PivotCol_PivotFunction = Generalization(general=PivotFunction, specific=sql_PivotCol)
gen_sql_GroupByColumnFull_OrGroupByColumn = Generalization(general=OrGroupByColumn, specific=sql_GroupByColumnFull)
gen_sql_PivotCol_PivotColumns = Generalization(general=PivotColumns, specific=sql_PivotCol)
gen_sql_PivotCol_Pivots = Generalization(general=Pivots, specific=sql_PivotCol)
gen_sql_DbObjectName_ColumnFull = Generalization(general=ColumnFull, specific=sql_DbObjectName)
gen_sql_DbObjectName_PivotCol = Generalization(general=PivotCol, specific=sql_DbObjectName)
gen_sql_DbObjectName_TableFull = Generalization(general=TableFull, specific=sql_DbObjectName)
gen_sql_OrderByColumnFull_OrOrderByColumn = Generalization(general=OrOrderByColumn, specific=sql_OrderByColumnFull)
gen_sql_FullExpression_OrExpr = Generalization(general=OrExpr, specific=sql_FullExpression)
gen_sql_JRParameter_Prms = Generalization(general=Prms, specific=sql_JRParameter)
gen_sql_Operands_OpFunctionArgAgregate = Generalization(general=OpFunctionArgAgregate, specific=sql_Operands)
gen_sql_WindowingClauseBetween_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseBetween)
gen_sql_WindowingClauseOperandPreceding_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseOperandPreceding)
gen_sql_OrderByClauseArg_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OrderByClauseArg)
gen_sql_AnalyticExprArgs_QueryPartitionClause = Generalization(general=QueryPartitionClause, specific=sql_AnalyticExprArgs)
gen_sql_AnalyticExprArg_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AnalyticExprArg)
gen_sql_OpFunctionArgOperand_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFunctionArgOperand)
gen_sql_ScalarOperand_OperandList = Generalization(general=OperandList, specific=sql_ScalarOperand)
gen_sql_SqlCaseWhen_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_SqlCaseWhen)
gen_sql_UnipivotInClause_UnpivotInClause = Generalization(general=UnpivotInClause, specific=sql_UnipivotInClause)
gen_sql_Col_ColumnFull = Generalization(general=ColumnFull, specific=sql_Col)
gen_sql_Plus_Operands = Generalization(general=Operands, specific=sql_Plus)
gen_sql_uicargs_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_uicargs)
gen_sql_pvcs_Pivots = Generalization(general=Pivots, specific=sql_pvcs)
gen_sql_pcols_PivotCol = Generalization(general=PivotCol, specific=sql_pcols)
gen_sql_tbls_TableFull = Generalization(general=TableFull, specific=sql_tbls)
gen_sql_OpList_OperandList = Generalization(general=OperandList, specific=sql_OpList)
gen_sql_Minus_Operands = Generalization(general=Operands, specific=sql_Minus)
gen_sql_Star_Operands = Generalization(general=Operands, specific=sql_Star)
gen_sql_Div_Operands = Generalization(general=Operands, specific=sql_Div)
gen_sql_Concat_Operands = Generalization(general=Operands, specific=sql_Concat)
gen_sql_OBCArgs_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OBCArgs)
gen_sql_AExpArgs_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AExpArgs)
gen_sql_OpFList_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFList)
gen_sql_WhenList_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_WhenList)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_SelectSubSet, sql_Select, SelectQuery, sql_Model, sql_SelectQuery, sql_FetchFirst, sql_IntegerValue, sql_Offset, sql_Limit, sql_OrOrderByColumn, PivotForClause, sql_OrColumn, sql_OrTable, sql_OrExpr, sql_OrGroupByColumn, sql_ColumnFull, sql_FromTable, OrTable, sql_TableOrAlias, sql_FromTableJoin, sql_ColumnOrAlias, OrColumn, sql_Operands, sql_DbObjectName, sql_DbObjectNameAll, sql_PivotFunctions, sql_PivotForClause, sql_PivotInClause, sql_TableFull, sql_SubQueryOperand, sql_PivotTable, sql_UnpivotTable, sql_UnpivotInClauseArg, UnpivotInClauseArgs, sql_Pivots, PivotColumns, sql_PivotCol, PivotFunction, sql_PivotFunction, sql_UnpivotInClauseArgs, sql_PivotColumns, sql_UnpivotInClause, sql_GroupByColumnFull, OrGroupByColumn, sql_OpFunction, Pivots, ColumnFull, PivotCol, TableFull, sql_OrderByColumnFull, OrOrderByColumn, sql_XExpr, sql_InOper, sql_ExistsOper, sql_Between, sql_FullExpression, OrExpr, sql_ExprGroup, sql_Prms, sql_JRParameter, Prms, sql_Like, sql_Comparison, sql_POperand, sql_LikeOperand, sql_OpFunctionCast, OpFunctionArgAgregate, sql_Operand, sql_OperandListGroup, sql_OperandList, sql_AnalyticClause, sql_ColumnOperand, sql_SQLCaseOperand, sql_ExpOperand, sql_ScalarOperand, sql_FunctionExtract, sql_OpFunctionArg, sql_FunctionAnalytical, sql_OrderByClauseArgs, sql_QueryPartitionClause, sql_OrderByClause, sql_WindowingClause, sql_WindowingClauseBetween, WindowingClause, sql_WindowingClauseOperandPreceding, sql_WindowingClauseOperandFollowing, sql_AnalyticExprArg, sql_OrderByClauseArg, OrderByClauseArgs, sql_AnalyticExprArgs, QueryPartitionClause, AnalyticExprArgs, sql_OpFunctionArgOperand, OpFunctionArg, sql_OpFunctionArgAgregate, OperandList, sql_SQLCaseWhens, sql_SqlCaseWhen, SQLCaseWhens, sql_UnipivotInClause, UnpivotInClause, sql_Col, Operands, sql_uicargs, sql_pvcs, sql_pcols, sql_tbls, sql_OpList, sql_Plus, sql_Minus, sql_Star, sql_Div, sql_Concat, sql_OBCArgs, sql_AExpArgs, sql_OpFList, sql_WhenList, EXTRACT_VALUES, XFunction},
    associations={l22, query4, op5, query0, fetchFirst1, havingEntry16, orderByEntry19, lim21, offset24, fetchFirst26, cols8, tbl10, whereExpression12, groupByEntry14, entries37, table39, fjoin41, entries29, ce31, colAlias33, dbAllCols35, unpivot55, tblAlias57, pfun60, pfor62, pin64, onTable43, joinExpr46, tfull49, sq51, pivot53, inop76, pcols78, cfuls80, sq66, args69, pcols71, pfor73, colOrder85, entries87, colGrBy89, gbFunction92, entries83, exp102, xexp104, in106, exists108, op1110, between113, entries94, efrag97, expgroup99, col122, prm125, entries127, like115, comp117, expr119, fparam139, op2141, op3144, op2129, op2132, fop2134, fcast137, opGroup158, op1160, left163, subquery147, opList150, subquery152, opList155, right165, anClause200, func181, column168, sqlcase184, xop171, param186, subq173, fcast176, eparam189, scalar191, args193, fan195, operand197, fext179, abc202, obc204, winc206, wcoP208, wcoF209, exp211, expr213, op229, args216, col218, args220, ce222, colAlias225, op228, cfull232, sel235, expr238, when241, expr243, texp245, eexp248, entries251, args253, entries255, entries257, entries258, entries260, entries262, entries264, entries266, entries268, entries270},
    generalizations={gen_sql_Select_SelectQuery, gen_sql_OrColumn_PivotForClause, gen_sql_ColumnFull_PivotForClause, gen_sql_FromTable_OrTable, gen_sql_ColumnOrAlias_OrColumn, gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs, gen_sql_Pivots_PivotColumns, gen_sql_PivotCol_PivotFunction, gen_sql_GroupByColumnFull_OrGroupByColumn, gen_sql_PivotCol_PivotColumns, gen_sql_PivotCol_Pivots, gen_sql_DbObjectName_ColumnFull, gen_sql_DbObjectName_PivotCol, gen_sql_DbObjectName_TableFull, gen_sql_OrderByColumnFull_OrOrderByColumn, gen_sql_FullExpression_OrExpr, gen_sql_JRParameter_Prms, gen_sql_Operands_OpFunctionArgAgregate, gen_sql_WindowingClauseBetween_WindowingClause, gen_sql_WindowingClauseOperandPreceding_WindowingClause, gen_sql_OrderByClauseArg_OrderByClauseArgs, gen_sql_AnalyticExprArgs_QueryPartitionClause, gen_sql_AnalyticExprArg_AnalyticExprArgs, gen_sql_OpFunctionArgOperand_OpFunctionArg, gen_sql_ScalarOperand_OperandList, gen_sql_SqlCaseWhen_SQLCaseWhens, gen_sql_UnipivotInClause_UnpivotInClause, gen_sql_Col_ColumnFull, gen_sql_Plus_Operands, gen_sql_uicargs_UnpivotInClauseArgs, gen_sql_pvcs_Pivots, gen_sql_pcols_PivotCol, gen_sql_tbls_TableFull, gen_sql_OpList_OperandList, gen_sql_Minus_Operands, gen_sql_Star_Operands, gen_sql_Div_Operands, gen_sql_Concat_Operands, gen_sql_OBCArgs_OrderByClauseArgs, gen_sql_AExpArgs_AnalyticExprArgs, gen_sql_OpFList_OpFunctionArg, gen_sql_WhenList_SQLCaseWhens},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
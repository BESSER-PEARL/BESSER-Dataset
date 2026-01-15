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
            EnumerationLiteral(name="xbwnc"),
			EnumerationLiteral(name="xbwnl"),
			EnumerationLiteral(name="xbwnr"),
			EnumerationLiteral(name="xin"),
			EnumerationLiteral(name="xnotin"),
			EnumerationLiteral(name="xeq"),
			EnumerationLiteral(name="xnoteq"),
			EnumerationLiteral(name="xls"),
			EnumerationLiteral(name="xlsr"),
			EnumerationLiteral(name="xgtl"),
			EnumerationLiteral(name="xgt"),
			EnumerationLiteral(name="xbwn")
    }
)

EXTRACT_VALUES: Enumeration = Enumeration(
    name="EXTRACT_VALUES",
    literals={
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
			EnumerationLiteral(name="hms"),
			EnumerationLiteral(name="hs"),
			EnumerationLiteral(name="hmin"),
			EnumerationLiteral(name="dms"),
			EnumerationLiteral(name="ds"),
			EnumerationLiteral(name="daymin"),
			EnumerationLiteral(name="dayh"),
			EnumerationLiteral(name="yearMonth")
    }
)

# Classes
sql_Select = Class(name="sql::Select")
sql_Model = Class(name="sql::Model")
sql_WithQuery = Class(name="sql::WithQuery")
sql_SelectQuery = Class(name="sql::SelectQuery")
sql_WithColumns = Class(name="sql::WithColumns")
sql_FetchFirst = Class(name="sql::FetchFirst")
sql_UnsignedValue = Class(name="sql::UnsignedValue")
sql_Offset = Class(name="sql::Offset")
sql_Limit = Class(name="sql::Limit")
sql_SelectSubSet = Class(name="sql::SelectSubSet")
sql_ColumnFull = Class(name="sql::ColumnFull")
SelectQuery = Class(name="SelectQuery")
sql_OrColumn = Class(name="sql::OrColumn")
sql_OrTable = Class(name="sql::OrTable")
sql_OrExpr = Class(name="sql::OrExpr")
sql_OrGroupByColumn = Class(name="sql::OrGroupByColumn")
sql_OrOrderByColumn = Class(name="sql::OrOrderByColumn")
PivotForClause = Class(name="PivotForClause")
sql_ColumnOrAlias = Class(name="sql::ColumnOrAlias")
OrColumn = Class(name="OrColumn")
sql_Operands = Class(name="sql::Operands")
sql_DbObjectName = Class(name="sql::DbObjectName")
sql_DbObjectNameAll = Class(name="sql::DbObjectNameAll")
sql_ColumnNames = Class(name="sql::ColumnNames")
FromValuesColumnNames = Class(name="FromValuesColumnNames")
sql_FromTable = Class(name="sql::FromTable")
OrTable = Class(name="OrTable")
sql_TableOrAlias = Class(name="sql::TableOrAlias")
sql_FromTableJoin = Class(name="sql::FromTableJoin")
sql_JoinCondition = Class(name="sql::JoinCondition")
sql_UsingCols = Class(name="sql::UsingCols")
WithColumns = Class(name="WithColumns")
sql_TableFull = Class(name="sql::TableFull")
sql_SubQueryOperand = Class(name="sql::SubQueryOperand")
sql_FromValues = Class(name="sql::FromValues")
sql_PivotTable = Class(name="sql::PivotTable")
sql_UnpivotTable = Class(name="sql::UnpivotTable")
sql_Values = Class(name="sql::Values")
sql_FromValuesColumns = Class(name="sql::FromValuesColumns")
sql_FromValuesColumnNames = Class(name="sql::FromValuesColumnNames")
sql_Rows = Class(name="sql::Rows")
sql_Row = Class(name="sql::Row")
Rows = Class(name="Rows")
sql_RowValues = Class(name="sql::RowValues")
sql_RowValue = Class(name="sql::RowValue")
RowValues = Class(name="RowValues")
sql_PivotFunctions = Class(name="sql::PivotFunctions")
sql_PivotForClause = Class(name="sql::PivotForClause")
sql_PivotInClause = Class(name="sql::PivotInClause")
sql_PivotFunction = Class(name="sql::PivotFunction")
sql_UnpivotInClauseArgs = Class(name="sql::UnpivotInClauseArgs")
sql_PivotColumns = Class(name="sql::PivotColumns")
sql_UnpivotInClause = Class(name="sql::UnpivotInClause")
sql_UnpivotInClauseArg = Class(name="sql::UnpivotInClauseArg")
UnpivotInClauseArgs = Class(name="UnpivotInClauseArgs")
sql_OpFunction = Class(name="sql::OpFunction")
sql_Pivots = Class(name="sql::Pivots")
PivotColumns = Class(name="PivotColumns")
sql_PivotCol = Class(name="sql::PivotCol")
PivotFunction = Class(name="PivotFunction")
Pivots = Class(name="Pivots")
ColumnFull = Class(name="ColumnFull")
UsingCols = Class(name="UsingCols")
PivotCol = Class(name="PivotCol")
TableFull = Class(name="TableFull")
sql_OrderByColumnFull = Class(name="sql::OrderByColumnFull")
OrOrderByColumn = Class(name="OrOrderByColumn")
sql_GroupByColumnFull = Class(name="sql::GroupByColumnFull")
OrGroupByColumn = Class(name="OrGroupByColumn")
sql_Between = Class(name="sql::Between")
sql_FullExpression = Class(name="sql::FullExpression")
OrExpr = Class(name="OrExpr")
sql_ExprGroup = Class(name="sql::ExprGroup")
sql_XExpr = Class(name="sql::XExpr")
sql_InOper = Class(name="sql::InOper")
sql_ExistsOper = Class(name="sql::ExistsOper")
sql_Like = Class(name="sql::Like")
sql_Comparison = Class(name="sql::Comparison")
sql_Prms = Class(name="sql::Prms")
sql_JRParameter = Class(name="sql::JRParameter")
Prms = Class(name="Prms")
sql_LikeOperand = Class(name="sql::LikeOperand")
sql_OpFunctionCast = Class(name="sql::OpFunctionCast")
sql_POperand = Class(name="sql::POperand")
sql_OperandListGroup = Class(name="sql::OperandListGroup")
sql_OperandList = Class(name="sql::OperandList")
OpFunctionArgAgregate = Class(name="OpFunctionArgAgregate")
sql_Operand = Class(name="sql::Operand")
sql_ColumnOperand = Class(name="sql::ColumnOperand")
sql_FunctionExtract = Class(name="sql::FunctionExtract")
sql_SQLCaseOperand = Class(name="sql::SQLCaseOperand")
sql_ExpOperand = Class(name="sql::ExpOperand")
sql_ScalarOperand = Class(name="sql::ScalarOperand")
sql_OpFunctionArg = Class(name="sql::OpFunctionArg")
sql_FunctionAnalytical = Class(name="sql::FunctionAnalytical")
sql_AnalyticClause = Class(name="sql::AnalyticClause")
sql_QueryPartitionClause = Class(name="sql::QueryPartitionClause")
sql_OrderByClause = Class(name="sql::OrderByClause")
sql_WindowingClause = Class(name="sql::WindowingClause")
AnalyticExprArgs = Class(name="AnalyticExprArgs")
sql_WindowingClauseBetween = Class(name="sql::WindowingClauseBetween")
WindowingClause = Class(name="WindowingClause")
sql_WindowingClauseOperandPreceding = Class(name="sql::WindowingClauseOperandPreceding")
sql_WindowingClauseOperandFollowing = Class(name="sql::WindowingClauseOperandFollowing")
sql_AnalyticExprArg = Class(name="sql::AnalyticExprArg")
sql_OrderByClauseArgs = Class(name="sql::OrderByClauseArgs")
sql_OrderByClauseArg = Class(name="sql::OrderByClauseArg")
OrderByClauseArgs = Class(name="OrderByClauseArgs")
sql_AnalyticExprArgs = Class(name="sql::AnalyticExprArgs")
QueryPartitionClause = Class(name="QueryPartitionClause")
sql_OpFunctionArgOperand = Class(name="sql::OpFunctionArgOperand")
OpFunctionArg = Class(name="OpFunctionArg")
sql_OpFunctionArgAgregate = Class(name="sql::OpFunctionArgAgregate")
RowValue = Class(name="RowValue")
OperandList = Class(name="OperandList")
sql_SQLCaseWhens = Class(name="sql::SQLCaseWhens")
sql_SqlCaseWhen = Class(name="sql::SqlCaseWhen")
SQLCaseWhens = Class(name="SQLCaseWhens")
sql_IntegerValue = Class(name="sql::IntegerValue")
sql_Col = Class(name="sql::Col")
sql_abc = Class(name="sql::abc")
sql_UnipivotInClause = Class(name="sql::UnipivotInClause")
UnpivotInClause = Class(name="UnpivotInClause")
sql_uicargs = Class(name="sql::uicargs")
sql_pvcs = Class(name="sql::pvcs")
sql_pcols = Class(name="sql::pcols")
sql_tbls = Class(name="sql::tbls")
sql_OpList = Class(name="sql::OpList")
sql_Plus = Class(name="sql::Plus")
Operands = Class(name="Operands")
sql_Minus = Class(name="sql::Minus")
sql_Concat = Class(name="sql::Concat")
sql_Multiply = Class(name="sql::Multiply")
sql_Division = Class(name="sql::Division")
sql_OBCArgs = Class(name="sql::OBCArgs")
sql_WhenList = Class(name="sql::WhenList")
sql_AExpArgs = Class(name="sql::AExpArgs")
sql_OpFList = Class(name="sql::OpFList")

# sql_Select class attributes and methods
sql_Select_select: Property = Property(name="select", type=StringType)
sql_Select.attributes={sql_Select_select}

# sql_Model class attributes and methods

# sql_WithQuery class attributes and methods
sql_WithQuery_w: Property = Property(name="w", type=StringType)
sql_WithQuery_wname: Property = Property(name="wname", type=StringType)
sql_WithQuery.attributes={sql_WithQuery_w, sql_WithQuery_wname}

# sql_SelectQuery class attributes and methods

# sql_WithColumns class attributes and methods

# sql_FetchFirst class attributes and methods
sql_FetchFirst_row: Property = Property(name="row", type=StringType)
sql_FetchFirst.attributes={sql_FetchFirst_row}

# sql_UnsignedValue class attributes and methods
sql_UnsignedValue_integer: Property = Property(name="integer", type=StringType)
sql_UnsignedValue.attributes={sql_UnsignedValue_integer}

# sql_Offset class attributes and methods
sql_Offset_offset: Property = Property(name="offset", type=StringType)
sql_Offset.attributes={sql_Offset_offset}

# sql_Limit class attributes and methods
sql_Limit_l1: Property = Property(name="l1", type=StringType)
sql_Limit_l2: Property = Property(name="l2", type=StringType)
sql_Limit.attributes={sql_Limit_l2, sql_Limit_l1}

# sql_SelectSubSet class attributes and methods
sql_SelectSubSet_op: Property = Property(name="op", type=StringType)
sql_SelectSubSet_all: Property = Property(name="all", type=StringType)
sql_SelectSubSet.attributes={sql_SelectSubSet_all, sql_SelectSubSet_op}

# sql_ColumnFull class attributes and methods

# SelectQuery class attributes and methods

# sql_OrColumn class attributes and methods

# sql_OrTable class attributes and methods

# sql_OrExpr class attributes and methods

# sql_OrGroupByColumn class attributes and methods

# sql_OrOrderByColumn class attributes and methods

# PivotForClause class attributes and methods

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

# sql_ColumnNames class attributes and methods
sql_ColumnNames_colName: Property = Property(name="colName", type=StringType)
sql_ColumnNames.attributes={sql_ColumnNames_colName}

# FromValuesColumnNames class attributes and methods

# sql_FromTable class attributes and methods

# OrTable class attributes and methods

# sql_TableOrAlias class attributes and methods
sql_TableOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_TableOrAlias.attributes={sql_TableOrAlias_alias}

# sql_FromTableJoin class attributes and methods
sql_FromTableJoin_join: Property = Property(name="join", type=StringType)
sql_FromTableJoin.attributes={sql_FromTableJoin_join}

# sql_JoinCondition class attributes and methods

# sql_UsingCols class attributes and methods

# WithColumns class attributes and methods

# sql_TableFull class attributes and methods

# sql_SubQueryOperand class attributes and methods

# sql_FromValues class attributes and methods

# sql_PivotTable class attributes and methods

# sql_UnpivotTable class attributes and methods

# sql_Values class attributes and methods

# sql_FromValuesColumns class attributes and methods

# sql_FromValuesColumnNames class attributes and methods

# sql_Rows class attributes and methods

# sql_Row class attributes and methods

# Rows class attributes and methods

# sql_RowValues class attributes and methods

# sql_RowValue class attributes and methods
sql_RowValue_null: Property = Property(name="null", type=StringType)
sql_RowValue.attributes={sql_RowValue_null}

# RowValues class attributes and methods

# sql_PivotFunctions class attributes and methods
sql_PivotFunctions_abc: Property = Property(name="abc", type=StringType)
sql_PivotFunctions.attributes={sql_PivotFunctions_abc}

# sql_PivotForClause class attributes and methods

# sql_PivotInClause class attributes and methods
sql_PivotInClause_pinany: Property = Property(name="pinany", type=StringType)
sql_PivotInClause.attributes={sql_PivotInClause_pinany}

# sql_PivotFunction class attributes and methods

# sql_UnpivotInClauseArgs class attributes and methods

# sql_PivotColumns class attributes and methods

# sql_UnpivotInClause class attributes and methods

# sql_UnpivotInClauseArg class attributes and methods

# UnpivotInClauseArgs class attributes and methods

# sql_OpFunction class attributes and methods
sql_OpFunction_fname: Property = Property(name="fname", type=StringType)
sql_OpFunction_star: Property = Property(name="star", type=StringType)
sql_OpFunction.attributes={sql_OpFunction_star, sql_OpFunction_fname}

# sql_Pivots class attributes and methods

# PivotColumns class attributes and methods

# sql_PivotCol class attributes and methods

# PivotFunction class attributes and methods

# Pivots class attributes and methods

# ColumnFull class attributes and methods

# UsingCols class attributes and methods

# PivotCol class attributes and methods

# TableFull class attributes and methods

# sql_OrderByColumnFull class attributes and methods
sql_OrderByColumnFull_colOrderInt: Property = Property(name="colOrderInt", type=StringType)
sql_OrderByColumnFull_direction: Property = Property(name="direction", type=StringType)
sql_OrderByColumnFull.attributes={sql_OrderByColumnFull_direction, sql_OrderByColumnFull_colOrderInt}

# OrOrderByColumn class attributes and methods

# sql_GroupByColumnFull class attributes and methods
sql_GroupByColumnFull_grByInt: Property = Property(name="grByInt", type=StringType)
sql_GroupByColumnFull.attributes={sql_GroupByColumnFull_grByInt}

# OrGroupByColumn class attributes and methods

# sql_Between class attributes and methods
sql_Between_opBetween: Property = Property(name="opBetween", type=StringType)
sql_Between.attributes={sql_Between_opBetween}

# sql_FullExpression class attributes and methods
sql_FullExpression_c: Property = Property(name="c", type=StringType)
sql_FullExpression_notPrm: Property = Property(name="notPrm", type=StringType)
sql_FullExpression_isnull: Property = Property(name="isnull", type=StringType)
sql_FullExpression.attributes={sql_FullExpression_isnull, sql_FullExpression_notPrm, sql_FullExpression_c}

# OrExpr class attributes and methods

# sql_ExprGroup class attributes and methods
sql_ExprGroup_isnot: Property = Property(name="isnot", type=StringType)
sql_ExprGroup.attributes={sql_ExprGroup_isnot}

# sql_XExpr class attributes and methods
sql_XExpr_xf: Property = Property(name="xf", type=StringType)
sql_XExpr.attributes={sql_XExpr_xf}

# sql_InOper class attributes and methods
sql_InOper_op: Property = Property(name="op", type=StringType)
sql_InOper.attributes={sql_InOper_op}

# sql_ExistsOper class attributes and methods
sql_ExistsOper_op: Property = Property(name="op", type=StringType)
sql_ExistsOper.attributes={sql_ExistsOper_op}

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

# sql_OpFunctionCast class attributes and methods
sql_OpFunctionCast_type: Property = Property(name="type", type=StringType)
sql_OpFunctionCast_p: Property = Property(name="p", type=StringType)
sql_OpFunctionCast_p2: Property = Property(name="p2", type=StringType)
sql_OpFunctionCast.attributes={sql_OpFunctionCast_type, sql_OpFunctionCast_p, sql_OpFunctionCast_p2}

# sql_POperand class attributes and methods
sql_POperand_prm: Property = Property(name="prm", type=StringType)
sql_POperand.attributes={sql_POperand_prm}

# sql_OperandListGroup class attributes and methods

# sql_OperandList class attributes and methods

# OpFunctionArgAgregate class attributes and methods

# sql_Operand class attributes and methods

# sql_ColumnOperand class attributes and methods
sql_ColumnOperand_ora: Property = Property(name="ora", type=StringType)
sql_ColumnOperand.attributes={sql_ColumnOperand_ora}

# sql_FunctionExtract class attributes and methods
sql_FunctionExtract_v: Property = Property(name="v", type=StringType)
sql_FunctionExtract.attributes={sql_FunctionExtract_v}

# sql_SQLCaseOperand class attributes and methods

# sql_ExpOperand class attributes and methods
sql_ExpOperand_prm: Property = Property(name="prm", type=StringType)
sql_ExpOperand.attributes={sql_ExpOperand_prm}

# sql_ScalarOperand class attributes and methods
sql_ScalarOperand_sostr: Property = Property(name="sostr", type=StringType)
sql_ScalarOperand_sodbl: Property = Property(name="sodbl", type=StringType)
sql_ScalarOperand_sodate: Property = Property(name="sodate", type=StringType)
sql_ScalarOperand_sotime: Property = Property(name="sotime", type=StringType)
sql_ScalarOperand_sodt: Property = Property(name="sodt", type=StringType)
sql_ScalarOperand_soUInt: Property = Property(name="soUInt", type=StringType)
sql_ScalarOperand_soint: Property = Property(name="soint", type=StringType)
sql_ScalarOperand.attributes={sql_ScalarOperand_sodbl, sql_ScalarOperand_sodt, sql_ScalarOperand_sotime, sql_ScalarOperand_sodate, sql_ScalarOperand_soUInt, sql_ScalarOperand_sostr, sql_ScalarOperand_soint}

# sql_OpFunctionArg class attributes and methods

# sql_FunctionAnalytical class attributes and methods

# sql_AnalyticClause class attributes and methods

# sql_QueryPartitionClause class attributes and methods

# sql_OrderByClause class attributes and methods

# sql_WindowingClause class attributes and methods

# AnalyticExprArgs class attributes and methods

# sql_WindowingClauseBetween class attributes and methods

# WindowingClause class attributes and methods

# sql_WindowingClauseOperandPreceding class attributes and methods

# sql_WindowingClauseOperandFollowing class attributes and methods

# sql_AnalyticExprArg class attributes and methods

# sql_OrderByClauseArgs class attributes and methods

# sql_OrderByClauseArg class attributes and methods

# OrderByClauseArgs class attributes and methods

# sql_AnalyticExprArgs class attributes and methods

# QueryPartitionClause class attributes and methods

# sql_OpFunctionArgOperand class attributes and methods

# OpFunctionArg class attributes and methods

# sql_OpFunctionArgAgregate class attributes and methods

# RowValue class attributes and methods

# OperandList class attributes and methods

# sql_SQLCaseWhens class attributes and methods

# sql_SqlCaseWhen class attributes and methods

# SQLCaseWhens class attributes and methods

# sql_IntegerValue class attributes and methods
sql_IntegerValue_integer: Property = Property(name="integer", type=StringType)
sql_IntegerValue.attributes={sql_IntegerValue_integer}

# sql_Col class attributes and methods

# sql_abc class attributes and methods

# sql_UnipivotInClause class attributes and methods
sql_UnipivotInClause_op: Property = Property(name="op", type=StringType)
sql_UnipivotInClause.attributes={sql_UnipivotInClause_op}

# UnpivotInClause class attributes and methods

# sql_uicargs class attributes and methods

# sql_pvcs class attributes and methods

# sql_pcols class attributes and methods

# sql_tbls class attributes and methods

# sql_OpList class attributes and methods

# sql_Plus class attributes and methods

# Operands class attributes and methods

# sql_Minus class attributes and methods

# sql_Concat class attributes and methods

# sql_Multiply class attributes and methods

# sql_Division class attributes and methods

# sql_OBCArgs class attributes and methods

# sql_WhenList class attributes and methods

# sql_AExpArgs class attributes and methods

# sql_OpFList class attributes and methods

# Relationships
query9: BinaryAssociation = BinaryAssociation(
    name="query9",
    ends={
        Property(name="sql_Select", type=sql_SelectSubSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectSubSet", type=sql_Select, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wq0: BinaryAssociation = BinaryAssociation(
    name="wq0",
    ends={
        Property(name="sql_WithQuery", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model", type=sql_WithQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query1: BinaryAssociation = BinaryAssociation(
    name="query1",
    ends={
        Property(name="sql_SelectQuery", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model2", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withCols3: BinaryAssociation = BinaryAssociation(
    name="withCols3",
    ends={
        Property(name="sql_WithColumns", type=sql_WithQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WithQuery4", type=sql_WithColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query5: BinaryAssociation = BinaryAssociation(
    name="query5",
    ends={
        Property(name="sql_SelectQuery7", type=sql_WithQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WithQuery6", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fetchFirst8: BinaryAssociation = BinaryAssociation(
    name="fetchFirst8",
    ends={
        Property(name="sql_UnsignedValue", type=sql_FetchFirst, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FetchFirst", type=sql_UnsignedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op10: BinaryAssociation = BinaryAssociation(
    name="op10",
    ends={
        Property(name="sql_SelectSubSet12", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select11", type=sql_SelectSubSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols13: BinaryAssociation = BinaryAssociation(
    name="cols13",
    ends={
        Property(name="sql_OrColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select14", type=sql_OrColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbl15: BinaryAssociation = BinaryAssociation(
    name="tbl15",
    ends={
        Property(name="sql_OrTable", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select16", type=sql_OrTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression17: BinaryAssociation = BinaryAssociation(
    name="whereExpression17",
    ends={
        Property(name="sql_OrExpr", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select18", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByEntry19: BinaryAssociation = BinaryAssociation(
    name="groupByEntry19",
    ends={
        Property(name="sql_OrGroupByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select20", type=sql_OrGroupByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
havingEntry21: BinaryAssociation = BinaryAssociation(
    name="havingEntry21",
    ends={
        Property(name="sql_OrExpr23", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select22", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderByEntry24: BinaryAssociation = BinaryAssociation(
    name="orderByEntry24",
    ends={
        Property(name="sql_OrOrderByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select25", type=sql_OrOrderByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lim26: BinaryAssociation = BinaryAssociation(
    name="lim26",
    ends={
        Property(name="sql_Limit", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select27", type=sql_Limit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset28: BinaryAssociation = BinaryAssociation(
    name="offset28",
    ends={
        Property(name="sql_Offset", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select29", type=sql_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fetchFirst30: BinaryAssociation = BinaryAssociation(
    name="fetchFirst30",
    ends={
        Property(name="sql_FetchFirst32", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select31", type=sql_FetchFirst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries33: BinaryAssociation = BinaryAssociation(
    name="entries33",
    ends={
        Property(name="sql_ColumnOrAlias", type=sql_OrColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrColumn34", type=sql_ColumnOrAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce35: BinaryAssociation = BinaryAssociation(
    name="ce35",
    ends={
        Property(name="sql_Operands", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias36", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias37: BinaryAssociation = BinaryAssociation(
    name="colAlias37",
    ends={
        Property(name="sql_DbObjectName", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias38", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dbAllCols39: BinaryAssociation = BinaryAssociation(
    name="dbAllCols39",
    ends={
        Property(name="sql_DbObjectNameAll", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias40", type=sql_DbObjectNameAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fvCols77: BinaryAssociation = BinaryAssociation(
    name="fvCols77",
    ends={
        Property(name="sql_FromValuesColumnNames", type=sql_FromValuesColumns, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValuesColumns78", type=sql_FromValuesColumnNames, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries41: BinaryAssociation = BinaryAssociation(
    name="entries41",
    ends={
        Property(name="sql_FromTable", type=sql_OrTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrTable42", type=sql_FromTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table43: BinaryAssociation = BinaryAssociation(
    name="table43",
    ends={
        Property(name="sql_TableOrAlias", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable44", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fjoin45: BinaryAssociation = BinaryAssociation(
    name="fjoin45",
    ends={
        Property(name="sql_FromTableJoin", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable46", type=sql_FromTableJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onTable47: BinaryAssociation = BinaryAssociation(
    name="onTable47",
    ends={
        Property(name="sql_TableOrAlias49", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin48", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinExpr50: BinaryAssociation = BinaryAssociation(
    name="joinExpr50",
    ends={
        Property(name="sql_OrExpr52", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin51", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinCond53: BinaryAssociation = BinaryAssociation(
    name="joinCond53",
    ends={
        Property(name="sql_JoinCondition", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin54", type=sql_JoinCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
useCols55: BinaryAssociation = BinaryAssociation(
    name="useCols55",
    ends={
        Property(name="sql_UsingCols", type=sql_JoinCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_JoinCondition56", type=sql_UsingCols, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries57: BinaryAssociation = BinaryAssociation(
    name="entries57",
    ends={
        Property(name="sql_DbObjectName59", type=sql_UsingCols, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UsingCols58", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfull60: BinaryAssociation = BinaryAssociation(
    name="tfull60",
    ends={
        Property(name="sql_TableFull", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias61", type=sql_TableFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq62: BinaryAssociation = BinaryAssociation(
    name="sq62",
    ends={
        Property(name="sql_SubQueryOperand", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias63", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values64: BinaryAssociation = BinaryAssociation(
    name="values64",
    ends={
        Property(name="sql_FromValues", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias65", type=sql_FromValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pivot66: BinaryAssociation = BinaryAssociation(
    name="pivot66",
    ends={
        Property(name="sql_PivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias67", type=sql_PivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpivot68: BinaryAssociation = BinaryAssociation(
    name="unpivot68",
    ends={
        Property(name="sql_UnpivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias69", type=sql_UnpivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tblAlias70: BinaryAssociation = BinaryAssociation(
    name="tblAlias70",
    ends={
        Property(name="sql_DbObjectName72", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias71", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values73: BinaryAssociation = BinaryAssociation(
    name="values73",
    ends={
        Property(name="sql_Values", type=sql_FromValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValues74", type=sql_Values, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c75: BinaryAssociation = BinaryAssociation(
    name="c75",
    ends={
        Property(name="sql_FromValuesColumns", type=sql_FromValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValues76", type=sql_FromValuesColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols105: BinaryAssociation = BinaryAssociation(
    name="pcols105",
    ends={
        Property(name="sql_PivotColumns106", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfuls107: BinaryAssociation = BinaryAssociation(
    name="cfuls107",
    ends={
        Property(name="sql_PivotColumns109", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg108", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows79: BinaryAssociation = BinaryAssociation(
    name="rows79",
    ends={
        Property(name="sql_Rows", type=sql_Values, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Values80", type=sql_Rows, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries81: BinaryAssociation = BinaryAssociation(
    name="entries81",
    ends={
        Property(name="sql_Row", type=sql_Rows, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Rows82", type=sql_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rowValues83: BinaryAssociation = BinaryAssociation(
    name="rowValues83",
    ends={
        Property(name="sql_RowValues", type=sql_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Row84", type=sql_RowValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries85: BinaryAssociation = BinaryAssociation(
    name="entries85",
    ends={
        Property(name="sql_RowValue", type=sql_RowValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_RowValues86", type=sql_RowValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pfun87: BinaryAssociation = BinaryAssociation(
    name="pfun87",
    ends={
        Property(name="sql_PivotFunctions", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable88", type=sql_PivotFunctions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor89: BinaryAssociation = BinaryAssociation(
    name="pfor89",
    ends={
        Property(name="sql_PivotForClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable90", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pin91: BinaryAssociation = BinaryAssociation(
    name="pin91",
    ends={
        Property(name="sql_PivotInClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable92", type=sql_PivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq93: BinaryAssociation = BinaryAssociation(
    name="sq93",
    ends={
        Property(name="sql_SubQueryOperand95", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause94", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args96: BinaryAssociation = BinaryAssociation(
    name="args96",
    ends={
        Property(name="sql_UnpivotInClauseArgs", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause97", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols98: BinaryAssociation = BinaryAssociation(
    name="pcols98",
    ends={
        Property(name="sql_PivotColumns", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable99", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor100: BinaryAssociation = BinaryAssociation(
    name="pfor100",
    ends={
        Property(name="sql_PivotForClause102", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable101", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inop103: BinaryAssociation = BinaryAssociation(
    name="inop103",
    ends={
        Property(name="sql_UnpivotInClause", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable104", type=sql_UnpivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colGrBy116: BinaryAssociation = BinaryAssociation(
    name="colGrBy116",
    ends={
        Property(name="sql_ColumnFull118", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull117", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gbFunction119: BinaryAssociation = BinaryAssociation(
    name="gbFunction119",
    ends={
        Property(name="sql_OpFunction", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull120", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries110: BinaryAssociation = BinaryAssociation(
    name="entries110",
    ends={
        Property(name="sql_OrderByColumnFull", type=sql_OrOrderByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrOrderByColumn111", type=sql_OrderByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colOrder112: BinaryAssociation = BinaryAssociation(
    name="colOrder112",
    ends={
        Property(name="sql_ColumnFull", type=sql_OrderByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByColumnFull113", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries114: BinaryAssociation = BinaryAssociation(
    name="entries114",
    ends={
        Property(name="sql_GroupByColumnFull", type=sql_OrGroupByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrGroupByColumn115", type=sql_GroupByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
between140: BinaryAssociation = BinaryAssociation(
    name="between140",
    ends={
        Property(name="sql_Between", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression141", type=sql_Between, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries121: BinaryAssociation = BinaryAssociation(
    name="entries121",
    ends={
        Property(name="sql_FullExpression", type=sql_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrExpr122", type=sql_FullExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
efrag124: BinaryAssociation = BinaryAssociation(
    name="efrag124",
    ends={
        Property(name="sql_FullExpression125", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression123", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expgroup126: BinaryAssociation = BinaryAssociation(
    name="expgroup126",
    ends={
        Property(name="sql_ExprGroup", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression127", type=sql_ExprGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp129: BinaryAssociation = BinaryAssociation(
    name="exp129",
    ends={
        Property(name="sql_FullExpression130", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression128", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xexp131: BinaryAssociation = BinaryAssociation(
    name="xexp131",
    ends={
        Property(name="sql_XExpr", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression132", type=sql_XExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in133: BinaryAssociation = BinaryAssociation(
    name="in133",
    ends={
        Property(name="sql_InOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression134", type=sql_InOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exists135: BinaryAssociation = BinaryAssociation(
    name="exists135",
    ends={
        Property(name="sql_ExistsOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression136", type=sql_ExistsOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1137: BinaryAssociation = BinaryAssociation(
    name="op1137",
    ends={
        Property(name="sql_Operands139", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression138", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
like142: BinaryAssociation = BinaryAssociation(
    name="like142",
    ends={
        Property(name="sql_Like", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression143", type=sql_Like, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comp144: BinaryAssociation = BinaryAssociation(
    name="comp144",
    ends={
        Property(name="sql_Comparison", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression145", type=sql_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr146: BinaryAssociation = BinaryAssociation(
    name="expr146",
    ends={
        Property(name="sql_OrExpr148", type=sql_ExprGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExprGroup147", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col149: BinaryAssociation = BinaryAssociation(
    name="col149",
    ends={
        Property(name="sql_Operands151", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr150", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prm152: BinaryAssociation = BinaryAssociation(
    name="prm152",
    ends={
        Property(name="sql_Prms", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr153", type=sql_Prms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left190: BinaryAssociation = BinaryAssociation(
    name="left190",
    ends={
        Property(name="sql_Operands191", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands189", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries154: BinaryAssociation = BinaryAssociation(
    name="entries154",
    ends={
        Property(name="sql_JRParameter", type=sql_Prms, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Prms155", type=sql_JRParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op2156: BinaryAssociation = BinaryAssociation(
    name="op2156",
    ends={
        Property(name="sql_Operands158", type=sql_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Comparison157", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2159: BinaryAssociation = BinaryAssociation(
    name="op2159",
    ends={
        Property(name="sql_LikeOperand", type=sql_Like, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Like160", type=sql_LikeOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fop2161: BinaryAssociation = BinaryAssociation(
    name="fop2161",
    ends={
        Property(name="sql_OpFunction163", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand162", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast164: BinaryAssociation = BinaryAssociation(
    name="fcast164",
    ends={
        Property(name="sql_OpFunctionCast", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand165", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fparam166: BinaryAssociation = BinaryAssociation(
    name="fparam166",
    ends={
        Property(name="sql_POperand", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand167", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2168: BinaryAssociation = BinaryAssociation(
    name="op2168",
    ends={
        Property(name="sql_Operands170", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between169", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op3171: BinaryAssociation = BinaryAssociation(
    name="op3171",
    ends={
        Property(name="sql_Operands173", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between172", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery174: BinaryAssociation = BinaryAssociation(
    name="subquery174",
    ends={
        Property(name="sql_SubQueryOperand176", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper175", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList177: BinaryAssociation = BinaryAssociation(
    name="opList177",
    ends={
        Property(name="sql_OperandListGroup", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper178", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery179: BinaryAssociation = BinaryAssociation(
    name="subquery179",
    ends={
        Property(name="sql_SubQueryOperand181", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper180", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList182: BinaryAssociation = BinaryAssociation(
    name="opList182",
    ends={
        Property(name="sql_OperandListGroup184", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper183", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opGroup185: BinaryAssociation = BinaryAssociation(
    name="opGroup185",
    ends={
        Property(name="sql_OperandList", type=sql_OperandListGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OperandListGroup186", type=sql_OperandList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1187: BinaryAssociation = BinaryAssociation(
    name="op1187",
    ends={
        Property(name="sql_Operand", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands188", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right192: BinaryAssociation = BinaryAssociation(
    name="right192",
    ends={
        Property(name="sql_Operand194", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands193", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column195: BinaryAssociation = BinaryAssociation(
    name="column195",
    ends={
        Property(name="sql_ColumnOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand196", type=sql_ColumnOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xop198: BinaryAssociation = BinaryAssociation(
    name="xop198",
    ends={
        Property(name="sql_Operand199", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand197", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subq200: BinaryAssociation = BinaryAssociation(
    name="subq200",
    ends={
        Property(name="sql_SubQueryOperand202", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand201", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast203: BinaryAssociation = BinaryAssociation(
    name="fcast203",
    ends={
        Property(name="sql_OpFunctionCast205", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand204", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fext206: BinaryAssociation = BinaryAssociation(
    name="fext206",
    ends={
        Property(name="sql_FunctionExtract", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand207", type=sql_FunctionExtract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func208: BinaryAssociation = BinaryAssociation(
    name="func208",
    ends={
        Property(name="sql_OpFunction210", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand209", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sqlcase211: BinaryAssociation = BinaryAssociation(
    name="sqlcase211",
    ends={
        Property(name="sql_SQLCaseOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand212", type=sql_SQLCaseOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param213: BinaryAssociation = BinaryAssociation(
    name="param213",
    ends={
        Property(name="sql_POperand215", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand214", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eparam216: BinaryAssociation = BinaryAssociation(
    name="eparam216",
    ends={
        Property(name="sql_ExpOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand217", type=sql_ExpOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scalar218: BinaryAssociation = BinaryAssociation(
    name="scalar218",
    ends={
        Property(name="sql_ScalarOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand219", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args220: BinaryAssociation = BinaryAssociation(
    name="args220",
    ends={
        Property(name="sql_OpFunctionArg", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction221", type=sql_OpFunctionArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fan222: BinaryAssociation = BinaryAssociation(
    name="fan222",
    ends={
        Property(name="sql_FunctionAnalytical", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction223", type=sql_FunctionAnalytical, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand224: BinaryAssociation = BinaryAssociation(
    name="operand224",
    ends={
        Property(name="sql_Operands226", type=sql_FunctionExtract, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionExtract225", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anClause227: BinaryAssociation = BinaryAssociation(
    name="anClause227",
    ends={
        Property(name="sql_AnalyticClause", type=sql_FunctionAnalytical, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionAnalytical228", type=sql_AnalyticClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abc229: BinaryAssociation = BinaryAssociation(
    name="abc229",
    ends={
        Property(name="sql_QueryPartitionClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause230", type=sql_QueryPartitionClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obc231: BinaryAssociation = BinaryAssociation(
    name="obc231",
    ends={
        Property(name="sql_OrderByClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause232", type=sql_OrderByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
winc233: BinaryAssociation = BinaryAssociation(
    name="winc233",
    ends={
        Property(name="sql_WindowingClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause234", type=sql_WindowingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoP235: BinaryAssociation = BinaryAssociation(
    name="wcoP235",
    ends={
        Property(name="sql_WindowingClauseOperandPreceding", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoF236: BinaryAssociation = BinaryAssociation(
    name="wcoF236",
    ends={
        Property(name="sql_WindowingClauseOperandFollowing", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween237", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp238: BinaryAssociation = BinaryAssociation(
    name="exp238",
    ends={
        Property(name="sql_AnalyticExprArg", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandFollowing239", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr240: BinaryAssociation = BinaryAssociation(
    name="expr240",
    ends={
        Property(name="sql_AnalyticExprArg242", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandPreceding241", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args243: BinaryAssociation = BinaryAssociation(
    name="args243",
    ends={
        Property(name="sql_OrderByClauseArgs", type=sql_OrderByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClause244", type=sql_OrderByClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col245: BinaryAssociation = BinaryAssociation(
    name="col245",
    ends={
        Property(name="sql_AnalyticExprArg246", type=sql_OrderByClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClauseArg", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args247: BinaryAssociation = BinaryAssociation(
    name="args247",
    ends={
        Property(name="sql_AnalyticExprArgs", type=sql_QueryPartitionClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_QueryPartitionClause248", type=sql_AnalyticExprArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ce249: BinaryAssociation = BinaryAssociation(
    name="ce249",
    ends={
        Property(name="sql_Operands251", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg250", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias252: BinaryAssociation = BinaryAssociation(
    name="colAlias252",
    ends={
        Property(name="sql_DbObjectName254", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg253", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op255: BinaryAssociation = BinaryAssociation(
    name="op255",
    ends={
        Property(name="sql_OpFunctionArgAgregate", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionArgOperand", type=sql_OpFunctionArgAgregate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op256: BinaryAssociation = BinaryAssociation(
    name="op256",
    ends={
        Property(name="sql_Operands258", type=sql_OpFunctionCast, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionCast257", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfull259: BinaryAssociation = BinaryAssociation(
    name="cfull259",
    ends={
        Property(name="sql_ColumnFull261", type=sql_ColumnOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOperand260", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr275: BinaryAssociation = BinaryAssociation(
    name="expr275",
    ends={
        Property(name="sql_OrExpr277", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen276", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sel262: BinaryAssociation = BinaryAssociation(
    name="sel262",
    ends={
        Property(name="sql_SelectQuery264", type=sql_SubQueryOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SubQueryOperand263", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wop265: BinaryAssociation = BinaryAssociation(
    name="wop265",
    ends={
        Property(name="sql_Operands267", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand266", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr268: BinaryAssociation = BinaryAssociation(
    name="expr268",
    ends={
        Property(name="sql_OrExpr270", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand269", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when271: BinaryAssociation = BinaryAssociation(
    name="when271",
    ends={
        Property(name="sql_SQLCaseWhens", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand272", type=sql_SQLCaseWhens, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wop273: BinaryAssociation = BinaryAssociation(
    name="wop273",
    ends={
        Property(name="sql_Operands274", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
texp278: BinaryAssociation = BinaryAssociation(
    name="texp278",
    ends={
        Property(name="sql_Operands280", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen279", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eexp281: BinaryAssociation = BinaryAssociation(
    name="eexp281",
    ends={
        Property(name="sql_Operands283", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen282", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries292: BinaryAssociation = BinaryAssociation(
    name="entries292",
    ends={
        Property(name="sql_DbObjectName293", type=sql_pcols, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pcols", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries284: BinaryAssociation = BinaryAssociation(
    name="entries284",
    ends={
        Property(name="sql_DbObjectName285", type=sql_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Col", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries286: BinaryAssociation = BinaryAssociation(
    name="entries286",
    ends={
        Property(name="sql_ColumnNames", type=sql_abc, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_abc", type=sql_ColumnNames, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args287: BinaryAssociation = BinaryAssociation(
    name="args287",
    ends={
        Property(name="sql_UnpivotInClauseArgs288", type=sql_UnipivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnipivotInClause", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries289: BinaryAssociation = BinaryAssociation(
    name="entries289",
    ends={
        Property(name="sql_UnpivotInClauseArg290", type=sql_uicargs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_uicargs", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries291: BinaryAssociation = BinaryAssociation(
    name="entries291",
    ends={
        Property(name="sql_PivotCol", type=sql_pvcs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pvcs", type=sql_PivotCol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries294: BinaryAssociation = BinaryAssociation(
    name="entries294",
    ends={
        Property(name="sql_DbObjectName295", type=sql_tbls, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_tbls", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries296: BinaryAssociation = BinaryAssociation(
    name="entries296",
    ends={
        Property(name="sql_ScalarOperand297", type=sql_OpList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpList", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries302: BinaryAssociation = BinaryAssociation(
    name="entries302",
    ends={
        Property(name="sql_OpFunctionArgOperand303", type=sql_OpFList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFList", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries304: BinaryAssociation = BinaryAssociation(
    name="entries304",
    ends={
        Property(name="sql_SqlCaseWhen305", type=sql_WhenList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WhenList", type=sql_SqlCaseWhen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries298: BinaryAssociation = BinaryAssociation(
    name="entries298",
    ends={
        Property(name="sql_OrderByClauseArg299", type=sql_OBCArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OBCArgs", type=sql_OrderByClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries300: BinaryAssociation = BinaryAssociation(
    name="entries300",
    ends={
        Property(name="sql_AnalyticExprArg301", type=sql_AExpArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AExpArgs", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sql_ColumnFull_PivotForClause = Generalization(general=PivotForClause, specific=sql_ColumnFull)
gen_sql_Select_SelectQuery = Generalization(general=SelectQuery, specific=sql_Select)
gen_sql_OrColumn_PivotForClause = Generalization(general=PivotForClause, specific=sql_OrColumn)
gen_sql_ColumnOrAlias_OrColumn = Generalization(general=OrColumn, specific=sql_ColumnOrAlias)
gen_sql_ColumnNames_FromValuesColumnNames = Generalization(general=FromValuesColumnNames, specific=sql_ColumnNames)
gen_sql_FromTable_OrTable = Generalization(general=OrTable, specific=sql_FromTable)
gen_sql_UsingCols_WithColumns = Generalization(general=WithColumns, specific=sql_UsingCols)
gen_sql_Row_Rows = Generalization(general=Rows, specific=sql_Row)
gen_sql_RowValue_RowValues = Generalization(general=RowValues, specific=sql_RowValue)
gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_UnpivotInClauseArg)
gen_sql_Pivots_PivotColumns = Generalization(general=PivotColumns, specific=sql_Pivots)
gen_sql_PivotCol_PivotFunction = Generalization(general=PivotFunction, specific=sql_PivotCol)
gen_sql_PivotCol_PivotColumns = Generalization(general=PivotColumns, specific=sql_PivotCol)
gen_sql_PivotCol_Pivots = Generalization(general=Pivots, specific=sql_PivotCol)
gen_sql_DbObjectName_ColumnFull = Generalization(general=ColumnFull, specific=sql_DbObjectName)
gen_sql_DbObjectName_UsingCols = Generalization(general=UsingCols, specific=sql_DbObjectName)
gen_sql_DbObjectName_PivotCol = Generalization(general=PivotCol, specific=sql_DbObjectName)
gen_sql_DbObjectName_TableFull = Generalization(general=TableFull, specific=sql_DbObjectName)
gen_sql_OrderByColumnFull_OrOrderByColumn = Generalization(general=OrOrderByColumn, specific=sql_OrderByColumnFull)
gen_sql_GroupByColumnFull_OrGroupByColumn = Generalization(general=OrGroupByColumn, specific=sql_GroupByColumnFull)
gen_sql_FullExpression_OrExpr = Generalization(general=OrExpr, specific=sql_FullExpression)
gen_sql_JRParameter_Prms = Generalization(general=Prms, specific=sql_JRParameter)
gen_sql_Operands_OpFunctionArgAgregate = Generalization(general=OpFunctionArgAgregate, specific=sql_Operands)
gen_sql_AnalyticExprArgs_QueryPartitionClause = Generalization(general=QueryPartitionClause, specific=sql_AnalyticExprArgs)
gen_sql_AnalyticExprArg_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AnalyticExprArg)
gen_sql_WindowingClauseBetween_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseBetween)
gen_sql_WindowingClauseOperandPreceding_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseOperandPreceding)
gen_sql_OrderByClauseArg_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OrderByClauseArg)
gen_sql_OpFunctionArgOperand_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFunctionArgOperand)
gen_sql_ScalarOperand_RowValue = Generalization(general=RowValue, specific=sql_ScalarOperand)
gen_sql_ScalarOperand_OperandList = Generalization(general=OperandList, specific=sql_ScalarOperand)
gen_sql_SqlCaseWhen_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_SqlCaseWhen)
gen_sql_Col_ColumnFull = Generalization(general=ColumnFull, specific=sql_Col)
gen_sql_abc_FromValuesColumnNames = Generalization(general=FromValuesColumnNames, specific=sql_abc)
gen_sql_UnipivotInClause_UnpivotInClause = Generalization(general=UnpivotInClause, specific=sql_UnipivotInClause)
gen_sql_uicargs_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_uicargs)
gen_sql_pvcs_Pivots = Generalization(general=Pivots, specific=sql_pvcs)
gen_sql_pcols_PivotCol = Generalization(general=PivotCol, specific=sql_pcols)
gen_sql_tbls_TableFull = Generalization(general=TableFull, specific=sql_tbls)
gen_sql_OpList_OperandList = Generalization(general=OperandList, specific=sql_OpList)
gen_sql_Plus_Operands = Generalization(general=Operands, specific=sql_Plus)
gen_sql_Minus_Operands = Generalization(general=Operands, specific=sql_Minus)
gen_sql_Concat_Operands = Generalization(general=Operands, specific=sql_Concat)
gen_sql_Multiply_Operands = Generalization(general=Operands, specific=sql_Multiply)
gen_sql_Division_Operands = Generalization(general=Operands, specific=sql_Division)
gen_sql_OBCArgs_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OBCArgs)
gen_sql_WhenList_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_WhenList)
gen_sql_AExpArgs_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AExpArgs)
gen_sql_OpFList_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFList)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Select, sql_Model, sql_WithQuery, sql_SelectQuery, sql_WithColumns, sql_FetchFirst, sql_UnsignedValue, sql_Offset, sql_Limit, sql_SelectSubSet, sql_ColumnFull, SelectQuery, sql_OrColumn, sql_OrTable, sql_OrExpr, sql_OrGroupByColumn, sql_OrOrderByColumn, PivotForClause, sql_ColumnOrAlias, OrColumn, sql_Operands, sql_DbObjectName, sql_DbObjectNameAll, sql_ColumnNames, FromValuesColumnNames, sql_FromTable, OrTable, sql_TableOrAlias, sql_FromTableJoin, sql_JoinCondition, sql_UsingCols, WithColumns, sql_TableFull, sql_SubQueryOperand, sql_FromValues, sql_PivotTable, sql_UnpivotTable, sql_Values, sql_FromValuesColumns, sql_FromValuesColumnNames, sql_Rows, sql_Row, Rows, sql_RowValues, sql_RowValue, RowValues, sql_PivotFunctions, sql_PivotForClause, sql_PivotInClause, sql_PivotFunction, sql_UnpivotInClauseArgs, sql_PivotColumns, sql_UnpivotInClause, sql_UnpivotInClauseArg, UnpivotInClauseArgs, sql_OpFunction, sql_Pivots, PivotColumns, sql_PivotCol, PivotFunction, Pivots, ColumnFull, UsingCols, PivotCol, TableFull, sql_OrderByColumnFull, OrOrderByColumn, sql_GroupByColumnFull, OrGroupByColumn, sql_Between, sql_FullExpression, OrExpr, sql_ExprGroup, sql_XExpr, sql_InOper, sql_ExistsOper, sql_Like, sql_Comparison, sql_Prms, sql_JRParameter, Prms, sql_LikeOperand, sql_OpFunctionCast, sql_POperand, sql_OperandListGroup, sql_OperandList, OpFunctionArgAgregate, sql_Operand, sql_ColumnOperand, sql_FunctionExtract, sql_SQLCaseOperand, sql_ExpOperand, sql_ScalarOperand, sql_OpFunctionArg, sql_FunctionAnalytical, sql_AnalyticClause, sql_QueryPartitionClause, sql_OrderByClause, sql_WindowingClause, AnalyticExprArgs, sql_WindowingClauseBetween, WindowingClause, sql_WindowingClauseOperandPreceding, sql_WindowingClauseOperandFollowing, sql_AnalyticExprArg, sql_OrderByClauseArgs, sql_OrderByClauseArg, OrderByClauseArgs, sql_AnalyticExprArgs, QueryPartitionClause, sql_OpFunctionArgOperand, OpFunctionArg, sql_OpFunctionArgAgregate, RowValue, OperandList, sql_SQLCaseWhens, sql_SqlCaseWhen, SQLCaseWhens, sql_IntegerValue, sql_Col, sql_abc, sql_UnipivotInClause, UnpivotInClause, sql_uicargs, sql_pvcs, sql_pcols, sql_tbls, sql_OpList, sql_Plus, Operands, sql_Minus, sql_Concat, sql_Multiply, sql_Division, sql_OBCArgs, sql_WhenList, sql_AExpArgs, sql_OpFList, XFunction, EXTRACT_VALUES},
    associations={query9, wq0, query1, withCols3, query5, fetchFirst8, op10, cols13, tbl15, whereExpression17, groupByEntry19, havingEntry21, orderByEntry24, lim26, offset28, fetchFirst30, entries33, ce35, colAlias37, dbAllCols39, fvCols77, entries41, table43, fjoin45, onTable47, joinExpr50, joinCond53, useCols55, entries57, tfull60, sq62, values64, pivot66, unpivot68, tblAlias70, values73, c75, pcols105, cfuls107, rows79, entries81, rowValues83, entries85, pfun87, pfor89, pin91, sq93, args96, pcols98, pfor100, inop103, colGrBy116, gbFunction119, entries110, colOrder112, entries114, between140, entries121, efrag124, expgroup126, exp129, xexp131, in133, exists135, op1137, like142, comp144, expr146, col149, prm152, left190, entries154, op2156, op2159, fop2161, fcast164, fparam166, op2168, op3171, subquery174, opList177, subquery179, opList182, opGroup185, op1187, right192, column195, xop198, subq200, fcast203, fext206, func208, sqlcase211, param213, eparam216, scalar218, args220, fan222, operand224, anClause227, abc229, obc231, winc233, wcoP235, wcoF236, exp238, expr240, args243, col245, args247, ce249, colAlias252, op255, op256, cfull259, expr275, sel262, wop265, expr268, when271, wop273, texp278, eexp281, entries292, entries284, entries286, args287, entries289, entries291, entries294, entries296, entries302, entries304, entries298, entries300},
    generalizations={gen_sql_ColumnFull_PivotForClause, gen_sql_Select_SelectQuery, gen_sql_OrColumn_PivotForClause, gen_sql_ColumnOrAlias_OrColumn, gen_sql_ColumnNames_FromValuesColumnNames, gen_sql_FromTable_OrTable, gen_sql_UsingCols_WithColumns, gen_sql_Row_Rows, gen_sql_RowValue_RowValues, gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs, gen_sql_Pivots_PivotColumns, gen_sql_PivotCol_PivotFunction, gen_sql_PivotCol_PivotColumns, gen_sql_PivotCol_Pivots, gen_sql_DbObjectName_ColumnFull, gen_sql_DbObjectName_UsingCols, gen_sql_DbObjectName_PivotCol, gen_sql_DbObjectName_TableFull, gen_sql_OrderByColumnFull_OrOrderByColumn, gen_sql_GroupByColumnFull_OrGroupByColumn, gen_sql_FullExpression_OrExpr, gen_sql_JRParameter_Prms, gen_sql_Operands_OpFunctionArgAgregate, gen_sql_AnalyticExprArgs_QueryPartitionClause, gen_sql_AnalyticExprArg_AnalyticExprArgs, gen_sql_WindowingClauseBetween_WindowingClause, gen_sql_WindowingClauseOperandPreceding_WindowingClause, gen_sql_OrderByClauseArg_OrderByClauseArgs, gen_sql_OpFunctionArgOperand_OpFunctionArg, gen_sql_ScalarOperand_RowValue, gen_sql_ScalarOperand_OperandList, gen_sql_SqlCaseWhen_SQLCaseWhens, gen_sql_Col_ColumnFull, gen_sql_abc_FromValuesColumnNames, gen_sql_UnipivotInClause_UnpivotInClause, gen_sql_uicargs_UnpivotInClauseArgs, gen_sql_pvcs_Pivots, gen_sql_pcols_PivotCol, gen_sql_tbls_TableFull, gen_sql_OpList_OperandList, gen_sql_Plus_Operands, gen_sql_Minus_Operands, gen_sql_Concat_Operands, gen_sql_Multiply_Operands, gen_sql_Division_Operands, gen_sql_OBCArgs_OrderByClauseArgs, gen_sql_WhenList_SQLCaseWhens, gen_sql_AExpArgs_AnalyticExprArgs, gen_sql_OpFList_OpFunctionArg},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
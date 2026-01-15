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
sql_FetchFirst = Class(name="sql::FetchFirst")
sql_UnsignedValue = Class(name="sql::UnsignedValue")
sql_Offset = Class(name="sql::Offset")
sql_OrExpr = Class(name="sql::OrExpr")
sql_OrGroupByColumn = Class(name="sql::OrGroupByColumn")
sql_OrOrderByColumn = Class(name="sql::OrOrderByColumn")
sql_Limit = Class(name="sql::Limit")
sql_SelectSubSet = Class(name="sql::SelectSubSet")
sql_Select = Class(name="sql::Select")
SelectQuery = Class(name="SelectQuery")
sql_OrColumn = Class(name="sql::OrColumn")
sql_OrTable = Class(name="sql::OrTable")
OrTable = Class(name="OrTable")
sql_TableOrAlias = Class(name="sql::TableOrAlias")
sql_FromTableJoin = Class(name="sql::FromTableJoin")
sql_JoinCondition = Class(name="sql::JoinCondition")
sql_UsingCols = Class(name="sql::UsingCols")
PivotForClause = Class(name="PivotForClause")
sql_ColumnOrAlias = Class(name="sql::ColumnOrAlias")
OrColumn = Class(name="OrColumn")
sql_Operands = Class(name="sql::Operands")
sql_DbObjectName = Class(name="sql::DbObjectName")
sql_DbObjectNameAll = Class(name="sql::DbObjectNameAll")
sql_ColumnFull = Class(name="sql::ColumnFull")
sql_FromTable = Class(name="sql::FromTable")
sql_Values = Class(name="sql::Values")
sql_FromValuesColumns = Class(name="sql::FromValuesColumns")
sql_FromValuesColumnNames = Class(name="sql::FromValuesColumnNames")
sql_ColumnNames = Class(name="sql::ColumnNames")
FromValuesColumnNames = Class(name="FromValuesColumnNames")
sql_Rows = Class(name="sql::Rows")
sql_Row = Class(name="sql::Row")
sql_TableFull = Class(name="sql::TableFull")
sql_SubQueryOperand = Class(name="sql::SubQueryOperand")
sql_FromValues = Class(name="sql::FromValues")
sql_PivotTable = Class(name="sql::PivotTable")
sql_UnpivotTable = Class(name="sql::UnpivotTable")
sql_PivotFunction = Class(name="sql::PivotFunction")
sql_UnpivotInClauseArgs = Class(name="sql::UnpivotInClauseArgs")
sql_PivotColumns = Class(name="sql::PivotColumns")
sql_UnpivotInClause = Class(name="sql::UnpivotInClause")
sql_UnpivotInClauseArg = Class(name="sql::UnpivotInClauseArg")
UnpivotInClauseArgs = Class(name="UnpivotInClauseArgs")
Rows = Class(name="Rows")
sql_RowValues = Class(name="sql::RowValues")
sql_RowValue = Class(name="sql::RowValue")
RowValues = Class(name="RowValues")
sql_PivotFunctions = Class(name="sql::PivotFunctions")
sql_PivotForClause = Class(name="sql::PivotForClause")
sql_PivotInClause = Class(name="sql::PivotInClause")
OrOrderByColumn = Class(name="OrOrderByColumn")
sql_GroupByColumnFull = Class(name="sql::GroupByColumnFull")
OrGroupByColumn = Class(name="OrGroupByColumn")
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
sql_Between = Class(name="sql::Between")
sql_Like = Class(name="sql::Like")
sql_Comparison = Class(name="sql::Comparison")
sql_FullExpression = Class(name="sql::FullExpression")
OrExpr = Class(name="OrExpr")
sql_ExprGroup = Class(name="sql::ExprGroup")
sql_XExpr = Class(name="sql::XExpr")
sql_InOper = Class(name="sql::InOper")
sql_ExistsOper = Class(name="sql::ExistsOper")
sql_LikeOperand = Class(name="sql::LikeOperand")
sql_OpFunctionCast = Class(name="sql::OpFunctionCast")
sql_POperand = Class(name="sql::POperand")
sql_Prms = Class(name="sql::Prms")
sql_JRParameter = Class(name="sql::JRParameter")
Prms = Class(name="Prms")
sql_ColumnOperand = Class(name="sql::ColumnOperand")
sql_OperandListGroup = Class(name="sql::OperandListGroup")
sql_OperandList = Class(name="sql::OperandList")
OpFunctionArgAgregate = Class(name="OpFunctionArgAgregate")
sql_Operand = Class(name="sql::Operand")
sql_ScalarOperand = Class(name="sql::ScalarOperand")
sql_OpFunctionArg = Class(name="sql::OpFunctionArg")
sql_FunctionAnalytical = Class(name="sql::FunctionAnalytical")
sql_FunctionExtract = Class(name="sql::FunctionExtract")
sql_SQLCaseOperand = Class(name="sql::SQLCaseOperand")
sql_ExpOperand = Class(name="sql::ExpOperand")
sql_OrderByClause = Class(name="sql::OrderByClause")
sql_WindowingClause = Class(name="sql::WindowingClause")
sql_WindowingClauseBetween = Class(name="sql::WindowingClauseBetween")
WindowingClause = Class(name="WindowingClause")
sql_WindowingClauseOperandPreceding = Class(name="sql::WindowingClauseOperandPreceding")
sql_WindowingClauseOperandFollowing = Class(name="sql::WindowingClauseOperandFollowing")
sql_AnalyticExprArg = Class(name="sql::AnalyticExprArg")
sql_AnalyticClause = Class(name="sql::AnalyticClause")
sql_QueryPartitionClause = Class(name="sql::QueryPartitionClause")
AnalyticExprArgs = Class(name="AnalyticExprArgs")
sql_OpFunctionArgOperand = Class(name="sql::OpFunctionArgOperand")
OpFunctionArg = Class(name="OpFunctionArg")
sql_OpFunctionArgAgregate = Class(name="sql::OpFunctionArgAgregate")
sql_OrderByClauseArgs = Class(name="sql::OrderByClauseArgs")
sql_OrderByClauseArg = Class(name="sql::OrderByClauseArg")
OrderByClauseArgs = Class(name="OrderByClauseArgs")
sql_AnalyticExprArgs = Class(name="sql::AnalyticExprArgs")
QueryPartitionClause = Class(name="QueryPartitionClause")
RowValue = Class(name="RowValue")
OperandList = Class(name="OperandList")
sql_SQLCaseWhens = Class(name="sql::SQLCaseWhens")
sql_SqlCaseWhen = Class(name="sql::SqlCaseWhen")
SQLCaseWhens = Class(name="SQLCaseWhens")
sql_pvcs = Class(name="sql::pvcs")
sql_pcols = Class(name="sql::pcols")
sql_tbls = Class(name="sql::tbls")
sql_OpList = Class(name="sql::OpList")
sql_Plus = Class(name="sql::Plus")
Operands = Class(name="Operands")
sql_Minus = Class(name="sql::Minus")
sql_IntegerValue = Class(name="sql::IntegerValue")
sql_Col = Class(name="sql::Col")
sql_abc = Class(name="sql::abc")
sql_UnipivotInClause = Class(name="sql::UnipivotInClause")
UnpivotInClause = Class(name="UnpivotInClause")
sql_uicargs = Class(name="sql::uicargs")
sql_Concat = Class(name="sql::Concat")
sql_Multiply = Class(name="sql::Multiply")
sql_Division = Class(name="sql::Division")
sql_OBCArgs = Class(name="sql::OBCArgs")
sql_AExpArgs = Class(name="sql::AExpArgs")
sql_OpFList = Class(name="sql::OpFList")
sql_WhenList = Class(name="sql::WhenList")

# sql_Model class attributes and methods

# sql_SelectQuery class attributes and methods

# sql_FetchFirst class attributes and methods
sql_FetchFirst_row: Property = Property(name="row", type=StringType)
sql_FetchFirst.attributes={sql_FetchFirst_row}

# sql_UnsignedValue class attributes and methods
sql_UnsignedValue_integer: Property = Property(name="integer", type=StringType)
sql_UnsignedValue.attributes={sql_UnsignedValue_integer}

# sql_Offset class attributes and methods
sql_Offset_offset: Property = Property(name="offset", type=StringType)
sql_Offset.attributes={sql_Offset_offset}

# sql_OrExpr class attributes and methods

# sql_OrGroupByColumn class attributes and methods

# sql_OrOrderByColumn class attributes and methods

# sql_Limit class attributes and methods
sql_Limit_l1: Property = Property(name="l1", type=StringType)
sql_Limit_l2: Property = Property(name="l2", type=StringType)
sql_Limit.attributes={sql_Limit_l2, sql_Limit_l1}

# sql_SelectSubSet class attributes and methods
sql_SelectSubSet_op: Property = Property(name="op", type=StringType)
sql_SelectSubSet_all: Property = Property(name="all", type=StringType)
sql_SelectSubSet.attributes={sql_SelectSubSet_op, sql_SelectSubSet_all}

# sql_Select class attributes and methods
sql_Select_select: Property = Property(name="select", type=StringType)
sql_Select.attributes={sql_Select_select}

# SelectQuery class attributes and methods

# sql_OrColumn class attributes and methods

# sql_OrTable class attributes and methods

# OrTable class attributes and methods

# sql_TableOrAlias class attributes and methods
sql_TableOrAlias_alias: Property = Property(name="alias", type=StringType)
sql_TableOrAlias.attributes={sql_TableOrAlias_alias}

# sql_FromTableJoin class attributes and methods
sql_FromTableJoin_join: Property = Property(name="join", type=StringType)
sql_FromTableJoin.attributes={sql_FromTableJoin_join}

# sql_JoinCondition class attributes and methods

# sql_UsingCols class attributes and methods

# PivotForClause class attributes and methods

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

# sql_ColumnFull class attributes and methods

# sql_FromTable class attributes and methods

# sql_Values class attributes and methods

# sql_FromValuesColumns class attributes and methods

# sql_FromValuesColumnNames class attributes and methods

# sql_ColumnNames class attributes and methods
sql_ColumnNames_colName: Property = Property(name="colName", type=StringType)
sql_ColumnNames.attributes={sql_ColumnNames_colName}

# FromValuesColumnNames class attributes and methods

# sql_Rows class attributes and methods

# sql_Row class attributes and methods

# sql_TableFull class attributes and methods

# sql_SubQueryOperand class attributes and methods

# sql_FromValues class attributes and methods

# sql_PivotTable class attributes and methods

# sql_UnpivotTable class attributes and methods

# sql_PivotFunction class attributes and methods

# sql_UnpivotInClauseArgs class attributes and methods

# sql_PivotColumns class attributes and methods

# sql_UnpivotInClause class attributes and methods

# sql_UnpivotInClauseArg class attributes and methods

# UnpivotInClauseArgs class attributes and methods

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

# OrOrderByColumn class attributes and methods

# sql_GroupByColumnFull class attributes and methods
sql_GroupByColumnFull_grByInt: Property = Property(name="grByInt", type=StringType)
sql_GroupByColumnFull.attributes={sql_GroupByColumnFull_grByInt}

# OrGroupByColumn class attributes and methods

# sql_OpFunction class attributes and methods
sql_OpFunction_fname: Property = Property(name="fname", type=StringType)
sql_OpFunction_star: Property = Property(name="star", type=StringType)
sql_OpFunction.attributes={sql_OpFunction_fname, sql_OpFunction_star}

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

# sql_Between class attributes and methods
sql_Between_opBetween: Property = Property(name="opBetween", type=StringType)
sql_Between.attributes={sql_Between_opBetween}

# sql_Like class attributes and methods
sql_Like_opLike: Property = Property(name="opLike", type=StringType)
sql_Like.attributes={sql_Like_opLike}

# sql_Comparison class attributes and methods
sql_Comparison_operator: Property = Property(name="operator", type=StringType)
sql_Comparison_subOperator: Property = Property(name="subOperator", type=StringType)
sql_Comparison.attributes={sql_Comparison_operator, sql_Comparison_subOperator}

# sql_FullExpression class attributes and methods
sql_FullExpression_isnull: Property = Property(name="isnull", type=StringType)
sql_FullExpression_c: Property = Property(name="c", type=StringType)
sql_FullExpression_notPrm: Property = Property(name="notPrm", type=StringType)
sql_FullExpression.attributes={sql_FullExpression_isnull, sql_FullExpression_c, sql_FullExpression_notPrm}

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

# sql_LikeOperand class attributes and methods
sql_LikeOperand_op2: Property = Property(name="op2", type=StringType)
sql_LikeOperand.attributes={sql_LikeOperand_op2}

# sql_OpFunctionCast class attributes and methods
sql_OpFunctionCast_type: Property = Property(name="type", type=StringType)
sql_OpFunctionCast_p: Property = Property(name="p", type=StringType)
sql_OpFunctionCast_p2: Property = Property(name="p2", type=StringType)
sql_OpFunctionCast.attributes={sql_OpFunctionCast_p2, sql_OpFunctionCast_type, sql_OpFunctionCast_p}

# sql_POperand class attributes and methods
sql_POperand_prm: Property = Property(name="prm", type=StringType)
sql_POperand.attributes={sql_POperand_prm}

# sql_Prms class attributes and methods

# sql_JRParameter class attributes and methods
sql_JRParameter_jrprm: Property = Property(name="jrprm", type=StringType)
sql_JRParameter.attributes={sql_JRParameter_jrprm}

# Prms class attributes and methods

# sql_ColumnOperand class attributes and methods
sql_ColumnOperand_ora: Property = Property(name="ora", type=StringType)
sql_ColumnOperand.attributes={sql_ColumnOperand_ora}

# sql_OperandListGroup class attributes and methods

# sql_OperandList class attributes and methods

# OpFunctionArgAgregate class attributes and methods

# sql_Operand class attributes and methods

# sql_ScalarOperand class attributes and methods
sql_ScalarOperand_sostr: Property = Property(name="sostr", type=StringType)
sql_ScalarOperand_sodbl: Property = Property(name="sodbl", type=StringType)
sql_ScalarOperand_sodate: Property = Property(name="sodate", type=StringType)
sql_ScalarOperand_sotime: Property = Property(name="sotime", type=StringType)
sql_ScalarOperand_sodt: Property = Property(name="sodt", type=StringType)
sql_ScalarOperand_soUInt: Property = Property(name="soUInt", type=StringType)
sql_ScalarOperand_soint: Property = Property(name="soint", type=StringType)
sql_ScalarOperand.attributes={sql_ScalarOperand_sostr, sql_ScalarOperand_sodt, sql_ScalarOperand_sodate, sql_ScalarOperand_soUInt, sql_ScalarOperand_soint, sql_ScalarOperand_sodbl, sql_ScalarOperand_sotime}

# sql_OpFunctionArg class attributes and methods

# sql_FunctionAnalytical class attributes and methods

# sql_FunctionExtract class attributes and methods
sql_FunctionExtract_v: Property = Property(name="v", type=StringType)
sql_FunctionExtract.attributes={sql_FunctionExtract_v}

# sql_SQLCaseOperand class attributes and methods

# sql_ExpOperand class attributes and methods
sql_ExpOperand_prm: Property = Property(name="prm", type=StringType)
sql_ExpOperand.attributes={sql_ExpOperand_prm}

# sql_OrderByClause class attributes and methods

# sql_WindowingClause class attributes and methods

# sql_WindowingClauseBetween class attributes and methods

# WindowingClause class attributes and methods

# sql_WindowingClauseOperandPreceding class attributes and methods

# sql_WindowingClauseOperandFollowing class attributes and methods

# sql_AnalyticExprArg class attributes and methods

# sql_AnalyticClause class attributes and methods

# sql_QueryPartitionClause class attributes and methods

# AnalyticExprArgs class attributes and methods

# sql_OpFunctionArgOperand class attributes and methods

# OpFunctionArg class attributes and methods

# sql_OpFunctionArgAgregate class attributes and methods

# sql_OrderByClauseArgs class attributes and methods

# sql_OrderByClauseArg class attributes and methods

# OrderByClauseArgs class attributes and methods

# sql_AnalyticExprArgs class attributes and methods

# QueryPartitionClause class attributes and methods

# RowValue class attributes and methods

# OperandList class attributes and methods

# sql_SQLCaseWhens class attributes and methods

# sql_SqlCaseWhen class attributes and methods

# SQLCaseWhens class attributes and methods

# sql_pvcs class attributes and methods

# sql_pcols class attributes and methods

# sql_tbls class attributes and methods

# sql_OpList class attributes and methods

# sql_Plus class attributes and methods

# Operands class attributes and methods

# sql_Minus class attributes and methods

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

# sql_Concat class attributes and methods

# sql_Multiply class attributes and methods

# sql_Division class attributes and methods

# sql_OBCArgs class attributes and methods

# sql_AExpArgs class attributes and methods

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
fetchFirst1: BinaryAssociation = BinaryAssociation(
    name="fetchFirst1",
    ends={
        Property(name="sql_UnsignedValue", type=sql_FetchFirst, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FetchFirst", type=sql_UnsignedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression10: BinaryAssociation = BinaryAssociation(
    name="whereExpression10",
    ends={
        Property(name="sql_OrExpr", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select11", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByEntry12: BinaryAssociation = BinaryAssociation(
    name="groupByEntry12",
    ends={
        Property(name="sql_OrGroupByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select13", type=sql_OrGroupByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
havingEntry14: BinaryAssociation = BinaryAssociation(
    name="havingEntry14",
    ends={
        Property(name="sql_OrExpr16", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select15", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderByEntry17: BinaryAssociation = BinaryAssociation(
    name="orderByEntry17",
    ends={
        Property(name="sql_OrOrderByColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select18", type=sql_OrOrderByColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lim19: BinaryAssociation = BinaryAssociation(
    name="lim19",
    ends={
        Property(name="sql_Limit", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select20", type=sql_Limit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offset21: BinaryAssociation = BinaryAssociation(
    name="offset21",
    ends={
        Property(name="sql_Offset", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select22", type=sql_Offset, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query2: BinaryAssociation = BinaryAssociation(
    name="query2",
    ends={
        Property(name="sql_Select", type=sql_SelectSubSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectSubSet", type=sql_Select, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op3: BinaryAssociation = BinaryAssociation(
    name="op3",
    ends={
        Property(name="sql_SelectSubSet5", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select4", type=sql_SelectSubSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols6: BinaryAssociation = BinaryAssociation(
    name="cols6",
    ends={
        Property(name="sql_OrColumn", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select7", type=sql_OrColumn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbl8: BinaryAssociation = BinaryAssociation(
    name="tbl8",
    ends={
        Property(name="sql_OrTable", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select9", type=sql_OrTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries34: BinaryAssociation = BinaryAssociation(
    name="entries34",
    ends={
        Property(name="sql_FromTable", type=sql_OrTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrTable35", type=sql_FromTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table36: BinaryAssociation = BinaryAssociation(
    name="table36",
    ends={
        Property(name="sql_TableOrAlias", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable37", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fjoin38: BinaryAssociation = BinaryAssociation(
    name="fjoin38",
    ends={
        Property(name="sql_FromTableJoin", type=sql_FromTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTable39", type=sql_FromTableJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onTable40: BinaryAssociation = BinaryAssociation(
    name="onTable40",
    ends={
        Property(name="sql_TableOrAlias42", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin41", type=sql_TableOrAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinExpr43: BinaryAssociation = BinaryAssociation(
    name="joinExpr43",
    ends={
        Property(name="sql_OrExpr45", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin44", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinCond46: BinaryAssociation = BinaryAssociation(
    name="joinCond46",
    ends={
        Property(name="sql_JoinCondition", type=sql_FromTableJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromTableJoin47", type=sql_JoinCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fetchFirst23: BinaryAssociation = BinaryAssociation(
    name="fetchFirst23",
    ends={
        Property(name="sql_FetchFirst25", type=sql_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Select24", type=sql_FetchFirst, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries26: BinaryAssociation = BinaryAssociation(
    name="entries26",
    ends={
        Property(name="sql_ColumnOrAlias", type=sql_OrColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrColumn27", type=sql_ColumnOrAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ce28: BinaryAssociation = BinaryAssociation(
    name="ce28",
    ends={
        Property(name="sql_Operands", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias29", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias30: BinaryAssociation = BinaryAssociation(
    name="colAlias30",
    ends={
        Property(name="sql_DbObjectName", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias31", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dbAllCols32: BinaryAssociation = BinaryAssociation(
    name="dbAllCols32",
    ends={
        Property(name="sql_DbObjectNameAll", type=sql_ColumnOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOrAlias33", type=sql_DbObjectNameAll, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values66: BinaryAssociation = BinaryAssociation(
    name="values66",
    ends={
        Property(name="sql_Values", type=sql_FromValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValues67", type=sql_Values, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c68: BinaryAssociation = BinaryAssociation(
    name="c68",
    ends={
        Property(name="sql_FromValuesColumns", type=sql_FromValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValues69", type=sql_FromValuesColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fvCols70: BinaryAssociation = BinaryAssociation(
    name="fvCols70",
    ends={
        Property(name="sql_FromValuesColumnNames", type=sql_FromValuesColumns, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FromValuesColumns71", type=sql_FromValuesColumnNames, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows72: BinaryAssociation = BinaryAssociation(
    name="rows72",
    ends={
        Property(name="sql_Rows", type=sql_Values, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Values73", type=sql_Rows, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
useCols48: BinaryAssociation = BinaryAssociation(
    name="useCols48",
    ends={
        Property(name="sql_UsingCols", type=sql_JoinCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_JoinCondition49", type=sql_UsingCols, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries50: BinaryAssociation = BinaryAssociation(
    name="entries50",
    ends={
        Property(name="sql_DbObjectName52", type=sql_UsingCols, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UsingCols51", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tfull53: BinaryAssociation = BinaryAssociation(
    name="tfull53",
    ends={
        Property(name="sql_TableFull", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias54", type=sql_TableFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq55: BinaryAssociation = BinaryAssociation(
    name="sq55",
    ends={
        Property(name="sql_SubQueryOperand", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias56", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values57: BinaryAssociation = BinaryAssociation(
    name="values57",
    ends={
        Property(name="sql_FromValues", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias58", type=sql_FromValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pivot59: BinaryAssociation = BinaryAssociation(
    name="pivot59",
    ends={
        Property(name="sql_PivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias60", type=sql_PivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpivot61: BinaryAssociation = BinaryAssociation(
    name="unpivot61",
    ends={
        Property(name="sql_UnpivotTable", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias62", type=sql_UnpivotTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tblAlias63: BinaryAssociation = BinaryAssociation(
    name="tblAlias63",
    ends={
        Property(name="sql_DbObjectName65", type=sql_TableOrAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_TableOrAlias64", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sq86: BinaryAssociation = BinaryAssociation(
    name="sq86",
    ends={
        Property(name="sql_SubQueryOperand88", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause87", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args89: BinaryAssociation = BinaryAssociation(
    name="args89",
    ends={
        Property(name="sql_UnpivotInClauseArgs", type=sql_PivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotInClause90", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols91: BinaryAssociation = BinaryAssociation(
    name="pcols91",
    ends={
        Property(name="sql_PivotColumns", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable92", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor93: BinaryAssociation = BinaryAssociation(
    name="pfor93",
    ends={
        Property(name="sql_PivotForClause95", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable94", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inop96: BinaryAssociation = BinaryAssociation(
    name="inop96",
    ends={
        Property(name="sql_UnpivotInClause", type=sql_UnpivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotTable97", type=sql_UnpivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries74: BinaryAssociation = BinaryAssociation(
    name="entries74",
    ends={
        Property(name="sql_Row", type=sql_Rows, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Rows75", type=sql_Row, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rowValues76: BinaryAssociation = BinaryAssociation(
    name="rowValues76",
    ends={
        Property(name="sql_RowValues", type=sql_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Row77", type=sql_RowValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries78: BinaryAssociation = BinaryAssociation(
    name="entries78",
    ends={
        Property(name="sql_RowValue", type=sql_RowValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_RowValues79", type=sql_RowValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pfun80: BinaryAssociation = BinaryAssociation(
    name="pfun80",
    ends={
        Property(name="sql_PivotFunctions", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable81", type=sql_PivotFunctions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pfor82: BinaryAssociation = BinaryAssociation(
    name="pfor82",
    ends={
        Property(name="sql_PivotForClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable83", type=sql_PivotForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pin84: BinaryAssociation = BinaryAssociation(
    name="pin84",
    ends={
        Property(name="sql_PivotInClause", type=sql_PivotTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_PivotTable85", type=sql_PivotInClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries103: BinaryAssociation = BinaryAssociation(
    name="entries103",
    ends={
        Property(name="sql_OrderByColumnFull", type=sql_OrOrderByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrOrderByColumn104", type=sql_OrderByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colOrder105: BinaryAssociation = BinaryAssociation(
    name="colOrder105",
    ends={
        Property(name="sql_ColumnFull", type=sql_OrderByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByColumnFull106", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries107: BinaryAssociation = BinaryAssociation(
    name="entries107",
    ends={
        Property(name="sql_GroupByColumnFull", type=sql_OrGroupByColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrGroupByColumn108", type=sql_GroupByColumnFull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colGrBy109: BinaryAssociation = BinaryAssociation(
    name="colGrBy109",
    ends={
        Property(name="sql_ColumnFull111", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull110", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gbFunction112: BinaryAssociation = BinaryAssociation(
    name="gbFunction112",
    ends={
        Property(name="sql_OpFunction", type=sql_GroupByColumnFull, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_GroupByColumnFull113", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pcols98: BinaryAssociation = BinaryAssociation(
    name="pcols98",
    ends={
        Property(name="sql_PivotColumns99", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfuls100: BinaryAssociation = BinaryAssociation(
    name="cfuls100",
    ends={
        Property(name="sql_PivotColumns102", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnpivotInClauseArg101", type=sql_PivotColumns, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1130: BinaryAssociation = BinaryAssociation(
    name="op1130",
    ends={
        Property(name="sql_Operands132", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression131", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
between133: BinaryAssociation = BinaryAssociation(
    name="between133",
    ends={
        Property(name="sql_Between", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression134", type=sql_Between, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
like135: BinaryAssociation = BinaryAssociation(
    name="like135",
    ends={
        Property(name="sql_Like", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression136", type=sql_Like, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comp137: BinaryAssociation = BinaryAssociation(
    name="comp137",
    ends={
        Property(name="sql_Comparison", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression138", type=sql_Comparison, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries114: BinaryAssociation = BinaryAssociation(
    name="entries114",
    ends={
        Property(name="sql_FullExpression", type=sql_OrExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrExpr115", type=sql_FullExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
efrag117: BinaryAssociation = BinaryAssociation(
    name="efrag117",
    ends={
        Property(name="sql_FullExpression118", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression116", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expgroup119: BinaryAssociation = BinaryAssociation(
    name="expgroup119",
    ends={
        Property(name="sql_ExprGroup", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression120", type=sql_ExprGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp122: BinaryAssociation = BinaryAssociation(
    name="exp122",
    ends={
        Property(name="sql_FullExpression123", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression121", type=sql_FullExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xexp124: BinaryAssociation = BinaryAssociation(
    name="xexp124",
    ends={
        Property(name="sql_XExpr", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression125", type=sql_XExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in126: BinaryAssociation = BinaryAssociation(
    name="in126",
    ends={
        Property(name="sql_InOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression127", type=sql_InOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exists128: BinaryAssociation = BinaryAssociation(
    name="exists128",
    ends={
        Property(name="sql_ExistsOper", type=sql_FullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FullExpression129", type=sql_ExistsOper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2152: BinaryAssociation = BinaryAssociation(
    name="op2152",
    ends={
        Property(name="sql_LikeOperand", type=sql_Like, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Like153", type=sql_LikeOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fop2154: BinaryAssociation = BinaryAssociation(
    name="fop2154",
    ends={
        Property(name="sql_OpFunction156", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand155", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast157: BinaryAssociation = BinaryAssociation(
    name="fcast157",
    ends={
        Property(name="sql_OpFunctionCast", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand158", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fparam159: BinaryAssociation = BinaryAssociation(
    name="fparam159",
    ends={
        Property(name="sql_POperand", type=sql_LikeOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_LikeOperand160", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op2161: BinaryAssociation = BinaryAssociation(
    name="op2161",
    ends={
        Property(name="sql_Operands163", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between162", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op3164: BinaryAssociation = BinaryAssociation(
    name="op3164",
    ends={
        Property(name="sql_Operands166", type=sql_Between, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Between165", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr139: BinaryAssociation = BinaryAssociation(
    name="expr139",
    ends={
        Property(name="sql_OrExpr141", type=sql_ExprGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExprGroup140", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col142: BinaryAssociation = BinaryAssociation(
    name="col142",
    ends={
        Property(name="sql_Operands144", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr143", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prm145: BinaryAssociation = BinaryAssociation(
    name="prm145",
    ends={
        Property(name="sql_Prms", type=sql_XExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_XExpr146", type=sql_Prms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries147: BinaryAssociation = BinaryAssociation(
    name="entries147",
    ends={
        Property(name="sql_JRParameter", type=sql_Prms, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Prms148", type=sql_JRParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op2149: BinaryAssociation = BinaryAssociation(
    name="op2149",
    ends={
        Property(name="sql_Operands151", type=sql_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Comparison150", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op1180: BinaryAssociation = BinaryAssociation(
    name="op1180",
    ends={
        Property(name="sql_Operand", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands181", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left183: BinaryAssociation = BinaryAssociation(
    name="left183",
    ends={
        Property(name="sql_Operands184", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands182", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right185: BinaryAssociation = BinaryAssociation(
    name="right185",
    ends={
        Property(name="sql_Operand187", type=sql_Operands, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operands186", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column188: BinaryAssociation = BinaryAssociation(
    name="column188",
    ends={
        Property(name="sql_ColumnOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand189", type=sql_ColumnOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery167: BinaryAssociation = BinaryAssociation(
    name="subquery167",
    ends={
        Property(name="sql_SubQueryOperand169", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper168", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList170: BinaryAssociation = BinaryAssociation(
    name="opList170",
    ends={
        Property(name="sql_OperandListGroup", type=sql_InOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_InOper171", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subquery172: BinaryAssociation = BinaryAssociation(
    name="subquery172",
    ends={
        Property(name="sql_SubQueryOperand174", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper173", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opList175: BinaryAssociation = BinaryAssociation(
    name="opList175",
    ends={
        Property(name="sql_OperandListGroup177", type=sql_ExistsOper, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ExistsOper176", type=sql_OperandListGroup, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opGroup178: BinaryAssociation = BinaryAssociation(
    name="opGroup178",
    ends={
        Property(name="sql_OperandList", type=sql_OperandListGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OperandListGroup179", type=sql_OperandList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eparam209: BinaryAssociation = BinaryAssociation(
    name="eparam209",
    ends={
        Property(name="sql_ExpOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand210", type=sql_ExpOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scalar211: BinaryAssociation = BinaryAssociation(
    name="scalar211",
    ends={
        Property(name="sql_ScalarOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand212", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args213: BinaryAssociation = BinaryAssociation(
    name="args213",
    ends={
        Property(name="sql_OpFunctionArg", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction214", type=sql_OpFunctionArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fan215: BinaryAssociation = BinaryAssociation(
    name="fan215",
    ends={
        Property(name="sql_FunctionAnalytical", type=sql_OpFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunction216", type=sql_FunctionAnalytical, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand217: BinaryAssociation = BinaryAssociation(
    name="operand217",
    ends={
        Property(name="sql_Operands219", type=sql_FunctionExtract, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionExtract218", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xop191: BinaryAssociation = BinaryAssociation(
    name="xop191",
    ends={
        Property(name="sql_Operand192", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand190", type=sql_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subq193: BinaryAssociation = BinaryAssociation(
    name="subq193",
    ends={
        Property(name="sql_SubQueryOperand195", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand194", type=sql_SubQueryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fcast196: BinaryAssociation = BinaryAssociation(
    name="fcast196",
    ends={
        Property(name="sql_OpFunctionCast198", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand197", type=sql_OpFunctionCast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fext199: BinaryAssociation = BinaryAssociation(
    name="fext199",
    ends={
        Property(name="sql_FunctionExtract", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand200", type=sql_FunctionExtract, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func201: BinaryAssociation = BinaryAssociation(
    name="func201",
    ends={
        Property(name="sql_OpFunction203", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand202", type=sql_OpFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sqlcase204: BinaryAssociation = BinaryAssociation(
    name="sqlcase204",
    ends={
        Property(name="sql_SQLCaseOperand", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand205", type=sql_SQLCaseOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param206: BinaryAssociation = BinaryAssociation(
    name="param206",
    ends={
        Property(name="sql_POperand208", type=sql_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Operand207", type=sql_POperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obc224: BinaryAssociation = BinaryAssociation(
    name="obc224",
    ends={
        Property(name="sql_OrderByClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause225", type=sql_OrderByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
winc226: BinaryAssociation = BinaryAssociation(
    name="winc226",
    ends={
        Property(name="sql_WindowingClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause227", type=sql_WindowingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoP228: BinaryAssociation = BinaryAssociation(
    name="wcoP228",
    ends={
        Property(name="sql_WindowingClauseOperandPreceding", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcoF229: BinaryAssociation = BinaryAssociation(
    name="wcoF229",
    ends={
        Property(name="sql_WindowingClauseOperandFollowing", type=sql_WindowingClauseBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseBetween230", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anClause220: BinaryAssociation = BinaryAssociation(
    name="anClause220",
    ends={
        Property(name="sql_AnalyticClause", type=sql_FunctionAnalytical, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_FunctionAnalytical221", type=sql_AnalyticClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abc222: BinaryAssociation = BinaryAssociation(
    name="abc222",
    ends={
        Property(name="sql_QueryPartitionClause", type=sql_AnalyticClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticClause223", type=sql_QueryPartitionClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ce242: BinaryAssociation = BinaryAssociation(
    name="ce242",
    ends={
        Property(name="sql_Operands244", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg243", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colAlias245: BinaryAssociation = BinaryAssociation(
    name="colAlias245",
    ends={
        Property(name="sql_DbObjectName247", type=sql_AnalyticExprArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AnalyticExprArg246", type=sql_DbObjectName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op248: BinaryAssociation = BinaryAssociation(
    name="op248",
    ends={
        Property(name="sql_OpFunctionArgAgregate", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionArgOperand", type=sql_OpFunctionArgAgregate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op249: BinaryAssociation = BinaryAssociation(
    name="op249",
    ends={
        Property(name="sql_Operands251", type=sql_OpFunctionCast, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFunctionCast250", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp231: BinaryAssociation = BinaryAssociation(
    name="exp231",
    ends={
        Property(name="sql_AnalyticExprArg", type=sql_WindowingClauseOperandFollowing, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandFollowing232", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr233: BinaryAssociation = BinaryAssociation(
    name="expr233",
    ends={
        Property(name="sql_AnalyticExprArg235", type=sql_WindowingClauseOperandPreceding, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WindowingClauseOperandPreceding234", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args236: BinaryAssociation = BinaryAssociation(
    name="args236",
    ends={
        Property(name="sql_OrderByClauseArgs", type=sql_OrderByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClause237", type=sql_OrderByClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col238: BinaryAssociation = BinaryAssociation(
    name="col238",
    ends={
        Property(name="sql_AnalyticExprArg239", type=sql_OrderByClauseArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OrderByClauseArg", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args240: BinaryAssociation = BinaryAssociation(
    name="args240",
    ends={
        Property(name="sql_AnalyticExprArgs", type=sql_QueryPartitionClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_QueryPartitionClause241", type=sql_AnalyticExprArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eexp268: BinaryAssociation = BinaryAssociation(
    name="eexp268",
    ends={
        Property(name="sql_Operands270", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen269", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cfull252: BinaryAssociation = BinaryAssociation(
    name="cfull252",
    ends={
        Property(name="sql_ColumnFull254", type=sql_ColumnOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_ColumnOperand253", type=sql_ColumnFull, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sel255: BinaryAssociation = BinaryAssociation(
    name="sel255",
    ends={
        Property(name="sql_SelectQuery257", type=sql_SubQueryOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SubQueryOperand256", type=sql_SelectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr258: BinaryAssociation = BinaryAssociation(
    name="expr258",
    ends={
        Property(name="sql_OrExpr260", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand259", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when261: BinaryAssociation = BinaryAssociation(
    name="when261",
    ends={
        Property(name="sql_SQLCaseWhens", type=sql_SQLCaseOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SQLCaseOperand262", type=sql_SQLCaseWhens, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr263: BinaryAssociation = BinaryAssociation(
    name="expr263",
    ends={
        Property(name="sql_OrExpr264", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen", type=sql_OrExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
texp265: BinaryAssociation = BinaryAssociation(
    name="texp265",
    ends={
        Property(name="sql_Operands267", type=sql_SqlCaseWhen, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SqlCaseWhen266", type=sql_Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries276: BinaryAssociation = BinaryAssociation(
    name="entries276",
    ends={
        Property(name="sql_UnpivotInClauseArg277", type=sql_uicargs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_uicargs", type=sql_UnpivotInClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries278: BinaryAssociation = BinaryAssociation(
    name="entries278",
    ends={
        Property(name="sql_PivotCol", type=sql_pvcs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pvcs", type=sql_PivotCol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries279: BinaryAssociation = BinaryAssociation(
    name="entries279",
    ends={
        Property(name="sql_DbObjectName280", type=sql_pcols, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_pcols", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries281: BinaryAssociation = BinaryAssociation(
    name="entries281",
    ends={
        Property(name="sql_DbObjectName282", type=sql_tbls, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_tbls", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries283: BinaryAssociation = BinaryAssociation(
    name="entries283",
    ends={
        Property(name="sql_ScalarOperand284", type=sql_OpList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpList", type=sql_ScalarOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries271: BinaryAssociation = BinaryAssociation(
    name="entries271",
    ends={
        Property(name="sql_DbObjectName272", type=sql_Col, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Col", type=sql_DbObjectName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries273: BinaryAssociation = BinaryAssociation(
    name="entries273",
    ends={
        Property(name="sql_ColumnNames", type=sql_abc, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_abc", type=sql_ColumnNames, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args274: BinaryAssociation = BinaryAssociation(
    name="args274",
    ends={
        Property(name="sql_UnpivotInClauseArgs275", type=sql_UnipivotInClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_UnipivotInClause", type=sql_UnpivotInClauseArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries285: BinaryAssociation = BinaryAssociation(
    name="entries285",
    ends={
        Property(name="sql_OrderByClauseArg286", type=sql_OBCArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OBCArgs", type=sql_OrderByClauseArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries287: BinaryAssociation = BinaryAssociation(
    name="entries287",
    ends={
        Property(name="sql_AnalyticExprArg288", type=sql_AExpArgs, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_AExpArgs", type=sql_AnalyticExprArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries289: BinaryAssociation = BinaryAssociation(
    name="entries289",
    ends={
        Property(name="sql_OpFunctionArgOperand290", type=sql_OpFList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_OpFList", type=sql_OpFunctionArgOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries291: BinaryAssociation = BinaryAssociation(
    name="entries291",
    ends={
        Property(name="sql_SqlCaseWhen292", type=sql_WhenList, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_WhenList", type=sql_SqlCaseWhen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sql_Select_SelectQuery = Generalization(general=SelectQuery, specific=sql_Select)
gen_sql_FromTable_OrTable = Generalization(general=OrTable, specific=sql_FromTable)
gen_sql_OrColumn_PivotForClause = Generalization(general=PivotForClause, specific=sql_OrColumn)
gen_sql_ColumnOrAlias_OrColumn = Generalization(general=OrColumn, specific=sql_ColumnOrAlias)
gen_sql_ColumnFull_PivotForClause = Generalization(general=PivotForClause, specific=sql_ColumnFull)
gen_sql_ColumnNames_FromValuesColumnNames = Generalization(general=FromValuesColumnNames, specific=sql_ColumnNames)
gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_UnpivotInClauseArg)
gen_sql_Row_Rows = Generalization(general=Rows, specific=sql_Row)
gen_sql_RowValue_RowValues = Generalization(general=RowValues, specific=sql_RowValue)
gen_sql_OrderByColumnFull_OrOrderByColumn = Generalization(general=OrOrderByColumn, specific=sql_OrderByColumnFull)
gen_sql_GroupByColumnFull_OrGroupByColumn = Generalization(general=OrGroupByColumn, specific=sql_GroupByColumnFull)
gen_sql_Pivots_PivotColumns = Generalization(general=PivotColumns, specific=sql_Pivots)
gen_sql_PivotCol_PivotFunction = Generalization(general=PivotFunction, specific=sql_PivotCol)
gen_sql_PivotCol_PivotColumns = Generalization(general=PivotColumns, specific=sql_PivotCol)
gen_sql_PivotCol_Pivots = Generalization(general=Pivots, specific=sql_PivotCol)
gen_sql_DbObjectName_ColumnFull = Generalization(general=ColumnFull, specific=sql_DbObjectName)
gen_sql_DbObjectName_UsingCols = Generalization(general=UsingCols, specific=sql_DbObjectName)
gen_sql_DbObjectName_PivotCol = Generalization(general=PivotCol, specific=sql_DbObjectName)
gen_sql_DbObjectName_TableFull = Generalization(general=TableFull, specific=sql_DbObjectName)
gen_sql_FullExpression_OrExpr = Generalization(general=OrExpr, specific=sql_FullExpression)
gen_sql_JRParameter_Prms = Generalization(general=Prms, specific=sql_JRParameter)
gen_sql_Operands_OpFunctionArgAgregate = Generalization(general=OpFunctionArgAgregate, specific=sql_Operands)
gen_sql_WindowingClauseBetween_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseBetween)
gen_sql_AnalyticExprArg_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AnalyticExprArg)
gen_sql_OpFunctionArgOperand_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFunctionArgOperand)
gen_sql_WindowingClauseOperandPreceding_WindowingClause = Generalization(general=WindowingClause, specific=sql_WindowingClauseOperandPreceding)
gen_sql_OrderByClauseArg_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OrderByClauseArg)
gen_sql_AnalyticExprArgs_QueryPartitionClause = Generalization(general=QueryPartitionClause, specific=sql_AnalyticExprArgs)
gen_sql_ScalarOperand_RowValue = Generalization(general=RowValue, specific=sql_ScalarOperand)
gen_sql_ScalarOperand_OperandList = Generalization(general=OperandList, specific=sql_ScalarOperand)
gen_sql_SqlCaseWhen_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_SqlCaseWhen)
gen_sql_pvcs_Pivots = Generalization(general=Pivots, specific=sql_pvcs)
gen_sql_pcols_PivotCol = Generalization(general=PivotCol, specific=sql_pcols)
gen_sql_tbls_TableFull = Generalization(general=TableFull, specific=sql_tbls)
gen_sql_OpList_OperandList = Generalization(general=OperandList, specific=sql_OpList)
gen_sql_Plus_Operands = Generalization(general=Operands, specific=sql_Plus)
gen_sql_Col_ColumnFull = Generalization(general=ColumnFull, specific=sql_Col)
gen_sql_abc_FromValuesColumnNames = Generalization(general=FromValuesColumnNames, specific=sql_abc)
gen_sql_UnipivotInClause_UnpivotInClause = Generalization(general=UnpivotInClause, specific=sql_UnipivotInClause)
gen_sql_uicargs_UnpivotInClauseArgs = Generalization(general=UnpivotInClauseArgs, specific=sql_uicargs)
gen_sql_Minus_Operands = Generalization(general=Operands, specific=sql_Minus)
gen_sql_Concat_Operands = Generalization(general=Operands, specific=sql_Concat)
gen_sql_Multiply_Operands = Generalization(general=Operands, specific=sql_Multiply)
gen_sql_Division_Operands = Generalization(general=Operands, specific=sql_Division)
gen_sql_OBCArgs_OrderByClauseArgs = Generalization(general=OrderByClauseArgs, specific=sql_OBCArgs)
gen_sql_AExpArgs_AnalyticExprArgs = Generalization(general=AnalyticExprArgs, specific=sql_AExpArgs)
gen_sql_OpFList_OpFunctionArg = Generalization(general=OpFunctionArg, specific=sql_OpFList)
gen_sql_WhenList_SQLCaseWhens = Generalization(general=SQLCaseWhens, specific=sql_WhenList)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Model, sql_SelectQuery, sql_FetchFirst, sql_UnsignedValue, sql_Offset, sql_OrExpr, sql_OrGroupByColumn, sql_OrOrderByColumn, sql_Limit, sql_SelectSubSet, sql_Select, SelectQuery, sql_OrColumn, sql_OrTable, OrTable, sql_TableOrAlias, sql_FromTableJoin, sql_JoinCondition, sql_UsingCols, PivotForClause, sql_ColumnOrAlias, OrColumn, sql_Operands, sql_DbObjectName, sql_DbObjectNameAll, sql_ColumnFull, sql_FromTable, sql_Values, sql_FromValuesColumns, sql_FromValuesColumnNames, sql_ColumnNames, FromValuesColumnNames, sql_Rows, sql_Row, sql_TableFull, sql_SubQueryOperand, sql_FromValues, sql_PivotTable, sql_UnpivotTable, sql_PivotFunction, sql_UnpivotInClauseArgs, sql_PivotColumns, sql_UnpivotInClause, sql_UnpivotInClauseArg, UnpivotInClauseArgs, Rows, sql_RowValues, sql_RowValue, RowValues, sql_PivotFunctions, sql_PivotForClause, sql_PivotInClause, OrOrderByColumn, sql_GroupByColumnFull, OrGroupByColumn, sql_OpFunction, sql_Pivots, PivotColumns, sql_PivotCol, PivotFunction, Pivots, ColumnFull, UsingCols, PivotCol, TableFull, sql_OrderByColumnFull, sql_Between, sql_Like, sql_Comparison, sql_FullExpression, OrExpr, sql_ExprGroup, sql_XExpr, sql_InOper, sql_ExistsOper, sql_LikeOperand, sql_OpFunctionCast, sql_POperand, sql_Prms, sql_JRParameter, Prms, sql_ColumnOperand, sql_OperandListGroup, sql_OperandList, OpFunctionArgAgregate, sql_Operand, sql_ScalarOperand, sql_OpFunctionArg, sql_FunctionAnalytical, sql_FunctionExtract, sql_SQLCaseOperand, sql_ExpOperand, sql_OrderByClause, sql_WindowingClause, sql_WindowingClauseBetween, WindowingClause, sql_WindowingClauseOperandPreceding, sql_WindowingClauseOperandFollowing, sql_AnalyticExprArg, sql_AnalyticClause, sql_QueryPartitionClause, AnalyticExprArgs, sql_OpFunctionArgOperand, OpFunctionArg, sql_OpFunctionArgAgregate, sql_OrderByClauseArgs, sql_OrderByClauseArg, OrderByClauseArgs, sql_AnalyticExprArgs, QueryPartitionClause, RowValue, OperandList, sql_SQLCaseWhens, sql_SqlCaseWhen, SQLCaseWhens, sql_pvcs, sql_pcols, sql_tbls, sql_OpList, sql_Plus, Operands, sql_Minus, sql_IntegerValue, sql_Col, sql_abc, sql_UnipivotInClause, UnpivotInClause, sql_uicargs, sql_Concat, sql_Multiply, sql_Division, sql_OBCArgs, sql_AExpArgs, sql_OpFList, sql_WhenList, EXTRACT_VALUES, XFunction},
    associations={query0, fetchFirst1, whereExpression10, groupByEntry12, havingEntry14, orderByEntry17, lim19, offset21, query2, op3, cols6, tbl8, entries34, table36, fjoin38, onTable40, joinExpr43, joinCond46, fetchFirst23, entries26, ce28, colAlias30, dbAllCols32, values66, c68, fvCols70, rows72, useCols48, entries50, tfull53, sq55, values57, pivot59, unpivot61, tblAlias63, sq86, args89, pcols91, pfor93, inop96, entries74, rowValues76, entries78, pfun80, pfor82, pin84, entries103, colOrder105, entries107, colGrBy109, gbFunction112, pcols98, cfuls100, op1130, between133, like135, comp137, entries114, efrag117, expgroup119, exp122, xexp124, in126, exists128, op2152, fop2154, fcast157, fparam159, op2161, op3164, expr139, col142, prm145, entries147, op2149, op1180, left183, right185, column188, subquery167, opList170, subquery172, opList175, opGroup178, eparam209, scalar211, args213, fan215, operand217, xop191, subq193, fcast196, fext199, func201, sqlcase204, param206, obc224, winc226, wcoP228, wcoF229, anClause220, abc222, ce242, colAlias245, op248, op249, exp231, expr233, args236, col238, args240, eexp268, cfull252, sel255, expr258, when261, expr263, texp265, entries276, entries278, entries279, entries281, entries283, entries271, entries273, args274, entries285, entries287, entries289, entries291},
    generalizations={gen_sql_Select_SelectQuery, gen_sql_FromTable_OrTable, gen_sql_OrColumn_PivotForClause, gen_sql_ColumnOrAlias_OrColumn, gen_sql_ColumnFull_PivotForClause, gen_sql_ColumnNames_FromValuesColumnNames, gen_sql_UnpivotInClauseArg_UnpivotInClauseArgs, gen_sql_Row_Rows, gen_sql_RowValue_RowValues, gen_sql_OrderByColumnFull_OrOrderByColumn, gen_sql_GroupByColumnFull_OrGroupByColumn, gen_sql_Pivots_PivotColumns, gen_sql_PivotCol_PivotFunction, gen_sql_PivotCol_PivotColumns, gen_sql_PivotCol_Pivots, gen_sql_DbObjectName_ColumnFull, gen_sql_DbObjectName_UsingCols, gen_sql_DbObjectName_PivotCol, gen_sql_DbObjectName_TableFull, gen_sql_FullExpression_OrExpr, gen_sql_JRParameter_Prms, gen_sql_Operands_OpFunctionArgAgregate, gen_sql_WindowingClauseBetween_WindowingClause, gen_sql_AnalyticExprArg_AnalyticExprArgs, gen_sql_OpFunctionArgOperand_OpFunctionArg, gen_sql_WindowingClauseOperandPreceding_WindowingClause, gen_sql_OrderByClauseArg_OrderByClauseArgs, gen_sql_AnalyticExprArgs_QueryPartitionClause, gen_sql_ScalarOperand_RowValue, gen_sql_ScalarOperand_OperandList, gen_sql_SqlCaseWhen_SQLCaseWhens, gen_sql_pvcs_Pivots, gen_sql_pcols_PivotCol, gen_sql_tbls_TableFull, gen_sql_OpList_OperandList, gen_sql_Plus_Operands, gen_sql_Col_ColumnFull, gen_sql_abc_FromValuesColumnNames, gen_sql_UnipivotInClause_UnpivotInClause, gen_sql_uicargs_UnpivotInClauseArgs, gen_sql_Minus_Operands, gen_sql_Concat_Operands, gen_sql_Multiply_Operands, gen_sql_Division_Operands, gen_sql_OBCArgs_OrderByClauseArgs, gen_sql_AExpArgs_AnalyticExprArgs, gen_sql_OpFList_OpFunctionArg, gen_sql_WhenList_SQLCaseWhens},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
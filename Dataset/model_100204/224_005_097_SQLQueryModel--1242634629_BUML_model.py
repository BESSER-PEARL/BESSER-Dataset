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
SuperGroupType: Enumeration = Enumeration(
    name="SuperGroupType",
    literals={
            EnumerationLiteral(name="CUBE"),
			EnumerationLiteral(name="GRANDTOTAL"),
			EnumerationLiteral(name="ROLLUP")
    }
)

SearchConditionCombinedOperator: Enumeration = Enumeration(
    name="SearchConditionCombinedOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

TableJoinedOperator: Enumeration = Enumeration(
    name="TableJoinedOperator",
    literals={
            EnumerationLiteral(name="DEFAULT_INNER"),
			EnumerationLiteral(name="EXPLICIT_INNER"),
			EnumerationLiteral(name="LEFT_OUTER"),
			EnumerationLiteral(name="RIGHT_OUTER"),
			EnumerationLiteral(name="FULL_OUTER")
    }
)

QueryCombinedOperator: Enumeration = Enumeration(
    name="QueryCombinedOperator",
    literals={
            EnumerationLiteral(name="UNION"),
			EnumerationLiteral(name="UNION_ALL"),
			EnumerationLiteral(name="INTERSECT"),
			EnumerationLiteral(name="INTERSECT_ALL"),
			EnumerationLiteral(name="EXCEPT"),
			EnumerationLiteral(name="EXCEPT_ALL")
    }
)

ValueExpressionUnaryOperator: Enumeration = Enumeration(
    name="ValueExpressionUnaryOperator",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

PredicateQuantifiedType: Enumeration = Enumeration(
    name="PredicateQuantifiedType",
    literals={
            EnumerationLiteral(name="SOME"),
			EnumerationLiteral(name="ANY"),
			EnumerationLiteral(name="ALL")
    }
)

PredicateComparisonOperator: Enumeration = Enumeration(
    name="PredicateComparisonOperator",
    literals={
            EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="LESS_THAN_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_THAN_OR_EQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="NOT_EQUAL"),
			EnumerationLiteral(name="LESS_THAN")
    }
)

ValueExpressionCombinedOperator: Enumeration = Enumeration(
    name="ValueExpressionCombinedOperator",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBTRACT"),
			EnumerationLiteral(name="MULTIPLY"),
			EnumerationLiteral(name="DIVIDE"),
			EnumerationLiteral(name="CONCATENATE")
    }
)

ValueExpressionLabeledDurationType: Enumeration = Enumeration(
    name="ValueExpressionLabeledDurationType",
    literals={
            EnumerationLiteral(name="YEARS"),
			EnumerationLiteral(name="MONTHS"),
			EnumerationLiteral(name="DAYS"),
			EnumerationLiteral(name="HOURS"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MICROSECONDS")
    }
)

NullOrderingType: Enumeration = Enumeration(
    name="NullOrderingType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="NULLS_FIRST"),
			EnumerationLiteral(name="NULLS_LAST")
    }
)

OrderingSpecType: Enumeration = Enumeration(
    name="OrderingSpecType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="ASC"),
			EnumerationLiteral(name="DESC")
    }
)

UpdatabilityType: Enumeration = Enumeration(
    name="UpdatabilityType",
    literals={
            EnumerationLiteral(name="READ_ONLY"),
			EnumerationLiteral(name="UPDATE")
    }
)

# Classes
query_QueryDeleteStatement = Class(name="query_QueryDeleteStatement")
QueryChangeStatement = Class(name="QueryChangeStatement")
query_QueryStatement = Class(name="query_QueryStatement", is_abstract=True)
SQLQueryObject = Class(name="SQLQueryObject")
statements_SQLDataStatement = Class(name="statements_SQLDataStatement")
query_CursorReference = Class(name="query_CursorReference")
query_QuerySearchCondition = Class(name="query_QuerySearchCondition", is_abstract=True)
query_TableInDatabase = Class(name="query_TableInDatabase")
query_QueryInsertStatement = Class(name="query_QueryInsertStatement")
query_QueryExpressionRoot = Class(name="query_QueryExpressionRoot")
query_ValuesRow = Class(name="query_ValuesRow")
query_ValueExpressionColumn = Class(name="query_ValueExpressionColumn")
query_QuerySelectStatement = Class(name="query_QuerySelectStatement")
QueryStatement = Class(name="QueryStatement")
query_OrderBySpecification = Class(name="query_OrderBySpecification", is_abstract=True)
query_UpdatabilityExpression = Class(name="query_UpdatabilityExpression")
query_QueryUpdateStatement = Class(name="query_QueryUpdateStatement")
query_UpdateAssignmentExpression = Class(name="query_UpdateAssignmentExpression")
query_UpdateSource = Class(name="query_UpdateSource")
query_MergeUpdateSpecification = Class(name="query_MergeUpdateSpecification")
expressions_SearchCondition = Class(name="expressions_SearchCondition")
query_TableJoined = Class(name="query_TableJoined")
query_SearchConditionCombined = Class(name="query_SearchConditionCombined")
query_QueryCombined = Class(name="query_QueryCombined")
query_QuerySelect = Class(name="query_QuerySelect")
query_ValueExpressionCaseSearchContent = Class(name="query_ValueExpressionCaseSearchContent")
query_SearchConditionNested = Class(name="query_SearchConditionNested")
query_MergeOnCondition = Class(name="query_MergeOnCondition")
query_QueryExpressionBody = Class(name="query_QueryExpressionBody", is_abstract=True)
TableExpression = Class(name="TableExpression")
expressions_ValueExpression = Class(name="expressions_ValueExpression")
DataType = Class(name="DataType")
query_PredicateExists = Class(name="query_PredicateExists")
query_UpdateSourceQuery = Class(name="query_UpdateSourceQuery")
query_WithTableSpecification = Class(name="query_WithTableSpecification")
query_QueryNested = Class(name="query_QueryNested")
query_QueryValueExpression = Class(name="query_QueryValueExpression", is_abstract=True)
query_PredicateIsNull = Class(name="query_PredicateIsNull")
query_OrderByValueExpression = Class(name="query_OrderByValueExpression")
query_ResultColumn = Class(name="query_ResultColumn")
query_PredicateBasic = Class(name="query_PredicateBasic")
query_PredicateLike = Class(name="query_PredicateLike")
query_PredicateBetween = Class(name="query_PredicateBetween")
query_PredicateInValueList = Class(name="query_PredicateInValueList")
query_PredicateInValueRowSelect = Class(name="query_PredicateInValueRowSelect")
query_PredicateInValueSelect = Class(name="query_PredicateInValueSelect")
query_PredicateQuantifiedRowSelect = Class(name="query_PredicateQuantifiedRowSelect")
query_PredicateQuantifiedValueSelect = Class(name="query_PredicateQuantifiedValueSelect")
query_GroupingExpression = Class(name="query_GroupingExpression")
query_ValueExpressionCaseElse = Class(name="query_ValueExpressionCaseElse")
query_ValueExpressionCast = Class(name="query_ValueExpressionCast")
query_ValueExpressionFunction = Class(name="query_ValueExpressionFunction")
query_ValueExpressionCombined = Class(name="query_ValueExpressionCombined")
query_ValueExpressionLabeledDuration = Class(name="query_ValueExpressionLabeledDuration")
query_ValueExpressionNested = Class(name="query_ValueExpressionNested")
query_ValueExpressionCaseSimple = Class(name="query_ValueExpressionCaseSimple")
query_ValueExpressionCaseSimpleContent = Class(name="query_ValueExpressionCaseSimpleContent")
expressions_QueryExpression = Class(name="expressions_QueryExpression")
query_UpdateSourceExprList = Class(name="query_UpdateSourceExprList")
query_TableFunction = Class(name="query_TableFunction")
query_ValueExpressionRow = Class(name="query_ValueExpressionRow")
query_CallStatement = Class(name="query_CallStatement")
query_ValueExpressionScalarSelect = Class(name="query_ValueExpressionScalarSelect")
query_QueryValues = Class(name="query_QueryValues")
QueryExpressionBody = Class(name="QueryExpressionBody")
query_TableReference = Class(name="query_TableReference", is_abstract=True)
query_TableNested = Class(name="query_TableNested")
query_MergeSourceTable = Class(name="query_MergeSourceTable")
query_TableExpression = Class(name="query_TableExpression", is_abstract=True)
TableReference = Class(name="TableReference")
query_TableCorrelation = Class(name="query_TableCorrelation")
query_ResultTableAllColumns = Class(name="query_ResultTableAllColumns")
query_MergeTargetTable = Class(name="query_MergeTargetTable")
query_WithTableReference = Class(name="query_WithTableReference")
query_ColumnName = Class(name="query_ColumnName")
query_Predicate = Class(name="query_Predicate", is_abstract=True)
QuerySearchCondition = Class(name="QuerySearchCondition")
OrderBySpecification = Class(name="OrderBySpecification")
query_GroupingSpecification = Class(name="query_GroupingSpecification", is_abstract=True)
query_QueryResultSpecification = Class(name="query_QueryResultSpecification", is_abstract=True)
query_ValueExpressionVariable = Class(name="query_ValueExpressionVariable")
QueryResultSpecification = Class(name="QueryResultSpecification")
query_OrderByResultColumn = Class(name="query_OrderByResultColumn")
Predicate = Class(name="Predicate")
query_PredicateQuantified = Class(name="query_PredicateQuantified", is_abstract=True)
query_PredicateIn = Class(name="query_PredicateIn", is_abstract=True)
PredicateIn = Class(name="PredicateIn")
PredicateQuantified = Class(name="PredicateQuantified")
query_ValueExpressionSimple = Class(name="query_ValueExpressionSimple")
ValueExpressionAtomic = Class(name="ValueExpressionAtomic")
query_MergeInsertSpecification = Class(name="query_MergeInsertSpecification")
query_ValueExpressionCase = Class(name="query_ValueExpressionCase", is_abstract=True)
query_ValueExpressionNullValue = Class(name="query_ValueExpressionNullValue")
query_ValueExpressionDefaultValue = Class(name="query_ValueExpressionDefaultValue")
Function = Class(name="Function")
QueryValueExpression = Class(name="QueryValueExpression")
query_GroupingSets = Class(name="query_GroupingSets")
GroupingSpecification = Class(name="GroupingSpecification")
query_GroupingSetsElement = Class(name="query_GroupingSetsElement", is_abstract=True)
query_Grouping = Class(name="query_Grouping", is_abstract=True)
query_GroupingSetsElementExpression = Class(name="query_GroupingSetsElementExpression")
query_GroupingSetsElementSublist = Class(name="query_GroupingSetsElementSublist")
GroupingSetsElement = Class(name="GroupingSetsElement")
query_SuperGroupElementSublist = Class(name="query_SuperGroupElementSublist")
SuperGroupElement = Class(name="SuperGroupElement")
query_SuperGroup = Class(name="query_SuperGroup")
Grouping = Class(name="Grouping")
query_SuperGroupElement = Class(name="query_SuperGroupElement", is_abstract=True)
query_SuperGroupElementExpression = Class(name="query_SuperGroupElementExpression")
query_ValueExpressionCaseSearch = Class(name="query_ValueExpressionCaseSearch")
ValueExpressionCase = Class(name="ValueExpressionCase")
Table = Class(name="Table")
query_SQLQueryObject = Class(name="query_SQLQueryObject", is_abstract=True)
SQLObject = Class(name="SQLObject")
query_QueryMergeStatement = Class(name="query_QueryMergeStatement")
query_QueryChangeStatement = Class(name="query_QueryChangeStatement", is_abstract=True)
statements_SQLDataChangeStatement = Class(name="statements_SQLDataChangeStatement")
query_MergeOperationSpecification = Class(name="query_MergeOperationSpecification")
query_OrderByOrdinal = Class(name="query_OrderByOrdinal")
query_ValueExpressionAtomic = Class(name="query_ValueExpressionAtomic", is_abstract=True)
UpdateSource = Class(name="UpdateSource")
MergeOperationSpecification = Class(name="MergeOperationSpecification")
query_UpdateOfColumn = Class(name="query_UpdateOfColumn")
Procedure = Class(name="Procedure")
statements_SQLControlStatement = Class(name="statements_SQLControlStatement")
query_ProcedureReference = Class(name="query_ProcedureReference")
query_TableQueryLateral = Class(name="query_TableQueryLateral")

# query_QueryDeleteStatement class attributes and methods

# QueryChangeStatement class attributes and methods

# query_QueryStatement class attributes and methods

# SQLQueryObject class attributes and methods

# statements_SQLDataStatement class attributes and methods

# query_CursorReference class attributes and methods

# query_QuerySearchCondition class attributes and methods
query_QuerySearchCondition_negatedCondition: Property = Property(name="negatedCondition", type=BooleanType)
query_QuerySearchCondition.attributes={query_QuerySearchCondition_negatedCondition}

# query_TableInDatabase class attributes and methods

# query_QueryInsertStatement class attributes and methods

# query_QueryExpressionRoot class attributes and methods

# query_ValuesRow class attributes and methods

# query_ValueExpressionColumn class attributes and methods

# query_QuerySelectStatement class attributes and methods

# QueryStatement class attributes and methods

# query_OrderBySpecification class attributes and methods
query_OrderBySpecification_OrderingSpecOption: Property = Property(name="OrderingSpecOption", type=StringType)
query_OrderBySpecification_NullOrderingOption: Property = Property(name="NullOrderingOption", type=StringType)
query_OrderBySpecification_descending: Property = Property(name="descending", type=BooleanType)
query_OrderBySpecification.attributes={query_OrderBySpecification_descending, query_OrderBySpecification_OrderingSpecOption, query_OrderBySpecification_NullOrderingOption}

# query_UpdatabilityExpression class attributes and methods
query_UpdatabilityExpression_updatabilityType: Property = Property(name="updatabilityType", type=StringType)
query_UpdatabilityExpression.attributes={query_UpdatabilityExpression_updatabilityType}

# query_QueryUpdateStatement class attributes and methods

# query_UpdateAssignmentExpression class attributes and methods

# query_UpdateSource class attributes and methods

# query_MergeUpdateSpecification class attributes and methods

# expressions_SearchCondition class attributes and methods

# query_TableJoined class attributes and methods
query_TableJoined_joinOperator: Property = Property(name="joinOperator", type=StringType)
query_TableJoined.attributes={query_TableJoined_joinOperator}

# query_SearchConditionCombined class attributes and methods
query_SearchConditionCombined_combinedOperator: Property = Property(name="combinedOperator", type=StringType)
query_SearchConditionCombined.attributes={query_SearchConditionCombined_combinedOperator}

# query_QueryCombined class attributes and methods
query_QueryCombined_combinedOperator: Property = Property(name="combinedOperator", type=StringType)
query_QueryCombined.attributes={query_QueryCombined_combinedOperator}

# query_QuerySelect class attributes and methods
query_QuerySelect_distinct: Property = Property(name="distinct", type=BooleanType)
query_QuerySelect.attributes={query_QuerySelect_distinct}

# query_ValueExpressionCaseSearchContent class attributes and methods

# query_SearchConditionNested class attributes and methods

# query_MergeOnCondition class attributes and methods

# query_QueryExpressionBody class attributes and methods
query_QueryExpressionBody_rowFetchLimit: Property = Property(name="rowFetchLimit", type=IntegerType)
query_QueryExpressionBody.attributes={query_QueryExpressionBody_rowFetchLimit}

# TableExpression class attributes and methods

# expressions_ValueExpression class attributes and methods

# DataType class attributes and methods

# query_PredicateExists class attributes and methods

# query_UpdateSourceQuery class attributes and methods

# query_WithTableSpecification class attributes and methods

# query_QueryNested class attributes and methods

# query_QueryValueExpression class attributes and methods
query_QueryValueExpression_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
query_QueryValueExpression.attributes={query_QueryValueExpression_unaryOperator}

# query_PredicateIsNull class attributes and methods
query_PredicateIsNull_notNull: Property = Property(name="notNull", type=BooleanType)
query_PredicateIsNull.attributes={query_PredicateIsNull_notNull}

# query_OrderByValueExpression class attributes and methods

# query_ResultColumn class attributes and methods

# query_PredicateBasic class attributes and methods
query_PredicateBasic_comparisonOperator: Property = Property(name="comparisonOperator", type=StringType)
query_PredicateBasic.attributes={query_PredicateBasic_comparisonOperator}

# query_PredicateLike class attributes and methods
query_PredicateLike_notLike: Property = Property(name="notLike", type=BooleanType)
query_PredicateLike.attributes={query_PredicateLike_notLike}

# query_PredicateBetween class attributes and methods
query_PredicateBetween_notBetween: Property = Property(name="notBetween", type=BooleanType)
query_PredicateBetween.attributes={query_PredicateBetween_notBetween}

# query_PredicateInValueList class attributes and methods

# query_PredicateInValueRowSelect class attributes and methods

# query_PredicateInValueSelect class attributes and methods

# query_PredicateQuantifiedRowSelect class attributes and methods
query_PredicateQuantifiedRowSelect_quantifiedType: Property = Property(name="quantifiedType", type=StringType)
query_PredicateQuantifiedRowSelect.attributes={query_PredicateQuantifiedRowSelect_quantifiedType}

# query_PredicateQuantifiedValueSelect class attributes and methods
query_PredicateQuantifiedValueSelect_quantifiedType: Property = Property(name="quantifiedType", type=StringType)
query_PredicateQuantifiedValueSelect_comparisonOperator: Property = Property(name="comparisonOperator", type=StringType)
query_PredicateQuantifiedValueSelect.attributes={query_PredicateQuantifiedValueSelect_comparisonOperator, query_PredicateQuantifiedValueSelect_quantifiedType}

# query_GroupingExpression class attributes and methods

# query_ValueExpressionCaseElse class attributes and methods

# query_ValueExpressionCast class attributes and methods

# query_ValueExpressionFunction class attributes and methods
query_ValueExpressionFunction_specialRegister: Property = Property(name="specialRegister", type=BooleanType)
query_ValueExpressionFunction_distinct: Property = Property(name="distinct", type=BooleanType)
query_ValueExpressionFunction_columnFunction: Property = Property(name="columnFunction", type=BooleanType)
query_ValueExpressionFunction.attributes={query_ValueExpressionFunction_distinct, query_ValueExpressionFunction_columnFunction, query_ValueExpressionFunction_specialRegister}

# query_ValueExpressionCombined class attributes and methods
query_ValueExpressionCombined_combinedOperator: Property = Property(name="combinedOperator", type=StringType)
query_ValueExpressionCombined.attributes={query_ValueExpressionCombined_combinedOperator}

# query_ValueExpressionLabeledDuration class attributes and methods
query_ValueExpressionLabeledDuration_labeledDurationType: Property = Property(name="labeledDurationType", type=StringType)
query_ValueExpressionLabeledDuration.attributes={query_ValueExpressionLabeledDuration_labeledDurationType}

# query_ValueExpressionNested class attributes and methods

# query_ValueExpressionCaseSimple class attributes and methods

# query_ValueExpressionCaseSimpleContent class attributes and methods

# expressions_QueryExpression class attributes and methods

# query_UpdateSourceExprList class attributes and methods

# query_TableFunction class attributes and methods

# query_ValueExpressionRow class attributes and methods

# query_CallStatement class attributes and methods

# query_ValueExpressionScalarSelect class attributes and methods

# query_QueryValues class attributes and methods

# QueryExpressionBody class attributes and methods

# query_TableReference class attributes and methods

# query_TableNested class attributes and methods

# query_MergeSourceTable class attributes and methods

# query_TableExpression class attributes and methods

# TableReference class attributes and methods

# query_TableCorrelation class attributes and methods

# query_ResultTableAllColumns class attributes and methods

# query_MergeTargetTable class attributes and methods

# query_WithTableReference class attributes and methods

# query_ColumnName class attributes and methods

# query_Predicate class attributes and methods
query_Predicate_negatedPredicate: Property = Property(name="negatedPredicate", type=BooleanType)
query_Predicate_hasSelectivity: Property = Property(name="hasSelectivity", type=BooleanType)
query_Predicate_selectivityValue: Property = Property(name="selectivityValue", type=StringType)
query_Predicate.attributes={query_Predicate_selectivityValue, query_Predicate_hasSelectivity, query_Predicate_negatedPredicate}

# QuerySearchCondition class attributes and methods

# OrderBySpecification class attributes and methods

# query_GroupingSpecification class attributes and methods

# query_QueryResultSpecification class attributes and methods

# query_ValueExpressionVariable class attributes and methods

# QueryResultSpecification class attributes and methods

# query_OrderByResultColumn class attributes and methods

# Predicate class attributes and methods

# query_PredicateQuantified class attributes and methods

# query_PredicateIn class attributes and methods
query_PredicateIn_notIn: Property = Property(name="notIn", type=BooleanType)
query_PredicateIn.attributes={query_PredicateIn_notIn}

# PredicateIn class attributes and methods

# PredicateQuantified class attributes and methods

# query_ValueExpressionSimple class attributes and methods
query_ValueExpressionSimple_value: Property = Property(name="value", type=StringType)
query_ValueExpressionSimple.attributes={query_ValueExpressionSimple_value}

# ValueExpressionAtomic class attributes and methods

# query_MergeInsertSpecification class attributes and methods

# query_ValueExpressionCase class attributes and methods

# query_ValueExpressionNullValue class attributes and methods

# query_ValueExpressionDefaultValue class attributes and methods

# Function class attributes and methods

# QueryValueExpression class attributes and methods

# query_GroupingSets class attributes and methods

# GroupingSpecification class attributes and methods

# query_GroupingSetsElement class attributes and methods

# query_Grouping class attributes and methods

# query_GroupingSetsElementExpression class attributes and methods

# query_GroupingSetsElementSublist class attributes and methods

# GroupingSetsElement class attributes and methods

# query_SuperGroupElementSublist class attributes and methods

# SuperGroupElement class attributes and methods

# query_SuperGroup class attributes and methods
query_SuperGroup_superGroupType: Property = Property(name="superGroupType", type=StringType)
query_SuperGroup.attributes={query_SuperGroup_superGroupType}

# Grouping class attributes and methods

# query_SuperGroupElement class attributes and methods

# query_SuperGroupElementExpression class attributes and methods

# query_ValueExpressionCaseSearch class attributes and methods

# ValueExpressionCase class attributes and methods

# Table class attributes and methods

# query_SQLQueryObject class attributes and methods
query_SQLQueryObject_m_getSQL: Method = Method(name="getSQL", parameters={}, type=StringType)
query_SQLQueryObject_m_setSQL: Method = Method(name="setSQL", parameters={Parameter(name='query_sqlText', type=StringType)})
query_SQLQueryObject.methods={query_SQLQueryObject_m_getSQL, query_SQLQueryObject_m_setSQL}

# SQLObject class attributes and methods

# query_QueryMergeStatement class attributes and methods

# query_QueryChangeStatement class attributes and methods

# statements_SQLDataChangeStatement class attributes and methods

# query_MergeOperationSpecification class attributes and methods

# query_OrderByOrdinal class attributes and methods
query_OrderByOrdinal_ordinalValue: Property = Property(name="ordinalValue", type=IntegerType)
query_OrderByOrdinal.attributes={query_OrderByOrdinal_ordinalValue}

# query_ValueExpressionAtomic class attributes and methods

# UpdateSource class attributes and methods

# MergeOperationSpecification class attributes and methods

# query_UpdateOfColumn class attributes and methods

# Procedure class attributes and methods

# statements_SQLControlStatement class attributes and methods

# query_ProcedureReference class attributes and methods

# query_TableQueryLateral class attributes and methods

# Relationships
sourceValuesRowList6: BinaryAssociation = BinaryAssociation(
    name="sourceValuesRowList6",
    ends={
        Property(name="ValuesRow", type=query_QueryInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="insertStatement7", type=query_ValuesRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereCurrentOfClause0: BinaryAssociation = BinaryAssociation(
    name="whereCurrentOfClause0",
    ends={
        Property(name="CursorReference", type=query_QueryDeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="deleteStatement", type=query_CursorReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause1: BinaryAssociation = BinaryAssociation(
    name="whereClause1",
    ends={
        Property(name="QuerySearchCondition", type=query_QueryDeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="deleteStatement2", type=query_QuerySearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetTable3: BinaryAssociation = BinaryAssociation(
    name="targetTable3",
    ends={
        Property(name="TableInDatabase", type=query_QueryDeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="deleteStatement4", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceQuery5: BinaryAssociation = BinaryAssociation(
    name="sourceQuery5",
    ends={
        Property(name="QueryExpressionRoot", type=query_QueryInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="insertStatement", type=query_QueryExpressionRoot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignmentClause19: BinaryAssociation = BinaryAssociation(
    name="assignmentClause19",
    ends={
        Property(name="updateStatement", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="UpdateAssignmentExpression", type=query_QueryUpdateStatement, multiplicity=Multiplicity(1, 1))
    }
)
whereCurrentOfClause20: BinaryAssociation = BinaryAssociation(
    name="whereCurrentOfClause20",
    ends={
        Property(name="CursorReference22", type=query_QueryUpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="updateStatement21", type=query_CursorReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetTable8: BinaryAssociation = BinaryAssociation(
    name="targetTable8",
    ends={
        Property(name="TableInDatabase10", type=query_QueryInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="insertStatement9", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetColumnList11: BinaryAssociation = BinaryAssociation(
    name="targetColumnList11",
    ends={
        Property(name="ValueExpressionColumn", type=query_QueryInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="insertStatement12", type=query_ValueExpressionColumn, multiplicity=Multiplicity(0, 9999))
    }
)
queryExpr13: BinaryAssociation = BinaryAssociation(
    name="queryExpr13",
    ends={
        Property(name="QueryExpressionRoot14", type=query_QuerySelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="selectStatement", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
orderByClause15: BinaryAssociation = BinaryAssociation(
    name="orderByClause15",
    ends={
        Property(name="OrderBySpecification", type=query_QuerySelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="selectStatement16", type=query_OrderBySpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updatabilityExpr17: BinaryAssociation = BinaryAssociation(
    name="updatabilityExpr17",
    ends={
        Property(name="UpdatabilityExpression", type=query_QuerySelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="selectStatement18", type=query_UpdatabilityExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateStatement34: BinaryAssociation = BinaryAssociation(
    name="updateStatement34",
    ends={
        Property(name="QueryUpdateStatement35", type=query_CursorReference, multiplicity=Multiplicity(1, 1)),
        Property(name="whereCurrentOfClause", type=query_QueryUpdateStatement, multiplicity=Multiplicity(0, 1))
    }
)
whereClause23: BinaryAssociation = BinaryAssociation(
    name="whereClause23",
    ends={
        Property(name="QuerySearchCondition25", type=query_QueryUpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="updateStatement24", type=query_QuerySearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetTable26: BinaryAssociation = BinaryAssociation(
    name="targetTable26",
    ends={
        Property(name="TableInDatabase28", type=query_QueryUpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="updateStatement27", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updateStatement29: BinaryAssociation = BinaryAssociation(
    name="updateStatement29",
    ends={
        Property(name="QueryUpdateStatement", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="assignmentClause", type=query_QueryUpdateStatement, multiplicity=Multiplicity(0, 1))
    }
)
targetColumnList30: BinaryAssociation = BinaryAssociation(
    name="targetColumnList30",
    ends={
        Property(name="ValueExpressionColumn31", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="assignmentExprTarget", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 9999))
    }
)
updateSource32: BinaryAssociation = BinaryAssociation(
    name="updateSource32",
    ends={
        Property(name="UpdateSource", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="updateAssignmentExpr", type=query_UpdateSource, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mergeUpdateSpec33: BinaryAssociation = BinaryAssociation(
    name="mergeUpdateSpec33",
    ends={
        Property(name="MergeUpdateSpecification", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="assignementExprList", type=query_MergeUpdateSpecification, multiplicity=Multiplicity(0, 1))
    }
)
combinedRight45: BinaryAssociation = BinaryAssociation(
    name="combinedRight45",
    ends={
        Property(name="SearchConditionCombined46", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="rightCondition", type=query_SearchConditionCombined, multiplicity=Multiplicity(0, 1))
    }
)
deleteStatement36: BinaryAssociation = BinaryAssociation(
    name="deleteStatement36",
    ends={
        Property(name="QueryDeleteStatement", type=query_CursorReference, multiplicity=Multiplicity(1, 1)),
        Property(name="whereCurrentOfClause37", type=query_QueryDeleteStatement, multiplicity=Multiplicity(0, 1))
    }
)
updateStatement38: BinaryAssociation = BinaryAssociation(
    name="updateStatement38",
    ends={
        Property(name="QueryUpdateStatement39", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="whereClause", type=query_QueryUpdateStatement, multiplicity=Multiplicity(0, 1))
    }
)
deleteStatement40: BinaryAssociation = BinaryAssociation(
    name="deleteStatement40",
    ends={
        Property(name="QueryDeleteStatement42", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="whereClause41", type=query_QueryDeleteStatement, multiplicity=Multiplicity(0, 1))
    }
)
tableJoined43: BinaryAssociation = BinaryAssociation(
    name="tableJoined43",
    ends={
        Property(name="TableJoined", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="joinCondition", type=query_TableJoined, multiplicity=Multiplicity(0, 1))
    }
)
combinedLeft44: BinaryAssociation = BinaryAssociation(
    name="combinedLeft44",
    ends={
        Property(name="SearchConditionCombined", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="leftCondition", type=query_SearchConditionCombined, multiplicity=Multiplicity(0, 1))
    }
)
queryExpression55: BinaryAssociation = BinaryAssociation(
    name="queryExpression55",
    ends={
        Property(name="QueryExpressionRoot56", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=query_QueryExpressionRoot, multiplicity=Multiplicity(0, 1))
    }
)
querySelectHaving47: BinaryAssociation = BinaryAssociation(
    name="querySelectHaving47",
    ends={
        Property(name="QuerySelect", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="havingClause", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
querySelectWhere48: BinaryAssociation = BinaryAssociation(
    name="querySelectWhere48",
    ends={
        Property(name="QuerySelect50", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="whereClause49", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseSearchContent51: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSearchContent51",
    ends={
        Property(name="ValueExpressionCaseSearchContent", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="searchCondition", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(0, 1))
    }
)
nest52: BinaryAssociation = BinaryAssociation(
    name="nest52",
    ends={
        Property(name="SearchConditionNested", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedCondition", type=query_SearchConditionNested, multiplicity=Multiplicity(0, 1))
    }
)
mergeOnCondition53: BinaryAssociation = BinaryAssociation(
    name="mergeOnCondition53",
    ends={
        Property(name="MergeOnCondition", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="searchCondition54", type=query_MergeOnCondition, multiplicity=Multiplicity(0, 1))
    }
)
combinedLeft57: BinaryAssociation = BinaryAssociation(
    name="combinedLeft57",
    ends={
        Property(name="QueryCombined", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="leftQuery", type=query_QueryCombined, multiplicity=Multiplicity(0, 1))
    }
)
combinedRight58: BinaryAssociation = BinaryAssociation(
    name="combinedRight58",
    ends={
        Property(name="QueryCombined59", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="rightQuery", type=query_QueryCombined, multiplicity=Multiplicity(0, 1))
    }
)
predicateExists60: BinaryAssociation = BinaryAssociation(
    name="predicateExists60",
    ends={
        Property(name="PredicateExists", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr", type=query_PredicateExists, multiplicity=Multiplicity(0, 1))
    }
)
updateSourceQuery61: BinaryAssociation = BinaryAssociation(
    name="updateSourceQuery61",
    ends={
        Property(name="UpdateSourceQuery", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr62", type=query_UpdateSourceQuery, multiplicity=Multiplicity(1, 1))
    }
)
withTableSpecification63: BinaryAssociation = BinaryAssociation(
    name="withTableSpecification63",
    ends={
        Property(name="WithTableSpecification", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="withTableQueryExpr", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1))
    }
)
queryNest64: BinaryAssociation = BinaryAssociation(
    name="queryNest64",
    ends={
        Property(name="QueryNested", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedQuery", type=query_QueryNested, multiplicity=Multiplicity(0, 1))
    }
)
sortSpecList65: BinaryAssociation = BinaryAssociation(
    name="sortSpecList65",
    ends={
        Property(name="OrderBySpecification67", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="query66", type=query_OrderBySpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
likeMatching78: BinaryAssociation = BinaryAssociation(
    name="likeMatching78",
    ends={
        Property(name="PredicateLike79", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="matchingValueExpr", type=query_PredicateLike, multiplicity=Multiplicity(0, 1))
    }
)
dataType68: BinaryAssociation = BinaryAssociation(
    name="dataType68",
    ends={
        Property(name="DataType", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="query_QueryValueExpression", type=DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valuesRow69: BinaryAssociation = BinaryAssociation(
    name="valuesRow69",
    ends={
        Property(name="ValuesRow70", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="exprList", type=query_ValuesRow, multiplicity=Multiplicity(0, 1))
    }
)
orderByValueExpr71: BinaryAssociation = BinaryAssociation(
    name="orderByValueExpr71",
    ends={
        Property(name="OrderByValueExpression", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr", type=query_OrderByValueExpression, multiplicity=Multiplicity(0, 1))
    }
)
resultColumn72: BinaryAssociation = BinaryAssociation(
    name="resultColumn72",
    ends={
        Property(name="ResultColumn", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr73", type=query_ResultColumn, multiplicity=Multiplicity(0, 1))
    }
)
basicRight74: BinaryAssociation = BinaryAssociation(
    name="basicRight74",
    ends={
        Property(name="PredicateBasic", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rightValueExpr", type=query_PredicateBasic, multiplicity=Multiplicity(0, 1))
    }
)
basicLeft75: BinaryAssociation = BinaryAssociation(
    name="basicLeft75",
    ends={
        Property(name="PredicateBasic76", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="leftValueExpr", type=query_PredicateBasic, multiplicity=Multiplicity(0, 1))
    }
)
likePattern77: BinaryAssociation = BinaryAssociation(
    name="likePattern77",
    ends={
        Property(name="PredicateLike", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="patternValueExpr", type=query_PredicateLike, multiplicity=Multiplicity(0, 1))
    }
)
betweenLeft94: BinaryAssociation = BinaryAssociation(
    name="betweenLeft94",
    ends={
        Property(name="PredicateBetween", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="leftValueExpr95", type=query_PredicateBetween, multiplicity=Multiplicity(0, 1))
    }
)
predicateNull80: BinaryAssociation = BinaryAssociation(
    name="predicateNull80",
    ends={
        Property(name="PredicateIsNull", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr81", type=query_PredicateIsNull, multiplicity=Multiplicity(0, 1))
    }
)
inValueListRight82: BinaryAssociation = BinaryAssociation(
    name="inValueListRight82",
    ends={
        Property(name="PredicateInValueList", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprList", type=query_PredicateInValueList, multiplicity=Multiplicity(0, 1))
    }
)
inValueListLeft83: BinaryAssociation = BinaryAssociation(
    name="inValueListLeft83",
    ends={
        Property(name="PredicateInValueList85", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr84", type=query_PredicateInValueList, multiplicity=Multiplicity(0, 1))
    }
)
inValueRowSelectLeft86: BinaryAssociation = BinaryAssociation(
    name="inValueRowSelectLeft86",
    ends={
        Property(name="PredicateInValueRowSelect", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprList87", type=query_PredicateInValueRowSelect, multiplicity=Multiplicity(0, 1))
    }
)
inValueSelectLeft88: BinaryAssociation = BinaryAssociation(
    name="inValueSelectLeft88",
    ends={
        Property(name="PredicateInValueSelect", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr89", type=query_PredicateInValueSelect, multiplicity=Multiplicity(0, 1))
    }
)
quantifiedRowSelectLeft90: BinaryAssociation = BinaryAssociation(
    name="quantifiedRowSelectLeft90",
    ends={
        Property(name="PredicateQuantifiedRowSelect", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprList91", type=query_PredicateQuantifiedRowSelect, multiplicity=Multiplicity(0, 1))
    }
)
quantifiedValueSelectLeft92: BinaryAssociation = BinaryAssociation(
    name="quantifiedValueSelectLeft92",
    ends={
        Property(name="PredicateQuantifiedValueSelect", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr93", type=query_PredicateQuantifiedValueSelect, multiplicity=Multiplicity(0, 1))
    }
)
groupingExpr108: BinaryAssociation = BinaryAssociation(
    name="groupingExpr108",
    ends={
        Property(name="GroupingExpression", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr109", type=query_GroupingExpression, multiplicity=Multiplicity(0, 1))
    }
)
betweenRight196: BinaryAssociation = BinaryAssociation(
    name="betweenRight196",
    ends={
        Property(name="PredicateBetween97", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rightValueExpr1", type=query_PredicateBetween, multiplicity=Multiplicity(0, 1))
    }
)
betweenRight298: BinaryAssociation = BinaryAssociation(
    name="betweenRight298",
    ends={
        Property(name="PredicateBetween99", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rightValueExpr2", type=query_PredicateBetween, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCast100: BinaryAssociation = BinaryAssociation(
    name="valueExprCast100",
    ends={
        Property(name="ValueExpressionCast", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr101", type=query_ValueExpressionCast, multiplicity=Multiplicity(0, 1))
    }
)
valueExprFunction102: BinaryAssociation = BinaryAssociation(
    name="valueExprFunction102",
    ends={
        Property(name="ValueExpressionFunction", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterList", type=query_ValueExpressionFunction, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCombinedLeft103: BinaryAssociation = BinaryAssociation(
    name="valueExprCombinedLeft103",
    ends={
        Property(name="ValueExpressionCombined", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="leftValueExpr104", type=query_ValueExpressionCombined, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCombinedRight105: BinaryAssociation = BinaryAssociation(
    name="valueExprCombinedRight105",
    ends={
        Property(name="ValueExpressionCombined107", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rightValueExpr106", type=query_ValueExpressionCombined, multiplicity=Multiplicity(0, 1))
    }
)
valueExprLabeledDuration122: BinaryAssociation = BinaryAssociation(
    name="valueExprLabeledDuration122",
    ends={
        Property(name="ValueExpressionLabeledDuration", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr123", type=query_ValueExpressionLabeledDuration, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseElse110: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseElse110",
    ends={
        Property(name="ValueExpressionCaseElse", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr111", type=query_ValueExpressionCaseElse, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseSimple112: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSimple112",
    ends={
        Property(name="ValueExpressionCaseSimple", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr113", type=query_ValueExpressionCaseSimple, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseSimpleContentWhen114: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSimpleContentWhen114",
    ends={
        Property(name="ValueExpressionCaseSimpleContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="whenValueExpr", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseSimpleContentResult115: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSimpleContentResult115",
    ends={
        Property(name="ValueExpressionCaseSimpleContent116", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="resultValueExpr", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCaseSearchContent117: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSearchContent117",
    ends={
        Property(name="ValueExpressionCaseSearchContent119", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExpr118", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(0, 1))
    }
)
likeEscape120: BinaryAssociation = BinaryAssociation(
    name="likeEscape120",
    ends={
        Property(name="PredicateLike121", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="escapeValueExpr", type=query_PredicateLike, multiplicity=Multiplicity(0, 1))
    }
)
insertStatement132: BinaryAssociation = BinaryAssociation(
    name="insertStatement132",
    ends={
        Property(name="QueryInsertStatement", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceQuery", type=query_QueryInsertStatement, multiplicity=Multiplicity(0, 1))
    }
)
nest124: BinaryAssociation = BinaryAssociation(
    name="nest124",
    ends={
        Property(name="ValueExpressionNested", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedValueExpr", type=query_ValueExpressionNested, multiplicity=Multiplicity(0, 1))
    }
)
updateSourceExprList125: BinaryAssociation = BinaryAssociation(
    name="updateSourceExprList125",
    ends={
        Property(name="UpdateSourceExprList", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprList126", type=query_UpdateSourceExprList, multiplicity=Multiplicity(0, 1))
    }
)
tableFunction127: BinaryAssociation = BinaryAssociation(
    name="tableFunction127",
    ends={
        Property(name="TableFunction", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterList128", type=query_TableFunction, multiplicity=Multiplicity(1, 1))
    }
)
valueExprRow129: BinaryAssociation = BinaryAssociation(
    name="valueExprRow129",
    ends={
        Property(name="ValueExpressionRow", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprList130", type=query_ValueExpressionRow, multiplicity=Multiplicity(1, 1))
    }
)
callStatement131: BinaryAssociation = BinaryAssociation(
    name="callStatement131",
    ends={
        Property(name="CallStatement", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="argumentList", type=query_CallStatement, multiplicity=Multiplicity(1, 1))
    }
)
valExprScalarSelect150: BinaryAssociation = BinaryAssociation(
    name="valExprScalarSelect150",
    ends={
        Property(name="ValueExpressionScalarSelect", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr151", type=query_ValueExpressionScalarSelect, multiplicity=Multiplicity(0, 1))
    }
)
selectStatement133: BinaryAssociation = BinaryAssociation(
    name="selectStatement133",
    ends={
        Property(name="QuerySelectStatement", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr134", type=query_QuerySelectStatement, multiplicity=Multiplicity(0, 1))
    }
)
withClause135: BinaryAssociation = BinaryAssociation(
    name="withClause135",
    ends={
        Property(name="WithTableSpecification136", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpressionRoot", type=query_WithTableSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query137: BinaryAssociation = BinaryAssociation(
    name="query137",
    ends={
        Property(name="QueryExpressionBody", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpression", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inValueRowSelectRight138: BinaryAssociation = BinaryAssociation(
    name="inValueRowSelectRight138",
    ends={
        Property(name="PredicateInValueRowSelect140", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr139", type=query_PredicateInValueRowSelect, multiplicity=Multiplicity(0, 1))
    }
)
inValueSelectRight141: BinaryAssociation = BinaryAssociation(
    name="inValueSelectRight141",
    ends={
        Property(name="PredicateInValueSelect143", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr142", type=query_PredicateInValueSelect, multiplicity=Multiplicity(0, 1))
    }
)
quantifiedRowSelectRight144: BinaryAssociation = BinaryAssociation(
    name="quantifiedRowSelectRight144",
    ends={
        Property(name="PredicateQuantifiedRowSelect146", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr145", type=query_PredicateQuantifiedRowSelect, multiplicity=Multiplicity(0, 1))
    }
)
quantifiedValueSelectRight147: BinaryAssociation = BinaryAssociation(
    name="quantifiedValueSelectRight147",
    ends={
        Property(name="PredicateQuantifiedValueSelect149", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="queryExpr148", type=query_PredicateQuantifiedValueSelect, multiplicity=Multiplicity(0, 1))
    }
)
tableJoinedRight158: BinaryAssociation = BinaryAssociation(
    name="tableJoinedRight158",
    ends={
        Property(name="TableJoined159", type=query_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="tableRefRight", type=query_TableJoined, multiplicity=Multiplicity(1, 1))
    }
)
insertStatement152: BinaryAssociation = BinaryAssociation(
    name="insertStatement152",
    ends={
        Property(name="QueryInsertStatement153", type=query_ValuesRow, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceValuesRowList", type=query_QueryInsertStatement, multiplicity=Multiplicity(0, 1))
    }
)
exprList154: BinaryAssociation = BinaryAssociation(
    name="exprList154",
    ends={
        Property(name="QueryValueExpression", type=query_ValuesRow, multiplicity=Multiplicity(1, 1)),
        Property(name="valuesRow", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
queryValues155: BinaryAssociation = BinaryAssociation(
    name="queryValues155",
    ends={
        Property(name="QueryValues", type=query_ValuesRow, multiplicity=Multiplicity(1, 1)),
        Property(name="valuesRowList", type=query_QueryValues, multiplicity=Multiplicity(1, 1))
    }
)
valuesRowList156: BinaryAssociation = BinaryAssociation(
    name="valuesRowList156",
    ends={
        Property(name="ValuesRow157", type=query_QueryValues, multiplicity=Multiplicity(1, 1)),
        Property(name="queryValues", type=query_ValuesRow, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExprColumns171: BinaryAssociation = BinaryAssociation(
    name="valueExprColumns171",
    ends={
        Property(name="ValueExpressionColumn173", type=query_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tableExpr172", type=query_ValueExpressionColumn, multiplicity=Multiplicity(0, 9999))
    }
)
tableJoinedLeft160: BinaryAssociation = BinaryAssociation(
    name="tableJoinedLeft160",
    ends={
        Property(name="TableJoined161", type=query_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="tableRefLeft", type=query_TableJoined, multiplicity=Multiplicity(1, 1))
    }
)
querySelect162: BinaryAssociation = BinaryAssociation(
    name="querySelect162",
    ends={
        Property(name="QuerySelect163", type=query_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="fromClause", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
nest164: BinaryAssociation = BinaryAssociation(
    name="nest164",
    ends={
        Property(name="TableNested", type=query_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedTableRef", type=query_TableNested, multiplicity=Multiplicity(0, 1))
    }
)
mergeSourceTable165: BinaryAssociation = BinaryAssociation(
    name="mergeSourceTable165",
    ends={
        Property(name="MergeSourceTable", type=query_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="tableRef", type=query_MergeSourceTable, multiplicity=Multiplicity(0, 1))
    }
)
columnList166: BinaryAssociation = BinaryAssociation(
    name="columnList166",
    ends={
        Property(name="ValueExpressionColumn167", type=query_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parentTableExpr", type=query_ValueExpressionColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableCorrelation168: BinaryAssociation = BinaryAssociation(
    name="tableCorrelation168",
    ends={
        Property(name="TableCorrelation", type=query_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tableExpr", type=query_TableCorrelation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultTableAllColumns169: BinaryAssociation = BinaryAssociation(
    name="resultTableAllColumns169",
    ends={
        Property(name="ResultTableAllColumns", type=query_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tableExpr170", type=query_ResultTableAllColumns, multiplicity=Multiplicity(0, 9999))
    }
)
mergeTargetTable174: BinaryAssociation = BinaryAssociation(
    name="mergeTargetTable174",
    ends={
        Property(name="MergeTargetTable", type=query_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tableExpr175", type=query_MergeTargetTable, multiplicity=Multiplicity(0, 1))
    }
)
joinCondition176: BinaryAssociation = BinaryAssociation(
    name="joinCondition176",
    ends={
        Property(name="QuerySearchCondition177", type=query_TableJoined, multiplicity=Multiplicity(1, 1)),
        Property(name="tableJoined", type=query_QuerySearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableRefRight178: BinaryAssociation = BinaryAssociation(
    name="tableRefRight178",
    ends={
        Property(name="TableReference", type=query_TableJoined, multiplicity=Multiplicity(1, 1)),
        Property(name="tableJoinedRight", type=query_TableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableRefLeft179: BinaryAssociation = BinaryAssociation(
    name="tableRefLeft179",
    ends={
        Property(name="TableReference180", type=query_TableJoined, multiplicity=Multiplicity(1, 1)),
        Property(name="tableJoinedLeft", type=query_TableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryExpressionRoot181: BinaryAssociation = BinaryAssociation(
    name="queryExpressionRoot181",
    ends={
        Property(name="QueryExpressionRoot182", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="withClause", type=query_QueryExpressionRoot, multiplicity=Multiplicity(0, 1))
    }
)
leftCondition189: BinaryAssociation = BinaryAssociation(
    name="leftCondition189",
    ends={
        Property(name="QuerySearchCondition190", type=query_SearchConditionCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="combinedLeft", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
withTableQueryExpr183: BinaryAssociation = BinaryAssociation(
    name="withTableQueryExpr183",
    ends={
        Property(name="QueryExpressionBody184", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="withTableSpecification", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
withTableReferences185: BinaryAssociation = BinaryAssociation(
    name="withTableReferences185",
    ends={
        Property(name="WithTableReference", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="withTableSpecification186", type=query_WithTableReference, multiplicity=Multiplicity(0, 9999))
    }
)
columnNameList187: BinaryAssociation = BinaryAssociation(
    name="columnNameList187",
    ends={
        Property(name="ColumnName", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="withTableSpecification188", type=query_ColumnName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightCondition191: BinaryAssociation = BinaryAssociation(
    name="rightCondition191",
    ends={
        Property(name="QuerySearchCondition192", type=query_SearchConditionCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="combinedRight", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr193: BinaryAssociation = BinaryAssociation(
    name="valueExpr193",
    ends={
        Property(name="QueryValueExpression194", type=query_OrderByValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="orderByValueExpr", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftQuery195: BinaryAssociation = BinaryAssociation(
    name="leftQuery195",
    ends={
        Property(name="QueryExpressionBody197", type=query_QueryCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="combinedLeft196", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightQuery198: BinaryAssociation = BinaryAssociation(
    name="rightQuery198",
    ends={
        Property(name="QueryExpressionBody200", type=query_QueryCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="combinedRight199", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
querySelect213: BinaryAssociation = BinaryAssociation(
    name="querySelect213",
    ends={
        Property(name="QuerySelect214", type=query_GroupingSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="groupByClause", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
havingClause201: BinaryAssociation = BinaryAssociation(
    name="havingClause201",
    ends={
        Property(name="QuerySearchCondition202", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelectHaving", type=query_QuerySearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause203: BinaryAssociation = BinaryAssociation(
    name="whereClause203",
    ends={
        Property(name="QuerySearchCondition204", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelectWhere", type=query_QuerySearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByClause205: BinaryAssociation = BinaryAssociation(
    name="groupByClause205",
    ends={
        Property(name="GroupingSpecification", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelect", type=query_GroupingSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectClause206: BinaryAssociation = BinaryAssociation(
    name="selectClause206",
    ends={
        Property(name="QueryResultSpecification", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelect207", type=query_QueryResultSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromClause208: BinaryAssociation = BinaryAssociation(
    name="fromClause208",
    ends={
        Property(name="TableReference210", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelect209", type=query_TableReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
intoClause211: BinaryAssociation = BinaryAssociation(
    name="intoClause211",
    ends={
        Property(name="ValueExpressionVariable", type=query_QuerySelect, multiplicity=Multiplicity(1, 1)),
        Property(name="querySelect212", type=query_ValueExpressionVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightValueExpr221: BinaryAssociation = BinaryAssociation(
    name="rightValueExpr221",
    ends={
        Property(name="QueryValueExpression222", type=query_PredicateBasic, multiplicity=Multiplicity(1, 1)),
        Property(name="basicRight", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
querySelect215: BinaryAssociation = BinaryAssociation(
    name="querySelect215",
    ends={
        Property(name="QuerySelect216", type=query_QueryResultSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="selectClause", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
tableExpr217: BinaryAssociation = BinaryAssociation(
    name="tableExpr217",
    ends={
        Property(name="TableExpression", type=query_ResultTableAllColumns, multiplicity=Multiplicity(1, 1)),
        Property(name="resultTableAllColumns", type=query_TableExpression, multiplicity=Multiplicity(1, 1))
    }
)
valueExpr218: BinaryAssociation = BinaryAssociation(
    name="valueExpr218",
    ends={
        Property(name="QueryValueExpression219", type=query_ResultColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="resultColumn", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
orderByResultCol220: BinaryAssociation = BinaryAssociation(
    name="orderByResultCol220",
    ends={
        Property(name="OrderByResultColumn", type=query_ResultColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="resultCol", type=query_OrderByResultColumn, multiplicity=Multiplicity(0, 9999))
    }
)
leftValueExpr223: BinaryAssociation = BinaryAssociation(
    name="leftValueExpr223",
    ends={
        Property(name="QueryValueExpression224", type=query_PredicateBasic, multiplicity=Multiplicity(1, 1)),
        Property(name="basicLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftValueExpr225: BinaryAssociation = BinaryAssociation(
    name="leftValueExpr225",
    ends={
        Property(name="QueryValueExpression226", type=query_PredicateBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="betweenLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightValueExpr1227: BinaryAssociation = BinaryAssociation(
    name="rightValueExpr1227",
    ends={
        Property(name="QueryValueExpression228", type=query_PredicateBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="betweenRight1", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightValueExpr2229: BinaryAssociation = BinaryAssociation(
    name="rightValueExpr2229",
    ends={
        Property(name="QueryValueExpression230", type=query_PredicateBetween, multiplicity=Multiplicity(1, 1)),
        Property(name="betweenRight2", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryExpr231: BinaryAssociation = BinaryAssociation(
    name="queryExpr231",
    ends={
        Property(name="QueryExpressionBody232", type=query_PredicateExists, multiplicity=Multiplicity(1, 1)),
        Property(name="predicateExists", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patternValueExpr233: BinaryAssociation = BinaryAssociation(
    name="patternValueExpr233",
    ends={
        Property(name="QueryValueExpression234", type=query_PredicateLike, multiplicity=Multiplicity(1, 1)),
        Property(name="likePattern", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
matchingValueExpr235: BinaryAssociation = BinaryAssociation(
    name="matchingValueExpr235",
    ends={
        Property(name="QueryValueExpression236", type=query_PredicateLike, multiplicity=Multiplicity(1, 1)),
        Property(name="likeMatching", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
escapeValueExpr237: BinaryAssociation = BinaryAssociation(
    name="escapeValueExpr237",
    ends={
        Property(name="QueryValueExpression238", type=query_PredicateLike, multiplicity=Multiplicity(1, 1)),
        Property(name="likeEscape", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueExprList247: BinaryAssociation = BinaryAssociation(
    name="valueExprList247",
    ends={
        Property(name="QueryValueExpression248", type=query_PredicateQuantifiedRowSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="quantifiedRowSelectLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExpr239: BinaryAssociation = BinaryAssociation(
    name="valueExpr239",
    ends={
        Property(name="QueryValueExpression240", type=query_PredicateIsNull, multiplicity=Multiplicity(1, 1)),
        Property(name="predicateNull", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryExpr241: BinaryAssociation = BinaryAssociation(
    name="queryExpr241",
    ends={
        Property(name="QueryExpressionRoot242", type=query_PredicateQuantifiedValueSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="quantifiedValueSelectRight", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr243: BinaryAssociation = BinaryAssociation(
    name="valueExpr243",
    ends={
        Property(name="QueryValueExpression244", type=query_PredicateQuantifiedValueSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="quantifiedValueSelectLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryExpr245: BinaryAssociation = BinaryAssociation(
    name="queryExpr245",
    ends={
        Property(name="QueryExpressionRoot246", type=query_PredicateQuantifiedRowSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="quantifiedRowSelectRight", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExprList257: BinaryAssociation = BinaryAssociation(
    name="valueExprList257",
    ends={
        Property(name="QueryValueExpression258", type=query_PredicateInValueRowSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueRowSelectLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
queryExpr249: BinaryAssociation = BinaryAssociation(
    name="queryExpr249",
    ends={
        Property(name="QueryExpressionRoot250", type=query_PredicateInValueSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueSelectRight", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr251: BinaryAssociation = BinaryAssociation(
    name="valueExpr251",
    ends={
        Property(name="QueryValueExpression252", type=query_PredicateInValueSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueSelectLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExprList253: BinaryAssociation = BinaryAssociation(
    name="valueExprList253",
    ends={
        Property(name="QueryValueExpression254", type=query_PredicateInValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueListRight", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExpr255: BinaryAssociation = BinaryAssociation(
    name="valueExpr255",
    ends={
        Property(name="QueryValueExpression256", type=query_PredicateInValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueListLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableInDatabase270: BinaryAssociation = BinaryAssociation(
    name="tableInDatabase270",
    ends={
        Property(name="TableInDatabase271", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedColumnList", type=query_TableInDatabase, multiplicity=Multiplicity(0, 1))
    }
)
queryExpr259: BinaryAssociation = BinaryAssociation(
    name="queryExpr259",
    ends={
        Property(name="QueryExpressionRoot260", type=query_PredicateInValueRowSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="inValueRowSelectRight", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentExprTarget261: BinaryAssociation = BinaryAssociation(
    name="assignmentExprTarget261",
    ends={
        Property(name="UpdateAssignmentExpression262", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="targetColumnList", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(0, 9999))
    }
)
parentTableExpr263: BinaryAssociation = BinaryAssociation(
    name="parentTableExpr263",
    ends={
        Property(name="TableExpression264", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columnList", type=query_TableExpression, multiplicity=Multiplicity(1, 1))
    }
)
insertStatement265: BinaryAssociation = BinaryAssociation(
    name="insertStatement265",
    ends={
        Property(name="QueryInsertStatement267", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="targetColumnList266", type=query_QueryInsertStatement, multiplicity=Multiplicity(0, 9999))
    }
)
tableExpr268: BinaryAssociation = BinaryAssociation(
    name="tableExpr268",
    ends={
        Property(name="TableExpression269", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprColumns", type=query_TableExpression, multiplicity=Multiplicity(1, 1))
    }
)
caseElse280: BinaryAssociation = BinaryAssociation(
    name="caseElse280",
    ends={
        Property(name="ValueExpressionCaseElse281", type=query_ValueExpressionCase, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCase", type=query_ValueExpressionCaseElse, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mergeInsertSpec272: BinaryAssociation = BinaryAssociation(
    name="mergeInsertSpec272",
    ends={
        Property(name="MergeInsertSpecification", type=query_ValueExpressionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="targetColumnList273", type=query_MergeInsertSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
querySelect274: BinaryAssociation = BinaryAssociation(
    name="querySelect274",
    ends={
        Property(name="QuerySelect275", type=query_ValueExpressionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="intoClause", type=query_QuerySelect, multiplicity=Multiplicity(0, 1))
    }
)
queryExpr276: BinaryAssociation = BinaryAssociation(
    name="queryExpr276",
    ends={
        Property(name="QueryExpressionRoot277", type=query_ValueExpressionScalarSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="valExprScalarSelect", type=query_QueryExpressionRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr278: BinaryAssociation = BinaryAssociation(
    name="valueExpr278",
    ends={
        Property(name="QueryValueExpression279", type=query_ValueExpressionLabeledDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprLabeledDuration", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftValueExpr287: BinaryAssociation = BinaryAssociation(
    name="leftValueExpr287",
    ends={
        Property(name="QueryValueExpression288", type=query_ValueExpressionCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCombinedLeft", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr282: BinaryAssociation = BinaryAssociation(
    name="valueExpr282",
    ends={
        Property(name="QueryValueExpression283", type=query_ValueExpressionCast, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCast", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterList284: BinaryAssociation = BinaryAssociation(
    name="parameterList284",
    ends={
        Property(name="QueryValueExpression285", type=query_ValueExpressionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprFunction", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function286: BinaryAssociation = BinaryAssociation(
    name="function286",
    ends={
        Property(name="Function", type=query_ValueExpressionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="query_ValueExpressionFunction", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
groupingSetsElementExprList294: BinaryAssociation = BinaryAssociation(
    name="groupingSetsElementExprList294",
    ends={
        Property(name="GroupingSetsElementExpression295", type=query_GroupingSetsElementSublist, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingSetsElementSublist", type=query_GroupingSetsElementExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rightValueExpr289: BinaryAssociation = BinaryAssociation(
    name="rightValueExpr289",
    ends={
        Property(name="QueryValueExpression290", type=query_ValueExpressionCombined, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCombinedRight", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groupingSetsElementList291: BinaryAssociation = BinaryAssociation(
    name="groupingSetsElementList291",
    ends={
        Property(name="GroupingSetsElement", type=query_GroupingSets, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingSets", type=query_GroupingSetsElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
groupingSetsElementExpr292: BinaryAssociation = BinaryAssociation(
    name="groupingSetsElementExpr292",
    ends={
        Property(name="GroupingSetsElementExpression", type=query_Grouping, multiplicity=Multiplicity(1, 1)),
        Property(name="grouping", type=query_GroupingSetsElementExpression, multiplicity=Multiplicity(0, 1))
    }
)
groupingSets293: BinaryAssociation = BinaryAssociation(
    name="groupingSets293",
    ends={
        Property(name="GroupingSets", type=query_GroupingSetsElement, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingSetsElementList", type=query_GroupingSets, multiplicity=Multiplicity(0, 1))
    }
)
superGroup303: BinaryAssociation = BinaryAssociation(
    name="superGroup303",
    ends={
        Property(name="superGroupElementList", type=query_SuperGroup, multiplicity=Multiplicity(0, 1)),
        Property(name="SuperGroup", type=query_SuperGroupElement, multiplicity=Multiplicity(1, 1))
    }
)
groupingSetsElementSublist296: BinaryAssociation = BinaryAssociation(
    name="groupingSetsElementSublist296",
    ends={
        Property(name="GroupingSetsElementSublist", type=query_GroupingSetsElementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingSetsElementExprList", type=query_GroupingSetsElementSublist, multiplicity=Multiplicity(0, 1))
    }
)
grouping297: BinaryAssociation = BinaryAssociation(
    name="grouping297",
    ends={
        Property(name="Grouping", type=query_GroupingSetsElementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingSetsElementExpr", type=query_Grouping, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superGroupElementList298: BinaryAssociation = BinaryAssociation(
    name="superGroupElementList298",
    ends={
        Property(name="SuperGroupElement", type=query_SuperGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroup", type=query_SuperGroupElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueExpr299: BinaryAssociation = BinaryAssociation(
    name="valueExpr299",
    ends={
        Property(name="QueryValueExpression300", type=query_GroupingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingExpr", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superGroupElementExpr301: BinaryAssociation = BinaryAssociation(
    name="superGroupElementExpr301",
    ends={
        Property(name="SuperGroupElementExpression", type=query_GroupingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="groupingExpr302", type=query_SuperGroupElementExpression, multiplicity=Multiplicity(0, 1))
    }
)
valueExprCase316: BinaryAssociation = BinaryAssociation(
    name="valueExprCase316",
    ends={
        Property(name="ValueExpressionCase", type=query_ValueExpressionCaseElse, multiplicity=Multiplicity(1, 1)),
        Property(name="caseElse", type=query_ValueExpressionCase, multiplicity=Multiplicity(0, 1))
    }
)
superGroupElementExprList304: BinaryAssociation = BinaryAssociation(
    name="superGroupElementExprList304",
    ends={
        Property(name="SuperGroupElementExpression305", type=query_SuperGroupElementSublist, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroupElementSublist", type=query_SuperGroupElementExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExpr317: BinaryAssociation = BinaryAssociation(
    name="valueExpr317",
    ends={
        Property(name="QueryValueExpression318", type=query_ValueExpressionCaseElse, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseElse", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superGroupElementSublist306: BinaryAssociation = BinaryAssociation(
    name="superGroupElementSublist306",
    ends={
        Property(name="SuperGroupElementSublist", type=query_SuperGroupElementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroupElementExprList", type=query_SuperGroupElementSublist, multiplicity=Multiplicity(0, 1))
    }
)
groupingExpr307: BinaryAssociation = BinaryAssociation(
    name="groupingExpr307",
    ends={
        Property(name="GroupingExpression308", type=query_SuperGroupElementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroupElementExpr", type=query_GroupingExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExpr319: BinaryAssociation = BinaryAssociation(
    name="valueExpr319",
    ends={
        Property(name="QueryValueExpression320", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSearchContent", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
searchContentList309: BinaryAssociation = BinaryAssociation(
    name="searchContentList309",
    ends={
        Property(name="ValueExpressionCaseSearchContent310", type=query_ValueExpressionCaseSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSearch", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contentList311: BinaryAssociation = BinaryAssociation(
    name="contentList311",
    ends={
        Property(name="ValueExpressionCaseSimpleContent312", type=query_ValueExpressionCaseSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSimple", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueExpr313: BinaryAssociation = BinaryAssociation(
    name="valueExpr313",
    ends={
        Property(name="QueryValueExpression315", type=query_ValueExpressionCaseSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSimple314", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExprCaseSimple325: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSimple325",
    ends={
        Property(name="ValueExpressionCaseSimple326", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentList", type=query_ValueExpressionCaseSimple, multiplicity=Multiplicity(0, 1))
    }
)
whenValueExpr327: BinaryAssociation = BinaryAssociation(
    name="whenValueExpr327",
    ends={
        Property(name="QueryValueExpression328", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSimpleContentWhen", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultValueExpr329: BinaryAssociation = BinaryAssociation(
    name="resultValueExpr329",
    ends={
        Property(name="QueryValueExpression330", type=query_ValueExpressionCaseSimpleContent, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSimpleContentResult", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
searchCondition321: BinaryAssociation = BinaryAssociation(
    name="searchCondition321",
    ends={
        Property(name="QuerySearchCondition323", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprCaseSearchContent322", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExprCaseSearch324: BinaryAssociation = BinaryAssociation(
    name="valueExprCaseSearch324",
    ends={
        Property(name="ValueExpressionCaseSearch", type=query_ValueExpressionCaseSearchContent, multiplicity=Multiplicity(1, 1)),
        Property(name="searchContentList", type=query_ValueExpressionCaseSearch, multiplicity=Multiplicity(0, 1))
    }
)
updateStatement331: BinaryAssociation = BinaryAssociation(
    name="updateStatement331",
    ends={
        Property(name="targetTable", type=query_QueryUpdateStatement, multiplicity=Multiplicity(0, 1)),
        Property(name="QueryUpdateStatement332", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1))
    }
)
deleteStatement333: BinaryAssociation = BinaryAssociation(
    name="deleteStatement333",
    ends={
        Property(name="QueryDeleteStatement335", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="targetTable334", type=query_QueryDeleteStatement, multiplicity=Multiplicity(0, 1))
    }
)
insertStatement336: BinaryAssociation = BinaryAssociation(
    name="insertStatement336",
    ends={
        Property(name="QueryInsertStatement338", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="targetTable337", type=query_QueryInsertStatement, multiplicity=Multiplicity(0, 1))
    }
)
databaseTable339: BinaryAssociation = BinaryAssociation(
    name="databaseTable339",
    ends={
        Property(name="Table", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="query_TableInDatabase", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
function342: BinaryAssociation = BinaryAssociation(
    name="function342",
    ends={
        Property(name="query_TableFunction", type=Function, multiplicity=Multiplicity(1, 1)),
        Property(name="Function343", type=query_TableFunction, multiplicity=Multiplicity(1, 1))
    }
)
parameterList344: BinaryAssociation = BinaryAssociation(
    name="parameterList344",
    ends={
        Property(name="QueryValueExpression345", type=query_TableFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="tableFunction", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivedColumnList340: BinaryAssociation = BinaryAssociation(
    name="derivedColumnList340",
    ends={
        Property(name="ValueExpressionColumn341", type=query_TableInDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="tableInDatabase", type=query_ValueExpressionColumn, multiplicity=Multiplicity(0, 9999))
    }
)
withTableSpecification348: BinaryAssociation = BinaryAssociation(
    name="withTableSpecification348",
    ends={
        Property(name="WithTableSpecification350", type=query_ColumnName, multiplicity=Multiplicity(1, 1)),
        Property(name="columnNameList349", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1))
    }
)
nestedTableRef351: BinaryAssociation = BinaryAssociation(
    name="nestedTableRef351",
    ends={
        Property(name="TableReference352", type=query_TableNested, multiplicity=Multiplicity(1, 1)),
        Property(name="nest", type=query_TableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetTable353: BinaryAssociation = BinaryAssociation(
    name="targetTable353",
    ends={
        Property(name="MergeTargetTable354", type=query_QueryMergeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeStatement", type=query_MergeTargetTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableCorrelation346: BinaryAssociation = BinaryAssociation(
    name="tableCorrelation346",
    ends={
        Property(name="TableCorrelation347", type=query_ColumnName, multiplicity=Multiplicity(1, 1)),
        Property(name="columnNameList", type=query_TableCorrelation, multiplicity=Multiplicity(0, 1))
    }
)
operationSpecList361: BinaryAssociation = BinaryAssociation(
    name="operationSpecList361",
    ends={
        Property(name="MergeOperationSpecification", type=query_QueryMergeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeStatement362", type=query_MergeOperationSpecification, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nestedCondition363: BinaryAssociation = BinaryAssociation(
    name="nestedCondition363",
    ends={
        Property(name="QuerySearchCondition365", type=query_SearchConditionNested, multiplicity=Multiplicity(1, 1)),
        Property(name="nest364", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nestedValueExpr366: BinaryAssociation = BinaryAssociation(
    name="nestedValueExpr366",
    ends={
        Property(name="QueryValueExpression368", type=query_ValueExpressionNested, multiplicity=Multiplicity(1, 1)),
        Property(name="nest367", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceTable355: BinaryAssociation = BinaryAssociation(
    name="sourceTable355",
    ends={
        Property(name="MergeSourceTable357", type=query_QueryMergeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeStatement356", type=query_MergeSourceTable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
onCondition358: BinaryAssociation = BinaryAssociation(
    name="onCondition358",
    ends={
        Property(name="MergeOnCondition360", type=query_QueryMergeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeStatement359", type=query_MergeOnCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectStatement369: BinaryAssociation = BinaryAssociation(
    name="selectStatement369",
    ends={
        Property(name="QuerySelectStatement370", type=query_OrderBySpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="orderByClause", type=query_QuerySelectStatement, multiplicity=Multiplicity(0, 1))
    }
)
query371: BinaryAssociation = BinaryAssociation(
    name="query371",
    ends={
        Property(name="QueryExpressionBody372", type=query_OrderBySpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="sortSpecList", type=query_QueryExpressionBody, multiplicity=Multiplicity(0, 1))
    }
)
updateAssignmentExpr378: BinaryAssociation = BinaryAssociation(
    name="updateAssignmentExpr378",
    ends={
        Property(name="UpdateAssignmentExpression379", type=query_UpdateSource, multiplicity=Multiplicity(1, 1)),
        Property(name="updateSource", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(0, 1))
    }
)
valueExprList380: BinaryAssociation = BinaryAssociation(
    name="valueExprList380",
    ends={
        Property(name="QueryValueExpression381", type=query_UpdateSourceExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="updateSourceExprList", type=query_QueryValueExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tableExpr373: BinaryAssociation = BinaryAssociation(
    name="tableExpr373",
    ends={
        Property(name="TableExpression374", type=query_TableCorrelation, multiplicity=Multiplicity(1, 1)),
        Property(name="tableCorrelation", type=query_TableExpression, multiplicity=Multiplicity(0, 1))
    }
)
columnNameList375: BinaryAssociation = BinaryAssociation(
    name="columnNameList375",
    ends={
        Property(name="ColumnName377", type=query_TableCorrelation, multiplicity=Multiplicity(1, 1)),
        Property(name="tableCorrelation376", type=query_ColumnName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
withTableSpecification386: BinaryAssociation = BinaryAssociation(
    name="withTableSpecification386",
    ends={
        Property(name="WithTableSpecification387", type=query_WithTableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="withTableReferences", type=query_WithTableSpecification, multiplicity=Multiplicity(1, 1))
    }
)
queryExpr382: BinaryAssociation = BinaryAssociation(
    name="queryExpr382",
    ends={
        Property(name="QueryExpressionBody383", type=query_UpdateSourceQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="updateSourceQuery", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resultCol384: BinaryAssociation = BinaryAssociation(
    name="resultCol384",
    ends={
        Property(name="ResultColumn385", type=query_OrderByResultColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="orderByResultCol", type=query_ResultColumn, multiplicity=Multiplicity(1, 1))
    }
)
nestedQuery388: BinaryAssociation = BinaryAssociation(
    name="nestedQuery388",
    ends={
        Property(name="QueryExpressionBody389", type=query_QueryNested, multiplicity=Multiplicity(1, 1)),
        Property(name="queryNest", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueExprList390: BinaryAssociation = BinaryAssociation(
    name="valueExprList390",
    ends={
        Property(name="QueryValueExpression391", type=query_ValueExpressionRow, multiplicity=Multiplicity(1, 1)),
        Property(name="valueExprRow", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableRef399: BinaryAssociation = BinaryAssociation(
    name="tableRef399",
    ends={
        Property(name="TableReference400", type=query_MergeSourceTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeSourceTable", type=query_TableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mergeStatement392: BinaryAssociation = BinaryAssociation(
    name="mergeStatement392",
    ends={
        Property(name="QueryMergeStatement", type=query_MergeTargetTable, multiplicity=Multiplicity(1, 1)),
        Property(name="targetTable393", type=query_QueryMergeStatement, multiplicity=Multiplicity(0, 1))
    }
)
tableExpr394: BinaryAssociation = BinaryAssociation(
    name="tableExpr394",
    ends={
        Property(name="TableExpression395", type=query_MergeTargetTable, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeTargetTable", type=query_TableExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
QueryMergeStatement396: BinaryAssociation = BinaryAssociation(
    name="QueryMergeStatement396",
    ends={
        Property(name="query_QueryMergeStatement", type=query_MergeSourceTable, multiplicity=Multiplicity(1, 1)),
        Property(name="query_MergeSourceTable", type=query_QueryMergeStatement, multiplicity=Multiplicity(0, 9999))
    }
)
mergeStatement397: BinaryAssociation = BinaryAssociation(
    name="mergeStatement397",
    ends={
        Property(name="QueryMergeStatement398", type=query_MergeSourceTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceTable", type=query_QueryMergeStatement, multiplicity=Multiplicity(0, 1))
    }
)
targetColumnList407: BinaryAssociation = BinaryAssociation(
    name="targetColumnList407",
    ends={
        Property(name="ValueExpressionColumn408", type=query_MergeInsertSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeInsertSpec", type=query_ValueExpressionColumn, multiplicity=Multiplicity(0, 9999))
    }
)
mergeStatement401: BinaryAssociation = BinaryAssociation(
    name="mergeStatement401",
    ends={
        Property(name="QueryMergeStatement402", type=query_MergeOnCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="onCondition", type=query_QueryMergeStatement, multiplicity=Multiplicity(0, 1))
    }
)
searchCondition403: BinaryAssociation = BinaryAssociation(
    name="searchCondition403",
    ends={
        Property(name="QuerySearchCondition404", type=query_MergeOnCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeOnCondition", type=query_QuerySearchCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignementExprList405: BinaryAssociation = BinaryAssociation(
    name="assignementExprList405",
    ends={
        Property(name="UpdateAssignmentExpression406", type=query_MergeUpdateSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="mergeUpdateSpec", type=query_UpdateAssignmentExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
updateOfColumnList414: BinaryAssociation = BinaryAssociation(
    name="updateOfColumnList414",
    ends={
        Property(name="UpdateOfColumn", type=query_UpdatabilityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="updatabilityExpr", type=query_UpdateOfColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceValuesRow409: BinaryAssociation = BinaryAssociation(
    name="sourceValuesRow409",
    ends={
        Property(name="query_ValuesRow", type=query_MergeInsertSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="query_MergeInsertSpecification", type=query_ValuesRow, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mergeStatement410: BinaryAssociation = BinaryAssociation(
    name="mergeStatement410",
    ends={
        Property(name="QueryMergeStatement411", type=query_MergeOperationSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="operationSpecList", type=query_QueryMergeStatement, multiplicity=Multiplicity(0, 1))
    }
)
updatabilityExpr412: BinaryAssociation = BinaryAssociation(
    name="updatabilityExpr412",
    ends={
        Property(name="UpdatabilityExpression413", type=query_UpdateOfColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="updateOfColumnList", type=query_UpdatabilityExpression, multiplicity=Multiplicity(0, 1))
    }
)
procedure424: BinaryAssociation = BinaryAssociation(
    name="procedure424",
    ends={
        Property(name="Procedure", type=query_ProcedureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="query_ProcedureReference", type=Procedure, multiplicity=Multiplicity(1, 1))
    }
)
selectStatement415: BinaryAssociation = BinaryAssociation(
    name="selectStatement415",
    ends={
        Property(name="QuerySelectStatement417", type=query_UpdatabilityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="updatabilityExpr416", type=query_QuerySelectStatement, multiplicity=Multiplicity(0, 1))
    }
)
argumentList418: BinaryAssociation = BinaryAssociation(
    name="argumentList418",
    ends={
        Property(name="QueryValueExpression419", type=query_CallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="callStatement", type=query_QueryValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedureRef420: BinaryAssociation = BinaryAssociation(
    name="procedureRef420",
    ends={
        Property(name="ProcedureReference", type=query_CallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="callStatement421", type=query_ProcedureReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callStatement422: BinaryAssociation = BinaryAssociation(
    name="callStatement422",
    ends={
        Property(name="CallStatement423", type=query_ProcedureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="procedureRef", type=query_CallStatement, multiplicity=Multiplicity(1, 1))
    }
)
query425: BinaryAssociation = BinaryAssociation(
    name="query425",
    ends={
        Property(name="query_QueryExpressionBody", type=query_TableQueryLateral, multiplicity=Multiplicity(1, 1)),
        Property(name="query_TableQueryLateral", type=query_QueryExpressionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_query_QueryDeleteStatement_QueryChangeStatement = Generalization(general=QueryChangeStatement, specific=query_QueryDeleteStatement)
gen_query_QueryStatement_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_QueryStatement)
gen_query_QueryStatement_statements_SQLDataStatement = Generalization(general=statements_SQLDataStatement, specific=query_QueryStatement)
gen_query_QueryInsertStatement_QueryChangeStatement = Generalization(general=QueryChangeStatement, specific=query_QueryInsertStatement)
gen_query_QuerySelectStatement_QueryStatement = Generalization(general=QueryStatement, specific=query_QuerySelectStatement)
gen_query_QueryUpdateStatement_QueryChangeStatement = Generalization(general=QueryChangeStatement, specific=query_QueryUpdateStatement)
gen_query_CursorReference_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_CursorReference)
gen_query_UpdateAssignmentExpression_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_UpdateAssignmentExpression)
gen_query_QuerySearchCondition_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_QuerySearchCondition)
gen_query_QuerySearchCondition_expressions_SearchCondition = Generalization(general=expressions_SearchCondition, specific=query_QuerySearchCondition)
gen_query_QueryExpressionBody_TableExpression = Generalization(general=TableExpression, specific=query_QueryExpressionBody)
gen_query_QueryValueExpression_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_QueryValueExpression)
gen_query_QueryValueExpression_expressions_ValueExpression = Generalization(general=expressions_ValueExpression, specific=query_QueryValueExpression)
gen_query_QueryExpressionRoot_expressions_QueryExpression = Generalization(general=expressions_QueryExpression, specific=query_QueryExpressionRoot)
gen_query_QueryExpressionRoot_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_QueryExpressionRoot)
gen_query_ValuesRow_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ValuesRow)
gen_query_QueryValues_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=query_QueryValues)
gen_query_TableReference_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_TableReference)
gen_query_TableExpression_TableReference = Generalization(general=TableReference, specific=query_TableExpression)
gen_query_TableJoined_TableReference = Generalization(general=TableReference, specific=query_TableJoined)
gen_query_WithTableSpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_WithTableSpecification)
gen_query_Predicate_QuerySearchCondition = Generalization(general=QuerySearchCondition, specific=query_Predicate)
gen_query_SearchConditionCombined_QuerySearchCondition = Generalization(general=QuerySearchCondition, specific=query_SearchConditionCombined)
gen_query_QuerySelect_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=query_QuerySelect)
gen_query_OrderByValueExpression_OrderBySpecification = Generalization(general=OrderBySpecification, specific=query_OrderByValueExpression)
gen_query_QueryCombined_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=query_QueryCombined)
gen_query_QueryResultSpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_QueryResultSpecification)
gen_query_GroupingSpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_GroupingSpecification)
gen_query_ResultTableAllColumns_QueryResultSpecification = Generalization(general=QueryResultSpecification, specific=query_ResultTableAllColumns)
gen_query_ResultColumn_QueryResultSpecification = Generalization(general=QueryResultSpecification, specific=query_ResultColumn)
gen_query_PredicateBasic_Predicate = Generalization(general=Predicate, specific=query_PredicateBasic)
gen_query_PredicateExists_Predicate = Generalization(general=Predicate, specific=query_PredicateExists)
gen_query_PredicateQuantified_Predicate = Generalization(general=Predicate, specific=query_PredicateQuantified)
gen_query_PredicateBetween_Predicate = Generalization(general=Predicate, specific=query_PredicateBetween)
gen_query_PredicateIsNull_Predicate = Generalization(general=Predicate, specific=query_PredicateIsNull)
gen_query_PredicateIn_Predicate = Generalization(general=Predicate, specific=query_PredicateIn)
gen_query_PredicateLike_Predicate = Generalization(general=Predicate, specific=query_PredicateLike)
gen_query_PredicateQuantifiedValueSelect_PredicateQuantified = Generalization(general=PredicateQuantified, specific=query_PredicateQuantifiedValueSelect)
gen_query_PredicateQuantifiedRowSelect_PredicateQuantified = Generalization(general=PredicateQuantified, specific=query_PredicateQuantifiedRowSelect)
gen_query_PredicateInValueSelect_PredicateIn = Generalization(general=PredicateIn, specific=query_PredicateInValueSelect)
gen_query_PredicateInValueList_PredicateIn = Generalization(general=PredicateIn, specific=query_PredicateInValueList)
gen_query_PredicateInValueRowSelect_PredicateIn = Generalization(general=PredicateIn, specific=query_PredicateInValueRowSelect)
gen_query_ValueExpressionSimple_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionSimple)
gen_query_ValueExpressionColumn_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionColumn)
gen_query_ValueExpressionCase_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionCase)
gen_query_ValueExpressionVariable_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionVariable)
gen_query_ValueExpressionScalarSelect_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionScalarSelect)
gen_query_ValueExpressionLabeledDuration_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionLabeledDuration)
gen_query_ValueExpressionCast_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionCast)
gen_query_ValueExpressionNullValue_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionNullValue)
gen_query_ValueExpressionDefaultValue_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionDefaultValue)
gen_query_ValueExpressionFunction_ValueExpressionAtomic = Generalization(general=ValueExpressionAtomic, specific=query_ValueExpressionFunction)
gen_query_ValueExpressionCombined_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_ValueExpressionCombined)
gen_query_GroupingSetsElementExpression_GroupingSetsElement = Generalization(general=GroupingSetsElement, specific=query_GroupingSetsElementExpression)
gen_query_GroupingSets_GroupingSpecification = Generalization(general=GroupingSpecification, specific=query_GroupingSets)
gen_query_Grouping_GroupingSpecification = Generalization(general=GroupingSpecification, specific=query_Grouping)
gen_query_GroupingSetsElement_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_GroupingSetsElement)
gen_query_GroupingSetsElementSublist_GroupingSetsElement = Generalization(general=GroupingSetsElement, specific=query_GroupingSetsElementSublist)
gen_query_SuperGroupElementSublist_SuperGroupElement = Generalization(general=SuperGroupElement, specific=query_SuperGroupElementSublist)
gen_query_SuperGroup_Grouping = Generalization(general=Grouping, specific=query_SuperGroup)
gen_query_GroupingExpression_Grouping = Generalization(general=Grouping, specific=query_GroupingExpression)
gen_query_SuperGroupElement_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_SuperGroupElement)
gen_query_ValueExpressionCaseElse_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ValueExpressionCaseElse)
gen_query_SuperGroupElementExpression_SuperGroupElement = Generalization(general=SuperGroupElement, specific=query_SuperGroupElementExpression)
gen_query_ValueExpressionCaseSearchContent_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ValueExpressionCaseSearchContent)
gen_query_ValueExpressionCaseSearch_ValueExpressionCase = Generalization(general=ValueExpressionCase, specific=query_ValueExpressionCaseSearch)
gen_query_ValueExpressionCaseSimple_ValueExpressionCase = Generalization(general=ValueExpressionCase, specific=query_ValueExpressionCaseSimple)
gen_query_ValueExpressionCaseSimpleContent_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ValueExpressionCaseSimpleContent)
gen_query_TableInDatabase_TableExpression = Generalization(general=TableExpression, specific=query_TableInDatabase)
gen_query_SQLQueryObject_SQLObject = Generalization(general=SQLObject, specific=query_SQLQueryObject)
gen_query_TableFunction_TableExpression = Generalization(general=TableExpression, specific=query_TableFunction)
gen_query_TableNested_TableReference = Generalization(general=TableReference, specific=query_TableNested)
gen_query_QueryMergeStatement_QueryChangeStatement = Generalization(general=QueryChangeStatement, specific=query_QueryMergeStatement)
gen_query_QueryChangeStatement_QueryStatement = Generalization(general=QueryStatement, specific=query_QueryChangeStatement)
gen_query_QueryChangeStatement_statements_SQLDataChangeStatement = Generalization(general=statements_SQLDataChangeStatement, specific=query_QueryChangeStatement)
gen_query_ColumnName_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ColumnName)
gen_query_SearchConditionNested_QuerySearchCondition = Generalization(general=QuerySearchCondition, specific=query_SearchConditionNested)
gen_query_ValueExpressionNested_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_ValueExpressionNested)
gen_query_OrderByOrdinal_OrderBySpecification = Generalization(general=OrderBySpecification, specific=query_OrderByOrdinal)
gen_query_TableCorrelation_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_TableCorrelation)
gen_query_ValueExpressionAtomic_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_ValueExpressionAtomic)
gen_query_OrderBySpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_OrderBySpecification)
gen_query_UpdateSource_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_UpdateSource)
gen_query_UpdateSourceExprList_UpdateSource = Generalization(general=UpdateSource, specific=query_UpdateSourceExprList)
gen_query_UpdateSourceQuery_UpdateSource = Generalization(general=UpdateSource, specific=query_UpdateSourceQuery)
gen_query_WithTableReference_TableExpression = Generalization(general=TableExpression, specific=query_WithTableReference)
gen_query_MergeTargetTable_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_MergeTargetTable)
gen_query_OrderByResultColumn_OrderBySpecification = Generalization(general=OrderBySpecification, specific=query_OrderByResultColumn)
gen_query_QueryNested_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=query_QueryNested)
gen_query_ValueExpressionRow_QueryValueExpression = Generalization(general=QueryValueExpression, specific=query_ValueExpressionRow)
gen_query_MergeOnCondition_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_MergeOnCondition)
gen_query_MergeSourceTable_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_MergeSourceTable)
gen_query_MergeUpdateSpecification_MergeOperationSpecification = Generalization(general=MergeOperationSpecification, specific=query_MergeUpdateSpecification)
gen_query_MergeInsertSpecification_MergeOperationSpecification = Generalization(general=MergeOperationSpecification, specific=query_MergeInsertSpecification)
gen_query_MergeOperationSpecification_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_MergeOperationSpecification)
gen_query_UpdateOfColumn_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_UpdateOfColumn)
gen_query_UpdatabilityExpression_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_UpdatabilityExpression)
gen_query_CallStatement_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_CallStatement)
gen_query_CallStatement_statements_SQLControlStatement = Generalization(general=statements_SQLControlStatement, specific=query_CallStatement)
gen_query_ProcedureReference_SQLQueryObject = Generalization(general=SQLQueryObject, specific=query_ProcedureReference)
gen_query_TableQueryLateral_TableExpression = Generalization(general=TableExpression, specific=query_TableQueryLateral)

# Domain Model
domain_model = DomainModel(
    name="query",
    types={query_QueryDeleteStatement, QueryChangeStatement, query_QueryStatement, SQLQueryObject, statements_SQLDataStatement, query_CursorReference, query_QuerySearchCondition, query_TableInDatabase, query_QueryInsertStatement, query_QueryExpressionRoot, query_ValuesRow, query_ValueExpressionColumn, query_QuerySelectStatement, QueryStatement, query_OrderBySpecification, query_UpdatabilityExpression, query_QueryUpdateStatement, query_UpdateAssignmentExpression, query_UpdateSource, query_MergeUpdateSpecification, expressions_SearchCondition, query_TableJoined, query_SearchConditionCombined, query_QueryCombined, query_QuerySelect, query_ValueExpressionCaseSearchContent, query_SearchConditionNested, query_MergeOnCondition, query_QueryExpressionBody, TableExpression, expressions_ValueExpression, DataType, query_PredicateExists, query_UpdateSourceQuery, query_WithTableSpecification, query_QueryNested, query_QueryValueExpression, query_PredicateIsNull, query_OrderByValueExpression, query_ResultColumn, query_PredicateBasic, query_PredicateLike, query_PredicateBetween, query_PredicateInValueList, query_PredicateInValueRowSelect, query_PredicateInValueSelect, query_PredicateQuantifiedRowSelect, query_PredicateQuantifiedValueSelect, query_GroupingExpression, query_ValueExpressionCaseElse, query_ValueExpressionCast, query_ValueExpressionFunction, query_ValueExpressionCombined, query_ValueExpressionLabeledDuration, query_ValueExpressionNested, query_ValueExpressionCaseSimple, query_ValueExpressionCaseSimpleContent, expressions_QueryExpression, query_UpdateSourceExprList, query_TableFunction, query_ValueExpressionRow, query_CallStatement, query_ValueExpressionScalarSelect, query_QueryValues, QueryExpressionBody, query_TableReference, query_TableNested, query_MergeSourceTable, query_TableExpression, TableReference, query_TableCorrelation, query_ResultTableAllColumns, query_MergeTargetTable, query_WithTableReference, query_ColumnName, query_Predicate, QuerySearchCondition, OrderBySpecification, query_GroupingSpecification, query_QueryResultSpecification, query_ValueExpressionVariable, QueryResultSpecification, query_OrderByResultColumn, Predicate, query_PredicateQuantified, query_PredicateIn, PredicateIn, PredicateQuantified, query_ValueExpressionSimple, ValueExpressionAtomic, query_MergeInsertSpecification, query_ValueExpressionCase, query_ValueExpressionNullValue, query_ValueExpressionDefaultValue, Function, QueryValueExpression, query_GroupingSets, GroupingSpecification, query_GroupingSetsElement, query_Grouping, query_GroupingSetsElementExpression, query_GroupingSetsElementSublist, GroupingSetsElement, query_SuperGroupElementSublist, SuperGroupElement, query_SuperGroup, Grouping, query_SuperGroupElement, query_SuperGroupElementExpression, query_ValueExpressionCaseSearch, ValueExpressionCase, Table, query_SQLQueryObject, SQLObject, query_QueryMergeStatement, query_QueryChangeStatement, statements_SQLDataChangeStatement, query_MergeOperationSpecification, query_OrderByOrdinal, query_ValueExpressionAtomic, UpdateSource, MergeOperationSpecification, query_UpdateOfColumn, Procedure, statements_SQLControlStatement, query_ProcedureReference, query_TableQueryLateral, SuperGroupType, SearchConditionCombinedOperator, TableJoinedOperator, QueryCombinedOperator, ValueExpressionUnaryOperator, PredicateQuantifiedType, PredicateComparisonOperator, ValueExpressionCombinedOperator, ValueExpressionLabeledDurationType, NullOrderingType, OrderingSpecType, UpdatabilityType},
    associations={sourceValuesRowList6, whereCurrentOfClause0, whereClause1, targetTable3, sourceQuery5, assignmentClause19, whereCurrentOfClause20, targetTable8, targetColumnList11, queryExpr13, orderByClause15, updatabilityExpr17, updateStatement34, whereClause23, targetTable26, updateStatement29, targetColumnList30, updateSource32, mergeUpdateSpec33, combinedRight45, deleteStatement36, updateStatement38, deleteStatement40, tableJoined43, combinedLeft44, queryExpression55, querySelectHaving47, querySelectWhere48, valueExprCaseSearchContent51, nest52, mergeOnCondition53, combinedLeft57, combinedRight58, predicateExists60, updateSourceQuery61, withTableSpecification63, queryNest64, sortSpecList65, likeMatching78, dataType68, valuesRow69, orderByValueExpr71, resultColumn72, basicRight74, basicLeft75, likePattern77, betweenLeft94, predicateNull80, inValueListRight82, inValueListLeft83, inValueRowSelectLeft86, inValueSelectLeft88, quantifiedRowSelectLeft90, quantifiedValueSelectLeft92, groupingExpr108, betweenRight196, betweenRight298, valueExprCast100, valueExprFunction102, valueExprCombinedLeft103, valueExprCombinedRight105, valueExprLabeledDuration122, valueExprCaseElse110, valueExprCaseSimple112, valueExprCaseSimpleContentWhen114, valueExprCaseSimpleContentResult115, valueExprCaseSearchContent117, likeEscape120, insertStatement132, nest124, updateSourceExprList125, tableFunction127, valueExprRow129, callStatement131, valExprScalarSelect150, selectStatement133, withClause135, query137, inValueRowSelectRight138, inValueSelectRight141, quantifiedRowSelectRight144, quantifiedValueSelectRight147, tableJoinedRight158, insertStatement152, exprList154, queryValues155, valuesRowList156, valueExprColumns171, tableJoinedLeft160, querySelect162, nest164, mergeSourceTable165, columnList166, tableCorrelation168, resultTableAllColumns169, mergeTargetTable174, joinCondition176, tableRefRight178, tableRefLeft179, queryExpressionRoot181, leftCondition189, withTableQueryExpr183, withTableReferences185, columnNameList187, rightCondition191, valueExpr193, leftQuery195, rightQuery198, querySelect213, havingClause201, whereClause203, groupByClause205, selectClause206, fromClause208, intoClause211, rightValueExpr221, querySelect215, tableExpr217, valueExpr218, orderByResultCol220, leftValueExpr223, leftValueExpr225, rightValueExpr1227, rightValueExpr2229, queryExpr231, patternValueExpr233, matchingValueExpr235, escapeValueExpr237, valueExprList247, valueExpr239, queryExpr241, valueExpr243, queryExpr245, valueExprList257, queryExpr249, valueExpr251, valueExprList253, valueExpr255, tableInDatabase270, queryExpr259, assignmentExprTarget261, parentTableExpr263, insertStatement265, tableExpr268, caseElse280, mergeInsertSpec272, querySelect274, queryExpr276, valueExpr278, leftValueExpr287, valueExpr282, parameterList284, function286, groupingSetsElementExprList294, rightValueExpr289, groupingSetsElementList291, groupingSetsElementExpr292, groupingSets293, superGroup303, groupingSetsElementSublist296, grouping297, superGroupElementList298, valueExpr299, superGroupElementExpr301, valueExprCase316, superGroupElementExprList304, valueExpr317, superGroupElementSublist306, groupingExpr307, valueExpr319, searchContentList309, contentList311, valueExpr313, valueExprCaseSimple325, whenValueExpr327, resultValueExpr329, searchCondition321, valueExprCaseSearch324, updateStatement331, deleteStatement333, insertStatement336, databaseTable339, function342, parameterList344, derivedColumnList340, withTableSpecification348, nestedTableRef351, targetTable353, tableCorrelation346, operationSpecList361, nestedCondition363, nestedValueExpr366, sourceTable355, onCondition358, selectStatement369, query371, updateAssignmentExpr378, valueExprList380, tableExpr373, columnNameList375, withTableSpecification386, queryExpr382, resultCol384, nestedQuery388, valueExprList390, tableRef399, mergeStatement392, tableExpr394, QueryMergeStatement396, mergeStatement397, targetColumnList407, mergeStatement401, searchCondition403, assignementExprList405, updateOfColumnList414, sourceValuesRow409, mergeStatement410, updatabilityExpr412, procedure424, selectStatement415, argumentList418, procedureRef420, callStatement422, query425},
    generalizations={gen_query_QueryDeleteStatement_QueryChangeStatement, gen_query_QueryStatement_SQLQueryObject, gen_query_QueryStatement_statements_SQLDataStatement, gen_query_QueryInsertStatement_QueryChangeStatement, gen_query_QuerySelectStatement_QueryStatement, gen_query_QueryUpdateStatement_QueryChangeStatement, gen_query_CursorReference_SQLQueryObject, gen_query_UpdateAssignmentExpression_SQLQueryObject, gen_query_QuerySearchCondition_SQLQueryObject, gen_query_QuerySearchCondition_expressions_SearchCondition, gen_query_QueryExpressionBody_TableExpression, gen_query_QueryValueExpression_SQLQueryObject, gen_query_QueryValueExpression_expressions_ValueExpression, gen_query_QueryExpressionRoot_expressions_QueryExpression, gen_query_QueryExpressionRoot_SQLQueryObject, gen_query_ValuesRow_SQLQueryObject, gen_query_QueryValues_QueryExpressionBody, gen_query_TableReference_SQLQueryObject, gen_query_TableExpression_TableReference, gen_query_TableJoined_TableReference, gen_query_WithTableSpecification_SQLQueryObject, gen_query_Predicate_QuerySearchCondition, gen_query_SearchConditionCombined_QuerySearchCondition, gen_query_QuerySelect_QueryExpressionBody, gen_query_OrderByValueExpression_OrderBySpecification, gen_query_QueryCombined_QueryExpressionBody, gen_query_QueryResultSpecification_SQLQueryObject, gen_query_GroupingSpecification_SQLQueryObject, gen_query_ResultTableAllColumns_QueryResultSpecification, gen_query_ResultColumn_QueryResultSpecification, gen_query_PredicateBasic_Predicate, gen_query_PredicateExists_Predicate, gen_query_PredicateQuantified_Predicate, gen_query_PredicateBetween_Predicate, gen_query_PredicateIsNull_Predicate, gen_query_PredicateIn_Predicate, gen_query_PredicateLike_Predicate, gen_query_PredicateQuantifiedValueSelect_PredicateQuantified, gen_query_PredicateQuantifiedRowSelect_PredicateQuantified, gen_query_PredicateInValueSelect_PredicateIn, gen_query_PredicateInValueList_PredicateIn, gen_query_PredicateInValueRowSelect_PredicateIn, gen_query_ValueExpressionSimple_ValueExpressionAtomic, gen_query_ValueExpressionColumn_ValueExpressionAtomic, gen_query_ValueExpressionCase_ValueExpressionAtomic, gen_query_ValueExpressionVariable_ValueExpressionAtomic, gen_query_ValueExpressionScalarSelect_ValueExpressionAtomic, gen_query_ValueExpressionLabeledDuration_ValueExpressionAtomic, gen_query_ValueExpressionCast_ValueExpressionAtomic, gen_query_ValueExpressionNullValue_ValueExpressionAtomic, gen_query_ValueExpressionDefaultValue_ValueExpressionAtomic, gen_query_ValueExpressionFunction_ValueExpressionAtomic, gen_query_ValueExpressionCombined_QueryValueExpression, gen_query_GroupingSetsElementExpression_GroupingSetsElement, gen_query_GroupingSets_GroupingSpecification, gen_query_Grouping_GroupingSpecification, gen_query_GroupingSetsElement_SQLQueryObject, gen_query_GroupingSetsElementSublist_GroupingSetsElement, gen_query_SuperGroupElementSublist_SuperGroupElement, gen_query_SuperGroup_Grouping, gen_query_GroupingExpression_Grouping, gen_query_SuperGroupElement_SQLQueryObject, gen_query_ValueExpressionCaseElse_SQLQueryObject, gen_query_SuperGroupElementExpression_SuperGroupElement, gen_query_ValueExpressionCaseSearchContent_SQLQueryObject, gen_query_ValueExpressionCaseSearch_ValueExpressionCase, gen_query_ValueExpressionCaseSimple_ValueExpressionCase, gen_query_ValueExpressionCaseSimpleContent_SQLQueryObject, gen_query_TableInDatabase_TableExpression, gen_query_SQLQueryObject_SQLObject, gen_query_TableFunction_TableExpression, gen_query_TableNested_TableReference, gen_query_QueryMergeStatement_QueryChangeStatement, gen_query_QueryChangeStatement_QueryStatement, gen_query_QueryChangeStatement_statements_SQLDataChangeStatement, gen_query_ColumnName_SQLQueryObject, gen_query_SearchConditionNested_QuerySearchCondition, gen_query_ValueExpressionNested_QueryValueExpression, gen_query_OrderByOrdinal_OrderBySpecification, gen_query_TableCorrelation_SQLQueryObject, gen_query_ValueExpressionAtomic_QueryValueExpression, gen_query_OrderBySpecification_SQLQueryObject, gen_query_UpdateSource_SQLQueryObject, gen_query_UpdateSourceExprList_UpdateSource, gen_query_UpdateSourceQuery_UpdateSource, gen_query_WithTableReference_TableExpression, gen_query_MergeTargetTable_SQLQueryObject, gen_query_OrderByResultColumn_OrderBySpecification, gen_query_QueryNested_QueryExpressionBody, gen_query_ValueExpressionRow_QueryValueExpression, gen_query_MergeOnCondition_SQLQueryObject, gen_query_MergeSourceTable_SQLQueryObject, gen_query_MergeUpdateSpecification_MergeOperationSpecification, gen_query_MergeInsertSpecification_MergeOperationSpecification, gen_query_MergeOperationSpecification_SQLQueryObject, gen_query_UpdateOfColumn_SQLQueryObject, gen_query_UpdatabilityExpression_SQLQueryObject, gen_query_CallStatement_SQLQueryObject, gen_query_CallStatement_statements_SQLControlStatement, gen_query_ProcedureReference_SQLQueryObject, gen_query_TableQueryLateral_TableExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
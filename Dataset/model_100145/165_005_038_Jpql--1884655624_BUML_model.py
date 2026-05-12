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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="lessThen"),
			EnumerationLiteral(name="greaterThen"),
			EnumerationLiteral(name="lessEqual"),
			EnumerationLiteral(name="greaterEqual"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notEqual")
    }
)

# Classes
jpql_JPQLQuery = Class(name="jpql_JPQLQuery")
jpql_NamedQuery = Class(name="jpql_NamedQuery")
jpql_WhereClause = Class(name="jpql_WhereClause")
jpql_SelectStatement = Class(name="jpql_SelectStatement")
JPQLQuery = Class(name="JPQLQuery")
ExpressionTerm = Class(name="ExpressionTerm")
jpql_SelectFromClause = Class(name="jpql_SelectFromClause")
jpql_HavingClause = Class(name="jpql_HavingClause")
jpql_OrderClause = Class(name="jpql_OrderClause")
jpql_QueryModule = Class(name="jpql_QueryModule")
jpql_Import = Class(name="jpql_Import")
jpql_UpdateItem = Class(name="jpql_UpdateItem")
jpql_AliasAttributeExpression = Class(name="jpql_AliasAttributeExpression")
jpql_Value = Class(name="jpql_Value")
jpql_DeleteStatement = Class(name="jpql_DeleteStatement")
jpql_DeleteClause = Class(name="jpql_DeleteClause")
jpql_FromClause = Class(name="jpql_FromClause")
jpql_SelectClause = Class(name="jpql_SelectClause")
jpql_Expression = Class(name="jpql_Expression")
jpql_OrderItem = Class(name="jpql_OrderItem")
jpql_FromEntry = Class(name="jpql_FromEntry")
jpql_UpdateStatement = Class(name="jpql_UpdateStatement")
jpql_UpdateClause = Class(name="jpql_UpdateClause")
jpql_SetClause = Class(name="jpql_SetClause")
jpql_VariableDeclaration = Class(name="jpql_VariableDeclaration")
jpql_FromClass = Class(name="jpql_FromClass")
FromEntry = Class(name="FromEntry")
jpql_FromJoin = Class(name="jpql_FromJoin")
jpql_FromCollection = Class(name="jpql_FromCollection")
jpql_SelectExpression = Class(name="jpql_SelectExpression")
jpql_SelectAggregateExpression = Class(name="jpql_SelectAggregateExpression")
SelectExpression = Class(name="SelectExpression")
jpql_AvgAggregate = Class(name="jpql_AvgAggregate")
SelectAggregateExpression = Class(name="SelectAggregateExpression")
jpql_MaxAggregate = Class(name="jpql_MaxAggregate")
jpql_MinAggregate = Class(name="jpql_MinAggregate")
jpql_SumAggregate = Class(name="jpql_SumAggregate")
jpql_CountAggregate = Class(name="jpql_CountAggregate")
jpql_SelectConstructorExpression = Class(name="jpql_SelectConstructorExpression")
jpql_ExistsExpression = Class(name="jpql_ExistsExpression")
jpql_AllExpression = Class(name="jpql_AllExpression")
jpql_AnyExpression = Class(name="jpql_AnyExpression")
jpql_SomeExpression = Class(name="jpql_SomeExpression")
jpql_CollectionExpression = Class(name="jpql_CollectionExpression")
jpql_NullComparisonExpression = Class(name="jpql_NullComparisonExpression")
jpql_Join = Class(name="jpql_Join")
FromJoin = Class(name="FromJoin")
jpql_LeftJoin = Class(name="jpql_LeftJoin")
jpql_InnerJoin = Class(name="jpql_InnerJoin")
jpql_OperatorExpression = Class(name="jpql_OperatorExpression")
Expression = Class(name="Expression")
jpql_Variable = Class(name="jpql_Variable")
jpql_ExpressionTerm = Class(name="jpql_ExpressionTerm")
jpql_InSeqExpression = Class(name="jpql_InSeqExpression")
InExpression = Class(name="InExpression")
jpql_InQueryExpression = Class(name="jpql_InQueryExpression")
jpql_BetweenExpression = Class(name="jpql_BetweenExpression")
Variable = Class(name="Variable")
jpql_EmptyComparisonExpression = Class(name="jpql_EmptyComparisonExpression")
jpql_LikeExpression = Class(name="jpql_LikeExpression")
jpql_InExpression = Class(name="jpql_InExpression")
jpql_DateTimeExpression = Class(name="jpql_DateTimeExpression")
jpql_OrExpression = Class(name="jpql_OrExpression")
jpql_AndExpression = Class(name="jpql_AndExpression")
jpql_ParameterExpression = Class(name="jpql_ParameterExpression")
jpql_Function = Class(name="jpql_Function")
jpql_IntegerExpression = Class(name="jpql_IntegerExpression")
Value = Class(name="Value")
jpql_StringExpression = Class(name="jpql_StringExpression")
jpql_NullExpression = Class(name="jpql_NullExpression")
jpql_BooleanExpression = Class(name="jpql_BooleanExpression")

# jpql_JPQLQuery class attributes and methods

# jpql_NamedQuery class attributes and methods
jpql_NamedQuery_name: Property = Property(name="name", type=StringType)
jpql_NamedQuery.attributes={jpql_NamedQuery_name}

# jpql_WhereClause class attributes and methods

# jpql_SelectStatement class attributes and methods

# JPQLQuery class attributes and methods

# ExpressionTerm class attributes and methods

# jpql_SelectFromClause class attributes and methods

# jpql_HavingClause class attributes and methods

# jpql_OrderClause class attributes and methods
jpql_OrderClause_isAsc: Property = Property(name="isAsc", type=BooleanType)
jpql_OrderClause_isDesc: Property = Property(name="isDesc", type=BooleanType)
jpql_OrderClause.attributes={jpql_OrderClause_isDesc, jpql_OrderClause_isAsc}

# jpql_QueryModule class attributes and methods

# jpql_Import class attributes and methods
jpql_Import_importURI: Property = Property(name="importURI", type=StringType)
jpql_Import.attributes={jpql_Import_importURI}

# jpql_UpdateItem class attributes and methods

# jpql_AliasAttributeExpression class attributes and methods
jpql_AliasAttributeExpression_attributes: Property = Property(name="attributes", type=StringType)
jpql_AliasAttributeExpression.attributes={jpql_AliasAttributeExpression_attributes}

# jpql_Value class attributes and methods

# jpql_DeleteStatement class attributes and methods

# jpql_DeleteClause class attributes and methods

# jpql_FromClause class attributes and methods

# jpql_SelectClause class attributes and methods
jpql_SelectClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jpql_SelectClause.attributes={jpql_SelectClause_isDistinct}

# jpql_Expression class attributes and methods

# jpql_OrderItem class attributes and methods
jpql_OrderItem_feature: Property = Property(name="feature", type=StringType)
jpql_OrderItem.attributes={jpql_OrderItem_feature}

# jpql_FromEntry class attributes and methods

# jpql_UpdateStatement class attributes and methods

# jpql_UpdateClause class attributes and methods

# jpql_SetClause class attributes and methods

# jpql_VariableDeclaration class attributes and methods
jpql_VariableDeclaration_name: Property = Property(name="name", type=StringType)
jpql_VariableDeclaration.attributes={jpql_VariableDeclaration_name}

# jpql_FromClass class attributes and methods
jpql_FromClass_type: Property = Property(name="type", type=StringType)
jpql_FromClass.attributes={jpql_FromClass_type}

# FromEntry class attributes and methods

# jpql_FromJoin class attributes and methods
jpql_FromJoin_isFetch: Property = Property(name="isFetch", type=BooleanType)
jpql_FromJoin.attributes={jpql_FromJoin_isFetch}

# jpql_FromCollection class attributes and methods

# jpql_SelectExpression class attributes and methods

# jpql_SelectAggregateExpression class attributes and methods
jpql_SelectAggregateExpression_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jpql_SelectAggregateExpression.attributes={jpql_SelectAggregateExpression_isDistinct}

# SelectExpression class attributes and methods

# jpql_AvgAggregate class attributes and methods

# SelectAggregateExpression class attributes and methods

# jpql_MaxAggregate class attributes and methods

# jpql_MinAggregate class attributes and methods

# jpql_SumAggregate class attributes and methods

# jpql_CountAggregate class attributes and methods

# jpql_SelectConstructorExpression class attributes and methods
jpql_SelectConstructorExpression_name: Property = Property(name="name", type=StringType)
jpql_SelectConstructorExpression.attributes={jpql_SelectConstructorExpression_name}

# jpql_ExistsExpression class attributes and methods
jpql_ExistsExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_ExistsExpression.attributes={jpql_ExistsExpression_isNot}

# jpql_AllExpression class attributes and methods

# jpql_AnyExpression class attributes and methods

# jpql_SomeExpression class attributes and methods

# jpql_CollectionExpression class attributes and methods
jpql_CollectionExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_CollectionExpression.attributes={jpql_CollectionExpression_isNot}

# jpql_NullComparisonExpression class attributes and methods
jpql_NullComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_NullComparisonExpression.attributes={jpql_NullComparisonExpression_isNot}

# jpql_Join class attributes and methods

# FromJoin class attributes and methods

# jpql_LeftJoin class attributes and methods
jpql_LeftJoin_isOuter: Property = Property(name="isOuter", type=BooleanType)
jpql_LeftJoin.attributes={jpql_LeftJoin_isOuter}

# jpql_InnerJoin class attributes and methods

# jpql_OperatorExpression class attributes and methods
jpql_OperatorExpression_operator: Property = Property(name="operator", type=StringType)
jpql_OperatorExpression.attributes={jpql_OperatorExpression_operator}

# Expression class attributes and methods

# jpql_Variable class attributes and methods

# jpql_ExpressionTerm class attributes and methods

# jpql_InSeqExpression class attributes and methods

# InExpression class attributes and methods

# jpql_InQueryExpression class attributes and methods

# jpql_BetweenExpression class attributes and methods
jpql_BetweenExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_BetweenExpression.attributes={jpql_BetweenExpression_isNot}

# Variable class attributes and methods

# jpql_EmptyComparisonExpression class attributes and methods
jpql_EmptyComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_EmptyComparisonExpression.attributes={jpql_EmptyComparisonExpression_isNot}

# jpql_LikeExpression class attributes and methods
jpql_LikeExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_LikeExpression_pattern: Property = Property(name="pattern", type=StringType)
jpql_LikeExpression.attributes={jpql_LikeExpression_pattern, jpql_LikeExpression_isNot}

# jpql_InExpression class attributes and methods
jpql_InExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jpql_InExpression.attributes={jpql_InExpression_isNot}

# jpql_DateTimeExpression class attributes and methods
jpql_DateTimeExpression_value: Property = Property(name="value", type=StringType)
jpql_DateTimeExpression.attributes={jpql_DateTimeExpression_value}

# jpql_OrExpression class attributes and methods

# jpql_AndExpression class attributes and methods

# jpql_ParameterExpression class attributes and methods
jpql_ParameterExpression_name: Property = Property(name="name", type=StringType)
jpql_ParameterExpression.attributes={jpql_ParameterExpression_name}

# jpql_Function class attributes and methods
jpql_Function_name: Property = Property(name="name", type=StringType)
jpql_Function.attributes={jpql_Function_name}

# jpql_IntegerExpression class attributes and methods
jpql_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
jpql_IntegerExpression.attributes={jpql_IntegerExpression_value}

# Value class attributes and methods

# jpql_StringExpression class attributes and methods
jpql_StringExpression_value: Property = Property(name="value", type=StringType)
jpql_StringExpression.attributes={jpql_StringExpression_value}

# jpql_NullExpression class attributes and methods
jpql_NullExpression_value: Property = Property(name="value", type=StringType)
jpql_NullExpression.attributes={jpql_NullExpression_value}

# jpql_BooleanExpression class attributes and methods
jpql_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
jpql_BooleanExpression.attributes={jpql_BooleanExpression_value}

# Relationships
defaultQuery1: BinaryAssociation = BinaryAssociation(
    name="defaultQuery1",
    ends={
        Property(name="jpql_JPQLQuery", type=jpql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_QueryModule2", type=jpql_JPQLQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedQueries3: BinaryAssociation = BinaryAssociation(
    name="namedQueries3",
    ends={
        Property(name="jpql_NamedQuery", type=jpql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_QueryModule4", type=jpql_NamedQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query5: BinaryAssociation = BinaryAssociation(
    name="query5",
    ends={
        Property(name="jpql_JPQLQuery7", type=jpql_NamedQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_NamedQuery6", type=jpql_JPQLQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause8: BinaryAssociation = BinaryAssociation(
    name="whereClause8",
    ends={
        Property(name="jpql_WhereClause", type=jpql_JPQLQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_JPQLQuery9", type=jpql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectFromClause10: BinaryAssociation = BinaryAssociation(
    name="selectFromClause10",
    ends={
        Property(name="jpql_SelectFromClause", type=jpql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectStatement", type=jpql_SelectFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having11: BinaryAssociation = BinaryAssociation(
    name="having11",
    ends={
        Property(name="jpql_HavingClause", type=jpql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectStatement12", type=jpql_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
order13: BinaryAssociation = BinaryAssociation(
    name="order13",
    ends={
        Property(name="jpql_OrderClause", type=jpql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectStatement14", type=jpql_OrderClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="jpql_Import", type=jpql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_QueryModule", type=jpql_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromEntries24: BinaryAssociation = BinaryAssociation(
    name="fromEntries24",
    ends={
        Property(name="jpql_FromEntry26", type=jpql_UpdateClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_UpdateClause25", type=jpql_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items27: BinaryAssociation = BinaryAssociation(
    name="items27",
    ends={
        Property(name="jpql_UpdateItem", type=jpql_SetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SetClause28", type=jpql_UpdateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias29: BinaryAssociation = BinaryAssociation(
    name="alias29",
    ends={
        Property(name="jpql_AliasAttributeExpression", type=jpql_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_UpdateItem30", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="jpql_Value", type=jpql_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_UpdateItem32", type=jpql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteClause33: BinaryAssociation = BinaryAssociation(
    name="deleteClause33",
    ends={
        Property(name="jpql_DeleteClause", type=jpql_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_DeleteStatement", type=jpql_DeleteClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause34: BinaryAssociation = BinaryAssociation(
    name="fromClause34",
    ends={
        Property(name="jpql_FromClause", type=jpql_DeleteClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_DeleteClause35", type=jpql_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectClause36: BinaryAssociation = BinaryAssociation(
    name="selectClause36",
    ends={
        Property(name="jpql_SelectClause", type=jpql_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectFromClause37", type=jpql_SelectClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause38: BinaryAssociation = BinaryAssociation(
    name="fromClause38",
    ends={
        Property(name="jpql_FromClause40", type=jpql_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectFromClause39", type=jpql_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having15: BinaryAssociation = BinaryAssociation(
    name="having15",
    ends={
        Property(name="jpql_Expression", type=jpql_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_HavingClause16", type=jpql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering17: BinaryAssociation = BinaryAssociation(
    name="ordering17",
    ends={
        Property(name="jpql_OrderItem", type=jpql_OrderClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_OrderClause18", type=jpql_OrderItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var19: BinaryAssociation = BinaryAssociation(
    name="var19",
    ends={
        Property(name="jpql_FromEntry", type=jpql_OrderItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_OrderItem20", type=jpql_FromEntry, multiplicity=Multiplicity(0, 1))
    }
)
updateClause21: BinaryAssociation = BinaryAssociation(
    name="updateClause21",
    ends={
        Property(name="jpql_UpdateClause", type=jpql_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_UpdateStatement", type=jpql_UpdateClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setClause22: BinaryAssociation = BinaryAssociation(
    name="setClause22",
    ends={
        Property(name="jpql_SetClause", type=jpql_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_UpdateStatement23", type=jpql_SetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items45: BinaryAssociation = BinaryAssociation(
    name="items45",
    ends={
        Property(name="jpql_AliasAttributeExpression46", type=jpql_SelectConstructorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectConstructorExpression", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromEntries47: BinaryAssociation = BinaryAssociation(
    name="fromEntries47",
    ends={
        Property(name="jpql_FromEntry49", type=jpql_FromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromClause48", type=jpql_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable50: BinaryAssociation = BinaryAssociation(
    name="variable50",
    ends={
        Property(name="jpql_VariableDeclaration", type=jpql_FromEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromEntry51", type=jpql_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joins52: BinaryAssociation = BinaryAssociation(
    name="joins52",
    ends={
        Property(name="jpql_FromJoin", type=jpql_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromClass", type=jpql_FromJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path53: BinaryAssociation = BinaryAssociation(
    name="path53",
    ends={
        Property(name="jpql_AliasAttributeExpression54", type=jpql_FromCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromCollection", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path55: BinaryAssociation = BinaryAssociation(
    name="path55",
    ends={
        Property(name="jpql_AliasAttributeExpression57", type=jpql_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromJoin56", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable58: BinaryAssociation = BinaryAssociation(
    name="variable58",
    ends={
        Property(name="jpql_VariableDeclaration60", type=jpql_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_FromJoin59", type=jpql_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions41: BinaryAssociation = BinaryAssociation(
    name="expressions41",
    ends={
        Property(name="jpql_SelectExpression", type=jpql_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectClause42", type=jpql_SelectExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item43: BinaryAssociation = BinaryAssociation(
    name="item43",
    ends={
        Property(name="jpql_AliasAttributeExpression44", type=jpql_SelectAggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SelectAggregateExpression", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query67: BinaryAssociation = BinaryAssociation(
    name="query67",
    ends={
        Property(name="jpql_SelectStatement68", type=jpql_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_ExistsExpression", type=jpql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query69: BinaryAssociation = BinaryAssociation(
    name="query69",
    ends={
        Property(name="jpql_SelectStatement70", type=jpql_AllExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_AllExpression", type=jpql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query71: BinaryAssociation = BinaryAssociation(
    name="query71",
    ends={
        Property(name="jpql_SelectStatement72", type=jpql_AnyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_AnyExpression", type=jpql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query73: BinaryAssociation = BinaryAssociation(
    name="query73",
    ends={
        Property(name="jpql_SelectStatement74", type=jpql_SomeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_SomeExpression", type=jpql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs75: BinaryAssociation = BinaryAssociation(
    name="lhs75",
    ends={
        Property(name="jpql_Variable76", type=jpql_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_CollectionExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs77: BinaryAssociation = BinaryAssociation(
    name="rhs77",
    ends={
        Property(name="jpql_AliasAttributeExpression79", type=jpql_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_CollectionExpression78", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereEntry61: BinaryAssociation = BinaryAssociation(
    name="whereEntry61",
    ends={
        Property(name="jpql_Expression63", type=jpql_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_WhereClause62", type=jpql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs64: BinaryAssociation = BinaryAssociation(
    name="lhs64",
    ends={
        Property(name="jpql_Variable", type=jpql_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_OperatorExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs65: BinaryAssociation = BinaryAssociation(
    name="rhs65",
    ends={
        Property(name="jpql_ExpressionTerm", type=jpql_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_OperatorExpression66", type=jpql_ExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items88: BinaryAssociation = BinaryAssociation(
    name="items88",
    ends={
        Property(name="jpql_Variable89", type=jpql_InSeqExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_InSeqExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query90: BinaryAssociation = BinaryAssociation(
    name="query90",
    ends={
        Property(name="jpql_SelectStatement91", type=jpql_InQueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_InQueryExpression", type=jpql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs92: BinaryAssociation = BinaryAssociation(
    name="lhs92",
    ends={
        Property(name="jpql_Variable93", type=jpql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_BetweenExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
min94: BinaryAssociation = BinaryAssociation(
    name="min94",
    ends={
        Property(name="jpql_Value96", type=jpql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_BetweenExpression95", type=jpql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max97: BinaryAssociation = BinaryAssociation(
    name="max97",
    ends={
        Property(name="jpql_Value99", type=jpql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_BetweenExpression98", type=jpql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias100: BinaryAssociation = BinaryAssociation(
    name="alias100",
    ends={
        Property(name="jpql_VariableDeclaration102", type=jpql_AliasAttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_AliasAttributeExpression101", type=jpql_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
lhs80: BinaryAssociation = BinaryAssociation(
    name="lhs80",
    ends={
        Property(name="jpql_Variable81", type=jpql_NullComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_NullComparisonExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs82: BinaryAssociation = BinaryAssociation(
    name="lhs82",
    ends={
        Property(name="jpql_Variable83", type=jpql_EmptyComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_EmptyComparisonExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs84: BinaryAssociation = BinaryAssociation(
    name="lhs84",
    ends={
        Property(name="jpql_Variable85", type=jpql_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_LikeExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs86: BinaryAssociation = BinaryAssociation(
    name="lhs86",
    ends={
        Property(name="jpql_Variable87", type=jpql_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_InExpression", type=jpql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries105: BinaryAssociation = BinaryAssociation(
    name="entries105",
    ends={
        Property(name="jpql_Expression106", type=jpql_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_OrExpression", type=jpql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries107: BinaryAssociation = BinaryAssociation(
    name="entries107",
    ends={
        Property(name="jpql_Expression108", type=jpql_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_AndExpression", type=jpql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params103: BinaryAssociation = BinaryAssociation(
    name="params103",
    ends={
        Property(name="jpql_Variable104", type=jpql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="jpql_Function", type=jpql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jpql_SelectStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jpql_SelectStatement)
gen_jpql_SelectStatement_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jpql_SelectStatement)
gen_jpql_DeleteStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jpql_DeleteStatement)
gen_jpql_UpdateStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jpql_UpdateStatement)
gen_jpql_FromClass_FromEntry = Generalization(general=FromEntry, specific=jpql_FromClass)
gen_jpql_FromCollection_FromEntry = Generalization(general=FromEntry, specific=jpql_FromCollection)
gen_jpql_SelectAggregateExpression_SelectExpression = Generalization(general=SelectExpression, specific=jpql_SelectAggregateExpression)
gen_jpql_AvgAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jpql_AvgAggregate)
gen_jpql_MaxAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jpql_MaxAggregate)
gen_jpql_MinAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jpql_MinAggregate)
gen_jpql_SumAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jpql_SumAggregate)
gen_jpql_CountAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jpql_CountAggregate)
gen_jpql_SelectConstructorExpression_SelectExpression = Generalization(general=SelectExpression, specific=jpql_SelectConstructorExpression)
gen_jpql_ExistsExpression_Expression = Generalization(general=Expression, specific=jpql_ExistsExpression)
gen_jpql_AllExpression_Expression = Generalization(general=Expression, specific=jpql_AllExpression)
gen_jpql_AnyExpression_Expression = Generalization(general=Expression, specific=jpql_AnyExpression)
gen_jpql_SomeExpression_Expression = Generalization(general=Expression, specific=jpql_SomeExpression)
gen_jpql_CollectionExpression_Expression = Generalization(general=Expression, specific=jpql_CollectionExpression)
gen_jpql_NullComparisonExpression_Expression = Generalization(general=Expression, specific=jpql_NullComparisonExpression)
gen_jpql_Join_FromJoin = Generalization(general=FromJoin, specific=jpql_Join)
gen_jpql_LeftJoin_FromJoin = Generalization(general=FromJoin, specific=jpql_LeftJoin)
gen_jpql_InnerJoin_FromJoin = Generalization(general=FromJoin, specific=jpql_InnerJoin)
gen_jpql_OperatorExpression_Expression = Generalization(general=Expression, specific=jpql_OperatorExpression)
gen_jpql_InSeqExpression_InExpression = Generalization(general=InExpression, specific=jpql_InSeqExpression)
gen_jpql_InQueryExpression_InExpression = Generalization(general=InExpression, specific=jpql_InQueryExpression)
gen_jpql_BetweenExpression_Expression = Generalization(general=Expression, specific=jpql_BetweenExpression)
gen_jpql_Variable_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jpql_Variable)
gen_jpql_ExpressionTerm_Expression = Generalization(general=Expression, specific=jpql_ExpressionTerm)
gen_jpql_AliasAttributeExpression_SelectExpression = Generalization(general=SelectExpression, specific=jpql_AliasAttributeExpression)
gen_jpql_AliasAttributeExpression_Variable = Generalization(general=Variable, specific=jpql_AliasAttributeExpression)
gen_jpql_EmptyComparisonExpression_Expression = Generalization(general=Expression, specific=jpql_EmptyComparisonExpression)
gen_jpql_LikeExpression_Expression = Generalization(general=Expression, specific=jpql_LikeExpression)
gen_jpql_InExpression_Expression = Generalization(general=Expression, specific=jpql_InExpression)
gen_jpql_DateTimeExpression_Value = Generalization(general=Value, specific=jpql_DateTimeExpression)
gen_jpql_OrExpression_Expression = Generalization(general=Expression, specific=jpql_OrExpression)
gen_jpql_AndExpression_Expression = Generalization(general=Expression, specific=jpql_AndExpression)
gen_jpql_ParameterExpression_Variable = Generalization(general=Variable, specific=jpql_ParameterExpression)
gen_jpql_Value_Variable = Generalization(general=Variable, specific=jpql_Value)
gen_jpql_IntegerExpression_Value = Generalization(general=Value, specific=jpql_IntegerExpression)
gen_jpql_StringExpression_Value = Generalization(general=Value, specific=jpql_StringExpression)
gen_jpql_NullExpression_Value = Generalization(general=Value, specific=jpql_NullExpression)
gen_jpql_BooleanExpression_Value = Generalization(general=Value, specific=jpql_BooleanExpression)

# Domain Model
domain_model = DomainModel(
    name="jpql",
    types={jpql_JPQLQuery, jpql_NamedQuery, jpql_WhereClause, jpql_SelectStatement, JPQLQuery, ExpressionTerm, jpql_SelectFromClause, jpql_HavingClause, jpql_OrderClause, jpql_QueryModule, jpql_Import, jpql_UpdateItem, jpql_AliasAttributeExpression, jpql_Value, jpql_DeleteStatement, jpql_DeleteClause, jpql_FromClause, jpql_SelectClause, jpql_Expression, jpql_OrderItem, jpql_FromEntry, jpql_UpdateStatement, jpql_UpdateClause, jpql_SetClause, jpql_VariableDeclaration, jpql_FromClass, FromEntry, jpql_FromJoin, jpql_FromCollection, jpql_SelectExpression, jpql_SelectAggregateExpression, SelectExpression, jpql_AvgAggregate, SelectAggregateExpression, jpql_MaxAggregate, jpql_MinAggregate, jpql_SumAggregate, jpql_CountAggregate, jpql_SelectConstructorExpression, jpql_ExistsExpression, jpql_AllExpression, jpql_AnyExpression, jpql_SomeExpression, jpql_CollectionExpression, jpql_NullComparisonExpression, jpql_Join, FromJoin, jpql_LeftJoin, jpql_InnerJoin, jpql_OperatorExpression, Expression, jpql_Variable, jpql_ExpressionTerm, jpql_InSeqExpression, InExpression, jpql_InQueryExpression, jpql_BetweenExpression, Variable, jpql_EmptyComparisonExpression, jpql_LikeExpression, jpql_InExpression, jpql_DateTimeExpression, jpql_OrExpression, jpql_AndExpression, jpql_ParameterExpression, jpql_Function, jpql_IntegerExpression, Value, jpql_StringExpression, jpql_NullExpression, jpql_BooleanExpression, Operator},
    associations={defaultQuery1, namedQueries3, query5, whereClause8, selectFromClause10, having11, order13, imports0, fromEntries24, items27, alias29, value31, deleteClause33, fromClause34, selectClause36, fromClause38, having15, ordering17, var19, updateClause21, setClause22, items45, fromEntries47, variable50, joins52, path53, path55, variable58, expressions41, item43, query67, query69, query71, query73, lhs75, rhs77, whereEntry61, lhs64, rhs65, items88, query90, lhs92, min94, max97, alias100, lhs80, lhs82, lhs84, lhs86, entries105, entries107, params103},
    generalizations={gen_jpql_SelectStatement_JPQLQuery, gen_jpql_SelectStatement_ExpressionTerm, gen_jpql_DeleteStatement_JPQLQuery, gen_jpql_UpdateStatement_JPQLQuery, gen_jpql_FromClass_FromEntry, gen_jpql_FromCollection_FromEntry, gen_jpql_SelectAggregateExpression_SelectExpression, gen_jpql_AvgAggregate_SelectAggregateExpression, gen_jpql_MaxAggregate_SelectAggregateExpression, gen_jpql_MinAggregate_SelectAggregateExpression, gen_jpql_SumAggregate_SelectAggregateExpression, gen_jpql_CountAggregate_SelectAggregateExpression, gen_jpql_SelectConstructorExpression_SelectExpression, gen_jpql_ExistsExpression_Expression, gen_jpql_AllExpression_Expression, gen_jpql_AnyExpression_Expression, gen_jpql_SomeExpression_Expression, gen_jpql_CollectionExpression_Expression, gen_jpql_NullComparisonExpression_Expression, gen_jpql_Join_FromJoin, gen_jpql_LeftJoin_FromJoin, gen_jpql_InnerJoin_FromJoin, gen_jpql_OperatorExpression_Expression, gen_jpql_InSeqExpression_InExpression, gen_jpql_InQueryExpression_InExpression, gen_jpql_BetweenExpression_Expression, gen_jpql_Variable_ExpressionTerm, gen_jpql_ExpressionTerm_Expression, gen_jpql_AliasAttributeExpression_SelectExpression, gen_jpql_AliasAttributeExpression_Variable, gen_jpql_EmptyComparisonExpression_Expression, gen_jpql_LikeExpression_Expression, gen_jpql_InExpression_Expression, gen_jpql_DateTimeExpression_Value, gen_jpql_OrExpression_Expression, gen_jpql_AndExpression_Expression, gen_jpql_ParameterExpression_Variable, gen_jpql_Value_Variable, gen_jpql_IntegerExpression_Value, gen_jpql_StringExpression_Value, gen_jpql_NullExpression_Value, gen_jpql_BooleanExpression_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
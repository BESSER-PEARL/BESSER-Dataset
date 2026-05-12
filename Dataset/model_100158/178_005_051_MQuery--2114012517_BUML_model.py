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
mql_QueryModule = Class(name="mql_QueryModule")
mql_Import = Class(name="mql_Import")
mql_MQuery = Class(name="mql_MQuery")
mql_NamedQuery = Class(name="mql_NamedQuery")
mql_WhereClause = Class(name="mql_WhereClause")
mql_SelectStatement = Class(name="mql_SelectStatement")
MQuery = Class(name="MQuery")
ExpressionTerm = Class(name="ExpressionTerm")
mql_SelectFromClause = Class(name="mql_SelectFromClause")
mql_OrderItem = Class(name="mql_OrderItem")
mql_FromEntry = Class(name="mql_FromEntry")
mql_UpdateStatement = Class(name="mql_UpdateStatement")
mql_UpdateClause = Class(name="mql_UpdateClause")
mql_SetClause = Class(name="mql_SetClause")
mql_UpdateItem = Class(name="mql_UpdateItem")
mql_AliasAttributeExpression = Class(name="mql_AliasAttributeExpression")
mql_Value = Class(name="mql_Value")
mql_DeleteStatement = Class(name="mql_DeleteStatement")
mql_DeleteClause = Class(name="mql_DeleteClause")
mql_FromClause = Class(name="mql_FromClause")
mql_HavingClause = Class(name="mql_HavingClause")
mql_OrderClause = Class(name="mql_OrderClause")
mql_Expression = Class(name="mql_Expression")
mql_SelectExpression = Class(name="mql_SelectExpression")
mql_SelectAggregateExpression = Class(name="mql_SelectAggregateExpression")
SelectExpression = Class(name="SelectExpression")
mql_AvgAggregate = Class(name="mql_AvgAggregate")
SelectAggregateExpression = Class(name="SelectAggregateExpression")
mql_MaxAggregate = Class(name="mql_MaxAggregate")
mql_MinAggregate = Class(name="mql_MinAggregate")
mql_SumAggregate = Class(name="mql_SumAggregate")
mql_CountAggregate = Class(name="mql_CountAggregate")
mql_SelectConstructorExpression = Class(name="mql_SelectConstructorExpression")
mql_VariableDeclaration = Class(name="mql_VariableDeclaration")
mql_FromClass = Class(name="mql_FromClass")
FromEntry = Class(name="FromEntry")
mql_FromJoin = Class(name="mql_FromJoin")
mql_SelectClause = Class(name="mql_SelectClause")
mql_Join = Class(name="mql_Join")
FromJoin = Class(name="FromJoin")
mql_LeftJoin = Class(name="mql_LeftJoin")
mql_InnerJoin = Class(name="mql_InnerJoin")
mql_OperatorExpression = Class(name="mql_OperatorExpression")
Expression = Class(name="Expression")
mql_Variable = Class(name="mql_Variable")
mql_ExpressionTerm = Class(name="mql_ExpressionTerm")
mql_ExistsExpression = Class(name="mql_ExistsExpression")
mql_AllExpression = Class(name="mql_AllExpression")
mql_AnyExpression = Class(name="mql_AnyExpression")
mql_FromCollection = Class(name="mql_FromCollection")
mql_NullComparisonExpression = Class(name="mql_NullComparisonExpression")
mql_EmptyComparisonExpression = Class(name="mql_EmptyComparisonExpression")
mql_LikeExpression = Class(name="mql_LikeExpression")
mql_InExpression = Class(name="mql_InExpression")
mql_InSeqExpression = Class(name="mql_InSeqExpression")
InExpression = Class(name="InExpression")
mql_InQueryExpression = Class(name="mql_InQueryExpression")
mql_BetweenExpression = Class(name="mql_BetweenExpression")
mql_SomeExpression = Class(name="mql_SomeExpression")
mql_CollectionExpression = Class(name="mql_CollectionExpression")
Variable = Class(name="Variable")
mql_ParameterExpression = Class(name="mql_ParameterExpression")
mql_Function = Class(name="mql_Function")
mql_IntegerExpression = Class(name="mql_IntegerExpression")
Value = Class(name="Value")
mql_StringExpression = Class(name="mql_StringExpression")
mql_NullExpression = Class(name="mql_NullExpression")
mql_BooleanExpression = Class(name="mql_BooleanExpression")
mql_DateTimeExpression = Class(name="mql_DateTimeExpression")
mql_OrExpression = Class(name="mql_OrExpression")
mql_AndExpression = Class(name="mql_AndExpression")

# mql_QueryModule class attributes and methods

# mql_Import class attributes and methods
mql_Import_importURI: Property = Property(name="importURI", type=StringType)
mql_Import.attributes={mql_Import_importURI}

# mql_MQuery class attributes and methods

# mql_NamedQuery class attributes and methods
mql_NamedQuery_name: Property = Property(name="name", type=StringType)
mql_NamedQuery.attributes={mql_NamedQuery_name}

# mql_WhereClause class attributes and methods

# mql_SelectStatement class attributes and methods

# MQuery class attributes and methods

# ExpressionTerm class attributes and methods

# mql_SelectFromClause class attributes and methods

# mql_OrderItem class attributes and methods
mql_OrderItem_feature: Property = Property(name="feature", type=StringType)
mql_OrderItem.attributes={mql_OrderItem_feature}

# mql_FromEntry class attributes and methods

# mql_UpdateStatement class attributes and methods

# mql_UpdateClause class attributes and methods

# mql_SetClause class attributes and methods

# mql_UpdateItem class attributes and methods

# mql_AliasAttributeExpression class attributes and methods
mql_AliasAttributeExpression_attributes: Property = Property(name="attributes", type=StringType)
mql_AliasAttributeExpression.attributes={mql_AliasAttributeExpression_attributes}

# mql_Value class attributes and methods

# mql_DeleteStatement class attributes and methods

# mql_DeleteClause class attributes and methods

# mql_FromClause class attributes and methods

# mql_HavingClause class attributes and methods

# mql_OrderClause class attributes and methods
mql_OrderClause_isAsc: Property = Property(name="isAsc", type=BooleanType)
mql_OrderClause_isDesc: Property = Property(name="isDesc", type=BooleanType)
mql_OrderClause.attributes={mql_OrderClause_isAsc, mql_OrderClause_isDesc}

# mql_Expression class attributes and methods

# mql_SelectExpression class attributes and methods

# mql_SelectAggregateExpression class attributes and methods
mql_SelectAggregateExpression_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
mql_SelectAggregateExpression.attributes={mql_SelectAggregateExpression_isDistinct}

# SelectExpression class attributes and methods

# mql_AvgAggregate class attributes and methods

# SelectAggregateExpression class attributes and methods

# mql_MaxAggregate class attributes and methods

# mql_MinAggregate class attributes and methods

# mql_SumAggregate class attributes and methods

# mql_CountAggregate class attributes and methods

# mql_SelectConstructorExpression class attributes and methods
mql_SelectConstructorExpression_name: Property = Property(name="name", type=StringType)
mql_SelectConstructorExpression.attributes={mql_SelectConstructorExpression_name}

# mql_VariableDeclaration class attributes and methods
mql_VariableDeclaration_name: Property = Property(name="name", type=StringType)
mql_VariableDeclaration.attributes={mql_VariableDeclaration_name}

# mql_FromClass class attributes and methods
mql_FromClass_type: Property = Property(name="type", type=StringType)
mql_FromClass.attributes={mql_FromClass_type}

# FromEntry class attributes and methods

# mql_FromJoin class attributes and methods
mql_FromJoin_isFetch: Property = Property(name="isFetch", type=BooleanType)
mql_FromJoin.attributes={mql_FromJoin_isFetch}

# mql_SelectClause class attributes and methods
mql_SelectClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
mql_SelectClause.attributes={mql_SelectClause_isDistinct}

# mql_Join class attributes and methods

# FromJoin class attributes and methods

# mql_LeftJoin class attributes and methods
mql_LeftJoin_isOuter: Property = Property(name="isOuter", type=BooleanType)
mql_LeftJoin.attributes={mql_LeftJoin_isOuter}

# mql_InnerJoin class attributes and methods

# mql_OperatorExpression class attributes and methods
mql_OperatorExpression_operator: Property = Property(name="operator", type=StringType)
mql_OperatorExpression.attributes={mql_OperatorExpression_operator}

# Expression class attributes and methods

# mql_Variable class attributes and methods

# mql_ExpressionTerm class attributes and methods

# mql_ExistsExpression class attributes and methods
mql_ExistsExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_ExistsExpression.attributes={mql_ExistsExpression_isNot}

# mql_AllExpression class attributes and methods

# mql_AnyExpression class attributes and methods

# mql_FromCollection class attributes and methods

# mql_NullComparisonExpression class attributes and methods
mql_NullComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_NullComparisonExpression.attributes={mql_NullComparisonExpression_isNot}

# mql_EmptyComparisonExpression class attributes and methods
mql_EmptyComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_EmptyComparisonExpression.attributes={mql_EmptyComparisonExpression_isNot}

# mql_LikeExpression class attributes and methods
mql_LikeExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_LikeExpression_pattern: Property = Property(name="pattern", type=StringType)
mql_LikeExpression.attributes={mql_LikeExpression_isNot, mql_LikeExpression_pattern}

# mql_InExpression class attributes and methods
mql_InExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_InExpression.attributes={mql_InExpression_isNot}

# mql_InSeqExpression class attributes and methods

# InExpression class attributes and methods

# mql_InQueryExpression class attributes and methods

# mql_BetweenExpression class attributes and methods
mql_BetweenExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_BetweenExpression.attributes={mql_BetweenExpression_isNot}

# mql_SomeExpression class attributes and methods

# mql_CollectionExpression class attributes and methods
mql_CollectionExpression_isNot: Property = Property(name="isNot", type=BooleanType)
mql_CollectionExpression.attributes={mql_CollectionExpression_isNot}

# Variable class attributes and methods

# mql_ParameterExpression class attributes and methods
mql_ParameterExpression_name: Property = Property(name="name", type=StringType)
mql_ParameterExpression.attributes={mql_ParameterExpression_name}

# mql_Function class attributes and methods
mql_Function_name: Property = Property(name="name", type=StringType)
mql_Function.attributes={mql_Function_name}

# mql_IntegerExpression class attributes and methods
mql_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
mql_IntegerExpression.attributes={mql_IntegerExpression_value}

# Value class attributes and methods

# mql_StringExpression class attributes and methods
mql_StringExpression_value: Property = Property(name="value", type=StringType)
mql_StringExpression.attributes={mql_StringExpression_value}

# mql_NullExpression class attributes and methods
mql_NullExpression_value: Property = Property(name="value", type=StringType)
mql_NullExpression.attributes={mql_NullExpression_value}

# mql_BooleanExpression class attributes and methods
mql_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
mql_BooleanExpression.attributes={mql_BooleanExpression_value}

# mql_DateTimeExpression class attributes and methods
mql_DateTimeExpression_value: Property = Property(name="value", type=StringType)
mql_DateTimeExpression.attributes={mql_DateTimeExpression_value}

# mql_OrExpression class attributes and methods

# mql_AndExpression class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="mql_Import", type=mql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_QueryModule", type=mql_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultQuery1: BinaryAssociation = BinaryAssociation(
    name="defaultQuery1",
    ends={
        Property(name="mql_MQuery", type=mql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_QueryModule2", type=mql_MQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedQueries3: BinaryAssociation = BinaryAssociation(
    name="namedQueries3",
    ends={
        Property(name="mql_NamedQuery", type=mql_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_QueryModule4", type=mql_NamedQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query5: BinaryAssociation = BinaryAssociation(
    name="query5",
    ends={
        Property(name="mql_MQuery7", type=mql_NamedQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_NamedQuery6", type=mql_MQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause8: BinaryAssociation = BinaryAssociation(
    name="whereClause8",
    ends={
        Property(name="mql_WhereClause", type=mql_MQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_MQuery9", type=mql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectFromClause10: BinaryAssociation = BinaryAssociation(
    name="selectFromClause10",
    ends={
        Property(name="mql_SelectFromClause", type=mql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectStatement", type=mql_SelectFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering17: BinaryAssociation = BinaryAssociation(
    name="ordering17",
    ends={
        Property(name="mql_OrderItem", type=mql_OrderClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_OrderClause18", type=mql_OrderItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var19: BinaryAssociation = BinaryAssociation(
    name="var19",
    ends={
        Property(name="mql_FromEntry", type=mql_OrderItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_OrderItem20", type=mql_FromEntry, multiplicity=Multiplicity(0, 1))
    }
)
updateClause21: BinaryAssociation = BinaryAssociation(
    name="updateClause21",
    ends={
        Property(name="mql_UpdateClause", type=mql_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_UpdateStatement", type=mql_UpdateClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setClause22: BinaryAssociation = BinaryAssociation(
    name="setClause22",
    ends={
        Property(name="mql_SetClause", type=mql_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_UpdateStatement23", type=mql_SetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromEntries24: BinaryAssociation = BinaryAssociation(
    name="fromEntries24",
    ends={
        Property(name="mql_FromEntry26", type=mql_UpdateClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_UpdateClause25", type=mql_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items27: BinaryAssociation = BinaryAssociation(
    name="items27",
    ends={
        Property(name="mql_UpdateItem", type=mql_SetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SetClause28", type=mql_UpdateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias29: BinaryAssociation = BinaryAssociation(
    name="alias29",
    ends={
        Property(name="mql_AliasAttributeExpression", type=mql_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_UpdateItem30", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="mql_Value", type=mql_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_UpdateItem32", type=mql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteClause33: BinaryAssociation = BinaryAssociation(
    name="deleteClause33",
    ends={
        Property(name="mql_DeleteClause", type=mql_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_DeleteStatement", type=mql_DeleteClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having11: BinaryAssociation = BinaryAssociation(
    name="having11",
    ends={
        Property(name="mql_HavingClause", type=mql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectStatement12", type=mql_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
order13: BinaryAssociation = BinaryAssociation(
    name="order13",
    ends={
        Property(name="mql_OrderClause", type=mql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectStatement14", type=mql_OrderClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having15: BinaryAssociation = BinaryAssociation(
    name="having15",
    ends={
        Property(name="mql_Expression", type=mql_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_HavingClause16", type=mql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions41: BinaryAssociation = BinaryAssociation(
    name="expressions41",
    ends={
        Property(name="mql_SelectExpression", type=mql_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectClause42", type=mql_SelectExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item43: BinaryAssociation = BinaryAssociation(
    name="item43",
    ends={
        Property(name="mql_AliasAttributeExpression44", type=mql_SelectAggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectAggregateExpression", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items45: BinaryAssociation = BinaryAssociation(
    name="items45",
    ends={
        Property(name="mql_AliasAttributeExpression46", type=mql_SelectConstructorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectConstructorExpression", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromEntries47: BinaryAssociation = BinaryAssociation(
    name="fromEntries47",
    ends={
        Property(name="mql_FromEntry49", type=mql_FromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromClause48", type=mql_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable50: BinaryAssociation = BinaryAssociation(
    name="variable50",
    ends={
        Property(name="mql_VariableDeclaration", type=mql_FromEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromEntry51", type=mql_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joins52: BinaryAssociation = BinaryAssociation(
    name="joins52",
    ends={
        Property(name="mql_FromJoin", type=mql_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromClass", type=mql_FromJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromClause34: BinaryAssociation = BinaryAssociation(
    name="fromClause34",
    ends={
        Property(name="mql_FromClause", type=mql_DeleteClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_DeleteClause35", type=mql_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectClause36: BinaryAssociation = BinaryAssociation(
    name="selectClause36",
    ends={
        Property(name="mql_SelectClause", type=mql_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectFromClause37", type=mql_SelectClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause38: BinaryAssociation = BinaryAssociation(
    name="fromClause38",
    ends={
        Property(name="mql_FromClause40", type=mql_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SelectFromClause39", type=mql_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable58: BinaryAssociation = BinaryAssociation(
    name="variable58",
    ends={
        Property(name="mql_VariableDeclaration60", type=mql_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromJoin59", type=mql_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereEntry61: BinaryAssociation = BinaryAssociation(
    name="whereEntry61",
    ends={
        Property(name="mql_Expression63", type=mql_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_WhereClause62", type=mql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs64: BinaryAssociation = BinaryAssociation(
    name="lhs64",
    ends={
        Property(name="mql_Variable", type=mql_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_OperatorExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs65: BinaryAssociation = BinaryAssociation(
    name="rhs65",
    ends={
        Property(name="mql_ExpressionTerm", type=mql_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_OperatorExpression66", type=mql_ExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query67: BinaryAssociation = BinaryAssociation(
    name="query67",
    ends={
        Property(name="mql_SelectStatement68", type=mql_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_ExistsExpression", type=mql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query69: BinaryAssociation = BinaryAssociation(
    name="query69",
    ends={
        Property(name="mql_SelectStatement70", type=mql_AllExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_AllExpression", type=mql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query71: BinaryAssociation = BinaryAssociation(
    name="query71",
    ends={
        Property(name="mql_SelectStatement72", type=mql_AnyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_AnyExpression", type=mql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path53: BinaryAssociation = BinaryAssociation(
    name="path53",
    ends={
        Property(name="mql_AliasAttributeExpression54", type=mql_FromCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromCollection", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path55: BinaryAssociation = BinaryAssociation(
    name="path55",
    ends={
        Property(name="mql_AliasAttributeExpression57", type=mql_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_FromJoin56", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs77: BinaryAssociation = BinaryAssociation(
    name="rhs77",
    ends={
        Property(name="mql_AliasAttributeExpression79", type=mql_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_CollectionExpression78", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs80: BinaryAssociation = BinaryAssociation(
    name="lhs80",
    ends={
        Property(name="mql_Variable81", type=mql_NullComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_NullComparisonExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs82: BinaryAssociation = BinaryAssociation(
    name="lhs82",
    ends={
        Property(name="mql_Variable83", type=mql_EmptyComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_EmptyComparisonExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs84: BinaryAssociation = BinaryAssociation(
    name="lhs84",
    ends={
        Property(name="mql_Variable85", type=mql_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_LikeExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs86: BinaryAssociation = BinaryAssociation(
    name="lhs86",
    ends={
        Property(name="mql_Variable87", type=mql_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_InExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items88: BinaryAssociation = BinaryAssociation(
    name="items88",
    ends={
        Property(name="mql_Variable89", type=mql_InSeqExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_InSeqExpression", type=mql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query90: BinaryAssociation = BinaryAssociation(
    name="query90",
    ends={
        Property(name="mql_SelectStatement91", type=mql_InQueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_InQueryExpression", type=mql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query73: BinaryAssociation = BinaryAssociation(
    name="query73",
    ends={
        Property(name="mql_SelectStatement74", type=mql_SomeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_SomeExpression", type=mql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs75: BinaryAssociation = BinaryAssociation(
    name="lhs75",
    ends={
        Property(name="mql_Variable76", type=mql_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_CollectionExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias100: BinaryAssociation = BinaryAssociation(
    name="alias100",
    ends={
        Property(name="mql_VariableDeclaration102", type=mql_AliasAttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_AliasAttributeExpression101", type=mql_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
params103: BinaryAssociation = BinaryAssociation(
    name="params103",
    ends={
        Property(name="mql_Variable104", type=mql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_Function", type=mql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs92: BinaryAssociation = BinaryAssociation(
    name="lhs92",
    ends={
        Property(name="mql_Variable93", type=mql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_BetweenExpression", type=mql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
min94: BinaryAssociation = BinaryAssociation(
    name="min94",
    ends={
        Property(name="mql_Value96", type=mql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_BetweenExpression95", type=mql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max97: BinaryAssociation = BinaryAssociation(
    name="max97",
    ends={
        Property(name="mql_Value99", type=mql_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_BetweenExpression98", type=mql_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries107: BinaryAssociation = BinaryAssociation(
    name="entries107",
    ends={
        Property(name="mql_Expression108", type=mql_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_AndExpression", type=mql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries105: BinaryAssociation = BinaryAssociation(
    name="entries105",
    ends={
        Property(name="mql_Expression106", type=mql_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mql_OrExpression", type=mql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mql_SelectStatement_MQuery = Generalization(general=MQuery, specific=mql_SelectStatement)
gen_mql_SelectStatement_ExpressionTerm = Generalization(general=ExpressionTerm, specific=mql_SelectStatement)
gen_mql_UpdateStatement_MQuery = Generalization(general=MQuery, specific=mql_UpdateStatement)
gen_mql_DeleteStatement_MQuery = Generalization(general=MQuery, specific=mql_DeleteStatement)
gen_mql_SelectAggregateExpression_SelectExpression = Generalization(general=SelectExpression, specific=mql_SelectAggregateExpression)
gen_mql_AvgAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=mql_AvgAggregate)
gen_mql_MaxAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=mql_MaxAggregate)
gen_mql_MinAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=mql_MinAggregate)
gen_mql_SumAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=mql_SumAggregate)
gen_mql_CountAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=mql_CountAggregate)
gen_mql_SelectConstructorExpression_SelectExpression = Generalization(general=SelectExpression, specific=mql_SelectConstructorExpression)
gen_mql_FromClass_FromEntry = Generalization(general=FromEntry, specific=mql_FromClass)
gen_mql_Join_FromJoin = Generalization(general=FromJoin, specific=mql_Join)
gen_mql_LeftJoin_FromJoin = Generalization(general=FromJoin, specific=mql_LeftJoin)
gen_mql_InnerJoin_FromJoin = Generalization(general=FromJoin, specific=mql_InnerJoin)
gen_mql_OperatorExpression_Expression = Generalization(general=Expression, specific=mql_OperatorExpression)
gen_mql_ExistsExpression_Expression = Generalization(general=Expression, specific=mql_ExistsExpression)
gen_mql_AllExpression_Expression = Generalization(general=Expression, specific=mql_AllExpression)
gen_mql_AnyExpression_Expression = Generalization(general=Expression, specific=mql_AnyExpression)
gen_mql_FromCollection_FromEntry = Generalization(general=FromEntry, specific=mql_FromCollection)
gen_mql_NullComparisonExpression_Expression = Generalization(general=Expression, specific=mql_NullComparisonExpression)
gen_mql_EmptyComparisonExpression_Expression = Generalization(general=Expression, specific=mql_EmptyComparisonExpression)
gen_mql_LikeExpression_Expression = Generalization(general=Expression, specific=mql_LikeExpression)
gen_mql_InExpression_Expression = Generalization(general=Expression, specific=mql_InExpression)
gen_mql_InSeqExpression_InExpression = Generalization(general=InExpression, specific=mql_InSeqExpression)
gen_mql_InQueryExpression_InExpression = Generalization(general=InExpression, specific=mql_InQueryExpression)
gen_mql_BetweenExpression_Expression = Generalization(general=Expression, specific=mql_BetweenExpression)
gen_mql_SomeExpression_Expression = Generalization(general=Expression, specific=mql_SomeExpression)
gen_mql_CollectionExpression_Expression = Generalization(general=Expression, specific=mql_CollectionExpression)
gen_mql_Variable_ExpressionTerm = Generalization(general=ExpressionTerm, specific=mql_Variable)
gen_mql_ExpressionTerm_Expression = Generalization(general=Expression, specific=mql_ExpressionTerm)
gen_mql_AliasAttributeExpression_SelectExpression = Generalization(general=SelectExpression, specific=mql_AliasAttributeExpression)
gen_mql_AliasAttributeExpression_Variable = Generalization(general=Variable, specific=mql_AliasAttributeExpression)
gen_mql_ParameterExpression_Variable = Generalization(general=Variable, specific=mql_ParameterExpression)
gen_mql_Value_Variable = Generalization(general=Variable, specific=mql_Value)
gen_mql_IntegerExpression_Value = Generalization(general=Value, specific=mql_IntegerExpression)
gen_mql_StringExpression_Value = Generalization(general=Value, specific=mql_StringExpression)
gen_mql_NullExpression_Value = Generalization(general=Value, specific=mql_NullExpression)
gen_mql_BooleanExpression_Value = Generalization(general=Value, specific=mql_BooleanExpression)
gen_mql_DateTimeExpression_Value = Generalization(general=Value, specific=mql_DateTimeExpression)
gen_mql_OrExpression_Expression = Generalization(general=Expression, specific=mql_OrExpression)
gen_mql_AndExpression_Expression = Generalization(general=Expression, specific=mql_AndExpression)

# Domain Model
domain_model = DomainModel(
    name="mql",
    types={mql_QueryModule, mql_Import, mql_MQuery, mql_NamedQuery, mql_WhereClause, mql_SelectStatement, MQuery, ExpressionTerm, mql_SelectFromClause, mql_OrderItem, mql_FromEntry, mql_UpdateStatement, mql_UpdateClause, mql_SetClause, mql_UpdateItem, mql_AliasAttributeExpression, mql_Value, mql_DeleteStatement, mql_DeleteClause, mql_FromClause, mql_HavingClause, mql_OrderClause, mql_Expression, mql_SelectExpression, mql_SelectAggregateExpression, SelectExpression, mql_AvgAggregate, SelectAggregateExpression, mql_MaxAggregate, mql_MinAggregate, mql_SumAggregate, mql_CountAggregate, mql_SelectConstructorExpression, mql_VariableDeclaration, mql_FromClass, FromEntry, mql_FromJoin, mql_SelectClause, mql_Join, FromJoin, mql_LeftJoin, mql_InnerJoin, mql_OperatorExpression, Expression, mql_Variable, mql_ExpressionTerm, mql_ExistsExpression, mql_AllExpression, mql_AnyExpression, mql_FromCollection, mql_NullComparisonExpression, mql_EmptyComparisonExpression, mql_LikeExpression, mql_InExpression, mql_InSeqExpression, InExpression, mql_InQueryExpression, mql_BetweenExpression, mql_SomeExpression, mql_CollectionExpression, Variable, mql_ParameterExpression, mql_Function, mql_IntegerExpression, Value, mql_StringExpression, mql_NullExpression, mql_BooleanExpression, mql_DateTimeExpression, mql_OrExpression, mql_AndExpression, Operator},
    associations={imports0, defaultQuery1, namedQueries3, query5, whereClause8, selectFromClause10, ordering17, var19, updateClause21, setClause22, fromEntries24, items27, alias29, value31, deleteClause33, having11, order13, having15, expressions41, item43, items45, fromEntries47, variable50, joins52, fromClause34, selectClause36, fromClause38, variable58, whereEntry61, lhs64, rhs65, query67, query69, query71, path53, path55, rhs77, lhs80, lhs82, lhs84, lhs86, items88, query90, query73, lhs75, alias100, params103, lhs92, min94, max97, entries107, entries105},
    generalizations={gen_mql_SelectStatement_MQuery, gen_mql_SelectStatement_ExpressionTerm, gen_mql_UpdateStatement_MQuery, gen_mql_DeleteStatement_MQuery, gen_mql_SelectAggregateExpression_SelectExpression, gen_mql_AvgAggregate_SelectAggregateExpression, gen_mql_MaxAggregate_SelectAggregateExpression, gen_mql_MinAggregate_SelectAggregateExpression, gen_mql_SumAggregate_SelectAggregateExpression, gen_mql_CountAggregate_SelectAggregateExpression, gen_mql_SelectConstructorExpression_SelectExpression, gen_mql_FromClass_FromEntry, gen_mql_Join_FromJoin, gen_mql_LeftJoin_FromJoin, gen_mql_InnerJoin_FromJoin, gen_mql_OperatorExpression_Expression, gen_mql_ExistsExpression_Expression, gen_mql_AllExpression_Expression, gen_mql_AnyExpression_Expression, gen_mql_FromCollection_FromEntry, gen_mql_NullComparisonExpression_Expression, gen_mql_EmptyComparisonExpression_Expression, gen_mql_LikeExpression_Expression, gen_mql_InExpression_Expression, gen_mql_InSeqExpression_InExpression, gen_mql_InQueryExpression_InExpression, gen_mql_BetweenExpression_Expression, gen_mql_SomeExpression_Expression, gen_mql_CollectionExpression_Expression, gen_mql_Variable_ExpressionTerm, gen_mql_ExpressionTerm_Expression, gen_mql_AliasAttributeExpression_SelectExpression, gen_mql_AliasAttributeExpression_Variable, gen_mql_ParameterExpression_Variable, gen_mql_Value_Variable, gen_mql_IntegerExpression_Value, gen_mql_StringExpression_Value, gen_mql_NullExpression_Value, gen_mql_BooleanExpression_Value, gen_mql_DateTimeExpression_Value, gen_mql_OrExpression_Expression, gen_mql_AndExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
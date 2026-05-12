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
jPQL_SelectStatement = Class(name="jPQL_SelectStatement")
Query = Class(name="Query")
ExpressionTerm = Class(name="ExpressionTerm")
jPQL_SelectFromClause = Class(name="jPQL_SelectFromClause")
jPQL_HavingClause = Class(name="jPQL_HavingClause")
jPQL_OrderClause = Class(name="jPQL_OrderClause")
jPQL_Expression = Class(name="jPQL_Expression")
jPQL_OrderItem = Class(name="jPQL_OrderItem")
jPQL_QueryModule = Class(name="jPQL_QueryModule")
jPQL_Query = Class(name="jPQL_Query")
jPQL_WhereClause = Class(name="jPQL_WhereClause")
jPQL_DeleteStatement = Class(name="jPQL_DeleteStatement")
jPQL_DeleteClause = Class(name="jPQL_DeleteClause")
jPQL_FromClause = Class(name="jPQL_FromClause")
jPQL_SelectClause = Class(name="jPQL_SelectClause")
jPQL_SelectExpression = Class(name="jPQL_SelectExpression")
jPQL_FromEntry = Class(name="jPQL_FromEntry")
jPQL_UpdateStatement = Class(name="jPQL_UpdateStatement")
jPQL_UpdateClause = Class(name="jPQL_UpdateClause")
jPQL_SetClause = Class(name="jPQL_SetClause")
jPQL_UpdateItem = Class(name="jPQL_UpdateItem")
jPQL_AliasAttributeExpression = Class(name="jPQL_AliasAttributeExpression")
jPQL_Value = Class(name="jPQL_Value")
jPQL_FromJoin = Class(name="jPQL_FromJoin")
jPQL_FromCollection = Class(name="jPQL_FromCollection")
jPQL_Join = Class(name="jPQL_Join")
FromJoin = Class(name="FromJoin")
jPQL_LeftJoin = Class(name="jPQL_LeftJoin")
jPQL_InnerJoin = Class(name="jPQL_InnerJoin")
jPQL_SelectAggregateExpression = Class(name="jPQL_SelectAggregateExpression")
SelectExpression = Class(name="SelectExpression")
jPQL_AvgAggregate = Class(name="jPQL_AvgAggregate")
SelectAggregateExpression = Class(name="SelectAggregateExpression")
jPQL_MaxAggregate = Class(name="jPQL_MaxAggregate")
jPQL_MinAggregate = Class(name="jPQL_MinAggregate")
jPQL_SumAggregate = Class(name="jPQL_SumAggregate")
jPQL_CountAggregate = Class(name="jPQL_CountAggregate")
jPQL_SelectConstructorExpression = Class(name="jPQL_SelectConstructorExpression")
jPQL_VariableDeclaration = Class(name="jPQL_VariableDeclaration")
jPQL_FromClass = Class(name="jPQL_FromClass")
FromEntry = Class(name="FromEntry")
jPQL_JvmType = Class(name="jPQL_JvmType")
jPQL_CollectionExpression = Class(name="jPQL_CollectionExpression")
jPQL_NullComparisonExpression = Class(name="jPQL_NullComparisonExpression")
jPQL_EmptyComparisonExpression = Class(name="jPQL_EmptyComparisonExpression")
jPQL_LikeExpression = Class(name="jPQL_LikeExpression")
jPQL_OperatorExpression = Class(name="jPQL_OperatorExpression")
Expression = Class(name="Expression")
jPQL_Variable = Class(name="jPQL_Variable")
jPQL_ExpressionTerm = Class(name="jPQL_ExpressionTerm")
jPQL_ExistsExpression = Class(name="jPQL_ExistsExpression")
jPQL_AllExpression = Class(name="jPQL_AllExpression")
jPQL_AnyExpression = Class(name="jPQL_AnyExpression")
jPQL_SomeExpression = Class(name="jPQL_SomeExpression")
Variable = Class(name="Variable")
jPQL_ParameterExpression = Class(name="jPQL_ParameterExpression")
jPQL_Function = Class(name="jPQL_Function")
jPQL_IntegerExpression = Class(name="jPQL_IntegerExpression")
Value = Class(name="Value")
jPQL_InExpression = Class(name="jPQL_InExpression")
jPQL_InSeqExpression = Class(name="jPQL_InSeqExpression")
InExpression = Class(name="InExpression")
jPQL_InQueryExpression = Class(name="jPQL_InQueryExpression")
jPQL_BetweenExpression = Class(name="jPQL_BetweenExpression")
jPQL_StringExpression = Class(name="jPQL_StringExpression")
jPQL_NullExpression = Class(name="jPQL_NullExpression")
jPQL_BooleanExpression = Class(name="jPQL_BooleanExpression")
jPQL_DateTimeExpression = Class(name="jPQL_DateTimeExpression")
jPQL_OrExpression = Class(name="jPQL_OrExpression")
jPQL_AndExpression = Class(name="jPQL_AndExpression")

# jPQL_SelectStatement class attributes and methods

# Query class attributes and methods

# ExpressionTerm class attributes and methods

# jPQL_SelectFromClause class attributes and methods

# jPQL_HavingClause class attributes and methods

# jPQL_OrderClause class attributes and methods
jPQL_OrderClause_isAsc: Property = Property(name="isAsc", type=BooleanType)
jPQL_OrderClause_isDesc: Property = Property(name="isDesc", type=BooleanType)
jPQL_OrderClause.attributes={jPQL_OrderClause_isAsc, jPQL_OrderClause_isDesc}

# jPQL_Expression class attributes and methods

# jPQL_OrderItem class attributes and methods
jPQL_OrderItem_feature: Property = Property(name="feature", type=StringType)
jPQL_OrderItem.attributes={jPQL_OrderItem_feature}

# jPQL_QueryModule class attributes and methods

# jPQL_Query class attributes and methods

# jPQL_WhereClause class attributes and methods

# jPQL_DeleteStatement class attributes and methods

# jPQL_DeleteClause class attributes and methods

# jPQL_FromClause class attributes and methods

# jPQL_SelectClause class attributes and methods
jPQL_SelectClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jPQL_SelectClause.attributes={jPQL_SelectClause_isDistinct}

# jPQL_SelectExpression class attributes and methods

# jPQL_FromEntry class attributes and methods

# jPQL_UpdateStatement class attributes and methods

# jPQL_UpdateClause class attributes and methods

# jPQL_SetClause class attributes and methods

# jPQL_UpdateItem class attributes and methods

# jPQL_AliasAttributeExpression class attributes and methods
jPQL_AliasAttributeExpression_attributes: Property = Property(name="attributes", type=StringType)
jPQL_AliasAttributeExpression.attributes={jPQL_AliasAttributeExpression_attributes}

# jPQL_Value class attributes and methods

# jPQL_FromJoin class attributes and methods
jPQL_FromJoin_isFetch: Property = Property(name="isFetch", type=BooleanType)
jPQL_FromJoin.attributes={jPQL_FromJoin_isFetch}

# jPQL_FromCollection class attributes and methods

# jPQL_Join class attributes and methods

# FromJoin class attributes and methods

# jPQL_LeftJoin class attributes and methods
jPQL_LeftJoin_isOuter: Property = Property(name="isOuter", type=BooleanType)
jPQL_LeftJoin.attributes={jPQL_LeftJoin_isOuter}

# jPQL_InnerJoin class attributes and methods

# jPQL_SelectAggregateExpression class attributes and methods
jPQL_SelectAggregateExpression_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jPQL_SelectAggregateExpression.attributes={jPQL_SelectAggregateExpression_isDistinct}

# SelectExpression class attributes and methods

# jPQL_AvgAggregate class attributes and methods

# SelectAggregateExpression class attributes and methods

# jPQL_MaxAggregate class attributes and methods

# jPQL_MinAggregate class attributes and methods

# jPQL_SumAggregate class attributes and methods

# jPQL_CountAggregate class attributes and methods

# jPQL_SelectConstructorExpression class attributes and methods
jPQL_SelectConstructorExpression_name: Property = Property(name="name", type=StringType)
jPQL_SelectConstructorExpression.attributes={jPQL_SelectConstructorExpression_name}

# jPQL_VariableDeclaration class attributes and methods
jPQL_VariableDeclaration_name: Property = Property(name="name", type=StringType)
jPQL_VariableDeclaration.attributes={jPQL_VariableDeclaration_name}

# jPQL_FromClass class attributes and methods

# FromEntry class attributes and methods

# jPQL_JvmType class attributes and methods

# jPQL_CollectionExpression class attributes and methods
jPQL_CollectionExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_CollectionExpression.attributes={jPQL_CollectionExpression_isNot}

# jPQL_NullComparisonExpression class attributes and methods
jPQL_NullComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_NullComparisonExpression.attributes={jPQL_NullComparisonExpression_isNot}

# jPQL_EmptyComparisonExpression class attributes and methods
jPQL_EmptyComparisonExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_EmptyComparisonExpression.attributes={jPQL_EmptyComparisonExpression_isNot}

# jPQL_LikeExpression class attributes and methods
jPQL_LikeExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_LikeExpression_pattern: Property = Property(name="pattern", type=StringType)
jPQL_LikeExpression.attributes={jPQL_LikeExpression_isNot, jPQL_LikeExpression_pattern}

# jPQL_OperatorExpression class attributes and methods
jPQL_OperatorExpression_operator: Property = Property(name="operator", type=StringType)
jPQL_OperatorExpression.attributes={jPQL_OperatorExpression_operator}

# Expression class attributes and methods

# jPQL_Variable class attributes and methods

# jPQL_ExpressionTerm class attributes and methods

# jPQL_ExistsExpression class attributes and methods
jPQL_ExistsExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_ExistsExpression.attributes={jPQL_ExistsExpression_isNot}

# jPQL_AllExpression class attributes and methods

# jPQL_AnyExpression class attributes and methods

# jPQL_SomeExpression class attributes and methods

# Variable class attributes and methods

# jPQL_ParameterExpression class attributes and methods
jPQL_ParameterExpression_name: Property = Property(name="name", type=StringType)
jPQL_ParameterExpression.attributes={jPQL_ParameterExpression_name}

# jPQL_Function class attributes and methods
jPQL_Function_name: Property = Property(name="name", type=StringType)
jPQL_Function.attributes={jPQL_Function_name}

# jPQL_IntegerExpression class attributes and methods
jPQL_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
jPQL_IntegerExpression.attributes={jPQL_IntegerExpression_value}

# Value class attributes and methods

# jPQL_InExpression class attributes and methods
jPQL_InExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_InExpression.attributes={jPQL_InExpression_isNot}

# jPQL_InSeqExpression class attributes and methods

# InExpression class attributes and methods

# jPQL_InQueryExpression class attributes and methods

# jPQL_BetweenExpression class attributes and methods
jPQL_BetweenExpression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_BetweenExpression.attributes={jPQL_BetweenExpression_isNot}

# jPQL_StringExpression class attributes and methods
jPQL_StringExpression_value: Property = Property(name="value", type=StringType)
jPQL_StringExpression.attributes={jPQL_StringExpression_value}

# jPQL_NullExpression class attributes and methods
jPQL_NullExpression_value: Property = Property(name="value", type=StringType)
jPQL_NullExpression.attributes={jPQL_NullExpression_value}

# jPQL_BooleanExpression class attributes and methods
jPQL_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
jPQL_BooleanExpression.attributes={jPQL_BooleanExpression_value}

# jPQL_DateTimeExpression class attributes and methods
jPQL_DateTimeExpression_value: Property = Property(name="value", type=StringType)
jPQL_DateTimeExpression.attributes={jPQL_DateTimeExpression_value}

# jPQL_OrExpression class attributes and methods

# jPQL_AndExpression class attributes and methods

# Relationships
whereClause1: BinaryAssociation = BinaryAssociation(
    name="whereClause1",
    ends={
        Property(name="jPQL_WhereClause", type=jPQL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Query2", type=jPQL_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectFromClause3: BinaryAssociation = BinaryAssociation(
    name="selectFromClause3",
    ends={
        Property(name="jPQL_SelectFromClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement", type=jPQL_SelectFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having4: BinaryAssociation = BinaryAssociation(
    name="having4",
    ends={
        Property(name="jPQL_HavingClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement5", type=jPQL_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
order6: BinaryAssociation = BinaryAssociation(
    name="order6",
    ends={
        Property(name="jPQL_OrderClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement7", type=jPQL_OrderClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having8: BinaryAssociation = BinaryAssociation(
    name="having8",
    ends={
        Property(name="jPQL_Expression", type=jPQL_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_HavingClause9", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering10: BinaryAssociation = BinaryAssociation(
    name="ordering10",
    ends={
        Property(name="jPQL_OrderItem", type=jPQL_OrderClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OrderClause11", type=jPQL_OrderItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries0: BinaryAssociation = BinaryAssociation(
    name="queries0",
    ends={
        Property(name="jPQL_Query", type=jPQL_QueryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_QueryModule", type=jPQL_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deleteClause26: BinaryAssociation = BinaryAssociation(
    name="deleteClause26",
    ends={
        Property(name="jPQL_DeleteClause", type=jPQL_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_DeleteStatement", type=jPQL_DeleteClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause27: BinaryAssociation = BinaryAssociation(
    name="fromClause27",
    ends={
        Property(name="jPQL_FromClause", type=jPQL_DeleteClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_DeleteClause28", type=jPQL_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectClause29: BinaryAssociation = BinaryAssociation(
    name="selectClause29",
    ends={
        Property(name="jPQL_SelectClause", type=jPQL_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectFromClause30", type=jPQL_SelectClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause31: BinaryAssociation = BinaryAssociation(
    name="fromClause31",
    ends={
        Property(name="jPQL_FromClause33", type=jPQL_SelectFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectFromClause32", type=jPQL_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions34: BinaryAssociation = BinaryAssociation(
    name="expressions34",
    ends={
        Property(name="jPQL_SelectExpression", type=jPQL_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectClause35", type=jPQL_SelectExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var12: BinaryAssociation = BinaryAssociation(
    name="var12",
    ends={
        Property(name="jPQL_FromEntry", type=jPQL_OrderItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OrderItem13", type=jPQL_FromEntry, multiplicity=Multiplicity(0, 1))
    }
)
updateClause14: BinaryAssociation = BinaryAssociation(
    name="updateClause14",
    ends={
        Property(name="jPQL_UpdateClause", type=jPQL_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateStatement", type=jPQL_UpdateClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setClause15: BinaryAssociation = BinaryAssociation(
    name="setClause15",
    ends={
        Property(name="jPQL_SetClause", type=jPQL_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateStatement16", type=jPQL_SetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromEntries17: BinaryAssociation = BinaryAssociation(
    name="fromEntries17",
    ends={
        Property(name="jPQL_FromEntry19", type=jPQL_UpdateClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateClause18", type=jPQL_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items20: BinaryAssociation = BinaryAssociation(
    name="items20",
    ends={
        Property(name="jPQL_UpdateItem", type=jPQL_SetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SetClause21", type=jPQL_UpdateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias22: BinaryAssociation = BinaryAssociation(
    name="alias22",
    ends={
        Property(name="jPQL_AliasAttributeExpression", type=jPQL_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateItem23", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="jPQL_Value", type=jPQL_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateItem25", type=jPQL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joins46: BinaryAssociation = BinaryAssociation(
    name="joins46",
    ends={
        Property(name="jPQL_FromJoin", type=jPQL_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromClass47", type=jPQL_FromJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path48: BinaryAssociation = BinaryAssociation(
    name="path48",
    ends={
        Property(name="jPQL_AliasAttributeExpression49", type=jPQL_FromCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromCollection", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path50: BinaryAssociation = BinaryAssociation(
    name="path50",
    ends={
        Property(name="jPQL_AliasAttributeExpression52", type=jPQL_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromJoin51", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable53: BinaryAssociation = BinaryAssociation(
    name="variable53",
    ends={
        Property(name="jPQL_VariableDeclaration55", type=jPQL_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromJoin54", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item36: BinaryAssociation = BinaryAssociation(
    name="item36",
    ends={
        Property(name="jPQL_AliasAttributeExpression37", type=jPQL_SelectAggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectAggregateExpression", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items38: BinaryAssociation = BinaryAssociation(
    name="items38",
    ends={
        Property(name="jPQL_AliasAttributeExpression39", type=jPQL_SelectConstructorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectConstructorExpression", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromEntries40: BinaryAssociation = BinaryAssociation(
    name="fromEntries40",
    ends={
        Property(name="jPQL_FromEntry42", type=jPQL_FromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromClause41", type=jPQL_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable43: BinaryAssociation = BinaryAssociation(
    name="variable43",
    ends={
        Property(name="jPQL_VariableDeclaration", type=jPQL_FromEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromEntry44", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="jPQL_JvmType", type=jPQL_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromClass", type=jPQL_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
lhs70: BinaryAssociation = BinaryAssociation(
    name="lhs70",
    ends={
        Property(name="jPQL_Variable71", type=jPQL_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_CollectionExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs72: BinaryAssociation = BinaryAssociation(
    name="rhs72",
    ends={
        Property(name="jPQL_AliasAttributeExpression74", type=jPQL_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_CollectionExpression73", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs75: BinaryAssociation = BinaryAssociation(
    name="lhs75",
    ends={
        Property(name="jPQL_Variable76", type=jPQL_NullComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_NullComparisonExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs77: BinaryAssociation = BinaryAssociation(
    name="lhs77",
    ends={
        Property(name="jPQL_Variable78", type=jPQL_EmptyComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_EmptyComparisonExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereEntry56: BinaryAssociation = BinaryAssociation(
    name="whereEntry56",
    ends={
        Property(name="jPQL_Expression58", type=jPQL_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_WhereClause57", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs59: BinaryAssociation = BinaryAssociation(
    name="lhs59",
    ends={
        Property(name="jPQL_Variable", type=jPQL_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OperatorExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs60: BinaryAssociation = BinaryAssociation(
    name="rhs60",
    ends={
        Property(name="jPQL_ExpressionTerm", type=jPQL_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OperatorExpression61", type=jPQL_ExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query62: BinaryAssociation = BinaryAssociation(
    name="query62",
    ends={
        Property(name="jPQL_SelectStatement63", type=jPQL_ExistsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_ExistsExpression", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query64: BinaryAssociation = BinaryAssociation(
    name="query64",
    ends={
        Property(name="jPQL_SelectStatement65", type=jPQL_AllExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AllExpression", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query66: BinaryAssociation = BinaryAssociation(
    name="query66",
    ends={
        Property(name="jPQL_SelectStatement67", type=jPQL_AnyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AnyExpression", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query68: BinaryAssociation = BinaryAssociation(
    name="query68",
    ends={
        Property(name="jPQL_SelectStatement69", type=jPQL_SomeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SomeExpression", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias95: BinaryAssociation = BinaryAssociation(
    name="alias95",
    ends={
        Property(name="jPQL_VariableDeclaration97", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AliasAttributeExpression96", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
params98: BinaryAssociation = BinaryAssociation(
    name="params98",
    ends={
        Property(name="jPQL_Variable99", type=jPQL_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Function", type=jPQL_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs79: BinaryAssociation = BinaryAssociation(
    name="lhs79",
    ends={
        Property(name="jPQL_Variable80", type=jPQL_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_LikeExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs81: BinaryAssociation = BinaryAssociation(
    name="lhs81",
    ends={
        Property(name="jPQL_Variable82", type=jPQL_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_InExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items83: BinaryAssociation = BinaryAssociation(
    name="items83",
    ends={
        Property(name="jPQL_Variable84", type=jPQL_InSeqExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_InSeqExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query85: BinaryAssociation = BinaryAssociation(
    name="query85",
    ends={
        Property(name="jPQL_SelectStatement86", type=jPQL_InQueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_InQueryExpression", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs87: BinaryAssociation = BinaryAssociation(
    name="lhs87",
    ends={
        Property(name="jPQL_Variable88", type=jPQL_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_BetweenExpression", type=jPQL_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
min89: BinaryAssociation = BinaryAssociation(
    name="min89",
    ends={
        Property(name="jPQL_Value91", type=jPQL_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_BetweenExpression90", type=jPQL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max92: BinaryAssociation = BinaryAssociation(
    name="max92",
    ends={
        Property(name="jPQL_Value94", type=jPQL_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_BetweenExpression93", type=jPQL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries100: BinaryAssociation = BinaryAssociation(
    name="entries100",
    ends={
        Property(name="jPQL_Expression101", type=jPQL_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OrExpression", type=jPQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries102: BinaryAssociation = BinaryAssociation(
    name="entries102",
    ends={
        Property(name="jPQL_Expression103", type=jPQL_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AndExpression", type=jPQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jPQL_SelectStatement_Query = Generalization(general=Query, specific=jPQL_SelectStatement)
gen_jPQL_SelectStatement_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jPQL_SelectStatement)
gen_jPQL_DeleteStatement_Query = Generalization(general=Query, specific=jPQL_DeleteStatement)
gen_jPQL_UpdateStatement_Query = Generalization(general=Query, specific=jPQL_UpdateStatement)
gen_jPQL_FromCollection_FromEntry = Generalization(general=FromEntry, specific=jPQL_FromCollection)
gen_jPQL_Join_FromJoin = Generalization(general=FromJoin, specific=jPQL_Join)
gen_jPQL_LeftJoin_FromJoin = Generalization(general=FromJoin, specific=jPQL_LeftJoin)
gen_jPQL_InnerJoin_FromJoin = Generalization(general=FromJoin, specific=jPQL_InnerJoin)
gen_jPQL_SelectAggregateExpression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_SelectAggregateExpression)
gen_jPQL_AvgAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_AvgAggregate)
gen_jPQL_MaxAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_MaxAggregate)
gen_jPQL_MinAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_MinAggregate)
gen_jPQL_SumAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_SumAggregate)
gen_jPQL_CountAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_CountAggregate)
gen_jPQL_SelectConstructorExpression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_SelectConstructorExpression)
gen_jPQL_FromClass_FromEntry = Generalization(general=FromEntry, specific=jPQL_FromClass)
gen_jPQL_CollectionExpression_Expression = Generalization(general=Expression, specific=jPQL_CollectionExpression)
gen_jPQL_NullComparisonExpression_Expression = Generalization(general=Expression, specific=jPQL_NullComparisonExpression)
gen_jPQL_EmptyComparisonExpression_Expression = Generalization(general=Expression, specific=jPQL_EmptyComparisonExpression)
gen_jPQL_LikeExpression_Expression = Generalization(general=Expression, specific=jPQL_LikeExpression)
gen_jPQL_OperatorExpression_Expression = Generalization(general=Expression, specific=jPQL_OperatorExpression)
gen_jPQL_ExistsExpression_Expression = Generalization(general=Expression, specific=jPQL_ExistsExpression)
gen_jPQL_AllExpression_Expression = Generalization(general=Expression, specific=jPQL_AllExpression)
gen_jPQL_AnyExpression_Expression = Generalization(general=Expression, specific=jPQL_AnyExpression)
gen_jPQL_SomeExpression_Expression = Generalization(general=Expression, specific=jPQL_SomeExpression)
gen_jPQL_ExpressionTerm_Expression = Generalization(general=Expression, specific=jPQL_ExpressionTerm)
gen_jPQL_AliasAttributeExpression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_AliasAttributeExpression)
gen_jPQL_AliasAttributeExpression_Variable = Generalization(general=Variable, specific=jPQL_AliasAttributeExpression)
gen_jPQL_ParameterExpression_Variable = Generalization(general=Variable, specific=jPQL_ParameterExpression)
gen_jPQL_Value_Variable = Generalization(general=Variable, specific=jPQL_Value)
gen_jPQL_IntegerExpression_Value = Generalization(general=Value, specific=jPQL_IntegerExpression)
gen_jPQL_InExpression_Expression = Generalization(general=Expression, specific=jPQL_InExpression)
gen_jPQL_InSeqExpression_InExpression = Generalization(general=InExpression, specific=jPQL_InSeqExpression)
gen_jPQL_InQueryExpression_InExpression = Generalization(general=InExpression, specific=jPQL_InQueryExpression)
gen_jPQL_BetweenExpression_Expression = Generalization(general=Expression, specific=jPQL_BetweenExpression)
gen_jPQL_Variable_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jPQL_Variable)
gen_jPQL_StringExpression_Value = Generalization(general=Value, specific=jPQL_StringExpression)
gen_jPQL_NullExpression_Value = Generalization(general=Value, specific=jPQL_NullExpression)
gen_jPQL_BooleanExpression_Value = Generalization(general=Value, specific=jPQL_BooleanExpression)
gen_jPQL_DateTimeExpression_Value = Generalization(general=Value, specific=jPQL_DateTimeExpression)
gen_jPQL_OrExpression_Expression = Generalization(general=Expression, specific=jPQL_OrExpression)
gen_jPQL_AndExpression_Expression = Generalization(general=Expression, specific=jPQL_AndExpression)

# Domain Model
domain_model = DomainModel(
    name="jPQL",
    types={jPQL_SelectStatement, Query, ExpressionTerm, jPQL_SelectFromClause, jPQL_HavingClause, jPQL_OrderClause, jPQL_Expression, jPQL_OrderItem, jPQL_QueryModule, jPQL_Query, jPQL_WhereClause, jPQL_DeleteStatement, jPQL_DeleteClause, jPQL_FromClause, jPQL_SelectClause, jPQL_SelectExpression, jPQL_FromEntry, jPQL_UpdateStatement, jPQL_UpdateClause, jPQL_SetClause, jPQL_UpdateItem, jPQL_AliasAttributeExpression, jPQL_Value, jPQL_FromJoin, jPQL_FromCollection, jPQL_Join, FromJoin, jPQL_LeftJoin, jPQL_InnerJoin, jPQL_SelectAggregateExpression, SelectExpression, jPQL_AvgAggregate, SelectAggregateExpression, jPQL_MaxAggregate, jPQL_MinAggregate, jPQL_SumAggregate, jPQL_CountAggregate, jPQL_SelectConstructorExpression, jPQL_VariableDeclaration, jPQL_FromClass, FromEntry, jPQL_JvmType, jPQL_CollectionExpression, jPQL_NullComparisonExpression, jPQL_EmptyComparisonExpression, jPQL_LikeExpression, jPQL_OperatorExpression, Expression, jPQL_Variable, jPQL_ExpressionTerm, jPQL_ExistsExpression, jPQL_AllExpression, jPQL_AnyExpression, jPQL_SomeExpression, Variable, jPQL_ParameterExpression, jPQL_Function, jPQL_IntegerExpression, Value, jPQL_InExpression, jPQL_InSeqExpression, InExpression, jPQL_InQueryExpression, jPQL_BetweenExpression, jPQL_StringExpression, jPQL_NullExpression, jPQL_BooleanExpression, jPQL_DateTimeExpression, jPQL_OrExpression, jPQL_AndExpression, Operator},
    associations={whereClause1, selectFromClause3, having4, order6, having8, ordering10, queries0, deleteClause26, fromClause27, selectClause29, fromClause31, expressions34, var12, updateClause14, setClause15, fromEntries17, items20, alias22, value24, joins46, path48, path50, variable53, item36, items38, fromEntries40, variable43, type45, lhs70, rhs72, lhs75, lhs77, whereEntry56, lhs59, rhs60, query62, query64, query66, query68, alias95, params98, lhs79, lhs81, items83, query85, lhs87, min89, max92, entries100, entries102},
    generalizations={gen_jPQL_SelectStatement_Query, gen_jPQL_SelectStatement_ExpressionTerm, gen_jPQL_DeleteStatement_Query, gen_jPQL_UpdateStatement_Query, gen_jPQL_FromCollection_FromEntry, gen_jPQL_Join_FromJoin, gen_jPQL_LeftJoin_FromJoin, gen_jPQL_InnerJoin_FromJoin, gen_jPQL_SelectAggregateExpression_SelectExpression, gen_jPQL_AvgAggregate_SelectAggregateExpression, gen_jPQL_MaxAggregate_SelectAggregateExpression, gen_jPQL_MinAggregate_SelectAggregateExpression, gen_jPQL_SumAggregate_SelectAggregateExpression, gen_jPQL_CountAggregate_SelectAggregateExpression, gen_jPQL_SelectConstructorExpression_SelectExpression, gen_jPQL_FromClass_FromEntry, gen_jPQL_CollectionExpression_Expression, gen_jPQL_NullComparisonExpression_Expression, gen_jPQL_EmptyComparisonExpression_Expression, gen_jPQL_LikeExpression_Expression, gen_jPQL_OperatorExpression_Expression, gen_jPQL_ExistsExpression_Expression, gen_jPQL_AllExpression_Expression, gen_jPQL_AnyExpression_Expression, gen_jPQL_SomeExpression_Expression, gen_jPQL_ExpressionTerm_Expression, gen_jPQL_AliasAttributeExpression_SelectExpression, gen_jPQL_AliasAttributeExpression_Variable, gen_jPQL_ParameterExpression_Variable, gen_jPQL_Value_Variable, gen_jPQL_IntegerExpression_Value, gen_jPQL_InExpression_Expression, gen_jPQL_InSeqExpression_InExpression, gen_jPQL_InQueryExpression_InExpression, gen_jPQL_BetweenExpression_Expression, gen_jPQL_Variable_ExpressionTerm, gen_jPQL_StringExpression_Value, gen_jPQL_NullExpression_Value, gen_jPQL_BooleanExpression_Value, gen_jPQL_DateTimeExpression_Value, gen_jPQL_OrExpression_Expression, gen_jPQL_AndExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
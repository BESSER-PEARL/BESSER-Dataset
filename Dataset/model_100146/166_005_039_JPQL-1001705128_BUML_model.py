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
OrderByDirection: Enumeration = Enumeration(
    name="OrderByDirection",
    literals={
            EnumerationLiteral(name="asc"),
			EnumerationLiteral(name="desc")
    }
)

TrimSpec: Enumeration = Enumeration(
    name="TrimSpec",
    literals={
            EnumerationLiteral(name="leading"),
			EnumerationLiteral(name="trailing"),
			EnumerationLiteral(name="both")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="positive"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="logicalNot")
    }
)

AdditionOperator: Enumeration = Enumeration(
    name="AdditionOperator",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract")
    }
)

MultiplicationOperator: Enumeration = Enumeration(
    name="MultiplicationOperator",
    literals={
            EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide")
    }
)

ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
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
jPQL_JPQLQuery = Class(name="jPQL_JPQLQuery")
jPQL_SetClause = Class(name="jPQL_SetClause")
jPQL_FromEntry = Class(name="jPQL_FromEntry")
jPQL_UpdateItem = Class(name="jPQL_UpdateItem")
jPQL_WhereClause = Class(name="jPQL_WhereClause")
jPQL_SelectStatement = Class(name="jPQL_SelectStatement")
JPQLQuery = Class(name="JPQLQuery")
ExpressionTerm = Class(name="ExpressionTerm")
jPQL_SelectClause = Class(name="jPQL_SelectClause")
jPQL_FromClause = Class(name="jPQL_FromClause")
jPQL_GroupByClause = Class(name="jPQL_GroupByClause")
jPQL_OrderByClause = Class(name="jPQL_OrderByClause")
jPQL_AliasAttributeExpression = Class(name="jPQL_AliasAttributeExpression")
jPQL_HavingClause = Class(name="jPQL_HavingClause")
jPQL_Expression = Class(name="jPQL_Expression")
jPQL_OrderBySpec = Class(name="jPQL_OrderBySpec")
jPQL_UpdateStatement = Class(name="jPQL_UpdateStatement")
jPQL_UpdateClause = Class(name="jPQL_UpdateClause")
jPQL_VariableDeclaration = Class(name="jPQL_VariableDeclaration")
jPQL_FromClass = Class(name="jPQL_FromClass")
FromEntry = Class(name="FromEntry")
jPQL_Literal = Class(name="jPQL_Literal")
jPQL_DeleteStatement = Class(name="jPQL_DeleteStatement")
jPQL_DeleteClause = Class(name="jPQL_DeleteClause")
jPQL_SelectExpression = Class(name="jPQL_SelectExpression")
jPQL_SelectAggregateExpression = Class(name="jPQL_SelectAggregateExpression")
SelectExpression = Class(name="SelectExpression")
jPQL_AvgAggregate = Class(name="jPQL_AvgAggregate")
SelectAggregateExpression = Class(name="SelectAggregateExpression")
jPQL_CountAggregate = Class(name="jPQL_CountAggregate")
jPQL_MaxAggregate = Class(name="jPQL_MaxAggregate")
jPQL_MinAggregate = Class(name="jPQL_MinAggregate")
jPQL_SumAggregate = Class(name="jPQL_SumAggregate")
jPQL_SelectConstructorExpression = Class(name="jPQL_SelectConstructorExpression")
Expression = Class(name="Expression")
jPQL_FromJoin = Class(name="jPQL_FromJoin")
jPQL_FromCollection = Class(name="jPQL_FromCollection")
jPQL_Join = Class(name="jPQL_Join")
FromJoin = Class(name="FromJoin")
jPQL_LeftJoin = Class(name="jPQL_LeftJoin")
jPQL_InnerJoin = Class(name="jPQL_InnerJoin")
jPQL_Variable = Class(name="jPQL_Variable")
jPQL_Float = Class(name="jPQL_Float")
jPQL_StringLiteral = Class(name="jPQL_StringLiteral")
jPQL_ExpressionTerm = Class(name="jPQL_ExpressionTerm")
OrderBySpec = Class(name="OrderBySpec")
Variable = Class(name="Variable")
jPQL_ParameterExpression = Class(name="jPQL_ParameterExpression")
jPQL_FunctionExpression = Class(name="jPQL_FunctionExpression")
jPQL_IntegerLiteral = Class(name="jPQL_IntegerLiteral")
Literal = Class(name="Literal")
jPQL_FloatLiteral = Class(name="jPQL_FloatLiteral")
jPQL_AndExpression = Class(name="jPQL_AndExpression")
jPQL_NullLiteral = Class(name="jPQL_NullLiteral")
jPQL_BooleanLiteral = Class(name="jPQL_BooleanLiteral")
jPQL_OrExpression = Class(name="jPQL_OrExpression")
jPQL_ComparisonOperatorExpression = Class(name="jPQL_ComparisonOperatorExpression")
jPQL_AdditionExpression = Class(name="jPQL_AdditionExpression")
jPQL_MultiplicationExpression = Class(name="jPQL_MultiplicationExpression")

# jPQL_JPQLQuery class attributes and methods

# jPQL_SetClause class attributes and methods

# jPQL_FromEntry class attributes and methods

# jPQL_UpdateItem class attributes and methods

# jPQL_WhereClause class attributes and methods

# jPQL_SelectStatement class attributes and methods

# JPQLQuery class attributes and methods

# ExpressionTerm class attributes and methods

# jPQL_SelectClause class attributes and methods
jPQL_SelectClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jPQL_SelectClause.attributes={jPQL_SelectClause_isDistinct}

# jPQL_FromClause class attributes and methods

# jPQL_GroupByClause class attributes and methods

# jPQL_OrderByClause class attributes and methods

# jPQL_AliasAttributeExpression class attributes and methods
jPQL_AliasAttributeExpression_direction: Property = Property(name="direction", type=StringType)
jPQL_AliasAttributeExpression_attributes: Property = Property(name="attributes", type=StringType)
jPQL_AliasAttributeExpression.attributes={jPQL_AliasAttributeExpression_attributes, jPQL_AliasAttributeExpression_direction}

# jPQL_HavingClause class attributes and methods

# jPQL_Expression class attributes and methods
jPQL_Expression_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
jPQL_Expression_isNot: Property = Property(name="isNot", type=BooleanType)
jPQL_Expression.attributes={jPQL_Expression_isNot, jPQL_Expression_unaryOperator}

# jPQL_OrderBySpec class attributes and methods

# jPQL_UpdateStatement class attributes and methods

# jPQL_UpdateClause class attributes and methods

# jPQL_VariableDeclaration class attributes and methods
jPQL_VariableDeclaration_name: Property = Property(name="name", type=StringType)
jPQL_VariableDeclaration.attributes={jPQL_VariableDeclaration_name}

# jPQL_FromClass class attributes and methods
jPQL_FromClass_type: Property = Property(name="type", type=StringType)
jPQL_FromClass.attributes={jPQL_FromClass_type}

# FromEntry class attributes and methods

# jPQL_Literal class attributes and methods

# jPQL_DeleteStatement class attributes and methods

# jPQL_DeleteClause class attributes and methods

# jPQL_SelectExpression class attributes and methods

# jPQL_SelectAggregateExpression class attributes and methods
jPQL_SelectAggregateExpression_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jPQL_SelectAggregateExpression.attributes={jPQL_SelectAggregateExpression_isDistinct}

# SelectExpression class attributes and methods

# jPQL_AvgAggregate class attributes and methods

# SelectAggregateExpression class attributes and methods

# jPQL_CountAggregate class attributes and methods

# jPQL_MaxAggregate class attributes and methods

# jPQL_MinAggregate class attributes and methods

# jPQL_SumAggregate class attributes and methods

# jPQL_SelectConstructorExpression class attributes and methods
jPQL_SelectConstructorExpression_name: Property = Property(name="name", type=StringType)
jPQL_SelectConstructorExpression.attributes={jPQL_SelectConstructorExpression_name}

# Expression class attributes and methods

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

# jPQL_Variable class attributes and methods

# jPQL_Float class attributes and methods
jPQL_Float_integerValue: Property = Property(name="integerValue", type=IntegerType)
jPQL_Float_fractionValue: Property = Property(name="fractionValue", type=IntegerType)
jPQL_Float.attributes={jPQL_Float_fractionValue, jPQL_Float_integerValue}

# jPQL_StringLiteral class attributes and methods
jPQL_StringLiteral_value: Property = Property(name="value", type=StringType)
jPQL_StringLiteral.attributes={jPQL_StringLiteral_value}

# jPQL_ExpressionTerm class attributes and methods

# OrderBySpec class attributes and methods

# Variable class attributes and methods

# jPQL_ParameterExpression class attributes and methods
jPQL_ParameterExpression_name: Property = Property(name="name", type=StringType)
jPQL_ParameterExpression_index: Property = Property(name="index", type=IntegerType)
jPQL_ParameterExpression.attributes={jPQL_ParameterExpression_index, jPQL_ParameterExpression_name}

# jPQL_FunctionExpression class attributes and methods
jPQL_FunctionExpression_name: Property = Property(name="name", type=StringType)
jPQL_FunctionExpression_trimSpec: Property = Property(name="trimSpec", type=StringType)
jPQL_FunctionExpression.attributes={jPQL_FunctionExpression_trimSpec, jPQL_FunctionExpression_name}

# jPQL_IntegerLiteral class attributes and methods
jPQL_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
jPQL_IntegerLiteral.attributes={jPQL_IntegerLiteral_value}

# Literal class attributes and methods

# jPQL_FloatLiteral class attributes and methods

# jPQL_AndExpression class attributes and methods

# jPQL_NullLiteral class attributes and methods
jPQL_NullLiteral_value: Property = Property(name="value", type=StringType)
jPQL_NullLiteral.attributes={jPQL_NullLiteral_value}

# jPQL_BooleanLiteral class attributes and methods
jPQL_BooleanLiteral_value: Property = Property(name="value", type=StringType)
jPQL_BooleanLiteral.attributes={jPQL_BooleanLiteral_value}

# jPQL_OrExpression class attributes and methods

# jPQL_ComparisonOperatorExpression class attributes and methods
jPQL_ComparisonOperatorExpression_operator: Property = Property(name="operator", type=StringType)
jPQL_ComparisonOperatorExpression.attributes={jPQL_ComparisonOperatorExpression_operator}

# jPQL_AdditionExpression class attributes and methods
jPQL_AdditionExpression_operator: Property = Property(name="operator", type=StringType)
jPQL_AdditionExpression.attributes={jPQL_AdditionExpression_operator}

# jPQL_MultiplicationExpression class attributes and methods
jPQL_MultiplicationExpression_operator: Property = Property(name="operator", type=StringType)
jPQL_MultiplicationExpression.attributes={jPQL_MultiplicationExpression_operator}

# Relationships
setClause17: BinaryAssociation = BinaryAssociation(
    name="setClause17",
    ends={
        Property(name="jPQL_SetClause", type=jPQL_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateStatement18", type=jPQL_SetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromEntries19: BinaryAssociation = BinaryAssociation(
    name="fromEntries19",
    ends={
        Property(name="jPQL_FromEntry", type=jPQL_UpdateClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateClause20", type=jPQL_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereClause0: BinaryAssociation = BinaryAssociation(
    name="whereClause0",
    ends={
        Property(name="jPQL_WhereClause", type=jPQL_JPQLQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_JPQLQuery", type=jPQL_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectClause1: BinaryAssociation = BinaryAssociation(
    name="selectClause1",
    ends={
        Property(name="jPQL_SelectClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement", type=jPQL_SelectClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause2: BinaryAssociation = BinaryAssociation(
    name="fromClause2",
    ends={
        Property(name="jPQL_FromClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement3", type=jPQL_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByClause4: BinaryAssociation = BinaryAssociation(
    name="groupByClause4",
    ends={
        Property(name="jPQL_GroupByClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement5", type=jPQL_GroupByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderByClause6: BinaryAssociation = BinaryAssociation(
    name="orderByClause6",
    ends={
        Property(name="jPQL_OrderByClause", type=jPQL_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectStatement7", type=jPQL_OrderByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
grouping8: BinaryAssociation = BinaryAssociation(
    name="grouping8",
    ends={
        Property(name="jPQL_AliasAttributeExpression", type=jPQL_GroupByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_GroupByClause9", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
havingClause10: BinaryAssociation = BinaryAssociation(
    name="havingClause10",
    ends={
        Property(name="jPQL_HavingClause", type=jPQL_GroupByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_GroupByClause11", type=jPQL_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having12: BinaryAssociation = BinaryAssociation(
    name="having12",
    ends={
        Property(name="jPQL_Expression", type=jPQL_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_HavingClause13", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering14: BinaryAssociation = BinaryAssociation(
    name="ordering14",
    ends={
        Property(name="jPQL_OrderBySpec", type=jPQL_OrderByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OrderByClause15", type=jPQL_OrderBySpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updateClause16: BinaryAssociation = BinaryAssociation(
    name="updateClause16",
    ends={
        Property(name="jPQL_UpdateClause", type=jPQL_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateStatement", type=jPQL_UpdateClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromEntries38: BinaryAssociation = BinaryAssociation(
    name="fromEntries38",
    ends={
        Property(name="jPQL_FromEntry40", type=jPQL_FromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromClause39", type=jPQL_FromEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable41: BinaryAssociation = BinaryAssociation(
    name="variable41",
    ends={
        Property(name="jPQL_VariableDeclaration", type=jPQL_FromEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromEntry42", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items21: BinaryAssociation = BinaryAssociation(
    name="items21",
    ends={
        Property(name="jPQL_UpdateItem", type=jPQL_SetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SetClause22", type=jPQL_UpdateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias23: BinaryAssociation = BinaryAssociation(
    name="alias23",
    ends={
        Property(name="jPQL_AliasAttributeExpression25", type=jPQL_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateItem24", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="jPQL_Literal", type=jPQL_UpdateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_UpdateItem27", type=jPQL_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteClause28: BinaryAssociation = BinaryAssociation(
    name="deleteClause28",
    ends={
        Property(name="jPQL_DeleteClause", type=jPQL_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_DeleteStatement", type=jPQL_DeleteClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause29: BinaryAssociation = BinaryAssociation(
    name="fromClause29",
    ends={
        Property(name="jPQL_FromClause31", type=jPQL_DeleteClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_DeleteClause30", type=jPQL_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions32: BinaryAssociation = BinaryAssociation(
    name="expressions32",
    ends={
        Property(name="jPQL_SelectExpression", type=jPQL_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectClause33", type=jPQL_SelectExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item34: BinaryAssociation = BinaryAssociation(
    name="item34",
    ends={
        Property(name="jPQL_AliasAttributeExpression35", type=jPQL_SelectAggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectAggregateExpression", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items36: BinaryAssociation = BinaryAssociation(
    name="items36",
    ends={
        Property(name="jPQL_AliasAttributeExpression37", type=jPQL_SelectConstructorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_SelectConstructorExpression", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
min66: BinaryAssociation = BinaryAssociation(
    name="min66",
    ends={
        Property(name="jPQL_Literal68", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression67", type=jPQL_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max69: BinaryAssociation = BinaryAssociation(
    name="max69",
    ends={
        Property(name="jPQL_Literal71", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression70", type=jPQL_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joins43: BinaryAssociation = BinaryAssociation(
    name="joins43",
    ends={
        Property(name="jPQL_FromJoin", type=jPQL_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromClass", type=jPQL_FromJoin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path44: BinaryAssociation = BinaryAssociation(
    name="path44",
    ends={
        Property(name="jPQL_AliasAttributeExpression45", type=jPQL_FromCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromCollection", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path46: BinaryAssociation = BinaryAssociation(
    name="path46",
    ends={
        Property(name="jPQL_AliasAttributeExpression48", type=jPQL_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromJoin47", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable49: BinaryAssociation = BinaryAssociation(
    name="variable49",
    ends={
        Property(name="jPQL_VariableDeclaration51", type=jPQL_FromJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FromJoin50", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereEntry52: BinaryAssociation = BinaryAssociation(
    name="whereEntry52",
    ends={
        Property(name="jPQL_Expression54", type=jPQL_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_WhereClause53", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right56: BinaryAssociation = BinaryAssociation(
    name="right56",
    ends={
        Property(name="jPQL_Expression57", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression55", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left59: BinaryAssociation = BinaryAssociation(
    name="left59",
    ends={
        Property(name="jPQL_Expression60", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression58", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items61: BinaryAssociation = BinaryAssociation(
    name="items61",
    ends={
        Property(name="jPQL_Variable", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression62", type=jPQL_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query63: BinaryAssociation = BinaryAssociation(
    name="query63",
    ends={
        Property(name="jPQL_SelectStatement65", type=jPQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_Expression64", type=jPQL_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="jPQL_Float", type=jPQL_FloatLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FloatLiteral", type=jPQL_Float, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias72: BinaryAssociation = BinaryAssociation(
    name="alias72",
    ends={
        Property(name="jPQL_VariableDeclaration74", type=jPQL_AliasAttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AliasAttributeExpression73", type=jPQL_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
fields75: BinaryAssociation = BinaryAssociation(
    name="fields75",
    ends={
        Property(name="jPQL_Expression76", type=jPQL_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FunctionExpression", type=jPQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field77: BinaryAssociation = BinaryAssociation(
    name="field77",
    ends={
        Property(name="jPQL_Expression79", type=jPQL_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FunctionExpression78", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startPos80: BinaryAssociation = BinaryAssociation(
    name="startPos80",
    ends={
        Property(name="jPQL_Expression82", type=jPQL_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FunctionExpression81", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
length83: BinaryAssociation = BinaryAssociation(
    name="length83",
    ends={
        Property(name="jPQL_Expression85", type=jPQL_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FunctionExpression84", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trimChar86: BinaryAssociation = BinaryAssociation(
    name="trimChar86",
    ends={
        Property(name="jPQL_Expression88", type=jPQL_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_FunctionExpression87", type=jPQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries92: BinaryAssociation = BinaryAssociation(
    name="entries92",
    ends={
        Property(name="jPQL_Expression93", type=jPQL_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_AndExpression", type=jPQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries90: BinaryAssociation = BinaryAssociation(
    name="entries90",
    ends={
        Property(name="jPQL_Expression91", type=jPQL_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jPQL_OrExpression", type=jPQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jPQL_SelectStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jPQL_SelectStatement)
gen_jPQL_SelectStatement_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jPQL_SelectStatement)
gen_jPQL_UpdateStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jPQL_UpdateStatement)
gen_jPQL_FromClass_FromEntry = Generalization(general=FromEntry, specific=jPQL_FromClass)
gen_jPQL_DeleteStatement_JPQLQuery = Generalization(general=JPQLQuery, specific=jPQL_DeleteStatement)
gen_jPQL_SelectAggregateExpression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_SelectAggregateExpression)
gen_jPQL_AvgAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_AvgAggregate)
gen_jPQL_CountAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_CountAggregate)
gen_jPQL_MaxAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_MaxAggregate)
gen_jPQL_MinAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_MinAggregate)
gen_jPQL_SumAggregate_SelectAggregateExpression = Generalization(general=SelectAggregateExpression, specific=jPQL_SumAggregate)
gen_jPQL_SelectConstructorExpression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_SelectConstructorExpression)
gen_jPQL_Variable_Expression = Generalization(general=Expression, specific=jPQL_Variable)
gen_jPQL_Variable_ExpressionTerm = Generalization(general=ExpressionTerm, specific=jPQL_Variable)
gen_jPQL_FromCollection_FromEntry = Generalization(general=FromEntry, specific=jPQL_FromCollection)
gen_jPQL_Join_FromJoin = Generalization(general=FromJoin, specific=jPQL_Join)
gen_jPQL_LeftJoin_FromJoin = Generalization(general=FromJoin, specific=jPQL_LeftJoin)
gen_jPQL_InnerJoin_FromJoin = Generalization(general=FromJoin, specific=jPQL_InnerJoin)
gen_jPQL_Expression_SelectExpression = Generalization(general=SelectExpression, specific=jPQL_Expression)
gen_jPQL_StringLiteral_Literal = Generalization(general=Literal, specific=jPQL_StringLiteral)
gen_jPQL_ExpressionTerm_Expression = Generalization(general=Expression, specific=jPQL_ExpressionTerm)
gen_jPQL_AliasAttributeExpression_OrderBySpec = Generalization(general=OrderBySpec, specific=jPQL_AliasAttributeExpression)
gen_jPQL_AliasAttributeExpression_Variable = Generalization(general=Variable, specific=jPQL_AliasAttributeExpression)
gen_jPQL_ParameterExpression_Variable = Generalization(general=Variable, specific=jPQL_ParameterExpression)
gen_jPQL_FunctionExpression_Expression = Generalization(general=Expression, specific=jPQL_FunctionExpression)
gen_jPQL_Literal_Variable = Generalization(general=Variable, specific=jPQL_Literal)
gen_jPQL_IntegerLiteral_Literal = Generalization(general=Literal, specific=jPQL_IntegerLiteral)
gen_jPQL_FloatLiteral_Literal = Generalization(general=Literal, specific=jPQL_FloatLiteral)
gen_jPQL_AndExpression_Expression = Generalization(general=Expression, specific=jPQL_AndExpression)
gen_jPQL_NullLiteral_Literal = Generalization(general=Literal, specific=jPQL_NullLiteral)
gen_jPQL_BooleanLiteral_Literal = Generalization(general=Literal, specific=jPQL_BooleanLiteral)
gen_jPQL_OrExpression_Expression = Generalization(general=Expression, specific=jPQL_OrExpression)
gen_jPQL_ComparisonOperatorExpression_Expression = Generalization(general=Expression, specific=jPQL_ComparisonOperatorExpression)
gen_jPQL_AdditionExpression_Expression = Generalization(general=Expression, specific=jPQL_AdditionExpression)
gen_jPQL_MultiplicationExpression_Expression = Generalization(general=Expression, specific=jPQL_MultiplicationExpression)

# Domain Model
domain_model = DomainModel(
    name="jPQL",
    types={jPQL_JPQLQuery, jPQL_SetClause, jPQL_FromEntry, jPQL_UpdateItem, jPQL_WhereClause, jPQL_SelectStatement, JPQLQuery, ExpressionTerm, jPQL_SelectClause, jPQL_FromClause, jPQL_GroupByClause, jPQL_OrderByClause, jPQL_AliasAttributeExpression, jPQL_HavingClause, jPQL_Expression, jPQL_OrderBySpec, jPQL_UpdateStatement, jPQL_UpdateClause, jPQL_VariableDeclaration, jPQL_FromClass, FromEntry, jPQL_Literal, jPQL_DeleteStatement, jPQL_DeleteClause, jPQL_SelectExpression, jPQL_SelectAggregateExpression, SelectExpression, jPQL_AvgAggregate, SelectAggregateExpression, jPQL_CountAggregate, jPQL_MaxAggregate, jPQL_MinAggregate, jPQL_SumAggregate, jPQL_SelectConstructorExpression, Expression, jPQL_FromJoin, jPQL_FromCollection, jPQL_Join, FromJoin, jPQL_LeftJoin, jPQL_InnerJoin, jPQL_Variable, jPQL_Float, jPQL_StringLiteral, jPQL_ExpressionTerm, OrderBySpec, Variable, jPQL_ParameterExpression, jPQL_FunctionExpression, jPQL_IntegerLiteral, Literal, jPQL_FloatLiteral, jPQL_AndExpression, jPQL_NullLiteral, jPQL_BooleanLiteral, jPQL_OrExpression, jPQL_ComparisonOperatorExpression, jPQL_AdditionExpression, jPQL_MultiplicationExpression, OrderByDirection, TrimSpec, UnaryOperator, AdditionOperator, MultiplicationOperator, ComparisonOperator},
    associations={setClause17, fromEntries19, whereClause0, selectClause1, fromClause2, groupByClause4, orderByClause6, grouping8, havingClause10, having12, ordering14, updateClause16, fromEntries38, variable41, items21, alias23, value26, deleteClause28, fromClause29, expressions32, item34, items36, min66, max69, joins43, path44, path46, variable49, whereEntry52, right56, left59, items61, query63, value89, alias72, fields75, field77, startPos80, length83, trimChar86, entries92, entries90},
    generalizations={gen_jPQL_SelectStatement_JPQLQuery, gen_jPQL_SelectStatement_ExpressionTerm, gen_jPQL_UpdateStatement_JPQLQuery, gen_jPQL_FromClass_FromEntry, gen_jPQL_DeleteStatement_JPQLQuery, gen_jPQL_SelectAggregateExpression_SelectExpression, gen_jPQL_AvgAggregate_SelectAggregateExpression, gen_jPQL_CountAggregate_SelectAggregateExpression, gen_jPQL_MaxAggregate_SelectAggregateExpression, gen_jPQL_MinAggregate_SelectAggregateExpression, gen_jPQL_SumAggregate_SelectAggregateExpression, gen_jPQL_SelectConstructorExpression_SelectExpression, gen_jPQL_Variable_Expression, gen_jPQL_Variable_ExpressionTerm, gen_jPQL_FromCollection_FromEntry, gen_jPQL_Join_FromJoin, gen_jPQL_LeftJoin_FromJoin, gen_jPQL_InnerJoin_FromJoin, gen_jPQL_Expression_SelectExpression, gen_jPQL_StringLiteral_Literal, gen_jPQL_ExpressionTerm_Expression, gen_jPQL_AliasAttributeExpression_OrderBySpec, gen_jPQL_AliasAttributeExpression_Variable, gen_jPQL_ParameterExpression_Variable, gen_jPQL_FunctionExpression_Expression, gen_jPQL_Literal_Variable, gen_jPQL_IntegerLiteral_Literal, gen_jPQL_FloatLiteral_Literal, gen_jPQL_AndExpression_Expression, gen_jPQL_NullLiteral_Literal, gen_jPQL_BooleanLiteral_Literal, gen_jPQL_OrExpression_Expression, gen_jPQL_ComparisonOperatorExpression_Expression, gen_jPQL_AdditionExpression_Expression, gen_jPQL_MultiplicationExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
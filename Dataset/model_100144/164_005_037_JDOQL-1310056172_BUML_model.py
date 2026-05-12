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
			EnumerationLiteral(name="ascending"),
			EnumerationLiteral(name="desc"),
			EnumerationLiteral(name="descending")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="positive"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="bitwiseNot"),
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
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="modulo")
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
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="instanceof")
    }
)

# Classes
jDOQL_SubqueryFromClause = Class(name="jDOQL_SubqueryFromClause")
jDOQL_SingleStringJDOQL = Class(name="jDOQL_SingleStringJDOQL")
jDOQL_SelectClause = Class(name="jDOQL_SelectClause")
jDOQL_FromClause = Class(name="jDOQL_FromClause")
jDOQL_WhereClause = Class(name="jDOQL_WhereClause")
jDOQL_VariablesClause = Class(name="jDOQL_VariablesClause")
jDOQL_ParametersClause = Class(name="jDOQL_ParametersClause")
jDOQL_ImportClause = Class(name="jDOQL_ImportClause")
jDOQL_GroupByClause = Class(name="jDOQL_GroupByClause")
jDOQL_OrderByClause = Class(name="jDOQL_OrderByClause")
jDOQL_RangeClause = Class(name="jDOQL_RangeClause")
jDOQL_Subquery = Class(name="jDOQL_Subquery")
Expression = Class(name="Expression")
jDOQL_Alias = Class(name="jDOQL_Alias")
jDOQL_SubquerySelectClause = Class(name="jDOQL_SubquerySelectClause")
jDOQL_VariableDeclaration = Class(name="jDOQL_VariableDeclaration")
SubquerySelectClause = Class(name="SubquerySelectClause")
jDOQL_EObject = Class(name="jDOQL_EObject")
jDOQL_IntoClause = Class(name="jDOQL_IntoClause")
jDOQL_ResultClause = Class(name="jDOQL_ResultClause")
jDOQL_ResultSpec = Class(name="jDOQL_ResultSpec")
jDOQL_SubqueryResultClause = Class(name="jDOQL_SubqueryResultClause")
jDOQL_Expression = Class(name="jDOQL_Expression")
jDOQL_ResultNaming = Class(name="jDOQL_ResultNaming")
ResultSpec = Class(name="ResultSpec")
OrderBySpec = Class(name="OrderBySpec")
jDOQL_ParameterDeclaration = Class(name="jDOQL_ParameterDeclaration")
jDOQL_HavingClause = Class(name="jDOQL_HavingClause")
jDOQL_OrderBySpec = Class(name="jDOQL_OrderBySpec")
jDOQL_ConditionalAndExpression = Class(name="jDOQL_ConditionalAndExpression")
jDOQL_SimpleOrExpression = Class(name="jDOQL_SimpleOrExpression")
jDOQL_ConditionalOrExpression = Class(name="jDOQL_ConditionalOrExpression")
jDOQL_SimpleAndExpression = Class(name="jDOQL_SimpleAndExpression")
jDOQL_ComparisonOperatorExpression = Class(name="jDOQL_ComparisonOperatorExpression")
jDOQL_AdditionExpression = Class(name="jDOQL_AdditionExpression")
jDOQL_MultiplicationExpression = Class(name="jDOQL_MultiplicationExpression")
jDOQL_FieldAccessExpression = Class(name="jDOQL_FieldAccessExpression")

# jDOQL_SubqueryFromClause class attributes and methods
jDOQL_SubqueryFromClause_isExcludeSubclasses: Property = Property(name="isExcludeSubclasses", type=BooleanType)
jDOQL_SubqueryFromClause_candidateClassName: Property = Property(name="candidateClassName", type=StringType)
jDOQL_SubqueryFromClause.attributes={jDOQL_SubqueryFromClause_candidateClassName, jDOQL_SubqueryFromClause_isExcludeSubclasses}

# jDOQL_SingleStringJDOQL class attributes and methods

# jDOQL_SelectClause class attributes and methods
jDOQL_SelectClause_isUnique: Property = Property(name="isUnique", type=BooleanType)
jDOQL_SelectClause.attributes={jDOQL_SelectClause_isUnique}

# jDOQL_FromClause class attributes and methods
jDOQL_FromClause_candidateClassName: Property = Property(name="candidateClassName", type=StringType)
jDOQL_FromClause_isExcludeSubclasses: Property = Property(name="isExcludeSubclasses", type=BooleanType)
jDOQL_FromClause.attributes={jDOQL_FromClause_candidateClassName, jDOQL_FromClause_isExcludeSubclasses}

# jDOQL_WhereClause class attributes and methods

# jDOQL_VariablesClause class attributes and methods

# jDOQL_ParametersClause class attributes and methods

# jDOQL_ImportClause class attributes and methods
jDOQL_ImportClause_importDeclarations: Property = Property(name="importDeclarations", type=StringType)
jDOQL_ImportClause.attributes={jDOQL_ImportClause_importDeclarations}

# jDOQL_GroupByClause class attributes and methods

# jDOQL_OrderByClause class attributes and methods

# jDOQL_RangeClause class attributes and methods

# jDOQL_Subquery class attributes and methods

# Expression class attributes and methods

# jDOQL_Alias class attributes and methods
jDOQL_Alias_identifier: Property = Property(name="identifier", type=StringType)
jDOQL_Alias.attributes={jDOQL_Alias_identifier}

# jDOQL_SubquerySelectClause class attributes and methods

# jDOQL_VariableDeclaration class attributes and methods
jDOQL_VariableDeclaration_type: Property = Property(name="type", type=StringType)
jDOQL_VariableDeclaration_variableName: Property = Property(name="variableName", type=StringType)
jDOQL_VariableDeclaration.attributes={jDOQL_VariableDeclaration_type, jDOQL_VariableDeclaration_variableName}

# SubquerySelectClause class attributes and methods

# jDOQL_EObject class attributes and methods

# jDOQL_IntoClause class attributes and methods
jDOQL_IntoClause_resultClassName: Property = Property(name="resultClassName", type=StringType)
jDOQL_IntoClause.attributes={jDOQL_IntoClause_resultClassName}

# jDOQL_ResultClause class attributes and methods
jDOQL_ResultClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jDOQL_ResultClause.attributes={jDOQL_ResultClause_isDistinct}

# jDOQL_ResultSpec class attributes and methods

# jDOQL_SubqueryResultClause class attributes and methods
jDOQL_SubqueryResultClause_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jDOQL_SubqueryResultClause.attributes={jDOQL_SubqueryResultClause_isDistinct}

# jDOQL_Expression class attributes and methods
jDOQL_Expression_direction: Property = Property(name="direction", type=StringType)
jDOQL_Expression_castType: Property = Property(name="castType", type=StringType)
jDOQL_Expression_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
jDOQL_Expression_literal: Property = Property(name="literal", type=StringType)
jDOQL_Expression_this: Property = Property(name="this", type=StringType)
jDOQL_Expression_id: Property = Property(name="id", type=StringType)
jDOQL_Expression_parameterName: Property = Property(name="parameterName", type=StringType)
jDOQL_Expression_name: Property = Property(name="name", type=StringType)
jDOQL_Expression_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
jDOQL_Expression.attributes={jDOQL_Expression_this, jDOQL_Expression_isDistinct, jDOQL_Expression_unaryOperator, jDOQL_Expression_name, jDOQL_Expression_castType, jDOQL_Expression_parameterName, jDOQL_Expression_id, jDOQL_Expression_direction, jDOQL_Expression_literal}

# jDOQL_ResultNaming class attributes and methods
jDOQL_ResultNaming_identifier: Property = Property(name="identifier", type=StringType)
jDOQL_ResultNaming.attributes={jDOQL_ResultNaming_identifier}

# ResultSpec class attributes and methods

# OrderBySpec class attributes and methods

# jDOQL_ParameterDeclaration class attributes and methods
jDOQL_ParameterDeclaration_type: Property = Property(name="type", type=StringType)
jDOQL_ParameterDeclaration_declaredParameterName: Property = Property(name="declaredParameterName", type=StringType)
jDOQL_ParameterDeclaration.attributes={jDOQL_ParameterDeclaration_type, jDOQL_ParameterDeclaration_declaredParameterName}

# jDOQL_HavingClause class attributes and methods

# jDOQL_OrderBySpec class attributes and methods

# jDOQL_ConditionalAndExpression class attributes and methods

# jDOQL_SimpleOrExpression class attributes and methods

# jDOQL_ConditionalOrExpression class attributes and methods

# jDOQL_SimpleAndExpression class attributes and methods

# jDOQL_ComparisonOperatorExpression class attributes and methods
jDOQL_ComparisonOperatorExpression_operator: Property = Property(name="operator", type=StringType)
jDOQL_ComparisonOperatorExpression.attributes={jDOQL_ComparisonOperatorExpression_operator}

# jDOQL_AdditionExpression class attributes and methods
jDOQL_AdditionExpression_operator: Property = Property(name="operator", type=StringType)
jDOQL_AdditionExpression.attributes={jDOQL_AdditionExpression_operator}

# jDOQL_MultiplicationExpression class attributes and methods
jDOQL_MultiplicationExpression_operator: Property = Property(name="operator", type=StringType)
jDOQL_MultiplicationExpression.attributes={jDOQL_MultiplicationExpression_operator}

# jDOQL_FieldAccessExpression class attributes and methods

# Relationships
selectClause17: BinaryAssociation = BinaryAssociation(
    name="selectClause17",
    ends={
        Property(name="jDOQL_Subquery", type=jDOQL_SubquerySelectClause, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="jDOQL_SubquerySelectClause", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1))
    }
)
fromClause18: BinaryAssociation = BinaryAssociation(
    name="fromClause18",
    ends={
        Property(name="jDOQL_SubqueryFromClause", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Subquery19", type=jDOQL_SubqueryFromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause20: BinaryAssociation = BinaryAssociation(
    name="whereClause20",
    ends={
        Property(name="jDOQL_WhereClause22", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Subquery21", type=jDOQL_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variablesClause23: BinaryAssociation = BinaryAssociation(
    name="variablesClause23",
    ends={
        Property(name="jDOQL_VariablesClause25", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Subquery24", type=jDOQL_VariablesClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametersClause26: BinaryAssociation = BinaryAssociation(
    name="parametersClause26",
    ends={
        Property(name="jDOQL_ParametersClause28", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Subquery27", type=jDOQL_ParametersClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectClause0: BinaryAssociation = BinaryAssociation(
    name="selectClause0",
    ends={
        Property(name="jDOQL_SelectClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL", type=jDOQL_SelectClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromClause1: BinaryAssociation = BinaryAssociation(
    name="fromClause1",
    ends={
        Property(name="jDOQL_FromClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL2", type=jDOQL_FromClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause3: BinaryAssociation = BinaryAssociation(
    name="whereClause3",
    ends={
        Property(name="jDOQL_WhereClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL4", type=jDOQL_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variablesClause5: BinaryAssociation = BinaryAssociation(
    name="variablesClause5",
    ends={
        Property(name="jDOQL_VariablesClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL6", type=jDOQL_VariablesClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametersClause7: BinaryAssociation = BinaryAssociation(
    name="parametersClause7",
    ends={
        Property(name="jDOQL_ParametersClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL8", type=jDOQL_ParametersClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importClause9: BinaryAssociation = BinaryAssociation(
    name="importClause9",
    ends={
        Property(name="jDOQL_ImportClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL10", type=jDOQL_ImportClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByClause11: BinaryAssociation = BinaryAssociation(
    name="groupByClause11",
    ends={
        Property(name="jDOQL_GroupByClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL12", type=jDOQL_GroupByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderByClause13: BinaryAssociation = BinaryAssociation(
    name="orderByClause13",
    ends={
        Property(name="jDOQL_OrderByClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL14", type=jDOQL_OrderByClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangeClause15: BinaryAssociation = BinaryAssociation(
    name="rangeClause15",
    ends={
        Property(name="jDOQL_RangeClause", type=jDOQL_SingleStringJDOQL, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SingleStringJDOQL16", type=jDOQL_RangeClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias41: BinaryAssociation = BinaryAssociation(
    name="alias41",
    ends={
        Property(name="jDOQL_Alias", type=jDOQL_SubqueryFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SubqueryFromClause42", type=jDOQL_Alias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filter43: BinaryAssociation = BinaryAssociation(
    name="filter43",
    ends={
        Property(name="jDOQL_Expression45", type=jDOQL_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_WhereClause44", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarations46: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations46",
    ends={
        Property(name="jDOQL_VariableDeclaration", type=jDOQL_VariablesClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_VariablesClause47", type=jDOQL_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importClause29: BinaryAssociation = BinaryAssociation(
    name="importClause29",
    ends={
        Property(name="jDOQL_ImportClause31", type=jDOQL_Subquery, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Subquery30", type=jDOQL_ImportClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultClause32: BinaryAssociation = BinaryAssociation(
    name="resultClause32",
    ends={
        Property(name="jDOQL_EObject", type=jDOQL_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SelectClause33", type=jDOQL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intoClause34: BinaryAssociation = BinaryAssociation(
    name="intoClause34",
    ends={
        Property(name="jDOQL_IntoClause", type=jDOQL_SelectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SelectClause35", type=jDOQL_IntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSpecs36: BinaryAssociation = BinaryAssociation(
    name="resultSpecs36",
    ends={
        Property(name="jDOQL_ResultSpec", type=jDOQL_ResultClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_ResultClause", type=jDOQL_ResultSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultExpression37: BinaryAssociation = BinaryAssociation(
    name="resultExpression37",
    ends={
        Property(name="jDOQL_Expression", type=jDOQL_SubqueryResultClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SubqueryResultClause", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldAccessExpression38: BinaryAssociation = BinaryAssociation(
    name="fieldAccessExpression38",
    ends={
        Property(name="jDOQL_Expression40", type=jDOQL_SubqueryFromClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SubqueryFromClause39", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end63: BinaryAssociation = BinaryAssociation(
    name="end63",
    ends={
        Property(name="jDOQL_Expression65", type=jDOQL_RangeClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_RangeClause64", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultNaming66: BinaryAssociation = BinaryAssociation(
    name="resultNaming66",
    ends={
        Property(name="jDOQL_ResultNaming", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression67", type=jDOQL_ResultNaming, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="jDOQL_Expression70", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression68", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterDeclarations48: BinaryAssociation = BinaryAssociation(
    name="parameterDeclarations48",
    ends={
        Property(name="jDOQL_ParameterDeclaration", type=jDOQL_ParametersClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_ParametersClause49", type=jDOQL_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grouping50: BinaryAssociation = BinaryAssociation(
    name="grouping50",
    ends={
        Property(name="jDOQL_Expression52", type=jDOQL_GroupByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_GroupByClause51", type=jDOQL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
havingClause53: BinaryAssociation = BinaryAssociation(
    name="havingClause53",
    ends={
        Property(name="jDOQL_HavingClause", type=jDOQL_GroupByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_GroupByClause54", type=jDOQL_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having55: BinaryAssociation = BinaryAssociation(
    name="having55",
    ends={
        Property(name="jDOQL_Expression57", type=jDOQL_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_HavingClause56", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering58: BinaryAssociation = BinaryAssociation(
    name="ordering58",
    ends={
        Property(name="jDOQL_OrderBySpec", type=jDOQL_OrderByClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_OrderByClause59", type=jDOQL_OrderBySpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start60: BinaryAssociation = BinaryAssociation(
    name="start60",
    ends={
        Property(name="jDOQL_Expression62", type=jDOQL_RangeClause, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_RangeClause61", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value93: BinaryAssociation = BinaryAssociation(
    name="value93",
    ends={
        Property(name="jDOQL_Expression94", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression92", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index96: BinaryAssociation = BinaryAssociation(
    name="index96",
    ends={
        Property(name="jDOQL_Expression97", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression95", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
string99: BinaryAssociation = BinaryAssociation(
    name="string99",
    ends={
        Property(name="jDOQL_Expression100", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression98", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromIndex102: BinaryAssociation = BinaryAssociation(
    name="fromIndex102",
    ends={
        Property(name="jDOQL_Expression103", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression101", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method72: BinaryAssociation = BinaryAssociation(
    name="method72",
    ends={
        Property(name="jDOQL_Expression73", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression71", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
number75: BinaryAssociation = BinaryAssociation(
    name="number75",
    ends={
        Property(name="jDOQL_Expression76", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression74", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
persistable78: BinaryAssociation = BinaryAssociation(
    name="persistable78",
    ends={
        Property(name="jDOQL_Expression79", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression77", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateArgument81: BinaryAssociation = BinaryAssociation(
    name="aggregateArgument81",
    ends={
        Property(name="jDOQL_Expression82", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression80", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element84: BinaryAssociation = BinaryAssociation(
    name="element84",
    ends={
        Property(name="jDOQL_Expression85", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression83", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg87: BinaryAssociation = BinaryAssociation(
    name="arg87",
    ends={
        Property(name="jDOQL_Expression88", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression86", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key90: BinaryAssociation = BinaryAssociation(
    name="key90",
    ends={
        Property(name="jDOQL_Expression91", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression89", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="jDOQL_ConditionalOrExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="jDOQL_Expression117", type=jDOQL_ConditionalOrExpression, multiplicity=Multiplicity(1, 1))
    }
)
left118: BinaryAssociation = BinaryAssociation(
    name="left118",
    ends={
        Property(name="jDOQL_Expression119", type=jDOQL_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_ConditionalAndExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left120: BinaryAssociation = BinaryAssociation(
    name="left120",
    ends={
        Property(name="jDOQL_Expression121", type=jDOQL_SimpleOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SimpleOrExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
regex105: BinaryAssociation = BinaryAssociation(
    name="regex105",
    ends={
        Property(name="jDOQL_Expression106", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression104", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replacement108: BinaryAssociation = BinaryAssociation(
    name="replacement108",
    ends={
        Property(name="jDOQL_Expression109", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression107", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beginIndex111: BinaryAssociation = BinaryAssociation(
    name="beginIndex111",
    ends={
        Property(name="jDOQL_Expression112", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression110", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endIndex114: BinaryAssociation = BinaryAssociation(
    name="endIndex114",
    ends={
        Property(name="jDOQL_Expression115", type=jDOQL_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_Expression113", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left122: BinaryAssociation = BinaryAssociation(
    name="left122",
    ends={
        Property(name="jDOQL_Expression123", type=jDOQL_SimpleAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_SimpleAndExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left124: BinaryAssociation = BinaryAssociation(
    name="left124",
    ends={
        Property(name="jDOQL_Expression125", type=jDOQL_ComparisonOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_ComparisonOperatorExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="jDOQL_Expression127", type=jDOQL_AdditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_AdditionExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left128: BinaryAssociation = BinaryAssociation(
    name="left128",
    ends={
        Property(name="jDOQL_Expression129", type=jDOQL_MultiplicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_MultiplicationExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left130: BinaryAssociation = BinaryAssociation(
    name="left130",
    ends={
        Property(name="jDOQL_Expression131", type=jDOQL_FieldAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jDOQL_FieldAccessExpression", type=jDOQL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_jDOQL_Subquery_Expression = Generalization(general=Expression, specific=jDOQL_Subquery)
gen_jDOQL_SelectClause_SubquerySelectClause = Generalization(general=SubquerySelectClause, specific=jDOQL_SelectClause)
gen_jDOQL_Expression_ResultSpec = Generalization(general=ResultSpec, specific=jDOQL_Expression)
gen_jDOQL_Expression_OrderBySpec = Generalization(general=OrderBySpec, specific=jDOQL_Expression)
gen_jDOQL_ConditionalAndExpression_Expression = Generalization(general=Expression, specific=jDOQL_ConditionalAndExpression)
gen_jDOQL_SimpleOrExpression_Expression = Generalization(general=Expression, specific=jDOQL_SimpleOrExpression)
gen_jDOQL_ConditionalOrExpression_Expression = Generalization(general=Expression, specific=jDOQL_ConditionalOrExpression)
gen_jDOQL_SimpleAndExpression_Expression = Generalization(general=Expression, specific=jDOQL_SimpleAndExpression)
gen_jDOQL_ComparisonOperatorExpression_Expression = Generalization(general=Expression, specific=jDOQL_ComparisonOperatorExpression)
gen_jDOQL_AdditionExpression_Expression = Generalization(general=Expression, specific=jDOQL_AdditionExpression)
gen_jDOQL_MultiplicationExpression_Expression = Generalization(general=Expression, specific=jDOQL_MultiplicationExpression)
gen_jDOQL_FieldAccessExpression_Expression = Generalization(general=Expression, specific=jDOQL_FieldAccessExpression)

# Domain Model
domain_model = DomainModel(
    name="jDOQL",
    types={jDOQL_SubqueryFromClause, jDOQL_SingleStringJDOQL, jDOQL_SelectClause, jDOQL_FromClause, jDOQL_WhereClause, jDOQL_VariablesClause, jDOQL_ParametersClause, jDOQL_ImportClause, jDOQL_GroupByClause, jDOQL_OrderByClause, jDOQL_RangeClause, jDOQL_Subquery, Expression, jDOQL_Alias, jDOQL_SubquerySelectClause, jDOQL_VariableDeclaration, SubquerySelectClause, jDOQL_EObject, jDOQL_IntoClause, jDOQL_ResultClause, jDOQL_ResultSpec, jDOQL_SubqueryResultClause, jDOQL_Expression, jDOQL_ResultNaming, ResultSpec, OrderBySpec, jDOQL_ParameterDeclaration, jDOQL_HavingClause, jDOQL_OrderBySpec, jDOQL_ConditionalAndExpression, jDOQL_SimpleOrExpression, jDOQL_ConditionalOrExpression, jDOQL_SimpleAndExpression, jDOQL_ComparisonOperatorExpression, jDOQL_AdditionExpression, jDOQL_MultiplicationExpression, jDOQL_FieldAccessExpression, OrderByDirection, UnaryOperator, AdditionOperator, MultiplicationOperator, ComparisonOperator},
    associations={selectClause17, fromClause18, whereClause20, variablesClause23, parametersClause26, selectClause0, fromClause1, whereClause3, variablesClause5, parametersClause7, importClause9, groupByClause11, orderByClause13, rangeClause15, alias41, filter43, variableDeclarations46, importClause29, resultClause32, intoClause34, resultSpecs36, resultExpression37, fieldAccessExpression38, end63, resultNaming66, right69, parameterDeclarations48, grouping50, havingClause53, having55, ordering58, start60, value93, index96, string99, fromIndex102, method72, number75, persistable78, aggregateArgument81, element84, arg87, key90, left116, left118, left120, regex105, replacement108, beginIndex111, endIndex114, left122, left124, left126, left128, left130},
    generalizations={gen_jDOQL_Subquery_Expression, gen_jDOQL_SelectClause_SubquerySelectClause, gen_jDOQL_Expression_ResultSpec, gen_jDOQL_Expression_OrderBySpec, gen_jDOQL_ConditionalAndExpression_Expression, gen_jDOQL_SimpleOrExpression_Expression, gen_jDOQL_ConditionalOrExpression_Expression, gen_jDOQL_SimpleAndExpression_Expression, gen_jDOQL_ComparisonOperatorExpression_Expression, gen_jDOQL_AdditionExpression_Expression, gen_jDOQL_MultiplicationExpression_Expression, gen_jDOQL_FieldAccessExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
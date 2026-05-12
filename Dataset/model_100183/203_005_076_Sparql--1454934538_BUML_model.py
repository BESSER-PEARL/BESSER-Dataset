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
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="sum"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="sub"),
			EnumerationLiteral(name="multiplicity")
    }
)

# Classes
sparql_SPARQLQuery = Class(name="sparql_SPARQLQuery")
sparql_Prefix = Class(name="sparql_Prefix")
sparql_Base = Class(name="sparql_Base")
sparql_IRI = Class(name="sparql_IRI")
sparql_SelectionQuery = Class(name="sparql_SelectionQuery")
SPARQLQuery = Class(name="SPARQLQuery")
sparql_DatasetClause = Class(name="sparql_DatasetClause")
sparql_WhereClause = Class(name="sparql_WhereClause")
sparql_GroupClause = Class(name="sparql_GroupClause")
sparql_HavingClause = Class(name="sparql_HavingClause")
sparql_LimitClause = Class(name="sparql_LimitClause")
sparql_SelectQuery = Class(name="sparql_SelectQuery")
SelectionQuery = Class(name="SelectionQuery")
sparql_Variable = Class(name="sparql_Variable")
sparql_AskQuery = Class(name="sparql_AskQuery")
sparql_DescribeQuery = Class(name="sparql_DescribeQuery")
sparql_GraphNode = Class(name="sparql_GraphNode")
sparql_ConstructQuery = Class(name="sparql_ConstructQuery")
sparql_GroupGraphPattern = Class(name="sparql_GroupGraphPattern")
sparql_UpdateQuery = Class(name="sparql_UpdateQuery")
sparql_UpdateOperation = Class(name="sparql_UpdateOperation")
sparql_ModifyQuery = Class(name="sparql_ModifyQuery")
UpdateOperation = Class(name="UpdateOperation")
sparql_CreateGraphQuery = Class(name="sparql_CreateGraphQuery")
sparql_DropGraphQuery = Class(name="sparql_DropGraphQuery")
sparql_LoadGraphQuery = Class(name="sparql_LoadGraphQuery")
sparql_ClearGraphQuery = Class(name="sparql_ClearGraphQuery")
sparql_UsingGraph = Class(name="sparql_UsingGraph")
sparql_InsertQuery = Class(name="sparql_InsertQuery")
ModifyQuery = Class(name="ModifyQuery")
sparql_InsertDataQuery = Class(name="sparql_InsertDataQuery")
sparql_DeleteQuery = Class(name="sparql_DeleteQuery")
sparql_DeleteDataQuery = Class(name="sparql_DeleteDataQuery")
sparql_DeleteWhereQuery = Class(name="sparql_DeleteWhereQuery")
sparql_DefaultDataSet = Class(name="sparql_DefaultDataSet")
DatasetClause = Class(name="DatasetClause")
sparql_NamedDataSet = Class(name="sparql_NamedDataSet")
sparql_ServiceDataSet = Class(name="sparql_ServiceDataSet")
sparql_GroupCondition = Class(name="sparql_GroupCondition")
sparql_Constraint = Class(name="sparql_Constraint")
sparql_SubSelectQuery = Class(name="sparql_SubSelectQuery")
GroupGraphPattern = Class(name="GroupGraphPattern")
sparql_GroupGraphPatternSub = Class(name="sparql_GroupGraphPatternSub")
sparql_GraphPattern = Class(name="sparql_GraphPattern")
sparql_PropertyList = Class(name="sparql_PropertyList")
sparql_GroupOrUnionGraphPattern = Class(name="sparql_GroupOrUnionGraphPattern")
sparql_OptionalGraphPattern = Class(name="sparql_OptionalGraphPattern")
sparql_TriplesSameSubject = Class(name="sparql_TriplesSameSubject")
GraphPattern = Class(name="GraphPattern")
sparql_GraphGraphPattern = Class(name="sparql_GraphGraphPattern")
sparql_ServiceGraphPattern = Class(name="sparql_ServiceGraphPattern")
sparql_FilterPattern = Class(name="sparql_FilterPattern")
sparql_Expression = Class(name="sparql_Expression")
sparql_NotExistsPattern = Class(name="sparql_NotExistsPattern")
sparql_MinusPattern = Class(name="sparql_MinusPattern")
Constraint = Class(name="Constraint")
sparql_ExpressionFilterExpression = Class(name="sparql_ExpressionFilterExpression")
Expression = Class(name="Expression")
sparql_FilterNode = Class(name="sparql_FilterNode")
sparql_ExistsPattern = Class(name="sparql_ExistsPattern")
sparql_Function = Class(name="sparql_Function")
GroupCondition = Class(name="GroupCondition")
FilterNode = Class(name="FilterNode")
sparql_NamedFunction = Class(name="sparql_NamedFunction")
Function = Class(name="Function")
sparql_SparqlFunction = Class(name="sparql_SparqlFunction")
sparql_BuiltInCall = Class(name="sparql_BuiltInCall")
sparql_Aggregate = Class(name="sparql_Aggregate")
GraphNode = Class(name="GraphNode")
sparql_UnNamedVariable = Class(name="sparql_UnNamedVariable")
Variable = Class(name="Variable")
sparql_NamedVariable = Class(name="sparql_NamedVariable")
sparql_ExprAggArg = Class(name="sparql_ExprAggArg")
sparql_BlankNode = Class(name="sparql_BlankNode")
sparql_Parameter = Class(name="sparql_Parameter")
sparql_Value = Class(name="sparql_Value")
sparql_RDFTag = Class(name="sparql_RDFTag")
sparql_StringValue = Class(name="sparql_StringValue")
Value = Class(name="Value")
sparql_TypeTag = Class(name="sparql_TypeTag")
RDFTag = Class(name="RDFTag")
sparql_LangTag = Class(name="sparql_LangTag")
sparql_OrFilterExpression = Class(name="sparql_OrFilterExpression")
sparql_AndFilterExpression = Class(name="sparql_AndFilterExpression")
sparql_IntegerValue = Class(name="sparql_IntegerValue")
sparql_CountAggregate = Class(name="sparql_CountAggregate")
Aggregate = Class(name="Aggregate")
sparql_SumAggregate = Class(name="sparql_SumAggregate")
sparql_MinAgregate = Class(name="sparql_MinAgregate")
sparql_AvgAggregate = Class(name="sparql_AvgAggregate")
sparql_SampleAggregate = Class(name="sparql_SampleAggregate")
sparql_GroupAggregate = Class(name="sparql_GroupAggregate")
sparql_MaxAggregate = Class(name="sparql_MaxAggregate")

# sparql_SPARQLQuery class attributes and methods

# sparql_Prefix class attributes and methods
sparql_Prefix_iref: Property = Property(name="iref", type=StringType)
sparql_Prefix_name: Property = Property(name="name", type=StringType)
sparql_Prefix.attributes={sparql_Prefix_name, sparql_Prefix_iref}

# sparql_Base class attributes and methods

# sparql_IRI class attributes and methods
sparql_IRI_value: Property = Property(name="value", type=StringType)
sparql_IRI.attributes={sparql_IRI_value}

# sparql_SelectionQuery class attributes and methods

# SPARQLQuery class attributes and methods

# sparql_DatasetClause class attributes and methods

# sparql_WhereClause class attributes and methods

# sparql_GroupClause class attributes and methods

# sparql_HavingClause class attributes and methods

# sparql_LimitClause class attributes and methods
sparql_LimitClause_limit: Property = Property(name="limit", type=IntegerType)
sparql_LimitClause.attributes={sparql_LimitClause_limit}

# sparql_SelectQuery class attributes and methods
sparql_SelectQuery_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
sparql_SelectQuery_isReduced: Property = Property(name="isReduced", type=BooleanType)
sparql_SelectQuery_all: Property = Property(name="all", type=BooleanType)
sparql_SelectQuery.attributes={sparql_SelectQuery_isReduced, sparql_SelectQuery_isDistinct, sparql_SelectQuery_all}

# SelectionQuery class attributes and methods

# sparql_Variable class attributes and methods
sparql_Variable_name: Property = Property(name="name", type=StringType)
sparql_Variable.attributes={sparql_Variable_name}

# sparql_AskQuery class attributes and methods

# sparql_DescribeQuery class attributes and methods

# sparql_GraphNode class attributes and methods

# sparql_ConstructQuery class attributes and methods

# sparql_GroupGraphPattern class attributes and methods

# sparql_UpdateQuery class attributes and methods

# sparql_UpdateOperation class attributes and methods

# sparql_ModifyQuery class attributes and methods
sparql_ModifyQuery_withGraph: Property = Property(name="withGraph", type=StringType)
sparql_ModifyQuery.attributes={sparql_ModifyQuery_withGraph}

# UpdateOperation class attributes and methods

# sparql_CreateGraphQuery class attributes and methods
sparql_CreateGraphQuery_isSilent: Property = Property(name="isSilent", type=StringType)
sparql_CreateGraphQuery_graph: Property = Property(name="graph", type=StringType)
sparql_CreateGraphQuery.attributes={sparql_CreateGraphQuery_graph, sparql_CreateGraphQuery_isSilent}

# sparql_DropGraphQuery class attributes and methods
sparql_DropGraphQuery_isSilent: Property = Property(name="isSilent", type=StringType)
sparql_DropGraphQuery_graph: Property = Property(name="graph", type=StringType)
sparql_DropGraphQuery.attributes={sparql_DropGraphQuery_isSilent, sparql_DropGraphQuery_graph}

# sparql_LoadGraphQuery class attributes and methods
sparql_LoadGraphQuery_intoGraph: Property = Property(name="intoGraph", type=StringType)
sparql_LoadGraphQuery_graph: Property = Property(name="graph", type=StringType)
sparql_LoadGraphQuery.attributes={sparql_LoadGraphQuery_graph, sparql_LoadGraphQuery_intoGraph}

# sparql_ClearGraphQuery class attributes and methods
sparql_ClearGraphQuery_uri: Property = Property(name="uri", type=StringType)
sparql_ClearGraphQuery_isDefault: Property = Property(name="isDefault", type=BooleanType)
sparql_ClearGraphQuery.attributes={sparql_ClearGraphQuery_uri, sparql_ClearGraphQuery_isDefault}

# sparql_UsingGraph class attributes and methods
sparql_UsingGraph_named: Property = Property(name="named", type=BooleanType)
sparql_UsingGraph_uri: Property = Property(name="uri", type=StringType)
sparql_UsingGraph.attributes={sparql_UsingGraph_uri, sparql_UsingGraph_named}

# sparql_InsertQuery class attributes and methods
sparql_InsertQuery_graph: Property = Property(name="graph", type=StringType)
sparql_InsertQuery.attributes={sparql_InsertQuery_graph}

# ModifyQuery class attributes and methods

# sparql_InsertDataQuery class attributes and methods
sparql_InsertDataQuery_graph: Property = Property(name="graph", type=StringType)
sparql_InsertDataQuery.attributes={sparql_InsertDataQuery_graph}

# sparql_DeleteQuery class attributes and methods
sparql_DeleteQuery_graph: Property = Property(name="graph", type=StringType)
sparql_DeleteQuery.attributes={sparql_DeleteQuery_graph}

# sparql_DeleteDataQuery class attributes and methods
sparql_DeleteDataQuery_graph: Property = Property(name="graph", type=StringType)
sparql_DeleteDataQuery.attributes={sparql_DeleteDataQuery_graph}

# sparql_DeleteWhereQuery class attributes and methods

# sparql_DefaultDataSet class attributes and methods

# DatasetClause class attributes and methods

# sparql_NamedDataSet class attributes and methods

# sparql_ServiceDataSet class attributes and methods

# sparql_GroupCondition class attributes and methods

# sparql_Constraint class attributes and methods

# sparql_SubSelectQuery class attributes and methods

# GroupGraphPattern class attributes and methods

# sparql_GroupGraphPatternSub class attributes and methods

# sparql_GraphPattern class attributes and methods

# sparql_PropertyList class attributes and methods

# sparql_GroupOrUnionGraphPattern class attributes and methods

# sparql_OptionalGraphPattern class attributes and methods

# sparql_TriplesSameSubject class attributes and methods

# GraphPattern class attributes and methods

# sparql_GraphGraphPattern class attributes and methods

# sparql_ServiceGraphPattern class attributes and methods

# sparql_FilterPattern class attributes and methods

# sparql_Expression class attributes and methods

# sparql_NotExistsPattern class attributes and methods

# sparql_MinusPattern class attributes and methods

# Constraint class attributes and methods

# sparql_ExpressionFilterExpression class attributes and methods
sparql_ExpressionFilterExpression_operator: Property = Property(name="operator", type=StringType)
sparql_ExpressionFilterExpression.attributes={sparql_ExpressionFilterExpression_operator}

# Expression class attributes and methods

# sparql_FilterNode class attributes and methods

# sparql_ExistsPattern class attributes and methods

# sparql_Function class attributes and methods
sparql_Function_name: Property = Property(name="name", type=StringType)
sparql_Function.attributes={sparql_Function_name}

# GroupCondition class attributes and methods

# FilterNode class attributes and methods

# sparql_NamedFunction class attributes and methods

# Function class attributes and methods

# sparql_SparqlFunction class attributes and methods

# sparql_BuiltInCall class attributes and methods

# sparql_Aggregate class attributes and methods

# GraphNode class attributes and methods

# sparql_UnNamedVariable class attributes and methods

# Variable class attributes and methods

# sparql_NamedVariable class attributes and methods

# sparql_ExprAggArg class attributes and methods
sparql_ExprAggArg_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
sparql_ExprAggArg.attributes={sparql_ExprAggArg_isDistinct}

# sparql_BlankNode class attributes and methods
sparql_BlankNode_name: Property = Property(name="name", type=StringType)
sparql_BlankNode.attributes={sparql_BlankNode_name}

# sparql_Parameter class attributes and methods
sparql_Parameter_name: Property = Property(name="name", type=StringType)
sparql_Parameter.attributes={sparql_Parameter_name}

# sparql_Value class attributes and methods

# sparql_RDFTag class attributes and methods

# sparql_StringValue class attributes and methods
sparql_StringValue_value: Property = Property(name="value", type=StringType)
sparql_StringValue.attributes={sparql_StringValue_value}

# Value class attributes and methods

# sparql_TypeTag class attributes and methods

# RDFTag class attributes and methods

# sparql_LangTag class attributes and methods
sparql_LangTag_lang: Property = Property(name="lang", type=StringType)
sparql_LangTag.attributes={sparql_LangTag_lang}

# sparql_OrFilterExpression class attributes and methods

# sparql_AndFilterExpression class attributes and methods

# sparql_IntegerValue class attributes and methods
sparql_IntegerValue_value: Property = Property(name="value", type=IntegerType)
sparql_IntegerValue.attributes={sparql_IntegerValue_value}

# sparql_CountAggregate class attributes and methods
sparql_CountAggregate_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
sparql_CountAggregate_isAll: Property = Property(name="isAll", type=BooleanType)
sparql_CountAggregate.attributes={sparql_CountAggregate_isDistinct, sparql_CountAggregate_isAll}

# Aggregate class attributes and methods

# sparql_SumAggregate class attributes and methods

# sparql_MinAgregate class attributes and methods

# sparql_AvgAggregate class attributes and methods

# sparql_SampleAggregate class attributes and methods

# sparql_GroupAggregate class attributes and methods
sparql_GroupAggregate_isDistinct: Property = Property(name="isDistinct", type=BooleanType)
sparql_GroupAggregate_value: Property = Property(name="value", type=StringType)
sparql_GroupAggregate.attributes={sparql_GroupAggregate_value, sparql_GroupAggregate_isDistinct}

# sparql_MaxAggregate class attributes and methods

# Relationships
prefixes0: BinaryAssociation = BinaryAssociation(
    name="prefixes0",
    ends={
        Property(name="sparql_Prefix", type=sparql_SPARQLQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SPARQLQuery", type=sparql_Prefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iref1: BinaryAssociation = BinaryAssociation(
    name="iref1",
    ends={
        Property(name="sparql_IRI", type=sparql_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Base", type=sparql_IRI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base2: BinaryAssociation = BinaryAssociation(
    name="base2",
    ends={
        Property(name="sparql_Base3", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery", type=sparql_Base, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datasetClause4: BinaryAssociation = BinaryAssociation(
    name="datasetClause4",
    ends={
        Property(name="sparql_DatasetClause", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery5", type=sparql_DatasetClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereClause6: BinaryAssociation = BinaryAssociation(
    name="whereClause6",
    ends={
        Property(name="sparql_WhereClause", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery7", type=sparql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupClause8: BinaryAssociation = BinaryAssociation(
    name="groupClause8",
    ends={
        Property(name="sparql_GroupClause", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery9", type=sparql_GroupClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limitClause12: BinaryAssociation = BinaryAssociation(
    name="limitClause12",
    ends={
        Property(name="sparql_LimitClause", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery13", type=sparql_LimitClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables14: BinaryAssociation = BinaryAssociation(
    name="variables14",
    ends={
        Property(name="sparql_Variable", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectQuery", type=sparql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables15: BinaryAssociation = BinaryAssociation(
    name="variables15",
    ends={
        Property(name="sparql_GraphNode", type=sparql_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DescribeQuery", type=sparql_GraphNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
havingClause10: BinaryAssociation = BinaryAssociation(
    name="havingClause10",
    ends={
        Property(name="sparql_HavingClause", type=sparql_SelectionQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectionQuery11", type=sparql_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations17: BinaryAssociation = BinaryAssociation(
    name="operations17",
    ends={
        Property(name="sparql_UpdateOperation", type=sparql_UpdateQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_UpdateQuery", type=sparql_UpdateOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern18: BinaryAssociation = BinaryAssociation(
    name="pattern18",
    ends={
        Property(name="sparql_GroupGraphPattern19", type=sparql_ModifyQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ModifyQuery", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructTemplate16: BinaryAssociation = BinaryAssociation(
    name="constructTemplate16",
    ends={
        Property(name="sparql_GroupGraphPattern", type=sparql_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructQuery", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause20: BinaryAssociation = BinaryAssociation(
    name="whereClause20",
    ends={
        Property(name="sparql_WhereClause21", type=sparql_InsertQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_InsertQuery", type=sparql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereClause24: BinaryAssociation = BinaryAssociation(
    name="whereClause24",
    ends={
        Property(name="sparql_WhereClause26", type=sparql_DeleteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DeleteQuery25", type=sparql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataSet27: BinaryAssociation = BinaryAssociation(
    name="dataSet27",
    ends={
        Property(name="sparql_IRI29", type=sparql_DatasetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DatasetClause28", type=sparql_IRI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertPattern22: BinaryAssociation = BinaryAssociation(
    name="insertPattern22",
    ends={
        Property(name="sparql_GroupGraphPattern23", type=sparql_DeleteQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DeleteQuery", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupGraphPattern30: BinaryAssociation = BinaryAssociation(
    name="groupGraphPattern30",
    ends={
        Property(name="sparql_GroupGraphPattern32", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_WhereClause31", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="sparql_GroupCondition", type=sparql_GroupClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupClause34", type=sparql_GroupCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint35: BinaryAssociation = BinaryAssociation(
    name="constraint35",
    ends={
        Property(name="sparql_Constraint", type=sparql_HavingClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_HavingClause36", type=sparql_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables37: BinaryAssociation = BinaryAssociation(
    name="variables37",
    ends={
        Property(name="sparql_Variable38", type=sparql_SubSelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SubSelectQuery", type=sparql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereClause39: BinaryAssociation = BinaryAssociation(
    name="whereClause39",
    ends={
        Property(name="sparql_WhereClause41", type=sparql_SubSelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SubSelectQuery40", type=sparql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupClause42: BinaryAssociation = BinaryAssociation(
    name="groupClause42",
    ends={
        Property(name="sparql_GroupClause44", type=sparql_SubSelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SubSelectQuery43", type=sparql_GroupClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
havingClause45: BinaryAssociation = BinaryAssociation(
    name="havingClause45",
    ends={
        Property(name="sparql_HavingClause47", type=sparql_SubSelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SubSelectQuery46", type=sparql_HavingClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphPatterns48: BinaryAssociation = BinaryAssociation(
    name="graphPatterns48",
    ends={
        Property(name="sparql_GraphPattern", type=sparql_GroupGraphPatternSub, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupGraphPatternSub", type=sparql_GraphPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject49: BinaryAssociation = BinaryAssociation(
    name="subject49",
    ends={
        Property(name="sparql_GraphNode50", type=sparql_TriplesSameSubject, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubject", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyList51: BinaryAssociation = BinaryAssociation(
    name="propertyList51",
    ends={
        Property(name="sparql_PropertyList", type=sparql_TriplesSameSubject, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubject52", type=sparql_PropertyList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphPatterns53: BinaryAssociation = BinaryAssociation(
    name="graphPatterns53",
    ends={
        Property(name="sparql_GroupGraphPattern54", type=sparql_GroupOrUnionGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupOrUnionGraphPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphPattern55: BinaryAssociation = BinaryAssociation(
    name="graphPattern55",
    ends={
        Property(name="sparql_GroupGraphPattern56", type=sparql_OptionalGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OptionalGraphPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property57: BinaryAssociation = BinaryAssociation(
    name="property57",
    ends={
        Property(name="sparql_GraphNode59", type=sparql_PropertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PropertyList58", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object60: BinaryAssociation = BinaryAssociation(
    name="object60",
    ends={
        Property(name="sparql_GraphNode62", type=sparql_PropertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PropertyList61", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var63: BinaryAssociation = BinaryAssociation(
    name="var63",
    ends={
        Property(name="sparql_GraphNode64", type=sparql_GraphGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GraphGraphPattern", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern65: BinaryAssociation = BinaryAssociation(
    name="pattern65",
    ends={
        Property(name="sparql_GroupGraphPattern67", type=sparql_GraphGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GraphGraphPattern66", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var68: BinaryAssociation = BinaryAssociation(
    name="var68",
    ends={
        Property(name="sparql_GraphNode69", type=sparql_ServiceGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ServiceGraphPattern", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern70: BinaryAssociation = BinaryAssociation(
    name="pattern70",
    ends={
        Property(name="sparql_GroupGraphPattern72", type=sparql_ServiceGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ServiceGraphPattern71", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression73: BinaryAssociation = BinaryAssociation(
    name="expression73",
    ends={
        Property(name="sparql_Expression", type=sparql_FilterPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_FilterPattern", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern74: BinaryAssociation = BinaryAssociation(
    name="pattern74",
    ends={
        Property(name="sparql_GroupGraphPattern75", type=sparql_ExistsPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ExistsPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern76: BinaryAssociation = BinaryAssociation(
    name="pattern76",
    ends={
        Property(name="sparql_GroupGraphPattern77", type=sparql_NotExistsPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NotExistsPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern78: BinaryAssociation = BinaryAssociation(
    name="pattern78",
    ends={
        Property(name="sparql_GroupGraphPattern79", type=sparql_MinusPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MinusPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="sparql_FilterNode", type=sparql_ExpressionFilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ExpressionFilterExpression", type=sparql_FilterNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="sparql_FilterNode83", type=sparql_ExpressionFilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ExpressionFilterExpression82", type=sparql_FilterNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters84: BinaryAssociation = BinaryAssociation(
    name="parameters84",
    ends={
        Property(name="sparql_Variable85", type=sparql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Function", type=sparql_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prefix86: BinaryAssociation = BinaryAssociation(
    name="prefix86",
    ends={
        Property(name="sparql_Prefix87", type=sparql_NamedFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NamedFunction", type=sparql_Prefix, multiplicity=Multiplicity(0, 1))
    }
)
expr88: BinaryAssociation = BinaryAssociation(
    name="expr88",
    ends={
        Property(name="sparql_BuiltInCall", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sparql_Expression89", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1))
    }
)
left90: BinaryAssociation = BinaryAssociation(
    name="left90",
    ends={
        Property(name="sparql_Expression92", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall91", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right93: BinaryAssociation = BinaryAssociation(
    name="right93",
    ends={
        Property(name="sparql_Expression95", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall94", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var96: BinaryAssociation = BinaryAssociation(
    name="var96",
    ends={
        Property(name="sparql_Variable98", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall97", type=sparql_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpr99: BinaryAssociation = BinaryAssociation(
    name="ifExpr99",
    ends={
        Property(name="sparql_Expression101", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall100", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpr102: BinaryAssociation = BinaryAssociation(
    name="thenExpr102",
    ends={
        Property(name="sparql_Expression104", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall103", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpr105: BinaryAssociation = BinaryAssociation(
    name="elseExpr105",
    ends={
        Property(name="sparql_Expression107", type=sparql_BuiltInCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BuiltInCall106", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr108: BinaryAssociation = BinaryAssociation(
    name="expr108",
    ends={
        Property(name="sparql_Expression109", type=sparql_ExprAggArg, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ExprAggArg", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag112: BinaryAssociation = BinaryAssociation(
    name="tag112",
    ends={
        Property(name="sparql_RDFTag", type=sparql_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Value", type=sparql_RDFTag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prefix110: BinaryAssociation = BinaryAssociation(
    name="prefix110",
    ends={
        Property(name="sparql_Prefix111", type=sparql_NamedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NamedVariable", type=sparql_Prefix, multiplicity=Multiplicity(0, 1))
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="sparql_GraphNode114", type=sparql_TypeTag, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TypeTag", type=sparql_GraphNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries115: BinaryAssociation = BinaryAssociation(
    name="entries115",
    ends={
        Property(name="sparql_Expression116", type=sparql_OrFilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OrFilterExpression", type=sparql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries117: BinaryAssociation = BinaryAssociation(
    name="entries117",
    ends={
        Property(name="sparql_Expression118", type=sparql_AndFilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AndFilterExpression", type=sparql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr119: BinaryAssociation = BinaryAssociation(
    name="expr119",
    ends={
        Property(name="sparql_Expression120", type=sparql_CountAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_CountAggregate", type=sparql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr121: BinaryAssociation = BinaryAssociation(
    name="expr121",
    ends={
        Property(name="sparql_ExprAggArg122", type=sparql_SumAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SumAggregate", type=sparql_ExprAggArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr123: BinaryAssociation = BinaryAssociation(
    name="expr123",
    ends={
        Property(name="sparql_ExprAggArg124", type=sparql_MinAgregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MinAgregate", type=sparql_ExprAggArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr125: BinaryAssociation = BinaryAssociation(
    name="expr125",
    ends={
        Property(name="sparql_ExprAggArg126", type=sparql_MaxAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MaxAggregate", type=sparql_ExprAggArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr127: BinaryAssociation = BinaryAssociation(
    name="expr127",
    ends={
        Property(name="sparql_ExprAggArg128", type=sparql_AvgAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AvgAggregate", type=sparql_ExprAggArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr129: BinaryAssociation = BinaryAssociation(
    name="expr129",
    ends={
        Property(name="sparql_ExprAggArg130", type=sparql_SampleAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SampleAggregate", type=sparql_ExprAggArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr131: BinaryAssociation = BinaryAssociation(
    name="expr131",
    ends={
        Property(name="sparql_Expression132", type=sparql_GroupAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupAggregate", type=sparql_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sparql_SelectionQuery_SPARQLQuery = Generalization(general=SPARQLQuery, specific=sparql_SelectionQuery)
gen_sparql_SelectQuery_SelectionQuery = Generalization(general=SelectionQuery, specific=sparql_SelectQuery)
gen_sparql_AskQuery_SelectionQuery = Generalization(general=SelectionQuery, specific=sparql_AskQuery)
gen_sparql_DescribeQuery_SelectionQuery = Generalization(general=SelectionQuery, specific=sparql_DescribeQuery)
gen_sparql_ConstructQuery_SelectionQuery = Generalization(general=SelectionQuery, specific=sparql_ConstructQuery)
gen_sparql_UpdateQuery_SPARQLQuery = Generalization(general=SPARQLQuery, specific=sparql_UpdateQuery)
gen_sparql_ModifyQuery_UpdateOperation = Generalization(general=UpdateOperation, specific=sparql_ModifyQuery)
gen_sparql_CreateGraphQuery_UpdateOperation = Generalization(general=UpdateOperation, specific=sparql_CreateGraphQuery)
gen_sparql_DropGraphQuery_UpdateOperation = Generalization(general=UpdateOperation, specific=sparql_DropGraphQuery)
gen_sparql_LoadGraphQuery_UpdateOperation = Generalization(general=UpdateOperation, specific=sparql_LoadGraphQuery)
gen_sparql_ClearGraphQuery_UpdateOperation = Generalization(general=UpdateOperation, specific=sparql_ClearGraphQuery)
gen_sparql_InsertQuery_ModifyQuery = Generalization(general=ModifyQuery, specific=sparql_InsertQuery)
gen_sparql_InsertDataQuery_ModifyQuery = Generalization(general=ModifyQuery, specific=sparql_InsertDataQuery)
gen_sparql_DeleteQuery_ModifyQuery = Generalization(general=ModifyQuery, specific=sparql_DeleteQuery)
gen_sparql_DeleteDataQuery_ModifyQuery = Generalization(general=ModifyQuery, specific=sparql_DeleteDataQuery)
gen_sparql_DeleteWhereQuery_ModifyQuery = Generalization(general=ModifyQuery, specific=sparql_DeleteWhereQuery)
gen_sparql_DefaultDataSet_DatasetClause = Generalization(general=DatasetClause, specific=sparql_DefaultDataSet)
gen_sparql_NamedDataSet_DatasetClause = Generalization(general=DatasetClause, specific=sparql_NamedDataSet)
gen_sparql_ServiceDataSet_DatasetClause = Generalization(general=DatasetClause, specific=sparql_ServiceDataSet)
gen_sparql_SubSelectQuery_GroupGraphPattern = Generalization(general=GroupGraphPattern, specific=sparql_SubSelectQuery)
gen_sparql_GroupGraphPatternSub_GroupGraphPattern = Generalization(general=GroupGraphPattern, specific=sparql_GroupGraphPatternSub)
gen_sparql_GroupOrUnionGraphPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_GroupOrUnionGraphPattern)
gen_sparql_OptionalGraphPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_OptionalGraphPattern)
gen_sparql_TriplesSameSubject_GraphPattern = Generalization(general=GraphPattern, specific=sparql_TriplesSameSubject)
gen_sparql_GraphGraphPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_GraphGraphPattern)
gen_sparql_ServiceGraphPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_ServiceGraphPattern)
gen_sparql_FilterPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_FilterPattern)
gen_sparql_NotExistsPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_NotExistsPattern)
gen_sparql_MinusPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_MinusPattern)
gen_sparql_Expression_Constraint = Generalization(general=Constraint, specific=sparql_Expression)
gen_sparql_ExpressionFilterExpression_Expression = Generalization(general=Expression, specific=sparql_ExpressionFilterExpression)
gen_sparql_ExistsPattern_GraphPattern = Generalization(general=GraphPattern, specific=sparql_ExistsPattern)
gen_sparql_Function_GroupCondition = Generalization(general=GroupCondition, specific=sparql_Function)
gen_sparql_Function_Constraint = Generalization(general=Constraint, specific=sparql_Function)
gen_sparql_Function_FilterNode = Generalization(general=FilterNode, specific=sparql_Function)
gen_sparql_NamedFunction_Function = Generalization(general=Function, specific=sparql_NamedFunction)
gen_sparql_SparqlFunction_Function = Generalization(general=Function, specific=sparql_SparqlFunction)
gen_sparql_BuiltInCall_GroupCondition = Generalization(general=GroupCondition, specific=sparql_BuiltInCall)
gen_sparql_BuiltInCall_Constraint = Generalization(general=Constraint, specific=sparql_BuiltInCall)
gen_sparql_GraphNode_FilterNode = Generalization(general=FilterNode, specific=sparql_GraphNode)
gen_sparql_Variable_GroupCondition = Generalization(general=GroupCondition, specific=sparql_Variable)
gen_sparql_Variable_GraphNode = Generalization(general=GraphNode, specific=sparql_Variable)
gen_sparql_UnNamedVariable_Variable = Generalization(general=Variable, specific=sparql_UnNamedVariable)
gen_sparql_NamedVariable_Variable = Generalization(general=Variable, specific=sparql_NamedVariable)
gen_sparql_BlankNode_GraphNode = Generalization(general=GraphNode, specific=sparql_BlankNode)
gen_sparql_Parameter_GraphNode = Generalization(general=GraphNode, specific=sparql_Parameter)
gen_sparql_Value_GraphNode = Generalization(general=GraphNode, specific=sparql_Value)
gen_sparql_IRI_GraphNode = Generalization(general=GraphNode, specific=sparql_IRI)
gen_sparql_StringValue_Value = Generalization(general=Value, specific=sparql_StringValue)
gen_sparql_TypeTag_RDFTag = Generalization(general=RDFTag, specific=sparql_TypeTag)
gen_sparql_LangTag_RDFTag = Generalization(general=RDFTag, specific=sparql_LangTag)
gen_sparql_OrFilterExpression_Expression = Generalization(general=Expression, specific=sparql_OrFilterExpression)
gen_sparql_AndFilterExpression_Expression = Generalization(general=Expression, specific=sparql_AndFilterExpression)
gen_sparql_IntegerValue_Value = Generalization(general=Value, specific=sparql_IntegerValue)
gen_sparql_CountAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_CountAggregate)
gen_sparql_SumAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_SumAggregate)
gen_sparql_MinAgregate_Aggregate = Generalization(general=Aggregate, specific=sparql_MinAgregate)
gen_sparql_AvgAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_AvgAggregate)
gen_sparql_SampleAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_SampleAggregate)
gen_sparql_GroupAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_GroupAggregate)
gen_sparql_MaxAggregate_Aggregate = Generalization(general=Aggregate, specific=sparql_MaxAggregate)

# Domain Model
domain_model = DomainModel(
    name="sparql",
    types={sparql_SPARQLQuery, sparql_Prefix, sparql_Base, sparql_IRI, sparql_SelectionQuery, SPARQLQuery, sparql_DatasetClause, sparql_WhereClause, sparql_GroupClause, sparql_HavingClause, sparql_LimitClause, sparql_SelectQuery, SelectionQuery, sparql_Variable, sparql_AskQuery, sparql_DescribeQuery, sparql_GraphNode, sparql_ConstructQuery, sparql_GroupGraphPattern, sparql_UpdateQuery, sparql_UpdateOperation, sparql_ModifyQuery, UpdateOperation, sparql_CreateGraphQuery, sparql_DropGraphQuery, sparql_LoadGraphQuery, sparql_ClearGraphQuery, sparql_UsingGraph, sparql_InsertQuery, ModifyQuery, sparql_InsertDataQuery, sparql_DeleteQuery, sparql_DeleteDataQuery, sparql_DeleteWhereQuery, sparql_DefaultDataSet, DatasetClause, sparql_NamedDataSet, sparql_ServiceDataSet, sparql_GroupCondition, sparql_Constraint, sparql_SubSelectQuery, GroupGraphPattern, sparql_GroupGraphPatternSub, sparql_GraphPattern, sparql_PropertyList, sparql_GroupOrUnionGraphPattern, sparql_OptionalGraphPattern, sparql_TriplesSameSubject, GraphPattern, sparql_GraphGraphPattern, sparql_ServiceGraphPattern, sparql_FilterPattern, sparql_Expression, sparql_NotExistsPattern, sparql_MinusPattern, Constraint, sparql_ExpressionFilterExpression, Expression, sparql_FilterNode, sparql_ExistsPattern, sparql_Function, GroupCondition, FilterNode, sparql_NamedFunction, Function, sparql_SparqlFunction, sparql_BuiltInCall, sparql_Aggregate, GraphNode, sparql_UnNamedVariable, Variable, sparql_NamedVariable, sparql_ExprAggArg, sparql_BlankNode, sparql_Parameter, sparql_Value, sparql_RDFTag, sparql_StringValue, Value, sparql_TypeTag, RDFTag, sparql_LangTag, sparql_OrFilterExpression, sparql_AndFilterExpression, sparql_IntegerValue, sparql_CountAggregate, Aggregate, sparql_SumAggregate, sparql_MinAgregate, sparql_AvgAggregate, sparql_SampleAggregate, sparql_GroupAggregate, sparql_MaxAggregate, Operator},
    associations={prefixes0, iref1, base2, datasetClause4, whereClause6, groupClause8, limitClause12, variables14, variables15, havingClause10, operations17, pattern18, constructTemplate16, whereClause20, whereClause24, dataSet27, insertPattern22, groupGraphPattern30, condition33, constraint35, variables37, whereClause39, groupClause42, havingClause45, graphPatterns48, subject49, propertyList51, graphPatterns53, graphPattern55, property57, object60, var63, pattern65, var68, pattern70, expression73, pattern74, pattern76, pattern78, left80, right81, parameters84, prefix86, expr88, left90, right93, var96, ifExpr99, thenExpr102, elseExpr105, expr108, tag112, prefix110, type113, entries115, entries117, expr119, expr121, expr123, expr125, expr127, expr129, expr131},
    generalizations={gen_sparql_SelectionQuery_SPARQLQuery, gen_sparql_SelectQuery_SelectionQuery, gen_sparql_AskQuery_SelectionQuery, gen_sparql_DescribeQuery_SelectionQuery, gen_sparql_ConstructQuery_SelectionQuery, gen_sparql_UpdateQuery_SPARQLQuery, gen_sparql_ModifyQuery_UpdateOperation, gen_sparql_CreateGraphQuery_UpdateOperation, gen_sparql_DropGraphQuery_UpdateOperation, gen_sparql_LoadGraphQuery_UpdateOperation, gen_sparql_ClearGraphQuery_UpdateOperation, gen_sparql_InsertQuery_ModifyQuery, gen_sparql_InsertDataQuery_ModifyQuery, gen_sparql_DeleteQuery_ModifyQuery, gen_sparql_DeleteDataQuery_ModifyQuery, gen_sparql_DeleteWhereQuery_ModifyQuery, gen_sparql_DefaultDataSet_DatasetClause, gen_sparql_NamedDataSet_DatasetClause, gen_sparql_ServiceDataSet_DatasetClause, gen_sparql_SubSelectQuery_GroupGraphPattern, gen_sparql_GroupGraphPatternSub_GroupGraphPattern, gen_sparql_GroupOrUnionGraphPattern_GraphPattern, gen_sparql_OptionalGraphPattern_GraphPattern, gen_sparql_TriplesSameSubject_GraphPattern, gen_sparql_GraphGraphPattern_GraphPattern, gen_sparql_ServiceGraphPattern_GraphPattern, gen_sparql_FilterPattern_GraphPattern, gen_sparql_NotExistsPattern_GraphPattern, gen_sparql_MinusPattern_GraphPattern, gen_sparql_Expression_Constraint, gen_sparql_ExpressionFilterExpression_Expression, gen_sparql_ExistsPattern_GraphPattern, gen_sparql_Function_GroupCondition, gen_sparql_Function_Constraint, gen_sparql_Function_FilterNode, gen_sparql_NamedFunction_Function, gen_sparql_SparqlFunction_Function, gen_sparql_BuiltInCall_GroupCondition, gen_sparql_BuiltInCall_Constraint, gen_sparql_GraphNode_FilterNode, gen_sparql_Variable_GroupCondition, gen_sparql_Variable_GraphNode, gen_sparql_UnNamedVariable_Variable, gen_sparql_NamedVariable_Variable, gen_sparql_BlankNode_GraphNode, gen_sparql_Parameter_GraphNode, gen_sparql_Value_GraphNode, gen_sparql_IRI_GraphNode, gen_sparql_StringValue_Value, gen_sparql_TypeTag_RDFTag, gen_sparql_LangTag_RDFTag, gen_sparql_OrFilterExpression_Expression, gen_sparql_AndFilterExpression_Expression, gen_sparql_IntegerValue_Value, gen_sparql_CountAggregate_Aggregate, gen_sparql_SumAggregate_Aggregate, gen_sparql_MinAgregate_Aggregate, gen_sparql_AvgAggregate_Aggregate, gen_sparql_SampleAggregate_Aggregate, gen_sparql_GroupAggregate_Aggregate, gen_sparql_MaxAggregate_Aggregate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
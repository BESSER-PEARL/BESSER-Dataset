import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphNode,
    sparql_Aggregate,
    Function,
    sparql_SparqlFunction,
    sparql_NamedFunction,
    FilterNode,
    GroupCondition,
    sparql_FilterNode,
    Expression,
    sparql_ExpressionFilterExpression,
    Constraint,
    sparql_BuiltInCall,
    sparql_Function,
    sparql_Expression,
    GraphPattern,
    sparql_FilterPattern,
    sparql_NotExistsPattern,
    sparql_MinusPattern,
    sparql_GraphGraphPattern,
    sparql_ServiceGraphPattern,
    sparql_ExistsPattern,
    sparql_TriplesSameSubject,
    sparql_OptionalGraphPattern,
    sparql_GroupOrUnionGraphPattern,
    sparql_PropertyList,
    sparql_GraphPattern,
    GroupGraphPattern,
    sparql_GroupGraphPatternSub,
    sparql_SubSelectQuery,
    sparql_Constraint,
    sparql_GroupCondition,
    DatasetClause,
    sparql_NamedDataSet,
    sparql_ServiceDataSet,
    sparql_DefaultDataSet,
    ModifyQuery,
    sparql_DeleteDataQuery,
    sparql_DeleteQuery,
    sparql_InsertDataQuery,
    sparql_DeleteWhereQuery,
    sparql_InsertQuery,
    sparql_UsingGraph,
    UpdateOperation,
    sparql_DropGraphQuery,
    sparql_CreateGraphQuery,
    sparql_ClearGraphQuery,
    sparql_LoadGraphQuery,
    sparql_ModifyQuery,
    sparql_UpdateOperation,
    sparql_GroupGraphPattern,
    sparql_GraphNode,
    sparql_Variable,
    SelectionQuery,
    sparql_DescribeQuery,
    sparql_AskQuery,
    sparql_ConstructQuery,
    sparql_SelectQuery,
    sparql_LimitClause,
    sparql_HavingClause,
    sparql_GroupClause,
    sparql_WhereClause,
    sparql_DatasetClause,
    SPARQLQuery,
    sparql_UpdateQuery,
    sparql_SelectionQuery,
    sparql_IRI,
    sparql_Base,
    sparql_Prefix,
    sparql_SPARQLQuery,
    Aggregate,
    sparql_SampleAggregate,
    sparql_SumAggregate,
    sparql_AvgAggregate,
    sparql_MaxAggregate,
    sparql_GroupAggregate,
    sparql_MinAgregate,
    sparql_CountAggregate,
    sparql_AndFilterExpression,
    sparql_OrFilterExpression,
    RDFTag,
    sparql_LangTag,
    sparql_TypeTag,
    Value,
    sparql_IntegerValue,
    sparql_StringValue,
    sparql_RDFTag,
    sparql_Value,
    sparql_Parameter,
    sparql_BlankNode,
    sparql_ExprAggArg,
    Variable,
    sparql_NamedVariable,
    sparql_UnNamedVariable,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_aggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_Aggregate)


def test_sparql_aggregate_constructor_exists():
    assert callable(sparql_Aggregate.__init__)


def test_sparql_aggregate_constructor_args():
    sig = inspect.signature(sparql_Aggregate.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sparqlfunction_is_not_abstract():
    assert not inspect.isabstract(sparql_SparqlFunction)


def test_sparql_sparqlfunction_constructor_exists():
    assert callable(sparql_SparqlFunction.__init__)


def test_sparql_sparqlfunction_constructor_args():
    sig = inspect.signature(sparql_SparqlFunction.__init__)
    params = list(sig.parameters.keys())



def test_sparql_namedfunction_is_not_abstract():
    assert not inspect.isabstract(sparql_NamedFunction)


def test_sparql_namedfunction_constructor_exists():
    assert callable(sparql_NamedFunction.__init__)


def test_sparql_namedfunction_constructor_args():
    sig = inspect.signature(sparql_NamedFunction.__init__)
    params = list(sig.parameters.keys())



def test_filternode_is_not_abstract():
    assert not inspect.isabstract(FilterNode)


def test_filternode_constructor_exists():
    assert callable(FilterNode.__init__)


def test_filternode_constructor_args():
    sig = inspect.signature(FilterNode.__init__)
    params = list(sig.parameters.keys())



def test_groupcondition_is_not_abstract():
    assert not inspect.isabstract(GroupCondition)


def test_groupcondition_constructor_exists():
    assert callable(GroupCondition.__init__)


def test_groupcondition_constructor_args():
    sig = inspect.signature(GroupCondition.__init__)
    params = list(sig.parameters.keys())



def test_sparql_filternode_is_not_abstract():
    assert not inspect.isabstract(sparql_FilterNode)


def test_sparql_filternode_constructor_exists():
    assert callable(sparql_FilterNode.__init__)


def test_sparql_filternode_constructor_args():
    sig = inspect.signature(sparql_FilterNode.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_expressionfilterexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_ExpressionFilterExpression)


def test_sparql_expressionfilterexpression_constructor_exists():
    assert callable(sparql_ExpressionFilterExpression.__init__)


def test_sparql_expressionfilterexpression_constructor_args():
    sig = inspect.signature(sparql_ExpressionFilterExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_sparql_expressionfilterexpression_has_operator():
    assert hasattr(sparql_ExpressionFilterExpression, "operator")
    descriptor = None
    for klass in sparql_ExpressionFilterExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sparql_builtincall_is_not_abstract():
    assert not inspect.isabstract(sparql_BuiltInCall)


def test_sparql_builtincall_constructor_exists():
    assert callable(sparql_BuiltInCall.__init__)


def test_sparql_builtincall_constructor_args():
    sig = inspect.signature(sparql_BuiltInCall.__init__)
    params = list(sig.parameters.keys())



def test_sparql_function_is_not_abstract():
    assert not inspect.isabstract(sparql_Function)


def test_sparql_function_constructor_exists():
    assert callable(sparql_Function.__init__)


def test_sparql_function_constructor_args():
    sig = inspect.signature(sparql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sparql_function_has_name():
    assert hasattr(sparql_Function, "name")
    descriptor = None
    for klass in sparql_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sparql_expression_is_not_abstract():
    assert not inspect.isabstract(sparql_Expression)


def test_sparql_expression_constructor_exists():
    assert callable(sparql_Expression.__init__)


def test_sparql_expression_constructor_args():
    sig = inspect.signature(sparql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_graphpattern_is_not_abstract():
    assert not inspect.isabstract(GraphPattern)


def test_graphpattern_constructor_exists():
    assert callable(GraphPattern.__init__)


def test_graphpattern_constructor_args():
    sig = inspect.signature(GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_filterpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_FilterPattern)


def test_sparql_filterpattern_constructor_exists():
    assert callable(sparql_FilterPattern.__init__)


def test_sparql_filterpattern_constructor_args():
    sig = inspect.signature(sparql_FilterPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_notexistspattern_is_not_abstract():
    assert not inspect.isabstract(sparql_NotExistsPattern)


def test_sparql_notexistspattern_constructor_exists():
    assert callable(sparql_NotExistsPattern.__init__)


def test_sparql_notexistspattern_constructor_args():
    sig = inspect.signature(sparql_NotExistsPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_minuspattern_is_not_abstract():
    assert not inspect.isabstract(sparql_MinusPattern)


def test_sparql_minuspattern_constructor_exists():
    assert callable(sparql_MinusPattern.__init__)


def test_sparql_minuspattern_constructor_args():
    sig = inspect.signature(sparql_MinusPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphGraphPattern)


def test_sparql_graphgraphpattern_constructor_exists():
    assert callable(sparql_GraphGraphPattern.__init__)


def test_sparql_graphgraphpattern_constructor_args():
    sig = inspect.signature(sparql_GraphGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_servicegraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_ServiceGraphPattern)


def test_sparql_servicegraphpattern_constructor_exists():
    assert callable(sparql_ServiceGraphPattern.__init__)


def test_sparql_servicegraphpattern_constructor_args():
    sig = inspect.signature(sparql_ServiceGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_existspattern_is_not_abstract():
    assert not inspect.isabstract(sparql_ExistsPattern)


def test_sparql_existspattern_constructor_exists():
    assert callable(sparql_ExistsPattern.__init__)


def test_sparql_existspattern_constructor_args():
    sig = inspect.signature(sparql_ExistsPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_triplessamesubject_is_not_abstract():
    assert not inspect.isabstract(sparql_TriplesSameSubject)


def test_sparql_triplessamesubject_constructor_exists():
    assert callable(sparql_TriplesSameSubject.__init__)


def test_sparql_triplessamesubject_constructor_args():
    sig = inspect.signature(sparql_TriplesSameSubject.__init__)
    params = list(sig.parameters.keys())



def test_sparql_optionalgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_OptionalGraphPattern)


def test_sparql_optionalgraphpattern_constructor_exists():
    assert callable(sparql_OptionalGraphPattern.__init__)


def test_sparql_optionalgraphpattern_constructor_args():
    sig = inspect.signature(sparql_OptionalGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_grouporuniongraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupOrUnionGraphPattern)


def test_sparql_grouporuniongraphpattern_constructor_exists():
    assert callable(sparql_GroupOrUnionGraphPattern.__init__)


def test_sparql_grouporuniongraphpattern_constructor_args():
    sig = inspect.signature(sparql_GroupOrUnionGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_propertylist_is_not_abstract():
    assert not inspect.isabstract(sparql_PropertyList)


def test_sparql_propertylist_constructor_exists():
    assert callable(sparql_PropertyList.__init__)


def test_sparql_propertylist_constructor_args():
    sig = inspect.signature(sparql_PropertyList.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphPattern)


def test_sparql_graphpattern_constructor_exists():
    assert callable(sparql_GraphPattern.__init__)


def test_sparql_graphpattern_constructor_args():
    sig = inspect.signature(sparql_GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_groupgraphpattern_is_not_abstract():
    assert not inspect.isabstract(GroupGraphPattern)


def test_groupgraphpattern_constructor_exists():
    assert callable(GroupGraphPattern.__init__)


def test_groupgraphpattern_constructor_args():
    sig = inspect.signature(GroupGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupgraphpatternsub_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupGraphPatternSub)


def test_sparql_groupgraphpatternsub_constructor_exists():
    assert callable(sparql_GroupGraphPatternSub.__init__)


def test_sparql_groupgraphpatternsub_constructor_args():
    sig = inspect.signature(sparql_GroupGraphPatternSub.__init__)
    params = list(sig.parameters.keys())



def test_sparql_subselectquery_is_not_abstract():
    assert not inspect.isabstract(sparql_SubSelectQuery)


def test_sparql_subselectquery_constructor_exists():
    assert callable(sparql_SubSelectQuery.__init__)


def test_sparql_subselectquery_constructor_args():
    sig = inspect.signature(sparql_SubSelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_constraint_is_not_abstract():
    assert not inspect.isabstract(sparql_Constraint)


def test_sparql_constraint_constructor_exists():
    assert callable(sparql_Constraint.__init__)


def test_sparql_constraint_constructor_args():
    sig = inspect.signature(sparql_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupcondition_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupCondition)


def test_sparql_groupcondition_constructor_exists():
    assert callable(sparql_GroupCondition.__init__)


def test_sparql_groupcondition_constructor_args():
    sig = inspect.signature(sparql_GroupCondition.__init__)
    params = list(sig.parameters.keys())



def test_datasetclause_is_not_abstract():
    assert not inspect.isabstract(DatasetClause)


def test_datasetclause_constructor_exists():
    assert callable(DatasetClause.__init__)


def test_datasetclause_constructor_args():
    sig = inspect.signature(DatasetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_nameddataset_is_not_abstract():
    assert not inspect.isabstract(sparql_NamedDataSet)


def test_sparql_nameddataset_constructor_exists():
    assert callable(sparql_NamedDataSet.__init__)


def test_sparql_nameddataset_constructor_args():
    sig = inspect.signature(sparql_NamedDataSet.__init__)
    params = list(sig.parameters.keys())



def test_sparql_servicedataset_is_not_abstract():
    assert not inspect.isabstract(sparql_ServiceDataSet)


def test_sparql_servicedataset_constructor_exists():
    assert callable(sparql_ServiceDataSet.__init__)


def test_sparql_servicedataset_constructor_args():
    sig = inspect.signature(sparql_ServiceDataSet.__init__)
    params = list(sig.parameters.keys())



def test_sparql_defaultdataset_is_not_abstract():
    assert not inspect.isabstract(sparql_DefaultDataSet)


def test_sparql_defaultdataset_constructor_exists():
    assert callable(sparql_DefaultDataSet.__init__)


def test_sparql_defaultdataset_constructor_args():
    sig = inspect.signature(sparql_DefaultDataSet.__init__)
    params = list(sig.parameters.keys())



def test_modifyquery_is_not_abstract():
    assert not inspect.isabstract(ModifyQuery)


def test_modifyquery_constructor_exists():
    assert callable(ModifyQuery.__init__)


def test_modifyquery_constructor_args():
    sig = inspect.signature(ModifyQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_deletedataquery_is_not_abstract():
    assert not inspect.isabstract(sparql_DeleteDataQuery)


def test_sparql_deletedataquery_constructor_exists():
    assert callable(sparql_DeleteDataQuery.__init__)


def test_sparql_deletedataquery_constructor_args():
    sig = inspect.signature(sparql_DeleteDataQuery.__init__)
    params = list(sig.parameters.keys())
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_deletedataquery_has_graph():
    assert hasattr(sparql_DeleteDataQuery, "graph")
    descriptor = None
    for klass in sparql_DeleteDataQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_deletequery_is_not_abstract():
    assert not inspect.isabstract(sparql_DeleteQuery)


def test_sparql_deletequery_constructor_exists():
    assert callable(sparql_DeleteQuery.__init__)


def test_sparql_deletequery_constructor_args():
    sig = inspect.signature(sparql_DeleteQuery.__init__)
    params = list(sig.parameters.keys())
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_deletequery_has_graph():
    assert hasattr(sparql_DeleteQuery, "graph")
    descriptor = None
    for klass in sparql_DeleteQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_insertdataquery_is_not_abstract():
    assert not inspect.isabstract(sparql_InsertDataQuery)


def test_sparql_insertdataquery_constructor_exists():
    assert callable(sparql_InsertDataQuery.__init__)


def test_sparql_insertdataquery_constructor_args():
    sig = inspect.signature(sparql_InsertDataQuery.__init__)
    params = list(sig.parameters.keys())
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_insertdataquery_has_graph():
    assert hasattr(sparql_InsertDataQuery, "graph")
    descriptor = None
    for klass in sparql_InsertDataQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_deletewherequery_is_not_abstract():
    assert not inspect.isabstract(sparql_DeleteWhereQuery)


def test_sparql_deletewherequery_constructor_exists():
    assert callable(sparql_DeleteWhereQuery.__init__)


def test_sparql_deletewherequery_constructor_args():
    sig = inspect.signature(sparql_DeleteWhereQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_insertquery_is_not_abstract():
    assert not inspect.isabstract(sparql_InsertQuery)


def test_sparql_insertquery_constructor_exists():
    assert callable(sparql_InsertQuery.__init__)


def test_sparql_insertquery_constructor_args():
    sig = inspect.signature(sparql_InsertQuery.__init__)
    params = list(sig.parameters.keys())
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_insertquery_has_graph():
    assert hasattr(sparql_InsertQuery, "graph")
    descriptor = None
    for klass in sparql_InsertQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_usinggraph_is_not_abstract():
    assert not inspect.isabstract(sparql_UsingGraph)


def test_sparql_usinggraph_constructor_exists():
    assert callable(sparql_UsingGraph.__init__)


def test_sparql_usinggraph_constructor_args():
    sig = inspect.signature(sparql_UsingGraph.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "named" in params, "Missing parameter 'named'"

def test_sparql_usinggraph_has_uri():
    assert hasattr(sparql_UsingGraph, "uri")
    descriptor = None
    for klass in sparql_UsingGraph.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_sparql_usinggraph_has_named():
    assert hasattr(sparql_UsingGraph, "named")
    descriptor = None
    for klass in sparql_UsingGraph.__mro__:
        if "named" in klass.__dict__:
            descriptor = klass.__dict__["named"]
            break
    assert isinstance(descriptor, property)



def test_updateoperation_is_not_abstract():
    assert not inspect.isabstract(UpdateOperation)


def test_updateoperation_constructor_exists():
    assert callable(UpdateOperation.__init__)


def test_updateoperation_constructor_args():
    sig = inspect.signature(UpdateOperation.__init__)
    params = list(sig.parameters.keys())



def test_sparql_dropgraphquery_is_not_abstract():
    assert not inspect.isabstract(sparql_DropGraphQuery)


def test_sparql_dropgraphquery_constructor_exists():
    assert callable(sparql_DropGraphQuery.__init__)


def test_sparql_dropgraphquery_constructor_args():
    sig = inspect.signature(sparql_DropGraphQuery.__init__)
    params = list(sig.parameters.keys())
    assert "graph" in params, "Missing parameter 'graph'"
    assert "isSilent" in params, "Missing parameter 'isSilent'"

def test_sparql_dropgraphquery_has_graph():
    assert hasattr(sparql_DropGraphQuery, "graph")
    descriptor = None
    for klass in sparql_DropGraphQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)

def test_sparql_dropgraphquery_has_isSilent():
    assert hasattr(sparql_DropGraphQuery, "isSilent")
    descriptor = None
    for klass in sparql_DropGraphQuery.__mro__:
        if "isSilent" in klass.__dict__:
            descriptor = klass.__dict__["isSilent"]
            break
    assert isinstance(descriptor, property)



def test_sparql_creategraphquery_is_not_abstract():
    assert not inspect.isabstract(sparql_CreateGraphQuery)


def test_sparql_creategraphquery_constructor_exists():
    assert callable(sparql_CreateGraphQuery.__init__)


def test_sparql_creategraphquery_constructor_args():
    sig = inspect.signature(sparql_CreateGraphQuery.__init__)
    params = list(sig.parameters.keys())
    assert "isSilent" in params, "Missing parameter 'isSilent'"
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_creategraphquery_has_isSilent():
    assert hasattr(sparql_CreateGraphQuery, "isSilent")
    descriptor = None
    for klass in sparql_CreateGraphQuery.__mro__:
        if "isSilent" in klass.__dict__:
            descriptor = klass.__dict__["isSilent"]
            break
    assert isinstance(descriptor, property)

def test_sparql_creategraphquery_has_graph():
    assert hasattr(sparql_CreateGraphQuery, "graph")
    descriptor = None
    for klass in sparql_CreateGraphQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_cleargraphquery_is_not_abstract():
    assert not inspect.isabstract(sparql_ClearGraphQuery)


def test_sparql_cleargraphquery_constructor_exists():
    assert callable(sparql_ClearGraphQuery.__init__)


def test_sparql_cleargraphquery_constructor_args():
    sig = inspect.signature(sparql_ClearGraphQuery.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_sparql_cleargraphquery_has_uri():
    assert hasattr(sparql_ClearGraphQuery, "uri")
    descriptor = None
    for klass in sparql_ClearGraphQuery.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_sparql_cleargraphquery_has_isDefault():
    assert hasattr(sparql_ClearGraphQuery, "isDefault")
    descriptor = None
    for klass in sparql_ClearGraphQuery.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_sparql_loadgraphquery_is_not_abstract():
    assert not inspect.isabstract(sparql_LoadGraphQuery)


def test_sparql_loadgraphquery_constructor_exists():
    assert callable(sparql_LoadGraphQuery.__init__)


def test_sparql_loadgraphquery_constructor_args():
    sig = inspect.signature(sparql_LoadGraphQuery.__init__)
    params = list(sig.parameters.keys())
    assert "intoGraph" in params, "Missing parameter 'intoGraph'"
    assert "graph" in params, "Missing parameter 'graph'"

def test_sparql_loadgraphquery_has_intoGraph():
    assert hasattr(sparql_LoadGraphQuery, "intoGraph")
    descriptor = None
    for klass in sparql_LoadGraphQuery.__mro__:
        if "intoGraph" in klass.__dict__:
            descriptor = klass.__dict__["intoGraph"]
            break
    assert isinstance(descriptor, property)

def test_sparql_loadgraphquery_has_graph():
    assert hasattr(sparql_LoadGraphQuery, "graph")
    descriptor = None
    for klass in sparql_LoadGraphQuery.__mro__:
        if "graph" in klass.__dict__:
            descriptor = klass.__dict__["graph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_modifyquery_is_not_abstract():
    assert not inspect.isabstract(sparql_ModifyQuery)


def test_sparql_modifyquery_constructor_exists():
    assert callable(sparql_ModifyQuery.__init__)


def test_sparql_modifyquery_constructor_args():
    sig = inspect.signature(sparql_ModifyQuery.__init__)
    params = list(sig.parameters.keys())
    assert "withGraph" in params, "Missing parameter 'withGraph'"

def test_sparql_modifyquery_has_withGraph():
    assert hasattr(sparql_ModifyQuery, "withGraph")
    descriptor = None
    for klass in sparql_ModifyQuery.__mro__:
        if "withGraph" in klass.__dict__:
            descriptor = klass.__dict__["withGraph"]
            break
    assert isinstance(descriptor, property)



def test_sparql_updateoperation_is_not_abstract():
    assert not inspect.isabstract(sparql_UpdateOperation)


def test_sparql_updateoperation_constructor_exists():
    assert callable(sparql_UpdateOperation.__init__)


def test_sparql_updateoperation_constructor_args():
    sig = inspect.signature(sparql_UpdateOperation.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupgraphpattern_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupGraphPattern)


def test_sparql_groupgraphpattern_constructor_exists():
    assert callable(sparql_GroupGraphPattern.__init__)


def test_sparql_groupgraphpattern_constructor_args():
    sig = inspect.signature(sparql_GroupGraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sparql_graphnode_is_not_abstract():
    assert not inspect.isabstract(sparql_GraphNode)


def test_sparql_graphnode_constructor_exists():
    assert callable(sparql_GraphNode.__init__)


def test_sparql_graphnode_constructor_args():
    sig = inspect.signature(sparql_GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_sparql_variable_is_not_abstract():
    assert not inspect.isabstract(sparql_Variable)


def test_sparql_variable_constructor_exists():
    assert callable(sparql_Variable.__init__)


def test_sparql_variable_constructor_args():
    sig = inspect.signature(sparql_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sparql_variable_has_name():
    assert hasattr(sparql_Variable, "name")
    descriptor = None
    for klass in sparql_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_selectionquery_is_not_abstract():
    assert not inspect.isabstract(SelectionQuery)


def test_selectionquery_constructor_exists():
    assert callable(SelectionQuery.__init__)


def test_selectionquery_constructor_args():
    sig = inspect.signature(SelectionQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_describequery_is_not_abstract():
    assert not inspect.isabstract(sparql_DescribeQuery)


def test_sparql_describequery_constructor_exists():
    assert callable(sparql_DescribeQuery.__init__)


def test_sparql_describequery_constructor_args():
    sig = inspect.signature(sparql_DescribeQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_askquery_is_not_abstract():
    assert not inspect.isabstract(sparql_AskQuery)


def test_sparql_askquery_constructor_exists():
    assert callable(sparql_AskQuery.__init__)


def test_sparql_askquery_constructor_args():
    sig = inspect.signature(sparql_AskQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_constructquery_is_not_abstract():
    assert not inspect.isabstract(sparql_ConstructQuery)


def test_sparql_constructquery_constructor_exists():
    assert callable(sparql_ConstructQuery.__init__)


def test_sparql_constructquery_constructor_args():
    sig = inspect.signature(sparql_ConstructQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sparql_SelectQuery)


def test_sparql_selectquery_constructor_exists():
    assert callable(sparql_SelectQuery.__init__)


def test_sparql_selectquery_constructor_args():
    sig = inspect.signature(sparql_SelectQuery.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"
    assert "isReduced" in params, "Missing parameter 'isReduced'"

def test_sparql_selectquery_has_all():
    assert hasattr(sparql_SelectQuery, "all")
    descriptor = None
    for klass in sparql_SelectQuery.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_sparql_selectquery_has_isDistinct():
    assert hasattr(sparql_SelectQuery, "isDistinct")
    descriptor = None
    for klass in sparql_SelectQuery.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)

def test_sparql_selectquery_has_isReduced():
    assert hasattr(sparql_SelectQuery, "isReduced")
    descriptor = None
    for klass in sparql_SelectQuery.__mro__:
        if "isReduced" in klass.__dict__:
            descriptor = klass.__dict__["isReduced"]
            break
    assert isinstance(descriptor, property)



def test_sparql_limitclause_is_not_abstract():
    assert not inspect.isabstract(sparql_LimitClause)


def test_sparql_limitclause_constructor_exists():
    assert callable(sparql_LimitClause.__init__)


def test_sparql_limitclause_constructor_args():
    sig = inspect.signature(sparql_LimitClause.__init__)
    params = list(sig.parameters.keys())
    assert "limit" in params, "Missing parameter 'limit'"

def test_sparql_limitclause_has_limit():
    assert hasattr(sparql_LimitClause, "limit")
    descriptor = None
    for klass in sparql_LimitClause.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)



def test_sparql_havingclause_is_not_abstract():
    assert not inspect.isabstract(sparql_HavingClause)


def test_sparql_havingclause_constructor_exists():
    assert callable(sparql_HavingClause.__init__)


def test_sparql_havingclause_constructor_args():
    sig = inspect.signature(sparql_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupclause_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupClause)


def test_sparql_groupclause_constructor_exists():
    assert callable(sparql_GroupClause.__init__)


def test_sparql_groupclause_constructor_args():
    sig = inspect.signature(sparql_GroupClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_whereclause_is_not_abstract():
    assert not inspect.isabstract(sparql_WhereClause)


def test_sparql_whereclause_constructor_exists():
    assert callable(sparql_WhereClause.__init__)


def test_sparql_whereclause_constructor_args():
    sig = inspect.signature(sparql_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_sparql_datasetclause_is_not_abstract():
    assert not inspect.isabstract(sparql_DatasetClause)


def test_sparql_datasetclause_constructor_exists():
    assert callable(sparql_DatasetClause.__init__)


def test_sparql_datasetclause_constructor_args():
    sig = inspect.signature(sparql_DatasetClause.__init__)
    params = list(sig.parameters.keys())



def test_sparqlquery_is_not_abstract():
    assert not inspect.isabstract(SPARQLQuery)


def test_sparqlquery_constructor_exists():
    assert callable(SPARQLQuery.__init__)


def test_sparqlquery_constructor_args():
    sig = inspect.signature(SPARQLQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_updatequery_is_not_abstract():
    assert not inspect.isabstract(sparql_UpdateQuery)


def test_sparql_updatequery_constructor_exists():
    assert callable(sparql_UpdateQuery.__init__)


def test_sparql_updatequery_constructor_args():
    sig = inspect.signature(sparql_UpdateQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_selectionquery_is_not_abstract():
    assert not inspect.isabstract(sparql_SelectionQuery)


def test_sparql_selectionquery_constructor_exists():
    assert callable(sparql_SelectionQuery.__init__)


def test_sparql_selectionquery_constructor_args():
    sig = inspect.signature(sparql_SelectionQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparql_iri_is_not_abstract():
    assert not inspect.isabstract(sparql_IRI)


def test_sparql_iri_constructor_exists():
    assert callable(sparql_IRI.__init__)


def test_sparql_iri_constructor_args():
    sig = inspect.signature(sparql_IRI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sparql_iri_has_value():
    assert hasattr(sparql_IRI, "value")
    descriptor = None
    for klass in sparql_IRI.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sparql_base_is_not_abstract():
    assert not inspect.isabstract(sparql_Base)


def test_sparql_base_constructor_exists():
    assert callable(sparql_Base.__init__)


def test_sparql_base_constructor_args():
    sig = inspect.signature(sparql_Base.__init__)
    params = list(sig.parameters.keys())



def test_sparql_prefix_is_not_abstract():
    assert not inspect.isabstract(sparql_Prefix)


def test_sparql_prefix_constructor_exists():
    assert callable(sparql_Prefix.__init__)


def test_sparql_prefix_constructor_args():
    sig = inspect.signature(sparql_Prefix.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "iref" in params, "Missing parameter 'iref'"

def test_sparql_prefix_has_name():
    assert hasattr(sparql_Prefix, "name")
    descriptor = None
    for klass in sparql_Prefix.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sparql_prefix_has_iref():
    assert hasattr(sparql_Prefix, "iref")
    descriptor = None
    for klass in sparql_Prefix.__mro__:
        if "iref" in klass.__dict__:
            descriptor = klass.__dict__["iref"]
            break
    assert isinstance(descriptor, property)



def test_sparql_sparqlquery_is_not_abstract():
    assert not inspect.isabstract(sparql_SPARQLQuery)


def test_sparql_sparqlquery_constructor_exists():
    assert callable(sparql_SPARQLQuery.__init__)


def test_sparql_sparqlquery_constructor_args():
    sig = inspect.signature(sparql_SPARQLQuery.__init__)
    params = list(sig.parameters.keys())



def test_aggregate_is_not_abstract():
    assert not inspect.isabstract(Aggregate)


def test_aggregate_constructor_exists():
    assert callable(Aggregate.__init__)


def test_aggregate_constructor_args():
    sig = inspect.signature(Aggregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sampleaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_SampleAggregate)


def test_sparql_sampleaggregate_constructor_exists():
    assert callable(sparql_SampleAggregate.__init__)


def test_sparql_sampleaggregate_constructor_args():
    sig = inspect.signature(sparql_SampleAggregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_sumaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_SumAggregate)


def test_sparql_sumaggregate_constructor_exists():
    assert callable(sparql_SumAggregate.__init__)


def test_sparql_sumaggregate_constructor_args():
    sig = inspect.signature(sparql_SumAggregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_avgaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_AvgAggregate)


def test_sparql_avgaggregate_constructor_exists():
    assert callable(sparql_AvgAggregate.__init__)


def test_sparql_avgaggregate_constructor_args():
    sig = inspect.signature(sparql_AvgAggregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_maxaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_MaxAggregate)


def test_sparql_maxaggregate_constructor_exists():
    assert callable(sparql_MaxAggregate.__init__)


def test_sparql_maxaggregate_constructor_args():
    sig = inspect.signature(sparql_MaxAggregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_groupaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_GroupAggregate)


def test_sparql_groupaggregate_constructor_exists():
    assert callable(sparql_GroupAggregate.__init__)


def test_sparql_groupaggregate_constructor_args():
    sig = inspect.signature(sparql_GroupAggregate.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_sparql_groupaggregate_has_value():
    assert hasattr(sparql_GroupAggregate, "value")
    descriptor = None
    for klass in sparql_GroupAggregate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sparql_groupaggregate_has_isDistinct():
    assert hasattr(sparql_GroupAggregate, "isDistinct")
    descriptor = None
    for klass in sparql_GroupAggregate.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_sparql_minagregate_is_not_abstract():
    assert not inspect.isabstract(sparql_MinAgregate)


def test_sparql_minagregate_constructor_exists():
    assert callable(sparql_MinAgregate.__init__)


def test_sparql_minagregate_constructor_args():
    sig = inspect.signature(sparql_MinAgregate.__init__)
    params = list(sig.parameters.keys())



def test_sparql_countaggregate_is_not_abstract():
    assert not inspect.isabstract(sparql_CountAggregate)


def test_sparql_countaggregate_constructor_exists():
    assert callable(sparql_CountAggregate.__init__)


def test_sparql_countaggregate_constructor_args():
    sig = inspect.signature(sparql_CountAggregate.__init__)
    params = list(sig.parameters.keys())
    assert "isAll" in params, "Missing parameter 'isAll'"
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_sparql_countaggregate_has_isAll():
    assert hasattr(sparql_CountAggregate, "isAll")
    descriptor = None
    for klass in sparql_CountAggregate.__mro__:
        if "isAll" in klass.__dict__:
            descriptor = klass.__dict__["isAll"]
            break
    assert isinstance(descriptor, property)

def test_sparql_countaggregate_has_isDistinct():
    assert hasattr(sparql_CountAggregate, "isDistinct")
    descriptor = None
    for klass in sparql_CountAggregate.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_sparql_andfilterexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_AndFilterExpression)


def test_sparql_andfilterexpression_constructor_exists():
    assert callable(sparql_AndFilterExpression.__init__)


def test_sparql_andfilterexpression_constructor_args():
    sig = inspect.signature(sparql_AndFilterExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparql_orfilterexpression_is_not_abstract():
    assert not inspect.isabstract(sparql_OrFilterExpression)


def test_sparql_orfilterexpression_constructor_exists():
    assert callable(sparql_OrFilterExpression.__init__)


def test_sparql_orfilterexpression_constructor_args():
    sig = inspect.signature(sparql_OrFilterExpression.__init__)
    params = list(sig.parameters.keys())



def test_rdftag_is_not_abstract():
    assert not inspect.isabstract(RDFTag)


def test_rdftag_constructor_exists():
    assert callable(RDFTag.__init__)


def test_rdftag_constructor_args():
    sig = inspect.signature(RDFTag.__init__)
    params = list(sig.parameters.keys())



def test_sparql_langtag_is_not_abstract():
    assert not inspect.isabstract(sparql_LangTag)


def test_sparql_langtag_constructor_exists():
    assert callable(sparql_LangTag.__init__)


def test_sparql_langtag_constructor_args():
    sig = inspect.signature(sparql_LangTag.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"

def test_sparql_langtag_has_lang():
    assert hasattr(sparql_LangTag, "lang")
    descriptor = None
    for klass in sparql_LangTag.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_sparql_typetag_is_not_abstract():
    assert not inspect.isabstract(sparql_TypeTag)


def test_sparql_typetag_constructor_exists():
    assert callable(sparql_TypeTag.__init__)


def test_sparql_typetag_constructor_args():
    sig = inspect.signature(sparql_TypeTag.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sparql_integervalue_is_not_abstract():
    assert not inspect.isabstract(sparql_IntegerValue)


def test_sparql_integervalue_constructor_exists():
    assert callable(sparql_IntegerValue.__init__)


def test_sparql_integervalue_constructor_args():
    sig = inspect.signature(sparql_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sparql_integervalue_has_value():
    assert hasattr(sparql_IntegerValue, "value")
    descriptor = None
    for klass in sparql_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sparql_stringvalue_is_not_abstract():
    assert not inspect.isabstract(sparql_StringValue)


def test_sparql_stringvalue_constructor_exists():
    assert callable(sparql_StringValue.__init__)


def test_sparql_stringvalue_constructor_args():
    sig = inspect.signature(sparql_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sparql_stringvalue_has_value():
    assert hasattr(sparql_StringValue, "value")
    descriptor = None
    for klass in sparql_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sparql_rdftag_is_not_abstract():
    assert not inspect.isabstract(sparql_RDFTag)


def test_sparql_rdftag_constructor_exists():
    assert callable(sparql_RDFTag.__init__)


def test_sparql_rdftag_constructor_args():
    sig = inspect.signature(sparql_RDFTag.__init__)
    params = list(sig.parameters.keys())



def test_sparql_value_is_not_abstract():
    assert not inspect.isabstract(sparql_Value)


def test_sparql_value_constructor_exists():
    assert callable(sparql_Value.__init__)


def test_sparql_value_constructor_args():
    sig = inspect.signature(sparql_Value.__init__)
    params = list(sig.parameters.keys())



def test_sparql_parameter_is_not_abstract():
    assert not inspect.isabstract(sparql_Parameter)


def test_sparql_parameter_constructor_exists():
    assert callable(sparql_Parameter.__init__)


def test_sparql_parameter_constructor_args():
    sig = inspect.signature(sparql_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sparql_parameter_has_name():
    assert hasattr(sparql_Parameter, "name")
    descriptor = None
    for klass in sparql_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sparql_blanknode_is_not_abstract():
    assert not inspect.isabstract(sparql_BlankNode)


def test_sparql_blanknode_constructor_exists():
    assert callable(sparql_BlankNode.__init__)


def test_sparql_blanknode_constructor_args():
    sig = inspect.signature(sparql_BlankNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sparql_blanknode_has_name():
    assert hasattr(sparql_BlankNode, "name")
    descriptor = None
    for klass in sparql_BlankNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sparql_expraggarg_is_not_abstract():
    assert not inspect.isabstract(sparql_ExprAggArg)


def test_sparql_expraggarg_constructor_exists():
    assert callable(sparql_ExprAggArg.__init__)


def test_sparql_expraggarg_constructor_args():
    sig = inspect.signature(sparql_ExprAggArg.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_sparql_expraggarg_has_isDistinct():
    assert hasattr(sparql_ExprAggArg, "isDistinct")
    descriptor = None
    for klass in sparql_ExprAggArg.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_sparql_namedvariable_is_not_abstract():
    assert not inspect.isabstract(sparql_NamedVariable)


def test_sparql_namedvariable_constructor_exists():
    assert callable(sparql_NamedVariable.__init__)


def test_sparql_namedvariable_constructor_args():
    sig = inspect.signature(sparql_NamedVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparql_unnamedvariable_is_not_abstract():
    assert not inspect.isabstract(sparql_UnNamedVariable)


def test_sparql_unnamedvariable_constructor_exists():
    assert callable(sparql_UnNamedVariable.__init__)


def test_sparql_unnamedvariable_constructor_args():
    sig = inspect.signature(sparql_UnNamedVariable.__init__)
    params = list(sig.parameters.keys())

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "equal",
        "multiplicity",
        "div",
        "greaterEqual",
        "sum",
        "notEqual",
        "lessThen",
        "sub",
        "lessEqual",
        "greaterThen",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
GraphNode_strategy = st.builds(
    GraphNode,
)
sparql_Aggregate_strategy = st.builds(
    sparql_Aggregate,
)
Function_strategy = st.builds(
    Function,
)
sparql_SparqlFunction_strategy = st.builds(
    sparql_SparqlFunction,
)
sparql_NamedFunction_strategy = st.builds(
    sparql_NamedFunction,
)
FilterNode_strategy = st.builds(
    FilterNode,
)
GroupCondition_strategy = st.builds(
    GroupCondition,
)
sparql_FilterNode_strategy = st.builds(
    sparql_FilterNode,
)
Expression_strategy = st.builds(
    Expression,
)
sparql_ExpressionFilterExpression_strategy = st.builds(
    sparql_ExpressionFilterExpression,
    operator=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
sparql_BuiltInCall_strategy = st.builds(
    sparql_BuiltInCall,
)
sparql_Function_strategy = st.builds(
    sparql_Function,
    name=
        safe_text
)
sparql_Expression_strategy = st.builds(
    sparql_Expression,
)
GraphPattern_strategy = st.builds(
    GraphPattern,
)
sparql_FilterPattern_strategy = st.builds(
    sparql_FilterPattern,
)
sparql_NotExistsPattern_strategy = st.builds(
    sparql_NotExistsPattern,
)
sparql_MinusPattern_strategy = st.builds(
    sparql_MinusPattern,
)
sparql_GraphGraphPattern_strategy = st.builds(
    sparql_GraphGraphPattern,
)
sparql_ServiceGraphPattern_strategy = st.builds(
    sparql_ServiceGraphPattern,
)
sparql_ExistsPattern_strategy = st.builds(
    sparql_ExistsPattern,
)
sparql_TriplesSameSubject_strategy = st.builds(
    sparql_TriplesSameSubject,
)
sparql_OptionalGraphPattern_strategy = st.builds(
    sparql_OptionalGraphPattern,
)
sparql_GroupOrUnionGraphPattern_strategy = st.builds(
    sparql_GroupOrUnionGraphPattern,
)
sparql_PropertyList_strategy = st.builds(
    sparql_PropertyList,
)
sparql_GraphPattern_strategy = st.builds(
    sparql_GraphPattern,
)
GroupGraphPattern_strategy = st.builds(
    GroupGraphPattern,
)
sparql_GroupGraphPatternSub_strategy = st.builds(
    sparql_GroupGraphPatternSub,
)
sparql_SubSelectQuery_strategy = st.builds(
    sparql_SubSelectQuery,
)
sparql_Constraint_strategy = st.builds(
    sparql_Constraint,
)
sparql_GroupCondition_strategy = st.builds(
    sparql_GroupCondition,
)
DatasetClause_strategy = st.builds(
    DatasetClause,
)
sparql_NamedDataSet_strategy = st.builds(
    sparql_NamedDataSet,
)
sparql_ServiceDataSet_strategy = st.builds(
    sparql_ServiceDataSet,
)
sparql_DefaultDataSet_strategy = st.builds(
    sparql_DefaultDataSet,
)
ModifyQuery_strategy = st.builds(
    ModifyQuery,
)
sparql_DeleteDataQuery_strategy = st.builds(
    sparql_DeleteDataQuery,
    graph=
        safe_text
)
sparql_DeleteQuery_strategy = st.builds(
    sparql_DeleteQuery,
    graph=
        safe_text
)
sparql_InsertDataQuery_strategy = st.builds(
    sparql_InsertDataQuery,
    graph=
        safe_text
)
sparql_DeleteWhereQuery_strategy = st.builds(
    sparql_DeleteWhereQuery,
)
sparql_InsertQuery_strategy = st.builds(
    sparql_InsertQuery,
    graph=
        safe_text
)
sparql_UsingGraph_strategy = st.builds(
    sparql_UsingGraph,
    uri=
        safe_text,
    named=
        st.booleans()
)
UpdateOperation_strategy = st.builds(
    UpdateOperation,
)
sparql_DropGraphQuery_strategy = st.builds(
    sparql_DropGraphQuery,
    graph=
        safe_text,
    isSilent=
        safe_text
)
sparql_CreateGraphQuery_strategy = st.builds(
    sparql_CreateGraphQuery,
    isSilent=
        safe_text,
    graph=
        safe_text
)
sparql_ClearGraphQuery_strategy = st.builds(
    sparql_ClearGraphQuery,
    uri=
        safe_text,
    isDefault=
        st.booleans()
)
sparql_LoadGraphQuery_strategy = st.builds(
    sparql_LoadGraphQuery,
    intoGraph=
        safe_text,
    graph=
        safe_text
)
sparql_ModifyQuery_strategy = st.builds(
    sparql_ModifyQuery,
    withGraph=
        safe_text
)
sparql_UpdateOperation_strategy = st.builds(
    sparql_UpdateOperation,
)
sparql_GroupGraphPattern_strategy = st.builds(
    sparql_GroupGraphPattern,
)
sparql_GraphNode_strategy = st.builds(
    sparql_GraphNode,
)
sparql_Variable_strategy = st.builds(
    sparql_Variable,
    name=
        safe_text
)
SelectionQuery_strategy = st.builds(
    SelectionQuery,
)
sparql_DescribeQuery_strategy = st.builds(
    sparql_DescribeQuery,
)
sparql_AskQuery_strategy = st.builds(
    sparql_AskQuery,
)
sparql_ConstructQuery_strategy = st.builds(
    sparql_ConstructQuery,
)
sparql_SelectQuery_strategy = st.builds(
    sparql_SelectQuery,
    all=
        st.booleans(),
    isDistinct=
        st.booleans(),
    isReduced=
        st.booleans()
)
sparql_LimitClause_strategy = st.builds(
    sparql_LimitClause,
    limit=
        st.integers()
)
sparql_HavingClause_strategy = st.builds(
    sparql_HavingClause,
)
sparql_GroupClause_strategy = st.builds(
    sparql_GroupClause,
)
sparql_WhereClause_strategy = st.builds(
    sparql_WhereClause,
)
sparql_DatasetClause_strategy = st.builds(
    sparql_DatasetClause,
)
SPARQLQuery_strategy = st.builds(
    SPARQLQuery,
)
sparql_UpdateQuery_strategy = st.builds(
    sparql_UpdateQuery,
)
sparql_SelectionQuery_strategy = st.builds(
    sparql_SelectionQuery,
)
sparql_IRI_strategy = st.builds(
    sparql_IRI,
    value=
        safe_text
)
sparql_Base_strategy = st.builds(
    sparql_Base,
)
sparql_Prefix_strategy = st.builds(
    sparql_Prefix,
    name=
        safe_text,
    iref=
        safe_text
)
sparql_SPARQLQuery_strategy = st.builds(
    sparql_SPARQLQuery,
)
Aggregate_strategy = st.builds(
    Aggregate,
)
sparql_SampleAggregate_strategy = st.builds(
    sparql_SampleAggregate,
)
sparql_SumAggregate_strategy = st.builds(
    sparql_SumAggregate,
)
sparql_AvgAggregate_strategy = st.builds(
    sparql_AvgAggregate,
)
sparql_MaxAggregate_strategy = st.builds(
    sparql_MaxAggregate,
)
sparql_GroupAggregate_strategy = st.builds(
    sparql_GroupAggregate,
    value=
        safe_text,
    isDistinct=
        st.booleans()
)
sparql_MinAgregate_strategy = st.builds(
    sparql_MinAgregate,
)
sparql_CountAggregate_strategy = st.builds(
    sparql_CountAggregate,
    isAll=
        st.booleans(),
    isDistinct=
        st.booleans()
)
sparql_AndFilterExpression_strategy = st.builds(
    sparql_AndFilterExpression,
)
sparql_OrFilterExpression_strategy = st.builds(
    sparql_OrFilterExpression,
)
RDFTag_strategy = st.builds(
    RDFTag,
)
sparql_LangTag_strategy = st.builds(
    sparql_LangTag,
    lang=
        safe_text
)
sparql_TypeTag_strategy = st.builds(
    sparql_TypeTag,
)
Value_strategy = st.builds(
    Value,
)
sparql_IntegerValue_strategy = st.builds(
    sparql_IntegerValue,
    value=
        st.integers()
)
sparql_StringValue_strategy = st.builds(
    sparql_StringValue,
    value=
        safe_text
)
sparql_RDFTag_strategy = st.builds(
    sparql_RDFTag,
)
sparql_Value_strategy = st.builds(
    sparql_Value,
)
sparql_Parameter_strategy = st.builds(
    sparql_Parameter,
    name=
        safe_text
)
sparql_BlankNode_strategy = st.builds(
    sparql_BlankNode,
    name=
        safe_text
)
sparql_ExprAggArg_strategy = st.builds(
    sparql_ExprAggArg,
    isDistinct=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
sparql_NamedVariable_strategy = st.builds(
    sparql_NamedVariable,
)
sparql_UnNamedVariable_strategy = st.builds(
    sparql_UnNamedVariable,
)

@given(instance=GraphNode_strategy)
@settings(max_examples=50)
def test_graphnode_instantiation(instance):
    assert isinstance(instance, GraphNode)

@given(instance=sparql_Aggregate_strategy)
@settings(max_examples=50)
def test_sparql_aggregate_instantiation(instance):
    assert isinstance(instance, sparql_Aggregate)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=sparql_SparqlFunction_strategy)
@settings(max_examples=50)
def test_sparql_sparqlfunction_instantiation(instance):
    assert isinstance(instance, sparql_SparqlFunction)

@given(instance=sparql_NamedFunction_strategy)
@settings(max_examples=50)
def test_sparql_namedfunction_instantiation(instance):
    assert isinstance(instance, sparql_NamedFunction)

@given(instance=FilterNode_strategy)
@settings(max_examples=50)
def test_filternode_instantiation(instance):
    assert isinstance(instance, FilterNode)

@given(instance=GroupCondition_strategy)
@settings(max_examples=50)
def test_groupcondition_instantiation(instance):
    assert isinstance(instance, GroupCondition)

@given(instance=sparql_FilterNode_strategy)
@settings(max_examples=50)
def test_sparql_filternode_instantiation(instance):
    assert isinstance(instance, sparql_FilterNode)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sparql_ExpressionFilterExpression_strategy)
@settings(max_examples=50)
def test_sparql_expressionfilterexpression_instantiation(instance):
    assert isinstance(instance, sparql_ExpressionFilterExpression)



@given(instance=sparql_ExpressionFilterExpression_strategy)
def test_sparql_expressionfilterexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=sparql_BuiltInCall_strategy)
@settings(max_examples=50)
def test_sparql_builtincall_instantiation(instance):
    assert isinstance(instance, sparql_BuiltInCall)

@given(instance=sparql_Function_strategy)
@settings(max_examples=50)
def test_sparql_function_instantiation(instance):
    assert isinstance(instance, sparql_Function)



@given(instance=sparql_Function_strategy)
def test_sparql_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sparql_Expression_strategy)
@settings(max_examples=50)
def test_sparql_expression_instantiation(instance):
    assert isinstance(instance, sparql_Expression)

@given(instance=GraphPattern_strategy)
@settings(max_examples=50)
def test_graphpattern_instantiation(instance):
    assert isinstance(instance, GraphPattern)

@given(instance=sparql_FilterPattern_strategy)
@settings(max_examples=50)
def test_sparql_filterpattern_instantiation(instance):
    assert isinstance(instance, sparql_FilterPattern)

@given(instance=sparql_NotExistsPattern_strategy)
@settings(max_examples=50)
def test_sparql_notexistspattern_instantiation(instance):
    assert isinstance(instance, sparql_NotExistsPattern)

@given(instance=sparql_MinusPattern_strategy)
@settings(max_examples=50)
def test_sparql_minuspattern_instantiation(instance):
    assert isinstance(instance, sparql_MinusPattern)

@given(instance=sparql_GraphGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_graphgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GraphGraphPattern)

@given(instance=sparql_ServiceGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_servicegraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_ServiceGraphPattern)

@given(instance=sparql_ExistsPattern_strategy)
@settings(max_examples=50)
def test_sparql_existspattern_instantiation(instance):
    assert isinstance(instance, sparql_ExistsPattern)

@given(instance=sparql_TriplesSameSubject_strategy)
@settings(max_examples=50)
def test_sparql_triplessamesubject_instantiation(instance):
    assert isinstance(instance, sparql_TriplesSameSubject)

@given(instance=sparql_OptionalGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_optionalgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_OptionalGraphPattern)

@given(instance=sparql_GroupOrUnionGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_grouporuniongraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GroupOrUnionGraphPattern)

@given(instance=sparql_PropertyList_strategy)
@settings(max_examples=50)
def test_sparql_propertylist_instantiation(instance):
    assert isinstance(instance, sparql_PropertyList)

@given(instance=sparql_GraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_graphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GraphPattern)

@given(instance=GroupGraphPattern_strategy)
@settings(max_examples=50)
def test_groupgraphpattern_instantiation(instance):
    assert isinstance(instance, GroupGraphPattern)

@given(instance=sparql_GroupGraphPatternSub_strategy)
@settings(max_examples=50)
def test_sparql_groupgraphpatternsub_instantiation(instance):
    assert isinstance(instance, sparql_GroupGraphPatternSub)

@given(instance=sparql_SubSelectQuery_strategy)
@settings(max_examples=50)
def test_sparql_subselectquery_instantiation(instance):
    assert isinstance(instance, sparql_SubSelectQuery)

@given(instance=sparql_Constraint_strategy)
@settings(max_examples=50)
def test_sparql_constraint_instantiation(instance):
    assert isinstance(instance, sparql_Constraint)

@given(instance=sparql_GroupCondition_strategy)
@settings(max_examples=50)
def test_sparql_groupcondition_instantiation(instance):
    assert isinstance(instance, sparql_GroupCondition)

@given(instance=DatasetClause_strategy)
@settings(max_examples=50)
def test_datasetclause_instantiation(instance):
    assert isinstance(instance, DatasetClause)

@given(instance=sparql_NamedDataSet_strategy)
@settings(max_examples=50)
def test_sparql_nameddataset_instantiation(instance):
    assert isinstance(instance, sparql_NamedDataSet)

@given(instance=sparql_ServiceDataSet_strategy)
@settings(max_examples=50)
def test_sparql_servicedataset_instantiation(instance):
    assert isinstance(instance, sparql_ServiceDataSet)

@given(instance=sparql_DefaultDataSet_strategy)
@settings(max_examples=50)
def test_sparql_defaultdataset_instantiation(instance):
    assert isinstance(instance, sparql_DefaultDataSet)

@given(instance=ModifyQuery_strategy)
@settings(max_examples=50)
def test_modifyquery_instantiation(instance):
    assert isinstance(instance, ModifyQuery)

@given(instance=sparql_DeleteDataQuery_strategy)
@settings(max_examples=50)
def test_sparql_deletedataquery_instantiation(instance):
    assert isinstance(instance, sparql_DeleteDataQuery)



@given(instance=sparql_DeleteDataQuery_strategy)
def test_sparql_deletedataquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_DeleteQuery_strategy)
@settings(max_examples=50)
def test_sparql_deletequery_instantiation(instance):
    assert isinstance(instance, sparql_DeleteQuery)



@given(instance=sparql_DeleteQuery_strategy)
def test_sparql_deletequery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_InsertDataQuery_strategy)
@settings(max_examples=50)
def test_sparql_insertdataquery_instantiation(instance):
    assert isinstance(instance, sparql_InsertDataQuery)



@given(instance=sparql_InsertDataQuery_strategy)
def test_sparql_insertdataquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_DeleteWhereQuery_strategy)
@settings(max_examples=50)
def test_sparql_deletewherequery_instantiation(instance):
    assert isinstance(instance, sparql_DeleteWhereQuery)

@given(instance=sparql_InsertQuery_strategy)
@settings(max_examples=50)
def test_sparql_insertquery_instantiation(instance):
    assert isinstance(instance, sparql_InsertQuery)



@given(instance=sparql_InsertQuery_strategy)
def test_sparql_insertquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_UsingGraph_strategy)
@settings(max_examples=50)
def test_sparql_usinggraph_instantiation(instance):
    assert isinstance(instance, sparql_UsingGraph)



@given(instance=sparql_UsingGraph_strategy)
def test_sparql_usinggraph_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=sparql_UsingGraph_strategy)
def test_sparql_usinggraph_named_setter(instance):
    original = instance.named
    instance.named = original
    assert instance.named == original

@given(instance=UpdateOperation_strategy)
@settings(max_examples=50)
def test_updateoperation_instantiation(instance):
    assert isinstance(instance, UpdateOperation)

@given(instance=sparql_DropGraphQuery_strategy)
@settings(max_examples=50)
def test_sparql_dropgraphquery_instantiation(instance):
    assert isinstance(instance, sparql_DropGraphQuery)



@given(instance=sparql_DropGraphQuery_strategy)
def test_sparql_dropgraphquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original



@given(instance=sparql_DropGraphQuery_strategy)
def test_sparql_dropgraphquery_isSilent_setter(instance):
    original = instance.isSilent
    instance.isSilent = original
    assert instance.isSilent == original

@given(instance=sparql_CreateGraphQuery_strategy)
@settings(max_examples=50)
def test_sparql_creategraphquery_instantiation(instance):
    assert isinstance(instance, sparql_CreateGraphQuery)



@given(instance=sparql_CreateGraphQuery_strategy)
def test_sparql_creategraphquery_isSilent_setter(instance):
    original = instance.isSilent
    instance.isSilent = original
    assert instance.isSilent == original



@given(instance=sparql_CreateGraphQuery_strategy)
def test_sparql_creategraphquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_ClearGraphQuery_strategy)
@settings(max_examples=50)
def test_sparql_cleargraphquery_instantiation(instance):
    assert isinstance(instance, sparql_ClearGraphQuery)



@given(instance=sparql_ClearGraphQuery_strategy)
def test_sparql_cleargraphquery_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=sparql_ClearGraphQuery_strategy)
def test_sparql_cleargraphquery_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=sparql_LoadGraphQuery_strategy)
@settings(max_examples=50)
def test_sparql_loadgraphquery_instantiation(instance):
    assert isinstance(instance, sparql_LoadGraphQuery)



@given(instance=sparql_LoadGraphQuery_strategy)
def test_sparql_loadgraphquery_intoGraph_setter(instance):
    original = instance.intoGraph
    instance.intoGraph = original
    assert instance.intoGraph == original



@given(instance=sparql_LoadGraphQuery_strategy)
def test_sparql_loadgraphquery_graph_setter(instance):
    original = instance.graph
    instance.graph = original
    assert instance.graph == original

@given(instance=sparql_ModifyQuery_strategy)
@settings(max_examples=50)
def test_sparql_modifyquery_instantiation(instance):
    assert isinstance(instance, sparql_ModifyQuery)



@given(instance=sparql_ModifyQuery_strategy)
def test_sparql_modifyquery_withGraph_setter(instance):
    original = instance.withGraph
    instance.withGraph = original
    assert instance.withGraph == original

@given(instance=sparql_UpdateOperation_strategy)
@settings(max_examples=50)
def test_sparql_updateoperation_instantiation(instance):
    assert isinstance(instance, sparql_UpdateOperation)

@given(instance=sparql_GroupGraphPattern_strategy)
@settings(max_examples=50)
def test_sparql_groupgraphpattern_instantiation(instance):
    assert isinstance(instance, sparql_GroupGraphPattern)

@given(instance=sparql_GraphNode_strategy)
@settings(max_examples=50)
def test_sparql_graphnode_instantiation(instance):
    assert isinstance(instance, sparql_GraphNode)

@given(instance=sparql_Variable_strategy)
@settings(max_examples=50)
def test_sparql_variable_instantiation(instance):
    assert isinstance(instance, sparql_Variable)



@given(instance=sparql_Variable_strategy)
def test_sparql_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SelectionQuery_strategy)
@settings(max_examples=50)
def test_selectionquery_instantiation(instance):
    assert isinstance(instance, SelectionQuery)

@given(instance=sparql_DescribeQuery_strategy)
@settings(max_examples=50)
def test_sparql_describequery_instantiation(instance):
    assert isinstance(instance, sparql_DescribeQuery)

@given(instance=sparql_AskQuery_strategy)
@settings(max_examples=50)
def test_sparql_askquery_instantiation(instance):
    assert isinstance(instance, sparql_AskQuery)

@given(instance=sparql_ConstructQuery_strategy)
@settings(max_examples=50)
def test_sparql_constructquery_instantiation(instance):
    assert isinstance(instance, sparql_ConstructQuery)

@given(instance=sparql_SelectQuery_strategy)
@settings(max_examples=50)
def test_sparql_selectquery_instantiation(instance):
    assert isinstance(instance, sparql_SelectQuery)



@given(instance=sparql_SelectQuery_strategy)
def test_sparql_selectquery_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=sparql_SelectQuery_strategy)
def test_sparql_selectquery_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original



@given(instance=sparql_SelectQuery_strategy)
def test_sparql_selectquery_isReduced_setter(instance):
    original = instance.isReduced
    instance.isReduced = original
    assert instance.isReduced == original

@given(instance=sparql_LimitClause_strategy)
@settings(max_examples=50)
def test_sparql_limitclause_instantiation(instance):
    assert isinstance(instance, sparql_LimitClause)



@given(instance=sparql_LimitClause_strategy)
def test_sparql_limitclause_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=sparql_HavingClause_strategy)
@settings(max_examples=50)
def test_sparql_havingclause_instantiation(instance):
    assert isinstance(instance, sparql_HavingClause)

@given(instance=sparql_GroupClause_strategy)
@settings(max_examples=50)
def test_sparql_groupclause_instantiation(instance):
    assert isinstance(instance, sparql_GroupClause)

@given(instance=sparql_WhereClause_strategy)
@settings(max_examples=50)
def test_sparql_whereclause_instantiation(instance):
    assert isinstance(instance, sparql_WhereClause)

@given(instance=sparql_DatasetClause_strategy)
@settings(max_examples=50)
def test_sparql_datasetclause_instantiation(instance):
    assert isinstance(instance, sparql_DatasetClause)

@given(instance=SPARQLQuery_strategy)
@settings(max_examples=50)
def test_sparqlquery_instantiation(instance):
    assert isinstance(instance, SPARQLQuery)

@given(instance=sparql_UpdateQuery_strategy)
@settings(max_examples=50)
def test_sparql_updatequery_instantiation(instance):
    assert isinstance(instance, sparql_UpdateQuery)

@given(instance=sparql_SelectionQuery_strategy)
@settings(max_examples=50)
def test_sparql_selectionquery_instantiation(instance):
    assert isinstance(instance, sparql_SelectionQuery)

@given(instance=sparql_IRI_strategy)
@settings(max_examples=50)
def test_sparql_iri_instantiation(instance):
    assert isinstance(instance, sparql_IRI)



@given(instance=sparql_IRI_strategy)
def test_sparql_iri_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sparql_Base_strategy)
@settings(max_examples=50)
def test_sparql_base_instantiation(instance):
    assert isinstance(instance, sparql_Base)

@given(instance=sparql_Prefix_strategy)
@settings(max_examples=50)
def test_sparql_prefix_instantiation(instance):
    assert isinstance(instance, sparql_Prefix)



@given(instance=sparql_Prefix_strategy)
def test_sparql_prefix_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sparql_Prefix_strategy)
def test_sparql_prefix_iref_setter(instance):
    original = instance.iref
    instance.iref = original
    assert instance.iref == original

@given(instance=sparql_SPARQLQuery_strategy)
@settings(max_examples=50)
def test_sparql_sparqlquery_instantiation(instance):
    assert isinstance(instance, sparql_SPARQLQuery)

@given(instance=Aggregate_strategy)
@settings(max_examples=50)
def test_aggregate_instantiation(instance):
    assert isinstance(instance, Aggregate)

@given(instance=sparql_SampleAggregate_strategy)
@settings(max_examples=50)
def test_sparql_sampleaggregate_instantiation(instance):
    assert isinstance(instance, sparql_SampleAggregate)

@given(instance=sparql_SumAggregate_strategy)
@settings(max_examples=50)
def test_sparql_sumaggregate_instantiation(instance):
    assert isinstance(instance, sparql_SumAggregate)

@given(instance=sparql_AvgAggregate_strategy)
@settings(max_examples=50)
def test_sparql_avgaggregate_instantiation(instance):
    assert isinstance(instance, sparql_AvgAggregate)

@given(instance=sparql_MaxAggregate_strategy)
@settings(max_examples=50)
def test_sparql_maxaggregate_instantiation(instance):
    assert isinstance(instance, sparql_MaxAggregate)

@given(instance=sparql_GroupAggregate_strategy)
@settings(max_examples=50)
def test_sparql_groupaggregate_instantiation(instance):
    assert isinstance(instance, sparql_GroupAggregate)



@given(instance=sparql_GroupAggregate_strategy)
def test_sparql_groupaggregate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=sparql_GroupAggregate_strategy)
def test_sparql_groupaggregate_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=sparql_MinAgregate_strategy)
@settings(max_examples=50)
def test_sparql_minagregate_instantiation(instance):
    assert isinstance(instance, sparql_MinAgregate)

@given(instance=sparql_CountAggregate_strategy)
@settings(max_examples=50)
def test_sparql_countaggregate_instantiation(instance):
    assert isinstance(instance, sparql_CountAggregate)



@given(instance=sparql_CountAggregate_strategy)
def test_sparql_countaggregate_isAll_setter(instance):
    original = instance.isAll
    instance.isAll = original
    assert instance.isAll == original



@given(instance=sparql_CountAggregate_strategy)
def test_sparql_countaggregate_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=sparql_AndFilterExpression_strategy)
@settings(max_examples=50)
def test_sparql_andfilterexpression_instantiation(instance):
    assert isinstance(instance, sparql_AndFilterExpression)

@given(instance=sparql_OrFilterExpression_strategy)
@settings(max_examples=50)
def test_sparql_orfilterexpression_instantiation(instance):
    assert isinstance(instance, sparql_OrFilterExpression)

@given(instance=RDFTag_strategy)
@settings(max_examples=50)
def test_rdftag_instantiation(instance):
    assert isinstance(instance, RDFTag)

@given(instance=sparql_LangTag_strategy)
@settings(max_examples=50)
def test_sparql_langtag_instantiation(instance):
    assert isinstance(instance, sparql_LangTag)



@given(instance=sparql_LangTag_strategy)
def test_sparql_langtag_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=sparql_TypeTag_strategy)
@settings(max_examples=50)
def test_sparql_typetag_instantiation(instance):
    assert isinstance(instance, sparql_TypeTag)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=sparql_IntegerValue_strategy)
@settings(max_examples=50)
def test_sparql_integervalue_instantiation(instance):
    assert isinstance(instance, sparql_IntegerValue)



@given(instance=sparql_IntegerValue_strategy)
def test_sparql_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sparql_StringValue_strategy)
@settings(max_examples=50)
def test_sparql_stringvalue_instantiation(instance):
    assert isinstance(instance, sparql_StringValue)



@given(instance=sparql_StringValue_strategy)
def test_sparql_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sparql_RDFTag_strategy)
@settings(max_examples=50)
def test_sparql_rdftag_instantiation(instance):
    assert isinstance(instance, sparql_RDFTag)

@given(instance=sparql_Value_strategy)
@settings(max_examples=50)
def test_sparql_value_instantiation(instance):
    assert isinstance(instance, sparql_Value)

@given(instance=sparql_Parameter_strategy)
@settings(max_examples=50)
def test_sparql_parameter_instantiation(instance):
    assert isinstance(instance, sparql_Parameter)



@given(instance=sparql_Parameter_strategy)
def test_sparql_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sparql_BlankNode_strategy)
@settings(max_examples=50)
def test_sparql_blanknode_instantiation(instance):
    assert isinstance(instance, sparql_BlankNode)



@given(instance=sparql_BlankNode_strategy)
def test_sparql_blanknode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sparql_ExprAggArg_strategy)
@settings(max_examples=50)
def test_sparql_expraggarg_instantiation(instance):
    assert isinstance(instance, sparql_ExprAggArg)



@given(instance=sparql_ExprAggArg_strategy)
def test_sparql_expraggarg_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=sparql_NamedVariable_strategy)
@settings(max_examples=50)
def test_sparql_namedvariable_instantiation(instance):
    assert isinstance(instance, sparql_NamedVariable)

@given(instance=sparql_UnNamedVariable_strategy)
@settings(max_examples=50)
def test_sparql_unnamedvariable_instantiation(instance):
    assert isinstance(instance, sparql_UnNamedVariable)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jDOQL_OrderBySpec,
    jDOQL_HavingClause,
    jDOQL_ParameterDeclaration,
    OrderBySpec,
    ResultSpec,
    jDOQL_ResultNaming,
    jDOQL_Expression,
    jDOQL_SubqueryResultClause,
    jDOQL_ResultSpec,
    jDOQL_ResultClause,
    jDOQL_IntoClause,
    jDOQL_EObject,
    SubquerySelectClause,
    jDOQL_VariableDeclaration,
    jDOQL_SubquerySelectClause,
    jDOQL_Alias,
    Expression,
    jDOQL_MultiplicationExpression,
    jDOQL_ComparisonOperatorExpression,
    jDOQL_ConditionalAndExpression,
    jDOQL_ConditionalOrExpression,
    jDOQL_SimpleAndExpression,
    jDOQL_FieldAccessExpression,
    jDOQL_SimpleOrExpression,
    jDOQL_AdditionExpression,
    jDOQL_Subquery,
    jDOQL_RangeClause,
    jDOQL_OrderByClause,
    jDOQL_GroupByClause,
    jDOQL_ImportClause,
    jDOQL_ParametersClause,
    jDOQL_VariablesClause,
    jDOQL_WhereClause,
    jDOQL_FromClause,
    jDOQL_SelectClause,
    jDOQL_SingleStringJDOQL,
    jDOQL_SubqueryFromClause,
    OrderByDirection,
    AdditionOperator,
    UnaryOperator,
    ComparisonOperator,
    MultiplicationOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jdoql_orderbyspec_is_not_abstract():
    assert not inspect.isabstract(jDOQL_OrderBySpec)


def test_jdoql_orderbyspec_constructor_exists():
    assert callable(jDOQL_OrderBySpec.__init__)


def test_jdoql_orderbyspec_constructor_args():
    sig = inspect.signature(jDOQL_OrderBySpec.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_havingclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_HavingClause)


def test_jdoql_havingclause_constructor_exists():
    assert callable(jDOQL_HavingClause.__init__)


def test_jdoql_havingclause_constructor_args():
    sig = inspect.signature(jDOQL_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ParameterDeclaration)


def test_jdoql_parameterdeclaration_constructor_exists():
    assert callable(jDOQL_ParameterDeclaration.__init__)


def test_jdoql_parameterdeclaration_constructor_args():
    sig = inspect.signature(jDOQL_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "declaredParameterName" in params, "Missing parameter 'declaredParameterName'"
    assert "type" in params, "Missing parameter 'type'"

def test_jdoql_parameterdeclaration_has_declaredParameterName():
    assert hasattr(jDOQL_ParameterDeclaration, "declaredParameterName")
    descriptor = None
    for klass in jDOQL_ParameterDeclaration.__mro__:
        if "declaredParameterName" in klass.__dict__:
            descriptor = klass.__dict__["declaredParameterName"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_parameterdeclaration_has_type():
    assert hasattr(jDOQL_ParameterDeclaration, "type")
    descriptor = None
    for klass in jDOQL_ParameterDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_orderbyspec_is_not_abstract():
    assert not inspect.isabstract(OrderBySpec)


def test_orderbyspec_constructor_exists():
    assert callable(OrderBySpec.__init__)


def test_orderbyspec_constructor_args():
    sig = inspect.signature(OrderBySpec.__init__)
    params = list(sig.parameters.keys())



def test_resultspec_is_not_abstract():
    assert not inspect.isabstract(ResultSpec)


def test_resultspec_constructor_exists():
    assert callable(ResultSpec.__init__)


def test_resultspec_constructor_args():
    sig = inspect.signature(ResultSpec.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_resultnaming_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ResultNaming)


def test_jdoql_resultnaming_constructor_exists():
    assert callable(jDOQL_ResultNaming.__init__)


def test_jdoql_resultnaming_constructor_args():
    sig = inspect.signature(jDOQL_ResultNaming.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdoql_resultnaming_has_identifier():
    assert hasattr(jDOQL_ResultNaming, "identifier")
    descriptor = None
    for klass in jDOQL_ResultNaming.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_expression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_Expression)


def test_jdoql_expression_constructor_exists():
    assert callable(jDOQL_Expression.__init__)


def test_jdoql_expression_constructor_args():
    sig = inspect.signature(jDOQL_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "castType" in params, "Missing parameter 'castType'"
    assert "id" in params, "Missing parameter 'id'"
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"
    assert "this" in params, "Missing parameter 'this'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_jdoql_expression_has_castType():
    assert hasattr(jDOQL_Expression, "castType")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "castType" in klass.__dict__:
            descriptor = klass.__dict__["castType"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_id():
    assert hasattr(jDOQL_Expression, "id")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_isDistinct():
    assert hasattr(jDOQL_Expression, "isDistinct")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_this():
    assert hasattr(jDOQL_Expression, "this")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_direction():
    assert hasattr(jDOQL_Expression, "direction")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_literal():
    assert hasattr(jDOQL_Expression, "literal")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_parameterName():
    assert hasattr(jDOQL_Expression, "parameterName")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_name():
    assert hasattr(jDOQL_Expression, "name")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_expression_has_unaryOperator():
    assert hasattr(jDOQL_Expression, "unaryOperator")
    descriptor = None
    for klass in jDOQL_Expression.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_subqueryresultclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SubqueryResultClause)


def test_jdoql_subqueryresultclause_constructor_exists():
    assert callable(jDOQL_SubqueryResultClause.__init__)


def test_jdoql_subqueryresultclause_constructor_args():
    sig = inspect.signature(jDOQL_SubqueryResultClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jdoql_subqueryresultclause_has_isDistinct():
    assert hasattr(jDOQL_SubqueryResultClause, "isDistinct")
    descriptor = None
    for klass in jDOQL_SubqueryResultClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_resultspec_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ResultSpec)


def test_jdoql_resultspec_constructor_exists():
    assert callable(jDOQL_ResultSpec.__init__)


def test_jdoql_resultspec_constructor_args():
    sig = inspect.signature(jDOQL_ResultSpec.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_resultclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ResultClause)


def test_jdoql_resultclause_constructor_exists():
    assert callable(jDOQL_ResultClause.__init__)


def test_jdoql_resultclause_constructor_args():
    sig = inspect.signature(jDOQL_ResultClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jdoql_resultclause_has_isDistinct():
    assert hasattr(jDOQL_ResultClause, "isDistinct")
    descriptor = None
    for klass in jDOQL_ResultClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_intoclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_IntoClause)


def test_jdoql_intoclause_constructor_exists():
    assert callable(jDOQL_IntoClause.__init__)


def test_jdoql_intoclause_constructor_args():
    sig = inspect.signature(jDOQL_IntoClause.__init__)
    params = list(sig.parameters.keys())
    assert "resultClassName" in params, "Missing parameter 'resultClassName'"

def test_jdoql_intoclause_has_resultClassName():
    assert hasattr(jDOQL_IntoClause, "resultClassName")
    descriptor = None
    for klass in jDOQL_IntoClause.__mro__:
        if "resultClassName" in klass.__dict__:
            descriptor = klass.__dict__["resultClassName"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_eobject_is_not_abstract():
    assert not inspect.isabstract(jDOQL_EObject)


def test_jdoql_eobject_constructor_exists():
    assert callable(jDOQL_EObject.__init__)


def test_jdoql_eobject_constructor_args():
    sig = inspect.signature(jDOQL_EObject.__init__)
    params = list(sig.parameters.keys())



def test_subqueryselectclause_is_not_abstract():
    assert not inspect.isabstract(SubquerySelectClause)


def test_subqueryselectclause_constructor_exists():
    assert callable(SubquerySelectClause.__init__)


def test_subqueryselectclause_constructor_args():
    sig = inspect.signature(SubquerySelectClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jDOQL_VariableDeclaration)


def test_jdoql_variabledeclaration_constructor_exists():
    assert callable(jDOQL_VariableDeclaration.__init__)


def test_jdoql_variabledeclaration_constructor_args():
    sig = inspect.signature(jDOQL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "type" in params, "Missing parameter 'type'"

def test_jdoql_variabledeclaration_has_variableName():
    assert hasattr(jDOQL_VariableDeclaration, "variableName")
    descriptor = None
    for klass in jDOQL_VariableDeclaration.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_variabledeclaration_has_type():
    assert hasattr(jDOQL_VariableDeclaration, "type")
    descriptor = None
    for klass in jDOQL_VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_subqueryselectclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SubquerySelectClause)


def test_jdoql_subqueryselectclause_constructor_exists():
    assert callable(jDOQL_SubquerySelectClause.__init__)


def test_jdoql_subqueryselectclause_constructor_args():
    sig = inspect.signature(jDOQL_SubquerySelectClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_alias_is_not_abstract():
    assert not inspect.isabstract(jDOQL_Alias)


def test_jdoql_alias_constructor_exists():
    assert callable(jDOQL_Alias.__init__)


def test_jdoql_alias_constructor_args():
    sig = inspect.signature(jDOQL_Alias.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdoql_alias_has_identifier():
    assert hasattr(jDOQL_Alias, "identifier")
    descriptor = None
    for klass in jDOQL_Alias.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_MultiplicationExpression)


def test_jdoql_multiplicationexpression_constructor_exists():
    assert callable(jDOQL_MultiplicationExpression.__init__)


def test_jdoql_multiplicationexpression_constructor_args():
    sig = inspect.signature(jDOQL_MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql_multiplicationexpression_has_operator():
    assert hasattr(jDOQL_MultiplicationExpression, "operator")
    descriptor = None
    for klass in jDOQL_MultiplicationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ComparisonOperatorExpression)


def test_jdoql_comparisonoperatorexpression_constructor_exists():
    assert callable(jDOQL_ComparisonOperatorExpression.__init__)


def test_jdoql_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(jDOQL_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql_comparisonoperatorexpression_has_operator():
    assert hasattr(jDOQL_ComparisonOperatorExpression, "operator")
    descriptor = None
    for klass in jDOQL_ComparisonOperatorExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ConditionalAndExpression)


def test_jdoql_conditionalandexpression_constructor_exists():
    assert callable(jDOQL_ConditionalAndExpression.__init__)


def test_jdoql_conditionalandexpression_constructor_args():
    sig = inspect.signature(jDOQL_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ConditionalOrExpression)


def test_jdoql_conditionalorexpression_constructor_exists():
    assert callable(jDOQL_ConditionalOrExpression.__init__)


def test_jdoql_conditionalorexpression_constructor_args():
    sig = inspect.signature(jDOQL_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_simpleandexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SimpleAndExpression)


def test_jdoql_simpleandexpression_constructor_exists():
    assert callable(jDOQL_SimpleAndExpression.__init__)


def test_jdoql_simpleandexpression_constructor_args():
    sig = inspect.signature(jDOQL_SimpleAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_fieldaccessexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_FieldAccessExpression)


def test_jdoql_fieldaccessexpression_constructor_exists():
    assert callable(jDOQL_FieldAccessExpression.__init__)


def test_jdoql_fieldaccessexpression_constructor_args():
    sig = inspect.signature(jDOQL_FieldAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_simpleorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SimpleOrExpression)


def test_jdoql_simpleorexpression_constructor_exists():
    assert callable(jDOQL_SimpleOrExpression.__init__)


def test_jdoql_simpleorexpression_constructor_args():
    sig = inspect.signature(jDOQL_SimpleOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_additionexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL_AdditionExpression)


def test_jdoql_additionexpression_constructor_exists():
    assert callable(jDOQL_AdditionExpression.__init__)


def test_jdoql_additionexpression_constructor_args():
    sig = inspect.signature(jDOQL_AdditionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql_additionexpression_has_operator():
    assert hasattr(jDOQL_AdditionExpression, "operator")
    descriptor = None
    for klass in jDOQL_AdditionExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_subquery_is_not_abstract():
    assert not inspect.isabstract(jDOQL_Subquery)


def test_jdoql_subquery_constructor_exists():
    assert callable(jDOQL_Subquery.__init__)


def test_jdoql_subquery_constructor_args():
    sig = inspect.signature(jDOQL_Subquery.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_rangeclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_RangeClause)


def test_jdoql_rangeclause_constructor_exists():
    assert callable(jDOQL_RangeClause.__init__)


def test_jdoql_rangeclause_constructor_args():
    sig = inspect.signature(jDOQL_RangeClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_orderbyclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_OrderByClause)


def test_jdoql_orderbyclause_constructor_exists():
    assert callable(jDOQL_OrderByClause.__init__)


def test_jdoql_orderbyclause_constructor_args():
    sig = inspect.signature(jDOQL_OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_groupbyclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_GroupByClause)


def test_jdoql_groupbyclause_constructor_exists():
    assert callable(jDOQL_GroupByClause.__init__)


def test_jdoql_groupbyclause_constructor_args():
    sig = inspect.signature(jDOQL_GroupByClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_importclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ImportClause)


def test_jdoql_importclause_constructor_exists():
    assert callable(jDOQL_ImportClause.__init__)


def test_jdoql_importclause_constructor_args():
    sig = inspect.signature(jDOQL_ImportClause.__init__)
    params = list(sig.parameters.keys())
    assert "importDeclarations" in params, "Missing parameter 'importDeclarations'"

def test_jdoql_importclause_has_importDeclarations():
    assert hasattr(jDOQL_ImportClause, "importDeclarations")
    descriptor = None
    for klass in jDOQL_ImportClause.__mro__:
        if "importDeclarations" in klass.__dict__:
            descriptor = klass.__dict__["importDeclarations"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_parametersclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_ParametersClause)


def test_jdoql_parametersclause_constructor_exists():
    assert callable(jDOQL_ParametersClause.__init__)


def test_jdoql_parametersclause_constructor_args():
    sig = inspect.signature(jDOQL_ParametersClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_variablesclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_VariablesClause)


def test_jdoql_variablesclause_constructor_exists():
    assert callable(jDOQL_VariablesClause.__init__)


def test_jdoql_variablesclause_constructor_args():
    sig = inspect.signature(jDOQL_VariablesClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_whereclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_WhereClause)


def test_jdoql_whereclause_constructor_exists():
    assert callable(jDOQL_WhereClause.__init__)


def test_jdoql_whereclause_constructor_args():
    sig = inspect.signature(jDOQL_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_fromclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_FromClause)


def test_jdoql_fromclause_constructor_exists():
    assert callable(jDOQL_FromClause.__init__)


def test_jdoql_fromclause_constructor_args():
    sig = inspect.signature(jDOQL_FromClause.__init__)
    params = list(sig.parameters.keys())
    assert "isExcludeSubclasses" in params, "Missing parameter 'isExcludeSubclasses'"
    assert "candidateClassName" in params, "Missing parameter 'candidateClassName'"

def test_jdoql_fromclause_has_isExcludeSubclasses():
    assert hasattr(jDOQL_FromClause, "isExcludeSubclasses")
    descriptor = None
    for klass in jDOQL_FromClause.__mro__:
        if "isExcludeSubclasses" in klass.__dict__:
            descriptor = klass.__dict__["isExcludeSubclasses"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_fromclause_has_candidateClassName():
    assert hasattr(jDOQL_FromClause, "candidateClassName")
    descriptor = None
    for klass in jDOQL_FromClause.__mro__:
        if "candidateClassName" in klass.__dict__:
            descriptor = klass.__dict__["candidateClassName"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_selectclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SelectClause)


def test_jdoql_selectclause_constructor_exists():
    assert callable(jDOQL_SelectClause.__init__)


def test_jdoql_selectclause_constructor_args():
    sig = inspect.signature(jDOQL_SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_jdoql_selectclause_has_isUnique():
    assert hasattr(jDOQL_SelectClause, "isUnique")
    descriptor = None
    for klass in jDOQL_SelectClause.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_jdoql_singlestringjdoql_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SingleStringJDOQL)


def test_jdoql_singlestringjdoql_constructor_exists():
    assert callable(jDOQL_SingleStringJDOQL.__init__)


def test_jdoql_singlestringjdoql_constructor_args():
    sig = inspect.signature(jDOQL_SingleStringJDOQL.__init__)
    params = list(sig.parameters.keys())



def test_jdoql_subqueryfromclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL_SubqueryFromClause)


def test_jdoql_subqueryfromclause_constructor_exists():
    assert callable(jDOQL_SubqueryFromClause.__init__)


def test_jdoql_subqueryfromclause_constructor_args():
    sig = inspect.signature(jDOQL_SubqueryFromClause.__init__)
    params = list(sig.parameters.keys())
    assert "isExcludeSubclasses" in params, "Missing parameter 'isExcludeSubclasses'"
    assert "candidateClassName" in params, "Missing parameter 'candidateClassName'"

def test_jdoql_subqueryfromclause_has_isExcludeSubclasses():
    assert hasattr(jDOQL_SubqueryFromClause, "isExcludeSubclasses")
    descriptor = None
    for klass in jDOQL_SubqueryFromClause.__mro__:
        if "isExcludeSubclasses" in klass.__dict__:
            descriptor = klass.__dict__["isExcludeSubclasses"]
            break
    assert isinstance(descriptor, property)

def test_jdoql_subqueryfromclause_has_candidateClassName():
    assert hasattr(jDOQL_SubqueryFromClause, "candidateClassName")
    descriptor = None
    for klass in jDOQL_SubqueryFromClause.__mro__:
        if "candidateClassName" in klass.__dict__:
            descriptor = klass.__dict__["candidateClassName"]
            break
    assert isinstance(descriptor, property)

def test_orderbydirection_exists():
    # Check that the Enumeration exists
    assert OrderByDirection is not None

def test_orderbydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderByDirection]
    expected_literals = [
        "descending",
        "asc",
        "ascending",
        "desc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderByDirection"

def test_additionoperator_exists():
    # Check that the Enumeration exists
    assert AdditionOperator is not None

def test_additionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditionOperator]
    expected_literals = [
        "subtract",
        "add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditionOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "logicalNot",
        "bitwiseNot",
        "positive",
        "negative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "lessEqual",
        "notEqual",
        "greaterThen",
        "instanceof",
        "greaterEqual",
        "lessThen",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_multiplicationoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicationOperator is not None

def test_multiplicationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicationOperator]
    expected_literals = [
        "multiply",
        "divide",
        "modulo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicationOperator"


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
jDOQL_OrderBySpec_strategy = st.builds(
    jDOQL_OrderBySpec,
)
jDOQL_HavingClause_strategy = st.builds(
    jDOQL_HavingClause,
)
jDOQL_ParameterDeclaration_strategy = st.builds(
    jDOQL_ParameterDeclaration,
    declaredParameterName=
        safe_text,
    type=
        safe_text
)
OrderBySpec_strategy = st.builds(
    OrderBySpec,
)
ResultSpec_strategy = st.builds(
    ResultSpec,
)
jDOQL_ResultNaming_strategy = st.builds(
    jDOQL_ResultNaming,
    identifier=
        safe_text
)
jDOQL_Expression_strategy = st.builds(
    jDOQL_Expression,
    castType=
        safe_text,
    id=
        safe_text,
    isDistinct=
        st.booleans(),
    this=
        safe_text,
    direction=
        safe_text,
    literal=
        safe_text,
    parameterName=
        safe_text,
    name=
        safe_text,
    unaryOperator=
        safe_text
)
jDOQL_SubqueryResultClause_strategy = st.builds(
    jDOQL_SubqueryResultClause,
    isDistinct=
        st.booleans()
)
jDOQL_ResultSpec_strategy = st.builds(
    jDOQL_ResultSpec,
)
jDOQL_ResultClause_strategy = st.builds(
    jDOQL_ResultClause,
    isDistinct=
        st.booleans()
)
jDOQL_IntoClause_strategy = st.builds(
    jDOQL_IntoClause,
    resultClassName=
        safe_text
)
jDOQL_EObject_strategy = st.builds(
    jDOQL_EObject,
)
SubquerySelectClause_strategy = st.builds(
    SubquerySelectClause,
)
jDOQL_VariableDeclaration_strategy = st.builds(
    jDOQL_VariableDeclaration,
    variableName=
        safe_text,
    type=
        safe_text
)
jDOQL_SubquerySelectClause_strategy = st.builds(
    jDOQL_SubquerySelectClause,
)
jDOQL_Alias_strategy = st.builds(
    jDOQL_Alias,
    identifier=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
jDOQL_MultiplicationExpression_strategy = st.builds(
    jDOQL_MultiplicationExpression,
    operator=
        safe_text
)
jDOQL_ComparisonOperatorExpression_strategy = st.builds(
    jDOQL_ComparisonOperatorExpression,
    operator=
        safe_text
)
jDOQL_ConditionalAndExpression_strategy = st.builds(
    jDOQL_ConditionalAndExpression,
)
jDOQL_ConditionalOrExpression_strategy = st.builds(
    jDOQL_ConditionalOrExpression,
)
jDOQL_SimpleAndExpression_strategy = st.builds(
    jDOQL_SimpleAndExpression,
)
jDOQL_FieldAccessExpression_strategy = st.builds(
    jDOQL_FieldAccessExpression,
)
jDOQL_SimpleOrExpression_strategy = st.builds(
    jDOQL_SimpleOrExpression,
)
jDOQL_AdditionExpression_strategy = st.builds(
    jDOQL_AdditionExpression,
    operator=
        safe_text
)
jDOQL_Subquery_strategy = st.builds(
    jDOQL_Subquery,
)
jDOQL_RangeClause_strategy = st.builds(
    jDOQL_RangeClause,
)
jDOQL_OrderByClause_strategy = st.builds(
    jDOQL_OrderByClause,
)
jDOQL_GroupByClause_strategy = st.builds(
    jDOQL_GroupByClause,
)
jDOQL_ImportClause_strategy = st.builds(
    jDOQL_ImportClause,
    importDeclarations=
        safe_text
)
jDOQL_ParametersClause_strategy = st.builds(
    jDOQL_ParametersClause,
)
jDOQL_VariablesClause_strategy = st.builds(
    jDOQL_VariablesClause,
)
jDOQL_WhereClause_strategy = st.builds(
    jDOQL_WhereClause,
)
jDOQL_FromClause_strategy = st.builds(
    jDOQL_FromClause,
    isExcludeSubclasses=
        st.booleans(),
    candidateClassName=
        safe_text
)
jDOQL_SelectClause_strategy = st.builds(
    jDOQL_SelectClause,
    isUnique=
        st.booleans()
)
jDOQL_SingleStringJDOQL_strategy = st.builds(
    jDOQL_SingleStringJDOQL,
)
jDOQL_SubqueryFromClause_strategy = st.builds(
    jDOQL_SubqueryFromClause,
    isExcludeSubclasses=
        st.booleans(),
    candidateClassName=
        safe_text
)

@given(instance=jDOQL_OrderBySpec_strategy)
@settings(max_examples=50)
def test_jdoql_orderbyspec_instantiation(instance):
    assert isinstance(instance, jDOQL_OrderBySpec)

@given(instance=jDOQL_HavingClause_strategy)
@settings(max_examples=50)
def test_jdoql_havingclause_instantiation(instance):
    assert isinstance(instance, jDOQL_HavingClause)

@given(instance=jDOQL_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_jdoql_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, jDOQL_ParameterDeclaration)



@given(instance=jDOQL_ParameterDeclaration_strategy)
def test_jdoql_parameterdeclaration_declaredParameterName_setter(instance):
    original = instance.declaredParameterName
    instance.declaredParameterName = original
    assert instance.declaredParameterName == original



@given(instance=jDOQL_ParameterDeclaration_strategy)
def test_jdoql_parameterdeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=OrderBySpec_strategy)
@settings(max_examples=50)
def test_orderbyspec_instantiation(instance):
    assert isinstance(instance, OrderBySpec)

@given(instance=ResultSpec_strategy)
@settings(max_examples=50)
def test_resultspec_instantiation(instance):
    assert isinstance(instance, ResultSpec)

@given(instance=jDOQL_ResultNaming_strategy)
@settings(max_examples=50)
def test_jdoql_resultnaming_instantiation(instance):
    assert isinstance(instance, jDOQL_ResultNaming)



@given(instance=jDOQL_ResultNaming_strategy)
def test_jdoql_resultnaming_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=jDOQL_Expression_strategy)
@settings(max_examples=50)
def test_jdoql_expression_instantiation(instance):
    assert isinstance(instance, jDOQL_Expression)



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_castType_setter(instance):
    original = instance.castType
    instance.castType = original
    assert instance.castType == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jDOQL_Expression_strategy)
def test_jdoql_expression_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=jDOQL_SubqueryResultClause_strategy)
@settings(max_examples=50)
def test_jdoql_subqueryresultclause_instantiation(instance):
    assert isinstance(instance, jDOQL_SubqueryResultClause)



@given(instance=jDOQL_SubqueryResultClause_strategy)
def test_jdoql_subqueryresultclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jDOQL_ResultSpec_strategy)
@settings(max_examples=50)
def test_jdoql_resultspec_instantiation(instance):
    assert isinstance(instance, jDOQL_ResultSpec)

@given(instance=jDOQL_ResultClause_strategy)
@settings(max_examples=50)
def test_jdoql_resultclause_instantiation(instance):
    assert isinstance(instance, jDOQL_ResultClause)



@given(instance=jDOQL_ResultClause_strategy)
def test_jdoql_resultclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jDOQL_IntoClause_strategy)
@settings(max_examples=50)
def test_jdoql_intoclause_instantiation(instance):
    assert isinstance(instance, jDOQL_IntoClause)



@given(instance=jDOQL_IntoClause_strategy)
def test_jdoql_intoclause_resultClassName_setter(instance):
    original = instance.resultClassName
    instance.resultClassName = original
    assert instance.resultClassName == original

@given(instance=jDOQL_EObject_strategy)
@settings(max_examples=50)
def test_jdoql_eobject_instantiation(instance):
    assert isinstance(instance, jDOQL_EObject)

@given(instance=SubquerySelectClause_strategy)
@settings(max_examples=50)
def test_subqueryselectclause_instantiation(instance):
    assert isinstance(instance, SubquerySelectClause)

@given(instance=jDOQL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdoql_variabledeclaration_instantiation(instance):
    assert isinstance(instance, jDOQL_VariableDeclaration)



@given(instance=jDOQL_VariableDeclaration_strategy)
def test_jdoql_variabledeclaration_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=jDOQL_VariableDeclaration_strategy)
def test_jdoql_variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jDOQL_SubquerySelectClause_strategy)
@settings(max_examples=50)
def test_jdoql_subqueryselectclause_instantiation(instance):
    assert isinstance(instance, jDOQL_SubquerySelectClause)

@given(instance=jDOQL_Alias_strategy)
@settings(max_examples=50)
def test_jdoql_alias_instantiation(instance):
    assert isinstance(instance, jDOQL_Alias)



@given(instance=jDOQL_Alias_strategy)
def test_jdoql_alias_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=jDOQL_MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_jdoql_multiplicationexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_MultiplicationExpression)



@given(instance=jDOQL_MultiplicationExpression_strategy)
def test_jdoql_multiplicationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL_ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_jdoql_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_ComparisonOperatorExpression)



@given(instance=jDOQL_ComparisonOperatorExpression_strategy)
def test_jdoql_comparisonoperatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL_ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_jdoql_conditionalandexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_ConditionalAndExpression)

@given(instance=jDOQL_ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_jdoql_conditionalorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_ConditionalOrExpression)

@given(instance=jDOQL_SimpleAndExpression_strategy)
@settings(max_examples=50)
def test_jdoql_simpleandexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_SimpleAndExpression)

@given(instance=jDOQL_FieldAccessExpression_strategy)
@settings(max_examples=50)
def test_jdoql_fieldaccessexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_FieldAccessExpression)

@given(instance=jDOQL_SimpleOrExpression_strategy)
@settings(max_examples=50)
def test_jdoql_simpleorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_SimpleOrExpression)

@given(instance=jDOQL_AdditionExpression_strategy)
@settings(max_examples=50)
def test_jdoql_additionexpression_instantiation(instance):
    assert isinstance(instance, jDOQL_AdditionExpression)



@given(instance=jDOQL_AdditionExpression_strategy)
def test_jdoql_additionexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL_Subquery_strategy)
@settings(max_examples=50)
def test_jdoql_subquery_instantiation(instance):
    assert isinstance(instance, jDOQL_Subquery)

@given(instance=jDOQL_RangeClause_strategy)
@settings(max_examples=50)
def test_jdoql_rangeclause_instantiation(instance):
    assert isinstance(instance, jDOQL_RangeClause)

@given(instance=jDOQL_OrderByClause_strategy)
@settings(max_examples=50)
def test_jdoql_orderbyclause_instantiation(instance):
    assert isinstance(instance, jDOQL_OrderByClause)

@given(instance=jDOQL_GroupByClause_strategy)
@settings(max_examples=50)
def test_jdoql_groupbyclause_instantiation(instance):
    assert isinstance(instance, jDOQL_GroupByClause)

@given(instance=jDOQL_ImportClause_strategy)
@settings(max_examples=50)
def test_jdoql_importclause_instantiation(instance):
    assert isinstance(instance, jDOQL_ImportClause)



@given(instance=jDOQL_ImportClause_strategy)
def test_jdoql_importclause_importDeclarations_setter(instance):
    original = instance.importDeclarations
    instance.importDeclarations = original
    assert instance.importDeclarations == original

@given(instance=jDOQL_ParametersClause_strategy)
@settings(max_examples=50)
def test_jdoql_parametersclause_instantiation(instance):
    assert isinstance(instance, jDOQL_ParametersClause)

@given(instance=jDOQL_VariablesClause_strategy)
@settings(max_examples=50)
def test_jdoql_variablesclause_instantiation(instance):
    assert isinstance(instance, jDOQL_VariablesClause)

@given(instance=jDOQL_WhereClause_strategy)
@settings(max_examples=50)
def test_jdoql_whereclause_instantiation(instance):
    assert isinstance(instance, jDOQL_WhereClause)

@given(instance=jDOQL_FromClause_strategy)
@settings(max_examples=50)
def test_jdoql_fromclause_instantiation(instance):
    assert isinstance(instance, jDOQL_FromClause)



@given(instance=jDOQL_FromClause_strategy)
def test_jdoql_fromclause_isExcludeSubclasses_setter(instance):
    original = instance.isExcludeSubclasses
    instance.isExcludeSubclasses = original
    assert instance.isExcludeSubclasses == original



@given(instance=jDOQL_FromClause_strategy)
def test_jdoql_fromclause_candidateClassName_setter(instance):
    original = instance.candidateClassName
    instance.candidateClassName = original
    assert instance.candidateClassName == original

@given(instance=jDOQL_SelectClause_strategy)
@settings(max_examples=50)
def test_jdoql_selectclause_instantiation(instance):
    assert isinstance(instance, jDOQL_SelectClause)



@given(instance=jDOQL_SelectClause_strategy)
def test_jdoql_selectclause_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=jDOQL_SingleStringJDOQL_strategy)
@settings(max_examples=50)
def test_jdoql_singlestringjdoql_instantiation(instance):
    assert isinstance(instance, jDOQL_SingleStringJDOQL)

@given(instance=jDOQL_SubqueryFromClause_strategy)
@settings(max_examples=50)
def test_jdoql_subqueryfromclause_instantiation(instance):
    assert isinstance(instance, jDOQL_SubqueryFromClause)



@given(instance=jDOQL_SubqueryFromClause_strategy)
def test_jdoql_subqueryfromclause_isExcludeSubclasses_setter(instance):
    original = instance.isExcludeSubclasses
    instance.isExcludeSubclasses = original
    assert instance.isExcludeSubclasses == original



@given(instance=jDOQL_SubqueryFromClause_strategy)
def test_jdoql_subqueryfromclause_candidateClassName_setter(instance):
    original = instance.candidateClassName
    instance.candidateClassName = original
    assert instance.candidateClassName == original

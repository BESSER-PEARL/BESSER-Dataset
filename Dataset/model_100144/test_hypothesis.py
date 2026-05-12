import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jDOQL::OrderBySpec,
    jDOQL::HavingClause,
    jDOQL::ParameterDeclaration,
    OrderBySpec,
    ResultSpec,
    jDOQL::ResultNaming,
    jDOQL::Expression,
    jDOQL::SubqueryResultClause,
    jDOQL::ResultSpec,
    jDOQL::ResultClause,
    jDOQL::IntoClause,
    jDOQL::EObject,
    SubquerySelectClause,
    jDOQL::VariableDeclaration,
    jDOQL::SubquerySelectClause,
    jDOQL::Alias,
    Expression,
    jDOQL::SimpleAndExpression,
    jDOQL::ComparisonOperatorExpression,
    jDOQL::ConditionalOrExpression,
    jDOQL::FieldAccessExpression,
    jDOQL::AdditionExpression,
    jDOQL::SimpleOrExpression,
    jDOQL::MultiplicationExpression,
    jDOQL::ConditionalAndExpression,
    jDOQL::Subquery,
    jDOQL::RangeClause,
    jDOQL::OrderByClause,
    jDOQL::GroupByClause,
    jDOQL::ImportClause,
    jDOQL::ParametersClause,
    jDOQL::VariablesClause,
    jDOQL::WhereClause,
    jDOQL::FromClause,
    jDOQL::SelectClause,
    jDOQL::SingleStringJDOQL,
    jDOQL::SubqueryFromClause,
    UnaryOperator,
    OrderByDirection,
    ComparisonOperator,
    AdditionOperator,
    MultiplicationOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jdoql::orderbyspec_is_not_abstract():
    assert not inspect.isabstract(jDOQL::OrderBySpec)


def test_jdoql::orderbyspec_constructor_exists():
    assert callable(jDOQL::OrderBySpec.__init__)


def test_jdoql::orderbyspec_constructor_args():
    sig = inspect.signature(jDOQL::OrderBySpec.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::havingclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::HavingClause)


def test_jdoql::havingclause_constructor_exists():
    assert callable(jDOQL::HavingClause.__init__)


def test_jdoql::havingclause_constructor_args():
    sig = inspect.signature(jDOQL::HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ParameterDeclaration)


def test_jdoql::parameterdeclaration_constructor_exists():
    assert callable(jDOQL::ParameterDeclaration.__init__)


def test_jdoql::parameterdeclaration_constructor_args():
    sig = inspect.signature(jDOQL::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "declaredParameterName" in params, "Missing parameter 'declaredParameterName'"
    assert "type" in params, "Missing parameter 'type'"

def test_jdoql::parameterdeclaration_has_declaredParameterName():
    assert hasattr(jDOQL::ParameterDeclaration, "declaredParameterName")
    descriptor = None
    for klass in jDOQL::ParameterDeclaration.__mro__:
        if "declaredParameterName" in klass.__dict__:
            descriptor = klass.__dict__["declaredParameterName"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::parameterdeclaration_has_type():
    assert hasattr(jDOQL::ParameterDeclaration, "type")
    descriptor = None
    for klass in jDOQL::ParameterDeclaration.__mro__:
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



def test_jdoql::resultnaming_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ResultNaming)


def test_jdoql::resultnaming_constructor_exists():
    assert callable(jDOQL::ResultNaming.__init__)


def test_jdoql::resultnaming_constructor_args():
    sig = inspect.signature(jDOQL::ResultNaming.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdoql::resultnaming_has_identifier():
    assert hasattr(jDOQL::ResultNaming, "identifier")
    descriptor = None
    for klass in jDOQL::ResultNaming.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::expression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::Expression)


def test_jdoql::expression_constructor_exists():
    assert callable(jDOQL::Expression.__init__)


def test_jdoql::expression_constructor_args():
    sig = inspect.signature(jDOQL::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"
    assert "this" in params, "Missing parameter 'this'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "name" in params, "Missing parameter 'name'"
    assert "castType" in params, "Missing parameter 'castType'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"
    assert "id" in params, "Missing parameter 'id'"

def test_jdoql::expression_has_unaryOperator():
    assert hasattr(jDOQL::Expression, "unaryOperator")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_this():
    assert hasattr(jDOQL::Expression, "this")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_direction():
    assert hasattr(jDOQL::Expression, "direction")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_name():
    assert hasattr(jDOQL::Expression, "name")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_castType():
    assert hasattr(jDOQL::Expression, "castType")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "castType" in klass.__dict__:
            descriptor = klass.__dict__["castType"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_literal():
    assert hasattr(jDOQL::Expression, "literal")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_isDistinct():
    assert hasattr(jDOQL::Expression, "isDistinct")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_parameterName():
    assert hasattr(jDOQL::Expression, "parameterName")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::expression_has_id():
    assert hasattr(jDOQL::Expression, "id")
    descriptor = None
    for klass in jDOQL::Expression.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::subqueryresultclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SubqueryResultClause)


def test_jdoql::subqueryresultclause_constructor_exists():
    assert callable(jDOQL::SubqueryResultClause.__init__)


def test_jdoql::subqueryresultclause_constructor_args():
    sig = inspect.signature(jDOQL::SubqueryResultClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jdoql::subqueryresultclause_has_isDistinct():
    assert hasattr(jDOQL::SubqueryResultClause, "isDistinct")
    descriptor = None
    for klass in jDOQL::SubqueryResultClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::resultspec_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ResultSpec)


def test_jdoql::resultspec_constructor_exists():
    assert callable(jDOQL::ResultSpec.__init__)


def test_jdoql::resultspec_constructor_args():
    sig = inspect.signature(jDOQL::ResultSpec.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::resultclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ResultClause)


def test_jdoql::resultclause_constructor_exists():
    assert callable(jDOQL::ResultClause.__init__)


def test_jdoql::resultclause_constructor_args():
    sig = inspect.signature(jDOQL::ResultClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jdoql::resultclause_has_isDistinct():
    assert hasattr(jDOQL::ResultClause, "isDistinct")
    descriptor = None
    for klass in jDOQL::ResultClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::intoclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::IntoClause)


def test_jdoql::intoclause_constructor_exists():
    assert callable(jDOQL::IntoClause.__init__)


def test_jdoql::intoclause_constructor_args():
    sig = inspect.signature(jDOQL::IntoClause.__init__)
    params = list(sig.parameters.keys())
    assert "resultClassName" in params, "Missing parameter 'resultClassName'"

def test_jdoql::intoclause_has_resultClassName():
    assert hasattr(jDOQL::IntoClause, "resultClassName")
    descriptor = None
    for klass in jDOQL::IntoClause.__mro__:
        if "resultClassName" in klass.__dict__:
            descriptor = klass.__dict__["resultClassName"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::eobject_is_not_abstract():
    assert not inspect.isabstract(jDOQL::EObject)


def test_jdoql::eobject_constructor_exists():
    assert callable(jDOQL::EObject.__init__)


def test_jdoql::eobject_constructor_args():
    sig = inspect.signature(jDOQL::EObject.__init__)
    params = list(sig.parameters.keys())



def test_subqueryselectclause_is_not_abstract():
    assert not inspect.isabstract(SubquerySelectClause)


def test_subqueryselectclause_constructor_exists():
    assert callable(SubquerySelectClause.__init__)


def test_subqueryselectclause_constructor_args():
    sig = inspect.signature(SubquerySelectClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jDOQL::VariableDeclaration)


def test_jdoql::variabledeclaration_constructor_exists():
    assert callable(jDOQL::VariableDeclaration.__init__)


def test_jdoql::variabledeclaration_constructor_args():
    sig = inspect.signature(jDOQL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_jdoql::variabledeclaration_has_type():
    assert hasattr(jDOQL::VariableDeclaration, "type")
    descriptor = None
    for klass in jDOQL::VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::variabledeclaration_has_variableName():
    assert hasattr(jDOQL::VariableDeclaration, "variableName")
    descriptor = None
    for klass in jDOQL::VariableDeclaration.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::subqueryselectclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SubquerySelectClause)


def test_jdoql::subqueryselectclause_constructor_exists():
    assert callable(jDOQL::SubquerySelectClause.__init__)


def test_jdoql::subqueryselectclause_constructor_args():
    sig = inspect.signature(jDOQL::SubquerySelectClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::alias_is_not_abstract():
    assert not inspect.isabstract(jDOQL::Alias)


def test_jdoql::alias_constructor_exists():
    assert callable(jDOQL::Alias.__init__)


def test_jdoql::alias_constructor_args():
    sig = inspect.signature(jDOQL::Alias.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_jdoql::alias_has_identifier():
    assert hasattr(jDOQL::Alias, "identifier")
    descriptor = None
    for klass in jDOQL::Alias.__mro__:
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



def test_jdoql::simpleandexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SimpleAndExpression)


def test_jdoql::simpleandexpression_constructor_exists():
    assert callable(jDOQL::SimpleAndExpression.__init__)


def test_jdoql::simpleandexpression_constructor_args():
    sig = inspect.signature(jDOQL::SimpleAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ComparisonOperatorExpression)


def test_jdoql::comparisonoperatorexpression_constructor_exists():
    assert callable(jDOQL::ComparisonOperatorExpression.__init__)


def test_jdoql::comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(jDOQL::ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql::comparisonoperatorexpression_has_operator():
    assert hasattr(jDOQL::ComparisonOperatorExpression, "operator")
    descriptor = None
    for klass in jDOQL::ComparisonOperatorExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ConditionalOrExpression)


def test_jdoql::conditionalorexpression_constructor_exists():
    assert callable(jDOQL::ConditionalOrExpression.__init__)


def test_jdoql::conditionalorexpression_constructor_args():
    sig = inspect.signature(jDOQL::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::fieldaccessexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::FieldAccessExpression)


def test_jdoql::fieldaccessexpression_constructor_exists():
    assert callable(jDOQL::FieldAccessExpression.__init__)


def test_jdoql::fieldaccessexpression_constructor_args():
    sig = inspect.signature(jDOQL::FieldAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::additionexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::AdditionExpression)


def test_jdoql::additionexpression_constructor_exists():
    assert callable(jDOQL::AdditionExpression.__init__)


def test_jdoql::additionexpression_constructor_args():
    sig = inspect.signature(jDOQL::AdditionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql::additionexpression_has_operator():
    assert hasattr(jDOQL::AdditionExpression, "operator")
    descriptor = None
    for klass in jDOQL::AdditionExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::simpleorexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SimpleOrExpression)


def test_jdoql::simpleorexpression_constructor_exists():
    assert callable(jDOQL::SimpleOrExpression.__init__)


def test_jdoql::simpleorexpression_constructor_args():
    sig = inspect.signature(jDOQL::SimpleOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::MultiplicationExpression)


def test_jdoql::multiplicationexpression_constructor_exists():
    assert callable(jDOQL::MultiplicationExpression.__init__)


def test_jdoql::multiplicationexpression_constructor_args():
    sig = inspect.signature(jDOQL::MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jdoql::multiplicationexpression_has_operator():
    assert hasattr(jDOQL::MultiplicationExpression, "operator")
    descriptor = None
    for klass in jDOQL::MultiplicationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ConditionalAndExpression)


def test_jdoql::conditionalandexpression_constructor_exists():
    assert callable(jDOQL::ConditionalAndExpression.__init__)


def test_jdoql::conditionalandexpression_constructor_args():
    sig = inspect.signature(jDOQL::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::subquery_is_not_abstract():
    assert not inspect.isabstract(jDOQL::Subquery)


def test_jdoql::subquery_constructor_exists():
    assert callable(jDOQL::Subquery.__init__)


def test_jdoql::subquery_constructor_args():
    sig = inspect.signature(jDOQL::Subquery.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::rangeclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::RangeClause)


def test_jdoql::rangeclause_constructor_exists():
    assert callable(jDOQL::RangeClause.__init__)


def test_jdoql::rangeclause_constructor_args():
    sig = inspect.signature(jDOQL::RangeClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::orderbyclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::OrderByClause)


def test_jdoql::orderbyclause_constructor_exists():
    assert callable(jDOQL::OrderByClause.__init__)


def test_jdoql::orderbyclause_constructor_args():
    sig = inspect.signature(jDOQL::OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::groupbyclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::GroupByClause)


def test_jdoql::groupbyclause_constructor_exists():
    assert callable(jDOQL::GroupByClause.__init__)


def test_jdoql::groupbyclause_constructor_args():
    sig = inspect.signature(jDOQL::GroupByClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::importclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ImportClause)


def test_jdoql::importclause_constructor_exists():
    assert callable(jDOQL::ImportClause.__init__)


def test_jdoql::importclause_constructor_args():
    sig = inspect.signature(jDOQL::ImportClause.__init__)
    params = list(sig.parameters.keys())
    assert "importDeclarations" in params, "Missing parameter 'importDeclarations'"

def test_jdoql::importclause_has_importDeclarations():
    assert hasattr(jDOQL::ImportClause, "importDeclarations")
    descriptor = None
    for klass in jDOQL::ImportClause.__mro__:
        if "importDeclarations" in klass.__dict__:
            descriptor = klass.__dict__["importDeclarations"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::parametersclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::ParametersClause)


def test_jdoql::parametersclause_constructor_exists():
    assert callable(jDOQL::ParametersClause.__init__)


def test_jdoql::parametersclause_constructor_args():
    sig = inspect.signature(jDOQL::ParametersClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::variablesclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::VariablesClause)


def test_jdoql::variablesclause_constructor_exists():
    assert callable(jDOQL::VariablesClause.__init__)


def test_jdoql::variablesclause_constructor_args():
    sig = inspect.signature(jDOQL::VariablesClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::whereclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::WhereClause)


def test_jdoql::whereclause_constructor_exists():
    assert callable(jDOQL::WhereClause.__init__)


def test_jdoql::whereclause_constructor_args():
    sig = inspect.signature(jDOQL::WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::fromclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::FromClause)


def test_jdoql::fromclause_constructor_exists():
    assert callable(jDOQL::FromClause.__init__)


def test_jdoql::fromclause_constructor_args():
    sig = inspect.signature(jDOQL::FromClause.__init__)
    params = list(sig.parameters.keys())
    assert "isExcludeSubclasses" in params, "Missing parameter 'isExcludeSubclasses'"
    assert "candidateClassName" in params, "Missing parameter 'candidateClassName'"

def test_jdoql::fromclause_has_isExcludeSubclasses():
    assert hasattr(jDOQL::FromClause, "isExcludeSubclasses")
    descriptor = None
    for klass in jDOQL::FromClause.__mro__:
        if "isExcludeSubclasses" in klass.__dict__:
            descriptor = klass.__dict__["isExcludeSubclasses"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::fromclause_has_candidateClassName():
    assert hasattr(jDOQL::FromClause, "candidateClassName")
    descriptor = None
    for klass in jDOQL::FromClause.__mro__:
        if "candidateClassName" in klass.__dict__:
            descriptor = klass.__dict__["candidateClassName"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::selectclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SelectClause)


def test_jdoql::selectclause_constructor_exists():
    assert callable(jDOQL::SelectClause.__init__)


def test_jdoql::selectclause_constructor_args():
    sig = inspect.signature(jDOQL::SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_jdoql::selectclause_has_isUnique():
    assert hasattr(jDOQL::SelectClause, "isUnique")
    descriptor = None
    for klass in jDOQL::SelectClause.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_jdoql::singlestringjdoql_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SingleStringJDOQL)


def test_jdoql::singlestringjdoql_constructor_exists():
    assert callable(jDOQL::SingleStringJDOQL.__init__)


def test_jdoql::singlestringjdoql_constructor_args():
    sig = inspect.signature(jDOQL::SingleStringJDOQL.__init__)
    params = list(sig.parameters.keys())



def test_jdoql::subqueryfromclause_is_not_abstract():
    assert not inspect.isabstract(jDOQL::SubqueryFromClause)


def test_jdoql::subqueryfromclause_constructor_exists():
    assert callable(jDOQL::SubqueryFromClause.__init__)


def test_jdoql::subqueryfromclause_constructor_args():
    sig = inspect.signature(jDOQL::SubqueryFromClause.__init__)
    params = list(sig.parameters.keys())
    assert "isExcludeSubclasses" in params, "Missing parameter 'isExcludeSubclasses'"
    assert "candidateClassName" in params, "Missing parameter 'candidateClassName'"

def test_jdoql::subqueryfromclause_has_isExcludeSubclasses():
    assert hasattr(jDOQL::SubqueryFromClause, "isExcludeSubclasses")
    descriptor = None
    for klass in jDOQL::SubqueryFromClause.__mro__:
        if "isExcludeSubclasses" in klass.__dict__:
            descriptor = klass.__dict__["isExcludeSubclasses"]
            break
    assert isinstance(descriptor, property)

def test_jdoql::subqueryfromclause_has_candidateClassName():
    assert hasattr(jDOQL::SubqueryFromClause, "candidateClassName")
    descriptor = None
    for klass in jDOQL::SubqueryFromClause.__mro__:
        if "candidateClassName" in klass.__dict__:
            descriptor = klass.__dict__["candidateClassName"]
            break
    assert isinstance(descriptor, property)

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "bitwiseNot",
        "negative",
        "logicalNot",
        "positive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_orderbydirection_exists():
    # Check that the Enumeration exists
    assert OrderByDirection is not None

def test_orderbydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderByDirection]
    expected_literals = [
        "descending",
        "desc",
        "asc",
        "ascending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderByDirection"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "lessEqual",
        "equal",
        "greaterEqual",
        "greaterThen",
        "instanceof",
        "notEqual",
        "lessThen",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

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

def test_multiplicationoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicationOperator is not None

def test_multiplicationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicationOperator]
    expected_literals = [
        "modulo",
        "multiply",
        "divide",
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
jDOQL::OrderBySpec_strategy = st.builds(
    jDOQL::OrderBySpec,
)
jDOQL::HavingClause_strategy = st.builds(
    jDOQL::HavingClause,
)
jDOQL::ParameterDeclaration_strategy = st.builds(
    jDOQL::ParameterDeclaration,
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
jDOQL::ResultNaming_strategy = st.builds(
    jDOQL::ResultNaming,
    identifier=
        safe_text
)
jDOQL::Expression_strategy = st.builds(
    jDOQL::Expression,
    unaryOperator=
        safe_text,
    this=
        safe_text,
    direction=
        safe_text,
    name=
        safe_text,
    castType=
        safe_text,
    literal=
        safe_text,
    isDistinct=
        st.booleans(),
    parameterName=
        safe_text,
    id=
        safe_text
)
jDOQL::SubqueryResultClause_strategy = st.builds(
    jDOQL::SubqueryResultClause,
    isDistinct=
        st.booleans()
)
jDOQL::ResultSpec_strategy = st.builds(
    jDOQL::ResultSpec,
)
jDOQL::ResultClause_strategy = st.builds(
    jDOQL::ResultClause,
    isDistinct=
        st.booleans()
)
jDOQL::IntoClause_strategy = st.builds(
    jDOQL::IntoClause,
    resultClassName=
        safe_text
)
jDOQL::EObject_strategy = st.builds(
    jDOQL::EObject,
)
SubquerySelectClause_strategy = st.builds(
    SubquerySelectClause,
)
jDOQL::VariableDeclaration_strategy = st.builds(
    jDOQL::VariableDeclaration,
    type=
        safe_text,
    variableName=
        safe_text
)
jDOQL::SubquerySelectClause_strategy = st.builds(
    jDOQL::SubquerySelectClause,
)
jDOQL::Alias_strategy = st.builds(
    jDOQL::Alias,
    identifier=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
jDOQL::SimpleAndExpression_strategy = st.builds(
    jDOQL::SimpleAndExpression,
)
jDOQL::ComparisonOperatorExpression_strategy = st.builds(
    jDOQL::ComparisonOperatorExpression,
    operator=
        safe_text
)
jDOQL::ConditionalOrExpression_strategy = st.builds(
    jDOQL::ConditionalOrExpression,
)
jDOQL::FieldAccessExpression_strategy = st.builds(
    jDOQL::FieldAccessExpression,
)
jDOQL::AdditionExpression_strategy = st.builds(
    jDOQL::AdditionExpression,
    operator=
        safe_text
)
jDOQL::SimpleOrExpression_strategy = st.builds(
    jDOQL::SimpleOrExpression,
)
jDOQL::MultiplicationExpression_strategy = st.builds(
    jDOQL::MultiplicationExpression,
    operator=
        safe_text
)
jDOQL::ConditionalAndExpression_strategy = st.builds(
    jDOQL::ConditionalAndExpression,
)
jDOQL::Subquery_strategy = st.builds(
    jDOQL::Subquery,
)
jDOQL::RangeClause_strategy = st.builds(
    jDOQL::RangeClause,
)
jDOQL::OrderByClause_strategy = st.builds(
    jDOQL::OrderByClause,
)
jDOQL::GroupByClause_strategy = st.builds(
    jDOQL::GroupByClause,
)
jDOQL::ImportClause_strategy = st.builds(
    jDOQL::ImportClause,
    importDeclarations=
        safe_text
)
jDOQL::ParametersClause_strategy = st.builds(
    jDOQL::ParametersClause,
)
jDOQL::VariablesClause_strategy = st.builds(
    jDOQL::VariablesClause,
)
jDOQL::WhereClause_strategy = st.builds(
    jDOQL::WhereClause,
)
jDOQL::FromClause_strategy = st.builds(
    jDOQL::FromClause,
    isExcludeSubclasses=
        st.booleans(),
    candidateClassName=
        safe_text
)
jDOQL::SelectClause_strategy = st.builds(
    jDOQL::SelectClause,
    isUnique=
        st.booleans()
)
jDOQL::SingleStringJDOQL_strategy = st.builds(
    jDOQL::SingleStringJDOQL,
)
jDOQL::SubqueryFromClause_strategy = st.builds(
    jDOQL::SubqueryFromClause,
    isExcludeSubclasses=
        st.booleans(),
    candidateClassName=
        safe_text
)

@given(instance=jDOQL::OrderBySpec_strategy)
@settings(max_examples=50)
def test_jdoql::orderbyspec_instantiation(instance):
    assert isinstance(instance, jDOQL::OrderBySpec)

@given(instance=jDOQL::HavingClause_strategy)
@settings(max_examples=50)
def test_jdoql::havingclause_instantiation(instance):
    assert isinstance(instance, jDOQL::HavingClause)

@given(instance=jDOQL::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_jdoql::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, jDOQL::ParameterDeclaration)

@given(instance=jDOQL::ParameterDeclaration_strategy)
def test_jdoql::parameterdeclaration_declaredParameterName_type(instance):
    assert isinstance(instance.declaredParameterName, str)


@given(instance=jDOQL::ParameterDeclaration_strategy)
def test_jdoql::parameterdeclaration_declaredParameterName_setter(instance):
    original = instance.declaredParameterName
    instance.declaredParameterName = original
    assert instance.declaredParameterName == original

@given(instance=jDOQL::ParameterDeclaration_strategy)
def test_jdoql::parameterdeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jDOQL::ParameterDeclaration_strategy)
def test_jdoql::parameterdeclaration_type_setter(instance):
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

@given(instance=jDOQL::ResultNaming_strategy)
@settings(max_examples=50)
def test_jdoql::resultnaming_instantiation(instance):
    assert isinstance(instance, jDOQL::ResultNaming)

@given(instance=jDOQL::ResultNaming_strategy)
def test_jdoql::resultnaming_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=jDOQL::ResultNaming_strategy)
def test_jdoql::resultnaming_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=jDOQL::Expression_strategy)
@settings(max_examples=50)
def test_jdoql::expression_instantiation(instance):
    assert isinstance(instance, jDOQL::Expression)

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_unaryOperator_type(instance):
    assert isinstance(instance.unaryOperator, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_this_type(instance):
    assert isinstance(instance.this, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_castType_type(instance):
    assert isinstance(instance.castType, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_castType_setter(instance):
    original = instance.castType
    instance.castType = original
    assert instance.castType == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_isDistinct_type(instance):
    assert isinstance(instance.isDistinct, bool)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_parameterName_type(instance):
    assert isinstance(instance.parameterName, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original

@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=jDOQL::Expression_strategy)
def test_jdoql::expression_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jDOQL::SubqueryResultClause_strategy)
@settings(max_examples=50)
def test_jdoql::subqueryresultclause_instantiation(instance):
    assert isinstance(instance, jDOQL::SubqueryResultClause)

@given(instance=jDOQL::SubqueryResultClause_strategy)
def test_jdoql::subqueryresultclause_isDistinct_type(instance):
    assert isinstance(instance.isDistinct, bool)


@given(instance=jDOQL::SubqueryResultClause_strategy)
def test_jdoql::subqueryresultclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jDOQL::ResultSpec_strategy)
@settings(max_examples=50)
def test_jdoql::resultspec_instantiation(instance):
    assert isinstance(instance, jDOQL::ResultSpec)

@given(instance=jDOQL::ResultClause_strategy)
@settings(max_examples=50)
def test_jdoql::resultclause_instantiation(instance):
    assert isinstance(instance, jDOQL::ResultClause)

@given(instance=jDOQL::ResultClause_strategy)
def test_jdoql::resultclause_isDistinct_type(instance):
    assert isinstance(instance.isDistinct, bool)


@given(instance=jDOQL::ResultClause_strategy)
def test_jdoql::resultclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jDOQL::IntoClause_strategy)
@settings(max_examples=50)
def test_jdoql::intoclause_instantiation(instance):
    assert isinstance(instance, jDOQL::IntoClause)

@given(instance=jDOQL::IntoClause_strategy)
def test_jdoql::intoclause_resultClassName_type(instance):
    assert isinstance(instance.resultClassName, str)


@given(instance=jDOQL::IntoClause_strategy)
def test_jdoql::intoclause_resultClassName_setter(instance):
    original = instance.resultClassName
    instance.resultClassName = original
    assert instance.resultClassName == original

@given(instance=jDOQL::EObject_strategy)
@settings(max_examples=50)
def test_jdoql::eobject_instantiation(instance):
    assert isinstance(instance, jDOQL::EObject)

@given(instance=SubquerySelectClause_strategy)
@settings(max_examples=50)
def test_subqueryselectclause_instantiation(instance):
    assert isinstance(instance, SubquerySelectClause)

@given(instance=jDOQL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jdoql::variabledeclaration_instantiation(instance):
    assert isinstance(instance, jDOQL::VariableDeclaration)

@given(instance=jDOQL::VariableDeclaration_strategy)
def test_jdoql::variabledeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=jDOQL::VariableDeclaration_strategy)
def test_jdoql::variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jDOQL::VariableDeclaration_strategy)
def test_jdoql::variabledeclaration_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=jDOQL::VariableDeclaration_strategy)
def test_jdoql::variabledeclaration_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=jDOQL::SubquerySelectClause_strategy)
@settings(max_examples=50)
def test_jdoql::subqueryselectclause_instantiation(instance):
    assert isinstance(instance, jDOQL::SubquerySelectClause)

@given(instance=jDOQL::Alias_strategy)
@settings(max_examples=50)
def test_jdoql::alias_instantiation(instance):
    assert isinstance(instance, jDOQL::Alias)

@given(instance=jDOQL::Alias_strategy)
def test_jdoql::alias_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=jDOQL::Alias_strategy)
def test_jdoql::alias_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=jDOQL::SimpleAndExpression_strategy)
@settings(max_examples=50)
def test_jdoql::simpleandexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::SimpleAndExpression)

@given(instance=jDOQL::ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_jdoql::comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::ComparisonOperatorExpression)

@given(instance=jDOQL::ComparisonOperatorExpression_strategy)
def test_jdoql::comparisonoperatorexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=jDOQL::ComparisonOperatorExpression_strategy)
def test_jdoql::comparisonoperatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_jdoql::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::ConditionalOrExpression)

@given(instance=jDOQL::FieldAccessExpression_strategy)
@settings(max_examples=50)
def test_jdoql::fieldaccessexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::FieldAccessExpression)

@given(instance=jDOQL::AdditionExpression_strategy)
@settings(max_examples=50)
def test_jdoql::additionexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::AdditionExpression)

@given(instance=jDOQL::AdditionExpression_strategy)
def test_jdoql::additionexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=jDOQL::AdditionExpression_strategy)
def test_jdoql::additionexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL::SimpleOrExpression_strategy)
@settings(max_examples=50)
def test_jdoql::simpleorexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::SimpleOrExpression)

@given(instance=jDOQL::MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_jdoql::multiplicationexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::MultiplicationExpression)

@given(instance=jDOQL::MultiplicationExpression_strategy)
def test_jdoql::multiplicationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=jDOQL::MultiplicationExpression_strategy)
def test_jdoql::multiplicationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jDOQL::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_jdoql::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, jDOQL::ConditionalAndExpression)

@given(instance=jDOQL::Subquery_strategy)
@settings(max_examples=50)
def test_jdoql::subquery_instantiation(instance):
    assert isinstance(instance, jDOQL::Subquery)

@given(instance=jDOQL::RangeClause_strategy)
@settings(max_examples=50)
def test_jdoql::rangeclause_instantiation(instance):
    assert isinstance(instance, jDOQL::RangeClause)

@given(instance=jDOQL::OrderByClause_strategy)
@settings(max_examples=50)
def test_jdoql::orderbyclause_instantiation(instance):
    assert isinstance(instance, jDOQL::OrderByClause)

@given(instance=jDOQL::GroupByClause_strategy)
@settings(max_examples=50)
def test_jdoql::groupbyclause_instantiation(instance):
    assert isinstance(instance, jDOQL::GroupByClause)

@given(instance=jDOQL::ImportClause_strategy)
@settings(max_examples=50)
def test_jdoql::importclause_instantiation(instance):
    assert isinstance(instance, jDOQL::ImportClause)

@given(instance=jDOQL::ImportClause_strategy)
def test_jdoql::importclause_importDeclarations_type(instance):
    assert isinstance(instance.importDeclarations, str)


@given(instance=jDOQL::ImportClause_strategy)
def test_jdoql::importclause_importDeclarations_setter(instance):
    original = instance.importDeclarations
    instance.importDeclarations = original
    assert instance.importDeclarations == original

@given(instance=jDOQL::ParametersClause_strategy)
@settings(max_examples=50)
def test_jdoql::parametersclause_instantiation(instance):
    assert isinstance(instance, jDOQL::ParametersClause)

@given(instance=jDOQL::VariablesClause_strategy)
@settings(max_examples=50)
def test_jdoql::variablesclause_instantiation(instance):
    assert isinstance(instance, jDOQL::VariablesClause)

@given(instance=jDOQL::WhereClause_strategy)
@settings(max_examples=50)
def test_jdoql::whereclause_instantiation(instance):
    assert isinstance(instance, jDOQL::WhereClause)

@given(instance=jDOQL::FromClause_strategy)
@settings(max_examples=50)
def test_jdoql::fromclause_instantiation(instance):
    assert isinstance(instance, jDOQL::FromClause)

@given(instance=jDOQL::FromClause_strategy)
def test_jdoql::fromclause_isExcludeSubclasses_type(instance):
    assert isinstance(instance.isExcludeSubclasses, bool)


@given(instance=jDOQL::FromClause_strategy)
def test_jdoql::fromclause_isExcludeSubclasses_setter(instance):
    original = instance.isExcludeSubclasses
    instance.isExcludeSubclasses = original
    assert instance.isExcludeSubclasses == original

@given(instance=jDOQL::FromClause_strategy)
def test_jdoql::fromclause_candidateClassName_type(instance):
    assert isinstance(instance.candidateClassName, str)


@given(instance=jDOQL::FromClause_strategy)
def test_jdoql::fromclause_candidateClassName_setter(instance):
    original = instance.candidateClassName
    instance.candidateClassName = original
    assert instance.candidateClassName == original

@given(instance=jDOQL::SelectClause_strategy)
@settings(max_examples=50)
def test_jdoql::selectclause_instantiation(instance):
    assert isinstance(instance, jDOQL::SelectClause)

@given(instance=jDOQL::SelectClause_strategy)
def test_jdoql::selectclause_isUnique_type(instance):
    assert isinstance(instance.isUnique, bool)


@given(instance=jDOQL::SelectClause_strategy)
def test_jdoql::selectclause_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=jDOQL::SingleStringJDOQL_strategy)
@settings(max_examples=50)
def test_jdoql::singlestringjdoql_instantiation(instance):
    assert isinstance(instance, jDOQL::SingleStringJDOQL)

@given(instance=jDOQL::SubqueryFromClause_strategy)
@settings(max_examples=50)
def test_jdoql::subqueryfromclause_instantiation(instance):
    assert isinstance(instance, jDOQL::SubqueryFromClause)

@given(instance=jDOQL::SubqueryFromClause_strategy)
def test_jdoql::subqueryfromclause_isExcludeSubclasses_type(instance):
    assert isinstance(instance.isExcludeSubclasses, bool)


@given(instance=jDOQL::SubqueryFromClause_strategy)
def test_jdoql::subqueryfromclause_isExcludeSubclasses_setter(instance):
    original = instance.isExcludeSubclasses
    instance.isExcludeSubclasses = original
    assert instance.isExcludeSubclasses == original

@given(instance=jDOQL::SubqueryFromClause_strategy)
def test_jdoql::subqueryfromclause_candidateClassName_type(instance):
    assert isinstance(instance.candidateClassName, str)


@given(instance=jDOQL::SubqueryFromClause_strategy)
def test_jdoql::subqueryfromclause_candidateClassName_setter(instance):
    original = instance.candidateClassName
    instance.candidateClassName = original
    assert instance.candidateClassName == original

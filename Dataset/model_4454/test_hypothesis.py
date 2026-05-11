import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CompareOperator,
    arduinoDSL::Greater,
    arduinoDSL::NotEquals,
    arduinoDSL::SmallerThanEquals,
    arduinoDSL::Smaller,
    arduinoDSL::GreaterThanEquals,
    arduinoDSL::Equals,
    BooleanOperator,
    arduinoDSL::Or,
    arduinoDSL::And,
    arduinoDSL::Range,
    arduinoDSL::Smoothing,
    arduinoDSL::Map,
    arduinoDSL::Rate,
    arduinoDSL::ComponentBody,
    arduinoDSL::Board,
    arduinoDSL::NodeDefinition,
    arduinoDSL::Cast,
    SimpleStatement,
    arduinoDSL::VariableDeclaration,
    arduinoDSL::Assignment,
    arduinoDSL::SimpleStatement,
    arduinoDSL::State,
    arduinoDSL::BooleanLiteral,
    arduinoDSL::Component,
    arduinoDSL::Node,
    Value,
    arduinoDSL::NumberLiteral,
    arduinoDSL::Delta,
    arduinoDSL::VariableReference,
    arduinoDSL::Attribute,
    NumberExpression,
    arduinoDSL::Mod,
    arduinoDSL::Plus,
    arduinoDSL::Minus,
    arduinoDSL::Mult,
    arduinoDSL::Div,
    arduinoDSL::Value,
    arduinoDSL::NumberExpressionBlock,
    arduinoDSL::CompareOperator,
    arduinoDSL::BooleanOperator,
    BooleanExpression,
    arduinoDSL::Comparison,
    arduinoDSL::AndOr,
    arduinoDSL::BooleanExpressionBlock,
    arduinoDSL::NumberExpression,
    arduinoDSL::RuleBody,
    arduinoDSL::BooleanExpression,
    arduinoDSL::Rule,
    arduinoDSL::EObject,
    arduinoDSL::Program,
    VariableReference,
    arduinoDSL::VarRef,
    arduinoDSL::ElseStatement,
    arduinoDSL::ElseIfStatement,
    arduinoDSL::IfStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_compareoperator_is_not_abstract():
    assert not inspect.isabstract(CompareOperator)


def test_compareoperator_constructor_exists():
    assert callable(CompareOperator.__init__)


def test_compareoperator_constructor_args():
    sig = inspect.signature(CompareOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::greater_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Greater)


def test_arduinodsl::greater_constructor_exists():
    assert callable(arduinoDSL::Greater.__init__)


def test_arduinodsl::greater_constructor_args():
    sig = inspect.signature(arduinoDSL::Greater.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::notequals_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::NotEquals)


def test_arduinodsl::notequals_constructor_exists():
    assert callable(arduinoDSL::NotEquals.__init__)


def test_arduinodsl::notequals_constructor_args():
    sig = inspect.signature(arduinoDSL::NotEquals.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::smallerthanequals_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::SmallerThanEquals)


def test_arduinodsl::smallerthanequals_constructor_exists():
    assert callable(arduinoDSL::SmallerThanEquals.__init__)


def test_arduinodsl::smallerthanequals_constructor_args():
    sig = inspect.signature(arduinoDSL::SmallerThanEquals.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::smaller_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Smaller)


def test_arduinodsl::smaller_constructor_exists():
    assert callable(arduinoDSL::Smaller.__init__)


def test_arduinodsl::smaller_constructor_args():
    sig = inspect.signature(arduinoDSL::Smaller.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::greaterthanequals_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::GreaterThanEquals)


def test_arduinodsl::greaterthanequals_constructor_exists():
    assert callable(arduinoDSL::GreaterThanEquals.__init__)


def test_arduinodsl::greaterthanequals_constructor_args():
    sig = inspect.signature(arduinoDSL::GreaterThanEquals.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::equals_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Equals)


def test_arduinodsl::equals_constructor_exists():
    assert callable(arduinoDSL::Equals.__init__)


def test_arduinodsl::equals_constructor_args():
    sig = inspect.signature(arduinoDSL::Equals.__init__)
    params = list(sig.parameters.keys())



def test_booleanoperator_is_not_abstract():
    assert not inspect.isabstract(BooleanOperator)


def test_booleanoperator_constructor_exists():
    assert callable(BooleanOperator.__init__)


def test_booleanoperator_constructor_args():
    sig = inspect.signature(BooleanOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::or_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Or)


def test_arduinodsl::or_constructor_exists():
    assert callable(arduinoDSL::Or.__init__)


def test_arduinodsl::or_constructor_args():
    sig = inspect.signature(arduinoDSL::Or.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::and_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::And)


def test_arduinodsl::and_constructor_exists():
    assert callable(arduinoDSL::And.__init__)


def test_arduinodsl::and_constructor_args():
    sig = inspect.signature(arduinoDSL::And.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::range_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Range)


def test_arduinodsl::range_constructor_exists():
    assert callable(arduinoDSL::Range.__init__)


def test_arduinodsl::range_constructor_args():
    sig = inspect.signature(arduinoDSL::Range.__init__)
    params = list(sig.parameters.keys())
    assert "low" in params, "Missing parameter 'low'"
    assert "high" in params, "Missing parameter 'high'"

def test_arduinodsl::range_has_low():
    assert hasattr(arduinoDSL::Range, "low")
    descriptor = None
    for klass in arduinoDSL::Range.__mro__:
        if "low" in klass.__dict__:
            descriptor = klass.__dict__["low"]
            break
    assert isinstance(descriptor, property)

def test_arduinodsl::range_has_high():
    assert hasattr(arduinoDSL::Range, "high")
    descriptor = None
    for klass in arduinoDSL::Range.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::smoothing_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Smoothing)


def test_arduinodsl::smoothing_constructor_exists():
    assert callable(arduinoDSL::Smoothing.__init__)


def test_arduinodsl::smoothing_constructor_args():
    sig = inspect.signature(arduinoDSL::Smoothing.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinodsl::smoothing_has_value():
    assert hasattr(arduinoDSL::Smoothing, "value")
    descriptor = None
    for klass in arduinoDSL::Smoothing.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::map_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Map)


def test_arduinodsl::map_constructor_exists():
    assert callable(arduinoDSL::Map.__init__)


def test_arduinodsl::map_constructor_args():
    sig = inspect.signature(arduinoDSL::Map.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::rate_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Rate)


def test_arduinodsl::rate_constructor_exists():
    assert callable(arduinoDSL::Rate.__init__)


def test_arduinodsl::rate_constructor_args():
    sig = inspect.signature(arduinoDSL::Rate.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinodsl::rate_has_value():
    assert hasattr(arduinoDSL::Rate, "value")
    descriptor = None
    for klass in arduinoDSL::Rate.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::componentbody_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::ComponentBody)


def test_arduinodsl::componentbody_constructor_exists():
    assert callable(arduinoDSL::ComponentBody.__init__)


def test_arduinodsl::componentbody_constructor_args():
    sig = inspect.signature(arduinoDSL::ComponentBody.__init__)
    params = list(sig.parameters.keys())
    assert "io" in params, "Missing parameter 'io'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduinodsl::componentbody_has_io():
    assert hasattr(arduinoDSL::ComponentBody, "io")
    descriptor = None
    for klass in arduinoDSL::ComponentBody.__mro__:
        if "io" in klass.__dict__:
            descriptor = klass.__dict__["io"]
            break
    assert isinstance(descriptor, property)

def test_arduinodsl::componentbody_has_type():
    assert hasattr(arduinoDSL::ComponentBody, "type")
    descriptor = None
    for klass in arduinoDSL::ComponentBody.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_arduinodsl::componentbody_has_pin():
    assert hasattr(arduinoDSL::ComponentBody, "pin")
    descriptor = None
    for klass in arduinoDSL::ComponentBody.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::board_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Board)


def test_arduinodsl::board_constructor_exists():
    assert callable(arduinoDSL::Board.__init__)


def test_arduinodsl::board_constructor_args():
    sig = inspect.signature(arduinoDSL::Board.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_arduinodsl::board_has_b():
    assert hasattr(arduinoDSL::Board, "b")
    descriptor = None
    for klass in arduinoDSL::Board.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::nodedefinition_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::NodeDefinition)


def test_arduinodsl::nodedefinition_constructor_exists():
    assert callable(arduinoDSL::NodeDefinition.__init__)


def test_arduinodsl::nodedefinition_constructor_args():
    sig = inspect.signature(arduinoDSL::NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::cast_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Cast)


def test_arduinodsl::cast_constructor_exists():
    assert callable(arduinoDSL::Cast.__init__)


def test_arduinodsl::cast_constructor_args():
    sig = inspect.signature(arduinoDSL::Cast.__init__)
    params = list(sig.parameters.keys())
    assert "castType" in params, "Missing parameter 'castType'"

def test_arduinodsl::cast_has_castType():
    assert hasattr(arduinoDSL::Cast, "castType")
    descriptor = None
    for klass in arduinoDSL::Cast.__mro__:
        if "castType" in klass.__dict__:
            descriptor = klass.__dict__["castType"]
            break
    assert isinstance(descriptor, property)



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::VariableDeclaration)


def test_arduinodsl::variabledeclaration_constructor_exists():
    assert callable(arduinoDSL::VariableDeclaration.__init__)


def test_arduinodsl::variabledeclaration_constructor_args():
    sig = inspect.signature(arduinoDSL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_arduinodsl::variabledeclaration_has_type():
    assert hasattr(arduinoDSL::VariableDeclaration, "type")
    descriptor = None
    for klass in arduinoDSL::VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_arduinodsl::variabledeclaration_has_name():
    assert hasattr(arduinoDSL::VariableDeclaration, "name")
    descriptor = None
    for klass in arduinoDSL::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::assignment_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Assignment)


def test_arduinodsl::assignment_constructor_exists():
    assert callable(arduinoDSL::Assignment.__init__)


def test_arduinodsl::assignment_constructor_args():
    sig = inspect.signature(arduinoDSL::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::simplestatement_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::SimpleStatement)


def test_arduinodsl::simplestatement_constructor_exists():
    assert callable(arduinoDSL::SimpleStatement.__init__)


def test_arduinodsl::simplestatement_constructor_args():
    sig = inspect.signature(arduinoDSL::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::state_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::State)


def test_arduinodsl::state_constructor_exists():
    assert callable(arduinoDSL::State.__init__)


def test_arduinodsl::state_constructor_args():
    sig = inspect.signature(arduinoDSL::State.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinodsl::state_has_value():
    assert hasattr(arduinoDSL::State, "value")
    descriptor = None
    for klass in arduinoDSL::State.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::BooleanLiteral)


def test_arduinodsl::booleanliteral_constructor_exists():
    assert callable(arduinoDSL::BooleanLiteral.__init__)


def test_arduinodsl::booleanliteral_constructor_args():
    sig = inspect.signature(arduinoDSL::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduinodsl::booleanliteral_has_value():
    assert hasattr(arduinoDSL::BooleanLiteral, "value")
    descriptor = None
    for klass in arduinoDSL::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::component_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Component)


def test_arduinodsl::component_constructor_exists():
    assert callable(arduinoDSL::Component.__init__)


def test_arduinodsl::component_constructor_args():
    sig = inspect.signature(arduinoDSL::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinodsl::component_has_name():
    assert hasattr(arduinoDSL::Component, "name")
    descriptor = None
    for klass in arduinoDSL::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::node_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Node)


def test_arduinodsl::node_constructor_exists():
    assert callable(arduinoDSL::Node.__init__)


def test_arduinodsl::node_constructor_args():
    sig = inspect.signature(arduinoDSL::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduinodsl::node_has_name():
    assert hasattr(arduinoDSL::Node, "name")
    descriptor = None
    for klass in arduinoDSL::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::numberliteral_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::NumberLiteral)


def test_arduinodsl::numberliteral_constructor_exists():
    assert callable(arduinoDSL::NumberLiteral.__init__)


def test_arduinodsl::numberliteral_constructor_args():
    sig = inspect.signature(arduinoDSL::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "intVal" in params, "Missing parameter 'intVal'"
    assert "floatVal" in params, "Missing parameter 'floatVal'"

def test_arduinodsl::numberliteral_has_intVal():
    assert hasattr(arduinoDSL::NumberLiteral, "intVal")
    descriptor = None
    for klass in arduinoDSL::NumberLiteral.__mro__:
        if "intVal" in klass.__dict__:
            descriptor = klass.__dict__["intVal"]
            break
    assert isinstance(descriptor, property)

def test_arduinodsl::numberliteral_has_floatVal():
    assert hasattr(arduinoDSL::NumberLiteral, "floatVal")
    descriptor = None
    for klass in arduinoDSL::NumberLiteral.__mro__:
        if "floatVal" in klass.__dict__:
            descriptor = klass.__dict__["floatVal"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::delta_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Delta)


def test_arduinodsl::delta_constructor_exists():
    assert callable(arduinoDSL::Delta.__init__)


def test_arduinodsl::delta_constructor_args():
    sig = inspect.signature(arduinoDSL::Delta.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::variablereference_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::VariableReference)


def test_arduinodsl::variablereference_constructor_exists():
    assert callable(arduinoDSL::VariableReference.__init__)


def test_arduinodsl::variablereference_constructor_args():
    sig = inspect.signature(arduinoDSL::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::attribute_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Attribute)


def test_arduinodsl::attribute_constructor_exists():
    assert callable(arduinoDSL::Attribute.__init__)


def test_arduinodsl::attribute_constructor_args():
    sig = inspect.signature(arduinoDSL::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_numberexpression_is_not_abstract():
    assert not inspect.isabstract(NumberExpression)


def test_numberexpression_constructor_exists():
    assert callable(NumberExpression.__init__)


def test_numberexpression_constructor_args():
    sig = inspect.signature(NumberExpression.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::mod_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Mod)


def test_arduinodsl::mod_constructor_exists():
    assert callable(arduinoDSL::Mod.__init__)


def test_arduinodsl::mod_constructor_args():
    sig = inspect.signature(arduinoDSL::Mod.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::plus_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Plus)


def test_arduinodsl::plus_constructor_exists():
    assert callable(arduinoDSL::Plus.__init__)


def test_arduinodsl::plus_constructor_args():
    sig = inspect.signature(arduinoDSL::Plus.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::minus_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Minus)


def test_arduinodsl::minus_constructor_exists():
    assert callable(arduinoDSL::Minus.__init__)


def test_arduinodsl::minus_constructor_args():
    sig = inspect.signature(arduinoDSL::Minus.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::mult_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Mult)


def test_arduinodsl::mult_constructor_exists():
    assert callable(arduinoDSL::Mult.__init__)


def test_arduinodsl::mult_constructor_args():
    sig = inspect.signature(arduinoDSL::Mult.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::div_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Div)


def test_arduinodsl::div_constructor_exists():
    assert callable(arduinoDSL::Div.__init__)


def test_arduinodsl::div_constructor_args():
    sig = inspect.signature(arduinoDSL::Div.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::value_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Value)


def test_arduinodsl::value_constructor_exists():
    assert callable(arduinoDSL::Value.__init__)


def test_arduinodsl::value_constructor_args():
    sig = inspect.signature(arduinoDSL::Value.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::numberexpressionblock_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::NumberExpressionBlock)


def test_arduinodsl::numberexpressionblock_constructor_exists():
    assert callable(arduinoDSL::NumberExpressionBlock.__init__)


def test_arduinodsl::numberexpressionblock_constructor_args():
    sig = inspect.signature(arduinoDSL::NumberExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::compareoperator_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::CompareOperator)


def test_arduinodsl::compareoperator_constructor_exists():
    assert callable(arduinoDSL::CompareOperator.__init__)


def test_arduinodsl::compareoperator_constructor_args():
    sig = inspect.signature(arduinoDSL::CompareOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::booleanoperator_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::BooleanOperator)


def test_arduinodsl::booleanoperator_constructor_exists():
    assert callable(arduinoDSL::BooleanOperator.__init__)


def test_arduinodsl::booleanoperator_constructor_args():
    sig = inspect.signature(arduinoDSL::BooleanOperator.__init__)
    params = list(sig.parameters.keys())



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::comparison_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Comparison)


def test_arduinodsl::comparison_constructor_exists():
    assert callable(arduinoDSL::Comparison.__init__)


def test_arduinodsl::comparison_constructor_args():
    sig = inspect.signature(arduinoDSL::Comparison.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::andor_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::AndOr)


def test_arduinodsl::andor_constructor_exists():
    assert callable(arduinoDSL::AndOr.__init__)


def test_arduinodsl::andor_constructor_args():
    sig = inspect.signature(arduinoDSL::AndOr.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::booleanexpressionblock_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::BooleanExpressionBlock)


def test_arduinodsl::booleanexpressionblock_constructor_exists():
    assert callable(arduinoDSL::BooleanExpressionBlock.__init__)


def test_arduinodsl::booleanexpressionblock_constructor_args():
    sig = inspect.signature(arduinoDSL::BooleanExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::numberexpression_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::NumberExpression)


def test_arduinodsl::numberexpression_constructor_exists():
    assert callable(arduinoDSL::NumberExpression.__init__)


def test_arduinodsl::numberexpression_constructor_args():
    sig = inspect.signature(arduinoDSL::NumberExpression.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::rulebody_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::RuleBody)


def test_arduinodsl::rulebody_constructor_exists():
    assert callable(arduinoDSL::RuleBody.__init__)


def test_arduinodsl::rulebody_constructor_args():
    sig = inspect.signature(arduinoDSL::RuleBody.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::BooleanExpression)


def test_arduinodsl::booleanexpression_constructor_exists():
    assert callable(arduinoDSL::BooleanExpression.__init__)


def test_arduinodsl::booleanexpression_constructor_args():
    sig = inspect.signature(arduinoDSL::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::rule_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Rule)


def test_arduinodsl::rule_constructor_exists():
    assert callable(arduinoDSL::Rule.__init__)


def test_arduinodsl::rule_constructor_args():
    sig = inspect.signature(arduinoDSL::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_arduinodsl::rule_has_type():
    assert hasattr(arduinoDSL::Rule, "type")
    descriptor = None
    for klass in arduinoDSL::Rule.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_arduinodsl::eobject_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::EObject)


def test_arduinodsl::eobject_constructor_exists():
    assert callable(arduinoDSL::EObject.__init__)


def test_arduinodsl::eobject_constructor_args():
    sig = inspect.signature(arduinoDSL::EObject.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::program_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::Program)


def test_arduinodsl::program_constructor_exists():
    assert callable(arduinoDSL::Program.__init__)


def test_arduinodsl::program_constructor_args():
    sig = inspect.signature(arduinoDSL::Program.__init__)
    params = list(sig.parameters.keys())



def test_variablereference_is_not_abstract():
    assert not inspect.isabstract(VariableReference)


def test_variablereference_constructor_exists():
    assert callable(VariableReference.__init__)


def test_variablereference_constructor_args():
    sig = inspect.signature(VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::varref_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::VarRef)


def test_arduinodsl::varref_constructor_exists():
    assert callable(arduinoDSL::VarRef.__init__)


def test_arduinodsl::varref_constructor_args():
    sig = inspect.signature(arduinoDSL::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::elsestatement_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::ElseStatement)


def test_arduinodsl::elsestatement_constructor_exists():
    assert callable(arduinoDSL::ElseStatement.__init__)


def test_arduinodsl::elsestatement_constructor_args():
    sig = inspect.signature(arduinoDSL::ElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::elseifstatement_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::ElseIfStatement)


def test_arduinodsl::elseifstatement_constructor_exists():
    assert callable(arduinoDSL::ElseIfStatement.__init__)


def test_arduinodsl::elseifstatement_constructor_args():
    sig = inspect.signature(arduinoDSL::ElseIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_arduinodsl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(arduinoDSL::IfStatement)


def test_arduinodsl::ifstatement_constructor_exists():
    assert callable(arduinoDSL::IfStatement.__init__)


def test_arduinodsl::ifstatement_constructor_args():
    sig = inspect.signature(arduinoDSL::IfStatement.__init__)
    params = list(sig.parameters.keys())


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
CompareOperator_strategy = st.builds(
    CompareOperator,
)
arduinoDSL::Greater_strategy = st.builds(
    arduinoDSL::Greater,
)
arduinoDSL::NotEquals_strategy = st.builds(
    arduinoDSL::NotEquals,
)
arduinoDSL::SmallerThanEquals_strategy = st.builds(
    arduinoDSL::SmallerThanEquals,
)
arduinoDSL::Smaller_strategy = st.builds(
    arduinoDSL::Smaller,
)
arduinoDSL::GreaterThanEquals_strategy = st.builds(
    arduinoDSL::GreaterThanEquals,
)
arduinoDSL::Equals_strategy = st.builds(
    arduinoDSL::Equals,
)
BooleanOperator_strategy = st.builds(
    BooleanOperator,
)
arduinoDSL::Or_strategy = st.builds(
    arduinoDSL::Or,
)
arduinoDSL::And_strategy = st.builds(
    arduinoDSL::And,
)
arduinoDSL::Range_strategy = st.builds(
    arduinoDSL::Range,
    low=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    high=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
arduinoDSL::Smoothing_strategy = st.builds(
    arduinoDSL::Smoothing,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
arduinoDSL::Map_strategy = st.builds(
    arduinoDSL::Map,
)
arduinoDSL::Rate_strategy = st.builds(
    arduinoDSL::Rate,
    value=
        st.integers()
)
arduinoDSL::ComponentBody_strategy = st.builds(
    arduinoDSL::ComponentBody,
    io=
        safe_text,
    type=
        safe_text,
    pin=
        st.integers()
)
arduinoDSL::Board_strategy = st.builds(
    arduinoDSL::Board,
    b=
        safe_text
)
arduinoDSL::NodeDefinition_strategy = st.builds(
    arduinoDSL::NodeDefinition,
)
arduinoDSL::Cast_strategy = st.builds(
    arduinoDSL::Cast,
    castType=
        safe_text
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
arduinoDSL::VariableDeclaration_strategy = st.builds(
    arduinoDSL::VariableDeclaration,
    type=
        safe_text,
    name=
        safe_text
)
arduinoDSL::Assignment_strategy = st.builds(
    arduinoDSL::Assignment,
)
arduinoDSL::SimpleStatement_strategy = st.builds(
    arduinoDSL::SimpleStatement,
)
arduinoDSL::State_strategy = st.builds(
    arduinoDSL::State,
    value=
        safe_text
)
arduinoDSL::BooleanLiteral_strategy = st.builds(
    arduinoDSL::BooleanLiteral,
    value=
        st.booleans()
)
arduinoDSL::Component_strategy = st.builds(
    arduinoDSL::Component,
    name=
        safe_text
)
arduinoDSL::Node_strategy = st.builds(
    arduinoDSL::Node,
    name=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
arduinoDSL::NumberLiteral_strategy = st.builds(
    arduinoDSL::NumberLiteral,
    intVal=
        st.integers(),
    floatVal=
        safe_text
)
arduinoDSL::Delta_strategy = st.builds(
    arduinoDSL::Delta,
)
arduinoDSL::VariableReference_strategy = st.builds(
    arduinoDSL::VariableReference,
)
arduinoDSL::Attribute_strategy = st.builds(
    arduinoDSL::Attribute,
)
NumberExpression_strategy = st.builds(
    NumberExpression,
)
arduinoDSL::Mod_strategy = st.builds(
    arduinoDSL::Mod,
)
arduinoDSL::Plus_strategy = st.builds(
    arduinoDSL::Plus,
)
arduinoDSL::Minus_strategy = st.builds(
    arduinoDSL::Minus,
)
arduinoDSL::Mult_strategy = st.builds(
    arduinoDSL::Mult,
)
arduinoDSL::Div_strategy = st.builds(
    arduinoDSL::Div,
)
arduinoDSL::Value_strategy = st.builds(
    arduinoDSL::Value,
)
arduinoDSL::NumberExpressionBlock_strategy = st.builds(
    arduinoDSL::NumberExpressionBlock,
)
arduinoDSL::CompareOperator_strategy = st.builds(
    arduinoDSL::CompareOperator,
)
arduinoDSL::BooleanOperator_strategy = st.builds(
    arduinoDSL::BooleanOperator,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
arduinoDSL::Comparison_strategy = st.builds(
    arduinoDSL::Comparison,
)
arduinoDSL::AndOr_strategy = st.builds(
    arduinoDSL::AndOr,
)
arduinoDSL::BooleanExpressionBlock_strategy = st.builds(
    arduinoDSL::BooleanExpressionBlock,
)
arduinoDSL::NumberExpression_strategy = st.builds(
    arduinoDSL::NumberExpression,
)
arduinoDSL::RuleBody_strategy = st.builds(
    arduinoDSL::RuleBody,
)
arduinoDSL::BooleanExpression_strategy = st.builds(
    arduinoDSL::BooleanExpression,
)
arduinoDSL::Rule_strategy = st.builds(
    arduinoDSL::Rule,
    type=
        safe_text
)
arduinoDSL::EObject_strategy = st.builds(
    arduinoDSL::EObject,
)
arduinoDSL::Program_strategy = st.builds(
    arduinoDSL::Program,
)
VariableReference_strategy = st.builds(
    VariableReference,
)
arduinoDSL::VarRef_strategy = st.builds(
    arduinoDSL::VarRef,
)
arduinoDSL::ElseStatement_strategy = st.builds(
    arduinoDSL::ElseStatement,
)
arduinoDSL::ElseIfStatement_strategy = st.builds(
    arduinoDSL::ElseIfStatement,
)
arduinoDSL::IfStatement_strategy = st.builds(
    arduinoDSL::IfStatement,
)

@given(instance=CompareOperator_strategy)
@settings(max_examples=50)
def test_compareoperator_instantiation(instance):
    assert isinstance(instance, CompareOperator)

@given(instance=arduinoDSL::Greater_strategy)
@settings(max_examples=50)
def test_arduinodsl::greater_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Greater)

@given(instance=arduinoDSL::NotEquals_strategy)
@settings(max_examples=50)
def test_arduinodsl::notequals_instantiation(instance):
    assert isinstance(instance, arduinoDSL::NotEquals)

@given(instance=arduinoDSL::SmallerThanEquals_strategy)
@settings(max_examples=50)
def test_arduinodsl::smallerthanequals_instantiation(instance):
    assert isinstance(instance, arduinoDSL::SmallerThanEquals)

@given(instance=arduinoDSL::Smaller_strategy)
@settings(max_examples=50)
def test_arduinodsl::smaller_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Smaller)

@given(instance=arduinoDSL::GreaterThanEquals_strategy)
@settings(max_examples=50)
def test_arduinodsl::greaterthanequals_instantiation(instance):
    assert isinstance(instance, arduinoDSL::GreaterThanEquals)

@given(instance=arduinoDSL::Equals_strategy)
@settings(max_examples=50)
def test_arduinodsl::equals_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Equals)

@given(instance=BooleanOperator_strategy)
@settings(max_examples=50)
def test_booleanoperator_instantiation(instance):
    assert isinstance(instance, BooleanOperator)

@given(instance=arduinoDSL::Or_strategy)
@settings(max_examples=50)
def test_arduinodsl::or_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Or)

@given(instance=arduinoDSL::And_strategy)
@settings(max_examples=50)
def test_arduinodsl::and_instantiation(instance):
    assert isinstance(instance, arduinoDSL::And)

@given(instance=arduinoDSL::Range_strategy)
@settings(max_examples=50)
def test_arduinodsl::range_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Range)

@given(instance=arduinoDSL::Range_strategy)
def test_arduinodsl::range_low_type(instance):
    assert isinstance(instance.low, float)


@given(instance=arduinoDSL::Range_strategy)
def test_arduinodsl::range_low_setter(instance):
    original = instance.low
    instance.low = original
    assert instance.low == original

@given(instance=arduinoDSL::Range_strategy)
def test_arduinodsl::range_high_type(instance):
    assert isinstance(instance.high, float)


@given(instance=arduinoDSL::Range_strategy)
def test_arduinodsl::range_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original

@given(instance=arduinoDSL::Smoothing_strategy)
@settings(max_examples=50)
def test_arduinodsl::smoothing_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Smoothing)

@given(instance=arduinoDSL::Smoothing_strategy)
def test_arduinodsl::smoothing_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=arduinoDSL::Smoothing_strategy)
def test_arduinodsl::smoothing_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoDSL::Map_strategy)
@settings(max_examples=50)
def test_arduinodsl::map_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Map)

@given(instance=arduinoDSL::Rate_strategy)
@settings(max_examples=50)
def test_arduinodsl::rate_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Rate)

@given(instance=arduinoDSL::Rate_strategy)
def test_arduinodsl::rate_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduinoDSL::Rate_strategy)
def test_arduinodsl::rate_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoDSL::ComponentBody_strategy)
@settings(max_examples=50)
def test_arduinodsl::componentbody_instantiation(instance):
    assert isinstance(instance, arduinoDSL::ComponentBody)

@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_io_type(instance):
    assert isinstance(instance.io, str)


@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_io_setter(instance):
    original = instance.io
    instance.io = original
    assert instance.io == original

@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_pin_type(instance):
    assert isinstance(instance.pin, int)


@given(instance=arduinoDSL::ComponentBody_strategy)
def test_arduinodsl::componentbody_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduinoDSL::Board_strategy)
@settings(max_examples=50)
def test_arduinodsl::board_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Board)

@given(instance=arduinoDSL::Board_strategy)
def test_arduinodsl::board_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=arduinoDSL::Board_strategy)
def test_arduinodsl::board_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=arduinoDSL::NodeDefinition_strategy)
@settings(max_examples=50)
def test_arduinodsl::nodedefinition_instantiation(instance):
    assert isinstance(instance, arduinoDSL::NodeDefinition)

@given(instance=arduinoDSL::Cast_strategy)
@settings(max_examples=50)
def test_arduinodsl::cast_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Cast)

@given(instance=arduinoDSL::Cast_strategy)
def test_arduinodsl::cast_castType_type(instance):
    assert isinstance(instance.castType, str)


@given(instance=arduinoDSL::Cast_strategy)
def test_arduinodsl::cast_castType_setter(instance):
    original = instance.castType
    instance.castType = original
    assert instance.castType == original

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=arduinoDSL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_arduinodsl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, arduinoDSL::VariableDeclaration)

@given(instance=arduinoDSL::VariableDeclaration_strategy)
def test_arduinodsl::variabledeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduinoDSL::VariableDeclaration_strategy)
def test_arduinodsl::variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduinoDSL::VariableDeclaration_strategy)
def test_arduinodsl::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoDSL::VariableDeclaration_strategy)
def test_arduinodsl::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoDSL::Assignment_strategy)
@settings(max_examples=50)
def test_arduinodsl::assignment_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Assignment)

@given(instance=arduinoDSL::SimpleStatement_strategy)
@settings(max_examples=50)
def test_arduinodsl::simplestatement_instantiation(instance):
    assert isinstance(instance, arduinoDSL::SimpleStatement)

@given(instance=arduinoDSL::State_strategy)
@settings(max_examples=50)
def test_arduinodsl::state_instantiation(instance):
    assert isinstance(instance, arduinoDSL::State)

@given(instance=arduinoDSL::State_strategy)
def test_arduinodsl::state_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduinoDSL::State_strategy)
def test_arduinodsl::state_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoDSL::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_arduinodsl::booleanliteral_instantiation(instance):
    assert isinstance(instance, arduinoDSL::BooleanLiteral)

@given(instance=arduinoDSL::BooleanLiteral_strategy)
def test_arduinodsl::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=arduinoDSL::BooleanLiteral_strategy)
def test_arduinodsl::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduinoDSL::Component_strategy)
@settings(max_examples=50)
def test_arduinodsl::component_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Component)

@given(instance=arduinoDSL::Component_strategy)
def test_arduinodsl::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoDSL::Component_strategy)
def test_arduinodsl::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduinoDSL::Node_strategy)
@settings(max_examples=50)
def test_arduinodsl::node_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Node)

@given(instance=arduinoDSL::Node_strategy)
def test_arduinodsl::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduinoDSL::Node_strategy)
def test_arduinodsl::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=arduinoDSL::NumberLiteral_strategy)
@settings(max_examples=50)
def test_arduinodsl::numberliteral_instantiation(instance):
    assert isinstance(instance, arduinoDSL::NumberLiteral)

@given(instance=arduinoDSL::NumberLiteral_strategy)
def test_arduinodsl::numberliteral_intVal_type(instance):
    assert isinstance(instance.intVal, int)


@given(instance=arduinoDSL::NumberLiteral_strategy)
def test_arduinodsl::numberliteral_intVal_setter(instance):
    original = instance.intVal
    instance.intVal = original
    assert instance.intVal == original

@given(instance=arduinoDSL::NumberLiteral_strategy)
def test_arduinodsl::numberliteral_floatVal_type(instance):
    assert isinstance(instance.floatVal, str)


@given(instance=arduinoDSL::NumberLiteral_strategy)
def test_arduinodsl::numberliteral_floatVal_setter(instance):
    original = instance.floatVal
    instance.floatVal = original
    assert instance.floatVal == original

@given(instance=arduinoDSL::Delta_strategy)
@settings(max_examples=50)
def test_arduinodsl::delta_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Delta)

@given(instance=arduinoDSL::VariableReference_strategy)
@settings(max_examples=50)
def test_arduinodsl::variablereference_instantiation(instance):
    assert isinstance(instance, arduinoDSL::VariableReference)

@given(instance=arduinoDSL::Attribute_strategy)
@settings(max_examples=50)
def test_arduinodsl::attribute_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Attribute)

@given(instance=NumberExpression_strategy)
@settings(max_examples=50)
def test_numberexpression_instantiation(instance):
    assert isinstance(instance, NumberExpression)

@given(instance=arduinoDSL::Mod_strategy)
@settings(max_examples=50)
def test_arduinodsl::mod_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Mod)

@given(instance=arduinoDSL::Plus_strategy)
@settings(max_examples=50)
def test_arduinodsl::plus_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Plus)

@given(instance=arduinoDSL::Minus_strategy)
@settings(max_examples=50)
def test_arduinodsl::minus_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Minus)

@given(instance=arduinoDSL::Mult_strategy)
@settings(max_examples=50)
def test_arduinodsl::mult_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Mult)

@given(instance=arduinoDSL::Div_strategy)
@settings(max_examples=50)
def test_arduinodsl::div_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Div)

@given(instance=arduinoDSL::Value_strategy)
@settings(max_examples=50)
def test_arduinodsl::value_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Value)

@given(instance=arduinoDSL::NumberExpressionBlock_strategy)
@settings(max_examples=50)
def test_arduinodsl::numberexpressionblock_instantiation(instance):
    assert isinstance(instance, arduinoDSL::NumberExpressionBlock)

@given(instance=arduinoDSL::CompareOperator_strategy)
@settings(max_examples=50)
def test_arduinodsl::compareoperator_instantiation(instance):
    assert isinstance(instance, arduinoDSL::CompareOperator)

@given(instance=arduinoDSL::BooleanOperator_strategy)
@settings(max_examples=50)
def test_arduinodsl::booleanoperator_instantiation(instance):
    assert isinstance(instance, arduinoDSL::BooleanOperator)

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=arduinoDSL::Comparison_strategy)
@settings(max_examples=50)
def test_arduinodsl::comparison_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Comparison)

@given(instance=arduinoDSL::AndOr_strategy)
@settings(max_examples=50)
def test_arduinodsl::andor_instantiation(instance):
    assert isinstance(instance, arduinoDSL::AndOr)

@given(instance=arduinoDSL::BooleanExpressionBlock_strategy)
@settings(max_examples=50)
def test_arduinodsl::booleanexpressionblock_instantiation(instance):
    assert isinstance(instance, arduinoDSL::BooleanExpressionBlock)

@given(instance=arduinoDSL::NumberExpression_strategy)
@settings(max_examples=50)
def test_arduinodsl::numberexpression_instantiation(instance):
    assert isinstance(instance, arduinoDSL::NumberExpression)

@given(instance=arduinoDSL::RuleBody_strategy)
@settings(max_examples=50)
def test_arduinodsl::rulebody_instantiation(instance):
    assert isinstance(instance, arduinoDSL::RuleBody)

@given(instance=arduinoDSL::BooleanExpression_strategy)
@settings(max_examples=50)
def test_arduinodsl::booleanexpression_instantiation(instance):
    assert isinstance(instance, arduinoDSL::BooleanExpression)

@given(instance=arduinoDSL::Rule_strategy)
@settings(max_examples=50)
def test_arduinodsl::rule_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Rule)

@given(instance=arduinoDSL::Rule_strategy)
def test_arduinodsl::rule_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduinoDSL::Rule_strategy)
def test_arduinodsl::rule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduinoDSL::EObject_strategy)
@settings(max_examples=50)
def test_arduinodsl::eobject_instantiation(instance):
    assert isinstance(instance, arduinoDSL::EObject)

@given(instance=arduinoDSL::Program_strategy)
@settings(max_examples=50)
def test_arduinodsl::program_instantiation(instance):
    assert isinstance(instance, arduinoDSL::Program)

@given(instance=VariableReference_strategy)
@settings(max_examples=50)
def test_variablereference_instantiation(instance):
    assert isinstance(instance, VariableReference)

@given(instance=arduinoDSL::VarRef_strategy)
@settings(max_examples=50)
def test_arduinodsl::varref_instantiation(instance):
    assert isinstance(instance, arduinoDSL::VarRef)

@given(instance=arduinoDSL::ElseStatement_strategy)
@settings(max_examples=50)
def test_arduinodsl::elsestatement_instantiation(instance):
    assert isinstance(instance, arduinoDSL::ElseStatement)

@given(instance=arduinoDSL::ElseIfStatement_strategy)
@settings(max_examples=50)
def test_arduinodsl::elseifstatement_instantiation(instance):
    assert isinstance(instance, arduinoDSL::ElseIfStatement)

@given(instance=arduinoDSL::IfStatement_strategy)
@settings(max_examples=50)
def test_arduinodsl::ifstatement_instantiation(instance):
    assert isinstance(instance, arduinoDSL::IfStatement)

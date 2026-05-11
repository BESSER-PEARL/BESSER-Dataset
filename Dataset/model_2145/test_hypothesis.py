import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expr,
    graph::BoolConstant,
    graph::VariableRef,
    graph::StringConstant,
    graph::ParticleConstant,
    graph::And,
    graph::GraphConstant,
    graph::Or,
    graph::IntConstant,
    graph::Not,
    graph::MulOrDiv,
    graph::PlusOrMin,
    graph::Comparison,
    graph::PathExistence,
    graph::Statement,
    graph::Declaration,
    graph::Program,
    graph::Edge,
    graph::Vertex,
    graph::Expr,
    Statement,
    graph::WhileStmt,
    graph::PrintStmt,
    graph::IfStmt,
    graph::MoveStmt,
    graph::AssignStmt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_graph::boolconstant_is_not_abstract():
    assert not inspect.isabstract(graph::BoolConstant)


def test_graph::boolconstant_constructor_exists():
    assert callable(graph::BoolConstant.__init__)


def test_graph::boolconstant_constructor_args():
    sig = inspect.signature(graph::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph::boolconstant_has_value():
    assert hasattr(graph::BoolConstant, "value")
    descriptor = None
    for klass in graph::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph::variableref_is_not_abstract():
    assert not inspect.isabstract(graph::VariableRef)


def test_graph::variableref_constructor_exists():
    assert callable(graph::VariableRef.__init__)


def test_graph::variableref_constructor_args():
    sig = inspect.signature(graph::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_graph::stringconstant_is_not_abstract():
    assert not inspect.isabstract(graph::StringConstant)


def test_graph::stringconstant_constructor_exists():
    assert callable(graph::StringConstant.__init__)


def test_graph::stringconstant_constructor_args():
    sig = inspect.signature(graph::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph::stringconstant_has_value():
    assert hasattr(graph::StringConstant, "value")
    descriptor = None
    for klass in graph::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph::particleconstant_is_not_abstract():
    assert not inspect.isabstract(graph::ParticleConstant)


def test_graph::particleconstant_constructor_exists():
    assert callable(graph::ParticleConstant.__init__)


def test_graph::particleconstant_constructor_args():
    sig = inspect.signature(graph::ParticleConstant.__init__)
    params = list(sig.parameters.keys())



def test_graph::and_is_not_abstract():
    assert not inspect.isabstract(graph::And)


def test_graph::and_constructor_exists():
    assert callable(graph::And.__init__)


def test_graph::and_constructor_args():
    sig = inspect.signature(graph::And.__init__)
    params = list(sig.parameters.keys())



def test_graph::graphconstant_is_not_abstract():
    assert not inspect.isabstract(graph::GraphConstant)


def test_graph::graphconstant_constructor_exists():
    assert callable(graph::GraphConstant.__init__)


def test_graph::graphconstant_constructor_args():
    sig = inspect.signature(graph::GraphConstant.__init__)
    params = list(sig.parameters.keys())



def test_graph::or_is_not_abstract():
    assert not inspect.isabstract(graph::Or)


def test_graph::or_constructor_exists():
    assert callable(graph::Or.__init__)


def test_graph::or_constructor_args():
    sig = inspect.signature(graph::Or.__init__)
    params = list(sig.parameters.keys())



def test_graph::intconstant_is_not_abstract():
    assert not inspect.isabstract(graph::IntConstant)


def test_graph::intconstant_constructor_exists():
    assert callable(graph::IntConstant.__init__)


def test_graph::intconstant_constructor_args():
    sig = inspect.signature(graph::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph::intconstant_has_value():
    assert hasattr(graph::IntConstant, "value")
    descriptor = None
    for klass in graph::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph::not_is_not_abstract():
    assert not inspect.isabstract(graph::Not)


def test_graph::not_constructor_exists():
    assert callable(graph::Not.__init__)


def test_graph::not_constructor_args():
    sig = inspect.signature(graph::Not.__init__)
    params = list(sig.parameters.keys())



def test_graph::mulordiv_is_not_abstract():
    assert not inspect.isabstract(graph::MulOrDiv)


def test_graph::mulordiv_constructor_exists():
    assert callable(graph::MulOrDiv.__init__)


def test_graph::mulordiv_constructor_args():
    sig = inspect.signature(graph::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph::mulordiv_has_op():
    assert hasattr(graph::MulOrDiv, "op")
    descriptor = None
    for klass in graph::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph::plusormin_is_not_abstract():
    assert not inspect.isabstract(graph::PlusOrMin)


def test_graph::plusormin_constructor_exists():
    assert callable(graph::PlusOrMin.__init__)


def test_graph::plusormin_constructor_args():
    sig = inspect.signature(graph::PlusOrMin.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph::plusormin_has_op():
    assert hasattr(graph::PlusOrMin, "op")
    descriptor = None
    for klass in graph::PlusOrMin.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph::comparison_is_not_abstract():
    assert not inspect.isabstract(graph::Comparison)


def test_graph::comparison_constructor_exists():
    assert callable(graph::Comparison.__init__)


def test_graph::comparison_constructor_args():
    sig = inspect.signature(graph::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph::comparison_has_op():
    assert hasattr(graph::Comparison, "op")
    descriptor = None
    for klass in graph::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph::pathexistence_is_not_abstract():
    assert not inspect.isabstract(graph::PathExistence)


def test_graph::pathexistence_constructor_exists():
    assert callable(graph::PathExistence.__init__)


def test_graph::pathexistence_constructor_args():
    sig = inspect.signature(graph::PathExistence.__init__)
    params = list(sig.parameters.keys())



def test_graph::statement_is_not_abstract():
    assert not inspect.isabstract(graph::Statement)


def test_graph::statement_constructor_exists():
    assert callable(graph::Statement.__init__)


def test_graph::statement_constructor_args():
    sig = inspect.signature(graph::Statement.__init__)
    params = list(sig.parameters.keys())



def test_graph::declaration_is_not_abstract():
    assert not inspect.isabstract(graph::Declaration)


def test_graph::declaration_constructor_exists():
    assert callable(graph::Declaration.__init__)


def test_graph::declaration_constructor_args():
    sig = inspect.signature(graph::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_graph::declaration_has_name():
    assert hasattr(graph::Declaration, "name")
    descriptor = None
    for klass in graph::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graph::declaration_has_type():
    assert hasattr(graph::Declaration, "type")
    descriptor = None
    for klass in graph::Declaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graph::program_is_not_abstract():
    assert not inspect.isabstract(graph::Program)


def test_graph::program_constructor_exists():
    assert callable(graph::Program.__init__)


def test_graph::program_constructor_args():
    sig = inspect.signature(graph::Program.__init__)
    params = list(sig.parameters.keys())



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph::vertex_is_not_abstract():
    assert not inspect.isabstract(graph::Vertex)


def test_graph::vertex_constructor_exists():
    assert callable(graph::Vertex.__init__)


def test_graph::vertex_constructor_args():
    sig = inspect.signature(graph::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::vertex_has_name():
    assert hasattr(graph::Vertex, "name")
    descriptor = None
    for klass in graph::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::expr_is_not_abstract():
    assert not inspect.isabstract(graph::Expr)


def test_graph::expr_constructor_exists():
    assert callable(graph::Expr.__init__)


def test_graph::expr_constructor_args():
    sig = inspect.signature(graph::Expr.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_graph::whilestmt_is_not_abstract():
    assert not inspect.isabstract(graph::WhileStmt)


def test_graph::whilestmt_constructor_exists():
    assert callable(graph::WhileStmt.__init__)


def test_graph::whilestmt_constructor_args():
    sig = inspect.signature(graph::WhileStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph::printstmt_is_not_abstract():
    assert not inspect.isabstract(graph::PrintStmt)


def test_graph::printstmt_constructor_exists():
    assert callable(graph::PrintStmt.__init__)


def test_graph::printstmt_constructor_args():
    sig = inspect.signature(graph::PrintStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph::ifstmt_is_not_abstract():
    assert not inspect.isabstract(graph::IfStmt)


def test_graph::ifstmt_constructor_exists():
    assert callable(graph::IfStmt.__init__)


def test_graph::ifstmt_constructor_args():
    sig = inspect.signature(graph::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph::movestmt_is_not_abstract():
    assert not inspect.isabstract(graph::MoveStmt)


def test_graph::movestmt_constructor_exists():
    assert callable(graph::MoveStmt.__init__)


def test_graph::movestmt_constructor_args():
    sig = inspect.signature(graph::MoveStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph::assignstmt_is_not_abstract():
    assert not inspect.isabstract(graph::AssignStmt)


def test_graph::assignstmt_constructor_exists():
    assert callable(graph::AssignStmt.__init__)


def test_graph::assignstmt_constructor_args():
    sig = inspect.signature(graph::AssignStmt.__init__)
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
Expr_strategy = st.builds(
    Expr,
)
graph::BoolConstant_strategy = st.builds(
    graph::BoolConstant,
    value=
        safe_text
)
graph::VariableRef_strategy = st.builds(
    graph::VariableRef,
)
graph::StringConstant_strategy = st.builds(
    graph::StringConstant,
    value=
        safe_text
)
graph::ParticleConstant_strategy = st.builds(
    graph::ParticleConstant,
)
graph::And_strategy = st.builds(
    graph::And,
)
graph::GraphConstant_strategy = st.builds(
    graph::GraphConstant,
)
graph::Or_strategy = st.builds(
    graph::Or,
)
graph::IntConstant_strategy = st.builds(
    graph::IntConstant,
    value=
        st.integers()
)
graph::Not_strategy = st.builds(
    graph::Not,
)
graph::MulOrDiv_strategy = st.builds(
    graph::MulOrDiv,
    op=
        safe_text
)
graph::PlusOrMin_strategy = st.builds(
    graph::PlusOrMin,
    op=
        safe_text
)
graph::Comparison_strategy = st.builds(
    graph::Comparison,
    op=
        safe_text
)
graph::PathExistence_strategy = st.builds(
    graph::PathExistence,
)
graph::Statement_strategy = st.builds(
    graph::Statement,
)
graph::Declaration_strategy = st.builds(
    graph::Declaration,
    name=
        safe_text,
    type=
        safe_text
)
graph::Program_strategy = st.builds(
    graph::Program,
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
graph::Vertex_strategy = st.builds(
    graph::Vertex,
    name=
        safe_text
)
graph::Expr_strategy = st.builds(
    graph::Expr,
)
Statement_strategy = st.builds(
    Statement,
)
graph::WhileStmt_strategy = st.builds(
    graph::WhileStmt,
)
graph::PrintStmt_strategy = st.builds(
    graph::PrintStmt,
)
graph::IfStmt_strategy = st.builds(
    graph::IfStmt,
)
graph::MoveStmt_strategy = st.builds(
    graph::MoveStmt,
)
graph::AssignStmt_strategy = st.builds(
    graph::AssignStmt,
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=graph::BoolConstant_strategy)
@settings(max_examples=50)
def test_graph::boolconstant_instantiation(instance):
    assert isinstance(instance, graph::BoolConstant)

@given(instance=graph::BoolConstant_strategy)
def test_graph::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graph::BoolConstant_strategy)
def test_graph::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph::VariableRef_strategy)
@settings(max_examples=50)
def test_graph::variableref_instantiation(instance):
    assert isinstance(instance, graph::VariableRef)

@given(instance=graph::StringConstant_strategy)
@settings(max_examples=50)
def test_graph::stringconstant_instantiation(instance):
    assert isinstance(instance, graph::StringConstant)

@given(instance=graph::StringConstant_strategy)
def test_graph::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=graph::StringConstant_strategy)
def test_graph::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph::ParticleConstant_strategy)
@settings(max_examples=50)
def test_graph::particleconstant_instantiation(instance):
    assert isinstance(instance, graph::ParticleConstant)

@given(instance=graph::And_strategy)
@settings(max_examples=50)
def test_graph::and_instantiation(instance):
    assert isinstance(instance, graph::And)

@given(instance=graph::GraphConstant_strategy)
@settings(max_examples=50)
def test_graph::graphconstant_instantiation(instance):
    assert isinstance(instance, graph::GraphConstant)

@given(instance=graph::Or_strategy)
@settings(max_examples=50)
def test_graph::or_instantiation(instance):
    assert isinstance(instance, graph::Or)

@given(instance=graph::IntConstant_strategy)
@settings(max_examples=50)
def test_graph::intconstant_instantiation(instance):
    assert isinstance(instance, graph::IntConstant)

@given(instance=graph::IntConstant_strategy)
def test_graph::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=graph::IntConstant_strategy)
def test_graph::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph::Not_strategy)
@settings(max_examples=50)
def test_graph::not_instantiation(instance):
    assert isinstance(instance, graph::Not)

@given(instance=graph::MulOrDiv_strategy)
@settings(max_examples=50)
def test_graph::mulordiv_instantiation(instance):
    assert isinstance(instance, graph::MulOrDiv)

@given(instance=graph::MulOrDiv_strategy)
def test_graph::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=graph::MulOrDiv_strategy)
def test_graph::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph::PlusOrMin_strategy)
@settings(max_examples=50)
def test_graph::plusormin_instantiation(instance):
    assert isinstance(instance, graph::PlusOrMin)

@given(instance=graph::PlusOrMin_strategy)
def test_graph::plusormin_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=graph::PlusOrMin_strategy)
def test_graph::plusormin_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph::Comparison_strategy)
@settings(max_examples=50)
def test_graph::comparison_instantiation(instance):
    assert isinstance(instance, graph::Comparison)

@given(instance=graph::Comparison_strategy)
def test_graph::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=graph::Comparison_strategy)
def test_graph::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph::PathExistence_strategy)
@settings(max_examples=50)
def test_graph::pathexistence_instantiation(instance):
    assert isinstance(instance, graph::PathExistence)

@given(instance=graph::Statement_strategy)
@settings(max_examples=50)
def test_graph::statement_instantiation(instance):
    assert isinstance(instance, graph::Statement)

@given(instance=graph::Declaration_strategy)
@settings(max_examples=50)
def test_graph::declaration_instantiation(instance):
    assert isinstance(instance, graph::Declaration)

@given(instance=graph::Declaration_strategy)
def test_graph::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Declaration_strategy)
def test_graph::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Declaration_strategy)
def test_graph::declaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graph::Declaration_strategy)
def test_graph::declaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graph::Program_strategy)
@settings(max_examples=50)
def test_graph::program_instantiation(instance):
    assert isinstance(instance, graph::Program)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Vertex_strategy)
@settings(max_examples=50)
def test_graph::vertex_instantiation(instance):
    assert isinstance(instance, graph::Vertex)

@given(instance=graph::Vertex_strategy)
def test_graph::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Vertex_strategy)
def test_graph::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Expr_strategy)
@settings(max_examples=50)
def test_graph::expr_instantiation(instance):
    assert isinstance(instance, graph::Expr)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=graph::WhileStmt_strategy)
@settings(max_examples=50)
def test_graph::whilestmt_instantiation(instance):
    assert isinstance(instance, graph::WhileStmt)

@given(instance=graph::PrintStmt_strategy)
@settings(max_examples=50)
def test_graph::printstmt_instantiation(instance):
    assert isinstance(instance, graph::PrintStmt)

@given(instance=graph::IfStmt_strategy)
@settings(max_examples=50)
def test_graph::ifstmt_instantiation(instance):
    assert isinstance(instance, graph::IfStmt)

@given(instance=graph::MoveStmt_strategy)
@settings(max_examples=50)
def test_graph::movestmt_instantiation(instance):
    assert isinstance(instance, graph::MoveStmt)

@given(instance=graph::AssignStmt_strategy)
@settings(max_examples=50)
def test_graph::assignstmt_instantiation(instance):
    assert isinstance(instance, graph::AssignStmt)

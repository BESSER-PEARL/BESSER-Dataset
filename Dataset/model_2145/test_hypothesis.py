import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expr,
    graph_GraphConstant,
    graph_BoolConstant,
    graph_StringConstant,
    graph_ParticleConstant,
    graph_And,
    graph_VariableRef,
    graph_Or,
    graph_IntConstant,
    graph_Not,
    graph_MulOrDiv,
    graph_PlusOrMin,
    graph_Comparison,
    graph_PathExistence,
    graph_Statement,
    graph_Declaration,
    graph_Program,
    graph_Edge,
    graph_Vertex,
    graph_Expr,
    Statement,
    graph_WhileStmt,
    graph_IfStmt,
    graph_MoveStmt,
    graph_PrintStmt,
    graph_AssignStmt,
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



def test_graph_graphconstant_is_not_abstract():
    assert not inspect.isabstract(graph_GraphConstant)


def test_graph_graphconstant_constructor_exists():
    assert callable(graph_GraphConstant.__init__)


def test_graph_graphconstant_constructor_args():
    sig = inspect.signature(graph_GraphConstant.__init__)
    params = list(sig.parameters.keys())



def test_graph_boolconstant_is_not_abstract():
    assert not inspect.isabstract(graph_BoolConstant)


def test_graph_boolconstant_constructor_exists():
    assert callable(graph_BoolConstant.__init__)


def test_graph_boolconstant_constructor_args():
    sig = inspect.signature(graph_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph_boolconstant_has_value():
    assert hasattr(graph_BoolConstant, "value")
    descriptor = None
    for klass in graph_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph_stringconstant_is_not_abstract():
    assert not inspect.isabstract(graph_StringConstant)


def test_graph_stringconstant_constructor_exists():
    assert callable(graph_StringConstant.__init__)


def test_graph_stringconstant_constructor_args():
    sig = inspect.signature(graph_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph_stringconstant_has_value():
    assert hasattr(graph_StringConstant, "value")
    descriptor = None
    for klass in graph_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph_particleconstant_is_not_abstract():
    assert not inspect.isabstract(graph_ParticleConstant)


def test_graph_particleconstant_constructor_exists():
    assert callable(graph_ParticleConstant.__init__)


def test_graph_particleconstant_constructor_args():
    sig = inspect.signature(graph_ParticleConstant.__init__)
    params = list(sig.parameters.keys())



def test_graph_and_is_not_abstract():
    assert not inspect.isabstract(graph_And)


def test_graph_and_constructor_exists():
    assert callable(graph_And.__init__)


def test_graph_and_constructor_args():
    sig = inspect.signature(graph_And.__init__)
    params = list(sig.parameters.keys())



def test_graph_variableref_is_not_abstract():
    assert not inspect.isabstract(graph_VariableRef)


def test_graph_variableref_constructor_exists():
    assert callable(graph_VariableRef.__init__)


def test_graph_variableref_constructor_args():
    sig = inspect.signature(graph_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_graph_or_is_not_abstract():
    assert not inspect.isabstract(graph_Or)


def test_graph_or_constructor_exists():
    assert callable(graph_Or.__init__)


def test_graph_or_constructor_args():
    sig = inspect.signature(graph_Or.__init__)
    params = list(sig.parameters.keys())



def test_graph_intconstant_is_not_abstract():
    assert not inspect.isabstract(graph_IntConstant)


def test_graph_intconstant_constructor_exists():
    assert callable(graph_IntConstant.__init__)


def test_graph_intconstant_constructor_args():
    sig = inspect.signature(graph_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph_intconstant_has_value():
    assert hasattr(graph_IntConstant, "value")
    descriptor = None
    for klass in graph_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph_not_is_not_abstract():
    assert not inspect.isabstract(graph_Not)


def test_graph_not_constructor_exists():
    assert callable(graph_Not.__init__)


def test_graph_not_constructor_args():
    sig = inspect.signature(graph_Not.__init__)
    params = list(sig.parameters.keys())



def test_graph_mulordiv_is_not_abstract():
    assert not inspect.isabstract(graph_MulOrDiv)


def test_graph_mulordiv_constructor_exists():
    assert callable(graph_MulOrDiv.__init__)


def test_graph_mulordiv_constructor_args():
    sig = inspect.signature(graph_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph_mulordiv_has_op():
    assert hasattr(graph_MulOrDiv, "op")
    descriptor = None
    for klass in graph_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph_plusormin_is_not_abstract():
    assert not inspect.isabstract(graph_PlusOrMin)


def test_graph_plusormin_constructor_exists():
    assert callable(graph_PlusOrMin.__init__)


def test_graph_plusormin_constructor_args():
    sig = inspect.signature(graph_PlusOrMin.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph_plusormin_has_op():
    assert hasattr(graph_PlusOrMin, "op")
    descriptor = None
    for klass in graph_PlusOrMin.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph_comparison_is_not_abstract():
    assert not inspect.isabstract(graph_Comparison)


def test_graph_comparison_constructor_exists():
    assert callable(graph_Comparison.__init__)


def test_graph_comparison_constructor_args():
    sig = inspect.signature(graph_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_graph_comparison_has_op():
    assert hasattr(graph_Comparison, "op")
    descriptor = None
    for klass in graph_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_graph_pathexistence_is_not_abstract():
    assert not inspect.isabstract(graph_PathExistence)


def test_graph_pathexistence_constructor_exists():
    assert callable(graph_PathExistence.__init__)


def test_graph_pathexistence_constructor_args():
    sig = inspect.signature(graph_PathExistence.__init__)
    params = list(sig.parameters.keys())



def test_graph_statement_is_not_abstract():
    assert not inspect.isabstract(graph_Statement)


def test_graph_statement_constructor_exists():
    assert callable(graph_Statement.__init__)


def test_graph_statement_constructor_args():
    sig = inspect.signature(graph_Statement.__init__)
    params = list(sig.parameters.keys())



def test_graph_declaration_is_not_abstract():
    assert not inspect.isabstract(graph_Declaration)


def test_graph_declaration_constructor_exists():
    assert callable(graph_Declaration.__init__)


def test_graph_declaration_constructor_args():
    sig = inspect.signature(graph_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_graph_declaration_has_type():
    assert hasattr(graph_Declaration, "type")
    descriptor = None
    for klass in graph_Declaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graph_declaration_has_name():
    assert hasattr(graph_Declaration, "name")
    descriptor = None
    for klass in graph_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_program_is_not_abstract():
    assert not inspect.isabstract(graph_Program)


def test_graph_program_constructor_exists():
    assert callable(graph_Program.__init__)


def test_graph_program_constructor_args():
    sig = inspect.signature(graph_Program.__init__)
    params = list(sig.parameters.keys())



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_vertex_has_name():
    assert hasattr(graph_Vertex, "name")
    descriptor = None
    for klass in graph_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_expr_is_not_abstract():
    assert not inspect.isabstract(graph_Expr)


def test_graph_expr_constructor_exists():
    assert callable(graph_Expr.__init__)


def test_graph_expr_constructor_args():
    sig = inspect.signature(graph_Expr.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_graph_whilestmt_is_not_abstract():
    assert not inspect.isabstract(graph_WhileStmt)


def test_graph_whilestmt_constructor_exists():
    assert callable(graph_WhileStmt.__init__)


def test_graph_whilestmt_constructor_args():
    sig = inspect.signature(graph_WhileStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph_ifstmt_is_not_abstract():
    assert not inspect.isabstract(graph_IfStmt)


def test_graph_ifstmt_constructor_exists():
    assert callable(graph_IfStmt.__init__)


def test_graph_ifstmt_constructor_args():
    sig = inspect.signature(graph_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph_movestmt_is_not_abstract():
    assert not inspect.isabstract(graph_MoveStmt)


def test_graph_movestmt_constructor_exists():
    assert callable(graph_MoveStmt.__init__)


def test_graph_movestmt_constructor_args():
    sig = inspect.signature(graph_MoveStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph_printstmt_is_not_abstract():
    assert not inspect.isabstract(graph_PrintStmt)


def test_graph_printstmt_constructor_exists():
    assert callable(graph_PrintStmt.__init__)


def test_graph_printstmt_constructor_args():
    sig = inspect.signature(graph_PrintStmt.__init__)
    params = list(sig.parameters.keys())



def test_graph_assignstmt_is_not_abstract():
    assert not inspect.isabstract(graph_AssignStmt)


def test_graph_assignstmt_constructor_exists():
    assert callable(graph_AssignStmt.__init__)


def test_graph_assignstmt_constructor_args():
    sig = inspect.signature(graph_AssignStmt.__init__)
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
graph_GraphConstant_strategy = st.builds(
    graph_GraphConstant,
)
graph_BoolConstant_strategy = st.builds(
    graph_BoolConstant,
    value=
        safe_text
)
graph_StringConstant_strategy = st.builds(
    graph_StringConstant,
    value=
        safe_text
)
graph_ParticleConstant_strategy = st.builds(
    graph_ParticleConstant,
)
graph_And_strategy = st.builds(
    graph_And,
)
graph_VariableRef_strategy = st.builds(
    graph_VariableRef,
)
graph_Or_strategy = st.builds(
    graph_Or,
)
graph_IntConstant_strategy = st.builds(
    graph_IntConstant,
    value=
        st.integers()
)
graph_Not_strategy = st.builds(
    graph_Not,
)
graph_MulOrDiv_strategy = st.builds(
    graph_MulOrDiv,
    op=
        safe_text
)
graph_PlusOrMin_strategy = st.builds(
    graph_PlusOrMin,
    op=
        safe_text
)
graph_Comparison_strategy = st.builds(
    graph_Comparison,
    op=
        safe_text
)
graph_PathExistence_strategy = st.builds(
    graph_PathExistence,
)
graph_Statement_strategy = st.builds(
    graph_Statement,
)
graph_Declaration_strategy = st.builds(
    graph_Declaration,
    type=
        safe_text,
    name=
        safe_text
)
graph_Program_strategy = st.builds(
    graph_Program,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Vertex_strategy = st.builds(
    graph_Vertex,
    name=
        safe_text
)
graph_Expr_strategy = st.builds(
    graph_Expr,
)
Statement_strategy = st.builds(
    Statement,
)
graph_WhileStmt_strategy = st.builds(
    graph_WhileStmt,
)
graph_IfStmt_strategy = st.builds(
    graph_IfStmt,
)
graph_MoveStmt_strategy = st.builds(
    graph_MoveStmt,
)
graph_PrintStmt_strategy = st.builds(
    graph_PrintStmt,
)
graph_AssignStmt_strategy = st.builds(
    graph_AssignStmt,
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=graph_GraphConstant_strategy)
@settings(max_examples=50)
def test_graph_graphconstant_instantiation(instance):
    assert isinstance(instance, graph_GraphConstant)

@given(instance=graph_BoolConstant_strategy)
@settings(max_examples=50)
def test_graph_boolconstant_instantiation(instance):
    assert isinstance(instance, graph_BoolConstant)



@given(instance=graph_BoolConstant_strategy)
def test_graph_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph_StringConstant_strategy)
@settings(max_examples=50)
def test_graph_stringconstant_instantiation(instance):
    assert isinstance(instance, graph_StringConstant)



@given(instance=graph_StringConstant_strategy)
def test_graph_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph_ParticleConstant_strategy)
@settings(max_examples=50)
def test_graph_particleconstant_instantiation(instance):
    assert isinstance(instance, graph_ParticleConstant)

@given(instance=graph_And_strategy)
@settings(max_examples=50)
def test_graph_and_instantiation(instance):
    assert isinstance(instance, graph_And)

@given(instance=graph_VariableRef_strategy)
@settings(max_examples=50)
def test_graph_variableref_instantiation(instance):
    assert isinstance(instance, graph_VariableRef)

@given(instance=graph_Or_strategy)
@settings(max_examples=50)
def test_graph_or_instantiation(instance):
    assert isinstance(instance, graph_Or)

@given(instance=graph_IntConstant_strategy)
@settings(max_examples=50)
def test_graph_intconstant_instantiation(instance):
    assert isinstance(instance, graph_IntConstant)



@given(instance=graph_IntConstant_strategy)
def test_graph_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph_Not_strategy)
@settings(max_examples=50)
def test_graph_not_instantiation(instance):
    assert isinstance(instance, graph_Not)

@given(instance=graph_MulOrDiv_strategy)
@settings(max_examples=50)
def test_graph_mulordiv_instantiation(instance):
    assert isinstance(instance, graph_MulOrDiv)



@given(instance=graph_MulOrDiv_strategy)
def test_graph_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph_PlusOrMin_strategy)
@settings(max_examples=50)
def test_graph_plusormin_instantiation(instance):
    assert isinstance(instance, graph_PlusOrMin)



@given(instance=graph_PlusOrMin_strategy)
def test_graph_plusormin_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph_Comparison_strategy)
@settings(max_examples=50)
def test_graph_comparison_instantiation(instance):
    assert isinstance(instance, graph_Comparison)



@given(instance=graph_Comparison_strategy)
def test_graph_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=graph_PathExistence_strategy)
@settings(max_examples=50)
def test_graph_pathexistence_instantiation(instance):
    assert isinstance(instance, graph_PathExistence)

@given(instance=graph_Statement_strategy)
@settings(max_examples=50)
def test_graph_statement_instantiation(instance):
    assert isinstance(instance, graph_Statement)

@given(instance=graph_Declaration_strategy)
@settings(max_examples=50)
def test_graph_declaration_instantiation(instance):
    assert isinstance(instance, graph_Declaration)



@given(instance=graph_Declaration_strategy)
def test_graph_declaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graph_Declaration_strategy)
def test_graph_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Program_strategy)
@settings(max_examples=50)
def test_graph_program_instantiation(instance):
    assert isinstance(instance, graph_Program)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Vertex_strategy)
@settings(max_examples=50)
def test_graph_vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)



@given(instance=graph_Vertex_strategy)
def test_graph_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Expr_strategy)
@settings(max_examples=50)
def test_graph_expr_instantiation(instance):
    assert isinstance(instance, graph_Expr)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=graph_WhileStmt_strategy)
@settings(max_examples=50)
def test_graph_whilestmt_instantiation(instance):
    assert isinstance(instance, graph_WhileStmt)

@given(instance=graph_IfStmt_strategy)
@settings(max_examples=50)
def test_graph_ifstmt_instantiation(instance):
    assert isinstance(instance, graph_IfStmt)

@given(instance=graph_MoveStmt_strategy)
@settings(max_examples=50)
def test_graph_movestmt_instantiation(instance):
    assert isinstance(instance, graph_MoveStmt)

@given(instance=graph_PrintStmt_strategy)
@settings(max_examples=50)
def test_graph_printstmt_instantiation(instance):
    assert isinstance(instance, graph_PrintStmt)

@given(instance=graph_AssignStmt_strategy)
@settings(max_examples=50)
def test_graph_assignstmt_instantiation(instance):
    assert isinstance(instance, graph_AssignStmt)

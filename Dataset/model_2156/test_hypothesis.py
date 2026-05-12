import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SkillGraph_Node,
    SkillGraph_Requirement,
    SkillGraph_Edge,
    SkillGraph_Equation,
    SkillGraph_Graph,
    SkillGraph_Parameter,
    Type,
    Category,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_skillgraph_node_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Node)


def test_skillgraph_node_constructor_exists():
    assert callable(SkillGraph_Node.__init__)


def test_skillgraph_node_constructor_args():
    sig = inspect.signature(SkillGraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "category" in params, "Missing parameter 'category'"
    assert "programPath" in params, "Missing parameter 'programPath'"

def test_skillgraph_node_has_name():
    assert hasattr(SkillGraph_Node, "name")
    descriptor = None
    for klass in SkillGraph_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_node_has_category():
    assert hasattr(SkillGraph_Node, "category")
    descriptor = None
    for klass in SkillGraph_Node.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_node_has_programPath():
    assert hasattr(SkillGraph_Node, "programPath")
    descriptor = None
    for klass in SkillGraph_Node.__mro__:
        if "programPath" in klass.__dict__:
            descriptor = klass.__dict__["programPath"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph_requirement_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Requirement)


def test_skillgraph_requirement_constructor_exists():
    assert callable(SkillGraph_Requirement.__init__)


def test_skillgraph_requirement_constructor_args():
    sig = inspect.signature(SkillGraph_Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_skillgraph_requirement_has_term():
    assert hasattr(SkillGraph_Requirement, "term")
    descriptor = None
    for klass in SkillGraph_Requirement.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_requirement_has_type():
    assert hasattr(SkillGraph_Requirement, "type")
    descriptor = None
    for klass in SkillGraph_Requirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_requirement_has_comment():
    assert hasattr(SkillGraph_Requirement, "comment")
    descriptor = None
    for klass in SkillGraph_Requirement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph_edge_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Edge)


def test_skillgraph_edge_constructor_exists():
    assert callable(SkillGraph_Edge.__init__)


def test_skillgraph_edge_constructor_args():
    sig = inspect.signature(SkillGraph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_skillgraph_equation_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Equation)


def test_skillgraph_equation_constructor_exists():
    assert callable(SkillGraph_Equation.__init__)


def test_skillgraph_equation_constructor_args():
    sig = inspect.signature(SkillGraph_Equation.__init__)
    params = list(sig.parameters.keys())
    assert "equation" in params, "Missing parameter 'equation'"

def test_skillgraph_equation_has_equation():
    assert hasattr(SkillGraph_Equation, "equation")
    descriptor = None
    for klass in SkillGraph_Equation.__mro__:
        if "equation" in klass.__dict__:
            descriptor = klass.__dict__["equation"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph_graph_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Graph)


def test_skillgraph_graph_constructor_exists():
    assert callable(SkillGraph_Graph.__init__)


def test_skillgraph_graph_constructor_args():
    sig = inspect.signature(SkillGraph_Graph.__init__)
    params = list(sig.parameters.keys())



def test_skillgraph_parameter_is_not_abstract():
    assert not inspect.isabstract(SkillGraph_Parameter)


def test_skillgraph_parameter_constructor_exists():
    assert callable(SkillGraph_Parameter.__init__)


def test_skillgraph_parameter_constructor_args():
    sig = inspect.signature(SkillGraph_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"

def test_skillgraph_parameter_has_name():
    assert hasattr(SkillGraph_Parameter, "name")
    descriptor = None
    for klass in SkillGraph_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_parameter_has_unit():
    assert hasattr(SkillGraph_Parameter, "unit")
    descriptor = None
    for klass in SkillGraph_Parameter.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_parameter_has_variable():
    assert hasattr(SkillGraph_Parameter, "variable")
    descriptor = None
    for klass in SkillGraph_Parameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_parameter_has_defaultValue():
    assert hasattr(SkillGraph_Parameter, "defaultValue")
    descriptor = None
    for klass in SkillGraph_Parameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph_parameter_has_abbreviation():
    assert hasattr(SkillGraph_Parameter, "abbreviation")
    descriptor = None
    for klass in SkillGraph_Parameter.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Functional_Safety_Requirement",
        "Technical_Safety_Requirement",
        "Technical_Requirement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_category_exists():
    # Check that the Enumeration exists
    assert Category is not None

def test_category_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Category]
    expected_literals = [
        "perception",
        "main",
        "planning",
        "observable_external_behavior",
        "action",
        "sensor",
        "actuator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Category"


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
SkillGraph_Node_strategy = st.builds(
    SkillGraph_Node,
    name=
        safe_text,
    category=
        safe_text,
    programPath=
        safe_text
)
SkillGraph_Requirement_strategy = st.builds(
    SkillGraph_Requirement,
    term=
        safe_text,
    type=
        safe_text,
    comment=
        safe_text
)
SkillGraph_Edge_strategy = st.builds(
    SkillGraph_Edge,
)
SkillGraph_Equation_strategy = st.builds(
    SkillGraph_Equation,
    equation=
        safe_text
)
SkillGraph_Graph_strategy = st.builds(
    SkillGraph_Graph,
)
SkillGraph_Parameter_strategy = st.builds(
    SkillGraph_Parameter,
    name=
        safe_text,
    unit=
        safe_text,
    variable=
        st.booleans(),
    defaultValue=
        safe_text,
    abbreviation=
        safe_text
)

@given(instance=SkillGraph_Node_strategy)
@settings(max_examples=50)
def test_skillgraph_node_instantiation(instance):
    assert isinstance(instance, SkillGraph_Node)



@given(instance=SkillGraph_Node_strategy)
def test_skillgraph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SkillGraph_Node_strategy)
def test_skillgraph_node_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SkillGraph_Node_strategy)
def test_skillgraph_node_programPath_setter(instance):
    original = instance.programPath
    instance.programPath = original
    assert instance.programPath == original

@given(instance=SkillGraph_Requirement_strategy)
@settings(max_examples=50)
def test_skillgraph_requirement_instantiation(instance):
    assert isinstance(instance, SkillGraph_Requirement)



@given(instance=SkillGraph_Requirement_strategy)
def test_skillgraph_requirement_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=SkillGraph_Requirement_strategy)
def test_skillgraph_requirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=SkillGraph_Requirement_strategy)
def test_skillgraph_requirement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=SkillGraph_Edge_strategy)
@settings(max_examples=50)
def test_skillgraph_edge_instantiation(instance):
    assert isinstance(instance, SkillGraph_Edge)

@given(instance=SkillGraph_Equation_strategy)
@settings(max_examples=50)
def test_skillgraph_equation_instantiation(instance):
    assert isinstance(instance, SkillGraph_Equation)



@given(instance=SkillGraph_Equation_strategy)
def test_skillgraph_equation_equation_setter(instance):
    original = instance.equation
    instance.equation = original
    assert instance.equation == original

@given(instance=SkillGraph_Graph_strategy)
@settings(max_examples=50)
def test_skillgraph_graph_instantiation(instance):
    assert isinstance(instance, SkillGraph_Graph)

@given(instance=SkillGraph_Parameter_strategy)
@settings(max_examples=50)
def test_skillgraph_parameter_instantiation(instance):
    assert isinstance(instance, SkillGraph_Parameter)



@given(instance=SkillGraph_Parameter_strategy)
def test_skillgraph_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SkillGraph_Parameter_strategy)
def test_skillgraph_parameter_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=SkillGraph_Parameter_strategy)
def test_skillgraph_parameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=SkillGraph_Parameter_strategy)
def test_skillgraph_parameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=SkillGraph_Parameter_strategy)
def test_skillgraph_parameter_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original

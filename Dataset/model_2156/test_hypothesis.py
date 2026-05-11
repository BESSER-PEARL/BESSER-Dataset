import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SkillGraph::Node,
    SkillGraph::Requirement,
    SkillGraph::Edge,
    SkillGraph::Equation,
    SkillGraph::Graph,
    SkillGraph::Parameter,
    Category,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_skillgraph::node_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Node)


def test_skillgraph::node_constructor_exists():
    assert callable(SkillGraph::Node.__init__)


def test_skillgraph::node_constructor_args():
    sig = inspect.signature(SkillGraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "programPath" in params, "Missing parameter 'programPath'"
    assert "category" in params, "Missing parameter 'category'"

def test_skillgraph::node_has_name():
    assert hasattr(SkillGraph::Node, "name")
    descriptor = None
    for klass in SkillGraph::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::node_has_programPath():
    assert hasattr(SkillGraph::Node, "programPath")
    descriptor = None
    for klass in SkillGraph::Node.__mro__:
        if "programPath" in klass.__dict__:
            descriptor = klass.__dict__["programPath"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::node_has_category():
    assert hasattr(SkillGraph::Node, "category")
    descriptor = None
    for klass in SkillGraph::Node.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph::requirement_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Requirement)


def test_skillgraph::requirement_constructor_exists():
    assert callable(SkillGraph::Requirement.__init__)


def test_skillgraph::requirement_constructor_args():
    sig = inspect.signature(SkillGraph::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_skillgraph::requirement_has_term():
    assert hasattr(SkillGraph::Requirement, "term")
    descriptor = None
    for klass in SkillGraph::Requirement.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::requirement_has_type():
    assert hasattr(SkillGraph::Requirement, "type")
    descriptor = None
    for klass in SkillGraph::Requirement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::requirement_has_comment():
    assert hasattr(SkillGraph::Requirement, "comment")
    descriptor = None
    for klass in SkillGraph::Requirement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph::edge_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Edge)


def test_skillgraph::edge_constructor_exists():
    assert callable(SkillGraph::Edge.__init__)


def test_skillgraph::edge_constructor_args():
    sig = inspect.signature(SkillGraph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_skillgraph::equation_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Equation)


def test_skillgraph::equation_constructor_exists():
    assert callable(SkillGraph::Equation.__init__)


def test_skillgraph::equation_constructor_args():
    sig = inspect.signature(SkillGraph::Equation.__init__)
    params = list(sig.parameters.keys())
    assert "equation" in params, "Missing parameter 'equation'"

def test_skillgraph::equation_has_equation():
    assert hasattr(SkillGraph::Equation, "equation")
    descriptor = None
    for klass in SkillGraph::Equation.__mro__:
        if "equation" in klass.__dict__:
            descriptor = klass.__dict__["equation"]
            break
    assert isinstance(descriptor, property)



def test_skillgraph::graph_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Graph)


def test_skillgraph::graph_constructor_exists():
    assert callable(SkillGraph::Graph.__init__)


def test_skillgraph::graph_constructor_args():
    sig = inspect.signature(SkillGraph::Graph.__init__)
    params = list(sig.parameters.keys())



def test_skillgraph::parameter_is_not_abstract():
    assert not inspect.isabstract(SkillGraph::Parameter)


def test_skillgraph::parameter_constructor_exists():
    assert callable(SkillGraph::Parameter.__init__)


def test_skillgraph::parameter_constructor_args():
    sig = inspect.signature(SkillGraph::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "abbreviation" in params, "Missing parameter 'abbreviation'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "name" in params, "Missing parameter 'name'"

def test_skillgraph::parameter_has_abbreviation():
    assert hasattr(SkillGraph::Parameter, "abbreviation")
    descriptor = None
    for klass in SkillGraph::Parameter.__mro__:
        if "abbreviation" in klass.__dict__:
            descriptor = klass.__dict__["abbreviation"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::parameter_has_variable():
    assert hasattr(SkillGraph::Parameter, "variable")
    descriptor = None
    for klass in SkillGraph::Parameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::parameter_has_defaultValue():
    assert hasattr(SkillGraph::Parameter, "defaultValue")
    descriptor = None
    for klass in SkillGraph::Parameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::parameter_has_unit():
    assert hasattr(SkillGraph::Parameter, "unit")
    descriptor = None
    for klass in SkillGraph::Parameter.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_skillgraph::parameter_has_name():
    assert hasattr(SkillGraph::Parameter, "name")
    descriptor = None
    for klass in SkillGraph::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_category_exists():
    # Check that the Enumeration exists
    assert Category is not None

def test_category_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Category]
    expected_literals = [
        "sensor",
        "action",
        "planning",
        "perception",
        "main",
        "actuator",
        "observable_external_behavior",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Category"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Functional_Safety_Requirement",
        "Technical_Requirement",
        "Technical_Safety_Requirement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
SkillGraph::Node_strategy = st.builds(
    SkillGraph::Node,
    name=
        safe_text,
    programPath=
        safe_text,
    category=
        safe_text
)
SkillGraph::Requirement_strategy = st.builds(
    SkillGraph::Requirement,
    term=
        safe_text,
    type=
        safe_text,
    comment=
        safe_text
)
SkillGraph::Edge_strategy = st.builds(
    SkillGraph::Edge,
)
SkillGraph::Equation_strategy = st.builds(
    SkillGraph::Equation,
    equation=
        safe_text
)
SkillGraph::Graph_strategy = st.builds(
    SkillGraph::Graph,
)
SkillGraph::Parameter_strategy = st.builds(
    SkillGraph::Parameter,
    abbreviation=
        safe_text,
    variable=
        st.booleans(),
    defaultValue=
        safe_text,
    unit=
        safe_text,
    name=
        safe_text
)

@given(instance=SkillGraph::Node_strategy)
@settings(max_examples=50)
def test_skillgraph::node_instantiation(instance):
    assert isinstance(instance, SkillGraph::Node)

@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_programPath_type(instance):
    assert isinstance(instance.programPath, str)


@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_programPath_setter(instance):
    original = instance.programPath
    instance.programPath = original
    assert instance.programPath == original

@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=SkillGraph::Node_strategy)
def test_skillgraph::node_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=SkillGraph::Requirement_strategy)
@settings(max_examples=50)
def test_skillgraph::requirement_instantiation(instance):
    assert isinstance(instance, SkillGraph::Requirement)

@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_term_type(instance):
    assert isinstance(instance.term, str)


@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=SkillGraph::Requirement_strategy)
def test_skillgraph::requirement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=SkillGraph::Edge_strategy)
@settings(max_examples=50)
def test_skillgraph::edge_instantiation(instance):
    assert isinstance(instance, SkillGraph::Edge)

@given(instance=SkillGraph::Equation_strategy)
@settings(max_examples=50)
def test_skillgraph::equation_instantiation(instance):
    assert isinstance(instance, SkillGraph::Equation)

@given(instance=SkillGraph::Equation_strategy)
def test_skillgraph::equation_equation_type(instance):
    assert isinstance(instance.equation, str)


@given(instance=SkillGraph::Equation_strategy)
def test_skillgraph::equation_equation_setter(instance):
    original = instance.equation
    instance.equation = original
    assert instance.equation == original

@given(instance=SkillGraph::Graph_strategy)
@settings(max_examples=50)
def test_skillgraph::graph_instantiation(instance):
    assert isinstance(instance, SkillGraph::Graph)

@given(instance=SkillGraph::Parameter_strategy)
@settings(max_examples=50)
def test_skillgraph::parameter_instantiation(instance):
    assert isinstance(instance, SkillGraph::Parameter)

@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_abbreviation_type(instance):
    assert isinstance(instance.abbreviation, str)


@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_abbreviation_setter(instance):
    original = instance.abbreviation
    instance.abbreviation = original
    assert instance.abbreviation == original

@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_variable_type(instance):
    assert isinstance(instance.variable, bool)


@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SkillGraph::Parameter_strategy)
def test_skillgraph::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

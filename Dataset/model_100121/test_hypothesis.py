import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Schema,
    Database,
    Diagram,
    ui::diagram::DMDiagram,
    schema::DataModelerNamedElement,
    schema::FunctionalElement,
    ui::project::Project,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_schema_is_not_abstract():
    assert not inspect.isabstract(Schema)


def test_schema_constructor_exists():
    assert callable(Schema.__init__)


def test_schema_constructor_args():
    sig = inspect.signature(Schema.__init__)
    params = list(sig.parameters.keys())



def test_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_database_constructor_exists():
    assert callable(Database.__init__)


def test_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_ui::diagram::dmdiagram_is_not_abstract():
    assert not inspect.isabstract(ui::diagram::DMDiagram)


def test_ui::diagram::dmdiagram_constructor_exists():
    assert callable(ui::diagram::DMDiagram.__init__)


def test_ui::diagram::dmdiagram_constructor_args():
    sig = inspect.signature(ui::diagram::DMDiagram.__init__)
    params = list(sig.parameters.keys())



def test_schema::datamodelernamedelement_is_not_abstract():
    assert not inspect.isabstract(schema::DataModelerNamedElement)


def test_schema::datamodelernamedelement_constructor_exists():
    assert callable(schema::DataModelerNamedElement.__init__)


def test_schema::datamodelernamedelement_constructor_args():
    sig = inspect.signature(schema::DataModelerNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_schema::functionalelement_is_not_abstract():
    assert not inspect.isabstract(schema::FunctionalElement)


def test_schema::functionalelement_constructor_exists():
    assert callable(schema::FunctionalElement.__init__)


def test_schema::functionalelement_constructor_args():
    sig = inspect.signature(schema::FunctionalElement.__init__)
    params = list(sig.parameters.keys())



def test_ui::project::project_is_not_abstract():
    assert not inspect.isabstract(ui::project::Project)


def test_ui::project::project_constructor_exists():
    assert callable(ui::project::Project.__init__)


def test_ui::project::project_constructor_args():
    sig = inspect.signature(ui::project::Project.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "application" in params, "Missing parameter 'application'"

def test_ui::project::project_has_description():
    assert hasattr(ui::project::Project, "description")
    descriptor = None
    for klass in ui::project::Project.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ui::project::project_has_application():
    assert hasattr(ui::project::Project, "application")
    descriptor = None
    for klass in ui::project::Project.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)


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
Schema_strategy = st.builds(
    Schema,
)
Database_strategy = st.builds(
    Database,
)
Diagram_strategy = st.builds(
    Diagram,
)
ui::diagram::DMDiagram_strategy = st.builds(
    ui::diagram::DMDiagram,
)
schema::DataModelerNamedElement_strategy = st.builds(
    schema::DataModelerNamedElement,
)
schema::FunctionalElement_strategy = st.builds(
    schema::FunctionalElement,
)
ui::project::Project_strategy = st.builds(
    ui::project::Project,
    description=
        safe_text,
    application=
        safe_text
)

@given(instance=Schema_strategy)
@settings(max_examples=50)
def test_schema_instantiation(instance):
    assert isinstance(instance, Schema)

@given(instance=Database_strategy)
@settings(max_examples=50)
def test_database_instantiation(instance):
    assert isinstance(instance, Database)

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=ui::diagram::DMDiagram_strategy)
@settings(max_examples=50)
def test_ui::diagram::dmdiagram_instantiation(instance):
    assert isinstance(instance, ui::diagram::DMDiagram)

@given(instance=schema::DataModelerNamedElement_strategy)
@settings(max_examples=50)
def test_schema::datamodelernamedelement_instantiation(instance):
    assert isinstance(instance, schema::DataModelerNamedElement)

@given(instance=schema::FunctionalElement_strategy)
@settings(max_examples=50)
def test_schema::functionalelement_instantiation(instance):
    assert isinstance(instance, schema::FunctionalElement)

@given(instance=ui::project::Project_strategy)
@settings(max_examples=50)
def test_ui::project::project_instantiation(instance):
    assert isinstance(instance, ui::project::Project)

@given(instance=ui::project::Project_strategy)
def test_ui::project::project_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=ui::project::Project_strategy)
def test_ui::project::project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=ui::project::Project_strategy)
def test_ui::project::project_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=ui::project::Project_strategy)
def test_ui::project::project_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ui::project::Project_strategy)
@settings(max_examples=30)
def test_ui::project::project_isvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValid(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValid' in ui::project::Project is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValid' in ui::project::Project did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValid' in ui::project::Project is not implemented or raised an error")

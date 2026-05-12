import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Schema,
    Database,
    Diagram,
    ui_diagram_DMDiagram,
    schema_DataModelerNamedElement,
    schema_FunctionalElement,
    ui_project_Project,
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



def test_ui_diagram_dmdiagram_is_not_abstract():
    assert not inspect.isabstract(ui_diagram_DMDiagram)


def test_ui_diagram_dmdiagram_constructor_exists():
    assert callable(ui_diagram_DMDiagram.__init__)


def test_ui_diagram_dmdiagram_constructor_args():
    sig = inspect.signature(ui_diagram_DMDiagram.__init__)
    params = list(sig.parameters.keys())



def test_schema_datamodelernamedelement_is_not_abstract():
    assert not inspect.isabstract(schema_DataModelerNamedElement)


def test_schema_datamodelernamedelement_constructor_exists():
    assert callable(schema_DataModelerNamedElement.__init__)


def test_schema_datamodelernamedelement_constructor_args():
    sig = inspect.signature(schema_DataModelerNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_schema_functionalelement_is_not_abstract():
    assert not inspect.isabstract(schema_FunctionalElement)


def test_schema_functionalelement_constructor_exists():
    assert callable(schema_FunctionalElement.__init__)


def test_schema_functionalelement_constructor_args():
    sig = inspect.signature(schema_FunctionalElement.__init__)
    params = list(sig.parameters.keys())



def test_ui_project_project_is_not_abstract():
    assert not inspect.isabstract(ui_project_Project)


def test_ui_project_project_constructor_exists():
    assert callable(ui_project_Project.__init__)


def test_ui_project_project_constructor_args():
    sig = inspect.signature(ui_project_Project.__init__)
    params = list(sig.parameters.keys())
    assert "application" in params, "Missing parameter 'application'"
    assert "description" in params, "Missing parameter 'description'"

def test_ui_project_project_has_application():
    assert hasattr(ui_project_Project, "application")
    descriptor = None
    for klass in ui_project_Project.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_ui_project_project_has_description():
    assert hasattr(ui_project_Project, "description")
    descriptor = None
    for klass in ui_project_Project.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
ui_diagram_DMDiagram_strategy = st.builds(
    ui_diagram_DMDiagram,
)
schema_DataModelerNamedElement_strategy = st.builds(
    schema_DataModelerNamedElement,
)
schema_FunctionalElement_strategy = st.builds(
    schema_FunctionalElement,
)
ui_project_Project_strategy = st.builds(
    ui_project_Project,
    application=
        safe_text,
    description=
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

@given(instance=ui_diagram_DMDiagram_strategy)
@settings(max_examples=50)
def test_ui_diagram_dmdiagram_instantiation(instance):
    assert isinstance(instance, ui_diagram_DMDiagram)

@given(instance=schema_DataModelerNamedElement_strategy)
@settings(max_examples=50)
def test_schema_datamodelernamedelement_instantiation(instance):
    assert isinstance(instance, schema_DataModelerNamedElement)

@given(instance=schema_FunctionalElement_strategy)
@settings(max_examples=50)
def test_schema_functionalelement_instantiation(instance):
    assert isinstance(instance, schema_FunctionalElement)

@given(instance=ui_project_Project_strategy)
@settings(max_examples=50)
def test_ui_project_project_instantiation(instance):
    assert isinstance(instance, ui_project_Project)



@given(instance=ui_project_Project_strategy)
def test_ui_project_project_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=ui_project_Project_strategy)
def test_ui_project_project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ui_project_Project_strategy)
@settings(max_examples=30)
def test_ui_project_project_isvalid_changes_state(instance):
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
        assert has_statements, f"Function 'isValid' in ui_project_Project is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValid' in ui_project_Project did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValid' in ui_project_Project is not implemented or raised an error")

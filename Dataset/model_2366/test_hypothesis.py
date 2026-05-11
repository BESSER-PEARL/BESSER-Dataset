import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sql::Annotation,
    sql::ModelElement,
    NamedElement,
    sql::Table,
    Key,
    sql::Schema,
    sql::ForeignKey,
    sql::PrimaryKey,
    ModelElement,
    sql::Key,
    sql::Event,
    sql::Column,
    sql::NamedElement,
    Condition,
    Action,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql::annotation_is_not_abstract():
    assert not inspect.isabstract(sql::Annotation)


def test_sql::annotation_constructor_exists():
    assert callable(sql::Annotation.__init__)


def test_sql::annotation_constructor_args():
    sig = inspect.signature(sql::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "annotation" in params, "Missing parameter 'annotation'"

def test_sql::annotation_has_annotation():
    assert hasattr(sql::Annotation, "annotation")
    descriptor = None
    for klass in sql::Annotation.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)



def test_sql::modelelement_is_not_abstract():
    assert not inspect.isabstract(sql::ModelElement)


def test_sql::modelelement_constructor_exists():
    assert callable(sql::ModelElement.__init__)


def test_sql::modelelement_constructor_args():
    sig = inspect.signature(sql::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sql::table_is_not_abstract():
    assert not inspect.isabstract(sql::Table)


def test_sql::table_constructor_exists():
    assert callable(sql::Table.__init__)


def test_sql::table_constructor_args():
    sig = inspect.signature(sql::Table.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_sql::schema_is_not_abstract():
    assert not inspect.isabstract(sql::Schema)


def test_sql::schema_constructor_exists():
    assert callable(sql::Schema.__init__)


def test_sql::schema_constructor_args():
    sig = inspect.signature(sql::Schema.__init__)
    params = list(sig.parameters.keys())



def test_sql::foreignkey_is_not_abstract():
    assert not inspect.isabstract(sql::ForeignKey)


def test_sql::foreignkey_constructor_exists():
    assert callable(sql::ForeignKey.__init__)


def test_sql::foreignkey_constructor_args():
    sig = inspect.signature(sql::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql::primarykey_is_not_abstract():
    assert not inspect.isabstract(sql::PrimaryKey)


def test_sql::primarykey_constructor_exists():
    assert callable(sql::PrimaryKey.__init__)


def test_sql::primarykey_constructor_args():
    sig = inspect.signature(sql::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sql::key_is_not_abstract():
    assert not inspect.isabstract(sql::Key)


def test_sql::key_constructor_exists():
    assert callable(sql::Key.__init__)


def test_sql::key_constructor_args():
    sig = inspect.signature(sql::Key.__init__)
    params = list(sig.parameters.keys())



def test_sql::event_is_not_abstract():
    assert not inspect.isabstract(sql::Event)


def test_sql::event_constructor_exists():
    assert callable(sql::Event.__init__)


def test_sql::event_constructor_args():
    sig = inspect.signature(sql::Event.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_sql::event_has_action():
    assert hasattr(sql::Event, "action")
    descriptor = None
    for klass in sql::Event.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_sql::event_has_condition():
    assert hasattr(sql::Event, "condition")
    descriptor = None
    for klass in sql::Event.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_sql::column_is_not_abstract():
    assert not inspect.isabstract(sql::Column)


def test_sql::column_constructor_exists():
    assert callable(sql::Column.__init__)


def test_sql::column_constructor_args():
    sig = inspect.signature(sql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "properties" in params, "Missing parameter 'properties'"

def test_sql::column_has_type():
    assert hasattr(sql::Column, "type")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sql::column_has_properties():
    assert hasattr(sql::Column, "properties")
    descriptor = None
    for klass in sql::Column.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)



def test_sql::namedelement_is_not_abstract():
    assert not inspect.isabstract(sql::NamedElement)


def test_sql::namedelement_constructor_exists():
    assert callable(sql::NamedElement.__init__)


def test_sql::namedelement_constructor_args():
    sig = inspect.signature(sql::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::namedelement_has_name():
    assert hasattr(sql::NamedElement, "name")
    descriptor = None
    for klass in sql::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_condition_exists():
    # Check that the Enumeration exists
    assert Condition is not None

def test_condition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Condition]
    expected_literals = [
        "Delete",
        "Update",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Condition"

def test_action_exists():
    # Check that the Enumeration exists
    assert Action is not None

def test_action_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Action]
    expected_literals = [
        "SetNull",
        "Cascade",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Action"

def test_property_exists():
    # Check that the Enumeration exists
    assert Property is not None

def test_property_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Property]
    expected_literals = [
        "AutoIncrement",
        "Unique",
        "NotNull",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Property"


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
sql::Annotation_strategy = st.builds(
    sql::Annotation,
    annotation=
        safe_text
)
sql::ModelElement_strategy = st.builds(
    sql::ModelElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sql::Table_strategy = st.builds(
    sql::Table,
)
Key_strategy = st.builds(
    Key,
)
sql::Schema_strategy = st.builds(
    sql::Schema,
)
sql::ForeignKey_strategy = st.builds(
    sql::ForeignKey,
)
sql::PrimaryKey_strategy = st.builds(
    sql::PrimaryKey,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
sql::Key_strategy = st.builds(
    sql::Key,
)
sql::Event_strategy = st.builds(
    sql::Event,
    action=
        safe_text,
    condition=
        safe_text
)
sql::Column_strategy = st.builds(
    sql::Column,
    type=
        safe_text,
    properties=
        safe_text
)
sql::NamedElement_strategy = st.builds(
    sql::NamedElement,
    name=
        safe_text
)

@given(instance=sql::Annotation_strategy)
@settings(max_examples=50)
def test_sql::annotation_instantiation(instance):
    assert isinstance(instance, sql::Annotation)

@given(instance=sql::Annotation_strategy)
def test_sql::annotation_annotation_type(instance):
    assert isinstance(instance.annotation, str)


@given(instance=sql::Annotation_strategy)
def test_sql::annotation_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=sql::ModelElement_strategy)
@settings(max_examples=50)
def test_sql::modelelement_instantiation(instance):
    assert isinstance(instance, sql::ModelElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sql::Table_strategy)
@settings(max_examples=50)
def test_sql::table_instantiation(instance):
    assert isinstance(instance, sql::Table)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=sql::Schema_strategy)
@settings(max_examples=50)
def test_sql::schema_instantiation(instance):
    assert isinstance(instance, sql::Schema)

@given(instance=sql::ForeignKey_strategy)
@settings(max_examples=50)
def test_sql::foreignkey_instantiation(instance):
    assert isinstance(instance, sql::ForeignKey)

@given(instance=sql::PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql::primarykey_instantiation(instance):
    assert isinstance(instance, sql::PrimaryKey)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=sql::Key_strategy)
@settings(max_examples=50)
def test_sql::key_instantiation(instance):
    assert isinstance(instance, sql::Key)

@given(instance=sql::Event_strategy)
@settings(max_examples=50)
def test_sql::event_instantiation(instance):
    assert isinstance(instance, sql::Event)

@given(instance=sql::Event_strategy)
def test_sql::event_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=sql::Event_strategy)
def test_sql::event_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=sql::Event_strategy)
def test_sql::event_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=sql::Event_strategy)
def test_sql::event_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=sql::Column_strategy)
@settings(max_examples=50)
def test_sql::column_instantiation(instance):
    assert isinstance(instance, sql::Column)

@given(instance=sql::Column_strategy)
def test_sql::column_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sql::Column_strategy)
def test_sql::column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql::Column_strategy)
def test_sql::column_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=sql::Column_strategy)
def test_sql::column_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=sql::NamedElement_strategy)
@settings(max_examples=50)
def test_sql::namedelement_instantiation(instance):
    assert isinstance(instance, sql::NamedElement)

@given(instance=sql::NamedElement_strategy)
def test_sql::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::NamedElement_strategy)
def test_sql::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

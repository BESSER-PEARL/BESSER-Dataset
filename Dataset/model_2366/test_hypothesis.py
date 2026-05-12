import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sql_Annotation,
    sql_ModelElement,
    NamedElement,
    sql_Table,
    Key,
    sql_Schema,
    sql_ForeignKey,
    sql_PrimaryKey,
    ModelElement,
    sql_Column,
    sql_Event,
    sql_Key,
    sql_NamedElement,
    Condition,
    Property,
    Action,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sql_annotation_is_not_abstract():
    assert not inspect.isabstract(sql_Annotation)


def test_sql_annotation_constructor_exists():
    assert callable(sql_Annotation.__init__)


def test_sql_annotation_constructor_args():
    sig = inspect.signature(sql_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "annotation" in params, "Missing parameter 'annotation'"

def test_sql_annotation_has_annotation():
    assert hasattr(sql_Annotation, "annotation")
    descriptor = None
    for klass in sql_Annotation.__mro__:
        if "annotation" in klass.__dict__:
            descriptor = klass.__dict__["annotation"]
            break
    assert isinstance(descriptor, property)



def test_sql_modelelement_is_not_abstract():
    assert not inspect.isabstract(sql_ModelElement)


def test_sql_modelelement_constructor_exists():
    assert callable(sql_ModelElement.__init__)


def test_sql_modelelement_constructor_args():
    sig = inspect.signature(sql_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sql_table_is_not_abstract():
    assert not inspect.isabstract(sql_Table)


def test_sql_table_constructor_exists():
    assert callable(sql_Table.__init__)


def test_sql_table_constructor_args():
    sig = inspect.signature(sql_Table.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_sql_schema_is_not_abstract():
    assert not inspect.isabstract(sql_Schema)


def test_sql_schema_constructor_exists():
    assert callable(sql_Schema.__init__)


def test_sql_schema_constructor_args():
    sig = inspect.signature(sql_Schema.__init__)
    params = list(sig.parameters.keys())



def test_sql_foreignkey_is_not_abstract():
    assert not inspect.isabstract(sql_ForeignKey)


def test_sql_foreignkey_constructor_exists():
    assert callable(sql_ForeignKey.__init__)


def test_sql_foreignkey_constructor_args():
    sig = inspect.signature(sql_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_sql_primarykey_is_not_abstract():
    assert not inspect.isabstract(sql_PrimaryKey)


def test_sql_primarykey_constructor_exists():
    assert callable(sql_PrimaryKey.__init__)


def test_sql_primarykey_constructor_args():
    sig = inspect.signature(sql_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_is_not_abstract():
    assert not inspect.isabstract(sql_Column)


def test_sql_column_constructor_exists():
    assert callable(sql_Column.__init__)


def test_sql_column_constructor_args():
    sig = inspect.signature(sql_Column.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "properties" in params, "Missing parameter 'properties'"

def test_sql_column_has_type():
    assert hasattr(sql_Column, "type")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sql_column_has_properties():
    assert hasattr(sql_Column, "properties")
    descriptor = None
    for klass in sql_Column.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)



def test_sql_event_is_not_abstract():
    assert not inspect.isabstract(sql_Event)


def test_sql_event_constructor_exists():
    assert callable(sql_Event.__init__)


def test_sql_event_constructor_args():
    sig = inspect.signature(sql_Event.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_sql_event_has_action():
    assert hasattr(sql_Event, "action")
    descriptor = None
    for klass in sql_Event.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_sql_event_has_condition():
    assert hasattr(sql_Event, "condition")
    descriptor = None
    for klass in sql_Event.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_sql_key_is_not_abstract():
    assert not inspect.isabstract(sql_Key)


def test_sql_key_constructor_exists():
    assert callable(sql_Key.__init__)


def test_sql_key_constructor_args():
    sig = inspect.signature(sql_Key.__init__)
    params = list(sig.parameters.keys())



def test_sql_namedelement_is_not_abstract():
    assert not inspect.isabstract(sql_NamedElement)


def test_sql_namedelement_constructor_exists():
    assert callable(sql_NamedElement.__init__)


def test_sql_namedelement_constructor_args():
    sig = inspect.signature(sql_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_namedelement_has_name():
    assert hasattr(sql_NamedElement, "name")
    descriptor = None
    for klass in sql_NamedElement.__mro__:
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

def test_action_exists():
    # Check that the Enumeration exists
    assert Action is not None

def test_action_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Action]
    expected_literals = [
        "Cascade",
        "SetNull",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Action"


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
sql_Annotation_strategy = st.builds(
    sql_Annotation,
    annotation=
        safe_text
)
sql_ModelElement_strategy = st.builds(
    sql_ModelElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sql_Table_strategy = st.builds(
    sql_Table,
)
Key_strategy = st.builds(
    Key,
)
sql_Schema_strategy = st.builds(
    sql_Schema,
)
sql_ForeignKey_strategy = st.builds(
    sql_ForeignKey,
)
sql_PrimaryKey_strategy = st.builds(
    sql_PrimaryKey,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
sql_Column_strategy = st.builds(
    sql_Column,
    type=
        safe_text,
    properties=
        safe_text
)
sql_Event_strategy = st.builds(
    sql_Event,
    action=
        safe_text,
    condition=
        safe_text
)
sql_Key_strategy = st.builds(
    sql_Key,
)
sql_NamedElement_strategy = st.builds(
    sql_NamedElement,
    name=
        safe_text
)

@given(instance=sql_Annotation_strategy)
@settings(max_examples=50)
def test_sql_annotation_instantiation(instance):
    assert isinstance(instance, sql_Annotation)



@given(instance=sql_Annotation_strategy)
def test_sql_annotation_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original

@given(instance=sql_ModelElement_strategy)
@settings(max_examples=50)
def test_sql_modelelement_instantiation(instance):
    assert isinstance(instance, sql_ModelElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sql_Table_strategy)
@settings(max_examples=50)
def test_sql_table_instantiation(instance):
    assert isinstance(instance, sql_Table)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=sql_Schema_strategy)
@settings(max_examples=50)
def test_sql_schema_instantiation(instance):
    assert isinstance(instance, sql_Schema)

@given(instance=sql_ForeignKey_strategy)
@settings(max_examples=50)
def test_sql_foreignkey_instantiation(instance):
    assert isinstance(instance, sql_ForeignKey)

@given(instance=sql_PrimaryKey_strategy)
@settings(max_examples=50)
def test_sql_primarykey_instantiation(instance):
    assert isinstance(instance, sql_PrimaryKey)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=sql_Column_strategy)
@settings(max_examples=50)
def test_sql_column_instantiation(instance):
    assert isinstance(instance, sql_Column)



@given(instance=sql_Column_strategy)
def test_sql_column_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=sql_Column_strategy)
def test_sql_column_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=sql_Event_strategy)
@settings(max_examples=50)
def test_sql_event_instantiation(instance):
    assert isinstance(instance, sql_Event)



@given(instance=sql_Event_strategy)
def test_sql_event_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=sql_Event_strategy)
def test_sql_event_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=sql_Key_strategy)
@settings(max_examples=50)
def test_sql_key_instantiation(instance):
    assert isinstance(instance, sql_Key)

@given(instance=sql_NamedElement_strategy)
@settings(max_examples=50)
def test_sql_namedelement_instantiation(instance):
    assert isinstance(instance, sql_NamedElement)



@given(instance=sql_NamedElement_strategy)
def test_sql_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

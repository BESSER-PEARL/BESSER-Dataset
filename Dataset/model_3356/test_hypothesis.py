import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Widget,
    uispecDsl::CheckBoxWidget,
    uispecDsl::ComboWidget,
    uispecDsl::TextFieldWidget,
    uispecDsl::Attribute,
    uispecDsl::Widget,
    uispecDsl::Entity,
    uispecDsl::EntityReference,
    uispecDsl::Form,
    uispecDsl::Field,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::checkboxwidget_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::CheckBoxWidget)


def test_uispecdsl::checkboxwidget_constructor_exists():
    assert callable(uispecDsl::CheckBoxWidget.__init__)


def test_uispecdsl::checkboxwidget_constructor_args():
    sig = inspect.signature(uispecDsl::CheckBoxWidget.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::combowidget_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::ComboWidget)


def test_uispecdsl::combowidget_constructor_exists():
    assert callable(uispecDsl::ComboWidget.__init__)


def test_uispecdsl::combowidget_constructor_args():
    sig = inspect.signature(uispecDsl::ComboWidget.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_uispecdsl::combowidget_has_values():
    assert hasattr(uispecDsl::ComboWidget, "values")
    descriptor = None
    for klass in uispecDsl::ComboWidget.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_uispecdsl::textfieldwidget_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::TextFieldWidget)


def test_uispecdsl::textfieldwidget_constructor_exists():
    assert callable(uispecDsl::TextFieldWidget.__init__)


def test_uispecdsl::textfieldwidget_constructor_args():
    sig = inspect.signature(uispecDsl::TextFieldWidget.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_uispecdsl::textfieldwidget_has_length():
    assert hasattr(uispecDsl::TextFieldWidget, "length")
    descriptor = None
    for klass in uispecDsl::TextFieldWidget.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_uispecdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::Attribute)


def test_uispecdsl::attribute_constructor_exists():
    assert callable(uispecDsl::Attribute.__init__)


def test_uispecdsl::attribute_constructor_args():
    sig = inspect.signature(uispecDsl::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::widget_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::Widget)


def test_uispecdsl::widget_constructor_exists():
    assert callable(uispecDsl::Widget.__init__)


def test_uispecdsl::widget_constructor_args():
    sig = inspect.signature(uispecDsl::Widget.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::entity_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::Entity)


def test_uispecdsl::entity_constructor_exists():
    assert callable(uispecDsl::Entity.__init__)


def test_uispecdsl::entity_constructor_args():
    sig = inspect.signature(uispecDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::entityreference_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::EntityReference)


def test_uispecdsl::entityreference_constructor_exists():
    assert callable(uispecDsl::EntityReference.__init__)


def test_uispecdsl::entityreference_constructor_args():
    sig = inspect.signature(uispecDsl::EntityReference.__init__)
    params = list(sig.parameters.keys())



def test_uispecdsl::form_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::Form)


def test_uispecdsl::form_constructor_exists():
    assert callable(uispecDsl::Form.__init__)


def test_uispecdsl::form_constructor_args():
    sig = inspect.signature(uispecDsl::Form.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uispecdsl::form_has_name():
    assert hasattr(uispecDsl::Form, "name")
    descriptor = None
    for klass in uispecDsl::Form.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uispecdsl::field_is_not_abstract():
    assert not inspect.isabstract(uispecDsl::Field)


def test_uispecdsl::field_constructor_exists():
    assert callable(uispecDsl::Field.__init__)


def test_uispecdsl::field_constructor_args():
    sig = inspect.signature(uispecDsl::Field.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_uispecdsl::field_has_label():
    assert hasattr(uispecDsl::Field, "label")
    descriptor = None
    for klass in uispecDsl::Field.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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
Widget_strategy = st.builds(
    Widget,
)
uispecDsl::CheckBoxWidget_strategy = st.builds(
    uispecDsl::CheckBoxWidget,
)
uispecDsl::ComboWidget_strategy = st.builds(
    uispecDsl::ComboWidget,
    values=
        safe_text
)
uispecDsl::TextFieldWidget_strategy = st.builds(
    uispecDsl::TextFieldWidget,
    length=
        st.integers()
)
uispecDsl::Attribute_strategy = st.builds(
    uispecDsl::Attribute,
)
uispecDsl::Widget_strategy = st.builds(
    uispecDsl::Widget,
)
uispecDsl::Entity_strategy = st.builds(
    uispecDsl::Entity,
)
uispecDsl::EntityReference_strategy = st.builds(
    uispecDsl::EntityReference,
)
uispecDsl::Form_strategy = st.builds(
    uispecDsl::Form,
    name=
        safe_text
)
uispecDsl::Field_strategy = st.builds(
    uispecDsl::Field,
    label=
        safe_text
)

@given(instance=Widget_strategy)
@settings(max_examples=50)
def test_widget_instantiation(instance):
    assert isinstance(instance, Widget)

@given(instance=uispecDsl::CheckBoxWidget_strategy)
@settings(max_examples=50)
def test_uispecdsl::checkboxwidget_instantiation(instance):
    assert isinstance(instance, uispecDsl::CheckBoxWidget)

@given(instance=uispecDsl::ComboWidget_strategy)
@settings(max_examples=50)
def test_uispecdsl::combowidget_instantiation(instance):
    assert isinstance(instance, uispecDsl::ComboWidget)

@given(instance=uispecDsl::ComboWidget_strategy)
def test_uispecdsl::combowidget_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=uispecDsl::ComboWidget_strategy)
def test_uispecdsl::combowidget_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=uispecDsl::TextFieldWidget_strategy)
@settings(max_examples=50)
def test_uispecdsl::textfieldwidget_instantiation(instance):
    assert isinstance(instance, uispecDsl::TextFieldWidget)

@given(instance=uispecDsl::TextFieldWidget_strategy)
def test_uispecdsl::textfieldwidget_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=uispecDsl::TextFieldWidget_strategy)
def test_uispecdsl::textfieldwidget_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=uispecDsl::Attribute_strategy)
@settings(max_examples=50)
def test_uispecdsl::attribute_instantiation(instance):
    assert isinstance(instance, uispecDsl::Attribute)

@given(instance=uispecDsl::Widget_strategy)
@settings(max_examples=50)
def test_uispecdsl::widget_instantiation(instance):
    assert isinstance(instance, uispecDsl::Widget)

@given(instance=uispecDsl::Entity_strategy)
@settings(max_examples=50)
def test_uispecdsl::entity_instantiation(instance):
    assert isinstance(instance, uispecDsl::Entity)

@given(instance=uispecDsl::EntityReference_strategy)
@settings(max_examples=50)
def test_uispecdsl::entityreference_instantiation(instance):
    assert isinstance(instance, uispecDsl::EntityReference)

@given(instance=uispecDsl::Form_strategy)
@settings(max_examples=50)
def test_uispecdsl::form_instantiation(instance):
    assert isinstance(instance, uispecDsl::Form)

@given(instance=uispecDsl::Form_strategy)
def test_uispecdsl::form_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uispecDsl::Form_strategy)
def test_uispecdsl::form_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uispecDsl::Field_strategy)
@settings(max_examples=50)
def test_uispecdsl::field_instantiation(instance):
    assert isinstance(instance, uispecDsl::Field)

@given(instance=uispecDsl::Field_strategy)
def test_uispecdsl::field_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=uispecDsl::Field_strategy)
def test_uispecdsl::field_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

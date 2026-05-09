import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UIComponent,
    mvc::UIInput,
    mvc::UIActions,
    mvc::UILayout,
    Annotable,
    mvc::Event,
    mvc::View,
    mvc::UIComponent,
    mvc::Entity,
    mvc::Controller,
    mvc::Attribute,
    mvc::Component,
    mvc::Association,
    mvc::MVCModel,
    mvc::ControllerView,
    mvc::Action,
    mvc::EventAction,
    mvc::Model,
    AssociationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uicomponent_is_not_abstract():
    assert not inspect.isabstract(UIComponent)


def test_uicomponent_constructor_exists():
    assert callable(UIComponent.__init__)


def test_uicomponent_constructor_args():
    sig = inspect.signature(UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_mvc::uiinput_is_not_abstract():
    assert not inspect.isabstract(mvc::UIInput)


def test_mvc::uiinput_constructor_exists():
    assert callable(mvc::UIInput.__init__)


def test_mvc::uiinput_constructor_args():
    sig = inspect.signature(mvc::UIInput.__init__)
    params = list(sig.parameters.keys())



def test_mvc::uiactions_is_not_abstract():
    assert not inspect.isabstract(mvc::UIActions)


def test_mvc::uiactions_constructor_exists():
    assert callable(mvc::UIActions.__init__)


def test_mvc::uiactions_constructor_args():
    sig = inspect.signature(mvc::UIActions.__init__)
    params = list(sig.parameters.keys())



def test_mvc::uilayout_is_not_abstract():
    assert not inspect.isabstract(mvc::UILayout)


def test_mvc::uilayout_constructor_exists():
    assert callable(mvc::UILayout.__init__)


def test_mvc::uilayout_constructor_args():
    sig = inspect.signature(mvc::UILayout.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "columns" in params, "Missing parameter 'columns'"

def test_mvc::uilayout_has_orientation():
    assert hasattr(mvc::UILayout, "orientation")
    descriptor = None
    for klass in mvc::UILayout.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_mvc::uilayout_has_columns():
    assert hasattr(mvc::UILayout, "columns")
    descriptor = None
    for klass in mvc::UILayout.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_annotable_is_not_abstract():
    assert not inspect.isabstract(Annotable)


def test_annotable_constructor_exists():
    assert callable(Annotable.__init__)


def test_annotable_constructor_args():
    sig = inspect.signature(Annotable.__init__)
    params = list(sig.parameters.keys())



def test_mvc::event_is_not_abstract():
    assert not inspect.isabstract(mvc::Event)


def test_mvc::event_constructor_exists():
    assert callable(mvc::Event.__init__)


def test_mvc::event_constructor_args():
    sig = inspect.signature(mvc::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::event_has_name():
    assert hasattr(mvc::Event, "name")
    descriptor = None
    for klass in mvc::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::view_is_not_abstract():
    assert not inspect.isabstract(mvc::View)


def test_mvc::view_constructor_exists():
    assert callable(mvc::View.__init__)


def test_mvc::view_constructor_args():
    sig = inspect.signature(mvc::View.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::view_has_name():
    assert hasattr(mvc::View, "name")
    descriptor = None
    for klass in mvc::View.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::uicomponent_is_not_abstract():
    assert not inspect.isabstract(mvc::UIComponent)


def test_mvc::uicomponent_constructor_exists():
    assert callable(mvc::UIComponent.__init__)


def test_mvc::uicomponent_constructor_args():
    sig = inspect.signature(mvc::UIComponent.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::uicomponent_has_type():
    assert hasattr(mvc::UIComponent, "type")
    descriptor = None
    for klass in mvc::UIComponent.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mvc::uicomponent_has_name():
    assert hasattr(mvc::UIComponent, "name")
    descriptor = None
    for klass in mvc::UIComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::entity_is_not_abstract():
    assert not inspect.isabstract(mvc::Entity)


def test_mvc::entity_constructor_exists():
    assert callable(mvc::Entity.__init__)


def test_mvc::entity_constructor_args():
    sig = inspect.signature(mvc::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::entity_has_name():
    assert hasattr(mvc::Entity, "name")
    descriptor = None
    for klass in mvc::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::controller_is_not_abstract():
    assert not inspect.isabstract(mvc::Controller)


def test_mvc::controller_constructor_exists():
    assert callable(mvc::Controller.__init__)


def test_mvc::controller_constructor_args():
    sig = inspect.signature(mvc::Controller.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::controller_has_name():
    assert hasattr(mvc::Controller, "name")
    descriptor = None
    for klass in mvc::Controller.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::attribute_is_not_abstract():
    assert not inspect.isabstract(mvc::Attribute)


def test_mvc::attribute_constructor_exists():
    assert callable(mvc::Attribute.__init__)


def test_mvc::attribute_constructor_args():
    sig = inspect.signature(mvc::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::attribute_has_type():
    assert hasattr(mvc::Attribute, "type")
    descriptor = None
    for klass in mvc::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mvc::attribute_has_name():
    assert hasattr(mvc::Attribute, "name")
    descriptor = None
    for klass in mvc::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::component_is_not_abstract():
    assert not inspect.isabstract(mvc::Component)


def test_mvc::component_constructor_exists():
    assert callable(mvc::Component.__init__)


def test_mvc::component_constructor_args():
    sig = inspect.signature(mvc::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::component_has_name():
    assert hasattr(mvc::Component, "name")
    descriptor = None
    for klass in mvc::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::association_is_not_abstract():
    assert not inspect.isabstract(mvc::Association)


def test_mvc::association_constructor_exists():
    assert callable(mvc::Association.__init__)


def test_mvc::association_constructor_args():
    sig = inspect.signature(mvc::Association.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_mvc::association_has_containment():
    assert hasattr(mvc::Association, "containment")
    descriptor = None
    for klass in mvc::Association.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)

def test_mvc::association_has_lowerBound():
    assert hasattr(mvc::Association, "lowerBound")
    descriptor = None
    for klass in mvc::Association.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_mvc::association_has_upperBound():
    assert hasattr(mvc::Association, "upperBound")
    descriptor = None
    for klass in mvc::Association.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_mvc::association_has_name():
    assert hasattr(mvc::Association, "name")
    descriptor = None
    for klass in mvc::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mvc::association_has_type():
    assert hasattr(mvc::Association, "type")
    descriptor = None
    for klass in mvc::Association.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mvc::mvcmodel_is_not_abstract():
    assert not inspect.isabstract(mvc::MVCModel)


def test_mvc::mvcmodel_constructor_exists():
    assert callable(mvc::MVCModel.__init__)


def test_mvc::mvcmodel_constructor_args():
    sig = inspect.signature(mvc::MVCModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_mvc::mvcmodel_has_name():
    assert hasattr(mvc::MVCModel, "name")
    descriptor = None
    for klass in mvc::MVCModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mvc::mvcmodel_has_version():
    assert hasattr(mvc::MVCModel, "version")
    descriptor = None
    for klass in mvc::MVCModel.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_mvc::controllerview_is_not_abstract():
    assert not inspect.isabstract(mvc::ControllerView)


def test_mvc::controllerview_constructor_exists():
    assert callable(mvc::ControllerView.__init__)


def test_mvc::controllerview_constructor_args():
    sig = inspect.signature(mvc::ControllerView.__init__)
    params = list(sig.parameters.keys())



def test_mvc::action_is_not_abstract():
    assert not inspect.isabstract(mvc::Action)


def test_mvc::action_constructor_exists():
    assert callable(mvc::Action.__init__)


def test_mvc::action_constructor_args():
    sig = inspect.signature(mvc::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::action_has_name():
    assert hasattr(mvc::Action, "name")
    descriptor = None
    for klass in mvc::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mvc::eventaction_is_not_abstract():
    assert not inspect.isabstract(mvc::EventAction)


def test_mvc::eventaction_constructor_exists():
    assert callable(mvc::EventAction.__init__)


def test_mvc::eventaction_constructor_args():
    sig = inspect.signature(mvc::EventAction.__init__)
    params = list(sig.parameters.keys())



def test_mvc::model_is_not_abstract():
    assert not inspect.isabstract(mvc::Model)


def test_mvc::model_constructor_exists():
    assert callable(mvc::Model.__init__)


def test_mvc::model_constructor_args():
    sig = inspect.signature(mvc::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mvc::model_has_name():
    assert hasattr(mvc::Model, "name")
    descriptor = None
    for klass in mvc::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_associationtype_exists():
    # Check that the Enumeration exists
    assert AssociationType is not None

def test_associationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationType"


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
UIComponent_strategy = st.builds(
    UIComponent,
)
mvc::UIInput_strategy = st.builds(
    mvc::UIInput,
)
mvc::UIActions_strategy = st.builds(
    mvc::UIActions,
)
mvc::UILayout_strategy = st.builds(
    mvc::UILayout,
    orientation=
        safe_text,
    columns=
        st.integers()
)
Annotable_strategy = st.builds(
    Annotable,
)
mvc::Event_strategy = st.builds(
    mvc::Event,
    name=
        safe_text
)
mvc::View_strategy = st.builds(
    mvc::View,
    name=
        safe_text
)
mvc::UIComponent_strategy = st.builds(
    mvc::UIComponent,
    type=
        safe_text,
    name=
        safe_text
)
mvc::Entity_strategy = st.builds(
    mvc::Entity,
    name=
        safe_text
)
mvc::Controller_strategy = st.builds(
    mvc::Controller,
    name=
        safe_text
)
mvc::Attribute_strategy = st.builds(
    mvc::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
mvc::Component_strategy = st.builds(
    mvc::Component,
    name=
        safe_text
)
mvc::Association_strategy = st.builds(
    mvc::Association,
    containment=
        st.booleans(),
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    name=
        safe_text,
    type=
        safe_text
)
mvc::MVCModel_strategy = st.builds(
    mvc::MVCModel,
    name=
        safe_text,
    version=
        safe_text
)
mvc::ControllerView_strategy = st.builds(
    mvc::ControllerView,
)
mvc::Action_strategy = st.builds(
    mvc::Action,
    name=
        safe_text
)
mvc::EventAction_strategy = st.builds(
    mvc::EventAction,
)
mvc::Model_strategy = st.builds(
    mvc::Model,
    name=
        safe_text
)

@given(instance=UIComponent_strategy)
@settings(max_examples=50)
def test_uicomponent_instantiation(instance):
    assert isinstance(instance, UIComponent)

@given(instance=mvc::UIInput_strategy)
@settings(max_examples=50)
def test_mvc::uiinput_instantiation(instance):
    assert isinstance(instance, mvc::UIInput)

@given(instance=mvc::UIActions_strategy)
@settings(max_examples=50)
def test_mvc::uiactions_instantiation(instance):
    assert isinstance(instance, mvc::UIActions)

@given(instance=mvc::UILayout_strategy)
@settings(max_examples=50)
def test_mvc::uilayout_instantiation(instance):
    assert isinstance(instance, mvc::UILayout)

@given(instance=mvc::UILayout_strategy)
def test_mvc::uilayout_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=mvc::UILayout_strategy)
def test_mvc::uilayout_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=mvc::UILayout_strategy)
def test_mvc::uilayout_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=mvc::UILayout_strategy)
def test_mvc::uilayout_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=Annotable_strategy)
@settings(max_examples=50)
def test_annotable_instantiation(instance):
    assert isinstance(instance, Annotable)

@given(instance=mvc::Event_strategy)
@settings(max_examples=50)
def test_mvc::event_instantiation(instance):
    assert isinstance(instance, mvc::Event)

@given(instance=mvc::Event_strategy)
def test_mvc::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Event_strategy)
def test_mvc::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::View_strategy)
@settings(max_examples=50)
def test_mvc::view_instantiation(instance):
    assert isinstance(instance, mvc::View)

@given(instance=mvc::View_strategy)
def test_mvc::view_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::View_strategy)
def test_mvc::view_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::UIComponent_strategy)
@settings(max_examples=50)
def test_mvc::uicomponent_instantiation(instance):
    assert isinstance(instance, mvc::UIComponent)

@given(instance=mvc::UIComponent_strategy)
def test_mvc::uicomponent_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mvc::UIComponent_strategy)
def test_mvc::uicomponent_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mvc::UIComponent_strategy)
def test_mvc::uicomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::UIComponent_strategy)
def test_mvc::uicomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Entity_strategy)
@settings(max_examples=50)
def test_mvc::entity_instantiation(instance):
    assert isinstance(instance, mvc::Entity)

@given(instance=mvc::Entity_strategy)
def test_mvc::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Entity_strategy)
def test_mvc::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Controller_strategy)
@settings(max_examples=50)
def test_mvc::controller_instantiation(instance):
    assert isinstance(instance, mvc::Controller)

@given(instance=mvc::Controller_strategy)
def test_mvc::controller_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Controller_strategy)
def test_mvc::controller_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Attribute_strategy)
@settings(max_examples=50)
def test_mvc::attribute_instantiation(instance):
    assert isinstance(instance, mvc::Attribute)

@given(instance=mvc::Attribute_strategy)
def test_mvc::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mvc::Attribute_strategy)
def test_mvc::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mvc::Attribute_strategy)
def test_mvc::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Attribute_strategy)
def test_mvc::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Component_strategy)
@settings(max_examples=50)
def test_mvc::component_instantiation(instance):
    assert isinstance(instance, mvc::Component)

@given(instance=mvc::Component_strategy)
def test_mvc::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Component_strategy)
def test_mvc::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Association_strategy)
@settings(max_examples=50)
def test_mvc::association_instantiation(instance):
    assert isinstance(instance, mvc::Association)

@given(instance=mvc::Association_strategy)
def test_mvc::association_containment_type(instance):
    assert isinstance(instance.containment, bool)


@given(instance=mvc::Association_strategy)
def test_mvc::association_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=mvc::Association_strategy)
def test_mvc::association_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=mvc::Association_strategy)
def test_mvc::association_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=mvc::Association_strategy)
def test_mvc::association_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=mvc::Association_strategy)
def test_mvc::association_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=mvc::Association_strategy)
def test_mvc::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Association_strategy)
def test_mvc::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::Association_strategy)
def test_mvc::association_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mvc::Association_strategy)
def test_mvc::association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mvc::MVCModel_strategy)
@settings(max_examples=50)
def test_mvc::mvcmodel_instantiation(instance):
    assert isinstance(instance, mvc::MVCModel)

@given(instance=mvc::MVCModel_strategy)
def test_mvc::mvcmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::MVCModel_strategy)
def test_mvc::mvcmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::MVCModel_strategy)
def test_mvc::mvcmodel_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mvc::MVCModel_strategy)
def test_mvc::mvcmodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mvc::ControllerView_strategy)
@settings(max_examples=50)
def test_mvc::controllerview_instantiation(instance):
    assert isinstance(instance, mvc::ControllerView)

@given(instance=mvc::Action_strategy)
@settings(max_examples=50)
def test_mvc::action_instantiation(instance):
    assert isinstance(instance, mvc::Action)

@given(instance=mvc::Action_strategy)
def test_mvc::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Action_strategy)
def test_mvc::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mvc::EventAction_strategy)
@settings(max_examples=50)
def test_mvc::eventaction_instantiation(instance):
    assert isinstance(instance, mvc::EventAction)

@given(instance=mvc::Model_strategy)
@settings(max_examples=50)
def test_mvc::model_instantiation(instance):
    assert isinstance(instance, mvc::Model)

@given(instance=mvc::Model_strategy)
def test_mvc::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mvc::Model_strategy)
def test_mvc::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

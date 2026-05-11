import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UIElement,
    myDsl01::Label,
    myDsl01::Bounds,
    myDsl01::Button,
    myDsl01::Field,
    myDsl01::Property,
    myDsl01::Window,
    myDsl01::UIElement,
    Window,
    myDsl01::EntryWindow,
    myDsl01::ListWindow,
    myDsl01::Size,
    Property,
    myDsl01::Reference,
    myDsl01::Attribute,
    myDsl01::Entity,
    myDsl01::Model,
    AttributeType,
    ButtonKind,
    MultiplicityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uielement_is_not_abstract():
    assert not inspect.isabstract(UIElement)


def test_uielement_constructor_exists():
    assert callable(UIElement.__init__)


def test_uielement_constructor_args():
    sig = inspect.signature(UIElement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::label_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Label)


def test_mydsl01::label_constructor_exists():
    assert callable(myDsl01::Label.__init__)


def test_mydsl01::label_constructor_args():
    sig = inspect.signature(myDsl01::Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mydsl01::label_has_text():
    assert hasattr(myDsl01::Label, "text")
    descriptor = None
    for klass in myDsl01::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::bounds_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Bounds)


def test_mydsl01::bounds_constructor_exists():
    assert callable(myDsl01::Bounds.__init__)


def test_mydsl01::bounds_constructor_args():
    sig = inspect.signature(myDsl01::Bounds.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"

def test_mydsl01::bounds_has_width():
    assert hasattr(myDsl01::Bounds, "width")
    descriptor = None
    for klass in myDsl01::Bounds.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::bounds_has_x():
    assert hasattr(myDsl01::Bounds, "x")
    descriptor = None
    for klass in myDsl01::Bounds.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::bounds_has_y():
    assert hasattr(myDsl01::Bounds, "y")
    descriptor = None
    for klass in myDsl01::Bounds.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::bounds_has_height():
    assert hasattr(myDsl01::Bounds, "height")
    descriptor = None
    for klass in myDsl01::Bounds.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::button_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Button)


def test_mydsl01::button_constructor_exists():
    assert callable(myDsl01::Button.__init__)


def test_mydsl01::button_constructor_args():
    sig = inspect.signature(myDsl01::Button.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_mydsl01::button_has_text():
    assert hasattr(myDsl01::Button, "text")
    descriptor = None
    for klass in myDsl01::Button.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::button_has_kind():
    assert hasattr(myDsl01::Button, "kind")
    descriptor = None
    for klass in myDsl01::Button.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::field_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Field)


def test_mydsl01::field_constructor_exists():
    assert callable(myDsl01::Field.__init__)


def test_mydsl01::field_constructor_args():
    sig = inspect.signature(myDsl01::Field.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::property_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Property)


def test_mydsl01::property_constructor_exists():
    assert callable(myDsl01::Property.__init__)


def test_mydsl01::property_constructor_args():
    sig = inspect.signature(myDsl01::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01::property_has_name():
    assert hasattr(myDsl01::Property, "name")
    descriptor = None
    for klass in myDsl01::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::window_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Window)


def test_mydsl01::window_constructor_exists():
    assert callable(myDsl01::Window.__init__)


def test_mydsl01::window_constructor_args():
    sig = inspect.signature(myDsl01::Window.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01::window_has_title():
    assert hasattr(myDsl01::Window, "title")
    descriptor = None
    for klass in myDsl01::Window.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::window_has_name():
    assert hasattr(myDsl01::Window, "name")
    descriptor = None
    for klass in myDsl01::Window.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::uielement_is_not_abstract():
    assert not inspect.isabstract(myDsl01::UIElement)


def test_mydsl01::uielement_constructor_exists():
    assert callable(myDsl01::UIElement.__init__)


def test_mydsl01::uielement_constructor_args():
    sig = inspect.signature(myDsl01::UIElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01::uielement_has_name():
    assert hasattr(myDsl01::UIElement, "name")
    descriptor = None
    for klass in myDsl01::UIElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_window_is_not_abstract():
    assert not inspect.isabstract(Window)


def test_window_constructor_exists():
    assert callable(Window.__init__)


def test_window_constructor_args():
    sig = inspect.signature(Window.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::entrywindow_is_not_abstract():
    assert not inspect.isabstract(myDsl01::EntryWindow)


def test_mydsl01::entrywindow_constructor_exists():
    assert callable(myDsl01::EntryWindow.__init__)


def test_mydsl01::entrywindow_constructor_args():
    sig = inspect.signature(myDsl01::EntryWindow.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::listwindow_is_not_abstract():
    assert not inspect.isabstract(myDsl01::ListWindow)


def test_mydsl01::listwindow_constructor_exists():
    assert callable(myDsl01::ListWindow.__init__)


def test_mydsl01::listwindow_constructor_args():
    sig = inspect.signature(myDsl01::ListWindow.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::size_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Size)


def test_mydsl01::size_constructor_exists():
    assert callable(myDsl01::Size.__init__)


def test_mydsl01::size_constructor_args():
    sig = inspect.signature(myDsl01::Size.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_mydsl01::size_has_height():
    assert hasattr(myDsl01::Size, "height")
    descriptor = None
    for klass in myDsl01::Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::size_has_width():
    assert hasattr(myDsl01::Size, "width")
    descriptor = None
    for klass in myDsl01::Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01::reference_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Reference)


def test_mydsl01::reference_constructor_exists():
    assert callable(myDsl01::Reference.__init__)


def test_mydsl01::reference_constructor_args():
    sig = inspect.signature(myDsl01::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_mydsl01::reference_has_multiplicity():
    assert hasattr(myDsl01::Reference, "multiplicity")
    descriptor = None
    for klass in myDsl01::Reference.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Attribute)


def test_mydsl01::attribute_constructor_exists():
    assert callable(myDsl01::Attribute.__init__)


def test_mydsl01::attribute_constructor_args():
    sig = inspect.signature(myDsl01::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_mydsl01::attribute_has_type():
    assert hasattr(myDsl01::Attribute, "type")
    descriptor = None
    for klass in myDsl01::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::attribute_has_optional():
    assert hasattr(myDsl01::Attribute, "optional")
    descriptor = None
    for klass in myDsl01::Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Entity)


def test_mydsl01::entity_constructor_exists():
    assert callable(myDsl01::Entity.__init__)


def test_mydsl01::entity_constructor_args():
    sig = inspect.signature(myDsl01::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01::entity_has_abstract():
    assert hasattr(myDsl01::Entity, "abstract")
    descriptor = None
    for klass in myDsl01::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01::entity_has_name():
    assert hasattr(myDsl01::Entity, "name")
    descriptor = None
    for klass in myDsl01::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01::model_is_not_abstract():
    assert not inspect.isabstract(myDsl01::Model)


def test_mydsl01::model_constructor_exists():
    assert callable(myDsl01::Model.__init__)


def test_mydsl01::model_constructor_args():
    sig = inspect.signature(myDsl01::Model.__init__)
    params = list(sig.parameters.keys())

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "Date",
        "Integer",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"

def test_buttonkind_exists():
    # Check that the Enumeration exists
    assert ButtonKind is not None

def test_buttonkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonKind]
    expected_literals = [
        "cancel",
        "delete",
        "createEdit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonKind"

def test_multiplicitykind_exists():
    # Check that the Enumeration exists
    assert MultiplicityKind is not None

def test_multiplicitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicityKind]
    expected_literals = [
        "Single",
        "Multiple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicityKind"


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
UIElement_strategy = st.builds(
    UIElement,
)
myDsl01::Label_strategy = st.builds(
    myDsl01::Label,
    text=
        safe_text
)
myDsl01::Bounds_strategy = st.builds(
    myDsl01::Bounds,
    width=
        st.integers(),
    x=
        st.integers(),
    y=
        st.integers(),
    height=
        st.integers()
)
myDsl01::Button_strategy = st.builds(
    myDsl01::Button,
    text=
        safe_text,
    kind=
        safe_text
)
myDsl01::Field_strategy = st.builds(
    myDsl01::Field,
)
myDsl01::Property_strategy = st.builds(
    myDsl01::Property,
    name=
        safe_text
)
myDsl01::Window_strategy = st.builds(
    myDsl01::Window,
    title=
        safe_text,
    name=
        safe_text
)
myDsl01::UIElement_strategy = st.builds(
    myDsl01::UIElement,
    name=
        safe_text
)
Window_strategy = st.builds(
    Window,
)
myDsl01::EntryWindow_strategy = st.builds(
    myDsl01::EntryWindow,
)
myDsl01::ListWindow_strategy = st.builds(
    myDsl01::ListWindow,
)
myDsl01::Size_strategy = st.builds(
    myDsl01::Size,
    height=
        st.integers(),
    width=
        st.integers()
)
Property_strategy = st.builds(
    Property,
)
myDsl01::Reference_strategy = st.builds(
    myDsl01::Reference,
    multiplicity=
        safe_text
)
myDsl01::Attribute_strategy = st.builds(
    myDsl01::Attribute,
    type=
        safe_text,
    optional=
        st.booleans()
)
myDsl01::Entity_strategy = st.builds(
    myDsl01::Entity,
    abstract=
        st.booleans(),
    name=
        safe_text
)
myDsl01::Model_strategy = st.builds(
    myDsl01::Model,
)

@given(instance=UIElement_strategy)
@settings(max_examples=50)
def test_uielement_instantiation(instance):
    assert isinstance(instance, UIElement)

@given(instance=myDsl01::Label_strategy)
@settings(max_examples=50)
def test_mydsl01::label_instantiation(instance):
    assert isinstance(instance, myDsl01::Label)

@given(instance=myDsl01::Label_strategy)
def test_mydsl01::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=myDsl01::Label_strategy)
def test_mydsl01::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl01::Bounds_strategy)
@settings(max_examples=50)
def test_mydsl01::bounds_instantiation(instance):
    assert isinstance(instance, myDsl01::Bounds)

@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=myDsl01::Bounds_strategy)
def test_mydsl01::bounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=myDsl01::Button_strategy)
@settings(max_examples=50)
def test_mydsl01::button_instantiation(instance):
    assert isinstance(instance, myDsl01::Button)

@given(instance=myDsl01::Button_strategy)
def test_mydsl01::button_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=myDsl01::Button_strategy)
def test_mydsl01::button_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl01::Button_strategy)
def test_mydsl01::button_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=myDsl01::Button_strategy)
def test_mydsl01::button_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=myDsl01::Field_strategy)
@settings(max_examples=50)
def test_mydsl01::field_instantiation(instance):
    assert isinstance(instance, myDsl01::Field)

@given(instance=myDsl01::Property_strategy)
@settings(max_examples=50)
def test_mydsl01::property_instantiation(instance):
    assert isinstance(instance, myDsl01::Property)

@given(instance=myDsl01::Property_strategy)
def test_mydsl01::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl01::Property_strategy)
def test_mydsl01::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl01::Window_strategy)
@settings(max_examples=50)
def test_mydsl01::window_instantiation(instance):
    assert isinstance(instance, myDsl01::Window)

@given(instance=myDsl01::Window_strategy)
def test_mydsl01::window_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=myDsl01::Window_strategy)
def test_mydsl01::window_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=myDsl01::Window_strategy)
def test_mydsl01::window_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl01::Window_strategy)
def test_mydsl01::window_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl01::UIElement_strategy)
@settings(max_examples=50)
def test_mydsl01::uielement_instantiation(instance):
    assert isinstance(instance, myDsl01::UIElement)

@given(instance=myDsl01::UIElement_strategy)
def test_mydsl01::uielement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl01::UIElement_strategy)
def test_mydsl01::uielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Window_strategy)
@settings(max_examples=50)
def test_window_instantiation(instance):
    assert isinstance(instance, Window)

@given(instance=myDsl01::EntryWindow_strategy)
@settings(max_examples=50)
def test_mydsl01::entrywindow_instantiation(instance):
    assert isinstance(instance, myDsl01::EntryWindow)

@given(instance=myDsl01::ListWindow_strategy)
@settings(max_examples=50)
def test_mydsl01::listwindow_instantiation(instance):
    assert isinstance(instance, myDsl01::ListWindow)

@given(instance=myDsl01::Size_strategy)
@settings(max_examples=50)
def test_mydsl01::size_instantiation(instance):
    assert isinstance(instance, myDsl01::Size)

@given(instance=myDsl01::Size_strategy)
def test_mydsl01::size_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=myDsl01::Size_strategy)
def test_mydsl01::size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=myDsl01::Size_strategy)
def test_mydsl01::size_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=myDsl01::Size_strategy)
def test_mydsl01::size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=myDsl01::Reference_strategy)
@settings(max_examples=50)
def test_mydsl01::reference_instantiation(instance):
    assert isinstance(instance, myDsl01::Reference)

@given(instance=myDsl01::Reference_strategy)
def test_mydsl01::reference_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=myDsl01::Reference_strategy)
def test_mydsl01::reference_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=myDsl01::Attribute_strategy)
@settings(max_examples=50)
def test_mydsl01::attribute_instantiation(instance):
    assert isinstance(instance, myDsl01::Attribute)

@given(instance=myDsl01::Attribute_strategy)
def test_mydsl01::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl01::Attribute_strategy)
def test_mydsl01::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl01::Attribute_strategy)
def test_mydsl01::attribute_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=myDsl01::Attribute_strategy)
def test_mydsl01::attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=myDsl01::Entity_strategy)
@settings(max_examples=50)
def test_mydsl01::entity_instantiation(instance):
    assert isinstance(instance, myDsl01::Entity)

@given(instance=myDsl01::Entity_strategy)
def test_mydsl01::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=myDsl01::Entity_strategy)
def test_mydsl01::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=myDsl01::Entity_strategy)
def test_mydsl01::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl01::Entity_strategy)
def test_mydsl01::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl01::Model_strategy)
@settings(max_examples=50)
def test_mydsl01::model_instantiation(instance):
    assert isinstance(instance, myDsl01::Model)

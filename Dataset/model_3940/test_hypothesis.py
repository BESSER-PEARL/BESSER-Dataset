import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UIElement,
    myDsl01_Label,
    myDsl01_Bounds,
    myDsl01_Button,
    myDsl01_Field,
    myDsl01_Property,
    myDsl01_Window,
    myDsl01_UIElement,
    Window,
    myDsl01_EntryWindow,
    myDsl01_ListWindow,
    myDsl01_Size,
    Property,
    myDsl01_Reference,
    myDsl01_Attribute,
    myDsl01_Entity,
    myDsl01_Model,
    MultiplicityKind,
    AttributeType,
    ButtonKind,
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



def test_mydsl01_label_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Label)


def test_mydsl01_label_constructor_exists():
    assert callable(myDsl01_Label.__init__)


def test_mydsl01_label_constructor_args():
    sig = inspect.signature(myDsl01_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_mydsl01_label_has_text():
    assert hasattr(myDsl01_Label, "text")
    descriptor = None
    for klass in myDsl01_Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_bounds_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Bounds)


def test_mydsl01_bounds_constructor_exists():
    assert callable(myDsl01_Bounds.__init__)


def test_mydsl01_bounds_constructor_args():
    sig = inspect.signature(myDsl01_Bounds.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"

def test_mydsl01_bounds_has_height():
    assert hasattr(myDsl01_Bounds, "height")
    descriptor = None
    for klass in myDsl01_Bounds.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_bounds_has_y():
    assert hasattr(myDsl01_Bounds, "y")
    descriptor = None
    for klass in myDsl01_Bounds.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_bounds_has_x():
    assert hasattr(myDsl01_Bounds, "x")
    descriptor = None
    for klass in myDsl01_Bounds.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_bounds_has_width():
    assert hasattr(myDsl01_Bounds, "width")
    descriptor = None
    for klass in myDsl01_Bounds.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_button_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Button)


def test_mydsl01_button_constructor_exists():
    assert callable(myDsl01_Button.__init__)


def test_mydsl01_button_constructor_args():
    sig = inspect.signature(myDsl01_Button.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "text" in params, "Missing parameter 'text'"

def test_mydsl01_button_has_kind():
    assert hasattr(myDsl01_Button, "kind")
    descriptor = None
    for klass in myDsl01_Button.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_button_has_text():
    assert hasattr(myDsl01_Button, "text")
    descriptor = None
    for klass in myDsl01_Button.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_field_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Field)


def test_mydsl01_field_constructor_exists():
    assert callable(myDsl01_Field.__init__)


def test_mydsl01_field_constructor_args():
    sig = inspect.signature(myDsl01_Field.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01_property_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Property)


def test_mydsl01_property_constructor_exists():
    assert callable(myDsl01_Property.__init__)


def test_mydsl01_property_constructor_args():
    sig = inspect.signature(myDsl01_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01_property_has_name():
    assert hasattr(myDsl01_Property, "name")
    descriptor = None
    for klass in myDsl01_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_window_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Window)


def test_mydsl01_window_constructor_exists():
    assert callable(myDsl01_Window.__init__)


def test_mydsl01_window_constructor_args():
    sig = inspect.signature(myDsl01_Window.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "title" in params, "Missing parameter 'title'"

def test_mydsl01_window_has_name():
    assert hasattr(myDsl01_Window, "name")
    descriptor = None
    for klass in myDsl01_Window.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_window_has_title():
    assert hasattr(myDsl01_Window, "title")
    descriptor = None
    for klass in myDsl01_Window.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_uielement_is_not_abstract():
    assert not inspect.isabstract(myDsl01_UIElement)


def test_mydsl01_uielement_constructor_exists():
    assert callable(myDsl01_UIElement.__init__)


def test_mydsl01_uielement_constructor_args():
    sig = inspect.signature(myDsl01_UIElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01_uielement_has_name():
    assert hasattr(myDsl01_UIElement, "name")
    descriptor = None
    for klass in myDsl01_UIElement.__mro__:
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



def test_mydsl01_entrywindow_is_not_abstract():
    assert not inspect.isabstract(myDsl01_EntryWindow)


def test_mydsl01_entrywindow_constructor_exists():
    assert callable(myDsl01_EntryWindow.__init__)


def test_mydsl01_entrywindow_constructor_args():
    sig = inspect.signature(myDsl01_EntryWindow.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01_listwindow_is_not_abstract():
    assert not inspect.isabstract(myDsl01_ListWindow)


def test_mydsl01_listwindow_constructor_exists():
    assert callable(myDsl01_ListWindow.__init__)


def test_mydsl01_listwindow_constructor_args():
    sig = inspect.signature(myDsl01_ListWindow.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01_size_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Size)


def test_mydsl01_size_constructor_exists():
    assert callable(myDsl01_Size.__init__)


def test_mydsl01_size_constructor_args():
    sig = inspect.signature(myDsl01_Size.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_mydsl01_size_has_width():
    assert hasattr(myDsl01_Size, "width")
    descriptor = None
    for klass in myDsl01_Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_size_has_height():
    assert hasattr(myDsl01_Size, "height")
    descriptor = None
    for klass in myDsl01_Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_mydsl01_reference_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Reference)


def test_mydsl01_reference_constructor_exists():
    assert callable(myDsl01_Reference.__init__)


def test_mydsl01_reference_constructor_args():
    sig = inspect.signature(myDsl01_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_mydsl01_reference_has_multiplicity():
    assert hasattr(myDsl01_Reference, "multiplicity")
    descriptor = None
    for klass in myDsl01_Reference.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Attribute)


def test_mydsl01_attribute_constructor_exists():
    assert callable(myDsl01_Attribute.__init__)


def test_mydsl01_attribute_constructor_args():
    sig = inspect.signature(myDsl01_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_mydsl01_attribute_has_type():
    assert hasattr(myDsl01_Attribute, "type")
    descriptor = None
    for klass in myDsl01_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_attribute_has_optional():
    assert hasattr(myDsl01_Attribute, "optional")
    descriptor = None
    for klass in myDsl01_Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Entity)


def test_mydsl01_entity_constructor_exists():
    assert callable(myDsl01_Entity.__init__)


def test_mydsl01_entity_constructor_args():
    sig = inspect.signature(myDsl01_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl01_entity_has_abstract():
    assert hasattr(myDsl01_Entity, "abstract")
    descriptor = None
    for klass in myDsl01_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_mydsl01_entity_has_name():
    assert hasattr(myDsl01_Entity, "name")
    descriptor = None
    for klass in myDsl01_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl01_model_is_not_abstract():
    assert not inspect.isabstract(myDsl01_Model)


def test_mydsl01_model_constructor_exists():
    assert callable(myDsl01_Model.__init__)


def test_mydsl01_model_constructor_args():
    sig = inspect.signature(myDsl01_Model.__init__)
    params = list(sig.parameters.keys())

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

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "Date",
        "String",
        "Integer",
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
myDsl01_Label_strategy = st.builds(
    myDsl01_Label,
    text=
        safe_text
)
myDsl01_Bounds_strategy = st.builds(
    myDsl01_Bounds,
    height=
        st.integers(),
    y=
        st.integers(),
    x=
        st.integers(),
    width=
        st.integers()
)
myDsl01_Button_strategy = st.builds(
    myDsl01_Button,
    kind=
        safe_text,
    text=
        safe_text
)
myDsl01_Field_strategy = st.builds(
    myDsl01_Field,
)
myDsl01_Property_strategy = st.builds(
    myDsl01_Property,
    name=
        safe_text
)
myDsl01_Window_strategy = st.builds(
    myDsl01_Window,
    name=
        safe_text,
    title=
        safe_text
)
myDsl01_UIElement_strategy = st.builds(
    myDsl01_UIElement,
    name=
        safe_text
)
Window_strategy = st.builds(
    Window,
)
myDsl01_EntryWindow_strategy = st.builds(
    myDsl01_EntryWindow,
)
myDsl01_ListWindow_strategy = st.builds(
    myDsl01_ListWindow,
)
myDsl01_Size_strategy = st.builds(
    myDsl01_Size,
    width=
        st.integers(),
    height=
        st.integers()
)
Property_strategy = st.builds(
    Property,
)
myDsl01_Reference_strategy = st.builds(
    myDsl01_Reference,
    multiplicity=
        safe_text
)
myDsl01_Attribute_strategy = st.builds(
    myDsl01_Attribute,
    type=
        safe_text,
    optional=
        st.booleans()
)
myDsl01_Entity_strategy = st.builds(
    myDsl01_Entity,
    abstract=
        st.booleans(),
    name=
        safe_text
)
myDsl01_Model_strategy = st.builds(
    myDsl01_Model,
)

@given(instance=UIElement_strategy)
@settings(max_examples=50)
def test_uielement_instantiation(instance):
    assert isinstance(instance, UIElement)

@given(instance=myDsl01_Label_strategy)
@settings(max_examples=50)
def test_mydsl01_label_instantiation(instance):
    assert isinstance(instance, myDsl01_Label)



@given(instance=myDsl01_Label_strategy)
def test_mydsl01_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl01_Bounds_strategy)
@settings(max_examples=50)
def test_mydsl01_bounds_instantiation(instance):
    assert isinstance(instance, myDsl01_Bounds)



@given(instance=myDsl01_Bounds_strategy)
def test_mydsl01_bounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=myDsl01_Bounds_strategy)
def test_mydsl01_bounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=myDsl01_Bounds_strategy)
def test_mydsl01_bounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=myDsl01_Bounds_strategy)
def test_mydsl01_bounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=myDsl01_Button_strategy)
@settings(max_examples=50)
def test_mydsl01_button_instantiation(instance):
    assert isinstance(instance, myDsl01_Button)



@given(instance=myDsl01_Button_strategy)
def test_mydsl01_button_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=myDsl01_Button_strategy)
def test_mydsl01_button_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=myDsl01_Field_strategy)
@settings(max_examples=50)
def test_mydsl01_field_instantiation(instance):
    assert isinstance(instance, myDsl01_Field)

@given(instance=myDsl01_Property_strategy)
@settings(max_examples=50)
def test_mydsl01_property_instantiation(instance):
    assert isinstance(instance, myDsl01_Property)



@given(instance=myDsl01_Property_strategy)
def test_mydsl01_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl01_Window_strategy)
@settings(max_examples=50)
def test_mydsl01_window_instantiation(instance):
    assert isinstance(instance, myDsl01_Window)



@given(instance=myDsl01_Window_strategy)
def test_mydsl01_window_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl01_Window_strategy)
def test_mydsl01_window_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=myDsl01_UIElement_strategy)
@settings(max_examples=50)
def test_mydsl01_uielement_instantiation(instance):
    assert isinstance(instance, myDsl01_UIElement)



@given(instance=myDsl01_UIElement_strategy)
def test_mydsl01_uielement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Window_strategy)
@settings(max_examples=50)
def test_window_instantiation(instance):
    assert isinstance(instance, Window)

@given(instance=myDsl01_EntryWindow_strategy)
@settings(max_examples=50)
def test_mydsl01_entrywindow_instantiation(instance):
    assert isinstance(instance, myDsl01_EntryWindow)

@given(instance=myDsl01_ListWindow_strategy)
@settings(max_examples=50)
def test_mydsl01_listwindow_instantiation(instance):
    assert isinstance(instance, myDsl01_ListWindow)

@given(instance=myDsl01_Size_strategy)
@settings(max_examples=50)
def test_mydsl01_size_instantiation(instance):
    assert isinstance(instance, myDsl01_Size)



@given(instance=myDsl01_Size_strategy)
def test_mydsl01_size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=myDsl01_Size_strategy)
def test_mydsl01_size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=myDsl01_Reference_strategy)
@settings(max_examples=50)
def test_mydsl01_reference_instantiation(instance):
    assert isinstance(instance, myDsl01_Reference)



@given(instance=myDsl01_Reference_strategy)
def test_mydsl01_reference_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=myDsl01_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl01_attribute_instantiation(instance):
    assert isinstance(instance, myDsl01_Attribute)



@given(instance=myDsl01_Attribute_strategy)
def test_mydsl01_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=myDsl01_Attribute_strategy)
def test_mydsl01_attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=myDsl01_Entity_strategy)
@settings(max_examples=50)
def test_mydsl01_entity_instantiation(instance):
    assert isinstance(instance, myDsl01_Entity)



@given(instance=myDsl01_Entity_strategy)
def test_mydsl01_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=myDsl01_Entity_strategy)
def test_mydsl01_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl01_Model_strategy)
@settings(max_examples=50)
def test_mydsl01_model_instantiation(instance):
    assert isinstance(instance, myDsl01_Model)

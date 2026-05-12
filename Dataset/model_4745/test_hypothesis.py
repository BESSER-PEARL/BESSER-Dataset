import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sWML_Attribute,
    sWML_Class,
    sWML_IndexPage,
    sWML_ContentLayer,
    sWML_HypertextLayer,
    sWML_WebModel,
    SWMLTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_swml_attribute_is_not_abstract():
    assert not inspect.isabstract(sWML_Attribute)


def test_swml_attribute_constructor_exists():
    assert callable(sWML_Attribute.__init__)


def test_swml_attribute_constructor_args():
    sig = inspect.signature(sWML_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_swml_attribute_has_name():
    assert hasattr(sWML_Attribute, "name")
    descriptor = None
    for klass in sWML_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml_attribute_has_type():
    assert hasattr(sWML_Attribute, "type")
    descriptor = None
    for klass in sWML_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_swml_class_is_not_abstract():
    assert not inspect.isabstract(sWML_Class)


def test_swml_class_constructor_exists():
    assert callable(sWML_Class.__init__)


def test_swml_class_constructor_args():
    sig = inspect.signature(sWML_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_class_has_name():
    assert hasattr(sWML_Class, "name")
    descriptor = None
    for klass in sWML_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml_indexpage_is_not_abstract():
    assert not inspect.isabstract(sWML_IndexPage)


def test_swml_indexpage_constructor_exists():
    assert callable(sWML_IndexPage.__init__)


def test_swml_indexpage_constructor_args():
    sig = inspect.signature(sWML_IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"

def test_swml_indexpage_has_name():
    assert hasattr(sWML_IndexPage, "name")
    descriptor = None
    for klass in sWML_IndexPage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml_indexpage_has_size():
    assert hasattr(sWML_IndexPage, "size")
    descriptor = None
    for klass in sWML_IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_swml_contentlayer_is_not_abstract():
    assert not inspect.isabstract(sWML_ContentLayer)


def test_swml_contentlayer_constructor_exists():
    assert callable(sWML_ContentLayer.__init__)


def test_swml_contentlayer_constructor_args():
    sig = inspect.signature(sWML_ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_hypertextlayer_is_not_abstract():
    assert not inspect.isabstract(sWML_HypertextLayer)


def test_swml_hypertextlayer_constructor_exists():
    assert callable(sWML_HypertextLayer.__init__)


def test_swml_hypertextlayer_constructor_args():
    sig = inspect.signature(sWML_HypertextLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_webmodel_is_not_abstract():
    assert not inspect.isabstract(sWML_WebModel)


def test_swml_webmodel_constructor_exists():
    assert callable(sWML_WebModel.__init__)


def test_swml_webmodel_constructor_args():
    sig = inspect.signature(sWML_WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_webmodel_has_name():
    assert hasattr(sWML_WebModel, "name")
    descriptor = None
    for klass in sWML_WebModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swmltypes_exists():
    # Check that the Enumeration exists
    assert SWMLTypes is not None

def test_swmltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SWMLTypes]
    expected_literals = [
        "Boolean",
        "Float",
        "String",
        "Email",
        "Integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SWMLTypes"


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
sWML_Attribute_strategy = st.builds(
    sWML_Attribute,
    name=
        safe_text,
    type=
        safe_text
)
sWML_Class_strategy = st.builds(
    sWML_Class,
    name=
        safe_text
)
sWML_IndexPage_strategy = st.builds(
    sWML_IndexPage,
    name=
        safe_text,
    size=
        st.integers()
)
sWML_ContentLayer_strategy = st.builds(
    sWML_ContentLayer,
)
sWML_HypertextLayer_strategy = st.builds(
    sWML_HypertextLayer,
)
sWML_WebModel_strategy = st.builds(
    sWML_WebModel,
    name=
        safe_text
)

@given(instance=sWML_Attribute_strategy)
@settings(max_examples=50)
def test_swml_attribute_instantiation(instance):
    assert isinstance(instance, sWML_Attribute)



@given(instance=sWML_Attribute_strategy)
def test_swml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sWML_Attribute_strategy)
def test_swml_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sWML_Class_strategy)
@settings(max_examples=50)
def test_swml_class_instantiation(instance):
    assert isinstance(instance, sWML_Class)



@given(instance=sWML_Class_strategy)
def test_swml_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sWML_IndexPage_strategy)
@settings(max_examples=50)
def test_swml_indexpage_instantiation(instance):
    assert isinstance(instance, sWML_IndexPage)



@given(instance=sWML_IndexPage_strategy)
def test_swml_indexpage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sWML_IndexPage_strategy)
def test_swml_indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=sWML_ContentLayer_strategy)
@settings(max_examples=50)
def test_swml_contentlayer_instantiation(instance):
    assert isinstance(instance, sWML_ContentLayer)

@given(instance=sWML_HypertextLayer_strategy)
@settings(max_examples=50)
def test_swml_hypertextlayer_instantiation(instance):
    assert isinstance(instance, sWML_HypertextLayer)

@given(instance=sWML_WebModel_strategy)
@settings(max_examples=50)
def test_swml_webmodel_instantiation(instance):
    assert isinstance(instance, sWML_WebModel)



@given(instance=sWML_WebModel_strategy)
def test_swml_webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

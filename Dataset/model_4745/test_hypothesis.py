import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sWML::Attribute,
    sWML::Class,
    sWML::IndexPage,
    sWML::ContentLayer,
    sWML::HypertextLayer,
    sWML::WebModel,
    SWMLTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_swml::attribute_is_not_abstract():
    assert not inspect.isabstract(sWML::Attribute)


def test_swml::attribute_constructor_exists():
    assert callable(sWML::Attribute.__init__)


def test_swml::attribute_constructor_args():
    sig = inspect.signature(sWML::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_swml::attribute_has_type():
    assert hasattr(sWML::Attribute, "type")
    descriptor = None
    for klass in sWML::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_swml::attribute_has_name():
    assert hasattr(sWML::Attribute, "name")
    descriptor = None
    for klass in sWML::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::class_is_not_abstract():
    assert not inspect.isabstract(sWML::Class)


def test_swml::class_constructor_exists():
    assert callable(sWML::Class.__init__)


def test_swml::class_constructor_args():
    sig = inspect.signature(sWML::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::class_has_name():
    assert hasattr(sWML::Class, "name")
    descriptor = None
    for klass in sWML::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::indexpage_is_not_abstract():
    assert not inspect.isabstract(sWML::IndexPage)


def test_swml::indexpage_constructor_exists():
    assert callable(sWML::IndexPage.__init__)


def test_swml::indexpage_constructor_args():
    sig = inspect.signature(sWML::IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "name" in params, "Missing parameter 'name'"

def test_swml::indexpage_has_size():
    assert hasattr(sWML::IndexPage, "size")
    descriptor = None
    for klass in sWML::IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_swml::indexpage_has_name():
    assert hasattr(sWML::IndexPage, "name")
    descriptor = None
    for klass in sWML::IndexPage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::contentlayer_is_not_abstract():
    assert not inspect.isabstract(sWML::ContentLayer)


def test_swml::contentlayer_constructor_exists():
    assert callable(sWML::ContentLayer.__init__)


def test_swml::contentlayer_constructor_args():
    sig = inspect.signature(sWML::ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::hypertextlayer_is_not_abstract():
    assert not inspect.isabstract(sWML::HypertextLayer)


def test_swml::hypertextlayer_constructor_exists():
    assert callable(sWML::HypertextLayer.__init__)


def test_swml::hypertextlayer_constructor_args():
    sig = inspect.signature(sWML::HypertextLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::webmodel_is_not_abstract():
    assert not inspect.isabstract(sWML::WebModel)


def test_swml::webmodel_constructor_exists():
    assert callable(sWML::WebModel.__init__)


def test_swml::webmodel_constructor_args():
    sig = inspect.signature(sWML::WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::webmodel_has_name():
    assert hasattr(sWML::WebModel, "name")
    descriptor = None
    for klass in sWML::WebModel.__mro__:
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
        "Integer",
        "Float",
        "String",
        "Email",
        "Boolean",
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
sWML::Attribute_strategy = st.builds(
    sWML::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
sWML::Class_strategy = st.builds(
    sWML::Class,
    name=
        safe_text
)
sWML::IndexPage_strategy = st.builds(
    sWML::IndexPage,
    size=
        st.integers(),
    name=
        safe_text
)
sWML::ContentLayer_strategy = st.builds(
    sWML::ContentLayer,
)
sWML::HypertextLayer_strategy = st.builds(
    sWML::HypertextLayer,
)
sWML::WebModel_strategy = st.builds(
    sWML::WebModel,
    name=
        safe_text
)

@given(instance=sWML::Attribute_strategy)
@settings(max_examples=50)
def test_swml::attribute_instantiation(instance):
    assert isinstance(instance, sWML::Attribute)

@given(instance=sWML::Attribute_strategy)
def test_swml::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sWML::Attribute_strategy)
def test_swml::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sWML::Attribute_strategy)
def test_swml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sWML::Attribute_strategy)
def test_swml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sWML::Class_strategy)
@settings(max_examples=50)
def test_swml::class_instantiation(instance):
    assert isinstance(instance, sWML::Class)

@given(instance=sWML::Class_strategy)
def test_swml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sWML::Class_strategy)
def test_swml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sWML::IndexPage_strategy)
@settings(max_examples=50)
def test_swml::indexpage_instantiation(instance):
    assert isinstance(instance, sWML::IndexPage)

@given(instance=sWML::IndexPage_strategy)
def test_swml::indexpage_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=sWML::IndexPage_strategy)
def test_swml::indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=sWML::IndexPage_strategy)
def test_swml::indexpage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sWML::IndexPage_strategy)
def test_swml::indexpage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sWML::ContentLayer_strategy)
@settings(max_examples=50)
def test_swml::contentlayer_instantiation(instance):
    assert isinstance(instance, sWML::ContentLayer)

@given(instance=sWML::HypertextLayer_strategy)
@settings(max_examples=50)
def test_swml::hypertextlayer_instantiation(instance):
    assert isinstance(instance, sWML::HypertextLayer)

@given(instance=sWML::WebModel_strategy)
@settings(max_examples=50)
def test_swml::webmodel_instantiation(instance):
    assert isinstance(instance, sWML::WebModel)

@given(instance=sWML::WebModel_strategy)
def test_swml::webmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sWML::WebModel_strategy)
def test_swml::webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

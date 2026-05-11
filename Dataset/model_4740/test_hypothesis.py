import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    swml::Attribute,
    swml::Class,
    Link,
    swml::CLink,
    swml::NCLink,
    Page,
    swml::StaticPage,
    swml::DynamicPage,
    DynamicPage,
    swml::DetailsPage,
    swml::IndexPage,
    swml::Link,
    swml::Page,
    swml::ContentLayer,
    swml::HypertextLayer,
    swml::WebModel,
    SWMLTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_swml::attribute_is_not_abstract():
    assert not inspect.isabstract(swml::Attribute)


def test_swml::attribute_constructor_exists():
    assert callable(swml::Attribute.__init__)


def test_swml::attribute_constructor_args():
    sig = inspect.signature(swml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_swml::attribute_has_type():
    assert hasattr(swml::Attribute, "type")
    descriptor = None
    for klass in swml::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_swml::attribute_has_name():
    assert hasattr(swml::Attribute, "name")
    descriptor = None
    for klass in swml::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::class_is_not_abstract():
    assert not inspect.isabstract(swml::Class)


def test_swml::class_constructor_exists():
    assert callable(swml::Class.__init__)


def test_swml::class_constructor_args():
    sig = inspect.signature(swml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::class_has_name():
    assert hasattr(swml::Class, "name")
    descriptor = None
    for klass in swml::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_swml::clink_is_not_abstract():
    assert not inspect.isabstract(swml::CLink)


def test_swml::clink_constructor_exists():
    assert callable(swml::CLink.__init__)


def test_swml::clink_constructor_args():
    sig = inspect.signature(swml::CLink.__init__)
    params = list(sig.parameters.keys())



def test_swml::nclink_is_not_abstract():
    assert not inspect.isabstract(swml::NCLink)


def test_swml::nclink_constructor_exists():
    assert callable(swml::NCLink.__init__)


def test_swml::nclink_constructor_args():
    sig = inspect.signature(swml::NCLink.__init__)
    params = list(sig.parameters.keys())



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_swml::staticpage_is_not_abstract():
    assert not inspect.isabstract(swml::StaticPage)


def test_swml::staticpage_constructor_exists():
    assert callable(swml::StaticPage.__init__)


def test_swml::staticpage_constructor_args():
    sig = inspect.signature(swml::StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::dynamicpage_is_not_abstract():
    assert not inspect.isabstract(swml::DynamicPage)


def test_swml::dynamicpage_constructor_exists():
    assert callable(swml::DynamicPage.__init__)


def test_swml::dynamicpage_constructor_args():
    sig = inspect.signature(swml::DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::detailspage_is_not_abstract():
    assert not inspect.isabstract(swml::DetailsPage)


def test_swml::detailspage_constructor_exists():
    assert callable(swml::DetailsPage.__init__)


def test_swml::detailspage_constructor_args():
    sig = inspect.signature(swml::DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::indexpage_is_not_abstract():
    assert not inspect.isabstract(swml::IndexPage)


def test_swml::indexpage_constructor_exists():
    assert callable(swml::IndexPage.__init__)


def test_swml::indexpage_constructor_args():
    sig = inspect.signature(swml::IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_swml::indexpage_has_size():
    assert hasattr(swml::IndexPage, "size")
    descriptor = None
    for klass in swml::IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_swml::link_is_not_abstract():
    assert not inspect.isabstract(swml::Link)


def test_swml::link_constructor_exists():
    assert callable(swml::Link.__init__)


def test_swml::link_constructor_args():
    sig = inspect.signature(swml::Link.__init__)
    params = list(sig.parameters.keys())



def test_swml::page_is_not_abstract():
    assert not inspect.isabstract(swml::Page)


def test_swml::page_constructor_exists():
    assert callable(swml::Page.__init__)


def test_swml::page_constructor_args():
    sig = inspect.signature(swml::Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::page_has_name():
    assert hasattr(swml::Page, "name")
    descriptor = None
    for klass in swml::Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::contentlayer_is_not_abstract():
    assert not inspect.isabstract(swml::ContentLayer)


def test_swml::contentlayer_constructor_exists():
    assert callable(swml::ContentLayer.__init__)


def test_swml::contentlayer_constructor_args():
    sig = inspect.signature(swml::ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::hypertextlayer_is_not_abstract():
    assert not inspect.isabstract(swml::HypertextLayer)


def test_swml::hypertextlayer_constructor_exists():
    assert callable(swml::HypertextLayer.__init__)


def test_swml::hypertextlayer_constructor_args():
    sig = inspect.signature(swml::HypertextLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::webmodel_is_not_abstract():
    assert not inspect.isabstract(swml::WebModel)


def test_swml::webmodel_constructor_exists():
    assert callable(swml::WebModel.__init__)


def test_swml::webmodel_constructor_args():
    sig = inspect.signature(swml::WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::webmodel_has_name():
    assert hasattr(swml::WebModel, "name")
    descriptor = None
    for klass in swml::WebModel.__mro__:
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
        "Boolean",
        "Email",
        "Float",
        "String",
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
swml::Attribute_strategy = st.builds(
    swml::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
swml::Class_strategy = st.builds(
    swml::Class,
    name=
        safe_text
)
Link_strategy = st.builds(
    Link,
)
swml::CLink_strategy = st.builds(
    swml::CLink,
)
swml::NCLink_strategy = st.builds(
    swml::NCLink,
)
Page_strategy = st.builds(
    Page,
)
swml::StaticPage_strategy = st.builds(
    swml::StaticPage,
)
swml::DynamicPage_strategy = st.builds(
    swml::DynamicPage,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
swml::DetailsPage_strategy = st.builds(
    swml::DetailsPage,
)
swml::IndexPage_strategy = st.builds(
    swml::IndexPage,
    size=
        st.integers()
)
swml::Link_strategy = st.builds(
    swml::Link,
)
swml::Page_strategy = st.builds(
    swml::Page,
    name=
        safe_text
)
swml::ContentLayer_strategy = st.builds(
    swml::ContentLayer,
)
swml::HypertextLayer_strategy = st.builds(
    swml::HypertextLayer,
)
swml::WebModel_strategy = st.builds(
    swml::WebModel,
    name=
        safe_text
)

@given(instance=swml::Attribute_strategy)
@settings(max_examples=50)
def test_swml::attribute_instantiation(instance):
    assert isinstance(instance, swml::Attribute)

@given(instance=swml::Attribute_strategy)
def test_swml::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=swml::Attribute_strategy)
def test_swml::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=swml::Attribute_strategy)
def test_swml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::Attribute_strategy)
def test_swml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::Class_strategy)
@settings(max_examples=50)
def test_swml::class_instantiation(instance):
    assert isinstance(instance, swml::Class)

@given(instance=swml::Class_strategy)
def test_swml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::Class_strategy)
def test_swml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=swml::CLink_strategy)
@settings(max_examples=50)
def test_swml::clink_instantiation(instance):
    assert isinstance(instance, swml::CLink)

@given(instance=swml::NCLink_strategy)
@settings(max_examples=50)
def test_swml::nclink_instantiation(instance):
    assert isinstance(instance, swml::NCLink)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=swml::StaticPage_strategy)
@settings(max_examples=50)
def test_swml::staticpage_instantiation(instance):
    assert isinstance(instance, swml::StaticPage)

@given(instance=swml::DynamicPage_strategy)
@settings(max_examples=50)
def test_swml::dynamicpage_instantiation(instance):
    assert isinstance(instance, swml::DynamicPage)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=swml::DetailsPage_strategy)
@settings(max_examples=50)
def test_swml::detailspage_instantiation(instance):
    assert isinstance(instance, swml::DetailsPage)

@given(instance=swml::IndexPage_strategy)
@settings(max_examples=50)
def test_swml::indexpage_instantiation(instance):
    assert isinstance(instance, swml::IndexPage)

@given(instance=swml::IndexPage_strategy)
def test_swml::indexpage_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=swml::IndexPage_strategy)
def test_swml::indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=swml::Link_strategy)
@settings(max_examples=50)
def test_swml::link_instantiation(instance):
    assert isinstance(instance, swml::Link)

@given(instance=swml::Page_strategy)
@settings(max_examples=50)
def test_swml::page_instantiation(instance):
    assert isinstance(instance, swml::Page)

@given(instance=swml::Page_strategy)
def test_swml::page_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::Page_strategy)
def test_swml::page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::ContentLayer_strategy)
@settings(max_examples=50)
def test_swml::contentlayer_instantiation(instance):
    assert isinstance(instance, swml::ContentLayer)

@given(instance=swml::HypertextLayer_strategy)
@settings(max_examples=50)
def test_swml::hypertextlayer_instantiation(instance):
    assert isinstance(instance, swml::HypertextLayer)

@given(instance=swml::WebModel_strategy)
@settings(max_examples=50)
def test_swml::webmodel_instantiation(instance):
    assert isinstance(instance, swml::WebModel)

@given(instance=swml::WebModel_strategy)
def test_swml::webmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::WebModel_strategy)
def test_swml::webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

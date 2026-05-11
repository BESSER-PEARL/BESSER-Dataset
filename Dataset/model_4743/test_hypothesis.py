import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    swml::v2::Attribute,
    swml::v2::Class,
    swml::v2::ContentLayer,
    swml::v2::NavigationLayer,
    swml::v2::WebModel,
    swml::v2::Page,
    Page,
    swml::v2::DynamicPage,
    DynamicPage,
    swml::v2::DetailsPage,
    swml::v2::IndexPage,
    swml::v2::Link,
    Link,
    swml::v2::CLink,
    swml::v2::NCLink,
    swml::v2::StaticPage,
    SWMLTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_swml::v2::attribute_is_not_abstract():
    assert not inspect.isabstract(swml::v2::Attribute)


def test_swml::v2::attribute_constructor_exists():
    assert callable(swml::v2::Attribute.__init__)


def test_swml::v2::attribute_constructor_args():
    sig = inspect.signature(swml::v2::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_swml::v2::attribute_has_name():
    assert hasattr(swml::v2::Attribute, "name")
    descriptor = None
    for klass in swml::v2::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml::v2::attribute_has_type():
    assert hasattr(swml::v2::Attribute, "type")
    descriptor = None
    for klass in swml::v2::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_swml::v2::class_is_not_abstract():
    assert not inspect.isabstract(swml::v2::Class)


def test_swml::v2::class_constructor_exists():
    assert callable(swml::v2::Class.__init__)


def test_swml::v2::class_constructor_args():
    sig = inspect.signature(swml::v2::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::v2::class_has_name():
    assert hasattr(swml::v2::Class, "name")
    descriptor = None
    for klass in swml::v2::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::v2::contentlayer_is_not_abstract():
    assert not inspect.isabstract(swml::v2::ContentLayer)


def test_swml::v2::contentlayer_constructor_exists():
    assert callable(swml::v2::ContentLayer.__init__)


def test_swml::v2::contentlayer_constructor_args():
    sig = inspect.signature(swml::v2::ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::navigationlayer_is_not_abstract():
    assert not inspect.isabstract(swml::v2::NavigationLayer)


def test_swml::v2::navigationlayer_constructor_exists():
    assert callable(swml::v2::NavigationLayer.__init__)


def test_swml::v2::navigationlayer_constructor_args():
    sig = inspect.signature(swml::v2::NavigationLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::webmodel_is_not_abstract():
    assert not inspect.isabstract(swml::v2::WebModel)


def test_swml::v2::webmodel_constructor_exists():
    assert callable(swml::v2::WebModel.__init__)


def test_swml::v2::webmodel_constructor_args():
    sig = inspect.signature(swml::v2::WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::v2::webmodel_has_name():
    assert hasattr(swml::v2::WebModel, "name")
    descriptor = None
    for klass in swml::v2::WebModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::v2::page_is_not_abstract():
    assert not inspect.isabstract(swml::v2::Page)


def test_swml::v2::page_constructor_exists():
    assert callable(swml::v2::Page.__init__)


def test_swml::v2::page_constructor_args():
    sig = inspect.signature(swml::v2::Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::v2::page_has_name():
    assert hasattr(swml::v2::Page, "name")
    descriptor = None
    for klass in swml::v2::Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::dynamicpage_is_not_abstract():
    assert not inspect.isabstract(swml::v2::DynamicPage)


def test_swml::v2::dynamicpage_constructor_exists():
    assert callable(swml::v2::DynamicPage.__init__)


def test_swml::v2::dynamicpage_constructor_args():
    sig = inspect.signature(swml::v2::DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::detailspage_is_not_abstract():
    assert not inspect.isabstract(swml::v2::DetailsPage)


def test_swml::v2::detailspage_constructor_exists():
    assert callable(swml::v2::DetailsPage.__init__)


def test_swml::v2::detailspage_constructor_args():
    sig = inspect.signature(swml::v2::DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::indexpage_is_not_abstract():
    assert not inspect.isabstract(swml::v2::IndexPage)


def test_swml::v2::indexpage_constructor_exists():
    assert callable(swml::v2::IndexPage.__init__)


def test_swml::v2::indexpage_constructor_args():
    sig = inspect.signature(swml::v2::IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_swml::v2::indexpage_has_size():
    assert hasattr(swml::v2::IndexPage, "size")
    descriptor = None
    for klass in swml::v2::IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_swml::v2::link_is_not_abstract():
    assert not inspect.isabstract(swml::v2::Link)


def test_swml::v2::link_constructor_exists():
    assert callable(swml::v2::Link.__init__)


def test_swml::v2::link_constructor_args():
    sig = inspect.signature(swml::v2::Link.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::clink_is_not_abstract():
    assert not inspect.isabstract(swml::v2::CLink)


def test_swml::v2::clink_constructor_exists():
    assert callable(swml::v2::CLink.__init__)


def test_swml::v2::clink_constructor_args():
    sig = inspect.signature(swml::v2::CLink.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::nclink_is_not_abstract():
    assert not inspect.isabstract(swml::v2::NCLink)


def test_swml::v2::nclink_constructor_exists():
    assert callable(swml::v2::NCLink.__init__)


def test_swml::v2::nclink_constructor_args():
    sig = inspect.signature(swml::v2::NCLink.__init__)
    params = list(sig.parameters.keys())



def test_swml::v2::staticpage_is_not_abstract():
    assert not inspect.isabstract(swml::v2::StaticPage)


def test_swml::v2::staticpage_constructor_exists():
    assert callable(swml::v2::StaticPage.__init__)


def test_swml::v2::staticpage_constructor_args():
    sig = inspect.signature(swml::v2::StaticPage.__init__)
    params = list(sig.parameters.keys())

def test_swmltypes_exists():
    # Check that the Enumeration exists
    assert SWMLTypes is not None

def test_swmltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SWMLTypes]
    expected_literals = [
        "Boolean",
        "Integer",
        "Email",
        "String",
        "Float",
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
swml::v2::Attribute_strategy = st.builds(
    swml::v2::Attribute,
    name=
        safe_text,
    type=
        safe_text
)
swml::v2::Class_strategy = st.builds(
    swml::v2::Class,
    name=
        safe_text
)
swml::v2::ContentLayer_strategy = st.builds(
    swml::v2::ContentLayer,
)
swml::v2::NavigationLayer_strategy = st.builds(
    swml::v2::NavigationLayer,
)
swml::v2::WebModel_strategy = st.builds(
    swml::v2::WebModel,
    name=
        safe_text
)
swml::v2::Page_strategy = st.builds(
    swml::v2::Page,
    name=
        safe_text
)
Page_strategy = st.builds(
    Page,
)
swml::v2::DynamicPage_strategy = st.builds(
    swml::v2::DynamicPage,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
swml::v2::DetailsPage_strategy = st.builds(
    swml::v2::DetailsPage,
)
swml::v2::IndexPage_strategy = st.builds(
    swml::v2::IndexPage,
    size=
        st.integers()
)
swml::v2::Link_strategy = st.builds(
    swml::v2::Link,
)
Link_strategy = st.builds(
    Link,
)
swml::v2::CLink_strategy = st.builds(
    swml::v2::CLink,
)
swml::v2::NCLink_strategy = st.builds(
    swml::v2::NCLink,
)
swml::v2::StaticPage_strategy = st.builds(
    swml::v2::StaticPage,
)

@given(instance=swml::v2::Attribute_strategy)
@settings(max_examples=50)
def test_swml::v2::attribute_instantiation(instance):
    assert isinstance(instance, swml::v2::Attribute)

@given(instance=swml::v2::Attribute_strategy)
def test_swml::v2::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::v2::Attribute_strategy)
def test_swml::v2::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::v2::Attribute_strategy)
def test_swml::v2::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=swml::v2::Attribute_strategy)
def test_swml::v2::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=swml::v2::Class_strategy)
@settings(max_examples=50)
def test_swml::v2::class_instantiation(instance):
    assert isinstance(instance, swml::v2::Class)

@given(instance=swml::v2::Class_strategy)
def test_swml::v2::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::v2::Class_strategy)
def test_swml::v2::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::v2::ContentLayer_strategy)
@settings(max_examples=50)
def test_swml::v2::contentlayer_instantiation(instance):
    assert isinstance(instance, swml::v2::ContentLayer)

@given(instance=swml::v2::NavigationLayer_strategy)
@settings(max_examples=50)
def test_swml::v2::navigationlayer_instantiation(instance):
    assert isinstance(instance, swml::v2::NavigationLayer)

@given(instance=swml::v2::WebModel_strategy)
@settings(max_examples=50)
def test_swml::v2::webmodel_instantiation(instance):
    assert isinstance(instance, swml::v2::WebModel)

@given(instance=swml::v2::WebModel_strategy)
def test_swml::v2::webmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::v2::WebModel_strategy)
def test_swml::v2::webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::v2::Page_strategy)
@settings(max_examples=50)
def test_swml::v2::page_instantiation(instance):
    assert isinstance(instance, swml::v2::Page)

@given(instance=swml::v2::Page_strategy)
def test_swml::v2::page_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::v2::Page_strategy)
def test_swml::v2::page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=swml::v2::DynamicPage_strategy)
@settings(max_examples=50)
def test_swml::v2::dynamicpage_instantiation(instance):
    assert isinstance(instance, swml::v2::DynamicPage)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=swml::v2::DetailsPage_strategy)
@settings(max_examples=50)
def test_swml::v2::detailspage_instantiation(instance):
    assert isinstance(instance, swml::v2::DetailsPage)

@given(instance=swml::v2::IndexPage_strategy)
@settings(max_examples=50)
def test_swml::v2::indexpage_instantiation(instance):
    assert isinstance(instance, swml::v2::IndexPage)

@given(instance=swml::v2::IndexPage_strategy)
def test_swml::v2::indexpage_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=swml::v2::IndexPage_strategy)
def test_swml::v2::indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=swml::v2::Link_strategy)
@settings(max_examples=50)
def test_swml::v2::link_instantiation(instance):
    assert isinstance(instance, swml::v2::Link)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=swml::v2::CLink_strategy)
@settings(max_examples=50)
def test_swml::v2::clink_instantiation(instance):
    assert isinstance(instance, swml::v2::CLink)

@given(instance=swml::v2::NCLink_strategy)
@settings(max_examples=50)
def test_swml::v2::nclink_instantiation(instance):
    assert isinstance(instance, swml::v2::NCLink)

@given(instance=swml::v2::StaticPage_strategy)
@settings(max_examples=50)
def test_swml::v2::staticpage_instantiation(instance):
    assert isinstance(instance, swml::v2::StaticPage)

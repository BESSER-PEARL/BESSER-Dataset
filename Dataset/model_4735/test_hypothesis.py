import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DynamicPage,
    swml::IndexPage,
    swml::EntityPage,
    swml::Icon,
    swml::Link,
    WebPage,
    swml::DynamicPage,
    swml::WebPage,
    swml::Relationship,
    swml::Attribute,
    swml::StaticPage,
    swml::Entity,
    swml::WebApplication,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::indexpage_is_not_abstract():
    assert not inspect.isabstract(swml::IndexPage)


def test_swml::indexpage_constructor_exists():
    assert callable(swml::IndexPage.__init__)


def test_swml::indexpage_constructor_args():
    sig = inspect.signature(swml::IndexPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::entitypage_is_not_abstract():
    assert not inspect.isabstract(swml::EntityPage)


def test_swml::entitypage_constructor_exists():
    assert callable(swml::EntityPage.__init__)


def test_swml::entitypage_constructor_args():
    sig = inspect.signature(swml::EntityPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::icon_is_not_abstract():
    assert not inspect.isabstract(swml::Icon)


def test_swml::icon_constructor_exists():
    assert callable(swml::Icon.__init__)


def test_swml::icon_constructor_args():
    sig = inspect.signature(swml::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_swml::icon_has_image():
    assert hasattr(swml::Icon, "image")
    descriptor = None
    for klass in swml::Icon.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_swml::link_is_not_abstract():
    assert not inspect.isabstract(swml::Link)


def test_swml::link_constructor_exists():
    assert callable(swml::Link.__init__)


def test_swml::link_constructor_args():
    sig = inspect.signature(swml::Link.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"

def test_swml::link_has_href():
    assert hasattr(swml::Link, "href")
    descriptor = None
    for klass in swml::Link.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_webpage_is_not_abstract():
    assert not inspect.isabstract(WebPage)


def test_webpage_constructor_exists():
    assert callable(WebPage.__init__)


def test_webpage_constructor_args():
    sig = inspect.signature(WebPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::dynamicpage_is_not_abstract():
    assert not inspect.isabstract(swml::DynamicPage)


def test_swml::dynamicpage_constructor_exists():
    assert callable(swml::DynamicPage.__init__)


def test_swml::dynamicpage_constructor_args():
    sig = inspect.signature(swml::DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::webpage_is_not_abstract():
    assert not inspect.isabstract(swml::WebPage)


def test_swml::webpage_constructor_exists():
    assert callable(swml::WebPage.__init__)


def test_swml::webpage_constructor_args():
    sig = inspect.signature(swml::WebPage.__init__)
    params = list(sig.parameters.keys())
    assert "relativeUrl" in params, "Missing parameter 'relativeUrl'"
    assert "title" in params, "Missing parameter 'title'"

def test_swml::webpage_has_relativeUrl():
    assert hasattr(swml::WebPage, "relativeUrl")
    descriptor = None
    for klass in swml::WebPage.__mro__:
        if "relativeUrl" in klass.__dict__:
            descriptor = klass.__dict__["relativeUrl"]
            break
    assert isinstance(descriptor, property)

def test_swml::webpage_has_title():
    assert hasattr(swml::WebPage, "title")
    descriptor = None
    for klass in swml::WebPage.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_swml::relationship_is_not_abstract():
    assert not inspect.isabstract(swml::Relationship)


def test_swml::relationship_constructor_exists():
    assert callable(swml::Relationship.__init__)


def test_swml::relationship_constructor_args():
    sig = inspect.signature(swml::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "role" in params, "Missing parameter 'role'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_swml::relationship_has_upperBound():
    assert hasattr(swml::Relationship, "upperBound")
    descriptor = None
    for klass in swml::Relationship.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_swml::relationship_has_role():
    assert hasattr(swml::Relationship, "role")
    descriptor = None
    for klass in swml::Relationship.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_swml::relationship_has_lowerBound():
    assert hasattr(swml::Relationship, "lowerBound")
    descriptor = None
    for klass in swml::Relationship.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_swml::attribute_is_not_abstract():
    assert not inspect.isabstract(swml::Attribute)


def test_swml::attribute_constructor_exists():
    assert callable(swml::Attribute.__init__)


def test_swml::attribute_constructor_args():
    sig = inspect.signature(swml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_swml::attribute_has_name():
    assert hasattr(swml::Attribute, "name")
    descriptor = None
    for klass in swml::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml::attribute_has_dataType():
    assert hasattr(swml::Attribute, "dataType")
    descriptor = None
    for klass in swml::Attribute.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_swml::staticpage_is_not_abstract():
    assert not inspect.isabstract(swml::StaticPage)


def test_swml::staticpage_constructor_exists():
    assert callable(swml::StaticPage.__init__)


def test_swml::staticpage_constructor_args():
    sig = inspect.signature(swml::StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_swml::entity_is_not_abstract():
    assert not inspect.isabstract(swml::Entity)


def test_swml::entity_constructor_exists():
    assert callable(swml::Entity.__init__)


def test_swml::entity_constructor_args():
    sig = inspect.signature(swml::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::entity_has_name():
    assert hasattr(swml::Entity, "name")
    descriptor = None
    for klass in swml::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml::webapplication_is_not_abstract():
    assert not inspect.isabstract(swml::WebApplication)


def test_swml::webapplication_constructor_exists():
    assert callable(swml::WebApplication.__init__)


def test_swml::webapplication_constructor_args():
    sig = inspect.signature(swml::WebApplication.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml::webapplication_has_name():
    assert hasattr(swml::WebApplication, "name")
    descriptor = None
    for klass in swml::WebApplication.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Boolean",
        "Integer",
        "String",
        "Float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
DynamicPage_strategy = st.builds(
    DynamicPage,
)
swml::IndexPage_strategy = st.builds(
    swml::IndexPage,
)
swml::EntityPage_strategy = st.builds(
    swml::EntityPage,
)
swml::Icon_strategy = st.builds(
    swml::Icon,
    image=
        safe_text
)
swml::Link_strategy = st.builds(
    swml::Link,
    href=
        safe_text
)
WebPage_strategy = st.builds(
    WebPage,
)
swml::DynamicPage_strategy = st.builds(
    swml::DynamicPage,
)
swml::WebPage_strategy = st.builds(
    swml::WebPage,
    relativeUrl=
        safe_text,
    title=
        safe_text
)
swml::Relationship_strategy = st.builds(
    swml::Relationship,
    upperBound=
        st.integers(),
    role=
        safe_text,
    lowerBound=
        st.integers()
)
swml::Attribute_strategy = st.builds(
    swml::Attribute,
    name=
        safe_text,
    dataType=
        safe_text
)
swml::StaticPage_strategy = st.builds(
    swml::StaticPage,
)
swml::Entity_strategy = st.builds(
    swml::Entity,
    name=
        safe_text
)
swml::WebApplication_strategy = st.builds(
    swml::WebApplication,
    name=
        safe_text
)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=swml::IndexPage_strategy)
@settings(max_examples=50)
def test_swml::indexpage_instantiation(instance):
    assert isinstance(instance, swml::IndexPage)

@given(instance=swml::EntityPage_strategy)
@settings(max_examples=50)
def test_swml::entitypage_instantiation(instance):
    assert isinstance(instance, swml::EntityPage)

@given(instance=swml::Icon_strategy)
@settings(max_examples=50)
def test_swml::icon_instantiation(instance):
    assert isinstance(instance, swml::Icon)

@given(instance=swml::Icon_strategy)
def test_swml::icon_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=swml::Icon_strategy)
def test_swml::icon_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=swml::Link_strategy)
@settings(max_examples=50)
def test_swml::link_instantiation(instance):
    assert isinstance(instance, swml::Link)

@given(instance=swml::Link_strategy)
def test_swml::link_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=swml::Link_strategy)
def test_swml::link_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=WebPage_strategy)
@settings(max_examples=50)
def test_webpage_instantiation(instance):
    assert isinstance(instance, WebPage)

@given(instance=swml::DynamicPage_strategy)
@settings(max_examples=50)
def test_swml::dynamicpage_instantiation(instance):
    assert isinstance(instance, swml::DynamicPage)

@given(instance=swml::WebPage_strategy)
@settings(max_examples=50)
def test_swml::webpage_instantiation(instance):
    assert isinstance(instance, swml::WebPage)

@given(instance=swml::WebPage_strategy)
def test_swml::webpage_relativeUrl_type(instance):
    assert isinstance(instance.relativeUrl, str)


@given(instance=swml::WebPage_strategy)
def test_swml::webpage_relativeUrl_setter(instance):
    original = instance.relativeUrl
    instance.relativeUrl = original
    assert instance.relativeUrl == original

@given(instance=swml::WebPage_strategy)
def test_swml::webpage_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=swml::WebPage_strategy)
def test_swml::webpage_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=swml::Relationship_strategy)
@settings(max_examples=50)
def test_swml::relationship_instantiation(instance):
    assert isinstance(instance, swml::Relationship)

@given(instance=swml::Relationship_strategy)
def test_swml::relationship_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=swml::Relationship_strategy)
def test_swml::relationship_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=swml::Relationship_strategy)
def test_swml::relationship_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=swml::Relationship_strategy)
def test_swml::relationship_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=swml::Relationship_strategy)
def test_swml::relationship_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=swml::Relationship_strategy)
def test_swml::relationship_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=swml::Attribute_strategy)
@settings(max_examples=50)
def test_swml::attribute_instantiation(instance):
    assert isinstance(instance, swml::Attribute)

@given(instance=swml::Attribute_strategy)
def test_swml::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::Attribute_strategy)
def test_swml::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::Attribute_strategy)
def test_swml::attribute_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=swml::Attribute_strategy)
def test_swml::attribute_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=swml::StaticPage_strategy)
@settings(max_examples=50)
def test_swml::staticpage_instantiation(instance):
    assert isinstance(instance, swml::StaticPage)

@given(instance=swml::Entity_strategy)
@settings(max_examples=50)
def test_swml::entity_instantiation(instance):
    assert isinstance(instance, swml::Entity)

@given(instance=swml::Entity_strategy)
def test_swml::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::Entity_strategy)
def test_swml::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml::WebApplication_strategy)
@settings(max_examples=50)
def test_swml::webapplication_instantiation(instance):
    assert isinstance(instance, swml::WebApplication)

@given(instance=swml::WebApplication_strategy)
def test_swml::webapplication_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swml::WebApplication_strategy)
def test_swml::webapplication_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

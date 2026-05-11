import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wappm::Reference,
    wappm::Attribute,
    DynamicPage,
    wappm::IndexPage,
    wappm::DetailPage,
    wappm::WebClass,
    Page,
    wappm::DynamicPage,
    wappm::StaticPage,
    wappm::Link,
    wappm::Page,
    wappm::ContentLayer,
    wappm::HypertextLayer,
    wappm::WebModel,
    AppTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wappm::reference_is_not_abstract():
    assert not inspect.isabstract(wappm::Reference)


def test_wappm::reference_constructor_exists():
    assert callable(wappm::Reference.__init__)


def test_wappm::reference_constructor_args():
    sig = inspect.signature(wappm::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "lowBound" in params, "Missing parameter 'lowBound'"
    assert "upBound" in params, "Missing parameter 'upBound'"
    assert "name" in params, "Missing parameter 'name'"

def test_wappm::reference_has_lowBound():
    assert hasattr(wappm::Reference, "lowBound")
    descriptor = None
    for klass in wappm::Reference.__mro__:
        if "lowBound" in klass.__dict__:
            descriptor = klass.__dict__["lowBound"]
            break
    assert isinstance(descriptor, property)

def test_wappm::reference_has_upBound():
    assert hasattr(wappm::Reference, "upBound")
    descriptor = None
    for klass in wappm::Reference.__mro__:
        if "upBound" in klass.__dict__:
            descriptor = klass.__dict__["upBound"]
            break
    assert isinstance(descriptor, property)

def test_wappm::reference_has_name():
    assert hasattr(wappm::Reference, "name")
    descriptor = None
    for klass in wappm::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wappm::attribute_is_not_abstract():
    assert not inspect.isabstract(wappm::Attribute)


def test_wappm::attribute_constructor_exists():
    assert callable(wappm::Attribute.__init__)


def test_wappm::attribute_constructor_args():
    sig = inspect.signature(wappm::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_wappm::attribute_has_type():
    assert hasattr(wappm::Attribute, "type")
    descriptor = None
    for klass in wappm::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_wappm::attribute_has_name():
    assert hasattr(wappm::Attribute, "name")
    descriptor = None
    for klass in wappm::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_wappm::indexpage_is_not_abstract():
    assert not inspect.isabstract(wappm::IndexPage)


def test_wappm::indexpage_constructor_exists():
    assert callable(wappm::IndexPage.__init__)


def test_wappm::indexpage_constructor_args():
    sig = inspect.signature(wappm::IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_wappm::indexpage_has_size():
    assert hasattr(wappm::IndexPage, "size")
    descriptor = None
    for klass in wappm::IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_wappm::detailpage_is_not_abstract():
    assert not inspect.isabstract(wappm::DetailPage)


def test_wappm::detailpage_constructor_exists():
    assert callable(wappm::DetailPage.__init__)


def test_wappm::detailpage_constructor_args():
    sig = inspect.signature(wappm::DetailPage.__init__)
    params = list(sig.parameters.keys())



def test_wappm::webclass_is_not_abstract():
    assert not inspect.isabstract(wappm::WebClass)


def test_wappm::webclass_constructor_exists():
    assert callable(wappm::WebClass.__init__)


def test_wappm::webclass_constructor_args():
    sig = inspect.signature(wappm::WebClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wappm::webclass_has_name():
    assert hasattr(wappm::WebClass, "name")
    descriptor = None
    for klass in wappm::WebClass.__mro__:
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



def test_wappm::dynamicpage_is_not_abstract():
    assert not inspect.isabstract(wappm::DynamicPage)


def test_wappm::dynamicpage_constructor_exists():
    assert callable(wappm::DynamicPage.__init__)


def test_wappm::dynamicpage_constructor_args():
    sig = inspect.signature(wappm::DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_wappm::staticpage_is_not_abstract():
    assert not inspect.isabstract(wappm::StaticPage)


def test_wappm::staticpage_constructor_exists():
    assert callable(wappm::StaticPage.__init__)


def test_wappm::staticpage_constructor_args():
    sig = inspect.signature(wappm::StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_wappm::link_is_not_abstract():
    assert not inspect.isabstract(wappm::Link)


def test_wappm::link_constructor_exists():
    assert callable(wappm::Link.__init__)


def test_wappm::link_constructor_args():
    sig = inspect.signature(wappm::Link.__init__)
    params = list(sig.parameters.keys())



def test_wappm::page_is_not_abstract():
    assert not inspect.isabstract(wappm::Page)


def test_wappm::page_constructor_exists():
    assert callable(wappm::Page.__init__)


def test_wappm::page_constructor_args():
    sig = inspect.signature(wappm::Page.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_wappm::page_has_path():
    assert hasattr(wappm::Page, "path")
    descriptor = None
    for klass in wappm::Page.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_wappm::page_has_name():
    assert hasattr(wappm::Page, "name")
    descriptor = None
    for klass in wappm::Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wappm::contentlayer_is_not_abstract():
    assert not inspect.isabstract(wappm::ContentLayer)


def test_wappm::contentlayer_constructor_exists():
    assert callable(wappm::ContentLayer.__init__)


def test_wappm::contentlayer_constructor_args():
    sig = inspect.signature(wappm::ContentLayer.__init__)
    params = list(sig.parameters.keys())
    assert "contentName" in params, "Missing parameter 'contentName'"

def test_wappm::contentlayer_has_contentName():
    assert hasattr(wappm::ContentLayer, "contentName")
    descriptor = None
    for klass in wappm::ContentLayer.__mro__:
        if "contentName" in klass.__dict__:
            descriptor = klass.__dict__["contentName"]
            break
    assert isinstance(descriptor, property)



def test_wappm::hypertextlayer_is_not_abstract():
    assert not inspect.isabstract(wappm::HypertextLayer)


def test_wappm::hypertextlayer_constructor_exists():
    assert callable(wappm::HypertextLayer.__init__)


def test_wappm::hypertextlayer_constructor_args():
    sig = inspect.signature(wappm::HypertextLayer.__init__)
    params = list(sig.parameters.keys())
    assert "hyperName" in params, "Missing parameter 'hyperName'"

def test_wappm::hypertextlayer_has_hyperName():
    assert hasattr(wappm::HypertextLayer, "hyperName")
    descriptor = None
    for klass in wappm::HypertextLayer.__mro__:
        if "hyperName" in klass.__dict__:
            descriptor = klass.__dict__["hyperName"]
            break
    assert isinstance(descriptor, property)



def test_wappm::webmodel_is_not_abstract():
    assert not inspect.isabstract(wappm::WebModel)


def test_wappm::webmodel_constructor_exists():
    assert callable(wappm::WebModel.__init__)


def test_wappm::webmodel_constructor_args():
    sig = inspect.signature(wappm::WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wappm::webmodel_has_name():
    assert hasattr(wappm::WebModel, "name")
    descriptor = None
    for klass in wappm::WebModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_apptypes_exists():
    # Check that the Enumeration exists
    assert AppTypes is not None

def test_apptypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AppTypes]
    expected_literals = [
        "String",
        "Double",
        "Integer",
        "Float",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AppTypes"


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
wappm::Reference_strategy = st.builds(
    wappm::Reference,
    lowBound=
        st.integers(),
    upBound=
        st.integers(),
    name=
        safe_text
)
wappm::Attribute_strategy = st.builds(
    wappm::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
wappm::IndexPage_strategy = st.builds(
    wappm::IndexPage,
    size=
        st.integers()
)
wappm::DetailPage_strategy = st.builds(
    wappm::DetailPage,
)
wappm::WebClass_strategy = st.builds(
    wappm::WebClass,
    name=
        safe_text
)
Page_strategy = st.builds(
    Page,
)
wappm::DynamicPage_strategy = st.builds(
    wappm::DynamicPage,
)
wappm::StaticPage_strategy = st.builds(
    wappm::StaticPage,
)
wappm::Link_strategy = st.builds(
    wappm::Link,
)
wappm::Page_strategy = st.builds(
    wappm::Page,
    path=
        safe_text,
    name=
        safe_text
)
wappm::ContentLayer_strategy = st.builds(
    wappm::ContentLayer,
    contentName=
        safe_text
)
wappm::HypertextLayer_strategy = st.builds(
    wappm::HypertextLayer,
    hyperName=
        safe_text
)
wappm::WebModel_strategy = st.builds(
    wappm::WebModel,
    name=
        safe_text
)

@given(instance=wappm::Reference_strategy)
@settings(max_examples=50)
def test_wappm::reference_instantiation(instance):
    assert isinstance(instance, wappm::Reference)

@given(instance=wappm::Reference_strategy)
def test_wappm::reference_lowBound_type(instance):
    assert isinstance(instance.lowBound, int)


@given(instance=wappm::Reference_strategy)
def test_wappm::reference_lowBound_setter(instance):
    original = instance.lowBound
    instance.lowBound = original
    assert instance.lowBound == original

@given(instance=wappm::Reference_strategy)
def test_wappm::reference_upBound_type(instance):
    assert isinstance(instance.upBound, int)


@given(instance=wappm::Reference_strategy)
def test_wappm::reference_upBound_setter(instance):
    original = instance.upBound
    instance.upBound = original
    assert instance.upBound == original

@given(instance=wappm::Reference_strategy)
def test_wappm::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wappm::Reference_strategy)
def test_wappm::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wappm::Attribute_strategy)
@settings(max_examples=50)
def test_wappm::attribute_instantiation(instance):
    assert isinstance(instance, wappm::Attribute)

@given(instance=wappm::Attribute_strategy)
def test_wappm::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=wappm::Attribute_strategy)
def test_wappm::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=wappm::Attribute_strategy)
def test_wappm::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wappm::Attribute_strategy)
def test_wappm::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=wappm::IndexPage_strategy)
@settings(max_examples=50)
def test_wappm::indexpage_instantiation(instance):
    assert isinstance(instance, wappm::IndexPage)

@given(instance=wappm::IndexPage_strategy)
def test_wappm::indexpage_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=wappm::IndexPage_strategy)
def test_wappm::indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=wappm::DetailPage_strategy)
@settings(max_examples=50)
def test_wappm::detailpage_instantiation(instance):
    assert isinstance(instance, wappm::DetailPage)

@given(instance=wappm::WebClass_strategy)
@settings(max_examples=50)
def test_wappm::webclass_instantiation(instance):
    assert isinstance(instance, wappm::WebClass)

@given(instance=wappm::WebClass_strategy)
def test_wappm::webclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wappm::WebClass_strategy)
def test_wappm::webclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=wappm::DynamicPage_strategy)
@settings(max_examples=50)
def test_wappm::dynamicpage_instantiation(instance):
    assert isinstance(instance, wappm::DynamicPage)

@given(instance=wappm::StaticPage_strategy)
@settings(max_examples=50)
def test_wappm::staticpage_instantiation(instance):
    assert isinstance(instance, wappm::StaticPage)

@given(instance=wappm::Link_strategy)
@settings(max_examples=50)
def test_wappm::link_instantiation(instance):
    assert isinstance(instance, wappm::Link)

@given(instance=wappm::Page_strategy)
@settings(max_examples=50)
def test_wappm::page_instantiation(instance):
    assert isinstance(instance, wappm::Page)

@given(instance=wappm::Page_strategy)
def test_wappm::page_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=wappm::Page_strategy)
def test_wappm::page_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=wappm::Page_strategy)
def test_wappm::page_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wappm::Page_strategy)
def test_wappm::page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wappm::ContentLayer_strategy)
@settings(max_examples=50)
def test_wappm::contentlayer_instantiation(instance):
    assert isinstance(instance, wappm::ContentLayer)

@given(instance=wappm::ContentLayer_strategy)
def test_wappm::contentlayer_contentName_type(instance):
    assert isinstance(instance.contentName, str)


@given(instance=wappm::ContentLayer_strategy)
def test_wappm::contentlayer_contentName_setter(instance):
    original = instance.contentName
    instance.contentName = original
    assert instance.contentName == original

@given(instance=wappm::HypertextLayer_strategy)
@settings(max_examples=50)
def test_wappm::hypertextlayer_instantiation(instance):
    assert isinstance(instance, wappm::HypertextLayer)

@given(instance=wappm::HypertextLayer_strategy)
def test_wappm::hypertextlayer_hyperName_type(instance):
    assert isinstance(instance.hyperName, str)


@given(instance=wappm::HypertextLayer_strategy)
def test_wappm::hypertextlayer_hyperName_setter(instance):
    original = instance.hyperName
    instance.hyperName = original
    assert instance.hyperName == original

@given(instance=wappm::WebModel_strategy)
@settings(max_examples=50)
def test_wappm::webmodel_instantiation(instance):
    assert isinstance(instance, wappm::WebModel)

@given(instance=wappm::WebModel_strategy)
def test_wappm::webmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wappm::WebModel_strategy)
def test_wappm::webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

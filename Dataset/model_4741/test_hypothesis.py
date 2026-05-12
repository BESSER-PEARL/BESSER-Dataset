import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Page,
    swml_DynamicPage,
    DynamicPage,
    swml_DetailsPage,
    swml_IndexPage,
    swml_Link,
    Link,
    swml_CLink,
    swml_NCLink,
    swml_StaticPage,
    swml_ContentLayer,
    swml_Attribute,
    swml_Class,
    swml_Page,
    swml_HypertextLayer,
    swml_WebModel,
    SWMLTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_swml_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(swml_DynamicPage)


def test_swml_dynamicpage_constructor_exists():
    assert callable(swml_DynamicPage.__init__)


def test_swml_dynamicpage_constructor_args():
    sig = inspect.signature(swml_DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_detailspage_is_not_abstract():
    assert not inspect.isabstract(swml_DetailsPage)


def test_swml_detailspage_constructor_exists():
    assert callable(swml_DetailsPage.__init__)


def test_swml_detailspage_constructor_args():
    sig = inspect.signature(swml_DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_indexpage_is_not_abstract():
    assert not inspect.isabstract(swml_IndexPage)


def test_swml_indexpage_constructor_exists():
    assert callable(swml_IndexPage.__init__)


def test_swml_indexpage_constructor_args():
    sig = inspect.signature(swml_IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_swml_indexpage_has_size():
    assert hasattr(swml_IndexPage, "size")
    descriptor = None
    for klass in swml_IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_swml_link_is_not_abstract():
    assert not inspect.isabstract(swml_Link)


def test_swml_link_constructor_exists():
    assert callable(swml_Link.__init__)


def test_swml_link_constructor_args():
    sig = inspect.signature(swml_Link.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_swml_clink_is_not_abstract():
    assert not inspect.isabstract(swml_CLink)


def test_swml_clink_constructor_exists():
    assert callable(swml_CLink.__init__)


def test_swml_clink_constructor_args():
    sig = inspect.signature(swml_CLink.__init__)
    params = list(sig.parameters.keys())



def test_swml_nclink_is_not_abstract():
    assert not inspect.isabstract(swml_NCLink)


def test_swml_nclink_constructor_exists():
    assert callable(swml_NCLink.__init__)


def test_swml_nclink_constructor_args():
    sig = inspect.signature(swml_NCLink.__init__)
    params = list(sig.parameters.keys())



def test_swml_staticpage_is_not_abstract():
    assert not inspect.isabstract(swml_StaticPage)


def test_swml_staticpage_constructor_exists():
    assert callable(swml_StaticPage.__init__)


def test_swml_staticpage_constructor_args():
    sig = inspect.signature(swml_StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_contentlayer_is_not_abstract():
    assert not inspect.isabstract(swml_ContentLayer)


def test_swml_contentlayer_constructor_exists():
    assert callable(swml_ContentLayer.__init__)


def test_swml_contentlayer_constructor_args():
    sig = inspect.signature(swml_ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_attribute_is_not_abstract():
    assert not inspect.isabstract(swml_Attribute)


def test_swml_attribute_constructor_exists():
    assert callable(swml_Attribute.__init__)


def test_swml_attribute_constructor_args():
    sig = inspect.signature(swml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_swml_attribute_has_name():
    assert hasattr(swml_Attribute, "name")
    descriptor = None
    for klass in swml_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml_attribute_has_type():
    assert hasattr(swml_Attribute, "type")
    descriptor = None
    for klass in swml_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_swml_class_is_not_abstract():
    assert not inspect.isabstract(swml_Class)


def test_swml_class_constructor_exists():
    assert callable(swml_Class.__init__)


def test_swml_class_constructor_args():
    sig = inspect.signature(swml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_class_has_name():
    assert hasattr(swml_Class, "name")
    descriptor = None
    for klass in swml_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml_page_is_not_abstract():
    assert not inspect.isabstract(swml_Page)


def test_swml_page_constructor_exists():
    assert callable(swml_Page.__init__)


def test_swml_page_constructor_args():
    sig = inspect.signature(swml_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_page_has_name():
    assert hasattr(swml_Page, "name")
    descriptor = None
    for klass in swml_Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml_hypertextlayer_is_not_abstract():
    assert not inspect.isabstract(swml_HypertextLayer)


def test_swml_hypertextlayer_constructor_exists():
    assert callable(swml_HypertextLayer.__init__)


def test_swml_hypertextlayer_constructor_args():
    sig = inspect.signature(swml_HypertextLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_webmodel_is_not_abstract():
    assert not inspect.isabstract(swml_WebModel)


def test_swml_webmodel_constructor_exists():
    assert callable(swml_WebModel.__init__)


def test_swml_webmodel_constructor_args():
    sig = inspect.signature(swml_WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_webmodel_has_name():
    assert hasattr(swml_WebModel, "name")
    descriptor = None
    for klass in swml_WebModel.__mro__:
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
        "String",
        "Float",
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
Page_strategy = st.builds(
    Page,
)
swml_DynamicPage_strategy = st.builds(
    swml_DynamicPage,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
swml_DetailsPage_strategy = st.builds(
    swml_DetailsPage,
)
swml_IndexPage_strategy = st.builds(
    swml_IndexPage,
    size=
        st.integers()
)
swml_Link_strategy = st.builds(
    swml_Link,
)
Link_strategy = st.builds(
    Link,
)
swml_CLink_strategy = st.builds(
    swml_CLink,
)
swml_NCLink_strategy = st.builds(
    swml_NCLink,
)
swml_StaticPage_strategy = st.builds(
    swml_StaticPage,
)
swml_ContentLayer_strategy = st.builds(
    swml_ContentLayer,
)
swml_Attribute_strategy = st.builds(
    swml_Attribute,
    name=
        safe_text,
    type=
        safe_text
)
swml_Class_strategy = st.builds(
    swml_Class,
    name=
        safe_text
)
swml_Page_strategy = st.builds(
    swml_Page,
    name=
        safe_text
)
swml_HypertextLayer_strategy = st.builds(
    swml_HypertextLayer,
)
swml_WebModel_strategy = st.builds(
    swml_WebModel,
    name=
        safe_text
)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=swml_DynamicPage_strategy)
@settings(max_examples=50)
def test_swml_dynamicpage_instantiation(instance):
    assert isinstance(instance, swml_DynamicPage)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=swml_DetailsPage_strategy)
@settings(max_examples=50)
def test_swml_detailspage_instantiation(instance):
    assert isinstance(instance, swml_DetailsPage)

@given(instance=swml_IndexPage_strategy)
@settings(max_examples=50)
def test_swml_indexpage_instantiation(instance):
    assert isinstance(instance, swml_IndexPage)



@given(instance=swml_IndexPage_strategy)
def test_swml_indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=swml_Link_strategy)
@settings(max_examples=50)
def test_swml_link_instantiation(instance):
    assert isinstance(instance, swml_Link)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=swml_CLink_strategy)
@settings(max_examples=50)
def test_swml_clink_instantiation(instance):
    assert isinstance(instance, swml_CLink)

@given(instance=swml_NCLink_strategy)
@settings(max_examples=50)
def test_swml_nclink_instantiation(instance):
    assert isinstance(instance, swml_NCLink)

@given(instance=swml_StaticPage_strategy)
@settings(max_examples=50)
def test_swml_staticpage_instantiation(instance):
    assert isinstance(instance, swml_StaticPage)

@given(instance=swml_ContentLayer_strategy)
@settings(max_examples=50)
def test_swml_contentlayer_instantiation(instance):
    assert isinstance(instance, swml_ContentLayer)

@given(instance=swml_Attribute_strategy)
@settings(max_examples=50)
def test_swml_attribute_instantiation(instance):
    assert isinstance(instance, swml_Attribute)



@given(instance=swml_Attribute_strategy)
def test_swml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=swml_Attribute_strategy)
def test_swml_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=swml_Class_strategy)
@settings(max_examples=50)
def test_swml_class_instantiation(instance):
    assert isinstance(instance, swml_Class)



@given(instance=swml_Class_strategy)
def test_swml_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml_Page_strategy)
@settings(max_examples=50)
def test_swml_page_instantiation(instance):
    assert isinstance(instance, swml_Page)



@given(instance=swml_Page_strategy)
def test_swml_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml_HypertextLayer_strategy)
@settings(max_examples=50)
def test_swml_hypertextlayer_instantiation(instance):
    assert isinstance(instance, swml_HypertextLayer)

@given(instance=swml_WebModel_strategy)
@settings(max_examples=50)
def test_swml_webmodel_instantiation(instance):
    assert isinstance(instance, swml_WebModel)



@given(instance=swml_WebModel_strategy)
def test_swml_webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

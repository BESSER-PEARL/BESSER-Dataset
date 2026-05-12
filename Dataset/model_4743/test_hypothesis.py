import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Page,
    swml_v2_DynamicPage,
    DynamicPage,
    swml_v2_DetailsPage,
    swml_v2_IndexPage,
    swml_v2_Link,
    Link,
    swml_v2_CLink,
    swml_v2_NCLink,
    swml_v2_StaticPage,
    swml_v2_Attribute,
    swml_v2_Class,
    swml_v2_ContentLayer,
    swml_v2_NavigationLayer,
    swml_v2_WebModel,
    swml_v2_Page,
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



def test_swml_v2_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(swml_v2_DynamicPage)


def test_swml_v2_dynamicpage_constructor_exists():
    assert callable(swml_v2_DynamicPage.__init__)


def test_swml_v2_dynamicpage_constructor_args():
    sig = inspect.signature(swml_v2_DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_detailspage_is_not_abstract():
    assert not inspect.isabstract(swml_v2_DetailsPage)


def test_swml_v2_detailspage_constructor_exists():
    assert callable(swml_v2_DetailsPage.__init__)


def test_swml_v2_detailspage_constructor_args():
    sig = inspect.signature(swml_v2_DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_indexpage_is_not_abstract():
    assert not inspect.isabstract(swml_v2_IndexPage)


def test_swml_v2_indexpage_constructor_exists():
    assert callable(swml_v2_IndexPage.__init__)


def test_swml_v2_indexpage_constructor_args():
    sig = inspect.signature(swml_v2_IndexPage.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_swml_v2_indexpage_has_size():
    assert hasattr(swml_v2_IndexPage, "size")
    descriptor = None
    for klass in swml_v2_IndexPage.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_swml_v2_link_is_not_abstract():
    assert not inspect.isabstract(swml_v2_Link)


def test_swml_v2_link_constructor_exists():
    assert callable(swml_v2_Link.__init__)


def test_swml_v2_link_constructor_args():
    sig = inspect.signature(swml_v2_Link.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_clink_is_not_abstract():
    assert not inspect.isabstract(swml_v2_CLink)


def test_swml_v2_clink_constructor_exists():
    assert callable(swml_v2_CLink.__init__)


def test_swml_v2_clink_constructor_args():
    sig = inspect.signature(swml_v2_CLink.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_nclink_is_not_abstract():
    assert not inspect.isabstract(swml_v2_NCLink)


def test_swml_v2_nclink_constructor_exists():
    assert callable(swml_v2_NCLink.__init__)


def test_swml_v2_nclink_constructor_args():
    sig = inspect.signature(swml_v2_NCLink.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_staticpage_is_not_abstract():
    assert not inspect.isabstract(swml_v2_StaticPage)


def test_swml_v2_staticpage_constructor_exists():
    assert callable(swml_v2_StaticPage.__init__)


def test_swml_v2_staticpage_constructor_args():
    sig = inspect.signature(swml_v2_StaticPage.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_attribute_is_not_abstract():
    assert not inspect.isabstract(swml_v2_Attribute)


def test_swml_v2_attribute_constructor_exists():
    assert callable(swml_v2_Attribute.__init__)


def test_swml_v2_attribute_constructor_args():
    sig = inspect.signature(swml_v2_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_swml_v2_attribute_has_name():
    assert hasattr(swml_v2_Attribute, "name")
    descriptor = None
    for klass in swml_v2_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swml_v2_attribute_has_type():
    assert hasattr(swml_v2_Attribute, "type")
    descriptor = None
    for klass in swml_v2_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_swml_v2_class_is_not_abstract():
    assert not inspect.isabstract(swml_v2_Class)


def test_swml_v2_class_constructor_exists():
    assert callable(swml_v2_Class.__init__)


def test_swml_v2_class_constructor_args():
    sig = inspect.signature(swml_v2_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_v2_class_has_name():
    assert hasattr(swml_v2_Class, "name")
    descriptor = None
    for klass in swml_v2_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml_v2_contentlayer_is_not_abstract():
    assert not inspect.isabstract(swml_v2_ContentLayer)


def test_swml_v2_contentlayer_constructor_exists():
    assert callable(swml_v2_ContentLayer.__init__)


def test_swml_v2_contentlayer_constructor_args():
    sig = inspect.signature(swml_v2_ContentLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_navigationlayer_is_not_abstract():
    assert not inspect.isabstract(swml_v2_NavigationLayer)


def test_swml_v2_navigationlayer_constructor_exists():
    assert callable(swml_v2_NavigationLayer.__init__)


def test_swml_v2_navigationlayer_constructor_args():
    sig = inspect.signature(swml_v2_NavigationLayer.__init__)
    params = list(sig.parameters.keys())



def test_swml_v2_webmodel_is_not_abstract():
    assert not inspect.isabstract(swml_v2_WebModel)


def test_swml_v2_webmodel_constructor_exists():
    assert callable(swml_v2_WebModel.__init__)


def test_swml_v2_webmodel_constructor_args():
    sig = inspect.signature(swml_v2_WebModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_v2_webmodel_has_name():
    assert hasattr(swml_v2_WebModel, "name")
    descriptor = None
    for klass in swml_v2_WebModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swml_v2_page_is_not_abstract():
    assert not inspect.isabstract(swml_v2_Page)


def test_swml_v2_page_constructor_exists():
    assert callable(swml_v2_Page.__init__)


def test_swml_v2_page_constructor_args():
    sig = inspect.signature(swml_v2_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swml_v2_page_has_name():
    assert hasattr(swml_v2_Page, "name")
    descriptor = None
    for klass in swml_v2_Page.__mro__:
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
        "Email",
        "String",
        "Integer",
        "Boolean",
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
Page_strategy = st.builds(
    Page,
)
swml_v2_DynamicPage_strategy = st.builds(
    swml_v2_DynamicPage,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
swml_v2_DetailsPage_strategy = st.builds(
    swml_v2_DetailsPage,
)
swml_v2_IndexPage_strategy = st.builds(
    swml_v2_IndexPage,
    size=
        st.integers()
)
swml_v2_Link_strategy = st.builds(
    swml_v2_Link,
)
Link_strategy = st.builds(
    Link,
)
swml_v2_CLink_strategy = st.builds(
    swml_v2_CLink,
)
swml_v2_NCLink_strategy = st.builds(
    swml_v2_NCLink,
)
swml_v2_StaticPage_strategy = st.builds(
    swml_v2_StaticPage,
)
swml_v2_Attribute_strategy = st.builds(
    swml_v2_Attribute,
    name=
        safe_text,
    type=
        safe_text
)
swml_v2_Class_strategy = st.builds(
    swml_v2_Class,
    name=
        safe_text
)
swml_v2_ContentLayer_strategy = st.builds(
    swml_v2_ContentLayer,
)
swml_v2_NavigationLayer_strategy = st.builds(
    swml_v2_NavigationLayer,
)
swml_v2_WebModel_strategy = st.builds(
    swml_v2_WebModel,
    name=
        safe_text
)
swml_v2_Page_strategy = st.builds(
    swml_v2_Page,
    name=
        safe_text
)

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=swml_v2_DynamicPage_strategy)
@settings(max_examples=50)
def test_swml_v2_dynamicpage_instantiation(instance):
    assert isinstance(instance, swml_v2_DynamicPage)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=swml_v2_DetailsPage_strategy)
@settings(max_examples=50)
def test_swml_v2_detailspage_instantiation(instance):
    assert isinstance(instance, swml_v2_DetailsPage)

@given(instance=swml_v2_IndexPage_strategy)
@settings(max_examples=50)
def test_swml_v2_indexpage_instantiation(instance):
    assert isinstance(instance, swml_v2_IndexPage)



@given(instance=swml_v2_IndexPage_strategy)
def test_swml_v2_indexpage_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=swml_v2_Link_strategy)
@settings(max_examples=50)
def test_swml_v2_link_instantiation(instance):
    assert isinstance(instance, swml_v2_Link)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=swml_v2_CLink_strategy)
@settings(max_examples=50)
def test_swml_v2_clink_instantiation(instance):
    assert isinstance(instance, swml_v2_CLink)

@given(instance=swml_v2_NCLink_strategy)
@settings(max_examples=50)
def test_swml_v2_nclink_instantiation(instance):
    assert isinstance(instance, swml_v2_NCLink)

@given(instance=swml_v2_StaticPage_strategy)
@settings(max_examples=50)
def test_swml_v2_staticpage_instantiation(instance):
    assert isinstance(instance, swml_v2_StaticPage)

@given(instance=swml_v2_Attribute_strategy)
@settings(max_examples=50)
def test_swml_v2_attribute_instantiation(instance):
    assert isinstance(instance, swml_v2_Attribute)



@given(instance=swml_v2_Attribute_strategy)
def test_swml_v2_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=swml_v2_Attribute_strategy)
def test_swml_v2_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=swml_v2_Class_strategy)
@settings(max_examples=50)
def test_swml_v2_class_instantiation(instance):
    assert isinstance(instance, swml_v2_Class)



@given(instance=swml_v2_Class_strategy)
def test_swml_v2_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml_v2_ContentLayer_strategy)
@settings(max_examples=50)
def test_swml_v2_contentlayer_instantiation(instance):
    assert isinstance(instance, swml_v2_ContentLayer)

@given(instance=swml_v2_NavigationLayer_strategy)
@settings(max_examples=50)
def test_swml_v2_navigationlayer_instantiation(instance):
    assert isinstance(instance, swml_v2_NavigationLayer)

@given(instance=swml_v2_WebModel_strategy)
@settings(max_examples=50)
def test_swml_v2_webmodel_instantiation(instance):
    assert isinstance(instance, swml_v2_WebModel)



@given(instance=swml_v2_WebModel_strategy)
def test_swml_v2_webmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swml_v2_Page_strategy)
@settings(max_examples=50)
def test_swml_v2_page_instantiation(instance):
    assert isinstance(instance, swml_v2_Page)



@given(instance=swml_v2_Page_strategy)
def test_swml_v2_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

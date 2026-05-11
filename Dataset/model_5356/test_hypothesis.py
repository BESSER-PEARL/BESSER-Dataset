import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LocatedElement,
    p2::FeatureMetadata,
    Bundle,
    FeatureMetadata,
    p2::Plugin,
    p2::Vendor,
    p2::License,
    p2::DiscoverySite,
    p2::Description,
    p2::Copyright,
    Tool,
    p2::Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_p2::featuremetadata_is_not_abstract():
    assert not inspect.isabstract(p2::FeatureMetadata)


def test_p2::featuremetadata_constructor_exists():
    assert callable(p2::FeatureMetadata.__init__)


def test_p2::featuremetadata_constructor_args():
    sig = inspect.signature(p2::FeatureMetadata.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "name" in params, "Missing parameter 'name'"

def test_p2::featuremetadata_has_text():
    assert hasattr(p2::FeatureMetadata, "text")
    descriptor = None
    for klass in p2::FeatureMetadata.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_p2::featuremetadata_has_name():
    assert hasattr(p2::FeatureMetadata, "name")
    descriptor = None
    for klass in p2::FeatureMetadata.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bundle_is_not_abstract():
    assert not inspect.isabstract(Bundle)


def test_bundle_constructor_exists():
    assert callable(Bundle.__init__)


def test_bundle_constructor_args():
    sig = inspect.signature(Bundle.__init__)
    params = list(sig.parameters.keys())



def test_featuremetadata_is_not_abstract():
    assert not inspect.isabstract(FeatureMetadata)


def test_featuremetadata_constructor_exists():
    assert callable(FeatureMetadata.__init__)


def test_featuremetadata_constructor_args():
    sig = inspect.signature(FeatureMetadata.__init__)
    params = list(sig.parameters.keys())



def test_p2::plugin_is_not_abstract():
    assert not inspect.isabstract(p2::Plugin)


def test_p2::plugin_constructor_exists():
    assert callable(p2::Plugin.__init__)


def test_p2::plugin_constructor_args():
    sig = inspect.signature(p2::Plugin.__init__)
    params = list(sig.parameters.keys())



def test_p2::vendor_is_not_abstract():
    assert not inspect.isabstract(p2::Vendor)


def test_p2::vendor_constructor_exists():
    assert callable(p2::Vendor.__init__)


def test_p2::vendor_constructor_args():
    sig = inspect.signature(p2::Vendor.__init__)
    params = list(sig.parameters.keys())



def test_p2::license_is_not_abstract():
    assert not inspect.isabstract(p2::License)


def test_p2::license_constructor_exists():
    assert callable(p2::License.__init__)


def test_p2::license_constructor_args():
    sig = inspect.signature(p2::License.__init__)
    params = list(sig.parameters.keys())



def test_p2::discoverysite_is_not_abstract():
    assert not inspect.isabstract(p2::DiscoverySite)


def test_p2::discoverysite_constructor_exists():
    assert callable(p2::DiscoverySite.__init__)


def test_p2::discoverysite_constructor_args():
    sig = inspect.signature(p2::DiscoverySite.__init__)
    params = list(sig.parameters.keys())



def test_p2::description_is_not_abstract():
    assert not inspect.isabstract(p2::Description)


def test_p2::description_constructor_exists():
    assert callable(p2::Description.__init__)


def test_p2::description_constructor_args():
    sig = inspect.signature(p2::Description.__init__)
    params = list(sig.parameters.keys())



def test_p2::copyright_is_not_abstract():
    assert not inspect.isabstract(p2::Copyright)


def test_p2::copyright_constructor_exists():
    assert callable(p2::Copyright.__init__)


def test_p2::copyright_constructor_args():
    sig = inspect.signature(p2::Copyright.__init__)
    params = list(sig.parameters.keys())



def test_tool_is_not_abstract():
    assert not inspect.isabstract(Tool)


def test_tool_constructor_exists():
    assert callable(Tool.__init__)


def test_tool_constructor_args():
    sig = inspect.signature(Tool.__init__)
    params = list(sig.parameters.keys())



def test_p2::feature_is_not_abstract():
    assert not inspect.isabstract(p2::Feature)


def test_p2::feature_constructor_exists():
    assert callable(p2::Feature.__init__)


def test_p2::feature_constructor_args():
    sig = inspect.signature(p2::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "application" in params, "Missing parameter 'application'"

def test_p2::feature_has_application():
    assert hasattr(p2::Feature, "application")
    descriptor = None
    for klass in p2::Feature.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)


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
LocatedElement_strategy = st.builds(
    LocatedElement,
)
p2::FeatureMetadata_strategy = st.builds(
    p2::FeatureMetadata,
    text=
        safe_text,
    name=
        safe_text
)
Bundle_strategy = st.builds(
    Bundle,
)
FeatureMetadata_strategy = st.builds(
    FeatureMetadata,
)
p2::Plugin_strategy = st.builds(
    p2::Plugin,
)
p2::Vendor_strategy = st.builds(
    p2::Vendor,
)
p2::License_strategy = st.builds(
    p2::License,
)
p2::DiscoverySite_strategy = st.builds(
    p2::DiscoverySite,
)
p2::Description_strategy = st.builds(
    p2::Description,
)
p2::Copyright_strategy = st.builds(
    p2::Copyright,
)
Tool_strategy = st.builds(
    Tool,
)
p2::Feature_strategy = st.builds(
    p2::Feature,
    application=
        safe_text
)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=p2::FeatureMetadata_strategy)
@settings(max_examples=50)
def test_p2::featuremetadata_instantiation(instance):
    assert isinstance(instance, p2::FeatureMetadata)

@given(instance=p2::FeatureMetadata_strategy)
def test_p2::featuremetadata_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=p2::FeatureMetadata_strategy)
def test_p2::featuremetadata_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=p2::FeatureMetadata_strategy)
def test_p2::featuremetadata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=p2::FeatureMetadata_strategy)
def test_p2::featuremetadata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Bundle_strategy)
@settings(max_examples=50)
def test_bundle_instantiation(instance):
    assert isinstance(instance, Bundle)

@given(instance=FeatureMetadata_strategy)
@settings(max_examples=50)
def test_featuremetadata_instantiation(instance):
    assert isinstance(instance, FeatureMetadata)

@given(instance=p2::Plugin_strategy)
@settings(max_examples=50)
def test_p2::plugin_instantiation(instance):
    assert isinstance(instance, p2::Plugin)

@given(instance=p2::Vendor_strategy)
@settings(max_examples=50)
def test_p2::vendor_instantiation(instance):
    assert isinstance(instance, p2::Vendor)

@given(instance=p2::License_strategy)
@settings(max_examples=50)
def test_p2::license_instantiation(instance):
    assert isinstance(instance, p2::License)

@given(instance=p2::DiscoverySite_strategy)
@settings(max_examples=50)
def test_p2::discoverysite_instantiation(instance):
    assert isinstance(instance, p2::DiscoverySite)

@given(instance=p2::Description_strategy)
@settings(max_examples=50)
def test_p2::description_instantiation(instance):
    assert isinstance(instance, p2::Description)

@given(instance=p2::Copyright_strategy)
@settings(max_examples=50)
def test_p2::copyright_instantiation(instance):
    assert isinstance(instance, p2::Copyright)

@given(instance=Tool_strategy)
@settings(max_examples=50)
def test_tool_instantiation(instance):
    assert isinstance(instance, Tool)

@given(instance=p2::Feature_strategy)
@settings(max_examples=50)
def test_p2::feature_instantiation(instance):
    assert isinstance(instance, p2::Feature)

@given(instance=p2::Feature_strategy)
def test_p2::feature_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=p2::Feature_strategy)
def test_p2::feature_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

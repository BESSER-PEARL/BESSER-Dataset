import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    configDsl::Generator,
    configDsl::Config,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_configdsl::generator_is_not_abstract():
    assert not inspect.isabstract(configDsl::Generator)


def test_configdsl::generator_constructor_exists():
    assert callable(configDsl::Generator.__init__)


def test_configdsl::generator_constructor_args():
    sig = inspect.signature(configDsl::Generator.__init__)
    params = list(sig.parameters.keys())
    assert "genClass" in params, "Missing parameter 'genClass'"
    assert "bundle" in params, "Missing parameter 'bundle'"
    assert "name" in params, "Missing parameter 'name'"

def test_configdsl::generator_has_genClass():
    assert hasattr(configDsl::Generator, "genClass")
    descriptor = None
    for klass in configDsl::Generator.__mro__:
        if "genClass" in klass.__dict__:
            descriptor = klass.__dict__["genClass"]
            break
    assert isinstance(descriptor, property)

def test_configdsl::generator_has_bundle():
    assert hasattr(configDsl::Generator, "bundle")
    descriptor = None
    for klass in configDsl::Generator.__mro__:
        if "bundle" in klass.__dict__:
            descriptor = klass.__dict__["bundle"]
            break
    assert isinstance(descriptor, property)

def test_configdsl::generator_has_name():
    assert hasattr(configDsl::Generator, "name")
    descriptor = None
    for klass in configDsl::Generator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_configdsl::config_is_not_abstract():
    assert not inspect.isabstract(configDsl::Config)


def test_configdsl::config_constructor_exists():
    assert callable(configDsl::Config.__init__)


def test_configdsl::config_constructor_args():
    sig = inspect.signature(configDsl::Config.__init__)
    params = list(sig.parameters.keys())
    assert "srcFolder" in params, "Missing parameter 'srcFolder'"
    assert "mainClass" in params, "Missing parameter 'mainClass'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "outFolder" in params, "Missing parameter 'outFolder'"

def test_configdsl::config_has_srcFolder():
    assert hasattr(configDsl::Config, "srcFolder")
    descriptor = None
    for klass in configDsl::Config.__mro__:
        if "srcFolder" in klass.__dict__:
            descriptor = klass.__dict__["srcFolder"]
            break
    assert isinstance(descriptor, property)

def test_configdsl::config_has_mainClass():
    assert hasattr(configDsl::Config, "mainClass")
    descriptor = None
    for klass in configDsl::Config.__mro__:
        if "mainClass" in klass.__dict__:
            descriptor = klass.__dict__["mainClass"]
            break
    assert isinstance(descriptor, property)

def test_configdsl::config_has_appName():
    assert hasattr(configDsl::Config, "appName")
    descriptor = None
    for klass in configDsl::Config.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_configdsl::config_has_outFolder():
    assert hasattr(configDsl::Config, "outFolder")
    descriptor = None
    for klass in configDsl::Config.__mro__:
        if "outFolder" in klass.__dict__:
            descriptor = klass.__dict__["outFolder"]
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
configDsl::Generator_strategy = st.builds(
    configDsl::Generator,
    genClass=
        safe_text,
    bundle=
        safe_text,
    name=
        safe_text
)
configDsl::Config_strategy = st.builds(
    configDsl::Config,
    srcFolder=
        safe_text,
    mainClass=
        safe_text,
    appName=
        safe_text,
    outFolder=
        safe_text
)

@given(instance=configDsl::Generator_strategy)
@settings(max_examples=50)
def test_configdsl::generator_instantiation(instance):
    assert isinstance(instance, configDsl::Generator)

@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_genClass_type(instance):
    assert isinstance(instance.genClass, str)


@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_genClass_setter(instance):
    original = instance.genClass
    instance.genClass = original
    assert instance.genClass == original

@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_bundle_type(instance):
    assert isinstance(instance.bundle, str)


@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_bundle_setter(instance):
    original = instance.bundle
    instance.bundle = original
    assert instance.bundle == original

@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=configDsl::Generator_strategy)
def test_configdsl::generator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=configDsl::Config_strategy)
@settings(max_examples=50)
def test_configdsl::config_instantiation(instance):
    assert isinstance(instance, configDsl::Config)

@given(instance=configDsl::Config_strategy)
def test_configdsl::config_srcFolder_type(instance):
    assert isinstance(instance.srcFolder, str)


@given(instance=configDsl::Config_strategy)
def test_configdsl::config_srcFolder_setter(instance):
    original = instance.srcFolder
    instance.srcFolder = original
    assert instance.srcFolder == original

@given(instance=configDsl::Config_strategy)
def test_configdsl::config_mainClass_type(instance):
    assert isinstance(instance.mainClass, str)


@given(instance=configDsl::Config_strategy)
def test_configdsl::config_mainClass_setter(instance):
    original = instance.mainClass
    instance.mainClass = original
    assert instance.mainClass == original

@given(instance=configDsl::Config_strategy)
def test_configdsl::config_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=configDsl::Config_strategy)
def test_configdsl::config_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=configDsl::Config_strategy)
def test_configdsl::config_outFolder_type(instance):
    assert isinstance(instance.outFolder, str)


@given(instance=configDsl::Config_strategy)
def test_configdsl::config_outFolder_setter(instance):
    original = instance.outFolder
    instance.outFolder = original
    assert instance.outFolder == original

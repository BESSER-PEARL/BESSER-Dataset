import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    configDsl_Generator,
    configDsl_Config,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_configdsl_generator_is_not_abstract():
    assert not inspect.isabstract(configDsl_Generator)


def test_configdsl_generator_constructor_exists():
    assert callable(configDsl_Generator.__init__)


def test_configdsl_generator_constructor_args():
    sig = inspect.signature(configDsl_Generator.__init__)
    params = list(sig.parameters.keys())
    assert "genClass" in params, "Missing parameter 'genClass'"
    assert "name" in params, "Missing parameter 'name'"
    assert "bundle" in params, "Missing parameter 'bundle'"

def test_configdsl_generator_has_genClass():
    assert hasattr(configDsl_Generator, "genClass")
    descriptor = None
    for klass in configDsl_Generator.__mro__:
        if "genClass" in klass.__dict__:
            descriptor = klass.__dict__["genClass"]
            break
    assert isinstance(descriptor, property)

def test_configdsl_generator_has_name():
    assert hasattr(configDsl_Generator, "name")
    descriptor = None
    for klass in configDsl_Generator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_configdsl_generator_has_bundle():
    assert hasattr(configDsl_Generator, "bundle")
    descriptor = None
    for klass in configDsl_Generator.__mro__:
        if "bundle" in klass.__dict__:
            descriptor = klass.__dict__["bundle"]
            break
    assert isinstance(descriptor, property)



def test_configdsl_config_is_not_abstract():
    assert not inspect.isabstract(configDsl_Config)


def test_configdsl_config_constructor_exists():
    assert callable(configDsl_Config.__init__)


def test_configdsl_config_constructor_args():
    sig = inspect.signature(configDsl_Config.__init__)
    params = list(sig.parameters.keys())
    assert "srcFolder" in params, "Missing parameter 'srcFolder'"
    assert "mainClass" in params, "Missing parameter 'mainClass'"
    assert "outFolder" in params, "Missing parameter 'outFolder'"
    assert "appName" in params, "Missing parameter 'appName'"

def test_configdsl_config_has_srcFolder():
    assert hasattr(configDsl_Config, "srcFolder")
    descriptor = None
    for klass in configDsl_Config.__mro__:
        if "srcFolder" in klass.__dict__:
            descriptor = klass.__dict__["srcFolder"]
            break
    assert isinstance(descriptor, property)

def test_configdsl_config_has_mainClass():
    assert hasattr(configDsl_Config, "mainClass")
    descriptor = None
    for klass in configDsl_Config.__mro__:
        if "mainClass" in klass.__dict__:
            descriptor = klass.__dict__["mainClass"]
            break
    assert isinstance(descriptor, property)

def test_configdsl_config_has_outFolder():
    assert hasattr(configDsl_Config, "outFolder")
    descriptor = None
    for klass in configDsl_Config.__mro__:
        if "outFolder" in klass.__dict__:
            descriptor = klass.__dict__["outFolder"]
            break
    assert isinstance(descriptor, property)

def test_configdsl_config_has_appName():
    assert hasattr(configDsl_Config, "appName")
    descriptor = None
    for klass in configDsl_Config.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
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
configDsl_Generator_strategy = st.builds(
    configDsl_Generator,
    genClass=
        safe_text,
    name=
        safe_text,
    bundle=
        safe_text
)
configDsl_Config_strategy = st.builds(
    configDsl_Config,
    srcFolder=
        safe_text,
    mainClass=
        safe_text,
    outFolder=
        safe_text,
    appName=
        safe_text
)

@given(instance=configDsl_Generator_strategy)
@settings(max_examples=50)
def test_configdsl_generator_instantiation(instance):
    assert isinstance(instance, configDsl_Generator)



@given(instance=configDsl_Generator_strategy)
def test_configdsl_generator_genClass_setter(instance):
    original = instance.genClass
    instance.genClass = original
    assert instance.genClass == original



@given(instance=configDsl_Generator_strategy)
def test_configdsl_generator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=configDsl_Generator_strategy)
def test_configdsl_generator_bundle_setter(instance):
    original = instance.bundle
    instance.bundle = original
    assert instance.bundle == original

@given(instance=configDsl_Config_strategy)
@settings(max_examples=50)
def test_configdsl_config_instantiation(instance):
    assert isinstance(instance, configDsl_Config)



@given(instance=configDsl_Config_strategy)
def test_configdsl_config_srcFolder_setter(instance):
    original = instance.srcFolder
    instance.srcFolder = original
    assert instance.srcFolder == original



@given(instance=configDsl_Config_strategy)
def test_configdsl_config_mainClass_setter(instance):
    original = instance.mainClass
    instance.mainClass = original
    assert instance.mainClass == original



@given(instance=configDsl_Config_strategy)
def test_configdsl_config_outFolder_setter(instance):
    original = instance.outFolder
    instance.outFolder = original
    assert instance.outFolder == original



@given(instance=configDsl_Config_strategy)
def test_configdsl_config_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

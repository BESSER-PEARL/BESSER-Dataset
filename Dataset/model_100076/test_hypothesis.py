import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OptionBinding,
    build_FileName,
    build_Include,
    build_ModuleType,
    Instance,
    build_ModuleInstance,
    build_Configuration,
    build_Build,
    build_OptionInstance,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_optionbinding_is_not_abstract():
    assert not inspect.isabstract(OptionBinding)


def test_optionbinding_constructor_exists():
    assert callable(OptionBinding.__init__)


def test_optionbinding_constructor_args():
    sig = inspect.signature(OptionBinding.__init__)
    params = list(sig.parameters.keys())



def test_build_filename_is_not_abstract():
    assert not inspect.isabstract(build_FileName)


def test_build_filename_constructor_exists():
    assert callable(build_FileName.__init__)


def test_build_filename_constructor_args():
    sig = inspect.signature(build_FileName.__init__)
    params = list(sig.parameters.keys())



def test_build_include_is_not_abstract():
    assert not inspect.isabstract(build_Include)


def test_build_include_constructor_exists():
    assert callable(build_Include.__init__)


def test_build_include_constructor_args():
    sig = inspect.signature(build_Include.__init__)
    params = list(sig.parameters.keys())



def test_build_moduletype_is_not_abstract():
    assert not inspect.isabstract(build_ModuleType)


def test_build_moduletype_constructor_exists():
    assert callable(build_ModuleType.__init__)


def test_build_moduletype_constructor_args():
    sig = inspect.signature(build_ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_build_moduleinstance_is_not_abstract():
    assert not inspect.isabstract(build_ModuleInstance)


def test_build_moduleinstance_constructor_exists():
    assert callable(build_ModuleInstance.__init__)


def test_build_moduleinstance_constructor_args():
    sig = inspect.signature(build_ModuleInstance.__init__)
    params = list(sig.parameters.keys())



def test_build_configuration_is_not_abstract():
    assert not inspect.isabstract(build_Configuration)


def test_build_configuration_constructor_exists():
    assert callable(build_Configuration.__init__)


def test_build_configuration_constructor_args():
    sig = inspect.signature(build_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_build_build_is_not_abstract():
    assert not inspect.isabstract(build_Build)


def test_build_build_constructor_exists():
    assert callable(build_Build.__init__)


def test_build_build_constructor_args():
    sig = inspect.signature(build_Build.__init__)
    params = list(sig.parameters.keys())



def test_build_optioninstance_is_not_abstract():
    assert not inspect.isabstract(build_OptionInstance)


def test_build_optioninstance_constructor_exists():
    assert callable(build_OptionInstance.__init__)


def test_build_optioninstance_constructor_args():
    sig = inspect.signature(build_OptionInstance.__init__)
    params = list(sig.parameters.keys())


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
OptionBinding_strategy = st.builds(
    OptionBinding,
)
build_FileName_strategy = st.builds(
    build_FileName,
)
build_Include_strategy = st.builds(
    build_Include,
)
build_ModuleType_strategy = st.builds(
    build_ModuleType,
)
Instance_strategy = st.builds(
    Instance,
)
build_ModuleInstance_strategy = st.builds(
    build_ModuleInstance,
)
build_Configuration_strategy = st.builds(
    build_Configuration,
)
build_Build_strategy = st.builds(
    build_Build,
)
build_OptionInstance_strategy = st.builds(
    build_OptionInstance,
)

@given(instance=OptionBinding_strategy)
@settings(max_examples=50)
def test_optionbinding_instantiation(instance):
    assert isinstance(instance, OptionBinding)

@given(instance=build_FileName_strategy)
@settings(max_examples=50)
def test_build_filename_instantiation(instance):
    assert isinstance(instance, build_FileName)

@given(instance=build_Include_strategy)
@settings(max_examples=50)
def test_build_include_instantiation(instance):
    assert isinstance(instance, build_Include)

@given(instance=build_ModuleType_strategy)
@settings(max_examples=50)
def test_build_moduletype_instantiation(instance):
    assert isinstance(instance, build_ModuleType)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=build_ModuleInstance_strategy)
@settings(max_examples=50)
def test_build_moduleinstance_instantiation(instance):
    assert isinstance(instance, build_ModuleInstance)

@given(instance=build_Configuration_strategy)
@settings(max_examples=50)
def test_build_configuration_instantiation(instance):
    assert isinstance(instance, build_Configuration)

@given(instance=build_Build_strategy)
@settings(max_examples=50)
def test_build_build_instantiation(instance):
    assert isinstance(instance, build_Build)

@given(instance=build_OptionInstance_strategy)
@settings(max_examples=50)
def test_build_optioninstance_instantiation(instance):
    assert isinstance(instance, build_OptionInstance)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    build::Configuration,
    build::Build,
    OptionBinding,
    build::OptionInstance,
    build::FileName,
    build::Include,
    build::ModuleType,
    Instance,
    build::ModuleInstance,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_build::configuration_is_not_abstract():
    assert not inspect.isabstract(build::Configuration)


def test_build::configuration_constructor_exists():
    assert callable(build::Configuration.__init__)


def test_build::configuration_constructor_args():
    sig = inspect.signature(build::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_build::build_is_not_abstract():
    assert not inspect.isabstract(build::Build)


def test_build::build_constructor_exists():
    assert callable(build::Build.__init__)


def test_build::build_constructor_args():
    sig = inspect.signature(build::Build.__init__)
    params = list(sig.parameters.keys())



def test_optionbinding_is_not_abstract():
    assert not inspect.isabstract(OptionBinding)


def test_optionbinding_constructor_exists():
    assert callable(OptionBinding.__init__)


def test_optionbinding_constructor_args():
    sig = inspect.signature(OptionBinding.__init__)
    params = list(sig.parameters.keys())



def test_build::optioninstance_is_not_abstract():
    assert not inspect.isabstract(build::OptionInstance)


def test_build::optioninstance_constructor_exists():
    assert callable(build::OptionInstance.__init__)


def test_build::optioninstance_constructor_args():
    sig = inspect.signature(build::OptionInstance.__init__)
    params = list(sig.parameters.keys())



def test_build::filename_is_not_abstract():
    assert not inspect.isabstract(build::FileName)


def test_build::filename_constructor_exists():
    assert callable(build::FileName.__init__)


def test_build::filename_constructor_args():
    sig = inspect.signature(build::FileName.__init__)
    params = list(sig.parameters.keys())



def test_build::include_is_not_abstract():
    assert not inspect.isabstract(build::Include)


def test_build::include_constructor_exists():
    assert callable(build::Include.__init__)


def test_build::include_constructor_args():
    sig = inspect.signature(build::Include.__init__)
    params = list(sig.parameters.keys())



def test_build::moduletype_is_not_abstract():
    assert not inspect.isabstract(build::ModuleType)


def test_build::moduletype_constructor_exists():
    assert callable(build::ModuleType.__init__)


def test_build::moduletype_constructor_args():
    sig = inspect.signature(build::ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_instance_is_not_abstract():
    assert not inspect.isabstract(Instance)


def test_instance_constructor_exists():
    assert callable(Instance.__init__)


def test_instance_constructor_args():
    sig = inspect.signature(Instance.__init__)
    params = list(sig.parameters.keys())



def test_build::moduleinstance_is_not_abstract():
    assert not inspect.isabstract(build::ModuleInstance)


def test_build::moduleinstance_constructor_exists():
    assert callable(build::ModuleInstance.__init__)


def test_build::moduleinstance_constructor_args():
    sig = inspect.signature(build::ModuleInstance.__init__)
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
build::Configuration_strategy = st.builds(
    build::Configuration,
)
build::Build_strategy = st.builds(
    build::Build,
)
OptionBinding_strategy = st.builds(
    OptionBinding,
)
build::OptionInstance_strategy = st.builds(
    build::OptionInstance,
)
build::FileName_strategy = st.builds(
    build::FileName,
)
build::Include_strategy = st.builds(
    build::Include,
)
build::ModuleType_strategy = st.builds(
    build::ModuleType,
)
Instance_strategy = st.builds(
    Instance,
)
build::ModuleInstance_strategy = st.builds(
    build::ModuleInstance,
)

@given(instance=build::Configuration_strategy)
@settings(max_examples=50)
def test_build::configuration_instantiation(instance):
    assert isinstance(instance, build::Configuration)

@given(instance=build::Build_strategy)
@settings(max_examples=50)
def test_build::build_instantiation(instance):
    assert isinstance(instance, build::Build)

@given(instance=OptionBinding_strategy)
@settings(max_examples=50)
def test_optionbinding_instantiation(instance):
    assert isinstance(instance, OptionBinding)

@given(instance=build::OptionInstance_strategy)
@settings(max_examples=50)
def test_build::optioninstance_instantiation(instance):
    assert isinstance(instance, build::OptionInstance)

@given(instance=build::FileName_strategy)
@settings(max_examples=50)
def test_build::filename_instantiation(instance):
    assert isinstance(instance, build::FileName)

@given(instance=build::Include_strategy)
@settings(max_examples=50)
def test_build::include_instantiation(instance):
    assert isinstance(instance, build::Include)

@given(instance=build::ModuleType_strategy)
@settings(max_examples=50)
def test_build::moduletype_instantiation(instance):
    assert isinstance(instance, build::ModuleType)

@given(instance=Instance_strategy)
@settings(max_examples=50)
def test_instance_instantiation(instance):
    assert isinstance(instance, Instance)

@given(instance=build::ModuleInstance_strategy)
@settings(max_examples=50)
def test_build::moduleinstance_instantiation(instance):
    assert isinstance(instance, build::ModuleInstance)

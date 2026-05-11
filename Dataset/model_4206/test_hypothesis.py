import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Import,
    myDsl::Greeting,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::import_is_not_abstract():
    assert not inspect.isabstract(myDsl::Import)


def test_mydsl::import_constructor_exists():
    assert callable(myDsl::Import.__init__)


def test_mydsl::import_constructor_args():
    sig = inspect.signature(myDsl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "Import_type" in params, "Missing parameter 'Import_type'"
    assert "import_num" in params, "Missing parameter 'import_num'"

def test_mydsl::import_has_Import_type():
    assert hasattr(myDsl::Import, "Import_type")
    descriptor = None
    for klass in myDsl::Import.__mro__:
        if "Import_type" in klass.__dict__:
            descriptor = klass.__dict__["Import_type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::import_has_import_num():
    assert hasattr(myDsl::Import, "import_num")
    descriptor = None
    for klass in myDsl::Import.__mro__:
        if "import_num" in klass.__dict__:
            descriptor = klass.__dict__["import_num"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_name():
    assert hasattr(myDsl::Greeting, "name")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
myDsl::Import_strategy = st.builds(
    myDsl::Import,
    Import_type=
        safe_text,
    import_num=
        st.integers()
)
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=myDsl::Import_strategy)
@settings(max_examples=50)
def test_mydsl::import_instantiation(instance):
    assert isinstance(instance, myDsl::Import)

@given(instance=myDsl::Import_strategy)
def test_mydsl::import_Import_type_type(instance):
    assert isinstance(instance.Import_type, str)


@given(instance=myDsl::Import_strategy)
def test_mydsl::import_Import_type_setter(instance):
    original = instance.Import_type
    instance.Import_type = original
    assert instance.Import_type == original

@given(instance=myDsl::Import_strategy)
def test_mydsl::import_import_num_type(instance):
    assert isinstance(instance.import_num, int)


@given(instance=myDsl::Import_strategy)
def test_mydsl::import_import_num_setter(instance):
    original = instance.import_num
    instance.import_num = original
    assert instance.import_num == original

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

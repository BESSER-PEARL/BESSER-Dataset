import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    fds::Table,
    fds::Database,
    fds::NamedElement,
    CandidateKey,
    fds::PrimaryKey,
    Restriction,
    fds::CandidateKey,
    fds::ForeignKey,
    fds::RestrictionColumn,
    fds::Restriction,
    fds::FunctionalDependency,
    fds::Column,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fds::table_is_not_abstract():
    assert not inspect.isabstract(fds::Table)


def test_fds::table_constructor_exists():
    assert callable(fds::Table.__init__)


def test_fds::table_constructor_args():
    sig = inspect.signature(fds::Table.__init__)
    params = list(sig.parameters.keys())



def test_fds::database_is_not_abstract():
    assert not inspect.isabstract(fds::Database)


def test_fds::database_constructor_exists():
    assert callable(fds::Database.__init__)


def test_fds::database_constructor_args():
    sig = inspect.signature(fds::Database.__init__)
    params = list(sig.parameters.keys())



def test_fds::namedelement_is_not_abstract():
    assert not inspect.isabstract(fds::NamedElement)


def test_fds::namedelement_constructor_exists():
    assert callable(fds::NamedElement.__init__)


def test_fds::namedelement_constructor_args():
    sig = inspect.signature(fds::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fds::namedelement_has_name():
    assert hasattr(fds::NamedElement, "name")
    descriptor = None
    for klass in fds::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_candidatekey_is_not_abstract():
    assert not inspect.isabstract(CandidateKey)


def test_candidatekey_constructor_exists():
    assert callable(CandidateKey.__init__)


def test_candidatekey_constructor_args():
    sig = inspect.signature(CandidateKey.__init__)
    params = list(sig.parameters.keys())



def test_fds::primarykey_is_not_abstract():
    assert not inspect.isabstract(fds::PrimaryKey)


def test_fds::primarykey_constructor_exists():
    assert callable(fds::PrimaryKey.__init__)


def test_fds::primarykey_constructor_args():
    sig = inspect.signature(fds::PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_fds::candidatekey_is_not_abstract():
    assert not inspect.isabstract(fds::CandidateKey)


def test_fds::candidatekey_constructor_exists():
    assert callable(fds::CandidateKey.__init__)


def test_fds::candidatekey_constructor_args():
    sig = inspect.signature(fds::CandidateKey.__init__)
    params = list(sig.parameters.keys())



def test_fds::foreignkey_is_not_abstract():
    assert not inspect.isabstract(fds::ForeignKey)


def test_fds::foreignkey_constructor_exists():
    assert callable(fds::ForeignKey.__init__)


def test_fds::foreignkey_constructor_args():
    sig = inspect.signature(fds::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_fds::restrictioncolumn_is_not_abstract():
    assert not inspect.isabstract(fds::RestrictionColumn)


def test_fds::restrictioncolumn_constructor_exists():
    assert callable(fds::RestrictionColumn.__init__)


def test_fds::restrictioncolumn_constructor_args():
    sig = inspect.signature(fds::RestrictionColumn.__init__)
    params = list(sig.parameters.keys())



def test_fds::restriction_is_not_abstract():
    assert not inspect.isabstract(fds::Restriction)


def test_fds::restriction_constructor_exists():
    assert callable(fds::Restriction.__init__)


def test_fds::restriction_constructor_args():
    sig = inspect.signature(fds::Restriction.__init__)
    params = list(sig.parameters.keys())



def test_fds::functionaldependency_is_not_abstract():
    assert not inspect.isabstract(fds::FunctionalDependency)


def test_fds::functionaldependency_constructor_exists():
    assert callable(fds::FunctionalDependency.__init__)


def test_fds::functionaldependency_constructor_args():
    sig = inspect.signature(fds::FunctionalDependency.__init__)
    params = list(sig.parameters.keys())



def test_fds::column_is_not_abstract():
    assert not inspect.isabstract(fds::Column)


def test_fds::column_constructor_exists():
    assert callable(fds::Column.__init__)


def test_fds::column_constructor_args():
    sig = inspect.signature(fds::Column.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
fds::Table_strategy = st.builds(
    fds::Table,
)
fds::Database_strategy = st.builds(
    fds::Database,
)
fds::NamedElement_strategy = st.builds(
    fds::NamedElement,
    name=
        safe_text
)
CandidateKey_strategy = st.builds(
    CandidateKey,
)
fds::PrimaryKey_strategy = st.builds(
    fds::PrimaryKey,
)
Restriction_strategy = st.builds(
    Restriction,
)
fds::CandidateKey_strategy = st.builds(
    fds::CandidateKey,
)
fds::ForeignKey_strategy = st.builds(
    fds::ForeignKey,
)
fds::RestrictionColumn_strategy = st.builds(
    fds::RestrictionColumn,
)
fds::Restriction_strategy = st.builds(
    fds::Restriction,
)
fds::FunctionalDependency_strategy = st.builds(
    fds::FunctionalDependency,
)
fds::Column_strategy = st.builds(
    fds::Column,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fds::Table_strategy)
@settings(max_examples=50)
def test_fds::table_instantiation(instance):
    assert isinstance(instance, fds::Table)

@given(instance=fds::Database_strategy)
@settings(max_examples=50)
def test_fds::database_instantiation(instance):
    assert isinstance(instance, fds::Database)

@given(instance=fds::NamedElement_strategy)
@settings(max_examples=50)
def test_fds::namedelement_instantiation(instance):
    assert isinstance(instance, fds::NamedElement)

@given(instance=fds::NamedElement_strategy)
def test_fds::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fds::NamedElement_strategy)
def test_fds::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CandidateKey_strategy)
@settings(max_examples=50)
def test_candidatekey_instantiation(instance):
    assert isinstance(instance, CandidateKey)

@given(instance=fds::PrimaryKey_strategy)
@settings(max_examples=50)
def test_fds::primarykey_instantiation(instance):
    assert isinstance(instance, fds::PrimaryKey)

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=fds::CandidateKey_strategy)
@settings(max_examples=50)
def test_fds::candidatekey_instantiation(instance):
    assert isinstance(instance, fds::CandidateKey)

@given(instance=fds::ForeignKey_strategy)
@settings(max_examples=50)
def test_fds::foreignkey_instantiation(instance):
    assert isinstance(instance, fds::ForeignKey)

@given(instance=fds::RestrictionColumn_strategy)
@settings(max_examples=50)
def test_fds::restrictioncolumn_instantiation(instance):
    assert isinstance(instance, fds::RestrictionColumn)

@given(instance=fds::Restriction_strategy)
@settings(max_examples=50)
def test_fds::restriction_instantiation(instance):
    assert isinstance(instance, fds::Restriction)

@given(instance=fds::FunctionalDependency_strategy)
@settings(max_examples=50)
def test_fds::functionaldependency_instantiation(instance):
    assert isinstance(instance, fds::FunctionalDependency)

@given(instance=fds::Column_strategy)
@settings(max_examples=50)
def test_fds::column_instantiation(instance):
    assert isinstance(instance, fds::Column)

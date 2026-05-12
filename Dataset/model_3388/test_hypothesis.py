import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    fds_Table,
    fds_Database,
    fds_NamedElement,
    CandidateKey,
    fds_PrimaryKey,
    Restriction,
    fds_CandidateKey,
    fds_ForeignKey,
    fds_RestrictionColumn,
    fds_Restriction,
    fds_FunctionalDependency,
    fds_Column,
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



def test_fds_table_is_not_abstract():
    assert not inspect.isabstract(fds_Table)


def test_fds_table_constructor_exists():
    assert callable(fds_Table.__init__)


def test_fds_table_constructor_args():
    sig = inspect.signature(fds_Table.__init__)
    params = list(sig.parameters.keys())



def test_fds_database_is_not_abstract():
    assert not inspect.isabstract(fds_Database)


def test_fds_database_constructor_exists():
    assert callable(fds_Database.__init__)


def test_fds_database_constructor_args():
    sig = inspect.signature(fds_Database.__init__)
    params = list(sig.parameters.keys())



def test_fds_namedelement_is_not_abstract():
    assert not inspect.isabstract(fds_NamedElement)


def test_fds_namedelement_constructor_exists():
    assert callable(fds_NamedElement.__init__)


def test_fds_namedelement_constructor_args():
    sig = inspect.signature(fds_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fds_namedelement_has_name():
    assert hasattr(fds_NamedElement, "name")
    descriptor = None
    for klass in fds_NamedElement.__mro__:
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



def test_fds_primarykey_is_not_abstract():
    assert not inspect.isabstract(fds_PrimaryKey)


def test_fds_primarykey_constructor_exists():
    assert callable(fds_PrimaryKey.__init__)


def test_fds_primarykey_constructor_args():
    sig = inspect.signature(fds_PrimaryKey.__init__)
    params = list(sig.parameters.keys())



def test_restriction_is_not_abstract():
    assert not inspect.isabstract(Restriction)


def test_restriction_constructor_exists():
    assert callable(Restriction.__init__)


def test_restriction_constructor_args():
    sig = inspect.signature(Restriction.__init__)
    params = list(sig.parameters.keys())



def test_fds_candidatekey_is_not_abstract():
    assert not inspect.isabstract(fds_CandidateKey)


def test_fds_candidatekey_constructor_exists():
    assert callable(fds_CandidateKey.__init__)


def test_fds_candidatekey_constructor_args():
    sig = inspect.signature(fds_CandidateKey.__init__)
    params = list(sig.parameters.keys())



def test_fds_foreignkey_is_not_abstract():
    assert not inspect.isabstract(fds_ForeignKey)


def test_fds_foreignkey_constructor_exists():
    assert callable(fds_ForeignKey.__init__)


def test_fds_foreignkey_constructor_args():
    sig = inspect.signature(fds_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_fds_restrictioncolumn_is_not_abstract():
    assert not inspect.isabstract(fds_RestrictionColumn)


def test_fds_restrictioncolumn_constructor_exists():
    assert callable(fds_RestrictionColumn.__init__)


def test_fds_restrictioncolumn_constructor_args():
    sig = inspect.signature(fds_RestrictionColumn.__init__)
    params = list(sig.parameters.keys())



def test_fds_restriction_is_not_abstract():
    assert not inspect.isabstract(fds_Restriction)


def test_fds_restriction_constructor_exists():
    assert callable(fds_Restriction.__init__)


def test_fds_restriction_constructor_args():
    sig = inspect.signature(fds_Restriction.__init__)
    params = list(sig.parameters.keys())



def test_fds_functionaldependency_is_not_abstract():
    assert not inspect.isabstract(fds_FunctionalDependency)


def test_fds_functionaldependency_constructor_exists():
    assert callable(fds_FunctionalDependency.__init__)


def test_fds_functionaldependency_constructor_args():
    sig = inspect.signature(fds_FunctionalDependency.__init__)
    params = list(sig.parameters.keys())



def test_fds_column_is_not_abstract():
    assert not inspect.isabstract(fds_Column)


def test_fds_column_constructor_exists():
    assert callable(fds_Column.__init__)


def test_fds_column_constructor_args():
    sig = inspect.signature(fds_Column.__init__)
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
fds_Table_strategy = st.builds(
    fds_Table,
)
fds_Database_strategy = st.builds(
    fds_Database,
)
fds_NamedElement_strategy = st.builds(
    fds_NamedElement,
    name=
        safe_text
)
CandidateKey_strategy = st.builds(
    CandidateKey,
)
fds_PrimaryKey_strategy = st.builds(
    fds_PrimaryKey,
)
Restriction_strategy = st.builds(
    Restriction,
)
fds_CandidateKey_strategy = st.builds(
    fds_CandidateKey,
)
fds_ForeignKey_strategy = st.builds(
    fds_ForeignKey,
)
fds_RestrictionColumn_strategy = st.builds(
    fds_RestrictionColumn,
)
fds_Restriction_strategy = st.builds(
    fds_Restriction,
)
fds_FunctionalDependency_strategy = st.builds(
    fds_FunctionalDependency,
)
fds_Column_strategy = st.builds(
    fds_Column,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fds_Table_strategy)
@settings(max_examples=50)
def test_fds_table_instantiation(instance):
    assert isinstance(instance, fds_Table)

@given(instance=fds_Database_strategy)
@settings(max_examples=50)
def test_fds_database_instantiation(instance):
    assert isinstance(instance, fds_Database)

@given(instance=fds_NamedElement_strategy)
@settings(max_examples=50)
def test_fds_namedelement_instantiation(instance):
    assert isinstance(instance, fds_NamedElement)



@given(instance=fds_NamedElement_strategy)
def test_fds_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CandidateKey_strategy)
@settings(max_examples=50)
def test_candidatekey_instantiation(instance):
    assert isinstance(instance, CandidateKey)

@given(instance=fds_PrimaryKey_strategy)
@settings(max_examples=50)
def test_fds_primarykey_instantiation(instance):
    assert isinstance(instance, fds_PrimaryKey)

@given(instance=Restriction_strategy)
@settings(max_examples=50)
def test_restriction_instantiation(instance):
    assert isinstance(instance, Restriction)

@given(instance=fds_CandidateKey_strategy)
@settings(max_examples=50)
def test_fds_candidatekey_instantiation(instance):
    assert isinstance(instance, fds_CandidateKey)

@given(instance=fds_ForeignKey_strategy)
@settings(max_examples=50)
def test_fds_foreignkey_instantiation(instance):
    assert isinstance(instance, fds_ForeignKey)

@given(instance=fds_RestrictionColumn_strategy)
@settings(max_examples=50)
def test_fds_restrictioncolumn_instantiation(instance):
    assert isinstance(instance, fds_RestrictionColumn)

@given(instance=fds_Restriction_strategy)
@settings(max_examples=50)
def test_fds_restriction_instantiation(instance):
    assert isinstance(instance, fds_Restriction)

@given(instance=fds_FunctionalDependency_strategy)
@settings(max_examples=50)
def test_fds_functionaldependency_instantiation(instance):
    assert isinstance(instance, fds_FunctionalDependency)

@given(instance=fds_Column_strategy)
@settings(max_examples=50)
def test_fds_column_instantiation(instance):
    assert isinstance(instance, fds_Column)

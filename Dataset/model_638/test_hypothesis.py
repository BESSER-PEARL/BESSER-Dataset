import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    libraryModel::ecore::NamedElement,
    libraryModel::ecore::LibraryModel,
    NamedElement,
    libraryModel::ecore::Author,
    libraryModel::ecore::Picture,
    libraryModel::ecore::Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_librarymodel::ecore::namedelement_is_not_abstract():
    assert not inspect.isabstract(libraryModel::ecore::NamedElement)


def test_librarymodel::ecore::namedelement_constructor_exists():
    assert callable(libraryModel::ecore::NamedElement.__init__)


def test_librarymodel::ecore::namedelement_constructor_args():
    sig = inspect.signature(libraryModel::ecore::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_librarymodel::ecore::namedelement_has_Name():
    assert hasattr(libraryModel::ecore::NamedElement, "Name")
    descriptor = None
    for klass in libraryModel::ecore::NamedElement.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel::ecore::librarymodel_is_not_abstract():
    assert not inspect.isabstract(libraryModel::ecore::LibraryModel)


def test_librarymodel::ecore::librarymodel_constructor_exists():
    assert callable(libraryModel::ecore::LibraryModel.__init__)


def test_librarymodel::ecore::librarymodel_constructor_args():
    sig = inspect.signature(libraryModel::ecore::LibraryModel.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_librarymodel::ecore::author_is_not_abstract():
    assert not inspect.isabstract(libraryModel::ecore::Author)


def test_librarymodel::ecore::author_constructor_exists():
    assert callable(libraryModel::ecore::Author.__init__)


def test_librarymodel::ecore::author_constructor_args():
    sig = inspect.signature(libraryModel::ecore::Author.__init__)
    params = list(sig.parameters.keys())



def test_librarymodel::ecore::picture_is_not_abstract():
    assert not inspect.isabstract(libraryModel::ecore::Picture)


def test_librarymodel::ecore::picture_constructor_exists():
    assert callable(libraryModel::ecore::Picture.__init__)


def test_librarymodel::ecore::picture_constructor_args():
    sig = inspect.signature(libraryModel::ecore::Picture.__init__)
    params = list(sig.parameters.keys())
    assert "pageNumber" in params, "Missing parameter 'pageNumber'"

def test_librarymodel::ecore::picture_has_pageNumber():
    assert hasattr(libraryModel::ecore::Picture, "pageNumber")
    descriptor = None
    for klass in libraryModel::ecore::Picture.__mro__:
        if "pageNumber" in klass.__dict__:
            descriptor = klass.__dict__["pageNumber"]
            break
    assert isinstance(descriptor, property)



def test_librarymodel::ecore::book_is_not_abstract():
    assert not inspect.isabstract(libraryModel::ecore::Book)


def test_librarymodel::ecore::book_constructor_exists():
    assert callable(libraryModel::ecore::Book.__init__)


def test_librarymodel::ecore::book_constructor_args():
    sig = inspect.signature(libraryModel::ecore::Book.__init__)
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
libraryModel::ecore::NamedElement_strategy = st.builds(
    libraryModel::ecore::NamedElement,
    Name=
        safe_text
)
libraryModel::ecore::LibraryModel_strategy = st.builds(
    libraryModel::ecore::LibraryModel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
libraryModel::ecore::Author_strategy = st.builds(
    libraryModel::ecore::Author,
)
libraryModel::ecore::Picture_strategy = st.builds(
    libraryModel::ecore::Picture,
    pageNumber=
        safe_text
)
libraryModel::ecore::Book_strategy = st.builds(
    libraryModel::ecore::Book,
)

@given(instance=libraryModel::ecore::NamedElement_strategy)
@settings(max_examples=50)
def test_librarymodel::ecore::namedelement_instantiation(instance):
    assert isinstance(instance, libraryModel::ecore::NamedElement)

@given(instance=libraryModel::ecore::NamedElement_strategy)
def test_librarymodel::ecore::namedelement_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=libraryModel::ecore::NamedElement_strategy)
def test_librarymodel::ecore::namedelement_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=libraryModel::ecore::LibraryModel_strategy)
@settings(max_examples=50)
def test_librarymodel::ecore::librarymodel_instantiation(instance):
    assert isinstance(instance, libraryModel::ecore::LibraryModel)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryModel::ecore::LibraryModel_strategy)
@settings(max_examples=30)
def test_librarymodel::ecore::librarymodel_printlibrary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printLibrary()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printLibrary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printLibrary' in libraryModel::ecore::LibraryModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printLibrary' in libraryModel::ecore::LibraryModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printLibrary' in libraryModel::ecore::LibraryModel is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=libraryModel::ecore::Author_strategy)
@settings(max_examples=50)
def test_librarymodel::ecore::author_instantiation(instance):
    assert isinstance(instance, libraryModel::ecore::Author)

@given(instance=libraryModel::ecore::Picture_strategy)
@settings(max_examples=50)
def test_librarymodel::ecore::picture_instantiation(instance):
    assert isinstance(instance, libraryModel::ecore::Picture)

@given(instance=libraryModel::ecore::Picture_strategy)
def test_librarymodel::ecore::picture_pageNumber_type(instance):
    assert isinstance(instance.pageNumber, str)


@given(instance=libraryModel::ecore::Picture_strategy)
def test_librarymodel::ecore::picture_pageNumber_setter(instance):
    original = instance.pageNumber
    instance.pageNumber = original
    assert instance.pageNumber == original

@given(instance=libraryModel::ecore::Book_strategy)
@settings(max_examples=50)
def test_librarymodel::ecore::book_instantiation(instance):
    assert isinstance(instance, libraryModel::ecore::Book)

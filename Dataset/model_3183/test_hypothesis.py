import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    architecture::AtomicType,
    architecture::Binding,
    architecture::Variable,
    architecture::Operation,
    architecture::Architecture,
    architecture::Component,
    architecture::Import,
    architecture::AbstractModel,
    architecture::DomainDeclaration,
    architecture::Model,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_architecture::atomictype_is_not_abstract():
    assert not inspect.isabstract(architecture::AtomicType)


def test_architecture::atomictype_constructor_exists():
    assert callable(architecture::AtomicType.__init__)


def test_architecture::atomictype_constructor_args():
    sig = inspect.signature(architecture::AtomicType.__init__)
    params = list(sig.parameters.keys())
    assert "atomType" in params, "Missing parameter 'atomType'"

def test_architecture::atomictype_has_atomType():
    assert hasattr(architecture::AtomicType, "atomType")
    descriptor = None
    for klass in architecture::AtomicType.__mro__:
        if "atomType" in klass.__dict__:
            descriptor = klass.__dict__["atomType"]
            break
    assert isinstance(descriptor, property)



def test_architecture::binding_is_not_abstract():
    assert not inspect.isabstract(architecture::Binding)


def test_architecture::binding_constructor_exists():
    assert callable(architecture::Binding.__init__)


def test_architecture::binding_constructor_args():
    sig = inspect.signature(architecture::Binding.__init__)
    params = list(sig.parameters.keys())



def test_architecture::variable_is_not_abstract():
    assert not inspect.isabstract(architecture::Variable)


def test_architecture::variable_constructor_exists():
    assert callable(architecture::Variable.__init__)


def test_architecture::variable_constructor_args():
    sig = inspect.signature(architecture::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_architecture::variable_has_name():
    assert hasattr(architecture::Variable, "name")
    descriptor = None
    for klass in architecture::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_architecture::operation_is_not_abstract():
    assert not inspect.isabstract(architecture::Operation)


def test_architecture::operation_constructor_exists():
    assert callable(architecture::Operation.__init__)


def test_architecture::operation_constructor_args():
    sig = inspect.signature(architecture::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_architecture::operation_has_name():
    assert hasattr(architecture::Operation, "name")
    descriptor = None
    for klass in architecture::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_architecture::architecture_is_not_abstract():
    assert not inspect.isabstract(architecture::Architecture)


def test_architecture::architecture_constructor_exists():
    assert callable(architecture::Architecture.__init__)


def test_architecture::architecture_constructor_args():
    sig = inspect.signature(architecture::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_architecture::component_is_not_abstract():
    assert not inspect.isabstract(architecture::Component)


def test_architecture::component_constructor_exists():
    assert callable(architecture::Component.__init__)


def test_architecture::component_constructor_args():
    sig = inspect.signature(architecture::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_architecture::component_has_name():
    assert hasattr(architecture::Component, "name")
    descriptor = None
    for klass in architecture::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_architecture::import_is_not_abstract():
    assert not inspect.isabstract(architecture::Import)


def test_architecture::import_constructor_exists():
    assert callable(architecture::Import.__init__)


def test_architecture::import_constructor_args():
    sig = inspect.signature(architecture::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_architecture::import_has_importedNamespace():
    assert hasattr(architecture::Import, "importedNamespace")
    descriptor = None
    for klass in architecture::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_architecture::abstractmodel_is_not_abstract():
    assert not inspect.isabstract(architecture::AbstractModel)


def test_architecture::abstractmodel_constructor_exists():
    assert callable(architecture::AbstractModel.__init__)


def test_architecture::abstractmodel_constructor_args():
    sig = inspect.signature(architecture::AbstractModel.__init__)
    params = list(sig.parameters.keys())



def test_architecture::domaindeclaration_is_not_abstract():
    assert not inspect.isabstract(architecture::DomainDeclaration)


def test_architecture::domaindeclaration_constructor_exists():
    assert callable(architecture::DomainDeclaration.__init__)


def test_architecture::domaindeclaration_constructor_args():
    sig = inspect.signature(architecture::DomainDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_architecture::domaindeclaration_has_name():
    assert hasattr(architecture::DomainDeclaration, "name")
    descriptor = None
    for klass in architecture::DomainDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_architecture::model_is_not_abstract():
    assert not inspect.isabstract(architecture::Model)


def test_architecture::model_constructor_exists():
    assert callable(architecture::Model.__init__)


def test_architecture::model_constructor_args():
    sig = inspect.signature(architecture::Model.__init__)
    params = list(sig.parameters.keys())

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "Double",
        "Void",
        "INT",
        "STRING",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
architecture::AtomicType_strategy = st.builds(
    architecture::AtomicType,
    atomType=
        safe_text
)
architecture::Binding_strategy = st.builds(
    architecture::Binding,
)
architecture::Variable_strategy = st.builds(
    architecture::Variable,
    name=
        safe_text
)
architecture::Operation_strategy = st.builds(
    architecture::Operation,
    name=
        safe_text
)
architecture::Architecture_strategy = st.builds(
    architecture::Architecture,
)
architecture::Component_strategy = st.builds(
    architecture::Component,
    name=
        safe_text
)
architecture::Import_strategy = st.builds(
    architecture::Import,
    importedNamespace=
        safe_text
)
architecture::AbstractModel_strategy = st.builds(
    architecture::AbstractModel,
)
architecture::DomainDeclaration_strategy = st.builds(
    architecture::DomainDeclaration,
    name=
        safe_text
)
architecture::Model_strategy = st.builds(
    architecture::Model,
)

@given(instance=architecture::AtomicType_strategy)
@settings(max_examples=50)
def test_architecture::atomictype_instantiation(instance):
    assert isinstance(instance, architecture::AtomicType)

@given(instance=architecture::AtomicType_strategy)
def test_architecture::atomictype_atomType_type(instance):
    assert isinstance(instance.atomType, str)


@given(instance=architecture::AtomicType_strategy)
def test_architecture::atomictype_atomType_setter(instance):
    original = instance.atomType
    instance.atomType = original
    assert instance.atomType == original

@given(instance=architecture::Binding_strategy)
@settings(max_examples=50)
def test_architecture::binding_instantiation(instance):
    assert isinstance(instance, architecture::Binding)

@given(instance=architecture::Variable_strategy)
@settings(max_examples=50)
def test_architecture::variable_instantiation(instance):
    assert isinstance(instance, architecture::Variable)

@given(instance=architecture::Variable_strategy)
def test_architecture::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=architecture::Variable_strategy)
def test_architecture::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=architecture::Operation_strategy)
@settings(max_examples=50)
def test_architecture::operation_instantiation(instance):
    assert isinstance(instance, architecture::Operation)

@given(instance=architecture::Operation_strategy)
def test_architecture::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=architecture::Operation_strategy)
def test_architecture::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=architecture::Architecture_strategy)
@settings(max_examples=50)
def test_architecture::architecture_instantiation(instance):
    assert isinstance(instance, architecture::Architecture)

@given(instance=architecture::Component_strategy)
@settings(max_examples=50)
def test_architecture::component_instantiation(instance):
    assert isinstance(instance, architecture::Component)

@given(instance=architecture::Component_strategy)
def test_architecture::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=architecture::Component_strategy)
def test_architecture::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=architecture::Import_strategy)
@settings(max_examples=50)
def test_architecture::import_instantiation(instance):
    assert isinstance(instance, architecture::Import)

@given(instance=architecture::Import_strategy)
def test_architecture::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=architecture::Import_strategy)
def test_architecture::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=architecture::AbstractModel_strategy)
@settings(max_examples=50)
def test_architecture::abstractmodel_instantiation(instance):
    assert isinstance(instance, architecture::AbstractModel)

@given(instance=architecture::DomainDeclaration_strategy)
@settings(max_examples=50)
def test_architecture::domaindeclaration_instantiation(instance):
    assert isinstance(instance, architecture::DomainDeclaration)

@given(instance=architecture::DomainDeclaration_strategy)
def test_architecture::domaindeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=architecture::DomainDeclaration_strategy)
def test_architecture::domaindeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=architecture::Model_strategy)
@settings(max_examples=50)
def test_architecture::model_instantiation(instance):
    assert isinstance(instance, architecture::Model)

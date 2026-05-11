import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    domainmodel::TypeRef,
    domainmodel::TypedElement,
    StructuralFeature,
    domainmodel::Reference,
    domainmodel::Attribute,
    AbstractElement,
    domainmodel::PackageDeclaration,
    domainmodel::Import,
    domainmodel::AbstractElement,
    domainmodel::DomainModel,
    Feature,
    domainmodel::Operation,
    domainmodel::StructuralFeature,
    TypedElement,
    domainmodel::Parameter,
    domainmodel::Feature,
    Type,
    domainmodel::Entity,
    domainmodel::DataType,
    domainmodel::Type,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domainmodel::typeref_is_not_abstract():
    assert not inspect.isabstract(domainmodel::TypeRef)


def test_domainmodel::typeref_constructor_exists():
    assert callable(domainmodel::TypeRef.__init__)


def test_domainmodel::typeref_constructor_args():
    sig = inspect.signature(domainmodel::TypeRef.__init__)
    params = list(sig.parameters.keys())
    assert "multi" in params, "Missing parameter 'multi'"

def test_domainmodel::typeref_has_multi():
    assert hasattr(domainmodel::TypeRef, "multi")
    descriptor = None
    for klass in domainmodel::TypeRef.__mro__:
        if "multi" in klass.__dict__:
            descriptor = klass.__dict__["multi"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::typedelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel::TypedElement)


def test_domainmodel::typedelement_constructor_exists():
    assert callable(domainmodel::TypedElement.__init__)


def test_domainmodel::typedelement_constructor_args():
    sig = inspect.signature(domainmodel::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::typedelement_has_name():
    assert hasattr(domainmodel::TypedElement, "name")
    descriptor = None
    for klass in domainmodel::TypedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::reference_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Reference)


def test_domainmodel::reference_constructor_exists():
    assert callable(domainmodel::Reference.__init__)


def test_domainmodel::reference_constructor_args():
    sig = inspect.signature(domainmodel::Reference.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::attribute_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Attribute)


def test_domainmodel::attribute_constructor_exists():
    assert callable(domainmodel::Attribute.__init__)


def test_domainmodel::attribute_constructor_args():
    sig = inspect.signature(domainmodel::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainmodel::PackageDeclaration)


def test_domainmodel::packagedeclaration_constructor_exists():
    assert callable(domainmodel::PackageDeclaration.__init__)


def test_domainmodel::packagedeclaration_constructor_args():
    sig = inspect.signature(domainmodel::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::packagedeclaration_has_name():
    assert hasattr(domainmodel::PackageDeclaration, "name")
    descriptor = None
    for klass in domainmodel::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::import_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Import)


def test_domainmodel::import_constructor_exists():
    assert callable(domainmodel::Import.__init__)


def test_domainmodel::import_constructor_args():
    sig = inspect.signature(domainmodel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domainmodel::import_has_importedNamespace():
    assert hasattr(domainmodel::Import, "importedNamespace")
    descriptor = None
    for klass in domainmodel::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel::AbstractElement)


def test_domainmodel::abstractelement_constructor_exists():
    assert callable(domainmodel::AbstractElement.__init__)


def test_domainmodel::abstractelement_constructor_args():
    sig = inspect.signature(domainmodel::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainmodel::DomainModel)


def test_domainmodel::domainmodel_constructor_exists():
    assert callable(domainmodel::DomainModel.__init__)


def test_domainmodel::domainmodel_constructor_args():
    sig = inspect.signature(domainmodel::DomainModel.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::operation_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Operation)


def test_domainmodel::operation_constructor_exists():
    assert callable(domainmodel::Operation.__init__)


def test_domainmodel::operation_constructor_args():
    sig = inspect.signature(domainmodel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_domainmodel::operation_has_visibility():
    assert hasattr(domainmodel::Operation, "visibility")
    descriptor = None
    for klass in domainmodel::Operation.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel::StructuralFeature)


def test_domainmodel::structuralfeature_constructor_exists():
    assert callable(domainmodel::StructuralFeature.__init__)


def test_domainmodel::structuralfeature_constructor_args():
    sig = inspect.signature(domainmodel::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::parameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Parameter)


def test_domainmodel::parameter_constructor_exists():
    assert callable(domainmodel::Parameter.__init__)


def test_domainmodel::parameter_constructor_args():
    sig = inspect.signature(domainmodel::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::feature_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Feature)


def test_domainmodel::feature_constructor_exists():
    assert callable(domainmodel::Feature.__init__)


def test_domainmodel::feature_constructor_args():
    sig = inspect.signature(domainmodel::Feature.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::entity_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Entity)


def test_domainmodel::entity_constructor_exists():
    assert callable(domainmodel::Entity.__init__)


def test_domainmodel::entity_constructor_args():
    sig = inspect.signature(domainmodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(domainmodel::DataType)


def test_domainmodel::datatype_constructor_exists():
    assert callable(domainmodel::DataType.__init__)


def test_domainmodel::datatype_constructor_args():
    sig = inspect.signature(domainmodel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::type_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Type)


def test_domainmodel::type_constructor_exists():
    assert callable(domainmodel::Type.__init__)


def test_domainmodel::type_constructor_args():
    sig = inspect.signature(domainmodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::type_has_name():
    assert hasattr(domainmodel::Type, "name")
    descriptor = None
    for klass in domainmodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "private",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
domainmodel::TypeRef_strategy = st.builds(
    domainmodel::TypeRef,
    multi=
        st.booleans()
)
domainmodel::TypedElement_strategy = st.builds(
    domainmodel::TypedElement,
    name=
        safe_text
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
domainmodel::Reference_strategy = st.builds(
    domainmodel::Reference,
)
domainmodel::Attribute_strategy = st.builds(
    domainmodel::Attribute,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainmodel::PackageDeclaration_strategy = st.builds(
    domainmodel::PackageDeclaration,
    name=
        safe_text
)
domainmodel::Import_strategy = st.builds(
    domainmodel::Import,
    importedNamespace=
        safe_text
)
domainmodel::AbstractElement_strategy = st.builds(
    domainmodel::AbstractElement,
)
domainmodel::DomainModel_strategy = st.builds(
    domainmodel::DomainModel,
)
Feature_strategy = st.builds(
    Feature,
)
domainmodel::Operation_strategy = st.builds(
    domainmodel::Operation,
    visibility=
        safe_text
)
domainmodel::StructuralFeature_strategy = st.builds(
    domainmodel::StructuralFeature,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
domainmodel::Parameter_strategy = st.builds(
    domainmodel::Parameter,
)
domainmodel::Feature_strategy = st.builds(
    domainmodel::Feature,
)
Type_strategy = st.builds(
    Type,
)
domainmodel::Entity_strategy = st.builds(
    domainmodel::Entity,
)
domainmodel::DataType_strategy = st.builds(
    domainmodel::DataType,
)
domainmodel::Type_strategy = st.builds(
    domainmodel::Type,
    name=
        safe_text
)

@given(instance=domainmodel::TypeRef_strategy)
@settings(max_examples=50)
def test_domainmodel::typeref_instantiation(instance):
    assert isinstance(instance, domainmodel::TypeRef)

@given(instance=domainmodel::TypeRef_strategy)
def test_domainmodel::typeref_multi_type(instance):
    assert isinstance(instance.multi, bool)


@given(instance=domainmodel::TypeRef_strategy)
def test_domainmodel::typeref_multi_setter(instance):
    original = instance.multi
    instance.multi = original
    assert instance.multi == original

@given(instance=domainmodel::TypedElement_strategy)
@settings(max_examples=50)
def test_domainmodel::typedelement_instantiation(instance):
    assert isinstance(instance, domainmodel::TypedElement)

@given(instance=domainmodel::TypedElement_strategy)
def test_domainmodel::typedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::TypedElement_strategy)
def test_domainmodel::typedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=domainmodel::Reference_strategy)
@settings(max_examples=50)
def test_domainmodel::reference_instantiation(instance):
    assert isinstance(instance, domainmodel::Reference)

@given(instance=domainmodel::Attribute_strategy)
@settings(max_examples=50)
def test_domainmodel::attribute_instantiation(instance):
    assert isinstance(instance, domainmodel::Attribute)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainmodel::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_domainmodel::packagedeclaration_instantiation(instance):
    assert isinstance(instance, domainmodel::PackageDeclaration)

@given(instance=domainmodel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::PackageDeclaration_strategy)
def test_domainmodel::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::Import_strategy)
@settings(max_examples=50)
def test_domainmodel::import_instantiation(instance):
    assert isinstance(instance, domainmodel::Import)

@given(instance=domainmodel::Import_strategy)
def test_domainmodel::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=domainmodel::Import_strategy)
def test_domainmodel::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainmodel::AbstractElement_strategy)
@settings(max_examples=50)
def test_domainmodel::abstractelement_instantiation(instance):
    assert isinstance(instance, domainmodel::AbstractElement)

@given(instance=domainmodel::DomainModel_strategy)
@settings(max_examples=50)
def test_domainmodel::domainmodel_instantiation(instance):
    assert isinstance(instance, domainmodel::DomainModel)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=domainmodel::Operation_strategy)
@settings(max_examples=50)
def test_domainmodel::operation_instantiation(instance):
    assert isinstance(instance, domainmodel::Operation)

@given(instance=domainmodel::Operation_strategy)
def test_domainmodel::operation_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=domainmodel::Operation_strategy)
def test_domainmodel::operation_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=domainmodel::StructuralFeature_strategy)
@settings(max_examples=50)
def test_domainmodel::structuralfeature_instantiation(instance):
    assert isinstance(instance, domainmodel::StructuralFeature)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=domainmodel::Parameter_strategy)
@settings(max_examples=50)
def test_domainmodel::parameter_instantiation(instance):
    assert isinstance(instance, domainmodel::Parameter)

@given(instance=domainmodel::Feature_strategy)
@settings(max_examples=50)
def test_domainmodel::feature_instantiation(instance):
    assert isinstance(instance, domainmodel::Feature)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainmodel::Entity_strategy)
@settings(max_examples=50)
def test_domainmodel::entity_instantiation(instance):
    assert isinstance(instance, domainmodel::Entity)

@given(instance=domainmodel::DataType_strategy)
@settings(max_examples=50)
def test_domainmodel::datatype_instantiation(instance):
    assert isinstance(instance, domainmodel::DataType)

@given(instance=domainmodel::Type_strategy)
@settings(max_examples=50)
def test_domainmodel::type_instantiation(instance):
    assert isinstance(instance, domainmodel::Type)

@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

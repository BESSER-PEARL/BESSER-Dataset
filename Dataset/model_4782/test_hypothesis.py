import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeConstraint,
    types::RangeConstraint,
    ParameterizedType,
    types::ComplexType,
    Type,
    types::ParameterizedType,
    types::TypeParameter,
    types::PrimitiveType,
    PrimitiveType,
    types::EnumerationType,
    types::TypedElement,
    Declaration,
    types::Event,
    types::Property,
    TypedElement,
    types::TypeAlias,
    types::TypeConstraint,
    PackageMember,
    types::Operation,
    types::Type,
    types::Domain,
    NamedElement,
    types::Parameter,
    types::Enumerator,
    types::Declaration,
    types::Package,
    types::PackageMember,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(TypeConstraint)


def test_typeconstraint_constructor_exists():
    assert callable(TypeConstraint.__init__)


def test_typeconstraint_constructor_args():
    sig = inspect.signature(TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_types::rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(types::RangeConstraint)


def test_types::rangeconstraint_constructor_exists():
    assert callable(types::RangeConstraint.__init__)


def test_types::rangeconstraint_constructor_args():
    sig = inspect.signature(types::RangeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_types::rangeconstraint_has_lowerBound():
    assert hasattr(types::RangeConstraint, "lowerBound")
    descriptor = None
    for klass in types::RangeConstraint.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_types::rangeconstraint_has_upperBound():
    assert hasattr(types::RangeConstraint, "upperBound")
    descriptor = None
    for klass in types::RangeConstraint.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ParameterizedType)


def test_parameterizedtype_constructor_exists():
    assert callable(ParameterizedType.__init__)


def test_parameterizedtype_constructor_args():
    sig = inspect.signature(ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_types::complextype_is_not_abstract():
    assert not inspect.isabstract(types::ComplexType)


def test_types::complextype_constructor_exists():
    assert callable(types::ComplexType.__init__)


def test_types::complextype_constructor_args():
    sig = inspect.signature(types::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types::parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(types::ParameterizedType)


def test_types::parameterizedtype_constructor_exists():
    assert callable(types::ParameterizedType.__init__)


def test_types::parameterizedtype_constructor_args():
    sig = inspect.signature(types::ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_types::typeparameter_is_not_abstract():
    assert not inspect.isabstract(types::TypeParameter)


def test_types::typeparameter_constructor_exists():
    assert callable(types::TypeParameter.__init__)


def test_types::typeparameter_constructor_args():
    sig = inspect.signature(types::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumerationType)


def test_types::enumerationtype_constructor_exists():
    assert callable(types::EnumerationType.__init__)


def test_types::enumerationtype_constructor_args():
    sig = inspect.signature(types::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_types::typedelement_is_not_abstract():
    assert not inspect.isabstract(types::TypedElement)


def test_types::typedelement_constructor_exists():
    assert callable(types::TypedElement.__init__)


def test_types::typedelement_constructor_args():
    sig = inspect.signature(types::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_types::event_is_not_abstract():
    assert not inspect.isabstract(types::Event)


def test_types::event_constructor_exists():
    assert callable(types::Event.__init__)


def test_types::event_constructor_args():
    sig = inspect.signature(types::Event.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_types::event_has_direction():
    assert hasattr(types::Event, "direction")
    descriptor = None
    for klass in types::Event.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_types::property_is_not_abstract():
    assert not inspect.isabstract(types::Property)


def test_types::property_constructor_exists():
    assert callable(types::Property.__init__)


def test_types::property_constructor_args():
    sig = inspect.signature(types::Property.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "const" in params, "Missing parameter 'const'"

def test_types::property_has_external():
    assert hasattr(types::Property, "external")
    descriptor = None
    for klass in types::Property.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_types::property_has_readonly():
    assert hasattr(types::Property, "readonly")
    descriptor = None
    for klass in types::Property.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_types::property_has_const():
    assert hasattr(types::Property, "const")
    descriptor = None
    for klass in types::Property.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::typealias_is_not_abstract():
    assert not inspect.isabstract(types::TypeAlias)


def test_types::typealias_constructor_exists():
    assert callable(types::TypeAlias.__init__)


def test_types::typealias_constructor_args():
    sig = inspect.signature(types::TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_types::typeconstraint_is_not_abstract():
    assert not inspect.isabstract(types::TypeConstraint)


def test_types::typeconstraint_constructor_exists():
    assert callable(types::TypeConstraint.__init__)


def test_types::typeconstraint_constructor_args():
    sig = inspect.signature(types::TypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types::typeconstraint_has_value():
    assert hasattr(types::TypeConstraint, "value")
    descriptor = None
    for klass in types::TypeConstraint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_packagemember_is_not_abstract():
    assert not inspect.isabstract(PackageMember)


def test_packagemember_constructor_exists():
    assert callable(PackageMember.__init__)


def test_packagemember_constructor_args():
    sig = inspect.signature(PackageMember.__init__)
    params = list(sig.parameters.keys())



def test_types::operation_is_not_abstract():
    assert not inspect.isabstract(types::Operation)


def test_types::operation_constructor_exists():
    assert callable(types::Operation.__init__)


def test_types::operation_constructor_args():
    sig = inspect.signature(types::Operation.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_types::type_has_abstract():
    assert hasattr(types::Type, "abstract")
    descriptor = None
    for klass in types::Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_types::domain_is_not_abstract():
    assert not inspect.isabstract(types::Domain)


def test_types::domain_constructor_exists():
    assert callable(types::Domain.__init__)


def test_types::domain_constructor_args():
    sig = inspect.signature(types::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "domainID" in params, "Missing parameter 'domainID'"

def test_types::domain_has_domainID():
    assert hasattr(types::Domain, "domainID")
    descriptor = None
    for klass in types::Domain.__mro__:
        if "domainID" in klass.__dict__:
            descriptor = klass.__dict__["domainID"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::parameter_is_not_abstract():
    assert not inspect.isabstract(types::Parameter)


def test_types::parameter_constructor_exists():
    assert callable(types::Parameter.__init__)


def test_types::parameter_constructor_args():
    sig = inspect.signature(types::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_types::enumerator_is_not_abstract():
    assert not inspect.isabstract(types::Enumerator)


def test_types::enumerator_constructor_exists():
    assert callable(types::Enumerator.__init__)


def test_types::enumerator_constructor_args():
    sig = inspect.signature(types::Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_types::enumerator_has_literalValue():
    assert hasattr(types::Enumerator, "literalValue")
    descriptor = None
    for klass in types::Enumerator.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_types::declaration_is_not_abstract():
    assert not inspect.isabstract(types::Declaration)


def test_types::declaration_constructor_exists():
    assert callable(types::Declaration.__init__)


def test_types::declaration_constructor_args():
    sig = inspect.signature(types::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_types::package_is_not_abstract():
    assert not inspect.isabstract(types::Package)


def test_types::package_constructor_exists():
    assert callable(types::Package.__init__)


def test_types::package_constructor_args():
    sig = inspect.signature(types::Package.__init__)
    params = list(sig.parameters.keys())



def test_types::packagemember_is_not_abstract():
    assert not inspect.isabstract(types::PackageMember)


def test_types::packagemember_constructor_exists():
    assert callable(types::PackageMember.__init__)


def test_types::packagemember_constructor_args():
    sig = inspect.signature(types::PackageMember.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "LOCAL",
        "IN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
TypeConstraint_strategy = st.builds(
    TypeConstraint,
)
types::RangeConstraint_strategy = st.builds(
    types::RangeConstraint,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
ParameterizedType_strategy = st.builds(
    ParameterizedType,
)
types::ComplexType_strategy = st.builds(
    types::ComplexType,
)
Type_strategy = st.builds(
    Type,
)
types::ParameterizedType_strategy = st.builds(
    types::ParameterizedType,
)
types::TypeParameter_strategy = st.builds(
    types::TypeParameter,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types::EnumerationType_strategy = st.builds(
    types::EnumerationType,
)
types::TypedElement_strategy = st.builds(
    types::TypedElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
types::Event_strategy = st.builds(
    types::Event,
    direction=
        safe_text
)
types::Property_strategy = st.builds(
    types::Property,
    external=
        st.booleans(),
    readonly=
        st.booleans(),
    const=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
types::TypeAlias_strategy = st.builds(
    types::TypeAlias,
)
types::TypeConstraint_strategy = st.builds(
    types::TypeConstraint,
    value=
        safe_text
)
PackageMember_strategy = st.builds(
    PackageMember,
)
types::Operation_strategy = st.builds(
    types::Operation,
)
types::Type_strategy = st.builds(
    types::Type,
    abstract=
        st.booleans()
)
types::Domain_strategy = st.builds(
    types::Domain,
    domainID=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
types::Parameter_strategy = st.builds(
    types::Parameter,
)
types::Enumerator_strategy = st.builds(
    types::Enumerator,
    literalValue=
        safe_text
)
types::Declaration_strategy = st.builds(
    types::Declaration,
)
types::Package_strategy = st.builds(
    types::Package,
)
types::PackageMember_strategy = st.builds(
    types::PackageMember,
)

@given(instance=TypeConstraint_strategy)
@settings(max_examples=50)
def test_typeconstraint_instantiation(instance):
    assert isinstance(instance, TypeConstraint)

@given(instance=types::RangeConstraint_strategy)
@settings(max_examples=50)
def test_types::rangeconstraint_instantiation(instance):
    assert isinstance(instance, types::RangeConstraint)

@given(instance=types::RangeConstraint_strategy)
def test_types::rangeconstraint_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=types::RangeConstraint_strategy)
def test_types::rangeconstraint_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=types::RangeConstraint_strategy)
def test_types::rangeconstraint_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=types::RangeConstraint_strategy)
def test_types::rangeconstraint_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=ParameterizedType_strategy)
@settings(max_examples=50)
def test_parameterizedtype_instantiation(instance):
    assert isinstance(instance, ParameterizedType)

@given(instance=types::ComplexType_strategy)
@settings(max_examples=50)
def test_types::complextype_instantiation(instance):
    assert isinstance(instance, types::ComplexType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::ParameterizedType_strategy)
@settings(max_examples=50)
def test_types::parameterizedtype_instantiation(instance):
    assert isinstance(instance, types::ParameterizedType)

@given(instance=types::TypeParameter_strategy)
@settings(max_examples=50)
def test_types::typeparameter_instantiation(instance):
    assert isinstance(instance, types::TypeParameter)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types::EnumerationType_strategy)
@settings(max_examples=50)
def test_types::enumerationtype_instantiation(instance):
    assert isinstance(instance, types::EnumerationType)

@given(instance=types::TypedElement_strategy)
@settings(max_examples=50)
def test_types::typedelement_instantiation(instance):
    assert isinstance(instance, types::TypedElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=types::Event_strategy)
@settings(max_examples=50)
def test_types::event_instantiation(instance):
    assert isinstance(instance, types::Event)

@given(instance=types::Event_strategy)
def test_types::event_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=types::Event_strategy)
def test_types::event_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=types::Property_strategy)
@settings(max_examples=50)
def test_types::property_instantiation(instance):
    assert isinstance(instance, types::Property)

@given(instance=types::Property_strategy)
def test_types::property_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=types::Property_strategy)
def test_types::property_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=types::Property_strategy)
def test_types::property_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=types::Property_strategy)
def test_types::property_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=types::Property_strategy)
def test_types::property_const_type(instance):
    assert isinstance(instance.const, bool)


@given(instance=types::Property_strategy)
def test_types::property_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=types::TypeAlias_strategy)
@settings(max_examples=50)
def test_types::typealias_instantiation(instance):
    assert isinstance(instance, types::TypeAlias)

@given(instance=types::TypeConstraint_strategy)
@settings(max_examples=50)
def test_types::typeconstraint_instantiation(instance):
    assert isinstance(instance, types::TypeConstraint)

@given(instance=types::TypeConstraint_strategy)
def test_types::typeconstraint_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=types::TypeConstraint_strategy)
def test_types::typeconstraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PackageMember_strategy)
@settings(max_examples=50)
def test_packagemember_instantiation(instance):
    assert isinstance(instance, PackageMember)

@given(instance=types::Operation_strategy)
@settings(max_examples=50)
def test_types::operation_instantiation(instance):
    assert isinstance(instance, types::Operation)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Type_strategy)
def test_types::type_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=types::Type_strategy)
def test_types::type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types::Domain_strategy)
@settings(max_examples=50)
def test_types::domain_instantiation(instance):
    assert isinstance(instance, types::Domain)

@given(instance=types::Domain_strategy)
def test_types::domain_domainID_type(instance):
    assert isinstance(instance.domainID, str)


@given(instance=types::Domain_strategy)
def test_types::domain_domainID_setter(instance):
    original = instance.domainID
    instance.domainID = original
    assert instance.domainID == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=types::Parameter_strategy)
@settings(max_examples=50)
def test_types::parameter_instantiation(instance):
    assert isinstance(instance, types::Parameter)

@given(instance=types::Enumerator_strategy)
@settings(max_examples=50)
def test_types::enumerator_instantiation(instance):
    assert isinstance(instance, types::Enumerator)

@given(instance=types::Enumerator_strategy)
def test_types::enumerator_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=types::Enumerator_strategy)
def test_types::enumerator_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=types::Declaration_strategy)
@settings(max_examples=50)
def test_types::declaration_instantiation(instance):
    assert isinstance(instance, types::Declaration)

@given(instance=types::Package_strategy)
@settings(max_examples=50)
def test_types::package_instantiation(instance):
    assert isinstance(instance, types::Package)

@given(instance=types::PackageMember_strategy)
@settings(max_examples=50)
def test_types::packagemember_instantiation(instance):
    assert isinstance(instance, types::PackageMember)

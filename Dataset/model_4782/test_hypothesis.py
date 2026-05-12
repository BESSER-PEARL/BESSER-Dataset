import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeConstraint,
    types_RangeConstraint,
    ParameterizedType,
    types_ComplexType,
    Type,
    types_ParameterizedType,
    types_TypeParameter,
    types_PrimitiveType,
    PrimitiveType,
    types_EnumerationType,
    types_TypedElement,
    Declaration,
    types_Event,
    types_Property,
    TypedElement,
    types_TypeAlias,
    types_TypeConstraint,
    PackageMember,
    types_Operation,
    types_Type,
    types_Domain,
    NamedElement,
    types_Parameter,
    types_Enumerator,
    types_Declaration,
    types_Package,
    types_PackageMember,
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



def test_types_rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(types_RangeConstraint)


def test_types_rangeconstraint_constructor_exists():
    assert callable(types_RangeConstraint.__init__)


def test_types_rangeconstraint_constructor_args():
    sig = inspect.signature(types_RangeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_types_rangeconstraint_has_lowerBound():
    assert hasattr(types_RangeConstraint, "lowerBound")
    descriptor = None
    for klass in types_RangeConstraint.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_types_rangeconstraint_has_upperBound():
    assert hasattr(types_RangeConstraint, "upperBound")
    descriptor = None
    for klass in types_RangeConstraint.__mro__:
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



def test_types_complextype_is_not_abstract():
    assert not inspect.isabstract(types_ComplexType)


def test_types_complextype_constructor_exists():
    assert callable(types_ComplexType.__init__)


def test_types_complextype_constructor_args():
    sig = inspect.signature(types_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(types_ParameterizedType)


def test_types_parameterizedtype_constructor_exists():
    assert callable(types_ParameterizedType.__init__)


def test_types_parameterizedtype_constructor_args():
    sig = inspect.signature(types_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_types_typeparameter_is_not_abstract():
    assert not inspect.isabstract(types_TypeParameter)


def test_types_typeparameter_constructor_exists():
    assert callable(types_TypeParameter.__init__)


def test_types_typeparameter_constructor_args():
    sig = inspect.signature(types_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationType)


def test_types_enumerationtype_constructor_exists():
    assert callable(types_EnumerationType.__init__)


def test_types_enumerationtype_constructor_args():
    sig = inspect.signature(types_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_types_typedelement_is_not_abstract():
    assert not inspect.isabstract(types_TypedElement)


def test_types_typedelement_constructor_exists():
    assert callable(types_TypedElement.__init__)


def test_types_typedelement_constructor_args():
    sig = inspect.signature(types_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_types_event_is_not_abstract():
    assert not inspect.isabstract(types_Event)


def test_types_event_constructor_exists():
    assert callable(types_Event.__init__)


def test_types_event_constructor_args():
    sig = inspect.signature(types_Event.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_types_event_has_direction():
    assert hasattr(types_Event, "direction")
    descriptor = None
    for klass in types_Event.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_types_property_is_not_abstract():
    assert not inspect.isabstract(types_Property)


def test_types_property_constructor_exists():
    assert callable(types_Property.__init__)


def test_types_property_constructor_args():
    sig = inspect.signature(types_Property.__init__)
    params = list(sig.parameters.keys())
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "external" in params, "Missing parameter 'external'"
    assert "const" in params, "Missing parameter 'const'"

def test_types_property_has_readonly():
    assert hasattr(types_Property, "readonly")
    descriptor = None
    for klass in types_Property.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_types_property_has_external():
    assert hasattr(types_Property, "external")
    descriptor = None
    for klass in types_Property.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_types_property_has_const():
    assert hasattr(types_Property, "const")
    descriptor = None
    for klass in types_Property.__mro__:
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



def test_types_typealias_is_not_abstract():
    assert not inspect.isabstract(types_TypeAlias)


def test_types_typealias_constructor_exists():
    assert callable(types_TypeAlias.__init__)


def test_types_typealias_constructor_args():
    sig = inspect.signature(types_TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_types_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(types_TypeConstraint)


def test_types_typeconstraint_constructor_exists():
    assert callable(types_TypeConstraint.__init__)


def test_types_typeconstraint_constructor_args():
    sig = inspect.signature(types_TypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types_typeconstraint_has_value():
    assert hasattr(types_TypeConstraint, "value")
    descriptor = None
    for klass in types_TypeConstraint.__mro__:
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



def test_types_operation_is_not_abstract():
    assert not inspect.isabstract(types_Operation)


def test_types_operation_constructor_exists():
    assert callable(types_Operation.__init__)


def test_types_operation_constructor_args():
    sig = inspect.signature(types_Operation.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_types_type_has_abstract():
    assert hasattr(types_Type, "abstract")
    descriptor = None
    for klass in types_Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_types_domain_is_not_abstract():
    assert not inspect.isabstract(types_Domain)


def test_types_domain_constructor_exists():
    assert callable(types_Domain.__init__)


def test_types_domain_constructor_args():
    sig = inspect.signature(types_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "domainID" in params, "Missing parameter 'domainID'"

def test_types_domain_has_domainID():
    assert hasattr(types_Domain, "domainID")
    descriptor = None
    for klass in types_Domain.__mro__:
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



def test_types_parameter_is_not_abstract():
    assert not inspect.isabstract(types_Parameter)


def test_types_parameter_constructor_exists():
    assert callable(types_Parameter.__init__)


def test_types_parameter_constructor_args():
    sig = inspect.signature(types_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_types_enumerator_is_not_abstract():
    assert not inspect.isabstract(types_Enumerator)


def test_types_enumerator_constructor_exists():
    assert callable(types_Enumerator.__init__)


def test_types_enumerator_constructor_args():
    sig = inspect.signature(types_Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_types_enumerator_has_literalValue():
    assert hasattr(types_Enumerator, "literalValue")
    descriptor = None
    for klass in types_Enumerator.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_types_declaration_is_not_abstract():
    assert not inspect.isabstract(types_Declaration)


def test_types_declaration_constructor_exists():
    assert callable(types_Declaration.__init__)


def test_types_declaration_constructor_args():
    sig = inspect.signature(types_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_types_package_is_not_abstract():
    assert not inspect.isabstract(types_Package)


def test_types_package_constructor_exists():
    assert callable(types_Package.__init__)


def test_types_package_constructor_args():
    sig = inspect.signature(types_Package.__init__)
    params = list(sig.parameters.keys())



def test_types_packagemember_is_not_abstract():
    assert not inspect.isabstract(types_PackageMember)


def test_types_packagemember_constructor_exists():
    assert callable(types_PackageMember.__init__)


def test_types_packagemember_constructor_args():
    sig = inspect.signature(types_PackageMember.__init__)
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
types_RangeConstraint_strategy = st.builds(
    types_RangeConstraint,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
ParameterizedType_strategy = st.builds(
    ParameterizedType,
)
types_ComplexType_strategy = st.builds(
    types_ComplexType,
)
Type_strategy = st.builds(
    Type,
)
types_ParameterizedType_strategy = st.builds(
    types_ParameterizedType,
)
types_TypeParameter_strategy = st.builds(
    types_TypeParameter,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types_EnumerationType_strategy = st.builds(
    types_EnumerationType,
)
types_TypedElement_strategy = st.builds(
    types_TypedElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
types_Event_strategy = st.builds(
    types_Event,
    direction=
        safe_text
)
types_Property_strategy = st.builds(
    types_Property,
    readonly=
        st.booleans(),
    external=
        st.booleans(),
    const=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
types_TypeAlias_strategy = st.builds(
    types_TypeAlias,
)
types_TypeConstraint_strategy = st.builds(
    types_TypeConstraint,
    value=
        safe_text
)
PackageMember_strategy = st.builds(
    PackageMember,
)
types_Operation_strategy = st.builds(
    types_Operation,
)
types_Type_strategy = st.builds(
    types_Type,
    abstract=
        st.booleans()
)
types_Domain_strategy = st.builds(
    types_Domain,
    domainID=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
types_Parameter_strategy = st.builds(
    types_Parameter,
)
types_Enumerator_strategy = st.builds(
    types_Enumerator,
    literalValue=
        safe_text
)
types_Declaration_strategy = st.builds(
    types_Declaration,
)
types_Package_strategy = st.builds(
    types_Package,
)
types_PackageMember_strategy = st.builds(
    types_PackageMember,
)

@given(instance=TypeConstraint_strategy)
@settings(max_examples=50)
def test_typeconstraint_instantiation(instance):
    assert isinstance(instance, TypeConstraint)

@given(instance=types_RangeConstraint_strategy)
@settings(max_examples=50)
def test_types_rangeconstraint_instantiation(instance):
    assert isinstance(instance, types_RangeConstraint)



@given(instance=types_RangeConstraint_strategy)
def test_types_rangeconstraint_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=types_RangeConstraint_strategy)
def test_types_rangeconstraint_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=ParameterizedType_strategy)
@settings(max_examples=50)
def test_parameterizedtype_instantiation(instance):
    assert isinstance(instance, ParameterizedType)

@given(instance=types_ComplexType_strategy)
@settings(max_examples=50)
def test_types_complextype_instantiation(instance):
    assert isinstance(instance, types_ComplexType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_ParameterizedType_strategy)
@settings(max_examples=50)
def test_types_parameterizedtype_instantiation(instance):
    assert isinstance(instance, types_ParameterizedType)

@given(instance=types_TypeParameter_strategy)
@settings(max_examples=50)
def test_types_typeparameter_instantiation(instance):
    assert isinstance(instance, types_TypeParameter)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types_EnumerationType_strategy)
@settings(max_examples=50)
def test_types_enumerationtype_instantiation(instance):
    assert isinstance(instance, types_EnumerationType)

@given(instance=types_TypedElement_strategy)
@settings(max_examples=50)
def test_types_typedelement_instantiation(instance):
    assert isinstance(instance, types_TypedElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=types_Event_strategy)
@settings(max_examples=50)
def test_types_event_instantiation(instance):
    assert isinstance(instance, types_Event)



@given(instance=types_Event_strategy)
def test_types_event_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=types_Property_strategy)
@settings(max_examples=50)
def test_types_property_instantiation(instance):
    assert isinstance(instance, types_Property)



@given(instance=types_Property_strategy)
def test_types_property_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original



@given(instance=types_Property_strategy)
def test_types_property_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original



@given(instance=types_Property_strategy)
def test_types_property_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=types_TypeAlias_strategy)
@settings(max_examples=50)
def test_types_typealias_instantiation(instance):
    assert isinstance(instance, types_TypeAlias)

@given(instance=types_TypeConstraint_strategy)
@settings(max_examples=50)
def test_types_typeconstraint_instantiation(instance):
    assert isinstance(instance, types_TypeConstraint)



@given(instance=types_TypeConstraint_strategy)
def test_types_typeconstraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PackageMember_strategy)
@settings(max_examples=50)
def test_packagemember_instantiation(instance):
    assert isinstance(instance, PackageMember)

@given(instance=types_Operation_strategy)
@settings(max_examples=50)
def test_types_operation_instantiation(instance):
    assert isinstance(instance, types_Operation)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)



@given(instance=types_Type_strategy)
def test_types_type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types_Domain_strategy)
@settings(max_examples=50)
def test_types_domain_instantiation(instance):
    assert isinstance(instance, types_Domain)



@given(instance=types_Domain_strategy)
def test_types_domain_domainID_setter(instance):
    original = instance.domainID
    instance.domainID = original
    assert instance.domainID == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=types_Parameter_strategy)
@settings(max_examples=50)
def test_types_parameter_instantiation(instance):
    assert isinstance(instance, types_Parameter)

@given(instance=types_Enumerator_strategy)
@settings(max_examples=50)
def test_types_enumerator_instantiation(instance):
    assert isinstance(instance, types_Enumerator)



@given(instance=types_Enumerator_strategy)
def test_types_enumerator_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=types_Declaration_strategy)
@settings(max_examples=50)
def test_types_declaration_instantiation(instance):
    assert isinstance(instance, types_Declaration)

@given(instance=types_Package_strategy)
@settings(max_examples=50)
def test_types_package_instantiation(instance):
    assert isinstance(instance, types_Package)

@given(instance=types_PackageMember_strategy)
@settings(max_examples=50)
def test_types_packagemember_instantiation(instance):
    assert isinstance(instance, types_PackageMember)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ComplexPrimitivePropertyType,
    datatype::DictionaryPropertyType,
    datatype::EnumLiteral,
    datatype::Constraint,
    PropertyType,
    datatype::ObjectPropertyType,
    datatype::ComplexPrimitivePropertyType,
    datatype::PrimitivePropertyType,
    datatype::PropertyAttribute,
    datatype::PropertyType,
    datatype::ConstraintRule,
    PropertyAttribute,
    datatype::EnumLiteralPropertyAttribute,
    datatype::BooleanPropertyAttribute,
    Model,
    datatype::Type,
    Type,
    datatype::Enum,
    datatype::Entity,
    datatype::Presence,
    datatype::Property,
    EnumLiteralPropertyAttributeType,
    BooleanPropertyAttributeType,
    ConstraintIntervalType,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_complexprimitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(ComplexPrimitivePropertyType)


def test_complexprimitivepropertytype_constructor_exists():
    assert callable(ComplexPrimitivePropertyType.__init__)


def test_complexprimitivepropertytype_constructor_args():
    sig = inspect.signature(ComplexPrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::dictionarypropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype::DictionaryPropertyType)


def test_datatype::dictionarypropertytype_constructor_exists():
    assert callable(datatype::DictionaryPropertyType.__init__)


def test_datatype::dictionarypropertytype_constructor_args():
    sig = inspect.signature(datatype::DictionaryPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::enumliteral_is_not_abstract():
    assert not inspect.isabstract(datatype::EnumLiteral)


def test_datatype::enumliteral_constructor_exists():
    assert callable(datatype::EnumLiteral.__init__)


def test_datatype::enumliteral_constructor_args():
    sig = inspect.signature(datatype::EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_datatype::enumliteral_has_name():
    assert hasattr(datatype::EnumLiteral, "name")
    descriptor = None
    for klass in datatype::EnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatype::enumliteral_has_description():
    assert hasattr(datatype::EnumLiteral, "description")
    descriptor = None
    for klass in datatype::EnumLiteral.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_datatype::constraint_is_not_abstract():
    assert not inspect.isabstract(datatype::Constraint)


def test_datatype::constraint_constructor_exists():
    assert callable(datatype::Constraint.__init__)


def test_datatype::constraint_constructor_args():
    sig = inspect.signature(datatype::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "constraintValues" in params, "Missing parameter 'constraintValues'"
    assert "type" in params, "Missing parameter 'type'"

def test_datatype::constraint_has_constraintValues():
    assert hasattr(datatype::Constraint, "constraintValues")
    descriptor = None
    for klass in datatype::Constraint.__mro__:
        if "constraintValues" in klass.__dict__:
            descriptor = klass.__dict__["constraintValues"]
            break
    assert isinstance(descriptor, property)

def test_datatype::constraint_has_type():
    assert hasattr(datatype::Constraint, "type")
    descriptor = None
    for klass in datatype::Constraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::objectpropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype::ObjectPropertyType)


def test_datatype::objectpropertytype_constructor_exists():
    assert callable(datatype::ObjectPropertyType.__init__)


def test_datatype::objectpropertytype_constructor_args():
    sig = inspect.signature(datatype::ObjectPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::complexprimitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype::ComplexPrimitivePropertyType)


def test_datatype::complexprimitivepropertytype_constructor_exists():
    assert callable(datatype::ComplexPrimitivePropertyType.__init__)


def test_datatype::complexprimitivepropertytype_constructor_args():
    sig = inspect.signature(datatype::ComplexPrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::primitivepropertytype_is_not_abstract():
    assert not inspect.isabstract(datatype::PrimitivePropertyType)


def test_datatype::primitivepropertytype_constructor_exists():
    assert callable(datatype::PrimitivePropertyType.__init__)


def test_datatype::primitivepropertytype_constructor_args():
    sig = inspect.signature(datatype::PrimitivePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_datatype::primitivepropertytype_has_type():
    assert hasattr(datatype::PrimitivePropertyType, "type")
    descriptor = None
    for klass in datatype::PrimitivePropertyType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_datatype::propertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype::PropertyAttribute)


def test_datatype::propertyattribute_constructor_exists():
    assert callable(datatype::PropertyAttribute.__init__)


def test_datatype::propertyattribute_constructor_args():
    sig = inspect.signature(datatype::PropertyAttribute.__init__)
    params = list(sig.parameters.keys())



def test_datatype::propertytype_is_not_abstract():
    assert not inspect.isabstract(datatype::PropertyType)


def test_datatype::propertytype_constructor_exists():
    assert callable(datatype::PropertyType.__init__)


def test_datatype::propertytype_constructor_args():
    sig = inspect.signature(datatype::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_datatype::constraintrule_is_not_abstract():
    assert not inspect.isabstract(datatype::ConstraintRule)


def test_datatype::constraintrule_constructor_exists():
    assert callable(datatype::ConstraintRule.__init__)


def test_datatype::constraintrule_constructor_args():
    sig = inspect.signature(datatype::ConstraintRule.__init__)
    params = list(sig.parameters.keys())



def test_propertyattribute_is_not_abstract():
    assert not inspect.isabstract(PropertyAttribute)


def test_propertyattribute_constructor_exists():
    assert callable(PropertyAttribute.__init__)


def test_propertyattribute_constructor_args():
    sig = inspect.signature(PropertyAttribute.__init__)
    params = list(sig.parameters.keys())



def test_datatype::enumliteralpropertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype::EnumLiteralPropertyAttribute)


def test_datatype::enumliteralpropertyattribute_constructor_exists():
    assert callable(datatype::EnumLiteralPropertyAttribute.__init__)


def test_datatype::enumliteralpropertyattribute_constructor_args():
    sig = inspect.signature(datatype::EnumLiteralPropertyAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_datatype::enumliteralpropertyattribute_has_type():
    assert hasattr(datatype::EnumLiteralPropertyAttribute, "type")
    descriptor = None
    for klass in datatype::EnumLiteralPropertyAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_datatype::booleanpropertyattribute_is_not_abstract():
    assert not inspect.isabstract(datatype::BooleanPropertyAttribute)


def test_datatype::booleanpropertyattribute_constructor_exists():
    assert callable(datatype::BooleanPropertyAttribute.__init__)


def test_datatype::booleanpropertyattribute_constructor_args():
    sig = inspect.signature(datatype::BooleanPropertyAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_datatype::booleanpropertyattribute_has_type():
    assert hasattr(datatype::BooleanPropertyAttribute, "type")
    descriptor = None
    for klass in datatype::BooleanPropertyAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_datatype::booleanpropertyattribute_has_value():
    assert hasattr(datatype::BooleanPropertyAttribute, "value")
    descriptor = None
    for klass in datatype::BooleanPropertyAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_datatype::type_is_not_abstract():
    assert not inspect.isabstract(datatype::Type)


def test_datatype::type_constructor_exists():
    assert callable(datatype::Type.__init__)


def test_datatype::type_constructor_args():
    sig = inspect.signature(datatype::Type.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_datatype::enum_is_not_abstract():
    assert not inspect.isabstract(datatype::Enum)


def test_datatype::enum_constructor_exists():
    assert callable(datatype::Enum.__init__)


def test_datatype::enum_constructor_args():
    sig = inspect.signature(datatype::Enum.__init__)
    params = list(sig.parameters.keys())



def test_datatype::entity_is_not_abstract():
    assert not inspect.isabstract(datatype::Entity)


def test_datatype::entity_constructor_exists():
    assert callable(datatype::Entity.__init__)


def test_datatype::entity_constructor_args():
    sig = inspect.signature(datatype::Entity.__init__)
    params = list(sig.parameters.keys())



def test_datatype::presence_is_not_abstract():
    assert not inspect.isabstract(datatype::Presence)


def test_datatype::presence_constructor_exists():
    assert callable(datatype::Presence.__init__)


def test_datatype::presence_constructor_args():
    sig = inspect.signature(datatype::Presence.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"

def test_datatype::presence_has_mandatory():
    assert hasattr(datatype::Presence, "mandatory")
    descriptor = None
    for klass in datatype::Presence.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)



def test_datatype::property_is_not_abstract():
    assert not inspect.isabstract(datatype::Property)


def test_datatype::property_constructor_exists():
    assert callable(datatype::Property.__init__)


def test_datatype::property_constructor_args():
    sig = inspect.signature(datatype::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "extension" in params, "Missing parameter 'extension'"

def test_datatype::property_has_name():
    assert hasattr(datatype::Property, "name")
    descriptor = None
    for klass in datatype::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatype::property_has_description():
    assert hasattr(datatype::Property, "description")
    descriptor = None
    for klass in datatype::Property.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_datatype::property_has_multiplicity():
    assert hasattr(datatype::Property, "multiplicity")
    descriptor = None
    for klass in datatype::Property.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_datatype::property_has_extension():
    assert hasattr(datatype::Property, "extension")
    descriptor = None
    for klass in datatype::Property.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_enumliteralpropertyattributetype_exists():
    # Check that the Enumeration exists
    assert EnumLiteralPropertyAttributeType is not None

def test_enumliteralpropertyattributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumLiteralPropertyAttributeType]
    expected_literals = [
        "measurementUnit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumLiteralPropertyAttributeType"

def test_booleanpropertyattributetype_exists():
    # Check that the Enumeration exists
    assert BooleanPropertyAttributeType is not None

def test_booleanpropertyattributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanPropertyAttributeType]
    expected_literals = [
        "eventable",
        "writable",
        "readable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanPropertyAttributeType"

def test_constraintintervaltype_exists():
    # Check that the Enumeration exists
    assert ConstraintIntervalType is not None

def test_constraintintervaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintIntervalType]
    expected_literals = [
        "nullable",
        "mimetype",
        "max",
        "default",
        "strlen",
        "regex",
        "scaling",
        "min",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintIntervalType"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "short",
        "int",
        "base64Binary",
        "boolean",
        "datetime",
        "double",
        "string",
        "long",
        "float",
        "byte",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
ComplexPrimitivePropertyType_strategy = st.builds(
    ComplexPrimitivePropertyType,
)
datatype::DictionaryPropertyType_strategy = st.builds(
    datatype::DictionaryPropertyType,
)
datatype::EnumLiteral_strategy = st.builds(
    datatype::EnumLiteral,
    name=
        safe_text,
    description=
        safe_text
)
datatype::Constraint_strategy = st.builds(
    datatype::Constraint,
    constraintValues=
        safe_text,
    type=
        safe_text
)
PropertyType_strategy = st.builds(
    PropertyType,
)
datatype::ObjectPropertyType_strategy = st.builds(
    datatype::ObjectPropertyType,
)
datatype::ComplexPrimitivePropertyType_strategy = st.builds(
    datatype::ComplexPrimitivePropertyType,
)
datatype::PrimitivePropertyType_strategy = st.builds(
    datatype::PrimitivePropertyType,
    type=
        safe_text
)
datatype::PropertyAttribute_strategy = st.builds(
    datatype::PropertyAttribute,
)
datatype::PropertyType_strategy = st.builds(
    datatype::PropertyType,
)
datatype::ConstraintRule_strategy = st.builds(
    datatype::ConstraintRule,
)
PropertyAttribute_strategy = st.builds(
    PropertyAttribute,
)
datatype::EnumLiteralPropertyAttribute_strategy = st.builds(
    datatype::EnumLiteralPropertyAttribute,
    type=
        safe_text
)
datatype::BooleanPropertyAttribute_strategy = st.builds(
    datatype::BooleanPropertyAttribute,
    type=
        safe_text,
    value=
        st.booleans()
)
Model_strategy = st.builds(
    Model,
)
datatype::Type_strategy = st.builds(
    datatype::Type,
)
Type_strategy = st.builds(
    Type,
)
datatype::Enum_strategy = st.builds(
    datatype::Enum,
)
datatype::Entity_strategy = st.builds(
    datatype::Entity,
)
datatype::Presence_strategy = st.builds(
    datatype::Presence,
    mandatory=
        st.booleans()
)
datatype::Property_strategy = st.builds(
    datatype::Property,
    name=
        safe_text,
    description=
        safe_text,
    multiplicity=
        st.booleans(),
    extension=
        st.booleans()
)

@given(instance=ComplexPrimitivePropertyType_strategy)
@settings(max_examples=50)
def test_complexprimitivepropertytype_instantiation(instance):
    assert isinstance(instance, ComplexPrimitivePropertyType)

@given(instance=datatype::DictionaryPropertyType_strategy)
@settings(max_examples=50)
def test_datatype::dictionarypropertytype_instantiation(instance):
    assert isinstance(instance, datatype::DictionaryPropertyType)

@given(instance=datatype::EnumLiteral_strategy)
@settings(max_examples=50)
def test_datatype::enumliteral_instantiation(instance):
    assert isinstance(instance, datatype::EnumLiteral)

@given(instance=datatype::EnumLiteral_strategy)
def test_datatype::enumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatype::EnumLiteral_strategy)
def test_datatype::enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datatype::EnumLiteral_strategy)
def test_datatype::enumliteral_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=datatype::EnumLiteral_strategy)
def test_datatype::enumliteral_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=datatype::Constraint_strategy)
@settings(max_examples=50)
def test_datatype::constraint_instantiation(instance):
    assert isinstance(instance, datatype::Constraint)

@given(instance=datatype::Constraint_strategy)
def test_datatype::constraint_constraintValues_type(instance):
    assert isinstance(instance.constraintValues, str)


@given(instance=datatype::Constraint_strategy)
def test_datatype::constraint_constraintValues_setter(instance):
    original = instance.constraintValues
    instance.constraintValues = original
    assert instance.constraintValues == original

@given(instance=datatype::Constraint_strategy)
def test_datatype::constraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=datatype::Constraint_strategy)
def test_datatype::constraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=datatype::ObjectPropertyType_strategy)
@settings(max_examples=50)
def test_datatype::objectpropertytype_instantiation(instance):
    assert isinstance(instance, datatype::ObjectPropertyType)

@given(instance=datatype::ComplexPrimitivePropertyType_strategy)
@settings(max_examples=50)
def test_datatype::complexprimitivepropertytype_instantiation(instance):
    assert isinstance(instance, datatype::ComplexPrimitivePropertyType)

@given(instance=datatype::PrimitivePropertyType_strategy)
@settings(max_examples=50)
def test_datatype::primitivepropertytype_instantiation(instance):
    assert isinstance(instance, datatype::PrimitivePropertyType)

@given(instance=datatype::PrimitivePropertyType_strategy)
def test_datatype::primitivepropertytype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=datatype::PrimitivePropertyType_strategy)
def test_datatype::primitivepropertytype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=datatype::PropertyAttribute_strategy)
@settings(max_examples=50)
def test_datatype::propertyattribute_instantiation(instance):
    assert isinstance(instance, datatype::PropertyAttribute)

@given(instance=datatype::PropertyType_strategy)
@settings(max_examples=50)
def test_datatype::propertytype_instantiation(instance):
    assert isinstance(instance, datatype::PropertyType)

@given(instance=datatype::ConstraintRule_strategy)
@settings(max_examples=50)
def test_datatype::constraintrule_instantiation(instance):
    assert isinstance(instance, datatype::ConstraintRule)

@given(instance=PropertyAttribute_strategy)
@settings(max_examples=50)
def test_propertyattribute_instantiation(instance):
    assert isinstance(instance, PropertyAttribute)

@given(instance=datatype::EnumLiteralPropertyAttribute_strategy)
@settings(max_examples=50)
def test_datatype::enumliteralpropertyattribute_instantiation(instance):
    assert isinstance(instance, datatype::EnumLiteralPropertyAttribute)

@given(instance=datatype::EnumLiteralPropertyAttribute_strategy)
def test_datatype::enumliteralpropertyattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=datatype::EnumLiteralPropertyAttribute_strategy)
def test_datatype::enumliteralpropertyattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=datatype::BooleanPropertyAttribute_strategy)
@settings(max_examples=50)
def test_datatype::booleanpropertyattribute_instantiation(instance):
    assert isinstance(instance, datatype::BooleanPropertyAttribute)

@given(instance=datatype::BooleanPropertyAttribute_strategy)
def test_datatype::booleanpropertyattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=datatype::BooleanPropertyAttribute_strategy)
def test_datatype::booleanpropertyattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=datatype::BooleanPropertyAttribute_strategy)
def test_datatype::booleanpropertyattribute_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=datatype::BooleanPropertyAttribute_strategy)
def test_datatype::booleanpropertyattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=datatype::Type_strategy)
@settings(max_examples=50)
def test_datatype::type_instantiation(instance):
    assert isinstance(instance, datatype::Type)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=datatype::Enum_strategy)
@settings(max_examples=50)
def test_datatype::enum_instantiation(instance):
    assert isinstance(instance, datatype::Enum)

@given(instance=datatype::Entity_strategy)
@settings(max_examples=50)
def test_datatype::entity_instantiation(instance):
    assert isinstance(instance, datatype::Entity)

@given(instance=datatype::Presence_strategy)
@settings(max_examples=50)
def test_datatype::presence_instantiation(instance):
    assert isinstance(instance, datatype::Presence)

@given(instance=datatype::Presence_strategy)
def test_datatype::presence_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=datatype::Presence_strategy)
def test_datatype::presence_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=datatype::Property_strategy)
@settings(max_examples=50)
def test_datatype::property_instantiation(instance):
    assert isinstance(instance, datatype::Property)

@given(instance=datatype::Property_strategy)
def test_datatype::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datatype::Property_strategy)
def test_datatype::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datatype::Property_strategy)
def test_datatype::property_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=datatype::Property_strategy)
def test_datatype::property_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=datatype::Property_strategy)
def test_datatype::property_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, bool)


@given(instance=datatype::Property_strategy)
def test_datatype::property_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=datatype::Property_strategy)
def test_datatype::property_extension_type(instance):
    assert isinstance(instance.extension, bool)


@given(instance=datatype::Property_strategy)
def test_datatype::property_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

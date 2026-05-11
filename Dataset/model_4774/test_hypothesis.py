import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    types::BooleanLiteral,
    types::NumberLiteral,
    types::CharLiteral,
    types::MappedByReference,
    types::Literal,
    types::PropertyReference,
    types::EntityRelationship,
    types::Property,
    types::EnumerationLiteral,
    ComplexType,
    types::EntityType,
    types::EnumerationType,
    types::StringLiteral,
    NamedType,
    types::PrimitiveType,
    types::DeclarationTypeReference,
    DeclarationTypeReference,
    types::TypeReference,
    Type,
    types::CollectionType,
    types::MapType,
    types::NamedType,
    types::Type,
    types::ComplexType,
    types::Import,
    types::Model,
    TypeStorageModifier,
    PropertyStorageModifier,
    EntityRelationshipKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_types::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(types::BooleanLiteral)


def test_types::booleanliteral_constructor_exists():
    assert callable(types::BooleanLiteral.__init__)


def test_types::booleanliteral_constructor_args():
    sig = inspect.signature(types::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types::booleanliteral_has_value():
    assert hasattr(types::BooleanLiteral, "value")
    descriptor = None
    for klass in types::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types::numberliteral_is_not_abstract():
    assert not inspect.isabstract(types::NumberLiteral)


def test_types::numberliteral_constructor_exists():
    assert callable(types::NumberLiteral.__init__)


def test_types::numberliteral_constructor_args():
    sig = inspect.signature(types::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types::numberliteral_has_value():
    assert hasattr(types::NumberLiteral, "value")
    descriptor = None
    for klass in types::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types::charliteral_is_not_abstract():
    assert not inspect.isabstract(types::CharLiteral)


def test_types::charliteral_constructor_exists():
    assert callable(types::CharLiteral.__init__)


def test_types::charliteral_constructor_args():
    sig = inspect.signature(types::CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types::charliteral_has_value():
    assert hasattr(types::CharLiteral, "value")
    descriptor = None
    for klass in types::CharLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types::mappedbyreference_is_not_abstract():
    assert not inspect.isabstract(types::MappedByReference)


def test_types::mappedbyreference_constructor_exists():
    assert callable(types::MappedByReference.__init__)


def test_types::mappedbyreference_constructor_args():
    sig = inspect.signature(types::MappedByReference.__init__)
    params = list(sig.parameters.keys())



def test_types::literal_is_not_abstract():
    assert not inspect.isabstract(types::Literal)


def test_types::literal_constructor_exists():
    assert callable(types::Literal.__init__)


def test_types::literal_constructor_args():
    sig = inspect.signature(types::Literal.__init__)
    params = list(sig.parameters.keys())



def test_types::propertyreference_is_not_abstract():
    assert not inspect.isabstract(types::PropertyReference)


def test_types::propertyreference_constructor_exists():
    assert callable(types::PropertyReference.__init__)


def test_types::propertyreference_constructor_args():
    sig = inspect.signature(types::PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_types::entityrelationship_is_not_abstract():
    assert not inspect.isabstract(types::EntityRelationship)


def test_types::entityrelationship_constructor_exists():
    assert callable(types::EntityRelationship.__init__)


def test_types::entityrelationship_constructor_args():
    sig = inspect.signature(types::EntityRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_types::entityrelationship_has_kind():
    assert hasattr(types::EntityRelationship, "kind")
    descriptor = None
    for klass in types::EntityRelationship.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_types::property_is_not_abstract():
    assert not inspect.isabstract(types::Property)


def test_types::property_constructor_exists():
    assert callable(types::Property.__init__)


def test_types::property_constructor_args():
    sig = inspect.signature(types::Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"

def test_types::property_has_name():
    assert hasattr(types::Property, "name")
    descriptor = None
    for klass in types::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_types::property_has_storageModifier():
    assert hasattr(types::Property, "storageModifier")
    descriptor = None
    for klass in types::Property.__mro__:
        if "storageModifier" in klass.__dict__:
            descriptor = klass.__dict__["storageModifier"]
            break
    assert isinstance(descriptor, property)



def test_types::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(types::EnumerationLiteral)


def test_types::enumerationliteral_constructor_exists():
    assert callable(types::EnumerationLiteral.__init__)


def test_types::enumerationliteral_constructor_args():
    sig = inspect.signature(types::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::enumerationliteral_has_name():
    assert hasattr(types::EnumerationLiteral, "name")
    descriptor = None
    for klass in types::EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_types::entitytype_is_not_abstract():
    assert not inspect.isabstract(types::EntityType)


def test_types::entitytype_constructor_exists():
    assert callable(types::EntityType.__init__)


def test_types::entitytype_constructor_args():
    sig = inspect.signature(types::EntityType.__init__)
    params = list(sig.parameters.keys())
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"

def test_types::entitytype_has_storageModifier():
    assert hasattr(types::EntityType, "storageModifier")
    descriptor = None
    for klass in types::EntityType.__mro__:
        if "storageModifier" in klass.__dict__:
            descriptor = klass.__dict__["storageModifier"]
            break
    assert isinstance(descriptor, property)



def test_types::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumerationType)


def test_types::enumerationtype_constructor_exists():
    assert callable(types::EnumerationType.__init__)


def test_types::enumerationtype_constructor_args():
    sig = inspect.signature(types::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_types::stringliteral_is_not_abstract():
    assert not inspect.isabstract(types::StringLiteral)


def test_types::stringliteral_constructor_exists():
    assert callable(types::StringLiteral.__init__)


def test_types::stringliteral_constructor_args():
    sig = inspect.signature(types::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types::stringliteral_has_value():
    assert hasattr(types::StringLiteral, "value")
    descriptor = None
    for klass in types::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(types::DeclarationTypeReference)


def test_types::declarationtypereference_constructor_exists():
    assert callable(types::DeclarationTypeReference.__init__)


def test_types::declarationtypereference_constructor_args():
    sig = inspect.signature(types::DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(DeclarationTypeReference)


def test_declarationtypereference_constructor_exists():
    assert callable(DeclarationTypeReference.__init__)


def test_declarationtypereference_constructor_args():
    sig = inspect.signature(DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types::typereference_is_not_abstract():
    assert not inspect.isabstract(types::TypeReference)


def test_types::typereference_constructor_exists():
    assert callable(types::TypeReference.__init__)


def test_types::typereference_constructor_args():
    sig = inspect.signature(types::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types::collectiontype_is_not_abstract():
    assert not inspect.isabstract(types::CollectionType)


def test_types::collectiontype_constructor_exists():
    assert callable(types::CollectionType.__init__)


def test_types::collectiontype_constructor_args():
    sig = inspect.signature(types::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types::collectiontype_has_size():
    assert hasattr(types::CollectionType, "size")
    descriptor = None
    for klass in types::CollectionType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types::maptype_is_not_abstract():
    assert not inspect.isabstract(types::MapType)


def test_types::maptype_constructor_exists():
    assert callable(types::MapType.__init__)


def test_types::maptype_constructor_args():
    sig = inspect.signature(types::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types::maptype_has_size():
    assert hasattr(types::MapType, "size")
    descriptor = None
    for klass in types::MapType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types::namedtype_is_not_abstract():
    assert not inspect.isabstract(types::NamedType)


def test_types::namedtype_constructor_exists():
    assert callable(types::NamedType.__init__)


def test_types::namedtype_constructor_args():
    sig = inspect.signature(types::NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::namedtype_has_name():
    assert hasattr(types::NamedType, "name")
    descriptor = None
    for klass in types::NamedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())



def test_types::complextype_is_not_abstract():
    assert not inspect.isabstract(types::ComplexType)


def test_types::complextype_constructor_exists():
    assert callable(types::ComplexType.__init__)


def test_types::complextype_constructor_args():
    sig = inspect.signature(types::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_types::import_is_not_abstract():
    assert not inspect.isabstract(types::Import)


def test_types::import_constructor_exists():
    assert callable(types::Import.__init__)


def test_types::import_constructor_args():
    sig = inspect.signature(types::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_types::import_has_importedNamespace():
    assert hasattr(types::Import, "importedNamespace")
    descriptor = None
    for klass in types::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_types::model_is_not_abstract():
    assert not inspect.isabstract(types::Model)


def test_types::model_constructor_exists():
    assert callable(types::Model.__init__)


def test_types::model_constructor_args():
    sig = inspect.signature(types::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types::model_has_name():
    assert hasattr(types::Model, "name")
    descriptor = None
    for klass in types::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typestoragemodifier_exists():
    # Check that the Enumeration exists
    assert TypeStorageModifier is not None

def test_typestoragemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeStorageModifier]
    expected_literals = [
        "EMBEDDABLE",
        "STORABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeStorageModifier"

def test_propertystoragemodifier_exists():
    # Check that the Enumeration exists
    assert PropertyStorageModifier is not None

def test_propertystoragemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PropertyStorageModifier]
    expected_literals = [
        "VARIABLE",
        "VALUE",
        "TRANSIENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PropertyStorageModifier"

def test_entityrelationshipkind_exists():
    # Check that the Enumeration exists
    assert EntityRelationshipKind is not None

def test_entityrelationshipkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityRelationshipKind]
    expected_literals = [
        "UNIQUE",
        "MANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityRelationshipKind"


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
Literal_strategy = st.builds(
    Literal,
)
types::BooleanLiteral_strategy = st.builds(
    types::BooleanLiteral,
    value=
        st.booleans()
)
types::NumberLiteral_strategy = st.builds(
    types::NumberLiteral,
    value=
        safe_text
)
types::CharLiteral_strategy = st.builds(
    types::CharLiteral,
    value=
        safe_text
)
types::MappedByReference_strategy = st.builds(
    types::MappedByReference,
)
types::Literal_strategy = st.builds(
    types::Literal,
)
types::PropertyReference_strategy = st.builds(
    types::PropertyReference,
)
types::EntityRelationship_strategy = st.builds(
    types::EntityRelationship,
    kind=
        safe_text
)
types::Property_strategy = st.builds(
    types::Property,
    name=
        safe_text,
    storageModifier=
        safe_text
)
types::EnumerationLiteral_strategy = st.builds(
    types::EnumerationLiteral,
    name=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
types::EntityType_strategy = st.builds(
    types::EntityType,
    storageModifier=
        safe_text
)
types::EnumerationType_strategy = st.builds(
    types::EnumerationType,
)
types::StringLiteral_strategy = st.builds(
    types::StringLiteral,
    value=
        safe_text
)
NamedType_strategy = st.builds(
    NamedType,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
types::DeclarationTypeReference_strategy = st.builds(
    types::DeclarationTypeReference,
)
DeclarationTypeReference_strategy = st.builds(
    DeclarationTypeReference,
)
types::TypeReference_strategy = st.builds(
    types::TypeReference,
)
Type_strategy = st.builds(
    Type,
)
types::CollectionType_strategy = st.builds(
    types::CollectionType,
    size=
        st.integers()
)
types::MapType_strategy = st.builds(
    types::MapType,
    size=
        st.integers()
)
types::NamedType_strategy = st.builds(
    types::NamedType,
    name=
        safe_text
)
types::Type_strategy = st.builds(
    types::Type,
)
types::ComplexType_strategy = st.builds(
    types::ComplexType,
)
types::Import_strategy = st.builds(
    types::Import,
    importedNamespace=
        safe_text
)
types::Model_strategy = st.builds(
    types::Model,
    name=
        safe_text
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=types::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_types::booleanliteral_instantiation(instance):
    assert isinstance(instance, types::BooleanLiteral)

@given(instance=types::BooleanLiteral_strategy)
def test_types::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=types::BooleanLiteral_strategy)
def test_types::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types::NumberLiteral_strategy)
@settings(max_examples=50)
def test_types::numberliteral_instantiation(instance):
    assert isinstance(instance, types::NumberLiteral)

@given(instance=types::NumberLiteral_strategy)
def test_types::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=types::NumberLiteral_strategy)
def test_types::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types::CharLiteral_strategy)
@settings(max_examples=50)
def test_types::charliteral_instantiation(instance):
    assert isinstance(instance, types::CharLiteral)

@given(instance=types::CharLiteral_strategy)
def test_types::charliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=types::CharLiteral_strategy)
def test_types::charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types::MappedByReference_strategy)
@settings(max_examples=50)
def test_types::mappedbyreference_instantiation(instance):
    assert isinstance(instance, types::MappedByReference)

@given(instance=types::Literal_strategy)
@settings(max_examples=50)
def test_types::literal_instantiation(instance):
    assert isinstance(instance, types::Literal)

@given(instance=types::PropertyReference_strategy)
@settings(max_examples=50)
def test_types::propertyreference_instantiation(instance):
    assert isinstance(instance, types::PropertyReference)

@given(instance=types::EntityRelationship_strategy)
@settings(max_examples=50)
def test_types::entityrelationship_instantiation(instance):
    assert isinstance(instance, types::EntityRelationship)

@given(instance=types::EntityRelationship_strategy)
def test_types::entityrelationship_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=types::EntityRelationship_strategy)
def test_types::entityrelationship_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=types::Property_strategy)
@settings(max_examples=50)
def test_types::property_instantiation(instance):
    assert isinstance(instance, types::Property)

@given(instance=types::Property_strategy)
def test_types::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Property_strategy)
def test_types::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::Property_strategy)
def test_types::property_storageModifier_type(instance):
    assert isinstance(instance.storageModifier, str)


@given(instance=types::Property_strategy)
def test_types::property_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original

@given(instance=types::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_types::enumerationliteral_instantiation(instance):
    assert isinstance(instance, types::EnumerationLiteral)

@given(instance=types::EnumerationLiteral_strategy)
def test_types::enumerationliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::EnumerationLiteral_strategy)
def test_types::enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=types::EntityType_strategy)
@settings(max_examples=50)
def test_types::entitytype_instantiation(instance):
    assert isinstance(instance, types::EntityType)

@given(instance=types::EntityType_strategy)
def test_types::entitytype_storageModifier_type(instance):
    assert isinstance(instance.storageModifier, str)


@given(instance=types::EntityType_strategy)
def test_types::entitytype_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original

@given(instance=types::EnumerationType_strategy)
@settings(max_examples=50)
def test_types::enumerationtype_instantiation(instance):
    assert isinstance(instance, types::EnumerationType)

@given(instance=types::StringLiteral_strategy)
@settings(max_examples=50)
def test_types::stringliteral_instantiation(instance):
    assert isinstance(instance, types::StringLiteral)

@given(instance=types::StringLiteral_strategy)
def test_types::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=types::StringLiteral_strategy)
def test_types::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=types::DeclarationTypeReference_strategy)
@settings(max_examples=50)
def test_types::declarationtypereference_instantiation(instance):
    assert isinstance(instance, types::DeclarationTypeReference)

@given(instance=DeclarationTypeReference_strategy)
@settings(max_examples=50)
def test_declarationtypereference_instantiation(instance):
    assert isinstance(instance, DeclarationTypeReference)

@given(instance=types::TypeReference_strategy)
@settings(max_examples=50)
def test_types::typereference_instantiation(instance):
    assert isinstance(instance, types::TypeReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::CollectionType_strategy)
@settings(max_examples=50)
def test_types::collectiontype_instantiation(instance):
    assert isinstance(instance, types::CollectionType)

@given(instance=types::CollectionType_strategy)
def test_types::collectiontype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=types::CollectionType_strategy)
def test_types::collectiontype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types::MapType_strategy)
@settings(max_examples=50)
def test_types::maptype_instantiation(instance):
    assert isinstance(instance, types::MapType)

@given(instance=types::MapType_strategy)
def test_types::maptype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=types::MapType_strategy)
def test_types::maptype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types::NamedType_strategy)
@settings(max_examples=50)
def test_types::namedtype_instantiation(instance):
    assert isinstance(instance, types::NamedType)

@given(instance=types::NamedType_strategy)
def test_types::namedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::NamedType_strategy)
def test_types::namedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::ComplexType_strategy)
@settings(max_examples=50)
def test_types::complextype_instantiation(instance):
    assert isinstance(instance, types::ComplexType)

@given(instance=types::Import_strategy)
@settings(max_examples=50)
def test_types::import_instantiation(instance):
    assert isinstance(instance, types::Import)

@given(instance=types::Import_strategy)
def test_types::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=types::Import_strategy)
def test_types::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=types::Model_strategy)
@settings(max_examples=50)
def test_types::model_instantiation(instance):
    assert isinstance(instance, types::Model)

@given(instance=types::Model_strategy)
def test_types::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=types::Model_strategy)
def test_types::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

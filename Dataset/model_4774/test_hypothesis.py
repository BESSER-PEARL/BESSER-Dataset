import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    types_CharLiteral,
    types_BooleanLiteral,
    types_NumberLiteral,
    types_MappedByReference,
    types_Literal,
    types_PropertyReference,
    types_EntityRelationship,
    types_Property,
    types_EnumerationLiteral,
    ComplexType,
    types_EntityType,
    types_EnumerationType,
    types_StringLiteral,
    NamedType,
    types_PrimitiveType,
    types_DeclarationTypeReference,
    DeclarationTypeReference,
    types_TypeReference,
    Type,
    types_MapType,
    types_CollectionType,
    types_NamedType,
    types_Type,
    types_ComplexType,
    types_Import,
    types_Model,
    TypeStorageModifier,
    EntityRelationshipKind,
    PropertyStorageModifier,
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



def test_types_charliteral_is_not_abstract():
    assert not inspect.isabstract(types_CharLiteral)


def test_types_charliteral_constructor_exists():
    assert callable(types_CharLiteral.__init__)


def test_types_charliteral_constructor_args():
    sig = inspect.signature(types_CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types_charliteral_has_value():
    assert hasattr(types_CharLiteral, "value")
    descriptor = None
    for klass in types_CharLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(types_BooleanLiteral)


def test_types_booleanliteral_constructor_exists():
    assert callable(types_BooleanLiteral.__init__)


def test_types_booleanliteral_constructor_args():
    sig = inspect.signature(types_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types_booleanliteral_has_value():
    assert hasattr(types_BooleanLiteral, "value")
    descriptor = None
    for klass in types_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types_numberliteral_is_not_abstract():
    assert not inspect.isabstract(types_NumberLiteral)


def test_types_numberliteral_constructor_exists():
    assert callable(types_NumberLiteral.__init__)


def test_types_numberliteral_constructor_args():
    sig = inspect.signature(types_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types_numberliteral_has_value():
    assert hasattr(types_NumberLiteral, "value")
    descriptor = None
    for klass in types_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_types_mappedbyreference_is_not_abstract():
    assert not inspect.isabstract(types_MappedByReference)


def test_types_mappedbyreference_constructor_exists():
    assert callable(types_MappedByReference.__init__)


def test_types_mappedbyreference_constructor_args():
    sig = inspect.signature(types_MappedByReference.__init__)
    params = list(sig.parameters.keys())



def test_types_literal_is_not_abstract():
    assert not inspect.isabstract(types_Literal)


def test_types_literal_constructor_exists():
    assert callable(types_Literal.__init__)


def test_types_literal_constructor_args():
    sig = inspect.signature(types_Literal.__init__)
    params = list(sig.parameters.keys())



def test_types_propertyreference_is_not_abstract():
    assert not inspect.isabstract(types_PropertyReference)


def test_types_propertyreference_constructor_exists():
    assert callable(types_PropertyReference.__init__)


def test_types_propertyreference_constructor_args():
    sig = inspect.signature(types_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_types_entityrelationship_is_not_abstract():
    assert not inspect.isabstract(types_EntityRelationship)


def test_types_entityrelationship_constructor_exists():
    assert callable(types_EntityRelationship.__init__)


def test_types_entityrelationship_constructor_args():
    sig = inspect.signature(types_EntityRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_types_entityrelationship_has_kind():
    assert hasattr(types_EntityRelationship, "kind")
    descriptor = None
    for klass in types_EntityRelationship.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_types_property_is_not_abstract():
    assert not inspect.isabstract(types_Property)


def test_types_property_constructor_exists():
    assert callable(types_Property.__init__)


def test_types_property_constructor_args():
    sig = inspect.signature(types_Property.__init__)
    params = list(sig.parameters.keys())
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_types_property_has_storageModifier():
    assert hasattr(types_Property, "storageModifier")
    descriptor = None
    for klass in types_Property.__mro__:
        if "storageModifier" in klass.__dict__:
            descriptor = klass.__dict__["storageModifier"]
            break
    assert isinstance(descriptor, property)

def test_types_property_has_name():
    assert hasattr(types_Property, "name")
    descriptor = None
    for klass in types_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationLiteral)


def test_types_enumerationliteral_constructor_exists():
    assert callable(types_EnumerationLiteral.__init__)


def test_types_enumerationliteral_constructor_args():
    sig = inspect.signature(types_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_enumerationliteral_has_name():
    assert hasattr(types_EnumerationLiteral, "name")
    descriptor = None
    for klass in types_EnumerationLiteral.__mro__:
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



def test_types_entitytype_is_not_abstract():
    assert not inspect.isabstract(types_EntityType)


def test_types_entitytype_constructor_exists():
    assert callable(types_EntityType.__init__)


def test_types_entitytype_constructor_args():
    sig = inspect.signature(types_EntityType.__init__)
    params = list(sig.parameters.keys())
    assert "storageModifier" in params, "Missing parameter 'storageModifier'"

def test_types_entitytype_has_storageModifier():
    assert hasattr(types_EntityType, "storageModifier")
    descriptor = None
    for klass in types_EntityType.__mro__:
        if "storageModifier" in klass.__dict__:
            descriptor = klass.__dict__["storageModifier"]
            break
    assert isinstance(descriptor, property)



def test_types_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationType)


def test_types_enumerationtype_constructor_exists():
    assert callable(types_EnumerationType.__init__)


def test_types_enumerationtype_constructor_args():
    sig = inspect.signature(types_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_types_stringliteral_is_not_abstract():
    assert not inspect.isabstract(types_StringLiteral)


def test_types_stringliteral_constructor_exists():
    assert callable(types_StringLiteral.__init__)


def test_types_stringliteral_constructor_args():
    sig = inspect.signature(types_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_types_stringliteral_has_value():
    assert hasattr(types_StringLiteral, "value")
    descriptor = None
    for klass in types_StringLiteral.__mro__:
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



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types_declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(types_DeclarationTypeReference)


def test_types_declarationtypereference_constructor_exists():
    assert callable(types_DeclarationTypeReference.__init__)


def test_types_declarationtypereference_constructor_args():
    sig = inspect.signature(types_DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_declarationtypereference_is_not_abstract():
    assert not inspect.isabstract(DeclarationTypeReference)


def test_declarationtypereference_constructor_exists():
    assert callable(DeclarationTypeReference.__init__)


def test_declarationtypereference_constructor_args():
    sig = inspect.signature(DeclarationTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_types_typereference_is_not_abstract():
    assert not inspect.isabstract(types_TypeReference)


def test_types_typereference_constructor_exists():
    assert callable(types_TypeReference.__init__)


def test_types_typereference_constructor_args():
    sig = inspect.signature(types_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_maptype_is_not_abstract():
    assert not inspect.isabstract(types_MapType)


def test_types_maptype_constructor_exists():
    assert callable(types_MapType.__init__)


def test_types_maptype_constructor_args():
    sig = inspect.signature(types_MapType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types_maptype_has_size():
    assert hasattr(types_MapType, "size")
    descriptor = None
    for klass in types_MapType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types_collectiontype_is_not_abstract():
    assert not inspect.isabstract(types_CollectionType)


def test_types_collectiontype_constructor_exists():
    assert callable(types_CollectionType.__init__)


def test_types_collectiontype_constructor_args():
    sig = inspect.signature(types_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types_collectiontype_has_size():
    assert hasattr(types_CollectionType, "size")
    descriptor = None
    for klass in types_CollectionType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types_namedtype_is_not_abstract():
    assert not inspect.isabstract(types_NamedType)


def test_types_namedtype_constructor_exists():
    assert callable(types_NamedType.__init__)


def test_types_namedtype_constructor_args():
    sig = inspect.signature(types_NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_namedtype_has_name():
    assert hasattr(types_NamedType, "name")
    descriptor = None
    for klass in types_NamedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_types_complextype_is_not_abstract():
    assert not inspect.isabstract(types_ComplexType)


def test_types_complextype_constructor_exists():
    assert callable(types_ComplexType.__init__)


def test_types_complextype_constructor_args():
    sig = inspect.signature(types_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_types_import_is_not_abstract():
    assert not inspect.isabstract(types_Import)


def test_types_import_constructor_exists():
    assert callable(types_Import.__init__)


def test_types_import_constructor_args():
    sig = inspect.signature(types_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_types_import_has_importedNamespace():
    assert hasattr(types_Import, "importedNamespace")
    descriptor = None
    for klass in types_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_types_model_is_not_abstract():
    assert not inspect.isabstract(types_Model)


def test_types_model_constructor_exists():
    assert callable(types_Model.__init__)


def test_types_model_constructor_args():
    sig = inspect.signature(types_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_types_model_has_name():
    assert hasattr(types_Model, "name")
    descriptor = None
    for klass in types_Model.__mro__:
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
        "STORABLE",
        "EMBEDDABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeStorageModifier"

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

def test_propertystoragemodifier_exists():
    # Check that the Enumeration exists
    assert PropertyStorageModifier is not None

def test_propertystoragemodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PropertyStorageModifier]
    expected_literals = [
        "VARIABLE",
        "TRANSIENT",
        "VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PropertyStorageModifier"


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
types_CharLiteral_strategy = st.builds(
    types_CharLiteral,
    value=
        safe_text
)
types_BooleanLiteral_strategy = st.builds(
    types_BooleanLiteral,
    value=
        st.booleans()
)
types_NumberLiteral_strategy = st.builds(
    types_NumberLiteral,
    value=
        safe_text
)
types_MappedByReference_strategy = st.builds(
    types_MappedByReference,
)
types_Literal_strategy = st.builds(
    types_Literal,
)
types_PropertyReference_strategy = st.builds(
    types_PropertyReference,
)
types_EntityRelationship_strategy = st.builds(
    types_EntityRelationship,
    kind=
        safe_text
)
types_Property_strategy = st.builds(
    types_Property,
    storageModifier=
        safe_text,
    name=
        safe_text
)
types_EnumerationLiteral_strategy = st.builds(
    types_EnumerationLiteral,
    name=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
types_EntityType_strategy = st.builds(
    types_EntityType,
    storageModifier=
        safe_text
)
types_EnumerationType_strategy = st.builds(
    types_EnumerationType,
)
types_StringLiteral_strategy = st.builds(
    types_StringLiteral,
    value=
        safe_text
)
NamedType_strategy = st.builds(
    NamedType,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
types_DeclarationTypeReference_strategy = st.builds(
    types_DeclarationTypeReference,
)
DeclarationTypeReference_strategy = st.builds(
    DeclarationTypeReference,
)
types_TypeReference_strategy = st.builds(
    types_TypeReference,
)
Type_strategy = st.builds(
    Type,
)
types_MapType_strategy = st.builds(
    types_MapType,
    size=
        st.integers()
)
types_CollectionType_strategy = st.builds(
    types_CollectionType,
    size=
        st.integers()
)
types_NamedType_strategy = st.builds(
    types_NamedType,
    name=
        safe_text
)
types_Type_strategy = st.builds(
    types_Type,
)
types_ComplexType_strategy = st.builds(
    types_ComplexType,
)
types_Import_strategy = st.builds(
    types_Import,
    importedNamespace=
        safe_text
)
types_Model_strategy = st.builds(
    types_Model,
    name=
        safe_text
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=types_CharLiteral_strategy)
@settings(max_examples=50)
def test_types_charliteral_instantiation(instance):
    assert isinstance(instance, types_CharLiteral)



@given(instance=types_CharLiteral_strategy)
def test_types_charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_types_booleanliteral_instantiation(instance):
    assert isinstance(instance, types_BooleanLiteral)



@given(instance=types_BooleanLiteral_strategy)
def test_types_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types_NumberLiteral_strategy)
@settings(max_examples=50)
def test_types_numberliteral_instantiation(instance):
    assert isinstance(instance, types_NumberLiteral)



@given(instance=types_NumberLiteral_strategy)
def test_types_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=types_MappedByReference_strategy)
@settings(max_examples=50)
def test_types_mappedbyreference_instantiation(instance):
    assert isinstance(instance, types_MappedByReference)

@given(instance=types_Literal_strategy)
@settings(max_examples=50)
def test_types_literal_instantiation(instance):
    assert isinstance(instance, types_Literal)

@given(instance=types_PropertyReference_strategy)
@settings(max_examples=50)
def test_types_propertyreference_instantiation(instance):
    assert isinstance(instance, types_PropertyReference)

@given(instance=types_EntityRelationship_strategy)
@settings(max_examples=50)
def test_types_entityrelationship_instantiation(instance):
    assert isinstance(instance, types_EntityRelationship)



@given(instance=types_EntityRelationship_strategy)
def test_types_entityrelationship_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=types_Property_strategy)
@settings(max_examples=50)
def test_types_property_instantiation(instance):
    assert isinstance(instance, types_Property)



@given(instance=types_Property_strategy)
def test_types_property_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original



@given(instance=types_Property_strategy)
def test_types_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_types_enumerationliteral_instantiation(instance):
    assert isinstance(instance, types_EnumerationLiteral)



@given(instance=types_EnumerationLiteral_strategy)
def test_types_enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=types_EntityType_strategy)
@settings(max_examples=50)
def test_types_entitytype_instantiation(instance):
    assert isinstance(instance, types_EntityType)



@given(instance=types_EntityType_strategy)
def test_types_entitytype_storageModifier_setter(instance):
    original = instance.storageModifier
    instance.storageModifier = original
    assert instance.storageModifier == original

@given(instance=types_EnumerationType_strategy)
@settings(max_examples=50)
def test_types_enumerationtype_instantiation(instance):
    assert isinstance(instance, types_EnumerationType)

@given(instance=types_StringLiteral_strategy)
@settings(max_examples=50)
def test_types_stringliteral_instantiation(instance):
    assert isinstance(instance, types_StringLiteral)



@given(instance=types_StringLiteral_strategy)
def test_types_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

@given(instance=types_DeclarationTypeReference_strategy)
@settings(max_examples=50)
def test_types_declarationtypereference_instantiation(instance):
    assert isinstance(instance, types_DeclarationTypeReference)

@given(instance=DeclarationTypeReference_strategy)
@settings(max_examples=50)
def test_declarationtypereference_instantiation(instance):
    assert isinstance(instance, DeclarationTypeReference)

@given(instance=types_TypeReference_strategy)
@settings(max_examples=50)
def test_types_typereference_instantiation(instance):
    assert isinstance(instance, types_TypeReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_MapType_strategy)
@settings(max_examples=50)
def test_types_maptype_instantiation(instance):
    assert isinstance(instance, types_MapType)



@given(instance=types_MapType_strategy)
def test_types_maptype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types_CollectionType_strategy)
@settings(max_examples=50)
def test_types_collectiontype_instantiation(instance):
    assert isinstance(instance, types_CollectionType)



@given(instance=types_CollectionType_strategy)
def test_types_collectiontype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types_NamedType_strategy)
@settings(max_examples=50)
def test_types_namedtype_instantiation(instance):
    assert isinstance(instance, types_NamedType)



@given(instance=types_NamedType_strategy)
def test_types_namedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)

@given(instance=types_ComplexType_strategy)
@settings(max_examples=50)
def test_types_complextype_instantiation(instance):
    assert isinstance(instance, types_ComplexType)

@given(instance=types_Import_strategy)
@settings(max_examples=50)
def test_types_import_instantiation(instance):
    assert isinstance(instance, types_Import)



@given(instance=types_Import_strategy)
def test_types_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=types_Model_strategy)
@settings(max_examples=50)
def test_types_model_instantiation(instance):
    assert isinstance(instance, types_Model)



@given(instance=types_Model_strategy)
def test_types_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

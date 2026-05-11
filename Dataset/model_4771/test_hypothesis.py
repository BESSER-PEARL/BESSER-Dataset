import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RealType,
    eol::types::IntegerType,
    PrimitiveType,
    eol::types::RealType,
    eol::types::StringType,
    eol::types::BooleanType,
    OrderedCollectionType,
    eol::types::SequenceType,
    UniqueCollectionType,
    eol::types::OrderedSetType,
    eol::types::SetType,
    CollectionType,
    eol::types::OrderedCollectionType,
    eol::types::UniqueCollectionType,
    eol::types::BagType,
    PseudoType,
    eol::types::SelfContentType,
    eol::types::SelfType,
    AnyType,
    eol::types::PrimitiveType,
    eol::types::MapType,
    eol::types::InvalidType,
    eol::types::PseudoType,
    eol::types::CollectionType,
    eol::types::VoidType,
    eol::types::ModelElementType,
    eol::types::NativeType,
    eol::types::ModelType,
    Type,
    eol::types::AnyType,
    eol::types::Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_realtype_is_not_abstract():
    assert not inspect.isabstract(RealType)


def test_realtype_constructor_exists():
    assert callable(RealType.__init__)


def test_realtype_constructor_args():
    sig = inspect.signature(RealType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::integertype_is_not_abstract():
    assert not inspect.isabstract(eol::types::IntegerType)


def test_eol::types::integertype_constructor_exists():
    assert callable(eol::types::IntegerType.__init__)


def test_eol::types::integertype_constructor_args():
    sig = inspect.signature(eol::types::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::realtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::RealType)


def test_eol::types::realtype_constructor_exists():
    assert callable(eol::types::RealType.__init__)


def test_eol::types::realtype_constructor_args():
    sig = inspect.signature(eol::types::RealType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::stringtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::StringType)


def test_eol::types::stringtype_constructor_exists():
    assert callable(eol::types::StringType.__init__)


def test_eol::types::stringtype_constructor_args():
    sig = inspect.signature(eol::types::StringType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::booleantype_is_not_abstract():
    assert not inspect.isabstract(eol::types::BooleanType)


def test_eol::types::booleantype_constructor_exists():
    assert callable(eol::types::BooleanType.__init__)


def test_eol::types::booleantype_constructor_args():
    sig = inspect.signature(eol::types::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(OrderedCollectionType)


def test_orderedcollectiontype_constructor_exists():
    assert callable(OrderedCollectionType.__init__)


def test_orderedcollectiontype_constructor_args():
    sig = inspect.signature(OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::sequencetype_is_not_abstract():
    assert not inspect.isabstract(eol::types::SequenceType)


def test_eol::types::sequencetype_constructor_exists():
    assert callable(eol::types::SequenceType.__init__)


def test_eol::types::sequencetype_constructor_args():
    sig = inspect.signature(eol::types::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(UniqueCollectionType)


def test_uniquecollectiontype_constructor_exists():
    assert callable(UniqueCollectionType.__init__)


def test_uniquecollectiontype_constructor_args():
    sig = inspect.signature(UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(eol::types::OrderedSetType)


def test_eol::types::orderedsettype_constructor_exists():
    assert callable(eol::types::OrderedSetType.__init__)


def test_eol::types::orderedsettype_constructor_args():
    sig = inspect.signature(eol::types::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::settype_is_not_abstract():
    assert not inspect.isabstract(eol::types::SetType)


def test_eol::types::settype_constructor_exists():
    assert callable(eol::types::SetType.__init__)


def test_eol::types::settype_constructor_args():
    sig = inspect.signature(eol::types::SetType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::orderedcollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::types::OrderedCollectionType)


def test_eol::types::orderedcollectiontype_constructor_exists():
    assert callable(eol::types::OrderedCollectionType.__init__)


def test_eol::types::orderedcollectiontype_constructor_args():
    sig = inspect.signature(eol::types::OrderedCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::uniquecollectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::types::UniqueCollectionType)


def test_eol::types::uniquecollectiontype_constructor_exists():
    assert callable(eol::types::UniqueCollectionType.__init__)


def test_eol::types::uniquecollectiontype_constructor_args():
    sig = inspect.signature(eol::types::UniqueCollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::bagtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::BagType)


def test_eol::types::bagtype_constructor_exists():
    assert callable(eol::types::BagType.__init__)


def test_eol::types::bagtype_constructor_args():
    sig = inspect.signature(eol::types::BagType.__init__)
    params = list(sig.parameters.keys())



def test_pseudotype_is_not_abstract():
    assert not inspect.isabstract(PseudoType)


def test_pseudotype_constructor_exists():
    assert callable(PseudoType.__init__)


def test_pseudotype_constructor_args():
    sig = inspect.signature(PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::selfcontenttype_is_not_abstract():
    assert not inspect.isabstract(eol::types::SelfContentType)


def test_eol::types::selfcontenttype_constructor_exists():
    assert callable(eol::types::SelfContentType.__init__)


def test_eol::types::selfcontenttype_constructor_args():
    sig = inspect.signature(eol::types::SelfContentType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::selftype_is_not_abstract():
    assert not inspect.isabstract(eol::types::SelfType)


def test_eol::types::selftype_constructor_exists():
    assert callable(eol::types::SelfType.__init__)


def test_eol::types::selftype_constructor_args():
    sig = inspect.signature(eol::types::SelfType.__init__)
    params = list(sig.parameters.keys())



def test_anytype_is_not_abstract():
    assert not inspect.isabstract(AnyType)


def test_anytype_constructor_exists():
    assert callable(AnyType.__init__)


def test_anytype_constructor_args():
    sig = inspect.signature(AnyType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(eol::types::PrimitiveType)


def test_eol::types::primitivetype_constructor_exists():
    assert callable(eol::types::PrimitiveType.__init__)


def test_eol::types::primitivetype_constructor_args():
    sig = inspect.signature(eol::types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::maptype_is_not_abstract():
    assert not inspect.isabstract(eol::types::MapType)


def test_eol::types::maptype_constructor_exists():
    assert callable(eol::types::MapType.__init__)


def test_eol::types::maptype_constructor_args():
    sig = inspect.signature(eol::types::MapType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::invalidtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::InvalidType)


def test_eol::types::invalidtype_constructor_exists():
    assert callable(eol::types::InvalidType.__init__)


def test_eol::types::invalidtype_constructor_args():
    sig = inspect.signature(eol::types::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::pseudotype_is_not_abstract():
    assert not inspect.isabstract(eol::types::PseudoType)


def test_eol::types::pseudotype_constructor_exists():
    assert callable(eol::types::PseudoType.__init__)


def test_eol::types::pseudotype_constructor_args():
    sig = inspect.signature(eol::types::PseudoType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::collectiontype_is_not_abstract():
    assert not inspect.isabstract(eol::types::CollectionType)


def test_eol::types::collectiontype_constructor_exists():
    assert callable(eol::types::CollectionType.__init__)


def test_eol::types::collectiontype_constructor_args():
    sig = inspect.signature(eol::types::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::voidtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::VoidType)


def test_eol::types::voidtype_constructor_exists():
    assert callable(eol::types::VoidType.__init__)


def test_eol::types::voidtype_constructor_args():
    sig = inspect.signature(eol::types::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::modelelementtype_is_not_abstract():
    assert not inspect.isabstract(eol::types::ModelElementType)


def test_eol::types::modelelementtype_constructor_exists():
    assert callable(eol::types::ModelElementType.__init__)


def test_eol::types::modelelementtype_constructor_args():
    sig = inspect.signature(eol::types::ModelElementType.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_eol::types::modelelementtype_has_elementName():
    assert hasattr(eol::types::ModelElementType, "elementName")
    descriptor = None
    for klass in eol::types::ModelElementType.__mro__:
        if "elementName" in klass.__dict__:
            descriptor = klass.__dict__["elementName"]
            break
    assert isinstance(descriptor, property)

def test_eol::types::modelelementtype_has_modelName():
    assert hasattr(eol::types::ModelElementType, "modelName")
    descriptor = None
    for klass in eol::types::ModelElementType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_eol::types::nativetype_is_not_abstract():
    assert not inspect.isabstract(eol::types::NativeType)


def test_eol::types::nativetype_constructor_exists():
    assert callable(eol::types::NativeType.__init__)


def test_eol::types::nativetype_constructor_args():
    sig = inspect.signature(eol::types::NativeType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_eol::types::nativetype_has_value():
    assert hasattr(eol::types::NativeType, "value")
    descriptor = None
    for klass in eol::types::NativeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_eol::types::modeltype_is_not_abstract():
    assert not inspect.isabstract(eol::types::ModelType)


def test_eol::types::modeltype_constructor_exists():
    assert callable(eol::types::ModelType.__init__)


def test_eol::types::modeltype_constructor_args():
    sig = inspect.signature(eol::types::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_eol::types::modeltype_has_modelName():
    assert hasattr(eol::types::ModelType, "modelName")
    descriptor = None
    for klass in eol::types::ModelType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_eol::types::anytype_is_not_abstract():
    assert not inspect.isabstract(eol::types::AnyType)


def test_eol::types::anytype_constructor_exists():
    assert callable(eol::types::AnyType.__init__)


def test_eol::types::anytype_constructor_args():
    sig = inspect.signature(eol::types::AnyType.__init__)
    params = list(sig.parameters.keys())
    assert "declared" in params, "Missing parameter 'declared'"

def test_eol::types::anytype_has_declared():
    assert hasattr(eol::types::AnyType, "declared")
    descriptor = None
    for klass in eol::types::AnyType.__mro__:
        if "declared" in klass.__dict__:
            descriptor = klass.__dict__["declared"]
            break
    assert isinstance(descriptor, property)



def test_eol::types::type_is_not_abstract():
    assert not inspect.isabstract(eol::types::Type)


def test_eol::types::type_constructor_exists():
    assert callable(eol::types::Type.__init__)


def test_eol::types::type_constructor_args():
    sig = inspect.signature(eol::types::Type.__init__)
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
RealType_strategy = st.builds(
    RealType,
)
eol::types::IntegerType_strategy = st.builds(
    eol::types::IntegerType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
eol::types::RealType_strategy = st.builds(
    eol::types::RealType,
)
eol::types::StringType_strategy = st.builds(
    eol::types::StringType,
)
eol::types::BooleanType_strategy = st.builds(
    eol::types::BooleanType,
)
OrderedCollectionType_strategy = st.builds(
    OrderedCollectionType,
)
eol::types::SequenceType_strategy = st.builds(
    eol::types::SequenceType,
)
UniqueCollectionType_strategy = st.builds(
    UniqueCollectionType,
)
eol::types::OrderedSetType_strategy = st.builds(
    eol::types::OrderedSetType,
)
eol::types::SetType_strategy = st.builds(
    eol::types::SetType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
eol::types::OrderedCollectionType_strategy = st.builds(
    eol::types::OrderedCollectionType,
)
eol::types::UniqueCollectionType_strategy = st.builds(
    eol::types::UniqueCollectionType,
)
eol::types::BagType_strategy = st.builds(
    eol::types::BagType,
)
PseudoType_strategy = st.builds(
    PseudoType,
)
eol::types::SelfContentType_strategy = st.builds(
    eol::types::SelfContentType,
)
eol::types::SelfType_strategy = st.builds(
    eol::types::SelfType,
)
AnyType_strategy = st.builds(
    AnyType,
)
eol::types::PrimitiveType_strategy = st.builds(
    eol::types::PrimitiveType,
)
eol::types::MapType_strategy = st.builds(
    eol::types::MapType,
)
eol::types::InvalidType_strategy = st.builds(
    eol::types::InvalidType,
)
eol::types::PseudoType_strategy = st.builds(
    eol::types::PseudoType,
)
eol::types::CollectionType_strategy = st.builds(
    eol::types::CollectionType,
)
eol::types::VoidType_strategy = st.builds(
    eol::types::VoidType,
)
eol::types::ModelElementType_strategy = st.builds(
    eol::types::ModelElementType,
    elementName=
        safe_text,
    modelName=
        safe_text
)
eol::types::NativeType_strategy = st.builds(
    eol::types::NativeType,
    value=
        safe_text
)
eol::types::ModelType_strategy = st.builds(
    eol::types::ModelType,
    modelName=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
eol::types::AnyType_strategy = st.builds(
    eol::types::AnyType,
    declared=
        st.booleans()
)
eol::types::Type_strategy = st.builds(
    eol::types::Type,
)

@given(instance=RealType_strategy)
@settings(max_examples=50)
def test_realtype_instantiation(instance):
    assert isinstance(instance, RealType)

@given(instance=eol::types::IntegerType_strategy)
@settings(max_examples=50)
def test_eol::types::integertype_instantiation(instance):
    assert isinstance(instance, eol::types::IntegerType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=eol::types::RealType_strategy)
@settings(max_examples=50)
def test_eol::types::realtype_instantiation(instance):
    assert isinstance(instance, eol::types::RealType)

@given(instance=eol::types::StringType_strategy)
@settings(max_examples=50)
def test_eol::types::stringtype_instantiation(instance):
    assert isinstance(instance, eol::types::StringType)

@given(instance=eol::types::BooleanType_strategy)
@settings(max_examples=50)
def test_eol::types::booleantype_instantiation(instance):
    assert isinstance(instance, eol::types::BooleanType)

@given(instance=OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, OrderedCollectionType)

@given(instance=eol::types::SequenceType_strategy)
@settings(max_examples=50)
def test_eol::types::sequencetype_instantiation(instance):
    assert isinstance(instance, eol::types::SequenceType)

@given(instance=UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, UniqueCollectionType)

@given(instance=eol::types::OrderedSetType_strategy)
@settings(max_examples=50)
def test_eol::types::orderedsettype_instantiation(instance):
    assert isinstance(instance, eol::types::OrderedSetType)

@given(instance=eol::types::SetType_strategy)
@settings(max_examples=50)
def test_eol::types::settype_instantiation(instance):
    assert isinstance(instance, eol::types::SetType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=eol::types::OrderedCollectionType_strategy)
@settings(max_examples=50)
def test_eol::types::orderedcollectiontype_instantiation(instance):
    assert isinstance(instance, eol::types::OrderedCollectionType)

@given(instance=eol::types::UniqueCollectionType_strategy)
@settings(max_examples=50)
def test_eol::types::uniquecollectiontype_instantiation(instance):
    assert isinstance(instance, eol::types::UniqueCollectionType)

@given(instance=eol::types::BagType_strategy)
@settings(max_examples=50)
def test_eol::types::bagtype_instantiation(instance):
    assert isinstance(instance, eol::types::BagType)

@given(instance=PseudoType_strategy)
@settings(max_examples=50)
def test_pseudotype_instantiation(instance):
    assert isinstance(instance, PseudoType)

@given(instance=eol::types::SelfContentType_strategy)
@settings(max_examples=50)
def test_eol::types::selfcontenttype_instantiation(instance):
    assert isinstance(instance, eol::types::SelfContentType)

@given(instance=eol::types::SelfType_strategy)
@settings(max_examples=50)
def test_eol::types::selftype_instantiation(instance):
    assert isinstance(instance, eol::types::SelfType)

@given(instance=AnyType_strategy)
@settings(max_examples=50)
def test_anytype_instantiation(instance):
    assert isinstance(instance, AnyType)

@given(instance=eol::types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_eol::types::primitivetype_instantiation(instance):
    assert isinstance(instance, eol::types::PrimitiveType)

@given(instance=eol::types::MapType_strategy)
@settings(max_examples=50)
def test_eol::types::maptype_instantiation(instance):
    assert isinstance(instance, eol::types::MapType)

@given(instance=eol::types::InvalidType_strategy)
@settings(max_examples=50)
def test_eol::types::invalidtype_instantiation(instance):
    assert isinstance(instance, eol::types::InvalidType)

@given(instance=eol::types::PseudoType_strategy)
@settings(max_examples=50)
def test_eol::types::pseudotype_instantiation(instance):
    assert isinstance(instance, eol::types::PseudoType)

@given(instance=eol::types::CollectionType_strategy)
@settings(max_examples=50)
def test_eol::types::collectiontype_instantiation(instance):
    assert isinstance(instance, eol::types::CollectionType)

@given(instance=eol::types::VoidType_strategy)
@settings(max_examples=50)
def test_eol::types::voidtype_instantiation(instance):
    assert isinstance(instance, eol::types::VoidType)

@given(instance=eol::types::ModelElementType_strategy)
@settings(max_examples=50)
def test_eol::types::modelelementtype_instantiation(instance):
    assert isinstance(instance, eol::types::ModelElementType)

@given(instance=eol::types::ModelElementType_strategy)
def test_eol::types::modelelementtype_elementName_type(instance):
    assert isinstance(instance.elementName, str)


@given(instance=eol::types::ModelElementType_strategy)
def test_eol::types::modelelementtype_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original

@given(instance=eol::types::ModelElementType_strategy)
def test_eol::types::modelelementtype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=eol::types::ModelElementType_strategy)
def test_eol::types::modelelementtype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=eol::types::NativeType_strategy)
@settings(max_examples=50)
def test_eol::types::nativetype_instantiation(instance):
    assert isinstance(instance, eol::types::NativeType)

@given(instance=eol::types::NativeType_strategy)
def test_eol::types::nativetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eol::types::NativeType_strategy)
def test_eol::types::nativetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eol::types::ModelType_strategy)
@settings(max_examples=50)
def test_eol::types::modeltype_instantiation(instance):
    assert isinstance(instance, eol::types::ModelType)

@given(instance=eol::types::ModelType_strategy)
def test_eol::types::modeltype_modelName_type(instance):
    assert isinstance(instance.modelName, str)


@given(instance=eol::types::ModelType_strategy)
def test_eol::types::modeltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eol::types::AnyType_strategy)
@settings(max_examples=50)
def test_eol::types::anytype_instantiation(instance):
    assert isinstance(instance, eol::types::AnyType)

@given(instance=eol::types::AnyType_strategy)
def test_eol::types::anytype_declared_type(instance):
    assert isinstance(instance.declared, bool)


@given(instance=eol::types::AnyType_strategy)
def test_eol::types::anytype_declared_setter(instance):
    original = instance.declared
    instance.declared = original
    assert instance.declared == original

@given(instance=eol::types::Type_strategy)
@settings(max_examples=50)
def test_eol::types::type_instantiation(instance):
    assert isinstance(instance, eol::types::Type)

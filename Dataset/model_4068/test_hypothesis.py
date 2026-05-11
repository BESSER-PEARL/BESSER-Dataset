import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModelElement,
    simpleuml::Property,
    simpleuml::Generalization,
    simpleuml::TaggedValue,
    simpleuml::ModelElement,
    simpleuml::Classifier,
    simpleuml::EnumerationLiteral,
    Type,
    simpleuml::Enumeration,
    simpleuml::PrimitiveType,
    simpleuml::DataType,
    DataType,
    simpleuml::Class,
    simpleuml::Packageable,
    Packageable,
    simpleuml::Association,
    Classifier,
    simpleuml::Type,
    simpleuml::Package,
    Package,
    simpleuml::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::property_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Property)


def test_simpleuml::property_constructor_exists():
    assert callable(simpleuml::Property.__init__)


def test_simpleuml::property_constructor_args():
    sig = inspect.signature(simpleuml::Property.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::generalization_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Generalization)


def test_simpleuml::generalization_constructor_exists():
    assert callable(simpleuml::Generalization.__init__)


def test_simpleuml::generalization_constructor_args():
    sig = inspect.signature(simpleuml::Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_simpleuml::generalization_has_isSubstitutable():
    assert hasattr(simpleuml::Generalization, "isSubstitutable")
    descriptor = None
    for klass in simpleuml::Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::taggedvalue_is_not_abstract():
    assert not inspect.isabstract(simpleuml::TaggedValue)


def test_simpleuml::taggedvalue_constructor_exists():
    assert callable(simpleuml::TaggedValue.__init__)


def test_simpleuml::taggedvalue_constructor_args():
    sig = inspect.signature(simpleuml::TaggedValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_simpleuml::taggedvalue_has_name():
    assert hasattr(simpleuml::TaggedValue, "name")
    descriptor = None
    for klass in simpleuml::TaggedValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::taggedvalue_has_value():
    assert hasattr(simpleuml::TaggedValue, "value")
    descriptor = None
    for klass in simpleuml::TaggedValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::modelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml::ModelElement)


def test_simpleuml::modelelement_constructor_exists():
    assert callable(simpleuml::ModelElement.__init__)


def test_simpleuml::modelelement_constructor_args():
    sig = inspect.signature(simpleuml::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_simpleuml::modelelement_has_name():
    assert hasattr(simpleuml::ModelElement, "name")
    descriptor = None
    for klass in simpleuml::ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleuml::modelelement_has_stereotype():
    assert hasattr(simpleuml::ModelElement, "stereotype")
    descriptor = None
    for klass in simpleuml::ModelElement.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleuml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleuml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(simpleuml::EnumerationLiteral)


def test_simpleuml::enumerationliteral_constructor_exists():
    assert callable(simpleuml::EnumerationLiteral.__init__)


def test_simpleuml::enumerationliteral_constructor_args():
    sig = inspect.signature(simpleuml::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::enumerationliteral_has_name():
    assert hasattr(simpleuml::EnumerationLiteral, "name")
    descriptor = None
    for klass in simpleuml::EnumerationLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::enumeration_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Enumeration)


def test_simpleuml::enumeration_constructor_exists():
    assert callable(simpleuml::Enumeration.__init__)


def test_simpleuml::enumeration_constructor_args():
    sig = inspect.signature(simpleuml::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::primitivetype_is_not_abstract():
    assert not inspect.isabstract(simpleuml::PrimitiveType)


def test_simpleuml::primitivetype_constructor_exists():
    assert callable(simpleuml::PrimitiveType.__init__)


def test_simpleuml::primitivetype_constructor_args():
    sig = inspect.signature(simpleuml::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::datatype_is_not_abstract():
    assert not inspect.isabstract(simpleuml::DataType)


def test_simpleuml::datatype_constructor_exists():
    assert callable(simpleuml::DataType.__init__)


def test_simpleuml::datatype_constructor_args():
    sig = inspect.signature(simpleuml::DataType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleuml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleuml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_simpleuml::class_has_abstract():
    assert hasattr(simpleuml::Class, "abstract")
    descriptor = None
    for klass in simpleuml::Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::packageable_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Packageable)


def test_simpleuml::packageable_constructor_exists():
    assert callable(simpleuml::Packageable.__init__)


def test_simpleuml::packageable_constructor_args():
    sig = inspect.signature(simpleuml::Packageable.__init__)
    params = list(sig.parameters.keys())



def test_packageable_is_not_abstract():
    assert not inspect.isabstract(Packageable)


def test_packageable_constructor_exists():
    assert callable(Packageable.__init__)


def test_packageable_constructor_args():
    sig = inspect.signature(Packageable.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(simpleuml::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(simpleuml::Association.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::type_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Type)


def test_simpleuml::type_constructor_exists():
    assert callable(simpleuml::Type.__init__)


def test_simpleuml::type_constructor_args():
    sig = inspect.signature(simpleuml::Type.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(simpleuml::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(simpleuml::Package.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::model_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Model)


def test_simpleuml::model_constructor_exists():
    assert callable(simpleuml::Model.__init__)


def test_simpleuml::model_constructor_args():
    sig = inspect.signature(simpleuml::Model.__init__)
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
ModelElement_strategy = st.builds(
    ModelElement,
)
simpleuml::Property_strategy = st.builds(
    simpleuml::Property,
)
simpleuml::Generalization_strategy = st.builds(
    simpleuml::Generalization,
    isSubstitutable=
        st.booleans()
)
simpleuml::TaggedValue_strategy = st.builds(
    simpleuml::TaggedValue,
    name=
        safe_text,
    value=
        safe_text
)
simpleuml::ModelElement_strategy = st.builds(
    simpleuml::ModelElement,
    name=
        safe_text,
    stereotype=
        safe_text
)
simpleuml::Classifier_strategy = st.builds(
    simpleuml::Classifier,
)
simpleuml::EnumerationLiteral_strategy = st.builds(
    simpleuml::EnumerationLiteral,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
simpleuml::Enumeration_strategy = st.builds(
    simpleuml::Enumeration,
)
simpleuml::PrimitiveType_strategy = st.builds(
    simpleuml::PrimitiveType,
)
simpleuml::DataType_strategy = st.builds(
    simpleuml::DataType,
)
DataType_strategy = st.builds(
    DataType,
)
simpleuml::Class_strategy = st.builds(
    simpleuml::Class,
    abstract=
        st.booleans()
)
simpleuml::Packageable_strategy = st.builds(
    simpleuml::Packageable,
)
Packageable_strategy = st.builds(
    Packageable,
)
simpleuml::Association_strategy = st.builds(
    simpleuml::Association,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml::Type_strategy = st.builds(
    simpleuml::Type,
)
simpleuml::Package_strategy = st.builds(
    simpleuml::Package,
)
Package_strategy = st.builds(
    Package,
)
simpleuml::Model_strategy = st.builds(
    simpleuml::Model,
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=simpleuml::Property_strategy)
@settings(max_examples=50)
def test_simpleuml::property_instantiation(instance):
    assert isinstance(instance, simpleuml::Property)

@given(instance=simpleuml::Generalization_strategy)
@settings(max_examples=50)
def test_simpleuml::generalization_instantiation(instance):
    assert isinstance(instance, simpleuml::Generalization)

@given(instance=simpleuml::Generalization_strategy)
def test_simpleuml::generalization_isSubstitutable_type(instance):
    assert isinstance(instance.isSubstitutable, bool)


@given(instance=simpleuml::Generalization_strategy)
def test_simpleuml::generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=simpleuml::TaggedValue_strategy)
@settings(max_examples=50)
def test_simpleuml::taggedvalue_instantiation(instance):
    assert isinstance(instance, simpleuml::TaggedValue)

@given(instance=simpleuml::TaggedValue_strategy)
def test_simpleuml::taggedvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::TaggedValue_strategy)
def test_simpleuml::taggedvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleuml::TaggedValue_strategy)
def test_simpleuml::taggedvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simpleuml::TaggedValue_strategy)
def test_simpleuml::taggedvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simpleuml::ModelElement_strategy)
@settings(max_examples=50)
def test_simpleuml::modelelement_instantiation(instance):
    assert isinstance(instance, simpleuml::ModelElement)

@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=simpleuml::ModelElement_strategy)
def test_simpleuml::modelelement_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=simpleuml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleuml::Classifier)

@given(instance=simpleuml::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_simpleuml::enumerationliteral_instantiation(instance):
    assert isinstance(instance, simpleuml::EnumerationLiteral)

@given(instance=simpleuml::EnumerationLiteral_strategy)
def test_simpleuml::enumerationliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::EnumerationLiteral_strategy)
def test_simpleuml::enumerationliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=simpleuml::Enumeration_strategy)
@settings(max_examples=50)
def test_simpleuml::enumeration_instantiation(instance):
    assert isinstance(instance, simpleuml::Enumeration)

@given(instance=simpleuml::PrimitiveType_strategy)
@settings(max_examples=50)
def test_simpleuml::primitivetype_instantiation(instance):
    assert isinstance(instance, simpleuml::PrimitiveType)

@given(instance=simpleuml::DataType_strategy)
@settings(max_examples=50)
def test_simpleuml::datatype_instantiation(instance):
    assert isinstance(instance, simpleuml::DataType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=simpleuml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleuml::Class)

@given(instance=simpleuml::Class_strategy)
def test_simpleuml::class_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=simpleuml::Class_strategy)
def test_simpleuml::class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=simpleuml::Packageable_strategy)
@settings(max_examples=50)
def test_simpleuml::packageable_instantiation(instance):
    assert isinstance(instance, simpleuml::Packageable)

@given(instance=Packageable_strategy)
@settings(max_examples=50)
def test_packageable_instantiation(instance):
    assert isinstance(instance, Packageable)

@given(instance=simpleuml::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, simpleuml::Association)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml::Type_strategy)
@settings(max_examples=50)
def test_simpleuml::type_instantiation(instance):
    assert isinstance(instance, simpleuml::Type)

@given(instance=simpleuml::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, simpleuml::Package)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=simpleuml::Model_strategy)
@settings(max_examples=50)
def test_simpleuml::model_instantiation(instance):
    assert isinstance(instance, simpleuml::Model)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Attribute,
    Type,
    Table,
    Column,
    Named,
    ClassDiagram::Column,
    ClassDiagram::Type,
    ClassDiagram::Table,
    ClassDiagram::Named,
    Class,
    Classifier,
    ClassDiagram::Class,
    ClassDiagram::DataType,
    NamedElement,
    ClassDiagram::Attribute,
    ClassDiagram::Classifier,
    ClassDiagram::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::column_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Column)


def test_classdiagram::column_constructor_exists():
    assert callable(ClassDiagram::Column.__init__)


def test_classdiagram::column_constructor_args():
    sig = inspect.signature(ClassDiagram::Column.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::type_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Type)


def test_classdiagram::type_constructor_exists():
    assert callable(ClassDiagram::Type.__init__)


def test_classdiagram::type_constructor_args():
    sig = inspect.signature(ClassDiagram::Type.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::table_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Table)


def test_classdiagram::table_constructor_exists():
    assert callable(ClassDiagram::Table.__init__)


def test_classdiagram::table_constructor_args():
    sig = inspect.signature(ClassDiagram::Table.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::named_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Named)


def test_classdiagram::named_constructor_exists():
    assert callable(ClassDiagram::Named.__init__)


def test_classdiagram::named_constructor_args():
    sig = inspect.signature(ClassDiagram::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::named_has_name():
    assert hasattr(ClassDiagram::Named, "name")
    descriptor = None
    for klass in ClassDiagram::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(ClassDiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(ClassDiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classdiagram::class_has_isAbstract():
    assert hasattr(ClassDiagram::Class, "isAbstract")
    descriptor = None
    for klass in ClassDiagram::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::datatype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::DataType)


def test_classdiagram::datatype_constructor_exists():
    assert callable(ClassDiagram::DataType.__init__)


def test_classdiagram::datatype_constructor_args():
    sig = inspect.signature(ClassDiagram::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(ClassDiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(ClassDiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_classdiagram::attribute_has_multiValued():
    assert hasattr(ClassDiagram::Attribute, "multiValued")
    descriptor = None
    for klass in ClassDiagram::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(ClassDiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(ClassDiagram::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::NamedElement)


def test_classdiagram::namedelement_constructor_exists():
    assert callable(ClassDiagram::NamedElement.__init__)


def test_classdiagram::namedelement_constructor_args():
    sig = inspect.signature(ClassDiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::namedelement_has_name():
    assert hasattr(ClassDiagram::NamedElement, "name")
    descriptor = None
    for klass in ClassDiagram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Attribute_strategy = st.builds(
    Attribute,
)
Type_strategy = st.builds(
    Type,
)
Table_strategy = st.builds(
    Table,
)
Column_strategy = st.builds(
    Column,
)
Named_strategy = st.builds(
    Named,
)
ClassDiagram::Column_strategy = st.builds(
    ClassDiagram::Column,
)
ClassDiagram::Type_strategy = st.builds(
    ClassDiagram::Type,
)
ClassDiagram::Table_strategy = st.builds(
    ClassDiagram::Table,
)
ClassDiagram::Named_strategy = st.builds(
    ClassDiagram::Named,
    name=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassDiagram::Class_strategy = st.builds(
    ClassDiagram::Class,
    isAbstract=
        safe_text
)
ClassDiagram::DataType_strategy = st.builds(
    ClassDiagram::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ClassDiagram::Attribute_strategy = st.builds(
    ClassDiagram::Attribute,
    multiValued=
        safe_text
)
ClassDiagram::Classifier_strategy = st.builds(
    ClassDiagram::Classifier,
)
ClassDiagram::NamedElement_strategy = st.builds(
    ClassDiagram::NamedElement,
    name=
        safe_text
)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=ClassDiagram::Column_strategy)
@settings(max_examples=50)
def test_classdiagram::column_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Column)

@given(instance=ClassDiagram::Type_strategy)
@settings(max_examples=50)
def test_classdiagram::type_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Type)

@given(instance=ClassDiagram::Table_strategy)
@settings(max_examples=50)
def test_classdiagram::table_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Table)

@given(instance=ClassDiagram::Named_strategy)
@settings(max_examples=50)
def test_classdiagram::named_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Named)

@given(instance=ClassDiagram::Named_strategy)
def test_classdiagram::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Named_strategy)
def test_classdiagram::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassDiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Class)

@given(instance=ClassDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=ClassDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ClassDiagram::DataType_strategy)
@settings(max_examples=50)
def test_classdiagram::datatype_instantiation(instance):
    assert isinstance(instance, ClassDiagram::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=ClassDiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Attribute)

@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, str)


@given(instance=ClassDiagram::Attribute_strategy)
def test_classdiagram::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=ClassDiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Classifier)

@given(instance=ClassDiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, ClassDiagram::NamedElement)

@given(instance=ClassDiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::NamedElement_strategy)
def test_classdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

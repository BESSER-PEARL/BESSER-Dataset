import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Dependency,
    ClassDiagram::Realization,
    ClassDiagram::Property,
    Classifier,
    ClassDiagram::Class,
    ClassDiagram::Interface,
    ClassDiagram::DataType,
    ClassDiagram::Classifier,
    Relationship,
    ClassDiagram::Generalization,
    ClassDiagram::Dependency,
    ClassDiagram::Association,
    ClassDiagram::Relationship,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::realization_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Realization)


def test_classdiagram::realization_constructor_exists():
    assert callable(ClassDiagram::Realization.__init__)


def test_classdiagram::realization_constructor_args():
    sig = inspect.signature(ClassDiagram::Realization.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::property_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Property)


def test_classdiagram::property_constructor_exists():
    assert callable(ClassDiagram::Property.__init__)


def test_classdiagram::property_constructor_args():
    sig = inspect.signature(ClassDiagram::Property.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_classdiagram::property_has_upper():
    assert hasattr(ClassDiagram::Property, "upper")
    descriptor = None
    for klass in ClassDiagram::Property.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::property_has_name():
    assert hasattr(ClassDiagram::Property, "name")
    descriptor = None
    for klass in ClassDiagram::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::property_has_lower():
    assert hasattr(ClassDiagram::Property, "lower")
    descriptor = None
    for klass in ClassDiagram::Property.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::property_has_aggregation():
    assert hasattr(ClassDiagram::Property, "aggregation")
    descriptor = None
    for klass in ClassDiagram::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



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



def test_classdiagram::interface_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Interface)


def test_classdiagram::interface_constructor_exists():
    assert callable(ClassDiagram::Interface.__init__)


def test_classdiagram::interface_constructor_args():
    sig = inspect.signature(ClassDiagram::Interface.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::datatype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::DataType)


def test_classdiagram::datatype_constructor_exists():
    assert callable(ClassDiagram::DataType.__init__)


def test_classdiagram::datatype_constructor_args():
    sig = inspect.signature(ClassDiagram::DataType.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(ClassDiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(ClassDiagram::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::classifier_has_name():
    assert hasattr(ClassDiagram::Classifier, "name")
    descriptor = None
    for klass in ClassDiagram::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::generalization_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Generalization)


def test_classdiagram::generalization_constructor_exists():
    assert callable(ClassDiagram::Generalization.__init__)


def test_classdiagram::generalization_constructor_args():
    sig = inspect.signature(ClassDiagram::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::dependency_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Dependency)


def test_classdiagram::dependency_constructor_exists():
    assert callable(ClassDiagram::Dependency.__init__)


def test_classdiagram::dependency_constructor_args():
    sig = inspect.signature(ClassDiagram::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::association_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Association)


def test_classdiagram::association_constructor_exists():
    assert callable(ClassDiagram::Association.__init__)


def test_classdiagram::association_constructor_args():
    sig = inspect.signature(ClassDiagram::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::association_has_name():
    assert hasattr(ClassDiagram::Association, "name")
    descriptor = None
    for klass in ClassDiagram::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::relationship_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram::Relationship)


def test_classdiagram::relationship_constructor_exists():
    assert callable(ClassDiagram::Relationship.__init__)


def test_classdiagram::relationship_constructor_args():
    sig = inspect.signature(ClassDiagram::Relationship.__init__)
    params = list(sig.parameters.keys())

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "composite",
        "none",
        "shared",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"


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
Dependency_strategy = st.builds(
    Dependency,
)
ClassDiagram::Realization_strategy = st.builds(
    ClassDiagram::Realization,
)
ClassDiagram::Property_strategy = st.builds(
    ClassDiagram::Property,
    upper=
        safe_text,
    name=
        safe_text,
    lower=
        st.integers(),
    aggregation=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassDiagram::Class_strategy = st.builds(
    ClassDiagram::Class,
)
ClassDiagram::Interface_strategy = st.builds(
    ClassDiagram::Interface,
)
ClassDiagram::DataType_strategy = st.builds(
    ClassDiagram::DataType,
)
ClassDiagram::Classifier_strategy = st.builds(
    ClassDiagram::Classifier,
    name=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
ClassDiagram::Generalization_strategy = st.builds(
    ClassDiagram::Generalization,
)
ClassDiagram::Dependency_strategy = st.builds(
    ClassDiagram::Dependency,
)
ClassDiagram::Association_strategy = st.builds(
    ClassDiagram::Association,
    name=
        safe_text
)
ClassDiagram::Relationship_strategy = st.builds(
    ClassDiagram::Relationship,
)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=ClassDiagram::Realization_strategy)
@settings(max_examples=50)
def test_classdiagram::realization_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Realization)

@given(instance=ClassDiagram::Property_strategy)
@settings(max_examples=50)
def test_classdiagram::property_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Property)

@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=ClassDiagram::Property_strategy)
def test_classdiagram::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassDiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Class)

@given(instance=ClassDiagram::Interface_strategy)
@settings(max_examples=50)
def test_classdiagram::interface_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Interface)

@given(instance=ClassDiagram::DataType_strategy)
@settings(max_examples=50)
def test_classdiagram::datatype_instantiation(instance):
    assert isinstance(instance, ClassDiagram::DataType)

@given(instance=ClassDiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Classifier)

@given(instance=ClassDiagram::Classifier_strategy)
def test_classdiagram::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Classifier_strategy)
def test_classdiagram::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=ClassDiagram::Generalization_strategy)
@settings(max_examples=50)
def test_classdiagram::generalization_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Generalization)

@given(instance=ClassDiagram::Dependency_strategy)
@settings(max_examples=50)
def test_classdiagram::dependency_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Dependency)

@given(instance=ClassDiagram::Association_strategy)
@settings(max_examples=50)
def test_classdiagram::association_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Association)

@given(instance=ClassDiagram::Association_strategy)
def test_classdiagram::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ClassDiagram::Association_strategy)
def test_classdiagram::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassDiagram::Relationship_strategy)
@settings(max_examples=50)
def test_classdiagram::relationship_instantiation(instance):
    assert isinstance(instance, ClassDiagram::Relationship)

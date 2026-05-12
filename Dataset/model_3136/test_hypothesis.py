import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Dependency,
    ClassDiagram_Realization,
    ClassDiagram_Property,
    Classifier,
    ClassDiagram_Class,
    ClassDiagram_Interface,
    ClassDiagram_DataType,
    ClassDiagram_Classifier,
    Relationship,
    ClassDiagram_Generalization,
    ClassDiagram_Dependency,
    ClassDiagram_Association,
    ClassDiagram_Relationship,
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



def test_classdiagram_realization_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Realization)


def test_classdiagram_realization_constructor_exists():
    assert callable(ClassDiagram_Realization.__init__)


def test_classdiagram_realization_constructor_args():
    sig = inspect.signature(ClassDiagram_Realization.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_property_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Property)


def test_classdiagram_property_constructor_exists():
    assert callable(ClassDiagram_Property.__init__)


def test_classdiagram_property_constructor_args():
    sig = inspect.signature(ClassDiagram_Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "name" in params, "Missing parameter 'name'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_classdiagram_property_has_aggregation():
    assert hasattr(ClassDiagram_Property, "aggregation")
    descriptor = None
    for klass in ClassDiagram_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_property_has_upper():
    assert hasattr(ClassDiagram_Property, "upper")
    descriptor = None
    for klass in ClassDiagram_Property.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_property_has_name():
    assert hasattr(ClassDiagram_Property, "name")
    descriptor = None
    for klass in ClassDiagram_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_property_has_lower():
    assert hasattr(ClassDiagram_Property, "lower")
    descriptor = None
    for klass in ClassDiagram_Property.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Class)


def test_classdiagram_class_constructor_exists():
    assert callable(ClassDiagram_Class.__init__)


def test_classdiagram_class_constructor_args():
    sig = inspect.signature(ClassDiagram_Class.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_interface_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Interface)


def test_classdiagram_interface_constructor_exists():
    assert callable(ClassDiagram_Interface.__init__)


def test_classdiagram_interface_constructor_args():
    sig = inspect.signature(ClassDiagram_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_datatype_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_DataType)


def test_classdiagram_datatype_constructor_exists():
    assert callable(ClassDiagram_DataType.__init__)


def test_classdiagram_datatype_constructor_args():
    sig = inspect.signature(ClassDiagram_DataType.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_classifier_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Classifier)


def test_classdiagram_classifier_constructor_exists():
    assert callable(ClassDiagram_Classifier.__init__)


def test_classdiagram_classifier_constructor_args():
    sig = inspect.signature(ClassDiagram_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_classifier_has_name():
    assert hasattr(ClassDiagram_Classifier, "name")
    descriptor = None
    for klass in ClassDiagram_Classifier.__mro__:
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



def test_classdiagram_generalization_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Generalization)


def test_classdiagram_generalization_constructor_exists():
    assert callable(ClassDiagram_Generalization.__init__)


def test_classdiagram_generalization_constructor_args():
    sig = inspect.signature(ClassDiagram_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_dependency_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Dependency)


def test_classdiagram_dependency_constructor_exists():
    assert callable(ClassDiagram_Dependency.__init__)


def test_classdiagram_dependency_constructor_args():
    sig = inspect.signature(ClassDiagram_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_association_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Association)


def test_classdiagram_association_constructor_exists():
    assert callable(ClassDiagram_Association.__init__)


def test_classdiagram_association_constructor_args():
    sig = inspect.signature(ClassDiagram_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_association_has_name():
    assert hasattr(ClassDiagram_Association, "name")
    descriptor = None
    for klass in ClassDiagram_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_relationship_is_not_abstract():
    assert not inspect.isabstract(ClassDiagram_Relationship)


def test_classdiagram_relationship_constructor_exists():
    assert callable(ClassDiagram_Relationship.__init__)


def test_classdiagram_relationship_constructor_args():
    sig = inspect.signature(ClassDiagram_Relationship.__init__)
    params = list(sig.parameters.keys())

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "none",
        "shared",
        "composite",
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
ClassDiagram_Realization_strategy = st.builds(
    ClassDiagram_Realization,
)
ClassDiagram_Property_strategy = st.builds(
    ClassDiagram_Property,
    aggregation=
        safe_text,
    upper=
        safe_text,
    name=
        safe_text,
    lower=
        st.integers()
)
Classifier_strategy = st.builds(
    Classifier,
)
ClassDiagram_Class_strategy = st.builds(
    ClassDiagram_Class,
)
ClassDiagram_Interface_strategy = st.builds(
    ClassDiagram_Interface,
)
ClassDiagram_DataType_strategy = st.builds(
    ClassDiagram_DataType,
)
ClassDiagram_Classifier_strategy = st.builds(
    ClassDiagram_Classifier,
    name=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
ClassDiagram_Generalization_strategy = st.builds(
    ClassDiagram_Generalization,
)
ClassDiagram_Dependency_strategy = st.builds(
    ClassDiagram_Dependency,
)
ClassDiagram_Association_strategy = st.builds(
    ClassDiagram_Association,
    name=
        safe_text
)
ClassDiagram_Relationship_strategy = st.builds(
    ClassDiagram_Relationship,
)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=ClassDiagram_Realization_strategy)
@settings(max_examples=50)
def test_classdiagram_realization_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Realization)

@given(instance=ClassDiagram_Property_strategy)
@settings(max_examples=50)
def test_classdiagram_property_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Property)



@given(instance=ClassDiagram_Property_strategy)
def test_classdiagram_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=ClassDiagram_Property_strategy)
def test_classdiagram_property_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=ClassDiagram_Property_strategy)
def test_classdiagram_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ClassDiagram_Property_strategy)
def test_classdiagram_property_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ClassDiagram_Class_strategy)
@settings(max_examples=50)
def test_classdiagram_class_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Class)

@given(instance=ClassDiagram_Interface_strategy)
@settings(max_examples=50)
def test_classdiagram_interface_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Interface)

@given(instance=ClassDiagram_DataType_strategy)
@settings(max_examples=50)
def test_classdiagram_datatype_instantiation(instance):
    assert isinstance(instance, ClassDiagram_DataType)

@given(instance=ClassDiagram_Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram_classifier_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Classifier)



@given(instance=ClassDiagram_Classifier_strategy)
def test_classdiagram_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=ClassDiagram_Generalization_strategy)
@settings(max_examples=50)
def test_classdiagram_generalization_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Generalization)

@given(instance=ClassDiagram_Dependency_strategy)
@settings(max_examples=50)
def test_classdiagram_dependency_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Dependency)

@given(instance=ClassDiagram_Association_strategy)
@settings(max_examples=50)
def test_classdiagram_association_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Association)



@given(instance=ClassDiagram_Association_strategy)
def test_classdiagram_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassDiagram_Relationship_strategy)
@settings(max_examples=50)
def test_classdiagram_relationship_instantiation(instance):
    assert isinstance(instance, ClassDiagram_Relationship)

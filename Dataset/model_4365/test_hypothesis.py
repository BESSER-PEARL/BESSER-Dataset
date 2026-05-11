import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relation,
    design::Composition,
    design::Generalization,
    design::Dependency,
    design::Association,
    design::Relation,
    design::Classifier,
    design::Design,
    design::Operation,
    design::Attribute,
    Classifier,
    design::Interface,
    design::Class,
    design::Realization,
    design::Aggregation,
    Types,
    Languages,
    AccessModifiers,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_design::composition_is_not_abstract():
    assert not inspect.isabstract(design::Composition)


def test_design::composition_constructor_exists():
    assert callable(design::Composition.__init__)


def test_design::composition_constructor_args():
    sig = inspect.signature(design::Composition.__init__)
    params = list(sig.parameters.keys())



def test_design::generalization_is_not_abstract():
    assert not inspect.isabstract(design::Generalization)


def test_design::generalization_constructor_exists():
    assert callable(design::Generalization.__init__)


def test_design::generalization_constructor_args():
    sig = inspect.signature(design::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_design::dependency_is_not_abstract():
    assert not inspect.isabstract(design::Dependency)


def test_design::dependency_constructor_exists():
    assert callable(design::Dependency.__init__)


def test_design::dependency_constructor_args():
    sig = inspect.signature(design::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_design::association_is_not_abstract():
    assert not inspect.isabstract(design::Association)


def test_design::association_constructor_exists():
    assert callable(design::Association.__init__)


def test_design::association_constructor_args():
    sig = inspect.signature(design::Association.__init__)
    params = list(sig.parameters.keys())



def test_design::relation_is_not_abstract():
    assert not inspect.isabstract(design::Relation)


def test_design::relation_constructor_exists():
    assert callable(design::Relation.__init__)


def test_design::relation_constructor_args():
    sig = inspect.signature(design::Relation.__init__)
    params = list(sig.parameters.keys())



def test_design::classifier_is_not_abstract():
    assert not inspect.isabstract(design::Classifier)


def test_design::classifier_constructor_exists():
    assert callable(design::Classifier.__init__)


def test_design::classifier_constructor_args():
    sig = inspect.signature(design::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "name" in params, "Missing parameter 'name'"

def test_design::classifier_has_accessModifier():
    assert hasattr(design::Classifier, "accessModifier")
    descriptor = None
    for klass in design::Classifier.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_design::classifier_has_name():
    assert hasattr(design::Classifier, "name")
    descriptor = None
    for klass in design::Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_design::design_is_not_abstract():
    assert not inspect.isabstract(design::Design)


def test_design::design_constructor_exists():
    assert callable(design::Design.__init__)


def test_design::design_constructor_args():
    sig = inspect.signature(design::Design.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_design::design_has_language():
    assert hasattr(design::Design, "language")
    descriptor = None
    for klass in design::Design.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_design::operation_is_not_abstract():
    assert not inspect.isabstract(design::Operation)


def test_design::operation_constructor_exists():
    assert callable(design::Operation.__init__)


def test_design::operation_constructor_args():
    sig = inspect.signature(design::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "name" in params, "Missing parameter 'name'"

def test_design::operation_has_returnType():
    assert hasattr(design::Operation, "returnType")
    descriptor = None
    for klass in design::Operation.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_design::operation_has_name():
    assert hasattr(design::Operation, "name")
    descriptor = None
    for klass in design::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_design::attribute_is_not_abstract():
    assert not inspect.isabstract(design::Attribute)


def test_design::attribute_constructor_exists():
    assert callable(design::Attribute.__init__)


def test_design::attribute_constructor_args():
    sig = inspect.signature(design::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_design::attribute_has_type():
    assert hasattr(design::Attribute, "type")
    descriptor = None
    for klass in design::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_design::attribute_has_name():
    assert hasattr(design::Attribute, "name")
    descriptor = None
    for klass in design::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_design::interface_is_not_abstract():
    assert not inspect.isabstract(design::Interface)


def test_design::interface_constructor_exists():
    assert callable(design::Interface.__init__)


def test_design::interface_constructor_args():
    sig = inspect.signature(design::Interface.__init__)
    params = list(sig.parameters.keys())



def test_design::class_is_not_abstract():
    assert not inspect.isabstract(design::Class)


def test_design::class_constructor_exists():
    assert callable(design::Class.__init__)


def test_design::class_constructor_args():
    sig = inspect.signature(design::Class.__init__)
    params = list(sig.parameters.keys())



def test_design::realization_is_not_abstract():
    assert not inspect.isabstract(design::Realization)


def test_design::realization_constructor_exists():
    assert callable(design::Realization.__init__)


def test_design::realization_constructor_args():
    sig = inspect.signature(design::Realization.__init__)
    params = list(sig.parameters.keys())



def test_design::aggregation_is_not_abstract():
    assert not inspect.isabstract(design::Aggregation)


def test_design::aggregation_constructor_exists():
    assert callable(design::Aggregation.__init__)


def test_design::aggregation_constructor_args():
    sig = inspect.signature(design::Aggregation.__init__)
    params = list(sig.parameters.keys())

def test_types_exists():
    # Check that the Enumeration exists
    assert Types is not None

def test_types_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Types]
    expected_literals = [
        "float",
        "void",
        "string",
        "double",
        "long",
        "boolean",
        "int",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Types"

def test_languages_exists():
    # Check that the Enumeration exists
    assert Languages is not None

def test_languages_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Languages]
    expected_literals = [
        "CS",
        "CPP",
        "Python",
        "Java",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Languages"

def test_accessmodifiers_exists():
    # Check that the Enumeration exists
    assert AccessModifiers is not None

def test_accessmodifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifiers]
    expected_literals = [
        "public",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifiers"


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
Relation_strategy = st.builds(
    Relation,
)
design::Composition_strategy = st.builds(
    design::Composition,
)
design::Generalization_strategy = st.builds(
    design::Generalization,
)
design::Dependency_strategy = st.builds(
    design::Dependency,
)
design::Association_strategy = st.builds(
    design::Association,
)
design::Relation_strategy = st.builds(
    design::Relation,
)
design::Classifier_strategy = st.builds(
    design::Classifier,
    accessModifier=
        safe_text,
    name=
        safe_text
)
design::Design_strategy = st.builds(
    design::Design,
    language=
        safe_text
)
design::Operation_strategy = st.builds(
    design::Operation,
    returnType=
        safe_text,
    name=
        safe_text
)
design::Attribute_strategy = st.builds(
    design::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
design::Interface_strategy = st.builds(
    design::Interface,
)
design::Class_strategy = st.builds(
    design::Class,
)
design::Realization_strategy = st.builds(
    design::Realization,
)
design::Aggregation_strategy = st.builds(
    design::Aggregation,
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=design::Composition_strategy)
@settings(max_examples=50)
def test_design::composition_instantiation(instance):
    assert isinstance(instance, design::Composition)

@given(instance=design::Generalization_strategy)
@settings(max_examples=50)
def test_design::generalization_instantiation(instance):
    assert isinstance(instance, design::Generalization)

@given(instance=design::Dependency_strategy)
@settings(max_examples=50)
def test_design::dependency_instantiation(instance):
    assert isinstance(instance, design::Dependency)

@given(instance=design::Association_strategy)
@settings(max_examples=50)
def test_design::association_instantiation(instance):
    assert isinstance(instance, design::Association)

@given(instance=design::Relation_strategy)
@settings(max_examples=50)
def test_design::relation_instantiation(instance):
    assert isinstance(instance, design::Relation)

@given(instance=design::Classifier_strategy)
@settings(max_examples=50)
def test_design::classifier_instantiation(instance):
    assert isinstance(instance, design::Classifier)

@given(instance=design::Classifier_strategy)
def test_design::classifier_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=design::Classifier_strategy)
def test_design::classifier_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=design::Classifier_strategy)
def test_design::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=design::Classifier_strategy)
def test_design::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=design::Design_strategy)
@settings(max_examples=50)
def test_design::design_instantiation(instance):
    assert isinstance(instance, design::Design)

@given(instance=design::Design_strategy)
def test_design::design_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=design::Design_strategy)
def test_design::design_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=design::Operation_strategy)
@settings(max_examples=50)
def test_design::operation_instantiation(instance):
    assert isinstance(instance, design::Operation)

@given(instance=design::Operation_strategy)
def test_design::operation_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=design::Operation_strategy)
def test_design::operation_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=design::Operation_strategy)
def test_design::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=design::Operation_strategy)
def test_design::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=design::Attribute_strategy)
@settings(max_examples=50)
def test_design::attribute_instantiation(instance):
    assert isinstance(instance, design::Attribute)

@given(instance=design::Attribute_strategy)
def test_design::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=design::Attribute_strategy)
def test_design::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=design::Attribute_strategy)
def test_design::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=design::Attribute_strategy)
def test_design::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=design::Interface_strategy)
@settings(max_examples=50)
def test_design::interface_instantiation(instance):
    assert isinstance(instance, design::Interface)

@given(instance=design::Class_strategy)
@settings(max_examples=50)
def test_design::class_instantiation(instance):
    assert isinstance(instance, design::Class)

@given(instance=design::Realization_strategy)
@settings(max_examples=50)
def test_design::realization_instantiation(instance):
    assert isinstance(instance, design::Realization)

@given(instance=design::Aggregation_strategy)
@settings(max_examples=50)
def test_design::aggregation_instantiation(instance):
    assert isinstance(instance, design::Aggregation)

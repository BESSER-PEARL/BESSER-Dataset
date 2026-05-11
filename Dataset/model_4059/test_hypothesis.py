import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Classifier,
    classDiagram::Type,
    classDiagram::Class,
    ModelingConcept,
    classDiagram::Attribute,
    classDiagram::Function,
    classDiagram::Classifier,
    classDiagram::ModelingConcept,
    classDiagram::Package,
    classDiagram::ClassModel,
    AccessModifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::type_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Type)


def test_classdiagram::type_constructor_exists():
    assert callable(classDiagram::Type.__init__)


def test_classdiagram::type_constructor_args():
    sig = inspect.signature(classDiagram::Type.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::class_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Class)


def test_classdiagram::class_constructor_exists():
    assert callable(classDiagram::Class.__init__)


def test_classdiagram::class_constructor_args():
    sig = inspect.signature(classDiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"

def test_classdiagram::class_has_isStatic():
    assert hasattr(classDiagram::Class, "isStatic")
    descriptor = None
    for klass in classDiagram::Class.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::class_has_isAbstract():
    assert hasattr(classDiagram::Class, "isAbstract")
    descriptor = None
    for klass in classDiagram::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::class_has_accessModifier():
    assert hasattr(classDiagram::Class, "accessModifier")
    descriptor = None
    for klass in classDiagram::Class.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)



def test_modelingconcept_is_not_abstract():
    assert not inspect.isabstract(ModelingConcept)


def test_modelingconcept_constructor_exists():
    assert callable(ModelingConcept.__init__)


def test_modelingconcept_constructor_args():
    sig = inspect.signature(ModelingConcept.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Attribute)


def test_classdiagram::attribute_constructor_exists():
    assert callable(classDiagram::Attribute.__init__)


def test_classdiagram::attribute_constructor_args():
    sig = inspect.signature(classDiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_classdiagram::attribute_has_accessModifier():
    assert hasattr(classDiagram::Attribute, "accessModifier")
    descriptor = None
    for klass in classDiagram::Attribute.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::attribute_has_isStatic():
    assert hasattr(classDiagram::Attribute, "isStatic")
    descriptor = None
    for klass in classDiagram::Attribute.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::function_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Function)


def test_classdiagram::function_constructor_exists():
    assert callable(classDiagram::Function.__init__)


def test_classdiagram::function_constructor_args():
    sig = inspect.signature(classDiagram::Function.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "body" in params, "Missing parameter 'body'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classdiagram::function_has_isStatic():
    assert hasattr(classDiagram::Function, "isStatic")
    descriptor = None
    for klass in classDiagram::Function.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::function_has_body():
    assert hasattr(classDiagram::Function, "body")
    descriptor = None
    for klass in classDiagram::Function.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::function_has_accessModifier():
    assert hasattr(classDiagram::Function, "accessModifier")
    descriptor = None
    for klass in classDiagram::Function.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram::function_has_isAbstract():
    assert hasattr(classDiagram::Function, "isAbstract")
    descriptor = None
    for klass in classDiagram::Function.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Classifier)


def test_classdiagram::classifier_constructor_exists():
    assert callable(classDiagram::Classifier.__init__)


def test_classdiagram::classifier_constructor_args():
    sig = inspect.signature(classDiagram::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::modelingconcept_is_not_abstract():
    assert not inspect.isabstract(classDiagram::ModelingConcept)


def test_classdiagram::modelingconcept_constructor_exists():
    assert callable(classDiagram::ModelingConcept.__init__)


def test_classdiagram::modelingconcept_constructor_args():
    sig = inspect.signature(classDiagram::ModelingConcept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram::modelingconcept_has_name():
    assert hasattr(classDiagram::ModelingConcept, "name")
    descriptor = None
    for klass in classDiagram::ModelingConcept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram::package_is_not_abstract():
    assert not inspect.isabstract(classDiagram::Package)


def test_classdiagram::package_constructor_exists():
    assert callable(classDiagram::Package.__init__)


def test_classdiagram::package_constructor_args():
    sig = inspect.signature(classDiagram::Package.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram::classmodel_is_not_abstract():
    assert not inspect.isabstract(classDiagram::ClassModel)


def test_classdiagram::classmodel_constructor_exists():
    assert callable(classDiagram::ClassModel.__init__)


def test_classdiagram::classmodel_constructor_args():
    sig = inspect.signature(classDiagram::ClassModel.__init__)
    params = list(sig.parameters.keys())

def test_accessmodifier_exists():
    # Check that the Enumeration exists
    assert AccessModifier is not None

def test_accessmodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifier]
    expected_literals = [
        "protected",
        "private",
        "default",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifier"


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
Classifier_strategy = st.builds(
    Classifier,
)
classDiagram::Type_strategy = st.builds(
    classDiagram::Type,
)
classDiagram::Class_strategy = st.builds(
    classDiagram::Class,
    isStatic=
        st.booleans(),
    isAbstract=
        st.booleans(),
    accessModifier=
        safe_text
)
ModelingConcept_strategy = st.builds(
    ModelingConcept,
)
classDiagram::Attribute_strategy = st.builds(
    classDiagram::Attribute,
    accessModifier=
        safe_text,
    isStatic=
        st.booleans()
)
classDiagram::Function_strategy = st.builds(
    classDiagram::Function,
    isStatic=
        st.booleans(),
    body=
        safe_text,
    accessModifier=
        safe_text,
    isAbstract=
        st.booleans()
)
classDiagram::Classifier_strategy = st.builds(
    classDiagram::Classifier,
)
classDiagram::ModelingConcept_strategy = st.builds(
    classDiagram::ModelingConcept,
    name=
        safe_text
)
classDiagram::Package_strategy = st.builds(
    classDiagram::Package,
)
classDiagram::ClassModel_strategy = st.builds(
    classDiagram::ClassModel,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classDiagram::Type_strategy)
@settings(max_examples=50)
def test_classdiagram::type_instantiation(instance):
    assert isinstance(instance, classDiagram::Type)

@given(instance=classDiagram::Class_strategy)
@settings(max_examples=50)
def test_classdiagram::class_instantiation(instance):
    assert isinstance(instance, classDiagram::Class)

@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=classDiagram::Class_strategy)
def test_classdiagram::class_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=ModelingConcept_strategy)
@settings(max_examples=50)
def test_modelingconcept_instantiation(instance):
    assert isinstance(instance, ModelingConcept)

@given(instance=classDiagram::Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram::attribute_instantiation(instance):
    assert isinstance(instance, classDiagram::Attribute)

@given(instance=classDiagram::Attribute_strategy)
def test_classdiagram::attribute_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=classDiagram::Attribute_strategy)
def test_classdiagram::attribute_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=classDiagram::Attribute_strategy)
def test_classdiagram::attribute_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=classDiagram::Attribute_strategy)
def test_classdiagram::attribute_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=classDiagram::Function_strategy)
@settings(max_examples=50)
def test_classdiagram::function_instantiation(instance):
    assert isinstance(instance, classDiagram::Function)

@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=classDiagram::Function_strategy)
def test_classdiagram::function_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=classDiagram::Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram::classifier_instantiation(instance):
    assert isinstance(instance, classDiagram::Classifier)

@given(instance=classDiagram::ModelingConcept_strategy)
@settings(max_examples=50)
def test_classdiagram::modelingconcept_instantiation(instance):
    assert isinstance(instance, classDiagram::ModelingConcept)

@given(instance=classDiagram::ModelingConcept_strategy)
def test_classdiagram::modelingconcept_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classDiagram::ModelingConcept_strategy)
def test_classdiagram::modelingconcept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classDiagram::Package_strategy)
@settings(max_examples=50)
def test_classdiagram::package_instantiation(instance):
    assert isinstance(instance, classDiagram::Package)

@given(instance=classDiagram::ClassModel_strategy)
@settings(max_examples=50)
def test_classdiagram::classmodel_instantiation(instance):
    assert isinstance(instance, classDiagram::ClassModel)

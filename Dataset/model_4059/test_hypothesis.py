import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Classifier,
    classDiagram_Type,
    classDiagram_Class,
    ModelingConcept,
    classDiagram_Attribute,
    classDiagram_Classifier,
    classDiagram_Function,
    classDiagram_ModelingConcept,
    classDiagram_Package,
    classDiagram_ClassModel,
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



def test_classdiagram_type_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Type)


def test_classdiagram_type_constructor_exists():
    assert callable(classDiagram_Type.__init__)


def test_classdiagram_type_constructor_args():
    sig = inspect.signature(classDiagram_Type.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Class)


def test_classdiagram_class_constructor_exists():
    assert callable(classDiagram_Class.__init__)


def test_classdiagram_class_constructor_args():
    sig = inspect.signature(classDiagram_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_classdiagram_class_has_isStatic():
    assert hasattr(classDiagram_Class, "isStatic")
    descriptor = None
    for klass in classDiagram_Class.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_class_has_accessModifier():
    assert hasattr(classDiagram_Class, "accessModifier")
    descriptor = None
    for klass in classDiagram_Class.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_class_has_isAbstract():
    assert hasattr(classDiagram_Class, "isAbstract")
    descriptor = None
    for klass in classDiagram_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_modelingconcept_is_not_abstract():
    assert not inspect.isabstract(ModelingConcept)


def test_modelingconcept_constructor_exists():
    assert callable(ModelingConcept.__init__)


def test_modelingconcept_constructor_args():
    sig = inspect.signature(ModelingConcept.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Attribute)


def test_classdiagram_attribute_constructor_exists():
    assert callable(classDiagram_Attribute.__init__)


def test_classdiagram_attribute_constructor_args():
    sig = inspect.signature(classDiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_classdiagram_attribute_has_accessModifier():
    assert hasattr(classDiagram_Attribute, "accessModifier")
    descriptor = None
    for klass in classDiagram_Attribute.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_attribute_has_isStatic():
    assert hasattr(classDiagram_Attribute, "isStatic")
    descriptor = None
    for klass in classDiagram_Attribute.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_classifier_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Classifier)


def test_classdiagram_classifier_constructor_exists():
    assert callable(classDiagram_Classifier.__init__)


def test_classdiagram_classifier_constructor_args():
    sig = inspect.signature(classDiagram_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_function_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Function)


def test_classdiagram_function_constructor_exists():
    assert callable(classDiagram_Function.__init__)


def test_classdiagram_function_constructor_args():
    sig = inspect.signature(classDiagram_Function.__init__)
    params = list(sig.parameters.keys())
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "body" in params, "Missing parameter 'body'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_classdiagram_function_has_accessModifier():
    assert hasattr(classDiagram_Function, "accessModifier")
    descriptor = None
    for klass in classDiagram_Function.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_function_has_body():
    assert hasattr(classDiagram_Function, "body")
    descriptor = None
    for klass in classDiagram_Function.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_function_has_isAbstract():
    assert hasattr(classDiagram_Function, "isAbstract")
    descriptor = None
    for klass in classDiagram_Function.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_classdiagram_function_has_isStatic():
    assert hasattr(classDiagram_Function, "isStatic")
    descriptor = None
    for klass in classDiagram_Function.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_modelingconcept_is_not_abstract():
    assert not inspect.isabstract(classDiagram_ModelingConcept)


def test_classdiagram_modelingconcept_constructor_exists():
    assert callable(classDiagram_ModelingConcept.__init__)


def test_classdiagram_modelingconcept_constructor_args():
    sig = inspect.signature(classDiagram_ModelingConcept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_modelingconcept_has_name():
    assert hasattr(classDiagram_ModelingConcept, "name")
    descriptor = None
    for klass in classDiagram_ModelingConcept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_package_is_not_abstract():
    assert not inspect.isabstract(classDiagram_Package)


def test_classdiagram_package_constructor_exists():
    assert callable(classDiagram_Package.__init__)


def test_classdiagram_package_constructor_args():
    sig = inspect.signature(classDiagram_Package.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_classmodel_is_not_abstract():
    assert not inspect.isabstract(classDiagram_ClassModel)


def test_classdiagram_classmodel_constructor_exists():
    assert callable(classDiagram_ClassModel.__init__)


def test_classdiagram_classmodel_constructor_args():
    sig = inspect.signature(classDiagram_ClassModel.__init__)
    params = list(sig.parameters.keys())

def test_accessmodifier_exists():
    # Check that the Enumeration exists
    assert AccessModifier is not None

def test_accessmodifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifier]
    expected_literals = [
        "public",
        "protected",
        "private",
        "default",
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
classDiagram_Type_strategy = st.builds(
    classDiagram_Type,
)
classDiagram_Class_strategy = st.builds(
    classDiagram_Class,
    isStatic=
        st.booleans(),
    accessModifier=
        safe_text,
    isAbstract=
        st.booleans()
)
ModelingConcept_strategy = st.builds(
    ModelingConcept,
)
classDiagram_Attribute_strategy = st.builds(
    classDiagram_Attribute,
    accessModifier=
        safe_text,
    isStatic=
        st.booleans()
)
classDiagram_Classifier_strategy = st.builds(
    classDiagram_Classifier,
)
classDiagram_Function_strategy = st.builds(
    classDiagram_Function,
    accessModifier=
        safe_text,
    body=
        safe_text,
    isAbstract=
        st.booleans(),
    isStatic=
        st.booleans()
)
classDiagram_ModelingConcept_strategy = st.builds(
    classDiagram_ModelingConcept,
    name=
        safe_text
)
classDiagram_Package_strategy = st.builds(
    classDiagram_Package,
)
classDiagram_ClassModel_strategy = st.builds(
    classDiagram_ClassModel,
)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=classDiagram_Type_strategy)
@settings(max_examples=50)
def test_classdiagram_type_instantiation(instance):
    assert isinstance(instance, classDiagram_Type)

@given(instance=classDiagram_Class_strategy)
@settings(max_examples=50)
def test_classdiagram_class_instantiation(instance):
    assert isinstance(instance, classDiagram_Class)



@given(instance=classDiagram_Class_strategy)
def test_classdiagram_class_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=classDiagram_Class_strategy)
def test_classdiagram_class_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original



@given(instance=classDiagram_Class_strategy)
def test_classdiagram_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=ModelingConcept_strategy)
@settings(max_examples=50)
def test_modelingconcept_instantiation(instance):
    assert isinstance(instance, ModelingConcept)

@given(instance=classDiagram_Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram_attribute_instantiation(instance):
    assert isinstance(instance, classDiagram_Attribute)



@given(instance=classDiagram_Attribute_strategy)
def test_classdiagram_attribute_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original



@given(instance=classDiagram_Attribute_strategy)
def test_classdiagram_attribute_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=classDiagram_Classifier_strategy)
@settings(max_examples=50)
def test_classdiagram_classifier_instantiation(instance):
    assert isinstance(instance, classDiagram_Classifier)

@given(instance=classDiagram_Function_strategy)
@settings(max_examples=50)
def test_classdiagram_function_instantiation(instance):
    assert isinstance(instance, classDiagram_Function)



@given(instance=classDiagram_Function_strategy)
def test_classdiagram_function_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original



@given(instance=classDiagram_Function_strategy)
def test_classdiagram_function_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=classDiagram_Function_strategy)
def test_classdiagram_function_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=classDiagram_Function_strategy)
def test_classdiagram_function_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=classDiagram_ModelingConcept_strategy)
@settings(max_examples=50)
def test_classdiagram_modelingconcept_instantiation(instance):
    assert isinstance(instance, classDiagram_ModelingConcept)



@given(instance=classDiagram_ModelingConcept_strategy)
def test_classdiagram_modelingconcept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classDiagram_Package_strategy)
@settings(max_examples=50)
def test_classdiagram_package_instantiation(instance):
    assert isinstance(instance, classDiagram_Package)

@given(instance=classDiagram_ClassModel_strategy)
@settings(max_examples=50)
def test_classdiagram_classmodel_instantiation(instance):
    assert isinstance(instance, classDiagram_ClassModel)

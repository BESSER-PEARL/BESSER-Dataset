import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    java_AnnotationInstanceValue,
    java_AnnotationInstanceParameter,
    java_AnnotationInstance,
    java_Annotable,
    java_GETExpression,
    Statement,
    java_AssertStatement,
    java_Statement,
    java_Argument,
    java_Container,
    java_Contained,
    java_Import,
    java_GenericBinding,
    Annotable,
    Contained,
    java_Field,
    java_Method,
    java_Generalization,
    java_InterfaceImplementation,
    Classifier,
    java_Annotation,
    java_Class,
    Container,
    java_Interface,
    java_Classifier,
    java_Package,
    java_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java_annotationinstancevalue_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationInstanceValue)


def test_java_annotationinstancevalue_constructor_exists():
    assert callable(java_AnnotationInstanceValue.__init__)


def test_java_annotationinstancevalue_constructor_args():
    sig = inspect.signature(java_AnnotationInstanceValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_annotationinstancevalue_has_value():
    assert hasattr(java_AnnotationInstanceValue, "value")
    descriptor = None
    for klass in java_AnnotationInstanceValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_java_annotationinstancevalue_has_id():
    assert hasattr(java_AnnotationInstanceValue, "id")
    descriptor = None
    for klass in java_AnnotationInstanceValue.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_java_annotationinstancevalue_has_name():
    assert hasattr(java_AnnotationInstanceValue, "name")
    descriptor = None
    for klass in java_AnnotationInstanceValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_annotationinstanceparameter_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationInstanceParameter)


def test_java_annotationinstanceparameter_constructor_exists():
    assert callable(java_AnnotationInstanceParameter.__init__)


def test_java_annotationinstanceparameter_constructor_args():
    sig = inspect.signature(java_AnnotationInstanceParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_annotationinstanceparameter_has_name():
    assert hasattr(java_AnnotationInstanceParameter, "name")
    descriptor = None
    for klass in java_AnnotationInstanceParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_annotationinstance_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationInstance)


def test_java_annotationinstance_constructor_exists():
    assert callable(java_AnnotationInstance.__init__)


def test_java_annotationinstance_constructor_args():
    sig = inspect.signature(java_AnnotationInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_annotationinstance_has_name():
    assert hasattr(java_AnnotationInstance, "name")
    descriptor = None
    for klass in java_AnnotationInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_annotable_is_not_abstract():
    assert not inspect.isabstract(java_Annotable)


def test_java_annotable_constructor_exists():
    assert callable(java_Annotable.__init__)


def test_java_annotable_constructor_args():
    sig = inspect.signature(java_Annotable.__init__)
    params = list(sig.parameters.keys())



def test_java_getexpression_is_not_abstract():
    assert not inspect.isabstract(java_GETExpression)


def test_java_getexpression_constructor_exists():
    assert callable(java_GETExpression.__init__)


def test_java_getexpression_constructor_args():
    sig = inspect.signature(java_GETExpression.__init__)
    params = list(sig.parameters.keys())
    assert "rightSide" in params, "Missing parameter 'rightSide'"
    assert "leftSide" in params, "Missing parameter 'leftSide'"

def test_java_getexpression_has_rightSide():
    assert hasattr(java_GETExpression, "rightSide")
    descriptor = None
    for klass in java_GETExpression.__mro__:
        if "rightSide" in klass.__dict__:
            descriptor = klass.__dict__["rightSide"]
            break
    assert isinstance(descriptor, property)

def test_java_getexpression_has_leftSide():
    assert hasattr(java_GETExpression, "leftSide")
    descriptor = None
    for klass in java_GETExpression.__mro__:
        if "leftSide" in klass.__dict__:
            descriptor = klass.__dict__["leftSide"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_assertstatement_is_not_abstract():
    assert not inspect.isabstract(java_AssertStatement)


def test_java_assertstatement_constructor_exists():
    assert callable(java_AssertStatement.__init__)


def test_java_assertstatement_constructor_args():
    sig = inspect.signature(java_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(java_Statement)


def test_java_statement_constructor_exists():
    assert callable(java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(java_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_statement_has_name():
    assert hasattr(java_Statement, "name")
    descriptor = None
    for klass in java_Statement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_argument_is_not_abstract():
    assert not inspect.isabstract(java_Argument)


def test_java_argument_constructor_exists():
    assert callable(java_Argument.__init__)


def test_java_argument_constructor_args():
    sig = inspect.signature(java_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_argument_has_order():
    assert hasattr(java_Argument, "order")
    descriptor = None
    for klass in java_Argument.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_java_argument_has_name():
    assert hasattr(java_Argument, "name")
    descriptor = None
    for klass in java_Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_container_is_not_abstract():
    assert not inspect.isabstract(java_Container)


def test_java_container_constructor_exists():
    assert callable(java_Container.__init__)


def test_java_container_constructor_args():
    sig = inspect.signature(java_Container.__init__)
    params = list(sig.parameters.keys())



def test_java_contained_is_not_abstract():
    assert not inspect.isabstract(java_Contained)


def test_java_contained_constructor_exists():
    assert callable(java_Contained.__init__)


def test_java_contained_constructor_args():
    sig = inspect.signature(java_Contained.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_java_contained_has_visibility():
    assert hasattr(java_Contained, "visibility")
    descriptor = None
    for klass in java_Contained.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_java_import_is_not_abstract():
    assert not inspect.isabstract(java_Import)


def test_java_import_constructor_exists():
    assert callable(java_Import.__init__)


def test_java_import_constructor_args():
    sig = inspect.signature(java_Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_import_has_name():
    assert hasattr(java_Import, "name")
    descriptor = None
    for klass in java_Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_genericbinding_is_not_abstract():
    assert not inspect.isabstract(java_GenericBinding)


def test_java_genericbinding_constructor_exists():
    assert callable(java_GenericBinding.__init__)


def test_java_genericbinding_constructor_args():
    sig = inspect.signature(java_GenericBinding.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_genericbinding_has_name():
    assert hasattr(java_GenericBinding, "name")
    descriptor = None
    for klass in java_GenericBinding.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_annotable_is_not_abstract():
    assert not inspect.isabstract(Annotable)


def test_annotable_constructor_exists():
    assert callable(Annotable.__init__)


def test_annotable_constructor_args():
    sig = inspect.signature(Annotable.__init__)
    params = list(sig.parameters.keys())



def test_contained_is_not_abstract():
    assert not inspect.isabstract(Contained)


def test_contained_constructor_exists():
    assert callable(Contained.__init__)


def test_contained_constructor_args():
    sig = inspect.signature(Contained.__init__)
    params = list(sig.parameters.keys())



def test_java_field_is_not_abstract():
    assert not inspect.isabstract(java_Field)


def test_java_field_constructor_exists():
    assert callable(java_Field.__init__)


def test_java_field_constructor_args():
    sig = inspect.signature(java_Field.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_java_field_has_isFinal():
    assert hasattr(java_Field, "isFinal")
    descriptor = None
    for klass in java_Field.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_name():
    assert hasattr(java_Field, "name")
    descriptor = None
    for klass in java_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_default():
    assert hasattr(java_Field, "default")
    descriptor = None
    for klass in java_Field.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_isStatic():
    assert hasattr(java_Field, "isStatic")
    descriptor = None
    for klass in java_Field.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_java_method_is_not_abstract():
    assert not inspect.isabstract(java_Method)


def test_java_method_constructor_exists():
    assert callable(java_Method.__init__)


def test_java_method_constructor_args():
    sig = inspect.signature(java_Method.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "concurrency" in params, "Missing parameter 'concurrency'"

def test_java_method_has_isDefault():
    assert hasattr(java_Method, "isDefault")
    descriptor = None
    for klass in java_Method.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)

def test_java_method_has_name():
    assert hasattr(java_Method, "name")
    descriptor = None
    for klass in java_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_method_has_isStatic():
    assert hasattr(java_Method, "isStatic")
    descriptor = None
    for klass in java_Method.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_java_method_has_isAbstract():
    assert hasattr(java_Method, "isAbstract")
    descriptor = None
    for klass in java_Method.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_java_method_has_isFinal():
    assert hasattr(java_Method, "isFinal")
    descriptor = None
    for klass in java_Method.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_java_method_has_concurrency():
    assert hasattr(java_Method, "concurrency")
    descriptor = None
    for klass in java_Method.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)



def test_java_generalization_is_not_abstract():
    assert not inspect.isabstract(java_Generalization)


def test_java_generalization_constructor_exists():
    assert callable(java_Generalization.__init__)


def test_java_generalization_constructor_args():
    sig = inspect.signature(java_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_generalization_has_name():
    assert hasattr(java_Generalization, "name")
    descriptor = None
    for klass in java_Generalization.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_interfaceimplementation_is_not_abstract():
    assert not inspect.isabstract(java_InterfaceImplementation)


def test_java_interfaceimplementation_constructor_exists():
    assert callable(java_InterfaceImplementation.__init__)


def test_java_interfaceimplementation_constructor_args():
    sig = inspect.signature(java_InterfaceImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_interfaceimplementation_has_name():
    assert hasattr(java_InterfaceImplementation, "name")
    descriptor = None
    for klass in java_InterfaceImplementation.__mro__:
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



def test_java_annotation_is_not_abstract():
    assert not inspect.isabstract(java_Annotation)


def test_java_annotation_constructor_exists():
    assert callable(java_Annotation.__init__)


def test_java_annotation_constructor_args():
    sig = inspect.signature(java_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_java_class_is_not_abstract():
    assert not inspect.isabstract(java_Class)


def test_java_class_constructor_exists():
    assert callable(java_Class.__init__)


def test_java_class_constructor_args():
    sig = inspect.signature(java_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_java_class_has_isStatic():
    assert hasattr(java_Class, "isStatic")
    descriptor = None
    for klass in java_Class.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_java_class_has_isFinal():
    assert hasattr(java_Class, "isFinal")
    descriptor = None
    for klass in java_Class.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_java_class_has_isAbstract():
    assert hasattr(java_Class, "isAbstract")
    descriptor = None
    for klass in java_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_java_interface_is_not_abstract():
    assert not inspect.isabstract(java_Interface)


def test_java_interface_constructor_exists():
    assert callable(java_Interface.__init__)


def test_java_interface_constructor_args():
    sig = inspect.signature(java_Interface.__init__)
    params = list(sig.parameters.keys())



def test_java_classifier_is_not_abstract():
    assert not inspect.isabstract(java_Classifier)


def test_java_classifier_constructor_exists():
    assert callable(java_Classifier.__init__)


def test_java_classifier_constructor_args():
    sig = inspect.signature(java_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_classifier_has_name():
    assert hasattr(java_Classifier, "name")
    descriptor = None
    for klass in java_Classifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(java_Package)


def test_java_package_constructor_exists():
    assert callable(java_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(java_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_package_has_name():
    assert hasattr(java_Package, "name")
    descriptor = None
    for klass in java_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_system_is_not_abstract():
    assert not inspect.isabstract(java_System)


def test_java_system_constructor_exists():
    assert callable(java_System.__init__)


def test_java_system_constructor_args():
    sig = inspect.signature(java_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_system_has_name():
    assert hasattr(java_System, "name")
    descriptor = None
    for klass in java_System.__mro__:
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
java_AnnotationInstanceValue_strategy = st.builds(
    java_AnnotationInstanceValue,
    value=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
java_AnnotationInstanceParameter_strategy = st.builds(
    java_AnnotationInstanceParameter,
    name=
        safe_text
)
java_AnnotationInstance_strategy = st.builds(
    java_AnnotationInstance,
    name=
        safe_text
)
java_Annotable_strategy = st.builds(
    java_Annotable,
)
java_GETExpression_strategy = st.builds(
    java_GETExpression,
    rightSide=
        safe_text,
    leftSide=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
java_AssertStatement_strategy = st.builds(
    java_AssertStatement,
)
java_Statement_strategy = st.builds(
    java_Statement,
    name=
        safe_text
)
java_Argument_strategy = st.builds(
    java_Argument,
    order=
        st.integers(),
    name=
        safe_text
)
java_Container_strategy = st.builds(
    java_Container,
)
java_Contained_strategy = st.builds(
    java_Contained,
    visibility=
        safe_text
)
java_Import_strategy = st.builds(
    java_Import,
    name=
        safe_text
)
java_GenericBinding_strategy = st.builds(
    java_GenericBinding,
    name=
        safe_text
)
Annotable_strategy = st.builds(
    Annotable,
)
Contained_strategy = st.builds(
    Contained,
)
java_Field_strategy = st.builds(
    java_Field,
    isFinal=
        st.booleans(),
    name=
        safe_text,
    default=
        safe_text,
    isStatic=
        st.booleans()
)
java_Method_strategy = st.builds(
    java_Method,
    isDefault=
        st.booleans(),
    name=
        safe_text,
    isStatic=
        st.booleans(),
    isAbstract=
        st.booleans(),
    isFinal=
        st.booleans(),
    concurrency=
        safe_text
)
java_Generalization_strategy = st.builds(
    java_Generalization,
    name=
        safe_text
)
java_InterfaceImplementation_strategy = st.builds(
    java_InterfaceImplementation,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
java_Annotation_strategy = st.builds(
    java_Annotation,
)
java_Class_strategy = st.builds(
    java_Class,
    isStatic=
        st.booleans(),
    isFinal=
        st.booleans(),
    isAbstract=
        st.booleans()
)
Container_strategy = st.builds(
    Container,
)
java_Interface_strategy = st.builds(
    java_Interface,
)
java_Classifier_strategy = st.builds(
    java_Classifier,
    name=
        safe_text
)
java_Package_strategy = st.builds(
    java_Package,
    name=
        safe_text
)
java_System_strategy = st.builds(
    java_System,
    name=
        safe_text
)

@given(instance=java_AnnotationInstanceValue_strategy)
@settings(max_examples=50)
def test_java_annotationinstancevalue_instantiation(instance):
    assert isinstance(instance, java_AnnotationInstanceValue)



@given(instance=java_AnnotationInstanceValue_strategy)
def test_java_annotationinstancevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=java_AnnotationInstanceValue_strategy)
def test_java_annotationinstancevalue_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=java_AnnotationInstanceValue_strategy)
def test_java_annotationinstancevalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_AnnotationInstanceParameter_strategy)
@settings(max_examples=50)
def test_java_annotationinstanceparameter_instantiation(instance):
    assert isinstance(instance, java_AnnotationInstanceParameter)



@given(instance=java_AnnotationInstanceParameter_strategy)
def test_java_annotationinstanceparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_AnnotationInstance_strategy)
@settings(max_examples=50)
def test_java_annotationinstance_instantiation(instance):
    assert isinstance(instance, java_AnnotationInstance)



@given(instance=java_AnnotationInstance_strategy)
def test_java_annotationinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Annotable_strategy)
@settings(max_examples=50)
def test_java_annotable_instantiation(instance):
    assert isinstance(instance, java_Annotable)

@given(instance=java_GETExpression_strategy)
@settings(max_examples=50)
def test_java_getexpression_instantiation(instance):
    assert isinstance(instance, java_GETExpression)



@given(instance=java_GETExpression_strategy)
def test_java_getexpression_rightSide_setter(instance):
    original = instance.rightSide
    instance.rightSide = original
    assert instance.rightSide == original



@given(instance=java_GETExpression_strategy)
def test_java_getexpression_leftSide_setter(instance):
    original = instance.leftSide
    instance.leftSide = original
    assert instance.leftSide == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=java_AssertStatement_strategy)
@settings(max_examples=50)
def test_java_assertstatement_instantiation(instance):
    assert isinstance(instance, java_AssertStatement)

@given(instance=java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, java_Statement)



@given(instance=java_Statement_strategy)
def test_java_statement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Argument_strategy)
@settings(max_examples=50)
def test_java_argument_instantiation(instance):
    assert isinstance(instance, java_Argument)



@given(instance=java_Argument_strategy)
def test_java_argument_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=java_Argument_strategy)
def test_java_argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Container_strategy)
@settings(max_examples=50)
def test_java_container_instantiation(instance):
    assert isinstance(instance, java_Container)

@given(instance=java_Contained_strategy)
@settings(max_examples=50)
def test_java_contained_instantiation(instance):
    assert isinstance(instance, java_Contained)



@given(instance=java_Contained_strategy)
def test_java_contained_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=java_Import_strategy)
@settings(max_examples=50)
def test_java_import_instantiation(instance):
    assert isinstance(instance, java_Import)



@given(instance=java_Import_strategy)
def test_java_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_GenericBinding_strategy)
@settings(max_examples=50)
def test_java_genericbinding_instantiation(instance):
    assert isinstance(instance, java_GenericBinding)



@given(instance=java_GenericBinding_strategy)
def test_java_genericbinding_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Annotable_strategy)
@settings(max_examples=50)
def test_annotable_instantiation(instance):
    assert isinstance(instance, Annotable)

@given(instance=Contained_strategy)
@settings(max_examples=50)
def test_contained_instantiation(instance):
    assert isinstance(instance, Contained)

@given(instance=java_Field_strategy)
@settings(max_examples=50)
def test_java_field_instantiation(instance):
    assert isinstance(instance, java_Field)



@given(instance=java_Field_strategy)
def test_java_field_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=java_Field_strategy)
def test_java_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Field_strategy)
def test_java_field_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=java_Field_strategy)
def test_java_field_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=java_Method_strategy)
@settings(max_examples=50)
def test_java_method_instantiation(instance):
    assert isinstance(instance, java_Method)



@given(instance=java_Method_strategy)
def test_java_method_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original



@given(instance=java_Method_strategy)
def test_java_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_Method_strategy)
def test_java_method_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=java_Method_strategy)
def test_java_method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=java_Method_strategy)
def test_java_method_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=java_Method_strategy)
def test_java_method_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original

@given(instance=java_Generalization_strategy)
@settings(max_examples=50)
def test_java_generalization_instantiation(instance):
    assert isinstance(instance, java_Generalization)



@given(instance=java_Generalization_strategy)
def test_java_generalization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_InterfaceImplementation_strategy)
@settings(max_examples=50)
def test_java_interfaceimplementation_instantiation(instance):
    assert isinstance(instance, java_InterfaceImplementation)



@given(instance=java_InterfaceImplementation_strategy)
def test_java_interfaceimplementation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=java_Annotation_strategy)
@settings(max_examples=50)
def test_java_annotation_instantiation(instance):
    assert isinstance(instance, java_Annotation)

@given(instance=java_Class_strategy)
@settings(max_examples=50)
def test_java_class_instantiation(instance):
    assert isinstance(instance, java_Class)



@given(instance=java_Class_strategy)
def test_java_class_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=java_Class_strategy)
def test_java_class_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=java_Class_strategy)
def test_java_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=java_Interface_strategy)
@settings(max_examples=50)
def test_java_interface_instantiation(instance):
    assert isinstance(instance, java_Interface)

@given(instance=java_Classifier_strategy)
@settings(max_examples=50)
def test_java_classifier_instantiation(instance):
    assert isinstance(instance, java_Classifier)



@given(instance=java_Classifier_strategy)
def test_java_classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, java_Package)



@given(instance=java_Package_strategy)
def test_java_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_System_strategy)
@settings(max_examples=50)
def test_java_system_instantiation(instance):
    assert isinstance(instance, java_System)



@given(instance=java_System_strategy)
def test_java_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

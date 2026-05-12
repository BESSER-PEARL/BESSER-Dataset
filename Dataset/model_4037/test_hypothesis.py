import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    uml_Element,
    Type,
    PackageableElement,
    uml_Type,
    Classifier,
    uml_Class,
    Package,
    uml_Model,
    TypedElement,
    uml_Behavior,
    NamedElement,
    uml_TypedElement,
    uml_Feature,
    Feature,
    Element,
    uml_Classifier,
    uml_Package,
    uml_Dependency,
    uml_PackageableElement,
    uml_NamedElement,
    uml_Parameter,
    uml_Property,
    uml_Operation,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml_element_is_not_abstract():
    assert not inspect.isabstract(uml_Element)


def test_uml_element_constructor_exists():
    assert callable(uml_Element.__init__)


def test_uml_element_constructor_args():
    sig = inspect.signature(uml_Element.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_type_is_not_abstract():
    assert not inspect.isabstract(uml_Type)


def test_uml_type_constructor_exists():
    assert callable(uml_Type.__init__)


def test_uml_type_constructor_args():
    sig = inspect.signature(uml_Type.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_uml_class_has_isAbstract():
    assert hasattr(uml_Class, "isAbstract")
    descriptor = None
    for klass in uml_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uml_class_has_isLeaf():
    assert hasattr(uml_Class, "isLeaf")
    descriptor = None
    for klass in uml_Class.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml_model_is_not_abstract():
    assert not inspect.isabstract(uml_Model)


def test_uml_model_constructor_exists():
    assert callable(uml_Model.__init__)


def test_uml_model_constructor_args():
    sig = inspect.signature(uml_Model.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_behavior_is_not_abstract():
    assert not inspect.isabstract(uml_Behavior)


def test_uml_behavior_constructor_exists():
    assert callable(uml_Behavior.__init__)


def test_uml_behavior_constructor_args():
    sig = inspect.signature(uml_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_typedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TypedElement)


def test_uml_typedelement_constructor_exists():
    assert callable(uml_TypedElement.__init__)


def test_uml_typedelement_constructor_args():
    sig = inspect.signature(uml_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_feature_is_not_abstract():
    assert not inspect.isabstract(uml_Feature)


def test_uml_feature_constructor_exists():
    assert callable(uml_Feature.__init__)


def test_uml_feature_constructor_args():
    sig = inspect.signature(uml_Feature.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml_classifier_is_not_abstract():
    assert not inspect.isabstract(uml_Classifier)


def test_uml_classifier_constructor_exists():
    assert callable(uml_Classifier.__init__)


def test_uml_classifier_constructor_args():
    sig = inspect.signature(uml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_package_is_not_abstract():
    assert not inspect.isabstract(uml_Package)


def test_uml_package_constructor_exists():
    assert callable(uml_Package.__init__)


def test_uml_package_constructor_args():
    sig = inspect.signature(uml_Package.__init__)
    params = list(sig.parameters.keys())



def test_uml_dependency_is_not_abstract():
    assert not inspect.isabstract(uml_Dependency)


def test_uml_dependency_constructor_exists():
    assert callable(uml_Dependency.__init__)


def test_uml_dependency_constructor_args():
    sig = inspect.signature(uml_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uml_PackageableElement)


def test_uml_packageableelement_constructor_exists():
    assert callable(uml_PackageableElement.__init__)


def test_uml_packageableelement_constructor_args():
    sig = inspect.signature(uml_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml_NamedElement)


def test_uml_namedelement_constructor_exists():
    assert callable(uml_NamedElement.__init__)


def test_uml_namedelement_constructor_args():
    sig = inspect.signature(uml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_uml_namedelement_has_visibility():
    assert hasattr(uml_NamedElement, "visibility")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml_namedelement_has_name():
    assert hasattr(uml_NamedElement, "name")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml_parameter_is_not_abstract():
    assert not inspect.isabstract(uml_Parameter)


def test_uml_parameter_constructor_exists():
    assert callable(uml_Parameter.__init__)


def test_uml_parameter_constructor_args():
    sig = inspect.signature(uml_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_property_is_not_abstract():
    assert not inspect.isabstract(uml_Property)


def test_uml_property_constructor_exists():
    assert callable(uml_Property.__init__)


def test_uml_property_constructor_args():
    sig = inspect.signature(uml_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml_operation_is_not_abstract():
    assert not inspect.isabstract(uml_Operation)


def test_uml_operation_constructor_exists():
    assert callable(uml_Operation.__init__)


def test_uml_operation_constructor_args():
    sig = inspect.signature(uml_Operation.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "package",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
Class_strategy = st.builds(
    Class,
)
uml_Element_strategy = st.builds(
    uml_Element,
)
Type_strategy = st.builds(
    Type,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uml_Type_strategy = st.builds(
    uml_Type,
)
Classifier_strategy = st.builds(
    Classifier,
)
uml_Class_strategy = st.builds(
    uml_Class,
    isAbstract=
        safe_text,
    isLeaf=
        safe_text
)
Package_strategy = st.builds(
    Package,
)
uml_Model_strategy = st.builds(
    uml_Model,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uml_Behavior_strategy = st.builds(
    uml_Behavior,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml_TypedElement_strategy = st.builds(
    uml_TypedElement,
)
uml_Feature_strategy = st.builds(
    uml_Feature,
)
Feature_strategy = st.builds(
    Feature,
)
Element_strategy = st.builds(
    Element,
)
uml_Classifier_strategy = st.builds(
    uml_Classifier,
)
uml_Package_strategy = st.builds(
    uml_Package,
)
uml_Dependency_strategy = st.builds(
    uml_Dependency,
)
uml_PackageableElement_strategy = st.builds(
    uml_PackageableElement,
)
uml_NamedElement_strategy = st.builds(
    uml_NamedElement,
    visibility=
        safe_text,
    name=
        safe_text
)
uml_Parameter_strategy = st.builds(
    uml_Parameter,
)
uml_Property_strategy = st.builds(
    uml_Property,
)
uml_Operation_strategy = st.builds(
    uml_Operation,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=uml_Element_strategy)
@settings(max_examples=50)
def test_uml_element_instantiation(instance):
    assert isinstance(instance, uml_Element)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uml_Type_strategy)
@settings(max_examples=50)
def test_uml_type_instantiation(instance):
    assert isinstance(instance, uml_Type)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uml_Class_strategy)
@settings(max_examples=50)
def test_uml_class_instantiation(instance):
    assert isinstance(instance, uml_Class)



@given(instance=uml_Class_strategy)
def test_uml_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=uml_Class_strategy)
def test_uml_class_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=uml_Model_strategy)
@settings(max_examples=50)
def test_uml_model_instantiation(instance):
    assert isinstance(instance, uml_Model)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=uml_Behavior_strategy)
@settings(max_examples=50)
def test_uml_behavior_instantiation(instance):
    assert isinstance(instance, uml_Behavior)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml_TypedElement_strategy)
@settings(max_examples=50)
def test_uml_typedelement_instantiation(instance):
    assert isinstance(instance, uml_TypedElement)

@given(instance=uml_Feature_strategy)
@settings(max_examples=50)
def test_uml_feature_instantiation(instance):
    assert isinstance(instance, uml_Feature)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uml_Classifier_strategy)
@settings(max_examples=50)
def test_uml_classifier_instantiation(instance):
    assert isinstance(instance, uml_Classifier)

@given(instance=uml_Package_strategy)
@settings(max_examples=50)
def test_uml_package_instantiation(instance):
    assert isinstance(instance, uml_Package)

@given(instance=uml_Dependency_strategy)
@settings(max_examples=50)
def test_uml_dependency_instantiation(instance):
    assert isinstance(instance, uml_Dependency)

@given(instance=uml_PackageableElement_strategy)
@settings(max_examples=50)
def test_uml_packageableelement_instantiation(instance):
    assert isinstance(instance, uml_PackageableElement)

@given(instance=uml_NamedElement_strategy)
@settings(max_examples=50)
def test_uml_namedelement_instantiation(instance):
    assert isinstance(instance, uml_NamedElement)



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml_Parameter_strategy)
@settings(max_examples=50)
def test_uml_parameter_instantiation(instance):
    assert isinstance(instance, uml_Parameter)

@given(instance=uml_Property_strategy)
@settings(max_examples=50)
def test_uml_property_instantiation(instance):
    assert isinstance(instance, uml_Property)

@given(instance=uml_Operation_strategy)
@settings(max_examples=50)
def test_uml_operation_instantiation(instance):
    assert isinstance(instance, uml_Operation)

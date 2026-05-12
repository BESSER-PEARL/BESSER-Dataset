import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuralFeature,
    oml_Attribute,
    oml_Reference,
    AnnotatedElement,
    oml_NamedElement,
    oml_Annotation,
    oml_AnnotatedElement,
    Feature,
    oml_Operation,
    oml_StructuralFeature,
    Classifier,
    oml_Datatype,
    oml_Class,
    Class,
    oml_ExternalClass,
    PackageableElement,
    oml_Classifier,
    oml_Package,
    NamedElement,
    oml_Parameter,
    oml_Feature,
    oml_PackageableElement,
    Package,
    oml_Model,
    VisibilityEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_oml_attribute_is_not_abstract():
    assert not inspect.isabstract(oml_Attribute)


def test_oml_attribute_constructor_exists():
    assert callable(oml_Attribute.__init__)


def test_oml_attribute_constructor_args():
    sig = inspect.signature(oml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_oml_reference_is_not_abstract():
    assert not inspect.isabstract(oml_Reference)


def test_oml_reference_constructor_exists():
    assert callable(oml_Reference.__init__)


def test_oml_reference_constructor_args():
    sig = inspect.signature(oml_Reference.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oml_namedelement_is_not_abstract():
    assert not inspect.isabstract(oml_NamedElement)


def test_oml_namedelement_constructor_exists():
    assert callable(oml_NamedElement.__init__)


def test_oml_namedelement_constructor_args():
    sig = inspect.signature(oml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oml_namedelement_has_name():
    assert hasattr(oml_NamedElement, "name")
    descriptor = None
    for klass in oml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oml_annotation_is_not_abstract():
    assert not inspect.isabstract(oml_Annotation)


def test_oml_annotation_constructor_exists():
    assert callable(oml_Annotation.__init__)


def test_oml_annotation_constructor_args():
    sig = inspect.signature(oml_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_oml_annotation_has_key():
    assert hasattr(oml_Annotation, "key")
    descriptor = None
    for klass in oml_Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_oml_annotation_has_value():
    assert hasattr(oml_Annotation, "value")
    descriptor = None
    for klass in oml_Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oml_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(oml_AnnotatedElement)


def test_oml_annotatedelement_constructor_exists():
    assert callable(oml_AnnotatedElement.__init__)


def test_oml_annotatedelement_constructor_args():
    sig = inspect.signature(oml_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_oml_operation_is_not_abstract():
    assert not inspect.isabstract(oml_Operation)


def test_oml_operation_constructor_exists():
    assert callable(oml_Operation.__init__)


def test_oml_operation_constructor_args():
    sig = inspect.signature(oml_Operation.__init__)
    params = list(sig.parameters.keys())



def test_oml_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(oml_StructuralFeature)


def test_oml_structuralfeature_constructor_exists():
    assert callable(oml_StructuralFeature.__init__)


def test_oml_structuralfeature_constructor_args():
    sig = inspect.signature(oml_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_oml_structuralfeature_has_isMany():
    assert hasattr(oml_StructuralFeature, "isMany")
    descriptor = None
    for klass in oml_StructuralFeature.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_oml_datatype_is_not_abstract():
    assert not inspect.isabstract(oml_Datatype)


def test_oml_datatype_constructor_exists():
    assert callable(oml_Datatype.__init__)


def test_oml_datatype_constructor_args():
    sig = inspect.signature(oml_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_oml_class_is_not_abstract():
    assert not inspect.isabstract(oml_Class)


def test_oml_class_constructor_exists():
    assert callable(oml_Class.__init__)


def test_oml_class_constructor_args():
    sig = inspect.signature(oml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_oml_class_has_isAbstract():
    assert hasattr(oml_Class, "isAbstract")
    descriptor = None
    for klass in oml_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_oml_externalclass_is_not_abstract():
    assert not inspect.isabstract(oml_ExternalClass)


def test_oml_externalclass_constructor_exists():
    assert callable(oml_ExternalClass.__init__)


def test_oml_externalclass_constructor_args():
    sig = inspect.signature(oml_ExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_oml_classifier_is_not_abstract():
    assert not inspect.isabstract(oml_Classifier)


def test_oml_classifier_constructor_exists():
    assert callable(oml_Classifier.__init__)


def test_oml_classifier_constructor_args():
    sig = inspect.signature(oml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_oml_package_is_not_abstract():
    assert not inspect.isabstract(oml_Package)


def test_oml_package_constructor_exists():
    assert callable(oml_Package.__init__)


def test_oml_package_constructor_args():
    sig = inspect.signature(oml_Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_oml_parameter_is_not_abstract():
    assert not inspect.isabstract(oml_Parameter)


def test_oml_parameter_constructor_exists():
    assert callable(oml_Parameter.__init__)


def test_oml_parameter_constructor_args():
    sig = inspect.signature(oml_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oml_feature_is_not_abstract():
    assert not inspect.isabstract(oml_Feature)


def test_oml_feature_constructor_exists():
    assert callable(oml_Feature.__init__)


def test_oml_feature_constructor_args():
    sig = inspect.signature(oml_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oml_feature_has_visibility():
    assert hasattr(oml_Feature, "visibility")
    descriptor = None
    for klass in oml_Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_oml_packageableelement_is_not_abstract():
    assert not inspect.isabstract(oml_PackageableElement)


def test_oml_packageableelement_constructor_exists():
    assert callable(oml_PackageableElement.__init__)


def test_oml_packageableelement_constructor_args():
    sig = inspect.signature(oml_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_oml_model_is_not_abstract():
    assert not inspect.isabstract(oml_Model)


def test_oml_model_constructor_exists():
    assert callable(oml_Model.__init__)


def test_oml_model_constructor_args():
    sig = inspect.signature(oml_Model.__init__)
    params = list(sig.parameters.keys())

def test_visibilityenum_exists():
    # Check that the Enumeration exists
    assert VisibilityEnum is not None

def test_visibilityenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityEnum]
    expected_literals = [
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityEnum"


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
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
oml_Attribute_strategy = st.builds(
    oml_Attribute,
)
oml_Reference_strategy = st.builds(
    oml_Reference,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
oml_NamedElement_strategy = st.builds(
    oml_NamedElement,
    name=
        safe_text
)
oml_Annotation_strategy = st.builds(
    oml_Annotation,
    key=
        safe_text,
    value=
        safe_text
)
oml_AnnotatedElement_strategy = st.builds(
    oml_AnnotatedElement,
)
Feature_strategy = st.builds(
    Feature,
)
oml_Operation_strategy = st.builds(
    oml_Operation,
)
oml_StructuralFeature_strategy = st.builds(
    oml_StructuralFeature,
    isMany=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
oml_Datatype_strategy = st.builds(
    oml_Datatype,
)
oml_Class_strategy = st.builds(
    oml_Class,
    isAbstract=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
oml_ExternalClass_strategy = st.builds(
    oml_ExternalClass,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
oml_Classifier_strategy = st.builds(
    oml_Classifier,
)
oml_Package_strategy = st.builds(
    oml_Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
oml_Parameter_strategy = st.builds(
    oml_Parameter,
)
oml_Feature_strategy = st.builds(
    oml_Feature,
    visibility=
        safe_text
)
oml_PackageableElement_strategy = st.builds(
    oml_PackageableElement,
)
Package_strategy = st.builds(
    Package,
)
oml_Model_strategy = st.builds(
    oml_Model,
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=oml_Attribute_strategy)
@settings(max_examples=50)
def test_oml_attribute_instantiation(instance):
    assert isinstance(instance, oml_Attribute)

@given(instance=oml_Reference_strategy)
@settings(max_examples=50)
def test_oml_reference_instantiation(instance):
    assert isinstance(instance, oml_Reference)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=oml_NamedElement_strategy)
@settings(max_examples=50)
def test_oml_namedelement_instantiation(instance):
    assert isinstance(instance, oml_NamedElement)



@given(instance=oml_NamedElement_strategy)
def test_oml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oml_Annotation_strategy)
@settings(max_examples=50)
def test_oml_annotation_instantiation(instance):
    assert isinstance(instance, oml_Annotation)



@given(instance=oml_Annotation_strategy)
def test_oml_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=oml_Annotation_strategy)
def test_oml_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oml_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_oml_annotatedelement_instantiation(instance):
    assert isinstance(instance, oml_AnnotatedElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=oml_Operation_strategy)
@settings(max_examples=50)
def test_oml_operation_instantiation(instance):
    assert isinstance(instance, oml_Operation)

@given(instance=oml_StructuralFeature_strategy)
@settings(max_examples=50)
def test_oml_structuralfeature_instantiation(instance):
    assert isinstance(instance, oml_StructuralFeature)



@given(instance=oml_StructuralFeature_strategy)
def test_oml_structuralfeature_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=oml_Datatype_strategy)
@settings(max_examples=50)
def test_oml_datatype_instantiation(instance):
    assert isinstance(instance, oml_Datatype)

@given(instance=oml_Class_strategy)
@settings(max_examples=50)
def test_oml_class_instantiation(instance):
    assert isinstance(instance, oml_Class)



@given(instance=oml_Class_strategy)
def test_oml_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=oml_ExternalClass_strategy)
@settings(max_examples=50)
def test_oml_externalclass_instantiation(instance):
    assert isinstance(instance, oml_ExternalClass)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=oml_Classifier_strategy)
@settings(max_examples=50)
def test_oml_classifier_instantiation(instance):
    assert isinstance(instance, oml_Classifier)

@given(instance=oml_Package_strategy)
@settings(max_examples=50)
def test_oml_package_instantiation(instance):
    assert isinstance(instance, oml_Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=oml_Parameter_strategy)
@settings(max_examples=50)
def test_oml_parameter_instantiation(instance):
    assert isinstance(instance, oml_Parameter)

@given(instance=oml_Feature_strategy)
@settings(max_examples=50)
def test_oml_feature_instantiation(instance):
    assert isinstance(instance, oml_Feature)



@given(instance=oml_Feature_strategy)
def test_oml_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oml_PackageableElement_strategy)
@settings(max_examples=50)
def test_oml_packageableelement_instantiation(instance):
    assert isinstance(instance, oml_PackageableElement)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=oml_Model_strategy)
@settings(max_examples=50)
def test_oml_model_instantiation(instance):
    assert isinstance(instance, oml_Model)

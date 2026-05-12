import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuralFeature,
    OO_Attribute,
    OO_Reference,
    Feature,
    OO_Operation,
    OO_StructuralFeature,
    Classifier,
    OO_Class,
    Class,
    OO_ExternalClass,
    PackageableElement,
    OO_Classifier,
    AnnotatedElement,
    OO_NamedElement,
    OO_Annotation,
    OO_AnnotatedElement,
    OO_Package,
    NamedElement,
    OO_Parameter,
    OO_PackageableElement,
    Package,
    OO_Model,
    OO_Datatype,
    OO_Feature,
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



def test_oo_attribute_is_not_abstract():
    assert not inspect.isabstract(OO_Attribute)


def test_oo_attribute_constructor_exists():
    assert callable(OO_Attribute.__init__)


def test_oo_attribute_constructor_args():
    sig = inspect.signature(OO_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_oo_reference_is_not_abstract():
    assert not inspect.isabstract(OO_Reference)


def test_oo_reference_constructor_exists():
    assert callable(OO_Reference.__init__)


def test_oo_reference_constructor_args():
    sig = inspect.signature(OO_Reference.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_oo_operation_is_not_abstract():
    assert not inspect.isabstract(OO_Operation)


def test_oo_operation_constructor_exists():
    assert callable(OO_Operation.__init__)


def test_oo_operation_constructor_args():
    sig = inspect.signature(OO_Operation.__init__)
    params = list(sig.parameters.keys())



def test_oo_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(OO_StructuralFeature)


def test_oo_structuralfeature_constructor_exists():
    assert callable(OO_StructuralFeature.__init__)


def test_oo_structuralfeature_constructor_args():
    sig = inspect.signature(OO_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_oo_structuralfeature_has_isMany():
    assert hasattr(OO_StructuralFeature, "isMany")
    descriptor = None
    for klass in OO_StructuralFeature.__mro__:
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



def test_oo_class_is_not_abstract():
    assert not inspect.isabstract(OO_Class)


def test_oo_class_constructor_exists():
    assert callable(OO_Class.__init__)


def test_oo_class_constructor_args():
    sig = inspect.signature(OO_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_oo_class_has_isAbstract():
    assert hasattr(OO_Class, "isAbstract")
    descriptor = None
    for klass in OO_Class.__mro__:
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



def test_oo_externalclass_is_not_abstract():
    assert not inspect.isabstract(OO_ExternalClass)


def test_oo_externalclass_constructor_exists():
    assert callable(OO_ExternalClass.__init__)


def test_oo_externalclass_constructor_args():
    sig = inspect.signature(OO_ExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_oo_classifier_is_not_abstract():
    assert not inspect.isabstract(OO_Classifier)


def test_oo_classifier_constructor_exists():
    assert callable(OO_Classifier.__init__)


def test_oo_classifier_constructor_args():
    sig = inspect.signature(OO_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo_namedelement_is_not_abstract():
    assert not inspect.isabstract(OO_NamedElement)


def test_oo_namedelement_constructor_exists():
    assert callable(OO_NamedElement.__init__)


def test_oo_namedelement_constructor_args():
    sig = inspect.signature(OO_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oo_namedelement_has_name():
    assert hasattr(OO_NamedElement, "name")
    descriptor = None
    for klass in OO_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oo_annotation_is_not_abstract():
    assert not inspect.isabstract(OO_Annotation)


def test_oo_annotation_constructor_exists():
    assert callable(OO_Annotation.__init__)


def test_oo_annotation_constructor_args():
    sig = inspect.signature(OO_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_oo_annotation_has_value():
    assert hasattr(OO_Annotation, "value")
    descriptor = None
    for klass in OO_Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_oo_annotation_has_key():
    assert hasattr(OO_Annotation, "key")
    descriptor = None
    for klass in OO_Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_oo_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(OO_AnnotatedElement)


def test_oo_annotatedelement_constructor_exists():
    assert callable(OO_AnnotatedElement.__init__)


def test_oo_annotatedelement_constructor_args():
    sig = inspect.signature(OO_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo_package_is_not_abstract():
    assert not inspect.isabstract(OO_Package)


def test_oo_package_constructor_exists():
    assert callable(OO_Package.__init__)


def test_oo_package_constructor_args():
    sig = inspect.signature(OO_Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo_parameter_is_not_abstract():
    assert not inspect.isabstract(OO_Parameter)


def test_oo_parameter_constructor_exists():
    assert callable(OO_Parameter.__init__)


def test_oo_parameter_constructor_args():
    sig = inspect.signature(OO_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oo_packageableelement_is_not_abstract():
    assert not inspect.isabstract(OO_PackageableElement)


def test_oo_packageableelement_constructor_exists():
    assert callable(OO_PackageableElement.__init__)


def test_oo_packageableelement_constructor_args():
    sig = inspect.signature(OO_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_oo_model_is_not_abstract():
    assert not inspect.isabstract(OO_Model)


def test_oo_model_constructor_exists():
    assert callable(OO_Model.__init__)


def test_oo_model_constructor_args():
    sig = inspect.signature(OO_Model.__init__)
    params = list(sig.parameters.keys())



def test_oo_datatype_is_not_abstract():
    assert not inspect.isabstract(OO_Datatype)


def test_oo_datatype_constructor_exists():
    assert callable(OO_Datatype.__init__)


def test_oo_datatype_constructor_args():
    sig = inspect.signature(OO_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_oo_feature_is_not_abstract():
    assert not inspect.isabstract(OO_Feature)


def test_oo_feature_constructor_exists():
    assert callable(OO_Feature.__init__)


def test_oo_feature_constructor_args():
    sig = inspect.signature(OO_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oo_feature_has_visibility():
    assert hasattr(OO_Feature, "visibility")
    descriptor = None
    for klass in OO_Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_visibilityenum_exists():
    # Check that the Enumeration exists
    assert VisibilityEnum is not None

def test_visibilityenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityEnum]
    expected_literals = [
        "private",
        "public",
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
OO_Attribute_strategy = st.builds(
    OO_Attribute,
)
OO_Reference_strategy = st.builds(
    OO_Reference,
)
Feature_strategy = st.builds(
    Feature,
)
OO_Operation_strategy = st.builds(
    OO_Operation,
)
OO_StructuralFeature_strategy = st.builds(
    OO_StructuralFeature,
    isMany=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
OO_Class_strategy = st.builds(
    OO_Class,
    isAbstract=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
OO_ExternalClass_strategy = st.builds(
    OO_ExternalClass,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
OO_Classifier_strategy = st.builds(
    OO_Classifier,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
OO_NamedElement_strategy = st.builds(
    OO_NamedElement,
    name=
        safe_text
)
OO_Annotation_strategy = st.builds(
    OO_Annotation,
    value=
        safe_text,
    key=
        safe_text
)
OO_AnnotatedElement_strategy = st.builds(
    OO_AnnotatedElement,
)
OO_Package_strategy = st.builds(
    OO_Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OO_Parameter_strategy = st.builds(
    OO_Parameter,
)
OO_PackageableElement_strategy = st.builds(
    OO_PackageableElement,
)
Package_strategy = st.builds(
    Package,
)
OO_Model_strategy = st.builds(
    OO_Model,
)
OO_Datatype_strategy = st.builds(
    OO_Datatype,
)
OO_Feature_strategy = st.builds(
    OO_Feature,
    visibility=
        safe_text
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=OO_Attribute_strategy)
@settings(max_examples=50)
def test_oo_attribute_instantiation(instance):
    assert isinstance(instance, OO_Attribute)

@given(instance=OO_Reference_strategy)
@settings(max_examples=50)
def test_oo_reference_instantiation(instance):
    assert isinstance(instance, OO_Reference)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=OO_Operation_strategy)
@settings(max_examples=50)
def test_oo_operation_instantiation(instance):
    assert isinstance(instance, OO_Operation)

@given(instance=OO_StructuralFeature_strategy)
@settings(max_examples=50)
def test_oo_structuralfeature_instantiation(instance):
    assert isinstance(instance, OO_StructuralFeature)



@given(instance=OO_StructuralFeature_strategy)
def test_oo_structuralfeature_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=OO_Class_strategy)
@settings(max_examples=50)
def test_oo_class_instantiation(instance):
    assert isinstance(instance, OO_Class)



@given(instance=OO_Class_strategy)
def test_oo_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OO_ExternalClass_strategy)
@settings(max_examples=50)
def test_oo_externalclass_instantiation(instance):
    assert isinstance(instance, OO_ExternalClass)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=OO_Classifier_strategy)
@settings(max_examples=50)
def test_oo_classifier_instantiation(instance):
    assert isinstance(instance, OO_Classifier)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=OO_NamedElement_strategy)
@settings(max_examples=50)
def test_oo_namedelement_instantiation(instance):
    assert isinstance(instance, OO_NamedElement)



@given(instance=OO_NamedElement_strategy)
def test_oo_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OO_Annotation_strategy)
@settings(max_examples=50)
def test_oo_annotation_instantiation(instance):
    assert isinstance(instance, OO_Annotation)



@given(instance=OO_Annotation_strategy)
def test_oo_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=OO_Annotation_strategy)
def test_oo_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=OO_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_oo_annotatedelement_instantiation(instance):
    assert isinstance(instance, OO_AnnotatedElement)

@given(instance=OO_Package_strategy)
@settings(max_examples=50)
def test_oo_package_instantiation(instance):
    assert isinstance(instance, OO_Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=OO_Parameter_strategy)
@settings(max_examples=50)
def test_oo_parameter_instantiation(instance):
    assert isinstance(instance, OO_Parameter)

@given(instance=OO_PackageableElement_strategy)
@settings(max_examples=50)
def test_oo_packageableelement_instantiation(instance):
    assert isinstance(instance, OO_PackageableElement)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=OO_Model_strategy)
@settings(max_examples=50)
def test_oo_model_instantiation(instance):
    assert isinstance(instance, OO_Model)

@given(instance=OO_Datatype_strategy)
@settings(max_examples=50)
def test_oo_datatype_instantiation(instance):
    assert isinstance(instance, OO_Datatype)

@given(instance=OO_Feature_strategy)
@settings(max_examples=50)
def test_oo_feature_instantiation(instance):
    assert isinstance(instance, OO_Feature)



@given(instance=OO_Feature_strategy)
def test_oo_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

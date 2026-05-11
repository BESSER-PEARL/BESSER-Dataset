import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuralFeature,
    oml::Attribute,
    oml::Reference,
    AnnotatedElement,
    oml::NamedElement,
    oml::Annotation,
    oml::AnnotatedElement,
    Feature,
    oml::Operation,
    oml::StructuralFeature,
    Classifier,
    oml::Datatype,
    oml::Class,
    Class,
    oml::ExternalClass,
    PackageableElement,
    oml::Classifier,
    oml::Package,
    NamedElement,
    oml::Feature,
    oml::Parameter,
    oml::PackageableElement,
    Package,
    oml::Model,
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



def test_oml::attribute_is_not_abstract():
    assert not inspect.isabstract(oml::Attribute)


def test_oml::attribute_constructor_exists():
    assert callable(oml::Attribute.__init__)


def test_oml::attribute_constructor_args():
    sig = inspect.signature(oml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_oml::reference_is_not_abstract():
    assert not inspect.isabstract(oml::Reference)


def test_oml::reference_constructor_exists():
    assert callable(oml::Reference.__init__)


def test_oml::reference_constructor_args():
    sig = inspect.signature(oml::Reference.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oml::namedelement_is_not_abstract():
    assert not inspect.isabstract(oml::NamedElement)


def test_oml::namedelement_constructor_exists():
    assert callable(oml::NamedElement.__init__)


def test_oml::namedelement_constructor_args():
    sig = inspect.signature(oml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oml::namedelement_has_name():
    assert hasattr(oml::NamedElement, "name")
    descriptor = None
    for klass in oml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oml::annotation_is_not_abstract():
    assert not inspect.isabstract(oml::Annotation)


def test_oml::annotation_constructor_exists():
    assert callable(oml::Annotation.__init__)


def test_oml::annotation_constructor_args():
    sig = inspect.signature(oml::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_oml::annotation_has_key():
    assert hasattr(oml::Annotation, "key")
    descriptor = None
    for klass in oml::Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_oml::annotation_has_value():
    assert hasattr(oml::Annotation, "value")
    descriptor = None
    for klass in oml::Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oml::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(oml::AnnotatedElement)


def test_oml::annotatedelement_constructor_exists():
    assert callable(oml::AnnotatedElement.__init__)


def test_oml::annotatedelement_constructor_args():
    sig = inspect.signature(oml::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_oml::operation_is_not_abstract():
    assert not inspect.isabstract(oml::Operation)


def test_oml::operation_constructor_exists():
    assert callable(oml::Operation.__init__)


def test_oml::operation_constructor_args():
    sig = inspect.signature(oml::Operation.__init__)
    params = list(sig.parameters.keys())



def test_oml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(oml::StructuralFeature)


def test_oml::structuralfeature_constructor_exists():
    assert callable(oml::StructuralFeature.__init__)


def test_oml::structuralfeature_constructor_args():
    sig = inspect.signature(oml::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_oml::structuralfeature_has_isMany():
    assert hasattr(oml::StructuralFeature, "isMany")
    descriptor = None
    for klass in oml::StructuralFeature.__mro__:
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



def test_oml::datatype_is_not_abstract():
    assert not inspect.isabstract(oml::Datatype)


def test_oml::datatype_constructor_exists():
    assert callable(oml::Datatype.__init__)


def test_oml::datatype_constructor_args():
    sig = inspect.signature(oml::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_oml::class_is_not_abstract():
    assert not inspect.isabstract(oml::Class)


def test_oml::class_constructor_exists():
    assert callable(oml::Class.__init__)


def test_oml::class_constructor_args():
    sig = inspect.signature(oml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_oml::class_has_isAbstract():
    assert hasattr(oml::Class, "isAbstract")
    descriptor = None
    for klass in oml::Class.__mro__:
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



def test_oml::externalclass_is_not_abstract():
    assert not inspect.isabstract(oml::ExternalClass)


def test_oml::externalclass_constructor_exists():
    assert callable(oml::ExternalClass.__init__)


def test_oml::externalclass_constructor_args():
    sig = inspect.signature(oml::ExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_oml::classifier_is_not_abstract():
    assert not inspect.isabstract(oml::Classifier)


def test_oml::classifier_constructor_exists():
    assert callable(oml::Classifier.__init__)


def test_oml::classifier_constructor_args():
    sig = inspect.signature(oml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_oml::package_is_not_abstract():
    assert not inspect.isabstract(oml::Package)


def test_oml::package_constructor_exists():
    assert callable(oml::Package.__init__)


def test_oml::package_constructor_args():
    sig = inspect.signature(oml::Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_oml::feature_is_not_abstract():
    assert not inspect.isabstract(oml::Feature)


def test_oml::feature_constructor_exists():
    assert callable(oml::Feature.__init__)


def test_oml::feature_constructor_args():
    sig = inspect.signature(oml::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oml::feature_has_visibility():
    assert hasattr(oml::Feature, "visibility")
    descriptor = None
    for klass in oml::Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_oml::parameter_is_not_abstract():
    assert not inspect.isabstract(oml::Parameter)


def test_oml::parameter_constructor_exists():
    assert callable(oml::Parameter.__init__)


def test_oml::parameter_constructor_args():
    sig = inspect.signature(oml::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oml::packageableelement_is_not_abstract():
    assert not inspect.isabstract(oml::PackageableElement)


def test_oml::packageableelement_constructor_exists():
    assert callable(oml::PackageableElement.__init__)


def test_oml::packageableelement_constructor_args():
    sig = inspect.signature(oml::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_oml::model_is_not_abstract():
    assert not inspect.isabstract(oml::Model)


def test_oml::model_constructor_exists():
    assert callable(oml::Model.__init__)


def test_oml::model_constructor_args():
    sig = inspect.signature(oml::Model.__init__)
    params = list(sig.parameters.keys())

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
oml::Attribute_strategy = st.builds(
    oml::Attribute,
)
oml::Reference_strategy = st.builds(
    oml::Reference,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
oml::NamedElement_strategy = st.builds(
    oml::NamedElement,
    name=
        safe_text
)
oml::Annotation_strategy = st.builds(
    oml::Annotation,
    key=
        safe_text,
    value=
        safe_text
)
oml::AnnotatedElement_strategy = st.builds(
    oml::AnnotatedElement,
)
Feature_strategy = st.builds(
    Feature,
)
oml::Operation_strategy = st.builds(
    oml::Operation,
)
oml::StructuralFeature_strategy = st.builds(
    oml::StructuralFeature,
    isMany=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
oml::Datatype_strategy = st.builds(
    oml::Datatype,
)
oml::Class_strategy = st.builds(
    oml::Class,
    isAbstract=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
oml::ExternalClass_strategy = st.builds(
    oml::ExternalClass,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
oml::Classifier_strategy = st.builds(
    oml::Classifier,
)
oml::Package_strategy = st.builds(
    oml::Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
oml::Feature_strategy = st.builds(
    oml::Feature,
    visibility=
        safe_text
)
oml::Parameter_strategy = st.builds(
    oml::Parameter,
)
oml::PackageableElement_strategy = st.builds(
    oml::PackageableElement,
)
Package_strategy = st.builds(
    Package,
)
oml::Model_strategy = st.builds(
    oml::Model,
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=oml::Attribute_strategy)
@settings(max_examples=50)
def test_oml::attribute_instantiation(instance):
    assert isinstance(instance, oml::Attribute)

@given(instance=oml::Reference_strategy)
@settings(max_examples=50)
def test_oml::reference_instantiation(instance):
    assert isinstance(instance, oml::Reference)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=oml::NamedElement_strategy)
@settings(max_examples=50)
def test_oml::namedelement_instantiation(instance):
    assert isinstance(instance, oml::NamedElement)

@given(instance=oml::NamedElement_strategy)
def test_oml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oml::NamedElement_strategy)
def test_oml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oml::Annotation_strategy)
@settings(max_examples=50)
def test_oml::annotation_instantiation(instance):
    assert isinstance(instance, oml::Annotation)

@given(instance=oml::Annotation_strategy)
def test_oml::annotation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=oml::Annotation_strategy)
def test_oml::annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=oml::Annotation_strategy)
def test_oml::annotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oml::Annotation_strategy)
def test_oml::annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oml::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_oml::annotatedelement_instantiation(instance):
    assert isinstance(instance, oml::AnnotatedElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=oml::Operation_strategy)
@settings(max_examples=50)
def test_oml::operation_instantiation(instance):
    assert isinstance(instance, oml::Operation)

@given(instance=oml::StructuralFeature_strategy)
@settings(max_examples=50)
def test_oml::structuralfeature_instantiation(instance):
    assert isinstance(instance, oml::StructuralFeature)

@given(instance=oml::StructuralFeature_strategy)
def test_oml::structuralfeature_isMany_type(instance):
    assert isinstance(instance.isMany, str)


@given(instance=oml::StructuralFeature_strategy)
def test_oml::structuralfeature_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=oml::Datatype_strategy)
@settings(max_examples=50)
def test_oml::datatype_instantiation(instance):
    assert isinstance(instance, oml::Datatype)

@given(instance=oml::Class_strategy)
@settings(max_examples=50)
def test_oml::class_instantiation(instance):
    assert isinstance(instance, oml::Class)

@given(instance=oml::Class_strategy)
def test_oml::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=oml::Class_strategy)
def test_oml::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=oml::ExternalClass_strategy)
@settings(max_examples=50)
def test_oml::externalclass_instantiation(instance):
    assert isinstance(instance, oml::ExternalClass)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=oml::Classifier_strategy)
@settings(max_examples=50)
def test_oml::classifier_instantiation(instance):
    assert isinstance(instance, oml::Classifier)

@given(instance=oml::Package_strategy)
@settings(max_examples=50)
def test_oml::package_instantiation(instance):
    assert isinstance(instance, oml::Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=oml::Feature_strategy)
@settings(max_examples=50)
def test_oml::feature_instantiation(instance):
    assert isinstance(instance, oml::Feature)

@given(instance=oml::Feature_strategy)
def test_oml::feature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=oml::Feature_strategy)
def test_oml::feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=oml::Parameter_strategy)
@settings(max_examples=50)
def test_oml::parameter_instantiation(instance):
    assert isinstance(instance, oml::Parameter)

@given(instance=oml::PackageableElement_strategy)
@settings(max_examples=50)
def test_oml::packageableelement_instantiation(instance):
    assert isinstance(instance, oml::PackageableElement)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=oml::Model_strategy)
@settings(max_examples=50)
def test_oml::model_instantiation(instance):
    assert isinstance(instance, oml::Model)

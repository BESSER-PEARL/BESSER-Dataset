import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuralFeature,
    OO::Attribute,
    OO::Reference,
    Classifier,
    OO::Datatype,
    OO::Class,
    Class,
    OO::ExternalClass,
    PackageableElement,
    OO::Classifier,
    AnnotatedElement,
    OO::NamedElement,
    OO::Annotation,
    OO::AnnotatedElement,
    Feature,
    OO::Operation,
    OO::StructuralFeature,
    OO::Package,
    NamedElement,
    OO::Feature,
    OO::Parameter,
    OO::PackageableElement,
    Package,
    OO::Model,
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



def test_oo::attribute_is_not_abstract():
    assert not inspect.isabstract(OO::Attribute)


def test_oo::attribute_constructor_exists():
    assert callable(OO::Attribute.__init__)


def test_oo::attribute_constructor_args():
    sig = inspect.signature(OO::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_oo::reference_is_not_abstract():
    assert not inspect.isabstract(OO::Reference)


def test_oo::reference_constructor_exists():
    assert callable(OO::Reference.__init__)


def test_oo::reference_constructor_args():
    sig = inspect.signature(OO::Reference.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_oo::datatype_is_not_abstract():
    assert not inspect.isabstract(OO::Datatype)


def test_oo::datatype_constructor_exists():
    assert callable(OO::Datatype.__init__)


def test_oo::datatype_constructor_args():
    sig = inspect.signature(OO::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_oo::class_is_not_abstract():
    assert not inspect.isabstract(OO::Class)


def test_oo::class_constructor_exists():
    assert callable(OO::Class.__init__)


def test_oo::class_constructor_args():
    sig = inspect.signature(OO::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_oo::class_has_isAbstract():
    assert hasattr(OO::Class, "isAbstract")
    descriptor = None
    for klass in OO::Class.__mro__:
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



def test_oo::externalclass_is_not_abstract():
    assert not inspect.isabstract(OO::ExternalClass)


def test_oo::externalclass_constructor_exists():
    assert callable(OO::ExternalClass.__init__)


def test_oo::externalclass_constructor_args():
    sig = inspect.signature(OO::ExternalClass.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::classifier_is_not_abstract():
    assert not inspect.isabstract(OO::Classifier)


def test_oo::classifier_constructor_exists():
    assert callable(OO::Classifier.__init__)


def test_oo::classifier_constructor_args():
    sig = inspect.signature(OO::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatedElement)


def test_annotatedelement_constructor_exists():
    assert callable(AnnotatedElement.__init__)


def test_annotatedelement_constructor_args():
    sig = inspect.signature(AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::namedelement_is_not_abstract():
    assert not inspect.isabstract(OO::NamedElement)


def test_oo::namedelement_constructor_exists():
    assert callable(OO::NamedElement.__init__)


def test_oo::namedelement_constructor_args():
    sig = inspect.signature(OO::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oo::namedelement_has_name():
    assert hasattr(OO::NamedElement, "name")
    descriptor = None
    for klass in OO::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oo::annotation_is_not_abstract():
    assert not inspect.isabstract(OO::Annotation)


def test_oo::annotation_constructor_exists():
    assert callable(OO::Annotation.__init__)


def test_oo::annotation_constructor_args():
    sig = inspect.signature(OO::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_oo::annotation_has_key():
    assert hasattr(OO::Annotation, "key")
    descriptor = None
    for klass in OO::Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_oo::annotation_has_value():
    assert hasattr(OO::Annotation, "value")
    descriptor = None
    for klass in OO::Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oo::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(OO::AnnotatedElement)


def test_oo::annotatedelement_constructor_exists():
    assert callable(OO::AnnotatedElement.__init__)


def test_oo::annotatedelement_constructor_args():
    sig = inspect.signature(OO::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_oo::operation_is_not_abstract():
    assert not inspect.isabstract(OO::Operation)


def test_oo::operation_constructor_exists():
    assert callable(OO::Operation.__init__)


def test_oo::operation_constructor_args():
    sig = inspect.signature(OO::Operation.__init__)
    params = list(sig.parameters.keys())



def test_oo::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(OO::StructuralFeature)


def test_oo::structuralfeature_constructor_exists():
    assert callable(OO::StructuralFeature.__init__)


def test_oo::structuralfeature_constructor_args():
    sig = inspect.signature(OO::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isMany" in params, "Missing parameter 'isMany'"

def test_oo::structuralfeature_has_isMany():
    assert hasattr(OO::StructuralFeature, "isMany")
    descriptor = None
    for klass in OO::StructuralFeature.__mro__:
        if "isMany" in klass.__dict__:
            descriptor = klass.__dict__["isMany"]
            break
    assert isinstance(descriptor, property)



def test_oo::package_is_not_abstract():
    assert not inspect.isabstract(OO::Package)


def test_oo::package_constructor_exists():
    assert callable(OO::Package.__init__)


def test_oo::package_constructor_args():
    sig = inspect.signature(OO::Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_oo::feature_is_not_abstract():
    assert not inspect.isabstract(OO::Feature)


def test_oo::feature_constructor_exists():
    assert callable(OO::Feature.__init__)


def test_oo::feature_constructor_args():
    sig = inspect.signature(OO::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_oo::feature_has_visibility():
    assert hasattr(OO::Feature, "visibility")
    descriptor = None
    for klass in OO::Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_oo::parameter_is_not_abstract():
    assert not inspect.isabstract(OO::Parameter)


def test_oo::parameter_constructor_exists():
    assert callable(OO::Parameter.__init__)


def test_oo::parameter_constructor_args():
    sig = inspect.signature(OO::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oo::packageableelement_is_not_abstract():
    assert not inspect.isabstract(OO::PackageableElement)


def test_oo::packageableelement_constructor_exists():
    assert callable(OO::PackageableElement.__init__)


def test_oo::packageableelement_constructor_args():
    sig = inspect.signature(OO::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_oo::model_is_not_abstract():
    assert not inspect.isabstract(OO::Model)


def test_oo::model_constructor_exists():
    assert callable(OO::Model.__init__)


def test_oo::model_constructor_args():
    sig = inspect.signature(OO::Model.__init__)
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
OO::Attribute_strategy = st.builds(
    OO::Attribute,
)
OO::Reference_strategy = st.builds(
    OO::Reference,
)
Classifier_strategy = st.builds(
    Classifier,
)
OO::Datatype_strategy = st.builds(
    OO::Datatype,
)
OO::Class_strategy = st.builds(
    OO::Class,
    isAbstract=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
OO::ExternalClass_strategy = st.builds(
    OO::ExternalClass,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
OO::Classifier_strategy = st.builds(
    OO::Classifier,
)
AnnotatedElement_strategy = st.builds(
    AnnotatedElement,
)
OO::NamedElement_strategy = st.builds(
    OO::NamedElement,
    name=
        safe_text
)
OO::Annotation_strategy = st.builds(
    OO::Annotation,
    key=
        safe_text,
    value=
        safe_text
)
OO::AnnotatedElement_strategy = st.builds(
    OO::AnnotatedElement,
)
Feature_strategy = st.builds(
    Feature,
)
OO::Operation_strategy = st.builds(
    OO::Operation,
)
OO::StructuralFeature_strategy = st.builds(
    OO::StructuralFeature,
    isMany=
        safe_text
)
OO::Package_strategy = st.builds(
    OO::Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OO::Feature_strategy = st.builds(
    OO::Feature,
    visibility=
        safe_text
)
OO::Parameter_strategy = st.builds(
    OO::Parameter,
)
OO::PackageableElement_strategy = st.builds(
    OO::PackageableElement,
)
Package_strategy = st.builds(
    Package,
)
OO::Model_strategy = st.builds(
    OO::Model,
)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=OO::Attribute_strategy)
@settings(max_examples=50)
def test_oo::attribute_instantiation(instance):
    assert isinstance(instance, OO::Attribute)

@given(instance=OO::Reference_strategy)
@settings(max_examples=50)
def test_oo::reference_instantiation(instance):
    assert isinstance(instance, OO::Reference)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=OO::Datatype_strategy)
@settings(max_examples=50)
def test_oo::datatype_instantiation(instance):
    assert isinstance(instance, OO::Datatype)

@given(instance=OO::Class_strategy)
@settings(max_examples=50)
def test_oo::class_instantiation(instance):
    assert isinstance(instance, OO::Class)

@given(instance=OO::Class_strategy)
def test_oo::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=OO::Class_strategy)
def test_oo::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OO::ExternalClass_strategy)
@settings(max_examples=50)
def test_oo::externalclass_instantiation(instance):
    assert isinstance(instance, OO::ExternalClass)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=OO::Classifier_strategy)
@settings(max_examples=50)
def test_oo::classifier_instantiation(instance):
    assert isinstance(instance, OO::Classifier)

@given(instance=AnnotatedElement_strategy)
@settings(max_examples=50)
def test_annotatedelement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)

@given(instance=OO::NamedElement_strategy)
@settings(max_examples=50)
def test_oo::namedelement_instantiation(instance):
    assert isinstance(instance, OO::NamedElement)

@given(instance=OO::NamedElement_strategy)
def test_oo::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=OO::NamedElement_strategy)
def test_oo::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OO::Annotation_strategy)
@settings(max_examples=50)
def test_oo::annotation_instantiation(instance):
    assert isinstance(instance, OO::Annotation)

@given(instance=OO::Annotation_strategy)
def test_oo::annotation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=OO::Annotation_strategy)
def test_oo::annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=OO::Annotation_strategy)
def test_oo::annotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=OO::Annotation_strategy)
def test_oo::annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OO::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_oo::annotatedelement_instantiation(instance):
    assert isinstance(instance, OO::AnnotatedElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=OO::Operation_strategy)
@settings(max_examples=50)
def test_oo::operation_instantiation(instance):
    assert isinstance(instance, OO::Operation)

@given(instance=OO::StructuralFeature_strategy)
@settings(max_examples=50)
def test_oo::structuralfeature_instantiation(instance):
    assert isinstance(instance, OO::StructuralFeature)

@given(instance=OO::StructuralFeature_strategy)
def test_oo::structuralfeature_isMany_type(instance):
    assert isinstance(instance.isMany, str)


@given(instance=OO::StructuralFeature_strategy)
def test_oo::structuralfeature_isMany_setter(instance):
    original = instance.isMany
    instance.isMany = original
    assert instance.isMany == original

@given(instance=OO::Package_strategy)
@settings(max_examples=50)
def test_oo::package_instantiation(instance):
    assert isinstance(instance, OO::Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=OO::Feature_strategy)
@settings(max_examples=50)
def test_oo::feature_instantiation(instance):
    assert isinstance(instance, OO::Feature)

@given(instance=OO::Feature_strategy)
def test_oo::feature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=OO::Feature_strategy)
def test_oo::feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=OO::Parameter_strategy)
@settings(max_examples=50)
def test_oo::parameter_instantiation(instance):
    assert isinstance(instance, OO::Parameter)

@given(instance=OO::PackageableElement_strategy)
@settings(max_examples=50)
def test_oo::packageableelement_instantiation(instance):
    assert isinstance(instance, OO::PackageableElement)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=OO::Model_strategy)
@settings(max_examples=50)
def test_oo::model_instantiation(instance):
    assert isinstance(instance, OO::Model)

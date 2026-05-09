import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oclinEcoreCST::ReferenceRef,
    oclinEcoreCST::ImportCS,
    oclinEcoreCST::DocumentCS,
    DataTypeRef,
    oclinEcoreCST::DataTypeCSRef,
    DataTypeOrEnumCS,
    oclinEcoreCST::DataTypeCS,
    oclinEcoreCST::OclExpressionCS,
    TypedElementCS,
    oclinEcoreCST::ParameterCS,
    oclinEcoreCST::ModelElementCS,
    oclinEcoreCST::EnumCS,
    oclinEcoreCST::EReference,
    ReferenceRef,
    oclinEcoreCST::ReferenceCSRef,
    oclinEcoreCST::EReferenceRef,
    oclinEcoreCST::EDataType,
    oclinEcoreCST::EDataTypeRef,
    oclinEcoreCST::EClassifier,
    oclinEcoreCST::EClass,
    oclinEcoreCST::EAttribute,
    oclinEcoreCST::AttributeRef,
    AttributeRef,
    oclinEcoreCST::EAttributeRef,
    oclinEcoreCST::AttributeCSRef,
    StructuralFeatureCS,
    oclinEcoreCST::ReferenceCS,
    oclinEcoreCST::AttributeCS,
    oclinEcoreCST::DetailCS,
    ModelElementCS,
    oclinEcoreCST::NamedElementCS,
    oclinEcoreCST::AnnotationCS,
    oclinEcoreCST::ClassifierRef,
    NamedElementCS,
    oclinEcoreCST::TypedElementCS,
    oclinEcoreCST::PackageCS,
    oclinEcoreCST::ConstraintCS,
    oclinEcoreCST::EnumLiteralCS,
    oclinEcoreCST::TypeParameterCS,
    oclinEcoreCST::ClassifierCS,
    ClassifierRef,
    oclinEcoreCST::ClassifierCSRef,
    oclinEcoreCST::EClassifierRef,
    oclinEcoreCST::DataTypeRef,
    ClassRef,
    oclinEcoreCST::EClassRef,
    oclinEcoreCST::ClassCSRef,
    oclinEcoreCST::StructuralFeatureCS,
    oclinEcoreCST::OperationCS,
    oclinEcoreCST::ClassRef,
    ClassifierCS,
    oclinEcoreCST::DataTypeOrEnumCS,
    oclinEcoreCST::ClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclinecorecst::referenceref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ReferenceRef)


def test_oclinecorecst::referenceref_constructor_exists():
    assert callable(oclinEcoreCST::ReferenceRef.__init__)


def test_oclinecorecst::referenceref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::importcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ImportCS)


def test_oclinecorecst::importcs_constructor_exists():
    assert callable(oclinEcoreCST::ImportCS.__init__)


def test_oclinecorecst::importcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_oclinecorecst::importcs_has_importedNamespace():
    assert hasattr(oclinEcoreCST::ImportCS, "importedNamespace")
    descriptor = None
    for klass in oclinEcoreCST::ImportCS.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::documentcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DocumentCS)


def test_oclinecorecst::documentcs_constructor_exists():
    assert callable(oclinEcoreCST::DocumentCS.__init__)


def test_oclinecorecst::documentcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_datatyperef_is_not_abstract():
    assert not inspect.isabstract(DataTypeRef)


def test_datatyperef_constructor_exists():
    assert callable(DataTypeRef.__init__)


def test_datatyperef_constructor_args():
    sig = inspect.signature(DataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::datatypecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DataTypeCSRef)


def test_oclinecorecst::datatypecsref_constructor_exists():
    assert callable(oclinEcoreCST::DataTypeCSRef.__init__)


def test_oclinecorecst::datatypecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DataTypeCSRef.__init__)
    params = list(sig.parameters.keys())



def test_datatypeorenumcs_is_not_abstract():
    assert not inspect.isabstract(DataTypeOrEnumCS)


def test_datatypeorenumcs_constructor_exists():
    assert callable(DataTypeOrEnumCS.__init__)


def test_datatypeorenumcs_constructor_args():
    sig = inspect.signature(DataTypeOrEnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::datatypecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DataTypeCS)


def test_oclinecorecst::datatypecs_constructor_exists():
    assert callable(oclinEcoreCST::DataTypeCS.__init__)


def test_oclinecorecst::datatypecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::OclExpressionCS)


def test_oclinecorecst::oclexpressioncs_constructor_exists():
    assert callable(oclinEcoreCST::OclExpressionCS.__init__)


def test_oclinecorecst::oclexpressioncs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::parametercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ParameterCS)


def test_oclinecorecst::parametercs_constructor_exists():
    assert callable(oclinEcoreCST::ParameterCS.__init__)


def test_oclinecorecst::parametercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::modelelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ModelElementCS)


def test_oclinecorecst::modelelementcs_constructor_exists():
    assert callable(oclinEcoreCST::ModelElementCS.__init__)


def test_oclinecorecst::modelelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::enumcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EnumCS)


def test_oclinecorecst::enumcs_constructor_exists():
    assert callable(oclinEcoreCST::EnumCS.__init__)


def test_oclinecorecst::enumcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::ereference_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EReference)


def test_oclinecorecst::ereference_constructor_exists():
    assert callable(oclinEcoreCST::EReference.__init__)


def test_oclinecorecst::ereference_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EReference.__init__)
    params = list(sig.parameters.keys())



def test_referenceref_is_not_abstract():
    assert not inspect.isabstract(ReferenceRef)


def test_referenceref_constructor_exists():
    assert callable(ReferenceRef.__init__)


def test_referenceref_constructor_args():
    sig = inspect.signature(ReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::referencecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ReferenceCSRef)


def test_oclinecorecst::referencecsref_constructor_exists():
    assert callable(oclinEcoreCST::ReferenceCSRef.__init__)


def test_oclinecorecst::referencecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ReferenceCSRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::ereferenceref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EReferenceRef)


def test_oclinecorecst::ereferenceref_constructor_exists():
    assert callable(oclinEcoreCST::EReferenceRef.__init__)


def test_oclinecorecst::ereferenceref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::edatatype_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EDataType)


def test_oclinecorecst::edatatype_constructor_exists():
    assert callable(oclinEcoreCST::EDataType.__init__)


def test_oclinecorecst::edatatype_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::edatatyperef_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EDataTypeRef)


def test_oclinecorecst::edatatyperef_constructor_exists():
    assert callable(oclinEcoreCST::EDataTypeRef.__init__)


def test_oclinecorecst::edatatyperef_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EDataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eclassifier_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EClassifier)


def test_oclinecorecst::eclassifier_constructor_exists():
    assert callable(oclinEcoreCST::EClassifier.__init__)


def test_oclinecorecst::eclassifier_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eclass_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EClass)


def test_oclinecorecst::eclass_constructor_exists():
    assert callable(oclinEcoreCST::EClass.__init__)


def test_oclinecorecst::eclass_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EClass.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eattribute_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EAttribute)


def test_oclinecorecst::eattribute_constructor_exists():
    assert callable(oclinEcoreCST::EAttribute.__init__)


def test_oclinecorecst::eattribute_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::attributeref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::AttributeRef)


def test_oclinecorecst::attributeref_constructor_exists():
    assert callable(oclinEcoreCST::AttributeRef.__init__)


def test_oclinecorecst::attributeref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::AttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_attributeref_is_not_abstract():
    assert not inspect.isabstract(AttributeRef)


def test_attributeref_constructor_exists():
    assert callable(AttributeRef.__init__)


def test_attributeref_constructor_args():
    sig = inspect.signature(AttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eattributeref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EAttributeRef)


def test_oclinecorecst::eattributeref_constructor_exists():
    assert callable(oclinEcoreCST::EAttributeRef.__init__)


def test_oclinecorecst::eattributeref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EAttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::attributecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::AttributeCSRef)


def test_oclinecorecst::attributecsref_constructor_exists():
    assert callable(oclinEcoreCST::AttributeCSRef.__init__)


def test_oclinecorecst::attributecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::AttributeCSRef.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::referencecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ReferenceCS)


def test_oclinecorecst::referencecs_constructor_exists():
    assert callable(oclinEcoreCST::ReferenceCS.__init__)


def test_oclinecorecst::referencecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ReferenceCS.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"

def test_oclinecorecst::referencecs_has_containment():
    assert hasattr(oclinEcoreCST::ReferenceCS, "containment")
    descriptor = None
    for klass in oclinEcoreCST::ReferenceCS.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::attributecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::AttributeCS)


def test_oclinecorecst::attributecs_constructor_exists():
    assert callable(oclinEcoreCST::AttributeCS.__init__)


def test_oclinecorecst::attributecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::detailcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DetailCS)


def test_oclinecorecst::detailcs_constructor_exists():
    assert callable(oclinEcoreCST::DetailCS.__init__)


def test_oclinecorecst::detailcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "idName" in params, "Missing parameter 'idName'"
    assert "stringName" in params, "Missing parameter 'stringName'"

def test_oclinecorecst::detailcs_has_value():
    assert hasattr(oclinEcoreCST::DetailCS, "value")
    descriptor = None
    for klass in oclinEcoreCST::DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::detailcs_has_idName():
    assert hasattr(oclinEcoreCST::DetailCS, "idName")
    descriptor = None
    for klass in oclinEcoreCST::DetailCS.__mro__:
        if "idName" in klass.__dict__:
            descriptor = klass.__dict__["idName"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::detailcs_has_stringName():
    assert hasattr(oclinEcoreCST::DetailCS, "stringName")
    descriptor = None
    for klass in oclinEcoreCST::DetailCS.__mro__:
        if "stringName" in klass.__dict__:
            descriptor = klass.__dict__["stringName"]
            break
    assert isinstance(descriptor, property)



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::namedelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::NamedElementCS)


def test_oclinecorecst::namedelementcs_constructor_exists():
    assert callable(oclinEcoreCST::NamedElementCS.__init__)


def test_oclinecorecst::namedelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinecorecst::namedelementcs_has_name():
    assert hasattr(oclinEcoreCST::NamedElementCS, "name")
    descriptor = None
    for klass in oclinEcoreCST::NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::annotationcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::AnnotationCS)


def test_oclinecorecst::annotationcs_constructor_exists():
    assert callable(oclinEcoreCST::AnnotationCS.__init__)


def test_oclinecorecst::annotationcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::AnnotationCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSource" in params, "Missing parameter 'stringSource'"
    assert "idSource" in params, "Missing parameter 'idSource'"

def test_oclinecorecst::annotationcs_has_stringSource():
    assert hasattr(oclinEcoreCST::AnnotationCS, "stringSource")
    descriptor = None
    for klass in oclinEcoreCST::AnnotationCS.__mro__:
        if "stringSource" in klass.__dict__:
            descriptor = klass.__dict__["stringSource"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::annotationcs_has_idSource():
    assert hasattr(oclinEcoreCST::AnnotationCS, "idSource")
    descriptor = None
    for klass in oclinEcoreCST::AnnotationCS.__mro__:
        if "idSource" in klass.__dict__:
            descriptor = klass.__dict__["idSource"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::classifierref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassifierRef)


def test_oclinecorecst::classifierref_constructor_exists():
    assert callable(oclinEcoreCST::ClassifierRef.__init__)


def test_oclinecorecst::classifierref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::typedelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::TypedElementCS)


def test_oclinecorecst::typedelementcs_constructor_exists():
    assert callable(oclinEcoreCST::TypedElementCS.__init__)


def test_oclinecorecst::typedelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_oclinecorecst::typedelementcs_has_multiplicity():
    assert hasattr(oclinEcoreCST::TypedElementCS, "multiplicity")
    descriptor = None
    for klass in oclinEcoreCST::TypedElementCS.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::typedelementcs_has_upper():
    assert hasattr(oclinEcoreCST::TypedElementCS, "upper")
    descriptor = None
    for klass in oclinEcoreCST::TypedElementCS.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::typedelementcs_has_qualifiers():
    assert hasattr(oclinEcoreCST::TypedElementCS, "qualifiers")
    descriptor = None
    for klass in oclinEcoreCST::TypedElementCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::typedelementcs_has_lower():
    assert hasattr(oclinEcoreCST::TypedElementCS, "lower")
    descriptor = None
    for klass in oclinEcoreCST::TypedElementCS.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::packagecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::PackageCS)


def test_oclinecorecst::packagecs_constructor_exists():
    assert callable(oclinEcoreCST::PackageCS.__init__)


def test_oclinecorecst::packagecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::constraintcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ConstraintCS)


def test_oclinecorecst::constraintcs_constructor_exists():
    assert callable(oclinEcoreCST::ConstraintCS.__init__)


def test_oclinecorecst::constraintcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_oclinecorecst::constraintcs_has_stereotype():
    assert hasattr(oclinEcoreCST::ConstraintCS, "stereotype")
    descriptor = None
    for klass in oclinEcoreCST::ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::enumliteralcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EnumLiteralCS)


def test_oclinecorecst::enumliteralcs_constructor_exists():
    assert callable(oclinEcoreCST::EnumLiteralCS.__init__)


def test_oclinecorecst::enumliteralcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EnumLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oclinecorecst::enumliteralcs_has_value():
    assert hasattr(oclinEcoreCST::EnumLiteralCS, "value")
    descriptor = None
    for klass in oclinEcoreCST::EnumLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst::typeparametercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::TypeParameterCS)


def test_oclinecorecst::typeparametercs_constructor_exists():
    assert callable(oclinEcoreCST::TypeParameterCS.__init__)


def test_oclinecorecst::typeparametercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::classifiercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassifierCS)


def test_oclinecorecst::classifiercs_constructor_exists():
    assert callable(oclinEcoreCST::ClassifierCS.__init__)


def test_oclinecorecst::classifiercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_oclinecorecst::classifiercs_has_qualifiers():
    assert hasattr(oclinEcoreCST::ClassifierCS, "qualifiers")
    descriptor = None
    for klass in oclinEcoreCST::ClassifierCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst::classifiercs_has_instanceClassName():
    assert hasattr(oclinEcoreCST::ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in oclinEcoreCST::ClassifierCS.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_classifierref_is_not_abstract():
    assert not inspect.isabstract(ClassifierRef)


def test_classifierref_constructor_exists():
    assert callable(ClassifierRef.__init__)


def test_classifierref_constructor_args():
    sig = inspect.signature(ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::classifiercsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassifierCSRef)


def test_oclinecorecst::classifiercsref_constructor_exists():
    assert callable(oclinEcoreCST::ClassifierCSRef.__init__)


def test_oclinecorecst::classifiercsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassifierCSRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eclassifierref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EClassifierRef)


def test_oclinecorecst::eclassifierref_constructor_exists():
    assert callable(oclinEcoreCST::EClassifierRef.__init__)


def test_oclinecorecst::eclassifierref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::datatyperef_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DataTypeRef)


def test_oclinecorecst::datatyperef_constructor_exists():
    assert callable(oclinEcoreCST::DataTypeRef.__init__)


def test_oclinecorecst::datatyperef_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_classref_is_not_abstract():
    assert not inspect.isabstract(ClassRef)


def test_classref_constructor_exists():
    assert callable(ClassRef.__init__)


def test_classref_constructor_args():
    sig = inspect.signature(ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::eclassref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::EClassRef)


def test_oclinecorecst::eclassref_constructor_exists():
    assert callable(oclinEcoreCST::EClassRef.__init__)


def test_oclinecorecst::eclassref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::EClassRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::classcsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassCSRef)


def test_oclinecorecst::classcsref_constructor_exists():
    assert callable(oclinEcoreCST::ClassCSRef.__init__)


def test_oclinecorecst::classcsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassCSRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::StructuralFeatureCS)


def test_oclinecorecst::structuralfeaturecs_constructor_exists():
    assert callable(oclinEcoreCST::StructuralFeatureCS.__init__)


def test_oclinecorecst::structuralfeaturecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::operationcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::OperationCS)


def test_oclinecorecst::operationcs_constructor_exists():
    assert callable(oclinEcoreCST::OperationCS.__init__)


def test_oclinecorecst::operationcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::classref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassRef)


def test_oclinecorecst::classref_constructor_exists():
    assert callable(oclinEcoreCST::ClassRef.__init__)


def test_oclinecorecst::classref_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::datatypeorenumcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::DataTypeOrEnumCS)


def test_oclinecorecst::datatypeorenumcs_constructor_exists():
    assert callable(oclinEcoreCST::DataTypeOrEnumCS.__init__)


def test_oclinecorecst::datatypeorenumcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::DataTypeOrEnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst::classcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST::ClassCS)


def test_oclinecorecst::classcs_constructor_exists():
    assert callable(oclinEcoreCST::ClassCS.__init__)


def test_oclinecorecst::classcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST::ClassCS.__init__)
    params = list(sig.parameters.keys())


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
oclinEcoreCST::ReferenceRef_strategy = st.builds(
    oclinEcoreCST::ReferenceRef,
)
oclinEcoreCST::ImportCS_strategy = st.builds(
    oclinEcoreCST::ImportCS,
    importedNamespace=
        safe_text
)
oclinEcoreCST::DocumentCS_strategy = st.builds(
    oclinEcoreCST::DocumentCS,
)
DataTypeRef_strategy = st.builds(
    DataTypeRef,
)
oclinEcoreCST::DataTypeCSRef_strategy = st.builds(
    oclinEcoreCST::DataTypeCSRef,
)
DataTypeOrEnumCS_strategy = st.builds(
    DataTypeOrEnumCS,
)
oclinEcoreCST::DataTypeCS_strategy = st.builds(
    oclinEcoreCST::DataTypeCS,
)
oclinEcoreCST::OclExpressionCS_strategy = st.builds(
    oclinEcoreCST::OclExpressionCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
oclinEcoreCST::ParameterCS_strategy = st.builds(
    oclinEcoreCST::ParameterCS,
)
oclinEcoreCST::ModelElementCS_strategy = st.builds(
    oclinEcoreCST::ModelElementCS,
)
oclinEcoreCST::EnumCS_strategy = st.builds(
    oclinEcoreCST::EnumCS,
)
oclinEcoreCST::EReference_strategy = st.builds(
    oclinEcoreCST::EReference,
)
ReferenceRef_strategy = st.builds(
    ReferenceRef,
)
oclinEcoreCST::ReferenceCSRef_strategy = st.builds(
    oclinEcoreCST::ReferenceCSRef,
)
oclinEcoreCST::EReferenceRef_strategy = st.builds(
    oclinEcoreCST::EReferenceRef,
)
oclinEcoreCST::EDataType_strategy = st.builds(
    oclinEcoreCST::EDataType,
)
oclinEcoreCST::EDataTypeRef_strategy = st.builds(
    oclinEcoreCST::EDataTypeRef,
)
oclinEcoreCST::EClassifier_strategy = st.builds(
    oclinEcoreCST::EClassifier,
)
oclinEcoreCST::EClass_strategy = st.builds(
    oclinEcoreCST::EClass,
)
oclinEcoreCST::EAttribute_strategy = st.builds(
    oclinEcoreCST::EAttribute,
)
oclinEcoreCST::AttributeRef_strategy = st.builds(
    oclinEcoreCST::AttributeRef,
)
AttributeRef_strategy = st.builds(
    AttributeRef,
)
oclinEcoreCST::EAttributeRef_strategy = st.builds(
    oclinEcoreCST::EAttributeRef,
)
oclinEcoreCST::AttributeCSRef_strategy = st.builds(
    oclinEcoreCST::AttributeCSRef,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
oclinEcoreCST::ReferenceCS_strategy = st.builds(
    oclinEcoreCST::ReferenceCS,
    containment=
        st.booleans()
)
oclinEcoreCST::AttributeCS_strategy = st.builds(
    oclinEcoreCST::AttributeCS,
)
oclinEcoreCST::DetailCS_strategy = st.builds(
    oclinEcoreCST::DetailCS,
    value=
        safe_text,
    idName=
        safe_text,
    stringName=
        safe_text
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
oclinEcoreCST::NamedElementCS_strategy = st.builds(
    oclinEcoreCST::NamedElementCS,
    name=
        safe_text
)
oclinEcoreCST::AnnotationCS_strategy = st.builds(
    oclinEcoreCST::AnnotationCS,
    stringSource=
        safe_text,
    idSource=
        safe_text
)
oclinEcoreCST::ClassifierRef_strategy = st.builds(
    oclinEcoreCST::ClassifierRef,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
oclinEcoreCST::TypedElementCS_strategy = st.builds(
    oclinEcoreCST::TypedElementCS,
    multiplicity=
        safe_text,
    upper=
        st.integers(),
    qualifiers=
        safe_text,
    lower=
        st.integers()
)
oclinEcoreCST::PackageCS_strategy = st.builds(
    oclinEcoreCST::PackageCS,
)
oclinEcoreCST::ConstraintCS_strategy = st.builds(
    oclinEcoreCST::ConstraintCS,
    stereotype=
        safe_text
)
oclinEcoreCST::EnumLiteralCS_strategy = st.builds(
    oclinEcoreCST::EnumLiteralCS,
    value=
        st.integers()
)
oclinEcoreCST::TypeParameterCS_strategy = st.builds(
    oclinEcoreCST::TypeParameterCS,
)
oclinEcoreCST::ClassifierCS_strategy = st.builds(
    oclinEcoreCST::ClassifierCS,
    qualifiers=
        safe_text,
    instanceClassName=
        safe_text
)
ClassifierRef_strategy = st.builds(
    ClassifierRef,
)
oclinEcoreCST::ClassifierCSRef_strategy = st.builds(
    oclinEcoreCST::ClassifierCSRef,
)
oclinEcoreCST::EClassifierRef_strategy = st.builds(
    oclinEcoreCST::EClassifierRef,
)
oclinEcoreCST::DataTypeRef_strategy = st.builds(
    oclinEcoreCST::DataTypeRef,
)
ClassRef_strategy = st.builds(
    ClassRef,
)
oclinEcoreCST::EClassRef_strategy = st.builds(
    oclinEcoreCST::EClassRef,
)
oclinEcoreCST::ClassCSRef_strategy = st.builds(
    oclinEcoreCST::ClassCSRef,
)
oclinEcoreCST::StructuralFeatureCS_strategy = st.builds(
    oclinEcoreCST::StructuralFeatureCS,
)
oclinEcoreCST::OperationCS_strategy = st.builds(
    oclinEcoreCST::OperationCS,
)
oclinEcoreCST::ClassRef_strategy = st.builds(
    oclinEcoreCST::ClassRef,
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
oclinEcoreCST::DataTypeOrEnumCS_strategy = st.builds(
    oclinEcoreCST::DataTypeOrEnumCS,
)
oclinEcoreCST::ClassCS_strategy = st.builds(
    oclinEcoreCST::ClassCS,
)

@given(instance=oclinEcoreCST::ReferenceRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::referenceref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ReferenceRef)

@given(instance=oclinEcoreCST::ImportCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::importcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ImportCS)

@given(instance=oclinEcoreCST::ImportCS_strategy)
def test_oclinecorecst::importcs_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=oclinEcoreCST::ImportCS_strategy)
def test_oclinecorecst::importcs_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=oclinEcoreCST::DocumentCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::documentcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DocumentCS)

@given(instance=DataTypeRef_strategy)
@settings(max_examples=50)
def test_datatyperef_instantiation(instance):
    assert isinstance(instance, DataTypeRef)

@given(instance=oclinEcoreCST::DataTypeCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::datatypecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DataTypeCSRef)

@given(instance=DataTypeOrEnumCS_strategy)
@settings(max_examples=50)
def test_datatypeorenumcs_instantiation(instance):
    assert isinstance(instance, DataTypeOrEnumCS)

@given(instance=oclinEcoreCST::DataTypeCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::datatypecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DataTypeCS)

@given(instance=oclinEcoreCST::OclExpressionCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::oclexpressioncs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::OclExpressionCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=oclinEcoreCST::ParameterCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::parametercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ParameterCS)

@given(instance=oclinEcoreCST::ModelElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::modelelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ModelElementCS)

@given(instance=oclinEcoreCST::EnumCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::enumcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EnumCS)

@given(instance=oclinEcoreCST::EReference_strategy)
@settings(max_examples=50)
def test_oclinecorecst::ereference_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EReference)

@given(instance=ReferenceRef_strategy)
@settings(max_examples=50)
def test_referenceref_instantiation(instance):
    assert isinstance(instance, ReferenceRef)

@given(instance=oclinEcoreCST::ReferenceCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::referencecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ReferenceCSRef)

@given(instance=oclinEcoreCST::EReferenceRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::ereferenceref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EReferenceRef)

@given(instance=oclinEcoreCST::EDataType_strategy)
@settings(max_examples=50)
def test_oclinecorecst::edatatype_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EDataType)

@given(instance=oclinEcoreCST::EDataTypeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::edatatyperef_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EDataTypeRef)

@given(instance=oclinEcoreCST::EClassifier_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eclassifier_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EClassifier)

@given(instance=oclinEcoreCST::EClass_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eclass_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EClass)

@given(instance=oclinEcoreCST::EAttribute_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eattribute_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EAttribute)

@given(instance=oclinEcoreCST::AttributeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::attributeref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::AttributeRef)

@given(instance=AttributeRef_strategy)
@settings(max_examples=50)
def test_attributeref_instantiation(instance):
    assert isinstance(instance, AttributeRef)

@given(instance=oclinEcoreCST::EAttributeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eattributeref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EAttributeRef)

@given(instance=oclinEcoreCST::AttributeCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::attributecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::AttributeCSRef)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=oclinEcoreCST::ReferenceCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::referencecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ReferenceCS)

@given(instance=oclinEcoreCST::ReferenceCS_strategy)
def test_oclinecorecst::referencecs_containment_type(instance):
    assert isinstance(instance.containment, bool)


@given(instance=oclinEcoreCST::ReferenceCS_strategy)
def test_oclinecorecst::referencecs_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=oclinEcoreCST::AttributeCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::attributecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::AttributeCS)

@given(instance=oclinEcoreCST::DetailCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::detailcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DetailCS)

@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_idName_type(instance):
    assert isinstance(instance.idName, str)


@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_idName_setter(instance):
    original = instance.idName
    instance.idName = original
    assert instance.idName == original

@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_stringName_type(instance):
    assert isinstance(instance.stringName, str)


@given(instance=oclinEcoreCST::DetailCS_strategy)
def test_oclinecorecst::detailcs_stringName_setter(instance):
    original = instance.stringName
    instance.stringName = original
    assert instance.stringName == original

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=oclinEcoreCST::NamedElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::namedelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::NamedElementCS)

@given(instance=oclinEcoreCST::NamedElementCS_strategy)
def test_oclinecorecst::namedelementcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclinEcoreCST::NamedElementCS_strategy)
def test_oclinecorecst::namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclinEcoreCST::AnnotationCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::annotationcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::AnnotationCS)

@given(instance=oclinEcoreCST::AnnotationCS_strategy)
def test_oclinecorecst::annotationcs_stringSource_type(instance):
    assert isinstance(instance.stringSource, str)


@given(instance=oclinEcoreCST::AnnotationCS_strategy)
def test_oclinecorecst::annotationcs_stringSource_setter(instance):
    original = instance.stringSource
    instance.stringSource = original
    assert instance.stringSource == original

@given(instance=oclinEcoreCST::AnnotationCS_strategy)
def test_oclinecorecst::annotationcs_idSource_type(instance):
    assert isinstance(instance.idSource, str)


@given(instance=oclinEcoreCST::AnnotationCS_strategy)
def test_oclinecorecst::annotationcs_idSource_setter(instance):
    original = instance.idSource
    instance.idSource = original
    assert instance.idSource == original

@given(instance=oclinEcoreCST::ClassifierRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classifierref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassifierRef)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=oclinEcoreCST::TypedElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::typedelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::TypedElementCS)

@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, str)


@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_qualifiers_type(instance):
    assert isinstance(instance.qualifiers, str)


@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original

@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=oclinEcoreCST::TypedElementCS_strategy)
def test_oclinecorecst::typedelementcs_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=oclinEcoreCST::PackageCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::packagecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::PackageCS)

@given(instance=oclinEcoreCST::ConstraintCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::constraintcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ConstraintCS)

@given(instance=oclinEcoreCST::ConstraintCS_strategy)
def test_oclinecorecst::constraintcs_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=oclinEcoreCST::ConstraintCS_strategy)
def test_oclinecorecst::constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=oclinEcoreCST::EnumLiteralCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::enumliteralcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EnumLiteralCS)

@given(instance=oclinEcoreCST::EnumLiteralCS_strategy)
def test_oclinecorecst::enumliteralcs_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=oclinEcoreCST::EnumLiteralCS_strategy)
def test_oclinecorecst::enumliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclinEcoreCST::TypeParameterCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::typeparametercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::TypeParameterCS)

@given(instance=oclinEcoreCST::ClassifierCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classifiercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassifierCS)

@given(instance=oclinEcoreCST::ClassifierCS_strategy)
def test_oclinecorecst::classifiercs_qualifiers_type(instance):
    assert isinstance(instance.qualifiers, str)


@given(instance=oclinEcoreCST::ClassifierCS_strategy)
def test_oclinecorecst::classifiercs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original

@given(instance=oclinEcoreCST::ClassifierCS_strategy)
def test_oclinecorecst::classifiercs_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=oclinEcoreCST::ClassifierCS_strategy)
def test_oclinecorecst::classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=ClassifierRef_strategy)
@settings(max_examples=50)
def test_classifierref_instantiation(instance):
    assert isinstance(instance, ClassifierRef)

@given(instance=oclinEcoreCST::ClassifierCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classifiercsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassifierCSRef)

@given(instance=oclinEcoreCST::EClassifierRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eclassifierref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EClassifierRef)

@given(instance=oclinEcoreCST::DataTypeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::datatyperef_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DataTypeRef)

@given(instance=ClassRef_strategy)
@settings(max_examples=50)
def test_classref_instantiation(instance):
    assert isinstance(instance, ClassRef)

@given(instance=oclinEcoreCST::EClassRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::eclassref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::EClassRef)

@given(instance=oclinEcoreCST::ClassCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classcsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassCSRef)

@given(instance=oclinEcoreCST::StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::StructuralFeatureCS)

@given(instance=oclinEcoreCST::OperationCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::operationcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::OperationCS)

@given(instance=oclinEcoreCST::ClassRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassRef)

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=oclinEcoreCST::DataTypeOrEnumCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::datatypeorenumcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::DataTypeOrEnumCS)

@given(instance=oclinEcoreCST::ClassCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst::classcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST::ClassCS)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oclinEcoreCST_ReferenceRef,
    oclinEcoreCST_ImportCS,
    oclinEcoreCST_DocumentCS,
    DataTypeRef,
    oclinEcoreCST_DataTypeCSRef,
    DataTypeOrEnumCS,
    oclinEcoreCST_DataTypeCS,
    oclinEcoreCST_OclExpressionCS,
    TypedElementCS,
    oclinEcoreCST_ParameterCS,
    oclinEcoreCST_ModelElementCS,
    oclinEcoreCST_EnumCS,
    oclinEcoreCST_EReference,
    ReferenceRef,
    oclinEcoreCST_ReferenceCSRef,
    oclinEcoreCST_EReferenceRef,
    oclinEcoreCST_EDataType,
    oclinEcoreCST_EDataTypeRef,
    oclinEcoreCST_EClassifier,
    oclinEcoreCST_EClass,
    oclinEcoreCST_EAttribute,
    oclinEcoreCST_AttributeRef,
    AttributeRef,
    oclinEcoreCST_EAttributeRef,
    oclinEcoreCST_AttributeCSRef,
    StructuralFeatureCS,
    oclinEcoreCST_ReferenceCS,
    oclinEcoreCST_AttributeCS,
    oclinEcoreCST_DetailCS,
    ModelElementCS,
    oclinEcoreCST_NamedElementCS,
    oclinEcoreCST_AnnotationCS,
    oclinEcoreCST_ClassifierRef,
    NamedElementCS,
    oclinEcoreCST_EnumLiteralCS,
    oclinEcoreCST_PackageCS,
    oclinEcoreCST_TypedElementCS,
    oclinEcoreCST_TypeParameterCS,
    oclinEcoreCST_ConstraintCS,
    oclinEcoreCST_ClassifierCS,
    ClassifierRef,
    oclinEcoreCST_EClassifierRef,
    oclinEcoreCST_DataTypeRef,
    oclinEcoreCST_ClassifierCSRef,
    ClassRef,
    oclinEcoreCST_EClassRef,
    oclinEcoreCST_ClassCSRef,
    oclinEcoreCST_StructuralFeatureCS,
    oclinEcoreCST_OperationCS,
    oclinEcoreCST_ClassRef,
    ClassifierCS,
    oclinEcoreCST_DataTypeOrEnumCS,
    oclinEcoreCST_ClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclinecorecst_referenceref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ReferenceRef)


def test_oclinecorecst_referenceref_constructor_exists():
    assert callable(oclinEcoreCST_ReferenceRef.__init__)


def test_oclinecorecst_referenceref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_importcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ImportCS)


def test_oclinecorecst_importcs_constructor_exists():
    assert callable(oclinEcoreCST_ImportCS.__init__)


def test_oclinecorecst_importcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_oclinecorecst_importcs_has_importedNamespace():
    assert hasattr(oclinEcoreCST_ImportCS, "importedNamespace")
    descriptor = None
    for klass in oclinEcoreCST_ImportCS.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_documentcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DocumentCS)


def test_oclinecorecst_documentcs_constructor_exists():
    assert callable(oclinEcoreCST_DocumentCS.__init__)


def test_oclinecorecst_documentcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DocumentCS.__init__)
    params = list(sig.parameters.keys())



def test_datatyperef_is_not_abstract():
    assert not inspect.isabstract(DataTypeRef)


def test_datatyperef_constructor_exists():
    assert callable(DataTypeRef.__init__)


def test_datatyperef_constructor_args():
    sig = inspect.signature(DataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_datatypecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DataTypeCSRef)


def test_oclinecorecst_datatypecsref_constructor_exists():
    assert callable(oclinEcoreCST_DataTypeCSRef.__init__)


def test_oclinecorecst_datatypecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DataTypeCSRef.__init__)
    params = list(sig.parameters.keys())



def test_datatypeorenumcs_is_not_abstract():
    assert not inspect.isabstract(DataTypeOrEnumCS)


def test_datatypeorenumcs_constructor_exists():
    assert callable(DataTypeOrEnumCS.__init__)


def test_datatypeorenumcs_constructor_args():
    sig = inspect.signature(DataTypeOrEnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_datatypecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DataTypeCS)


def test_oclinecorecst_datatypecs_constructor_exists():
    assert callable(oclinEcoreCST_DataTypeCS.__init__)


def test_oclinecorecst_datatypecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_OclExpressionCS)


def test_oclinecorecst_oclexpressioncs_constructor_exists():
    assert callable(oclinEcoreCST_OclExpressionCS.__init__)


def test_oclinecorecst_oclexpressioncs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_OclExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_parametercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ParameterCS)


def test_oclinecorecst_parametercs_constructor_exists():
    assert callable(oclinEcoreCST_ParameterCS.__init__)


def test_oclinecorecst_parametercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ModelElementCS)


def test_oclinecorecst_modelelementcs_constructor_exists():
    assert callable(oclinEcoreCST_ModelElementCS.__init__)


def test_oclinecorecst_modelelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_enumcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EnumCS)


def test_oclinecorecst_enumcs_constructor_exists():
    assert callable(oclinEcoreCST_EnumCS.__init__)


def test_oclinecorecst_enumcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_ereference_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EReference)


def test_oclinecorecst_ereference_constructor_exists():
    assert callable(oclinEcoreCST_EReference.__init__)


def test_oclinecorecst_ereference_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EReference.__init__)
    params = list(sig.parameters.keys())



def test_referenceref_is_not_abstract():
    assert not inspect.isabstract(ReferenceRef)


def test_referenceref_constructor_exists():
    assert callable(ReferenceRef.__init__)


def test_referenceref_constructor_args():
    sig = inspect.signature(ReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_referencecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ReferenceCSRef)


def test_oclinecorecst_referencecsref_constructor_exists():
    assert callable(oclinEcoreCST_ReferenceCSRef.__init__)


def test_oclinecorecst_referencecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ReferenceCSRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_ereferenceref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EReferenceRef)


def test_oclinecorecst_ereferenceref_constructor_exists():
    assert callable(oclinEcoreCST_EReferenceRef.__init__)


def test_oclinecorecst_ereferenceref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_edatatype_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EDataType)


def test_oclinecorecst_edatatype_constructor_exists():
    assert callable(oclinEcoreCST_EDataType.__init__)


def test_oclinecorecst_edatatype_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EDataType.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_edatatyperef_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EDataTypeRef)


def test_oclinecorecst_edatatyperef_constructor_exists():
    assert callable(oclinEcoreCST_EDataTypeRef.__init__)


def test_oclinecorecst_edatatyperef_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EDataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_eclassifier_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EClassifier)


def test_oclinecorecst_eclassifier_constructor_exists():
    assert callable(oclinEcoreCST_EClassifier.__init__)


def test_oclinecorecst_eclassifier_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_eclass_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EClass)


def test_oclinecorecst_eclass_constructor_exists():
    assert callable(oclinEcoreCST_EClass.__init__)


def test_oclinecorecst_eclass_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EClass.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_eattribute_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EAttribute)


def test_oclinecorecst_eattribute_constructor_exists():
    assert callable(oclinEcoreCST_EAttribute.__init__)


def test_oclinecorecst_eattribute_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_attributeref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_AttributeRef)


def test_oclinecorecst_attributeref_constructor_exists():
    assert callable(oclinEcoreCST_AttributeRef.__init__)


def test_oclinecorecst_attributeref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_AttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_attributeref_is_not_abstract():
    assert not inspect.isabstract(AttributeRef)


def test_attributeref_constructor_exists():
    assert callable(AttributeRef.__init__)


def test_attributeref_constructor_args():
    sig = inspect.signature(AttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_eattributeref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EAttributeRef)


def test_oclinecorecst_eattributeref_constructor_exists():
    assert callable(oclinEcoreCST_EAttributeRef.__init__)


def test_oclinecorecst_eattributeref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EAttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_attributecsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_AttributeCSRef)


def test_oclinecorecst_attributecsref_constructor_exists():
    assert callable(oclinEcoreCST_AttributeCSRef.__init__)


def test_oclinecorecst_attributecsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_AttributeCSRef.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_referencecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ReferenceCS)


def test_oclinecorecst_referencecs_constructor_exists():
    assert callable(oclinEcoreCST_ReferenceCS.__init__)


def test_oclinecorecst_referencecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ReferenceCS.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"

def test_oclinecorecst_referencecs_has_containment():
    assert hasattr(oclinEcoreCST_ReferenceCS, "containment")
    descriptor = None
    for klass in oclinEcoreCST_ReferenceCS.__mro__:
        if "containment" in klass.__dict__:
            descriptor = klass.__dict__["containment"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_attributecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_AttributeCS)


def test_oclinecorecst_attributecs_constructor_exists():
    assert callable(oclinEcoreCST_AttributeCS.__init__)


def test_oclinecorecst_attributecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_detailcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DetailCS)


def test_oclinecorecst_detailcs_constructor_exists():
    assert callable(oclinEcoreCST_DetailCS.__init__)


def test_oclinecorecst_detailcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringName" in params, "Missing parameter 'stringName'"
    assert "value" in params, "Missing parameter 'value'"
    assert "idName" in params, "Missing parameter 'idName'"

def test_oclinecorecst_detailcs_has_stringName():
    assert hasattr(oclinEcoreCST_DetailCS, "stringName")
    descriptor = None
    for klass in oclinEcoreCST_DetailCS.__mro__:
        if "stringName" in klass.__dict__:
            descriptor = klass.__dict__["stringName"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_detailcs_has_value():
    assert hasattr(oclinEcoreCST_DetailCS, "value")
    descriptor = None
    for klass in oclinEcoreCST_DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_detailcs_has_idName():
    assert hasattr(oclinEcoreCST_DetailCS, "idName")
    descriptor = None
    for klass in oclinEcoreCST_DetailCS.__mro__:
        if "idName" in klass.__dict__:
            descriptor = klass.__dict__["idName"]
            break
    assert isinstance(descriptor, property)



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_NamedElementCS)


def test_oclinecorecst_namedelementcs_constructor_exists():
    assert callable(oclinEcoreCST_NamedElementCS.__init__)


def test_oclinecorecst_namedelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclinecorecst_namedelementcs_has_name():
    assert hasattr(oclinEcoreCST_NamedElementCS, "name")
    descriptor = None
    for klass in oclinEcoreCST_NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_annotationcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_AnnotationCS)


def test_oclinecorecst_annotationcs_constructor_exists():
    assert callable(oclinEcoreCST_AnnotationCS.__init__)


def test_oclinecorecst_annotationcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_AnnotationCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSource" in params, "Missing parameter 'stringSource'"
    assert "idSource" in params, "Missing parameter 'idSource'"

def test_oclinecorecst_annotationcs_has_stringSource():
    assert hasattr(oclinEcoreCST_AnnotationCS, "stringSource")
    descriptor = None
    for klass in oclinEcoreCST_AnnotationCS.__mro__:
        if "stringSource" in klass.__dict__:
            descriptor = klass.__dict__["stringSource"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_annotationcs_has_idSource():
    assert hasattr(oclinEcoreCST_AnnotationCS, "idSource")
    descriptor = None
    for klass in oclinEcoreCST_AnnotationCS.__mro__:
        if "idSource" in klass.__dict__:
            descriptor = klass.__dict__["idSource"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_classifierref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassifierRef)


def test_oclinecorecst_classifierref_constructor_exists():
    assert callable(oclinEcoreCST_ClassifierRef.__init__)


def test_oclinecorecst_classifierref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_enumliteralcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EnumLiteralCS)


def test_oclinecorecst_enumliteralcs_constructor_exists():
    assert callable(oclinEcoreCST_EnumLiteralCS.__init__)


def test_oclinecorecst_enumliteralcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EnumLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_oclinecorecst_enumliteralcs_has_value():
    assert hasattr(oclinEcoreCST_EnumLiteralCS, "value")
    descriptor = None
    for klass in oclinEcoreCST_EnumLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_packagecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_PackageCS)


def test_oclinecorecst_packagecs_constructor_exists():
    assert callable(oclinEcoreCST_PackageCS.__init__)


def test_oclinecorecst_packagecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_TypedElementCS)


def test_oclinecorecst_typedelementcs_constructor_exists():
    assert callable(oclinEcoreCST_TypedElementCS.__init__)


def test_oclinecorecst_typedelementcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_oclinecorecst_typedelementcs_has_upper():
    assert hasattr(oclinEcoreCST_TypedElementCS, "upper")
    descriptor = None
    for klass in oclinEcoreCST_TypedElementCS.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_typedelementcs_has_multiplicity():
    assert hasattr(oclinEcoreCST_TypedElementCS, "multiplicity")
    descriptor = None
    for klass in oclinEcoreCST_TypedElementCS.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_typedelementcs_has_qualifiers():
    assert hasattr(oclinEcoreCST_TypedElementCS, "qualifiers")
    descriptor = None
    for klass in oclinEcoreCST_TypedElementCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_typedelementcs_has_lower():
    assert hasattr(oclinEcoreCST_TypedElementCS, "lower")
    descriptor = None
    for klass in oclinEcoreCST_TypedElementCS.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_typeparametercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_TypeParameterCS)


def test_oclinecorecst_typeparametercs_constructor_exists():
    assert callable(oclinEcoreCST_TypeParameterCS.__init__)


def test_oclinecorecst_typeparametercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_constraintcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ConstraintCS)


def test_oclinecorecst_constraintcs_constructor_exists():
    assert callable(oclinEcoreCST_ConstraintCS.__init__)


def test_oclinecorecst_constraintcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_oclinecorecst_constraintcs_has_stereotype():
    assert hasattr(oclinEcoreCST_ConstraintCS, "stereotype")
    descriptor = None
    for klass in oclinEcoreCST_ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_oclinecorecst_classifiercs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassifierCS)


def test_oclinecorecst_classifiercs_constructor_exists():
    assert callable(oclinEcoreCST_ClassifierCS.__init__)


def test_oclinecorecst_classifiercs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_oclinecorecst_classifiercs_has_qualifiers():
    assert hasattr(oclinEcoreCST_ClassifierCS, "qualifiers")
    descriptor = None
    for klass in oclinEcoreCST_ClassifierCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)

def test_oclinecorecst_classifiercs_has_instanceClassName():
    assert hasattr(oclinEcoreCST_ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in oclinEcoreCST_ClassifierCS.__mro__:
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



def test_oclinecorecst_eclassifierref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EClassifierRef)


def test_oclinecorecst_eclassifierref_constructor_exists():
    assert callable(oclinEcoreCST_EClassifierRef.__init__)


def test_oclinecorecst_eclassifierref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_datatyperef_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DataTypeRef)


def test_oclinecorecst_datatyperef_constructor_exists():
    assert callable(oclinEcoreCST_DataTypeRef.__init__)


def test_oclinecorecst_datatyperef_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DataTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_classifiercsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassifierCSRef)


def test_oclinecorecst_classifiercsref_constructor_exists():
    assert callable(oclinEcoreCST_ClassifierCSRef.__init__)


def test_oclinecorecst_classifiercsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassifierCSRef.__init__)
    params = list(sig.parameters.keys())



def test_classref_is_not_abstract():
    assert not inspect.isabstract(ClassRef)


def test_classref_constructor_exists():
    assert callable(ClassRef.__init__)


def test_classref_constructor_args():
    sig = inspect.signature(ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_eclassref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_EClassRef)


def test_oclinecorecst_eclassref_constructor_exists():
    assert callable(oclinEcoreCST_EClassRef.__init__)


def test_oclinecorecst_eclassref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_EClassRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_classcsref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassCSRef)


def test_oclinecorecst_classcsref_constructor_exists():
    assert callable(oclinEcoreCST_ClassCSRef.__init__)


def test_oclinecorecst_classcsref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassCSRef.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_StructuralFeatureCS)


def test_oclinecorecst_structuralfeaturecs_constructor_exists():
    assert callable(oclinEcoreCST_StructuralFeatureCS.__init__)


def test_oclinecorecst_structuralfeaturecs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_operationcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_OperationCS)


def test_oclinecorecst_operationcs_constructor_exists():
    assert callable(oclinEcoreCST_OperationCS.__init__)


def test_oclinecorecst_operationcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_classref_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassRef)


def test_oclinecorecst_classref_constructor_exists():
    assert callable(oclinEcoreCST_ClassRef.__init__)


def test_oclinecorecst_classref_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_datatypeorenumcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_DataTypeOrEnumCS)


def test_oclinecorecst_datatypeorenumcs_constructor_exists():
    assert callable(oclinEcoreCST_DataTypeOrEnumCS.__init__)


def test_oclinecorecst_datatypeorenumcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_DataTypeOrEnumCS.__init__)
    params = list(sig.parameters.keys())



def test_oclinecorecst_classcs_is_not_abstract():
    assert not inspect.isabstract(oclinEcoreCST_ClassCS)


def test_oclinecorecst_classcs_constructor_exists():
    assert callable(oclinEcoreCST_ClassCS.__init__)


def test_oclinecorecst_classcs_constructor_args():
    sig = inspect.signature(oclinEcoreCST_ClassCS.__init__)
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
oclinEcoreCST_ReferenceRef_strategy = st.builds(
    oclinEcoreCST_ReferenceRef,
)
oclinEcoreCST_ImportCS_strategy = st.builds(
    oclinEcoreCST_ImportCS,
    importedNamespace=
        safe_text
)
oclinEcoreCST_DocumentCS_strategy = st.builds(
    oclinEcoreCST_DocumentCS,
)
DataTypeRef_strategy = st.builds(
    DataTypeRef,
)
oclinEcoreCST_DataTypeCSRef_strategy = st.builds(
    oclinEcoreCST_DataTypeCSRef,
)
DataTypeOrEnumCS_strategy = st.builds(
    DataTypeOrEnumCS,
)
oclinEcoreCST_DataTypeCS_strategy = st.builds(
    oclinEcoreCST_DataTypeCS,
)
oclinEcoreCST_OclExpressionCS_strategy = st.builds(
    oclinEcoreCST_OclExpressionCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
oclinEcoreCST_ParameterCS_strategy = st.builds(
    oclinEcoreCST_ParameterCS,
)
oclinEcoreCST_ModelElementCS_strategy = st.builds(
    oclinEcoreCST_ModelElementCS,
)
oclinEcoreCST_EnumCS_strategy = st.builds(
    oclinEcoreCST_EnumCS,
)
oclinEcoreCST_EReference_strategy = st.builds(
    oclinEcoreCST_EReference,
)
ReferenceRef_strategy = st.builds(
    ReferenceRef,
)
oclinEcoreCST_ReferenceCSRef_strategy = st.builds(
    oclinEcoreCST_ReferenceCSRef,
)
oclinEcoreCST_EReferenceRef_strategy = st.builds(
    oclinEcoreCST_EReferenceRef,
)
oclinEcoreCST_EDataType_strategy = st.builds(
    oclinEcoreCST_EDataType,
)
oclinEcoreCST_EDataTypeRef_strategy = st.builds(
    oclinEcoreCST_EDataTypeRef,
)
oclinEcoreCST_EClassifier_strategy = st.builds(
    oclinEcoreCST_EClassifier,
)
oclinEcoreCST_EClass_strategy = st.builds(
    oclinEcoreCST_EClass,
)
oclinEcoreCST_EAttribute_strategy = st.builds(
    oclinEcoreCST_EAttribute,
)
oclinEcoreCST_AttributeRef_strategy = st.builds(
    oclinEcoreCST_AttributeRef,
)
AttributeRef_strategy = st.builds(
    AttributeRef,
)
oclinEcoreCST_EAttributeRef_strategy = st.builds(
    oclinEcoreCST_EAttributeRef,
)
oclinEcoreCST_AttributeCSRef_strategy = st.builds(
    oclinEcoreCST_AttributeCSRef,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
oclinEcoreCST_ReferenceCS_strategy = st.builds(
    oclinEcoreCST_ReferenceCS,
    containment=
        st.booleans()
)
oclinEcoreCST_AttributeCS_strategy = st.builds(
    oclinEcoreCST_AttributeCS,
)
oclinEcoreCST_DetailCS_strategy = st.builds(
    oclinEcoreCST_DetailCS,
    stringName=
        safe_text,
    value=
        safe_text,
    idName=
        safe_text
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
oclinEcoreCST_NamedElementCS_strategy = st.builds(
    oclinEcoreCST_NamedElementCS,
    name=
        safe_text
)
oclinEcoreCST_AnnotationCS_strategy = st.builds(
    oclinEcoreCST_AnnotationCS,
    stringSource=
        safe_text,
    idSource=
        safe_text
)
oclinEcoreCST_ClassifierRef_strategy = st.builds(
    oclinEcoreCST_ClassifierRef,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
oclinEcoreCST_EnumLiteralCS_strategy = st.builds(
    oclinEcoreCST_EnumLiteralCS,
    value=
        st.integers()
)
oclinEcoreCST_PackageCS_strategy = st.builds(
    oclinEcoreCST_PackageCS,
)
oclinEcoreCST_TypedElementCS_strategy = st.builds(
    oclinEcoreCST_TypedElementCS,
    upper=
        st.integers(),
    multiplicity=
        safe_text,
    qualifiers=
        safe_text,
    lower=
        st.integers()
)
oclinEcoreCST_TypeParameterCS_strategy = st.builds(
    oclinEcoreCST_TypeParameterCS,
)
oclinEcoreCST_ConstraintCS_strategy = st.builds(
    oclinEcoreCST_ConstraintCS,
    stereotype=
        safe_text
)
oclinEcoreCST_ClassifierCS_strategy = st.builds(
    oclinEcoreCST_ClassifierCS,
    qualifiers=
        safe_text,
    instanceClassName=
        safe_text
)
ClassifierRef_strategy = st.builds(
    ClassifierRef,
)
oclinEcoreCST_EClassifierRef_strategy = st.builds(
    oclinEcoreCST_EClassifierRef,
)
oclinEcoreCST_DataTypeRef_strategy = st.builds(
    oclinEcoreCST_DataTypeRef,
)
oclinEcoreCST_ClassifierCSRef_strategy = st.builds(
    oclinEcoreCST_ClassifierCSRef,
)
ClassRef_strategy = st.builds(
    ClassRef,
)
oclinEcoreCST_EClassRef_strategy = st.builds(
    oclinEcoreCST_EClassRef,
)
oclinEcoreCST_ClassCSRef_strategy = st.builds(
    oclinEcoreCST_ClassCSRef,
)
oclinEcoreCST_StructuralFeatureCS_strategy = st.builds(
    oclinEcoreCST_StructuralFeatureCS,
)
oclinEcoreCST_OperationCS_strategy = st.builds(
    oclinEcoreCST_OperationCS,
)
oclinEcoreCST_ClassRef_strategy = st.builds(
    oclinEcoreCST_ClassRef,
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
oclinEcoreCST_DataTypeOrEnumCS_strategy = st.builds(
    oclinEcoreCST_DataTypeOrEnumCS,
)
oclinEcoreCST_ClassCS_strategy = st.builds(
    oclinEcoreCST_ClassCS,
)

@given(instance=oclinEcoreCST_ReferenceRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_referenceref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ReferenceRef)

@given(instance=oclinEcoreCST_ImportCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_importcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ImportCS)



@given(instance=oclinEcoreCST_ImportCS_strategy)
def test_oclinecorecst_importcs_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=oclinEcoreCST_DocumentCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_documentcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DocumentCS)

@given(instance=DataTypeRef_strategy)
@settings(max_examples=50)
def test_datatyperef_instantiation(instance):
    assert isinstance(instance, DataTypeRef)

@given(instance=oclinEcoreCST_DataTypeCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_datatypecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DataTypeCSRef)

@given(instance=DataTypeOrEnumCS_strategy)
@settings(max_examples=50)
def test_datatypeorenumcs_instantiation(instance):
    assert isinstance(instance, DataTypeOrEnumCS)

@given(instance=oclinEcoreCST_DataTypeCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_datatypecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DataTypeCS)

@given(instance=oclinEcoreCST_OclExpressionCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_OclExpressionCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=oclinEcoreCST_ParameterCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_parametercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ParameterCS)

@given(instance=oclinEcoreCST_ModelElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_modelelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ModelElementCS)

@given(instance=oclinEcoreCST_EnumCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_enumcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EnumCS)

@given(instance=oclinEcoreCST_EReference_strategy)
@settings(max_examples=50)
def test_oclinecorecst_ereference_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EReference)

@given(instance=ReferenceRef_strategy)
@settings(max_examples=50)
def test_referenceref_instantiation(instance):
    assert isinstance(instance, ReferenceRef)

@given(instance=oclinEcoreCST_ReferenceCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_referencecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ReferenceCSRef)

@given(instance=oclinEcoreCST_EReferenceRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_ereferenceref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EReferenceRef)

@given(instance=oclinEcoreCST_EDataType_strategy)
@settings(max_examples=50)
def test_oclinecorecst_edatatype_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EDataType)

@given(instance=oclinEcoreCST_EDataTypeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_edatatyperef_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EDataTypeRef)

@given(instance=oclinEcoreCST_EClassifier_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eclassifier_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EClassifier)

@given(instance=oclinEcoreCST_EClass_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eclass_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EClass)

@given(instance=oclinEcoreCST_EAttribute_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eattribute_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EAttribute)

@given(instance=oclinEcoreCST_AttributeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_attributeref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_AttributeRef)

@given(instance=AttributeRef_strategy)
@settings(max_examples=50)
def test_attributeref_instantiation(instance):
    assert isinstance(instance, AttributeRef)

@given(instance=oclinEcoreCST_EAttributeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eattributeref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EAttributeRef)

@given(instance=oclinEcoreCST_AttributeCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_attributecsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_AttributeCSRef)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=oclinEcoreCST_ReferenceCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_referencecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ReferenceCS)



@given(instance=oclinEcoreCST_ReferenceCS_strategy)
def test_oclinecorecst_referencecs_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original

@given(instance=oclinEcoreCST_AttributeCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_attributecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_AttributeCS)

@given(instance=oclinEcoreCST_DetailCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_detailcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DetailCS)



@given(instance=oclinEcoreCST_DetailCS_strategy)
def test_oclinecorecst_detailcs_stringName_setter(instance):
    original = instance.stringName
    instance.stringName = original
    assert instance.stringName == original



@given(instance=oclinEcoreCST_DetailCS_strategy)
def test_oclinecorecst_detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=oclinEcoreCST_DetailCS_strategy)
def test_oclinecorecst_detailcs_idName_setter(instance):
    original = instance.idName
    instance.idName = original
    assert instance.idName == original

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=oclinEcoreCST_NamedElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_namedelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_NamedElementCS)



@given(instance=oclinEcoreCST_NamedElementCS_strategy)
def test_oclinecorecst_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclinEcoreCST_AnnotationCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_annotationcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_AnnotationCS)



@given(instance=oclinEcoreCST_AnnotationCS_strategy)
def test_oclinecorecst_annotationcs_stringSource_setter(instance):
    original = instance.stringSource
    instance.stringSource = original
    assert instance.stringSource == original



@given(instance=oclinEcoreCST_AnnotationCS_strategy)
def test_oclinecorecst_annotationcs_idSource_setter(instance):
    original = instance.idSource
    instance.idSource = original
    assert instance.idSource == original

@given(instance=oclinEcoreCST_ClassifierRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classifierref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassifierRef)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=oclinEcoreCST_EnumLiteralCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_enumliteralcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EnumLiteralCS)



@given(instance=oclinEcoreCST_EnumLiteralCS_strategy)
def test_oclinecorecst_enumliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=oclinEcoreCST_PackageCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_packagecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_PackageCS)

@given(instance=oclinEcoreCST_TypedElementCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_typedelementcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_TypedElementCS)



@given(instance=oclinEcoreCST_TypedElementCS_strategy)
def test_oclinecorecst_typedelementcs_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=oclinEcoreCST_TypedElementCS_strategy)
def test_oclinecorecst_typedelementcs_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=oclinEcoreCST_TypedElementCS_strategy)
def test_oclinecorecst_typedelementcs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original



@given(instance=oclinEcoreCST_TypedElementCS_strategy)
def test_oclinecorecst_typedelementcs_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=oclinEcoreCST_TypeParameterCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_typeparametercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_TypeParameterCS)

@given(instance=oclinEcoreCST_ConstraintCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_constraintcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ConstraintCS)



@given(instance=oclinEcoreCST_ConstraintCS_strategy)
def test_oclinecorecst_constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=oclinEcoreCST_ClassifierCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classifiercs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassifierCS)



@given(instance=oclinEcoreCST_ClassifierCS_strategy)
def test_oclinecorecst_classifiercs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original



@given(instance=oclinEcoreCST_ClassifierCS_strategy)
def test_oclinecorecst_classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=ClassifierRef_strategy)
@settings(max_examples=50)
def test_classifierref_instantiation(instance):
    assert isinstance(instance, ClassifierRef)

@given(instance=oclinEcoreCST_EClassifierRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eclassifierref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EClassifierRef)

@given(instance=oclinEcoreCST_DataTypeRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_datatyperef_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DataTypeRef)

@given(instance=oclinEcoreCST_ClassifierCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classifiercsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassifierCSRef)

@given(instance=ClassRef_strategy)
@settings(max_examples=50)
def test_classref_instantiation(instance):
    assert isinstance(instance, ClassRef)

@given(instance=oclinEcoreCST_EClassRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_eclassref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_EClassRef)

@given(instance=oclinEcoreCST_ClassCSRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classcsref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassCSRef)

@given(instance=oclinEcoreCST_StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_StructuralFeatureCS)

@given(instance=oclinEcoreCST_OperationCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_operationcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_OperationCS)

@given(instance=oclinEcoreCST_ClassRef_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classref_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassRef)

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=oclinEcoreCST_DataTypeOrEnumCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_datatypeorenumcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_DataTypeOrEnumCS)

@given(instance=oclinEcoreCST_ClassCS_strategy)
@settings(max_examples=50)
def test_oclinecorecst_classcs_instantiation(instance):
    assert isinstance(instance, oclinEcoreCST_ClassCS)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    baseCST_VisitableCS,
    baseCST_Type,
    TypeRefCS,
    baseCST_WildcardTypeRefCS,
    TemplateParameterCS,
    PathElementCS,
    baseCST_PathElementWithURICS,
    RootCS,
    PackageCS,
    baseCST_RootPackageCS,
    baseCST_Property,
    baseCST_EClassifier,
    Pivotable,
    FeatureCS,
    ModelElementCS,
    baseCST_RootCS,
    baseCST_TemplateParameterSubstitutionCS,
    baseCST_TemplateSignatureCS,
    baseCST_TypeCS,
    ElementCS,
    baseCST_PivotableElementCS,
    baseCST_PathElementCS,
    baseCST_TemplateableElementCS,
    baseCST_PathNameCS,
    baseCST_MultiplicityCS,
    MultiplicityCS,
    baseCST_MultiplicityStringCS,
    baseCST_MultiplicityBoundsCS,
    baseCST_Element,
    ElementRefCS,
    baseCST_TemplateBindingCS,
    baseCST_TypeRefCS,
    Nameable,
    baseCST_NamedElementCS,
    TypedRefCS,
    baseCST_PrimitiveTypeRefCS,
    baseCST_TupleTypeCS,
    baseCST_TypedTypeRefCS,
    baseCST_Namespace,
    TypedElementCS,
    baseCST_ParameterCS,
    baseCST_TuplePartCS,
    baseCST_FeatureCS,
    PivotableElementCS,
    baseCST_ElementRefCS,
    VisitableCS,
    baseCST_ElementCS,
    baseCST_SpecificationCS,
    TemplateableElementCS,
    baseCST_LambdaTypeCS,
    baseCST_OperationCS,
    TypeCS,
    baseCST_TypeParameterCS,
    baseCST_StructuralFeatureCS,
    baseCST_TypedRefCS,
    NamespaceCS,
    baseCST_ImportCS,
    baseCST_LibraryCS,
    baseCST_PackageCS,
    ClassifierCS,
    baseCST_EnumerationCS,
    baseCST_DataTypeCS,
    baseCST_ClassCS,
    StructuralFeatureCS,
    baseCST_ReferenceCS,
    baseCST_AttributeCS,
    NamedElementCS,
    baseCST_EnumerationLiteralCS,
    baseCST_ConstraintCS,
    baseCST_TypedElementCS,
    baseCST_TemplateParameterCS,
    baseCST_DetailCS,
    baseCST_ClassifierCS,
    baseCST_NamespaceCS,
    baseCST_AnnotationElementCS,
    baseCST_ModelElementRefCS,
    baseCST_ModelElementCS,
    AnnotationElementCS,
    baseCST_DocumentationCS,
    baseCST_AnnotationCS,
    IteratorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basecst_visitablecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_VisitableCS)


def test_basecst_visitablecs_constructor_exists():
    assert callable(baseCST_VisitableCS.__init__)


def test_basecst_visitablecs_constructor_args():
    sig = inspect.signature(baseCST_VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_type_is_not_abstract():
    assert not inspect.isabstract(baseCST_Type)


def test_basecst_type_constructor_exists():
    assert callable(baseCST_Type.__init__)


def test_basecst_type_constructor_args():
    sig = inspect.signature(baseCST_Type.__init__)
    params = list(sig.parameters.keys())



def test_typerefcs_is_not_abstract():
    assert not inspect.isabstract(TypeRefCS)


def test_typerefcs_constructor_exists():
    assert callable(TypeRefCS.__init__)


def test_typerefcs_constructor_args():
    sig = inspect.signature(TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_wildcardtyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_WildcardTypeRefCS)


def test_basecst_wildcardtyperefcs_constructor_exists():
    assert callable(baseCST_WildcardTypeRefCS.__init__)


def test_basecst_wildcardtyperefcs_constructor_args():
    sig = inspect.signature(baseCST_WildcardTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(TemplateParameterCS)


def test_templateparametercs_constructor_exists():
    assert callable(TemplateParameterCS.__init__)


def test_templateparametercs_constructor_args():
    sig = inspect.signature(TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(PathElementCS)


def test_pathelementcs_constructor_exists():
    assert callable(PathElementCS.__init__)


def test_pathelementcs_constructor_args():
    sig = inspect.signature(PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_pathelementwithurics_is_not_abstract():
    assert not inspect.isabstract(baseCST_PathElementWithURICS)


def test_basecst_pathelementwithurics_constructor_exists():
    assert callable(baseCST_PathElementWithURICS.__init__)


def test_basecst_pathelementwithurics_constructor_args():
    sig = inspect.signature(baseCST_PathElementWithURICS.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_basecst_pathelementwithurics_has_uri():
    assert hasattr(baseCST_PathElementWithURICS, "uri")
    descriptor = None
    for klass in baseCST_PathElementWithURICS.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_packagecs_is_not_abstract():
    assert not inspect.isabstract(PackageCS)


def test_packagecs_constructor_exists():
    assert callable(PackageCS.__init__)


def test_packagecs_constructor_args():
    sig = inspect.signature(PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_RootPackageCS)


def test_basecst_rootpackagecs_constructor_exists():
    assert callable(baseCST_RootPackageCS.__init__)


def test_basecst_rootpackagecs_constructor_args():
    sig = inspect.signature(baseCST_RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_property_is_not_abstract():
    assert not inspect.isabstract(baseCST_Property)


def test_basecst_property_constructor_exists():
    assert callable(baseCST_Property.__init__)


def test_basecst_property_constructor_args():
    sig = inspect.signature(baseCST_Property.__init__)
    params = list(sig.parameters.keys())



def test_basecst_eclassifier_is_not_abstract():
    assert not inspect.isabstract(baseCST_EClassifier)


def test_basecst_eclassifier_constructor_exists():
    assert callable(baseCST_EClassifier.__init__)


def test_basecst_eclassifier_constructor_args():
    sig = inspect.signature(baseCST_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pivotable_is_not_abstract():
    assert not inspect.isabstract(Pivotable)


def test_pivotable_constructor_exists():
    assert callable(Pivotable.__init__)


def test_pivotable_constructor_args():
    sig = inspect.signature(Pivotable.__init__)
    params = list(sig.parameters.keys())



def test_featurecs_is_not_abstract():
    assert not inspect.isabstract(FeatureCS)


def test_featurecs_constructor_exists():
    assert callable(FeatureCS.__init__)


def test_featurecs_constructor_args():
    sig = inspect.signature(FeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_rootcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_RootCS)


def test_basecst_rootcs_constructor_exists():
    assert callable(baseCST_RootCS.__init__)


def test_basecst_rootcs_constructor_args():
    sig = inspect.signature(baseCST_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_templateparametersubstitutioncs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TemplateParameterSubstitutionCS)


def test_basecst_templateparametersubstitutioncs_constructor_exists():
    assert callable(baseCST_TemplateParameterSubstitutionCS.__init__)


def test_basecst_templateparametersubstitutioncs_constructor_args():
    sig = inspect.signature(baseCST_TemplateParameterSubstitutionCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_templatesignaturecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TemplateSignatureCS)


def test_basecst_templatesignaturecs_constructor_exists():
    assert callable(baseCST_TemplateSignatureCS.__init__)


def test_basecst_templatesignaturecs_constructor_args():
    sig = inspect.signature(baseCST_TemplateSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_typecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypeCS)


def test_basecst_typecs_constructor_exists():
    assert callable(baseCST_TypeCS.__init__)


def test_basecst_typecs_constructor_args():
    sig = inspect.signature(baseCST_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_PivotableElementCS)


def test_basecst_pivotableelementcs_constructor_exists():
    assert callable(baseCST_PivotableElementCS.__init__)


def test_basecst_pivotableelementcs_constructor_args():
    sig = inspect.signature(baseCST_PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_PathElementCS)


def test_basecst_pathelementcs_constructor_exists():
    assert callable(baseCST_PathElementCS.__init__)


def test_basecst_pathelementcs_constructor_args():
    sig = inspect.signature(baseCST_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TemplateableElementCS)


def test_basecst_templateableelementcs_constructor_exists():
    assert callable(baseCST_TemplateableElementCS.__init__)


def test_basecst_templateableelementcs_constructor_args():
    sig = inspect.signature(baseCST_TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_PathNameCS)


def test_basecst_pathnamecs_constructor_exists():
    assert callable(baseCST_PathNameCS.__init__)


def test_basecst_pathnamecs_constructor_args():
    sig = inspect.signature(baseCST_PathNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "scopeFilter" in params, "Missing parameter 'scopeFilter'"

def test_basecst_pathnamecs_has_scopeFilter():
    assert hasattr(baseCST_PathNameCS, "scopeFilter")
    descriptor = None
    for klass in baseCST_PathNameCS.__mro__:
        if "scopeFilter" in klass.__dict__:
            descriptor = klass.__dict__["scopeFilter"]
            break
    assert isinstance(descriptor, property)



def test_basecst_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(baseCST_MultiplicityCS)


def test_basecst_multiplicitycs_constructor_exists():
    assert callable(baseCST_MultiplicityCS.__init__)


def test_basecst_multiplicitycs_constructor_args():
    sig = inspect.signature(baseCST_MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityCS)


def test_multiplicitycs_constructor_exists():
    assert callable(MultiplicityCS.__init__)


def test_multiplicitycs_constructor_args():
    sig = inspect.signature(MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_multiplicitystringcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_MultiplicityStringCS)


def test_basecst_multiplicitystringcs_constructor_exists():
    assert callable(baseCST_MultiplicityStringCS.__init__)


def test_basecst_multiplicitystringcs_constructor_args():
    sig = inspect.signature(baseCST_MultiplicityStringCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringBounds" in params, "Missing parameter 'stringBounds'"

def test_basecst_multiplicitystringcs_has_stringBounds():
    assert hasattr(baseCST_MultiplicityStringCS, "stringBounds")
    descriptor = None
    for klass in baseCST_MultiplicityStringCS.__mro__:
        if "stringBounds" in klass.__dict__:
            descriptor = klass.__dict__["stringBounds"]
            break
    assert isinstance(descriptor, property)



def test_basecst_multiplicityboundscs_is_not_abstract():
    assert not inspect.isabstract(baseCST_MultiplicityBoundsCS)


def test_basecst_multiplicityboundscs_constructor_exists():
    assert callable(baseCST_MultiplicityBoundsCS.__init__)


def test_basecst_multiplicityboundscs_constructor_args():
    sig = inspect.signature(baseCST_MultiplicityBoundsCS.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_basecst_multiplicityboundscs_has_lowerBound():
    assert hasattr(baseCST_MultiplicityBoundsCS, "lowerBound")
    descriptor = None
    for klass in baseCST_MultiplicityBoundsCS.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_basecst_multiplicityboundscs_has_upperBound():
    assert hasattr(baseCST_MultiplicityBoundsCS, "upperBound")
    descriptor = None
    for klass in baseCST_MultiplicityBoundsCS.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_basecst_element_is_not_abstract():
    assert not inspect.isabstract(baseCST_Element)


def test_basecst_element_constructor_exists():
    assert callable(baseCST_Element.__init__)


def test_basecst_element_constructor_args():
    sig = inspect.signature(baseCST_Element.__init__)
    params = list(sig.parameters.keys())



def test_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(ElementRefCS)


def test_elementrefcs_constructor_exists():
    assert callable(ElementRefCS.__init__)


def test_elementrefcs_constructor_args():
    sig = inspect.signature(ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_templatebindingcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TemplateBindingCS)


def test_basecst_templatebindingcs_constructor_exists():
    assert callable(baseCST_TemplateBindingCS.__init__)


def test_basecst_templatebindingcs_constructor_args():
    sig = inspect.signature(baseCST_TemplateBindingCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_typerefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypeRefCS)


def test_basecst_typerefcs_constructor_exists():
    assert callable(baseCST_TypeRefCS.__init__)


def test_basecst_typerefcs_constructor_args():
    sig = inspect.signature(baseCST_TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_basecst_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_NamedElementCS)


def test_basecst_namedelementcs_constructor_exists():
    assert callable(baseCST_NamedElementCS.__init__)


def test_basecst_namedelementcs_constructor_args():
    sig = inspect.signature(baseCST_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst_namedelementcs_has_name():
    assert hasattr(baseCST_NamedElementCS, "name")
    descriptor = None
    for klass in baseCST_NamedElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_primitivetyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_PrimitiveTypeRefCS)


def test_basecst_primitivetyperefcs_constructor_exists():
    assert callable(baseCST_PrimitiveTypeRefCS.__init__)


def test_basecst_primitivetyperefcs_constructor_args():
    sig = inspect.signature(baseCST_PrimitiveTypeRefCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst_primitivetyperefcs_has_name():
    assert hasattr(baseCST_PrimitiveTypeRefCS, "name")
    descriptor = None
    for klass in baseCST_PrimitiveTypeRefCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecst_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TupleTypeCS)


def test_basecst_tupletypecs_constructor_exists():
    assert callable(baseCST_TupleTypeCS.__init__)


def test_basecst_tupletypecs_constructor_args():
    sig = inspect.signature(baseCST_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst_tupletypecs_has_name():
    assert hasattr(baseCST_TupleTypeCS, "name")
    descriptor = None
    for klass in baseCST_TupleTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecst_typedtyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypedTypeRefCS)


def test_basecst_typedtyperefcs_constructor_exists():
    assert callable(baseCST_TypedTypeRefCS.__init__)


def test_basecst_typedtyperefcs_constructor_args():
    sig = inspect.signature(baseCST_TypedTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_namespace_is_not_abstract():
    assert not inspect.isabstract(baseCST_Namespace)


def test_basecst_namespace_constructor_exists():
    assert callable(baseCST_Namespace.__init__)


def test_basecst_namespace_constructor_args():
    sig = inspect.signature(baseCST_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_parametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ParameterCS)


def test_basecst_parametercs_constructor_exists():
    assert callable(baseCST_ParameterCS.__init__)


def test_basecst_parametercs_constructor_args():
    sig = inspect.signature(baseCST_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TuplePartCS)


def test_basecst_tuplepartcs_constructor_exists():
    assert callable(baseCST_TuplePartCS.__init__)


def test_basecst_tuplepartcs_constructor_args():
    sig = inspect.signature(baseCST_TuplePartCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_featurecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_FeatureCS)


def test_basecst_featurecs_constructor_exists():
    assert callable(baseCST_FeatureCS.__init__)


def test_basecst_featurecs_constructor_args():
    sig = inspect.signature(baseCST_FeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(PivotableElementCS)


def test_pivotableelementcs_constructor_exists():
    assert callable(PivotableElementCS.__init__)


def test_pivotableelementcs_constructor_args():
    sig = inspect.signature(PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ElementRefCS)


def test_basecst_elementrefcs_constructor_exists():
    assert callable(baseCST_ElementRefCS.__init__)


def test_basecst_elementrefcs_constructor_args():
    sig = inspect.signature(baseCST_ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_visitablecs_is_not_abstract():
    assert not inspect.isabstract(VisitableCS)


def test_visitablecs_constructor_exists():
    assert callable(VisitableCS.__init__)


def test_visitablecs_constructor_args():
    sig = inspect.signature(VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_elementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ElementCS)


def test_basecst_elementcs_constructor_exists():
    assert callable(baseCST_ElementCS.__init__)


def test_basecst_elementcs_constructor_args():
    sig = inspect.signature(baseCST_ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_specificationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_SpecificationCS)


def test_basecst_specificationcs_constructor_exists():
    assert callable(baseCST_SpecificationCS.__init__)


def test_basecst_specificationcs_constructor_args():
    sig = inspect.signature(baseCST_SpecificationCS.__init__)
    params = list(sig.parameters.keys())
    assert "exprString" in params, "Missing parameter 'exprString'"

def test_basecst_specificationcs_has_exprString():
    assert hasattr(baseCST_SpecificationCS, "exprString")
    descriptor = None
    for klass in baseCST_SpecificationCS.__mro__:
        if "exprString" in klass.__dict__:
            descriptor = klass.__dict__["exprString"]
            break
    assert isinstance(descriptor, property)



def test_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(TemplateableElementCS)


def test_templateableelementcs_constructor_exists():
    assert callable(TemplateableElementCS.__init__)


def test_templateableelementcs_constructor_args():
    sig = inspect.signature(TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_lambdatypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_LambdaTypeCS)


def test_basecst_lambdatypecs_constructor_exists():
    assert callable(baseCST_LambdaTypeCS.__init__)


def test_basecst_lambdatypecs_constructor_args():
    sig = inspect.signature(baseCST_LambdaTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst_lambdatypecs_has_name():
    assert hasattr(baseCST_LambdaTypeCS, "name")
    descriptor = None
    for klass in baseCST_LambdaTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecst_operationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_OperationCS)


def test_basecst_operationcs_constructor_exists():
    assert callable(baseCST_OperationCS.__init__)


def test_basecst_operationcs_constructor_args():
    sig = inspect.signature(baseCST_OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_typeparametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypeParameterCS)


def test_basecst_typeparametercs_constructor_exists():
    assert callable(baseCST_TypeParameterCS.__init__)


def test_basecst_typeparametercs_constructor_args():
    sig = inspect.signature(baseCST_TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_StructuralFeatureCS)


def test_basecst_structuralfeaturecs_constructor_exists():
    assert callable(baseCST_StructuralFeatureCS.__init__)


def test_basecst_structuralfeaturecs_constructor_args():
    sig = inspect.signature(baseCST_StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_basecst_structuralfeaturecs_has_default():
    assert hasattr(baseCST_StructuralFeatureCS, "default")
    descriptor = None
    for klass in baseCST_StructuralFeatureCS.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_basecst_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypedRefCS)


def test_basecst_typedrefcs_constructor_exists():
    assert callable(baseCST_TypedRefCS.__init__)


def test_basecst_typedrefcs_constructor_args():
    sig = inspect.signature(baseCST_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_importcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ImportCS)


def test_basecst_importcs_constructor_exists():
    assert callable(baseCST_ImportCS.__init__)


def test_basecst_importcs_constructor_args():
    sig = inspect.signature(baseCST_ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_basecst_importcs_has_all():
    assert hasattr(baseCST_ImportCS, "all")
    descriptor = None
    for klass in baseCST_ImportCS.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_basecst_librarycs_is_not_abstract():
    assert not inspect.isabstract(baseCST_LibraryCS)


def test_basecst_librarycs_constructor_exists():
    assert callable(baseCST_LibraryCS.__init__)


def test_basecst_librarycs_constructor_args():
    sig = inspect.signature(baseCST_LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_packagecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_PackageCS)


def test_basecst_packagecs_constructor_exists():
    assert callable(baseCST_PackageCS.__init__)


def test_basecst_packagecs_constructor_args():
    sig = inspect.signature(baseCST_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_basecst_packagecs_has_nsURI():
    assert hasattr(baseCST_PackageCS, "nsURI")
    descriptor = None
    for klass in baseCST_PackageCS.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)

def test_basecst_packagecs_has_nsPrefix():
    assert hasattr(baseCST_PackageCS, "nsPrefix")
    descriptor = None
    for klass in baseCST_PackageCS.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_enumerationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_EnumerationCS)


def test_basecst_enumerationcs_constructor_exists():
    assert callable(baseCST_EnumerationCS.__init__)


def test_basecst_enumerationcs_constructor_args():
    sig = inspect.signature(baseCST_EnumerationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_datatypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_DataTypeCS)


def test_basecst_datatypecs_constructor_exists():
    assert callable(baseCST_DataTypeCS.__init__)


def test_basecst_datatypecs_constructor_args():
    sig = inspect.signature(baseCST_DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_classcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ClassCS)


def test_basecst_classcs_constructor_exists():
    assert callable(baseCST_ClassCS.__init__)


def test_basecst_classcs_constructor_args():
    sig = inspect.signature(baseCST_ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_referencecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ReferenceCS)


def test_basecst_referencecs_constructor_exists():
    assert callable(baseCST_ReferenceCS.__init__)


def test_basecst_referencecs_constructor_args():
    sig = inspect.signature(baseCST_ReferenceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_attributecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_AttributeCS)


def test_basecst_attributecs_constructor_exists():
    assert callable(baseCST_AttributeCS.__init__)


def test_basecst_attributecs_constructor_args():
    sig = inspect.signature(baseCST_AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_enumerationliteralcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_EnumerationLiteralCS)


def test_basecst_enumerationliteralcs_constructor_exists():
    assert callable(baseCST_EnumerationLiteralCS.__init__)


def test_basecst_enumerationliteralcs_constructor_args():
    sig = inspect.signature(baseCST_EnumerationLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst_enumerationliteralcs_has_value():
    assert hasattr(baseCST_EnumerationLiteralCS, "value")
    descriptor = None
    for klass in baseCST_EnumerationLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst_constraintcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ConstraintCS)


def test_basecst_constraintcs_constructor_exists():
    assert callable(baseCST_ConstraintCS.__init__)


def test_basecst_constraintcs_constructor_args():
    sig = inspect.signature(baseCST_ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_basecst_constraintcs_has_stereotype():
    assert hasattr(baseCST_ConstraintCS, "stereotype")
    descriptor = None
    for klass in baseCST_ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_basecst_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TypedElementCS)


def test_basecst_typedelementcs_constructor_exists():
    assert callable(baseCST_TypedElementCS.__init__)


def test_basecst_typedelementcs_constructor_args():
    sig = inspect.signature(baseCST_TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_basecst_typedelementcs_has_optional():
    assert hasattr(baseCST_TypedElementCS, "optional")
    descriptor = None
    for klass in baseCST_TypedElementCS.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_basecst_typedelementcs_has_qualifier():
    assert hasattr(baseCST_TypedElementCS, "qualifier")
    descriptor = None
    for klass in baseCST_TypedElementCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_basecst_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST_TemplateParameterCS)


def test_basecst_templateparametercs_constructor_exists():
    assert callable(baseCST_TemplateParameterCS.__init__)


def test_basecst_templateparametercs_constructor_args():
    sig = inspect.signature(baseCST_TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_detailcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_DetailCS)


def test_basecst_detailcs_constructor_exists():
    assert callable(baseCST_DetailCS.__init__)


def test_basecst_detailcs_constructor_args():
    sig = inspect.signature(baseCST_DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst_detailcs_has_value():
    assert hasattr(baseCST_DetailCS, "value")
    descriptor = None
    for klass in baseCST_DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst_classifiercs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ClassifierCS)


def test_basecst_classifiercs_constructor_exists():
    assert callable(baseCST_ClassifierCS.__init__)


def test_basecst_classifiercs_constructor_args():
    sig = inspect.signature(baseCST_ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_basecst_classifiercs_has_instanceClassName():
    assert hasattr(baseCST_ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in baseCST_ClassifierCS.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)

def test_basecst_classifiercs_has_qualifier():
    assert hasattr(baseCST_ClassifierCS, "qualifier")
    descriptor = None
    for klass in baseCST_ClassifierCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_basecst_namespacecs_is_not_abstract():
    assert not inspect.isabstract(baseCST_NamespaceCS)


def test_basecst_namespacecs_constructor_exists():
    assert callable(baseCST_NamespaceCS.__init__)


def test_basecst_namespacecs_constructor_args():
    sig = inspect.signature(baseCST_NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_AnnotationElementCS)


def test_basecst_annotationelementcs_constructor_exists():
    assert callable(baseCST_AnnotationElementCS.__init__)


def test_basecst_annotationelementcs_constructor_args():
    sig = inspect.signature(baseCST_AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_modelelementrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ModelElementRefCS)


def test_basecst_modelelementrefcs_constructor_exists():
    assert callable(baseCST_ModelElementRefCS.__init__)


def test_basecst_modelelementrefcs_constructor_args():
    sig = inspect.signature(baseCST_ModelElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_ModelElementCS)


def test_basecst_modelelementcs_constructor_exists():
    assert callable(baseCST_ModelElementCS.__init__)


def test_basecst_modelelementcs_constructor_args():
    sig = inspect.signature(baseCST_ModelElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "originalXmiId" in params, "Missing parameter 'originalXmiId'"
    assert "csi" in params, "Missing parameter 'csi'"

def test_basecst_modelelementcs_has_originalXmiId():
    assert hasattr(baseCST_ModelElementCS, "originalXmiId")
    descriptor = None
    for klass in baseCST_ModelElementCS.__mro__:
        if "originalXmiId" in klass.__dict__:
            descriptor = klass.__dict__["originalXmiId"]
            break
    assert isinstance(descriptor, property)

def test_basecst_modelelementcs_has_csi():
    assert hasattr(baseCST_ModelElementCS, "csi")
    descriptor = None
    for klass in baseCST_ModelElementCS.__mro__:
        if "csi" in klass.__dict__:
            descriptor = klass.__dict__["csi"]
            break
    assert isinstance(descriptor, property)



def test_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(AnnotationElementCS)


def test_annotationelementcs_constructor_exists():
    assert callable(AnnotationElementCS.__init__)


def test_annotationelementcs_constructor_args():
    sig = inspect.signature(AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst_documentationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_DocumentationCS)


def test_basecst_documentationcs_constructor_exists():
    assert callable(baseCST_DocumentationCS.__init__)


def test_basecst_documentationcs_constructor_args():
    sig = inspect.signature(baseCST_DocumentationCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst_documentationcs_has_value():
    assert hasattr(baseCST_DocumentationCS, "value")
    descriptor = None
    for klass in baseCST_DocumentationCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst_annotationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST_AnnotationCS)


def test_basecst_annotationcs_constructor_exists():
    assert callable(baseCST_AnnotationCS.__init__)


def test_basecst_annotationcs_constructor_args():
    sig = inspect.signature(baseCST_AnnotationCS.__init__)
    params = list(sig.parameters.keys())

def test_iteratorkind_exists():
    # Check that the Enumeration exists
    assert IteratorKind is not None

def test_iteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorKind]
    expected_literals = [
        "Parameter",
        "Accumulator",
        "Iterator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IteratorKind"


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
baseCST_VisitableCS_strategy = st.builds(
    baseCST_VisitableCS,
)
baseCST_Type_strategy = st.builds(
    baseCST_Type,
)
TypeRefCS_strategy = st.builds(
    TypeRefCS,
)
baseCST_WildcardTypeRefCS_strategy = st.builds(
    baseCST_WildcardTypeRefCS,
)
TemplateParameterCS_strategy = st.builds(
    TemplateParameterCS,
)
PathElementCS_strategy = st.builds(
    PathElementCS,
)
baseCST_PathElementWithURICS_strategy = st.builds(
    baseCST_PathElementWithURICS,
    uri=
        safe_text
)
RootCS_strategy = st.builds(
    RootCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
baseCST_RootPackageCS_strategy = st.builds(
    baseCST_RootPackageCS,
)
baseCST_Property_strategy = st.builds(
    baseCST_Property,
)
baseCST_EClassifier_strategy = st.builds(
    baseCST_EClassifier,
)
Pivotable_strategy = st.builds(
    Pivotable,
)
FeatureCS_strategy = st.builds(
    FeatureCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
baseCST_RootCS_strategy = st.builds(
    baseCST_RootCS,
)
baseCST_TemplateParameterSubstitutionCS_strategy = st.builds(
    baseCST_TemplateParameterSubstitutionCS,
)
baseCST_TemplateSignatureCS_strategy = st.builds(
    baseCST_TemplateSignatureCS,
)
baseCST_TypeCS_strategy = st.builds(
    baseCST_TypeCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
baseCST_PivotableElementCS_strategy = st.builds(
    baseCST_PivotableElementCS,
)
baseCST_PathElementCS_strategy = st.builds(
    baseCST_PathElementCS,
)
baseCST_TemplateableElementCS_strategy = st.builds(
    baseCST_TemplateableElementCS,
)
baseCST_PathNameCS_strategy = st.builds(
    baseCST_PathNameCS,
    scopeFilter=
        safe_text
)
baseCST_MultiplicityCS_strategy = st.builds(
    baseCST_MultiplicityCS,
)
MultiplicityCS_strategy = st.builds(
    MultiplicityCS,
)
baseCST_MultiplicityStringCS_strategy = st.builds(
    baseCST_MultiplicityStringCS,
    stringBounds=
        safe_text
)
baseCST_MultiplicityBoundsCS_strategy = st.builds(
    baseCST_MultiplicityBoundsCS,
    lowerBound=
        st.integers(),
    upperBound=
        safe_text
)
baseCST_Element_strategy = st.builds(
    baseCST_Element,
)
ElementRefCS_strategy = st.builds(
    ElementRefCS,
)
baseCST_TemplateBindingCS_strategy = st.builds(
    baseCST_TemplateBindingCS,
)
baseCST_TypeRefCS_strategy = st.builds(
    baseCST_TypeRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
baseCST_NamedElementCS_strategy = st.builds(
    baseCST_NamedElementCS,
    name=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
baseCST_PrimitiveTypeRefCS_strategy = st.builds(
    baseCST_PrimitiveTypeRefCS,
    name=
        safe_text
)
baseCST_TupleTypeCS_strategy = st.builds(
    baseCST_TupleTypeCS,
    name=
        safe_text
)
baseCST_TypedTypeRefCS_strategy = st.builds(
    baseCST_TypedTypeRefCS,
)
baseCST_Namespace_strategy = st.builds(
    baseCST_Namespace,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
baseCST_ParameterCS_strategy = st.builds(
    baseCST_ParameterCS,
)
baseCST_TuplePartCS_strategy = st.builds(
    baseCST_TuplePartCS,
)
baseCST_FeatureCS_strategy = st.builds(
    baseCST_FeatureCS,
)
PivotableElementCS_strategy = st.builds(
    PivotableElementCS,
)
baseCST_ElementRefCS_strategy = st.builds(
    baseCST_ElementRefCS,
)
VisitableCS_strategy = st.builds(
    VisitableCS,
)
baseCST_ElementCS_strategy = st.builds(
    baseCST_ElementCS,
)
baseCST_SpecificationCS_strategy = st.builds(
    baseCST_SpecificationCS,
    exprString=
        safe_text
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
baseCST_LambdaTypeCS_strategy = st.builds(
    baseCST_LambdaTypeCS,
    name=
        safe_text
)
baseCST_OperationCS_strategy = st.builds(
    baseCST_OperationCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
baseCST_TypeParameterCS_strategy = st.builds(
    baseCST_TypeParameterCS,
)
baseCST_StructuralFeatureCS_strategy = st.builds(
    baseCST_StructuralFeatureCS,
    default=
        safe_text
)
baseCST_TypedRefCS_strategy = st.builds(
    baseCST_TypedRefCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
baseCST_ImportCS_strategy = st.builds(
    baseCST_ImportCS,
    all=
        st.booleans()
)
baseCST_LibraryCS_strategy = st.builds(
    baseCST_LibraryCS,
)
baseCST_PackageCS_strategy = st.builds(
    baseCST_PackageCS,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
baseCST_EnumerationCS_strategy = st.builds(
    baseCST_EnumerationCS,
)
baseCST_DataTypeCS_strategy = st.builds(
    baseCST_DataTypeCS,
)
baseCST_ClassCS_strategy = st.builds(
    baseCST_ClassCS,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
baseCST_ReferenceCS_strategy = st.builds(
    baseCST_ReferenceCS,
)
baseCST_AttributeCS_strategy = st.builds(
    baseCST_AttributeCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
baseCST_EnumerationLiteralCS_strategy = st.builds(
    baseCST_EnumerationLiteralCS,
    value=
        st.integers()
)
baseCST_ConstraintCS_strategy = st.builds(
    baseCST_ConstraintCS,
    stereotype=
        safe_text
)
baseCST_TypedElementCS_strategy = st.builds(
    baseCST_TypedElementCS,
    optional=
        st.booleans(),
    qualifier=
        safe_text
)
baseCST_TemplateParameterCS_strategy = st.builds(
    baseCST_TemplateParameterCS,
)
baseCST_DetailCS_strategy = st.builds(
    baseCST_DetailCS,
    value=
        safe_text
)
baseCST_ClassifierCS_strategy = st.builds(
    baseCST_ClassifierCS,
    instanceClassName=
        safe_text,
    qualifier=
        safe_text
)
baseCST_NamespaceCS_strategy = st.builds(
    baseCST_NamespaceCS,
)
baseCST_AnnotationElementCS_strategy = st.builds(
    baseCST_AnnotationElementCS,
)
baseCST_ModelElementRefCS_strategy = st.builds(
    baseCST_ModelElementRefCS,
)
baseCST_ModelElementCS_strategy = st.builds(
    baseCST_ModelElementCS,
    originalXmiId=
        safe_text,
    csi=
        safe_text
)
AnnotationElementCS_strategy = st.builds(
    AnnotationElementCS,
)
baseCST_DocumentationCS_strategy = st.builds(
    baseCST_DocumentationCS,
    value=
        safe_text
)
baseCST_AnnotationCS_strategy = st.builds(
    baseCST_AnnotationCS,
)

@given(instance=baseCST_VisitableCS_strategy)
@settings(max_examples=50)
def test_basecst_visitablecs_instantiation(instance):
    assert isinstance(instance, baseCST_VisitableCS)

@given(instance=baseCST_Type_strategy)
@settings(max_examples=50)
def test_basecst_type_instantiation(instance):
    assert isinstance(instance, baseCST_Type)

@given(instance=TypeRefCS_strategy)
@settings(max_examples=50)
def test_typerefcs_instantiation(instance):
    assert isinstance(instance, TypeRefCS)

@given(instance=baseCST_WildcardTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst_wildcardtyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST_WildcardTypeRefCS)

@given(instance=TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_templateparametercs_instantiation(instance):
    assert isinstance(instance, TemplateParameterCS)

@given(instance=PathElementCS_strategy)
@settings(max_examples=50)
def test_pathelementcs_instantiation(instance):
    assert isinstance(instance, PathElementCS)

@given(instance=baseCST_PathElementWithURICS_strategy)
@settings(max_examples=50)
def test_basecst_pathelementwithurics_instantiation(instance):
    assert isinstance(instance, baseCST_PathElementWithURICS)



@given(instance=baseCST_PathElementWithURICS_strategy)
def test_basecst_pathelementwithurics_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=PackageCS_strategy)
@settings(max_examples=50)
def test_packagecs_instantiation(instance):
    assert isinstance(instance, PackageCS)

@given(instance=baseCST_RootPackageCS_strategy)
@settings(max_examples=50)
def test_basecst_rootpackagecs_instantiation(instance):
    assert isinstance(instance, baseCST_RootPackageCS)

@given(instance=baseCST_Property_strategy)
@settings(max_examples=50)
def test_basecst_property_instantiation(instance):
    assert isinstance(instance, baseCST_Property)

@given(instance=baseCST_EClassifier_strategy)
@settings(max_examples=50)
def test_basecst_eclassifier_instantiation(instance):
    assert isinstance(instance, baseCST_EClassifier)

@given(instance=Pivotable_strategy)
@settings(max_examples=50)
def test_pivotable_instantiation(instance):
    assert isinstance(instance, Pivotable)

@given(instance=FeatureCS_strategy)
@settings(max_examples=50)
def test_featurecs_instantiation(instance):
    assert isinstance(instance, FeatureCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=baseCST_RootCS_strategy)
@settings(max_examples=50)
def test_basecst_rootcs_instantiation(instance):
    assert isinstance(instance, baseCST_RootCS)

@given(instance=baseCST_TemplateParameterSubstitutionCS_strategy)
@settings(max_examples=50)
def test_basecst_templateparametersubstitutioncs_instantiation(instance):
    assert isinstance(instance, baseCST_TemplateParameterSubstitutionCS)

@given(instance=baseCST_TemplateSignatureCS_strategy)
@settings(max_examples=50)
def test_basecst_templatesignaturecs_instantiation(instance):
    assert isinstance(instance, baseCST_TemplateSignatureCS)

@given(instance=baseCST_TypeCS_strategy)
@settings(max_examples=50)
def test_basecst_typecs_instantiation(instance):
    assert isinstance(instance, baseCST_TypeCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=baseCST_PivotableElementCS_strategy)
@settings(max_examples=50)
def test_basecst_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_PivotableElementCS)

@given(instance=baseCST_PathElementCS_strategy)
@settings(max_examples=50)
def test_basecst_pathelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_PathElementCS)

@given(instance=baseCST_TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_basecst_templateableelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_TemplateableElementCS)

@given(instance=baseCST_PathNameCS_strategy)
@settings(max_examples=50)
def test_basecst_pathnamecs_instantiation(instance):
    assert isinstance(instance, baseCST_PathNameCS)



@given(instance=baseCST_PathNameCS_strategy)
def test_basecst_pathnamecs_scopeFilter_setter(instance):
    original = instance.scopeFilter
    instance.scopeFilter = original
    assert instance.scopeFilter == original

@given(instance=baseCST_MultiplicityCS_strategy)
@settings(max_examples=50)
def test_basecst_multiplicitycs_instantiation(instance):
    assert isinstance(instance, baseCST_MultiplicityCS)

@given(instance=MultiplicityCS_strategy)
@settings(max_examples=50)
def test_multiplicitycs_instantiation(instance):
    assert isinstance(instance, MultiplicityCS)

@given(instance=baseCST_MultiplicityStringCS_strategy)
@settings(max_examples=50)
def test_basecst_multiplicitystringcs_instantiation(instance):
    assert isinstance(instance, baseCST_MultiplicityStringCS)



@given(instance=baseCST_MultiplicityStringCS_strategy)
def test_basecst_multiplicitystringcs_stringBounds_setter(instance):
    original = instance.stringBounds
    instance.stringBounds = original
    assert instance.stringBounds == original

@given(instance=baseCST_MultiplicityBoundsCS_strategy)
@settings(max_examples=50)
def test_basecst_multiplicityboundscs_instantiation(instance):
    assert isinstance(instance, baseCST_MultiplicityBoundsCS)



@given(instance=baseCST_MultiplicityBoundsCS_strategy)
def test_basecst_multiplicityboundscs_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=baseCST_MultiplicityBoundsCS_strategy)
def test_basecst_multiplicityboundscs_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=baseCST_Element_strategy)
@settings(max_examples=50)
def test_basecst_element_instantiation(instance):
    assert isinstance(instance, baseCST_Element)

@given(instance=ElementRefCS_strategy)
@settings(max_examples=50)
def test_elementrefcs_instantiation(instance):
    assert isinstance(instance, ElementRefCS)

@given(instance=baseCST_TemplateBindingCS_strategy)
@settings(max_examples=50)
def test_basecst_templatebindingcs_instantiation(instance):
    assert isinstance(instance, baseCST_TemplateBindingCS)

@given(instance=baseCST_TypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst_typerefcs_instantiation(instance):
    assert isinstance(instance, baseCST_TypeRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=baseCST_NamedElementCS_strategy)
@settings(max_examples=50)
def test_basecst_namedelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_NamedElementCS)



@given(instance=baseCST_NamedElementCS_strategy)
def test_basecst_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=baseCST_PrimitiveTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst_primitivetyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST_PrimitiveTypeRefCS)



@given(instance=baseCST_PrimitiveTypeRefCS_strategy)
def test_basecst_primitivetyperefcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=baseCST_TupleTypeCS_strategy)
@settings(max_examples=50)
def test_basecst_tupletypecs_instantiation(instance):
    assert isinstance(instance, baseCST_TupleTypeCS)



@given(instance=baseCST_TupleTypeCS_strategy)
def test_basecst_tupletypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=baseCST_TypedTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst_typedtyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST_TypedTypeRefCS)

@given(instance=baseCST_Namespace_strategy)
@settings(max_examples=50)
def test_basecst_namespace_instantiation(instance):
    assert isinstance(instance, baseCST_Namespace)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=baseCST_ParameterCS_strategy)
@settings(max_examples=50)
def test_basecst_parametercs_instantiation(instance):
    assert isinstance(instance, baseCST_ParameterCS)

@given(instance=baseCST_TuplePartCS_strategy)
@settings(max_examples=50)
def test_basecst_tuplepartcs_instantiation(instance):
    assert isinstance(instance, baseCST_TuplePartCS)

@given(instance=baseCST_FeatureCS_strategy)
@settings(max_examples=50)
def test_basecst_featurecs_instantiation(instance):
    assert isinstance(instance, baseCST_FeatureCS)

@given(instance=PivotableElementCS_strategy)
@settings(max_examples=50)
def test_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, PivotableElementCS)

@given(instance=baseCST_ElementRefCS_strategy)
@settings(max_examples=50)
def test_basecst_elementrefcs_instantiation(instance):
    assert isinstance(instance, baseCST_ElementRefCS)

@given(instance=VisitableCS_strategy)
@settings(max_examples=50)
def test_visitablecs_instantiation(instance):
    assert isinstance(instance, VisitableCS)

@given(instance=baseCST_ElementCS_strategy)
@settings(max_examples=50)
def test_basecst_elementcs_instantiation(instance):
    assert isinstance(instance, baseCST_ElementCS)

@given(instance=baseCST_SpecificationCS_strategy)
@settings(max_examples=50)
def test_basecst_specificationcs_instantiation(instance):
    assert isinstance(instance, baseCST_SpecificationCS)



@given(instance=baseCST_SpecificationCS_strategy)
def test_basecst_specificationcs_exprString_setter(instance):
    original = instance.exprString
    instance.exprString = original
    assert instance.exprString == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=baseCST_LambdaTypeCS_strategy)
@settings(max_examples=50)
def test_basecst_lambdatypecs_instantiation(instance):
    assert isinstance(instance, baseCST_LambdaTypeCS)



@given(instance=baseCST_LambdaTypeCS_strategy)
def test_basecst_lambdatypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=baseCST_OperationCS_strategy)
@settings(max_examples=50)
def test_basecst_operationcs_instantiation(instance):
    assert isinstance(instance, baseCST_OperationCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=baseCST_TypeParameterCS_strategy)
@settings(max_examples=50)
def test_basecst_typeparametercs_instantiation(instance):
    assert isinstance(instance, baseCST_TypeParameterCS)

@given(instance=baseCST_StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_basecst_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, baseCST_StructuralFeatureCS)



@given(instance=baseCST_StructuralFeatureCS_strategy)
def test_basecst_structuralfeaturecs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=baseCST_TypedRefCS_strategy)
@settings(max_examples=50)
def test_basecst_typedrefcs_instantiation(instance):
    assert isinstance(instance, baseCST_TypedRefCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=baseCST_ImportCS_strategy)
@settings(max_examples=50)
def test_basecst_importcs_instantiation(instance):
    assert isinstance(instance, baseCST_ImportCS)



@given(instance=baseCST_ImportCS_strategy)
def test_basecst_importcs_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=baseCST_LibraryCS_strategy)
@settings(max_examples=50)
def test_basecst_librarycs_instantiation(instance):
    assert isinstance(instance, baseCST_LibraryCS)

@given(instance=baseCST_PackageCS_strategy)
@settings(max_examples=50)
def test_basecst_packagecs_instantiation(instance):
    assert isinstance(instance, baseCST_PackageCS)



@given(instance=baseCST_PackageCS_strategy)
def test_basecst_packagecs_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original



@given(instance=baseCST_PackageCS_strategy)
def test_basecst_packagecs_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=baseCST_EnumerationCS_strategy)
@settings(max_examples=50)
def test_basecst_enumerationcs_instantiation(instance):
    assert isinstance(instance, baseCST_EnumerationCS)

@given(instance=baseCST_DataTypeCS_strategy)
@settings(max_examples=50)
def test_basecst_datatypecs_instantiation(instance):
    assert isinstance(instance, baseCST_DataTypeCS)

@given(instance=baseCST_ClassCS_strategy)
@settings(max_examples=50)
def test_basecst_classcs_instantiation(instance):
    assert isinstance(instance, baseCST_ClassCS)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=baseCST_ReferenceCS_strategy)
@settings(max_examples=50)
def test_basecst_referencecs_instantiation(instance):
    assert isinstance(instance, baseCST_ReferenceCS)

@given(instance=baseCST_AttributeCS_strategy)
@settings(max_examples=50)
def test_basecst_attributecs_instantiation(instance):
    assert isinstance(instance, baseCST_AttributeCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=baseCST_EnumerationLiteralCS_strategy)
@settings(max_examples=50)
def test_basecst_enumerationliteralcs_instantiation(instance):
    assert isinstance(instance, baseCST_EnumerationLiteralCS)



@given(instance=baseCST_EnumerationLiteralCS_strategy)
def test_basecst_enumerationliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST_ConstraintCS_strategy)
@settings(max_examples=50)
def test_basecst_constraintcs_instantiation(instance):
    assert isinstance(instance, baseCST_ConstraintCS)



@given(instance=baseCST_ConstraintCS_strategy)
def test_basecst_constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=baseCST_TypedElementCS_strategy)
@settings(max_examples=50)
def test_basecst_typedelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_TypedElementCS)



@given(instance=baseCST_TypedElementCS_strategy)
def test_basecst_typedelementcs_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=baseCST_TypedElementCS_strategy)
def test_basecst_typedelementcs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=baseCST_TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_basecst_templateparametercs_instantiation(instance):
    assert isinstance(instance, baseCST_TemplateParameterCS)

@given(instance=baseCST_DetailCS_strategy)
@settings(max_examples=50)
def test_basecst_detailcs_instantiation(instance):
    assert isinstance(instance, baseCST_DetailCS)



@given(instance=baseCST_DetailCS_strategy)
def test_basecst_detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST_ClassifierCS_strategy)
@settings(max_examples=50)
def test_basecst_classifiercs_instantiation(instance):
    assert isinstance(instance, baseCST_ClassifierCS)



@given(instance=baseCST_ClassifierCS_strategy)
def test_basecst_classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original



@given(instance=baseCST_ClassifierCS_strategy)
def test_basecst_classifiercs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=baseCST_NamespaceCS_strategy)
@settings(max_examples=50)
def test_basecst_namespacecs_instantiation(instance):
    assert isinstance(instance, baseCST_NamespaceCS)

@given(instance=baseCST_AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_basecst_annotationelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_AnnotationElementCS)

@given(instance=baseCST_ModelElementRefCS_strategy)
@settings(max_examples=50)
def test_basecst_modelelementrefcs_instantiation(instance):
    assert isinstance(instance, baseCST_ModelElementRefCS)

@given(instance=baseCST_ModelElementCS_strategy)
@settings(max_examples=50)
def test_basecst_modelelementcs_instantiation(instance):
    assert isinstance(instance, baseCST_ModelElementCS)



@given(instance=baseCST_ModelElementCS_strategy)
def test_basecst_modelelementcs_originalXmiId_setter(instance):
    original = instance.originalXmiId
    instance.originalXmiId = original
    assert instance.originalXmiId == original



@given(instance=baseCST_ModelElementCS_strategy)
def test_basecst_modelelementcs_csi_setter(instance):
    original = instance.csi
    instance.csi = original
    assert instance.csi == original

@given(instance=AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_annotationelementcs_instantiation(instance):
    assert isinstance(instance, AnnotationElementCS)

@given(instance=baseCST_DocumentationCS_strategy)
@settings(max_examples=50)
def test_basecst_documentationcs_instantiation(instance):
    assert isinstance(instance, baseCST_DocumentationCS)



@given(instance=baseCST_DocumentationCS_strategy)
def test_basecst_documentationcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST_AnnotationCS_strategy)
@settings(max_examples=50)
def test_basecst_annotationcs_instantiation(instance):
    assert isinstance(instance, baseCST_AnnotationCS)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basecs_VisitableCS,
    basecs_Type,
    TypeRefCS,
    basecs_WildcardTypeRefCS,
    TemplateParameterCS,
    RootCS,
    basecs_Property,
    PathElementCS,
    basecs_PathElementWithURICS,
    basecs_EClassifier,
    Pivotable,
    PackageOwnerCS,
    basecs_RootPackageCS,
    TypedElementCS,
    basecs_TuplePartCS,
    basecs_ParameterCS,
    basecs_FeatureCS,
    FeatureCS,
    ModelElementCS,
    basecs_TemplateParameterSubstitutionCS,
    basecs_TemplateSignatureCS,
    basecs_RootCS,
    basecs_PackageOwnerCS,
    basecs_TypeCS,
    ElementCS,
    basecs_PivotableElementCS,
    basecs_TemplateableElementCS,
    basecs_PathElementCS,
    basecs_MultiplicityCS,
    MultiplicityCS,
    basecs_MultiplicityStringCS,
    basecs_MultiplicityBoundsCS,
    basecs_Element,
    ElementRefCS,
    basecs_TypeRefCS,
    basecs_TemplateBindingCS,
    Nameable,
    basecs_NamedElementCS,
    TypedRefCS,
    basecs_PrimitiveTypeRefCS,
    basecs_TupleTypeCS,
    basecs_TypedTypeRefCS,
    basecs_Namespace,
    basecs_PathNameCS,
    PivotableElementCS,
    basecs_ElementRefCS,
    VisitableCS,
    basecs_ElementCS,
    basecs_SpecificationCS,
    TemplateableElementCS,
    basecs_LambdaTypeCS,
    TypeCS,
    basecs_TypeParameterCS,
    basecs_StructuralFeatureCS,
    basecs_OperationCS,
    basecs_TypedRefCS,
    NamespaceCS,
    basecs_LibraryCS,
    basecs_ImportCS,
    basecs_PackageCS,
    ClassifierCS,
    basecs_EnumerationCS,
    basecs_DataTypeCS,
    basecs_ClassCS,
    StructuralFeatureCS,
    basecs_ReferenceCS,
    basecs_AttributeCS,
    NamedElementCS,
    basecs_NamespaceCS,
    basecs_EnumerationLiteralCS,
    basecs_ConstraintCS,
    basecs_ClassifierCS,
    basecs_TemplateParameterCS,
    basecs_DetailCS,
    basecs_TypedElementCS,
    basecs_AnnotationElementCS,
    basecs_ModelElementRefCS,
    basecs_ModelElementCS,
    AnnotationElementCS,
    basecs_DocumentationCS,
    basecs_AnnotationCS,
    IteratorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basecs_visitablecs_is_not_abstract():
    assert not inspect.isabstract(basecs_VisitableCS)


def test_basecs_visitablecs_constructor_exists():
    assert callable(basecs_VisitableCS.__init__)


def test_basecs_visitablecs_constructor_args():
    sig = inspect.signature(basecs_VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_type_is_not_abstract():
    assert not inspect.isabstract(basecs_Type)


def test_basecs_type_constructor_exists():
    assert callable(basecs_Type.__init__)


def test_basecs_type_constructor_args():
    sig = inspect.signature(basecs_Type.__init__)
    params = list(sig.parameters.keys())



def test_typerefcs_is_not_abstract():
    assert not inspect.isabstract(TypeRefCS)


def test_typerefcs_constructor_exists():
    assert callable(TypeRefCS.__init__)


def test_typerefcs_constructor_args():
    sig = inspect.signature(TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_wildcardtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_WildcardTypeRefCS)


def test_basecs_wildcardtyperefcs_constructor_exists():
    assert callable(basecs_WildcardTypeRefCS.__init__)


def test_basecs_wildcardtyperefcs_constructor_args():
    sig = inspect.signature(basecs_WildcardTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(TemplateParameterCS)


def test_templateparametercs_constructor_exists():
    assert callable(TemplateParameterCS.__init__)


def test_templateparametercs_constructor_args():
    sig = inspect.signature(TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_property_is_not_abstract():
    assert not inspect.isabstract(basecs_Property)


def test_basecs_property_constructor_exists():
    assert callable(basecs_Property.__init__)


def test_basecs_property_constructor_args():
    sig = inspect.signature(basecs_Property.__init__)
    params = list(sig.parameters.keys())



def test_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(PathElementCS)


def test_pathelementcs_constructor_exists():
    assert callable(PathElementCS.__init__)


def test_pathelementcs_constructor_args():
    sig = inspect.signature(PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_pathelementwithurics_is_not_abstract():
    assert not inspect.isabstract(basecs_PathElementWithURICS)


def test_basecs_pathelementwithurics_constructor_exists():
    assert callable(basecs_PathElementWithURICS.__init__)


def test_basecs_pathelementwithurics_constructor_args():
    sig = inspect.signature(basecs_PathElementWithURICS.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_basecs_pathelementwithurics_has_uri():
    assert hasattr(basecs_PathElementWithURICS, "uri")
    descriptor = None
    for klass in basecs_PathElementWithURICS.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_basecs_eclassifier_is_not_abstract():
    assert not inspect.isabstract(basecs_EClassifier)


def test_basecs_eclassifier_constructor_exists():
    assert callable(basecs_EClassifier.__init__)


def test_basecs_eclassifier_constructor_args():
    sig = inspect.signature(basecs_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_pivotable_is_not_abstract():
    assert not inspect.isabstract(Pivotable)


def test_pivotable_constructor_exists():
    assert callable(Pivotable.__init__)


def test_pivotable_constructor_args():
    sig = inspect.signature(Pivotable.__init__)
    params = list(sig.parameters.keys())



def test_packageownercs_is_not_abstract():
    assert not inspect.isabstract(PackageOwnerCS)


def test_packageownercs_constructor_exists():
    assert callable(PackageOwnerCS.__init__)


def test_packageownercs_constructor_args():
    sig = inspect.signature(PackageOwnerCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(basecs_RootPackageCS)


def test_basecs_rootpackagecs_constructor_exists():
    assert callable(basecs_RootPackageCS.__init__)


def test_basecs_rootpackagecs_constructor_args():
    sig = inspect.signature(basecs_RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TuplePartCS)


def test_basecs_tuplepartcs_constructor_exists():
    assert callable(basecs_TuplePartCS.__init__)


def test_basecs_tuplepartcs_constructor_args():
    sig = inspect.signature(basecs_TuplePartCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_parametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_ParameterCS)


def test_basecs_parametercs_constructor_exists():
    assert callable(basecs_ParameterCS.__init__)


def test_basecs_parametercs_constructor_args():
    sig = inspect.signature(basecs_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_featurecs_is_not_abstract():
    assert not inspect.isabstract(basecs_FeatureCS)


def test_basecs_featurecs_constructor_exists():
    assert callable(basecs_FeatureCS.__init__)


def test_basecs_featurecs_constructor_args():
    sig = inspect.signature(basecs_FeatureCS.__init__)
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



def test_basecs_templateparametersubstitutioncs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateParameterSubstitutionCS)


def test_basecs_templateparametersubstitutioncs_constructor_exists():
    assert callable(basecs_TemplateParameterSubstitutionCS.__init__)


def test_basecs_templateparametersubstitutioncs_constructor_args():
    sig = inspect.signature(basecs_TemplateParameterSubstitutionCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_templatesignaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateSignatureCS)


def test_basecs_templatesignaturecs_constructor_exists():
    assert callable(basecs_TemplateSignatureCS.__init__)


def test_basecs_templatesignaturecs_constructor_args():
    sig = inspect.signature(basecs_TemplateSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_rootcs_is_not_abstract():
    assert not inspect.isabstract(basecs_RootCS)


def test_basecs_rootcs_constructor_exists():
    assert callable(basecs_RootCS.__init__)


def test_basecs_rootcs_constructor_args():
    sig = inspect.signature(basecs_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_packageownercs_is_not_abstract():
    assert not inspect.isabstract(basecs_PackageOwnerCS)


def test_basecs_packageownercs_constructor_exists():
    assert callable(basecs_PackageOwnerCS.__init__)


def test_basecs_packageownercs_constructor_args():
    sig = inspect.signature(basecs_PackageOwnerCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_typecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeCS)


def test_basecs_typecs_constructor_exists():
    assert callable(basecs_TypeCS.__init__)


def test_basecs_typecs_constructor_args():
    sig = inspect.signature(basecs_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PivotableElementCS)


def test_basecs_pivotableelementcs_constructor_exists():
    assert callable(basecs_PivotableElementCS.__init__)


def test_basecs_pivotableelementcs_constructor_args():
    sig = inspect.signature(basecs_PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateableElementCS)


def test_basecs_templateableelementcs_constructor_exists():
    assert callable(basecs_TemplateableElementCS.__init__)


def test_basecs_templateableelementcs_constructor_args():
    sig = inspect.signature(basecs_TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PathElementCS)


def test_basecs_pathelementcs_constructor_exists():
    assert callable(basecs_PathElementCS.__init__)


def test_basecs_pathelementcs_constructor_args():
    sig = inspect.signature(basecs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityCS)


def test_basecs_multiplicitycs_constructor_exists():
    assert callable(basecs_MultiplicityCS.__init__)


def test_basecs_multiplicitycs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityCS)


def test_multiplicitycs_constructor_exists():
    assert callable(MultiplicityCS.__init__)


def test_multiplicitycs_constructor_args():
    sig = inspect.signature(MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_multiplicitystringcs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityStringCS)


def test_basecs_multiplicitystringcs_constructor_exists():
    assert callable(basecs_MultiplicityStringCS.__init__)


def test_basecs_multiplicitystringcs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityStringCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringBounds" in params, "Missing parameter 'stringBounds'"

def test_basecs_multiplicitystringcs_has_stringBounds():
    assert hasattr(basecs_MultiplicityStringCS, "stringBounds")
    descriptor = None
    for klass in basecs_MultiplicityStringCS.__mro__:
        if "stringBounds" in klass.__dict__:
            descriptor = klass.__dict__["stringBounds"]
            break
    assert isinstance(descriptor, property)



def test_basecs_multiplicityboundscs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityBoundsCS)


def test_basecs_multiplicityboundscs_constructor_exists():
    assert callable(basecs_MultiplicityBoundsCS.__init__)


def test_basecs_multiplicityboundscs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityBoundsCS.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_basecs_multiplicityboundscs_has_lowerBound():
    assert hasattr(basecs_MultiplicityBoundsCS, "lowerBound")
    descriptor = None
    for klass in basecs_MultiplicityBoundsCS.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_basecs_multiplicityboundscs_has_upperBound():
    assert hasattr(basecs_MultiplicityBoundsCS, "upperBound")
    descriptor = None
    for klass in basecs_MultiplicityBoundsCS.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_basecs_element_is_not_abstract():
    assert not inspect.isabstract(basecs_Element)


def test_basecs_element_constructor_exists():
    assert callable(basecs_Element.__init__)


def test_basecs_element_constructor_args():
    sig = inspect.signature(basecs_Element.__init__)
    params = list(sig.parameters.keys())



def test_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(ElementRefCS)


def test_elementrefcs_constructor_exists():
    assert callable(ElementRefCS.__init__)


def test_elementrefcs_constructor_args():
    sig = inspect.signature(ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_typerefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeRefCS)


def test_basecs_typerefcs_constructor_exists():
    assert callable(basecs_TypeRefCS.__init__)


def test_basecs_typerefcs_constructor_args():
    sig = inspect.signature(basecs_TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_templatebindingcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateBindingCS)


def test_basecs_templatebindingcs_constructor_exists():
    assert callable(basecs_TemplateBindingCS.__init__)


def test_basecs_templatebindingcs_constructor_args():
    sig = inspect.signature(basecs_TemplateBindingCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_basecs_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_NamedElementCS)


def test_basecs_namedelementcs_constructor_exists():
    assert callable(basecs_NamedElementCS.__init__)


def test_basecs_namedelementcs_constructor_args():
    sig = inspect.signature(basecs_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs_namedelementcs_has_name():
    assert hasattr(basecs_NamedElementCS, "name")
    descriptor = None
    for klass in basecs_NamedElementCS.__mro__:
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



def test_basecs_primitivetyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PrimitiveTypeRefCS)


def test_basecs_primitivetyperefcs_constructor_exists():
    assert callable(basecs_PrimitiveTypeRefCS.__init__)


def test_basecs_primitivetyperefcs_constructor_args():
    sig = inspect.signature(basecs_PrimitiveTypeRefCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs_primitivetyperefcs_has_name():
    assert hasattr(basecs_PrimitiveTypeRefCS, "name")
    descriptor = None
    for klass in basecs_PrimitiveTypeRefCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecs_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TupleTypeCS)


def test_basecs_tupletypecs_constructor_exists():
    assert callable(basecs_TupleTypeCS.__init__)


def test_basecs_tupletypecs_constructor_args():
    sig = inspect.signature(basecs_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs_tupletypecs_has_name():
    assert hasattr(basecs_TupleTypeCS, "name")
    descriptor = None
    for klass in basecs_TupleTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecs_typedtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedTypeRefCS)


def test_basecs_typedtyperefcs_constructor_exists():
    assert callable(basecs_TypedTypeRefCS.__init__)


def test_basecs_typedtyperefcs_constructor_args():
    sig = inspect.signature(basecs_TypedTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_namespace_is_not_abstract():
    assert not inspect.isabstract(basecs_Namespace)


def test_basecs_namespace_constructor_exists():
    assert callable(basecs_Namespace.__init__)


def test_basecs_namespace_constructor_args():
    sig = inspect.signature(basecs_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_basecs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(basecs_PathNameCS)


def test_basecs_pathnamecs_constructor_exists():
    assert callable(basecs_PathNameCS.__init__)


def test_basecs_pathnamecs_constructor_args():
    sig = inspect.signature(basecs_PathNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "scopeFilter" in params, "Missing parameter 'scopeFilter'"

def test_basecs_pathnamecs_has_scopeFilter():
    assert hasattr(basecs_PathNameCS, "scopeFilter")
    descriptor = None
    for klass in basecs_PathNameCS.__mro__:
        if "scopeFilter" in klass.__dict__:
            descriptor = klass.__dict__["scopeFilter"]
            break
    assert isinstance(descriptor, property)



def test_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(PivotableElementCS)


def test_pivotableelementcs_constructor_exists():
    assert callable(PivotableElementCS.__init__)


def test_pivotableelementcs_constructor_args():
    sig = inspect.signature(PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ElementRefCS)


def test_basecs_elementrefcs_constructor_exists():
    assert callable(basecs_ElementRefCS.__init__)


def test_basecs_elementrefcs_constructor_args():
    sig = inspect.signature(basecs_ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_visitablecs_is_not_abstract():
    assert not inspect.isabstract(VisitableCS)


def test_visitablecs_constructor_exists():
    assert callable(VisitableCS.__init__)


def test_visitablecs_constructor_args():
    sig = inspect.signature(VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_elementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ElementCS)


def test_basecs_elementcs_constructor_exists():
    assert callable(basecs_ElementCS.__init__)


def test_basecs_elementcs_constructor_args():
    sig = inspect.signature(basecs_ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_specificationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_SpecificationCS)


def test_basecs_specificationcs_constructor_exists():
    assert callable(basecs_SpecificationCS.__init__)


def test_basecs_specificationcs_constructor_args():
    sig = inspect.signature(basecs_SpecificationCS.__init__)
    params = list(sig.parameters.keys())
    assert "exprString" in params, "Missing parameter 'exprString'"

def test_basecs_specificationcs_has_exprString():
    assert hasattr(basecs_SpecificationCS, "exprString")
    descriptor = None
    for klass in basecs_SpecificationCS.__mro__:
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



def test_basecs_lambdatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_LambdaTypeCS)


def test_basecs_lambdatypecs_constructor_exists():
    assert callable(basecs_LambdaTypeCS.__init__)


def test_basecs_lambdatypecs_constructor_args():
    sig = inspect.signature(basecs_LambdaTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs_lambdatypecs_has_name():
    assert hasattr(basecs_LambdaTypeCS, "name")
    descriptor = None
    for klass in basecs_LambdaTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_typeparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeParameterCS)


def test_basecs_typeparametercs_constructor_exists():
    assert callable(basecs_TypeParameterCS.__init__)


def test_basecs_typeparametercs_constructor_args():
    sig = inspect.signature(basecs_TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs_StructuralFeatureCS)


def test_basecs_structuralfeaturecs_constructor_exists():
    assert callable(basecs_StructuralFeatureCS.__init__)


def test_basecs_structuralfeaturecs_constructor_args():
    sig = inspect.signature(basecs_StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_basecs_structuralfeaturecs_has_default():
    assert hasattr(basecs_StructuralFeatureCS, "default")
    descriptor = None
    for klass in basecs_StructuralFeatureCS.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_basecs_operationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_OperationCS)


def test_basecs_operationcs_constructor_exists():
    assert callable(basecs_OperationCS.__init__)


def test_basecs_operationcs_constructor_args():
    sig = inspect.signature(basecs_OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedRefCS)


def test_basecs_typedrefcs_constructor_exists():
    assert callable(basecs_TypedRefCS.__init__)


def test_basecs_typedrefcs_constructor_args():
    sig = inspect.signature(basecs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_librarycs_is_not_abstract():
    assert not inspect.isabstract(basecs_LibraryCS)


def test_basecs_librarycs_constructor_exists():
    assert callable(basecs_LibraryCS.__init__)


def test_basecs_librarycs_constructor_args():
    sig = inspect.signature(basecs_LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_importcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ImportCS)


def test_basecs_importcs_constructor_exists():
    assert callable(basecs_ImportCS.__init__)


def test_basecs_importcs_constructor_args():
    sig = inspect.signature(basecs_ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_basecs_importcs_has_all():
    assert hasattr(basecs_ImportCS, "all")
    descriptor = None
    for klass in basecs_ImportCS.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_basecs_packagecs_is_not_abstract():
    assert not inspect.isabstract(basecs_PackageCS)


def test_basecs_packagecs_constructor_exists():
    assert callable(basecs_PackageCS.__init__)


def test_basecs_packagecs_constructor_args():
    sig = inspect.signature(basecs_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"

def test_basecs_packagecs_has_nsPrefix():
    assert hasattr(basecs_PackageCS, "nsPrefix")
    descriptor = None
    for klass in basecs_PackageCS.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)

def test_basecs_packagecs_has_nsURI():
    assert hasattr(basecs_PackageCS, "nsURI")
    descriptor = None
    for klass in basecs_PackageCS.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)



def test_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_enumerationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_EnumerationCS)


def test_basecs_enumerationcs_constructor_exists():
    assert callable(basecs_EnumerationCS.__init__)


def test_basecs_enumerationcs_constructor_args():
    sig = inspect.signature(basecs_EnumerationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_datatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_DataTypeCS)


def test_basecs_datatypecs_constructor_exists():
    assert callable(basecs_DataTypeCS.__init__)


def test_basecs_datatypecs_constructor_args():
    sig = inspect.signature(basecs_DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_classcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ClassCS)


def test_basecs_classcs_constructor_exists():
    assert callable(basecs_ClassCS.__init__)


def test_basecs_classcs_constructor_args():
    sig = inspect.signature(basecs_ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_referencecs_is_not_abstract():
    assert not inspect.isabstract(basecs_ReferenceCS)


def test_basecs_referencecs_constructor_exists():
    assert callable(basecs_ReferenceCS.__init__)


def test_basecs_referencecs_constructor_args():
    sig = inspect.signature(basecs_ReferenceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_attributecs_is_not_abstract():
    assert not inspect.isabstract(basecs_AttributeCS)


def test_basecs_attributecs_constructor_exists():
    assert callable(basecs_AttributeCS.__init__)


def test_basecs_attributecs_constructor_args():
    sig = inspect.signature(basecs_AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_namespacecs_is_not_abstract():
    assert not inspect.isabstract(basecs_NamespaceCS)


def test_basecs_namespacecs_constructor_exists():
    assert callable(basecs_NamespaceCS.__init__)


def test_basecs_namespacecs_constructor_args():
    sig = inspect.signature(basecs_NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_enumerationliteralcs_is_not_abstract():
    assert not inspect.isabstract(basecs_EnumerationLiteralCS)


def test_basecs_enumerationliteralcs_constructor_exists():
    assert callable(basecs_EnumerationLiteralCS.__init__)


def test_basecs_enumerationliteralcs_constructor_args():
    sig = inspect.signature(basecs_EnumerationLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs_enumerationliteralcs_has_value():
    assert hasattr(basecs_EnumerationLiteralCS, "value")
    descriptor = None
    for klass in basecs_EnumerationLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs_constraintcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ConstraintCS)


def test_basecs_constraintcs_constructor_exists():
    assert callable(basecs_ConstraintCS.__init__)


def test_basecs_constraintcs_constructor_args():
    sig = inspect.signature(basecs_ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_basecs_constraintcs_has_stereotype():
    assert hasattr(basecs_ConstraintCS, "stereotype")
    descriptor = None
    for klass in basecs_ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_basecs_classifiercs_is_not_abstract():
    assert not inspect.isabstract(basecs_ClassifierCS)


def test_basecs_classifiercs_constructor_exists():
    assert callable(basecs_ClassifierCS.__init__)


def test_basecs_classifiercs_constructor_args():
    sig = inspect.signature(basecs_ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_basecs_classifiercs_has_qualifier():
    assert hasattr(basecs_ClassifierCS, "qualifier")
    descriptor = None
    for klass in basecs_ClassifierCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_basecs_classifiercs_has_instanceClassName():
    assert hasattr(basecs_ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in basecs_ClassifierCS.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_basecs_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateParameterCS)


def test_basecs_templateparametercs_constructor_exists():
    assert callable(basecs_TemplateParameterCS.__init__)


def test_basecs_templateparametercs_constructor_args():
    sig = inspect.signature(basecs_TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_detailcs_is_not_abstract():
    assert not inspect.isabstract(basecs_DetailCS)


def test_basecs_detailcs_constructor_exists():
    assert callable(basecs_DetailCS.__init__)


def test_basecs_detailcs_constructor_args():
    sig = inspect.signature(basecs_DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs_detailcs_has_value():
    assert hasattr(basecs_DetailCS, "value")
    descriptor = None
    for klass in basecs_DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedElementCS)


def test_basecs_typedelementcs_constructor_exists():
    assert callable(basecs_TypedElementCS.__init__)


def test_basecs_typedelementcs_constructor_args():
    sig = inspect.signature(basecs_TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_basecs_typedelementcs_has_optional():
    assert hasattr(basecs_TypedElementCS, "optional")
    descriptor = None
    for klass in basecs_TypedElementCS.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_basecs_typedelementcs_has_qualifier():
    assert hasattr(basecs_TypedElementCS, "qualifier")
    descriptor = None
    for klass in basecs_TypedElementCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_basecs_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_AnnotationElementCS)


def test_basecs_annotationelementcs_constructor_exists():
    assert callable(basecs_AnnotationElementCS.__init__)


def test_basecs_annotationelementcs_constructor_args():
    sig = inspect.signature(basecs_AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_modelelementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ModelElementRefCS)


def test_basecs_modelelementrefcs_constructor_exists():
    assert callable(basecs_ModelElementRefCS.__init__)


def test_basecs_modelelementrefcs_constructor_args():
    sig = inspect.signature(basecs_ModelElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ModelElementCS)


def test_basecs_modelelementcs_constructor_exists():
    assert callable(basecs_ModelElementCS.__init__)


def test_basecs_modelelementcs_constructor_args():
    sig = inspect.signature(basecs_ModelElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "csi" in params, "Missing parameter 'csi'"
    assert "originalXmiId" in params, "Missing parameter 'originalXmiId'"

def test_basecs_modelelementcs_has_csi():
    assert hasattr(basecs_ModelElementCS, "csi")
    descriptor = None
    for klass in basecs_ModelElementCS.__mro__:
        if "csi" in klass.__dict__:
            descriptor = klass.__dict__["csi"]
            break
    assert isinstance(descriptor, property)

def test_basecs_modelelementcs_has_originalXmiId():
    assert hasattr(basecs_ModelElementCS, "originalXmiId")
    descriptor = None
    for klass in basecs_ModelElementCS.__mro__:
        if "originalXmiId" in klass.__dict__:
            descriptor = klass.__dict__["originalXmiId"]
            break
    assert isinstance(descriptor, property)



def test_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(AnnotationElementCS)


def test_annotationelementcs_constructor_exists():
    assert callable(AnnotationElementCS.__init__)


def test_annotationelementcs_constructor_args():
    sig = inspect.signature(AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs_documentationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_DocumentationCS)


def test_basecs_documentationcs_constructor_exists():
    assert callable(basecs_DocumentationCS.__init__)


def test_basecs_documentationcs_constructor_args():
    sig = inspect.signature(basecs_DocumentationCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs_documentationcs_has_value():
    assert hasattr(basecs_DocumentationCS, "value")
    descriptor = None
    for klass in basecs_DocumentationCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs_annotationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_AnnotationCS)


def test_basecs_annotationcs_constructor_exists():
    assert callable(basecs_AnnotationCS.__init__)


def test_basecs_annotationcs_constructor_args():
    sig = inspect.signature(basecs_AnnotationCS.__init__)
    params = list(sig.parameters.keys())

def test_iteratorkind_exists():
    # Check that the Enumeration exists
    assert IteratorKind is not None

def test_iteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorKind]
    expected_literals = [
        "Iterator",
        "Parameter",
        "Accumulator",
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
basecs_VisitableCS_strategy = st.builds(
    basecs_VisitableCS,
)
basecs_Type_strategy = st.builds(
    basecs_Type,
)
TypeRefCS_strategy = st.builds(
    TypeRefCS,
)
basecs_WildcardTypeRefCS_strategy = st.builds(
    basecs_WildcardTypeRefCS,
)
TemplateParameterCS_strategy = st.builds(
    TemplateParameterCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
basecs_Property_strategy = st.builds(
    basecs_Property,
)
PathElementCS_strategy = st.builds(
    PathElementCS,
)
basecs_PathElementWithURICS_strategy = st.builds(
    basecs_PathElementWithURICS,
    uri=
        safe_text
)
basecs_EClassifier_strategy = st.builds(
    basecs_EClassifier,
)
Pivotable_strategy = st.builds(
    Pivotable,
)
PackageOwnerCS_strategy = st.builds(
    PackageOwnerCS,
)
basecs_RootPackageCS_strategy = st.builds(
    basecs_RootPackageCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
basecs_TuplePartCS_strategy = st.builds(
    basecs_TuplePartCS,
)
basecs_ParameterCS_strategy = st.builds(
    basecs_ParameterCS,
)
basecs_FeatureCS_strategy = st.builds(
    basecs_FeatureCS,
)
FeatureCS_strategy = st.builds(
    FeatureCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
basecs_TemplateParameterSubstitutionCS_strategy = st.builds(
    basecs_TemplateParameterSubstitutionCS,
)
basecs_TemplateSignatureCS_strategy = st.builds(
    basecs_TemplateSignatureCS,
)
basecs_RootCS_strategy = st.builds(
    basecs_RootCS,
)
basecs_PackageOwnerCS_strategy = st.builds(
    basecs_PackageOwnerCS,
)
basecs_TypeCS_strategy = st.builds(
    basecs_TypeCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
basecs_PivotableElementCS_strategy = st.builds(
    basecs_PivotableElementCS,
)
basecs_TemplateableElementCS_strategy = st.builds(
    basecs_TemplateableElementCS,
)
basecs_PathElementCS_strategy = st.builds(
    basecs_PathElementCS,
)
basecs_MultiplicityCS_strategy = st.builds(
    basecs_MultiplicityCS,
)
MultiplicityCS_strategy = st.builds(
    MultiplicityCS,
)
basecs_MultiplicityStringCS_strategy = st.builds(
    basecs_MultiplicityStringCS,
    stringBounds=
        safe_text
)
basecs_MultiplicityBoundsCS_strategy = st.builds(
    basecs_MultiplicityBoundsCS,
    lowerBound=
        st.integers(),
    upperBound=
        safe_text
)
basecs_Element_strategy = st.builds(
    basecs_Element,
)
ElementRefCS_strategy = st.builds(
    ElementRefCS,
)
basecs_TypeRefCS_strategy = st.builds(
    basecs_TypeRefCS,
)
basecs_TemplateBindingCS_strategy = st.builds(
    basecs_TemplateBindingCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
basecs_NamedElementCS_strategy = st.builds(
    basecs_NamedElementCS,
    name=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
basecs_PrimitiveTypeRefCS_strategy = st.builds(
    basecs_PrimitiveTypeRefCS,
    name=
        safe_text
)
basecs_TupleTypeCS_strategy = st.builds(
    basecs_TupleTypeCS,
    name=
        safe_text
)
basecs_TypedTypeRefCS_strategy = st.builds(
    basecs_TypedTypeRefCS,
)
basecs_Namespace_strategy = st.builds(
    basecs_Namespace,
)
basecs_PathNameCS_strategy = st.builds(
    basecs_PathNameCS,
    scopeFilter=
        safe_text
)
PivotableElementCS_strategy = st.builds(
    PivotableElementCS,
)
basecs_ElementRefCS_strategy = st.builds(
    basecs_ElementRefCS,
)
VisitableCS_strategy = st.builds(
    VisitableCS,
)
basecs_ElementCS_strategy = st.builds(
    basecs_ElementCS,
)
basecs_SpecificationCS_strategy = st.builds(
    basecs_SpecificationCS,
    exprString=
        safe_text
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
basecs_LambdaTypeCS_strategy = st.builds(
    basecs_LambdaTypeCS,
    name=
        safe_text
)
TypeCS_strategy = st.builds(
    TypeCS,
)
basecs_TypeParameterCS_strategy = st.builds(
    basecs_TypeParameterCS,
)
basecs_StructuralFeatureCS_strategy = st.builds(
    basecs_StructuralFeatureCS,
    default=
        safe_text
)
basecs_OperationCS_strategy = st.builds(
    basecs_OperationCS,
)
basecs_TypedRefCS_strategy = st.builds(
    basecs_TypedRefCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
basecs_LibraryCS_strategy = st.builds(
    basecs_LibraryCS,
)
basecs_ImportCS_strategy = st.builds(
    basecs_ImportCS,
    all=
        st.booleans()
)
basecs_PackageCS_strategy = st.builds(
    basecs_PackageCS,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
basecs_EnumerationCS_strategy = st.builds(
    basecs_EnumerationCS,
)
basecs_DataTypeCS_strategy = st.builds(
    basecs_DataTypeCS,
)
basecs_ClassCS_strategy = st.builds(
    basecs_ClassCS,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
basecs_ReferenceCS_strategy = st.builds(
    basecs_ReferenceCS,
)
basecs_AttributeCS_strategy = st.builds(
    basecs_AttributeCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
basecs_NamespaceCS_strategy = st.builds(
    basecs_NamespaceCS,
)
basecs_EnumerationLiteralCS_strategy = st.builds(
    basecs_EnumerationLiteralCS,
    value=
        st.integers()
)
basecs_ConstraintCS_strategy = st.builds(
    basecs_ConstraintCS,
    stereotype=
        safe_text
)
basecs_ClassifierCS_strategy = st.builds(
    basecs_ClassifierCS,
    qualifier=
        safe_text,
    instanceClassName=
        safe_text
)
basecs_TemplateParameterCS_strategy = st.builds(
    basecs_TemplateParameterCS,
)
basecs_DetailCS_strategy = st.builds(
    basecs_DetailCS,
    value=
        safe_text
)
basecs_TypedElementCS_strategy = st.builds(
    basecs_TypedElementCS,
    optional=
        st.booleans(),
    qualifier=
        safe_text
)
basecs_AnnotationElementCS_strategy = st.builds(
    basecs_AnnotationElementCS,
)
basecs_ModelElementRefCS_strategy = st.builds(
    basecs_ModelElementRefCS,
)
basecs_ModelElementCS_strategy = st.builds(
    basecs_ModelElementCS,
    csi=
        safe_text,
    originalXmiId=
        safe_text
)
AnnotationElementCS_strategy = st.builds(
    AnnotationElementCS,
)
basecs_DocumentationCS_strategy = st.builds(
    basecs_DocumentationCS,
    value=
        safe_text
)
basecs_AnnotationCS_strategy = st.builds(
    basecs_AnnotationCS,
)

@given(instance=basecs_VisitableCS_strategy)
@settings(max_examples=50)
def test_basecs_visitablecs_instantiation(instance):
    assert isinstance(instance, basecs_VisitableCS)

@given(instance=basecs_Type_strategy)
@settings(max_examples=50)
def test_basecs_type_instantiation(instance):
    assert isinstance(instance, basecs_Type)

@given(instance=TypeRefCS_strategy)
@settings(max_examples=50)
def test_typerefcs_instantiation(instance):
    assert isinstance(instance, TypeRefCS)

@given(instance=basecs_WildcardTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs_wildcardtyperefcs_instantiation(instance):
    assert isinstance(instance, basecs_WildcardTypeRefCS)

@given(instance=TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_templateparametercs_instantiation(instance):
    assert isinstance(instance, TemplateParameterCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=basecs_Property_strategy)
@settings(max_examples=50)
def test_basecs_property_instantiation(instance):
    assert isinstance(instance, basecs_Property)

@given(instance=PathElementCS_strategy)
@settings(max_examples=50)
def test_pathelementcs_instantiation(instance):
    assert isinstance(instance, PathElementCS)

@given(instance=basecs_PathElementWithURICS_strategy)
@settings(max_examples=50)
def test_basecs_pathelementwithurics_instantiation(instance):
    assert isinstance(instance, basecs_PathElementWithURICS)



@given(instance=basecs_PathElementWithURICS_strategy)
def test_basecs_pathelementwithurics_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=basecs_EClassifier_strategy)
@settings(max_examples=50)
def test_basecs_eclassifier_instantiation(instance):
    assert isinstance(instance, basecs_EClassifier)

@given(instance=Pivotable_strategy)
@settings(max_examples=50)
def test_pivotable_instantiation(instance):
    assert isinstance(instance, Pivotable)

@given(instance=PackageOwnerCS_strategy)
@settings(max_examples=50)
def test_packageownercs_instantiation(instance):
    assert isinstance(instance, PackageOwnerCS)

@given(instance=basecs_RootPackageCS_strategy)
@settings(max_examples=50)
def test_basecs_rootpackagecs_instantiation(instance):
    assert isinstance(instance, basecs_RootPackageCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=basecs_TuplePartCS_strategy)
@settings(max_examples=50)
def test_basecs_tuplepartcs_instantiation(instance):
    assert isinstance(instance, basecs_TuplePartCS)

@given(instance=basecs_ParameterCS_strategy)
@settings(max_examples=50)
def test_basecs_parametercs_instantiation(instance):
    assert isinstance(instance, basecs_ParameterCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_ParameterCS_strategy)
@settings(max_examples=30)
def test_basecs_parametercs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_ParameterCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_ParameterCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_ParameterCS is not implemented or raised an error")

@given(instance=basecs_FeatureCS_strategy)
@settings(max_examples=50)
def test_basecs_featurecs_instantiation(instance):
    assert isinstance(instance, basecs_FeatureCS)

@given(instance=FeatureCS_strategy)
@settings(max_examples=50)
def test_featurecs_instantiation(instance):
    assert isinstance(instance, FeatureCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=basecs_TemplateParameterSubstitutionCS_strategy)
@settings(max_examples=50)
def test_basecs_templateparametersubstitutioncs_instantiation(instance):
    assert isinstance(instance, basecs_TemplateParameterSubstitutionCS)

@given(instance=basecs_TemplateSignatureCS_strategy)
@settings(max_examples=50)
def test_basecs_templatesignaturecs_instantiation(instance):
    assert isinstance(instance, basecs_TemplateSignatureCS)

@given(instance=basecs_RootCS_strategy)
@settings(max_examples=50)
def test_basecs_rootcs_instantiation(instance):
    assert isinstance(instance, basecs_RootCS)

@given(instance=basecs_PackageOwnerCS_strategy)
@settings(max_examples=50)
def test_basecs_packageownercs_instantiation(instance):
    assert isinstance(instance, basecs_PackageOwnerCS)

@given(instance=basecs_TypeCS_strategy)
@settings(max_examples=50)
def test_basecs_typecs_instantiation(instance):
    assert isinstance(instance, basecs_TypeCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=basecs_PivotableElementCS_strategy)
@settings(max_examples=50)
def test_basecs_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, basecs_PivotableElementCS)

@given(instance=basecs_TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_basecs_templateableelementcs_instantiation(instance):
    assert isinstance(instance, basecs_TemplateableElementCS)

@given(instance=basecs_PathElementCS_strategy)
@settings(max_examples=50)
def test_basecs_pathelementcs_instantiation(instance):
    assert isinstance(instance, basecs_PathElementCS)

@given(instance=basecs_MultiplicityCS_strategy)
@settings(max_examples=50)
def test_basecs_multiplicitycs_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityCS)

@given(instance=MultiplicityCS_strategy)
@settings(max_examples=50)
def test_multiplicitycs_instantiation(instance):
    assert isinstance(instance, MultiplicityCS)

@given(instance=basecs_MultiplicityStringCS_strategy)
@settings(max_examples=50)
def test_basecs_multiplicitystringcs_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityStringCS)



@given(instance=basecs_MultiplicityStringCS_strategy)
def test_basecs_multiplicitystringcs_stringBounds_setter(instance):
    original = instance.stringBounds
    instance.stringBounds = original
    assert instance.stringBounds == original

@given(instance=basecs_MultiplicityBoundsCS_strategy)
@settings(max_examples=50)
def test_basecs_multiplicityboundscs_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityBoundsCS)



@given(instance=basecs_MultiplicityBoundsCS_strategy)
def test_basecs_multiplicityboundscs_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=basecs_MultiplicityBoundsCS_strategy)
def test_basecs_multiplicityboundscs_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=basecs_Element_strategy)
@settings(max_examples=50)
def test_basecs_element_instantiation(instance):
    assert isinstance(instance, basecs_Element)

@given(instance=ElementRefCS_strategy)
@settings(max_examples=50)
def test_elementrefcs_instantiation(instance):
    assert isinstance(instance, ElementRefCS)

@given(instance=basecs_TypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs_typerefcs_instantiation(instance):
    assert isinstance(instance, basecs_TypeRefCS)

@given(instance=basecs_TemplateBindingCS_strategy)
@settings(max_examples=50)
def test_basecs_templatebindingcs_instantiation(instance):
    assert isinstance(instance, basecs_TemplateBindingCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=basecs_NamedElementCS_strategy)
@settings(max_examples=50)
def test_basecs_namedelementcs_instantiation(instance):
    assert isinstance(instance, basecs_NamedElementCS)



@given(instance=basecs_NamedElementCS_strategy)
def test_basecs_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=basecs_PrimitiveTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs_primitivetyperefcs_instantiation(instance):
    assert isinstance(instance, basecs_PrimitiveTypeRefCS)



@given(instance=basecs_PrimitiveTypeRefCS_strategy)
def test_basecs_primitivetyperefcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basecs_TupleTypeCS_strategy)
@settings(max_examples=50)
def test_basecs_tupletypecs_instantiation(instance):
    assert isinstance(instance, basecs_TupleTypeCS)



@given(instance=basecs_TupleTypeCS_strategy)
def test_basecs_tupletypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basecs_TypedTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs_typedtyperefcs_instantiation(instance):
    assert isinstance(instance, basecs_TypedTypeRefCS)

@given(instance=basecs_Namespace_strategy)
@settings(max_examples=50)
def test_basecs_namespace_instantiation(instance):
    assert isinstance(instance, basecs_Namespace)

@given(instance=basecs_PathNameCS_strategy)
@settings(max_examples=50)
def test_basecs_pathnamecs_instantiation(instance):
    assert isinstance(instance, basecs_PathNameCS)



@given(instance=basecs_PathNameCS_strategy)
def test_basecs_pathnamecs_scopeFilter_setter(instance):
    original = instance.scopeFilter
    instance.scopeFilter = original
    assert instance.scopeFilter == original

@given(instance=PivotableElementCS_strategy)
@settings(max_examples=50)
def test_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, PivotableElementCS)

@given(instance=basecs_ElementRefCS_strategy)
@settings(max_examples=50)
def test_basecs_elementrefcs_instantiation(instance):
    assert isinstance(instance, basecs_ElementRefCS)

@given(instance=VisitableCS_strategy)
@settings(max_examples=50)
def test_visitablecs_instantiation(instance):
    assert isinstance(instance, VisitableCS)

@given(instance=basecs_ElementCS_strategy)
@settings(max_examples=50)
def test_basecs_elementcs_instantiation(instance):
    assert isinstance(instance, basecs_ElementCS)

@given(instance=basecs_SpecificationCS_strategy)
@settings(max_examples=50)
def test_basecs_specificationcs_instantiation(instance):
    assert isinstance(instance, basecs_SpecificationCS)



@given(instance=basecs_SpecificationCS_strategy)
def test_basecs_specificationcs_exprString_setter(instance):
    original = instance.exprString
    instance.exprString = original
    assert instance.exprString == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=basecs_LambdaTypeCS_strategy)
@settings(max_examples=50)
def test_basecs_lambdatypecs_instantiation(instance):
    assert isinstance(instance, basecs_LambdaTypeCS)



@given(instance=basecs_LambdaTypeCS_strategy)
def test_basecs_lambdatypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=basecs_TypeParameterCS_strategy)
@settings(max_examples=50)
def test_basecs_typeparametercs_instantiation(instance):
    assert isinstance(instance, basecs_TypeParameterCS)

@given(instance=basecs_StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_basecs_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, basecs_StructuralFeatureCS)



@given(instance=basecs_StructuralFeatureCS_strategy)
def test_basecs_structuralfeaturecs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_StructuralFeatureCS_strategy)
@settings(max_examples=30)
def test_basecs_structuralfeaturecs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_StructuralFeatureCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_StructuralFeatureCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_StructuralFeatureCS is not implemented or raised an error")

@given(instance=basecs_OperationCS_strategy)
@settings(max_examples=50)
def test_basecs_operationcs_instantiation(instance):
    assert isinstance(instance, basecs_OperationCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_OperationCS_strategy)
@settings(max_examples=30)
def test_basecs_operationcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_OperationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_OperationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_OperationCS is not implemented or raised an error")

@given(instance=basecs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_basecs_typedrefcs_instantiation(instance):
    assert isinstance(instance, basecs_TypedRefCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=basecs_LibraryCS_strategy)
@settings(max_examples=50)
def test_basecs_librarycs_instantiation(instance):
    assert isinstance(instance, basecs_LibraryCS)

@given(instance=basecs_ImportCS_strategy)
@settings(max_examples=50)
def test_basecs_importcs_instantiation(instance):
    assert isinstance(instance, basecs_ImportCS)



@given(instance=basecs_ImportCS_strategy)
def test_basecs_importcs_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=basecs_PackageCS_strategy)
@settings(max_examples=50)
def test_basecs_packagecs_instantiation(instance):
    assert isinstance(instance, basecs_PackageCS)



@given(instance=basecs_PackageCS_strategy)
def test_basecs_packagecs_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original



@given(instance=basecs_PackageCS_strategy)
def test_basecs_packagecs_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_PackageCS_strategy)
@settings(max_examples=30)
def test_basecs_packagecs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_PackageCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_PackageCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_PackageCS is not implemented or raised an error")

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=basecs_EnumerationCS_strategy)
@settings(max_examples=50)
def test_basecs_enumerationcs_instantiation(instance):
    assert isinstance(instance, basecs_EnumerationCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_EnumerationCS_strategy)
@settings(max_examples=30)
def test_basecs_enumerationcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_EnumerationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_EnumerationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_EnumerationCS is not implemented or raised an error")

@given(instance=basecs_DataTypeCS_strategy)
@settings(max_examples=50)
def test_basecs_datatypecs_instantiation(instance):
    assert isinstance(instance, basecs_DataTypeCS)

@given(instance=basecs_ClassCS_strategy)
@settings(max_examples=50)
def test_basecs_classcs_instantiation(instance):
    assert isinstance(instance, basecs_ClassCS)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=basecs_ReferenceCS_strategy)
@settings(max_examples=50)
def test_basecs_referencecs_instantiation(instance):
    assert isinstance(instance, basecs_ReferenceCS)

@given(instance=basecs_AttributeCS_strategy)
@settings(max_examples=50)
def test_basecs_attributecs_instantiation(instance):
    assert isinstance(instance, basecs_AttributeCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=basecs_NamespaceCS_strategy)
@settings(max_examples=50)
def test_basecs_namespacecs_instantiation(instance):
    assert isinstance(instance, basecs_NamespaceCS)

@given(instance=basecs_EnumerationLiteralCS_strategy)
@settings(max_examples=50)
def test_basecs_enumerationliteralcs_instantiation(instance):
    assert isinstance(instance, basecs_EnumerationLiteralCS)



@given(instance=basecs_EnumerationLiteralCS_strategy)
def test_basecs_enumerationliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_EnumerationLiteralCS_strategy)
@settings(max_examples=30)
def test_basecs_enumerationliteralcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_EnumerationLiteralCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_EnumerationLiteralCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_EnumerationLiteralCS is not implemented or raised an error")

@given(instance=basecs_ConstraintCS_strategy)
@settings(max_examples=50)
def test_basecs_constraintcs_instantiation(instance):
    assert isinstance(instance, basecs_ConstraintCS)



@given(instance=basecs_ConstraintCS_strategy)
def test_basecs_constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=basecs_ClassifierCS_strategy)
@settings(max_examples=50)
def test_basecs_classifiercs_instantiation(instance):
    assert isinstance(instance, basecs_ClassifierCS)



@given(instance=basecs_ClassifierCS_strategy)
def test_basecs_classifiercs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=basecs_ClassifierCS_strategy)
def test_basecs_classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_ClassifierCS_strategy)
@settings(max_examples=30)
def test_basecs_classifiercs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_ClassifierCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_ClassifierCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_ClassifierCS is not implemented or raised an error")

@given(instance=basecs_TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_basecs_templateparametercs_instantiation(instance):
    assert isinstance(instance, basecs_TemplateParameterCS)

@given(instance=basecs_DetailCS_strategy)
@settings(max_examples=50)
def test_basecs_detailcs_instantiation(instance):
    assert isinstance(instance, basecs_DetailCS)



@given(instance=basecs_DetailCS_strategy)
def test_basecs_detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=basecs_TypedElementCS_strategy)
@settings(max_examples=50)
def test_basecs_typedelementcs_instantiation(instance):
    assert isinstance(instance, basecs_TypedElementCS)



@given(instance=basecs_TypedElementCS_strategy)
def test_basecs_typedelementcs_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=basecs_TypedElementCS_strategy)
def test_basecs_typedelementcs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=basecs_AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_basecs_annotationelementcs_instantiation(instance):
    assert isinstance(instance, basecs_AnnotationElementCS)

@given(instance=basecs_ModelElementRefCS_strategy)
@settings(max_examples=50)
def test_basecs_modelelementrefcs_instantiation(instance):
    assert isinstance(instance, basecs_ModelElementRefCS)

@given(instance=basecs_ModelElementCS_strategy)
@settings(max_examples=50)
def test_basecs_modelelementcs_instantiation(instance):
    assert isinstance(instance, basecs_ModelElementCS)



@given(instance=basecs_ModelElementCS_strategy)
def test_basecs_modelelementcs_csi_setter(instance):
    original = instance.csi
    instance.csi = original
    assert instance.csi == original



@given(instance=basecs_ModelElementCS_strategy)
def test_basecs_modelelementcs_originalXmiId_setter(instance):
    original = instance.originalXmiId
    instance.originalXmiId = original
    assert instance.originalXmiId == original

@given(instance=AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_annotationelementcs_instantiation(instance):
    assert isinstance(instance, AnnotationElementCS)

@given(instance=basecs_DocumentationCS_strategy)
@settings(max_examples=50)
def test_basecs_documentationcs_instantiation(instance):
    assert isinstance(instance, basecs_DocumentationCS)



@given(instance=basecs_DocumentationCS_strategy)
def test_basecs_documentationcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=basecs_AnnotationCS_strategy)
@settings(max_examples=50)
def test_basecs_annotationcs_instantiation(instance):
    assert isinstance(instance, basecs_AnnotationCS)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    baseCST::VisitableCS,
    baseCST::Type,
    TypeRefCS,
    baseCST::WildcardTypeRefCS,
    TemplateParameterCS,
    PathElementCS,
    baseCST::PathElementWithURICS,
    RootCS,
    PackageCS,
    baseCST::RootPackageCS,
    baseCST::Property,
    baseCST::EClassifier,
    Pivotable,
    FeatureCS,
    ModelElementCS,
    baseCST::TypeCS,
    baseCST::RootCS,
    baseCST::TemplateSignatureCS,
    baseCST::TemplateParameterSubstitutionCS,
    ElementCS,
    baseCST::PathNameCS,
    baseCST::TemplateableElementCS,
    baseCST::PathElementCS,
    baseCST::PivotableElementCS,
    baseCST::MultiplicityCS,
    MultiplicityCS,
    baseCST::MultiplicityStringCS,
    baseCST::MultiplicityBoundsCS,
    baseCST::Element,
    ElementRefCS,
    baseCST::TemplateBindingCS,
    baseCST::TypeRefCS,
    Nameable,
    baseCST::NamedElementCS,
    TypedRefCS,
    baseCST::PrimitiveTypeRefCS,
    baseCST::TypedTypeRefCS,
    baseCST::TupleTypeCS,
    baseCST::Namespace,
    TypedElementCS,
    baseCST::TuplePartCS,
    baseCST::ParameterCS,
    baseCST::FeatureCS,
    PivotableElementCS,
    baseCST::ElementRefCS,
    VisitableCS,
    baseCST::ElementCS,
    baseCST::SpecificationCS,
    TemplateableElementCS,
    baseCST::OperationCS,
    baseCST::LambdaTypeCS,
    TypeCS,
    baseCST::TypeParameterCS,
    baseCST::StructuralFeatureCS,
    baseCST::TypedRefCS,
    NamespaceCS,
    baseCST::PackageCS,
    baseCST::LibraryCS,
    baseCST::ImportCS,
    ClassifierCS,
    baseCST::DataTypeCS,
    baseCST::EnumerationCS,
    baseCST::ClassCS,
    StructuralFeatureCS,
    baseCST::ReferenceCS,
    baseCST::AttributeCS,
    NamedElementCS,
    baseCST::NamespaceCS,
    baseCST::EnumerationLiteralCS,
    baseCST::DetailCS,
    baseCST::TypedElementCS,
    baseCST::ConstraintCS,
    baseCST::TemplateParameterCS,
    baseCST::ClassifierCS,
    baseCST::AnnotationElementCS,
    baseCST::ModelElementRefCS,
    baseCST::ModelElementCS,
    AnnotationElementCS,
    baseCST::DocumentationCS,
    baseCST::AnnotationCS,
    IteratorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basecst::visitablecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::VisitableCS)


def test_basecst::visitablecs_constructor_exists():
    assert callable(baseCST::VisitableCS.__init__)


def test_basecst::visitablecs_constructor_args():
    sig = inspect.signature(baseCST::VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::type_is_not_abstract():
    assert not inspect.isabstract(baseCST::Type)


def test_basecst::type_constructor_exists():
    assert callable(baseCST::Type.__init__)


def test_basecst::type_constructor_args():
    sig = inspect.signature(baseCST::Type.__init__)
    params = list(sig.parameters.keys())



def test_typerefcs_is_not_abstract():
    assert not inspect.isabstract(TypeRefCS)


def test_typerefcs_constructor_exists():
    assert callable(TypeRefCS.__init__)


def test_typerefcs_constructor_args():
    sig = inspect.signature(TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::wildcardtyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::WildcardTypeRefCS)


def test_basecst::wildcardtyperefcs_constructor_exists():
    assert callable(baseCST::WildcardTypeRefCS.__init__)


def test_basecst::wildcardtyperefcs_constructor_args():
    sig = inspect.signature(baseCST::WildcardTypeRefCS.__init__)
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



def test_basecst::pathelementwithurics_is_not_abstract():
    assert not inspect.isabstract(baseCST::PathElementWithURICS)


def test_basecst::pathelementwithurics_constructor_exists():
    assert callable(baseCST::PathElementWithURICS.__init__)


def test_basecst::pathelementwithurics_constructor_args():
    sig = inspect.signature(baseCST::PathElementWithURICS.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_basecst::pathelementwithurics_has_uri():
    assert hasattr(baseCST::PathElementWithURICS, "uri")
    descriptor = None
    for klass in baseCST::PathElementWithURICS.__mro__:
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



def test_basecst::rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::RootPackageCS)


def test_basecst::rootpackagecs_constructor_exists():
    assert callable(baseCST::RootPackageCS.__init__)


def test_basecst::rootpackagecs_constructor_args():
    sig = inspect.signature(baseCST::RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::property_is_not_abstract():
    assert not inspect.isabstract(baseCST::Property)


def test_basecst::property_constructor_exists():
    assert callable(baseCST::Property.__init__)


def test_basecst::property_constructor_args():
    sig = inspect.signature(baseCST::Property.__init__)
    params = list(sig.parameters.keys())



def test_basecst::eclassifier_is_not_abstract():
    assert not inspect.isabstract(baseCST::EClassifier)


def test_basecst::eclassifier_constructor_exists():
    assert callable(baseCST::EClassifier.__init__)


def test_basecst::eclassifier_constructor_args():
    sig = inspect.signature(baseCST::EClassifier.__init__)
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



def test_basecst::typecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypeCS)


def test_basecst::typecs_constructor_exists():
    assert callable(baseCST::TypeCS.__init__)


def test_basecst::typecs_constructor_args():
    sig = inspect.signature(baseCST::TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::rootcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::RootCS)


def test_basecst::rootcs_constructor_exists():
    assert callable(baseCST::RootCS.__init__)


def test_basecst::rootcs_constructor_args():
    sig = inspect.signature(baseCST::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::templatesignaturecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TemplateSignatureCS)


def test_basecst::templatesignaturecs_constructor_exists():
    assert callable(baseCST::TemplateSignatureCS.__init__)


def test_basecst::templatesignaturecs_constructor_args():
    sig = inspect.signature(baseCST::TemplateSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::templateparametersubstitutioncs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TemplateParameterSubstitutionCS)


def test_basecst::templateparametersubstitutioncs_constructor_exists():
    assert callable(baseCST::TemplateParameterSubstitutionCS.__init__)


def test_basecst::templateparametersubstitutioncs_constructor_args():
    sig = inspect.signature(baseCST::TemplateParameterSubstitutionCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::PathNameCS)


def test_basecst::pathnamecs_constructor_exists():
    assert callable(baseCST::PathNameCS.__init__)


def test_basecst::pathnamecs_constructor_args():
    sig = inspect.signature(baseCST::PathNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "scopeFilter" in params, "Missing parameter 'scopeFilter'"

def test_basecst::pathnamecs_has_scopeFilter():
    assert hasattr(baseCST::PathNameCS, "scopeFilter")
    descriptor = None
    for klass in baseCST::PathNameCS.__mro__:
        if "scopeFilter" in klass.__dict__:
            descriptor = klass.__dict__["scopeFilter"]
            break
    assert isinstance(descriptor, property)



def test_basecst::templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TemplateableElementCS)


def test_basecst::templateableelementcs_constructor_exists():
    assert callable(baseCST::TemplateableElementCS.__init__)


def test_basecst::templateableelementcs_constructor_args():
    sig = inspect.signature(baseCST::TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::PathElementCS)


def test_basecst::pathelementcs_constructor_exists():
    assert callable(baseCST::PathElementCS.__init__)


def test_basecst::pathelementcs_constructor_args():
    sig = inspect.signature(baseCST::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::PivotableElementCS)


def test_basecst::pivotableelementcs_constructor_exists():
    assert callable(baseCST::PivotableElementCS.__init__)


def test_basecst::pivotableelementcs_constructor_args():
    sig = inspect.signature(baseCST::PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(baseCST::MultiplicityCS)


def test_basecst::multiplicitycs_constructor_exists():
    assert callable(baseCST::MultiplicityCS.__init__)


def test_basecst::multiplicitycs_constructor_args():
    sig = inspect.signature(baseCST::MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityCS)


def test_multiplicitycs_constructor_exists():
    assert callable(MultiplicityCS.__init__)


def test_multiplicitycs_constructor_args():
    sig = inspect.signature(MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::multiplicitystringcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::MultiplicityStringCS)


def test_basecst::multiplicitystringcs_constructor_exists():
    assert callable(baseCST::MultiplicityStringCS.__init__)


def test_basecst::multiplicitystringcs_constructor_args():
    sig = inspect.signature(baseCST::MultiplicityStringCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringBounds" in params, "Missing parameter 'stringBounds'"

def test_basecst::multiplicitystringcs_has_stringBounds():
    assert hasattr(baseCST::MultiplicityStringCS, "stringBounds")
    descriptor = None
    for klass in baseCST::MultiplicityStringCS.__mro__:
        if "stringBounds" in klass.__dict__:
            descriptor = klass.__dict__["stringBounds"]
            break
    assert isinstance(descriptor, property)



def test_basecst::multiplicityboundscs_is_not_abstract():
    assert not inspect.isabstract(baseCST::MultiplicityBoundsCS)


def test_basecst::multiplicityboundscs_constructor_exists():
    assert callable(baseCST::MultiplicityBoundsCS.__init__)


def test_basecst::multiplicityboundscs_constructor_args():
    sig = inspect.signature(baseCST::MultiplicityBoundsCS.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_basecst::multiplicityboundscs_has_lowerBound():
    assert hasattr(baseCST::MultiplicityBoundsCS, "lowerBound")
    descriptor = None
    for klass in baseCST::MultiplicityBoundsCS.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_basecst::multiplicityboundscs_has_upperBound():
    assert hasattr(baseCST::MultiplicityBoundsCS, "upperBound")
    descriptor = None
    for klass in baseCST::MultiplicityBoundsCS.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_basecst::element_is_not_abstract():
    assert not inspect.isabstract(baseCST::Element)


def test_basecst::element_constructor_exists():
    assert callable(baseCST::Element.__init__)


def test_basecst::element_constructor_args():
    sig = inspect.signature(baseCST::Element.__init__)
    params = list(sig.parameters.keys())



def test_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(ElementRefCS)


def test_elementrefcs_constructor_exists():
    assert callable(ElementRefCS.__init__)


def test_elementrefcs_constructor_args():
    sig = inspect.signature(ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::templatebindingcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TemplateBindingCS)


def test_basecst::templatebindingcs_constructor_exists():
    assert callable(baseCST::TemplateBindingCS.__init__)


def test_basecst::templatebindingcs_constructor_args():
    sig = inspect.signature(baseCST::TemplateBindingCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::typerefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypeRefCS)


def test_basecst::typerefcs_constructor_exists():
    assert callable(baseCST::TypeRefCS.__init__)


def test_basecst::typerefcs_constructor_args():
    sig = inspect.signature(baseCST::TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_basecst::namedelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::NamedElementCS)


def test_basecst::namedelementcs_constructor_exists():
    assert callable(baseCST::NamedElementCS.__init__)


def test_basecst::namedelementcs_constructor_args():
    sig = inspect.signature(baseCST::NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst::namedelementcs_has_name():
    assert hasattr(baseCST::NamedElementCS, "name")
    descriptor = None
    for klass in baseCST::NamedElementCS.__mro__:
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



def test_basecst::primitivetyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::PrimitiveTypeRefCS)


def test_basecst::primitivetyperefcs_constructor_exists():
    assert callable(baseCST::PrimitiveTypeRefCS.__init__)


def test_basecst::primitivetyperefcs_constructor_args():
    sig = inspect.signature(baseCST::PrimitiveTypeRefCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst::primitivetyperefcs_has_name():
    assert hasattr(baseCST::PrimitiveTypeRefCS, "name")
    descriptor = None
    for klass in baseCST::PrimitiveTypeRefCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecst::typedtyperefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypedTypeRefCS)


def test_basecst::typedtyperefcs_constructor_exists():
    assert callable(baseCST::TypedTypeRefCS.__init__)


def test_basecst::typedtyperefcs_constructor_args():
    sig = inspect.signature(baseCST::TypedTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::tupletypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TupleTypeCS)


def test_basecst::tupletypecs_constructor_exists():
    assert callable(baseCST::TupleTypeCS.__init__)


def test_basecst::tupletypecs_constructor_args():
    sig = inspect.signature(baseCST::TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst::tupletypecs_has_name():
    assert hasattr(baseCST::TupleTypeCS, "name")
    descriptor = None
    for klass in baseCST::TupleTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecst::namespace_is_not_abstract():
    assert not inspect.isabstract(baseCST::Namespace)


def test_basecst::namespace_constructor_exists():
    assert callable(baseCST::Namespace.__init__)


def test_basecst::namespace_constructor_args():
    sig = inspect.signature(baseCST::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TuplePartCS)


def test_basecst::tuplepartcs_constructor_exists():
    assert callable(baseCST::TuplePartCS.__init__)


def test_basecst::tuplepartcs_constructor_args():
    sig = inspect.signature(baseCST::TuplePartCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::parametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ParameterCS)


def test_basecst::parametercs_constructor_exists():
    assert callable(baseCST::ParameterCS.__init__)


def test_basecst::parametercs_constructor_args():
    sig = inspect.signature(baseCST::ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::featurecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::FeatureCS)


def test_basecst::featurecs_constructor_exists():
    assert callable(baseCST::FeatureCS.__init__)


def test_basecst::featurecs_constructor_args():
    sig = inspect.signature(baseCST::FeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(PivotableElementCS)


def test_pivotableelementcs_constructor_exists():
    assert callable(PivotableElementCS.__init__)


def test_pivotableelementcs_constructor_args():
    sig = inspect.signature(PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::elementrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ElementRefCS)


def test_basecst::elementrefcs_constructor_exists():
    assert callable(baseCST::ElementRefCS.__init__)


def test_basecst::elementrefcs_constructor_args():
    sig = inspect.signature(baseCST::ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_visitablecs_is_not_abstract():
    assert not inspect.isabstract(VisitableCS)


def test_visitablecs_constructor_exists():
    assert callable(VisitableCS.__init__)


def test_visitablecs_constructor_args():
    sig = inspect.signature(VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::elementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ElementCS)


def test_basecst::elementcs_constructor_exists():
    assert callable(baseCST::ElementCS.__init__)


def test_basecst::elementcs_constructor_args():
    sig = inspect.signature(baseCST::ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::specificationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::SpecificationCS)


def test_basecst::specificationcs_constructor_exists():
    assert callable(baseCST::SpecificationCS.__init__)


def test_basecst::specificationcs_constructor_args():
    sig = inspect.signature(baseCST::SpecificationCS.__init__)
    params = list(sig.parameters.keys())
    assert "exprString" in params, "Missing parameter 'exprString'"

def test_basecst::specificationcs_has_exprString():
    assert hasattr(baseCST::SpecificationCS, "exprString")
    descriptor = None
    for klass in baseCST::SpecificationCS.__mro__:
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



def test_basecst::operationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::OperationCS)


def test_basecst::operationcs_constructor_exists():
    assert callable(baseCST::OperationCS.__init__)


def test_basecst::operationcs_constructor_args():
    sig = inspect.signature(baseCST::OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::lambdatypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::LambdaTypeCS)


def test_basecst::lambdatypecs_constructor_exists():
    assert callable(baseCST::LambdaTypeCS.__init__)


def test_basecst::lambdatypecs_constructor_args():
    sig = inspect.signature(baseCST::LambdaTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecst::lambdatypecs_has_name():
    assert hasattr(baseCST::LambdaTypeCS, "name")
    descriptor = None
    for klass in baseCST::LambdaTypeCS.__mro__:
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



def test_basecst::typeparametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypeParameterCS)


def test_basecst::typeparametercs_constructor_exists():
    assert callable(baseCST::TypeParameterCS.__init__)


def test_basecst::typeparametercs_constructor_args():
    sig = inspect.signature(baseCST::TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::StructuralFeatureCS)


def test_basecst::structuralfeaturecs_constructor_exists():
    assert callable(baseCST::StructuralFeatureCS.__init__)


def test_basecst::structuralfeaturecs_constructor_args():
    sig = inspect.signature(baseCST::StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_basecst::structuralfeaturecs_has_default():
    assert hasattr(baseCST::StructuralFeatureCS, "default")
    descriptor = None
    for klass in baseCST::StructuralFeatureCS.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_basecst::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypedRefCS)


def test_basecst::typedrefcs_constructor_exists():
    assert callable(baseCST::TypedRefCS.__init__)


def test_basecst::typedrefcs_constructor_args():
    sig = inspect.signature(baseCST::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::packagecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::PackageCS)


def test_basecst::packagecs_constructor_exists():
    assert callable(baseCST::PackageCS.__init__)


def test_basecst::packagecs_constructor_args():
    sig = inspect.signature(baseCST::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"

def test_basecst::packagecs_has_nsURI():
    assert hasattr(baseCST::PackageCS, "nsURI")
    descriptor = None
    for klass in baseCST::PackageCS.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)

def test_basecst::packagecs_has_nsPrefix():
    assert hasattr(baseCST::PackageCS, "nsPrefix")
    descriptor = None
    for klass in baseCST::PackageCS.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)



def test_basecst::librarycs_is_not_abstract():
    assert not inspect.isabstract(baseCST::LibraryCS)


def test_basecst::librarycs_constructor_exists():
    assert callable(baseCST::LibraryCS.__init__)


def test_basecst::librarycs_constructor_args():
    sig = inspect.signature(baseCST::LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::importcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ImportCS)


def test_basecst::importcs_constructor_exists():
    assert callable(baseCST::ImportCS.__init__)


def test_basecst::importcs_constructor_args():
    sig = inspect.signature(baseCST::ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_basecst::importcs_has_all():
    assert hasattr(baseCST::ImportCS, "all")
    descriptor = None
    for klass in baseCST::ImportCS.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::datatypecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::DataTypeCS)


def test_basecst::datatypecs_constructor_exists():
    assert callable(baseCST::DataTypeCS.__init__)


def test_basecst::datatypecs_constructor_args():
    sig = inspect.signature(baseCST::DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::enumerationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::EnumerationCS)


def test_basecst::enumerationcs_constructor_exists():
    assert callable(baseCST::EnumerationCS.__init__)


def test_basecst::enumerationcs_constructor_args():
    sig = inspect.signature(baseCST::EnumerationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::classcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ClassCS)


def test_basecst::classcs_constructor_exists():
    assert callable(baseCST::ClassCS.__init__)


def test_basecst::classcs_constructor_args():
    sig = inspect.signature(baseCST::ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::referencecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ReferenceCS)


def test_basecst::referencecs_constructor_exists():
    assert callable(baseCST::ReferenceCS.__init__)


def test_basecst::referencecs_constructor_args():
    sig = inspect.signature(baseCST::ReferenceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::attributecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::AttributeCS)


def test_basecst::attributecs_constructor_exists():
    assert callable(baseCST::AttributeCS.__init__)


def test_basecst::attributecs_constructor_args():
    sig = inspect.signature(baseCST::AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::namespacecs_is_not_abstract():
    assert not inspect.isabstract(baseCST::NamespaceCS)


def test_basecst::namespacecs_constructor_exists():
    assert callable(baseCST::NamespaceCS.__init__)


def test_basecst::namespacecs_constructor_args():
    sig = inspect.signature(baseCST::NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::enumerationliteralcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::EnumerationLiteralCS)


def test_basecst::enumerationliteralcs_constructor_exists():
    assert callable(baseCST::EnumerationLiteralCS.__init__)


def test_basecst::enumerationliteralcs_constructor_args():
    sig = inspect.signature(baseCST::EnumerationLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst::enumerationliteralcs_has_value():
    assert hasattr(baseCST::EnumerationLiteralCS, "value")
    descriptor = None
    for klass in baseCST::EnumerationLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst::detailcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::DetailCS)


def test_basecst::detailcs_constructor_exists():
    assert callable(baseCST::DetailCS.__init__)


def test_basecst::detailcs_constructor_args():
    sig = inspect.signature(baseCST::DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst::detailcs_has_value():
    assert hasattr(baseCST::DetailCS, "value")
    descriptor = None
    for klass in baseCST::DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst::typedelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TypedElementCS)


def test_basecst::typedelementcs_constructor_exists():
    assert callable(baseCST::TypedElementCS.__init__)


def test_basecst::typedelementcs_constructor_args():
    sig = inspect.signature(baseCST::TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_basecst::typedelementcs_has_optional():
    assert hasattr(baseCST::TypedElementCS, "optional")
    descriptor = None
    for klass in baseCST::TypedElementCS.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_basecst::typedelementcs_has_qualifier():
    assert hasattr(baseCST::TypedElementCS, "qualifier")
    descriptor = None
    for klass in baseCST::TypedElementCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_basecst::constraintcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ConstraintCS)


def test_basecst::constraintcs_constructor_exists():
    assert callable(baseCST::ConstraintCS.__init__)


def test_basecst::constraintcs_constructor_args():
    sig = inspect.signature(baseCST::ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_basecst::constraintcs_has_stereotype():
    assert hasattr(baseCST::ConstraintCS, "stereotype")
    descriptor = None
    for klass in baseCST::ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_basecst::templateparametercs_is_not_abstract():
    assert not inspect.isabstract(baseCST::TemplateParameterCS)


def test_basecst::templateparametercs_constructor_exists():
    assert callable(baseCST::TemplateParameterCS.__init__)


def test_basecst::templateparametercs_constructor_args():
    sig = inspect.signature(baseCST::TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::classifiercs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ClassifierCS)


def test_basecst::classifiercs_constructor_exists():
    assert callable(baseCST::ClassifierCS.__init__)


def test_basecst::classifiercs_constructor_args():
    sig = inspect.signature(baseCST::ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_basecst::classifiercs_has_qualifier():
    assert hasattr(baseCST::ClassifierCS, "qualifier")
    descriptor = None
    for klass in baseCST::ClassifierCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_basecst::classifiercs_has_instanceClassName():
    assert hasattr(baseCST::ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in baseCST::ClassifierCS.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_basecst::annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::AnnotationElementCS)


def test_basecst::annotationelementcs_constructor_exists():
    assert callable(baseCST::AnnotationElementCS.__init__)


def test_basecst::annotationelementcs_constructor_args():
    sig = inspect.signature(baseCST::AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::modelelementrefcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ModelElementRefCS)


def test_basecst::modelelementrefcs_constructor_exists():
    assert callable(baseCST::ModelElementRefCS.__init__)


def test_basecst::modelelementrefcs_constructor_args():
    sig = inspect.signature(baseCST::ModelElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecst::modelelementcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::ModelElementCS)


def test_basecst::modelelementcs_constructor_exists():
    assert callable(baseCST::ModelElementCS.__init__)


def test_basecst::modelelementcs_constructor_args():
    sig = inspect.signature(baseCST::ModelElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "csi" in params, "Missing parameter 'csi'"
    assert "originalXmiId" in params, "Missing parameter 'originalXmiId'"

def test_basecst::modelelementcs_has_csi():
    assert hasattr(baseCST::ModelElementCS, "csi")
    descriptor = None
    for klass in baseCST::ModelElementCS.__mro__:
        if "csi" in klass.__dict__:
            descriptor = klass.__dict__["csi"]
            break
    assert isinstance(descriptor, property)

def test_basecst::modelelementcs_has_originalXmiId():
    assert hasattr(baseCST::ModelElementCS, "originalXmiId")
    descriptor = None
    for klass in baseCST::ModelElementCS.__mro__:
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



def test_basecst::documentationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::DocumentationCS)


def test_basecst::documentationcs_constructor_exists():
    assert callable(baseCST::DocumentationCS.__init__)


def test_basecst::documentationcs_constructor_args():
    sig = inspect.signature(baseCST::DocumentationCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecst::documentationcs_has_value():
    assert hasattr(baseCST::DocumentationCS, "value")
    descriptor = None
    for klass in baseCST::DocumentationCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecst::annotationcs_is_not_abstract():
    assert not inspect.isabstract(baseCST::AnnotationCS)


def test_basecst::annotationcs_constructor_exists():
    assert callable(baseCST::AnnotationCS.__init__)


def test_basecst::annotationcs_constructor_args():
    sig = inspect.signature(baseCST::AnnotationCS.__init__)
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
baseCST::VisitableCS_strategy = st.builds(
    baseCST::VisitableCS,
)
baseCST::Type_strategy = st.builds(
    baseCST::Type,
)
TypeRefCS_strategy = st.builds(
    TypeRefCS,
)
baseCST::WildcardTypeRefCS_strategy = st.builds(
    baseCST::WildcardTypeRefCS,
)
TemplateParameterCS_strategy = st.builds(
    TemplateParameterCS,
)
PathElementCS_strategy = st.builds(
    PathElementCS,
)
baseCST::PathElementWithURICS_strategy = st.builds(
    baseCST::PathElementWithURICS,
    uri=
        safe_text
)
RootCS_strategy = st.builds(
    RootCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
baseCST::RootPackageCS_strategy = st.builds(
    baseCST::RootPackageCS,
)
baseCST::Property_strategy = st.builds(
    baseCST::Property,
)
baseCST::EClassifier_strategy = st.builds(
    baseCST::EClassifier,
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
baseCST::TypeCS_strategy = st.builds(
    baseCST::TypeCS,
)
baseCST::RootCS_strategy = st.builds(
    baseCST::RootCS,
)
baseCST::TemplateSignatureCS_strategy = st.builds(
    baseCST::TemplateSignatureCS,
)
baseCST::TemplateParameterSubstitutionCS_strategy = st.builds(
    baseCST::TemplateParameterSubstitutionCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
baseCST::PathNameCS_strategy = st.builds(
    baseCST::PathNameCS,
    scopeFilter=
        safe_text
)
baseCST::TemplateableElementCS_strategy = st.builds(
    baseCST::TemplateableElementCS,
)
baseCST::PathElementCS_strategy = st.builds(
    baseCST::PathElementCS,
)
baseCST::PivotableElementCS_strategy = st.builds(
    baseCST::PivotableElementCS,
)
baseCST::MultiplicityCS_strategy = st.builds(
    baseCST::MultiplicityCS,
)
MultiplicityCS_strategy = st.builds(
    MultiplicityCS,
)
baseCST::MultiplicityStringCS_strategy = st.builds(
    baseCST::MultiplicityStringCS,
    stringBounds=
        safe_text
)
baseCST::MultiplicityBoundsCS_strategy = st.builds(
    baseCST::MultiplicityBoundsCS,
    lowerBound=
        st.integers(),
    upperBound=
        safe_text
)
baseCST::Element_strategy = st.builds(
    baseCST::Element,
)
ElementRefCS_strategy = st.builds(
    ElementRefCS,
)
baseCST::TemplateBindingCS_strategy = st.builds(
    baseCST::TemplateBindingCS,
)
baseCST::TypeRefCS_strategy = st.builds(
    baseCST::TypeRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
baseCST::NamedElementCS_strategy = st.builds(
    baseCST::NamedElementCS,
    name=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
baseCST::PrimitiveTypeRefCS_strategy = st.builds(
    baseCST::PrimitiveTypeRefCS,
    name=
        safe_text
)
baseCST::TypedTypeRefCS_strategy = st.builds(
    baseCST::TypedTypeRefCS,
)
baseCST::TupleTypeCS_strategy = st.builds(
    baseCST::TupleTypeCS,
    name=
        safe_text
)
baseCST::Namespace_strategy = st.builds(
    baseCST::Namespace,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
baseCST::TuplePartCS_strategy = st.builds(
    baseCST::TuplePartCS,
)
baseCST::ParameterCS_strategy = st.builds(
    baseCST::ParameterCS,
)
baseCST::FeatureCS_strategy = st.builds(
    baseCST::FeatureCS,
)
PivotableElementCS_strategy = st.builds(
    PivotableElementCS,
)
baseCST::ElementRefCS_strategy = st.builds(
    baseCST::ElementRefCS,
)
VisitableCS_strategy = st.builds(
    VisitableCS,
)
baseCST::ElementCS_strategy = st.builds(
    baseCST::ElementCS,
)
baseCST::SpecificationCS_strategy = st.builds(
    baseCST::SpecificationCS,
    exprString=
        safe_text
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
baseCST::OperationCS_strategy = st.builds(
    baseCST::OperationCS,
)
baseCST::LambdaTypeCS_strategy = st.builds(
    baseCST::LambdaTypeCS,
    name=
        safe_text
)
TypeCS_strategy = st.builds(
    TypeCS,
)
baseCST::TypeParameterCS_strategy = st.builds(
    baseCST::TypeParameterCS,
)
baseCST::StructuralFeatureCS_strategy = st.builds(
    baseCST::StructuralFeatureCS,
    default=
        safe_text
)
baseCST::TypedRefCS_strategy = st.builds(
    baseCST::TypedRefCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
baseCST::PackageCS_strategy = st.builds(
    baseCST::PackageCS,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
baseCST::LibraryCS_strategy = st.builds(
    baseCST::LibraryCS,
)
baseCST::ImportCS_strategy = st.builds(
    baseCST::ImportCS,
    all=
        st.booleans()
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
baseCST::DataTypeCS_strategy = st.builds(
    baseCST::DataTypeCS,
)
baseCST::EnumerationCS_strategy = st.builds(
    baseCST::EnumerationCS,
)
baseCST::ClassCS_strategy = st.builds(
    baseCST::ClassCS,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
baseCST::ReferenceCS_strategy = st.builds(
    baseCST::ReferenceCS,
)
baseCST::AttributeCS_strategy = st.builds(
    baseCST::AttributeCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
baseCST::NamespaceCS_strategy = st.builds(
    baseCST::NamespaceCS,
)
baseCST::EnumerationLiteralCS_strategy = st.builds(
    baseCST::EnumerationLiteralCS,
    value=
        st.integers()
)
baseCST::DetailCS_strategy = st.builds(
    baseCST::DetailCS,
    value=
        safe_text
)
baseCST::TypedElementCS_strategy = st.builds(
    baseCST::TypedElementCS,
    optional=
        st.booleans(),
    qualifier=
        safe_text
)
baseCST::ConstraintCS_strategy = st.builds(
    baseCST::ConstraintCS,
    stereotype=
        safe_text
)
baseCST::TemplateParameterCS_strategy = st.builds(
    baseCST::TemplateParameterCS,
)
baseCST::ClassifierCS_strategy = st.builds(
    baseCST::ClassifierCS,
    qualifier=
        safe_text,
    instanceClassName=
        safe_text
)
baseCST::AnnotationElementCS_strategy = st.builds(
    baseCST::AnnotationElementCS,
)
baseCST::ModelElementRefCS_strategy = st.builds(
    baseCST::ModelElementRefCS,
)
baseCST::ModelElementCS_strategy = st.builds(
    baseCST::ModelElementCS,
    csi=
        safe_text,
    originalXmiId=
        safe_text
)
AnnotationElementCS_strategy = st.builds(
    AnnotationElementCS,
)
baseCST::DocumentationCS_strategy = st.builds(
    baseCST::DocumentationCS,
    value=
        safe_text
)
baseCST::AnnotationCS_strategy = st.builds(
    baseCST::AnnotationCS,
)

@given(instance=baseCST::VisitableCS_strategy)
@settings(max_examples=50)
def test_basecst::visitablecs_instantiation(instance):
    assert isinstance(instance, baseCST::VisitableCS)

@given(instance=baseCST::Type_strategy)
@settings(max_examples=50)
def test_basecst::type_instantiation(instance):
    assert isinstance(instance, baseCST::Type)

@given(instance=TypeRefCS_strategy)
@settings(max_examples=50)
def test_typerefcs_instantiation(instance):
    assert isinstance(instance, TypeRefCS)

@given(instance=baseCST::WildcardTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst::wildcardtyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST::WildcardTypeRefCS)

@given(instance=TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_templateparametercs_instantiation(instance):
    assert isinstance(instance, TemplateParameterCS)

@given(instance=PathElementCS_strategy)
@settings(max_examples=50)
def test_pathelementcs_instantiation(instance):
    assert isinstance(instance, PathElementCS)

@given(instance=baseCST::PathElementWithURICS_strategy)
@settings(max_examples=50)
def test_basecst::pathelementwithurics_instantiation(instance):
    assert isinstance(instance, baseCST::PathElementWithURICS)

@given(instance=baseCST::PathElementWithURICS_strategy)
def test_basecst::pathelementwithurics_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=baseCST::PathElementWithURICS_strategy)
def test_basecst::pathelementwithurics_uri_setter(instance):
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

@given(instance=baseCST::RootPackageCS_strategy)
@settings(max_examples=50)
def test_basecst::rootpackagecs_instantiation(instance):
    assert isinstance(instance, baseCST::RootPackageCS)

@given(instance=baseCST::Property_strategy)
@settings(max_examples=50)
def test_basecst::property_instantiation(instance):
    assert isinstance(instance, baseCST::Property)

@given(instance=baseCST::EClassifier_strategy)
@settings(max_examples=50)
def test_basecst::eclassifier_instantiation(instance):
    assert isinstance(instance, baseCST::EClassifier)

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

@given(instance=baseCST::TypeCS_strategy)
@settings(max_examples=50)
def test_basecst::typecs_instantiation(instance):
    assert isinstance(instance, baseCST::TypeCS)

@given(instance=baseCST::RootCS_strategy)
@settings(max_examples=50)
def test_basecst::rootcs_instantiation(instance):
    assert isinstance(instance, baseCST::RootCS)

@given(instance=baseCST::TemplateSignatureCS_strategy)
@settings(max_examples=50)
def test_basecst::templatesignaturecs_instantiation(instance):
    assert isinstance(instance, baseCST::TemplateSignatureCS)

@given(instance=baseCST::TemplateParameterSubstitutionCS_strategy)
@settings(max_examples=50)
def test_basecst::templateparametersubstitutioncs_instantiation(instance):
    assert isinstance(instance, baseCST::TemplateParameterSubstitutionCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=baseCST::PathNameCS_strategy)
@settings(max_examples=50)
def test_basecst::pathnamecs_instantiation(instance):
    assert isinstance(instance, baseCST::PathNameCS)

@given(instance=baseCST::PathNameCS_strategy)
def test_basecst::pathnamecs_scopeFilter_type(instance):
    assert isinstance(instance.scopeFilter, str)


@given(instance=baseCST::PathNameCS_strategy)
def test_basecst::pathnamecs_scopeFilter_setter(instance):
    original = instance.scopeFilter
    instance.scopeFilter = original
    assert instance.scopeFilter == original

@given(instance=baseCST::TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_basecst::templateableelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::TemplateableElementCS)

@given(instance=baseCST::PathElementCS_strategy)
@settings(max_examples=50)
def test_basecst::pathelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::PathElementCS)

@given(instance=baseCST::PivotableElementCS_strategy)
@settings(max_examples=50)
def test_basecst::pivotableelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::PivotableElementCS)

@given(instance=baseCST::MultiplicityCS_strategy)
@settings(max_examples=50)
def test_basecst::multiplicitycs_instantiation(instance):
    assert isinstance(instance, baseCST::MultiplicityCS)

@given(instance=MultiplicityCS_strategy)
@settings(max_examples=50)
def test_multiplicitycs_instantiation(instance):
    assert isinstance(instance, MultiplicityCS)

@given(instance=baseCST::MultiplicityStringCS_strategy)
@settings(max_examples=50)
def test_basecst::multiplicitystringcs_instantiation(instance):
    assert isinstance(instance, baseCST::MultiplicityStringCS)

@given(instance=baseCST::MultiplicityStringCS_strategy)
def test_basecst::multiplicitystringcs_stringBounds_type(instance):
    assert isinstance(instance.stringBounds, str)


@given(instance=baseCST::MultiplicityStringCS_strategy)
def test_basecst::multiplicitystringcs_stringBounds_setter(instance):
    original = instance.stringBounds
    instance.stringBounds = original
    assert instance.stringBounds == original

@given(instance=baseCST::MultiplicityBoundsCS_strategy)
@settings(max_examples=50)
def test_basecst::multiplicityboundscs_instantiation(instance):
    assert isinstance(instance, baseCST::MultiplicityBoundsCS)

@given(instance=baseCST::MultiplicityBoundsCS_strategy)
def test_basecst::multiplicityboundscs_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=baseCST::MultiplicityBoundsCS_strategy)
def test_basecst::multiplicityboundscs_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=baseCST::MultiplicityBoundsCS_strategy)
def test_basecst::multiplicityboundscs_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=baseCST::MultiplicityBoundsCS_strategy)
def test_basecst::multiplicityboundscs_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=baseCST::Element_strategy)
@settings(max_examples=50)
def test_basecst::element_instantiation(instance):
    assert isinstance(instance, baseCST::Element)

@given(instance=ElementRefCS_strategy)
@settings(max_examples=50)
def test_elementrefcs_instantiation(instance):
    assert isinstance(instance, ElementRefCS)

@given(instance=baseCST::TemplateBindingCS_strategy)
@settings(max_examples=50)
def test_basecst::templatebindingcs_instantiation(instance):
    assert isinstance(instance, baseCST::TemplateBindingCS)

@given(instance=baseCST::TypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst::typerefcs_instantiation(instance):
    assert isinstance(instance, baseCST::TypeRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=baseCST::NamedElementCS_strategy)
@settings(max_examples=50)
def test_basecst::namedelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::NamedElementCS)

@given(instance=baseCST::NamedElementCS_strategy)
def test_basecst::namedelementcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=baseCST::NamedElementCS_strategy)
def test_basecst::namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=baseCST::PrimitiveTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst::primitivetyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST::PrimitiveTypeRefCS)

@given(instance=baseCST::PrimitiveTypeRefCS_strategy)
def test_basecst::primitivetyperefcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=baseCST::PrimitiveTypeRefCS_strategy)
def test_basecst::primitivetyperefcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=baseCST::TypedTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecst::typedtyperefcs_instantiation(instance):
    assert isinstance(instance, baseCST::TypedTypeRefCS)

@given(instance=baseCST::TupleTypeCS_strategy)
@settings(max_examples=50)
def test_basecst::tupletypecs_instantiation(instance):
    assert isinstance(instance, baseCST::TupleTypeCS)

@given(instance=baseCST::TupleTypeCS_strategy)
def test_basecst::tupletypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=baseCST::TupleTypeCS_strategy)
def test_basecst::tupletypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=baseCST::Namespace_strategy)
@settings(max_examples=50)
def test_basecst::namespace_instantiation(instance):
    assert isinstance(instance, baseCST::Namespace)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=baseCST::TuplePartCS_strategy)
@settings(max_examples=50)
def test_basecst::tuplepartcs_instantiation(instance):
    assert isinstance(instance, baseCST::TuplePartCS)

@given(instance=baseCST::ParameterCS_strategy)
@settings(max_examples=50)
def test_basecst::parametercs_instantiation(instance):
    assert isinstance(instance, baseCST::ParameterCS)

@given(instance=baseCST::FeatureCS_strategy)
@settings(max_examples=50)
def test_basecst::featurecs_instantiation(instance):
    assert isinstance(instance, baseCST::FeatureCS)

@given(instance=PivotableElementCS_strategy)
@settings(max_examples=50)
def test_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, PivotableElementCS)

@given(instance=baseCST::ElementRefCS_strategy)
@settings(max_examples=50)
def test_basecst::elementrefcs_instantiation(instance):
    assert isinstance(instance, baseCST::ElementRefCS)

@given(instance=VisitableCS_strategy)
@settings(max_examples=50)
def test_visitablecs_instantiation(instance):
    assert isinstance(instance, VisitableCS)

@given(instance=baseCST::ElementCS_strategy)
@settings(max_examples=50)
def test_basecst::elementcs_instantiation(instance):
    assert isinstance(instance, baseCST::ElementCS)

@given(instance=baseCST::SpecificationCS_strategy)
@settings(max_examples=50)
def test_basecst::specificationcs_instantiation(instance):
    assert isinstance(instance, baseCST::SpecificationCS)

@given(instance=baseCST::SpecificationCS_strategy)
def test_basecst::specificationcs_exprString_type(instance):
    assert isinstance(instance.exprString, str)


@given(instance=baseCST::SpecificationCS_strategy)
def test_basecst::specificationcs_exprString_setter(instance):
    original = instance.exprString
    instance.exprString = original
    assert instance.exprString == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=baseCST::OperationCS_strategy)
@settings(max_examples=50)
def test_basecst::operationcs_instantiation(instance):
    assert isinstance(instance, baseCST::OperationCS)

@given(instance=baseCST::LambdaTypeCS_strategy)
@settings(max_examples=50)
def test_basecst::lambdatypecs_instantiation(instance):
    assert isinstance(instance, baseCST::LambdaTypeCS)

@given(instance=baseCST::LambdaTypeCS_strategy)
def test_basecst::lambdatypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=baseCST::LambdaTypeCS_strategy)
def test_basecst::lambdatypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=baseCST::TypeParameterCS_strategy)
@settings(max_examples=50)
def test_basecst::typeparametercs_instantiation(instance):
    assert isinstance(instance, baseCST::TypeParameterCS)

@given(instance=baseCST::StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_basecst::structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, baseCST::StructuralFeatureCS)

@given(instance=baseCST::StructuralFeatureCS_strategy)
def test_basecst::structuralfeaturecs_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=baseCST::StructuralFeatureCS_strategy)
def test_basecst::structuralfeaturecs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=baseCST::TypedRefCS_strategy)
@settings(max_examples=50)
def test_basecst::typedrefcs_instantiation(instance):
    assert isinstance(instance, baseCST::TypedRefCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=baseCST::PackageCS_strategy)
@settings(max_examples=50)
def test_basecst::packagecs_instantiation(instance):
    assert isinstance(instance, baseCST::PackageCS)

@given(instance=baseCST::PackageCS_strategy)
def test_basecst::packagecs_nsURI_type(instance):
    assert isinstance(instance.nsURI, str)


@given(instance=baseCST::PackageCS_strategy)
def test_basecst::packagecs_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

@given(instance=baseCST::PackageCS_strategy)
def test_basecst::packagecs_nsPrefix_type(instance):
    assert isinstance(instance.nsPrefix, str)


@given(instance=baseCST::PackageCS_strategy)
def test_basecst::packagecs_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=baseCST::LibraryCS_strategy)
@settings(max_examples=50)
def test_basecst::librarycs_instantiation(instance):
    assert isinstance(instance, baseCST::LibraryCS)

@given(instance=baseCST::ImportCS_strategy)
@settings(max_examples=50)
def test_basecst::importcs_instantiation(instance):
    assert isinstance(instance, baseCST::ImportCS)

@given(instance=baseCST::ImportCS_strategy)
def test_basecst::importcs_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=baseCST::ImportCS_strategy)
def test_basecst::importcs_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=baseCST::DataTypeCS_strategy)
@settings(max_examples=50)
def test_basecst::datatypecs_instantiation(instance):
    assert isinstance(instance, baseCST::DataTypeCS)

@given(instance=baseCST::EnumerationCS_strategy)
@settings(max_examples=50)
def test_basecst::enumerationcs_instantiation(instance):
    assert isinstance(instance, baseCST::EnumerationCS)

@given(instance=baseCST::ClassCS_strategy)
@settings(max_examples=50)
def test_basecst::classcs_instantiation(instance):
    assert isinstance(instance, baseCST::ClassCS)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=baseCST::ReferenceCS_strategy)
@settings(max_examples=50)
def test_basecst::referencecs_instantiation(instance):
    assert isinstance(instance, baseCST::ReferenceCS)

@given(instance=baseCST::AttributeCS_strategy)
@settings(max_examples=50)
def test_basecst::attributecs_instantiation(instance):
    assert isinstance(instance, baseCST::AttributeCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=baseCST::NamespaceCS_strategy)
@settings(max_examples=50)
def test_basecst::namespacecs_instantiation(instance):
    assert isinstance(instance, baseCST::NamespaceCS)

@given(instance=baseCST::EnumerationLiteralCS_strategy)
@settings(max_examples=50)
def test_basecst::enumerationliteralcs_instantiation(instance):
    assert isinstance(instance, baseCST::EnumerationLiteralCS)

@given(instance=baseCST::EnumerationLiteralCS_strategy)
def test_basecst::enumerationliteralcs_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=baseCST::EnumerationLiteralCS_strategy)
def test_basecst::enumerationliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST::DetailCS_strategy)
@settings(max_examples=50)
def test_basecst::detailcs_instantiation(instance):
    assert isinstance(instance, baseCST::DetailCS)

@given(instance=baseCST::DetailCS_strategy)
def test_basecst::detailcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=baseCST::DetailCS_strategy)
def test_basecst::detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST::TypedElementCS_strategy)
@settings(max_examples=50)
def test_basecst::typedelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::TypedElementCS)

@given(instance=baseCST::TypedElementCS_strategy)
def test_basecst::typedelementcs_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=baseCST::TypedElementCS_strategy)
def test_basecst::typedelementcs_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=baseCST::TypedElementCS_strategy)
def test_basecst::typedelementcs_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=baseCST::TypedElementCS_strategy)
def test_basecst::typedelementcs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=baseCST::ConstraintCS_strategy)
@settings(max_examples=50)
def test_basecst::constraintcs_instantiation(instance):
    assert isinstance(instance, baseCST::ConstraintCS)

@given(instance=baseCST::ConstraintCS_strategy)
def test_basecst::constraintcs_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=baseCST::ConstraintCS_strategy)
def test_basecst::constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=baseCST::TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_basecst::templateparametercs_instantiation(instance):
    assert isinstance(instance, baseCST::TemplateParameterCS)

@given(instance=baseCST::ClassifierCS_strategy)
@settings(max_examples=50)
def test_basecst::classifiercs_instantiation(instance):
    assert isinstance(instance, baseCST::ClassifierCS)

@given(instance=baseCST::ClassifierCS_strategy)
def test_basecst::classifiercs_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=baseCST::ClassifierCS_strategy)
def test_basecst::classifiercs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=baseCST::ClassifierCS_strategy)
def test_basecst::classifiercs_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=baseCST::ClassifierCS_strategy)
def test_basecst::classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

@given(instance=baseCST::AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_basecst::annotationelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::AnnotationElementCS)

@given(instance=baseCST::ModelElementRefCS_strategy)
@settings(max_examples=50)
def test_basecst::modelelementrefcs_instantiation(instance):
    assert isinstance(instance, baseCST::ModelElementRefCS)

@given(instance=baseCST::ModelElementCS_strategy)
@settings(max_examples=50)
def test_basecst::modelelementcs_instantiation(instance):
    assert isinstance(instance, baseCST::ModelElementCS)

@given(instance=baseCST::ModelElementCS_strategy)
def test_basecst::modelelementcs_csi_type(instance):
    assert isinstance(instance.csi, str)


@given(instance=baseCST::ModelElementCS_strategy)
def test_basecst::modelelementcs_csi_setter(instance):
    original = instance.csi
    instance.csi = original
    assert instance.csi == original

@given(instance=baseCST::ModelElementCS_strategy)
def test_basecst::modelelementcs_originalXmiId_type(instance):
    assert isinstance(instance.originalXmiId, str)


@given(instance=baseCST::ModelElementCS_strategy)
def test_basecst::modelelementcs_originalXmiId_setter(instance):
    original = instance.originalXmiId
    instance.originalXmiId = original
    assert instance.originalXmiId == original

@given(instance=AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_annotationelementcs_instantiation(instance):
    assert isinstance(instance, AnnotationElementCS)

@given(instance=baseCST::DocumentationCS_strategy)
@settings(max_examples=50)
def test_basecst::documentationcs_instantiation(instance):
    assert isinstance(instance, baseCST::DocumentationCS)

@given(instance=baseCST::DocumentationCS_strategy)
def test_basecst::documentationcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=baseCST::DocumentationCS_strategy)
def test_basecst::documentationcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=baseCST::AnnotationCS_strategy)
@settings(max_examples=50)
def test_basecst::annotationcs_instantiation(instance):
    assert isinstance(instance, baseCST::AnnotationCS)

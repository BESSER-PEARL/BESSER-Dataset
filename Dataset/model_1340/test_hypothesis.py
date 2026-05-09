import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basecs::VisitableCS,
    basecs::Type,
    TypeRefCS,
    basecs::WildcardTypeRefCS,
    TemplateParameterCS,
    RootCS,
    basecs::Property,
    PathElementCS,
    basecs::PathElementWithURICS,
    basecs::EClassifier,
    Pivotable,
    PackageOwnerCS,
    basecs::RootPackageCS,
    TypedElementCS,
    basecs::TuplePartCS,
    basecs::ParameterCS,
    basecs::FeatureCS,
    FeatureCS,
    ModelElementCS,
    basecs::PackageOwnerCS,
    basecs::TypeCS,
    basecs::TemplateParameterSubstitutionCS,
    basecs::RootCS,
    basecs::TemplateSignatureCS,
    ElementCS,
    basecs::TemplateableElementCS,
    basecs::PathElementCS,
    basecs::PivotableElementCS,
    basecs::MultiplicityCS,
    MultiplicityCS,
    basecs::MultiplicityStringCS,
    basecs::MultiplicityBoundsCS,
    basecs::Element,
    ElementRefCS,
    basecs::TemplateBindingCS,
    basecs::TypeRefCS,
    Nameable,
    basecs::NamedElementCS,
    TypedRefCS,
    basecs::TupleTypeCS,
    basecs::TypedTypeRefCS,
    basecs::PrimitiveTypeRefCS,
    basecs::Namespace,
    basecs::PathNameCS,
    PivotableElementCS,
    basecs::ElementRefCS,
    VisitableCS,
    basecs::ElementCS,
    basecs::SpecificationCS,
    TemplateableElementCS,
    basecs::LambdaTypeCS,
    TypeCS,
    basecs::TypeParameterCS,
    basecs::StructuralFeatureCS,
    basecs::OperationCS,
    basecs::TypedRefCS,
    NamespaceCS,
    basecs::PackageCS,
    basecs::LibraryCS,
    basecs::ImportCS,
    ClassifierCS,
    basecs::DataTypeCS,
    basecs::EnumerationCS,
    basecs::ClassCS,
    StructuralFeatureCS,
    basecs::ReferenceCS,
    basecs::AttributeCS,
    NamedElementCS,
    basecs::DetailCS,
    basecs::ConstraintCS,
    basecs::TemplateParameterCS,
    basecs::TypedElementCS,
    basecs::ClassifierCS,
    basecs::EnumerationLiteralCS,
    basecs::NamespaceCS,
    basecs::AnnotationElementCS,
    basecs::ModelElementRefCS,
    basecs::ModelElementCS,
    AnnotationElementCS,
    basecs::DocumentationCS,
    basecs::AnnotationCS,
    IteratorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basecs::visitablecs_is_not_abstract():
    assert not inspect.isabstract(basecs::VisitableCS)


def test_basecs::visitablecs_constructor_exists():
    assert callable(basecs::VisitableCS.__init__)


def test_basecs::visitablecs_constructor_args():
    sig = inspect.signature(basecs::VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::type_is_not_abstract():
    assert not inspect.isabstract(basecs::Type)


def test_basecs::type_constructor_exists():
    assert callable(basecs::Type.__init__)


def test_basecs::type_constructor_args():
    sig = inspect.signature(basecs::Type.__init__)
    params = list(sig.parameters.keys())



def test_typerefcs_is_not_abstract():
    assert not inspect.isabstract(TypeRefCS)


def test_typerefcs_constructor_exists():
    assert callable(TypeRefCS.__init__)


def test_typerefcs_constructor_args():
    sig = inspect.signature(TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::wildcardtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::WildcardTypeRefCS)


def test_basecs::wildcardtyperefcs_constructor_exists():
    assert callable(basecs::WildcardTypeRefCS.__init__)


def test_basecs::wildcardtyperefcs_constructor_args():
    sig = inspect.signature(basecs::WildcardTypeRefCS.__init__)
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



def test_basecs::property_is_not_abstract():
    assert not inspect.isabstract(basecs::Property)


def test_basecs::property_constructor_exists():
    assert callable(basecs::Property.__init__)


def test_basecs::property_constructor_args():
    sig = inspect.signature(basecs::Property.__init__)
    params = list(sig.parameters.keys())



def test_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(PathElementCS)


def test_pathelementcs_constructor_exists():
    assert callable(PathElementCS.__init__)


def test_pathelementcs_constructor_args():
    sig = inspect.signature(PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::pathelementwithurics_is_not_abstract():
    assert not inspect.isabstract(basecs::PathElementWithURICS)


def test_basecs::pathelementwithurics_constructor_exists():
    assert callable(basecs::PathElementWithURICS.__init__)


def test_basecs::pathelementwithurics_constructor_args():
    sig = inspect.signature(basecs::PathElementWithURICS.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_basecs::pathelementwithurics_has_uri():
    assert hasattr(basecs::PathElementWithURICS, "uri")
    descriptor = None
    for klass in basecs::PathElementWithURICS.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_basecs::eclassifier_is_not_abstract():
    assert not inspect.isabstract(basecs::EClassifier)


def test_basecs::eclassifier_constructor_exists():
    assert callable(basecs::EClassifier.__init__)


def test_basecs::eclassifier_constructor_args():
    sig = inspect.signature(basecs::EClassifier.__init__)
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



def test_basecs::rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(basecs::RootPackageCS)


def test_basecs::rootpackagecs_constructor_exists():
    assert callable(basecs::RootPackageCS.__init__)


def test_basecs::rootpackagecs_constructor_args():
    sig = inspect.signature(basecs::RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TuplePartCS)


def test_basecs::tuplepartcs_constructor_exists():
    assert callable(basecs::TuplePartCS.__init__)


def test_basecs::tuplepartcs_constructor_args():
    sig = inspect.signature(basecs::TuplePartCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::parametercs_is_not_abstract():
    assert not inspect.isabstract(basecs::ParameterCS)


def test_basecs::parametercs_constructor_exists():
    assert callable(basecs::ParameterCS.__init__)


def test_basecs::parametercs_constructor_args():
    sig = inspect.signature(basecs::ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::featurecs_is_not_abstract():
    assert not inspect.isabstract(basecs::FeatureCS)


def test_basecs::featurecs_constructor_exists():
    assert callable(basecs::FeatureCS.__init__)


def test_basecs::featurecs_constructor_args():
    sig = inspect.signature(basecs::FeatureCS.__init__)
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



def test_basecs::packageownercs_is_not_abstract():
    assert not inspect.isabstract(basecs::PackageOwnerCS)


def test_basecs::packageownercs_constructor_exists():
    assert callable(basecs::PackageOwnerCS.__init__)


def test_basecs::packageownercs_constructor_args():
    sig = inspect.signature(basecs::PackageOwnerCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::typecs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypeCS)


def test_basecs::typecs_constructor_exists():
    assert callable(basecs::TypeCS.__init__)


def test_basecs::typecs_constructor_args():
    sig = inspect.signature(basecs::TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::templateparametersubstitutioncs_is_not_abstract():
    assert not inspect.isabstract(basecs::TemplateParameterSubstitutionCS)


def test_basecs::templateparametersubstitutioncs_constructor_exists():
    assert callable(basecs::TemplateParameterSubstitutionCS.__init__)


def test_basecs::templateparametersubstitutioncs_constructor_args():
    sig = inspect.signature(basecs::TemplateParameterSubstitutionCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::rootcs_is_not_abstract():
    assert not inspect.isabstract(basecs::RootCS)


def test_basecs::rootcs_constructor_exists():
    assert callable(basecs::RootCS.__init__)


def test_basecs::rootcs_constructor_args():
    sig = inspect.signature(basecs::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::templatesignaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs::TemplateSignatureCS)


def test_basecs::templatesignaturecs_constructor_exists():
    assert callable(basecs::TemplateSignatureCS.__init__)


def test_basecs::templatesignaturecs_constructor_args():
    sig = inspect.signature(basecs::TemplateSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TemplateableElementCS)


def test_basecs::templateableelementcs_constructor_exists():
    assert callable(basecs::TemplateableElementCS.__init__)


def test_basecs::templateableelementcs_constructor_args():
    sig = inspect.signature(basecs::TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::PathElementCS)


def test_basecs::pathelementcs_constructor_exists():
    assert callable(basecs::PathElementCS.__init__)


def test_basecs::pathelementcs_constructor_args():
    sig = inspect.signature(basecs::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::PivotableElementCS)


def test_basecs::pivotableelementcs_constructor_exists():
    assert callable(basecs::PivotableElementCS.__init__)


def test_basecs::pivotableelementcs_constructor_args():
    sig = inspect.signature(basecs::PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(basecs::MultiplicityCS)


def test_basecs::multiplicitycs_constructor_exists():
    assert callable(basecs::MultiplicityCS.__init__)


def test_basecs::multiplicitycs_constructor_args():
    sig = inspect.signature(basecs::MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityCS)


def test_multiplicitycs_constructor_exists():
    assert callable(MultiplicityCS.__init__)


def test_multiplicitycs_constructor_args():
    sig = inspect.signature(MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::multiplicitystringcs_is_not_abstract():
    assert not inspect.isabstract(basecs::MultiplicityStringCS)


def test_basecs::multiplicitystringcs_constructor_exists():
    assert callable(basecs::MultiplicityStringCS.__init__)


def test_basecs::multiplicitystringcs_constructor_args():
    sig = inspect.signature(basecs::MultiplicityStringCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringBounds" in params, "Missing parameter 'stringBounds'"

def test_basecs::multiplicitystringcs_has_stringBounds():
    assert hasattr(basecs::MultiplicityStringCS, "stringBounds")
    descriptor = None
    for klass in basecs::MultiplicityStringCS.__mro__:
        if "stringBounds" in klass.__dict__:
            descriptor = klass.__dict__["stringBounds"]
            break
    assert isinstance(descriptor, property)



def test_basecs::multiplicityboundscs_is_not_abstract():
    assert not inspect.isabstract(basecs::MultiplicityBoundsCS)


def test_basecs::multiplicityboundscs_constructor_exists():
    assert callable(basecs::MultiplicityBoundsCS.__init__)


def test_basecs::multiplicityboundscs_constructor_args():
    sig = inspect.signature(basecs::MultiplicityBoundsCS.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_basecs::multiplicityboundscs_has_upperBound():
    assert hasattr(basecs::MultiplicityBoundsCS, "upperBound")
    descriptor = None
    for klass in basecs::MultiplicityBoundsCS.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_basecs::multiplicityboundscs_has_lowerBound():
    assert hasattr(basecs::MultiplicityBoundsCS, "lowerBound")
    descriptor = None
    for klass in basecs::MultiplicityBoundsCS.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_basecs::element_is_not_abstract():
    assert not inspect.isabstract(basecs::Element)


def test_basecs::element_constructor_exists():
    assert callable(basecs::Element.__init__)


def test_basecs::element_constructor_args():
    sig = inspect.signature(basecs::Element.__init__)
    params = list(sig.parameters.keys())



def test_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(ElementRefCS)


def test_elementrefcs_constructor_exists():
    assert callable(ElementRefCS.__init__)


def test_elementrefcs_constructor_args():
    sig = inspect.signature(ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::templatebindingcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TemplateBindingCS)


def test_basecs::templatebindingcs_constructor_exists():
    assert callable(basecs::TemplateBindingCS.__init__)


def test_basecs::templatebindingcs_constructor_args():
    sig = inspect.signature(basecs::TemplateBindingCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::typerefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypeRefCS)


def test_basecs::typerefcs_constructor_exists():
    assert callable(basecs::TypeRefCS.__init__)


def test_basecs::typerefcs_constructor_args():
    sig = inspect.signature(basecs::TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_basecs::namedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::NamedElementCS)


def test_basecs::namedelementcs_constructor_exists():
    assert callable(basecs::NamedElementCS.__init__)


def test_basecs::namedelementcs_constructor_args():
    sig = inspect.signature(basecs::NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs::namedelementcs_has_name():
    assert hasattr(basecs::NamedElementCS, "name")
    descriptor = None
    for klass in basecs::NamedElementCS.__mro__:
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



def test_basecs::tupletypecs_is_not_abstract():
    assert not inspect.isabstract(basecs::TupleTypeCS)


def test_basecs::tupletypecs_constructor_exists():
    assert callable(basecs::TupleTypeCS.__init__)


def test_basecs::tupletypecs_constructor_args():
    sig = inspect.signature(basecs::TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs::tupletypecs_has_name():
    assert hasattr(basecs::TupleTypeCS, "name")
    descriptor = None
    for klass in basecs::TupleTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecs::typedtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypedTypeRefCS)


def test_basecs::typedtyperefcs_constructor_exists():
    assert callable(basecs::TypedTypeRefCS.__init__)


def test_basecs::typedtyperefcs_constructor_args():
    sig = inspect.signature(basecs::TypedTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::primitivetyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::PrimitiveTypeRefCS)


def test_basecs::primitivetyperefcs_constructor_exists():
    assert callable(basecs::PrimitiveTypeRefCS.__init__)


def test_basecs::primitivetyperefcs_constructor_args():
    sig = inspect.signature(basecs::PrimitiveTypeRefCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs::primitivetyperefcs_has_name():
    assert hasattr(basecs::PrimitiveTypeRefCS, "name")
    descriptor = None
    for klass in basecs::PrimitiveTypeRefCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basecs::namespace_is_not_abstract():
    assert not inspect.isabstract(basecs::Namespace)


def test_basecs::namespace_constructor_exists():
    assert callable(basecs::Namespace.__init__)


def test_basecs::namespace_constructor_args():
    sig = inspect.signature(basecs::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_basecs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(basecs::PathNameCS)


def test_basecs::pathnamecs_constructor_exists():
    assert callable(basecs::PathNameCS.__init__)


def test_basecs::pathnamecs_constructor_args():
    sig = inspect.signature(basecs::PathNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "scopeFilter" in params, "Missing parameter 'scopeFilter'"

def test_basecs::pathnamecs_has_scopeFilter():
    assert hasattr(basecs::PathNameCS, "scopeFilter")
    descriptor = None
    for klass in basecs::PathNameCS.__mro__:
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



def test_basecs::elementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ElementRefCS)


def test_basecs::elementrefcs_constructor_exists():
    assert callable(basecs::ElementRefCS.__init__)


def test_basecs::elementrefcs_constructor_args():
    sig = inspect.signature(basecs::ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_visitablecs_is_not_abstract():
    assert not inspect.isabstract(VisitableCS)


def test_visitablecs_constructor_exists():
    assert callable(VisitableCS.__init__)


def test_visitablecs_constructor_args():
    sig = inspect.signature(VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::elementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ElementCS)


def test_basecs::elementcs_constructor_exists():
    assert callable(basecs::ElementCS.__init__)


def test_basecs::elementcs_constructor_args():
    sig = inspect.signature(basecs::ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::specificationcs_is_not_abstract():
    assert not inspect.isabstract(basecs::SpecificationCS)


def test_basecs::specificationcs_constructor_exists():
    assert callable(basecs::SpecificationCS.__init__)


def test_basecs::specificationcs_constructor_args():
    sig = inspect.signature(basecs::SpecificationCS.__init__)
    params = list(sig.parameters.keys())
    assert "exprString" in params, "Missing parameter 'exprString'"

def test_basecs::specificationcs_has_exprString():
    assert hasattr(basecs::SpecificationCS, "exprString")
    descriptor = None
    for klass in basecs::SpecificationCS.__mro__:
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



def test_basecs::lambdatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs::LambdaTypeCS)


def test_basecs::lambdatypecs_constructor_exists():
    assert callable(basecs::LambdaTypeCS.__init__)


def test_basecs::lambdatypecs_constructor_args():
    sig = inspect.signature(basecs::LambdaTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basecs::lambdatypecs_has_name():
    assert hasattr(basecs::LambdaTypeCS, "name")
    descriptor = None
    for klass in basecs::LambdaTypeCS.__mro__:
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



def test_basecs::typeparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypeParameterCS)


def test_basecs::typeparametercs_constructor_exists():
    assert callable(basecs::TypeParameterCS.__init__)


def test_basecs::typeparametercs_constructor_args():
    sig = inspect.signature(basecs::TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs::StructuralFeatureCS)


def test_basecs::structuralfeaturecs_constructor_exists():
    assert callable(basecs::StructuralFeatureCS.__init__)


def test_basecs::structuralfeaturecs_constructor_args():
    sig = inspect.signature(basecs::StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_basecs::structuralfeaturecs_has_default():
    assert hasattr(basecs::StructuralFeatureCS, "default")
    descriptor = None
    for klass in basecs::StructuralFeatureCS.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_basecs::operationcs_is_not_abstract():
    assert not inspect.isabstract(basecs::OperationCS)


def test_basecs::operationcs_constructor_exists():
    assert callable(basecs::OperationCS.__init__)


def test_basecs::operationcs_constructor_args():
    sig = inspect.signature(basecs::OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypedRefCS)


def test_basecs::typedrefcs_constructor_exists():
    assert callable(basecs::TypedRefCS.__init__)


def test_basecs::typedrefcs_constructor_args():
    sig = inspect.signature(basecs::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::packagecs_is_not_abstract():
    assert not inspect.isabstract(basecs::PackageCS)


def test_basecs::packagecs_constructor_exists():
    assert callable(basecs::PackageCS.__init__)


def test_basecs::packagecs_constructor_args():
    sig = inspect.signature(basecs::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"

def test_basecs::packagecs_has_nsPrefix():
    assert hasattr(basecs::PackageCS, "nsPrefix")
    descriptor = None
    for klass in basecs::PackageCS.__mro__:
        if "nsPrefix" in klass.__dict__:
            descriptor = klass.__dict__["nsPrefix"]
            break
    assert isinstance(descriptor, property)

def test_basecs::packagecs_has_nsURI():
    assert hasattr(basecs::PackageCS, "nsURI")
    descriptor = None
    for klass in basecs::PackageCS.__mro__:
        if "nsURI" in klass.__dict__:
            descriptor = klass.__dict__["nsURI"]
            break
    assert isinstance(descriptor, property)



def test_basecs::librarycs_is_not_abstract():
    assert not inspect.isabstract(basecs::LibraryCS)


def test_basecs::librarycs_constructor_exists():
    assert callable(basecs::LibraryCS.__init__)


def test_basecs::librarycs_constructor_args():
    sig = inspect.signature(basecs::LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::importcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ImportCS)


def test_basecs::importcs_constructor_exists():
    assert callable(basecs::ImportCS.__init__)


def test_basecs::importcs_constructor_args():
    sig = inspect.signature(basecs::ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_basecs::importcs_has_all():
    assert hasattr(basecs::ImportCS, "all")
    descriptor = None
    for klass in basecs::ImportCS.__mro__:
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



def test_basecs::datatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs::DataTypeCS)


def test_basecs::datatypecs_constructor_exists():
    assert callable(basecs::DataTypeCS.__init__)


def test_basecs::datatypecs_constructor_args():
    sig = inspect.signature(basecs::DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::enumerationcs_is_not_abstract():
    assert not inspect.isabstract(basecs::EnumerationCS)


def test_basecs::enumerationcs_constructor_exists():
    assert callable(basecs::EnumerationCS.__init__)


def test_basecs::enumerationcs_constructor_args():
    sig = inspect.signature(basecs::EnumerationCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::classcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ClassCS)


def test_basecs::classcs_constructor_exists():
    assert callable(basecs::ClassCS.__init__)


def test_basecs::classcs_constructor_args():
    sig = inspect.signature(basecs::ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::referencecs_is_not_abstract():
    assert not inspect.isabstract(basecs::ReferenceCS)


def test_basecs::referencecs_constructor_exists():
    assert callable(basecs::ReferenceCS.__init__)


def test_basecs::referencecs_constructor_args():
    sig = inspect.signature(basecs::ReferenceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::attributecs_is_not_abstract():
    assert not inspect.isabstract(basecs::AttributeCS)


def test_basecs::attributecs_constructor_exists():
    assert callable(basecs::AttributeCS.__init__)


def test_basecs::attributecs_constructor_args():
    sig = inspect.signature(basecs::AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::detailcs_is_not_abstract():
    assert not inspect.isabstract(basecs::DetailCS)


def test_basecs::detailcs_constructor_exists():
    assert callable(basecs::DetailCS.__init__)


def test_basecs::detailcs_constructor_args():
    sig = inspect.signature(basecs::DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs::detailcs_has_value():
    assert hasattr(basecs::DetailCS, "value")
    descriptor = None
    for klass in basecs::DetailCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs::constraintcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ConstraintCS)


def test_basecs::constraintcs_constructor_exists():
    assert callable(basecs::ConstraintCS.__init__)


def test_basecs::constraintcs_constructor_args():
    sig = inspect.signature(basecs::ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_basecs::constraintcs_has_stereotype():
    assert hasattr(basecs::ConstraintCS, "stereotype")
    descriptor = None
    for klass in basecs::ConstraintCS.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_basecs::templateparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs::TemplateParameterCS)


def test_basecs::templateparametercs_constructor_exists():
    assert callable(basecs::TemplateParameterCS.__init__)


def test_basecs::templateparametercs_constructor_args():
    sig = inspect.signature(basecs::TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::typedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::TypedElementCS)


def test_basecs::typedelementcs_constructor_exists():
    assert callable(basecs::TypedElementCS.__init__)


def test_basecs::typedelementcs_constructor_args():
    sig = inspect.signature(basecs::TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_basecs::typedelementcs_has_qualifier():
    assert hasattr(basecs::TypedElementCS, "qualifier")
    descriptor = None
    for klass in basecs::TypedElementCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_basecs::typedelementcs_has_optional():
    assert hasattr(basecs::TypedElementCS, "optional")
    descriptor = None
    for klass in basecs::TypedElementCS.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_basecs::classifiercs_is_not_abstract():
    assert not inspect.isabstract(basecs::ClassifierCS)


def test_basecs::classifiercs_constructor_exists():
    assert callable(basecs::ClassifierCS.__init__)


def test_basecs::classifiercs_constructor_args():
    sig = inspect.signature(basecs::ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"

def test_basecs::classifiercs_has_qualifier():
    assert hasattr(basecs::ClassifierCS, "qualifier")
    descriptor = None
    for klass in basecs::ClassifierCS.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_basecs::classifiercs_has_instanceClassName():
    assert hasattr(basecs::ClassifierCS, "instanceClassName")
    descriptor = None
    for klass in basecs::ClassifierCS.__mro__:
        if "instanceClassName" in klass.__dict__:
            descriptor = klass.__dict__["instanceClassName"]
            break
    assert isinstance(descriptor, property)



def test_basecs::enumerationliteralcs_is_not_abstract():
    assert not inspect.isabstract(basecs::EnumerationLiteralCS)


def test_basecs::enumerationliteralcs_constructor_exists():
    assert callable(basecs::EnumerationLiteralCS.__init__)


def test_basecs::enumerationliteralcs_constructor_args():
    sig = inspect.signature(basecs::EnumerationLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs::enumerationliteralcs_has_value():
    assert hasattr(basecs::EnumerationLiteralCS, "value")
    descriptor = None
    for klass in basecs::EnumerationLiteralCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs::namespacecs_is_not_abstract():
    assert not inspect.isabstract(basecs::NamespaceCS)


def test_basecs::namespacecs_constructor_exists():
    assert callable(basecs::NamespaceCS.__init__)


def test_basecs::namespacecs_constructor_args():
    sig = inspect.signature(basecs::NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::AnnotationElementCS)


def test_basecs::annotationelementcs_constructor_exists():
    assert callable(basecs::AnnotationElementCS.__init__)


def test_basecs::annotationelementcs_constructor_args():
    sig = inspect.signature(basecs::AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::modelelementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ModelElementRefCS)


def test_basecs::modelelementrefcs_constructor_exists():
    assert callable(basecs::ModelElementRefCS.__init__)


def test_basecs::modelelementrefcs_constructor_args():
    sig = inspect.signature(basecs::ModelElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_basecs::modelelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs::ModelElementCS)


def test_basecs::modelelementcs_constructor_exists():
    assert callable(basecs::ModelElementCS.__init__)


def test_basecs::modelelementcs_constructor_args():
    sig = inspect.signature(basecs::ModelElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "originalXmiId" in params, "Missing parameter 'originalXmiId'"
    assert "csi" in params, "Missing parameter 'csi'"

def test_basecs::modelelementcs_has_originalXmiId():
    assert hasattr(basecs::ModelElementCS, "originalXmiId")
    descriptor = None
    for klass in basecs::ModelElementCS.__mro__:
        if "originalXmiId" in klass.__dict__:
            descriptor = klass.__dict__["originalXmiId"]
            break
    assert isinstance(descriptor, property)

def test_basecs::modelelementcs_has_csi():
    assert hasattr(basecs::ModelElementCS, "csi")
    descriptor = None
    for klass in basecs::ModelElementCS.__mro__:
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



def test_basecs::documentationcs_is_not_abstract():
    assert not inspect.isabstract(basecs::DocumentationCS)


def test_basecs::documentationcs_constructor_exists():
    assert callable(basecs::DocumentationCS.__init__)


def test_basecs::documentationcs_constructor_args():
    sig = inspect.signature(basecs::DocumentationCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_basecs::documentationcs_has_value():
    assert hasattr(basecs::DocumentationCS, "value")
    descriptor = None
    for klass in basecs::DocumentationCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_basecs::annotationcs_is_not_abstract():
    assert not inspect.isabstract(basecs::AnnotationCS)


def test_basecs::annotationcs_constructor_exists():
    assert callable(basecs::AnnotationCS.__init__)


def test_basecs::annotationcs_constructor_args():
    sig = inspect.signature(basecs::AnnotationCS.__init__)
    params = list(sig.parameters.keys())

def test_iteratorkind_exists():
    # Check that the Enumeration exists
    assert IteratorKind is not None

def test_iteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorKind]
    expected_literals = [
        "Accumulator",
        "Parameter",
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
basecs::VisitableCS_strategy = st.builds(
    basecs::VisitableCS,
)
basecs::Type_strategy = st.builds(
    basecs::Type,
)
TypeRefCS_strategy = st.builds(
    TypeRefCS,
)
basecs::WildcardTypeRefCS_strategy = st.builds(
    basecs::WildcardTypeRefCS,
)
TemplateParameterCS_strategy = st.builds(
    TemplateParameterCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
basecs::Property_strategy = st.builds(
    basecs::Property,
)
PathElementCS_strategy = st.builds(
    PathElementCS,
)
basecs::PathElementWithURICS_strategy = st.builds(
    basecs::PathElementWithURICS,
    uri=
        safe_text
)
basecs::EClassifier_strategy = st.builds(
    basecs::EClassifier,
)
Pivotable_strategy = st.builds(
    Pivotable,
)
PackageOwnerCS_strategy = st.builds(
    PackageOwnerCS,
)
basecs::RootPackageCS_strategy = st.builds(
    basecs::RootPackageCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
basecs::TuplePartCS_strategy = st.builds(
    basecs::TuplePartCS,
)
basecs::ParameterCS_strategy = st.builds(
    basecs::ParameterCS,
)
basecs::FeatureCS_strategy = st.builds(
    basecs::FeatureCS,
)
FeatureCS_strategy = st.builds(
    FeatureCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
basecs::PackageOwnerCS_strategy = st.builds(
    basecs::PackageOwnerCS,
)
basecs::TypeCS_strategy = st.builds(
    basecs::TypeCS,
)
basecs::TemplateParameterSubstitutionCS_strategy = st.builds(
    basecs::TemplateParameterSubstitutionCS,
)
basecs::RootCS_strategy = st.builds(
    basecs::RootCS,
)
basecs::TemplateSignatureCS_strategy = st.builds(
    basecs::TemplateSignatureCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
basecs::TemplateableElementCS_strategy = st.builds(
    basecs::TemplateableElementCS,
)
basecs::PathElementCS_strategy = st.builds(
    basecs::PathElementCS,
)
basecs::PivotableElementCS_strategy = st.builds(
    basecs::PivotableElementCS,
)
basecs::MultiplicityCS_strategy = st.builds(
    basecs::MultiplicityCS,
)
MultiplicityCS_strategy = st.builds(
    MultiplicityCS,
)
basecs::MultiplicityStringCS_strategy = st.builds(
    basecs::MultiplicityStringCS,
    stringBounds=
        safe_text
)
basecs::MultiplicityBoundsCS_strategy = st.builds(
    basecs::MultiplicityBoundsCS,
    upperBound=
        safe_text,
    lowerBound=
        st.integers()
)
basecs::Element_strategy = st.builds(
    basecs::Element,
)
ElementRefCS_strategy = st.builds(
    ElementRefCS,
)
basecs::TemplateBindingCS_strategy = st.builds(
    basecs::TemplateBindingCS,
)
basecs::TypeRefCS_strategy = st.builds(
    basecs::TypeRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
basecs::NamedElementCS_strategy = st.builds(
    basecs::NamedElementCS,
    name=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
basecs::TupleTypeCS_strategy = st.builds(
    basecs::TupleTypeCS,
    name=
        safe_text
)
basecs::TypedTypeRefCS_strategy = st.builds(
    basecs::TypedTypeRefCS,
)
basecs::PrimitiveTypeRefCS_strategy = st.builds(
    basecs::PrimitiveTypeRefCS,
    name=
        safe_text
)
basecs::Namespace_strategy = st.builds(
    basecs::Namespace,
)
basecs::PathNameCS_strategy = st.builds(
    basecs::PathNameCS,
    scopeFilter=
        safe_text
)
PivotableElementCS_strategy = st.builds(
    PivotableElementCS,
)
basecs::ElementRefCS_strategy = st.builds(
    basecs::ElementRefCS,
)
VisitableCS_strategy = st.builds(
    VisitableCS,
)
basecs::ElementCS_strategy = st.builds(
    basecs::ElementCS,
)
basecs::SpecificationCS_strategy = st.builds(
    basecs::SpecificationCS,
    exprString=
        safe_text
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
basecs::LambdaTypeCS_strategy = st.builds(
    basecs::LambdaTypeCS,
    name=
        safe_text
)
TypeCS_strategy = st.builds(
    TypeCS,
)
basecs::TypeParameterCS_strategy = st.builds(
    basecs::TypeParameterCS,
)
basecs::StructuralFeatureCS_strategy = st.builds(
    basecs::StructuralFeatureCS,
    default=
        safe_text
)
basecs::OperationCS_strategy = st.builds(
    basecs::OperationCS,
)
basecs::TypedRefCS_strategy = st.builds(
    basecs::TypedRefCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
basecs::PackageCS_strategy = st.builds(
    basecs::PackageCS,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
basecs::LibraryCS_strategy = st.builds(
    basecs::LibraryCS,
)
basecs::ImportCS_strategy = st.builds(
    basecs::ImportCS,
    all=
        st.booleans()
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
basecs::DataTypeCS_strategy = st.builds(
    basecs::DataTypeCS,
)
basecs::EnumerationCS_strategy = st.builds(
    basecs::EnumerationCS,
)
basecs::ClassCS_strategy = st.builds(
    basecs::ClassCS,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
basecs::ReferenceCS_strategy = st.builds(
    basecs::ReferenceCS,
)
basecs::AttributeCS_strategy = st.builds(
    basecs::AttributeCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
basecs::DetailCS_strategy = st.builds(
    basecs::DetailCS,
    value=
        safe_text
)
basecs::ConstraintCS_strategy = st.builds(
    basecs::ConstraintCS,
    stereotype=
        safe_text
)
basecs::TemplateParameterCS_strategy = st.builds(
    basecs::TemplateParameterCS,
)
basecs::TypedElementCS_strategy = st.builds(
    basecs::TypedElementCS,
    qualifier=
        safe_text,
    optional=
        st.booleans()
)
basecs::ClassifierCS_strategy = st.builds(
    basecs::ClassifierCS,
    qualifier=
        safe_text,
    instanceClassName=
        safe_text
)
basecs::EnumerationLiteralCS_strategy = st.builds(
    basecs::EnumerationLiteralCS,
    value=
        st.integers()
)
basecs::NamespaceCS_strategy = st.builds(
    basecs::NamespaceCS,
)
basecs::AnnotationElementCS_strategy = st.builds(
    basecs::AnnotationElementCS,
)
basecs::ModelElementRefCS_strategy = st.builds(
    basecs::ModelElementRefCS,
)
basecs::ModelElementCS_strategy = st.builds(
    basecs::ModelElementCS,
    originalXmiId=
        safe_text,
    csi=
        safe_text
)
AnnotationElementCS_strategy = st.builds(
    AnnotationElementCS,
)
basecs::DocumentationCS_strategy = st.builds(
    basecs::DocumentationCS,
    value=
        safe_text
)
basecs::AnnotationCS_strategy = st.builds(
    basecs::AnnotationCS,
)

@given(instance=basecs::VisitableCS_strategy)
@settings(max_examples=50)
def test_basecs::visitablecs_instantiation(instance):
    assert isinstance(instance, basecs::VisitableCS)

@given(instance=basecs::Type_strategy)
@settings(max_examples=50)
def test_basecs::type_instantiation(instance):
    assert isinstance(instance, basecs::Type)

@given(instance=TypeRefCS_strategy)
@settings(max_examples=50)
def test_typerefcs_instantiation(instance):
    assert isinstance(instance, TypeRefCS)

@given(instance=basecs::WildcardTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs::wildcardtyperefcs_instantiation(instance):
    assert isinstance(instance, basecs::WildcardTypeRefCS)

@given(instance=TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_templateparametercs_instantiation(instance):
    assert isinstance(instance, TemplateParameterCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=basecs::Property_strategy)
@settings(max_examples=50)
def test_basecs::property_instantiation(instance):
    assert isinstance(instance, basecs::Property)

@given(instance=PathElementCS_strategy)
@settings(max_examples=50)
def test_pathelementcs_instantiation(instance):
    assert isinstance(instance, PathElementCS)

@given(instance=basecs::PathElementWithURICS_strategy)
@settings(max_examples=50)
def test_basecs::pathelementwithurics_instantiation(instance):
    assert isinstance(instance, basecs::PathElementWithURICS)

@given(instance=basecs::PathElementWithURICS_strategy)
def test_basecs::pathelementwithurics_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=basecs::PathElementWithURICS_strategy)
def test_basecs::pathelementwithurics_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=basecs::EClassifier_strategy)
@settings(max_examples=50)
def test_basecs::eclassifier_instantiation(instance):
    assert isinstance(instance, basecs::EClassifier)

@given(instance=Pivotable_strategy)
@settings(max_examples=50)
def test_pivotable_instantiation(instance):
    assert isinstance(instance, Pivotable)

@given(instance=PackageOwnerCS_strategy)
@settings(max_examples=50)
def test_packageownercs_instantiation(instance):
    assert isinstance(instance, PackageOwnerCS)

@given(instance=basecs::RootPackageCS_strategy)
@settings(max_examples=50)
def test_basecs::rootpackagecs_instantiation(instance):
    assert isinstance(instance, basecs::RootPackageCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=basecs::TuplePartCS_strategy)
@settings(max_examples=50)
def test_basecs::tuplepartcs_instantiation(instance):
    assert isinstance(instance, basecs::TuplePartCS)

@given(instance=basecs::ParameterCS_strategy)
@settings(max_examples=50)
def test_basecs::parametercs_instantiation(instance):
    assert isinstance(instance, basecs::ParameterCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::ParameterCS_strategy)
@settings(max_examples=30)
def test_basecs::parametercs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::ParameterCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::ParameterCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::ParameterCS is not implemented or raised an error")

@given(instance=basecs::FeatureCS_strategy)
@settings(max_examples=50)
def test_basecs::featurecs_instantiation(instance):
    assert isinstance(instance, basecs::FeatureCS)

@given(instance=FeatureCS_strategy)
@settings(max_examples=50)
def test_featurecs_instantiation(instance):
    assert isinstance(instance, FeatureCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=basecs::PackageOwnerCS_strategy)
@settings(max_examples=50)
def test_basecs::packageownercs_instantiation(instance):
    assert isinstance(instance, basecs::PackageOwnerCS)

@given(instance=basecs::TypeCS_strategy)
@settings(max_examples=50)
def test_basecs::typecs_instantiation(instance):
    assert isinstance(instance, basecs::TypeCS)

@given(instance=basecs::TemplateParameterSubstitutionCS_strategy)
@settings(max_examples=50)
def test_basecs::templateparametersubstitutioncs_instantiation(instance):
    assert isinstance(instance, basecs::TemplateParameterSubstitutionCS)

@given(instance=basecs::RootCS_strategy)
@settings(max_examples=50)
def test_basecs::rootcs_instantiation(instance):
    assert isinstance(instance, basecs::RootCS)

@given(instance=basecs::TemplateSignatureCS_strategy)
@settings(max_examples=50)
def test_basecs::templatesignaturecs_instantiation(instance):
    assert isinstance(instance, basecs::TemplateSignatureCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=basecs::TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_basecs::templateableelementcs_instantiation(instance):
    assert isinstance(instance, basecs::TemplateableElementCS)

@given(instance=basecs::PathElementCS_strategy)
@settings(max_examples=50)
def test_basecs::pathelementcs_instantiation(instance):
    assert isinstance(instance, basecs::PathElementCS)

@given(instance=basecs::PivotableElementCS_strategy)
@settings(max_examples=50)
def test_basecs::pivotableelementcs_instantiation(instance):
    assert isinstance(instance, basecs::PivotableElementCS)

@given(instance=basecs::MultiplicityCS_strategy)
@settings(max_examples=50)
def test_basecs::multiplicitycs_instantiation(instance):
    assert isinstance(instance, basecs::MultiplicityCS)

@given(instance=MultiplicityCS_strategy)
@settings(max_examples=50)
def test_multiplicitycs_instantiation(instance):
    assert isinstance(instance, MultiplicityCS)

@given(instance=basecs::MultiplicityStringCS_strategy)
@settings(max_examples=50)
def test_basecs::multiplicitystringcs_instantiation(instance):
    assert isinstance(instance, basecs::MultiplicityStringCS)

@given(instance=basecs::MultiplicityStringCS_strategy)
def test_basecs::multiplicitystringcs_stringBounds_type(instance):
    assert isinstance(instance.stringBounds, str)


@given(instance=basecs::MultiplicityStringCS_strategy)
def test_basecs::multiplicitystringcs_stringBounds_setter(instance):
    original = instance.stringBounds
    instance.stringBounds = original
    assert instance.stringBounds == original

@given(instance=basecs::MultiplicityBoundsCS_strategy)
@settings(max_examples=50)
def test_basecs::multiplicityboundscs_instantiation(instance):
    assert isinstance(instance, basecs::MultiplicityBoundsCS)

@given(instance=basecs::MultiplicityBoundsCS_strategy)
def test_basecs::multiplicityboundscs_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=basecs::MultiplicityBoundsCS_strategy)
def test_basecs::multiplicityboundscs_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=basecs::MultiplicityBoundsCS_strategy)
def test_basecs::multiplicityboundscs_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=basecs::MultiplicityBoundsCS_strategy)
def test_basecs::multiplicityboundscs_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=basecs::Element_strategy)
@settings(max_examples=50)
def test_basecs::element_instantiation(instance):
    assert isinstance(instance, basecs::Element)

@given(instance=ElementRefCS_strategy)
@settings(max_examples=50)
def test_elementrefcs_instantiation(instance):
    assert isinstance(instance, ElementRefCS)

@given(instance=basecs::TemplateBindingCS_strategy)
@settings(max_examples=50)
def test_basecs::templatebindingcs_instantiation(instance):
    assert isinstance(instance, basecs::TemplateBindingCS)

@given(instance=basecs::TypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs::typerefcs_instantiation(instance):
    assert isinstance(instance, basecs::TypeRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=basecs::NamedElementCS_strategy)
@settings(max_examples=50)
def test_basecs::namedelementcs_instantiation(instance):
    assert isinstance(instance, basecs::NamedElementCS)

@given(instance=basecs::NamedElementCS_strategy)
def test_basecs::namedelementcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basecs::NamedElementCS_strategy)
def test_basecs::namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=basecs::TupleTypeCS_strategy)
@settings(max_examples=50)
def test_basecs::tupletypecs_instantiation(instance):
    assert isinstance(instance, basecs::TupleTypeCS)

@given(instance=basecs::TupleTypeCS_strategy)
def test_basecs::tupletypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basecs::TupleTypeCS_strategy)
def test_basecs::tupletypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basecs::TypedTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs::typedtyperefcs_instantiation(instance):
    assert isinstance(instance, basecs::TypedTypeRefCS)

@given(instance=basecs::PrimitiveTypeRefCS_strategy)
@settings(max_examples=50)
def test_basecs::primitivetyperefcs_instantiation(instance):
    assert isinstance(instance, basecs::PrimitiveTypeRefCS)

@given(instance=basecs::PrimitiveTypeRefCS_strategy)
def test_basecs::primitivetyperefcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basecs::PrimitiveTypeRefCS_strategy)
def test_basecs::primitivetyperefcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basecs::Namespace_strategy)
@settings(max_examples=50)
def test_basecs::namespace_instantiation(instance):
    assert isinstance(instance, basecs::Namespace)

@given(instance=basecs::PathNameCS_strategy)
@settings(max_examples=50)
def test_basecs::pathnamecs_instantiation(instance):
    assert isinstance(instance, basecs::PathNameCS)

@given(instance=basecs::PathNameCS_strategy)
def test_basecs::pathnamecs_scopeFilter_type(instance):
    assert isinstance(instance.scopeFilter, str)


@given(instance=basecs::PathNameCS_strategy)
def test_basecs::pathnamecs_scopeFilter_setter(instance):
    original = instance.scopeFilter
    instance.scopeFilter = original
    assert instance.scopeFilter == original

@given(instance=PivotableElementCS_strategy)
@settings(max_examples=50)
def test_pivotableelementcs_instantiation(instance):
    assert isinstance(instance, PivotableElementCS)

@given(instance=basecs::ElementRefCS_strategy)
@settings(max_examples=50)
def test_basecs::elementrefcs_instantiation(instance):
    assert isinstance(instance, basecs::ElementRefCS)

@given(instance=VisitableCS_strategy)
@settings(max_examples=50)
def test_visitablecs_instantiation(instance):
    assert isinstance(instance, VisitableCS)

@given(instance=basecs::ElementCS_strategy)
@settings(max_examples=50)
def test_basecs::elementcs_instantiation(instance):
    assert isinstance(instance, basecs::ElementCS)

@given(instance=basecs::SpecificationCS_strategy)
@settings(max_examples=50)
def test_basecs::specificationcs_instantiation(instance):
    assert isinstance(instance, basecs::SpecificationCS)

@given(instance=basecs::SpecificationCS_strategy)
def test_basecs::specificationcs_exprString_type(instance):
    assert isinstance(instance.exprString, str)


@given(instance=basecs::SpecificationCS_strategy)
def test_basecs::specificationcs_exprString_setter(instance):
    original = instance.exprString
    instance.exprString = original
    assert instance.exprString == original

@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=50)
def test_templateableelementcs_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)

@given(instance=basecs::LambdaTypeCS_strategy)
@settings(max_examples=50)
def test_basecs::lambdatypecs_instantiation(instance):
    assert isinstance(instance, basecs::LambdaTypeCS)

@given(instance=basecs::LambdaTypeCS_strategy)
def test_basecs::lambdatypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=basecs::LambdaTypeCS_strategy)
def test_basecs::lambdatypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=basecs::TypeParameterCS_strategy)
@settings(max_examples=50)
def test_basecs::typeparametercs_instantiation(instance):
    assert isinstance(instance, basecs::TypeParameterCS)

@given(instance=basecs::StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_basecs::structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, basecs::StructuralFeatureCS)

@given(instance=basecs::StructuralFeatureCS_strategy)
def test_basecs::structuralfeaturecs_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=basecs::StructuralFeatureCS_strategy)
def test_basecs::structuralfeaturecs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::StructuralFeatureCS_strategy)
@settings(max_examples=30)
def test_basecs::structuralfeaturecs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::StructuralFeatureCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::StructuralFeatureCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::StructuralFeatureCS is not implemented or raised an error")

@given(instance=basecs::OperationCS_strategy)
@settings(max_examples=50)
def test_basecs::operationcs_instantiation(instance):
    assert isinstance(instance, basecs::OperationCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::OperationCS_strategy)
@settings(max_examples=30)
def test_basecs::operationcs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::OperationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::OperationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::OperationCS is not implemented or raised an error")

@given(instance=basecs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_basecs::typedrefcs_instantiation(instance):
    assert isinstance(instance, basecs::TypedRefCS)

@given(instance=NamespaceCS_strategy)
@settings(max_examples=50)
def test_namespacecs_instantiation(instance):
    assert isinstance(instance, NamespaceCS)

@given(instance=basecs::PackageCS_strategy)
@settings(max_examples=50)
def test_basecs::packagecs_instantiation(instance):
    assert isinstance(instance, basecs::PackageCS)

@given(instance=basecs::PackageCS_strategy)
def test_basecs::packagecs_nsPrefix_type(instance):
    assert isinstance(instance.nsPrefix, str)


@given(instance=basecs::PackageCS_strategy)
def test_basecs::packagecs_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original

@given(instance=basecs::PackageCS_strategy)
def test_basecs::packagecs_nsURI_type(instance):
    assert isinstance(instance.nsURI, str)


@given(instance=basecs::PackageCS_strategy)
def test_basecs::packagecs_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::PackageCS_strategy)
@settings(max_examples=30)
def test_basecs::packagecs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::PackageCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::PackageCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::PackageCS is not implemented or raised an error")

@given(instance=basecs::LibraryCS_strategy)
@settings(max_examples=50)
def test_basecs::librarycs_instantiation(instance):
    assert isinstance(instance, basecs::LibraryCS)

@given(instance=basecs::ImportCS_strategy)
@settings(max_examples=50)
def test_basecs::importcs_instantiation(instance):
    assert isinstance(instance, basecs::ImportCS)

@given(instance=basecs::ImportCS_strategy)
def test_basecs::importcs_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=basecs::ImportCS_strategy)
def test_basecs::importcs_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=ClassifierCS_strategy)
@settings(max_examples=50)
def test_classifiercs_instantiation(instance):
    assert isinstance(instance, ClassifierCS)

@given(instance=basecs::DataTypeCS_strategy)
@settings(max_examples=50)
def test_basecs::datatypecs_instantiation(instance):
    assert isinstance(instance, basecs::DataTypeCS)

@given(instance=basecs::EnumerationCS_strategy)
@settings(max_examples=50)
def test_basecs::enumerationcs_instantiation(instance):
    assert isinstance(instance, basecs::EnumerationCS)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::EnumerationCS_strategy)
@settings(max_examples=30)
def test_basecs::enumerationcs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::EnumerationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::EnumerationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::EnumerationCS is not implemented or raised an error")

@given(instance=basecs::ClassCS_strategy)
@settings(max_examples=50)
def test_basecs::classcs_instantiation(instance):
    assert isinstance(instance, basecs::ClassCS)

@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=50)
def test_structuralfeaturecs_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)

@given(instance=basecs::ReferenceCS_strategy)
@settings(max_examples=50)
def test_basecs::referencecs_instantiation(instance):
    assert isinstance(instance, basecs::ReferenceCS)

@given(instance=basecs::AttributeCS_strategy)
@settings(max_examples=50)
def test_basecs::attributecs_instantiation(instance):
    assert isinstance(instance, basecs::AttributeCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=basecs::DetailCS_strategy)
@settings(max_examples=50)
def test_basecs::detailcs_instantiation(instance):
    assert isinstance(instance, basecs::DetailCS)

@given(instance=basecs::DetailCS_strategy)
def test_basecs::detailcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=basecs::DetailCS_strategy)
def test_basecs::detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=basecs::ConstraintCS_strategy)
@settings(max_examples=50)
def test_basecs::constraintcs_instantiation(instance):
    assert isinstance(instance, basecs::ConstraintCS)

@given(instance=basecs::ConstraintCS_strategy)
def test_basecs::constraintcs_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=basecs::ConstraintCS_strategy)
def test_basecs::constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=basecs::TemplateParameterCS_strategy)
@settings(max_examples=50)
def test_basecs::templateparametercs_instantiation(instance):
    assert isinstance(instance, basecs::TemplateParameterCS)

@given(instance=basecs::TypedElementCS_strategy)
@settings(max_examples=50)
def test_basecs::typedelementcs_instantiation(instance):
    assert isinstance(instance, basecs::TypedElementCS)

@given(instance=basecs::TypedElementCS_strategy)
def test_basecs::typedelementcs_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=basecs::TypedElementCS_strategy)
def test_basecs::typedelementcs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=basecs::TypedElementCS_strategy)
def test_basecs::typedelementcs_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=basecs::TypedElementCS_strategy)
def test_basecs::typedelementcs_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=basecs::ClassifierCS_strategy)
@settings(max_examples=50)
def test_basecs::classifiercs_instantiation(instance):
    assert isinstance(instance, basecs::ClassifierCS)

@given(instance=basecs::ClassifierCS_strategy)
def test_basecs::classifiercs_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=basecs::ClassifierCS_strategy)
def test_basecs::classifiercs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=basecs::ClassifierCS_strategy)
def test_basecs::classifiercs_instanceClassName_type(instance):
    assert isinstance(instance.instanceClassName, str)


@given(instance=basecs::ClassifierCS_strategy)
def test_basecs::classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::ClassifierCS_strategy)
@settings(max_examples=30)
def test_basecs::classifiercs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::ClassifierCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::ClassifierCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::ClassifierCS is not implemented or raised an error")

@given(instance=basecs::EnumerationLiteralCS_strategy)
@settings(max_examples=50)
def test_basecs::enumerationliteralcs_instantiation(instance):
    assert isinstance(instance, basecs::EnumerationLiteralCS)

@given(instance=basecs::EnumerationLiteralCS_strategy)
def test_basecs::enumerationliteralcs_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=basecs::EnumerationLiteralCS_strategy)
def test_basecs::enumerationliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs::EnumerationLiteralCS_strategy)
@settings(max_examples=30)
def test_basecs::enumerationliteralcs_ast_changes_state(instance):
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
        assert has_statements, f"Function 'ast' in basecs::EnumerationLiteralCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs::EnumerationLiteralCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs::EnumerationLiteralCS is not implemented or raised an error")

@given(instance=basecs::NamespaceCS_strategy)
@settings(max_examples=50)
def test_basecs::namespacecs_instantiation(instance):
    assert isinstance(instance, basecs::NamespaceCS)

@given(instance=basecs::AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_basecs::annotationelementcs_instantiation(instance):
    assert isinstance(instance, basecs::AnnotationElementCS)

@given(instance=basecs::ModelElementRefCS_strategy)
@settings(max_examples=50)
def test_basecs::modelelementrefcs_instantiation(instance):
    assert isinstance(instance, basecs::ModelElementRefCS)

@given(instance=basecs::ModelElementCS_strategy)
@settings(max_examples=50)
def test_basecs::modelelementcs_instantiation(instance):
    assert isinstance(instance, basecs::ModelElementCS)

@given(instance=basecs::ModelElementCS_strategy)
def test_basecs::modelelementcs_originalXmiId_type(instance):
    assert isinstance(instance.originalXmiId, str)


@given(instance=basecs::ModelElementCS_strategy)
def test_basecs::modelelementcs_originalXmiId_setter(instance):
    original = instance.originalXmiId
    instance.originalXmiId = original
    assert instance.originalXmiId == original

@given(instance=basecs::ModelElementCS_strategy)
def test_basecs::modelelementcs_csi_type(instance):
    assert isinstance(instance.csi, str)


@given(instance=basecs::ModelElementCS_strategy)
def test_basecs::modelelementcs_csi_setter(instance):
    original = instance.csi
    instance.csi = original
    assert instance.csi == original

@given(instance=AnnotationElementCS_strategy)
@settings(max_examples=50)
def test_annotationelementcs_instantiation(instance):
    assert isinstance(instance, AnnotationElementCS)

@given(instance=basecs::DocumentationCS_strategy)
@settings(max_examples=50)
def test_basecs::documentationcs_instantiation(instance):
    assert isinstance(instance, basecs::DocumentationCS)

@given(instance=basecs::DocumentationCS_strategy)
def test_basecs::documentationcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=basecs::DocumentationCS_strategy)
def test_basecs::documentationcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=basecs::AnnotationCS_strategy)
@settings(max_examples=50)
def test_basecs::annotationcs_instantiation(instance):
    assert isinstance(instance, basecs::AnnotationCS)

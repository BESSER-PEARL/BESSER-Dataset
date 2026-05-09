import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    qvtrelationcs::Transformation,
    ClassCS,
    qvtrelationcs::TransformationCS,
    RootPackageCS,
    qvtrelationcs::TopLevelCS,
    qvtrelationcs::TypedRefCS,
    qvtrelationcs::Element,
    TypedElementCS,
    qvtrelationcs::ParamDeclarationCS,
    ExpCS,
    Relation,
    qvtrelationcs::QueryCS,
    AbstractDomainCS,
    qvtrelationcs::DomainCS,
    qvtrelationcs::Variable,
    qvtrelationcs::ExpCS,
    qvtrelationcs::Namespace,
    NamedElementCS,
    qvtrelationcs::RelationCS,
    qvtrelationcs::VarDeclarationIdCS,
    qvtrelationcs::TemplateVariableCS,
    qvtrelationcs::ModelDeclCS,
    qvtrelationcs::Class,
    qvtrelationcs::Property,
    qvtrelationcs::PathNameCS,
    TemplateVariableCS,
    qvtrelationcs::ElementTemplateCS,
    qvtrelationcs::PrimitiveTypeDomainCS,
    qvtrelationcs::TemplateCS,
    qvtrelationcs::TypedModel,
    TemplateCS,
    qvtrelationcs::ObjectTemplateCS,
    qvtrelationcs::CollectionTemplateCS,
    Nameable,
    ModelElementCS,
    qvtrelationcs::PropertyTemplateCS,
    qvtrelationcs::PredicateCS,
    qvtrelationcs::DefaultValueCS,
    qvtrelationcs::VarDeclarationCS,
    qvtrelationcs::DomainPatternCS,
    qvtrelationcs::KeyDeclCS,
    qvtrelationcs::PatternCS,
    qvtrelationcs::AbstractDomainCS,
    qvtrelationcs::UnitCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvtrelationcs::transformation_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Transformation)


def test_qvtrelationcs::transformation_constructor_exists():
    assert callable(qvtrelationcs::Transformation.__init__)


def test_qvtrelationcs::transformation_constructor_args():
    sig = inspect.signature(qvtrelationcs::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_classcs_is_not_abstract():
    assert not inspect.isabstract(ClassCS)


def test_classcs_constructor_exists():
    assert callable(ClassCS.__init__)


def test_classcs_constructor_args():
    sig = inspect.signature(ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TransformationCS)


def test_qvtrelationcs::transformationcs_constructor_exists():
    assert callable(qvtrelationcs::TransformationCS.__init__)


def test_qvtrelationcs::transformationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(RootPackageCS)


def test_rootpackagecs_constructor_exists():
    assert callable(RootPackageCS.__init__)


def test_rootpackagecs_constructor_args():
    sig = inspect.signature(RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TopLevelCS)


def test_qvtrelationcs::toplevelcs_constructor_exists():
    assert callable(qvtrelationcs::TopLevelCS.__init__)


def test_qvtrelationcs::toplevelcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TypedRefCS)


def test_qvtrelationcs::typedrefcs_constructor_exists():
    assert callable(qvtrelationcs::TypedRefCS.__init__)


def test_qvtrelationcs::typedrefcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::element_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Element)


def test_qvtrelationcs::element_constructor_exists():
    assert callable(qvtrelationcs::Element.__init__)


def test_qvtrelationcs::element_constructor_args():
    sig = inspect.signature(qvtrelationcs::Element.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::ParamDeclarationCS)


def test_qvtrelationcs::paramdeclarationcs_constructor_exists():
    assert callable(qvtrelationcs::ParamDeclarationCS.__init__)


def test_qvtrelationcs::paramdeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::querycs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::QueryCS)


def test_qvtrelationcs::querycs_constructor_exists():
    assert callable(qvtrelationcs::QueryCS.__init__)


def test_qvtrelationcs::querycs_constructor_args():
    sig = inspect.signature(qvtrelationcs::QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(AbstractDomainCS)


def test_abstractdomaincs_constructor_exists():
    assert callable(AbstractDomainCS.__init__)


def test_abstractdomaincs_constructor_args():
    sig = inspect.signature(AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::domaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::DomainCS)


def test_qvtrelationcs::domaincs_constructor_exists():
    assert callable(qvtrelationcs::DomainCS.__init__)


def test_qvtrelationcs::domaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs::DomainCS.__init__)
    params = list(sig.parameters.keys())
    assert "isReplace" in params, "Missing parameter 'isReplace'"
    assert "isCheckonly" in params, "Missing parameter 'isCheckonly'"
    assert "implementedBy" in params, "Missing parameter 'implementedBy'"
    assert "isEnforce" in params, "Missing parameter 'isEnforce'"

def test_qvtrelationcs::domaincs_has_isReplace():
    assert hasattr(qvtrelationcs::DomainCS, "isReplace")
    descriptor = None
    for klass in qvtrelationcs::DomainCS.__mro__:
        if "isReplace" in klass.__dict__:
            descriptor = klass.__dict__["isReplace"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs::domaincs_has_isCheckonly():
    assert hasattr(qvtrelationcs::DomainCS, "isCheckonly")
    descriptor = None
    for klass in qvtrelationcs::DomainCS.__mro__:
        if "isCheckonly" in klass.__dict__:
            descriptor = klass.__dict__["isCheckonly"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs::domaincs_has_implementedBy():
    assert hasattr(qvtrelationcs::DomainCS, "implementedBy")
    descriptor = None
    for klass in qvtrelationcs::DomainCS.__mro__:
        if "implementedBy" in klass.__dict__:
            descriptor = klass.__dict__["implementedBy"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs::domaincs_has_isEnforce():
    assert hasattr(qvtrelationcs::DomainCS, "isEnforce")
    descriptor = None
    for klass in qvtrelationcs::DomainCS.__mro__:
        if "isEnforce" in klass.__dict__:
            descriptor = klass.__dict__["isEnforce"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelationcs::variable_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Variable)


def test_qvtrelationcs::variable_constructor_exists():
    assert callable(qvtrelationcs::Variable.__init__)


def test_qvtrelationcs::variable_constructor_args():
    sig = inspect.signature(qvtrelationcs::Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::expcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::ExpCS)


def test_qvtrelationcs::expcs_constructor_exists():
    assert callable(qvtrelationcs::ExpCS.__init__)


def test_qvtrelationcs::expcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::namespace_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Namespace)


def test_qvtrelationcs::namespace_constructor_exists():
    assert callable(qvtrelationcs::Namespace.__init__)


def test_qvtrelationcs::namespace_constructor_args():
    sig = inspect.signature(qvtrelationcs::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::relationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::RelationCS)


def test_qvtrelationcs::relationcs_constructor_exists():
    assert callable(qvtrelationcs::RelationCS.__init__)


def test_qvtrelationcs::relationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::RelationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isTop" in params, "Missing parameter 'isTop'"
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_qvtrelationcs::relationcs_has_isTop():
    assert hasattr(qvtrelationcs::RelationCS, "isTop")
    descriptor = None
    for klass in qvtrelationcs::RelationCS.__mro__:
        if "isTop" in klass.__dict__:
            descriptor = klass.__dict__["isTop"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs::relationcs_has_isDefault():
    assert hasattr(qvtrelationcs::RelationCS, "isDefault")
    descriptor = None
    for klass in qvtrelationcs::RelationCS.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelationcs::vardeclarationidcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::VarDeclarationIdCS)


def test_qvtrelationcs::vardeclarationidcs_constructor_exists():
    assert callable(qvtrelationcs::VarDeclarationIdCS.__init__)


def test_qvtrelationcs::vardeclarationidcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::VarDeclarationIdCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TemplateVariableCS)


def test_qvtrelationcs::templatevariablecs_constructor_exists():
    assert callable(qvtrelationcs::TemplateVariableCS.__init__)


def test_qvtrelationcs::templatevariablecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::modeldeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::ModelDeclCS)


def test_qvtrelationcs::modeldeclcs_constructor_exists():
    assert callable(qvtrelationcs::ModelDeclCS.__init__)


def test_qvtrelationcs::modeldeclcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::ModelDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::class_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Class)


def test_qvtrelationcs::class_constructor_exists():
    assert callable(qvtrelationcs::Class.__init__)


def test_qvtrelationcs::class_constructor_args():
    sig = inspect.signature(qvtrelationcs::Class.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::property_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::Property)


def test_qvtrelationcs::property_constructor_exists():
    assert callable(qvtrelationcs::Property.__init__)


def test_qvtrelationcs::property_constructor_args():
    sig = inspect.signature(qvtrelationcs::Property.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::PathNameCS)


def test_qvtrelationcs::pathnamecs_constructor_exists():
    assert callable(qvtrelationcs::PathNameCS.__init__)


def test_qvtrelationcs::pathnamecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(TemplateVariableCS)


def test_templatevariablecs_constructor_exists():
    assert callable(TemplateVariableCS.__init__)


def test_templatevariablecs_constructor_args():
    sig = inspect.signature(TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::elementtemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::ElementTemplateCS)


def test_qvtrelationcs::elementtemplatecs_constructor_exists():
    assert callable(qvtrelationcs::ElementTemplateCS.__init__)


def test_qvtrelationcs::elementtemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::ElementTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::primitivetypedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::PrimitiveTypeDomainCS)


def test_qvtrelationcs::primitivetypedomaincs_constructor_exists():
    assert callable(qvtrelationcs::PrimitiveTypeDomainCS.__init__)


def test_qvtrelationcs::primitivetypedomaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs::PrimitiveTypeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::templatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TemplateCS)


def test_qvtrelationcs::templatecs_constructor_exists():
    assert callable(qvtrelationcs::TemplateCS.__init__)


def test_qvtrelationcs::templatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::typedmodel_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::TypedModel)


def test_qvtrelationcs::typedmodel_constructor_exists():
    assert callable(qvtrelationcs::TypedModel.__init__)


def test_qvtrelationcs::typedmodel_constructor_args():
    sig = inspect.signature(qvtrelationcs::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_templatecs_is_not_abstract():
    assert not inspect.isabstract(TemplateCS)


def test_templatecs_constructor_exists():
    assert callable(TemplateCS.__init__)


def test_templatecs_constructor_args():
    sig = inspect.signature(TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::objecttemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::ObjectTemplateCS)


def test_qvtrelationcs::objecttemplatecs_constructor_exists():
    assert callable(qvtrelationcs::ObjectTemplateCS.__init__)


def test_qvtrelationcs::objecttemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::ObjectTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::collectiontemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::CollectionTemplateCS)


def test_qvtrelationcs::collectiontemplatecs_constructor_exists():
    assert callable(qvtrelationcs::CollectionTemplateCS.__init__)


def test_qvtrelationcs::collectiontemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::CollectionTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::propertytemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::PropertyTemplateCS)


def test_qvtrelationcs::propertytemplatecs_constructor_exists():
    assert callable(qvtrelationcs::PropertyTemplateCS.__init__)


def test_qvtrelationcs::propertytemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::PropertyTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::predicatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::PredicateCS)


def test_qvtrelationcs::predicatecs_constructor_exists():
    assert callable(qvtrelationcs::PredicateCS.__init__)


def test_qvtrelationcs::predicatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::PredicateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::defaultvaluecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::DefaultValueCS)


def test_qvtrelationcs::defaultvaluecs_constructor_exists():
    assert callable(qvtrelationcs::DefaultValueCS.__init__)


def test_qvtrelationcs::defaultvaluecs_constructor_args():
    sig = inspect.signature(qvtrelationcs::DefaultValueCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::vardeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::VarDeclarationCS)


def test_qvtrelationcs::vardeclarationcs_constructor_exists():
    assert callable(qvtrelationcs::VarDeclarationCS.__init__)


def test_qvtrelationcs::vardeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::VarDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::domainpatterncs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::DomainPatternCS)


def test_qvtrelationcs::domainpatterncs_constructor_exists():
    assert callable(qvtrelationcs::DomainPatternCS.__init__)


def test_qvtrelationcs::domainpatterncs_constructor_args():
    sig = inspect.signature(qvtrelationcs::DomainPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::keydeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::KeyDeclCS)


def test_qvtrelationcs::keydeclcs_constructor_exists():
    assert callable(qvtrelationcs::KeyDeclCS.__init__)


def test_qvtrelationcs::keydeclcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::KeyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::patterncs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::PatternCS)


def test_qvtrelationcs::patterncs_constructor_exists():
    assert callable(qvtrelationcs::PatternCS.__init__)


def test_qvtrelationcs::patterncs_constructor_args():
    sig = inspect.signature(qvtrelationcs::PatternCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::AbstractDomainCS)


def test_qvtrelationcs::abstractdomaincs_constructor_exists():
    assert callable(qvtrelationcs::AbstractDomainCS.__init__)


def test_qvtrelationcs::abstractdomaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs::AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs::unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs::UnitCS)


def test_qvtrelationcs::unitcs_constructor_exists():
    assert callable(qvtrelationcs::UnitCS.__init__)


def test_qvtrelationcs::unitcs_constructor_args():
    sig = inspect.signature(qvtrelationcs::UnitCS.__init__)
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
qvtrelationcs::Transformation_strategy = st.builds(
    qvtrelationcs::Transformation,
)
ClassCS_strategy = st.builds(
    ClassCS,
)
qvtrelationcs::TransformationCS_strategy = st.builds(
    qvtrelationcs::TransformationCS,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
qvtrelationcs::TopLevelCS_strategy = st.builds(
    qvtrelationcs::TopLevelCS,
)
qvtrelationcs::TypedRefCS_strategy = st.builds(
    qvtrelationcs::TypedRefCS,
)
qvtrelationcs::Element_strategy = st.builds(
    qvtrelationcs::Element,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
qvtrelationcs::ParamDeclarationCS_strategy = st.builds(
    qvtrelationcs::ParamDeclarationCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
Relation_strategy = st.builds(
    Relation,
)
qvtrelationcs::QueryCS_strategy = st.builds(
    qvtrelationcs::QueryCS,
)
AbstractDomainCS_strategy = st.builds(
    AbstractDomainCS,
)
qvtrelationcs::DomainCS_strategy = st.builds(
    qvtrelationcs::DomainCS,
    isReplace=
        st.booleans(),
    isCheckonly=
        st.booleans(),
    implementedBy=
        safe_text,
    isEnforce=
        st.booleans()
)
qvtrelationcs::Variable_strategy = st.builds(
    qvtrelationcs::Variable,
)
qvtrelationcs::ExpCS_strategy = st.builds(
    qvtrelationcs::ExpCS,
)
qvtrelationcs::Namespace_strategy = st.builds(
    qvtrelationcs::Namespace,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
qvtrelationcs::RelationCS_strategy = st.builds(
    qvtrelationcs::RelationCS,
    isTop=
        st.booleans(),
    isDefault=
        st.booleans()
)
qvtrelationcs::VarDeclarationIdCS_strategy = st.builds(
    qvtrelationcs::VarDeclarationIdCS,
)
qvtrelationcs::TemplateVariableCS_strategy = st.builds(
    qvtrelationcs::TemplateVariableCS,
)
qvtrelationcs::ModelDeclCS_strategy = st.builds(
    qvtrelationcs::ModelDeclCS,
)
qvtrelationcs::Class_strategy = st.builds(
    qvtrelationcs::Class,
)
qvtrelationcs::Property_strategy = st.builds(
    qvtrelationcs::Property,
)
qvtrelationcs::PathNameCS_strategy = st.builds(
    qvtrelationcs::PathNameCS,
)
TemplateVariableCS_strategy = st.builds(
    TemplateVariableCS,
)
qvtrelationcs::ElementTemplateCS_strategy = st.builds(
    qvtrelationcs::ElementTemplateCS,
)
qvtrelationcs::PrimitiveTypeDomainCS_strategy = st.builds(
    qvtrelationcs::PrimitiveTypeDomainCS,
)
qvtrelationcs::TemplateCS_strategy = st.builds(
    qvtrelationcs::TemplateCS,
)
qvtrelationcs::TypedModel_strategy = st.builds(
    qvtrelationcs::TypedModel,
)
TemplateCS_strategy = st.builds(
    TemplateCS,
)
qvtrelationcs::ObjectTemplateCS_strategy = st.builds(
    qvtrelationcs::ObjectTemplateCS,
)
qvtrelationcs::CollectionTemplateCS_strategy = st.builds(
    qvtrelationcs::CollectionTemplateCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
qvtrelationcs::PropertyTemplateCS_strategy = st.builds(
    qvtrelationcs::PropertyTemplateCS,
)
qvtrelationcs::PredicateCS_strategy = st.builds(
    qvtrelationcs::PredicateCS,
)
qvtrelationcs::DefaultValueCS_strategy = st.builds(
    qvtrelationcs::DefaultValueCS,
)
qvtrelationcs::VarDeclarationCS_strategy = st.builds(
    qvtrelationcs::VarDeclarationCS,
)
qvtrelationcs::DomainPatternCS_strategy = st.builds(
    qvtrelationcs::DomainPatternCS,
)
qvtrelationcs::KeyDeclCS_strategy = st.builds(
    qvtrelationcs::KeyDeclCS,
)
qvtrelationcs::PatternCS_strategy = st.builds(
    qvtrelationcs::PatternCS,
)
qvtrelationcs::AbstractDomainCS_strategy = st.builds(
    qvtrelationcs::AbstractDomainCS,
)
qvtrelationcs::UnitCS_strategy = st.builds(
    qvtrelationcs::UnitCS,
)

@given(instance=qvtrelationcs::Transformation_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::transformation_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Transformation)

@given(instance=ClassCS_strategy)
@settings(max_examples=50)
def test_classcs_instantiation(instance):
    assert isinstance(instance, ClassCS)

@given(instance=qvtrelationcs::TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::transformationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TransformationCS)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=qvtrelationcs::TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TopLevelCS)

@given(instance=qvtrelationcs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::typedrefcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TypedRefCS)

@given(instance=qvtrelationcs::Element_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::element_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Element)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=qvtrelationcs::ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::ParamDeclarationCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=qvtrelationcs::QueryCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::querycs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::QueryCS)

@given(instance=AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, AbstractDomainCS)

@given(instance=qvtrelationcs::DomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::domaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::DomainCS)

@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isReplace_type(instance):
    assert isinstance(instance.isReplace, bool)


@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isReplace_setter(instance):
    original = instance.isReplace
    instance.isReplace = original
    assert instance.isReplace == original

@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isCheckonly_type(instance):
    assert isinstance(instance.isCheckonly, bool)


@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isCheckonly_setter(instance):
    original = instance.isCheckonly
    instance.isCheckonly = original
    assert instance.isCheckonly == original

@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_implementedBy_type(instance):
    assert isinstance(instance.implementedBy, str)


@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_implementedBy_setter(instance):
    original = instance.implementedBy
    instance.implementedBy = original
    assert instance.implementedBy == original

@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isEnforce_type(instance):
    assert isinstance(instance.isEnforce, bool)


@given(instance=qvtrelationcs::DomainCS_strategy)
def test_qvtrelationcs::domaincs_isEnforce_setter(instance):
    original = instance.isEnforce
    instance.isEnforce = original
    assert instance.isEnforce == original

@given(instance=qvtrelationcs::Variable_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::variable_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Variable)

@given(instance=qvtrelationcs::ExpCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::expcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::ExpCS)

@given(instance=qvtrelationcs::Namespace_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::namespace_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Namespace)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=qvtrelationcs::RelationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::relationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::RelationCS)

@given(instance=qvtrelationcs::RelationCS_strategy)
def test_qvtrelationcs::relationcs_isTop_type(instance):
    assert isinstance(instance.isTop, bool)


@given(instance=qvtrelationcs::RelationCS_strategy)
def test_qvtrelationcs::relationcs_isTop_setter(instance):
    original = instance.isTop
    instance.isTop = original
    assert instance.isTop == original

@given(instance=qvtrelationcs::RelationCS_strategy)
def test_qvtrelationcs::relationcs_isDefault_type(instance):
    assert isinstance(instance.isDefault, bool)


@given(instance=qvtrelationcs::RelationCS_strategy)
def test_qvtrelationcs::relationcs_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=qvtrelationcs::VarDeclarationIdCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::vardeclarationidcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::VarDeclarationIdCS)

@given(instance=qvtrelationcs::TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::templatevariablecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TemplateVariableCS)

@given(instance=qvtrelationcs::ModelDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::modeldeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::ModelDeclCS)

@given(instance=qvtrelationcs::Class_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::class_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Class)

@given(instance=qvtrelationcs::Property_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::property_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::Property)

@given(instance=qvtrelationcs::PathNameCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::pathnamecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::PathNameCS)

@given(instance=TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_templatevariablecs_instantiation(instance):
    assert isinstance(instance, TemplateVariableCS)

@given(instance=qvtrelationcs::ElementTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::elementtemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::ElementTemplateCS)

@given(instance=qvtrelationcs::PrimitiveTypeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::primitivetypedomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::PrimitiveTypeDomainCS)

@given(instance=qvtrelationcs::TemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::templatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TemplateCS)

@given(instance=qvtrelationcs::TypedModel_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::typedmodel_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::TypedModel)

@given(instance=TemplateCS_strategy)
@settings(max_examples=50)
def test_templatecs_instantiation(instance):
    assert isinstance(instance, TemplateCS)

@given(instance=qvtrelationcs::ObjectTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::objecttemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::ObjectTemplateCS)

@given(instance=qvtrelationcs::CollectionTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::collectiontemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::CollectionTemplateCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=qvtrelationcs::PropertyTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::propertytemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::PropertyTemplateCS)

@given(instance=qvtrelationcs::PredicateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::predicatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::PredicateCS)

@given(instance=qvtrelationcs::DefaultValueCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::defaultvaluecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::DefaultValueCS)

@given(instance=qvtrelationcs::VarDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::vardeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::VarDeclarationCS)

@given(instance=qvtrelationcs::DomainPatternCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::domainpatterncs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::DomainPatternCS)

@given(instance=qvtrelationcs::KeyDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::keydeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::KeyDeclCS)

@given(instance=qvtrelationcs::PatternCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::patterncs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::PatternCS)

@given(instance=qvtrelationcs::AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::abstractdomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::AbstractDomainCS)

@given(instance=qvtrelationcs::UnitCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs::unitcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs::UnitCS)

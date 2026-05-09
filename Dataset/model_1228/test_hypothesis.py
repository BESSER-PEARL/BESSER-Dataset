import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    QueryCS,
    KeyDeclCS,
    ModelDeclCS,
    TransformationCS,
    UnitCS,
    cst::OCLExpressionCS,
    WhereCS,
    WhenCS,
    VarDeclarationCS,
    RelationCS,
    cst::qvtrelation::EStructuralFeature,
    cst::AbstractDomainCS,
    cst::TemplateVariableCS,
    qvtrelation::cst::TemplateCS,
    qvtrelation::cst::PrimitiveTypeDomainCS,
    TypeCS,
    cst::qvtrelation::EClass,
    PropertyTemplateCS,
    PathNameCS,
    OperationCallExpCS,
    DefaultValueCS,
    ParamDeclarationCS,
    IdentifierCS,
    cst::qvtrelation::EClassifier,
    IdentifiedCS,
    qvtrelation::cst::TemplateVariableCS,
    TemplateCS,
    qvtrelation::cst::ObjectTemplateCS,
    qvtrelation::cst::CollectionTemplateCS,
    CSTNode,
    qvtrelation::cst::QueryCS,
    qvtrelation::cst::TransformationCS,
    qvtrelation::cst::TopLevelCS,
    qvtrelation::cst::UnitCS,
    qvtrelation::cst::RelationCS,
    qvtrelation::cst::VarDeclarationCS,
    qvtrelation::cst::KeyDeclCS,
    qvtrelation::cst::ParamDeclarationCS,
    qvtrelation::cst::WhereCS,
    qvtrelation::cst::WhenCS,
    qvtrelation::cst::PropertyTemplateCS,
    qvtrelation::cst::ModelDeclCS,
    qvtrelation::cst::AbstractDomainCS,
    AbstractDomainCS,
    qvtrelation::cst::DomainCS,
    OCLExpressionCS,
    qvtrelation::cst::DefaultValueCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_querycs_is_not_abstract():
    assert not inspect.isabstract(QueryCS)


def test_querycs_constructor_exists():
    assert callable(QueryCS.__init__)


def test_querycs_constructor_args():
    sig = inspect.signature(QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_keydeclcs_is_not_abstract():
    assert not inspect.isabstract(KeyDeclCS)


def test_keydeclcs_constructor_exists():
    assert callable(KeyDeclCS.__init__)


def test_keydeclcs_constructor_args():
    sig = inspect.signature(KeyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_modeldeclcs_is_not_abstract():
    assert not inspect.isabstract(ModelDeclCS)


def test_modeldeclcs_constructor_exists():
    assert callable(ModelDeclCS.__init__)


def test_modeldeclcs_constructor_args():
    sig = inspect.signature(ModelDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_transformationcs_is_not_abstract():
    assert not inspect.isabstract(TransformationCS)


def test_transformationcs_constructor_exists():
    assert callable(TransformationCS.__init__)


def test_transformationcs_constructor_args():
    sig = inspect.signature(TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_unitcs_is_not_abstract():
    assert not inspect.isabstract(UnitCS)


def test_unitcs_constructor_exists():
    assert callable(UnitCS.__init__)


def test_unitcs_constructor_args():
    sig = inspect.signature(UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(cst::OCLExpressionCS)


def test_cst::oclexpressioncs_constructor_exists():
    assert callable(cst::OCLExpressionCS.__init__)


def test_cst::oclexpressioncs_constructor_args():
    sig = inspect.signature(cst::OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_wherecs_is_not_abstract():
    assert not inspect.isabstract(WhereCS)


def test_wherecs_constructor_exists():
    assert callable(WhereCS.__init__)


def test_wherecs_constructor_args():
    sig = inspect.signature(WhereCS.__init__)
    params = list(sig.parameters.keys())



def test_whencs_is_not_abstract():
    assert not inspect.isabstract(WhenCS)


def test_whencs_constructor_exists():
    assert callable(WhenCS.__init__)


def test_whencs_constructor_args():
    sig = inspect.signature(WhenCS.__init__)
    params = list(sig.parameters.keys())



def test_vardeclarationcs_is_not_abstract():
    assert not inspect.isabstract(VarDeclarationCS)


def test_vardeclarationcs_constructor_exists():
    assert callable(VarDeclarationCS.__init__)


def test_vardeclarationcs_constructor_args():
    sig = inspect.signature(VarDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_relationcs_is_not_abstract():
    assert not inspect.isabstract(RelationCS)


def test_relationcs_constructor_exists():
    assert callable(RelationCS.__init__)


def test_relationcs_constructor_args():
    sig = inspect.signature(RelationCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::qvtrelation::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(cst::qvtrelation::EStructuralFeature)


def test_cst::qvtrelation::estructuralfeature_constructor_exists():
    assert callable(cst::qvtrelation::EStructuralFeature.__init__)


def test_cst::qvtrelation::estructuralfeature_constructor_args():
    sig = inspect.signature(cst::qvtrelation::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_cst::abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(cst::AbstractDomainCS)


def test_cst::abstractdomaincs_constructor_exists():
    assert callable(cst::AbstractDomainCS.__init__)


def test_cst::abstractdomaincs_constructor_args():
    sig = inspect.signature(cst::AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(cst::TemplateVariableCS)


def test_cst::templatevariablecs_constructor_exists():
    assert callable(cst::TemplateVariableCS.__init__)


def test_cst::templatevariablecs_constructor_args():
    sig = inspect.signature(cst::TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::templatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::TemplateCS)


def test_qvtrelation::cst::templatecs_constructor_exists():
    assert callable(qvtrelation::cst::TemplateCS.__init__)


def test_qvtrelation::cst::templatecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::primitivetypedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::PrimitiveTypeDomainCS)


def test_qvtrelation::cst::primitivetypedomaincs_constructor_exists():
    assert callable(qvtrelation::cst::PrimitiveTypeDomainCS.__init__)


def test_qvtrelation::cst::primitivetypedomaincs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::PrimitiveTypeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::qvtrelation::eclass_is_not_abstract():
    assert not inspect.isabstract(cst::qvtrelation::EClass)


def test_cst::qvtrelation::eclass_constructor_exists():
    assert callable(cst::qvtrelation::EClass.__init__)


def test_cst::qvtrelation::eclass_constructor_args():
    sig = inspect.signature(cst::qvtrelation::EClass.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplatecs_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateCS)


def test_propertytemplatecs_constructor_exists():
    assert callable(PropertyTemplateCS.__init__)


def test_propertytemplatecs_constructor_args():
    sig = inspect.signature(PropertyTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_defaultvaluecs_is_not_abstract():
    assert not inspect.isabstract(DefaultValueCS)


def test_defaultvaluecs_constructor_exists():
    assert callable(DefaultValueCS.__init__)


def test_defaultvaluecs_constructor_args():
    sig = inspect.signature(DefaultValueCS.__init__)
    params = list(sig.parameters.keys())



def test_paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ParamDeclarationCS)


def test_paramdeclarationcs_constructor_exists():
    assert callable(ParamDeclarationCS.__init__)


def test_paramdeclarationcs_constructor_args():
    sig = inspect.signature(ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_identifiercs_is_not_abstract():
    assert not inspect.isabstract(IdentifierCS)


def test_identifiercs_constructor_exists():
    assert callable(IdentifierCS.__init__)


def test_identifiercs_constructor_args():
    sig = inspect.signature(IdentifierCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::qvtrelation::eclassifier_is_not_abstract():
    assert not inspect.isabstract(cst::qvtrelation::EClassifier)


def test_cst::qvtrelation::eclassifier_constructor_exists():
    assert callable(cst::qvtrelation::EClassifier.__init__)


def test_cst::qvtrelation::eclassifier_constructor_args():
    sig = inspect.signature(cst::qvtrelation::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiedcs_is_not_abstract():
    assert not inspect.isabstract(IdentifiedCS)


def test_identifiedcs_constructor_exists():
    assert callable(IdentifiedCS.__init__)


def test_identifiedcs_constructor_args():
    sig = inspect.signature(IdentifiedCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::TemplateVariableCS)


def test_qvtrelation::cst::templatevariablecs_constructor_exists():
    assert callable(qvtrelation::cst::TemplateVariableCS.__init__)


def test_qvtrelation::cst::templatevariablecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_templatecs_is_not_abstract():
    assert not inspect.isabstract(TemplateCS)


def test_templatecs_constructor_exists():
    assert callable(TemplateCS.__init__)


def test_templatecs_constructor_args():
    sig = inspect.signature(TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::objecttemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::ObjectTemplateCS)


def test_qvtrelation::cst::objecttemplatecs_constructor_exists():
    assert callable(qvtrelation::cst::ObjectTemplateCS.__init__)


def test_qvtrelation::cst::objecttemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::ObjectTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::collectiontemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::CollectionTemplateCS)


def test_qvtrelation::cst::collectiontemplatecs_constructor_exists():
    assert callable(qvtrelation::cst::CollectionTemplateCS.__init__)


def test_qvtrelation::cst::collectiontemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::CollectionTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::querycs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::QueryCS)


def test_qvtrelation::cst::querycs_constructor_exists():
    assert callable(qvtrelation::cst::QueryCS.__init__)


def test_qvtrelation::cst::querycs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::TransformationCS)


def test_qvtrelation::cst::transformationcs_constructor_exists():
    assert callable(qvtrelation::cst::TransformationCS.__init__)


def test_qvtrelation::cst::transformationcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::TopLevelCS)


def test_qvtrelation::cst::toplevelcs_constructor_exists():
    assert callable(qvtrelation::cst::TopLevelCS.__init__)


def test_qvtrelation::cst::toplevelcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::UnitCS)


def test_qvtrelation::cst::unitcs_constructor_exists():
    assert callable(qvtrelation::cst::UnitCS.__init__)


def test_qvtrelation::cst::unitcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::relationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::RelationCS)


def test_qvtrelation::cst::relationcs_constructor_exists():
    assert callable(qvtrelation::cst::RelationCS.__init__)


def test_qvtrelation::cst::relationcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::RelationCS.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_qvtrelation::cst::relationcs_has_top():
    assert hasattr(qvtrelation::cst::RelationCS, "top")
    descriptor = None
    for klass in qvtrelation::cst::RelationCS.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation::cst::vardeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::VarDeclarationCS)


def test_qvtrelation::cst::vardeclarationcs_constructor_exists():
    assert callable(qvtrelation::cst::VarDeclarationCS.__init__)


def test_qvtrelation::cst::vardeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::VarDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::keydeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::KeyDeclCS)


def test_qvtrelation::cst::keydeclcs_constructor_exists():
    assert callable(qvtrelation::cst::KeyDeclCS.__init__)


def test_qvtrelation::cst::keydeclcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::KeyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::ParamDeclarationCS)


def test_qvtrelation::cst::paramdeclarationcs_constructor_exists():
    assert callable(qvtrelation::cst::ParamDeclarationCS.__init__)


def test_qvtrelation::cst::paramdeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::wherecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::WhereCS)


def test_qvtrelation::cst::wherecs_constructor_exists():
    assert callable(qvtrelation::cst::WhereCS.__init__)


def test_qvtrelation::cst::wherecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::WhereCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::whencs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::WhenCS)


def test_qvtrelation::cst::whencs_constructor_exists():
    assert callable(qvtrelation::cst::WhenCS.__init__)


def test_qvtrelation::cst::whencs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::WhenCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::propertytemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::PropertyTemplateCS)


def test_qvtrelation::cst::propertytemplatecs_constructor_exists():
    assert callable(qvtrelation::cst::PropertyTemplateCS.__init__)


def test_qvtrelation::cst::propertytemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::PropertyTemplateCS.__init__)
    params = list(sig.parameters.keys())
    assert "opposite" in params, "Missing parameter 'opposite'"

def test_qvtrelation::cst::propertytemplatecs_has_opposite():
    assert hasattr(qvtrelation::cst::PropertyTemplateCS, "opposite")
    descriptor = None
    for klass in qvtrelation::cst::PropertyTemplateCS.__mro__:
        if "opposite" in klass.__dict__:
            descriptor = klass.__dict__["opposite"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation::cst::modeldeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::ModelDeclCS)


def test_qvtrelation::cst::modeldeclcs_constructor_exists():
    assert callable(qvtrelation::cst::ModelDeclCS.__init__)


def test_qvtrelation::cst::modeldeclcs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::ModelDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::AbstractDomainCS)


def test_qvtrelation::cst::abstractdomaincs_constructor_exists():
    assert callable(qvtrelation::cst::AbstractDomainCS.__init__)


def test_qvtrelation::cst::abstractdomaincs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(AbstractDomainCS)


def test_abstractdomaincs_constructor_exists():
    assert callable(AbstractDomainCS.__init__)


def test_abstractdomaincs_constructor_args():
    sig = inspect.signature(AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::domaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::DomainCS)


def test_qvtrelation::cst::domaincs_constructor_exists():
    assert callable(qvtrelation::cst::DomainCS.__init__)


def test_qvtrelation::cst::domaincs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::DomainCS.__init__)
    params = list(sig.parameters.keys())
    assert "enforce" in params, "Missing parameter 'enforce'"
    assert "checkonly" in params, "Missing parameter 'checkonly'"
    assert "replace" in params, "Missing parameter 'replace'"

def test_qvtrelation::cst::domaincs_has_enforce():
    assert hasattr(qvtrelation::cst::DomainCS, "enforce")
    descriptor = None
    for klass in qvtrelation::cst::DomainCS.__mro__:
        if "enforce" in klass.__dict__:
            descriptor = klass.__dict__["enforce"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelation::cst::domaincs_has_checkonly():
    assert hasattr(qvtrelation::cst::DomainCS, "checkonly")
    descriptor = None
    for klass in qvtrelation::cst::DomainCS.__mro__:
        if "checkonly" in klass.__dict__:
            descriptor = klass.__dict__["checkonly"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelation::cst::domaincs_has_replace():
    assert hasattr(qvtrelation::cst::DomainCS, "replace")
    descriptor = None
    for klass in qvtrelation::cst::DomainCS.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::cst::defaultvaluecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::cst::DefaultValueCS)


def test_qvtrelation::cst::defaultvaluecs_constructor_exists():
    assert callable(qvtrelation::cst::DefaultValueCS.__init__)


def test_qvtrelation::cst::defaultvaluecs_constructor_args():
    sig = inspect.signature(qvtrelation::cst::DefaultValueCS.__init__)
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
QueryCS_strategy = st.builds(
    QueryCS,
)
KeyDeclCS_strategy = st.builds(
    KeyDeclCS,
)
ModelDeclCS_strategy = st.builds(
    ModelDeclCS,
)
TransformationCS_strategy = st.builds(
    TransformationCS,
)
UnitCS_strategy = st.builds(
    UnitCS,
)
cst::OCLExpressionCS_strategy = st.builds(
    cst::OCLExpressionCS,
)
WhereCS_strategy = st.builds(
    WhereCS,
)
WhenCS_strategy = st.builds(
    WhenCS,
)
VarDeclarationCS_strategy = st.builds(
    VarDeclarationCS,
)
RelationCS_strategy = st.builds(
    RelationCS,
)
cst::qvtrelation::EStructuralFeature_strategy = st.builds(
    cst::qvtrelation::EStructuralFeature,
)
cst::AbstractDomainCS_strategy = st.builds(
    cst::AbstractDomainCS,
)
cst::TemplateVariableCS_strategy = st.builds(
    cst::TemplateVariableCS,
)
qvtrelation::cst::TemplateCS_strategy = st.builds(
    qvtrelation::cst::TemplateCS,
)
qvtrelation::cst::PrimitiveTypeDomainCS_strategy = st.builds(
    qvtrelation::cst::PrimitiveTypeDomainCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
cst::qvtrelation::EClass_strategy = st.builds(
    cst::qvtrelation::EClass,
)
PropertyTemplateCS_strategy = st.builds(
    PropertyTemplateCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
DefaultValueCS_strategy = st.builds(
    DefaultValueCS,
)
ParamDeclarationCS_strategy = st.builds(
    ParamDeclarationCS,
)
IdentifierCS_strategy = st.builds(
    IdentifierCS,
)
cst::qvtrelation::EClassifier_strategy = st.builds(
    cst::qvtrelation::EClassifier,
)
IdentifiedCS_strategy = st.builds(
    IdentifiedCS,
)
qvtrelation::cst::TemplateVariableCS_strategy = st.builds(
    qvtrelation::cst::TemplateVariableCS,
)
TemplateCS_strategy = st.builds(
    TemplateCS,
)
qvtrelation::cst::ObjectTemplateCS_strategy = st.builds(
    qvtrelation::cst::ObjectTemplateCS,
)
qvtrelation::cst::CollectionTemplateCS_strategy = st.builds(
    qvtrelation::cst::CollectionTemplateCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
qvtrelation::cst::QueryCS_strategy = st.builds(
    qvtrelation::cst::QueryCS,
)
qvtrelation::cst::TransformationCS_strategy = st.builds(
    qvtrelation::cst::TransformationCS,
)
qvtrelation::cst::TopLevelCS_strategy = st.builds(
    qvtrelation::cst::TopLevelCS,
)
qvtrelation::cst::UnitCS_strategy = st.builds(
    qvtrelation::cst::UnitCS,
)
qvtrelation::cst::RelationCS_strategy = st.builds(
    qvtrelation::cst::RelationCS,
    top=
        st.booleans()
)
qvtrelation::cst::VarDeclarationCS_strategy = st.builds(
    qvtrelation::cst::VarDeclarationCS,
)
qvtrelation::cst::KeyDeclCS_strategy = st.builds(
    qvtrelation::cst::KeyDeclCS,
)
qvtrelation::cst::ParamDeclarationCS_strategy = st.builds(
    qvtrelation::cst::ParamDeclarationCS,
)
qvtrelation::cst::WhereCS_strategy = st.builds(
    qvtrelation::cst::WhereCS,
)
qvtrelation::cst::WhenCS_strategy = st.builds(
    qvtrelation::cst::WhenCS,
)
qvtrelation::cst::PropertyTemplateCS_strategy = st.builds(
    qvtrelation::cst::PropertyTemplateCS,
    opposite=
        st.booleans()
)
qvtrelation::cst::ModelDeclCS_strategy = st.builds(
    qvtrelation::cst::ModelDeclCS,
)
qvtrelation::cst::AbstractDomainCS_strategy = st.builds(
    qvtrelation::cst::AbstractDomainCS,
)
AbstractDomainCS_strategy = st.builds(
    AbstractDomainCS,
)
qvtrelation::cst::DomainCS_strategy = st.builds(
    qvtrelation::cst::DomainCS,
    enforce=
        st.booleans(),
    checkonly=
        st.booleans(),
    replace=
        st.booleans()
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
qvtrelation::cst::DefaultValueCS_strategy = st.builds(
    qvtrelation::cst::DefaultValueCS,
)

@given(instance=QueryCS_strategy)
@settings(max_examples=50)
def test_querycs_instantiation(instance):
    assert isinstance(instance, QueryCS)

@given(instance=KeyDeclCS_strategy)
@settings(max_examples=50)
def test_keydeclcs_instantiation(instance):
    assert isinstance(instance, KeyDeclCS)

@given(instance=ModelDeclCS_strategy)
@settings(max_examples=50)
def test_modeldeclcs_instantiation(instance):
    assert isinstance(instance, ModelDeclCS)

@given(instance=TransformationCS_strategy)
@settings(max_examples=50)
def test_transformationcs_instantiation(instance):
    assert isinstance(instance, TransformationCS)

@given(instance=UnitCS_strategy)
@settings(max_examples=50)
def test_unitcs_instantiation(instance):
    assert isinstance(instance, UnitCS)

@given(instance=cst::OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_cst::oclexpressioncs_instantiation(instance):
    assert isinstance(instance, cst::OCLExpressionCS)

@given(instance=WhereCS_strategy)
@settings(max_examples=50)
def test_wherecs_instantiation(instance):
    assert isinstance(instance, WhereCS)

@given(instance=WhenCS_strategy)
@settings(max_examples=50)
def test_whencs_instantiation(instance):
    assert isinstance(instance, WhenCS)

@given(instance=VarDeclarationCS_strategy)
@settings(max_examples=50)
def test_vardeclarationcs_instantiation(instance):
    assert isinstance(instance, VarDeclarationCS)

@given(instance=RelationCS_strategy)
@settings(max_examples=50)
def test_relationcs_instantiation(instance):
    assert isinstance(instance, RelationCS)

@given(instance=cst::qvtrelation::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_cst::qvtrelation::estructuralfeature_instantiation(instance):
    assert isinstance(instance, cst::qvtrelation::EStructuralFeature)

@given(instance=cst::AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_cst::abstractdomaincs_instantiation(instance):
    assert isinstance(instance, cst::AbstractDomainCS)

@given(instance=cst::TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_cst::templatevariablecs_instantiation(instance):
    assert isinstance(instance, cst::TemplateVariableCS)

@given(instance=qvtrelation::cst::TemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::templatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::TemplateCS)

@given(instance=qvtrelation::cst::PrimitiveTypeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::primitivetypedomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::PrimitiveTypeDomainCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=cst::qvtrelation::EClass_strategy)
@settings(max_examples=50)
def test_cst::qvtrelation::eclass_instantiation(instance):
    assert isinstance(instance, cst::qvtrelation::EClass)

@given(instance=PropertyTemplateCS_strategy)
@settings(max_examples=50)
def test_propertytemplatecs_instantiation(instance):
    assert isinstance(instance, PropertyTemplateCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)

@given(instance=DefaultValueCS_strategy)
@settings(max_examples=50)
def test_defaultvaluecs_instantiation(instance):
    assert isinstance(instance, DefaultValueCS)

@given(instance=ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, ParamDeclarationCS)

@given(instance=IdentifierCS_strategy)
@settings(max_examples=50)
def test_identifiercs_instantiation(instance):
    assert isinstance(instance, IdentifierCS)

@given(instance=cst::qvtrelation::EClassifier_strategy)
@settings(max_examples=50)
def test_cst::qvtrelation::eclassifier_instantiation(instance):
    assert isinstance(instance, cst::qvtrelation::EClassifier)

@given(instance=IdentifiedCS_strategy)
@settings(max_examples=50)
def test_identifiedcs_instantiation(instance):
    assert isinstance(instance, IdentifiedCS)

@given(instance=qvtrelation::cst::TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::templatevariablecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::TemplateVariableCS)

@given(instance=TemplateCS_strategy)
@settings(max_examples=50)
def test_templatecs_instantiation(instance):
    assert isinstance(instance, TemplateCS)

@given(instance=qvtrelation::cst::ObjectTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::objecttemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::ObjectTemplateCS)

@given(instance=qvtrelation::cst::CollectionTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::collectiontemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::CollectionTemplateCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=qvtrelation::cst::QueryCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::querycs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::QueryCS)

@given(instance=qvtrelation::cst::TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::transformationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::TransformationCS)

@given(instance=qvtrelation::cst::TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::TopLevelCS)

@given(instance=qvtrelation::cst::UnitCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::unitcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::UnitCS)

@given(instance=qvtrelation::cst::RelationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::relationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::RelationCS)

@given(instance=qvtrelation::cst::RelationCS_strategy)
def test_qvtrelation::cst::relationcs_top_type(instance):
    assert isinstance(instance.top, bool)


@given(instance=qvtrelation::cst::RelationCS_strategy)
def test_qvtrelation::cst::relationcs_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=qvtrelation::cst::VarDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::vardeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::VarDeclarationCS)

@given(instance=qvtrelation::cst::KeyDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::keydeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::KeyDeclCS)

@given(instance=qvtrelation::cst::ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::ParamDeclarationCS)

@given(instance=qvtrelation::cst::WhereCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::wherecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::WhereCS)

@given(instance=qvtrelation::cst::WhenCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::whencs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::WhenCS)

@given(instance=qvtrelation::cst::PropertyTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::propertytemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::PropertyTemplateCS)

@given(instance=qvtrelation::cst::PropertyTemplateCS_strategy)
def test_qvtrelation::cst::propertytemplatecs_opposite_type(instance):
    assert isinstance(instance.opposite, bool)


@given(instance=qvtrelation::cst::PropertyTemplateCS_strategy)
def test_qvtrelation::cst::propertytemplatecs_opposite_setter(instance):
    original = instance.opposite
    instance.opposite = original
    assert instance.opposite == original

@given(instance=qvtrelation::cst::ModelDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::modeldeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::ModelDeclCS)

@given(instance=qvtrelation::cst::AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::abstractdomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::AbstractDomainCS)

@given(instance=AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, AbstractDomainCS)

@given(instance=qvtrelation::cst::DomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::domaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::DomainCS)

@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_enforce_type(instance):
    assert isinstance(instance.enforce, bool)


@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_enforce_setter(instance):
    original = instance.enforce
    instance.enforce = original
    assert instance.enforce == original

@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_checkonly_type(instance):
    assert isinstance(instance.checkonly, bool)


@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_checkonly_setter(instance):
    original = instance.checkonly
    instance.checkonly = original
    assert instance.checkonly == original

@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_replace_type(instance):
    assert isinstance(instance.replace, bool)


@given(instance=qvtrelation::cst::DomainCS_strategy)
def test_qvtrelation::cst::domaincs_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=qvtrelation::cst::DefaultValueCS_strategy)
@settings(max_examples=50)
def test_qvtrelation::cst::defaultvaluecs_instantiation(instance):
    assert isinstance(instance, qvtrelation::cst::DefaultValueCS)

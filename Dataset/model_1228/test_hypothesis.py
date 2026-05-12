import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    WhereCS,
    WhenCS,
    VarDeclarationCS,
    RelationCS,
    cst_qvtrelation_EStructuralFeature,
    cst_AbstractDomainCS,
    cst_TemplateVariableCS,
    qvtrelation_cst_PrimitiveTypeDomainCS,
    TypeCS,
    cst_qvtrelation_EClass,
    PropertyTemplateCS,
    PathNameCS,
    OperationCallExpCS,
    DefaultValueCS,
    ParamDeclarationCS,
    IdentifierCS,
    cst_qvtrelation_EClassifier,
    IdentifiedCS,
    TemplateCS,
    qvtrelation_cst_ObjectTemplateCS,
    qvtrelation_cst_CollectionTemplateCS,
    CSTNode,
    qvtrelation_cst_QueryCS,
    qvtrelation_cst_UnitCS,
    qvtrelation_cst_ModelDeclCS,
    qvtrelation_cst_KeyDeclCS,
    qvtrelation_cst_RelationCS,
    qvtrelation_cst_VarDeclarationCS,
    qvtrelation_cst_PropertyTemplateCS,
    qvtrelation_cst_ParamDeclarationCS,
    qvtrelation_cst_AbstractDomainCS,
    AbstractDomainCS,
    qvtrelation_cst_DomainCS,
    OCLExpressionCS,
    qvtrelation_cst_DefaultValueCS,
    qvtrelation_cst_WhereCS,
    qvtrelation_cst_WhenCS,
    QueryCS,
    KeyDeclCS,
    ModelDeclCS,
    qvtrelation_cst_TransformationCS,
    TransformationCS,
    UnitCS,
    qvtrelation_cst_TopLevelCS,
    qvtrelation_cst_TemplateVariableCS,
    cst_OCLExpressionCS,
    qvtrelation_cst_TemplateCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_cst_qvtrelation_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(cst_qvtrelation_EStructuralFeature)


def test_cst_qvtrelation_estructuralfeature_constructor_exists():
    assert callable(cst_qvtrelation_EStructuralFeature.__init__)


def test_cst_qvtrelation_estructuralfeature_constructor_args():
    sig = inspect.signature(cst_qvtrelation_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_cst_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(cst_AbstractDomainCS)


def test_cst_abstractdomaincs_constructor_exists():
    assert callable(cst_AbstractDomainCS.__init__)


def test_cst_abstractdomaincs_constructor_args():
    sig = inspect.signature(cst_AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(cst_TemplateVariableCS)


def test_cst_templatevariablecs_constructor_exists():
    assert callable(cst_TemplateVariableCS.__init__)


def test_cst_templatevariablecs_constructor_args():
    sig = inspect.signature(cst_TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_primitivetypedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_PrimitiveTypeDomainCS)


def test_qvtrelation_cst_primitivetypedomaincs_constructor_exists():
    assert callable(qvtrelation_cst_PrimitiveTypeDomainCS.__init__)


def test_qvtrelation_cst_primitivetypedomaincs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_PrimitiveTypeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_qvtrelation_eclass_is_not_abstract():
    assert not inspect.isabstract(cst_qvtrelation_EClass)


def test_cst_qvtrelation_eclass_constructor_exists():
    assert callable(cst_qvtrelation_EClass.__init__)


def test_cst_qvtrelation_eclass_constructor_args():
    sig = inspect.signature(cst_qvtrelation_EClass.__init__)
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



def test_cst_qvtrelation_eclassifier_is_not_abstract():
    assert not inspect.isabstract(cst_qvtrelation_EClassifier)


def test_cst_qvtrelation_eclassifier_constructor_exists():
    assert callable(cst_qvtrelation_EClassifier.__init__)


def test_cst_qvtrelation_eclassifier_constructor_args():
    sig = inspect.signature(cst_qvtrelation_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiedcs_is_not_abstract():
    assert not inspect.isabstract(IdentifiedCS)


def test_identifiedcs_constructor_exists():
    assert callable(IdentifiedCS.__init__)


def test_identifiedcs_constructor_args():
    sig = inspect.signature(IdentifiedCS.__init__)
    params = list(sig.parameters.keys())



def test_templatecs_is_not_abstract():
    assert not inspect.isabstract(TemplateCS)


def test_templatecs_constructor_exists():
    assert callable(TemplateCS.__init__)


def test_templatecs_constructor_args():
    sig = inspect.signature(TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_objecttemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_ObjectTemplateCS)


def test_qvtrelation_cst_objecttemplatecs_constructor_exists():
    assert callable(qvtrelation_cst_ObjectTemplateCS.__init__)


def test_qvtrelation_cst_objecttemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_ObjectTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_collectiontemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_CollectionTemplateCS)


def test_qvtrelation_cst_collectiontemplatecs_constructor_exists():
    assert callable(qvtrelation_cst_CollectionTemplateCS.__init__)


def test_qvtrelation_cst_collectiontemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_CollectionTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_querycs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_QueryCS)


def test_qvtrelation_cst_querycs_constructor_exists():
    assert callable(qvtrelation_cst_QueryCS.__init__)


def test_qvtrelation_cst_querycs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_UnitCS)


def test_qvtrelation_cst_unitcs_constructor_exists():
    assert callable(qvtrelation_cst_UnitCS.__init__)


def test_qvtrelation_cst_unitcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_modeldeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_ModelDeclCS)


def test_qvtrelation_cst_modeldeclcs_constructor_exists():
    assert callable(qvtrelation_cst_ModelDeclCS.__init__)


def test_qvtrelation_cst_modeldeclcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_ModelDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_keydeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_KeyDeclCS)


def test_qvtrelation_cst_keydeclcs_constructor_exists():
    assert callable(qvtrelation_cst_KeyDeclCS.__init__)


def test_qvtrelation_cst_keydeclcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_KeyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_relationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_RelationCS)


def test_qvtrelation_cst_relationcs_constructor_exists():
    assert callable(qvtrelation_cst_RelationCS.__init__)


def test_qvtrelation_cst_relationcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_RelationCS.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_qvtrelation_cst_relationcs_has_top():
    assert hasattr(qvtrelation_cst_RelationCS, "top")
    descriptor = None
    for klass in qvtrelation_cst_RelationCS.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation_cst_vardeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_VarDeclarationCS)


def test_qvtrelation_cst_vardeclarationcs_constructor_exists():
    assert callable(qvtrelation_cst_VarDeclarationCS.__init__)


def test_qvtrelation_cst_vardeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_VarDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_propertytemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_PropertyTemplateCS)


def test_qvtrelation_cst_propertytemplatecs_constructor_exists():
    assert callable(qvtrelation_cst_PropertyTemplateCS.__init__)


def test_qvtrelation_cst_propertytemplatecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_PropertyTemplateCS.__init__)
    params = list(sig.parameters.keys())
    assert "opposite" in params, "Missing parameter 'opposite'"

def test_qvtrelation_cst_propertytemplatecs_has_opposite():
    assert hasattr(qvtrelation_cst_PropertyTemplateCS, "opposite")
    descriptor = None
    for klass in qvtrelation_cst_PropertyTemplateCS.__mro__:
        if "opposite" in klass.__dict__:
            descriptor = klass.__dict__["opposite"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation_cst_paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_ParamDeclarationCS)


def test_qvtrelation_cst_paramdeclarationcs_constructor_exists():
    assert callable(qvtrelation_cst_ParamDeclarationCS.__init__)


def test_qvtrelation_cst_paramdeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_AbstractDomainCS)


def test_qvtrelation_cst_abstractdomaincs_constructor_exists():
    assert callable(qvtrelation_cst_AbstractDomainCS.__init__)


def test_qvtrelation_cst_abstractdomaincs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(AbstractDomainCS)


def test_abstractdomaincs_constructor_exists():
    assert callable(AbstractDomainCS.__init__)


def test_abstractdomaincs_constructor_args():
    sig = inspect.signature(AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_domaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_DomainCS)


def test_qvtrelation_cst_domaincs_constructor_exists():
    assert callable(qvtrelation_cst_DomainCS.__init__)


def test_qvtrelation_cst_domaincs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_DomainCS.__init__)
    params = list(sig.parameters.keys())
    assert "replace" in params, "Missing parameter 'replace'"
    assert "checkonly" in params, "Missing parameter 'checkonly'"
    assert "enforce" in params, "Missing parameter 'enforce'"

def test_qvtrelation_cst_domaincs_has_replace():
    assert hasattr(qvtrelation_cst_DomainCS, "replace")
    descriptor = None
    for klass in qvtrelation_cst_DomainCS.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelation_cst_domaincs_has_checkonly():
    assert hasattr(qvtrelation_cst_DomainCS, "checkonly")
    descriptor = None
    for klass in qvtrelation_cst_DomainCS.__mro__:
        if "checkonly" in klass.__dict__:
            descriptor = klass.__dict__["checkonly"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelation_cst_domaincs_has_enforce():
    assert hasattr(qvtrelation_cst_DomainCS, "enforce")
    descriptor = None
    for klass in qvtrelation_cst_DomainCS.__mro__:
        if "enforce" in klass.__dict__:
            descriptor = klass.__dict__["enforce"]
            break
    assert isinstance(descriptor, property)



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_defaultvaluecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_DefaultValueCS)


def test_qvtrelation_cst_defaultvaluecs_constructor_exists():
    assert callable(qvtrelation_cst_DefaultValueCS.__init__)


def test_qvtrelation_cst_defaultvaluecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_DefaultValueCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_wherecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_WhereCS)


def test_qvtrelation_cst_wherecs_constructor_exists():
    assert callable(qvtrelation_cst_WhereCS.__init__)


def test_qvtrelation_cst_wherecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_WhereCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_whencs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_WhenCS)


def test_qvtrelation_cst_whencs_constructor_exists():
    assert callable(qvtrelation_cst_WhenCS.__init__)


def test_qvtrelation_cst_whencs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_WhenCS.__init__)
    params = list(sig.parameters.keys())



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



def test_qvtrelation_cst_transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_TransformationCS)


def test_qvtrelation_cst_transformationcs_constructor_exists():
    assert callable(qvtrelation_cst_TransformationCS.__init__)


def test_qvtrelation_cst_transformationcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_TransformationCS.__init__)
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



def test_qvtrelation_cst_toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_TopLevelCS)


def test_qvtrelation_cst_toplevelcs_constructor_exists():
    assert callable(qvtrelation_cst_TopLevelCS.__init__)


def test_qvtrelation_cst_toplevelcs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_TemplateVariableCS)


def test_qvtrelation_cst_templatevariablecs_constructor_exists():
    assert callable(qvtrelation_cst_TemplateVariableCS.__init__)


def test_qvtrelation_cst_templatevariablecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(cst_OCLExpressionCS)


def test_cst_oclexpressioncs_constructor_exists():
    assert callable(cst_OCLExpressionCS.__init__)


def test_cst_oclexpressioncs_constructor_args():
    sig = inspect.signature(cst_OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation_cst_templatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelation_cst_TemplateCS)


def test_qvtrelation_cst_templatecs_constructor_exists():
    assert callable(qvtrelation_cst_TemplateCS.__init__)


def test_qvtrelation_cst_templatecs_constructor_args():
    sig = inspect.signature(qvtrelation_cst_TemplateCS.__init__)
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
cst_qvtrelation_EStructuralFeature_strategy = st.builds(
    cst_qvtrelation_EStructuralFeature,
)
cst_AbstractDomainCS_strategy = st.builds(
    cst_AbstractDomainCS,
)
cst_TemplateVariableCS_strategy = st.builds(
    cst_TemplateVariableCS,
)
qvtrelation_cst_PrimitiveTypeDomainCS_strategy = st.builds(
    qvtrelation_cst_PrimitiveTypeDomainCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
cst_qvtrelation_EClass_strategy = st.builds(
    cst_qvtrelation_EClass,
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
cst_qvtrelation_EClassifier_strategy = st.builds(
    cst_qvtrelation_EClassifier,
)
IdentifiedCS_strategy = st.builds(
    IdentifiedCS,
)
TemplateCS_strategy = st.builds(
    TemplateCS,
)
qvtrelation_cst_ObjectTemplateCS_strategy = st.builds(
    qvtrelation_cst_ObjectTemplateCS,
)
qvtrelation_cst_CollectionTemplateCS_strategy = st.builds(
    qvtrelation_cst_CollectionTemplateCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
qvtrelation_cst_QueryCS_strategy = st.builds(
    qvtrelation_cst_QueryCS,
)
qvtrelation_cst_UnitCS_strategy = st.builds(
    qvtrelation_cst_UnitCS,
)
qvtrelation_cst_ModelDeclCS_strategy = st.builds(
    qvtrelation_cst_ModelDeclCS,
)
qvtrelation_cst_KeyDeclCS_strategy = st.builds(
    qvtrelation_cst_KeyDeclCS,
)
qvtrelation_cst_RelationCS_strategy = st.builds(
    qvtrelation_cst_RelationCS,
    top=
        st.booleans()
)
qvtrelation_cst_VarDeclarationCS_strategy = st.builds(
    qvtrelation_cst_VarDeclarationCS,
)
qvtrelation_cst_PropertyTemplateCS_strategy = st.builds(
    qvtrelation_cst_PropertyTemplateCS,
    opposite=
        st.booleans()
)
qvtrelation_cst_ParamDeclarationCS_strategy = st.builds(
    qvtrelation_cst_ParamDeclarationCS,
)
qvtrelation_cst_AbstractDomainCS_strategy = st.builds(
    qvtrelation_cst_AbstractDomainCS,
)
AbstractDomainCS_strategy = st.builds(
    AbstractDomainCS,
)
qvtrelation_cst_DomainCS_strategy = st.builds(
    qvtrelation_cst_DomainCS,
    replace=
        st.booleans(),
    checkonly=
        st.booleans(),
    enforce=
        st.booleans()
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
qvtrelation_cst_DefaultValueCS_strategy = st.builds(
    qvtrelation_cst_DefaultValueCS,
)
qvtrelation_cst_WhereCS_strategy = st.builds(
    qvtrelation_cst_WhereCS,
)
qvtrelation_cst_WhenCS_strategy = st.builds(
    qvtrelation_cst_WhenCS,
)
QueryCS_strategy = st.builds(
    QueryCS,
)
KeyDeclCS_strategy = st.builds(
    KeyDeclCS,
)
ModelDeclCS_strategy = st.builds(
    ModelDeclCS,
)
qvtrelation_cst_TransformationCS_strategy = st.builds(
    qvtrelation_cst_TransformationCS,
)
TransformationCS_strategy = st.builds(
    TransformationCS,
)
UnitCS_strategy = st.builds(
    UnitCS,
)
qvtrelation_cst_TopLevelCS_strategy = st.builds(
    qvtrelation_cst_TopLevelCS,
)
qvtrelation_cst_TemplateVariableCS_strategy = st.builds(
    qvtrelation_cst_TemplateVariableCS,
)
cst_OCLExpressionCS_strategy = st.builds(
    cst_OCLExpressionCS,
)
qvtrelation_cst_TemplateCS_strategy = st.builds(
    qvtrelation_cst_TemplateCS,
)

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

@given(instance=cst_qvtrelation_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_cst_qvtrelation_estructuralfeature_instantiation(instance):
    assert isinstance(instance, cst_qvtrelation_EStructuralFeature)

@given(instance=cst_AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_cst_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, cst_AbstractDomainCS)

@given(instance=cst_TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_cst_templatevariablecs_instantiation(instance):
    assert isinstance(instance, cst_TemplateVariableCS)

@given(instance=qvtrelation_cst_PrimitiveTypeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_primitivetypedomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_PrimitiveTypeDomainCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=cst_qvtrelation_EClass_strategy)
@settings(max_examples=50)
def test_cst_qvtrelation_eclass_instantiation(instance):
    assert isinstance(instance, cst_qvtrelation_EClass)

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

@given(instance=cst_qvtrelation_EClassifier_strategy)
@settings(max_examples=50)
def test_cst_qvtrelation_eclassifier_instantiation(instance):
    assert isinstance(instance, cst_qvtrelation_EClassifier)

@given(instance=IdentifiedCS_strategy)
@settings(max_examples=50)
def test_identifiedcs_instantiation(instance):
    assert isinstance(instance, IdentifiedCS)

@given(instance=TemplateCS_strategy)
@settings(max_examples=50)
def test_templatecs_instantiation(instance):
    assert isinstance(instance, TemplateCS)

@given(instance=qvtrelation_cst_ObjectTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_objecttemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_ObjectTemplateCS)

@given(instance=qvtrelation_cst_CollectionTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_collectiontemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_CollectionTemplateCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=qvtrelation_cst_QueryCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_querycs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_QueryCS)

@given(instance=qvtrelation_cst_UnitCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_unitcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_UnitCS)

@given(instance=qvtrelation_cst_ModelDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_modeldeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_ModelDeclCS)

@given(instance=qvtrelation_cst_KeyDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_keydeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_KeyDeclCS)

@given(instance=qvtrelation_cst_RelationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_relationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_RelationCS)



@given(instance=qvtrelation_cst_RelationCS_strategy)
def test_qvtrelation_cst_relationcs_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=qvtrelation_cst_VarDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_vardeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_VarDeclarationCS)

@given(instance=qvtrelation_cst_PropertyTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_propertytemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_PropertyTemplateCS)



@given(instance=qvtrelation_cst_PropertyTemplateCS_strategy)
def test_qvtrelation_cst_propertytemplatecs_opposite_setter(instance):
    original = instance.opposite
    instance.opposite = original
    assert instance.opposite == original

@given(instance=qvtrelation_cst_ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_ParamDeclarationCS)

@given(instance=qvtrelation_cst_AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_AbstractDomainCS)

@given(instance=AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, AbstractDomainCS)

@given(instance=qvtrelation_cst_DomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_domaincs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_DomainCS)



@given(instance=qvtrelation_cst_DomainCS_strategy)
def test_qvtrelation_cst_domaincs_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original



@given(instance=qvtrelation_cst_DomainCS_strategy)
def test_qvtrelation_cst_domaincs_checkonly_setter(instance):
    original = instance.checkonly
    instance.checkonly = original
    assert instance.checkonly == original



@given(instance=qvtrelation_cst_DomainCS_strategy)
def test_qvtrelation_cst_domaincs_enforce_setter(instance):
    original = instance.enforce
    instance.enforce = original
    assert instance.enforce == original

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=qvtrelation_cst_DefaultValueCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_defaultvaluecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_DefaultValueCS)

@given(instance=qvtrelation_cst_WhereCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_wherecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_WhereCS)

@given(instance=qvtrelation_cst_WhenCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_whencs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_WhenCS)

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

@given(instance=qvtrelation_cst_TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_transformationcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_TransformationCS)

@given(instance=TransformationCS_strategy)
@settings(max_examples=50)
def test_transformationcs_instantiation(instance):
    assert isinstance(instance, TransformationCS)

@given(instance=UnitCS_strategy)
@settings(max_examples=50)
def test_unitcs_instantiation(instance):
    assert isinstance(instance, UnitCS)

@given(instance=qvtrelation_cst_TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_TopLevelCS)

@given(instance=qvtrelation_cst_TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_templatevariablecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_TemplateVariableCS)

@given(instance=cst_OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_cst_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, cst_OCLExpressionCS)

@given(instance=qvtrelation_cst_TemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelation_cst_templatecs_instantiation(instance):
    assert isinstance(instance, qvtrelation_cst_TemplateCS)

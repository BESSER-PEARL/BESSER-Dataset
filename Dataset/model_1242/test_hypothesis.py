import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    qvtrelationcs_Class,
    qvtrelationcs_Property,
    qvtrelationcs_PathNameCS,
    TemplateVariableCS,
    qvtrelationcs_TypedModel,
    TemplateCS,
    qvtrelationcs_CollectionTemplateCS,
    Nameable,
    ModelElementCS,
    qvtrelationcs_DomainPatternCS,
    qvtrelationcs_KeyDeclCS,
    qvtrelationcs_AbstractDomainCS,
    qvtrelationcs_Transformation,
    ClassCS,
    qvtrelationcs_TransformationCS,
    qvtrelationcs_UnitCS,
    RootPackageCS,
    qvtrelationcs_TopLevelCS,
    qvtrelationcs_TypedRefCS,
    qvtrelationcs_Element,
    qvtrelationcs_PredicateCS,
    qvtrelationcs_PatternCS,
    TypedElementCS,
    qvtrelationcs_ParamDeclarationCS,
    qvtrelationcs_PropertyTemplateCS,
    ExpCS,
    qvtrelationcs_TemplateCS,
    qvtrelationcs_VarDeclarationCS,
    Relation,
    qvtrelationcs_QueryCS,
    AbstractDomainCS,
    qvtrelationcs_PrimitiveTypeDomainCS,
    qvtrelationcs_DomainCS,
    qvtrelationcs_Variable,
    qvtrelationcs_ExpCS,
    qvtrelationcs_DefaultValueCS,
    qvtrelationcs_ElementTemplateCS,
    qvtrelationcs_ObjectTemplateCS,
    qvtrelationcs_Namespace,
    NamedElementCS,
    qvtrelationcs_VarDeclarationIdCS,
    qvtrelationcs_TemplateVariableCS,
    qvtrelationcs_RelationCS,
    qvtrelationcs_ModelDeclCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvtrelationcs_class_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Class)


def test_qvtrelationcs_class_constructor_exists():
    assert callable(qvtrelationcs_Class.__init__)


def test_qvtrelationcs_class_constructor_args():
    sig = inspect.signature(qvtrelationcs_Class.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_property_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Property)


def test_qvtrelationcs_property_constructor_exists():
    assert callable(qvtrelationcs_Property.__init__)


def test_qvtrelationcs_property_constructor_args():
    sig = inspect.signature(qvtrelationcs_Property.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_PathNameCS)


def test_qvtrelationcs_pathnamecs_constructor_exists():
    assert callable(qvtrelationcs_PathNameCS.__init__)


def test_qvtrelationcs_pathnamecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(TemplateVariableCS)


def test_templatevariablecs_constructor_exists():
    assert callable(TemplateVariableCS.__init__)


def test_templatevariablecs_constructor_args():
    sig = inspect.signature(TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_typedmodel_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TypedModel)


def test_qvtrelationcs_typedmodel_constructor_exists():
    assert callable(qvtrelationcs_TypedModel.__init__)


def test_qvtrelationcs_typedmodel_constructor_args():
    sig = inspect.signature(qvtrelationcs_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_templatecs_is_not_abstract():
    assert not inspect.isabstract(TemplateCS)


def test_templatecs_constructor_exists():
    assert callable(TemplateCS.__init__)


def test_templatecs_constructor_args():
    sig = inspect.signature(TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_collectiontemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_CollectionTemplateCS)


def test_qvtrelationcs_collectiontemplatecs_constructor_exists():
    assert callable(qvtrelationcs_CollectionTemplateCS.__init__)


def test_qvtrelationcs_collectiontemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_CollectionTemplateCS.__init__)
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



def test_qvtrelationcs_domainpatterncs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_DomainPatternCS)


def test_qvtrelationcs_domainpatterncs_constructor_exists():
    assert callable(qvtrelationcs_DomainPatternCS.__init__)


def test_qvtrelationcs_domainpatterncs_constructor_args():
    sig = inspect.signature(qvtrelationcs_DomainPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_keydeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_KeyDeclCS)


def test_qvtrelationcs_keydeclcs_constructor_exists():
    assert callable(qvtrelationcs_KeyDeclCS.__init__)


def test_qvtrelationcs_keydeclcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_KeyDeclCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_AbstractDomainCS)


def test_qvtrelationcs_abstractdomaincs_constructor_exists():
    assert callable(qvtrelationcs_AbstractDomainCS.__init__)


def test_qvtrelationcs_abstractdomaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs_AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_transformation_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Transformation)


def test_qvtrelationcs_transformation_constructor_exists():
    assert callable(qvtrelationcs_Transformation.__init__)


def test_qvtrelationcs_transformation_constructor_args():
    sig = inspect.signature(qvtrelationcs_Transformation.__init__)
    params = list(sig.parameters.keys())



def test_classcs_is_not_abstract():
    assert not inspect.isabstract(ClassCS)


def test_classcs_constructor_exists():
    assert callable(ClassCS.__init__)


def test_classcs_constructor_args():
    sig = inspect.signature(ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TransformationCS)


def test_qvtrelationcs_transformationcs_constructor_exists():
    assert callable(qvtrelationcs_TransformationCS.__init__)


def test_qvtrelationcs_transformationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_UnitCS)


def test_qvtrelationcs_unitcs_constructor_exists():
    assert callable(qvtrelationcs_UnitCS.__init__)


def test_qvtrelationcs_unitcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(RootPackageCS)


def test_rootpackagecs_constructor_exists():
    assert callable(RootPackageCS.__init__)


def test_rootpackagecs_constructor_args():
    sig = inspect.signature(RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TopLevelCS)


def test_qvtrelationcs_toplevelcs_constructor_exists():
    assert callable(qvtrelationcs_TopLevelCS.__init__)


def test_qvtrelationcs_toplevelcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TypedRefCS)


def test_qvtrelationcs_typedrefcs_constructor_exists():
    assert callable(qvtrelationcs_TypedRefCS.__init__)


def test_qvtrelationcs_typedrefcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_element_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Element)


def test_qvtrelationcs_element_constructor_exists():
    assert callable(qvtrelationcs_Element.__init__)


def test_qvtrelationcs_element_constructor_args():
    sig = inspect.signature(qvtrelationcs_Element.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_predicatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_PredicateCS)


def test_qvtrelationcs_predicatecs_constructor_exists():
    assert callable(qvtrelationcs_PredicateCS.__init__)


def test_qvtrelationcs_predicatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_PredicateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_patterncs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_PatternCS)


def test_qvtrelationcs_patterncs_constructor_exists():
    assert callable(qvtrelationcs_PatternCS.__init__)


def test_qvtrelationcs_patterncs_constructor_args():
    sig = inspect.signature(qvtrelationcs_PatternCS.__init__)
    params = list(sig.parameters.keys())



def test_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_ParamDeclarationCS)


def test_qvtrelationcs_paramdeclarationcs_constructor_exists():
    assert callable(qvtrelationcs_ParamDeclarationCS.__init__)


def test_qvtrelationcs_paramdeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_propertytemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_PropertyTemplateCS)


def test_qvtrelationcs_propertytemplatecs_constructor_exists():
    assert callable(qvtrelationcs_PropertyTemplateCS.__init__)


def test_qvtrelationcs_propertytemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_PropertyTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_templatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TemplateCS)


def test_qvtrelationcs_templatecs_constructor_exists():
    assert callable(qvtrelationcs_TemplateCS.__init__)


def test_qvtrelationcs_templatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_TemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_vardeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_VarDeclarationCS)


def test_qvtrelationcs_vardeclarationcs_constructor_exists():
    assert callable(qvtrelationcs_VarDeclarationCS.__init__)


def test_qvtrelationcs_vardeclarationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_VarDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_querycs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_QueryCS)


def test_qvtrelationcs_querycs_constructor_exists():
    assert callable(qvtrelationcs_QueryCS.__init__)


def test_qvtrelationcs_querycs_constructor_args():
    sig = inspect.signature(qvtrelationcs_QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractdomaincs_is_not_abstract():
    assert not inspect.isabstract(AbstractDomainCS)


def test_abstractdomaincs_constructor_exists():
    assert callable(AbstractDomainCS.__init__)


def test_abstractdomaincs_constructor_args():
    sig = inspect.signature(AbstractDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_primitivetypedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_PrimitiveTypeDomainCS)


def test_qvtrelationcs_primitivetypedomaincs_constructor_exists():
    assert callable(qvtrelationcs_PrimitiveTypeDomainCS.__init__)


def test_qvtrelationcs_primitivetypedomaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs_PrimitiveTypeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_domaincs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_DomainCS)


def test_qvtrelationcs_domaincs_constructor_exists():
    assert callable(qvtrelationcs_DomainCS.__init__)


def test_qvtrelationcs_domaincs_constructor_args():
    sig = inspect.signature(qvtrelationcs_DomainCS.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckonly" in params, "Missing parameter 'isCheckonly'"
    assert "implementedBy" in params, "Missing parameter 'implementedBy'"
    assert "isEnforce" in params, "Missing parameter 'isEnforce'"
    assert "isReplace" in params, "Missing parameter 'isReplace'"

def test_qvtrelationcs_domaincs_has_isCheckonly():
    assert hasattr(qvtrelationcs_DomainCS, "isCheckonly")
    descriptor = None
    for klass in qvtrelationcs_DomainCS.__mro__:
        if "isCheckonly" in klass.__dict__:
            descriptor = klass.__dict__["isCheckonly"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs_domaincs_has_implementedBy():
    assert hasattr(qvtrelationcs_DomainCS, "implementedBy")
    descriptor = None
    for klass in qvtrelationcs_DomainCS.__mro__:
        if "implementedBy" in klass.__dict__:
            descriptor = klass.__dict__["implementedBy"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs_domaincs_has_isEnforce():
    assert hasattr(qvtrelationcs_DomainCS, "isEnforce")
    descriptor = None
    for klass in qvtrelationcs_DomainCS.__mro__:
        if "isEnforce" in klass.__dict__:
            descriptor = klass.__dict__["isEnforce"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs_domaincs_has_isReplace():
    assert hasattr(qvtrelationcs_DomainCS, "isReplace")
    descriptor = None
    for klass in qvtrelationcs_DomainCS.__mro__:
        if "isReplace" in klass.__dict__:
            descriptor = klass.__dict__["isReplace"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelationcs_variable_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Variable)


def test_qvtrelationcs_variable_constructor_exists():
    assert callable(qvtrelationcs_Variable.__init__)


def test_qvtrelationcs_variable_constructor_args():
    sig = inspect.signature(qvtrelationcs_Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_expcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_ExpCS)


def test_qvtrelationcs_expcs_constructor_exists():
    assert callable(qvtrelationcs_ExpCS.__init__)


def test_qvtrelationcs_expcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_defaultvaluecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_DefaultValueCS)


def test_qvtrelationcs_defaultvaluecs_constructor_exists():
    assert callable(qvtrelationcs_DefaultValueCS.__init__)


def test_qvtrelationcs_defaultvaluecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_DefaultValueCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_elementtemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_ElementTemplateCS)


def test_qvtrelationcs_elementtemplatecs_constructor_exists():
    assert callable(qvtrelationcs_ElementTemplateCS.__init__)


def test_qvtrelationcs_elementtemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_ElementTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_objecttemplatecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_ObjectTemplateCS)


def test_qvtrelationcs_objecttemplatecs_constructor_exists():
    assert callable(qvtrelationcs_ObjectTemplateCS.__init__)


def test_qvtrelationcs_objecttemplatecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_ObjectTemplateCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_namespace_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_Namespace)


def test_qvtrelationcs_namespace_constructor_exists():
    assert callable(qvtrelationcs_Namespace.__init__)


def test_qvtrelationcs_namespace_constructor_args():
    sig = inspect.signature(qvtrelationcs_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_vardeclarationidcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_VarDeclarationIdCS)


def test_qvtrelationcs_vardeclarationidcs_constructor_exists():
    assert callable(qvtrelationcs_VarDeclarationIdCS.__init__)


def test_qvtrelationcs_vardeclarationidcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_VarDeclarationIdCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_templatevariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_TemplateVariableCS)


def test_qvtrelationcs_templatevariablecs_constructor_exists():
    assert callable(qvtrelationcs_TemplateVariableCS.__init__)


def test_qvtrelationcs_templatevariablecs_constructor_args():
    sig = inspect.signature(qvtrelationcs_TemplateVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelationcs_relationcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_RelationCS)


def test_qvtrelationcs_relationcs_constructor_exists():
    assert callable(qvtrelationcs_RelationCS.__init__)


def test_qvtrelationcs_relationcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_RelationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"
    assert "isTop" in params, "Missing parameter 'isTop'"

def test_qvtrelationcs_relationcs_has_isDefault():
    assert hasattr(qvtrelationcs_RelationCS, "isDefault")
    descriptor = None
    for klass in qvtrelationcs_RelationCS.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)

def test_qvtrelationcs_relationcs_has_isTop():
    assert hasattr(qvtrelationcs_RelationCS, "isTop")
    descriptor = None
    for klass in qvtrelationcs_RelationCS.__mro__:
        if "isTop" in klass.__dict__:
            descriptor = klass.__dict__["isTop"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelationcs_modeldeclcs_is_not_abstract():
    assert not inspect.isabstract(qvtrelationcs_ModelDeclCS)


def test_qvtrelationcs_modeldeclcs_constructor_exists():
    assert callable(qvtrelationcs_ModelDeclCS.__init__)


def test_qvtrelationcs_modeldeclcs_constructor_args():
    sig = inspect.signature(qvtrelationcs_ModelDeclCS.__init__)
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
qvtrelationcs_Class_strategy = st.builds(
    qvtrelationcs_Class,
)
qvtrelationcs_Property_strategy = st.builds(
    qvtrelationcs_Property,
)
qvtrelationcs_PathNameCS_strategy = st.builds(
    qvtrelationcs_PathNameCS,
)
TemplateVariableCS_strategy = st.builds(
    TemplateVariableCS,
)
qvtrelationcs_TypedModel_strategy = st.builds(
    qvtrelationcs_TypedModel,
)
TemplateCS_strategy = st.builds(
    TemplateCS,
)
qvtrelationcs_CollectionTemplateCS_strategy = st.builds(
    qvtrelationcs_CollectionTemplateCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
qvtrelationcs_DomainPatternCS_strategy = st.builds(
    qvtrelationcs_DomainPatternCS,
)
qvtrelationcs_KeyDeclCS_strategy = st.builds(
    qvtrelationcs_KeyDeclCS,
)
qvtrelationcs_AbstractDomainCS_strategy = st.builds(
    qvtrelationcs_AbstractDomainCS,
)
qvtrelationcs_Transformation_strategy = st.builds(
    qvtrelationcs_Transformation,
)
ClassCS_strategy = st.builds(
    ClassCS,
)
qvtrelationcs_TransformationCS_strategy = st.builds(
    qvtrelationcs_TransformationCS,
)
qvtrelationcs_UnitCS_strategy = st.builds(
    qvtrelationcs_UnitCS,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
qvtrelationcs_TopLevelCS_strategy = st.builds(
    qvtrelationcs_TopLevelCS,
)
qvtrelationcs_TypedRefCS_strategy = st.builds(
    qvtrelationcs_TypedRefCS,
)
qvtrelationcs_Element_strategy = st.builds(
    qvtrelationcs_Element,
)
qvtrelationcs_PredicateCS_strategy = st.builds(
    qvtrelationcs_PredicateCS,
)
qvtrelationcs_PatternCS_strategy = st.builds(
    qvtrelationcs_PatternCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
qvtrelationcs_ParamDeclarationCS_strategy = st.builds(
    qvtrelationcs_ParamDeclarationCS,
)
qvtrelationcs_PropertyTemplateCS_strategy = st.builds(
    qvtrelationcs_PropertyTemplateCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
qvtrelationcs_TemplateCS_strategy = st.builds(
    qvtrelationcs_TemplateCS,
)
qvtrelationcs_VarDeclarationCS_strategy = st.builds(
    qvtrelationcs_VarDeclarationCS,
)
Relation_strategy = st.builds(
    Relation,
)
qvtrelationcs_QueryCS_strategy = st.builds(
    qvtrelationcs_QueryCS,
)
AbstractDomainCS_strategy = st.builds(
    AbstractDomainCS,
)
qvtrelationcs_PrimitiveTypeDomainCS_strategy = st.builds(
    qvtrelationcs_PrimitiveTypeDomainCS,
)
qvtrelationcs_DomainCS_strategy = st.builds(
    qvtrelationcs_DomainCS,
    isCheckonly=
        st.booleans(),
    implementedBy=
        safe_text,
    isEnforce=
        st.booleans(),
    isReplace=
        st.booleans()
)
qvtrelationcs_Variable_strategy = st.builds(
    qvtrelationcs_Variable,
)
qvtrelationcs_ExpCS_strategy = st.builds(
    qvtrelationcs_ExpCS,
)
qvtrelationcs_DefaultValueCS_strategy = st.builds(
    qvtrelationcs_DefaultValueCS,
)
qvtrelationcs_ElementTemplateCS_strategy = st.builds(
    qvtrelationcs_ElementTemplateCS,
)
qvtrelationcs_ObjectTemplateCS_strategy = st.builds(
    qvtrelationcs_ObjectTemplateCS,
)
qvtrelationcs_Namespace_strategy = st.builds(
    qvtrelationcs_Namespace,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
qvtrelationcs_VarDeclarationIdCS_strategy = st.builds(
    qvtrelationcs_VarDeclarationIdCS,
)
qvtrelationcs_TemplateVariableCS_strategy = st.builds(
    qvtrelationcs_TemplateVariableCS,
)
qvtrelationcs_RelationCS_strategy = st.builds(
    qvtrelationcs_RelationCS,
    isDefault=
        st.booleans(),
    isTop=
        st.booleans()
)
qvtrelationcs_ModelDeclCS_strategy = st.builds(
    qvtrelationcs_ModelDeclCS,
)

@given(instance=qvtrelationcs_Class_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_class_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Class)

@given(instance=qvtrelationcs_Property_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_property_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Property)

@given(instance=qvtrelationcs_PathNameCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_pathnamecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_PathNameCS)

@given(instance=TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_templatevariablecs_instantiation(instance):
    assert isinstance(instance, TemplateVariableCS)

@given(instance=qvtrelationcs_TypedModel_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_typedmodel_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TypedModel)

@given(instance=TemplateCS_strategy)
@settings(max_examples=50)
def test_templatecs_instantiation(instance):
    assert isinstance(instance, TemplateCS)

@given(instance=qvtrelationcs_CollectionTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_collectiontemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_CollectionTemplateCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=qvtrelationcs_DomainPatternCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_domainpatterncs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_DomainPatternCS)

@given(instance=qvtrelationcs_KeyDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_keydeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_KeyDeclCS)

@given(instance=qvtrelationcs_AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_AbstractDomainCS)

@given(instance=qvtrelationcs_Transformation_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_transformation_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Transformation)

@given(instance=ClassCS_strategy)
@settings(max_examples=50)
def test_classcs_instantiation(instance):
    assert isinstance(instance, ClassCS)

@given(instance=qvtrelationcs_TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_transformationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TransformationCS)

@given(instance=qvtrelationcs_UnitCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_unitcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_UnitCS)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=qvtrelationcs_TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TopLevelCS)

@given(instance=qvtrelationcs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_typedrefcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TypedRefCS)

@given(instance=qvtrelationcs_Element_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_element_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Element)

@given(instance=qvtrelationcs_PredicateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_predicatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_PredicateCS)

@given(instance=qvtrelationcs_PatternCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_patterncs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_PatternCS)

@given(instance=TypedElementCS_strategy)
@settings(max_examples=50)
def test_typedelementcs_instantiation(instance):
    assert isinstance(instance, TypedElementCS)

@given(instance=qvtrelationcs_ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_ParamDeclarationCS)

@given(instance=qvtrelationcs_PropertyTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_propertytemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_PropertyTemplateCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=qvtrelationcs_TemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_templatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TemplateCS)

@given(instance=qvtrelationcs_VarDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_vardeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_VarDeclarationCS)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=qvtrelationcs_QueryCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_querycs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_QueryCS)

@given(instance=AbstractDomainCS_strategy)
@settings(max_examples=50)
def test_abstractdomaincs_instantiation(instance):
    assert isinstance(instance, AbstractDomainCS)

@given(instance=qvtrelationcs_PrimitiveTypeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_primitivetypedomaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_PrimitiveTypeDomainCS)

@given(instance=qvtrelationcs_DomainCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_domaincs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_DomainCS)



@given(instance=qvtrelationcs_DomainCS_strategy)
def test_qvtrelationcs_domaincs_isCheckonly_setter(instance):
    original = instance.isCheckonly
    instance.isCheckonly = original
    assert instance.isCheckonly == original



@given(instance=qvtrelationcs_DomainCS_strategy)
def test_qvtrelationcs_domaincs_implementedBy_setter(instance):
    original = instance.implementedBy
    instance.implementedBy = original
    assert instance.implementedBy == original



@given(instance=qvtrelationcs_DomainCS_strategy)
def test_qvtrelationcs_domaincs_isEnforce_setter(instance):
    original = instance.isEnforce
    instance.isEnforce = original
    assert instance.isEnforce == original



@given(instance=qvtrelationcs_DomainCS_strategy)
def test_qvtrelationcs_domaincs_isReplace_setter(instance):
    original = instance.isReplace
    instance.isReplace = original
    assert instance.isReplace == original

@given(instance=qvtrelationcs_Variable_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_variable_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Variable)

@given(instance=qvtrelationcs_ExpCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_expcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_ExpCS)

@given(instance=qvtrelationcs_DefaultValueCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_defaultvaluecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_DefaultValueCS)

@given(instance=qvtrelationcs_ElementTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_elementtemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_ElementTemplateCS)

@given(instance=qvtrelationcs_ObjectTemplateCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_objecttemplatecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_ObjectTemplateCS)

@given(instance=qvtrelationcs_Namespace_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_namespace_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_Namespace)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=qvtrelationcs_VarDeclarationIdCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_vardeclarationidcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_VarDeclarationIdCS)

@given(instance=qvtrelationcs_TemplateVariableCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_templatevariablecs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_TemplateVariableCS)

@given(instance=qvtrelationcs_RelationCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_relationcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_RelationCS)



@given(instance=qvtrelationcs_RelationCS_strategy)
def test_qvtrelationcs_relationcs_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original



@given(instance=qvtrelationcs_RelationCS_strategy)
def test_qvtrelationcs_relationcs_isTop_setter(instance):
    original = instance.isTop
    instance.isTop = original
    assert instance.isTop == original

@given(instance=qvtrelationcs_ModelDeclCS_strategy)
@settings(max_examples=50)
def test_qvtrelationcs_modeldeclcs_instantiation(instance):
    assert isinstance(instance, qvtrelationcs_ModelDeclCS)

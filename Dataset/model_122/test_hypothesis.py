import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JMM_ASTNode,
    TypeDeclaration,
    JMM_InterfaceDeclaration,
    JMM_ClassDeclaration,
    AbstractMethodDeclaration,
    JMM_ConstructorDeclaration,
    JMM_MethodDeclaration,
    ASTNode,
    JMM_AbstractVariablesContainer,
    JMM_Expression,
    JMM_NamespaceAccess,
    JMM_NamedElement,
    JMM_Modifier,
    Type,
    NamedElement,
    JMM_BodyDeclaration,
    JMM_Type,
    NamespaceAccess,
    Expression,
    JMM_TypeAccess,
    JMM_Package,
    JMM_Model,
    AbstractTypeDeclaration,
    JMM_TypeDeclaration,
    JMM_AnnotationTypeDeclaration,
    AbstractVariablesContainer,
    BodyDeclaration,
    JMM_AbstractMethodDeclaration,
    JMM_AbstractTypeDeclaration,
    JMM_FieldDeclaration,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jmm_astnode_is_not_abstract():
    assert not inspect.isabstract(JMM_ASTNode)


def test_jmm_astnode_constructor_exists():
    assert callable(JMM_ASTNode.__init__)


def test_jmm_astnode_constructor_args():
    sig = inspect.signature(JMM_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_InterfaceDeclaration)


def test_jmm_interfacedeclaration_constructor_exists():
    assert callable(JMM_InterfaceDeclaration.__init__)


def test_jmm_interfacedeclaration_constructor_args():
    sig = inspect.signature(JMM_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_ClassDeclaration)


def test_jmm_classdeclaration_constructor_exists():
    assert callable(JMM_ClassDeclaration.__init__)


def test_jmm_classdeclaration_constructor_args():
    sig = inspect.signature(JMM_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_ConstructorDeclaration)


def test_jmm_constructordeclaration_constructor_exists():
    assert callable(JMM_ConstructorDeclaration.__init__)


def test_jmm_constructordeclaration_constructor_args():
    sig = inspect.signature(JMM_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_MethodDeclaration)


def test_jmm_methoddeclaration_constructor_exists():
    assert callable(JMM_MethodDeclaration.__init__)


def test_jmm_methoddeclaration_constructor_args():
    sig = inspect.signature(JMM_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jmm_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractVariablesContainer)


def test_jmm_abstractvariablescontainer_constructor_exists():
    assert callable(JMM_AbstractVariablesContainer.__init__)


def test_jmm_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(JMM_AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_jmm_expression_is_not_abstract():
    assert not inspect.isabstract(JMM_Expression)


def test_jmm_expression_constructor_exists():
    assert callable(JMM_Expression.__init__)


def test_jmm_expression_constructor_args():
    sig = inspect.signature(JMM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_jmm_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(JMM_NamespaceAccess)


def test_jmm_namespaceaccess_constructor_exists():
    assert callable(JMM_NamespaceAccess.__init__)


def test_jmm_namespaceaccess_constructor_args():
    sig = inspect.signature(JMM_NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_jmm_namedelement_is_not_abstract():
    assert not inspect.isabstract(JMM_NamedElement)


def test_jmm_namedelement_constructor_exists():
    assert callable(JMM_NamedElement.__init__)


def test_jmm_namedelement_constructor_args():
    sig = inspect.signature(JMM_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_jmm_namedelement_has_name():
    assert hasattr(JMM_NamedElement, "name")
    descriptor = None
    for klass in JMM_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jmm_namedelement_has_proxy():
    assert hasattr(JMM_NamedElement, "proxy")
    descriptor = None
    for klass in JMM_NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_jmm_modifier_is_not_abstract():
    assert not inspect.isabstract(JMM_Modifier)


def test_jmm_modifier_constructor_exists():
    assert callable(JMM_Modifier.__init__)


def test_jmm_modifier_constructor_args():
    sig = inspect.signature(JMM_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_jmm_modifier_has_inheritance():
    assert hasattr(JMM_Modifier, "inheritance")
    descriptor = None
    for klass in JMM_Modifier.__mro__:
        if "inheritance" in klass.__dict__:
            descriptor = klass.__dict__["inheritance"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jmm_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_BodyDeclaration)


def test_jmm_bodydeclaration_constructor_exists():
    assert callable(JMM_BodyDeclaration.__init__)


def test_jmm_bodydeclaration_constructor_args():
    sig = inspect.signature(JMM_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_type_is_not_abstract():
    assert not inspect.isabstract(JMM_Type)


def test_jmm_type_constructor_exists():
    assert callable(JMM_Type.__init__)


def test_jmm_type_constructor_args():
    sig = inspect.signature(JMM_Type.__init__)
    params = list(sig.parameters.keys())



def test_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jmm_typeaccess_is_not_abstract():
    assert not inspect.isabstract(JMM_TypeAccess)


def test_jmm_typeaccess_constructor_exists():
    assert callable(JMM_TypeAccess.__init__)


def test_jmm_typeaccess_constructor_args():
    sig = inspect.signature(JMM_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_jmm_package_is_not_abstract():
    assert not inspect.isabstract(JMM_Package)


def test_jmm_package_constructor_exists():
    assert callable(JMM_Package.__init__)


def test_jmm_package_constructor_args():
    sig = inspect.signature(JMM_Package.__init__)
    params = list(sig.parameters.keys())



def test_jmm_model_is_not_abstract():
    assert not inspect.isabstract(JMM_Model)


def test_jmm_model_constructor_exists():
    assert callable(JMM_Model.__init__)


def test_jmm_model_constructor_args():
    sig = inspect.signature(JMM_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jmm_model_has_name():
    assert hasattr(JMM_Model, "name")
    descriptor = None
    for klass in JMM_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_TypeDeclaration)


def test_jmm_typedeclaration_constructor_exists():
    assert callable(JMM_TypeDeclaration.__init__)


def test_jmm_typedeclaration_constructor_args():
    sig = inspect.signature(JMM_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AnnotationTypeDeclaration)


def test_jmm_annotationtypedeclaration_constructor_exists():
    assert callable(JMM_AnnotationTypeDeclaration.__init__)


def test_jmm_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JMM_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractMethodDeclaration)


def test_jmm_abstractmethoddeclaration_constructor_exists():
    assert callable(JMM_AbstractMethodDeclaration.__init__)


def test_jmm_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(JMM_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_AbstractTypeDeclaration)


def test_jmm_abstracttypedeclaration_constructor_exists():
    assert callable(JMM_AbstractTypeDeclaration.__init__)


def test_jmm_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JMM_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM_FieldDeclaration)


def test_jmm_fielddeclaration_constructor_exists():
    assert callable(JMM_FieldDeclaration.__init__)


def test_jmm_fielddeclaration_constructor_args():
    sig = inspect.signature(JMM_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "final",
        "abstract",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"


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
JMM_ASTNode_strategy = st.builds(
    JMM_ASTNode,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
JMM_InterfaceDeclaration_strategy = st.builds(
    JMM_InterfaceDeclaration,
)
JMM_ClassDeclaration_strategy = st.builds(
    JMM_ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
JMM_ConstructorDeclaration_strategy = st.builds(
    JMM_ConstructorDeclaration,
)
JMM_MethodDeclaration_strategy = st.builds(
    JMM_MethodDeclaration,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JMM_AbstractVariablesContainer_strategy = st.builds(
    JMM_AbstractVariablesContainer,
)
JMM_Expression_strategy = st.builds(
    JMM_Expression,
)
JMM_NamespaceAccess_strategy = st.builds(
    JMM_NamespaceAccess,
)
JMM_NamedElement_strategy = st.builds(
    JMM_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
JMM_Modifier_strategy = st.builds(
    JMM_Modifier,
    inheritance=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JMM_BodyDeclaration_strategy = st.builds(
    JMM_BodyDeclaration,
)
JMM_Type_strategy = st.builds(
    JMM_Type,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
Expression_strategy = st.builds(
    Expression,
)
JMM_TypeAccess_strategy = st.builds(
    JMM_TypeAccess,
)
JMM_Package_strategy = st.builds(
    JMM_Package,
)
JMM_Model_strategy = st.builds(
    JMM_Model,
    name=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JMM_TypeDeclaration_strategy = st.builds(
    JMM_TypeDeclaration,
)
JMM_AnnotationTypeDeclaration_strategy = st.builds(
    JMM_AnnotationTypeDeclaration,
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JMM_AbstractMethodDeclaration_strategy = st.builds(
    JMM_AbstractMethodDeclaration,
)
JMM_AbstractTypeDeclaration_strategy = st.builds(
    JMM_AbstractTypeDeclaration,
)
JMM_FieldDeclaration_strategy = st.builds(
    JMM_FieldDeclaration,
)

@given(instance=JMM_ASTNode_strategy)
@settings(max_examples=50)
def test_jmm_astnode_instantiation(instance):
    assert isinstance(instance, JMM_ASTNode)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=JMM_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, JMM_InterfaceDeclaration)

@given(instance=JMM_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_classdeclaration_instantiation(instance):
    assert isinstance(instance, JMM_ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=JMM_ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_constructordeclaration_instantiation(instance):
    assert isinstance(instance, JMM_ConstructorDeclaration)

@given(instance=JMM_MethodDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_methoddeclaration_instantiation(instance):
    assert isinstance(instance, JMM_MethodDeclaration)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JMM_AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_jmm_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, JMM_AbstractVariablesContainer)

@given(instance=JMM_Expression_strategy)
@settings(max_examples=50)
def test_jmm_expression_instantiation(instance):
    assert isinstance(instance, JMM_Expression)

@given(instance=JMM_NamespaceAccess_strategy)
@settings(max_examples=50)
def test_jmm_namespaceaccess_instantiation(instance):
    assert isinstance(instance, JMM_NamespaceAccess)

@given(instance=JMM_NamedElement_strategy)
@settings(max_examples=50)
def test_jmm_namedelement_instantiation(instance):
    assert isinstance(instance, JMM_NamedElement)



@given(instance=JMM_NamedElement_strategy)
def test_jmm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=JMM_NamedElement_strategy)
def test_jmm_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=JMM_Modifier_strategy)
@settings(max_examples=50)
def test_jmm_modifier_instantiation(instance):
    assert isinstance(instance, JMM_Modifier)



@given(instance=JMM_Modifier_strategy)
def test_jmm_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JMM_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_bodydeclaration_instantiation(instance):
    assert isinstance(instance, JMM_BodyDeclaration)

@given(instance=JMM_Type_strategy)
@settings(max_examples=50)
def test_jmm_type_instantiation(instance):
    assert isinstance(instance, JMM_Type)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JMM_TypeAccess_strategy)
@settings(max_examples=50)
def test_jmm_typeaccess_instantiation(instance):
    assert isinstance(instance, JMM_TypeAccess)

@given(instance=JMM_Package_strategy)
@settings(max_examples=50)
def test_jmm_package_instantiation(instance):
    assert isinstance(instance, JMM_Package)

@given(instance=JMM_Model_strategy)
@settings(max_examples=50)
def test_jmm_model_instantiation(instance):
    assert isinstance(instance, JMM_Model)



@given(instance=JMM_Model_strategy)
def test_jmm_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JMM_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_typedeclaration_instantiation(instance):
    assert isinstance(instance, JMM_TypeDeclaration)

@given(instance=JMM_AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AnnotationTypeDeclaration)

@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JMM_AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AbstractMethodDeclaration)

@given(instance=JMM_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JMM_AbstractTypeDeclaration)

@given(instance=JMM_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_jmm_fielddeclaration_instantiation(instance):
    assert isinstance(instance, JMM_FieldDeclaration)

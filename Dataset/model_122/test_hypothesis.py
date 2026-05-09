import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JMM::ASTNode,
    TypeDeclaration,
    JMM::InterfaceDeclaration,
    JMM::ClassDeclaration,
    AbstractMethodDeclaration,
    JMM::ConstructorDeclaration,
    JMM::MethodDeclaration,
    ASTNode,
    JMM::NamespaceAccess,
    JMM::Expression,
    JMM::AbstractVariablesContainer,
    JMM::NamedElement,
    JMM::Modifier,
    Type,
    NamedElement,
    JMM::BodyDeclaration,
    JMM::Type,
    NamespaceAccess,
    Expression,
    JMM::TypeAccess,
    JMM::Package,
    JMM::Model,
    AbstractTypeDeclaration,
    JMM::TypeDeclaration,
    JMM::AnnotationTypeDeclaration,
    AbstractVariablesContainer,
    BodyDeclaration,
    JMM::AbstractTypeDeclaration,
    JMM::AbstractMethodDeclaration,
    JMM::FieldDeclaration,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jmm::astnode_is_not_abstract():
    assert not inspect.isabstract(JMM::ASTNode)


def test_jmm::astnode_constructor_exists():
    assert callable(JMM::ASTNode.__init__)


def test_jmm::astnode_constructor_args():
    sig = inspect.signature(JMM::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::InterfaceDeclaration)


def test_jmm::interfacedeclaration_constructor_exists():
    assert callable(JMM::InterfaceDeclaration.__init__)


def test_jmm::interfacedeclaration_constructor_args():
    sig = inspect.signature(JMM::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::ClassDeclaration)


def test_jmm::classdeclaration_constructor_exists():
    assert callable(JMM::ClassDeclaration.__init__)


def test_jmm::classdeclaration_constructor_args():
    sig = inspect.signature(JMM::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::ConstructorDeclaration)


def test_jmm::constructordeclaration_constructor_exists():
    assert callable(JMM::ConstructorDeclaration.__init__)


def test_jmm::constructordeclaration_constructor_args():
    sig = inspect.signature(JMM::ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::MethodDeclaration)


def test_jmm::methoddeclaration_constructor_exists():
    assert callable(JMM::MethodDeclaration.__init__)


def test_jmm::methoddeclaration_constructor_args():
    sig = inspect.signature(JMM::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_jmm::namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(JMM::NamespaceAccess)


def test_jmm::namespaceaccess_constructor_exists():
    assert callable(JMM::NamespaceAccess.__init__)


def test_jmm::namespaceaccess_constructor_args():
    sig = inspect.signature(JMM::NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_jmm::expression_is_not_abstract():
    assert not inspect.isabstract(JMM::Expression)


def test_jmm::expression_constructor_exists():
    assert callable(JMM::Expression.__init__)


def test_jmm::expression_constructor_args():
    sig = inspect.signature(JMM::Expression.__init__)
    params = list(sig.parameters.keys())



def test_jmm::abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(JMM::AbstractVariablesContainer)


def test_jmm::abstractvariablescontainer_constructor_exists():
    assert callable(JMM::AbstractVariablesContainer.__init__)


def test_jmm::abstractvariablescontainer_constructor_args():
    sig = inspect.signature(JMM::AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_jmm::namedelement_is_not_abstract():
    assert not inspect.isabstract(JMM::NamedElement)


def test_jmm::namedelement_constructor_exists():
    assert callable(JMM::NamedElement.__init__)


def test_jmm::namedelement_constructor_args():
    sig = inspect.signature(JMM::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_jmm::namedelement_has_name():
    assert hasattr(JMM::NamedElement, "name")
    descriptor = None
    for klass in JMM::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jmm::namedelement_has_proxy():
    assert hasattr(JMM::NamedElement, "proxy")
    descriptor = None
    for klass in JMM::NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_jmm::modifier_is_not_abstract():
    assert not inspect.isabstract(JMM::Modifier)


def test_jmm::modifier_constructor_exists():
    assert callable(JMM::Modifier.__init__)


def test_jmm::modifier_constructor_args():
    sig = inspect.signature(JMM::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"

def test_jmm::modifier_has_inheritance():
    assert hasattr(JMM::Modifier, "inheritance")
    descriptor = None
    for klass in JMM::Modifier.__mro__:
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



def test_jmm::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::BodyDeclaration)


def test_jmm::bodydeclaration_constructor_exists():
    assert callable(JMM::BodyDeclaration.__init__)


def test_jmm::bodydeclaration_constructor_args():
    sig = inspect.signature(JMM::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::type_is_not_abstract():
    assert not inspect.isabstract(JMM::Type)


def test_jmm::type_constructor_exists():
    assert callable(JMM::Type.__init__)


def test_jmm::type_constructor_args():
    sig = inspect.signature(JMM::Type.__init__)
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



def test_jmm::typeaccess_is_not_abstract():
    assert not inspect.isabstract(JMM::TypeAccess)


def test_jmm::typeaccess_constructor_exists():
    assert callable(JMM::TypeAccess.__init__)


def test_jmm::typeaccess_constructor_args():
    sig = inspect.signature(JMM::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_jmm::package_is_not_abstract():
    assert not inspect.isabstract(JMM::Package)


def test_jmm::package_constructor_exists():
    assert callable(JMM::Package.__init__)


def test_jmm::package_constructor_args():
    sig = inspect.signature(JMM::Package.__init__)
    params = list(sig.parameters.keys())



def test_jmm::model_is_not_abstract():
    assert not inspect.isabstract(JMM::Model)


def test_jmm::model_constructor_exists():
    assert callable(JMM::Model.__init__)


def test_jmm::model_constructor_args():
    sig = inspect.signature(JMM::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jmm::model_has_name():
    assert hasattr(JMM::Model, "name")
    descriptor = None
    for klass in JMM::Model.__mro__:
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



def test_jmm::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::TypeDeclaration)


def test_jmm::typedeclaration_constructor_exists():
    assert callable(JMM::TypeDeclaration.__init__)


def test_jmm::typedeclaration_constructor_args():
    sig = inspect.signature(JMM::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::AnnotationTypeDeclaration)


def test_jmm::annotationtypedeclaration_constructor_exists():
    assert callable(JMM::AnnotationTypeDeclaration.__init__)


def test_jmm::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(JMM::AnnotationTypeDeclaration.__init__)
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



def test_jmm::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::AbstractTypeDeclaration)


def test_jmm::abstracttypedeclaration_constructor_exists():
    assert callable(JMM::AbstractTypeDeclaration.__init__)


def test_jmm::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JMM::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::AbstractMethodDeclaration)


def test_jmm::abstractmethoddeclaration_constructor_exists():
    assert callable(JMM::AbstractMethodDeclaration.__init__)


def test_jmm::abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(JMM::AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_jmm::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JMM::FieldDeclaration)


def test_jmm::fielddeclaration_constructor_exists():
    assert callable(JMM::FieldDeclaration.__init__)


def test_jmm::fielddeclaration_constructor_args():
    sig = inspect.signature(JMM::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "abstract",
        "none",
        "final",
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
JMM::ASTNode_strategy = st.builds(
    JMM::ASTNode,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
JMM::InterfaceDeclaration_strategy = st.builds(
    JMM::InterfaceDeclaration,
)
JMM::ClassDeclaration_strategy = st.builds(
    JMM::ClassDeclaration,
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
JMM::ConstructorDeclaration_strategy = st.builds(
    JMM::ConstructorDeclaration,
)
JMM::MethodDeclaration_strategy = st.builds(
    JMM::MethodDeclaration,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JMM::NamespaceAccess_strategy = st.builds(
    JMM::NamespaceAccess,
)
JMM::Expression_strategy = st.builds(
    JMM::Expression,
)
JMM::AbstractVariablesContainer_strategy = st.builds(
    JMM::AbstractVariablesContainer,
)
JMM::NamedElement_strategy = st.builds(
    JMM::NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
JMM::Modifier_strategy = st.builds(
    JMM::Modifier,
    inheritance=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JMM::BodyDeclaration_strategy = st.builds(
    JMM::BodyDeclaration,
)
JMM::Type_strategy = st.builds(
    JMM::Type,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
Expression_strategy = st.builds(
    Expression,
)
JMM::TypeAccess_strategy = st.builds(
    JMM::TypeAccess,
)
JMM::Package_strategy = st.builds(
    JMM::Package,
)
JMM::Model_strategy = st.builds(
    JMM::Model,
    name=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JMM::TypeDeclaration_strategy = st.builds(
    JMM::TypeDeclaration,
)
JMM::AnnotationTypeDeclaration_strategy = st.builds(
    JMM::AnnotationTypeDeclaration,
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JMM::AbstractTypeDeclaration_strategy = st.builds(
    JMM::AbstractTypeDeclaration,
)
JMM::AbstractMethodDeclaration_strategy = st.builds(
    JMM::AbstractMethodDeclaration,
)
JMM::FieldDeclaration_strategy = st.builds(
    JMM::FieldDeclaration,
)

@given(instance=JMM::ASTNode_strategy)
@settings(max_examples=50)
def test_jmm::astnode_instantiation(instance):
    assert isinstance(instance, JMM::ASTNode)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=JMM::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, JMM::InterfaceDeclaration)

@given(instance=JMM::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::classdeclaration_instantiation(instance):
    assert isinstance(instance, JMM::ClassDeclaration)

@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)

@given(instance=JMM::ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::constructordeclaration_instantiation(instance):
    assert isinstance(instance, JMM::ConstructorDeclaration)

@given(instance=JMM::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::methoddeclaration_instantiation(instance):
    assert isinstance(instance, JMM::MethodDeclaration)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JMM::NamespaceAccess_strategy)
@settings(max_examples=50)
def test_jmm::namespaceaccess_instantiation(instance):
    assert isinstance(instance, JMM::NamespaceAccess)

@given(instance=JMM::Expression_strategy)
@settings(max_examples=50)
def test_jmm::expression_instantiation(instance):
    assert isinstance(instance, JMM::Expression)

@given(instance=JMM::AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_jmm::abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, JMM::AbstractVariablesContainer)

@given(instance=JMM::NamedElement_strategy)
@settings(max_examples=50)
def test_jmm::namedelement_instantiation(instance):
    assert isinstance(instance, JMM::NamedElement)

@given(instance=JMM::NamedElement_strategy)
def test_jmm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JMM::NamedElement_strategy)
def test_jmm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JMM::NamedElement_strategy)
def test_jmm::namedelement_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=JMM::NamedElement_strategy)
def test_jmm::namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=JMM::Modifier_strategy)
@settings(max_examples=50)
def test_jmm::modifier_instantiation(instance):
    assert isinstance(instance, JMM::Modifier)

@given(instance=JMM::Modifier_strategy)
def test_jmm::modifier_inheritance_type(instance):
    assert isinstance(instance.inheritance, str)


@given(instance=JMM::Modifier_strategy)
def test_jmm::modifier_inheritance_setter(instance):
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

@given(instance=JMM::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::bodydeclaration_instantiation(instance):
    assert isinstance(instance, JMM::BodyDeclaration)

@given(instance=JMM::Type_strategy)
@settings(max_examples=50)
def test_jmm::type_instantiation(instance):
    assert isinstance(instance, JMM::Type)

@given(instance=NamespaceAccess_strategy)
@settings(max_examples=50)
def test_namespaceaccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JMM::TypeAccess_strategy)
@settings(max_examples=50)
def test_jmm::typeaccess_instantiation(instance):
    assert isinstance(instance, JMM::TypeAccess)

@given(instance=JMM::Package_strategy)
@settings(max_examples=50)
def test_jmm::package_instantiation(instance):
    assert isinstance(instance, JMM::Package)

@given(instance=JMM::Model_strategy)
@settings(max_examples=50)
def test_jmm::model_instantiation(instance):
    assert isinstance(instance, JMM::Model)

@given(instance=JMM::Model_strategy)
def test_jmm::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JMM::Model_strategy)
def test_jmm::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JMM::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::typedeclaration_instantiation(instance):
    assert isinstance(instance, JMM::TypeDeclaration)

@given(instance=JMM::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, JMM::AnnotationTypeDeclaration)

@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=50)
def test_abstractvariablescontainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JMM::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JMM::AbstractTypeDeclaration)

@given(instance=JMM::AbstractMethodDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::abstractmethoddeclaration_instantiation(instance):
    assert isinstance(instance, JMM::AbstractMethodDeclaration)

@given(instance=JMM::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_jmm::fielddeclaration_instantiation(instance):
    assert isinstance(instance, JMM::FieldDeclaration)

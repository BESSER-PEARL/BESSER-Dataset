import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    BodyDeclaration,
    JAVA::AbstractTypeDeclaration,
    NamedElement,
    JAVA::Package,
    Expression,
    JAVA::FieldDeclaration,
    JAVA::BodyDeclaration,
    AbstractTypeDeclaration,
    JAVA::TypeDeclaration,
    JAVA::ASTNode,
    ASTNode,
    JAVA::Expression,
    JAVA::NamedElement,
    JAVA::Type,
    JAVA::TypeAccess,
    TypeDeclaration,
    JAVA::InterfaceDeclaration,
    JAVA::ClassDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::AbstractTypeDeclaration)


def test_java::abstracttypedeclaration_constructor_exists():
    assert callable(JAVA::AbstractTypeDeclaration.__init__)


def test_java::abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JAVA::AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java::package_is_not_abstract():
    assert not inspect.isabstract(JAVA::Package)


def test_java::package_constructor_exists():
    assert callable(JAVA::Package.__init__)


def test_java::package_constructor_args():
    sig = inspect.signature(JAVA::Package.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::FieldDeclaration)


def test_java::fielddeclaration_constructor_exists():
    assert callable(JAVA::FieldDeclaration.__init__)


def test_java::fielddeclaration_constructor_args():
    sig = inspect.signature(JAVA::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::BodyDeclaration)


def test_java::bodydeclaration_constructor_exists():
    assert callable(JAVA::BodyDeclaration.__init__)


def test_java::bodydeclaration_constructor_args():
    sig = inspect.signature(JAVA::BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::TypeDeclaration)


def test_java::typedeclaration_constructor_exists():
    assert callable(JAVA::TypeDeclaration.__init__)


def test_java::typedeclaration_constructor_args():
    sig = inspect.signature(JAVA::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::astnode_is_not_abstract():
    assert not inspect.isabstract(JAVA::ASTNode)


def test_java::astnode_constructor_exists():
    assert callable(JAVA::ASTNode.__init__)


def test_java::astnode_constructor_args():
    sig = inspect.signature(JAVA::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java::expression_is_not_abstract():
    assert not inspect.isabstract(JAVA::Expression)


def test_java::expression_constructor_exists():
    assert callable(JAVA::Expression.__init__)


def test_java::expression_constructor_args():
    sig = inspect.signature(JAVA::Expression.__init__)
    params = list(sig.parameters.keys())



def test_java::namedelement_is_not_abstract():
    assert not inspect.isabstract(JAVA::NamedElement)


def test_java::namedelement_constructor_exists():
    assert callable(JAVA::NamedElement.__init__)


def test_java::namedelement_constructor_args():
    sig = inspect.signature(JAVA::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"

def test_java::namedelement_has_name():
    assert hasattr(JAVA::NamedElement, "name")
    descriptor = None
    for klass in JAVA::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::namedelement_has_proxy():
    assert hasattr(JAVA::NamedElement, "proxy")
    descriptor = None
    for klass in JAVA::NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(JAVA::Type)


def test_java::type_constructor_exists():
    assert callable(JAVA::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(JAVA::Type.__init__)
    params = list(sig.parameters.keys())



def test_java::typeaccess_is_not_abstract():
    assert not inspect.isabstract(JAVA::TypeAccess)


def test_java::typeaccess_constructor_exists():
    assert callable(JAVA::TypeAccess.__init__)


def test_java::typeaccess_constructor_args():
    sig = inspect.signature(JAVA::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::InterfaceDeclaration)


def test_java::interfacedeclaration_constructor_exists():
    assert callable(JAVA::InterfaceDeclaration.__init__)


def test_java::interfacedeclaration_constructor_args():
    sig = inspect.signature(JAVA::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA::ClassDeclaration)


def test_java::classdeclaration_constructor_exists():
    assert callable(JAVA::ClassDeclaration.__init__)


def test_java::classdeclaration_constructor_args():
    sig = inspect.signature(JAVA::ClassDeclaration.__init__)
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
Type_strategy = st.builds(
    Type,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
JAVA::AbstractTypeDeclaration_strategy = st.builds(
    JAVA::AbstractTypeDeclaration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JAVA::Package_strategy = st.builds(
    JAVA::Package,
)
Expression_strategy = st.builds(
    Expression,
)
JAVA::FieldDeclaration_strategy = st.builds(
    JAVA::FieldDeclaration,
)
JAVA::BodyDeclaration_strategy = st.builds(
    JAVA::BodyDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JAVA::TypeDeclaration_strategy = st.builds(
    JAVA::TypeDeclaration,
)
JAVA::ASTNode_strategy = st.builds(
    JAVA::ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JAVA::Expression_strategy = st.builds(
    JAVA::Expression,
)
JAVA::NamedElement_strategy = st.builds(
    JAVA::NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
JAVA::Type_strategy = st.builds(
    JAVA::Type,
)
JAVA::TypeAccess_strategy = st.builds(
    JAVA::TypeAccess,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
JAVA::InterfaceDeclaration_strategy = st.builds(
    JAVA::InterfaceDeclaration,
)
JAVA::ClassDeclaration_strategy = st.builds(
    JAVA::ClassDeclaration,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JAVA::AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::AbstractTypeDeclaration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JAVA::Package_strategy)
@settings(max_examples=50)
def test_java::package_instantiation(instance):
    assert isinstance(instance, JAVA::Package)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JAVA::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java::fielddeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::FieldDeclaration)

@given(instance=JAVA::BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java::bodydeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::BodyDeclaration)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JAVA::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java::typedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::TypeDeclaration)

@given(instance=JAVA::ASTNode_strategy)
@settings(max_examples=50)
def test_java::astnode_instantiation(instance):
    assert isinstance(instance, JAVA::ASTNode)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JAVA::Expression_strategy)
@settings(max_examples=50)
def test_java::expression_instantiation(instance):
    assert isinstance(instance, JAVA::Expression)

@given(instance=JAVA::NamedElement_strategy)
@settings(max_examples=50)
def test_java::namedelement_instantiation(instance):
    assert isinstance(instance, JAVA::NamedElement)

@given(instance=JAVA::NamedElement_strategy)
def test_java::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JAVA::NamedElement_strategy)
def test_java::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JAVA::NamedElement_strategy)
def test_java::namedelement_proxy_type(instance):
    assert isinstance(instance.proxy, bool)


@given(instance=JAVA::NamedElement_strategy)
def test_java::namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original

@given(instance=JAVA::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, JAVA::Type)

@given(instance=JAVA::TypeAccess_strategy)
@settings(max_examples=50)
def test_java::typeaccess_instantiation(instance):
    assert isinstance(instance, JAVA::TypeAccess)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=JAVA::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::InterfaceDeclaration)

@given(instance=JAVA::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java::classdeclaration_instantiation(instance):
    assert isinstance(instance, JAVA::ClassDeclaration)

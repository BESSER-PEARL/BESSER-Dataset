import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    BodyDeclaration,
    JAVA_AbstractTypeDeclaration,
    NamedElement,
    JAVA_Package,
    Expression,
    JAVA_FieldDeclaration,
    JAVA_BodyDeclaration,
    AbstractTypeDeclaration,
    JAVA_TypeDeclaration,
    JAVA_ASTNode,
    ASTNode,
    JAVA_Expression,
    JAVA_NamedElement,
    JAVA_Type,
    JAVA_TypeAccess,
    TypeDeclaration,
    JAVA_InterfaceDeclaration,
    JAVA_ClassDeclaration,
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



def test_java_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_AbstractTypeDeclaration)


def test_java_abstracttypedeclaration_constructor_exists():
    assert callable(JAVA_AbstractTypeDeclaration.__init__)


def test_java_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(JAVA_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(JAVA_Package)


def test_java_package_constructor_exists():
    assert callable(JAVA_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(JAVA_Package.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_FieldDeclaration)


def test_java_fielddeclaration_constructor_exists():
    assert callable(JAVA_FieldDeclaration.__init__)


def test_java_fielddeclaration_constructor_args():
    sig = inspect.signature(JAVA_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_BodyDeclaration)


def test_java_bodydeclaration_constructor_exists():
    assert callable(JAVA_BodyDeclaration.__init__)


def test_java_bodydeclaration_constructor_args():
    sig = inspect.signature(JAVA_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_TypeDeclaration)


def test_java_typedeclaration_constructor_exists():
    assert callable(JAVA_TypeDeclaration.__init__)


def test_java_typedeclaration_constructor_args():
    sig = inspect.signature(JAVA_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_astnode_is_not_abstract():
    assert not inspect.isabstract(JAVA_ASTNode)


def test_java_astnode_constructor_exists():
    assert callable(JAVA_ASTNode.__init__)


def test_java_astnode_constructor_args():
    sig = inspect.signature(JAVA_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_java_expression_is_not_abstract():
    assert not inspect.isabstract(JAVA_Expression)


def test_java_expression_constructor_exists():
    assert callable(JAVA_Expression.__init__)


def test_java_expression_constructor_args():
    sig = inspect.signature(JAVA_Expression.__init__)
    params = list(sig.parameters.keys())



def test_java_namedelement_is_not_abstract():
    assert not inspect.isabstract(JAVA_NamedElement)


def test_java_namedelement_constructor_exists():
    assert callable(JAVA_NamedElement.__init__)


def test_java_namedelement_constructor_args():
    sig = inspect.signature(JAVA_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "proxy" in params, "Missing parameter 'proxy'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_namedelement_has_proxy():
    assert hasattr(JAVA_NamedElement, "proxy")
    descriptor = None
    for klass in JAVA_NamedElement.__mro__:
        if "proxy" in klass.__dict__:
            descriptor = klass.__dict__["proxy"]
            break
    assert isinstance(descriptor, property)

def test_java_namedelement_has_name():
    assert hasattr(JAVA_NamedElement, "name")
    descriptor = None
    for klass in JAVA_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(JAVA_Type)


def test_java_type_constructor_exists():
    assert callable(JAVA_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(JAVA_Type.__init__)
    params = list(sig.parameters.keys())



def test_java_typeaccess_is_not_abstract():
    assert not inspect.isabstract(JAVA_TypeAccess)


def test_java_typeaccess_constructor_exists():
    assert callable(JAVA_TypeAccess.__init__)


def test_java_typeaccess_constructor_args():
    sig = inspect.signature(JAVA_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_InterfaceDeclaration)


def test_java_interfacedeclaration_constructor_exists():
    assert callable(JAVA_InterfaceDeclaration.__init__)


def test_java_interfacedeclaration_constructor_args():
    sig = inspect.signature(JAVA_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_java_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(JAVA_ClassDeclaration)


def test_java_classdeclaration_constructor_exists():
    assert callable(JAVA_ClassDeclaration.__init__)


def test_java_classdeclaration_constructor_args():
    sig = inspect.signature(JAVA_ClassDeclaration.__init__)
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
JAVA_AbstractTypeDeclaration_strategy = st.builds(
    JAVA_AbstractTypeDeclaration,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JAVA_Package_strategy = st.builds(
    JAVA_Package,
)
Expression_strategy = st.builds(
    Expression,
)
JAVA_FieldDeclaration_strategy = st.builds(
    JAVA_FieldDeclaration,
)
JAVA_BodyDeclaration_strategy = st.builds(
    JAVA_BodyDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
JAVA_TypeDeclaration_strategy = st.builds(
    JAVA_TypeDeclaration,
)
JAVA_ASTNode_strategy = st.builds(
    JAVA_ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
JAVA_Expression_strategy = st.builds(
    JAVA_Expression,
)
JAVA_NamedElement_strategy = st.builds(
    JAVA_NamedElement,
    proxy=
        st.booleans(),
    name=
        safe_text
)
JAVA_Type_strategy = st.builds(
    JAVA_Type,
)
JAVA_TypeAccess_strategy = st.builds(
    JAVA_TypeAccess,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
JAVA_InterfaceDeclaration_strategy = st.builds(
    JAVA_InterfaceDeclaration,
)
JAVA_ClassDeclaration_strategy = st.builds(
    JAVA_ClassDeclaration,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=BodyDeclaration_strategy)
@settings(max_examples=50)
def test_bodydeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)

@given(instance=JAVA_AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_AbstractTypeDeclaration)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JAVA_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, JAVA_Package)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=JAVA_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_java_fielddeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_FieldDeclaration)

@given(instance=JAVA_BodyDeclaration_strategy)
@settings(max_examples=50)
def test_java_bodydeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_BodyDeclaration)

@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=50)
def test_abstracttypedeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)

@given(instance=JAVA_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_java_typedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_TypeDeclaration)

@given(instance=JAVA_ASTNode_strategy)
@settings(max_examples=50)
def test_java_astnode_instantiation(instance):
    assert isinstance(instance, JAVA_ASTNode)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=JAVA_Expression_strategy)
@settings(max_examples=50)
def test_java_expression_instantiation(instance):
    assert isinstance(instance, JAVA_Expression)

@given(instance=JAVA_NamedElement_strategy)
@settings(max_examples=50)
def test_java_namedelement_instantiation(instance):
    assert isinstance(instance, JAVA_NamedElement)



@given(instance=JAVA_NamedElement_strategy)
def test_java_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original



@given(instance=JAVA_NamedElement_strategy)
def test_java_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JAVA_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, JAVA_Type)

@given(instance=JAVA_TypeAccess_strategy)
@settings(max_examples=50)
def test_java_typeaccess_instantiation(instance):
    assert isinstance(instance, JAVA_TypeAccess)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=JAVA_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_java_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_InterfaceDeclaration)

@given(instance=JAVA_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_java_classdeclaration_instantiation(instance):
    assert isinstance(instance, JAVA_ClassDeclaration)

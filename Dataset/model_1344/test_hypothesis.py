import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myAtl_EObject,
    NavigatingExpCS,
    myAtl_NavigatingExpCS_Base,
    NavigatingExpCS_Base,
    myAtl_IndexExpCS,
    myAtl_UnaryOperatorCS,
    InfixedExpCS,
    myAtl_InfixExpCS,
    myAtl_PrefixedExpCS,
    BinaryOperatorCS,
    myAtl_NavigationOperatorCS,
    myAtl_InfixOperatorCS,
    myAtl_BinaryOperatorCS,
    ExpCS,
    myAtl_InfixedExpCS,
    NavigatingArgExpCS,
    IndexExpCS,
    PrefixedExpCS,
    myAtl_PrefixExpCS,
    myAtl_PrimaryExpCS,
    myAtl_LetVariableCS,
    myAtl_NavigatingSemiArgCS,
    myAtl_NavigatingCommaArgCS,
    myAtl_NavigatingBarArgCS,
    myAtl_NavigatingArgExpCS,
    myAtl_NavigatingArgCS,
    myAtl_TypeLiteralExpCS,
    TypeExpCS,
    myAtl_TypeNameExpCS,
    myAtl_TypeLiteralCS,
    PrimitiveLiteralExpCS,
    myAtl_NullLiteralExpCS,
    myAtl_StringLiteralExpCS,
    myAtl_BooleanLiteralExpCS,
    myAtl_InvalidLiteralExpCS,
    myAtl_UnlimitedNaturalLiteralExpCS,
    myAtl_NumberLiteralExpCS,
    myAtl_TupleLiteralPartCS,
    PrimaryExpCS,
    myAtl_TupleLiteralExpCS,
    myAtl_SelfExpCS,
    myAtl_StringExpCs,
    myAtl_NavigatingExpCS,
    myAtl_LetExpCS,
    myAtl_NestedExpCS,
    myAtl_IfExpCS,
    myAtl_PrimitiveLiteralExpCS,
    myAtl_tuplePartCS,
    TypeLiteralCS,
    myAtl_PrimitiveTypeCS,
    myAtl_TupleTypeCS,
    myAtl_CollectionTypeCS,
    myAtl_TypeExpCS,
    Statement,
    myAtl_BindingStat,
    myAtl_Statement,
    myAtl_Binding,
    OutPatternElement,
    myAtl_ForEachOutPatternElement,
    myAtl_SimpleOutPatternElement,
    myAtl_OutPatternElement,
    myAtl_InPatternElement,
    myAtl_ATLType,
    myAtl_ATLDefCS,
    myAtl_ExpCS,
    myAtl_ATLParameterCS,
    myAtl_ActionBlock,
    myAtl_OutPattern,
    myAtl_RuleVariableDeclaration,
    myAtl_InPattern,
    ModuleElement,
    myAtl_QueryRule,
    myAtl_Helper,
    myAtl_CalledRule,
    myAtl_MatchedRule,
    myAtl_ModuleElement,
    myAtl_NameExpCS,
    myAtl_Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_myatl_eobject_is_not_abstract():
    assert not inspect.isabstract(myAtl_EObject)


def test_myatl_eobject_constructor_exists():
    assert callable(myAtl_EObject.__init__)


def test_myatl_eobject_constructor_args():
    sig = inspect.signature(myAtl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigatingExpCS)


def test_navigatingexpcs_constructor_exists():
    assert callable(NavigatingExpCS.__init__)


def test_navigatingexpcs_constructor_args():
    sig = inspect.signature(NavigatingExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_navigatingexpcs_base_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingExpCS_Base)


def test_myatl_navigatingexpcs_base_constructor_exists():
    assert callable(myAtl_NavigatingExpCS_Base.__init__)


def test_myatl_navigatingexpcs_base_constructor_args():
    sig = inspect.signature(myAtl_NavigatingExpCS_Base.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexpcs_base_is_not_abstract():
    assert not inspect.isabstract(NavigatingExpCS_Base)


def test_navigatingexpcs_base_constructor_exists():
    assert callable(NavigatingExpCS_Base.__init__)


def test_navigatingexpcs_base_constructor_args():
    sig = inspect.signature(NavigatingExpCS_Base.__init__)
    params = list(sig.parameters.keys())



def test_myatl_indexexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_IndexExpCS)


def test_myatl_indexexpcs_constructor_exists():
    assert callable(myAtl_IndexExpCS.__init__)


def test_myatl_indexexpcs_constructor_args():
    sig = inspect.signature(myAtl_IndexExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_unaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_UnaryOperatorCS)


def test_myatl_unaryoperatorcs_constructor_exists():
    assert callable(myAtl_UnaryOperatorCS.__init__)


def test_myatl_unaryoperatorcs_constructor_args():
    sig = inspect.signature(myAtl_UnaryOperatorCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_unaryoperatorcs_has_name():
    assert hasattr(myAtl_UnaryOperatorCS, "name")
    descriptor = None
    for klass in myAtl_UnaryOperatorCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_infixedexpcs_is_not_abstract():
    assert not inspect.isabstract(InfixedExpCS)


def test_infixedexpcs_constructor_exists():
    assert callable(InfixedExpCS.__init__)


def test_infixedexpcs_constructor_args():
    sig = inspect.signature(InfixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_infixexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_InfixExpCS)


def test_myatl_infixexpcs_constructor_exists():
    assert callable(myAtl_InfixExpCS.__init__)


def test_myatl_infixexpcs_constructor_args():
    sig = inspect.signature(myAtl_InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_prefixedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_PrefixedExpCS)


def test_myatl_prefixedexpcs_constructor_exists():
    assert callable(myAtl_PrefixedExpCS.__init__)


def test_myatl_prefixedexpcs_constructor_args():
    sig = inspect.signature(myAtl_PrefixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorCS)


def test_binaryoperatorcs_constructor_exists():
    assert callable(BinaryOperatorCS.__init__)


def test_binaryoperatorcs_constructor_args():
    sig = inspect.signature(BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_navigationoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigationOperatorCS)


def test_myatl_navigationoperatorcs_constructor_exists():
    assert callable(myAtl_NavigationOperatorCS.__init__)


def test_myatl_navigationoperatorcs_constructor_args():
    sig = inspect.signature(myAtl_NavigationOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_infixoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_InfixOperatorCS)


def test_myatl_infixoperatorcs_constructor_exists():
    assert callable(myAtl_InfixOperatorCS.__init__)


def test_myatl_infixoperatorcs_constructor_args():
    sig = inspect.signature(myAtl_InfixOperatorCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_binaryoperatorcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_BinaryOperatorCS)


def test_myatl_binaryoperatorcs_constructor_exists():
    assert callable(myAtl_BinaryOperatorCS.__init__)


def test_myatl_binaryoperatorcs_constructor_args():
    sig = inspect.signature(myAtl_BinaryOperatorCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_binaryoperatorcs_has_name():
    assert hasattr(myAtl_BinaryOperatorCS, "name")
    descriptor = None
    for klass in myAtl_BinaryOperatorCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_infixedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_InfixedExpCS)


def test_myatl_infixedexpcs_constructor_exists():
    assert callable(myAtl_InfixedExpCS.__init__)


def test_myatl_infixedexpcs_constructor_args():
    sig = inspect.signature(myAtl_InfixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigatingargexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigatingArgExpCS)


def test_navigatingargexpcs_constructor_exists():
    assert callable(NavigatingArgExpCS.__init__)


def test_navigatingargexpcs_constructor_args():
    sig = inspect.signature(NavigatingArgExpCS.__init__)
    params = list(sig.parameters.keys())



def test_indexexpcs_is_not_abstract():
    assert not inspect.isabstract(IndexExpCS)


def test_indexexpcs_constructor_exists():
    assert callable(IndexExpCS.__init__)


def test_indexexpcs_constructor_args():
    sig = inspect.signature(IndexExpCS.__init__)
    params = list(sig.parameters.keys())



def test_prefixedexpcs_is_not_abstract():
    assert not inspect.isabstract(PrefixedExpCS)


def test_prefixedexpcs_constructor_exists():
    assert callable(PrefixedExpCS.__init__)


def test_prefixedexpcs_constructor_args():
    sig = inspect.signature(PrefixedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_PrefixExpCS)


def test_myatl_prefixexpcs_constructor_exists():
    assert callable(myAtl_PrefixExpCS.__init__)


def test_myatl_prefixexpcs_constructor_args():
    sig = inspect.signature(myAtl_PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_PrimaryExpCS)


def test_myatl_primaryexpcs_constructor_exists():
    assert callable(myAtl_PrimaryExpCS.__init__)


def test_myatl_primaryexpcs_constructor_args():
    sig = inspect.signature(myAtl_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_letvariablecs_is_not_abstract():
    assert not inspect.isabstract(myAtl_LetVariableCS)


def test_myatl_letvariablecs_constructor_exists():
    assert callable(myAtl_LetVariableCS.__init__)


def test_myatl_letvariablecs_constructor_args():
    sig = inspect.signature(myAtl_LetVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_letvariablecs_has_name():
    assert hasattr(myAtl_LetVariableCS, "name")
    descriptor = None
    for klass in myAtl_LetVariableCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_navigatingsemiargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingSemiArgCS)


def test_myatl_navigatingsemiargcs_constructor_exists():
    assert callable(myAtl_NavigatingSemiArgCS.__init__)


def test_myatl_navigatingsemiargcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingSemiArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl_navigatingsemiargcs_has_prefix():
    assert hasattr(myAtl_NavigatingSemiArgCS, "prefix")
    descriptor = None
    for klass in myAtl_NavigatingSemiArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl_navigatingcommaargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingCommaArgCS)


def test_myatl_navigatingcommaargcs_constructor_exists():
    assert callable(myAtl_NavigatingCommaArgCS.__init__)


def test_myatl_navigatingcommaargcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingCommaArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl_navigatingcommaargcs_has_prefix():
    assert hasattr(myAtl_NavigatingCommaArgCS, "prefix")
    descriptor = None
    for klass in myAtl_NavigatingCommaArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl_navigatingbarargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingBarArgCS)


def test_myatl_navigatingbarargcs_constructor_exists():
    assert callable(myAtl_NavigatingBarArgCS.__init__)


def test_myatl_navigatingbarargcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingBarArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_myatl_navigatingbarargcs_has_prefix():
    assert hasattr(myAtl_NavigatingBarArgCS, "prefix")
    descriptor = None
    for klass in myAtl_NavigatingBarArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_myatl_navigatingargexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingArgExpCS)


def test_myatl_navigatingargexpcs_constructor_exists():
    assert callable(myAtl_NavigatingArgExpCS.__init__)


def test_myatl_navigatingargexpcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingArgExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingArgCS)


def test_myatl_navigatingargcs_constructor_exists():
    assert callable(myAtl_NavigatingArgCS.__init__)


def test_myatl_navigatingargcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TypeLiteralExpCS)


def test_myatl_typeliteralexpcs_constructor_exists():
    assert callable(myAtl_TypeLiteralExpCS.__init__)


def test_myatl_typeliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_typeexpcs_is_not_abstract():
    assert not inspect.isabstract(TypeExpCS)


def test_typeexpcs_constructor_exists():
    assert callable(TypeExpCS.__init__)


def test_typeexpcs_constructor_args():
    sig = inspect.signature(TypeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TypeNameExpCS)


def test_myatl_typenameexpcs_constructor_exists():
    assert callable(myAtl_TypeNameExpCS.__init__)


def test_myatl_typenameexpcs_constructor_args():
    sig = inspect.signature(myAtl_TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "element" in params, "Missing parameter 'element'"

def test_myatl_typenameexpcs_has_namespace():
    assert hasattr(myAtl_TypeNameExpCS, "namespace")
    descriptor = None
    for klass in myAtl_TypeNameExpCS.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_myatl_typenameexpcs_has_element():
    assert hasattr(myAtl_TypeNameExpCS, "element")
    descriptor = None
    for klass in myAtl_TypeNameExpCS.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_myatl_typeliteralcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TypeLiteralCS)


def test_myatl_typeliteralcs_constructor_exists():
    assert callable(myAtl_TypeLiteralCS.__init__)


def test_myatl_typeliteralcs_constructor_args():
    sig = inspect.signature(myAtl_TypeLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_typeliteralcs_has_name():
    assert hasattr(myAtl_TypeLiteralCS, "name")
    descriptor = None
    for klass in myAtl_TypeLiteralCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NullLiteralExpCS)


def test_myatl_nullliteralexpcs_constructor_exists():
    assert callable(myAtl_NullLiteralExpCS.__init__)


def test_myatl_nullliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_StringLiteralExpCS)


def test_myatl_stringliteralexpcs_constructor_exists():
    assert callable(myAtl_StringLiteralExpCS.__init__)


def test_myatl_stringliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_stringliteralexpcs_has_name():
    assert hasattr(myAtl_StringLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl_StringLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_BooleanLiteralExpCS)


def test_myatl_booleanliteralexpcs_constructor_exists():
    assert callable(myAtl_BooleanLiteralExpCS.__init__)


def test_myatl_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_booleanliteralexpcs_has_name():
    assert hasattr(myAtl_BooleanLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl_BooleanLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_InvalidLiteralExpCS)


def test_myatl_invalidliteralexpcs_constructor_exists():
    assert callable(myAtl_InvalidLiteralExpCS.__init__)


def test_myatl_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_UnlimitedNaturalLiteralExpCS)


def test_myatl_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(myAtl_UnlimitedNaturalLiteralExpCS.__init__)


def test_myatl_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NumberLiteralExpCS)


def test_myatl_numberliteralexpcs_constructor_exists():
    assert callable(myAtl_NumberLiteralExpCS.__init__)


def test_myatl_numberliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_numberliteralexpcs_has_name():
    assert hasattr(myAtl_NumberLiteralExpCS, "name")
    descriptor = None
    for klass in myAtl_NumberLiteralExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TupleLiteralPartCS)


def test_myatl_tupleliteralpartcs_constructor_exists():
    assert callable(myAtl_TupleLiteralPartCS.__init__)


def test_myatl_tupleliteralpartcs_constructor_args():
    sig = inspect.signature(myAtl_TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_tupleliteralpartcs_has_name():
    assert hasattr(myAtl_TupleLiteralPartCS, "name")
    descriptor = None
    for klass in myAtl_TupleLiteralPartCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TupleLiteralExpCS)


def test_myatl_tupleliteralexpcs_constructor_exists():
    assert callable(myAtl_TupleLiteralExpCS.__init__)


def test_myatl_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_selfexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_SelfExpCS)


def test_myatl_selfexpcs_constructor_exists():
    assert callable(myAtl_SelfExpCS.__init__)


def test_myatl_selfexpcs_constructor_args():
    sig = inspect.signature(myAtl_SelfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_stringexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_StringExpCs)


def test_myatl_stringexpcs_constructor_exists():
    assert callable(myAtl_StringExpCs.__init__)


def test_myatl_stringexpcs_constructor_args():
    sig = inspect.signature(myAtl_StringExpCs.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_stringexpcs_has_name():
    assert hasattr(myAtl_StringExpCs, "name")
    descriptor = None
    for klass in myAtl_StringExpCs.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_navigatingexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NavigatingExpCS)


def test_myatl_navigatingexpcs_constructor_exists():
    assert callable(myAtl_NavigatingExpCS.__init__)


def test_myatl_navigatingexpcs_constructor_args():
    sig = inspect.signature(myAtl_NavigatingExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_letexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_LetExpCS)


def test_myatl_letexpcs_constructor_exists():
    assert callable(myAtl_LetExpCS.__init__)


def test_myatl_letexpcs_constructor_args():
    sig = inspect.signature(myAtl_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NestedExpCS)


def test_myatl_nestedexpcs_constructor_exists():
    assert callable(myAtl_NestedExpCS.__init__)


def test_myatl_nestedexpcs_constructor_args():
    sig = inspect.signature(myAtl_NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_IfExpCS)


def test_myatl_ifexpcs_constructor_exists():
    assert callable(myAtl_IfExpCS.__init__)


def test_myatl_ifexpcs_constructor_args():
    sig = inspect.signature(myAtl_IfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_PrimitiveLiteralExpCS)


def test_myatl_primitiveliteralexpcs_constructor_exists():
    assert callable(myAtl_PrimitiveLiteralExpCS.__init__)


def test_myatl_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(myAtl_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_tuplePartCS)


def test_myatl_tuplepartcs_constructor_exists():
    assert callable(myAtl_tuplePartCS.__init__)


def test_myatl_tuplepartcs_constructor_args():
    sig = inspect.signature(myAtl_tuplePartCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_tuplepartcs_has_name():
    assert hasattr(myAtl_tuplePartCS, "name")
    descriptor = None
    for klass in myAtl_tuplePartCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeliteralcs_is_not_abstract():
    assert not inspect.isabstract(TypeLiteralCS)


def test_typeliteralcs_constructor_exists():
    assert callable(TypeLiteralCS.__init__)


def test_typeliteralcs_constructor_args():
    sig = inspect.signature(TypeLiteralCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_primitivetypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl_PrimitiveTypeCS)


def test_myatl_primitivetypecs_constructor_exists():
    assert callable(myAtl_PrimitiveTypeCS.__init__)


def test_myatl_primitivetypecs_constructor_args():
    sig = inspect.signature(myAtl_PrimitiveTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TupleTypeCS)


def test_myatl_tupletypecs_constructor_exists():
    assert callable(myAtl_TupleTypeCS.__init__)


def test_myatl_tupletypecs_constructor_args():
    sig = inspect.signature(myAtl_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "backtrack" in params, "Missing parameter 'backtrack'"

def test_myatl_tupletypecs_has_backtrack():
    assert hasattr(myAtl_TupleTypeCS, "backtrack")
    descriptor = None
    for klass in myAtl_TupleTypeCS.__mro__:
        if "backtrack" in klass.__dict__:
            descriptor = klass.__dict__["backtrack"]
            break
    assert isinstance(descriptor, property)



def test_myatl_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(myAtl_CollectionTypeCS)


def test_myatl_collectiontypecs_constructor_exists():
    assert callable(myAtl_CollectionTypeCS.__init__)


def test_myatl_collectiontypecs_constructor_args():
    sig = inspect.signature(myAtl_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_typeexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_TypeExpCS)


def test_myatl_typeexpcs_constructor_exists():
    assert callable(myAtl_TypeExpCS.__init__)


def test_myatl_typeexpcs_constructor_args():
    sig = inspect.signature(myAtl_TypeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_bindingstat_is_not_abstract():
    assert not inspect.isabstract(myAtl_BindingStat)


def test_myatl_bindingstat_constructor_exists():
    assert callable(myAtl_BindingStat.__init__)


def test_myatl_bindingstat_constructor_args():
    sig = inspect.signature(myAtl_BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_myatl_bindingstat_has_propertyName():
    assert hasattr(myAtl_BindingStat, "propertyName")
    descriptor = None
    for klass in myAtl_BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_statement_is_not_abstract():
    assert not inspect.isabstract(myAtl_Statement)


def test_myatl_statement_constructor_exists():
    assert callable(myAtl_Statement.__init__)


def test_myatl_statement_constructor_args():
    sig = inspect.signature(myAtl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_binding_is_not_abstract():
    assert not inspect.isabstract(myAtl_Binding)


def test_myatl_binding_constructor_exists():
    assert callable(myAtl_Binding.__init__)


def test_myatl_binding_constructor_args():
    sig = inspect.signature(myAtl_Binding.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_myatl_binding_has_propertyName():
    assert hasattr(myAtl_Binding, "propertyName")
    descriptor = None
    for klass in myAtl_Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl_ForEachOutPatternElement)


def test_myatl_foreachoutpatternelement_constructor_exists():
    assert callable(myAtl_ForEachOutPatternElement.__init__)


def test_myatl_foreachoutpatternelement_constructor_args():
    sig = inspect.signature(myAtl_ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl_SimpleOutPatternElement)


def test_myatl_simpleoutpatternelement_constructor_exists():
    assert callable(myAtl_SimpleOutPatternElement.__init__)


def test_myatl_simpleoutpatternelement_constructor_args():
    sig = inspect.signature(myAtl_SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl_simpleoutpatternelement_has_varName():
    assert hasattr(myAtl_SimpleOutPatternElement, "varName")
    descriptor = None
    for klass in myAtl_SimpleOutPatternElement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl_OutPatternElement)


def test_myatl_outpatternelement_constructor_exists():
    assert callable(myAtl_OutPatternElement.__init__)


def test_myatl_outpatternelement_constructor_args():
    sig = inspect.signature(myAtl_OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_inpatternelement_is_not_abstract():
    assert not inspect.isabstract(myAtl_InPatternElement)


def test_myatl_inpatternelement_constructor_exists():
    assert callable(myAtl_InPatternElement.__init__)


def test_myatl_inpatternelement_constructor_args():
    sig = inspect.signature(myAtl_InPatternElement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl_inpatternelement_has_varName():
    assert hasattr(myAtl_InPatternElement, "varName")
    descriptor = None
    for klass in myAtl_InPatternElement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_atltype_is_not_abstract():
    assert not inspect.isabstract(myAtl_ATLType)


def test_myatl_atltype_constructor_exists():
    assert callable(myAtl_ATLType.__init__)


def test_myatl_atltype_constructor_args():
    sig = inspect.signature(myAtl_ATLType.__init__)
    params = list(sig.parameters.keys())
    assert "modelName" in params, "Missing parameter 'modelName'"

def test_myatl_atltype_has_modelName():
    assert hasattr(myAtl_ATLType, "modelName")
    descriptor = None
    for klass in myAtl_ATLType.__mro__:
        if "modelName" in klass.__dict__:
            descriptor = klass.__dict__["modelName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_atldefcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_ATLDefCS)


def test_myatl_atldefcs_constructor_exists():
    assert callable(myAtl_ATLDefCS.__init__)


def test_myatl_atldefcs_constructor_args():
    sig = inspect.signature(myAtl_ATLDefCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl_atldefcs_has_varName():
    assert hasattr(myAtl_ATLDefCS, "varName")
    descriptor = None
    for klass in myAtl_ATLDefCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_expcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_ExpCS)


def test_myatl_expcs_constructor_exists():
    assert callable(myAtl_ExpCS.__init__)


def test_myatl_expcs_constructor_args():
    sig = inspect.signature(myAtl_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_myatl_atlparametercs_is_not_abstract():
    assert not inspect.isabstract(myAtl_ATLParameterCS)


def test_myatl_atlparametercs_constructor_exists():
    assert callable(myAtl_ATLParameterCS.__init__)


def test_myatl_atlparametercs_constructor_args():
    sig = inspect.signature(myAtl_ATLParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl_atlparametercs_has_varName():
    assert hasattr(myAtl_ATLParameterCS, "varName")
    descriptor = None
    for klass in myAtl_ATLParameterCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_actionblock_is_not_abstract():
    assert not inspect.isabstract(myAtl_ActionBlock)


def test_myatl_actionblock_constructor_exists():
    assert callable(myAtl_ActionBlock.__init__)


def test_myatl_actionblock_constructor_args():
    sig = inspect.signature(myAtl_ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_myatl_outpattern_is_not_abstract():
    assert not inspect.isabstract(myAtl_OutPattern)


def test_myatl_outpattern_constructor_exists():
    assert callable(myAtl_OutPattern.__init__)


def test_myatl_outpattern_constructor_args():
    sig = inspect.signature(myAtl_OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_myatl_rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(myAtl_RuleVariableDeclaration)


def test_myatl_rulevariabledeclaration_constructor_exists():
    assert callable(myAtl_RuleVariableDeclaration.__init__)


def test_myatl_rulevariabledeclaration_constructor_args():
    sig = inspect.signature(myAtl_RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_myatl_rulevariabledeclaration_has_varName():
    assert hasattr(myAtl_RuleVariableDeclaration, "varName")
    descriptor = None
    for klass in myAtl_RuleVariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_myatl_inpattern_is_not_abstract():
    assert not inspect.isabstract(myAtl_InPattern)


def test_myatl_inpattern_constructor_exists():
    assert callable(myAtl_InPattern.__init__)


def test_myatl_inpattern_constructor_args():
    sig = inspect.signature(myAtl_InPattern.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_myatl_queryrule_is_not_abstract():
    assert not inspect.isabstract(myAtl_QueryRule)


def test_myatl_queryrule_constructor_exists():
    assert callable(myAtl_QueryRule.__init__)


def test_myatl_queryrule_constructor_args():
    sig = inspect.signature(myAtl_QueryRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl_helper_is_not_abstract():
    assert not inspect.isabstract(myAtl_Helper)


def test_myatl_helper_constructor_exists():
    assert callable(myAtl_Helper.__init__)


def test_myatl_helper_constructor_args():
    sig = inspect.signature(myAtl_Helper.__init__)
    params = list(sig.parameters.keys())



def test_myatl_calledrule_is_not_abstract():
    assert not inspect.isabstract(myAtl_CalledRule)


def test_myatl_calledrule_constructor_exists():
    assert callable(myAtl_CalledRule.__init__)


def test_myatl_calledrule_constructor_args():
    sig = inspect.signature(myAtl_CalledRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl_matchedrule_is_not_abstract():
    assert not inspect.isabstract(myAtl_MatchedRule)


def test_myatl_matchedrule_constructor_exists():
    assert callable(myAtl_MatchedRule.__init__)


def test_myatl_matchedrule_constructor_args():
    sig = inspect.signature(myAtl_MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_myatl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(myAtl_ModuleElement)


def test_myatl_moduleelement_constructor_exists():
    assert callable(myAtl_ModuleElement.__init__)


def test_myatl_moduleelement_constructor_args():
    sig = inspect.signature(myAtl_ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_moduleelement_has_name():
    assert hasattr(myAtl_ModuleElement, "name")
    descriptor = None
    for klass in myAtl_ModuleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_myatl_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(myAtl_NameExpCS)


def test_myatl_nameexpcs_constructor_exists():
    assert callable(myAtl_NameExpCS.__init__)


def test_myatl_nameexpcs_constructor_args():
    sig = inspect.signature(myAtl_NameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "element" in params, "Missing parameter 'element'"

def test_myatl_nameexpcs_has_namespace():
    assert hasattr(myAtl_NameExpCS, "namespace")
    descriptor = None
    for klass in myAtl_NameExpCS.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_myatl_nameexpcs_has_element():
    assert hasattr(myAtl_NameExpCS, "element")
    descriptor = None
    for klass in myAtl_NameExpCS.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_myatl_module_is_not_abstract():
    assert not inspect.isabstract(myAtl_Module)


def test_myatl_module_constructor_exists():
    assert callable(myAtl_Module.__init__)


def test_myatl_module_constructor_args():
    sig = inspect.signature(myAtl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_myatl_module_has_name():
    assert hasattr(myAtl_Module, "name")
    descriptor = None
    for klass in myAtl_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
myAtl_EObject_strategy = st.builds(
    myAtl_EObject,
)
NavigatingExpCS_strategy = st.builds(
    NavigatingExpCS,
)
myAtl_NavigatingExpCS_Base_strategy = st.builds(
    myAtl_NavigatingExpCS_Base,
)
NavigatingExpCS_Base_strategy = st.builds(
    NavigatingExpCS_Base,
)
myAtl_IndexExpCS_strategy = st.builds(
    myAtl_IndexExpCS,
)
myAtl_UnaryOperatorCS_strategy = st.builds(
    myAtl_UnaryOperatorCS,
    name=
        safe_text
)
InfixedExpCS_strategy = st.builds(
    InfixedExpCS,
)
myAtl_InfixExpCS_strategy = st.builds(
    myAtl_InfixExpCS,
)
myAtl_PrefixedExpCS_strategy = st.builds(
    myAtl_PrefixedExpCS,
)
BinaryOperatorCS_strategy = st.builds(
    BinaryOperatorCS,
)
myAtl_NavigationOperatorCS_strategy = st.builds(
    myAtl_NavigationOperatorCS,
)
myAtl_InfixOperatorCS_strategy = st.builds(
    myAtl_InfixOperatorCS,
)
myAtl_BinaryOperatorCS_strategy = st.builds(
    myAtl_BinaryOperatorCS,
    name=
        safe_text
)
ExpCS_strategy = st.builds(
    ExpCS,
)
myAtl_InfixedExpCS_strategy = st.builds(
    myAtl_InfixedExpCS,
)
NavigatingArgExpCS_strategy = st.builds(
    NavigatingArgExpCS,
)
IndexExpCS_strategy = st.builds(
    IndexExpCS,
)
PrefixedExpCS_strategy = st.builds(
    PrefixedExpCS,
)
myAtl_PrefixExpCS_strategy = st.builds(
    myAtl_PrefixExpCS,
)
myAtl_PrimaryExpCS_strategy = st.builds(
    myAtl_PrimaryExpCS,
)
myAtl_LetVariableCS_strategy = st.builds(
    myAtl_LetVariableCS,
    name=
        safe_text
)
myAtl_NavigatingSemiArgCS_strategy = st.builds(
    myAtl_NavigatingSemiArgCS,
    prefix=
        safe_text
)
myAtl_NavigatingCommaArgCS_strategy = st.builds(
    myAtl_NavigatingCommaArgCS,
    prefix=
        safe_text
)
myAtl_NavigatingBarArgCS_strategy = st.builds(
    myAtl_NavigatingBarArgCS,
    prefix=
        safe_text
)
myAtl_NavigatingArgExpCS_strategy = st.builds(
    myAtl_NavigatingArgExpCS,
)
myAtl_NavigatingArgCS_strategy = st.builds(
    myAtl_NavigatingArgCS,
)
myAtl_TypeLiteralExpCS_strategy = st.builds(
    myAtl_TypeLiteralExpCS,
)
TypeExpCS_strategy = st.builds(
    TypeExpCS,
)
myAtl_TypeNameExpCS_strategy = st.builds(
    myAtl_TypeNameExpCS,
    namespace=
        safe_text,
    element=
        safe_text
)
myAtl_TypeLiteralCS_strategy = st.builds(
    myAtl_TypeLiteralCS,
    name=
        safe_text
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
myAtl_NullLiteralExpCS_strategy = st.builds(
    myAtl_NullLiteralExpCS,
)
myAtl_StringLiteralExpCS_strategy = st.builds(
    myAtl_StringLiteralExpCS,
    name=
        safe_text
)
myAtl_BooleanLiteralExpCS_strategy = st.builds(
    myAtl_BooleanLiteralExpCS,
    name=
        safe_text
)
myAtl_InvalidLiteralExpCS_strategy = st.builds(
    myAtl_InvalidLiteralExpCS,
)
myAtl_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    myAtl_UnlimitedNaturalLiteralExpCS,
)
myAtl_NumberLiteralExpCS_strategy = st.builds(
    myAtl_NumberLiteralExpCS,
    name=
        safe_text
)
myAtl_TupleLiteralPartCS_strategy = st.builds(
    myAtl_TupleLiteralPartCS,
    name=
        safe_text
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
myAtl_TupleLiteralExpCS_strategy = st.builds(
    myAtl_TupleLiteralExpCS,
)
myAtl_SelfExpCS_strategy = st.builds(
    myAtl_SelfExpCS,
)
myAtl_StringExpCs_strategy = st.builds(
    myAtl_StringExpCs,
    name=
        safe_text
)
myAtl_NavigatingExpCS_strategy = st.builds(
    myAtl_NavigatingExpCS,
)
myAtl_LetExpCS_strategy = st.builds(
    myAtl_LetExpCS,
)
myAtl_NestedExpCS_strategy = st.builds(
    myAtl_NestedExpCS,
)
myAtl_IfExpCS_strategy = st.builds(
    myAtl_IfExpCS,
)
myAtl_PrimitiveLiteralExpCS_strategy = st.builds(
    myAtl_PrimitiveLiteralExpCS,
)
myAtl_tuplePartCS_strategy = st.builds(
    myAtl_tuplePartCS,
    name=
        safe_text
)
TypeLiteralCS_strategy = st.builds(
    TypeLiteralCS,
)
myAtl_PrimitiveTypeCS_strategy = st.builds(
    myAtl_PrimitiveTypeCS,
)
myAtl_TupleTypeCS_strategy = st.builds(
    myAtl_TupleTypeCS,
    backtrack=
        safe_text
)
myAtl_CollectionTypeCS_strategy = st.builds(
    myAtl_CollectionTypeCS,
)
myAtl_TypeExpCS_strategy = st.builds(
    myAtl_TypeExpCS,
)
Statement_strategy = st.builds(
    Statement,
)
myAtl_BindingStat_strategy = st.builds(
    myAtl_BindingStat,
    propertyName=
        safe_text
)
myAtl_Statement_strategy = st.builds(
    myAtl_Statement,
)
myAtl_Binding_strategy = st.builds(
    myAtl_Binding,
    propertyName=
        safe_text
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
myAtl_ForEachOutPatternElement_strategy = st.builds(
    myAtl_ForEachOutPatternElement,
)
myAtl_SimpleOutPatternElement_strategy = st.builds(
    myAtl_SimpleOutPatternElement,
    varName=
        safe_text
)
myAtl_OutPatternElement_strategy = st.builds(
    myAtl_OutPatternElement,
)
myAtl_InPatternElement_strategy = st.builds(
    myAtl_InPatternElement,
    varName=
        safe_text
)
myAtl_ATLType_strategy = st.builds(
    myAtl_ATLType,
    modelName=
        safe_text
)
myAtl_ATLDefCS_strategy = st.builds(
    myAtl_ATLDefCS,
    varName=
        safe_text
)
myAtl_ExpCS_strategy = st.builds(
    myAtl_ExpCS,
)
myAtl_ATLParameterCS_strategy = st.builds(
    myAtl_ATLParameterCS,
    varName=
        safe_text
)
myAtl_ActionBlock_strategy = st.builds(
    myAtl_ActionBlock,
)
myAtl_OutPattern_strategy = st.builds(
    myAtl_OutPattern,
)
myAtl_RuleVariableDeclaration_strategy = st.builds(
    myAtl_RuleVariableDeclaration,
    varName=
        safe_text
)
myAtl_InPattern_strategy = st.builds(
    myAtl_InPattern,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
myAtl_QueryRule_strategy = st.builds(
    myAtl_QueryRule,
)
myAtl_Helper_strategy = st.builds(
    myAtl_Helper,
)
myAtl_CalledRule_strategy = st.builds(
    myAtl_CalledRule,
)
myAtl_MatchedRule_strategy = st.builds(
    myAtl_MatchedRule,
)
myAtl_ModuleElement_strategy = st.builds(
    myAtl_ModuleElement,
    name=
        safe_text
)
myAtl_NameExpCS_strategy = st.builds(
    myAtl_NameExpCS,
    namespace=
        safe_text,
    element=
        safe_text
)
myAtl_Module_strategy = st.builds(
    myAtl_Module,
    name=
        safe_text
)

@given(instance=myAtl_EObject_strategy)
@settings(max_examples=50)
def test_myatl_eobject_instantiation(instance):
    assert isinstance(instance, myAtl_EObject)

@given(instance=NavigatingExpCS_strategy)
@settings(max_examples=50)
def test_navigatingexpcs_instantiation(instance):
    assert isinstance(instance, NavigatingExpCS)

@given(instance=myAtl_NavigatingExpCS_Base_strategy)
@settings(max_examples=50)
def test_myatl_navigatingexpcs_base_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingExpCS_Base)

@given(instance=NavigatingExpCS_Base_strategy)
@settings(max_examples=50)
def test_navigatingexpcs_base_instantiation(instance):
    assert isinstance(instance, NavigatingExpCS_Base)

@given(instance=myAtl_IndexExpCS_strategy)
@settings(max_examples=50)
def test_myatl_indexexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_IndexExpCS)

@given(instance=myAtl_UnaryOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl_unaryoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl_UnaryOperatorCS)



@given(instance=myAtl_UnaryOperatorCS_strategy)
def test_myatl_unaryoperatorcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InfixedExpCS_strategy)
@settings(max_examples=50)
def test_infixedexpcs_instantiation(instance):
    assert isinstance(instance, InfixedExpCS)

@given(instance=myAtl_InfixExpCS_strategy)
@settings(max_examples=50)
def test_myatl_infixexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_InfixExpCS)

@given(instance=myAtl_PrefixedExpCS_strategy)
@settings(max_examples=50)
def test_myatl_prefixedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_PrefixedExpCS)

@given(instance=BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, BinaryOperatorCS)

@given(instance=myAtl_NavigationOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl_navigationoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigationOperatorCS)

@given(instance=myAtl_InfixOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl_infixoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl_InfixOperatorCS)

@given(instance=myAtl_BinaryOperatorCS_strategy)
@settings(max_examples=50)
def test_myatl_binaryoperatorcs_instantiation(instance):
    assert isinstance(instance, myAtl_BinaryOperatorCS)



@given(instance=myAtl_BinaryOperatorCS_strategy)
def test_myatl_binaryoperatorcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=myAtl_InfixedExpCS_strategy)
@settings(max_examples=50)
def test_myatl_infixedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_InfixedExpCS)

@given(instance=NavigatingArgExpCS_strategy)
@settings(max_examples=50)
def test_navigatingargexpcs_instantiation(instance):
    assert isinstance(instance, NavigatingArgExpCS)

@given(instance=IndexExpCS_strategy)
@settings(max_examples=50)
def test_indexexpcs_instantiation(instance):
    assert isinstance(instance, IndexExpCS)

@given(instance=PrefixedExpCS_strategy)
@settings(max_examples=50)
def test_prefixedexpcs_instantiation(instance):
    assert isinstance(instance, PrefixedExpCS)

@given(instance=myAtl_PrefixExpCS_strategy)
@settings(max_examples=50)
def test_myatl_prefixexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_PrefixExpCS)

@given(instance=myAtl_PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_myatl_primaryexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_PrimaryExpCS)

@given(instance=myAtl_LetVariableCS_strategy)
@settings(max_examples=50)
def test_myatl_letvariablecs_instantiation(instance):
    assert isinstance(instance, myAtl_LetVariableCS)



@given(instance=myAtl_LetVariableCS_strategy)
def test_myatl_letvariablecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_NavigatingSemiArgCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingsemiargcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingSemiArgCS)



@given(instance=myAtl_NavigatingSemiArgCS_strategy)
def test_myatl_navigatingsemiargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl_NavigatingCommaArgCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingcommaargcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingCommaArgCS)



@given(instance=myAtl_NavigatingCommaArgCS_strategy)
def test_myatl_navigatingcommaargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl_NavigatingBarArgCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingbarargcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingBarArgCS)



@given(instance=myAtl_NavigatingBarArgCS_strategy)
def test_myatl_navigatingbarargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=myAtl_NavigatingArgExpCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingargexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingArgExpCS)

@given(instance=myAtl_NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingargcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingArgCS)

@given(instance=myAtl_TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_TypeLiteralExpCS)

@given(instance=TypeExpCS_strategy)
@settings(max_examples=50)
def test_typeexpcs_instantiation(instance):
    assert isinstance(instance, TypeExpCS)

@given(instance=myAtl_TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_myatl_typenameexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_TypeNameExpCS)



@given(instance=myAtl_TypeNameExpCS_strategy)
def test_myatl_typenameexpcs_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=myAtl_TypeNameExpCS_strategy)
def test_myatl_typenameexpcs_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=myAtl_TypeLiteralCS_strategy)
@settings(max_examples=50)
def test_myatl_typeliteralcs_instantiation(instance):
    assert isinstance(instance, myAtl_TypeLiteralCS)



@given(instance=myAtl_TypeLiteralCS_strategy)
def test_myatl_typeliteralcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=myAtl_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NullLiteralExpCS)

@given(instance=myAtl_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_StringLiteralExpCS)



@given(instance=myAtl_StringLiteralExpCS_strategy)
def test_myatl_stringliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_BooleanLiteralExpCS)



@given(instance=myAtl_BooleanLiteralExpCS_strategy)
def test_myatl_booleanliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_InvalidLiteralExpCS)

@given(instance=myAtl_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_UnlimitedNaturalLiteralExpCS)

@given(instance=myAtl_NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NumberLiteralExpCS)



@given(instance=myAtl_NumberLiteralExpCS_strategy)
def test_myatl_numberliteralexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_myatl_tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, myAtl_TupleLiteralPartCS)



@given(instance=myAtl_TupleLiteralPartCS_strategy)
def test_myatl_tupleliteralpartcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=myAtl_TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_TupleLiteralExpCS)

@given(instance=myAtl_SelfExpCS_strategy)
@settings(max_examples=50)
def test_myatl_selfexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_SelfExpCS)

@given(instance=myAtl_StringExpCs_strategy)
@settings(max_examples=50)
def test_myatl_stringexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_StringExpCs)



@given(instance=myAtl_StringExpCs_strategy)
def test_myatl_stringexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_NavigatingExpCS_strategy)
@settings(max_examples=50)
def test_myatl_navigatingexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NavigatingExpCS)

@given(instance=myAtl_LetExpCS_strategy)
@settings(max_examples=50)
def test_myatl_letexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_LetExpCS)

@given(instance=myAtl_NestedExpCS_strategy)
@settings(max_examples=50)
def test_myatl_nestedexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NestedExpCS)

@given(instance=myAtl_IfExpCS_strategy)
@settings(max_examples=50)
def test_myatl_ifexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_IfExpCS)

@given(instance=myAtl_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_myatl_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_PrimitiveLiteralExpCS)

@given(instance=myAtl_tuplePartCS_strategy)
@settings(max_examples=50)
def test_myatl_tuplepartcs_instantiation(instance):
    assert isinstance(instance, myAtl_tuplePartCS)



@given(instance=myAtl_tuplePartCS_strategy)
def test_myatl_tuplepartcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeLiteralCS_strategy)
@settings(max_examples=50)
def test_typeliteralcs_instantiation(instance):
    assert isinstance(instance, TypeLiteralCS)

@given(instance=myAtl_PrimitiveTypeCS_strategy)
@settings(max_examples=50)
def test_myatl_primitivetypecs_instantiation(instance):
    assert isinstance(instance, myAtl_PrimitiveTypeCS)

@given(instance=myAtl_TupleTypeCS_strategy)
@settings(max_examples=50)
def test_myatl_tupletypecs_instantiation(instance):
    assert isinstance(instance, myAtl_TupleTypeCS)



@given(instance=myAtl_TupleTypeCS_strategy)
def test_myatl_tupletypecs_backtrack_setter(instance):
    original = instance.backtrack
    instance.backtrack = original
    assert instance.backtrack == original

@given(instance=myAtl_CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_myatl_collectiontypecs_instantiation(instance):
    assert isinstance(instance, myAtl_CollectionTypeCS)

@given(instance=myAtl_TypeExpCS_strategy)
@settings(max_examples=50)
def test_myatl_typeexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_TypeExpCS)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=myAtl_BindingStat_strategy)
@settings(max_examples=50)
def test_myatl_bindingstat_instantiation(instance):
    assert isinstance(instance, myAtl_BindingStat)



@given(instance=myAtl_BindingStat_strategy)
def test_myatl_bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=myAtl_Statement_strategy)
@settings(max_examples=50)
def test_myatl_statement_instantiation(instance):
    assert isinstance(instance, myAtl_Statement)

@given(instance=myAtl_Binding_strategy)
@settings(max_examples=50)
def test_myatl_binding_instantiation(instance):
    assert isinstance(instance, myAtl_Binding)



@given(instance=myAtl_Binding_strategy)
def test_myatl_binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=myAtl_ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl_foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl_ForEachOutPatternElement)

@given(instance=myAtl_SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl_simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl_SimpleOutPatternElement)



@given(instance=myAtl_SimpleOutPatternElement_strategy)
def test_myatl_simpleoutpatternelement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl_OutPatternElement_strategy)
@settings(max_examples=50)
def test_myatl_outpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl_OutPatternElement)

@given(instance=myAtl_InPatternElement_strategy)
@settings(max_examples=50)
def test_myatl_inpatternelement_instantiation(instance):
    assert isinstance(instance, myAtl_InPatternElement)



@given(instance=myAtl_InPatternElement_strategy)
def test_myatl_inpatternelement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl_ATLType_strategy)
@settings(max_examples=50)
def test_myatl_atltype_instantiation(instance):
    assert isinstance(instance, myAtl_ATLType)



@given(instance=myAtl_ATLType_strategy)
def test_myatl_atltype_modelName_setter(instance):
    original = instance.modelName
    instance.modelName = original
    assert instance.modelName == original

@given(instance=myAtl_ATLDefCS_strategy)
@settings(max_examples=50)
def test_myatl_atldefcs_instantiation(instance):
    assert isinstance(instance, myAtl_ATLDefCS)



@given(instance=myAtl_ATLDefCS_strategy)
def test_myatl_atldefcs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl_ExpCS_strategy)
@settings(max_examples=50)
def test_myatl_expcs_instantiation(instance):
    assert isinstance(instance, myAtl_ExpCS)

@given(instance=myAtl_ATLParameterCS_strategy)
@settings(max_examples=50)
def test_myatl_atlparametercs_instantiation(instance):
    assert isinstance(instance, myAtl_ATLParameterCS)



@given(instance=myAtl_ATLParameterCS_strategy)
def test_myatl_atlparametercs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl_ActionBlock_strategy)
@settings(max_examples=50)
def test_myatl_actionblock_instantiation(instance):
    assert isinstance(instance, myAtl_ActionBlock)

@given(instance=myAtl_OutPattern_strategy)
@settings(max_examples=50)
def test_myatl_outpattern_instantiation(instance):
    assert isinstance(instance, myAtl_OutPattern)

@given(instance=myAtl_RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_myatl_rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, myAtl_RuleVariableDeclaration)



@given(instance=myAtl_RuleVariableDeclaration_strategy)
def test_myatl_rulevariabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=myAtl_InPattern_strategy)
@settings(max_examples=50)
def test_myatl_inpattern_instantiation(instance):
    assert isinstance(instance, myAtl_InPattern)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=myAtl_QueryRule_strategy)
@settings(max_examples=50)
def test_myatl_queryrule_instantiation(instance):
    assert isinstance(instance, myAtl_QueryRule)

@given(instance=myAtl_Helper_strategy)
@settings(max_examples=50)
def test_myatl_helper_instantiation(instance):
    assert isinstance(instance, myAtl_Helper)

@given(instance=myAtl_CalledRule_strategy)
@settings(max_examples=50)
def test_myatl_calledrule_instantiation(instance):
    assert isinstance(instance, myAtl_CalledRule)

@given(instance=myAtl_MatchedRule_strategy)
@settings(max_examples=50)
def test_myatl_matchedrule_instantiation(instance):
    assert isinstance(instance, myAtl_MatchedRule)

@given(instance=myAtl_ModuleElement_strategy)
@settings(max_examples=50)
def test_myatl_moduleelement_instantiation(instance):
    assert isinstance(instance, myAtl_ModuleElement)



@given(instance=myAtl_ModuleElement_strategy)
def test_myatl_moduleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myAtl_NameExpCS_strategy)
@settings(max_examples=50)
def test_myatl_nameexpcs_instantiation(instance):
    assert isinstance(instance, myAtl_NameExpCS)



@given(instance=myAtl_NameExpCS_strategy)
def test_myatl_nameexpcs_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=myAtl_NameExpCS_strategy)
def test_myatl_nameexpcs_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=myAtl_Module_strategy)
@settings(max_examples=50)
def test_myatl_module_instantiation(instance):
    assert isinstance(instance, myAtl_Module)



@given(instance=myAtl_Module_strategy)
def test_myatl_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

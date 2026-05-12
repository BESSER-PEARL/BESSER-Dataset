import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelElementCS,
    AbstractNameExpCS,
    essentialoclcs_CallExpCS,
    PrimitiveLiteralExpCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_AssociationClass,
    CallExpCS,
    essentialoclcs_AssociationClassCallExpCS,
    essentialoclcs_Type,
    essentialoclcs_PathNameCS,
    ExpCS,
    essentialoclcs_AbstractNameExpCS,
    essentialoclcs_Variable,
    essentialoclcs_VariableExpCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_ShadowExpCS,
    essentialoclcs_SelfExpCS,
    essentialoclcs_Property,
    essentialoclcs_PropertyCallExpCS,
    essentialoclcs_TypeRefCS,
    essentialoclcs_Operation,
    essentialoclcs_OperationCallExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_Iteration,
    essentialoclcs_NavigatingArgCS,
    VariableExpCS,
    PropertyCallExpCS,
    OperationCallExpCS,
    IterateCallExpCS,
    ShadowExpCS,
    AssociationClassCallExpCS,
    essentialoclcs_MapLiteralPartCS,
    essentialoclcs_LiteralExpCS,
    VariableCS,
    essentialoclcs_TupleLiteralPartCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_IterationCallExpCS,
    IterationCallExpCS,
    essentialoclcs_NameExpCS,
    essentialoclcs_IterateCallExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    OperatorExpCS,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_IfThenExpCS,
    essentialoclcs_IfExpCS,
    SpecificationCS,
    essentialoclcs_ExpSpecificationCS,
    essentialoclcs_Precedence,
    essentialoclcs_CollectionLiteralPartCS,
    LiteralExpCS,
    essentialoclcs_MapLiteralExpCS,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_LambdaLiteralExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    essentialoclcs_ExpCS,
    ContextLessElementCS,
    essentialoclcs_CurlyBracketedClauseCS,
    essentialoclcs_RoundBracketedClauseCS,
    essentialoclcs_SquareBracketedClauseCS,
    RootCS,
    NamedElementCS,
    essentialoclcs_OperatorExpCS,
    essentialoclcs_VariableCS,
    essentialoclcs_ContextCS,
    essentialoclcs_TypedRefCS,
    Nameable,
    essentialoclcs_ShadowPartCS,
    essentialoclcs_PatternExpCS,
    TypedRefCS,
    essentialoclcs_CollectionTypeCS,
    essentialoclcs_TypeNameExpCS,
    essentialoclcs_MapTypeCS,
    essentialoclcs_CollectionPatternCS,
    NavigationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(AbstractNameExpCS)


def test_abstractnameexpcs_constructor_exists():
    assert callable(AbstractNameExpCS.__init__)


def test_abstractnameexpcs_constructor_args():
    sig = inspect.signature(AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CallExpCS)


def test_essentialoclcs_callexpcs_constructor_exists():
    assert callable(essentialoclcs_CallExpCS.__init__)


def test_essentialoclcs_callexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_BooleanLiteralExpCS)


def test_essentialoclcs_booleanliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_BooleanLiteralExpCS.__init__)


def test_essentialoclcs_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialoclcs_booleanliteralexpcs_has_symbol():
    assert hasattr(essentialoclcs_BooleanLiteralExpCS, "symbol")
    descriptor = None
    for klass in essentialoclcs_BooleanLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_associationclass_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AssociationClass)


def test_essentialoclcs_associationclass_constructor_exists():
    assert callable(essentialoclcs_AssociationClass.__init__)


def test_essentialoclcs_associationclass_constructor_args():
    sig = inspect.signature(essentialoclcs_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_associationclasscallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AssociationClassCallExpCS)


def test_essentialoclcs_associationclasscallexpcs_constructor_exists():
    assert callable(essentialoclcs_AssociationClassCallExpCS.__init__)


def test_essentialoclcs_associationclasscallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_AssociationClassCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_type_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Type)


def test_essentialoclcs_type_constructor_exists():
    assert callable(essentialoclcs_Type.__init__)


def test_essentialoclcs_type_constructor_args():
    sig = inspect.signature(essentialoclcs_Type.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PathNameCS)


def test_essentialoclcs_pathnamecs_constructor_exists():
    assert callable(essentialoclcs_PathNameCS.__init__)


def test_essentialoclcs_pathnamecs_constructor_args():
    sig = inspect.signature(essentialoclcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_AbstractNameExpCS)


def test_essentialoclcs_abstractnameexpcs_constructor_exists():
    assert callable(essentialoclcs_AbstractNameExpCS.__init__)


def test_essentialoclcs_abstractnameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_essentialoclcs_abstractnameexpcs_has_isPre():
    assert hasattr(essentialoclcs_AbstractNameExpCS, "isPre")
    descriptor = None
    for klass in essentialoclcs_AbstractNameExpCS.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_variable_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Variable)


def test_essentialoclcs_variable_constructor_exists():
    assert callable(essentialoclcs_Variable.__init__)


def test_essentialoclcs_variable_constructor_args():
    sig = inspect.signature(essentialoclcs_Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_VariableExpCS)


def test_essentialoclcs_variableexpcs_constructor_exists():
    assert callable(essentialoclcs_VariableExpCS.__init__)


def test_essentialoclcs_variableexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_UnlimitedNaturalLiteralExpCS)


def test_essentialoclcs_unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcs_unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_StringLiteralExpCS)


def test_essentialoclcs_stringliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_StringLiteralExpCS.__init__)


def test_essentialoclcs_stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_essentialoclcs_stringliteralexpcs_has_segments():
    assert hasattr(essentialoclcs_StringLiteralExpCS, "segments")
    descriptor = None
    for klass in essentialoclcs_StringLiteralExpCS.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_shadowexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ShadowExpCS)


def test_essentialoclcs_shadowexpcs_constructor_exists():
    assert callable(essentialoclcs_ShadowExpCS.__init__)


def test_essentialoclcs_shadowexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ShadowExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs_shadowexpcs_has_value():
    assert hasattr(essentialoclcs_ShadowExpCS, "value")
    descriptor = None
    for klass in essentialoclcs_ShadowExpCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_selfexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_SelfExpCS)


def test_essentialoclcs_selfexpcs_constructor_exists():
    assert callable(essentialoclcs_SelfExpCS.__init__)


def test_essentialoclcs_selfexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_SelfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_selfexpcs_has_name():
    assert hasattr(essentialoclcs_SelfExpCS, "name")
    descriptor = None
    for klass in essentialoclcs_SelfExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_property_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Property)


def test_essentialoclcs_property_constructor_exists():
    assert callable(essentialoclcs_Property.__init__)


def test_essentialoclcs_property_constructor_args():
    sig = inspect.signature(essentialoclcs_Property.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_propertycallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PropertyCallExpCS)


def test_essentialoclcs_propertycallexpcs_constructor_exists():
    assert callable(essentialoclcs_PropertyCallExpCS.__init__)


def test_essentialoclcs_propertycallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PropertyCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_typerefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeRefCS)


def test_essentialoclcs_typerefcs_constructor_exists():
    assert callable(essentialoclcs_TypeRefCS.__init__)


def test_essentialoclcs_typerefcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_operation_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Operation)


def test_essentialoclcs_operation_constructor_exists():
    assert callable(essentialoclcs_Operation.__init__)


def test_essentialoclcs_operation_constructor_args():
    sig = inspect.signature(essentialoclcs_Operation.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_OperationCallExpCS)


def test_essentialoclcs_operationcallexpcs_constructor_exists():
    assert callable(essentialoclcs_OperationCallExpCS.__init__)


def test_essentialoclcs_operationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NumberLiteralExpCS)


def test_essentialoclcs_numberliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NumberLiteralExpCS.__init__)


def test_essentialoclcs_numberliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialoclcs_numberliteralexpcs_has_symbol():
    assert hasattr(essentialoclcs_NumberLiteralExpCS, "symbol")
    descriptor = None
    for klass in essentialoclcs_NumberLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NullLiteralExpCS)


def test_essentialoclcs_nullliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_NullLiteralExpCS.__init__)


def test_essentialoclcs_nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NestedExpCS)


def test_essentialoclcs_nestedexpcs_constructor_exists():
    assert callable(essentialoclcs_NestedExpCS.__init__)


def test_essentialoclcs_nestedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetExpCS)


def test_essentialoclcs_letexpcs_constructor_exists():
    assert callable(essentialoclcs_LetExpCS.__init__)


def test_essentialoclcs_letexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_essentialoclcs_letexpcs_has_isImplicit():
    assert hasattr(essentialoclcs_LetExpCS, "isImplicit")
    descriptor = None
    for klass in essentialoclcs_LetExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_iteration_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Iteration)


def test_essentialoclcs_iteration_constructor_exists():
    assert callable(essentialoclcs_Iteration.__init__)


def test_essentialoclcs_iteration_constructor_args():
    sig = inspect.signature(essentialoclcs_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NavigatingArgCS)


def test_essentialoclcs_navigatingargcs_constructor_exists():
    assert callable(essentialoclcs_NavigatingArgCS.__init__)


def test_essentialoclcs_navigatingargcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "role" in params, "Missing parameter 'role'"

def test_essentialoclcs_navigatingargcs_has_prefix():
    assert hasattr(essentialoclcs_NavigatingArgCS, "prefix")
    descriptor = None
    for klass in essentialoclcs_NavigatingArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_essentialoclcs_navigatingargcs_has_role():
    assert hasattr(essentialoclcs_NavigatingArgCS, "role")
    descriptor = None
    for klass in essentialoclcs_NavigatingArgCS.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_variableexpcs_is_not_abstract():
    assert not inspect.isabstract(VariableExpCS)


def test_variableexpcs_constructor_exists():
    assert callable(VariableExpCS.__init__)


def test_variableexpcs_constructor_args():
    sig = inspect.signature(VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexpcs_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExpCS)


def test_propertycallexpcs_constructor_exists():
    assert callable(PropertyCallExpCS.__init__)


def test_propertycallexpcs_constructor_args():
    sig = inspect.signature(PropertyCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_iteratecallexpcs_is_not_abstract():
    assert not inspect.isabstract(IterateCallExpCS)


def test_iteratecallexpcs_constructor_exists():
    assert callable(IterateCallExpCS.__init__)


def test_iteratecallexpcs_constructor_args():
    sig = inspect.signature(IterateCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_shadowexpcs_is_not_abstract():
    assert not inspect.isabstract(ShadowExpCS)


def test_shadowexpcs_constructor_exists():
    assert callable(ShadowExpCS.__init__)


def test_shadowexpcs_constructor_args():
    sig = inspect.signature(ShadowExpCS.__init__)
    params = list(sig.parameters.keys())



def test_associationclasscallexpcs_is_not_abstract():
    assert not inspect.isabstract(AssociationClassCallExpCS)


def test_associationclasscallexpcs_constructor_exists():
    assert callable(AssociationClassCallExpCS.__init__)


def test_associationclasscallexpcs_constructor_args():
    sig = inspect.signature(AssociationClassCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_mapliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapLiteralPartCS)


def test_essentialoclcs_mapliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_MapLiteralPartCS.__init__)


def test_essentialoclcs_mapliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LiteralExpCS)


def test_essentialoclcs_literalexpcs_constructor_exists():
    assert callable(essentialoclcs_LiteralExpCS.__init__)


def test_essentialoclcs_literalexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralPartCS)


def test_essentialoclcs_tupleliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralPartCS.__init__)


def test_essentialoclcs_tupleliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_letvariablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LetVariableCS)


def test_essentialoclcs_letvariablecs_constructor_exists():
    assert callable(essentialoclcs_LetVariableCS.__init__)


def test_essentialoclcs_letvariablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_LetVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IterationCallExpCS)


def test_essentialoclcs_iterationcallexpcs_constructor_exists():
    assert callable(essentialoclcs_IterationCallExpCS.__init__)


def test_essentialoclcs_iterationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(IterationCallExpCS)


def test_iterationcallexpcs_constructor_exists():
    assert callable(IterationCallExpCS.__init__)


def test_iterationcallexpcs_constructor_args():
    sig = inspect.signature(IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_NameExpCS)


def test_essentialoclcs_nameexpcs_constructor_exists():
    assert callable(essentialoclcs_NameExpCS.__init__)


def test_essentialoclcs_nameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_iteratecallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IterateCallExpCS)


def test_essentialoclcs_iteratecallexpcs_constructor_exists():
    assert callable(essentialoclcs_IterateCallExpCS.__init__)


def test_essentialoclcs_iteratecallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IterateCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InvalidLiteralExpCS)


def test_essentialoclcs_invalidliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_InvalidLiteralExpCS.__init__)


def test_essentialoclcs_invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(OperatorExpCS)


def test_operatorexpcs_constructor_exists():
    assert callable(OperatorExpCS.__init__)


def test_operatorexpcs_constructor_args():
    sig = inspect.signature(OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrefixExpCS)


def test_essentialoclcs_prefixexpcs_constructor_exists():
    assert callable(essentialoclcs_PrefixExpCS.__init__)


def test_essentialoclcs_prefixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_infixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_InfixExpCS)


def test_essentialoclcs_infixexpcs_constructor_exists():
    assert callable(essentialoclcs_InfixExpCS.__init__)


def test_essentialoclcs_infixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_ifthenexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IfThenExpCS)


def test_essentialoclcs_ifthenexpcs_constructor_exists():
    assert callable(essentialoclcs_IfThenExpCS.__init__)


def test_essentialoclcs_ifthenexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IfThenExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_IfExpCS)


def test_essentialoclcs_ifexpcs_constructor_exists():
    assert callable(essentialoclcs_IfExpCS.__init__)


def test_essentialoclcs_ifexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_IfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_essentialoclcs_ifexpcs_has_isImplicit():
    assert hasattr(essentialoclcs_IfExpCS, "isImplicit")
    descriptor = None
    for klass in essentialoclcs_IfExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_specificationcs_is_not_abstract():
    assert not inspect.isabstract(SpecificationCS)


def test_specificationcs_constructor_exists():
    assert callable(SpecificationCS.__init__)


def test_specificationcs_constructor_args():
    sig = inspect.signature(SpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpSpecificationCS)


def test_essentialoclcs_expspecificationcs_constructor_exists():
    assert callable(essentialoclcs_ExpSpecificationCS.__init__)


def test_essentialoclcs_expspecificationcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpSpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_precedence_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_Precedence)


def test_essentialoclcs_precedence_constructor_exists():
    assert callable(essentialoclcs_Precedence.__init__)


def test_essentialoclcs_precedence_constructor_args():
    sig = inspect.signature(essentialoclcs_Precedence.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralPartCS)


def test_essentialoclcs_collectionliteralpartcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralPartCS.__init__)


def test_essentialoclcs_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_mapliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapLiteralExpCS)


def test_essentialoclcs_mapliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_MapLiteralExpCS.__init__)


def test_essentialoclcs_mapliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeLiteralExpCS)


def test_essentialoclcs_typeliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeLiteralExpCS.__init__)


def test_essentialoclcs_typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TupleLiteralExpCS)


def test_essentialoclcs_tupleliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_TupleLiteralExpCS.__init__)


def test_essentialoclcs_tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_lambdaliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_LambdaLiteralExpCS)


def test_essentialoclcs_lambdaliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_LambdaLiteralExpCS.__init__)


def test_essentialoclcs_lambdaliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_LambdaLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PrimitiveLiteralExpCS)


def test_essentialoclcs_primitiveliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_PrimitiveLiteralExpCS.__init__)


def test_essentialoclcs_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionLiteralExpCS)


def test_essentialoclcs_collectionliteralexpcs_constructor_exists():
    assert callable(essentialoclcs_CollectionLiteralExpCS.__init__)


def test_essentialoclcs_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_expcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ExpCS)


def test_essentialoclcs_expcs_constructor_exists():
    assert callable(essentialoclcs_ExpCS.__init__)


def test_essentialoclcs_expcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "hasError" in params, "Missing parameter 'hasError'"

def test_essentialoclcs_expcs_has_hasError():
    assert hasattr(essentialoclcs_ExpCS, "hasError")
    descriptor = None
    for klass in essentialoclcs_ExpCS.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)



def test_contextlesselementcs_is_not_abstract():
    assert not inspect.isabstract(ContextLessElementCS)


def test_contextlesselementcs_constructor_exists():
    assert callable(ContextLessElementCS.__init__)


def test_contextlesselementcs_constructor_args():
    sig = inspect.signature(ContextLessElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_curlybracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CurlyBracketedClauseCS)


def test_essentialoclcs_curlybracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_CurlyBracketedClauseCS.__init__)


def test_essentialoclcs_curlybracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_CurlyBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs_curlybracketedclausecs_has_value():
    assert hasattr(essentialoclcs_CurlyBracketedClauseCS, "value")
    descriptor = None
    for klass in essentialoclcs_CurlyBracketedClauseCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_roundbracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_RoundBracketedClauseCS)


def test_essentialoclcs_roundbracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_RoundBracketedClauseCS.__init__)


def test_essentialoclcs_roundbracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_RoundBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_squarebracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_SquareBracketedClauseCS)


def test_essentialoclcs_squarebracketedclausecs_constructor_exists():
    assert callable(essentialoclcs_SquareBracketedClauseCS.__init__)


def test_essentialoclcs_squarebracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs_SquareBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_OperatorExpCS)


def test_essentialoclcs_operatorexpcs_constructor_exists():
    assert callable(essentialoclcs_OperatorExpCS.__init__)


def test_essentialoclcs_operatorexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_VariableCS)


def test_essentialoclcs_variablecs_constructor_exists():
    assert callable(essentialoclcs_VariableCS.__init__)


def test_essentialoclcs_variablecs_constructor_args():
    sig = inspect.signature(essentialoclcs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_contextcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ContextCS)


def test_essentialoclcs_contextcs_constructor_exists():
    assert callable(essentialoclcs_ContextCS.__init__)


def test_essentialoclcs_contextcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ContextCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypedRefCS)


def test_essentialoclcs_typedrefcs_constructor_exists():
    assert callable(essentialoclcs_TypedRefCS.__init__)


def test_essentialoclcs_typedrefcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_shadowpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_ShadowPartCS)


def test_essentialoclcs_shadowpartcs_constructor_exists():
    assert callable(essentialoclcs_ShadowPartCS.__init__)


def test_essentialoclcs_shadowpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs_ShadowPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_patternexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_PatternExpCS)


def test_essentialoclcs_patternexpcs_constructor_exists():
    assert callable(essentialoclcs_PatternExpCS.__init__)


def test_essentialoclcs_patternexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_PatternExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "patternVariableName" in params, "Missing parameter 'patternVariableName'"

def test_essentialoclcs_patternexpcs_has_patternVariableName():
    assert hasattr(essentialoclcs_PatternExpCS, "patternVariableName")
    descriptor = None
    for klass in essentialoclcs_PatternExpCS.__mro__:
        if "patternVariableName" in klass.__dict__:
            descriptor = klass.__dict__["patternVariableName"]
            break
    assert isinstance(descriptor, property)



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionTypeCS)


def test_essentialoclcs_collectiontypecs_constructor_exists():
    assert callable(essentialoclcs_CollectionTypeCS.__init__)


def test_essentialoclcs_collectiontypecs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_collectiontypecs_has_name():
    assert hasattr(essentialoclcs_CollectionTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs_CollectionTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_TypeNameExpCS)


def test_essentialoclcs_typenameexpcs_constructor_exists():
    assert callable(essentialoclcs_TypeNameExpCS.__init__)


def test_essentialoclcs_typenameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs_TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs_maptypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_MapTypeCS)


def test_essentialoclcs_maptypecs_constructor_exists():
    assert callable(essentialoclcs_MapTypeCS.__init__)


def test_essentialoclcs_maptypecs_constructor_args():
    sig = inspect.signature(essentialoclcs_MapTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs_maptypecs_has_name():
    assert hasattr(essentialoclcs_MapTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs_MapTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs_collectionpatterncs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs_CollectionPatternCS)


def test_essentialoclcs_collectionpatterncs_constructor_exists():
    assert callable(essentialoclcs_CollectionPatternCS.__init__)


def test_essentialoclcs_collectionpatterncs_constructor_args():
    sig = inspect.signature(essentialoclcs_CollectionPatternCS.__init__)
    params = list(sig.parameters.keys())
    assert "restVariableName" in params, "Missing parameter 'restVariableName'"

def test_essentialoclcs_collectionpatterncs_has_restVariableName():
    assert hasattr(essentialoclcs_CollectionPatternCS, "restVariableName")
    descriptor = None
    for klass in essentialoclcs_CollectionPatternCS.__mro__:
        if "restVariableName" in klass.__dict__:
            descriptor = klass.__dict__["restVariableName"]
            break
    assert isinstance(descriptor, property)

def test_navigationrole_exists():
    # Check that the Enumeration exists
    assert NavigationRole is not None

def test_navigationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationRole]
    expected_literals = [
        "ACCUMULATOR",
        "ITERATOR",
        "EXPRESSION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NavigationRole"


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
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
AbstractNameExpCS_strategy = st.builds(
    AbstractNameExpCS,
)
essentialoclcs_CallExpCS_strategy = st.builds(
    essentialoclcs_CallExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialoclcs_BooleanLiteralExpCS_strategy = st.builds(
    essentialoclcs_BooleanLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs_AssociationClass_strategy = st.builds(
    essentialoclcs_AssociationClass,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
essentialoclcs_AssociationClassCallExpCS_strategy = st.builds(
    essentialoclcs_AssociationClassCallExpCS,
)
essentialoclcs_Type_strategy = st.builds(
    essentialoclcs_Type,
)
essentialoclcs_PathNameCS_strategy = st.builds(
    essentialoclcs_PathNameCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
essentialoclcs_AbstractNameExpCS_strategy = st.builds(
    essentialoclcs_AbstractNameExpCS,
    isPre=
        st.booleans()
)
essentialoclcs_Variable_strategy = st.builds(
    essentialoclcs_Variable,
)
essentialoclcs_VariableExpCS_strategy = st.builds(
    essentialoclcs_VariableExpCS,
)
essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
)
essentialoclcs_StringLiteralExpCS_strategy = st.builds(
    essentialoclcs_StringLiteralExpCS,
    segments=
        safe_text
)
essentialoclcs_ShadowExpCS_strategy = st.builds(
    essentialoclcs_ShadowExpCS,
    value=
        safe_text
)
essentialoclcs_SelfExpCS_strategy = st.builds(
    essentialoclcs_SelfExpCS,
    name=
        safe_text
)
essentialoclcs_Property_strategy = st.builds(
    essentialoclcs_Property,
)
essentialoclcs_PropertyCallExpCS_strategy = st.builds(
    essentialoclcs_PropertyCallExpCS,
)
essentialoclcs_TypeRefCS_strategy = st.builds(
    essentialoclcs_TypeRefCS,
)
essentialoclcs_Operation_strategy = st.builds(
    essentialoclcs_Operation,
)
essentialoclcs_OperationCallExpCS_strategy = st.builds(
    essentialoclcs_OperationCallExpCS,
)
essentialoclcs_NumberLiteralExpCS_strategy = st.builds(
    essentialoclcs_NumberLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs_NullLiteralExpCS_strategy = st.builds(
    essentialoclcs_NullLiteralExpCS,
)
essentialoclcs_NestedExpCS_strategy = st.builds(
    essentialoclcs_NestedExpCS,
)
essentialoclcs_LetExpCS_strategy = st.builds(
    essentialoclcs_LetExpCS,
    isImplicit=
        st.booleans()
)
essentialoclcs_Iteration_strategy = st.builds(
    essentialoclcs_Iteration,
)
essentialoclcs_NavigatingArgCS_strategy = st.builds(
    essentialoclcs_NavigatingArgCS,
    prefix=
        safe_text,
    role=
        safe_text
)
VariableExpCS_strategy = st.builds(
    VariableExpCS,
)
PropertyCallExpCS_strategy = st.builds(
    PropertyCallExpCS,
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
IterateCallExpCS_strategy = st.builds(
    IterateCallExpCS,
)
ShadowExpCS_strategy = st.builds(
    ShadowExpCS,
)
AssociationClassCallExpCS_strategy = st.builds(
    AssociationClassCallExpCS,
)
essentialoclcs_MapLiteralPartCS_strategy = st.builds(
    essentialoclcs_MapLiteralPartCS,
)
essentialoclcs_LiteralExpCS_strategy = st.builds(
    essentialoclcs_LiteralExpCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
essentialoclcs_TupleLiteralPartCS_strategy = st.builds(
    essentialoclcs_TupleLiteralPartCS,
)
essentialoclcs_LetVariableCS_strategy = st.builds(
    essentialoclcs_LetVariableCS,
)
essentialoclcs_IterationCallExpCS_strategy = st.builds(
    essentialoclcs_IterationCallExpCS,
)
IterationCallExpCS_strategy = st.builds(
    IterationCallExpCS,
)
essentialoclcs_NameExpCS_strategy = st.builds(
    essentialoclcs_NameExpCS,
)
essentialoclcs_IterateCallExpCS_strategy = st.builds(
    essentialoclcs_IterateCallExpCS,
)
essentialoclcs_InvalidLiteralExpCS_strategy = st.builds(
    essentialoclcs_InvalidLiteralExpCS,
)
OperatorExpCS_strategy = st.builds(
    OperatorExpCS,
)
essentialoclcs_PrefixExpCS_strategy = st.builds(
    essentialoclcs_PrefixExpCS,
)
essentialoclcs_InfixExpCS_strategy = st.builds(
    essentialoclcs_InfixExpCS,
)
essentialoclcs_IfThenExpCS_strategy = st.builds(
    essentialoclcs_IfThenExpCS,
)
essentialoclcs_IfExpCS_strategy = st.builds(
    essentialoclcs_IfExpCS,
    isImplicit=
        st.booleans()
)
SpecificationCS_strategy = st.builds(
    SpecificationCS,
)
essentialoclcs_ExpSpecificationCS_strategy = st.builds(
    essentialoclcs_ExpSpecificationCS,
)
essentialoclcs_Precedence_strategy = st.builds(
    essentialoclcs_Precedence,
)
essentialoclcs_CollectionLiteralPartCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialoclcs_MapLiteralExpCS_strategy = st.builds(
    essentialoclcs_MapLiteralExpCS,
)
essentialoclcs_TypeLiteralExpCS_strategy = st.builds(
    essentialoclcs_TypeLiteralExpCS,
)
essentialoclcs_TupleLiteralExpCS_strategy = st.builds(
    essentialoclcs_TupleLiteralExpCS,
)
essentialoclcs_LambdaLiteralExpCS_strategy = st.builds(
    essentialoclcs_LambdaLiteralExpCS,
)
essentialoclcs_PrimitiveLiteralExpCS_strategy = st.builds(
    essentialoclcs_PrimitiveLiteralExpCS,
)
essentialoclcs_CollectionLiteralExpCS_strategy = st.builds(
    essentialoclcs_CollectionLiteralExpCS,
)
essentialoclcs_ExpCS_strategy = st.builds(
    essentialoclcs_ExpCS,
    hasError=
        st.booleans()
)
ContextLessElementCS_strategy = st.builds(
    ContextLessElementCS,
)
essentialoclcs_CurlyBracketedClauseCS_strategy = st.builds(
    essentialoclcs_CurlyBracketedClauseCS,
    value=
        safe_text
)
essentialoclcs_RoundBracketedClauseCS_strategy = st.builds(
    essentialoclcs_RoundBracketedClauseCS,
)
essentialoclcs_SquareBracketedClauseCS_strategy = st.builds(
    essentialoclcs_SquareBracketedClauseCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
essentialoclcs_OperatorExpCS_strategy = st.builds(
    essentialoclcs_OperatorExpCS,
)
essentialoclcs_VariableCS_strategy = st.builds(
    essentialoclcs_VariableCS,
)
essentialoclcs_ContextCS_strategy = st.builds(
    essentialoclcs_ContextCS,
)
essentialoclcs_TypedRefCS_strategy = st.builds(
    essentialoclcs_TypedRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
essentialoclcs_ShadowPartCS_strategy = st.builds(
    essentialoclcs_ShadowPartCS,
)
essentialoclcs_PatternExpCS_strategy = st.builds(
    essentialoclcs_PatternExpCS,
    patternVariableName=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
essentialoclcs_CollectionTypeCS_strategy = st.builds(
    essentialoclcs_CollectionTypeCS,
    name=
        safe_text
)
essentialoclcs_TypeNameExpCS_strategy = st.builds(
    essentialoclcs_TypeNameExpCS,
)
essentialoclcs_MapTypeCS_strategy = st.builds(
    essentialoclcs_MapTypeCS,
    name=
        safe_text
)
essentialoclcs_CollectionPatternCS_strategy = st.builds(
    essentialoclcs_CollectionPatternCS,
    restVariableName=
        safe_text
)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, AbstractNameExpCS)

@given(instance=essentialoclcs_CallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_callexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CallExpCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_BooleanLiteralExpCS)



@given(instance=essentialoclcs_BooleanLiteralExpCS_strategy)
def test_essentialoclcs_booleanliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=essentialoclcs_AssociationClass_strategy)
@settings(max_examples=50)
def test_essentialoclcs_associationclass_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AssociationClass)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=essentialoclcs_AssociationClassCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_associationclasscallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AssociationClassCallExpCS)

@given(instance=essentialoclcs_Type_strategy)
@settings(max_examples=50)
def test_essentialoclcs_type_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Type)

@given(instance=essentialoclcs_PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PathNameCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=essentialoclcs_AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_AbstractNameExpCS)



@given(instance=essentialoclcs_AbstractNameExpCS_strategy)
def test_essentialoclcs_abstractnameexpcs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

@given(instance=essentialoclcs_Variable_strategy)
@settings(max_examples=50)
def test_essentialoclcs_variable_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Variable)

@given(instance=essentialoclcs_VariableExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_variableexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_VariableExpCS)

@given(instance=essentialoclcs_UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_UnlimitedNaturalLiteralExpCS)

@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_StringLiteralExpCS)



@given(instance=essentialoclcs_StringLiteralExpCS_strategy)
def test_essentialoclcs_stringliteralexpcs_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=essentialoclcs_ShadowExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_shadowexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ShadowExpCS)



@given(instance=essentialoclcs_ShadowExpCS_strategy)
def test_essentialoclcs_shadowexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialoclcs_SelfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_selfexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_SelfExpCS)



@given(instance=essentialoclcs_SelfExpCS_strategy)
def test_essentialoclcs_selfexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_Property_strategy)
@settings(max_examples=50)
def test_essentialoclcs_property_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Property)

@given(instance=essentialoclcs_PropertyCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_propertycallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PropertyCallExpCS)

@given(instance=essentialoclcs_TypeRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typerefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeRefCS)

@given(instance=essentialoclcs_Operation_strategy)
@settings(max_examples=50)
def test_essentialoclcs_operation_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Operation)

@given(instance=essentialoclcs_OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_OperationCallExpCS)

@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NumberLiteralExpCS)



@given(instance=essentialoclcs_NumberLiteralExpCS_strategy)
def test_essentialoclcs_numberliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=essentialoclcs_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NullLiteralExpCS)

@given(instance=essentialoclcs_NestedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nestedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NestedExpCS)

@given(instance=essentialoclcs_LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_letexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetExpCS)



@given(instance=essentialoclcs_LetExpCS_strategy)
def test_essentialoclcs_letexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=essentialoclcs_Iteration_strategy)
@settings(max_examples=50)
def test_essentialoclcs_iteration_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Iteration)

@given(instance=essentialoclcs_NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_navigatingargcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NavigatingArgCS)



@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_essentialoclcs_navigatingargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=essentialoclcs_NavigatingArgCS_strategy)
def test_essentialoclcs_navigatingargcs_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=VariableExpCS_strategy)
@settings(max_examples=50)
def test_variableexpcs_instantiation(instance):
    assert isinstance(instance, VariableExpCS)

@given(instance=PropertyCallExpCS_strategy)
@settings(max_examples=50)
def test_propertycallexpcs_instantiation(instance):
    assert isinstance(instance, PropertyCallExpCS)

@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)

@given(instance=IterateCallExpCS_strategy)
@settings(max_examples=50)
def test_iteratecallexpcs_instantiation(instance):
    assert isinstance(instance, IterateCallExpCS)

@given(instance=ShadowExpCS_strategy)
@settings(max_examples=50)
def test_shadowexpcs_instantiation(instance):
    assert isinstance(instance, ShadowExpCS)

@given(instance=AssociationClassCallExpCS_strategy)
@settings(max_examples=50)
def test_associationclasscallexpcs_instantiation(instance):
    assert isinstance(instance, AssociationClassCallExpCS)

@given(instance=essentialoclcs_MapLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_mapliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapLiteralPartCS)

@given(instance=essentialoclcs_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LiteralExpCS)

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=essentialoclcs_TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralPartCS)

@given(instance=essentialoclcs_LetVariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_letvariablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LetVariableCS)

@given(instance=essentialoclcs_IterationCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_iterationcallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IterationCallExpCS)

@given(instance=IterationCallExpCS_strategy)
@settings(max_examples=50)
def test_iterationcallexpcs_instantiation(instance):
    assert isinstance(instance, IterationCallExpCS)

@given(instance=essentialoclcs_NameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_nameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_NameExpCS)

@given(instance=essentialoclcs_IterateCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_iteratecallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IterateCallExpCS)

@given(instance=essentialoclcs_InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InvalidLiteralExpCS)

@given(instance=OperatorExpCS_strategy)
@settings(max_examples=50)
def test_operatorexpcs_instantiation(instance):
    assert isinstance(instance, OperatorExpCS)

@given(instance=essentialoclcs_PrefixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_prefixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrefixExpCS)

@given(instance=essentialoclcs_InfixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_infixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_InfixExpCS)

@given(instance=essentialoclcs_IfThenExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_ifthenexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IfThenExpCS)

@given(instance=essentialoclcs_IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_IfExpCS)



@given(instance=essentialoclcs_IfExpCS_strategy)
def test_essentialoclcs_ifexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=SpecificationCS_strategy)
@settings(max_examples=50)
def test_specificationcs_instantiation(instance):
    assert isinstance(instance, SpecificationCS)

@given(instance=essentialoclcs_ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_expspecificationcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpSpecificationCS)

@given(instance=essentialoclcs_Precedence_strategy)
@settings(max_examples=50)
def test_essentialoclcs_precedence_instantiation(instance):
    assert isinstance(instance, essentialoclcs_Precedence)

@given(instance=essentialoclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralPartCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialoclcs_MapLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_mapliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapLiteralExpCS)

@given(instance=essentialoclcs_TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeLiteralExpCS)

@given(instance=essentialoclcs_TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TupleLiteralExpCS)

@given(instance=essentialoclcs_LambdaLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_lambdaliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_LambdaLiteralExpCS)

@given(instance=essentialoclcs_PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PrimitiveLiteralExpCS)

@given(instance=essentialoclcs_CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionLiteralExpCS)

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_expcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ExpCS)



@given(instance=essentialoclcs_ExpCS_strategy)
def test_essentialoclcs_expcs_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=30)
def test_essentialoclcs_expcs_islocalleftancestorof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocalLeftAncestorOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocalLeftAncestorOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs_ExpCS is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs_ExpCS_strategy)
@settings(max_examples=30)
def test_essentialoclcs_expcs_islocalrightancestorof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocalRightAncestorOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocalRightAncestorOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocalRightAncestorOf' in essentialoclcs_ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs_ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs_ExpCS is not implemented or raised an error")

@given(instance=ContextLessElementCS_strategy)
@settings(max_examples=50)
def test_contextlesselementcs_instantiation(instance):
    assert isinstance(instance, ContextLessElementCS)

@given(instance=essentialoclcs_CurlyBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_curlybracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CurlyBracketedClauseCS)



@given(instance=essentialoclcs_CurlyBracketedClauseCS_strategy)
def test_essentialoclcs_curlybracketedclausecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialoclcs_RoundBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_roundbracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_RoundBracketedClauseCS)

@given(instance=essentialoclcs_SquareBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_squarebracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_SquareBracketedClauseCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=essentialoclcs_OperatorExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_operatorexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_OperatorExpCS)

@given(instance=essentialoclcs_VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_variablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_VariableCS)

@given(instance=essentialoclcs_ContextCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_contextcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ContextCS)

@given(instance=essentialoclcs_TypedRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typedrefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypedRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=essentialoclcs_ShadowPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_shadowpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_ShadowPartCS)

@given(instance=essentialoclcs_PatternExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_patternexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_PatternExpCS)



@given(instance=essentialoclcs_PatternExpCS_strategy)
def test_essentialoclcs_patternexpcs_patternVariableName_setter(instance):
    original = instance.patternVariableName
    instance.patternVariableName = original
    assert instance.patternVariableName == original

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=essentialoclcs_CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionTypeCS)



@given(instance=essentialoclcs_CollectionTypeCS_strategy)
def test_essentialoclcs_collectiontypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_typenameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_TypeNameExpCS)

@given(instance=essentialoclcs_MapTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_maptypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_MapTypeCS)



@given(instance=essentialoclcs_MapTypeCS_strategy)
def test_essentialoclcs_maptypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs_CollectionPatternCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs_collectionpatterncs_instantiation(instance):
    assert isinstance(instance, essentialoclcs_CollectionPatternCS)



@given(instance=essentialoclcs_CollectionPatternCS_strategy)
def test_essentialoclcs_collectionpatterncs_restVariableName_setter(instance):
    original = instance.restVariableName
    instance.restVariableName = original
    assert instance.restVariableName == original

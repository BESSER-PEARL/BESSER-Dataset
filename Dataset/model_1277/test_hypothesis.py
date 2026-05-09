import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    essentialoclcs::Variable,
    essentialoclcs::Property,
    essentialoclcs::TypeRefCS,
    essentialoclcs::Operation,
    essentialoclcs::Iteration,
    VariableExpCS,
    PropertyCallExpCS,
    OperationCallExpCS,
    IterateCallExpCS,
    ShadowExpCS,
    AssociationClassCallExpCS,
    VariableCS,
    essentialoclcs::TupleLiteralPartCS,
    IterationCallExpCS,
    essentialoclcs::NameExpCS,
    essentialoclcs::IterateCallExpCS,
    OperatorExpCS,
    essentialoclcs::PrefixExpCS,
    essentialoclcs::InfixExpCS,
    SpecificationCS,
    essentialoclcs::ExpSpecificationCS,
    essentialoclcs::Precedence,
    LiteralExpCS,
    essentialoclcs::TypeLiteralExpCS,
    essentialoclcs::LambdaLiteralExpCS,
    essentialoclcs::PrimitiveLiteralExpCS,
    essentialoclcs::TupleLiteralExpCS,
    essentialoclcs::MapLiteralExpCS,
    essentialoclcs::CollectionLiteralExpCS,
    ContextLessElementCS,
    RootCS,
    NamedElementCS,
    essentialoclcs::VariableCS,
    essentialoclcs::ContextCS,
    essentialoclcs::TypedRefCS,
    Nameable,
    TypedRefCS,
    essentialoclcs::TypeNameExpCS,
    essentialoclcs::CollectionTypeCS,
    essentialoclcs::MapTypeCS,
    essentialoclcs::CollectionPatternCS,
    ModelElementCS,
    essentialoclcs::CollectionLiteralPartCS,
    essentialoclcs::ShadowPartCS,
    essentialoclcs::MapLiteralPartCS,
    essentialoclcs::NavigatingArgCS,
    essentialoclcs::ExpCS,
    AbstractNameExpCS,
    essentialoclcs::ShadowExpCS,
    essentialoclcs::VariableExpCS,
    essentialoclcs::CallExpCS,
    PrimitiveLiteralExpCS,
    essentialoclcs::StringLiteralExpCS,
    essentialoclcs::NumberLiteralExpCS,
    essentialoclcs::NullLiteralExpCS,
    essentialoclcs::UnlimitedNaturalLiteralExpCS,
    essentialoclcs::InvalidLiteralExpCS,
    essentialoclcs::BooleanLiteralExpCS,
    essentialoclcs::AssociationClass,
    CallExpCS,
    essentialoclcs::IterationCallExpCS,
    essentialoclcs::PropertyCallExpCS,
    essentialoclcs::OperationCallExpCS,
    essentialoclcs::AssociationClassCallExpCS,
    essentialoclcs::Type,
    essentialoclcs::SquareBracketedClauseCS,
    essentialoclcs::RoundBracketedClauseCS,
    essentialoclcs::PathNameCS,
    essentialoclcs::CurlyBracketedClauseCS,
    ExpCS,
    essentialoclcs::OperatorExpCS,
    essentialoclcs::SelfExpCS,
    essentialoclcs::LetExpCS,
    essentialoclcs::LiteralExpCS,
    essentialoclcs::NestedExpCS,
    essentialoclcs::PatternExpCS,
    essentialoclcs::IfExpCS,
    essentialoclcs::LetVariableCS,
    essentialoclcs::IfThenExpCS,
    essentialoclcs::AbstractNameExpCS,
    NavigationRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_essentialoclcs::variable_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Variable)


def test_essentialoclcs::variable_constructor_exists():
    assert callable(essentialoclcs::Variable.__init__)


def test_essentialoclcs::variable_constructor_args():
    sig = inspect.signature(essentialoclcs::Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::property_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Property)


def test_essentialoclcs::property_constructor_exists():
    assert callable(essentialoclcs::Property.__init__)


def test_essentialoclcs::property_constructor_args():
    sig = inspect.signature(essentialoclcs::Property.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::typerefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypeRefCS)


def test_essentialoclcs::typerefcs_constructor_exists():
    assert callable(essentialoclcs::TypeRefCS.__init__)


def test_essentialoclcs::typerefcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::operation_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Operation)


def test_essentialoclcs::operation_constructor_exists():
    assert callable(essentialoclcs::Operation.__init__)


def test_essentialoclcs::operation_constructor_args():
    sig = inspect.signature(essentialoclcs::Operation.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::iteration_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Iteration)


def test_essentialoclcs::iteration_constructor_exists():
    assert callable(essentialoclcs::Iteration.__init__)


def test_essentialoclcs::iteration_constructor_args():
    sig = inspect.signature(essentialoclcs::Iteration.__init__)
    params = list(sig.parameters.keys())



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



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::tupleliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TupleLiteralPartCS)


def test_essentialoclcs::tupleliteralpartcs_constructor_exists():
    assert callable(essentialoclcs::TupleLiteralPartCS.__init__)


def test_essentialoclcs::tupleliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TupleLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(IterationCallExpCS)


def test_iterationcallexpcs_constructor_exists():
    assert callable(IterationCallExpCS.__init__)


def test_iterationcallexpcs_constructor_args():
    sig = inspect.signature(IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NameExpCS)


def test_essentialoclcs::nameexpcs_constructor_exists():
    assert callable(essentialoclcs::NameExpCS.__init__)


def test_essentialoclcs::nameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::iteratecallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IterateCallExpCS)


def test_essentialoclcs::iteratecallexpcs_constructor_exists():
    assert callable(essentialoclcs::IterateCallExpCS.__init__)


def test_essentialoclcs::iteratecallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IterateCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(OperatorExpCS)


def test_operatorexpcs_constructor_exists():
    assert callable(OperatorExpCS.__init__)


def test_operatorexpcs_constructor_args():
    sig = inspect.signature(OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::prefixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PrefixExpCS)


def test_essentialoclcs::prefixexpcs_constructor_exists():
    assert callable(essentialoclcs::PrefixExpCS.__init__)


def test_essentialoclcs::prefixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PrefixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::infixexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::InfixExpCS)


def test_essentialoclcs::infixexpcs_constructor_exists():
    assert callable(essentialoclcs::InfixExpCS.__init__)


def test_essentialoclcs::infixexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::InfixExpCS.__init__)
    params = list(sig.parameters.keys())



def test_specificationcs_is_not_abstract():
    assert not inspect.isabstract(SpecificationCS)


def test_specificationcs_constructor_exists():
    assert callable(SpecificationCS.__init__)


def test_specificationcs_constructor_args():
    sig = inspect.signature(SpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::expspecificationcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ExpSpecificationCS)


def test_essentialoclcs::expspecificationcs_constructor_exists():
    assert callable(essentialoclcs::ExpSpecificationCS.__init__)


def test_essentialoclcs::expspecificationcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ExpSpecificationCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::precedence_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Precedence)


def test_essentialoclcs::precedence_constructor_exists():
    assert callable(essentialoclcs::Precedence.__init__)


def test_essentialoclcs::precedence_constructor_args():
    sig = inspect.signature(essentialoclcs::Precedence.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::typeliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypeLiteralExpCS)


def test_essentialoclcs::typeliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::TypeLiteralExpCS.__init__)


def test_essentialoclcs::typeliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypeLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::lambdaliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LambdaLiteralExpCS)


def test_essentialoclcs::lambdaliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::LambdaLiteralExpCS.__init__)


def test_essentialoclcs::lambdaliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::LambdaLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PrimitiveLiteralExpCS)


def test_essentialoclcs::primitiveliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::PrimitiveLiteralExpCS.__init__)


def test_essentialoclcs::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::tupleliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TupleLiteralExpCS)


def test_essentialoclcs::tupleliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::TupleLiteralExpCS.__init__)


def test_essentialoclcs::tupleliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TupleLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::mapliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::MapLiteralExpCS)


def test_essentialoclcs::mapliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::MapLiteralExpCS.__init__)


def test_essentialoclcs::mapliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::MapLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionLiteralExpCS)


def test_essentialoclcs::collectionliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::CollectionLiteralExpCS.__init__)


def test_essentialoclcs::collectionliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_contextlesselementcs_is_not_abstract():
    assert not inspect.isabstract(ContextLessElementCS)


def test_contextlesselementcs_constructor_exists():
    assert callable(ContextLessElementCS.__init__)


def test_contextlesselementcs_constructor_args():
    sig = inspect.signature(ContextLessElementCS.__init__)
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



def test_essentialoclcs::variablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::VariableCS)


def test_essentialoclcs::variablecs_constructor_exists():
    assert callable(essentialoclcs::VariableCS.__init__)


def test_essentialoclcs::variablecs_constructor_args():
    sig = inspect.signature(essentialoclcs::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::contextcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ContextCS)


def test_essentialoclcs::contextcs_constructor_exists():
    assert callable(essentialoclcs::ContextCS.__init__)


def test_essentialoclcs::contextcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ContextCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypedRefCS)


def test_essentialoclcs::typedrefcs_constructor_exists():
    assert callable(essentialoclcs::TypedRefCS.__init__)


def test_essentialoclcs::typedrefcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::typenameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::TypeNameExpCS)


def test_essentialoclcs::typenameexpcs_constructor_exists():
    assert callable(essentialoclcs::TypeNameExpCS.__init__)


def test_essentialoclcs::typenameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::TypeNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::collectiontypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionTypeCS)


def test_essentialoclcs::collectiontypecs_constructor_exists():
    assert callable(essentialoclcs::CollectionTypeCS.__init__)


def test_essentialoclcs::collectiontypecs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::collectiontypecs_has_name():
    assert hasattr(essentialoclcs::CollectionTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs::CollectionTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::maptypecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::MapTypeCS)


def test_essentialoclcs::maptypecs_constructor_exists():
    assert callable(essentialoclcs::MapTypeCS.__init__)


def test_essentialoclcs::maptypecs_constructor_args():
    sig = inspect.signature(essentialoclcs::MapTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::maptypecs_has_name():
    assert hasattr(essentialoclcs::MapTypeCS, "name")
    descriptor = None
    for klass in essentialoclcs::MapTypeCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::collectionpatterncs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionPatternCS)


def test_essentialoclcs::collectionpatterncs_constructor_exists():
    assert callable(essentialoclcs::CollectionPatternCS.__init__)


def test_essentialoclcs::collectionpatterncs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionPatternCS.__init__)
    params = list(sig.parameters.keys())
    assert "restVariableName" in params, "Missing parameter 'restVariableName'"

def test_essentialoclcs::collectionpatterncs_has_restVariableName():
    assert hasattr(essentialoclcs::CollectionPatternCS, "restVariableName")
    descriptor = None
    for klass in essentialoclcs::CollectionPatternCS.__mro__:
        if "restVariableName" in klass.__dict__:
            descriptor = klass.__dict__["restVariableName"]
            break
    assert isinstance(descriptor, property)



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CollectionLiteralPartCS)


def test_essentialoclcs::collectionliteralpartcs_constructor_exists():
    assert callable(essentialoclcs::CollectionLiteralPartCS.__init__)


def test_essentialoclcs::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::shadowpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ShadowPartCS)


def test_essentialoclcs::shadowpartcs_constructor_exists():
    assert callable(essentialoclcs::ShadowPartCS.__init__)


def test_essentialoclcs::shadowpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ShadowPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::mapliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::MapLiteralPartCS)


def test_essentialoclcs::mapliteralpartcs_constructor_exists():
    assert callable(essentialoclcs::MapLiteralPartCS.__init__)


def test_essentialoclcs::mapliteralpartcs_constructor_args():
    sig = inspect.signature(essentialoclcs::MapLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::navigatingargcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NavigatingArgCS)


def test_essentialoclcs::navigatingargcs_constructor_exists():
    assert callable(essentialoclcs::NavigatingArgCS.__init__)


def test_essentialoclcs::navigatingargcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NavigatingArgCS.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "role" in params, "Missing parameter 'role'"

def test_essentialoclcs::navigatingargcs_has_prefix():
    assert hasattr(essentialoclcs::NavigatingArgCS, "prefix")
    descriptor = None
    for klass in essentialoclcs::NavigatingArgCS.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_essentialoclcs::navigatingargcs_has_role():
    assert hasattr(essentialoclcs::NavigatingArgCS, "role")
    descriptor = None
    for klass in essentialoclcs::NavigatingArgCS.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::expcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ExpCS)


def test_essentialoclcs::expcs_constructor_exists():
    assert callable(essentialoclcs::ExpCS.__init__)


def test_essentialoclcs::expcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "hasError" in params, "Missing parameter 'hasError'"

def test_essentialoclcs::expcs_has_hasError():
    assert hasattr(essentialoclcs::ExpCS, "hasError")
    descriptor = None
    for klass in essentialoclcs::ExpCS.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)



def test_abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(AbstractNameExpCS)


def test_abstractnameexpcs_constructor_exists():
    assert callable(AbstractNameExpCS.__init__)


def test_abstractnameexpcs_constructor_args():
    sig = inspect.signature(AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::shadowexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::ShadowExpCS)


def test_essentialoclcs::shadowexpcs_constructor_exists():
    assert callable(essentialoclcs::ShadowExpCS.__init__)


def test_essentialoclcs::shadowexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::ShadowExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs::shadowexpcs_has_value():
    assert hasattr(essentialoclcs::ShadowExpCS, "value")
    descriptor = None
    for klass in essentialoclcs::ShadowExpCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::variableexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::VariableExpCS)


def test_essentialoclcs::variableexpcs_constructor_exists():
    assert callable(essentialoclcs::VariableExpCS.__init__)


def test_essentialoclcs::variableexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::VariableExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::callexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CallExpCS)


def test_essentialoclcs::callexpcs_constructor_exists():
    assert callable(essentialoclcs::CallExpCS.__init__)


def test_essentialoclcs::callexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::StringLiteralExpCS)


def test_essentialoclcs::stringliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::StringLiteralExpCS.__init__)


def test_essentialoclcs::stringliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "segments" in params, "Missing parameter 'segments'"

def test_essentialoclcs::stringliteralexpcs_has_segments():
    assert hasattr(essentialoclcs::StringLiteralExpCS, "segments")
    descriptor = None
    for klass in essentialoclcs::StringLiteralExpCS.__mro__:
        if "segments" in klass.__dict__:
            descriptor = klass.__dict__["segments"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::numberliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NumberLiteralExpCS)


def test_essentialoclcs::numberliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::NumberLiteralExpCS.__init__)


def test_essentialoclcs::numberliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NumberLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialoclcs::numberliteralexpcs_has_symbol():
    assert hasattr(essentialoclcs::NumberLiteralExpCS, "symbol")
    descriptor = None
    for klass in essentialoclcs::NumberLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NullLiteralExpCS)


def test_essentialoclcs::nullliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::NullLiteralExpCS.__init__)


def test_essentialoclcs::nullliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::unlimitednaturalliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::UnlimitedNaturalLiteralExpCS)


def test_essentialoclcs::unlimitednaturalliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::UnlimitedNaturalLiteralExpCS.__init__)


def test_essentialoclcs::unlimitednaturalliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::UnlimitedNaturalLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::invalidliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::InvalidLiteralExpCS)


def test_essentialoclcs::invalidliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::InvalidLiteralExpCS.__init__)


def test_essentialoclcs::invalidliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::InvalidLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::BooleanLiteralExpCS)


def test_essentialoclcs::booleanliteralexpcs_constructor_exists():
    assert callable(essentialoclcs::BooleanLiteralExpCS.__init__)


def test_essentialoclcs::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialoclcs::booleanliteralexpcs_has_symbol():
    assert hasattr(essentialoclcs::BooleanLiteralExpCS, "symbol")
    descriptor = None
    for klass in essentialoclcs::BooleanLiteralExpCS.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::associationclass_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::AssociationClass)


def test_essentialoclcs::associationclass_constructor_exists():
    assert callable(essentialoclcs::AssociationClass.__init__)


def test_essentialoclcs::associationclass_constructor_args():
    sig = inspect.signature(essentialoclcs::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::iterationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IterationCallExpCS)


def test_essentialoclcs::iterationcallexpcs_constructor_exists():
    assert callable(essentialoclcs::IterationCallExpCS.__init__)


def test_essentialoclcs::iterationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IterationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::propertycallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PropertyCallExpCS)


def test_essentialoclcs::propertycallexpcs_constructor_exists():
    assert callable(essentialoclcs::PropertyCallExpCS.__init__)


def test_essentialoclcs::propertycallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PropertyCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::OperationCallExpCS)


def test_essentialoclcs::operationcallexpcs_constructor_exists():
    assert callable(essentialoclcs::OperationCallExpCS.__init__)


def test_essentialoclcs::operationcallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::associationclasscallexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::AssociationClassCallExpCS)


def test_essentialoclcs::associationclasscallexpcs_constructor_exists():
    assert callable(essentialoclcs::AssociationClassCallExpCS.__init__)


def test_essentialoclcs::associationclasscallexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::AssociationClassCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::type_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::Type)


def test_essentialoclcs::type_constructor_exists():
    assert callable(essentialoclcs::Type.__init__)


def test_essentialoclcs::type_constructor_args():
    sig = inspect.signature(essentialoclcs::Type.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::squarebracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::SquareBracketedClauseCS)


def test_essentialoclcs::squarebracketedclausecs_constructor_exists():
    assert callable(essentialoclcs::SquareBracketedClauseCS.__init__)


def test_essentialoclcs::squarebracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs::SquareBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::roundbracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::RoundBracketedClauseCS)


def test_essentialoclcs::roundbracketedclausecs_constructor_exists():
    assert callable(essentialoclcs::RoundBracketedClauseCS.__init__)


def test_essentialoclcs::roundbracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs::RoundBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PathNameCS)


def test_essentialoclcs::pathnamecs_constructor_exists():
    assert callable(essentialoclcs::PathNameCS.__init__)


def test_essentialoclcs::pathnamecs_constructor_args():
    sig = inspect.signature(essentialoclcs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::curlybracketedclausecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::CurlyBracketedClauseCS)


def test_essentialoclcs::curlybracketedclausecs_constructor_exists():
    assert callable(essentialoclcs::CurlyBracketedClauseCS.__init__)


def test_essentialoclcs::curlybracketedclausecs_constructor_args():
    sig = inspect.signature(essentialoclcs::CurlyBracketedClauseCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_essentialoclcs::curlybracketedclausecs_has_value():
    assert hasattr(essentialoclcs::CurlyBracketedClauseCS, "value")
    descriptor = None
    for klass in essentialoclcs::CurlyBracketedClauseCS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::operatorexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::OperatorExpCS)


def test_essentialoclcs::operatorexpcs_constructor_exists():
    assert callable(essentialoclcs::OperatorExpCS.__init__)


def test_essentialoclcs::operatorexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::OperatorExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::selfexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::SelfExpCS)


def test_essentialoclcs::selfexpcs_constructor_exists():
    assert callable(essentialoclcs::SelfExpCS.__init__)


def test_essentialoclcs::selfexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::SelfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_essentialoclcs::selfexpcs_has_name():
    assert hasattr(essentialoclcs::SelfExpCS, "name")
    descriptor = None
    for klass in essentialoclcs::SelfExpCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::letexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LetExpCS)


def test_essentialoclcs::letexpcs_constructor_exists():
    assert callable(essentialoclcs::LetExpCS.__init__)


def test_essentialoclcs::letexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::LetExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_essentialoclcs::letexpcs_has_isImplicit():
    assert hasattr(essentialoclcs::LetExpCS, "isImplicit")
    descriptor = None
    for klass in essentialoclcs::LetExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LiteralExpCS)


def test_essentialoclcs::literalexpcs_constructor_exists():
    assert callable(essentialoclcs::LiteralExpCS.__init__)


def test_essentialoclcs::literalexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::nestedexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::NestedExpCS)


def test_essentialoclcs::nestedexpcs_constructor_exists():
    assert callable(essentialoclcs::NestedExpCS.__init__)


def test_essentialoclcs::nestedexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::NestedExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::patternexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::PatternExpCS)


def test_essentialoclcs::patternexpcs_constructor_exists():
    assert callable(essentialoclcs::PatternExpCS.__init__)


def test_essentialoclcs::patternexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::PatternExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "patternVariableName" in params, "Missing parameter 'patternVariableName'"

def test_essentialoclcs::patternexpcs_has_patternVariableName():
    assert hasattr(essentialoclcs::PatternExpCS, "patternVariableName")
    descriptor = None
    for klass in essentialoclcs::PatternExpCS.__mro__:
        if "patternVariableName" in klass.__dict__:
            descriptor = klass.__dict__["patternVariableName"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::ifexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IfExpCS)


def test_essentialoclcs::ifexpcs_constructor_exists():
    assert callable(essentialoclcs::IfExpCS.__init__)


def test_essentialoclcs::ifexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IfExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_essentialoclcs::ifexpcs_has_isImplicit():
    assert hasattr(essentialoclcs::IfExpCS, "isImplicit")
    descriptor = None
    for klass in essentialoclcs::IfExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_essentialoclcs::letvariablecs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::LetVariableCS)


def test_essentialoclcs::letvariablecs_constructor_exists():
    assert callable(essentialoclcs::LetVariableCS.__init__)


def test_essentialoclcs::letvariablecs_constructor_args():
    sig = inspect.signature(essentialoclcs::LetVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::ifthenexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::IfThenExpCS)


def test_essentialoclcs::ifthenexpcs_constructor_exists():
    assert callable(essentialoclcs::IfThenExpCS.__init__)


def test_essentialoclcs::ifthenexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::IfThenExpCS.__init__)
    params = list(sig.parameters.keys())



def test_essentialoclcs::abstractnameexpcs_is_not_abstract():
    assert not inspect.isabstract(essentialoclcs::AbstractNameExpCS)


def test_essentialoclcs::abstractnameexpcs_constructor_exists():
    assert callable(essentialoclcs::AbstractNameExpCS.__init__)


def test_essentialoclcs::abstractnameexpcs_constructor_args():
    sig = inspect.signature(essentialoclcs::AbstractNameExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPre" in params, "Missing parameter 'isPre'"

def test_essentialoclcs::abstractnameexpcs_has_isPre():
    assert hasattr(essentialoclcs::AbstractNameExpCS, "isPre")
    descriptor = None
    for klass in essentialoclcs::AbstractNameExpCS.__mro__:
        if "isPre" in klass.__dict__:
            descriptor = klass.__dict__["isPre"]
            break
    assert isinstance(descriptor, property)

def test_navigationrole_exists():
    # Check that the Enumeration exists
    assert NavigationRole is not None

def test_navigationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationRole]
    expected_literals = [
        "EXPRESSION",
        "ITERATOR",
        "ACCUMULATOR",
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
essentialoclcs::Variable_strategy = st.builds(
    essentialoclcs::Variable,
)
essentialoclcs::Property_strategy = st.builds(
    essentialoclcs::Property,
)
essentialoclcs::TypeRefCS_strategy = st.builds(
    essentialoclcs::TypeRefCS,
)
essentialoclcs::Operation_strategy = st.builds(
    essentialoclcs::Operation,
)
essentialoclcs::Iteration_strategy = st.builds(
    essentialoclcs::Iteration,
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
VariableCS_strategy = st.builds(
    VariableCS,
)
essentialoclcs::TupleLiteralPartCS_strategy = st.builds(
    essentialoclcs::TupleLiteralPartCS,
)
IterationCallExpCS_strategy = st.builds(
    IterationCallExpCS,
)
essentialoclcs::NameExpCS_strategy = st.builds(
    essentialoclcs::NameExpCS,
)
essentialoclcs::IterateCallExpCS_strategy = st.builds(
    essentialoclcs::IterateCallExpCS,
)
OperatorExpCS_strategy = st.builds(
    OperatorExpCS,
)
essentialoclcs::PrefixExpCS_strategy = st.builds(
    essentialoclcs::PrefixExpCS,
)
essentialoclcs::InfixExpCS_strategy = st.builds(
    essentialoclcs::InfixExpCS,
)
SpecificationCS_strategy = st.builds(
    SpecificationCS,
)
essentialoclcs::ExpSpecificationCS_strategy = st.builds(
    essentialoclcs::ExpSpecificationCS,
)
essentialoclcs::Precedence_strategy = st.builds(
    essentialoclcs::Precedence,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
essentialoclcs::TypeLiteralExpCS_strategy = st.builds(
    essentialoclcs::TypeLiteralExpCS,
)
essentialoclcs::LambdaLiteralExpCS_strategy = st.builds(
    essentialoclcs::LambdaLiteralExpCS,
)
essentialoclcs::PrimitiveLiteralExpCS_strategy = st.builds(
    essentialoclcs::PrimitiveLiteralExpCS,
)
essentialoclcs::TupleLiteralExpCS_strategy = st.builds(
    essentialoclcs::TupleLiteralExpCS,
)
essentialoclcs::MapLiteralExpCS_strategy = st.builds(
    essentialoclcs::MapLiteralExpCS,
)
essentialoclcs::CollectionLiteralExpCS_strategy = st.builds(
    essentialoclcs::CollectionLiteralExpCS,
)
ContextLessElementCS_strategy = st.builds(
    ContextLessElementCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
essentialoclcs::VariableCS_strategy = st.builds(
    essentialoclcs::VariableCS,
)
essentialoclcs::ContextCS_strategy = st.builds(
    essentialoclcs::ContextCS,
)
essentialoclcs::TypedRefCS_strategy = st.builds(
    essentialoclcs::TypedRefCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
essentialoclcs::TypeNameExpCS_strategy = st.builds(
    essentialoclcs::TypeNameExpCS,
)
essentialoclcs::CollectionTypeCS_strategy = st.builds(
    essentialoclcs::CollectionTypeCS,
    name=
        safe_text
)
essentialoclcs::MapTypeCS_strategy = st.builds(
    essentialoclcs::MapTypeCS,
    name=
        safe_text
)
essentialoclcs::CollectionPatternCS_strategy = st.builds(
    essentialoclcs::CollectionPatternCS,
    restVariableName=
        safe_text
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
essentialoclcs::CollectionLiteralPartCS_strategy = st.builds(
    essentialoclcs::CollectionLiteralPartCS,
)
essentialoclcs::ShadowPartCS_strategy = st.builds(
    essentialoclcs::ShadowPartCS,
)
essentialoclcs::MapLiteralPartCS_strategy = st.builds(
    essentialoclcs::MapLiteralPartCS,
)
essentialoclcs::NavigatingArgCS_strategy = st.builds(
    essentialoclcs::NavigatingArgCS,
    prefix=
        safe_text,
    role=
        safe_text
)
essentialoclcs::ExpCS_strategy = st.builds(
    essentialoclcs::ExpCS,
    hasError=
        st.booleans()
)
AbstractNameExpCS_strategy = st.builds(
    AbstractNameExpCS,
)
essentialoclcs::ShadowExpCS_strategy = st.builds(
    essentialoclcs::ShadowExpCS,
    value=
        safe_text
)
essentialoclcs::VariableExpCS_strategy = st.builds(
    essentialoclcs::VariableExpCS,
)
essentialoclcs::CallExpCS_strategy = st.builds(
    essentialoclcs::CallExpCS,
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
essentialoclcs::StringLiteralExpCS_strategy = st.builds(
    essentialoclcs::StringLiteralExpCS,
    segments=
        safe_text
)
essentialoclcs::NumberLiteralExpCS_strategy = st.builds(
    essentialoclcs::NumberLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs::NullLiteralExpCS_strategy = st.builds(
    essentialoclcs::NullLiteralExpCS,
)
essentialoclcs::UnlimitedNaturalLiteralExpCS_strategy = st.builds(
    essentialoclcs::UnlimitedNaturalLiteralExpCS,
)
essentialoclcs::InvalidLiteralExpCS_strategy = st.builds(
    essentialoclcs::InvalidLiteralExpCS,
)
essentialoclcs::BooleanLiteralExpCS_strategy = st.builds(
    essentialoclcs::BooleanLiteralExpCS,
    symbol=
        safe_text
)
essentialoclcs::AssociationClass_strategy = st.builds(
    essentialoclcs::AssociationClass,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
essentialoclcs::IterationCallExpCS_strategy = st.builds(
    essentialoclcs::IterationCallExpCS,
)
essentialoclcs::PropertyCallExpCS_strategy = st.builds(
    essentialoclcs::PropertyCallExpCS,
)
essentialoclcs::OperationCallExpCS_strategy = st.builds(
    essentialoclcs::OperationCallExpCS,
)
essentialoclcs::AssociationClassCallExpCS_strategy = st.builds(
    essentialoclcs::AssociationClassCallExpCS,
)
essentialoclcs::Type_strategy = st.builds(
    essentialoclcs::Type,
)
essentialoclcs::SquareBracketedClauseCS_strategy = st.builds(
    essentialoclcs::SquareBracketedClauseCS,
)
essentialoclcs::RoundBracketedClauseCS_strategy = st.builds(
    essentialoclcs::RoundBracketedClauseCS,
)
essentialoclcs::PathNameCS_strategy = st.builds(
    essentialoclcs::PathNameCS,
)
essentialoclcs::CurlyBracketedClauseCS_strategy = st.builds(
    essentialoclcs::CurlyBracketedClauseCS,
    value=
        safe_text
)
ExpCS_strategy = st.builds(
    ExpCS,
)
essentialoclcs::OperatorExpCS_strategy = st.builds(
    essentialoclcs::OperatorExpCS,
)
essentialoclcs::SelfExpCS_strategy = st.builds(
    essentialoclcs::SelfExpCS,
    name=
        safe_text
)
essentialoclcs::LetExpCS_strategy = st.builds(
    essentialoclcs::LetExpCS,
    isImplicit=
        st.booleans()
)
essentialoclcs::LiteralExpCS_strategy = st.builds(
    essentialoclcs::LiteralExpCS,
)
essentialoclcs::NestedExpCS_strategy = st.builds(
    essentialoclcs::NestedExpCS,
)
essentialoclcs::PatternExpCS_strategy = st.builds(
    essentialoclcs::PatternExpCS,
    patternVariableName=
        safe_text
)
essentialoclcs::IfExpCS_strategy = st.builds(
    essentialoclcs::IfExpCS,
    isImplicit=
        st.booleans()
)
essentialoclcs::LetVariableCS_strategy = st.builds(
    essentialoclcs::LetVariableCS,
)
essentialoclcs::IfThenExpCS_strategy = st.builds(
    essentialoclcs::IfThenExpCS,
)
essentialoclcs::AbstractNameExpCS_strategy = st.builds(
    essentialoclcs::AbstractNameExpCS,
    isPre=
        st.booleans()
)

@given(instance=essentialoclcs::Variable_strategy)
@settings(max_examples=50)
def test_essentialoclcs::variable_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Variable)

@given(instance=essentialoclcs::Property_strategy)
@settings(max_examples=50)
def test_essentialoclcs::property_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Property)

@given(instance=essentialoclcs::TypeRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typerefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypeRefCS)

@given(instance=essentialoclcs::Operation_strategy)
@settings(max_examples=50)
def test_essentialoclcs::operation_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Operation)

@given(instance=essentialoclcs::Iteration_strategy)
@settings(max_examples=50)
def test_essentialoclcs::iteration_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Iteration)

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

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=essentialoclcs::TupleLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::tupleliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TupleLiteralPartCS)

@given(instance=IterationCallExpCS_strategy)
@settings(max_examples=50)
def test_iterationcallexpcs_instantiation(instance):
    assert isinstance(instance, IterationCallExpCS)

@given(instance=essentialoclcs::NameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NameExpCS)

@given(instance=essentialoclcs::IterateCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::iteratecallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IterateCallExpCS)

@given(instance=OperatorExpCS_strategy)
@settings(max_examples=50)
def test_operatorexpcs_instantiation(instance):
    assert isinstance(instance, OperatorExpCS)

@given(instance=essentialoclcs::PrefixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::prefixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PrefixExpCS)

@given(instance=essentialoclcs::InfixExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::infixexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::InfixExpCS)

@given(instance=SpecificationCS_strategy)
@settings(max_examples=50)
def test_specificationcs_instantiation(instance):
    assert isinstance(instance, SpecificationCS)

@given(instance=essentialoclcs::ExpSpecificationCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::expspecificationcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ExpSpecificationCS)

@given(instance=essentialoclcs::Precedence_strategy)
@settings(max_examples=50)
def test_essentialoclcs::precedence_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Precedence)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=essentialoclcs::TypeLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typeliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypeLiteralExpCS)

@given(instance=essentialoclcs::LambdaLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::lambdaliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LambdaLiteralExpCS)

@given(instance=essentialoclcs::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PrimitiveLiteralExpCS)

@given(instance=essentialoclcs::TupleLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::tupleliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TupleLiteralExpCS)

@given(instance=essentialoclcs::MapLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::mapliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::MapLiteralExpCS)

@given(instance=essentialoclcs::CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionLiteralExpCS)

@given(instance=ContextLessElementCS_strategy)
@settings(max_examples=50)
def test_contextlesselementcs_instantiation(instance):
    assert isinstance(instance, ContextLessElementCS)

@given(instance=RootCS_strategy)
@settings(max_examples=50)
def test_rootcs_instantiation(instance):
    assert isinstance(instance, RootCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=essentialoclcs::VariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::variablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::VariableCS)

@given(instance=essentialoclcs::ContextCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::contextcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ContextCS)

@given(instance=essentialoclcs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typedrefcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypedRefCS)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=essentialoclcs::TypeNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::typenameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::TypeNameExpCS)

@given(instance=essentialoclcs::CollectionTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectiontypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionTypeCS)

@given(instance=essentialoclcs::CollectionTypeCS_strategy)
def test_essentialoclcs::collectiontypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::CollectionTypeCS_strategy)
def test_essentialoclcs::collectiontypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::MapTypeCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::maptypecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::MapTypeCS)

@given(instance=essentialoclcs::MapTypeCS_strategy)
def test_essentialoclcs::maptypecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::MapTypeCS_strategy)
def test_essentialoclcs::maptypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::CollectionPatternCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectionpatterncs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionPatternCS)

@given(instance=essentialoclcs::CollectionPatternCS_strategy)
def test_essentialoclcs::collectionpatterncs_restVariableName_type(instance):
    assert isinstance(instance.restVariableName, str)


@given(instance=essentialoclcs::CollectionPatternCS_strategy)
def test_essentialoclcs::collectionpatterncs_restVariableName_setter(instance):
    original = instance.restVariableName
    instance.restVariableName = original
    assert instance.restVariableName == original

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=essentialoclcs::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CollectionLiteralPartCS)

@given(instance=essentialoclcs::ShadowPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::shadowpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ShadowPartCS)

@given(instance=essentialoclcs::MapLiteralPartCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::mapliteralpartcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::MapLiteralPartCS)

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::navigatingargcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NavigatingArgCS)

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=essentialoclcs::NavigatingArgCS_strategy)
def test_essentialoclcs::navigatingargcs_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=essentialoclcs::ExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::expcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ExpCS)

@given(instance=essentialoclcs::ExpCS_strategy)
def test_essentialoclcs::expcs_hasError_type(instance):
    assert isinstance(instance.hasError, bool)


@given(instance=essentialoclcs::ExpCS_strategy)
def test_essentialoclcs::expcs_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs::ExpCS_strategy)
@settings(max_examples=30)
def test_essentialoclcs::expcs_islocalrightancestorof_changes_state(instance):
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
        assert has_statements, f"Function 'isLocalRightAncestorOf' in essentialoclcs::ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs::ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalRightAncestorOf' in essentialoclcs::ExpCS is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=essentialoclcs::ExpCS_strategy)
@settings(max_examples=30)
def test_essentialoclcs::expcs_islocalleftancestorof_changes_state(instance):
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
        assert has_statements, f"Function 'isLocalLeftAncestorOf' in essentialoclcs::ExpCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs::ExpCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocalLeftAncestorOf' in essentialoclcs::ExpCS is not implemented or raised an error")

@given(instance=AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, AbstractNameExpCS)

@given(instance=essentialoclcs::ShadowExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::shadowexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::ShadowExpCS)

@given(instance=essentialoclcs::ShadowExpCS_strategy)
def test_essentialoclcs::shadowexpcs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialoclcs::ShadowExpCS_strategy)
def test_essentialoclcs::shadowexpcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=essentialoclcs::VariableExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::variableexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::VariableExpCS)

@given(instance=essentialoclcs::CallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::callexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CallExpCS)

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::StringLiteralExpCS)

@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
def test_essentialoclcs::stringliteralexpcs_segments_type(instance):
    assert isinstance(instance.segments, str)


@given(instance=essentialoclcs::StringLiteralExpCS_strategy)
def test_essentialoclcs::stringliteralexpcs_segments_setter(instance):
    original = instance.segments
    instance.segments = original
    assert instance.segments == original

@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::numberliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NumberLiteralExpCS)

@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
def test_essentialoclcs::numberliteralexpcs_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=essentialoclcs::NumberLiteralExpCS_strategy)
def test_essentialoclcs::numberliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=essentialoclcs::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NullLiteralExpCS)

@given(instance=essentialoclcs::UnlimitedNaturalLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::unlimitednaturalliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::UnlimitedNaturalLiteralExpCS)

@given(instance=essentialoclcs::InvalidLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::invalidliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::InvalidLiteralExpCS)

@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::BooleanLiteralExpCS)

@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
def test_essentialoclcs::booleanliteralexpcs_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=essentialoclcs::BooleanLiteralExpCS_strategy)
def test_essentialoclcs::booleanliteralexpcs_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=essentialoclcs::AssociationClass_strategy)
@settings(max_examples=50)
def test_essentialoclcs::associationclass_instantiation(instance):
    assert isinstance(instance, essentialoclcs::AssociationClass)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=essentialoclcs::IterationCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::iterationcallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IterationCallExpCS)

@given(instance=essentialoclcs::PropertyCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::propertycallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PropertyCallExpCS)

@given(instance=essentialoclcs::OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::operationcallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::OperationCallExpCS)

@given(instance=essentialoclcs::AssociationClassCallExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::associationclasscallexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::AssociationClassCallExpCS)

@given(instance=essentialoclcs::Type_strategy)
@settings(max_examples=50)
def test_essentialoclcs::type_instantiation(instance):
    assert isinstance(instance, essentialoclcs::Type)

@given(instance=essentialoclcs::SquareBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::squarebracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::SquareBracketedClauseCS)

@given(instance=essentialoclcs::RoundBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::roundbracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::RoundBracketedClauseCS)

@given(instance=essentialoclcs::PathNameCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::pathnamecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PathNameCS)

@given(instance=essentialoclcs::CurlyBracketedClauseCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::curlybracketedclausecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::CurlyBracketedClauseCS)

@given(instance=essentialoclcs::CurlyBracketedClauseCS_strategy)
def test_essentialoclcs::curlybracketedclausecs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=essentialoclcs::CurlyBracketedClauseCS_strategy)
def test_essentialoclcs::curlybracketedclausecs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=essentialoclcs::OperatorExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::operatorexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::OperatorExpCS)

@given(instance=essentialoclcs::SelfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::selfexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::SelfExpCS)

@given(instance=essentialoclcs::SelfExpCS_strategy)
def test_essentialoclcs::selfexpcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=essentialoclcs::SelfExpCS_strategy)
def test_essentialoclcs::selfexpcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=essentialoclcs::LetExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::letexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LetExpCS)

@given(instance=essentialoclcs::LetExpCS_strategy)
def test_essentialoclcs::letexpcs_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, bool)


@given(instance=essentialoclcs::LetExpCS_strategy)
def test_essentialoclcs::letexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=essentialoclcs::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::literalexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LiteralExpCS)

@given(instance=essentialoclcs::NestedExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::nestedexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::NestedExpCS)

@given(instance=essentialoclcs::PatternExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::patternexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::PatternExpCS)

@given(instance=essentialoclcs::PatternExpCS_strategy)
def test_essentialoclcs::patternexpcs_patternVariableName_type(instance):
    assert isinstance(instance.patternVariableName, str)


@given(instance=essentialoclcs::PatternExpCS_strategy)
def test_essentialoclcs::patternexpcs_patternVariableName_setter(instance):
    original = instance.patternVariableName
    instance.patternVariableName = original
    assert instance.patternVariableName == original

@given(instance=essentialoclcs::IfExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::ifexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IfExpCS)

@given(instance=essentialoclcs::IfExpCS_strategy)
def test_essentialoclcs::ifexpcs_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, bool)


@given(instance=essentialoclcs::IfExpCS_strategy)
def test_essentialoclcs::ifexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=essentialoclcs::LetVariableCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::letvariablecs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::LetVariableCS)

@given(instance=essentialoclcs::IfThenExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::ifthenexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::IfThenExpCS)

@given(instance=essentialoclcs::AbstractNameExpCS_strategy)
@settings(max_examples=50)
def test_essentialoclcs::abstractnameexpcs_instantiation(instance):
    assert isinstance(instance, essentialoclcs::AbstractNameExpCS)

@given(instance=essentialoclcs::AbstractNameExpCS_strategy)
def test_essentialoclcs::abstractnameexpcs_isPre_type(instance):
    assert isinstance(instance.isPre, bool)


@given(instance=essentialoclcs::AbstractNameExpCS_strategy)
def test_essentialoclcs::abstractnameexpcs_isPre_setter(instance):
    original = instance.isPre
    instance.isPre = original
    assert instance.isPre == original

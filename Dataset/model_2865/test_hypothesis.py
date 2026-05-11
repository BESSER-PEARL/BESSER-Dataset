import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleOptionLiteral,
    deviceModelingLanguage::SimpleSomeLiteral,
    deviceModelingLanguage::SimpleNoneLiteral,
    Exp,
    deviceModelingLanguage::PrimaryExp,
    deviceModelingLanguage::UnaryExp,
    deviceModelingLanguage::BinaryExp,
    OptionLiteral,
    deviceModelingLanguage::SomeLiteral,
    deviceModelingLanguage::NoneLiteral,
    BaseType,
    deviceModelingLanguage::NoneType,
    deviceModelingLanguage::SomeType,
    deviceModelingLanguage::OptionType,
    deviceModelingLanguage::TupleType,
    Primary,
    deviceModelingLanguage::LiteralExp,
    deviceModelingLanguage::NameExp,
    deviceModelingLanguage::AccessExp,
    Modifier,
    MModifier,
    deviceModelingLanguage::Const,
    ConstraintNat,
    deviceModelingLanguage::AnyNatConstraint,
    deviceModelingLanguage::NumNatConstraint,
    deviceModelingLanguage::Override,
    deviceModelingLanguage::Var,
    deviceModelingLanguage::Val,
    Type,
    deviceModelingLanguage::SetType,
    deviceModelingLanguage::SeqType,
    deviceModelingLanguage::BaseType,
    deviceModelingLanguage::Primary,
    deviceModelingLanguage::Accessor,
    SimpleLiteral,
    deviceModelingLanguage::SimpleSeqLiteral,
    deviceModelingLanguage::SimpleTupleLiteral,
    deviceModelingLanguage::SimpleSetLiteral,
    deviceModelingLanguage::SimpleOptionLiteral,
    deviceModelingLanguage::SimpleBasicLiteral,
    deviceModelingLanguage::SimpleLiteral,
    Literal,
    deviceModelingLanguage::SetLiteral,
    deviceModelingLanguage::BasicLiteral,
    deviceModelingLanguage::TupleLiteral,
    deviceModelingLanguage::OptionLiteral,
    deviceModelingLanguage::SeqLiteral,
    deviceModelingLanguage::Report,
    deviceModelingLanguage::FeatureType,
    deviceModelingLanguage::MModifier,
    deviceModelingLanguage::ReportMemberDecl,
    deviceModelingLanguage::Param,
    deviceModelingLanguage::ConstraintExp,
    FeatureDecl,
    deviceModelingLanguage::Feature,
    deviceModelingLanguage::Data,
    deviceModelingLanguage::App,
    deviceModelingLanguage::SubMemberMatch,
    deviceModelingLanguage::ConstraintNat,
    InvariantDecl,
    deviceModelingLanguage::GeneralInvariant,
    deviceModelingLanguage::MultiplicityInvariant,
    FeatureType,
    deviceModelingLanguage::SeqFeatureType,
    deviceModelingLanguage::SomeFeatureType,
    deviceModelingLanguage::OptionFeatureType,
    deviceModelingLanguage::SetFeatureType,
    deviceModelingLanguage::EitherFeatureType,
    deviceModelingLanguage::BaseFeatureType,
    deviceModelingLanguage::Model,
    deviceModelingLanguage::Literal,
    deviceModelingLanguage::Type,
    deviceModelingLanguage::Modifier,
    Accessor,
    MemberDecl,
    deviceModelingLanguage::SubMemberDecl,
    deviceModelingLanguage::InvariantDecl,
    deviceModelingLanguage::AttrDecl,
    deviceModelingLanguage::Exp,
    deviceModelingLanguage::Assignment,
    deviceModelingLanguage::Device,
    deviceModelingLanguage::MemberDecl,
    Decl,
    deviceModelingLanguage::FeatureDecl,
    deviceModelingLanguage::TypeDecl,
    deviceModelingLanguage::Decl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleoptionliteral_is_not_abstract():
    assert not inspect.isabstract(SimpleOptionLiteral)


def test_simpleoptionliteral_constructor_exists():
    assert callable(SimpleOptionLiteral.__init__)


def test_simpleoptionliteral_constructor_args():
    sig = inspect.signature(SimpleOptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simplesomeliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleSomeLiteral)


def test_devicemodelinglanguage::simplesomeliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleSomeLiteral.__init__)


def test_devicemodelinglanguage::simplesomeliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleSomeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simplenoneliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleNoneLiteral)


def test_devicemodelinglanguage::simplenoneliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleNoneLiteral.__init__)


def test_devicemodelinglanguage::simplenoneliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleNoneLiteral.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::primaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::PrimaryExp)


def test_devicemodelinglanguage::primaryexp_constructor_exists():
    assert callable(deviceModelingLanguage::PrimaryExp.__init__)


def test_devicemodelinglanguage::primaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::PrimaryExp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::unaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::UnaryExp)


def test_devicemodelinglanguage::unaryexp_constructor_exists():
    assert callable(deviceModelingLanguage::UnaryExp.__init__)


def test_devicemodelinglanguage::unaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::UnaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_devicemodelinglanguage::unaryexp_has_op():
    assert hasattr(deviceModelingLanguage::UnaryExp, "op")
    descriptor = None
    for klass in deviceModelingLanguage::UnaryExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::binaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::BinaryExp)


def test_devicemodelinglanguage::binaryexp_constructor_exists():
    assert callable(deviceModelingLanguage::BinaryExp.__init__)


def test_devicemodelinglanguage::binaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_devicemodelinglanguage::binaryexp_has_op():
    assert hasattr(deviceModelingLanguage::BinaryExp, "op")
    descriptor = None
    for klass in deviceModelingLanguage::BinaryExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_optionliteral_is_not_abstract():
    assert not inspect.isabstract(OptionLiteral)


def test_optionliteral_constructor_exists():
    assert callable(OptionLiteral.__init__)


def test_optionliteral_constructor_args():
    sig = inspect.signature(OptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::someliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SomeLiteral)


def test_devicemodelinglanguage::someliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SomeLiteral.__init__)


def test_devicemodelinglanguage::someliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SomeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::noneliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::NoneLiteral)


def test_devicemodelinglanguage::noneliteral_constructor_exists():
    assert callable(deviceModelingLanguage::NoneLiteral.__init__)


def test_devicemodelinglanguage::noneliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::NoneLiteral.__init__)
    params = list(sig.parameters.keys())



def test_basetype_is_not_abstract():
    assert not inspect.isabstract(BaseType)


def test_basetype_constructor_exists():
    assert callable(BaseType.__init__)


def test_basetype_constructor_args():
    sig = inspect.signature(BaseType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::nonetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::NoneType)


def test_devicemodelinglanguage::nonetype_constructor_exists():
    assert callable(deviceModelingLanguage::NoneType.__init__)


def test_devicemodelinglanguage::nonetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::NoneType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::sometype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SomeType)


def test_devicemodelinglanguage::sometype_constructor_exists():
    assert callable(deviceModelingLanguage::SomeType.__init__)


def test_devicemodelinglanguage::sometype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SomeType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::optiontype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::OptionType)


def test_devicemodelinglanguage::optiontype_constructor_exists():
    assert callable(deviceModelingLanguage::OptionType.__init__)


def test_devicemodelinglanguage::optiontype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::OptionType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::tupletype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::TupleType)


def test_devicemodelinglanguage::tupletype_constructor_exists():
    assert callable(deviceModelingLanguage::TupleType.__init__)


def test_devicemodelinglanguage::tupletype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::literalexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::LiteralExp)


def test_devicemodelinglanguage::literalexp_constructor_exists():
    assert callable(deviceModelingLanguage::LiteralExp.__init__)


def test_devicemodelinglanguage::literalexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::nameexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::NameExp)


def test_devicemodelinglanguage::nameexp_constructor_exists():
    assert callable(deviceModelingLanguage::NameExp.__init__)


def test_devicemodelinglanguage::nameexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::NameExp.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_devicemodelinglanguage::nameexp_has_id():
    assert hasattr(deviceModelingLanguage::NameExp, "id")
    descriptor = None
    for klass in deviceModelingLanguage::NameExp.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::accessexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::AccessExp)


def test_devicemodelinglanguage::accessexp_constructor_exists():
    assert callable(deviceModelingLanguage::AccessExp.__init__)


def test_devicemodelinglanguage::accessexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::AccessExp.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_mmodifier_is_not_abstract():
    assert not inspect.isabstract(MModifier)


def test_mmodifier_constructor_exists():
    assert callable(MModifier.__init__)


def test_mmodifier_constructor_args():
    sig = inspect.signature(MModifier.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::const_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Const)


def test_devicemodelinglanguage::const_constructor_exists():
    assert callable(deviceModelingLanguage::Const.__init__)


def test_devicemodelinglanguage::const_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Const.__init__)
    params = list(sig.parameters.keys())
    assert "product" in params, "Missing parameter 'product'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_devicemodelinglanguage::const_has_product():
    assert hasattr(deviceModelingLanguage::Const, "product")
    descriptor = None
    for klass in deviceModelingLanguage::Const.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::const_has_instance():
    assert hasattr(deviceModelingLanguage::Const, "instance")
    descriptor = None
    for klass in deviceModelingLanguage::Const.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::const_has_schema():
    assert hasattr(deviceModelingLanguage::Const, "schema")
    descriptor = None
    for klass in deviceModelingLanguage::Const.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::const_has_class_():
    assert hasattr(deviceModelingLanguage::Const, "class_")
    descriptor = None
    for klass in deviceModelingLanguage::Const.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_constraintnat_is_not_abstract():
    assert not inspect.isabstract(ConstraintNat)


def test_constraintnat_constructor_exists():
    assert callable(ConstraintNat.__init__)


def test_constraintnat_constructor_args():
    sig = inspect.signature(ConstraintNat.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::anynatconstraint_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::AnyNatConstraint)


def test_devicemodelinglanguage::anynatconstraint_constructor_exists():
    assert callable(deviceModelingLanguage::AnyNatConstraint.__init__)


def test_devicemodelinglanguage::anynatconstraint_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::AnyNatConstraint.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::numnatconstraint_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::NumNatConstraint)


def test_devicemodelinglanguage::numnatconstraint_constructor_exists():
    assert callable(deviceModelingLanguage::NumNatConstraint.__init__)


def test_devicemodelinglanguage::numnatconstraint_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::NumNatConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"

def test_devicemodelinglanguage::numnatconstraint_has_num():
    assert hasattr(deviceModelingLanguage::NumNatConstraint, "num")
    descriptor = None
    for klass in deviceModelingLanguage::NumNatConstraint.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::override_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Override)


def test_devicemodelinglanguage::override_constructor_exists():
    assert callable(deviceModelingLanguage::Override.__init__)


def test_devicemodelinglanguage::override_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Override.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::var_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Var)


def test_devicemodelinglanguage::var_constructor_exists():
    assert callable(deviceModelingLanguage::Var.__init__)


def test_devicemodelinglanguage::var_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Var.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::val_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Val)


def test_devicemodelinglanguage::val_constructor_exists():
    assert callable(deviceModelingLanguage::Val.__init__)


def test_devicemodelinglanguage::val_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Val.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::settype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SetType)


def test_devicemodelinglanguage::settype_constructor_exists():
    assert callable(deviceModelingLanguage::SetType.__init__)


def test_devicemodelinglanguage::settype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SetType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::seqtype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SeqType)


def test_devicemodelinglanguage::seqtype_constructor_exists():
    assert callable(deviceModelingLanguage::SeqType.__init__)


def test_devicemodelinglanguage::seqtype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SeqType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::basetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::BaseType)


def test_devicemodelinglanguage::basetype_constructor_exists():
    assert callable(deviceModelingLanguage::BaseType.__init__)


def test_devicemodelinglanguage::basetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::BaseType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::primary_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Primary)


def test_devicemodelinglanguage::primary_constructor_exists():
    assert callable(deviceModelingLanguage::Primary.__init__)


def test_devicemodelinglanguage::primary_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Primary.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::accessor_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Accessor)


def test_devicemodelinglanguage::accessor_constructor_exists():
    assert callable(deviceModelingLanguage::Accessor.__init__)


def test_devicemodelinglanguage::accessor_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Accessor.__init__)
    params = list(sig.parameters.keys())



def test_simpleliteral_is_not_abstract():
    assert not inspect.isabstract(SimpleLiteral)


def test_simpleliteral_constructor_exists():
    assert callable(SimpleLiteral.__init__)


def test_simpleliteral_constructor_args():
    sig = inspect.signature(SimpleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simpleseqliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleSeqLiteral)


def test_devicemodelinglanguage::simpleseqliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleSeqLiteral.__init__)


def test_devicemodelinglanguage::simpleseqliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleSeqLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simpletupleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleTupleLiteral)


def test_devicemodelinglanguage::simpletupleliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleTupleLiteral.__init__)


def test_devicemodelinglanguage::simpletupleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleTupleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simplesetliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleSetLiteral)


def test_devicemodelinglanguage::simplesetliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleSetLiteral.__init__)


def test_devicemodelinglanguage::simplesetliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleSetLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simpleoptionliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleOptionLiteral)


def test_devicemodelinglanguage::simpleoptionliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleOptionLiteral.__init__)


def test_devicemodelinglanguage::simpleoptionliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleOptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::simplebasicliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleBasicLiteral)


def test_devicemodelinglanguage::simplebasicliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleBasicLiteral.__init__)


def test_devicemodelinglanguage::simplebasicliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleBasicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "lit" in params, "Missing parameter 'lit'"

def test_devicemodelinglanguage::simplebasicliteral_has_lit():
    assert hasattr(deviceModelingLanguage::SimpleBasicLiteral, "lit")
    descriptor = None
    for klass in deviceModelingLanguage::SimpleBasicLiteral.__mro__:
        if "lit" in klass.__dict__:
            descriptor = klass.__dict__["lit"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::simpleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SimpleLiteral)


def test_devicemodelinglanguage::simpleliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SimpleLiteral.__init__)


def test_devicemodelinglanguage::simpleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SimpleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::setliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SetLiteral)


def test_devicemodelinglanguage::setliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SetLiteral.__init__)


def test_devicemodelinglanguage::setliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SetLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::basicliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::BasicLiteral)


def test_devicemodelinglanguage::basicliteral_constructor_exists():
    assert callable(deviceModelingLanguage::BasicLiteral.__init__)


def test_devicemodelinglanguage::basicliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::BasicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "lit" in params, "Missing parameter 'lit'"

def test_devicemodelinglanguage::basicliteral_has_lit():
    assert hasattr(deviceModelingLanguage::BasicLiteral, "lit")
    descriptor = None
    for klass in deviceModelingLanguage::BasicLiteral.__mro__:
        if "lit" in klass.__dict__:
            descriptor = klass.__dict__["lit"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::tupleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::TupleLiteral)


def test_devicemodelinglanguage::tupleliteral_constructor_exists():
    assert callable(deviceModelingLanguage::TupleLiteral.__init__)


def test_devicemodelinglanguage::tupleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::TupleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::optionliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::OptionLiteral)


def test_devicemodelinglanguage::optionliteral_constructor_exists():
    assert callable(deviceModelingLanguage::OptionLiteral.__init__)


def test_devicemodelinglanguage::optionliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::OptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::seqliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SeqLiteral)


def test_devicemodelinglanguage::seqliteral_constructor_exists():
    assert callable(deviceModelingLanguage::SeqLiteral.__init__)


def test_devicemodelinglanguage::seqliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SeqLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::report_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Report)


def test_devicemodelinglanguage::report_constructor_exists():
    assert callable(deviceModelingLanguage::Report.__init__)


def test_devicemodelinglanguage::report_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Report.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::report_has_name():
    assert hasattr(deviceModelingLanguage::Report, "name")
    descriptor = None
    for klass in deviceModelingLanguage::Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::featuretype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::FeatureType)


def test_devicemodelinglanguage::featuretype_constructor_exists():
    assert callable(deviceModelingLanguage::FeatureType.__init__)


def test_devicemodelinglanguage::featuretype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::mmodifier_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::MModifier)


def test_devicemodelinglanguage::mmodifier_constructor_exists():
    assert callable(deviceModelingLanguage::MModifier.__init__)


def test_devicemodelinglanguage::mmodifier_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::MModifier.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::reportmemberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::ReportMemberDecl)


def test_devicemodelinglanguage::reportmemberdecl_constructor_exists():
    assert callable(deviceModelingLanguage::ReportMemberDecl.__init__)


def test_devicemodelinglanguage::reportmemberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::ReportMemberDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::reportmemberdecl_has_name():
    assert hasattr(deviceModelingLanguage::ReportMemberDecl, "name")
    descriptor = None
    for klass in deviceModelingLanguage::ReportMemberDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::param_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Param)


def test_devicemodelinglanguage::param_constructor_exists():
    assert callable(deviceModelingLanguage::Param.__init__)


def test_devicemodelinglanguage::param_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::param_has_name():
    assert hasattr(deviceModelingLanguage::Param, "name")
    descriptor = None
    for klass in deviceModelingLanguage::Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::constraintexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::ConstraintExp)


def test_devicemodelinglanguage::constraintexp_constructor_exists():
    assert callable(deviceModelingLanguage::ConstraintExp.__init__)


def test_devicemodelinglanguage::constraintexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::ConstraintExp.__init__)
    params = list(sig.parameters.keys())



def test_featuredecl_is_not_abstract():
    assert not inspect.isabstract(FeatureDecl)


def test_featuredecl_constructor_exists():
    assert callable(FeatureDecl.__init__)


def test_featuredecl_constructor_args():
    sig = inspect.signature(FeatureDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::feature_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Feature)


def test_devicemodelinglanguage::feature_constructor_exists():
    assert callable(deviceModelingLanguage::Feature.__init__)


def test_devicemodelinglanguage::feature_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "product" in params, "Missing parameter 'product'"

def test_devicemodelinglanguage::feature_has_class_():
    assert hasattr(deviceModelingLanguage::Feature, "class_")
    descriptor = None
    for klass in deviceModelingLanguage::Feature.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::feature_has_schema():
    assert hasattr(deviceModelingLanguage::Feature, "schema")
    descriptor = None
    for klass in deviceModelingLanguage::Feature.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::feature_has_product():
    assert hasattr(deviceModelingLanguage::Feature, "product")
    descriptor = None
    for klass in deviceModelingLanguage::Feature.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::data_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Data)


def test_devicemodelinglanguage::data_constructor_exists():
    assert callable(deviceModelingLanguage::Data.__init__)


def test_devicemodelinglanguage::data_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Data.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::app_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::App)


def test_devicemodelinglanguage::app_constructor_exists():
    assert callable(deviceModelingLanguage::App.__init__)


def test_devicemodelinglanguage::app_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::App.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::submembermatch_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SubMemberMatch)


def test_devicemodelinglanguage::submembermatch_constructor_exists():
    assert callable(deviceModelingLanguage::SubMemberMatch.__init__)


def test_devicemodelinglanguage::submembermatch_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SubMemberMatch.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"
    assert "qNames" in params, "Missing parameter 'qNames'"

def test_devicemodelinglanguage::submembermatch_has_any():
    assert hasattr(deviceModelingLanguage::SubMemberMatch, "any")
    descriptor = None
    for klass in deviceModelingLanguage::SubMemberMatch.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::submembermatch_has_name():
    assert hasattr(deviceModelingLanguage::SubMemberMatch, "name")
    descriptor = None
    for klass in deviceModelingLanguage::SubMemberMatch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::submembermatch_has_qNames():
    assert hasattr(deviceModelingLanguage::SubMemberMatch, "qNames")
    descriptor = None
    for klass in deviceModelingLanguage::SubMemberMatch.__mro__:
        if "qNames" in klass.__dict__:
            descriptor = klass.__dict__["qNames"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::constraintnat_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::ConstraintNat)


def test_devicemodelinglanguage::constraintnat_constructor_exists():
    assert callable(deviceModelingLanguage::ConstraintNat.__init__)


def test_devicemodelinglanguage::constraintnat_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::ConstraintNat.__init__)
    params = list(sig.parameters.keys())



def test_invariantdecl_is_not_abstract():
    assert not inspect.isabstract(InvariantDecl)


def test_invariantdecl_constructor_exists():
    assert callable(InvariantDecl.__init__)


def test_invariantdecl_constructor_args():
    sig = inspect.signature(InvariantDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::generalinvariant_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::GeneralInvariant)


def test_devicemodelinglanguage::generalinvariant_constructor_exists():
    assert callable(deviceModelingLanguage::GeneralInvariant.__init__)


def test_devicemodelinglanguage::generalinvariant_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::GeneralInvariant.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::multiplicityinvariant_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::MultiplicityInvariant)


def test_devicemodelinglanguage::multiplicityinvariant_constructor_exists():
    assert callable(deviceModelingLanguage::MultiplicityInvariant.__init__)


def test_devicemodelinglanguage::multiplicityinvariant_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::MultiplicityInvariant.__init__)
    params = list(sig.parameters.keys())



def test_featuretype_is_not_abstract():
    assert not inspect.isabstract(FeatureType)


def test_featuretype_constructor_exists():
    assert callable(FeatureType.__init__)


def test_featuretype_constructor_args():
    sig = inspect.signature(FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::seqfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SeqFeatureType)


def test_devicemodelinglanguage::seqfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::SeqFeatureType.__init__)


def test_devicemodelinglanguage::seqfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SeqFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::somefeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SomeFeatureType)


def test_devicemodelinglanguage::somefeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::SomeFeatureType.__init__)


def test_devicemodelinglanguage::somefeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SomeFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::optionfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::OptionFeatureType)


def test_devicemodelinglanguage::optionfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::OptionFeatureType.__init__)


def test_devicemodelinglanguage::optionfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::OptionFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"

def test_devicemodelinglanguage::optionfeaturetype_has_none():
    assert hasattr(deviceModelingLanguage::OptionFeatureType, "none")
    descriptor = None
    for klass in deviceModelingLanguage::OptionFeatureType.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::setfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SetFeatureType)


def test_devicemodelinglanguage::setfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::SetFeatureType.__init__)


def test_devicemodelinglanguage::setfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SetFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::eitherfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::EitherFeatureType)


def test_devicemodelinglanguage::eitherfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::EitherFeatureType.__init__)


def test_devicemodelinglanguage::eitherfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::EitherFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "choice" in params, "Missing parameter 'choice'"

def test_devicemodelinglanguage::eitherfeaturetype_has_choice():
    assert hasattr(deviceModelingLanguage::EitherFeatureType, "choice")
    descriptor = None
    for klass in deviceModelingLanguage::EitherFeatureType.__mro__:
        if "choice" in klass.__dict__:
            descriptor = klass.__dict__["choice"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::basefeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::BaseFeatureType)


def test_devicemodelinglanguage::basefeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage::BaseFeatureType.__init__)


def test_devicemodelinglanguage::basefeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::BaseFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::model_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Model)


def test_devicemodelinglanguage::model_constructor_exists():
    assert callable(deviceModelingLanguage::Model.__init__)


def test_devicemodelinglanguage::model_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Model.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "product" in params, "Missing parameter 'product'"
    assert "schema" in params, "Missing parameter 'schema'"

def test_devicemodelinglanguage::model_has_class_():
    assert hasattr(deviceModelingLanguage::Model, "class_")
    descriptor = None
    for klass in deviceModelingLanguage::Model.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::model_has_product():
    assert hasattr(deviceModelingLanguage::Model, "product")
    descriptor = None
    for klass in deviceModelingLanguage::Model.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage::model_has_schema():
    assert hasattr(deviceModelingLanguage::Model, "schema")
    descriptor = None
    for klass in deviceModelingLanguage::Model.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::literal_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Literal)


def test_devicemodelinglanguage::literal_constructor_exists():
    assert callable(deviceModelingLanguage::Literal.__init__)


def test_devicemodelinglanguage::literal_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Literal.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::type_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Type)


def test_devicemodelinglanguage::type_constructor_exists():
    assert callable(deviceModelingLanguage::Type.__init__)


def test_devicemodelinglanguage::type_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Type.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::modifier_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Modifier)


def test_devicemodelinglanguage::modifier_constructor_exists():
    assert callable(deviceModelingLanguage::Modifier.__init__)


def test_devicemodelinglanguage::modifier_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Modifier.__init__)
    params = list(sig.parameters.keys())



def test_accessor_is_not_abstract():
    assert not inspect.isabstract(Accessor)


def test_accessor_constructor_exists():
    assert callable(Accessor.__init__)


def test_accessor_constructor_args():
    sig = inspect.signature(Accessor.__init__)
    params = list(sig.parameters.keys())



def test_memberdecl_is_not_abstract():
    assert not inspect.isabstract(MemberDecl)


def test_memberdecl_constructor_exists():
    assert callable(MemberDecl.__init__)


def test_memberdecl_constructor_args():
    sig = inspect.signature(MemberDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::submemberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::SubMemberDecl)


def test_devicemodelinglanguage::submemberdecl_constructor_exists():
    assert callable(deviceModelingLanguage::SubMemberDecl.__init__)


def test_devicemodelinglanguage::submemberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::SubMemberDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::submemberdecl_has_name():
    assert hasattr(deviceModelingLanguage::SubMemberDecl, "name")
    descriptor = None
    for klass in deviceModelingLanguage::SubMemberDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::invariantdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::InvariantDecl)


def test_devicemodelinglanguage::invariantdecl_constructor_exists():
    assert callable(deviceModelingLanguage::InvariantDecl.__init__)


def test_devicemodelinglanguage::invariantdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::InvariantDecl.__init__)
    params = list(sig.parameters.keys())
    assert "invName" in params, "Missing parameter 'invName'"

def test_devicemodelinglanguage::invariantdecl_has_invName():
    assert hasattr(deviceModelingLanguage::InvariantDecl, "invName")
    descriptor = None
    for klass in deviceModelingLanguage::InvariantDecl.__mro__:
        if "invName" in klass.__dict__:
            descriptor = klass.__dict__["invName"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::attrdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::AttrDecl)


def test_devicemodelinglanguage::attrdecl_constructor_exists():
    assert callable(deviceModelingLanguage::AttrDecl.__init__)


def test_devicemodelinglanguage::attrdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::AttrDecl.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_devicemodelinglanguage::attrdecl_has_attributeName():
    assert hasattr(deviceModelingLanguage::AttrDecl, "attributeName")
    descriptor = None
    for klass in deviceModelingLanguage::AttrDecl.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::exp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Exp)


def test_devicemodelinglanguage::exp_constructor_exists():
    assert callable(deviceModelingLanguage::Exp.__init__)


def test_devicemodelinglanguage::exp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Exp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::assignment_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Assignment)


def test_devicemodelinglanguage::assignment_constructor_exists():
    assert callable(deviceModelingLanguage::Assignment.__init__)


def test_devicemodelinglanguage::assignment_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::assignment_has_name():
    assert hasattr(deviceModelingLanguage::Assignment, "name")
    descriptor = None
    for klass in deviceModelingLanguage::Assignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage::device_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Device)


def test_devicemodelinglanguage::device_constructor_exists():
    assert callable(deviceModelingLanguage::Device.__init__)


def test_devicemodelinglanguage::device_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Device.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::memberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::MemberDecl)


def test_devicemodelinglanguage::memberdecl_constructor_exists():
    assert callable(deviceModelingLanguage::MemberDecl.__init__)


def test_devicemodelinglanguage::memberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::MemberDecl.__init__)
    params = list(sig.parameters.keys())



def test_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::featuredecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::FeatureDecl)


def test_devicemodelinglanguage::featuredecl_constructor_exists():
    assert callable(deviceModelingLanguage::FeatureDecl.__init__)


def test_devicemodelinglanguage::featuredecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::FeatureDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::typedecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::TypeDecl)


def test_devicemodelinglanguage::typedecl_constructor_exists():
    assert callable(deviceModelingLanguage::TypeDecl.__init__)


def test_devicemodelinglanguage::typedecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage::decl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage::Decl)


def test_devicemodelinglanguage::decl_constructor_exists():
    assert callable(deviceModelingLanguage::Decl.__init__)


def test_devicemodelinglanguage::decl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage::Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage::decl_has_name():
    assert hasattr(deviceModelingLanguage::Decl, "name")
    descriptor = None
    for klass in deviceModelingLanguage::Decl.__mro__:
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
SimpleOptionLiteral_strategy = st.builds(
    SimpleOptionLiteral,
)
deviceModelingLanguage::SimpleSomeLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleSomeLiteral,
)
deviceModelingLanguage::SimpleNoneLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleNoneLiteral,
)
Exp_strategy = st.builds(
    Exp,
)
deviceModelingLanguage::PrimaryExp_strategy = st.builds(
    deviceModelingLanguage::PrimaryExp,
)
deviceModelingLanguage::UnaryExp_strategy = st.builds(
    deviceModelingLanguage::UnaryExp,
    op=
        safe_text
)
deviceModelingLanguage::BinaryExp_strategy = st.builds(
    deviceModelingLanguage::BinaryExp,
    op=
        safe_text
)
OptionLiteral_strategy = st.builds(
    OptionLiteral,
)
deviceModelingLanguage::SomeLiteral_strategy = st.builds(
    deviceModelingLanguage::SomeLiteral,
)
deviceModelingLanguage::NoneLiteral_strategy = st.builds(
    deviceModelingLanguage::NoneLiteral,
)
BaseType_strategy = st.builds(
    BaseType,
)
deviceModelingLanguage::NoneType_strategy = st.builds(
    deviceModelingLanguage::NoneType,
)
deviceModelingLanguage::SomeType_strategy = st.builds(
    deviceModelingLanguage::SomeType,
)
deviceModelingLanguage::OptionType_strategy = st.builds(
    deviceModelingLanguage::OptionType,
)
deviceModelingLanguage::TupleType_strategy = st.builds(
    deviceModelingLanguage::TupleType,
)
Primary_strategy = st.builds(
    Primary,
)
deviceModelingLanguage::LiteralExp_strategy = st.builds(
    deviceModelingLanguage::LiteralExp,
)
deviceModelingLanguage::NameExp_strategy = st.builds(
    deviceModelingLanguage::NameExp,
    id=
        safe_text
)
deviceModelingLanguage::AccessExp_strategy = st.builds(
    deviceModelingLanguage::AccessExp,
)
Modifier_strategy = st.builds(
    Modifier,
)
MModifier_strategy = st.builds(
    MModifier,
)
deviceModelingLanguage::Const_strategy = st.builds(
    deviceModelingLanguage::Const,
    product=
        st.booleans(),
    instance=
        st.booleans(),
    schema=
        st.booleans(),
    class_=
        st.booleans()
)
ConstraintNat_strategy = st.builds(
    ConstraintNat,
)
deviceModelingLanguage::AnyNatConstraint_strategy = st.builds(
    deviceModelingLanguage::AnyNatConstraint,
)
deviceModelingLanguage::NumNatConstraint_strategy = st.builds(
    deviceModelingLanguage::NumNatConstraint,
    num=
        safe_text
)
deviceModelingLanguage::Override_strategy = st.builds(
    deviceModelingLanguage::Override,
)
deviceModelingLanguage::Var_strategy = st.builds(
    deviceModelingLanguage::Var,
)
deviceModelingLanguage::Val_strategy = st.builds(
    deviceModelingLanguage::Val,
)
Type_strategy = st.builds(
    Type,
)
deviceModelingLanguage::SetType_strategy = st.builds(
    deviceModelingLanguage::SetType,
)
deviceModelingLanguage::SeqType_strategy = st.builds(
    deviceModelingLanguage::SeqType,
)
deviceModelingLanguage::BaseType_strategy = st.builds(
    deviceModelingLanguage::BaseType,
)
deviceModelingLanguage::Primary_strategy = st.builds(
    deviceModelingLanguage::Primary,
)
deviceModelingLanguage::Accessor_strategy = st.builds(
    deviceModelingLanguage::Accessor,
)
SimpleLiteral_strategy = st.builds(
    SimpleLiteral,
)
deviceModelingLanguage::SimpleSeqLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleSeqLiteral,
)
deviceModelingLanguage::SimpleTupleLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleTupleLiteral,
)
deviceModelingLanguage::SimpleSetLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleSetLiteral,
)
deviceModelingLanguage::SimpleOptionLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleOptionLiteral,
)
deviceModelingLanguage::SimpleBasicLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleBasicLiteral,
    lit=
        safe_text
)
deviceModelingLanguage::SimpleLiteral_strategy = st.builds(
    deviceModelingLanguage::SimpleLiteral,
)
Literal_strategy = st.builds(
    Literal,
)
deviceModelingLanguage::SetLiteral_strategy = st.builds(
    deviceModelingLanguage::SetLiteral,
)
deviceModelingLanguage::BasicLiteral_strategy = st.builds(
    deviceModelingLanguage::BasicLiteral,
    lit=
        safe_text
)
deviceModelingLanguage::TupleLiteral_strategy = st.builds(
    deviceModelingLanguage::TupleLiteral,
)
deviceModelingLanguage::OptionLiteral_strategy = st.builds(
    deviceModelingLanguage::OptionLiteral,
)
deviceModelingLanguage::SeqLiteral_strategy = st.builds(
    deviceModelingLanguage::SeqLiteral,
)
deviceModelingLanguage::Report_strategy = st.builds(
    deviceModelingLanguage::Report,
    name=
        safe_text
)
deviceModelingLanguage::FeatureType_strategy = st.builds(
    deviceModelingLanguage::FeatureType,
)
deviceModelingLanguage::MModifier_strategy = st.builds(
    deviceModelingLanguage::MModifier,
)
deviceModelingLanguage::ReportMemberDecl_strategy = st.builds(
    deviceModelingLanguage::ReportMemberDecl,
    name=
        safe_text
)
deviceModelingLanguage::Param_strategy = st.builds(
    deviceModelingLanguage::Param,
    name=
        safe_text
)
deviceModelingLanguage::ConstraintExp_strategy = st.builds(
    deviceModelingLanguage::ConstraintExp,
)
FeatureDecl_strategy = st.builds(
    FeatureDecl,
)
deviceModelingLanguage::Feature_strategy = st.builds(
    deviceModelingLanguage::Feature,
    class_=
        st.booleans(),
    schema=
        st.booleans(),
    product=
        st.booleans()
)
deviceModelingLanguage::Data_strategy = st.builds(
    deviceModelingLanguage::Data,
)
deviceModelingLanguage::App_strategy = st.builds(
    deviceModelingLanguage::App,
)
deviceModelingLanguage::SubMemberMatch_strategy = st.builds(
    deviceModelingLanguage::SubMemberMatch,
    any=
        safe_text,
    name=
        safe_text,
    qNames=
        safe_text
)
deviceModelingLanguage::ConstraintNat_strategy = st.builds(
    deviceModelingLanguage::ConstraintNat,
)
InvariantDecl_strategy = st.builds(
    InvariantDecl,
)
deviceModelingLanguage::GeneralInvariant_strategy = st.builds(
    deviceModelingLanguage::GeneralInvariant,
)
deviceModelingLanguage::MultiplicityInvariant_strategy = st.builds(
    deviceModelingLanguage::MultiplicityInvariant,
)
FeatureType_strategy = st.builds(
    FeatureType,
)
deviceModelingLanguage::SeqFeatureType_strategy = st.builds(
    deviceModelingLanguage::SeqFeatureType,
)
deviceModelingLanguage::SomeFeatureType_strategy = st.builds(
    deviceModelingLanguage::SomeFeatureType,
)
deviceModelingLanguage::OptionFeatureType_strategy = st.builds(
    deviceModelingLanguage::OptionFeatureType,
    none=
        st.booleans()
)
deviceModelingLanguage::SetFeatureType_strategy = st.builds(
    deviceModelingLanguage::SetFeatureType,
)
deviceModelingLanguage::EitherFeatureType_strategy = st.builds(
    deviceModelingLanguage::EitherFeatureType,
    choice=
        safe_text
)
deviceModelingLanguage::BaseFeatureType_strategy = st.builds(
    deviceModelingLanguage::BaseFeatureType,
)
deviceModelingLanguage::Model_strategy = st.builds(
    deviceModelingLanguage::Model,
    class_=
        st.booleans(),
    product=
        st.booleans(),
    schema=
        st.booleans()
)
deviceModelingLanguage::Literal_strategy = st.builds(
    deviceModelingLanguage::Literal,
)
deviceModelingLanguage::Type_strategy = st.builds(
    deviceModelingLanguage::Type,
)
deviceModelingLanguage::Modifier_strategy = st.builds(
    deviceModelingLanguage::Modifier,
)
Accessor_strategy = st.builds(
    Accessor,
)
MemberDecl_strategy = st.builds(
    MemberDecl,
)
deviceModelingLanguage::SubMemberDecl_strategy = st.builds(
    deviceModelingLanguage::SubMemberDecl,
    name=
        safe_text
)
deviceModelingLanguage::InvariantDecl_strategy = st.builds(
    deviceModelingLanguage::InvariantDecl,
    invName=
        safe_text
)
deviceModelingLanguage::AttrDecl_strategy = st.builds(
    deviceModelingLanguage::AttrDecl,
    attributeName=
        safe_text
)
deviceModelingLanguage::Exp_strategy = st.builds(
    deviceModelingLanguage::Exp,
)
deviceModelingLanguage::Assignment_strategy = st.builds(
    deviceModelingLanguage::Assignment,
    name=
        safe_text
)
deviceModelingLanguage::Device_strategy = st.builds(
    deviceModelingLanguage::Device,
)
deviceModelingLanguage::MemberDecl_strategy = st.builds(
    deviceModelingLanguage::MemberDecl,
)
Decl_strategy = st.builds(
    Decl,
)
deviceModelingLanguage::FeatureDecl_strategy = st.builds(
    deviceModelingLanguage::FeatureDecl,
)
deviceModelingLanguage::TypeDecl_strategy = st.builds(
    deviceModelingLanguage::TypeDecl,
)
deviceModelingLanguage::Decl_strategy = st.builds(
    deviceModelingLanguage::Decl,
    name=
        safe_text
)

@given(instance=SimpleOptionLiteral_strategy)
@settings(max_examples=50)
def test_simpleoptionliteral_instantiation(instance):
    assert isinstance(instance, SimpleOptionLiteral)

@given(instance=deviceModelingLanguage::SimpleSomeLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simplesomeliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleSomeLiteral)

@given(instance=deviceModelingLanguage::SimpleNoneLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simplenoneliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleNoneLiteral)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=deviceModelingLanguage::PrimaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::primaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::PrimaryExp)

@given(instance=deviceModelingLanguage::UnaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::unaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::UnaryExp)

@given(instance=deviceModelingLanguage::UnaryExp_strategy)
def test_devicemodelinglanguage::unaryexp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=deviceModelingLanguage::UnaryExp_strategy)
def test_devicemodelinglanguage::unaryexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=deviceModelingLanguage::BinaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::binaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::BinaryExp)

@given(instance=deviceModelingLanguage::BinaryExp_strategy)
def test_devicemodelinglanguage::binaryexp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=deviceModelingLanguage::BinaryExp_strategy)
def test_devicemodelinglanguage::binaryexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OptionLiteral_strategy)
@settings(max_examples=50)
def test_optionliteral_instantiation(instance):
    assert isinstance(instance, OptionLiteral)

@given(instance=deviceModelingLanguage::SomeLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::someliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SomeLiteral)

@given(instance=deviceModelingLanguage::NoneLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::noneliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::NoneLiteral)

@given(instance=BaseType_strategy)
@settings(max_examples=50)
def test_basetype_instantiation(instance):
    assert isinstance(instance, BaseType)

@given(instance=deviceModelingLanguage::NoneType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::nonetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::NoneType)

@given(instance=deviceModelingLanguage::SomeType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::sometype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SomeType)

@given(instance=deviceModelingLanguage::OptionType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::optiontype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::OptionType)

@given(instance=deviceModelingLanguage::TupleType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::tupletype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::TupleType)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=deviceModelingLanguage::LiteralExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::literalexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::LiteralExp)

@given(instance=deviceModelingLanguage::NameExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::nameexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::NameExp)

@given(instance=deviceModelingLanguage::NameExp_strategy)
def test_devicemodelinglanguage::nameexp_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=deviceModelingLanguage::NameExp_strategy)
def test_devicemodelinglanguage::nameexp_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=deviceModelingLanguage::AccessExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::accessexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::AccessExp)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=MModifier_strategy)
@settings(max_examples=50)
def test_mmodifier_instantiation(instance):
    assert isinstance(instance, MModifier)

@given(instance=deviceModelingLanguage::Const_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::const_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Const)

@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_product_type(instance):
    assert isinstance(instance.product, bool)


@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_instance_type(instance):
    assert isinstance(instance.instance, bool)


@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_schema_type(instance):
    assert isinstance(instance.schema, bool)


@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_class__type(instance):
    assert isinstance(instance.class_, bool)


@given(instance=deviceModelingLanguage::Const_strategy)
def test_devicemodelinglanguage::const_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=ConstraintNat_strategy)
@settings(max_examples=50)
def test_constraintnat_instantiation(instance):
    assert isinstance(instance, ConstraintNat)

@given(instance=deviceModelingLanguage::AnyNatConstraint_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::anynatconstraint_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::AnyNatConstraint)

@given(instance=deviceModelingLanguage::NumNatConstraint_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::numnatconstraint_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::NumNatConstraint)

@given(instance=deviceModelingLanguage::NumNatConstraint_strategy)
def test_devicemodelinglanguage::numnatconstraint_num_type(instance):
    assert isinstance(instance.num, str)


@given(instance=deviceModelingLanguage::NumNatConstraint_strategy)
def test_devicemodelinglanguage::numnatconstraint_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=deviceModelingLanguage::Override_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::override_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Override)

@given(instance=deviceModelingLanguage::Var_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::var_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Var)

@given(instance=deviceModelingLanguage::Val_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::val_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Val)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=deviceModelingLanguage::SetType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::settype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SetType)

@given(instance=deviceModelingLanguage::SeqType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::seqtype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SeqType)

@given(instance=deviceModelingLanguage::BaseType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::basetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::BaseType)

@given(instance=deviceModelingLanguage::Primary_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::primary_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Primary)

@given(instance=deviceModelingLanguage::Accessor_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::accessor_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Accessor)

@given(instance=SimpleLiteral_strategy)
@settings(max_examples=50)
def test_simpleliteral_instantiation(instance):
    assert isinstance(instance, SimpleLiteral)

@given(instance=deviceModelingLanguage::SimpleSeqLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simpleseqliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleSeqLiteral)

@given(instance=deviceModelingLanguage::SimpleTupleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simpletupleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleTupleLiteral)

@given(instance=deviceModelingLanguage::SimpleSetLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simplesetliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleSetLiteral)

@given(instance=deviceModelingLanguage::SimpleOptionLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simpleoptionliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleOptionLiteral)

@given(instance=deviceModelingLanguage::SimpleBasicLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simplebasicliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleBasicLiteral)

@given(instance=deviceModelingLanguage::SimpleBasicLiteral_strategy)
def test_devicemodelinglanguage::simplebasicliteral_lit_type(instance):
    assert isinstance(instance.lit, str)


@given(instance=deviceModelingLanguage::SimpleBasicLiteral_strategy)
def test_devicemodelinglanguage::simplebasicliteral_lit_setter(instance):
    original = instance.lit
    instance.lit = original
    assert instance.lit == original

@given(instance=deviceModelingLanguage::SimpleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::simpleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SimpleLiteral)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=deviceModelingLanguage::SetLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::setliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SetLiteral)

@given(instance=deviceModelingLanguage::BasicLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::basicliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::BasicLiteral)

@given(instance=deviceModelingLanguage::BasicLiteral_strategy)
def test_devicemodelinglanguage::basicliteral_lit_type(instance):
    assert isinstance(instance.lit, str)


@given(instance=deviceModelingLanguage::BasicLiteral_strategy)
def test_devicemodelinglanguage::basicliteral_lit_setter(instance):
    original = instance.lit
    instance.lit = original
    assert instance.lit == original

@given(instance=deviceModelingLanguage::TupleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::tupleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::TupleLiteral)

@given(instance=deviceModelingLanguage::OptionLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::optionliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::OptionLiteral)

@given(instance=deviceModelingLanguage::SeqLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::seqliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SeqLiteral)

@given(instance=deviceModelingLanguage::Report_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::report_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Report)

@given(instance=deviceModelingLanguage::Report_strategy)
def test_devicemodelinglanguage::report_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::Report_strategy)
def test_devicemodelinglanguage::report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::FeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::featuretype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::FeatureType)

@given(instance=deviceModelingLanguage::MModifier_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::mmodifier_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::MModifier)

@given(instance=deviceModelingLanguage::ReportMemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::reportmemberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::ReportMemberDecl)

@given(instance=deviceModelingLanguage::ReportMemberDecl_strategy)
def test_devicemodelinglanguage::reportmemberdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::ReportMemberDecl_strategy)
def test_devicemodelinglanguage::reportmemberdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::Param_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::param_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Param)

@given(instance=deviceModelingLanguage::Param_strategy)
def test_devicemodelinglanguage::param_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::Param_strategy)
def test_devicemodelinglanguage::param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::ConstraintExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::constraintexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::ConstraintExp)

@given(instance=FeatureDecl_strategy)
@settings(max_examples=50)
def test_featuredecl_instantiation(instance):
    assert isinstance(instance, FeatureDecl)

@given(instance=deviceModelingLanguage::Feature_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::feature_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Feature)

@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_class__type(instance):
    assert isinstance(instance.class_, bool)


@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_schema_type(instance):
    assert isinstance(instance.schema, bool)


@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_product_type(instance):
    assert isinstance(instance.product, bool)


@given(instance=deviceModelingLanguage::Feature_strategy)
def test_devicemodelinglanguage::feature_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=deviceModelingLanguage::Data_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::data_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Data)

@given(instance=deviceModelingLanguage::App_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::app_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::App)

@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::submembermatch_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SubMemberMatch)

@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_qNames_type(instance):
    assert isinstance(instance.qNames, str)


@given(instance=deviceModelingLanguage::SubMemberMatch_strategy)
def test_devicemodelinglanguage::submembermatch_qNames_setter(instance):
    original = instance.qNames
    instance.qNames = original
    assert instance.qNames == original

@given(instance=deviceModelingLanguage::ConstraintNat_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::constraintnat_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::ConstraintNat)

@given(instance=InvariantDecl_strategy)
@settings(max_examples=50)
def test_invariantdecl_instantiation(instance):
    assert isinstance(instance, InvariantDecl)

@given(instance=deviceModelingLanguage::GeneralInvariant_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::generalinvariant_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::GeneralInvariant)

@given(instance=deviceModelingLanguage::MultiplicityInvariant_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::multiplicityinvariant_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::MultiplicityInvariant)

@given(instance=FeatureType_strategy)
@settings(max_examples=50)
def test_featuretype_instantiation(instance):
    assert isinstance(instance, FeatureType)

@given(instance=deviceModelingLanguage::SeqFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::seqfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SeqFeatureType)

@given(instance=deviceModelingLanguage::SomeFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::somefeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SomeFeatureType)

@given(instance=deviceModelingLanguage::OptionFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::optionfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::OptionFeatureType)

@given(instance=deviceModelingLanguage::OptionFeatureType_strategy)
def test_devicemodelinglanguage::optionfeaturetype_none_type(instance):
    assert isinstance(instance.none, bool)


@given(instance=deviceModelingLanguage::OptionFeatureType_strategy)
def test_devicemodelinglanguage::optionfeaturetype_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=deviceModelingLanguage::SetFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::setfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SetFeatureType)

@given(instance=deviceModelingLanguage::EitherFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::eitherfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::EitherFeatureType)

@given(instance=deviceModelingLanguage::EitherFeatureType_strategy)
def test_devicemodelinglanguage::eitherfeaturetype_choice_type(instance):
    assert isinstance(instance.choice, str)


@given(instance=deviceModelingLanguage::EitherFeatureType_strategy)
def test_devicemodelinglanguage::eitherfeaturetype_choice_setter(instance):
    original = instance.choice
    instance.choice = original
    assert instance.choice == original

@given(instance=deviceModelingLanguage::BaseFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::basefeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::BaseFeatureType)

@given(instance=deviceModelingLanguage::Model_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::model_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Model)

@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_class__type(instance):
    assert isinstance(instance.class_, bool)


@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_product_type(instance):
    assert isinstance(instance.product, bool)


@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_schema_type(instance):
    assert isinstance(instance.schema, bool)


@given(instance=deviceModelingLanguage::Model_strategy)
def test_devicemodelinglanguage::model_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=deviceModelingLanguage::Literal_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::literal_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Literal)

@given(instance=deviceModelingLanguage::Type_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::type_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Type)

@given(instance=deviceModelingLanguage::Modifier_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::modifier_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Modifier)

@given(instance=Accessor_strategy)
@settings(max_examples=50)
def test_accessor_instantiation(instance):
    assert isinstance(instance, Accessor)

@given(instance=MemberDecl_strategy)
@settings(max_examples=50)
def test_memberdecl_instantiation(instance):
    assert isinstance(instance, MemberDecl)

@given(instance=deviceModelingLanguage::SubMemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::submemberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::SubMemberDecl)

@given(instance=deviceModelingLanguage::SubMemberDecl_strategy)
def test_devicemodelinglanguage::submemberdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::SubMemberDecl_strategy)
def test_devicemodelinglanguage::submemberdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::InvariantDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::invariantdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::InvariantDecl)

@given(instance=deviceModelingLanguage::InvariantDecl_strategy)
def test_devicemodelinglanguage::invariantdecl_invName_type(instance):
    assert isinstance(instance.invName, str)


@given(instance=deviceModelingLanguage::InvariantDecl_strategy)
def test_devicemodelinglanguage::invariantdecl_invName_setter(instance):
    original = instance.invName
    instance.invName = original
    assert instance.invName == original

@given(instance=deviceModelingLanguage::AttrDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::attrdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::AttrDecl)

@given(instance=deviceModelingLanguage::AttrDecl_strategy)
def test_devicemodelinglanguage::attrdecl_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=deviceModelingLanguage::AttrDecl_strategy)
def test_devicemodelinglanguage::attrdecl_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=deviceModelingLanguage::Exp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::exp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Exp)

@given(instance=deviceModelingLanguage::Assignment_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::assignment_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Assignment)

@given(instance=deviceModelingLanguage::Assignment_strategy)
def test_devicemodelinglanguage::assignment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::Assignment_strategy)
def test_devicemodelinglanguage::assignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage::Device_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::device_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Device)

@given(instance=deviceModelingLanguage::MemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::memberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::MemberDecl)

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=deviceModelingLanguage::FeatureDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::featuredecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::FeatureDecl)

@given(instance=deviceModelingLanguage::TypeDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::typedecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::TypeDecl)

@given(instance=deviceModelingLanguage::Decl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage::decl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage::Decl)

@given(instance=deviceModelingLanguage::Decl_strategy)
def test_devicemodelinglanguage::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=deviceModelingLanguage::Decl_strategy)
def test_devicemodelinglanguage::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

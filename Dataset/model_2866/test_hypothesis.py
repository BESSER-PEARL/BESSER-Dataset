import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleOptionLiteral,
    deviceModelingLanguage_SimpleSomeLiteral,
    deviceModelingLanguage_SimpleNoneLiteral,
    BaseType,
    deviceModelingLanguage_SomeType,
    deviceModelingLanguage_OptionType,
    deviceModelingLanguage_TupleType,
    Primary,
    deviceModelingLanguage_LiteralExp,
    MModifier,
    ConstraintNat,
    deviceModelingLanguage_AnyNatConstraint,
    deviceModelingLanguage_NumNatConstraint,
    deviceModelingLanguage_SimpleLiteral,
    Literal,
    deviceModelingLanguage_TupleLiteral,
    deviceModelingLanguage_OptionLiteral,
    deviceModelingLanguage_SeqLiteral,
    deviceModelingLanguage_SetLiteral,
    deviceModelingLanguage_BasicLiteral,
    Type,
    deviceModelingLanguage_SetType,
    deviceModelingLanguage_SeqType,
    deviceModelingLanguage_BaseType,
    deviceModelingLanguage_Primary,
    deviceModelingLanguage_Accessor,
    deviceModelingLanguage_ReportMemberDecl,
    deviceModelingLanguage_Param,
    deviceModelingLanguage_ConstraintExp,
    deviceModelingLanguage_NameExp,
    Exp,
    deviceModelingLanguage_UnaryExp,
    deviceModelingLanguage_AccessExp,
    deviceModelingLanguage_PrimaryExp,
    deviceModelingLanguage_BinaryExp,
    OptionLiteral,
    deviceModelingLanguage_SomeLiteral,
    deviceModelingLanguage_NoneLiteral,
    deviceModelingLanguage_NoneType,
    Modifier,
    deviceModelingLanguage_Override,
    deviceModelingLanguage_Val,
    deviceModelingLanguage_Var,
    deviceModelingLanguage_Const,
    SimpleLiteral,
    deviceModelingLanguage_SimpleSeqLiteral,
    deviceModelingLanguage_SimpleOptionLiteral,
    deviceModelingLanguage_SimpleSetLiteral,
    deviceModelingLanguage_SimpleTupleLiteral,
    deviceModelingLanguage_SimpleBasicLiteral,
    deviceModelingLanguage_SubMemberMatch,
    deviceModelingLanguage_ConstraintNat,
    InvariantDecl,
    deviceModelingLanguage_MultiplicityInvariant,
    FeatureType,
    deviceModelingLanguage_SomeFeatureType,
    deviceModelingLanguage_EitherFeatureType,
    deviceModelingLanguage_SetFeatureType,
    deviceModelingLanguage_OptionFeatureType,
    deviceModelingLanguage_SeqFeatureType,
    deviceModelingLanguage_BaseFeatureType,
    deviceModelingLanguage_Report,
    deviceModelingLanguage_FeatureType,
    deviceModelingLanguage_MModifier,
    deviceModelingLanguage_Literal,
    deviceModelingLanguage_Type,
    deviceModelingLanguage_Modifier,
    Accessor,
    MemberDecl,
    deviceModelingLanguage_InvariantDecl,
    deviceModelingLanguage_SubMemberDecl,
    FeatureDecl,
    deviceModelingLanguage_Data,
    deviceModelingLanguage_App,
    deviceModelingLanguage_Feature,
    deviceModelingLanguage_GeneralInvariant,
    Decl,
    deviceModelingLanguage_FeatureDecl,
    deviceModelingLanguage_TypeDecl,
    deviceModelingLanguage_Decl,
    deviceModelingLanguage_Model,
    deviceModelingLanguage_AttrDecl,
    deviceModelingLanguage_Exp,
    deviceModelingLanguage_Assignment,
    deviceModelingLanguage_Device,
    deviceModelingLanguage_MemberDecl,
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



def test_devicemodelinglanguage_simplesomeliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleSomeLiteral)


def test_devicemodelinglanguage_simplesomeliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleSomeLiteral.__init__)


def test_devicemodelinglanguage_simplesomeliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleSomeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simplenoneliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleNoneLiteral)


def test_devicemodelinglanguage_simplenoneliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleNoneLiteral.__init__)


def test_devicemodelinglanguage_simplenoneliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleNoneLiteral.__init__)
    params = list(sig.parameters.keys())



def test_basetype_is_not_abstract():
    assert not inspect.isabstract(BaseType)


def test_basetype_constructor_exists():
    assert callable(BaseType.__init__)


def test_basetype_constructor_args():
    sig = inspect.signature(BaseType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_sometype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SomeType)


def test_devicemodelinglanguage_sometype_constructor_exists():
    assert callable(deviceModelingLanguage_SomeType.__init__)


def test_devicemodelinglanguage_sometype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SomeType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_optiontype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_OptionType)


def test_devicemodelinglanguage_optiontype_constructor_exists():
    assert callable(deviceModelingLanguage_OptionType.__init__)


def test_devicemodelinglanguage_optiontype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_OptionType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_tupletype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_TupleType)


def test_devicemodelinglanguage_tupletype_constructor_exists():
    assert callable(deviceModelingLanguage_TupleType.__init__)


def test_devicemodelinglanguage_tupletype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_literalexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_LiteralExp)


def test_devicemodelinglanguage_literalexp_constructor_exists():
    assert callable(deviceModelingLanguage_LiteralExp.__init__)


def test_devicemodelinglanguage_literalexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_mmodifier_is_not_abstract():
    assert not inspect.isabstract(MModifier)


def test_mmodifier_constructor_exists():
    assert callable(MModifier.__init__)


def test_mmodifier_constructor_args():
    sig = inspect.signature(MModifier.__init__)
    params = list(sig.parameters.keys())



def test_constraintnat_is_not_abstract():
    assert not inspect.isabstract(ConstraintNat)


def test_constraintnat_constructor_exists():
    assert callable(ConstraintNat.__init__)


def test_constraintnat_constructor_args():
    sig = inspect.signature(ConstraintNat.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_anynatconstraint_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_AnyNatConstraint)


def test_devicemodelinglanguage_anynatconstraint_constructor_exists():
    assert callable(deviceModelingLanguage_AnyNatConstraint.__init__)


def test_devicemodelinglanguage_anynatconstraint_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_AnyNatConstraint.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_numnatconstraint_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_NumNatConstraint)


def test_devicemodelinglanguage_numnatconstraint_constructor_exists():
    assert callable(deviceModelingLanguage_NumNatConstraint.__init__)


def test_devicemodelinglanguage_numnatconstraint_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_NumNatConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"

def test_devicemodelinglanguage_numnatconstraint_has_num():
    assert hasattr(deviceModelingLanguage_NumNatConstraint, "num")
    descriptor = None
    for klass in deviceModelingLanguage_NumNatConstraint.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_simpleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleLiteral)


def test_devicemodelinglanguage_simpleliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleLiteral.__init__)


def test_devicemodelinglanguage_simpleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_tupleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_TupleLiteral)


def test_devicemodelinglanguage_tupleliteral_constructor_exists():
    assert callable(deviceModelingLanguage_TupleLiteral.__init__)


def test_devicemodelinglanguage_tupleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_TupleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_optionliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_OptionLiteral)


def test_devicemodelinglanguage_optionliteral_constructor_exists():
    assert callable(deviceModelingLanguage_OptionLiteral.__init__)


def test_devicemodelinglanguage_optionliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_OptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_seqliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SeqLiteral)


def test_devicemodelinglanguage_seqliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SeqLiteral.__init__)


def test_devicemodelinglanguage_seqliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SeqLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_setliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SetLiteral)


def test_devicemodelinglanguage_setliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SetLiteral.__init__)


def test_devicemodelinglanguage_setliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SetLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_basicliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_BasicLiteral)


def test_devicemodelinglanguage_basicliteral_constructor_exists():
    assert callable(deviceModelingLanguage_BasicLiteral.__init__)


def test_devicemodelinglanguage_basicliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_BasicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "lit" in params, "Missing parameter 'lit'"

def test_devicemodelinglanguage_basicliteral_has_lit():
    assert hasattr(deviceModelingLanguage_BasicLiteral, "lit")
    descriptor = None
    for klass in deviceModelingLanguage_BasicLiteral.__mro__:
        if "lit" in klass.__dict__:
            descriptor = klass.__dict__["lit"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_settype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SetType)


def test_devicemodelinglanguage_settype_constructor_exists():
    assert callable(deviceModelingLanguage_SetType.__init__)


def test_devicemodelinglanguage_settype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SetType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_seqtype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SeqType)


def test_devicemodelinglanguage_seqtype_constructor_exists():
    assert callable(deviceModelingLanguage_SeqType.__init__)


def test_devicemodelinglanguage_seqtype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SeqType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_basetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_BaseType)


def test_devicemodelinglanguage_basetype_constructor_exists():
    assert callable(deviceModelingLanguage_BaseType.__init__)


def test_devicemodelinglanguage_basetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_BaseType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_primary_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Primary)


def test_devicemodelinglanguage_primary_constructor_exists():
    assert callable(deviceModelingLanguage_Primary.__init__)


def test_devicemodelinglanguage_primary_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Primary.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_accessor_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Accessor)


def test_devicemodelinglanguage_accessor_constructor_exists():
    assert callable(deviceModelingLanguage_Accessor.__init__)


def test_devicemodelinglanguage_accessor_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Accessor.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_reportmemberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_ReportMemberDecl)


def test_devicemodelinglanguage_reportmemberdecl_constructor_exists():
    assert callable(deviceModelingLanguage_ReportMemberDecl.__init__)


def test_devicemodelinglanguage_reportmemberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_ReportMemberDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_reportmemberdecl_has_name():
    assert hasattr(deviceModelingLanguage_ReportMemberDecl, "name")
    descriptor = None
    for klass in deviceModelingLanguage_ReportMemberDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_param_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Param)


def test_devicemodelinglanguage_param_constructor_exists():
    assert callable(deviceModelingLanguage_Param.__init__)


def test_devicemodelinglanguage_param_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_param_has_name():
    assert hasattr(deviceModelingLanguage_Param, "name")
    descriptor = None
    for klass in deviceModelingLanguage_Param.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_constraintexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_ConstraintExp)


def test_devicemodelinglanguage_constraintexp_constructor_exists():
    assert callable(deviceModelingLanguage_ConstraintExp.__init__)


def test_devicemodelinglanguage_constraintexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_ConstraintExp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_nameexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_NameExp)


def test_devicemodelinglanguage_nameexp_constructor_exists():
    assert callable(deviceModelingLanguage_NameExp.__init__)


def test_devicemodelinglanguage_nameexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_NameExp.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_devicemodelinglanguage_nameexp_has_id():
    assert hasattr(deviceModelingLanguage_NameExp, "id")
    descriptor = None
    for klass in deviceModelingLanguage_NameExp.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_unaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_UnaryExp)


def test_devicemodelinglanguage_unaryexp_constructor_exists():
    assert callable(deviceModelingLanguage_UnaryExp.__init__)


def test_devicemodelinglanguage_unaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_UnaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_devicemodelinglanguage_unaryexp_has_op():
    assert hasattr(deviceModelingLanguage_UnaryExp, "op")
    descriptor = None
    for klass in deviceModelingLanguage_UnaryExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_accessexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_AccessExp)


def test_devicemodelinglanguage_accessexp_constructor_exists():
    assert callable(deviceModelingLanguage_AccessExp.__init__)


def test_devicemodelinglanguage_accessexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_AccessExp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_primaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_PrimaryExp)


def test_devicemodelinglanguage_primaryexp_constructor_exists():
    assert callable(deviceModelingLanguage_PrimaryExp.__init__)


def test_devicemodelinglanguage_primaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_PrimaryExp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_binaryexp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_BinaryExp)


def test_devicemodelinglanguage_binaryexp_constructor_exists():
    assert callable(deviceModelingLanguage_BinaryExp.__init__)


def test_devicemodelinglanguage_binaryexp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_devicemodelinglanguage_binaryexp_has_op():
    assert hasattr(deviceModelingLanguage_BinaryExp, "op")
    descriptor = None
    for klass in deviceModelingLanguage_BinaryExp.__mro__:
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



def test_devicemodelinglanguage_someliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SomeLiteral)


def test_devicemodelinglanguage_someliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SomeLiteral.__init__)


def test_devicemodelinglanguage_someliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SomeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_noneliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_NoneLiteral)


def test_devicemodelinglanguage_noneliteral_constructor_exists():
    assert callable(deviceModelingLanguage_NoneLiteral.__init__)


def test_devicemodelinglanguage_noneliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_NoneLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_nonetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_NoneType)


def test_devicemodelinglanguage_nonetype_constructor_exists():
    assert callable(deviceModelingLanguage_NoneType.__init__)


def test_devicemodelinglanguage_nonetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_NoneType.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_override_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Override)


def test_devicemodelinglanguage_override_constructor_exists():
    assert callable(deviceModelingLanguage_Override.__init__)


def test_devicemodelinglanguage_override_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Override.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_val_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Val)


def test_devicemodelinglanguage_val_constructor_exists():
    assert callable(deviceModelingLanguage_Val.__init__)


def test_devicemodelinglanguage_val_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Val.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_var_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Var)


def test_devicemodelinglanguage_var_constructor_exists():
    assert callable(deviceModelingLanguage_Var.__init__)


def test_devicemodelinglanguage_var_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Var.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_const_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Const)


def test_devicemodelinglanguage_const_constructor_exists():
    assert callable(deviceModelingLanguage_Const.__init__)


def test_devicemodelinglanguage_const_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Const.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "product" in params, "Missing parameter 'product'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "schema" in params, "Missing parameter 'schema'"

def test_devicemodelinglanguage_const_has_class_():
    assert hasattr(deviceModelingLanguage_Const, "class_")
    descriptor = None
    for klass in deviceModelingLanguage_Const.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_const_has_product():
    assert hasattr(deviceModelingLanguage_Const, "product")
    descriptor = None
    for klass in deviceModelingLanguage_Const.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_const_has_instance():
    assert hasattr(deviceModelingLanguage_Const, "instance")
    descriptor = None
    for klass in deviceModelingLanguage_Const.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_const_has_schema():
    assert hasattr(deviceModelingLanguage_Const, "schema")
    descriptor = None
    for klass in deviceModelingLanguage_Const.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_simpleliteral_is_not_abstract():
    assert not inspect.isabstract(SimpleLiteral)


def test_simpleliteral_constructor_exists():
    assert callable(SimpleLiteral.__init__)


def test_simpleliteral_constructor_args():
    sig = inspect.signature(SimpleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simpleseqliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleSeqLiteral)


def test_devicemodelinglanguage_simpleseqliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleSeqLiteral.__init__)


def test_devicemodelinglanguage_simpleseqliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleSeqLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simpleoptionliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleOptionLiteral)


def test_devicemodelinglanguage_simpleoptionliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleOptionLiteral.__init__)


def test_devicemodelinglanguage_simpleoptionliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleOptionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simplesetliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleSetLiteral)


def test_devicemodelinglanguage_simplesetliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleSetLiteral.__init__)


def test_devicemodelinglanguage_simplesetliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleSetLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simpletupleliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleTupleLiteral)


def test_devicemodelinglanguage_simpletupleliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleTupleLiteral.__init__)


def test_devicemodelinglanguage_simpletupleliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleTupleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_simplebasicliteral_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SimpleBasicLiteral)


def test_devicemodelinglanguage_simplebasicliteral_constructor_exists():
    assert callable(deviceModelingLanguage_SimpleBasicLiteral.__init__)


def test_devicemodelinglanguage_simplebasicliteral_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SimpleBasicLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "lit" in params, "Missing parameter 'lit'"

def test_devicemodelinglanguage_simplebasicliteral_has_lit():
    assert hasattr(deviceModelingLanguage_SimpleBasicLiteral, "lit")
    descriptor = None
    for klass in deviceModelingLanguage_SimpleBasicLiteral.__mro__:
        if "lit" in klass.__dict__:
            descriptor = klass.__dict__["lit"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_submembermatch_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SubMemberMatch)


def test_devicemodelinglanguage_submembermatch_constructor_exists():
    assert callable(deviceModelingLanguage_SubMemberMatch.__init__)


def test_devicemodelinglanguage_submembermatch_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SubMemberMatch.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "qNames" in params, "Missing parameter 'qNames'"
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_submembermatch_has_any():
    assert hasattr(deviceModelingLanguage_SubMemberMatch, "any")
    descriptor = None
    for klass in deviceModelingLanguage_SubMemberMatch.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_submembermatch_has_qNames():
    assert hasattr(deviceModelingLanguage_SubMemberMatch, "qNames")
    descriptor = None
    for klass in deviceModelingLanguage_SubMemberMatch.__mro__:
        if "qNames" in klass.__dict__:
            descriptor = klass.__dict__["qNames"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_submembermatch_has_name():
    assert hasattr(deviceModelingLanguage_SubMemberMatch, "name")
    descriptor = None
    for klass in deviceModelingLanguage_SubMemberMatch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_constraintnat_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_ConstraintNat)


def test_devicemodelinglanguage_constraintnat_constructor_exists():
    assert callable(deviceModelingLanguage_ConstraintNat.__init__)


def test_devicemodelinglanguage_constraintnat_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_ConstraintNat.__init__)
    params = list(sig.parameters.keys())



def test_invariantdecl_is_not_abstract():
    assert not inspect.isabstract(InvariantDecl)


def test_invariantdecl_constructor_exists():
    assert callable(InvariantDecl.__init__)


def test_invariantdecl_constructor_args():
    sig = inspect.signature(InvariantDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_multiplicityinvariant_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_MultiplicityInvariant)


def test_devicemodelinglanguage_multiplicityinvariant_constructor_exists():
    assert callable(deviceModelingLanguage_MultiplicityInvariant.__init__)


def test_devicemodelinglanguage_multiplicityinvariant_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_MultiplicityInvariant.__init__)
    params = list(sig.parameters.keys())



def test_featuretype_is_not_abstract():
    assert not inspect.isabstract(FeatureType)


def test_featuretype_constructor_exists():
    assert callable(FeatureType.__init__)


def test_featuretype_constructor_args():
    sig = inspect.signature(FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_somefeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SomeFeatureType)


def test_devicemodelinglanguage_somefeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_SomeFeatureType.__init__)


def test_devicemodelinglanguage_somefeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SomeFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_eitherfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_EitherFeatureType)


def test_devicemodelinglanguage_eitherfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_EitherFeatureType.__init__)


def test_devicemodelinglanguage_eitherfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_EitherFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "choice" in params, "Missing parameter 'choice'"

def test_devicemodelinglanguage_eitherfeaturetype_has_choice():
    assert hasattr(deviceModelingLanguage_EitherFeatureType, "choice")
    descriptor = None
    for klass in deviceModelingLanguage_EitherFeatureType.__mro__:
        if "choice" in klass.__dict__:
            descriptor = klass.__dict__["choice"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_setfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SetFeatureType)


def test_devicemodelinglanguage_setfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_SetFeatureType.__init__)


def test_devicemodelinglanguage_setfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SetFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_optionfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_OptionFeatureType)


def test_devicemodelinglanguage_optionfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_OptionFeatureType.__init__)


def test_devicemodelinglanguage_optionfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_OptionFeatureType.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"

def test_devicemodelinglanguage_optionfeaturetype_has_none():
    assert hasattr(deviceModelingLanguage_OptionFeatureType, "none")
    descriptor = None
    for klass in deviceModelingLanguage_OptionFeatureType.__mro__:
        if "none" in klass.__dict__:
            descriptor = klass.__dict__["none"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_seqfeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SeqFeatureType)


def test_devicemodelinglanguage_seqfeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_SeqFeatureType.__init__)


def test_devicemodelinglanguage_seqfeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SeqFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_basefeaturetype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_BaseFeatureType)


def test_devicemodelinglanguage_basefeaturetype_constructor_exists():
    assert callable(deviceModelingLanguage_BaseFeatureType.__init__)


def test_devicemodelinglanguage_basefeaturetype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_BaseFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_report_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Report)


def test_devicemodelinglanguage_report_constructor_exists():
    assert callable(deviceModelingLanguage_Report.__init__)


def test_devicemodelinglanguage_report_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Report.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_report_has_name():
    assert hasattr(deviceModelingLanguage_Report, "name")
    descriptor = None
    for klass in deviceModelingLanguage_Report.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_featuretype_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_FeatureType)


def test_devicemodelinglanguage_featuretype_constructor_exists():
    assert callable(deviceModelingLanguage_FeatureType.__init__)


def test_devicemodelinglanguage_featuretype_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_mmodifier_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_MModifier)


def test_devicemodelinglanguage_mmodifier_constructor_exists():
    assert callable(deviceModelingLanguage_MModifier.__init__)


def test_devicemodelinglanguage_mmodifier_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_MModifier.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_literal_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Literal)


def test_devicemodelinglanguage_literal_constructor_exists():
    assert callable(deviceModelingLanguage_Literal.__init__)


def test_devicemodelinglanguage_literal_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Literal.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_type_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Type)


def test_devicemodelinglanguage_type_constructor_exists():
    assert callable(deviceModelingLanguage_Type.__init__)


def test_devicemodelinglanguage_type_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Type.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_modifier_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Modifier)


def test_devicemodelinglanguage_modifier_constructor_exists():
    assert callable(deviceModelingLanguage_Modifier.__init__)


def test_devicemodelinglanguage_modifier_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Modifier.__init__)
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



def test_devicemodelinglanguage_invariantdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_InvariantDecl)


def test_devicemodelinglanguage_invariantdecl_constructor_exists():
    assert callable(deviceModelingLanguage_InvariantDecl.__init__)


def test_devicemodelinglanguage_invariantdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_InvariantDecl.__init__)
    params = list(sig.parameters.keys())
    assert "invName" in params, "Missing parameter 'invName'"

def test_devicemodelinglanguage_invariantdecl_has_invName():
    assert hasattr(deviceModelingLanguage_InvariantDecl, "invName")
    descriptor = None
    for klass in deviceModelingLanguage_InvariantDecl.__mro__:
        if "invName" in klass.__dict__:
            descriptor = klass.__dict__["invName"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_submemberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_SubMemberDecl)


def test_devicemodelinglanguage_submemberdecl_constructor_exists():
    assert callable(deviceModelingLanguage_SubMemberDecl.__init__)


def test_devicemodelinglanguage_submemberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_SubMemberDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_submemberdecl_has_name():
    assert hasattr(deviceModelingLanguage_SubMemberDecl, "name")
    descriptor = None
    for klass in deviceModelingLanguage_SubMemberDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuredecl_is_not_abstract():
    assert not inspect.isabstract(FeatureDecl)


def test_featuredecl_constructor_exists():
    assert callable(FeatureDecl.__init__)


def test_featuredecl_constructor_args():
    sig = inspect.signature(FeatureDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_data_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Data)


def test_devicemodelinglanguage_data_constructor_exists():
    assert callable(deviceModelingLanguage_Data.__init__)


def test_devicemodelinglanguage_data_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Data.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_app_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_App)


def test_devicemodelinglanguage_app_constructor_exists():
    assert callable(deviceModelingLanguage_App.__init__)


def test_devicemodelinglanguage_app_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_App.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_feature_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Feature)


def test_devicemodelinglanguage_feature_constructor_exists():
    assert callable(deviceModelingLanguage_Feature.__init__)


def test_devicemodelinglanguage_feature_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "product" in params, "Missing parameter 'product'"

def test_devicemodelinglanguage_feature_has_schema():
    assert hasattr(deviceModelingLanguage_Feature, "schema")
    descriptor = None
    for klass in deviceModelingLanguage_Feature.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_feature_has_class_():
    assert hasattr(deviceModelingLanguage_Feature, "class_")
    descriptor = None
    for klass in deviceModelingLanguage_Feature.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_feature_has_product():
    assert hasattr(deviceModelingLanguage_Feature, "product")
    descriptor = None
    for klass in deviceModelingLanguage_Feature.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_generalinvariant_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_GeneralInvariant)


def test_devicemodelinglanguage_generalinvariant_constructor_exists():
    assert callable(deviceModelingLanguage_GeneralInvariant.__init__)


def test_devicemodelinglanguage_generalinvariant_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_GeneralInvariant.__init__)
    params = list(sig.parameters.keys())



def test_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_featuredecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_FeatureDecl)


def test_devicemodelinglanguage_featuredecl_constructor_exists():
    assert callable(deviceModelingLanguage_FeatureDecl.__init__)


def test_devicemodelinglanguage_featuredecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_FeatureDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_typedecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_TypeDecl)


def test_devicemodelinglanguage_typedecl_constructor_exists():
    assert callable(deviceModelingLanguage_TypeDecl.__init__)


def test_devicemodelinglanguage_typedecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_decl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Decl)


def test_devicemodelinglanguage_decl_constructor_exists():
    assert callable(deviceModelingLanguage_Decl.__init__)


def test_devicemodelinglanguage_decl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_decl_has_name():
    assert hasattr(deviceModelingLanguage_Decl, "name")
    descriptor = None
    for klass in deviceModelingLanguage_Decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_model_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Model)


def test_devicemodelinglanguage_model_constructor_exists():
    assert callable(deviceModelingLanguage_Model.__init__)


def test_devicemodelinglanguage_model_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Model.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "product" in params, "Missing parameter 'product'"
    assert "schema" in params, "Missing parameter 'schema'"

def test_devicemodelinglanguage_model_has_class_():
    assert hasattr(deviceModelingLanguage_Model, "class_")
    descriptor = None
    for klass in deviceModelingLanguage_Model.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_model_has_product():
    assert hasattr(deviceModelingLanguage_Model, "product")
    descriptor = None
    for klass in deviceModelingLanguage_Model.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_devicemodelinglanguage_model_has_schema():
    assert hasattr(deviceModelingLanguage_Model, "schema")
    descriptor = None
    for klass in deviceModelingLanguage_Model.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_attrdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_AttrDecl)


def test_devicemodelinglanguage_attrdecl_constructor_exists():
    assert callable(deviceModelingLanguage_AttrDecl.__init__)


def test_devicemodelinglanguage_attrdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_AttrDecl.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_devicemodelinglanguage_attrdecl_has_attributeName():
    assert hasattr(deviceModelingLanguage_AttrDecl, "attributeName")
    descriptor = None
    for klass in deviceModelingLanguage_AttrDecl.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_exp_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Exp)


def test_devicemodelinglanguage_exp_constructor_exists():
    assert callable(deviceModelingLanguage_Exp.__init__)


def test_devicemodelinglanguage_exp_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Exp.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_assignment_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Assignment)


def test_devicemodelinglanguage_assignment_constructor_exists():
    assert callable(deviceModelingLanguage_Assignment.__init__)


def test_devicemodelinglanguage_assignment_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_devicemodelinglanguage_assignment_has_name():
    assert hasattr(deviceModelingLanguage_Assignment, "name")
    descriptor = None
    for klass in deviceModelingLanguage_Assignment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_devicemodelinglanguage_device_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_Device)


def test_devicemodelinglanguage_device_constructor_exists():
    assert callable(deviceModelingLanguage_Device.__init__)


def test_devicemodelinglanguage_device_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_Device.__init__)
    params = list(sig.parameters.keys())



def test_devicemodelinglanguage_memberdecl_is_not_abstract():
    assert not inspect.isabstract(deviceModelingLanguage_MemberDecl)


def test_devicemodelinglanguage_memberdecl_constructor_exists():
    assert callable(deviceModelingLanguage_MemberDecl.__init__)


def test_devicemodelinglanguage_memberdecl_constructor_args():
    sig = inspect.signature(deviceModelingLanguage_MemberDecl.__init__)
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
SimpleOptionLiteral_strategy = st.builds(
    SimpleOptionLiteral,
)
deviceModelingLanguage_SimpleSomeLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleSomeLiteral,
)
deviceModelingLanguage_SimpleNoneLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleNoneLiteral,
)
BaseType_strategy = st.builds(
    BaseType,
)
deviceModelingLanguage_SomeType_strategy = st.builds(
    deviceModelingLanguage_SomeType,
)
deviceModelingLanguage_OptionType_strategy = st.builds(
    deviceModelingLanguage_OptionType,
)
deviceModelingLanguage_TupleType_strategy = st.builds(
    deviceModelingLanguage_TupleType,
)
Primary_strategy = st.builds(
    Primary,
)
deviceModelingLanguage_LiteralExp_strategy = st.builds(
    deviceModelingLanguage_LiteralExp,
)
MModifier_strategy = st.builds(
    MModifier,
)
ConstraintNat_strategy = st.builds(
    ConstraintNat,
)
deviceModelingLanguage_AnyNatConstraint_strategy = st.builds(
    deviceModelingLanguage_AnyNatConstraint,
)
deviceModelingLanguage_NumNatConstraint_strategy = st.builds(
    deviceModelingLanguage_NumNatConstraint,
    num=
        safe_text
)
deviceModelingLanguage_SimpleLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleLiteral,
)
Literal_strategy = st.builds(
    Literal,
)
deviceModelingLanguage_TupleLiteral_strategy = st.builds(
    deviceModelingLanguage_TupleLiteral,
)
deviceModelingLanguage_OptionLiteral_strategy = st.builds(
    deviceModelingLanguage_OptionLiteral,
)
deviceModelingLanguage_SeqLiteral_strategy = st.builds(
    deviceModelingLanguage_SeqLiteral,
)
deviceModelingLanguage_SetLiteral_strategy = st.builds(
    deviceModelingLanguage_SetLiteral,
)
deviceModelingLanguage_BasicLiteral_strategy = st.builds(
    deviceModelingLanguage_BasicLiteral,
    lit=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
deviceModelingLanguage_SetType_strategy = st.builds(
    deviceModelingLanguage_SetType,
)
deviceModelingLanguage_SeqType_strategy = st.builds(
    deviceModelingLanguage_SeqType,
)
deviceModelingLanguage_BaseType_strategy = st.builds(
    deviceModelingLanguage_BaseType,
)
deviceModelingLanguage_Primary_strategy = st.builds(
    deviceModelingLanguage_Primary,
)
deviceModelingLanguage_Accessor_strategy = st.builds(
    deviceModelingLanguage_Accessor,
)
deviceModelingLanguage_ReportMemberDecl_strategy = st.builds(
    deviceModelingLanguage_ReportMemberDecl,
    name=
        safe_text
)
deviceModelingLanguage_Param_strategy = st.builds(
    deviceModelingLanguage_Param,
    name=
        safe_text
)
deviceModelingLanguage_ConstraintExp_strategy = st.builds(
    deviceModelingLanguage_ConstraintExp,
)
deviceModelingLanguage_NameExp_strategy = st.builds(
    deviceModelingLanguage_NameExp,
    id=
        safe_text
)
Exp_strategy = st.builds(
    Exp,
)
deviceModelingLanguage_UnaryExp_strategy = st.builds(
    deviceModelingLanguage_UnaryExp,
    op=
        safe_text
)
deviceModelingLanguage_AccessExp_strategy = st.builds(
    deviceModelingLanguage_AccessExp,
)
deviceModelingLanguage_PrimaryExp_strategy = st.builds(
    deviceModelingLanguage_PrimaryExp,
)
deviceModelingLanguage_BinaryExp_strategy = st.builds(
    deviceModelingLanguage_BinaryExp,
    op=
        safe_text
)
OptionLiteral_strategy = st.builds(
    OptionLiteral,
)
deviceModelingLanguage_SomeLiteral_strategy = st.builds(
    deviceModelingLanguage_SomeLiteral,
)
deviceModelingLanguage_NoneLiteral_strategy = st.builds(
    deviceModelingLanguage_NoneLiteral,
)
deviceModelingLanguage_NoneType_strategy = st.builds(
    deviceModelingLanguage_NoneType,
)
Modifier_strategy = st.builds(
    Modifier,
)
deviceModelingLanguage_Override_strategy = st.builds(
    deviceModelingLanguage_Override,
)
deviceModelingLanguage_Val_strategy = st.builds(
    deviceModelingLanguage_Val,
)
deviceModelingLanguage_Var_strategy = st.builds(
    deviceModelingLanguage_Var,
)
deviceModelingLanguage_Const_strategy = st.builds(
    deviceModelingLanguage_Const,
    class_=
        st.booleans(),
    product=
        st.booleans(),
    instance=
        st.booleans(),
    schema=
        st.booleans()
)
SimpleLiteral_strategy = st.builds(
    SimpleLiteral,
)
deviceModelingLanguage_SimpleSeqLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleSeqLiteral,
)
deviceModelingLanguage_SimpleOptionLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleOptionLiteral,
)
deviceModelingLanguage_SimpleSetLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleSetLiteral,
)
deviceModelingLanguage_SimpleTupleLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleTupleLiteral,
)
deviceModelingLanguage_SimpleBasicLiteral_strategy = st.builds(
    deviceModelingLanguage_SimpleBasicLiteral,
    lit=
        safe_text
)
deviceModelingLanguage_SubMemberMatch_strategy = st.builds(
    deviceModelingLanguage_SubMemberMatch,
    any=
        safe_text,
    qNames=
        safe_text,
    name=
        safe_text
)
deviceModelingLanguage_ConstraintNat_strategy = st.builds(
    deviceModelingLanguage_ConstraintNat,
)
InvariantDecl_strategy = st.builds(
    InvariantDecl,
)
deviceModelingLanguage_MultiplicityInvariant_strategy = st.builds(
    deviceModelingLanguage_MultiplicityInvariant,
)
FeatureType_strategy = st.builds(
    FeatureType,
)
deviceModelingLanguage_SomeFeatureType_strategy = st.builds(
    deviceModelingLanguage_SomeFeatureType,
)
deviceModelingLanguage_EitherFeatureType_strategy = st.builds(
    deviceModelingLanguage_EitherFeatureType,
    choice=
        safe_text
)
deviceModelingLanguage_SetFeatureType_strategy = st.builds(
    deviceModelingLanguage_SetFeatureType,
)
deviceModelingLanguage_OptionFeatureType_strategy = st.builds(
    deviceModelingLanguage_OptionFeatureType,
    none=
        st.booleans()
)
deviceModelingLanguage_SeqFeatureType_strategy = st.builds(
    deviceModelingLanguage_SeqFeatureType,
)
deviceModelingLanguage_BaseFeatureType_strategy = st.builds(
    deviceModelingLanguage_BaseFeatureType,
)
deviceModelingLanguage_Report_strategy = st.builds(
    deviceModelingLanguage_Report,
    name=
        safe_text
)
deviceModelingLanguage_FeatureType_strategy = st.builds(
    deviceModelingLanguage_FeatureType,
)
deviceModelingLanguage_MModifier_strategy = st.builds(
    deviceModelingLanguage_MModifier,
)
deviceModelingLanguage_Literal_strategy = st.builds(
    deviceModelingLanguage_Literal,
)
deviceModelingLanguage_Type_strategy = st.builds(
    deviceModelingLanguage_Type,
)
deviceModelingLanguage_Modifier_strategy = st.builds(
    deviceModelingLanguage_Modifier,
)
Accessor_strategy = st.builds(
    Accessor,
)
MemberDecl_strategy = st.builds(
    MemberDecl,
)
deviceModelingLanguage_InvariantDecl_strategy = st.builds(
    deviceModelingLanguage_InvariantDecl,
    invName=
        safe_text
)
deviceModelingLanguage_SubMemberDecl_strategy = st.builds(
    deviceModelingLanguage_SubMemberDecl,
    name=
        safe_text
)
FeatureDecl_strategy = st.builds(
    FeatureDecl,
)
deviceModelingLanguage_Data_strategy = st.builds(
    deviceModelingLanguage_Data,
)
deviceModelingLanguage_App_strategy = st.builds(
    deviceModelingLanguage_App,
)
deviceModelingLanguage_Feature_strategy = st.builds(
    deviceModelingLanguage_Feature,
    schema=
        st.booleans(),
    class_=
        st.booleans(),
    product=
        st.booleans()
)
deviceModelingLanguage_GeneralInvariant_strategy = st.builds(
    deviceModelingLanguage_GeneralInvariant,
)
Decl_strategy = st.builds(
    Decl,
)
deviceModelingLanguage_FeatureDecl_strategy = st.builds(
    deviceModelingLanguage_FeatureDecl,
)
deviceModelingLanguage_TypeDecl_strategy = st.builds(
    deviceModelingLanguage_TypeDecl,
)
deviceModelingLanguage_Decl_strategy = st.builds(
    deviceModelingLanguage_Decl,
    name=
        safe_text
)
deviceModelingLanguage_Model_strategy = st.builds(
    deviceModelingLanguage_Model,
    class_=
        st.booleans(),
    product=
        st.booleans(),
    schema=
        st.booleans()
)
deviceModelingLanguage_AttrDecl_strategy = st.builds(
    deviceModelingLanguage_AttrDecl,
    attributeName=
        safe_text
)
deviceModelingLanguage_Exp_strategy = st.builds(
    deviceModelingLanguage_Exp,
)
deviceModelingLanguage_Assignment_strategy = st.builds(
    deviceModelingLanguage_Assignment,
    name=
        safe_text
)
deviceModelingLanguage_Device_strategy = st.builds(
    deviceModelingLanguage_Device,
)
deviceModelingLanguage_MemberDecl_strategy = st.builds(
    deviceModelingLanguage_MemberDecl,
)

@given(instance=SimpleOptionLiteral_strategy)
@settings(max_examples=50)
def test_simpleoptionliteral_instantiation(instance):
    assert isinstance(instance, SimpleOptionLiteral)

@given(instance=deviceModelingLanguage_SimpleSomeLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simplesomeliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleSomeLiteral)

@given(instance=deviceModelingLanguage_SimpleNoneLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simplenoneliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleNoneLiteral)

@given(instance=BaseType_strategy)
@settings(max_examples=50)
def test_basetype_instantiation(instance):
    assert isinstance(instance, BaseType)

@given(instance=deviceModelingLanguage_SomeType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_sometype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SomeType)

@given(instance=deviceModelingLanguage_OptionType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_optiontype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_OptionType)

@given(instance=deviceModelingLanguage_TupleType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_tupletype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_TupleType)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=deviceModelingLanguage_LiteralExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_literalexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_LiteralExp)

@given(instance=MModifier_strategy)
@settings(max_examples=50)
def test_mmodifier_instantiation(instance):
    assert isinstance(instance, MModifier)

@given(instance=ConstraintNat_strategy)
@settings(max_examples=50)
def test_constraintnat_instantiation(instance):
    assert isinstance(instance, ConstraintNat)

@given(instance=deviceModelingLanguage_AnyNatConstraint_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_anynatconstraint_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_AnyNatConstraint)

@given(instance=deviceModelingLanguage_NumNatConstraint_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_numnatconstraint_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_NumNatConstraint)



@given(instance=deviceModelingLanguage_NumNatConstraint_strategy)
def test_devicemodelinglanguage_numnatconstraint_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=deviceModelingLanguage_SimpleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simpleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleLiteral)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=deviceModelingLanguage_TupleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_tupleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_TupleLiteral)

@given(instance=deviceModelingLanguage_OptionLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_optionliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_OptionLiteral)

@given(instance=deviceModelingLanguage_SeqLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_seqliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SeqLiteral)

@given(instance=deviceModelingLanguage_SetLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_setliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SetLiteral)

@given(instance=deviceModelingLanguage_BasicLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_basicliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_BasicLiteral)



@given(instance=deviceModelingLanguage_BasicLiteral_strategy)
def test_devicemodelinglanguage_basicliteral_lit_setter(instance):
    original = instance.lit
    instance.lit = original
    assert instance.lit == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=deviceModelingLanguage_SetType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_settype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SetType)

@given(instance=deviceModelingLanguage_SeqType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_seqtype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SeqType)

@given(instance=deviceModelingLanguage_BaseType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_basetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_BaseType)

@given(instance=deviceModelingLanguage_Primary_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_primary_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Primary)

@given(instance=deviceModelingLanguage_Accessor_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_accessor_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Accessor)

@given(instance=deviceModelingLanguage_ReportMemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_reportmemberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_ReportMemberDecl)



@given(instance=deviceModelingLanguage_ReportMemberDecl_strategy)
def test_devicemodelinglanguage_reportmemberdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_Param_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_param_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Param)



@given(instance=deviceModelingLanguage_Param_strategy)
def test_devicemodelinglanguage_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_ConstraintExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_constraintexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_ConstraintExp)

@given(instance=deviceModelingLanguage_NameExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_nameexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_NameExp)



@given(instance=deviceModelingLanguage_NameExp_strategy)
def test_devicemodelinglanguage_nameexp_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=deviceModelingLanguage_UnaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_unaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_UnaryExp)



@given(instance=deviceModelingLanguage_UnaryExp_strategy)
def test_devicemodelinglanguage_unaryexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=deviceModelingLanguage_AccessExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_accessexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_AccessExp)

@given(instance=deviceModelingLanguage_PrimaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_primaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_PrimaryExp)

@given(instance=deviceModelingLanguage_BinaryExp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_binaryexp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_BinaryExp)



@given(instance=deviceModelingLanguage_BinaryExp_strategy)
def test_devicemodelinglanguage_binaryexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OptionLiteral_strategy)
@settings(max_examples=50)
def test_optionliteral_instantiation(instance):
    assert isinstance(instance, OptionLiteral)

@given(instance=deviceModelingLanguage_SomeLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_someliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SomeLiteral)

@given(instance=deviceModelingLanguage_NoneLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_noneliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_NoneLiteral)

@given(instance=deviceModelingLanguage_NoneType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_nonetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_NoneType)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=deviceModelingLanguage_Override_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_override_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Override)

@given(instance=deviceModelingLanguage_Val_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_val_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Val)

@given(instance=deviceModelingLanguage_Var_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_var_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Var)

@given(instance=deviceModelingLanguage_Const_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_const_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Const)



@given(instance=deviceModelingLanguage_Const_strategy)
def test_devicemodelinglanguage_const_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=deviceModelingLanguage_Const_strategy)
def test_devicemodelinglanguage_const_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=deviceModelingLanguage_Const_strategy)
def test_devicemodelinglanguage_const_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original



@given(instance=deviceModelingLanguage_Const_strategy)
def test_devicemodelinglanguage_const_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=SimpleLiteral_strategy)
@settings(max_examples=50)
def test_simpleliteral_instantiation(instance):
    assert isinstance(instance, SimpleLiteral)

@given(instance=deviceModelingLanguage_SimpleSeqLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simpleseqliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleSeqLiteral)

@given(instance=deviceModelingLanguage_SimpleOptionLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simpleoptionliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleOptionLiteral)

@given(instance=deviceModelingLanguage_SimpleSetLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simplesetliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleSetLiteral)

@given(instance=deviceModelingLanguage_SimpleTupleLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simpletupleliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleTupleLiteral)

@given(instance=deviceModelingLanguage_SimpleBasicLiteral_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_simplebasicliteral_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SimpleBasicLiteral)



@given(instance=deviceModelingLanguage_SimpleBasicLiteral_strategy)
def test_devicemodelinglanguage_simplebasicliteral_lit_setter(instance):
    original = instance.lit
    instance.lit = original
    assert instance.lit == original

@given(instance=deviceModelingLanguage_SubMemberMatch_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_submembermatch_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SubMemberMatch)



@given(instance=deviceModelingLanguage_SubMemberMatch_strategy)
def test_devicemodelinglanguage_submembermatch_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=deviceModelingLanguage_SubMemberMatch_strategy)
def test_devicemodelinglanguage_submembermatch_qNames_setter(instance):
    original = instance.qNames
    instance.qNames = original
    assert instance.qNames == original



@given(instance=deviceModelingLanguage_SubMemberMatch_strategy)
def test_devicemodelinglanguage_submembermatch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_ConstraintNat_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_constraintnat_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_ConstraintNat)

@given(instance=InvariantDecl_strategy)
@settings(max_examples=50)
def test_invariantdecl_instantiation(instance):
    assert isinstance(instance, InvariantDecl)

@given(instance=deviceModelingLanguage_MultiplicityInvariant_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_multiplicityinvariant_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_MultiplicityInvariant)

@given(instance=FeatureType_strategy)
@settings(max_examples=50)
def test_featuretype_instantiation(instance):
    assert isinstance(instance, FeatureType)

@given(instance=deviceModelingLanguage_SomeFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_somefeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SomeFeatureType)

@given(instance=deviceModelingLanguage_EitherFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_eitherfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_EitherFeatureType)



@given(instance=deviceModelingLanguage_EitherFeatureType_strategy)
def test_devicemodelinglanguage_eitherfeaturetype_choice_setter(instance):
    original = instance.choice
    instance.choice = original
    assert instance.choice == original

@given(instance=deviceModelingLanguage_SetFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_setfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SetFeatureType)

@given(instance=deviceModelingLanguage_OptionFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_optionfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_OptionFeatureType)



@given(instance=deviceModelingLanguage_OptionFeatureType_strategy)
def test_devicemodelinglanguage_optionfeaturetype_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original

@given(instance=deviceModelingLanguage_SeqFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_seqfeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SeqFeatureType)

@given(instance=deviceModelingLanguage_BaseFeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_basefeaturetype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_BaseFeatureType)

@given(instance=deviceModelingLanguage_Report_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_report_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Report)



@given(instance=deviceModelingLanguage_Report_strategy)
def test_devicemodelinglanguage_report_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_FeatureType_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_featuretype_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_FeatureType)

@given(instance=deviceModelingLanguage_MModifier_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_mmodifier_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_MModifier)

@given(instance=deviceModelingLanguage_Literal_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_literal_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Literal)

@given(instance=deviceModelingLanguage_Type_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_type_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Type)

@given(instance=deviceModelingLanguage_Modifier_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_modifier_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Modifier)

@given(instance=Accessor_strategy)
@settings(max_examples=50)
def test_accessor_instantiation(instance):
    assert isinstance(instance, Accessor)

@given(instance=MemberDecl_strategy)
@settings(max_examples=50)
def test_memberdecl_instantiation(instance):
    assert isinstance(instance, MemberDecl)

@given(instance=deviceModelingLanguage_InvariantDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_invariantdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_InvariantDecl)



@given(instance=deviceModelingLanguage_InvariantDecl_strategy)
def test_devicemodelinglanguage_invariantdecl_invName_setter(instance):
    original = instance.invName
    instance.invName = original
    assert instance.invName == original

@given(instance=deviceModelingLanguage_SubMemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_submemberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_SubMemberDecl)



@given(instance=deviceModelingLanguage_SubMemberDecl_strategy)
def test_devicemodelinglanguage_submemberdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FeatureDecl_strategy)
@settings(max_examples=50)
def test_featuredecl_instantiation(instance):
    assert isinstance(instance, FeatureDecl)

@given(instance=deviceModelingLanguage_Data_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_data_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Data)

@given(instance=deviceModelingLanguage_App_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_app_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_App)

@given(instance=deviceModelingLanguage_Feature_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_feature_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Feature)



@given(instance=deviceModelingLanguage_Feature_strategy)
def test_devicemodelinglanguage_feature_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=deviceModelingLanguage_Feature_strategy)
def test_devicemodelinglanguage_feature_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=deviceModelingLanguage_Feature_strategy)
def test_devicemodelinglanguage_feature_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original

@given(instance=deviceModelingLanguage_GeneralInvariant_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_generalinvariant_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_GeneralInvariant)

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=deviceModelingLanguage_FeatureDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_featuredecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_FeatureDecl)

@given(instance=deviceModelingLanguage_TypeDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_typedecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_TypeDecl)

@given(instance=deviceModelingLanguage_Decl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_decl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Decl)



@given(instance=deviceModelingLanguage_Decl_strategy)
def test_devicemodelinglanguage_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_Model_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_model_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Model)



@given(instance=deviceModelingLanguage_Model_strategy)
def test_devicemodelinglanguage_model_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=deviceModelingLanguage_Model_strategy)
def test_devicemodelinglanguage_model_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=deviceModelingLanguage_Model_strategy)
def test_devicemodelinglanguage_model_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=deviceModelingLanguage_AttrDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_attrdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_AttrDecl)



@given(instance=deviceModelingLanguage_AttrDecl_strategy)
def test_devicemodelinglanguage_attrdecl_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=deviceModelingLanguage_Exp_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_exp_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Exp)

@given(instance=deviceModelingLanguage_Assignment_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_assignment_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Assignment)



@given(instance=deviceModelingLanguage_Assignment_strategy)
def test_devicemodelinglanguage_assignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=deviceModelingLanguage_Device_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_device_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_Device)

@given(instance=deviceModelingLanguage_MemberDecl_strategy)
@settings(max_examples=50)
def test_devicemodelinglanguage_memberdecl_instantiation(instance):
    assert isinstance(instance, deviceModelingLanguage_MemberDecl)

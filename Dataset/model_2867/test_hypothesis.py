import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fiacre_Variable,
    fiacre_MaxBound,
    fiacre_MinBound,
    Exp,
    fiacre_ArrayElem,
    fiacre_BinExp,
    fiacre_RecordElem,
    fiacre_UnExp,
    fiacre_Pattern,
    fiacre_SingleAssignment,
    Assignment,
    fiacre_NonDeterministicAssignment,
    fiacre_DeterministicAssignment,
    fiacre_InlineCollection,
    fiacre_CondExp,
    MaxBound,
    fiacre_InfiniteBound,
    MinBound,
    fiacre_FiniteBound,
    fiacre_LabeledType,
    fiacre_ConstrExp,
    fiacre_Rule,
    Channel,
    fiacre_Profile,
    PortDecl,
    Communication,
    fiacre_Emission,
    fiacre_Reception,
    fiacre_Synchronization,
    fiacre_ValuedField,
    fiacre_InlineRecord,
    Pattern,
    fiacre_Literal,
    fiacre_ConstrPattern,
    fiacre_AnyPattern,
    fiacre_ConstantRef,
    fiacre_FieldPattern,
    fiacre_ArrayPattern,
    fiacre_VarRef,
    Literal,
    fiacre_BoolLiteral,
    fiacre_NatLiteral,
    LabeledType,
    fiacre_Constr,
    fiacre_Field,
    BasicType,
    fiacre_IntType,
    fiacre_NatType,
    fiacre_BoolType,
    Type,
    fiacre_Array,
    fiacre_TypeId,
    fiacre_Union,
    fiacre_Record,
    fiacre_Queue,
    fiacre_Interval,
    fiacre_BasicType,
    InlineCollection,
    fiacre_InlineArray,
    fiacre_InlineQueue,
    fiacre_InterfacedComp,
    Composition,
    fiacre_Instance,
    fiacre_Par,
    Statement,
    fiacre_To,
    fiacre_Select,
    fiacre_Wait,
    fiacre_Seq,
    fiacre_Assignment,
    fiacre_IfStmt,
    fiacre_WhileStmt,
    fiacre_Foreach,
    fiacre_CaseStmt,
    fiacre_Communication,
    fiacre_NullStmt,
    Arg,
    fiacre_Exp,
    fiacre_RefArg,
    fiacre_Arg,
    Declaration,
    fiacre_ConstantDecl,
    fiacre_NodeDecl,
    fiacre_Declaration,
    Variable,
    fiacre_ArgumentVariable,
    fiacre_PortDecl,
    fiacre_Transition,
    fiacre_State,
    fiacre_Priority,
    fiacre_Composition,
    NodeDecl,
    fiacre_ProcessDecl,
    fiacre_ComponentDecl,
    fiacre_Channel,
    fiacre_ChannelDecl,
    fiacre_Type,
    fiacre_TypeDecl,
    fiacre_Statement,
    fiacre_LocalPortDecl,
    fiacre_ParamPortDecl,
    fiacre_LocalVariable,
    fiacre_Program,
    UnOp,
    BinOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fiacre_variable_is_not_abstract():
    assert not inspect.isabstract(fiacre_Variable)


def test_fiacre_variable_constructor_exists():
    assert callable(fiacre_Variable.__init__)


def test_fiacre_variable_constructor_args():
    sig = inspect.signature(fiacre_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_variable_has_name():
    assert hasattr(fiacre_Variable, "name")
    descriptor = None
    for klass in fiacre_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_maxbound_is_not_abstract():
    assert not inspect.isabstract(fiacre_MaxBound)


def test_fiacre_maxbound_constructor_exists():
    assert callable(fiacre_MaxBound.__init__)


def test_fiacre_maxbound_constructor_args():
    sig = inspect.signature(fiacre_MaxBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_minbound_is_not_abstract():
    assert not inspect.isabstract(fiacre_MinBound)


def test_fiacre_minbound_constructor_exists():
    assert callable(fiacre_MinBound.__init__)


def test_fiacre_minbound_constructor_args():
    sig = inspect.signature(fiacre_MinBound.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_arrayelem_is_not_abstract():
    assert not inspect.isabstract(fiacre_ArrayElem)


def test_fiacre_arrayelem_constructor_exists():
    assert callable(fiacre_ArrayElem.__init__)


def test_fiacre_arrayelem_constructor_args():
    sig = inspect.signature(fiacre_ArrayElem.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_binexp_is_not_abstract():
    assert not inspect.isabstract(fiacre_BinExp)


def test_fiacre_binexp_constructor_exists():
    assert callable(fiacre_BinExp.__init__)


def test_fiacre_binexp_constructor_args():
    sig = inspect.signature(fiacre_BinExp.__init__)
    params = list(sig.parameters.keys())
    assert "binOp" in params, "Missing parameter 'binOp'"

def test_fiacre_binexp_has_binOp():
    assert hasattr(fiacre_BinExp, "binOp")
    descriptor = None
    for klass in fiacre_BinExp.__mro__:
        if "binOp" in klass.__dict__:
            descriptor = klass.__dict__["binOp"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_recordelem_is_not_abstract():
    assert not inspect.isabstract(fiacre_RecordElem)


def test_fiacre_recordelem_constructor_exists():
    assert callable(fiacre_RecordElem.__init__)


def test_fiacre_recordelem_constructor_args():
    sig = inspect.signature(fiacre_RecordElem.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre_recordelem_has_field():
    assert hasattr(fiacre_RecordElem, "field")
    descriptor = None
    for klass in fiacre_RecordElem.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_unexp_is_not_abstract():
    assert not inspect.isabstract(fiacre_UnExp)


def test_fiacre_unexp_constructor_exists():
    assert callable(fiacre_UnExp.__init__)


def test_fiacre_unexp_constructor_args():
    sig = inspect.signature(fiacre_UnExp.__init__)
    params = list(sig.parameters.keys())
    assert "unop" in params, "Missing parameter 'unop'"

def test_fiacre_unexp_has_unop():
    assert hasattr(fiacre_UnExp, "unop")
    descriptor = None
    for klass in fiacre_UnExp.__mro__:
        if "unop" in klass.__dict__:
            descriptor = klass.__dict__["unop"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_pattern_is_not_abstract():
    assert not inspect.isabstract(fiacre_Pattern)


def test_fiacre_pattern_constructor_exists():
    assert callable(fiacre_Pattern.__init__)


def test_fiacre_pattern_constructor_args():
    sig = inspect.signature(fiacre_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_singleassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre_SingleAssignment)


def test_fiacre_singleassignment_constructor_exists():
    assert callable(fiacre_SingleAssignment.__init__)


def test_fiacre_singleassignment_constructor_args():
    sig = inspect.signature(fiacre_SingleAssignment.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_nondeterministicassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre_NonDeterministicAssignment)


def test_fiacre_nondeterministicassignment_constructor_exists():
    assert callable(fiacre_NonDeterministicAssignment.__init__)


def test_fiacre_nondeterministicassignment_constructor_args():
    sig = inspect.signature(fiacre_NonDeterministicAssignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_deterministicassignment_is_not_abstract():
    assert not inspect.isabstract(fiacre_DeterministicAssignment)


def test_fiacre_deterministicassignment_constructor_exists():
    assert callable(fiacre_DeterministicAssignment.__init__)


def test_fiacre_deterministicassignment_constructor_args():
    sig = inspect.signature(fiacre_DeterministicAssignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_inlinecollection_is_not_abstract():
    assert not inspect.isabstract(fiacre_InlineCollection)


def test_fiacre_inlinecollection_constructor_exists():
    assert callable(fiacre_InlineCollection.__init__)


def test_fiacre_inlinecollection_constructor_args():
    sig = inspect.signature(fiacre_InlineCollection.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_condexp_is_not_abstract():
    assert not inspect.isabstract(fiacre_CondExp)


def test_fiacre_condexp_constructor_exists():
    assert callable(fiacre_CondExp.__init__)


def test_fiacre_condexp_constructor_args():
    sig = inspect.signature(fiacre_CondExp.__init__)
    params = list(sig.parameters.keys())



def test_maxbound_is_not_abstract():
    assert not inspect.isabstract(MaxBound)


def test_maxbound_constructor_exists():
    assert callable(MaxBound.__init__)


def test_maxbound_constructor_args():
    sig = inspect.signature(MaxBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_infinitebound_is_not_abstract():
    assert not inspect.isabstract(fiacre_InfiniteBound)


def test_fiacre_infinitebound_constructor_exists():
    assert callable(fiacre_InfiniteBound.__init__)


def test_fiacre_infinitebound_constructor_args():
    sig = inspect.signature(fiacre_InfiniteBound.__init__)
    params = list(sig.parameters.keys())



def test_minbound_is_not_abstract():
    assert not inspect.isabstract(MinBound)


def test_minbound_constructor_exists():
    assert callable(MinBound.__init__)


def test_minbound_constructor_args():
    sig = inspect.signature(MinBound.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_finitebound_is_not_abstract():
    assert not inspect.isabstract(fiacre_FiniteBound)


def test_fiacre_finitebound_constructor_exists():
    assert callable(fiacre_FiniteBound.__init__)


def test_fiacre_finitebound_constructor_args():
    sig = inspect.signature(fiacre_FiniteBound.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"
    assert "val" in params, "Missing parameter 'val'"

def test_fiacre_finitebound_has_strict():
    assert hasattr(fiacre_FiniteBound, "strict")
    descriptor = None
    for klass in fiacre_FiniteBound.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_fiacre_finitebound_has_val():
    assert hasattr(fiacre_FiniteBound, "val")
    descriptor = None
    for klass in fiacre_FiniteBound.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_labeledtype_is_not_abstract():
    assert not inspect.isabstract(fiacre_LabeledType)


def test_fiacre_labeledtype_constructor_exists():
    assert callable(fiacre_LabeledType.__init__)


def test_fiacre_labeledtype_constructor_args():
    sig = inspect.signature(fiacre_LabeledType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_labeledtype_has_name():
    assert hasattr(fiacre_LabeledType, "name")
    descriptor = None
    for klass in fiacre_LabeledType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_constrexp_is_not_abstract():
    assert not inspect.isabstract(fiacre_ConstrExp)


def test_fiacre_constrexp_constructor_exists():
    assert callable(fiacre_ConstrExp.__init__)


def test_fiacre_constrexp_constructor_args():
    sig = inspect.signature(fiacre_ConstrExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_constrexp_has_name():
    assert hasattr(fiacre_ConstrExp, "name")
    descriptor = None
    for klass in fiacre_ConstrExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_rule_is_not_abstract():
    assert not inspect.isabstract(fiacre_Rule)


def test_fiacre_rule_constructor_exists():
    assert callable(fiacre_Rule.__init__)


def test_fiacre_rule_constructor_args():
    sig = inspect.signature(fiacre_Rule.__init__)
    params = list(sig.parameters.keys())



def test_channel_is_not_abstract():
    assert not inspect.isabstract(Channel)


def test_channel_constructor_exists():
    assert callable(Channel.__init__)


def test_channel_constructor_args():
    sig = inspect.signature(Channel.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_profile_is_not_abstract():
    assert not inspect.isabstract(fiacre_Profile)


def test_fiacre_profile_constructor_exists():
    assert callable(fiacre_Profile.__init__)


def test_fiacre_profile_constructor_args():
    sig = inspect.signature(fiacre_Profile.__init__)
    params = list(sig.parameters.keys())



def test_portdecl_is_not_abstract():
    assert not inspect.isabstract(PortDecl)


def test_portdecl_constructor_exists():
    assert callable(PortDecl.__init__)


def test_portdecl_constructor_args():
    sig = inspect.signature(PortDecl.__init__)
    params = list(sig.parameters.keys())



def test_communication_is_not_abstract():
    assert not inspect.isabstract(Communication)


def test_communication_constructor_exists():
    assert callable(Communication.__init__)


def test_communication_constructor_args():
    sig = inspect.signature(Communication.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_emission_is_not_abstract():
    assert not inspect.isabstract(fiacre_Emission)


def test_fiacre_emission_constructor_exists():
    assert callable(fiacre_Emission.__init__)


def test_fiacre_emission_constructor_args():
    sig = inspect.signature(fiacre_Emission.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_reception_is_not_abstract():
    assert not inspect.isabstract(fiacre_Reception)


def test_fiacre_reception_constructor_exists():
    assert callable(fiacre_Reception.__init__)


def test_fiacre_reception_constructor_args():
    sig = inspect.signature(fiacre_Reception.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_synchronization_is_not_abstract():
    assert not inspect.isabstract(fiacre_Synchronization)


def test_fiacre_synchronization_constructor_exists():
    assert callable(fiacre_Synchronization.__init__)


def test_fiacre_synchronization_constructor_args():
    sig = inspect.signature(fiacre_Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_valuedfield_is_not_abstract():
    assert not inspect.isabstract(fiacre_ValuedField)


def test_fiacre_valuedfield_constructor_exists():
    assert callable(fiacre_ValuedField.__init__)


def test_fiacre_valuedfield_constructor_args():
    sig = inspect.signature(fiacre_ValuedField.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre_valuedfield_has_field():
    assert hasattr(fiacre_ValuedField, "field")
    descriptor = None
    for klass in fiacre_ValuedField.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_inlinerecord_is_not_abstract():
    assert not inspect.isabstract(fiacre_InlineRecord)


def test_fiacre_inlinerecord_constructor_exists():
    assert callable(fiacre_InlineRecord.__init__)


def test_fiacre_inlinerecord_constructor_args():
    sig = inspect.signature(fiacre_InlineRecord.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_literal_is_not_abstract():
    assert not inspect.isabstract(fiacre_Literal)


def test_fiacre_literal_constructor_exists():
    assert callable(fiacre_Literal.__init__)


def test_fiacre_literal_constructor_args():
    sig = inspect.signature(fiacre_Literal.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_constrpattern_is_not_abstract():
    assert not inspect.isabstract(fiacre_ConstrPattern)


def test_fiacre_constrpattern_constructor_exists():
    assert callable(fiacre_ConstrPattern.__init__)


def test_fiacre_constrpattern_constructor_args():
    sig = inspect.signature(fiacre_ConstrPattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_constrpattern_has_name():
    assert hasattr(fiacre_ConstrPattern, "name")
    descriptor = None
    for klass in fiacre_ConstrPattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_anypattern_is_not_abstract():
    assert not inspect.isabstract(fiacre_AnyPattern)


def test_fiacre_anypattern_constructor_exists():
    assert callable(fiacre_AnyPattern.__init__)


def test_fiacre_anypattern_constructor_args():
    sig = inspect.signature(fiacre_AnyPattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_constantref_is_not_abstract():
    assert not inspect.isabstract(fiacre_ConstantRef)


def test_fiacre_constantref_constructor_exists():
    assert callable(fiacre_ConstantRef.__init__)


def test_fiacre_constantref_constructor_args():
    sig = inspect.signature(fiacre_ConstantRef.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_fieldpattern_is_not_abstract():
    assert not inspect.isabstract(fiacre_FieldPattern)


def test_fiacre_fieldpattern_constructor_exists():
    assert callable(fiacre_FieldPattern.__init__)


def test_fiacre_fieldpattern_constructor_args():
    sig = inspect.signature(fiacre_FieldPattern.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_fiacre_fieldpattern_has_field():
    assert hasattr(fiacre_FieldPattern, "field")
    descriptor = None
    for klass in fiacre_FieldPattern.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_arraypattern_is_not_abstract():
    assert not inspect.isabstract(fiacre_ArrayPattern)


def test_fiacre_arraypattern_constructor_exists():
    assert callable(fiacre_ArrayPattern.__init__)


def test_fiacre_arraypattern_constructor_args():
    sig = inspect.signature(fiacre_ArrayPattern.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_varref_is_not_abstract():
    assert not inspect.isabstract(fiacre_VarRef)


def test_fiacre_varref_constructor_exists():
    assert callable(fiacre_VarRef.__init__)


def test_fiacre_varref_constructor_args():
    sig = inspect.signature(fiacre_VarRef.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_boolliteral_is_not_abstract():
    assert not inspect.isabstract(fiacre_BoolLiteral)


def test_fiacre_boolliteral_constructor_exists():
    assert callable(fiacre_BoolLiteral.__init__)


def test_fiacre_boolliteral_constructor_args():
    sig = inspect.signature(fiacre_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fiacre_boolliteral_has_value():
    assert hasattr(fiacre_BoolLiteral, "value")
    descriptor = None
    for klass in fiacre_BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_natliteral_is_not_abstract():
    assert not inspect.isabstract(fiacre_NatLiteral)


def test_fiacre_natliteral_constructor_exists():
    assert callable(fiacre_NatLiteral.__init__)


def test_fiacre_natliteral_constructor_args():
    sig = inspect.signature(fiacre_NatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fiacre_natliteral_has_value():
    assert hasattr(fiacre_NatLiteral, "value")
    descriptor = None
    for klass in fiacre_NatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_labeledtype_is_not_abstract():
    assert not inspect.isabstract(LabeledType)


def test_labeledtype_constructor_exists():
    assert callable(LabeledType.__init__)


def test_labeledtype_constructor_args():
    sig = inspect.signature(LabeledType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_constr_is_not_abstract():
    assert not inspect.isabstract(fiacre_Constr)


def test_fiacre_constr_constructor_exists():
    assert callable(fiacre_Constr.__init__)


def test_fiacre_constr_constructor_args():
    sig = inspect.signature(fiacre_Constr.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_field_is_not_abstract():
    assert not inspect.isabstract(fiacre_Field)


def test_fiacre_field_constructor_exists():
    assert callable(fiacre_Field.__init__)


def test_fiacre_field_constructor_args():
    sig = inspect.signature(fiacre_Field.__init__)
    params = list(sig.parameters.keys())



def test_basictype_is_not_abstract():
    assert not inspect.isabstract(BasicType)


def test_basictype_constructor_exists():
    assert callable(BasicType.__init__)


def test_basictype_constructor_args():
    sig = inspect.signature(BasicType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_inttype_is_not_abstract():
    assert not inspect.isabstract(fiacre_IntType)


def test_fiacre_inttype_constructor_exists():
    assert callable(fiacre_IntType.__init__)


def test_fiacre_inttype_constructor_args():
    sig = inspect.signature(fiacre_IntType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_nattype_is_not_abstract():
    assert not inspect.isabstract(fiacre_NatType)


def test_fiacre_nattype_constructor_exists():
    assert callable(fiacre_NatType.__init__)


def test_fiacre_nattype_constructor_args():
    sig = inspect.signature(fiacre_NatType.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_booltype_is_not_abstract():
    assert not inspect.isabstract(fiacre_BoolType)


def test_fiacre_booltype_constructor_exists():
    assert callable(fiacre_BoolType.__init__)


def test_fiacre_booltype_constructor_args():
    sig = inspect.signature(fiacre_BoolType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_array_is_not_abstract():
    assert not inspect.isabstract(fiacre_Array)


def test_fiacre_array_constructor_exists():
    assert callable(fiacre_Array.__init__)


def test_fiacre_array_constructor_args():
    sig = inspect.signature(fiacre_Array.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_typeid_is_not_abstract():
    assert not inspect.isabstract(fiacre_TypeId)


def test_fiacre_typeid_constructor_exists():
    assert callable(fiacre_TypeId.__init__)


def test_fiacre_typeid_constructor_args():
    sig = inspect.signature(fiacre_TypeId.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_union_is_not_abstract():
    assert not inspect.isabstract(fiacre_Union)


def test_fiacre_union_constructor_exists():
    assert callable(fiacre_Union.__init__)


def test_fiacre_union_constructor_args():
    sig = inspect.signature(fiacre_Union.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_record_is_not_abstract():
    assert not inspect.isabstract(fiacre_Record)


def test_fiacre_record_constructor_exists():
    assert callable(fiacre_Record.__init__)


def test_fiacre_record_constructor_args():
    sig = inspect.signature(fiacre_Record.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_queue_is_not_abstract():
    assert not inspect.isabstract(fiacre_Queue)


def test_fiacre_queue_constructor_exists():
    assert callable(fiacre_Queue.__init__)


def test_fiacre_queue_constructor_args():
    sig = inspect.signature(fiacre_Queue.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_interval_is_not_abstract():
    assert not inspect.isabstract(fiacre_Interval)


def test_fiacre_interval_constructor_exists():
    assert callable(fiacre_Interval.__init__)


def test_fiacre_interval_constructor_args():
    sig = inspect.signature(fiacre_Interval.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_basictype_is_not_abstract():
    assert not inspect.isabstract(fiacre_BasicType)


def test_fiacre_basictype_constructor_exists():
    assert callable(fiacre_BasicType.__init__)


def test_fiacre_basictype_constructor_args():
    sig = inspect.signature(fiacre_BasicType.__init__)
    params = list(sig.parameters.keys())



def test_inlinecollection_is_not_abstract():
    assert not inspect.isabstract(InlineCollection)


def test_inlinecollection_constructor_exists():
    assert callable(InlineCollection.__init__)


def test_inlinecollection_constructor_args():
    sig = inspect.signature(InlineCollection.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_inlinearray_is_not_abstract():
    assert not inspect.isabstract(fiacre_InlineArray)


def test_fiacre_inlinearray_constructor_exists():
    assert callable(fiacre_InlineArray.__init__)


def test_fiacre_inlinearray_constructor_args():
    sig = inspect.signature(fiacre_InlineArray.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_inlinequeue_is_not_abstract():
    assert not inspect.isabstract(fiacre_InlineQueue)


def test_fiacre_inlinequeue_constructor_exists():
    assert callable(fiacre_InlineQueue.__init__)


def test_fiacre_inlinequeue_constructor_args():
    sig = inspect.signature(fiacre_InlineQueue.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_interfacedcomp_is_not_abstract():
    assert not inspect.isabstract(fiacre_InterfacedComp)


def test_fiacre_interfacedcomp_constructor_exists():
    assert callable(fiacre_InterfacedComp.__init__)


def test_fiacre_interfacedcomp_constructor_args():
    sig = inspect.signature(fiacre_InterfacedComp.__init__)
    params = list(sig.parameters.keys())



def test_composition_is_not_abstract():
    assert not inspect.isabstract(Composition)


def test_composition_constructor_exists():
    assert callable(Composition.__init__)


def test_composition_constructor_args():
    sig = inspect.signature(Composition.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_instance_is_not_abstract():
    assert not inspect.isabstract(fiacre_Instance)


def test_fiacre_instance_constructor_exists():
    assert callable(fiacre_Instance.__init__)


def test_fiacre_instance_constructor_args():
    sig = inspect.signature(fiacre_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_instance_has_name():
    assert hasattr(fiacre_Instance, "name")
    descriptor = None
    for klass in fiacre_Instance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_par_is_not_abstract():
    assert not inspect.isabstract(fiacre_Par)


def test_fiacre_par_constructor_exists():
    assert callable(fiacre_Par.__init__)


def test_fiacre_par_constructor_args():
    sig = inspect.signature(fiacre_Par.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_to_is_not_abstract():
    assert not inspect.isabstract(fiacre_To)


def test_fiacre_to_constructor_exists():
    assert callable(fiacre_To.__init__)


def test_fiacre_to_constructor_args():
    sig = inspect.signature(fiacre_To.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_select_is_not_abstract():
    assert not inspect.isabstract(fiacre_Select)


def test_fiacre_select_constructor_exists():
    assert callable(fiacre_Select.__init__)


def test_fiacre_select_constructor_args():
    sig = inspect.signature(fiacre_Select.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_wait_is_not_abstract():
    assert not inspect.isabstract(fiacre_Wait)


def test_fiacre_wait_constructor_exists():
    assert callable(fiacre_Wait.__init__)


def test_fiacre_wait_constructor_args():
    sig = inspect.signature(fiacre_Wait.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_seq_is_not_abstract():
    assert not inspect.isabstract(fiacre_Seq)


def test_fiacre_seq_constructor_exists():
    assert callable(fiacre_Seq.__init__)


def test_fiacre_seq_constructor_args():
    sig = inspect.signature(fiacre_Seq.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_assignment_is_not_abstract():
    assert not inspect.isabstract(fiacre_Assignment)


def test_fiacre_assignment_constructor_exists():
    assert callable(fiacre_Assignment.__init__)


def test_fiacre_assignment_constructor_args():
    sig = inspect.signature(fiacre_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_ifstmt_is_not_abstract():
    assert not inspect.isabstract(fiacre_IfStmt)


def test_fiacre_ifstmt_constructor_exists():
    assert callable(fiacre_IfStmt.__init__)


def test_fiacre_ifstmt_constructor_args():
    sig = inspect.signature(fiacre_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_whilestmt_is_not_abstract():
    assert not inspect.isabstract(fiacre_WhileStmt)


def test_fiacre_whilestmt_constructor_exists():
    assert callable(fiacre_WhileStmt.__init__)


def test_fiacre_whilestmt_constructor_args():
    sig = inspect.signature(fiacre_WhileStmt.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_foreach_is_not_abstract():
    assert not inspect.isabstract(fiacre_Foreach)


def test_fiacre_foreach_constructor_exists():
    assert callable(fiacre_Foreach.__init__)


def test_fiacre_foreach_constructor_args():
    sig = inspect.signature(fiacre_Foreach.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_casestmt_is_not_abstract():
    assert not inspect.isabstract(fiacre_CaseStmt)


def test_fiacre_casestmt_constructor_exists():
    assert callable(fiacre_CaseStmt.__init__)


def test_fiacre_casestmt_constructor_args():
    sig = inspect.signature(fiacre_CaseStmt.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_communication_is_not_abstract():
    assert not inspect.isabstract(fiacre_Communication)


def test_fiacre_communication_constructor_exists():
    assert callable(fiacre_Communication.__init__)


def test_fiacre_communication_constructor_args():
    sig = inspect.signature(fiacre_Communication.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_nullstmt_is_not_abstract():
    assert not inspect.isabstract(fiacre_NullStmt)


def test_fiacre_nullstmt_constructor_exists():
    assert callable(fiacre_NullStmt.__init__)


def test_fiacre_nullstmt_constructor_args():
    sig = inspect.signature(fiacre_NullStmt.__init__)
    params = list(sig.parameters.keys())



def test_arg_is_not_abstract():
    assert not inspect.isabstract(Arg)


def test_arg_constructor_exists():
    assert callable(Arg.__init__)


def test_arg_constructor_args():
    sig = inspect.signature(Arg.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_exp_is_not_abstract():
    assert not inspect.isabstract(fiacre_Exp)


def test_fiacre_exp_constructor_exists():
    assert callable(fiacre_Exp.__init__)


def test_fiacre_exp_constructor_args():
    sig = inspect.signature(fiacre_Exp.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_refarg_is_not_abstract():
    assert not inspect.isabstract(fiacre_RefArg)


def test_fiacre_refarg_constructor_exists():
    assert callable(fiacre_RefArg.__init__)


def test_fiacre_refarg_constructor_args():
    sig = inspect.signature(fiacre_RefArg.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_arg_is_not_abstract():
    assert not inspect.isabstract(fiacre_Arg)


def test_fiacre_arg_constructor_exists():
    assert callable(fiacre_Arg.__init__)


def test_fiacre_arg_constructor_args():
    sig = inspect.signature(fiacre_Arg.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_constantdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_ConstantDecl)


def test_fiacre_constantdecl_constructor_exists():
    assert callable(fiacre_ConstantDecl.__init__)


def test_fiacre_constantdecl_constructor_args():
    sig = inspect.signature(fiacre_ConstantDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_nodedecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_NodeDecl)


def test_fiacre_nodedecl_constructor_exists():
    assert callable(fiacre_NodeDecl.__init__)


def test_fiacre_nodedecl_constructor_args():
    sig = inspect.signature(fiacre_NodeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_declaration_is_not_abstract():
    assert not inspect.isabstract(fiacre_Declaration)


def test_fiacre_declaration_constructor_exists():
    assert callable(fiacre_Declaration.__init__)


def test_fiacre_declaration_constructor_args():
    sig = inspect.signature(fiacre_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_declaration_has_name():
    assert hasattr(fiacre_Declaration, "name")
    descriptor = None
    for klass in fiacre_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_argumentvariable_is_not_abstract():
    assert not inspect.isabstract(fiacre_ArgumentVariable)


def test_fiacre_argumentvariable_constructor_exists():
    assert callable(fiacre_ArgumentVariable.__init__)


def test_fiacre_argumentvariable_constructor_args():
    sig = inspect.signature(fiacre_ArgumentVariable.__init__)
    params = list(sig.parameters.keys())
    assert "read" in params, "Missing parameter 'read'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "write" in params, "Missing parameter 'write'"

def test_fiacre_argumentvariable_has_read():
    assert hasattr(fiacre_ArgumentVariable, "read")
    descriptor = None
    for klass in fiacre_ArgumentVariable.__mro__:
        if "read" in klass.__dict__:
            descriptor = klass.__dict__["read"]
            break
    assert isinstance(descriptor, property)

def test_fiacre_argumentvariable_has_ref():
    assert hasattr(fiacre_ArgumentVariable, "ref")
    descriptor = None
    for klass in fiacre_ArgumentVariable.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_fiacre_argumentvariable_has_write():
    assert hasattr(fiacre_ArgumentVariable, "write")
    descriptor = None
    for klass in fiacre_ArgumentVariable.__mro__:
        if "write" in klass.__dict__:
            descriptor = klass.__dict__["write"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_portdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_PortDecl)


def test_fiacre_portdecl_constructor_exists():
    assert callable(fiacre_PortDecl.__init__)


def test_fiacre_portdecl_constructor_args():
    sig = inspect.signature(fiacre_PortDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_fiacre_portdecl_has_name():
    assert hasattr(fiacre_PortDecl, "name")
    descriptor = None
    for klass in fiacre_PortDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fiacre_portdecl_has_out():
    assert hasattr(fiacre_PortDecl, "out")
    descriptor = None
    for klass in fiacre_PortDecl.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_fiacre_portdecl_has_in_():
    assert hasattr(fiacre_PortDecl, "in_")
    descriptor = None
    for klass in fiacre_PortDecl.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_transition_is_not_abstract():
    assert not inspect.isabstract(fiacre_Transition)


def test_fiacre_transition_constructor_exists():
    assert callable(fiacre_Transition.__init__)


def test_fiacre_transition_constructor_args():
    sig = inspect.signature(fiacre_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_transition_has_name():
    assert hasattr(fiacre_Transition, "name")
    descriptor = None
    for klass in fiacre_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_state_is_not_abstract():
    assert not inspect.isabstract(fiacre_State)


def test_fiacre_state_constructor_exists():
    assert callable(fiacre_State.__init__)


def test_fiacre_state_constructor_args():
    sig = inspect.signature(fiacre_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fiacre_state_has_name():
    assert hasattr(fiacre_State, "name")
    descriptor = None
    for klass in fiacre_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_priority_is_not_abstract():
    assert not inspect.isabstract(fiacre_Priority)


def test_fiacre_priority_constructor_exists():
    assert callable(fiacre_Priority.__init__)


def test_fiacre_priority_constructor_args():
    sig = inspect.signature(fiacre_Priority.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_composition_is_not_abstract():
    assert not inspect.isabstract(fiacre_Composition)


def test_fiacre_composition_constructor_exists():
    assert callable(fiacre_Composition.__init__)


def test_fiacre_composition_constructor_args():
    sig = inspect.signature(fiacre_Composition.__init__)
    params = list(sig.parameters.keys())



def test_nodedecl_is_not_abstract():
    assert not inspect.isabstract(NodeDecl)


def test_nodedecl_constructor_exists():
    assert callable(NodeDecl.__init__)


def test_nodedecl_constructor_args():
    sig = inspect.signature(NodeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_processdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_ProcessDecl)


def test_fiacre_processdecl_constructor_exists():
    assert callable(fiacre_ProcessDecl.__init__)


def test_fiacre_processdecl_constructor_args():
    sig = inspect.signature(fiacre_ProcessDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_componentdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_ComponentDecl)


def test_fiacre_componentdecl_constructor_exists():
    assert callable(fiacre_ComponentDecl.__init__)


def test_fiacre_componentdecl_constructor_args():
    sig = inspect.signature(fiacre_ComponentDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_channel_is_not_abstract():
    assert not inspect.isabstract(fiacre_Channel)


def test_fiacre_channel_constructor_exists():
    assert callable(fiacre_Channel.__init__)


def test_fiacre_channel_constructor_args():
    sig = inspect.signature(fiacre_Channel.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_channeldecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_ChannelDecl)


def test_fiacre_channeldecl_constructor_exists():
    assert callable(fiacre_ChannelDecl.__init__)


def test_fiacre_channeldecl_constructor_args():
    sig = inspect.signature(fiacre_ChannelDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_type_is_not_abstract():
    assert not inspect.isabstract(fiacre_Type)


def test_fiacre_type_constructor_exists():
    assert callable(fiacre_Type.__init__)


def test_fiacre_type_constructor_args():
    sig = inspect.signature(fiacre_Type.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_typedecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_TypeDecl)


def test_fiacre_typedecl_constructor_exists():
    assert callable(fiacre_TypeDecl.__init__)


def test_fiacre_typedecl_constructor_args():
    sig = inspect.signature(fiacre_TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_statement_is_not_abstract():
    assert not inspect.isabstract(fiacre_Statement)


def test_fiacre_statement_constructor_exists():
    assert callable(fiacre_Statement.__init__)


def test_fiacre_statement_constructor_args():
    sig = inspect.signature(fiacre_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_fiacre_statement_has_comment():
    assert hasattr(fiacre_Statement, "comment")
    descriptor = None
    for klass in fiacre_Statement.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_localportdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_LocalPortDecl)


def test_fiacre_localportdecl_constructor_exists():
    assert callable(fiacre_LocalPortDecl.__init__)


def test_fiacre_localportdecl_constructor_args():
    sig = inspect.signature(fiacre_LocalPortDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_paramportdecl_is_not_abstract():
    assert not inspect.isabstract(fiacre_ParamPortDecl)


def test_fiacre_paramportdecl_constructor_exists():
    assert callable(fiacre_ParamPortDecl.__init__)


def test_fiacre_paramportdecl_constructor_args():
    sig = inspect.signature(fiacre_ParamPortDecl.__init__)
    params = list(sig.parameters.keys())



def test_fiacre_localvariable_is_not_abstract():
    assert not inspect.isabstract(fiacre_LocalVariable)


def test_fiacre_localvariable_constructor_exists():
    assert callable(fiacre_LocalVariable.__init__)


def test_fiacre_localvariable_constructor_args():
    sig = inspect.signature(fiacre_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_fiacre_localvariable_has_constant():
    assert hasattr(fiacre_LocalVariable, "constant")
    descriptor = None
    for klass in fiacre_LocalVariable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_fiacre_program_is_not_abstract():
    assert not inspect.isabstract(fiacre_Program)


def test_fiacre_program_constructor_exists():
    assert callable(fiacre_Program.__init__)


def test_fiacre_program_constructor_args():
    sig = inspect.signature(fiacre_Program.__init__)
    params = list(sig.parameters.keys())

def test_unop_exists():
    # Check that the Enumeration exists
    assert UnOp is not None

def test_unop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnOp]
    expected_literals = [
        "DEQUEUE",
        "UEMPTY",
        "UMINUS",
        "UFULL",
        "UDOLLAR",
        "UNOT",
        "FIRST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnOp"

def test_binop_exists():
    # Check that the Enumeration exists
    assert BinOp is not None

def test_binop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinOp]
    expected_literals = [
        "BADD",
        "BMUL",
        "BMOD",
        "BOR",
        "BGT",
        "BDIV",
        "APPEND",
        "BLT",
        "BNE",
        "BGE",
        "BMINUS",
        "ENQUEUE",
        "BLE",
        "BAND",
        "BEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinOp"


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
fiacre_Variable_strategy = st.builds(
    fiacre_Variable,
    name=
        safe_text
)
fiacre_MaxBound_strategy = st.builds(
    fiacre_MaxBound,
)
fiacre_MinBound_strategy = st.builds(
    fiacre_MinBound,
)
Exp_strategy = st.builds(
    Exp,
)
fiacre_ArrayElem_strategy = st.builds(
    fiacre_ArrayElem,
)
fiacre_BinExp_strategy = st.builds(
    fiacre_BinExp,
    binOp=
        safe_text
)
fiacre_RecordElem_strategy = st.builds(
    fiacre_RecordElem,
    field=
        safe_text
)
fiacre_UnExp_strategy = st.builds(
    fiacre_UnExp,
    unop=
        safe_text
)
fiacre_Pattern_strategy = st.builds(
    fiacre_Pattern,
)
fiacre_SingleAssignment_strategy = st.builds(
    fiacre_SingleAssignment,
)
Assignment_strategy = st.builds(
    Assignment,
)
fiacre_NonDeterministicAssignment_strategy = st.builds(
    fiacre_NonDeterministicAssignment,
)
fiacre_DeterministicAssignment_strategy = st.builds(
    fiacre_DeterministicAssignment,
)
fiacre_InlineCollection_strategy = st.builds(
    fiacre_InlineCollection,
)
fiacre_CondExp_strategy = st.builds(
    fiacre_CondExp,
)
MaxBound_strategy = st.builds(
    MaxBound,
)
fiacre_InfiniteBound_strategy = st.builds(
    fiacre_InfiniteBound,
)
MinBound_strategy = st.builds(
    MinBound,
)
fiacre_FiniteBound_strategy = st.builds(
    fiacre_FiniteBound,
    strict=
        st.booleans(),
    val=
        st.integers()
)
fiacre_LabeledType_strategy = st.builds(
    fiacre_LabeledType,
    name=
        safe_text
)
fiacre_ConstrExp_strategy = st.builds(
    fiacre_ConstrExp,
    name=
        safe_text
)
fiacre_Rule_strategy = st.builds(
    fiacre_Rule,
)
Channel_strategy = st.builds(
    Channel,
)
fiacre_Profile_strategy = st.builds(
    fiacre_Profile,
)
PortDecl_strategy = st.builds(
    PortDecl,
)
Communication_strategy = st.builds(
    Communication,
)
fiacre_Emission_strategy = st.builds(
    fiacre_Emission,
)
fiacre_Reception_strategy = st.builds(
    fiacre_Reception,
)
fiacre_Synchronization_strategy = st.builds(
    fiacre_Synchronization,
)
fiacre_ValuedField_strategy = st.builds(
    fiacre_ValuedField,
    field=
        safe_text
)
fiacre_InlineRecord_strategy = st.builds(
    fiacre_InlineRecord,
)
Pattern_strategy = st.builds(
    Pattern,
)
fiacre_Literal_strategy = st.builds(
    fiacre_Literal,
)
fiacre_ConstrPattern_strategy = st.builds(
    fiacre_ConstrPattern,
    name=
        safe_text
)
fiacre_AnyPattern_strategy = st.builds(
    fiacre_AnyPattern,
)
fiacre_ConstantRef_strategy = st.builds(
    fiacre_ConstantRef,
)
fiacre_FieldPattern_strategy = st.builds(
    fiacre_FieldPattern,
    field=
        safe_text
)
fiacre_ArrayPattern_strategy = st.builds(
    fiacre_ArrayPattern,
)
fiacre_VarRef_strategy = st.builds(
    fiacre_VarRef,
)
Literal_strategy = st.builds(
    Literal,
)
fiacre_BoolLiteral_strategy = st.builds(
    fiacre_BoolLiteral,
    value=
        st.booleans()
)
fiacre_NatLiteral_strategy = st.builds(
    fiacre_NatLiteral,
    value=
        st.integers()
)
LabeledType_strategy = st.builds(
    LabeledType,
)
fiacre_Constr_strategy = st.builds(
    fiacre_Constr,
)
fiacre_Field_strategy = st.builds(
    fiacre_Field,
)
BasicType_strategy = st.builds(
    BasicType,
)
fiacre_IntType_strategy = st.builds(
    fiacre_IntType,
)
fiacre_NatType_strategy = st.builds(
    fiacre_NatType,
)
fiacre_BoolType_strategy = st.builds(
    fiacre_BoolType,
)
Type_strategy = st.builds(
    Type,
)
fiacre_Array_strategy = st.builds(
    fiacre_Array,
)
fiacre_TypeId_strategy = st.builds(
    fiacre_TypeId,
)
fiacre_Union_strategy = st.builds(
    fiacre_Union,
)
fiacre_Record_strategy = st.builds(
    fiacre_Record,
)
fiacre_Queue_strategy = st.builds(
    fiacre_Queue,
)
fiacre_Interval_strategy = st.builds(
    fiacre_Interval,
)
fiacre_BasicType_strategy = st.builds(
    fiacre_BasicType,
)
InlineCollection_strategy = st.builds(
    InlineCollection,
)
fiacre_InlineArray_strategy = st.builds(
    fiacre_InlineArray,
)
fiacre_InlineQueue_strategy = st.builds(
    fiacre_InlineQueue,
)
fiacre_InterfacedComp_strategy = st.builds(
    fiacre_InterfacedComp,
)
Composition_strategy = st.builds(
    Composition,
)
fiacre_Instance_strategy = st.builds(
    fiacre_Instance,
    name=
        safe_text
)
fiacre_Par_strategy = st.builds(
    fiacre_Par,
)
Statement_strategy = st.builds(
    Statement,
)
fiacre_To_strategy = st.builds(
    fiacre_To,
)
fiacre_Select_strategy = st.builds(
    fiacre_Select,
)
fiacre_Wait_strategy = st.builds(
    fiacre_Wait,
)
fiacre_Seq_strategy = st.builds(
    fiacre_Seq,
)
fiacre_Assignment_strategy = st.builds(
    fiacre_Assignment,
)
fiacre_IfStmt_strategy = st.builds(
    fiacre_IfStmt,
)
fiacre_WhileStmt_strategy = st.builds(
    fiacre_WhileStmt,
)
fiacre_Foreach_strategy = st.builds(
    fiacre_Foreach,
)
fiacre_CaseStmt_strategy = st.builds(
    fiacre_CaseStmt,
)
fiacre_Communication_strategy = st.builds(
    fiacre_Communication,
)
fiacre_NullStmt_strategy = st.builds(
    fiacre_NullStmt,
)
Arg_strategy = st.builds(
    Arg,
)
fiacre_Exp_strategy = st.builds(
    fiacre_Exp,
)
fiacre_RefArg_strategy = st.builds(
    fiacre_RefArg,
)
fiacre_Arg_strategy = st.builds(
    fiacre_Arg,
)
Declaration_strategy = st.builds(
    Declaration,
)
fiacre_ConstantDecl_strategy = st.builds(
    fiacre_ConstantDecl,
)
fiacre_NodeDecl_strategy = st.builds(
    fiacre_NodeDecl,
)
fiacre_Declaration_strategy = st.builds(
    fiacre_Declaration,
    name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
fiacre_ArgumentVariable_strategy = st.builds(
    fiacre_ArgumentVariable,
    read=
        st.booleans(),
    ref=
        st.booleans(),
    write=
        st.booleans()
)
fiacre_PortDecl_strategy = st.builds(
    fiacre_PortDecl,
    name=
        safe_text,
    out=
        st.booleans(),
    in_=
        st.booleans()
)
fiacre_Transition_strategy = st.builds(
    fiacre_Transition,
    name=
        safe_text
)
fiacre_State_strategy = st.builds(
    fiacre_State,
    name=
        safe_text
)
fiacre_Priority_strategy = st.builds(
    fiacre_Priority,
)
fiacre_Composition_strategy = st.builds(
    fiacre_Composition,
)
NodeDecl_strategy = st.builds(
    NodeDecl,
)
fiacre_ProcessDecl_strategy = st.builds(
    fiacre_ProcessDecl,
)
fiacre_ComponentDecl_strategy = st.builds(
    fiacre_ComponentDecl,
)
fiacre_Channel_strategy = st.builds(
    fiacre_Channel,
)
fiacre_ChannelDecl_strategy = st.builds(
    fiacre_ChannelDecl,
)
fiacre_Type_strategy = st.builds(
    fiacre_Type,
)
fiacre_TypeDecl_strategy = st.builds(
    fiacre_TypeDecl,
)
fiacre_Statement_strategy = st.builds(
    fiacre_Statement,
    comment=
        safe_text
)
fiacre_LocalPortDecl_strategy = st.builds(
    fiacre_LocalPortDecl,
)
fiacre_ParamPortDecl_strategy = st.builds(
    fiacre_ParamPortDecl,
)
fiacre_LocalVariable_strategy = st.builds(
    fiacre_LocalVariable,
    constant=
        st.booleans()
)
fiacre_Program_strategy = st.builds(
    fiacre_Program,
)

@given(instance=fiacre_Variable_strategy)
@settings(max_examples=50)
def test_fiacre_variable_instantiation(instance):
    assert isinstance(instance, fiacre_Variable)



@given(instance=fiacre_Variable_strategy)
def test_fiacre_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_MaxBound_strategy)
@settings(max_examples=50)
def test_fiacre_maxbound_instantiation(instance):
    assert isinstance(instance, fiacre_MaxBound)

@given(instance=fiacre_MinBound_strategy)
@settings(max_examples=50)
def test_fiacre_minbound_instantiation(instance):
    assert isinstance(instance, fiacre_MinBound)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=fiacre_ArrayElem_strategy)
@settings(max_examples=50)
def test_fiacre_arrayelem_instantiation(instance):
    assert isinstance(instance, fiacre_ArrayElem)

@given(instance=fiacre_BinExp_strategy)
@settings(max_examples=50)
def test_fiacre_binexp_instantiation(instance):
    assert isinstance(instance, fiacre_BinExp)



@given(instance=fiacre_BinExp_strategy)
def test_fiacre_binexp_binOp_setter(instance):
    original = instance.binOp
    instance.binOp = original
    assert instance.binOp == original

@given(instance=fiacre_RecordElem_strategy)
@settings(max_examples=50)
def test_fiacre_recordelem_instantiation(instance):
    assert isinstance(instance, fiacre_RecordElem)



@given(instance=fiacre_RecordElem_strategy)
def test_fiacre_recordelem_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre_UnExp_strategy)
@settings(max_examples=50)
def test_fiacre_unexp_instantiation(instance):
    assert isinstance(instance, fiacre_UnExp)



@given(instance=fiacre_UnExp_strategy)
def test_fiacre_unexp_unop_setter(instance):
    original = instance.unop
    instance.unop = original
    assert instance.unop == original

@given(instance=fiacre_Pattern_strategy)
@settings(max_examples=50)
def test_fiacre_pattern_instantiation(instance):
    assert isinstance(instance, fiacre_Pattern)

@given(instance=fiacre_SingleAssignment_strategy)
@settings(max_examples=50)
def test_fiacre_singleassignment_instantiation(instance):
    assert isinstance(instance, fiacre_SingleAssignment)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=fiacre_NonDeterministicAssignment_strategy)
@settings(max_examples=50)
def test_fiacre_nondeterministicassignment_instantiation(instance):
    assert isinstance(instance, fiacre_NonDeterministicAssignment)

@given(instance=fiacre_DeterministicAssignment_strategy)
@settings(max_examples=50)
def test_fiacre_deterministicassignment_instantiation(instance):
    assert isinstance(instance, fiacre_DeterministicAssignment)

@given(instance=fiacre_InlineCollection_strategy)
@settings(max_examples=50)
def test_fiacre_inlinecollection_instantiation(instance):
    assert isinstance(instance, fiacre_InlineCollection)

@given(instance=fiacre_CondExp_strategy)
@settings(max_examples=50)
def test_fiacre_condexp_instantiation(instance):
    assert isinstance(instance, fiacre_CondExp)

@given(instance=MaxBound_strategy)
@settings(max_examples=50)
def test_maxbound_instantiation(instance):
    assert isinstance(instance, MaxBound)

@given(instance=fiacre_InfiniteBound_strategy)
@settings(max_examples=50)
def test_fiacre_infinitebound_instantiation(instance):
    assert isinstance(instance, fiacre_InfiniteBound)

@given(instance=MinBound_strategy)
@settings(max_examples=50)
def test_minbound_instantiation(instance):
    assert isinstance(instance, MinBound)

@given(instance=fiacre_FiniteBound_strategy)
@settings(max_examples=50)
def test_fiacre_finitebound_instantiation(instance):
    assert isinstance(instance, fiacre_FiniteBound)



@given(instance=fiacre_FiniteBound_strategy)
def test_fiacre_finitebound_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original



@given(instance=fiacre_FiniteBound_strategy)
def test_fiacre_finitebound_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=fiacre_LabeledType_strategy)
@settings(max_examples=50)
def test_fiacre_labeledtype_instantiation(instance):
    assert isinstance(instance, fiacre_LabeledType)



@given(instance=fiacre_LabeledType_strategy)
def test_fiacre_labeledtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_ConstrExp_strategy)
@settings(max_examples=50)
def test_fiacre_constrexp_instantiation(instance):
    assert isinstance(instance, fiacre_ConstrExp)



@given(instance=fiacre_ConstrExp_strategy)
def test_fiacre_constrexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_Rule_strategy)
@settings(max_examples=50)
def test_fiacre_rule_instantiation(instance):
    assert isinstance(instance, fiacre_Rule)

@given(instance=Channel_strategy)
@settings(max_examples=50)
def test_channel_instantiation(instance):
    assert isinstance(instance, Channel)

@given(instance=fiacre_Profile_strategy)
@settings(max_examples=50)
def test_fiacre_profile_instantiation(instance):
    assert isinstance(instance, fiacre_Profile)

@given(instance=PortDecl_strategy)
@settings(max_examples=50)
def test_portdecl_instantiation(instance):
    assert isinstance(instance, PortDecl)

@given(instance=Communication_strategy)
@settings(max_examples=50)
def test_communication_instantiation(instance):
    assert isinstance(instance, Communication)

@given(instance=fiacre_Emission_strategy)
@settings(max_examples=50)
def test_fiacre_emission_instantiation(instance):
    assert isinstance(instance, fiacre_Emission)

@given(instance=fiacre_Reception_strategy)
@settings(max_examples=50)
def test_fiacre_reception_instantiation(instance):
    assert isinstance(instance, fiacre_Reception)

@given(instance=fiacre_Synchronization_strategy)
@settings(max_examples=50)
def test_fiacre_synchronization_instantiation(instance):
    assert isinstance(instance, fiacre_Synchronization)

@given(instance=fiacre_ValuedField_strategy)
@settings(max_examples=50)
def test_fiacre_valuedfield_instantiation(instance):
    assert isinstance(instance, fiacre_ValuedField)



@given(instance=fiacre_ValuedField_strategy)
def test_fiacre_valuedfield_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre_InlineRecord_strategy)
@settings(max_examples=50)
def test_fiacre_inlinerecord_instantiation(instance):
    assert isinstance(instance, fiacre_InlineRecord)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=fiacre_Literal_strategy)
@settings(max_examples=50)
def test_fiacre_literal_instantiation(instance):
    assert isinstance(instance, fiacre_Literal)

@given(instance=fiacre_ConstrPattern_strategy)
@settings(max_examples=50)
def test_fiacre_constrpattern_instantiation(instance):
    assert isinstance(instance, fiacre_ConstrPattern)



@given(instance=fiacre_ConstrPattern_strategy)
def test_fiacre_constrpattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_AnyPattern_strategy)
@settings(max_examples=50)
def test_fiacre_anypattern_instantiation(instance):
    assert isinstance(instance, fiacre_AnyPattern)

@given(instance=fiacre_ConstantRef_strategy)
@settings(max_examples=50)
def test_fiacre_constantref_instantiation(instance):
    assert isinstance(instance, fiacre_ConstantRef)

@given(instance=fiacre_FieldPattern_strategy)
@settings(max_examples=50)
def test_fiacre_fieldpattern_instantiation(instance):
    assert isinstance(instance, fiacre_FieldPattern)



@given(instance=fiacre_FieldPattern_strategy)
def test_fiacre_fieldpattern_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=fiacre_ArrayPattern_strategy)
@settings(max_examples=50)
def test_fiacre_arraypattern_instantiation(instance):
    assert isinstance(instance, fiacre_ArrayPattern)

@given(instance=fiacre_VarRef_strategy)
@settings(max_examples=50)
def test_fiacre_varref_instantiation(instance):
    assert isinstance(instance, fiacre_VarRef)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fiacre_BoolLiteral_strategy)
@settings(max_examples=50)
def test_fiacre_boolliteral_instantiation(instance):
    assert isinstance(instance, fiacre_BoolLiteral)



@given(instance=fiacre_BoolLiteral_strategy)
def test_fiacre_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fiacre_NatLiteral_strategy)
@settings(max_examples=50)
def test_fiacre_natliteral_instantiation(instance):
    assert isinstance(instance, fiacre_NatLiteral)



@given(instance=fiacre_NatLiteral_strategy)
def test_fiacre_natliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=LabeledType_strategy)
@settings(max_examples=50)
def test_labeledtype_instantiation(instance):
    assert isinstance(instance, LabeledType)

@given(instance=fiacre_Constr_strategy)
@settings(max_examples=50)
def test_fiacre_constr_instantiation(instance):
    assert isinstance(instance, fiacre_Constr)

@given(instance=fiacre_Field_strategy)
@settings(max_examples=50)
def test_fiacre_field_instantiation(instance):
    assert isinstance(instance, fiacre_Field)

@given(instance=BasicType_strategy)
@settings(max_examples=50)
def test_basictype_instantiation(instance):
    assert isinstance(instance, BasicType)

@given(instance=fiacre_IntType_strategy)
@settings(max_examples=50)
def test_fiacre_inttype_instantiation(instance):
    assert isinstance(instance, fiacre_IntType)

@given(instance=fiacre_NatType_strategy)
@settings(max_examples=50)
def test_fiacre_nattype_instantiation(instance):
    assert isinstance(instance, fiacre_NatType)

@given(instance=fiacre_BoolType_strategy)
@settings(max_examples=50)
def test_fiacre_booltype_instantiation(instance):
    assert isinstance(instance, fiacre_BoolType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=fiacre_Array_strategy)
@settings(max_examples=50)
def test_fiacre_array_instantiation(instance):
    assert isinstance(instance, fiacre_Array)

@given(instance=fiacre_TypeId_strategy)
@settings(max_examples=50)
def test_fiacre_typeid_instantiation(instance):
    assert isinstance(instance, fiacre_TypeId)

@given(instance=fiacre_Union_strategy)
@settings(max_examples=50)
def test_fiacre_union_instantiation(instance):
    assert isinstance(instance, fiacre_Union)

@given(instance=fiacre_Record_strategy)
@settings(max_examples=50)
def test_fiacre_record_instantiation(instance):
    assert isinstance(instance, fiacre_Record)

@given(instance=fiacre_Queue_strategy)
@settings(max_examples=50)
def test_fiacre_queue_instantiation(instance):
    assert isinstance(instance, fiacre_Queue)

@given(instance=fiacre_Interval_strategy)
@settings(max_examples=50)
def test_fiacre_interval_instantiation(instance):
    assert isinstance(instance, fiacre_Interval)

@given(instance=fiacre_BasicType_strategy)
@settings(max_examples=50)
def test_fiacre_basictype_instantiation(instance):
    assert isinstance(instance, fiacre_BasicType)

@given(instance=InlineCollection_strategy)
@settings(max_examples=50)
def test_inlinecollection_instantiation(instance):
    assert isinstance(instance, InlineCollection)

@given(instance=fiacre_InlineArray_strategy)
@settings(max_examples=50)
def test_fiacre_inlinearray_instantiation(instance):
    assert isinstance(instance, fiacre_InlineArray)

@given(instance=fiacre_InlineQueue_strategy)
@settings(max_examples=50)
def test_fiacre_inlinequeue_instantiation(instance):
    assert isinstance(instance, fiacre_InlineQueue)

@given(instance=fiacre_InterfacedComp_strategy)
@settings(max_examples=50)
def test_fiacre_interfacedcomp_instantiation(instance):
    assert isinstance(instance, fiacre_InterfacedComp)

@given(instance=Composition_strategy)
@settings(max_examples=50)
def test_composition_instantiation(instance):
    assert isinstance(instance, Composition)

@given(instance=fiacre_Instance_strategy)
@settings(max_examples=50)
def test_fiacre_instance_instantiation(instance):
    assert isinstance(instance, fiacre_Instance)



@given(instance=fiacre_Instance_strategy)
def test_fiacre_instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_Par_strategy)
@settings(max_examples=50)
def test_fiacre_par_instantiation(instance):
    assert isinstance(instance, fiacre_Par)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fiacre_To_strategy)
@settings(max_examples=50)
def test_fiacre_to_instantiation(instance):
    assert isinstance(instance, fiacre_To)

@given(instance=fiacre_Select_strategy)
@settings(max_examples=50)
def test_fiacre_select_instantiation(instance):
    assert isinstance(instance, fiacre_Select)

@given(instance=fiacre_Wait_strategy)
@settings(max_examples=50)
def test_fiacre_wait_instantiation(instance):
    assert isinstance(instance, fiacre_Wait)

@given(instance=fiacre_Seq_strategy)
@settings(max_examples=50)
def test_fiacre_seq_instantiation(instance):
    assert isinstance(instance, fiacre_Seq)

@given(instance=fiacre_Assignment_strategy)
@settings(max_examples=50)
def test_fiacre_assignment_instantiation(instance):
    assert isinstance(instance, fiacre_Assignment)

@given(instance=fiacre_IfStmt_strategy)
@settings(max_examples=50)
def test_fiacre_ifstmt_instantiation(instance):
    assert isinstance(instance, fiacre_IfStmt)

@given(instance=fiacre_WhileStmt_strategy)
@settings(max_examples=50)
def test_fiacre_whilestmt_instantiation(instance):
    assert isinstance(instance, fiacre_WhileStmt)

@given(instance=fiacre_Foreach_strategy)
@settings(max_examples=50)
def test_fiacre_foreach_instantiation(instance):
    assert isinstance(instance, fiacre_Foreach)

@given(instance=fiacre_CaseStmt_strategy)
@settings(max_examples=50)
def test_fiacre_casestmt_instantiation(instance):
    assert isinstance(instance, fiacre_CaseStmt)

@given(instance=fiacre_Communication_strategy)
@settings(max_examples=50)
def test_fiacre_communication_instantiation(instance):
    assert isinstance(instance, fiacre_Communication)

@given(instance=fiacre_NullStmt_strategy)
@settings(max_examples=50)
def test_fiacre_nullstmt_instantiation(instance):
    assert isinstance(instance, fiacre_NullStmt)

@given(instance=Arg_strategy)
@settings(max_examples=50)
def test_arg_instantiation(instance):
    assert isinstance(instance, Arg)

@given(instance=fiacre_Exp_strategy)
@settings(max_examples=50)
def test_fiacre_exp_instantiation(instance):
    assert isinstance(instance, fiacre_Exp)

@given(instance=fiacre_RefArg_strategy)
@settings(max_examples=50)
def test_fiacre_refarg_instantiation(instance):
    assert isinstance(instance, fiacre_RefArg)

@given(instance=fiacre_Arg_strategy)
@settings(max_examples=50)
def test_fiacre_arg_instantiation(instance):
    assert isinstance(instance, fiacre_Arg)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=fiacre_ConstantDecl_strategy)
@settings(max_examples=50)
def test_fiacre_constantdecl_instantiation(instance):
    assert isinstance(instance, fiacre_ConstantDecl)

@given(instance=fiacre_NodeDecl_strategy)
@settings(max_examples=50)
def test_fiacre_nodedecl_instantiation(instance):
    assert isinstance(instance, fiacre_NodeDecl)

@given(instance=fiacre_Declaration_strategy)
@settings(max_examples=50)
def test_fiacre_declaration_instantiation(instance):
    assert isinstance(instance, fiacre_Declaration)



@given(instance=fiacre_Declaration_strategy)
def test_fiacre_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=fiacre_ArgumentVariable_strategy)
@settings(max_examples=50)
def test_fiacre_argumentvariable_instantiation(instance):
    assert isinstance(instance, fiacre_ArgumentVariable)



@given(instance=fiacre_ArgumentVariable_strategy)
def test_fiacre_argumentvariable_read_setter(instance):
    original = instance.read
    instance.read = original
    assert instance.read == original



@given(instance=fiacre_ArgumentVariable_strategy)
def test_fiacre_argumentvariable_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



@given(instance=fiacre_ArgumentVariable_strategy)
def test_fiacre_argumentvariable_write_setter(instance):
    original = instance.write
    instance.write = original
    assert instance.write == original

@given(instance=fiacre_PortDecl_strategy)
@settings(max_examples=50)
def test_fiacre_portdecl_instantiation(instance):
    assert isinstance(instance, fiacre_PortDecl)



@given(instance=fiacre_PortDecl_strategy)
def test_fiacre_portdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fiacre_PortDecl_strategy)
def test_fiacre_portdecl_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=fiacre_PortDecl_strategy)
def test_fiacre_portdecl_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=fiacre_Transition_strategy)
@settings(max_examples=50)
def test_fiacre_transition_instantiation(instance):
    assert isinstance(instance, fiacre_Transition)



@given(instance=fiacre_Transition_strategy)
def test_fiacre_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_State_strategy)
@settings(max_examples=50)
def test_fiacre_state_instantiation(instance):
    assert isinstance(instance, fiacre_State)



@given(instance=fiacre_State_strategy)
def test_fiacre_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fiacre_Priority_strategy)
@settings(max_examples=50)
def test_fiacre_priority_instantiation(instance):
    assert isinstance(instance, fiacre_Priority)

@given(instance=fiacre_Composition_strategy)
@settings(max_examples=50)
def test_fiacre_composition_instantiation(instance):
    assert isinstance(instance, fiacre_Composition)

@given(instance=NodeDecl_strategy)
@settings(max_examples=50)
def test_nodedecl_instantiation(instance):
    assert isinstance(instance, NodeDecl)

@given(instance=fiacre_ProcessDecl_strategy)
@settings(max_examples=50)
def test_fiacre_processdecl_instantiation(instance):
    assert isinstance(instance, fiacre_ProcessDecl)

@given(instance=fiacre_ComponentDecl_strategy)
@settings(max_examples=50)
def test_fiacre_componentdecl_instantiation(instance):
    assert isinstance(instance, fiacre_ComponentDecl)

@given(instance=fiacre_Channel_strategy)
@settings(max_examples=50)
def test_fiacre_channel_instantiation(instance):
    assert isinstance(instance, fiacre_Channel)

@given(instance=fiacre_ChannelDecl_strategy)
@settings(max_examples=50)
def test_fiacre_channeldecl_instantiation(instance):
    assert isinstance(instance, fiacre_ChannelDecl)

@given(instance=fiacre_Type_strategy)
@settings(max_examples=50)
def test_fiacre_type_instantiation(instance):
    assert isinstance(instance, fiacre_Type)

@given(instance=fiacre_TypeDecl_strategy)
@settings(max_examples=50)
def test_fiacre_typedecl_instantiation(instance):
    assert isinstance(instance, fiacre_TypeDecl)

@given(instance=fiacre_Statement_strategy)
@settings(max_examples=50)
def test_fiacre_statement_instantiation(instance):
    assert isinstance(instance, fiacre_Statement)



@given(instance=fiacre_Statement_strategy)
def test_fiacre_statement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=fiacre_LocalPortDecl_strategy)
@settings(max_examples=50)
def test_fiacre_localportdecl_instantiation(instance):
    assert isinstance(instance, fiacre_LocalPortDecl)

@given(instance=fiacre_ParamPortDecl_strategy)
@settings(max_examples=50)
def test_fiacre_paramportdecl_instantiation(instance):
    assert isinstance(instance, fiacre_ParamPortDecl)

@given(instance=fiacre_LocalVariable_strategy)
@settings(max_examples=50)
def test_fiacre_localvariable_instantiation(instance):
    assert isinstance(instance, fiacre_LocalVariable)



@given(instance=fiacre_LocalVariable_strategy)
def test_fiacre_localvariable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=fiacre_Program_strategy)
@settings(max_examples=50)
def test_fiacre_program_instantiation(instance):
    assert isinstance(instance, fiacre_Program)

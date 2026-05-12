import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Constraint,
    tExp_Size,
    tExp_Cardinality,
    tExp_Singletons,
    tExp_Together,
    Expression,
    tExp_AndExpr,
    tExp_FilterExpr,
    tExp_UnionExpr,
    tExp_SeqExpr,
    tExp_CatExpr,
    tExp_VarExpr,
    tExp_TerminalExpr,
    tExp_ShuffleExpr,
    PrologExpression,
    tExp_StringExpression,
    tExp_NumberExpression,
    tExp_VariableExpression,
    tExp_ListExpression,
    tExp_AtomExpression,
    tExp_Expression,
    tExp_Channel,
    tExp_Constraint,
    tExp_Partition,
    tExp_Msg,
    tExp_EventType,
    tExp_Role,
    tExp_Term,
    tExp_PrologExpression,
    tExp_TraceExpression,
    tExp_Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_texp_size_is_not_abstract():
    assert not inspect.isabstract(tExp_Size)


def test_texp_size_constructor_exists():
    assert callable(tExp_Size.__init__)


def test_texp_size_constructor_args():
    sig = inspect.signature(tExp_Size.__init__)
    params = list(sig.parameters.keys())
    assert "minSize" in params, "Missing parameter 'minSize'"
    assert "maxSize" in params, "Missing parameter 'maxSize'"

def test_texp_size_has_minSize():
    assert hasattr(tExp_Size, "minSize")
    descriptor = None
    for klass in tExp_Size.__mro__:
        if "minSize" in klass.__dict__:
            descriptor = klass.__dict__["minSize"]
            break
    assert isinstance(descriptor, property)

def test_texp_size_has_maxSize():
    assert hasattr(tExp_Size, "maxSize")
    descriptor = None
    for klass in tExp_Size.__mro__:
        if "maxSize" in klass.__dict__:
            descriptor = klass.__dict__["maxSize"]
            break
    assert isinstance(descriptor, property)



def test_texp_cardinality_is_not_abstract():
    assert not inspect.isabstract(tExp_Cardinality)


def test_texp_cardinality_constructor_exists():
    assert callable(tExp_Cardinality.__init__)


def test_texp_cardinality_constructor_args():
    sig = inspect.signature(tExp_Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"

def test_texp_cardinality_has_maxCardinality():
    assert hasattr(tExp_Cardinality, "maxCardinality")
    descriptor = None
    for klass in tExp_Cardinality.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)

def test_texp_cardinality_has_minCardinality():
    assert hasattr(tExp_Cardinality, "minCardinality")
    descriptor = None
    for klass in tExp_Cardinality.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)



def test_texp_singletons_is_not_abstract():
    assert not inspect.isabstract(tExp_Singletons)


def test_texp_singletons_constructor_exists():
    assert callable(tExp_Singletons.__init__)


def test_texp_singletons_constructor_args():
    sig = inspect.signature(tExp_Singletons.__init__)
    params = list(sig.parameters.keys())
    assert "maxSingletons" in params, "Missing parameter 'maxSingletons'"
    assert "minSingletons" in params, "Missing parameter 'minSingletons'"

def test_texp_singletons_has_maxSingletons():
    assert hasattr(tExp_Singletons, "maxSingletons")
    descriptor = None
    for klass in tExp_Singletons.__mro__:
        if "maxSingletons" in klass.__dict__:
            descriptor = klass.__dict__["maxSingletons"]
            break
    assert isinstance(descriptor, property)

def test_texp_singletons_has_minSingletons():
    assert hasattr(tExp_Singletons, "minSingletons")
    descriptor = None
    for klass in tExp_Singletons.__mro__:
        if "minSingletons" in klass.__dict__:
            descriptor = klass.__dict__["minSingletons"]
            break
    assert isinstance(descriptor, property)



def test_texp_together_is_not_abstract():
    assert not inspect.isabstract(tExp_Together)


def test_texp_together_constructor_exists():
    assert callable(tExp_Together.__init__)


def test_texp_together_constructor_args():
    sig = inspect.signature(tExp_Together.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_texp_andexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_AndExpr)


def test_texp_andexpr_constructor_exists():
    assert callable(tExp_AndExpr.__init__)


def test_texp_andexpr_constructor_args():
    sig = inspect.signature(tExp_AndExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_filterexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_FilterExpr)


def test_texp_filterexpr_constructor_exists():
    assert callable(tExp_FilterExpr.__init__)


def test_texp_filterexpr_constructor_args():
    sig = inspect.signature(tExp_FilterExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_unionexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_UnionExpr)


def test_texp_unionexpr_constructor_exists():
    assert callable(tExp_UnionExpr.__init__)


def test_texp_unionexpr_constructor_args():
    sig = inspect.signature(tExp_UnionExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_seqexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_SeqExpr)


def test_texp_seqexpr_constructor_exists():
    assert callable(tExp_SeqExpr.__init__)


def test_texp_seqexpr_constructor_args():
    sig = inspect.signature(tExp_SeqExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_catexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_CatExpr)


def test_texp_catexpr_constructor_exists():
    assert callable(tExp_CatExpr.__init__)


def test_texp_catexpr_constructor_args():
    sig = inspect.signature(tExp_CatExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_varexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_VarExpr)


def test_texp_varexpr_constructor_exists():
    assert callable(tExp_VarExpr.__init__)


def test_texp_varexpr_constructor_args():
    sig = inspect.signature(tExp_VarExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_terminalexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_TerminalExpr)


def test_texp_terminalexpr_constructor_exists():
    assert callable(tExp_TerminalExpr.__init__)


def test_texp_terminalexpr_constructor_args():
    sig = inspect.signature(tExp_TerminalExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp_shuffleexpr_is_not_abstract():
    assert not inspect.isabstract(tExp_ShuffleExpr)


def test_texp_shuffleexpr_constructor_exists():
    assert callable(tExp_ShuffleExpr.__init__)


def test_texp_shuffleexpr_constructor_args():
    sig = inspect.signature(tExp_ShuffleExpr.__init__)
    params = list(sig.parameters.keys())



def test_prologexpression_is_not_abstract():
    assert not inspect.isabstract(PrologExpression)


def test_prologexpression_constructor_exists():
    assert callable(PrologExpression.__init__)


def test_prologexpression_constructor_args():
    sig = inspect.signature(PrologExpression.__init__)
    params = list(sig.parameters.keys())



def test_texp_stringexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_StringExpression)


def test_texp_stringexpression_constructor_exists():
    assert callable(tExp_StringExpression.__init__)


def test_texp_stringexpression_constructor_args():
    sig = inspect.signature(tExp_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_texp_stringexpression_has_value():
    assert hasattr(tExp_StringExpression, "value")
    descriptor = None
    for klass in tExp_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_texp_numberexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_NumberExpression)


def test_texp_numberexpression_constructor_exists():
    assert callable(tExp_NumberExpression.__init__)


def test_texp_numberexpression_constructor_args():
    sig = inspect.signature(tExp_NumberExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_texp_numberexpression_has_value():
    assert hasattr(tExp_NumberExpression, "value")
    descriptor = None
    for klass in tExp_NumberExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_texp_variableexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_VariableExpression)


def test_texp_variableexpression_constructor_exists():
    assert callable(tExp_VariableExpression.__init__)


def test_texp_variableexpression_constructor_args():
    sig = inspect.signature(tExp_VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp_variableexpression_has_name():
    assert hasattr(tExp_VariableExpression, "name")
    descriptor = None
    for klass in tExp_VariableExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp_listexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_ListExpression)


def test_texp_listexpression_constructor_exists():
    assert callable(tExp_ListExpression.__init__)


def test_texp_listexpression_constructor_args():
    sig = inspect.signature(tExp_ListExpression.__init__)
    params = list(sig.parameters.keys())



def test_texp_atomexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_AtomExpression)


def test_texp_atomexpression_constructor_exists():
    assert callable(tExp_AtomExpression.__init__)


def test_texp_atomexpression_constructor_args():
    sig = inspect.signature(tExp_AtomExpression.__init__)
    params = list(sig.parameters.keys())
    assert "atom" in params, "Missing parameter 'atom'"

def test_texp_atomexpression_has_atom():
    assert hasattr(tExp_AtomExpression, "atom")
    descriptor = None
    for klass in tExp_AtomExpression.__mro__:
        if "atom" in klass.__dict__:
            descriptor = klass.__dict__["atom"]
            break
    assert isinstance(descriptor, property)



def test_texp_expression_is_not_abstract():
    assert not inspect.isabstract(tExp_Expression)


def test_texp_expression_constructor_exists():
    assert callable(tExp_Expression.__init__)


def test_texp_expression_constructor_args():
    sig = inspect.signature(tExp_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "eps" in params, "Missing parameter 'eps'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_texp_expression_has_eps():
    assert hasattr(tExp_Expression, "eps")
    descriptor = None
    for klass in tExp_Expression.__mro__:
        if "eps" in klass.__dict__:
            descriptor = klass.__dict__["eps"]
            break
    assert isinstance(descriptor, property)

def test_texp_expression_has_variable():
    assert hasattr(tExp_Expression, "variable")
    descriptor = None
    for klass in tExp_Expression.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_texp_expression_has_operator():
    assert hasattr(tExp_Expression, "operator")
    descriptor = None
    for klass in tExp_Expression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_texp_channel_is_not_abstract():
    assert not inspect.isabstract(tExp_Channel)


def test_texp_channel_constructor_exists():
    assert callable(tExp_Channel.__init__)


def test_texp_channel_constructor_args():
    sig = inspect.signature(tExp_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "reliability" in params, "Missing parameter 'reliability'"

def test_texp_channel_has_name():
    assert hasattr(tExp_Channel, "name")
    descriptor = None
    for klass in tExp_Channel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_texp_channel_has_reliability():
    assert hasattr(tExp_Channel, "reliability")
    descriptor = None
    for klass in tExp_Channel.__mro__:
        if "reliability" in klass.__dict__:
            descriptor = klass.__dict__["reliability"]
            break
    assert isinstance(descriptor, property)



def test_texp_constraint_is_not_abstract():
    assert not inspect.isabstract(tExp_Constraint)


def test_texp_constraint_constructor_exists():
    assert callable(tExp_Constraint.__init__)


def test_texp_constraint_constructor_args():
    sig = inspect.signature(tExp_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "together" in params, "Missing parameter 'together'"
    assert "split" in params, "Missing parameter 'split'"
    assert "parMin" in params, "Missing parameter 'parMin'"
    assert "parMax" in params, "Missing parameter 'parMax'"

def test_texp_constraint_has_together():
    assert hasattr(tExp_Constraint, "together")
    descriptor = None
    for klass in tExp_Constraint.__mro__:
        if "together" in klass.__dict__:
            descriptor = klass.__dict__["together"]
            break
    assert isinstance(descriptor, property)

def test_texp_constraint_has_split():
    assert hasattr(tExp_Constraint, "split")
    descriptor = None
    for klass in tExp_Constraint.__mro__:
        if "split" in klass.__dict__:
            descriptor = klass.__dict__["split"]
            break
    assert isinstance(descriptor, property)

def test_texp_constraint_has_parMin():
    assert hasattr(tExp_Constraint, "parMin")
    descriptor = None
    for klass in tExp_Constraint.__mro__:
        if "parMin" in klass.__dict__:
            descriptor = klass.__dict__["parMin"]
            break
    assert isinstance(descriptor, property)

def test_texp_constraint_has_parMax():
    assert hasattr(tExp_Constraint, "parMax")
    descriptor = None
    for klass in tExp_Constraint.__mro__:
        if "parMax" in klass.__dict__:
            descriptor = klass.__dict__["parMax"]
            break
    assert isinstance(descriptor, property)



def test_texp_partition_is_not_abstract():
    assert not inspect.isabstract(tExp_Partition)


def test_texp_partition_constructor_exists():
    assert callable(tExp_Partition.__init__)


def test_texp_partition_constructor_args():
    sig = inspect.signature(tExp_Partition.__init__)
    params = list(sig.parameters.keys())



def test_texp_msg_is_not_abstract():
    assert not inspect.isabstract(tExp_Msg)


def test_texp_msg_constructor_exists():
    assert callable(tExp_Msg.__init__)


def test_texp_msg_constructor_args():
    sig = inspect.signature(tExp_Msg.__init__)
    params = list(sig.parameters.keys())
    assert "performative" in params, "Missing parameter 'performative'"

def test_texp_msg_has_performative():
    assert hasattr(tExp_Msg, "performative")
    descriptor = None
    for klass in tExp_Msg.__mro__:
        if "performative" in klass.__dict__:
            descriptor = klass.__dict__["performative"]
            break
    assert isinstance(descriptor, property)



def test_texp_eventtype_is_not_abstract():
    assert not inspect.isabstract(tExp_EventType)


def test_texp_eventtype_constructor_exists():
    assert callable(tExp_EventType.__init__)


def test_texp_eventtype_constructor_args():
    sig = inspect.signature(tExp_EventType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp_eventtype_has_name():
    assert hasattr(tExp_EventType, "name")
    descriptor = None
    for klass in tExp_EventType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp_role_is_not_abstract():
    assert not inspect.isabstract(tExp_Role)


def test_texp_role_constructor_exists():
    assert callable(tExp_Role.__init__)


def test_texp_role_constructor_args():
    sig = inspect.signature(tExp_Role.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "name" in params, "Missing parameter 'name'"

def test_texp_role_has_args():
    assert hasattr(tExp_Role, "args")
    descriptor = None
    for klass in tExp_Role.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_texp_role_has_class_():
    assert hasattr(tExp_Role, "class_")
    descriptor = None
    for klass in tExp_Role.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_texp_role_has_name():
    assert hasattr(tExp_Role, "name")
    descriptor = None
    for klass in tExp_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp_term_is_not_abstract():
    assert not inspect.isabstract(tExp_Term)


def test_texp_term_constructor_exists():
    assert callable(tExp_Term.__init__)


def test_texp_term_constructor_args():
    sig = inspect.signature(tExp_Term.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp_term_has_name():
    assert hasattr(tExp_Term, "name")
    descriptor = None
    for klass in tExp_Term.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp_prologexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_PrologExpression)


def test_texp_prologexpression_constructor_exists():
    assert callable(tExp_PrologExpression.__init__)


def test_texp_prologexpression_constructor_args():
    sig = inspect.signature(tExp_PrologExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_texp_prologexpression_has_op():
    assert hasattr(tExp_PrologExpression, "op")
    descriptor = None
    for klass in tExp_PrologExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_texp_traceexpression_is_not_abstract():
    assert not inspect.isabstract(tExp_TraceExpression)


def test_texp_traceexpression_constructor_exists():
    assert callable(tExp_TraceExpression.__init__)


def test_texp_traceexpression_constructor_args():
    sig = inspect.signature(tExp_TraceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "minimal" in params, "Missing parameter 'minimal'"
    assert "modules" in params, "Missing parameter 'modules'"
    assert "guiL" in params, "Missing parameter 'guiL'"
    assert "channelsL" in params, "Missing parameter 'channelsL'"
    assert "partitionL" in params, "Missing parameter 'partitionL'"
    assert "decentralizedL" in params, "Missing parameter 'decentralizedL'"
    assert "bodyL" in params, "Missing parameter 'bodyL'"
    assert "decentralized" in params, "Missing parameter 'decentralized'"
    assert "threshold" in params, "Missing parameter 'threshold'"
    assert "modulesL" in params, "Missing parameter 'modulesL'"
    assert "typesL" in params, "Missing parameter 'typesL'"
    assert "constraintsL" in params, "Missing parameter 'constraintsL'"
    assert "gui" in params, "Missing parameter 'gui'"
    assert "thresholdL" in params, "Missing parameter 'thresholdL'"
    assert "name" in params, "Missing parameter 'name'"
    assert "minimalL" in params, "Missing parameter 'minimalL'"
    assert "rolesL" in params, "Missing parameter 'rolesL'"

def test_texp_traceexpression_has_minimal():
    assert hasattr(tExp_TraceExpression, "minimal")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "minimal" in klass.__dict__:
            descriptor = klass.__dict__["minimal"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_modules():
    assert hasattr(tExp_TraceExpression, "modules")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "modules" in klass.__dict__:
            descriptor = klass.__dict__["modules"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_guiL():
    assert hasattr(tExp_TraceExpression, "guiL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "guiL" in klass.__dict__:
            descriptor = klass.__dict__["guiL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_channelsL():
    assert hasattr(tExp_TraceExpression, "channelsL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "channelsL" in klass.__dict__:
            descriptor = klass.__dict__["channelsL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_partitionL():
    assert hasattr(tExp_TraceExpression, "partitionL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "partitionL" in klass.__dict__:
            descriptor = klass.__dict__["partitionL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_decentralizedL():
    assert hasattr(tExp_TraceExpression, "decentralizedL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "decentralizedL" in klass.__dict__:
            descriptor = klass.__dict__["decentralizedL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_bodyL():
    assert hasattr(tExp_TraceExpression, "bodyL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "bodyL" in klass.__dict__:
            descriptor = klass.__dict__["bodyL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_decentralized():
    assert hasattr(tExp_TraceExpression, "decentralized")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "decentralized" in klass.__dict__:
            descriptor = klass.__dict__["decentralized"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_threshold():
    assert hasattr(tExp_TraceExpression, "threshold")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "threshold" in klass.__dict__:
            descriptor = klass.__dict__["threshold"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_modulesL():
    assert hasattr(tExp_TraceExpression, "modulesL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "modulesL" in klass.__dict__:
            descriptor = klass.__dict__["modulesL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_typesL():
    assert hasattr(tExp_TraceExpression, "typesL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "typesL" in klass.__dict__:
            descriptor = klass.__dict__["typesL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_constraintsL():
    assert hasattr(tExp_TraceExpression, "constraintsL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "constraintsL" in klass.__dict__:
            descriptor = klass.__dict__["constraintsL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_gui():
    assert hasattr(tExp_TraceExpression, "gui")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "gui" in klass.__dict__:
            descriptor = klass.__dict__["gui"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_thresholdL():
    assert hasattr(tExp_TraceExpression, "thresholdL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "thresholdL" in klass.__dict__:
            descriptor = klass.__dict__["thresholdL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_name():
    assert hasattr(tExp_TraceExpression, "name")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_minimalL():
    assert hasattr(tExp_TraceExpression, "minimalL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "minimalL" in klass.__dict__:
            descriptor = klass.__dict__["minimalL"]
            break
    assert isinstance(descriptor, property)

def test_texp_traceexpression_has_rolesL():
    assert hasattr(tExp_TraceExpression, "rolesL")
    descriptor = None
    for klass in tExp_TraceExpression.__mro__:
        if "rolesL" in klass.__dict__:
            descriptor = klass.__dict__["rolesL"]
            break
    assert isinstance(descriptor, property)



def test_texp_domainmodel_is_not_abstract():
    assert not inspect.isabstract(tExp_Domainmodel)


def test_texp_domainmodel_constructor_exists():
    assert callable(tExp_Domainmodel.__init__)


def test_texp_domainmodel_constructor_args():
    sig = inspect.signature(tExp_Domainmodel.__init__)
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
Constraint_strategy = st.builds(
    Constraint,
)
tExp_Size_strategy = st.builds(
    tExp_Size,
    minSize=
        st.integers(),
    maxSize=
        st.integers()
)
tExp_Cardinality_strategy = st.builds(
    tExp_Cardinality,
    maxCardinality=
        st.integers(),
    minCardinality=
        st.integers()
)
tExp_Singletons_strategy = st.builds(
    tExp_Singletons,
    maxSingletons=
        st.integers(),
    minSingletons=
        st.integers()
)
tExp_Together_strategy = st.builds(
    tExp_Together,
)
Expression_strategy = st.builds(
    Expression,
)
tExp_AndExpr_strategy = st.builds(
    tExp_AndExpr,
)
tExp_FilterExpr_strategy = st.builds(
    tExp_FilterExpr,
)
tExp_UnionExpr_strategy = st.builds(
    tExp_UnionExpr,
)
tExp_SeqExpr_strategy = st.builds(
    tExp_SeqExpr,
)
tExp_CatExpr_strategy = st.builds(
    tExp_CatExpr,
)
tExp_VarExpr_strategy = st.builds(
    tExp_VarExpr,
)
tExp_TerminalExpr_strategy = st.builds(
    tExp_TerminalExpr,
)
tExp_ShuffleExpr_strategy = st.builds(
    tExp_ShuffleExpr,
)
PrologExpression_strategy = st.builds(
    PrologExpression,
)
tExp_StringExpression_strategy = st.builds(
    tExp_StringExpression,
    value=
        safe_text
)
tExp_NumberExpression_strategy = st.builds(
    tExp_NumberExpression,
    value=
        safe_text
)
tExp_VariableExpression_strategy = st.builds(
    tExp_VariableExpression,
    name=
        safe_text
)
tExp_ListExpression_strategy = st.builds(
    tExp_ListExpression,
)
tExp_AtomExpression_strategy = st.builds(
    tExp_AtomExpression,
    atom=
        safe_text
)
tExp_Expression_strategy = st.builds(
    tExp_Expression,
    eps=
        safe_text,
    variable=
        safe_text,
    operator=
        safe_text
)
tExp_Channel_strategy = st.builds(
    tExp_Channel,
    name=
        safe_text,
    reliability=
        safe_text
)
tExp_Constraint_strategy = st.builds(
    tExp_Constraint,
    together=
        safe_text,
    split=
        safe_text,
    parMin=
        safe_text,
    parMax=
        safe_text
)
tExp_Partition_strategy = st.builds(
    tExp_Partition,
)
tExp_Msg_strategy = st.builds(
    tExp_Msg,
    performative=
        safe_text
)
tExp_EventType_strategy = st.builds(
    tExp_EventType,
    name=
        safe_text
)
tExp_Role_strategy = st.builds(
    tExp_Role,
    args=
        safe_text,
    class_=
        safe_text,
    name=
        safe_text
)
tExp_Term_strategy = st.builds(
    tExp_Term,
    name=
        safe_text
)
tExp_PrologExpression_strategy = st.builds(
    tExp_PrologExpression,
    op=
        safe_text
)
tExp_TraceExpression_strategy = st.builds(
    tExp_TraceExpression,
    minimal=
        safe_text,
    modules=
        safe_text,
    guiL=
        safe_text,
    channelsL=
        safe_text,
    partitionL=
        safe_text,
    decentralizedL=
        safe_text,
    bodyL=
        safe_text,
    decentralized=
        safe_text,
    threshold=
        safe_text,
    modulesL=
        safe_text,
    typesL=
        safe_text,
    constraintsL=
        safe_text,
    gui=
        safe_text,
    thresholdL=
        safe_text,
    name=
        safe_text,
    minimalL=
        safe_text,
    rolesL=
        safe_text
)
tExp_Domainmodel_strategy = st.builds(
    tExp_Domainmodel,
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=tExp_Size_strategy)
@settings(max_examples=50)
def test_texp_size_instantiation(instance):
    assert isinstance(instance, tExp_Size)



@given(instance=tExp_Size_strategy)
def test_texp_size_minSize_setter(instance):
    original = instance.minSize
    instance.minSize = original
    assert instance.minSize == original



@given(instance=tExp_Size_strategy)
def test_texp_size_maxSize_setter(instance):
    original = instance.maxSize
    instance.maxSize = original
    assert instance.maxSize == original

@given(instance=tExp_Cardinality_strategy)
@settings(max_examples=50)
def test_texp_cardinality_instantiation(instance):
    assert isinstance(instance, tExp_Cardinality)



@given(instance=tExp_Cardinality_strategy)
def test_texp_cardinality_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original



@given(instance=tExp_Cardinality_strategy)
def test_texp_cardinality_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=tExp_Singletons_strategy)
@settings(max_examples=50)
def test_texp_singletons_instantiation(instance):
    assert isinstance(instance, tExp_Singletons)



@given(instance=tExp_Singletons_strategy)
def test_texp_singletons_maxSingletons_setter(instance):
    original = instance.maxSingletons
    instance.maxSingletons = original
    assert instance.maxSingletons == original



@given(instance=tExp_Singletons_strategy)
def test_texp_singletons_minSingletons_setter(instance):
    original = instance.minSingletons
    instance.minSingletons = original
    assert instance.minSingletons == original

@given(instance=tExp_Together_strategy)
@settings(max_examples=50)
def test_texp_together_instantiation(instance):
    assert isinstance(instance, tExp_Together)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=tExp_AndExpr_strategy)
@settings(max_examples=50)
def test_texp_andexpr_instantiation(instance):
    assert isinstance(instance, tExp_AndExpr)

@given(instance=tExp_FilterExpr_strategy)
@settings(max_examples=50)
def test_texp_filterexpr_instantiation(instance):
    assert isinstance(instance, tExp_FilterExpr)

@given(instance=tExp_UnionExpr_strategy)
@settings(max_examples=50)
def test_texp_unionexpr_instantiation(instance):
    assert isinstance(instance, tExp_UnionExpr)

@given(instance=tExp_SeqExpr_strategy)
@settings(max_examples=50)
def test_texp_seqexpr_instantiation(instance):
    assert isinstance(instance, tExp_SeqExpr)

@given(instance=tExp_CatExpr_strategy)
@settings(max_examples=50)
def test_texp_catexpr_instantiation(instance):
    assert isinstance(instance, tExp_CatExpr)

@given(instance=tExp_VarExpr_strategy)
@settings(max_examples=50)
def test_texp_varexpr_instantiation(instance):
    assert isinstance(instance, tExp_VarExpr)

@given(instance=tExp_TerminalExpr_strategy)
@settings(max_examples=50)
def test_texp_terminalexpr_instantiation(instance):
    assert isinstance(instance, tExp_TerminalExpr)

@given(instance=tExp_ShuffleExpr_strategy)
@settings(max_examples=50)
def test_texp_shuffleexpr_instantiation(instance):
    assert isinstance(instance, tExp_ShuffleExpr)

@given(instance=PrologExpression_strategy)
@settings(max_examples=50)
def test_prologexpression_instantiation(instance):
    assert isinstance(instance, PrologExpression)

@given(instance=tExp_StringExpression_strategy)
@settings(max_examples=50)
def test_texp_stringexpression_instantiation(instance):
    assert isinstance(instance, tExp_StringExpression)



@given(instance=tExp_StringExpression_strategy)
def test_texp_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tExp_NumberExpression_strategy)
@settings(max_examples=50)
def test_texp_numberexpression_instantiation(instance):
    assert isinstance(instance, tExp_NumberExpression)



@given(instance=tExp_NumberExpression_strategy)
def test_texp_numberexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tExp_VariableExpression_strategy)
@settings(max_examples=50)
def test_texp_variableexpression_instantiation(instance):
    assert isinstance(instance, tExp_VariableExpression)



@given(instance=tExp_VariableExpression_strategy)
def test_texp_variableexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp_ListExpression_strategy)
@settings(max_examples=50)
def test_texp_listexpression_instantiation(instance):
    assert isinstance(instance, tExp_ListExpression)

@given(instance=tExp_AtomExpression_strategy)
@settings(max_examples=50)
def test_texp_atomexpression_instantiation(instance):
    assert isinstance(instance, tExp_AtomExpression)



@given(instance=tExp_AtomExpression_strategy)
def test_texp_atomexpression_atom_setter(instance):
    original = instance.atom
    instance.atom = original
    assert instance.atom == original

@given(instance=tExp_Expression_strategy)
@settings(max_examples=50)
def test_texp_expression_instantiation(instance):
    assert isinstance(instance, tExp_Expression)



@given(instance=tExp_Expression_strategy)
def test_texp_expression_eps_setter(instance):
    original = instance.eps
    instance.eps = original
    assert instance.eps == original



@given(instance=tExp_Expression_strategy)
def test_texp_expression_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=tExp_Expression_strategy)
def test_texp_expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=tExp_Channel_strategy)
@settings(max_examples=50)
def test_texp_channel_instantiation(instance):
    assert isinstance(instance, tExp_Channel)



@given(instance=tExp_Channel_strategy)
def test_texp_channel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tExp_Channel_strategy)
def test_texp_channel_reliability_setter(instance):
    original = instance.reliability
    instance.reliability = original
    assert instance.reliability == original

@given(instance=tExp_Constraint_strategy)
@settings(max_examples=50)
def test_texp_constraint_instantiation(instance):
    assert isinstance(instance, tExp_Constraint)



@given(instance=tExp_Constraint_strategy)
def test_texp_constraint_together_setter(instance):
    original = instance.together
    instance.together = original
    assert instance.together == original



@given(instance=tExp_Constraint_strategy)
def test_texp_constraint_split_setter(instance):
    original = instance.split
    instance.split = original
    assert instance.split == original



@given(instance=tExp_Constraint_strategy)
def test_texp_constraint_parMin_setter(instance):
    original = instance.parMin
    instance.parMin = original
    assert instance.parMin == original



@given(instance=tExp_Constraint_strategy)
def test_texp_constraint_parMax_setter(instance):
    original = instance.parMax
    instance.parMax = original
    assert instance.parMax == original

@given(instance=tExp_Partition_strategy)
@settings(max_examples=50)
def test_texp_partition_instantiation(instance):
    assert isinstance(instance, tExp_Partition)

@given(instance=tExp_Msg_strategy)
@settings(max_examples=50)
def test_texp_msg_instantiation(instance):
    assert isinstance(instance, tExp_Msg)



@given(instance=tExp_Msg_strategy)
def test_texp_msg_performative_setter(instance):
    original = instance.performative
    instance.performative = original
    assert instance.performative == original

@given(instance=tExp_EventType_strategy)
@settings(max_examples=50)
def test_texp_eventtype_instantiation(instance):
    assert isinstance(instance, tExp_EventType)



@given(instance=tExp_EventType_strategy)
def test_texp_eventtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp_Role_strategy)
@settings(max_examples=50)
def test_texp_role_instantiation(instance):
    assert isinstance(instance, tExp_Role)



@given(instance=tExp_Role_strategy)
def test_texp_role_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original



@given(instance=tExp_Role_strategy)
def test_texp_role_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=tExp_Role_strategy)
def test_texp_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp_Term_strategy)
@settings(max_examples=50)
def test_texp_term_instantiation(instance):
    assert isinstance(instance, tExp_Term)



@given(instance=tExp_Term_strategy)
def test_texp_term_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp_PrologExpression_strategy)
@settings(max_examples=50)
def test_texp_prologexpression_instantiation(instance):
    assert isinstance(instance, tExp_PrologExpression)



@given(instance=tExp_PrologExpression_strategy)
def test_texp_prologexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tExp_TraceExpression_strategy)
@settings(max_examples=50)
def test_texp_traceexpression_instantiation(instance):
    assert isinstance(instance, tExp_TraceExpression)



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_minimal_setter(instance):
    original = instance.minimal
    instance.minimal = original
    assert instance.minimal == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_modules_setter(instance):
    original = instance.modules
    instance.modules = original
    assert instance.modules == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_guiL_setter(instance):
    original = instance.guiL
    instance.guiL = original
    assert instance.guiL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_channelsL_setter(instance):
    original = instance.channelsL
    instance.channelsL = original
    assert instance.channelsL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_partitionL_setter(instance):
    original = instance.partitionL
    instance.partitionL = original
    assert instance.partitionL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_decentralizedL_setter(instance):
    original = instance.decentralizedL
    instance.decentralizedL = original
    assert instance.decentralizedL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_bodyL_setter(instance):
    original = instance.bodyL
    instance.bodyL = original
    assert instance.bodyL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_decentralized_setter(instance):
    original = instance.decentralized
    instance.decentralized = original
    assert instance.decentralized == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_threshold_setter(instance):
    original = instance.threshold
    instance.threshold = original
    assert instance.threshold == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_modulesL_setter(instance):
    original = instance.modulesL
    instance.modulesL = original
    assert instance.modulesL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_typesL_setter(instance):
    original = instance.typesL
    instance.typesL = original
    assert instance.typesL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_constraintsL_setter(instance):
    original = instance.constraintsL
    instance.constraintsL = original
    assert instance.constraintsL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_gui_setter(instance):
    original = instance.gui
    instance.gui = original
    assert instance.gui == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_thresholdL_setter(instance):
    original = instance.thresholdL
    instance.thresholdL = original
    assert instance.thresholdL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_minimalL_setter(instance):
    original = instance.minimalL
    instance.minimalL = original
    assert instance.minimalL == original



@given(instance=tExp_TraceExpression_strategy)
def test_texp_traceexpression_rolesL_setter(instance):
    original = instance.rolesL
    instance.rolesL = original
    assert instance.rolesL == original

@given(instance=tExp_Domainmodel_strategy)
@settings(max_examples=50)
def test_texp_domainmodel_instantiation(instance):
    assert isinstance(instance, tExp_Domainmodel)

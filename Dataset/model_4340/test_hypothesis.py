import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Constraint,
    tExp::Cardinality,
    tExp::Size,
    tExp::Singletons,
    tExp::Together,
    Expression,
    tExp::CatExpr,
    tExp::UnionExpr,
    tExp::FilterExpr,
    tExp::VarExpr,
    tExp::TerminalExpr,
    tExp::SeqExpr,
    tExp::AndExpr,
    tExp::ShuffleExpr,
    PrologExpression,
    tExp::StringExpression,
    tExp::ListExpression,
    tExp::NumberExpression,
    tExp::VariableExpression,
    tExp::AtomExpression,
    tExp::Expression,
    tExp::Channel,
    tExp::Constraint,
    tExp::Partition,
    tExp::Msg,
    tExp::EventType,
    tExp::Role,
    tExp::Term,
    tExp::PrologExpression,
    tExp::TraceExpression,
    tExp::Domainmodel,
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



def test_texp::cardinality_is_not_abstract():
    assert not inspect.isabstract(tExp::Cardinality)


def test_texp::cardinality_constructor_exists():
    assert callable(tExp::Cardinality.__init__)


def test_texp::cardinality_constructor_args():
    sig = inspect.signature(tExp::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "maxCardinality" in params, "Missing parameter 'maxCardinality'"
    assert "minCardinality" in params, "Missing parameter 'minCardinality'"

def test_texp::cardinality_has_maxCardinality():
    assert hasattr(tExp::Cardinality, "maxCardinality")
    descriptor = None
    for klass in tExp::Cardinality.__mro__:
        if "maxCardinality" in klass.__dict__:
            descriptor = klass.__dict__["maxCardinality"]
            break
    assert isinstance(descriptor, property)

def test_texp::cardinality_has_minCardinality():
    assert hasattr(tExp::Cardinality, "minCardinality")
    descriptor = None
    for klass in tExp::Cardinality.__mro__:
        if "minCardinality" in klass.__dict__:
            descriptor = klass.__dict__["minCardinality"]
            break
    assert isinstance(descriptor, property)



def test_texp::size_is_not_abstract():
    assert not inspect.isabstract(tExp::Size)


def test_texp::size_constructor_exists():
    assert callable(tExp::Size.__init__)


def test_texp::size_constructor_args():
    sig = inspect.signature(tExp::Size.__init__)
    params = list(sig.parameters.keys())
    assert "maxSize" in params, "Missing parameter 'maxSize'"
    assert "minSize" in params, "Missing parameter 'minSize'"

def test_texp::size_has_maxSize():
    assert hasattr(tExp::Size, "maxSize")
    descriptor = None
    for klass in tExp::Size.__mro__:
        if "maxSize" in klass.__dict__:
            descriptor = klass.__dict__["maxSize"]
            break
    assert isinstance(descriptor, property)

def test_texp::size_has_minSize():
    assert hasattr(tExp::Size, "minSize")
    descriptor = None
    for klass in tExp::Size.__mro__:
        if "minSize" in klass.__dict__:
            descriptor = klass.__dict__["minSize"]
            break
    assert isinstance(descriptor, property)



def test_texp::singletons_is_not_abstract():
    assert not inspect.isabstract(tExp::Singletons)


def test_texp::singletons_constructor_exists():
    assert callable(tExp::Singletons.__init__)


def test_texp::singletons_constructor_args():
    sig = inspect.signature(tExp::Singletons.__init__)
    params = list(sig.parameters.keys())
    assert "minSingletons" in params, "Missing parameter 'minSingletons'"
    assert "maxSingletons" in params, "Missing parameter 'maxSingletons'"

def test_texp::singletons_has_minSingletons():
    assert hasattr(tExp::Singletons, "minSingletons")
    descriptor = None
    for klass in tExp::Singletons.__mro__:
        if "minSingletons" in klass.__dict__:
            descriptor = klass.__dict__["minSingletons"]
            break
    assert isinstance(descriptor, property)

def test_texp::singletons_has_maxSingletons():
    assert hasattr(tExp::Singletons, "maxSingletons")
    descriptor = None
    for klass in tExp::Singletons.__mro__:
        if "maxSingletons" in klass.__dict__:
            descriptor = klass.__dict__["maxSingletons"]
            break
    assert isinstance(descriptor, property)



def test_texp::together_is_not_abstract():
    assert not inspect.isabstract(tExp::Together)


def test_texp::together_constructor_exists():
    assert callable(tExp::Together.__init__)


def test_texp::together_constructor_args():
    sig = inspect.signature(tExp::Together.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_texp::catexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::CatExpr)


def test_texp::catexpr_constructor_exists():
    assert callable(tExp::CatExpr.__init__)


def test_texp::catexpr_constructor_args():
    sig = inspect.signature(tExp::CatExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::unionexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::UnionExpr)


def test_texp::unionexpr_constructor_exists():
    assert callable(tExp::UnionExpr.__init__)


def test_texp::unionexpr_constructor_args():
    sig = inspect.signature(tExp::UnionExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::filterexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::FilterExpr)


def test_texp::filterexpr_constructor_exists():
    assert callable(tExp::FilterExpr.__init__)


def test_texp::filterexpr_constructor_args():
    sig = inspect.signature(tExp::FilterExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::varexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::VarExpr)


def test_texp::varexpr_constructor_exists():
    assert callable(tExp::VarExpr.__init__)


def test_texp::varexpr_constructor_args():
    sig = inspect.signature(tExp::VarExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::terminalexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::TerminalExpr)


def test_texp::terminalexpr_constructor_exists():
    assert callable(tExp::TerminalExpr.__init__)


def test_texp::terminalexpr_constructor_args():
    sig = inspect.signature(tExp::TerminalExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::seqexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::SeqExpr)


def test_texp::seqexpr_constructor_exists():
    assert callable(tExp::SeqExpr.__init__)


def test_texp::seqexpr_constructor_args():
    sig = inspect.signature(tExp::SeqExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::andexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::AndExpr)


def test_texp::andexpr_constructor_exists():
    assert callable(tExp::AndExpr.__init__)


def test_texp::andexpr_constructor_args():
    sig = inspect.signature(tExp::AndExpr.__init__)
    params = list(sig.parameters.keys())



def test_texp::shuffleexpr_is_not_abstract():
    assert not inspect.isabstract(tExp::ShuffleExpr)


def test_texp::shuffleexpr_constructor_exists():
    assert callable(tExp::ShuffleExpr.__init__)


def test_texp::shuffleexpr_constructor_args():
    sig = inspect.signature(tExp::ShuffleExpr.__init__)
    params = list(sig.parameters.keys())



def test_prologexpression_is_not_abstract():
    assert not inspect.isabstract(PrologExpression)


def test_prologexpression_constructor_exists():
    assert callable(PrologExpression.__init__)


def test_prologexpression_constructor_args():
    sig = inspect.signature(PrologExpression.__init__)
    params = list(sig.parameters.keys())



def test_texp::stringexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::StringExpression)


def test_texp::stringexpression_constructor_exists():
    assert callable(tExp::StringExpression.__init__)


def test_texp::stringexpression_constructor_args():
    sig = inspect.signature(tExp::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_texp::stringexpression_has_value():
    assert hasattr(tExp::StringExpression, "value")
    descriptor = None
    for klass in tExp::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_texp::listexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::ListExpression)


def test_texp::listexpression_constructor_exists():
    assert callable(tExp::ListExpression.__init__)


def test_texp::listexpression_constructor_args():
    sig = inspect.signature(tExp::ListExpression.__init__)
    params = list(sig.parameters.keys())



def test_texp::numberexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::NumberExpression)


def test_texp::numberexpression_constructor_exists():
    assert callable(tExp::NumberExpression.__init__)


def test_texp::numberexpression_constructor_args():
    sig = inspect.signature(tExp::NumberExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_texp::numberexpression_has_value():
    assert hasattr(tExp::NumberExpression, "value")
    descriptor = None
    for klass in tExp::NumberExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_texp::variableexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::VariableExpression)


def test_texp::variableexpression_constructor_exists():
    assert callable(tExp::VariableExpression.__init__)


def test_texp::variableexpression_constructor_args():
    sig = inspect.signature(tExp::VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp::variableexpression_has_name():
    assert hasattr(tExp::VariableExpression, "name")
    descriptor = None
    for klass in tExp::VariableExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp::atomexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::AtomExpression)


def test_texp::atomexpression_constructor_exists():
    assert callable(tExp::AtomExpression.__init__)


def test_texp::atomexpression_constructor_args():
    sig = inspect.signature(tExp::AtomExpression.__init__)
    params = list(sig.parameters.keys())
    assert "atom" in params, "Missing parameter 'atom'"

def test_texp::atomexpression_has_atom():
    assert hasattr(tExp::AtomExpression, "atom")
    descriptor = None
    for klass in tExp::AtomExpression.__mro__:
        if "atom" in klass.__dict__:
            descriptor = klass.__dict__["atom"]
            break
    assert isinstance(descriptor, property)



def test_texp::expression_is_not_abstract():
    assert not inspect.isabstract(tExp::Expression)


def test_texp::expression_constructor_exists():
    assert callable(tExp::Expression.__init__)


def test_texp::expression_constructor_args():
    sig = inspect.signature(tExp::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "operator" in params, "Missing parameter 'operator'"
    assert "eps" in params, "Missing parameter 'eps'"

def test_texp::expression_has_variable():
    assert hasattr(tExp::Expression, "variable")
    descriptor = None
    for klass in tExp::Expression.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_texp::expression_has_operator():
    assert hasattr(tExp::Expression, "operator")
    descriptor = None
    for klass in tExp::Expression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_texp::expression_has_eps():
    assert hasattr(tExp::Expression, "eps")
    descriptor = None
    for klass in tExp::Expression.__mro__:
        if "eps" in klass.__dict__:
            descriptor = klass.__dict__["eps"]
            break
    assert isinstance(descriptor, property)



def test_texp::channel_is_not_abstract():
    assert not inspect.isabstract(tExp::Channel)


def test_texp::channel_constructor_exists():
    assert callable(tExp::Channel.__init__)


def test_texp::channel_constructor_args():
    sig = inspect.signature(tExp::Channel.__init__)
    params = list(sig.parameters.keys())
    assert "reliability" in params, "Missing parameter 'reliability'"
    assert "name" in params, "Missing parameter 'name'"

def test_texp::channel_has_reliability():
    assert hasattr(tExp::Channel, "reliability")
    descriptor = None
    for klass in tExp::Channel.__mro__:
        if "reliability" in klass.__dict__:
            descriptor = klass.__dict__["reliability"]
            break
    assert isinstance(descriptor, property)

def test_texp::channel_has_name():
    assert hasattr(tExp::Channel, "name")
    descriptor = None
    for klass in tExp::Channel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp::constraint_is_not_abstract():
    assert not inspect.isabstract(tExp::Constraint)


def test_texp::constraint_constructor_exists():
    assert callable(tExp::Constraint.__init__)


def test_texp::constraint_constructor_args():
    sig = inspect.signature(tExp::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "split" in params, "Missing parameter 'split'"
    assert "parMax" in params, "Missing parameter 'parMax'"
    assert "parMin" in params, "Missing parameter 'parMin'"
    assert "together" in params, "Missing parameter 'together'"

def test_texp::constraint_has_split():
    assert hasattr(tExp::Constraint, "split")
    descriptor = None
    for klass in tExp::Constraint.__mro__:
        if "split" in klass.__dict__:
            descriptor = klass.__dict__["split"]
            break
    assert isinstance(descriptor, property)

def test_texp::constraint_has_parMax():
    assert hasattr(tExp::Constraint, "parMax")
    descriptor = None
    for klass in tExp::Constraint.__mro__:
        if "parMax" in klass.__dict__:
            descriptor = klass.__dict__["parMax"]
            break
    assert isinstance(descriptor, property)

def test_texp::constraint_has_parMin():
    assert hasattr(tExp::Constraint, "parMin")
    descriptor = None
    for klass in tExp::Constraint.__mro__:
        if "parMin" in klass.__dict__:
            descriptor = klass.__dict__["parMin"]
            break
    assert isinstance(descriptor, property)

def test_texp::constraint_has_together():
    assert hasattr(tExp::Constraint, "together")
    descriptor = None
    for klass in tExp::Constraint.__mro__:
        if "together" in klass.__dict__:
            descriptor = klass.__dict__["together"]
            break
    assert isinstance(descriptor, property)



def test_texp::partition_is_not_abstract():
    assert not inspect.isabstract(tExp::Partition)


def test_texp::partition_constructor_exists():
    assert callable(tExp::Partition.__init__)


def test_texp::partition_constructor_args():
    sig = inspect.signature(tExp::Partition.__init__)
    params = list(sig.parameters.keys())



def test_texp::msg_is_not_abstract():
    assert not inspect.isabstract(tExp::Msg)


def test_texp::msg_constructor_exists():
    assert callable(tExp::Msg.__init__)


def test_texp::msg_constructor_args():
    sig = inspect.signature(tExp::Msg.__init__)
    params = list(sig.parameters.keys())
    assert "performative" in params, "Missing parameter 'performative'"

def test_texp::msg_has_performative():
    assert hasattr(tExp::Msg, "performative")
    descriptor = None
    for klass in tExp::Msg.__mro__:
        if "performative" in klass.__dict__:
            descriptor = klass.__dict__["performative"]
            break
    assert isinstance(descriptor, property)



def test_texp::eventtype_is_not_abstract():
    assert not inspect.isabstract(tExp::EventType)


def test_texp::eventtype_constructor_exists():
    assert callable(tExp::EventType.__init__)


def test_texp::eventtype_constructor_args():
    sig = inspect.signature(tExp::EventType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp::eventtype_has_name():
    assert hasattr(tExp::EventType, "name")
    descriptor = None
    for klass in tExp::EventType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp::role_is_not_abstract():
    assert not inspect.isabstract(tExp::Role)


def test_texp::role_constructor_exists():
    assert callable(tExp::Role.__init__)


def test_texp::role_constructor_args():
    sig = inspect.signature(tExp::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "args" in params, "Missing parameter 'args'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_texp::role_has_name():
    assert hasattr(tExp::Role, "name")
    descriptor = None
    for klass in tExp::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_texp::role_has_args():
    assert hasattr(tExp::Role, "args")
    descriptor = None
    for klass in tExp::Role.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_texp::role_has_class_():
    assert hasattr(tExp::Role, "class_")
    descriptor = None
    for klass in tExp::Role.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_texp::term_is_not_abstract():
    assert not inspect.isabstract(tExp::Term)


def test_texp::term_constructor_exists():
    assert callable(tExp::Term.__init__)


def test_texp::term_constructor_args():
    sig = inspect.signature(tExp::Term.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_texp::term_has_name():
    assert hasattr(tExp::Term, "name")
    descriptor = None
    for klass in tExp::Term.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_texp::prologexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::PrologExpression)


def test_texp::prologexpression_constructor_exists():
    assert callable(tExp::PrologExpression.__init__)


def test_texp::prologexpression_constructor_args():
    sig = inspect.signature(tExp::PrologExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_texp::prologexpression_has_op():
    assert hasattr(tExp::PrologExpression, "op")
    descriptor = None
    for klass in tExp::PrologExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_texp::traceexpression_is_not_abstract():
    assert not inspect.isabstract(tExp::TraceExpression)


def test_texp::traceexpression_constructor_exists():
    assert callable(tExp::TraceExpression.__init__)


def test_texp::traceexpression_constructor_args():
    sig = inspect.signature(tExp::TraceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "modulesL" in params, "Missing parameter 'modulesL'"
    assert "threshold" in params, "Missing parameter 'threshold'"
    assert "modules" in params, "Missing parameter 'modules'"
    assert "rolesL" in params, "Missing parameter 'rolesL'"
    assert "bodyL" in params, "Missing parameter 'bodyL'"
    assert "minimalL" in params, "Missing parameter 'minimalL'"
    assert "constraintsL" in params, "Missing parameter 'constraintsL'"
    assert "typesL" in params, "Missing parameter 'typesL'"
    assert "guiL" in params, "Missing parameter 'guiL'"
    assert "decentralizedL" in params, "Missing parameter 'decentralizedL'"
    assert "gui" in params, "Missing parameter 'gui'"
    assert "name" in params, "Missing parameter 'name'"
    assert "decentralized" in params, "Missing parameter 'decentralized'"
    assert "partitionL" in params, "Missing parameter 'partitionL'"
    assert "minimal" in params, "Missing parameter 'minimal'"
    assert "thresholdL" in params, "Missing parameter 'thresholdL'"
    assert "channelsL" in params, "Missing parameter 'channelsL'"

def test_texp::traceexpression_has_modulesL():
    assert hasattr(tExp::TraceExpression, "modulesL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "modulesL" in klass.__dict__:
            descriptor = klass.__dict__["modulesL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_threshold():
    assert hasattr(tExp::TraceExpression, "threshold")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "threshold" in klass.__dict__:
            descriptor = klass.__dict__["threshold"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_modules():
    assert hasattr(tExp::TraceExpression, "modules")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "modules" in klass.__dict__:
            descriptor = klass.__dict__["modules"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_rolesL():
    assert hasattr(tExp::TraceExpression, "rolesL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "rolesL" in klass.__dict__:
            descriptor = klass.__dict__["rolesL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_bodyL():
    assert hasattr(tExp::TraceExpression, "bodyL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "bodyL" in klass.__dict__:
            descriptor = klass.__dict__["bodyL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_minimalL():
    assert hasattr(tExp::TraceExpression, "minimalL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "minimalL" in klass.__dict__:
            descriptor = klass.__dict__["minimalL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_constraintsL():
    assert hasattr(tExp::TraceExpression, "constraintsL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "constraintsL" in klass.__dict__:
            descriptor = klass.__dict__["constraintsL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_typesL():
    assert hasattr(tExp::TraceExpression, "typesL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "typesL" in klass.__dict__:
            descriptor = klass.__dict__["typesL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_guiL():
    assert hasattr(tExp::TraceExpression, "guiL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "guiL" in klass.__dict__:
            descriptor = klass.__dict__["guiL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_decentralizedL():
    assert hasattr(tExp::TraceExpression, "decentralizedL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "decentralizedL" in klass.__dict__:
            descriptor = klass.__dict__["decentralizedL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_gui():
    assert hasattr(tExp::TraceExpression, "gui")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "gui" in klass.__dict__:
            descriptor = klass.__dict__["gui"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_name():
    assert hasattr(tExp::TraceExpression, "name")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_decentralized():
    assert hasattr(tExp::TraceExpression, "decentralized")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "decentralized" in klass.__dict__:
            descriptor = klass.__dict__["decentralized"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_partitionL():
    assert hasattr(tExp::TraceExpression, "partitionL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "partitionL" in klass.__dict__:
            descriptor = klass.__dict__["partitionL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_minimal():
    assert hasattr(tExp::TraceExpression, "minimal")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "minimal" in klass.__dict__:
            descriptor = klass.__dict__["minimal"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_thresholdL():
    assert hasattr(tExp::TraceExpression, "thresholdL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "thresholdL" in klass.__dict__:
            descriptor = klass.__dict__["thresholdL"]
            break
    assert isinstance(descriptor, property)

def test_texp::traceexpression_has_channelsL():
    assert hasattr(tExp::TraceExpression, "channelsL")
    descriptor = None
    for klass in tExp::TraceExpression.__mro__:
        if "channelsL" in klass.__dict__:
            descriptor = klass.__dict__["channelsL"]
            break
    assert isinstance(descriptor, property)



def test_texp::domainmodel_is_not_abstract():
    assert not inspect.isabstract(tExp::Domainmodel)


def test_texp::domainmodel_constructor_exists():
    assert callable(tExp::Domainmodel.__init__)


def test_texp::domainmodel_constructor_args():
    sig = inspect.signature(tExp::Domainmodel.__init__)
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
tExp::Cardinality_strategy = st.builds(
    tExp::Cardinality,
    maxCardinality=
        st.integers(),
    minCardinality=
        st.integers()
)
tExp::Size_strategy = st.builds(
    tExp::Size,
    maxSize=
        st.integers(),
    minSize=
        st.integers()
)
tExp::Singletons_strategy = st.builds(
    tExp::Singletons,
    minSingletons=
        st.integers(),
    maxSingletons=
        st.integers()
)
tExp::Together_strategy = st.builds(
    tExp::Together,
)
Expression_strategy = st.builds(
    Expression,
)
tExp::CatExpr_strategy = st.builds(
    tExp::CatExpr,
)
tExp::UnionExpr_strategy = st.builds(
    tExp::UnionExpr,
)
tExp::FilterExpr_strategy = st.builds(
    tExp::FilterExpr,
)
tExp::VarExpr_strategy = st.builds(
    tExp::VarExpr,
)
tExp::TerminalExpr_strategy = st.builds(
    tExp::TerminalExpr,
)
tExp::SeqExpr_strategy = st.builds(
    tExp::SeqExpr,
)
tExp::AndExpr_strategy = st.builds(
    tExp::AndExpr,
)
tExp::ShuffleExpr_strategy = st.builds(
    tExp::ShuffleExpr,
)
PrologExpression_strategy = st.builds(
    PrologExpression,
)
tExp::StringExpression_strategy = st.builds(
    tExp::StringExpression,
    value=
        safe_text
)
tExp::ListExpression_strategy = st.builds(
    tExp::ListExpression,
)
tExp::NumberExpression_strategy = st.builds(
    tExp::NumberExpression,
    value=
        safe_text
)
tExp::VariableExpression_strategy = st.builds(
    tExp::VariableExpression,
    name=
        safe_text
)
tExp::AtomExpression_strategy = st.builds(
    tExp::AtomExpression,
    atom=
        safe_text
)
tExp::Expression_strategy = st.builds(
    tExp::Expression,
    variable=
        safe_text,
    operator=
        safe_text,
    eps=
        safe_text
)
tExp::Channel_strategy = st.builds(
    tExp::Channel,
    reliability=
        safe_text,
    name=
        safe_text
)
tExp::Constraint_strategy = st.builds(
    tExp::Constraint,
    split=
        safe_text,
    parMax=
        safe_text,
    parMin=
        safe_text,
    together=
        safe_text
)
tExp::Partition_strategy = st.builds(
    tExp::Partition,
)
tExp::Msg_strategy = st.builds(
    tExp::Msg,
    performative=
        safe_text
)
tExp::EventType_strategy = st.builds(
    tExp::EventType,
    name=
        safe_text
)
tExp::Role_strategy = st.builds(
    tExp::Role,
    name=
        safe_text,
    args=
        safe_text,
    class_=
        safe_text
)
tExp::Term_strategy = st.builds(
    tExp::Term,
    name=
        safe_text
)
tExp::PrologExpression_strategy = st.builds(
    tExp::PrologExpression,
    op=
        safe_text
)
tExp::TraceExpression_strategy = st.builds(
    tExp::TraceExpression,
    modulesL=
        safe_text,
    threshold=
        safe_text,
    modules=
        safe_text,
    rolesL=
        safe_text,
    bodyL=
        safe_text,
    minimalL=
        safe_text,
    constraintsL=
        safe_text,
    typesL=
        safe_text,
    guiL=
        safe_text,
    decentralizedL=
        safe_text,
    gui=
        safe_text,
    name=
        safe_text,
    decentralized=
        safe_text,
    partitionL=
        safe_text,
    minimal=
        safe_text,
    thresholdL=
        safe_text,
    channelsL=
        safe_text
)
tExp::Domainmodel_strategy = st.builds(
    tExp::Domainmodel,
)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=tExp::Cardinality_strategy)
@settings(max_examples=50)
def test_texp::cardinality_instantiation(instance):
    assert isinstance(instance, tExp::Cardinality)

@given(instance=tExp::Cardinality_strategy)
def test_texp::cardinality_maxCardinality_type(instance):
    assert isinstance(instance.maxCardinality, int)


@given(instance=tExp::Cardinality_strategy)
def test_texp::cardinality_maxCardinality_setter(instance):
    original = instance.maxCardinality
    instance.maxCardinality = original
    assert instance.maxCardinality == original

@given(instance=tExp::Cardinality_strategy)
def test_texp::cardinality_minCardinality_type(instance):
    assert isinstance(instance.minCardinality, int)


@given(instance=tExp::Cardinality_strategy)
def test_texp::cardinality_minCardinality_setter(instance):
    original = instance.minCardinality
    instance.minCardinality = original
    assert instance.minCardinality == original

@given(instance=tExp::Size_strategy)
@settings(max_examples=50)
def test_texp::size_instantiation(instance):
    assert isinstance(instance, tExp::Size)

@given(instance=tExp::Size_strategy)
def test_texp::size_maxSize_type(instance):
    assert isinstance(instance.maxSize, int)


@given(instance=tExp::Size_strategy)
def test_texp::size_maxSize_setter(instance):
    original = instance.maxSize
    instance.maxSize = original
    assert instance.maxSize == original

@given(instance=tExp::Size_strategy)
def test_texp::size_minSize_type(instance):
    assert isinstance(instance.minSize, int)


@given(instance=tExp::Size_strategy)
def test_texp::size_minSize_setter(instance):
    original = instance.minSize
    instance.minSize = original
    assert instance.minSize == original

@given(instance=tExp::Singletons_strategy)
@settings(max_examples=50)
def test_texp::singletons_instantiation(instance):
    assert isinstance(instance, tExp::Singletons)

@given(instance=tExp::Singletons_strategy)
def test_texp::singletons_minSingletons_type(instance):
    assert isinstance(instance.minSingletons, int)


@given(instance=tExp::Singletons_strategy)
def test_texp::singletons_minSingletons_setter(instance):
    original = instance.minSingletons
    instance.minSingletons = original
    assert instance.minSingletons == original

@given(instance=tExp::Singletons_strategy)
def test_texp::singletons_maxSingletons_type(instance):
    assert isinstance(instance.maxSingletons, int)


@given(instance=tExp::Singletons_strategy)
def test_texp::singletons_maxSingletons_setter(instance):
    original = instance.maxSingletons
    instance.maxSingletons = original
    assert instance.maxSingletons == original

@given(instance=tExp::Together_strategy)
@settings(max_examples=50)
def test_texp::together_instantiation(instance):
    assert isinstance(instance, tExp::Together)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=tExp::CatExpr_strategy)
@settings(max_examples=50)
def test_texp::catexpr_instantiation(instance):
    assert isinstance(instance, tExp::CatExpr)

@given(instance=tExp::UnionExpr_strategy)
@settings(max_examples=50)
def test_texp::unionexpr_instantiation(instance):
    assert isinstance(instance, tExp::UnionExpr)

@given(instance=tExp::FilterExpr_strategy)
@settings(max_examples=50)
def test_texp::filterexpr_instantiation(instance):
    assert isinstance(instance, tExp::FilterExpr)

@given(instance=tExp::VarExpr_strategy)
@settings(max_examples=50)
def test_texp::varexpr_instantiation(instance):
    assert isinstance(instance, tExp::VarExpr)

@given(instance=tExp::TerminalExpr_strategy)
@settings(max_examples=50)
def test_texp::terminalexpr_instantiation(instance):
    assert isinstance(instance, tExp::TerminalExpr)

@given(instance=tExp::SeqExpr_strategy)
@settings(max_examples=50)
def test_texp::seqexpr_instantiation(instance):
    assert isinstance(instance, tExp::SeqExpr)

@given(instance=tExp::AndExpr_strategy)
@settings(max_examples=50)
def test_texp::andexpr_instantiation(instance):
    assert isinstance(instance, tExp::AndExpr)

@given(instance=tExp::ShuffleExpr_strategy)
@settings(max_examples=50)
def test_texp::shuffleexpr_instantiation(instance):
    assert isinstance(instance, tExp::ShuffleExpr)

@given(instance=PrologExpression_strategy)
@settings(max_examples=50)
def test_prologexpression_instantiation(instance):
    assert isinstance(instance, PrologExpression)

@given(instance=tExp::StringExpression_strategy)
@settings(max_examples=50)
def test_texp::stringexpression_instantiation(instance):
    assert isinstance(instance, tExp::StringExpression)

@given(instance=tExp::StringExpression_strategy)
def test_texp::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tExp::StringExpression_strategy)
def test_texp::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tExp::ListExpression_strategy)
@settings(max_examples=50)
def test_texp::listexpression_instantiation(instance):
    assert isinstance(instance, tExp::ListExpression)

@given(instance=tExp::NumberExpression_strategy)
@settings(max_examples=50)
def test_texp::numberexpression_instantiation(instance):
    assert isinstance(instance, tExp::NumberExpression)

@given(instance=tExp::NumberExpression_strategy)
def test_texp::numberexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tExp::NumberExpression_strategy)
def test_texp::numberexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tExp::VariableExpression_strategy)
@settings(max_examples=50)
def test_texp::variableexpression_instantiation(instance):
    assert isinstance(instance, tExp::VariableExpression)

@given(instance=tExp::VariableExpression_strategy)
def test_texp::variableexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::VariableExpression_strategy)
def test_texp::variableexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::AtomExpression_strategy)
@settings(max_examples=50)
def test_texp::atomexpression_instantiation(instance):
    assert isinstance(instance, tExp::AtomExpression)

@given(instance=tExp::AtomExpression_strategy)
def test_texp::atomexpression_atom_type(instance):
    assert isinstance(instance.atom, str)


@given(instance=tExp::AtomExpression_strategy)
def test_texp::atomexpression_atom_setter(instance):
    original = instance.atom
    instance.atom = original
    assert instance.atom == original

@given(instance=tExp::Expression_strategy)
@settings(max_examples=50)
def test_texp::expression_instantiation(instance):
    assert isinstance(instance, tExp::Expression)

@given(instance=tExp::Expression_strategy)
def test_texp::expression_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=tExp::Expression_strategy)
def test_texp::expression_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=tExp::Expression_strategy)
def test_texp::expression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=tExp::Expression_strategy)
def test_texp::expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=tExp::Expression_strategy)
def test_texp::expression_eps_type(instance):
    assert isinstance(instance.eps, str)


@given(instance=tExp::Expression_strategy)
def test_texp::expression_eps_setter(instance):
    original = instance.eps
    instance.eps = original
    assert instance.eps == original

@given(instance=tExp::Channel_strategy)
@settings(max_examples=50)
def test_texp::channel_instantiation(instance):
    assert isinstance(instance, tExp::Channel)

@given(instance=tExp::Channel_strategy)
def test_texp::channel_reliability_type(instance):
    assert isinstance(instance.reliability, str)


@given(instance=tExp::Channel_strategy)
def test_texp::channel_reliability_setter(instance):
    original = instance.reliability
    instance.reliability = original
    assert instance.reliability == original

@given(instance=tExp::Channel_strategy)
def test_texp::channel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::Channel_strategy)
def test_texp::channel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::Constraint_strategy)
@settings(max_examples=50)
def test_texp::constraint_instantiation(instance):
    assert isinstance(instance, tExp::Constraint)

@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_split_type(instance):
    assert isinstance(instance.split, str)


@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_split_setter(instance):
    original = instance.split
    instance.split = original
    assert instance.split == original

@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_parMax_type(instance):
    assert isinstance(instance.parMax, str)


@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_parMax_setter(instance):
    original = instance.parMax
    instance.parMax = original
    assert instance.parMax == original

@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_parMin_type(instance):
    assert isinstance(instance.parMin, str)


@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_parMin_setter(instance):
    original = instance.parMin
    instance.parMin = original
    assert instance.parMin == original

@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_together_type(instance):
    assert isinstance(instance.together, str)


@given(instance=tExp::Constraint_strategy)
def test_texp::constraint_together_setter(instance):
    original = instance.together
    instance.together = original
    assert instance.together == original

@given(instance=tExp::Partition_strategy)
@settings(max_examples=50)
def test_texp::partition_instantiation(instance):
    assert isinstance(instance, tExp::Partition)

@given(instance=tExp::Msg_strategy)
@settings(max_examples=50)
def test_texp::msg_instantiation(instance):
    assert isinstance(instance, tExp::Msg)

@given(instance=tExp::Msg_strategy)
def test_texp::msg_performative_type(instance):
    assert isinstance(instance.performative, str)


@given(instance=tExp::Msg_strategy)
def test_texp::msg_performative_setter(instance):
    original = instance.performative
    instance.performative = original
    assert instance.performative == original

@given(instance=tExp::EventType_strategy)
@settings(max_examples=50)
def test_texp::eventtype_instantiation(instance):
    assert isinstance(instance, tExp::EventType)

@given(instance=tExp::EventType_strategy)
def test_texp::eventtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::EventType_strategy)
def test_texp::eventtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::Role_strategy)
@settings(max_examples=50)
def test_texp::role_instantiation(instance):
    assert isinstance(instance, tExp::Role)

@given(instance=tExp::Role_strategy)
def test_texp::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::Role_strategy)
def test_texp::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::Role_strategy)
def test_texp::role_args_type(instance):
    assert isinstance(instance.args, str)


@given(instance=tExp::Role_strategy)
def test_texp::role_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=tExp::Role_strategy)
def test_texp::role_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=tExp::Role_strategy)
def test_texp::role_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=tExp::Term_strategy)
@settings(max_examples=50)
def test_texp::term_instantiation(instance):
    assert isinstance(instance, tExp::Term)

@given(instance=tExp::Term_strategy)
def test_texp::term_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::Term_strategy)
def test_texp::term_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::PrologExpression_strategy)
@settings(max_examples=50)
def test_texp::prologexpression_instantiation(instance):
    assert isinstance(instance, tExp::PrologExpression)

@given(instance=tExp::PrologExpression_strategy)
def test_texp::prologexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tExp::PrologExpression_strategy)
def test_texp::prologexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tExp::TraceExpression_strategy)
@settings(max_examples=50)
def test_texp::traceexpression_instantiation(instance):
    assert isinstance(instance, tExp::TraceExpression)

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_modulesL_type(instance):
    assert isinstance(instance.modulesL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_modulesL_setter(instance):
    original = instance.modulesL
    instance.modulesL = original
    assert instance.modulesL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_threshold_type(instance):
    assert isinstance(instance.threshold, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_threshold_setter(instance):
    original = instance.threshold
    instance.threshold = original
    assert instance.threshold == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_modules_type(instance):
    assert isinstance(instance.modules, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_modules_setter(instance):
    original = instance.modules
    instance.modules = original
    assert instance.modules == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_rolesL_type(instance):
    assert isinstance(instance.rolesL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_rolesL_setter(instance):
    original = instance.rolesL
    instance.rolesL = original
    assert instance.rolesL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_bodyL_type(instance):
    assert isinstance(instance.bodyL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_bodyL_setter(instance):
    original = instance.bodyL
    instance.bodyL = original
    assert instance.bodyL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_minimalL_type(instance):
    assert isinstance(instance.minimalL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_minimalL_setter(instance):
    original = instance.minimalL
    instance.minimalL = original
    assert instance.minimalL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_constraintsL_type(instance):
    assert isinstance(instance.constraintsL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_constraintsL_setter(instance):
    original = instance.constraintsL
    instance.constraintsL = original
    assert instance.constraintsL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_typesL_type(instance):
    assert isinstance(instance.typesL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_typesL_setter(instance):
    original = instance.typesL
    instance.typesL = original
    assert instance.typesL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_guiL_type(instance):
    assert isinstance(instance.guiL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_guiL_setter(instance):
    original = instance.guiL
    instance.guiL = original
    assert instance.guiL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_decentralizedL_type(instance):
    assert isinstance(instance.decentralizedL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_decentralizedL_setter(instance):
    original = instance.decentralizedL
    instance.decentralizedL = original
    assert instance.decentralizedL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_gui_type(instance):
    assert isinstance(instance.gui, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_gui_setter(instance):
    original = instance.gui
    instance.gui = original
    assert instance.gui == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_decentralized_type(instance):
    assert isinstance(instance.decentralized, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_decentralized_setter(instance):
    original = instance.decentralized
    instance.decentralized = original
    assert instance.decentralized == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_partitionL_type(instance):
    assert isinstance(instance.partitionL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_partitionL_setter(instance):
    original = instance.partitionL
    instance.partitionL = original
    assert instance.partitionL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_minimal_type(instance):
    assert isinstance(instance.minimal, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_minimal_setter(instance):
    original = instance.minimal
    instance.minimal = original
    assert instance.minimal == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_thresholdL_type(instance):
    assert isinstance(instance.thresholdL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_thresholdL_setter(instance):
    original = instance.thresholdL
    instance.thresholdL = original
    assert instance.thresholdL == original

@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_channelsL_type(instance):
    assert isinstance(instance.channelsL, str)


@given(instance=tExp::TraceExpression_strategy)
def test_texp::traceexpression_channelsL_setter(instance):
    original = instance.channelsL
    instance.channelsL = original
    assert instance.channelsL == original

@given(instance=tExp::Domainmodel_strategy)
@settings(max_examples=50)
def test_texp::domainmodel_instantiation(instance):
    assert isinstance(instance, tExp::Domainmodel)

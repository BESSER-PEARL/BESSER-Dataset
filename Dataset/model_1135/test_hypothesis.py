import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gpfl::State,
    GExpression,
    gpfl::AutomatonCmd,
    gpfl::OutPort,
    gpfl::CmdAdd,
    gpfl::SetCmd,
    gpfl::InPort,
    gpfl::IterStmt,
    gpfl::StringLit,
    gpfl::Variable,
    gpfl::CmdGCompare,
    gpfl::AlarmCmd,
    gpfl::CmdGECompare,
    gpfl::CmdEq,
    gpfl::NopCmd,
    gpfl::CmdAnd,
    gpfl::CmdNEq,
    gpfl::GBoolFalse,
    gpfl::IntLitCmd,
    gpfl::PortLit,
    gpfl::DropCmd,
    gpfl::AcceptCmd,
    gpfl::InterruptStmt,
    gpfl::GBoolTrue,
    gpfl::CmdLCompare,
    gpfl::StpCmd,
    gpfl::SendCmd,
    gpfl::CmdLECompare,
    gpfl::CmdSub,
    gpfl::CondStmt,
    gpfl::Transition,
    gpfl::Field,
    gpfl::GExpression,
    gpfl::AutomataDef,
    gpfl::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gpfl::state_is_not_abstract():
    assert not inspect.isabstract(gpfl::State)


def test_gpfl::state_constructor_exists():
    assert callable(gpfl::State.__init__)


def test_gpfl::state_constructor_args():
    sig = inspect.signature(gpfl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::state_has_name():
    assert hasattr(gpfl::State, "name")
    descriptor = None
    for klass in gpfl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gexpression_is_not_abstract():
    assert not inspect.isabstract(GExpression)


def test_gexpression_constructor_exists():
    assert callable(GExpression.__init__)


def test_gexpression_constructor_args():
    sig = inspect.signature(GExpression.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::automatoncmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::AutomatonCmd)


def test_gpfl::automatoncmd_constructor_exists():
    assert callable(gpfl::AutomatonCmd.__init__)


def test_gpfl::automatoncmd_constructor_args():
    sig = inspect.signature(gpfl::AutomatonCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::automatoncmd_has_name():
    assert hasattr(gpfl::AutomatonCmd, "name")
    descriptor = None
    for klass in gpfl::AutomatonCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::outport_is_not_abstract():
    assert not inspect.isabstract(gpfl::OutPort)


def test_gpfl::outport_constructor_exists():
    assert callable(gpfl::OutPort.__init__)


def test_gpfl::outport_constructor_args():
    sig = inspect.signature(gpfl::OutPort.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdadd_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdAdd)


def test_gpfl::cmdadd_constructor_exists():
    assert callable(gpfl::CmdAdd.__init__)


def test_gpfl::cmdadd_constructor_args():
    sig = inspect.signature(gpfl::CmdAdd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::setcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::SetCmd)


def test_gpfl::setcmd_constructor_exists():
    assert callable(gpfl::SetCmd.__init__)


def test_gpfl::setcmd_constructor_args():
    sig = inspect.signature(gpfl::SetCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::setcmd_has_name():
    assert hasattr(gpfl::SetCmd, "name")
    descriptor = None
    for klass in gpfl::SetCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::inport_is_not_abstract():
    assert not inspect.isabstract(gpfl::InPort)


def test_gpfl::inport_constructor_exists():
    assert callable(gpfl::InPort.__init__)


def test_gpfl::inport_constructor_args():
    sig = inspect.signature(gpfl::InPort.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::iterstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl::IterStmt)


def test_gpfl::iterstmt_constructor_exists():
    assert callable(gpfl::IterStmt.__init__)


def test_gpfl::iterstmt_constructor_args():
    sig = inspect.signature(gpfl::IterStmt.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::stringlit_is_not_abstract():
    assert not inspect.isabstract(gpfl::StringLit)


def test_gpfl::stringlit_constructor_exists():
    assert callable(gpfl::StringLit.__init__)


def test_gpfl::stringlit_constructor_args():
    sig = inspect.signature(gpfl::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl::stringlit_has_value():
    assert hasattr(gpfl::StringLit, "value")
    descriptor = None
    for klass in gpfl::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::variable_is_not_abstract():
    assert not inspect.isabstract(gpfl::Variable)


def test_gpfl::variable_constructor_exists():
    assert callable(gpfl::Variable.__init__)


def test_gpfl::variable_constructor_args():
    sig = inspect.signature(gpfl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl::variable_has_value():
    assert hasattr(gpfl::Variable, "value")
    descriptor = None
    for klass in gpfl::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::cmdgcompare_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdGCompare)


def test_gpfl::cmdgcompare_constructor_exists():
    assert callable(gpfl::CmdGCompare.__init__)


def test_gpfl::cmdgcompare_constructor_args():
    sig = inspect.signature(gpfl::CmdGCompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::alarmcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::AlarmCmd)


def test_gpfl::alarmcmd_constructor_exists():
    assert callable(gpfl::AlarmCmd.__init__)


def test_gpfl::alarmcmd_constructor_args():
    sig = inspect.signature(gpfl::AlarmCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdgecompare_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdGECompare)


def test_gpfl::cmdgecompare_constructor_exists():
    assert callable(gpfl::CmdGECompare.__init__)


def test_gpfl::cmdgecompare_constructor_args():
    sig = inspect.signature(gpfl::CmdGECompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdeq_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdEq)


def test_gpfl::cmdeq_constructor_exists():
    assert callable(gpfl::CmdEq.__init__)


def test_gpfl::cmdeq_constructor_args():
    sig = inspect.signature(gpfl::CmdEq.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::nopcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::NopCmd)


def test_gpfl::nopcmd_constructor_exists():
    assert callable(gpfl::NopCmd.__init__)


def test_gpfl::nopcmd_constructor_args():
    sig = inspect.signature(gpfl::NopCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdand_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdAnd)


def test_gpfl::cmdand_constructor_exists():
    assert callable(gpfl::CmdAnd.__init__)


def test_gpfl::cmdand_constructor_args():
    sig = inspect.signature(gpfl::CmdAnd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdneq_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdNEq)


def test_gpfl::cmdneq_constructor_exists():
    assert callable(gpfl::CmdNEq.__init__)


def test_gpfl::cmdneq_constructor_args():
    sig = inspect.signature(gpfl::CmdNEq.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::gboolfalse_is_not_abstract():
    assert not inspect.isabstract(gpfl::GBoolFalse)


def test_gpfl::gboolfalse_constructor_exists():
    assert callable(gpfl::GBoolFalse.__init__)


def test_gpfl::gboolfalse_constructor_args():
    sig = inspect.signature(gpfl::GBoolFalse.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::intlitcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::IntLitCmd)


def test_gpfl::intlitcmd_constructor_exists():
    assert callable(gpfl::IntLitCmd.__init__)


def test_gpfl::intlitcmd_constructor_args():
    sig = inspect.signature(gpfl::IntLitCmd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl::intlitcmd_has_value():
    assert hasattr(gpfl::IntLitCmd, "value")
    descriptor = None
    for klass in gpfl::IntLitCmd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::portlit_is_not_abstract():
    assert not inspect.isabstract(gpfl::PortLit)


def test_gpfl::portlit_constructor_exists():
    assert callable(gpfl::PortLit.__init__)


def test_gpfl::portlit_constructor_args():
    sig = inspect.signature(gpfl::PortLit.__init__)
    params = list(sig.parameters.keys())
    assert "inSide" in params, "Missing parameter 'inSide'"

def test_gpfl::portlit_has_inSide():
    assert hasattr(gpfl::PortLit, "inSide")
    descriptor = None
    for klass in gpfl::PortLit.__mro__:
        if "inSide" in klass.__dict__:
            descriptor = klass.__dict__["inSide"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::dropcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::DropCmd)


def test_gpfl::dropcmd_constructor_exists():
    assert callable(gpfl::DropCmd.__init__)


def test_gpfl::dropcmd_constructor_args():
    sig = inspect.signature(gpfl::DropCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::acceptcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::AcceptCmd)


def test_gpfl::acceptcmd_constructor_exists():
    assert callable(gpfl::AcceptCmd.__init__)


def test_gpfl::acceptcmd_constructor_args():
    sig = inspect.signature(gpfl::AcceptCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::interruptstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl::InterruptStmt)


def test_gpfl::interruptstmt_constructor_exists():
    assert callable(gpfl::InterruptStmt.__init__)


def test_gpfl::interruptstmt_constructor_args():
    sig = inspect.signature(gpfl::InterruptStmt.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_gpfl::interruptstmt_has_timeout():
    assert hasattr(gpfl::InterruptStmt, "timeout")
    descriptor = None
    for klass in gpfl::InterruptStmt.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::gbooltrue_is_not_abstract():
    assert not inspect.isabstract(gpfl::GBoolTrue)


def test_gpfl::gbooltrue_constructor_exists():
    assert callable(gpfl::GBoolTrue.__init__)


def test_gpfl::gbooltrue_constructor_args():
    sig = inspect.signature(gpfl::GBoolTrue.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdlcompare_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdLCompare)


def test_gpfl::cmdlcompare_constructor_exists():
    assert callable(gpfl::CmdLCompare.__init__)


def test_gpfl::cmdlcompare_constructor_args():
    sig = inspect.signature(gpfl::CmdLCompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::stpcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::StpCmd)


def test_gpfl::stpcmd_constructor_exists():
    assert callable(gpfl::StpCmd.__init__)


def test_gpfl::stpcmd_constructor_args():
    sig = inspect.signature(gpfl::StpCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::sendcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl::SendCmd)


def test_gpfl::sendcmd_constructor_exists():
    assert callable(gpfl::SendCmd.__init__)


def test_gpfl::sendcmd_constructor_args():
    sig = inspect.signature(gpfl::SendCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdlecompare_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdLECompare)


def test_gpfl::cmdlecompare_constructor_exists():
    assert callable(gpfl::CmdLECompare.__init__)


def test_gpfl::cmdlecompare_constructor_args():
    sig = inspect.signature(gpfl::CmdLECompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::cmdsub_is_not_abstract():
    assert not inspect.isabstract(gpfl::CmdSub)


def test_gpfl::cmdsub_constructor_exists():
    assert callable(gpfl::CmdSub.__init__)


def test_gpfl::cmdsub_constructor_args():
    sig = inspect.signature(gpfl::CmdSub.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::condstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl::CondStmt)


def test_gpfl::condstmt_constructor_exists():
    assert callable(gpfl::CondStmt.__init__)


def test_gpfl::condstmt_constructor_args():
    sig = inspect.signature(gpfl::CondStmt.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::transition_is_not_abstract():
    assert not inspect.isabstract(gpfl::Transition)


def test_gpfl::transition_constructor_exists():
    assert callable(gpfl::Transition.__init__)


def test_gpfl::transition_constructor_args():
    sig = inspect.signature(gpfl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gpfl::transition_has_event():
    assert hasattr(gpfl::Transition, "event")
    descriptor = None
    for klass in gpfl::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::field_is_not_abstract():
    assert not inspect.isabstract(gpfl::Field)


def test_gpfl::field_constructor_exists():
    assert callable(gpfl::Field.__init__)


def test_gpfl::field_constructor_args():
    sig = inspect.signature(gpfl::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::field_has_name():
    assert hasattr(gpfl::Field, "name")
    descriptor = None
    for klass in gpfl::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::gexpression_is_not_abstract():
    assert not inspect.isabstract(gpfl::GExpression)


def test_gpfl::gexpression_constructor_exists():
    assert callable(gpfl::GExpression.__init__)


def test_gpfl::gexpression_constructor_args():
    sig = inspect.signature(gpfl::GExpression.__init__)
    params = list(sig.parameters.keys())



def test_gpfl::automatadef_is_not_abstract():
    assert not inspect.isabstract(gpfl::AutomataDef)


def test_gpfl::automatadef_constructor_exists():
    assert callable(gpfl::AutomataDef.__init__)


def test_gpfl::automatadef_constructor_args():
    sig = inspect.signature(gpfl::AutomataDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::automatadef_has_name():
    assert hasattr(gpfl::AutomataDef, "name")
    descriptor = None
    for klass in gpfl::AutomataDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl::program_is_not_abstract():
    assert not inspect.isabstract(gpfl::Program)


def test_gpfl::program_constructor_exists():
    assert callable(gpfl::Program.__init__)


def test_gpfl::program_constructor_args():
    sig = inspect.signature(gpfl::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl::program_has_name():
    assert hasattr(gpfl::Program, "name")
    descriptor = None
    for klass in gpfl::Program.__mro__:
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
gpfl::State_strategy = st.builds(
    gpfl::State,
    name=
        safe_text
)
GExpression_strategy = st.builds(
    GExpression,
)
gpfl::AutomatonCmd_strategy = st.builds(
    gpfl::AutomatonCmd,
    name=
        safe_text
)
gpfl::OutPort_strategy = st.builds(
    gpfl::OutPort,
)
gpfl::CmdAdd_strategy = st.builds(
    gpfl::CmdAdd,
)
gpfl::SetCmd_strategy = st.builds(
    gpfl::SetCmd,
    name=
        safe_text
)
gpfl::InPort_strategy = st.builds(
    gpfl::InPort,
)
gpfl::IterStmt_strategy = st.builds(
    gpfl::IterStmt,
)
gpfl::StringLit_strategy = st.builds(
    gpfl::StringLit,
    value=
        safe_text
)
gpfl::Variable_strategy = st.builds(
    gpfl::Variable,
    value=
        safe_text
)
gpfl::CmdGCompare_strategy = st.builds(
    gpfl::CmdGCompare,
)
gpfl::AlarmCmd_strategy = st.builds(
    gpfl::AlarmCmd,
)
gpfl::CmdGECompare_strategy = st.builds(
    gpfl::CmdGECompare,
)
gpfl::CmdEq_strategy = st.builds(
    gpfl::CmdEq,
)
gpfl::NopCmd_strategy = st.builds(
    gpfl::NopCmd,
)
gpfl::CmdAnd_strategy = st.builds(
    gpfl::CmdAnd,
)
gpfl::CmdNEq_strategy = st.builds(
    gpfl::CmdNEq,
)
gpfl::GBoolFalse_strategy = st.builds(
    gpfl::GBoolFalse,
)
gpfl::IntLitCmd_strategy = st.builds(
    gpfl::IntLitCmd,
    value=
        st.integers()
)
gpfl::PortLit_strategy = st.builds(
    gpfl::PortLit,
    inSide=
        st.booleans()
)
gpfl::DropCmd_strategy = st.builds(
    gpfl::DropCmd,
)
gpfl::AcceptCmd_strategy = st.builds(
    gpfl::AcceptCmd,
)
gpfl::InterruptStmt_strategy = st.builds(
    gpfl::InterruptStmt,
    timeout=
        st.integers()
)
gpfl::GBoolTrue_strategy = st.builds(
    gpfl::GBoolTrue,
)
gpfl::CmdLCompare_strategy = st.builds(
    gpfl::CmdLCompare,
)
gpfl::StpCmd_strategy = st.builds(
    gpfl::StpCmd,
)
gpfl::SendCmd_strategy = st.builds(
    gpfl::SendCmd,
)
gpfl::CmdLECompare_strategy = st.builds(
    gpfl::CmdLECompare,
)
gpfl::CmdSub_strategy = st.builds(
    gpfl::CmdSub,
)
gpfl::CondStmt_strategy = st.builds(
    gpfl::CondStmt,
)
gpfl::Transition_strategy = st.builds(
    gpfl::Transition,
    event=
        safe_text
)
gpfl::Field_strategy = st.builds(
    gpfl::Field,
    name=
        safe_text
)
gpfl::GExpression_strategy = st.builds(
    gpfl::GExpression,
)
gpfl::AutomataDef_strategy = st.builds(
    gpfl::AutomataDef,
    name=
        safe_text
)
gpfl::Program_strategy = st.builds(
    gpfl::Program,
    name=
        safe_text
)

@given(instance=gpfl::State_strategy)
@settings(max_examples=50)
def test_gpfl::state_instantiation(instance):
    assert isinstance(instance, gpfl::State)

@given(instance=gpfl::State_strategy)
def test_gpfl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::State_strategy)
def test_gpfl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GExpression_strategy)
@settings(max_examples=50)
def test_gexpression_instantiation(instance):
    assert isinstance(instance, GExpression)

@given(instance=gpfl::AutomatonCmd_strategy)
@settings(max_examples=50)
def test_gpfl::automatoncmd_instantiation(instance):
    assert isinstance(instance, gpfl::AutomatonCmd)

@given(instance=gpfl::AutomatonCmd_strategy)
def test_gpfl::automatoncmd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::AutomatonCmd_strategy)
def test_gpfl::automatoncmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl::OutPort_strategy)
@settings(max_examples=50)
def test_gpfl::outport_instantiation(instance):
    assert isinstance(instance, gpfl::OutPort)

@given(instance=gpfl::CmdAdd_strategy)
@settings(max_examples=50)
def test_gpfl::cmdadd_instantiation(instance):
    assert isinstance(instance, gpfl::CmdAdd)

@given(instance=gpfl::SetCmd_strategy)
@settings(max_examples=50)
def test_gpfl::setcmd_instantiation(instance):
    assert isinstance(instance, gpfl::SetCmd)

@given(instance=gpfl::SetCmd_strategy)
def test_gpfl::setcmd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::SetCmd_strategy)
def test_gpfl::setcmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl::InPort_strategy)
@settings(max_examples=50)
def test_gpfl::inport_instantiation(instance):
    assert isinstance(instance, gpfl::InPort)

@given(instance=gpfl::IterStmt_strategy)
@settings(max_examples=50)
def test_gpfl::iterstmt_instantiation(instance):
    assert isinstance(instance, gpfl::IterStmt)

@given(instance=gpfl::StringLit_strategy)
@settings(max_examples=50)
def test_gpfl::stringlit_instantiation(instance):
    assert isinstance(instance, gpfl::StringLit)

@given(instance=gpfl::StringLit_strategy)
def test_gpfl::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gpfl::StringLit_strategy)
def test_gpfl::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl::Variable_strategy)
@settings(max_examples=50)
def test_gpfl::variable_instantiation(instance):
    assert isinstance(instance, gpfl::Variable)

@given(instance=gpfl::Variable_strategy)
def test_gpfl::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gpfl::Variable_strategy)
def test_gpfl::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl::CmdGCompare_strategy)
@settings(max_examples=50)
def test_gpfl::cmdgcompare_instantiation(instance):
    assert isinstance(instance, gpfl::CmdGCompare)

@given(instance=gpfl::AlarmCmd_strategy)
@settings(max_examples=50)
def test_gpfl::alarmcmd_instantiation(instance):
    assert isinstance(instance, gpfl::AlarmCmd)

@given(instance=gpfl::CmdGECompare_strategy)
@settings(max_examples=50)
def test_gpfl::cmdgecompare_instantiation(instance):
    assert isinstance(instance, gpfl::CmdGECompare)

@given(instance=gpfl::CmdEq_strategy)
@settings(max_examples=50)
def test_gpfl::cmdeq_instantiation(instance):
    assert isinstance(instance, gpfl::CmdEq)

@given(instance=gpfl::NopCmd_strategy)
@settings(max_examples=50)
def test_gpfl::nopcmd_instantiation(instance):
    assert isinstance(instance, gpfl::NopCmd)

@given(instance=gpfl::CmdAnd_strategy)
@settings(max_examples=50)
def test_gpfl::cmdand_instantiation(instance):
    assert isinstance(instance, gpfl::CmdAnd)

@given(instance=gpfl::CmdNEq_strategy)
@settings(max_examples=50)
def test_gpfl::cmdneq_instantiation(instance):
    assert isinstance(instance, gpfl::CmdNEq)

@given(instance=gpfl::GBoolFalse_strategy)
@settings(max_examples=50)
def test_gpfl::gboolfalse_instantiation(instance):
    assert isinstance(instance, gpfl::GBoolFalse)

@given(instance=gpfl::IntLitCmd_strategy)
@settings(max_examples=50)
def test_gpfl::intlitcmd_instantiation(instance):
    assert isinstance(instance, gpfl::IntLitCmd)

@given(instance=gpfl::IntLitCmd_strategy)
def test_gpfl::intlitcmd_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=gpfl::IntLitCmd_strategy)
def test_gpfl::intlitcmd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl::PortLit_strategy)
@settings(max_examples=50)
def test_gpfl::portlit_instantiation(instance):
    assert isinstance(instance, gpfl::PortLit)

@given(instance=gpfl::PortLit_strategy)
def test_gpfl::portlit_inSide_type(instance):
    assert isinstance(instance.inSide, bool)


@given(instance=gpfl::PortLit_strategy)
def test_gpfl::portlit_inSide_setter(instance):
    original = instance.inSide
    instance.inSide = original
    assert instance.inSide == original

@given(instance=gpfl::DropCmd_strategy)
@settings(max_examples=50)
def test_gpfl::dropcmd_instantiation(instance):
    assert isinstance(instance, gpfl::DropCmd)

@given(instance=gpfl::AcceptCmd_strategy)
@settings(max_examples=50)
def test_gpfl::acceptcmd_instantiation(instance):
    assert isinstance(instance, gpfl::AcceptCmd)

@given(instance=gpfl::InterruptStmt_strategy)
@settings(max_examples=50)
def test_gpfl::interruptstmt_instantiation(instance):
    assert isinstance(instance, gpfl::InterruptStmt)

@given(instance=gpfl::InterruptStmt_strategy)
def test_gpfl::interruptstmt_timeout_type(instance):
    assert isinstance(instance.timeout, int)


@given(instance=gpfl::InterruptStmt_strategy)
def test_gpfl::interruptstmt_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=gpfl::GBoolTrue_strategy)
@settings(max_examples=50)
def test_gpfl::gbooltrue_instantiation(instance):
    assert isinstance(instance, gpfl::GBoolTrue)

@given(instance=gpfl::CmdLCompare_strategy)
@settings(max_examples=50)
def test_gpfl::cmdlcompare_instantiation(instance):
    assert isinstance(instance, gpfl::CmdLCompare)

@given(instance=gpfl::StpCmd_strategy)
@settings(max_examples=50)
def test_gpfl::stpcmd_instantiation(instance):
    assert isinstance(instance, gpfl::StpCmd)

@given(instance=gpfl::SendCmd_strategy)
@settings(max_examples=50)
def test_gpfl::sendcmd_instantiation(instance):
    assert isinstance(instance, gpfl::SendCmd)

@given(instance=gpfl::CmdLECompare_strategy)
@settings(max_examples=50)
def test_gpfl::cmdlecompare_instantiation(instance):
    assert isinstance(instance, gpfl::CmdLECompare)

@given(instance=gpfl::CmdSub_strategy)
@settings(max_examples=50)
def test_gpfl::cmdsub_instantiation(instance):
    assert isinstance(instance, gpfl::CmdSub)

@given(instance=gpfl::CondStmt_strategy)
@settings(max_examples=50)
def test_gpfl::condstmt_instantiation(instance):
    assert isinstance(instance, gpfl::CondStmt)

@given(instance=gpfl::Transition_strategy)
@settings(max_examples=50)
def test_gpfl::transition_instantiation(instance):
    assert isinstance(instance, gpfl::Transition)

@given(instance=gpfl::Transition_strategy)
def test_gpfl::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=gpfl::Transition_strategy)
def test_gpfl::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=gpfl::Field_strategy)
@settings(max_examples=50)
def test_gpfl::field_instantiation(instance):
    assert isinstance(instance, gpfl::Field)

@given(instance=gpfl::Field_strategy)
def test_gpfl::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::Field_strategy)
def test_gpfl::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl::GExpression_strategy)
@settings(max_examples=50)
def test_gpfl::gexpression_instantiation(instance):
    assert isinstance(instance, gpfl::GExpression)

@given(instance=gpfl::AutomataDef_strategy)
@settings(max_examples=50)
def test_gpfl::automatadef_instantiation(instance):
    assert isinstance(instance, gpfl::AutomataDef)

@given(instance=gpfl::AutomataDef_strategy)
def test_gpfl::automatadef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::AutomataDef_strategy)
def test_gpfl::automatadef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl::Program_strategy)
@settings(max_examples=50)
def test_gpfl::program_instantiation(instance):
    assert isinstance(instance, gpfl::Program)

@given(instance=gpfl::Program_strategy)
def test_gpfl::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gpfl::Program_strategy)
def test_gpfl::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

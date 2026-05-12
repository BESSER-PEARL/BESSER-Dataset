import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gpfl_State,
    GExpression,
    gpfl_GBoolTrue,
    gpfl_CmdLECompare,
    gpfl_CmdAnd,
    gpfl_CmdAdd,
    gpfl_InPort,
    gpfl_StringLit,
    gpfl_StpCmd,
    gpfl_OutPort,
    gpfl_IntLitCmd,
    gpfl_CmdEq,
    gpfl_CmdSub,
    gpfl_SendCmd,
    gpfl_AcceptCmd,
    gpfl_AutomatonCmd,
    gpfl_CmdGECompare,
    gpfl_SetCmd,
    gpfl_AlarmCmd,
    gpfl_CmdGCompare,
    gpfl_Variable,
    gpfl_CmdLCompare,
    gpfl_InterruptStmt,
    gpfl_GBoolFalse,
    gpfl_PortLit,
    gpfl_DropCmd,
    gpfl_IterStmt,
    gpfl_NopCmd,
    gpfl_CmdNEq,
    gpfl_CondStmt,
    gpfl_Transition,
    gpfl_Field,
    gpfl_GExpression,
    gpfl_AutomataDef,
    gpfl_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gpfl_state_is_not_abstract():
    assert not inspect.isabstract(gpfl_State)


def test_gpfl_state_constructor_exists():
    assert callable(gpfl_State.__init__)


def test_gpfl_state_constructor_args():
    sig = inspect.signature(gpfl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_state_has_name():
    assert hasattr(gpfl_State, "name")
    descriptor = None
    for klass in gpfl_State.__mro__:
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



def test_gpfl_gbooltrue_is_not_abstract():
    assert not inspect.isabstract(gpfl_GBoolTrue)


def test_gpfl_gbooltrue_constructor_exists():
    assert callable(gpfl_GBoolTrue.__init__)


def test_gpfl_gbooltrue_constructor_args():
    sig = inspect.signature(gpfl_GBoolTrue.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdlecompare_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdLECompare)


def test_gpfl_cmdlecompare_constructor_exists():
    assert callable(gpfl_CmdLECompare.__init__)


def test_gpfl_cmdlecompare_constructor_args():
    sig = inspect.signature(gpfl_CmdLECompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdand_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdAnd)


def test_gpfl_cmdand_constructor_exists():
    assert callable(gpfl_CmdAnd.__init__)


def test_gpfl_cmdand_constructor_args():
    sig = inspect.signature(gpfl_CmdAnd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdadd_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdAdd)


def test_gpfl_cmdadd_constructor_exists():
    assert callable(gpfl_CmdAdd.__init__)


def test_gpfl_cmdadd_constructor_args():
    sig = inspect.signature(gpfl_CmdAdd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_inport_is_not_abstract():
    assert not inspect.isabstract(gpfl_InPort)


def test_gpfl_inport_constructor_exists():
    assert callable(gpfl_InPort.__init__)


def test_gpfl_inport_constructor_args():
    sig = inspect.signature(gpfl_InPort.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_stringlit_is_not_abstract():
    assert not inspect.isabstract(gpfl_StringLit)


def test_gpfl_stringlit_constructor_exists():
    assert callable(gpfl_StringLit.__init__)


def test_gpfl_stringlit_constructor_args():
    sig = inspect.signature(gpfl_StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl_stringlit_has_value():
    assert hasattr(gpfl_StringLit, "value")
    descriptor = None
    for klass in gpfl_StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_stpcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_StpCmd)


def test_gpfl_stpcmd_constructor_exists():
    assert callable(gpfl_StpCmd.__init__)


def test_gpfl_stpcmd_constructor_args():
    sig = inspect.signature(gpfl_StpCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_outport_is_not_abstract():
    assert not inspect.isabstract(gpfl_OutPort)


def test_gpfl_outport_constructor_exists():
    assert callable(gpfl_OutPort.__init__)


def test_gpfl_outport_constructor_args():
    sig = inspect.signature(gpfl_OutPort.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_intlitcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_IntLitCmd)


def test_gpfl_intlitcmd_constructor_exists():
    assert callable(gpfl_IntLitCmd.__init__)


def test_gpfl_intlitcmd_constructor_args():
    sig = inspect.signature(gpfl_IntLitCmd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl_intlitcmd_has_value():
    assert hasattr(gpfl_IntLitCmd, "value")
    descriptor = None
    for klass in gpfl_IntLitCmd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_cmdeq_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdEq)


def test_gpfl_cmdeq_constructor_exists():
    assert callable(gpfl_CmdEq.__init__)


def test_gpfl_cmdeq_constructor_args():
    sig = inspect.signature(gpfl_CmdEq.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdsub_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdSub)


def test_gpfl_cmdsub_constructor_exists():
    assert callable(gpfl_CmdSub.__init__)


def test_gpfl_cmdsub_constructor_args():
    sig = inspect.signature(gpfl_CmdSub.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_sendcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_SendCmd)


def test_gpfl_sendcmd_constructor_exists():
    assert callable(gpfl_SendCmd.__init__)


def test_gpfl_sendcmd_constructor_args():
    sig = inspect.signature(gpfl_SendCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_acceptcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_AcceptCmd)


def test_gpfl_acceptcmd_constructor_exists():
    assert callable(gpfl_AcceptCmd.__init__)


def test_gpfl_acceptcmd_constructor_args():
    sig = inspect.signature(gpfl_AcceptCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_automatoncmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_AutomatonCmd)


def test_gpfl_automatoncmd_constructor_exists():
    assert callable(gpfl_AutomatonCmd.__init__)


def test_gpfl_automatoncmd_constructor_args():
    sig = inspect.signature(gpfl_AutomatonCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_automatoncmd_has_name():
    assert hasattr(gpfl_AutomatonCmd, "name")
    descriptor = None
    for klass in gpfl_AutomatonCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_cmdgecompare_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdGECompare)


def test_gpfl_cmdgecompare_constructor_exists():
    assert callable(gpfl_CmdGECompare.__init__)


def test_gpfl_cmdgecompare_constructor_args():
    sig = inspect.signature(gpfl_CmdGECompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_setcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_SetCmd)


def test_gpfl_setcmd_constructor_exists():
    assert callable(gpfl_SetCmd.__init__)


def test_gpfl_setcmd_constructor_args():
    sig = inspect.signature(gpfl_SetCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_setcmd_has_name():
    assert hasattr(gpfl_SetCmd, "name")
    descriptor = None
    for klass in gpfl_SetCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_alarmcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_AlarmCmd)


def test_gpfl_alarmcmd_constructor_exists():
    assert callable(gpfl_AlarmCmd.__init__)


def test_gpfl_alarmcmd_constructor_args():
    sig = inspect.signature(gpfl_AlarmCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdgcompare_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdGCompare)


def test_gpfl_cmdgcompare_constructor_exists():
    assert callable(gpfl_CmdGCompare.__init__)


def test_gpfl_cmdgcompare_constructor_args():
    sig = inspect.signature(gpfl_CmdGCompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_variable_is_not_abstract():
    assert not inspect.isabstract(gpfl_Variable)


def test_gpfl_variable_constructor_exists():
    assert callable(gpfl_Variable.__init__)


def test_gpfl_variable_constructor_args():
    sig = inspect.signature(gpfl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gpfl_variable_has_value():
    assert hasattr(gpfl_Variable, "value")
    descriptor = None
    for klass in gpfl_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_cmdlcompare_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdLCompare)


def test_gpfl_cmdlcompare_constructor_exists():
    assert callable(gpfl_CmdLCompare.__init__)


def test_gpfl_cmdlcompare_constructor_args():
    sig = inspect.signature(gpfl_CmdLCompare.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_interruptstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl_InterruptStmt)


def test_gpfl_interruptstmt_constructor_exists():
    assert callable(gpfl_InterruptStmt.__init__)


def test_gpfl_interruptstmt_constructor_args():
    sig = inspect.signature(gpfl_InterruptStmt.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_gpfl_interruptstmt_has_timeout():
    assert hasattr(gpfl_InterruptStmt, "timeout")
    descriptor = None
    for klass in gpfl_InterruptStmt.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_gboolfalse_is_not_abstract():
    assert not inspect.isabstract(gpfl_GBoolFalse)


def test_gpfl_gboolfalse_constructor_exists():
    assert callable(gpfl_GBoolFalse.__init__)


def test_gpfl_gboolfalse_constructor_args():
    sig = inspect.signature(gpfl_GBoolFalse.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_portlit_is_not_abstract():
    assert not inspect.isabstract(gpfl_PortLit)


def test_gpfl_portlit_constructor_exists():
    assert callable(gpfl_PortLit.__init__)


def test_gpfl_portlit_constructor_args():
    sig = inspect.signature(gpfl_PortLit.__init__)
    params = list(sig.parameters.keys())
    assert "inSide" in params, "Missing parameter 'inSide'"

def test_gpfl_portlit_has_inSide():
    assert hasattr(gpfl_PortLit, "inSide")
    descriptor = None
    for klass in gpfl_PortLit.__mro__:
        if "inSide" in klass.__dict__:
            descriptor = klass.__dict__["inSide"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_dropcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_DropCmd)


def test_gpfl_dropcmd_constructor_exists():
    assert callable(gpfl_DropCmd.__init__)


def test_gpfl_dropcmd_constructor_args():
    sig = inspect.signature(gpfl_DropCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_iterstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl_IterStmt)


def test_gpfl_iterstmt_constructor_exists():
    assert callable(gpfl_IterStmt.__init__)


def test_gpfl_iterstmt_constructor_args():
    sig = inspect.signature(gpfl_IterStmt.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_nopcmd_is_not_abstract():
    assert not inspect.isabstract(gpfl_NopCmd)


def test_gpfl_nopcmd_constructor_exists():
    assert callable(gpfl_NopCmd.__init__)


def test_gpfl_nopcmd_constructor_args():
    sig = inspect.signature(gpfl_NopCmd.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_cmdneq_is_not_abstract():
    assert not inspect.isabstract(gpfl_CmdNEq)


def test_gpfl_cmdneq_constructor_exists():
    assert callable(gpfl_CmdNEq.__init__)


def test_gpfl_cmdneq_constructor_args():
    sig = inspect.signature(gpfl_CmdNEq.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_condstmt_is_not_abstract():
    assert not inspect.isabstract(gpfl_CondStmt)


def test_gpfl_condstmt_constructor_exists():
    assert callable(gpfl_CondStmt.__init__)


def test_gpfl_condstmt_constructor_args():
    sig = inspect.signature(gpfl_CondStmt.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_transition_is_not_abstract():
    assert not inspect.isabstract(gpfl_Transition)


def test_gpfl_transition_constructor_exists():
    assert callable(gpfl_Transition.__init__)


def test_gpfl_transition_constructor_args():
    sig = inspect.signature(gpfl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_gpfl_transition_has_event():
    assert hasattr(gpfl_Transition, "event")
    descriptor = None
    for klass in gpfl_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_field_is_not_abstract():
    assert not inspect.isabstract(gpfl_Field)


def test_gpfl_field_constructor_exists():
    assert callable(gpfl_Field.__init__)


def test_gpfl_field_constructor_args():
    sig = inspect.signature(gpfl_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_field_has_name():
    assert hasattr(gpfl_Field, "name")
    descriptor = None
    for klass in gpfl_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_gexpression_is_not_abstract():
    assert not inspect.isabstract(gpfl_GExpression)


def test_gpfl_gexpression_constructor_exists():
    assert callable(gpfl_GExpression.__init__)


def test_gpfl_gexpression_constructor_args():
    sig = inspect.signature(gpfl_GExpression.__init__)
    params = list(sig.parameters.keys())



def test_gpfl_automatadef_is_not_abstract():
    assert not inspect.isabstract(gpfl_AutomataDef)


def test_gpfl_automatadef_constructor_exists():
    assert callable(gpfl_AutomataDef.__init__)


def test_gpfl_automatadef_constructor_args():
    sig = inspect.signature(gpfl_AutomataDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_automatadef_has_name():
    assert hasattr(gpfl_AutomataDef, "name")
    descriptor = None
    for klass in gpfl_AutomataDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gpfl_program_is_not_abstract():
    assert not inspect.isabstract(gpfl_Program)


def test_gpfl_program_constructor_exists():
    assert callable(gpfl_Program.__init__)


def test_gpfl_program_constructor_args():
    sig = inspect.signature(gpfl_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gpfl_program_has_name():
    assert hasattr(gpfl_Program, "name")
    descriptor = None
    for klass in gpfl_Program.__mro__:
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
gpfl_State_strategy = st.builds(
    gpfl_State,
    name=
        safe_text
)
GExpression_strategy = st.builds(
    GExpression,
)
gpfl_GBoolTrue_strategy = st.builds(
    gpfl_GBoolTrue,
)
gpfl_CmdLECompare_strategy = st.builds(
    gpfl_CmdLECompare,
)
gpfl_CmdAnd_strategy = st.builds(
    gpfl_CmdAnd,
)
gpfl_CmdAdd_strategy = st.builds(
    gpfl_CmdAdd,
)
gpfl_InPort_strategy = st.builds(
    gpfl_InPort,
)
gpfl_StringLit_strategy = st.builds(
    gpfl_StringLit,
    value=
        safe_text
)
gpfl_StpCmd_strategy = st.builds(
    gpfl_StpCmd,
)
gpfl_OutPort_strategy = st.builds(
    gpfl_OutPort,
)
gpfl_IntLitCmd_strategy = st.builds(
    gpfl_IntLitCmd,
    value=
        st.integers()
)
gpfl_CmdEq_strategy = st.builds(
    gpfl_CmdEq,
)
gpfl_CmdSub_strategy = st.builds(
    gpfl_CmdSub,
)
gpfl_SendCmd_strategy = st.builds(
    gpfl_SendCmd,
)
gpfl_AcceptCmd_strategy = st.builds(
    gpfl_AcceptCmd,
)
gpfl_AutomatonCmd_strategy = st.builds(
    gpfl_AutomatonCmd,
    name=
        safe_text
)
gpfl_CmdGECompare_strategy = st.builds(
    gpfl_CmdGECompare,
)
gpfl_SetCmd_strategy = st.builds(
    gpfl_SetCmd,
    name=
        safe_text
)
gpfl_AlarmCmd_strategy = st.builds(
    gpfl_AlarmCmd,
)
gpfl_CmdGCompare_strategy = st.builds(
    gpfl_CmdGCompare,
)
gpfl_Variable_strategy = st.builds(
    gpfl_Variable,
    value=
        safe_text
)
gpfl_CmdLCompare_strategy = st.builds(
    gpfl_CmdLCompare,
)
gpfl_InterruptStmt_strategy = st.builds(
    gpfl_InterruptStmt,
    timeout=
        st.integers()
)
gpfl_GBoolFalse_strategy = st.builds(
    gpfl_GBoolFalse,
)
gpfl_PortLit_strategy = st.builds(
    gpfl_PortLit,
    inSide=
        st.booleans()
)
gpfl_DropCmd_strategy = st.builds(
    gpfl_DropCmd,
)
gpfl_IterStmt_strategy = st.builds(
    gpfl_IterStmt,
)
gpfl_NopCmd_strategy = st.builds(
    gpfl_NopCmd,
)
gpfl_CmdNEq_strategy = st.builds(
    gpfl_CmdNEq,
)
gpfl_CondStmt_strategy = st.builds(
    gpfl_CondStmt,
)
gpfl_Transition_strategy = st.builds(
    gpfl_Transition,
    event=
        safe_text
)
gpfl_Field_strategy = st.builds(
    gpfl_Field,
    name=
        safe_text
)
gpfl_GExpression_strategy = st.builds(
    gpfl_GExpression,
)
gpfl_AutomataDef_strategy = st.builds(
    gpfl_AutomataDef,
    name=
        safe_text
)
gpfl_Program_strategy = st.builds(
    gpfl_Program,
    name=
        safe_text
)

@given(instance=gpfl_State_strategy)
@settings(max_examples=50)
def test_gpfl_state_instantiation(instance):
    assert isinstance(instance, gpfl_State)



@given(instance=gpfl_State_strategy)
def test_gpfl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GExpression_strategy)
@settings(max_examples=50)
def test_gexpression_instantiation(instance):
    assert isinstance(instance, GExpression)

@given(instance=gpfl_GBoolTrue_strategy)
@settings(max_examples=50)
def test_gpfl_gbooltrue_instantiation(instance):
    assert isinstance(instance, gpfl_GBoolTrue)

@given(instance=gpfl_CmdLECompare_strategy)
@settings(max_examples=50)
def test_gpfl_cmdlecompare_instantiation(instance):
    assert isinstance(instance, gpfl_CmdLECompare)

@given(instance=gpfl_CmdAnd_strategy)
@settings(max_examples=50)
def test_gpfl_cmdand_instantiation(instance):
    assert isinstance(instance, gpfl_CmdAnd)

@given(instance=gpfl_CmdAdd_strategy)
@settings(max_examples=50)
def test_gpfl_cmdadd_instantiation(instance):
    assert isinstance(instance, gpfl_CmdAdd)

@given(instance=gpfl_InPort_strategy)
@settings(max_examples=50)
def test_gpfl_inport_instantiation(instance):
    assert isinstance(instance, gpfl_InPort)

@given(instance=gpfl_StringLit_strategy)
@settings(max_examples=50)
def test_gpfl_stringlit_instantiation(instance):
    assert isinstance(instance, gpfl_StringLit)



@given(instance=gpfl_StringLit_strategy)
def test_gpfl_stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl_StpCmd_strategy)
@settings(max_examples=50)
def test_gpfl_stpcmd_instantiation(instance):
    assert isinstance(instance, gpfl_StpCmd)

@given(instance=gpfl_OutPort_strategy)
@settings(max_examples=50)
def test_gpfl_outport_instantiation(instance):
    assert isinstance(instance, gpfl_OutPort)

@given(instance=gpfl_IntLitCmd_strategy)
@settings(max_examples=50)
def test_gpfl_intlitcmd_instantiation(instance):
    assert isinstance(instance, gpfl_IntLitCmd)



@given(instance=gpfl_IntLitCmd_strategy)
def test_gpfl_intlitcmd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl_CmdEq_strategy)
@settings(max_examples=50)
def test_gpfl_cmdeq_instantiation(instance):
    assert isinstance(instance, gpfl_CmdEq)

@given(instance=gpfl_CmdSub_strategy)
@settings(max_examples=50)
def test_gpfl_cmdsub_instantiation(instance):
    assert isinstance(instance, gpfl_CmdSub)

@given(instance=gpfl_SendCmd_strategy)
@settings(max_examples=50)
def test_gpfl_sendcmd_instantiation(instance):
    assert isinstance(instance, gpfl_SendCmd)

@given(instance=gpfl_AcceptCmd_strategy)
@settings(max_examples=50)
def test_gpfl_acceptcmd_instantiation(instance):
    assert isinstance(instance, gpfl_AcceptCmd)

@given(instance=gpfl_AutomatonCmd_strategy)
@settings(max_examples=50)
def test_gpfl_automatoncmd_instantiation(instance):
    assert isinstance(instance, gpfl_AutomatonCmd)



@given(instance=gpfl_AutomatonCmd_strategy)
def test_gpfl_automatoncmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl_CmdGECompare_strategy)
@settings(max_examples=50)
def test_gpfl_cmdgecompare_instantiation(instance):
    assert isinstance(instance, gpfl_CmdGECompare)

@given(instance=gpfl_SetCmd_strategy)
@settings(max_examples=50)
def test_gpfl_setcmd_instantiation(instance):
    assert isinstance(instance, gpfl_SetCmd)



@given(instance=gpfl_SetCmd_strategy)
def test_gpfl_setcmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl_AlarmCmd_strategy)
@settings(max_examples=50)
def test_gpfl_alarmcmd_instantiation(instance):
    assert isinstance(instance, gpfl_AlarmCmd)

@given(instance=gpfl_CmdGCompare_strategy)
@settings(max_examples=50)
def test_gpfl_cmdgcompare_instantiation(instance):
    assert isinstance(instance, gpfl_CmdGCompare)

@given(instance=gpfl_Variable_strategy)
@settings(max_examples=50)
def test_gpfl_variable_instantiation(instance):
    assert isinstance(instance, gpfl_Variable)



@given(instance=gpfl_Variable_strategy)
def test_gpfl_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gpfl_CmdLCompare_strategy)
@settings(max_examples=50)
def test_gpfl_cmdlcompare_instantiation(instance):
    assert isinstance(instance, gpfl_CmdLCompare)

@given(instance=gpfl_InterruptStmt_strategy)
@settings(max_examples=50)
def test_gpfl_interruptstmt_instantiation(instance):
    assert isinstance(instance, gpfl_InterruptStmt)



@given(instance=gpfl_InterruptStmt_strategy)
def test_gpfl_interruptstmt_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=gpfl_GBoolFalse_strategy)
@settings(max_examples=50)
def test_gpfl_gboolfalse_instantiation(instance):
    assert isinstance(instance, gpfl_GBoolFalse)

@given(instance=gpfl_PortLit_strategy)
@settings(max_examples=50)
def test_gpfl_portlit_instantiation(instance):
    assert isinstance(instance, gpfl_PortLit)



@given(instance=gpfl_PortLit_strategy)
def test_gpfl_portlit_inSide_setter(instance):
    original = instance.inSide
    instance.inSide = original
    assert instance.inSide == original

@given(instance=gpfl_DropCmd_strategy)
@settings(max_examples=50)
def test_gpfl_dropcmd_instantiation(instance):
    assert isinstance(instance, gpfl_DropCmd)

@given(instance=gpfl_IterStmt_strategy)
@settings(max_examples=50)
def test_gpfl_iterstmt_instantiation(instance):
    assert isinstance(instance, gpfl_IterStmt)

@given(instance=gpfl_NopCmd_strategy)
@settings(max_examples=50)
def test_gpfl_nopcmd_instantiation(instance):
    assert isinstance(instance, gpfl_NopCmd)

@given(instance=gpfl_CmdNEq_strategy)
@settings(max_examples=50)
def test_gpfl_cmdneq_instantiation(instance):
    assert isinstance(instance, gpfl_CmdNEq)

@given(instance=gpfl_CondStmt_strategy)
@settings(max_examples=50)
def test_gpfl_condstmt_instantiation(instance):
    assert isinstance(instance, gpfl_CondStmt)

@given(instance=gpfl_Transition_strategy)
@settings(max_examples=50)
def test_gpfl_transition_instantiation(instance):
    assert isinstance(instance, gpfl_Transition)



@given(instance=gpfl_Transition_strategy)
def test_gpfl_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=gpfl_Field_strategy)
@settings(max_examples=50)
def test_gpfl_field_instantiation(instance):
    assert isinstance(instance, gpfl_Field)



@given(instance=gpfl_Field_strategy)
def test_gpfl_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl_GExpression_strategy)
@settings(max_examples=50)
def test_gpfl_gexpression_instantiation(instance):
    assert isinstance(instance, gpfl_GExpression)

@given(instance=gpfl_AutomataDef_strategy)
@settings(max_examples=50)
def test_gpfl_automatadef_instantiation(instance):
    assert isinstance(instance, gpfl_AutomataDef)



@given(instance=gpfl_AutomataDef_strategy)
def test_gpfl_automatadef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gpfl_Program_strategy)
@settings(max_examples=50)
def test_gpfl_program_instantiation(instance):
    assert isinstance(instance, gpfl_Program)



@given(instance=gpfl_Program_strategy)
def test_gpfl_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

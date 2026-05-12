import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Model_PhaseTransition,
    PhaseTransition,
    Model_EClassifier,
    Model_Port,
    Port,
    Model_EOC,
    Model_IC,
    Model_EIC,
    Model_Event,
    Model_Phase,
    Model_ExtTrans,
    Model_ConfTrans,
    Model_IntTransition,
    DEVS,
    Model_CoupledDEVS,
    Model_AtomicDEVS,
    Model_OPort,
    Model_IPort,
    Model_DEVS,
    Model_Variable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_phasetransition_is_not_abstract():
    assert not inspect.isabstract(Model_PhaseTransition)


def test_model_phasetransition_constructor_exists():
    assert callable(Model_PhaseTransition.__init__)


def test_model_phasetransition_constructor_args():
    sig = inspect.signature(Model_PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_phasetransition_is_not_abstract():
    assert not inspect.isabstract(PhaseTransition)


def test_phasetransition_constructor_exists():
    assert callable(PhaseTransition.__init__)


def test_phasetransition_constructor_args():
    sig = inspect.signature(PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_model_eclassifier_is_not_abstract():
    assert not inspect.isabstract(Model_EClassifier)


def test_model_eclassifier_constructor_exists():
    assert callable(Model_EClassifier.__init__)


def test_model_eclassifier_constructor_args():
    sig = inspect.signature(Model_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_model_port_is_not_abstract():
    assert not inspect.isabstract(Model_Port)


def test_model_port_constructor_exists():
    assert callable(Model_Port.__init__)


def test_model_port_constructor_args():
    sig = inspect.signature(Model_Port.__init__)
    params = list(sig.parameters.keys())
    assert "portId" in params, "Missing parameter 'portId'"

def test_model_port_has_portId():
    assert hasattr(Model_Port, "portId")
    descriptor = None
    for klass in Model_Port.__mro__:
        if "portId" in klass.__dict__:
            descriptor = klass.__dict__["portId"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_model_eoc_is_not_abstract():
    assert not inspect.isabstract(Model_EOC)


def test_model_eoc_constructor_exists():
    assert callable(Model_EOC.__init__)


def test_model_eoc_constructor_args():
    sig = inspect.signature(Model_EOC.__init__)
    params = list(sig.parameters.keys())



def test_model_ic_is_not_abstract():
    assert not inspect.isabstract(Model_IC)


def test_model_ic_constructor_exists():
    assert callable(Model_IC.__init__)


def test_model_ic_constructor_args():
    sig = inspect.signature(Model_IC.__init__)
    params = list(sig.parameters.keys())



def test_model_eic_is_not_abstract():
    assert not inspect.isabstract(Model_EIC)


def test_model_eic_constructor_exists():
    assert callable(Model_EIC.__init__)


def test_model_eic_constructor_args():
    sig = inspect.signature(Model_EIC.__init__)
    params = list(sig.parameters.keys())



def test_model_event_is_not_abstract():
    assert not inspect.isabstract(Model_Event)


def test_model_event_constructor_exists():
    assert callable(Model_Event.__init__)


def test_model_event_constructor_args():
    sig = inspect.signature(Model_Event.__init__)
    params = list(sig.parameters.keys())



def test_model_phase_is_not_abstract():
    assert not inspect.isabstract(Model_Phase)


def test_model_phase_constructor_exists():
    assert callable(Model_Phase.__init__)


def test_model_phase_constructor_args():
    sig = inspect.signature(Model_Phase.__init__)
    params = list(sig.parameters.keys())
    assert "timeAdvance" in params, "Missing parameter 'timeAdvance'"
    assert "phaseID" in params, "Missing parameter 'phaseID'"

def test_model_phase_has_timeAdvance():
    assert hasattr(Model_Phase, "timeAdvance")
    descriptor = None
    for klass in Model_Phase.__mro__:
        if "timeAdvance" in klass.__dict__:
            descriptor = klass.__dict__["timeAdvance"]
            break
    assert isinstance(descriptor, property)

def test_model_phase_has_phaseID():
    assert hasattr(Model_Phase, "phaseID")
    descriptor = None
    for klass in Model_Phase.__mro__:
        if "phaseID" in klass.__dict__:
            descriptor = klass.__dict__["phaseID"]
            break
    assert isinstance(descriptor, property)



def test_model_exttrans_is_not_abstract():
    assert not inspect.isabstract(Model_ExtTrans)


def test_model_exttrans_constructor_exists():
    assert callable(Model_ExtTrans.__init__)


def test_model_exttrans_constructor_args():
    sig = inspect.signature(Model_ExtTrans.__init__)
    params = list(sig.parameters.keys())



def test_model_conftrans_is_not_abstract():
    assert not inspect.isabstract(Model_ConfTrans)


def test_model_conftrans_constructor_exists():
    assert callable(Model_ConfTrans.__init__)


def test_model_conftrans_constructor_args():
    sig = inspect.signature(Model_ConfTrans.__init__)
    params = list(sig.parameters.keys())



def test_model_inttransition_is_not_abstract():
    assert not inspect.isabstract(Model_IntTransition)


def test_model_inttransition_constructor_exists():
    assert callable(Model_IntTransition.__init__)


def test_model_inttransition_constructor_args():
    sig = inspect.signature(Model_IntTransition.__init__)
    params = list(sig.parameters.keys())



def test_devs_is_not_abstract():
    assert not inspect.isabstract(DEVS)


def test_devs_constructor_exists():
    assert callable(DEVS.__init__)


def test_devs_constructor_args():
    sig = inspect.signature(DEVS.__init__)
    params = list(sig.parameters.keys())



def test_model_coupleddevs_is_not_abstract():
    assert not inspect.isabstract(Model_CoupledDEVS)


def test_model_coupleddevs_constructor_exists():
    assert callable(Model_CoupledDEVS.__init__)


def test_model_coupleddevs_constructor_args():
    sig = inspect.signature(Model_CoupledDEVS.__init__)
    params = list(sig.parameters.keys())



def test_model_atomicdevs_is_not_abstract():
    assert not inspect.isabstract(Model_AtomicDEVS)


def test_model_atomicdevs_constructor_exists():
    assert callable(Model_AtomicDEVS.__init__)


def test_model_atomicdevs_constructor_args():
    sig = inspect.signature(Model_AtomicDEVS.__init__)
    params = list(sig.parameters.keys())



def test_model_oport_is_not_abstract():
    assert not inspect.isabstract(Model_OPort)


def test_model_oport_constructor_exists():
    assert callable(Model_OPort.__init__)


def test_model_oport_constructor_args():
    sig = inspect.signature(Model_OPort.__init__)
    params = list(sig.parameters.keys())



def test_model_iport_is_not_abstract():
    assert not inspect.isabstract(Model_IPort)


def test_model_iport_constructor_exists():
    assert callable(Model_IPort.__init__)


def test_model_iport_constructor_args():
    sig = inspect.signature(Model_IPort.__init__)
    params = list(sig.parameters.keys())



def test_model_devs_is_not_abstract():
    assert not inspect.isabstract(Model_DEVS)


def test_model_devs_constructor_exists():
    assert callable(Model_DEVS.__init__)


def test_model_devs_constructor_args():
    sig = inspect.signature(Model_DEVS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_devs_has_name():
    assert hasattr(Model_DEVS, "name")
    descriptor = None
    for klass in Model_DEVS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_variable_is_not_abstract():
    assert not inspect.isabstract(Model_Variable)


def test_model_variable_constructor_exists():
    assert callable(Model_Variable.__init__)


def test_model_variable_constructor_args():
    sig = inspect.signature(Model_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_variable_has_name():
    assert hasattr(Model_Variable, "name")
    descriptor = None
    for klass in Model_Variable.__mro__:
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
Model_PhaseTransition_strategy = st.builds(
    Model_PhaseTransition,
)
PhaseTransition_strategy = st.builds(
    PhaseTransition,
)
Model_EClassifier_strategy = st.builds(
    Model_EClassifier,
)
Model_Port_strategy = st.builds(
    Model_Port,
    portId=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
Model_EOC_strategy = st.builds(
    Model_EOC,
)
Model_IC_strategy = st.builds(
    Model_IC,
)
Model_EIC_strategy = st.builds(
    Model_EIC,
)
Model_Event_strategy = st.builds(
    Model_Event,
)
Model_Phase_strategy = st.builds(
    Model_Phase,
    timeAdvance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    phaseID=
        safe_text
)
Model_ExtTrans_strategy = st.builds(
    Model_ExtTrans,
)
Model_ConfTrans_strategy = st.builds(
    Model_ConfTrans,
)
Model_IntTransition_strategy = st.builds(
    Model_IntTransition,
)
DEVS_strategy = st.builds(
    DEVS,
)
Model_CoupledDEVS_strategy = st.builds(
    Model_CoupledDEVS,
)
Model_AtomicDEVS_strategy = st.builds(
    Model_AtomicDEVS,
)
Model_OPort_strategy = st.builds(
    Model_OPort,
)
Model_IPort_strategy = st.builds(
    Model_IPort,
)
Model_DEVS_strategy = st.builds(
    Model_DEVS,
    name=
        safe_text
)
Model_Variable_strategy = st.builds(
    Model_Variable,
    name=
        safe_text
)

@given(instance=Model_PhaseTransition_strategy)
@settings(max_examples=50)
def test_model_phasetransition_instantiation(instance):
    assert isinstance(instance, Model_PhaseTransition)

@given(instance=PhaseTransition_strategy)
@settings(max_examples=50)
def test_phasetransition_instantiation(instance):
    assert isinstance(instance, PhaseTransition)

@given(instance=Model_EClassifier_strategy)
@settings(max_examples=50)
def test_model_eclassifier_instantiation(instance):
    assert isinstance(instance, Model_EClassifier)

@given(instance=Model_Port_strategy)
@settings(max_examples=50)
def test_model_port_instantiation(instance):
    assert isinstance(instance, Model_Port)



@given(instance=Model_Port_strategy)
def test_model_port_portId_setter(instance):
    original = instance.portId
    instance.portId = original
    assert instance.portId == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Model_EOC_strategy)
@settings(max_examples=50)
def test_model_eoc_instantiation(instance):
    assert isinstance(instance, Model_EOC)

@given(instance=Model_IC_strategy)
@settings(max_examples=50)
def test_model_ic_instantiation(instance):
    assert isinstance(instance, Model_IC)

@given(instance=Model_EIC_strategy)
@settings(max_examples=50)
def test_model_eic_instantiation(instance):
    assert isinstance(instance, Model_EIC)

@given(instance=Model_Event_strategy)
@settings(max_examples=50)
def test_model_event_instantiation(instance):
    assert isinstance(instance, Model_Event)

@given(instance=Model_Phase_strategy)
@settings(max_examples=50)
def test_model_phase_instantiation(instance):
    assert isinstance(instance, Model_Phase)



@given(instance=Model_Phase_strategy)
def test_model_phase_timeAdvance_setter(instance):
    original = instance.timeAdvance
    instance.timeAdvance = original
    assert instance.timeAdvance == original



@given(instance=Model_Phase_strategy)
def test_model_phase_phaseID_setter(instance):
    original = instance.phaseID
    instance.phaseID = original
    assert instance.phaseID == original

@given(instance=Model_ExtTrans_strategy)
@settings(max_examples=50)
def test_model_exttrans_instantiation(instance):
    assert isinstance(instance, Model_ExtTrans)

@given(instance=Model_ConfTrans_strategy)
@settings(max_examples=50)
def test_model_conftrans_instantiation(instance):
    assert isinstance(instance, Model_ConfTrans)

@given(instance=Model_IntTransition_strategy)
@settings(max_examples=50)
def test_model_inttransition_instantiation(instance):
    assert isinstance(instance, Model_IntTransition)

@given(instance=DEVS_strategy)
@settings(max_examples=50)
def test_devs_instantiation(instance):
    assert isinstance(instance, DEVS)

@given(instance=Model_CoupledDEVS_strategy)
@settings(max_examples=50)
def test_model_coupleddevs_instantiation(instance):
    assert isinstance(instance, Model_CoupledDEVS)

@given(instance=Model_AtomicDEVS_strategy)
@settings(max_examples=50)
def test_model_atomicdevs_instantiation(instance):
    assert isinstance(instance, Model_AtomicDEVS)

@given(instance=Model_OPort_strategy)
@settings(max_examples=50)
def test_model_oport_instantiation(instance):
    assert isinstance(instance, Model_OPort)

@given(instance=Model_IPort_strategy)
@settings(max_examples=50)
def test_model_iport_instantiation(instance):
    assert isinstance(instance, Model_IPort)

@given(instance=Model_DEVS_strategy)
@settings(max_examples=50)
def test_model_devs_instantiation(instance):
    assert isinstance(instance, Model_DEVS)



@given(instance=Model_DEVS_strategy)
def test_model_devs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Model_Variable_strategy)
@settings(max_examples=50)
def test_model_variable_instantiation(instance):
    assert isinstance(instance, Model_Variable)



@given(instance=Model_Variable_strategy)
def test_model_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Predicate,
    Model_Expression,
    Model_SimplePredicate,
    Model_PhaseTransition,
    Model_Predicate,
    Model_Event,
    PhaseTransition,
    Model_Property,
    Model_EOC,
    Model_IC,
    Model_EIC,
    Model_Variable,
    Model_Phase,
    Model_ExtTrans,
    Model_ConfTrans,
    Model_IntTransition,
    DEVS,
    Model_CoupledDEVS,
    Model_AtomicDEVS,
    Model_Port,
    Port,
    Model_DEVS,
    Model_OPort,
    Model_IPort,
    Classifier,
    MathOperators,
    LogicOperators,
    RelationalOperators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_model_expression_is_not_abstract():
    assert not inspect.isabstract(Model_Expression)


def test_model_expression_constructor_exists():
    assert callable(Model_Expression.__init__)


def test_model_expression_constructor_args():
    sig = inspect.signature(Model_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model_expression_has_operator():
    assert hasattr(Model_Expression, "operator")
    descriptor = None
    for klass in Model_Expression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model_simplepredicate_is_not_abstract():
    assert not inspect.isabstract(Model_SimplePredicate)


def test_model_simplepredicate_constructor_exists():
    assert callable(Model_SimplePredicate.__init__)


def test_model_simplepredicate_constructor_args():
    sig = inspect.signature(Model_SimplePredicate.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model_simplepredicate_has_operator():
    assert hasattr(Model_SimplePredicate, "operator")
    descriptor = None
    for klass in Model_SimplePredicate.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model_phasetransition_is_not_abstract():
    assert not inspect.isabstract(Model_PhaseTransition)


def test_model_phasetransition_constructor_exists():
    assert callable(Model_PhaseTransition.__init__)


def test_model_phasetransition_constructor_args():
    sig = inspect.signature(Model_PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_model_predicate_is_not_abstract():
    assert not inspect.isabstract(Model_Predicate)


def test_model_predicate_constructor_exists():
    assert callable(Model_Predicate.__init__)


def test_model_predicate_constructor_args():
    sig = inspect.signature(Model_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_model_event_is_not_abstract():
    assert not inspect.isabstract(Model_Event)


def test_model_event_constructor_exists():
    assert callable(Model_Event.__init__)


def test_model_event_constructor_args():
    sig = inspect.signature(Model_Event.__init__)
    params = list(sig.parameters.keys())



def test_phasetransition_is_not_abstract():
    assert not inspect.isabstract(PhaseTransition)


def test_phasetransition_constructor_exists():
    assert callable(PhaseTransition.__init__)


def test_phasetransition_constructor_args():
    sig = inspect.signature(PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_model_property_is_not_abstract():
    assert not inspect.isabstract(Model_Property)


def test_model_property_constructor_exists():
    assert callable(Model_Property.__init__)


def test_model_property_constructor_args():
    sig = inspect.signature(Model_Property.__init__)
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



def test_model_variable_is_not_abstract():
    assert not inspect.isabstract(Model_Variable)


def test_model_variable_constructor_exists():
    assert callable(Model_Variable.__init__)


def test_model_variable_constructor_args():
    sig = inspect.signature(Model_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_variable_has_domain():
    assert hasattr(Model_Variable, "domain")
    descriptor = None
    for klass in Model_Variable.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

def test_model_variable_has_name():
    assert hasattr(Model_Variable, "name")
    descriptor = None
    for klass in Model_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_phase_is_not_abstract():
    assert not inspect.isabstract(Model_Phase)


def test_model_phase_constructor_exists():
    assert callable(Model_Phase.__init__)


def test_model_phase_constructor_args():
    sig = inspect.signature(Model_Phase.__init__)
    params = list(sig.parameters.keys())
    assert "phaseID" in params, "Missing parameter 'phaseID'"
    assert "timeAdvance" in params, "Missing parameter 'timeAdvance'"

def test_model_phase_has_phaseID():
    assert hasattr(Model_Phase, "phaseID")
    descriptor = None
    for klass in Model_Phase.__mro__:
        if "phaseID" in klass.__dict__:
            descriptor = klass.__dict__["phaseID"]
            break
    assert isinstance(descriptor, property)

def test_model_phase_has_timeAdvance():
    assert hasattr(Model_Phase, "timeAdvance")
    descriptor = None
    for klass in Model_Phase.__mro__:
        if "timeAdvance" in klass.__dict__:
            descriptor = klass.__dict__["timeAdvance"]
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



def test_model_port_is_not_abstract():
    assert not inspect.isabstract(Model_Port)


def test_model_port_constructor_exists():
    assert callable(Model_Port.__init__)


def test_model_port_constructor_args():
    sig = inspect.signature(Model_Port.__init__)
    params = list(sig.parameters.keys())
    assert "portType" in params, "Missing parameter 'portType'"
    assert "portId" in params, "Missing parameter 'portId'"

def test_model_port_has_portType():
    assert hasattr(Model_Port, "portType")
    descriptor = None
    for klass in Model_Port.__mro__:
        if "portType" in klass.__dict__:
            descriptor = klass.__dict__["portType"]
            break
    assert isinstance(descriptor, property)

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

def test_classifier_exists():
    # Check that the Enumeration exists
    assert Classifier is not None

def test_classifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Classifier]
    expected_literals = [
        "Integer",
        "String",
        "Class",
        "Double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Classifier"

def test_mathoperators_exists():
    # Check that the Enumeration exists
    assert MathOperators is not None

def test_mathoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MathOperators]
    expected_literals = [
        "plus",
        "divide",
        "multiple",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MathOperators"

def test_logicoperators_exists():
    # Check that the Enumeration exists
    assert LogicOperators is not None

def test_logicoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperators]
    expected_literals = [
        "and_",
        "not_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperators"

def test_relationaloperators_exists():
    # Check that the Enumeration exists
    assert RelationalOperators is not None

def test_relationaloperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperators]
    expected_literals = [
        "greater_or_equals",
        "lesser_or_equals",
        "lesser",
        "not_equals",
        "equals",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperators"


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
Predicate_strategy = st.builds(
    Predicate,
)
Model_Expression_strategy = st.builds(
    Model_Expression,
    operator=
        safe_text
)
Model_SimplePredicate_strategy = st.builds(
    Model_SimplePredicate,
    operator=
        safe_text
)
Model_PhaseTransition_strategy = st.builds(
    Model_PhaseTransition,
)
Model_Predicate_strategy = st.builds(
    Model_Predicate,
)
Model_Event_strategy = st.builds(
    Model_Event,
)
PhaseTransition_strategy = st.builds(
    PhaseTransition,
)
Model_Property_strategy = st.builds(
    Model_Property,
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
Model_Variable_strategy = st.builds(
    Model_Variable,
    domain=
        safe_text,
    name=
        safe_text
)
Model_Phase_strategy = st.builds(
    Model_Phase,
    phaseID=
        safe_text,
    timeAdvance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
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
Model_Port_strategy = st.builds(
    Model_Port,
    portType=
        safe_text,
    portId=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
Model_DEVS_strategy = st.builds(
    Model_DEVS,
    name=
        safe_text
)
Model_OPort_strategy = st.builds(
    Model_OPort,
)
Model_IPort_strategy = st.builds(
    Model_IPort,
)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=Model_Expression_strategy)
@settings(max_examples=50)
def test_model_expression_instantiation(instance):
    assert isinstance(instance, Model_Expression)



@given(instance=Model_Expression_strategy)
def test_model_expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Model_SimplePredicate_strategy)
@settings(max_examples=50)
def test_model_simplepredicate_instantiation(instance):
    assert isinstance(instance, Model_SimplePredicate)



@given(instance=Model_SimplePredicate_strategy)
def test_model_simplepredicate_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Model_PhaseTransition_strategy)
@settings(max_examples=50)
def test_model_phasetransition_instantiation(instance):
    assert isinstance(instance, Model_PhaseTransition)

@given(instance=Model_Predicate_strategy)
@settings(max_examples=50)
def test_model_predicate_instantiation(instance):
    assert isinstance(instance, Model_Predicate)

@given(instance=Model_Event_strategy)
@settings(max_examples=50)
def test_model_event_instantiation(instance):
    assert isinstance(instance, Model_Event)

@given(instance=PhaseTransition_strategy)
@settings(max_examples=50)
def test_phasetransition_instantiation(instance):
    assert isinstance(instance, PhaseTransition)

@given(instance=Model_Property_strategy)
@settings(max_examples=50)
def test_model_property_instantiation(instance):
    assert isinstance(instance, Model_Property)

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

@given(instance=Model_Variable_strategy)
@settings(max_examples=50)
def test_model_variable_instantiation(instance):
    assert isinstance(instance, Model_Variable)



@given(instance=Model_Variable_strategy)
def test_model_variable_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original



@given(instance=Model_Variable_strategy)
def test_model_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Model_Phase_strategy)
@settings(max_examples=50)
def test_model_phase_instantiation(instance):
    assert isinstance(instance, Model_Phase)



@given(instance=Model_Phase_strategy)
def test_model_phase_phaseID_setter(instance):
    original = instance.phaseID
    instance.phaseID = original
    assert instance.phaseID == original



@given(instance=Model_Phase_strategy)
def test_model_phase_timeAdvance_setter(instance):
    original = instance.timeAdvance
    instance.timeAdvance = original
    assert instance.timeAdvance == original

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

@given(instance=Model_Port_strategy)
@settings(max_examples=50)
def test_model_port_instantiation(instance):
    assert isinstance(instance, Model_Port)



@given(instance=Model_Port_strategy)
def test_model_port_portType_setter(instance):
    original = instance.portType
    instance.portType = original
    assert instance.portType == original



@given(instance=Model_Port_strategy)
def test_model_port_portId_setter(instance):
    original = instance.portId
    instance.portId = original
    assert instance.portId == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Model_DEVS_strategy)
@settings(max_examples=50)
def test_model_devs_instantiation(instance):
    assert isinstance(instance, Model_DEVS)



@given(instance=Model_DEVS_strategy)
def test_model_devs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Model_OPort_strategy)
@settings(max_examples=50)
def test_model_oport_instantiation(instance):
    assert isinstance(instance, Model_OPort)

@given(instance=Model_IPort_strategy)
@settings(max_examples=50)
def test_model_iport_instantiation(instance):
    assert isinstance(instance, Model_IPort)

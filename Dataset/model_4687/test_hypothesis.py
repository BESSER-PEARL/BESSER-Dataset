import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Predicate,
    Model::Expression,
    Model::SimplePredicate,
    Model::PhaseTransition,
    Model::Predicate,
    Model::Event,
    PhaseTransition,
    Model::Property,
    Model::EOC,
    Model::IC,
    Model::EIC,
    Model::Variable,
    Model::Phase,
    Model::ExtTrans,
    Model::ConfTrans,
    Model::IntTransition,
    DEVS,
    Model::CoupledDEVS,
    Model::AtomicDEVS,
    Model::Port,
    Port,
    Model::DEVS,
    Model::OPort,
    Model::IPort,
    Classifier,
    MathOperators,
    RelationalOperators,
    LogicOperators,
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



def test_model::expression_is_not_abstract():
    assert not inspect.isabstract(Model::Expression)


def test_model::expression_constructor_exists():
    assert callable(Model::Expression.__init__)


def test_model::expression_constructor_args():
    sig = inspect.signature(Model::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model::expression_has_operator():
    assert hasattr(Model::Expression, "operator")
    descriptor = None
    for klass in Model::Expression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model::simplepredicate_is_not_abstract():
    assert not inspect.isabstract(Model::SimplePredicate)


def test_model::simplepredicate_constructor_exists():
    assert callable(Model::SimplePredicate.__init__)


def test_model::simplepredicate_constructor_args():
    sig = inspect.signature(Model::SimplePredicate.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model::simplepredicate_has_operator():
    assert hasattr(Model::SimplePredicate, "operator")
    descriptor = None
    for klass in Model::SimplePredicate.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model::phasetransition_is_not_abstract():
    assert not inspect.isabstract(Model::PhaseTransition)


def test_model::phasetransition_constructor_exists():
    assert callable(Model::PhaseTransition.__init__)


def test_model::phasetransition_constructor_args():
    sig = inspect.signature(Model::PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_model::predicate_is_not_abstract():
    assert not inspect.isabstract(Model::Predicate)


def test_model::predicate_constructor_exists():
    assert callable(Model::Predicate.__init__)


def test_model::predicate_constructor_args():
    sig = inspect.signature(Model::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_model::event_is_not_abstract():
    assert not inspect.isabstract(Model::Event)


def test_model::event_constructor_exists():
    assert callable(Model::Event.__init__)


def test_model::event_constructor_args():
    sig = inspect.signature(Model::Event.__init__)
    params = list(sig.parameters.keys())



def test_phasetransition_is_not_abstract():
    assert not inspect.isabstract(PhaseTransition)


def test_phasetransition_constructor_exists():
    assert callable(PhaseTransition.__init__)


def test_phasetransition_constructor_args():
    sig = inspect.signature(PhaseTransition.__init__)
    params = list(sig.parameters.keys())



def test_model::property_is_not_abstract():
    assert not inspect.isabstract(Model::Property)


def test_model::property_constructor_exists():
    assert callable(Model::Property.__init__)


def test_model::property_constructor_args():
    sig = inspect.signature(Model::Property.__init__)
    params = list(sig.parameters.keys())



def test_model::eoc_is_not_abstract():
    assert not inspect.isabstract(Model::EOC)


def test_model::eoc_constructor_exists():
    assert callable(Model::EOC.__init__)


def test_model::eoc_constructor_args():
    sig = inspect.signature(Model::EOC.__init__)
    params = list(sig.parameters.keys())



def test_model::ic_is_not_abstract():
    assert not inspect.isabstract(Model::IC)


def test_model::ic_constructor_exists():
    assert callable(Model::IC.__init__)


def test_model::ic_constructor_args():
    sig = inspect.signature(Model::IC.__init__)
    params = list(sig.parameters.keys())



def test_model::eic_is_not_abstract():
    assert not inspect.isabstract(Model::EIC)


def test_model::eic_constructor_exists():
    assert callable(Model::EIC.__init__)


def test_model::eic_constructor_args():
    sig = inspect.signature(Model::EIC.__init__)
    params = list(sig.parameters.keys())



def test_model::variable_is_not_abstract():
    assert not inspect.isabstract(Model::Variable)


def test_model::variable_constructor_exists():
    assert callable(Model::Variable.__init__)


def test_model::variable_constructor_args():
    sig = inspect.signature(Model::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::variable_has_domain():
    assert hasattr(Model::Variable, "domain")
    descriptor = None
    for klass in Model::Variable.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

def test_model::variable_has_name():
    assert hasattr(Model::Variable, "name")
    descriptor = None
    for klass in Model::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::phase_is_not_abstract():
    assert not inspect.isabstract(Model::Phase)


def test_model::phase_constructor_exists():
    assert callable(Model::Phase.__init__)


def test_model::phase_constructor_args():
    sig = inspect.signature(Model::Phase.__init__)
    params = list(sig.parameters.keys())
    assert "phaseID" in params, "Missing parameter 'phaseID'"
    assert "timeAdvance" in params, "Missing parameter 'timeAdvance'"

def test_model::phase_has_phaseID():
    assert hasattr(Model::Phase, "phaseID")
    descriptor = None
    for klass in Model::Phase.__mro__:
        if "phaseID" in klass.__dict__:
            descriptor = klass.__dict__["phaseID"]
            break
    assert isinstance(descriptor, property)

def test_model::phase_has_timeAdvance():
    assert hasattr(Model::Phase, "timeAdvance")
    descriptor = None
    for klass in Model::Phase.__mro__:
        if "timeAdvance" in klass.__dict__:
            descriptor = klass.__dict__["timeAdvance"]
            break
    assert isinstance(descriptor, property)



def test_model::exttrans_is_not_abstract():
    assert not inspect.isabstract(Model::ExtTrans)


def test_model::exttrans_constructor_exists():
    assert callable(Model::ExtTrans.__init__)


def test_model::exttrans_constructor_args():
    sig = inspect.signature(Model::ExtTrans.__init__)
    params = list(sig.parameters.keys())



def test_model::conftrans_is_not_abstract():
    assert not inspect.isabstract(Model::ConfTrans)


def test_model::conftrans_constructor_exists():
    assert callable(Model::ConfTrans.__init__)


def test_model::conftrans_constructor_args():
    sig = inspect.signature(Model::ConfTrans.__init__)
    params = list(sig.parameters.keys())



def test_model::inttransition_is_not_abstract():
    assert not inspect.isabstract(Model::IntTransition)


def test_model::inttransition_constructor_exists():
    assert callable(Model::IntTransition.__init__)


def test_model::inttransition_constructor_args():
    sig = inspect.signature(Model::IntTransition.__init__)
    params = list(sig.parameters.keys())



def test_devs_is_not_abstract():
    assert not inspect.isabstract(DEVS)


def test_devs_constructor_exists():
    assert callable(DEVS.__init__)


def test_devs_constructor_args():
    sig = inspect.signature(DEVS.__init__)
    params = list(sig.parameters.keys())



def test_model::coupleddevs_is_not_abstract():
    assert not inspect.isabstract(Model::CoupledDEVS)


def test_model::coupleddevs_constructor_exists():
    assert callable(Model::CoupledDEVS.__init__)


def test_model::coupleddevs_constructor_args():
    sig = inspect.signature(Model::CoupledDEVS.__init__)
    params = list(sig.parameters.keys())



def test_model::atomicdevs_is_not_abstract():
    assert not inspect.isabstract(Model::AtomicDEVS)


def test_model::atomicdevs_constructor_exists():
    assert callable(Model::AtomicDEVS.__init__)


def test_model::atomicdevs_constructor_args():
    sig = inspect.signature(Model::AtomicDEVS.__init__)
    params = list(sig.parameters.keys())



def test_model::port_is_not_abstract():
    assert not inspect.isabstract(Model::Port)


def test_model::port_constructor_exists():
    assert callable(Model::Port.__init__)


def test_model::port_constructor_args():
    sig = inspect.signature(Model::Port.__init__)
    params = list(sig.parameters.keys())
    assert "portId" in params, "Missing parameter 'portId'"
    assert "portType" in params, "Missing parameter 'portType'"

def test_model::port_has_portId():
    assert hasattr(Model::Port, "portId")
    descriptor = None
    for klass in Model::Port.__mro__:
        if "portId" in klass.__dict__:
            descriptor = klass.__dict__["portId"]
            break
    assert isinstance(descriptor, property)

def test_model::port_has_portType():
    assert hasattr(Model::Port, "portType")
    descriptor = None
    for klass in Model::Port.__mro__:
        if "portType" in klass.__dict__:
            descriptor = klass.__dict__["portType"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_model::devs_is_not_abstract():
    assert not inspect.isabstract(Model::DEVS)


def test_model::devs_constructor_exists():
    assert callable(Model::DEVS.__init__)


def test_model::devs_constructor_args():
    sig = inspect.signature(Model::DEVS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::devs_has_name():
    assert hasattr(Model::DEVS, "name")
    descriptor = None
    for klass in Model::DEVS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::oport_is_not_abstract():
    assert not inspect.isabstract(Model::OPort)


def test_model::oport_constructor_exists():
    assert callable(Model::OPort.__init__)


def test_model::oport_constructor_args():
    sig = inspect.signature(Model::OPort.__init__)
    params = list(sig.parameters.keys())



def test_model::iport_is_not_abstract():
    assert not inspect.isabstract(Model::IPort)


def test_model::iport_constructor_exists():
    assert callable(Model::IPort.__init__)


def test_model::iport_constructor_args():
    sig = inspect.signature(Model::IPort.__init__)
    params = list(sig.parameters.keys())

def test_classifier_exists():
    # Check that the Enumeration exists
    assert Classifier is not None

def test_classifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Classifier]
    expected_literals = [
        "Class",
        "String",
        "Double",
        "Integer",
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
        "minus",
        "multiple",
        "plus",
        "divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MathOperators"

def test_relationaloperators_exists():
    # Check that the Enumeration exists
    assert RelationalOperators is not None

def test_relationaloperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperators]
    expected_literals = [
        "greater_or_equals",
        "not_equals",
        "lesser",
        "equals",
        "greater",
        "lesser_or_equals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperators"

def test_logicoperators_exists():
    # Check that the Enumeration exists
    assert LogicOperators is not None

def test_logicoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperators]
    expected_literals = [
        "not_",
        "or_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperators"


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
Model::Expression_strategy = st.builds(
    Model::Expression,
    operator=
        safe_text
)
Model::SimplePredicate_strategy = st.builds(
    Model::SimplePredicate,
    operator=
        safe_text
)
Model::PhaseTransition_strategy = st.builds(
    Model::PhaseTransition,
)
Model::Predicate_strategy = st.builds(
    Model::Predicate,
)
Model::Event_strategy = st.builds(
    Model::Event,
)
PhaseTransition_strategy = st.builds(
    PhaseTransition,
)
Model::Property_strategy = st.builds(
    Model::Property,
)
Model::EOC_strategy = st.builds(
    Model::EOC,
)
Model::IC_strategy = st.builds(
    Model::IC,
)
Model::EIC_strategy = st.builds(
    Model::EIC,
)
Model::Variable_strategy = st.builds(
    Model::Variable,
    domain=
        safe_text,
    name=
        safe_text
)
Model::Phase_strategy = st.builds(
    Model::Phase,
    phaseID=
        safe_text,
    timeAdvance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Model::ExtTrans_strategy = st.builds(
    Model::ExtTrans,
)
Model::ConfTrans_strategy = st.builds(
    Model::ConfTrans,
)
Model::IntTransition_strategy = st.builds(
    Model::IntTransition,
)
DEVS_strategy = st.builds(
    DEVS,
)
Model::CoupledDEVS_strategy = st.builds(
    Model::CoupledDEVS,
)
Model::AtomicDEVS_strategy = st.builds(
    Model::AtomicDEVS,
)
Model::Port_strategy = st.builds(
    Model::Port,
    portId=
        safe_text,
    portType=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
Model::DEVS_strategy = st.builds(
    Model::DEVS,
    name=
        safe_text
)
Model::OPort_strategy = st.builds(
    Model::OPort,
)
Model::IPort_strategy = st.builds(
    Model::IPort,
)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=Model::Expression_strategy)
@settings(max_examples=50)
def test_model::expression_instantiation(instance):
    assert isinstance(instance, Model::Expression)

@given(instance=Model::Expression_strategy)
def test_model::expression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Model::Expression_strategy)
def test_model::expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Model::SimplePredicate_strategy)
@settings(max_examples=50)
def test_model::simplepredicate_instantiation(instance):
    assert isinstance(instance, Model::SimplePredicate)

@given(instance=Model::SimplePredicate_strategy)
def test_model::simplepredicate_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Model::SimplePredicate_strategy)
def test_model::simplepredicate_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Model::PhaseTransition_strategy)
@settings(max_examples=50)
def test_model::phasetransition_instantiation(instance):
    assert isinstance(instance, Model::PhaseTransition)

@given(instance=Model::Predicate_strategy)
@settings(max_examples=50)
def test_model::predicate_instantiation(instance):
    assert isinstance(instance, Model::Predicate)

@given(instance=Model::Event_strategy)
@settings(max_examples=50)
def test_model::event_instantiation(instance):
    assert isinstance(instance, Model::Event)

@given(instance=PhaseTransition_strategy)
@settings(max_examples=50)
def test_phasetransition_instantiation(instance):
    assert isinstance(instance, PhaseTransition)

@given(instance=Model::Property_strategy)
@settings(max_examples=50)
def test_model::property_instantiation(instance):
    assert isinstance(instance, Model::Property)

@given(instance=Model::EOC_strategy)
@settings(max_examples=50)
def test_model::eoc_instantiation(instance):
    assert isinstance(instance, Model::EOC)

@given(instance=Model::IC_strategy)
@settings(max_examples=50)
def test_model::ic_instantiation(instance):
    assert isinstance(instance, Model::IC)

@given(instance=Model::EIC_strategy)
@settings(max_examples=50)
def test_model::eic_instantiation(instance):
    assert isinstance(instance, Model::EIC)

@given(instance=Model::Variable_strategy)
@settings(max_examples=50)
def test_model::variable_instantiation(instance):
    assert isinstance(instance, Model::Variable)

@given(instance=Model::Variable_strategy)
def test_model::variable_domain_type(instance):
    assert isinstance(instance.domain, str)


@given(instance=Model::Variable_strategy)
def test_model::variable_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original

@given(instance=Model::Variable_strategy)
def test_model::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Model::Variable_strategy)
def test_model::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Model::Phase_strategy)
@settings(max_examples=50)
def test_model::phase_instantiation(instance):
    assert isinstance(instance, Model::Phase)

@given(instance=Model::Phase_strategy)
def test_model::phase_phaseID_type(instance):
    assert isinstance(instance.phaseID, str)


@given(instance=Model::Phase_strategy)
def test_model::phase_phaseID_setter(instance):
    original = instance.phaseID
    instance.phaseID = original
    assert instance.phaseID == original

@given(instance=Model::Phase_strategy)
def test_model::phase_timeAdvance_type(instance):
    assert isinstance(instance.timeAdvance, float)


@given(instance=Model::Phase_strategy)
def test_model::phase_timeAdvance_setter(instance):
    original = instance.timeAdvance
    instance.timeAdvance = original
    assert instance.timeAdvance == original

@given(instance=Model::ExtTrans_strategy)
@settings(max_examples=50)
def test_model::exttrans_instantiation(instance):
    assert isinstance(instance, Model::ExtTrans)

@given(instance=Model::ConfTrans_strategy)
@settings(max_examples=50)
def test_model::conftrans_instantiation(instance):
    assert isinstance(instance, Model::ConfTrans)

@given(instance=Model::IntTransition_strategy)
@settings(max_examples=50)
def test_model::inttransition_instantiation(instance):
    assert isinstance(instance, Model::IntTransition)

@given(instance=DEVS_strategy)
@settings(max_examples=50)
def test_devs_instantiation(instance):
    assert isinstance(instance, DEVS)

@given(instance=Model::CoupledDEVS_strategy)
@settings(max_examples=50)
def test_model::coupleddevs_instantiation(instance):
    assert isinstance(instance, Model::CoupledDEVS)

@given(instance=Model::AtomicDEVS_strategy)
@settings(max_examples=50)
def test_model::atomicdevs_instantiation(instance):
    assert isinstance(instance, Model::AtomicDEVS)

@given(instance=Model::Port_strategy)
@settings(max_examples=50)
def test_model::port_instantiation(instance):
    assert isinstance(instance, Model::Port)

@given(instance=Model::Port_strategy)
def test_model::port_portId_type(instance):
    assert isinstance(instance.portId, str)


@given(instance=Model::Port_strategy)
def test_model::port_portId_setter(instance):
    original = instance.portId
    instance.portId = original
    assert instance.portId == original

@given(instance=Model::Port_strategy)
def test_model::port_portType_type(instance):
    assert isinstance(instance.portType, str)


@given(instance=Model::Port_strategy)
def test_model::port_portType_setter(instance):
    original = instance.portType
    instance.portType = original
    assert instance.portType == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Model::DEVS_strategy)
@settings(max_examples=50)
def test_model::devs_instantiation(instance):
    assert isinstance(instance, Model::DEVS)

@given(instance=Model::DEVS_strategy)
def test_model::devs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Model::DEVS_strategy)
def test_model::devs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Model::OPort_strategy)
@settings(max_examples=50)
def test_model::oport_instantiation(instance):
    assert isinstance(instance, Model::OPort)

@given(instance=Model::IPort_strategy)
@settings(max_examples=50)
def test_model::iport_instantiation(instance):
    assert isinstance(instance, Model::IPort)

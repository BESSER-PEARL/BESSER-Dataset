import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FMEAEntry,
    failureLogic_FMEDAEntry,
    Cause,
    failureLogic_Gate,
    FailureModel,
    failureLogic_MarkovChain,
    failureLogic_FMEA,
    failureLogic_FaultTree,
    Failure,
    failureLogic_SecurityViolation,
    BaseElement,
    failureLogic_ProbDistParam,
    failureLogic_MinimalCutSets,
    failureLogic_State,
    failureLogic_MinimalCutset,
    failureLogic_ProbDist,
    failureLogic_FMEAEntry,
    failureLogic_Cause,
    failureLogic_Transition,
    failureLogic_Failure,
    failureLogic_FailureModel,
    ODEProductPackage,
    failureLogic_FailureLogicPackage,
    CauseType,
    FailureOriginType,
    GateType,
    FMEAType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fmeaentry_is_not_abstract():
    assert not inspect.isabstract(FMEAEntry)


def test_fmeaentry_constructor_exists():
    assert callable(FMEAEntry.__init__)


def test_fmeaentry_constructor_args():
    sig = inspect.signature(FMEAEntry.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_fmedaentry_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FMEDAEntry)


def test_failurelogic_fmedaentry_constructor_exists():
    assert callable(failureLogic_FMEDAEntry.__init__)


def test_failurelogic_fmedaentry_constructor_args():
    sig = inspect.signature(failureLogic_FMEDAEntry.__init__)
    params = list(sig.parameters.keys())
    assert "diagnosisRate" in params, "Missing parameter 'diagnosisRate'"

def test_failurelogic_fmedaentry_has_diagnosisRate():
    assert hasattr(failureLogic_FMEDAEntry, "diagnosisRate")
    descriptor = None
    for klass in failureLogic_FMEDAEntry.__mro__:
        if "diagnosisRate" in klass.__dict__:
            descriptor = klass.__dict__["diagnosisRate"]
            break
    assert isinstance(descriptor, property)



def test_cause_is_not_abstract():
    assert not inspect.isabstract(Cause)


def test_cause_constructor_exists():
    assert callable(Cause.__init__)


def test_cause_constructor_args():
    sig = inspect.signature(Cause.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_gate_is_not_abstract():
    assert not inspect.isabstract(failureLogic_Gate)


def test_failurelogic_gate_constructor_exists():
    assert callable(failureLogic_Gate.__init__)


def test_failurelogic_gate_constructor_args():
    sig = inspect.signature(failureLogic_Gate.__init__)
    params = list(sig.parameters.keys())
    assert "gateType" in params, "Missing parameter 'gateType'"

def test_failurelogic_gate_has_gateType():
    assert hasattr(failureLogic_Gate, "gateType")
    descriptor = None
    for klass in failureLogic_Gate.__mro__:
        if "gateType" in klass.__dict__:
            descriptor = klass.__dict__["gateType"]
            break
    assert isinstance(descriptor, property)



def test_failuremodel_is_not_abstract():
    assert not inspect.isabstract(FailureModel)


def test_failuremodel_constructor_exists():
    assert callable(FailureModel.__init__)


def test_failuremodel_constructor_args():
    sig = inspect.signature(FailureModel.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_markovchain_is_not_abstract():
    assert not inspect.isabstract(failureLogic_MarkovChain)


def test_failurelogic_markovchain_constructor_exists():
    assert callable(failureLogic_MarkovChain.__init__)


def test_failurelogic_markovchain_constructor_args():
    sig = inspect.signature(failureLogic_MarkovChain.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_fmea_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FMEA)


def test_failurelogic_fmea_constructor_exists():
    assert callable(failureLogic_FMEA.__init__)


def test_failurelogic_fmea_constructor_args():
    sig = inspect.signature(failureLogic_FMEA.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_failurelogic_fmea_has_type():
    assert hasattr(failureLogic_FMEA, "type")
    descriptor = None
    for klass in failureLogic_FMEA.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_faulttree_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FaultTree)


def test_failurelogic_faulttree_constructor_exists():
    assert callable(failureLogic_FaultTree.__init__)


def test_failurelogic_faulttree_constructor_args():
    sig = inspect.signature(failureLogic_FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_failure_is_not_abstract():
    assert not inspect.isabstract(Failure)


def test_failure_constructor_exists():
    assert callable(Failure.__init__)


def test_failure_constructor_args():
    sig = inspect.signature(Failure.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_securityviolation_is_not_abstract():
    assert not inspect.isabstract(failureLogic_SecurityViolation)


def test_failurelogic_securityviolation_constructor_exists():
    assert callable(failureLogic_SecurityViolation.__init__)


def test_failurelogic_securityviolation_constructor_args():
    sig = inspect.signature(failureLogic_SecurityViolation.__init__)
    params = list(sig.parameters.keys())



def test_baseelement_is_not_abstract():
    assert not inspect.isabstract(BaseElement)


def test_baseelement_constructor_exists():
    assert callable(BaseElement.__init__)


def test_baseelement_constructor_args():
    sig = inspect.signature(BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_probdistparam_is_not_abstract():
    assert not inspect.isabstract(failureLogic_ProbDistParam)


def test_failurelogic_probdistparam_constructor_exists():
    assert callable(failureLogic_ProbDistParam.__init__)


def test_failurelogic_probdistparam_constructor_args():
    sig = inspect.signature(failureLogic_ProbDistParam.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_failurelogic_probdistparam_has_value():
    assert hasattr(failureLogic_ProbDistParam, "value")
    descriptor = None
    for klass in failureLogic_ProbDistParam.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_minimalcutsets_is_not_abstract():
    assert not inspect.isabstract(failureLogic_MinimalCutSets)


def test_failurelogic_minimalcutsets_constructor_exists():
    assert callable(failureLogic_MinimalCutSets.__init__)


def test_failurelogic_minimalcutsets_constructor_args():
    sig = inspect.signature(failureLogic_MinimalCutSets.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_state_is_not_abstract():
    assert not inspect.isabstract(failureLogic_State)


def test_failurelogic_state_constructor_exists():
    assert callable(failureLogic_State.__init__)


def test_failurelogic_state_constructor_args():
    sig = inspect.signature(failureLogic_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFailState" in params, "Missing parameter 'isFailState'"
    assert "isInitialState" in params, "Missing parameter 'isInitialState'"

def test_failurelogic_state_has_isFailState():
    assert hasattr(failureLogic_State, "isFailState")
    descriptor = None
    for klass in failureLogic_State.__mro__:
        if "isFailState" in klass.__dict__:
            descriptor = klass.__dict__["isFailState"]
            break
    assert isinstance(descriptor, property)

def test_failurelogic_state_has_isInitialState():
    assert hasattr(failureLogic_State, "isInitialState")
    descriptor = None
    for klass in failureLogic_State.__mro__:
        if "isInitialState" in klass.__dict__:
            descriptor = klass.__dict__["isInitialState"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_minimalcutset_is_not_abstract():
    assert not inspect.isabstract(failureLogic_MinimalCutset)


def test_failurelogic_minimalcutset_constructor_exists():
    assert callable(failureLogic_MinimalCutset.__init__)


def test_failurelogic_minimalcutset_constructor_args():
    sig = inspect.signature(failureLogic_MinimalCutset.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_probdist_is_not_abstract():
    assert not inspect.isabstract(failureLogic_ProbDist)


def test_failurelogic_probdist_constructor_exists():
    assert callable(failureLogic_ProbDist.__init__)


def test_failurelogic_probdist_constructor_args():
    sig = inspect.signature(failureLogic_ProbDist.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_failurelogic_probdist_has_type():
    assert hasattr(failureLogic_ProbDist, "type")
    descriptor = None
    for klass in failureLogic_ProbDist.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_fmeaentry_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FMEAEntry)


def test_failurelogic_fmeaentry_constructor_exists():
    assert callable(failureLogic_FMEAEntry.__init__)


def test_failurelogic_fmeaentry_constructor_args():
    sig = inspect.signature(failureLogic_FMEAEntry.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_cause_is_not_abstract():
    assert not inspect.isabstract(failureLogic_Cause)


def test_failurelogic_cause_constructor_exists():
    assert callable(failureLogic_Cause.__init__)


def test_failurelogic_cause_constructor_args():
    sig = inspect.signature(failureLogic_Cause.__init__)
    params = list(sig.parameters.keys())
    assert "causeType" in params, "Missing parameter 'causeType'"

def test_failurelogic_cause_has_causeType():
    assert hasattr(failureLogic_Cause, "causeType")
    descriptor = None
    for klass in failureLogic_Cause.__mro__:
        if "causeType" in klass.__dict__:
            descriptor = klass.__dict__["causeType"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_transition_is_not_abstract():
    assert not inspect.isabstract(failureLogic_Transition)


def test_failurelogic_transition_constructor_exists():
    assert callable(failureLogic_Transition.__init__)


def test_failurelogic_transition_constructor_args():
    sig = inspect.signature(failureLogic_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "transition" in params, "Missing parameter 'transition'"

def test_failurelogic_transition_has_transition():
    assert hasattr(failureLogic_Transition, "transition")
    descriptor = None
    for klass in failureLogic_Transition.__mro__:
        if "transition" in klass.__dict__:
            descriptor = klass.__dict__["transition"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_failure_is_not_abstract():
    assert not inspect.isabstract(failureLogic_Failure)


def test_failurelogic_failure_constructor_exists():
    assert callable(failureLogic_Failure.__init__)


def test_failurelogic_failure_constructor_args():
    sig = inspect.signature(failureLogic_Failure.__init__)
    params = list(sig.parameters.keys())
    assert "failureRate" in params, "Missing parameter 'failureRate'"
    assert "originType" in params, "Missing parameter 'originType'"
    assert "isCcf" in params, "Missing parameter 'isCcf'"
    assert "failureClass" in params, "Missing parameter 'failureClass'"

def test_failurelogic_failure_has_failureRate():
    assert hasattr(failureLogic_Failure, "failureRate")
    descriptor = None
    for klass in failureLogic_Failure.__mro__:
        if "failureRate" in klass.__dict__:
            descriptor = klass.__dict__["failureRate"]
            break
    assert isinstance(descriptor, property)

def test_failurelogic_failure_has_originType():
    assert hasattr(failureLogic_Failure, "originType")
    descriptor = None
    for klass in failureLogic_Failure.__mro__:
        if "originType" in klass.__dict__:
            descriptor = klass.__dict__["originType"]
            break
    assert isinstance(descriptor, property)

def test_failurelogic_failure_has_isCcf():
    assert hasattr(failureLogic_Failure, "isCcf")
    descriptor = None
    for klass in failureLogic_Failure.__mro__:
        if "isCcf" in klass.__dict__:
            descriptor = klass.__dict__["isCcf"]
            break
    assert isinstance(descriptor, property)

def test_failurelogic_failure_has_failureClass():
    assert hasattr(failureLogic_Failure, "failureClass")
    descriptor = None
    for klass in failureLogic_Failure.__mro__:
        if "failureClass" in klass.__dict__:
            descriptor = klass.__dict__["failureClass"]
            break
    assert isinstance(descriptor, property)



def test_failurelogic_failuremodel_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FailureModel)


def test_failurelogic_failuremodel_constructor_exists():
    assert callable(failureLogic_FailureModel.__init__)


def test_failurelogic_failuremodel_constructor_args():
    sig = inspect.signature(failureLogic_FailureModel.__init__)
    params = list(sig.parameters.keys())



def test_odeproductpackage_is_not_abstract():
    assert not inspect.isabstract(ODEProductPackage)


def test_odeproductpackage_constructor_exists():
    assert callable(ODEProductPackage.__init__)


def test_odeproductpackage_constructor_args():
    sig = inspect.signature(ODEProductPackage.__init__)
    params = list(sig.parameters.keys())



def test_failurelogic_failurelogicpackage_is_not_abstract():
    assert not inspect.isabstract(failureLogic_FailureLogicPackage)


def test_failurelogic_failurelogicpackage_constructor_exists():
    assert callable(failureLogic_FailureLogicPackage.__init__)


def test_failurelogic_failurelogicpackage_constructor_args():
    sig = inspect.signature(failureLogic_FailureLogicPackage.__init__)
    params = list(sig.parameters.keys())

def test_causetype_exists():
    # Check that the Enumeration exists
    assert CauseType is not None

def test_causetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CauseType]
    expected_literals = [
        "InputEvent",
        "Gate",
        "OutputEvent",
        "BasicEvent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CauseType"

def test_failureorigintype_exists():
    # Check that the Enumeration exists
    assert FailureOriginType is not None

def test_failureorigintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FailureOriginType]
    expected_literals = [
        "Input",
        "Output",
        "Internal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FailureOriginType"

def test_gatetype_exists():
    # Check that the Enumeration exists
    assert GateType is not None

def test_gatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GateType]
    expected_literals = [
        "InputEvent",
        "POR",
        "AND",
        "VOTE",
        "OutputEvent",
        "PAND",
        "SAND",
        "NOT",
        "XOR",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GateType"

def test_fmeatype_exists():
    # Check that the Enumeration exists
    assert FMEAType is not None

def test_fmeatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FMEAType]
    expected_literals = [
        "FMEA",
        "FMEDA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FMEAType"


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
FMEAEntry_strategy = st.builds(
    FMEAEntry,
)
failureLogic_FMEDAEntry_strategy = st.builds(
    failureLogic_FMEDAEntry,
    diagnosisRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Cause_strategy = st.builds(
    Cause,
)
failureLogic_Gate_strategy = st.builds(
    failureLogic_Gate,
    gateType=
        safe_text
)
FailureModel_strategy = st.builds(
    FailureModel,
)
failureLogic_MarkovChain_strategy = st.builds(
    failureLogic_MarkovChain,
)
failureLogic_FMEA_strategy = st.builds(
    failureLogic_FMEA,
    type=
        safe_text
)
failureLogic_FaultTree_strategy = st.builds(
    failureLogic_FaultTree,
)
Failure_strategy = st.builds(
    Failure,
)
failureLogic_SecurityViolation_strategy = st.builds(
    failureLogic_SecurityViolation,
)
BaseElement_strategy = st.builds(
    BaseElement,
)
failureLogic_ProbDistParam_strategy = st.builds(
    failureLogic_ProbDistParam,
    value=
        safe_text
)
failureLogic_MinimalCutSets_strategy = st.builds(
    failureLogic_MinimalCutSets,
)
failureLogic_State_strategy = st.builds(
    failureLogic_State,
    isFailState=
        st.booleans(),
    isInitialState=
        st.booleans()
)
failureLogic_MinimalCutset_strategy = st.builds(
    failureLogic_MinimalCutset,
)
failureLogic_ProbDist_strategy = st.builds(
    failureLogic_ProbDist,
    type=
        safe_text
)
failureLogic_FMEAEntry_strategy = st.builds(
    failureLogic_FMEAEntry,
)
failureLogic_Cause_strategy = st.builds(
    failureLogic_Cause,
    causeType=
        safe_text
)
failureLogic_Transition_strategy = st.builds(
    failureLogic_Transition,
    transition=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
failureLogic_Failure_strategy = st.builds(
    failureLogic_Failure,
    failureRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    originType=
        safe_text,
    isCcf=
        st.booleans(),
    failureClass=
        safe_text
)
failureLogic_FailureModel_strategy = st.builds(
    failureLogic_FailureModel,
)
ODEProductPackage_strategy = st.builds(
    ODEProductPackage,
)
failureLogic_FailureLogicPackage_strategy = st.builds(
    failureLogic_FailureLogicPackage,
)

@given(instance=FMEAEntry_strategy)
@settings(max_examples=50)
def test_fmeaentry_instantiation(instance):
    assert isinstance(instance, FMEAEntry)

@given(instance=failureLogic_FMEDAEntry_strategy)
@settings(max_examples=50)
def test_failurelogic_fmedaentry_instantiation(instance):
    assert isinstance(instance, failureLogic_FMEDAEntry)



@given(instance=failureLogic_FMEDAEntry_strategy)
def test_failurelogic_fmedaentry_diagnosisRate_setter(instance):
    original = instance.diagnosisRate
    instance.diagnosisRate = original
    assert instance.diagnosisRate == original

@given(instance=Cause_strategy)
@settings(max_examples=50)
def test_cause_instantiation(instance):
    assert isinstance(instance, Cause)

@given(instance=failureLogic_Gate_strategy)
@settings(max_examples=50)
def test_failurelogic_gate_instantiation(instance):
    assert isinstance(instance, failureLogic_Gate)



@given(instance=failureLogic_Gate_strategy)
def test_failurelogic_gate_gateType_setter(instance):
    original = instance.gateType
    instance.gateType = original
    assert instance.gateType == original

@given(instance=FailureModel_strategy)
@settings(max_examples=50)
def test_failuremodel_instantiation(instance):
    assert isinstance(instance, FailureModel)

@given(instance=failureLogic_MarkovChain_strategy)
@settings(max_examples=50)
def test_failurelogic_markovchain_instantiation(instance):
    assert isinstance(instance, failureLogic_MarkovChain)

@given(instance=failureLogic_FMEA_strategy)
@settings(max_examples=50)
def test_failurelogic_fmea_instantiation(instance):
    assert isinstance(instance, failureLogic_FMEA)



@given(instance=failureLogic_FMEA_strategy)
def test_failurelogic_fmea_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=failureLogic_FaultTree_strategy)
@settings(max_examples=50)
def test_failurelogic_faulttree_instantiation(instance):
    assert isinstance(instance, failureLogic_FaultTree)

@given(instance=Failure_strategy)
@settings(max_examples=50)
def test_failure_instantiation(instance):
    assert isinstance(instance, Failure)

@given(instance=failureLogic_SecurityViolation_strategy)
@settings(max_examples=50)
def test_failurelogic_securityviolation_instantiation(instance):
    assert isinstance(instance, failureLogic_SecurityViolation)

@given(instance=BaseElement_strategy)
@settings(max_examples=50)
def test_baseelement_instantiation(instance):
    assert isinstance(instance, BaseElement)

@given(instance=failureLogic_ProbDistParam_strategy)
@settings(max_examples=50)
def test_failurelogic_probdistparam_instantiation(instance):
    assert isinstance(instance, failureLogic_ProbDistParam)



@given(instance=failureLogic_ProbDistParam_strategy)
def test_failurelogic_probdistparam_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=failureLogic_MinimalCutSets_strategy)
@settings(max_examples=50)
def test_failurelogic_minimalcutsets_instantiation(instance):
    assert isinstance(instance, failureLogic_MinimalCutSets)

@given(instance=failureLogic_State_strategy)
@settings(max_examples=50)
def test_failurelogic_state_instantiation(instance):
    assert isinstance(instance, failureLogic_State)



@given(instance=failureLogic_State_strategy)
def test_failurelogic_state_isFailState_setter(instance):
    original = instance.isFailState
    instance.isFailState = original
    assert instance.isFailState == original



@given(instance=failureLogic_State_strategy)
def test_failurelogic_state_isInitialState_setter(instance):
    original = instance.isInitialState
    instance.isInitialState = original
    assert instance.isInitialState == original

@given(instance=failureLogic_MinimalCutset_strategy)
@settings(max_examples=50)
def test_failurelogic_minimalcutset_instantiation(instance):
    assert isinstance(instance, failureLogic_MinimalCutset)

@given(instance=failureLogic_ProbDist_strategy)
@settings(max_examples=50)
def test_failurelogic_probdist_instantiation(instance):
    assert isinstance(instance, failureLogic_ProbDist)



@given(instance=failureLogic_ProbDist_strategy)
def test_failurelogic_probdist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=failureLogic_FMEAEntry_strategy)
@settings(max_examples=50)
def test_failurelogic_fmeaentry_instantiation(instance):
    assert isinstance(instance, failureLogic_FMEAEntry)

@given(instance=failureLogic_Cause_strategy)
@settings(max_examples=50)
def test_failurelogic_cause_instantiation(instance):
    assert isinstance(instance, failureLogic_Cause)



@given(instance=failureLogic_Cause_strategy)
def test_failurelogic_cause_causeType_setter(instance):
    original = instance.causeType
    instance.causeType = original
    assert instance.causeType == original

@given(instance=failureLogic_Transition_strategy)
@settings(max_examples=50)
def test_failurelogic_transition_instantiation(instance):
    assert isinstance(instance, failureLogic_Transition)



@given(instance=failureLogic_Transition_strategy)
def test_failurelogic_transition_transition_setter(instance):
    original = instance.transition
    instance.transition = original
    assert instance.transition == original

@given(instance=failureLogic_Failure_strategy)
@settings(max_examples=50)
def test_failurelogic_failure_instantiation(instance):
    assert isinstance(instance, failureLogic_Failure)



@given(instance=failureLogic_Failure_strategy)
def test_failurelogic_failure_failureRate_setter(instance):
    original = instance.failureRate
    instance.failureRate = original
    assert instance.failureRate == original



@given(instance=failureLogic_Failure_strategy)
def test_failurelogic_failure_originType_setter(instance):
    original = instance.originType
    instance.originType = original
    assert instance.originType == original



@given(instance=failureLogic_Failure_strategy)
def test_failurelogic_failure_isCcf_setter(instance):
    original = instance.isCcf
    instance.isCcf = original
    assert instance.isCcf == original



@given(instance=failureLogic_Failure_strategy)
def test_failurelogic_failure_failureClass_setter(instance):
    original = instance.failureClass
    instance.failureClass = original
    assert instance.failureClass == original

@given(instance=failureLogic_FailureModel_strategy)
@settings(max_examples=50)
def test_failurelogic_failuremodel_instantiation(instance):
    assert isinstance(instance, failureLogic_FailureModel)

@given(instance=ODEProductPackage_strategy)
@settings(max_examples=50)
def test_odeproductpackage_instantiation(instance):
    assert isinstance(instance, ODEProductPackage)

@given(instance=failureLogic_FailureLogicPackage_strategy)
@settings(max_examples=50)
def test_failurelogic_failurelogicpackage_instantiation(instance):
    assert isinstance(instance, failureLogic_FailureLogicPackage)

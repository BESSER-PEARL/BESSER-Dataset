import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    interaction::ValueSpecification,
    CapellaElement,
    AbstractFunctionalChainContainer,
    Structure,
    interaction::AbstractCapability,
    interaction::ExchangeItemElement,
    interaction::FunctionalChain,
    interaction::State,
    interaction::ExchangeItem,
    interaction::AbstractEventOperation,
    interaction::Constraint,
    NamedElement,
    interaction::CombinedFragment,
    interaction::InteractionOperand,
    interaction::SequenceMessage,
    AbstractBehavior,
    Namespace,
    interaction::Scenario,
    interaction::SequenceMessageValuation,
    interaction::AbstractFunction,
    interaction::Part,
    ScenarioKind,
    InteractionOperatorKind,
    MessageKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_interaction::valuespecification_is_not_abstract():
    assert not inspect.isabstract(interaction::ValueSpecification)


def test_interaction::valuespecification_constructor_exists():
    assert callable(interaction::ValueSpecification.__init__)


def test_interaction::valuespecification_constructor_args():
    sig = inspect.signature(interaction::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_capellaelement_is_not_abstract():
    assert not inspect.isabstract(CapellaElement)


def test_capellaelement_constructor_exists():
    assert callable(CapellaElement.__init__)


def test_capellaelement_constructor_args():
    sig = inspect.signature(CapellaElement.__init__)
    params = list(sig.parameters.keys())



def test_abstractfunctionalchaincontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractFunctionalChainContainer)


def test_abstractfunctionalchaincontainer_constructor_exists():
    assert callable(AbstractFunctionalChainContainer.__init__)


def test_abstractfunctionalchaincontainer_constructor_args():
    sig = inspect.signature(AbstractFunctionalChainContainer.__init__)
    params = list(sig.parameters.keys())



def test_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_interaction::abstractcapability_is_not_abstract():
    assert not inspect.isabstract(interaction::AbstractCapability)


def test_interaction::abstractcapability_constructor_exists():
    assert callable(interaction::AbstractCapability.__init__)


def test_interaction::abstractcapability_constructor_args():
    sig = inspect.signature(interaction::AbstractCapability.__init__)
    params = list(sig.parameters.keys())



def test_interaction::exchangeitemelement_is_not_abstract():
    assert not inspect.isabstract(interaction::ExchangeItemElement)


def test_interaction::exchangeitemelement_constructor_exists():
    assert callable(interaction::ExchangeItemElement.__init__)


def test_interaction::exchangeitemelement_constructor_args():
    sig = inspect.signature(interaction::ExchangeItemElement.__init__)
    params = list(sig.parameters.keys())



def test_interaction::functionalchain_is_not_abstract():
    assert not inspect.isabstract(interaction::FunctionalChain)


def test_interaction::functionalchain_constructor_exists():
    assert callable(interaction::FunctionalChain.__init__)


def test_interaction::functionalchain_constructor_args():
    sig = inspect.signature(interaction::FunctionalChain.__init__)
    params = list(sig.parameters.keys())



def test_interaction::state_is_not_abstract():
    assert not inspect.isabstract(interaction::State)


def test_interaction::state_constructor_exists():
    assert callable(interaction::State.__init__)


def test_interaction::state_constructor_args():
    sig = inspect.signature(interaction::State.__init__)
    params = list(sig.parameters.keys())



def test_interaction::exchangeitem_is_not_abstract():
    assert not inspect.isabstract(interaction::ExchangeItem)


def test_interaction::exchangeitem_constructor_exists():
    assert callable(interaction::ExchangeItem.__init__)


def test_interaction::exchangeitem_constructor_args():
    sig = inspect.signature(interaction::ExchangeItem.__init__)
    params = list(sig.parameters.keys())



def test_interaction::abstracteventoperation_is_not_abstract():
    assert not inspect.isabstract(interaction::AbstractEventOperation)


def test_interaction::abstracteventoperation_constructor_exists():
    assert callable(interaction::AbstractEventOperation.__init__)


def test_interaction::abstracteventoperation_constructor_args():
    sig = inspect.signature(interaction::AbstractEventOperation.__init__)
    params = list(sig.parameters.keys())



def test_interaction::constraint_is_not_abstract():
    assert not inspect.isabstract(interaction::Constraint)


def test_interaction::constraint_constructor_exists():
    assert callable(interaction::Constraint.__init__)


def test_interaction::constraint_constructor_args():
    sig = inspect.signature(interaction::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_interaction::combinedfragment_is_not_abstract():
    assert not inspect.isabstract(interaction::CombinedFragment)


def test_interaction::combinedfragment_constructor_exists():
    assert callable(interaction::CombinedFragment.__init__)


def test_interaction::combinedfragment_constructor_args():
    sig = inspect.signature(interaction::CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_interaction::combinedfragment_has_operator():
    assert hasattr(interaction::CombinedFragment, "operator")
    descriptor = None
    for klass in interaction::CombinedFragment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_interaction::interactionoperand_is_not_abstract():
    assert not inspect.isabstract(interaction::InteractionOperand)


def test_interaction::interactionoperand_constructor_exists():
    assert callable(interaction::InteractionOperand.__init__)


def test_interaction::interactionoperand_constructor_args():
    sig = inspect.signature(interaction::InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_interaction::sequencemessage_is_not_abstract():
    assert not inspect.isabstract(interaction::SequenceMessage)


def test_interaction::sequencemessage_constructor_exists():
    assert callable(interaction::SequenceMessage.__init__)


def test_interaction::sequencemessage_constructor_args():
    sig = inspect.signature(interaction::SequenceMessage.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_interaction::sequencemessage_has_kind():
    assert hasattr(interaction::SequenceMessage, "kind")
    descriptor = None
    for klass in interaction::SequenceMessage.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_abstractbehavior_is_not_abstract():
    assert not inspect.isabstract(AbstractBehavior)


def test_abstractbehavior_constructor_exists():
    assert callable(AbstractBehavior.__init__)


def test_abstractbehavior_constructor_args():
    sig = inspect.signature(AbstractBehavior.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_interaction::scenario_is_not_abstract():
    assert not inspect.isabstract(interaction::Scenario)


def test_interaction::scenario_constructor_exists():
    assert callable(interaction::Scenario.__init__)


def test_interaction::scenario_constructor_args():
    sig = inspect.signature(interaction::Scenario.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "merged" in params, "Missing parameter 'merged'"

def test_interaction::scenario_has_kind():
    assert hasattr(interaction::Scenario, "kind")
    descriptor = None
    for klass in interaction::Scenario.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_interaction::scenario_has_merged():
    assert hasattr(interaction::Scenario, "merged")
    descriptor = None
    for klass in interaction::Scenario.__mro__:
        if "merged" in klass.__dict__:
            descriptor = klass.__dict__["merged"]
            break
    assert isinstance(descriptor, property)



def test_interaction::sequencemessagevaluation_is_not_abstract():
    assert not inspect.isabstract(interaction::SequenceMessageValuation)


def test_interaction::sequencemessagevaluation_constructor_exists():
    assert callable(interaction::SequenceMessageValuation.__init__)


def test_interaction::sequencemessagevaluation_constructor_args():
    sig = inspect.signature(interaction::SequenceMessageValuation.__init__)
    params = list(sig.parameters.keys())



def test_interaction::abstractfunction_is_not_abstract():
    assert not inspect.isabstract(interaction::AbstractFunction)


def test_interaction::abstractfunction_constructor_exists():
    assert callable(interaction::AbstractFunction.__init__)


def test_interaction::abstractfunction_constructor_args():
    sig = inspect.signature(interaction::AbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_interaction::part_is_not_abstract():
    assert not inspect.isabstract(interaction::Part)


def test_interaction::part_constructor_exists():
    assert callable(interaction::Part.__init__)


def test_interaction::part_constructor_args():
    sig = inspect.signature(interaction::Part.__init__)
    params = list(sig.parameters.keys())

def test_scenariokind_exists():
    # Check that the Enumeration exists
    assert ScenarioKind is not None

def test_scenariokind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScenarioKind]
    expected_literals = [
        "DATA_FLOW",
        "INTERFACE",
        "UNSET",
        "FUNCTIONAL",
        "INTERACTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScenarioKind"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "UNSET",
        "LOOP",
        "ASSERT",
        "IGNORE",
        "CRITICAL",
        "SEQ",
        "CONSIDER",
        "PAR",
        "NEG",
        "OPT",
        "ALT",
        "STRICT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "UNSET",
        "REPLY",
        "TIMER",
        "CREATE",
        "SYNCHRONOUS_CALL",
        "DELETE",
        "ASYNCHRONOUS_CALL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"


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
interaction::ValueSpecification_strategy = st.builds(
    interaction::ValueSpecification,
)
CapellaElement_strategy = st.builds(
    CapellaElement,
)
AbstractFunctionalChainContainer_strategy = st.builds(
    AbstractFunctionalChainContainer,
)
Structure_strategy = st.builds(
    Structure,
)
interaction::AbstractCapability_strategy = st.builds(
    interaction::AbstractCapability,
)
interaction::ExchangeItemElement_strategy = st.builds(
    interaction::ExchangeItemElement,
)
interaction::FunctionalChain_strategy = st.builds(
    interaction::FunctionalChain,
)
interaction::State_strategy = st.builds(
    interaction::State,
)
interaction::ExchangeItem_strategy = st.builds(
    interaction::ExchangeItem,
)
interaction::AbstractEventOperation_strategy = st.builds(
    interaction::AbstractEventOperation,
)
interaction::Constraint_strategy = st.builds(
    interaction::Constraint,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
interaction::CombinedFragment_strategy = st.builds(
    interaction::CombinedFragment,
    operator=
        safe_text
)
interaction::InteractionOperand_strategy = st.builds(
    interaction::InteractionOperand,
)
interaction::SequenceMessage_strategy = st.builds(
    interaction::SequenceMessage,
    kind=
        safe_text
)
AbstractBehavior_strategy = st.builds(
    AbstractBehavior,
)
Namespace_strategy = st.builds(
    Namespace,
)
interaction::Scenario_strategy = st.builds(
    interaction::Scenario,
    kind=
        safe_text,
    merged=
        st.booleans()
)
interaction::SequenceMessageValuation_strategy = st.builds(
    interaction::SequenceMessageValuation,
)
interaction::AbstractFunction_strategy = st.builds(
    interaction::AbstractFunction,
)
interaction::Part_strategy = st.builds(
    interaction::Part,
)

@given(instance=interaction::ValueSpecification_strategy)
@settings(max_examples=50)
def test_interaction::valuespecification_instantiation(instance):
    assert isinstance(instance, interaction::ValueSpecification)

@given(instance=CapellaElement_strategy)
@settings(max_examples=50)
def test_capellaelement_instantiation(instance):
    assert isinstance(instance, CapellaElement)

@given(instance=AbstractFunctionalChainContainer_strategy)
@settings(max_examples=50)
def test_abstractfunctionalchaincontainer_instantiation(instance):
    assert isinstance(instance, AbstractFunctionalChainContainer)

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=interaction::AbstractCapability_strategy)
@settings(max_examples=50)
def test_interaction::abstractcapability_instantiation(instance):
    assert isinstance(instance, interaction::AbstractCapability)

@given(instance=interaction::ExchangeItemElement_strategy)
@settings(max_examples=50)
def test_interaction::exchangeitemelement_instantiation(instance):
    assert isinstance(instance, interaction::ExchangeItemElement)

@given(instance=interaction::FunctionalChain_strategy)
@settings(max_examples=50)
def test_interaction::functionalchain_instantiation(instance):
    assert isinstance(instance, interaction::FunctionalChain)

@given(instance=interaction::State_strategy)
@settings(max_examples=50)
def test_interaction::state_instantiation(instance):
    assert isinstance(instance, interaction::State)

@given(instance=interaction::ExchangeItem_strategy)
@settings(max_examples=50)
def test_interaction::exchangeitem_instantiation(instance):
    assert isinstance(instance, interaction::ExchangeItem)

@given(instance=interaction::AbstractEventOperation_strategy)
@settings(max_examples=50)
def test_interaction::abstracteventoperation_instantiation(instance):
    assert isinstance(instance, interaction::AbstractEventOperation)

@given(instance=interaction::Constraint_strategy)
@settings(max_examples=50)
def test_interaction::constraint_instantiation(instance):
    assert isinstance(instance, interaction::Constraint)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=interaction::CombinedFragment_strategy)
@settings(max_examples=50)
def test_interaction::combinedfragment_instantiation(instance):
    assert isinstance(instance, interaction::CombinedFragment)

@given(instance=interaction::CombinedFragment_strategy)
def test_interaction::combinedfragment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=interaction::CombinedFragment_strategy)
def test_interaction::combinedfragment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=interaction::InteractionOperand_strategy)
@settings(max_examples=50)
def test_interaction::interactionoperand_instantiation(instance):
    assert isinstance(instance, interaction::InteractionOperand)

@given(instance=interaction::SequenceMessage_strategy)
@settings(max_examples=50)
def test_interaction::sequencemessage_instantiation(instance):
    assert isinstance(instance, interaction::SequenceMessage)

@given(instance=interaction::SequenceMessage_strategy)
def test_interaction::sequencemessage_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=interaction::SequenceMessage_strategy)
def test_interaction::sequencemessage_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=AbstractBehavior_strategy)
@settings(max_examples=50)
def test_abstractbehavior_instantiation(instance):
    assert isinstance(instance, AbstractBehavior)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=interaction::Scenario_strategy)
@settings(max_examples=50)
def test_interaction::scenario_instantiation(instance):
    assert isinstance(instance, interaction::Scenario)

@given(instance=interaction::Scenario_strategy)
def test_interaction::scenario_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=interaction::Scenario_strategy)
def test_interaction::scenario_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=interaction::Scenario_strategy)
def test_interaction::scenario_merged_type(instance):
    assert isinstance(instance.merged, bool)


@given(instance=interaction::Scenario_strategy)
def test_interaction::scenario_merged_setter(instance):
    original = instance.merged
    instance.merged = original
    assert instance.merged == original

@given(instance=interaction::SequenceMessageValuation_strategy)
@settings(max_examples=50)
def test_interaction::sequencemessagevaluation_instantiation(instance):
    assert isinstance(instance, interaction::SequenceMessageValuation)

@given(instance=interaction::AbstractFunction_strategy)
@settings(max_examples=50)
def test_interaction::abstractfunction_instantiation(instance):
    assert isinstance(instance, interaction::AbstractFunction)

@given(instance=interaction::Part_strategy)
@settings(max_examples=50)
def test_interaction::part_instantiation(instance):
    assert isinstance(instance, interaction::Part)

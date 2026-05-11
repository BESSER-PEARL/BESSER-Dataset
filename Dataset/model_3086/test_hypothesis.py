import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Pin,
    ObjectNode,
    activity::Pin,
    activity::AbstractBehavior,
    activity::IState,
    AbstractAction,
    activity::AcceptEventAction,
    activity::OutputPin,
    activity::InputPin,
    ActivityNode,
    AbstractNamedElement,
    activity::AbstractAction,
    activity::ObjectNode,
    ActivityEdge,
    activity::ObjectFlow,
    activity::ActivityNode,
    activity::ValueSpecification,
    ModelElement,
    activity::ActivityPartition,
    activity::ActivityEdge,
    TraceableElement,
    AbstractBehavior,
    activity::AbstractActivity,
    ObjectNodeKind,
    ObjectNodeOrderingKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activity::pin_is_not_abstract():
    assert not inspect.isabstract(activity::Pin)


def test_activity::pin_constructor_exists():
    assert callable(activity::Pin.__init__)


def test_activity::pin_constructor_args():
    sig = inspect.signature(activity::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_activity::pin_has_isControl():
    assert hasattr(activity::Pin, "isControl")
    descriptor = None
    for klass in activity::Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_activity::abstractbehavior_is_not_abstract():
    assert not inspect.isabstract(activity::AbstractBehavior)


def test_activity::abstractbehavior_constructor_exists():
    assert callable(activity::AbstractBehavior.__init__)


def test_activity::abstractbehavior_constructor_args():
    sig = inspect.signature(activity::AbstractBehavior.__init__)
    params = list(sig.parameters.keys())



def test_activity::istate_is_not_abstract():
    assert not inspect.isabstract(activity::IState)


def test_activity::istate_constructor_exists():
    assert callable(activity::IState.__init__)


def test_activity::istate_constructor_args():
    sig = inspect.signature(activity::IState.__init__)
    params = list(sig.parameters.keys())



def test_abstractaction_is_not_abstract():
    assert not inspect.isabstract(AbstractAction)


def test_abstractaction_constructor_exists():
    assert callable(AbstractAction.__init__)


def test_abstractaction_constructor_args():
    sig = inspect.signature(AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_activity::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(activity::AcceptEventAction)


def test_activity::accepteventaction_constructor_exists():
    assert callable(activity::AcceptEventAction.__init__)


def test_activity::accepteventaction_constructor_args():
    sig = inspect.signature(activity::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_activity::accepteventaction_has_isUnmarshall():
    assert hasattr(activity::AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in activity::AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_activity::outputpin_is_not_abstract():
    assert not inspect.isabstract(activity::OutputPin)


def test_activity::outputpin_constructor_exists():
    assert callable(activity::OutputPin.__init__)


def test_activity::outputpin_constructor_args():
    sig = inspect.signature(activity::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_activity::inputpin_is_not_abstract():
    assert not inspect.isabstract(activity::InputPin)


def test_activity::inputpin_constructor_exists():
    assert callable(activity::InputPin.__init__)


def test_activity::inputpin_constructor_args():
    sig = inspect.signature(activity::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_abstractnamedelement_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedElement)


def test_abstractnamedelement_constructor_exists():
    assert callable(AbstractNamedElement.__init__)


def test_abstractnamedelement_constructor_args():
    sig = inspect.signature(AbstractNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_activity::abstractaction_is_not_abstract():
    assert not inspect.isabstract(activity::AbstractAction)


def test_activity::abstractaction_constructor_exists():
    assert callable(activity::AbstractAction.__init__)


def test_activity::abstractaction_constructor_args():
    sig = inspect.signature(activity::AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_activity::objectnode_is_not_abstract():
    assert not inspect.isabstract(activity::ObjectNode)


def test_activity::objectnode_constructor_exists():
    assert callable(activity::ObjectNode.__init__)


def test_activity::objectnode_constructor_args():
    sig = inspect.signature(activity::ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "kindOfNode" in params, "Missing parameter 'kindOfNode'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_activity::objectnode_has_kindOfNode():
    assert hasattr(activity::ObjectNode, "kindOfNode")
    descriptor = None
    for klass in activity::ObjectNode.__mro__:
        if "kindOfNode" in klass.__dict__:
            descriptor = klass.__dict__["kindOfNode"]
            break
    assert isinstance(descriptor, property)

def test_activity::objectnode_has_isControlType():
    assert hasattr(activity::ObjectNode, "isControlType")
    descriptor = None
    for klass in activity::ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_activity::objectnode_has_ordering():
    assert hasattr(activity::ObjectNode, "ordering")
    descriptor = None
    for klass in activity::ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activity::objectflow_is_not_abstract():
    assert not inspect.isabstract(activity::ObjectFlow)


def test_activity::objectflow_constructor_exists():
    assert callable(activity::ObjectFlow.__init__)


def test_activity::objectflow_constructor_args():
    sig = inspect.signature(activity::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"

def test_activity::objectflow_has_isMultireceive():
    assert hasattr(activity::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in activity::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_activity::objectflow_has_isMulticast():
    assert hasattr(activity::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in activity::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)



def test_activity::activitynode_is_not_abstract():
    assert not inspect.isabstract(activity::ActivityNode)


def test_activity::activitynode_constructor_exists():
    assert callable(activity::ActivityNode.__init__)


def test_activity::activitynode_constructor_args():
    sig = inspect.signature(activity::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activity::valuespecification_is_not_abstract():
    assert not inspect.isabstract(activity::ValueSpecification)


def test_activity::valuespecification_constructor_exists():
    assert callable(activity::ValueSpecification.__init__)


def test_activity::valuespecification_constructor_args():
    sig = inspect.signature(activity::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_activity::activitypartition_is_not_abstract():
    assert not inspect.isabstract(activity::ActivityPartition)


def test_activity::activitypartition_constructor_exists():
    assert callable(activity::ActivityPartition.__init__)


def test_activity::activitypartition_constructor_args():
    sig = inspect.signature(activity::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_activity::activitypartition_has_isDimension():
    assert hasattr(activity::ActivityPartition, "isDimension")
    descriptor = None
    for klass in activity::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_activity::activitypartition_has_isExternal():
    assert hasattr(activity::ActivityPartition, "isExternal")
    descriptor = None
    for klass in activity::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_activity::activityedge_is_not_abstract():
    assert not inspect.isabstract(activity::ActivityEdge)


def test_activity::activityedge_constructor_exists():
    assert callable(activity::ActivityEdge.__init__)


def test_activity::activityedge_constructor_args():
    sig = inspect.signature(activity::ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "kindOfRate" in params, "Missing parameter 'kindOfRate'"

def test_activity::activityedge_has_kindOfRate():
    assert hasattr(activity::ActivityEdge, "kindOfRate")
    descriptor = None
    for klass in activity::ActivityEdge.__mro__:
        if "kindOfRate" in klass.__dict__:
            descriptor = klass.__dict__["kindOfRate"]
            break
    assert isinstance(descriptor, property)



def test_traceableelement_is_not_abstract():
    assert not inspect.isabstract(TraceableElement)


def test_traceableelement_constructor_exists():
    assert callable(TraceableElement.__init__)


def test_traceableelement_constructor_args():
    sig = inspect.signature(TraceableElement.__init__)
    params = list(sig.parameters.keys())



def test_abstractbehavior_is_not_abstract():
    assert not inspect.isabstract(AbstractBehavior)


def test_abstractbehavior_constructor_exists():
    assert callable(AbstractBehavior.__init__)


def test_abstractbehavior_constructor_args():
    sig = inspect.signature(AbstractBehavior.__init__)
    params = list(sig.parameters.keys())



def test_activity::abstractactivity_is_not_abstract():
    assert not inspect.isabstract(activity::AbstractActivity)


def test_activity::abstractactivity_constructor_exists():
    assert callable(activity::AbstractActivity.__init__)


def test_activity::abstractactivity_constructor_args():
    sig = inspect.signature(activity::AbstractActivity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_activity::abstractactivity_has_isSingleExecution():
    assert hasattr(activity::AbstractActivity, "isSingleExecution")
    descriptor = None
    for klass in activity::AbstractActivity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_activity::abstractactivity_has_isReadOnly():
    assert hasattr(activity::AbstractActivity, "isReadOnly")
    descriptor = None
    for klass in activity::AbstractActivity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_objectnodekind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeKind is not None

def test_objectnodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeKind]
    expected_literals = [
        "Unspecified",
        "Overwrite",
        "NoBuffer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "ordered",
        "unordered",
        "FIFO",
        "LIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"


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
Pin_strategy = st.builds(
    Pin,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
activity::Pin_strategy = st.builds(
    activity::Pin,
    isControl=
        st.booleans()
)
activity::AbstractBehavior_strategy = st.builds(
    activity::AbstractBehavior,
)
activity::IState_strategy = st.builds(
    activity::IState,
)
AbstractAction_strategy = st.builds(
    AbstractAction,
)
activity::AcceptEventAction_strategy = st.builds(
    activity::AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
activity::OutputPin_strategy = st.builds(
    activity::OutputPin,
)
activity::InputPin_strategy = st.builds(
    activity::InputPin,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
AbstractNamedElement_strategy = st.builds(
    AbstractNamedElement,
)
activity::AbstractAction_strategy = st.builds(
    activity::AbstractAction,
)
activity::ObjectNode_strategy = st.builds(
    activity::ObjectNode,
    kindOfNode=
        safe_text,
    isControlType=
        st.booleans(),
    ordering=
        safe_text
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
activity::ObjectFlow_strategy = st.builds(
    activity::ObjectFlow,
    isMultireceive=
        st.booleans(),
    isMulticast=
        st.booleans()
)
activity::ActivityNode_strategy = st.builds(
    activity::ActivityNode,
)
activity::ValueSpecification_strategy = st.builds(
    activity::ValueSpecification,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
activity::ActivityPartition_strategy = st.builds(
    activity::ActivityPartition,
    isDimension=
        st.booleans(),
    isExternal=
        st.booleans()
)
activity::ActivityEdge_strategy = st.builds(
    activity::ActivityEdge,
    kindOfRate=
        safe_text
)
TraceableElement_strategy = st.builds(
    TraceableElement,
)
AbstractBehavior_strategy = st.builds(
    AbstractBehavior,
)
activity::AbstractActivity_strategy = st.builds(
    activity::AbstractActivity,
    isSingleExecution=
        st.booleans(),
    isReadOnly=
        st.booleans()
)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=activity::Pin_strategy)
@settings(max_examples=50)
def test_activity::pin_instantiation(instance):
    assert isinstance(instance, activity::Pin)

@given(instance=activity::Pin_strategy)
def test_activity::pin_isControl_type(instance):
    assert isinstance(instance.isControl, bool)


@given(instance=activity::Pin_strategy)
def test_activity::pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=activity::AbstractBehavior_strategy)
@settings(max_examples=50)
def test_activity::abstractbehavior_instantiation(instance):
    assert isinstance(instance, activity::AbstractBehavior)

@given(instance=activity::IState_strategy)
@settings(max_examples=50)
def test_activity::istate_instantiation(instance):
    assert isinstance(instance, activity::IState)

@given(instance=AbstractAction_strategy)
@settings(max_examples=50)
def test_abstractaction_instantiation(instance):
    assert isinstance(instance, AbstractAction)

@given(instance=activity::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_activity::accepteventaction_instantiation(instance):
    assert isinstance(instance, activity::AcceptEventAction)

@given(instance=activity::AcceptEventAction_strategy)
def test_activity::accepteventaction_isUnmarshall_type(instance):
    assert isinstance(instance.isUnmarshall, bool)


@given(instance=activity::AcceptEventAction_strategy)
def test_activity::accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=activity::OutputPin_strategy)
@settings(max_examples=50)
def test_activity::outputpin_instantiation(instance):
    assert isinstance(instance, activity::OutputPin)

@given(instance=activity::InputPin_strategy)
@settings(max_examples=50)
def test_activity::inputpin_instantiation(instance):
    assert isinstance(instance, activity::InputPin)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=AbstractNamedElement_strategy)
@settings(max_examples=50)
def test_abstractnamedelement_instantiation(instance):
    assert isinstance(instance, AbstractNamedElement)

@given(instance=activity::AbstractAction_strategy)
@settings(max_examples=50)
def test_activity::abstractaction_instantiation(instance):
    assert isinstance(instance, activity::AbstractAction)

@given(instance=activity::ObjectNode_strategy)
@settings(max_examples=50)
def test_activity::objectnode_instantiation(instance):
    assert isinstance(instance, activity::ObjectNode)

@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_kindOfNode_type(instance):
    assert isinstance(instance.kindOfNode, str)


@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_kindOfNode_setter(instance):
    original = instance.kindOfNode
    instance.kindOfNode = original
    assert instance.kindOfNode == original

@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_isControlType_type(instance):
    assert isinstance(instance.isControlType, bool)


@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=activity::ObjectNode_strategy)
def test_activity::objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=activity::ObjectFlow_strategy)
@settings(max_examples=50)
def test_activity::objectflow_instantiation(instance):
    assert isinstance(instance, activity::ObjectFlow)

@given(instance=activity::ObjectFlow_strategy)
def test_activity::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, bool)


@given(instance=activity::ObjectFlow_strategy)
def test_activity::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=activity::ObjectFlow_strategy)
def test_activity::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, bool)


@given(instance=activity::ObjectFlow_strategy)
def test_activity::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=activity::ActivityNode_strategy)
@settings(max_examples=50)
def test_activity::activitynode_instantiation(instance):
    assert isinstance(instance, activity::ActivityNode)

@given(instance=activity::ValueSpecification_strategy)
@settings(max_examples=50)
def test_activity::valuespecification_instantiation(instance):
    assert isinstance(instance, activity::ValueSpecification)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=activity::ActivityPartition_strategy)
@settings(max_examples=50)
def test_activity::activitypartition_instantiation(instance):
    assert isinstance(instance, activity::ActivityPartition)

@given(instance=activity::ActivityPartition_strategy)
def test_activity::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, bool)


@given(instance=activity::ActivityPartition_strategy)
def test_activity::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=activity::ActivityPartition_strategy)
def test_activity::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, bool)


@given(instance=activity::ActivityPartition_strategy)
def test_activity::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=activity::ActivityEdge_strategy)
@settings(max_examples=50)
def test_activity::activityedge_instantiation(instance):
    assert isinstance(instance, activity::ActivityEdge)

@given(instance=activity::ActivityEdge_strategy)
def test_activity::activityedge_kindOfRate_type(instance):
    assert isinstance(instance.kindOfRate, str)


@given(instance=activity::ActivityEdge_strategy)
def test_activity::activityedge_kindOfRate_setter(instance):
    original = instance.kindOfRate
    instance.kindOfRate = original
    assert instance.kindOfRate == original

@given(instance=TraceableElement_strategy)
@settings(max_examples=50)
def test_traceableelement_instantiation(instance):
    assert isinstance(instance, TraceableElement)

@given(instance=AbstractBehavior_strategy)
@settings(max_examples=50)
def test_abstractbehavior_instantiation(instance):
    assert isinstance(instance, AbstractBehavior)

@given(instance=activity::AbstractActivity_strategy)
@settings(max_examples=50)
def test_activity::abstractactivity_instantiation(instance):
    assert isinstance(instance, activity::AbstractActivity)

@given(instance=activity::AbstractActivity_strategy)
def test_activity::abstractactivity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, bool)


@given(instance=activity::AbstractActivity_strategy)
def test_activity::abstractactivity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=activity::AbstractActivity_strategy)
def test_activity::abstractactivity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=activity::AbstractActivity_strategy)
def test_activity::abstractactivity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

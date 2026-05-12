import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Pin,
    ObjectNode,
    activity_Pin,
    activity_AbstractBehavior,
    activity_IState,
    AbstractAction,
    activity_AcceptEventAction,
    activity_OutputPin,
    activity_InputPin,
    ActivityNode,
    AbstractNamedElement,
    activity_ObjectNode,
    activity_AbstractAction,
    ActivityEdge,
    activity_ObjectFlow,
    activity_ActivityNode,
    activity_ValueSpecification,
    ModelElement,
    activity_ActivityPartition,
    activity_ActivityEdge,
    TraceableElement,
    AbstractBehavior,
    activity_AbstractActivity,
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



def test_activity_pin_is_not_abstract():
    assert not inspect.isabstract(activity_Pin)


def test_activity_pin_constructor_exists():
    assert callable(activity_Pin.__init__)


def test_activity_pin_constructor_args():
    sig = inspect.signature(activity_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_activity_pin_has_isControl():
    assert hasattr(activity_Pin, "isControl")
    descriptor = None
    for klass in activity_Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_activity_abstractbehavior_is_not_abstract():
    assert not inspect.isabstract(activity_AbstractBehavior)


def test_activity_abstractbehavior_constructor_exists():
    assert callable(activity_AbstractBehavior.__init__)


def test_activity_abstractbehavior_constructor_args():
    sig = inspect.signature(activity_AbstractBehavior.__init__)
    params = list(sig.parameters.keys())



def test_activity_istate_is_not_abstract():
    assert not inspect.isabstract(activity_IState)


def test_activity_istate_constructor_exists():
    assert callable(activity_IState.__init__)


def test_activity_istate_constructor_args():
    sig = inspect.signature(activity_IState.__init__)
    params = list(sig.parameters.keys())



def test_abstractaction_is_not_abstract():
    assert not inspect.isabstract(AbstractAction)


def test_abstractaction_constructor_exists():
    assert callable(AbstractAction.__init__)


def test_abstractaction_constructor_args():
    sig = inspect.signature(AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_activity_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(activity_AcceptEventAction)


def test_activity_accepteventaction_constructor_exists():
    assert callable(activity_AcceptEventAction.__init__)


def test_activity_accepteventaction_constructor_args():
    sig = inspect.signature(activity_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_activity_accepteventaction_has_isUnmarshall():
    assert hasattr(activity_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in activity_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_activity_outputpin_is_not_abstract():
    assert not inspect.isabstract(activity_OutputPin)


def test_activity_outputpin_constructor_exists():
    assert callable(activity_OutputPin.__init__)


def test_activity_outputpin_constructor_args():
    sig = inspect.signature(activity_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_activity_inputpin_is_not_abstract():
    assert not inspect.isabstract(activity_InputPin)


def test_activity_inputpin_constructor_exists():
    assert callable(activity_InputPin.__init__)


def test_activity_inputpin_constructor_args():
    sig = inspect.signature(activity_InputPin.__init__)
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



def test_activity_objectnode_is_not_abstract():
    assert not inspect.isabstract(activity_ObjectNode)


def test_activity_objectnode_constructor_exists():
    assert callable(activity_ObjectNode.__init__)


def test_activity_objectnode_constructor_args():
    sig = inspect.signature(activity_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "kindOfNode" in params, "Missing parameter 'kindOfNode'"
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"

def test_activity_objectnode_has_kindOfNode():
    assert hasattr(activity_ObjectNode, "kindOfNode")
    descriptor = None
    for klass in activity_ObjectNode.__mro__:
        if "kindOfNode" in klass.__dict__:
            descriptor = klass.__dict__["kindOfNode"]
            break
    assert isinstance(descriptor, property)

def test_activity_objectnode_has_ordering():
    assert hasattr(activity_ObjectNode, "ordering")
    descriptor = None
    for klass in activity_ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_activity_objectnode_has_isControlType():
    assert hasattr(activity_ObjectNode, "isControlType")
    descriptor = None
    for klass in activity_ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)



def test_activity_abstractaction_is_not_abstract():
    assert not inspect.isabstract(activity_AbstractAction)


def test_activity_abstractaction_constructor_exists():
    assert callable(activity_AbstractAction.__init__)


def test_activity_abstractaction_constructor_args():
    sig = inspect.signature(activity_AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activity_objectflow_is_not_abstract():
    assert not inspect.isabstract(activity_ObjectFlow)


def test_activity_objectflow_constructor_exists():
    assert callable(activity_ObjectFlow.__init__)


def test_activity_objectflow_constructor_args():
    sig = inspect.signature(activity_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_activity_objectflow_has_isMulticast():
    assert hasattr(activity_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in activity_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_activity_objectflow_has_isMultireceive():
    assert hasattr(activity_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in activity_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_activity_activitynode_is_not_abstract():
    assert not inspect.isabstract(activity_ActivityNode)


def test_activity_activitynode_constructor_exists():
    assert callable(activity_ActivityNode.__init__)


def test_activity_activitynode_constructor_args():
    sig = inspect.signature(activity_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activity_valuespecification_is_not_abstract():
    assert not inspect.isabstract(activity_ValueSpecification)


def test_activity_valuespecification_constructor_exists():
    assert callable(activity_ValueSpecification.__init__)


def test_activity_valuespecification_constructor_args():
    sig = inspect.signature(activity_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_activity_activitypartition_is_not_abstract():
    assert not inspect.isabstract(activity_ActivityPartition)


def test_activity_activitypartition_constructor_exists():
    assert callable(activity_ActivityPartition.__init__)


def test_activity_activitypartition_constructor_args():
    sig = inspect.signature(activity_ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"

def test_activity_activitypartition_has_isExternal():
    assert hasattr(activity_ActivityPartition, "isExternal")
    descriptor = None
    for klass in activity_ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_activity_activitypartition_has_isDimension():
    assert hasattr(activity_ActivityPartition, "isDimension")
    descriptor = None
    for klass in activity_ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)



def test_activity_activityedge_is_not_abstract():
    assert not inspect.isabstract(activity_ActivityEdge)


def test_activity_activityedge_constructor_exists():
    assert callable(activity_ActivityEdge.__init__)


def test_activity_activityedge_constructor_args():
    sig = inspect.signature(activity_ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "kindOfRate" in params, "Missing parameter 'kindOfRate'"

def test_activity_activityedge_has_kindOfRate():
    assert hasattr(activity_ActivityEdge, "kindOfRate")
    descriptor = None
    for klass in activity_ActivityEdge.__mro__:
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



def test_activity_abstractactivity_is_not_abstract():
    assert not inspect.isabstract(activity_AbstractActivity)


def test_activity_abstractactivity_constructor_exists():
    assert callable(activity_AbstractActivity.__init__)


def test_activity_abstractactivity_constructor_args():
    sig = inspect.signature(activity_AbstractActivity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_activity_abstractactivity_has_isReadOnly():
    assert hasattr(activity_AbstractActivity, "isReadOnly")
    descriptor = None
    for klass in activity_AbstractActivity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_activity_abstractactivity_has_isSingleExecution():
    assert hasattr(activity_AbstractActivity, "isSingleExecution")
    descriptor = None
    for klass in activity_AbstractActivity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_objectnodekind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeKind is not None

def test_objectnodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeKind]
    expected_literals = [
        "Overwrite",
        "Unspecified",
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
        "FIFO",
        "LIFO",
        "unordered",
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
activity_Pin_strategy = st.builds(
    activity_Pin,
    isControl=
        st.booleans()
)
activity_AbstractBehavior_strategy = st.builds(
    activity_AbstractBehavior,
)
activity_IState_strategy = st.builds(
    activity_IState,
)
AbstractAction_strategy = st.builds(
    AbstractAction,
)
activity_AcceptEventAction_strategy = st.builds(
    activity_AcceptEventAction,
    isUnmarshall=
        st.booleans()
)
activity_OutputPin_strategy = st.builds(
    activity_OutputPin,
)
activity_InputPin_strategy = st.builds(
    activity_InputPin,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
AbstractNamedElement_strategy = st.builds(
    AbstractNamedElement,
)
activity_ObjectNode_strategy = st.builds(
    activity_ObjectNode,
    kindOfNode=
        safe_text,
    ordering=
        safe_text,
    isControlType=
        st.booleans()
)
activity_AbstractAction_strategy = st.builds(
    activity_AbstractAction,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
activity_ObjectFlow_strategy = st.builds(
    activity_ObjectFlow,
    isMulticast=
        st.booleans(),
    isMultireceive=
        st.booleans()
)
activity_ActivityNode_strategy = st.builds(
    activity_ActivityNode,
)
activity_ValueSpecification_strategy = st.builds(
    activity_ValueSpecification,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
activity_ActivityPartition_strategy = st.builds(
    activity_ActivityPartition,
    isExternal=
        st.booleans(),
    isDimension=
        st.booleans()
)
activity_ActivityEdge_strategy = st.builds(
    activity_ActivityEdge,
    kindOfRate=
        safe_text
)
TraceableElement_strategy = st.builds(
    TraceableElement,
)
AbstractBehavior_strategy = st.builds(
    AbstractBehavior,
)
activity_AbstractActivity_strategy = st.builds(
    activity_AbstractActivity,
    isReadOnly=
        st.booleans(),
    isSingleExecution=
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

@given(instance=activity_Pin_strategy)
@settings(max_examples=50)
def test_activity_pin_instantiation(instance):
    assert isinstance(instance, activity_Pin)



@given(instance=activity_Pin_strategy)
def test_activity_pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=activity_AbstractBehavior_strategy)
@settings(max_examples=50)
def test_activity_abstractbehavior_instantiation(instance):
    assert isinstance(instance, activity_AbstractBehavior)

@given(instance=activity_IState_strategy)
@settings(max_examples=50)
def test_activity_istate_instantiation(instance):
    assert isinstance(instance, activity_IState)

@given(instance=AbstractAction_strategy)
@settings(max_examples=50)
def test_abstractaction_instantiation(instance):
    assert isinstance(instance, AbstractAction)

@given(instance=activity_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_activity_accepteventaction_instantiation(instance):
    assert isinstance(instance, activity_AcceptEventAction)



@given(instance=activity_AcceptEventAction_strategy)
def test_activity_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=activity_OutputPin_strategy)
@settings(max_examples=50)
def test_activity_outputpin_instantiation(instance):
    assert isinstance(instance, activity_OutputPin)

@given(instance=activity_InputPin_strategy)
@settings(max_examples=50)
def test_activity_inputpin_instantiation(instance):
    assert isinstance(instance, activity_InputPin)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=AbstractNamedElement_strategy)
@settings(max_examples=50)
def test_abstractnamedelement_instantiation(instance):
    assert isinstance(instance, AbstractNamedElement)

@given(instance=activity_ObjectNode_strategy)
@settings(max_examples=50)
def test_activity_objectnode_instantiation(instance):
    assert isinstance(instance, activity_ObjectNode)



@given(instance=activity_ObjectNode_strategy)
def test_activity_objectnode_kindOfNode_setter(instance):
    original = instance.kindOfNode
    instance.kindOfNode = original
    assert instance.kindOfNode == original



@given(instance=activity_ObjectNode_strategy)
def test_activity_objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=activity_ObjectNode_strategy)
def test_activity_objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=activity_AbstractAction_strategy)
@settings(max_examples=50)
def test_activity_abstractaction_instantiation(instance):
    assert isinstance(instance, activity_AbstractAction)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=activity_ObjectFlow_strategy)
@settings(max_examples=50)
def test_activity_objectflow_instantiation(instance):
    assert isinstance(instance, activity_ObjectFlow)



@given(instance=activity_ObjectFlow_strategy)
def test_activity_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=activity_ObjectFlow_strategy)
def test_activity_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=activity_ActivityNode_strategy)
@settings(max_examples=50)
def test_activity_activitynode_instantiation(instance):
    assert isinstance(instance, activity_ActivityNode)

@given(instance=activity_ValueSpecification_strategy)
@settings(max_examples=50)
def test_activity_valuespecification_instantiation(instance):
    assert isinstance(instance, activity_ValueSpecification)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=activity_ActivityPartition_strategy)
@settings(max_examples=50)
def test_activity_activitypartition_instantiation(instance):
    assert isinstance(instance, activity_ActivityPartition)



@given(instance=activity_ActivityPartition_strategy)
def test_activity_activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=activity_ActivityPartition_strategy)
def test_activity_activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=activity_ActivityEdge_strategy)
@settings(max_examples=50)
def test_activity_activityedge_instantiation(instance):
    assert isinstance(instance, activity_ActivityEdge)



@given(instance=activity_ActivityEdge_strategy)
def test_activity_activityedge_kindOfRate_setter(instance):
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

@given(instance=activity_AbstractActivity_strategy)
@settings(max_examples=50)
def test_activity_abstractactivity_instantiation(instance):
    assert isinstance(instance, activity_AbstractActivity)



@given(instance=activity_AbstractActivity_strategy)
def test_activity_abstractactivity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=activity_AbstractActivity_strategy)
def test_activity_abstractactivity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

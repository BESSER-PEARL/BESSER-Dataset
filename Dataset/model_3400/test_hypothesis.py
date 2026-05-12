import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    guigraph_InhibitorArc,
    guigraph_StandardArc,
    rules_IRealTimeConsumer,
    GuiGraphNode,
    guigraph_Place,
    guigraph_Transition,
    Place,
    guigraph_NoWidgetNode,
    Widget,
    guigraph_Form,
    GuiGraph,
    guigraph_Page,
    ITimeConsumer,
    Predicate,
    guigraph_PreGenerationSequence,
    Transition,
    guigraph_TimerTransition,
    guigraph_PageTransition,
    guigraph_ConditionActionTransition,
    AbstractModelElement,
    guigraph_GuiGraphNode,
    guigraph_Widget,
    guigraph_GuiGraph,
    guigraph_Arc,
    TimingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_inhibitorarc_is_not_abstract():
    assert not inspect.isabstract(guigraph_InhibitorArc)


def test_guigraph_inhibitorarc_constructor_exists():
    assert callable(guigraph_InhibitorArc.__init__)


def test_guigraph_inhibitorarc_constructor_args():
    sig = inspect.signature(guigraph_InhibitorArc.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_standardarc_is_not_abstract():
    assert not inspect.isabstract(guigraph_StandardArc)


def test_guigraph_standardarc_constructor_exists():
    assert callable(guigraph_StandardArc.__init__)


def test_guigraph_standardarc_constructor_args():
    sig = inspect.signature(guigraph_StandardArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_guigraph_standardarc_has_weight():
    assert hasattr(guigraph_StandardArc, "weight")
    descriptor = None
    for klass in guigraph_StandardArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_rules_irealtimeconsumer_is_not_abstract():
    assert not inspect.isabstract(rules_IRealTimeConsumer)


def test_rules_irealtimeconsumer_constructor_exists():
    assert callable(rules_IRealTimeConsumer.__init__)


def test_rules_irealtimeconsumer_constructor_args():
    sig = inspect.signature(rules_IRealTimeConsumer.__init__)
    params = list(sig.parameters.keys())



def test_guigraphnode_is_not_abstract():
    assert not inspect.isabstract(GuiGraphNode)


def test_guigraphnode_constructor_exists():
    assert callable(GuiGraphNode.__init__)


def test_guigraphnode_constructor_args():
    sig = inspect.signature(GuiGraphNode.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_place_is_not_abstract():
    assert not inspect.isabstract(guigraph_Place)


def test_guigraph_place_constructor_exists():
    assert callable(guigraph_Place.__init__)


def test_guigraph_place_constructor_args():
    sig = inspect.signature(guigraph_Place.__init__)
    params = list(sig.parameters.keys())
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_guigraph_place_has_initialTokens():
    assert hasattr(guigraph_Place, "initialTokens")
    descriptor = None
    for klass in guigraph_Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_guigraph_transition_is_not_abstract():
    assert not inspect.isabstract(guigraph_Transition)


def test_guigraph_transition_constructor_exists():
    assert callable(guigraph_Transition.__init__)


def test_guigraph_transition_constructor_args():
    sig = inspect.signature(guigraph_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "faultProbability" in params, "Missing parameter 'faultProbability'"
    assert "rate" in params, "Missing parameter 'rate'"
    assert "timeMin" in params, "Missing parameter 'timeMin'"
    assert "timeMax" in params, "Missing parameter 'timeMax'"
    assert "timingType" in params, "Missing parameter 'timingType'"
    assert "terminates" in params, "Missing parameter 'terminates'"
    assert "faultImpact" in params, "Missing parameter 'faultImpact'"

def test_guigraph_transition_has_faultProbability():
    assert hasattr(guigraph_Transition, "faultProbability")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "faultProbability" in klass.__dict__:
            descriptor = klass.__dict__["faultProbability"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_rate():
    assert hasattr(guigraph_Transition, "rate")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_timeMin():
    assert hasattr(guigraph_Transition, "timeMin")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "timeMin" in klass.__dict__:
            descriptor = klass.__dict__["timeMin"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_timeMax():
    assert hasattr(guigraph_Transition, "timeMax")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "timeMax" in klass.__dict__:
            descriptor = klass.__dict__["timeMax"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_timingType():
    assert hasattr(guigraph_Transition, "timingType")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "timingType" in klass.__dict__:
            descriptor = klass.__dict__["timingType"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_terminates():
    assert hasattr(guigraph_Transition, "terminates")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "terminates" in klass.__dict__:
            descriptor = klass.__dict__["terminates"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_transition_has_faultImpact():
    assert hasattr(guigraph_Transition, "faultImpact")
    descriptor = None
    for klass in guigraph_Transition.__mro__:
        if "faultImpact" in klass.__dict__:
            descriptor = klass.__dict__["faultImpact"]
            break
    assert isinstance(descriptor, property)



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_nowidgetnode_is_not_abstract():
    assert not inspect.isabstract(guigraph_NoWidgetNode)


def test_guigraph_nowidgetnode_constructor_exists():
    assert callable(guigraph_NoWidgetNode.__init__)


def test_guigraph_nowidgetnode_constructor_args():
    sig = inspect.signature(guigraph_NoWidgetNode.__init__)
    params = list(sig.parameters.keys())



def test_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_form_is_not_abstract():
    assert not inspect.isabstract(guigraph_Form)


def test_guigraph_form_constructor_exists():
    assert callable(guigraph_Form.__init__)


def test_guigraph_form_constructor_args():
    sig = inspect.signature(guigraph_Form.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_is_not_abstract():
    assert not inspect.isabstract(GuiGraph)


def test_guigraph_constructor_exists():
    assert callable(GuiGraph.__init__)


def test_guigraph_constructor_args():
    sig = inspect.signature(GuiGraph.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_page_is_not_abstract():
    assert not inspect.isabstract(guigraph_Page)


def test_guigraph_page_constructor_exists():
    assert callable(guigraph_Page.__init__)


def test_guigraph_page_constructor_args():
    sig = inspect.signature(guigraph_Page.__init__)
    params = list(sig.parameters.keys())



def test_itimeconsumer_is_not_abstract():
    assert not inspect.isabstract(ITimeConsumer)


def test_itimeconsumer_constructor_exists():
    assert callable(ITimeConsumer.__init__)


def test_itimeconsumer_constructor_args():
    sig = inspect.signature(ITimeConsumer.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_pregenerationsequence_is_not_abstract():
    assert not inspect.isabstract(guigraph_PreGenerationSequence)


def test_guigraph_pregenerationsequence_constructor_exists():
    assert callable(guigraph_PreGenerationSequence.__init__)


def test_guigraph_pregenerationsequence_constructor_args():
    sig = inspect.signature(guigraph_PreGenerationSequence.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_timertransition_is_not_abstract():
    assert not inspect.isabstract(guigraph_TimerTransition)


def test_guigraph_timertransition_constructor_exists():
    assert callable(guigraph_TimerTransition.__init__)


def test_guigraph_timertransition_constructor_args():
    sig = inspect.signature(guigraph_TimerTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_guigraph_timertransition_has_duration():
    assert hasattr(guigraph_TimerTransition, "duration")
    descriptor = None
    for klass in guigraph_TimerTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_guigraph_pagetransition_is_not_abstract():
    assert not inspect.isabstract(guigraph_PageTransition)


def test_guigraph_pagetransition_constructor_exists():
    assert callable(guigraph_PageTransition.__init__)


def test_guigraph_pagetransition_constructor_args():
    sig = inspect.signature(guigraph_PageTransition.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_conditionactiontransition_is_not_abstract():
    assert not inspect.isabstract(guigraph_ConditionActionTransition)


def test_guigraph_conditionactiontransition_constructor_exists():
    assert callable(guigraph_ConditionActionTransition.__init__)


def test_guigraph_conditionactiontransition_constructor_args():
    sig = inspect.signature(guigraph_ConditionActionTransition.__init__)
    params = list(sig.parameters.keys())
    assert "applicationConditionText" in params, "Missing parameter 'applicationConditionText'"
    assert "actionsText" in params, "Missing parameter 'actionsText'"

def test_guigraph_conditionactiontransition_has_applicationConditionText():
    assert hasattr(guigraph_ConditionActionTransition, "applicationConditionText")
    descriptor = None
    for klass in guigraph_ConditionActionTransition.__mro__:
        if "applicationConditionText" in klass.__dict__:
            descriptor = klass.__dict__["applicationConditionText"]
            break
    assert isinstance(descriptor, property)

def test_guigraph_conditionactiontransition_has_actionsText():
    assert hasattr(guigraph_ConditionActionTransition, "actionsText")
    descriptor = None
    for klass in guigraph_ConditionActionTransition.__mro__:
        if "actionsText" in klass.__dict__:
            descriptor = klass.__dict__["actionsText"]
            break
    assert isinstance(descriptor, property)



def test_abstractmodelelement_is_not_abstract():
    assert not inspect.isabstract(AbstractModelElement)


def test_abstractmodelelement_constructor_exists():
    assert callable(AbstractModelElement.__init__)


def test_abstractmodelelement_constructor_args():
    sig = inspect.signature(AbstractModelElement.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_guigraphnode_is_not_abstract():
    assert not inspect.isabstract(guigraph_GuiGraphNode)


def test_guigraph_guigraphnode_constructor_exists():
    assert callable(guigraph_GuiGraphNode.__init__)


def test_guigraph_guigraphnode_constructor_args():
    sig = inspect.signature(guigraph_GuiGraphNode.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_widget_is_not_abstract():
    assert not inspect.isabstract(guigraph_Widget)


def test_guigraph_widget_constructor_exists():
    assert callable(guigraph_Widget.__init__)


def test_guigraph_widget_constructor_args():
    sig = inspect.signature(guigraph_Widget.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_guigraph_widget_has_image():
    assert hasattr(guigraph_Widget, "image")
    descriptor = None
    for klass in guigraph_Widget.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_guigraph_guigraph_is_not_abstract():
    assert not inspect.isabstract(guigraph_GuiGraph)


def test_guigraph_guigraph_constructor_exists():
    assert callable(guigraph_GuiGraph.__init__)


def test_guigraph_guigraph_constructor_args():
    sig = inspect.signature(guigraph_GuiGraph.__init__)
    params = list(sig.parameters.keys())
    assert "invariantText" in params, "Missing parameter 'invariantText'"

def test_guigraph_guigraph_has_invariantText():
    assert hasattr(guigraph_GuiGraph, "invariantText")
    descriptor = None
    for klass in guigraph_GuiGraph.__mro__:
        if "invariantText" in klass.__dict__:
            descriptor = klass.__dict__["invariantText"]
            break
    assert isinstance(descriptor, property)



def test_guigraph_arc_is_not_abstract():
    assert not inspect.isabstract(guigraph_Arc)


def test_guigraph_arc_constructor_exists():
    assert callable(guigraph_Arc.__init__)


def test_guigraph_arc_constructor_args():
    sig = inspect.signature(guigraph_Arc.__init__)
    params = list(sig.parameters.keys())

def test_timingtype_exists():
    # Check that the Enumeration exists
    assert TimingType is not None

def test_timingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimingType]
    expected_literals = [
        "Interval",
        "DelayUntilStart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimingType"


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
Arc_strategy = st.builds(
    Arc,
)
guigraph_InhibitorArc_strategy = st.builds(
    guigraph_InhibitorArc,
)
guigraph_StandardArc_strategy = st.builds(
    guigraph_StandardArc,
    weight=
        st.integers()
)
rules_IRealTimeConsumer_strategy = st.builds(
    rules_IRealTimeConsumer,
)
GuiGraphNode_strategy = st.builds(
    GuiGraphNode,
)
guigraph_Place_strategy = st.builds(
    guigraph_Place,
    initialTokens=
        st.integers()
)
guigraph_Transition_strategy = st.builds(
    guigraph_Transition,
    faultProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rate=
        st.integers(),
    timeMin=
        safe_text,
    timeMax=
        safe_text,
    timingType=
        safe_text,
    terminates=
        st.booleans(),
    faultImpact=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Place_strategy = st.builds(
    Place,
)
guigraph_NoWidgetNode_strategy = st.builds(
    guigraph_NoWidgetNode,
)
Widget_strategy = st.builds(
    Widget,
)
guigraph_Form_strategy = st.builds(
    guigraph_Form,
)
GuiGraph_strategy = st.builds(
    GuiGraph,
)
guigraph_Page_strategy = st.builds(
    guigraph_Page,
)
ITimeConsumer_strategy = st.builds(
    ITimeConsumer,
)
Predicate_strategy = st.builds(
    Predicate,
)
guigraph_PreGenerationSequence_strategy = st.builds(
    guigraph_PreGenerationSequence,
)
Transition_strategy = st.builds(
    Transition,
)
guigraph_TimerTransition_strategy = st.builds(
    guigraph_TimerTransition,
    duration=
        st.integers()
)
guigraph_PageTransition_strategy = st.builds(
    guigraph_PageTransition,
)
guigraph_ConditionActionTransition_strategy = st.builds(
    guigraph_ConditionActionTransition,
    applicationConditionText=
        safe_text,
    actionsText=
        safe_text
)
AbstractModelElement_strategy = st.builds(
    AbstractModelElement,
)
guigraph_GuiGraphNode_strategy = st.builds(
    guigraph_GuiGraphNode,
)
guigraph_Widget_strategy = st.builds(
    guigraph_Widget,
    image=
        safe_text
)
guigraph_GuiGraph_strategy = st.builds(
    guigraph_GuiGraph,
    invariantText=
        safe_text
)
guigraph_Arc_strategy = st.builds(
    guigraph_Arc,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=guigraph_InhibitorArc_strategy)
@settings(max_examples=50)
def test_guigraph_inhibitorarc_instantiation(instance):
    assert isinstance(instance, guigraph_InhibitorArc)

@given(instance=guigraph_StandardArc_strategy)
@settings(max_examples=50)
def test_guigraph_standardarc_instantiation(instance):
    assert isinstance(instance, guigraph_StandardArc)



@given(instance=guigraph_StandardArc_strategy)
def test_guigraph_standardarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=rules_IRealTimeConsumer_strategy)
@settings(max_examples=50)
def test_rules_irealtimeconsumer_instantiation(instance):
    assert isinstance(instance, rules_IRealTimeConsumer)

@given(instance=GuiGraphNode_strategy)
@settings(max_examples=50)
def test_guigraphnode_instantiation(instance):
    assert isinstance(instance, GuiGraphNode)

@given(instance=guigraph_Place_strategy)
@settings(max_examples=50)
def test_guigraph_place_instantiation(instance):
    assert isinstance(instance, guigraph_Place)



@given(instance=guigraph_Place_strategy)
def test_guigraph_place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=guigraph_Transition_strategy)
@settings(max_examples=50)
def test_guigraph_transition_instantiation(instance):
    assert isinstance(instance, guigraph_Transition)



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_faultProbability_setter(instance):
    original = instance.faultProbability
    instance.faultProbability = original
    assert instance.faultProbability == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_timeMin_setter(instance):
    original = instance.timeMin
    instance.timeMin = original
    assert instance.timeMin == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_timeMax_setter(instance):
    original = instance.timeMax
    instance.timeMax = original
    assert instance.timeMax == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_timingType_setter(instance):
    original = instance.timingType
    instance.timingType = original
    assert instance.timingType == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_terminates_setter(instance):
    original = instance.terminates
    instance.terminates = original
    assert instance.terminates == original



@given(instance=guigraph_Transition_strategy)
def test_guigraph_transition_faultImpact_setter(instance):
    original = instance.faultImpact
    instance.faultImpact = original
    assert instance.faultImpact == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=guigraph_NoWidgetNode_strategy)
@settings(max_examples=50)
def test_guigraph_nowidgetnode_instantiation(instance):
    assert isinstance(instance, guigraph_NoWidgetNode)

@given(instance=Widget_strategy)
@settings(max_examples=50)
def test_widget_instantiation(instance):
    assert isinstance(instance, Widget)

@given(instance=guigraph_Form_strategy)
@settings(max_examples=50)
def test_guigraph_form_instantiation(instance):
    assert isinstance(instance, guigraph_Form)

@given(instance=GuiGraph_strategy)
@settings(max_examples=50)
def test_guigraph_instantiation(instance):
    assert isinstance(instance, GuiGraph)

@given(instance=guigraph_Page_strategy)
@settings(max_examples=50)
def test_guigraph_page_instantiation(instance):
    assert isinstance(instance, guigraph_Page)

@given(instance=ITimeConsumer_strategy)
@settings(max_examples=50)
def test_itimeconsumer_instantiation(instance):
    assert isinstance(instance, ITimeConsumer)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=guigraph_PreGenerationSequence_strategy)
@settings(max_examples=50)
def test_guigraph_pregenerationsequence_instantiation(instance):
    assert isinstance(instance, guigraph_PreGenerationSequence)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=guigraph_TimerTransition_strategy)
@settings(max_examples=50)
def test_guigraph_timertransition_instantiation(instance):
    assert isinstance(instance, guigraph_TimerTransition)



@given(instance=guigraph_TimerTransition_strategy)
def test_guigraph_timertransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=guigraph_PageTransition_strategy)
@settings(max_examples=50)
def test_guigraph_pagetransition_instantiation(instance):
    assert isinstance(instance, guigraph_PageTransition)

@given(instance=guigraph_ConditionActionTransition_strategy)
@settings(max_examples=50)
def test_guigraph_conditionactiontransition_instantiation(instance):
    assert isinstance(instance, guigraph_ConditionActionTransition)



@given(instance=guigraph_ConditionActionTransition_strategy)
def test_guigraph_conditionactiontransition_applicationConditionText_setter(instance):
    original = instance.applicationConditionText
    instance.applicationConditionText = original
    assert instance.applicationConditionText == original



@given(instance=guigraph_ConditionActionTransition_strategy)
def test_guigraph_conditionactiontransition_actionsText_setter(instance):
    original = instance.actionsText
    instance.actionsText = original
    assert instance.actionsText == original

@given(instance=AbstractModelElement_strategy)
@settings(max_examples=50)
def test_abstractmodelelement_instantiation(instance):
    assert isinstance(instance, AbstractModelElement)

@given(instance=guigraph_GuiGraphNode_strategy)
@settings(max_examples=50)
def test_guigraph_guigraphnode_instantiation(instance):
    assert isinstance(instance, guigraph_GuiGraphNode)

@given(instance=guigraph_Widget_strategy)
@settings(max_examples=50)
def test_guigraph_widget_instantiation(instance):
    assert isinstance(instance, guigraph_Widget)



@given(instance=guigraph_Widget_strategy)
def test_guigraph_widget_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=guigraph_GuiGraph_strategy)
@settings(max_examples=50)
def test_guigraph_guigraph_instantiation(instance):
    assert isinstance(instance, guigraph_GuiGraph)



@given(instance=guigraph_GuiGraph_strategy)
def test_guigraph_guigraph_invariantText_setter(instance):
    original = instance.invariantText
    instance.invariantText = original
    assert instance.invariantText == original

@given(instance=guigraph_Arc_strategy)
@settings(max_examples=50)
def test_guigraph_arc_instantiation(instance):
    assert isinstance(instance, guigraph_Arc)

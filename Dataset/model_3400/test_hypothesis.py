import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    guigraph::InhibitorArc,
    guigraph::StandardArc,
    rules::IRealTimeConsumer,
    GuiGraphNode,
    guigraph::Place,
    guigraph::Transition,
    Place,
    guigraph::NoWidgetNode,
    Widget,
    guigraph::Form,
    GuiGraph,
    guigraph::Page,
    ITimeConsumer,
    Predicate,
    guigraph::PreGenerationSequence,
    Transition,
    guigraph::TimerTransition,
    guigraph::PageTransition,
    guigraph::ConditionActionTransition,
    AbstractModelElement,
    guigraph::GuiGraphNode,
    guigraph::Widget,
    guigraph::GuiGraph,
    guigraph::Arc,
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



def test_guigraph::inhibitorarc_is_not_abstract():
    assert not inspect.isabstract(guigraph::InhibitorArc)


def test_guigraph::inhibitorarc_constructor_exists():
    assert callable(guigraph::InhibitorArc.__init__)


def test_guigraph::inhibitorarc_constructor_args():
    sig = inspect.signature(guigraph::InhibitorArc.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::standardarc_is_not_abstract():
    assert not inspect.isabstract(guigraph::StandardArc)


def test_guigraph::standardarc_constructor_exists():
    assert callable(guigraph::StandardArc.__init__)


def test_guigraph::standardarc_constructor_args():
    sig = inspect.signature(guigraph::StandardArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_guigraph::standardarc_has_weight():
    assert hasattr(guigraph::StandardArc, "weight")
    descriptor = None
    for klass in guigraph::StandardArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_rules::irealtimeconsumer_is_not_abstract():
    assert not inspect.isabstract(rules::IRealTimeConsumer)


def test_rules::irealtimeconsumer_constructor_exists():
    assert callable(rules::IRealTimeConsumer.__init__)


def test_rules::irealtimeconsumer_constructor_args():
    sig = inspect.signature(rules::IRealTimeConsumer.__init__)
    params = list(sig.parameters.keys())



def test_guigraphnode_is_not_abstract():
    assert not inspect.isabstract(GuiGraphNode)


def test_guigraphnode_constructor_exists():
    assert callable(GuiGraphNode.__init__)


def test_guigraphnode_constructor_args():
    sig = inspect.signature(GuiGraphNode.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::place_is_not_abstract():
    assert not inspect.isabstract(guigraph::Place)


def test_guigraph::place_constructor_exists():
    assert callable(guigraph::Place.__init__)


def test_guigraph::place_constructor_args():
    sig = inspect.signature(guigraph::Place.__init__)
    params = list(sig.parameters.keys())
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_guigraph::place_has_initialTokens():
    assert hasattr(guigraph::Place, "initialTokens")
    descriptor = None
    for klass in guigraph::Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_guigraph::transition_is_not_abstract():
    assert not inspect.isabstract(guigraph::Transition)


def test_guigraph::transition_constructor_exists():
    assert callable(guigraph::Transition.__init__)


def test_guigraph::transition_constructor_args():
    sig = inspect.signature(guigraph::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "timingType" in params, "Missing parameter 'timingType'"
    assert "timeMax" in params, "Missing parameter 'timeMax'"
    assert "terminates" in params, "Missing parameter 'terminates'"
    assert "faultImpact" in params, "Missing parameter 'faultImpact'"
    assert "rate" in params, "Missing parameter 'rate'"
    assert "faultProbability" in params, "Missing parameter 'faultProbability'"
    assert "timeMin" in params, "Missing parameter 'timeMin'"

def test_guigraph::transition_has_timingType():
    assert hasattr(guigraph::Transition, "timingType")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "timingType" in klass.__dict__:
            descriptor = klass.__dict__["timingType"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_timeMax():
    assert hasattr(guigraph::Transition, "timeMax")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "timeMax" in klass.__dict__:
            descriptor = klass.__dict__["timeMax"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_terminates():
    assert hasattr(guigraph::Transition, "terminates")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "terminates" in klass.__dict__:
            descriptor = klass.__dict__["terminates"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_faultImpact():
    assert hasattr(guigraph::Transition, "faultImpact")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "faultImpact" in klass.__dict__:
            descriptor = klass.__dict__["faultImpact"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_rate():
    assert hasattr(guigraph::Transition, "rate")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_faultProbability():
    assert hasattr(guigraph::Transition, "faultProbability")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "faultProbability" in klass.__dict__:
            descriptor = klass.__dict__["faultProbability"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::transition_has_timeMin():
    assert hasattr(guigraph::Transition, "timeMin")
    descriptor = None
    for klass in guigraph::Transition.__mro__:
        if "timeMin" in klass.__dict__:
            descriptor = klass.__dict__["timeMin"]
            break
    assert isinstance(descriptor, property)



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::nowidgetnode_is_not_abstract():
    assert not inspect.isabstract(guigraph::NoWidgetNode)


def test_guigraph::nowidgetnode_constructor_exists():
    assert callable(guigraph::NoWidgetNode.__init__)


def test_guigraph::nowidgetnode_constructor_args():
    sig = inspect.signature(guigraph::NoWidgetNode.__init__)
    params = list(sig.parameters.keys())



def test_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::form_is_not_abstract():
    assert not inspect.isabstract(guigraph::Form)


def test_guigraph::form_constructor_exists():
    assert callable(guigraph::Form.__init__)


def test_guigraph::form_constructor_args():
    sig = inspect.signature(guigraph::Form.__init__)
    params = list(sig.parameters.keys())



def test_guigraph_is_not_abstract():
    assert not inspect.isabstract(GuiGraph)


def test_guigraph_constructor_exists():
    assert callable(GuiGraph.__init__)


def test_guigraph_constructor_args():
    sig = inspect.signature(GuiGraph.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::page_is_not_abstract():
    assert not inspect.isabstract(guigraph::Page)


def test_guigraph::page_constructor_exists():
    assert callable(guigraph::Page.__init__)


def test_guigraph::page_constructor_args():
    sig = inspect.signature(guigraph::Page.__init__)
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



def test_guigraph::pregenerationsequence_is_not_abstract():
    assert not inspect.isabstract(guigraph::PreGenerationSequence)


def test_guigraph::pregenerationsequence_constructor_exists():
    assert callable(guigraph::PreGenerationSequence.__init__)


def test_guigraph::pregenerationsequence_constructor_args():
    sig = inspect.signature(guigraph::PreGenerationSequence.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::timertransition_is_not_abstract():
    assert not inspect.isabstract(guigraph::TimerTransition)


def test_guigraph::timertransition_constructor_exists():
    assert callable(guigraph::TimerTransition.__init__)


def test_guigraph::timertransition_constructor_args():
    sig = inspect.signature(guigraph::TimerTransition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_guigraph::timertransition_has_duration():
    assert hasattr(guigraph::TimerTransition, "duration")
    descriptor = None
    for klass in guigraph::TimerTransition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_guigraph::pagetransition_is_not_abstract():
    assert not inspect.isabstract(guigraph::PageTransition)


def test_guigraph::pagetransition_constructor_exists():
    assert callable(guigraph::PageTransition.__init__)


def test_guigraph::pagetransition_constructor_args():
    sig = inspect.signature(guigraph::PageTransition.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::conditionactiontransition_is_not_abstract():
    assert not inspect.isabstract(guigraph::ConditionActionTransition)


def test_guigraph::conditionactiontransition_constructor_exists():
    assert callable(guigraph::ConditionActionTransition.__init__)


def test_guigraph::conditionactiontransition_constructor_args():
    sig = inspect.signature(guigraph::ConditionActionTransition.__init__)
    params = list(sig.parameters.keys())
    assert "actionsText" in params, "Missing parameter 'actionsText'"
    assert "applicationConditionText" in params, "Missing parameter 'applicationConditionText'"

def test_guigraph::conditionactiontransition_has_actionsText():
    assert hasattr(guigraph::ConditionActionTransition, "actionsText")
    descriptor = None
    for klass in guigraph::ConditionActionTransition.__mro__:
        if "actionsText" in klass.__dict__:
            descriptor = klass.__dict__["actionsText"]
            break
    assert isinstance(descriptor, property)

def test_guigraph::conditionactiontransition_has_applicationConditionText():
    assert hasattr(guigraph::ConditionActionTransition, "applicationConditionText")
    descriptor = None
    for klass in guigraph::ConditionActionTransition.__mro__:
        if "applicationConditionText" in klass.__dict__:
            descriptor = klass.__dict__["applicationConditionText"]
            break
    assert isinstance(descriptor, property)



def test_abstractmodelelement_is_not_abstract():
    assert not inspect.isabstract(AbstractModelElement)


def test_abstractmodelelement_constructor_exists():
    assert callable(AbstractModelElement.__init__)


def test_abstractmodelelement_constructor_args():
    sig = inspect.signature(AbstractModelElement.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::guigraphnode_is_not_abstract():
    assert not inspect.isabstract(guigraph::GuiGraphNode)


def test_guigraph::guigraphnode_constructor_exists():
    assert callable(guigraph::GuiGraphNode.__init__)


def test_guigraph::guigraphnode_constructor_args():
    sig = inspect.signature(guigraph::GuiGraphNode.__init__)
    params = list(sig.parameters.keys())



def test_guigraph::widget_is_not_abstract():
    assert not inspect.isabstract(guigraph::Widget)


def test_guigraph::widget_constructor_exists():
    assert callable(guigraph::Widget.__init__)


def test_guigraph::widget_constructor_args():
    sig = inspect.signature(guigraph::Widget.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_guigraph::widget_has_image():
    assert hasattr(guigraph::Widget, "image")
    descriptor = None
    for klass in guigraph::Widget.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_guigraph::guigraph_is_not_abstract():
    assert not inspect.isabstract(guigraph::GuiGraph)


def test_guigraph::guigraph_constructor_exists():
    assert callable(guigraph::GuiGraph.__init__)


def test_guigraph::guigraph_constructor_args():
    sig = inspect.signature(guigraph::GuiGraph.__init__)
    params = list(sig.parameters.keys())
    assert "invariantText" in params, "Missing parameter 'invariantText'"

def test_guigraph::guigraph_has_invariantText():
    assert hasattr(guigraph::GuiGraph, "invariantText")
    descriptor = None
    for klass in guigraph::GuiGraph.__mro__:
        if "invariantText" in klass.__dict__:
            descriptor = klass.__dict__["invariantText"]
            break
    assert isinstance(descriptor, property)



def test_guigraph::arc_is_not_abstract():
    assert not inspect.isabstract(guigraph::Arc)


def test_guigraph::arc_constructor_exists():
    assert callable(guigraph::Arc.__init__)


def test_guigraph::arc_constructor_args():
    sig = inspect.signature(guigraph::Arc.__init__)
    params = list(sig.parameters.keys())

def test_timingtype_exists():
    # Check that the Enumeration exists
    assert TimingType is not None

def test_timingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimingType]
    expected_literals = [
        "DelayUntilStart",
        "Interval",
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
guigraph::InhibitorArc_strategy = st.builds(
    guigraph::InhibitorArc,
)
guigraph::StandardArc_strategy = st.builds(
    guigraph::StandardArc,
    weight=
        st.integers()
)
rules::IRealTimeConsumer_strategy = st.builds(
    rules::IRealTimeConsumer,
)
GuiGraphNode_strategy = st.builds(
    GuiGraphNode,
)
guigraph::Place_strategy = st.builds(
    guigraph::Place,
    initialTokens=
        st.integers()
)
guigraph::Transition_strategy = st.builds(
    guigraph::Transition,
    timingType=
        safe_text,
    timeMax=
        safe_text,
    terminates=
        st.booleans(),
    faultImpact=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rate=
        st.integers(),
    faultProbability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timeMin=
        safe_text
)
Place_strategy = st.builds(
    Place,
)
guigraph::NoWidgetNode_strategy = st.builds(
    guigraph::NoWidgetNode,
)
Widget_strategy = st.builds(
    Widget,
)
guigraph::Form_strategy = st.builds(
    guigraph::Form,
)
GuiGraph_strategy = st.builds(
    GuiGraph,
)
guigraph::Page_strategy = st.builds(
    guigraph::Page,
)
ITimeConsumer_strategy = st.builds(
    ITimeConsumer,
)
Predicate_strategy = st.builds(
    Predicate,
)
guigraph::PreGenerationSequence_strategy = st.builds(
    guigraph::PreGenerationSequence,
)
Transition_strategy = st.builds(
    Transition,
)
guigraph::TimerTransition_strategy = st.builds(
    guigraph::TimerTransition,
    duration=
        st.integers()
)
guigraph::PageTransition_strategy = st.builds(
    guigraph::PageTransition,
)
guigraph::ConditionActionTransition_strategy = st.builds(
    guigraph::ConditionActionTransition,
    actionsText=
        safe_text,
    applicationConditionText=
        safe_text
)
AbstractModelElement_strategy = st.builds(
    AbstractModelElement,
)
guigraph::GuiGraphNode_strategy = st.builds(
    guigraph::GuiGraphNode,
)
guigraph::Widget_strategy = st.builds(
    guigraph::Widget,
    image=
        safe_text
)
guigraph::GuiGraph_strategy = st.builds(
    guigraph::GuiGraph,
    invariantText=
        safe_text
)
guigraph::Arc_strategy = st.builds(
    guigraph::Arc,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=guigraph::InhibitorArc_strategy)
@settings(max_examples=50)
def test_guigraph::inhibitorarc_instantiation(instance):
    assert isinstance(instance, guigraph::InhibitorArc)

@given(instance=guigraph::StandardArc_strategy)
@settings(max_examples=50)
def test_guigraph::standardarc_instantiation(instance):
    assert isinstance(instance, guigraph::StandardArc)

@given(instance=guigraph::StandardArc_strategy)
def test_guigraph::standardarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=guigraph::StandardArc_strategy)
def test_guigraph::standardarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=rules::IRealTimeConsumer_strategy)
@settings(max_examples=50)
def test_rules::irealtimeconsumer_instantiation(instance):
    assert isinstance(instance, rules::IRealTimeConsumer)

@given(instance=GuiGraphNode_strategy)
@settings(max_examples=50)
def test_guigraphnode_instantiation(instance):
    assert isinstance(instance, GuiGraphNode)

@given(instance=guigraph::Place_strategy)
@settings(max_examples=50)
def test_guigraph::place_instantiation(instance):
    assert isinstance(instance, guigraph::Place)

@given(instance=guigraph::Place_strategy)
def test_guigraph::place_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=guigraph::Place_strategy)
def test_guigraph::place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=guigraph::Transition_strategy)
@settings(max_examples=50)
def test_guigraph::transition_instantiation(instance):
    assert isinstance(instance, guigraph::Transition)

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timingType_type(instance):
    assert isinstance(instance.timingType, str)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timingType_setter(instance):
    original = instance.timingType
    instance.timingType = original
    assert instance.timingType == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timeMax_type(instance):
    assert isinstance(instance.timeMax, str)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timeMax_setter(instance):
    original = instance.timeMax
    instance.timeMax = original
    assert instance.timeMax == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_terminates_type(instance):
    assert isinstance(instance.terminates, bool)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_terminates_setter(instance):
    original = instance.terminates
    instance.terminates = original
    assert instance.terminates == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_faultImpact_type(instance):
    assert isinstance(instance.faultImpact, float)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_faultImpact_setter(instance):
    original = instance.faultImpact
    instance.faultImpact = original
    assert instance.faultImpact == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_rate_type(instance):
    assert isinstance(instance.rate, int)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_faultProbability_type(instance):
    assert isinstance(instance.faultProbability, float)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_faultProbability_setter(instance):
    original = instance.faultProbability
    instance.faultProbability = original
    assert instance.faultProbability == original

@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timeMin_type(instance):
    assert isinstance(instance.timeMin, str)


@given(instance=guigraph::Transition_strategy)
def test_guigraph::transition_timeMin_setter(instance):
    original = instance.timeMin
    instance.timeMin = original
    assert instance.timeMin == original

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=guigraph::NoWidgetNode_strategy)
@settings(max_examples=50)
def test_guigraph::nowidgetnode_instantiation(instance):
    assert isinstance(instance, guigraph::NoWidgetNode)

@given(instance=Widget_strategy)
@settings(max_examples=50)
def test_widget_instantiation(instance):
    assert isinstance(instance, Widget)

@given(instance=guigraph::Form_strategy)
@settings(max_examples=50)
def test_guigraph::form_instantiation(instance):
    assert isinstance(instance, guigraph::Form)

@given(instance=GuiGraph_strategy)
@settings(max_examples=50)
def test_guigraph_instantiation(instance):
    assert isinstance(instance, GuiGraph)

@given(instance=guigraph::Page_strategy)
@settings(max_examples=50)
def test_guigraph::page_instantiation(instance):
    assert isinstance(instance, guigraph::Page)

@given(instance=ITimeConsumer_strategy)
@settings(max_examples=50)
def test_itimeconsumer_instantiation(instance):
    assert isinstance(instance, ITimeConsumer)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=guigraph::PreGenerationSequence_strategy)
@settings(max_examples=50)
def test_guigraph::pregenerationsequence_instantiation(instance):
    assert isinstance(instance, guigraph::PreGenerationSequence)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=guigraph::TimerTransition_strategy)
@settings(max_examples=50)
def test_guigraph::timertransition_instantiation(instance):
    assert isinstance(instance, guigraph::TimerTransition)

@given(instance=guigraph::TimerTransition_strategy)
def test_guigraph::timertransition_duration_type(instance):
    assert isinstance(instance.duration, int)


@given(instance=guigraph::TimerTransition_strategy)
def test_guigraph::timertransition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=guigraph::PageTransition_strategy)
@settings(max_examples=50)
def test_guigraph::pagetransition_instantiation(instance):
    assert isinstance(instance, guigraph::PageTransition)

@given(instance=guigraph::ConditionActionTransition_strategy)
@settings(max_examples=50)
def test_guigraph::conditionactiontransition_instantiation(instance):
    assert isinstance(instance, guigraph::ConditionActionTransition)

@given(instance=guigraph::ConditionActionTransition_strategy)
def test_guigraph::conditionactiontransition_actionsText_type(instance):
    assert isinstance(instance.actionsText, str)


@given(instance=guigraph::ConditionActionTransition_strategy)
def test_guigraph::conditionactiontransition_actionsText_setter(instance):
    original = instance.actionsText
    instance.actionsText = original
    assert instance.actionsText == original

@given(instance=guigraph::ConditionActionTransition_strategy)
def test_guigraph::conditionactiontransition_applicationConditionText_type(instance):
    assert isinstance(instance.applicationConditionText, str)


@given(instance=guigraph::ConditionActionTransition_strategy)
def test_guigraph::conditionactiontransition_applicationConditionText_setter(instance):
    original = instance.applicationConditionText
    instance.applicationConditionText = original
    assert instance.applicationConditionText == original

@given(instance=AbstractModelElement_strategy)
@settings(max_examples=50)
def test_abstractmodelelement_instantiation(instance):
    assert isinstance(instance, AbstractModelElement)

@given(instance=guigraph::GuiGraphNode_strategy)
@settings(max_examples=50)
def test_guigraph::guigraphnode_instantiation(instance):
    assert isinstance(instance, guigraph::GuiGraphNode)

@given(instance=guigraph::Widget_strategy)
@settings(max_examples=50)
def test_guigraph::widget_instantiation(instance):
    assert isinstance(instance, guigraph::Widget)

@given(instance=guigraph::Widget_strategy)
def test_guigraph::widget_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=guigraph::Widget_strategy)
def test_guigraph::widget_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=guigraph::GuiGraph_strategy)
@settings(max_examples=50)
def test_guigraph::guigraph_instantiation(instance):
    assert isinstance(instance, guigraph::GuiGraph)

@given(instance=guigraph::GuiGraph_strategy)
def test_guigraph::guigraph_invariantText_type(instance):
    assert isinstance(instance.invariantText, str)


@given(instance=guigraph::GuiGraph_strategy)
def test_guigraph::guigraph_invariantText_setter(instance):
    original = instance.invariantText
    instance.invariantText = original
    assert instance.invariantText == original

@given(instance=guigraph::Arc_strategy)
@settings(max_examples=50)
def test_guigraph::arc_instantiation(instance):
    assert isinstance(instance, guigraph::Arc)

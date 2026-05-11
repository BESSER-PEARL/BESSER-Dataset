import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Message,
    behavior::AlternativeMessage,
    behavior::OptionalMessage,
    ExecutionSpecification,
    MessageEnd,
    OccurrenceSpecification,
    behavior::ExecutionOccurrenceSpecification,
    behavior::MessageOccurrenceSpecification,
    Event,
    behavior::ExecutionEvent,
    behavior::CreatEvent,
    RedefinableElement,
    InteractionFragment,
    behavior::OccurrenceSpecification,
    behavior::ExecutionSpecification,
    Behavior,
    behavior::BehaviorExecutionSpecification,
    behavior::Interaction,
    behavior::Element,
    BehavioredClassifier,
    behavior::Object,
    behavior::Class,
    Object,
    behavior::Actor,
    behavior::Feature,
    Namespace,
    behavior::Classifier,
    behavior::DestructionEvent,
    Class,
    Element,
    behavior::Comment,
    behavior::NamedElement,
    BehavioralFeature,
    behavior::Operation,
    behavior::Behavior,
    NamedElement,
    behavior::RedefinableElement,
    behavior::Message,
    behavior::Event,
    behavior::InteractionFragment,
    behavior::Namespace,
    behavior::MessageEnd,
    behavior::GeneralOrdering,
    behavior::Lifeline,
    Feature,
    behavior::Connector,
    behavior::BehavioralFeature,
    Classifier,
    behavior::BehavioredClassifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_behavior::alternativemessage_is_not_abstract():
    assert not inspect.isabstract(behavior::AlternativeMessage)


def test_behavior::alternativemessage_constructor_exists():
    assert callable(behavior::AlternativeMessage.__init__)


def test_behavior::alternativemessage_constructor_args():
    sig = inspect.signature(behavior::AlternativeMessage.__init__)
    params = list(sig.parameters.keys())



def test_behavior::optionalmessage_is_not_abstract():
    assert not inspect.isabstract(behavior::OptionalMessage)


def test_behavior::optionalmessage_constructor_exists():
    assert callable(behavior::OptionalMessage.__init__)


def test_behavior::optionalmessage_constructor_args():
    sig = inspect.signature(behavior::OptionalMessage.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavior::executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(behavior::ExecutionOccurrenceSpecification)


def test_behavior::executionoccurrencespecification_constructor_exists():
    assert callable(behavior::ExecutionOccurrenceSpecification.__init__)


def test_behavior::executionoccurrencespecification_constructor_args():
    sig = inspect.signature(behavior::ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavior::messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(behavior::MessageOccurrenceSpecification)


def test_behavior::messageoccurrencespecification_constructor_exists():
    assert callable(behavior::MessageOccurrenceSpecification.__init__)


def test_behavior::messageoccurrencespecification_constructor_args():
    sig = inspect.signature(behavior::MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_behavior::executionevent_is_not_abstract():
    assert not inspect.isabstract(behavior::ExecutionEvent)


def test_behavior::executionevent_constructor_exists():
    assert callable(behavior::ExecutionEvent.__init__)


def test_behavior::executionevent_constructor_args():
    sig = inspect.signature(behavior::ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_behavior::createvent_is_not_abstract():
    assert not inspect.isabstract(behavior::CreatEvent)


def test_behavior::createvent_constructor_exists():
    assert callable(behavior::CreatEvent.__init__)


def test_behavior::createvent_constructor_args():
    sig = inspect.signature(behavior::CreatEvent.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_behavior::occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(behavior::OccurrenceSpecification)


def test_behavior::occurrencespecification_constructor_exists():
    assert callable(behavior::OccurrenceSpecification.__init__)


def test_behavior::occurrencespecification_constructor_args():
    sig = inspect.signature(behavior::OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavior::executionspecification_is_not_abstract():
    assert not inspect.isabstract(behavior::ExecutionSpecification)


def test_behavior::executionspecification_constructor_exists():
    assert callable(behavior::ExecutionSpecification.__init__)


def test_behavior::executionspecification_constructor_args():
    sig = inspect.signature(behavior::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_behavior::behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(behavior::BehaviorExecutionSpecification)


def test_behavior::behaviorexecutionspecification_constructor_exists():
    assert callable(behavior::BehaviorExecutionSpecification.__init__)


def test_behavior::behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(behavior::BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavior::interaction_is_not_abstract():
    assert not inspect.isabstract(behavior::Interaction)


def test_behavior::interaction_constructor_exists():
    assert callable(behavior::Interaction.__init__)


def test_behavior::interaction_constructor_args():
    sig = inspect.signature(behavior::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_behavior::element_is_not_abstract():
    assert not inspect.isabstract(behavior::Element)


def test_behavior::element_constructor_exists():
    assert callable(behavior::Element.__init__)


def test_behavior::element_constructor_args():
    sig = inspect.signature(behavior::Element.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavior::object_is_not_abstract():
    assert not inspect.isabstract(behavior::Object)


def test_behavior::object_constructor_exists():
    assert callable(behavior::Object.__init__)


def test_behavior::object_constructor_args():
    sig = inspect.signature(behavior::Object.__init__)
    params = list(sig.parameters.keys())



def test_behavior::class_is_not_abstract():
    assert not inspect.isabstract(behavior::Class)


def test_behavior::class_constructor_exists():
    assert callable(behavior::Class.__init__)


def test_behavior::class_constructor_args():
    sig = inspect.signature(behavior::Class.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_behavior::actor_is_not_abstract():
    assert not inspect.isabstract(behavior::Actor)


def test_behavior::actor_constructor_exists():
    assert callable(behavior::Actor.__init__)


def test_behavior::actor_constructor_args():
    sig = inspect.signature(behavior::Actor.__init__)
    params = list(sig.parameters.keys())



def test_behavior::feature_is_not_abstract():
    assert not inspect.isabstract(behavior::Feature)


def test_behavior::feature_constructor_exists():
    assert callable(behavior::Feature.__init__)


def test_behavior::feature_constructor_args():
    sig = inspect.signature(behavior::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_behavior::feature_has_isStatic():
    assert hasattr(behavior::Feature, "isStatic")
    descriptor = None
    for klass in behavior::Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_behavior::classifier_is_not_abstract():
    assert not inspect.isabstract(behavior::Classifier)


def test_behavior::classifier_constructor_exists():
    assert callable(behavior::Classifier.__init__)


def test_behavior::classifier_constructor_args():
    sig = inspect.signature(behavior::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_behavior::classifier_has_isAbstract():
    assert hasattr(behavior::Classifier, "isAbstract")
    descriptor = None
    for klass in behavior::Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_behavior::destructionevent_is_not_abstract():
    assert not inspect.isabstract(behavior::DestructionEvent)


def test_behavior::destructionevent_constructor_exists():
    assert callable(behavior::DestructionEvent.__init__)


def test_behavior::destructionevent_constructor_args():
    sig = inspect.signature(behavior::DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_behavior::comment_is_not_abstract():
    assert not inspect.isabstract(behavior::Comment)


def test_behavior::comment_constructor_exists():
    assert callable(behavior::Comment.__init__)


def test_behavior::comment_constructor_args():
    sig = inspect.signature(behavior::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_behavior::comment_has_body():
    assert hasattr(behavior::Comment, "body")
    descriptor = None
    for klass in behavior::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_behavior::namedelement_is_not_abstract():
    assert not inspect.isabstract(behavior::NamedElement)


def test_behavior::namedelement_constructor_exists():
    assert callable(behavior::NamedElement.__init__)


def test_behavior::namedelement_constructor_args():
    sig = inspect.signature(behavior::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "Archpoint" in params, "Missing parameter 'Archpoint'"
    assert "name" in params, "Missing parameter 'name'"

def test_behavior::namedelement_has_Archpoint():
    assert hasattr(behavior::NamedElement, "Archpoint")
    descriptor = None
    for klass in behavior::NamedElement.__mro__:
        if "Archpoint" in klass.__dict__:
            descriptor = klass.__dict__["Archpoint"]
            break
    assert isinstance(descriptor, property)

def test_behavior::namedelement_has_name():
    assert hasattr(behavior::NamedElement, "name")
    descriptor = None
    for klass in behavior::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_behavior::operation_is_not_abstract():
    assert not inspect.isabstract(behavior::Operation)


def test_behavior::operation_constructor_exists():
    assert callable(behavior::Operation.__init__)


def test_behavior::operation_constructor_args():
    sig = inspect.signature(behavior::Operation.__init__)
    params = list(sig.parameters.keys())



def test_behavior::behavior_is_not_abstract():
    assert not inspect.isabstract(behavior::Behavior)


def test_behavior::behavior_constructor_exists():
    assert callable(behavior::Behavior.__init__)


def test_behavior::behavior_constructor_args():
    sig = inspect.signature(behavior::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behavior::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(behavior::RedefinableElement)


def test_behavior::redefinableelement_constructor_exists():
    assert callable(behavior::RedefinableElement.__init__)


def test_behavior::redefinableelement_constructor_args():
    sig = inspect.signature(behavior::RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavior::message_is_not_abstract():
    assert not inspect.isabstract(behavior::Message)


def test_behavior::message_constructor_exists():
    assert callable(behavior::Message.__init__)


def test_behavior::message_constructor_args():
    sig = inspect.signature(behavior::Message.__init__)
    params = list(sig.parameters.keys())
    assert "MessageOrder" in params, "Missing parameter 'MessageOrder'"

def test_behavior::message_has_MessageOrder():
    assert hasattr(behavior::Message, "MessageOrder")
    descriptor = None
    for klass in behavior::Message.__mro__:
        if "MessageOrder" in klass.__dict__:
            descriptor = klass.__dict__["MessageOrder"]
            break
    assert isinstance(descriptor, property)



def test_behavior::event_is_not_abstract():
    assert not inspect.isabstract(behavior::Event)


def test_behavior::event_constructor_exists():
    assert callable(behavior::Event.__init__)


def test_behavior::event_constructor_args():
    sig = inspect.signature(behavior::Event.__init__)
    params = list(sig.parameters.keys())



def test_behavior::interactionfragment_is_not_abstract():
    assert not inspect.isabstract(behavior::InteractionFragment)


def test_behavior::interactionfragment_constructor_exists():
    assert callable(behavior::InteractionFragment.__init__)


def test_behavior::interactionfragment_constructor_args():
    sig = inspect.signature(behavior::InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_behavior::namespace_is_not_abstract():
    assert not inspect.isabstract(behavior::Namespace)


def test_behavior::namespace_constructor_exists():
    assert callable(behavior::Namespace.__init__)


def test_behavior::namespace_constructor_args():
    sig = inspect.signature(behavior::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_behavior::messageend_is_not_abstract():
    assert not inspect.isabstract(behavior::MessageEnd)


def test_behavior::messageend_constructor_exists():
    assert callable(behavior::MessageEnd.__init__)


def test_behavior::messageend_constructor_args():
    sig = inspect.signature(behavior::MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_behavior::generalordering_is_not_abstract():
    assert not inspect.isabstract(behavior::GeneralOrdering)


def test_behavior::generalordering_constructor_exists():
    assert callable(behavior::GeneralOrdering.__init__)


def test_behavior::generalordering_constructor_args():
    sig = inspect.signature(behavior::GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_behavior::lifeline_is_not_abstract():
    assert not inspect.isabstract(behavior::Lifeline)


def test_behavior::lifeline_constructor_exists():
    assert callable(behavior::Lifeline.__init__)


def test_behavior::lifeline_constructor_args():
    sig = inspect.signature(behavior::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_behavior::connector_is_not_abstract():
    assert not inspect.isabstract(behavior::Connector)


def test_behavior::connector_constructor_exists():
    assert callable(behavior::Connector.__init__)


def test_behavior::connector_constructor_args():
    sig = inspect.signature(behavior::Connector.__init__)
    params = list(sig.parameters.keys())



def test_behavior::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(behavior::BehavioralFeature)


def test_behavior::behavioralfeature_constructor_exists():
    assert callable(behavior::BehavioralFeature.__init__)


def test_behavior::behavioralfeature_constructor_args():
    sig = inspect.signature(behavior::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_behavior::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(behavior::BehavioredClassifier)


def test_behavior::behavioredclassifier_constructor_exists():
    assert callable(behavior::BehavioredClassifier.__init__)


def test_behavior::behavioredclassifier_constructor_args():
    sig = inspect.signature(behavior::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())


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
Message_strategy = st.builds(
    Message,
)
behavior::AlternativeMessage_strategy = st.builds(
    behavior::AlternativeMessage,
)
behavior::OptionalMessage_strategy = st.builds(
    behavior::OptionalMessage,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
behavior::ExecutionOccurrenceSpecification_strategy = st.builds(
    behavior::ExecutionOccurrenceSpecification,
)
behavior::MessageOccurrenceSpecification_strategy = st.builds(
    behavior::MessageOccurrenceSpecification,
)
Event_strategy = st.builds(
    Event,
)
behavior::ExecutionEvent_strategy = st.builds(
    behavior::ExecutionEvent,
)
behavior::CreatEvent_strategy = st.builds(
    behavior::CreatEvent,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
behavior::OccurrenceSpecification_strategy = st.builds(
    behavior::OccurrenceSpecification,
)
behavior::ExecutionSpecification_strategy = st.builds(
    behavior::ExecutionSpecification,
)
Behavior_strategy = st.builds(
    Behavior,
)
behavior::BehaviorExecutionSpecification_strategy = st.builds(
    behavior::BehaviorExecutionSpecification,
)
behavior::Interaction_strategy = st.builds(
    behavior::Interaction,
)
behavior::Element_strategy = st.builds(
    behavior::Element,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
behavior::Object_strategy = st.builds(
    behavior::Object,
)
behavior::Class_strategy = st.builds(
    behavior::Class,
)
Object_strategy = st.builds(
    Object,
)
behavior::Actor_strategy = st.builds(
    behavior::Actor,
)
behavior::Feature_strategy = st.builds(
    behavior::Feature,
    isStatic=
        st.booleans()
)
Namespace_strategy = st.builds(
    Namespace,
)
behavior::Classifier_strategy = st.builds(
    behavior::Classifier,
    isAbstract=
        st.booleans()
)
behavior::DestructionEvent_strategy = st.builds(
    behavior::DestructionEvent,
)
Class_strategy = st.builds(
    Class,
)
Element_strategy = st.builds(
    Element,
)
behavior::Comment_strategy = st.builds(
    behavior::Comment,
    body=
        safe_text
)
behavior::NamedElement_strategy = st.builds(
    behavior::NamedElement,
    Archpoint=
        st.booleans(),
    name=
        safe_text
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
behavior::Operation_strategy = st.builds(
    behavior::Operation,
)
behavior::Behavior_strategy = st.builds(
    behavior::Behavior,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behavior::RedefinableElement_strategy = st.builds(
    behavior::RedefinableElement,
)
behavior::Message_strategy = st.builds(
    behavior::Message,
    MessageOrder=
        st.integers()
)
behavior::Event_strategy = st.builds(
    behavior::Event,
)
behavior::InteractionFragment_strategy = st.builds(
    behavior::InteractionFragment,
)
behavior::Namespace_strategy = st.builds(
    behavior::Namespace,
)
behavior::MessageEnd_strategy = st.builds(
    behavior::MessageEnd,
)
behavior::GeneralOrdering_strategy = st.builds(
    behavior::GeneralOrdering,
)
behavior::Lifeline_strategy = st.builds(
    behavior::Lifeline,
)
Feature_strategy = st.builds(
    Feature,
)
behavior::Connector_strategy = st.builds(
    behavior::Connector,
)
behavior::BehavioralFeature_strategy = st.builds(
    behavior::BehavioralFeature,
)
Classifier_strategy = st.builds(
    Classifier,
)
behavior::BehavioredClassifier_strategy = st.builds(
    behavior::BehavioredClassifier,
)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=behavior::AlternativeMessage_strategy)
@settings(max_examples=50)
def test_behavior::alternativemessage_instantiation(instance):
    assert isinstance(instance, behavior::AlternativeMessage)

@given(instance=behavior::OptionalMessage_strategy)
@settings(max_examples=50)
def test_behavior::optionalmessage_instantiation(instance):
    assert isinstance(instance, behavior::OptionalMessage)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=behavior::ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_behavior::executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, behavior::ExecutionOccurrenceSpecification)

@given(instance=behavior::MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_behavior::messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, behavior::MessageOccurrenceSpecification)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=behavior::ExecutionEvent_strategy)
@settings(max_examples=50)
def test_behavior::executionevent_instantiation(instance):
    assert isinstance(instance, behavior::ExecutionEvent)

@given(instance=behavior::CreatEvent_strategy)
@settings(max_examples=50)
def test_behavior::createvent_instantiation(instance):
    assert isinstance(instance, behavior::CreatEvent)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=behavior::OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_behavior::occurrencespecification_instantiation(instance):
    assert isinstance(instance, behavior::OccurrenceSpecification)

@given(instance=behavior::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_behavior::executionspecification_instantiation(instance):
    assert isinstance(instance, behavior::ExecutionSpecification)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=behavior::BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_behavior::behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, behavior::BehaviorExecutionSpecification)

@given(instance=behavior::Interaction_strategy)
@settings(max_examples=50)
def test_behavior::interaction_instantiation(instance):
    assert isinstance(instance, behavior::Interaction)

@given(instance=behavior::Element_strategy)
@settings(max_examples=50)
def test_behavior::element_instantiation(instance):
    assert isinstance(instance, behavior::Element)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=behavior::Object_strategy)
@settings(max_examples=50)
def test_behavior::object_instantiation(instance):
    assert isinstance(instance, behavior::Object)

@given(instance=behavior::Class_strategy)
@settings(max_examples=50)
def test_behavior::class_instantiation(instance):
    assert isinstance(instance, behavior::Class)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=behavior::Actor_strategy)
@settings(max_examples=50)
def test_behavior::actor_instantiation(instance):
    assert isinstance(instance, behavior::Actor)

@given(instance=behavior::Feature_strategy)
@settings(max_examples=50)
def test_behavior::feature_instantiation(instance):
    assert isinstance(instance, behavior::Feature)

@given(instance=behavior::Feature_strategy)
def test_behavior::feature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=behavior::Feature_strategy)
def test_behavior::feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=behavior::Classifier_strategy)
@settings(max_examples=50)
def test_behavior::classifier_instantiation(instance):
    assert isinstance(instance, behavior::Classifier)

@given(instance=behavior::Classifier_strategy)
def test_behavior::classifier_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=behavior::Classifier_strategy)
def test_behavior::classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=behavior::DestructionEvent_strategy)
@settings(max_examples=50)
def test_behavior::destructionevent_instantiation(instance):
    assert isinstance(instance, behavior::DestructionEvent)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=behavior::Comment_strategy)
@settings(max_examples=50)
def test_behavior::comment_instantiation(instance):
    assert isinstance(instance, behavior::Comment)

@given(instance=behavior::Comment_strategy)
def test_behavior::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=behavior::Comment_strategy)
def test_behavior::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=behavior::NamedElement_strategy)
@settings(max_examples=50)
def test_behavior::namedelement_instantiation(instance):
    assert isinstance(instance, behavior::NamedElement)

@given(instance=behavior::NamedElement_strategy)
def test_behavior::namedelement_Archpoint_type(instance):
    assert isinstance(instance.Archpoint, bool)


@given(instance=behavior::NamedElement_strategy)
def test_behavior::namedelement_Archpoint_setter(instance):
    original = instance.Archpoint
    instance.Archpoint = original
    assert instance.Archpoint == original

@given(instance=behavior::NamedElement_strategy)
def test_behavior::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behavior::NamedElement_strategy)
def test_behavior::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=behavior::Operation_strategy)
@settings(max_examples=50)
def test_behavior::operation_instantiation(instance):
    assert isinstance(instance, behavior::Operation)

@given(instance=behavior::Behavior_strategy)
@settings(max_examples=50)
def test_behavior::behavior_instantiation(instance):
    assert isinstance(instance, behavior::Behavior)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behavior::RedefinableElement_strategy)
@settings(max_examples=50)
def test_behavior::redefinableelement_instantiation(instance):
    assert isinstance(instance, behavior::RedefinableElement)

@given(instance=behavior::Message_strategy)
@settings(max_examples=50)
def test_behavior::message_instantiation(instance):
    assert isinstance(instance, behavior::Message)

@given(instance=behavior::Message_strategy)
def test_behavior::message_MessageOrder_type(instance):
    assert isinstance(instance.MessageOrder, int)


@given(instance=behavior::Message_strategy)
def test_behavior::message_MessageOrder_setter(instance):
    original = instance.MessageOrder
    instance.MessageOrder = original
    assert instance.MessageOrder == original

@given(instance=behavior::Event_strategy)
@settings(max_examples=50)
def test_behavior::event_instantiation(instance):
    assert isinstance(instance, behavior::Event)

@given(instance=behavior::InteractionFragment_strategy)
@settings(max_examples=50)
def test_behavior::interactionfragment_instantiation(instance):
    assert isinstance(instance, behavior::InteractionFragment)

@given(instance=behavior::Namespace_strategy)
@settings(max_examples=50)
def test_behavior::namespace_instantiation(instance):
    assert isinstance(instance, behavior::Namespace)

@given(instance=behavior::MessageEnd_strategy)
@settings(max_examples=50)
def test_behavior::messageend_instantiation(instance):
    assert isinstance(instance, behavior::MessageEnd)

@given(instance=behavior::GeneralOrdering_strategy)
@settings(max_examples=50)
def test_behavior::generalordering_instantiation(instance):
    assert isinstance(instance, behavior::GeneralOrdering)

@given(instance=behavior::Lifeline_strategy)
@settings(max_examples=50)
def test_behavior::lifeline_instantiation(instance):
    assert isinstance(instance, behavior::Lifeline)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=behavior::Connector_strategy)
@settings(max_examples=50)
def test_behavior::connector_instantiation(instance):
    assert isinstance(instance, behavior::Connector)

@given(instance=behavior::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavior::behavioralfeature_instantiation(instance):
    assert isinstance(instance, behavior::BehavioralFeature)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=behavior::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavior::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, behavior::BehavioredClassifier)

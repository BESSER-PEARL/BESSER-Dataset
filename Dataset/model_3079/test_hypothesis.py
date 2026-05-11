import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    adaptations::smartadapters4MODERATES::ActionBlock,
    adaptations::smartadapters4MODERATES::PlatformAnnotation,
    adaptations::smartadapters4MODERATES::AnnotatedElement,
    adaptations::smartadapters4MODERATES::Expression,
    adaptations::smartadapters4MODERATES::Event,
    adaptations::smartadapters4MODERATES::Property,
    adaptations::smartadapters4MODERATES::Action,
    adaptations::smartadapters4MODERATES::Transition,
    smartadapters4MODERATES::Adaptation,
    UnsetAdaptation,
    smartadapters4MODERATES::adaptations::UnsetState,
    smartadapters4MODERATES::adaptations::UnsetTransition,
    smartadapters4MODERATES::adaptations::UnsetCompositeState,
    adaptations::smartadapters4MODERATES::State,
    adaptations::smartadapters4MODERATES::CompositeState,
    SetAdaptation,
    smartadapters4MODERATES::adaptations::SetTransition,
    smartadapters4MODERATES::adaptations::SetAnnotatedElement,
    smartadapters4MODERATES::adaptations::SetState,
    smartadapters4MODERATES::adaptations::SetActionBlock,
    smartadapters4MODERATES::adaptations::SetCompositeState,
    ScopedInstantiation,
    smartadapters4MODERATES::PerElementMatch,
    smartadapters4MODERATES::PerRoleMatch,
    InstantiationStrategy,
    smartadapters4MODERATES::ScopedInstantiation,
    smartadapters4MODERATES::GlobalInstantiation,
    smartadapters4MODERATES::AspectModelElement,
    Adaptation,
    smartadapters4MODERATES::SetAdaptation,
    smartadapters4MODERATES::UnsetAdaptation,
    smartadapters4MODERATES::CreateAdaptation,
    smartadapters4MODERATES::CloneAdaptation,
    smartadapters4MODERATES::InstantiationStrategy,
    smartadapters4MODERATES::AdviceModel,
    smartadapters4MODERATES::PointcutModel,
    smartadapters4MODERATES::Aspect,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adaptations::smartadapters4moderates::actionblock_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::ActionBlock)


def test_adaptations::smartadapters4moderates::actionblock_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::ActionBlock.__init__)


def test_adaptations::smartadapters4moderates::actionblock_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::platformannotation_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::PlatformAnnotation)


def test_adaptations::smartadapters4moderates::platformannotation_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::PlatformAnnotation.__init__)


def test_adaptations::smartadapters4moderates::platformannotation_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::annotatedelement_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::AnnotatedElement)


def test_adaptations::smartadapters4moderates::annotatedelement_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::AnnotatedElement.__init__)


def test_adaptations::smartadapters4moderates::annotatedelement_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::expression_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::Expression)


def test_adaptations::smartadapters4moderates::expression_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::Expression.__init__)


def test_adaptations::smartadapters4moderates::expression_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::Expression.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::event_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::Event)


def test_adaptations::smartadapters4moderates::event_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::Event.__init__)


def test_adaptations::smartadapters4moderates::event_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::Event.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::property_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::Property)


def test_adaptations::smartadapters4moderates::property_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::Property.__init__)


def test_adaptations::smartadapters4moderates::property_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::Property.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::action_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::Action)


def test_adaptations::smartadapters4moderates::action_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::Action.__init__)


def test_adaptations::smartadapters4moderates::action_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::Action.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::transition_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::Transition)


def test_adaptations::smartadapters4moderates::transition_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::Transition.__init__)


def test_adaptations::smartadapters4moderates::transition_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::Transition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::Adaptation)


def test_smartadapters4moderates::adaptation_constructor_exists():
    assert callable(smartadapters4MODERATES::Adaptation.__init__)


def test_smartadapters4moderates::adaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::Adaptation.__init__)
    params = list(sig.parameters.keys())



def test_unsetadaptation_is_not_abstract():
    assert not inspect.isabstract(UnsetAdaptation)


def test_unsetadaptation_constructor_exists():
    assert callable(UnsetAdaptation.__init__)


def test_unsetadaptation_constructor_args():
    sig = inspect.signature(UnsetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::unsetstate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::UnsetState)


def test_smartadapters4moderates::adaptations::unsetstate_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::UnsetState.__init__)


def test_smartadapters4moderates::adaptations::unsetstate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::UnsetState.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::unsettransition_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::UnsetTransition)


def test_smartadapters4moderates::adaptations::unsettransition_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::UnsetTransition.__init__)


def test_smartadapters4moderates::adaptations::unsettransition_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::UnsetTransition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::unsetcompositestate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::UnsetCompositeState)


def test_smartadapters4moderates::adaptations::unsetcompositestate_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::UnsetCompositeState.__init__)


def test_smartadapters4moderates::adaptations::unsetcompositestate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::UnsetCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::state_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::State)


def test_adaptations::smartadapters4moderates::state_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::State.__init__)


def test_adaptations::smartadapters4moderates::state_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::State.__init__)
    params = list(sig.parameters.keys())



def test_adaptations::smartadapters4moderates::compositestate_is_not_abstract():
    assert not inspect.isabstract(adaptations::smartadapters4MODERATES::CompositeState)


def test_adaptations::smartadapters4moderates::compositestate_constructor_exists():
    assert callable(adaptations::smartadapters4MODERATES::CompositeState.__init__)


def test_adaptations::smartadapters4moderates::compositestate_constructor_args():
    sig = inspect.signature(adaptations::smartadapters4MODERATES::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_setadaptation_is_not_abstract():
    assert not inspect.isabstract(SetAdaptation)


def test_setadaptation_constructor_exists():
    assert callable(SetAdaptation.__init__)


def test_setadaptation_constructor_args():
    sig = inspect.signature(SetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::settransition_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::SetTransition)


def test_smartadapters4moderates::adaptations::settransition_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::SetTransition.__init__)


def test_smartadapters4moderates::adaptations::settransition_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::SetTransition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::setannotatedelement_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::SetAnnotatedElement)


def test_smartadapters4moderates::adaptations::setannotatedelement_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::SetAnnotatedElement.__init__)


def test_smartadapters4moderates::adaptations::setannotatedelement_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::SetAnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::setstate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::SetState)


def test_smartadapters4moderates::adaptations::setstate_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::SetState.__init__)


def test_smartadapters4moderates::adaptations::setstate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::SetState.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::setactionblock_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::SetActionBlock)


def test_smartadapters4moderates::adaptations::setactionblock_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::SetActionBlock.__init__)


def test_smartadapters4moderates::adaptations::setactionblock_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::SetActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::adaptations::setcompositestate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::adaptations::SetCompositeState)


def test_smartadapters4moderates::adaptations::setcompositestate_constructor_exists():
    assert callable(smartadapters4MODERATES::adaptations::SetCompositeState.__init__)


def test_smartadapters4moderates::adaptations::setcompositestate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::adaptations::SetCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_scopedinstantiation_is_not_abstract():
    assert not inspect.isabstract(ScopedInstantiation)


def test_scopedinstantiation_constructor_exists():
    assert callable(ScopedInstantiation.__init__)


def test_scopedinstantiation_constructor_args():
    sig = inspect.signature(ScopedInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::perelementmatch_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::PerElementMatch)


def test_smartadapters4moderates::perelementmatch_constructor_exists():
    assert callable(smartadapters4MODERATES::PerElementMatch.__init__)


def test_smartadapters4moderates::perelementmatch_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::PerElementMatch.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::perrolematch_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::PerRoleMatch)


def test_smartadapters4moderates::perrolematch_constructor_exists():
    assert callable(smartadapters4MODERATES::PerRoleMatch.__init__)


def test_smartadapters4moderates::perrolematch_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::PerRoleMatch.__init__)
    params = list(sig.parameters.keys())



def test_instantiationstrategy_is_not_abstract():
    assert not inspect.isabstract(InstantiationStrategy)


def test_instantiationstrategy_constructor_exists():
    assert callable(InstantiationStrategy.__init__)


def test_instantiationstrategy_constructor_args():
    sig = inspect.signature(InstantiationStrategy.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::scopedinstantiation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::ScopedInstantiation)


def test_smartadapters4moderates::scopedinstantiation_constructor_exists():
    assert callable(smartadapters4MODERATES::ScopedInstantiation.__init__)


def test_smartadapters4moderates::scopedinstantiation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::ScopedInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::globalinstantiation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::GlobalInstantiation)


def test_smartadapters4moderates::globalinstantiation_constructor_exists():
    assert callable(smartadapters4MODERATES::GlobalInstantiation.__init__)


def test_smartadapters4moderates::globalinstantiation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::GlobalInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::aspectmodelelement_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::AspectModelElement)


def test_smartadapters4moderates::aspectmodelelement_constructor_exists():
    assert callable(smartadapters4MODERATES::AspectModelElement.__init__)


def test_smartadapters4moderates::aspectmodelelement_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::AspectModelElement.__init__)
    params = list(sig.parameters.keys())



def test_adaptation_is_not_abstract():
    assert not inspect.isabstract(Adaptation)


def test_adaptation_constructor_exists():
    assert callable(Adaptation.__init__)


def test_adaptation_constructor_args():
    sig = inspect.signature(Adaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::setadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::SetAdaptation)


def test_smartadapters4moderates::setadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES::SetAdaptation.__init__)


def test_smartadapters4moderates::setadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::SetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::unsetadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::UnsetAdaptation)


def test_smartadapters4moderates::unsetadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES::UnsetAdaptation.__init__)


def test_smartadapters4moderates::unsetadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::UnsetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::createadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::CreateAdaptation)


def test_smartadapters4moderates::createadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES::CreateAdaptation.__init__)


def test_smartadapters4moderates::createadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::CreateAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::cloneadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::CloneAdaptation)


def test_smartadapters4moderates::cloneadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES::CloneAdaptation.__init__)


def test_smartadapters4moderates::cloneadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::CloneAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::instantiationstrategy_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::InstantiationStrategy)


def test_smartadapters4moderates::instantiationstrategy_constructor_exists():
    assert callable(smartadapters4MODERATES::InstantiationStrategy.__init__)


def test_smartadapters4moderates::instantiationstrategy_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::InstantiationStrategy.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::advicemodel_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::AdviceModel)


def test_smartadapters4moderates::advicemodel_constructor_exists():
    assert callable(smartadapters4MODERATES::AdviceModel.__init__)


def test_smartadapters4moderates::advicemodel_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::AdviceModel.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::pointcutmodel_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::PointcutModel)


def test_smartadapters4moderates::pointcutmodel_constructor_exists():
    assert callable(smartadapters4MODERATES::PointcutModel.__init__)


def test_smartadapters4moderates::pointcutmodel_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::PointcutModel.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates::aspect_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES::Aspect)


def test_smartadapters4moderates::aspect_constructor_exists():
    assert callable(smartadapters4MODERATES::Aspect.__init__)


def test_smartadapters4moderates::aspect_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES::Aspect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smartadapters4moderates::aspect_has_name():
    assert hasattr(smartadapters4MODERATES::Aspect, "name")
    descriptor = None
    for klass in smartadapters4MODERATES::Aspect.__mro__:
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
adaptations::smartadapters4MODERATES::ActionBlock_strategy = st.builds(
    adaptations::smartadapters4MODERATES::ActionBlock,
)
adaptations::smartadapters4MODERATES::PlatformAnnotation_strategy = st.builds(
    adaptations::smartadapters4MODERATES::PlatformAnnotation,
)
adaptations::smartadapters4MODERATES::AnnotatedElement_strategy = st.builds(
    adaptations::smartadapters4MODERATES::AnnotatedElement,
)
adaptations::smartadapters4MODERATES::Expression_strategy = st.builds(
    adaptations::smartadapters4MODERATES::Expression,
)
adaptations::smartadapters4MODERATES::Event_strategy = st.builds(
    adaptations::smartadapters4MODERATES::Event,
)
adaptations::smartadapters4MODERATES::Property_strategy = st.builds(
    adaptations::smartadapters4MODERATES::Property,
)
adaptations::smartadapters4MODERATES::Action_strategy = st.builds(
    adaptations::smartadapters4MODERATES::Action,
)
adaptations::smartadapters4MODERATES::Transition_strategy = st.builds(
    adaptations::smartadapters4MODERATES::Transition,
)
smartadapters4MODERATES::Adaptation_strategy = st.builds(
    smartadapters4MODERATES::Adaptation,
)
UnsetAdaptation_strategy = st.builds(
    UnsetAdaptation,
)
smartadapters4MODERATES::adaptations::UnsetState_strategy = st.builds(
    smartadapters4MODERATES::adaptations::UnsetState,
)
smartadapters4MODERATES::adaptations::UnsetTransition_strategy = st.builds(
    smartadapters4MODERATES::adaptations::UnsetTransition,
)
smartadapters4MODERATES::adaptations::UnsetCompositeState_strategy = st.builds(
    smartadapters4MODERATES::adaptations::UnsetCompositeState,
)
adaptations::smartadapters4MODERATES::State_strategy = st.builds(
    adaptations::smartadapters4MODERATES::State,
)
adaptations::smartadapters4MODERATES::CompositeState_strategy = st.builds(
    adaptations::smartadapters4MODERATES::CompositeState,
)
SetAdaptation_strategy = st.builds(
    SetAdaptation,
)
smartadapters4MODERATES::adaptations::SetTransition_strategy = st.builds(
    smartadapters4MODERATES::adaptations::SetTransition,
)
smartadapters4MODERATES::adaptations::SetAnnotatedElement_strategy = st.builds(
    smartadapters4MODERATES::adaptations::SetAnnotatedElement,
)
smartadapters4MODERATES::adaptations::SetState_strategy = st.builds(
    smartadapters4MODERATES::adaptations::SetState,
)
smartadapters4MODERATES::adaptations::SetActionBlock_strategy = st.builds(
    smartadapters4MODERATES::adaptations::SetActionBlock,
)
smartadapters4MODERATES::adaptations::SetCompositeState_strategy = st.builds(
    smartadapters4MODERATES::adaptations::SetCompositeState,
)
ScopedInstantiation_strategy = st.builds(
    ScopedInstantiation,
)
smartadapters4MODERATES::PerElementMatch_strategy = st.builds(
    smartadapters4MODERATES::PerElementMatch,
)
smartadapters4MODERATES::PerRoleMatch_strategy = st.builds(
    smartadapters4MODERATES::PerRoleMatch,
)
InstantiationStrategy_strategy = st.builds(
    InstantiationStrategy,
)
smartadapters4MODERATES::ScopedInstantiation_strategy = st.builds(
    smartadapters4MODERATES::ScopedInstantiation,
)
smartadapters4MODERATES::GlobalInstantiation_strategy = st.builds(
    smartadapters4MODERATES::GlobalInstantiation,
)
smartadapters4MODERATES::AspectModelElement_strategy = st.builds(
    smartadapters4MODERATES::AspectModelElement,
)
Adaptation_strategy = st.builds(
    Adaptation,
)
smartadapters4MODERATES::SetAdaptation_strategy = st.builds(
    smartadapters4MODERATES::SetAdaptation,
)
smartadapters4MODERATES::UnsetAdaptation_strategy = st.builds(
    smartadapters4MODERATES::UnsetAdaptation,
)
smartadapters4MODERATES::CreateAdaptation_strategy = st.builds(
    smartadapters4MODERATES::CreateAdaptation,
)
smartadapters4MODERATES::CloneAdaptation_strategy = st.builds(
    smartadapters4MODERATES::CloneAdaptation,
)
smartadapters4MODERATES::InstantiationStrategy_strategy = st.builds(
    smartadapters4MODERATES::InstantiationStrategy,
)
smartadapters4MODERATES::AdviceModel_strategy = st.builds(
    smartadapters4MODERATES::AdviceModel,
)
smartadapters4MODERATES::PointcutModel_strategy = st.builds(
    smartadapters4MODERATES::PointcutModel,
)
smartadapters4MODERATES::Aspect_strategy = st.builds(
    smartadapters4MODERATES::Aspect,
    name=
        safe_text
)

@given(instance=adaptations::smartadapters4MODERATES::ActionBlock_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::actionblock_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::ActionBlock)

@given(instance=adaptations::smartadapters4MODERATES::PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::platformannotation_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::PlatformAnnotation)

@given(instance=adaptations::smartadapters4MODERATES::AnnotatedElement_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::annotatedelement_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::AnnotatedElement)

@given(instance=adaptations::smartadapters4MODERATES::Expression_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::expression_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::Expression)

@given(instance=adaptations::smartadapters4MODERATES::Event_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::event_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::Event)

@given(instance=adaptations::smartadapters4MODERATES::Property_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::property_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::Property)

@given(instance=adaptations::smartadapters4MODERATES::Action_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::action_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::Action)

@given(instance=adaptations::smartadapters4MODERATES::Transition_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::transition_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::Transition)

@given(instance=smartadapters4MODERATES::Adaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::Adaptation)

@given(instance=UnsetAdaptation_strategy)
@settings(max_examples=50)
def test_unsetadaptation_instantiation(instance):
    assert isinstance(instance, UnsetAdaptation)

@given(instance=smartadapters4MODERATES::adaptations::UnsetState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::unsetstate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::UnsetState)

@given(instance=smartadapters4MODERATES::adaptations::UnsetTransition_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::unsettransition_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::UnsetTransition)

@given(instance=smartadapters4MODERATES::adaptations::UnsetCompositeState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::unsetcompositestate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::UnsetCompositeState)

@given(instance=adaptations::smartadapters4MODERATES::State_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::state_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::State)

@given(instance=adaptations::smartadapters4MODERATES::CompositeState_strategy)
@settings(max_examples=50)
def test_adaptations::smartadapters4moderates::compositestate_instantiation(instance):
    assert isinstance(instance, adaptations::smartadapters4MODERATES::CompositeState)

@given(instance=SetAdaptation_strategy)
@settings(max_examples=50)
def test_setadaptation_instantiation(instance):
    assert isinstance(instance, SetAdaptation)

@given(instance=smartadapters4MODERATES::adaptations::SetTransition_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::settransition_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::SetTransition)

@given(instance=smartadapters4MODERATES::adaptations::SetAnnotatedElement_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::setannotatedelement_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::SetAnnotatedElement)

@given(instance=smartadapters4MODERATES::adaptations::SetState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::setstate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::SetState)

@given(instance=smartadapters4MODERATES::adaptations::SetActionBlock_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::setactionblock_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::SetActionBlock)

@given(instance=smartadapters4MODERATES::adaptations::SetCompositeState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::adaptations::setcompositestate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::adaptations::SetCompositeState)

@given(instance=ScopedInstantiation_strategy)
@settings(max_examples=50)
def test_scopedinstantiation_instantiation(instance):
    assert isinstance(instance, ScopedInstantiation)

@given(instance=smartadapters4MODERATES::PerElementMatch_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::perelementmatch_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::PerElementMatch)

@given(instance=smartadapters4MODERATES::PerRoleMatch_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::perrolematch_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::PerRoleMatch)

@given(instance=InstantiationStrategy_strategy)
@settings(max_examples=50)
def test_instantiationstrategy_instantiation(instance):
    assert isinstance(instance, InstantiationStrategy)

@given(instance=smartadapters4MODERATES::ScopedInstantiation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::scopedinstantiation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::ScopedInstantiation)

@given(instance=smartadapters4MODERATES::GlobalInstantiation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::globalinstantiation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::GlobalInstantiation)

@given(instance=smartadapters4MODERATES::AspectModelElement_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::aspectmodelelement_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::AspectModelElement)

@given(instance=Adaptation_strategy)
@settings(max_examples=50)
def test_adaptation_instantiation(instance):
    assert isinstance(instance, Adaptation)

@given(instance=smartadapters4MODERATES::SetAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::setadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::SetAdaptation)

@given(instance=smartadapters4MODERATES::UnsetAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::unsetadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::UnsetAdaptation)

@given(instance=smartadapters4MODERATES::CreateAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::createadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::CreateAdaptation)

@given(instance=smartadapters4MODERATES::CloneAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::cloneadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::CloneAdaptation)

@given(instance=smartadapters4MODERATES::InstantiationStrategy_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::instantiationstrategy_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::InstantiationStrategy)

@given(instance=smartadapters4MODERATES::AdviceModel_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::advicemodel_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::AdviceModel)

@given(instance=smartadapters4MODERATES::PointcutModel_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::pointcutmodel_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::PointcutModel)

@given(instance=smartadapters4MODERATES::Aspect_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates::aspect_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES::Aspect)

@given(instance=smartadapters4MODERATES::Aspect_strategy)
def test_smartadapters4moderates::aspect_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smartadapters4MODERATES::Aspect_strategy)
def test_smartadapters4moderates::aspect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

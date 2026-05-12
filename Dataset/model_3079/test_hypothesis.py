import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    adaptations_smartadapters4MODERATES_ActionBlock,
    adaptations_smartadapters4MODERATES_PlatformAnnotation,
    adaptations_smartadapters4MODERATES_AnnotatedElement,
    adaptations_smartadapters4MODERATES_Expression,
    adaptations_smartadapters4MODERATES_Event,
    adaptations_smartadapters4MODERATES_Property,
    adaptations_smartadapters4MODERATES_Action,
    adaptations_smartadapters4MODERATES_Transition,
    smartadapters4MODERATES_Adaptation,
    UnsetAdaptation,
    smartadapters4MODERATES_adaptations_UnsetTransition,
    smartadapters4MODERATES_adaptations_UnsetState,
    smartadapters4MODERATES_adaptations_UnsetCompositeState,
    adaptations_smartadapters4MODERATES_State,
    adaptations_smartadapters4MODERATES_CompositeState,
    SetAdaptation,
    smartadapters4MODERATES_adaptations_SetActionBlock,
    smartadapters4MODERATES_adaptations_SetTransition,
    smartadapters4MODERATES_adaptations_SetState,
    smartadapters4MODERATES_adaptations_SetAnnotatedElement,
    smartadapters4MODERATES_adaptations_SetCompositeState,
    ScopedInstantiation,
    smartadapters4MODERATES_PerElementMatch,
    smartadapters4MODERATES_PerRoleMatch,
    InstantiationStrategy,
    smartadapters4MODERATES_ScopedInstantiation,
    smartadapters4MODERATES_GlobalInstantiation,
    smartadapters4MODERATES_AspectModelElement,
    Adaptation,
    smartadapters4MODERATES_CreateAdaptation,
    smartadapters4MODERATES_SetAdaptation,
    smartadapters4MODERATES_UnsetAdaptation,
    smartadapters4MODERATES_CloneAdaptation,
    smartadapters4MODERATES_InstantiationStrategy,
    smartadapters4MODERATES_AdviceModel,
    smartadapters4MODERATES_PointcutModel,
    smartadapters4MODERATES_Aspect,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adaptations_smartadapters4moderates_actionblock_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_ActionBlock)


def test_adaptations_smartadapters4moderates_actionblock_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_ActionBlock.__init__)


def test_adaptations_smartadapters4moderates_actionblock_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_platformannotation_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_PlatformAnnotation)


def test_adaptations_smartadapters4moderates_platformannotation_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_PlatformAnnotation.__init__)


def test_adaptations_smartadapters4moderates_platformannotation_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_PlatformAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_annotatedelement_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_AnnotatedElement)


def test_adaptations_smartadapters4moderates_annotatedelement_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_AnnotatedElement.__init__)


def test_adaptations_smartadapters4moderates_annotatedelement_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_AnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_expression_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_Expression)


def test_adaptations_smartadapters4moderates_expression_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_Expression.__init__)


def test_adaptations_smartadapters4moderates_expression_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_Expression.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_event_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_Event)


def test_adaptations_smartadapters4moderates_event_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_Event.__init__)


def test_adaptations_smartadapters4moderates_event_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_Event.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_property_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_Property)


def test_adaptations_smartadapters4moderates_property_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_Property.__init__)


def test_adaptations_smartadapters4moderates_property_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_Property.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_action_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_Action)


def test_adaptations_smartadapters4moderates_action_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_Action.__init__)


def test_adaptations_smartadapters4moderates_action_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_Action.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_transition_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_Transition)


def test_adaptations_smartadapters4moderates_transition_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_Transition.__init__)


def test_adaptations_smartadapters4moderates_transition_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_Transition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_Adaptation)


def test_smartadapters4moderates_adaptation_constructor_exists():
    assert callable(smartadapters4MODERATES_Adaptation.__init__)


def test_smartadapters4moderates_adaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_Adaptation.__init__)
    params = list(sig.parameters.keys())



def test_unsetadaptation_is_not_abstract():
    assert not inspect.isabstract(UnsetAdaptation)


def test_unsetadaptation_constructor_exists():
    assert callable(UnsetAdaptation.__init__)


def test_unsetadaptation_constructor_args():
    sig = inspect.signature(UnsetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_unsettransition_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_UnsetTransition)


def test_smartadapters4moderates_adaptations_unsettransition_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_UnsetTransition.__init__)


def test_smartadapters4moderates_adaptations_unsettransition_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_UnsetTransition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_unsetstate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_UnsetState)


def test_smartadapters4moderates_adaptations_unsetstate_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_UnsetState.__init__)


def test_smartadapters4moderates_adaptations_unsetstate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_UnsetState.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_unsetcompositestate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_UnsetCompositeState)


def test_smartadapters4moderates_adaptations_unsetcompositestate_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_UnsetCompositeState.__init__)


def test_smartadapters4moderates_adaptations_unsetcompositestate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_UnsetCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_state_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_State)


def test_adaptations_smartadapters4moderates_state_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_State.__init__)


def test_adaptations_smartadapters4moderates_state_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_State.__init__)
    params = list(sig.parameters.keys())



def test_adaptations_smartadapters4moderates_compositestate_is_not_abstract():
    assert not inspect.isabstract(adaptations_smartadapters4MODERATES_CompositeState)


def test_adaptations_smartadapters4moderates_compositestate_constructor_exists():
    assert callable(adaptations_smartadapters4MODERATES_CompositeState.__init__)


def test_adaptations_smartadapters4moderates_compositestate_constructor_args():
    sig = inspect.signature(adaptations_smartadapters4MODERATES_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_setadaptation_is_not_abstract():
    assert not inspect.isabstract(SetAdaptation)


def test_setadaptation_constructor_exists():
    assert callable(SetAdaptation.__init__)


def test_setadaptation_constructor_args():
    sig = inspect.signature(SetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_setactionblock_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_SetActionBlock)


def test_smartadapters4moderates_adaptations_setactionblock_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_SetActionBlock.__init__)


def test_smartadapters4moderates_adaptations_setactionblock_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_SetActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_settransition_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_SetTransition)


def test_smartadapters4moderates_adaptations_settransition_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_SetTransition.__init__)


def test_smartadapters4moderates_adaptations_settransition_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_SetTransition.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_setstate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_SetState)


def test_smartadapters4moderates_adaptations_setstate_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_SetState.__init__)


def test_smartadapters4moderates_adaptations_setstate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_SetState.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_setannotatedelement_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_SetAnnotatedElement)


def test_smartadapters4moderates_adaptations_setannotatedelement_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_SetAnnotatedElement.__init__)


def test_smartadapters4moderates_adaptations_setannotatedelement_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_SetAnnotatedElement.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_adaptations_setcompositestate_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_adaptations_SetCompositeState)


def test_smartadapters4moderates_adaptations_setcompositestate_constructor_exists():
    assert callable(smartadapters4MODERATES_adaptations_SetCompositeState.__init__)


def test_smartadapters4moderates_adaptations_setcompositestate_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_adaptations_SetCompositeState.__init__)
    params = list(sig.parameters.keys())



def test_scopedinstantiation_is_not_abstract():
    assert not inspect.isabstract(ScopedInstantiation)


def test_scopedinstantiation_constructor_exists():
    assert callable(ScopedInstantiation.__init__)


def test_scopedinstantiation_constructor_args():
    sig = inspect.signature(ScopedInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_perelementmatch_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_PerElementMatch)


def test_smartadapters4moderates_perelementmatch_constructor_exists():
    assert callable(smartadapters4MODERATES_PerElementMatch.__init__)


def test_smartadapters4moderates_perelementmatch_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_PerElementMatch.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_perrolematch_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_PerRoleMatch)


def test_smartadapters4moderates_perrolematch_constructor_exists():
    assert callable(smartadapters4MODERATES_PerRoleMatch.__init__)


def test_smartadapters4moderates_perrolematch_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_PerRoleMatch.__init__)
    params = list(sig.parameters.keys())



def test_instantiationstrategy_is_not_abstract():
    assert not inspect.isabstract(InstantiationStrategy)


def test_instantiationstrategy_constructor_exists():
    assert callable(InstantiationStrategy.__init__)


def test_instantiationstrategy_constructor_args():
    sig = inspect.signature(InstantiationStrategy.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_scopedinstantiation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_ScopedInstantiation)


def test_smartadapters4moderates_scopedinstantiation_constructor_exists():
    assert callable(smartadapters4MODERATES_ScopedInstantiation.__init__)


def test_smartadapters4moderates_scopedinstantiation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_ScopedInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_globalinstantiation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_GlobalInstantiation)


def test_smartadapters4moderates_globalinstantiation_constructor_exists():
    assert callable(smartadapters4MODERATES_GlobalInstantiation.__init__)


def test_smartadapters4moderates_globalinstantiation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_GlobalInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_aspectmodelelement_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_AspectModelElement)


def test_smartadapters4moderates_aspectmodelelement_constructor_exists():
    assert callable(smartadapters4MODERATES_AspectModelElement.__init__)


def test_smartadapters4moderates_aspectmodelelement_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_AspectModelElement.__init__)
    params = list(sig.parameters.keys())



def test_adaptation_is_not_abstract():
    assert not inspect.isabstract(Adaptation)


def test_adaptation_constructor_exists():
    assert callable(Adaptation.__init__)


def test_adaptation_constructor_args():
    sig = inspect.signature(Adaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_createadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_CreateAdaptation)


def test_smartadapters4moderates_createadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES_CreateAdaptation.__init__)


def test_smartadapters4moderates_createadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_CreateAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_setadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_SetAdaptation)


def test_smartadapters4moderates_setadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES_SetAdaptation.__init__)


def test_smartadapters4moderates_setadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_SetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_unsetadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_UnsetAdaptation)


def test_smartadapters4moderates_unsetadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES_UnsetAdaptation.__init__)


def test_smartadapters4moderates_unsetadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_UnsetAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_cloneadaptation_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_CloneAdaptation)


def test_smartadapters4moderates_cloneadaptation_constructor_exists():
    assert callable(smartadapters4MODERATES_CloneAdaptation.__init__)


def test_smartadapters4moderates_cloneadaptation_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_CloneAdaptation.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_instantiationstrategy_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_InstantiationStrategy)


def test_smartadapters4moderates_instantiationstrategy_constructor_exists():
    assert callable(smartadapters4MODERATES_InstantiationStrategy.__init__)


def test_smartadapters4moderates_instantiationstrategy_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_InstantiationStrategy.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_advicemodel_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_AdviceModel)


def test_smartadapters4moderates_advicemodel_constructor_exists():
    assert callable(smartadapters4MODERATES_AdviceModel.__init__)


def test_smartadapters4moderates_advicemodel_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_AdviceModel.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_pointcutmodel_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_PointcutModel)


def test_smartadapters4moderates_pointcutmodel_constructor_exists():
    assert callable(smartadapters4MODERATES_PointcutModel.__init__)


def test_smartadapters4moderates_pointcutmodel_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_PointcutModel.__init__)
    params = list(sig.parameters.keys())



def test_smartadapters4moderates_aspect_is_not_abstract():
    assert not inspect.isabstract(smartadapters4MODERATES_Aspect)


def test_smartadapters4moderates_aspect_constructor_exists():
    assert callable(smartadapters4MODERATES_Aspect.__init__)


def test_smartadapters4moderates_aspect_constructor_args():
    sig = inspect.signature(smartadapters4MODERATES_Aspect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smartadapters4moderates_aspect_has_name():
    assert hasattr(smartadapters4MODERATES_Aspect, "name")
    descriptor = None
    for klass in smartadapters4MODERATES_Aspect.__mro__:
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
adaptations_smartadapters4MODERATES_ActionBlock_strategy = st.builds(
    adaptations_smartadapters4MODERATES_ActionBlock,
)
adaptations_smartadapters4MODERATES_PlatformAnnotation_strategy = st.builds(
    adaptations_smartadapters4MODERATES_PlatformAnnotation,
)
adaptations_smartadapters4MODERATES_AnnotatedElement_strategy = st.builds(
    adaptations_smartadapters4MODERATES_AnnotatedElement,
)
adaptations_smartadapters4MODERATES_Expression_strategy = st.builds(
    adaptations_smartadapters4MODERATES_Expression,
)
adaptations_smartadapters4MODERATES_Event_strategy = st.builds(
    adaptations_smartadapters4MODERATES_Event,
)
adaptations_smartadapters4MODERATES_Property_strategy = st.builds(
    adaptations_smartadapters4MODERATES_Property,
)
adaptations_smartadapters4MODERATES_Action_strategy = st.builds(
    adaptations_smartadapters4MODERATES_Action,
)
adaptations_smartadapters4MODERATES_Transition_strategy = st.builds(
    adaptations_smartadapters4MODERATES_Transition,
)
smartadapters4MODERATES_Adaptation_strategy = st.builds(
    smartadapters4MODERATES_Adaptation,
)
UnsetAdaptation_strategy = st.builds(
    UnsetAdaptation,
)
smartadapters4MODERATES_adaptations_UnsetTransition_strategy = st.builds(
    smartadapters4MODERATES_adaptations_UnsetTransition,
)
smartadapters4MODERATES_adaptations_UnsetState_strategy = st.builds(
    smartadapters4MODERATES_adaptations_UnsetState,
)
smartadapters4MODERATES_adaptations_UnsetCompositeState_strategy = st.builds(
    smartadapters4MODERATES_adaptations_UnsetCompositeState,
)
adaptations_smartadapters4MODERATES_State_strategy = st.builds(
    adaptations_smartadapters4MODERATES_State,
)
adaptations_smartadapters4MODERATES_CompositeState_strategy = st.builds(
    adaptations_smartadapters4MODERATES_CompositeState,
)
SetAdaptation_strategy = st.builds(
    SetAdaptation,
)
smartadapters4MODERATES_adaptations_SetActionBlock_strategy = st.builds(
    smartadapters4MODERATES_adaptations_SetActionBlock,
)
smartadapters4MODERATES_adaptations_SetTransition_strategy = st.builds(
    smartadapters4MODERATES_adaptations_SetTransition,
)
smartadapters4MODERATES_adaptations_SetState_strategy = st.builds(
    smartadapters4MODERATES_adaptations_SetState,
)
smartadapters4MODERATES_adaptations_SetAnnotatedElement_strategy = st.builds(
    smartadapters4MODERATES_adaptations_SetAnnotatedElement,
)
smartadapters4MODERATES_adaptations_SetCompositeState_strategy = st.builds(
    smartadapters4MODERATES_adaptations_SetCompositeState,
)
ScopedInstantiation_strategy = st.builds(
    ScopedInstantiation,
)
smartadapters4MODERATES_PerElementMatch_strategy = st.builds(
    smartadapters4MODERATES_PerElementMatch,
)
smartadapters4MODERATES_PerRoleMatch_strategy = st.builds(
    smartadapters4MODERATES_PerRoleMatch,
)
InstantiationStrategy_strategy = st.builds(
    InstantiationStrategy,
)
smartadapters4MODERATES_ScopedInstantiation_strategy = st.builds(
    smartadapters4MODERATES_ScopedInstantiation,
)
smartadapters4MODERATES_GlobalInstantiation_strategy = st.builds(
    smartadapters4MODERATES_GlobalInstantiation,
)
smartadapters4MODERATES_AspectModelElement_strategy = st.builds(
    smartadapters4MODERATES_AspectModelElement,
)
Adaptation_strategy = st.builds(
    Adaptation,
)
smartadapters4MODERATES_CreateAdaptation_strategy = st.builds(
    smartadapters4MODERATES_CreateAdaptation,
)
smartadapters4MODERATES_SetAdaptation_strategy = st.builds(
    smartadapters4MODERATES_SetAdaptation,
)
smartadapters4MODERATES_UnsetAdaptation_strategy = st.builds(
    smartadapters4MODERATES_UnsetAdaptation,
)
smartadapters4MODERATES_CloneAdaptation_strategy = st.builds(
    smartadapters4MODERATES_CloneAdaptation,
)
smartadapters4MODERATES_InstantiationStrategy_strategy = st.builds(
    smartadapters4MODERATES_InstantiationStrategy,
)
smartadapters4MODERATES_AdviceModel_strategy = st.builds(
    smartadapters4MODERATES_AdviceModel,
)
smartadapters4MODERATES_PointcutModel_strategy = st.builds(
    smartadapters4MODERATES_PointcutModel,
)
smartadapters4MODERATES_Aspect_strategy = st.builds(
    smartadapters4MODERATES_Aspect,
    name=
        safe_text
)

@given(instance=adaptations_smartadapters4MODERATES_ActionBlock_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_actionblock_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_ActionBlock)

@given(instance=adaptations_smartadapters4MODERATES_PlatformAnnotation_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_platformannotation_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_PlatformAnnotation)

@given(instance=adaptations_smartadapters4MODERATES_AnnotatedElement_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_annotatedelement_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_AnnotatedElement)

@given(instance=adaptations_smartadapters4MODERATES_Expression_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_expression_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_Expression)

@given(instance=adaptations_smartadapters4MODERATES_Event_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_event_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_Event)

@given(instance=adaptations_smartadapters4MODERATES_Property_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_property_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_Property)

@given(instance=adaptations_smartadapters4MODERATES_Action_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_action_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_Action)

@given(instance=adaptations_smartadapters4MODERATES_Transition_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_transition_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_Transition)

@given(instance=smartadapters4MODERATES_Adaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_Adaptation)

@given(instance=UnsetAdaptation_strategy)
@settings(max_examples=50)
def test_unsetadaptation_instantiation(instance):
    assert isinstance(instance, UnsetAdaptation)

@given(instance=smartadapters4MODERATES_adaptations_UnsetTransition_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_unsettransition_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_UnsetTransition)

@given(instance=smartadapters4MODERATES_adaptations_UnsetState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_unsetstate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_UnsetState)

@given(instance=smartadapters4MODERATES_adaptations_UnsetCompositeState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_unsetcompositestate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_UnsetCompositeState)

@given(instance=adaptations_smartadapters4MODERATES_State_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_state_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_State)

@given(instance=adaptations_smartadapters4MODERATES_CompositeState_strategy)
@settings(max_examples=50)
def test_adaptations_smartadapters4moderates_compositestate_instantiation(instance):
    assert isinstance(instance, adaptations_smartadapters4MODERATES_CompositeState)

@given(instance=SetAdaptation_strategy)
@settings(max_examples=50)
def test_setadaptation_instantiation(instance):
    assert isinstance(instance, SetAdaptation)

@given(instance=smartadapters4MODERATES_adaptations_SetActionBlock_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_setactionblock_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_SetActionBlock)

@given(instance=smartadapters4MODERATES_adaptations_SetTransition_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_settransition_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_SetTransition)

@given(instance=smartadapters4MODERATES_adaptations_SetState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_setstate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_SetState)

@given(instance=smartadapters4MODERATES_adaptations_SetAnnotatedElement_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_setannotatedelement_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_SetAnnotatedElement)

@given(instance=smartadapters4MODERATES_adaptations_SetCompositeState_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_adaptations_setcompositestate_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_adaptations_SetCompositeState)

@given(instance=ScopedInstantiation_strategy)
@settings(max_examples=50)
def test_scopedinstantiation_instantiation(instance):
    assert isinstance(instance, ScopedInstantiation)

@given(instance=smartadapters4MODERATES_PerElementMatch_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_perelementmatch_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_PerElementMatch)

@given(instance=smartadapters4MODERATES_PerRoleMatch_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_perrolematch_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_PerRoleMatch)

@given(instance=InstantiationStrategy_strategy)
@settings(max_examples=50)
def test_instantiationstrategy_instantiation(instance):
    assert isinstance(instance, InstantiationStrategy)

@given(instance=smartadapters4MODERATES_ScopedInstantiation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_scopedinstantiation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_ScopedInstantiation)

@given(instance=smartadapters4MODERATES_GlobalInstantiation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_globalinstantiation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_GlobalInstantiation)

@given(instance=smartadapters4MODERATES_AspectModelElement_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_aspectmodelelement_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_AspectModelElement)

@given(instance=Adaptation_strategy)
@settings(max_examples=50)
def test_adaptation_instantiation(instance):
    assert isinstance(instance, Adaptation)

@given(instance=smartadapters4MODERATES_CreateAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_createadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_CreateAdaptation)

@given(instance=smartadapters4MODERATES_SetAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_setadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_SetAdaptation)

@given(instance=smartadapters4MODERATES_UnsetAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_unsetadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_UnsetAdaptation)

@given(instance=smartadapters4MODERATES_CloneAdaptation_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_cloneadaptation_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_CloneAdaptation)

@given(instance=smartadapters4MODERATES_InstantiationStrategy_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_instantiationstrategy_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_InstantiationStrategy)

@given(instance=smartadapters4MODERATES_AdviceModel_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_advicemodel_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_AdviceModel)

@given(instance=smartadapters4MODERATES_PointcutModel_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_pointcutmodel_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_PointcutModel)

@given(instance=smartadapters4MODERATES_Aspect_strategy)
@settings(max_examples=50)
def test_smartadapters4moderates_aspect_instantiation(instance):
    assert isinstance(instance, smartadapters4MODERATES_Aspect)



@given(instance=smartadapters4MODERATES_Aspect_strategy)
def test_smartadapters4moderates_aspect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

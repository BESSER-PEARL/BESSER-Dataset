import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TrgArc,
    jointPackage::Grafcet2PetriNet::TrgPlaceToTransition,
    jointPackage::Grafcet2PetriNet::TrgTransitionToPlace,
    TrgElement,
    jointPackage::Grafcet2PetriNet::TrgTransition,
    jointPackage::Grafcet2PetriNet::TrgPlace,
    TrgNamedElement,
    jointPackage::Grafcet2PetriNet::TrgArc,
    jointPackage::Grafcet2PetriNet::TrgElement,
    TrgLocatedElement,
    jointPackage::Grafcet2PetriNet::TrgNamedElement,
    jointPackage::Grafcet2PetriNet::TrgLocatedElement,
    SrcLocatedElement,
    jointPackage::Grafcet2PetriNet::SrcNamedElement,
    SrcConnection,
    jointPackage::Grafcet2PetriNet::SrcStepToTransition,
    jointPackage::Grafcet2PetriNet::SrcTransitionToStep,
    SrcElement,
    jointPackage::Grafcet2PetriNet::SrcTransition,
    jointPackage::Grafcet2PetriNet::SrcStep,
    SrcNamedElement,
    jointPackage::Grafcet2PetriNet::SrcConnection,
    jointPackage::Grafcet2PetriNet::SrcElement,
    jointPackage::Grafcet2PetriNet::SrcLocatedElement,
    jointPackage::Grafcet2PetriNet::TrgPetriNet,
    jointPackage::Grafcet2PetriNet::SrcGrafcet,
    jointPackage::Grafcet2PetriNet::JointMM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgarc_is_not_abstract():
    assert not inspect.isabstract(TrgArc)


def test_trgarc_constructor_exists():
    assert callable(TrgArc.__init__)


def test_trgarc_constructor_args():
    sig = inspect.signature(TrgArc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgplacetotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgPlaceToTransition)


def test_jointpackage::grafcet2petrinet::trgplacetotransition_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgPlaceToTransition.__init__)


def test_jointpackage::grafcet2petrinet::trgplacetotransition_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgPlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgtransitiontoplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgTransitionToPlace)


def test_jointpackage::grafcet2petrinet::trgtransitiontoplace_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgTransitionToPlace.__init__)


def test_jointpackage::grafcet2petrinet::trgtransitiontoplace_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgTransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_trgelement_is_not_abstract():
    assert not inspect.isabstract(TrgElement)


def test_trgelement_constructor_exists():
    assert callable(TrgElement.__init__)


def test_trgelement_constructor_args():
    sig = inspect.signature(TrgElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgTransition)


def test_jointpackage::grafcet2petrinet::trgtransition_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgTransition.__init__)


def test_jointpackage::grafcet2petrinet::trgtransition_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgPlace)


def test_jointpackage::grafcet2petrinet::trgplace_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgPlace.__init__)


def test_jointpackage::grafcet2petrinet::trgplace_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_trgnamedelement_is_not_abstract():
    assert not inspect.isabstract(TrgNamedElement)


def test_trgnamedelement_constructor_exists():
    assert callable(TrgNamedElement.__init__)


def test_trgnamedelement_constructor_args():
    sig = inspect.signature(TrgNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgArc)


def test_jointpackage::grafcet2petrinet::trgarc_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgArc.__init__)


def test_jointpackage::grafcet2petrinet::trgarc_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_jointpackage::grafcet2petrinet::trgarc_has_weight():
    assert hasattr(jointPackage::Grafcet2PetriNet::TrgArc, "weight")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::TrgArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::grafcet2petrinet::trgelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgElement)


def test_jointpackage::grafcet2petrinet::trgelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgElement.__init__)


def test_jointpackage::grafcet2petrinet::trgelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgElement.__init__)
    params = list(sig.parameters.keys())



def test_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(TrgLocatedElement)


def test_trglocatedelement_constructor_exists():
    assert callable(TrgLocatedElement.__init__)


def test_trglocatedelement_constructor_args():
    sig = inspect.signature(TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::trgnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgNamedElement)


def test_jointpackage::grafcet2petrinet::trgnamedelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgNamedElement.__init__)


def test_jointpackage::grafcet2petrinet::trgnamedelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::grafcet2petrinet::trgnamedelement_has_name():
    assert hasattr(jointPackage::Grafcet2PetriNet::TrgNamedElement, "name")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::TrgNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::grafcet2petrinet::trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgLocatedElement)


def test_jointpackage::grafcet2petrinet::trglocatedelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgLocatedElement.__init__)


def test_jointpackage::grafcet2petrinet::trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage::grafcet2petrinet::trglocatedelement_has_location():
    assert hasattr(jointPackage::Grafcet2PetriNet::TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::TrgLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(SrcLocatedElement)


def test_srclocatedelement_constructor_exists():
    assert callable(SrcLocatedElement.__init__)


def test_srclocatedelement_constructor_args():
    sig = inspect.signature(SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcNamedElement)


def test_jointpackage::grafcet2petrinet::srcnamedelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcNamedElement.__init__)


def test_jointpackage::grafcet2petrinet::srcnamedelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::grafcet2petrinet::srcnamedelement_has_name():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcNamedElement, "name")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_srcconnection_is_not_abstract():
    assert not inspect.isabstract(SrcConnection)


def test_srcconnection_constructor_exists():
    assert callable(SrcConnection.__init__)


def test_srcconnection_constructor_args():
    sig = inspect.signature(SrcConnection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srcsteptotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcStepToTransition)


def test_jointpackage::grafcet2petrinet::srcsteptotransition_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcStepToTransition.__init__)


def test_jointpackage::grafcet2petrinet::srcsteptotransition_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcStepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srctransitiontostep_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcTransitionToStep)


def test_jointpackage::grafcet2petrinet::srctransitiontostep_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcTransitionToStep.__init__)


def test_jointpackage::grafcet2petrinet::srctransitiontostep_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcTransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_srcelement_is_not_abstract():
    assert not inspect.isabstract(SrcElement)


def test_srcelement_constructor_exists():
    assert callable(SrcElement.__init__)


def test_srcelement_constructor_args():
    sig = inspect.signature(SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcTransition)


def test_jointpackage::grafcet2petrinet::srctransition_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcTransition.__init__)


def test_jointpackage::grafcet2petrinet::srctransition_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcTransition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_jointpackage::grafcet2petrinet::srctransition_has_condition():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcTransition, "condition")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcTransition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::grafcet2petrinet::srcstep_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcStep)


def test_jointpackage::grafcet2petrinet::srcstep_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcStep.__init__)


def test_jointpackage::grafcet2petrinet::srcstep_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcStep.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_jointpackage::grafcet2petrinet::srcstep_has_action():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcStep, "action")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcStep.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::grafcet2petrinet::srcstep_has_isActive():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcStep, "isActive")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcStep.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage::grafcet2petrinet::srcstep_has_isInitial():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcStep, "isInitial")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcStep.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(SrcNamedElement)


def test_srcnamedelement_constructor_exists():
    assert callable(SrcNamedElement.__init__)


def test_srcnamedelement_constructor_args():
    sig = inspect.signature(SrcNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srcconnection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcConnection)


def test_jointpackage::grafcet2petrinet::srcconnection_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcConnection.__init__)


def test_jointpackage::grafcet2petrinet::srcconnection_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcConnection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcElement)


def test_jointpackage::grafcet2petrinet::srcelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcElement.__init__)


def test_jointpackage::grafcet2petrinet::srcelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcLocatedElement)


def test_jointpackage::grafcet2petrinet::srclocatedelement_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcLocatedElement.__init__)


def test_jointpackage::grafcet2petrinet::srclocatedelement_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage::grafcet2petrinet::srclocatedelement_has_location():
    assert hasattr(jointPackage::Grafcet2PetriNet::SrcLocatedElement, "location")
    descriptor = None
    for klass in jointPackage::Grafcet2PetriNet::SrcLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::grafcet2petrinet::trgpetrinet_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::TrgPetriNet)


def test_jointpackage::grafcet2petrinet::trgpetrinet_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::TrgPetriNet.__init__)


def test_jointpackage::grafcet2petrinet::trgpetrinet_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::TrgPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::srcgrafcet_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::SrcGrafcet)


def test_jointpackage::grafcet2petrinet::srcgrafcet_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::SrcGrafcet.__init__)


def test_jointpackage::grafcet2petrinet::srcgrafcet_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::SrcGrafcet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::grafcet2petrinet::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::Grafcet2PetriNet::JointMM)


def test_jointpackage::grafcet2petrinet::jointmm_constructor_exists():
    assert callable(jointPackage::Grafcet2PetriNet::JointMM.__init__)


def test_jointpackage::grafcet2petrinet::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::Grafcet2PetriNet::JointMM.__init__)
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
TrgArc_strategy = st.builds(
    TrgArc,
)
jointPackage::Grafcet2PetriNet::TrgPlaceToTransition_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgPlaceToTransition,
)
jointPackage::Grafcet2PetriNet::TrgTransitionToPlace_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgTransitionToPlace,
)
TrgElement_strategy = st.builds(
    TrgElement,
)
jointPackage::Grafcet2PetriNet::TrgTransition_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgTransition,
)
jointPackage::Grafcet2PetriNet::TrgPlace_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgPlace,
)
TrgNamedElement_strategy = st.builds(
    TrgNamedElement,
)
jointPackage::Grafcet2PetriNet::TrgArc_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgArc,
    weight=
        st.integers()
)
jointPackage::Grafcet2PetriNet::TrgElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgElement,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage::Grafcet2PetriNet::TrgNamedElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgNamedElement,
    name=
        safe_text
)
jointPackage::Grafcet2PetriNet::TrgLocatedElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgLocatedElement,
    location=
        safe_text
)
SrcLocatedElement_strategy = st.builds(
    SrcLocatedElement,
)
jointPackage::Grafcet2PetriNet::SrcNamedElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcNamedElement,
    name=
        safe_text
)
SrcConnection_strategy = st.builds(
    SrcConnection,
)
jointPackage::Grafcet2PetriNet::SrcStepToTransition_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcStepToTransition,
)
jointPackage::Grafcet2PetriNet::SrcTransitionToStep_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcTransitionToStep,
)
SrcElement_strategy = st.builds(
    SrcElement,
)
jointPackage::Grafcet2PetriNet::SrcTransition_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcTransition,
    condition=
        safe_text
)
jointPackage::Grafcet2PetriNet::SrcStep_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcStep,
    action=
        safe_text,
    isActive=
        st.booleans(),
    isInitial=
        st.booleans()
)
SrcNamedElement_strategy = st.builds(
    SrcNamedElement,
)
jointPackage::Grafcet2PetriNet::SrcConnection_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcConnection,
)
jointPackage::Grafcet2PetriNet::SrcElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcElement,
)
jointPackage::Grafcet2PetriNet::SrcLocatedElement_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcLocatedElement,
    location=
        safe_text
)
jointPackage::Grafcet2PetriNet::TrgPetriNet_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::TrgPetriNet,
)
jointPackage::Grafcet2PetriNet::SrcGrafcet_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::SrcGrafcet,
)
jointPackage::Grafcet2PetriNet::JointMM_strategy = st.builds(
    jointPackage::Grafcet2PetriNet::JointMM,
)

@given(instance=TrgArc_strategy)
@settings(max_examples=50)
def test_trgarc_instantiation(instance):
    assert isinstance(instance, TrgArc)

@given(instance=jointPackage::Grafcet2PetriNet::TrgPlaceToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgplacetotransition_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgPlaceToTransition)

@given(instance=jointPackage::Grafcet2PetriNet::TrgTransitionToPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgtransitiontoplace_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgTransitionToPlace)

@given(instance=TrgElement_strategy)
@settings(max_examples=50)
def test_trgelement_instantiation(instance):
    assert isinstance(instance, TrgElement)

@given(instance=jointPackage::Grafcet2PetriNet::TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgTransition)

@given(instance=jointPackage::Grafcet2PetriNet::TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgPlace)

@given(instance=TrgNamedElement_strategy)
@settings(max_examples=50)
def test_trgnamedelement_instantiation(instance):
    assert isinstance(instance, TrgNamedElement)

@given(instance=jointPackage::Grafcet2PetriNet::TrgArc_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgarc_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgArc)

@given(instance=jointPackage::Grafcet2PetriNet::TrgArc_strategy)
def test_jointpackage::grafcet2petrinet::trgarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=jointPackage::Grafcet2PetriNet::TrgArc_strategy)
def test_jointpackage::grafcet2petrinet::trgarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=jointPackage::Grafcet2PetriNet::TrgElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgElement)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage::Grafcet2PetriNet::TrgNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgNamedElement)

@given(instance=jointPackage::Grafcet2PetriNet::TrgNamedElement_strategy)
def test_jointpackage::grafcet2petrinet::trgnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Grafcet2PetriNet::TrgNamedElement_strategy)
def test_jointpackage::grafcet2petrinet::trgnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::Grafcet2PetriNet::TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgLocatedElement)

@given(instance=jointPackage::Grafcet2PetriNet::TrgLocatedElement_strategy)
def test_jointpackage::grafcet2petrinet::trglocatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=jointPackage::Grafcet2PetriNet::TrgLocatedElement_strategy)
def test_jointpackage::grafcet2petrinet::trglocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_srclocatedelement_instantiation(instance):
    assert isinstance(instance, SrcLocatedElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcNamedElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcNamedElement_strategy)
def test_jointpackage::grafcet2petrinet::srcnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::Grafcet2PetriNet::SrcNamedElement_strategy)
def test_jointpackage::grafcet2petrinet::srcnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SrcConnection_strategy)
@settings(max_examples=50)
def test_srcconnection_instantiation(instance):
    assert isinstance(instance, SrcConnection)

@given(instance=jointPackage::Grafcet2PetriNet::SrcStepToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcsteptotransition_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcStepToTransition)

@given(instance=jointPackage::Grafcet2PetriNet::SrcTransitionToStep_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srctransitiontostep_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcTransitionToStep)

@given(instance=SrcElement_strategy)
@settings(max_examples=50)
def test_srcelement_instantiation(instance):
    assert isinstance(instance, SrcElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcTransition)

@given(instance=jointPackage::Grafcet2PetriNet::SrcTransition_strategy)
def test_jointpackage::grafcet2petrinet::srctransition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=jointPackage::Grafcet2PetriNet::SrcTransition_strategy)
def test_jointpackage::grafcet2petrinet::srctransition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcstep_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcStep)

@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=jointPackage::Grafcet2PetriNet::SrcStep_strategy)
def test_jointpackage::grafcet2petrinet::srcstep_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=SrcNamedElement_strategy)
@settings(max_examples=50)
def test_srcnamedelement_instantiation(instance):
    assert isinstance(instance, SrcNamedElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcConnection_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcconnection_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcConnection)

@given(instance=jointPackage::Grafcet2PetriNet::SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srclocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcLocatedElement)

@given(instance=jointPackage::Grafcet2PetriNet::SrcLocatedElement_strategy)
def test_jointpackage::grafcet2petrinet::srclocatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=jointPackage::Grafcet2PetriNet::SrcLocatedElement_strategy)
def test_jointpackage::grafcet2petrinet::srclocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=jointPackage::Grafcet2PetriNet::TrgPetriNet_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::trgpetrinet_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::TrgPetriNet)

@given(instance=jointPackage::Grafcet2PetriNet::SrcGrafcet_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::srcgrafcet_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::SrcGrafcet)

@given(instance=jointPackage::Grafcet2PetriNet::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::grafcet2petrinet::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::Grafcet2PetriNet::JointMM)

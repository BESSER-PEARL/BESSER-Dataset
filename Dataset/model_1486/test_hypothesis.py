import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TrgArc,
    jointPackage_Grafcet2PetriNet_TrgPlaceToTransition,
    jointPackage_Grafcet2PetriNet_TrgTransitionToPlace,
    TrgElement,
    jointPackage_Grafcet2PetriNet_TrgTransition,
    jointPackage_Grafcet2PetriNet_TrgPlace,
    TrgNamedElement,
    jointPackage_Grafcet2PetriNet_TrgArc,
    jointPackage_Grafcet2PetriNet_TrgElement,
    TrgLocatedElement,
    jointPackage_Grafcet2PetriNet_TrgNamedElement,
    jointPackage_Grafcet2PetriNet_TrgLocatedElement,
    SrcLocatedElement,
    jointPackage_Grafcet2PetriNet_SrcNamedElement,
    SrcConnection,
    jointPackage_Grafcet2PetriNet_SrcStepToTransition,
    jointPackage_Grafcet2PetriNet_SrcTransitionToStep,
    SrcElement,
    jointPackage_Grafcet2PetriNet_SrcTransition,
    jointPackage_Grafcet2PetriNet_SrcStep,
    SrcNamedElement,
    jointPackage_Grafcet2PetriNet_SrcElement,
    jointPackage_Grafcet2PetriNet_SrcConnection,
    jointPackage_Grafcet2PetriNet_SrcLocatedElement,
    jointPackage_Grafcet2PetriNet_TrgPetriNet,
    jointPackage_Grafcet2PetriNet_SrcGrafcet,
    jointPackage_Grafcet2PetriNet_JointMM,
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



def test_jointpackage_grafcet2petrinet_trgplacetotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgPlaceToTransition)


def test_jointpackage_grafcet2petrinet_trgplacetotransition_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgPlaceToTransition.__init__)


def test_jointpackage_grafcet2petrinet_trgplacetotransition_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgPlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_trgtransitiontoplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgTransitionToPlace)


def test_jointpackage_grafcet2petrinet_trgtransitiontoplace_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgTransitionToPlace.__init__)


def test_jointpackage_grafcet2petrinet_trgtransitiontoplace_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgTransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_trgelement_is_not_abstract():
    assert not inspect.isabstract(TrgElement)


def test_trgelement_constructor_exists():
    assert callable(TrgElement.__init__)


def test_trgelement_constructor_args():
    sig = inspect.signature(TrgElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgTransition)


def test_jointpackage_grafcet2petrinet_trgtransition_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgTransition.__init__)


def test_jointpackage_grafcet2petrinet_trgtransition_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgPlace)


def test_jointpackage_grafcet2petrinet_trgplace_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgPlace.__init__)


def test_jointpackage_grafcet2petrinet_trgplace_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_trgnamedelement_is_not_abstract():
    assert not inspect.isabstract(TrgNamedElement)


def test_trgnamedelement_constructor_exists():
    assert callable(TrgNamedElement.__init__)


def test_trgnamedelement_constructor_args():
    sig = inspect.signature(TrgNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_trgarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgArc)


def test_jointpackage_grafcet2petrinet_trgarc_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgArc.__init__)


def test_jointpackage_grafcet2petrinet_trgarc_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_jointpackage_grafcet2petrinet_trgarc_has_weight():
    assert hasattr(jointPackage_Grafcet2PetriNet_TrgArc, "weight")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_TrgArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_grafcet2petrinet_trgelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgElement)


def test_jointpackage_grafcet2petrinet_trgelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgElement.__init__)


def test_jointpackage_grafcet2petrinet_trgelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgElement.__init__)
    params = list(sig.parameters.keys())



def test_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(TrgLocatedElement)


def test_trglocatedelement_constructor_exists():
    assert callable(TrgLocatedElement.__init__)


def test_trglocatedelement_constructor_args():
    sig = inspect.signature(TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_trgnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgNamedElement)


def test_jointpackage_grafcet2petrinet_trgnamedelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgNamedElement.__init__)


def test_jointpackage_grafcet2petrinet_trgnamedelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_grafcet2petrinet_trgnamedelement_has_name():
    assert hasattr(jointPackage_Grafcet2PetriNet_TrgNamedElement, "name")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_TrgNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_grafcet2petrinet_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgLocatedElement)


def test_jointpackage_grafcet2petrinet_trglocatedelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgLocatedElement.__init__)


def test_jointpackage_grafcet2petrinet_trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage_grafcet2petrinet_trglocatedelement_has_location():
    assert hasattr(jointPackage_Grafcet2PetriNet_TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_TrgLocatedElement.__mro__:
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



def test_jointpackage_grafcet2petrinet_srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcNamedElement)


def test_jointpackage_grafcet2petrinet_srcnamedelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcNamedElement.__init__)


def test_jointpackage_grafcet2petrinet_srcnamedelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_grafcet2petrinet_srcnamedelement_has_name():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcNamedElement, "name")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcNamedElement.__mro__:
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



def test_jointpackage_grafcet2petrinet_srcsteptotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcStepToTransition)


def test_jointpackage_grafcet2petrinet_srcsteptotransition_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcStepToTransition.__init__)


def test_jointpackage_grafcet2petrinet_srcsteptotransition_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcStepToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_srctransitiontostep_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcTransitionToStep)


def test_jointpackage_grafcet2petrinet_srctransitiontostep_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcTransitionToStep.__init__)


def test_jointpackage_grafcet2petrinet_srctransitiontostep_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcTransitionToStep.__init__)
    params = list(sig.parameters.keys())



def test_srcelement_is_not_abstract():
    assert not inspect.isabstract(SrcElement)


def test_srcelement_constructor_exists():
    assert callable(SrcElement.__init__)


def test_srcelement_constructor_args():
    sig = inspect.signature(SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcTransition)


def test_jointpackage_grafcet2petrinet_srctransition_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcTransition.__init__)


def test_jointpackage_grafcet2petrinet_srctransition_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcTransition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_jointpackage_grafcet2petrinet_srctransition_has_condition():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcTransition, "condition")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcTransition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_grafcet2petrinet_srcstep_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcStep)


def test_jointpackage_grafcet2petrinet_srcstep_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcStep.__init__)


def test_jointpackage_grafcet2petrinet_srcstep_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcStep.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_jointpackage_grafcet2petrinet_srcstep_has_action():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcStep, "action")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcStep.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_grafcet2petrinet_srcstep_has_isActive():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcStep, "isActive")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcStep.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_jointpackage_grafcet2petrinet_srcstep_has_isInitial():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcStep, "isInitial")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcStep.__mro__:
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



def test_jointpackage_grafcet2petrinet_srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcElement)


def test_jointpackage_grafcet2petrinet_srcelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcElement.__init__)


def test_jointpackage_grafcet2petrinet_srcelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_srcconnection_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcConnection)


def test_jointpackage_grafcet2petrinet_srcconnection_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcConnection.__init__)


def test_jointpackage_grafcet2petrinet_srcconnection_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcConnection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcLocatedElement)


def test_jointpackage_grafcet2petrinet_srclocatedelement_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcLocatedElement.__init__)


def test_jointpackage_grafcet2petrinet_srclocatedelement_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage_grafcet2petrinet_srclocatedelement_has_location():
    assert hasattr(jointPackage_Grafcet2PetriNet_SrcLocatedElement, "location")
    descriptor = None
    for klass in jointPackage_Grafcet2PetriNet_SrcLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_grafcet2petrinet_trgpetrinet_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_TrgPetriNet)


def test_jointpackage_grafcet2petrinet_trgpetrinet_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_TrgPetriNet.__init__)


def test_jointpackage_grafcet2petrinet_trgpetrinet_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_TrgPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_srcgrafcet_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_SrcGrafcet)


def test_jointpackage_grafcet2petrinet_srcgrafcet_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_SrcGrafcet.__init__)


def test_jointpackage_grafcet2petrinet_srcgrafcet_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_SrcGrafcet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_grafcet2petrinet_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_Grafcet2PetriNet_JointMM)


def test_jointpackage_grafcet2petrinet_jointmm_constructor_exists():
    assert callable(jointPackage_Grafcet2PetriNet_JointMM.__init__)


def test_jointpackage_grafcet2petrinet_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_Grafcet2PetriNet_JointMM.__init__)
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
jointPackage_Grafcet2PetriNet_TrgPlaceToTransition_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgPlaceToTransition,
)
jointPackage_Grafcet2PetriNet_TrgTransitionToPlace_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgTransitionToPlace,
)
TrgElement_strategy = st.builds(
    TrgElement,
)
jointPackage_Grafcet2PetriNet_TrgTransition_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgTransition,
)
jointPackage_Grafcet2PetriNet_TrgPlace_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgPlace,
)
TrgNamedElement_strategy = st.builds(
    TrgNamedElement,
)
jointPackage_Grafcet2PetriNet_TrgArc_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgArc,
    weight=
        st.integers()
)
jointPackage_Grafcet2PetriNet_TrgElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgElement,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage_Grafcet2PetriNet_TrgNamedElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgNamedElement,
    name=
        safe_text
)
jointPackage_Grafcet2PetriNet_TrgLocatedElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgLocatedElement,
    location=
        safe_text
)
SrcLocatedElement_strategy = st.builds(
    SrcLocatedElement,
)
jointPackage_Grafcet2PetriNet_SrcNamedElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcNamedElement,
    name=
        safe_text
)
SrcConnection_strategy = st.builds(
    SrcConnection,
)
jointPackage_Grafcet2PetriNet_SrcStepToTransition_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcStepToTransition,
)
jointPackage_Grafcet2PetriNet_SrcTransitionToStep_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcTransitionToStep,
)
SrcElement_strategy = st.builds(
    SrcElement,
)
jointPackage_Grafcet2PetriNet_SrcTransition_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcTransition,
    condition=
        safe_text
)
jointPackage_Grafcet2PetriNet_SrcStep_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcStep,
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
jointPackage_Grafcet2PetriNet_SrcElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcElement,
)
jointPackage_Grafcet2PetriNet_SrcConnection_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcConnection,
)
jointPackage_Grafcet2PetriNet_SrcLocatedElement_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcLocatedElement,
    location=
        safe_text
)
jointPackage_Grafcet2PetriNet_TrgPetriNet_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_TrgPetriNet,
)
jointPackage_Grafcet2PetriNet_SrcGrafcet_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_SrcGrafcet,
)
jointPackage_Grafcet2PetriNet_JointMM_strategy = st.builds(
    jointPackage_Grafcet2PetriNet_JointMM,
)

@given(instance=TrgArc_strategy)
@settings(max_examples=50)
def test_trgarc_instantiation(instance):
    assert isinstance(instance, TrgArc)

@given(instance=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgplacetotransition_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgPlaceToTransition)

@given(instance=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgtransitiontoplace_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgTransitionToPlace)

@given(instance=TrgElement_strategy)
@settings(max_examples=50)
def test_trgelement_instantiation(instance):
    assert isinstance(instance, TrgElement)

@given(instance=jointPackage_Grafcet2PetriNet_TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgTransition)

@given(instance=jointPackage_Grafcet2PetriNet_TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgPlace)

@given(instance=TrgNamedElement_strategy)
@settings(max_examples=50)
def test_trgnamedelement_instantiation(instance):
    assert isinstance(instance, TrgNamedElement)

@given(instance=jointPackage_Grafcet2PetriNet_TrgArc_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgarc_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgArc)



@given(instance=jointPackage_Grafcet2PetriNet_TrgArc_strategy)
def test_jointpackage_grafcet2petrinet_trgarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=jointPackage_Grafcet2PetriNet_TrgElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgElement)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage_Grafcet2PetriNet_TrgNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgNamedElement)



@given(instance=jointPackage_Grafcet2PetriNet_TrgNamedElement_strategy)
def test_jointpackage_grafcet2petrinet_trgnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_Grafcet2PetriNet_TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgLocatedElement)



@given(instance=jointPackage_Grafcet2PetriNet_TrgLocatedElement_strategy)
def test_jointpackage_grafcet2petrinet_trglocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_srclocatedelement_instantiation(instance):
    assert isinstance(instance, SrcLocatedElement)

@given(instance=jointPackage_Grafcet2PetriNet_SrcNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcNamedElement)



@given(instance=jointPackage_Grafcet2PetriNet_SrcNamedElement_strategy)
def test_jointpackage_grafcet2petrinet_srcnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SrcConnection_strategy)
@settings(max_examples=50)
def test_srcconnection_instantiation(instance):
    assert isinstance(instance, SrcConnection)

@given(instance=jointPackage_Grafcet2PetriNet_SrcStepToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcsteptotransition_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcStepToTransition)

@given(instance=jointPackage_Grafcet2PetriNet_SrcTransitionToStep_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srctransitiontostep_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcTransitionToStep)

@given(instance=SrcElement_strategy)
@settings(max_examples=50)
def test_srcelement_instantiation(instance):
    assert isinstance(instance, SrcElement)

@given(instance=jointPackage_Grafcet2PetriNet_SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcTransition)



@given(instance=jointPackage_Grafcet2PetriNet_SrcTransition_strategy)
def test_jointpackage_grafcet2petrinet_srctransition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=jointPackage_Grafcet2PetriNet_SrcStep_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcstep_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcStep)



@given(instance=jointPackage_Grafcet2PetriNet_SrcStep_strategy)
def test_jointpackage_grafcet2petrinet_srcstep_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=jointPackage_Grafcet2PetriNet_SrcStep_strategy)
def test_jointpackage_grafcet2petrinet_srcstep_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=jointPackage_Grafcet2PetriNet_SrcStep_strategy)
def test_jointpackage_grafcet2petrinet_srcstep_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=SrcNamedElement_strategy)
@settings(max_examples=50)
def test_srcnamedelement_instantiation(instance):
    assert isinstance(instance, SrcNamedElement)

@given(instance=jointPackage_Grafcet2PetriNet_SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcElement)

@given(instance=jointPackage_Grafcet2PetriNet_SrcConnection_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcconnection_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcConnection)

@given(instance=jointPackage_Grafcet2PetriNet_SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srclocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcLocatedElement)



@given(instance=jointPackage_Grafcet2PetriNet_SrcLocatedElement_strategy)
def test_jointpackage_grafcet2petrinet_srclocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=jointPackage_Grafcet2PetriNet_TrgPetriNet_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_trgpetrinet_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_TrgPetriNet)

@given(instance=jointPackage_Grafcet2PetriNet_SrcGrafcet_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_srcgrafcet_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_SrcGrafcet)

@given(instance=jointPackage_Grafcet2PetriNet_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_grafcet2petrinet_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_Grafcet2PetriNet_JointMM)

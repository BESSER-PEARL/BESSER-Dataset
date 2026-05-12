import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TrgNetContentElement,
    jointPackage_PetriNet2PNML_TrgTransition,
    jointPackage_PetriNet2PNML_TrgPlace,
    jointPackage_PetriNet2PNML_TrgLocatedElement,
    TrgNetContent,
    TrgLabeledElement,
    jointPackage_PetriNet2PNML_TrgName,
    TrgIdedElement,
    jointPackage_PetriNet2PNML_TrgNetContentElement,
    jointPackage_PetriNet2PNML_TrgArc,
    jointPackage_PetriNet2PNML_TrgNetElement,
    SrcElement,
    jointPackage_PetriNet2PNML_SrcPlace,
    TrgLocatedElement,
    jointPackage_PetriNet2PNML_TrgNetContent,
    jointPackage_PetriNet2PNML_TrgLabeledElement,
    jointPackage_PetriNet2PNML_TrgIdedElement,
    jointPackage_PetriNet2PNML_TrgURI,
    jointPackage_PetriNet2PNML_TrgLabel,
    SrcArc,
    jointPackage_PetriNet2PNML_SrcPlaceToTransition,
    jointPackage_PetriNet2PNML_SrcTransitionToPlace,
    jointPackage_PetriNet2PNML_SrcTransition,
    SrcNamedElement,
    jointPackage_PetriNet2PNML_SrcArc,
    jointPackage_PetriNet2PNML_SrcElement,
    SrcLocatedElement,
    jointPackage_PetriNet2PNML_SrcNamedElement,
    jointPackage_PetriNet2PNML_SrcLocatedElement,
    jointPackage_PetriNet2PNML_TrgPNMLDocument,
    jointPackage_PetriNet2PNML_SrcPetriNet,
    jointPackage_PetriNet2PNML_JointMM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trgnetcontentelement_is_not_abstract():
    assert not inspect.isabstract(TrgNetContentElement)


def test_trgnetcontentelement_constructor_exists():
    assert callable(TrgNetContentElement.__init__)


def test_trgnetcontentelement_constructor_args():
    sig = inspect.signature(TrgNetContentElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgTransition)


def test_jointpackage_petrinet2pnml_trgtransition_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgTransition.__init__)


def test_jointpackage_petrinet2pnml_trgtransition_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgPlace)


def test_jointpackage_petrinet2pnml_trgplace_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgPlace.__init__)


def test_jointpackage_petrinet2pnml_trgplace_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgLocatedElement)


def test_jointpackage_petrinet2pnml_trglocatedelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgLocatedElement.__init__)


def test_jointpackage_petrinet2pnml_trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage_petrinet2pnml_trglocatedelement_has_location():
    assert hasattr(jointPackage_PetriNet2PNML_TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_TrgLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_trgnetcontent_is_not_abstract():
    assert not inspect.isabstract(TrgNetContent)


def test_trgnetcontent_constructor_exists():
    assert callable(TrgNetContent.__init__)


def test_trgnetcontent_constructor_args():
    sig = inspect.signature(TrgNetContent.__init__)
    params = list(sig.parameters.keys())



def test_trglabeledelement_is_not_abstract():
    assert not inspect.isabstract(TrgLabeledElement)


def test_trglabeledelement_constructor_exists():
    assert callable(TrgLabeledElement.__init__)


def test_trglabeledelement_constructor_args():
    sig = inspect.signature(TrgLabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgname_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgName)


def test_jointpackage_petrinet2pnml_trgname_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgName.__init__)


def test_jointpackage_petrinet2pnml_trgname_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgName.__init__)
    params = list(sig.parameters.keys())



def test_trgidedelement_is_not_abstract():
    assert not inspect.isabstract(TrgIdedElement)


def test_trgidedelement_constructor_exists():
    assert callable(TrgIdedElement.__init__)


def test_trgidedelement_constructor_args():
    sig = inspect.signature(TrgIdedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgnetcontentelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgNetContentElement)


def test_jointpackage_petrinet2pnml_trgnetcontentelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgNetContentElement.__init__)


def test_jointpackage_petrinet2pnml_trgnetcontentelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgNetContentElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgArc)


def test_jointpackage_petrinet2pnml_trgarc_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgArc.__init__)


def test_jointpackage_petrinet2pnml_trgarc_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgArc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgnetelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgNetElement)


def test_jointpackage_petrinet2pnml_trgnetelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgNetElement.__init__)


def test_jointpackage_petrinet2pnml_trgnetelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgNetElement.__init__)
    params = list(sig.parameters.keys())



def test_srcelement_is_not_abstract():
    assert not inspect.isabstract(SrcElement)


def test_srcelement_constructor_exists():
    assert callable(SrcElement.__init__)


def test_srcelement_constructor_args():
    sig = inspect.signature(SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srcplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcPlace)


def test_jointpackage_petrinet2pnml_srcplace_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcPlace.__init__)


def test_jointpackage_petrinet2pnml_srcplace_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcPlace.__init__)
    params = list(sig.parameters.keys())



def test_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(TrgLocatedElement)


def test_trglocatedelement_constructor_exists():
    assert callable(TrgLocatedElement.__init__)


def test_trglocatedelement_constructor_args():
    sig = inspect.signature(TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgnetcontent_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgNetContent)


def test_jointpackage_petrinet2pnml_trgnetcontent_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgNetContent.__init__)


def test_jointpackage_petrinet2pnml_trgnetcontent_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgNetContent.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trglabeledelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgLabeledElement)


def test_jointpackage_petrinet2pnml_trglabeledelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgLabeledElement.__init__)


def test_jointpackage_petrinet2pnml_trglabeledelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgLabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_trgidedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgIdedElement)


def test_jointpackage_petrinet2pnml_trgidedelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgIdedElement.__init__)


def test_jointpackage_petrinet2pnml_trgidedelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgIdedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage_petrinet2pnml_trgidedelement_has_id():
    assert hasattr(jointPackage_PetriNet2PNML_TrgIdedElement, "id")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_TrgIdedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_petrinet2pnml_trguri_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgURI)


def test_jointpackage_petrinet2pnml_trguri_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgURI.__init__)


def test_jointpackage_petrinet2pnml_trguri_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgURI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage_petrinet2pnml_trguri_has_value():
    assert hasattr(jointPackage_PetriNet2PNML_TrgURI, "value")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_TrgURI.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_petrinet2pnml_trglabel_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgLabel)


def test_jointpackage_petrinet2pnml_trglabel_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgLabel.__init__)


def test_jointpackage_petrinet2pnml_trglabel_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_jointpackage_petrinet2pnml_trglabel_has_text():
    assert hasattr(jointPackage_PetriNet2PNML_TrgLabel, "text")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_TrgLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_srcarc_is_not_abstract():
    assert not inspect.isabstract(SrcArc)


def test_srcarc_constructor_exists():
    assert callable(SrcArc.__init__)


def test_srcarc_constructor_args():
    sig = inspect.signature(SrcArc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srcplacetotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcPlaceToTransition)


def test_jointpackage_petrinet2pnml_srcplacetotransition_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcPlaceToTransition.__init__)


def test_jointpackage_petrinet2pnml_srcplacetotransition_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcPlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srctransitiontoplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcTransitionToPlace)


def test_jointpackage_petrinet2pnml_srctransitiontoplace_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcTransitionToPlace.__init__)


def test_jointpackage_petrinet2pnml_srctransitiontoplace_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcTransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcTransition)


def test_jointpackage_petrinet2pnml_srctransition_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcTransition.__init__)


def test_jointpackage_petrinet2pnml_srctransition_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcTransition.__init__)
    params = list(sig.parameters.keys())



def test_srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(SrcNamedElement)


def test_srcnamedelement_constructor_exists():
    assert callable(SrcNamedElement.__init__)


def test_srcnamedelement_constructor_args():
    sig = inspect.signature(SrcNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srcarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcArc)


def test_jointpackage_petrinet2pnml_srcarc_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcArc.__init__)


def test_jointpackage_petrinet2pnml_srcarc_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_jointpackage_petrinet2pnml_srcarc_has_weight():
    assert hasattr(jointPackage_PetriNet2PNML_SrcArc, "weight")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_SrcArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_petrinet2pnml_srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcElement)


def test_jointpackage_petrinet2pnml_srcelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcElement.__init__)


def test_jointpackage_petrinet2pnml_srcelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(SrcLocatedElement)


def test_srclocatedelement_constructor_exists():
    assert callable(SrcLocatedElement.__init__)


def test_srclocatedelement_constructor_args():
    sig = inspect.signature(SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcNamedElement)


def test_jointpackage_petrinet2pnml_srcnamedelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcNamedElement.__init__)


def test_jointpackage_petrinet2pnml_srcnamedelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage_petrinet2pnml_srcnamedelement_has_name():
    assert hasattr(jointPackage_PetriNet2PNML_SrcNamedElement, "name")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_SrcNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_petrinet2pnml_srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcLocatedElement)


def test_jointpackage_petrinet2pnml_srclocatedelement_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcLocatedElement.__init__)


def test_jointpackage_petrinet2pnml_srclocatedelement_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage_petrinet2pnml_srclocatedelement_has_location():
    assert hasattr(jointPackage_PetriNet2PNML_SrcLocatedElement, "location")
    descriptor = None
    for klass in jointPackage_PetriNet2PNML_SrcLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_petrinet2pnml_trgpnmldocument_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_TrgPNMLDocument)


def test_jointpackage_petrinet2pnml_trgpnmldocument_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_TrgPNMLDocument.__init__)


def test_jointpackage_petrinet2pnml_trgpnmldocument_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_TrgPNMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_srcpetrinet_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_SrcPetriNet)


def test_jointpackage_petrinet2pnml_srcpetrinet_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_SrcPetriNet.__init__)


def test_jointpackage_petrinet2pnml_srcpetrinet_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_SrcPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_petrinet2pnml_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_PetriNet2PNML_JointMM)


def test_jointpackage_petrinet2pnml_jointmm_constructor_exists():
    assert callable(jointPackage_PetriNet2PNML_JointMM.__init__)


def test_jointpackage_petrinet2pnml_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_PetriNet2PNML_JointMM.__init__)
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
TrgNetContentElement_strategy = st.builds(
    TrgNetContentElement,
)
jointPackage_PetriNet2PNML_TrgTransition_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgTransition,
)
jointPackage_PetriNet2PNML_TrgPlace_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgPlace,
)
jointPackage_PetriNet2PNML_TrgLocatedElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgLocatedElement,
    location=
        safe_text
)
TrgNetContent_strategy = st.builds(
    TrgNetContent,
)
TrgLabeledElement_strategy = st.builds(
    TrgLabeledElement,
)
jointPackage_PetriNet2PNML_TrgName_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgName,
)
TrgIdedElement_strategy = st.builds(
    TrgIdedElement,
)
jointPackage_PetriNet2PNML_TrgNetContentElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgNetContentElement,
)
jointPackage_PetriNet2PNML_TrgArc_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgArc,
)
jointPackage_PetriNet2PNML_TrgNetElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgNetElement,
)
SrcElement_strategy = st.builds(
    SrcElement,
)
jointPackage_PetriNet2PNML_SrcPlace_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcPlace,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage_PetriNet2PNML_TrgNetContent_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgNetContent,
)
jointPackage_PetriNet2PNML_TrgLabeledElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgLabeledElement,
)
jointPackage_PetriNet2PNML_TrgIdedElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgIdedElement,
    id=
        safe_text
)
jointPackage_PetriNet2PNML_TrgURI_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgURI,
    value=
        safe_text
)
jointPackage_PetriNet2PNML_TrgLabel_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgLabel,
    text=
        safe_text
)
SrcArc_strategy = st.builds(
    SrcArc,
)
jointPackage_PetriNet2PNML_SrcPlaceToTransition_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcPlaceToTransition,
)
jointPackage_PetriNet2PNML_SrcTransitionToPlace_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcTransitionToPlace,
)
jointPackage_PetriNet2PNML_SrcTransition_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcTransition,
)
SrcNamedElement_strategy = st.builds(
    SrcNamedElement,
)
jointPackage_PetriNet2PNML_SrcArc_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcArc,
    weight=
        st.integers()
)
jointPackage_PetriNet2PNML_SrcElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcElement,
)
SrcLocatedElement_strategy = st.builds(
    SrcLocatedElement,
)
jointPackage_PetriNet2PNML_SrcNamedElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcNamedElement,
    name=
        safe_text
)
jointPackage_PetriNet2PNML_SrcLocatedElement_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcLocatedElement,
    location=
        safe_text
)
jointPackage_PetriNet2PNML_TrgPNMLDocument_strategy = st.builds(
    jointPackage_PetriNet2PNML_TrgPNMLDocument,
)
jointPackage_PetriNet2PNML_SrcPetriNet_strategy = st.builds(
    jointPackage_PetriNet2PNML_SrcPetriNet,
)
jointPackage_PetriNet2PNML_JointMM_strategy = st.builds(
    jointPackage_PetriNet2PNML_JointMM,
)

@given(instance=TrgNetContentElement_strategy)
@settings(max_examples=50)
def test_trgnetcontentelement_instantiation(instance):
    assert isinstance(instance, TrgNetContentElement)

@given(instance=jointPackage_PetriNet2PNML_TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgTransition)

@given(instance=jointPackage_PetriNet2PNML_TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgPlace)

@given(instance=jointPackage_PetriNet2PNML_TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLocatedElement)



@given(instance=jointPackage_PetriNet2PNML_TrgLocatedElement_strategy)
def test_jointpackage_petrinet2pnml_trglocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=TrgNetContent_strategy)
@settings(max_examples=50)
def test_trgnetcontent_instantiation(instance):
    assert isinstance(instance, TrgNetContent)

@given(instance=TrgLabeledElement_strategy)
@settings(max_examples=50)
def test_trglabeledelement_instantiation(instance):
    assert isinstance(instance, TrgLabeledElement)

@given(instance=jointPackage_PetriNet2PNML_TrgName_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgname_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgName)

@given(instance=TrgIdedElement_strategy)
@settings(max_examples=50)
def test_trgidedelement_instantiation(instance):
    assert isinstance(instance, TrgIdedElement)

@given(instance=jointPackage_PetriNet2PNML_TrgNetContentElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgnetcontentelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetContentElement)

@given(instance=jointPackage_PetriNet2PNML_TrgArc_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgarc_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgArc)

@given(instance=jointPackage_PetriNet2PNML_TrgNetElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgnetelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetElement)

@given(instance=SrcElement_strategy)
@settings(max_examples=50)
def test_srcelement_instantiation(instance):
    assert isinstance(instance, SrcElement)

@given(instance=jointPackage_PetriNet2PNML_SrcPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcplace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPlace)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage_PetriNet2PNML_TrgNetContent_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgnetcontent_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgNetContent)

@given(instance=jointPackage_PetriNet2PNML_TrgLabeledElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trglabeledelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLabeledElement)

@given(instance=jointPackage_PetriNet2PNML_TrgIdedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgidedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgIdedElement)



@given(instance=jointPackage_PetriNet2PNML_TrgIdedElement_strategy)
def test_jointpackage_petrinet2pnml_trgidedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jointPackage_PetriNet2PNML_TrgURI_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trguri_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgURI)



@given(instance=jointPackage_PetriNet2PNML_TrgURI_strategy)
def test_jointpackage_petrinet2pnml_trguri_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage_PetriNet2PNML_TrgLabel_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trglabel_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgLabel)



@given(instance=jointPackage_PetriNet2PNML_TrgLabel_strategy)
def test_jointpackage_petrinet2pnml_trglabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SrcArc_strategy)
@settings(max_examples=50)
def test_srcarc_instantiation(instance):
    assert isinstance(instance, SrcArc)

@given(instance=jointPackage_PetriNet2PNML_SrcPlaceToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcplacetotransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPlaceToTransition)

@given(instance=jointPackage_PetriNet2PNML_SrcTransitionToPlace_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srctransitiontoplace_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcTransitionToPlace)

@given(instance=jointPackage_PetriNet2PNML_SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcTransition)

@given(instance=SrcNamedElement_strategy)
@settings(max_examples=50)
def test_srcnamedelement_instantiation(instance):
    assert isinstance(instance, SrcNamedElement)

@given(instance=jointPackage_PetriNet2PNML_SrcArc_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcarc_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcArc)



@given(instance=jointPackage_PetriNet2PNML_SrcArc_strategy)
def test_jointpackage_petrinet2pnml_srcarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=jointPackage_PetriNet2PNML_SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcElement)

@given(instance=SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_srclocatedelement_instantiation(instance):
    assert isinstance(instance, SrcLocatedElement)

@given(instance=jointPackage_PetriNet2PNML_SrcNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcNamedElement)



@given(instance=jointPackage_PetriNet2PNML_SrcNamedElement_strategy)
def test_jointpackage_petrinet2pnml_srcnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage_PetriNet2PNML_SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srclocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcLocatedElement)



@given(instance=jointPackage_PetriNet2PNML_SrcLocatedElement_strategy)
def test_jointpackage_petrinet2pnml_srclocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=jointPackage_PetriNet2PNML_TrgPNMLDocument_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_trgpnmldocument_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_TrgPNMLDocument)

@given(instance=jointPackage_PetriNet2PNML_SrcPetriNet_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_srcpetrinet_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_SrcPetriNet)

@given(instance=jointPackage_PetriNet2PNML_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_petrinet2pnml_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_PetriNet2PNML_JointMM)

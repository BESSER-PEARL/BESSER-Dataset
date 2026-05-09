import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TrgNetContentElement,
    jointPackage::PetriNet2PNML::TrgTransition,
    jointPackage::PetriNet2PNML::TrgPlace,
    jointPackage::PetriNet2PNML::TrgLocatedElement,
    TrgNetContent,
    TrgLabeledElement,
    jointPackage::PetriNet2PNML::TrgName,
    TrgIdedElement,
    jointPackage::PetriNet2PNML::TrgNetElement,
    jointPackage::PetriNet2PNML::TrgNetContentElement,
    jointPackage::PetriNet2PNML::TrgArc,
    SrcElement,
    jointPackage::PetriNet2PNML::SrcPlace,
    TrgLocatedElement,
    jointPackage::PetriNet2PNML::TrgIdedElement,
    jointPackage::PetriNet2PNML::TrgNetContent,
    jointPackage::PetriNet2PNML::TrgURI,
    jointPackage::PetriNet2PNML::TrgLabeledElement,
    jointPackage::PetriNet2PNML::TrgLabel,
    SrcArc,
    jointPackage::PetriNet2PNML::SrcPlaceToTransition,
    jointPackage::PetriNet2PNML::SrcTransitionToPlace,
    jointPackage::PetriNet2PNML::SrcTransition,
    SrcNamedElement,
    jointPackage::PetriNet2PNML::SrcArc,
    jointPackage::PetriNet2PNML::SrcElement,
    SrcLocatedElement,
    jointPackage::PetriNet2PNML::SrcNamedElement,
    jointPackage::PetriNet2PNML::SrcLocatedElement,
    jointPackage::PetriNet2PNML::TrgPNMLDocument,
    jointPackage::PetriNet2PNML::SrcPetriNet,
    jointPackage::PetriNet2PNML::JointMM,
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



def test_jointpackage::petrinet2pnml::trgtransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgTransition)


def test_jointpackage::petrinet2pnml::trgtransition_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgTransition.__init__)


def test_jointpackage::petrinet2pnml::trgtransition_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trgplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgPlace)


def test_jointpackage::petrinet2pnml::trgplace_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgPlace.__init__)


def test_jointpackage::petrinet2pnml::trgplace_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgLocatedElement)


def test_jointpackage::petrinet2pnml::trglocatedelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgLocatedElement.__init__)


def test_jointpackage::petrinet2pnml::trglocatedelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage::petrinet2pnml::trglocatedelement_has_location():
    assert hasattr(jointPackage::PetriNet2PNML::TrgLocatedElement, "location")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::TrgLocatedElement.__mro__:
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



def test_jointpackage::petrinet2pnml::trgname_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgName)


def test_jointpackage::petrinet2pnml::trgname_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgName.__init__)


def test_jointpackage::petrinet2pnml::trgname_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgName.__init__)
    params = list(sig.parameters.keys())



def test_trgidedelement_is_not_abstract():
    assert not inspect.isabstract(TrgIdedElement)


def test_trgidedelement_constructor_exists():
    assert callable(TrgIdedElement.__init__)


def test_trgidedelement_constructor_args():
    sig = inspect.signature(TrgIdedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trgnetelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgNetElement)


def test_jointpackage::petrinet2pnml::trgnetelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgNetElement.__init__)


def test_jointpackage::petrinet2pnml::trgnetelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgNetElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trgnetcontentelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgNetContentElement)


def test_jointpackage::petrinet2pnml::trgnetcontentelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgNetContentElement.__init__)


def test_jointpackage::petrinet2pnml::trgnetcontentelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgNetContentElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trgarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgArc)


def test_jointpackage::petrinet2pnml::trgarc_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgArc.__init__)


def test_jointpackage::petrinet2pnml::trgarc_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgArc.__init__)
    params = list(sig.parameters.keys())



def test_srcelement_is_not_abstract():
    assert not inspect.isabstract(SrcElement)


def test_srcelement_constructor_exists():
    assert callable(SrcElement.__init__)


def test_srcelement_constructor_args():
    sig = inspect.signature(SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srcplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcPlace)


def test_jointpackage::petrinet2pnml::srcplace_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcPlace.__init__)


def test_jointpackage::petrinet2pnml::srcplace_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcPlace.__init__)
    params = list(sig.parameters.keys())



def test_trglocatedelement_is_not_abstract():
    assert not inspect.isabstract(TrgLocatedElement)


def test_trglocatedelement_constructor_exists():
    assert callable(TrgLocatedElement.__init__)


def test_trglocatedelement_constructor_args():
    sig = inspect.signature(TrgLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trgidedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgIdedElement)


def test_jointpackage::petrinet2pnml::trgidedelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgIdedElement.__init__)


def test_jointpackage::petrinet2pnml::trgidedelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgIdedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage::petrinet2pnml::trgidedelement_has_id():
    assert hasattr(jointPackage::PetriNet2PNML::TrgIdedElement, "id")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::TrgIdedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::petrinet2pnml::trgnetcontent_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgNetContent)


def test_jointpackage::petrinet2pnml::trgnetcontent_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgNetContent.__init__)


def test_jointpackage::petrinet2pnml::trgnetcontent_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgNetContent.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trguri_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgURI)


def test_jointpackage::petrinet2pnml::trguri_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgURI.__init__)


def test_jointpackage::petrinet2pnml::trguri_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgURI.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jointpackage::petrinet2pnml::trguri_has_value():
    assert hasattr(jointPackage::PetriNet2PNML::TrgURI, "value")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::TrgURI.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::petrinet2pnml::trglabeledelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgLabeledElement)


def test_jointpackage::petrinet2pnml::trglabeledelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgLabeledElement.__init__)


def test_jointpackage::petrinet2pnml::trglabeledelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgLabeledElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::trglabel_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgLabel)


def test_jointpackage::petrinet2pnml::trglabel_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgLabel.__init__)


def test_jointpackage::petrinet2pnml::trglabel_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_jointpackage::petrinet2pnml::trglabel_has_text():
    assert hasattr(jointPackage::PetriNet2PNML::TrgLabel, "text")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::TrgLabel.__mro__:
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



def test_jointpackage::petrinet2pnml::srcplacetotransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcPlaceToTransition)


def test_jointpackage::petrinet2pnml::srcplacetotransition_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcPlaceToTransition.__init__)


def test_jointpackage::petrinet2pnml::srcplacetotransition_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcPlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srctransitiontoplace_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcTransitionToPlace)


def test_jointpackage::petrinet2pnml::srctransitiontoplace_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcTransitionToPlace.__init__)


def test_jointpackage::petrinet2pnml::srctransitiontoplace_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcTransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srctransition_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcTransition)


def test_jointpackage::petrinet2pnml::srctransition_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcTransition.__init__)


def test_jointpackage::petrinet2pnml::srctransition_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcTransition.__init__)
    params = list(sig.parameters.keys())



def test_srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(SrcNamedElement)


def test_srcnamedelement_constructor_exists():
    assert callable(SrcNamedElement.__init__)


def test_srcnamedelement_constructor_args():
    sig = inspect.signature(SrcNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srcarc_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcArc)


def test_jointpackage::petrinet2pnml::srcarc_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcArc.__init__)


def test_jointpackage::petrinet2pnml::srcarc_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_jointpackage::petrinet2pnml::srcarc_has_weight():
    assert hasattr(jointPackage::PetriNet2PNML::SrcArc, "weight")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::SrcArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::petrinet2pnml::srcelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcElement)


def test_jointpackage::petrinet2pnml::srcelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcElement.__init__)


def test_jointpackage::petrinet2pnml::srcelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcElement.__init__)
    params = list(sig.parameters.keys())



def test_srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(SrcLocatedElement)


def test_srclocatedelement_constructor_exists():
    assert callable(SrcLocatedElement.__init__)


def test_srclocatedelement_constructor_args():
    sig = inspect.signature(SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srcnamedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcNamedElement)


def test_jointpackage::petrinet2pnml::srcnamedelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcNamedElement.__init__)


def test_jointpackage::petrinet2pnml::srcnamedelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jointpackage::petrinet2pnml::srcnamedelement_has_name():
    assert hasattr(jointPackage::PetriNet2PNML::SrcNamedElement, "name")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::SrcNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::petrinet2pnml::srclocatedelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcLocatedElement)


def test_jointpackage::petrinet2pnml::srclocatedelement_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcLocatedElement.__init__)


def test_jointpackage::petrinet2pnml::srclocatedelement_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcLocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_jointpackage::petrinet2pnml::srclocatedelement_has_location():
    assert hasattr(jointPackage::PetriNet2PNML::SrcLocatedElement, "location")
    descriptor = None
    for klass in jointPackage::PetriNet2PNML::SrcLocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::petrinet2pnml::trgpnmldocument_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::TrgPNMLDocument)


def test_jointpackage::petrinet2pnml::trgpnmldocument_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::TrgPNMLDocument.__init__)


def test_jointpackage::petrinet2pnml::trgpnmldocument_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::TrgPNMLDocument.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::srcpetrinet_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::SrcPetriNet)


def test_jointpackage::petrinet2pnml::srcpetrinet_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::SrcPetriNet.__init__)


def test_jointpackage::petrinet2pnml::srcpetrinet_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::SrcPetriNet.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::petrinet2pnml::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::PetriNet2PNML::JointMM)


def test_jointpackage::petrinet2pnml::jointmm_constructor_exists():
    assert callable(jointPackage::PetriNet2PNML::JointMM.__init__)


def test_jointpackage::petrinet2pnml::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::PetriNet2PNML::JointMM.__init__)
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
jointPackage::PetriNet2PNML::TrgTransition_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgTransition,
)
jointPackage::PetriNet2PNML::TrgPlace_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgPlace,
)
jointPackage::PetriNet2PNML::TrgLocatedElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgLocatedElement,
    location=
        safe_text
)
TrgNetContent_strategy = st.builds(
    TrgNetContent,
)
TrgLabeledElement_strategy = st.builds(
    TrgLabeledElement,
)
jointPackage::PetriNet2PNML::TrgName_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgName,
)
TrgIdedElement_strategy = st.builds(
    TrgIdedElement,
)
jointPackage::PetriNet2PNML::TrgNetElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgNetElement,
)
jointPackage::PetriNet2PNML::TrgNetContentElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgNetContentElement,
)
jointPackage::PetriNet2PNML::TrgArc_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgArc,
)
SrcElement_strategy = st.builds(
    SrcElement,
)
jointPackage::PetriNet2PNML::SrcPlace_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcPlace,
)
TrgLocatedElement_strategy = st.builds(
    TrgLocatedElement,
)
jointPackage::PetriNet2PNML::TrgIdedElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgIdedElement,
    id=
        safe_text
)
jointPackage::PetriNet2PNML::TrgNetContent_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgNetContent,
)
jointPackage::PetriNet2PNML::TrgURI_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgURI,
    value=
        safe_text
)
jointPackage::PetriNet2PNML::TrgLabeledElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgLabeledElement,
)
jointPackage::PetriNet2PNML::TrgLabel_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgLabel,
    text=
        safe_text
)
SrcArc_strategy = st.builds(
    SrcArc,
)
jointPackage::PetriNet2PNML::SrcPlaceToTransition_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcPlaceToTransition,
)
jointPackage::PetriNet2PNML::SrcTransitionToPlace_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcTransitionToPlace,
)
jointPackage::PetriNet2PNML::SrcTransition_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcTransition,
)
SrcNamedElement_strategy = st.builds(
    SrcNamedElement,
)
jointPackage::PetriNet2PNML::SrcArc_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcArc,
    weight=
        st.integers()
)
jointPackage::PetriNet2PNML::SrcElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcElement,
)
SrcLocatedElement_strategy = st.builds(
    SrcLocatedElement,
)
jointPackage::PetriNet2PNML::SrcNamedElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcNamedElement,
    name=
        safe_text
)
jointPackage::PetriNet2PNML::SrcLocatedElement_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcLocatedElement,
    location=
        safe_text
)
jointPackage::PetriNet2PNML::TrgPNMLDocument_strategy = st.builds(
    jointPackage::PetriNet2PNML::TrgPNMLDocument,
)
jointPackage::PetriNet2PNML::SrcPetriNet_strategy = st.builds(
    jointPackage::PetriNet2PNML::SrcPetriNet,
)
jointPackage::PetriNet2PNML::JointMM_strategy = st.builds(
    jointPackage::PetriNet2PNML::JointMM,
)

@given(instance=TrgNetContentElement_strategy)
@settings(max_examples=50)
def test_trgnetcontentelement_instantiation(instance):
    assert isinstance(instance, TrgNetContentElement)

@given(instance=jointPackage::PetriNet2PNML::TrgTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgtransition_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgTransition)

@given(instance=jointPackage::PetriNet2PNML::TrgPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgplace_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgPlace)

@given(instance=jointPackage::PetriNet2PNML::TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trglocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgLocatedElement)

@given(instance=jointPackage::PetriNet2PNML::TrgLocatedElement_strategy)
def test_jointpackage::petrinet2pnml::trglocatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=jointPackage::PetriNet2PNML::TrgLocatedElement_strategy)
def test_jointpackage::petrinet2pnml::trglocatedelement_location_setter(instance):
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

@given(instance=jointPackage::PetriNet2PNML::TrgName_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgname_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgName)

@given(instance=TrgIdedElement_strategy)
@settings(max_examples=50)
def test_trgidedelement_instantiation(instance):
    assert isinstance(instance, TrgIdedElement)

@given(instance=jointPackage::PetriNet2PNML::TrgNetElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgnetelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgNetElement)

@given(instance=jointPackage::PetriNet2PNML::TrgNetContentElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgnetcontentelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgNetContentElement)

@given(instance=jointPackage::PetriNet2PNML::TrgArc_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgarc_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgArc)

@given(instance=SrcElement_strategy)
@settings(max_examples=50)
def test_srcelement_instantiation(instance):
    assert isinstance(instance, SrcElement)

@given(instance=jointPackage::PetriNet2PNML::SrcPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcplace_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcPlace)

@given(instance=TrgLocatedElement_strategy)
@settings(max_examples=50)
def test_trglocatedelement_instantiation(instance):
    assert isinstance(instance, TrgLocatedElement)

@given(instance=jointPackage::PetriNet2PNML::TrgIdedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgidedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgIdedElement)

@given(instance=jointPackage::PetriNet2PNML::TrgIdedElement_strategy)
def test_jointpackage::petrinet2pnml::trgidedelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=jointPackage::PetriNet2PNML::TrgIdedElement_strategy)
def test_jointpackage::petrinet2pnml::trgidedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jointPackage::PetriNet2PNML::TrgNetContent_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgnetcontent_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgNetContent)

@given(instance=jointPackage::PetriNet2PNML::TrgURI_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trguri_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgURI)

@given(instance=jointPackage::PetriNet2PNML::TrgURI_strategy)
def test_jointpackage::petrinet2pnml::trguri_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=jointPackage::PetriNet2PNML::TrgURI_strategy)
def test_jointpackage::petrinet2pnml::trguri_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jointPackage::PetriNet2PNML::TrgLabeledElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trglabeledelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgLabeledElement)

@given(instance=jointPackage::PetriNet2PNML::TrgLabel_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trglabel_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgLabel)

@given(instance=jointPackage::PetriNet2PNML::TrgLabel_strategy)
def test_jointpackage::petrinet2pnml::trglabel_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=jointPackage::PetriNet2PNML::TrgLabel_strategy)
def test_jointpackage::petrinet2pnml::trglabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SrcArc_strategy)
@settings(max_examples=50)
def test_srcarc_instantiation(instance):
    assert isinstance(instance, SrcArc)

@given(instance=jointPackage::PetriNet2PNML::SrcPlaceToTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcplacetotransition_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcPlaceToTransition)

@given(instance=jointPackage::PetriNet2PNML::SrcTransitionToPlace_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srctransitiontoplace_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcTransitionToPlace)

@given(instance=jointPackage::PetriNet2PNML::SrcTransition_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srctransition_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcTransition)

@given(instance=SrcNamedElement_strategy)
@settings(max_examples=50)
def test_srcnamedelement_instantiation(instance):
    assert isinstance(instance, SrcNamedElement)

@given(instance=jointPackage::PetriNet2PNML::SrcArc_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcarc_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcArc)

@given(instance=jointPackage::PetriNet2PNML::SrcArc_strategy)
def test_jointpackage::petrinet2pnml::srcarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=jointPackage::PetriNet2PNML::SrcArc_strategy)
def test_jointpackage::petrinet2pnml::srcarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=jointPackage::PetriNet2PNML::SrcElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcElement)

@given(instance=SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_srclocatedelement_instantiation(instance):
    assert isinstance(instance, SrcLocatedElement)

@given(instance=jointPackage::PetriNet2PNML::SrcNamedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcnamedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcNamedElement)

@given(instance=jointPackage::PetriNet2PNML::SrcNamedElement_strategy)
def test_jointpackage::petrinet2pnml::srcnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=jointPackage::PetriNet2PNML::SrcNamedElement_strategy)
def test_jointpackage::petrinet2pnml::srcnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jointPackage::PetriNet2PNML::SrcLocatedElement_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srclocatedelement_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcLocatedElement)

@given(instance=jointPackage::PetriNet2PNML::SrcLocatedElement_strategy)
def test_jointpackage::petrinet2pnml::srclocatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=jointPackage::PetriNet2PNML::SrcLocatedElement_strategy)
def test_jointpackage::petrinet2pnml::srclocatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=jointPackage::PetriNet2PNML::TrgPNMLDocument_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::trgpnmldocument_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::TrgPNMLDocument)

@given(instance=jointPackage::PetriNet2PNML::SrcPetriNet_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::srcpetrinet_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::SrcPetriNet)

@given(instance=jointPackage::PetriNet2PNML::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::petrinet2pnml::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::PetriNet2PNML::JointMM)

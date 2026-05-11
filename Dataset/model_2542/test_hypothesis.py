import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fastfst::nShftGagL,
    fastfst::nNcIMUzn,
    fastfst::vOutList,
    fastfst::aBldGagNd,
    fastfst::iNBlGages,
    fastfst::aTwrGagNd,
    fastfst::iNTwGages,
    fastfst::sOutFmt,
    fastfst::bTabDelim,
    fastfst::nNcIMUyn,
    fastfst::nNcIMUxn,
    fastfst::nSttsTime,
    fastfst::iDecFact,
    fastfst::nTStart,
    fastfst::fBldFile::3::,
    fastfst::fBldFile::2::,
    fastfst::bOutFileFmt,
    fastfst::bSumPrint,
    fastfst::fLinFile,
    fastfst::fADAMSFile,
    fastfst::fNoiseFile,
    fastfst::fADFile,
    fastfst::nTeetHStP,
    fastfst::nTeetSStP,
    fastfst::fBldFile::1::,
    fastfst::nTpBrDT,
    fastfst::nTBDrConD,
    fastfst::nTBDrConN,
    fastfst::nTeetHSSp,
    fastfst::nTeetSSSp,
    fastfst::nYawNeut,
    fastfst::nYawDamp,
    fastfst::nTeetCDmp,
    fastfst::nTeetDmp,
    fastfst::nTeetDmpP,
    fastfst::iTeetMod,
    fastfst::fFurlFile,
    fastfst::nTEC::RLR,
    fastfst::bFurling,
    fastfst::nTEC::SLR,
    fastfst::nYawSpr,
    fastfst::fTwrFile,
    fastfst::iTwrNodes,
    fastfst::fPtfmFile,
    fastfst::iPtfmModel,
    fastfst::nTEC::MR,
    fastfst::nSIG::SlPc,
    fastfst::nDTTorDmp,
    fastfst::nTEC::VLL,
    fastfst::nTEC::Rres,
    fastfst::nTEC::Sres,
    fastfst::nTEC::Npol,
    fastfst::nTEC::Freq,
    fastfst::nSIG::PORt,
    fastfst::nSIG::RtTq,
    fastfst::nSIG::SySp,
    fastfst::nGenIner,
    fastfst::nDTTorSpr,
    fastfst::fDynBrkFi,
    fastfst::nHSSBrDT,
    fastfst::nHSSBrTqF,
    fastfst::bGBRevers,
    fastfst::nGBRatio,
    fastfst::nGenEff,
    fastfst::nGBoxEff,
    fastfst::nHubIner,
    fastfst::nPreCone::2::,
    fastfst::nNacYIner,
    fastfst::nTipMass::3::,
    fastfst::nTipMass::2::,
    fastfst::nTipMass::1::,
    fastfst::nHubMass,
    fastfst::nNacMass,
    fastfst::nYawBrMass,
    fastfst::nAzimB1Up,
    fastfst::nPreCone::3::,
    fastfst::nNacCMxn,
    fastfst::nOverHang,
    fastfst::nHubCM,
    fastfst::nPreCone::1::,
    fastfst::nDelta3,
    fastfst::nShftTilt,
    fastfst::nTwrRBHt,
    fastfst::nTwr2Shft,
    fastfst::nTowerHt,
    fastfst::nNacCMzn,
    fastfst::nNacCMyn,
    fastfst::nTTDspSS,
    fastfst::nTTDspFA,
    fastfst::nNacYaw,
    fastfst::nRotSpeed,
    fastfst::nUndSling,
    fastfst::nPSpnElN,
    fastfst::nHubRad,
    fastfst::nTipRad,
    fastfst::bTwFADOF1,
    fastfst::bYawDOF,
    fastfst::bGenDOF,
    fastfst::bDrTrDOF,
    fastfst::bTeetDOF,
    fastfst::bEdgeDOF,
    fastfst::nAzimuth,
    fastfst::bFlapDOF2,
    fastfst::nTeetDefl,
    fastfst::bFlapDOF1,
    fastfst::nIPDefl,
    fastfst::nGravity,
    fastfst::nOoPDefl,
    fastfst::nBlPitchF::3::,
    fastfst::nBlPitchF::2::,
    fastfst::bCompNoise,
    fastfst::nBlPitchF::1::,
    fastfst::bCompAero,
    fastfst::nBlPitch::3::,
    fastfst::bTwSSDOF2,
    fastfst::nBlPitch::2::,
    fastfst::bTwSSDOF1,
    fastfst::bTwFADOF2,
    fastfst::nTPitManE::2::,
    fastfst::nTPitManE::1::,
    fastfst::nTPitManS::3::,
    fastfst::nTPitManS::2::,
    fastfst::nTPitManS::1::,
    fastfst::nNacYawF,
    fastfst::nTYawManE,
    fastfst::nTYawManS,
    fastfst::nTBDepISp::3::,
    fastfst::nTBDepISp::2::,
    fastfst::nTBDepISp::1::,
    fastfst::nTTpBrDp::3::,
    fastfst::nTTpBrDp::2::,
    fastfst::nTTpBrDp::1::,
    fastfst::nBlPitch::1::,
    fastfst::nTPitManE::3::,
    fastfst::iHSSBrMode,
    fastfst::nTimGenOf,
    fastfst::nTimGenOn,
    fastfst::nSpdGenOn,
    fastfst::bGenTiStp,
    fastfst::bGenTiStr,
    fastfst::iGenModel,
    fastfst::nVS::SlPc,
    fastfst::nVS::Rgn2K,
    fastfst::nVS::RtTq,
    fastfst::nVS::RtGnSp,
    fastfst::iVSContrl,
    fastfst::nTPCOn,
    fastfst::iPCMode,
    fastfst::nTYCOn,
    fastfst::iYCMode,
    fastfst::nDT,
    fastfst::nTMax,
    fastfst::nTiDynBrk,
    fastfst::nTHSSBrDp,
    fastfst::iADAMSPrep,
    fastfst::bEcho,
    fastfst::Section,
    fastfst::Header,
    fastfst::ModelFastfst,
    fastfst::iNumBl,
    fastfst::iAnalMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fastfst::nshftgagl_is_not_abstract():
    assert not inspect.isabstract(fastfst::nShftGagL)


def test_fastfst::nshftgagl_constructor_exists():
    assert callable(fastfst::nShftGagL.__init__)


def test_fastfst::nshftgagl_constructor_args():
    sig = inspect.signature(fastfst::nShftGagL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nshftgagl_has_name():
    assert hasattr(fastfst::nShftGagL, "name")
    descriptor = None
    for klass in fastfst::nShftGagL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nshftgagl_has_value():
    assert hasattr(fastfst::nShftGagL, "value")
    descriptor = None
    for klass in fastfst::nShftGagL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nncimuzn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNcIMUzn)


def test_fastfst::nncimuzn_constructor_exists():
    assert callable(fastfst::nNcIMUzn.__init__)


def test_fastfst::nncimuzn_constructor_args():
    sig = inspect.signature(fastfst::nNcIMUzn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nncimuzn_has_value():
    assert hasattr(fastfst::nNcIMUzn, "value")
    descriptor = None
    for klass in fastfst::nNcIMUzn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nncimuzn_has_name():
    assert hasattr(fastfst::nNcIMUzn, "name")
    descriptor = None
    for klass in fastfst::nNcIMUzn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::voutlist_is_not_abstract():
    assert not inspect.isabstract(fastfst::vOutList)


def test_fastfst::voutlist_constructor_exists():
    assert callable(fastfst::vOutList.__init__)


def test_fastfst::voutlist_constructor_args():
    sig = inspect.signature(fastfst::vOutList.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::voutlist_has_value():
    assert hasattr(fastfst::vOutList, "value")
    descriptor = None
    for klass in fastfst::vOutList.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::voutlist_has_name():
    assert hasattr(fastfst::vOutList, "name")
    descriptor = None
    for klass in fastfst::vOutList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::abldgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst::aBldGagNd)


def test_fastfst::abldgagnd_constructor_exists():
    assert callable(fastfst::aBldGagNd.__init__)


def test_fastfst::abldgagnd_constructor_args():
    sig = inspect.signature(fastfst::aBldGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::abldgagnd_has_name():
    assert hasattr(fastfst::aBldGagNd, "name")
    descriptor = None
    for klass in fastfst::aBldGagNd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::abldgagnd_has_value():
    assert hasattr(fastfst::aBldGagNd, "value")
    descriptor = None
    for klass in fastfst::aBldGagNd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::inblgages_is_not_abstract():
    assert not inspect.isabstract(fastfst::iNBlGages)


def test_fastfst::inblgages_constructor_exists():
    assert callable(fastfst::iNBlGages.__init__)


def test_fastfst::inblgages_constructor_args():
    sig = inspect.signature(fastfst::iNBlGages.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::inblgages_has_name():
    assert hasattr(fastfst::iNBlGages, "name")
    descriptor = None
    for klass in fastfst::iNBlGages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::inblgages_has_value():
    assert hasattr(fastfst::iNBlGages, "value")
    descriptor = None
    for klass in fastfst::iNBlGages.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::atwrgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst::aTwrGagNd)


def test_fastfst::atwrgagnd_constructor_exists():
    assert callable(fastfst::aTwrGagNd.__init__)


def test_fastfst::atwrgagnd_constructor_args():
    sig = inspect.signature(fastfst::aTwrGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::atwrgagnd_has_name():
    assert hasattr(fastfst::aTwrGagNd, "name")
    descriptor = None
    for klass in fastfst::aTwrGagNd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::atwrgagnd_has_value():
    assert hasattr(fastfst::aTwrGagNd, "value")
    descriptor = None
    for klass in fastfst::aTwrGagNd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::intwgages_is_not_abstract():
    assert not inspect.isabstract(fastfst::iNTwGages)


def test_fastfst::intwgages_constructor_exists():
    assert callable(fastfst::iNTwGages.__init__)


def test_fastfst::intwgages_constructor_args():
    sig = inspect.signature(fastfst::iNTwGages.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::intwgages_has_name():
    assert hasattr(fastfst::iNTwGages, "name")
    descriptor = None
    for klass in fastfst::iNTwGages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::intwgages_has_value():
    assert hasattr(fastfst::iNTwGages, "value")
    descriptor = None
    for klass in fastfst::iNTwGages.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::soutfmt_is_not_abstract():
    assert not inspect.isabstract(fastfst::sOutFmt)


def test_fastfst::soutfmt_constructor_exists():
    assert callable(fastfst::sOutFmt.__init__)


def test_fastfst::soutfmt_constructor_args():
    sig = inspect.signature(fastfst::sOutFmt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::soutfmt_has_name():
    assert hasattr(fastfst::sOutFmt, "name")
    descriptor = None
    for klass in fastfst::sOutFmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::soutfmt_has_value():
    assert hasattr(fastfst::sOutFmt, "value")
    descriptor = None
    for klass in fastfst::sOutFmt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::btabdelim_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTabDelim)


def test_fastfst::btabdelim_constructor_exists():
    assert callable(fastfst::bTabDelim.__init__)


def test_fastfst::btabdelim_constructor_args():
    sig = inspect.signature(fastfst::bTabDelim.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::btabdelim_has_name():
    assert hasattr(fastfst::bTabDelim, "name")
    descriptor = None
    for klass in fastfst::bTabDelim.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::btabdelim_has_value():
    assert hasattr(fastfst::bTabDelim, "value")
    descriptor = None
    for klass in fastfst::bTabDelim.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nncimuyn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNcIMUyn)


def test_fastfst::nncimuyn_constructor_exists():
    assert callable(fastfst::nNcIMUyn.__init__)


def test_fastfst::nncimuyn_constructor_args():
    sig = inspect.signature(fastfst::nNcIMUyn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nncimuyn_has_name():
    assert hasattr(fastfst::nNcIMUyn, "name")
    descriptor = None
    for klass in fastfst::nNcIMUyn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nncimuyn_has_value():
    assert hasattr(fastfst::nNcIMUyn, "value")
    descriptor = None
    for klass in fastfst::nNcIMUyn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nncimuxn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNcIMUxn)


def test_fastfst::nncimuxn_constructor_exists():
    assert callable(fastfst::nNcIMUxn.__init__)


def test_fastfst::nncimuxn_constructor_args():
    sig = inspect.signature(fastfst::nNcIMUxn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nncimuxn_has_value():
    assert hasattr(fastfst::nNcIMUxn, "value")
    descriptor = None
    for klass in fastfst::nNcIMUxn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nncimuxn_has_name():
    assert hasattr(fastfst::nNcIMUxn, "name")
    descriptor = None
    for klass in fastfst::nNcIMUxn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nsttstime_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSttsTime)


def test_fastfst::nsttstime_constructor_exists():
    assert callable(fastfst::nSttsTime.__init__)


def test_fastfst::nsttstime_constructor_args():
    sig = inspect.signature(fastfst::nSttsTime.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nsttstime_has_name():
    assert hasattr(fastfst::nSttsTime, "name")
    descriptor = None
    for klass in fastfst::nSttsTime.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nsttstime_has_value():
    assert hasattr(fastfst::nSttsTime, "value")
    descriptor = None
    for klass in fastfst::nSttsTime.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::idecfact_is_not_abstract():
    assert not inspect.isabstract(fastfst::iDecFact)


def test_fastfst::idecfact_constructor_exists():
    assert callable(fastfst::iDecFact.__init__)


def test_fastfst::idecfact_constructor_args():
    sig = inspect.signature(fastfst::iDecFact.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::idecfact_has_value():
    assert hasattr(fastfst::iDecFact, "value")
    descriptor = None
    for klass in fastfst::iDecFact.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::idecfact_has_name():
    assert hasattr(fastfst::iDecFact, "name")
    descriptor = None
    for klass in fastfst::iDecFact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntstart_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTStart)


def test_fastfst::ntstart_constructor_exists():
    assert callable(fastfst::nTStart.__init__)


def test_fastfst::ntstart_constructor_args():
    sig = inspect.signature(fastfst::nTStart.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntstart_has_value():
    assert hasattr(fastfst::nTStart, "value")
    descriptor = None
    for klass in fastfst::nTStart.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntstart_has_name():
    assert hasattr(fastfst::nTStart, "name")
    descriptor = None
    for klass in fastfst::nTStart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fbldfile::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::fBldFile::3::)


def test_fastfst::fbldfile::3::_constructor_exists():
    assert callable(fastfst::fBldFile::3::.__init__)


def test_fastfst::fbldfile::3::_constructor_args():
    sig = inspect.signature(fastfst::fBldFile::3::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::fbldfile::3::_has_name():
    assert hasattr(fastfst::fBldFile::3::, "name")
    descriptor = None
    for klass in fastfst::fBldFile::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fbldfile::3::_has_value():
    assert hasattr(fastfst::fBldFile::3::, "value")
    descriptor = None
    for klass in fastfst::fBldFile::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fbldfile::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::fBldFile::2::)


def test_fastfst::fbldfile::2::_constructor_exists():
    assert callable(fastfst::fBldFile::2::.__init__)


def test_fastfst::fbldfile::2::_constructor_args():
    sig = inspect.signature(fastfst::fBldFile::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::fbldfile::2::_has_value():
    assert hasattr(fastfst::fBldFile::2::, "value")
    descriptor = None
    for klass in fastfst::fBldFile::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fbldfile::2::_has_name():
    assert hasattr(fastfst::fBldFile::2::, "name")
    descriptor = None
    for klass in fastfst::fBldFile::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::boutfilefmt_is_not_abstract():
    assert not inspect.isabstract(fastfst::bOutFileFmt)


def test_fastfst::boutfilefmt_constructor_exists():
    assert callable(fastfst::bOutFileFmt.__init__)


def test_fastfst::boutfilefmt_constructor_args():
    sig = inspect.signature(fastfst::bOutFileFmt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::boutfilefmt_has_value():
    assert hasattr(fastfst::bOutFileFmt, "value")
    descriptor = None
    for klass in fastfst::bOutFileFmt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::boutfilefmt_has_name():
    assert hasattr(fastfst::bOutFileFmt, "name")
    descriptor = None
    for klass in fastfst::bOutFileFmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bsumprint_is_not_abstract():
    assert not inspect.isabstract(fastfst::bSumPrint)


def test_fastfst::bsumprint_constructor_exists():
    assert callable(fastfst::bSumPrint.__init__)


def test_fastfst::bsumprint_constructor_args():
    sig = inspect.signature(fastfst::bSumPrint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::bsumprint_has_value():
    assert hasattr(fastfst::bSumPrint, "value")
    descriptor = None
    for klass in fastfst::bSumPrint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bsumprint_has_name():
    assert hasattr(fastfst::bSumPrint, "name")
    descriptor = None
    for klass in fastfst::bSumPrint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::flinfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fLinFile)


def test_fastfst::flinfile_constructor_exists():
    assert callable(fastfst::fLinFile.__init__)


def test_fastfst::flinfile_constructor_args():
    sig = inspect.signature(fastfst::fLinFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::flinfile_has_value():
    assert hasattr(fastfst::fLinFile, "value")
    descriptor = None
    for klass in fastfst::fLinFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::flinfile_has_name():
    assert hasattr(fastfst::fLinFile, "name")
    descriptor = None
    for klass in fastfst::fLinFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fadamsfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fADAMSFile)


def test_fastfst::fadamsfile_constructor_exists():
    assert callable(fastfst::fADAMSFile.__init__)


def test_fastfst::fadamsfile_constructor_args():
    sig = inspect.signature(fastfst::fADAMSFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::fadamsfile_has_name():
    assert hasattr(fastfst::fADAMSFile, "name")
    descriptor = None
    for klass in fastfst::fADAMSFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fadamsfile_has_value():
    assert hasattr(fastfst::fADAMSFile, "value")
    descriptor = None
    for klass in fastfst::fADAMSFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fnoisefile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fNoiseFile)


def test_fastfst::fnoisefile_constructor_exists():
    assert callable(fastfst::fNoiseFile.__init__)


def test_fastfst::fnoisefile_constructor_args():
    sig = inspect.signature(fastfst::fNoiseFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::fnoisefile_has_name():
    assert hasattr(fastfst::fNoiseFile, "name")
    descriptor = None
    for klass in fastfst::fNoiseFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fnoisefile_has_value():
    assert hasattr(fastfst::fNoiseFile, "value")
    descriptor = None
    for klass in fastfst::fNoiseFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fadfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fADFile)


def test_fastfst::fadfile_constructor_exists():
    assert callable(fastfst::fADFile.__init__)


def test_fastfst::fadfile_constructor_args():
    sig = inspect.signature(fastfst::fADFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::fadfile_has_value():
    assert hasattr(fastfst::fADFile, "value")
    descriptor = None
    for klass in fastfst::fADFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fadfile_has_name():
    assert hasattr(fastfst::fADFile, "name")
    descriptor = None
    for klass in fastfst::fADFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteethstp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetHStP)


def test_fastfst::nteethstp_constructor_exists():
    assert callable(fastfst::nTeetHStP.__init__)


def test_fastfst::nteethstp_constructor_args():
    sig = inspect.signature(fastfst::nTeetHStP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteethstp_has_value():
    assert hasattr(fastfst::nTeetHStP, "value")
    descriptor = None
    for klass in fastfst::nTeetHStP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteethstp_has_name():
    assert hasattr(fastfst::nTeetHStP, "name")
    descriptor = None
    for klass in fastfst::nTeetHStP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetsstp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetSStP)


def test_fastfst::nteetsstp_constructor_exists():
    assert callable(fastfst::nTeetSStP.__init__)


def test_fastfst::nteetsstp_constructor_args():
    sig = inspect.signature(fastfst::nTeetSStP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteetsstp_has_value():
    assert hasattr(fastfst::nTeetSStP, "value")
    descriptor = None
    for klass in fastfst::nTeetSStP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetsstp_has_name():
    assert hasattr(fastfst::nTeetSStP, "name")
    descriptor = None
    for klass in fastfst::nTeetSStP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fbldfile::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::fBldFile::1::)


def test_fastfst::fbldfile::1::_constructor_exists():
    assert callable(fastfst::fBldFile::1::.__init__)


def test_fastfst::fbldfile::1::_constructor_args():
    sig = inspect.signature(fastfst::fBldFile::1::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::fbldfile::1::_has_value():
    assert hasattr(fastfst::fBldFile::1::, "value")
    descriptor = None
    for klass in fastfst::fBldFile::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fbldfile::1::_has_name():
    assert hasattr(fastfst::fBldFile::1::, "name")
    descriptor = None
    for klass in fastfst::fBldFile::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTpBrDT)


def test_fastfst::ntpbrdt_constructor_exists():
    assert callable(fastfst::nTpBrDT.__init__)


def test_fastfst::ntpbrdt_constructor_args():
    sig = inspect.signature(fastfst::nTpBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntpbrdt_has_name():
    assert hasattr(fastfst::nTpBrDT, "name")
    descriptor = None
    for klass in fastfst::nTpBrDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpbrdt_has_value():
    assert hasattr(fastfst::nTpBrDT, "value")
    descriptor = None
    for klass in fastfst::nTpBrDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntbdrcond_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTBDrConD)


def test_fastfst::ntbdrcond_constructor_exists():
    assert callable(fastfst::nTBDrConD.__init__)


def test_fastfst::ntbdrcond_constructor_args():
    sig = inspect.signature(fastfst::nTBDrConD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntbdrcond_has_name():
    assert hasattr(fastfst::nTBDrConD, "name")
    descriptor = None
    for klass in fastfst::nTBDrConD.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntbdrcond_has_value():
    assert hasattr(fastfst::nTBDrConD, "value")
    descriptor = None
    for klass in fastfst::nTBDrConD.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntbdrconn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTBDrConN)


def test_fastfst::ntbdrconn_constructor_exists():
    assert callable(fastfst::nTBDrConN.__init__)


def test_fastfst::ntbdrconn_constructor_args():
    sig = inspect.signature(fastfst::nTBDrConN.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntbdrconn_has_name():
    assert hasattr(fastfst::nTBDrConN, "name")
    descriptor = None
    for klass in fastfst::nTBDrConN.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntbdrconn_has_value():
    assert hasattr(fastfst::nTBDrConN, "value")
    descriptor = None
    for klass in fastfst::nTBDrConN.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteethssp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetHSSp)


def test_fastfst::nteethssp_constructor_exists():
    assert callable(fastfst::nTeetHSSp.__init__)


def test_fastfst::nteethssp_constructor_args():
    sig = inspect.signature(fastfst::nTeetHSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteethssp_has_value():
    assert hasattr(fastfst::nTeetHSSp, "value")
    descriptor = None
    for klass in fastfst::nTeetHSSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteethssp_has_name():
    assert hasattr(fastfst::nTeetHSSp, "name")
    descriptor = None
    for klass in fastfst::nTeetHSSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetsssp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetSSSp)


def test_fastfst::nteetsssp_constructor_exists():
    assert callable(fastfst::nTeetSSSp.__init__)


def test_fastfst::nteetsssp_constructor_args():
    sig = inspect.signature(fastfst::nTeetSSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteetsssp_has_value():
    assert hasattr(fastfst::nTeetSSSp, "value")
    descriptor = None
    for klass in fastfst::nTeetSSSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetsssp_has_name():
    assert hasattr(fastfst::nTeetSSSp, "name")
    descriptor = None
    for klass in fastfst::nTeetSSSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nyawneut_is_not_abstract():
    assert not inspect.isabstract(fastfst::nYawNeut)


def test_fastfst::nyawneut_constructor_exists():
    assert callable(fastfst::nYawNeut.__init__)


def test_fastfst::nyawneut_constructor_args():
    sig = inspect.signature(fastfst::nYawNeut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nyawneut_has_value():
    assert hasattr(fastfst::nYawNeut, "value")
    descriptor = None
    for klass in fastfst::nYawNeut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nyawneut_has_name():
    assert hasattr(fastfst::nYawNeut, "name")
    descriptor = None
    for klass in fastfst::nYawNeut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nyawdamp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nYawDamp)


def test_fastfst::nyawdamp_constructor_exists():
    assert callable(fastfst::nYawDamp.__init__)


def test_fastfst::nyawdamp_constructor_args():
    sig = inspect.signature(fastfst::nYawDamp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nyawdamp_has_value():
    assert hasattr(fastfst::nYawDamp, "value")
    descriptor = None
    for klass in fastfst::nYawDamp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nyawdamp_has_name():
    assert hasattr(fastfst::nYawDamp, "name")
    descriptor = None
    for klass in fastfst::nYawDamp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetcdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetCDmp)


def test_fastfst::nteetcdmp_constructor_exists():
    assert callable(fastfst::nTeetCDmp.__init__)


def test_fastfst::nteetcdmp_constructor_args():
    sig = inspect.signature(fastfst::nTeetCDmp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nteetcdmp_has_name():
    assert hasattr(fastfst::nTeetCDmp, "name")
    descriptor = None
    for klass in fastfst::nTeetCDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetcdmp_has_value():
    assert hasattr(fastfst::nTeetCDmp, "value")
    descriptor = None
    for klass in fastfst::nTeetCDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetDmp)


def test_fastfst::nteetdmp_constructor_exists():
    assert callable(fastfst::nTeetDmp.__init__)


def test_fastfst::nteetdmp_constructor_args():
    sig = inspect.signature(fastfst::nTeetDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteetdmp_has_value():
    assert hasattr(fastfst::nTeetDmp, "value")
    descriptor = None
    for klass in fastfst::nTeetDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetdmp_has_name():
    assert hasattr(fastfst::nTeetDmp, "name")
    descriptor = None
    for klass in fastfst::nTeetDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetdmpp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetDmpP)


def test_fastfst::nteetdmpp_constructor_exists():
    assert callable(fastfst::nTeetDmpP.__init__)


def test_fastfst::nteetdmpp_constructor_args():
    sig = inspect.signature(fastfst::nTeetDmpP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteetdmpp_has_value():
    assert hasattr(fastfst::nTeetDmpP, "value")
    descriptor = None
    for klass in fastfst::nTeetDmpP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetdmpp_has_name():
    assert hasattr(fastfst::nTeetDmpP, "name")
    descriptor = None
    for klass in fastfst::nTeetDmpP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::iteetmod_is_not_abstract():
    assert not inspect.isabstract(fastfst::iTeetMod)


def test_fastfst::iteetmod_constructor_exists():
    assert callable(fastfst::iTeetMod.__init__)


def test_fastfst::iteetmod_constructor_args():
    sig = inspect.signature(fastfst::iTeetMod.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::iteetmod_has_value():
    assert hasattr(fastfst::iTeetMod, "value")
    descriptor = None
    for klass in fastfst::iTeetMod.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::iteetmod_has_name():
    assert hasattr(fastfst::iTeetMod, "name")
    descriptor = None
    for klass in fastfst::iTeetMod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ffurlfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fFurlFile)


def test_fastfst::ffurlfile_constructor_exists():
    assert callable(fastfst::fFurlFile.__init__)


def test_fastfst::ffurlfile_constructor_args():
    sig = inspect.signature(fastfst::fFurlFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ffurlfile_has_name():
    assert hasattr(fastfst::fFurlFile, "name")
    descriptor = None
    for klass in fastfst::fFurlFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ffurlfile_has_value():
    assert hasattr(fastfst::fFurlFile, "value")
    descriptor = None
    for klass in fastfst::fFurlFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::rlr_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::RLR)


def test_fastfst::ntec::rlr_constructor_exists():
    assert callable(fastfst::nTEC::RLR.__init__)


def test_fastfst::ntec::rlr_constructor_args():
    sig = inspect.signature(fastfst::nTEC::RLR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntec::rlr_has_value():
    assert hasattr(fastfst::nTEC::RLR, "value")
    descriptor = None
    for klass in fastfst::nTEC::RLR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::rlr_has_name():
    assert hasattr(fastfst::nTEC::RLR, "name")
    descriptor = None
    for klass in fastfst::nTEC::RLR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bfurling_is_not_abstract():
    assert not inspect.isabstract(fastfst::bFurling)


def test_fastfst::bfurling_constructor_exists():
    assert callable(fastfst::bFurling.__init__)


def test_fastfst::bfurling_constructor_args():
    sig = inspect.signature(fastfst::bFurling.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bfurling_has_name():
    assert hasattr(fastfst::bFurling, "name")
    descriptor = None
    for klass in fastfst::bFurling.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bfurling_has_value():
    assert hasattr(fastfst::bFurling, "value")
    descriptor = None
    for klass in fastfst::bFurling.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::slr_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::SLR)


def test_fastfst::ntec::slr_constructor_exists():
    assert callable(fastfst::nTEC::SLR.__init__)


def test_fastfst::ntec::slr_constructor_args():
    sig = inspect.signature(fastfst::nTEC::SLR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntec::slr_has_value():
    assert hasattr(fastfst::nTEC::SLR, "value")
    descriptor = None
    for klass in fastfst::nTEC::SLR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::slr_has_name():
    assert hasattr(fastfst::nTEC::SLR, "name")
    descriptor = None
    for klass in fastfst::nTEC::SLR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nyawspr_is_not_abstract():
    assert not inspect.isabstract(fastfst::nYawSpr)


def test_fastfst::nyawspr_constructor_exists():
    assert callable(fastfst::nYawSpr.__init__)


def test_fastfst::nyawspr_constructor_args():
    sig = inspect.signature(fastfst::nYawSpr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nyawspr_has_name():
    assert hasattr(fastfst::nYawSpr, "name")
    descriptor = None
    for klass in fastfst::nYawSpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nyawspr_has_value():
    assert hasattr(fastfst::nYawSpr, "value")
    descriptor = None
    for klass in fastfst::nYawSpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ftwrfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fTwrFile)


def test_fastfst::ftwrfile_constructor_exists():
    assert callable(fastfst::fTwrFile.__init__)


def test_fastfst::ftwrfile_constructor_args():
    sig = inspect.signature(fastfst::fTwrFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ftwrfile_has_name():
    assert hasattr(fastfst::fTwrFile, "name")
    descriptor = None
    for klass in fastfst::fTwrFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ftwrfile_has_value():
    assert hasattr(fastfst::fTwrFile, "value")
    descriptor = None
    for klass in fastfst::fTwrFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::itwrnodes_is_not_abstract():
    assert not inspect.isabstract(fastfst::iTwrNodes)


def test_fastfst::itwrnodes_constructor_exists():
    assert callable(fastfst::iTwrNodes.__init__)


def test_fastfst::itwrnodes_constructor_args():
    sig = inspect.signature(fastfst::iTwrNodes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::itwrnodes_has_name():
    assert hasattr(fastfst::iTwrNodes, "name")
    descriptor = None
    for klass in fastfst::iTwrNodes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::itwrnodes_has_value():
    assert hasattr(fastfst::iTwrNodes, "value")
    descriptor = None
    for klass in fastfst::iTwrNodes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fptfmfile_is_not_abstract():
    assert not inspect.isabstract(fastfst::fPtfmFile)


def test_fastfst::fptfmfile_constructor_exists():
    assert callable(fastfst::fPtfmFile.__init__)


def test_fastfst::fptfmfile_constructor_args():
    sig = inspect.signature(fastfst::fPtfmFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::fptfmfile_has_name():
    assert hasattr(fastfst::fPtfmFile, "name")
    descriptor = None
    for klass in fastfst::fPtfmFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fptfmfile_has_value():
    assert hasattr(fastfst::fPtfmFile, "value")
    descriptor = None
    for klass in fastfst::fPtfmFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::iptfmmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst::iPtfmModel)


def test_fastfst::iptfmmodel_constructor_exists():
    assert callable(fastfst::iPtfmModel.__init__)


def test_fastfst::iptfmmodel_constructor_args():
    sig = inspect.signature(fastfst::iPtfmModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::iptfmmodel_has_name():
    assert hasattr(fastfst::iPtfmModel, "name")
    descriptor = None
    for klass in fastfst::iPtfmModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::iptfmmodel_has_value():
    assert hasattr(fastfst::iPtfmModel, "value")
    descriptor = None
    for klass in fastfst::iPtfmModel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::mr_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::MR)


def test_fastfst::ntec::mr_constructor_exists():
    assert callable(fastfst::nTEC::MR.__init__)


def test_fastfst::ntec::mr_constructor_args():
    sig = inspect.signature(fastfst::nTEC::MR.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntec::mr_has_name():
    assert hasattr(fastfst::nTEC::MR, "name")
    descriptor = None
    for klass in fastfst::nTEC::MR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::mr_has_value():
    assert hasattr(fastfst::nTEC::MR, "value")
    descriptor = None
    for klass in fastfst::nTEC::MR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nsig::slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSIG::SlPc)


def test_fastfst::nsig::slpc_constructor_exists():
    assert callable(fastfst::nSIG::SlPc.__init__)


def test_fastfst::nsig::slpc_constructor_args():
    sig = inspect.signature(fastfst::nSIG::SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nsig::slpc_has_name():
    assert hasattr(fastfst::nSIG::SlPc, "name")
    descriptor = None
    for klass in fastfst::nSIG::SlPc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nsig::slpc_has_value():
    assert hasattr(fastfst::nSIG::SlPc, "value")
    descriptor = None
    for klass in fastfst::nSIG::SlPc.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ndttordmp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nDTTorDmp)


def test_fastfst::ndttordmp_constructor_exists():
    assert callable(fastfst::nDTTorDmp.__init__)


def test_fastfst::ndttordmp_constructor_args():
    sig = inspect.signature(fastfst::nDTTorDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ndttordmp_has_value():
    assert hasattr(fastfst::nDTTorDmp, "value")
    descriptor = None
    for klass in fastfst::nDTTorDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ndttordmp_has_name():
    assert hasattr(fastfst::nDTTorDmp, "name")
    descriptor = None
    for klass in fastfst::nDTTorDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::vll_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::VLL)


def test_fastfst::ntec::vll_constructor_exists():
    assert callable(fastfst::nTEC::VLL.__init__)


def test_fastfst::ntec::vll_constructor_args():
    sig = inspect.signature(fastfst::nTEC::VLL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntec::vll_has_name():
    assert hasattr(fastfst::nTEC::VLL, "name")
    descriptor = None
    for klass in fastfst::nTEC::VLL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::vll_has_value():
    assert hasattr(fastfst::nTEC::VLL, "value")
    descriptor = None
    for klass in fastfst::nTEC::VLL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::rres_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::Rres)


def test_fastfst::ntec::rres_constructor_exists():
    assert callable(fastfst::nTEC::Rres.__init__)


def test_fastfst::ntec::rres_constructor_args():
    sig = inspect.signature(fastfst::nTEC::Rres.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntec::rres_has_value():
    assert hasattr(fastfst::nTEC::Rres, "value")
    descriptor = None
    for klass in fastfst::nTEC::Rres.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::rres_has_name():
    assert hasattr(fastfst::nTEC::Rres, "name")
    descriptor = None
    for klass in fastfst::nTEC::Rres.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::sres_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::Sres)


def test_fastfst::ntec::sres_constructor_exists():
    assert callable(fastfst::nTEC::Sres.__init__)


def test_fastfst::ntec::sres_constructor_args():
    sig = inspect.signature(fastfst::nTEC::Sres.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntec::sres_has_value():
    assert hasattr(fastfst::nTEC::Sres, "value")
    descriptor = None
    for klass in fastfst::nTEC::Sres.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::sres_has_name():
    assert hasattr(fastfst::nTEC::Sres, "name")
    descriptor = None
    for klass in fastfst::nTEC::Sres.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::npol_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::Npol)


def test_fastfst::ntec::npol_constructor_exists():
    assert callable(fastfst::nTEC::Npol.__init__)


def test_fastfst::ntec::npol_constructor_args():
    sig = inspect.signature(fastfst::nTEC::Npol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntec::npol_has_name():
    assert hasattr(fastfst::nTEC::Npol, "name")
    descriptor = None
    for klass in fastfst::nTEC::Npol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::npol_has_value():
    assert hasattr(fastfst::nTEC::Npol, "value")
    descriptor = None
    for klass in fastfst::nTEC::Npol.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntec::freq_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTEC::Freq)


def test_fastfst::ntec::freq_constructor_exists():
    assert callable(fastfst::nTEC::Freq.__init__)


def test_fastfst::ntec::freq_constructor_args():
    sig = inspect.signature(fastfst::nTEC::Freq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntec::freq_has_value():
    assert hasattr(fastfst::nTEC::Freq, "value")
    descriptor = None
    for klass in fastfst::nTEC::Freq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntec::freq_has_name():
    assert hasattr(fastfst::nTEC::Freq, "name")
    descriptor = None
    for klass in fastfst::nTEC::Freq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nsig::port_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSIG::PORt)


def test_fastfst::nsig::port_constructor_exists():
    assert callable(fastfst::nSIG::PORt.__init__)


def test_fastfst::nsig::port_constructor_args():
    sig = inspect.signature(fastfst::nSIG::PORt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nsig::port_has_name():
    assert hasattr(fastfst::nSIG::PORt, "name")
    descriptor = None
    for klass in fastfst::nSIG::PORt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nsig::port_has_value():
    assert hasattr(fastfst::nSIG::PORt, "value")
    descriptor = None
    for klass in fastfst::nSIG::PORt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nsig::rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSIG::RtTq)


def test_fastfst::nsig::rttq_constructor_exists():
    assert callable(fastfst::nSIG::RtTq.__init__)


def test_fastfst::nsig::rttq_constructor_args():
    sig = inspect.signature(fastfst::nSIG::RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nsig::rttq_has_value():
    assert hasattr(fastfst::nSIG::RtTq, "value")
    descriptor = None
    for klass in fastfst::nSIG::RtTq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nsig::rttq_has_name():
    assert hasattr(fastfst::nSIG::RtTq, "name")
    descriptor = None
    for klass in fastfst::nSIG::RtTq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nsig::sysp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSIG::SySp)


def test_fastfst::nsig::sysp_constructor_exists():
    assert callable(fastfst::nSIG::SySp.__init__)


def test_fastfst::nsig::sysp_constructor_args():
    sig = inspect.signature(fastfst::nSIG::SySp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nsig::sysp_has_name():
    assert hasattr(fastfst::nSIG::SySp, "name")
    descriptor = None
    for klass in fastfst::nSIG::SySp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nsig::sysp_has_value():
    assert hasattr(fastfst::nSIG::SySp, "value")
    descriptor = None
    for klass in fastfst::nSIG::SySp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ngeniner_is_not_abstract():
    assert not inspect.isabstract(fastfst::nGenIner)


def test_fastfst::ngeniner_constructor_exists():
    assert callable(fastfst::nGenIner.__init__)


def test_fastfst::ngeniner_constructor_args():
    sig = inspect.signature(fastfst::nGenIner.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ngeniner_has_value():
    assert hasattr(fastfst::nGenIner, "value")
    descriptor = None
    for klass in fastfst::nGenIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ngeniner_has_name():
    assert hasattr(fastfst::nGenIner, "name")
    descriptor = None
    for klass in fastfst::nGenIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ndttorspr_is_not_abstract():
    assert not inspect.isabstract(fastfst::nDTTorSpr)


def test_fastfst::ndttorspr_constructor_exists():
    assert callable(fastfst::nDTTorSpr.__init__)


def test_fastfst::ndttorspr_constructor_args():
    sig = inspect.signature(fastfst::nDTTorSpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ndttorspr_has_value():
    assert hasattr(fastfst::nDTTorSpr, "value")
    descriptor = None
    for klass in fastfst::nDTTorSpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ndttorspr_has_name():
    assert hasattr(fastfst::nDTTorSpr, "name")
    descriptor = None
    for klass in fastfst::nDTTorSpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::fdynbrkfi_is_not_abstract():
    assert not inspect.isabstract(fastfst::fDynBrkFi)


def test_fastfst::fdynbrkfi_constructor_exists():
    assert callable(fastfst::fDynBrkFi.__init__)


def test_fastfst::fdynbrkfi_constructor_args():
    sig = inspect.signature(fastfst::fDynBrkFi.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::fdynbrkfi_has_name():
    assert hasattr(fastfst::fDynBrkFi, "name")
    descriptor = None
    for klass in fastfst::fDynBrkFi.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::fdynbrkfi_has_value():
    assert hasattr(fastfst::fDynBrkFi, "value")
    descriptor = None
    for klass in fastfst::fDynBrkFi.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhssbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHSSBrDT)


def test_fastfst::nhssbrdt_constructor_exists():
    assert callable(fastfst::nHSSBrDT.__init__)


def test_fastfst::nhssbrdt_constructor_args():
    sig = inspect.signature(fastfst::nHSSBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nhssbrdt_has_value():
    assert hasattr(fastfst::nHSSBrDT, "value")
    descriptor = None
    for klass in fastfst::nHSSBrDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhssbrdt_has_name():
    assert hasattr(fastfst::nHSSBrDT, "name")
    descriptor = None
    for klass in fastfst::nHSSBrDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhssbrtqf_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHSSBrTqF)


def test_fastfst::nhssbrtqf_constructor_exists():
    assert callable(fastfst::nHSSBrTqF.__init__)


def test_fastfst::nhssbrtqf_constructor_args():
    sig = inspect.signature(fastfst::nHSSBrTqF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nhssbrtqf_has_name():
    assert hasattr(fastfst::nHSSBrTqF, "name")
    descriptor = None
    for klass in fastfst::nHSSBrTqF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhssbrtqf_has_value():
    assert hasattr(fastfst::nHSSBrTqF, "value")
    descriptor = None
    for klass in fastfst::nHSSBrTqF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bgbrevers_is_not_abstract():
    assert not inspect.isabstract(fastfst::bGBRevers)


def test_fastfst::bgbrevers_constructor_exists():
    assert callable(fastfst::bGBRevers.__init__)


def test_fastfst::bgbrevers_constructor_args():
    sig = inspect.signature(fastfst::bGBRevers.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::bgbrevers_has_value():
    assert hasattr(fastfst::bGBRevers, "value")
    descriptor = None
    for klass in fastfst::bGBRevers.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bgbrevers_has_name():
    assert hasattr(fastfst::bGBRevers, "name")
    descriptor = None
    for klass in fastfst::bGBRevers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ngbratio_is_not_abstract():
    assert not inspect.isabstract(fastfst::nGBRatio)


def test_fastfst::ngbratio_constructor_exists():
    assert callable(fastfst::nGBRatio.__init__)


def test_fastfst::ngbratio_constructor_args():
    sig = inspect.signature(fastfst::nGBRatio.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ngbratio_has_name():
    assert hasattr(fastfst::nGBRatio, "name")
    descriptor = None
    for klass in fastfst::nGBRatio.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ngbratio_has_value():
    assert hasattr(fastfst::nGBRatio, "value")
    descriptor = None
    for klass in fastfst::nGBRatio.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ngeneff_is_not_abstract():
    assert not inspect.isabstract(fastfst::nGenEff)


def test_fastfst::ngeneff_constructor_exists():
    assert callable(fastfst::nGenEff.__init__)


def test_fastfst::ngeneff_constructor_args():
    sig = inspect.signature(fastfst::nGenEff.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ngeneff_has_value():
    assert hasattr(fastfst::nGenEff, "value")
    descriptor = None
    for klass in fastfst::nGenEff.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ngeneff_has_name():
    assert hasattr(fastfst::nGenEff, "name")
    descriptor = None
    for klass in fastfst::nGenEff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ngboxeff_is_not_abstract():
    assert not inspect.isabstract(fastfst::nGBoxEff)


def test_fastfst::ngboxeff_constructor_exists():
    assert callable(fastfst::nGBoxEff.__init__)


def test_fastfst::ngboxeff_constructor_args():
    sig = inspect.signature(fastfst::nGBoxEff.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ngboxeff_has_value():
    assert hasattr(fastfst::nGBoxEff, "value")
    descriptor = None
    for klass in fastfst::nGBoxEff.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ngboxeff_has_name():
    assert hasattr(fastfst::nGBoxEff, "name")
    descriptor = None
    for klass in fastfst::nGBoxEff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhubiner_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHubIner)


def test_fastfst::nhubiner_constructor_exists():
    assert callable(fastfst::nHubIner.__init__)


def test_fastfst::nhubiner_constructor_args():
    sig = inspect.signature(fastfst::nHubIner.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nhubiner_has_value():
    assert hasattr(fastfst::nHubIner, "value")
    descriptor = None
    for klass in fastfst::nHubIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhubiner_has_name():
    assert hasattr(fastfst::nHubIner, "name")
    descriptor = None
    for klass in fastfst::nHubIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nprecone::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nPreCone::2::)


def test_fastfst::nprecone::2::_constructor_exists():
    assert callable(fastfst::nPreCone::2::.__init__)


def test_fastfst::nprecone::2::_constructor_args():
    sig = inspect.signature(fastfst::nPreCone::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nprecone::2::_has_value():
    assert hasattr(fastfst::nPreCone::2::, "value")
    descriptor = None
    for klass in fastfst::nPreCone::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nprecone::2::_has_name():
    assert hasattr(fastfst::nPreCone::2::, "name")
    descriptor = None
    for klass in fastfst::nPreCone::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnacyiner_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacYIner)


def test_fastfst::nnacyiner_constructor_exists():
    assert callable(fastfst::nNacYIner.__init__)


def test_fastfst::nnacyiner_constructor_args():
    sig = inspect.signature(fastfst::nNacYIner.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nnacyiner_has_value():
    assert hasattr(fastfst::nNacYIner, "value")
    descriptor = None
    for klass in fastfst::nNacYIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnacyiner_has_name():
    assert hasattr(fastfst::nNacYIner, "name")
    descriptor = None
    for klass in fastfst::nNacYIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntipmass::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTipMass::3::)


def test_fastfst::ntipmass::3::_constructor_exists():
    assert callable(fastfst::nTipMass::3::.__init__)


def test_fastfst::ntipmass::3::_constructor_args():
    sig = inspect.signature(fastfst::nTipMass::3::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntipmass::3::_has_value():
    assert hasattr(fastfst::nTipMass::3::, "value")
    descriptor = None
    for klass in fastfst::nTipMass::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntipmass::3::_has_name():
    assert hasattr(fastfst::nTipMass::3::, "name")
    descriptor = None
    for klass in fastfst::nTipMass::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntipmass::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTipMass::2::)


def test_fastfst::ntipmass::2::_constructor_exists():
    assert callable(fastfst::nTipMass::2::.__init__)


def test_fastfst::ntipmass::2::_constructor_args():
    sig = inspect.signature(fastfst::nTipMass::2::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntipmass::2::_has_name():
    assert hasattr(fastfst::nTipMass::2::, "name")
    descriptor = None
    for klass in fastfst::nTipMass::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntipmass::2::_has_value():
    assert hasattr(fastfst::nTipMass::2::, "value")
    descriptor = None
    for klass in fastfst::nTipMass::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntipmass::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTipMass::1::)


def test_fastfst::ntipmass::1::_constructor_exists():
    assert callable(fastfst::nTipMass::1::.__init__)


def test_fastfst::ntipmass::1::_constructor_args():
    sig = inspect.signature(fastfst::nTipMass::1::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntipmass::1::_has_name():
    assert hasattr(fastfst::nTipMass::1::, "name")
    descriptor = None
    for klass in fastfst::nTipMass::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntipmass::1::_has_value():
    assert hasattr(fastfst::nTipMass::1::, "value")
    descriptor = None
    for klass in fastfst::nTipMass::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhubmass_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHubMass)


def test_fastfst::nhubmass_constructor_exists():
    assert callable(fastfst::nHubMass.__init__)


def test_fastfst::nhubmass_constructor_args():
    sig = inspect.signature(fastfst::nHubMass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nhubmass_has_name():
    assert hasattr(fastfst::nHubMass, "name")
    descriptor = None
    for klass in fastfst::nHubMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhubmass_has_value():
    assert hasattr(fastfst::nHubMass, "value")
    descriptor = None
    for klass in fastfst::nHubMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnacmass_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacMass)


def test_fastfst::nnacmass_constructor_exists():
    assert callable(fastfst::nNacMass.__init__)


def test_fastfst::nnacmass_constructor_args():
    sig = inspect.signature(fastfst::nNacMass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nnacmass_has_name():
    assert hasattr(fastfst::nNacMass, "name")
    descriptor = None
    for klass in fastfst::nNacMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnacmass_has_value():
    assert hasattr(fastfst::nNacMass, "value")
    descriptor = None
    for klass in fastfst::nNacMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nyawbrmass_is_not_abstract():
    assert not inspect.isabstract(fastfst::nYawBrMass)


def test_fastfst::nyawbrmass_constructor_exists():
    assert callable(fastfst::nYawBrMass.__init__)


def test_fastfst::nyawbrmass_constructor_args():
    sig = inspect.signature(fastfst::nYawBrMass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nyawbrmass_has_name():
    assert hasattr(fastfst::nYawBrMass, "name")
    descriptor = None
    for klass in fastfst::nYawBrMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nyawbrmass_has_value():
    assert hasattr(fastfst::nYawBrMass, "value")
    descriptor = None
    for klass in fastfst::nYawBrMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nazimb1up_is_not_abstract():
    assert not inspect.isabstract(fastfst::nAzimB1Up)


def test_fastfst::nazimb1up_constructor_exists():
    assert callable(fastfst::nAzimB1Up.__init__)


def test_fastfst::nazimb1up_constructor_args():
    sig = inspect.signature(fastfst::nAzimB1Up.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nazimb1up_has_name():
    assert hasattr(fastfst::nAzimB1Up, "name")
    descriptor = None
    for klass in fastfst::nAzimB1Up.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nazimb1up_has_value():
    assert hasattr(fastfst::nAzimB1Up, "value")
    descriptor = None
    for klass in fastfst::nAzimB1Up.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nprecone::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nPreCone::3::)


def test_fastfst::nprecone::3::_constructor_exists():
    assert callable(fastfst::nPreCone::3::.__init__)


def test_fastfst::nprecone::3::_constructor_args():
    sig = inspect.signature(fastfst::nPreCone::3::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nprecone::3::_has_value():
    assert hasattr(fastfst::nPreCone::3::, "value")
    descriptor = None
    for klass in fastfst::nPreCone::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nprecone::3::_has_name():
    assert hasattr(fastfst::nPreCone::3::, "name")
    descriptor = None
    for klass in fastfst::nPreCone::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnaccmxn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacCMxn)


def test_fastfst::nnaccmxn_constructor_exists():
    assert callable(fastfst::nNacCMxn.__init__)


def test_fastfst::nnaccmxn_constructor_args():
    sig = inspect.signature(fastfst::nNacCMxn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nnaccmxn_has_value():
    assert hasattr(fastfst::nNacCMxn, "value")
    descriptor = None
    for klass in fastfst::nNacCMxn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnaccmxn_has_name():
    assert hasattr(fastfst::nNacCMxn, "name")
    descriptor = None
    for klass in fastfst::nNacCMxn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::noverhang_is_not_abstract():
    assert not inspect.isabstract(fastfst::nOverHang)


def test_fastfst::noverhang_constructor_exists():
    assert callable(fastfst::nOverHang.__init__)


def test_fastfst::noverhang_constructor_args():
    sig = inspect.signature(fastfst::nOverHang.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::noverhang_has_name():
    assert hasattr(fastfst::nOverHang, "name")
    descriptor = None
    for klass in fastfst::nOverHang.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::noverhang_has_value():
    assert hasattr(fastfst::nOverHang, "value")
    descriptor = None
    for klass in fastfst::nOverHang.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhubcm_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHubCM)


def test_fastfst::nhubcm_constructor_exists():
    assert callable(fastfst::nHubCM.__init__)


def test_fastfst::nhubcm_constructor_args():
    sig = inspect.signature(fastfst::nHubCM.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nhubcm_has_value():
    assert hasattr(fastfst::nHubCM, "value")
    descriptor = None
    for klass in fastfst::nHubCM.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhubcm_has_name():
    assert hasattr(fastfst::nHubCM, "name")
    descriptor = None
    for klass in fastfst::nHubCM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nprecone::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nPreCone::1::)


def test_fastfst::nprecone::1::_constructor_exists():
    assert callable(fastfst::nPreCone::1::.__init__)


def test_fastfst::nprecone::1::_constructor_args():
    sig = inspect.signature(fastfst::nPreCone::1::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nprecone::1::_has_name():
    assert hasattr(fastfst::nPreCone::1::, "name")
    descriptor = None
    for klass in fastfst::nPreCone::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nprecone::1::_has_value():
    assert hasattr(fastfst::nPreCone::1::, "value")
    descriptor = None
    for klass in fastfst::nPreCone::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ndelta3_is_not_abstract():
    assert not inspect.isabstract(fastfst::nDelta3)


def test_fastfst::ndelta3_constructor_exists():
    assert callable(fastfst::nDelta3.__init__)


def test_fastfst::ndelta3_constructor_args():
    sig = inspect.signature(fastfst::nDelta3.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ndelta3_has_value():
    assert hasattr(fastfst::nDelta3, "value")
    descriptor = None
    for klass in fastfst::nDelta3.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ndelta3_has_name():
    assert hasattr(fastfst::nDelta3, "name")
    descriptor = None
    for klass in fastfst::nDelta3.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nshfttilt_is_not_abstract():
    assert not inspect.isabstract(fastfst::nShftTilt)


def test_fastfst::nshfttilt_constructor_exists():
    assert callable(fastfst::nShftTilt.__init__)


def test_fastfst::nshfttilt_constructor_args():
    sig = inspect.signature(fastfst::nShftTilt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nshfttilt_has_value():
    assert hasattr(fastfst::nShftTilt, "value")
    descriptor = None
    for klass in fastfst::nShftTilt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nshfttilt_has_name():
    assert hasattr(fastfst::nShftTilt, "name")
    descriptor = None
    for klass in fastfst::nShftTilt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntwrrbht_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTwrRBHt)


def test_fastfst::ntwrrbht_constructor_exists():
    assert callable(fastfst::nTwrRBHt.__init__)


def test_fastfst::ntwrrbht_constructor_args():
    sig = inspect.signature(fastfst::nTwrRBHt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntwrrbht_has_value():
    assert hasattr(fastfst::nTwrRBHt, "value")
    descriptor = None
    for klass in fastfst::nTwrRBHt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntwrrbht_has_name():
    assert hasattr(fastfst::nTwrRBHt, "name")
    descriptor = None
    for klass in fastfst::nTwrRBHt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntwr2shft_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTwr2Shft)


def test_fastfst::ntwr2shft_constructor_exists():
    assert callable(fastfst::nTwr2Shft.__init__)


def test_fastfst::ntwr2shft_constructor_args():
    sig = inspect.signature(fastfst::nTwr2Shft.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntwr2shft_has_name():
    assert hasattr(fastfst::nTwr2Shft, "name")
    descriptor = None
    for klass in fastfst::nTwr2Shft.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntwr2shft_has_value():
    assert hasattr(fastfst::nTwr2Shft, "value")
    descriptor = None
    for klass in fastfst::nTwr2Shft.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntowerht_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTowerHt)


def test_fastfst::ntowerht_constructor_exists():
    assert callable(fastfst::nTowerHt.__init__)


def test_fastfst::ntowerht_constructor_args():
    sig = inspect.signature(fastfst::nTowerHt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntowerht_has_value():
    assert hasattr(fastfst::nTowerHt, "value")
    descriptor = None
    for klass in fastfst::nTowerHt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntowerht_has_name():
    assert hasattr(fastfst::nTowerHt, "name")
    descriptor = None
    for klass in fastfst::nTowerHt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnaccmzn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacCMzn)


def test_fastfst::nnaccmzn_constructor_exists():
    assert callable(fastfst::nNacCMzn.__init__)


def test_fastfst::nnaccmzn_constructor_args():
    sig = inspect.signature(fastfst::nNacCMzn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nnaccmzn_has_name():
    assert hasattr(fastfst::nNacCMzn, "name")
    descriptor = None
    for klass in fastfst::nNacCMzn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnaccmzn_has_value():
    assert hasattr(fastfst::nNacCMzn, "value")
    descriptor = None
    for klass in fastfst::nNacCMzn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnaccmyn_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacCMyn)


def test_fastfst::nnaccmyn_constructor_exists():
    assert callable(fastfst::nNacCMyn.__init__)


def test_fastfst::nnaccmyn_constructor_args():
    sig = inspect.signature(fastfst::nNacCMyn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nnaccmyn_has_value():
    assert hasattr(fastfst::nNacCMyn, "value")
    descriptor = None
    for klass in fastfst::nNacCMyn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnaccmyn_has_name():
    assert hasattr(fastfst::nNacCMyn, "name")
    descriptor = None
    for klass in fastfst::nNacCMyn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nttdspss_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTTDspSS)


def test_fastfst::nttdspss_constructor_exists():
    assert callable(fastfst::nTTDspSS.__init__)


def test_fastfst::nttdspss_constructor_args():
    sig = inspect.signature(fastfst::nTTDspSS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nttdspss_has_value():
    assert hasattr(fastfst::nTTDspSS, "value")
    descriptor = None
    for klass in fastfst::nTTDspSS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nttdspss_has_name():
    assert hasattr(fastfst::nTTDspSS, "name")
    descriptor = None
    for klass in fastfst::nTTDspSS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nttdspfa_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTTDspFA)


def test_fastfst::nttdspfa_constructor_exists():
    assert callable(fastfst::nTTDspFA.__init__)


def test_fastfst::nttdspfa_constructor_args():
    sig = inspect.signature(fastfst::nTTDspFA.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nttdspfa_has_value():
    assert hasattr(fastfst::nTTDspFA, "value")
    descriptor = None
    for klass in fastfst::nTTDspFA.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nttdspfa_has_name():
    assert hasattr(fastfst::nTTDspFA, "name")
    descriptor = None
    for klass in fastfst::nTTDspFA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnacyaw_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacYaw)


def test_fastfst::nnacyaw_constructor_exists():
    assert callable(fastfst::nNacYaw.__init__)


def test_fastfst::nnacyaw_constructor_args():
    sig = inspect.signature(fastfst::nNacYaw.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nnacyaw_has_value():
    assert hasattr(fastfst::nNacYaw, "value")
    descriptor = None
    for klass in fastfst::nNacYaw.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnacyaw_has_name():
    assert hasattr(fastfst::nNacYaw, "name")
    descriptor = None
    for klass in fastfst::nNacYaw.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nrotspeed_is_not_abstract():
    assert not inspect.isabstract(fastfst::nRotSpeed)


def test_fastfst::nrotspeed_constructor_exists():
    assert callable(fastfst::nRotSpeed.__init__)


def test_fastfst::nrotspeed_constructor_args():
    sig = inspect.signature(fastfst::nRotSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nrotspeed_has_value():
    assert hasattr(fastfst::nRotSpeed, "value")
    descriptor = None
    for klass in fastfst::nRotSpeed.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nrotspeed_has_name():
    assert hasattr(fastfst::nRotSpeed, "name")
    descriptor = None
    for klass in fastfst::nRotSpeed.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nundsling_is_not_abstract():
    assert not inspect.isabstract(fastfst::nUndSling)


def test_fastfst::nundsling_constructor_exists():
    assert callable(fastfst::nUndSling.__init__)


def test_fastfst::nundsling_constructor_args():
    sig = inspect.signature(fastfst::nUndSling.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nundsling_has_name():
    assert hasattr(fastfst::nUndSling, "name")
    descriptor = None
    for klass in fastfst::nUndSling.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nundsling_has_value():
    assert hasattr(fastfst::nUndSling, "value")
    descriptor = None
    for klass in fastfst::nUndSling.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::npspneln_is_not_abstract():
    assert not inspect.isabstract(fastfst::nPSpnElN)


def test_fastfst::npspneln_constructor_exists():
    assert callable(fastfst::nPSpnElN.__init__)


def test_fastfst::npspneln_constructor_args():
    sig = inspect.signature(fastfst::nPSpnElN.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::npspneln_has_value():
    assert hasattr(fastfst::nPSpnElN, "value")
    descriptor = None
    for klass in fastfst::nPSpnElN.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::npspneln_has_name():
    assert hasattr(fastfst::nPSpnElN, "name")
    descriptor = None
    for klass in fastfst::nPSpnElN.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nhubrad_is_not_abstract():
    assert not inspect.isabstract(fastfst::nHubRad)


def test_fastfst::nhubrad_constructor_exists():
    assert callable(fastfst::nHubRad.__init__)


def test_fastfst::nhubrad_constructor_args():
    sig = inspect.signature(fastfst::nHubRad.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nhubrad_has_name():
    assert hasattr(fastfst::nHubRad, "name")
    descriptor = None
    for klass in fastfst::nHubRad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nhubrad_has_value():
    assert hasattr(fastfst::nHubRad, "value")
    descriptor = None
    for klass in fastfst::nHubRad.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntiprad_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTipRad)


def test_fastfst::ntiprad_constructor_exists():
    assert callable(fastfst::nTipRad.__init__)


def test_fastfst::ntiprad_constructor_args():
    sig = inspect.signature(fastfst::nTipRad.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntiprad_has_name():
    assert hasattr(fastfst::nTipRad, "name")
    descriptor = None
    for klass in fastfst::nTipRad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntiprad_has_value():
    assert hasattr(fastfst::nTipRad, "value")
    descriptor = None
    for klass in fastfst::nTipRad.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::btwfadof1_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTwFADOF1)


def test_fastfst::btwfadof1_constructor_exists():
    assert callable(fastfst::bTwFADOF1.__init__)


def test_fastfst::btwfadof1_constructor_args():
    sig = inspect.signature(fastfst::bTwFADOF1.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::btwfadof1_has_value():
    assert hasattr(fastfst::bTwFADOF1, "value")
    descriptor = None
    for klass in fastfst::bTwFADOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::btwfadof1_has_name():
    assert hasattr(fastfst::bTwFADOF1, "name")
    descriptor = None
    for klass in fastfst::bTwFADOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::byawdof_is_not_abstract():
    assert not inspect.isabstract(fastfst::bYawDOF)


def test_fastfst::byawdof_constructor_exists():
    assert callable(fastfst::bYawDOF.__init__)


def test_fastfst::byawdof_constructor_args():
    sig = inspect.signature(fastfst::bYawDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::byawdof_has_value():
    assert hasattr(fastfst::bYawDOF, "value")
    descriptor = None
    for klass in fastfst::bYawDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::byawdof_has_name():
    assert hasattr(fastfst::bYawDOF, "name")
    descriptor = None
    for klass in fastfst::bYawDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bgendof_is_not_abstract():
    assert not inspect.isabstract(fastfst::bGenDOF)


def test_fastfst::bgendof_constructor_exists():
    assert callable(fastfst::bGenDOF.__init__)


def test_fastfst::bgendof_constructor_args():
    sig = inspect.signature(fastfst::bGenDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bgendof_has_name():
    assert hasattr(fastfst::bGenDOF, "name")
    descriptor = None
    for klass in fastfst::bGenDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bgendof_has_value():
    assert hasattr(fastfst::bGenDOF, "value")
    descriptor = None
    for klass in fastfst::bGenDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bdrtrdof_is_not_abstract():
    assert not inspect.isabstract(fastfst::bDrTrDOF)


def test_fastfst::bdrtrdof_constructor_exists():
    assert callable(fastfst::bDrTrDOF.__init__)


def test_fastfst::bdrtrdof_constructor_args():
    sig = inspect.signature(fastfst::bDrTrDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bdrtrdof_has_name():
    assert hasattr(fastfst::bDrTrDOF, "name")
    descriptor = None
    for klass in fastfst::bDrTrDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bdrtrdof_has_value():
    assert hasattr(fastfst::bDrTrDOF, "value")
    descriptor = None
    for klass in fastfst::bDrTrDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bteetdof_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTeetDOF)


def test_fastfst::bteetdof_constructor_exists():
    assert callable(fastfst::bTeetDOF.__init__)


def test_fastfst::bteetdof_constructor_args():
    sig = inspect.signature(fastfst::bTeetDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bteetdof_has_name():
    assert hasattr(fastfst::bTeetDOF, "name")
    descriptor = None
    for klass in fastfst::bTeetDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bteetdof_has_value():
    assert hasattr(fastfst::bTeetDOF, "value")
    descriptor = None
    for klass in fastfst::bTeetDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bedgedof_is_not_abstract():
    assert not inspect.isabstract(fastfst::bEdgeDOF)


def test_fastfst::bedgedof_constructor_exists():
    assert callable(fastfst::bEdgeDOF.__init__)


def test_fastfst::bedgedof_constructor_args():
    sig = inspect.signature(fastfst::bEdgeDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::bedgedof_has_value():
    assert hasattr(fastfst::bEdgeDOF, "value")
    descriptor = None
    for klass in fastfst::bEdgeDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bedgedof_has_name():
    assert hasattr(fastfst::bEdgeDOF, "name")
    descriptor = None
    for klass in fastfst::bEdgeDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nazimuth_is_not_abstract():
    assert not inspect.isabstract(fastfst::nAzimuth)


def test_fastfst::nazimuth_constructor_exists():
    assert callable(fastfst::nAzimuth.__init__)


def test_fastfst::nazimuth_constructor_args():
    sig = inspect.signature(fastfst::nAzimuth.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nazimuth_has_name():
    assert hasattr(fastfst::nAzimuth, "name")
    descriptor = None
    for klass in fastfst::nAzimuth.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nazimuth_has_value():
    assert hasattr(fastfst::nAzimuth, "value")
    descriptor = None
    for klass in fastfst::nAzimuth.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bflapdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst::bFlapDOF2)


def test_fastfst::bflapdof2_constructor_exists():
    assert callable(fastfst::bFlapDOF2.__init__)


def test_fastfst::bflapdof2_constructor_args():
    sig = inspect.signature(fastfst::bFlapDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bflapdof2_has_name():
    assert hasattr(fastfst::bFlapDOF2, "name")
    descriptor = None
    for klass in fastfst::bFlapDOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bflapdof2_has_value():
    assert hasattr(fastfst::bFlapDOF2, "value")
    descriptor = None
    for klass in fastfst::bFlapDOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nteetdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTeetDefl)


def test_fastfst::nteetdefl_constructor_exists():
    assert callable(fastfst::nTeetDefl.__init__)


def test_fastfst::nteetdefl_constructor_args():
    sig = inspect.signature(fastfst::nTeetDefl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nteetdefl_has_value():
    assert hasattr(fastfst::nTeetDefl, "value")
    descriptor = None
    for klass in fastfst::nTeetDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nteetdefl_has_name():
    assert hasattr(fastfst::nTeetDefl, "name")
    descriptor = None
    for klass in fastfst::nTeetDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bflapdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst::bFlapDOF1)


def test_fastfst::bflapdof1_constructor_exists():
    assert callable(fastfst::bFlapDOF1.__init__)


def test_fastfst::bflapdof1_constructor_args():
    sig = inspect.signature(fastfst::bFlapDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bflapdof1_has_name():
    assert hasattr(fastfst::bFlapDOF1, "name")
    descriptor = None
    for klass in fastfst::bFlapDOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bflapdof1_has_value():
    assert hasattr(fastfst::bFlapDOF1, "value")
    descriptor = None
    for klass in fastfst::bFlapDOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nipdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst::nIPDefl)


def test_fastfst::nipdefl_constructor_exists():
    assert callable(fastfst::nIPDefl.__init__)


def test_fastfst::nipdefl_constructor_args():
    sig = inspect.signature(fastfst::nIPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nipdefl_has_name():
    assert hasattr(fastfst::nIPDefl, "name")
    descriptor = None
    for klass in fastfst::nIPDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nipdefl_has_value():
    assert hasattr(fastfst::nIPDefl, "value")
    descriptor = None
    for klass in fastfst::nIPDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ngravity_is_not_abstract():
    assert not inspect.isabstract(fastfst::nGravity)


def test_fastfst::ngravity_constructor_exists():
    assert callable(fastfst::nGravity.__init__)


def test_fastfst::ngravity_constructor_args():
    sig = inspect.signature(fastfst::nGravity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ngravity_has_value():
    assert hasattr(fastfst::nGravity, "value")
    descriptor = None
    for klass in fastfst::nGravity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ngravity_has_name():
    assert hasattr(fastfst::nGravity, "name")
    descriptor = None
    for klass in fastfst::nGravity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::noopdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst::nOoPDefl)


def test_fastfst::noopdefl_constructor_exists():
    assert callable(fastfst::nOoPDefl.__init__)


def test_fastfst::noopdefl_constructor_args():
    sig = inspect.signature(fastfst::nOoPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::noopdefl_has_name():
    assert hasattr(fastfst::nOoPDefl, "name")
    descriptor = None
    for klass in fastfst::nOoPDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::noopdefl_has_value():
    assert hasattr(fastfst::nOoPDefl, "value")
    descriptor = None
    for klass in fastfst::nOoPDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitchf::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitchF::3::)


def test_fastfst::nblpitchf::3::_constructor_exists():
    assert callable(fastfst::nBlPitchF::3::.__init__)


def test_fastfst::nblpitchf::3::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitchF::3::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nblpitchf::3::_has_name():
    assert hasattr(fastfst::nBlPitchF::3::, "name")
    descriptor = None
    for klass in fastfst::nBlPitchF::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitchf::3::_has_value():
    assert hasattr(fastfst::nBlPitchF::3::, "value")
    descriptor = None
    for klass in fastfst::nBlPitchF::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitchf::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitchF::2::)


def test_fastfst::nblpitchf::2::_constructor_exists():
    assert callable(fastfst::nBlPitchF::2::.__init__)


def test_fastfst::nblpitchf::2::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitchF::2::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nblpitchf::2::_has_name():
    assert hasattr(fastfst::nBlPitchF::2::, "name")
    descriptor = None
    for klass in fastfst::nBlPitchF::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitchf::2::_has_value():
    assert hasattr(fastfst::nBlPitchF::2::, "value")
    descriptor = None
    for klass in fastfst::nBlPitchF::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bcompnoise_is_not_abstract():
    assert not inspect.isabstract(fastfst::bCompNoise)


def test_fastfst::bcompnoise_constructor_exists():
    assert callable(fastfst::bCompNoise.__init__)


def test_fastfst::bcompnoise_constructor_args():
    sig = inspect.signature(fastfst::bCompNoise.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bcompnoise_has_name():
    assert hasattr(fastfst::bCompNoise, "name")
    descriptor = None
    for klass in fastfst::bCompNoise.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bcompnoise_has_value():
    assert hasattr(fastfst::bCompNoise, "value")
    descriptor = None
    for klass in fastfst::bCompNoise.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitchf::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitchF::1::)


def test_fastfst::nblpitchf::1::_constructor_exists():
    assert callable(fastfst::nBlPitchF::1::.__init__)


def test_fastfst::nblpitchf::1::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitchF::1::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nblpitchf::1::_has_value():
    assert hasattr(fastfst::nBlPitchF::1::, "value")
    descriptor = None
    for klass in fastfst::nBlPitchF::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitchf::1::_has_name():
    assert hasattr(fastfst::nBlPitchF::1::, "name")
    descriptor = None
    for klass in fastfst::nBlPitchF::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bcompaero_is_not_abstract():
    assert not inspect.isabstract(fastfst::bCompAero)


def test_fastfst::bcompaero_constructor_exists():
    assert callable(fastfst::bCompAero.__init__)


def test_fastfst::bcompaero_constructor_args():
    sig = inspect.signature(fastfst::bCompAero.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bcompaero_has_name():
    assert hasattr(fastfst::bCompAero, "name")
    descriptor = None
    for klass in fastfst::bCompAero.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bcompaero_has_value():
    assert hasattr(fastfst::bCompAero, "value")
    descriptor = None
    for klass in fastfst::bCompAero.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitch::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitch::3::)


def test_fastfst::nblpitch::3::_constructor_exists():
    assert callable(fastfst::nBlPitch::3::.__init__)


def test_fastfst::nblpitch::3::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitch::3::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nblpitch::3::_has_value():
    assert hasattr(fastfst::nBlPitch::3::, "value")
    descriptor = None
    for klass in fastfst::nBlPitch::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitch::3::_has_name():
    assert hasattr(fastfst::nBlPitch::3::, "name")
    descriptor = None
    for klass in fastfst::nBlPitch::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::btwssdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTwSSDOF2)


def test_fastfst::btwssdof2_constructor_exists():
    assert callable(fastfst::bTwSSDOF2.__init__)


def test_fastfst::btwssdof2_constructor_args():
    sig = inspect.signature(fastfst::bTwSSDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::btwssdof2_has_value():
    assert hasattr(fastfst::bTwSSDOF2, "value")
    descriptor = None
    for klass in fastfst::bTwSSDOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::btwssdof2_has_name():
    assert hasattr(fastfst::bTwSSDOF2, "name")
    descriptor = None
    for klass in fastfst::bTwSSDOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitch::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitch::2::)


def test_fastfst::nblpitch::2::_constructor_exists():
    assert callable(fastfst::nBlPitch::2::.__init__)


def test_fastfst::nblpitch::2::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitch::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nblpitch::2::_has_value():
    assert hasattr(fastfst::nBlPitch::2::, "value")
    descriptor = None
    for klass in fastfst::nBlPitch::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitch::2::_has_name():
    assert hasattr(fastfst::nBlPitch::2::, "name")
    descriptor = None
    for klass in fastfst::nBlPitch::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::btwssdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTwSSDOF1)


def test_fastfst::btwssdof1_constructor_exists():
    assert callable(fastfst::bTwSSDOF1.__init__)


def test_fastfst::btwssdof1_constructor_args():
    sig = inspect.signature(fastfst::bTwSSDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::btwssdof1_has_name():
    assert hasattr(fastfst::bTwSSDOF1, "name")
    descriptor = None
    for klass in fastfst::bTwSSDOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::btwssdof1_has_value():
    assert hasattr(fastfst::bTwSSDOF1, "value")
    descriptor = None
    for klass in fastfst::bTwSSDOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::btwfadof2_is_not_abstract():
    assert not inspect.isabstract(fastfst::bTwFADOF2)


def test_fastfst::btwfadof2_constructor_exists():
    assert callable(fastfst::bTwFADOF2.__init__)


def test_fastfst::btwfadof2_constructor_args():
    sig = inspect.signature(fastfst::bTwFADOF2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::btwfadof2_has_name():
    assert hasattr(fastfst::bTwFADOF2, "name")
    descriptor = None
    for klass in fastfst::bTwFADOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::btwfadof2_has_value():
    assert hasattr(fastfst::bTwFADOF2, "value")
    descriptor = None
    for klass in fastfst::bTwFADOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmane::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManE::2::)


def test_fastfst::ntpitmane::2::_constructor_exists():
    assert callable(fastfst::nTPitManE::2::.__init__)


def test_fastfst::ntpitmane::2::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManE::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntpitmane::2::_has_value():
    assert hasattr(fastfst::nTPitManE::2::, "value")
    descriptor = None
    for klass in fastfst::nTPitManE::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmane::2::_has_name():
    assert hasattr(fastfst::nTPitManE::2::, "name")
    descriptor = None
    for klass in fastfst::nTPitManE::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmane::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManE::1::)


def test_fastfst::ntpitmane::1::_constructor_exists():
    assert callable(fastfst::nTPitManE::1::.__init__)


def test_fastfst::ntpitmane::1::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManE::1::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntpitmane::1::_has_value():
    assert hasattr(fastfst::nTPitManE::1::, "value")
    descriptor = None
    for klass in fastfst::nTPitManE::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmane::1::_has_name():
    assert hasattr(fastfst::nTPitManE::1::, "name")
    descriptor = None
    for klass in fastfst::nTPitManE::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmans::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManS::3::)


def test_fastfst::ntpitmans::3::_constructor_exists():
    assert callable(fastfst::nTPitManS::3::.__init__)


def test_fastfst::ntpitmans::3::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManS::3::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntpitmans::3::_has_value():
    assert hasattr(fastfst::nTPitManS::3::, "value")
    descriptor = None
    for klass in fastfst::nTPitManS::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmans::3::_has_name():
    assert hasattr(fastfst::nTPitManS::3::, "name")
    descriptor = None
    for klass in fastfst::nTPitManS::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmans::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManS::2::)


def test_fastfst::ntpitmans::2::_constructor_exists():
    assert callable(fastfst::nTPitManS::2::.__init__)


def test_fastfst::ntpitmans::2::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManS::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntpitmans::2::_has_value():
    assert hasattr(fastfst::nTPitManS::2::, "value")
    descriptor = None
    for klass in fastfst::nTPitManS::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmans::2::_has_name():
    assert hasattr(fastfst::nTPitManS::2::, "name")
    descriptor = None
    for klass in fastfst::nTPitManS::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmans::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManS::1::)


def test_fastfst::ntpitmans::1::_constructor_exists():
    assert callable(fastfst::nTPitManS::1::.__init__)


def test_fastfst::ntpitmans::1::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManS::1::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntpitmans::1::_has_name():
    assert hasattr(fastfst::nTPitManS::1::, "name")
    descriptor = None
    for klass in fastfst::nTPitManS::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmans::1::_has_value():
    assert hasattr(fastfst::nTPitManS::1::, "value")
    descriptor = None
    for klass in fastfst::nTPitManS::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nnacyawf_is_not_abstract():
    assert not inspect.isabstract(fastfst::nNacYawF)


def test_fastfst::nnacyawf_constructor_exists():
    assert callable(fastfst::nNacYawF.__init__)


def test_fastfst::nnacyawf_constructor_args():
    sig = inspect.signature(fastfst::nNacYawF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nnacyawf_has_value():
    assert hasattr(fastfst::nNacYawF, "value")
    descriptor = None
    for klass in fastfst::nNacYawF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nnacyawf_has_name():
    assert hasattr(fastfst::nNacYawF, "name")
    descriptor = None
    for klass in fastfst::nNacYawF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntyawmane_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTYawManE)


def test_fastfst::ntyawmane_constructor_exists():
    assert callable(fastfst::nTYawManE.__init__)


def test_fastfst::ntyawmane_constructor_args():
    sig = inspect.signature(fastfst::nTYawManE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntyawmane_has_name():
    assert hasattr(fastfst::nTYawManE, "name")
    descriptor = None
    for klass in fastfst::nTYawManE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntyawmane_has_value():
    assert hasattr(fastfst::nTYawManE, "value")
    descriptor = None
    for klass in fastfst::nTYawManE.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntyawmans_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTYawManS)


def test_fastfst::ntyawmans_constructor_exists():
    assert callable(fastfst::nTYawManS.__init__)


def test_fastfst::ntyawmans_constructor_args():
    sig = inspect.signature(fastfst::nTYawManS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntyawmans_has_value():
    assert hasattr(fastfst::nTYawManS, "value")
    descriptor = None
    for klass in fastfst::nTYawManS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntyawmans_has_name():
    assert hasattr(fastfst::nTYawManS, "name")
    descriptor = None
    for klass in fastfst::nTYawManS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntbdepisp::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTBDepISp::3::)


def test_fastfst::ntbdepisp::3::_constructor_exists():
    assert callable(fastfst::nTBDepISp::3::.__init__)


def test_fastfst::ntbdepisp::3::_constructor_args():
    sig = inspect.signature(fastfst::nTBDepISp::3::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntbdepisp::3::_has_name():
    assert hasattr(fastfst::nTBDepISp::3::, "name")
    descriptor = None
    for klass in fastfst::nTBDepISp::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntbdepisp::3::_has_value():
    assert hasattr(fastfst::nTBDepISp::3::, "value")
    descriptor = None
    for klass in fastfst::nTBDepISp::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntbdepisp::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTBDepISp::2::)


def test_fastfst::ntbdepisp::2::_constructor_exists():
    assert callable(fastfst::nTBDepISp::2::.__init__)


def test_fastfst::ntbdepisp::2::_constructor_args():
    sig = inspect.signature(fastfst::nTBDepISp::2::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntbdepisp::2::_has_name():
    assert hasattr(fastfst::nTBDepISp::2::, "name")
    descriptor = None
    for klass in fastfst::nTBDepISp::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntbdepisp::2::_has_value():
    assert hasattr(fastfst::nTBDepISp::2::, "value")
    descriptor = None
    for klass in fastfst::nTBDepISp::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntbdepisp::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTBDepISp::1::)


def test_fastfst::ntbdepisp::1::_constructor_exists():
    assert callable(fastfst::nTBDepISp::1::.__init__)


def test_fastfst::ntbdepisp::1::_constructor_args():
    sig = inspect.signature(fastfst::nTBDepISp::1::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntbdepisp::1::_has_name():
    assert hasattr(fastfst::nTBDepISp::1::, "name")
    descriptor = None
    for klass in fastfst::nTBDepISp::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntbdepisp::1::_has_value():
    assert hasattr(fastfst::nTBDepISp::1::, "value")
    descriptor = None
    for klass in fastfst::nTBDepISp::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nttpbrdp::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTTpBrDp::3::)


def test_fastfst::nttpbrdp::3::_constructor_exists():
    assert callable(fastfst::nTTpBrDp::3::.__init__)


def test_fastfst::nttpbrdp::3::_constructor_args():
    sig = inspect.signature(fastfst::nTTpBrDp::3::.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nttpbrdp::3::_has_name():
    assert hasattr(fastfst::nTTpBrDp::3::, "name")
    descriptor = None
    for klass in fastfst::nTTpBrDp::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nttpbrdp::3::_has_value():
    assert hasattr(fastfst::nTTpBrDp::3::, "value")
    descriptor = None
    for klass in fastfst::nTTpBrDp::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nttpbrdp::2::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTTpBrDp::2::)


def test_fastfst::nttpbrdp::2::_constructor_exists():
    assert callable(fastfst::nTTpBrDp::2::.__init__)


def test_fastfst::nttpbrdp::2::_constructor_args():
    sig = inspect.signature(fastfst::nTTpBrDp::2::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nttpbrdp::2::_has_value():
    assert hasattr(fastfst::nTTpBrDp::2::, "value")
    descriptor = None
    for klass in fastfst::nTTpBrDp::2::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nttpbrdp::2::_has_name():
    assert hasattr(fastfst::nTTpBrDp::2::, "name")
    descriptor = None
    for klass in fastfst::nTTpBrDp::2::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nttpbrdp::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTTpBrDp::1::)


def test_fastfst::nttpbrdp::1::_constructor_exists():
    assert callable(fastfst::nTTpBrDp::1::.__init__)


def test_fastfst::nttpbrdp::1::_constructor_args():
    sig = inspect.signature(fastfst::nTTpBrDp::1::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nttpbrdp::1::_has_value():
    assert hasattr(fastfst::nTTpBrDp::1::, "value")
    descriptor = None
    for klass in fastfst::nTTpBrDp::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nttpbrdp::1::_has_name():
    assert hasattr(fastfst::nTTpBrDp::1::, "name")
    descriptor = None
    for klass in fastfst::nTTpBrDp::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nblpitch::1::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nBlPitch::1::)


def test_fastfst::nblpitch::1::_constructor_exists():
    assert callable(fastfst::nBlPitch::1::.__init__)


def test_fastfst::nblpitch::1::_constructor_args():
    sig = inspect.signature(fastfst::nBlPitch::1::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nblpitch::1::_has_value():
    assert hasattr(fastfst::nBlPitch::1::, "value")
    descriptor = None
    for klass in fastfst::nBlPitch::1::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nblpitch::1::_has_name():
    assert hasattr(fastfst::nBlPitch::1::, "name")
    descriptor = None
    for klass in fastfst::nBlPitch::1::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpitmane::3::_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPitManE::3::)


def test_fastfst::ntpitmane::3::_constructor_exists():
    assert callable(fastfst::nTPitManE::3::.__init__)


def test_fastfst::ntpitmane::3::_constructor_args():
    sig = inspect.signature(fastfst::nTPitManE::3::.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntpitmane::3::_has_value():
    assert hasattr(fastfst::nTPitManE::3::, "value")
    descriptor = None
    for klass in fastfst::nTPitManE::3::.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpitmane::3::_has_name():
    assert hasattr(fastfst::nTPitManE::3::, "name")
    descriptor = None
    for klass in fastfst::nTPitManE::3::.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ihssbrmode_is_not_abstract():
    assert not inspect.isabstract(fastfst::iHSSBrMode)


def test_fastfst::ihssbrmode_constructor_exists():
    assert callable(fastfst::iHSSBrMode.__init__)


def test_fastfst::ihssbrmode_constructor_args():
    sig = inspect.signature(fastfst::iHSSBrMode.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ihssbrmode_has_value():
    assert hasattr(fastfst::iHSSBrMode, "value")
    descriptor = None
    for klass in fastfst::iHSSBrMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ihssbrmode_has_name():
    assert hasattr(fastfst::iHSSBrMode, "name")
    descriptor = None
    for klass in fastfst::iHSSBrMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntimgenof_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTimGenOf)


def test_fastfst::ntimgenof_constructor_exists():
    assert callable(fastfst::nTimGenOf.__init__)


def test_fastfst::ntimgenof_constructor_args():
    sig = inspect.signature(fastfst::nTimGenOf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntimgenof_has_name():
    assert hasattr(fastfst::nTimGenOf, "name")
    descriptor = None
    for klass in fastfst::nTimGenOf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntimgenof_has_value():
    assert hasattr(fastfst::nTimGenOf, "value")
    descriptor = None
    for klass in fastfst::nTimGenOf.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntimgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTimGenOn)


def test_fastfst::ntimgenon_constructor_exists():
    assert callable(fastfst::nTimGenOn.__init__)


def test_fastfst::ntimgenon_constructor_args():
    sig = inspect.signature(fastfst::nTimGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntimgenon_has_name():
    assert hasattr(fastfst::nTimGenOn, "name")
    descriptor = None
    for klass in fastfst::nTimGenOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntimgenon_has_value():
    assert hasattr(fastfst::nTimGenOn, "value")
    descriptor = None
    for klass in fastfst::nTimGenOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nspdgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst::nSpdGenOn)


def test_fastfst::nspdgenon_constructor_exists():
    assert callable(fastfst::nSpdGenOn.__init__)


def test_fastfst::nspdgenon_constructor_args():
    sig = inspect.signature(fastfst::nSpdGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nspdgenon_has_value():
    assert hasattr(fastfst::nSpdGenOn, "value")
    descriptor = None
    for klass in fastfst::nSpdGenOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nspdgenon_has_name():
    assert hasattr(fastfst::nSpdGenOn, "name")
    descriptor = None
    for klass in fastfst::nSpdGenOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bgentistp_is_not_abstract():
    assert not inspect.isabstract(fastfst::bGenTiStp)


def test_fastfst::bgentistp_constructor_exists():
    assert callable(fastfst::bGenTiStp.__init__)


def test_fastfst::bgentistp_constructor_args():
    sig = inspect.signature(fastfst::bGenTiStp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::bgentistp_has_name():
    assert hasattr(fastfst::bGenTiStp, "name")
    descriptor = None
    for klass in fastfst::bGenTiStp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bgentistp_has_value():
    assert hasattr(fastfst::bGenTiStp, "value")
    descriptor = None
    for klass in fastfst::bGenTiStp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::bgentistr_is_not_abstract():
    assert not inspect.isabstract(fastfst::bGenTiStr)


def test_fastfst::bgentistr_constructor_exists():
    assert callable(fastfst::bGenTiStr.__init__)


def test_fastfst::bgentistr_constructor_args():
    sig = inspect.signature(fastfst::bGenTiStr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::bgentistr_has_value():
    assert hasattr(fastfst::bGenTiStr, "value")
    descriptor = None
    for klass in fastfst::bGenTiStr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::bgentistr_has_name():
    assert hasattr(fastfst::bGenTiStr, "name")
    descriptor = None
    for klass in fastfst::bGenTiStr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::igenmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst::iGenModel)


def test_fastfst::igenmodel_constructor_exists():
    assert callable(fastfst::iGenModel.__init__)


def test_fastfst::igenmodel_constructor_args():
    sig = inspect.signature(fastfst::iGenModel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::igenmodel_has_value():
    assert hasattr(fastfst::iGenModel, "value")
    descriptor = None
    for klass in fastfst::iGenModel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::igenmodel_has_name():
    assert hasattr(fastfst::iGenModel, "name")
    descriptor = None
    for klass in fastfst::iGenModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nvs::slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst::nVS::SlPc)


def test_fastfst::nvs::slpc_constructor_exists():
    assert callable(fastfst::nVS::SlPc.__init__)


def test_fastfst::nvs::slpc_constructor_args():
    sig = inspect.signature(fastfst::nVS::SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::nvs::slpc_has_value():
    assert hasattr(fastfst::nVS::SlPc, "value")
    descriptor = None
    for klass in fastfst::nVS::SlPc.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nvs::slpc_has_name():
    assert hasattr(fastfst::nVS::SlPc, "name")
    descriptor = None
    for klass in fastfst::nVS::SlPc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nvs::rgn2k_is_not_abstract():
    assert not inspect.isabstract(fastfst::nVS::Rgn2K)


def test_fastfst::nvs::rgn2k_constructor_exists():
    assert callable(fastfst::nVS::Rgn2K.__init__)


def test_fastfst::nvs::rgn2k_constructor_args():
    sig = inspect.signature(fastfst::nVS::Rgn2K.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nvs::rgn2k_has_name():
    assert hasattr(fastfst::nVS::Rgn2K, "name")
    descriptor = None
    for klass in fastfst::nVS::Rgn2K.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nvs::rgn2k_has_value():
    assert hasattr(fastfst::nVS::Rgn2K, "value")
    descriptor = None
    for klass in fastfst::nVS::Rgn2K.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nvs::rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst::nVS::RtTq)


def test_fastfst::nvs::rttq_constructor_exists():
    assert callable(fastfst::nVS::RtTq.__init__)


def test_fastfst::nvs::rttq_constructor_args():
    sig = inspect.signature(fastfst::nVS::RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nvs::rttq_has_name():
    assert hasattr(fastfst::nVS::RtTq, "name")
    descriptor = None
    for klass in fastfst::nVS::RtTq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nvs::rttq_has_value():
    assert hasattr(fastfst::nVS::RtTq, "value")
    descriptor = None
    for klass in fastfst::nVS::RtTq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nvs::rtgnsp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nVS::RtGnSp)


def test_fastfst::nvs::rtgnsp_constructor_exists():
    assert callable(fastfst::nVS::RtGnSp.__init__)


def test_fastfst::nvs::rtgnsp_constructor_args():
    sig = inspect.signature(fastfst::nVS::RtGnSp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nvs::rtgnsp_has_name():
    assert hasattr(fastfst::nVS::RtGnSp, "name")
    descriptor = None
    for klass in fastfst::nVS::RtGnSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nvs::rtgnsp_has_value():
    assert hasattr(fastfst::nVS::RtGnSp, "value")
    descriptor = None
    for klass in fastfst::nVS::RtGnSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ivscontrl_is_not_abstract():
    assert not inspect.isabstract(fastfst::iVSContrl)


def test_fastfst::ivscontrl_constructor_exists():
    assert callable(fastfst::iVSContrl.__init__)


def test_fastfst::ivscontrl_constructor_args():
    sig = inspect.signature(fastfst::iVSContrl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ivscontrl_has_name():
    assert hasattr(fastfst::iVSContrl, "name")
    descriptor = None
    for klass in fastfst::iVSContrl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ivscontrl_has_value():
    assert hasattr(fastfst::iVSContrl, "value")
    descriptor = None
    for klass in fastfst::iVSContrl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntpcon_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTPCOn)


def test_fastfst::ntpcon_constructor_exists():
    assert callable(fastfst::nTPCOn.__init__)


def test_fastfst::ntpcon_constructor_args():
    sig = inspect.signature(fastfst::nTPCOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntpcon_has_name():
    assert hasattr(fastfst::nTPCOn, "name")
    descriptor = None
    for klass in fastfst::nTPCOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntpcon_has_value():
    assert hasattr(fastfst::nTPCOn, "value")
    descriptor = None
    for klass in fastfst::nTPCOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ipcmode_is_not_abstract():
    assert not inspect.isabstract(fastfst::iPCMode)


def test_fastfst::ipcmode_constructor_exists():
    assert callable(fastfst::iPCMode.__init__)


def test_fastfst::ipcmode_constructor_args():
    sig = inspect.signature(fastfst::iPCMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ipcmode_has_name():
    assert hasattr(fastfst::iPCMode, "name")
    descriptor = None
    for klass in fastfst::iPCMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ipcmode_has_value():
    assert hasattr(fastfst::iPCMode, "value")
    descriptor = None
    for klass in fastfst::iPCMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntycon_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTYCOn)


def test_fastfst::ntycon_constructor_exists():
    assert callable(fastfst::nTYCOn.__init__)


def test_fastfst::ntycon_constructor_args():
    sig = inspect.signature(fastfst::nTYCOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntycon_has_value():
    assert hasattr(fastfst::nTYCOn, "value")
    descriptor = None
    for klass in fastfst::nTYCOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntycon_has_name():
    assert hasattr(fastfst::nTYCOn, "name")
    descriptor = None
    for klass in fastfst::nTYCOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::iycmode_is_not_abstract():
    assert not inspect.isabstract(fastfst::iYCMode)


def test_fastfst::iycmode_constructor_exists():
    assert callable(fastfst::iYCMode.__init__)


def test_fastfst::iycmode_constructor_args():
    sig = inspect.signature(fastfst::iYCMode.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::iycmode_has_value():
    assert hasattr(fastfst::iYCMode, "value")
    descriptor = None
    for klass in fastfst::iYCMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::iycmode_has_name():
    assert hasattr(fastfst::iYCMode, "name")
    descriptor = None
    for klass in fastfst::iYCMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ndt_is_not_abstract():
    assert not inspect.isabstract(fastfst::nDT)


def test_fastfst::ndt_constructor_exists():
    assert callable(fastfst::nDT.__init__)


def test_fastfst::ndt_constructor_args():
    sig = inspect.signature(fastfst::nDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ndt_has_value():
    assert hasattr(fastfst::nDT, "value")
    descriptor = None
    for klass in fastfst::nDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ndt_has_name():
    assert hasattr(fastfst::nDT, "name")
    descriptor = None
    for klass in fastfst::nDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntmax_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTMax)


def test_fastfst::ntmax_constructor_exists():
    assert callable(fastfst::nTMax.__init__)


def test_fastfst::ntmax_constructor_args():
    sig = inspect.signature(fastfst::nTMax.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::ntmax_has_value():
    assert hasattr(fastfst::nTMax, "value")
    descriptor = None
    for klass in fastfst::nTMax.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntmax_has_name():
    assert hasattr(fastfst::nTMax, "name")
    descriptor = None
    for klass in fastfst::nTMax.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ntidynbrk_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTiDynBrk)


def test_fastfst::ntidynbrk_constructor_exists():
    assert callable(fastfst::nTiDynBrk.__init__)


def test_fastfst::ntidynbrk_constructor_args():
    sig = inspect.signature(fastfst::nTiDynBrk.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ntidynbrk_has_name():
    assert hasattr(fastfst::nTiDynBrk, "name")
    descriptor = None
    for klass in fastfst::nTiDynBrk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ntidynbrk_has_value():
    assert hasattr(fastfst::nTiDynBrk, "value")
    descriptor = None
    for klass in fastfst::nTiDynBrk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::nthssbrdp_is_not_abstract():
    assert not inspect.isabstract(fastfst::nTHSSBrDp)


def test_fastfst::nthssbrdp_constructor_exists():
    assert callable(fastfst::nTHSSBrDp.__init__)


def test_fastfst::nthssbrdp_constructor_args():
    sig = inspect.signature(fastfst::nTHSSBrDp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::nthssbrdp_has_name():
    assert hasattr(fastfst::nTHSSBrDp, "name")
    descriptor = None
    for klass in fastfst::nTHSSBrDp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::nthssbrdp_has_value():
    assert hasattr(fastfst::nTHSSBrDp, "value")
    descriptor = None
    for klass in fastfst::nTHSSBrDp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::iadamsprep_is_not_abstract():
    assert not inspect.isabstract(fastfst::iADAMSPrep)


def test_fastfst::iadamsprep_constructor_exists():
    assert callable(fastfst::iADAMSPrep.__init__)


def test_fastfst::iadamsprep_constructor_args():
    sig = inspect.signature(fastfst::iADAMSPrep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::iadamsprep_has_name():
    assert hasattr(fastfst::iADAMSPrep, "name")
    descriptor = None
    for klass in fastfst::iADAMSPrep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::iadamsprep_has_value():
    assert hasattr(fastfst::iADAMSPrep, "value")
    descriptor = None
    for klass in fastfst::iADAMSPrep.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::becho_is_not_abstract():
    assert not inspect.isabstract(fastfst::bEcho)


def test_fastfst::becho_constructor_exists():
    assert callable(fastfst::bEcho.__init__)


def test_fastfst::becho_constructor_args():
    sig = inspect.signature(fastfst::bEcho.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::becho_has_name():
    assert hasattr(fastfst::bEcho, "name")
    descriptor = None
    for klass in fastfst::bEcho.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::becho_has_value():
    assert hasattr(fastfst::bEcho, "value")
    descriptor = None
    for klass in fastfst::bEcho.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::section_is_not_abstract():
    assert not inspect.isabstract(fastfst::Section)


def test_fastfst::section_constructor_exists():
    assert callable(fastfst::Section.__init__)


def test_fastfst::section_constructor_args():
    sig = inspect.signature(fastfst::Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::section_has_name():
    assert hasattr(fastfst::Section, "name")
    descriptor = None
    for klass in fastfst::Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::header_is_not_abstract():
    assert not inspect.isabstract(fastfst::Header)


def test_fastfst::header_constructor_exists():
    assert callable(fastfst::Header.__init__)


def test_fastfst::header_constructor_args():
    sig = inspect.signature(fastfst::Header.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"

def test_fastfst::header_has_rows():
    assert hasattr(fastfst::Header, "rows")
    descriptor = None
    for klass in fastfst::Header.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::modelfastfst_is_not_abstract():
    assert not inspect.isabstract(fastfst::ModelFastfst)


def test_fastfst::modelfastfst_constructor_exists():
    assert callable(fastfst::ModelFastfst.__init__)


def test_fastfst::modelfastfst_constructor_args():
    sig = inspect.signature(fastfst::ModelFastfst.__init__)
    params = list(sig.parameters.keys())



def test_fastfst::inumbl_is_not_abstract():
    assert not inspect.isabstract(fastfst::iNumBl)


def test_fastfst::inumbl_constructor_exists():
    assert callable(fastfst::iNumBl.__init__)


def test_fastfst::inumbl_constructor_args():
    sig = inspect.signature(fastfst::iNumBl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst::inumbl_has_value():
    assert hasattr(fastfst::iNumBl, "value")
    descriptor = None
    for klass in fastfst::iNumBl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::inumbl_has_name():
    assert hasattr(fastfst::iNumBl, "name")
    descriptor = None
    for klass in fastfst::iNumBl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst::ianalmode_is_not_abstract():
    assert not inspect.isabstract(fastfst::iAnalMode)


def test_fastfst::ianalmode_constructor_exists():
    assert callable(fastfst::iAnalMode.__init__)


def test_fastfst::ianalmode_constructor_args():
    sig = inspect.signature(fastfst::iAnalMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst::ianalmode_has_name():
    assert hasattr(fastfst::iAnalMode, "name")
    descriptor = None
    for klass in fastfst::iAnalMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst::ianalmode_has_value():
    assert hasattr(fastfst::iAnalMode, "value")
    descriptor = None
    for klass in fastfst::iAnalMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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
fastfst::nShftGagL_strategy = st.builds(
    fastfst::nShftGagL,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nNcIMUzn_strategy = st.builds(
    fastfst::nNcIMUzn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::vOutList_strategy = st.builds(
    fastfst::vOutList,
    value=
        safe_text,
    name=
        safe_text
)
fastfst::aBldGagNd_strategy = st.builds(
    fastfst::aBldGagNd,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::iNBlGages_strategy = st.builds(
    fastfst::iNBlGages,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::aTwrGagNd_strategy = st.builds(
    fastfst::aTwrGagNd,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::iNTwGages_strategy = st.builds(
    fastfst::iNTwGages,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::sOutFmt_strategy = st.builds(
    fastfst::sOutFmt,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::bTabDelim_strategy = st.builds(
    fastfst::bTabDelim,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nNcIMUyn_strategy = st.builds(
    fastfst::nNcIMUyn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nNcIMUxn_strategy = st.builds(
    fastfst::nNcIMUxn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nSttsTime_strategy = st.builds(
    fastfst::nSttsTime,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::iDecFact_strategy = st.builds(
    fastfst::iDecFact,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::nTStart_strategy = st.builds(
    fastfst::nTStart,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::fBldFile::3::_strategy = st.builds(
    fastfst::fBldFile::3::,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::fBldFile::2::_strategy = st.builds(
    fastfst::fBldFile::2::,
    value=
        safe_text,
    name=
        safe_text
)
fastfst::bOutFileFmt_strategy = st.builds(
    fastfst::bOutFileFmt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bSumPrint_strategy = st.builds(
    fastfst::bSumPrint,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::fLinFile_strategy = st.builds(
    fastfst::fLinFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst::fADAMSFile_strategy = st.builds(
    fastfst::fADAMSFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::fNoiseFile_strategy = st.builds(
    fastfst::fNoiseFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::fADFile_strategy = st.builds(
    fastfst::fADFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst::nTeetHStP_strategy = st.builds(
    fastfst::nTeetHStP,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTeetSStP_strategy = st.builds(
    fastfst::nTeetSStP,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::fBldFile::1::_strategy = st.builds(
    fastfst::fBldFile::1::,
    value=
        safe_text,
    name=
        safe_text
)
fastfst::nTpBrDT_strategy = st.builds(
    fastfst::nTpBrDT,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTBDrConD_strategy = st.builds(
    fastfst::nTBDrConD,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTBDrConN_strategy = st.builds(
    fastfst::nTBDrConN,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTeetHSSp_strategy = st.builds(
    fastfst::nTeetHSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTeetSSSp_strategy = st.builds(
    fastfst::nTeetSSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nYawNeut_strategy = st.builds(
    fastfst::nYawNeut,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nYawDamp_strategy = st.builds(
    fastfst::nYawDamp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTeetCDmp_strategy = st.builds(
    fastfst::nTeetCDmp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTeetDmp_strategy = st.builds(
    fastfst::nTeetDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTeetDmpP_strategy = st.builds(
    fastfst::nTeetDmpP,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::iTeetMod_strategy = st.builds(
    fastfst::iTeetMod,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::fFurlFile_strategy = st.builds(
    fastfst::fFurlFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::nTEC::RLR_strategy = st.builds(
    fastfst::nTEC::RLR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bFurling_strategy = st.builds(
    fastfst::bFurling,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nTEC::SLR_strategy = st.builds(
    fastfst::nTEC::SLR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nYawSpr_strategy = st.builds(
    fastfst::nYawSpr,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::fTwrFile_strategy = st.builds(
    fastfst::fTwrFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::iTwrNodes_strategy = st.builds(
    fastfst::iTwrNodes,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::fPtfmFile_strategy = st.builds(
    fastfst::fPtfmFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::iPtfmModel_strategy = st.builds(
    fastfst::iPtfmModel,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::nTEC::MR_strategy = st.builds(
    fastfst::nTEC::MR,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nSIG::SlPc_strategy = st.builds(
    fastfst::nSIG::SlPc,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nDTTorDmp_strategy = st.builds(
    fastfst::nDTTorDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTEC::VLL_strategy = st.builds(
    fastfst::nTEC::VLL,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTEC::Rres_strategy = st.builds(
    fastfst::nTEC::Rres,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTEC::Sres_strategy = st.builds(
    fastfst::nTEC::Sres,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTEC::Npol_strategy = st.builds(
    fastfst::nTEC::Npol,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTEC::Freq_strategy = st.builds(
    fastfst::nTEC::Freq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nSIG::PORt_strategy = st.builds(
    fastfst::nSIG::PORt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nSIG::RtTq_strategy = st.builds(
    fastfst::nSIG::RtTq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nSIG::SySp_strategy = st.builds(
    fastfst::nSIG::SySp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nGenIner_strategy = st.builds(
    fastfst::nGenIner,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nDTTorSpr_strategy = st.builds(
    fastfst::nDTTorSpr,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::fDynBrkFi_strategy = st.builds(
    fastfst::fDynBrkFi,
    name=
        safe_text,
    value=
        safe_text
)
fastfst::nHSSBrDT_strategy = st.builds(
    fastfst::nHSSBrDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nHSSBrTqF_strategy = st.builds(
    fastfst::nHSSBrTqF,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::bGBRevers_strategy = st.builds(
    fastfst::bGBRevers,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::nGBRatio_strategy = st.builds(
    fastfst::nGBRatio,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nGenEff_strategy = st.builds(
    fastfst::nGenEff,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nGBoxEff_strategy = st.builds(
    fastfst::nGBoxEff,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nHubIner_strategy = st.builds(
    fastfst::nHubIner,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nPreCone::2::_strategy = st.builds(
    fastfst::nPreCone::2::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nNacYIner_strategy = st.builds(
    fastfst::nNacYIner,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTipMass::3::_strategy = st.builds(
    fastfst::nTipMass::3::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTipMass::2::_strategy = st.builds(
    fastfst::nTipMass::2::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTipMass::1::_strategy = st.builds(
    fastfst::nTipMass::1::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nHubMass_strategy = st.builds(
    fastfst::nHubMass,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nNacMass_strategy = st.builds(
    fastfst::nNacMass,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nYawBrMass_strategy = st.builds(
    fastfst::nYawBrMass,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nAzimB1Up_strategy = st.builds(
    fastfst::nAzimB1Up,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nPreCone::3::_strategy = st.builds(
    fastfst::nPreCone::3::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nNacCMxn_strategy = st.builds(
    fastfst::nNacCMxn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nOverHang_strategy = st.builds(
    fastfst::nOverHang,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nHubCM_strategy = st.builds(
    fastfst::nHubCM,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nPreCone::1::_strategy = st.builds(
    fastfst::nPreCone::1::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nDelta3_strategy = st.builds(
    fastfst::nDelta3,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nShftTilt_strategy = st.builds(
    fastfst::nShftTilt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTwrRBHt_strategy = st.builds(
    fastfst::nTwrRBHt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTwr2Shft_strategy = st.builds(
    fastfst::nTwr2Shft,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTowerHt_strategy = st.builds(
    fastfst::nTowerHt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nNacCMzn_strategy = st.builds(
    fastfst::nNacCMzn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nNacCMyn_strategy = st.builds(
    fastfst::nNacCMyn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTTDspSS_strategy = st.builds(
    fastfst::nTTDspSS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTTDspFA_strategy = st.builds(
    fastfst::nTTDspFA,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nNacYaw_strategy = st.builds(
    fastfst::nNacYaw,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nRotSpeed_strategy = st.builds(
    fastfst::nRotSpeed,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nUndSling_strategy = st.builds(
    fastfst::nUndSling,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nPSpnElN_strategy = st.builds(
    fastfst::nPSpnElN,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::nHubRad_strategy = st.builds(
    fastfst::nHubRad,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTipRad_strategy = st.builds(
    fastfst::nTipRad,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::bTwFADOF1_strategy = st.builds(
    fastfst::bTwFADOF1,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::bYawDOF_strategy = st.builds(
    fastfst::bYawDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::bGenDOF_strategy = st.builds(
    fastfst::bGenDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::bDrTrDOF_strategy = st.builds(
    fastfst::bDrTrDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::bTeetDOF_strategy = st.builds(
    fastfst::bTeetDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::bEdgeDOF_strategy = st.builds(
    fastfst::bEdgeDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::nAzimuth_strategy = st.builds(
    fastfst::nAzimuth,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::bFlapDOF2_strategy = st.builds(
    fastfst::bFlapDOF2,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nTeetDefl_strategy = st.builds(
    fastfst::nTeetDefl,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bFlapDOF1_strategy = st.builds(
    fastfst::bFlapDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nIPDefl_strategy = st.builds(
    fastfst::nIPDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nGravity_strategy = st.builds(
    fastfst::nGravity,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nOoPDefl_strategy = st.builds(
    fastfst::nOoPDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nBlPitchF::3::_strategy = st.builds(
    fastfst::nBlPitchF::3::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nBlPitchF::2::_strategy = st.builds(
    fastfst::nBlPitchF::2::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::bCompNoise_strategy = st.builds(
    fastfst::bCompNoise,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nBlPitchF::1::_strategy = st.builds(
    fastfst::nBlPitchF::1::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bCompAero_strategy = st.builds(
    fastfst::bCompAero,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nBlPitch::3::_strategy = st.builds(
    fastfst::nBlPitch::3::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bTwSSDOF2_strategy = st.builds(
    fastfst::bTwSSDOF2,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::nBlPitch::2::_strategy = st.builds(
    fastfst::nBlPitch::2::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bTwSSDOF1_strategy = st.builds(
    fastfst::bTwSSDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::bTwFADOF2_strategy = st.builds(
    fastfst::bTwFADOF2,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::nTPitManE::2::_strategy = st.builds(
    fastfst::nTPitManE::2::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTPitManE::1::_strategy = st.builds(
    fastfst::nTPitManE::1::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTPitManS::3::_strategy = st.builds(
    fastfst::nTPitManS::3::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTPitManS::2::_strategy = st.builds(
    fastfst::nTPitManS::2::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTPitManS::1::_strategy = st.builds(
    fastfst::nTPitManS::1::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nNacYawF_strategy = st.builds(
    fastfst::nNacYawF,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTYawManE_strategy = st.builds(
    fastfst::nTYawManE,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTYawManS_strategy = st.builds(
    fastfst::nTYawManS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTBDepISp::3::_strategy = st.builds(
    fastfst::nTBDepISp::3::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTBDepISp::2::_strategy = st.builds(
    fastfst::nTBDepISp::2::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTBDepISp::1::_strategy = st.builds(
    fastfst::nTBDepISp::1::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTTpBrDp::3::_strategy = st.builds(
    fastfst::nTTpBrDp::3::,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTTpBrDp::2::_strategy = st.builds(
    fastfst::nTTpBrDp::2::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTTpBrDp::1::_strategy = st.builds(
    fastfst::nTTpBrDp::1::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nBlPitch::1::_strategy = st.builds(
    fastfst::nBlPitch::1::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTPitManE::3::_strategy = st.builds(
    fastfst::nTPitManE::3::,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::iHSSBrMode_strategy = st.builds(
    fastfst::iHSSBrMode,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::nTimGenOf_strategy = st.builds(
    fastfst::nTimGenOf,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTimGenOn_strategy = st.builds(
    fastfst::nTimGenOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nSpdGenOn_strategy = st.builds(
    fastfst::nSpdGenOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::bGenTiStp_strategy = st.builds(
    fastfst::bGenTiStp,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::bGenTiStr_strategy = st.builds(
    fastfst::bGenTiStr,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst::iGenModel_strategy = st.builds(
    fastfst::iGenModel,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::nVS::SlPc_strategy = st.builds(
    fastfst::nVS::SlPc,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nVS::Rgn2K_strategy = st.builds(
    fastfst::nVS::Rgn2K,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nVS::RtTq_strategy = st.builds(
    fastfst::nVS::RtTq,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nVS::RtGnSp_strategy = st.builds(
    fastfst::nVS::RtGnSp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::iVSContrl_strategy = st.builds(
    fastfst::iVSContrl,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::nTPCOn_strategy = st.builds(
    fastfst::nTPCOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::iPCMode_strategy = st.builds(
    fastfst::iPCMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::nTYCOn_strategy = st.builds(
    fastfst::nTYCOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::iYCMode_strategy = st.builds(
    fastfst::iYCMode,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::nDT_strategy = st.builds(
    fastfst::nDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTMax_strategy = st.builds(
    fastfst::nTMax,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst::nTiDynBrk_strategy = st.builds(
    fastfst::nTiDynBrk,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::nTHSSBrDp_strategy = st.builds(
    fastfst::nTHSSBrDp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst::iADAMSPrep_strategy = st.builds(
    fastfst::iADAMSPrep,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst::bEcho_strategy = st.builds(
    fastfst::bEcho,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst::Section_strategy = st.builds(
    fastfst::Section,
    name=
        safe_text
)
fastfst::Header_strategy = st.builds(
    fastfst::Header,
    rows=
        safe_text
)
fastfst::ModelFastfst_strategy = st.builds(
    fastfst::ModelFastfst,
)
fastfst::iNumBl_strategy = st.builds(
    fastfst::iNumBl,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst::iAnalMode_strategy = st.builds(
    fastfst::iAnalMode,
    name=
        safe_text,
    value=
        st.integers()
)

@given(instance=fastfst::nShftGagL_strategy)
@settings(max_examples=50)
def test_fastfst::nshftgagl_instantiation(instance):
    assert isinstance(instance, fastfst::nShftGagL)

@given(instance=fastfst::nShftGagL_strategy)
def test_fastfst::nshftgagl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nShftGagL_strategy)
def test_fastfst::nshftgagl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nShftGagL_strategy)
def test_fastfst::nshftgagl_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nShftGagL_strategy)
def test_fastfst::nshftgagl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNcIMUzn_strategy)
@settings(max_examples=50)
def test_fastfst::nncimuzn_instantiation(instance):
    assert isinstance(instance, fastfst::nNcIMUzn)

@given(instance=fastfst::nNcIMUzn_strategy)
def test_fastfst::nncimuzn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNcIMUzn_strategy)
def test_fastfst::nncimuzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNcIMUzn_strategy)
def test_fastfst::nncimuzn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNcIMUzn_strategy)
def test_fastfst::nncimuzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::vOutList_strategy)
@settings(max_examples=50)
def test_fastfst::voutlist_instantiation(instance):
    assert isinstance(instance, fastfst::vOutList)

@given(instance=fastfst::vOutList_strategy)
def test_fastfst::voutlist_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::vOutList_strategy)
def test_fastfst::voutlist_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::vOutList_strategy)
def test_fastfst::voutlist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::vOutList_strategy)
def test_fastfst::voutlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::aBldGagNd_strategy)
@settings(max_examples=50)
def test_fastfst::abldgagnd_instantiation(instance):
    assert isinstance(instance, fastfst::aBldGagNd)

@given(instance=fastfst::aBldGagNd_strategy)
def test_fastfst::abldgagnd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::aBldGagNd_strategy)
def test_fastfst::abldgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::aBldGagNd_strategy)
def test_fastfst::abldgagnd_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::aBldGagNd_strategy)
def test_fastfst::abldgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iNBlGages_strategy)
@settings(max_examples=50)
def test_fastfst::inblgages_instantiation(instance):
    assert isinstance(instance, fastfst::iNBlGages)

@given(instance=fastfst::iNBlGages_strategy)
def test_fastfst::inblgages_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iNBlGages_strategy)
def test_fastfst::inblgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iNBlGages_strategy)
def test_fastfst::inblgages_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iNBlGages_strategy)
def test_fastfst::inblgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::aTwrGagNd_strategy)
@settings(max_examples=50)
def test_fastfst::atwrgagnd_instantiation(instance):
    assert isinstance(instance, fastfst::aTwrGagNd)

@given(instance=fastfst::aTwrGagNd_strategy)
def test_fastfst::atwrgagnd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::aTwrGagNd_strategy)
def test_fastfst::atwrgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::aTwrGagNd_strategy)
def test_fastfst::atwrgagnd_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::aTwrGagNd_strategy)
def test_fastfst::atwrgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iNTwGages_strategy)
@settings(max_examples=50)
def test_fastfst::intwgages_instantiation(instance):
    assert isinstance(instance, fastfst::iNTwGages)

@given(instance=fastfst::iNTwGages_strategy)
def test_fastfst::intwgages_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iNTwGages_strategy)
def test_fastfst::intwgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iNTwGages_strategy)
def test_fastfst::intwgages_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iNTwGages_strategy)
def test_fastfst::intwgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::sOutFmt_strategy)
@settings(max_examples=50)
def test_fastfst::soutfmt_instantiation(instance):
    assert isinstance(instance, fastfst::sOutFmt)

@given(instance=fastfst::sOutFmt_strategy)
def test_fastfst::soutfmt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::sOutFmt_strategy)
def test_fastfst::soutfmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::sOutFmt_strategy)
def test_fastfst::soutfmt_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::sOutFmt_strategy)
def test_fastfst::soutfmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTabDelim_strategy)
@settings(max_examples=50)
def test_fastfst::btabdelim_instantiation(instance):
    assert isinstance(instance, fastfst::bTabDelim)

@given(instance=fastfst::bTabDelim_strategy)
def test_fastfst::btabdelim_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTabDelim_strategy)
def test_fastfst::btabdelim_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTabDelim_strategy)
def test_fastfst::btabdelim_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTabDelim_strategy)
def test_fastfst::btabdelim_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNcIMUyn_strategy)
@settings(max_examples=50)
def test_fastfst::nncimuyn_instantiation(instance):
    assert isinstance(instance, fastfst::nNcIMUyn)

@given(instance=fastfst::nNcIMUyn_strategy)
def test_fastfst::nncimuyn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNcIMUyn_strategy)
def test_fastfst::nncimuyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNcIMUyn_strategy)
def test_fastfst::nncimuyn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNcIMUyn_strategy)
def test_fastfst::nncimuyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNcIMUxn_strategy)
@settings(max_examples=50)
def test_fastfst::nncimuxn_instantiation(instance):
    assert isinstance(instance, fastfst::nNcIMUxn)

@given(instance=fastfst::nNcIMUxn_strategy)
def test_fastfst::nncimuxn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNcIMUxn_strategy)
def test_fastfst::nncimuxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNcIMUxn_strategy)
def test_fastfst::nncimuxn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNcIMUxn_strategy)
def test_fastfst::nncimuxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSttsTime_strategy)
@settings(max_examples=50)
def test_fastfst::nsttstime_instantiation(instance):
    assert isinstance(instance, fastfst::nSttsTime)

@given(instance=fastfst::nSttsTime_strategy)
def test_fastfst::nsttstime_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSttsTime_strategy)
def test_fastfst::nsttstime_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSttsTime_strategy)
def test_fastfst::nsttstime_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSttsTime_strategy)
def test_fastfst::nsttstime_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iDecFact_strategy)
@settings(max_examples=50)
def test_fastfst::idecfact_instantiation(instance):
    assert isinstance(instance, fastfst::iDecFact)

@given(instance=fastfst::iDecFact_strategy)
def test_fastfst::idecfact_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iDecFact_strategy)
def test_fastfst::idecfact_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iDecFact_strategy)
def test_fastfst::idecfact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iDecFact_strategy)
def test_fastfst::idecfact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTStart_strategy)
@settings(max_examples=50)
def test_fastfst::ntstart_instantiation(instance):
    assert isinstance(instance, fastfst::nTStart)

@given(instance=fastfst::nTStart_strategy)
def test_fastfst::ntstart_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTStart_strategy)
def test_fastfst::ntstart_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTStart_strategy)
def test_fastfst::ntstart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTStart_strategy)
def test_fastfst::ntstart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fBldFile::3::_strategy)
@settings(max_examples=50)
def test_fastfst::fbldfile::3::_instantiation(instance):
    assert isinstance(instance, fastfst::fBldFile::3::)

@given(instance=fastfst::fBldFile::3::_strategy)
def test_fastfst::fbldfile::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fBldFile::3::_strategy)
def test_fastfst::fbldfile::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fBldFile::3::_strategy)
def test_fastfst::fbldfile::3::_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fBldFile::3::_strategy)
def test_fastfst::fbldfile::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fBldFile::2::_strategy)
@settings(max_examples=50)
def test_fastfst::fbldfile::2::_instantiation(instance):
    assert isinstance(instance, fastfst::fBldFile::2::)

@given(instance=fastfst::fBldFile::2::_strategy)
def test_fastfst::fbldfile::2::_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fBldFile::2::_strategy)
def test_fastfst::fbldfile::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fBldFile::2::_strategy)
def test_fastfst::fbldfile::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fBldFile::2::_strategy)
def test_fastfst::fbldfile::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bOutFileFmt_strategy)
@settings(max_examples=50)
def test_fastfst::boutfilefmt_instantiation(instance):
    assert isinstance(instance, fastfst::bOutFileFmt)

@given(instance=fastfst::bOutFileFmt_strategy)
def test_fastfst::boutfilefmt_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::bOutFileFmt_strategy)
def test_fastfst::boutfilefmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bOutFileFmt_strategy)
def test_fastfst::boutfilefmt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bOutFileFmt_strategy)
def test_fastfst::boutfilefmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bSumPrint_strategy)
@settings(max_examples=50)
def test_fastfst::bsumprint_instantiation(instance):
    assert isinstance(instance, fastfst::bSumPrint)

@given(instance=fastfst::bSumPrint_strategy)
def test_fastfst::bsumprint_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bSumPrint_strategy)
def test_fastfst::bsumprint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bSumPrint_strategy)
def test_fastfst::bsumprint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bSumPrint_strategy)
def test_fastfst::bsumprint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fLinFile_strategy)
@settings(max_examples=50)
def test_fastfst::flinfile_instantiation(instance):
    assert isinstance(instance, fastfst::fLinFile)

@given(instance=fastfst::fLinFile_strategy)
def test_fastfst::flinfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fLinFile_strategy)
def test_fastfst::flinfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fLinFile_strategy)
def test_fastfst::flinfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fLinFile_strategy)
def test_fastfst::flinfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fADAMSFile_strategy)
@settings(max_examples=50)
def test_fastfst::fadamsfile_instantiation(instance):
    assert isinstance(instance, fastfst::fADAMSFile)

@given(instance=fastfst::fADAMSFile_strategy)
def test_fastfst::fadamsfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fADAMSFile_strategy)
def test_fastfst::fadamsfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fADAMSFile_strategy)
def test_fastfst::fadamsfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fADAMSFile_strategy)
def test_fastfst::fadamsfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fNoiseFile_strategy)
@settings(max_examples=50)
def test_fastfst::fnoisefile_instantiation(instance):
    assert isinstance(instance, fastfst::fNoiseFile)

@given(instance=fastfst::fNoiseFile_strategy)
def test_fastfst::fnoisefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fNoiseFile_strategy)
def test_fastfst::fnoisefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fNoiseFile_strategy)
def test_fastfst::fnoisefile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fNoiseFile_strategy)
def test_fastfst::fnoisefile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fADFile_strategy)
@settings(max_examples=50)
def test_fastfst::fadfile_instantiation(instance):
    assert isinstance(instance, fastfst::fADFile)

@given(instance=fastfst::fADFile_strategy)
def test_fastfst::fadfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fADFile_strategy)
def test_fastfst::fadfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fADFile_strategy)
def test_fastfst::fadfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fADFile_strategy)
def test_fastfst::fadfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetHStP_strategy)
@settings(max_examples=50)
def test_fastfst::nteethstp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetHStP)

@given(instance=fastfst::nTeetHStP_strategy)
def test_fastfst::nteethstp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetHStP_strategy)
def test_fastfst::nteethstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetHStP_strategy)
def test_fastfst::nteethstp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetHStP_strategy)
def test_fastfst::nteethstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetSStP_strategy)
@settings(max_examples=50)
def test_fastfst::nteetsstp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetSStP)

@given(instance=fastfst::nTeetSStP_strategy)
def test_fastfst::nteetsstp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetSStP_strategy)
def test_fastfst::nteetsstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetSStP_strategy)
def test_fastfst::nteetsstp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetSStP_strategy)
def test_fastfst::nteetsstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fBldFile::1::_strategy)
@settings(max_examples=50)
def test_fastfst::fbldfile::1::_instantiation(instance):
    assert isinstance(instance, fastfst::fBldFile::1::)

@given(instance=fastfst::fBldFile::1::_strategy)
def test_fastfst::fbldfile::1::_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fBldFile::1::_strategy)
def test_fastfst::fbldfile::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fBldFile::1::_strategy)
def test_fastfst::fbldfile::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fBldFile::1::_strategy)
def test_fastfst::fbldfile::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTpBrDT_strategy)
@settings(max_examples=50)
def test_fastfst::ntpbrdt_instantiation(instance):
    assert isinstance(instance, fastfst::nTpBrDT)

@given(instance=fastfst::nTpBrDT_strategy)
def test_fastfst::ntpbrdt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTpBrDT_strategy)
def test_fastfst::ntpbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTpBrDT_strategy)
def test_fastfst::ntpbrdt_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTpBrDT_strategy)
def test_fastfst::ntpbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTBDrConD_strategy)
@settings(max_examples=50)
def test_fastfst::ntbdrcond_instantiation(instance):
    assert isinstance(instance, fastfst::nTBDrConD)

@given(instance=fastfst::nTBDrConD_strategy)
def test_fastfst::ntbdrcond_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTBDrConD_strategy)
def test_fastfst::ntbdrcond_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDrConD_strategy)
def test_fastfst::ntbdrcond_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTBDrConD_strategy)
def test_fastfst::ntbdrcond_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTBDrConN_strategy)
@settings(max_examples=50)
def test_fastfst::ntbdrconn_instantiation(instance):
    assert isinstance(instance, fastfst::nTBDrConN)

@given(instance=fastfst::nTBDrConN_strategy)
def test_fastfst::ntbdrconn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTBDrConN_strategy)
def test_fastfst::ntbdrconn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDrConN_strategy)
def test_fastfst::ntbdrconn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTBDrConN_strategy)
def test_fastfst::ntbdrconn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetHSSp_strategy)
@settings(max_examples=50)
def test_fastfst::nteethssp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetHSSp)

@given(instance=fastfst::nTeetHSSp_strategy)
def test_fastfst::nteethssp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetHSSp_strategy)
def test_fastfst::nteethssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetHSSp_strategy)
def test_fastfst::nteethssp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetHSSp_strategy)
def test_fastfst::nteethssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetSSSp_strategy)
@settings(max_examples=50)
def test_fastfst::nteetsssp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetSSSp)

@given(instance=fastfst::nTeetSSSp_strategy)
def test_fastfst::nteetsssp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetSSSp_strategy)
def test_fastfst::nteetsssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetSSSp_strategy)
def test_fastfst::nteetsssp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetSSSp_strategy)
def test_fastfst::nteetsssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nYawNeut_strategy)
@settings(max_examples=50)
def test_fastfst::nyawneut_instantiation(instance):
    assert isinstance(instance, fastfst::nYawNeut)

@given(instance=fastfst::nYawNeut_strategy)
def test_fastfst::nyawneut_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nYawNeut_strategy)
def test_fastfst::nyawneut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nYawNeut_strategy)
def test_fastfst::nyawneut_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nYawNeut_strategy)
def test_fastfst::nyawneut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nYawDamp_strategy)
@settings(max_examples=50)
def test_fastfst::nyawdamp_instantiation(instance):
    assert isinstance(instance, fastfst::nYawDamp)

@given(instance=fastfst::nYawDamp_strategy)
def test_fastfst::nyawdamp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nYawDamp_strategy)
def test_fastfst::nyawdamp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nYawDamp_strategy)
def test_fastfst::nyawdamp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nYawDamp_strategy)
def test_fastfst::nyawdamp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetCDmp_strategy)
@settings(max_examples=50)
def test_fastfst::nteetcdmp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetCDmp)

@given(instance=fastfst::nTeetCDmp_strategy)
def test_fastfst::nteetcdmp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetCDmp_strategy)
def test_fastfst::nteetcdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetCDmp_strategy)
def test_fastfst::nteetcdmp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetCDmp_strategy)
def test_fastfst::nteetcdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetDmp_strategy)
@settings(max_examples=50)
def test_fastfst::nteetdmp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetDmp)

@given(instance=fastfst::nTeetDmp_strategy)
def test_fastfst::nteetdmp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetDmp_strategy)
def test_fastfst::nteetdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetDmp_strategy)
def test_fastfst::nteetdmp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetDmp_strategy)
def test_fastfst::nteetdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTeetDmpP_strategy)
@settings(max_examples=50)
def test_fastfst::nteetdmpp_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetDmpP)

@given(instance=fastfst::nTeetDmpP_strategy)
def test_fastfst::nteetdmpp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetDmpP_strategy)
def test_fastfst::nteetdmpp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetDmpP_strategy)
def test_fastfst::nteetdmpp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetDmpP_strategy)
def test_fastfst::nteetdmpp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iTeetMod_strategy)
@settings(max_examples=50)
def test_fastfst::iteetmod_instantiation(instance):
    assert isinstance(instance, fastfst::iTeetMod)

@given(instance=fastfst::iTeetMod_strategy)
def test_fastfst::iteetmod_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iTeetMod_strategy)
def test_fastfst::iteetmod_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iTeetMod_strategy)
def test_fastfst::iteetmod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iTeetMod_strategy)
def test_fastfst::iteetmod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fFurlFile_strategy)
@settings(max_examples=50)
def test_fastfst::ffurlfile_instantiation(instance):
    assert isinstance(instance, fastfst::fFurlFile)

@given(instance=fastfst::fFurlFile_strategy)
def test_fastfst::ffurlfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fFurlFile_strategy)
def test_fastfst::ffurlfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fFurlFile_strategy)
def test_fastfst::ffurlfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fFurlFile_strategy)
def test_fastfst::ffurlfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::RLR_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::rlr_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::RLR)

@given(instance=fastfst::nTEC::RLR_strategy)
def test_fastfst::ntec::rlr_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::RLR_strategy)
def test_fastfst::ntec::rlr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::RLR_strategy)
def test_fastfst::ntec::rlr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::RLR_strategy)
def test_fastfst::ntec::rlr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bFurling_strategy)
@settings(max_examples=50)
def test_fastfst::bfurling_instantiation(instance):
    assert isinstance(instance, fastfst::bFurling)

@given(instance=fastfst::bFurling_strategy)
def test_fastfst::bfurling_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bFurling_strategy)
def test_fastfst::bfurling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bFurling_strategy)
def test_fastfst::bfurling_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bFurling_strategy)
def test_fastfst::bfurling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::SLR_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::slr_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::SLR)

@given(instance=fastfst::nTEC::SLR_strategy)
def test_fastfst::ntec::slr_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::SLR_strategy)
def test_fastfst::ntec::slr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::SLR_strategy)
def test_fastfst::ntec::slr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::SLR_strategy)
def test_fastfst::ntec::slr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nYawSpr_strategy)
@settings(max_examples=50)
def test_fastfst::nyawspr_instantiation(instance):
    assert isinstance(instance, fastfst::nYawSpr)

@given(instance=fastfst::nYawSpr_strategy)
def test_fastfst::nyawspr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nYawSpr_strategy)
def test_fastfst::nyawspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nYawSpr_strategy)
def test_fastfst::nyawspr_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nYawSpr_strategy)
def test_fastfst::nyawspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fTwrFile_strategy)
@settings(max_examples=50)
def test_fastfst::ftwrfile_instantiation(instance):
    assert isinstance(instance, fastfst::fTwrFile)

@given(instance=fastfst::fTwrFile_strategy)
def test_fastfst::ftwrfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fTwrFile_strategy)
def test_fastfst::ftwrfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fTwrFile_strategy)
def test_fastfst::ftwrfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fTwrFile_strategy)
def test_fastfst::ftwrfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iTwrNodes_strategy)
@settings(max_examples=50)
def test_fastfst::itwrnodes_instantiation(instance):
    assert isinstance(instance, fastfst::iTwrNodes)

@given(instance=fastfst::iTwrNodes_strategy)
def test_fastfst::itwrnodes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iTwrNodes_strategy)
def test_fastfst::itwrnodes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iTwrNodes_strategy)
def test_fastfst::itwrnodes_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iTwrNodes_strategy)
def test_fastfst::itwrnodes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::fPtfmFile_strategy)
@settings(max_examples=50)
def test_fastfst::fptfmfile_instantiation(instance):
    assert isinstance(instance, fastfst::fPtfmFile)

@given(instance=fastfst::fPtfmFile_strategy)
def test_fastfst::fptfmfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fPtfmFile_strategy)
def test_fastfst::fptfmfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fPtfmFile_strategy)
def test_fastfst::fptfmfile_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fPtfmFile_strategy)
def test_fastfst::fptfmfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iPtfmModel_strategy)
@settings(max_examples=50)
def test_fastfst::iptfmmodel_instantiation(instance):
    assert isinstance(instance, fastfst::iPtfmModel)

@given(instance=fastfst::iPtfmModel_strategy)
def test_fastfst::iptfmmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iPtfmModel_strategy)
def test_fastfst::iptfmmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iPtfmModel_strategy)
def test_fastfst::iptfmmodel_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iPtfmModel_strategy)
def test_fastfst::iptfmmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::MR_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::mr_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::MR)

@given(instance=fastfst::nTEC::MR_strategy)
def test_fastfst::ntec::mr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::MR_strategy)
def test_fastfst::ntec::mr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::MR_strategy)
def test_fastfst::ntec::mr_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::MR_strategy)
def test_fastfst::ntec::mr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nSIG::SlPc_strategy)
@settings(max_examples=50)
def test_fastfst::nsig::slpc_instantiation(instance):
    assert isinstance(instance, fastfst::nSIG::SlPc)

@given(instance=fastfst::nSIG::SlPc_strategy)
def test_fastfst::nsig::slpc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSIG::SlPc_strategy)
def test_fastfst::nsig::slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSIG::SlPc_strategy)
def test_fastfst::nsig::slpc_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSIG::SlPc_strategy)
def test_fastfst::nsig::slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDTTorDmp_strategy)
@settings(max_examples=50)
def test_fastfst::ndttordmp_instantiation(instance):
    assert isinstance(instance, fastfst::nDTTorDmp)

@given(instance=fastfst::nDTTorDmp_strategy)
def test_fastfst::ndttordmp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nDTTorDmp_strategy)
def test_fastfst::ndttordmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDTTorDmp_strategy)
def test_fastfst::ndttordmp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nDTTorDmp_strategy)
def test_fastfst::ndttordmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::VLL_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::vll_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::VLL)

@given(instance=fastfst::nTEC::VLL_strategy)
def test_fastfst::ntec::vll_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::VLL_strategy)
def test_fastfst::ntec::vll_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::VLL_strategy)
def test_fastfst::ntec::vll_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::VLL_strategy)
def test_fastfst::ntec::vll_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::Rres_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::rres_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::Rres)

@given(instance=fastfst::nTEC::Rres_strategy)
def test_fastfst::ntec::rres_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::Rres_strategy)
def test_fastfst::ntec::rres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::Rres_strategy)
def test_fastfst::ntec::rres_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::Rres_strategy)
def test_fastfst::ntec::rres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::Sres_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::sres_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::Sres)

@given(instance=fastfst::nTEC::Sres_strategy)
def test_fastfst::ntec::sres_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::Sres_strategy)
def test_fastfst::ntec::sres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::Sres_strategy)
def test_fastfst::ntec::sres_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::Sres_strategy)
def test_fastfst::ntec::sres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::Npol_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::npol_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::Npol)

@given(instance=fastfst::nTEC::Npol_strategy)
def test_fastfst::ntec::npol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::Npol_strategy)
def test_fastfst::ntec::npol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTEC::Npol_strategy)
def test_fastfst::ntec::npol_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::Npol_strategy)
def test_fastfst::ntec::npol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::Freq_strategy)
@settings(max_examples=50)
def test_fastfst::ntec::freq_instantiation(instance):
    assert isinstance(instance, fastfst::nTEC::Freq)

@given(instance=fastfst::nTEC::Freq_strategy)
def test_fastfst::ntec::freq_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTEC::Freq_strategy)
def test_fastfst::ntec::freq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTEC::Freq_strategy)
def test_fastfst::ntec::freq_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTEC::Freq_strategy)
def test_fastfst::ntec::freq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSIG::PORt_strategy)
@settings(max_examples=50)
def test_fastfst::nsig::port_instantiation(instance):
    assert isinstance(instance, fastfst::nSIG::PORt)

@given(instance=fastfst::nSIG::PORt_strategy)
def test_fastfst::nsig::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSIG::PORt_strategy)
def test_fastfst::nsig::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSIG::PORt_strategy)
def test_fastfst::nsig::port_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSIG::PORt_strategy)
def test_fastfst::nsig::port_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nSIG::RtTq_strategy)
@settings(max_examples=50)
def test_fastfst::nsig::rttq_instantiation(instance):
    assert isinstance(instance, fastfst::nSIG::RtTq)

@given(instance=fastfst::nSIG::RtTq_strategy)
def test_fastfst::nsig::rttq_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSIG::RtTq_strategy)
def test_fastfst::nsig::rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nSIG::RtTq_strategy)
def test_fastfst::nsig::rttq_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSIG::RtTq_strategy)
def test_fastfst::nsig::rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSIG::SySp_strategy)
@settings(max_examples=50)
def test_fastfst::nsig::sysp_instantiation(instance):
    assert isinstance(instance, fastfst::nSIG::SySp)

@given(instance=fastfst::nSIG::SySp_strategy)
def test_fastfst::nsig::sysp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSIG::SySp_strategy)
def test_fastfst::nsig::sysp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nSIG::SySp_strategy)
def test_fastfst::nsig::sysp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSIG::SySp_strategy)
def test_fastfst::nsig::sysp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGenIner_strategy)
@settings(max_examples=50)
def test_fastfst::ngeniner_instantiation(instance):
    assert isinstance(instance, fastfst::nGenIner)

@given(instance=fastfst::nGenIner_strategy)
def test_fastfst::ngeniner_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nGenIner_strategy)
def test_fastfst::ngeniner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGenIner_strategy)
def test_fastfst::ngeniner_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nGenIner_strategy)
def test_fastfst::ngeniner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nDTTorSpr_strategy)
@settings(max_examples=50)
def test_fastfst::ndttorspr_instantiation(instance):
    assert isinstance(instance, fastfst::nDTTorSpr)

@given(instance=fastfst::nDTTorSpr_strategy)
def test_fastfst::ndttorspr_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nDTTorSpr_strategy)
def test_fastfst::ndttorspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDTTorSpr_strategy)
def test_fastfst::ndttorspr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nDTTorSpr_strategy)
def test_fastfst::ndttorspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fDynBrkFi_strategy)
@settings(max_examples=50)
def test_fastfst::fdynbrkfi_instantiation(instance):
    assert isinstance(instance, fastfst::fDynBrkFi)

@given(instance=fastfst::fDynBrkFi_strategy)
def test_fastfst::fdynbrkfi_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::fDynBrkFi_strategy)
def test_fastfst::fdynbrkfi_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::fDynBrkFi_strategy)
def test_fastfst::fdynbrkfi_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fastfst::fDynBrkFi_strategy)
def test_fastfst::fdynbrkfi_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHSSBrDT_strategy)
@settings(max_examples=50)
def test_fastfst::nhssbrdt_instantiation(instance):
    assert isinstance(instance, fastfst::nHSSBrDT)

@given(instance=fastfst::nHSSBrDT_strategy)
def test_fastfst::nhssbrdt_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHSSBrDT_strategy)
def test_fastfst::nhssbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHSSBrDT_strategy)
def test_fastfst::nhssbrdt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHSSBrDT_strategy)
def test_fastfst::nhssbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHSSBrTqF_strategy)
@settings(max_examples=50)
def test_fastfst::nhssbrtqf_instantiation(instance):
    assert isinstance(instance, fastfst::nHSSBrTqF)

@given(instance=fastfst::nHSSBrTqF_strategy)
def test_fastfst::nhssbrtqf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHSSBrTqF_strategy)
def test_fastfst::nhssbrtqf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHSSBrTqF_strategy)
def test_fastfst::nhssbrtqf_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHSSBrTqF_strategy)
def test_fastfst::nhssbrtqf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bGBRevers_strategy)
@settings(max_examples=50)
def test_fastfst::bgbrevers_instantiation(instance):
    assert isinstance(instance, fastfst::bGBRevers)

@given(instance=fastfst::bGBRevers_strategy)
def test_fastfst::bgbrevers_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bGBRevers_strategy)
def test_fastfst::bgbrevers_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bGBRevers_strategy)
def test_fastfst::bgbrevers_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bGBRevers_strategy)
def test_fastfst::bgbrevers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nGBRatio_strategy)
@settings(max_examples=50)
def test_fastfst::ngbratio_instantiation(instance):
    assert isinstance(instance, fastfst::nGBRatio)

@given(instance=fastfst::nGBRatio_strategy)
def test_fastfst::ngbratio_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nGBRatio_strategy)
def test_fastfst::ngbratio_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nGBRatio_strategy)
def test_fastfst::ngbratio_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nGBRatio_strategy)
def test_fastfst::ngbratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGenEff_strategy)
@settings(max_examples=50)
def test_fastfst::ngeneff_instantiation(instance):
    assert isinstance(instance, fastfst::nGenEff)

@given(instance=fastfst::nGenEff_strategy)
def test_fastfst::ngeneff_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nGenEff_strategy)
def test_fastfst::ngeneff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGenEff_strategy)
def test_fastfst::ngeneff_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nGenEff_strategy)
def test_fastfst::ngeneff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nGBoxEff_strategy)
@settings(max_examples=50)
def test_fastfst::ngboxeff_instantiation(instance):
    assert isinstance(instance, fastfst::nGBoxEff)

@given(instance=fastfst::nGBoxEff_strategy)
def test_fastfst::ngboxeff_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nGBoxEff_strategy)
def test_fastfst::ngboxeff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGBoxEff_strategy)
def test_fastfst::ngboxeff_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nGBoxEff_strategy)
def test_fastfst::ngboxeff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHubIner_strategy)
@settings(max_examples=50)
def test_fastfst::nhubiner_instantiation(instance):
    assert isinstance(instance, fastfst::nHubIner)

@given(instance=fastfst::nHubIner_strategy)
def test_fastfst::nhubiner_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHubIner_strategy)
def test_fastfst::nhubiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHubIner_strategy)
def test_fastfst::nhubiner_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHubIner_strategy)
def test_fastfst::nhubiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nPreCone::2::_strategy)
@settings(max_examples=50)
def test_fastfst::nprecone::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nPreCone::2::)

@given(instance=fastfst::nPreCone::2::_strategy)
def test_fastfst::nprecone::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nPreCone::2::_strategy)
def test_fastfst::nprecone::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nPreCone::2::_strategy)
def test_fastfst::nprecone::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nPreCone::2::_strategy)
def test_fastfst::nprecone::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacYIner_strategy)
@settings(max_examples=50)
def test_fastfst::nnacyiner_instantiation(instance):
    assert isinstance(instance, fastfst::nNacYIner)

@given(instance=fastfst::nNacYIner_strategy)
def test_fastfst::nnacyiner_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacYIner_strategy)
def test_fastfst::nnacyiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacYIner_strategy)
def test_fastfst::nnacyiner_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacYIner_strategy)
def test_fastfst::nnacyiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTipMass::3::_strategy)
@settings(max_examples=50)
def test_fastfst::ntipmass::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nTipMass::3::)

@given(instance=fastfst::nTipMass::3::_strategy)
def test_fastfst::ntipmass::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTipMass::3::_strategy)
def test_fastfst::ntipmass::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTipMass::3::_strategy)
def test_fastfst::ntipmass::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTipMass::3::_strategy)
def test_fastfst::ntipmass::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTipMass::2::_strategy)
@settings(max_examples=50)
def test_fastfst::ntipmass::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nTipMass::2::)

@given(instance=fastfst::nTipMass::2::_strategy)
def test_fastfst::ntipmass::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTipMass::2::_strategy)
def test_fastfst::ntipmass::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTipMass::2::_strategy)
def test_fastfst::ntipmass::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTipMass::2::_strategy)
def test_fastfst::ntipmass::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTipMass::1::_strategy)
@settings(max_examples=50)
def test_fastfst::ntipmass::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nTipMass::1::)

@given(instance=fastfst::nTipMass::1::_strategy)
def test_fastfst::ntipmass::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTipMass::1::_strategy)
def test_fastfst::ntipmass::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTipMass::1::_strategy)
def test_fastfst::ntipmass::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTipMass::1::_strategy)
def test_fastfst::ntipmass::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHubMass_strategy)
@settings(max_examples=50)
def test_fastfst::nhubmass_instantiation(instance):
    assert isinstance(instance, fastfst::nHubMass)

@given(instance=fastfst::nHubMass_strategy)
def test_fastfst::nhubmass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHubMass_strategy)
def test_fastfst::nhubmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHubMass_strategy)
def test_fastfst::nhubmass_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHubMass_strategy)
def test_fastfst::nhubmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacMass_strategy)
@settings(max_examples=50)
def test_fastfst::nnacmass_instantiation(instance):
    assert isinstance(instance, fastfst::nNacMass)

@given(instance=fastfst::nNacMass_strategy)
def test_fastfst::nnacmass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacMass_strategy)
def test_fastfst::nnacmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacMass_strategy)
def test_fastfst::nnacmass_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacMass_strategy)
def test_fastfst::nnacmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nYawBrMass_strategy)
@settings(max_examples=50)
def test_fastfst::nyawbrmass_instantiation(instance):
    assert isinstance(instance, fastfst::nYawBrMass)

@given(instance=fastfst::nYawBrMass_strategy)
def test_fastfst::nyawbrmass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nYawBrMass_strategy)
def test_fastfst::nyawbrmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nYawBrMass_strategy)
def test_fastfst::nyawbrmass_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nYawBrMass_strategy)
def test_fastfst::nyawbrmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nAzimB1Up_strategy)
@settings(max_examples=50)
def test_fastfst::nazimb1up_instantiation(instance):
    assert isinstance(instance, fastfst::nAzimB1Up)

@given(instance=fastfst::nAzimB1Up_strategy)
def test_fastfst::nazimb1up_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nAzimB1Up_strategy)
def test_fastfst::nazimb1up_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nAzimB1Up_strategy)
def test_fastfst::nazimb1up_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nAzimB1Up_strategy)
def test_fastfst::nazimb1up_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nPreCone::3::_strategy)
@settings(max_examples=50)
def test_fastfst::nprecone::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nPreCone::3::)

@given(instance=fastfst::nPreCone::3::_strategy)
def test_fastfst::nprecone::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nPreCone::3::_strategy)
def test_fastfst::nprecone::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nPreCone::3::_strategy)
def test_fastfst::nprecone::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nPreCone::3::_strategy)
def test_fastfst::nprecone::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacCMxn_strategy)
@settings(max_examples=50)
def test_fastfst::nnaccmxn_instantiation(instance):
    assert isinstance(instance, fastfst::nNacCMxn)

@given(instance=fastfst::nNacCMxn_strategy)
def test_fastfst::nnaccmxn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacCMxn_strategy)
def test_fastfst::nnaccmxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacCMxn_strategy)
def test_fastfst::nnaccmxn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacCMxn_strategy)
def test_fastfst::nnaccmxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nOverHang_strategy)
@settings(max_examples=50)
def test_fastfst::noverhang_instantiation(instance):
    assert isinstance(instance, fastfst::nOverHang)

@given(instance=fastfst::nOverHang_strategy)
def test_fastfst::noverhang_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nOverHang_strategy)
def test_fastfst::noverhang_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nOverHang_strategy)
def test_fastfst::noverhang_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nOverHang_strategy)
def test_fastfst::noverhang_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHubCM_strategy)
@settings(max_examples=50)
def test_fastfst::nhubcm_instantiation(instance):
    assert isinstance(instance, fastfst::nHubCM)

@given(instance=fastfst::nHubCM_strategy)
def test_fastfst::nhubcm_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHubCM_strategy)
def test_fastfst::nhubcm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nHubCM_strategy)
def test_fastfst::nhubcm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHubCM_strategy)
def test_fastfst::nhubcm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nPreCone::1::_strategy)
@settings(max_examples=50)
def test_fastfst::nprecone::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nPreCone::1::)

@given(instance=fastfst::nPreCone::1::_strategy)
def test_fastfst::nprecone::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nPreCone::1::_strategy)
def test_fastfst::nprecone::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nPreCone::1::_strategy)
def test_fastfst::nprecone::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nPreCone::1::_strategy)
def test_fastfst::nprecone::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDelta3_strategy)
@settings(max_examples=50)
def test_fastfst::ndelta3_instantiation(instance):
    assert isinstance(instance, fastfst::nDelta3)

@given(instance=fastfst::nDelta3_strategy)
def test_fastfst::ndelta3_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nDelta3_strategy)
def test_fastfst::ndelta3_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDelta3_strategy)
def test_fastfst::ndelta3_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nDelta3_strategy)
def test_fastfst::ndelta3_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nShftTilt_strategy)
@settings(max_examples=50)
def test_fastfst::nshfttilt_instantiation(instance):
    assert isinstance(instance, fastfst::nShftTilt)

@given(instance=fastfst::nShftTilt_strategy)
def test_fastfst::nshfttilt_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nShftTilt_strategy)
def test_fastfst::nshfttilt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nShftTilt_strategy)
def test_fastfst::nshfttilt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nShftTilt_strategy)
def test_fastfst::nshfttilt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTwrRBHt_strategy)
@settings(max_examples=50)
def test_fastfst::ntwrrbht_instantiation(instance):
    assert isinstance(instance, fastfst::nTwrRBHt)

@given(instance=fastfst::nTwrRBHt_strategy)
def test_fastfst::ntwrrbht_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTwrRBHt_strategy)
def test_fastfst::ntwrrbht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTwrRBHt_strategy)
def test_fastfst::ntwrrbht_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTwrRBHt_strategy)
def test_fastfst::ntwrrbht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTwr2Shft_strategy)
@settings(max_examples=50)
def test_fastfst::ntwr2shft_instantiation(instance):
    assert isinstance(instance, fastfst::nTwr2Shft)

@given(instance=fastfst::nTwr2Shft_strategy)
def test_fastfst::ntwr2shft_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTwr2Shft_strategy)
def test_fastfst::ntwr2shft_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTwr2Shft_strategy)
def test_fastfst::ntwr2shft_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTwr2Shft_strategy)
def test_fastfst::ntwr2shft_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTowerHt_strategy)
@settings(max_examples=50)
def test_fastfst::ntowerht_instantiation(instance):
    assert isinstance(instance, fastfst::nTowerHt)

@given(instance=fastfst::nTowerHt_strategy)
def test_fastfst::ntowerht_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTowerHt_strategy)
def test_fastfst::ntowerht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTowerHt_strategy)
def test_fastfst::ntowerht_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTowerHt_strategy)
def test_fastfst::ntowerht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacCMzn_strategy)
@settings(max_examples=50)
def test_fastfst::nnaccmzn_instantiation(instance):
    assert isinstance(instance, fastfst::nNacCMzn)

@given(instance=fastfst::nNacCMzn_strategy)
def test_fastfst::nnaccmzn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacCMzn_strategy)
def test_fastfst::nnaccmzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacCMzn_strategy)
def test_fastfst::nnaccmzn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacCMzn_strategy)
def test_fastfst::nnaccmzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacCMyn_strategy)
@settings(max_examples=50)
def test_fastfst::nnaccmyn_instantiation(instance):
    assert isinstance(instance, fastfst::nNacCMyn)

@given(instance=fastfst::nNacCMyn_strategy)
def test_fastfst::nnaccmyn_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacCMyn_strategy)
def test_fastfst::nnaccmyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacCMyn_strategy)
def test_fastfst::nnaccmyn_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacCMyn_strategy)
def test_fastfst::nnaccmyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTTDspSS_strategy)
@settings(max_examples=50)
def test_fastfst::nttdspss_instantiation(instance):
    assert isinstance(instance, fastfst::nTTDspSS)

@given(instance=fastfst::nTTDspSS_strategy)
def test_fastfst::nttdspss_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTTDspSS_strategy)
def test_fastfst::nttdspss_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTDspSS_strategy)
def test_fastfst::nttdspss_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTTDspSS_strategy)
def test_fastfst::nttdspss_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTTDspFA_strategy)
@settings(max_examples=50)
def test_fastfst::nttdspfa_instantiation(instance):
    assert isinstance(instance, fastfst::nTTDspFA)

@given(instance=fastfst::nTTDspFA_strategy)
def test_fastfst::nttdspfa_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTTDspFA_strategy)
def test_fastfst::nttdspfa_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTDspFA_strategy)
def test_fastfst::nttdspfa_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTTDspFA_strategy)
def test_fastfst::nttdspfa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nNacYaw_strategy)
@settings(max_examples=50)
def test_fastfst::nnacyaw_instantiation(instance):
    assert isinstance(instance, fastfst::nNacYaw)

@given(instance=fastfst::nNacYaw_strategy)
def test_fastfst::nnacyaw_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacYaw_strategy)
def test_fastfst::nnacyaw_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacYaw_strategy)
def test_fastfst::nnacyaw_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacYaw_strategy)
def test_fastfst::nnacyaw_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nRotSpeed_strategy)
@settings(max_examples=50)
def test_fastfst::nrotspeed_instantiation(instance):
    assert isinstance(instance, fastfst::nRotSpeed)

@given(instance=fastfst::nRotSpeed_strategy)
def test_fastfst::nrotspeed_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nRotSpeed_strategy)
def test_fastfst::nrotspeed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nRotSpeed_strategy)
def test_fastfst::nrotspeed_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nRotSpeed_strategy)
def test_fastfst::nrotspeed_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nUndSling_strategy)
@settings(max_examples=50)
def test_fastfst::nundsling_instantiation(instance):
    assert isinstance(instance, fastfst::nUndSling)

@given(instance=fastfst::nUndSling_strategy)
def test_fastfst::nundsling_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nUndSling_strategy)
def test_fastfst::nundsling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nUndSling_strategy)
def test_fastfst::nundsling_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nUndSling_strategy)
def test_fastfst::nundsling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nPSpnElN_strategy)
@settings(max_examples=50)
def test_fastfst::npspneln_instantiation(instance):
    assert isinstance(instance, fastfst::nPSpnElN)

@given(instance=fastfst::nPSpnElN_strategy)
def test_fastfst::npspneln_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::nPSpnElN_strategy)
def test_fastfst::npspneln_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nPSpnElN_strategy)
def test_fastfst::npspneln_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nPSpnElN_strategy)
def test_fastfst::npspneln_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHubRad_strategy)
@settings(max_examples=50)
def test_fastfst::nhubrad_instantiation(instance):
    assert isinstance(instance, fastfst::nHubRad)

@given(instance=fastfst::nHubRad_strategy)
def test_fastfst::nhubrad_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nHubRad_strategy)
def test_fastfst::nhubrad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nHubRad_strategy)
def test_fastfst::nhubrad_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nHubRad_strategy)
def test_fastfst::nhubrad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTipRad_strategy)
@settings(max_examples=50)
def test_fastfst::ntiprad_instantiation(instance):
    assert isinstance(instance, fastfst::nTipRad)

@given(instance=fastfst::nTipRad_strategy)
def test_fastfst::ntiprad_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTipRad_strategy)
def test_fastfst::ntiprad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTipRad_strategy)
def test_fastfst::ntiprad_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTipRad_strategy)
def test_fastfst::ntiprad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTwFADOF1_strategy)
@settings(max_examples=50)
def test_fastfst::btwfadof1_instantiation(instance):
    assert isinstance(instance, fastfst::bTwFADOF1)

@given(instance=fastfst::bTwFADOF1_strategy)
def test_fastfst::btwfadof1_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTwFADOF1_strategy)
def test_fastfst::btwfadof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTwFADOF1_strategy)
def test_fastfst::btwfadof1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTwFADOF1_strategy)
def test_fastfst::btwfadof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bYawDOF_strategy)
@settings(max_examples=50)
def test_fastfst::byawdof_instantiation(instance):
    assert isinstance(instance, fastfst::bYawDOF)

@given(instance=fastfst::bYawDOF_strategy)
def test_fastfst::byawdof_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bYawDOF_strategy)
def test_fastfst::byawdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bYawDOF_strategy)
def test_fastfst::byawdof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bYawDOF_strategy)
def test_fastfst::byawdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bGenDOF_strategy)
@settings(max_examples=50)
def test_fastfst::bgendof_instantiation(instance):
    assert isinstance(instance, fastfst::bGenDOF)

@given(instance=fastfst::bGenDOF_strategy)
def test_fastfst::bgendof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bGenDOF_strategy)
def test_fastfst::bgendof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bGenDOF_strategy)
def test_fastfst::bgendof_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bGenDOF_strategy)
def test_fastfst::bgendof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bDrTrDOF_strategy)
@settings(max_examples=50)
def test_fastfst::bdrtrdof_instantiation(instance):
    assert isinstance(instance, fastfst::bDrTrDOF)

@given(instance=fastfst::bDrTrDOF_strategy)
def test_fastfst::bdrtrdof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bDrTrDOF_strategy)
def test_fastfst::bdrtrdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bDrTrDOF_strategy)
def test_fastfst::bdrtrdof_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bDrTrDOF_strategy)
def test_fastfst::bdrtrdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTeetDOF_strategy)
@settings(max_examples=50)
def test_fastfst::bteetdof_instantiation(instance):
    assert isinstance(instance, fastfst::bTeetDOF)

@given(instance=fastfst::bTeetDOF_strategy)
def test_fastfst::bteetdof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTeetDOF_strategy)
def test_fastfst::bteetdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTeetDOF_strategy)
def test_fastfst::bteetdof_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTeetDOF_strategy)
def test_fastfst::bteetdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bEdgeDOF_strategy)
@settings(max_examples=50)
def test_fastfst::bedgedof_instantiation(instance):
    assert isinstance(instance, fastfst::bEdgeDOF)

@given(instance=fastfst::bEdgeDOF_strategy)
def test_fastfst::bedgedof_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bEdgeDOF_strategy)
def test_fastfst::bedgedof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bEdgeDOF_strategy)
def test_fastfst::bedgedof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bEdgeDOF_strategy)
def test_fastfst::bedgedof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nAzimuth_strategy)
@settings(max_examples=50)
def test_fastfst::nazimuth_instantiation(instance):
    assert isinstance(instance, fastfst::nAzimuth)

@given(instance=fastfst::nAzimuth_strategy)
def test_fastfst::nazimuth_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nAzimuth_strategy)
def test_fastfst::nazimuth_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nAzimuth_strategy)
def test_fastfst::nazimuth_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nAzimuth_strategy)
def test_fastfst::nazimuth_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bFlapDOF2_strategy)
@settings(max_examples=50)
def test_fastfst::bflapdof2_instantiation(instance):
    assert isinstance(instance, fastfst::bFlapDOF2)

@given(instance=fastfst::bFlapDOF2_strategy)
def test_fastfst::bflapdof2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bFlapDOF2_strategy)
def test_fastfst::bflapdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bFlapDOF2_strategy)
def test_fastfst::bflapdof2_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bFlapDOF2_strategy)
def test_fastfst::bflapdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetDefl_strategy)
@settings(max_examples=50)
def test_fastfst::nteetdefl_instantiation(instance):
    assert isinstance(instance, fastfst::nTeetDefl)

@given(instance=fastfst::nTeetDefl_strategy)
def test_fastfst::nteetdefl_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTeetDefl_strategy)
def test_fastfst::nteetdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTeetDefl_strategy)
def test_fastfst::nteetdefl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTeetDefl_strategy)
def test_fastfst::nteetdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bFlapDOF1_strategy)
@settings(max_examples=50)
def test_fastfst::bflapdof1_instantiation(instance):
    assert isinstance(instance, fastfst::bFlapDOF1)

@given(instance=fastfst::bFlapDOF1_strategy)
def test_fastfst::bflapdof1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bFlapDOF1_strategy)
def test_fastfst::bflapdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bFlapDOF1_strategy)
def test_fastfst::bflapdof1_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bFlapDOF1_strategy)
def test_fastfst::bflapdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nIPDefl_strategy)
@settings(max_examples=50)
def test_fastfst::nipdefl_instantiation(instance):
    assert isinstance(instance, fastfst::nIPDefl)

@given(instance=fastfst::nIPDefl_strategy)
def test_fastfst::nipdefl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nIPDefl_strategy)
def test_fastfst::nipdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nIPDefl_strategy)
def test_fastfst::nipdefl_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nIPDefl_strategy)
def test_fastfst::nipdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGravity_strategy)
@settings(max_examples=50)
def test_fastfst::ngravity_instantiation(instance):
    assert isinstance(instance, fastfst::nGravity)

@given(instance=fastfst::nGravity_strategy)
def test_fastfst::ngravity_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nGravity_strategy)
def test_fastfst::ngravity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nGravity_strategy)
def test_fastfst::ngravity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nGravity_strategy)
def test_fastfst::ngravity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nOoPDefl_strategy)
@settings(max_examples=50)
def test_fastfst::noopdefl_instantiation(instance):
    assert isinstance(instance, fastfst::nOoPDefl)

@given(instance=fastfst::nOoPDefl_strategy)
def test_fastfst::noopdefl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nOoPDefl_strategy)
def test_fastfst::noopdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nOoPDefl_strategy)
def test_fastfst::noopdefl_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nOoPDefl_strategy)
def test_fastfst::noopdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitchF::3::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitchf::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitchF::3::)

@given(instance=fastfst::nBlPitchF::3::_strategy)
def test_fastfst::nblpitchf::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitchF::3::_strategy)
def test_fastfst::nblpitchf::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nBlPitchF::3::_strategy)
def test_fastfst::nblpitchf::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitchF::3::_strategy)
def test_fastfst::nblpitchf::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitchF::2::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitchf::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitchF::2::)

@given(instance=fastfst::nBlPitchF::2::_strategy)
def test_fastfst::nblpitchf::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitchF::2::_strategy)
def test_fastfst::nblpitchf::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nBlPitchF::2::_strategy)
def test_fastfst::nblpitchf::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitchF::2::_strategy)
def test_fastfst::nblpitchf::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bCompNoise_strategy)
@settings(max_examples=50)
def test_fastfst::bcompnoise_instantiation(instance):
    assert isinstance(instance, fastfst::bCompNoise)

@given(instance=fastfst::bCompNoise_strategy)
def test_fastfst::bcompnoise_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bCompNoise_strategy)
def test_fastfst::bcompnoise_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bCompNoise_strategy)
def test_fastfst::bcompnoise_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bCompNoise_strategy)
def test_fastfst::bcompnoise_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitchF::1::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitchf::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitchF::1::)

@given(instance=fastfst::nBlPitchF::1::_strategy)
def test_fastfst::nblpitchf::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitchF::1::_strategy)
def test_fastfst::nblpitchf::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitchF::1::_strategy)
def test_fastfst::nblpitchf::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitchF::1::_strategy)
def test_fastfst::nblpitchf::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bCompAero_strategy)
@settings(max_examples=50)
def test_fastfst::bcompaero_instantiation(instance):
    assert isinstance(instance, fastfst::bCompAero)

@given(instance=fastfst::bCompAero_strategy)
def test_fastfst::bcompaero_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bCompAero_strategy)
def test_fastfst::bcompaero_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bCompAero_strategy)
def test_fastfst::bcompaero_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bCompAero_strategy)
def test_fastfst::bcompaero_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitch::3::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitch::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitch::3::)

@given(instance=fastfst::nBlPitch::3::_strategy)
def test_fastfst::nblpitch::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitch::3::_strategy)
def test_fastfst::nblpitch::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitch::3::_strategy)
def test_fastfst::nblpitch::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitch::3::_strategy)
def test_fastfst::nblpitch::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTwSSDOF2_strategy)
@settings(max_examples=50)
def test_fastfst::btwssdof2_instantiation(instance):
    assert isinstance(instance, fastfst::bTwSSDOF2)

@given(instance=fastfst::bTwSSDOF2_strategy)
def test_fastfst::btwssdof2_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTwSSDOF2_strategy)
def test_fastfst::btwssdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTwSSDOF2_strategy)
def test_fastfst::btwssdof2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTwSSDOF2_strategy)
def test_fastfst::btwssdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nBlPitch::2::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitch::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitch::2::)

@given(instance=fastfst::nBlPitch::2::_strategy)
def test_fastfst::nblpitch::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitch::2::_strategy)
def test_fastfst::nblpitch::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitch::2::_strategy)
def test_fastfst::nblpitch::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitch::2::_strategy)
def test_fastfst::nblpitch::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTwSSDOF1_strategy)
@settings(max_examples=50)
def test_fastfst::btwssdof1_instantiation(instance):
    assert isinstance(instance, fastfst::bTwSSDOF1)

@given(instance=fastfst::bTwSSDOF1_strategy)
def test_fastfst::btwssdof1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTwSSDOF1_strategy)
def test_fastfst::btwssdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTwSSDOF1_strategy)
def test_fastfst::btwssdof1_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTwSSDOF1_strategy)
def test_fastfst::btwssdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bTwFADOF2_strategy)
@settings(max_examples=50)
def test_fastfst::btwfadof2_instantiation(instance):
    assert isinstance(instance, fastfst::bTwFADOF2)

@given(instance=fastfst::bTwFADOF2_strategy)
def test_fastfst::btwfadof2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bTwFADOF2_strategy)
def test_fastfst::btwfadof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bTwFADOF2_strategy)
def test_fastfst::btwfadof2_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bTwFADOF2_strategy)
def test_fastfst::btwfadof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManE::2::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmane::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManE::2::)

@given(instance=fastfst::nTPitManE::2::_strategy)
def test_fastfst::ntpitmane::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManE::2::_strategy)
def test_fastfst::ntpitmane::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManE::2::_strategy)
def test_fastfst::ntpitmane::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManE::2::_strategy)
def test_fastfst::ntpitmane::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManE::1::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmane::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManE::1::)

@given(instance=fastfst::nTPitManE::1::_strategy)
def test_fastfst::ntpitmane::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManE::1::_strategy)
def test_fastfst::ntpitmane::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManE::1::_strategy)
def test_fastfst::ntpitmane::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManE::1::_strategy)
def test_fastfst::ntpitmane::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManS::3::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmans::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManS::3::)

@given(instance=fastfst::nTPitManS::3::_strategy)
def test_fastfst::ntpitmans::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManS::3::_strategy)
def test_fastfst::ntpitmans::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManS::3::_strategy)
def test_fastfst::ntpitmans::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManS::3::_strategy)
def test_fastfst::ntpitmans::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManS::2::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmans::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManS::2::)

@given(instance=fastfst::nTPitManS::2::_strategy)
def test_fastfst::ntpitmans::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManS::2::_strategy)
def test_fastfst::ntpitmans::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManS::2::_strategy)
def test_fastfst::ntpitmans::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManS::2::_strategy)
def test_fastfst::ntpitmans::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManS::1::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmans::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManS::1::)

@given(instance=fastfst::nTPitManS::1::_strategy)
def test_fastfst::ntpitmans::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManS::1::_strategy)
def test_fastfst::ntpitmans::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManS::1::_strategy)
def test_fastfst::ntpitmans::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManS::1::_strategy)
def test_fastfst::ntpitmans::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacYawF_strategy)
@settings(max_examples=50)
def test_fastfst::nnacyawf_instantiation(instance):
    assert isinstance(instance, fastfst::nNacYawF)

@given(instance=fastfst::nNacYawF_strategy)
def test_fastfst::nnacyawf_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nNacYawF_strategy)
def test_fastfst::nnacyawf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nNacYawF_strategy)
def test_fastfst::nnacyawf_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nNacYawF_strategy)
def test_fastfst::nnacyawf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTYawManE_strategy)
@settings(max_examples=50)
def test_fastfst::ntyawmane_instantiation(instance):
    assert isinstance(instance, fastfst::nTYawManE)

@given(instance=fastfst::nTYawManE_strategy)
def test_fastfst::ntyawmane_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTYawManE_strategy)
def test_fastfst::ntyawmane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTYawManE_strategy)
def test_fastfst::ntyawmane_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTYawManE_strategy)
def test_fastfst::ntyawmane_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTYawManS_strategy)
@settings(max_examples=50)
def test_fastfst::ntyawmans_instantiation(instance):
    assert isinstance(instance, fastfst::nTYawManS)

@given(instance=fastfst::nTYawManS_strategy)
def test_fastfst::ntyawmans_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTYawManS_strategy)
def test_fastfst::ntyawmans_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTYawManS_strategy)
def test_fastfst::ntyawmans_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTYawManS_strategy)
def test_fastfst::ntyawmans_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDepISp::3::_strategy)
@settings(max_examples=50)
def test_fastfst::ntbdepisp::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nTBDepISp::3::)

@given(instance=fastfst::nTBDepISp::3::_strategy)
def test_fastfst::ntbdepisp::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTBDepISp::3::_strategy)
def test_fastfst::ntbdepisp::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDepISp::3::_strategy)
def test_fastfst::ntbdepisp::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTBDepISp::3::_strategy)
def test_fastfst::ntbdepisp::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTBDepISp::2::_strategy)
@settings(max_examples=50)
def test_fastfst::ntbdepisp::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nTBDepISp::2::)

@given(instance=fastfst::nTBDepISp::2::_strategy)
def test_fastfst::ntbdepisp::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTBDepISp::2::_strategy)
def test_fastfst::ntbdepisp::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDepISp::2::_strategy)
def test_fastfst::ntbdepisp::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTBDepISp::2::_strategy)
def test_fastfst::ntbdepisp::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTBDepISp::1::_strategy)
@settings(max_examples=50)
def test_fastfst::ntbdepisp::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nTBDepISp::1::)

@given(instance=fastfst::nTBDepISp::1::_strategy)
def test_fastfst::ntbdepisp::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTBDepISp::1::_strategy)
def test_fastfst::ntbdepisp::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTBDepISp::1::_strategy)
def test_fastfst::ntbdepisp::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTBDepISp::1::_strategy)
def test_fastfst::ntbdepisp::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTpBrDp::3::_strategy)
@settings(max_examples=50)
def test_fastfst::nttpbrdp::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nTTpBrDp::3::)

@given(instance=fastfst::nTTpBrDp::3::_strategy)
def test_fastfst::nttpbrdp::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTTpBrDp::3::_strategy)
def test_fastfst::nttpbrdp::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTTpBrDp::3::_strategy)
def test_fastfst::nttpbrdp::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTTpBrDp::3::_strategy)
def test_fastfst::nttpbrdp::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTpBrDp::2::_strategy)
@settings(max_examples=50)
def test_fastfst::nttpbrdp::2::_instantiation(instance):
    assert isinstance(instance, fastfst::nTTpBrDp::2::)

@given(instance=fastfst::nTTpBrDp::2::_strategy)
def test_fastfst::nttpbrdp::2::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTTpBrDp::2::_strategy)
def test_fastfst::nttpbrdp::2::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTpBrDp::2::_strategy)
def test_fastfst::nttpbrdp::2::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTTpBrDp::2::_strategy)
def test_fastfst::nttpbrdp::2::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTTpBrDp::1::_strategy)
@settings(max_examples=50)
def test_fastfst::nttpbrdp::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nTTpBrDp::1::)

@given(instance=fastfst::nTTpBrDp::1::_strategy)
def test_fastfst::nttpbrdp::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTTpBrDp::1::_strategy)
def test_fastfst::nttpbrdp::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTTpBrDp::1::_strategy)
def test_fastfst::nttpbrdp::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTTpBrDp::1::_strategy)
def test_fastfst::nttpbrdp::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nBlPitch::1::_strategy)
@settings(max_examples=50)
def test_fastfst::nblpitch::1::_instantiation(instance):
    assert isinstance(instance, fastfst::nBlPitch::1::)

@given(instance=fastfst::nBlPitch::1::_strategy)
def test_fastfst::nblpitch::1::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nBlPitch::1::_strategy)
def test_fastfst::nblpitch::1::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nBlPitch::1::_strategy)
def test_fastfst::nblpitch::1::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nBlPitch::1::_strategy)
def test_fastfst::nblpitch::1::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPitManE::3::_strategy)
@settings(max_examples=50)
def test_fastfst::ntpitmane::3::_instantiation(instance):
    assert isinstance(instance, fastfst::nTPitManE::3::)

@given(instance=fastfst::nTPitManE::3::_strategy)
def test_fastfst::ntpitmane::3::_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPitManE::3::_strategy)
def test_fastfst::ntpitmane::3::_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPitManE::3::_strategy)
def test_fastfst::ntpitmane::3::_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPitManE::3::_strategy)
def test_fastfst::ntpitmane::3::_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iHSSBrMode_strategy)
@settings(max_examples=50)
def test_fastfst::ihssbrmode_instantiation(instance):
    assert isinstance(instance, fastfst::iHSSBrMode)

@given(instance=fastfst::iHSSBrMode_strategy)
def test_fastfst::ihssbrmode_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iHSSBrMode_strategy)
def test_fastfst::ihssbrmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iHSSBrMode_strategy)
def test_fastfst::ihssbrmode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iHSSBrMode_strategy)
def test_fastfst::ihssbrmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTimGenOf_strategy)
@settings(max_examples=50)
def test_fastfst::ntimgenof_instantiation(instance):
    assert isinstance(instance, fastfst::nTimGenOf)

@given(instance=fastfst::nTimGenOf_strategy)
def test_fastfst::ntimgenof_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTimGenOf_strategy)
def test_fastfst::ntimgenof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTimGenOf_strategy)
def test_fastfst::ntimgenof_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTimGenOf_strategy)
def test_fastfst::ntimgenof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTimGenOn_strategy)
@settings(max_examples=50)
def test_fastfst::ntimgenon_instantiation(instance):
    assert isinstance(instance, fastfst::nTimGenOn)

@given(instance=fastfst::nTimGenOn_strategy)
def test_fastfst::ntimgenon_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTimGenOn_strategy)
def test_fastfst::ntimgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTimGenOn_strategy)
def test_fastfst::ntimgenon_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTimGenOn_strategy)
def test_fastfst::ntimgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nSpdGenOn_strategy)
@settings(max_examples=50)
def test_fastfst::nspdgenon_instantiation(instance):
    assert isinstance(instance, fastfst::nSpdGenOn)

@given(instance=fastfst::nSpdGenOn_strategy)
def test_fastfst::nspdgenon_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nSpdGenOn_strategy)
def test_fastfst::nspdgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nSpdGenOn_strategy)
def test_fastfst::nspdgenon_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nSpdGenOn_strategy)
def test_fastfst::nspdgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bGenTiStp_strategy)
@settings(max_examples=50)
def test_fastfst::bgentistp_instantiation(instance):
    assert isinstance(instance, fastfst::bGenTiStp)

@given(instance=fastfst::bGenTiStp_strategy)
def test_fastfst::bgentistp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bGenTiStp_strategy)
def test_fastfst::bgentistp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bGenTiStp_strategy)
def test_fastfst::bgentistp_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bGenTiStp_strategy)
def test_fastfst::bgentistp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bGenTiStr_strategy)
@settings(max_examples=50)
def test_fastfst::bgentistr_instantiation(instance):
    assert isinstance(instance, fastfst::bGenTiStr)

@given(instance=fastfst::bGenTiStr_strategy)
def test_fastfst::bgentistr_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bGenTiStr_strategy)
def test_fastfst::bgentistr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bGenTiStr_strategy)
def test_fastfst::bgentistr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bGenTiStr_strategy)
def test_fastfst::bgentistr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iGenModel_strategy)
@settings(max_examples=50)
def test_fastfst::igenmodel_instantiation(instance):
    assert isinstance(instance, fastfst::iGenModel)

@given(instance=fastfst::iGenModel_strategy)
def test_fastfst::igenmodel_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iGenModel_strategy)
def test_fastfst::igenmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iGenModel_strategy)
def test_fastfst::igenmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iGenModel_strategy)
def test_fastfst::igenmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nVS::SlPc_strategy)
@settings(max_examples=50)
def test_fastfst::nvs::slpc_instantiation(instance):
    assert isinstance(instance, fastfst::nVS::SlPc)

@given(instance=fastfst::nVS::SlPc_strategy)
def test_fastfst::nvs::slpc_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nVS::SlPc_strategy)
def test_fastfst::nvs::slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nVS::SlPc_strategy)
def test_fastfst::nvs::slpc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nVS::SlPc_strategy)
def test_fastfst::nvs::slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nVS::Rgn2K_strategy)
@settings(max_examples=50)
def test_fastfst::nvs::rgn2k_instantiation(instance):
    assert isinstance(instance, fastfst::nVS::Rgn2K)

@given(instance=fastfst::nVS::Rgn2K_strategy)
def test_fastfst::nvs::rgn2k_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nVS::Rgn2K_strategy)
def test_fastfst::nvs::rgn2k_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nVS::Rgn2K_strategy)
def test_fastfst::nvs::rgn2k_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nVS::Rgn2K_strategy)
def test_fastfst::nvs::rgn2k_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nVS::RtTq_strategy)
@settings(max_examples=50)
def test_fastfst::nvs::rttq_instantiation(instance):
    assert isinstance(instance, fastfst::nVS::RtTq)

@given(instance=fastfst::nVS::RtTq_strategy)
def test_fastfst::nvs::rttq_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nVS::RtTq_strategy)
def test_fastfst::nvs::rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nVS::RtTq_strategy)
def test_fastfst::nvs::rttq_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nVS::RtTq_strategy)
def test_fastfst::nvs::rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nVS::RtGnSp_strategy)
@settings(max_examples=50)
def test_fastfst::nvs::rtgnsp_instantiation(instance):
    assert isinstance(instance, fastfst::nVS::RtGnSp)

@given(instance=fastfst::nVS::RtGnSp_strategy)
def test_fastfst::nvs::rtgnsp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nVS::RtGnSp_strategy)
def test_fastfst::nvs::rtgnsp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nVS::RtGnSp_strategy)
def test_fastfst::nvs::rtgnsp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nVS::RtGnSp_strategy)
def test_fastfst::nvs::rtgnsp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iVSContrl_strategy)
@settings(max_examples=50)
def test_fastfst::ivscontrl_instantiation(instance):
    assert isinstance(instance, fastfst::iVSContrl)

@given(instance=fastfst::iVSContrl_strategy)
def test_fastfst::ivscontrl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iVSContrl_strategy)
def test_fastfst::ivscontrl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iVSContrl_strategy)
def test_fastfst::ivscontrl_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iVSContrl_strategy)
def test_fastfst::ivscontrl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTPCOn_strategy)
@settings(max_examples=50)
def test_fastfst::ntpcon_instantiation(instance):
    assert isinstance(instance, fastfst::nTPCOn)

@given(instance=fastfst::nTPCOn_strategy)
def test_fastfst::ntpcon_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTPCOn_strategy)
def test_fastfst::ntpcon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTPCOn_strategy)
def test_fastfst::ntpcon_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTPCOn_strategy)
def test_fastfst::ntpcon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iPCMode_strategy)
@settings(max_examples=50)
def test_fastfst::ipcmode_instantiation(instance):
    assert isinstance(instance, fastfst::iPCMode)

@given(instance=fastfst::iPCMode_strategy)
def test_fastfst::ipcmode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iPCMode_strategy)
def test_fastfst::ipcmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iPCMode_strategy)
def test_fastfst::ipcmode_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iPCMode_strategy)
def test_fastfst::ipcmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTYCOn_strategy)
@settings(max_examples=50)
def test_fastfst::ntycon_instantiation(instance):
    assert isinstance(instance, fastfst::nTYCOn)

@given(instance=fastfst::nTYCOn_strategy)
def test_fastfst::ntycon_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTYCOn_strategy)
def test_fastfst::ntycon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTYCOn_strategy)
def test_fastfst::ntycon_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTYCOn_strategy)
def test_fastfst::ntycon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iYCMode_strategy)
@settings(max_examples=50)
def test_fastfst::iycmode_instantiation(instance):
    assert isinstance(instance, fastfst::iYCMode)

@given(instance=fastfst::iYCMode_strategy)
def test_fastfst::iycmode_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iYCMode_strategy)
def test_fastfst::iycmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iYCMode_strategy)
def test_fastfst::iycmode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iYCMode_strategy)
def test_fastfst::iycmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nDT_strategy)
@settings(max_examples=50)
def test_fastfst::ndt_instantiation(instance):
    assert isinstance(instance, fastfst::nDT)

@given(instance=fastfst::nDT_strategy)
def test_fastfst::ndt_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nDT_strategy)
def test_fastfst::ndt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nDT_strategy)
def test_fastfst::ndt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nDT_strategy)
def test_fastfst::ndt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTMax_strategy)
@settings(max_examples=50)
def test_fastfst::ntmax_instantiation(instance):
    assert isinstance(instance, fastfst::nTMax)

@given(instance=fastfst::nTMax_strategy)
def test_fastfst::ntmax_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTMax_strategy)
def test_fastfst::ntmax_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTMax_strategy)
def test_fastfst::ntmax_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTMax_strategy)
def test_fastfst::ntmax_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTiDynBrk_strategy)
@settings(max_examples=50)
def test_fastfst::ntidynbrk_instantiation(instance):
    assert isinstance(instance, fastfst::nTiDynBrk)

@given(instance=fastfst::nTiDynBrk_strategy)
def test_fastfst::ntidynbrk_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTiDynBrk_strategy)
def test_fastfst::ntidynbrk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTiDynBrk_strategy)
def test_fastfst::ntidynbrk_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTiDynBrk_strategy)
def test_fastfst::ntidynbrk_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::nTHSSBrDp_strategy)
@settings(max_examples=50)
def test_fastfst::nthssbrdp_instantiation(instance):
    assert isinstance(instance, fastfst::nTHSSBrDp)

@given(instance=fastfst::nTHSSBrDp_strategy)
def test_fastfst::nthssbrdp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::nTHSSBrDp_strategy)
def test_fastfst::nthssbrdp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::nTHSSBrDp_strategy)
def test_fastfst::nthssbrdp_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=fastfst::nTHSSBrDp_strategy)
def test_fastfst::nthssbrdp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iADAMSPrep_strategy)
@settings(max_examples=50)
def test_fastfst::iadamsprep_instantiation(instance):
    assert isinstance(instance, fastfst::iADAMSPrep)

@given(instance=fastfst::iADAMSPrep_strategy)
def test_fastfst::iadamsprep_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iADAMSPrep_strategy)
def test_fastfst::iadamsprep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iADAMSPrep_strategy)
def test_fastfst::iadamsprep_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iADAMSPrep_strategy)
def test_fastfst::iadamsprep_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::bEcho_strategy)
@settings(max_examples=50)
def test_fastfst::becho_instantiation(instance):
    assert isinstance(instance, fastfst::bEcho)

@given(instance=fastfst::bEcho_strategy)
def test_fastfst::becho_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::bEcho_strategy)
def test_fastfst::becho_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::bEcho_strategy)
def test_fastfst::becho_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fastfst::bEcho_strategy)
def test_fastfst::becho_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::Section_strategy)
@settings(max_examples=50)
def test_fastfst::section_instantiation(instance):
    assert isinstance(instance, fastfst::Section)

@given(instance=fastfst::Section_strategy)
def test_fastfst::section_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::Section_strategy)
def test_fastfst::section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::Header_strategy)
@settings(max_examples=50)
def test_fastfst::header_instantiation(instance):
    assert isinstance(instance, fastfst::Header)

@given(instance=fastfst::Header_strategy)
def test_fastfst::header_rows_type(instance):
    assert isinstance(instance.rows, str)


@given(instance=fastfst::Header_strategy)
def test_fastfst::header_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=fastfst::ModelFastfst_strategy)
@settings(max_examples=50)
def test_fastfst::modelfastfst_instantiation(instance):
    assert isinstance(instance, fastfst::ModelFastfst)

@given(instance=fastfst::iNumBl_strategy)
@settings(max_examples=50)
def test_fastfst::inumbl_instantiation(instance):
    assert isinstance(instance, fastfst::iNumBl)

@given(instance=fastfst::iNumBl_strategy)
def test_fastfst::inumbl_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iNumBl_strategy)
def test_fastfst::inumbl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst::iNumBl_strategy)
def test_fastfst::inumbl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iNumBl_strategy)
def test_fastfst::inumbl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iAnalMode_strategy)
@settings(max_examples=50)
def test_fastfst::ianalmode_instantiation(instance):
    assert isinstance(instance, fastfst::iAnalMode)

@given(instance=fastfst::iAnalMode_strategy)
def test_fastfst::ianalmode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fastfst::iAnalMode_strategy)
def test_fastfst::ianalmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst::iAnalMode_strategy)
def test_fastfst::ianalmode_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fastfst::iAnalMode_strategy)
def test_fastfst::ianalmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fastfst_nShftGagL,
    fastfst_nNcIMUzn,
    fastfst_vOutList,
    fastfst_aBldGagNd,
    fastfst_iNBlGages,
    fastfst_aTwrGagNd,
    fastfst_iNTwGages,
    fastfst_sOutFmt,
    fastfst_bTabDelim,
    fastfst_nNcIMUyn,
    fastfst_nNcIMUxn,
    fastfst_nSttsTime,
    fastfst_iDecFact,
    fastfst_nTStart,
    fastfst_fBldFile_3_,
    fastfst_fBldFile_2_,
    fastfst_bOutFileFmt,
    fastfst_bSumPrint,
    fastfst_fLinFile,
    fastfst_fADAMSFile,
    fastfst_fNoiseFile,
    fastfst_fADFile,
    fastfst_nTeetHStP,
    fastfst_nTeetSStP,
    fastfst_fBldFile_1_,
    fastfst_nTpBrDT,
    fastfst_nTBDrConD,
    fastfst_nTBDrConN,
    fastfst_nTeetHSSp,
    fastfst_nTeetSSSp,
    fastfst_nYawNeut,
    fastfst_nYawDamp,
    fastfst_nTeetCDmp,
    fastfst_nTeetDmp,
    fastfst_nTeetDmpP,
    fastfst_iTeetMod,
    fastfst_fFurlFile,
    fastfst_nTEC_RLR,
    fastfst_bFurling,
    fastfst_nTEC_SLR,
    fastfst_nYawSpr,
    fastfst_fTwrFile,
    fastfst_iTwrNodes,
    fastfst_fPtfmFile,
    fastfst_iPtfmModel,
    fastfst_nTEC_MR,
    fastfst_nSIG_SlPc,
    fastfst_nDTTorDmp,
    fastfst_nTEC_VLL,
    fastfst_nTEC_Rres,
    fastfst_nTEC_Sres,
    fastfst_nTEC_Npol,
    fastfst_nTEC_Freq,
    fastfst_nSIG_PORt,
    fastfst_nSIG_RtTq,
    fastfst_nSIG_SySp,
    fastfst_nGenIner,
    fastfst_nDTTorSpr,
    fastfst_fDynBrkFi,
    fastfst_nTwr2Shft,
    fastfst_nTowerHt,
    fastfst_nNacCMzn,
    fastfst_nNacCMyn,
    fastfst_nTTDspSS,
    fastfst_nTTDspFA,
    fastfst_nNacYaw,
    fastfst_nRotSpeed,
    fastfst_nUndSling,
    fastfst_nPSpnElN,
    fastfst_nHubRad,
    fastfst_nTipRad,
    fastfst_bTwFADOF1,
    fastfst_bYawDOF,
    fastfst_bGenDOF,
    fastfst_bDrTrDOF,
    fastfst_bTeetDOF,
    fastfst_bEdgeDOF,
    fastfst_nAzimuth,
    fastfst_bFlapDOF2,
    fastfst_nTeetDefl,
    fastfst_bFlapDOF1,
    fastfst_nIPDefl,
    fastfst_nGravity,
    fastfst_nOoPDefl,
    fastfst_nBlPitchF_3_,
    fastfst_nBlPitchF_2_,
    fastfst_bCompNoise,
    fastfst_nBlPitchF_1_,
    fastfst_bCompAero,
    fastfst_nBlPitch_3_,
    fastfst_bTwSSDOF2,
    fastfst_nBlPitch_2_,
    fastfst_bTwSSDOF1,
    fastfst_bTwFADOF2,
    fastfst_nTPitManE_2_,
    fastfst_nTPitManE_1_,
    fastfst_nTPitManS_3_,
    fastfst_nTPitManS_2_,
    fastfst_nTPitManS_1_,
    fastfst_nNacYawF,
    fastfst_nTYawManE,
    fastfst_nTYawManS,
    fastfst_nTBDepISp_3_,
    fastfst_nTBDepISp_2_,
    fastfst_nTBDepISp_1_,
    fastfst_nTTpBrDp_3_,
    fastfst_nTTpBrDp_2_,
    fastfst_nTTpBrDp_1_,
    fastfst_nBlPitch_1_,
    fastfst_nTPitManE_3_,
    fastfst_iHSSBrMode,
    fastfst_nTimGenOf,
    fastfst_nTimGenOn,
    fastfst_nSpdGenOn,
    fastfst_bGenTiStp,
    fastfst_bGenTiStr,
    fastfst_iGenModel,
    fastfst_nVS_SlPc,
    fastfst_nVS_Rgn2K,
    fastfst_nVS_RtTq,
    fastfst_nVS_RtGnSp,
    fastfst_iVSContrl,
    fastfst_nTPCOn,
    fastfst_iPCMode,
    fastfst_nTYCOn,
    fastfst_iYCMode,
    fastfst_nDT,
    fastfst_nTMax,
    fastfst_nTiDynBrk,
    fastfst_nTHSSBrDp,
    fastfst_iADAMSPrep,
    fastfst_bEcho,
    fastfst_Section,
    fastfst_Header,
    fastfst_ModelFastfst,
    fastfst_iNumBl,
    fastfst_iAnalMode,
    fastfst_nHSSBrDT,
    fastfst_nHSSBrTqF,
    fastfst_bGBRevers,
    fastfst_nGBRatio,
    fastfst_nGenEff,
    fastfst_nGBoxEff,
    fastfst_nHubIner,
    fastfst_nPreCone_2_,
    fastfst_nNacYIner,
    fastfst_nTipMass_3_,
    fastfst_nTipMass_2_,
    fastfst_nTipMass_1_,
    fastfst_nHubMass,
    fastfst_nNacMass,
    fastfst_nYawBrMass,
    fastfst_nAzimB1Up,
    fastfst_nPreCone_3_,
    fastfst_nNacCMxn,
    fastfst_nOverHang,
    fastfst_nHubCM,
    fastfst_nPreCone_1_,
    fastfst_nDelta3,
    fastfst_nShftTilt,
    fastfst_nTwrRBHt,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fastfst_nshftgagl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nShftGagL)


def test_fastfst_nshftgagl_constructor_exists():
    assert callable(fastfst_nShftGagL.__init__)


def test_fastfst_nshftgagl_constructor_args():
    sig = inspect.signature(fastfst_nShftGagL.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nshftgagl_has_name():
    assert hasattr(fastfst_nShftGagL, "name")
    descriptor = None
    for klass in fastfst_nShftGagL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nshftgagl_has_value():
    assert hasattr(fastfst_nShftGagL, "value")
    descriptor = None
    for klass in fastfst_nShftGagL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nncimuzn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUzn)


def test_fastfst_nncimuzn_constructor_exists():
    assert callable(fastfst_nNcIMUzn.__init__)


def test_fastfst_nncimuzn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUzn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nncimuzn_has_value():
    assert hasattr(fastfst_nNcIMUzn, "value")
    descriptor = None
    for klass in fastfst_nNcIMUzn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nncimuzn_has_name():
    assert hasattr(fastfst_nNcIMUzn, "name")
    descriptor = None
    for klass in fastfst_nNcIMUzn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_voutlist_is_not_abstract():
    assert not inspect.isabstract(fastfst_vOutList)


def test_fastfst_voutlist_constructor_exists():
    assert callable(fastfst_vOutList.__init__)


def test_fastfst_voutlist_constructor_args():
    sig = inspect.signature(fastfst_vOutList.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_voutlist_has_value():
    assert hasattr(fastfst_vOutList, "value")
    descriptor = None
    for klass in fastfst_vOutList.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_voutlist_has_name():
    assert hasattr(fastfst_vOutList, "name")
    descriptor = None
    for klass in fastfst_vOutList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_abldgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst_aBldGagNd)


def test_fastfst_abldgagnd_constructor_exists():
    assert callable(fastfst_aBldGagNd.__init__)


def test_fastfst_abldgagnd_constructor_args():
    sig = inspect.signature(fastfst_aBldGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_abldgagnd_has_value():
    assert hasattr(fastfst_aBldGagNd, "value")
    descriptor = None
    for klass in fastfst_aBldGagNd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_abldgagnd_has_name():
    assert hasattr(fastfst_aBldGagNd, "name")
    descriptor = None
    for klass in fastfst_aBldGagNd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_inblgages_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNBlGages)


def test_fastfst_inblgages_constructor_exists():
    assert callable(fastfst_iNBlGages.__init__)


def test_fastfst_inblgages_constructor_args():
    sig = inspect.signature(fastfst_iNBlGages.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_inblgages_has_value():
    assert hasattr(fastfst_iNBlGages, "value")
    descriptor = None
    for klass in fastfst_iNBlGages.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_inblgages_has_name():
    assert hasattr(fastfst_iNBlGages, "name")
    descriptor = None
    for klass in fastfst_iNBlGages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_atwrgagnd_is_not_abstract():
    assert not inspect.isabstract(fastfst_aTwrGagNd)


def test_fastfst_atwrgagnd_constructor_exists():
    assert callable(fastfst_aTwrGagNd.__init__)


def test_fastfst_atwrgagnd_constructor_args():
    sig = inspect.signature(fastfst_aTwrGagNd.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_atwrgagnd_has_value():
    assert hasattr(fastfst_aTwrGagNd, "value")
    descriptor = None
    for klass in fastfst_aTwrGagNd.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_atwrgagnd_has_name():
    assert hasattr(fastfst_aTwrGagNd, "name")
    descriptor = None
    for klass in fastfst_aTwrGagNd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_intwgages_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNTwGages)


def test_fastfst_intwgages_constructor_exists():
    assert callable(fastfst_iNTwGages.__init__)


def test_fastfst_intwgages_constructor_args():
    sig = inspect.signature(fastfst_iNTwGages.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_intwgages_has_value():
    assert hasattr(fastfst_iNTwGages, "value")
    descriptor = None
    for klass in fastfst_iNTwGages.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_intwgages_has_name():
    assert hasattr(fastfst_iNTwGages, "name")
    descriptor = None
    for klass in fastfst_iNTwGages.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_soutfmt_is_not_abstract():
    assert not inspect.isabstract(fastfst_sOutFmt)


def test_fastfst_soutfmt_constructor_exists():
    assert callable(fastfst_sOutFmt.__init__)


def test_fastfst_soutfmt_constructor_args():
    sig = inspect.signature(fastfst_sOutFmt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_soutfmt_has_value():
    assert hasattr(fastfst_sOutFmt, "value")
    descriptor = None
    for klass in fastfst_sOutFmt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_soutfmt_has_name():
    assert hasattr(fastfst_sOutFmt, "name")
    descriptor = None
    for klass in fastfst_sOutFmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_btabdelim_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTabDelim)


def test_fastfst_btabdelim_constructor_exists():
    assert callable(fastfst_bTabDelim.__init__)


def test_fastfst_btabdelim_constructor_args():
    sig = inspect.signature(fastfst_bTabDelim.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_btabdelim_has_name():
    assert hasattr(fastfst_bTabDelim, "name")
    descriptor = None
    for klass in fastfst_bTabDelim.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_btabdelim_has_value():
    assert hasattr(fastfst_bTabDelim, "value")
    descriptor = None
    for klass in fastfst_bTabDelim.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nncimuyn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUyn)


def test_fastfst_nncimuyn_constructor_exists():
    assert callable(fastfst_nNcIMUyn.__init__)


def test_fastfst_nncimuyn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUyn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nncimuyn_has_name():
    assert hasattr(fastfst_nNcIMUyn, "name")
    descriptor = None
    for klass in fastfst_nNcIMUyn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nncimuyn_has_value():
    assert hasattr(fastfst_nNcIMUyn, "value")
    descriptor = None
    for klass in fastfst_nNcIMUyn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nncimuxn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNcIMUxn)


def test_fastfst_nncimuxn_constructor_exists():
    assert callable(fastfst_nNcIMUxn.__init__)


def test_fastfst_nncimuxn_constructor_args():
    sig = inspect.signature(fastfst_nNcIMUxn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nncimuxn_has_name():
    assert hasattr(fastfst_nNcIMUxn, "name")
    descriptor = None
    for klass in fastfst_nNcIMUxn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nncimuxn_has_value():
    assert hasattr(fastfst_nNcIMUxn, "value")
    descriptor = None
    for klass in fastfst_nNcIMUxn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nsttstime_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSttsTime)


def test_fastfst_nsttstime_constructor_exists():
    assert callable(fastfst_nSttsTime.__init__)


def test_fastfst_nsttstime_constructor_args():
    sig = inspect.signature(fastfst_nSttsTime.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nsttstime_has_name():
    assert hasattr(fastfst_nSttsTime, "name")
    descriptor = None
    for klass in fastfst_nSttsTime.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nsttstime_has_value():
    assert hasattr(fastfst_nSttsTime, "value")
    descriptor = None
    for klass in fastfst_nSttsTime.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_idecfact_is_not_abstract():
    assert not inspect.isabstract(fastfst_iDecFact)


def test_fastfst_idecfact_constructor_exists():
    assert callable(fastfst_iDecFact.__init__)


def test_fastfst_idecfact_constructor_args():
    sig = inspect.signature(fastfst_iDecFact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_idecfact_has_name():
    assert hasattr(fastfst_iDecFact, "name")
    descriptor = None
    for klass in fastfst_iDecFact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_idecfact_has_value():
    assert hasattr(fastfst_iDecFact, "value")
    descriptor = None
    for klass in fastfst_iDecFact.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntstart_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTStart)


def test_fastfst_ntstart_constructor_exists():
    assert callable(fastfst_nTStart.__init__)


def test_fastfst_ntstart_constructor_args():
    sig = inspect.signature(fastfst_nTStart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntstart_has_name():
    assert hasattr(fastfst_nTStart, "name")
    descriptor = None
    for klass in fastfst_nTStart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntstart_has_value():
    assert hasattr(fastfst_nTStart, "value")
    descriptor = None
    for klass in fastfst_nTStart.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fbldfile_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_3_)


def test_fastfst_fbldfile_3__constructor_exists():
    assert callable(fastfst_fBldFile_3_.__init__)


def test_fastfst_fbldfile_3__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fbldfile_3__has_value():
    assert hasattr(fastfst_fBldFile_3_, "value")
    descriptor = None
    for klass in fastfst_fBldFile_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fbldfile_3__has_name():
    assert hasattr(fastfst_fBldFile_3_, "name")
    descriptor = None
    for klass in fastfst_fBldFile_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fbldfile_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_2_)


def test_fastfst_fbldfile_2__constructor_exists():
    assert callable(fastfst_fBldFile_2_.__init__)


def test_fastfst_fbldfile_2__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fbldfile_2__has_value():
    assert hasattr(fastfst_fBldFile_2_, "value")
    descriptor = None
    for klass in fastfst_fBldFile_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fbldfile_2__has_name():
    assert hasattr(fastfst_fBldFile_2_, "name")
    descriptor = None
    for klass in fastfst_fBldFile_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_boutfilefmt_is_not_abstract():
    assert not inspect.isabstract(fastfst_bOutFileFmt)


def test_fastfst_boutfilefmt_constructor_exists():
    assert callable(fastfst_bOutFileFmt.__init__)


def test_fastfst_boutfilefmt_constructor_args():
    sig = inspect.signature(fastfst_bOutFileFmt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_boutfilefmt_has_value():
    assert hasattr(fastfst_bOutFileFmt, "value")
    descriptor = None
    for klass in fastfst_bOutFileFmt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_boutfilefmt_has_name():
    assert hasattr(fastfst_bOutFileFmt, "name")
    descriptor = None
    for klass in fastfst_bOutFileFmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bsumprint_is_not_abstract():
    assert not inspect.isabstract(fastfst_bSumPrint)


def test_fastfst_bsumprint_constructor_exists():
    assert callable(fastfst_bSumPrint.__init__)


def test_fastfst_bsumprint_constructor_args():
    sig = inspect.signature(fastfst_bSumPrint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bsumprint_has_name():
    assert hasattr(fastfst_bSumPrint, "name")
    descriptor = None
    for klass in fastfst_bSumPrint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bsumprint_has_value():
    assert hasattr(fastfst_bSumPrint, "value")
    descriptor = None
    for klass in fastfst_bSumPrint.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_flinfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fLinFile)


def test_fastfst_flinfile_constructor_exists():
    assert callable(fastfst_fLinFile.__init__)


def test_fastfst_flinfile_constructor_args():
    sig = inspect.signature(fastfst_fLinFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_flinfile_has_name():
    assert hasattr(fastfst_fLinFile, "name")
    descriptor = None
    for klass in fastfst_fLinFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_flinfile_has_value():
    assert hasattr(fastfst_fLinFile, "value")
    descriptor = None
    for klass in fastfst_fLinFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fadamsfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fADAMSFile)


def test_fastfst_fadamsfile_constructor_exists():
    assert callable(fastfst_fADAMSFile.__init__)


def test_fastfst_fadamsfile_constructor_args():
    sig = inspect.signature(fastfst_fADAMSFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fadamsfile_has_value():
    assert hasattr(fastfst_fADAMSFile, "value")
    descriptor = None
    for klass in fastfst_fADAMSFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fadamsfile_has_name():
    assert hasattr(fastfst_fADAMSFile, "name")
    descriptor = None
    for klass in fastfst_fADAMSFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fnoisefile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fNoiseFile)


def test_fastfst_fnoisefile_constructor_exists():
    assert callable(fastfst_fNoiseFile.__init__)


def test_fastfst_fnoisefile_constructor_args():
    sig = inspect.signature(fastfst_fNoiseFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fnoisefile_has_value():
    assert hasattr(fastfst_fNoiseFile, "value")
    descriptor = None
    for klass in fastfst_fNoiseFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fnoisefile_has_name():
    assert hasattr(fastfst_fNoiseFile, "name")
    descriptor = None
    for klass in fastfst_fNoiseFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fadfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fADFile)


def test_fastfst_fadfile_constructor_exists():
    assert callable(fastfst_fADFile.__init__)


def test_fastfst_fadfile_constructor_args():
    sig = inspect.signature(fastfst_fADFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fadfile_has_value():
    assert hasattr(fastfst_fADFile, "value")
    descriptor = None
    for klass in fastfst_fADFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fadfile_has_name():
    assert hasattr(fastfst_fADFile, "name")
    descriptor = None
    for klass in fastfst_fADFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteethstp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetHStP)


def test_fastfst_nteethstp_constructor_exists():
    assert callable(fastfst_nTeetHStP.__init__)


def test_fastfst_nteethstp_constructor_args():
    sig = inspect.signature(fastfst_nTeetHStP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nteethstp_has_value():
    assert hasattr(fastfst_nTeetHStP, "value")
    descriptor = None
    for klass in fastfst_nTeetHStP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteethstp_has_name():
    assert hasattr(fastfst_nTeetHStP, "name")
    descriptor = None
    for klass in fastfst_nTeetHStP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetsstp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetSStP)


def test_fastfst_nteetsstp_constructor_exists():
    assert callable(fastfst_nTeetSStP.__init__)


def test_fastfst_nteetsstp_constructor_args():
    sig = inspect.signature(fastfst_nTeetSStP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nteetsstp_has_name():
    assert hasattr(fastfst_nTeetSStP, "name")
    descriptor = None
    for klass in fastfst_nTeetSStP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetsstp_has_value():
    assert hasattr(fastfst_nTeetSStP, "value")
    descriptor = None
    for klass in fastfst_nTeetSStP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fbldfile_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_fBldFile_1_)


def test_fastfst_fbldfile_1__constructor_exists():
    assert callable(fastfst_fBldFile_1_.__init__)


def test_fastfst_fbldfile_1__constructor_args():
    sig = inspect.signature(fastfst_fBldFile_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_fbldfile_1__has_value():
    assert hasattr(fastfst_fBldFile_1_, "value")
    descriptor = None
    for klass in fastfst_fBldFile_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fbldfile_1__has_name():
    assert hasattr(fastfst_fBldFile_1_, "name")
    descriptor = None
    for klass in fastfst_fBldFile_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTpBrDT)


def test_fastfst_ntpbrdt_constructor_exists():
    assert callable(fastfst_nTpBrDT.__init__)


def test_fastfst_ntpbrdt_constructor_args():
    sig = inspect.signature(fastfst_nTpBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntpbrdt_has_value():
    assert hasattr(fastfst_nTpBrDT, "value")
    descriptor = None
    for klass in fastfst_nTpBrDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpbrdt_has_name():
    assert hasattr(fastfst_nTpBrDT, "name")
    descriptor = None
    for klass in fastfst_nTpBrDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntbdrcond_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDrConD)


def test_fastfst_ntbdrcond_constructor_exists():
    assert callable(fastfst_nTBDrConD.__init__)


def test_fastfst_ntbdrcond_constructor_args():
    sig = inspect.signature(fastfst_nTBDrConD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntbdrcond_has_name():
    assert hasattr(fastfst_nTBDrConD, "name")
    descriptor = None
    for klass in fastfst_nTBDrConD.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntbdrcond_has_value():
    assert hasattr(fastfst_nTBDrConD, "value")
    descriptor = None
    for klass in fastfst_nTBDrConD.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntbdrconn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDrConN)


def test_fastfst_ntbdrconn_constructor_exists():
    assert callable(fastfst_nTBDrConN.__init__)


def test_fastfst_ntbdrconn_constructor_args():
    sig = inspect.signature(fastfst_nTBDrConN.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntbdrconn_has_name():
    assert hasattr(fastfst_nTBDrConN, "name")
    descriptor = None
    for klass in fastfst_nTBDrConN.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntbdrconn_has_value():
    assert hasattr(fastfst_nTBDrConN, "value")
    descriptor = None
    for klass in fastfst_nTBDrConN.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteethssp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetHSSp)


def test_fastfst_nteethssp_constructor_exists():
    assert callable(fastfst_nTeetHSSp.__init__)


def test_fastfst_nteethssp_constructor_args():
    sig = inspect.signature(fastfst_nTeetHSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nteethssp_has_value():
    assert hasattr(fastfst_nTeetHSSp, "value")
    descriptor = None
    for klass in fastfst_nTeetHSSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteethssp_has_name():
    assert hasattr(fastfst_nTeetHSSp, "name")
    descriptor = None
    for klass in fastfst_nTeetHSSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetsssp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetSSSp)


def test_fastfst_nteetsssp_constructor_exists():
    assert callable(fastfst_nTeetSSSp.__init__)


def test_fastfst_nteetsssp_constructor_args():
    sig = inspect.signature(fastfst_nTeetSSSp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nteetsssp_has_value():
    assert hasattr(fastfst_nTeetSSSp, "value")
    descriptor = None
    for klass in fastfst_nTeetSSSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetsssp_has_name():
    assert hasattr(fastfst_nTeetSSSp, "name")
    descriptor = None
    for klass in fastfst_nTeetSSSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nyawneut_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawNeut)


def test_fastfst_nyawneut_constructor_exists():
    assert callable(fastfst_nYawNeut.__init__)


def test_fastfst_nyawneut_constructor_args():
    sig = inspect.signature(fastfst_nYawNeut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nyawneut_has_value():
    assert hasattr(fastfst_nYawNeut, "value")
    descriptor = None
    for klass in fastfst_nYawNeut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nyawneut_has_name():
    assert hasattr(fastfst_nYawNeut, "name")
    descriptor = None
    for klass in fastfst_nYawNeut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nyawdamp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawDamp)


def test_fastfst_nyawdamp_constructor_exists():
    assert callable(fastfst_nYawDamp.__init__)


def test_fastfst_nyawdamp_constructor_args():
    sig = inspect.signature(fastfst_nYawDamp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nyawdamp_has_name():
    assert hasattr(fastfst_nYawDamp, "name")
    descriptor = None
    for klass in fastfst_nYawDamp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nyawdamp_has_value():
    assert hasattr(fastfst_nYawDamp, "value")
    descriptor = None
    for klass in fastfst_nYawDamp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetcdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetCDmp)


def test_fastfst_nteetcdmp_constructor_exists():
    assert callable(fastfst_nTeetCDmp.__init__)


def test_fastfst_nteetcdmp_constructor_args():
    sig = inspect.signature(fastfst_nTeetCDmp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nteetcdmp_has_name():
    assert hasattr(fastfst_nTeetCDmp, "name")
    descriptor = None
    for klass in fastfst_nTeetCDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetcdmp_has_value():
    assert hasattr(fastfst_nTeetCDmp, "value")
    descriptor = None
    for klass in fastfst_nTeetCDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetdmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDmp)


def test_fastfst_nteetdmp_constructor_exists():
    assert callable(fastfst_nTeetDmp.__init__)


def test_fastfst_nteetdmp_constructor_args():
    sig = inspect.signature(fastfst_nTeetDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nteetdmp_has_value():
    assert hasattr(fastfst_nTeetDmp, "value")
    descriptor = None
    for klass in fastfst_nTeetDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetdmp_has_name():
    assert hasattr(fastfst_nTeetDmp, "name")
    descriptor = None
    for klass in fastfst_nTeetDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetdmpp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDmpP)


def test_fastfst_nteetdmpp_constructor_exists():
    assert callable(fastfst_nTeetDmpP.__init__)


def test_fastfst_nteetdmpp_constructor_args():
    sig = inspect.signature(fastfst_nTeetDmpP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nteetdmpp_has_name():
    assert hasattr(fastfst_nTeetDmpP, "name")
    descriptor = None
    for klass in fastfst_nTeetDmpP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetdmpp_has_value():
    assert hasattr(fastfst_nTeetDmpP, "value")
    descriptor = None
    for klass in fastfst_nTeetDmpP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_iteetmod_is_not_abstract():
    assert not inspect.isabstract(fastfst_iTeetMod)


def test_fastfst_iteetmod_constructor_exists():
    assert callable(fastfst_iTeetMod.__init__)


def test_fastfst_iteetmod_constructor_args():
    sig = inspect.signature(fastfst_iTeetMod.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_iteetmod_has_value():
    assert hasattr(fastfst_iTeetMod, "value")
    descriptor = None
    for klass in fastfst_iTeetMod.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_iteetmod_has_name():
    assert hasattr(fastfst_iTeetMod, "name")
    descriptor = None
    for klass in fastfst_iTeetMod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ffurlfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fFurlFile)


def test_fastfst_ffurlfile_constructor_exists():
    assert callable(fastfst_fFurlFile.__init__)


def test_fastfst_ffurlfile_constructor_args():
    sig = inspect.signature(fastfst_fFurlFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ffurlfile_has_name():
    assert hasattr(fastfst_fFurlFile, "name")
    descriptor = None
    for klass in fastfst_fFurlFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ffurlfile_has_value():
    assert hasattr(fastfst_fFurlFile, "value")
    descriptor = None
    for klass in fastfst_fFurlFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_rlr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_RLR)


def test_fastfst_ntec_rlr_constructor_exists():
    assert callable(fastfst_nTEC_RLR.__init__)


def test_fastfst_ntec_rlr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_RLR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_rlr_has_value():
    assert hasattr(fastfst_nTEC_RLR, "value")
    descriptor = None
    for klass in fastfst_nTEC_RLR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_rlr_has_name():
    assert hasattr(fastfst_nTEC_RLR, "name")
    descriptor = None
    for klass in fastfst_nTEC_RLR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bfurling_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFurling)


def test_fastfst_bfurling_constructor_exists():
    assert callable(fastfst_bFurling.__init__)


def test_fastfst_bfurling_constructor_args():
    sig = inspect.signature(fastfst_bFurling.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bfurling_has_name():
    assert hasattr(fastfst_bFurling, "name")
    descriptor = None
    for klass in fastfst_bFurling.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bfurling_has_value():
    assert hasattr(fastfst_bFurling, "value")
    descriptor = None
    for klass in fastfst_bFurling.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_slr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_SLR)


def test_fastfst_ntec_slr_constructor_exists():
    assert callable(fastfst_nTEC_SLR.__init__)


def test_fastfst_ntec_slr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_SLR.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntec_slr_has_name():
    assert hasattr(fastfst_nTEC_SLR, "name")
    descriptor = None
    for klass in fastfst_nTEC_SLR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_slr_has_value():
    assert hasattr(fastfst_nTEC_SLR, "value")
    descriptor = None
    for klass in fastfst_nTEC_SLR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nyawspr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawSpr)


def test_fastfst_nyawspr_constructor_exists():
    assert callable(fastfst_nYawSpr.__init__)


def test_fastfst_nyawspr_constructor_args():
    sig = inspect.signature(fastfst_nYawSpr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nyawspr_has_name():
    assert hasattr(fastfst_nYawSpr, "name")
    descriptor = None
    for klass in fastfst_nYawSpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nyawspr_has_value():
    assert hasattr(fastfst_nYawSpr, "value")
    descriptor = None
    for klass in fastfst_nYawSpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ftwrfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fTwrFile)


def test_fastfst_ftwrfile_constructor_exists():
    assert callable(fastfst_fTwrFile.__init__)


def test_fastfst_ftwrfile_constructor_args():
    sig = inspect.signature(fastfst_fTwrFile.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ftwrfile_has_value():
    assert hasattr(fastfst_fTwrFile, "value")
    descriptor = None
    for klass in fastfst_fTwrFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ftwrfile_has_name():
    assert hasattr(fastfst_fTwrFile, "name")
    descriptor = None
    for klass in fastfst_fTwrFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_itwrnodes_is_not_abstract():
    assert not inspect.isabstract(fastfst_iTwrNodes)


def test_fastfst_itwrnodes_constructor_exists():
    assert callable(fastfst_iTwrNodes.__init__)


def test_fastfst_itwrnodes_constructor_args():
    sig = inspect.signature(fastfst_iTwrNodes.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_itwrnodes_has_value():
    assert hasattr(fastfst_iTwrNodes, "value")
    descriptor = None
    for klass in fastfst_iTwrNodes.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_itwrnodes_has_name():
    assert hasattr(fastfst_iTwrNodes, "name")
    descriptor = None
    for klass in fastfst_iTwrNodes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fptfmfile_is_not_abstract():
    assert not inspect.isabstract(fastfst_fPtfmFile)


def test_fastfst_fptfmfile_constructor_exists():
    assert callable(fastfst_fPtfmFile.__init__)


def test_fastfst_fptfmfile_constructor_args():
    sig = inspect.signature(fastfst_fPtfmFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_fptfmfile_has_name():
    assert hasattr(fastfst_fPtfmFile, "name")
    descriptor = None
    for klass in fastfst_fPtfmFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fptfmfile_has_value():
    assert hasattr(fastfst_fPtfmFile, "value")
    descriptor = None
    for klass in fastfst_fPtfmFile.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_iptfmmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst_iPtfmModel)


def test_fastfst_iptfmmodel_constructor_exists():
    assert callable(fastfst_iPtfmModel.__init__)


def test_fastfst_iptfmmodel_constructor_args():
    sig = inspect.signature(fastfst_iPtfmModel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_iptfmmodel_has_value():
    assert hasattr(fastfst_iPtfmModel, "value")
    descriptor = None
    for klass in fastfst_iPtfmModel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_iptfmmodel_has_name():
    assert hasattr(fastfst_iPtfmModel, "name")
    descriptor = None
    for klass in fastfst_iPtfmModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_mr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_MR)


def test_fastfst_ntec_mr_constructor_exists():
    assert callable(fastfst_nTEC_MR.__init__)


def test_fastfst_ntec_mr_constructor_args():
    sig = inspect.signature(fastfst_nTEC_MR.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_mr_has_value():
    assert hasattr(fastfst_nTEC_MR, "value")
    descriptor = None
    for klass in fastfst_nTEC_MR.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_mr_has_name():
    assert hasattr(fastfst_nTEC_MR, "name")
    descriptor = None
    for klass in fastfst_nTEC_MR.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nsig_slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_SlPc)


def test_fastfst_nsig_slpc_constructor_exists():
    assert callable(fastfst_nSIG_SlPc.__init__)


def test_fastfst_nsig_slpc_constructor_args():
    sig = inspect.signature(fastfst_nSIG_SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nsig_slpc_has_value():
    assert hasattr(fastfst_nSIG_SlPc, "value")
    descriptor = None
    for klass in fastfst_nSIG_SlPc.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nsig_slpc_has_name():
    assert hasattr(fastfst_nSIG_SlPc, "name")
    descriptor = None
    for klass in fastfst_nSIG_SlPc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ndttordmp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDTTorDmp)


def test_fastfst_ndttordmp_constructor_exists():
    assert callable(fastfst_nDTTorDmp.__init__)


def test_fastfst_ndttordmp_constructor_args():
    sig = inspect.signature(fastfst_nDTTorDmp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ndttordmp_has_value():
    assert hasattr(fastfst_nDTTorDmp, "value")
    descriptor = None
    for klass in fastfst_nDTTorDmp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ndttordmp_has_name():
    assert hasattr(fastfst_nDTTorDmp, "name")
    descriptor = None
    for klass in fastfst_nDTTorDmp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_vll_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_VLL)


def test_fastfst_ntec_vll_constructor_exists():
    assert callable(fastfst_nTEC_VLL.__init__)


def test_fastfst_ntec_vll_constructor_args():
    sig = inspect.signature(fastfst_nTEC_VLL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_vll_has_value():
    assert hasattr(fastfst_nTEC_VLL, "value")
    descriptor = None
    for klass in fastfst_nTEC_VLL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_vll_has_name():
    assert hasattr(fastfst_nTEC_VLL, "name")
    descriptor = None
    for klass in fastfst_nTEC_VLL.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_rres_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Rres)


def test_fastfst_ntec_rres_constructor_exists():
    assert callable(fastfst_nTEC_Rres.__init__)


def test_fastfst_ntec_rres_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Rres.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_rres_has_value():
    assert hasattr(fastfst_nTEC_Rres, "value")
    descriptor = None
    for klass in fastfst_nTEC_Rres.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_rres_has_name():
    assert hasattr(fastfst_nTEC_Rres, "name")
    descriptor = None
    for klass in fastfst_nTEC_Rres.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_sres_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Sres)


def test_fastfst_ntec_sres_constructor_exists():
    assert callable(fastfst_nTEC_Sres.__init__)


def test_fastfst_ntec_sres_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Sres.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntec_sres_has_name():
    assert hasattr(fastfst_nTEC_Sres, "name")
    descriptor = None
    for klass in fastfst_nTEC_Sres.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_sres_has_value():
    assert hasattr(fastfst_nTEC_Sres, "value")
    descriptor = None
    for klass in fastfst_nTEC_Sres.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_npol_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Npol)


def test_fastfst_ntec_npol_constructor_exists():
    assert callable(fastfst_nTEC_Npol.__init__)


def test_fastfst_ntec_npol_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Npol.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_npol_has_value():
    assert hasattr(fastfst_nTEC_Npol, "value")
    descriptor = None
    for klass in fastfst_nTEC_Npol.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_npol_has_name():
    assert hasattr(fastfst_nTEC_Npol, "name")
    descriptor = None
    for klass in fastfst_nTEC_Npol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntec_freq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTEC_Freq)


def test_fastfst_ntec_freq_constructor_exists():
    assert callable(fastfst_nTEC_Freq.__init__)


def test_fastfst_ntec_freq_constructor_args():
    sig = inspect.signature(fastfst_nTEC_Freq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntec_freq_has_value():
    assert hasattr(fastfst_nTEC_Freq, "value")
    descriptor = None
    for klass in fastfst_nTEC_Freq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntec_freq_has_name():
    assert hasattr(fastfst_nTEC_Freq, "name")
    descriptor = None
    for klass in fastfst_nTEC_Freq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nsig_port_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_PORt)


def test_fastfst_nsig_port_constructor_exists():
    assert callable(fastfst_nSIG_PORt.__init__)


def test_fastfst_nsig_port_constructor_args():
    sig = inspect.signature(fastfst_nSIG_PORt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nsig_port_has_name():
    assert hasattr(fastfst_nSIG_PORt, "name")
    descriptor = None
    for klass in fastfst_nSIG_PORt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nsig_port_has_value():
    assert hasattr(fastfst_nSIG_PORt, "value")
    descriptor = None
    for klass in fastfst_nSIG_PORt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nsig_rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_RtTq)


def test_fastfst_nsig_rttq_constructor_exists():
    assert callable(fastfst_nSIG_RtTq.__init__)


def test_fastfst_nsig_rttq_constructor_args():
    sig = inspect.signature(fastfst_nSIG_RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nsig_rttq_has_name():
    assert hasattr(fastfst_nSIG_RtTq, "name")
    descriptor = None
    for klass in fastfst_nSIG_RtTq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nsig_rttq_has_value():
    assert hasattr(fastfst_nSIG_RtTq, "value")
    descriptor = None
    for klass in fastfst_nSIG_RtTq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nsig_sysp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSIG_SySp)


def test_fastfst_nsig_sysp_constructor_exists():
    assert callable(fastfst_nSIG_SySp.__init__)


def test_fastfst_nsig_sysp_constructor_args():
    sig = inspect.signature(fastfst_nSIG_SySp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nsig_sysp_has_name():
    assert hasattr(fastfst_nSIG_SySp, "name")
    descriptor = None
    for klass in fastfst_nSIG_SySp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nsig_sysp_has_value():
    assert hasattr(fastfst_nSIG_SySp, "value")
    descriptor = None
    for klass in fastfst_nSIG_SySp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ngeniner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGenIner)


def test_fastfst_ngeniner_constructor_exists():
    assert callable(fastfst_nGenIner.__init__)


def test_fastfst_ngeniner_constructor_args():
    sig = inspect.signature(fastfst_nGenIner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ngeniner_has_name():
    assert hasattr(fastfst_nGenIner, "name")
    descriptor = None
    for klass in fastfst_nGenIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ngeniner_has_value():
    assert hasattr(fastfst_nGenIner, "value")
    descriptor = None
    for klass in fastfst_nGenIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ndttorspr_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDTTorSpr)


def test_fastfst_ndttorspr_constructor_exists():
    assert callable(fastfst_nDTTorSpr.__init__)


def test_fastfst_ndttorspr_constructor_args():
    sig = inspect.signature(fastfst_nDTTorSpr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ndttorspr_has_value():
    assert hasattr(fastfst_nDTTorSpr, "value")
    descriptor = None
    for klass in fastfst_nDTTorSpr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ndttorspr_has_name():
    assert hasattr(fastfst_nDTTorSpr, "name")
    descriptor = None
    for klass in fastfst_nDTTorSpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_fdynbrkfi_is_not_abstract():
    assert not inspect.isabstract(fastfst_fDynBrkFi)


def test_fastfst_fdynbrkfi_constructor_exists():
    assert callable(fastfst_fDynBrkFi.__init__)


def test_fastfst_fdynbrkfi_constructor_args():
    sig = inspect.signature(fastfst_fDynBrkFi.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_fdynbrkfi_has_name():
    assert hasattr(fastfst_fDynBrkFi, "name")
    descriptor = None
    for klass in fastfst_fDynBrkFi.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_fdynbrkfi_has_value():
    assert hasattr(fastfst_fDynBrkFi, "value")
    descriptor = None
    for klass in fastfst_fDynBrkFi.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntwr2shft_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTwr2Shft)


def test_fastfst_ntwr2shft_constructor_exists():
    assert callable(fastfst_nTwr2Shft.__init__)


def test_fastfst_ntwr2shft_constructor_args():
    sig = inspect.signature(fastfst_nTwr2Shft.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntwr2shft_has_value():
    assert hasattr(fastfst_nTwr2Shft, "value")
    descriptor = None
    for klass in fastfst_nTwr2Shft.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntwr2shft_has_name():
    assert hasattr(fastfst_nTwr2Shft, "name")
    descriptor = None
    for klass in fastfst_nTwr2Shft.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntowerht_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTowerHt)


def test_fastfst_ntowerht_constructor_exists():
    assert callable(fastfst_nTowerHt.__init__)


def test_fastfst_ntowerht_constructor_args():
    sig = inspect.signature(fastfst_nTowerHt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntowerht_has_value():
    assert hasattr(fastfst_nTowerHt, "value")
    descriptor = None
    for klass in fastfst_nTowerHt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntowerht_has_name():
    assert hasattr(fastfst_nTowerHt, "name")
    descriptor = None
    for klass in fastfst_nTowerHt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnaccmzn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMzn)


def test_fastfst_nnaccmzn_constructor_exists():
    assert callable(fastfst_nNacCMzn.__init__)


def test_fastfst_nnaccmzn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMzn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nnaccmzn_has_name():
    assert hasattr(fastfst_nNacCMzn, "name")
    descriptor = None
    for klass in fastfst_nNacCMzn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnaccmzn_has_value():
    assert hasattr(fastfst_nNacCMzn, "value")
    descriptor = None
    for klass in fastfst_nNacCMzn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnaccmyn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMyn)


def test_fastfst_nnaccmyn_constructor_exists():
    assert callable(fastfst_nNacCMyn.__init__)


def test_fastfst_nnaccmyn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMyn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nnaccmyn_has_name():
    assert hasattr(fastfst_nNacCMyn, "name")
    descriptor = None
    for klass in fastfst_nNacCMyn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnaccmyn_has_value():
    assert hasattr(fastfst_nNacCMyn, "value")
    descriptor = None
    for klass in fastfst_nNacCMyn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nttdspss_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTDspSS)


def test_fastfst_nttdspss_constructor_exists():
    assert callable(fastfst_nTTDspSS.__init__)


def test_fastfst_nttdspss_constructor_args():
    sig = inspect.signature(fastfst_nTTDspSS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nttdspss_has_value():
    assert hasattr(fastfst_nTTDspSS, "value")
    descriptor = None
    for klass in fastfst_nTTDspSS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nttdspss_has_name():
    assert hasattr(fastfst_nTTDspSS, "name")
    descriptor = None
    for klass in fastfst_nTTDspSS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nttdspfa_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTDspFA)


def test_fastfst_nttdspfa_constructor_exists():
    assert callable(fastfst_nTTDspFA.__init__)


def test_fastfst_nttdspfa_constructor_args():
    sig = inspect.signature(fastfst_nTTDspFA.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nttdspfa_has_value():
    assert hasattr(fastfst_nTTDspFA, "value")
    descriptor = None
    for klass in fastfst_nTTDspFA.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nttdspfa_has_name():
    assert hasattr(fastfst_nTTDspFA, "name")
    descriptor = None
    for klass in fastfst_nTTDspFA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnacyaw_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYaw)


def test_fastfst_nnacyaw_constructor_exists():
    assert callable(fastfst_nNacYaw.__init__)


def test_fastfst_nnacyaw_constructor_args():
    sig = inspect.signature(fastfst_nNacYaw.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nnacyaw_has_name():
    assert hasattr(fastfst_nNacYaw, "name")
    descriptor = None
    for klass in fastfst_nNacYaw.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnacyaw_has_value():
    assert hasattr(fastfst_nNacYaw, "value")
    descriptor = None
    for klass in fastfst_nNacYaw.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nrotspeed_is_not_abstract():
    assert not inspect.isabstract(fastfst_nRotSpeed)


def test_fastfst_nrotspeed_constructor_exists():
    assert callable(fastfst_nRotSpeed.__init__)


def test_fastfst_nrotspeed_constructor_args():
    sig = inspect.signature(fastfst_nRotSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nrotspeed_has_value():
    assert hasattr(fastfst_nRotSpeed, "value")
    descriptor = None
    for klass in fastfst_nRotSpeed.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nrotspeed_has_name():
    assert hasattr(fastfst_nRotSpeed, "name")
    descriptor = None
    for klass in fastfst_nRotSpeed.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nundsling_is_not_abstract():
    assert not inspect.isabstract(fastfst_nUndSling)


def test_fastfst_nundsling_constructor_exists():
    assert callable(fastfst_nUndSling.__init__)


def test_fastfst_nundsling_constructor_args():
    sig = inspect.signature(fastfst_nUndSling.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nundsling_has_value():
    assert hasattr(fastfst_nUndSling, "value")
    descriptor = None
    for klass in fastfst_nUndSling.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nundsling_has_name():
    assert hasattr(fastfst_nUndSling, "name")
    descriptor = None
    for klass in fastfst_nUndSling.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_npspneln_is_not_abstract():
    assert not inspect.isabstract(fastfst_nPSpnElN)


def test_fastfst_npspneln_constructor_exists():
    assert callable(fastfst_nPSpnElN.__init__)


def test_fastfst_npspneln_constructor_args():
    sig = inspect.signature(fastfst_nPSpnElN.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_npspneln_has_name():
    assert hasattr(fastfst_nPSpnElN, "name")
    descriptor = None
    for klass in fastfst_nPSpnElN.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_npspneln_has_value():
    assert hasattr(fastfst_nPSpnElN, "value")
    descriptor = None
    for klass in fastfst_nPSpnElN.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhubrad_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubRad)


def test_fastfst_nhubrad_constructor_exists():
    assert callable(fastfst_nHubRad.__init__)


def test_fastfst_nhubrad_constructor_args():
    sig = inspect.signature(fastfst_nHubRad.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nhubrad_has_value():
    assert hasattr(fastfst_nHubRad, "value")
    descriptor = None
    for klass in fastfst_nHubRad.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhubrad_has_name():
    assert hasattr(fastfst_nHubRad, "name")
    descriptor = None
    for klass in fastfst_nHubRad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntiprad_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipRad)


def test_fastfst_ntiprad_constructor_exists():
    assert callable(fastfst_nTipRad.__init__)


def test_fastfst_ntiprad_constructor_args():
    sig = inspect.signature(fastfst_nTipRad.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntiprad_has_name():
    assert hasattr(fastfst_nTipRad, "name")
    descriptor = None
    for klass in fastfst_nTipRad.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntiprad_has_value():
    assert hasattr(fastfst_nTipRad, "value")
    descriptor = None
    for klass in fastfst_nTipRad.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_btwfadof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwFADOF1)


def test_fastfst_btwfadof1_constructor_exists():
    assert callable(fastfst_bTwFADOF1.__init__)


def test_fastfst_btwfadof1_constructor_args():
    sig = inspect.signature(fastfst_bTwFADOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_btwfadof1_has_name():
    assert hasattr(fastfst_bTwFADOF1, "name")
    descriptor = None
    for klass in fastfst_bTwFADOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_btwfadof1_has_value():
    assert hasattr(fastfst_bTwFADOF1, "value")
    descriptor = None
    for klass in fastfst_bTwFADOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_byawdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bYawDOF)


def test_fastfst_byawdof_constructor_exists():
    assert callable(fastfst_bYawDOF.__init__)


def test_fastfst_byawdof_constructor_args():
    sig = inspect.signature(fastfst_bYawDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_byawdof_has_name():
    assert hasattr(fastfst_bYawDOF, "name")
    descriptor = None
    for klass in fastfst_bYawDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_byawdof_has_value():
    assert hasattr(fastfst_bYawDOF, "value")
    descriptor = None
    for klass in fastfst_bYawDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bgendof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenDOF)


def test_fastfst_bgendof_constructor_exists():
    assert callable(fastfst_bGenDOF.__init__)


def test_fastfst_bgendof_constructor_args():
    sig = inspect.signature(fastfst_bGenDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bgendof_has_name():
    assert hasattr(fastfst_bGenDOF, "name")
    descriptor = None
    for klass in fastfst_bGenDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bgendof_has_value():
    assert hasattr(fastfst_bGenDOF, "value")
    descriptor = None
    for klass in fastfst_bGenDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bdrtrdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bDrTrDOF)


def test_fastfst_bdrtrdof_constructor_exists():
    assert callable(fastfst_bDrTrDOF.__init__)


def test_fastfst_bdrtrdof_constructor_args():
    sig = inspect.signature(fastfst_bDrTrDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_bdrtrdof_has_value():
    assert hasattr(fastfst_bDrTrDOF, "value")
    descriptor = None
    for klass in fastfst_bDrTrDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bdrtrdof_has_name():
    assert hasattr(fastfst_bDrTrDOF, "name")
    descriptor = None
    for klass in fastfst_bDrTrDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bteetdof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTeetDOF)


def test_fastfst_bteetdof_constructor_exists():
    assert callable(fastfst_bTeetDOF.__init__)


def test_fastfst_bteetdof_constructor_args():
    sig = inspect.signature(fastfst_bTeetDOF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bteetdof_has_name():
    assert hasattr(fastfst_bTeetDOF, "name")
    descriptor = None
    for klass in fastfst_bTeetDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bteetdof_has_value():
    assert hasattr(fastfst_bTeetDOF, "value")
    descriptor = None
    for klass in fastfst_bTeetDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bedgedof_is_not_abstract():
    assert not inspect.isabstract(fastfst_bEdgeDOF)


def test_fastfst_bedgedof_constructor_exists():
    assert callable(fastfst_bEdgeDOF.__init__)


def test_fastfst_bedgedof_constructor_args():
    sig = inspect.signature(fastfst_bEdgeDOF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_bedgedof_has_value():
    assert hasattr(fastfst_bEdgeDOF, "value")
    descriptor = None
    for klass in fastfst_bEdgeDOF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bedgedof_has_name():
    assert hasattr(fastfst_bEdgeDOF, "name")
    descriptor = None
    for klass in fastfst_bEdgeDOF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nazimuth_is_not_abstract():
    assert not inspect.isabstract(fastfst_nAzimuth)


def test_fastfst_nazimuth_constructor_exists():
    assert callable(fastfst_nAzimuth.__init__)


def test_fastfst_nazimuth_constructor_args():
    sig = inspect.signature(fastfst_nAzimuth.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nazimuth_has_value():
    assert hasattr(fastfst_nAzimuth, "value")
    descriptor = None
    for klass in fastfst_nAzimuth.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nazimuth_has_name():
    assert hasattr(fastfst_nAzimuth, "name")
    descriptor = None
    for klass in fastfst_nAzimuth.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bflapdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFlapDOF2)


def test_fastfst_bflapdof2_constructor_exists():
    assert callable(fastfst_bFlapDOF2.__init__)


def test_fastfst_bflapdof2_constructor_args():
    sig = inspect.signature(fastfst_bFlapDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bflapdof2_has_name():
    assert hasattr(fastfst_bFlapDOF2, "name")
    descriptor = None
    for klass in fastfst_bFlapDOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bflapdof2_has_value():
    assert hasattr(fastfst_bFlapDOF2, "value")
    descriptor = None
    for klass in fastfst_bFlapDOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nteetdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTeetDefl)


def test_fastfst_nteetdefl_constructor_exists():
    assert callable(fastfst_nTeetDefl.__init__)


def test_fastfst_nteetdefl_constructor_args():
    sig = inspect.signature(fastfst_nTeetDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nteetdefl_has_name():
    assert hasattr(fastfst_nTeetDefl, "name")
    descriptor = None
    for klass in fastfst_nTeetDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nteetdefl_has_value():
    assert hasattr(fastfst_nTeetDefl, "value")
    descriptor = None
    for klass in fastfst_nTeetDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bflapdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bFlapDOF1)


def test_fastfst_bflapdof1_constructor_exists():
    assert callable(fastfst_bFlapDOF1.__init__)


def test_fastfst_bflapdof1_constructor_args():
    sig = inspect.signature(fastfst_bFlapDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bflapdof1_has_name():
    assert hasattr(fastfst_bFlapDOF1, "name")
    descriptor = None
    for klass in fastfst_bFlapDOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bflapdof1_has_value():
    assert hasattr(fastfst_bFlapDOF1, "value")
    descriptor = None
    for klass in fastfst_bFlapDOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nipdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nIPDefl)


def test_fastfst_nipdefl_constructor_exists():
    assert callable(fastfst_nIPDefl.__init__)


def test_fastfst_nipdefl_constructor_args():
    sig = inspect.signature(fastfst_nIPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nipdefl_has_name():
    assert hasattr(fastfst_nIPDefl, "name")
    descriptor = None
    for klass in fastfst_nIPDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nipdefl_has_value():
    assert hasattr(fastfst_nIPDefl, "value")
    descriptor = None
    for klass in fastfst_nIPDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ngravity_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGravity)


def test_fastfst_ngravity_constructor_exists():
    assert callable(fastfst_nGravity.__init__)


def test_fastfst_ngravity_constructor_args():
    sig = inspect.signature(fastfst_nGravity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ngravity_has_value():
    assert hasattr(fastfst_nGravity, "value")
    descriptor = None
    for klass in fastfst_nGravity.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ngravity_has_name():
    assert hasattr(fastfst_nGravity, "name")
    descriptor = None
    for klass in fastfst_nGravity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_noopdefl_is_not_abstract():
    assert not inspect.isabstract(fastfst_nOoPDefl)


def test_fastfst_noopdefl_constructor_exists():
    assert callable(fastfst_nOoPDefl.__init__)


def test_fastfst_noopdefl_constructor_args():
    sig = inspect.signature(fastfst_nOoPDefl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_noopdefl_has_value():
    assert hasattr(fastfst_nOoPDefl, "value")
    descriptor = None
    for klass in fastfst_nOoPDefl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_noopdefl_has_name():
    assert hasattr(fastfst_nOoPDefl, "name")
    descriptor = None
    for klass in fastfst_nOoPDefl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitchf_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_3_)


def test_fastfst_nblpitchf_3__constructor_exists():
    assert callable(fastfst_nBlPitchF_3_.__init__)


def test_fastfst_nblpitchf_3__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nblpitchf_3__has_value():
    assert hasattr(fastfst_nBlPitchF_3_, "value")
    descriptor = None
    for klass in fastfst_nBlPitchF_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitchf_3__has_name():
    assert hasattr(fastfst_nBlPitchF_3_, "name")
    descriptor = None
    for klass in fastfst_nBlPitchF_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitchf_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_2_)


def test_fastfst_nblpitchf_2__constructor_exists():
    assert callable(fastfst_nBlPitchF_2_.__init__)


def test_fastfst_nblpitchf_2__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nblpitchf_2__has_value():
    assert hasattr(fastfst_nBlPitchF_2_, "value")
    descriptor = None
    for klass in fastfst_nBlPitchF_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitchf_2__has_name():
    assert hasattr(fastfst_nBlPitchF_2_, "name")
    descriptor = None
    for klass in fastfst_nBlPitchF_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bcompnoise_is_not_abstract():
    assert not inspect.isabstract(fastfst_bCompNoise)


def test_fastfst_bcompnoise_constructor_exists():
    assert callable(fastfst_bCompNoise.__init__)


def test_fastfst_bcompnoise_constructor_args():
    sig = inspect.signature(fastfst_bCompNoise.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_bcompnoise_has_value():
    assert hasattr(fastfst_bCompNoise, "value")
    descriptor = None
    for klass in fastfst_bCompNoise.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bcompnoise_has_name():
    assert hasattr(fastfst_bCompNoise, "name")
    descriptor = None
    for klass in fastfst_bCompNoise.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitchf_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitchF_1_)


def test_fastfst_nblpitchf_1__constructor_exists():
    assert callable(fastfst_nBlPitchF_1_.__init__)


def test_fastfst_nblpitchf_1__constructor_args():
    sig = inspect.signature(fastfst_nBlPitchF_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nblpitchf_1__has_value():
    assert hasattr(fastfst_nBlPitchF_1_, "value")
    descriptor = None
    for klass in fastfst_nBlPitchF_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitchf_1__has_name():
    assert hasattr(fastfst_nBlPitchF_1_, "name")
    descriptor = None
    for klass in fastfst_nBlPitchF_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bcompaero_is_not_abstract():
    assert not inspect.isabstract(fastfst_bCompAero)


def test_fastfst_bcompaero_constructor_exists():
    assert callable(fastfst_bCompAero.__init__)


def test_fastfst_bcompaero_constructor_args():
    sig = inspect.signature(fastfst_bCompAero.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bcompaero_has_name():
    assert hasattr(fastfst_bCompAero, "name")
    descriptor = None
    for klass in fastfst_bCompAero.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bcompaero_has_value():
    assert hasattr(fastfst_bCompAero, "value")
    descriptor = None
    for klass in fastfst_bCompAero.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitch_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_3_)


def test_fastfst_nblpitch_3__constructor_exists():
    assert callable(fastfst_nBlPitch_3_.__init__)


def test_fastfst_nblpitch_3__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nblpitch_3__has_name():
    assert hasattr(fastfst_nBlPitch_3_, "name")
    descriptor = None
    for klass in fastfst_nBlPitch_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitch_3__has_value():
    assert hasattr(fastfst_nBlPitch_3_, "value")
    descriptor = None
    for klass in fastfst_nBlPitch_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_btwssdof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwSSDOF2)


def test_fastfst_btwssdof2_constructor_exists():
    assert callable(fastfst_bTwSSDOF2.__init__)


def test_fastfst_btwssdof2_constructor_args():
    sig = inspect.signature(fastfst_bTwSSDOF2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_btwssdof2_has_value():
    assert hasattr(fastfst_bTwSSDOF2, "value")
    descriptor = None
    for klass in fastfst_bTwSSDOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_btwssdof2_has_name():
    assert hasattr(fastfst_bTwSSDOF2, "name")
    descriptor = None
    for klass in fastfst_bTwSSDOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitch_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_2_)


def test_fastfst_nblpitch_2__constructor_exists():
    assert callable(fastfst_nBlPitch_2_.__init__)


def test_fastfst_nblpitch_2__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nblpitch_2__has_value():
    assert hasattr(fastfst_nBlPitch_2_, "value")
    descriptor = None
    for klass in fastfst_nBlPitch_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitch_2__has_name():
    assert hasattr(fastfst_nBlPitch_2_, "name")
    descriptor = None
    for klass in fastfst_nBlPitch_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_btwssdof1_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwSSDOF1)


def test_fastfst_btwssdof1_constructor_exists():
    assert callable(fastfst_bTwSSDOF1.__init__)


def test_fastfst_btwssdof1_constructor_args():
    sig = inspect.signature(fastfst_bTwSSDOF1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_btwssdof1_has_name():
    assert hasattr(fastfst_bTwSSDOF1, "name")
    descriptor = None
    for klass in fastfst_bTwSSDOF1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_btwssdof1_has_value():
    assert hasattr(fastfst_bTwSSDOF1, "value")
    descriptor = None
    for klass in fastfst_bTwSSDOF1.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_btwfadof2_is_not_abstract():
    assert not inspect.isabstract(fastfst_bTwFADOF2)


def test_fastfst_btwfadof2_constructor_exists():
    assert callable(fastfst_bTwFADOF2.__init__)


def test_fastfst_btwfadof2_constructor_args():
    sig = inspect.signature(fastfst_bTwFADOF2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_btwfadof2_has_value():
    assert hasattr(fastfst_bTwFADOF2, "value")
    descriptor = None
    for klass in fastfst_bTwFADOF2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_btwfadof2_has_name():
    assert hasattr(fastfst_bTwFADOF2, "name")
    descriptor = None
    for klass in fastfst_bTwFADOF2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmane_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_2_)


def test_fastfst_ntpitmane_2__constructor_exists():
    assert callable(fastfst_nTPitManE_2_.__init__)


def test_fastfst_ntpitmane_2__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntpitmane_2__has_value():
    assert hasattr(fastfst_nTPitManE_2_, "value")
    descriptor = None
    for klass in fastfst_nTPitManE_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmane_2__has_name():
    assert hasattr(fastfst_nTPitManE_2_, "name")
    descriptor = None
    for klass in fastfst_nTPitManE_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmane_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_1_)


def test_fastfst_ntpitmane_1__constructor_exists():
    assert callable(fastfst_nTPitManE_1_.__init__)


def test_fastfst_ntpitmane_1__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntpitmane_1__has_name():
    assert hasattr(fastfst_nTPitManE_1_, "name")
    descriptor = None
    for klass in fastfst_nTPitManE_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmane_1__has_value():
    assert hasattr(fastfst_nTPitManE_1_, "value")
    descriptor = None
    for klass in fastfst_nTPitManE_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmans_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_3_)


def test_fastfst_ntpitmans_3__constructor_exists():
    assert callable(fastfst_nTPitManS_3_.__init__)


def test_fastfst_ntpitmans_3__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntpitmans_3__has_name():
    assert hasattr(fastfst_nTPitManS_3_, "name")
    descriptor = None
    for klass in fastfst_nTPitManS_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmans_3__has_value():
    assert hasattr(fastfst_nTPitManS_3_, "value")
    descriptor = None
    for klass in fastfst_nTPitManS_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmans_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_2_)


def test_fastfst_ntpitmans_2__constructor_exists():
    assert callable(fastfst_nTPitManS_2_.__init__)


def test_fastfst_ntpitmans_2__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntpitmans_2__has_value():
    assert hasattr(fastfst_nTPitManS_2_, "value")
    descriptor = None
    for klass in fastfst_nTPitManS_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmans_2__has_name():
    assert hasattr(fastfst_nTPitManS_2_, "name")
    descriptor = None
    for klass in fastfst_nTPitManS_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmans_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManS_1_)


def test_fastfst_ntpitmans_1__constructor_exists():
    assert callable(fastfst_nTPitManS_1_.__init__)


def test_fastfst_ntpitmans_1__constructor_args():
    sig = inspect.signature(fastfst_nTPitManS_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntpitmans_1__has_value():
    assert hasattr(fastfst_nTPitManS_1_, "value")
    descriptor = None
    for klass in fastfst_nTPitManS_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmans_1__has_name():
    assert hasattr(fastfst_nTPitManS_1_, "name")
    descriptor = None
    for klass in fastfst_nTPitManS_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnacyawf_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYawF)


def test_fastfst_nnacyawf_constructor_exists():
    assert callable(fastfst_nNacYawF.__init__)


def test_fastfst_nnacyawf_constructor_args():
    sig = inspect.signature(fastfst_nNacYawF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nnacyawf_has_name():
    assert hasattr(fastfst_nNacYawF, "name")
    descriptor = None
    for klass in fastfst_nNacYawF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnacyawf_has_value():
    assert hasattr(fastfst_nNacYawF, "value")
    descriptor = None
    for klass in fastfst_nNacYawF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntyawmane_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYawManE)


def test_fastfst_ntyawmane_constructor_exists():
    assert callable(fastfst_nTYawManE.__init__)


def test_fastfst_ntyawmane_constructor_args():
    sig = inspect.signature(fastfst_nTYawManE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntyawmane_has_name():
    assert hasattr(fastfst_nTYawManE, "name")
    descriptor = None
    for klass in fastfst_nTYawManE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntyawmane_has_value():
    assert hasattr(fastfst_nTYawManE, "value")
    descriptor = None
    for klass in fastfst_nTYawManE.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntyawmans_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYawManS)


def test_fastfst_ntyawmans_constructor_exists():
    assert callable(fastfst_nTYawManS.__init__)


def test_fastfst_ntyawmans_constructor_args():
    sig = inspect.signature(fastfst_nTYawManS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntyawmans_has_value():
    assert hasattr(fastfst_nTYawManS, "value")
    descriptor = None
    for klass in fastfst_nTYawManS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntyawmans_has_name():
    assert hasattr(fastfst_nTYawManS, "name")
    descriptor = None
    for klass in fastfst_nTYawManS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntbdepisp_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_3_)


def test_fastfst_ntbdepisp_3__constructor_exists():
    assert callable(fastfst_nTBDepISp_3_.__init__)


def test_fastfst_ntbdepisp_3__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntbdepisp_3__has_value():
    assert hasattr(fastfst_nTBDepISp_3_, "value")
    descriptor = None
    for klass in fastfst_nTBDepISp_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntbdepisp_3__has_name():
    assert hasattr(fastfst_nTBDepISp_3_, "name")
    descriptor = None
    for klass in fastfst_nTBDepISp_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntbdepisp_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_2_)


def test_fastfst_ntbdepisp_2__constructor_exists():
    assert callable(fastfst_nTBDepISp_2_.__init__)


def test_fastfst_ntbdepisp_2__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_2_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntbdepisp_2__has_name():
    assert hasattr(fastfst_nTBDepISp_2_, "name")
    descriptor = None
    for klass in fastfst_nTBDepISp_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntbdepisp_2__has_value():
    assert hasattr(fastfst_nTBDepISp_2_, "value")
    descriptor = None
    for klass in fastfst_nTBDepISp_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntbdepisp_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTBDepISp_1_)


def test_fastfst_ntbdepisp_1__constructor_exists():
    assert callable(fastfst_nTBDepISp_1_.__init__)


def test_fastfst_ntbdepisp_1__constructor_args():
    sig = inspect.signature(fastfst_nTBDepISp_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntbdepisp_1__has_name():
    assert hasattr(fastfst_nTBDepISp_1_, "name")
    descriptor = None
    for klass in fastfst_nTBDepISp_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntbdepisp_1__has_value():
    assert hasattr(fastfst_nTBDepISp_1_, "value")
    descriptor = None
    for klass in fastfst_nTBDepISp_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nttpbrdp_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_3_)


def test_fastfst_nttpbrdp_3__constructor_exists():
    assert callable(fastfst_nTTpBrDp_3_.__init__)


def test_fastfst_nttpbrdp_3__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nttpbrdp_3__has_name():
    assert hasattr(fastfst_nTTpBrDp_3_, "name")
    descriptor = None
    for klass in fastfst_nTTpBrDp_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nttpbrdp_3__has_value():
    assert hasattr(fastfst_nTTpBrDp_3_, "value")
    descriptor = None
    for klass in fastfst_nTTpBrDp_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nttpbrdp_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_2_)


def test_fastfst_nttpbrdp_2__constructor_exists():
    assert callable(fastfst_nTTpBrDp_2_.__init__)


def test_fastfst_nttpbrdp_2__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nttpbrdp_2__has_value():
    assert hasattr(fastfst_nTTpBrDp_2_, "value")
    descriptor = None
    for klass in fastfst_nTTpBrDp_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nttpbrdp_2__has_name():
    assert hasattr(fastfst_nTTpBrDp_2_, "name")
    descriptor = None
    for klass in fastfst_nTTpBrDp_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nttpbrdp_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTTpBrDp_1_)


def test_fastfst_nttpbrdp_1__constructor_exists():
    assert callable(fastfst_nTTpBrDp_1_.__init__)


def test_fastfst_nttpbrdp_1__constructor_args():
    sig = inspect.signature(fastfst_nTTpBrDp_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nttpbrdp_1__has_name():
    assert hasattr(fastfst_nTTpBrDp_1_, "name")
    descriptor = None
    for klass in fastfst_nTTpBrDp_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nttpbrdp_1__has_value():
    assert hasattr(fastfst_nTTpBrDp_1_, "value")
    descriptor = None
    for klass in fastfst_nTTpBrDp_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nblpitch_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nBlPitch_1_)


def test_fastfst_nblpitch_1__constructor_exists():
    assert callable(fastfst_nBlPitch_1_.__init__)


def test_fastfst_nblpitch_1__constructor_args():
    sig = inspect.signature(fastfst_nBlPitch_1_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nblpitch_1__has_value():
    assert hasattr(fastfst_nBlPitch_1_, "value")
    descriptor = None
    for klass in fastfst_nBlPitch_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nblpitch_1__has_name():
    assert hasattr(fastfst_nBlPitch_1_, "name")
    descriptor = None
    for klass in fastfst_nBlPitch_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpitmane_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPitManE_3_)


def test_fastfst_ntpitmane_3__constructor_exists():
    assert callable(fastfst_nTPitManE_3_.__init__)


def test_fastfst_ntpitmane_3__constructor_args():
    sig = inspect.signature(fastfst_nTPitManE_3_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntpitmane_3__has_name():
    assert hasattr(fastfst_nTPitManE_3_, "name")
    descriptor = None
    for klass in fastfst_nTPitManE_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpitmane_3__has_value():
    assert hasattr(fastfst_nTPitManE_3_, "value")
    descriptor = None
    for klass in fastfst_nTPitManE_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ihssbrmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iHSSBrMode)


def test_fastfst_ihssbrmode_constructor_exists():
    assert callable(fastfst_iHSSBrMode.__init__)


def test_fastfst_ihssbrmode_constructor_args():
    sig = inspect.signature(fastfst_iHSSBrMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ihssbrmode_has_name():
    assert hasattr(fastfst_iHSSBrMode, "name")
    descriptor = None
    for klass in fastfst_iHSSBrMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ihssbrmode_has_value():
    assert hasattr(fastfst_iHSSBrMode, "value")
    descriptor = None
    for klass in fastfst_iHSSBrMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntimgenof_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTimGenOf)


def test_fastfst_ntimgenof_constructor_exists():
    assert callable(fastfst_nTimGenOf.__init__)


def test_fastfst_ntimgenof_constructor_args():
    sig = inspect.signature(fastfst_nTimGenOf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntimgenof_has_name():
    assert hasattr(fastfst_nTimGenOf, "name")
    descriptor = None
    for klass in fastfst_nTimGenOf.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntimgenof_has_value():
    assert hasattr(fastfst_nTimGenOf, "value")
    descriptor = None
    for klass in fastfst_nTimGenOf.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntimgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTimGenOn)


def test_fastfst_ntimgenon_constructor_exists():
    assert callable(fastfst_nTimGenOn.__init__)


def test_fastfst_ntimgenon_constructor_args():
    sig = inspect.signature(fastfst_nTimGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntimgenon_has_name():
    assert hasattr(fastfst_nTimGenOn, "name")
    descriptor = None
    for klass in fastfst_nTimGenOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntimgenon_has_value():
    assert hasattr(fastfst_nTimGenOn, "value")
    descriptor = None
    for klass in fastfst_nTimGenOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nspdgenon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nSpdGenOn)


def test_fastfst_nspdgenon_constructor_exists():
    assert callable(fastfst_nSpdGenOn.__init__)


def test_fastfst_nspdgenon_constructor_args():
    sig = inspect.signature(fastfst_nSpdGenOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nspdgenon_has_value():
    assert hasattr(fastfst_nSpdGenOn, "value")
    descriptor = None
    for klass in fastfst_nSpdGenOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nspdgenon_has_name():
    assert hasattr(fastfst_nSpdGenOn, "name")
    descriptor = None
    for klass in fastfst_nSpdGenOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bgentistp_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenTiStp)


def test_fastfst_bgentistp_constructor_exists():
    assert callable(fastfst_bGenTiStp.__init__)


def test_fastfst_bgentistp_constructor_args():
    sig = inspect.signature(fastfst_bGenTiStp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bgentistp_has_name():
    assert hasattr(fastfst_bGenTiStp, "name")
    descriptor = None
    for klass in fastfst_bGenTiStp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bgentistp_has_value():
    assert hasattr(fastfst_bGenTiStp, "value")
    descriptor = None
    for klass in fastfst_bGenTiStp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bgentistr_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGenTiStr)


def test_fastfst_bgentistr_constructor_exists():
    assert callable(fastfst_bGenTiStr.__init__)


def test_fastfst_bgentistr_constructor_args():
    sig = inspect.signature(fastfst_bGenTiStr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bgentistr_has_name():
    assert hasattr(fastfst_bGenTiStr, "name")
    descriptor = None
    for klass in fastfst_bGenTiStr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bgentistr_has_value():
    assert hasattr(fastfst_bGenTiStr, "value")
    descriptor = None
    for klass in fastfst_bGenTiStr.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_igenmodel_is_not_abstract():
    assert not inspect.isabstract(fastfst_iGenModel)


def test_fastfst_igenmodel_constructor_exists():
    assert callable(fastfst_iGenModel.__init__)


def test_fastfst_igenmodel_constructor_args():
    sig = inspect.signature(fastfst_iGenModel.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_igenmodel_has_value():
    assert hasattr(fastfst_iGenModel, "value")
    descriptor = None
    for klass in fastfst_iGenModel.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_igenmodel_has_name():
    assert hasattr(fastfst_iGenModel, "name")
    descriptor = None
    for klass in fastfst_iGenModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nvs_slpc_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_SlPc)


def test_fastfst_nvs_slpc_constructor_exists():
    assert callable(fastfst_nVS_SlPc.__init__)


def test_fastfst_nvs_slpc_constructor_args():
    sig = inspect.signature(fastfst_nVS_SlPc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nvs_slpc_has_name():
    assert hasattr(fastfst_nVS_SlPc, "name")
    descriptor = None
    for klass in fastfst_nVS_SlPc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nvs_slpc_has_value():
    assert hasattr(fastfst_nVS_SlPc, "value")
    descriptor = None
    for klass in fastfst_nVS_SlPc.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nvs_rgn2k_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_Rgn2K)


def test_fastfst_nvs_rgn2k_constructor_exists():
    assert callable(fastfst_nVS_Rgn2K.__init__)


def test_fastfst_nvs_rgn2k_constructor_args():
    sig = inspect.signature(fastfst_nVS_Rgn2K.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nvs_rgn2k_has_name():
    assert hasattr(fastfst_nVS_Rgn2K, "name")
    descriptor = None
    for klass in fastfst_nVS_Rgn2K.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nvs_rgn2k_has_value():
    assert hasattr(fastfst_nVS_Rgn2K, "value")
    descriptor = None
    for klass in fastfst_nVS_Rgn2K.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nvs_rttq_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_RtTq)


def test_fastfst_nvs_rttq_constructor_exists():
    assert callable(fastfst_nVS_RtTq.__init__)


def test_fastfst_nvs_rttq_constructor_args():
    sig = inspect.signature(fastfst_nVS_RtTq.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nvs_rttq_has_value():
    assert hasattr(fastfst_nVS_RtTq, "value")
    descriptor = None
    for klass in fastfst_nVS_RtTq.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nvs_rttq_has_name():
    assert hasattr(fastfst_nVS_RtTq, "name")
    descriptor = None
    for klass in fastfst_nVS_RtTq.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nvs_rtgnsp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nVS_RtGnSp)


def test_fastfst_nvs_rtgnsp_constructor_exists():
    assert callable(fastfst_nVS_RtGnSp.__init__)


def test_fastfst_nvs_rtgnsp_constructor_args():
    sig = inspect.signature(fastfst_nVS_RtGnSp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nvs_rtgnsp_has_name():
    assert hasattr(fastfst_nVS_RtGnSp, "name")
    descriptor = None
    for klass in fastfst_nVS_RtGnSp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nvs_rtgnsp_has_value():
    assert hasattr(fastfst_nVS_RtGnSp, "value")
    descriptor = None
    for klass in fastfst_nVS_RtGnSp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ivscontrl_is_not_abstract():
    assert not inspect.isabstract(fastfst_iVSContrl)


def test_fastfst_ivscontrl_constructor_exists():
    assert callable(fastfst_iVSContrl.__init__)


def test_fastfst_ivscontrl_constructor_args():
    sig = inspect.signature(fastfst_iVSContrl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ivscontrl_has_value():
    assert hasattr(fastfst_iVSContrl, "value")
    descriptor = None
    for klass in fastfst_iVSContrl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ivscontrl_has_name():
    assert hasattr(fastfst_iVSContrl, "name")
    descriptor = None
    for klass in fastfst_iVSContrl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntpcon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTPCOn)


def test_fastfst_ntpcon_constructor_exists():
    assert callable(fastfst_nTPCOn.__init__)


def test_fastfst_ntpcon_constructor_args():
    sig = inspect.signature(fastfst_nTPCOn.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntpcon_has_name():
    assert hasattr(fastfst_nTPCOn, "name")
    descriptor = None
    for klass in fastfst_nTPCOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntpcon_has_value():
    assert hasattr(fastfst_nTPCOn, "value")
    descriptor = None
    for klass in fastfst_nTPCOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ipcmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iPCMode)


def test_fastfst_ipcmode_constructor_exists():
    assert callable(fastfst_iPCMode.__init__)


def test_fastfst_ipcmode_constructor_args():
    sig = inspect.signature(fastfst_iPCMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ipcmode_has_name():
    assert hasattr(fastfst_iPCMode, "name")
    descriptor = None
    for klass in fastfst_iPCMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ipcmode_has_value():
    assert hasattr(fastfst_iPCMode, "value")
    descriptor = None
    for klass in fastfst_iPCMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntycon_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTYCOn)


def test_fastfst_ntycon_constructor_exists():
    assert callable(fastfst_nTYCOn.__init__)


def test_fastfst_ntycon_constructor_args():
    sig = inspect.signature(fastfst_nTYCOn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntycon_has_value():
    assert hasattr(fastfst_nTYCOn, "value")
    descriptor = None
    for klass in fastfst_nTYCOn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntycon_has_name():
    assert hasattr(fastfst_nTYCOn, "name")
    descriptor = None
    for klass in fastfst_nTYCOn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_iycmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iYCMode)


def test_fastfst_iycmode_constructor_exists():
    assert callable(fastfst_iYCMode.__init__)


def test_fastfst_iycmode_constructor_args():
    sig = inspect.signature(fastfst_iYCMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_iycmode_has_name():
    assert hasattr(fastfst_iYCMode, "name")
    descriptor = None
    for klass in fastfst_iYCMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_iycmode_has_value():
    assert hasattr(fastfst_iYCMode, "value")
    descriptor = None
    for klass in fastfst_iYCMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ndt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDT)


def test_fastfst_ndt_constructor_exists():
    assert callable(fastfst_nDT.__init__)


def test_fastfst_ndt_constructor_args():
    sig = inspect.signature(fastfst_nDT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ndt_has_value():
    assert hasattr(fastfst_nDT, "value")
    descriptor = None
    for klass in fastfst_nDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ndt_has_name():
    assert hasattr(fastfst_nDT, "name")
    descriptor = None
    for klass in fastfst_nDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntmax_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTMax)


def test_fastfst_ntmax_constructor_exists():
    assert callable(fastfst_nTMax.__init__)


def test_fastfst_ntmax_constructor_args():
    sig = inspect.signature(fastfst_nTMax.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntmax_has_name():
    assert hasattr(fastfst_nTMax, "name")
    descriptor = None
    for klass in fastfst_nTMax.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntmax_has_value():
    assert hasattr(fastfst_nTMax, "value")
    descriptor = None
    for klass in fastfst_nTMax.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntidynbrk_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTiDynBrk)


def test_fastfst_ntidynbrk_constructor_exists():
    assert callable(fastfst_nTiDynBrk.__init__)


def test_fastfst_ntidynbrk_constructor_args():
    sig = inspect.signature(fastfst_nTiDynBrk.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntidynbrk_has_value():
    assert hasattr(fastfst_nTiDynBrk, "value")
    descriptor = None
    for klass in fastfst_nTiDynBrk.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntidynbrk_has_name():
    assert hasattr(fastfst_nTiDynBrk, "name")
    descriptor = None
    for klass in fastfst_nTiDynBrk.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nthssbrdp_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTHSSBrDp)


def test_fastfst_nthssbrdp_constructor_exists():
    assert callable(fastfst_nTHSSBrDp.__init__)


def test_fastfst_nthssbrdp_constructor_args():
    sig = inspect.signature(fastfst_nTHSSBrDp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nthssbrdp_has_value():
    assert hasattr(fastfst_nTHSSBrDp, "value")
    descriptor = None
    for klass in fastfst_nTHSSBrDp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nthssbrdp_has_name():
    assert hasattr(fastfst_nTHSSBrDp, "name")
    descriptor = None
    for klass in fastfst_nTHSSBrDp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_iadamsprep_is_not_abstract():
    assert not inspect.isabstract(fastfst_iADAMSPrep)


def test_fastfst_iadamsprep_constructor_exists():
    assert callable(fastfst_iADAMSPrep.__init__)


def test_fastfst_iadamsprep_constructor_args():
    sig = inspect.signature(fastfst_iADAMSPrep.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_iadamsprep_has_name():
    assert hasattr(fastfst_iADAMSPrep, "name")
    descriptor = None
    for klass in fastfst_iADAMSPrep.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_iadamsprep_has_value():
    assert hasattr(fastfst_iADAMSPrep, "value")
    descriptor = None
    for klass in fastfst_iADAMSPrep.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_becho_is_not_abstract():
    assert not inspect.isabstract(fastfst_bEcho)


def test_fastfst_becho_constructor_exists():
    assert callable(fastfst_bEcho.__init__)


def test_fastfst_becho_constructor_args():
    sig = inspect.signature(fastfst_bEcho.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_becho_has_name():
    assert hasattr(fastfst_bEcho, "name")
    descriptor = None
    for klass in fastfst_bEcho.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_becho_has_value():
    assert hasattr(fastfst_bEcho, "value")
    descriptor = None
    for klass in fastfst_bEcho.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_section_is_not_abstract():
    assert not inspect.isabstract(fastfst_Section)


def test_fastfst_section_constructor_exists():
    assert callable(fastfst_Section.__init__)


def test_fastfst_section_constructor_args():
    sig = inspect.signature(fastfst_Section.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_section_has_name():
    assert hasattr(fastfst_Section, "name")
    descriptor = None
    for klass in fastfst_Section.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_header_is_not_abstract():
    assert not inspect.isabstract(fastfst_Header)


def test_fastfst_header_constructor_exists():
    assert callable(fastfst_Header.__init__)


def test_fastfst_header_constructor_args():
    sig = inspect.signature(fastfst_Header.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"

def test_fastfst_header_has_rows():
    assert hasattr(fastfst_Header, "rows")
    descriptor = None
    for klass in fastfst_Header.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_modelfastfst_is_not_abstract():
    assert not inspect.isabstract(fastfst_ModelFastfst)


def test_fastfst_modelfastfst_constructor_exists():
    assert callable(fastfst_ModelFastfst.__init__)


def test_fastfst_modelfastfst_constructor_args():
    sig = inspect.signature(fastfst_ModelFastfst.__init__)
    params = list(sig.parameters.keys())



def test_fastfst_inumbl_is_not_abstract():
    assert not inspect.isabstract(fastfst_iNumBl)


def test_fastfst_inumbl_constructor_exists():
    assert callable(fastfst_iNumBl.__init__)


def test_fastfst_inumbl_constructor_args():
    sig = inspect.signature(fastfst_iNumBl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_inumbl_has_name():
    assert hasattr(fastfst_iNumBl, "name")
    descriptor = None
    for klass in fastfst_iNumBl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_inumbl_has_value():
    assert hasattr(fastfst_iNumBl, "value")
    descriptor = None
    for klass in fastfst_iNumBl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ianalmode_is_not_abstract():
    assert not inspect.isabstract(fastfst_iAnalMode)


def test_fastfst_ianalmode_constructor_exists():
    assert callable(fastfst_iAnalMode.__init__)


def test_fastfst_ianalmode_constructor_args():
    sig = inspect.signature(fastfst_iAnalMode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ianalmode_has_name():
    assert hasattr(fastfst_iAnalMode, "name")
    descriptor = None
    for klass in fastfst_iAnalMode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ianalmode_has_value():
    assert hasattr(fastfst_iAnalMode, "value")
    descriptor = None
    for klass in fastfst_iAnalMode.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhssbrdt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHSSBrDT)


def test_fastfst_nhssbrdt_constructor_exists():
    assert callable(fastfst_nHSSBrDT.__init__)


def test_fastfst_nhssbrdt_constructor_args():
    sig = inspect.signature(fastfst_nHSSBrDT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nhssbrdt_has_name():
    assert hasattr(fastfst_nHSSBrDT, "name")
    descriptor = None
    for klass in fastfst_nHSSBrDT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhssbrdt_has_value():
    assert hasattr(fastfst_nHSSBrDT, "value")
    descriptor = None
    for klass in fastfst_nHSSBrDT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhssbrtqf_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHSSBrTqF)


def test_fastfst_nhssbrtqf_constructor_exists():
    assert callable(fastfst_nHSSBrTqF.__init__)


def test_fastfst_nhssbrtqf_constructor_args():
    sig = inspect.signature(fastfst_nHSSBrTqF.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nhssbrtqf_has_name():
    assert hasattr(fastfst_nHSSBrTqF, "name")
    descriptor = None
    for klass in fastfst_nHSSBrTqF.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhssbrtqf_has_value():
    assert hasattr(fastfst_nHSSBrTqF, "value")
    descriptor = None
    for klass in fastfst_nHSSBrTqF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_bgbrevers_is_not_abstract():
    assert not inspect.isabstract(fastfst_bGBRevers)


def test_fastfst_bgbrevers_constructor_exists():
    assert callable(fastfst_bGBRevers.__init__)


def test_fastfst_bgbrevers_constructor_args():
    sig = inspect.signature(fastfst_bGBRevers.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_bgbrevers_has_name():
    assert hasattr(fastfst_bGBRevers, "name")
    descriptor = None
    for klass in fastfst_bGBRevers.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_bgbrevers_has_value():
    assert hasattr(fastfst_bGBRevers, "value")
    descriptor = None
    for klass in fastfst_bGBRevers.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ngbratio_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGBRatio)


def test_fastfst_ngbratio_constructor_exists():
    assert callable(fastfst_nGBRatio.__init__)


def test_fastfst_ngbratio_constructor_args():
    sig = inspect.signature(fastfst_nGBRatio.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ngbratio_has_value():
    assert hasattr(fastfst_nGBRatio, "value")
    descriptor = None
    for klass in fastfst_nGBRatio.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ngbratio_has_name():
    assert hasattr(fastfst_nGBRatio, "name")
    descriptor = None
    for klass in fastfst_nGBRatio.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ngeneff_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGenEff)


def test_fastfst_ngeneff_constructor_exists():
    assert callable(fastfst_nGenEff.__init__)


def test_fastfst_ngeneff_constructor_args():
    sig = inspect.signature(fastfst_nGenEff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ngeneff_has_name():
    assert hasattr(fastfst_nGenEff, "name")
    descriptor = None
    for klass in fastfst_nGenEff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ngeneff_has_value():
    assert hasattr(fastfst_nGenEff, "value")
    descriptor = None
    for klass in fastfst_nGenEff.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ngboxeff_is_not_abstract():
    assert not inspect.isabstract(fastfst_nGBoxEff)


def test_fastfst_ngboxeff_constructor_exists():
    assert callable(fastfst_nGBoxEff.__init__)


def test_fastfst_ngboxeff_constructor_args():
    sig = inspect.signature(fastfst_nGBoxEff.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ngboxeff_has_value():
    assert hasattr(fastfst_nGBoxEff, "value")
    descriptor = None
    for klass in fastfst_nGBoxEff.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ngboxeff_has_name():
    assert hasattr(fastfst_nGBoxEff, "name")
    descriptor = None
    for klass in fastfst_nGBoxEff.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhubiner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubIner)


def test_fastfst_nhubiner_constructor_exists():
    assert callable(fastfst_nHubIner.__init__)


def test_fastfst_nhubiner_constructor_args():
    sig = inspect.signature(fastfst_nHubIner.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nhubiner_has_value():
    assert hasattr(fastfst_nHubIner, "value")
    descriptor = None
    for klass in fastfst_nHubIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhubiner_has_name():
    assert hasattr(fastfst_nHubIner, "name")
    descriptor = None
    for klass in fastfst_nHubIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nprecone_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_2_)


def test_fastfst_nprecone_2__constructor_exists():
    assert callable(fastfst_nPreCone_2_.__init__)


def test_fastfst_nprecone_2__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_2_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nprecone_2__has_value():
    assert hasattr(fastfst_nPreCone_2_, "value")
    descriptor = None
    for klass in fastfst_nPreCone_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nprecone_2__has_name():
    assert hasattr(fastfst_nPreCone_2_, "name")
    descriptor = None
    for klass in fastfst_nPreCone_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnacyiner_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacYIner)


def test_fastfst_nnacyiner_constructor_exists():
    assert callable(fastfst_nNacYIner.__init__)


def test_fastfst_nnacyiner_constructor_args():
    sig = inspect.signature(fastfst_nNacYIner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nnacyiner_has_name():
    assert hasattr(fastfst_nNacYIner, "name")
    descriptor = None
    for klass in fastfst_nNacYIner.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnacyiner_has_value():
    assert hasattr(fastfst_nNacYIner, "value")
    descriptor = None
    for klass in fastfst_nNacYIner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntipmass_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_3_)


def test_fastfst_ntipmass_3__constructor_exists():
    assert callable(fastfst_nTipMass_3_.__init__)


def test_fastfst_ntipmass_3__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_ntipmass_3__has_value():
    assert hasattr(fastfst_nTipMass_3_, "value")
    descriptor = None
    for klass in fastfst_nTipMass_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntipmass_3__has_name():
    assert hasattr(fastfst_nTipMass_3_, "name")
    descriptor = None
    for klass in fastfst_nTipMass_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntipmass_2__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_2_)


def test_fastfst_ntipmass_2__constructor_exists():
    assert callable(fastfst_nTipMass_2_.__init__)


def test_fastfst_ntipmass_2__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_2_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntipmass_2__has_name():
    assert hasattr(fastfst_nTipMass_2_, "name")
    descriptor = None
    for klass in fastfst_nTipMass_2_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntipmass_2__has_value():
    assert hasattr(fastfst_nTipMass_2_, "value")
    descriptor = None
    for klass in fastfst_nTipMass_2_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntipmass_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nTipMass_1_)


def test_fastfst_ntipmass_1__constructor_exists():
    assert callable(fastfst_nTipMass_1_.__init__)


def test_fastfst_ntipmass_1__constructor_args():
    sig = inspect.signature(fastfst_nTipMass_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntipmass_1__has_name():
    assert hasattr(fastfst_nTipMass_1_, "name")
    descriptor = None
    for klass in fastfst_nTipMass_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntipmass_1__has_value():
    assert hasattr(fastfst_nTipMass_1_, "value")
    descriptor = None
    for klass in fastfst_nTipMass_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhubmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubMass)


def test_fastfst_nhubmass_constructor_exists():
    assert callable(fastfst_nHubMass.__init__)


def test_fastfst_nhubmass_constructor_args():
    sig = inspect.signature(fastfst_nHubMass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nhubmass_has_value():
    assert hasattr(fastfst_nHubMass, "value")
    descriptor = None
    for klass in fastfst_nHubMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhubmass_has_name():
    assert hasattr(fastfst_nHubMass, "name")
    descriptor = None
    for klass in fastfst_nHubMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnacmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacMass)


def test_fastfst_nnacmass_constructor_exists():
    assert callable(fastfst_nNacMass.__init__)


def test_fastfst_nnacmass_constructor_args():
    sig = inspect.signature(fastfst_nNacMass.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nnacmass_has_value():
    assert hasattr(fastfst_nNacMass, "value")
    descriptor = None
    for klass in fastfst_nNacMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnacmass_has_name():
    assert hasattr(fastfst_nNacMass, "name")
    descriptor = None
    for klass in fastfst_nNacMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nyawbrmass_is_not_abstract():
    assert not inspect.isabstract(fastfst_nYawBrMass)


def test_fastfst_nyawbrmass_constructor_exists():
    assert callable(fastfst_nYawBrMass.__init__)


def test_fastfst_nyawbrmass_constructor_args():
    sig = inspect.signature(fastfst_nYawBrMass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nyawbrmass_has_name():
    assert hasattr(fastfst_nYawBrMass, "name")
    descriptor = None
    for klass in fastfst_nYawBrMass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nyawbrmass_has_value():
    assert hasattr(fastfst_nYawBrMass, "value")
    descriptor = None
    for klass in fastfst_nYawBrMass.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nazimb1up_is_not_abstract():
    assert not inspect.isabstract(fastfst_nAzimB1Up)


def test_fastfst_nazimb1up_constructor_exists():
    assert callable(fastfst_nAzimB1Up.__init__)


def test_fastfst_nazimb1up_constructor_args():
    sig = inspect.signature(fastfst_nAzimB1Up.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nazimb1up_has_value():
    assert hasattr(fastfst_nAzimB1Up, "value")
    descriptor = None
    for klass in fastfst_nAzimB1Up.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nazimb1up_has_name():
    assert hasattr(fastfst_nAzimB1Up, "name")
    descriptor = None
    for klass in fastfst_nAzimB1Up.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nprecone_3__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_3_)


def test_fastfst_nprecone_3__constructor_exists():
    assert callable(fastfst_nPreCone_3_.__init__)


def test_fastfst_nprecone_3__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_3_.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nprecone_3__has_value():
    assert hasattr(fastfst_nPreCone_3_, "value")
    descriptor = None
    for klass in fastfst_nPreCone_3_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nprecone_3__has_name():
    assert hasattr(fastfst_nPreCone_3_, "name")
    descriptor = None
    for klass in fastfst_nPreCone_3_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nnaccmxn_is_not_abstract():
    assert not inspect.isabstract(fastfst_nNacCMxn)


def test_fastfst_nnaccmxn_constructor_exists():
    assert callable(fastfst_nNacCMxn.__init__)


def test_fastfst_nnaccmxn_constructor_args():
    sig = inspect.signature(fastfst_nNacCMxn.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_fastfst_nnaccmxn_has_value():
    assert hasattr(fastfst_nNacCMxn, "value")
    descriptor = None
    for klass in fastfst_nNacCMxn.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nnaccmxn_has_name():
    assert hasattr(fastfst_nNacCMxn, "name")
    descriptor = None
    for klass in fastfst_nNacCMxn.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_noverhang_is_not_abstract():
    assert not inspect.isabstract(fastfst_nOverHang)


def test_fastfst_noverhang_constructor_exists():
    assert callable(fastfst_nOverHang.__init__)


def test_fastfst_noverhang_constructor_args():
    sig = inspect.signature(fastfst_nOverHang.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_noverhang_has_name():
    assert hasattr(fastfst_nOverHang, "name")
    descriptor = None
    for klass in fastfst_nOverHang.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_noverhang_has_value():
    assert hasattr(fastfst_nOverHang, "value")
    descriptor = None
    for klass in fastfst_nOverHang.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nhubcm_is_not_abstract():
    assert not inspect.isabstract(fastfst_nHubCM)


def test_fastfst_nhubcm_constructor_exists():
    assert callable(fastfst_nHubCM.__init__)


def test_fastfst_nhubcm_constructor_args():
    sig = inspect.signature(fastfst_nHubCM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nhubcm_has_name():
    assert hasattr(fastfst_nHubCM, "name")
    descriptor = None
    for klass in fastfst_nHubCM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nhubcm_has_value():
    assert hasattr(fastfst_nHubCM, "value")
    descriptor = None
    for klass in fastfst_nHubCM.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nprecone_1__is_not_abstract():
    assert not inspect.isabstract(fastfst_nPreCone_1_)


def test_fastfst_nprecone_1__constructor_exists():
    assert callable(fastfst_nPreCone_1_.__init__)


def test_fastfst_nprecone_1__constructor_args():
    sig = inspect.signature(fastfst_nPreCone_1_.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nprecone_1__has_name():
    assert hasattr(fastfst_nPreCone_1_, "name")
    descriptor = None
    for klass in fastfst_nPreCone_1_.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nprecone_1__has_value():
    assert hasattr(fastfst_nPreCone_1_, "value")
    descriptor = None
    for klass in fastfst_nPreCone_1_.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ndelta3_is_not_abstract():
    assert not inspect.isabstract(fastfst_nDelta3)


def test_fastfst_ndelta3_constructor_exists():
    assert callable(fastfst_nDelta3.__init__)


def test_fastfst_ndelta3_constructor_args():
    sig = inspect.signature(fastfst_nDelta3.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ndelta3_has_name():
    assert hasattr(fastfst_nDelta3, "name")
    descriptor = None
    for klass in fastfst_nDelta3.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ndelta3_has_value():
    assert hasattr(fastfst_nDelta3, "value")
    descriptor = None
    for klass in fastfst_nDelta3.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_nshfttilt_is_not_abstract():
    assert not inspect.isabstract(fastfst_nShftTilt)


def test_fastfst_nshfttilt_constructor_exists():
    assert callable(fastfst_nShftTilt.__init__)


def test_fastfst_nshfttilt_constructor_args():
    sig = inspect.signature(fastfst_nShftTilt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_nshfttilt_has_name():
    assert hasattr(fastfst_nShftTilt, "name")
    descriptor = None
    for klass in fastfst_nShftTilt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_nshfttilt_has_value():
    assert hasattr(fastfst_nShftTilt, "value")
    descriptor = None
    for klass in fastfst_nShftTilt.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fastfst_ntwrrbht_is_not_abstract():
    assert not inspect.isabstract(fastfst_nTwrRBHt)


def test_fastfst_ntwrrbht_constructor_exists():
    assert callable(fastfst_nTwrRBHt.__init__)


def test_fastfst_ntwrrbht_constructor_args():
    sig = inspect.signature(fastfst_nTwrRBHt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_fastfst_ntwrrbht_has_name():
    assert hasattr(fastfst_nTwrRBHt, "name")
    descriptor = None
    for klass in fastfst_nTwrRBHt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fastfst_ntwrrbht_has_value():
    assert hasattr(fastfst_nTwrRBHt, "value")
    descriptor = None
    for klass in fastfst_nTwrRBHt.__mro__:
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
fastfst_nShftGagL_strategy = st.builds(
    fastfst_nShftGagL,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNcIMUzn_strategy = st.builds(
    fastfst_nNcIMUzn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_vOutList_strategy = st.builds(
    fastfst_vOutList,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_aBldGagNd_strategy = st.builds(
    fastfst_aBldGagNd,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iNBlGages_strategy = st.builds(
    fastfst_iNBlGages,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_aTwrGagNd_strategy = st.builds(
    fastfst_aTwrGagNd,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iNTwGages_strategy = st.builds(
    fastfst_iNTwGages,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_sOutFmt_strategy = st.builds(
    fastfst_sOutFmt,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_bTabDelim_strategy = st.builds(
    fastfst_bTabDelim,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nNcIMUyn_strategy = st.builds(
    fastfst_nNcIMUyn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNcIMUxn_strategy = st.builds(
    fastfst_nNcIMUxn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSttsTime_strategy = st.builds(
    fastfst_nSttsTime,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iDecFact_strategy = st.builds(
    fastfst_iDecFact,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTStart_strategy = st.builds(
    fastfst_nTStart,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fBldFile_3__strategy = st.builds(
    fastfst_fBldFile_3_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fBldFile_2__strategy = st.builds(
    fastfst_fBldFile_2_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_bOutFileFmt_strategy = st.builds(
    fastfst_bOutFileFmt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bSumPrint_strategy = st.builds(
    fastfst_bSumPrint,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_fLinFile_strategy = st.builds(
    fastfst_fLinFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_fADAMSFile_strategy = st.builds(
    fastfst_fADAMSFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fNoiseFile_strategy = st.builds(
    fastfst_fNoiseFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_fADFile_strategy = st.builds(
    fastfst_fADFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_nTeetHStP_strategy = st.builds(
    fastfst_nTeetHStP,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetSStP_strategy = st.builds(
    fastfst_nTeetSStP,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fBldFile_1__strategy = st.builds(
    fastfst_fBldFile_1_,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_nTpBrDT_strategy = st.builds(
    fastfst_nTpBrDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDrConD_strategy = st.builds(
    fastfst_nTBDrConD,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTBDrConN_strategy = st.builds(
    fastfst_nTBDrConN,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetHSSp_strategy = st.builds(
    fastfst_nTeetHSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetSSSp_strategy = st.builds(
    fastfst_nTeetSSSp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawNeut_strategy = st.builds(
    fastfst_nYawNeut,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawDamp_strategy = st.builds(
    fastfst_nYawDamp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetCDmp_strategy = st.builds(
    fastfst_nTeetCDmp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTeetDmp_strategy = st.builds(
    fastfst_nTeetDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTeetDmpP_strategy = st.builds(
    fastfst_nTeetDmpP,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iTeetMod_strategy = st.builds(
    fastfst_iTeetMod,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_fFurlFile_strategy = st.builds(
    fastfst_fFurlFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_nTEC_RLR_strategy = st.builds(
    fastfst_nTEC_RLR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bFurling_strategy = st.builds(
    fastfst_bFurling,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nTEC_SLR_strategy = st.builds(
    fastfst_nTEC_SLR,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nYawSpr_strategy = st.builds(
    fastfst_nYawSpr,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_fTwrFile_strategy = st.builds(
    fastfst_fTwrFile,
    value=
        safe_text,
    name=
        safe_text
)
fastfst_iTwrNodes_strategy = st.builds(
    fastfst_iTwrNodes,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_fPtfmFile_strategy = st.builds(
    fastfst_fPtfmFile,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_iPtfmModel_strategy = st.builds(
    fastfst_iPtfmModel,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nTEC_MR_strategy = st.builds(
    fastfst_nTEC_MR,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nSIG_SlPc_strategy = st.builds(
    fastfst_nSIG_SlPc,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nDTTorDmp_strategy = st.builds(
    fastfst_nDTTorDmp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_VLL_strategy = st.builds(
    fastfst_nTEC_VLL,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Rres_strategy = st.builds(
    fastfst_nTEC_Rres,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Sres_strategy = st.builds(
    fastfst_nTEC_Sres,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTEC_Npol_strategy = st.builds(
    fastfst_nTEC_Npol,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTEC_Freq_strategy = st.builds(
    fastfst_nTEC_Freq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nSIG_PORt_strategy = st.builds(
    fastfst_nSIG_PORt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSIG_RtTq_strategy = st.builds(
    fastfst_nSIG_RtTq,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSIG_SySp_strategy = st.builds(
    fastfst_nSIG_SySp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGenIner_strategy = st.builds(
    fastfst_nGenIner,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nDTTorSpr_strategy = st.builds(
    fastfst_nDTTorSpr,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_fDynBrkFi_strategy = st.builds(
    fastfst_fDynBrkFi,
    name=
        safe_text,
    value=
        safe_text
)
fastfst_nTwr2Shft_strategy = st.builds(
    fastfst_nTwr2Shft,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTowerHt_strategy = st.builds(
    fastfst_nTowerHt,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacCMzn_strategy = st.builds(
    fastfst_nNacCMzn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nNacCMyn_strategy = st.builds(
    fastfst_nNacCMyn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTDspSS_strategy = st.builds(
    fastfst_nTTDspSS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTTDspFA_strategy = st.builds(
    fastfst_nTTDspFA,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYaw_strategy = st.builds(
    fastfst_nNacYaw,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nRotSpeed_strategy = st.builds(
    fastfst_nRotSpeed,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nUndSling_strategy = st.builds(
    fastfst_nUndSling,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPSpnElN_strategy = st.builds(
    fastfst_nPSpnElN,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nHubRad_strategy = st.builds(
    fastfst_nHubRad,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTipRad_strategy = st.builds(
    fastfst_nTipRad,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bTwFADOF1_strategy = st.builds(
    fastfst_bTwFADOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bYawDOF_strategy = st.builds(
    fastfst_bYawDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bGenDOF_strategy = st.builds(
    fastfst_bGenDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bDrTrDOF_strategy = st.builds(
    fastfst_bDrTrDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_bTeetDOF_strategy = st.builds(
    fastfst_bTeetDOF,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bEdgeDOF_strategy = st.builds(
    fastfst_bEdgeDOF,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nAzimuth_strategy = st.builds(
    fastfst_nAzimuth,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bFlapDOF2_strategy = st.builds(
    fastfst_bFlapDOF2,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nTeetDefl_strategy = st.builds(
    fastfst_nTeetDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bFlapDOF1_strategy = st.builds(
    fastfst_bFlapDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nIPDefl_strategy = st.builds(
    fastfst_nIPDefl,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGravity_strategy = st.builds(
    fastfst_nGravity,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nOoPDefl_strategy = st.builds(
    fastfst_nOoPDefl,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nBlPitchF_3__strategy = st.builds(
    fastfst_nBlPitchF_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nBlPitchF_2__strategy = st.builds(
    fastfst_nBlPitchF_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bCompNoise_strategy = st.builds(
    fastfst_bCompNoise,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nBlPitchF_1__strategy = st.builds(
    fastfst_nBlPitchF_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bCompAero_strategy = st.builds(
    fastfst_bCompAero,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nBlPitch_3__strategy = st.builds(
    fastfst_nBlPitch_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bTwSSDOF2_strategy = st.builds(
    fastfst_bTwSSDOF2,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nBlPitch_2__strategy = st.builds(
    fastfst_nBlPitch_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bTwSSDOF1_strategy = st.builds(
    fastfst_bTwSSDOF1,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bTwFADOF2_strategy = st.builds(
    fastfst_bTwFADOF2,
    value=
        st.booleans(),
    name=
        safe_text
)
fastfst_nTPitManE_2__strategy = st.builds(
    fastfst_nTPitManE_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManE_1__strategy = st.builds(
    fastfst_nTPitManE_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTPitManS_3__strategy = st.builds(
    fastfst_nTPitManS_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTPitManS_2__strategy = st.builds(
    fastfst_nTPitManS_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManS_1__strategy = st.builds(
    fastfst_nTPitManS_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYawF_strategy = st.builds(
    fastfst_nNacYawF,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTYawManE_strategy = st.builds(
    fastfst_nTYawManE,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTYawManS_strategy = st.builds(
    fastfst_nTYawManS,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDepISp_3__strategy = st.builds(
    fastfst_nTBDepISp_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTBDepISp_2__strategy = st.builds(
    fastfst_nTBDepISp_2_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTBDepISp_1__strategy = st.builds(
    fastfst_nTBDepISp_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTpBrDp_3__strategy = st.builds(
    fastfst_nTTpBrDp_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTTpBrDp_2__strategy = st.builds(
    fastfst_nTTpBrDp_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTTpBrDp_1__strategy = st.builds(
    fastfst_nTTpBrDp_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nBlPitch_1__strategy = st.builds(
    fastfst_nBlPitch_1_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTPitManE_3__strategy = st.builds(
    fastfst_nTPitManE_3_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iHSSBrMode_strategy = st.builds(
    fastfst_iHSSBrMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTimGenOf_strategy = st.builds(
    fastfst_nTimGenOf,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTimGenOn_strategy = st.builds(
    fastfst_nTimGenOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nSpdGenOn_strategy = st.builds(
    fastfst_nSpdGenOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_bGenTiStp_strategy = st.builds(
    fastfst_bGenTiStp,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_bGenTiStr_strategy = st.builds(
    fastfst_bGenTiStr,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_iGenModel_strategy = st.builds(
    fastfst_iGenModel,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nVS_SlPc_strategy = st.builds(
    fastfst_nVS_SlPc,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nVS_Rgn2K_strategy = st.builds(
    fastfst_nVS_Rgn2K,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nVS_RtTq_strategy = st.builds(
    fastfst_nVS_RtTq,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nVS_RtGnSp_strategy = st.builds(
    fastfst_nVS_RtGnSp,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iVSContrl_strategy = st.builds(
    fastfst_iVSContrl,
    value=
        st.integers(),
    name=
        safe_text
)
fastfst_nTPCOn_strategy = st.builds(
    fastfst_nTPCOn,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_iPCMode_strategy = st.builds(
    fastfst_iPCMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nTYCOn_strategy = st.builds(
    fastfst_nTYCOn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_iYCMode_strategy = st.builds(
    fastfst_iYCMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nDT_strategy = st.builds(
    fastfst_nDT,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTMax_strategy = st.builds(
    fastfst_nTMax,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTiDynBrk_strategy = st.builds(
    fastfst_nTiDynBrk,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTHSSBrDp_strategy = st.builds(
    fastfst_nTHSSBrDp,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_iADAMSPrep_strategy = st.builds(
    fastfst_iADAMSPrep,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_bEcho_strategy = st.builds(
    fastfst_bEcho,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_Section_strategy = st.builds(
    fastfst_Section,
    name=
        safe_text
)
fastfst_Header_strategy = st.builds(
    fastfst_Header,
    rows=
        safe_text
)
fastfst_ModelFastfst_strategy = st.builds(
    fastfst_ModelFastfst,
)
fastfst_iNumBl_strategy = st.builds(
    fastfst_iNumBl,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_iAnalMode_strategy = st.builds(
    fastfst_iAnalMode,
    name=
        safe_text,
    value=
        st.integers()
)
fastfst_nHSSBrDT_strategy = st.builds(
    fastfst_nHSSBrDT,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHSSBrTqF_strategy = st.builds(
    fastfst_nHSSBrTqF,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_bGBRevers_strategy = st.builds(
    fastfst_bGBRevers,
    name=
        safe_text,
    value=
        st.booleans()
)
fastfst_nGBRatio_strategy = st.builds(
    fastfst_nGBRatio,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nGenEff_strategy = st.builds(
    fastfst_nGenEff,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nGBoxEff_strategy = st.builds(
    fastfst_nGBoxEff,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nHubIner_strategy = st.builds(
    fastfst_nHubIner,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPreCone_2__strategy = st.builds(
    fastfst_nPreCone_2_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacYIner_strategy = st.builds(
    fastfst_nNacYIner,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTipMass_3__strategy = st.builds(
    fastfst_nTipMass_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nTipMass_2__strategy = st.builds(
    fastfst_nTipMass_2_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTipMass_1__strategy = st.builds(
    fastfst_nTipMass_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHubMass_strategy = st.builds(
    fastfst_nHubMass,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacMass_strategy = st.builds(
    fastfst_nNacMass,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nYawBrMass_strategy = st.builds(
    fastfst_nYawBrMass,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nAzimB1Up_strategy = st.builds(
    fastfst_nAzimB1Up,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nPreCone_3__strategy = st.builds(
    fastfst_nPreCone_3_,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nNacCMxn_strategy = st.builds(
    fastfst_nNacCMxn,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
fastfst_nOverHang_strategy = st.builds(
    fastfst_nOverHang,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nHubCM_strategy = st.builds(
    fastfst_nHubCM,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nPreCone_1__strategy = st.builds(
    fastfst_nPreCone_1_,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nDelta3_strategy = st.builds(
    fastfst_nDelta3,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nShftTilt_strategy = st.builds(
    fastfst_nShftTilt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
fastfst_nTwrRBHt_strategy = st.builds(
    fastfst_nTwrRBHt,
    name=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=fastfst_nShftGagL_strategy)
@settings(max_examples=50)
def test_fastfst_nshftgagl_instantiation(instance):
    assert isinstance(instance, fastfst_nShftGagL)



@given(instance=fastfst_nShftGagL_strategy)
def test_fastfst_nshftgagl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nShftGagL_strategy)
def test_fastfst_nshftgagl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nNcIMUzn_strategy)
@settings(max_examples=50)
def test_fastfst_nncimuzn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUzn)



@given(instance=fastfst_nNcIMUzn_strategy)
def test_fastfst_nncimuzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNcIMUzn_strategy)
def test_fastfst_nncimuzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_vOutList_strategy)
@settings(max_examples=50)
def test_fastfst_voutlist_instantiation(instance):
    assert isinstance(instance, fastfst_vOutList)



@given(instance=fastfst_vOutList_strategy)
def test_fastfst_voutlist_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_vOutList_strategy)
def test_fastfst_voutlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_aBldGagNd_strategy)
@settings(max_examples=50)
def test_fastfst_abldgagnd_instantiation(instance):
    assert isinstance(instance, fastfst_aBldGagNd)



@given(instance=fastfst_aBldGagNd_strategy)
def test_fastfst_abldgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_aBldGagNd_strategy)
def test_fastfst_abldgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_iNBlGages_strategy)
@settings(max_examples=50)
def test_fastfst_inblgages_instantiation(instance):
    assert isinstance(instance, fastfst_iNBlGages)



@given(instance=fastfst_iNBlGages_strategy)
def test_fastfst_inblgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iNBlGages_strategy)
def test_fastfst_inblgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_aTwrGagNd_strategy)
@settings(max_examples=50)
def test_fastfst_atwrgagnd_instantiation(instance):
    assert isinstance(instance, fastfst_aTwrGagNd)



@given(instance=fastfst_aTwrGagNd_strategy)
def test_fastfst_atwrgagnd_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_aTwrGagNd_strategy)
def test_fastfst_atwrgagnd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_iNTwGages_strategy)
@settings(max_examples=50)
def test_fastfst_intwgages_instantiation(instance):
    assert isinstance(instance, fastfst_iNTwGages)



@given(instance=fastfst_iNTwGages_strategy)
def test_fastfst_intwgages_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iNTwGages_strategy)
def test_fastfst_intwgages_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_sOutFmt_strategy)
@settings(max_examples=50)
def test_fastfst_soutfmt_instantiation(instance):
    assert isinstance(instance, fastfst_sOutFmt)



@given(instance=fastfst_sOutFmt_strategy)
def test_fastfst_soutfmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_sOutFmt_strategy)
def test_fastfst_soutfmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bTabDelim_strategy)
@settings(max_examples=50)
def test_fastfst_btabdelim_instantiation(instance):
    assert isinstance(instance, fastfst_bTabDelim)



@given(instance=fastfst_bTabDelim_strategy)
def test_fastfst_btabdelim_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTabDelim_strategy)
def test_fastfst_btabdelim_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nNcIMUyn_strategy)
@settings(max_examples=50)
def test_fastfst_nncimuyn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUyn)



@given(instance=fastfst_nNcIMUyn_strategy)
def test_fastfst_nncimuyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNcIMUyn_strategy)
def test_fastfst_nncimuyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nNcIMUxn_strategy)
@settings(max_examples=50)
def test_fastfst_nncimuxn_instantiation(instance):
    assert isinstance(instance, fastfst_nNcIMUxn)



@given(instance=fastfst_nNcIMUxn_strategy)
def test_fastfst_nncimuxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNcIMUxn_strategy)
def test_fastfst_nncimuxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nSttsTime_strategy)
@settings(max_examples=50)
def test_fastfst_nsttstime_instantiation(instance):
    assert isinstance(instance, fastfst_nSttsTime)



@given(instance=fastfst_nSttsTime_strategy)
def test_fastfst_nsttstime_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSttsTime_strategy)
def test_fastfst_nsttstime_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iDecFact_strategy)
@settings(max_examples=50)
def test_fastfst_idecfact_instantiation(instance):
    assert isinstance(instance, fastfst_iDecFact)



@given(instance=fastfst_iDecFact_strategy)
def test_fastfst_idecfact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iDecFact_strategy)
def test_fastfst_idecfact_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTStart_strategy)
@settings(max_examples=50)
def test_fastfst_ntstart_instantiation(instance):
    assert isinstance(instance, fastfst_nTStart)



@given(instance=fastfst_nTStart_strategy)
def test_fastfst_ntstart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTStart_strategy)
def test_fastfst_ntstart_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_fBldFile_3__strategy)
@settings(max_examples=50)
def test_fastfst_fbldfile_3__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_3_)



@given(instance=fastfst_fBldFile_3__strategy)
def test_fastfst_fbldfile_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_3__strategy)
def test_fastfst_fbldfile_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fBldFile_2__strategy)
@settings(max_examples=50)
def test_fastfst_fbldfile_2__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_2_)



@given(instance=fastfst_fBldFile_2__strategy)
def test_fastfst_fbldfile_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_2__strategy)
def test_fastfst_fbldfile_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bOutFileFmt_strategy)
@settings(max_examples=50)
def test_fastfst_boutfilefmt_instantiation(instance):
    assert isinstance(instance, fastfst_bOutFileFmt)



@given(instance=fastfst_bOutFileFmt_strategy)
def test_fastfst_boutfilefmt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bOutFileFmt_strategy)
def test_fastfst_boutfilefmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bSumPrint_strategy)
@settings(max_examples=50)
def test_fastfst_bsumprint_instantiation(instance):
    assert isinstance(instance, fastfst_bSumPrint)



@given(instance=fastfst_bSumPrint_strategy)
def test_fastfst_bsumprint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bSumPrint_strategy)
def test_fastfst_bsumprint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_fLinFile_strategy)
@settings(max_examples=50)
def test_fastfst_flinfile_instantiation(instance):
    assert isinstance(instance, fastfst_fLinFile)



@given(instance=fastfst_fLinFile_strategy)
def test_fastfst_flinfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fLinFile_strategy)
def test_fastfst_flinfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_fADAMSFile_strategy)
@settings(max_examples=50)
def test_fastfst_fadamsfile_instantiation(instance):
    assert isinstance(instance, fastfst_fADAMSFile)



@given(instance=fastfst_fADAMSFile_strategy)
def test_fastfst_fadamsfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fADAMSFile_strategy)
def test_fastfst_fadamsfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fNoiseFile_strategy)
@settings(max_examples=50)
def test_fastfst_fnoisefile_instantiation(instance):
    assert isinstance(instance, fastfst_fNoiseFile)



@given(instance=fastfst_fNoiseFile_strategy)
def test_fastfst_fnoisefile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fNoiseFile_strategy)
def test_fastfst_fnoisefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fADFile_strategy)
@settings(max_examples=50)
def test_fastfst_fadfile_instantiation(instance):
    assert isinstance(instance, fastfst_fADFile)



@given(instance=fastfst_fADFile_strategy)
def test_fastfst_fadfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fADFile_strategy)
def test_fastfst_fadfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTeetHStP_strategy)
@settings(max_examples=50)
def test_fastfst_nteethstp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetHStP)



@given(instance=fastfst_nTeetHStP_strategy)
def test_fastfst_nteethstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetHStP_strategy)
def test_fastfst_nteethstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTeetSStP_strategy)
@settings(max_examples=50)
def test_fastfst_nteetsstp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetSStP)



@given(instance=fastfst_nTeetSStP_strategy)
def test_fastfst_nteetsstp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetSStP_strategy)
def test_fastfst_nteetsstp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_fBldFile_1__strategy)
@settings(max_examples=50)
def test_fastfst_fbldfile_1__instantiation(instance):
    assert isinstance(instance, fastfst_fBldFile_1_)



@given(instance=fastfst_fBldFile_1__strategy)
def test_fastfst_fbldfile_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fBldFile_1__strategy)
def test_fastfst_fbldfile_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTpBrDT_strategy)
@settings(max_examples=50)
def test_fastfst_ntpbrdt_instantiation(instance):
    assert isinstance(instance, fastfst_nTpBrDT)



@given(instance=fastfst_nTpBrDT_strategy)
def test_fastfst_ntpbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTpBrDT_strategy)
def test_fastfst_ntpbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTBDrConD_strategy)
@settings(max_examples=50)
def test_fastfst_ntbdrcond_instantiation(instance):
    assert isinstance(instance, fastfst_nTBDrConD)



@given(instance=fastfst_nTBDrConD_strategy)
def test_fastfst_ntbdrcond_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDrConD_strategy)
def test_fastfst_ntbdrcond_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTBDrConN_strategy)
@settings(max_examples=50)
def test_fastfst_ntbdrconn_instantiation(instance):
    assert isinstance(instance, fastfst_nTBDrConN)



@given(instance=fastfst_nTBDrConN_strategy)
def test_fastfst_ntbdrconn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDrConN_strategy)
def test_fastfst_ntbdrconn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTeetHSSp_strategy)
@settings(max_examples=50)
def test_fastfst_nteethssp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetHSSp)



@given(instance=fastfst_nTeetHSSp_strategy)
def test_fastfst_nteethssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetHSSp_strategy)
def test_fastfst_nteethssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTeetSSSp_strategy)
@settings(max_examples=50)
def test_fastfst_nteetsssp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetSSSp)



@given(instance=fastfst_nTeetSSSp_strategy)
def test_fastfst_nteetsssp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetSSSp_strategy)
def test_fastfst_nteetsssp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nYawNeut_strategy)
@settings(max_examples=50)
def test_fastfst_nyawneut_instantiation(instance):
    assert isinstance(instance, fastfst_nYawNeut)



@given(instance=fastfst_nYawNeut_strategy)
def test_fastfst_nyawneut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nYawNeut_strategy)
def test_fastfst_nyawneut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nYawDamp_strategy)
@settings(max_examples=50)
def test_fastfst_nyawdamp_instantiation(instance):
    assert isinstance(instance, fastfst_nYawDamp)



@given(instance=fastfst_nYawDamp_strategy)
def test_fastfst_nyawdamp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawDamp_strategy)
def test_fastfst_nyawdamp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTeetCDmp_strategy)
@settings(max_examples=50)
def test_fastfst_nteetcdmp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetCDmp)



@given(instance=fastfst_nTeetCDmp_strategy)
def test_fastfst_nteetcdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetCDmp_strategy)
def test_fastfst_nteetcdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTeetDmp_strategy)
@settings(max_examples=50)
def test_fastfst_nteetdmp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDmp)



@given(instance=fastfst_nTeetDmp_strategy)
def test_fastfst_nteetdmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTeetDmp_strategy)
def test_fastfst_nteetdmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTeetDmpP_strategy)
@settings(max_examples=50)
def test_fastfst_nteetdmpp_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDmpP)



@given(instance=fastfst_nTeetDmpP_strategy)
def test_fastfst_nteetdmpp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetDmpP_strategy)
def test_fastfst_nteetdmpp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iTeetMod_strategy)
@settings(max_examples=50)
def test_fastfst_iteetmod_instantiation(instance):
    assert isinstance(instance, fastfst_iTeetMod)



@given(instance=fastfst_iTeetMod_strategy)
def test_fastfst_iteetmod_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iTeetMod_strategy)
def test_fastfst_iteetmod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fFurlFile_strategy)
@settings(max_examples=50)
def test_fastfst_ffurlfile_instantiation(instance):
    assert isinstance(instance, fastfst_fFurlFile)



@given(instance=fastfst_fFurlFile_strategy)
def test_fastfst_ffurlfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fFurlFile_strategy)
def test_fastfst_ffurlfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTEC_RLR_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_rlr_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_RLR)



@given(instance=fastfst_nTEC_RLR_strategy)
def test_fastfst_ntec_rlr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_RLR_strategy)
def test_fastfst_ntec_rlr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bFurling_strategy)
@settings(max_examples=50)
def test_fastfst_bfurling_instantiation(instance):
    assert isinstance(instance, fastfst_bFurling)



@given(instance=fastfst_bFurling_strategy)
def test_fastfst_bfurling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFurling_strategy)
def test_fastfst_bfurling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTEC_SLR_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_slr_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_SLR)



@given(instance=fastfst_nTEC_SLR_strategy)
def test_fastfst_ntec_slr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTEC_SLR_strategy)
def test_fastfst_ntec_slr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nYawSpr_strategy)
@settings(max_examples=50)
def test_fastfst_nyawspr_instantiation(instance):
    assert isinstance(instance, fastfst_nYawSpr)



@given(instance=fastfst_nYawSpr_strategy)
def test_fastfst_nyawspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawSpr_strategy)
def test_fastfst_nyawspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_fTwrFile_strategy)
@settings(max_examples=50)
def test_fastfst_ftwrfile_instantiation(instance):
    assert isinstance(instance, fastfst_fTwrFile)



@given(instance=fastfst_fTwrFile_strategy)
def test_fastfst_ftwrfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_fTwrFile_strategy)
def test_fastfst_ftwrfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_iTwrNodes_strategy)
@settings(max_examples=50)
def test_fastfst_itwrnodes_instantiation(instance):
    assert isinstance(instance, fastfst_iTwrNodes)



@given(instance=fastfst_iTwrNodes_strategy)
def test_fastfst_itwrnodes_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iTwrNodes_strategy)
def test_fastfst_itwrnodes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fPtfmFile_strategy)
@settings(max_examples=50)
def test_fastfst_fptfmfile_instantiation(instance):
    assert isinstance(instance, fastfst_fPtfmFile)



@given(instance=fastfst_fPtfmFile_strategy)
def test_fastfst_fptfmfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fPtfmFile_strategy)
def test_fastfst_fptfmfile_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iPtfmModel_strategy)
@settings(max_examples=50)
def test_fastfst_iptfmmodel_instantiation(instance):
    assert isinstance(instance, fastfst_iPtfmModel)



@given(instance=fastfst_iPtfmModel_strategy)
def test_fastfst_iptfmmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iPtfmModel_strategy)
def test_fastfst_iptfmmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTEC_MR_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_mr_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_MR)



@given(instance=fastfst_nTEC_MR_strategy)
def test_fastfst_ntec_mr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_MR_strategy)
def test_fastfst_ntec_mr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nSIG_SlPc_strategy)
@settings(max_examples=50)
def test_fastfst_nsig_slpc_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_SlPc)



@given(instance=fastfst_nSIG_SlPc_strategy)
def test_fastfst_nsig_slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nSIG_SlPc_strategy)
def test_fastfst_nsig_slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nDTTorDmp_strategy)
@settings(max_examples=50)
def test_fastfst_ndttordmp_instantiation(instance):
    assert isinstance(instance, fastfst_nDTTorDmp)



@given(instance=fastfst_nDTTorDmp_strategy)
def test_fastfst_ndttordmp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDTTorDmp_strategy)
def test_fastfst_ndttordmp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTEC_VLL_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_vll_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_VLL)



@given(instance=fastfst_nTEC_VLL_strategy)
def test_fastfst_ntec_vll_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_VLL_strategy)
def test_fastfst_ntec_vll_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTEC_Rres_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_rres_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Rres)



@given(instance=fastfst_nTEC_Rres_strategy)
def test_fastfst_ntec_rres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Rres_strategy)
def test_fastfst_ntec_rres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTEC_Sres_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_sres_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Sres)



@given(instance=fastfst_nTEC_Sres_strategy)
def test_fastfst_ntec_sres_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTEC_Sres_strategy)
def test_fastfst_ntec_sres_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTEC_Npol_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_npol_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Npol)



@given(instance=fastfst_nTEC_Npol_strategy)
def test_fastfst_ntec_npol_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Npol_strategy)
def test_fastfst_ntec_npol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTEC_Freq_strategy)
@settings(max_examples=50)
def test_fastfst_ntec_freq_instantiation(instance):
    assert isinstance(instance, fastfst_nTEC_Freq)



@given(instance=fastfst_nTEC_Freq_strategy)
def test_fastfst_ntec_freq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTEC_Freq_strategy)
def test_fastfst_ntec_freq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nSIG_PORt_strategy)
@settings(max_examples=50)
def test_fastfst_nsig_port_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_PORt)



@given(instance=fastfst_nSIG_PORt_strategy)
def test_fastfst_nsig_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_PORt_strategy)
def test_fastfst_nsig_port_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nSIG_RtTq_strategy)
@settings(max_examples=50)
def test_fastfst_nsig_rttq_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_RtTq)



@given(instance=fastfst_nSIG_RtTq_strategy)
def test_fastfst_nsig_rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_RtTq_strategy)
def test_fastfst_nsig_rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nSIG_SySp_strategy)
@settings(max_examples=50)
def test_fastfst_nsig_sysp_instantiation(instance):
    assert isinstance(instance, fastfst_nSIG_SySp)



@given(instance=fastfst_nSIG_SySp_strategy)
def test_fastfst_nsig_sysp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nSIG_SySp_strategy)
def test_fastfst_nsig_sysp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nGenIner_strategy)
@settings(max_examples=50)
def test_fastfst_ngeniner_instantiation(instance):
    assert isinstance(instance, fastfst_nGenIner)



@given(instance=fastfst_nGenIner_strategy)
def test_fastfst_ngeniner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nGenIner_strategy)
def test_fastfst_ngeniner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nDTTorSpr_strategy)
@settings(max_examples=50)
def test_fastfst_ndttorspr_instantiation(instance):
    assert isinstance(instance, fastfst_nDTTorSpr)



@given(instance=fastfst_nDTTorSpr_strategy)
def test_fastfst_ndttorspr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDTTorSpr_strategy)
def test_fastfst_ndttorspr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_fDynBrkFi_strategy)
@settings(max_examples=50)
def test_fastfst_fdynbrkfi_instantiation(instance):
    assert isinstance(instance, fastfst_fDynBrkFi)



@given(instance=fastfst_fDynBrkFi_strategy)
def test_fastfst_fdynbrkfi_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_fDynBrkFi_strategy)
def test_fastfst_fdynbrkfi_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTwr2Shft_strategy)
@settings(max_examples=50)
def test_fastfst_ntwr2shft_instantiation(instance):
    assert isinstance(instance, fastfst_nTwr2Shft)



@given(instance=fastfst_nTwr2Shft_strategy)
def test_fastfst_ntwr2shft_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTwr2Shft_strategy)
def test_fastfst_ntwr2shft_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTowerHt_strategy)
@settings(max_examples=50)
def test_fastfst_ntowerht_instantiation(instance):
    assert isinstance(instance, fastfst_nTowerHt)



@given(instance=fastfst_nTowerHt_strategy)
def test_fastfst_ntowerht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTowerHt_strategy)
def test_fastfst_ntowerht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacCMzn_strategy)
@settings(max_examples=50)
def test_fastfst_nnaccmzn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMzn)



@given(instance=fastfst_nNacCMzn_strategy)
def test_fastfst_nnaccmzn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacCMzn_strategy)
def test_fastfst_nnaccmzn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nNacCMyn_strategy)
@settings(max_examples=50)
def test_fastfst_nnaccmyn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMyn)



@given(instance=fastfst_nNacCMyn_strategy)
def test_fastfst_nnaccmyn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacCMyn_strategy)
def test_fastfst_nnaccmyn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTTDspSS_strategy)
@settings(max_examples=50)
def test_fastfst_nttdspss_instantiation(instance):
    assert isinstance(instance, fastfst_nTTDspSS)



@given(instance=fastfst_nTTDspSS_strategy)
def test_fastfst_nttdspss_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTDspSS_strategy)
def test_fastfst_nttdspss_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTTDspFA_strategy)
@settings(max_examples=50)
def test_fastfst_nttdspfa_instantiation(instance):
    assert isinstance(instance, fastfst_nTTDspFA)



@given(instance=fastfst_nTTDspFA_strategy)
def test_fastfst_nttdspfa_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTDspFA_strategy)
def test_fastfst_nttdspfa_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacYaw_strategy)
@settings(max_examples=50)
def test_fastfst_nnacyaw_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYaw)



@given(instance=fastfst_nNacYaw_strategy)
def test_fastfst_nnacyaw_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYaw_strategy)
def test_fastfst_nnacyaw_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nRotSpeed_strategy)
@settings(max_examples=50)
def test_fastfst_nrotspeed_instantiation(instance):
    assert isinstance(instance, fastfst_nRotSpeed)



@given(instance=fastfst_nRotSpeed_strategy)
def test_fastfst_nrotspeed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nRotSpeed_strategy)
def test_fastfst_nrotspeed_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nUndSling_strategy)
@settings(max_examples=50)
def test_fastfst_nundsling_instantiation(instance):
    assert isinstance(instance, fastfst_nUndSling)



@given(instance=fastfst_nUndSling_strategy)
def test_fastfst_nundsling_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nUndSling_strategy)
def test_fastfst_nundsling_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nPSpnElN_strategy)
@settings(max_examples=50)
def test_fastfst_npspneln_instantiation(instance):
    assert isinstance(instance, fastfst_nPSpnElN)



@given(instance=fastfst_nPSpnElN_strategy)
def test_fastfst_npspneln_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nPSpnElN_strategy)
def test_fastfst_npspneln_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nHubRad_strategy)
@settings(max_examples=50)
def test_fastfst_nhubrad_instantiation(instance):
    assert isinstance(instance, fastfst_nHubRad)



@given(instance=fastfst_nHubRad_strategy)
def test_fastfst_nhubrad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubRad_strategy)
def test_fastfst_nhubrad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTipRad_strategy)
@settings(max_examples=50)
def test_fastfst_ntiprad_instantiation(instance):
    assert isinstance(instance, fastfst_nTipRad)



@given(instance=fastfst_nTipRad_strategy)
def test_fastfst_ntiprad_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipRad_strategy)
def test_fastfst_ntiprad_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bTwFADOF1_strategy)
@settings(max_examples=50)
def test_fastfst_btwfadof1_instantiation(instance):
    assert isinstance(instance, fastfst_bTwFADOF1)



@given(instance=fastfst_bTwFADOF1_strategy)
def test_fastfst_btwfadof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTwFADOF1_strategy)
def test_fastfst_btwfadof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bYawDOF_strategy)
@settings(max_examples=50)
def test_fastfst_byawdof_instantiation(instance):
    assert isinstance(instance, fastfst_bYawDOF)



@given(instance=fastfst_bYawDOF_strategy)
def test_fastfst_byawdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bYawDOF_strategy)
def test_fastfst_byawdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bGenDOF_strategy)
@settings(max_examples=50)
def test_fastfst_bgendof_instantiation(instance):
    assert isinstance(instance, fastfst_bGenDOF)



@given(instance=fastfst_bGenDOF_strategy)
def test_fastfst_bgendof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenDOF_strategy)
def test_fastfst_bgendof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bDrTrDOF_strategy)
@settings(max_examples=50)
def test_fastfst_bdrtrdof_instantiation(instance):
    assert isinstance(instance, fastfst_bDrTrDOF)



@given(instance=fastfst_bDrTrDOF_strategy)
def test_fastfst_bdrtrdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bDrTrDOF_strategy)
def test_fastfst_bdrtrdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bTeetDOF_strategy)
@settings(max_examples=50)
def test_fastfst_bteetdof_instantiation(instance):
    assert isinstance(instance, fastfst_bTeetDOF)



@given(instance=fastfst_bTeetDOF_strategy)
def test_fastfst_bteetdof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTeetDOF_strategy)
def test_fastfst_bteetdof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bEdgeDOF_strategy)
@settings(max_examples=50)
def test_fastfst_bedgedof_instantiation(instance):
    assert isinstance(instance, fastfst_bEdgeDOF)



@given(instance=fastfst_bEdgeDOF_strategy)
def test_fastfst_bedgedof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bEdgeDOF_strategy)
def test_fastfst_bedgedof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nAzimuth_strategy)
@settings(max_examples=50)
def test_fastfst_nazimuth_instantiation(instance):
    assert isinstance(instance, fastfst_nAzimuth)



@given(instance=fastfst_nAzimuth_strategy)
def test_fastfst_nazimuth_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nAzimuth_strategy)
def test_fastfst_nazimuth_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bFlapDOF2_strategy)
@settings(max_examples=50)
def test_fastfst_bflapdof2_instantiation(instance):
    assert isinstance(instance, fastfst_bFlapDOF2)



@given(instance=fastfst_bFlapDOF2_strategy)
def test_fastfst_bflapdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFlapDOF2_strategy)
def test_fastfst_bflapdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTeetDefl_strategy)
@settings(max_examples=50)
def test_fastfst_nteetdefl_instantiation(instance):
    assert isinstance(instance, fastfst_nTeetDefl)



@given(instance=fastfst_nTeetDefl_strategy)
def test_fastfst_nteetdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTeetDefl_strategy)
def test_fastfst_nteetdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bFlapDOF1_strategy)
@settings(max_examples=50)
def test_fastfst_bflapdof1_instantiation(instance):
    assert isinstance(instance, fastfst_bFlapDOF1)



@given(instance=fastfst_bFlapDOF1_strategy)
def test_fastfst_bflapdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bFlapDOF1_strategy)
def test_fastfst_bflapdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nIPDefl_strategy)
@settings(max_examples=50)
def test_fastfst_nipdefl_instantiation(instance):
    assert isinstance(instance, fastfst_nIPDefl)



@given(instance=fastfst_nIPDefl_strategy)
def test_fastfst_nipdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nIPDefl_strategy)
def test_fastfst_nipdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nGravity_strategy)
@settings(max_examples=50)
def test_fastfst_ngravity_instantiation(instance):
    assert isinstance(instance, fastfst_nGravity)



@given(instance=fastfst_nGravity_strategy)
def test_fastfst_ngravity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGravity_strategy)
def test_fastfst_ngravity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nOoPDefl_strategy)
@settings(max_examples=50)
def test_fastfst_noopdefl_instantiation(instance):
    assert isinstance(instance, fastfst_nOoPDefl)



@given(instance=fastfst_nOoPDefl_strategy)
def test_fastfst_noopdefl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nOoPDefl_strategy)
def test_fastfst_noopdefl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nBlPitchF_3__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitchf_3__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_3_)



@given(instance=fastfst_nBlPitchF_3__strategy)
def test_fastfst_nblpitchf_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_3__strategy)
def test_fastfst_nblpitchf_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nBlPitchF_2__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitchf_2__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_2_)



@given(instance=fastfst_nBlPitchF_2__strategy)
def test_fastfst_nblpitchf_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_2__strategy)
def test_fastfst_nblpitchf_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bCompNoise_strategy)
@settings(max_examples=50)
def test_fastfst_bcompnoise_instantiation(instance):
    assert isinstance(instance, fastfst_bCompNoise)



@given(instance=fastfst_bCompNoise_strategy)
def test_fastfst_bcompnoise_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bCompNoise_strategy)
def test_fastfst_bcompnoise_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nBlPitchF_1__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitchf_1__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitchF_1_)



@given(instance=fastfst_nBlPitchF_1__strategy)
def test_fastfst_nblpitchf_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitchF_1__strategy)
def test_fastfst_nblpitchf_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bCompAero_strategy)
@settings(max_examples=50)
def test_fastfst_bcompaero_instantiation(instance):
    assert isinstance(instance, fastfst_bCompAero)



@given(instance=fastfst_bCompAero_strategy)
def test_fastfst_bcompaero_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bCompAero_strategy)
def test_fastfst_bcompaero_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nBlPitch_3__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitch_3__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_3_)



@given(instance=fastfst_nBlPitch_3__strategy)
def test_fastfst_nblpitch_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nBlPitch_3__strategy)
def test_fastfst_nblpitch_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bTwSSDOF2_strategy)
@settings(max_examples=50)
def test_fastfst_btwssdof2_instantiation(instance):
    assert isinstance(instance, fastfst_bTwSSDOF2)



@given(instance=fastfst_bTwSSDOF2_strategy)
def test_fastfst_btwssdof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bTwSSDOF2_strategy)
def test_fastfst_btwssdof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nBlPitch_2__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitch_2__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_2_)



@given(instance=fastfst_nBlPitch_2__strategy)
def test_fastfst_nblpitch_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitch_2__strategy)
def test_fastfst_nblpitch_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bTwSSDOF1_strategy)
@settings(max_examples=50)
def test_fastfst_btwssdof1_instantiation(instance):
    assert isinstance(instance, fastfst_bTwSSDOF1)



@given(instance=fastfst_bTwSSDOF1_strategy)
def test_fastfst_btwssdof1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bTwSSDOF1_strategy)
def test_fastfst_btwssdof1_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bTwFADOF2_strategy)
@settings(max_examples=50)
def test_fastfst_btwfadof2_instantiation(instance):
    assert isinstance(instance, fastfst_bTwFADOF2)



@given(instance=fastfst_bTwFADOF2_strategy)
def test_fastfst_btwfadof2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_bTwFADOF2_strategy)
def test_fastfst_btwfadof2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTPitManE_2__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmane_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_2_)



@given(instance=fastfst_nTPitManE_2__strategy)
def test_fastfst_ntpitmane_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManE_2__strategy)
def test_fastfst_ntpitmane_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTPitManE_1__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmane_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_1_)



@given(instance=fastfst_nTPitManE_1__strategy)
def test_fastfst_ntpitmane_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManE_1__strategy)
def test_fastfst_ntpitmane_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTPitManS_3__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmans_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_3_)



@given(instance=fastfst_nTPitManS_3__strategy)
def test_fastfst_ntpitmans_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManS_3__strategy)
def test_fastfst_ntpitmans_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTPitManS_2__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmans_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_2_)



@given(instance=fastfst_nTPitManS_2__strategy)
def test_fastfst_ntpitmans_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManS_2__strategy)
def test_fastfst_ntpitmans_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTPitManS_1__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmans_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManS_1_)



@given(instance=fastfst_nTPitManS_1__strategy)
def test_fastfst_ntpitmans_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTPitManS_1__strategy)
def test_fastfst_ntpitmans_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacYawF_strategy)
@settings(max_examples=50)
def test_fastfst_nnacyawf_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYawF)



@given(instance=fastfst_nNacYawF_strategy)
def test_fastfst_nnacyawf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYawF_strategy)
def test_fastfst_nnacyawf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTYawManE_strategy)
@settings(max_examples=50)
def test_fastfst_ntyawmane_instantiation(instance):
    assert isinstance(instance, fastfst_nTYawManE)



@given(instance=fastfst_nTYawManE_strategy)
def test_fastfst_ntyawmane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTYawManE_strategy)
def test_fastfst_ntyawmane_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTYawManS_strategy)
@settings(max_examples=50)
def test_fastfst_ntyawmans_instantiation(instance):
    assert isinstance(instance, fastfst_nTYawManS)



@given(instance=fastfst_nTYawManS_strategy)
def test_fastfst_ntyawmans_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTYawManS_strategy)
def test_fastfst_ntyawmans_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTBDepISp_3__strategy)
@settings(max_examples=50)
def test_fastfst_ntbdepisp_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_3_)



@given(instance=fastfst_nTBDepISp_3__strategy)
def test_fastfst_ntbdepisp_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTBDepISp_3__strategy)
def test_fastfst_ntbdepisp_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTBDepISp_2__strategy)
@settings(max_examples=50)
def test_fastfst_ntbdepisp_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_2_)



@given(instance=fastfst_nTBDepISp_2__strategy)
def test_fastfst_ntbdepisp_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDepISp_2__strategy)
def test_fastfst_ntbdepisp_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTBDepISp_1__strategy)
@settings(max_examples=50)
def test_fastfst_ntbdepisp_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTBDepISp_1_)



@given(instance=fastfst_nTBDepISp_1__strategy)
def test_fastfst_ntbdepisp_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTBDepISp_1__strategy)
def test_fastfst_ntbdepisp_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTTpBrDp_3__strategy)
@settings(max_examples=50)
def test_fastfst_nttpbrdp_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_3_)



@given(instance=fastfst_nTTpBrDp_3__strategy)
def test_fastfst_nttpbrdp_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTTpBrDp_3__strategy)
def test_fastfst_nttpbrdp_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTTpBrDp_2__strategy)
@settings(max_examples=50)
def test_fastfst_nttpbrdp_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_2_)



@given(instance=fastfst_nTTpBrDp_2__strategy)
def test_fastfst_nttpbrdp_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTTpBrDp_2__strategy)
def test_fastfst_nttpbrdp_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTTpBrDp_1__strategy)
@settings(max_examples=50)
def test_fastfst_nttpbrdp_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTTpBrDp_1_)



@given(instance=fastfst_nTTpBrDp_1__strategy)
def test_fastfst_nttpbrdp_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTTpBrDp_1__strategy)
def test_fastfst_nttpbrdp_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nBlPitch_1__strategy)
@settings(max_examples=50)
def test_fastfst_nblpitch_1__instantiation(instance):
    assert isinstance(instance, fastfst_nBlPitch_1_)



@given(instance=fastfst_nBlPitch_1__strategy)
def test_fastfst_nblpitch_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nBlPitch_1__strategy)
def test_fastfst_nblpitch_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTPitManE_3__strategy)
@settings(max_examples=50)
def test_fastfst_ntpitmane_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTPitManE_3_)



@given(instance=fastfst_nTPitManE_3__strategy)
def test_fastfst_ntpitmane_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPitManE_3__strategy)
def test_fastfst_ntpitmane_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iHSSBrMode_strategy)
@settings(max_examples=50)
def test_fastfst_ihssbrmode_instantiation(instance):
    assert isinstance(instance, fastfst_iHSSBrMode)



@given(instance=fastfst_iHSSBrMode_strategy)
def test_fastfst_ihssbrmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iHSSBrMode_strategy)
def test_fastfst_ihssbrmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTimGenOf_strategy)
@settings(max_examples=50)
def test_fastfst_ntimgenof_instantiation(instance):
    assert isinstance(instance, fastfst_nTimGenOf)



@given(instance=fastfst_nTimGenOf_strategy)
def test_fastfst_ntimgenof_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTimGenOf_strategy)
def test_fastfst_ntimgenof_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTimGenOn_strategy)
@settings(max_examples=50)
def test_fastfst_ntimgenon_instantiation(instance):
    assert isinstance(instance, fastfst_nTimGenOn)



@given(instance=fastfst_nTimGenOn_strategy)
def test_fastfst_ntimgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTimGenOn_strategy)
def test_fastfst_ntimgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nSpdGenOn_strategy)
@settings(max_examples=50)
def test_fastfst_nspdgenon_instantiation(instance):
    assert isinstance(instance, fastfst_nSpdGenOn)



@given(instance=fastfst_nSpdGenOn_strategy)
def test_fastfst_nspdgenon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nSpdGenOn_strategy)
def test_fastfst_nspdgenon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_bGenTiStp_strategy)
@settings(max_examples=50)
def test_fastfst_bgentistp_instantiation(instance):
    assert isinstance(instance, fastfst_bGenTiStp)



@given(instance=fastfst_bGenTiStp_strategy)
def test_fastfst_bgentistp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenTiStp_strategy)
def test_fastfst_bgentistp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bGenTiStr_strategy)
@settings(max_examples=50)
def test_fastfst_bgentistr_instantiation(instance):
    assert isinstance(instance, fastfst_bGenTiStr)



@given(instance=fastfst_bGenTiStr_strategy)
def test_fastfst_bgentistr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGenTiStr_strategy)
def test_fastfst_bgentistr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iGenModel_strategy)
@settings(max_examples=50)
def test_fastfst_igenmodel_instantiation(instance):
    assert isinstance(instance, fastfst_iGenModel)



@given(instance=fastfst_iGenModel_strategy)
def test_fastfst_igenmodel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iGenModel_strategy)
def test_fastfst_igenmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nVS_SlPc_strategy)
@settings(max_examples=50)
def test_fastfst_nvs_slpc_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_SlPc)



@given(instance=fastfst_nVS_SlPc_strategy)
def test_fastfst_nvs_slpc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_SlPc_strategy)
def test_fastfst_nvs_slpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nVS_Rgn2K_strategy)
@settings(max_examples=50)
def test_fastfst_nvs_rgn2k_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_Rgn2K)



@given(instance=fastfst_nVS_Rgn2K_strategy)
def test_fastfst_nvs_rgn2k_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_Rgn2K_strategy)
def test_fastfst_nvs_rgn2k_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nVS_RtTq_strategy)
@settings(max_examples=50)
def test_fastfst_nvs_rttq_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_RtTq)



@given(instance=fastfst_nVS_RtTq_strategy)
def test_fastfst_nvs_rttq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nVS_RtTq_strategy)
def test_fastfst_nvs_rttq_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nVS_RtGnSp_strategy)
@settings(max_examples=50)
def test_fastfst_nvs_rtgnsp_instantiation(instance):
    assert isinstance(instance, fastfst_nVS_RtGnSp)



@given(instance=fastfst_nVS_RtGnSp_strategy)
def test_fastfst_nvs_rtgnsp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nVS_RtGnSp_strategy)
def test_fastfst_nvs_rtgnsp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iVSContrl_strategy)
@settings(max_examples=50)
def test_fastfst_ivscontrl_instantiation(instance):
    assert isinstance(instance, fastfst_iVSContrl)



@given(instance=fastfst_iVSContrl_strategy)
def test_fastfst_ivscontrl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_iVSContrl_strategy)
def test_fastfst_ivscontrl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTPCOn_strategy)
@settings(max_examples=50)
def test_fastfst_ntpcon_instantiation(instance):
    assert isinstance(instance, fastfst_nTPCOn)



@given(instance=fastfst_nTPCOn_strategy)
def test_fastfst_ntpcon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTPCOn_strategy)
def test_fastfst_ntpcon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iPCMode_strategy)
@settings(max_examples=50)
def test_fastfst_ipcmode_instantiation(instance):
    assert isinstance(instance, fastfst_iPCMode)



@given(instance=fastfst_iPCMode_strategy)
def test_fastfst_ipcmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iPCMode_strategy)
def test_fastfst_ipcmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTYCOn_strategy)
@settings(max_examples=50)
def test_fastfst_ntycon_instantiation(instance):
    assert isinstance(instance, fastfst_nTYCOn)



@given(instance=fastfst_nTYCOn_strategy)
def test_fastfst_ntycon_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTYCOn_strategy)
def test_fastfst_ntycon_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_iYCMode_strategy)
@settings(max_examples=50)
def test_fastfst_iycmode_instantiation(instance):
    assert isinstance(instance, fastfst_iYCMode)



@given(instance=fastfst_iYCMode_strategy)
def test_fastfst_iycmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iYCMode_strategy)
def test_fastfst_iycmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nDT_strategy)
@settings(max_examples=50)
def test_fastfst_ndt_instantiation(instance):
    assert isinstance(instance, fastfst_nDT)



@given(instance=fastfst_nDT_strategy)
def test_fastfst_ndt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nDT_strategy)
def test_fastfst_ndt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTMax_strategy)
@settings(max_examples=50)
def test_fastfst_ntmax_instantiation(instance):
    assert isinstance(instance, fastfst_nTMax)



@given(instance=fastfst_nTMax_strategy)
def test_fastfst_ntmax_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTMax_strategy)
def test_fastfst_ntmax_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTiDynBrk_strategy)
@settings(max_examples=50)
def test_fastfst_ntidynbrk_instantiation(instance):
    assert isinstance(instance, fastfst_nTiDynBrk)



@given(instance=fastfst_nTiDynBrk_strategy)
def test_fastfst_ntidynbrk_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTiDynBrk_strategy)
def test_fastfst_ntidynbrk_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTHSSBrDp_strategy)
@settings(max_examples=50)
def test_fastfst_nthssbrdp_instantiation(instance):
    assert isinstance(instance, fastfst_nTHSSBrDp)



@given(instance=fastfst_nTHSSBrDp_strategy)
def test_fastfst_nthssbrdp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTHSSBrDp_strategy)
def test_fastfst_nthssbrdp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_iADAMSPrep_strategy)
@settings(max_examples=50)
def test_fastfst_iadamsprep_instantiation(instance):
    assert isinstance(instance, fastfst_iADAMSPrep)



@given(instance=fastfst_iADAMSPrep_strategy)
def test_fastfst_iadamsprep_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iADAMSPrep_strategy)
def test_fastfst_iadamsprep_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bEcho_strategy)
@settings(max_examples=50)
def test_fastfst_becho_instantiation(instance):
    assert isinstance(instance, fastfst_bEcho)



@given(instance=fastfst_bEcho_strategy)
def test_fastfst_becho_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bEcho_strategy)
def test_fastfst_becho_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_Section_strategy)
@settings(max_examples=50)
def test_fastfst_section_instantiation(instance):
    assert isinstance(instance, fastfst_Section)



@given(instance=fastfst_Section_strategy)
def test_fastfst_section_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_Header_strategy)
@settings(max_examples=50)
def test_fastfst_header_instantiation(instance):
    assert isinstance(instance, fastfst_Header)



@given(instance=fastfst_Header_strategy)
def test_fastfst_header_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=fastfst_ModelFastfst_strategy)
@settings(max_examples=50)
def test_fastfst_modelfastfst_instantiation(instance):
    assert isinstance(instance, fastfst_ModelFastfst)

@given(instance=fastfst_iNumBl_strategy)
@settings(max_examples=50)
def test_fastfst_inumbl_instantiation(instance):
    assert isinstance(instance, fastfst_iNumBl)



@given(instance=fastfst_iNumBl_strategy)
def test_fastfst_inumbl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iNumBl_strategy)
def test_fastfst_inumbl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_iAnalMode_strategy)
@settings(max_examples=50)
def test_fastfst_ianalmode_instantiation(instance):
    assert isinstance(instance, fastfst_iAnalMode)



@given(instance=fastfst_iAnalMode_strategy)
def test_fastfst_ianalmode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_iAnalMode_strategy)
def test_fastfst_ianalmode_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nHSSBrDT_strategy)
@settings(max_examples=50)
def test_fastfst_nhssbrdt_instantiation(instance):
    assert isinstance(instance, fastfst_nHSSBrDT)



@given(instance=fastfst_nHSSBrDT_strategy)
def test_fastfst_nhssbrdt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHSSBrDT_strategy)
def test_fastfst_nhssbrdt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nHSSBrTqF_strategy)
@settings(max_examples=50)
def test_fastfst_nhssbrtqf_instantiation(instance):
    assert isinstance(instance, fastfst_nHSSBrTqF)



@given(instance=fastfst_nHSSBrTqF_strategy)
def test_fastfst_nhssbrtqf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHSSBrTqF_strategy)
def test_fastfst_nhssbrtqf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_bGBRevers_strategy)
@settings(max_examples=50)
def test_fastfst_bgbrevers_instantiation(instance):
    assert isinstance(instance, fastfst_bGBRevers)



@given(instance=fastfst_bGBRevers_strategy)
def test_fastfst_bgbrevers_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_bGBRevers_strategy)
def test_fastfst_bgbrevers_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nGBRatio_strategy)
@settings(max_examples=50)
def test_fastfst_ngbratio_instantiation(instance):
    assert isinstance(instance, fastfst_nGBRatio)



@given(instance=fastfst_nGBRatio_strategy)
def test_fastfst_ngbratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGBRatio_strategy)
def test_fastfst_ngbratio_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nGenEff_strategy)
@settings(max_examples=50)
def test_fastfst_ngeneff_instantiation(instance):
    assert isinstance(instance, fastfst_nGenEff)



@given(instance=fastfst_nGenEff_strategy)
def test_fastfst_ngeneff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nGenEff_strategy)
def test_fastfst_ngeneff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nGBoxEff_strategy)
@settings(max_examples=50)
def test_fastfst_ngboxeff_instantiation(instance):
    assert isinstance(instance, fastfst_nGBoxEff)



@given(instance=fastfst_nGBoxEff_strategy)
def test_fastfst_ngboxeff_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nGBoxEff_strategy)
def test_fastfst_ngboxeff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nHubIner_strategy)
@settings(max_examples=50)
def test_fastfst_nhubiner_instantiation(instance):
    assert isinstance(instance, fastfst_nHubIner)



@given(instance=fastfst_nHubIner_strategy)
def test_fastfst_nhubiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubIner_strategy)
def test_fastfst_nhubiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nPreCone_2__strategy)
@settings(max_examples=50)
def test_fastfst_nprecone_2__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_2_)



@given(instance=fastfst_nPreCone_2__strategy)
def test_fastfst_nprecone_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nPreCone_2__strategy)
def test_fastfst_nprecone_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacYIner_strategy)
@settings(max_examples=50)
def test_fastfst_nnacyiner_instantiation(instance):
    assert isinstance(instance, fastfst_nNacYIner)



@given(instance=fastfst_nNacYIner_strategy)
def test_fastfst_nnacyiner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nNacYIner_strategy)
def test_fastfst_nnacyiner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTipMass_3__strategy)
@settings(max_examples=50)
def test_fastfst_ntipmass_3__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_3_)



@given(instance=fastfst_nTipMass_3__strategy)
def test_fastfst_ntipmass_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nTipMass_3__strategy)
def test_fastfst_ntipmass_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nTipMass_2__strategy)
@settings(max_examples=50)
def test_fastfst_ntipmass_2__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_2_)



@given(instance=fastfst_nTipMass_2__strategy)
def test_fastfst_ntipmass_2__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipMass_2__strategy)
def test_fastfst_ntipmass_2__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTipMass_1__strategy)
@settings(max_examples=50)
def test_fastfst_ntipmass_1__instantiation(instance):
    assert isinstance(instance, fastfst_nTipMass_1_)



@given(instance=fastfst_nTipMass_1__strategy)
def test_fastfst_ntipmass_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTipMass_1__strategy)
def test_fastfst_ntipmass_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nHubMass_strategy)
@settings(max_examples=50)
def test_fastfst_nhubmass_instantiation(instance):
    assert isinstance(instance, fastfst_nHubMass)



@given(instance=fastfst_nHubMass_strategy)
def test_fastfst_nhubmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nHubMass_strategy)
def test_fastfst_nhubmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacMass_strategy)
@settings(max_examples=50)
def test_fastfst_nnacmass_instantiation(instance):
    assert isinstance(instance, fastfst_nNacMass)



@given(instance=fastfst_nNacMass_strategy)
def test_fastfst_nnacmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNacMass_strategy)
def test_fastfst_nnacmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nYawBrMass_strategy)
@settings(max_examples=50)
def test_fastfst_nyawbrmass_instantiation(instance):
    assert isinstance(instance, fastfst_nYawBrMass)



@given(instance=fastfst_nYawBrMass_strategy)
def test_fastfst_nyawbrmass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nYawBrMass_strategy)
def test_fastfst_nyawbrmass_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nAzimB1Up_strategy)
@settings(max_examples=50)
def test_fastfst_nazimb1up_instantiation(instance):
    assert isinstance(instance, fastfst_nAzimB1Up)



@given(instance=fastfst_nAzimB1Up_strategy)
def test_fastfst_nazimb1up_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nAzimB1Up_strategy)
def test_fastfst_nazimb1up_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nPreCone_3__strategy)
@settings(max_examples=50)
def test_fastfst_nprecone_3__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_3_)



@given(instance=fastfst_nPreCone_3__strategy)
def test_fastfst_nprecone_3__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nPreCone_3__strategy)
def test_fastfst_nprecone_3__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nNacCMxn_strategy)
@settings(max_examples=50)
def test_fastfst_nnaccmxn_instantiation(instance):
    assert isinstance(instance, fastfst_nNacCMxn)



@given(instance=fastfst_nNacCMxn_strategy)
def test_fastfst_nnaccmxn_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fastfst_nNacCMxn_strategy)
def test_fastfst_nnaccmxn_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fastfst_nOverHang_strategy)
@settings(max_examples=50)
def test_fastfst_noverhang_instantiation(instance):
    assert isinstance(instance, fastfst_nOverHang)



@given(instance=fastfst_nOverHang_strategy)
def test_fastfst_noverhang_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nOverHang_strategy)
def test_fastfst_noverhang_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nHubCM_strategy)
@settings(max_examples=50)
def test_fastfst_nhubcm_instantiation(instance):
    assert isinstance(instance, fastfst_nHubCM)



@given(instance=fastfst_nHubCM_strategy)
def test_fastfst_nhubcm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nHubCM_strategy)
def test_fastfst_nhubcm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nPreCone_1__strategy)
@settings(max_examples=50)
def test_fastfst_nprecone_1__instantiation(instance):
    assert isinstance(instance, fastfst_nPreCone_1_)



@given(instance=fastfst_nPreCone_1__strategy)
def test_fastfst_nprecone_1__name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nPreCone_1__strategy)
def test_fastfst_nprecone_1__value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nDelta3_strategy)
@settings(max_examples=50)
def test_fastfst_ndelta3_instantiation(instance):
    assert isinstance(instance, fastfst_nDelta3)



@given(instance=fastfst_nDelta3_strategy)
def test_fastfst_ndelta3_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nDelta3_strategy)
def test_fastfst_ndelta3_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nShftTilt_strategy)
@settings(max_examples=50)
def test_fastfst_nshfttilt_instantiation(instance):
    assert isinstance(instance, fastfst_nShftTilt)



@given(instance=fastfst_nShftTilt_strategy)
def test_fastfst_nshfttilt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nShftTilt_strategy)
def test_fastfst_nshfttilt_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fastfst_nTwrRBHt_strategy)
@settings(max_examples=50)
def test_fastfst_ntwrrbht_instantiation(instance):
    assert isinstance(instance, fastfst_nTwrRBHt)



@given(instance=fastfst_nTwrRBHt_strategy)
def test_fastfst_ntwrrbht_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fastfst_nTwrRBHt_strategy)
def test_fastfst_ntwrrbht_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

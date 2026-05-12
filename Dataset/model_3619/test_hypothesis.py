import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    r2_XP,
    QSET,
    r2_IVL,
    IVL,
    r2_IVLINT,
    r2_IVLTS,
    r2_IVLCO,
    r2_IVLQTY,
    r2_IVLREAL,
    r2_IVLPQ,
    r2_HXIT,
    r2_EObject,
    QTY,
    r2_INT,
    r2_TS,
    r2_PIVLTS,
    r2_PQ,
    r2_RTO,
    r2_REAL,
    r2_CO,
    HXIT,
    r2_ANY,
    XP,
    r2_ENXP,
    ANY,
    r2_CS,
    r2_TEL,
    r2_QSET,
    r2_II,
    r2_CD,
    r2_BL,
    r2_ED,
    r2_QTY,
    r2_EN,
    r2_ST,
    r2_AD,
    r2_ADXP,
    CalendarCycle,
    EntityNamePartQualifier,
    TelecommunicationCapability,
    EntityNamePartType,
    TelecommunicationAddressUse,
    IntegrityCheckAlgorithm,
    PostalAddressUse,
    EntityNameUse,
    Compression,
    AddressPartType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_r2_xp_is_not_abstract():
    assert not inspect.isabstract(r2_XP)


def test_r2_xp_constructor_exists():
    assert callable(r2_XP.__init__)


def test_r2_xp_constructor_args():
    sig = inspect.signature(r2_XP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_xp_has_value():
    assert hasattr(r2_XP, "value")
    descriptor = None
    for klass in r2_XP.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_qset_is_not_abstract():
    assert not inspect.isabstract(QSET)


def test_qset_constructor_exists():
    assert callable(QSET.__init__)


def test_qset_constructor_args():
    sig = inspect.signature(QSET.__init__)
    params = list(sig.parameters.keys())



def test_r2_ivl_is_not_abstract():
    assert not inspect.isabstract(r2_IVL)


def test_r2_ivl_constructor_exists():
    assert callable(r2_IVL.__init__)


def test_r2_ivl_constructor_args():
    sig = inspect.signature(r2_IVL.__init__)
    params = list(sig.parameters.keys())



def test_ivl_is_not_abstract():
    assert not inspect.isabstract(IVL)


def test_ivl_constructor_exists():
    assert callable(IVL.__init__)


def test_ivl_constructor_args():
    sig = inspect.signature(IVL.__init__)
    params = list(sig.parameters.keys())



def test_r2_ivlint_is_not_abstract():
    assert not inspect.isabstract(r2_IVLINT)


def test_r2_ivlint_constructor_exists():
    assert callable(r2_IVLINT.__init__)


def test_r2_ivlint_constructor_args():
    sig = inspect.signature(r2_IVLINT.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2_ivlint_has_lowClosed():
    assert hasattr(r2_IVLINT, "lowClosed")
    descriptor = None
    for klass in r2_IVLINT.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlint_has_highClosed():
    assert hasattr(r2_IVLINT, "highClosed")
    descriptor = None
    for klass in r2_IVLINT.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_ivlts_is_not_abstract():
    assert not inspect.isabstract(r2_IVLTS)


def test_r2_ivlts_constructor_exists():
    assert callable(r2_IVLTS.__init__)


def test_r2_ivlts_constructor_args():
    sig = inspect.signature(r2_IVLTS.__init__)
    params = list(sig.parameters.keys())
    assert "highClosed" in params, "Missing parameter 'highClosed'"
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"

def test_r2_ivlts_has_highClosed():
    assert hasattr(r2_IVLTS, "highClosed")
    descriptor = None
    for klass in r2_IVLTS.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlts_has_lowClosed():
    assert hasattr(r2_IVLTS, "lowClosed")
    descriptor = None
    for klass in r2_IVLTS.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_ivlco_is_not_abstract():
    assert not inspect.isabstract(r2_IVLCO)


def test_r2_ivlco_constructor_exists():
    assert callable(r2_IVLCO.__init__)


def test_r2_ivlco_constructor_args():
    sig = inspect.signature(r2_IVLCO.__init__)
    params = list(sig.parameters.keys())
    assert "highClosed" in params, "Missing parameter 'highClosed'"
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"

def test_r2_ivlco_has_highClosed():
    assert hasattr(r2_IVLCO, "highClosed")
    descriptor = None
    for klass in r2_IVLCO.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlco_has_lowClosed():
    assert hasattr(r2_IVLCO, "lowClosed")
    descriptor = None
    for klass in r2_IVLCO.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_ivlqty_is_not_abstract():
    assert not inspect.isabstract(r2_IVLQTY)


def test_r2_ivlqty_constructor_exists():
    assert callable(r2_IVLQTY.__init__)


def test_r2_ivlqty_constructor_args():
    sig = inspect.signature(r2_IVLQTY.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2_ivlqty_has_lowClosed():
    assert hasattr(r2_IVLQTY, "lowClosed")
    descriptor = None
    for klass in r2_IVLQTY.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlqty_has_highClosed():
    assert hasattr(r2_IVLQTY, "highClosed")
    descriptor = None
    for klass in r2_IVLQTY.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_ivlreal_is_not_abstract():
    assert not inspect.isabstract(r2_IVLREAL)


def test_r2_ivlreal_constructor_exists():
    assert callable(r2_IVLREAL.__init__)


def test_r2_ivlreal_constructor_args():
    sig = inspect.signature(r2_IVLREAL.__init__)
    params = list(sig.parameters.keys())
    assert "highClosed" in params, "Missing parameter 'highClosed'"
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"

def test_r2_ivlreal_has_highClosed():
    assert hasattr(r2_IVLREAL, "highClosed")
    descriptor = None
    for klass in r2_IVLREAL.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlreal_has_lowClosed():
    assert hasattr(r2_IVLREAL, "lowClosed")
    descriptor = None
    for klass in r2_IVLREAL.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_ivlpq_is_not_abstract():
    assert not inspect.isabstract(r2_IVLPQ)


def test_r2_ivlpq_constructor_exists():
    assert callable(r2_IVLPQ.__init__)


def test_r2_ivlpq_constructor_args():
    sig = inspect.signature(r2_IVLPQ.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2_ivlpq_has_lowClosed():
    assert hasattr(r2_IVLPQ, "lowClosed")
    descriptor = None
    for klass in r2_IVLPQ.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2_ivlpq_has_highClosed():
    assert hasattr(r2_IVLPQ, "highClosed")
    descriptor = None
    for klass in r2_IVLPQ.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2_hxit_is_not_abstract():
    assert not inspect.isabstract(r2_HXIT)


def test_r2_hxit_constructor_exists():
    assert callable(r2_HXIT.__init__)


def test_r2_hxit_constructor_args():
    sig = inspect.signature(r2_HXIT.__init__)
    params = list(sig.parameters.keys())



def test_r2_eobject_is_not_abstract():
    assert not inspect.isabstract(r2_EObject)


def test_r2_eobject_constructor_exists():
    assert callable(r2_EObject.__init__)


def test_r2_eobject_constructor_args():
    sig = inspect.signature(r2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_qty_is_not_abstract():
    assert not inspect.isabstract(QTY)


def test_qty_constructor_exists():
    assert callable(QTY.__init__)


def test_qty_constructor_args():
    sig = inspect.signature(QTY.__init__)
    params = list(sig.parameters.keys())



def test_r2_int_is_not_abstract():
    assert not inspect.isabstract(r2_INT)


def test_r2_int_constructor_exists():
    assert callable(r2_INT.__init__)


def test_r2_int_constructor_args():
    sig = inspect.signature(r2_INT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_int_has_value():
    assert hasattr(r2_INT, "value")
    descriptor = None
    for klass in r2_INT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_ts_is_not_abstract():
    assert not inspect.isabstract(r2_TS)


def test_r2_ts_constructor_exists():
    assert callable(r2_TS.__init__)


def test_r2_ts_constructor_args():
    sig = inspect.signature(r2_TS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_ts_has_value():
    assert hasattr(r2_TS, "value")
    descriptor = None
    for klass in r2_TS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_pivlts_is_not_abstract():
    assert not inspect.isabstract(r2_PIVLTS)


def test_r2_pivlts_constructor_exists():
    assert callable(r2_PIVLTS.__init__)


def test_r2_pivlts_constructor_args():
    sig = inspect.signature(r2_PIVLTS.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "isFlexible" in params, "Missing parameter 'isFlexible'"

def test_r2_pivlts_has_alignment():
    assert hasattr(r2_PIVLTS, "alignment")
    descriptor = None
    for klass in r2_PIVLTS.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_r2_pivlts_has_isFlexible():
    assert hasattr(r2_PIVLTS, "isFlexible")
    descriptor = None
    for klass in r2_PIVLTS.__mro__:
        if "isFlexible" in klass.__dict__:
            descriptor = klass.__dict__["isFlexible"]
            break
    assert isinstance(descriptor, property)



def test_r2_pq_is_not_abstract():
    assert not inspect.isabstract(r2_PQ)


def test_r2_pq_constructor_exists():
    assert callable(r2_PQ.__init__)


def test_r2_pq_constructor_args():
    sig = inspect.signature(r2_PQ.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_r2_pq_has_unit():
    assert hasattr(r2_PQ, "unit")
    descriptor = None
    for klass in r2_PQ.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_r2_pq_has_value():
    assert hasattr(r2_PQ, "value")
    descriptor = None
    for klass in r2_PQ.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_rto_is_not_abstract():
    assert not inspect.isabstract(r2_RTO)


def test_r2_rto_constructor_exists():
    assert callable(r2_RTO.__init__)


def test_r2_rto_constructor_args():
    sig = inspect.signature(r2_RTO.__init__)
    params = list(sig.parameters.keys())



def test_r2_real_is_not_abstract():
    assert not inspect.isabstract(r2_REAL)


def test_r2_real_constructor_exists():
    assert callable(r2_REAL.__init__)


def test_r2_real_constructor_args():
    sig = inspect.signature(r2_REAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_real_has_value():
    assert hasattr(r2_REAL, "value")
    descriptor = None
    for klass in r2_REAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_co_is_not_abstract():
    assert not inspect.isabstract(r2_CO)


def test_r2_co_constructor_exists():
    assert callable(r2_CO.__init__)


def test_r2_co_constructor_args():
    sig = inspect.signature(r2_CO.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_co_has_value():
    assert hasattr(r2_CO, "value")
    descriptor = None
    for klass in r2_CO.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hxit_is_not_abstract():
    assert not inspect.isabstract(HXIT)


def test_hxit_constructor_exists():
    assert callable(HXIT.__init__)


def test_hxit_constructor_args():
    sig = inspect.signature(HXIT.__init__)
    params = list(sig.parameters.keys())



def test_r2_any_is_not_abstract():
    assert not inspect.isabstract(r2_ANY)


def test_r2_any_constructor_exists():
    assert callable(r2_ANY.__init__)


def test_r2_any_constructor_args():
    sig = inspect.signature(r2_ANY.__init__)
    params = list(sig.parameters.keys())



def test_xp_is_not_abstract():
    assert not inspect.isabstract(XP)


def test_xp_constructor_exists():
    assert callable(XP.__init__)


def test_xp_constructor_args():
    sig = inspect.signature(XP.__init__)
    params = list(sig.parameters.keys())



def test_r2_enxp_is_not_abstract():
    assert not inspect.isabstract(r2_ENXP)


def test_r2_enxp_constructor_exists():
    assert callable(r2_ENXP.__init__)


def test_r2_enxp_constructor_args():
    sig = inspect.signature(r2_ENXP.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_r2_enxp_has_type():
    assert hasattr(r2_ENXP, "type")
    descriptor = None
    for klass in r2_ENXP.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_r2_enxp_has_qualifier():
    assert hasattr(r2_ENXP, "qualifier")
    descriptor = None
    for klass in r2_ENXP.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_any_is_not_abstract():
    assert not inspect.isabstract(ANY)


def test_any_constructor_exists():
    assert callable(ANY.__init__)


def test_any_constructor_args():
    sig = inspect.signature(ANY.__init__)
    params = list(sig.parameters.keys())



def test_r2_cs_is_not_abstract():
    assert not inspect.isabstract(r2_CS)


def test_r2_cs_constructor_exists():
    assert callable(r2_CS.__init__)


def test_r2_cs_constructor_args():
    sig = inspect.signature(r2_CS.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_r2_cs_has_code():
    assert hasattr(r2_CS, "code")
    descriptor = None
    for klass in r2_CS.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_r2_tel_is_not_abstract():
    assert not inspect.isabstract(r2_TEL)


def test_r2_tel_constructor_exists():
    assert callable(r2_TEL.__init__)


def test_r2_tel_constructor_args():
    sig = inspect.signature(r2_TEL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "use" in params, "Missing parameter 'use'"
    assert "capabilities" in params, "Missing parameter 'capabilities'"

def test_r2_tel_has_value():
    assert hasattr(r2_TEL, "value")
    descriptor = None
    for klass in r2_TEL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_r2_tel_has_use():
    assert hasattr(r2_TEL, "use")
    descriptor = None
    for klass in r2_TEL.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_r2_tel_has_capabilities():
    assert hasattr(r2_TEL, "capabilities")
    descriptor = None
    for klass in r2_TEL.__mro__:
        if "capabilities" in klass.__dict__:
            descriptor = klass.__dict__["capabilities"]
            break
    assert isinstance(descriptor, property)



def test_r2_qset_is_not_abstract():
    assert not inspect.isabstract(r2_QSET)


def test_r2_qset_constructor_exists():
    assert callable(r2_QSET.__init__)


def test_r2_qset_constructor_args():
    sig = inspect.signature(r2_QSET.__init__)
    params = list(sig.parameters.keys())



def test_r2_ii_is_not_abstract():
    assert not inspect.isabstract(r2_II)


def test_r2_ii_constructor_exists():
    assert callable(r2_II.__init__)


def test_r2_ii_constructor_args():
    sig = inspect.signature(r2_II.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "identifierName" in params, "Missing parameter 'identifierName'"
    assert "root" in params, "Missing parameter 'root'"

def test_r2_ii_has_extension():
    assert hasattr(r2_II, "extension")
    descriptor = None
    for klass in r2_II.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_r2_ii_has_identifierName():
    assert hasattr(r2_II, "identifierName")
    descriptor = None
    for klass in r2_II.__mro__:
        if "identifierName" in klass.__dict__:
            descriptor = klass.__dict__["identifierName"]
            break
    assert isinstance(descriptor, property)

def test_r2_ii_has_root():
    assert hasattr(r2_II, "root")
    descriptor = None
    for klass in r2_II.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_r2_cd_is_not_abstract():
    assert not inspect.isabstract(r2_CD)


def test_r2_cd_constructor_exists():
    assert callable(r2_CD.__init__)


def test_r2_cd_constructor_args():
    sig = inspect.signature(r2_CD.__init__)
    params = list(sig.parameters.keys())
    assert "valueSet" in params, "Missing parameter 'valueSet'"
    assert "code" in params, "Missing parameter 'code'"
    assert "codeSystemVersion" in params, "Missing parameter 'codeSystemVersion'"
    assert "codeSystem" in params, "Missing parameter 'codeSystem'"
    assert "valueSetVersion" in params, "Missing parameter 'valueSetVersion'"
    assert "codeSystemName" in params, "Missing parameter 'codeSystemName'"

def test_r2_cd_has_valueSet():
    assert hasattr(r2_CD, "valueSet")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "valueSet" in klass.__dict__:
            descriptor = klass.__dict__["valueSet"]
            break
    assert isinstance(descriptor, property)

def test_r2_cd_has_code():
    assert hasattr(r2_CD, "code")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_r2_cd_has_codeSystemVersion():
    assert hasattr(r2_CD, "codeSystemVersion")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "codeSystemVersion" in klass.__dict__:
            descriptor = klass.__dict__["codeSystemVersion"]
            break
    assert isinstance(descriptor, property)

def test_r2_cd_has_codeSystem():
    assert hasattr(r2_CD, "codeSystem")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "codeSystem" in klass.__dict__:
            descriptor = klass.__dict__["codeSystem"]
            break
    assert isinstance(descriptor, property)

def test_r2_cd_has_valueSetVersion():
    assert hasattr(r2_CD, "valueSetVersion")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "valueSetVersion" in klass.__dict__:
            descriptor = klass.__dict__["valueSetVersion"]
            break
    assert isinstance(descriptor, property)

def test_r2_cd_has_codeSystemName():
    assert hasattr(r2_CD, "codeSystemName")
    descriptor = None
    for klass in r2_CD.__mro__:
        if "codeSystemName" in klass.__dict__:
            descriptor = klass.__dict__["codeSystemName"]
            break
    assert isinstance(descriptor, property)



def test_r2_bl_is_not_abstract():
    assert not inspect.isabstract(r2_BL)


def test_r2_bl_constructor_exists():
    assert callable(r2_BL.__init__)


def test_r2_bl_constructor_args():
    sig = inspect.signature(r2_BL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_bl_has_value():
    assert hasattr(r2_BL, "value")
    descriptor = None
    for klass in r2_BL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_ed_is_not_abstract():
    assert not inspect.isabstract(r2_ED)


def test_r2_ed_constructor_exists():
    assert callable(r2_ED.__init__)


def test_r2_ed_constructor_args():
    sig = inspect.signature(r2_ED.__init__)
    params = list(sig.parameters.keys())
    assert "compression" in params, "Missing parameter 'compression'"
    assert "value" in params, "Missing parameter 'value'"
    assert "integrityCheck" in params, "Missing parameter 'integrityCheck'"
    assert "mediaType" in params, "Missing parameter 'mediaType'"
    assert "language" in params, "Missing parameter 'language'"
    assert "charset" in params, "Missing parameter 'charset'"
    assert "integrityCheckAlgorithm" in params, "Missing parameter 'integrityCheckAlgorithm'"
    assert "data" in params, "Missing parameter 'data'"

def test_r2_ed_has_compression():
    assert hasattr(r2_ED, "compression")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "compression" in klass.__dict__:
            descriptor = klass.__dict__["compression"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_value():
    assert hasattr(r2_ED, "value")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_integrityCheck():
    assert hasattr(r2_ED, "integrityCheck")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "integrityCheck" in klass.__dict__:
            descriptor = klass.__dict__["integrityCheck"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_mediaType():
    assert hasattr(r2_ED, "mediaType")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "mediaType" in klass.__dict__:
            descriptor = klass.__dict__["mediaType"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_language():
    assert hasattr(r2_ED, "language")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_charset():
    assert hasattr(r2_ED, "charset")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "charset" in klass.__dict__:
            descriptor = klass.__dict__["charset"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_integrityCheckAlgorithm():
    assert hasattr(r2_ED, "integrityCheckAlgorithm")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "integrityCheckAlgorithm" in klass.__dict__:
            descriptor = klass.__dict__["integrityCheckAlgorithm"]
            break
    assert isinstance(descriptor, property)

def test_r2_ed_has_data():
    assert hasattr(r2_ED, "data")
    descriptor = None
    for klass in r2_ED.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_r2_qty_is_not_abstract():
    assert not inspect.isabstract(r2_QTY)


def test_r2_qty_constructor_exists():
    assert callable(r2_QTY.__init__)


def test_r2_qty_constructor_args():
    sig = inspect.signature(r2_QTY.__init__)
    params = list(sig.parameters.keys())



def test_r2_en_is_not_abstract():
    assert not inspect.isabstract(r2_EN)


def test_r2_en_constructor_exists():
    assert callable(r2_EN.__init__)


def test_r2_en_constructor_args():
    sig = inspect.signature(r2_EN.__init__)
    params = list(sig.parameters.keys())
    assert "use" in params, "Missing parameter 'use'"

def test_r2_en_has_use():
    assert hasattr(r2_EN, "use")
    descriptor = None
    for klass in r2_EN.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_r2_st_is_not_abstract():
    assert not inspect.isabstract(r2_ST)


def test_r2_st_constructor_exists():
    assert callable(r2_ST.__init__)


def test_r2_st_constructor_args():
    sig = inspect.signature(r2_ST.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2_st_has_value():
    assert hasattr(r2_ST, "value")
    descriptor = None
    for klass in r2_ST.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2_ad_is_not_abstract():
    assert not inspect.isabstract(r2_AD)


def test_r2_ad_constructor_exists():
    assert callable(r2_AD.__init__)


def test_r2_ad_constructor_args():
    sig = inspect.signature(r2_AD.__init__)
    params = list(sig.parameters.keys())
    assert "use" in params, "Missing parameter 'use'"

def test_r2_ad_has_use():
    assert hasattr(r2_AD, "use")
    descriptor = None
    for klass in r2_AD.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_r2_adxp_is_not_abstract():
    assert not inspect.isabstract(r2_ADXP)


def test_r2_adxp_constructor_exists():
    assert callable(r2_ADXP.__init__)


def test_r2_adxp_constructor_args():
    sig = inspect.signature(r2_ADXP.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_r2_adxp_has_type():
    assert hasattr(r2_ADXP, "type")
    descriptor = None
    for klass in r2_ADXP.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_calendarcycle_exists():
    # Check that the Enumeration exists
    assert CalendarCycle is not None

def test_calendarcycle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalendarCycle]
    expected_literals = [
        "DW",
        "HD",
        "MY",
        "CS",
        "CW",
        "CN",
        "DY",
        "SN",
        "CH",
        "NH",
        "DM",
        "WM",
        "CY",
        "WY",
        "CD",
        "CM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalendarCycle"

def test_entitynamepartqualifier_exists():
    # Check that the Enumeration exists
    assert EntityNamePartQualifier is not None

def test_entitynamepartqualifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNamePartQualifier]
    expected_literals = [
        "SFX",
        "PFX",
        "HON",
        "LS",
        "NB",
        "IN",
        "AC",
        "PR",
        "SP",
        "BR",
        "AD",
        "CL",
        "MID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNamePartQualifier"

def test_telecommunicationcapability_exists():
    # Check that the Enumeration exists
    assert TelecommunicationCapability is not None

def test_telecommunicationcapability_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TelecommunicationCapability]
    expected_literals = [
        "tty",
        "voice",
        "fax",
        "data",
        "sms",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TelecommunicationCapability"

def test_entitynameparttype_exists():
    # Check that the Enumeration exists
    assert EntityNamePartType is not None

def test_entitynameparttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNamePartType]
    expected_literals = [
        "TITLE",
        "DEL",
        "FAM",
        "GIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNamePartType"

def test_telecommunicationaddressuse_exists():
    # Check that the Enumeration exists
    assert TelecommunicationAddressUse is not None

def test_telecommunicationaddressuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TelecommunicationAddressUse]
    expected_literals = [
        "HP",
        "EC",
        "BAD",
        "H",
        "TMP",
        "MC",
        "WP",
        "DIR",
        "AS",
        "PG",
        "PUB",
        "HV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TelecommunicationAddressUse"

def test_integritycheckalgorithm_exists():
    # Check that the Enumeration exists
    assert IntegrityCheckAlgorithm is not None

def test_integritycheckalgorithm_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegrityCheckAlgorithm]
    expected_literals = [
        "SHA256",
        "SHA1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegrityCheckAlgorithm"

def test_postaladdressuse_exists():
    # Check that the Enumeration exists
    assert PostalAddressUse is not None

def test_postaladdressuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostalAddressUse]
    expected_literals = [
        "TMP",
        "H",
        "SYL",
        "WP",
        "BAD",
        "PHON",
        "PST",
        "IDE",
        "DIR",
        "SNDX",
        "HV",
        "PUB",
        "ABC",
        "PHYS",
        "SRCH",
        "HP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostalAddressUse"

def test_entitynameuse_exists():
    # Check that the Enumeration exists
    assert EntityNameUse is not None

def test_entitynameuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNameUse]
    expected_literals = [
        "IDE",
        "ANON",
        "PHON",
        "SYL",
        "P",
        "R",
        "T",
        "OLD",
        "I",
        "M",
        "A",
        "SRCH",
        "OR",
        "DN",
        "C",
        "ABC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNameUse"

def test_compression_exists():
    # Check that the Enumeration exists
    assert Compression is not None

def test_compression_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compression]
    expected_literals = [
        "Z",
        "BZ",
        "ZL",
        "Z7",
        "DF",
        "GZ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Compression"

def test_addressparttype_exists():
    # Check that the Enumeration exists
    assert AddressPartType is not None

def test_addressparttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddressPartType]
    expected_literals = [
        "AL",
        "INT",
        "DMODID",
        "PRE",
        "DINSTA",
        "DMOD",
        "ADL",
        "CPA",
        "SAL",
        "DINSTQ",
        "STA",
        "DPID",
        "BNS",
        "CNT",
        "BNR",
        "BNN",
        "DEL",
        "CAR",
        "DIR",
        "ZIP",
        "STB",
        "CTY",
        "UNIT",
        "DAL",
        "UNID",
        "CEN",
        "DINST",
        "STTYP",
        "STR",
        "POB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddressPartType"


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
r2_XP_strategy = st.builds(
    r2_XP,
    value=
        safe_text
)
QSET_strategy = st.builds(
    QSET,
)
r2_IVL_strategy = st.builds(
    r2_IVL,
)
IVL_strategy = st.builds(
    IVL,
)
r2_IVLINT_strategy = st.builds(
    r2_IVLINT,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2_IVLTS_strategy = st.builds(
    r2_IVLTS,
    highClosed=
        safe_text,
    lowClosed=
        safe_text
)
r2_IVLCO_strategy = st.builds(
    r2_IVLCO,
    highClosed=
        safe_text,
    lowClosed=
        safe_text
)
r2_IVLQTY_strategy = st.builds(
    r2_IVLQTY,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2_IVLREAL_strategy = st.builds(
    r2_IVLREAL,
    highClosed=
        safe_text,
    lowClosed=
        safe_text
)
r2_IVLPQ_strategy = st.builds(
    r2_IVLPQ,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2_HXIT_strategy = st.builds(
    r2_HXIT,
)
r2_EObject_strategy = st.builds(
    r2_EObject,
)
QTY_strategy = st.builds(
    QTY,
)
r2_INT_strategy = st.builds(
    r2_INT,
    value=
        safe_text
)
r2_TS_strategy = st.builds(
    r2_TS,
    value=
        safe_text
)
r2_PIVLTS_strategy = st.builds(
    r2_PIVLTS,
    alignment=
        safe_text,
    isFlexible=
        safe_text
)
r2_PQ_strategy = st.builds(
    r2_PQ,
    unit=
        safe_text,
    value=
        safe_text
)
r2_RTO_strategy = st.builds(
    r2_RTO,
)
r2_REAL_strategy = st.builds(
    r2_REAL,
    value=
        safe_text
)
r2_CO_strategy = st.builds(
    r2_CO,
    value=
        safe_text
)
HXIT_strategy = st.builds(
    HXIT,
)
r2_ANY_strategy = st.builds(
    r2_ANY,
)
XP_strategy = st.builds(
    XP,
)
r2_ENXP_strategy = st.builds(
    r2_ENXP,
    type=
        safe_text,
    qualifier=
        safe_text
)
ANY_strategy = st.builds(
    ANY,
)
r2_CS_strategy = st.builds(
    r2_CS,
    code=
        safe_text
)
r2_TEL_strategy = st.builds(
    r2_TEL,
    value=
        safe_text,
    use=
        safe_text,
    capabilities=
        safe_text
)
r2_QSET_strategy = st.builds(
    r2_QSET,
)
r2_II_strategy = st.builds(
    r2_II,
    extension=
        safe_text,
    identifierName=
        safe_text,
    root=
        safe_text
)
r2_CD_strategy = st.builds(
    r2_CD,
    valueSet=
        safe_text,
    code=
        safe_text,
    codeSystemVersion=
        safe_text,
    codeSystem=
        safe_text,
    valueSetVersion=
        safe_text,
    codeSystemName=
        safe_text
)
r2_BL_strategy = st.builds(
    r2_BL,
    value=
        safe_text
)
r2_ED_strategy = st.builds(
    r2_ED,
    compression=
        safe_text,
    value=
        safe_text,
    integrityCheck=
        safe_text,
    mediaType=
        safe_text,
    language=
        safe_text,
    charset=
        safe_text,
    integrityCheckAlgorithm=
        safe_text,
    data=
        safe_text
)
r2_QTY_strategy = st.builds(
    r2_QTY,
)
r2_EN_strategy = st.builds(
    r2_EN,
    use=
        safe_text
)
r2_ST_strategy = st.builds(
    r2_ST,
    value=
        safe_text
)
r2_AD_strategy = st.builds(
    r2_AD,
    use=
        safe_text
)
r2_ADXP_strategy = st.builds(
    r2_ADXP,
    type=
        safe_text
)

@given(instance=r2_XP_strategy)
@settings(max_examples=50)
def test_r2_xp_instantiation(instance):
    assert isinstance(instance, r2_XP)



@given(instance=r2_XP_strategy)
def test_r2_xp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QSET_strategy)
@settings(max_examples=50)
def test_qset_instantiation(instance):
    assert isinstance(instance, QSET)

@given(instance=r2_IVL_strategy)
@settings(max_examples=50)
def test_r2_ivl_instantiation(instance):
    assert isinstance(instance, r2_IVL)

@given(instance=IVL_strategy)
@settings(max_examples=50)
def test_ivl_instantiation(instance):
    assert isinstance(instance, IVL)

@given(instance=r2_IVLINT_strategy)
@settings(max_examples=50)
def test_r2_ivlint_instantiation(instance):
    assert isinstance(instance, r2_IVLINT)



@given(instance=r2_IVLINT_strategy)
def test_r2_ivlint_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original



@given(instance=r2_IVLINT_strategy)
def test_r2_ivlint_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2_IVLTS_strategy)
@settings(max_examples=50)
def test_r2_ivlts_instantiation(instance):
    assert isinstance(instance, r2_IVLTS)



@given(instance=r2_IVLTS_strategy)
def test_r2_ivlts_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original



@given(instance=r2_IVLTS_strategy)
def test_r2_ivlts_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2_IVLCO_strategy)
@settings(max_examples=50)
def test_r2_ivlco_instantiation(instance):
    assert isinstance(instance, r2_IVLCO)



@given(instance=r2_IVLCO_strategy)
def test_r2_ivlco_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original



@given(instance=r2_IVLCO_strategy)
def test_r2_ivlco_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2_IVLQTY_strategy)
@settings(max_examples=50)
def test_r2_ivlqty_instantiation(instance):
    assert isinstance(instance, r2_IVLQTY)



@given(instance=r2_IVLQTY_strategy)
def test_r2_ivlqty_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original



@given(instance=r2_IVLQTY_strategy)
def test_r2_ivlqty_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2_IVLREAL_strategy)
@settings(max_examples=50)
def test_r2_ivlreal_instantiation(instance):
    assert isinstance(instance, r2_IVLREAL)



@given(instance=r2_IVLREAL_strategy)
def test_r2_ivlreal_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original



@given(instance=r2_IVLREAL_strategy)
def test_r2_ivlreal_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2_IVLPQ_strategy)
@settings(max_examples=50)
def test_r2_ivlpq_instantiation(instance):
    assert isinstance(instance, r2_IVLPQ)



@given(instance=r2_IVLPQ_strategy)
def test_r2_ivlpq_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original



@given(instance=r2_IVLPQ_strategy)
def test_r2_ivlpq_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2_HXIT_strategy)
@settings(max_examples=50)
def test_r2_hxit_instantiation(instance):
    assert isinstance(instance, r2_HXIT)

@given(instance=r2_EObject_strategy)
@settings(max_examples=50)
def test_r2_eobject_instantiation(instance):
    assert isinstance(instance, r2_EObject)

@given(instance=QTY_strategy)
@settings(max_examples=50)
def test_qty_instantiation(instance):
    assert isinstance(instance, QTY)

@given(instance=r2_INT_strategy)
@settings(max_examples=50)
def test_r2_int_instantiation(instance):
    assert isinstance(instance, r2_INT)



@given(instance=r2_INT_strategy)
def test_r2_int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_TS_strategy)
@settings(max_examples=50)
def test_r2_ts_instantiation(instance):
    assert isinstance(instance, r2_TS)



@given(instance=r2_TS_strategy)
def test_r2_ts_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_PIVLTS_strategy)
@settings(max_examples=50)
def test_r2_pivlts_instantiation(instance):
    assert isinstance(instance, r2_PIVLTS)



@given(instance=r2_PIVLTS_strategy)
def test_r2_pivlts_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original



@given(instance=r2_PIVLTS_strategy)
def test_r2_pivlts_isFlexible_setter(instance):
    original = instance.isFlexible
    instance.isFlexible = original
    assert instance.isFlexible == original

@given(instance=r2_PQ_strategy)
@settings(max_examples=50)
def test_r2_pq_instantiation(instance):
    assert isinstance(instance, r2_PQ)



@given(instance=r2_PQ_strategy)
def test_r2_pq_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=r2_PQ_strategy)
def test_r2_pq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_RTO_strategy)
@settings(max_examples=50)
def test_r2_rto_instantiation(instance):
    assert isinstance(instance, r2_RTO)

@given(instance=r2_REAL_strategy)
@settings(max_examples=50)
def test_r2_real_instantiation(instance):
    assert isinstance(instance, r2_REAL)



@given(instance=r2_REAL_strategy)
def test_r2_real_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_CO_strategy)
@settings(max_examples=50)
def test_r2_co_instantiation(instance):
    assert isinstance(instance, r2_CO)



@given(instance=r2_CO_strategy)
def test_r2_co_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HXIT_strategy)
@settings(max_examples=50)
def test_hxit_instantiation(instance):
    assert isinstance(instance, HXIT)

@given(instance=r2_ANY_strategy)
@settings(max_examples=50)
def test_r2_any_instantiation(instance):
    assert isinstance(instance, r2_ANY)

@given(instance=XP_strategy)
@settings(max_examples=50)
def test_xp_instantiation(instance):
    assert isinstance(instance, XP)

@given(instance=r2_ENXP_strategy)
@settings(max_examples=50)
def test_r2_enxp_instantiation(instance):
    assert isinstance(instance, r2_ENXP)



@given(instance=r2_ENXP_strategy)
def test_r2_enxp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=r2_ENXP_strategy)
def test_r2_enxp_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=ANY_strategy)
@settings(max_examples=50)
def test_any_instantiation(instance):
    assert isinstance(instance, ANY)

@given(instance=r2_CS_strategy)
@settings(max_examples=50)
def test_r2_cs_instantiation(instance):
    assert isinstance(instance, r2_CS)



@given(instance=r2_CS_strategy)
def test_r2_cs_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=r2_TEL_strategy)
@settings(max_examples=50)
def test_r2_tel_instantiation(instance):
    assert isinstance(instance, r2_TEL)



@given(instance=r2_TEL_strategy)
def test_r2_tel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=r2_TEL_strategy)
def test_r2_tel_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original



@given(instance=r2_TEL_strategy)
def test_r2_tel_capabilities_setter(instance):
    original = instance.capabilities
    instance.capabilities = original
    assert instance.capabilities == original

@given(instance=r2_QSET_strategy)
@settings(max_examples=50)
def test_r2_qset_instantiation(instance):
    assert isinstance(instance, r2_QSET)

@given(instance=r2_II_strategy)
@settings(max_examples=50)
def test_r2_ii_instantiation(instance):
    assert isinstance(instance, r2_II)



@given(instance=r2_II_strategy)
def test_r2_ii_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=r2_II_strategy)
def test_r2_ii_identifierName_setter(instance):
    original = instance.identifierName
    instance.identifierName = original
    assert instance.identifierName == original



@given(instance=r2_II_strategy)
def test_r2_ii_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=r2_CD_strategy)
@settings(max_examples=50)
def test_r2_cd_instantiation(instance):
    assert isinstance(instance, r2_CD)



@given(instance=r2_CD_strategy)
def test_r2_cd_valueSet_setter(instance):
    original = instance.valueSet
    instance.valueSet = original
    assert instance.valueSet == original



@given(instance=r2_CD_strategy)
def test_r2_cd_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=r2_CD_strategy)
def test_r2_cd_codeSystemVersion_setter(instance):
    original = instance.codeSystemVersion
    instance.codeSystemVersion = original
    assert instance.codeSystemVersion == original



@given(instance=r2_CD_strategy)
def test_r2_cd_codeSystem_setter(instance):
    original = instance.codeSystem
    instance.codeSystem = original
    assert instance.codeSystem == original



@given(instance=r2_CD_strategy)
def test_r2_cd_valueSetVersion_setter(instance):
    original = instance.valueSetVersion
    instance.valueSetVersion = original
    assert instance.valueSetVersion == original



@given(instance=r2_CD_strategy)
def test_r2_cd_codeSystemName_setter(instance):
    original = instance.codeSystemName
    instance.codeSystemName = original
    assert instance.codeSystemName == original

@given(instance=r2_BL_strategy)
@settings(max_examples=50)
def test_r2_bl_instantiation(instance):
    assert isinstance(instance, r2_BL)



@given(instance=r2_BL_strategy)
def test_r2_bl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_ED_strategy)
@settings(max_examples=50)
def test_r2_ed_instantiation(instance):
    assert isinstance(instance, r2_ED)



@given(instance=r2_ED_strategy)
def test_r2_ed_compression_setter(instance):
    original = instance.compression
    instance.compression = original
    assert instance.compression == original



@given(instance=r2_ED_strategy)
def test_r2_ed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=r2_ED_strategy)
def test_r2_ed_integrityCheck_setter(instance):
    original = instance.integrityCheck
    instance.integrityCheck = original
    assert instance.integrityCheck == original



@given(instance=r2_ED_strategy)
def test_r2_ed_mediaType_setter(instance):
    original = instance.mediaType
    instance.mediaType = original
    assert instance.mediaType == original



@given(instance=r2_ED_strategy)
def test_r2_ed_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=r2_ED_strategy)
def test_r2_ed_charset_setter(instance):
    original = instance.charset
    instance.charset = original
    assert instance.charset == original



@given(instance=r2_ED_strategy)
def test_r2_ed_integrityCheckAlgorithm_setter(instance):
    original = instance.integrityCheckAlgorithm
    instance.integrityCheckAlgorithm = original
    assert instance.integrityCheckAlgorithm == original



@given(instance=r2_ED_strategy)
def test_r2_ed_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=r2_QTY_strategy)
@settings(max_examples=50)
def test_r2_qty_instantiation(instance):
    assert isinstance(instance, r2_QTY)

@given(instance=r2_EN_strategy)
@settings(max_examples=50)
def test_r2_en_instantiation(instance):
    assert isinstance(instance, r2_EN)



@given(instance=r2_EN_strategy)
def test_r2_en_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=r2_ST_strategy)
@settings(max_examples=50)
def test_r2_st_instantiation(instance):
    assert isinstance(instance, r2_ST)



@given(instance=r2_ST_strategy)
def test_r2_st_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2_AD_strategy)
@settings(max_examples=50)
def test_r2_ad_instantiation(instance):
    assert isinstance(instance, r2_AD)



@given(instance=r2_AD_strategy)
def test_r2_ad_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=r2_ADXP_strategy)
@settings(max_examples=50)
def test_r2_adxp_instantiation(instance):
    assert isinstance(instance, r2_ADXP)



@given(instance=r2_ADXP_strategy)
def test_r2_adxp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

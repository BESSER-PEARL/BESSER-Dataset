import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    r2::XP,
    QSET,
    r2::IVL,
    IVL,
    r2::IVLREAL,
    r2::IVLCO,
    r2::IVLTS,
    r2::IVLQTY,
    r2::IVLPQ,
    r2::IVLINT,
    r2::HXIT,
    r2::EObject,
    QTY,
    r2::REAL,
    r2::PQ,
    r2::TS,
    r2::RTO,
    r2::PIVLTS,
    r2::INT,
    r2::CO,
    HXIT,
    r2::ANY,
    XP,
    r2::ENXP,
    ANY,
    r2::BL,
    r2::ED,
    r2::CD,
    r2::QSET,
    r2::CS,
    r2::ST,
    r2::II,
    r2::QTY,
    r2::TEL,
    r2::EN,
    r2::AD,
    r2::ADXP,
    Compression,
    IntegrityCheckAlgorithm,
    EntityNameUse,
    AddressPartType,
    EntityNamePartQualifier,
    CalendarCycle,
    TelecommunicationAddressUse,
    PostalAddressUse,
    EntityNamePartType,
    TelecommunicationCapability,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_r2::xp_is_not_abstract():
    assert not inspect.isabstract(r2::XP)


def test_r2::xp_constructor_exists():
    assert callable(r2::XP.__init__)


def test_r2::xp_constructor_args():
    sig = inspect.signature(r2::XP.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::xp_has_value():
    assert hasattr(r2::XP, "value")
    descriptor = None
    for klass in r2::XP.__mro__:
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



def test_r2::ivl_is_not_abstract():
    assert not inspect.isabstract(r2::IVL)


def test_r2::ivl_constructor_exists():
    assert callable(r2::IVL.__init__)


def test_r2::ivl_constructor_args():
    sig = inspect.signature(r2::IVL.__init__)
    params = list(sig.parameters.keys())



def test_ivl_is_not_abstract():
    assert not inspect.isabstract(IVL)


def test_ivl_constructor_exists():
    assert callable(IVL.__init__)


def test_ivl_constructor_args():
    sig = inspect.signature(IVL.__init__)
    params = list(sig.parameters.keys())



def test_r2::ivlreal_is_not_abstract():
    assert not inspect.isabstract(r2::IVLREAL)


def test_r2::ivlreal_constructor_exists():
    assert callable(r2::IVLREAL.__init__)


def test_r2::ivlreal_constructor_args():
    sig = inspect.signature(r2::IVLREAL.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2::ivlreal_has_lowClosed():
    assert hasattr(r2::IVLREAL, "lowClosed")
    descriptor = None
    for klass in r2::IVLREAL.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlreal_has_highClosed():
    assert hasattr(r2::IVLREAL, "highClosed")
    descriptor = None
    for klass in r2::IVLREAL.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::ivlco_is_not_abstract():
    assert not inspect.isabstract(r2::IVLCO)


def test_r2::ivlco_constructor_exists():
    assert callable(r2::IVLCO.__init__)


def test_r2::ivlco_constructor_args():
    sig = inspect.signature(r2::IVLCO.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2::ivlco_has_lowClosed():
    assert hasattr(r2::IVLCO, "lowClosed")
    descriptor = None
    for klass in r2::IVLCO.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlco_has_highClosed():
    assert hasattr(r2::IVLCO, "highClosed")
    descriptor = None
    for klass in r2::IVLCO.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::ivlts_is_not_abstract():
    assert not inspect.isabstract(r2::IVLTS)


def test_r2::ivlts_constructor_exists():
    assert callable(r2::IVLTS.__init__)


def test_r2::ivlts_constructor_args():
    sig = inspect.signature(r2::IVLTS.__init__)
    params = list(sig.parameters.keys())
    assert "highClosed" in params, "Missing parameter 'highClosed'"
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"

def test_r2::ivlts_has_highClosed():
    assert hasattr(r2::IVLTS, "highClosed")
    descriptor = None
    for klass in r2::IVLTS.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlts_has_lowClosed():
    assert hasattr(r2::IVLTS, "lowClosed")
    descriptor = None
    for klass in r2::IVLTS.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::ivlqty_is_not_abstract():
    assert not inspect.isabstract(r2::IVLQTY)


def test_r2::ivlqty_constructor_exists():
    assert callable(r2::IVLQTY.__init__)


def test_r2::ivlqty_constructor_args():
    sig = inspect.signature(r2::IVLQTY.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2::ivlqty_has_lowClosed():
    assert hasattr(r2::IVLQTY, "lowClosed")
    descriptor = None
    for klass in r2::IVLQTY.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlqty_has_highClosed():
    assert hasattr(r2::IVLQTY, "highClosed")
    descriptor = None
    for klass in r2::IVLQTY.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::ivlpq_is_not_abstract():
    assert not inspect.isabstract(r2::IVLPQ)


def test_r2::ivlpq_constructor_exists():
    assert callable(r2::IVLPQ.__init__)


def test_r2::ivlpq_constructor_args():
    sig = inspect.signature(r2::IVLPQ.__init__)
    params = list(sig.parameters.keys())
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"
    assert "highClosed" in params, "Missing parameter 'highClosed'"

def test_r2::ivlpq_has_lowClosed():
    assert hasattr(r2::IVLPQ, "lowClosed")
    descriptor = None
    for klass in r2::IVLPQ.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlpq_has_highClosed():
    assert hasattr(r2::IVLPQ, "highClosed")
    descriptor = None
    for klass in r2::IVLPQ.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::ivlint_is_not_abstract():
    assert not inspect.isabstract(r2::IVLINT)


def test_r2::ivlint_constructor_exists():
    assert callable(r2::IVLINT.__init__)


def test_r2::ivlint_constructor_args():
    sig = inspect.signature(r2::IVLINT.__init__)
    params = list(sig.parameters.keys())
    assert "highClosed" in params, "Missing parameter 'highClosed'"
    assert "lowClosed" in params, "Missing parameter 'lowClosed'"

def test_r2::ivlint_has_highClosed():
    assert hasattr(r2::IVLINT, "highClosed")
    descriptor = None
    for klass in r2::IVLINT.__mro__:
        if "highClosed" in klass.__dict__:
            descriptor = klass.__dict__["highClosed"]
            break
    assert isinstance(descriptor, property)

def test_r2::ivlint_has_lowClosed():
    assert hasattr(r2::IVLINT, "lowClosed")
    descriptor = None
    for klass in r2::IVLINT.__mro__:
        if "lowClosed" in klass.__dict__:
            descriptor = klass.__dict__["lowClosed"]
            break
    assert isinstance(descriptor, property)



def test_r2::hxit_is_not_abstract():
    assert not inspect.isabstract(r2::HXIT)


def test_r2::hxit_constructor_exists():
    assert callable(r2::HXIT.__init__)


def test_r2::hxit_constructor_args():
    sig = inspect.signature(r2::HXIT.__init__)
    params = list(sig.parameters.keys())



def test_r2::eobject_is_not_abstract():
    assert not inspect.isabstract(r2::EObject)


def test_r2::eobject_constructor_exists():
    assert callable(r2::EObject.__init__)


def test_r2::eobject_constructor_args():
    sig = inspect.signature(r2::EObject.__init__)
    params = list(sig.parameters.keys())



def test_qty_is_not_abstract():
    assert not inspect.isabstract(QTY)


def test_qty_constructor_exists():
    assert callable(QTY.__init__)


def test_qty_constructor_args():
    sig = inspect.signature(QTY.__init__)
    params = list(sig.parameters.keys())



def test_r2::real_is_not_abstract():
    assert not inspect.isabstract(r2::REAL)


def test_r2::real_constructor_exists():
    assert callable(r2::REAL.__init__)


def test_r2::real_constructor_args():
    sig = inspect.signature(r2::REAL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::real_has_value():
    assert hasattr(r2::REAL, "value")
    descriptor = None
    for klass in r2::REAL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::pq_is_not_abstract():
    assert not inspect.isabstract(r2::PQ)


def test_r2::pq_constructor_exists():
    assert callable(r2::PQ.__init__)


def test_r2::pq_constructor_args():
    sig = inspect.signature(r2::PQ.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_r2::pq_has_unit():
    assert hasattr(r2::PQ, "unit")
    descriptor = None
    for klass in r2::PQ.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_r2::pq_has_value():
    assert hasattr(r2::PQ, "value")
    descriptor = None
    for klass in r2::PQ.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::ts_is_not_abstract():
    assert not inspect.isabstract(r2::TS)


def test_r2::ts_constructor_exists():
    assert callable(r2::TS.__init__)


def test_r2::ts_constructor_args():
    sig = inspect.signature(r2::TS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::ts_has_value():
    assert hasattr(r2::TS, "value")
    descriptor = None
    for klass in r2::TS.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::rto_is_not_abstract():
    assert not inspect.isabstract(r2::RTO)


def test_r2::rto_constructor_exists():
    assert callable(r2::RTO.__init__)


def test_r2::rto_constructor_args():
    sig = inspect.signature(r2::RTO.__init__)
    params = list(sig.parameters.keys())



def test_r2::pivlts_is_not_abstract():
    assert not inspect.isabstract(r2::PIVLTS)


def test_r2::pivlts_constructor_exists():
    assert callable(r2::PIVLTS.__init__)


def test_r2::pivlts_constructor_args():
    sig = inspect.signature(r2::PIVLTS.__init__)
    params = list(sig.parameters.keys())
    assert "isFlexible" in params, "Missing parameter 'isFlexible'"
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_r2::pivlts_has_isFlexible():
    assert hasattr(r2::PIVLTS, "isFlexible")
    descriptor = None
    for klass in r2::PIVLTS.__mro__:
        if "isFlexible" in klass.__dict__:
            descriptor = klass.__dict__["isFlexible"]
            break
    assert isinstance(descriptor, property)

def test_r2::pivlts_has_alignment():
    assert hasattr(r2::PIVLTS, "alignment")
    descriptor = None
    for klass in r2::PIVLTS.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_r2::int_is_not_abstract():
    assert not inspect.isabstract(r2::INT)


def test_r2::int_constructor_exists():
    assert callable(r2::INT.__init__)


def test_r2::int_constructor_args():
    sig = inspect.signature(r2::INT.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::int_has_value():
    assert hasattr(r2::INT, "value")
    descriptor = None
    for klass in r2::INT.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::co_is_not_abstract():
    assert not inspect.isabstract(r2::CO)


def test_r2::co_constructor_exists():
    assert callable(r2::CO.__init__)


def test_r2::co_constructor_args():
    sig = inspect.signature(r2::CO.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::co_has_value():
    assert hasattr(r2::CO, "value")
    descriptor = None
    for klass in r2::CO.__mro__:
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



def test_r2::any_is_not_abstract():
    assert not inspect.isabstract(r2::ANY)


def test_r2::any_constructor_exists():
    assert callable(r2::ANY.__init__)


def test_r2::any_constructor_args():
    sig = inspect.signature(r2::ANY.__init__)
    params = list(sig.parameters.keys())



def test_xp_is_not_abstract():
    assert not inspect.isabstract(XP)


def test_xp_constructor_exists():
    assert callable(XP.__init__)


def test_xp_constructor_args():
    sig = inspect.signature(XP.__init__)
    params = list(sig.parameters.keys())



def test_r2::enxp_is_not_abstract():
    assert not inspect.isabstract(r2::ENXP)


def test_r2::enxp_constructor_exists():
    assert callable(r2::ENXP.__init__)


def test_r2::enxp_constructor_args():
    sig = inspect.signature(r2::ENXP.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "type" in params, "Missing parameter 'type'"

def test_r2::enxp_has_qualifier():
    assert hasattr(r2::ENXP, "qualifier")
    descriptor = None
    for klass in r2::ENXP.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_r2::enxp_has_type():
    assert hasattr(r2::ENXP, "type")
    descriptor = None
    for klass in r2::ENXP.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_any_is_not_abstract():
    assert not inspect.isabstract(ANY)


def test_any_constructor_exists():
    assert callable(ANY.__init__)


def test_any_constructor_args():
    sig = inspect.signature(ANY.__init__)
    params = list(sig.parameters.keys())



def test_r2::bl_is_not_abstract():
    assert not inspect.isabstract(r2::BL)


def test_r2::bl_constructor_exists():
    assert callable(r2::BL.__init__)


def test_r2::bl_constructor_args():
    sig = inspect.signature(r2::BL.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::bl_has_value():
    assert hasattr(r2::BL, "value")
    descriptor = None
    for klass in r2::BL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::ed_is_not_abstract():
    assert not inspect.isabstract(r2::ED)


def test_r2::ed_constructor_exists():
    assert callable(r2::ED.__init__)


def test_r2::ed_constructor_args():
    sig = inspect.signature(r2::ED.__init__)
    params = list(sig.parameters.keys())
    assert "integrityCheckAlgorithm" in params, "Missing parameter 'integrityCheckAlgorithm'"
    assert "integrityCheck" in params, "Missing parameter 'integrityCheck'"
    assert "compression" in params, "Missing parameter 'compression'"
    assert "language" in params, "Missing parameter 'language'"
    assert "mediaType" in params, "Missing parameter 'mediaType'"
    assert "charset" in params, "Missing parameter 'charset'"
    assert "value" in params, "Missing parameter 'value'"
    assert "data" in params, "Missing parameter 'data'"

def test_r2::ed_has_integrityCheckAlgorithm():
    assert hasattr(r2::ED, "integrityCheckAlgorithm")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "integrityCheckAlgorithm" in klass.__dict__:
            descriptor = klass.__dict__["integrityCheckAlgorithm"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_integrityCheck():
    assert hasattr(r2::ED, "integrityCheck")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "integrityCheck" in klass.__dict__:
            descriptor = klass.__dict__["integrityCheck"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_compression():
    assert hasattr(r2::ED, "compression")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "compression" in klass.__dict__:
            descriptor = klass.__dict__["compression"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_language():
    assert hasattr(r2::ED, "language")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_mediaType():
    assert hasattr(r2::ED, "mediaType")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "mediaType" in klass.__dict__:
            descriptor = klass.__dict__["mediaType"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_charset():
    assert hasattr(r2::ED, "charset")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "charset" in klass.__dict__:
            descriptor = klass.__dict__["charset"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_value():
    assert hasattr(r2::ED, "value")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_r2::ed_has_data():
    assert hasattr(r2::ED, "data")
    descriptor = None
    for klass in r2::ED.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_r2::cd_is_not_abstract():
    assert not inspect.isabstract(r2::CD)


def test_r2::cd_constructor_exists():
    assert callable(r2::CD.__init__)


def test_r2::cd_constructor_args():
    sig = inspect.signature(r2::CD.__init__)
    params = list(sig.parameters.keys())
    assert "codeSystemName" in params, "Missing parameter 'codeSystemName'"
    assert "valueSetVersion" in params, "Missing parameter 'valueSetVersion'"
    assert "codeSystemVersion" in params, "Missing parameter 'codeSystemVersion'"
    assert "code" in params, "Missing parameter 'code'"
    assert "codeSystem" in params, "Missing parameter 'codeSystem'"
    assert "valueSet" in params, "Missing parameter 'valueSet'"

def test_r2::cd_has_codeSystemName():
    assert hasattr(r2::CD, "codeSystemName")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "codeSystemName" in klass.__dict__:
            descriptor = klass.__dict__["codeSystemName"]
            break
    assert isinstance(descriptor, property)

def test_r2::cd_has_valueSetVersion():
    assert hasattr(r2::CD, "valueSetVersion")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "valueSetVersion" in klass.__dict__:
            descriptor = klass.__dict__["valueSetVersion"]
            break
    assert isinstance(descriptor, property)

def test_r2::cd_has_codeSystemVersion():
    assert hasattr(r2::CD, "codeSystemVersion")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "codeSystemVersion" in klass.__dict__:
            descriptor = klass.__dict__["codeSystemVersion"]
            break
    assert isinstance(descriptor, property)

def test_r2::cd_has_code():
    assert hasattr(r2::CD, "code")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_r2::cd_has_codeSystem():
    assert hasattr(r2::CD, "codeSystem")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "codeSystem" in klass.__dict__:
            descriptor = klass.__dict__["codeSystem"]
            break
    assert isinstance(descriptor, property)

def test_r2::cd_has_valueSet():
    assert hasattr(r2::CD, "valueSet")
    descriptor = None
    for klass in r2::CD.__mro__:
        if "valueSet" in klass.__dict__:
            descriptor = klass.__dict__["valueSet"]
            break
    assert isinstance(descriptor, property)



def test_r2::qset_is_not_abstract():
    assert not inspect.isabstract(r2::QSET)


def test_r2::qset_constructor_exists():
    assert callable(r2::QSET.__init__)


def test_r2::qset_constructor_args():
    sig = inspect.signature(r2::QSET.__init__)
    params = list(sig.parameters.keys())



def test_r2::cs_is_not_abstract():
    assert not inspect.isabstract(r2::CS)


def test_r2::cs_constructor_exists():
    assert callable(r2::CS.__init__)


def test_r2::cs_constructor_args():
    sig = inspect.signature(r2::CS.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_r2::cs_has_code():
    assert hasattr(r2::CS, "code")
    descriptor = None
    for klass in r2::CS.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_r2::st_is_not_abstract():
    assert not inspect.isabstract(r2::ST)


def test_r2::st_constructor_exists():
    assert callable(r2::ST.__init__)


def test_r2::st_constructor_args():
    sig = inspect.signature(r2::ST.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_r2::st_has_value():
    assert hasattr(r2::ST, "value")
    descriptor = None
    for klass in r2::ST.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::ii_is_not_abstract():
    assert not inspect.isabstract(r2::II)


def test_r2::ii_constructor_exists():
    assert callable(r2::II.__init__)


def test_r2::ii_constructor_args():
    sig = inspect.signature(r2::II.__init__)
    params = list(sig.parameters.keys())
    assert "identifierName" in params, "Missing parameter 'identifierName'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "root" in params, "Missing parameter 'root'"

def test_r2::ii_has_identifierName():
    assert hasattr(r2::II, "identifierName")
    descriptor = None
    for klass in r2::II.__mro__:
        if "identifierName" in klass.__dict__:
            descriptor = klass.__dict__["identifierName"]
            break
    assert isinstance(descriptor, property)

def test_r2::ii_has_extension():
    assert hasattr(r2::II, "extension")
    descriptor = None
    for klass in r2::II.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_r2::ii_has_root():
    assert hasattr(r2::II, "root")
    descriptor = None
    for klass in r2::II.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)



def test_r2::qty_is_not_abstract():
    assert not inspect.isabstract(r2::QTY)


def test_r2::qty_constructor_exists():
    assert callable(r2::QTY.__init__)


def test_r2::qty_constructor_args():
    sig = inspect.signature(r2::QTY.__init__)
    params = list(sig.parameters.keys())



def test_r2::tel_is_not_abstract():
    assert not inspect.isabstract(r2::TEL)


def test_r2::tel_constructor_exists():
    assert callable(r2::TEL.__init__)


def test_r2::tel_constructor_args():
    sig = inspect.signature(r2::TEL.__init__)
    params = list(sig.parameters.keys())
    assert "capabilities" in params, "Missing parameter 'capabilities'"
    assert "use" in params, "Missing parameter 'use'"
    assert "value" in params, "Missing parameter 'value'"

def test_r2::tel_has_capabilities():
    assert hasattr(r2::TEL, "capabilities")
    descriptor = None
    for klass in r2::TEL.__mro__:
        if "capabilities" in klass.__dict__:
            descriptor = klass.__dict__["capabilities"]
            break
    assert isinstance(descriptor, property)

def test_r2::tel_has_use():
    assert hasattr(r2::TEL, "use")
    descriptor = None
    for klass in r2::TEL.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_r2::tel_has_value():
    assert hasattr(r2::TEL, "value")
    descriptor = None
    for klass in r2::TEL.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_r2::en_is_not_abstract():
    assert not inspect.isabstract(r2::EN)


def test_r2::en_constructor_exists():
    assert callable(r2::EN.__init__)


def test_r2::en_constructor_args():
    sig = inspect.signature(r2::EN.__init__)
    params = list(sig.parameters.keys())
    assert "use" in params, "Missing parameter 'use'"

def test_r2::en_has_use():
    assert hasattr(r2::EN, "use")
    descriptor = None
    for klass in r2::EN.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_r2::ad_is_not_abstract():
    assert not inspect.isabstract(r2::AD)


def test_r2::ad_constructor_exists():
    assert callable(r2::AD.__init__)


def test_r2::ad_constructor_args():
    sig = inspect.signature(r2::AD.__init__)
    params = list(sig.parameters.keys())
    assert "use" in params, "Missing parameter 'use'"

def test_r2::ad_has_use():
    assert hasattr(r2::AD, "use")
    descriptor = None
    for klass in r2::AD.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)



def test_r2::adxp_is_not_abstract():
    assert not inspect.isabstract(r2::ADXP)


def test_r2::adxp_constructor_exists():
    assert callable(r2::ADXP.__init__)


def test_r2::adxp_constructor_args():
    sig = inspect.signature(r2::ADXP.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_r2::adxp_has_type():
    assert hasattr(r2::ADXP, "type")
    descriptor = None
    for klass in r2::ADXP.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_compression_exists():
    # Check that the Enumeration exists
    assert Compression is not None

def test_compression_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Compression]
    expected_literals = [
        "BZ",
        "ZL",
        "Z",
        "DF",
        "Z7",
        "GZ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Compression"

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

def test_entitynameuse_exists():
    # Check that the Enumeration exists
    assert EntityNameUse is not None

def test_entitynameuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNameUse]
    expected_literals = [
        "DN",
        "SRCH",
        "ANON",
        "R",
        "OLD",
        "T",
        "I",
        "PHON",
        "M",
        "OR",
        "IDE",
        "P",
        "SYL",
        "A",
        "C",
        "ABC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNameUse"

def test_addressparttype_exists():
    # Check that the Enumeration exists
    assert AddressPartType is not None

def test_addressparttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddressPartType]
    expected_literals = [
        "BNN",
        "SAL",
        "DAL",
        "STR",
        "CPA",
        "DINSTA",
        "DPID",
        "ZIP",
        "BNR",
        "DINST",
        "STA",
        "DMOD",
        "PRE",
        "BNS",
        "AL",
        "UNID",
        "POB",
        "STTYP",
        "CNT",
        "ADL",
        "CTY",
        "INT",
        "DIR",
        "CEN",
        "DMODID",
        "STB",
        "DINSTQ",
        "CAR",
        "UNIT",
        "DEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddressPartType"

def test_entitynamepartqualifier_exists():
    # Check that the Enumeration exists
    assert EntityNamePartQualifier is not None

def test_entitynamepartqualifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNamePartQualifier]
    expected_literals = [
        "IN",
        "LS",
        "MID",
        "CL",
        "AD",
        "AC",
        "NB",
        "SFX",
        "BR",
        "PR",
        "SP",
        "HON",
        "PFX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNamePartQualifier"

def test_calendarcycle_exists():
    # Check that the Enumeration exists
    assert CalendarCycle is not None

def test_calendarcycle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalendarCycle]
    expected_literals = [
        "CW",
        "SN",
        "CD",
        "WM",
        "NH",
        "WY",
        "DM",
        "CM",
        "CH",
        "DY",
        "HD",
        "MY",
        "CS",
        "CY",
        "DW",
        "CN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalendarCycle"

def test_telecommunicationaddressuse_exists():
    # Check that the Enumeration exists
    assert TelecommunicationAddressUse is not None

def test_telecommunicationaddressuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TelecommunicationAddressUse]
    expected_literals = [
        "WP",
        "EC",
        "PG",
        "HP",
        "DIR",
        "H",
        "HV",
        "BAD",
        "MC",
        "TMP",
        "AS",
        "PUB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TelecommunicationAddressUse"

def test_postaladdressuse_exists():
    # Check that the Enumeration exists
    assert PostalAddressUse is not None

def test_postaladdressuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostalAddressUse]
    expected_literals = [
        "SYL",
        "SNDX",
        "HV",
        "HP",
        "H",
        "PST",
        "IDE",
        "TMP",
        "DIR",
        "PUB",
        "BAD",
        "PHON",
        "ABC",
        "PHYS",
        "SRCH",
        "WP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostalAddressUse"

def test_entitynameparttype_exists():
    # Check that the Enumeration exists
    assert EntityNamePartType is not None

def test_entitynameparttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityNamePartType]
    expected_literals = [
        "FAM",
        "TITLE",
        "GIV",
        "DEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityNamePartType"

def test_telecommunicationcapability_exists():
    # Check that the Enumeration exists
    assert TelecommunicationCapability is not None

def test_telecommunicationcapability_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TelecommunicationCapability]
    expected_literals = [
        "tty",
        "sms",
        "fax",
        "voice",
        "data",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TelecommunicationCapability"


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
r2::XP_strategy = st.builds(
    r2::XP,
    value=
        safe_text
)
QSET_strategy = st.builds(
    QSET,
)
r2::IVL_strategy = st.builds(
    r2::IVL,
)
IVL_strategy = st.builds(
    IVL,
)
r2::IVLREAL_strategy = st.builds(
    r2::IVLREAL,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2::IVLCO_strategy = st.builds(
    r2::IVLCO,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2::IVLTS_strategy = st.builds(
    r2::IVLTS,
    highClosed=
        safe_text,
    lowClosed=
        safe_text
)
r2::IVLQTY_strategy = st.builds(
    r2::IVLQTY,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2::IVLPQ_strategy = st.builds(
    r2::IVLPQ,
    lowClosed=
        safe_text,
    highClosed=
        safe_text
)
r2::IVLINT_strategy = st.builds(
    r2::IVLINT,
    highClosed=
        safe_text,
    lowClosed=
        safe_text
)
r2::HXIT_strategy = st.builds(
    r2::HXIT,
)
r2::EObject_strategy = st.builds(
    r2::EObject,
)
QTY_strategy = st.builds(
    QTY,
)
r2::REAL_strategy = st.builds(
    r2::REAL,
    value=
        safe_text
)
r2::PQ_strategy = st.builds(
    r2::PQ,
    unit=
        safe_text,
    value=
        safe_text
)
r2::TS_strategy = st.builds(
    r2::TS,
    value=
        safe_text
)
r2::RTO_strategy = st.builds(
    r2::RTO,
)
r2::PIVLTS_strategy = st.builds(
    r2::PIVLTS,
    isFlexible=
        safe_text,
    alignment=
        safe_text
)
r2::INT_strategy = st.builds(
    r2::INT,
    value=
        safe_text
)
r2::CO_strategy = st.builds(
    r2::CO,
    value=
        safe_text
)
HXIT_strategy = st.builds(
    HXIT,
)
r2::ANY_strategy = st.builds(
    r2::ANY,
)
XP_strategy = st.builds(
    XP,
)
r2::ENXP_strategy = st.builds(
    r2::ENXP,
    qualifier=
        safe_text,
    type=
        safe_text
)
ANY_strategy = st.builds(
    ANY,
)
r2::BL_strategy = st.builds(
    r2::BL,
    value=
        safe_text
)
r2::ED_strategy = st.builds(
    r2::ED,
    integrityCheckAlgorithm=
        safe_text,
    integrityCheck=
        safe_text,
    compression=
        safe_text,
    language=
        safe_text,
    mediaType=
        safe_text,
    charset=
        safe_text,
    value=
        safe_text,
    data=
        safe_text
)
r2::CD_strategy = st.builds(
    r2::CD,
    codeSystemName=
        safe_text,
    valueSetVersion=
        safe_text,
    codeSystemVersion=
        safe_text,
    code=
        safe_text,
    codeSystem=
        safe_text,
    valueSet=
        safe_text
)
r2::QSET_strategy = st.builds(
    r2::QSET,
)
r2::CS_strategy = st.builds(
    r2::CS,
    code=
        safe_text
)
r2::ST_strategy = st.builds(
    r2::ST,
    value=
        safe_text
)
r2::II_strategy = st.builds(
    r2::II,
    identifierName=
        safe_text,
    extension=
        safe_text,
    root=
        safe_text
)
r2::QTY_strategy = st.builds(
    r2::QTY,
)
r2::TEL_strategy = st.builds(
    r2::TEL,
    capabilities=
        safe_text,
    use=
        safe_text,
    value=
        safe_text
)
r2::EN_strategy = st.builds(
    r2::EN,
    use=
        safe_text
)
r2::AD_strategy = st.builds(
    r2::AD,
    use=
        safe_text
)
r2::ADXP_strategy = st.builds(
    r2::ADXP,
    type=
        safe_text
)

@given(instance=r2::XP_strategy)
@settings(max_examples=50)
def test_r2::xp_instantiation(instance):
    assert isinstance(instance, r2::XP)

@given(instance=r2::XP_strategy)
def test_r2::xp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::XP_strategy)
def test_r2::xp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=QSET_strategy)
@settings(max_examples=50)
def test_qset_instantiation(instance):
    assert isinstance(instance, QSET)

@given(instance=r2::IVL_strategy)
@settings(max_examples=50)
def test_r2::ivl_instantiation(instance):
    assert isinstance(instance, r2::IVL)

@given(instance=IVL_strategy)
@settings(max_examples=50)
def test_ivl_instantiation(instance):
    assert isinstance(instance, IVL)

@given(instance=r2::IVLREAL_strategy)
@settings(max_examples=50)
def test_r2::ivlreal_instantiation(instance):
    assert isinstance(instance, r2::IVLREAL)

@given(instance=r2::IVLREAL_strategy)
def test_r2::ivlreal_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLREAL_strategy)
def test_r2::ivlreal_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::IVLREAL_strategy)
def test_r2::ivlreal_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLREAL_strategy)
def test_r2::ivlreal_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLCO_strategy)
@settings(max_examples=50)
def test_r2::ivlco_instantiation(instance):
    assert isinstance(instance, r2::IVLCO)

@given(instance=r2::IVLCO_strategy)
def test_r2::ivlco_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLCO_strategy)
def test_r2::ivlco_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::IVLCO_strategy)
def test_r2::ivlco_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLCO_strategy)
def test_r2::ivlco_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLTS_strategy)
@settings(max_examples=50)
def test_r2::ivlts_instantiation(instance):
    assert isinstance(instance, r2::IVLTS)

@given(instance=r2::IVLTS_strategy)
def test_r2::ivlts_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLTS_strategy)
def test_r2::ivlts_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLTS_strategy)
def test_r2::ivlts_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLTS_strategy)
def test_r2::ivlts_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::IVLQTY_strategy)
@settings(max_examples=50)
def test_r2::ivlqty_instantiation(instance):
    assert isinstance(instance, r2::IVLQTY)

@given(instance=r2::IVLQTY_strategy)
def test_r2::ivlqty_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLQTY_strategy)
def test_r2::ivlqty_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::IVLQTY_strategy)
def test_r2::ivlqty_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLQTY_strategy)
def test_r2::ivlqty_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLPQ_strategy)
@settings(max_examples=50)
def test_r2::ivlpq_instantiation(instance):
    assert isinstance(instance, r2::IVLPQ)

@given(instance=r2::IVLPQ_strategy)
def test_r2::ivlpq_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLPQ_strategy)
def test_r2::ivlpq_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::IVLPQ_strategy)
def test_r2::ivlpq_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLPQ_strategy)
def test_r2::ivlpq_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLINT_strategy)
@settings(max_examples=50)
def test_r2::ivlint_instantiation(instance):
    assert isinstance(instance, r2::IVLINT)

@given(instance=r2::IVLINT_strategy)
def test_r2::ivlint_highClosed_type(instance):
    assert isinstance(instance.highClosed, str)


@given(instance=r2::IVLINT_strategy)
def test_r2::ivlint_highClosed_setter(instance):
    original = instance.highClosed
    instance.highClosed = original
    assert instance.highClosed == original

@given(instance=r2::IVLINT_strategy)
def test_r2::ivlint_lowClosed_type(instance):
    assert isinstance(instance.lowClosed, str)


@given(instance=r2::IVLINT_strategy)
def test_r2::ivlint_lowClosed_setter(instance):
    original = instance.lowClosed
    instance.lowClosed = original
    assert instance.lowClosed == original

@given(instance=r2::HXIT_strategy)
@settings(max_examples=50)
def test_r2::hxit_instantiation(instance):
    assert isinstance(instance, r2::HXIT)

@given(instance=r2::EObject_strategy)
@settings(max_examples=50)
def test_r2::eobject_instantiation(instance):
    assert isinstance(instance, r2::EObject)

@given(instance=QTY_strategy)
@settings(max_examples=50)
def test_qty_instantiation(instance):
    assert isinstance(instance, QTY)

@given(instance=r2::REAL_strategy)
@settings(max_examples=50)
def test_r2::real_instantiation(instance):
    assert isinstance(instance, r2::REAL)

@given(instance=r2::REAL_strategy)
def test_r2::real_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::REAL_strategy)
def test_r2::real_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::PQ_strategy)
@settings(max_examples=50)
def test_r2::pq_instantiation(instance):
    assert isinstance(instance, r2::PQ)

@given(instance=r2::PQ_strategy)
def test_r2::pq_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=r2::PQ_strategy)
def test_r2::pq_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=r2::PQ_strategy)
def test_r2::pq_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::PQ_strategy)
def test_r2::pq_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::TS_strategy)
@settings(max_examples=50)
def test_r2::ts_instantiation(instance):
    assert isinstance(instance, r2::TS)

@given(instance=r2::TS_strategy)
def test_r2::ts_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::TS_strategy)
def test_r2::ts_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::RTO_strategy)
@settings(max_examples=50)
def test_r2::rto_instantiation(instance):
    assert isinstance(instance, r2::RTO)

@given(instance=r2::PIVLTS_strategy)
@settings(max_examples=50)
def test_r2::pivlts_instantiation(instance):
    assert isinstance(instance, r2::PIVLTS)

@given(instance=r2::PIVLTS_strategy)
def test_r2::pivlts_isFlexible_type(instance):
    assert isinstance(instance.isFlexible, str)


@given(instance=r2::PIVLTS_strategy)
def test_r2::pivlts_isFlexible_setter(instance):
    original = instance.isFlexible
    instance.isFlexible = original
    assert instance.isFlexible == original

@given(instance=r2::PIVLTS_strategy)
def test_r2::pivlts_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=r2::PIVLTS_strategy)
def test_r2::pivlts_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=r2::INT_strategy)
@settings(max_examples=50)
def test_r2::int_instantiation(instance):
    assert isinstance(instance, r2::INT)

@given(instance=r2::INT_strategy)
def test_r2::int_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::INT_strategy)
def test_r2::int_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::CO_strategy)
@settings(max_examples=50)
def test_r2::co_instantiation(instance):
    assert isinstance(instance, r2::CO)

@given(instance=r2::CO_strategy)
def test_r2::co_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::CO_strategy)
def test_r2::co_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HXIT_strategy)
@settings(max_examples=50)
def test_hxit_instantiation(instance):
    assert isinstance(instance, HXIT)

@given(instance=r2::ANY_strategy)
@settings(max_examples=50)
def test_r2::any_instantiation(instance):
    assert isinstance(instance, r2::ANY)

@given(instance=XP_strategy)
@settings(max_examples=50)
def test_xp_instantiation(instance):
    assert isinstance(instance, XP)

@given(instance=r2::ENXP_strategy)
@settings(max_examples=50)
def test_r2::enxp_instantiation(instance):
    assert isinstance(instance, r2::ENXP)

@given(instance=r2::ENXP_strategy)
def test_r2::enxp_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=r2::ENXP_strategy)
def test_r2::enxp_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=r2::ENXP_strategy)
def test_r2::enxp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=r2::ENXP_strategy)
def test_r2::enxp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ANY_strategy)
@settings(max_examples=50)
def test_any_instantiation(instance):
    assert isinstance(instance, ANY)

@given(instance=r2::BL_strategy)
@settings(max_examples=50)
def test_r2::bl_instantiation(instance):
    assert isinstance(instance, r2::BL)

@given(instance=r2::BL_strategy)
def test_r2::bl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::BL_strategy)
def test_r2::bl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::ED_strategy)
@settings(max_examples=50)
def test_r2::ed_instantiation(instance):
    assert isinstance(instance, r2::ED)

@given(instance=r2::ED_strategy)
def test_r2::ed_integrityCheckAlgorithm_type(instance):
    assert isinstance(instance.integrityCheckAlgorithm, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_integrityCheckAlgorithm_setter(instance):
    original = instance.integrityCheckAlgorithm
    instance.integrityCheckAlgorithm = original
    assert instance.integrityCheckAlgorithm == original

@given(instance=r2::ED_strategy)
def test_r2::ed_integrityCheck_type(instance):
    assert isinstance(instance.integrityCheck, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_integrityCheck_setter(instance):
    original = instance.integrityCheck
    instance.integrityCheck = original
    assert instance.integrityCheck == original

@given(instance=r2::ED_strategy)
def test_r2::ed_compression_type(instance):
    assert isinstance(instance.compression, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_compression_setter(instance):
    original = instance.compression
    instance.compression = original
    assert instance.compression == original

@given(instance=r2::ED_strategy)
def test_r2::ed_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=r2::ED_strategy)
def test_r2::ed_mediaType_type(instance):
    assert isinstance(instance.mediaType, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_mediaType_setter(instance):
    original = instance.mediaType
    instance.mediaType = original
    assert instance.mediaType == original

@given(instance=r2::ED_strategy)
def test_r2::ed_charset_type(instance):
    assert isinstance(instance.charset, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_charset_setter(instance):
    original = instance.charset
    instance.charset = original
    assert instance.charset == original

@given(instance=r2::ED_strategy)
def test_r2::ed_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::ED_strategy)
def test_r2::ed_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=r2::ED_strategy)
def test_r2::ed_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=r2::CD_strategy)
@settings(max_examples=50)
def test_r2::cd_instantiation(instance):
    assert isinstance(instance, r2::CD)

@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystemName_type(instance):
    assert isinstance(instance.codeSystemName, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystemName_setter(instance):
    original = instance.codeSystemName
    instance.codeSystemName = original
    assert instance.codeSystemName == original

@given(instance=r2::CD_strategy)
def test_r2::cd_valueSetVersion_type(instance):
    assert isinstance(instance.valueSetVersion, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_valueSetVersion_setter(instance):
    original = instance.valueSetVersion
    instance.valueSetVersion = original
    assert instance.valueSetVersion == original

@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystemVersion_type(instance):
    assert isinstance(instance.codeSystemVersion, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystemVersion_setter(instance):
    original = instance.codeSystemVersion
    instance.codeSystemVersion = original
    assert instance.codeSystemVersion == original

@given(instance=r2::CD_strategy)
def test_r2::cd_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystem_type(instance):
    assert isinstance(instance.codeSystem, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_codeSystem_setter(instance):
    original = instance.codeSystem
    instance.codeSystem = original
    assert instance.codeSystem == original

@given(instance=r2::CD_strategy)
def test_r2::cd_valueSet_type(instance):
    assert isinstance(instance.valueSet, str)


@given(instance=r2::CD_strategy)
def test_r2::cd_valueSet_setter(instance):
    original = instance.valueSet
    instance.valueSet = original
    assert instance.valueSet == original

@given(instance=r2::QSET_strategy)
@settings(max_examples=50)
def test_r2::qset_instantiation(instance):
    assert isinstance(instance, r2::QSET)

@given(instance=r2::CS_strategy)
@settings(max_examples=50)
def test_r2::cs_instantiation(instance):
    assert isinstance(instance, r2::CS)

@given(instance=r2::CS_strategy)
def test_r2::cs_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=r2::CS_strategy)
def test_r2::cs_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=r2::ST_strategy)
@settings(max_examples=50)
def test_r2::st_instantiation(instance):
    assert isinstance(instance, r2::ST)

@given(instance=r2::ST_strategy)
def test_r2::st_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::ST_strategy)
def test_r2::st_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::II_strategy)
@settings(max_examples=50)
def test_r2::ii_instantiation(instance):
    assert isinstance(instance, r2::II)

@given(instance=r2::II_strategy)
def test_r2::ii_identifierName_type(instance):
    assert isinstance(instance.identifierName, str)


@given(instance=r2::II_strategy)
def test_r2::ii_identifierName_setter(instance):
    original = instance.identifierName
    instance.identifierName = original
    assert instance.identifierName == original

@given(instance=r2::II_strategy)
def test_r2::ii_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=r2::II_strategy)
def test_r2::ii_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=r2::II_strategy)
def test_r2::ii_root_type(instance):
    assert isinstance(instance.root, str)


@given(instance=r2::II_strategy)
def test_r2::ii_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=r2::QTY_strategy)
@settings(max_examples=50)
def test_r2::qty_instantiation(instance):
    assert isinstance(instance, r2::QTY)

@given(instance=r2::TEL_strategy)
@settings(max_examples=50)
def test_r2::tel_instantiation(instance):
    assert isinstance(instance, r2::TEL)

@given(instance=r2::TEL_strategy)
def test_r2::tel_capabilities_type(instance):
    assert isinstance(instance.capabilities, str)


@given(instance=r2::TEL_strategy)
def test_r2::tel_capabilities_setter(instance):
    original = instance.capabilities
    instance.capabilities = original
    assert instance.capabilities == original

@given(instance=r2::TEL_strategy)
def test_r2::tel_use_type(instance):
    assert isinstance(instance.use, str)


@given(instance=r2::TEL_strategy)
def test_r2::tel_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=r2::TEL_strategy)
def test_r2::tel_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=r2::TEL_strategy)
def test_r2::tel_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=r2::EN_strategy)
@settings(max_examples=50)
def test_r2::en_instantiation(instance):
    assert isinstance(instance, r2::EN)

@given(instance=r2::EN_strategy)
def test_r2::en_use_type(instance):
    assert isinstance(instance.use, str)


@given(instance=r2::EN_strategy)
def test_r2::en_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=r2::AD_strategy)
@settings(max_examples=50)
def test_r2::ad_instantiation(instance):
    assert isinstance(instance, r2::AD)

@given(instance=r2::AD_strategy)
def test_r2::ad_use_type(instance):
    assert isinstance(instance.use, str)


@given(instance=r2::AD_strategy)
def test_r2::ad_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=r2::ADXP_strategy)
@settings(max_examples=50)
def test_r2::adxp_instantiation(instance):
    assert isinstance(instance, r2::ADXP)

@given(instance=r2::ADXP_strategy)
def test_r2::adxp_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=r2::ADXP_strategy)
def test_r2::adxp_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

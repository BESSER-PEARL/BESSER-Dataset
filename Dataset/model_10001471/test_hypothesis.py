import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RazredK,
    RazredH,
    RazredJ,
    RazredG,
    RazredF,
    RazredE,
    RazredD,
    RazredC,
    RazredB,
    RazredA,
    BancniRacun,
    Lik3_Interface,
    Pravokotnik3,
    PravokotniLik,
    RazredB2,
    RazredA2,
    Stanovanje,
    Soba2,
    Objekt,
    Soba,
    InterfaceO_Interface1,
    ClassP1,
    Prepoznaven_Interface1,
    Avtomobil1,
    Kolo1,
    Vozen_Interface1,
    Oddelek2,
    Oseba4,
    Oseba3,
    Oddelek1,
    Class_N1,
    RazredM1,
    Class,
    Oddelek,
    Interface_Interface,
    Lik3,
    Pravokotnik1,
    BancniRacun1,
    Oseba2,
    Oseba1,
    Razred,
    NakupSkupinskeKarte_UseCase,
    NiVra_ila__UseCase,
    Preklic__UseCase,
    ZbiranjeDenarja_UseCase,
    NakupPosamezneKarte_UseCase,
    Potnik__Actor,
    NiVra_ila_UseCase,
    Preklic_UseCase,
    NeDeluje_UseCase,
    NakupKarte_UseCase,
    Potnik_Actor,
    Elipsa,
    Pravokotnik,
    Lik1,
    FileNotFoundException,
    SecurityException,
    IllegalArgumentException,
    ArithmeticException,
    IOException,
    RuntimeException,
    Exception,
    Throwable,
    Collection_Interface,
    Prepoznaven_Interface,
    Avtomobil,
    Kolo,
    Iterator_Interface,
    Vozen_Interface,
    Krog2,
    Lik2,
    Pravokotnik2,
    PravokotnikA,
    Color,
    Lik,
    RazredB1,
    RazredC1,
    RazredA1,
    LocalDate1,
    Student,
    Zaposlen,
    LocalDate,
    Oseba,
    Pes,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
    ClassP,
    Class_N,
    RazredM,
    RazredL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_razredk_is_not_abstract():
    assert not inspect.isabstract(RazredK)


def test_razredk_constructor_exists():
    assert callable(RazredK.__init__)


def test_razredk_constructor_args():
    sig = inspect.signature(RazredK.__init__)
    params = list(sig.parameters.keys())



def test_razredh_is_not_abstract():
    assert not inspect.isabstract(RazredH)


def test_razredh_constructor_exists():
    assert callable(RazredH.__init__)


def test_razredh_constructor_args():
    sig = inspect.signature(RazredH.__init__)
    params = list(sig.parameters.keys())



def test_razredj_is_not_abstract():
    assert not inspect.isabstract(RazredJ)


def test_razredj_constructor_exists():
    assert callable(RazredJ.__init__)


def test_razredj_constructor_args():
    sig = inspect.signature(RazredJ.__init__)
    params = list(sig.parameters.keys())



def test_razredg_is_not_abstract():
    assert not inspect.isabstract(RazredG)


def test_razredg_constructor_exists():
    assert callable(RazredG.__init__)


def test_razredg_constructor_args():
    sig = inspect.signature(RazredG.__init__)
    params = list(sig.parameters.keys())



def test_razredf_is_not_abstract():
    assert not inspect.isabstract(RazredF)


def test_razredf_constructor_exists():
    assert callable(RazredF.__init__)


def test_razredf_constructor_args():
    sig = inspect.signature(RazredF.__init__)
    params = list(sig.parameters.keys())



def test_razrede_is_not_abstract():
    assert not inspect.isabstract(RazredE)


def test_razrede_constructor_exists():
    assert callable(RazredE.__init__)


def test_razrede_constructor_args():
    sig = inspect.signature(RazredE.__init__)
    params = list(sig.parameters.keys())



def test_razredd_is_not_abstract():
    assert not inspect.isabstract(RazredD)


def test_razredd_constructor_exists():
    assert callable(RazredD.__init__)


def test_razredd_constructor_args():
    sig = inspect.signature(RazredD.__init__)
    params = list(sig.parameters.keys())



def test_razredc_is_not_abstract():
    assert not inspect.isabstract(RazredC)


def test_razredc_constructor_exists():
    assert callable(RazredC.__init__)


def test_razredc_constructor_args():
    sig = inspect.signature(RazredC.__init__)
    params = list(sig.parameters.keys())
    assert "protectedAtribut" in params, "Missing parameter 'protectedAtribut'"
    assert "packageAtribut" in params, "Missing parameter 'packageAtribut'"
    assert "publicAtribut" in params, "Missing parameter 'publicAtribut'"
    assert "privateAtribut" in params, "Missing parameter 'privateAtribut'"

def test_razredc_has_protectedAtribut():
    assert hasattr(RazredC, "protectedAtribut")
    descriptor = None
    for klass in RazredC.__mro__:
        if "protectedAtribut" in klass.__dict__:
            descriptor = klass.__dict__["protectedAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razredc_has_packageAtribut():
    assert hasattr(RazredC, "packageAtribut")
    descriptor = None
    for klass in RazredC.__mro__:
        if "packageAtribut" in klass.__dict__:
            descriptor = klass.__dict__["packageAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razredc_has_publicAtribut():
    assert hasattr(RazredC, "publicAtribut")
    descriptor = None
    for klass in RazredC.__mro__:
        if "publicAtribut" in klass.__dict__:
            descriptor = klass.__dict__["publicAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razredc_has_privateAtribut():
    assert hasattr(RazredC, "privateAtribut")
    descriptor = None
    for klass in RazredC.__mro__:
        if "privateAtribut" in klass.__dict__:
            descriptor = klass.__dict__["privateAtribut"]
            break
    assert isinstance(descriptor, property)



def test_razredb_is_not_abstract():
    assert not inspect.isabstract(RazredB)


def test_razredb_constructor_exists():
    assert callable(RazredB.__init__)


def test_razredb_constructor_args():
    sig = inspect.signature(RazredB.__init__)
    params = list(sig.parameters.keys())



def test_razreda_is_not_abstract():
    assert not inspect.isabstract(RazredA)


def test_razreda_constructor_exists():
    assert callable(RazredA.__init__)


def test_razreda_constructor_args():
    sig = inspect.signature(RazredA.__init__)
    params = list(sig.parameters.keys())
    assert "publicAtribut" in params, "Missing parameter 'publicAtribut'"
    assert "protectedAtribut" in params, "Missing parameter 'protectedAtribut'"
    assert "privateAtribut" in params, "Missing parameter 'privateAtribut'"
    assert "packageAtribut" in params, "Missing parameter 'packageAtribut'"

def test_razreda_has_publicAtribut():
    assert hasattr(RazredA, "publicAtribut")
    descriptor = None
    for klass in RazredA.__mro__:
        if "publicAtribut" in klass.__dict__:
            descriptor = klass.__dict__["publicAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razreda_has_protectedAtribut():
    assert hasattr(RazredA, "protectedAtribut")
    descriptor = None
    for klass in RazredA.__mro__:
        if "protectedAtribut" in klass.__dict__:
            descriptor = klass.__dict__["protectedAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razreda_has_privateAtribut():
    assert hasattr(RazredA, "privateAtribut")
    descriptor = None
    for klass in RazredA.__mro__:
        if "privateAtribut" in klass.__dict__:
            descriptor = klass.__dict__["privateAtribut"]
            break
    assert isinstance(descriptor, property)

def test_razreda_has_packageAtribut():
    assert hasattr(RazredA, "packageAtribut")
    descriptor = None
    for klass in RazredA.__mro__:
        if "packageAtribut" in klass.__dict__:
            descriptor = klass.__dict__["packageAtribut"]
            break
    assert isinstance(descriptor, property)



def test_bancniracun_is_not_abstract():
    assert not inspect.isabstract(BancniRacun)


def test_bancniracun_constructor_exists():
    assert callable(BancniRacun.__init__)


def test_bancniracun_constructor_args():
    sig = inspect.signature(BancniRacun.__init__)
    params = list(sig.parameters.keys())
    assert "aktiven" in params, "Missing parameter 'aktiven'"
    assert "lastnik" in params, "Missing parameter 'lastnik'"
    assert "stanje" in params, "Missing parameter 'stanje'"

def test_bancniracun_has_aktiven():
    assert hasattr(BancniRacun, "aktiven")
    descriptor = None
    for klass in BancniRacun.__mro__:
        if "aktiven" in klass.__dict__:
            descriptor = klass.__dict__["aktiven"]
            break
    assert isinstance(descriptor, property)

def test_bancniracun_has_lastnik():
    assert hasattr(BancniRacun, "lastnik")
    descriptor = None
    for klass in BancniRacun.__mro__:
        if "lastnik" in klass.__dict__:
            descriptor = klass.__dict__["lastnik"]
            break
    assert isinstance(descriptor, property)

def test_bancniracun_has_stanje():
    assert hasattr(BancniRacun, "stanje")
    descriptor = None
    for klass in BancniRacun.__mro__:
        if "stanje" in klass.__dict__:
            descriptor = klass.__dict__["stanje"]
            break
    assert isinstance(descriptor, property)



def test_lik3_interface_is_not_abstract():
    assert not inspect.isabstract(Lik3_Interface)


def test_lik3_interface_constructor_exists():
    assert callable(Lik3_Interface.__init__)


def test_lik3_interface_constructor_args():
    sig = inspect.signature(Lik3_Interface.__init__)
    params = list(sig.parameters.keys())



def test_pravokotnik3_is_not_abstract():
    assert not inspect.isabstract(Pravokotnik3)


def test_pravokotnik3_constructor_exists():
    assert callable(Pravokotnik3.__init__)


def test_pravokotnik3_constructor_args():
    sig = inspect.signature(Pravokotnik3.__init__)
    params = list(sig.parameters.keys())
    assert "koordinataX" in params, "Missing parameter 'koordinataX'"
    assert "koordinataY" in params, "Missing parameter 'koordinataY'"

def test_pravokotnik3_has_koordinataX():
    assert hasattr(Pravokotnik3, "koordinataX")
    descriptor = None
    for klass in Pravokotnik3.__mro__:
        if "koordinataX" in klass.__dict__:
            descriptor = klass.__dict__["koordinataX"]
            break
    assert isinstance(descriptor, property)

def test_pravokotnik3_has_koordinataY():
    assert hasattr(Pravokotnik3, "koordinataY")
    descriptor = None
    for klass in Pravokotnik3.__mro__:
        if "koordinataY" in klass.__dict__:
            descriptor = klass.__dict__["koordinataY"]
            break
    assert isinstance(descriptor, property)



def test_pravokotnilik_is_not_abstract():
    assert not inspect.isabstract(PravokotniLik)


def test_pravokotnilik_constructor_exists():
    assert callable(PravokotniLik.__init__)


def test_pravokotnilik_constructor_args():
    sig = inspect.signature(PravokotniLik.__init__)
    params = list(sig.parameters.keys())
    assert "sirina" in params, "Missing parameter 'sirina'"
    assert "visina" in params, "Missing parameter 'visina'"

def test_pravokotnilik_has_sirina():
    assert hasattr(PravokotniLik, "sirina")
    descriptor = None
    for klass in PravokotniLik.__mro__:
        if "sirina" in klass.__dict__:
            descriptor = klass.__dict__["sirina"]
            break
    assert isinstance(descriptor, property)

def test_pravokotnilik_has_visina():
    assert hasattr(PravokotniLik, "visina")
    descriptor = None
    for klass in PravokotniLik.__mro__:
        if "visina" in klass.__dict__:
            descriptor = klass.__dict__["visina"]
            break
    assert isinstance(descriptor, property)



def test_razredb2_is_not_abstract():
    assert not inspect.isabstract(RazredB2)


def test_razredb2_constructor_exists():
    assert callable(RazredB2.__init__)


def test_razredb2_constructor_args():
    sig = inspect.signature(RazredB2.__init__)
    params = list(sig.parameters.keys())



def test_razreda2_is_not_abstract():
    assert not inspect.isabstract(RazredA2)


def test_razreda2_constructor_exists():
    assert callable(RazredA2.__init__)


def test_razreda2_constructor_args():
    sig = inspect.signature(RazredA2.__init__)
    params = list(sig.parameters.keys())
    assert "objektB" in params, "Missing parameter 'objektB'"

def test_razreda2_has_objektB():
    assert hasattr(RazredA2, "objektB")
    descriptor = None
    for klass in RazredA2.__mro__:
        if "objektB" in klass.__dict__:
            descriptor = klass.__dict__["objektB"]
            break
    assert isinstance(descriptor, property)



def test_stanovanje_is_not_abstract():
    assert not inspect.isabstract(Stanovanje)


def test_stanovanje_constructor_exists():
    assert callable(Stanovanje.__init__)


def test_stanovanje_constructor_args():
    sig = inspect.signature(Stanovanje.__init__)
    params = list(sig.parameters.keys())



def test_soba2_is_not_abstract():
    assert not inspect.isabstract(Soba2)


def test_soba2_constructor_exists():
    assert callable(Soba2.__init__)


def test_soba2_constructor_args():
    sig = inspect.signature(Soba2.__init__)
    params = list(sig.parameters.keys())



def test_objekt_is_not_abstract():
    assert not inspect.isabstract(Objekt)


def test_objekt_constructor_exists():
    assert callable(Objekt.__init__)


def test_objekt_constructor_args():
    sig = inspect.signature(Objekt.__init__)
    params = list(sig.parameters.keys())



def test_soba_is_not_abstract():
    assert not inspect.isabstract(Soba)


def test_soba_constructor_exists():
    assert callable(Soba.__init__)


def test_soba_constructor_args():
    sig = inspect.signature(Soba.__init__)
    params = list(sig.parameters.keys())



def test_interfaceo_interface1_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface1)


def test_interfaceo_interface1_constructor_exists():
    assert callable(InterfaceO_Interface1.__init__)


def test_interfaceo_interface1_constructor_args():
    sig = inspect.signature(InterfaceO_Interface1.__init__)
    params = list(sig.parameters.keys())



def test_classp1_is_not_abstract():
    assert not inspect.isabstract(ClassP1)


def test_classp1_constructor_exists():
    assert callable(ClassP1.__init__)


def test_classp1_constructor_args():
    sig = inspect.signature(ClassP1.__init__)
    params = list(sig.parameters.keys())



def test_prepoznaven_interface1_is_not_abstract():
    assert not inspect.isabstract(Prepoznaven_Interface1)


def test_prepoznaven_interface1_constructor_exists():
    assert callable(Prepoznaven_Interface1.__init__)


def test_prepoznaven_interface1_constructor_args():
    sig = inspect.signature(Prepoznaven_Interface1.__init__)
    params = list(sig.parameters.keys())



def test_avtomobil1_is_not_abstract():
    assert not inspect.isabstract(Avtomobil1)


def test_avtomobil1_constructor_exists():
    assert callable(Avtomobil1.__init__)


def test_avtomobil1_constructor_args():
    sig = inspect.signature(Avtomobil1.__init__)
    params = list(sig.parameters.keys())



def test_kolo1_is_not_abstract():
    assert not inspect.isabstract(Kolo1)


def test_kolo1_constructor_exists():
    assert callable(Kolo1.__init__)


def test_kolo1_constructor_args():
    sig = inspect.signature(Kolo1.__init__)
    params = list(sig.parameters.keys())



def test_vozen_interface1_is_not_abstract():
    assert not inspect.isabstract(Vozen_Interface1)


def test_vozen_interface1_constructor_exists():
    assert callable(Vozen_Interface1.__init__)


def test_vozen_interface1_constructor_args():
    sig = inspect.signature(Vozen_Interface1.__init__)
    params = list(sig.parameters.keys())



def test_oddelek2_is_not_abstract():
    assert not inspect.isabstract(Oddelek2)


def test_oddelek2_constructor_exists():
    assert callable(Oddelek2.__init__)


def test_oddelek2_constructor_args():
    sig = inspect.signature(Oddelek2.__init__)
    params = list(sig.parameters.keys())



def test_oseba4_is_not_abstract():
    assert not inspect.isabstract(Oseba4)


def test_oseba4_constructor_exists():
    assert callable(Oseba4.__init__)


def test_oseba4_constructor_args():
    sig = inspect.signature(Oseba4.__init__)
    params = list(sig.parameters.keys())



def test_oseba3_is_not_abstract():
    assert not inspect.isabstract(Oseba3)


def test_oseba3_constructor_exists():
    assert callable(Oseba3.__init__)


def test_oseba3_constructor_args():
    sig = inspect.signature(Oseba3.__init__)
    params = list(sig.parameters.keys())



def test_oddelek1_is_not_abstract():
    assert not inspect.isabstract(Oddelek1)


def test_oddelek1_constructor_exists():
    assert callable(Oddelek1.__init__)


def test_oddelek1_constructor_args():
    sig = inspect.signature(Oddelek1.__init__)
    params = list(sig.parameters.keys())



def test_class_n1_is_not_abstract():
    assert not inspect.isabstract(Class_N1)


def test_class_n1_constructor_exists():
    assert callable(Class_N1.__init__)


def test_class_n1_constructor_args():
    sig = inspect.signature(Class_N1.__init__)
    params = list(sig.parameters.keys())



def test_razredm1_is_not_abstract():
    assert not inspect.isabstract(RazredM1)


def test_razredm1_constructor_exists():
    assert callable(RazredM1.__init__)


def test_razredm1_constructor_args():
    sig = inspect.signature(RazredM1.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_oddelek_is_not_abstract():
    assert not inspect.isabstract(Oddelek)


def test_oddelek_constructor_exists():
    assert callable(Oddelek.__init__)


def test_oddelek_constructor_args():
    sig = inspect.signature(Oddelek.__init__)
    params = list(sig.parameters.keys())



def test_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_lik3_is_not_abstract():
    assert not inspect.isabstract(Lik3)


def test_lik3_constructor_exists():
    assert callable(Lik3.__init__)


def test_lik3_constructor_args():
    sig = inspect.signature(Lik3.__init__)
    params = list(sig.parameters.keys())
    assert "x1" in params, "Missing parameter 'x1'"
    assert "x" in params, "Missing parameter 'x'"
    assert "barva" in params, "Missing parameter 'barva'"

def test_lik3_has_x1():
    assert hasattr(Lik3, "x1")
    descriptor = None
    for klass in Lik3.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_lik3_has_x():
    assert hasattr(Lik3, "x")
    descriptor = None
    for klass in Lik3.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_lik3_has_barva():
    assert hasattr(Lik3, "barva")
    descriptor = None
    for klass in Lik3.__mro__:
        if "barva" in klass.__dict__:
            descriptor = klass.__dict__["barva"]
            break
    assert isinstance(descriptor, property)



def test_pravokotnik1_is_not_abstract():
    assert not inspect.isabstract(Pravokotnik1)


def test_pravokotnik1_constructor_exists():
    assert callable(Pravokotnik1.__init__)


def test_pravokotnik1_constructor_args():
    sig = inspect.signature(Pravokotnik1.__init__)
    params = list(sig.parameters.keys())
    assert "stranicaA" in params, "Missing parameter 'stranicaA'"
    assert "stranicaB" in params, "Missing parameter 'stranicaB'"

def test_pravokotnik1_has_stranicaA():
    assert hasattr(Pravokotnik1, "stranicaA")
    descriptor = None
    for klass in Pravokotnik1.__mro__:
        if "stranicaA" in klass.__dict__:
            descriptor = klass.__dict__["stranicaA"]
            break
    assert isinstance(descriptor, property)

def test_pravokotnik1_has_stranicaB():
    assert hasattr(Pravokotnik1, "stranicaB")
    descriptor = None
    for klass in Pravokotnik1.__mro__:
        if "stranicaB" in klass.__dict__:
            descriptor = klass.__dict__["stranicaB"]
            break
    assert isinstance(descriptor, property)



def test_bancniracun1_is_not_abstract():
    assert not inspect.isabstract(BancniRacun1)


def test_bancniracun1_constructor_exists():
    assert callable(BancniRacun1.__init__)


def test_bancniracun1_constructor_args():
    sig = inspect.signature(BancniRacun1.__init__)
    params = list(sig.parameters.keys())
    assert "aktiven" in params, "Missing parameter 'aktiven'"
    assert "lastnik" in params, "Missing parameter 'lastnik'"
    assert "stanje" in params, "Missing parameter 'stanje'"

def test_bancniracun1_has_aktiven():
    assert hasattr(BancniRacun1, "aktiven")
    descriptor = None
    for klass in BancniRacun1.__mro__:
        if "aktiven" in klass.__dict__:
            descriptor = klass.__dict__["aktiven"]
            break
    assert isinstance(descriptor, property)

def test_bancniracun1_has_lastnik():
    assert hasattr(BancniRacun1, "lastnik")
    descriptor = None
    for klass in BancniRacun1.__mro__:
        if "lastnik" in klass.__dict__:
            descriptor = klass.__dict__["lastnik"]
            break
    assert isinstance(descriptor, property)

def test_bancniracun1_has_stanje():
    assert hasattr(BancniRacun1, "stanje")
    descriptor = None
    for klass in BancniRacun1.__mro__:
        if "stanje" in klass.__dict__:
            descriptor = klass.__dict__["stanje"]
            break
    assert isinstance(descriptor, property)



def test_oseba2_is_not_abstract():
    assert not inspect.isabstract(Oseba2)


def test_oseba2_constructor_exists():
    assert callable(Oseba2.__init__)


def test_oseba2_constructor_args():
    sig = inspect.signature(Oseba2.__init__)
    params = list(sig.parameters.keys())
    assert "priimek" in params, "Missing parameter 'priimek'"
    assert "datumRojstva" in params, "Missing parameter 'datumRojstva'"
    assert "ime" in params, "Missing parameter 'ime'"

def test_oseba2_has_priimek():
    assert hasattr(Oseba2, "priimek")
    descriptor = None
    for klass in Oseba2.__mro__:
        if "priimek" in klass.__dict__:
            descriptor = klass.__dict__["priimek"]
            break
    assert isinstance(descriptor, property)

def test_oseba2_has_datumRojstva():
    assert hasattr(Oseba2, "datumRojstva")
    descriptor = None
    for klass in Oseba2.__mro__:
        if "datumRojstva" in klass.__dict__:
            descriptor = klass.__dict__["datumRojstva"]
            break
    assert isinstance(descriptor, property)

def test_oseba2_has_ime():
    assert hasattr(Oseba2, "ime")
    descriptor = None
    for klass in Oseba2.__mro__:
        if "ime" in klass.__dict__:
            descriptor = klass.__dict__["ime"]
            break
    assert isinstance(descriptor, property)



def test_oseba1_is_not_abstract():
    assert not inspect.isabstract(Oseba1)


def test_oseba1_constructor_exists():
    assert callable(Oseba1.__init__)


def test_oseba1_constructor_args():
    sig = inspect.signature(Oseba1.__init__)
    params = list(sig.parameters.keys())
    assert "emso" in params, "Missing parameter 'emso'"
    assert "ime" in params, "Missing parameter 'ime'"
    assert "priimek" in params, "Missing parameter 'priimek'"

def test_oseba1_has_emso():
    assert hasattr(Oseba1, "emso")
    descriptor = None
    for klass in Oseba1.__mro__:
        if "emso" in klass.__dict__:
            descriptor = klass.__dict__["emso"]
            break
    assert isinstance(descriptor, property)

def test_oseba1_has_ime():
    assert hasattr(Oseba1, "ime")
    descriptor = None
    for klass in Oseba1.__mro__:
        if "ime" in klass.__dict__:
            descriptor = klass.__dict__["ime"]
            break
    assert isinstance(descriptor, property)

def test_oseba1_has_priimek():
    assert hasattr(Oseba1, "priimek")
    descriptor = None
    for klass in Oseba1.__mro__:
        if "priimek" in klass.__dict__:
            descriptor = klass.__dict__["priimek"]
            break
    assert isinstance(descriptor, property)



def test_razred_is_not_abstract():
    assert not inspect.isabstract(Razred)


def test_razred_constructor_exists():
    assert callable(Razred.__init__)


def test_razred_constructor_args():
    sig = inspect.signature(Razred.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_razred_has_attribute():
    assert hasattr(Razred, "attribute")
    descriptor = None
    for klass in Razred.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_nakupskupinskekarte_usecase_is_not_abstract():
    assert not inspect.isabstract(NakupSkupinskeKarte_UseCase)


def test_nakupskupinskekarte_usecase_constructor_exists():
    assert callable(NakupSkupinskeKarte_UseCase.__init__)


def test_nakupskupinskekarte_usecase_constructor_args():
    sig = inspect.signature(NakupSkupinskeKarte_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_nivra_ila__usecase_is_not_abstract():
    assert not inspect.isabstract(NiVra_ila__UseCase)


def test_nivra_ila__usecase_constructor_exists():
    assert callable(NiVra_ila__UseCase.__init__)


def test_nivra_ila__usecase_constructor_args():
    sig = inspect.signature(NiVra_ila__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_preklic__usecase_is_not_abstract():
    assert not inspect.isabstract(Preklic__UseCase)


def test_preklic__usecase_constructor_exists():
    assert callable(Preklic__UseCase.__init__)


def test_preklic__usecase_constructor_args():
    sig = inspect.signature(Preklic__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_zbiranjedenarja_usecase_is_not_abstract():
    assert not inspect.isabstract(ZbiranjeDenarja_UseCase)


def test_zbiranjedenarja_usecase_constructor_exists():
    assert callable(ZbiranjeDenarja_UseCase.__init__)


def test_zbiranjedenarja_usecase_constructor_args():
    sig = inspect.signature(ZbiranjeDenarja_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_nakupposameznekarte_usecase_is_not_abstract():
    assert not inspect.isabstract(NakupPosamezneKarte_UseCase)


def test_nakupposameznekarte_usecase_constructor_exists():
    assert callable(NakupPosamezneKarte_UseCase.__init__)


def test_nakupposameznekarte_usecase_constructor_args():
    sig = inspect.signature(NakupPosamezneKarte_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_potnik__actor_is_not_abstract():
    assert not inspect.isabstract(Potnik__Actor)


def test_potnik__actor_constructor_exists():
    assert callable(Potnik__Actor.__init__)


def test_potnik__actor_constructor_args():
    sig = inspect.signature(Potnik__Actor.__init__)
    params = list(sig.parameters.keys())



def test_nivra_ila_usecase_is_not_abstract():
    assert not inspect.isabstract(NiVra_ila_UseCase)


def test_nivra_ila_usecase_constructor_exists():
    assert callable(NiVra_ila_UseCase.__init__)


def test_nivra_ila_usecase_constructor_args():
    sig = inspect.signature(NiVra_ila_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_preklic_usecase_is_not_abstract():
    assert not inspect.isabstract(Preklic_UseCase)


def test_preklic_usecase_constructor_exists():
    assert callable(Preklic_UseCase.__init__)


def test_preklic_usecase_constructor_args():
    sig = inspect.signature(Preklic_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_nedeluje_usecase_is_not_abstract():
    assert not inspect.isabstract(NeDeluje_UseCase)


def test_nedeluje_usecase_constructor_exists():
    assert callable(NeDeluje_UseCase.__init__)


def test_nedeluje_usecase_constructor_args():
    sig = inspect.signature(NeDeluje_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_nakupkarte_usecase_is_not_abstract():
    assert not inspect.isabstract(NakupKarte_UseCase)


def test_nakupkarte_usecase_constructor_exists():
    assert callable(NakupKarte_UseCase.__init__)


def test_nakupkarte_usecase_constructor_args():
    sig = inspect.signature(NakupKarte_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_potnik_actor_is_not_abstract():
    assert not inspect.isabstract(Potnik_Actor)


def test_potnik_actor_constructor_exists():
    assert callable(Potnik_Actor.__init__)


def test_potnik_actor_constructor_args():
    sig = inspect.signature(Potnik_Actor.__init__)
    params = list(sig.parameters.keys())



def test_elipsa_is_not_abstract():
    assert not inspect.isabstract(Elipsa)


def test_elipsa_constructor_exists():
    assert callable(Elipsa.__init__)


def test_elipsa_constructor_args():
    sig = inspect.signature(Elipsa.__init__)
    params = list(sig.parameters.keys())



def test_pravokotnik_is_not_abstract():
    assert not inspect.isabstract(Pravokotnik)


def test_pravokotnik_constructor_exists():
    assert callable(Pravokotnik.__init__)


def test_pravokotnik_constructor_args():
    sig = inspect.signature(Pravokotnik.__init__)
    params = list(sig.parameters.keys())



def test_lik1_is_not_abstract():
    assert not inspect.isabstract(Lik1)


def test_lik1_constructor_exists():
    assert callable(Lik1.__init__)


def test_lik1_constructor_args():
    sig = inspect.signature(Lik1.__init__)
    params = list(sig.parameters.keys())
    assert "visina" in params, "Missing parameter 'visina'"
    assert "barva" in params, "Missing parameter 'barva'"
    assert "x1" in params, "Missing parameter 'x1'"
    assert "x" in params, "Missing parameter 'x'"
    assert "sirina" in params, "Missing parameter 'sirina'"

def test_lik1_has_visina():
    assert hasattr(Lik1, "visina")
    descriptor = None
    for klass in Lik1.__mro__:
        if "visina" in klass.__dict__:
            descriptor = klass.__dict__["visina"]
            break
    assert isinstance(descriptor, property)

def test_lik1_has_barva():
    assert hasattr(Lik1, "barva")
    descriptor = None
    for klass in Lik1.__mro__:
        if "barva" in klass.__dict__:
            descriptor = klass.__dict__["barva"]
            break
    assert isinstance(descriptor, property)

def test_lik1_has_x1():
    assert hasattr(Lik1, "x1")
    descriptor = None
    for klass in Lik1.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_lik1_has_x():
    assert hasattr(Lik1, "x")
    descriptor = None
    for klass in Lik1.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_lik1_has_sirina():
    assert hasattr(Lik1, "sirina")
    descriptor = None
    for klass in Lik1.__mro__:
        if "sirina" in klass.__dict__:
            descriptor = klass.__dict__["sirina"]
            break
    assert isinstance(descriptor, property)



def test_filenotfoundexception_is_not_abstract():
    assert not inspect.isabstract(FileNotFoundException)


def test_filenotfoundexception_constructor_exists():
    assert callable(FileNotFoundException.__init__)


def test_filenotfoundexception_constructor_args():
    sig = inspect.signature(FileNotFoundException.__init__)
    params = list(sig.parameters.keys())



def test_securityexception_is_not_abstract():
    assert not inspect.isabstract(SecurityException)


def test_securityexception_constructor_exists():
    assert callable(SecurityException.__init__)


def test_securityexception_constructor_args():
    sig = inspect.signature(SecurityException.__init__)
    params = list(sig.parameters.keys())



def test_illegalargumentexception_is_not_abstract():
    assert not inspect.isabstract(IllegalArgumentException)


def test_illegalargumentexception_constructor_exists():
    assert callable(IllegalArgumentException.__init__)


def test_illegalargumentexception_constructor_args():
    sig = inspect.signature(IllegalArgumentException.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexception_is_not_abstract():
    assert not inspect.isabstract(ArithmeticException)


def test_arithmeticexception_constructor_exists():
    assert callable(ArithmeticException.__init__)


def test_arithmeticexception_constructor_args():
    sig = inspect.signature(ArithmeticException.__init__)
    params = list(sig.parameters.keys())



def test_ioexception_is_not_abstract():
    assert not inspect.isabstract(IOException)


def test_ioexception_constructor_exists():
    assert callable(IOException.__init__)


def test_ioexception_constructor_args():
    sig = inspect.signature(IOException.__init__)
    params = list(sig.parameters.keys())



def test_runtimeexception_is_not_abstract():
    assert not inspect.isabstract(RuntimeException)


def test_runtimeexception_constructor_exists():
    assert callable(RuntimeException.__init__)


def test_runtimeexception_constructor_args():
    sig = inspect.signature(RuntimeException.__init__)
    params = list(sig.parameters.keys())



def test_exception_is_not_abstract():
    assert not inspect.isabstract(Exception)


def test_exception_constructor_exists():
    assert callable(Exception.__init__)


def test_exception_constructor_args():
    sig = inspect.signature(Exception.__init__)
    params = list(sig.parameters.keys())



def test_throwable_is_not_abstract():
    assert not inspect.isabstract(Throwable)


def test_throwable_constructor_exists():
    assert callable(Throwable.__init__)


def test_throwable_constructor_args():
    sig = inspect.signature(Throwable.__init__)
    params = list(sig.parameters.keys())



def test_collection_interface_is_not_abstract():
    assert not inspect.isabstract(Collection_Interface)


def test_collection_interface_constructor_exists():
    assert callable(Collection_Interface.__init__)


def test_collection_interface_constructor_args():
    sig = inspect.signature(Collection_Interface.__init__)
    params = list(sig.parameters.keys())



def test_prepoznaven_interface_is_not_abstract():
    assert not inspect.isabstract(Prepoznaven_Interface)


def test_prepoznaven_interface_constructor_exists():
    assert callable(Prepoznaven_Interface.__init__)


def test_prepoznaven_interface_constructor_args():
    sig = inspect.signature(Prepoznaven_Interface.__init__)
    params = list(sig.parameters.keys())



def test_avtomobil_is_not_abstract():
    assert not inspect.isabstract(Avtomobil)


def test_avtomobil_constructor_exists():
    assert callable(Avtomobil.__init__)


def test_avtomobil_constructor_args():
    sig = inspect.signature(Avtomobil.__init__)
    params = list(sig.parameters.keys())



def test_kolo_is_not_abstract():
    assert not inspect.isabstract(Kolo)


def test_kolo_constructor_exists():
    assert callable(Kolo.__init__)


def test_kolo_constructor_args():
    sig = inspect.signature(Kolo.__init__)
    params = list(sig.parameters.keys())



def test_iterator_interface_is_not_abstract():
    assert not inspect.isabstract(Iterator_Interface)


def test_iterator_interface_constructor_exists():
    assert callable(Iterator_Interface.__init__)


def test_iterator_interface_constructor_args():
    sig = inspect.signature(Iterator_Interface.__init__)
    params = list(sig.parameters.keys())



def test_vozen_interface_is_not_abstract():
    assert not inspect.isabstract(Vozen_Interface)


def test_vozen_interface_constructor_exists():
    assert callable(Vozen_Interface.__init__)


def test_vozen_interface_constructor_args():
    sig = inspect.signature(Vozen_Interface.__init__)
    params = list(sig.parameters.keys())



def test_krog2_is_not_abstract():
    assert not inspect.isabstract(Krog2)


def test_krog2_constructor_exists():
    assert callable(Krog2.__init__)


def test_krog2_constructor_args():
    sig = inspect.signature(Krog2.__init__)
    params = list(sig.parameters.keys())



def test_lik2_is_not_abstract():
    assert not inspect.isabstract(Lik2)


def test_lik2_constructor_exists():
    assert callable(Lik2.__init__)


def test_lik2_constructor_args():
    sig = inspect.signature(Lik2.__init__)
    params = list(sig.parameters.keys())
    assert "visina" in params, "Missing parameter 'visina'"
    assert "sirina" in params, "Missing parameter 'sirina'"
    assert "x" in params, "Missing parameter 'x'"
    assert "barva" in params, "Missing parameter 'barva'"
    assert "x1" in params, "Missing parameter 'x1'"

def test_lik2_has_visina():
    assert hasattr(Lik2, "visina")
    descriptor = None
    for klass in Lik2.__mro__:
        if "visina" in klass.__dict__:
            descriptor = klass.__dict__["visina"]
            break
    assert isinstance(descriptor, property)

def test_lik2_has_sirina():
    assert hasattr(Lik2, "sirina")
    descriptor = None
    for klass in Lik2.__mro__:
        if "sirina" in klass.__dict__:
            descriptor = klass.__dict__["sirina"]
            break
    assert isinstance(descriptor, property)

def test_lik2_has_x():
    assert hasattr(Lik2, "x")
    descriptor = None
    for klass in Lik2.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_lik2_has_barva():
    assert hasattr(Lik2, "barva")
    descriptor = None
    for klass in Lik2.__mro__:
        if "barva" in klass.__dict__:
            descriptor = klass.__dict__["barva"]
            break
    assert isinstance(descriptor, property)

def test_lik2_has_x1():
    assert hasattr(Lik2, "x1")
    descriptor = None
    for klass in Lik2.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)



def test_pravokotnik2_is_not_abstract():
    assert not inspect.isabstract(Pravokotnik2)


def test_pravokotnik2_constructor_exists():
    assert callable(Pravokotnik2.__init__)


def test_pravokotnik2_constructor_args():
    sig = inspect.signature(Pravokotnik2.__init__)
    params = list(sig.parameters.keys())



def test_pravokotnika_is_not_abstract():
    assert not inspect.isabstract(PravokotnikA)


def test_pravokotnika_constructor_exists():
    assert callable(PravokotnikA.__init__)


def test_pravokotnika_constructor_args():
    sig = inspect.signature(PravokotnikA.__init__)
    params = list(sig.parameters.keys())
    assert "stranicaB" in params, "Missing parameter 'stranicaB'"
    assert "stranicaA" in params, "Missing parameter 'stranicaA'"

def test_pravokotnika_has_stranicaB():
    assert hasattr(PravokotnikA, "stranicaB")
    descriptor = None
    for klass in PravokotnikA.__mro__:
        if "stranicaB" in klass.__dict__:
            descriptor = klass.__dict__["stranicaB"]
            break
    assert isinstance(descriptor, property)

def test_pravokotnika_has_stranicaA():
    assert hasattr(PravokotnikA, "stranicaA")
    descriptor = None
    for klass in PravokotnikA.__mro__:
        if "stranicaA" in klass.__dict__:
            descriptor = klass.__dict__["stranicaA"]
            break
    assert isinstance(descriptor, property)



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_lik_is_not_abstract():
    assert not inspect.isabstract(Lik)


def test_lik_constructor_exists():
    assert callable(Lik.__init__)


def test_lik_constructor_args():
    sig = inspect.signature(Lik.__init__)
    params = list(sig.parameters.keys())
    assert "x1" in params, "Missing parameter 'x1'"
    assert "x" in params, "Missing parameter 'x'"
    assert "barva" in params, "Missing parameter 'barva'"

def test_lik_has_x1():
    assert hasattr(Lik, "x1")
    descriptor = None
    for klass in Lik.__mro__:
        if "x1" in klass.__dict__:
            descriptor = klass.__dict__["x1"]
            break
    assert isinstance(descriptor, property)

def test_lik_has_x():
    assert hasattr(Lik, "x")
    descriptor = None
    for klass in Lik.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_lik_has_barva():
    assert hasattr(Lik, "barva")
    descriptor = None
    for klass in Lik.__mro__:
        if "barva" in klass.__dict__:
            descriptor = klass.__dict__["barva"]
            break
    assert isinstance(descriptor, property)



def test_razredb1_is_not_abstract():
    assert not inspect.isabstract(RazredB1)


def test_razredb1_constructor_exists():
    assert callable(RazredB1.__init__)


def test_razredb1_constructor_args():
    sig = inspect.signature(RazredB1.__init__)
    params = list(sig.parameters.keys())



def test_razredc1_is_not_abstract():
    assert not inspect.isabstract(RazredC1)


def test_razredc1_constructor_exists():
    assert callable(RazredC1.__init__)


def test_razredc1_constructor_args():
    sig = inspect.signature(RazredC1.__init__)
    params = list(sig.parameters.keys())
    assert "stevilo" in params, "Missing parameter 'stevilo'"

def test_razredc1_has_stevilo():
    assert hasattr(RazredC1, "stevilo")
    descriptor = None
    for klass in RazredC1.__mro__:
        if "stevilo" in klass.__dict__:
            descriptor = klass.__dict__["stevilo"]
            break
    assert isinstance(descriptor, property)



def test_razreda1_is_not_abstract():
    assert not inspect.isabstract(RazredA1)


def test_razreda1_constructor_exists():
    assert callable(RazredA1.__init__)


def test_razreda1_constructor_args():
    sig = inspect.signature(RazredA1.__init__)
    params = list(sig.parameters.keys())
    assert "stevilo" in params, "Missing parameter 'stevilo'"

def test_razreda1_has_stevilo():
    assert hasattr(RazredA1, "stevilo")
    descriptor = None
    for klass in RazredA1.__mro__:
        if "stevilo" in klass.__dict__:
            descriptor = klass.__dict__["stevilo"]
            break
    assert isinstance(descriptor, property)



def test_localdate1_is_not_abstract():
    assert not inspect.isabstract(LocalDate1)


def test_localdate1_constructor_exists():
    assert callable(LocalDate1.__init__)


def test_localdate1_constructor_args():
    sig = inspect.signature(LocalDate1.__init__)
    params = list(sig.parameters.keys())



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "vpisnaStevilka" in params, "Missing parameter 'vpisnaStevilka'"
    assert "studijskiProgram" in params, "Missing parameter 'studijskiProgram'"
    assert "datumVpisa" in params, "Missing parameter 'datumVpisa'"

def test_student_has_vpisnaStevilka():
    assert hasattr(Student, "vpisnaStevilka")
    descriptor = None
    for klass in Student.__mro__:
        if "vpisnaStevilka" in klass.__dict__:
            descriptor = klass.__dict__["vpisnaStevilka"]
            break
    assert isinstance(descriptor, property)

def test_student_has_studijskiProgram():
    assert hasattr(Student, "studijskiProgram")
    descriptor = None
    for klass in Student.__mro__:
        if "studijskiProgram" in klass.__dict__:
            descriptor = klass.__dict__["studijskiProgram"]
            break
    assert isinstance(descriptor, property)

def test_student_has_datumVpisa():
    assert hasattr(Student, "datumVpisa")
    descriptor = None
    for klass in Student.__mro__:
        if "datumVpisa" in klass.__dict__:
            descriptor = klass.__dict__["datumVpisa"]
            break
    assert isinstance(descriptor, property)



def test_zaposlen_is_not_abstract():
    assert not inspect.isabstract(Zaposlen)


def test_zaposlen_constructor_exists():
    assert callable(Zaposlen.__init__)


def test_zaposlen_constructor_args():
    sig = inspect.signature(Zaposlen.__init__)
    params = list(sig.parameters.keys())
    assert "izobrazba" in params, "Missing parameter 'izobrazba'"
    assert "urnaPostavka" in params, "Missing parameter 'urnaPostavka'"

def test_zaposlen_has_izobrazba():
    assert hasattr(Zaposlen, "izobrazba")
    descriptor = None
    for klass in Zaposlen.__mro__:
        if "izobrazba" in klass.__dict__:
            descriptor = klass.__dict__["izobrazba"]
            break
    assert isinstance(descriptor, property)

def test_zaposlen_has_urnaPostavka():
    assert hasattr(Zaposlen, "urnaPostavka")
    descriptor = None
    for klass in Zaposlen.__mro__:
        if "urnaPostavka" in klass.__dict__:
            descriptor = klass.__dict__["urnaPostavka"]
            break
    assert isinstance(descriptor, property)



def test_localdate_is_not_abstract():
    assert not inspect.isabstract(LocalDate)


def test_localdate_constructor_exists():
    assert callable(LocalDate.__init__)


def test_localdate_constructor_args():
    sig = inspect.signature(LocalDate.__init__)
    params = list(sig.parameters.keys())



def test_oseba_is_not_abstract():
    assert not inspect.isabstract(Oseba)


def test_oseba_constructor_exists():
    assert callable(Oseba.__init__)


def test_oseba_constructor_args():
    sig = inspect.signature(Oseba.__init__)
    params = list(sig.parameters.keys())
    assert "spol" in params, "Missing parameter 'spol'"
    assert "ime" in params, "Missing parameter 'ime'"
    assert "priimek" in params, "Missing parameter 'priimek'"
    assert "datumRojstva" in params, "Missing parameter 'datumRojstva'"

def test_oseba_has_spol():
    assert hasattr(Oseba, "spol")
    descriptor = None
    for klass in Oseba.__mro__:
        if "spol" in klass.__dict__:
            descriptor = klass.__dict__["spol"]
            break
    assert isinstance(descriptor, property)

def test_oseba_has_ime():
    assert hasattr(Oseba, "ime")
    descriptor = None
    for klass in Oseba.__mro__:
        if "ime" in klass.__dict__:
            descriptor = klass.__dict__["ime"]
            break
    assert isinstance(descriptor, property)

def test_oseba_has_priimek():
    assert hasattr(Oseba, "priimek")
    descriptor = None
    for klass in Oseba.__mro__:
        if "priimek" in klass.__dict__:
            descriptor = klass.__dict__["priimek"]
            break
    assert isinstance(descriptor, property)

def test_oseba_has_datumRojstva():
    assert hasattr(Oseba, "datumRojstva")
    descriptor = None
    for klass in Oseba.__mro__:
        if "datumRojstva" in klass.__dict__:
            descriptor = klass.__dict__["datumRojstva"]
            break
    assert isinstance(descriptor, property)



def test_pes_is_not_abstract():
    assert not inspect.isabstract(Pes)


def test_pes_constructor_exists():
    assert callable(Pes.__init__)


def test_pes_constructor_args():
    sig = inspect.signature(Pes.__init__)
    params = list(sig.parameters.keys())
    assert "visina" in params, "Missing parameter 'visina'"
    assert "pasma" in params, "Missing parameter 'pasma'"
    assert "vzdevek" in params, "Missing parameter 'vzdevek'"

def test_pes_has_visina():
    assert hasattr(Pes, "visina")
    descriptor = None
    for klass in Pes.__mro__:
        if "visina" in klass.__dict__:
            descriptor = klass.__dict__["visina"]
            break
    assert isinstance(descriptor, property)

def test_pes_has_pasma():
    assert hasattr(Pes, "pasma")
    descriptor = None
    for klass in Pes.__mro__:
        if "pasma" in klass.__dict__:
            descriptor = klass.__dict__["pasma"]
            break
    assert isinstance(descriptor, property)

def test_pes_has_vzdevek():
    assert hasattr(Pes, "vzdevek")
    descriptor = None
    for klass in Pes.__mro__:
        if "vzdevek" in klass.__dict__:
            descriptor = klass.__dict__["vzdevek"]
            break
    assert isinstance(descriptor, property)



def test_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_class_n_is_not_abstract():
    assert not inspect.isabstract(Class_N)


def test_class_n_constructor_exists():
    assert callable(Class_N.__init__)


def test_class_n_constructor_args():
    sig = inspect.signature(Class_N.__init__)
    params = list(sig.parameters.keys())



def test_razredm_is_not_abstract():
    assert not inspect.isabstract(RazredM)


def test_razredm_constructor_exists():
    assert callable(RazredM.__init__)


def test_razredm_constructor_args():
    sig = inspect.signature(RazredM.__init__)
    params = list(sig.parameters.keys())



def test_razredl_is_not_abstract():
    assert not inspect.isabstract(RazredL)


def test_razredl_constructor_exists():
    assert callable(RazredL.__init__)


def test_razredl_constructor_args():
    sig = inspect.signature(RazredL.__init__)
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
RazredK_strategy = st.builds(
    RazredK,
)
RazredH_strategy = st.builds(
    RazredH,
)
RazredJ_strategy = st.builds(
    RazredJ,
)
RazredG_strategy = st.builds(
    RazredG,
)
RazredF_strategy = st.builds(
    RazredF,
)
RazredE_strategy = st.builds(
    RazredE,
)
RazredD_strategy = st.builds(
    RazredD,
)
RazredC_strategy = st.builds(
    RazredC,
    protectedAtribut=
        safe_text,
    packageAtribut=
        safe_text,
    publicAtribut=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    privateAtribut=
        st.integers()
)
RazredB_strategy = st.builds(
    RazredB,
)
RazredA_strategy = st.builds(
    RazredA,
    publicAtribut=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAtribut=
        safe_text,
    privateAtribut=
        st.integers(),
    packageAtribut=
        safe_text
)
BancniRacun_strategy = st.builds(
    BancniRacun,
    aktiven=
        st.booleans(),
    lastnik=
        safe_text,
    stanje=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Lik3_Interface_strategy = st.builds(
    Lik3_Interface,
)
Pravokotnik3_strategy = st.builds(
    Pravokotnik3,
    koordinataX=
        safe_text,
    koordinataY=
        safe_text
)
PravokotniLik_strategy = st.builds(
    PravokotniLik,
    sirina=
        safe_text,
    visina=
        safe_text
)
RazredB2_strategy = st.builds(
    RazredB2,
)
RazredA2_strategy = st.builds(
    RazredA2,
    objektB=
        st.none()
)
Stanovanje_strategy = st.builds(
    Stanovanje,
)
Soba2_strategy = st.builds(
    Soba2,
)
Objekt_strategy = st.builds(
    Objekt,
)
Soba_strategy = st.builds(
    Soba,
)
InterfaceO_Interface1_strategy = st.builds(
    InterfaceO_Interface1,
)
ClassP1_strategy = st.builds(
    ClassP1,
)
Prepoznaven_Interface1_strategy = st.builds(
    Prepoznaven_Interface1,
)
Avtomobil1_strategy = st.builds(
    Avtomobil1,
)
Kolo1_strategy = st.builds(
    Kolo1,
)
Vozen_Interface1_strategy = st.builds(
    Vozen_Interface1,
)
Oddelek2_strategy = st.builds(
    Oddelek2,
)
Oseba4_strategy = st.builds(
    Oseba4,
)
Oseba3_strategy = st.builds(
    Oseba3,
)
Oddelek1_strategy = st.builds(
    Oddelek1,
)
Class_N1_strategy = st.builds(
    Class_N1,
)
RazredM1_strategy = st.builds(
    RazredM1,
)
Class_strategy = st.builds(
    Class,
)
Oddelek_strategy = st.builds(
    Oddelek,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Lik3_strategy = st.builds(
    Lik3,
    x1=
        safe_text,
    x=
        safe_text,
    barva=
        st.none()
)
Pravokotnik1_strategy = st.builds(
    Pravokotnik1,
    stranicaA=
        safe_text,
    stranicaB=
        safe_text
)
BancniRacun1_strategy = st.builds(
    BancniRacun1,
    aktiven=
        st.booleans(),
    lastnik=
        safe_text,
    stanje=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Oseba2_strategy = st.builds(
    Oseba2,
    priimek=
        safe_text,
    datumRojstva=
        st.dates(),
    ime=
        safe_text
)
Oseba1_strategy = st.builds(
    Oseba1,
    emso=
        safe_text,
    ime=
        safe_text,
    priimek=
        safe_text
)
Razred_strategy = st.builds(
    Razred,
    attribute=
        safe_text
)
NakupSkupinskeKarte_UseCase_strategy = st.builds(
    NakupSkupinskeKarte_UseCase,
)
NiVra_ila__UseCase_strategy = st.builds(
    NiVra_ila__UseCase,
)
Preklic__UseCase_strategy = st.builds(
    Preklic__UseCase,
)
ZbiranjeDenarja_UseCase_strategy = st.builds(
    ZbiranjeDenarja_UseCase,
)
NakupPosamezneKarte_UseCase_strategy = st.builds(
    NakupPosamezneKarte_UseCase,
)
Potnik__Actor_strategy = st.builds(
    Potnik__Actor,
)
NiVra_ila_UseCase_strategy = st.builds(
    NiVra_ila_UseCase,
)
Preklic_UseCase_strategy = st.builds(
    Preklic_UseCase,
)
NeDeluje_UseCase_strategy = st.builds(
    NeDeluje_UseCase,
)
NakupKarte_UseCase_strategy = st.builds(
    NakupKarte_UseCase,
)
Potnik_Actor_strategy = st.builds(
    Potnik_Actor,
)
Elipsa_strategy = st.builds(
    Elipsa,
)
Pravokotnik_strategy = st.builds(
    Pravokotnik,
)
Lik1_strategy = st.builds(
    Lik1,
    visina=
        safe_text,
    barva=
        st.none(),
    x1=
        safe_text,
    x=
        safe_text,
    sirina=
        safe_text
)
FileNotFoundException_strategy = st.builds(
    FileNotFoundException,
)
SecurityException_strategy = st.builds(
    SecurityException,
)
IllegalArgumentException_strategy = st.builds(
    IllegalArgumentException,
)
ArithmeticException_strategy = st.builds(
    ArithmeticException,
)
IOException_strategy = st.builds(
    IOException,
)
RuntimeException_strategy = st.builds(
    RuntimeException,
)
Exception_strategy = st.builds(
    Exception,
)
Throwable_strategy = st.builds(
    Throwable,
)
Collection_Interface_strategy = st.builds(
    Collection_Interface,
)
Prepoznaven_Interface_strategy = st.builds(
    Prepoznaven_Interface,
)
Avtomobil_strategy = st.builds(
    Avtomobil,
)
Kolo_strategy = st.builds(
    Kolo,
)
Iterator_Interface_strategy = st.builds(
    Iterator_Interface,
)
Vozen_Interface_strategy = st.builds(
    Vozen_Interface,
)
Krog2_strategy = st.builds(
    Krog2,
)
Lik2_strategy = st.builds(
    Lik2,
    visina=
        safe_text,
    sirina=
        safe_text,
    x=
        safe_text,
    barva=
        st.none(),
    x1=
        safe_text
)
Pravokotnik2_strategy = st.builds(
    Pravokotnik2,
)
PravokotnikA_strategy = st.builds(
    PravokotnikA,
    stranicaB=
        safe_text,
    stranicaA=
        safe_text
)
Color_strategy = st.builds(
    Color,
)
Lik_strategy = st.builds(
    Lik,
    x1=
        safe_text,
    x=
        safe_text,
    barva=
        st.none()
)
RazredB1_strategy = st.builds(
    RazredB1,
)
RazredC1_strategy = st.builds(
    RazredC1,
    stevilo=
        safe_text
)
RazredA1_strategy = st.builds(
    RazredA1,
    stevilo=
        safe_text
)
LocalDate1_strategy = st.builds(
    LocalDate1,
)
Student_strategy = st.builds(
    Student,
    vpisnaStevilka=
        safe_text,
    studijskiProgram=
        safe_text,
    datumVpisa=
        st.none()
)
Zaposlen_strategy = st.builds(
    Zaposlen,
    izobrazba=
        safe_text,
    urnaPostavka=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
LocalDate_strategy = st.builds(
    LocalDate,
)
Oseba_strategy = st.builds(
    Oseba,
    spol=
        safe_text,
    ime=
        safe_text,
    priimek=
        safe_text,
    datumRojstva=
        st.none()
)
Pes_strategy = st.builds(
    Pes,
    visina=
        safe_text,
    pasma=
        safe_text,
    vzdevek=
        safe_text
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)
ClassP_strategy = st.builds(
    ClassP,
)
Class_N_strategy = st.builds(
    Class_N,
)
RazredM_strategy = st.builds(
    RazredM,
)
RazredL_strategy = st.builds(
    RazredL,
)

@given(instance=RazredK_strategy)
@settings(max_examples=50)
def test_razredk_instantiation(instance):
    assert isinstance(instance, RazredK)

@given(instance=RazredH_strategy)
@settings(max_examples=50)
def test_razredh_instantiation(instance):
    assert isinstance(instance, RazredH)

@given(instance=RazredJ_strategy)
@settings(max_examples=50)
def test_razredj_instantiation(instance):
    assert isinstance(instance, RazredJ)

@given(instance=RazredG_strategy)
@settings(max_examples=50)
def test_razredg_instantiation(instance):
    assert isinstance(instance, RazredG)

@given(instance=RazredF_strategy)
@settings(max_examples=50)
def test_razredf_instantiation(instance):
    assert isinstance(instance, RazredF)

@given(instance=RazredE_strategy)
@settings(max_examples=50)
def test_razrede_instantiation(instance):
    assert isinstance(instance, RazredE)

@given(instance=RazredD_strategy)
@settings(max_examples=50)
def test_razredd_instantiation(instance):
    assert isinstance(instance, RazredD)

@given(instance=RazredC_strategy)
@settings(max_examples=50)
def test_razredc_instantiation(instance):
    assert isinstance(instance, RazredC)



@given(instance=RazredC_strategy)
def test_razredc_protectedAtribut_setter(instance):
    original = instance.protectedAtribut
    instance.protectedAtribut = original
    assert instance.protectedAtribut == original



@given(instance=RazredC_strategy)
def test_razredc_packageAtribut_setter(instance):
    original = instance.packageAtribut
    instance.packageAtribut = original
    assert instance.packageAtribut == original



@given(instance=RazredC_strategy)
def test_razredc_publicAtribut_setter(instance):
    original = instance.publicAtribut
    instance.publicAtribut = original
    assert instance.publicAtribut == original



@given(instance=RazredC_strategy)
def test_razredc_privateAtribut_setter(instance):
    original = instance.privateAtribut
    instance.privateAtribut = original
    assert instance.privateAtribut == original

@given(instance=RazredB_strategy)
@settings(max_examples=50)
def test_razredb_instantiation(instance):
    assert isinstance(instance, RazredB)

@given(instance=RazredA_strategy)
@settings(max_examples=50)
def test_razreda_instantiation(instance):
    assert isinstance(instance, RazredA)



@given(instance=RazredA_strategy)
def test_razreda_publicAtribut_setter(instance):
    original = instance.publicAtribut
    instance.publicAtribut = original
    assert instance.publicAtribut == original



@given(instance=RazredA_strategy)
def test_razreda_protectedAtribut_setter(instance):
    original = instance.protectedAtribut
    instance.protectedAtribut = original
    assert instance.protectedAtribut == original



@given(instance=RazredA_strategy)
def test_razreda_privateAtribut_setter(instance):
    original = instance.privateAtribut
    instance.privateAtribut = original
    assert instance.privateAtribut == original



@given(instance=RazredA_strategy)
def test_razreda_packageAtribut_setter(instance):
    original = instance.packageAtribut
    instance.packageAtribut = original
    assert instance.packageAtribut == original

@given(instance=BancniRacun_strategy)
@settings(max_examples=50)
def test_bancniracun_instantiation(instance):
    assert isinstance(instance, BancniRacun)



@given(instance=BancniRacun_strategy)
def test_bancniracun_aktiven_setter(instance):
    original = instance.aktiven
    instance.aktiven = original
    assert instance.aktiven == original



@given(instance=BancniRacun_strategy)
def test_bancniracun_lastnik_setter(instance):
    original = instance.lastnik
    instance.lastnik = original
    assert instance.lastnik == original



@given(instance=BancniRacun_strategy)
def test_bancniracun_stanje_setter(instance):
    original = instance.stanje
    instance.stanje = original
    assert instance.stanje == original

@given(instance=Lik3_Interface_strategy)
@settings(max_examples=50)
def test_lik3_interface_instantiation(instance):
    assert isinstance(instance, Lik3_Interface)

@given(instance=Pravokotnik3_strategy)
@settings(max_examples=50)
def test_pravokotnik3_instantiation(instance):
    assert isinstance(instance, Pravokotnik3)



@given(instance=Pravokotnik3_strategy)
def test_pravokotnik3_koordinataX_setter(instance):
    original = instance.koordinataX
    instance.koordinataX = original
    assert instance.koordinataX == original



@given(instance=Pravokotnik3_strategy)
def test_pravokotnik3_koordinataY_setter(instance):
    original = instance.koordinataY
    instance.koordinataY = original
    assert instance.koordinataY == original

@given(instance=PravokotniLik_strategy)
@settings(max_examples=50)
def test_pravokotnilik_instantiation(instance):
    assert isinstance(instance, PravokotniLik)



@given(instance=PravokotniLik_strategy)
def test_pravokotnilik_sirina_setter(instance):
    original = instance.sirina
    instance.sirina = original
    assert instance.sirina == original



@given(instance=PravokotniLik_strategy)
def test_pravokotnilik_visina_setter(instance):
    original = instance.visina
    instance.visina = original
    assert instance.visina == original

@given(instance=RazredB2_strategy)
@settings(max_examples=50)
def test_razredb2_instantiation(instance):
    assert isinstance(instance, RazredB2)

@given(instance=RazredA2_strategy)
@settings(max_examples=50)
def test_razreda2_instantiation(instance):
    assert isinstance(instance, RazredA2)



@given(instance=RazredA2_strategy)
def test_razreda2_objektB_setter(instance):
    original = instance.objektB
    instance.objektB = original
    assert instance.objektB == original

@given(instance=Stanovanje_strategy)
@settings(max_examples=50)
def test_stanovanje_instantiation(instance):
    assert isinstance(instance, Stanovanje)

@given(instance=Soba2_strategy)
@settings(max_examples=50)
def test_soba2_instantiation(instance):
    assert isinstance(instance, Soba2)

@given(instance=Objekt_strategy)
@settings(max_examples=50)
def test_objekt_instantiation(instance):
    assert isinstance(instance, Objekt)

@given(instance=Soba_strategy)
@settings(max_examples=50)
def test_soba_instantiation(instance):
    assert isinstance(instance, Soba)

@given(instance=InterfaceO_Interface1_strategy)
@settings(max_examples=50)
def test_interfaceo_interface1_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface1)

@given(instance=ClassP1_strategy)
@settings(max_examples=50)
def test_classp1_instantiation(instance):
    assert isinstance(instance, ClassP1)

@given(instance=Prepoznaven_Interface1_strategy)
@settings(max_examples=50)
def test_prepoznaven_interface1_instantiation(instance):
    assert isinstance(instance, Prepoznaven_Interface1)

@given(instance=Avtomobil1_strategy)
@settings(max_examples=50)
def test_avtomobil1_instantiation(instance):
    assert isinstance(instance, Avtomobil1)

@given(instance=Kolo1_strategy)
@settings(max_examples=50)
def test_kolo1_instantiation(instance):
    assert isinstance(instance, Kolo1)

@given(instance=Vozen_Interface1_strategy)
@settings(max_examples=50)
def test_vozen_interface1_instantiation(instance):
    assert isinstance(instance, Vozen_Interface1)

@given(instance=Oddelek2_strategy)
@settings(max_examples=50)
def test_oddelek2_instantiation(instance):
    assert isinstance(instance, Oddelek2)

@given(instance=Oseba4_strategy)
@settings(max_examples=50)
def test_oseba4_instantiation(instance):
    assert isinstance(instance, Oseba4)

@given(instance=Oseba3_strategy)
@settings(max_examples=50)
def test_oseba3_instantiation(instance):
    assert isinstance(instance, Oseba3)

@given(instance=Oddelek1_strategy)
@settings(max_examples=50)
def test_oddelek1_instantiation(instance):
    assert isinstance(instance, Oddelek1)

@given(instance=Class_N1_strategy)
@settings(max_examples=50)
def test_class_n1_instantiation(instance):
    assert isinstance(instance, Class_N1)

@given(instance=RazredM1_strategy)
@settings(max_examples=50)
def test_razredm1_instantiation(instance):
    assert isinstance(instance, RazredM1)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Oddelek_strategy)
@settings(max_examples=50)
def test_oddelek_instantiation(instance):
    assert isinstance(instance, Oddelek)

@given(instance=Interface_Interface_strategy)
@settings(max_examples=50)
def test_interface_interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)

@given(instance=Lik3_strategy)
@settings(max_examples=50)
def test_lik3_instantiation(instance):
    assert isinstance(instance, Lik3)



@given(instance=Lik3_strategy)
def test_lik3_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=Lik3_strategy)
def test_lik3_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Lik3_strategy)
def test_lik3_barva_setter(instance):
    original = instance.barva
    instance.barva = original
    assert instance.barva == original

@given(instance=Pravokotnik1_strategy)
@settings(max_examples=50)
def test_pravokotnik1_instantiation(instance):
    assert isinstance(instance, Pravokotnik1)



@given(instance=Pravokotnik1_strategy)
def test_pravokotnik1_stranicaA_setter(instance):
    original = instance.stranicaA
    instance.stranicaA = original
    assert instance.stranicaA == original



@given(instance=Pravokotnik1_strategy)
def test_pravokotnik1_stranicaB_setter(instance):
    original = instance.stranicaB
    instance.stranicaB = original
    assert instance.stranicaB == original

@given(instance=BancniRacun1_strategy)
@settings(max_examples=50)
def test_bancniracun1_instantiation(instance):
    assert isinstance(instance, BancniRacun1)



@given(instance=BancniRacun1_strategy)
def test_bancniracun1_aktiven_setter(instance):
    original = instance.aktiven
    instance.aktiven = original
    assert instance.aktiven == original



@given(instance=BancniRacun1_strategy)
def test_bancniracun1_lastnik_setter(instance):
    original = instance.lastnik
    instance.lastnik = original
    assert instance.lastnik == original



@given(instance=BancniRacun1_strategy)
def test_bancniracun1_stanje_setter(instance):
    original = instance.stanje
    instance.stanje = original
    assert instance.stanje == original

@given(instance=Oseba2_strategy)
@settings(max_examples=50)
def test_oseba2_instantiation(instance):
    assert isinstance(instance, Oseba2)



@given(instance=Oseba2_strategy)
def test_oseba2_priimek_setter(instance):
    original = instance.priimek
    instance.priimek = original
    assert instance.priimek == original



@given(instance=Oseba2_strategy)
def test_oseba2_datumRojstva_setter(instance):
    original = instance.datumRojstva
    instance.datumRojstva = original
    assert instance.datumRojstva == original



@given(instance=Oseba2_strategy)
def test_oseba2_ime_setter(instance):
    original = instance.ime
    instance.ime = original
    assert instance.ime == original

@given(instance=Oseba1_strategy)
@settings(max_examples=50)
def test_oseba1_instantiation(instance):
    assert isinstance(instance, Oseba1)



@given(instance=Oseba1_strategy)
def test_oseba1_emso_setter(instance):
    original = instance.emso
    instance.emso = original
    assert instance.emso == original



@given(instance=Oseba1_strategy)
def test_oseba1_ime_setter(instance):
    original = instance.ime
    instance.ime = original
    assert instance.ime == original



@given(instance=Oseba1_strategy)
def test_oseba1_priimek_setter(instance):
    original = instance.priimek
    instance.priimek = original
    assert instance.priimek == original

@given(instance=Razred_strategy)
@settings(max_examples=50)
def test_razred_instantiation(instance):
    assert isinstance(instance, Razred)



@given(instance=Razred_strategy)
def test_razred_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=NakupSkupinskeKarte_UseCase_strategy)
@settings(max_examples=50)
def test_nakupskupinskekarte_usecase_instantiation(instance):
    assert isinstance(instance, NakupSkupinskeKarte_UseCase)

@given(instance=NiVra_ila__UseCase_strategy)
@settings(max_examples=50)
def test_nivra_ila__usecase_instantiation(instance):
    assert isinstance(instance, NiVra_ila__UseCase)

@given(instance=Preklic__UseCase_strategy)
@settings(max_examples=50)
def test_preklic__usecase_instantiation(instance):
    assert isinstance(instance, Preklic__UseCase)

@given(instance=ZbiranjeDenarja_UseCase_strategy)
@settings(max_examples=50)
def test_zbiranjedenarja_usecase_instantiation(instance):
    assert isinstance(instance, ZbiranjeDenarja_UseCase)

@given(instance=NakupPosamezneKarte_UseCase_strategy)
@settings(max_examples=50)
def test_nakupposameznekarte_usecase_instantiation(instance):
    assert isinstance(instance, NakupPosamezneKarte_UseCase)

@given(instance=Potnik__Actor_strategy)
@settings(max_examples=50)
def test_potnik__actor_instantiation(instance):
    assert isinstance(instance, Potnik__Actor)

@given(instance=NiVra_ila_UseCase_strategy)
@settings(max_examples=50)
def test_nivra_ila_usecase_instantiation(instance):
    assert isinstance(instance, NiVra_ila_UseCase)

@given(instance=Preklic_UseCase_strategy)
@settings(max_examples=50)
def test_preklic_usecase_instantiation(instance):
    assert isinstance(instance, Preklic_UseCase)

@given(instance=NeDeluje_UseCase_strategy)
@settings(max_examples=50)
def test_nedeluje_usecase_instantiation(instance):
    assert isinstance(instance, NeDeluje_UseCase)

@given(instance=NakupKarte_UseCase_strategy)
@settings(max_examples=50)
def test_nakupkarte_usecase_instantiation(instance):
    assert isinstance(instance, NakupKarte_UseCase)

@given(instance=Potnik_Actor_strategy)
@settings(max_examples=50)
def test_potnik_actor_instantiation(instance):
    assert isinstance(instance, Potnik_Actor)

@given(instance=Elipsa_strategy)
@settings(max_examples=50)
def test_elipsa_instantiation(instance):
    assert isinstance(instance, Elipsa)

@given(instance=Pravokotnik_strategy)
@settings(max_examples=50)
def test_pravokotnik_instantiation(instance):
    assert isinstance(instance, Pravokotnik)

@given(instance=Lik1_strategy)
@settings(max_examples=50)
def test_lik1_instantiation(instance):
    assert isinstance(instance, Lik1)



@given(instance=Lik1_strategy)
def test_lik1_visina_setter(instance):
    original = instance.visina
    instance.visina = original
    assert instance.visina == original



@given(instance=Lik1_strategy)
def test_lik1_barva_setter(instance):
    original = instance.barva
    instance.barva = original
    assert instance.barva == original



@given(instance=Lik1_strategy)
def test_lik1_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=Lik1_strategy)
def test_lik1_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Lik1_strategy)
def test_lik1_sirina_setter(instance):
    original = instance.sirina
    instance.sirina = original
    assert instance.sirina == original

@given(instance=FileNotFoundException_strategy)
@settings(max_examples=50)
def test_filenotfoundexception_instantiation(instance):
    assert isinstance(instance, FileNotFoundException)

@given(instance=SecurityException_strategy)
@settings(max_examples=50)
def test_securityexception_instantiation(instance):
    assert isinstance(instance, SecurityException)

@given(instance=IllegalArgumentException_strategy)
@settings(max_examples=50)
def test_illegalargumentexception_instantiation(instance):
    assert isinstance(instance, IllegalArgumentException)

@given(instance=ArithmeticException_strategy)
@settings(max_examples=50)
def test_arithmeticexception_instantiation(instance):
    assert isinstance(instance, ArithmeticException)

@given(instance=IOException_strategy)
@settings(max_examples=50)
def test_ioexception_instantiation(instance):
    assert isinstance(instance, IOException)

@given(instance=RuntimeException_strategy)
@settings(max_examples=50)
def test_runtimeexception_instantiation(instance):
    assert isinstance(instance, RuntimeException)

@given(instance=Exception_strategy)
@settings(max_examples=50)
def test_exception_instantiation(instance):
    assert isinstance(instance, Exception)

@given(instance=Throwable_strategy)
@settings(max_examples=50)
def test_throwable_instantiation(instance):
    assert isinstance(instance, Throwable)

@given(instance=Collection_Interface_strategy)
@settings(max_examples=50)
def test_collection_interface_instantiation(instance):
    assert isinstance(instance, Collection_Interface)

@given(instance=Prepoznaven_Interface_strategy)
@settings(max_examples=50)
def test_prepoznaven_interface_instantiation(instance):
    assert isinstance(instance, Prepoznaven_Interface)

@given(instance=Avtomobil_strategy)
@settings(max_examples=50)
def test_avtomobil_instantiation(instance):
    assert isinstance(instance, Avtomobil)

@given(instance=Kolo_strategy)
@settings(max_examples=50)
def test_kolo_instantiation(instance):
    assert isinstance(instance, Kolo)

@given(instance=Iterator_Interface_strategy)
@settings(max_examples=50)
def test_iterator_interface_instantiation(instance):
    assert isinstance(instance, Iterator_Interface)

@given(instance=Vozen_Interface_strategy)
@settings(max_examples=50)
def test_vozen_interface_instantiation(instance):
    assert isinstance(instance, Vozen_Interface)

@given(instance=Krog2_strategy)
@settings(max_examples=50)
def test_krog2_instantiation(instance):
    assert isinstance(instance, Krog2)

@given(instance=Lik2_strategy)
@settings(max_examples=50)
def test_lik2_instantiation(instance):
    assert isinstance(instance, Lik2)



@given(instance=Lik2_strategy)
def test_lik2_visina_setter(instance):
    original = instance.visina
    instance.visina = original
    assert instance.visina == original



@given(instance=Lik2_strategy)
def test_lik2_sirina_setter(instance):
    original = instance.sirina
    instance.sirina = original
    assert instance.sirina == original



@given(instance=Lik2_strategy)
def test_lik2_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Lik2_strategy)
def test_lik2_barva_setter(instance):
    original = instance.barva
    instance.barva = original
    assert instance.barva == original



@given(instance=Lik2_strategy)
def test_lik2_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original

@given(instance=Pravokotnik2_strategy)
@settings(max_examples=50)
def test_pravokotnik2_instantiation(instance):
    assert isinstance(instance, Pravokotnik2)

@given(instance=PravokotnikA_strategy)
@settings(max_examples=50)
def test_pravokotnika_instantiation(instance):
    assert isinstance(instance, PravokotnikA)



@given(instance=PravokotnikA_strategy)
def test_pravokotnika_stranicaB_setter(instance):
    original = instance.stranicaB
    instance.stranicaB = original
    assert instance.stranicaB == original



@given(instance=PravokotnikA_strategy)
def test_pravokotnika_stranicaA_setter(instance):
    original = instance.stranicaA
    instance.stranicaA = original
    assert instance.stranicaA == original

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=Lik_strategy)
@settings(max_examples=50)
def test_lik_instantiation(instance):
    assert isinstance(instance, Lik)



@given(instance=Lik_strategy)
def test_lik_x1_setter(instance):
    original = instance.x1
    instance.x1 = original
    assert instance.x1 == original



@given(instance=Lik_strategy)
def test_lik_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=Lik_strategy)
def test_lik_barva_setter(instance):
    original = instance.barva
    instance.barva = original
    assert instance.barva == original

@given(instance=RazredB1_strategy)
@settings(max_examples=50)
def test_razredb1_instantiation(instance):
    assert isinstance(instance, RazredB1)

@given(instance=RazredC1_strategy)
@settings(max_examples=50)
def test_razredc1_instantiation(instance):
    assert isinstance(instance, RazredC1)



@given(instance=RazredC1_strategy)
def test_razredc1_stevilo_setter(instance):
    original = instance.stevilo
    instance.stevilo = original
    assert instance.stevilo == original

@given(instance=RazredA1_strategy)
@settings(max_examples=50)
def test_razreda1_instantiation(instance):
    assert isinstance(instance, RazredA1)



@given(instance=RazredA1_strategy)
def test_razreda1_stevilo_setter(instance):
    original = instance.stevilo
    instance.stevilo = original
    assert instance.stevilo == original

@given(instance=LocalDate1_strategy)
@settings(max_examples=50)
def test_localdate1_instantiation(instance):
    assert isinstance(instance, LocalDate1)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_vpisnaStevilka_setter(instance):
    original = instance.vpisnaStevilka
    instance.vpisnaStevilka = original
    assert instance.vpisnaStevilka == original



@given(instance=Student_strategy)
def test_student_studijskiProgram_setter(instance):
    original = instance.studijskiProgram
    instance.studijskiProgram = original
    assert instance.studijskiProgram == original



@given(instance=Student_strategy)
def test_student_datumVpisa_setter(instance):
    original = instance.datumVpisa
    instance.datumVpisa = original
    assert instance.datumVpisa == original

@given(instance=Zaposlen_strategy)
@settings(max_examples=50)
def test_zaposlen_instantiation(instance):
    assert isinstance(instance, Zaposlen)



@given(instance=Zaposlen_strategy)
def test_zaposlen_izobrazba_setter(instance):
    original = instance.izobrazba
    instance.izobrazba = original
    assert instance.izobrazba == original



@given(instance=Zaposlen_strategy)
def test_zaposlen_urnaPostavka_setter(instance):
    original = instance.urnaPostavka
    instance.urnaPostavka = original
    assert instance.urnaPostavka == original

@given(instance=LocalDate_strategy)
@settings(max_examples=50)
def test_localdate_instantiation(instance):
    assert isinstance(instance, LocalDate)

@given(instance=Oseba_strategy)
@settings(max_examples=50)
def test_oseba_instantiation(instance):
    assert isinstance(instance, Oseba)



@given(instance=Oseba_strategy)
def test_oseba_spol_setter(instance):
    original = instance.spol
    instance.spol = original
    assert instance.spol == original



@given(instance=Oseba_strategy)
def test_oseba_ime_setter(instance):
    original = instance.ime
    instance.ime = original
    assert instance.ime == original



@given(instance=Oseba_strategy)
def test_oseba_priimek_setter(instance):
    original = instance.priimek
    instance.priimek = original
    assert instance.priimek == original



@given(instance=Oseba_strategy)
def test_oseba_datumRojstva_setter(instance):
    original = instance.datumRojstva
    instance.datumRojstva = original
    assert instance.datumRojstva == original

@given(instance=Pes_strategy)
@settings(max_examples=50)
def test_pes_instantiation(instance):
    assert isinstance(instance, Pes)



@given(instance=Pes_strategy)
def test_pes_visina_setter(instance):
    original = instance.visina
    instance.visina = original
    assert instance.visina == original



@given(instance=Pes_strategy)
def test_pes_pasma_setter(instance):
    original = instance.pasma
    instance.pasma = original
    assert instance.pasma == original



@given(instance=Pes_strategy)
def test_pes_vzdevek_setter(instance):
    original = instance.vzdevek
    instance.vzdevek = original
    assert instance.vzdevek == original

@given(instance=ClassV_strategy)
@settings(max_examples=50)
def test_classv_instantiation(instance):
    assert isinstance(instance, ClassV)

@given(instance=ClassU_strategy)
@settings(max_examples=50)
def test_classu_instantiation(instance):
    assert isinstance(instance, ClassU)

@given(instance=ClassT_strategy)
@settings(max_examples=50)
def test_classt_instantiation(instance):
    assert isinstance(instance, ClassT)

@given(instance=ClassS_strategy)
@settings(max_examples=50)
def test_classs_instantiation(instance):
    assert isinstance(instance, ClassS)

@given(instance=ClassR_strategy)
@settings(max_examples=50)
def test_classr_instantiation(instance):
    assert isinstance(instance, ClassR)

@given(instance=ClassQ_strategy)
@settings(max_examples=50)
def test_classq_instantiation(instance):
    assert isinstance(instance, ClassQ)

@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=50)
def test_interfaceo_interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)

@given(instance=ClassP_strategy)
@settings(max_examples=50)
def test_classp_instantiation(instance):
    assert isinstance(instance, ClassP)

@given(instance=Class_N_strategy)
@settings(max_examples=50)
def test_class_n_instantiation(instance):
    assert isinstance(instance, Class_N)

@given(instance=RazredM_strategy)
@settings(max_examples=50)
def test_razredm_instantiation(instance):
    assert isinstance(instance, RazredM)

@given(instance=RazredL_strategy)
@settings(max_examples=50)
def test_razredl_instantiation(instance):
    assert isinstance(instance, RazredL)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    KeyPressEventArgs_,
    myException,
    Font_2,
    Font_,
    ThreadExceptionEventArgs_,
    Object_,
    App,
    Groesse_,
    PL_Form_,
    PL_Groesse_,
    List_TeigRezept___,
    Array_Zutat___,
    List_DekorRezept___,
    List_PlaetzchenForm___,
    List_Zutat___,
    GussRezept,
    Zutat_,
    Rezept,
    DekorRezept,
    GUIRezept,
    String_,
    PlaetzchenForm_,
    ComboBox,
    Plaetzchen_,
    Plaetzchen,
    TeigRezept_,
    TeigRezept,
    KonfigDatei_,
    KonfigDatei,
    GUIKeksform,
    GUI,
    Groesse,
    PlaetzchenForm,
    Zutat,
    PL_Form,
    PL_Groesse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_keypresseventargs__is_not_abstract():
    assert not inspect.isabstract(KeyPressEventArgs_)


def test_keypresseventargs__constructor_exists():
    assert callable(KeyPressEventArgs_.__init__)


def test_keypresseventargs__constructor_args():
    sig = inspect.signature(KeyPressEventArgs_.__init__)
    params = list(sig.parameters.keys())



def test_myexception_is_not_abstract():
    assert not inspect.isabstract(myException)


def test_myexception_constructor_exists():
    assert callable(myException.__init__)


def test_myexception_constructor_args():
    sig = inspect.signature(myException.__init__)
    params = list(sig.parameters.keys())



def test_font_2_is_not_abstract():
    assert not inspect.isabstract(Font_2)


def test_font_2_constructor_exists():
    assert callable(Font_2.__init__)


def test_font_2_constructor_args():
    sig = inspect.signature(Font_2.__init__)
    params = list(sig.parameters.keys())



def test_font__is_not_abstract():
    assert not inspect.isabstract(Font_)


def test_font__constructor_exists():
    assert callable(Font_.__init__)


def test_font__constructor_args():
    sig = inspect.signature(Font_.__init__)
    params = list(sig.parameters.keys())



def test_threadexceptioneventargs__is_not_abstract():
    assert not inspect.isabstract(ThreadExceptionEventArgs_)


def test_threadexceptioneventargs__constructor_exists():
    assert callable(ThreadExceptionEventArgs_.__init__)


def test_threadexceptioneventargs__constructor_args():
    sig = inspect.signature(ThreadExceptionEventArgs_.__init__)
    params = list(sig.parameters.keys())



def test_object__is_not_abstract():
    assert not inspect.isabstract(Object_)


def test_object__constructor_exists():
    assert callable(Object_.__init__)


def test_object__constructor_args():
    sig = inspect.signature(Object_.__init__)
    params = list(sig.parameters.keys())



def test_app_is_not_abstract():
    assert not inspect.isabstract(App)


def test_app_constructor_exists():
    assert callable(App.__init__)


def test_app_constructor_args():
    sig = inspect.signature(App.__init__)
    params = list(sig.parameters.keys())



def test_groesse__is_not_abstract():
    assert not inspect.isabstract(Groesse_)


def test_groesse__constructor_exists():
    assert callable(Groesse_.__init__)


def test_groesse__constructor_args():
    sig = inspect.signature(Groesse_.__init__)
    params = list(sig.parameters.keys())



def test_pl_form__is_not_abstract():
    assert not inspect.isabstract(PL_Form_)


def test_pl_form__constructor_exists():
    assert callable(PL_Form_.__init__)


def test_pl_form__constructor_args():
    sig = inspect.signature(PL_Form_.__init__)
    params = list(sig.parameters.keys())



def test_pl_groesse__is_not_abstract():
    assert not inspect.isabstract(PL_Groesse_)


def test_pl_groesse__constructor_exists():
    assert callable(PL_Groesse_.__init__)


def test_pl_groesse__constructor_args():
    sig = inspect.signature(PL_Groesse_.__init__)
    params = list(sig.parameters.keys())



def test_list_teigrezept____is_not_abstract():
    assert not inspect.isabstract(List_TeigRezept___)


def test_list_teigrezept____constructor_exists():
    assert callable(List_TeigRezept___.__init__)


def test_list_teigrezept____constructor_args():
    sig = inspect.signature(List_TeigRezept___.__init__)
    params = list(sig.parameters.keys())



def test_array_zutat____is_not_abstract():
    assert not inspect.isabstract(Array_Zutat___)


def test_array_zutat____constructor_exists():
    assert callable(Array_Zutat___.__init__)


def test_array_zutat____constructor_args():
    sig = inspect.signature(Array_Zutat___.__init__)
    params = list(sig.parameters.keys())



def test_list_dekorrezept____is_not_abstract():
    assert not inspect.isabstract(List_DekorRezept___)


def test_list_dekorrezept____constructor_exists():
    assert callable(List_DekorRezept___.__init__)


def test_list_dekorrezept____constructor_args():
    sig = inspect.signature(List_DekorRezept___.__init__)
    params = list(sig.parameters.keys())



def test_list_plaetzchenform____is_not_abstract():
    assert not inspect.isabstract(List_PlaetzchenForm___)


def test_list_plaetzchenform____constructor_exists():
    assert callable(List_PlaetzchenForm___.__init__)


def test_list_plaetzchenform____constructor_args():
    sig = inspect.signature(List_PlaetzchenForm___.__init__)
    params = list(sig.parameters.keys())



def test_list_zutat____is_not_abstract():
    assert not inspect.isabstract(List_Zutat___)


def test_list_zutat____constructor_exists():
    assert callable(List_Zutat___.__init__)


def test_list_zutat____constructor_args():
    sig = inspect.signature(List_Zutat___.__init__)
    params = list(sig.parameters.keys())



def test_gussrezept_is_not_abstract():
    assert not inspect.isabstract(GussRezept)


def test_gussrezept_constructor_exists():
    assert callable(GussRezept.__init__)


def test_gussrezept_constructor_args():
    sig = inspect.signature(GussRezept.__init__)
    params = list(sig.parameters.keys())
    assert "basis" in params, "Missing parameter 'basis'"
    assert "zutat" in params, "Missing parameter 'zutat'"
    assert "basismenge" in params, "Missing parameter 'basismenge'"

def test_gussrezept_has_basis():
    assert hasattr(GussRezept, "basis")
    descriptor = None
    for klass in GussRezept.__mro__:
        if "basis" in klass.__dict__:
            descriptor = klass.__dict__["basis"]
            break
    assert isinstance(descriptor, property)

def test_gussrezept_has_zutat():
    assert hasattr(GussRezept, "zutat")
    descriptor = None
    for klass in GussRezept.__mro__:
        if "zutat" in klass.__dict__:
            descriptor = klass.__dict__["zutat"]
            break
    assert isinstance(descriptor, property)

def test_gussrezept_has_basismenge():
    assert hasattr(GussRezept, "basismenge")
    descriptor = None
    for klass in GussRezept.__mro__:
        if "basismenge" in klass.__dict__:
            descriptor = klass.__dict__["basismenge"]
            break
    assert isinstance(descriptor, property)



def test_zutat__is_not_abstract():
    assert not inspect.isabstract(Zutat_)


def test_zutat__constructor_exists():
    assert callable(Zutat_.__init__)


def test_zutat__constructor_args():
    sig = inspect.signature(Zutat_.__init__)
    params = list(sig.parameters.keys())



def test_rezept_is_not_abstract():
    assert not inspect.isabstract(Rezept)


def test_rezept_constructor_exists():
    assert callable(Rezept.__init__)


def test_rezept_constructor_args():
    sig = inspect.signature(Rezept.__init__)
    params = list(sig.parameters.keys())
    assert "rezeptname" in params, "Missing parameter 'rezeptname'"
    assert "basismenge" in params, "Missing parameter 'basismenge'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "basis" in params, "Missing parameter 'basis'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_rezept_has_rezeptname():
    assert hasattr(Rezept, "rezeptname")
    descriptor = None
    for klass in Rezept.__mro__:
        if "rezeptname" in klass.__dict__:
            descriptor = klass.__dict__["rezeptname"]
            break
    assert isinstance(descriptor, property)

def test_rezept_has_basismenge():
    assert hasattr(Rezept, "basismenge")
    descriptor = None
    for klass in Rezept.__mro__:
        if "basismenge" in klass.__dict__:
            descriptor = klass.__dict__["basismenge"]
            break
    assert isinstance(descriptor, property)

def test_rezept_has_attribute2():
    assert hasattr(Rezept, "attribute2")
    descriptor = None
    for klass in Rezept.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_rezept_has_basis():
    assert hasattr(Rezept, "basis")
    descriptor = None
    for klass in Rezept.__mro__:
        if "basis" in klass.__dict__:
            descriptor = klass.__dict__["basis"]
            break
    assert isinstance(descriptor, property)

def test_rezept_has_attribute():
    assert hasattr(Rezept, "attribute")
    descriptor = None
    for klass in Rezept.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_dekorrezept_is_not_abstract():
    assert not inspect.isabstract(DekorRezept)


def test_dekorrezept_constructor_exists():
    assert callable(DekorRezept.__init__)


def test_dekorrezept_constructor_args():
    sig = inspect.signature(DekorRezept.__init__)
    params = list(sig.parameters.keys())
    assert "basismenge" in params, "Missing parameter 'basismenge'"
    assert "zutaten" in params, "Missing parameter 'zutaten'"
    assert "basis" in params, "Missing parameter 'basis'"
    assert "dekor" in params, "Missing parameter 'dekor'"

def test_dekorrezept_has_basismenge():
    assert hasattr(DekorRezept, "basismenge")
    descriptor = None
    for klass in DekorRezept.__mro__:
        if "basismenge" in klass.__dict__:
            descriptor = klass.__dict__["basismenge"]
            break
    assert isinstance(descriptor, property)

def test_dekorrezept_has_zutaten():
    assert hasattr(DekorRezept, "zutaten")
    descriptor = None
    for klass in DekorRezept.__mro__:
        if "zutaten" in klass.__dict__:
            descriptor = klass.__dict__["zutaten"]
            break
    assert isinstance(descriptor, property)

def test_dekorrezept_has_basis():
    assert hasattr(DekorRezept, "basis")
    descriptor = None
    for klass in DekorRezept.__mro__:
        if "basis" in klass.__dict__:
            descriptor = klass.__dict__["basis"]
            break
    assert isinstance(descriptor, property)

def test_dekorrezept_has_dekor():
    assert hasattr(DekorRezept, "dekor")
    descriptor = None
    for klass in DekorRezept.__mro__:
        if "dekor" in klass.__dict__:
            descriptor = klass.__dict__["dekor"]
            break
    assert isinstance(descriptor, property)



def test_guirezept_is_not_abstract():
    assert not inspect.isabstract(GUIRezept)


def test_guirezept_constructor_exists():
    assert callable(GUIRezept.__init__)


def test_guirezept_constructor_args():
    sig = inspect.signature(GUIRezept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_guirezept_has_name():
    assert hasattr(GUIRezept, "name")
    descriptor = None
    for klass in GUIRezept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_string__is_not_abstract():
    assert not inspect.isabstract(String_)


def test_string__constructor_exists():
    assert callable(String_.__init__)


def test_string__constructor_args():
    sig = inspect.signature(String_.__init__)
    params = list(sig.parameters.keys())



def test_plaetzchenform__is_not_abstract():
    assert not inspect.isabstract(PlaetzchenForm_)


def test_plaetzchenform__constructor_exists():
    assert callable(PlaetzchenForm_.__init__)


def test_plaetzchenform__constructor_args():
    sig = inspect.signature(PlaetzchenForm_.__init__)
    params = list(sig.parameters.keys())



def test_combobox_is_not_abstract():
    assert not inspect.isabstract(ComboBox)


def test_combobox_constructor_exists():
    assert callable(ComboBox.__init__)


def test_combobox_constructor_args():
    sig = inspect.signature(ComboBox.__init__)
    params = list(sig.parameters.keys())



def test_plaetzchen__is_not_abstract():
    assert not inspect.isabstract(Plaetzchen_)


def test_plaetzchen__constructor_exists():
    assert callable(Plaetzchen_.__init__)


def test_plaetzchen__constructor_args():
    sig = inspect.signature(Plaetzchen_.__init__)
    params = list(sig.parameters.keys())



def test_plaetzchen_is_not_abstract():
    assert not inspect.isabstract(Plaetzchen)


def test_plaetzchen_constructor_exists():
    assert callable(Plaetzchen.__init__)


def test_plaetzchen_constructor_args():
    sig = inspect.signature(Plaetzchen.__init__)
    params = list(sig.parameters.keys())
    assert "menge" in params, "Missing parameter 'menge'"
    assert "deko" in params, "Missing parameter 'deko'"
    assert "rezeptTeig" in params, "Missing parameter 'rezeptTeig'"
    assert "form" in params, "Missing parameter 'form'"
    assert "guss" in params, "Missing parameter 'guss'"
    assert "rezeptDeko" in params, "Missing parameter 'rezeptDeko'"
    assert "teig" in params, "Missing parameter 'teig'"
    assert "rezeptGuss" in params, "Missing parameter 'rezeptGuss'"
    assert "name" in params, "Missing parameter 'name'"

def test_plaetzchen_has_menge():
    assert hasattr(Plaetzchen, "menge")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "menge" in klass.__dict__:
            descriptor = klass.__dict__["menge"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_deko():
    assert hasattr(Plaetzchen, "deko")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "deko" in klass.__dict__:
            descriptor = klass.__dict__["deko"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_rezeptTeig():
    assert hasattr(Plaetzchen, "rezeptTeig")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "rezeptTeig" in klass.__dict__:
            descriptor = klass.__dict__["rezeptTeig"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_form():
    assert hasattr(Plaetzchen, "form")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_guss():
    assert hasattr(Plaetzchen, "guss")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "guss" in klass.__dict__:
            descriptor = klass.__dict__["guss"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_rezeptDeko():
    assert hasattr(Plaetzchen, "rezeptDeko")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "rezeptDeko" in klass.__dict__:
            descriptor = klass.__dict__["rezeptDeko"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_teig():
    assert hasattr(Plaetzchen, "teig")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "teig" in klass.__dict__:
            descriptor = klass.__dict__["teig"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_rezeptGuss():
    assert hasattr(Plaetzchen, "rezeptGuss")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "rezeptGuss" in klass.__dict__:
            descriptor = klass.__dict__["rezeptGuss"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchen_has_name():
    assert hasattr(Plaetzchen, "name")
    descriptor = None
    for klass in Plaetzchen.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_teigrezept__is_not_abstract():
    assert not inspect.isabstract(TeigRezept_)


def test_teigrezept__constructor_exists():
    assert callable(TeigRezept_.__init__)


def test_teigrezept__constructor_args():
    sig = inspect.signature(TeigRezept_.__init__)
    params = list(sig.parameters.keys())



def test_teigrezept_is_not_abstract():
    assert not inspect.isabstract(TeigRezept)


def test_teigrezept_constructor_exists():
    assert callable(TeigRezept.__init__)


def test_teigrezept_constructor_args():
    sig = inspect.signature(TeigRezept.__init__)
    params = list(sig.parameters.keys())
    assert "basismenge" in params, "Missing parameter 'basismenge'"
    assert "basis" in params, "Missing parameter 'basis'"
    assert "zutaten" in params, "Missing parameter 'zutaten'"
    assert "backzeit" in params, "Missing parameter 'backzeit'"
    assert "backtemp" in params, "Missing parameter 'backtemp'"

def test_teigrezept_has_basismenge():
    assert hasattr(TeigRezept, "basismenge")
    descriptor = None
    for klass in TeigRezept.__mro__:
        if "basismenge" in klass.__dict__:
            descriptor = klass.__dict__["basismenge"]
            break
    assert isinstance(descriptor, property)

def test_teigrezept_has_basis():
    assert hasattr(TeigRezept, "basis")
    descriptor = None
    for klass in TeigRezept.__mro__:
        if "basis" in klass.__dict__:
            descriptor = klass.__dict__["basis"]
            break
    assert isinstance(descriptor, property)

def test_teigrezept_has_zutaten():
    assert hasattr(TeigRezept, "zutaten")
    descriptor = None
    for klass in TeigRezept.__mro__:
        if "zutaten" in klass.__dict__:
            descriptor = klass.__dict__["zutaten"]
            break
    assert isinstance(descriptor, property)

def test_teigrezept_has_backzeit():
    assert hasattr(TeigRezept, "backzeit")
    descriptor = None
    for klass in TeigRezept.__mro__:
        if "backzeit" in klass.__dict__:
            descriptor = klass.__dict__["backzeit"]
            break
    assert isinstance(descriptor, property)

def test_teigrezept_has_backtemp():
    assert hasattr(TeigRezept, "backtemp")
    descriptor = None
    for klass in TeigRezept.__mro__:
        if "backtemp" in klass.__dict__:
            descriptor = klass.__dict__["backtemp"]
            break
    assert isinstance(descriptor, property)



def test_konfigdatei__is_not_abstract():
    assert not inspect.isabstract(KonfigDatei_)


def test_konfigdatei__constructor_exists():
    assert callable(KonfigDatei_.__init__)


def test_konfigdatei__constructor_args():
    sig = inspect.signature(KonfigDatei_.__init__)
    params = list(sig.parameters.keys())



def test_konfigdatei_is_not_abstract():
    assert not inspect.isabstract(KonfigDatei)


def test_konfigdatei_constructor_exists():
    assert callable(KonfigDatei.__init__)


def test_konfigdatei_constructor_args():
    sig = inspect.signature(KonfigDatei.__init__)
    params = list(sig.parameters.keys())
    assert "menge1" in params, "Missing parameter 'menge1'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "menge" in params, "Missing parameter 'menge'"
    assert "backtemp" in params, "Missing parameter 'backtemp'"
    assert "plaetzchen" in params, "Missing parameter 'plaetzchen'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "backzeit" in params, "Missing parameter 'backzeit'"
    assert "name" in params, "Missing parameter 'name'"

def test_konfigdatei_has_menge1():
    assert hasattr(KonfigDatei, "menge1")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "menge1" in klass.__dict__:
            descriptor = klass.__dict__["menge1"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_attribute():
    assert hasattr(KonfigDatei, "attribute")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_menge():
    assert hasattr(KonfigDatei, "menge")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "menge" in klass.__dict__:
            descriptor = klass.__dict__["menge"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_backtemp():
    assert hasattr(KonfigDatei, "backtemp")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "backtemp" in klass.__dict__:
            descriptor = klass.__dict__["backtemp"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_plaetzchen():
    assert hasattr(KonfigDatei, "plaetzchen")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "plaetzchen" in klass.__dict__:
            descriptor = klass.__dict__["plaetzchen"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_attribute2():
    assert hasattr(KonfigDatei, "attribute2")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_backzeit():
    assert hasattr(KonfigDatei, "backzeit")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "backzeit" in klass.__dict__:
            descriptor = klass.__dict__["backzeit"]
            break
    assert isinstance(descriptor, property)

def test_konfigdatei_has_name():
    assert hasattr(KonfigDatei, "name")
    descriptor = None
    for klass in KonfigDatei.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_guikeksform_is_not_abstract():
    assert not inspect.isabstract(GUIKeksform)


def test_guikeksform_constructor_exists():
    assert callable(GUIKeksform.__init__)


def test_guikeksform_constructor_args():
    sig = inspect.signature(GUIKeksform.__init__)
    params = list(sig.parameters.keys())
    assert "breite" in params, "Missing parameter 'breite'"
    assert "laenge" in params, "Missing parameter 'laenge'"
    assert "name" in params, "Missing parameter 'name'"
    assert "pl__f" in params, "Missing parameter 'pl__f'"

def test_guikeksform_has_breite():
    assert hasattr(GUIKeksform, "breite")
    descriptor = None
    for klass in GUIKeksform.__mro__:
        if "breite" in klass.__dict__:
            descriptor = klass.__dict__["breite"]
            break
    assert isinstance(descriptor, property)

def test_guikeksform_has_laenge():
    assert hasattr(GUIKeksform, "laenge")
    descriptor = None
    for klass in GUIKeksform.__mro__:
        if "laenge" in klass.__dict__:
            descriptor = klass.__dict__["laenge"]
            break
    assert isinstance(descriptor, property)

def test_guikeksform_has_name():
    assert hasattr(GUIKeksform, "name")
    descriptor = None
    for klass in GUIKeksform.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_guikeksform_has_pl__f():
    assert hasattr(GUIKeksform, "pl__f")
    descriptor = None
    for klass in GUIKeksform.__mro__:
        if "pl__f" in klass.__dict__:
            descriptor = klass.__dict__["pl__f"]
            break
    assert isinstance(descriptor, property)



def test_gui_is_not_abstract():
    assert not inspect.isabstract(GUI)


def test_gui_constructor_exists():
    assert callable(GUI.__init__)


def test_gui_constructor_args():
    sig = inspect.signature(GUI.__init__)
    params = list(sig.parameters.keys())
    assert "groesse" in params, "Missing parameter 'groesse'"
    assert "guss" in params, "Missing parameter 'guss'"
    assert "plaetzchenname" in params, "Missing parameter 'plaetzchenname'"
    assert "gussList" in params, "Missing parameter 'gussList'"
    assert "stueckzahl" in params, "Missing parameter 'stueckzahl'"
    assert "dekorList" in params, "Missing parameter 'dekorList'"
    assert "zutatenList" in params, "Missing parameter 'zutatenList'"
    assert "deko" in params, "Missing parameter 'deko'"
    assert "teigsorte" in params, "Missing parameter 'teigsorte'"
    assert "teigList" in params, "Missing parameter 'teigList'"
    assert "plaetzchen" in params, "Missing parameter 'plaetzchen'"
    assert "dateiname" in params, "Missing parameter 'dateiname'"
    assert "datei" in params, "Missing parameter 'datei'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "form" in params, "Missing parameter 'form'"
    assert "plformList" in params, "Missing parameter 'plformList'"

def test_gui_has_groesse():
    assert hasattr(GUI, "groesse")
    descriptor = None
    for klass in GUI.__mro__:
        if "groesse" in klass.__dict__:
            descriptor = klass.__dict__["groesse"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_guss():
    assert hasattr(GUI, "guss")
    descriptor = None
    for klass in GUI.__mro__:
        if "guss" in klass.__dict__:
            descriptor = klass.__dict__["guss"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_plaetzchenname():
    assert hasattr(GUI, "plaetzchenname")
    descriptor = None
    for klass in GUI.__mro__:
        if "plaetzchenname" in klass.__dict__:
            descriptor = klass.__dict__["plaetzchenname"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_gussList():
    assert hasattr(GUI, "gussList")
    descriptor = None
    for klass in GUI.__mro__:
        if "gussList" in klass.__dict__:
            descriptor = klass.__dict__["gussList"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_stueckzahl():
    assert hasattr(GUI, "stueckzahl")
    descriptor = None
    for klass in GUI.__mro__:
        if "stueckzahl" in klass.__dict__:
            descriptor = klass.__dict__["stueckzahl"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_dekorList():
    assert hasattr(GUI, "dekorList")
    descriptor = None
    for klass in GUI.__mro__:
        if "dekorList" in klass.__dict__:
            descriptor = klass.__dict__["dekorList"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_zutatenList():
    assert hasattr(GUI, "zutatenList")
    descriptor = None
    for klass in GUI.__mro__:
        if "zutatenList" in klass.__dict__:
            descriptor = klass.__dict__["zutatenList"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_deko():
    assert hasattr(GUI, "deko")
    descriptor = None
    for klass in GUI.__mro__:
        if "deko" in klass.__dict__:
            descriptor = klass.__dict__["deko"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_teigsorte():
    assert hasattr(GUI, "teigsorte")
    descriptor = None
    for klass in GUI.__mro__:
        if "teigsorte" in klass.__dict__:
            descriptor = klass.__dict__["teigsorte"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_teigList():
    assert hasattr(GUI, "teigList")
    descriptor = None
    for klass in GUI.__mro__:
        if "teigList" in klass.__dict__:
            descriptor = klass.__dict__["teigList"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_plaetzchen():
    assert hasattr(GUI, "plaetzchen")
    descriptor = None
    for klass in GUI.__mro__:
        if "plaetzchen" in klass.__dict__:
            descriptor = klass.__dict__["plaetzchen"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_dateiname():
    assert hasattr(GUI, "dateiname")
    descriptor = None
    for klass in GUI.__mro__:
        if "dateiname" in klass.__dict__:
            descriptor = klass.__dict__["dateiname"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_datei():
    assert hasattr(GUI, "datei")
    descriptor = None
    for klass in GUI.__mro__:
        if "datei" in klass.__dict__:
            descriptor = klass.__dict__["datei"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_attribute():
    assert hasattr(GUI, "attribute")
    descriptor = None
    for klass in GUI.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_form():
    assert hasattr(GUI, "form")
    descriptor = None
    for klass in GUI.__mro__:
        if "form" in klass.__dict__:
            descriptor = klass.__dict__["form"]
            break
    assert isinstance(descriptor, property)

def test_gui_has_plformList():
    assert hasattr(GUI, "plformList")
    descriptor = None
    for klass in GUI.__mro__:
        if "plformList" in klass.__dict__:
            descriptor = klass.__dict__["plformList"]
            break
    assert isinstance(descriptor, property)



def test_groesse_is_not_abstract():
    assert not inspect.isabstract(Groesse)


def test_groesse_constructor_exists():
    assert callable(Groesse.__init__)


def test_groesse_constructor_args():
    sig = inspect.signature(Groesse.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "breite" in params, "Missing parameter 'breite'"
    assert "name1" in params, "Missing parameter 'name1'"
    assert "laenge" in params, "Missing parameter 'laenge'"

def test_groesse_has_name():
    assert hasattr(Groesse, "name")
    descriptor = None
    for klass in Groesse.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_groesse_has_breite():
    assert hasattr(Groesse, "breite")
    descriptor = None
    for klass in Groesse.__mro__:
        if "breite" in klass.__dict__:
            descriptor = klass.__dict__["breite"]
            break
    assert isinstance(descriptor, property)

def test_groesse_has_name1():
    assert hasattr(Groesse, "name1")
    descriptor = None
    for klass in Groesse.__mro__:
        if "name1" in klass.__dict__:
            descriptor = klass.__dict__["name1"]
            break
    assert isinstance(descriptor, property)

def test_groesse_has_laenge():
    assert hasattr(Groesse, "laenge")
    descriptor = None
    for klass in Groesse.__mro__:
        if "laenge" in klass.__dict__:
            descriptor = klass.__dict__["laenge"]
            break
    assert isinstance(descriptor, property)



def test_plaetzchenform_is_not_abstract():
    assert not inspect.isabstract(PlaetzchenForm)


def test_plaetzchenform_constructor_exists():
    assert callable(PlaetzchenForm.__init__)


def test_plaetzchenform_constructor_args():
    sig = inspect.signature(PlaetzchenForm.__init__)
    params = list(sig.parameters.keys())
    assert "faktor" in params, "Missing parameter 'faktor'"
    assert "pl_groesse" in params, "Missing parameter 'pl_groesse'"
    assert "pl_form" in params, "Missing parameter 'pl_form'"

def test_plaetzchenform_has_faktor():
    assert hasattr(PlaetzchenForm, "faktor")
    descriptor = None
    for klass in PlaetzchenForm.__mro__:
        if "faktor" in klass.__dict__:
            descriptor = klass.__dict__["faktor"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchenform_has_pl_groesse():
    assert hasattr(PlaetzchenForm, "pl_groesse")
    descriptor = None
    for klass in PlaetzchenForm.__mro__:
        if "pl_groesse" in klass.__dict__:
            descriptor = klass.__dict__["pl_groesse"]
            break
    assert isinstance(descriptor, property)

def test_plaetzchenform_has_pl_form():
    assert hasattr(PlaetzchenForm, "pl_form")
    descriptor = None
    for klass in PlaetzchenForm.__mro__:
        if "pl_form" in klass.__dict__:
            descriptor = klass.__dict__["pl_form"]
            break
    assert isinstance(descriptor, property)



def test_zutat_is_not_abstract():
    assert not inspect.isabstract(Zutat)


def test_zutat_constructor_exists():
    assert callable(Zutat.__init__)


def test_zutat_constructor_args():
    sig = inspect.signature(Zutat.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "einheit" in params, "Missing parameter 'einheit'"
    assert "menge" in params, "Missing parameter 'menge'"

def test_zutat_has_name():
    assert hasattr(Zutat, "name")
    descriptor = None
    for klass in Zutat.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_zutat_has_einheit():
    assert hasattr(Zutat, "einheit")
    descriptor = None
    for klass in Zutat.__mro__:
        if "einheit" in klass.__dict__:
            descriptor = klass.__dict__["einheit"]
            break
    assert isinstance(descriptor, property)

def test_zutat_has_menge():
    assert hasattr(Zutat, "menge")
    descriptor = None
    for klass in Zutat.__mro__:
        if "menge" in klass.__dict__:
            descriptor = klass.__dict__["menge"]
            break
    assert isinstance(descriptor, property)

def test_pl_form_exists():
    # Check that the Enumeration exists
    assert PL_Form is not None

def test_pl_form_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PL_Form]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PL_Form"

def test_pl_groesse_exists():
    # Check that the Enumeration exists
    assert PL_Groesse is not None

def test_pl_groesse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PL_Groesse]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PL_Groesse"


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
KeyPressEventArgs__strategy = st.builds(
    KeyPressEventArgs_,
)
myException_strategy = st.builds(
    myException,
)
Font_2_strategy = st.builds(
    Font_2,
)
Font__strategy = st.builds(
    Font_,
)
ThreadExceptionEventArgs__strategy = st.builds(
    ThreadExceptionEventArgs_,
)
Object__strategy = st.builds(
    Object_,
)
App_strategy = st.builds(
    App,
)
Groesse__strategy = st.builds(
    Groesse_,
)
PL_Form__strategy = st.builds(
    PL_Form_,
)
PL_Groesse__strategy = st.builds(
    PL_Groesse_,
)
List_TeigRezept____strategy = st.builds(
    List_TeigRezept___,
)
Array_Zutat____strategy = st.builds(
    Array_Zutat___,
)
List_DekorRezept____strategy = st.builds(
    List_DekorRezept___,
)
List_PlaetzchenForm____strategy = st.builds(
    List_PlaetzchenForm___,
)
List_Zutat____strategy = st.builds(
    List_Zutat___,
)
GussRezept_strategy = st.builds(
    GussRezept,
    basis=
        st.none(),
    zutat=
        st.none(),
    basismenge=
        st.integers()
)
Zutat__strategy = st.builds(
    Zutat_,
)
Rezept_strategy = st.builds(
    Rezept,
    rezeptname=
        st.none(),
    basismenge=
        st.integers(),
    attribute2=
        safe_text,
    basis=
        st.none(),
    attribute=
        safe_text
)
DekorRezept_strategy = st.builds(
    DekorRezept,
    basismenge=
        st.integers(),
    zutaten=
        st.none(),
    basis=
        st.none(),
    dekor=
        st.none()
)
GUIRezept_strategy = st.builds(
    GUIRezept,
    name=
        safe_text
)
String__strategy = st.builds(
    String_,
)
PlaetzchenForm__strategy = st.builds(
    PlaetzchenForm_,
)
ComboBox_strategy = st.builds(
    ComboBox,
)
Plaetzchen__strategy = st.builds(
    Plaetzchen_,
)
Plaetzchen_strategy = st.builds(
    Plaetzchen,
    menge=
        st.integers(),
    deko=
        st.none(),
    rezeptTeig=
        st.none(),
    form=
        st.none(),
    guss=
        st.none(),
    rezeptDeko=
        safe_text,
    teig=
        st.none(),
    rezeptGuss=
        safe_text,
    name=
        st.none()
)
TeigRezept__strategy = st.builds(
    TeigRezept_,
)
TeigRezept_strategy = st.builds(
    TeigRezept,
    basismenge=
        st.integers(),
    basis=
        st.none(),
    zutaten=
        st.none(),
    backzeit=
        st.integers(),
    backtemp=
        st.integers()
)
KonfigDatei__strategy = st.builds(
    KonfigDatei_,
)
KonfigDatei_strategy = st.builds(
    KonfigDatei,
    menge1=
        st.integers(),
    attribute=
        safe_text,
    menge=
        st.integers(),
    backtemp=
        st.integers(),
    plaetzchen=
        st.none(),
    attribute2=
        safe_text,
    backzeit=
        st.integers(),
    name=
        st.none()
)
GUIKeksform_strategy = st.builds(
    GUIKeksform,
    breite=
        st.integers(),
    laenge=
        st.integers(),
    name=
        safe_text,
    pl__f=
        st.none()
)
GUI_strategy = st.builds(
    GUI,
    groesse=
        st.none(),
    guss=
        st.none(),
    plaetzchenname=
        safe_text,
    gussList=
        st.none(),
    stueckzahl=
        safe_text,
    dekorList=
        st.none(),
    zutatenList=
        st.none(),
    deko=
        st.none(),
    teigsorte=
        st.none(),
    teigList=
        st.none(),
    plaetzchen=
        st.none(),
    dateiname=
        safe_text,
    datei=
        st.none(),
    attribute=
        safe_text,
    form=
        st.none(),
    plformList=
        st.none()
)
Groesse_strategy = st.builds(
    Groesse,
    name=
        safe_text,
    breite=
        st.integers(),
    name1=
        st.none(),
    laenge=
        st.integers()
)
PlaetzchenForm_strategy = st.builds(
    PlaetzchenForm,
    faktor=
        safe_text,
    pl_groesse=
        st.none(),
    pl_form=
        st.none()
)
Zutat_strategy = st.builds(
    Zutat,
    name=
        st.none(),
    einheit=
        st.none(),
    menge=
        st.integers()
)

@given(instance=KeyPressEventArgs__strategy)
@settings(max_examples=50)
def test_keypresseventargs__instantiation(instance):
    assert isinstance(instance, KeyPressEventArgs_)

@given(instance=myException_strategy)
@settings(max_examples=50)
def test_myexception_instantiation(instance):
    assert isinstance(instance, myException)

@given(instance=Font_2_strategy)
@settings(max_examples=50)
def test_font_2_instantiation(instance):
    assert isinstance(instance, Font_2)

@given(instance=Font__strategy)
@settings(max_examples=50)
def test_font__instantiation(instance):
    assert isinstance(instance, Font_)

@given(instance=ThreadExceptionEventArgs__strategy)
@settings(max_examples=50)
def test_threadexceptioneventargs__instantiation(instance):
    assert isinstance(instance, ThreadExceptionEventArgs_)

@given(instance=Object__strategy)
@settings(max_examples=50)
def test_object__instantiation(instance):
    assert isinstance(instance, Object_)

@given(instance=App_strategy)
@settings(max_examples=50)
def test_app_instantiation(instance):
    assert isinstance(instance, App)

@given(instance=Groesse__strategy)
@settings(max_examples=50)
def test_groesse__instantiation(instance):
    assert isinstance(instance, Groesse_)

@given(instance=PL_Form__strategy)
@settings(max_examples=50)
def test_pl_form__instantiation(instance):
    assert isinstance(instance, PL_Form_)

@given(instance=PL_Groesse__strategy)
@settings(max_examples=50)
def test_pl_groesse__instantiation(instance):
    assert isinstance(instance, PL_Groesse_)

@given(instance=List_TeigRezept____strategy)
@settings(max_examples=50)
def test_list_teigrezept____instantiation(instance):
    assert isinstance(instance, List_TeigRezept___)

@given(instance=Array_Zutat____strategy)
@settings(max_examples=50)
def test_array_zutat____instantiation(instance):
    assert isinstance(instance, Array_Zutat___)

@given(instance=List_DekorRezept____strategy)
@settings(max_examples=50)
def test_list_dekorrezept____instantiation(instance):
    assert isinstance(instance, List_DekorRezept___)

@given(instance=List_PlaetzchenForm____strategy)
@settings(max_examples=50)
def test_list_plaetzchenform____instantiation(instance):
    assert isinstance(instance, List_PlaetzchenForm___)

@given(instance=List_Zutat____strategy)
@settings(max_examples=50)
def test_list_zutat____instantiation(instance):
    assert isinstance(instance, List_Zutat___)

@given(instance=GussRezept_strategy)
@settings(max_examples=50)
def test_gussrezept_instantiation(instance):
    assert isinstance(instance, GussRezept)



@given(instance=GussRezept_strategy)
def test_gussrezept_basis_setter(instance):
    original = instance.basis
    instance.basis = original
    assert instance.basis == original



@given(instance=GussRezept_strategy)
def test_gussrezept_zutat_setter(instance):
    original = instance.zutat
    instance.zutat = original
    assert instance.zutat == original



@given(instance=GussRezept_strategy)
def test_gussrezept_basismenge_setter(instance):
    original = instance.basismenge
    instance.basismenge = original
    assert instance.basismenge == original

@given(instance=Zutat__strategy)
@settings(max_examples=50)
def test_zutat__instantiation(instance):
    assert isinstance(instance, Zutat_)

@given(instance=Rezept_strategy)
@settings(max_examples=50)
def test_rezept_instantiation(instance):
    assert isinstance(instance, Rezept)



@given(instance=Rezept_strategy)
def test_rezept_rezeptname_setter(instance):
    original = instance.rezeptname
    instance.rezeptname = original
    assert instance.rezeptname == original



@given(instance=Rezept_strategy)
def test_rezept_basismenge_setter(instance):
    original = instance.basismenge
    instance.basismenge = original
    assert instance.basismenge == original



@given(instance=Rezept_strategy)
def test_rezept_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Rezept_strategy)
def test_rezept_basis_setter(instance):
    original = instance.basis
    instance.basis = original
    assert instance.basis == original



@given(instance=Rezept_strategy)
def test_rezept_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=DekorRezept_strategy)
@settings(max_examples=50)
def test_dekorrezept_instantiation(instance):
    assert isinstance(instance, DekorRezept)



@given(instance=DekorRezept_strategy)
def test_dekorrezept_basismenge_setter(instance):
    original = instance.basismenge
    instance.basismenge = original
    assert instance.basismenge == original



@given(instance=DekorRezept_strategy)
def test_dekorrezept_zutaten_setter(instance):
    original = instance.zutaten
    instance.zutaten = original
    assert instance.zutaten == original



@given(instance=DekorRezept_strategy)
def test_dekorrezept_basis_setter(instance):
    original = instance.basis
    instance.basis = original
    assert instance.basis == original



@given(instance=DekorRezept_strategy)
def test_dekorrezept_dekor_setter(instance):
    original = instance.dekor
    instance.dekor = original
    assert instance.dekor == original

@given(instance=GUIRezept_strategy)
@settings(max_examples=50)
def test_guirezept_instantiation(instance):
    assert isinstance(instance, GUIRezept)



@given(instance=GUIRezept_strategy)
def test_guirezept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=String__strategy)
@settings(max_examples=50)
def test_string__instantiation(instance):
    assert isinstance(instance, String_)

@given(instance=PlaetzchenForm__strategy)
@settings(max_examples=50)
def test_plaetzchenform__instantiation(instance):
    assert isinstance(instance, PlaetzchenForm_)

@given(instance=ComboBox_strategy)
@settings(max_examples=50)
def test_combobox_instantiation(instance):
    assert isinstance(instance, ComboBox)

@given(instance=Plaetzchen__strategy)
@settings(max_examples=50)
def test_plaetzchen__instantiation(instance):
    assert isinstance(instance, Plaetzchen_)

@given(instance=Plaetzchen_strategy)
@settings(max_examples=50)
def test_plaetzchen_instantiation(instance):
    assert isinstance(instance, Plaetzchen)



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_deko_setter(instance):
    original = instance.deko
    instance.deko = original
    assert instance.deko == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_rezeptTeig_setter(instance):
    original = instance.rezeptTeig
    instance.rezeptTeig = original
    assert instance.rezeptTeig == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_guss_setter(instance):
    original = instance.guss
    instance.guss = original
    assert instance.guss == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_rezeptDeko_setter(instance):
    original = instance.rezeptDeko
    instance.rezeptDeko = original
    assert instance.rezeptDeko == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_teig_setter(instance):
    original = instance.teig
    instance.teig = original
    assert instance.teig == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_rezeptGuss_setter(instance):
    original = instance.rezeptGuss
    instance.rezeptGuss = original
    assert instance.rezeptGuss == original



@given(instance=Plaetzchen_strategy)
def test_plaetzchen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TeigRezept__strategy)
@settings(max_examples=50)
def test_teigrezept__instantiation(instance):
    assert isinstance(instance, TeigRezept_)

@given(instance=TeigRezept_strategy)
@settings(max_examples=50)
def test_teigrezept_instantiation(instance):
    assert isinstance(instance, TeigRezept)



@given(instance=TeigRezept_strategy)
def test_teigrezept_basismenge_setter(instance):
    original = instance.basismenge
    instance.basismenge = original
    assert instance.basismenge == original



@given(instance=TeigRezept_strategy)
def test_teigrezept_basis_setter(instance):
    original = instance.basis
    instance.basis = original
    assert instance.basis == original



@given(instance=TeigRezept_strategy)
def test_teigrezept_zutaten_setter(instance):
    original = instance.zutaten
    instance.zutaten = original
    assert instance.zutaten == original



@given(instance=TeigRezept_strategy)
def test_teigrezept_backzeit_setter(instance):
    original = instance.backzeit
    instance.backzeit = original
    assert instance.backzeit == original



@given(instance=TeigRezept_strategy)
def test_teigrezept_backtemp_setter(instance):
    original = instance.backtemp
    instance.backtemp = original
    assert instance.backtemp == original

@given(instance=KonfigDatei__strategy)
@settings(max_examples=50)
def test_konfigdatei__instantiation(instance):
    assert isinstance(instance, KonfigDatei_)

@given(instance=KonfigDatei_strategy)
@settings(max_examples=50)
def test_konfigdatei_instantiation(instance):
    assert isinstance(instance, KonfigDatei)



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_menge1_setter(instance):
    original = instance.menge1
    instance.menge1 = original
    assert instance.menge1 == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_backtemp_setter(instance):
    original = instance.backtemp
    instance.backtemp = original
    assert instance.backtemp == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_plaetzchen_setter(instance):
    original = instance.plaetzchen
    instance.plaetzchen = original
    assert instance.plaetzchen == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_backzeit_setter(instance):
    original = instance.backzeit
    instance.backzeit = original
    assert instance.backzeit == original



@given(instance=KonfigDatei_strategy)
def test_konfigdatei_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GUIKeksform_strategy)
@settings(max_examples=50)
def test_guikeksform_instantiation(instance):
    assert isinstance(instance, GUIKeksform)



@given(instance=GUIKeksform_strategy)
def test_guikeksform_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original



@given(instance=GUIKeksform_strategy)
def test_guikeksform_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original



@given(instance=GUIKeksform_strategy)
def test_guikeksform_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=GUIKeksform_strategy)
def test_guikeksform_pl__f_setter(instance):
    original = instance.pl__f
    instance.pl__f = original
    assert instance.pl__f == original

@given(instance=GUI_strategy)
@settings(max_examples=50)
def test_gui_instantiation(instance):
    assert isinstance(instance, GUI)



@given(instance=GUI_strategy)
def test_gui_groesse_setter(instance):
    original = instance.groesse
    instance.groesse = original
    assert instance.groesse == original



@given(instance=GUI_strategy)
def test_gui_guss_setter(instance):
    original = instance.guss
    instance.guss = original
    assert instance.guss == original



@given(instance=GUI_strategy)
def test_gui_plaetzchenname_setter(instance):
    original = instance.plaetzchenname
    instance.plaetzchenname = original
    assert instance.plaetzchenname == original



@given(instance=GUI_strategy)
def test_gui_gussList_setter(instance):
    original = instance.gussList
    instance.gussList = original
    assert instance.gussList == original



@given(instance=GUI_strategy)
def test_gui_stueckzahl_setter(instance):
    original = instance.stueckzahl
    instance.stueckzahl = original
    assert instance.stueckzahl == original



@given(instance=GUI_strategy)
def test_gui_dekorList_setter(instance):
    original = instance.dekorList
    instance.dekorList = original
    assert instance.dekorList == original



@given(instance=GUI_strategy)
def test_gui_zutatenList_setter(instance):
    original = instance.zutatenList
    instance.zutatenList = original
    assert instance.zutatenList == original



@given(instance=GUI_strategy)
def test_gui_deko_setter(instance):
    original = instance.deko
    instance.deko = original
    assert instance.deko == original



@given(instance=GUI_strategy)
def test_gui_teigsorte_setter(instance):
    original = instance.teigsorte
    instance.teigsorte = original
    assert instance.teigsorte == original



@given(instance=GUI_strategy)
def test_gui_teigList_setter(instance):
    original = instance.teigList
    instance.teigList = original
    assert instance.teigList == original



@given(instance=GUI_strategy)
def test_gui_plaetzchen_setter(instance):
    original = instance.plaetzchen
    instance.plaetzchen = original
    assert instance.plaetzchen == original



@given(instance=GUI_strategy)
def test_gui_dateiname_setter(instance):
    original = instance.dateiname
    instance.dateiname = original
    assert instance.dateiname == original



@given(instance=GUI_strategy)
def test_gui_datei_setter(instance):
    original = instance.datei
    instance.datei = original
    assert instance.datei == original



@given(instance=GUI_strategy)
def test_gui_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=GUI_strategy)
def test_gui_form_setter(instance):
    original = instance.form
    instance.form = original
    assert instance.form == original



@given(instance=GUI_strategy)
def test_gui_plformList_setter(instance):
    original = instance.plformList
    instance.plformList = original
    assert instance.plformList == original

@given(instance=Groesse_strategy)
@settings(max_examples=50)
def test_groesse_instantiation(instance):
    assert isinstance(instance, Groesse)



@given(instance=Groesse_strategy)
def test_groesse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Groesse_strategy)
def test_groesse_breite_setter(instance):
    original = instance.breite
    instance.breite = original
    assert instance.breite == original



@given(instance=Groesse_strategy)
def test_groesse_name1_setter(instance):
    original = instance.name1
    instance.name1 = original
    assert instance.name1 == original



@given(instance=Groesse_strategy)
def test_groesse_laenge_setter(instance):
    original = instance.laenge
    instance.laenge = original
    assert instance.laenge == original

@given(instance=PlaetzchenForm_strategy)
@settings(max_examples=50)
def test_plaetzchenform_instantiation(instance):
    assert isinstance(instance, PlaetzchenForm)



@given(instance=PlaetzchenForm_strategy)
def test_plaetzchenform_faktor_setter(instance):
    original = instance.faktor
    instance.faktor = original
    assert instance.faktor == original



@given(instance=PlaetzchenForm_strategy)
def test_plaetzchenform_pl_groesse_setter(instance):
    original = instance.pl_groesse
    instance.pl_groesse = original
    assert instance.pl_groesse == original



@given(instance=PlaetzchenForm_strategy)
def test_plaetzchenform_pl_form_setter(instance):
    original = instance.pl_form
    instance.pl_form = original
    assert instance.pl_form == original

@given(instance=Zutat_strategy)
@settings(max_examples=50)
def test_zutat_instantiation(instance):
    assert isinstance(instance, Zutat)



@given(instance=Zutat_strategy)
def test_zutat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Zutat_strategy)
def test_zutat_einheit_setter(instance):
    original = instance.einheit
    instance.einheit = original
    assert instance.einheit == original



@given(instance=Zutat_strategy)
def test_zutat_menge_setter(instance):
    original = instance.menge
    instance.menge = original
    assert instance.menge == original

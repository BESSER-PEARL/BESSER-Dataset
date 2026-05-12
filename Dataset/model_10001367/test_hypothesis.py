import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Contactformulier,
    Afbeelding,
    Categorie,
    Adres,
    Nieuwsbericht,
    Product,
    Bestelregel,
    Factuur,
    Hoofdbeheerder,
    Beheerder,
    Klant,
    Persoon,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_contactformulier_is_not_abstract():
    assert not inspect.isabstract(Contactformulier)


def test_contactformulier_constructor_exists():
    assert callable(Contactformulier.__init__)


def test_contactformulier_constructor_args():
    sig = inspect.signature(Contactformulier.__init__)
    params = list(sig.parameters.keys())
    assert "tekst" in params, "Missing parameter 'tekst'"

def test_contactformulier_has_tekst():
    assert hasattr(Contactformulier, "tekst")
    descriptor = None
    for klass in Contactformulier.__mro__:
        if "tekst" in klass.__dict__:
            descriptor = klass.__dict__["tekst"]
            break
    assert isinstance(descriptor, property)



def test_afbeelding_is_not_abstract():
    assert not inspect.isabstract(Afbeelding)


def test_afbeelding_constructor_exists():
    assert callable(Afbeelding.__init__)


def test_afbeelding_constructor_args():
    sig = inspect.signature(Afbeelding.__init__)
    params = list(sig.parameters.keys())
    assert "naam" in params, "Missing parameter 'naam'"
    assert "locatie" in params, "Missing parameter 'locatie'"
    assert "datum" in params, "Missing parameter 'datum'"

def test_afbeelding_has_naam():
    assert hasattr(Afbeelding, "naam")
    descriptor = None
    for klass in Afbeelding.__mro__:
        if "naam" in klass.__dict__:
            descriptor = klass.__dict__["naam"]
            break
    assert isinstance(descriptor, property)

def test_afbeelding_has_locatie():
    assert hasattr(Afbeelding, "locatie")
    descriptor = None
    for klass in Afbeelding.__mro__:
        if "locatie" in klass.__dict__:
            descriptor = klass.__dict__["locatie"]
            break
    assert isinstance(descriptor, property)

def test_afbeelding_has_datum():
    assert hasattr(Afbeelding, "datum")
    descriptor = None
    for klass in Afbeelding.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)



def test_categorie_is_not_abstract():
    assert not inspect.isabstract(Categorie)


def test_categorie_constructor_exists():
    assert callable(Categorie.__init__)


def test_categorie_constructor_args():
    sig = inspect.signature(Categorie.__init__)
    params = list(sig.parameters.keys())



def test_adres_is_not_abstract():
    assert not inspect.isabstract(Adres)


def test_adres_constructor_exists():
    assert callable(Adres.__init__)


def test_adres_constructor_args():
    sig = inspect.signature(Adres.__init__)
    params = list(sig.parameters.keys())
    assert "postcode" in params, "Missing parameter 'postcode'"
    assert "straatnaam" in params, "Missing parameter 'straatnaam'"
    assert "huisnummer" in params, "Missing parameter 'huisnummer'"
    assert "bijvoegsel" in params, "Missing parameter 'bijvoegsel'"
    assert "stad" in params, "Missing parameter 'stad'"

def test_adres_has_postcode():
    assert hasattr(Adres, "postcode")
    descriptor = None
    for klass in Adres.__mro__:
        if "postcode" in klass.__dict__:
            descriptor = klass.__dict__["postcode"]
            break
    assert isinstance(descriptor, property)

def test_adres_has_straatnaam():
    assert hasattr(Adres, "straatnaam")
    descriptor = None
    for klass in Adres.__mro__:
        if "straatnaam" in klass.__dict__:
            descriptor = klass.__dict__["straatnaam"]
            break
    assert isinstance(descriptor, property)

def test_adres_has_huisnummer():
    assert hasattr(Adres, "huisnummer")
    descriptor = None
    for klass in Adres.__mro__:
        if "huisnummer" in klass.__dict__:
            descriptor = klass.__dict__["huisnummer"]
            break
    assert isinstance(descriptor, property)

def test_adres_has_bijvoegsel():
    assert hasattr(Adres, "bijvoegsel")
    descriptor = None
    for klass in Adres.__mro__:
        if "bijvoegsel" in klass.__dict__:
            descriptor = klass.__dict__["bijvoegsel"]
            break
    assert isinstance(descriptor, property)

def test_adres_has_stad():
    assert hasattr(Adres, "stad")
    descriptor = None
    for klass in Adres.__mro__:
        if "stad" in klass.__dict__:
            descriptor = klass.__dict__["stad"]
            break
    assert isinstance(descriptor, property)



def test_nieuwsbericht_is_not_abstract():
    assert not inspect.isabstract(Nieuwsbericht)


def test_nieuwsbericht_constructor_exists():
    assert callable(Nieuwsbericht.__init__)


def test_nieuwsbericht_constructor_args():
    sig = inspect.signature(Nieuwsbericht.__init__)
    params = list(sig.parameters.keys())
    assert "tekst" in params, "Missing parameter 'tekst'"
    assert "titel" in params, "Missing parameter 'titel'"

def test_nieuwsbericht_has_tekst():
    assert hasattr(Nieuwsbericht, "tekst")
    descriptor = None
    for klass in Nieuwsbericht.__mro__:
        if "tekst" in klass.__dict__:
            descriptor = klass.__dict__["tekst"]
            break
    assert isinstance(descriptor, property)

def test_nieuwsbericht_has_titel():
    assert hasattr(Nieuwsbericht, "titel")
    descriptor = None
    for klass in Nieuwsbericht.__mro__:
        if "titel" in klass.__dict__:
            descriptor = klass.__dict__["titel"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "prijs" in params, "Missing parameter 'prijs'"
    assert "naam" in params, "Missing parameter 'naam'"
    assert "voorraad" in params, "Missing parameter 'voorraad'"
    assert "actief" in params, "Missing parameter 'actief'"
    assert "beschrijving" in params, "Missing parameter 'beschrijving'"

def test_product_has_prijs():
    assert hasattr(Product, "prijs")
    descriptor = None
    for klass in Product.__mro__:
        if "prijs" in klass.__dict__:
            descriptor = klass.__dict__["prijs"]
            break
    assert isinstance(descriptor, property)

def test_product_has_naam():
    assert hasattr(Product, "naam")
    descriptor = None
    for klass in Product.__mro__:
        if "naam" in klass.__dict__:
            descriptor = klass.__dict__["naam"]
            break
    assert isinstance(descriptor, property)

def test_product_has_voorraad():
    assert hasattr(Product, "voorraad")
    descriptor = None
    for klass in Product.__mro__:
        if "voorraad" in klass.__dict__:
            descriptor = klass.__dict__["voorraad"]
            break
    assert isinstance(descriptor, property)

def test_product_has_actief():
    assert hasattr(Product, "actief")
    descriptor = None
    for klass in Product.__mro__:
        if "actief" in klass.__dict__:
            descriptor = klass.__dict__["actief"]
            break
    assert isinstance(descriptor, property)

def test_product_has_beschrijving():
    assert hasattr(Product, "beschrijving")
    descriptor = None
    for klass in Product.__mro__:
        if "beschrijving" in klass.__dict__:
            descriptor = klass.__dict__["beschrijving"]
            break
    assert isinstance(descriptor, property)



def test_bestelregel_is_not_abstract():
    assert not inspect.isabstract(Bestelregel)


def test_bestelregel_constructor_exists():
    assert callable(Bestelregel.__init__)


def test_bestelregel_constructor_args():
    sig = inspect.signature(Bestelregel.__init__)
    params = list(sig.parameters.keys())
    assert "aantal" in params, "Missing parameter 'aantal'"

def test_bestelregel_has_aantal():
    assert hasattr(Bestelregel, "aantal")
    descriptor = None
    for klass in Bestelregel.__mro__:
        if "aantal" in klass.__dict__:
            descriptor = klass.__dict__["aantal"]
            break
    assert isinstance(descriptor, property)



def test_factuur_is_not_abstract():
    assert not inspect.isabstract(Factuur)


def test_factuur_constructor_exists():
    assert callable(Factuur.__init__)


def test_factuur_constructor_args():
    sig = inspect.signature(Factuur.__init__)
    params = list(sig.parameters.keys())
    assert "btw" in params, "Missing parameter 'btw'"
    assert "status" in params, "Missing parameter 'status'"
    assert "datum" in params, "Missing parameter 'datum'"

def test_factuur_has_btw():
    assert hasattr(Factuur, "btw")
    descriptor = None
    for klass in Factuur.__mro__:
        if "btw" in klass.__dict__:
            descriptor = klass.__dict__["btw"]
            break
    assert isinstance(descriptor, property)

def test_factuur_has_status():
    assert hasattr(Factuur, "status")
    descriptor = None
    for klass in Factuur.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_factuur_has_datum():
    assert hasattr(Factuur, "datum")
    descriptor = None
    for klass in Factuur.__mro__:
        if "datum" in klass.__dict__:
            descriptor = klass.__dict__["datum"]
            break
    assert isinstance(descriptor, property)



def test_hoofdbeheerder_is_not_abstract():
    assert not inspect.isabstract(Hoofdbeheerder)


def test_hoofdbeheerder_constructor_exists():
    assert callable(Hoofdbeheerder.__init__)


def test_hoofdbeheerder_constructor_args():
    sig = inspect.signature(Hoofdbeheerder.__init__)
    params = list(sig.parameters.keys())



def test_beheerder_is_not_abstract():
    assert not inspect.isabstract(Beheerder)


def test_beheerder_constructor_exists():
    assert callable(Beheerder.__init__)


def test_beheerder_constructor_args():
    sig = inspect.signature(Beheerder.__init__)
    params = list(sig.parameters.keys())
    assert "rechten" in params, "Missing parameter 'rechten'"

def test_beheerder_has_rechten():
    assert hasattr(Beheerder, "rechten")
    descriptor = None
    for klass in Beheerder.__mro__:
        if "rechten" in klass.__dict__:
            descriptor = klass.__dict__["rechten"]
            break
    assert isinstance(descriptor, property)



def test_klant_is_not_abstract():
    assert not inspect.isabstract(Klant)


def test_klant_constructor_exists():
    assert callable(Klant.__init__)


def test_klant_constructor_args():
    sig = inspect.signature(Klant.__init__)
    params = list(sig.parameters.keys())
    assert "telefoonnummer" in params, "Missing parameter 'telefoonnummer'"
    assert "geboortedatum" in params, "Missing parameter 'geboortedatum'"

def test_klant_has_telefoonnummer():
    assert hasattr(Klant, "telefoonnummer")
    descriptor = None
    for klass in Klant.__mro__:
        if "telefoonnummer" in klass.__dict__:
            descriptor = klass.__dict__["telefoonnummer"]
            break
    assert isinstance(descriptor, property)

def test_klant_has_geboortedatum():
    assert hasattr(Klant, "geboortedatum")
    descriptor = None
    for klass in Klant.__mro__:
        if "geboortedatum" in klass.__dict__:
            descriptor = klass.__dict__["geboortedatum"]
            break
    assert isinstance(descriptor, property)



def test_persoon_is_not_abstract():
    assert not inspect.isabstract(Persoon)


def test_persoon_constructor_exists():
    assert callable(Persoon.__init__)


def test_persoon_constructor_args():
    sig = inspect.signature(Persoon.__init__)
    params = list(sig.parameters.keys())
    assert "tussenvoegsel" in params, "Missing parameter 'tussenvoegsel'"
    assert "voornaam" in params, "Missing parameter 'voornaam'"
    assert "achternaam" in params, "Missing parameter 'achternaam'"
    assert "wachtwoord" in params, "Missing parameter 'wachtwoord'"
    assert "e_mail" in params, "Missing parameter 'e_mail'"

def test_persoon_has_tussenvoegsel():
    assert hasattr(Persoon, "tussenvoegsel")
    descriptor = None
    for klass in Persoon.__mro__:
        if "tussenvoegsel" in klass.__dict__:
            descriptor = klass.__dict__["tussenvoegsel"]
            break
    assert isinstance(descriptor, property)

def test_persoon_has_voornaam():
    assert hasattr(Persoon, "voornaam")
    descriptor = None
    for klass in Persoon.__mro__:
        if "voornaam" in klass.__dict__:
            descriptor = klass.__dict__["voornaam"]
            break
    assert isinstance(descriptor, property)

def test_persoon_has_achternaam():
    assert hasattr(Persoon, "achternaam")
    descriptor = None
    for klass in Persoon.__mro__:
        if "achternaam" in klass.__dict__:
            descriptor = klass.__dict__["achternaam"]
            break
    assert isinstance(descriptor, property)

def test_persoon_has_wachtwoord():
    assert hasattr(Persoon, "wachtwoord")
    descriptor = None
    for klass in Persoon.__mro__:
        if "wachtwoord" in klass.__dict__:
            descriptor = klass.__dict__["wachtwoord"]
            break
    assert isinstance(descriptor, property)

def test_persoon_has_e_mail():
    assert hasattr(Persoon, "e_mail")
    descriptor = None
    for klass in Persoon.__mro__:
        if "e_mail" in klass.__dict__:
            descriptor = klass.__dict__["e_mail"]
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
Contactformulier_strategy = st.builds(
    Contactformulier,
    tekst=
        safe_text
)
Afbeelding_strategy = st.builds(
    Afbeelding,
    naam=
        safe_text,
    locatie=
        safe_text,
    datum=
        safe_text
)
Categorie_strategy = st.builds(
    Categorie,
)
Adres_strategy = st.builds(
    Adres,
    postcode=
        safe_text,
    straatnaam=
        safe_text,
    huisnummer=
        st.integers(),
    bijvoegsel=
        safe_text,
    stad=
        safe_text
)
Nieuwsbericht_strategy = st.builds(
    Nieuwsbericht,
    tekst=
        safe_text,
    titel=
        safe_text
)
Product_strategy = st.builds(
    Product,
    prijs=
        st.integers(),
    naam=
        safe_text,
    voorraad=
        st.integers(),
    actief=
        st.booleans(),
    beschrijving=
        safe_text
)
Bestelregel_strategy = st.builds(
    Bestelregel,
    aantal=
        st.integers()
)
Factuur_strategy = st.builds(
    Factuur,
    btw=
        st.integers(),
    status=
        safe_text,
    datum=
        safe_text
)
Hoofdbeheerder_strategy = st.builds(
    Hoofdbeheerder,
)
Beheerder_strategy = st.builds(
    Beheerder,
    rechten=
        st.booleans()
)
Klant_strategy = st.builds(
    Klant,
    telefoonnummer=
        safe_text,
    geboortedatum=
        safe_text
)
Persoon_strategy = st.builds(
    Persoon,
    tussenvoegsel=
        safe_text,
    voornaam=
        safe_text,
    achternaam=
        safe_text,
    wachtwoord=
        safe_text,
    e_mail=
        safe_text
)

@given(instance=Contactformulier_strategy)
@settings(max_examples=50)
def test_contactformulier_instantiation(instance):
    assert isinstance(instance, Contactformulier)

@given(instance=Contactformulier_strategy)
def test_contactformulier_tekst_type(instance):
    assert isinstance(instance.tekst, str)


@given(instance=Contactformulier_strategy)
def test_contactformulier_tekst_setter(instance):
    original = instance.tekst
    instance.tekst = original
    assert instance.tekst == original

@given(instance=Afbeelding_strategy)
@settings(max_examples=50)
def test_afbeelding_instantiation(instance):
    assert isinstance(instance, Afbeelding)

@given(instance=Afbeelding_strategy)
def test_afbeelding_naam_type(instance):
    assert isinstance(instance.naam, str)


@given(instance=Afbeelding_strategy)
def test_afbeelding_naam_setter(instance):
    original = instance.naam
    instance.naam = original
    assert instance.naam == original

@given(instance=Afbeelding_strategy)
def test_afbeelding_locatie_type(instance):
    assert isinstance(instance.locatie, str)


@given(instance=Afbeelding_strategy)
def test_afbeelding_locatie_setter(instance):
    original = instance.locatie
    instance.locatie = original
    assert instance.locatie == original

@given(instance=Afbeelding_strategy)
def test_afbeelding_datum_type(instance):
    assert isinstance(instance.datum, str)


@given(instance=Afbeelding_strategy)
def test_afbeelding_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original

@given(instance=Categorie_strategy)
@settings(max_examples=50)
def test_categorie_instantiation(instance):
    assert isinstance(instance, Categorie)

@given(instance=Adres_strategy)
@settings(max_examples=50)
def test_adres_instantiation(instance):
    assert isinstance(instance, Adres)

@given(instance=Adres_strategy)
def test_adres_postcode_type(instance):
    assert isinstance(instance.postcode, str)


@given(instance=Adres_strategy)
def test_adres_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original

@given(instance=Adres_strategy)
def test_adres_straatnaam_type(instance):
    assert isinstance(instance.straatnaam, str)


@given(instance=Adres_strategy)
def test_adres_straatnaam_setter(instance):
    original = instance.straatnaam
    instance.straatnaam = original
    assert instance.straatnaam == original

@given(instance=Adres_strategy)
def test_adres_huisnummer_type(instance):
    assert isinstance(instance.huisnummer, int)


@given(instance=Adres_strategy)
def test_adres_huisnummer_setter(instance):
    original = instance.huisnummer
    instance.huisnummer = original
    assert instance.huisnummer == original

@given(instance=Adres_strategy)
def test_adres_bijvoegsel_type(instance):
    assert isinstance(instance.bijvoegsel, str)


@given(instance=Adres_strategy)
def test_adres_bijvoegsel_setter(instance):
    original = instance.bijvoegsel
    instance.bijvoegsel = original
    assert instance.bijvoegsel == original

@given(instance=Adres_strategy)
def test_adres_stad_type(instance):
    assert isinstance(instance.stad, str)


@given(instance=Adres_strategy)
def test_adres_stad_setter(instance):
    original = instance.stad
    instance.stad = original
    assert instance.stad == original

@given(instance=Nieuwsbericht_strategy)
@settings(max_examples=50)
def test_nieuwsbericht_instantiation(instance):
    assert isinstance(instance, Nieuwsbericht)

@given(instance=Nieuwsbericht_strategy)
def test_nieuwsbericht_tekst_type(instance):
    assert isinstance(instance.tekst, str)


@given(instance=Nieuwsbericht_strategy)
def test_nieuwsbericht_tekst_setter(instance):
    original = instance.tekst
    instance.tekst = original
    assert instance.tekst == original

@given(instance=Nieuwsbericht_strategy)
def test_nieuwsbericht_titel_type(instance):
    assert isinstance(instance.titel, str)


@given(instance=Nieuwsbericht_strategy)
def test_nieuwsbericht_titel_setter(instance):
    original = instance.titel
    instance.titel = original
    assert instance.titel == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)

@given(instance=Product_strategy)
def test_product_prijs_type(instance):
    assert isinstance(instance.prijs, int)


@given(instance=Product_strategy)
def test_product_prijs_setter(instance):
    original = instance.prijs
    instance.prijs = original
    assert instance.prijs == original

@given(instance=Product_strategy)
def test_product_naam_type(instance):
    assert isinstance(instance.naam, str)


@given(instance=Product_strategy)
def test_product_naam_setter(instance):
    original = instance.naam
    instance.naam = original
    assert instance.naam == original

@given(instance=Product_strategy)
def test_product_voorraad_type(instance):
    assert isinstance(instance.voorraad, int)


@given(instance=Product_strategy)
def test_product_voorraad_setter(instance):
    original = instance.voorraad
    instance.voorraad = original
    assert instance.voorraad == original

@given(instance=Product_strategy)
def test_product_actief_type(instance):
    assert isinstance(instance.actief, bool)


@given(instance=Product_strategy)
def test_product_actief_setter(instance):
    original = instance.actief
    instance.actief = original
    assert instance.actief == original

@given(instance=Product_strategy)
def test_product_beschrijving_type(instance):
    assert isinstance(instance.beschrijving, str)


@given(instance=Product_strategy)
def test_product_beschrijving_setter(instance):
    original = instance.beschrijving
    instance.beschrijving = original
    assert instance.beschrijving == original

@given(instance=Bestelregel_strategy)
@settings(max_examples=50)
def test_bestelregel_instantiation(instance):
    assert isinstance(instance, Bestelregel)

@given(instance=Bestelregel_strategy)
def test_bestelregel_aantal_type(instance):
    assert isinstance(instance.aantal, int)


@given(instance=Bestelregel_strategy)
def test_bestelregel_aantal_setter(instance):
    original = instance.aantal
    instance.aantal = original
    assert instance.aantal == original

@given(instance=Factuur_strategy)
@settings(max_examples=50)
def test_factuur_instantiation(instance):
    assert isinstance(instance, Factuur)

@given(instance=Factuur_strategy)
def test_factuur_btw_type(instance):
    assert isinstance(instance.btw, int)


@given(instance=Factuur_strategy)
def test_factuur_btw_setter(instance):
    original = instance.btw
    instance.btw = original
    assert instance.btw == original

@given(instance=Factuur_strategy)
def test_factuur_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=Factuur_strategy)
def test_factuur_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Factuur_strategy)
def test_factuur_datum_type(instance):
    assert isinstance(instance.datum, str)


@given(instance=Factuur_strategy)
def test_factuur_datum_setter(instance):
    original = instance.datum
    instance.datum = original
    assert instance.datum == original

@given(instance=Hoofdbeheerder_strategy)
@settings(max_examples=50)
def test_hoofdbeheerder_instantiation(instance):
    assert isinstance(instance, Hoofdbeheerder)

@given(instance=Beheerder_strategy)
@settings(max_examples=50)
def test_beheerder_instantiation(instance):
    assert isinstance(instance, Beheerder)

@given(instance=Beheerder_strategy)
def test_beheerder_rechten_type(instance):
    assert isinstance(instance.rechten, bool)


@given(instance=Beheerder_strategy)
def test_beheerder_rechten_setter(instance):
    original = instance.rechten
    instance.rechten = original
    assert instance.rechten == original

@given(instance=Klant_strategy)
@settings(max_examples=50)
def test_klant_instantiation(instance):
    assert isinstance(instance, Klant)

@given(instance=Klant_strategy)
def test_klant_telefoonnummer_type(instance):
    assert isinstance(instance.telefoonnummer, str)


@given(instance=Klant_strategy)
def test_klant_telefoonnummer_setter(instance):
    original = instance.telefoonnummer
    instance.telefoonnummer = original
    assert instance.telefoonnummer == original

@given(instance=Klant_strategy)
def test_klant_geboortedatum_type(instance):
    assert isinstance(instance.geboortedatum, str)


@given(instance=Klant_strategy)
def test_klant_geboortedatum_setter(instance):
    original = instance.geboortedatum
    instance.geboortedatum = original
    assert instance.geboortedatum == original

@given(instance=Persoon_strategy)
@settings(max_examples=50)
def test_persoon_instantiation(instance):
    assert isinstance(instance, Persoon)

@given(instance=Persoon_strategy)
def test_persoon_tussenvoegsel_type(instance):
    assert isinstance(instance.tussenvoegsel, str)


@given(instance=Persoon_strategy)
def test_persoon_tussenvoegsel_setter(instance):
    original = instance.tussenvoegsel
    instance.tussenvoegsel = original
    assert instance.tussenvoegsel == original

@given(instance=Persoon_strategy)
def test_persoon_voornaam_type(instance):
    assert isinstance(instance.voornaam, str)


@given(instance=Persoon_strategy)
def test_persoon_voornaam_setter(instance):
    original = instance.voornaam
    instance.voornaam = original
    assert instance.voornaam == original

@given(instance=Persoon_strategy)
def test_persoon_achternaam_type(instance):
    assert isinstance(instance.achternaam, str)


@given(instance=Persoon_strategy)
def test_persoon_achternaam_setter(instance):
    original = instance.achternaam
    instance.achternaam = original
    assert instance.achternaam == original

@given(instance=Persoon_strategy)
def test_persoon_wachtwoord_type(instance):
    assert isinstance(instance.wachtwoord, str)


@given(instance=Persoon_strategy)
def test_persoon_wachtwoord_setter(instance):
    original = instance.wachtwoord
    instance.wachtwoord = original
    assert instance.wachtwoord == original

@given(instance=Persoon_strategy)
def test_persoon_e_mail_type(instance):
    assert isinstance(instance.e_mail, str)


@given(instance=Persoon_strategy)
def test_persoon_e_mail_setter(instance):
    original = instance.e_mail
    instance.e_mail = original
    assert instance.e_mail == original

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Covoiturage_Message,
    Covoiturage_Conducteur,
    Covoiturage_Reservation,
    Covoiturage_Avis,
    Covoiturage_Ville,
    Covoiturage_Trajet,
    Covoiturage_Authentification,
    Covoiturage_Voiture,
    Covoiturage_Passager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_covoiturage_message_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Message)


def test_covoiturage_message_constructor_exists():
    assert callable(Covoiturage_Message.__init__)


def test_covoiturage_message_constructor_args():
    sig = inspect.signature(Covoiturage_Message.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"
    assert "Id" in params, "Missing parameter 'Id'"

def test_covoiturage_message_has_Value():
    assert hasattr(Covoiturage_Message, "Value")
    descriptor = None
    for klass in Covoiturage_Message.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_message_has_Id():
    assert hasattr(Covoiturage_Message, "Id")
    descriptor = None
    for klass in Covoiturage_Message.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_conducteur_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Conducteur)


def test_covoiturage_conducteur_constructor_exists():
    assert callable(Covoiturage_Conducteur.__init__)


def test_covoiturage_conducteur_constructor_args():
    sig = inspect.signature(Covoiturage_Conducteur.__init__)
    params = list(sig.parameters.keys())
    assert "datePermi" in params, "Missing parameter 'datePermi'"

def test_covoiturage_conducteur_has_datePermi():
    assert hasattr(Covoiturage_Conducteur, "datePermi")
    descriptor = None
    for klass in Covoiturage_Conducteur.__mro__:
        if "datePermi" in klass.__dict__:
            descriptor = klass.__dict__["datePermi"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_reservation_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Reservation)


def test_covoiturage_reservation_constructor_exists():
    assert callable(Covoiturage_Reservation.__init__)


def test_covoiturage_reservation_constructor_args():
    sig = inspect.signature(Covoiturage_Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "id2" in params, "Missing parameter 'id2'"
    assert "dateReservation" in params, "Missing parameter 'dateReservation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "etat" in params, "Missing parameter 'etat'"

def test_covoiturage_reservation_has_id2():
    assert hasattr(Covoiturage_Reservation, "id2")
    descriptor = None
    for klass in Covoiturage_Reservation.__mro__:
        if "id2" in klass.__dict__:
            descriptor = klass.__dict__["id2"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservation_has_dateReservation():
    assert hasattr(Covoiturage_Reservation, "dateReservation")
    descriptor = None
    for klass in Covoiturage_Reservation.__mro__:
        if "dateReservation" in klass.__dict__:
            descriptor = klass.__dict__["dateReservation"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservation_has_id():
    assert hasattr(Covoiturage_Reservation, "id")
    descriptor = None
    for klass in Covoiturage_Reservation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_reservation_has_etat():
    assert hasattr(Covoiturage_Reservation, "etat")
    descriptor = None
    for klass in Covoiturage_Reservation.__mro__:
        if "etat" in klass.__dict__:
            descriptor = klass.__dict__["etat"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_avis_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Avis)


def test_covoiturage_avis_constructor_exists():
    assert callable(Covoiturage_Avis.__init__)


def test_covoiturage_avis_constructor_args():
    sig = inspect.signature(Covoiturage_Avis.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "note" in params, "Missing parameter 'note'"
    assert "commentaire" in params, "Missing parameter 'commentaire'"

def test_covoiturage_avis_has_id():
    assert hasattr(Covoiturage_Avis, "id")
    descriptor = None
    for klass in Covoiturage_Avis.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_avis_has_note():
    assert hasattr(Covoiturage_Avis, "note")
    descriptor = None
    for klass in Covoiturage_Avis.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_avis_has_commentaire():
    assert hasattr(Covoiturage_Avis, "commentaire")
    descriptor = None
    for klass in Covoiturage_Avis.__mro__:
        if "commentaire" in klass.__dict__:
            descriptor = klass.__dict__["commentaire"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_ville_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Ville)


def test_covoiturage_ville_constructor_exists():
    assert callable(Covoiturage_Ville.__init__)


def test_covoiturage_ville_constructor_args():
    sig = inspect.signature(Covoiturage_Ville.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"

def test_covoiturage_ville_has_cp():
    assert hasattr(Covoiturage_Ville, "cp")
    descriptor = None
    for klass in Covoiturage_Ville.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_ville_has_id():
    assert hasattr(Covoiturage_Ville, "id")
    descriptor = None
    for klass in Covoiturage_Ville.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_ville_has_nom():
    assert hasattr(Covoiturage_Ville, "nom")
    descriptor = None
    for klass in Covoiturage_Ville.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_trajet_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Trajet)


def test_covoiturage_trajet_constructor_exists():
    assert callable(Covoiturage_Trajet.__init__)


def test_covoiturage_trajet_constructor_args():
    sig = inspect.signature(Covoiturage_Trajet.__init__)
    params = list(sig.parameters.keys())
    assert "etat" in params, "Missing parameter 'etat'"
    assert "depart" in params, "Missing parameter 'depart'"
    assert "date" in params, "Missing parameter 'date'"
    assert "prix" in params, "Missing parameter 'prix'"
    assert "id" in params, "Missing parameter 'id'"
    assert "destination" in params, "Missing parameter 'destination'"

def test_covoiturage_trajet_has_etat():
    assert hasattr(Covoiturage_Trajet, "etat")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "etat" in klass.__dict__:
            descriptor = klass.__dict__["etat"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_trajet_has_depart():
    assert hasattr(Covoiturage_Trajet, "depart")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "depart" in klass.__dict__:
            descriptor = klass.__dict__["depart"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_trajet_has_date():
    assert hasattr(Covoiturage_Trajet, "date")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_trajet_has_prix():
    assert hasattr(Covoiturage_Trajet, "prix")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_trajet_has_id():
    assert hasattr(Covoiturage_Trajet, "id")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_trajet_has_destination():
    assert hasattr(Covoiturage_Trajet, "destination")
    descriptor = None
    for klass in Covoiturage_Trajet.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_authentification_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Authentification)


def test_covoiturage_authentification_constructor_exists():
    assert callable(Covoiturage_Authentification.__init__)


def test_covoiturage_authentification_constructor_args():
    sig = inspect.signature(Covoiturage_Authentification.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"

def test_covoiturage_authentification_has_password():
    assert hasattr(Covoiturage_Authentification, "password")
    descriptor = None
    for klass in Covoiturage_Authentification.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_authentification_has_id():
    assert hasattr(Covoiturage_Authentification, "id")
    descriptor = None
    for klass in Covoiturage_Authentification.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_voiture_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Voiture)


def test_covoiturage_voiture_constructor_exists():
    assert callable(Covoiturage_Voiture.__init__)


def test_covoiturage_voiture_constructor_args():
    sig = inspect.signature(Covoiturage_Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"
    assert "categorie" in params, "Missing parameter 'categorie'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "confort" in params, "Missing parameter 'confort'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "model" in params, "Missing parameter 'model'"

def test_covoiturage_voiture_has_id():
    assert hasattr(Covoiturage_Voiture, "id")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_nbPlaces():
    assert hasattr(Covoiturage_Voiture, "nbPlaces")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "nbPlaces" in klass.__dict__:
            descriptor = klass.__dict__["nbPlaces"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_categorie():
    assert hasattr(Covoiturage_Voiture, "categorie")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "categorie" in klass.__dict__:
            descriptor = klass.__dict__["categorie"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_attribute():
    assert hasattr(Covoiturage_Voiture, "attribute")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_confort():
    assert hasattr(Covoiturage_Voiture, "confort")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "confort" in klass.__dict__:
            descriptor = klass.__dict__["confort"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_marque():
    assert hasattr(Covoiturage_Voiture, "marque")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "marque" in klass.__dict__:
            descriptor = klass.__dict__["marque"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_voiture_has_model():
    assert hasattr(Covoiturage_Voiture, "model")
    descriptor = None
    for klass in Covoiturage_Voiture.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_covoiturage_passager_is_not_abstract():
    assert not inspect.isabstract(Covoiturage_Passager)


def test_covoiturage_passager_constructor_exists():
    assert callable(Covoiturage_Passager.__init__)


def test_covoiturage_passager_constructor_args():
    sig = inspect.signature(Covoiturage_Passager.__init__)
    params = list(sig.parameters.keys())
    assert "tel" in params, "Missing parameter 'tel'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "mail" in params, "Missing parameter 'mail'"

def test_covoiturage_passager_has_tel():
    assert hasattr(Covoiturage_Passager, "tel")
    descriptor = None
    for klass in Covoiturage_Passager.__mro__:
        if "tel" in klass.__dict__:
            descriptor = klass.__dict__["tel"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_passager_has_nom():
    assert hasattr(Covoiturage_Passager, "nom")
    descriptor = None
    for klass in Covoiturage_Passager.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_passager_has_id():
    assert hasattr(Covoiturage_Passager, "id")
    descriptor = None
    for klass in Covoiturage_Passager.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_passager_has_prenom():
    assert hasattr(Covoiturage_Passager, "prenom")
    descriptor = None
    for klass in Covoiturage_Passager.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_covoiturage_passager_has_mail():
    assert hasattr(Covoiturage_Passager, "mail")
    descriptor = None
    for klass in Covoiturage_Passager.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
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
Covoiturage_Message_strategy = st.builds(
    Covoiturage_Message,
    Value=
        safe_text,
    Id=
        safe_text
)
Covoiturage_Conducteur_strategy = st.builds(
    Covoiturage_Conducteur,
    datePermi=
        safe_text
)
Covoiturage_Reservation_strategy = st.builds(
    Covoiturage_Reservation,
    id2=
        st.integers(),
    dateReservation=
        st.dates(),
    id=
        st.integers(),
    etat=
        st.booleans()
)
Covoiturage_Avis_strategy = st.builds(
    Covoiturage_Avis,
    id=
        st.integers(),
    note=
        st.integers(),
    commentaire=
        safe_text
)
Covoiturage_Ville_strategy = st.builds(
    Covoiturage_Ville,
    cp=
        st.integers(),
    id=
        st.integers(),
    nom=
        safe_text
)
Covoiturage_Trajet_strategy = st.builds(
    Covoiturage_Trajet,
    etat=
        st.booleans(),
    depart=
        st.none(),
    date=
        st.dates(),
    prix=
        st.integers(),
    id=
        st.integers(),
    destination=
        st.none()
)
Covoiturage_Authentification_strategy = st.builds(
    Covoiturage_Authentification,
    password=
        safe_text,
    id=
        safe_text
)
Covoiturage_Voiture_strategy = st.builds(
    Covoiturage_Voiture,
    id=
        st.integers(),
    nbPlaces=
        st.integers(),
    categorie=
        safe_text,
    attribute=
        safe_text,
    confort=
        safe_text,
    marque=
        safe_text,
    model=
        safe_text
)
Covoiturage_Passager_strategy = st.builds(
    Covoiturage_Passager,
    tel=
        st.integers(),
    nom=
        safe_text,
    id=
        st.integers(),
    prenom=
        safe_text,
    mail=
        safe_text
)

@given(instance=Covoiturage_Message_strategy)
@settings(max_examples=50)
def test_covoiturage_message_instantiation(instance):
    assert isinstance(instance, Covoiturage_Message)



@given(instance=Covoiturage_Message_strategy)
def test_covoiturage_message_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original



@given(instance=Covoiturage_Message_strategy)
def test_covoiturage_message_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=Covoiturage_Conducteur_strategy)
@settings(max_examples=50)
def test_covoiturage_conducteur_instantiation(instance):
    assert isinstance(instance, Covoiturage_Conducteur)



@given(instance=Covoiturage_Conducteur_strategy)
def test_covoiturage_conducteur_datePermi_setter(instance):
    original = instance.datePermi
    instance.datePermi = original
    assert instance.datePermi == original

@given(instance=Covoiturage_Reservation_strategy)
@settings(max_examples=50)
def test_covoiturage_reservation_instantiation(instance):
    assert isinstance(instance, Covoiturage_Reservation)



@given(instance=Covoiturage_Reservation_strategy)
def test_covoiturage_reservation_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original



@given(instance=Covoiturage_Reservation_strategy)
def test_covoiturage_reservation_dateReservation_setter(instance):
    original = instance.dateReservation
    instance.dateReservation = original
    assert instance.dateReservation == original



@given(instance=Covoiturage_Reservation_strategy)
def test_covoiturage_reservation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Reservation_strategy)
def test_covoiturage_reservation_etat_setter(instance):
    original = instance.etat
    instance.etat = original
    assert instance.etat == original

@given(instance=Covoiturage_Avis_strategy)
@settings(max_examples=50)
def test_covoiturage_avis_instantiation(instance):
    assert isinstance(instance, Covoiturage_Avis)



@given(instance=Covoiturage_Avis_strategy)
def test_covoiturage_avis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Avis_strategy)
def test_covoiturage_avis_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original



@given(instance=Covoiturage_Avis_strategy)
def test_covoiturage_avis_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original

@given(instance=Covoiturage_Ville_strategy)
@settings(max_examples=50)
def test_covoiturage_ville_instantiation(instance):
    assert isinstance(instance, Covoiturage_Ville)



@given(instance=Covoiturage_Ville_strategy)
def test_covoiturage_ville_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=Covoiturage_Ville_strategy)
def test_covoiturage_ville_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Ville_strategy)
def test_covoiturage_ville_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=Covoiturage_Trajet_strategy)
@settings(max_examples=50)
def test_covoiturage_trajet_instantiation(instance):
    assert isinstance(instance, Covoiturage_Trajet)



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_etat_setter(instance):
    original = instance.etat
    instance.etat = original
    assert instance.etat == original



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_depart_setter(instance):
    original = instance.depart
    instance.depart = original
    assert instance.depart == original



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Trajet_strategy)
def test_covoiturage_trajet_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original

@given(instance=Covoiturage_Authentification_strategy)
@settings(max_examples=50)
def test_covoiturage_authentification_instantiation(instance):
    assert isinstance(instance, Covoiturage_Authentification)



@given(instance=Covoiturage_Authentification_strategy)
def test_covoiturage_authentification_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Covoiturage_Authentification_strategy)
def test_covoiturage_authentification_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Covoiturage_Voiture_strategy)
@settings(max_examples=50)
def test_covoiturage_voiture_instantiation(instance):
    assert isinstance(instance, Covoiturage_Voiture)



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_categorie_setter(instance):
    original = instance.categorie
    instance.categorie = original
    assert instance.categorie == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_confort_setter(instance):
    original = instance.confort
    instance.confort = original
    assert instance.confort == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=Covoiturage_Voiture_strategy)
def test_covoiturage_voiture_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=Covoiturage_Passager_strategy)
@settings(max_examples=50)
def test_covoiturage_passager_instantiation(instance):
    assert isinstance(instance, Covoiturage_Passager)



@given(instance=Covoiturage_Passager_strategy)
def test_covoiturage_passager_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original



@given(instance=Covoiturage_Passager_strategy)
def test_covoiturage_passager_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Covoiturage_Passager_strategy)
def test_covoiturage_passager_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Covoiturage_Passager_strategy)
def test_covoiturage_passager_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Covoiturage_Passager_strategy)
def test_covoiturage_passager_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original

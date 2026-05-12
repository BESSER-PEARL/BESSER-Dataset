import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Participant,
    Formateur,
    Prestation,
    Type,
    Convention,
    Facture,
    DevisEntete,
    Formation,
    Client,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_participant_is_not_abstract():
    assert not inspect.isabstract(Participant)


def test_participant_constructor_exists():
    assert callable(Participant.__init__)


def test_participant_constructor_args():
    sig = inspect.signature(Participant.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id_session" in params, "Missing parameter 'id_session'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "date_naissance" in params, "Missing parameter 'date_naissance'"

def test_participant_has_nom():
    assert hasattr(Participant, "nom")
    descriptor = None
    for klass in Participant.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_participant_has_id_session():
    assert hasattr(Participant, "id_session")
    descriptor = None
    for klass in Participant.__mro__:
        if "id_session" in klass.__dict__:
            descriptor = klass.__dict__["id_session"]
            break
    assert isinstance(descriptor, property)

def test_participant_has_prenom():
    assert hasattr(Participant, "prenom")
    descriptor = None
    for klass in Participant.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_participant_has_date_naissance():
    assert hasattr(Participant, "date_naissance")
    descriptor = None
    for klass in Participant.__mro__:
        if "date_naissance" in klass.__dict__:
            descriptor = klass.__dict__["date_naissance"]
            break
    assert isinstance(descriptor, property)



def test_formateur_is_not_abstract():
    assert not inspect.isabstract(Formateur)


def test_formateur_constructor_exists():
    assert callable(Formateur.__init__)


def test_formateur_constructor_args():
    sig = inspect.signature(Formateur.__init__)
    params = list(sig.parameters.keys())
    assert "Nom" in params, "Missing parameter 'Nom'"
    assert "Prenom" in params, "Missing parameter 'Prenom'"

def test_formateur_has_Nom():
    assert hasattr(Formateur, "Nom")
    descriptor = None
    for klass in Formateur.__mro__:
        if "Nom" in klass.__dict__:
            descriptor = klass.__dict__["Nom"]
            break
    assert isinstance(descriptor, property)

def test_formateur_has_Prenom():
    assert hasattr(Formateur, "Prenom")
    descriptor = None
    for klass in Formateur.__mro__:
        if "Prenom" in klass.__dict__:
            descriptor = klass.__dict__["Prenom"]
            break
    assert isinstance(descriptor, property)



def test_prestation_is_not_abstract():
    assert not inspect.isabstract(Prestation)


def test_prestation_constructor_exists():
    assert callable(Prestation.__init__)


def test_prestation_constructor_args():
    sig = inspect.signature(Prestation.__init__)
    params = list(sig.parameters.keys())
    assert "horaires" in params, "Missing parameter 'horaires'"
    assert "duree" in params, "Missing parameter 'duree'"
    assert "nb_stagiaires" in params, "Missing parameter 'nb_stagiaires'"
    assert "id_client" in params, "Missing parameter 'id_client'"
    assert "id_formateur" in params, "Missing parameter 'id_formateur'"
    assert "id_type" in params, "Missing parameter 'id_type'"
    assert "id_formation" in params, "Missing parameter 'id_formation'"
    assert "lieu" in params, "Missing parameter 'lieu'"
    assert "date_debut" in params, "Missing parameter 'date_debut'"
    assert "date_fin" in params, "Missing parameter 'date_fin'"

def test_prestation_has_horaires():
    assert hasattr(Prestation, "horaires")
    descriptor = None
    for klass in Prestation.__mro__:
        if "horaires" in klass.__dict__:
            descriptor = klass.__dict__["horaires"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_duree():
    assert hasattr(Prestation, "duree")
    descriptor = None
    for klass in Prestation.__mro__:
        if "duree" in klass.__dict__:
            descriptor = klass.__dict__["duree"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_nb_stagiaires():
    assert hasattr(Prestation, "nb_stagiaires")
    descriptor = None
    for klass in Prestation.__mro__:
        if "nb_stagiaires" in klass.__dict__:
            descriptor = klass.__dict__["nb_stagiaires"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_id_client():
    assert hasattr(Prestation, "id_client")
    descriptor = None
    for klass in Prestation.__mro__:
        if "id_client" in klass.__dict__:
            descriptor = klass.__dict__["id_client"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_id_formateur():
    assert hasattr(Prestation, "id_formateur")
    descriptor = None
    for klass in Prestation.__mro__:
        if "id_formateur" in klass.__dict__:
            descriptor = klass.__dict__["id_formateur"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_id_type():
    assert hasattr(Prestation, "id_type")
    descriptor = None
    for klass in Prestation.__mro__:
        if "id_type" in klass.__dict__:
            descriptor = klass.__dict__["id_type"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_id_formation():
    assert hasattr(Prestation, "id_formation")
    descriptor = None
    for klass in Prestation.__mro__:
        if "id_formation" in klass.__dict__:
            descriptor = klass.__dict__["id_formation"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_lieu():
    assert hasattr(Prestation, "lieu")
    descriptor = None
    for klass in Prestation.__mro__:
        if "lieu" in klass.__dict__:
            descriptor = klass.__dict__["lieu"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_date_debut():
    assert hasattr(Prestation, "date_debut")
    descriptor = None
    for klass in Prestation.__mro__:
        if "date_debut" in klass.__dict__:
            descriptor = klass.__dict__["date_debut"]
            break
    assert isinstance(descriptor, property)

def test_prestation_has_date_fin():
    assert hasattr(Prestation, "date_fin")
    descriptor = None
    for klass in Prestation.__mro__:
        if "date_fin" in klass.__dict__:
            descriptor = klass.__dict__["date_fin"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_type_has_type():
    assert hasattr(Type, "type")
    descriptor = None
    for klass in Type.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_convention_is_not_abstract():
    assert not inspect.isabstract(Convention)


def test_convention_constructor_exists():
    assert callable(Convention.__init__)


def test_convention_constructor_args():
    sig = inspect.signature(Convention.__init__)
    params = list(sig.parameters.keys())
    assert "id_convention" in params, "Missing parameter 'id_convention'"
    assert "numero" in params, "Missing parameter 'numero'"

def test_convention_has_id_convention():
    assert hasattr(Convention, "id_convention")
    descriptor = None
    for klass in Convention.__mro__:
        if "id_convention" in klass.__dict__:
            descriptor = klass.__dict__["id_convention"]
            break
    assert isinstance(descriptor, property)

def test_convention_has_numero():
    assert hasattr(Convention, "numero")
    descriptor = None
    for klass in Convention.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)



def test_facture_is_not_abstract():
    assert not inspect.isabstract(Facture)


def test_facture_constructor_exists():
    assert callable(Facture.__init__)


def test_facture_constructor_args():
    sig = inspect.signature(Facture.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "paye" in params, "Missing parameter 'paye'"
    assert "id_devis" in params, "Missing parameter 'id_devis'"

def test_facture_has_numero():
    assert hasattr(Facture, "numero")
    descriptor = None
    for klass in Facture.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_facture_has_paye():
    assert hasattr(Facture, "paye")
    descriptor = None
    for klass in Facture.__mro__:
        if "paye" in klass.__dict__:
            descriptor = klass.__dict__["paye"]
            break
    assert isinstance(descriptor, property)

def test_facture_has_id_devis():
    assert hasattr(Facture, "id_devis")
    descriptor = None
    for klass in Facture.__mro__:
        if "id_devis" in klass.__dict__:
            descriptor = klass.__dict__["id_devis"]
            break
    assert isinstance(descriptor, property)



def test_devisentete_is_not_abstract():
    assert not inspect.isabstract(DevisEntete)


def test_devisentete_constructor_exists():
    assert callable(DevisEntete.__init__)


def test_devisentete_constructor_args():
    sig = inspect.signature(DevisEntete.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "id_session" in params, "Missing parameter 'id_session'"

def test_devisentete_has_numero():
    assert hasattr(DevisEntete, "numero")
    descriptor = None
    for klass in DevisEntete.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_devisentete_has_id_session():
    assert hasattr(DevisEntete, "id_session")
    descriptor = None
    for klass in DevisEntete.__mro__:
        if "id_session" in klass.__dict__:
            descriptor = klass.__dict__["id_session"]
            break
    assert isinstance(descriptor, property)



def test_formation_is_not_abstract():
    assert not inspect.isabstract(Formation)


def test_formation_constructor_exists():
    assert callable(Formation.__init__)


def test_formation_constructor_args():
    sig = inspect.signature(Formation.__init__)
    params = list(sig.parameters.keys())
    assert "cout_unitaire" in params, "Missing parameter 'cout_unitaire'"
    assert "objectif" in params, "Missing parameter 'objectif'"
    assert "libelle" in params, "Missing parameter 'libelle'"

def test_formation_has_cout_unitaire():
    assert hasattr(Formation, "cout_unitaire")
    descriptor = None
    for klass in Formation.__mro__:
        if "cout_unitaire" in klass.__dict__:
            descriptor = klass.__dict__["cout_unitaire"]
            break
    assert isinstance(descriptor, property)

def test_formation_has_objectif():
    assert hasattr(Formation, "objectif")
    descriptor = None
    for klass in Formation.__mro__:
        if "objectif" in klass.__dict__:
            descriptor = klass.__dict__["objectif"]
            break
    assert isinstance(descriptor, property)

def test_formation_has_libelle():
    assert hasattr(Formation, "libelle")
    descriptor = None
    for klass in Formation.__mro__:
        if "libelle" in klass.__dict__:
            descriptor = klass.__dict__["libelle"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "codePostal" in params, "Missing parameter 'codePostal'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "tel" in params, "Missing parameter 'tel'"
    assert "ville" in params, "Missing parameter 'ville'"
    assert "adresse" in params, "Missing parameter 'adresse'"

def test_client_has_codePostal():
    assert hasattr(Client, "codePostal")
    descriptor = None
    for klass in Client.__mro__:
        if "codePostal" in klass.__dict__:
            descriptor = klass.__dict__["codePostal"]
            break
    assert isinstance(descriptor, property)

def test_client_has_nom():
    assert hasattr(Client, "nom")
    descriptor = None
    for klass in Client.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_client_has_contact():
    assert hasattr(Client, "contact")
    descriptor = None
    for klass in Client.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_client_has_tel():
    assert hasattr(Client, "tel")
    descriptor = None
    for klass in Client.__mro__:
        if "tel" in klass.__dict__:
            descriptor = klass.__dict__["tel"]
            break
    assert isinstance(descriptor, property)

def test_client_has_ville():
    assert hasattr(Client, "ville")
    descriptor = None
    for klass in Client.__mro__:
        if "ville" in klass.__dict__:
            descriptor = klass.__dict__["ville"]
            break
    assert isinstance(descriptor, property)

def test_client_has_adresse():
    assert hasattr(Client, "adresse")
    descriptor = None
    for klass in Client.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
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
Participant_strategy = st.builds(
    Participant,
    nom=
        safe_text,
    id_session=
        st.integers(),
    prenom=
        safe_text,
    date_naissance=
        safe_text
)
Formateur_strategy = st.builds(
    Formateur,
    Nom=
        safe_text,
    Prenom=
        safe_text
)
Prestation_strategy = st.builds(
    Prestation,
    horaires=
        safe_text,
    duree=
        safe_text,
    nb_stagiaires=
        st.integers(),
    id_client=
        st.integers(),
    id_formateur=
        st.integers(),
    id_type=
        st.integers(),
    id_formation=
        st.integers(),
    lieu=
        st.booleans(),
    date_debut=
        safe_text,
    date_fin=
        safe_text
)
Type_strategy = st.builds(
    Type,
    type=
        safe_text
)
Convention_strategy = st.builds(
    Convention,
    id_convention=
        st.integers(),
    numero=
        safe_text
)
Facture_strategy = st.builds(
    Facture,
    numero=
        safe_text,
    paye=
        st.booleans(),
    id_devis=
        st.integers()
)
DevisEntete_strategy = st.builds(
    DevisEntete,
    numero=
        safe_text,
    id_session=
        st.integers()
)
Formation_strategy = st.builds(
    Formation,
    cout_unitaire=
        st.integers(),
    objectif=
        safe_text,
    libelle=
        safe_text
)
Client_strategy = st.builds(
    Client,
    codePostal=
        safe_text,
    nom=
        safe_text,
    contact=
        safe_text,
    tel=
        safe_text,
    ville=
        safe_text,
    adresse=
        safe_text
)

@given(instance=Participant_strategy)
@settings(max_examples=50)
def test_participant_instantiation(instance):
    assert isinstance(instance, Participant)



@given(instance=Participant_strategy)
def test_participant_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Participant_strategy)
def test_participant_id_session_setter(instance):
    original = instance.id_session
    instance.id_session = original
    assert instance.id_session == original



@given(instance=Participant_strategy)
def test_participant_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Participant_strategy)
def test_participant_date_naissance_setter(instance):
    original = instance.date_naissance
    instance.date_naissance = original
    assert instance.date_naissance == original

@given(instance=Formateur_strategy)
@settings(max_examples=50)
def test_formateur_instantiation(instance):
    assert isinstance(instance, Formateur)



@given(instance=Formateur_strategy)
def test_formateur_Nom_setter(instance):
    original = instance.Nom
    instance.Nom = original
    assert instance.Nom == original



@given(instance=Formateur_strategy)
def test_formateur_Prenom_setter(instance):
    original = instance.Prenom
    instance.Prenom = original
    assert instance.Prenom == original

@given(instance=Prestation_strategy)
@settings(max_examples=50)
def test_prestation_instantiation(instance):
    assert isinstance(instance, Prestation)



@given(instance=Prestation_strategy)
def test_prestation_horaires_setter(instance):
    original = instance.horaires
    instance.horaires = original
    assert instance.horaires == original



@given(instance=Prestation_strategy)
def test_prestation_duree_setter(instance):
    original = instance.duree
    instance.duree = original
    assert instance.duree == original



@given(instance=Prestation_strategy)
def test_prestation_nb_stagiaires_setter(instance):
    original = instance.nb_stagiaires
    instance.nb_stagiaires = original
    assert instance.nb_stagiaires == original



@given(instance=Prestation_strategy)
def test_prestation_id_client_setter(instance):
    original = instance.id_client
    instance.id_client = original
    assert instance.id_client == original



@given(instance=Prestation_strategy)
def test_prestation_id_formateur_setter(instance):
    original = instance.id_formateur
    instance.id_formateur = original
    assert instance.id_formateur == original



@given(instance=Prestation_strategy)
def test_prestation_id_type_setter(instance):
    original = instance.id_type
    instance.id_type = original
    assert instance.id_type == original



@given(instance=Prestation_strategy)
def test_prestation_id_formation_setter(instance):
    original = instance.id_formation
    instance.id_formation = original
    assert instance.id_formation == original



@given(instance=Prestation_strategy)
def test_prestation_lieu_setter(instance):
    original = instance.lieu
    instance.lieu = original
    assert instance.lieu == original



@given(instance=Prestation_strategy)
def test_prestation_date_debut_setter(instance):
    original = instance.date_debut
    instance.date_debut = original
    assert instance.date_debut == original



@given(instance=Prestation_strategy)
def test_prestation_date_fin_setter(instance):
    original = instance.date_fin
    instance.date_fin = original
    assert instance.date_fin == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)



@given(instance=Type_strategy)
def test_type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Convention_strategy)
@settings(max_examples=50)
def test_convention_instantiation(instance):
    assert isinstance(instance, Convention)



@given(instance=Convention_strategy)
def test_convention_id_convention_setter(instance):
    original = instance.id_convention
    instance.id_convention = original
    assert instance.id_convention == original



@given(instance=Convention_strategy)
def test_convention_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original

@given(instance=Facture_strategy)
@settings(max_examples=50)
def test_facture_instantiation(instance):
    assert isinstance(instance, Facture)



@given(instance=Facture_strategy)
def test_facture_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Facture_strategy)
def test_facture_paye_setter(instance):
    original = instance.paye
    instance.paye = original
    assert instance.paye == original



@given(instance=Facture_strategy)
def test_facture_id_devis_setter(instance):
    original = instance.id_devis
    instance.id_devis = original
    assert instance.id_devis == original

@given(instance=DevisEntete_strategy)
@settings(max_examples=50)
def test_devisentete_instantiation(instance):
    assert isinstance(instance, DevisEntete)



@given(instance=DevisEntete_strategy)
def test_devisentete_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=DevisEntete_strategy)
def test_devisentete_id_session_setter(instance):
    original = instance.id_session
    instance.id_session = original
    assert instance.id_session == original

@given(instance=Formation_strategy)
@settings(max_examples=50)
def test_formation_instantiation(instance):
    assert isinstance(instance, Formation)



@given(instance=Formation_strategy)
def test_formation_cout_unitaire_setter(instance):
    original = instance.cout_unitaire
    instance.cout_unitaire = original
    assert instance.cout_unitaire == original



@given(instance=Formation_strategy)
def test_formation_objectif_setter(instance):
    original = instance.objectif
    instance.objectif = original
    assert instance.objectif == original



@given(instance=Formation_strategy)
def test_formation_libelle_setter(instance):
    original = instance.libelle
    instance.libelle = original
    assert instance.libelle == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)



@given(instance=Client_strategy)
def test_client_codePostal_setter(instance):
    original = instance.codePostal
    instance.codePostal = original
    assert instance.codePostal == original



@given(instance=Client_strategy)
def test_client_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Client_strategy)
def test_client_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Client_strategy)
def test_client_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original



@given(instance=Client_strategy)
def test_client_ville_setter(instance):
    original = instance.ville
    instance.ville = original
    assert instance.ville == original



@given(instance=Client_strategy)
def test_client_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original

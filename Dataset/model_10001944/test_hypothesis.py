import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CoursCode,
    CoursConduite,
    Groupe,
    Candidat,
    Professeur,
    Examen,
    cours,
    Voiture,
    Utilisateur,
    Personne,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_courscode_is_not_abstract():
    assert not inspect.isabstract(CoursCode)


def test_courscode_constructor_exists():
    assert callable(CoursCode.__init__)


def test_courscode_constructor_args():
    sig = inspect.signature(CoursCode.__init__)
    params = list(sig.parameters.keys())



def test_coursconduite_is_not_abstract():
    assert not inspect.isabstract(CoursConduite)


def test_coursconduite_constructor_exists():
    assert callable(CoursConduite.__init__)


def test_coursconduite_constructor_args():
    sig = inspect.signature(CoursConduite.__init__)
    params = list(sig.parameters.keys())



def test_groupe_is_not_abstract():
    assert not inspect.isabstract(Groupe)


def test_groupe_constructor_exists():
    assert callable(Groupe.__init__)


def test_groupe_constructor_args():
    sig = inspect.signature(Groupe.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "libelle" in params, "Missing parameter 'libelle'"
    assert "numeroGroupe" in params, "Missing parameter 'numeroGroupe'"

def test_groupe_has_id():
    assert hasattr(Groupe, "id")
    descriptor = None
    for klass in Groupe.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_groupe_has_libelle():
    assert hasattr(Groupe, "libelle")
    descriptor = None
    for klass in Groupe.__mro__:
        if "libelle" in klass.__dict__:
            descriptor = klass.__dict__["libelle"]
            break
    assert isinstance(descriptor, property)

def test_groupe_has_numeroGroupe():
    assert hasattr(Groupe, "numeroGroupe")
    descriptor = None
    for klass in Groupe.__mro__:
        if "numeroGroupe" in klass.__dict__:
            descriptor = klass.__dict__["numeroGroupe"]
            break
    assert isinstance(descriptor, property)



def test_candidat_is_not_abstract():
    assert not inspect.isabstract(Candidat)


def test_candidat_constructor_exists():
    assert callable(Candidat.__init__)


def test_candidat_constructor_args():
    sig = inspect.signature(Candidat.__init__)
    params = list(sig.parameters.keys())



def test_professeur_is_not_abstract():
    assert not inspect.isabstract(Professeur)


def test_professeur_constructor_exists():
    assert callable(Professeur.__init__)


def test_professeur_constructor_args():
    sig = inspect.signature(Professeur.__init__)
    params = list(sig.parameters.keys())
    assert "dateEmbauche" in params, "Missing parameter 'dateEmbauche'"

def test_professeur_has_dateEmbauche():
    assert hasattr(Professeur, "dateEmbauche")
    descriptor = None
    for klass in Professeur.__mro__:
        if "dateEmbauche" in klass.__dict__:
            descriptor = klass.__dict__["dateEmbauche"]
            break
    assert isinstance(descriptor, property)



def test_examen_is_not_abstract():
    assert not inspect.isabstract(Examen)


def test_examen_constructor_exists():
    assert callable(Examen.__init__)


def test_examen_constructor_args():
    sig = inspect.signature(Examen.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "heureF" in params, "Missing parameter 'heureF'"
    assert "heureD" in params, "Missing parameter 'heureD'"
    assert "dateExamen" in params, "Missing parameter 'dateExamen'"
    assert "typeExamen" in params, "Missing parameter 'typeExamen'"

def test_examen_has_id():
    assert hasattr(Examen, "id")
    descriptor = None
    for klass in Examen.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_heureF():
    assert hasattr(Examen, "heureF")
    descriptor = None
    for klass in Examen.__mro__:
        if "heureF" in klass.__dict__:
            descriptor = klass.__dict__["heureF"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_heureD():
    assert hasattr(Examen, "heureD")
    descriptor = None
    for klass in Examen.__mro__:
        if "heureD" in klass.__dict__:
            descriptor = klass.__dict__["heureD"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_dateExamen():
    assert hasattr(Examen, "dateExamen")
    descriptor = None
    for klass in Examen.__mro__:
        if "dateExamen" in klass.__dict__:
            descriptor = klass.__dict__["dateExamen"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_typeExamen():
    assert hasattr(Examen, "typeExamen")
    descriptor = None
    for klass in Examen.__mro__:
        if "typeExamen" in klass.__dict__:
            descriptor = klass.__dict__["typeExamen"]
            break
    assert isinstance(descriptor, property)



def test_cours_is_not_abstract():
    assert not inspect.isabstract(cours)


def test_cours_constructor_exists():
    assert callable(cours.__init__)


def test_cours_constructor_args():
    sig = inspect.signature(cours.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "dateCours" in params, "Missing parameter 'dateCours'"
    assert "heureF" in params, "Missing parameter 'heureF'"
    assert "heureD" in params, "Missing parameter 'heureD'"

def test_cours_has_id():
    assert hasattr(cours, "id")
    descriptor = None
    for klass in cours.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cours_has_dateCours():
    assert hasattr(cours, "dateCours")
    descriptor = None
    for klass in cours.__mro__:
        if "dateCours" in klass.__dict__:
            descriptor = klass.__dict__["dateCours"]
            break
    assert isinstance(descriptor, property)

def test_cours_has_heureF():
    assert hasattr(cours, "heureF")
    descriptor = None
    for klass in cours.__mro__:
        if "heureF" in klass.__dict__:
            descriptor = klass.__dict__["heureF"]
            break
    assert isinstance(descriptor, property)

def test_cours_has_heureD():
    assert hasattr(cours, "heureD")
    descriptor = None
    for klass in cours.__mro__:
        if "heureD" in klass.__dict__:
            descriptor = klass.__dict__["heureD"]
            break
    assert isinstance(descriptor, property)



def test_voiture_is_not_abstract():
    assert not inspect.isabstract(Voiture)


def test_voiture_constructor_exists():
    assert callable(Voiture.__init__)


def test_voiture_constructor_args():
    sig = inspect.signature(Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "modele" in params, "Missing parameter 'modele'"
    assert "id" in params, "Missing parameter 'id'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "immatriculation" in params, "Missing parameter 'immatriculation'"

def test_voiture_has_modele():
    assert hasattr(Voiture, "modele")
    descriptor = None
    for klass in Voiture.__mro__:
        if "modele" in klass.__dict__:
            descriptor = klass.__dict__["modele"]
            break
    assert isinstance(descriptor, property)

def test_voiture_has_id():
    assert hasattr(Voiture, "id")
    descriptor = None
    for klass in Voiture.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_voiture_has_marque():
    assert hasattr(Voiture, "marque")
    descriptor = None
    for klass in Voiture.__mro__:
        if "marque" in klass.__dict__:
            descriptor = klass.__dict__["marque"]
            break
    assert isinstance(descriptor, property)

def test_voiture_has_immatriculation():
    assert hasattr(Voiture, "immatriculation")
    descriptor = None
    for klass in Voiture.__mro__:
        if "immatriculation" in klass.__dict__:
            descriptor = klass.__dict__["immatriculation"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "mdp" in params, "Missing parameter 'mdp'"
    assert "login" in params, "Missing parameter 'login'"

def test_utilisateur_has_mdp():
    assert hasattr(Utilisateur, "mdp")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "mdp" in klass.__dict__:
            descriptor = klass.__dict__["mdp"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_login():
    assert hasattr(Utilisateur, "login")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)



def test_personne_is_not_abstract():
    assert not inspect.isabstract(Personne)


def test_personne_constructor_exists():
    assert callable(Personne.__init__)


def test_personne_constructor_args():
    sig = inspect.signature(Personne.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "dateNaissance" in params, "Missing parameter 'dateNaissance'"
    assert "email" in params, "Missing parameter 'email'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lieuNaissance" in params, "Missing parameter 'lieuNaissance'"
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "numeroCIN" in params, "Missing parameter 'numeroCIN'"

def test_personne_has_nom():
    assert hasattr(Personne, "nom")
    descriptor = None
    for klass in Personne.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_telephone():
    assert hasattr(Personne, "telephone")
    descriptor = None
    for klass in Personne.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_dateNaissance():
    assert hasattr(Personne, "dateNaissance")
    descriptor = None
    for klass in Personne.__mro__:
        if "dateNaissance" in klass.__dict__:
            descriptor = klass.__dict__["dateNaissance"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_email():
    assert hasattr(Personne, "email")
    descriptor = None
    for klass in Personne.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_prenom():
    assert hasattr(Personne, "prenom")
    descriptor = None
    for klass in Personne.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_id():
    assert hasattr(Personne, "id")
    descriptor = None
    for klass in Personne.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_lieuNaissance():
    assert hasattr(Personne, "lieuNaissance")
    descriptor = None
    for klass in Personne.__mro__:
        if "lieuNaissance" in klass.__dict__:
            descriptor = klass.__dict__["lieuNaissance"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_adresse():
    assert hasattr(Personne, "adresse")
    descriptor = None
    for klass in Personne.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_numeroCIN():
    assert hasattr(Personne, "numeroCIN")
    descriptor = None
    for klass in Personne.__mro__:
        if "numeroCIN" in klass.__dict__:
            descriptor = klass.__dict__["numeroCIN"]
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
CoursCode_strategy = st.builds(
    CoursCode,
)
CoursConduite_strategy = st.builds(
    CoursConduite,
)
Groupe_strategy = st.builds(
    Groupe,
    id=
        st.integers(),
    libelle=
        safe_text,
    numeroGroupe=
        st.integers()
)
Candidat_strategy = st.builds(
    Candidat,
)
Professeur_strategy = st.builds(
    Professeur,
    dateEmbauche=
        safe_text
)
Examen_strategy = st.builds(
    Examen,
    id=
        st.integers(),
    heureF=
        safe_text,
    heureD=
        safe_text,
    dateExamen=
        safe_text,
    typeExamen=
        safe_text
)
cours_strategy = st.builds(
    cours,
    id=
        st.integers(),
    dateCours=
        safe_text,
    heureF=
        safe_text,
    heureD=
        safe_text
)
Voiture_strategy = st.builds(
    Voiture,
    modele=
        safe_text,
    id=
        st.integers(),
    marque=
        safe_text,
    immatriculation=
        safe_text
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    mdp=
        safe_text,
    login=
        safe_text
)
Personne_strategy = st.builds(
    Personne,
    nom=
        safe_text,
    telephone=
        safe_text,
    dateNaissance=
        safe_text,
    email=
        safe_text,
    prenom=
        safe_text,
    id=
        st.integers(),
    lieuNaissance=
        safe_text,
    adresse=
        safe_text,
    numeroCIN=
        st.integers()
)

@given(instance=CoursCode_strategy)
@settings(max_examples=50)
def test_courscode_instantiation(instance):
    assert isinstance(instance, CoursCode)

@given(instance=CoursConduite_strategy)
@settings(max_examples=50)
def test_coursconduite_instantiation(instance):
    assert isinstance(instance, CoursConduite)

@given(instance=Groupe_strategy)
@settings(max_examples=50)
def test_groupe_instantiation(instance):
    assert isinstance(instance, Groupe)



@given(instance=Groupe_strategy)
def test_groupe_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Groupe_strategy)
def test_groupe_libelle_setter(instance):
    original = instance.libelle
    instance.libelle = original
    assert instance.libelle == original



@given(instance=Groupe_strategy)
def test_groupe_numeroGroupe_setter(instance):
    original = instance.numeroGroupe
    instance.numeroGroupe = original
    assert instance.numeroGroupe == original

@given(instance=Candidat_strategy)
@settings(max_examples=50)
def test_candidat_instantiation(instance):
    assert isinstance(instance, Candidat)

@given(instance=Professeur_strategy)
@settings(max_examples=50)
def test_professeur_instantiation(instance):
    assert isinstance(instance, Professeur)



@given(instance=Professeur_strategy)
def test_professeur_dateEmbauche_setter(instance):
    original = instance.dateEmbauche
    instance.dateEmbauche = original
    assert instance.dateEmbauche == original

@given(instance=Examen_strategy)
@settings(max_examples=50)
def test_examen_instantiation(instance):
    assert isinstance(instance, Examen)



@given(instance=Examen_strategy)
def test_examen_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Examen_strategy)
def test_examen_heureF_setter(instance):
    original = instance.heureF
    instance.heureF = original
    assert instance.heureF == original



@given(instance=Examen_strategy)
def test_examen_heureD_setter(instance):
    original = instance.heureD
    instance.heureD = original
    assert instance.heureD == original



@given(instance=Examen_strategy)
def test_examen_dateExamen_setter(instance):
    original = instance.dateExamen
    instance.dateExamen = original
    assert instance.dateExamen == original



@given(instance=Examen_strategy)
def test_examen_typeExamen_setter(instance):
    original = instance.typeExamen
    instance.typeExamen = original
    assert instance.typeExamen == original

@given(instance=cours_strategy)
@settings(max_examples=50)
def test_cours_instantiation(instance):
    assert isinstance(instance, cours)



@given(instance=cours_strategy)
def test_cours_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=cours_strategy)
def test_cours_dateCours_setter(instance):
    original = instance.dateCours
    instance.dateCours = original
    assert instance.dateCours == original



@given(instance=cours_strategy)
def test_cours_heureF_setter(instance):
    original = instance.heureF
    instance.heureF = original
    assert instance.heureF == original



@given(instance=cours_strategy)
def test_cours_heureD_setter(instance):
    original = instance.heureD
    instance.heureD = original
    assert instance.heureD == original

@given(instance=Voiture_strategy)
@settings(max_examples=50)
def test_voiture_instantiation(instance):
    assert isinstance(instance, Voiture)



@given(instance=Voiture_strategy)
def test_voiture_modele_setter(instance):
    original = instance.modele
    instance.modele = original
    assert instance.modele == original



@given(instance=Voiture_strategy)
def test_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Voiture_strategy)
def test_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=Voiture_strategy)
def test_voiture_immatriculation_setter(instance):
    original = instance.immatriculation
    instance.immatriculation = original
    assert instance.immatriculation == original

@given(instance=Utilisateur_strategy)
@settings(max_examples=50)
def test_utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)



@given(instance=Utilisateur_strategy)
def test_utilisateur_mdp_setter(instance):
    original = instance.mdp
    instance.mdp = original
    assert instance.mdp == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original

@given(instance=Personne_strategy)
@settings(max_examples=50)
def test_personne_instantiation(instance):
    assert isinstance(instance, Personne)



@given(instance=Personne_strategy)
def test_personne_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Personne_strategy)
def test_personne_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Personne_strategy)
def test_personne_dateNaissance_setter(instance):
    original = instance.dateNaissance
    instance.dateNaissance = original
    assert instance.dateNaissance == original



@given(instance=Personne_strategy)
def test_personne_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Personne_strategy)
def test_personne_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Personne_strategy)
def test_personne_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Personne_strategy)
def test_personne_lieuNaissance_setter(instance):
    original = instance.lieuNaissance
    instance.lieuNaissance = original
    assert instance.lieuNaissance == original



@given(instance=Personne_strategy)
def test_personne_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Personne_strategy)
def test_personne_numeroCIN_setter(instance):
    original = instance.numeroCIN
    instance.numeroCIN = original
    assert instance.numeroCIN == original

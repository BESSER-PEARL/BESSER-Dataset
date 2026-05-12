import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Test,
    Compte,
    Patient,
    Agenda,
    AgendaPartage,
    RDV,
    Medecin,
    EmployeAdministratif,
    Employe,
    Personne,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_test_constructor_exists():
    assert callable(Test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())
    assert "Prenom" in params, "Missing parameter 'Prenom'"

def test_test_has_Prenom():
    assert hasattr(Test, "Prenom")
    descriptor = None
    for klass in Test.__mro__:
        if "Prenom" in klass.__dict__:
            descriptor = klass.__dict__["Prenom"]
            break
    assert isinstance(descriptor, property)



def test_compte_is_not_abstract():
    assert not inspect.isabstract(Compte)


def test_compte_constructor_exists():
    assert callable(Compte.__init__)


def test_compte_constructor_args():
    sig = inspect.signature(Compte.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "typeCompte" in params, "Missing parameter 'typeCompte'"
    assert "password" in params, "Missing parameter 'password'"

def test_compte_has_login():
    assert hasattr(Compte, "login")
    descriptor = None
    for klass in Compte.__mro__:
        if "login" in klass.__dict__:
            descriptor = klass.__dict__["login"]
            break
    assert isinstance(descriptor, property)

def test_compte_has_typeCompte():
    assert hasattr(Compte, "typeCompte")
    descriptor = None
    for klass in Compte.__mro__:
        if "typeCompte" in klass.__dict__:
            descriptor = klass.__dict__["typeCompte"]
            break
    assert isinstance(descriptor, property)

def test_compte_has_password():
    assert hasattr(Compte, "password")
    descriptor = None
    for klass in Compte.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "antecedent" in params, "Missing parameter 'antecedent'"
    assert "allergies" in params, "Missing parameter 'allergies'"
    assert "traitement" in params, "Missing parameter 'traitement'"

def test_patient_has_antecedent():
    assert hasattr(Patient, "antecedent")
    descriptor = None
    for klass in Patient.__mro__:
        if "antecedent" in klass.__dict__:
            descriptor = klass.__dict__["antecedent"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_allergies():
    assert hasattr(Patient, "allergies")
    descriptor = None
    for klass in Patient.__mro__:
        if "allergies" in klass.__dict__:
            descriptor = klass.__dict__["allergies"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_traitement():
    assert hasattr(Patient, "traitement")
    descriptor = None
    for klass in Patient.__mro__:
        if "traitement" in klass.__dict__:
            descriptor = klass.__dict__["traitement"]
            break
    assert isinstance(descriptor, property)



def test_agenda_is_not_abstract():
    assert not inspect.isabstract(Agenda)


def test_agenda_constructor_exists():
    assert callable(Agenda.__init__)


def test_agenda_constructor_args():
    sig = inspect.signature(Agenda.__init__)
    params = list(sig.parameters.keys())
    assert "annee" in params, "Missing parameter 'annee'"

def test_agenda_has_annee():
    assert hasattr(Agenda, "annee")
    descriptor = None
    for klass in Agenda.__mro__:
        if "annee" in klass.__dict__:
            descriptor = klass.__dict__["annee"]
            break
    assert isinstance(descriptor, property)



def test_agendapartage_is_not_abstract():
    assert not inspect.isabstract(AgendaPartage)


def test_agendapartage_constructor_exists():
    assert callable(AgendaPartage.__init__)


def test_agendapartage_constructor_args():
    sig = inspect.signature(AgendaPartage.__init__)
    params = list(sig.parameters.keys())



def test_rdv_is_not_abstract():
    assert not inspect.isabstract(RDV)


def test_rdv_constructor_exists():
    assert callable(RDV.__init__)


def test_rdv_constructor_args():
    sig = inspect.signature(RDV.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "duree" in params, "Missing parameter 'duree'"
    assert "heure" in params, "Missing parameter 'heure'"

def test_rdv_has_date():
    assert hasattr(RDV, "date")
    descriptor = None
    for klass in RDV.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_rdv_has_duree():
    assert hasattr(RDV, "duree")
    descriptor = None
    for klass in RDV.__mro__:
        if "duree" in klass.__dict__:
            descriptor = klass.__dict__["duree"]
            break
    assert isinstance(descriptor, property)

def test_rdv_has_heure():
    assert hasattr(RDV, "heure")
    descriptor = None
    for klass in RDV.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)



def test_medecin_is_not_abstract():
    assert not inspect.isabstract(Medecin)


def test_medecin_constructor_exists():
    assert callable(Medecin.__init__)


def test_medecin_constructor_args():
    sig = inspect.signature(Medecin.__init__)
    params = list(sig.parameters.keys())
    assert "specialisation" in params, "Missing parameter 'specialisation'"

def test_medecin_has_specialisation():
    assert hasattr(Medecin, "specialisation")
    descriptor = None
    for klass in Medecin.__mro__:
        if "specialisation" in klass.__dict__:
            descriptor = klass.__dict__["specialisation"]
            break
    assert isinstance(descriptor, property)



def test_employeadministratif_is_not_abstract():
    assert not inspect.isabstract(EmployeAdministratif)


def test_employeadministratif_constructor_exists():
    assert callable(EmployeAdministratif.__init__)


def test_employeadministratif_constructor_args():
    sig = inspect.signature(EmployeAdministratif.__init__)
    params = list(sig.parameters.keys())
    assert "formation" in params, "Missing parameter 'formation'"

def test_employeadministratif_has_formation():
    assert hasattr(EmployeAdministratif, "formation")
    descriptor = None
    for klass in EmployeAdministratif.__mro__:
        if "formation" in klass.__dict__:
            descriptor = klass.__dict__["formation"]
            break
    assert isinstance(descriptor, property)



def test_employe_is_not_abstract():
    assert not inspect.isabstract(Employe)


def test_employe_constructor_exists():
    assert callable(Employe.__init__)


def test_employe_constructor_args():
    sig = inspect.signature(Employe.__init__)
    params = list(sig.parameters.keys())
    assert "joursVacance" in params, "Missing parameter 'joursVacance'"
    assert "salaire" in params, "Missing parameter 'salaire'"
    assert "dateDebut" in params, "Missing parameter 'dateDebut'"
    assert "dateFin" in params, "Missing parameter 'dateFin'"

def test_employe_has_joursVacance():
    assert hasattr(Employe, "joursVacance")
    descriptor = None
    for klass in Employe.__mro__:
        if "joursVacance" in klass.__dict__:
            descriptor = klass.__dict__["joursVacance"]
            break
    assert isinstance(descriptor, property)

def test_employe_has_salaire():
    assert hasattr(Employe, "salaire")
    descriptor = None
    for klass in Employe.__mro__:
        if "salaire" in klass.__dict__:
            descriptor = klass.__dict__["salaire"]
            break
    assert isinstance(descriptor, property)

def test_employe_has_dateDebut():
    assert hasattr(Employe, "dateDebut")
    descriptor = None
    for klass in Employe.__mro__:
        if "dateDebut" in klass.__dict__:
            descriptor = klass.__dict__["dateDebut"]
            break
    assert isinstance(descriptor, property)

def test_employe_has_dateFin():
    assert hasattr(Employe, "dateFin")
    descriptor = None
    for klass in Employe.__mro__:
        if "dateFin" in klass.__dict__:
            descriptor = klass.__dict__["dateFin"]
            break
    assert isinstance(descriptor, property)



def test_personne_is_not_abstract():
    assert not inspect.isabstract(Personne)


def test_personne_constructor_exists():
    assert callable(Personne.__init__)


def test_personne_constructor_args():
    sig = inspect.signature(Personne.__init__)
    params = list(sig.parameters.keys())
    assert "telPrive" in params, "Missing parameter 'telPrive'"
    assert "dateNaissance" in params, "Missing parameter 'dateNaissance'"
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "email" in params, "Missing parameter 'email'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "prenom" in params, "Missing parameter 'prenom'"

def test_personne_has_telPrive():
    assert hasattr(Personne, "telPrive")
    descriptor = None
    for klass in Personne.__mro__:
        if "telPrive" in klass.__dict__:
            descriptor = klass.__dict__["telPrive"]
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

def test_personne_has_adresse():
    assert hasattr(Personne, "adresse")
    descriptor = None
    for klass in Personne.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
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

def test_personne_has_nom():
    assert hasattr(Personne, "nom")
    descriptor = None
    for klass in Personne.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
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
Test_strategy = st.builds(
    Test,
    Prenom=
        safe_text
)
Compte_strategy = st.builds(
    Compte,
    login=
        safe_text,
    typeCompte=
        safe_text,
    password=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    antecedent=
        safe_text,
    allergies=
        safe_text,
    traitement=
        safe_text
)
Agenda_strategy = st.builds(
    Agenda,
    annee=
        safe_text
)
AgendaPartage_strategy = st.builds(
    AgendaPartage,
)
RDV_strategy = st.builds(
    RDV,
    date=
        safe_text,
    duree=
        st.integers(),
    heure=
        safe_text
)
Medecin_strategy = st.builds(
    Medecin,
    specialisation=
        safe_text
)
EmployeAdministratif_strategy = st.builds(
    EmployeAdministratif,
    formation=
        safe_text
)
Employe_strategy = st.builds(
    Employe,
    joursVacance=
        st.integers(),
    salaire=
        st.integers(),
    dateDebut=
        safe_text,
    dateFin=
        safe_text
)
Personne_strategy = st.builds(
    Personne,
    telPrive=
        safe_text,
    dateNaissance=
        safe_text,
    adresse=
        safe_text,
    email=
        safe_text,
    nom=
        safe_text,
    prenom=
        safe_text
)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)



@given(instance=Test_strategy)
def test_test_Prenom_setter(instance):
    original = instance.Prenom
    instance.Prenom = original
    assert instance.Prenom == original

@given(instance=Compte_strategy)
@settings(max_examples=50)
def test_compte_instantiation(instance):
    assert isinstance(instance, Compte)



@given(instance=Compte_strategy)
def test_compte_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=Compte_strategy)
def test_compte_typeCompte_setter(instance):
    original = instance.typeCompte
    instance.typeCompte = original
    assert instance.typeCompte == original



@given(instance=Compte_strategy)
def test_compte_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_antecedent_setter(instance):
    original = instance.antecedent
    instance.antecedent = original
    assert instance.antecedent == original



@given(instance=Patient_strategy)
def test_patient_allergies_setter(instance):
    original = instance.allergies
    instance.allergies = original
    assert instance.allergies == original



@given(instance=Patient_strategy)
def test_patient_traitement_setter(instance):
    original = instance.traitement
    instance.traitement = original
    assert instance.traitement == original

@given(instance=Agenda_strategy)
@settings(max_examples=50)
def test_agenda_instantiation(instance):
    assert isinstance(instance, Agenda)



@given(instance=Agenda_strategy)
def test_agenda_annee_setter(instance):
    original = instance.annee
    instance.annee = original
    assert instance.annee == original

@given(instance=AgendaPartage_strategy)
@settings(max_examples=50)
def test_agendapartage_instantiation(instance):
    assert isinstance(instance, AgendaPartage)

@given(instance=RDV_strategy)
@settings(max_examples=50)
def test_rdv_instantiation(instance):
    assert isinstance(instance, RDV)



@given(instance=RDV_strategy)
def test_rdv_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=RDV_strategy)
def test_rdv_duree_setter(instance):
    original = instance.duree
    instance.duree = original
    assert instance.duree == original



@given(instance=RDV_strategy)
def test_rdv_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original

@given(instance=Medecin_strategy)
@settings(max_examples=50)
def test_medecin_instantiation(instance):
    assert isinstance(instance, Medecin)



@given(instance=Medecin_strategy)
def test_medecin_specialisation_setter(instance):
    original = instance.specialisation
    instance.specialisation = original
    assert instance.specialisation == original

@given(instance=EmployeAdministratif_strategy)
@settings(max_examples=50)
def test_employeadministratif_instantiation(instance):
    assert isinstance(instance, EmployeAdministratif)



@given(instance=EmployeAdministratif_strategy)
def test_employeadministratif_formation_setter(instance):
    original = instance.formation
    instance.formation = original
    assert instance.formation == original

@given(instance=Employe_strategy)
@settings(max_examples=50)
def test_employe_instantiation(instance):
    assert isinstance(instance, Employe)



@given(instance=Employe_strategy)
def test_employe_joursVacance_setter(instance):
    original = instance.joursVacance
    instance.joursVacance = original
    assert instance.joursVacance == original



@given(instance=Employe_strategy)
def test_employe_salaire_setter(instance):
    original = instance.salaire
    instance.salaire = original
    assert instance.salaire == original



@given(instance=Employe_strategy)
def test_employe_dateDebut_setter(instance):
    original = instance.dateDebut
    instance.dateDebut = original
    assert instance.dateDebut == original



@given(instance=Employe_strategy)
def test_employe_dateFin_setter(instance):
    original = instance.dateFin
    instance.dateFin = original
    assert instance.dateFin == original

@given(instance=Personne_strategy)
@settings(max_examples=50)
def test_personne_instantiation(instance):
    assert isinstance(instance, Personne)



@given(instance=Personne_strategy)
def test_personne_telPrive_setter(instance):
    original = instance.telPrive
    instance.telPrive = original
    assert instance.telPrive == original



@given(instance=Personne_strategy)
def test_personne_dateNaissance_setter(instance):
    original = instance.dateNaissance
    instance.dateNaissance = original
    assert instance.dateNaissance == original



@given(instance=Personne_strategy)
def test_personne_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Personne_strategy)
def test_personne_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Personne_strategy)
def test_personne_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Personne_strategy)
def test_personne_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original

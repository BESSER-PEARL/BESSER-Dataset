import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Rendez_vous_Medecin_Patient_external,
    Rendez_vous_Laboratoire_Patient_external,
    Produit,
    Ordonance,
    Rendez_vous,
    Contact,
    Personne,
    Laboratoire,
    ResultatExamen,
    CentreHospitalier,
    Programme,
    Service,
    Medecin,
    Examen,
    Patient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rendez_vous_medecin_patient_external_is_not_abstract():
    assert not inspect.isabstract(Rendez_vous_Medecin_Patient_external)


def test_rendez_vous_medecin_patient_external_constructor_exists():
    assert callable(Rendez_vous_Medecin_Patient_external.__init__)


def test_rendez_vous_medecin_patient_external_constructor_args():
    sig = inspect.signature(Rendez_vous_Medecin_Patient_external.__init__)
    params = list(sig.parameters.keys())



def test_rendez_vous_laboratoire_patient_external_is_not_abstract():
    assert not inspect.isabstract(Rendez_vous_Laboratoire_Patient_external)


def test_rendez_vous_laboratoire_patient_external_constructor_exists():
    assert callable(Rendez_vous_Laboratoire_Patient_external.__init__)


def test_rendez_vous_laboratoire_patient_external_constructor_args():
    sig = inspect.signature(Rendez_vous_Laboratoire_Patient_external.__init__)
    params = list(sig.parameters.keys())



def test_produit_is_not_abstract():
    assert not inspect.isabstract(Produit)


def test_produit_constructor_exists():
    assert callable(Produit.__init__)


def test_produit_constructor_args():
    sig = inspect.signature(Produit.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "posologie" in params, "Missing parameter 'posologie'"
    assert "dose" in params, "Missing parameter 'dose'"

def test_produit_has_nom():
    assert hasattr(Produit, "nom")
    descriptor = None
    for klass in Produit.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_id():
    assert hasattr(Produit, "id")
    descriptor = None
    for klass in Produit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_posologie():
    assert hasattr(Produit, "posologie")
    descriptor = None
    for klass in Produit.__mro__:
        if "posologie" in klass.__dict__:
            descriptor = klass.__dict__["posologie"]
            break
    assert isinstance(descriptor, property)

def test_produit_has_dose():
    assert hasattr(Produit, "dose")
    descriptor = None
    for klass in Produit.__mro__:
        if "dose" in klass.__dict__:
            descriptor = klass.__dict__["dose"]
            break
    assert isinstance(descriptor, property)



def test_ordonance_is_not_abstract():
    assert not inspect.isabstract(Ordonance)


def test_ordonance_constructor_exists():
    assert callable(Ordonance.__init__)


def test_ordonance_constructor_args():
    sig = inspect.signature(Ordonance.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"

def test_ordonance_has_date():
    assert hasattr(Ordonance, "date")
    descriptor = None
    for klass in Ordonance.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_ordonance_has_id():
    assert hasattr(Ordonance, "id")
    descriptor = None
    for klass in Ordonance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_rendez_vous_is_not_abstract():
    assert not inspect.isabstract(Rendez_vous)


def test_rendez_vous_constructor_exists():
    assert callable(Rendez_vous.__init__)


def test_rendez_vous_constructor_args():
    sig = inspect.signature(Rendez_vous.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "numero" in params, "Missing parameter 'numero'"

def test_rendez_vous_has_id():
    assert hasattr(Rendez_vous, "id")
    descriptor = None
    for klass in Rendez_vous.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_rendez_vous_has_date():
    assert hasattr(Rendez_vous, "date")
    descriptor = None
    for klass in Rendez_vous.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_rendez_vous_has_numero():
    assert hasattr(Rendez_vous, "numero")
    descriptor = None
    for klass in Rendez_vous.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)



def test_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "mail" in params, "Missing parameter 'mail'"

def test_contact_has_id():
    assert hasattr(Contact, "id")
    descriptor = None
    for klass in Contact.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_contact_has_telephone():
    assert hasattr(Contact, "telephone")
    descriptor = None
    for klass in Contact.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_contact_has_mail():
    assert hasattr(Contact, "mail")
    descriptor = None
    for klass in Contact.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
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
    assert "numero" in params, "Missing parameter 'numero'"
    assert "numeroMedecin" in params, "Missing parameter 'numeroMedecin'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_personne_has_nom():
    assert hasattr(Personne, "nom")
    descriptor = None
    for klass in Personne.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_numero():
    assert hasattr(Personne, "numero")
    descriptor = None
    for klass in Personne.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_numeroMedecin():
    assert hasattr(Personne, "numeroMedecin")
    descriptor = None
    for klass in Personne.__mro__:
        if "numeroMedecin" in klass.__dict__:
            descriptor = klass.__dict__["numeroMedecin"]
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

def test_personne_has_attribute():
    assert hasattr(Personne, "attribute")
    descriptor = None
    for klass in Personne.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_laboratoire_is_not_abstract():
    assert not inspect.isabstract(Laboratoire)


def test_laboratoire_constructor_exists():
    assert callable(Laboratoire.__init__)


def test_laboratoire_constructor_args():
    sig = inspect.signature(Laboratoire.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "numero" in params, "Missing parameter 'numero'"

def test_laboratoire_has_id():
    assert hasattr(Laboratoire, "id")
    descriptor = None
    for klass in Laboratoire.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_laboratoire_has_nom():
    assert hasattr(Laboratoire, "nom")
    descriptor = None
    for klass in Laboratoire.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_laboratoire_has_numero():
    assert hasattr(Laboratoire, "numero")
    descriptor = None
    for klass in Laboratoire.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)



def test_resultatexamen_is_not_abstract():
    assert not inspect.isabstract(ResultatExamen)


def test_resultatexamen_constructor_exists():
    assert callable(ResultatExamen.__init__)


def test_resultatexamen_constructor_args():
    sig = inspect.signature(ResultatExamen.__init__)
    params = list(sig.parameters.keys())
    assert "numeroResultat" in params, "Missing parameter 'numeroResultat'"
    assert "infoResultat" in params, "Missing parameter 'infoResultat'"

def test_resultatexamen_has_numeroResultat():
    assert hasattr(ResultatExamen, "numeroResultat")
    descriptor = None
    for klass in ResultatExamen.__mro__:
        if "numeroResultat" in klass.__dict__:
            descriptor = klass.__dict__["numeroResultat"]
            break
    assert isinstance(descriptor, property)

def test_resultatexamen_has_infoResultat():
    assert hasattr(ResultatExamen, "infoResultat")
    descriptor = None
    for klass in ResultatExamen.__mro__:
        if "infoResultat" in klass.__dict__:
            descriptor = klass.__dict__["infoResultat"]
            break
    assert isinstance(descriptor, property)



def test_centrehospitalier_is_not_abstract():
    assert not inspect.isabstract(CentreHospitalier)


def test_centrehospitalier_constructor_exists():
    assert callable(CentreHospitalier.__init__)


def test_centrehospitalier_constructor_args():
    sig = inspect.signature(CentreHospitalier.__init__)
    params = list(sig.parameters.keys())
    assert "nomCentre" in params, "Missing parameter 'nomCentre'"
    assert "descriptionCentre" in params, "Missing parameter 'descriptionCentre'"
    assert "numeroCentre" in params, "Missing parameter 'numeroCentre'"

def test_centrehospitalier_has_nomCentre():
    assert hasattr(CentreHospitalier, "nomCentre")
    descriptor = None
    for klass in CentreHospitalier.__mro__:
        if "nomCentre" in klass.__dict__:
            descriptor = klass.__dict__["nomCentre"]
            break
    assert isinstance(descriptor, property)

def test_centrehospitalier_has_descriptionCentre():
    assert hasattr(CentreHospitalier, "descriptionCentre")
    descriptor = None
    for klass in CentreHospitalier.__mro__:
        if "descriptionCentre" in klass.__dict__:
            descriptor = klass.__dict__["descriptionCentre"]
            break
    assert isinstance(descriptor, property)

def test_centrehospitalier_has_numeroCentre():
    assert hasattr(CentreHospitalier, "numeroCentre")
    descriptor = None
    for klass in CentreHospitalier.__mro__:
        if "numeroCentre" in klass.__dict__:
            descriptor = klass.__dict__["numeroCentre"]
            break
    assert isinstance(descriptor, property)



def test_programme_is_not_abstract():
    assert not inspect.isabstract(Programme)


def test_programme_constructor_exists():
    assert callable(Programme.__init__)


def test_programme_constructor_args():
    sig = inspect.signature(Programme.__init__)
    params = list(sig.parameters.keys())
    assert "numeroProgramme" in params, "Missing parameter 'numeroProgramme'"
    assert "date" in params, "Missing parameter 'date'"
    assert "heure" in params, "Missing parameter 'heure'"

def test_programme_has_numeroProgramme():
    assert hasattr(Programme, "numeroProgramme")
    descriptor = None
    for klass in Programme.__mro__:
        if "numeroProgramme" in klass.__dict__:
            descriptor = klass.__dict__["numeroProgramme"]
            break
    assert isinstance(descriptor, property)

def test_programme_has_date():
    assert hasattr(Programme, "date")
    descriptor = None
    for klass in Programme.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_programme_has_heure():
    assert hasattr(Programme, "heure")
    descriptor = None
    for klass in Programme.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())
    assert "nomService" in params, "Missing parameter 'nomService'"
    assert "numeroService" in params, "Missing parameter 'numeroService'"
    assert "descriptionService" in params, "Missing parameter 'descriptionService'"

def test_service_has_nomService():
    assert hasattr(Service, "nomService")
    descriptor = None
    for klass in Service.__mro__:
        if "nomService" in klass.__dict__:
            descriptor = klass.__dict__["nomService"]
            break
    assert isinstance(descriptor, property)

def test_service_has_numeroService():
    assert hasattr(Service, "numeroService")
    descriptor = None
    for klass in Service.__mro__:
        if "numeroService" in klass.__dict__:
            descriptor = klass.__dict__["numeroService"]
            break
    assert isinstance(descriptor, property)

def test_service_has_descriptionService():
    assert hasattr(Service, "descriptionService")
    descriptor = None
    for klass in Service.__mro__:
        if "descriptionService" in klass.__dict__:
            descriptor = klass.__dict__["descriptionService"]
            break
    assert isinstance(descriptor, property)



def test_medecin_is_not_abstract():
    assert not inspect.isabstract(Medecin)


def test_medecin_constructor_exists():
    assert callable(Medecin.__init__)


def test_medecin_constructor_args():
    sig = inspect.signature(Medecin.__init__)
    params = list(sig.parameters.keys())
    assert "dateNaissance" in params, "Missing parameter 'dateNaissance'"
    assert "specialite" in params, "Missing parameter 'specialite'"
    assert "prenomMedecin" in params, "Missing parameter 'prenomMedecin'"
    assert "nomMedecin" in params, "Missing parameter 'nomMedecin'"

def test_medecin_has_dateNaissance():
    assert hasattr(Medecin, "dateNaissance")
    descriptor = None
    for klass in Medecin.__mro__:
        if "dateNaissance" in klass.__dict__:
            descriptor = klass.__dict__["dateNaissance"]
            break
    assert isinstance(descriptor, property)

def test_medecin_has_specialite():
    assert hasattr(Medecin, "specialite")
    descriptor = None
    for klass in Medecin.__mro__:
        if "specialite" in klass.__dict__:
            descriptor = klass.__dict__["specialite"]
            break
    assert isinstance(descriptor, property)

def test_medecin_has_prenomMedecin():
    assert hasattr(Medecin, "prenomMedecin")
    descriptor = None
    for klass in Medecin.__mro__:
        if "prenomMedecin" in klass.__dict__:
            descriptor = klass.__dict__["prenomMedecin"]
            break
    assert isinstance(descriptor, property)

def test_medecin_has_nomMedecin():
    assert hasattr(Medecin, "nomMedecin")
    descriptor = None
    for klass in Medecin.__mro__:
        if "nomMedecin" in klass.__dict__:
            descriptor = klass.__dict__["nomMedecin"]
            break
    assert isinstance(descriptor, property)



def test_examen_is_not_abstract():
    assert not inspect.isabstract(Examen)


def test_examen_constructor_exists():
    assert callable(Examen.__init__)


def test_examen_constructor_args():
    sig = inspect.signature(Examen.__init__)
    params = list(sig.parameters.keys())
    assert "numeroExamen" in params, "Missing parameter 'numeroExamen'"
    assert "dateProvisoir" in params, "Missing parameter 'dateProvisoir'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "motif" in params, "Missing parameter 'motif'"

def test_examen_has_numeroExamen():
    assert hasattr(Examen, "numeroExamen")
    descriptor = None
    for klass in Examen.__mro__:
        if "numeroExamen" in klass.__dict__:
            descriptor = klass.__dict__["numeroExamen"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_dateProvisoir():
    assert hasattr(Examen, "dateProvisoir")
    descriptor = None
    for klass in Examen.__mro__:
        if "dateProvisoir" in klass.__dict__:
            descriptor = klass.__dict__["dateProvisoir"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_heure():
    assert hasattr(Examen, "heure")
    descriptor = None
    for klass in Examen.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)

def test_examen_has_motif():
    assert hasattr(Examen, "motif")
    descriptor = None
    for klass in Examen.__mro__:
        if "motif" in klass.__dict__:
            descriptor = klass.__dict__["motif"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "prenomPatien" in params, "Missing parameter 'prenomPatien'"
    assert "agePatient" in params, "Missing parameter 'agePatient'"
    assert "lieuResidence" in params, "Missing parameter 'lieuResidence'"
    assert "profession" in params, "Missing parameter 'profession'"
    assert "nomPatient" in params, "Missing parameter 'nomPatient'"
    assert "numeroPatien" in params, "Missing parameter 'numeroPatien'"

def test_patient_has_prenomPatien():
    assert hasattr(Patient, "prenomPatien")
    descriptor = None
    for klass in Patient.__mro__:
        if "prenomPatien" in klass.__dict__:
            descriptor = klass.__dict__["prenomPatien"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_agePatient():
    assert hasattr(Patient, "agePatient")
    descriptor = None
    for klass in Patient.__mro__:
        if "agePatient" in klass.__dict__:
            descriptor = klass.__dict__["agePatient"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_lieuResidence():
    assert hasattr(Patient, "lieuResidence")
    descriptor = None
    for klass in Patient.__mro__:
        if "lieuResidence" in klass.__dict__:
            descriptor = klass.__dict__["lieuResidence"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_profession():
    assert hasattr(Patient, "profession")
    descriptor = None
    for klass in Patient.__mro__:
        if "profession" in klass.__dict__:
            descriptor = klass.__dict__["profession"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_nomPatient():
    assert hasattr(Patient, "nomPatient")
    descriptor = None
    for klass in Patient.__mro__:
        if "nomPatient" in klass.__dict__:
            descriptor = klass.__dict__["nomPatient"]
            break
    assert isinstance(descriptor, property)

def test_patient_has_numeroPatien():
    assert hasattr(Patient, "numeroPatien")
    descriptor = None
    for klass in Patient.__mro__:
        if "numeroPatien" in klass.__dict__:
            descriptor = klass.__dict__["numeroPatien"]
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
Rendez_vous_Medecin_Patient_external_strategy = st.builds(
    Rendez_vous_Medecin_Patient_external,
)
Rendez_vous_Laboratoire_Patient_external_strategy = st.builds(
    Rendez_vous_Laboratoire_Patient_external,
)
Produit_strategy = st.builds(
    Produit,
    nom=
        safe_text,
    id=
        st.integers(),
    posologie=
        safe_text,
    dose=
        safe_text
)
Ordonance_strategy = st.builds(
    Ordonance,
    date=
        safe_text,
    id=
        st.integers()
)
Rendez_vous_strategy = st.builds(
    Rendez_vous,
    id=
        st.integers(),
    date=
        safe_text,
    numero=
        safe_text
)
Contact_strategy = st.builds(
    Contact,
    id=
        st.integers(),
    telephone=
        st.integers(),
    mail=
        safe_text
)
Personne_strategy = st.builds(
    Personne,
    nom=
        safe_text,
    numero=
        safe_text,
    numeroMedecin=
        st.integers(),
    prenom=
        safe_text,
    id=
        st.integers(),
    attribute=
        safe_text
)
Laboratoire_strategy = st.builds(
    Laboratoire,
    id=
        st.integers(),
    nom=
        safe_text,
    numero=
        safe_text
)
ResultatExamen_strategy = st.builds(
    ResultatExamen,
    numeroResultat=
        st.integers(),
    infoResultat=
        safe_text
)
CentreHospitalier_strategy = st.builds(
    CentreHospitalier,
    nomCentre=
        safe_text,
    descriptionCentre=
        safe_text,
    numeroCentre=
        st.integers()
)
Programme_strategy = st.builds(
    Programme,
    numeroProgramme=
        safe_text,
    date=
        safe_text,
    heure=
        safe_text
)
Service_strategy = st.builds(
    Service,
    nomService=
        safe_text,
    numeroService=
        st.integers(),
    descriptionService=
        safe_text
)
Medecin_strategy = st.builds(
    Medecin,
    dateNaissance=
        safe_text,
    specialite=
        safe_text,
    prenomMedecin=
        safe_text,
    nomMedecin=
        safe_text
)
Examen_strategy = st.builds(
    Examen,
    numeroExamen=
        st.integers(),
    dateProvisoir=
        safe_text,
    heure=
        safe_text,
    motif=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    prenomPatien=
        safe_text,
    agePatient=
        st.integers(),
    lieuResidence=
        safe_text,
    profession=
        safe_text,
    nomPatient=
        safe_text,
    numeroPatien=
        st.integers()
)

@given(instance=Rendez_vous_Medecin_Patient_external_strategy)
@settings(max_examples=50)
def test_rendez_vous_medecin_patient_external_instantiation(instance):
    assert isinstance(instance, Rendez_vous_Medecin_Patient_external)

@given(instance=Rendez_vous_Laboratoire_Patient_external_strategy)
@settings(max_examples=50)
def test_rendez_vous_laboratoire_patient_external_instantiation(instance):
    assert isinstance(instance, Rendez_vous_Laboratoire_Patient_external)

@given(instance=Produit_strategy)
@settings(max_examples=50)
def test_produit_instantiation(instance):
    assert isinstance(instance, Produit)



@given(instance=Produit_strategy)
def test_produit_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Produit_strategy)
def test_produit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Produit_strategy)
def test_produit_posologie_setter(instance):
    original = instance.posologie
    instance.posologie = original
    assert instance.posologie == original



@given(instance=Produit_strategy)
def test_produit_dose_setter(instance):
    original = instance.dose
    instance.dose = original
    assert instance.dose == original

@given(instance=Ordonance_strategy)
@settings(max_examples=50)
def test_ordonance_instantiation(instance):
    assert isinstance(instance, Ordonance)



@given(instance=Ordonance_strategy)
def test_ordonance_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Ordonance_strategy)
def test_ordonance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Rendez_vous_strategy)
@settings(max_examples=50)
def test_rendez_vous_instantiation(instance):
    assert isinstance(instance, Rendez_vous)



@given(instance=Rendez_vous_strategy)
def test_rendez_vous_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Rendez_vous_strategy)
def test_rendez_vous_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Rendez_vous_strategy)
def test_rendez_vous_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original

@given(instance=Contact_strategy)
@settings(max_examples=50)
def test_contact_instantiation(instance):
    assert isinstance(instance, Contact)



@given(instance=Contact_strategy)
def test_contact_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Contact_strategy)
def test_contact_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Contact_strategy)
def test_contact_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original

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
def test_personne_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Personne_strategy)
def test_personne_numeroMedecin_setter(instance):
    original = instance.numeroMedecin
    instance.numeroMedecin = original
    assert instance.numeroMedecin == original



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
def test_personne_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Laboratoire_strategy)
@settings(max_examples=50)
def test_laboratoire_instantiation(instance):
    assert isinstance(instance, Laboratoire)



@given(instance=Laboratoire_strategy)
def test_laboratoire_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Laboratoire_strategy)
def test_laboratoire_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Laboratoire_strategy)
def test_laboratoire_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original

@given(instance=ResultatExamen_strategy)
@settings(max_examples=50)
def test_resultatexamen_instantiation(instance):
    assert isinstance(instance, ResultatExamen)



@given(instance=ResultatExamen_strategy)
def test_resultatexamen_numeroResultat_setter(instance):
    original = instance.numeroResultat
    instance.numeroResultat = original
    assert instance.numeroResultat == original



@given(instance=ResultatExamen_strategy)
def test_resultatexamen_infoResultat_setter(instance):
    original = instance.infoResultat
    instance.infoResultat = original
    assert instance.infoResultat == original

@given(instance=CentreHospitalier_strategy)
@settings(max_examples=50)
def test_centrehospitalier_instantiation(instance):
    assert isinstance(instance, CentreHospitalier)



@given(instance=CentreHospitalier_strategy)
def test_centrehospitalier_nomCentre_setter(instance):
    original = instance.nomCentre
    instance.nomCentre = original
    assert instance.nomCentre == original



@given(instance=CentreHospitalier_strategy)
def test_centrehospitalier_descriptionCentre_setter(instance):
    original = instance.descriptionCentre
    instance.descriptionCentre = original
    assert instance.descriptionCentre == original



@given(instance=CentreHospitalier_strategy)
def test_centrehospitalier_numeroCentre_setter(instance):
    original = instance.numeroCentre
    instance.numeroCentre = original
    assert instance.numeroCentre == original

@given(instance=Programme_strategy)
@settings(max_examples=50)
def test_programme_instantiation(instance):
    assert isinstance(instance, Programme)



@given(instance=Programme_strategy)
def test_programme_numeroProgramme_setter(instance):
    original = instance.numeroProgramme
    instance.numeroProgramme = original
    assert instance.numeroProgramme == original



@given(instance=Programme_strategy)
def test_programme_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Programme_strategy)
def test_programme_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)



@given(instance=Service_strategy)
def test_service_nomService_setter(instance):
    original = instance.nomService
    instance.nomService = original
    assert instance.nomService == original



@given(instance=Service_strategy)
def test_service_numeroService_setter(instance):
    original = instance.numeroService
    instance.numeroService = original
    assert instance.numeroService == original



@given(instance=Service_strategy)
def test_service_descriptionService_setter(instance):
    original = instance.descriptionService
    instance.descriptionService = original
    assert instance.descriptionService == original

@given(instance=Medecin_strategy)
@settings(max_examples=50)
def test_medecin_instantiation(instance):
    assert isinstance(instance, Medecin)



@given(instance=Medecin_strategy)
def test_medecin_dateNaissance_setter(instance):
    original = instance.dateNaissance
    instance.dateNaissance = original
    assert instance.dateNaissance == original



@given(instance=Medecin_strategy)
def test_medecin_specialite_setter(instance):
    original = instance.specialite
    instance.specialite = original
    assert instance.specialite == original



@given(instance=Medecin_strategy)
def test_medecin_prenomMedecin_setter(instance):
    original = instance.prenomMedecin
    instance.prenomMedecin = original
    assert instance.prenomMedecin == original



@given(instance=Medecin_strategy)
def test_medecin_nomMedecin_setter(instance):
    original = instance.nomMedecin
    instance.nomMedecin = original
    assert instance.nomMedecin == original

@given(instance=Examen_strategy)
@settings(max_examples=50)
def test_examen_instantiation(instance):
    assert isinstance(instance, Examen)



@given(instance=Examen_strategy)
def test_examen_numeroExamen_setter(instance):
    original = instance.numeroExamen
    instance.numeroExamen = original
    assert instance.numeroExamen == original



@given(instance=Examen_strategy)
def test_examen_dateProvisoir_setter(instance):
    original = instance.dateProvisoir
    instance.dateProvisoir = original
    assert instance.dateProvisoir == original



@given(instance=Examen_strategy)
def test_examen_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Examen_strategy)
def test_examen_motif_setter(instance):
    original = instance.motif
    instance.motif = original
    assert instance.motif == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_patient_prenomPatien_setter(instance):
    original = instance.prenomPatien
    instance.prenomPatien = original
    assert instance.prenomPatien == original



@given(instance=Patient_strategy)
def test_patient_agePatient_setter(instance):
    original = instance.agePatient
    instance.agePatient = original
    assert instance.agePatient == original



@given(instance=Patient_strategy)
def test_patient_lieuResidence_setter(instance):
    original = instance.lieuResidence
    instance.lieuResidence = original
    assert instance.lieuResidence == original



@given(instance=Patient_strategy)
def test_patient_profession_setter(instance):
    original = instance.profession
    instance.profession = original
    assert instance.profession == original



@given(instance=Patient_strategy)
def test_patient_nomPatient_setter(instance):
    original = instance.nomPatient
    instance.nomPatient = original
    assert instance.nomPatient == original



@given(instance=Patient_strategy)
def test_patient_numeroPatien_setter(instance):
    original = instance.numeroPatien
    instance.numeroPatien = original
    assert instance.numeroPatien == original

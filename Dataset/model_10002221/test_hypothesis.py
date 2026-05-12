import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Secretaire_external,
    ResultatExamen,
    CentreHospitalier,
    Programme,
    Service,
    Medecin,
    Examen,
    Consultion,
    Rendez_Vous,
    Patient,
    DossierPatient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_secretaire_external_is_not_abstract():
    assert not inspect.isabstract(Secretaire_external)


def test_secretaire_external_constructor_exists():
    assert callable(Secretaire_external.__init__)


def test_secretaire_external_constructor_args():
    sig = inspect.signature(Secretaire_external.__init__)
    params = list(sig.parameters.keys())



def test_resultatexamen_is_not_abstract():
    assert not inspect.isabstract(ResultatExamen)


def test_resultatexamen_constructor_exists():
    assert callable(ResultatExamen.__init__)


def test_resultatexamen_constructor_args():
    sig = inspect.signature(ResultatExamen.__init__)
    params = list(sig.parameters.keys())
    assert "infoResultat" in params, "Missing parameter 'infoResultat'"
    assert "numeroResultat" in params, "Missing parameter 'numeroResultat'"

def test_resultatexamen_has_infoResultat():
    assert hasattr(ResultatExamen, "infoResultat")
    descriptor = None
    for klass in ResultatExamen.__mro__:
        if "infoResultat" in klass.__dict__:
            descriptor = klass.__dict__["infoResultat"]
            break
    assert isinstance(descriptor, property)

def test_resultatexamen_has_numeroResultat():
    assert hasattr(ResultatExamen, "numeroResultat")
    descriptor = None
    for klass in ResultatExamen.__mro__:
        if "numeroResultat" in klass.__dict__:
            descriptor = klass.__dict__["numeroResultat"]
            break
    assert isinstance(descriptor, property)



def test_centrehospitalier_is_not_abstract():
    assert not inspect.isabstract(CentreHospitalier)


def test_centrehospitalier_constructor_exists():
    assert callable(CentreHospitalier.__init__)


def test_centrehospitalier_constructor_args():
    sig = inspect.signature(CentreHospitalier.__init__)
    params = list(sig.parameters.keys())
    assert "descriptionCentre" in params, "Missing parameter 'descriptionCentre'"
    assert "nomCentre" in params, "Missing parameter 'nomCentre'"
    assert "numeroCentre" in params, "Missing parameter 'numeroCentre'"

def test_centrehospitalier_has_descriptionCentre():
    assert hasattr(CentreHospitalier, "descriptionCentre")
    descriptor = None
    for klass in CentreHospitalier.__mro__:
        if "descriptionCentre" in klass.__dict__:
            descriptor = klass.__dict__["descriptionCentre"]
            break
    assert isinstance(descriptor, property)

def test_centrehospitalier_has_nomCentre():
    assert hasattr(CentreHospitalier, "nomCentre")
    descriptor = None
    for klass in CentreHospitalier.__mro__:
        if "nomCentre" in klass.__dict__:
            descriptor = klass.__dict__["nomCentre"]
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
    assert "heure" in params, "Missing parameter 'heure'"
    assert "date" in params, "Missing parameter 'date'"
    assert "numeroProgramme" in params, "Missing parameter 'numeroProgramme'"

def test_programme_has_heure():
    assert hasattr(Programme, "heure")
    descriptor = None
    for klass in Programme.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
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

def test_programme_has_numeroProgramme():
    assert hasattr(Programme, "numeroProgramme")
    descriptor = None
    for klass in Programme.__mro__:
        if "numeroProgramme" in klass.__dict__:
            descriptor = klass.__dict__["numeroProgramme"]
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
    assert "specialite" in params, "Missing parameter 'specialite'"
    assert "nomMedecin" in params, "Missing parameter 'nomMedecin'"
    assert "dateNaissance" in params, "Missing parameter 'dateNaissance'"
    assert "numeroMedecin" in params, "Missing parameter 'numeroMedecin'"
    assert "prenomMedecin" in params, "Missing parameter 'prenomMedecin'"

def test_medecin_has_specialite():
    assert hasattr(Medecin, "specialite")
    descriptor = None
    for klass in Medecin.__mro__:
        if "specialite" in klass.__dict__:
            descriptor = klass.__dict__["specialite"]
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

def test_medecin_has_dateNaissance():
    assert hasattr(Medecin, "dateNaissance")
    descriptor = None
    for klass in Medecin.__mro__:
        if "dateNaissance" in klass.__dict__:
            descriptor = klass.__dict__["dateNaissance"]
            break
    assert isinstance(descriptor, property)

def test_medecin_has_numeroMedecin():
    assert hasattr(Medecin, "numeroMedecin")
    descriptor = None
    for klass in Medecin.__mro__:
        if "numeroMedecin" in klass.__dict__:
            descriptor = klass.__dict__["numeroMedecin"]
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



def test_examen_is_not_abstract():
    assert not inspect.isabstract(Examen)


def test_examen_constructor_exists():
    assert callable(Examen.__init__)


def test_examen_constructor_args():
    sig = inspect.signature(Examen.__init__)
    params = list(sig.parameters.keys())
    assert "motif" in params, "Missing parameter 'motif'"
    assert "dateProvisoir" in params, "Missing parameter 'dateProvisoir'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "numeroExamen" in params, "Missing parameter 'numeroExamen'"

def test_examen_has_motif():
    assert hasattr(Examen, "motif")
    descriptor = None
    for klass in Examen.__mro__:
        if "motif" in klass.__dict__:
            descriptor = klass.__dict__["motif"]
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

def test_examen_has_numeroExamen():
    assert hasattr(Examen, "numeroExamen")
    descriptor = None
    for klass in Examen.__mro__:
        if "numeroExamen" in klass.__dict__:
            descriptor = klass.__dict__["numeroExamen"]
            break
    assert isinstance(descriptor, property)



def test_consultion_is_not_abstract():
    assert not inspect.isabstract(Consultion)


def test_consultion_constructor_exists():
    assert callable(Consultion.__init__)


def test_consultion_constructor_args():
    sig = inspect.signature(Consultion.__init__)
    params = list(sig.parameters.keys())
    assert "numeroConsultation" in params, "Missing parameter 'numeroConsultation'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "description" in params, "Missing parameter 'description'"
    assert "dateConsultation" in params, "Missing parameter 'dateConsultation'"

def test_consultion_has_numeroConsultation():
    assert hasattr(Consultion, "numeroConsultation")
    descriptor = None
    for klass in Consultion.__mro__:
        if "numeroConsultation" in klass.__dict__:
            descriptor = klass.__dict__["numeroConsultation"]
            break
    assert isinstance(descriptor, property)

def test_consultion_has_heure():
    assert hasattr(Consultion, "heure")
    descriptor = None
    for klass in Consultion.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)

def test_consultion_has_description():
    assert hasattr(Consultion, "description")
    descriptor = None
    for klass in Consultion.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_consultion_has_dateConsultation():
    assert hasattr(Consultion, "dateConsultation")
    descriptor = None
    for klass in Consultion.__mro__:
        if "dateConsultation" in klass.__dict__:
            descriptor = klass.__dict__["dateConsultation"]
            break
    assert isinstance(descriptor, property)



def test_rendez_vous_is_not_abstract():
    assert not inspect.isabstract(Rendez_Vous)


def test_rendez_vous_constructor_exists():
    assert callable(Rendez_Vous.__init__)


def test_rendez_vous_constructor_args():
    sig = inspect.signature(Rendez_Vous.__init__)
    params = list(sig.parameters.keys())
    assert "lieuRDV" in params, "Missing parameter 'lieuRDV'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "dateRDV" in params, "Missing parameter 'dateRDV'"
    assert "numeroRdV" in params, "Missing parameter 'numeroRdV'"

def test_rendez_vous_has_lieuRDV():
    assert hasattr(Rendez_Vous, "lieuRDV")
    descriptor = None
    for klass in Rendez_Vous.__mro__:
        if "lieuRDV" in klass.__dict__:
            descriptor = klass.__dict__["lieuRDV"]
            break
    assert isinstance(descriptor, property)

def test_rendez_vous_has_heure():
    assert hasattr(Rendez_Vous, "heure")
    descriptor = None
    for klass in Rendez_Vous.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)

def test_rendez_vous_has_dateRDV():
    assert hasattr(Rendez_Vous, "dateRDV")
    descriptor = None
    for klass in Rendez_Vous.__mro__:
        if "dateRDV" in klass.__dict__:
            descriptor = klass.__dict__["dateRDV"]
            break
    assert isinstance(descriptor, property)

def test_rendez_vous_has_numeroRdV():
    assert hasattr(Rendez_Vous, "numeroRdV")
    descriptor = None
    for klass in Rendez_Vous.__mro__:
        if "numeroRdV" in klass.__dict__:
            descriptor = klass.__dict__["numeroRdV"]
            break
    assert isinstance(descriptor, property)



def test_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "agePatient" in params, "Missing parameter 'agePatient'"
    assert "lieuResidence" in params, "Missing parameter 'lieuResidence'"
    assert "profession" in params, "Missing parameter 'profession'"
    assert "prenomPatien" in params, "Missing parameter 'prenomPatien'"
    assert "nomPatient" in params, "Missing parameter 'nomPatient'"
    assert "numeroPatien" in params, "Missing parameter 'numeroPatien'"

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

def test_patient_has_prenomPatien():
    assert hasattr(Patient, "prenomPatien")
    descriptor = None
    for klass in Patient.__mro__:
        if "prenomPatien" in klass.__dict__:
            descriptor = klass.__dict__["prenomPatien"]
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



def test_dossierpatient_is_not_abstract():
    assert not inspect.isabstract(DossierPatient)


def test_dossierpatient_constructor_exists():
    assert callable(DossierPatient.__init__)


def test_dossierpatient_constructor_args():
    sig = inspect.signature(DossierPatient.__init__)
    params = list(sig.parameters.keys())
    assert "dateCreation" in params, "Missing parameter 'dateCreation'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "numeroPatient" in params, "Missing parameter 'numeroPatient'"
    assert "nomDossier" in params, "Missing parameter 'nomDossier'"
    assert "infoAntecedant" in params, "Missing parameter 'infoAntecedant'"

def test_dossierpatient_has_dateCreation():
    assert hasattr(DossierPatient, "dateCreation")
    descriptor = None
    for klass in DossierPatient.__mro__:
        if "dateCreation" in klass.__dict__:
            descriptor = klass.__dict__["dateCreation"]
            break
    assert isinstance(descriptor, property)

def test_dossierpatient_has_heure():
    assert hasattr(DossierPatient, "heure")
    descriptor = None
    for klass in DossierPatient.__mro__:
        if "heure" in klass.__dict__:
            descriptor = klass.__dict__["heure"]
            break
    assert isinstance(descriptor, property)

def test_dossierpatient_has_numeroPatient():
    assert hasattr(DossierPatient, "numeroPatient")
    descriptor = None
    for klass in DossierPatient.__mro__:
        if "numeroPatient" in klass.__dict__:
            descriptor = klass.__dict__["numeroPatient"]
            break
    assert isinstance(descriptor, property)

def test_dossierpatient_has_nomDossier():
    assert hasattr(DossierPatient, "nomDossier")
    descriptor = None
    for klass in DossierPatient.__mro__:
        if "nomDossier" in klass.__dict__:
            descriptor = klass.__dict__["nomDossier"]
            break
    assert isinstance(descriptor, property)

def test_dossierpatient_has_infoAntecedant():
    assert hasattr(DossierPatient, "infoAntecedant")
    descriptor = None
    for klass in DossierPatient.__mro__:
        if "infoAntecedant" in klass.__dict__:
            descriptor = klass.__dict__["infoAntecedant"]
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
Secretaire_external_strategy = st.builds(
    Secretaire_external,
)
ResultatExamen_strategy = st.builds(
    ResultatExamen,
    infoResultat=
        safe_text,
    numeroResultat=
        st.integers()
)
CentreHospitalier_strategy = st.builds(
    CentreHospitalier,
    descriptionCentre=
        safe_text,
    nomCentre=
        safe_text,
    numeroCentre=
        st.integers()
)
Programme_strategy = st.builds(
    Programme,
    heure=
        safe_text,
    date=
        safe_text,
    numeroProgramme=
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
    specialite=
        safe_text,
    nomMedecin=
        safe_text,
    dateNaissance=
        safe_text,
    numeroMedecin=
        st.integers(),
    prenomMedecin=
        safe_text
)
Examen_strategy = st.builds(
    Examen,
    motif=
        safe_text,
    dateProvisoir=
        safe_text,
    heure=
        safe_text,
    numeroExamen=
        st.integers()
)
Consultion_strategy = st.builds(
    Consultion,
    numeroConsultation=
        st.integers(),
    heure=
        safe_text,
    description=
        safe_text,
    dateConsultation=
        safe_text
)
Rendez_Vous_strategy = st.builds(
    Rendez_Vous,
    lieuRDV=
        safe_text,
    heure=
        safe_text,
    dateRDV=
        safe_text,
    numeroRdV=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    agePatient=
        st.integers(),
    lieuResidence=
        safe_text,
    profession=
        safe_text,
    prenomPatien=
        safe_text,
    nomPatient=
        safe_text,
    numeroPatien=
        st.integers()
)
DossierPatient_strategy = st.builds(
    DossierPatient,
    dateCreation=
        st.integers(),
    heure=
        st.integers(),
    numeroPatient=
        st.integers(),
    nomDossier=
        safe_text,
    infoAntecedant=
        safe_text
)

@given(instance=Secretaire_external_strategy)
@settings(max_examples=50)
def test_secretaire_external_instantiation(instance):
    assert isinstance(instance, Secretaire_external)

@given(instance=ResultatExamen_strategy)
@settings(max_examples=50)
def test_resultatexamen_instantiation(instance):
    assert isinstance(instance, ResultatExamen)



@given(instance=ResultatExamen_strategy)
def test_resultatexamen_infoResultat_setter(instance):
    original = instance.infoResultat
    instance.infoResultat = original
    assert instance.infoResultat == original



@given(instance=ResultatExamen_strategy)
def test_resultatexamen_numeroResultat_setter(instance):
    original = instance.numeroResultat
    instance.numeroResultat = original
    assert instance.numeroResultat == original

@given(instance=CentreHospitalier_strategy)
@settings(max_examples=50)
def test_centrehospitalier_instantiation(instance):
    assert isinstance(instance, CentreHospitalier)



@given(instance=CentreHospitalier_strategy)
def test_centrehospitalier_descriptionCentre_setter(instance):
    original = instance.descriptionCentre
    instance.descriptionCentre = original
    assert instance.descriptionCentre == original



@given(instance=CentreHospitalier_strategy)
def test_centrehospitalier_nomCentre_setter(instance):
    original = instance.nomCentre
    instance.nomCentre = original
    assert instance.nomCentre == original



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
def test_programme_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Programme_strategy)
def test_programme_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Programme_strategy)
def test_programme_numeroProgramme_setter(instance):
    original = instance.numeroProgramme
    instance.numeroProgramme = original
    assert instance.numeroProgramme == original

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
def test_medecin_specialite_setter(instance):
    original = instance.specialite
    instance.specialite = original
    assert instance.specialite == original



@given(instance=Medecin_strategy)
def test_medecin_nomMedecin_setter(instance):
    original = instance.nomMedecin
    instance.nomMedecin = original
    assert instance.nomMedecin == original



@given(instance=Medecin_strategy)
def test_medecin_dateNaissance_setter(instance):
    original = instance.dateNaissance
    instance.dateNaissance = original
    assert instance.dateNaissance == original



@given(instance=Medecin_strategy)
def test_medecin_numeroMedecin_setter(instance):
    original = instance.numeroMedecin
    instance.numeroMedecin = original
    assert instance.numeroMedecin == original



@given(instance=Medecin_strategy)
def test_medecin_prenomMedecin_setter(instance):
    original = instance.prenomMedecin
    instance.prenomMedecin = original
    assert instance.prenomMedecin == original

@given(instance=Examen_strategy)
@settings(max_examples=50)
def test_examen_instantiation(instance):
    assert isinstance(instance, Examen)



@given(instance=Examen_strategy)
def test_examen_motif_setter(instance):
    original = instance.motif
    instance.motif = original
    assert instance.motif == original



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
def test_examen_numeroExamen_setter(instance):
    original = instance.numeroExamen
    instance.numeroExamen = original
    assert instance.numeroExamen == original

@given(instance=Consultion_strategy)
@settings(max_examples=50)
def test_consultion_instantiation(instance):
    assert isinstance(instance, Consultion)



@given(instance=Consultion_strategy)
def test_consultion_numeroConsultation_setter(instance):
    original = instance.numeroConsultation
    instance.numeroConsultation = original
    assert instance.numeroConsultation == original



@given(instance=Consultion_strategy)
def test_consultion_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Consultion_strategy)
def test_consultion_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Consultion_strategy)
def test_consultion_dateConsultation_setter(instance):
    original = instance.dateConsultation
    instance.dateConsultation = original
    assert instance.dateConsultation == original

@given(instance=Rendez_Vous_strategy)
@settings(max_examples=50)
def test_rendez_vous_instantiation(instance):
    assert isinstance(instance, Rendez_Vous)



@given(instance=Rendez_Vous_strategy)
def test_rendez_vous_lieuRDV_setter(instance):
    original = instance.lieuRDV
    instance.lieuRDV = original
    assert instance.lieuRDV == original



@given(instance=Rendez_Vous_strategy)
def test_rendez_vous_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Rendez_Vous_strategy)
def test_rendez_vous_dateRDV_setter(instance):
    original = instance.dateRDV
    instance.dateRDV = original
    assert instance.dateRDV == original



@given(instance=Rendez_Vous_strategy)
def test_rendez_vous_numeroRdV_setter(instance):
    original = instance.numeroRdV
    instance.numeroRdV = original
    assert instance.numeroRdV == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_patient_instantiation(instance):
    assert isinstance(instance, Patient)



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
def test_patient_prenomPatien_setter(instance):
    original = instance.prenomPatien
    instance.prenomPatien = original
    assert instance.prenomPatien == original



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

@given(instance=DossierPatient_strategy)
@settings(max_examples=50)
def test_dossierpatient_instantiation(instance):
    assert isinstance(instance, DossierPatient)



@given(instance=DossierPatient_strategy)
def test_dossierpatient_dateCreation_setter(instance):
    original = instance.dateCreation
    instance.dateCreation = original
    assert instance.dateCreation == original



@given(instance=DossierPatient_strategy)
def test_dossierpatient_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=DossierPatient_strategy)
def test_dossierpatient_numeroPatient_setter(instance):
    original = instance.numeroPatient
    instance.numeroPatient = original
    assert instance.numeroPatient == original



@given(instance=DossierPatient_strategy)
def test_dossierpatient_nomDossier_setter(instance):
    original = instance.nomDossier
    instance.nomDossier = original
    assert instance.nomDossier == original



@given(instance=DossierPatient_strategy)
def test_dossierpatient_infoAntecedant_setter(instance):
    original = instance.infoAntecedant
    instance.infoAntecedant = original
    assert instance.infoAntecedant == original

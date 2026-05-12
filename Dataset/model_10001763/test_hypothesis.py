import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    __table___T_Services,
    __table___T_CompteDeLUtilisateur,
    AffichageAccueil,
    RechercheAvancee,
    RechercheRapide,
    Contacter,
    AffichageDetailleResultat,
    SelectionnerUnResultat,
    AffichageResultats,
    CritereDeRecherche,
    DemandeDeService1,
    PropositionDeService1,
    CompteDeLUtilisateur1,
    Utilisateur1,
    RechercheDemandes,
    RecherchePropositions,
    DemandeDeService,
    PropositionDeService,
    CompteDeLUtilisateur,
    Utilisateur,
    Resultat,
    RechercheDAssociations,
    Systeme,
    Acteurs,
    Recherche_Rapide,
    Resultat_Recherche,
    Recherche_Avanc_e,
    Membre1,
    Service,
    Association,
    Membre,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test___table___t_services_is_not_abstract():
    assert not inspect.isabstract(__table___T_Services)


def test___table___t_services_constructor_exists():
    assert callable(__table___T_Services.__init__)


def test___table___t_services_constructor_args():
    sig = inspect.signature(__table___T_Services.__init__)
    params = list(sig.parameters.keys())
    assert "nbParticipants" in params, "Missing parameter 'nbParticipants'"
    assert "numeroUtilisateur" in params, "Missing parameter 'numeroUtilisateur'"
    assert "type" in params, "Missing parameter 'type'"
    assert "date" in params, "Missing parameter 'date'"
    assert "titre" in params, "Missing parameter 'titre'"
    assert "numeroService" in params, "Missing parameter 'numeroService'"
    assert "description" in params, "Missing parameter 'description'"

def test___table___t_services_has_nbParticipants():
    assert hasattr(__table___T_Services, "nbParticipants")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "nbParticipants" in klass.__dict__:
            descriptor = klass.__dict__["nbParticipants"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_numeroUtilisateur():
    assert hasattr(__table___T_Services, "numeroUtilisateur")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "numeroUtilisateur" in klass.__dict__:
            descriptor = klass.__dict__["numeroUtilisateur"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_type():
    assert hasattr(__table___T_Services, "type")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_date():
    assert hasattr(__table___T_Services, "date")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_titre():
    assert hasattr(__table___T_Services, "titre")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "titre" in klass.__dict__:
            descriptor = klass.__dict__["titre"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_numeroService():
    assert hasattr(__table___T_Services, "numeroService")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "numeroService" in klass.__dict__:
            descriptor = klass.__dict__["numeroService"]
            break
    assert isinstance(descriptor, property)

def test___table___t_services_has_description():
    assert hasattr(__table___T_Services, "description")
    descriptor = None
    for klass in __table___T_Services.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test___table___t_comptedelutilisateur_is_not_abstract():
    assert not inspect.isabstract(__table___T_CompteDeLUtilisateur)


def test___table___t_comptedelutilisateur_constructor_exists():
    assert callable(__table___T_CompteDeLUtilisateur.__init__)


def test___table___t_comptedelutilisateur_constructor_args():
    sig = inspect.signature(__table___T_CompteDeLUtilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "numeroUtilisateur" in params, "Missing parameter 'numeroUtilisateur'"
    assert "type" in params, "Missing parameter 'type'"
    assert "motDePasse" in params, "Missing parameter 'motDePasse'"
    assert "adresseMail" in params, "Missing parameter 'adresseMail'"
    assert "pseudo" in params, "Missing parameter 'pseudo'"

def test___table___t_comptedelutilisateur_has_numeroUtilisateur():
    assert hasattr(__table___T_CompteDeLUtilisateur, "numeroUtilisateur")
    descriptor = None
    for klass in __table___T_CompteDeLUtilisateur.__mro__:
        if "numeroUtilisateur" in klass.__dict__:
            descriptor = klass.__dict__["numeroUtilisateur"]
            break
    assert isinstance(descriptor, property)

def test___table___t_comptedelutilisateur_has_type():
    assert hasattr(__table___T_CompteDeLUtilisateur, "type")
    descriptor = None
    for klass in __table___T_CompteDeLUtilisateur.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test___table___t_comptedelutilisateur_has_motDePasse():
    assert hasattr(__table___T_CompteDeLUtilisateur, "motDePasse")
    descriptor = None
    for klass in __table___T_CompteDeLUtilisateur.__mro__:
        if "motDePasse" in klass.__dict__:
            descriptor = klass.__dict__["motDePasse"]
            break
    assert isinstance(descriptor, property)

def test___table___t_comptedelutilisateur_has_adresseMail():
    assert hasattr(__table___T_CompteDeLUtilisateur, "adresseMail")
    descriptor = None
    for klass in __table___T_CompteDeLUtilisateur.__mro__:
        if "adresseMail" in klass.__dict__:
            descriptor = klass.__dict__["adresseMail"]
            break
    assert isinstance(descriptor, property)

def test___table___t_comptedelutilisateur_has_pseudo():
    assert hasattr(__table___T_CompteDeLUtilisateur, "pseudo")
    descriptor = None
    for klass in __table___T_CompteDeLUtilisateur.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)



def test_affichageaccueil_is_not_abstract():
    assert not inspect.isabstract(AffichageAccueil)


def test_affichageaccueil_constructor_exists():
    assert callable(AffichageAccueil.__init__)


def test_affichageaccueil_constructor_args():
    sig = inspect.signature(AffichageAccueil.__init__)
    params = list(sig.parameters.keys())



def test_rechercheavancee_is_not_abstract():
    assert not inspect.isabstract(RechercheAvancee)


def test_rechercheavancee_constructor_exists():
    assert callable(RechercheAvancee.__init__)


def test_rechercheavancee_constructor_args():
    sig = inspect.signature(RechercheAvancee.__init__)
    params = list(sig.parameters.keys())
    assert "GenreService" in params, "Missing parameter 'GenreService'"
    assert "Association" in params, "Missing parameter 'Association'"
    assert "NbParticipants" in params, "Missing parameter 'NbParticipants'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Titre" in params, "Missing parameter 'Titre'"

def test_rechercheavancee_has_GenreService():
    assert hasattr(RechercheAvancee, "GenreService")
    descriptor = None
    for klass in RechercheAvancee.__mro__:
        if "GenreService" in klass.__dict__:
            descriptor = klass.__dict__["GenreService"]
            break
    assert isinstance(descriptor, property)

def test_rechercheavancee_has_Association():
    assert hasattr(RechercheAvancee, "Association")
    descriptor = None
    for klass in RechercheAvancee.__mro__:
        if "Association" in klass.__dict__:
            descriptor = klass.__dict__["Association"]
            break
    assert isinstance(descriptor, property)

def test_rechercheavancee_has_NbParticipants():
    assert hasattr(RechercheAvancee, "NbParticipants")
    descriptor = None
    for klass in RechercheAvancee.__mro__:
        if "NbParticipants" in klass.__dict__:
            descriptor = klass.__dict__["NbParticipants"]
            break
    assert isinstance(descriptor, property)

def test_rechercheavancee_has_Date():
    assert hasattr(RechercheAvancee, "Date")
    descriptor = None
    for klass in RechercheAvancee.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_rechercheavancee_has_Titre():
    assert hasattr(RechercheAvancee, "Titre")
    descriptor = None
    for klass in RechercheAvancee.__mro__:
        if "Titre" in klass.__dict__:
            descriptor = klass.__dict__["Titre"]
            break
    assert isinstance(descriptor, property)



def test_rechercherapide_is_not_abstract():
    assert not inspect.isabstract(RechercheRapide)


def test_rechercherapide_constructor_exists():
    assert callable(RechercheRapide.__init__)


def test_rechercherapide_constructor_args():
    sig = inspect.signature(RechercheRapide.__init__)
    params = list(sig.parameters.keys())
    assert "MotsCles" in params, "Missing parameter 'MotsCles'"

def test_rechercherapide_has_MotsCles():
    assert hasattr(RechercheRapide, "MotsCles")
    descriptor = None
    for klass in RechercheRapide.__mro__:
        if "MotsCles" in klass.__dict__:
            descriptor = klass.__dict__["MotsCles"]
            break
    assert isinstance(descriptor, property)



def test_contacter_is_not_abstract():
    assert not inspect.isabstract(Contacter)


def test_contacter_constructor_exists():
    assert callable(Contacter.__init__)


def test_contacter_constructor_args():
    sig = inspect.signature(Contacter.__init__)
    params = list(sig.parameters.keys())
    assert "personne" in params, "Missing parameter 'personne'"

def test_contacter_has_personne():
    assert hasattr(Contacter, "personne")
    descriptor = None
    for klass in Contacter.__mro__:
        if "personne" in klass.__dict__:
            descriptor = klass.__dict__["personne"]
            break
    assert isinstance(descriptor, property)



def test_affichagedetailleresultat_is_not_abstract():
    assert not inspect.isabstract(AffichageDetailleResultat)


def test_affichagedetailleresultat_constructor_exists():
    assert callable(AffichageDetailleResultat.__init__)


def test_affichagedetailleresultat_constructor_args():
    sig = inspect.signature(AffichageDetailleResultat.__init__)
    params = list(sig.parameters.keys())



def test_selectionnerunresultat_is_not_abstract():
    assert not inspect.isabstract(SelectionnerUnResultat)


def test_selectionnerunresultat_constructor_exists():
    assert callable(SelectionnerUnResultat.__init__)


def test_selectionnerunresultat_constructor_args():
    sig = inspect.signature(SelectionnerUnResultat.__init__)
    params = list(sig.parameters.keys())



def test_affichageresultats_is_not_abstract():
    assert not inspect.isabstract(AffichageResultats)


def test_affichageresultats_constructor_exists():
    assert callable(AffichageResultats.__init__)


def test_affichageresultats_constructor_args():
    sig = inspect.signature(AffichageResultats.__init__)
    params = list(sig.parameters.keys())



def test_criterederecherche_is_not_abstract():
    assert not inspect.isabstract(CritereDeRecherche)


def test_criterederecherche_constructor_exists():
    assert callable(CritereDeRecherche.__init__)


def test_criterederecherche_constructor_args():
    sig = inspect.signature(CritereDeRecherche.__init__)
    params = list(sig.parameters.keys())
    assert "critere" in params, "Missing parameter 'critere'"

def test_criterederecherche_has_critere():
    assert hasattr(CritereDeRecherche, "critere")
    descriptor = None
    for klass in CritereDeRecherche.__mro__:
        if "critere" in klass.__dict__:
            descriptor = klass.__dict__["critere"]
            break
    assert isinstance(descriptor, property)



def test_demandedeservice1_is_not_abstract():
    assert not inspect.isabstract(DemandeDeService1)


def test_demandedeservice1_constructor_exists():
    assert callable(DemandeDeService1.__init__)


def test_demandedeservice1_constructor_args():
    sig = inspect.signature(DemandeDeService1.__init__)
    params = list(sig.parameters.keys())



def test_propositiondeservice1_is_not_abstract():
    assert not inspect.isabstract(PropositionDeService1)


def test_propositiondeservice1_constructor_exists():
    assert callable(PropositionDeService1.__init__)


def test_propositiondeservice1_constructor_args():
    sig = inspect.signature(PropositionDeService1.__init__)
    params = list(sig.parameters.keys())



def test_comptedelutilisateur1_is_not_abstract():
    assert not inspect.isabstract(CompteDeLUtilisateur1)


def test_comptedelutilisateur1_constructor_exists():
    assert callable(CompteDeLUtilisateur1.__init__)


def test_comptedelutilisateur1_constructor_args():
    sig = inspect.signature(CompteDeLUtilisateur1.__init__)
    params = list(sig.parameters.keys())
    assert "motDePasse" in params, "Missing parameter 'motDePasse'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "peudo" in params, "Missing parameter 'peudo'"
    assert "adresseMail" in params, "Missing parameter 'adresseMail'"

def test_comptedelutilisateur1_has_motDePasse():
    assert hasattr(CompteDeLUtilisateur1, "motDePasse")
    descriptor = None
    for klass in CompteDeLUtilisateur1.__mro__:
        if "motDePasse" in klass.__dict__:
            descriptor = klass.__dict__["motDePasse"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur1_has_Type():
    assert hasattr(CompteDeLUtilisateur1, "Type")
    descriptor = None
    for klass in CompteDeLUtilisateur1.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur1_has_peudo():
    assert hasattr(CompteDeLUtilisateur1, "peudo")
    descriptor = None
    for klass in CompteDeLUtilisateur1.__mro__:
        if "peudo" in klass.__dict__:
            descriptor = klass.__dict__["peudo"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur1_has_adresseMail():
    assert hasattr(CompteDeLUtilisateur1, "adresseMail")
    descriptor = None
    for klass in CompteDeLUtilisateur1.__mro__:
        if "adresseMail" in klass.__dict__:
            descriptor = klass.__dict__["adresseMail"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur1_is_not_abstract():
    assert not inspect.isabstract(Utilisateur1)


def test_utilisateur1_constructor_exists():
    assert callable(Utilisateur1.__init__)


def test_utilisateur1_constructor_args():
    sig = inspect.signature(Utilisateur1.__init__)
    params = list(sig.parameters.keys())



def test_recherchedemandes_is_not_abstract():
    assert not inspect.isabstract(RechercheDemandes)


def test_recherchedemandes_constructor_exists():
    assert callable(RechercheDemandes.__init__)


def test_recherchedemandes_constructor_args():
    sig = inspect.signature(RechercheDemandes.__init__)
    params = list(sig.parameters.keys())
    assert "criteres" in params, "Missing parameter 'criteres'"

def test_recherchedemandes_has_criteres():
    assert hasattr(RechercheDemandes, "criteres")
    descriptor = None
    for klass in RechercheDemandes.__mro__:
        if "criteres" in klass.__dict__:
            descriptor = klass.__dict__["criteres"]
            break
    assert isinstance(descriptor, property)



def test_recherchepropositions_is_not_abstract():
    assert not inspect.isabstract(RecherchePropositions)


def test_recherchepropositions_constructor_exists():
    assert callable(RecherchePropositions.__init__)


def test_recherchepropositions_constructor_args():
    sig = inspect.signature(RecherchePropositions.__init__)
    params = list(sig.parameters.keys())
    assert "criteres" in params, "Missing parameter 'criteres'"

def test_recherchepropositions_has_criteres():
    assert hasattr(RecherchePropositions, "criteres")
    descriptor = None
    for klass in RecherchePropositions.__mro__:
        if "criteres" in klass.__dict__:
            descriptor = klass.__dict__["criteres"]
            break
    assert isinstance(descriptor, property)



def test_demandedeservice_is_not_abstract():
    assert not inspect.isabstract(DemandeDeService)


def test_demandedeservice_constructor_exists():
    assert callable(DemandeDeService.__init__)


def test_demandedeservice_constructor_args():
    sig = inspect.signature(DemandeDeService.__init__)
    params = list(sig.parameters.keys())



def test_propositiondeservice_is_not_abstract():
    assert not inspect.isabstract(PropositionDeService)


def test_propositiondeservice_constructor_exists():
    assert callable(PropositionDeService.__init__)


def test_propositiondeservice_constructor_args():
    sig = inspect.signature(PropositionDeService.__init__)
    params = list(sig.parameters.keys())



def test_comptedelutilisateur_is_not_abstract():
    assert not inspect.isabstract(CompteDeLUtilisateur)


def test_comptedelutilisateur_constructor_exists():
    assert callable(CompteDeLUtilisateur.__init__)


def test_comptedelutilisateur_constructor_args():
    sig = inspect.signature(CompteDeLUtilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "adresseMail" in params, "Missing parameter 'adresseMail'"
    assert "peudo" in params, "Missing parameter 'peudo'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "motDePasse" in params, "Missing parameter 'motDePasse'"

def test_comptedelutilisateur_has_adresseMail():
    assert hasattr(CompteDeLUtilisateur, "adresseMail")
    descriptor = None
    for klass in CompteDeLUtilisateur.__mro__:
        if "adresseMail" in klass.__dict__:
            descriptor = klass.__dict__["adresseMail"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur_has_peudo():
    assert hasattr(CompteDeLUtilisateur, "peudo")
    descriptor = None
    for klass in CompteDeLUtilisateur.__mro__:
        if "peudo" in klass.__dict__:
            descriptor = klass.__dict__["peudo"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur_has_Type():
    assert hasattr(CompteDeLUtilisateur, "Type")
    descriptor = None
    for klass in CompteDeLUtilisateur.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_comptedelutilisateur_has_motDePasse():
    assert hasattr(CompteDeLUtilisateur, "motDePasse")
    descriptor = None
    for klass in CompteDeLUtilisateur.__mro__:
        if "motDePasse" in klass.__dict__:
            descriptor = klass.__dict__["motDePasse"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())



def test_resultat_is_not_abstract():
    assert not inspect.isabstract(Resultat)


def test_resultat_constructor_exists():
    assert callable(Resultat.__init__)


def test_resultat_constructor_args():
    sig = inspect.signature(Resultat.__init__)
    params = list(sig.parameters.keys())
    assert "Liste" in params, "Missing parameter 'Liste'"

def test_resultat_has_Liste():
    assert hasattr(Resultat, "Liste")
    descriptor = None
    for klass in Resultat.__mro__:
        if "Liste" in klass.__dict__:
            descriptor = klass.__dict__["Liste"]
            break
    assert isinstance(descriptor, property)



def test_recherchedassociations_is_not_abstract():
    assert not inspect.isabstract(RechercheDAssociations)


def test_recherchedassociations_constructor_exists():
    assert callable(RechercheDAssociations.__init__)


def test_recherchedassociations_constructor_args():
    sig = inspect.signature(RechercheDAssociations.__init__)
    params = list(sig.parameters.keys())
    assert "criteres" in params, "Missing parameter 'criteres'"

def test_recherchedassociations_has_criteres():
    assert hasattr(RechercheDAssociations, "criteres")
    descriptor = None
    for klass in RechercheDAssociations.__mro__:
        if "criteres" in klass.__dict__:
            descriptor = klass.__dict__["criteres"]
            break
    assert isinstance(descriptor, property)



def test_systeme_is_not_abstract():
    assert not inspect.isabstract(Systeme)


def test_systeme_constructor_exists():
    assert callable(Systeme.__init__)


def test_systeme_constructor_args():
    sig = inspect.signature(Systeme.__init__)
    params = list(sig.parameters.keys())



def test_acteurs_is_not_abstract():
    assert not inspect.isabstract(Acteurs)


def test_acteurs_constructor_exists():
    assert callable(Acteurs.__init__)


def test_acteurs_constructor_args():
    sig = inspect.signature(Acteurs.__init__)
    params = list(sig.parameters.keys())



def test_recherche_rapide_is_not_abstract():
    assert not inspect.isabstract(Recherche_Rapide)


def test_recherche_rapide_constructor_exists():
    assert callable(Recherche_Rapide.__init__)


def test_recherche_rapide_constructor_args():
    sig = inspect.signature(Recherche_Rapide.__init__)
    params = list(sig.parameters.keys())
    assert "MotsCles" in params, "Missing parameter 'MotsCles'"

def test_recherche_rapide_has_MotsCles():
    assert hasattr(Recherche_Rapide, "MotsCles")
    descriptor = None
    for klass in Recherche_Rapide.__mro__:
        if "MotsCles" in klass.__dict__:
            descriptor = klass.__dict__["MotsCles"]
            break
    assert isinstance(descriptor, property)



def test_resultat_recherche_is_not_abstract():
    assert not inspect.isabstract(Resultat_Recherche)


def test_resultat_recherche_constructor_exists():
    assert callable(Resultat_Recherche.__init__)


def test_resultat_recherche_constructor_args():
    sig = inspect.signature(Resultat_Recherche.__init__)
    params = list(sig.parameters.keys())



def test_recherche_avanc_e_is_not_abstract():
    assert not inspect.isabstract(Recherche_Avanc_e)


def test_recherche_avanc_e_constructor_exists():
    assert callable(Recherche_Avanc_e.__init__)


def test_recherche_avanc_e_constructor_args():
    sig = inspect.signature(Recherche_Avanc_e.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Pays" in params, "Missing parameter 'Pays'"
    assert "NbParticipants" in params, "Missing parameter 'NbParticipants'"
    assert "Association" in params, "Missing parameter 'Association'"
    assert "Titre" in params, "Missing parameter 'Titre'"

def test_recherche_avanc_e_has_Date():
    assert hasattr(Recherche_Avanc_e, "Date")
    descriptor = None
    for klass in Recherche_Avanc_e.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_recherche_avanc_e_has_Pays():
    assert hasattr(Recherche_Avanc_e, "Pays")
    descriptor = None
    for klass in Recherche_Avanc_e.__mro__:
        if "Pays" in klass.__dict__:
            descriptor = klass.__dict__["Pays"]
            break
    assert isinstance(descriptor, property)

def test_recherche_avanc_e_has_NbParticipants():
    assert hasattr(Recherche_Avanc_e, "NbParticipants")
    descriptor = None
    for klass in Recherche_Avanc_e.__mro__:
        if "NbParticipants" in klass.__dict__:
            descriptor = klass.__dict__["NbParticipants"]
            break
    assert isinstance(descriptor, property)

def test_recherche_avanc_e_has_Association():
    assert hasattr(Recherche_Avanc_e, "Association")
    descriptor = None
    for klass in Recherche_Avanc_e.__mro__:
        if "Association" in klass.__dict__:
            descriptor = klass.__dict__["Association"]
            break
    assert isinstance(descriptor, property)

def test_recherche_avanc_e_has_Titre():
    assert hasattr(Recherche_Avanc_e, "Titre")
    descriptor = None
    for klass in Recherche_Avanc_e.__mro__:
        if "Titre" in klass.__dict__:
            descriptor = klass.__dict__["Titre"]
            break
    assert isinstance(descriptor, property)



def test_membre1_is_not_abstract():
    assert not inspect.isabstract(Membre1)


def test_membre1_constructor_exists():
    assert callable(Membre1.__init__)


def test_membre1_constructor_args():
    sig = inspect.signature(Membre1.__init__)
    params = list(sig.parameters.keys())



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_service_has_description():
    assert hasattr(Service, "description")
    descriptor = None
    for klass in Service.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())
    assert "nom___unicef" in params, "Missing parameter 'nom___unicef'"

def test_association_has_nom___unicef():
    assert hasattr(Association, "nom___unicef")
    descriptor = None
    for klass in Association.__mro__:
        if "nom___unicef" in klass.__dict__:
            descriptor = klass.__dict__["nom___unicef"]
            break
    assert isinstance(descriptor, property)



def test_membre_is_not_abstract():
    assert not inspect.isabstract(Membre)


def test_membre_constructor_exists():
    assert callable(Membre.__init__)


def test_membre_constructor_args():
    sig = inspect.signature(Membre.__init__)
    params = list(sig.parameters.keys())
    assert "nom___salim_talout" in params, "Missing parameter 'nom___salim_talout'"

def test_membre_has_nom___salim_talout():
    assert hasattr(Membre, "nom___salim_talout")
    descriptor = None
    for klass in Membre.__mro__:
        if "nom___salim_talout" in klass.__dict__:
            descriptor = klass.__dict__["nom___salim_talout"]
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
__table___T_Services_strategy = st.builds(
    __table___T_Services,
    nbParticipants=
        st.integers(),
    numeroUtilisateur=
        st.integers(),
    type=
        safe_text,
    date=
        st.dates(),
    titre=
        safe_text,
    numeroService=
        st.integers(),
    description=
        safe_text
)
__table___T_CompteDeLUtilisateur_strategy = st.builds(
    __table___T_CompteDeLUtilisateur,
    numeroUtilisateur=
        st.integers(),
    type=
        safe_text,
    motDePasse=
        safe_text,
    adresseMail=
        safe_text,
    pseudo=
        safe_text
)
AffichageAccueil_strategy = st.builds(
    AffichageAccueil,
)
RechercheAvancee_strategy = st.builds(
    RechercheAvancee,
    GenreService=
        st.none(),
    Association=
        st.none(),
    NbParticipants=
        st.integers(),
    Date=
        st.dates(),
    Titre=
        safe_text
)
RechercheRapide_strategy = st.builds(
    RechercheRapide,
    MotsCles=
        safe_text
)
Contacter_strategy = st.builds(
    Contacter,
    personne=
        st.none()
)
AffichageDetailleResultat_strategy = st.builds(
    AffichageDetailleResultat,
)
SelectionnerUnResultat_strategy = st.builds(
    SelectionnerUnResultat,
)
AffichageResultats_strategy = st.builds(
    AffichageResultats,
)
CritereDeRecherche_strategy = st.builds(
    CritereDeRecherche,
    critere=
        safe_text
)
DemandeDeService1_strategy = st.builds(
    DemandeDeService1,
)
PropositionDeService1_strategy = st.builds(
    PropositionDeService1,
)
CompteDeLUtilisateur1_strategy = st.builds(
    CompteDeLUtilisateur1,
    motDePasse=
        safe_text,
    Type=
        safe_text,
    peudo=
        safe_text,
    adresseMail=
        safe_text
)
Utilisateur1_strategy = st.builds(
    Utilisateur1,
)
RechercheDemandes_strategy = st.builds(
    RechercheDemandes,
    criteres=
        safe_text
)
RecherchePropositions_strategy = st.builds(
    RecherchePropositions,
    criteres=
        safe_text
)
DemandeDeService_strategy = st.builds(
    DemandeDeService,
)
PropositionDeService_strategy = st.builds(
    PropositionDeService,
)
CompteDeLUtilisateur_strategy = st.builds(
    CompteDeLUtilisateur,
    adresseMail=
        safe_text,
    peudo=
        safe_text,
    Type=
        safe_text,
    motDePasse=
        safe_text
)
Utilisateur_strategy = st.builds(
    Utilisateur,
)
Resultat_strategy = st.builds(
    Resultat,
    Liste=
        st.none()
)
RechercheDAssociations_strategy = st.builds(
    RechercheDAssociations,
    criteres=
        safe_text
)
Systeme_strategy = st.builds(
    Systeme,
)
Acteurs_strategy = st.builds(
    Acteurs,
)
Recherche_Rapide_strategy = st.builds(
    Recherche_Rapide,
    MotsCles=
        safe_text
)
Resultat_Recherche_strategy = st.builds(
    Resultat_Recherche,
)
Recherche_Avanc_e_strategy = st.builds(
    Recherche_Avanc_e,
    Date=
        st.dates(),
    Pays=
        safe_text,
    NbParticipants=
        st.integers(),
    Association=
        st.none(),
    Titre=
        safe_text
)
Membre1_strategy = st.builds(
    Membre1,
)
Service_strategy = st.builds(
    Service,
    description=
        safe_text
)
Association_strategy = st.builds(
    Association,
    nom___unicef=
        safe_text
)
Membre_strategy = st.builds(
    Membre,
    nom___salim_talout=
        safe_text
)

@given(instance=__table___T_Services_strategy)
@settings(max_examples=50)
def test___table___t_services_instantiation(instance):
    assert isinstance(instance, __table___T_Services)



@given(instance=__table___T_Services_strategy)
def test___table___t_services_nbParticipants_setter(instance):
    original = instance.nbParticipants
    instance.nbParticipants = original
    assert instance.nbParticipants == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_numeroUtilisateur_setter(instance):
    original = instance.numeroUtilisateur
    instance.numeroUtilisateur = original
    assert instance.numeroUtilisateur == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_titre_setter(instance):
    original = instance.titre
    instance.titre = original
    assert instance.titre == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_numeroService_setter(instance):
    original = instance.numeroService
    instance.numeroService = original
    assert instance.numeroService == original



@given(instance=__table___T_Services_strategy)
def test___table___t_services_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=__table___T_CompteDeLUtilisateur_strategy)
@settings(max_examples=50)
def test___table___t_comptedelutilisateur_instantiation(instance):
    assert isinstance(instance, __table___T_CompteDeLUtilisateur)



@given(instance=__table___T_CompteDeLUtilisateur_strategy)
def test___table___t_comptedelutilisateur_numeroUtilisateur_setter(instance):
    original = instance.numeroUtilisateur
    instance.numeroUtilisateur = original
    assert instance.numeroUtilisateur == original



@given(instance=__table___T_CompteDeLUtilisateur_strategy)
def test___table___t_comptedelutilisateur_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=__table___T_CompteDeLUtilisateur_strategy)
def test___table___t_comptedelutilisateur_motDePasse_setter(instance):
    original = instance.motDePasse
    instance.motDePasse = original
    assert instance.motDePasse == original



@given(instance=__table___T_CompteDeLUtilisateur_strategy)
def test___table___t_comptedelutilisateur_adresseMail_setter(instance):
    original = instance.adresseMail
    instance.adresseMail = original
    assert instance.adresseMail == original



@given(instance=__table___T_CompteDeLUtilisateur_strategy)
def test___table___t_comptedelutilisateur_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original

@given(instance=AffichageAccueil_strategy)
@settings(max_examples=50)
def test_affichageaccueil_instantiation(instance):
    assert isinstance(instance, AffichageAccueil)

@given(instance=RechercheAvancee_strategy)
@settings(max_examples=50)
def test_rechercheavancee_instantiation(instance):
    assert isinstance(instance, RechercheAvancee)



@given(instance=RechercheAvancee_strategy)
def test_rechercheavancee_GenreService_setter(instance):
    original = instance.GenreService
    instance.GenreService = original
    assert instance.GenreService == original



@given(instance=RechercheAvancee_strategy)
def test_rechercheavancee_Association_setter(instance):
    original = instance.Association
    instance.Association = original
    assert instance.Association == original



@given(instance=RechercheAvancee_strategy)
def test_rechercheavancee_NbParticipants_setter(instance):
    original = instance.NbParticipants
    instance.NbParticipants = original
    assert instance.NbParticipants == original



@given(instance=RechercheAvancee_strategy)
def test_rechercheavancee_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=RechercheAvancee_strategy)
def test_rechercheavancee_Titre_setter(instance):
    original = instance.Titre
    instance.Titre = original
    assert instance.Titre == original

@given(instance=RechercheRapide_strategy)
@settings(max_examples=50)
def test_rechercherapide_instantiation(instance):
    assert isinstance(instance, RechercheRapide)



@given(instance=RechercheRapide_strategy)
def test_rechercherapide_MotsCles_setter(instance):
    original = instance.MotsCles
    instance.MotsCles = original
    assert instance.MotsCles == original

@given(instance=Contacter_strategy)
@settings(max_examples=50)
def test_contacter_instantiation(instance):
    assert isinstance(instance, Contacter)



@given(instance=Contacter_strategy)
def test_contacter_personne_setter(instance):
    original = instance.personne
    instance.personne = original
    assert instance.personne == original

@given(instance=AffichageDetailleResultat_strategy)
@settings(max_examples=50)
def test_affichagedetailleresultat_instantiation(instance):
    assert isinstance(instance, AffichageDetailleResultat)

@given(instance=SelectionnerUnResultat_strategy)
@settings(max_examples=50)
def test_selectionnerunresultat_instantiation(instance):
    assert isinstance(instance, SelectionnerUnResultat)

@given(instance=AffichageResultats_strategy)
@settings(max_examples=50)
def test_affichageresultats_instantiation(instance):
    assert isinstance(instance, AffichageResultats)

@given(instance=CritereDeRecherche_strategy)
@settings(max_examples=50)
def test_criterederecherche_instantiation(instance):
    assert isinstance(instance, CritereDeRecherche)



@given(instance=CritereDeRecherche_strategy)
def test_criterederecherche_critere_setter(instance):
    original = instance.critere
    instance.critere = original
    assert instance.critere == original

@given(instance=DemandeDeService1_strategy)
@settings(max_examples=50)
def test_demandedeservice1_instantiation(instance):
    assert isinstance(instance, DemandeDeService1)

@given(instance=PropositionDeService1_strategy)
@settings(max_examples=50)
def test_propositiondeservice1_instantiation(instance):
    assert isinstance(instance, PropositionDeService1)

@given(instance=CompteDeLUtilisateur1_strategy)
@settings(max_examples=50)
def test_comptedelutilisateur1_instantiation(instance):
    assert isinstance(instance, CompteDeLUtilisateur1)



@given(instance=CompteDeLUtilisateur1_strategy)
def test_comptedelutilisateur1_motDePasse_setter(instance):
    original = instance.motDePasse
    instance.motDePasse = original
    assert instance.motDePasse == original



@given(instance=CompteDeLUtilisateur1_strategy)
def test_comptedelutilisateur1_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=CompteDeLUtilisateur1_strategy)
def test_comptedelutilisateur1_peudo_setter(instance):
    original = instance.peudo
    instance.peudo = original
    assert instance.peudo == original



@given(instance=CompteDeLUtilisateur1_strategy)
def test_comptedelutilisateur1_adresseMail_setter(instance):
    original = instance.adresseMail
    instance.adresseMail = original
    assert instance.adresseMail == original

@given(instance=Utilisateur1_strategy)
@settings(max_examples=50)
def test_utilisateur1_instantiation(instance):
    assert isinstance(instance, Utilisateur1)

@given(instance=RechercheDemandes_strategy)
@settings(max_examples=50)
def test_recherchedemandes_instantiation(instance):
    assert isinstance(instance, RechercheDemandes)



@given(instance=RechercheDemandes_strategy)
def test_recherchedemandes_criteres_setter(instance):
    original = instance.criteres
    instance.criteres = original
    assert instance.criteres == original

@given(instance=RecherchePropositions_strategy)
@settings(max_examples=50)
def test_recherchepropositions_instantiation(instance):
    assert isinstance(instance, RecherchePropositions)



@given(instance=RecherchePropositions_strategy)
def test_recherchepropositions_criteres_setter(instance):
    original = instance.criteres
    instance.criteres = original
    assert instance.criteres == original

@given(instance=DemandeDeService_strategy)
@settings(max_examples=50)
def test_demandedeservice_instantiation(instance):
    assert isinstance(instance, DemandeDeService)

@given(instance=PropositionDeService_strategy)
@settings(max_examples=50)
def test_propositiondeservice_instantiation(instance):
    assert isinstance(instance, PropositionDeService)

@given(instance=CompteDeLUtilisateur_strategy)
@settings(max_examples=50)
def test_comptedelutilisateur_instantiation(instance):
    assert isinstance(instance, CompteDeLUtilisateur)



@given(instance=CompteDeLUtilisateur_strategy)
def test_comptedelutilisateur_adresseMail_setter(instance):
    original = instance.adresseMail
    instance.adresseMail = original
    assert instance.adresseMail == original



@given(instance=CompteDeLUtilisateur_strategy)
def test_comptedelutilisateur_peudo_setter(instance):
    original = instance.peudo
    instance.peudo = original
    assert instance.peudo == original



@given(instance=CompteDeLUtilisateur_strategy)
def test_comptedelutilisateur_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=CompteDeLUtilisateur_strategy)
def test_comptedelutilisateur_motDePasse_setter(instance):
    original = instance.motDePasse
    instance.motDePasse = original
    assert instance.motDePasse == original

@given(instance=Utilisateur_strategy)
@settings(max_examples=50)
def test_utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)

@given(instance=Resultat_strategy)
@settings(max_examples=50)
def test_resultat_instantiation(instance):
    assert isinstance(instance, Resultat)



@given(instance=Resultat_strategy)
def test_resultat_Liste_setter(instance):
    original = instance.Liste
    instance.Liste = original
    assert instance.Liste == original

@given(instance=RechercheDAssociations_strategy)
@settings(max_examples=50)
def test_recherchedassociations_instantiation(instance):
    assert isinstance(instance, RechercheDAssociations)



@given(instance=RechercheDAssociations_strategy)
def test_recherchedassociations_criteres_setter(instance):
    original = instance.criteres
    instance.criteres = original
    assert instance.criteres == original

@given(instance=Systeme_strategy)
@settings(max_examples=50)
def test_systeme_instantiation(instance):
    assert isinstance(instance, Systeme)

@given(instance=Acteurs_strategy)
@settings(max_examples=50)
def test_acteurs_instantiation(instance):
    assert isinstance(instance, Acteurs)

@given(instance=Recherche_Rapide_strategy)
@settings(max_examples=50)
def test_recherche_rapide_instantiation(instance):
    assert isinstance(instance, Recherche_Rapide)



@given(instance=Recherche_Rapide_strategy)
def test_recherche_rapide_MotsCles_setter(instance):
    original = instance.MotsCles
    instance.MotsCles = original
    assert instance.MotsCles == original

@given(instance=Resultat_Recherche_strategy)
@settings(max_examples=50)
def test_resultat_recherche_instantiation(instance):
    assert isinstance(instance, Resultat_Recherche)

@given(instance=Recherche_Avanc_e_strategy)
@settings(max_examples=50)
def test_recherche_avanc_e_instantiation(instance):
    assert isinstance(instance, Recherche_Avanc_e)



@given(instance=Recherche_Avanc_e_strategy)
def test_recherche_avanc_e_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Recherche_Avanc_e_strategy)
def test_recherche_avanc_e_Pays_setter(instance):
    original = instance.Pays
    instance.Pays = original
    assert instance.Pays == original



@given(instance=Recherche_Avanc_e_strategy)
def test_recherche_avanc_e_NbParticipants_setter(instance):
    original = instance.NbParticipants
    instance.NbParticipants = original
    assert instance.NbParticipants == original



@given(instance=Recherche_Avanc_e_strategy)
def test_recherche_avanc_e_Association_setter(instance):
    original = instance.Association
    instance.Association = original
    assert instance.Association == original



@given(instance=Recherche_Avanc_e_strategy)
def test_recherche_avanc_e_Titre_setter(instance):
    original = instance.Titre
    instance.Titre = original
    assert instance.Titre == original

@given(instance=Membre1_strategy)
@settings(max_examples=50)
def test_membre1_instantiation(instance):
    assert isinstance(instance, Membre1)

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)



@given(instance=Service_strategy)
def test_service_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)



@given(instance=Association_strategy)
def test_association_nom___unicef_setter(instance):
    original = instance.nom___unicef
    instance.nom___unicef = original
    assert instance.nom___unicef == original

@given(instance=Membre_strategy)
@settings(max_examples=50)
def test_membre_instantiation(instance):
    assert isinstance(instance, Membre)



@given(instance=Membre_strategy)
def test_membre_nom___salim_talout_setter(instance):
    original = instance.nom___salim_talout
    instance.nom___salim_talout = original
    assert instance.nom___salim_talout == original

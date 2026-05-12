import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Effectue_un_paiement_UseCase,
    Valide_arriv__UseCase,
    Valide_embarquement_UseCase,
    confirme_voyage_UseCase,
    Reserve_voyage_UseCase,
    Administre_UseCase,
    Choisi_un_voyage_UseCase,
    S_authentifier_UseCase,
    Enregistre_son_vehicule_UseCase,
    Conducteur_Actor,
    Passager__Actor,
    S_enregistre_UseCase,
    Administrateur_Actor,
    Proposition_de_voyage_UseCase,
    Utilisateur_anonyme_Actor,
    Date_trajet,
    Utilisateur,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_effectue_un_paiement_usecase_is_not_abstract():
    assert not inspect.isabstract(Effectue_un_paiement_UseCase)


def test_effectue_un_paiement_usecase_constructor_exists():
    assert callable(Effectue_un_paiement_UseCase.__init__)


def test_effectue_un_paiement_usecase_constructor_args():
    sig = inspect.signature(Effectue_un_paiement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_valide_arriv__usecase_is_not_abstract():
    assert not inspect.isabstract(Valide_arriv__UseCase)


def test_valide_arriv__usecase_constructor_exists():
    assert callable(Valide_arriv__UseCase.__init__)


def test_valide_arriv__usecase_constructor_args():
    sig = inspect.signature(Valide_arriv__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_valide_embarquement_usecase_is_not_abstract():
    assert not inspect.isabstract(Valide_embarquement_UseCase)


def test_valide_embarquement_usecase_constructor_exists():
    assert callable(Valide_embarquement_UseCase.__init__)


def test_valide_embarquement_usecase_constructor_args():
    sig = inspect.signature(Valide_embarquement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_confirme_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(confirme_voyage_UseCase)


def test_confirme_voyage_usecase_constructor_exists():
    assert callable(confirme_voyage_UseCase.__init__)


def test_confirme_voyage_usecase_constructor_args():
    sig = inspect.signature(confirme_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reserve_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Reserve_voyage_UseCase)


def test_reserve_voyage_usecase_constructor_exists():
    assert callable(Reserve_voyage_UseCase.__init__)


def test_reserve_voyage_usecase_constructor_args():
    sig = inspect.signature(Reserve_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_administre_usecase_is_not_abstract():
    assert not inspect.isabstract(Administre_UseCase)


def test_administre_usecase_constructor_exists():
    assert callable(Administre_UseCase.__init__)


def test_administre_usecase_constructor_args():
    sig = inspect.signature(Administre_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_choisi_un_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Choisi_un_voyage_UseCase)


def test_choisi_un_voyage_usecase_constructor_exists():
    assert callable(Choisi_un_voyage_UseCase.__init__)


def test_choisi_un_voyage_usecase_constructor_args():
    sig = inspect.signature(Choisi_un_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_s_authentifier_usecase_is_not_abstract():
    assert not inspect.isabstract(S_authentifier_UseCase)


def test_s_authentifier_usecase_constructor_exists():
    assert callable(S_authentifier_UseCase.__init__)


def test_s_authentifier_usecase_constructor_args():
    sig = inspect.signature(S_authentifier_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_enregistre_son_vehicule_usecase_is_not_abstract():
    assert not inspect.isabstract(Enregistre_son_vehicule_UseCase)


def test_enregistre_son_vehicule_usecase_constructor_exists():
    assert callable(Enregistre_son_vehicule_UseCase.__init__)


def test_enregistre_son_vehicule_usecase_constructor_args():
    sig = inspect.signature(Enregistre_son_vehicule_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_conducteur_actor_is_not_abstract():
    assert not inspect.isabstract(Conducteur_Actor)


def test_conducteur_actor_constructor_exists():
    assert callable(Conducteur_Actor.__init__)


def test_conducteur_actor_constructor_args():
    sig = inspect.signature(Conducteur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_passager__actor_is_not_abstract():
    assert not inspect.isabstract(Passager__Actor)


def test_passager__actor_constructor_exists():
    assert callable(Passager__Actor.__init__)


def test_passager__actor_constructor_args():
    sig = inspect.signature(Passager__Actor.__init__)
    params = list(sig.parameters.keys())



def test_s_enregistre_usecase_is_not_abstract():
    assert not inspect.isabstract(S_enregistre_UseCase)


def test_s_enregistre_usecase_constructor_exists():
    assert callable(S_enregistre_UseCase.__init__)


def test_s_enregistre_usecase_constructor_args():
    sig = inspect.signature(S_enregistre_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_administrateur_actor_is_not_abstract():
    assert not inspect.isabstract(Administrateur_Actor)


def test_administrateur_actor_constructor_exists():
    assert callable(Administrateur_Actor.__init__)


def test_administrateur_actor_constructor_args():
    sig = inspect.signature(Administrateur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_proposition_de_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Proposition_de_voyage_UseCase)


def test_proposition_de_voyage_usecase_constructor_exists():
    assert callable(Proposition_de_voyage_UseCase.__init__)


def test_proposition_de_voyage_usecase_constructor_args():
    sig = inspect.signature(Proposition_de_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_utilisateur_anonyme_actor_is_not_abstract():
    assert not inspect.isabstract(Utilisateur_anonyme_Actor)


def test_utilisateur_anonyme_actor_constructor_exists():
    assert callable(Utilisateur_anonyme_Actor.__init__)


def test_utilisateur_anonyme_actor_constructor_args():
    sig = inspect.signature(Utilisateur_anonyme_Actor.__init__)
    params = list(sig.parameters.keys())



def test_date_trajet_is_not_abstract():
    assert not inspect.isabstract(Date_trajet)


def test_date_trajet_constructor_exists():
    assert callable(Date_trajet.__init__)


def test_date_trajet_constructor_args():
    sig = inspect.signature(Date_trajet.__init__)
    params = list(sig.parameters.keys())
    assert "Date___heure__minute" in params, "Missing parameter 'Date___heure__minute'"
    assert "Jour" in params, "Missing parameter 'Jour'"
    assert "Type_date" in params, "Missing parameter 'Type_date'"
    assert "id_date" in params, "Missing parameter 'id_date'"

def test_date_trajet_has_Date___heure__minute():
    assert hasattr(Date_trajet, "Date___heure__minute")
    descriptor = None
    for klass in Date_trajet.__mro__:
        if "Date___heure__minute" in klass.__dict__:
            descriptor = klass.__dict__["Date___heure__minute"]
            break
    assert isinstance(descriptor, property)

def test_date_trajet_has_Jour():
    assert hasattr(Date_trajet, "Jour")
    descriptor = None
    for klass in Date_trajet.__mro__:
        if "Jour" in klass.__dict__:
            descriptor = klass.__dict__["Jour"]
            break
    assert isinstance(descriptor, property)

def test_date_trajet_has_Type_date():
    assert hasattr(Date_trajet, "Type_date")
    descriptor = None
    for klass in Date_trajet.__mro__:
        if "Type_date" in klass.__dict__:
            descriptor = klass.__dict__["Type_date"]
            break
    assert isinstance(descriptor, property)

def test_date_trajet_has_id_date():
    assert hasattr(Date_trajet, "id_date")
    descriptor = None
    for klass in Date_trajet.__mro__:
        if "id_date" in klass.__dict__:
            descriptor = klass.__dict__["id_date"]
            break
    assert isinstance(descriptor, property)



def test_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Pr_nom" in params, "Missing parameter 'Pr_nom'"
    assert "Telephone" in params, "Missing parameter 'Telephone'"
    assert "Nom" in params, "Missing parameter 'Nom'"
    assert "id_utilisateur" in params, "Missing parameter 'id_utilisateur'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Login" in params, "Missing parameter 'Login'"

def test_utilisateur_has_Mail():
    assert hasattr(Utilisateur, "Mail")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Mail" in klass.__dict__:
            descriptor = klass.__dict__["Mail"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_Pr_nom():
    assert hasattr(Utilisateur, "Pr_nom")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Pr_nom" in klass.__dict__:
            descriptor = klass.__dict__["Pr_nom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_Telephone():
    assert hasattr(Utilisateur, "Telephone")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Telephone" in klass.__dict__:
            descriptor = klass.__dict__["Telephone"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_Nom():
    assert hasattr(Utilisateur, "Nom")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Nom" in klass.__dict__:
            descriptor = klass.__dict__["Nom"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_id_utilisateur():
    assert hasattr(Utilisateur, "id_utilisateur")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "id_utilisateur" in klass.__dict__:
            descriptor = klass.__dict__["id_utilisateur"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_Password():
    assert hasattr(Utilisateur, "Password")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_utilisateur_has_Login():
    assert hasattr(Utilisateur, "Login")
    descriptor = None
    for klass in Utilisateur.__mro__:
        if "Login" in klass.__dict__:
            descriptor = klass.__dict__["Login"]
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
Effectue_un_paiement_UseCase_strategy = st.builds(
    Effectue_un_paiement_UseCase,
)
Valide_arriv__UseCase_strategy = st.builds(
    Valide_arriv__UseCase,
)
Valide_embarquement_UseCase_strategy = st.builds(
    Valide_embarquement_UseCase,
)
confirme_voyage_UseCase_strategy = st.builds(
    confirme_voyage_UseCase,
)
Reserve_voyage_UseCase_strategy = st.builds(
    Reserve_voyage_UseCase,
)
Administre_UseCase_strategy = st.builds(
    Administre_UseCase,
)
Choisi_un_voyage_UseCase_strategy = st.builds(
    Choisi_un_voyage_UseCase,
)
S_authentifier_UseCase_strategy = st.builds(
    S_authentifier_UseCase,
)
Enregistre_son_vehicule_UseCase_strategy = st.builds(
    Enregistre_son_vehicule_UseCase,
)
Conducteur_Actor_strategy = st.builds(
    Conducteur_Actor,
)
Passager__Actor_strategy = st.builds(
    Passager__Actor,
)
S_enregistre_UseCase_strategy = st.builds(
    S_enregistre_UseCase,
)
Administrateur_Actor_strategy = st.builds(
    Administrateur_Actor,
)
Proposition_de_voyage_UseCase_strategy = st.builds(
    Proposition_de_voyage_UseCase,
)
Utilisateur_anonyme_Actor_strategy = st.builds(
    Utilisateur_anonyme_Actor,
)
Date_trajet_strategy = st.builds(
    Date_trajet,
    Date___heure__minute=
        safe_text,
    Jour=
        safe_text,
    Type_date=
        safe_text,
    id_date=
        st.integers()
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    Mail=
        safe_text,
    Pr_nom=
        safe_text,
    Telephone=
        safe_text,
    Nom=
        safe_text,
    id_utilisateur=
        st.integers(),
    Password=
        safe_text,
    Login=
        safe_text
)

@given(instance=Effectue_un_paiement_UseCase_strategy)
@settings(max_examples=50)
def test_effectue_un_paiement_usecase_instantiation(instance):
    assert isinstance(instance, Effectue_un_paiement_UseCase)

@given(instance=Valide_arriv__UseCase_strategy)
@settings(max_examples=50)
def test_valide_arriv__usecase_instantiation(instance):
    assert isinstance(instance, Valide_arriv__UseCase)

@given(instance=Valide_embarquement_UseCase_strategy)
@settings(max_examples=50)
def test_valide_embarquement_usecase_instantiation(instance):
    assert isinstance(instance, Valide_embarquement_UseCase)

@given(instance=confirme_voyage_UseCase_strategy)
@settings(max_examples=50)
def test_confirme_voyage_usecase_instantiation(instance):
    assert isinstance(instance, confirme_voyage_UseCase)

@given(instance=Reserve_voyage_UseCase_strategy)
@settings(max_examples=50)
def test_reserve_voyage_usecase_instantiation(instance):
    assert isinstance(instance, Reserve_voyage_UseCase)

@given(instance=Administre_UseCase_strategy)
@settings(max_examples=50)
def test_administre_usecase_instantiation(instance):
    assert isinstance(instance, Administre_UseCase)

@given(instance=Choisi_un_voyage_UseCase_strategy)
@settings(max_examples=50)
def test_choisi_un_voyage_usecase_instantiation(instance):
    assert isinstance(instance, Choisi_un_voyage_UseCase)

@given(instance=S_authentifier_UseCase_strategy)
@settings(max_examples=50)
def test_s_authentifier_usecase_instantiation(instance):
    assert isinstance(instance, S_authentifier_UseCase)

@given(instance=Enregistre_son_vehicule_UseCase_strategy)
@settings(max_examples=50)
def test_enregistre_son_vehicule_usecase_instantiation(instance):
    assert isinstance(instance, Enregistre_son_vehicule_UseCase)

@given(instance=Conducteur_Actor_strategy)
@settings(max_examples=50)
def test_conducteur_actor_instantiation(instance):
    assert isinstance(instance, Conducteur_Actor)

@given(instance=Passager__Actor_strategy)
@settings(max_examples=50)
def test_passager__actor_instantiation(instance):
    assert isinstance(instance, Passager__Actor)

@given(instance=S_enregistre_UseCase_strategy)
@settings(max_examples=50)
def test_s_enregistre_usecase_instantiation(instance):
    assert isinstance(instance, S_enregistre_UseCase)

@given(instance=Administrateur_Actor_strategy)
@settings(max_examples=50)
def test_administrateur_actor_instantiation(instance):
    assert isinstance(instance, Administrateur_Actor)

@given(instance=Proposition_de_voyage_UseCase_strategy)
@settings(max_examples=50)
def test_proposition_de_voyage_usecase_instantiation(instance):
    assert isinstance(instance, Proposition_de_voyage_UseCase)

@given(instance=Utilisateur_anonyme_Actor_strategy)
@settings(max_examples=50)
def test_utilisateur_anonyme_actor_instantiation(instance):
    assert isinstance(instance, Utilisateur_anonyme_Actor)

@given(instance=Date_trajet_strategy)
@settings(max_examples=50)
def test_date_trajet_instantiation(instance):
    assert isinstance(instance, Date_trajet)



@given(instance=Date_trajet_strategy)
def test_date_trajet_Date___heure__minute_setter(instance):
    original = instance.Date___heure__minute
    instance.Date___heure__minute = original
    assert instance.Date___heure__minute == original



@given(instance=Date_trajet_strategy)
def test_date_trajet_Jour_setter(instance):
    original = instance.Jour
    instance.Jour = original
    assert instance.Jour == original



@given(instance=Date_trajet_strategy)
def test_date_trajet_Type_date_setter(instance):
    original = instance.Type_date
    instance.Type_date = original
    assert instance.Type_date == original



@given(instance=Date_trajet_strategy)
def test_date_trajet_id_date_setter(instance):
    original = instance.id_date
    instance.id_date = original
    assert instance.id_date == original

@given(instance=Utilisateur_strategy)
@settings(max_examples=50)
def test_utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)



@given(instance=Utilisateur_strategy)
def test_utilisateur_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_Pr_nom_setter(instance):
    original = instance.Pr_nom
    instance.Pr_nom = original
    assert instance.Pr_nom == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_Telephone_setter(instance):
    original = instance.Telephone
    instance.Telephone = original
    assert instance.Telephone == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_Nom_setter(instance):
    original = instance.Nom
    instance.Nom = original
    assert instance.Nom == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_id_utilisateur_setter(instance):
    original = instance.id_utilisateur
    instance.id_utilisateur = original
    assert instance.id_utilisateur == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Utilisateur_strategy)
def test_utilisateur_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original

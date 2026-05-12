import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    G,
    F,
    E,
    Vehicule,
    Permis,
    Reservation,
    Groupe,
    Chauffeur,
    Client,
    Z,
    B,
    C1,
    C2,
    Y,
    R,
    A,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_g_is_not_abstract():
    assert not inspect.isabstract(G)


def test_g_constructor_exists():
    assert callable(G.__init__)


def test_g_constructor_args():
    sig = inspect.signature(G.__init__)
    params = list(sig.parameters.keys())



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())
    assert "attF" in params, "Missing parameter 'attF'"

def test_f_has_attF():
    assert hasattr(F, "attF")
    descriptor = None
    for klass in F.__mro__:
        if "attF" in klass.__dict__:
            descriptor = klass.__dict__["attF"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())
    assert "attE" in params, "Missing parameter 'attE'"

def test_e_has_attE():
    assert hasattr(E, "attE")
    descriptor = None
    for klass in E.__mro__:
        if "attE" in klass.__dict__:
            descriptor = klass.__dict__["attE"]
            break
    assert isinstance(descriptor, property)



def test_vehicule_is_not_abstract():
    assert not inspect.isabstract(Vehicule)


def test_vehicule_constructor_exists():
    assert callable(Vehicule.__init__)


def test_vehicule_constructor_args():
    sig = inspect.signature(Vehicule.__init__)
    params = list(sig.parameters.keys())
    assert "standing" in params, "Missing parameter 'standing'"
    assert "rang" in params, "Missing parameter 'rang'"

def test_vehicule_has_standing():
    assert hasattr(Vehicule, "standing")
    descriptor = None
    for klass in Vehicule.__mro__:
        if "standing" in klass.__dict__:
            descriptor = klass.__dict__["standing"]
            break
    assert isinstance(descriptor, property)

def test_vehicule_has_rang():
    assert hasattr(Vehicule, "rang")
    descriptor = None
    for klass in Vehicule.__mro__:
        if "rang" in klass.__dict__:
            descriptor = klass.__dict__["rang"]
            break
    assert isinstance(descriptor, property)



def test_permis_is_not_abstract():
    assert not inspect.isabstract(Permis)


def test_permis_constructor_exists():
    assert callable(Permis.__init__)


def test_permis_constructor_args():
    sig = inspect.signature(Permis.__init__)
    params = list(sig.parameters.keys())



def test_reservation_is_not_abstract():
    assert not inspect.isabstract(Reservation)


def test_reservation_constructor_exists():
    assert callable(Reservation.__init__)


def test_reservation_constructor_args():
    sig = inspect.signature(Reservation.__init__)
    params = list(sig.parameters.keys())



def test_groupe_is_not_abstract():
    assert not inspect.isabstract(Groupe)


def test_groupe_constructor_exists():
    assert callable(Groupe.__init__)


def test_groupe_constructor_args():
    sig = inspect.signature(Groupe.__init__)
    params = list(sig.parameters.keys())
    assert "rang" in params, "Missing parameter 'rang'"

def test_groupe_has_rang():
    assert hasattr(Groupe, "rang")
    descriptor = None
    for klass in Groupe.__mro__:
        if "rang" in klass.__dict__:
            descriptor = klass.__dict__["rang"]
            break
    assert isinstance(descriptor, property)



def test_chauffeur_is_not_abstract():
    assert not inspect.isabstract(Chauffeur)


def test_chauffeur_constructor_exists():
    assert callable(Chauffeur.__init__)


def test_chauffeur_constructor_args():
    sig = inspect.signature(Chauffeur.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_chauffeur_has_position():
    assert hasattr(Chauffeur, "position")
    descriptor = None
    for klass in Chauffeur.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_client_constructor_exists():
    assert callable(Client.__init__)


def test_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "fonction" in params, "Missing parameter 'fonction'"

def test_client_has_nom():
    assert hasattr(Client, "nom")
    descriptor = None
    for klass in Client.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_client_has_fonction():
    assert hasattr(Client, "fonction")
    descriptor = None
    for klass in Client.__mro__:
        if "fonction" in klass.__dict__:
            descriptor = klass.__dict__["fonction"]
            break
    assert isinstance(descriptor, property)



def test_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_z_constructor_exists():
    assert callable(Z.__init__)


def test_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attb" in params, "Missing parameter 'attb'"

def test_b_has_attb():
    assert hasattr(B, "attb")
    descriptor = None
    for klass in B.__mro__:
        if "attb" in klass.__dict__:
            descriptor = klass.__dict__["attb"]
            break
    assert isinstance(descriptor, property)



def test_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_c1_constructor_exists():
    assert callable(C1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())
    assert "atty" in params, "Missing parameter 'atty'"

def test_y_has_atty():
    assert hasattr(Y, "atty")
    descriptor = None
    for klass in Y.__mro__:
        if "atty" in klass.__dict__:
            descriptor = klass.__dict__["atty"]
            break
    assert isinstance(descriptor, property)



def test_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_r_constructor_exists():
    assert callable(R.__init__)


def test_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "atta" in params, "Missing parameter 'atta'"

def test_a_has_atta():
    assert hasattr(A, "atta")
    descriptor = None
    for klass in A.__mro__:
        if "atta" in klass.__dict__:
            descriptor = klass.__dict__["atta"]
            break
    assert isinstance(descriptor, property)



def test_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_c_constructor_exists():
    assert callable(C.__init__)


def test_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())
    assert "attc1" in params, "Missing parameter 'attc1'"
    assert "attc2" in params, "Missing parameter 'attc2'"

def test_c_has_attc1():
    assert hasattr(C, "attc1")
    descriptor = None
    for klass in C.__mro__:
        if "attc1" in klass.__dict__:
            descriptor = klass.__dict__["attc1"]
            break
    assert isinstance(descriptor, property)

def test_c_has_attc2():
    assert hasattr(C, "attc2")
    descriptor = None
    for klass in C.__mro__:
        if "attc2" in klass.__dict__:
            descriptor = klass.__dict__["attc2"]
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
G_strategy = st.builds(
    G,
)
F_strategy = st.builds(
    F,
    attF=
        safe_text
)
E_strategy = st.builds(
    E,
    attE=
        safe_text
)
Vehicule_strategy = st.builds(
    Vehicule,
    standing=
        safe_text,
    rang=
        st.integers()
)
Permis_strategy = st.builds(
    Permis,
)
Reservation_strategy = st.builds(
    Reservation,
)
Groupe_strategy = st.builds(
    Groupe,
    rang=
        safe_text
)
Chauffeur_strategy = st.builds(
    Chauffeur,
    position=
        safe_text
)
Client_strategy = st.builds(
    Client,
    nom=
        safe_text,
    fonction=
        safe_text
)
Z_strategy = st.builds(
    Z,
)
B_strategy = st.builds(
    B,
    attb=
        safe_text
)
C1_strategy = st.builds(
    C1,
)
C2_strategy = st.builds(
    C2,
)
Y_strategy = st.builds(
    Y,
    atty=
        safe_text
)
R_strategy = st.builds(
    R,
)
A_strategy = st.builds(
    A,
    atta=
        safe_text
)
C_strategy = st.builds(
    C,
    attc1=
        st.integers(),
    attc2=
        st.booleans()
)

@given(instance=G_strategy)
@settings(max_examples=50)
def test_g_instantiation(instance):
    assert isinstance(instance, G)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)



@given(instance=F_strategy)
def test_f_attF_setter(instance):
    original = instance.attF
    instance.attF = original
    assert instance.attF == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)



@given(instance=E_strategy)
def test_e_attE_setter(instance):
    original = instance.attE
    instance.attE = original
    assert instance.attE == original

@given(instance=Vehicule_strategy)
@settings(max_examples=50)
def test_vehicule_instantiation(instance):
    assert isinstance(instance, Vehicule)



@given(instance=Vehicule_strategy)
def test_vehicule_standing_setter(instance):
    original = instance.standing
    instance.standing = original
    assert instance.standing == original



@given(instance=Vehicule_strategy)
def test_vehicule_rang_setter(instance):
    original = instance.rang
    instance.rang = original
    assert instance.rang == original

@given(instance=Permis_strategy)
@settings(max_examples=50)
def test_permis_instantiation(instance):
    assert isinstance(instance, Permis)

@given(instance=Reservation_strategy)
@settings(max_examples=50)
def test_reservation_instantiation(instance):
    assert isinstance(instance, Reservation)

@given(instance=Groupe_strategy)
@settings(max_examples=50)
def test_groupe_instantiation(instance):
    assert isinstance(instance, Groupe)



@given(instance=Groupe_strategy)
def test_groupe_rang_setter(instance):
    original = instance.rang
    instance.rang = original
    assert instance.rang == original

@given(instance=Chauffeur_strategy)
@settings(max_examples=50)
def test_chauffeur_instantiation(instance):
    assert isinstance(instance, Chauffeur)



@given(instance=Chauffeur_strategy)
def test_chauffeur_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Client_strategy)
@settings(max_examples=50)
def test_client_instantiation(instance):
    assert isinstance(instance, Client)



@given(instance=Client_strategy)
def test_client_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Client_strategy)
def test_client_fonction_setter(instance):
    original = instance.fonction
    instance.fonction = original
    assert instance.fonction == original

@given(instance=Z_strategy)
@settings(max_examples=50)
def test_z_instantiation(instance):
    assert isinstance(instance, Z)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)



@given(instance=B_strategy)
def test_b_attb_setter(instance):
    original = instance.attb
    instance.attb = original
    assert instance.attb == original

@given(instance=C1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, C1)

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)



@given(instance=Y_strategy)
def test_y_atty_setter(instance):
    original = instance.atty
    instance.atty = original
    assert instance.atty == original

@given(instance=R_strategy)
@settings(max_examples=50)
def test_r_instantiation(instance):
    assert isinstance(instance, R)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)



@given(instance=A_strategy)
def test_a_atta_setter(instance):
    original = instance.atta
    instance.atta = original
    assert instance.atta == original

@given(instance=C_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, C)



@given(instance=C_strategy)
def test_c_attc1_setter(instance):
    original = instance.attc1
    instance.attc1 = original
    assert instance.attc1 == original



@given(instance=C_strategy)
def test_c_attc2_setter(instance):
    original = instance.attc2
    instance.attc2 = original
    assert instance.attc2 == original

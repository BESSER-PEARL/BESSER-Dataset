import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ClassF,
    ClassE,
    ClassD,
    Commentaires,
    Cours,
    Membres,
    Quizz,
    MyClass,
    ClassL,
    ClassK,
    ClassH,
    ClassJ,
    ClassG,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classf_is_not_abstract():
    assert not inspect.isabstract(ClassF)


def test_classf_constructor_exists():
    assert callable(ClassF.__init__)


def test_classf_constructor_args():
    sig = inspect.signature(ClassF.__init__)
    params = list(sig.parameters.keys())



def test_classe_is_not_abstract():
    assert not inspect.isabstract(ClassE)


def test_classe_constructor_exists():
    assert callable(ClassE.__init__)


def test_classe_constructor_args():
    sig = inspect.signature(ClassE.__init__)
    params = list(sig.parameters.keys())



def test_classd_is_not_abstract():
    assert not inspect.isabstract(ClassD)


def test_classd_constructor_exists():
    assert callable(ClassD.__init__)


def test_classd_constructor_args():
    sig = inspect.signature(ClassD.__init__)
    params = list(sig.parameters.keys())



def test_commentaires_is_not_abstract():
    assert not inspect.isabstract(Commentaires)


def test_commentaires_constructor_exists():
    assert callable(Commentaires.__init__)


def test_commentaires_constructor_args():
    sig = inspect.signature(Commentaires.__init__)
    params = list(sig.parameters.keys())
    assert "idComm" in params, "Missing parameter 'idComm'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"

def test_commentaires_has_idComm():
    assert hasattr(Commentaires, "idComm")
    descriptor = None
    for klass in Commentaires.__mro__:
        if "idComm" in klass.__dict__:
            descriptor = klass.__dict__["idComm"]
            break
    assert isinstance(descriptor, property)

def test_commentaires_has_protectedAttribute():
    assert hasattr(Commentaires, "protectedAttribute")
    descriptor = None
    for klass in Commentaires.__mro__:
        if "protectedAttribute" in klass.__dict__:
            descriptor = klass.__dict__["protectedAttribute"]
            break
    assert isinstance(descriptor, property)

def test_commentaires_has_packageAttribute():
    assert hasattr(Commentaires, "packageAttribute")
    descriptor = None
    for klass in Commentaires.__mro__:
        if "packageAttribute" in klass.__dict__:
            descriptor = klass.__dict__["packageAttribute"]
            break
    assert isinstance(descriptor, property)

def test_commentaires_has_privateAttribute():
    assert hasattr(Commentaires, "privateAttribute")
    descriptor = None
    for klass in Commentaires.__mro__:
        if "privateAttribute" in klass.__dict__:
            descriptor = klass.__dict__["privateAttribute"]
            break
    assert isinstance(descriptor, property)



def test_cours_is_not_abstract():
    assert not inspect.isabstract(Cours)


def test_cours_constructor_exists():
    assert callable(Cours.__init__)


def test_cours_constructor_args():
    sig = inspect.signature(Cours.__init__)
    params = list(sig.parameters.keys())



def test_membres_is_not_abstract():
    assert not inspect.isabstract(Membres)


def test_membres_constructor_exists():
    assert callable(Membres.__init__)


def test_membres_constructor_args():
    sig = inspect.signature(Membres.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "email" in params, "Missing parameter 'email'"
    assert "mdp" in params, "Missing parameter 'mdp'"
    assert "idM" in params, "Missing parameter 'idM'"
    assert "prenom" in params, "Missing parameter 'prenom'"

def test_membres_has_nom():
    assert hasattr(Membres, "nom")
    descriptor = None
    for klass in Membres.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_membres_has_telephone():
    assert hasattr(Membres, "telephone")
    descriptor = None
    for klass in Membres.__mro__:
        if "telephone" in klass.__dict__:
            descriptor = klass.__dict__["telephone"]
            break
    assert isinstance(descriptor, property)

def test_membres_has_email():
    assert hasattr(Membres, "email")
    descriptor = None
    for klass in Membres.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_membres_has_mdp():
    assert hasattr(Membres, "mdp")
    descriptor = None
    for klass in Membres.__mro__:
        if "mdp" in klass.__dict__:
            descriptor = klass.__dict__["mdp"]
            break
    assert isinstance(descriptor, property)

def test_membres_has_idM():
    assert hasattr(Membres, "idM")
    descriptor = None
    for klass in Membres.__mro__:
        if "idM" in klass.__dict__:
            descriptor = klass.__dict__["idM"]
            break
    assert isinstance(descriptor, property)

def test_membres_has_prenom():
    assert hasattr(Membres, "prenom")
    descriptor = None
    for klass in Membres.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)



def test_quizz_is_not_abstract():
    assert not inspect.isabstract(Quizz)


def test_quizz_constructor_exists():
    assert callable(Quizz.__init__)


def test_quizz_constructor_args():
    sig = inspect.signature(Quizz.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_quizz_has_ownerName():
    assert hasattr(Quizz, "ownerName")
    descriptor = None
    for klass in Quizz.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)

def test_quizz_has_balance():
    assert hasattr(Quizz, "balance")
    descriptor = None
    for klass in Quizz.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_classl_is_not_abstract():
    assert not inspect.isabstract(ClassL)


def test_classl_constructor_exists():
    assert callable(ClassL.__init__)


def test_classl_constructor_args():
    sig = inspect.signature(ClassL.__init__)
    params = list(sig.parameters.keys())



def test_classk_is_not_abstract():
    assert not inspect.isabstract(ClassK)


def test_classk_constructor_exists():
    assert callable(ClassK.__init__)


def test_classk_constructor_args():
    sig = inspect.signature(ClassK.__init__)
    params = list(sig.parameters.keys())



def test_classh_is_not_abstract():
    assert not inspect.isabstract(ClassH)


def test_classh_constructor_exists():
    assert callable(ClassH.__init__)


def test_classh_constructor_args():
    sig = inspect.signature(ClassH.__init__)
    params = list(sig.parameters.keys())



def test_classj_is_not_abstract():
    assert not inspect.isabstract(ClassJ)


def test_classj_constructor_exists():
    assert callable(ClassJ.__init__)


def test_classj_constructor_args():
    sig = inspect.signature(ClassJ.__init__)
    params = list(sig.parameters.keys())



def test_classg_is_not_abstract():
    assert not inspect.isabstract(ClassG)


def test_classg_constructor_exists():
    assert callable(ClassG.__init__)


def test_classg_constructor_args():
    sig = inspect.signature(ClassG.__init__)
    params = list(sig.parameters.keys())


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
ClassF_strategy = st.builds(
    ClassF,
)
ClassE_strategy = st.builds(
    ClassE,
)
ClassD_strategy = st.builds(
    ClassD,
)
Commentaires_strategy = st.builds(
    Commentaires,
    idComm=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAttribute=
        safe_text,
    packageAttribute=
        safe_text,
    privateAttribute=
        st.integers()
)
Cours_strategy = st.builds(
    Cours,
)
Membres_strategy = st.builds(
    Membres,
    nom=
        safe_text,
    telephone=
        st.integers(),
    email=
        safe_text,
    mdp=
        safe_text,
    idM=
        safe_text,
    prenom=
        safe_text
)
Quizz_strategy = st.builds(
    Quizz,
    ownerName=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MyClass_strategy = st.builds(
    MyClass,
)
ClassL_strategy = st.builds(
    ClassL,
)
ClassK_strategy = st.builds(
    ClassK,
)
ClassH_strategy = st.builds(
    ClassH,
)
ClassJ_strategy = st.builds(
    ClassJ,
)
ClassG_strategy = st.builds(
    ClassG,
)

@given(instance=ClassF_strategy)
@settings(max_examples=50)
def test_classf_instantiation(instance):
    assert isinstance(instance, ClassF)

@given(instance=ClassE_strategy)
@settings(max_examples=50)
def test_classe_instantiation(instance):
    assert isinstance(instance, ClassE)

@given(instance=ClassD_strategy)
@settings(max_examples=50)
def test_classd_instantiation(instance):
    assert isinstance(instance, ClassD)

@given(instance=Commentaires_strategy)
@settings(max_examples=50)
def test_commentaires_instantiation(instance):
    assert isinstance(instance, Commentaires)



@given(instance=Commentaires_strategy)
def test_commentaires_idComm_setter(instance):
    original = instance.idComm
    instance.idComm = original
    assert instance.idComm == original



@given(instance=Commentaires_strategy)
def test_commentaires_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original



@given(instance=Commentaires_strategy)
def test_commentaires_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original



@given(instance=Commentaires_strategy)
def test_commentaires_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original

@given(instance=Cours_strategy)
@settings(max_examples=50)
def test_cours_instantiation(instance):
    assert isinstance(instance, Cours)

@given(instance=Membres_strategy)
@settings(max_examples=50)
def test_membres_instantiation(instance):
    assert isinstance(instance, Membres)



@given(instance=Membres_strategy)
def test_membres_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Membres_strategy)
def test_membres_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Membres_strategy)
def test_membres_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Membres_strategy)
def test_membres_mdp_setter(instance):
    original = instance.mdp
    instance.mdp = original
    assert instance.mdp == original



@given(instance=Membres_strategy)
def test_membres_idM_setter(instance):
    original = instance.idM
    instance.idM = original
    assert instance.idM == original



@given(instance=Membres_strategy)
def test_membres_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original

@given(instance=Quizz_strategy)
@settings(max_examples=50)
def test_quizz_instantiation(instance):
    assert isinstance(instance, Quizz)



@given(instance=Quizz_strategy)
def test_quizz_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=Quizz_strategy)
def test_quizz_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=ClassL_strategy)
@settings(max_examples=50)
def test_classl_instantiation(instance):
    assert isinstance(instance, ClassL)

@given(instance=ClassK_strategy)
@settings(max_examples=50)
def test_classk_instantiation(instance):
    assert isinstance(instance, ClassK)

@given(instance=ClassH_strategy)
@settings(max_examples=50)
def test_classh_instantiation(instance):
    assert isinstance(instance, ClassH)

@given(instance=ClassJ_strategy)
@settings(max_examples=50)
def test_classj_instantiation(instance):
    assert isinstance(instance, ClassJ)

@given(instance=ClassG_strategy)
@settings(max_examples=50)
def test_classg_instantiation(instance):
    assert isinstance(instance, ClassG)

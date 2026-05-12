import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CCP,
    Document,
    Formation,
    Session,
    Administrateur,
    Direction,
    Formateur,
    Etudiant,
    Personne,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
    ClassP,
    ClassN,
    ClassM,
    ClassL,
    ClassK,
    ClassH,
    ClassJ,
    ClassG,
    ClassF,
    ClassE,
    ClassD,
    ClassC,
    ClassB,
    ClassA,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ccp_is_not_abstract():
    assert not inspect.isabstract(CCP)


def test_ccp_constructor_exists():
    assert callable(CCP.__init__)


def test_ccp_constructor_args():
    sig = inspect.signature(CCP.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id_ccp" in params, "Missing parameter 'id_ccp'"

def test_ccp_has_label():
    assert hasattr(CCP, "label")
    descriptor = None
    for klass in CCP.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ccp_has_description():
    assert hasattr(CCP, "description")
    descriptor = None
    for klass in CCP.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ccp_has_id_ccp():
    assert hasattr(CCP, "id_ccp")
    descriptor = None
    for klass in CCP.__mro__:
        if "id_ccp" in klass.__dict__:
            descriptor = klass.__dict__["id_ccp"]
            break
    assert isinstance(descriptor, property)



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "url" in params, "Missing parameter 'url'"
    assert "cours" in params, "Missing parameter 'cours'"
    assert "id_document" in params, "Missing parameter 'id_document'"
    assert "descriptif" in params, "Missing parameter 'descriptif'"

def test_document_has_label():
    assert hasattr(Document, "label")
    descriptor = None
    for klass in Document.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_document_has_url():
    assert hasattr(Document, "url")
    descriptor = None
    for klass in Document.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_document_has_cours():
    assert hasattr(Document, "cours")
    descriptor = None
    for klass in Document.__mro__:
        if "cours" in klass.__dict__:
            descriptor = klass.__dict__["cours"]
            break
    assert isinstance(descriptor, property)

def test_document_has_id_document():
    assert hasattr(Document, "id_document")
    descriptor = None
    for klass in Document.__mro__:
        if "id_document" in klass.__dict__:
            descriptor = klass.__dict__["id_document"]
            break
    assert isinstance(descriptor, property)

def test_document_has_descriptif():
    assert hasattr(Document, "descriptif")
    descriptor = None
    for klass in Document.__mro__:
        if "descriptif" in klass.__dict__:
            descriptor = klass.__dict__["descriptif"]
            break
    assert isinstance(descriptor, property)



def test_formation_is_not_abstract():
    assert not inspect.isabstract(Formation)


def test_formation_constructor_exists():
    assert callable(Formation.__init__)


def test_formation_constructor_args():
    sig = inspect.signature(Formation.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "descriptif" in params, "Missing parameter 'descriptif'"
    assert "id_formation" in params, "Missing parameter 'id_formation'"

def test_formation_has_label():
    assert hasattr(Formation, "label")
    descriptor = None
    for klass in Formation.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_formation_has_descriptif():
    assert hasattr(Formation, "descriptif")
    descriptor = None
    for klass in Formation.__mro__:
        if "descriptif" in klass.__dict__:
            descriptor = klass.__dict__["descriptif"]
            break
    assert isinstance(descriptor, property)

def test_formation_has_id_formation():
    assert hasattr(Formation, "id_formation")
    descriptor = None
    for klass in Formation.__mro__:
        if "id_formation" in klass.__dict__:
            descriptor = klass.__dict__["id_formation"]
            break
    assert isinstance(descriptor, property)



def test_session_is_not_abstract():
    assert not inspect.isabstract(Session)


def test_session_constructor_exists():
    assert callable(Session.__init__)


def test_session_constructor_args():
    sig = inspect.signature(Session.__init__)
    params = list(sig.parameters.keys())
    assert "adresse" in params, "Missing parameter 'adresse'"
    assert "date_fin" in params, "Missing parameter 'date_fin'"
    assert "date_debut" in params, "Missing parameter 'date_debut'"
    assert "label" in params, "Missing parameter 'label'"
    assert "id_session" in params, "Missing parameter 'id_session'"

def test_session_has_adresse():
    assert hasattr(Session, "adresse")
    descriptor = None
    for klass in Session.__mro__:
        if "adresse" in klass.__dict__:
            descriptor = klass.__dict__["adresse"]
            break
    assert isinstance(descriptor, property)

def test_session_has_date_fin():
    assert hasattr(Session, "date_fin")
    descriptor = None
    for klass in Session.__mro__:
        if "date_fin" in klass.__dict__:
            descriptor = klass.__dict__["date_fin"]
            break
    assert isinstance(descriptor, property)

def test_session_has_date_debut():
    assert hasattr(Session, "date_debut")
    descriptor = None
    for klass in Session.__mro__:
        if "date_debut" in klass.__dict__:
            descriptor = klass.__dict__["date_debut"]
            break
    assert isinstance(descriptor, property)

def test_session_has_label():
    assert hasattr(Session, "label")
    descriptor = None
    for klass in Session.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_session_has_id_session():
    assert hasattr(Session, "id_session")
    descriptor = None
    for klass in Session.__mro__:
        if "id_session" in klass.__dict__:
            descriptor = klass.__dict__["id_session"]
            break
    assert isinstance(descriptor, property)



def test_administrateur_is_not_abstract():
    assert not inspect.isabstract(Administrateur)


def test_administrateur_constructor_exists():
    assert callable(Administrateur.__init__)


def test_administrateur_constructor_args():
    sig = inspect.signature(Administrateur.__init__)
    params = list(sig.parameters.keys())
    assert "id_administrateur" in params, "Missing parameter 'id_administrateur'"
    assert "actif" in params, "Missing parameter 'actif'"

def test_administrateur_has_id_administrateur():
    assert hasattr(Administrateur, "id_administrateur")
    descriptor = None
    for klass in Administrateur.__mro__:
        if "id_administrateur" in klass.__dict__:
            descriptor = klass.__dict__["id_administrateur"]
            break
    assert isinstance(descriptor, property)

def test_administrateur_has_actif():
    assert hasattr(Administrateur, "actif")
    descriptor = None
    for klass in Administrateur.__mro__:
        if "actif" in klass.__dict__:
            descriptor = klass.__dict__["actif"]
            break
    assert isinstance(descriptor, property)



def test_direction_is_not_abstract():
    assert not inspect.isabstract(Direction)


def test_direction_constructor_exists():
    assert callable(Direction.__init__)


def test_direction_constructor_args():
    sig = inspect.signature(Direction.__init__)
    params = list(sig.parameters.keys())
    assert "actif" in params, "Missing parameter 'actif'"
    assert "id_direction" in params, "Missing parameter 'id_direction'"

def test_direction_has_actif():
    assert hasattr(Direction, "actif")
    descriptor = None
    for klass in Direction.__mro__:
        if "actif" in klass.__dict__:
            descriptor = klass.__dict__["actif"]
            break
    assert isinstance(descriptor, property)

def test_direction_has_id_direction():
    assert hasattr(Direction, "id_direction")
    descriptor = None
    for klass in Direction.__mro__:
        if "id_direction" in klass.__dict__:
            descriptor = klass.__dict__["id_direction"]
            break
    assert isinstance(descriptor, property)



def test_formateur_is_not_abstract():
    assert not inspect.isabstract(Formateur)


def test_formateur_constructor_exists():
    assert callable(Formateur.__init__)


def test_formateur_constructor_args():
    sig = inspect.signature(Formateur.__init__)
    params = list(sig.parameters.keys())
    assert "id_formateur" in params, "Missing parameter 'id_formateur'"
    assert "actif" in params, "Missing parameter 'actif'"

def test_formateur_has_id_formateur():
    assert hasattr(Formateur, "id_formateur")
    descriptor = None
    for klass in Formateur.__mro__:
        if "id_formateur" in klass.__dict__:
            descriptor = klass.__dict__["id_formateur"]
            break
    assert isinstance(descriptor, property)

def test_formateur_has_actif():
    assert hasattr(Formateur, "actif")
    descriptor = None
    for klass in Formateur.__mro__:
        if "actif" in klass.__dict__:
            descriptor = klass.__dict__["actif"]
            break
    assert isinstance(descriptor, property)



def test_etudiant_is_not_abstract():
    assert not inspect.isabstract(Etudiant)


def test_etudiant_constructor_exists():
    assert callable(Etudiant.__init__)


def test_etudiant_constructor_args():
    sig = inspect.signature(Etudiant.__init__)
    params = list(sig.parameters.keys())
    assert "cv" in params, "Missing parameter 'cv'"
    assert "list_commentaire" in params, "Missing parameter 'list_commentaire'"
    assert "id_etudiant" in params, "Missing parameter 'id_etudiant'"
    assert "list_notes" in params, "Missing parameter 'list_notes'"
    assert "actif" in params, "Missing parameter 'actif'"

def test_etudiant_has_cv():
    assert hasattr(Etudiant, "cv")
    descriptor = None
    for klass in Etudiant.__mro__:
        if "cv" in klass.__dict__:
            descriptor = klass.__dict__["cv"]
            break
    assert isinstance(descriptor, property)

def test_etudiant_has_list_commentaire():
    assert hasattr(Etudiant, "list_commentaire")
    descriptor = None
    for klass in Etudiant.__mro__:
        if "list_commentaire" in klass.__dict__:
            descriptor = klass.__dict__["list_commentaire"]
            break
    assert isinstance(descriptor, property)

def test_etudiant_has_id_etudiant():
    assert hasattr(Etudiant, "id_etudiant")
    descriptor = None
    for klass in Etudiant.__mro__:
        if "id_etudiant" in klass.__dict__:
            descriptor = klass.__dict__["id_etudiant"]
            break
    assert isinstance(descriptor, property)

def test_etudiant_has_list_notes():
    assert hasattr(Etudiant, "list_notes")
    descriptor = None
    for klass in Etudiant.__mro__:
        if "list_notes" in klass.__dict__:
            descriptor = klass.__dict__["list_notes"]
            break
    assert isinstance(descriptor, property)

def test_etudiant_has_actif():
    assert hasattr(Etudiant, "actif")
    descriptor = None
    for klass in Etudiant.__mro__:
        if "actif" in klass.__dict__:
            descriptor = klass.__dict__["actif"]
            break
    assert isinstance(descriptor, property)



def test_personne_is_not_abstract():
    assert not inspect.isabstract(Personne)


def test_personne_constructor_exists():
    assert callable(Personne.__init__)


def test_personne_constructor_args():
    sig = inspect.signature(Personne.__init__)
    params = list(sig.parameters.keys())
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "telephone" in params, "Missing parameter 'telephone'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "photo" in params, "Missing parameter 'photo'"
    assert "naissance" in params, "Missing parameter 'naissance'"

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

def test_personne_has_mail():
    assert hasattr(Personne, "mail")
    descriptor = None
    for klass in Personne.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
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

def test_personne_has_nom():
    assert hasattr(Personne, "nom")
    descriptor = None
    for klass in Personne.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_photo():
    assert hasattr(Personne, "photo")
    descriptor = None
    for klass in Personne.__mro__:
        if "photo" in klass.__dict__:
            descriptor = klass.__dict__["photo"]
            break
    assert isinstance(descriptor, property)

def test_personne_has_naissance():
    assert hasattr(Personne, "naissance")
    descriptor = None
    for klass in Personne.__mro__:
        if "naissance" in klass.__dict__:
            descriptor = klass.__dict__["naissance"]
            break
    assert isinstance(descriptor, property)



def test_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_classn_is_not_abstract():
    assert not inspect.isabstract(ClassN)


def test_classn_constructor_exists():
    assert callable(ClassN.__init__)


def test_classn_constructor_args():
    sig = inspect.signature(ClassN.__init__)
    params = list(sig.parameters.keys())



def test_classm_is_not_abstract():
    assert not inspect.isabstract(ClassM)


def test_classm_constructor_exists():
    assert callable(ClassM.__init__)


def test_classm_constructor_args():
    sig = inspect.signature(ClassM.__init__)
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



def test_classc_is_not_abstract():
    assert not inspect.isabstract(ClassC)


def test_classc_constructor_exists():
    assert callable(ClassC.__init__)


def test_classc_constructor_args():
    sig = inspect.signature(ClassC.__init__)
    params = list(sig.parameters.keys())
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"

def test_classc_has_publicAttribute():
    assert hasattr(ClassC, "publicAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "publicAttribute" in klass.__dict__:
            descriptor = klass.__dict__["publicAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_protectedAttribute():
    assert hasattr(ClassC, "protectedAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "protectedAttribute" in klass.__dict__:
            descriptor = klass.__dict__["protectedAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_privateAttribute():
    assert hasattr(ClassC, "privateAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "privateAttribute" in klass.__dict__:
            descriptor = klass.__dict__["privateAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classc_has_packageAttribute():
    assert hasattr(ClassC, "packageAttribute")
    descriptor = None
    for klass in ClassC.__mro__:
        if "packageAttribute" in klass.__dict__:
            descriptor = klass.__dict__["packageAttribute"]
            break
    assert isinstance(descriptor, property)



def test_classb_is_not_abstract():
    assert not inspect.isabstract(ClassB)


def test_classb_constructor_exists():
    assert callable(ClassB.__init__)


def test_classb_constructor_args():
    sig = inspect.signature(ClassB.__init__)
    params = list(sig.parameters.keys())



def test_classa_is_not_abstract():
    assert not inspect.isabstract(ClassA)


def test_classa_constructor_exists():
    assert callable(ClassA.__init__)


def test_classa_constructor_args():
    sig = inspect.signature(ClassA.__init__)
    params = list(sig.parameters.keys())
    assert "privateAttribute" in params, "Missing parameter 'privateAttribute'"
    assert "publicAttribute" in params, "Missing parameter 'publicAttribute'"
    assert "packageAttribute" in params, "Missing parameter 'packageAttribute'"
    assert "protectedAttribute" in params, "Missing parameter 'protectedAttribute'"

def test_classa_has_privateAttribute():
    assert hasattr(ClassA, "privateAttribute")
    descriptor = None
    for klass in ClassA.__mro__:
        if "privateAttribute" in klass.__dict__:
            descriptor = klass.__dict__["privateAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classa_has_publicAttribute():
    assert hasattr(ClassA, "publicAttribute")
    descriptor = None
    for klass in ClassA.__mro__:
        if "publicAttribute" in klass.__dict__:
            descriptor = klass.__dict__["publicAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classa_has_packageAttribute():
    assert hasattr(ClassA, "packageAttribute")
    descriptor = None
    for klass in ClassA.__mro__:
        if "packageAttribute" in klass.__dict__:
            descriptor = klass.__dict__["packageAttribute"]
            break
    assert isinstance(descriptor, property)

def test_classa_has_protectedAttribute():
    assert hasattr(ClassA, "protectedAttribute")
    descriptor = None
    for klass in ClassA.__mro__:
        if "protectedAttribute" in klass.__dict__:
            descriptor = klass.__dict__["protectedAttribute"]
            break
    assert isinstance(descriptor, property)



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "ownerName" in params, "Missing parameter 'ownerName'"

def test_bankaccount_has_balance():
    assert hasattr(BankAccount, "balance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_ownerName():
    assert hasattr(BankAccount, "ownerName")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
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
CCP_strategy = st.builds(
    CCP,
    label=
        safe_text,
    description=
        safe_text,
    id_ccp=
        st.integers()
)
Document_strategy = st.builds(
    Document,
    label=
        safe_text,
    url=
        safe_text,
    cours=
        st.booleans(),
    id_document=
        st.integers(),
    descriptif=
        safe_text
)
Formation_strategy = st.builds(
    Formation,
    label=
        safe_text,
    descriptif=
        safe_text,
    id_formation=
        st.integers()
)
Session_strategy = st.builds(
    Session,
    adresse=
        safe_text,
    date_fin=
        st.dates(),
    date_debut=
        st.dates(),
    label=
        safe_text,
    id_session=
        st.integers()
)
Administrateur_strategy = st.builds(
    Administrateur,
    id_administrateur=
        st.integers(),
    actif=
        st.booleans()
)
Direction_strategy = st.builds(
    Direction,
    actif=
        st.booleans(),
    id_direction=
        st.integers()
)
Formateur_strategy = st.builds(
    Formateur,
    id_formateur=
        st.integers(),
    actif=
        st.booleans()
)
Etudiant_strategy = st.builds(
    Etudiant,
    cv=
        safe_text,
    list_commentaire=
        safe_text,
    id_etudiant=
        st.integers(),
    list_notes=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    actif=
        st.booleans()
)
Personne_strategy = st.builds(
    Personne,
    prenom=
        safe_text,
    id=
        st.integers(),
    mail=
        safe_text,
    telephone=
        safe_text,
    nom=
        safe_text,
    photo=
        safe_text,
    naissance=
        st.dates()
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)
ClassP_strategy = st.builds(
    ClassP,
)
ClassN_strategy = st.builds(
    ClassN,
)
ClassM_strategy = st.builds(
    ClassM,
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
ClassF_strategy = st.builds(
    ClassF,
)
ClassE_strategy = st.builds(
    ClassE,
)
ClassD_strategy = st.builds(
    ClassD,
)
ClassC_strategy = st.builds(
    ClassC,
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    protectedAttribute=
        safe_text,
    privateAttribute=
        st.integers(),
    packageAttribute=
        safe_text
)
ClassB_strategy = st.builds(
    ClassB,
)
ClassA_strategy = st.builds(
    ClassA,
    privateAttribute=
        st.integers(),
    publicAttribute=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    packageAttribute=
        safe_text,
    protectedAttribute=
        safe_text
)
BankAccount_strategy = st.builds(
    BankAccount,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ownerName=
        safe_text
)

@given(instance=CCP_strategy)
@settings(max_examples=50)
def test_ccp_instantiation(instance):
    assert isinstance(instance, CCP)



@given(instance=CCP_strategy)
def test_ccp_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=CCP_strategy)
def test_ccp_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=CCP_strategy)
def test_ccp_id_ccp_setter(instance):
    original = instance.id_ccp
    instance.id_ccp = original
    assert instance.id_ccp == original

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)



@given(instance=Document_strategy)
def test_document_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=Document_strategy)
def test_document_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=Document_strategy)
def test_document_cours_setter(instance):
    original = instance.cours
    instance.cours = original
    assert instance.cours == original



@given(instance=Document_strategy)
def test_document_id_document_setter(instance):
    original = instance.id_document
    instance.id_document = original
    assert instance.id_document == original



@given(instance=Document_strategy)
def test_document_descriptif_setter(instance):
    original = instance.descriptif
    instance.descriptif = original
    assert instance.descriptif == original

@given(instance=Formation_strategy)
@settings(max_examples=50)
def test_formation_instantiation(instance):
    assert isinstance(instance, Formation)



@given(instance=Formation_strategy)
def test_formation_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=Formation_strategy)
def test_formation_descriptif_setter(instance):
    original = instance.descriptif
    instance.descriptif = original
    assert instance.descriptif == original



@given(instance=Formation_strategy)
def test_formation_id_formation_setter(instance):
    original = instance.id_formation
    instance.id_formation = original
    assert instance.id_formation == original

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_session_instantiation(instance):
    assert isinstance(instance, Session)



@given(instance=Session_strategy)
def test_session_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original



@given(instance=Session_strategy)
def test_session_date_fin_setter(instance):
    original = instance.date_fin
    instance.date_fin = original
    assert instance.date_fin == original



@given(instance=Session_strategy)
def test_session_date_debut_setter(instance):
    original = instance.date_debut
    instance.date_debut = original
    assert instance.date_debut == original



@given(instance=Session_strategy)
def test_session_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=Session_strategy)
def test_session_id_session_setter(instance):
    original = instance.id_session
    instance.id_session = original
    assert instance.id_session == original

@given(instance=Administrateur_strategy)
@settings(max_examples=50)
def test_administrateur_instantiation(instance):
    assert isinstance(instance, Administrateur)



@given(instance=Administrateur_strategy)
def test_administrateur_id_administrateur_setter(instance):
    original = instance.id_administrateur
    instance.id_administrateur = original
    assert instance.id_administrateur == original



@given(instance=Administrateur_strategy)
def test_administrateur_actif_setter(instance):
    original = instance.actif
    instance.actif = original
    assert instance.actif == original

@given(instance=Direction_strategy)
@settings(max_examples=50)
def test_direction_instantiation(instance):
    assert isinstance(instance, Direction)



@given(instance=Direction_strategy)
def test_direction_actif_setter(instance):
    original = instance.actif
    instance.actif = original
    assert instance.actif == original



@given(instance=Direction_strategy)
def test_direction_id_direction_setter(instance):
    original = instance.id_direction
    instance.id_direction = original
    assert instance.id_direction == original

@given(instance=Formateur_strategy)
@settings(max_examples=50)
def test_formateur_instantiation(instance):
    assert isinstance(instance, Formateur)



@given(instance=Formateur_strategy)
def test_formateur_id_formateur_setter(instance):
    original = instance.id_formateur
    instance.id_formateur = original
    assert instance.id_formateur == original



@given(instance=Formateur_strategy)
def test_formateur_actif_setter(instance):
    original = instance.actif
    instance.actif = original
    assert instance.actif == original

@given(instance=Etudiant_strategy)
@settings(max_examples=50)
def test_etudiant_instantiation(instance):
    assert isinstance(instance, Etudiant)



@given(instance=Etudiant_strategy)
def test_etudiant_cv_setter(instance):
    original = instance.cv
    instance.cv = original
    assert instance.cv == original



@given(instance=Etudiant_strategy)
def test_etudiant_list_commentaire_setter(instance):
    original = instance.list_commentaire
    instance.list_commentaire = original
    assert instance.list_commentaire == original



@given(instance=Etudiant_strategy)
def test_etudiant_id_etudiant_setter(instance):
    original = instance.id_etudiant
    instance.id_etudiant = original
    assert instance.id_etudiant == original



@given(instance=Etudiant_strategy)
def test_etudiant_list_notes_setter(instance):
    original = instance.list_notes
    instance.list_notes = original
    assert instance.list_notes == original



@given(instance=Etudiant_strategy)
def test_etudiant_actif_setter(instance):
    original = instance.actif
    instance.actif = original
    assert instance.actif == original

@given(instance=Personne_strategy)
@settings(max_examples=50)
def test_personne_instantiation(instance):
    assert isinstance(instance, Personne)



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
def test_personne_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=Personne_strategy)
def test_personne_telephone_setter(instance):
    original = instance.telephone
    instance.telephone = original
    assert instance.telephone == original



@given(instance=Personne_strategy)
def test_personne_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Personne_strategy)
def test_personne_photo_setter(instance):
    original = instance.photo
    instance.photo = original
    assert instance.photo == original



@given(instance=Personne_strategy)
def test_personne_naissance_setter(instance):
    original = instance.naissance
    instance.naissance = original
    assert instance.naissance == original

@given(instance=ClassV_strategy)
@settings(max_examples=50)
def test_classv_instantiation(instance):
    assert isinstance(instance, ClassV)

@given(instance=ClassU_strategy)
@settings(max_examples=50)
def test_classu_instantiation(instance):
    assert isinstance(instance, ClassU)

@given(instance=ClassT_strategy)
@settings(max_examples=50)
def test_classt_instantiation(instance):
    assert isinstance(instance, ClassT)

@given(instance=ClassS_strategy)
@settings(max_examples=50)
def test_classs_instantiation(instance):
    assert isinstance(instance, ClassS)

@given(instance=ClassR_strategy)
@settings(max_examples=50)
def test_classr_instantiation(instance):
    assert isinstance(instance, ClassR)

@given(instance=ClassQ_strategy)
@settings(max_examples=50)
def test_classq_instantiation(instance):
    assert isinstance(instance, ClassQ)

@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=50)
def test_interfaceo_interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)

@given(instance=ClassP_strategy)
@settings(max_examples=50)
def test_classp_instantiation(instance):
    assert isinstance(instance, ClassP)

@given(instance=ClassN_strategy)
@settings(max_examples=50)
def test_classn_instantiation(instance):
    assert isinstance(instance, ClassN)

@given(instance=ClassM_strategy)
@settings(max_examples=50)
def test_classm_instantiation(instance):
    assert isinstance(instance, ClassM)

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

@given(instance=ClassC_strategy)
@settings(max_examples=50)
def test_classc_instantiation(instance):
    assert isinstance(instance, ClassC)



@given(instance=ClassC_strategy)
def test_classc_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=ClassC_strategy)
def test_classc_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original



@given(instance=ClassC_strategy)
def test_classc_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=ClassC_strategy)
def test_classc_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original

@given(instance=ClassB_strategy)
@settings(max_examples=50)
def test_classb_instantiation(instance):
    assert isinstance(instance, ClassB)

@given(instance=ClassA_strategy)
@settings(max_examples=50)
def test_classa_instantiation(instance):
    assert isinstance(instance, ClassA)



@given(instance=ClassA_strategy)
def test_classa_privateAttribute_setter(instance):
    original = instance.privateAttribute
    instance.privateAttribute = original
    assert instance.privateAttribute == original



@given(instance=ClassA_strategy)
def test_classa_publicAttribute_setter(instance):
    original = instance.publicAttribute
    instance.publicAttribute = original
    assert instance.publicAttribute == original



@given(instance=ClassA_strategy)
def test_classa_packageAttribute_setter(instance):
    original = instance.packageAttribute
    instance.packageAttribute = original
    assert instance.packageAttribute == original



@given(instance=ClassA_strategy)
def test_classa_protectedAttribute_setter(instance):
    original = instance.protectedAttribute
    instance.protectedAttribute = original
    assert instance.protectedAttribute == original

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_bankaccount_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original

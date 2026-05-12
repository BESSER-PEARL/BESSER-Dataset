import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Parallele,
    droneDSLLib_Parallele3,
    droneDSLLib_Parallele4,
    droneDSLLib_Parallele2,
    droneDSLLib_CommandeBasique,
    droneDSLLib_DecollerAtterrir,
    droneDSLLib_Mouvement,
    droneDSLLib_AR,
    droneDSLLib_RGRD,
    droneDSLLib_GDr,
    droneDSLLib_MD,
    FonctionCall,
    droneDSLLib_FonctionCallInterne,
    droneDSLLib_FonctionCall,
    droneDSLLib_EObject,
    AR,
    RGRD,
    GDr,
    VarDecl,
    droneDSLLib_PourcentDecl,
    droneDSLLib_SecondeDecl,
    PourcentExp,
    droneDSLLib_PourcentConst,
    MD,
    CommandeBasique,
    droneDSLLib_Pause,
    Mouvement,
    droneDSLLib_Avancer,
    droneDSLLib_Reculer,
    droneDSLLib_Droite,
    droneDSLLib_RotationDroite,
    droneDSLLib_RotationGauche,
    droneDSLLib_Descendre,
    droneDSLLib_Parallele,
    droneDSLLib_Gauche,
    droneDSLLib_Monter,
    DecollerAtterrir,
    droneDSLLib_Atterrir,
    droneDSLLib_Decoller,
    droneDSLLib_SecondeExp,
    droneDSLLib_PourcentExp,
    droneDSLLib_RefPourcentVar,
    droneDSLLib_VarDecl,
    SecondeExp,
    droneDSLLib_RefSecondeVar,
    droneDSLLib_SecondeConst,
    droneDSLLib_FonctionDecl,
    droneDSLLib_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parallele_is_not_abstract():
    assert not inspect.isabstract(Parallele)


def test_parallele_constructor_exists():
    assert callable(Parallele.__init__)


def test_parallele_constructor_args():
    sig = inspect.signature(Parallele.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_parallele3_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Parallele3)


def test_dronedsllib_parallele3_constructor_exists():
    assert callable(droneDSLLib_Parallele3.__init__)


def test_dronedsllib_parallele3_constructor_args():
    sig = inspect.signature(droneDSLLib_Parallele3.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_parallele4_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Parallele4)


def test_dronedsllib_parallele4_constructor_exists():
    assert callable(droneDSLLib_Parallele4.__init__)


def test_dronedsllib_parallele4_constructor_args():
    sig = inspect.signature(droneDSLLib_Parallele4.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_parallele2_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Parallele2)


def test_dronedsllib_parallele2_constructor_exists():
    assert callable(droneDSLLib_Parallele2.__init__)


def test_dronedsllib_parallele2_constructor_args():
    sig = inspect.signature(droneDSLLib_Parallele2.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_commandebasique_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_CommandeBasique)


def test_dronedsllib_commandebasique_constructor_exists():
    assert callable(droneDSLLib_CommandeBasique.__init__)


def test_dronedsllib_commandebasique_constructor_args():
    sig = inspect.signature(droneDSLLib_CommandeBasique.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_decolleratterrir_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_DecollerAtterrir)


def test_dronedsllib_decolleratterrir_constructor_exists():
    assert callable(droneDSLLib_DecollerAtterrir.__init__)


def test_dronedsllib_decolleratterrir_constructor_args():
    sig = inspect.signature(droneDSLLib_DecollerAtterrir.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_dronedsllib_decolleratterrir_has_str():
    assert hasattr(droneDSLLib_DecollerAtterrir, "str")
    descriptor = None
    for klass in droneDSLLib_DecollerAtterrir.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib_mouvement_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Mouvement)


def test_dronedsllib_mouvement_constructor_exists():
    assert callable(droneDSLLib_Mouvement.__init__)


def test_dronedsllib_mouvement_constructor_args():
    sig = inspect.signature(droneDSLLib_Mouvement.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_ar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_AR)


def test_dronedsllib_ar_constructor_exists():
    assert callable(droneDSLLib_AR.__init__)


def test_dronedsllib_ar_constructor_args():
    sig = inspect.signature(droneDSLLib_AR.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_rgrd_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_RGRD)


def test_dronedsllib_rgrd_constructor_exists():
    assert callable(droneDSLLib_RGRD.__init__)


def test_dronedsllib_rgrd_constructor_args():
    sig = inspect.signature(droneDSLLib_RGRD.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_gdr_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_GDr)


def test_dronedsllib_gdr_constructor_exists():
    assert callable(droneDSLLib_GDr.__init__)


def test_dronedsllib_gdr_constructor_args():
    sig = inspect.signature(droneDSLLib_GDr.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_md_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_MD)


def test_dronedsllib_md_constructor_exists():
    assert callable(droneDSLLib_MD.__init__)


def test_dronedsllib_md_constructor_args():
    sig = inspect.signature(droneDSLLib_MD.__init__)
    params = list(sig.parameters.keys())



def test_fonctioncall_is_not_abstract():
    assert not inspect.isabstract(FonctionCall)


def test_fonctioncall_constructor_exists():
    assert callable(FonctionCall.__init__)


def test_fonctioncall_constructor_args():
    sig = inspect.signature(FonctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_fonctioncallinterne_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_FonctionCallInterne)


def test_dronedsllib_fonctioncallinterne_constructor_exists():
    assert callable(droneDSLLib_FonctionCallInterne.__init__)


def test_dronedsllib_fonctioncallinterne_constructor_args():
    sig = inspect.signature(droneDSLLib_FonctionCallInterne.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_fonctioncall_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_FonctionCall)


def test_dronedsllib_fonctioncall_constructor_exists():
    assert callable(droneDSLLib_FonctionCall.__init__)


def test_dronedsllib_fonctioncall_constructor_args():
    sig = inspect.signature(droneDSLLib_FonctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_eobject_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_EObject)


def test_dronedsllib_eobject_constructor_exists():
    assert callable(droneDSLLib_EObject.__init__)


def test_dronedsllib_eobject_constructor_args():
    sig = inspect.signature(droneDSLLib_EObject.__init__)
    params = list(sig.parameters.keys())



def test_ar_is_not_abstract():
    assert not inspect.isabstract(AR)


def test_ar_constructor_exists():
    assert callable(AR.__init__)


def test_ar_constructor_args():
    sig = inspect.signature(AR.__init__)
    params = list(sig.parameters.keys())



def test_rgrd_is_not_abstract():
    assert not inspect.isabstract(RGRD)


def test_rgrd_constructor_exists():
    assert callable(RGRD.__init__)


def test_rgrd_constructor_args():
    sig = inspect.signature(RGRD.__init__)
    params = list(sig.parameters.keys())



def test_gdr_is_not_abstract():
    assert not inspect.isabstract(GDr)


def test_gdr_constructor_exists():
    assert callable(GDr.__init__)


def test_gdr_constructor_args():
    sig = inspect.signature(GDr.__init__)
    params = list(sig.parameters.keys())



def test_vardecl_is_not_abstract():
    assert not inspect.isabstract(VarDecl)


def test_vardecl_constructor_exists():
    assert callable(VarDecl.__init__)


def test_vardecl_constructor_args():
    sig = inspect.signature(VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_pourcentdecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_PourcentDecl)


def test_dronedsllib_pourcentdecl_constructor_exists():
    assert callable(droneDSLLib_PourcentDecl.__init__)


def test_dronedsllib_pourcentdecl_constructor_args():
    sig = inspect.signature(droneDSLLib_PourcentDecl.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_secondedecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_SecondeDecl)


def test_dronedsllib_secondedecl_constructor_exists():
    assert callable(droneDSLLib_SecondeDecl.__init__)


def test_dronedsllib_secondedecl_constructor_args():
    sig = inspect.signature(droneDSLLib_SecondeDecl.__init__)
    params = list(sig.parameters.keys())



def test_pourcentexp_is_not_abstract():
    assert not inspect.isabstract(PourcentExp)


def test_pourcentexp_constructor_exists():
    assert callable(PourcentExp.__init__)


def test_pourcentexp_constructor_args():
    sig = inspect.signature(PourcentExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_pourcentconst_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_PourcentConst)


def test_dronedsllib_pourcentconst_constructor_exists():
    assert callable(droneDSLLib_PourcentConst.__init__)


def test_dronedsllib_pourcentconst_constructor_args():
    sig = inspect.signature(droneDSLLib_PourcentConst.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dronedsllib_pourcentconst_has_val():
    assert hasattr(droneDSLLib_PourcentConst, "val")
    descriptor = None
    for klass in droneDSLLib_PourcentConst.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_md_is_not_abstract():
    assert not inspect.isabstract(MD)


def test_md_constructor_exists():
    assert callable(MD.__init__)


def test_md_constructor_args():
    sig = inspect.signature(MD.__init__)
    params = list(sig.parameters.keys())



def test_commandebasique_is_not_abstract():
    assert not inspect.isabstract(CommandeBasique)


def test_commandebasique_constructor_exists():
    assert callable(CommandeBasique.__init__)


def test_commandebasique_constructor_args():
    sig = inspect.signature(CommandeBasique.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_pause_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Pause)


def test_dronedsllib_pause_constructor_exists():
    assert callable(droneDSLLib_Pause.__init__)


def test_dronedsllib_pause_constructor_args():
    sig = inspect.signature(droneDSLLib_Pause.__init__)
    params = list(sig.parameters.keys())



def test_mouvement_is_not_abstract():
    assert not inspect.isabstract(Mouvement)


def test_mouvement_constructor_exists():
    assert callable(Mouvement.__init__)


def test_mouvement_constructor_args():
    sig = inspect.signature(Mouvement.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_avancer_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Avancer)


def test_dronedsllib_avancer_constructor_exists():
    assert callable(droneDSLLib_Avancer.__init__)


def test_dronedsllib_avancer_constructor_args():
    sig = inspect.signature(droneDSLLib_Avancer.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_reculer_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Reculer)


def test_dronedsllib_reculer_constructor_exists():
    assert callable(droneDSLLib_Reculer.__init__)


def test_dronedsllib_reculer_constructor_args():
    sig = inspect.signature(droneDSLLib_Reculer.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_droite_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Droite)


def test_dronedsllib_droite_constructor_exists():
    assert callable(droneDSLLib_Droite.__init__)


def test_dronedsllib_droite_constructor_args():
    sig = inspect.signature(droneDSLLib_Droite.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_rotationdroite_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_RotationDroite)


def test_dronedsllib_rotationdroite_constructor_exists():
    assert callable(droneDSLLib_RotationDroite.__init__)


def test_dronedsllib_rotationdroite_constructor_args():
    sig = inspect.signature(droneDSLLib_RotationDroite.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_rotationgauche_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_RotationGauche)


def test_dronedsllib_rotationgauche_constructor_exists():
    assert callable(droneDSLLib_RotationGauche.__init__)


def test_dronedsllib_rotationgauche_constructor_args():
    sig = inspect.signature(droneDSLLib_RotationGauche.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_descendre_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Descendre)


def test_dronedsllib_descendre_constructor_exists():
    assert callable(droneDSLLib_Descendre.__init__)


def test_dronedsllib_descendre_constructor_args():
    sig = inspect.signature(droneDSLLib_Descendre.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_parallele_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Parallele)


def test_dronedsllib_parallele_constructor_exists():
    assert callable(droneDSLLib_Parallele.__init__)


def test_dronedsllib_parallele_constructor_args():
    sig = inspect.signature(droneDSLLib_Parallele.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_gauche_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Gauche)


def test_dronedsllib_gauche_constructor_exists():
    assert callable(droneDSLLib_Gauche.__init__)


def test_dronedsllib_gauche_constructor_args():
    sig = inspect.signature(droneDSLLib_Gauche.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_monter_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Monter)


def test_dronedsllib_monter_constructor_exists():
    assert callable(droneDSLLib_Monter.__init__)


def test_dronedsllib_monter_constructor_args():
    sig = inspect.signature(droneDSLLib_Monter.__init__)
    params = list(sig.parameters.keys())



def test_decolleratterrir_is_not_abstract():
    assert not inspect.isabstract(DecollerAtterrir)


def test_decolleratterrir_constructor_exists():
    assert callable(DecollerAtterrir.__init__)


def test_decolleratterrir_constructor_args():
    sig = inspect.signature(DecollerAtterrir.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_atterrir_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Atterrir)


def test_dronedsllib_atterrir_constructor_exists():
    assert callable(droneDSLLib_Atterrir.__init__)


def test_dronedsllib_atterrir_constructor_args():
    sig = inspect.signature(droneDSLLib_Atterrir.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_decoller_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Decoller)


def test_dronedsllib_decoller_constructor_exists():
    assert callable(droneDSLLib_Decoller.__init__)


def test_dronedsllib_decoller_constructor_args():
    sig = inspect.signature(droneDSLLib_Decoller.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_secondeexp_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_SecondeExp)


def test_dronedsllib_secondeexp_constructor_exists():
    assert callable(droneDSLLib_SecondeExp.__init__)


def test_dronedsllib_secondeexp_constructor_args():
    sig = inspect.signature(droneDSLLib_SecondeExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_pourcentexp_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_PourcentExp)


def test_dronedsllib_pourcentexp_constructor_exists():
    assert callable(droneDSLLib_PourcentExp.__init__)


def test_dronedsllib_pourcentexp_constructor_args():
    sig = inspect.signature(droneDSLLib_PourcentExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_refpourcentvar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_RefPourcentVar)


def test_dronedsllib_refpourcentvar_constructor_exists():
    assert callable(droneDSLLib_RefPourcentVar.__init__)


def test_dronedsllib_refpourcentvar_constructor_args():
    sig = inspect.signature(droneDSLLib_RefPourcentVar.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_vardecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_VarDecl)


def test_dronedsllib_vardecl_constructor_exists():
    assert callable(droneDSLLib_VarDecl.__init__)


def test_dronedsllib_vardecl_constructor_args():
    sig = inspect.signature(droneDSLLib_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dronedsllib_vardecl_has_name():
    assert hasattr(droneDSLLib_VarDecl, "name")
    descriptor = None
    for klass in droneDSLLib_VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_secondeexp_is_not_abstract():
    assert not inspect.isabstract(SecondeExp)


def test_secondeexp_constructor_exists():
    assert callable(SecondeExp.__init__)


def test_secondeexp_constructor_args():
    sig = inspect.signature(SecondeExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_refsecondevar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_RefSecondeVar)


def test_dronedsllib_refsecondevar_constructor_exists():
    assert callable(droneDSLLib_RefSecondeVar.__init__)


def test_dronedsllib_refsecondevar_constructor_args():
    sig = inspect.signature(droneDSLLib_RefSecondeVar.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib_secondeconst_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_SecondeConst)


def test_dronedsllib_secondeconst_constructor_exists():
    assert callable(droneDSLLib_SecondeConst.__init__)


def test_dronedsllib_secondeconst_constructor_args():
    sig = inspect.signature(droneDSLLib_SecondeConst.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dronedsllib_secondeconst_has_val():
    assert hasattr(droneDSLLib_SecondeConst, "val")
    descriptor = None
    for klass in droneDSLLib_SecondeConst.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib_fonctiondecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_FonctionDecl)


def test_dronedsllib_fonctiondecl_constructor_exists():
    assert callable(droneDSLLib_FonctionDecl.__init__)


def test_dronedsllib_fonctiondecl_constructor_args():
    sig = inspect.signature(droneDSLLib_FonctionDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dronedsllib_fonctiondecl_has_name():
    assert hasattr(droneDSLLib_FonctionDecl, "name")
    descriptor = None
    for klass in droneDSLLib_FonctionDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib_model_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib_Model)


def test_dronedsllib_model_constructor_exists():
    assert callable(droneDSLLib_Model.__init__)


def test_dronedsllib_model_constructor_args():
    sig = inspect.signature(droneDSLLib_Model.__init__)
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
Parallele_strategy = st.builds(
    Parallele,
)
droneDSLLib_Parallele3_strategy = st.builds(
    droneDSLLib_Parallele3,
)
droneDSLLib_Parallele4_strategy = st.builds(
    droneDSLLib_Parallele4,
)
droneDSLLib_Parallele2_strategy = st.builds(
    droneDSLLib_Parallele2,
)
droneDSLLib_CommandeBasique_strategy = st.builds(
    droneDSLLib_CommandeBasique,
)
droneDSLLib_DecollerAtterrir_strategy = st.builds(
    droneDSLLib_DecollerAtterrir,
    str=
        safe_text
)
droneDSLLib_Mouvement_strategy = st.builds(
    droneDSLLib_Mouvement,
)
droneDSLLib_AR_strategy = st.builds(
    droneDSLLib_AR,
)
droneDSLLib_RGRD_strategy = st.builds(
    droneDSLLib_RGRD,
)
droneDSLLib_GDr_strategy = st.builds(
    droneDSLLib_GDr,
)
droneDSLLib_MD_strategy = st.builds(
    droneDSLLib_MD,
)
FonctionCall_strategy = st.builds(
    FonctionCall,
)
droneDSLLib_FonctionCallInterne_strategy = st.builds(
    droneDSLLib_FonctionCallInterne,
)
droneDSLLib_FonctionCall_strategy = st.builds(
    droneDSLLib_FonctionCall,
)
droneDSLLib_EObject_strategy = st.builds(
    droneDSLLib_EObject,
)
AR_strategy = st.builds(
    AR,
)
RGRD_strategy = st.builds(
    RGRD,
)
GDr_strategy = st.builds(
    GDr,
)
VarDecl_strategy = st.builds(
    VarDecl,
)
droneDSLLib_PourcentDecl_strategy = st.builds(
    droneDSLLib_PourcentDecl,
)
droneDSLLib_SecondeDecl_strategy = st.builds(
    droneDSLLib_SecondeDecl,
)
PourcentExp_strategy = st.builds(
    PourcentExp,
)
droneDSLLib_PourcentConst_strategy = st.builds(
    droneDSLLib_PourcentConst,
    val=
        safe_text
)
MD_strategy = st.builds(
    MD,
)
CommandeBasique_strategy = st.builds(
    CommandeBasique,
)
droneDSLLib_Pause_strategy = st.builds(
    droneDSLLib_Pause,
)
Mouvement_strategy = st.builds(
    Mouvement,
)
droneDSLLib_Avancer_strategy = st.builds(
    droneDSLLib_Avancer,
)
droneDSLLib_Reculer_strategy = st.builds(
    droneDSLLib_Reculer,
)
droneDSLLib_Droite_strategy = st.builds(
    droneDSLLib_Droite,
)
droneDSLLib_RotationDroite_strategy = st.builds(
    droneDSLLib_RotationDroite,
)
droneDSLLib_RotationGauche_strategy = st.builds(
    droneDSLLib_RotationGauche,
)
droneDSLLib_Descendre_strategy = st.builds(
    droneDSLLib_Descendre,
)
droneDSLLib_Parallele_strategy = st.builds(
    droneDSLLib_Parallele,
)
droneDSLLib_Gauche_strategy = st.builds(
    droneDSLLib_Gauche,
)
droneDSLLib_Monter_strategy = st.builds(
    droneDSLLib_Monter,
)
DecollerAtterrir_strategy = st.builds(
    DecollerAtterrir,
)
droneDSLLib_Atterrir_strategy = st.builds(
    droneDSLLib_Atterrir,
)
droneDSLLib_Decoller_strategy = st.builds(
    droneDSLLib_Decoller,
)
droneDSLLib_SecondeExp_strategy = st.builds(
    droneDSLLib_SecondeExp,
)
droneDSLLib_PourcentExp_strategy = st.builds(
    droneDSLLib_PourcentExp,
)
droneDSLLib_RefPourcentVar_strategy = st.builds(
    droneDSLLib_RefPourcentVar,
)
droneDSLLib_VarDecl_strategy = st.builds(
    droneDSLLib_VarDecl,
    name=
        safe_text
)
SecondeExp_strategy = st.builds(
    SecondeExp,
)
droneDSLLib_RefSecondeVar_strategy = st.builds(
    droneDSLLib_RefSecondeVar,
)
droneDSLLib_SecondeConst_strategy = st.builds(
    droneDSLLib_SecondeConst,
    val=
        safe_text
)
droneDSLLib_FonctionDecl_strategy = st.builds(
    droneDSLLib_FonctionDecl,
    name=
        safe_text
)
droneDSLLib_Model_strategy = st.builds(
    droneDSLLib_Model,
)

@given(instance=Parallele_strategy)
@settings(max_examples=50)
def test_parallele_instantiation(instance):
    assert isinstance(instance, Parallele)

@given(instance=droneDSLLib_Parallele3_strategy)
@settings(max_examples=50)
def test_dronedsllib_parallele3_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Parallele3)

@given(instance=droneDSLLib_Parallele4_strategy)
@settings(max_examples=50)
def test_dronedsllib_parallele4_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Parallele4)

@given(instance=droneDSLLib_Parallele2_strategy)
@settings(max_examples=50)
def test_dronedsllib_parallele2_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Parallele2)

@given(instance=droneDSLLib_CommandeBasique_strategy)
@settings(max_examples=50)
def test_dronedsllib_commandebasique_instantiation(instance):
    assert isinstance(instance, droneDSLLib_CommandeBasique)

@given(instance=droneDSLLib_DecollerAtterrir_strategy)
@settings(max_examples=50)
def test_dronedsllib_decolleratterrir_instantiation(instance):
    assert isinstance(instance, droneDSLLib_DecollerAtterrir)



@given(instance=droneDSLLib_DecollerAtterrir_strategy)
def test_dronedsllib_decolleratterrir_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=droneDSLLib_Mouvement_strategy)
@settings(max_examples=50)
def test_dronedsllib_mouvement_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Mouvement)

@given(instance=droneDSLLib_AR_strategy)
@settings(max_examples=50)
def test_dronedsllib_ar_instantiation(instance):
    assert isinstance(instance, droneDSLLib_AR)

@given(instance=droneDSLLib_RGRD_strategy)
@settings(max_examples=50)
def test_dronedsllib_rgrd_instantiation(instance):
    assert isinstance(instance, droneDSLLib_RGRD)

@given(instance=droneDSLLib_GDr_strategy)
@settings(max_examples=50)
def test_dronedsllib_gdr_instantiation(instance):
    assert isinstance(instance, droneDSLLib_GDr)

@given(instance=droneDSLLib_MD_strategy)
@settings(max_examples=50)
def test_dronedsllib_md_instantiation(instance):
    assert isinstance(instance, droneDSLLib_MD)

@given(instance=FonctionCall_strategy)
@settings(max_examples=50)
def test_fonctioncall_instantiation(instance):
    assert isinstance(instance, FonctionCall)

@given(instance=droneDSLLib_FonctionCallInterne_strategy)
@settings(max_examples=50)
def test_dronedsllib_fonctioncallinterne_instantiation(instance):
    assert isinstance(instance, droneDSLLib_FonctionCallInterne)

@given(instance=droneDSLLib_FonctionCall_strategy)
@settings(max_examples=50)
def test_dronedsllib_fonctioncall_instantiation(instance):
    assert isinstance(instance, droneDSLLib_FonctionCall)

@given(instance=droneDSLLib_EObject_strategy)
@settings(max_examples=50)
def test_dronedsllib_eobject_instantiation(instance):
    assert isinstance(instance, droneDSLLib_EObject)

@given(instance=AR_strategy)
@settings(max_examples=50)
def test_ar_instantiation(instance):
    assert isinstance(instance, AR)

@given(instance=RGRD_strategy)
@settings(max_examples=50)
def test_rgrd_instantiation(instance):
    assert isinstance(instance, RGRD)

@given(instance=GDr_strategy)
@settings(max_examples=50)
def test_gdr_instantiation(instance):
    assert isinstance(instance, GDr)

@given(instance=VarDecl_strategy)
@settings(max_examples=50)
def test_vardecl_instantiation(instance):
    assert isinstance(instance, VarDecl)

@given(instance=droneDSLLib_PourcentDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib_pourcentdecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib_PourcentDecl)

@given(instance=droneDSLLib_SecondeDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib_secondedecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib_SecondeDecl)

@given(instance=PourcentExp_strategy)
@settings(max_examples=50)
def test_pourcentexp_instantiation(instance):
    assert isinstance(instance, PourcentExp)

@given(instance=droneDSLLib_PourcentConst_strategy)
@settings(max_examples=50)
def test_dronedsllib_pourcentconst_instantiation(instance):
    assert isinstance(instance, droneDSLLib_PourcentConst)



@given(instance=droneDSLLib_PourcentConst_strategy)
def test_dronedsllib_pourcentconst_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=MD_strategy)
@settings(max_examples=50)
def test_md_instantiation(instance):
    assert isinstance(instance, MD)

@given(instance=CommandeBasique_strategy)
@settings(max_examples=50)
def test_commandebasique_instantiation(instance):
    assert isinstance(instance, CommandeBasique)

@given(instance=droneDSLLib_Pause_strategy)
@settings(max_examples=50)
def test_dronedsllib_pause_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Pause)

@given(instance=Mouvement_strategy)
@settings(max_examples=50)
def test_mouvement_instantiation(instance):
    assert isinstance(instance, Mouvement)

@given(instance=droneDSLLib_Avancer_strategy)
@settings(max_examples=50)
def test_dronedsllib_avancer_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Avancer)

@given(instance=droneDSLLib_Reculer_strategy)
@settings(max_examples=50)
def test_dronedsllib_reculer_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Reculer)

@given(instance=droneDSLLib_Droite_strategy)
@settings(max_examples=50)
def test_dronedsllib_droite_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Droite)

@given(instance=droneDSLLib_RotationDroite_strategy)
@settings(max_examples=50)
def test_dronedsllib_rotationdroite_instantiation(instance):
    assert isinstance(instance, droneDSLLib_RotationDroite)

@given(instance=droneDSLLib_RotationGauche_strategy)
@settings(max_examples=50)
def test_dronedsllib_rotationgauche_instantiation(instance):
    assert isinstance(instance, droneDSLLib_RotationGauche)

@given(instance=droneDSLLib_Descendre_strategy)
@settings(max_examples=50)
def test_dronedsllib_descendre_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Descendre)

@given(instance=droneDSLLib_Parallele_strategy)
@settings(max_examples=50)
def test_dronedsllib_parallele_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Parallele)

@given(instance=droneDSLLib_Gauche_strategy)
@settings(max_examples=50)
def test_dronedsllib_gauche_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Gauche)

@given(instance=droneDSLLib_Monter_strategy)
@settings(max_examples=50)
def test_dronedsllib_monter_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Monter)

@given(instance=DecollerAtterrir_strategy)
@settings(max_examples=50)
def test_decolleratterrir_instantiation(instance):
    assert isinstance(instance, DecollerAtterrir)

@given(instance=droneDSLLib_Atterrir_strategy)
@settings(max_examples=50)
def test_dronedsllib_atterrir_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Atterrir)

@given(instance=droneDSLLib_Decoller_strategy)
@settings(max_examples=50)
def test_dronedsllib_decoller_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Decoller)

@given(instance=droneDSLLib_SecondeExp_strategy)
@settings(max_examples=50)
def test_dronedsllib_secondeexp_instantiation(instance):
    assert isinstance(instance, droneDSLLib_SecondeExp)

@given(instance=droneDSLLib_PourcentExp_strategy)
@settings(max_examples=50)
def test_dronedsllib_pourcentexp_instantiation(instance):
    assert isinstance(instance, droneDSLLib_PourcentExp)

@given(instance=droneDSLLib_RefPourcentVar_strategy)
@settings(max_examples=50)
def test_dronedsllib_refpourcentvar_instantiation(instance):
    assert isinstance(instance, droneDSLLib_RefPourcentVar)

@given(instance=droneDSLLib_VarDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib_vardecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib_VarDecl)



@given(instance=droneDSLLib_VarDecl_strategy)
def test_dronedsllib_vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SecondeExp_strategy)
@settings(max_examples=50)
def test_secondeexp_instantiation(instance):
    assert isinstance(instance, SecondeExp)

@given(instance=droneDSLLib_RefSecondeVar_strategy)
@settings(max_examples=50)
def test_dronedsllib_refsecondevar_instantiation(instance):
    assert isinstance(instance, droneDSLLib_RefSecondeVar)

@given(instance=droneDSLLib_SecondeConst_strategy)
@settings(max_examples=50)
def test_dronedsllib_secondeconst_instantiation(instance):
    assert isinstance(instance, droneDSLLib_SecondeConst)



@given(instance=droneDSLLib_SecondeConst_strategy)
def test_dronedsllib_secondeconst_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=droneDSLLib_FonctionDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib_fonctiondecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib_FonctionDecl)



@given(instance=droneDSLLib_FonctionDecl_strategy)
def test_dronedsllib_fonctiondecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=droneDSLLib_Model_strategy)
@settings(max_examples=50)
def test_dronedsllib_model_instantiation(instance):
    assert isinstance(instance, droneDSLLib_Model)

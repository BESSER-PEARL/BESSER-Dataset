import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Parallele,
    droneDSLLib::Parallele4,
    droneDSLLib::Parallele3,
    droneDSLLib::Parallele2,
    droneDSLLib::CommandeBasique,
    droneDSLLib::DecollerAtterrir,
    droneDSLLib::Mouvement,
    droneDSLLib::AR,
    droneDSLLib::RGRD,
    droneDSLLib::GDr,
    droneDSLLib::MD,
    FonctionCall,
    droneDSLLib::FonctionCallInterne,
    droneDSLLib::FonctionCall,
    droneDSLLib::EObject,
    AR,
    RGRD,
    GDr,
    VarDecl,
    droneDSLLib::PourcentDecl,
    droneDSLLib::SecondeDecl,
    PourcentExp,
    droneDSLLib::PourcentConst,
    MD,
    CommandeBasique,
    droneDSLLib::Pause,
    Mouvement,
    droneDSLLib::Droite,
    droneDSLLib::RotationDroite,
    droneDSLLib::Gauche,
    droneDSLLib::RotationGauche,
    droneDSLLib::Avancer,
    droneDSLLib::Parallele,
    droneDSLLib::Reculer,
    droneDSLLib::Descendre,
    droneDSLLib::Monter,
    DecollerAtterrir,
    droneDSLLib::Atterrir,
    droneDSLLib::Decoller,
    droneDSLLib::SecondeExp,
    droneDSLLib::PourcentExp,
    droneDSLLib::RefPourcentVar,
    droneDSLLib::VarDecl,
    SecondeExp,
    droneDSLLib::RefSecondeVar,
    droneDSLLib::SecondeConst,
    droneDSLLib::FonctionDecl,
    droneDSLLib::Model,
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



def test_dronedsllib::parallele4_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Parallele4)


def test_dronedsllib::parallele4_constructor_exists():
    assert callable(droneDSLLib::Parallele4.__init__)


def test_dronedsllib::parallele4_constructor_args():
    sig = inspect.signature(droneDSLLib::Parallele4.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::parallele3_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Parallele3)


def test_dronedsllib::parallele3_constructor_exists():
    assert callable(droneDSLLib::Parallele3.__init__)


def test_dronedsllib::parallele3_constructor_args():
    sig = inspect.signature(droneDSLLib::Parallele3.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::parallele2_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Parallele2)


def test_dronedsllib::parallele2_constructor_exists():
    assert callable(droneDSLLib::Parallele2.__init__)


def test_dronedsllib::parallele2_constructor_args():
    sig = inspect.signature(droneDSLLib::Parallele2.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::commandebasique_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::CommandeBasique)


def test_dronedsllib::commandebasique_constructor_exists():
    assert callable(droneDSLLib::CommandeBasique.__init__)


def test_dronedsllib::commandebasique_constructor_args():
    sig = inspect.signature(droneDSLLib::CommandeBasique.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::decolleratterrir_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::DecollerAtterrir)


def test_dronedsllib::decolleratterrir_constructor_exists():
    assert callable(droneDSLLib::DecollerAtterrir.__init__)


def test_dronedsllib::decolleratterrir_constructor_args():
    sig = inspect.signature(droneDSLLib::DecollerAtterrir.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_dronedsllib::decolleratterrir_has_str():
    assert hasattr(droneDSLLib::DecollerAtterrir, "str")
    descriptor = None
    for klass in droneDSLLib::DecollerAtterrir.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib::mouvement_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Mouvement)


def test_dronedsllib::mouvement_constructor_exists():
    assert callable(droneDSLLib::Mouvement.__init__)


def test_dronedsllib::mouvement_constructor_args():
    sig = inspect.signature(droneDSLLib::Mouvement.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::ar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::AR)


def test_dronedsllib::ar_constructor_exists():
    assert callable(droneDSLLib::AR.__init__)


def test_dronedsllib::ar_constructor_args():
    sig = inspect.signature(droneDSLLib::AR.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::rgrd_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::RGRD)


def test_dronedsllib::rgrd_constructor_exists():
    assert callable(droneDSLLib::RGRD.__init__)


def test_dronedsllib::rgrd_constructor_args():
    sig = inspect.signature(droneDSLLib::RGRD.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::gdr_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::GDr)


def test_dronedsllib::gdr_constructor_exists():
    assert callable(droneDSLLib::GDr.__init__)


def test_dronedsllib::gdr_constructor_args():
    sig = inspect.signature(droneDSLLib::GDr.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::md_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::MD)


def test_dronedsllib::md_constructor_exists():
    assert callable(droneDSLLib::MD.__init__)


def test_dronedsllib::md_constructor_args():
    sig = inspect.signature(droneDSLLib::MD.__init__)
    params = list(sig.parameters.keys())



def test_fonctioncall_is_not_abstract():
    assert not inspect.isabstract(FonctionCall)


def test_fonctioncall_constructor_exists():
    assert callable(FonctionCall.__init__)


def test_fonctioncall_constructor_args():
    sig = inspect.signature(FonctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::fonctioncallinterne_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::FonctionCallInterne)


def test_dronedsllib::fonctioncallinterne_constructor_exists():
    assert callable(droneDSLLib::FonctionCallInterne.__init__)


def test_dronedsllib::fonctioncallinterne_constructor_args():
    sig = inspect.signature(droneDSLLib::FonctionCallInterne.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::fonctioncall_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::FonctionCall)


def test_dronedsllib::fonctioncall_constructor_exists():
    assert callable(droneDSLLib::FonctionCall.__init__)


def test_dronedsllib::fonctioncall_constructor_args():
    sig = inspect.signature(droneDSLLib::FonctionCall.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::eobject_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::EObject)


def test_dronedsllib::eobject_constructor_exists():
    assert callable(droneDSLLib::EObject.__init__)


def test_dronedsllib::eobject_constructor_args():
    sig = inspect.signature(droneDSLLib::EObject.__init__)
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



def test_dronedsllib::pourcentdecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::PourcentDecl)


def test_dronedsllib::pourcentdecl_constructor_exists():
    assert callable(droneDSLLib::PourcentDecl.__init__)


def test_dronedsllib::pourcentdecl_constructor_args():
    sig = inspect.signature(droneDSLLib::PourcentDecl.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::secondedecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::SecondeDecl)


def test_dronedsllib::secondedecl_constructor_exists():
    assert callable(droneDSLLib::SecondeDecl.__init__)


def test_dronedsllib::secondedecl_constructor_args():
    sig = inspect.signature(droneDSLLib::SecondeDecl.__init__)
    params = list(sig.parameters.keys())



def test_pourcentexp_is_not_abstract():
    assert not inspect.isabstract(PourcentExp)


def test_pourcentexp_constructor_exists():
    assert callable(PourcentExp.__init__)


def test_pourcentexp_constructor_args():
    sig = inspect.signature(PourcentExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::pourcentconst_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::PourcentConst)


def test_dronedsllib::pourcentconst_constructor_exists():
    assert callable(droneDSLLib::PourcentConst.__init__)


def test_dronedsllib::pourcentconst_constructor_args():
    sig = inspect.signature(droneDSLLib::PourcentConst.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dronedsllib::pourcentconst_has_val():
    assert hasattr(droneDSLLib::PourcentConst, "val")
    descriptor = None
    for klass in droneDSLLib::PourcentConst.__mro__:
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



def test_dronedsllib::pause_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Pause)


def test_dronedsllib::pause_constructor_exists():
    assert callable(droneDSLLib::Pause.__init__)


def test_dronedsllib::pause_constructor_args():
    sig = inspect.signature(droneDSLLib::Pause.__init__)
    params = list(sig.parameters.keys())



def test_mouvement_is_not_abstract():
    assert not inspect.isabstract(Mouvement)


def test_mouvement_constructor_exists():
    assert callable(Mouvement.__init__)


def test_mouvement_constructor_args():
    sig = inspect.signature(Mouvement.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::droite_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Droite)


def test_dronedsllib::droite_constructor_exists():
    assert callable(droneDSLLib::Droite.__init__)


def test_dronedsllib::droite_constructor_args():
    sig = inspect.signature(droneDSLLib::Droite.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::rotationdroite_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::RotationDroite)


def test_dronedsllib::rotationdroite_constructor_exists():
    assert callable(droneDSLLib::RotationDroite.__init__)


def test_dronedsllib::rotationdroite_constructor_args():
    sig = inspect.signature(droneDSLLib::RotationDroite.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::gauche_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Gauche)


def test_dronedsllib::gauche_constructor_exists():
    assert callable(droneDSLLib::Gauche.__init__)


def test_dronedsllib::gauche_constructor_args():
    sig = inspect.signature(droneDSLLib::Gauche.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::rotationgauche_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::RotationGauche)


def test_dronedsllib::rotationgauche_constructor_exists():
    assert callable(droneDSLLib::RotationGauche.__init__)


def test_dronedsllib::rotationgauche_constructor_args():
    sig = inspect.signature(droneDSLLib::RotationGauche.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::avancer_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Avancer)


def test_dronedsllib::avancer_constructor_exists():
    assert callable(droneDSLLib::Avancer.__init__)


def test_dronedsllib::avancer_constructor_args():
    sig = inspect.signature(droneDSLLib::Avancer.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::parallele_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Parallele)


def test_dronedsllib::parallele_constructor_exists():
    assert callable(droneDSLLib::Parallele.__init__)


def test_dronedsllib::parallele_constructor_args():
    sig = inspect.signature(droneDSLLib::Parallele.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::reculer_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Reculer)


def test_dronedsllib::reculer_constructor_exists():
    assert callable(droneDSLLib::Reculer.__init__)


def test_dronedsllib::reculer_constructor_args():
    sig = inspect.signature(droneDSLLib::Reculer.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::descendre_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Descendre)


def test_dronedsllib::descendre_constructor_exists():
    assert callable(droneDSLLib::Descendre.__init__)


def test_dronedsllib::descendre_constructor_args():
    sig = inspect.signature(droneDSLLib::Descendre.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::monter_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Monter)


def test_dronedsllib::monter_constructor_exists():
    assert callable(droneDSLLib::Monter.__init__)


def test_dronedsllib::monter_constructor_args():
    sig = inspect.signature(droneDSLLib::Monter.__init__)
    params = list(sig.parameters.keys())



def test_decolleratterrir_is_not_abstract():
    assert not inspect.isabstract(DecollerAtterrir)


def test_decolleratterrir_constructor_exists():
    assert callable(DecollerAtterrir.__init__)


def test_decolleratterrir_constructor_args():
    sig = inspect.signature(DecollerAtterrir.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::atterrir_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Atterrir)


def test_dronedsllib::atterrir_constructor_exists():
    assert callable(droneDSLLib::Atterrir.__init__)


def test_dronedsllib::atterrir_constructor_args():
    sig = inspect.signature(droneDSLLib::Atterrir.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::decoller_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Decoller)


def test_dronedsllib::decoller_constructor_exists():
    assert callable(droneDSLLib::Decoller.__init__)


def test_dronedsllib::decoller_constructor_args():
    sig = inspect.signature(droneDSLLib::Decoller.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::secondeexp_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::SecondeExp)


def test_dronedsllib::secondeexp_constructor_exists():
    assert callable(droneDSLLib::SecondeExp.__init__)


def test_dronedsllib::secondeexp_constructor_args():
    sig = inspect.signature(droneDSLLib::SecondeExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::pourcentexp_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::PourcentExp)


def test_dronedsllib::pourcentexp_constructor_exists():
    assert callable(droneDSLLib::PourcentExp.__init__)


def test_dronedsllib::pourcentexp_constructor_args():
    sig = inspect.signature(droneDSLLib::PourcentExp.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::refpourcentvar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::RefPourcentVar)


def test_dronedsllib::refpourcentvar_constructor_exists():
    assert callable(droneDSLLib::RefPourcentVar.__init__)


def test_dronedsllib::refpourcentvar_constructor_args():
    sig = inspect.signature(droneDSLLib::RefPourcentVar.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::vardecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::VarDecl)


def test_dronedsllib::vardecl_constructor_exists():
    assert callable(droneDSLLib::VarDecl.__init__)


def test_dronedsllib::vardecl_constructor_args():
    sig = inspect.signature(droneDSLLib::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dronedsllib::vardecl_has_name():
    assert hasattr(droneDSLLib::VarDecl, "name")
    descriptor = None
    for klass in droneDSLLib::VarDecl.__mro__:
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



def test_dronedsllib::refsecondevar_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::RefSecondeVar)


def test_dronedsllib::refsecondevar_constructor_exists():
    assert callable(droneDSLLib::RefSecondeVar.__init__)


def test_dronedsllib::refsecondevar_constructor_args():
    sig = inspect.signature(droneDSLLib::RefSecondeVar.__init__)
    params = list(sig.parameters.keys())



def test_dronedsllib::secondeconst_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::SecondeConst)


def test_dronedsllib::secondeconst_constructor_exists():
    assert callable(droneDSLLib::SecondeConst.__init__)


def test_dronedsllib::secondeconst_constructor_args():
    sig = inspect.signature(droneDSLLib::SecondeConst.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dronedsllib::secondeconst_has_val():
    assert hasattr(droneDSLLib::SecondeConst, "val")
    descriptor = None
    for klass in droneDSLLib::SecondeConst.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib::fonctiondecl_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::FonctionDecl)


def test_dronedsllib::fonctiondecl_constructor_exists():
    assert callable(droneDSLLib::FonctionDecl.__init__)


def test_dronedsllib::fonctiondecl_constructor_args():
    sig = inspect.signature(droneDSLLib::FonctionDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dronedsllib::fonctiondecl_has_name():
    assert hasattr(droneDSLLib::FonctionDecl, "name")
    descriptor = None
    for klass in droneDSLLib::FonctionDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dronedsllib::model_is_not_abstract():
    assert not inspect.isabstract(droneDSLLib::Model)


def test_dronedsllib::model_constructor_exists():
    assert callable(droneDSLLib::Model.__init__)


def test_dronedsllib::model_constructor_args():
    sig = inspect.signature(droneDSLLib::Model.__init__)
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
droneDSLLib::Parallele4_strategy = st.builds(
    droneDSLLib::Parallele4,
)
droneDSLLib::Parallele3_strategy = st.builds(
    droneDSLLib::Parallele3,
)
droneDSLLib::Parallele2_strategy = st.builds(
    droneDSLLib::Parallele2,
)
droneDSLLib::CommandeBasique_strategy = st.builds(
    droneDSLLib::CommandeBasique,
)
droneDSLLib::DecollerAtterrir_strategy = st.builds(
    droneDSLLib::DecollerAtterrir,
    str=
        safe_text
)
droneDSLLib::Mouvement_strategy = st.builds(
    droneDSLLib::Mouvement,
)
droneDSLLib::AR_strategy = st.builds(
    droneDSLLib::AR,
)
droneDSLLib::RGRD_strategy = st.builds(
    droneDSLLib::RGRD,
)
droneDSLLib::GDr_strategy = st.builds(
    droneDSLLib::GDr,
)
droneDSLLib::MD_strategy = st.builds(
    droneDSLLib::MD,
)
FonctionCall_strategy = st.builds(
    FonctionCall,
)
droneDSLLib::FonctionCallInterne_strategy = st.builds(
    droneDSLLib::FonctionCallInterne,
)
droneDSLLib::FonctionCall_strategy = st.builds(
    droneDSLLib::FonctionCall,
)
droneDSLLib::EObject_strategy = st.builds(
    droneDSLLib::EObject,
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
droneDSLLib::PourcentDecl_strategy = st.builds(
    droneDSLLib::PourcentDecl,
)
droneDSLLib::SecondeDecl_strategy = st.builds(
    droneDSLLib::SecondeDecl,
)
PourcentExp_strategy = st.builds(
    PourcentExp,
)
droneDSLLib::PourcentConst_strategy = st.builds(
    droneDSLLib::PourcentConst,
    val=
        safe_text
)
MD_strategy = st.builds(
    MD,
)
CommandeBasique_strategy = st.builds(
    CommandeBasique,
)
droneDSLLib::Pause_strategy = st.builds(
    droneDSLLib::Pause,
)
Mouvement_strategy = st.builds(
    Mouvement,
)
droneDSLLib::Droite_strategy = st.builds(
    droneDSLLib::Droite,
)
droneDSLLib::RotationDroite_strategy = st.builds(
    droneDSLLib::RotationDroite,
)
droneDSLLib::Gauche_strategy = st.builds(
    droneDSLLib::Gauche,
)
droneDSLLib::RotationGauche_strategy = st.builds(
    droneDSLLib::RotationGauche,
)
droneDSLLib::Avancer_strategy = st.builds(
    droneDSLLib::Avancer,
)
droneDSLLib::Parallele_strategy = st.builds(
    droneDSLLib::Parallele,
)
droneDSLLib::Reculer_strategy = st.builds(
    droneDSLLib::Reculer,
)
droneDSLLib::Descendre_strategy = st.builds(
    droneDSLLib::Descendre,
)
droneDSLLib::Monter_strategy = st.builds(
    droneDSLLib::Monter,
)
DecollerAtterrir_strategy = st.builds(
    DecollerAtterrir,
)
droneDSLLib::Atterrir_strategy = st.builds(
    droneDSLLib::Atterrir,
)
droneDSLLib::Decoller_strategy = st.builds(
    droneDSLLib::Decoller,
)
droneDSLLib::SecondeExp_strategy = st.builds(
    droneDSLLib::SecondeExp,
)
droneDSLLib::PourcentExp_strategy = st.builds(
    droneDSLLib::PourcentExp,
)
droneDSLLib::RefPourcentVar_strategy = st.builds(
    droneDSLLib::RefPourcentVar,
)
droneDSLLib::VarDecl_strategy = st.builds(
    droneDSLLib::VarDecl,
    name=
        safe_text
)
SecondeExp_strategy = st.builds(
    SecondeExp,
)
droneDSLLib::RefSecondeVar_strategy = st.builds(
    droneDSLLib::RefSecondeVar,
)
droneDSLLib::SecondeConst_strategy = st.builds(
    droneDSLLib::SecondeConst,
    val=
        safe_text
)
droneDSLLib::FonctionDecl_strategy = st.builds(
    droneDSLLib::FonctionDecl,
    name=
        safe_text
)
droneDSLLib::Model_strategy = st.builds(
    droneDSLLib::Model,
)

@given(instance=Parallele_strategy)
@settings(max_examples=50)
def test_parallele_instantiation(instance):
    assert isinstance(instance, Parallele)

@given(instance=droneDSLLib::Parallele4_strategy)
@settings(max_examples=50)
def test_dronedsllib::parallele4_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Parallele4)

@given(instance=droneDSLLib::Parallele3_strategy)
@settings(max_examples=50)
def test_dronedsllib::parallele3_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Parallele3)

@given(instance=droneDSLLib::Parallele2_strategy)
@settings(max_examples=50)
def test_dronedsllib::parallele2_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Parallele2)

@given(instance=droneDSLLib::CommandeBasique_strategy)
@settings(max_examples=50)
def test_dronedsllib::commandebasique_instantiation(instance):
    assert isinstance(instance, droneDSLLib::CommandeBasique)

@given(instance=droneDSLLib::DecollerAtterrir_strategy)
@settings(max_examples=50)
def test_dronedsllib::decolleratterrir_instantiation(instance):
    assert isinstance(instance, droneDSLLib::DecollerAtterrir)

@given(instance=droneDSLLib::DecollerAtterrir_strategy)
def test_dronedsllib::decolleratterrir_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=droneDSLLib::DecollerAtterrir_strategy)
def test_dronedsllib::decolleratterrir_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=droneDSLLib::Mouvement_strategy)
@settings(max_examples=50)
def test_dronedsllib::mouvement_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Mouvement)

@given(instance=droneDSLLib::AR_strategy)
@settings(max_examples=50)
def test_dronedsllib::ar_instantiation(instance):
    assert isinstance(instance, droneDSLLib::AR)

@given(instance=droneDSLLib::RGRD_strategy)
@settings(max_examples=50)
def test_dronedsllib::rgrd_instantiation(instance):
    assert isinstance(instance, droneDSLLib::RGRD)

@given(instance=droneDSLLib::GDr_strategy)
@settings(max_examples=50)
def test_dronedsllib::gdr_instantiation(instance):
    assert isinstance(instance, droneDSLLib::GDr)

@given(instance=droneDSLLib::MD_strategy)
@settings(max_examples=50)
def test_dronedsllib::md_instantiation(instance):
    assert isinstance(instance, droneDSLLib::MD)

@given(instance=FonctionCall_strategy)
@settings(max_examples=50)
def test_fonctioncall_instantiation(instance):
    assert isinstance(instance, FonctionCall)

@given(instance=droneDSLLib::FonctionCallInterne_strategy)
@settings(max_examples=50)
def test_dronedsllib::fonctioncallinterne_instantiation(instance):
    assert isinstance(instance, droneDSLLib::FonctionCallInterne)

@given(instance=droneDSLLib::FonctionCall_strategy)
@settings(max_examples=50)
def test_dronedsllib::fonctioncall_instantiation(instance):
    assert isinstance(instance, droneDSLLib::FonctionCall)

@given(instance=droneDSLLib::EObject_strategy)
@settings(max_examples=50)
def test_dronedsllib::eobject_instantiation(instance):
    assert isinstance(instance, droneDSLLib::EObject)

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

@given(instance=droneDSLLib::PourcentDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib::pourcentdecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib::PourcentDecl)

@given(instance=droneDSLLib::SecondeDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib::secondedecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib::SecondeDecl)

@given(instance=PourcentExp_strategy)
@settings(max_examples=50)
def test_pourcentexp_instantiation(instance):
    assert isinstance(instance, PourcentExp)

@given(instance=droneDSLLib::PourcentConst_strategy)
@settings(max_examples=50)
def test_dronedsllib::pourcentconst_instantiation(instance):
    assert isinstance(instance, droneDSLLib::PourcentConst)

@given(instance=droneDSLLib::PourcentConst_strategy)
def test_dronedsllib::pourcentconst_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=droneDSLLib::PourcentConst_strategy)
def test_dronedsllib::pourcentconst_val_setter(instance):
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

@given(instance=droneDSLLib::Pause_strategy)
@settings(max_examples=50)
def test_dronedsllib::pause_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Pause)

@given(instance=Mouvement_strategy)
@settings(max_examples=50)
def test_mouvement_instantiation(instance):
    assert isinstance(instance, Mouvement)

@given(instance=droneDSLLib::Droite_strategy)
@settings(max_examples=50)
def test_dronedsllib::droite_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Droite)

@given(instance=droneDSLLib::RotationDroite_strategy)
@settings(max_examples=50)
def test_dronedsllib::rotationdroite_instantiation(instance):
    assert isinstance(instance, droneDSLLib::RotationDroite)

@given(instance=droneDSLLib::Gauche_strategy)
@settings(max_examples=50)
def test_dronedsllib::gauche_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Gauche)

@given(instance=droneDSLLib::RotationGauche_strategy)
@settings(max_examples=50)
def test_dronedsllib::rotationgauche_instantiation(instance):
    assert isinstance(instance, droneDSLLib::RotationGauche)

@given(instance=droneDSLLib::Avancer_strategy)
@settings(max_examples=50)
def test_dronedsllib::avancer_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Avancer)

@given(instance=droneDSLLib::Parallele_strategy)
@settings(max_examples=50)
def test_dronedsllib::parallele_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Parallele)

@given(instance=droneDSLLib::Reculer_strategy)
@settings(max_examples=50)
def test_dronedsllib::reculer_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Reculer)

@given(instance=droneDSLLib::Descendre_strategy)
@settings(max_examples=50)
def test_dronedsllib::descendre_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Descendre)

@given(instance=droneDSLLib::Monter_strategy)
@settings(max_examples=50)
def test_dronedsllib::monter_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Monter)

@given(instance=DecollerAtterrir_strategy)
@settings(max_examples=50)
def test_decolleratterrir_instantiation(instance):
    assert isinstance(instance, DecollerAtterrir)

@given(instance=droneDSLLib::Atterrir_strategy)
@settings(max_examples=50)
def test_dronedsllib::atterrir_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Atterrir)

@given(instance=droneDSLLib::Decoller_strategy)
@settings(max_examples=50)
def test_dronedsllib::decoller_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Decoller)

@given(instance=droneDSLLib::SecondeExp_strategy)
@settings(max_examples=50)
def test_dronedsllib::secondeexp_instantiation(instance):
    assert isinstance(instance, droneDSLLib::SecondeExp)

@given(instance=droneDSLLib::PourcentExp_strategy)
@settings(max_examples=50)
def test_dronedsllib::pourcentexp_instantiation(instance):
    assert isinstance(instance, droneDSLLib::PourcentExp)

@given(instance=droneDSLLib::RefPourcentVar_strategy)
@settings(max_examples=50)
def test_dronedsllib::refpourcentvar_instantiation(instance):
    assert isinstance(instance, droneDSLLib::RefPourcentVar)

@given(instance=droneDSLLib::VarDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib::vardecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib::VarDecl)

@given(instance=droneDSLLib::VarDecl_strategy)
def test_dronedsllib::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=droneDSLLib::VarDecl_strategy)
def test_dronedsllib::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SecondeExp_strategy)
@settings(max_examples=50)
def test_secondeexp_instantiation(instance):
    assert isinstance(instance, SecondeExp)

@given(instance=droneDSLLib::RefSecondeVar_strategy)
@settings(max_examples=50)
def test_dronedsllib::refsecondevar_instantiation(instance):
    assert isinstance(instance, droneDSLLib::RefSecondeVar)

@given(instance=droneDSLLib::SecondeConst_strategy)
@settings(max_examples=50)
def test_dronedsllib::secondeconst_instantiation(instance):
    assert isinstance(instance, droneDSLLib::SecondeConst)

@given(instance=droneDSLLib::SecondeConst_strategy)
def test_dronedsllib::secondeconst_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=droneDSLLib::SecondeConst_strategy)
def test_dronedsllib::secondeconst_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=droneDSLLib::FonctionDecl_strategy)
@settings(max_examples=50)
def test_dronedsllib::fonctiondecl_instantiation(instance):
    assert isinstance(instance, droneDSLLib::FonctionDecl)

@given(instance=droneDSLLib::FonctionDecl_strategy)
def test_dronedsllib::fonctiondecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=droneDSLLib::FonctionDecl_strategy)
def test_dronedsllib::fonctiondecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=droneDSLLib::Model_strategy)
@settings(max_examples=50)
def test_dronedsllib::model_instantiation(instance):
    assert isinstance(instance, droneDSLLib::Model)

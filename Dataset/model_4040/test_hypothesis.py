import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::ElementNomme,
    smalluml::ElementDiagramme,
    Type,
    smalluml::Entier,
    smalluml::Chaine,
    smalluml::Booleen,
    smalluml::Type,
    ElementNomme,
    smalluml::Cardinalite,
    smalluml::Methode,
    smalluml::Attribut,
    ElementDiagramme,
    smalluml::TypeDonnee,
    smalluml::Diagramme,
    smalluml::Association,
    smalluml::Enumeration,
    smalluml::Classe,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::elementnomme_is_not_abstract():
    assert not inspect.isabstract(smalluml::ElementNomme)


def test_smalluml::elementnomme_constructor_exists():
    assert callable(smalluml::ElementNomme.__init__)


def test_smalluml::elementnomme_constructor_args():
    sig = inspect.signature(smalluml::ElementNomme.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_smalluml::elementnomme_has_nom():
    assert hasattr(smalluml::ElementNomme, "nom")
    descriptor = None
    for klass in smalluml::ElementNomme.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::elementdiagramme_is_not_abstract():
    assert not inspect.isabstract(smalluml::ElementDiagramme)


def test_smalluml::elementdiagramme_constructor_exists():
    assert callable(smalluml::ElementDiagramme.__init__)


def test_smalluml::elementdiagramme_constructor_args():
    sig = inspect.signature(smalluml::ElementDiagramme.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::entier_is_not_abstract():
    assert not inspect.isabstract(smalluml::Entier)


def test_smalluml::entier_constructor_exists():
    assert callable(smalluml::Entier.__init__)


def test_smalluml::entier_constructor_args():
    sig = inspect.signature(smalluml::Entier.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::chaine_is_not_abstract():
    assert not inspect.isabstract(smalluml::Chaine)


def test_smalluml::chaine_constructor_exists():
    assert callable(smalluml::Chaine.__init__)


def test_smalluml::chaine_constructor_args():
    sig = inspect.signature(smalluml::Chaine.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::booleen_is_not_abstract():
    assert not inspect.isabstract(smalluml::Booleen)


def test_smalluml::booleen_constructor_exists():
    assert callable(smalluml::Booleen.__init__)


def test_smalluml::booleen_constructor_args():
    sig = inspect.signature(smalluml::Booleen.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_elementnomme_is_not_abstract():
    assert not inspect.isabstract(ElementNomme)


def test_elementnomme_constructor_exists():
    assert callable(ElementNomme.__init__)


def test_elementnomme_constructor_args():
    sig = inspect.signature(ElementNomme.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::cardinalite_is_not_abstract():
    assert not inspect.isabstract(smalluml::Cardinalite)


def test_smalluml::cardinalite_constructor_exists():
    assert callable(smalluml::Cardinalite.__init__)


def test_smalluml::cardinalite_constructor_args():
    sig = inspect.signature(smalluml::Cardinalite.__init__)
    params = list(sig.parameters.keys())
    assert "multipliciteSup" in params, "Missing parameter 'multipliciteSup'"
    assert "multipliciteInf" in params, "Missing parameter 'multipliciteInf'"

def test_smalluml::cardinalite_has_multipliciteSup():
    assert hasattr(smalluml::Cardinalite, "multipliciteSup")
    descriptor = None
    for klass in smalluml::Cardinalite.__mro__:
        if "multipliciteSup" in klass.__dict__:
            descriptor = klass.__dict__["multipliciteSup"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::cardinalite_has_multipliciteInf():
    assert hasattr(smalluml::Cardinalite, "multipliciteInf")
    descriptor = None
    for klass in smalluml::Cardinalite.__mro__:
        if "multipliciteInf" in klass.__dict__:
            descriptor = klass.__dict__["multipliciteInf"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::methode_is_not_abstract():
    assert not inspect.isabstract(smalluml::Methode)


def test_smalluml::methode_constructor_exists():
    assert callable(smalluml::Methode.__init__)


def test_smalluml::methode_constructor_args():
    sig = inspect.signature(smalluml::Methode.__init__)
    params = list(sig.parameters.keys())
    assert "methodeAbstraite" in params, "Missing parameter 'methodeAbstraite'"

def test_smalluml::methode_has_methodeAbstraite():
    assert hasattr(smalluml::Methode, "methodeAbstraite")
    descriptor = None
    for klass in smalluml::Methode.__mro__:
        if "methodeAbstraite" in klass.__dict__:
            descriptor = klass.__dict__["methodeAbstraite"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::attribut_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribut)


def test_smalluml::attribut_constructor_exists():
    assert callable(smalluml::Attribut.__init__)


def test_smalluml::attribut_constructor_args():
    sig = inspect.signature(smalluml::Attribut.__init__)
    params = list(sig.parameters.keys())



def test_elementdiagramme_is_not_abstract():
    assert not inspect.isabstract(ElementDiagramme)


def test_elementdiagramme_constructor_exists():
    assert callable(ElementDiagramme.__init__)


def test_elementdiagramme_constructor_args():
    sig = inspect.signature(ElementDiagramme.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::typedonnee_is_not_abstract():
    assert not inspect.isabstract(smalluml::TypeDonnee)


def test_smalluml::typedonnee_constructor_exists():
    assert callable(smalluml::TypeDonnee.__init__)


def test_smalluml::typedonnee_constructor_args():
    sig = inspect.signature(smalluml::TypeDonnee.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::diagramme_is_not_abstract():
    assert not inspect.isabstract(smalluml::Diagramme)


def test_smalluml::diagramme_constructor_exists():
    assert callable(smalluml::Diagramme.__init__)


def test_smalluml::diagramme_constructor_args():
    sig = inspect.signature(smalluml::Diagramme.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::association_is_not_abstract():
    assert not inspect.isabstract(smalluml::Association)


def test_smalluml::association_constructor_exists():
    assert callable(smalluml::Association.__init__)


def test_smalluml::association_constructor_args():
    sig = inspect.signature(smalluml::Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_smalluml::enumeration_has_elements():
    assert hasattr(smalluml::Enumeration, "elements")
    descriptor = None
    for klass in smalluml::Enumeration.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::classe_is_not_abstract():
    assert not inspect.isabstract(smalluml::Classe)


def test_smalluml::classe_constructor_exists():
    assert callable(smalluml::Classe.__init__)


def test_smalluml::classe_constructor_args():
    sig = inspect.signature(smalluml::Classe.__init__)
    params = list(sig.parameters.keys())
    assert "classeAbstraite" in params, "Missing parameter 'classeAbstraite'"
    assert "abstrait" in params, "Missing parameter 'abstrait'"

def test_smalluml::classe_has_classeAbstraite():
    assert hasattr(smalluml::Classe, "classeAbstraite")
    descriptor = None
    for klass in smalluml::Classe.__mro__:
        if "classeAbstraite" in klass.__dict__:
            descriptor = klass.__dict__["classeAbstraite"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::classe_has_abstrait():
    assert hasattr(smalluml::Classe, "abstrait")
    descriptor = None
    for klass in smalluml::Classe.__mro__:
        if "abstrait" in klass.__dict__:
            descriptor = klass.__dict__["abstrait"]
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
smalluml::ElementNomme_strategy = st.builds(
    smalluml::ElementNomme,
    nom=
        safe_text
)
smalluml::ElementDiagramme_strategy = st.builds(
    smalluml::ElementDiagramme,
)
Type_strategy = st.builds(
    Type,
)
smalluml::Entier_strategy = st.builds(
    smalluml::Entier,
)
smalluml::Chaine_strategy = st.builds(
    smalluml::Chaine,
)
smalluml::Booleen_strategy = st.builds(
    smalluml::Booleen,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
ElementNomme_strategy = st.builds(
    ElementNomme,
)
smalluml::Cardinalite_strategy = st.builds(
    smalluml::Cardinalite,
    multipliciteSup=
        safe_text,
    multipliciteInf=
        safe_text
)
smalluml::Methode_strategy = st.builds(
    smalluml::Methode,
    methodeAbstraite=
        st.booleans()
)
smalluml::Attribut_strategy = st.builds(
    smalluml::Attribut,
)
ElementDiagramme_strategy = st.builds(
    ElementDiagramme,
)
smalluml::TypeDonnee_strategy = st.builds(
    smalluml::TypeDonnee,
)
smalluml::Diagramme_strategy = st.builds(
    smalluml::Diagramme,
)
smalluml::Association_strategy = st.builds(
    smalluml::Association,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
    elements=
        safe_text
)
smalluml::Classe_strategy = st.builds(
    smalluml::Classe,
    classeAbstraite=
        st.booleans(),
    abstrait=
        st.booleans()
)

@given(instance=smalluml::ElementNomme_strategy)
@settings(max_examples=50)
def test_smalluml::elementnomme_instantiation(instance):
    assert isinstance(instance, smalluml::ElementNomme)

@given(instance=smalluml::ElementNomme_strategy)
def test_smalluml::elementnomme_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=smalluml::ElementNomme_strategy)
def test_smalluml::elementnomme_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=smalluml::ElementDiagramme_strategy)
@settings(max_examples=50)
def test_smalluml::elementdiagramme_instantiation(instance):
    assert isinstance(instance, smalluml::ElementDiagramme)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::Entier_strategy)
@settings(max_examples=50)
def test_smalluml::entier_instantiation(instance):
    assert isinstance(instance, smalluml::Entier)

@given(instance=smalluml::Chaine_strategy)
@settings(max_examples=50)
def test_smalluml::chaine_instantiation(instance):
    assert isinstance(instance, smalluml::Chaine)

@given(instance=smalluml::Booleen_strategy)
@settings(max_examples=50)
def test_smalluml::booleen_instantiation(instance):
    assert isinstance(instance, smalluml::Booleen)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=ElementNomme_strategy)
@settings(max_examples=50)
def test_elementnomme_instantiation(instance):
    assert isinstance(instance, ElementNomme)

@given(instance=smalluml::Cardinalite_strategy)
@settings(max_examples=50)
def test_smalluml::cardinalite_instantiation(instance):
    assert isinstance(instance, smalluml::Cardinalite)

@given(instance=smalluml::Cardinalite_strategy)
def test_smalluml::cardinalite_multipliciteSup_type(instance):
    assert isinstance(instance.multipliciteSup, str)


@given(instance=smalluml::Cardinalite_strategy)
def test_smalluml::cardinalite_multipliciteSup_setter(instance):
    original = instance.multipliciteSup
    instance.multipliciteSup = original
    assert instance.multipliciteSup == original

@given(instance=smalluml::Cardinalite_strategy)
def test_smalluml::cardinalite_multipliciteInf_type(instance):
    assert isinstance(instance.multipliciteInf, str)


@given(instance=smalluml::Cardinalite_strategy)
def test_smalluml::cardinalite_multipliciteInf_setter(instance):
    original = instance.multipliciteInf
    instance.multipliciteInf = original
    assert instance.multipliciteInf == original

@given(instance=smalluml::Methode_strategy)
@settings(max_examples=50)
def test_smalluml::methode_instantiation(instance):
    assert isinstance(instance, smalluml::Methode)

@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_methodeAbstraite_type(instance):
    assert isinstance(instance.methodeAbstraite, bool)


@given(instance=smalluml::Methode_strategy)
def test_smalluml::methode_methodeAbstraite_setter(instance):
    original = instance.methodeAbstraite
    instance.methodeAbstraite = original
    assert instance.methodeAbstraite == original

@given(instance=smalluml::Attribut_strategy)
@settings(max_examples=50)
def test_smalluml::attribut_instantiation(instance):
    assert isinstance(instance, smalluml::Attribut)

@given(instance=ElementDiagramme_strategy)
@settings(max_examples=50)
def test_elementdiagramme_instantiation(instance):
    assert isinstance(instance, ElementDiagramme)

@given(instance=smalluml::TypeDonnee_strategy)
@settings(max_examples=50)
def test_smalluml::typedonnee_instantiation(instance):
    assert isinstance(instance, smalluml::TypeDonnee)

@given(instance=smalluml::Diagramme_strategy)
@settings(max_examples=50)
def test_smalluml::diagramme_instantiation(instance):
    assert isinstance(instance, smalluml::Diagramme)

@given(instance=smalluml::Association_strategy)
@settings(max_examples=50)
def test_smalluml::association_instantiation(instance):
    assert isinstance(instance, smalluml::Association)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_elements_type(instance):
    assert isinstance(instance.elements, str)


@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=smalluml::Classe_strategy)
@settings(max_examples=50)
def test_smalluml::classe_instantiation(instance):
    assert isinstance(instance, smalluml::Classe)

@given(instance=smalluml::Classe_strategy)
def test_smalluml::classe_classeAbstraite_type(instance):
    assert isinstance(instance.classeAbstraite, bool)


@given(instance=smalluml::Classe_strategy)
def test_smalluml::classe_classeAbstraite_setter(instance):
    original = instance.classeAbstraite
    instance.classeAbstraite = original
    assert instance.classeAbstraite == original

@given(instance=smalluml::Classe_strategy)
def test_smalluml::classe_abstrait_type(instance):
    assert isinstance(instance.abstrait, bool)


@given(instance=smalluml::Classe_strategy)
def test_smalluml::classe_abstrait_setter(instance):
    original = instance.abstrait
    instance.abstrait = original
    assert instance.abstrait == original

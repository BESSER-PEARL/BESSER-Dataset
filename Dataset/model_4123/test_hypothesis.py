import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::OpAccSucc,
    myDsl::OpConstructeur,
    myDsl::COMPARATEUR,
    myDsl::Lexpr,
    myDsl::ElemSimple,
    myDsl::AccSucc,
    myDsl::Condition,
    myDsl::Nop,
    myDsl::ForEach,
    myDsl::For,
    myDsl::While,
    myDsl::If,
    myDsl::Expression,
    myDsl::Variable,
    myDsl::Affectation,
    myDsl::ABin,
    myDsl::Nill,
    myDsl::Output,
    myDsl::Commandes,
    myDsl::Input,
    myDsl::Fonction,
    myDsl::Program,
    myDsl::EObject,
    myDsl::Commande,
    Condition,
    myDsl::Not,
    myDsl::ExprSimple,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::opaccsucc_is_not_abstract():
    assert not inspect.isabstract(myDsl::OpAccSucc)


def test_mydsl::opaccsucc_constructor_exists():
    assert callable(myDsl::OpAccSucc.__init__)


def test_mydsl::opaccsucc_constructor_args():
    sig = inspect.signature(myDsl::OpAccSucc.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::opaccsucc_has_op():
    assert hasattr(myDsl::OpAccSucc, "op")
    descriptor = None
    for klass in myDsl::OpAccSucc.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::opconstructeur_is_not_abstract():
    assert not inspect.isabstract(myDsl::OpConstructeur)


def test_mydsl::opconstructeur_constructor_exists():
    assert callable(myDsl::OpConstructeur.__init__)


def test_mydsl::opconstructeur_constructor_args():
    sig = inspect.signature(myDsl::OpConstructeur.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::opconstructeur_has_op():
    assert hasattr(myDsl::OpConstructeur, "op")
    descriptor = None
    for klass in myDsl::OpConstructeur.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::comparateur_is_not_abstract():
    assert not inspect.isabstract(myDsl::COMPARATEUR)


def test_mydsl::comparateur_constructor_exists():
    assert callable(myDsl::COMPARATEUR.__init__)


def test_mydsl::comparateur_constructor_args():
    sig = inspect.signature(myDsl::COMPARATEUR.__init__)
    params = list(sig.parameters.keys())
    assert "comparateur" in params, "Missing parameter 'comparateur'"

def test_mydsl::comparateur_has_comparateur():
    assert hasattr(myDsl::COMPARATEUR, "comparateur")
    descriptor = None
    for klass in myDsl::COMPARATEUR.__mro__:
        if "comparateur" in klass.__dict__:
            descriptor = klass.__dict__["comparateur"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl::Lexpr)


def test_mydsl::lexpr_constructor_exists():
    assert callable(myDsl::Lexpr.__init__)


def test_mydsl::lexpr_constructor_args():
    sig = inspect.signature(myDsl::Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::elemsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl::ElemSimple)


def test_mydsl::elemsimple_constructor_exists():
    assert callable(myDsl::ElemSimple.__init__)


def test_mydsl::elemsimple_constructor_args():
    sig = inspect.signature(myDsl::ElemSimple.__init__)
    params = list(sig.parameters.keys())
    assert "symb" in params, "Missing parameter 'symb'"

def test_mydsl::elemsimple_has_symb():
    assert hasattr(myDsl::ElemSimple, "symb")
    descriptor = None
    for klass in myDsl::ElemSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::accsucc_is_not_abstract():
    assert not inspect.isabstract(myDsl::AccSucc)


def test_mydsl::accsucc_constructor_exists():
    assert callable(myDsl::AccSucc.__init__)


def test_mydsl::accsucc_constructor_args():
    sig = inspect.signature(myDsl::AccSucc.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::condition_is_not_abstract():
    assert not inspect.isabstract(myDsl::Condition)


def test_mydsl::condition_constructor_exists():
    assert callable(myDsl::Condition.__init__)


def test_mydsl::condition_constructor_args():
    sig = inspect.signature(myDsl::Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::nop_is_not_abstract():
    assert not inspect.isabstract(myDsl::Nop)


def test_mydsl::nop_constructor_exists():
    assert callable(myDsl::Nop.__init__)


def test_mydsl::nop_constructor_args():
    sig = inspect.signature(myDsl::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_mydsl::nop_has_nop():
    assert hasattr(myDsl::Nop, "nop")
    descriptor = None
    for klass in myDsl::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::foreach_is_not_abstract():
    assert not inspect.isabstract(myDsl::ForEach)


def test_mydsl::foreach_constructor_exists():
    assert callable(myDsl::ForEach.__init__)


def test_mydsl::foreach_constructor_args():
    sig = inspect.signature(myDsl::ForEach.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::for_is_not_abstract():
    assert not inspect.isabstract(myDsl::For)


def test_mydsl::for_constructor_exists():
    assert callable(myDsl::For.__init__)


def test_mydsl::for_constructor_args():
    sig = inspect.signature(myDsl::For.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::while_is_not_abstract():
    assert not inspect.isabstract(myDsl::While)


def test_mydsl::while_constructor_exists():
    assert callable(myDsl::While.__init__)


def test_mydsl::while_constructor_args():
    sig = inspect.signature(myDsl::While.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::if_is_not_abstract():
    assert not inspect.isabstract(myDsl::If)


def test_mydsl::if_constructor_exists():
    assert callable(myDsl::If.__init__)


def test_mydsl::if_constructor_args():
    sig = inspect.signature(myDsl::If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::Expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::Expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::variable_is_not_abstract():
    assert not inspect.isabstract(myDsl::Variable)


def test_mydsl::variable_constructor_exists():
    assert callable(myDsl::Variable.__init__)


def test_mydsl::variable_constructor_args():
    sig = inspect.signature(myDsl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_mydsl::variable_has_variable():
    assert hasattr(myDsl::Variable, "variable")
    descriptor = None
    for klass in myDsl::Variable.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::affectation_is_not_abstract():
    assert not inspect.isabstract(myDsl::Affectation)


def test_mydsl::affectation_constructor_exists():
    assert callable(myDsl::Affectation.__init__)


def test_mydsl::affectation_constructor_args():
    sig = inspect.signature(myDsl::Affectation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::abin_is_not_abstract():
    assert not inspect.isabstract(myDsl::ABin)


def test_mydsl::abin_constructor_exists():
    assert callable(myDsl::ABin.__init__)


def test_mydsl::abin_constructor_args():
    sig = inspect.signature(myDsl::ABin.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::nill_is_not_abstract():
    assert not inspect.isabstract(myDsl::Nill)


def test_mydsl::nill_constructor_exists():
    assert callable(myDsl::Nill.__init__)


def test_mydsl::nill_constructor_args():
    sig = inspect.signature(myDsl::Nill.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"

def test_mydsl::nill_has_nil():
    assert hasattr(myDsl::Nill, "nil")
    descriptor = None
    for klass in myDsl::Nill.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::output_is_not_abstract():
    assert not inspect.isabstract(myDsl::Output)


def test_mydsl::output_constructor_exists():
    assert callable(myDsl::Output.__init__)


def test_mydsl::output_constructor_args():
    sig = inspect.signature(myDsl::Output.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"

def test_mydsl::output_has_out():
    assert hasattr(myDsl::Output, "out")
    descriptor = None
    for klass in myDsl::Output.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::commandes_is_not_abstract():
    assert not inspect.isabstract(myDsl::Commandes)


def test_mydsl::commandes_constructor_exists():
    assert callable(myDsl::Commandes.__init__)


def test_mydsl::commandes_constructor_args():
    sig = inspect.signature(myDsl::Commandes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::input_is_not_abstract():
    assert not inspect.isabstract(myDsl::Input)


def test_mydsl::input_constructor_exists():
    assert callable(myDsl::Input.__init__)


def test_mydsl::input_constructor_args():
    sig = inspect.signature(myDsl::Input.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_mydsl::input_has_in_():
    assert hasattr(myDsl::Input, "in_")
    descriptor = None
    for klass in myDsl::Input.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::fonction_is_not_abstract():
    assert not inspect.isabstract(myDsl::Fonction)


def test_mydsl::fonction_constructor_exists():
    assert callable(myDsl::Fonction.__init__)


def test_mydsl::fonction_constructor_args():
    sig = inspect.signature(myDsl::Fonction.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_mydsl::fonction_has_nom():
    assert hasattr(myDsl::Fonction, "nom")
    descriptor = None
    for klass in myDsl::Fonction.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::program_is_not_abstract():
    assert not inspect.isabstract(myDsl::Program)


def test_mydsl::program_constructor_exists():
    assert callable(myDsl::Program.__init__)


def test_mydsl::program_constructor_args():
    sig = inspect.signature(myDsl::Program.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::commande_is_not_abstract():
    assert not inspect.isabstract(myDsl::Commande)


def test_mydsl::commande_constructor_exists():
    assert callable(myDsl::Commande.__init__)


def test_mydsl::commande_constructor_args():
    sig = inspect.signature(myDsl::Commande.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::not_is_not_abstract():
    assert not inspect.isabstract(myDsl::Not)


def test_mydsl::not_constructor_exists():
    assert callable(myDsl::Not.__init__)


def test_mydsl::not_constructor_args():
    sig = inspect.signature(myDsl::Not.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_mydsl::not_has_not_():
    assert hasattr(myDsl::Not, "not_")
    descriptor = None
    for klass in myDsl::Not.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl::ExprSimple)


def test_mydsl::exprsimple_constructor_exists():
    assert callable(myDsl::ExprSimple.__init__)


def test_mydsl::exprsimple_constructor_args():
    sig = inspect.signature(myDsl::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "symb" in params, "Missing parameter 'symb'"

def test_mydsl::exprsimple_has_symb():
    assert hasattr(myDsl::ExprSimple, "symb")
    descriptor = None
    for klass in myDsl::ExprSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
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
myDsl::OpAccSucc_strategy = st.builds(
    myDsl::OpAccSucc,
    op=
        safe_text
)
myDsl::OpConstructeur_strategy = st.builds(
    myDsl::OpConstructeur,
    op=
        safe_text
)
myDsl::COMPARATEUR_strategy = st.builds(
    myDsl::COMPARATEUR,
    comparateur=
        safe_text
)
myDsl::Lexpr_strategy = st.builds(
    myDsl::Lexpr,
)
myDsl::ElemSimple_strategy = st.builds(
    myDsl::ElemSimple,
    symb=
        safe_text
)
myDsl::AccSucc_strategy = st.builds(
    myDsl::AccSucc,
)
myDsl::Condition_strategy = st.builds(
    myDsl::Condition,
)
myDsl::Nop_strategy = st.builds(
    myDsl::Nop,
    nop=
        safe_text
)
myDsl::ForEach_strategy = st.builds(
    myDsl::ForEach,
)
myDsl::For_strategy = st.builds(
    myDsl::For,
)
myDsl::While_strategy = st.builds(
    myDsl::While,
)
myDsl::If_strategy = st.builds(
    myDsl::If,
)
myDsl::Expression_strategy = st.builds(
    myDsl::Expression,
)
myDsl::Variable_strategy = st.builds(
    myDsl::Variable,
    variable=
        safe_text
)
myDsl::Affectation_strategy = st.builds(
    myDsl::Affectation,
)
myDsl::ABin_strategy = st.builds(
    myDsl::ABin,
)
myDsl::Nill_strategy = st.builds(
    myDsl::Nill,
    nil=
        safe_text
)
myDsl::Output_strategy = st.builds(
    myDsl::Output,
    out=
        safe_text
)
myDsl::Commandes_strategy = st.builds(
    myDsl::Commandes,
)
myDsl::Input_strategy = st.builds(
    myDsl::Input,
    in_=
        safe_text
)
myDsl::Fonction_strategy = st.builds(
    myDsl::Fonction,
    nom=
        safe_text
)
myDsl::Program_strategy = st.builds(
    myDsl::Program,
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
myDsl::Commande_strategy = st.builds(
    myDsl::Commande,
)
Condition_strategy = st.builds(
    Condition,
)
myDsl::Not_strategy = st.builds(
    myDsl::Not,
    not_=
        safe_text
)
myDsl::ExprSimple_strategy = st.builds(
    myDsl::ExprSimple,
    symb=
        safe_text
)

@given(instance=myDsl::OpAccSucc_strategy)
@settings(max_examples=50)
def test_mydsl::opaccsucc_instantiation(instance):
    assert isinstance(instance, myDsl::OpAccSucc)

@given(instance=myDsl::OpAccSucc_strategy)
def test_mydsl::opaccsucc_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::OpAccSucc_strategy)
def test_mydsl::opaccsucc_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::OpConstructeur_strategy)
@settings(max_examples=50)
def test_mydsl::opconstructeur_instantiation(instance):
    assert isinstance(instance, myDsl::OpConstructeur)

@given(instance=myDsl::OpConstructeur_strategy)
def test_mydsl::opconstructeur_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::OpConstructeur_strategy)
def test_mydsl::opconstructeur_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::COMPARATEUR_strategy)
@settings(max_examples=50)
def test_mydsl::comparateur_instantiation(instance):
    assert isinstance(instance, myDsl::COMPARATEUR)

@given(instance=myDsl::COMPARATEUR_strategy)
def test_mydsl::comparateur_comparateur_type(instance):
    assert isinstance(instance.comparateur, str)


@given(instance=myDsl::COMPARATEUR_strategy)
def test_mydsl::comparateur_comparateur_setter(instance):
    original = instance.comparateur
    instance.comparateur = original
    assert instance.comparateur == original

@given(instance=myDsl::Lexpr_strategy)
@settings(max_examples=50)
def test_mydsl::lexpr_instantiation(instance):
    assert isinstance(instance, myDsl::Lexpr)

@given(instance=myDsl::ElemSimple_strategy)
@settings(max_examples=50)
def test_mydsl::elemsimple_instantiation(instance):
    assert isinstance(instance, myDsl::ElemSimple)

@given(instance=myDsl::ElemSimple_strategy)
def test_mydsl::elemsimple_symb_type(instance):
    assert isinstance(instance.symb, str)


@given(instance=myDsl::ElemSimple_strategy)
def test_mydsl::elemsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

@given(instance=myDsl::AccSucc_strategy)
@settings(max_examples=50)
def test_mydsl::accsucc_instantiation(instance):
    assert isinstance(instance, myDsl::AccSucc)

@given(instance=myDsl::Condition_strategy)
@settings(max_examples=50)
def test_mydsl::condition_instantiation(instance):
    assert isinstance(instance, myDsl::Condition)

@given(instance=myDsl::Nop_strategy)
@settings(max_examples=50)
def test_mydsl::nop_instantiation(instance):
    assert isinstance(instance, myDsl::Nop)

@given(instance=myDsl::Nop_strategy)
def test_mydsl::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=myDsl::Nop_strategy)
def test_mydsl::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=myDsl::ForEach_strategy)
@settings(max_examples=50)
def test_mydsl::foreach_instantiation(instance):
    assert isinstance(instance, myDsl::ForEach)

@given(instance=myDsl::For_strategy)
@settings(max_examples=50)
def test_mydsl::for_instantiation(instance):
    assert isinstance(instance, myDsl::For)

@given(instance=myDsl::While_strategy)
@settings(max_examples=50)
def test_mydsl::while_instantiation(instance):
    assert isinstance(instance, myDsl::While)

@given(instance=myDsl::If_strategy)
@settings(max_examples=50)
def test_mydsl::if_instantiation(instance):
    assert isinstance(instance, myDsl::If)

@given(instance=myDsl::Expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::Expression)

@given(instance=myDsl::Variable_strategy)
@settings(max_examples=50)
def test_mydsl::variable_instantiation(instance):
    assert isinstance(instance, myDsl::Variable)

@given(instance=myDsl::Variable_strategy)
def test_mydsl::variable_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=myDsl::Variable_strategy)
def test_mydsl::variable_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl::Affectation_strategy)
@settings(max_examples=50)
def test_mydsl::affectation_instantiation(instance):
    assert isinstance(instance, myDsl::Affectation)

@given(instance=myDsl::ABin_strategy)
@settings(max_examples=50)
def test_mydsl::abin_instantiation(instance):
    assert isinstance(instance, myDsl::ABin)

@given(instance=myDsl::Nill_strategy)
@settings(max_examples=50)
def test_mydsl::nill_instantiation(instance):
    assert isinstance(instance, myDsl::Nill)

@given(instance=myDsl::Nill_strategy)
def test_mydsl::nill_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=myDsl::Nill_strategy)
def test_mydsl::nill_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=myDsl::Output_strategy)
@settings(max_examples=50)
def test_mydsl::output_instantiation(instance):
    assert isinstance(instance, myDsl::Output)

@given(instance=myDsl::Output_strategy)
def test_mydsl::output_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=myDsl::Output_strategy)
def test_mydsl::output_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=myDsl::Commandes_strategy)
@settings(max_examples=50)
def test_mydsl::commandes_instantiation(instance):
    assert isinstance(instance, myDsl::Commandes)

@given(instance=myDsl::Input_strategy)
@settings(max_examples=50)
def test_mydsl::input_instantiation(instance):
    assert isinstance(instance, myDsl::Input)

@given(instance=myDsl::Input_strategy)
def test_mydsl::input_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=myDsl::Input_strategy)
def test_mydsl::input_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=myDsl::Fonction_strategy)
@settings(max_examples=50)
def test_mydsl::fonction_instantiation(instance):
    assert isinstance(instance, myDsl::Fonction)

@given(instance=myDsl::Fonction_strategy)
def test_mydsl::fonction_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=myDsl::Fonction_strategy)
def test_mydsl::fonction_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=myDsl::Program_strategy)
@settings(max_examples=50)
def test_mydsl::program_instantiation(instance):
    assert isinstance(instance, myDsl::Program)

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=myDsl::Commande_strategy)
@settings(max_examples=50)
def test_mydsl::commande_instantiation(instance):
    assert isinstance(instance, myDsl::Commande)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=myDsl::Not_strategy)
@settings(max_examples=50)
def test_mydsl::not_instantiation(instance):
    assert isinstance(instance, myDsl::Not)

@given(instance=myDsl::Not_strategy)
def test_mydsl::not_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=myDsl::Not_strategy)
def test_mydsl::not_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=myDsl::ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl::exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl::ExprSimple)

@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_symb_type(instance):
    assert isinstance(instance.symb, str)


@given(instance=myDsl::ExprSimple_strategy)
def test_mydsl::exprsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

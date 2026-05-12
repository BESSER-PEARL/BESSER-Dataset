import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_OpAccSucc,
    myDsl_OpConstructeur,
    myDsl_COMPARATEUR,
    myDsl_Lexpr,
    myDsl_ElemSimple,
    myDsl_AccSucc,
    Condition,
    myDsl_Not,
    myDsl_ExprSimple,
    myDsl_Condition,
    myDsl_Nop,
    myDsl_ForEach,
    myDsl_For,
    myDsl_While,
    myDsl_If,
    myDsl_Expression,
    myDsl_Variable,
    myDsl_Affectation,
    myDsl_ABin,
    myDsl_Nill,
    myDsl_Output,
    myDsl_Commandes,
    myDsl_Input,
    myDsl_Fonction,
    myDsl_Program,
    myDsl_EObject,
    myDsl_Commande,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_opaccsucc_is_not_abstract():
    assert not inspect.isabstract(myDsl_OpAccSucc)


def test_mydsl_opaccsucc_constructor_exists():
    assert callable(myDsl_OpAccSucc.__init__)


def test_mydsl_opaccsucc_constructor_args():
    sig = inspect.signature(myDsl_OpAccSucc.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_opaccsucc_has_op():
    assert hasattr(myDsl_OpAccSucc, "op")
    descriptor = None
    for klass in myDsl_OpAccSucc.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_opconstructeur_is_not_abstract():
    assert not inspect.isabstract(myDsl_OpConstructeur)


def test_mydsl_opconstructeur_constructor_exists():
    assert callable(myDsl_OpConstructeur.__init__)


def test_mydsl_opconstructeur_constructor_args():
    sig = inspect.signature(myDsl_OpConstructeur.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_opconstructeur_has_op():
    assert hasattr(myDsl_OpConstructeur, "op")
    descriptor = None
    for klass in myDsl_OpConstructeur.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_comparateur_is_not_abstract():
    assert not inspect.isabstract(myDsl_COMPARATEUR)


def test_mydsl_comparateur_constructor_exists():
    assert callable(myDsl_COMPARATEUR.__init__)


def test_mydsl_comparateur_constructor_args():
    sig = inspect.signature(myDsl_COMPARATEUR.__init__)
    params = list(sig.parameters.keys())
    assert "comparateur" in params, "Missing parameter 'comparateur'"

def test_mydsl_comparateur_has_comparateur():
    assert hasattr(myDsl_COMPARATEUR, "comparateur")
    descriptor = None
    for klass in myDsl_COMPARATEUR.__mro__:
        if "comparateur" in klass.__dict__:
            descriptor = klass.__dict__["comparateur"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_lexpr_is_not_abstract():
    assert not inspect.isabstract(myDsl_Lexpr)


def test_mydsl_lexpr_constructor_exists():
    assert callable(myDsl_Lexpr.__init__)


def test_mydsl_lexpr_constructor_args():
    sig = inspect.signature(myDsl_Lexpr.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_elemsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl_ElemSimple)


def test_mydsl_elemsimple_constructor_exists():
    assert callable(myDsl_ElemSimple.__init__)


def test_mydsl_elemsimple_constructor_args():
    sig = inspect.signature(myDsl_ElemSimple.__init__)
    params = list(sig.parameters.keys())
    assert "symb" in params, "Missing parameter 'symb'"

def test_mydsl_elemsimple_has_symb():
    assert hasattr(myDsl_ElemSimple, "symb")
    descriptor = None
    for klass in myDsl_ElemSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_accsucc_is_not_abstract():
    assert not inspect.isabstract(myDsl_AccSucc)


def test_mydsl_accsucc_constructor_exists():
    assert callable(myDsl_AccSucc.__init__)


def test_mydsl_accsucc_constructor_args():
    sig = inspect.signature(myDsl_AccSucc.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_not_is_not_abstract():
    assert not inspect.isabstract(myDsl_Not)


def test_mydsl_not_constructor_exists():
    assert callable(myDsl_Not.__init__)


def test_mydsl_not_constructor_args():
    sig = inspect.signature(myDsl_Not.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_mydsl_not_has_not_():
    assert hasattr(myDsl_Not, "not_")
    descriptor = None
    for klass in myDsl_Not.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_exprsimple_is_not_abstract():
    assert not inspect.isabstract(myDsl_ExprSimple)


def test_mydsl_exprsimple_constructor_exists():
    assert callable(myDsl_ExprSimple.__init__)


def test_mydsl_exprsimple_constructor_args():
    sig = inspect.signature(myDsl_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "symb" in params, "Missing parameter 'symb'"

def test_mydsl_exprsimple_has_symb():
    assert hasattr(myDsl_ExprSimple, "symb")
    descriptor = None
    for klass in myDsl_ExprSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_condition_is_not_abstract():
    assert not inspect.isabstract(myDsl_Condition)


def test_mydsl_condition_constructor_exists():
    assert callable(myDsl_Condition.__init__)


def test_mydsl_condition_constructor_args():
    sig = inspect.signature(myDsl_Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_nop_is_not_abstract():
    assert not inspect.isabstract(myDsl_Nop)


def test_mydsl_nop_constructor_exists():
    assert callable(myDsl_Nop.__init__)


def test_mydsl_nop_constructor_args():
    sig = inspect.signature(myDsl_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_mydsl_nop_has_nop():
    assert hasattr(myDsl_Nop, "nop")
    descriptor = None
    for klass in myDsl_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_foreach_is_not_abstract():
    assert not inspect.isabstract(myDsl_ForEach)


def test_mydsl_foreach_constructor_exists():
    assert callable(myDsl_ForEach.__init__)


def test_mydsl_foreach_constructor_args():
    sig = inspect.signature(myDsl_ForEach.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_for_is_not_abstract():
    assert not inspect.isabstract(myDsl_For)


def test_mydsl_for_constructor_exists():
    assert callable(myDsl_For.__init__)


def test_mydsl_for_constructor_args():
    sig = inspect.signature(myDsl_For.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_while_is_not_abstract():
    assert not inspect.isabstract(myDsl_While)


def test_mydsl_while_constructor_exists():
    assert callable(myDsl_While.__init__)


def test_mydsl_while_constructor_args():
    sig = inspect.signature(myDsl_While.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_if_is_not_abstract():
    assert not inspect.isabstract(myDsl_If)


def test_mydsl_if_constructor_exists():
    assert callable(myDsl_If.__init__)


def test_mydsl_if_constructor_args():
    sig = inspect.signature(myDsl_If.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_variable_is_not_abstract():
    assert not inspect.isabstract(myDsl_Variable)


def test_mydsl_variable_constructor_exists():
    assert callable(myDsl_Variable.__init__)


def test_mydsl_variable_constructor_args():
    sig = inspect.signature(myDsl_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_mydsl_variable_has_variable():
    assert hasattr(myDsl_Variable, "variable")
    descriptor = None
    for klass in myDsl_Variable.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_affectation_is_not_abstract():
    assert not inspect.isabstract(myDsl_Affectation)


def test_mydsl_affectation_constructor_exists():
    assert callable(myDsl_Affectation.__init__)


def test_mydsl_affectation_constructor_args():
    sig = inspect.signature(myDsl_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_abin_is_not_abstract():
    assert not inspect.isabstract(myDsl_ABin)


def test_mydsl_abin_constructor_exists():
    assert callable(myDsl_ABin.__init__)


def test_mydsl_abin_constructor_args():
    sig = inspect.signature(myDsl_ABin.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_nill_is_not_abstract():
    assert not inspect.isabstract(myDsl_Nill)


def test_mydsl_nill_constructor_exists():
    assert callable(myDsl_Nill.__init__)


def test_mydsl_nill_constructor_args():
    sig = inspect.signature(myDsl_Nill.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"

def test_mydsl_nill_has_nil():
    assert hasattr(myDsl_Nill, "nil")
    descriptor = None
    for klass in myDsl_Nill.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_output_is_not_abstract():
    assert not inspect.isabstract(myDsl_Output)


def test_mydsl_output_constructor_exists():
    assert callable(myDsl_Output.__init__)


def test_mydsl_output_constructor_args():
    sig = inspect.signature(myDsl_Output.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"

def test_mydsl_output_has_out():
    assert hasattr(myDsl_Output, "out")
    descriptor = None
    for klass in myDsl_Output.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_commandes_is_not_abstract():
    assert not inspect.isabstract(myDsl_Commandes)


def test_mydsl_commandes_constructor_exists():
    assert callable(myDsl_Commandes.__init__)


def test_mydsl_commandes_constructor_args():
    sig = inspect.signature(myDsl_Commandes.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_input_is_not_abstract():
    assert not inspect.isabstract(myDsl_Input)


def test_mydsl_input_constructor_exists():
    assert callable(myDsl_Input.__init__)


def test_mydsl_input_constructor_args():
    sig = inspect.signature(myDsl_Input.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_mydsl_input_has_in_():
    assert hasattr(myDsl_Input, "in_")
    descriptor = None
    for klass in myDsl_Input.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_fonction_is_not_abstract():
    assert not inspect.isabstract(myDsl_Fonction)


def test_mydsl_fonction_constructor_exists():
    assert callable(myDsl_Fonction.__init__)


def test_mydsl_fonction_constructor_args():
    sig = inspect.signature(myDsl_Fonction.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_mydsl_fonction_has_nom():
    assert hasattr(myDsl_Fonction, "nom")
    descriptor = None
    for klass in myDsl_Fonction.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_program_is_not_abstract():
    assert not inspect.isabstract(myDsl_Program)


def test_mydsl_program_constructor_exists():
    assert callable(myDsl_Program.__init__)


def test_mydsl_program_constructor_args():
    sig = inspect.signature(myDsl_Program.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl_EObject)


def test_mydsl_eobject_constructor_exists():
    assert callable(myDsl_EObject.__init__)


def test_mydsl_eobject_constructor_args():
    sig = inspect.signature(myDsl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_commande_is_not_abstract():
    assert not inspect.isabstract(myDsl_Commande)


def test_mydsl_commande_constructor_exists():
    assert callable(myDsl_Commande.__init__)


def test_mydsl_commande_constructor_args():
    sig = inspect.signature(myDsl_Commande.__init__)
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
myDsl_OpAccSucc_strategy = st.builds(
    myDsl_OpAccSucc,
    op=
        safe_text
)
myDsl_OpConstructeur_strategy = st.builds(
    myDsl_OpConstructeur,
    op=
        safe_text
)
myDsl_COMPARATEUR_strategy = st.builds(
    myDsl_COMPARATEUR,
    comparateur=
        safe_text
)
myDsl_Lexpr_strategy = st.builds(
    myDsl_Lexpr,
)
myDsl_ElemSimple_strategy = st.builds(
    myDsl_ElemSimple,
    symb=
        safe_text
)
myDsl_AccSucc_strategy = st.builds(
    myDsl_AccSucc,
)
Condition_strategy = st.builds(
    Condition,
)
myDsl_Not_strategy = st.builds(
    myDsl_Not,
    not_=
        safe_text
)
myDsl_ExprSimple_strategy = st.builds(
    myDsl_ExprSimple,
    symb=
        safe_text
)
myDsl_Condition_strategy = st.builds(
    myDsl_Condition,
)
myDsl_Nop_strategy = st.builds(
    myDsl_Nop,
    nop=
        safe_text
)
myDsl_ForEach_strategy = st.builds(
    myDsl_ForEach,
)
myDsl_For_strategy = st.builds(
    myDsl_For,
)
myDsl_While_strategy = st.builds(
    myDsl_While,
)
myDsl_If_strategy = st.builds(
    myDsl_If,
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
)
myDsl_Variable_strategy = st.builds(
    myDsl_Variable,
    variable=
        safe_text
)
myDsl_Affectation_strategy = st.builds(
    myDsl_Affectation,
)
myDsl_ABin_strategy = st.builds(
    myDsl_ABin,
)
myDsl_Nill_strategy = st.builds(
    myDsl_Nill,
    nil=
        safe_text
)
myDsl_Output_strategy = st.builds(
    myDsl_Output,
    out=
        safe_text
)
myDsl_Commandes_strategy = st.builds(
    myDsl_Commandes,
)
myDsl_Input_strategy = st.builds(
    myDsl_Input,
    in_=
        safe_text
)
myDsl_Fonction_strategy = st.builds(
    myDsl_Fonction,
    nom=
        safe_text
)
myDsl_Program_strategy = st.builds(
    myDsl_Program,
)
myDsl_EObject_strategy = st.builds(
    myDsl_EObject,
)
myDsl_Commande_strategy = st.builds(
    myDsl_Commande,
)

@given(instance=myDsl_OpAccSucc_strategy)
@settings(max_examples=50)
def test_mydsl_opaccsucc_instantiation(instance):
    assert isinstance(instance, myDsl_OpAccSucc)



@given(instance=myDsl_OpAccSucc_strategy)
def test_mydsl_opaccsucc_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_OpConstructeur_strategy)
@settings(max_examples=50)
def test_mydsl_opconstructeur_instantiation(instance):
    assert isinstance(instance, myDsl_OpConstructeur)



@given(instance=myDsl_OpConstructeur_strategy)
def test_mydsl_opconstructeur_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_COMPARATEUR_strategy)
@settings(max_examples=50)
def test_mydsl_comparateur_instantiation(instance):
    assert isinstance(instance, myDsl_COMPARATEUR)



@given(instance=myDsl_COMPARATEUR_strategy)
def test_mydsl_comparateur_comparateur_setter(instance):
    original = instance.comparateur
    instance.comparateur = original
    assert instance.comparateur == original

@given(instance=myDsl_Lexpr_strategy)
@settings(max_examples=50)
def test_mydsl_lexpr_instantiation(instance):
    assert isinstance(instance, myDsl_Lexpr)

@given(instance=myDsl_ElemSimple_strategy)
@settings(max_examples=50)
def test_mydsl_elemsimple_instantiation(instance):
    assert isinstance(instance, myDsl_ElemSimple)



@given(instance=myDsl_ElemSimple_strategy)
def test_mydsl_elemsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

@given(instance=myDsl_AccSucc_strategy)
@settings(max_examples=50)
def test_mydsl_accsucc_instantiation(instance):
    assert isinstance(instance, myDsl_AccSucc)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=myDsl_Not_strategy)
@settings(max_examples=50)
def test_mydsl_not_instantiation(instance):
    assert isinstance(instance, myDsl_Not)



@given(instance=myDsl_Not_strategy)
def test_mydsl_not_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=myDsl_ExprSimple_strategy)
@settings(max_examples=50)
def test_mydsl_exprsimple_instantiation(instance):
    assert isinstance(instance, myDsl_ExprSimple)



@given(instance=myDsl_ExprSimple_strategy)
def test_mydsl_exprsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

@given(instance=myDsl_Condition_strategy)
@settings(max_examples=50)
def test_mydsl_condition_instantiation(instance):
    assert isinstance(instance, myDsl_Condition)

@given(instance=myDsl_Nop_strategy)
@settings(max_examples=50)
def test_mydsl_nop_instantiation(instance):
    assert isinstance(instance, myDsl_Nop)



@given(instance=myDsl_Nop_strategy)
def test_mydsl_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=myDsl_ForEach_strategy)
@settings(max_examples=50)
def test_mydsl_foreach_instantiation(instance):
    assert isinstance(instance, myDsl_ForEach)

@given(instance=myDsl_For_strategy)
@settings(max_examples=50)
def test_mydsl_for_instantiation(instance):
    assert isinstance(instance, myDsl_For)

@given(instance=myDsl_While_strategy)
@settings(max_examples=50)
def test_mydsl_while_instantiation(instance):
    assert isinstance(instance, myDsl_While)

@given(instance=myDsl_If_strategy)
@settings(max_examples=50)
def test_mydsl_if_instantiation(instance):
    assert isinstance(instance, myDsl_If)

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)

@given(instance=myDsl_Variable_strategy)
@settings(max_examples=50)
def test_mydsl_variable_instantiation(instance):
    assert isinstance(instance, myDsl_Variable)



@given(instance=myDsl_Variable_strategy)
def test_mydsl_variable_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl_Affectation_strategy)
@settings(max_examples=50)
def test_mydsl_affectation_instantiation(instance):
    assert isinstance(instance, myDsl_Affectation)

@given(instance=myDsl_ABin_strategy)
@settings(max_examples=50)
def test_mydsl_abin_instantiation(instance):
    assert isinstance(instance, myDsl_ABin)

@given(instance=myDsl_Nill_strategy)
@settings(max_examples=50)
def test_mydsl_nill_instantiation(instance):
    assert isinstance(instance, myDsl_Nill)



@given(instance=myDsl_Nill_strategy)
def test_mydsl_nill_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=myDsl_Output_strategy)
@settings(max_examples=50)
def test_mydsl_output_instantiation(instance):
    assert isinstance(instance, myDsl_Output)



@given(instance=myDsl_Output_strategy)
def test_mydsl_output_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=myDsl_Commandes_strategy)
@settings(max_examples=50)
def test_mydsl_commandes_instantiation(instance):
    assert isinstance(instance, myDsl_Commandes)

@given(instance=myDsl_Input_strategy)
@settings(max_examples=50)
def test_mydsl_input_instantiation(instance):
    assert isinstance(instance, myDsl_Input)



@given(instance=myDsl_Input_strategy)
def test_mydsl_input_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=myDsl_Fonction_strategy)
@settings(max_examples=50)
def test_mydsl_fonction_instantiation(instance):
    assert isinstance(instance, myDsl_Fonction)



@given(instance=myDsl_Fonction_strategy)
def test_mydsl_fonction_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=myDsl_Program_strategy)
@settings(max_examples=50)
def test_mydsl_program_instantiation(instance):
    assert isinstance(instance, myDsl_Program)

@given(instance=myDsl_EObject_strategy)
@settings(max_examples=50)
def test_mydsl_eobject_instantiation(instance):
    assert isinstance(instance, myDsl_EObject)

@given(instance=myDsl_Commande_strategy)
@settings(max_examples=50)
def test_mydsl_commande_instantiation(instance):
    assert isinstance(instance, myDsl_Commande)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Collection,
    problog_PLTuple,
    problog_PLList,
    ProbabilityMeasure,
    problog_ProbabilityFraction,
    problog_ProbabilityLiteral,
    problog_ProbabilityMeasure,
    Proposition,
    problog_Annotatable,
    problog_AnnotatedReferable,
    Annotatable,
    Referable,
    problog_Variable,
    problog_Atom,
    problog_Collection,
    problog_TermInstance,
    problog_Term,
    problog_Statement,
    problog_ProbLogProgram,
    problog_Referable,
    problog_Proposition,
    ProbLogStatement,
    problog_Query,
    problog_Evidence,
    problog_RHS,
    problog_LHS,
    Statement,
    problog_ProbLogStatement,
    problog_ImportLibrary,
    problog_Cheat,
    problog_Comment,
    problog_Rule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())



def test_problog_pltuple_is_not_abstract():
    assert not inspect.isabstract(problog_PLTuple)


def test_problog_pltuple_constructor_exists():
    assert callable(problog_PLTuple.__init__)


def test_problog_pltuple_constructor_args():
    sig = inspect.signature(problog_PLTuple.__init__)
    params = list(sig.parameters.keys())



def test_problog_pllist_is_not_abstract():
    assert not inspect.isabstract(problog_PLList)


def test_problog_pllist_constructor_exists():
    assert callable(problog_PLList.__init__)


def test_problog_pllist_constructor_args():
    sig = inspect.signature(problog_PLList.__init__)
    params = list(sig.parameters.keys())



def test_probabilitymeasure_is_not_abstract():
    assert not inspect.isabstract(ProbabilityMeasure)


def test_probabilitymeasure_constructor_exists():
    assert callable(ProbabilityMeasure.__init__)


def test_probabilitymeasure_constructor_args():
    sig = inspect.signature(ProbabilityMeasure.__init__)
    params = list(sig.parameters.keys())



def test_problog_probabilityfraction_is_not_abstract():
    assert not inspect.isabstract(problog_ProbabilityFraction)


def test_problog_probabilityfraction_constructor_exists():
    assert callable(problog_ProbabilityFraction.__init__)


def test_problog_probabilityfraction_constructor_args():
    sig = inspect.signature(problog_ProbabilityFraction.__init__)
    params = list(sig.parameters.keys())
    assert "nominator" in params, "Missing parameter 'nominator'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_problog_probabilityfraction_has_nominator():
    assert hasattr(problog_ProbabilityFraction, "nominator")
    descriptor = None
    for klass in problog_ProbabilityFraction.__mro__:
        if "nominator" in klass.__dict__:
            descriptor = klass.__dict__["nominator"]
            break
    assert isinstance(descriptor, property)

def test_problog_probabilityfraction_has_denominator():
    assert hasattr(problog_ProbabilityFraction, "denominator")
    descriptor = None
    for klass in problog_ProbabilityFraction.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_problog_probabilityliteral_is_not_abstract():
    assert not inspect.isabstract(problog_ProbabilityLiteral)


def test_problog_probabilityliteral_constructor_exists():
    assert callable(problog_ProbabilityLiteral.__init__)


def test_problog_probabilityliteral_constructor_args():
    sig = inspect.signature(problog_ProbabilityLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_problog_probabilityliteral_has_value():
    assert hasattr(problog_ProbabilityLiteral, "value")
    descriptor = None
    for klass in problog_ProbabilityLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_problog_probabilitymeasure_is_not_abstract():
    assert not inspect.isabstract(problog_ProbabilityMeasure)


def test_problog_probabilitymeasure_constructor_exists():
    assert callable(problog_ProbabilityMeasure.__init__)


def test_problog_probabilitymeasure_constructor_args():
    sig = inspect.signature(problog_ProbabilityMeasure.__init__)
    params = list(sig.parameters.keys())



def test_proposition_is_not_abstract():
    assert not inspect.isabstract(Proposition)


def test_proposition_constructor_exists():
    assert callable(Proposition.__init__)


def test_proposition_constructor_args():
    sig = inspect.signature(Proposition.__init__)
    params = list(sig.parameters.keys())



def test_problog_annotatable_is_not_abstract():
    assert not inspect.isabstract(problog_Annotatable)


def test_problog_annotatable_constructor_exists():
    assert callable(problog_Annotatable.__init__)


def test_problog_annotatable_constructor_args():
    sig = inspect.signature(problog_Annotatable.__init__)
    params = list(sig.parameters.keys())



def test_problog_annotatedreferable_is_not_abstract():
    assert not inspect.isabstract(problog_AnnotatedReferable)


def test_problog_annotatedreferable_constructor_exists():
    assert callable(problog_AnnotatedReferable.__init__)


def test_problog_annotatedreferable_constructor_args():
    sig = inspect.signature(problog_AnnotatedReferable.__init__)
    params = list(sig.parameters.keys())



def test_annotatable_is_not_abstract():
    assert not inspect.isabstract(Annotatable)


def test_annotatable_constructor_exists():
    assert callable(Annotatable.__init__)


def test_annotatable_constructor_args():
    sig = inspect.signature(Annotatable.__init__)
    params = list(sig.parameters.keys())



def test_referable_is_not_abstract():
    assert not inspect.isabstract(Referable)


def test_referable_constructor_exists():
    assert callable(Referable.__init__)


def test_referable_constructor_args():
    sig = inspect.signature(Referable.__init__)
    params = list(sig.parameters.keys())



def test_problog_variable_is_not_abstract():
    assert not inspect.isabstract(problog_Variable)


def test_problog_variable_constructor_exists():
    assert callable(problog_Variable.__init__)


def test_problog_variable_constructor_args():
    sig = inspect.signature(problog_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog_variable_has_name():
    assert hasattr(problog_Variable, "name")
    descriptor = None
    for klass in problog_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog_atom_is_not_abstract():
    assert not inspect.isabstract(problog_Atom)


def test_problog_atom_constructor_exists():
    assert callable(problog_Atom.__init__)


def test_problog_atom_constructor_args():
    sig = inspect.signature(problog_Atom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog_atom_has_name():
    assert hasattr(problog_Atom, "name")
    descriptor = None
    for klass in problog_Atom.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog_collection_is_not_abstract():
    assert not inspect.isabstract(problog_Collection)


def test_problog_collection_constructor_exists():
    assert callable(problog_Collection.__init__)


def test_problog_collection_constructor_args():
    sig = inspect.signature(problog_Collection.__init__)
    params = list(sig.parameters.keys())



def test_problog_terminstance_is_not_abstract():
    assert not inspect.isabstract(problog_TermInstance)


def test_problog_terminstance_constructor_exists():
    assert callable(problog_TermInstance.__init__)


def test_problog_terminstance_constructor_args():
    sig = inspect.signature(problog_TermInstance.__init__)
    params = list(sig.parameters.keys())



def test_problog_term_is_not_abstract():
    assert not inspect.isabstract(problog_Term)


def test_problog_term_constructor_exists():
    assert callable(problog_Term.__init__)


def test_problog_term_constructor_args():
    sig = inspect.signature(problog_Term.__init__)
    params = list(sig.parameters.keys())
    assert "arguments" in params, "Missing parameter 'arguments'"
    assert "name" in params, "Missing parameter 'name'"

def test_problog_term_has_arguments():
    assert hasattr(problog_Term, "arguments")
    descriptor = None
    for klass in problog_Term.__mro__:
        if "arguments" in klass.__dict__:
            descriptor = klass.__dict__["arguments"]
            break
    assert isinstance(descriptor, property)

def test_problog_term_has_name():
    assert hasattr(problog_Term, "name")
    descriptor = None
    for klass in problog_Term.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog_statement_is_not_abstract():
    assert not inspect.isabstract(problog_Statement)


def test_problog_statement_constructor_exists():
    assert callable(problog_Statement.__init__)


def test_problog_statement_constructor_args():
    sig = inspect.signature(problog_Statement.__init__)
    params = list(sig.parameters.keys())



def test_problog_problogprogram_is_not_abstract():
    assert not inspect.isabstract(problog_ProbLogProgram)


def test_problog_problogprogram_constructor_exists():
    assert callable(problog_ProbLogProgram.__init__)


def test_problog_problogprogram_constructor_args():
    sig = inspect.signature(problog_ProbLogProgram.__init__)
    params = list(sig.parameters.keys())



def test_problog_referable_is_not_abstract():
    assert not inspect.isabstract(problog_Referable)


def test_problog_referable_constructor_exists():
    assert callable(problog_Referable.__init__)


def test_problog_referable_constructor_args():
    sig = inspect.signature(problog_Referable.__init__)
    params = list(sig.parameters.keys())



def test_problog_proposition_is_not_abstract():
    assert not inspect.isabstract(problog_Proposition)


def test_problog_proposition_constructor_exists():
    assert callable(problog_Proposition.__init__)


def test_problog_proposition_constructor_args():
    sig = inspect.signature(problog_Proposition.__init__)
    params = list(sig.parameters.keys())



def test_problogstatement_is_not_abstract():
    assert not inspect.isabstract(ProbLogStatement)


def test_problogstatement_constructor_exists():
    assert callable(ProbLogStatement.__init__)


def test_problogstatement_constructor_args():
    sig = inspect.signature(ProbLogStatement.__init__)
    params = list(sig.parameters.keys())



def test_problog_query_is_not_abstract():
    assert not inspect.isabstract(problog_Query)


def test_problog_query_constructor_exists():
    assert callable(problog_Query.__init__)


def test_problog_query_constructor_args():
    sig = inspect.signature(problog_Query.__init__)
    params = list(sig.parameters.keys())



def test_problog_evidence_is_not_abstract():
    assert not inspect.isabstract(problog_Evidence)


def test_problog_evidence_constructor_exists():
    assert callable(problog_Evidence.__init__)


def test_problog_evidence_constructor_args():
    sig = inspect.signature(problog_Evidence.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_problog_evidence_has_value():
    assert hasattr(problog_Evidence, "value")
    descriptor = None
    for klass in problog_Evidence.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_problog_rhs_is_not_abstract():
    assert not inspect.isabstract(problog_RHS)


def test_problog_rhs_constructor_exists():
    assert callable(problog_RHS.__init__)


def test_problog_rhs_constructor_args():
    sig = inspect.signature(problog_RHS.__init__)
    params = list(sig.parameters.keys())



def test_problog_lhs_is_not_abstract():
    assert not inspect.isabstract(problog_LHS)


def test_problog_lhs_constructor_exists():
    assert callable(problog_LHS.__init__)


def test_problog_lhs_constructor_args():
    sig = inspect.signature(problog_LHS.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_problog_problogstatement_is_not_abstract():
    assert not inspect.isabstract(problog_ProbLogStatement)


def test_problog_problogstatement_constructor_exists():
    assert callable(problog_ProbLogStatement.__init__)


def test_problog_problogstatement_constructor_args():
    sig = inspect.signature(problog_ProbLogStatement.__init__)
    params = list(sig.parameters.keys())



def test_problog_importlibrary_is_not_abstract():
    assert not inspect.isabstract(problog_ImportLibrary)


def test_problog_importlibrary_constructor_exists():
    assert callable(problog_ImportLibrary.__init__)


def test_problog_importlibrary_constructor_args():
    sig = inspect.signature(problog_ImportLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog_importlibrary_has_name():
    assert hasattr(problog_ImportLibrary, "name")
    descriptor = None
    for klass in problog_ImportLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog_cheat_is_not_abstract():
    assert not inspect.isabstract(problog_Cheat)


def test_problog_cheat_constructor_exists():
    assert callable(problog_Cheat.__init__)


def test_problog_cheat_constructor_args():
    sig = inspect.signature(problog_Cheat.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_problog_cheat_has_contents():
    assert hasattr(problog_Cheat, "contents")
    descriptor = None
    for klass in problog_Cheat.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)



def test_problog_comment_is_not_abstract():
    assert not inspect.isabstract(problog_Comment)


def test_problog_comment_constructor_exists():
    assert callable(problog_Comment.__init__)


def test_problog_comment_constructor_args():
    sig = inspect.signature(problog_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_problog_comment_has_text():
    assert hasattr(problog_Comment, "text")
    descriptor = None
    for klass in problog_Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_problog_rule_is_not_abstract():
    assert not inspect.isabstract(problog_Rule)


def test_problog_rule_constructor_exists():
    assert callable(problog_Rule.__init__)


def test_problog_rule_constructor_args():
    sig = inspect.signature(problog_Rule.__init__)
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
Collection_strategy = st.builds(
    Collection,
)
problog_PLTuple_strategy = st.builds(
    problog_PLTuple,
)
problog_PLList_strategy = st.builds(
    problog_PLList,
)
ProbabilityMeasure_strategy = st.builds(
    ProbabilityMeasure,
)
problog_ProbabilityFraction_strategy = st.builds(
    problog_ProbabilityFraction,
    nominator=
        st.integers(),
    denominator=
        st.integers()
)
problog_ProbabilityLiteral_strategy = st.builds(
    problog_ProbabilityLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
problog_ProbabilityMeasure_strategy = st.builds(
    problog_ProbabilityMeasure,
)
Proposition_strategy = st.builds(
    Proposition,
)
problog_Annotatable_strategy = st.builds(
    problog_Annotatable,
)
problog_AnnotatedReferable_strategy = st.builds(
    problog_AnnotatedReferable,
)
Annotatable_strategy = st.builds(
    Annotatable,
)
Referable_strategy = st.builds(
    Referable,
)
problog_Variable_strategy = st.builds(
    problog_Variable,
    name=
        safe_text
)
problog_Atom_strategy = st.builds(
    problog_Atom,
    name=
        safe_text
)
problog_Collection_strategy = st.builds(
    problog_Collection,
)
problog_TermInstance_strategy = st.builds(
    problog_TermInstance,
)
problog_Term_strategy = st.builds(
    problog_Term,
    arguments=
        st.integers(),
    name=
        safe_text
)
problog_Statement_strategy = st.builds(
    problog_Statement,
)
problog_ProbLogProgram_strategy = st.builds(
    problog_ProbLogProgram,
)
problog_Referable_strategy = st.builds(
    problog_Referable,
)
problog_Proposition_strategy = st.builds(
    problog_Proposition,
)
ProbLogStatement_strategy = st.builds(
    ProbLogStatement,
)
problog_Query_strategy = st.builds(
    problog_Query,
)
problog_Evidence_strategy = st.builds(
    problog_Evidence,
    value=
        safe_text
)
problog_RHS_strategy = st.builds(
    problog_RHS,
)
problog_LHS_strategy = st.builds(
    problog_LHS,
)
Statement_strategy = st.builds(
    Statement,
)
problog_ProbLogStatement_strategy = st.builds(
    problog_ProbLogStatement,
)
problog_ImportLibrary_strategy = st.builds(
    problog_ImportLibrary,
    name=
        safe_text
)
problog_Cheat_strategy = st.builds(
    problog_Cheat,
    contents=
        safe_text
)
problog_Comment_strategy = st.builds(
    problog_Comment,
    text=
        safe_text
)
problog_Rule_strategy = st.builds(
    problog_Rule,
)

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)

@given(instance=problog_PLTuple_strategy)
@settings(max_examples=50)
def test_problog_pltuple_instantiation(instance):
    assert isinstance(instance, problog_PLTuple)

@given(instance=problog_PLList_strategy)
@settings(max_examples=50)
def test_problog_pllist_instantiation(instance):
    assert isinstance(instance, problog_PLList)

@given(instance=ProbabilityMeasure_strategy)
@settings(max_examples=50)
def test_probabilitymeasure_instantiation(instance):
    assert isinstance(instance, ProbabilityMeasure)

@given(instance=problog_ProbabilityFraction_strategy)
@settings(max_examples=50)
def test_problog_probabilityfraction_instantiation(instance):
    assert isinstance(instance, problog_ProbabilityFraction)



@given(instance=problog_ProbabilityFraction_strategy)
def test_problog_probabilityfraction_nominator_setter(instance):
    original = instance.nominator
    instance.nominator = original
    assert instance.nominator == original



@given(instance=problog_ProbabilityFraction_strategy)
def test_problog_probabilityfraction_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=problog_ProbabilityLiteral_strategy)
@settings(max_examples=50)
def test_problog_probabilityliteral_instantiation(instance):
    assert isinstance(instance, problog_ProbabilityLiteral)



@given(instance=problog_ProbabilityLiteral_strategy)
def test_problog_probabilityliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=problog_ProbabilityMeasure_strategy)
@settings(max_examples=50)
def test_problog_probabilitymeasure_instantiation(instance):
    assert isinstance(instance, problog_ProbabilityMeasure)

@given(instance=Proposition_strategy)
@settings(max_examples=50)
def test_proposition_instantiation(instance):
    assert isinstance(instance, Proposition)

@given(instance=problog_Annotatable_strategy)
@settings(max_examples=50)
def test_problog_annotatable_instantiation(instance):
    assert isinstance(instance, problog_Annotatable)

@given(instance=problog_AnnotatedReferable_strategy)
@settings(max_examples=50)
def test_problog_annotatedreferable_instantiation(instance):
    assert isinstance(instance, problog_AnnotatedReferable)

@given(instance=Annotatable_strategy)
@settings(max_examples=50)
def test_annotatable_instantiation(instance):
    assert isinstance(instance, Annotatable)

@given(instance=Referable_strategy)
@settings(max_examples=50)
def test_referable_instantiation(instance):
    assert isinstance(instance, Referable)

@given(instance=problog_Variable_strategy)
@settings(max_examples=50)
def test_problog_variable_instantiation(instance):
    assert isinstance(instance, problog_Variable)



@given(instance=problog_Variable_strategy)
def test_problog_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog_Atom_strategy)
@settings(max_examples=50)
def test_problog_atom_instantiation(instance):
    assert isinstance(instance, problog_Atom)



@given(instance=problog_Atom_strategy)
def test_problog_atom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog_Collection_strategy)
@settings(max_examples=50)
def test_problog_collection_instantiation(instance):
    assert isinstance(instance, problog_Collection)

@given(instance=problog_TermInstance_strategy)
@settings(max_examples=50)
def test_problog_terminstance_instantiation(instance):
    assert isinstance(instance, problog_TermInstance)

@given(instance=problog_Term_strategy)
@settings(max_examples=50)
def test_problog_term_instantiation(instance):
    assert isinstance(instance, problog_Term)



@given(instance=problog_Term_strategy)
def test_problog_term_arguments_setter(instance):
    original = instance.arguments
    instance.arguments = original
    assert instance.arguments == original



@given(instance=problog_Term_strategy)
def test_problog_term_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog_Statement_strategy)
@settings(max_examples=50)
def test_problog_statement_instantiation(instance):
    assert isinstance(instance, problog_Statement)

@given(instance=problog_ProbLogProgram_strategy)
@settings(max_examples=50)
def test_problog_problogprogram_instantiation(instance):
    assert isinstance(instance, problog_ProbLogProgram)

@given(instance=problog_Referable_strategy)
@settings(max_examples=50)
def test_problog_referable_instantiation(instance):
    assert isinstance(instance, problog_Referable)

@given(instance=problog_Proposition_strategy)
@settings(max_examples=50)
def test_problog_proposition_instantiation(instance):
    assert isinstance(instance, problog_Proposition)

@given(instance=ProbLogStatement_strategy)
@settings(max_examples=50)
def test_problogstatement_instantiation(instance):
    assert isinstance(instance, ProbLogStatement)

@given(instance=problog_Query_strategy)
@settings(max_examples=50)
def test_problog_query_instantiation(instance):
    assert isinstance(instance, problog_Query)

@given(instance=problog_Evidence_strategy)
@settings(max_examples=50)
def test_problog_evidence_instantiation(instance):
    assert isinstance(instance, problog_Evidence)



@given(instance=problog_Evidence_strategy)
def test_problog_evidence_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=problog_RHS_strategy)
@settings(max_examples=50)
def test_problog_rhs_instantiation(instance):
    assert isinstance(instance, problog_RHS)

@given(instance=problog_LHS_strategy)
@settings(max_examples=50)
def test_problog_lhs_instantiation(instance):
    assert isinstance(instance, problog_LHS)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=problog_ProbLogStatement_strategy)
@settings(max_examples=50)
def test_problog_problogstatement_instantiation(instance):
    assert isinstance(instance, problog_ProbLogStatement)

@given(instance=problog_ImportLibrary_strategy)
@settings(max_examples=50)
def test_problog_importlibrary_instantiation(instance):
    assert isinstance(instance, problog_ImportLibrary)



@given(instance=problog_ImportLibrary_strategy)
def test_problog_importlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog_Cheat_strategy)
@settings(max_examples=50)
def test_problog_cheat_instantiation(instance):
    assert isinstance(instance, problog_Cheat)



@given(instance=problog_Cheat_strategy)
def test_problog_cheat_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=problog_Comment_strategy)
@settings(max_examples=50)
def test_problog_comment_instantiation(instance):
    assert isinstance(instance, problog_Comment)



@given(instance=problog_Comment_strategy)
def test_problog_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=problog_Rule_strategy)
@settings(max_examples=50)
def test_problog_rule_instantiation(instance):
    assert isinstance(instance, problog_Rule)

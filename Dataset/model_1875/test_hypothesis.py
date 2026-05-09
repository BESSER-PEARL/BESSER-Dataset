import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Collection,
    problog::PLTuple,
    problog::PLList,
    ProbabilityMeasure,
    problog::ProbabilityFraction,
    problog::ProbabilityLiteral,
    problog::ProbabilityMeasure,
    Proposition,
    problog::Annotatable,
    problog::AnnotatedReferable,
    Annotatable,
    Referable,
    problog::Variable,
    problog::Atom,
    problog::Collection,
    problog::TermInstance,
    problog::Term,
    problog::Statement,
    problog::ProbLogProgram,
    problog::Referable,
    problog::Proposition,
    ProbLogStatement,
    problog::Query,
    problog::Evidence,
    problog::RHS,
    problog::LHS,
    Statement,
    problog::ProbLogStatement,
    problog::ImportLibrary,
    problog::Cheat,
    problog::Comment,
    problog::Rule,
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



def test_problog::pltuple_is_not_abstract():
    assert not inspect.isabstract(problog::PLTuple)


def test_problog::pltuple_constructor_exists():
    assert callable(problog::PLTuple.__init__)


def test_problog::pltuple_constructor_args():
    sig = inspect.signature(problog::PLTuple.__init__)
    params = list(sig.parameters.keys())



def test_problog::pllist_is_not_abstract():
    assert not inspect.isabstract(problog::PLList)


def test_problog::pllist_constructor_exists():
    assert callable(problog::PLList.__init__)


def test_problog::pllist_constructor_args():
    sig = inspect.signature(problog::PLList.__init__)
    params = list(sig.parameters.keys())



def test_probabilitymeasure_is_not_abstract():
    assert not inspect.isabstract(ProbabilityMeasure)


def test_probabilitymeasure_constructor_exists():
    assert callable(ProbabilityMeasure.__init__)


def test_probabilitymeasure_constructor_args():
    sig = inspect.signature(ProbabilityMeasure.__init__)
    params = list(sig.parameters.keys())



def test_problog::probabilityfraction_is_not_abstract():
    assert not inspect.isabstract(problog::ProbabilityFraction)


def test_problog::probabilityfraction_constructor_exists():
    assert callable(problog::ProbabilityFraction.__init__)


def test_problog::probabilityfraction_constructor_args():
    sig = inspect.signature(problog::ProbabilityFraction.__init__)
    params = list(sig.parameters.keys())
    assert "nominator" in params, "Missing parameter 'nominator'"
    assert "denominator" in params, "Missing parameter 'denominator'"

def test_problog::probabilityfraction_has_nominator():
    assert hasattr(problog::ProbabilityFraction, "nominator")
    descriptor = None
    for klass in problog::ProbabilityFraction.__mro__:
        if "nominator" in klass.__dict__:
            descriptor = klass.__dict__["nominator"]
            break
    assert isinstance(descriptor, property)

def test_problog::probabilityfraction_has_denominator():
    assert hasattr(problog::ProbabilityFraction, "denominator")
    descriptor = None
    for klass in problog::ProbabilityFraction.__mro__:
        if "denominator" in klass.__dict__:
            descriptor = klass.__dict__["denominator"]
            break
    assert isinstance(descriptor, property)



def test_problog::probabilityliteral_is_not_abstract():
    assert not inspect.isabstract(problog::ProbabilityLiteral)


def test_problog::probabilityliteral_constructor_exists():
    assert callable(problog::ProbabilityLiteral.__init__)


def test_problog::probabilityliteral_constructor_args():
    sig = inspect.signature(problog::ProbabilityLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_problog::probabilityliteral_has_value():
    assert hasattr(problog::ProbabilityLiteral, "value")
    descriptor = None
    for klass in problog::ProbabilityLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_problog::probabilitymeasure_is_not_abstract():
    assert not inspect.isabstract(problog::ProbabilityMeasure)


def test_problog::probabilitymeasure_constructor_exists():
    assert callable(problog::ProbabilityMeasure.__init__)


def test_problog::probabilitymeasure_constructor_args():
    sig = inspect.signature(problog::ProbabilityMeasure.__init__)
    params = list(sig.parameters.keys())



def test_proposition_is_not_abstract():
    assert not inspect.isabstract(Proposition)


def test_proposition_constructor_exists():
    assert callable(Proposition.__init__)


def test_proposition_constructor_args():
    sig = inspect.signature(Proposition.__init__)
    params = list(sig.parameters.keys())



def test_problog::annotatable_is_not_abstract():
    assert not inspect.isabstract(problog::Annotatable)


def test_problog::annotatable_constructor_exists():
    assert callable(problog::Annotatable.__init__)


def test_problog::annotatable_constructor_args():
    sig = inspect.signature(problog::Annotatable.__init__)
    params = list(sig.parameters.keys())



def test_problog::annotatedreferable_is_not_abstract():
    assert not inspect.isabstract(problog::AnnotatedReferable)


def test_problog::annotatedreferable_constructor_exists():
    assert callable(problog::AnnotatedReferable.__init__)


def test_problog::annotatedreferable_constructor_args():
    sig = inspect.signature(problog::AnnotatedReferable.__init__)
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



def test_problog::variable_is_not_abstract():
    assert not inspect.isabstract(problog::Variable)


def test_problog::variable_constructor_exists():
    assert callable(problog::Variable.__init__)


def test_problog::variable_constructor_args():
    sig = inspect.signature(problog::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog::variable_has_name():
    assert hasattr(problog::Variable, "name")
    descriptor = None
    for klass in problog::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog::atom_is_not_abstract():
    assert not inspect.isabstract(problog::Atom)


def test_problog::atom_constructor_exists():
    assert callable(problog::Atom.__init__)


def test_problog::atom_constructor_args():
    sig = inspect.signature(problog::Atom.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog::atom_has_name():
    assert hasattr(problog::Atom, "name")
    descriptor = None
    for klass in problog::Atom.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog::collection_is_not_abstract():
    assert not inspect.isabstract(problog::Collection)


def test_problog::collection_constructor_exists():
    assert callable(problog::Collection.__init__)


def test_problog::collection_constructor_args():
    sig = inspect.signature(problog::Collection.__init__)
    params = list(sig.parameters.keys())



def test_problog::terminstance_is_not_abstract():
    assert not inspect.isabstract(problog::TermInstance)


def test_problog::terminstance_constructor_exists():
    assert callable(problog::TermInstance.__init__)


def test_problog::terminstance_constructor_args():
    sig = inspect.signature(problog::TermInstance.__init__)
    params = list(sig.parameters.keys())



def test_problog::term_is_not_abstract():
    assert not inspect.isabstract(problog::Term)


def test_problog::term_constructor_exists():
    assert callable(problog::Term.__init__)


def test_problog::term_constructor_args():
    sig = inspect.signature(problog::Term.__init__)
    params = list(sig.parameters.keys())
    assert "arguments" in params, "Missing parameter 'arguments'"
    assert "name" in params, "Missing parameter 'name'"

def test_problog::term_has_arguments():
    assert hasattr(problog::Term, "arguments")
    descriptor = None
    for klass in problog::Term.__mro__:
        if "arguments" in klass.__dict__:
            descriptor = klass.__dict__["arguments"]
            break
    assert isinstance(descriptor, property)

def test_problog::term_has_name():
    assert hasattr(problog::Term, "name")
    descriptor = None
    for klass in problog::Term.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog::statement_is_not_abstract():
    assert not inspect.isabstract(problog::Statement)


def test_problog::statement_constructor_exists():
    assert callable(problog::Statement.__init__)


def test_problog::statement_constructor_args():
    sig = inspect.signature(problog::Statement.__init__)
    params = list(sig.parameters.keys())



def test_problog::problogprogram_is_not_abstract():
    assert not inspect.isabstract(problog::ProbLogProgram)


def test_problog::problogprogram_constructor_exists():
    assert callable(problog::ProbLogProgram.__init__)


def test_problog::problogprogram_constructor_args():
    sig = inspect.signature(problog::ProbLogProgram.__init__)
    params = list(sig.parameters.keys())



def test_problog::referable_is_not_abstract():
    assert not inspect.isabstract(problog::Referable)


def test_problog::referable_constructor_exists():
    assert callable(problog::Referable.__init__)


def test_problog::referable_constructor_args():
    sig = inspect.signature(problog::Referable.__init__)
    params = list(sig.parameters.keys())



def test_problog::proposition_is_not_abstract():
    assert not inspect.isabstract(problog::Proposition)


def test_problog::proposition_constructor_exists():
    assert callable(problog::Proposition.__init__)


def test_problog::proposition_constructor_args():
    sig = inspect.signature(problog::Proposition.__init__)
    params = list(sig.parameters.keys())



def test_problogstatement_is_not_abstract():
    assert not inspect.isabstract(ProbLogStatement)


def test_problogstatement_constructor_exists():
    assert callable(ProbLogStatement.__init__)


def test_problogstatement_constructor_args():
    sig = inspect.signature(ProbLogStatement.__init__)
    params = list(sig.parameters.keys())



def test_problog::query_is_not_abstract():
    assert not inspect.isabstract(problog::Query)


def test_problog::query_constructor_exists():
    assert callable(problog::Query.__init__)


def test_problog::query_constructor_args():
    sig = inspect.signature(problog::Query.__init__)
    params = list(sig.parameters.keys())



def test_problog::evidence_is_not_abstract():
    assert not inspect.isabstract(problog::Evidence)


def test_problog::evidence_constructor_exists():
    assert callable(problog::Evidence.__init__)


def test_problog::evidence_constructor_args():
    sig = inspect.signature(problog::Evidence.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_problog::evidence_has_value():
    assert hasattr(problog::Evidence, "value")
    descriptor = None
    for klass in problog::Evidence.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_problog::rhs_is_not_abstract():
    assert not inspect.isabstract(problog::RHS)


def test_problog::rhs_constructor_exists():
    assert callable(problog::RHS.__init__)


def test_problog::rhs_constructor_args():
    sig = inspect.signature(problog::RHS.__init__)
    params = list(sig.parameters.keys())



def test_problog::lhs_is_not_abstract():
    assert not inspect.isabstract(problog::LHS)


def test_problog::lhs_constructor_exists():
    assert callable(problog::LHS.__init__)


def test_problog::lhs_constructor_args():
    sig = inspect.signature(problog::LHS.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_problog::problogstatement_is_not_abstract():
    assert not inspect.isabstract(problog::ProbLogStatement)


def test_problog::problogstatement_constructor_exists():
    assert callable(problog::ProbLogStatement.__init__)


def test_problog::problogstatement_constructor_args():
    sig = inspect.signature(problog::ProbLogStatement.__init__)
    params = list(sig.parameters.keys())



def test_problog::importlibrary_is_not_abstract():
    assert not inspect.isabstract(problog::ImportLibrary)


def test_problog::importlibrary_constructor_exists():
    assert callable(problog::ImportLibrary.__init__)


def test_problog::importlibrary_constructor_args():
    sig = inspect.signature(problog::ImportLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_problog::importlibrary_has_name():
    assert hasattr(problog::ImportLibrary, "name")
    descriptor = None
    for klass in problog::ImportLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_problog::cheat_is_not_abstract():
    assert not inspect.isabstract(problog::Cheat)


def test_problog::cheat_constructor_exists():
    assert callable(problog::Cheat.__init__)


def test_problog::cheat_constructor_args():
    sig = inspect.signature(problog::Cheat.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_problog::cheat_has_contents():
    assert hasattr(problog::Cheat, "contents")
    descriptor = None
    for klass in problog::Cheat.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)



def test_problog::comment_is_not_abstract():
    assert not inspect.isabstract(problog::Comment)


def test_problog::comment_constructor_exists():
    assert callable(problog::Comment.__init__)


def test_problog::comment_constructor_args():
    sig = inspect.signature(problog::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_problog::comment_has_text():
    assert hasattr(problog::Comment, "text")
    descriptor = None
    for klass in problog::Comment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_problog::rule_is_not_abstract():
    assert not inspect.isabstract(problog::Rule)


def test_problog::rule_constructor_exists():
    assert callable(problog::Rule.__init__)


def test_problog::rule_constructor_args():
    sig = inspect.signature(problog::Rule.__init__)
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
problog::PLTuple_strategy = st.builds(
    problog::PLTuple,
)
problog::PLList_strategy = st.builds(
    problog::PLList,
)
ProbabilityMeasure_strategy = st.builds(
    ProbabilityMeasure,
)
problog::ProbabilityFraction_strategy = st.builds(
    problog::ProbabilityFraction,
    nominator=
        st.integers(),
    denominator=
        st.integers()
)
problog::ProbabilityLiteral_strategy = st.builds(
    problog::ProbabilityLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
problog::ProbabilityMeasure_strategy = st.builds(
    problog::ProbabilityMeasure,
)
Proposition_strategy = st.builds(
    Proposition,
)
problog::Annotatable_strategy = st.builds(
    problog::Annotatable,
)
problog::AnnotatedReferable_strategy = st.builds(
    problog::AnnotatedReferable,
)
Annotatable_strategy = st.builds(
    Annotatable,
)
Referable_strategy = st.builds(
    Referable,
)
problog::Variable_strategy = st.builds(
    problog::Variable,
    name=
        safe_text
)
problog::Atom_strategy = st.builds(
    problog::Atom,
    name=
        safe_text
)
problog::Collection_strategy = st.builds(
    problog::Collection,
)
problog::TermInstance_strategy = st.builds(
    problog::TermInstance,
)
problog::Term_strategy = st.builds(
    problog::Term,
    arguments=
        st.integers(),
    name=
        safe_text
)
problog::Statement_strategy = st.builds(
    problog::Statement,
)
problog::ProbLogProgram_strategy = st.builds(
    problog::ProbLogProgram,
)
problog::Referable_strategy = st.builds(
    problog::Referable,
)
problog::Proposition_strategy = st.builds(
    problog::Proposition,
)
ProbLogStatement_strategy = st.builds(
    ProbLogStatement,
)
problog::Query_strategy = st.builds(
    problog::Query,
)
problog::Evidence_strategy = st.builds(
    problog::Evidence,
    value=
        safe_text
)
problog::RHS_strategy = st.builds(
    problog::RHS,
)
problog::LHS_strategy = st.builds(
    problog::LHS,
)
Statement_strategy = st.builds(
    Statement,
)
problog::ProbLogStatement_strategy = st.builds(
    problog::ProbLogStatement,
)
problog::ImportLibrary_strategy = st.builds(
    problog::ImportLibrary,
    name=
        safe_text
)
problog::Cheat_strategy = st.builds(
    problog::Cheat,
    contents=
        safe_text
)
problog::Comment_strategy = st.builds(
    problog::Comment,
    text=
        safe_text
)
problog::Rule_strategy = st.builds(
    problog::Rule,
)

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)

@given(instance=problog::PLTuple_strategy)
@settings(max_examples=50)
def test_problog::pltuple_instantiation(instance):
    assert isinstance(instance, problog::PLTuple)

@given(instance=problog::PLList_strategy)
@settings(max_examples=50)
def test_problog::pllist_instantiation(instance):
    assert isinstance(instance, problog::PLList)

@given(instance=ProbabilityMeasure_strategy)
@settings(max_examples=50)
def test_probabilitymeasure_instantiation(instance):
    assert isinstance(instance, ProbabilityMeasure)

@given(instance=problog::ProbabilityFraction_strategy)
@settings(max_examples=50)
def test_problog::probabilityfraction_instantiation(instance):
    assert isinstance(instance, problog::ProbabilityFraction)

@given(instance=problog::ProbabilityFraction_strategy)
def test_problog::probabilityfraction_nominator_type(instance):
    assert isinstance(instance.nominator, int)


@given(instance=problog::ProbabilityFraction_strategy)
def test_problog::probabilityfraction_nominator_setter(instance):
    original = instance.nominator
    instance.nominator = original
    assert instance.nominator == original

@given(instance=problog::ProbabilityFraction_strategy)
def test_problog::probabilityfraction_denominator_type(instance):
    assert isinstance(instance.denominator, int)


@given(instance=problog::ProbabilityFraction_strategy)
def test_problog::probabilityfraction_denominator_setter(instance):
    original = instance.denominator
    instance.denominator = original
    assert instance.denominator == original

@given(instance=problog::ProbabilityLiteral_strategy)
@settings(max_examples=50)
def test_problog::probabilityliteral_instantiation(instance):
    assert isinstance(instance, problog::ProbabilityLiteral)

@given(instance=problog::ProbabilityLiteral_strategy)
def test_problog::probabilityliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=problog::ProbabilityLiteral_strategy)
def test_problog::probabilityliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=problog::ProbabilityMeasure_strategy)
@settings(max_examples=50)
def test_problog::probabilitymeasure_instantiation(instance):
    assert isinstance(instance, problog::ProbabilityMeasure)

@given(instance=Proposition_strategy)
@settings(max_examples=50)
def test_proposition_instantiation(instance):
    assert isinstance(instance, Proposition)

@given(instance=problog::Annotatable_strategy)
@settings(max_examples=50)
def test_problog::annotatable_instantiation(instance):
    assert isinstance(instance, problog::Annotatable)

@given(instance=problog::AnnotatedReferable_strategy)
@settings(max_examples=50)
def test_problog::annotatedreferable_instantiation(instance):
    assert isinstance(instance, problog::AnnotatedReferable)

@given(instance=Annotatable_strategy)
@settings(max_examples=50)
def test_annotatable_instantiation(instance):
    assert isinstance(instance, Annotatable)

@given(instance=Referable_strategy)
@settings(max_examples=50)
def test_referable_instantiation(instance):
    assert isinstance(instance, Referable)

@given(instance=problog::Variable_strategy)
@settings(max_examples=50)
def test_problog::variable_instantiation(instance):
    assert isinstance(instance, problog::Variable)

@given(instance=problog::Variable_strategy)
def test_problog::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=problog::Variable_strategy)
def test_problog::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog::Atom_strategy)
@settings(max_examples=50)
def test_problog::atom_instantiation(instance):
    assert isinstance(instance, problog::Atom)

@given(instance=problog::Atom_strategy)
def test_problog::atom_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=problog::Atom_strategy)
def test_problog::atom_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog::Collection_strategy)
@settings(max_examples=50)
def test_problog::collection_instantiation(instance):
    assert isinstance(instance, problog::Collection)

@given(instance=problog::TermInstance_strategy)
@settings(max_examples=50)
def test_problog::terminstance_instantiation(instance):
    assert isinstance(instance, problog::TermInstance)

@given(instance=problog::Term_strategy)
@settings(max_examples=50)
def test_problog::term_instantiation(instance):
    assert isinstance(instance, problog::Term)

@given(instance=problog::Term_strategy)
def test_problog::term_arguments_type(instance):
    assert isinstance(instance.arguments, int)


@given(instance=problog::Term_strategy)
def test_problog::term_arguments_setter(instance):
    original = instance.arguments
    instance.arguments = original
    assert instance.arguments == original

@given(instance=problog::Term_strategy)
def test_problog::term_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=problog::Term_strategy)
def test_problog::term_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog::Statement_strategy)
@settings(max_examples=50)
def test_problog::statement_instantiation(instance):
    assert isinstance(instance, problog::Statement)

@given(instance=problog::ProbLogProgram_strategy)
@settings(max_examples=50)
def test_problog::problogprogram_instantiation(instance):
    assert isinstance(instance, problog::ProbLogProgram)

@given(instance=problog::Referable_strategy)
@settings(max_examples=50)
def test_problog::referable_instantiation(instance):
    assert isinstance(instance, problog::Referable)

@given(instance=problog::Proposition_strategy)
@settings(max_examples=50)
def test_problog::proposition_instantiation(instance):
    assert isinstance(instance, problog::Proposition)

@given(instance=ProbLogStatement_strategy)
@settings(max_examples=50)
def test_problogstatement_instantiation(instance):
    assert isinstance(instance, ProbLogStatement)

@given(instance=problog::Query_strategy)
@settings(max_examples=50)
def test_problog::query_instantiation(instance):
    assert isinstance(instance, problog::Query)

@given(instance=problog::Evidence_strategy)
@settings(max_examples=50)
def test_problog::evidence_instantiation(instance):
    assert isinstance(instance, problog::Evidence)

@given(instance=problog::Evidence_strategy)
def test_problog::evidence_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=problog::Evidence_strategy)
def test_problog::evidence_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=problog::RHS_strategy)
@settings(max_examples=50)
def test_problog::rhs_instantiation(instance):
    assert isinstance(instance, problog::RHS)

@given(instance=problog::LHS_strategy)
@settings(max_examples=50)
def test_problog::lhs_instantiation(instance):
    assert isinstance(instance, problog::LHS)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=problog::ProbLogStatement_strategy)
@settings(max_examples=50)
def test_problog::problogstatement_instantiation(instance):
    assert isinstance(instance, problog::ProbLogStatement)

@given(instance=problog::ImportLibrary_strategy)
@settings(max_examples=50)
def test_problog::importlibrary_instantiation(instance):
    assert isinstance(instance, problog::ImportLibrary)

@given(instance=problog::ImportLibrary_strategy)
def test_problog::importlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=problog::ImportLibrary_strategy)
def test_problog::importlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=problog::Cheat_strategy)
@settings(max_examples=50)
def test_problog::cheat_instantiation(instance):
    assert isinstance(instance, problog::Cheat)

@given(instance=problog::Cheat_strategy)
def test_problog::cheat_contents_type(instance):
    assert isinstance(instance.contents, str)


@given(instance=problog::Cheat_strategy)
def test_problog::cheat_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=problog::Comment_strategy)
@settings(max_examples=50)
def test_problog::comment_instantiation(instance):
    assert isinstance(instance, problog::Comment)

@given(instance=problog::Comment_strategy)
def test_problog::comment_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=problog::Comment_strategy)
def test_problog::comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=problog::Rule_strategy)
@settings(max_examples=50)
def test_problog::rule_instantiation(instance):
    assert isinstance(instance, problog::Rule)

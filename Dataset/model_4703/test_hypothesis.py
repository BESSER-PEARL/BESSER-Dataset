import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OperatorDecl,
    SortDecl,
    Operator,
    terms::BuiltInOperator,
    terms::Tuple,
    terms::UserOperator,
    terms::MultisetOperator,
    terms::BuiltInConstant,
    Term,
    terms::Variable,
    terms::PartitionElement,
    terms::HLAnnotation,
    terms::Condition,
    terms::HLMarking,
    terms::NamedOperator,
    terms::Operator,
    terms::Term,
    Sort,
    terms::UserSort,
    terms::BuiltInSort,
    TermsDeclaration,
    terms::OperatorDecl,
    terms::SortDecl,
    terms::Partition,
    terms::Empty,
    terms::All,
    terms::Type,
    terms::ProductSort,
    terms::VariableDecl,
    terms::NamedSort,
    terms::MultisetSort,
    terms::Sort,
    terms::MakeList,
    terms::EmptyList,
    terms::HLPNList,
    terms::TermsDeclaration,
    terms::Declarations,
    terms::Declaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operatordecl_is_not_abstract():
    assert not inspect.isabstract(OperatorDecl)


def test_operatordecl_constructor_exists():
    assert callable(OperatorDecl.__init__)


def test_operatordecl_constructor_args():
    sig = inspect.signature(OperatorDecl.__init__)
    params = list(sig.parameters.keys())



def test_sortdecl_is_not_abstract():
    assert not inspect.isabstract(SortDecl)


def test_sortdecl_constructor_exists():
    assert callable(SortDecl.__init__)


def test_sortdecl_constructor_args():
    sig = inspect.signature(SortDecl.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_terms::builtinoperator_is_not_abstract():
    assert not inspect.isabstract(terms::BuiltInOperator)


def test_terms::builtinoperator_constructor_exists():
    assert callable(terms::BuiltInOperator.__init__)


def test_terms::builtinoperator_constructor_args():
    sig = inspect.signature(terms::BuiltInOperator.__init__)
    params = list(sig.parameters.keys())



def test_terms::tuple_is_not_abstract():
    assert not inspect.isabstract(terms::Tuple)


def test_terms::tuple_constructor_exists():
    assert callable(terms::Tuple.__init__)


def test_terms::tuple_constructor_args():
    sig = inspect.signature(terms::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_terms::useroperator_is_not_abstract():
    assert not inspect.isabstract(terms::UserOperator)


def test_terms::useroperator_constructor_exists():
    assert callable(terms::UserOperator.__init__)


def test_terms::useroperator_constructor_args():
    sig = inspect.signature(terms::UserOperator.__init__)
    params = list(sig.parameters.keys())



def test_terms::multisetoperator_is_not_abstract():
    assert not inspect.isabstract(terms::MultisetOperator)


def test_terms::multisetoperator_constructor_exists():
    assert callable(terms::MultisetOperator.__init__)


def test_terms::multisetoperator_constructor_args():
    sig = inspect.signature(terms::MultisetOperator.__init__)
    params = list(sig.parameters.keys())



def test_terms::builtinconstant_is_not_abstract():
    assert not inspect.isabstract(terms::BuiltInConstant)


def test_terms::builtinconstant_constructor_exists():
    assert callable(terms::BuiltInConstant.__init__)


def test_terms::builtinconstant_constructor_args():
    sig = inspect.signature(terms::BuiltInConstant.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_terms::variable_is_not_abstract():
    assert not inspect.isabstract(terms::Variable)


def test_terms::variable_constructor_exists():
    assert callable(terms::Variable.__init__)


def test_terms::variable_constructor_args():
    sig = inspect.signature(terms::Variable.__init__)
    params = list(sig.parameters.keys())



def test_terms::partitionelement_is_not_abstract():
    assert not inspect.isabstract(terms::PartitionElement)


def test_terms::partitionelement_constructor_exists():
    assert callable(terms::PartitionElement.__init__)


def test_terms::partitionelement_constructor_args():
    sig = inspect.signature(terms::PartitionElement.__init__)
    params = list(sig.parameters.keys())



def test_terms::hlannotation_is_not_abstract():
    assert not inspect.isabstract(terms::HLAnnotation)


def test_terms::hlannotation_constructor_exists():
    assert callable(terms::HLAnnotation.__init__)


def test_terms::hlannotation_constructor_args():
    sig = inspect.signature(terms::HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_terms::condition_is_not_abstract():
    assert not inspect.isabstract(terms::Condition)


def test_terms::condition_constructor_exists():
    assert callable(terms::Condition.__init__)


def test_terms::condition_constructor_args():
    sig = inspect.signature(terms::Condition.__init__)
    params = list(sig.parameters.keys())



def test_terms::hlmarking_is_not_abstract():
    assert not inspect.isabstract(terms::HLMarking)


def test_terms::hlmarking_constructor_exists():
    assert callable(terms::HLMarking.__init__)


def test_terms::hlmarking_constructor_args():
    sig = inspect.signature(terms::HLMarking.__init__)
    params = list(sig.parameters.keys())



def test_terms::namedoperator_is_not_abstract():
    assert not inspect.isabstract(terms::NamedOperator)


def test_terms::namedoperator_constructor_exists():
    assert callable(terms::NamedOperator.__init__)


def test_terms::namedoperator_constructor_args():
    sig = inspect.signature(terms::NamedOperator.__init__)
    params = list(sig.parameters.keys())



def test_terms::operator_is_not_abstract():
    assert not inspect.isabstract(terms::Operator)


def test_terms::operator_constructor_exists():
    assert callable(terms::Operator.__init__)


def test_terms::operator_constructor_args():
    sig = inspect.signature(terms::Operator.__init__)
    params = list(sig.parameters.keys())



def test_terms::term_is_not_abstract():
    assert not inspect.isabstract(terms::Term)


def test_terms::term_constructor_exists():
    assert callable(terms::Term.__init__)


def test_terms::term_constructor_args():
    sig = inspect.signature(terms::Term.__init__)
    params = list(sig.parameters.keys())



def test_sort_is_not_abstract():
    assert not inspect.isabstract(Sort)


def test_sort_constructor_exists():
    assert callable(Sort.__init__)


def test_sort_constructor_args():
    sig = inspect.signature(Sort.__init__)
    params = list(sig.parameters.keys())



def test_terms::usersort_is_not_abstract():
    assert not inspect.isabstract(terms::UserSort)


def test_terms::usersort_constructor_exists():
    assert callable(terms::UserSort.__init__)


def test_terms::usersort_constructor_args():
    sig = inspect.signature(terms::UserSort.__init__)
    params = list(sig.parameters.keys())



def test_terms::builtinsort_is_not_abstract():
    assert not inspect.isabstract(terms::BuiltInSort)


def test_terms::builtinsort_constructor_exists():
    assert callable(terms::BuiltInSort.__init__)


def test_terms::builtinsort_constructor_args():
    sig = inspect.signature(terms::BuiltInSort.__init__)
    params = list(sig.parameters.keys())



def test_termsdeclaration_is_not_abstract():
    assert not inspect.isabstract(TermsDeclaration)


def test_termsdeclaration_constructor_exists():
    assert callable(TermsDeclaration.__init__)


def test_termsdeclaration_constructor_args():
    sig = inspect.signature(TermsDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_terms::operatordecl_is_not_abstract():
    assert not inspect.isabstract(terms::OperatorDecl)


def test_terms::operatordecl_constructor_exists():
    assert callable(terms::OperatorDecl.__init__)


def test_terms::operatordecl_constructor_args():
    sig = inspect.signature(terms::OperatorDecl.__init__)
    params = list(sig.parameters.keys())



def test_terms::sortdecl_is_not_abstract():
    assert not inspect.isabstract(terms::SortDecl)


def test_terms::sortdecl_constructor_exists():
    assert callable(terms::SortDecl.__init__)


def test_terms::sortdecl_constructor_args():
    sig = inspect.signature(terms::SortDecl.__init__)
    params = list(sig.parameters.keys())



def test_terms::partition_is_not_abstract():
    assert not inspect.isabstract(terms::Partition)


def test_terms::partition_constructor_exists():
    assert callable(terms::Partition.__init__)


def test_terms::partition_constructor_args():
    sig = inspect.signature(terms::Partition.__init__)
    params = list(sig.parameters.keys())



def test_terms::empty_is_not_abstract():
    assert not inspect.isabstract(terms::Empty)


def test_terms::empty_constructor_exists():
    assert callable(terms::Empty.__init__)


def test_terms::empty_constructor_args():
    sig = inspect.signature(terms::Empty.__init__)
    params = list(sig.parameters.keys())



def test_terms::all_is_not_abstract():
    assert not inspect.isabstract(terms::All)


def test_terms::all_constructor_exists():
    assert callable(terms::All.__init__)


def test_terms::all_constructor_args():
    sig = inspect.signature(terms::All.__init__)
    params = list(sig.parameters.keys())



def test_terms::type_is_not_abstract():
    assert not inspect.isabstract(terms::Type)


def test_terms::type_constructor_exists():
    assert callable(terms::Type.__init__)


def test_terms::type_constructor_args():
    sig = inspect.signature(terms::Type.__init__)
    params = list(sig.parameters.keys())



def test_terms::productsort_is_not_abstract():
    assert not inspect.isabstract(terms::ProductSort)


def test_terms::productsort_constructor_exists():
    assert callable(terms::ProductSort.__init__)


def test_terms::productsort_constructor_args():
    sig = inspect.signature(terms::ProductSort.__init__)
    params = list(sig.parameters.keys())



def test_terms::variabledecl_is_not_abstract():
    assert not inspect.isabstract(terms::VariableDecl)


def test_terms::variabledecl_constructor_exists():
    assert callable(terms::VariableDecl.__init__)


def test_terms::variabledecl_constructor_args():
    sig = inspect.signature(terms::VariableDecl.__init__)
    params = list(sig.parameters.keys())



def test_terms::namedsort_is_not_abstract():
    assert not inspect.isabstract(terms::NamedSort)


def test_terms::namedsort_constructor_exists():
    assert callable(terms::NamedSort.__init__)


def test_terms::namedsort_constructor_args():
    sig = inspect.signature(terms::NamedSort.__init__)
    params = list(sig.parameters.keys())



def test_terms::multisetsort_is_not_abstract():
    assert not inspect.isabstract(terms::MultisetSort)


def test_terms::multisetsort_constructor_exists():
    assert callable(terms::MultisetSort.__init__)


def test_terms::multisetsort_constructor_args():
    sig = inspect.signature(terms::MultisetSort.__init__)
    params = list(sig.parameters.keys())



def test_terms::sort_is_not_abstract():
    assert not inspect.isabstract(terms::Sort)


def test_terms::sort_constructor_exists():
    assert callable(terms::Sort.__init__)


def test_terms::sort_constructor_args():
    sig = inspect.signature(terms::Sort.__init__)
    params = list(sig.parameters.keys())



def test_terms::makelist_is_not_abstract():
    assert not inspect.isabstract(terms::MakeList)


def test_terms::makelist_constructor_exists():
    assert callable(terms::MakeList.__init__)


def test_terms::makelist_constructor_args():
    sig = inspect.signature(terms::MakeList.__init__)
    params = list(sig.parameters.keys())



def test_terms::emptylist_is_not_abstract():
    assert not inspect.isabstract(terms::EmptyList)


def test_terms::emptylist_constructor_exists():
    assert callable(terms::EmptyList.__init__)


def test_terms::emptylist_constructor_args():
    sig = inspect.signature(terms::EmptyList.__init__)
    params = list(sig.parameters.keys())



def test_terms::hlpnlist_is_not_abstract():
    assert not inspect.isabstract(terms::HLPNList)


def test_terms::hlpnlist_constructor_exists():
    assert callable(terms::HLPNList.__init__)


def test_terms::hlpnlist_constructor_args():
    sig = inspect.signature(terms::HLPNList.__init__)
    params = list(sig.parameters.keys())



def test_terms::termsdeclaration_is_not_abstract():
    assert not inspect.isabstract(terms::TermsDeclaration)


def test_terms::termsdeclaration_constructor_exists():
    assert callable(terms::TermsDeclaration.__init__)


def test_terms::termsdeclaration_constructor_args():
    sig = inspect.signature(terms::TermsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_terms::termsdeclaration_has_name():
    assert hasattr(terms::TermsDeclaration, "name")
    descriptor = None
    for klass in terms::TermsDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_terms::termsdeclaration_has_id():
    assert hasattr(terms::TermsDeclaration, "id")
    descriptor = None
    for klass in terms::TermsDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_terms::declarations_is_not_abstract():
    assert not inspect.isabstract(terms::Declarations)


def test_terms::declarations_constructor_exists():
    assert callable(terms::Declarations.__init__)


def test_terms::declarations_constructor_args():
    sig = inspect.signature(terms::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_terms::declaration_is_not_abstract():
    assert not inspect.isabstract(terms::Declaration)


def test_terms::declaration_constructor_exists():
    assert callable(terms::Declaration.__init__)


def test_terms::declaration_constructor_args():
    sig = inspect.signature(terms::Declaration.__init__)
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
OperatorDecl_strategy = st.builds(
    OperatorDecl,
)
SortDecl_strategy = st.builds(
    SortDecl,
)
Operator_strategy = st.builds(
    Operator,
)
terms::BuiltInOperator_strategy = st.builds(
    terms::BuiltInOperator,
)
terms::Tuple_strategy = st.builds(
    terms::Tuple,
)
terms::UserOperator_strategy = st.builds(
    terms::UserOperator,
)
terms::MultisetOperator_strategy = st.builds(
    terms::MultisetOperator,
)
terms::BuiltInConstant_strategy = st.builds(
    terms::BuiltInConstant,
)
Term_strategy = st.builds(
    Term,
)
terms::Variable_strategy = st.builds(
    terms::Variable,
)
terms::PartitionElement_strategy = st.builds(
    terms::PartitionElement,
)
terms::HLAnnotation_strategy = st.builds(
    terms::HLAnnotation,
)
terms::Condition_strategy = st.builds(
    terms::Condition,
)
terms::HLMarking_strategy = st.builds(
    terms::HLMarking,
)
terms::NamedOperator_strategy = st.builds(
    terms::NamedOperator,
)
terms::Operator_strategy = st.builds(
    terms::Operator,
)
terms::Term_strategy = st.builds(
    terms::Term,
)
Sort_strategy = st.builds(
    Sort,
)
terms::UserSort_strategy = st.builds(
    terms::UserSort,
)
terms::BuiltInSort_strategy = st.builds(
    terms::BuiltInSort,
)
TermsDeclaration_strategy = st.builds(
    TermsDeclaration,
)
terms::OperatorDecl_strategy = st.builds(
    terms::OperatorDecl,
)
terms::SortDecl_strategy = st.builds(
    terms::SortDecl,
)
terms::Partition_strategy = st.builds(
    terms::Partition,
)
terms::Empty_strategy = st.builds(
    terms::Empty,
)
terms::All_strategy = st.builds(
    terms::All,
)
terms::Type_strategy = st.builds(
    terms::Type,
)
terms::ProductSort_strategy = st.builds(
    terms::ProductSort,
)
terms::VariableDecl_strategy = st.builds(
    terms::VariableDecl,
)
terms::NamedSort_strategy = st.builds(
    terms::NamedSort,
)
terms::MultisetSort_strategy = st.builds(
    terms::MultisetSort,
)
terms::Sort_strategy = st.builds(
    terms::Sort,
)
terms::MakeList_strategy = st.builds(
    terms::MakeList,
)
terms::EmptyList_strategy = st.builds(
    terms::EmptyList,
)
terms::HLPNList_strategy = st.builds(
    terms::HLPNList,
)
terms::TermsDeclaration_strategy = st.builds(
    terms::TermsDeclaration,
    name=
        safe_text,
    id=
        safe_text
)
terms::Declarations_strategy = st.builds(
    terms::Declarations,
)
terms::Declaration_strategy = st.builds(
    terms::Declaration,
)

@given(instance=OperatorDecl_strategy)
@settings(max_examples=50)
def test_operatordecl_instantiation(instance):
    assert isinstance(instance, OperatorDecl)

@given(instance=SortDecl_strategy)
@settings(max_examples=50)
def test_sortdecl_instantiation(instance):
    assert isinstance(instance, SortDecl)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=terms::BuiltInOperator_strategy)
@settings(max_examples=50)
def test_terms::builtinoperator_instantiation(instance):
    assert isinstance(instance, terms::BuiltInOperator)

@given(instance=terms::Tuple_strategy)
@settings(max_examples=50)
def test_terms::tuple_instantiation(instance):
    assert isinstance(instance, terms::Tuple)

@given(instance=terms::UserOperator_strategy)
@settings(max_examples=50)
def test_terms::useroperator_instantiation(instance):
    assert isinstance(instance, terms::UserOperator)

@given(instance=terms::MultisetOperator_strategy)
@settings(max_examples=50)
def test_terms::multisetoperator_instantiation(instance):
    assert isinstance(instance, terms::MultisetOperator)

@given(instance=terms::BuiltInConstant_strategy)
@settings(max_examples=50)
def test_terms::builtinconstant_instantiation(instance):
    assert isinstance(instance, terms::BuiltInConstant)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=terms::Variable_strategy)
@settings(max_examples=50)
def test_terms::variable_instantiation(instance):
    assert isinstance(instance, terms::Variable)

@given(instance=terms::PartitionElement_strategy)
@settings(max_examples=50)
def test_terms::partitionelement_instantiation(instance):
    assert isinstance(instance, terms::PartitionElement)

@given(instance=terms::HLAnnotation_strategy)
@settings(max_examples=50)
def test_terms::hlannotation_instantiation(instance):
    assert isinstance(instance, terms::HLAnnotation)

@given(instance=terms::Condition_strategy)
@settings(max_examples=50)
def test_terms::condition_instantiation(instance):
    assert isinstance(instance, terms::Condition)

@given(instance=terms::HLMarking_strategy)
@settings(max_examples=50)
def test_terms::hlmarking_instantiation(instance):
    assert isinstance(instance, terms::HLMarking)

@given(instance=terms::NamedOperator_strategy)
@settings(max_examples=50)
def test_terms::namedoperator_instantiation(instance):
    assert isinstance(instance, terms::NamedOperator)

@given(instance=terms::Operator_strategy)
@settings(max_examples=50)
def test_terms::operator_instantiation(instance):
    assert isinstance(instance, terms::Operator)

@given(instance=terms::Term_strategy)
@settings(max_examples=50)
def test_terms::term_instantiation(instance):
    assert isinstance(instance, terms::Term)

@given(instance=Sort_strategy)
@settings(max_examples=50)
def test_sort_instantiation(instance):
    assert isinstance(instance, Sort)

@given(instance=terms::UserSort_strategy)
@settings(max_examples=50)
def test_terms::usersort_instantiation(instance):
    assert isinstance(instance, terms::UserSort)

@given(instance=terms::BuiltInSort_strategy)
@settings(max_examples=50)
def test_terms::builtinsort_instantiation(instance):
    assert isinstance(instance, terms::BuiltInSort)

@given(instance=TermsDeclaration_strategy)
@settings(max_examples=50)
def test_termsdeclaration_instantiation(instance):
    assert isinstance(instance, TermsDeclaration)

@given(instance=terms::OperatorDecl_strategy)
@settings(max_examples=50)
def test_terms::operatordecl_instantiation(instance):
    assert isinstance(instance, terms::OperatorDecl)

@given(instance=terms::SortDecl_strategy)
@settings(max_examples=50)
def test_terms::sortdecl_instantiation(instance):
    assert isinstance(instance, terms::SortDecl)

@given(instance=terms::Partition_strategy)
@settings(max_examples=50)
def test_terms::partition_instantiation(instance):
    assert isinstance(instance, terms::Partition)

@given(instance=terms::Empty_strategy)
@settings(max_examples=50)
def test_terms::empty_instantiation(instance):
    assert isinstance(instance, terms::Empty)

@given(instance=terms::All_strategy)
@settings(max_examples=50)
def test_terms::all_instantiation(instance):
    assert isinstance(instance, terms::All)

@given(instance=terms::Type_strategy)
@settings(max_examples=50)
def test_terms::type_instantiation(instance):
    assert isinstance(instance, terms::Type)

@given(instance=terms::ProductSort_strategy)
@settings(max_examples=50)
def test_terms::productsort_instantiation(instance):
    assert isinstance(instance, terms::ProductSort)

@given(instance=terms::VariableDecl_strategy)
@settings(max_examples=50)
def test_terms::variabledecl_instantiation(instance):
    assert isinstance(instance, terms::VariableDecl)

@given(instance=terms::NamedSort_strategy)
@settings(max_examples=50)
def test_terms::namedsort_instantiation(instance):
    assert isinstance(instance, terms::NamedSort)

@given(instance=terms::MultisetSort_strategy)
@settings(max_examples=50)
def test_terms::multisetsort_instantiation(instance):
    assert isinstance(instance, terms::MultisetSort)

@given(instance=terms::Sort_strategy)
@settings(max_examples=50)
def test_terms::sort_instantiation(instance):
    assert isinstance(instance, terms::Sort)

@given(instance=terms::MakeList_strategy)
@settings(max_examples=50)
def test_terms::makelist_instantiation(instance):
    assert isinstance(instance, terms::MakeList)

@given(instance=terms::EmptyList_strategy)
@settings(max_examples=50)
def test_terms::emptylist_instantiation(instance):
    assert isinstance(instance, terms::EmptyList)

@given(instance=terms::HLPNList_strategy)
@settings(max_examples=50)
def test_terms::hlpnlist_instantiation(instance):
    assert isinstance(instance, terms::HLPNList)

@given(instance=terms::TermsDeclaration_strategy)
@settings(max_examples=50)
def test_terms::termsdeclaration_instantiation(instance):
    assert isinstance(instance, terms::TermsDeclaration)

@given(instance=terms::TermsDeclaration_strategy)
def test_terms::termsdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=terms::TermsDeclaration_strategy)
def test_terms::termsdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=terms::TermsDeclaration_strategy)
def test_terms::termsdeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=terms::TermsDeclaration_strategy)
def test_terms::termsdeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=terms::Declarations_strategy)
@settings(max_examples=50)
def test_terms::declarations_instantiation(instance):
    assert isinstance(instance, terms::Declarations)

@given(instance=terms::Declaration_strategy)
@settings(max_examples=50)
def test_terms::declaration_instantiation(instance):
    assert isinstance(instance, terms::Declaration)

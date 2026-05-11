import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Atom,
    game::Cell,
    Index,
    game::Atom,
    Setable,
    game::SetExpression,
    Collection,
    game::Join,
    game::ImplicitSet,
    game::Brackets,
    Primary,
    game::LogicalNot,
    game::Collection,
    game::Index,
    game::Cardinal,
    game::Primary,
    game::Call,
    game::Variable,
    game::Expression,
    Statement,
    game::Forall,
    game::Assignment,
    game::Iteration,
    game::Subprocess,
    Multipliable,
    game::Multiplication,
    game::Setable,
    Addable,
    game::Addition,
    game::Multipliable,
    Comparable,
    game::Comparison,
    game::Addable,
    Equatable,
    game::Equality,
    game::Comparable,
    Andable,
    game::And,
    game::Equatable,
    Orable,
    game::Or,
    game::Andable,
    Expression,
    game::Orable,
    game::Function,
    game::End,
    game::ComponentData,
    game::System,
    game::Type,
    game::Game,
    game::Selection,
    game::Access,
    game::Query,
    game::Statement,
    AccessKind,
    MultiplicativeKind,
    AdditiveKind,
    EqualityKind,
    ComparisonKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_game::cell_is_not_abstract():
    assert not inspect.isabstract(game::Cell)


def test_game::cell_constructor_exists():
    assert callable(game::Cell.__init__)


def test_game::cell_constructor_args():
    sig = inspect.signature(game::Cell.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_game::atom_is_not_abstract():
    assert not inspect.isabstract(game::Atom)


def test_game::atom_constructor_exists():
    assert callable(game::Atom.__init__)


def test_game::atom_constructor_args():
    sig = inspect.signature(game::Atom.__init__)
    params = list(sig.parameters.keys())



def test_setable_is_not_abstract():
    assert not inspect.isabstract(Setable)


def test_setable_constructor_exists():
    assert callable(Setable.__init__)


def test_setable_constructor_args():
    sig = inspect.signature(Setable.__init__)
    params = list(sig.parameters.keys())



def test_game::setexpression_is_not_abstract():
    assert not inspect.isabstract(game::SetExpression)


def test_game::setexpression_constructor_exists():
    assert callable(game::SetExpression.__init__)


def test_game::setexpression_constructor_args():
    sig = inspect.signature(game::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())



def test_game::join_is_not_abstract():
    assert not inspect.isabstract(game::Join)


def test_game::join_constructor_exists():
    assert callable(game::Join.__init__)


def test_game::join_constructor_args():
    sig = inspect.signature(game::Join.__init__)
    params = list(sig.parameters.keys())



def test_game::implicitset_is_not_abstract():
    assert not inspect.isabstract(game::ImplicitSet)


def test_game::implicitset_constructor_exists():
    assert callable(game::ImplicitSet.__init__)


def test_game::implicitset_constructor_args():
    sig = inspect.signature(game::ImplicitSet.__init__)
    params = list(sig.parameters.keys())



def test_game::brackets_is_not_abstract():
    assert not inspect.isabstract(game::Brackets)


def test_game::brackets_constructor_exists():
    assert callable(game::Brackets.__init__)


def test_game::brackets_constructor_args():
    sig = inspect.signature(game::Brackets.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_game::logicalnot_is_not_abstract():
    assert not inspect.isabstract(game::LogicalNot)


def test_game::logicalnot_constructor_exists():
    assert callable(game::LogicalNot.__init__)


def test_game::logicalnot_constructor_args():
    sig = inspect.signature(game::LogicalNot.__init__)
    params = list(sig.parameters.keys())



def test_game::collection_is_not_abstract():
    assert not inspect.isabstract(game::Collection)


def test_game::collection_constructor_exists():
    assert callable(game::Collection.__init__)


def test_game::collection_constructor_args():
    sig = inspect.signature(game::Collection.__init__)
    params = list(sig.parameters.keys())



def test_game::index_is_not_abstract():
    assert not inspect.isabstract(game::Index)


def test_game::index_constructor_exists():
    assert callable(game::Index.__init__)


def test_game::index_constructor_args():
    sig = inspect.signature(game::Index.__init__)
    params = list(sig.parameters.keys())



def test_game::cardinal_is_not_abstract():
    assert not inspect.isabstract(game::Cardinal)


def test_game::cardinal_constructor_exists():
    assert callable(game::Cardinal.__init__)


def test_game::cardinal_constructor_args():
    sig = inspect.signature(game::Cardinal.__init__)
    params = list(sig.parameters.keys())



def test_game::primary_is_not_abstract():
    assert not inspect.isabstract(game::Primary)


def test_game::primary_constructor_exists():
    assert callable(game::Primary.__init__)


def test_game::primary_constructor_args():
    sig = inspect.signature(game::Primary.__init__)
    params = list(sig.parameters.keys())



def test_game::call_is_not_abstract():
    assert not inspect.isabstract(game::Call)


def test_game::call_constructor_exists():
    assert callable(game::Call.__init__)


def test_game::call_constructor_args():
    sig = inspect.signature(game::Call.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::call_has_name():
    assert hasattr(game::Call, "name")
    descriptor = None
    for klass in game::Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::variable_is_not_abstract():
    assert not inspect.isabstract(game::Variable)


def test_game::variable_constructor_exists():
    assert callable(game::Variable.__init__)


def test_game::variable_constructor_args():
    sig = inspect.signature(game::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::variable_has_name():
    assert hasattr(game::Variable, "name")
    descriptor = None
    for klass in game::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::expression_is_not_abstract():
    assert not inspect.isabstract(game::Expression)


def test_game::expression_constructor_exists():
    assert callable(game::Expression.__init__)


def test_game::expression_constructor_args():
    sig = inspect.signature(game::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_game::forall_is_not_abstract():
    assert not inspect.isabstract(game::Forall)


def test_game::forall_constructor_exists():
    assert callable(game::Forall.__init__)


def test_game::forall_constructor_args():
    sig = inspect.signature(game::Forall.__init__)
    params = list(sig.parameters.keys())



def test_game::assignment_is_not_abstract():
    assert not inspect.isabstract(game::Assignment)


def test_game::assignment_constructor_exists():
    assert callable(game::Assignment.__init__)


def test_game::assignment_constructor_args():
    sig = inspect.signature(game::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_game::iteration_is_not_abstract():
    assert not inspect.isabstract(game::Iteration)


def test_game::iteration_constructor_exists():
    assert callable(game::Iteration.__init__)


def test_game::iteration_constructor_args():
    sig = inspect.signature(game::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_game::subprocess_is_not_abstract():
    assert not inspect.isabstract(game::Subprocess)


def test_game::subprocess_constructor_exists():
    assert callable(game::Subprocess.__init__)


def test_game::subprocess_constructor_args():
    sig = inspect.signature(game::Subprocess.__init__)
    params = list(sig.parameters.keys())



def test_multipliable_is_not_abstract():
    assert not inspect.isabstract(Multipliable)


def test_multipliable_constructor_exists():
    assert callable(Multipliable.__init__)


def test_multipliable_constructor_args():
    sig = inspect.signature(Multipliable.__init__)
    params = list(sig.parameters.keys())



def test_game::multiplication_is_not_abstract():
    assert not inspect.isabstract(game::Multiplication)


def test_game::multiplication_constructor_exists():
    assert callable(game::Multiplication.__init__)


def test_game::multiplication_constructor_args():
    sig = inspect.signature(game::Multiplication.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game::multiplication_has_kind():
    assert hasattr(game::Multiplication, "kind")
    descriptor = None
    for klass in game::Multiplication.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game::setable_is_not_abstract():
    assert not inspect.isabstract(game::Setable)


def test_game::setable_constructor_exists():
    assert callable(game::Setable.__init__)


def test_game::setable_constructor_args():
    sig = inspect.signature(game::Setable.__init__)
    params = list(sig.parameters.keys())



def test_addable_is_not_abstract():
    assert not inspect.isabstract(Addable)


def test_addable_constructor_exists():
    assert callable(Addable.__init__)


def test_addable_constructor_args():
    sig = inspect.signature(Addable.__init__)
    params = list(sig.parameters.keys())



def test_game::addition_is_not_abstract():
    assert not inspect.isabstract(game::Addition)


def test_game::addition_constructor_exists():
    assert callable(game::Addition.__init__)


def test_game::addition_constructor_args():
    sig = inspect.signature(game::Addition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game::addition_has_kind():
    assert hasattr(game::Addition, "kind")
    descriptor = None
    for klass in game::Addition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game::multipliable_is_not_abstract():
    assert not inspect.isabstract(game::Multipliable)


def test_game::multipliable_constructor_exists():
    assert callable(game::Multipliable.__init__)


def test_game::multipliable_constructor_args():
    sig = inspect.signature(game::Multipliable.__init__)
    params = list(sig.parameters.keys())



def test_comparable_is_not_abstract():
    assert not inspect.isabstract(Comparable)


def test_comparable_constructor_exists():
    assert callable(Comparable.__init__)


def test_comparable_constructor_args():
    sig = inspect.signature(Comparable.__init__)
    params = list(sig.parameters.keys())



def test_game::comparison_is_not_abstract():
    assert not inspect.isabstract(game::Comparison)


def test_game::comparison_constructor_exists():
    assert callable(game::Comparison.__init__)


def test_game::comparison_constructor_args():
    sig = inspect.signature(game::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game::comparison_has_kind():
    assert hasattr(game::Comparison, "kind")
    descriptor = None
    for klass in game::Comparison.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game::addable_is_not_abstract():
    assert not inspect.isabstract(game::Addable)


def test_game::addable_constructor_exists():
    assert callable(game::Addable.__init__)


def test_game::addable_constructor_args():
    sig = inspect.signature(game::Addable.__init__)
    params = list(sig.parameters.keys())



def test_equatable_is_not_abstract():
    assert not inspect.isabstract(Equatable)


def test_equatable_constructor_exists():
    assert callable(Equatable.__init__)


def test_equatable_constructor_args():
    sig = inspect.signature(Equatable.__init__)
    params = list(sig.parameters.keys())



def test_game::equality_is_not_abstract():
    assert not inspect.isabstract(game::Equality)


def test_game::equality_constructor_exists():
    assert callable(game::Equality.__init__)


def test_game::equality_constructor_args():
    sig = inspect.signature(game::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game::equality_has_kind():
    assert hasattr(game::Equality, "kind")
    descriptor = None
    for klass in game::Equality.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game::comparable_is_not_abstract():
    assert not inspect.isabstract(game::Comparable)


def test_game::comparable_constructor_exists():
    assert callable(game::Comparable.__init__)


def test_game::comparable_constructor_args():
    sig = inspect.signature(game::Comparable.__init__)
    params = list(sig.parameters.keys())



def test_andable_is_not_abstract():
    assert not inspect.isabstract(Andable)


def test_andable_constructor_exists():
    assert callable(Andable.__init__)


def test_andable_constructor_args():
    sig = inspect.signature(Andable.__init__)
    params = list(sig.parameters.keys())



def test_game::and_is_not_abstract():
    assert not inspect.isabstract(game::And)


def test_game::and_constructor_exists():
    assert callable(game::And.__init__)


def test_game::and_constructor_args():
    sig = inspect.signature(game::And.__init__)
    params = list(sig.parameters.keys())



def test_game::equatable_is_not_abstract():
    assert not inspect.isabstract(game::Equatable)


def test_game::equatable_constructor_exists():
    assert callable(game::Equatable.__init__)


def test_game::equatable_constructor_args():
    sig = inspect.signature(game::Equatable.__init__)
    params = list(sig.parameters.keys())



def test_orable_is_not_abstract():
    assert not inspect.isabstract(Orable)


def test_orable_constructor_exists():
    assert callable(Orable.__init__)


def test_orable_constructor_args():
    sig = inspect.signature(Orable.__init__)
    params = list(sig.parameters.keys())



def test_game::or_is_not_abstract():
    assert not inspect.isabstract(game::Or)


def test_game::or_constructor_exists():
    assert callable(game::Or.__init__)


def test_game::or_constructor_args():
    sig = inspect.signature(game::Or.__init__)
    params = list(sig.parameters.keys())



def test_game::andable_is_not_abstract():
    assert not inspect.isabstract(game::Andable)


def test_game::andable_constructor_exists():
    assert callable(game::Andable.__init__)


def test_game::andable_constructor_args():
    sig = inspect.signature(game::Andable.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_game::orable_is_not_abstract():
    assert not inspect.isabstract(game::Orable)


def test_game::orable_constructor_exists():
    assert callable(game::Orable.__init__)


def test_game::orable_constructor_args():
    sig = inspect.signature(game::Orable.__init__)
    params = list(sig.parameters.keys())



def test_game::function_is_not_abstract():
    assert not inspect.isabstract(game::Function)


def test_game::function_constructor_exists():
    assert callable(game::Function.__init__)


def test_game::function_constructor_args():
    sig = inspect.signature(game::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::function_has_name():
    assert hasattr(game::Function, "name")
    descriptor = None
    for klass in game::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::end_is_not_abstract():
    assert not inspect.isabstract(game::End)


def test_game::end_constructor_exists():
    assert callable(game::End.__init__)


def test_game::end_constructor_args():
    sig = inspect.signature(game::End.__init__)
    params = list(sig.parameters.keys())



def test_game::componentdata_is_not_abstract():
    assert not inspect.isabstract(game::ComponentData)


def test_game::componentdata_constructor_exists():
    assert callable(game::ComponentData.__init__)


def test_game::componentdata_constructor_args():
    sig = inspect.signature(game::ComponentData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::componentdata_has_name():
    assert hasattr(game::ComponentData, "name")
    descriptor = None
    for klass in game::ComponentData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::system_is_not_abstract():
    assert not inspect.isabstract(game::System)


def test_game::system_constructor_exists():
    assert callable(game::System.__init__)


def test_game::system_constructor_args():
    sig = inspect.signature(game::System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::system_has_name():
    assert hasattr(game::System, "name")
    descriptor = None
    for klass in game::System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::type_is_not_abstract():
    assert not inspect.isabstract(game::Type)


def test_game::type_constructor_exists():
    assert callable(game::Type.__init__)


def test_game::type_constructor_args():
    sig = inspect.signature(game::Type.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "name" in params, "Missing parameter 'name'"

def test_game::type_has_namespace():
    assert hasattr(game::Type, "namespace")
    descriptor = None
    for klass in game::Type.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_game::type_has_valueType():
    assert hasattr(game::Type, "valueType")
    descriptor = None
    for klass in game::Type.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_game::type_has_name():
    assert hasattr(game::Type, "name")
    descriptor = None
    for klass in game::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::game_is_not_abstract():
    assert not inspect.isabstract(game::Game)


def test_game::game_constructor_exists():
    assert callable(game::Game.__init__)


def test_game::game_constructor_args():
    sig = inspect.signature(game::Game.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_game::game_has_version():
    assert hasattr(game::Game, "version")
    descriptor = None
    for klass in game::Game.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_game::game_has_name():
    assert hasattr(game::Game, "name")
    descriptor = None
    for klass in game::Game.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::selection_is_not_abstract():
    assert not inspect.isabstract(game::Selection)


def test_game::selection_constructor_exists():
    assert callable(game::Selection.__init__)


def test_game::selection_constructor_args():
    sig = inspect.signature(game::Selection.__init__)
    params = list(sig.parameters.keys())



def test_game::access_is_not_abstract():
    assert not inspect.isabstract(game::Access)


def test_game::access_constructor_exists():
    assert callable(game::Access.__init__)


def test_game::access_constructor_args():
    sig = inspect.signature(game::Access.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_game::access_has_kind():
    assert hasattr(game::Access, "kind")
    descriptor = None
    for klass in game::Access.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_game::access_has_name():
    assert hasattr(game::Access, "name")
    descriptor = None
    for klass in game::Access.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::query_is_not_abstract():
    assert not inspect.isabstract(game::Query)


def test_game::query_constructor_exists():
    assert callable(game::Query.__init__)


def test_game::query_constructor_args():
    sig = inspect.signature(game::Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game::query_has_name():
    assert hasattr(game::Query, "name")
    descriptor = None
    for klass in game::Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game::statement_is_not_abstract():
    assert not inspect.isabstract(game::Statement)


def test_game::statement_constructor_exists():
    assert callable(game::Statement.__init__)


def test_game::statement_constructor_args():
    sig = inspect.signature(game::Statement.__init__)
    params = list(sig.parameters.keys())

def test_accesskind_exists():
    # Check that the Enumeration exists
    assert AccessKind is not None

def test_accesskind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessKind]
    expected_literals = [
        "write",
        "exist",
        "read",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessKind"

def test_multiplicativekind_exists():
    # Check that the Enumeration exists
    assert MultiplicativeKind is not None

def test_multiplicativekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeKind]
    expected_literals = [
        "divide",
        "multiply",
        "remainder",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeKind"

def test_additivekind_exists():
    # Check that the Enumeration exists
    assert AdditiveKind is not None

def test_additivekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveKind]
    expected_literals = [
        "add",
        "subtract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveKind"

def test_equalitykind_exists():
    # Check that the Enumeration exists
    assert EqualityKind is not None

def test_equalitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityKind]
    expected_literals = [
        "equal",
        "notEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityKind"

def test_comparisonkind_exists():
    # Check that the Enumeration exists
    assert ComparisonKind is not None

def test_comparisonkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonKind]
    expected_literals = [
        "greaterOrEqual",
        "greater",
        "lower",
        "lowerOrEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonKind"


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
Atom_strategy = st.builds(
    Atom,
)
game::Cell_strategy = st.builds(
    game::Cell,
)
Index_strategy = st.builds(
    Index,
)
game::Atom_strategy = st.builds(
    game::Atom,
)
Setable_strategy = st.builds(
    Setable,
)
game::SetExpression_strategy = st.builds(
    game::SetExpression,
)
Collection_strategy = st.builds(
    Collection,
)
game::Join_strategy = st.builds(
    game::Join,
)
game::ImplicitSet_strategy = st.builds(
    game::ImplicitSet,
)
game::Brackets_strategy = st.builds(
    game::Brackets,
)
Primary_strategy = st.builds(
    Primary,
)
game::LogicalNot_strategy = st.builds(
    game::LogicalNot,
)
game::Collection_strategy = st.builds(
    game::Collection,
)
game::Index_strategy = st.builds(
    game::Index,
)
game::Cardinal_strategy = st.builds(
    game::Cardinal,
)
game::Primary_strategy = st.builds(
    game::Primary,
)
game::Call_strategy = st.builds(
    game::Call,
    name=
        safe_text
)
game::Variable_strategy = st.builds(
    game::Variable,
    name=
        safe_text
)
game::Expression_strategy = st.builds(
    game::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
game::Forall_strategy = st.builds(
    game::Forall,
)
game::Assignment_strategy = st.builds(
    game::Assignment,
)
game::Iteration_strategy = st.builds(
    game::Iteration,
)
game::Subprocess_strategy = st.builds(
    game::Subprocess,
)
Multipliable_strategy = st.builds(
    Multipliable,
)
game::Multiplication_strategy = st.builds(
    game::Multiplication,
    kind=
        safe_text
)
game::Setable_strategy = st.builds(
    game::Setable,
)
Addable_strategy = st.builds(
    Addable,
)
game::Addition_strategy = st.builds(
    game::Addition,
    kind=
        safe_text
)
game::Multipliable_strategy = st.builds(
    game::Multipliable,
)
Comparable_strategy = st.builds(
    Comparable,
)
game::Comparison_strategy = st.builds(
    game::Comparison,
    kind=
        safe_text
)
game::Addable_strategy = st.builds(
    game::Addable,
)
Equatable_strategy = st.builds(
    Equatable,
)
game::Equality_strategy = st.builds(
    game::Equality,
    kind=
        safe_text
)
game::Comparable_strategy = st.builds(
    game::Comparable,
)
Andable_strategy = st.builds(
    Andable,
)
game::And_strategy = st.builds(
    game::And,
)
game::Equatable_strategy = st.builds(
    game::Equatable,
)
Orable_strategy = st.builds(
    Orable,
)
game::Or_strategy = st.builds(
    game::Or,
)
game::Andable_strategy = st.builds(
    game::Andable,
)
Expression_strategy = st.builds(
    Expression,
)
game::Orable_strategy = st.builds(
    game::Orable,
)
game::Function_strategy = st.builds(
    game::Function,
    name=
        safe_text
)
game::End_strategy = st.builds(
    game::End,
)
game::ComponentData_strategy = st.builds(
    game::ComponentData,
    name=
        safe_text
)
game::System_strategy = st.builds(
    game::System,
    name=
        safe_text
)
game::Type_strategy = st.builds(
    game::Type,
    namespace=
        safe_text,
    valueType=
        st.booleans(),
    name=
        safe_text
)
game::Game_strategy = st.builds(
    game::Game,
    version=
        safe_text,
    name=
        safe_text
)
game::Selection_strategy = st.builds(
    game::Selection,
)
game::Access_strategy = st.builds(
    game::Access,
    kind=
        safe_text,
    name=
        safe_text
)
game::Query_strategy = st.builds(
    game::Query,
    name=
        safe_text
)
game::Statement_strategy = st.builds(
    game::Statement,
)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=game::Cell_strategy)
@settings(max_examples=50)
def test_game::cell_instantiation(instance):
    assert isinstance(instance, game::Cell)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=game::Atom_strategy)
@settings(max_examples=50)
def test_game::atom_instantiation(instance):
    assert isinstance(instance, game::Atom)

@given(instance=Setable_strategy)
@settings(max_examples=50)
def test_setable_instantiation(instance):
    assert isinstance(instance, Setable)

@given(instance=game::SetExpression_strategy)
@settings(max_examples=50)
def test_game::setexpression_instantiation(instance):
    assert isinstance(instance, game::SetExpression)

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)

@given(instance=game::Join_strategy)
@settings(max_examples=50)
def test_game::join_instantiation(instance):
    assert isinstance(instance, game::Join)

@given(instance=game::ImplicitSet_strategy)
@settings(max_examples=50)
def test_game::implicitset_instantiation(instance):
    assert isinstance(instance, game::ImplicitSet)

@given(instance=game::Brackets_strategy)
@settings(max_examples=50)
def test_game::brackets_instantiation(instance):
    assert isinstance(instance, game::Brackets)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=game::LogicalNot_strategy)
@settings(max_examples=50)
def test_game::logicalnot_instantiation(instance):
    assert isinstance(instance, game::LogicalNot)

@given(instance=game::Collection_strategy)
@settings(max_examples=50)
def test_game::collection_instantiation(instance):
    assert isinstance(instance, game::Collection)

@given(instance=game::Index_strategy)
@settings(max_examples=50)
def test_game::index_instantiation(instance):
    assert isinstance(instance, game::Index)

@given(instance=game::Cardinal_strategy)
@settings(max_examples=50)
def test_game::cardinal_instantiation(instance):
    assert isinstance(instance, game::Cardinal)

@given(instance=game::Primary_strategy)
@settings(max_examples=50)
def test_game::primary_instantiation(instance):
    assert isinstance(instance, game::Primary)

@given(instance=game::Call_strategy)
@settings(max_examples=50)
def test_game::call_instantiation(instance):
    assert isinstance(instance, game::Call)

@given(instance=game::Call_strategy)
def test_game::call_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Call_strategy)
def test_game::call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Variable_strategy)
@settings(max_examples=50)
def test_game::variable_instantiation(instance):
    assert isinstance(instance, game::Variable)

@given(instance=game::Variable_strategy)
def test_game::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Variable_strategy)
def test_game::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Expression_strategy)
@settings(max_examples=50)
def test_game::expression_instantiation(instance):
    assert isinstance(instance, game::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=game::Forall_strategy)
@settings(max_examples=50)
def test_game::forall_instantiation(instance):
    assert isinstance(instance, game::Forall)

@given(instance=game::Assignment_strategy)
@settings(max_examples=50)
def test_game::assignment_instantiation(instance):
    assert isinstance(instance, game::Assignment)

@given(instance=game::Iteration_strategy)
@settings(max_examples=50)
def test_game::iteration_instantiation(instance):
    assert isinstance(instance, game::Iteration)

@given(instance=game::Subprocess_strategy)
@settings(max_examples=50)
def test_game::subprocess_instantiation(instance):
    assert isinstance(instance, game::Subprocess)

@given(instance=Multipliable_strategy)
@settings(max_examples=50)
def test_multipliable_instantiation(instance):
    assert isinstance(instance, Multipliable)

@given(instance=game::Multiplication_strategy)
@settings(max_examples=50)
def test_game::multiplication_instantiation(instance):
    assert isinstance(instance, game::Multiplication)

@given(instance=game::Multiplication_strategy)
def test_game::multiplication_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=game::Multiplication_strategy)
def test_game::multiplication_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game::Setable_strategy)
@settings(max_examples=50)
def test_game::setable_instantiation(instance):
    assert isinstance(instance, game::Setable)

@given(instance=Addable_strategy)
@settings(max_examples=50)
def test_addable_instantiation(instance):
    assert isinstance(instance, Addable)

@given(instance=game::Addition_strategy)
@settings(max_examples=50)
def test_game::addition_instantiation(instance):
    assert isinstance(instance, game::Addition)

@given(instance=game::Addition_strategy)
def test_game::addition_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=game::Addition_strategy)
def test_game::addition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game::Multipliable_strategy)
@settings(max_examples=50)
def test_game::multipliable_instantiation(instance):
    assert isinstance(instance, game::Multipliable)

@given(instance=Comparable_strategy)
@settings(max_examples=50)
def test_comparable_instantiation(instance):
    assert isinstance(instance, Comparable)

@given(instance=game::Comparison_strategy)
@settings(max_examples=50)
def test_game::comparison_instantiation(instance):
    assert isinstance(instance, game::Comparison)

@given(instance=game::Comparison_strategy)
def test_game::comparison_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=game::Comparison_strategy)
def test_game::comparison_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game::Addable_strategy)
@settings(max_examples=50)
def test_game::addable_instantiation(instance):
    assert isinstance(instance, game::Addable)

@given(instance=Equatable_strategy)
@settings(max_examples=50)
def test_equatable_instantiation(instance):
    assert isinstance(instance, Equatable)

@given(instance=game::Equality_strategy)
@settings(max_examples=50)
def test_game::equality_instantiation(instance):
    assert isinstance(instance, game::Equality)

@given(instance=game::Equality_strategy)
def test_game::equality_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=game::Equality_strategy)
def test_game::equality_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game::Comparable_strategy)
@settings(max_examples=50)
def test_game::comparable_instantiation(instance):
    assert isinstance(instance, game::Comparable)

@given(instance=Andable_strategy)
@settings(max_examples=50)
def test_andable_instantiation(instance):
    assert isinstance(instance, Andable)

@given(instance=game::And_strategy)
@settings(max_examples=50)
def test_game::and_instantiation(instance):
    assert isinstance(instance, game::And)

@given(instance=game::Equatable_strategy)
@settings(max_examples=50)
def test_game::equatable_instantiation(instance):
    assert isinstance(instance, game::Equatable)

@given(instance=Orable_strategy)
@settings(max_examples=50)
def test_orable_instantiation(instance):
    assert isinstance(instance, Orable)

@given(instance=game::Or_strategy)
@settings(max_examples=50)
def test_game::or_instantiation(instance):
    assert isinstance(instance, game::Or)

@given(instance=game::Andable_strategy)
@settings(max_examples=50)
def test_game::andable_instantiation(instance):
    assert isinstance(instance, game::Andable)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=game::Orable_strategy)
@settings(max_examples=50)
def test_game::orable_instantiation(instance):
    assert isinstance(instance, game::Orable)

@given(instance=game::Function_strategy)
@settings(max_examples=50)
def test_game::function_instantiation(instance):
    assert isinstance(instance, game::Function)

@given(instance=game::Function_strategy)
def test_game::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Function_strategy)
def test_game::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::End_strategy)
@settings(max_examples=50)
def test_game::end_instantiation(instance):
    assert isinstance(instance, game::End)

@given(instance=game::ComponentData_strategy)
@settings(max_examples=50)
def test_game::componentdata_instantiation(instance):
    assert isinstance(instance, game::ComponentData)

@given(instance=game::ComponentData_strategy)
def test_game::componentdata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::ComponentData_strategy)
def test_game::componentdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::System_strategy)
@settings(max_examples=50)
def test_game::system_instantiation(instance):
    assert isinstance(instance, game::System)

@given(instance=game::System_strategy)
def test_game::system_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::System_strategy)
def test_game::system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Type_strategy)
@settings(max_examples=50)
def test_game::type_instantiation(instance):
    assert isinstance(instance, game::Type)

@given(instance=game::Type_strategy)
def test_game::type_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=game::Type_strategy)
def test_game::type_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=game::Type_strategy)
def test_game::type_valueType_type(instance):
    assert isinstance(instance.valueType, bool)


@given(instance=game::Type_strategy)
def test_game::type_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original

@given(instance=game::Type_strategy)
def test_game::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Type_strategy)
def test_game::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Game_strategy)
@settings(max_examples=50)
def test_game::game_instantiation(instance):
    assert isinstance(instance, game::Game)

@given(instance=game::Game_strategy)
def test_game::game_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=game::Game_strategy)
def test_game::game_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=game::Game_strategy)
def test_game::game_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Game_strategy)
def test_game::game_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Selection_strategy)
@settings(max_examples=50)
def test_game::selection_instantiation(instance):
    assert isinstance(instance, game::Selection)

@given(instance=game::Access_strategy)
@settings(max_examples=50)
def test_game::access_instantiation(instance):
    assert isinstance(instance, game::Access)

@given(instance=game::Access_strategy)
def test_game::access_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=game::Access_strategy)
def test_game::access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game::Access_strategy)
def test_game::access_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Access_strategy)
def test_game::access_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Query_strategy)
@settings(max_examples=50)
def test_game::query_instantiation(instance):
    assert isinstance(instance, game::Query)

@given(instance=game::Query_strategy)
def test_game::query_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=game::Query_strategy)
def test_game::query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game::Statement_strategy)
@settings(max_examples=50)
def test_game::statement_instantiation(instance):
    assert isinstance(instance, game::Statement)

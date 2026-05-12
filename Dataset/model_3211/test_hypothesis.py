import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    game_Orable,
    game_Function,
    game_End,
    game_ComponentData,
    game_System,
    game_Type,
    game_Game,
    game_Access,
    game_Query,
    game_Statement,
    Atom,
    game_Cell,
    Index,
    game_Atom,
    Setable,
    game_SetExpression,
    Collection,
    game_Join,
    game_ImplicitSet,
    game_Brackets,
    Primary,
    game_Cardinal,
    game_LogicalNot,
    game_Collection,
    game_Index,
    game_Primary,
    game_Call,
    game_Variable,
    game_Expression,
    Statement,
    game_Selection,
    game_Forall,
    game_Iteration,
    game_Assignment,
    game_Subprocess,
    Multipliable,
    game_Multiplication,
    game_Setable,
    Addable,
    game_Addition,
    game_Multipliable,
    Comparable,
    game_Comparison,
    game_Addable,
    Equatable,
    game_Equality,
    game_Comparable,
    Andable,
    game_And,
    game_Equatable,
    Orable,
    game_Andable,
    game_Or,
    EqualityKind,
    AccessKind,
    MultiplicativeKind,
    AdditiveKind,
    ComparisonKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_game_orable_is_not_abstract():
    assert not inspect.isabstract(game_Orable)


def test_game_orable_constructor_exists():
    assert callable(game_Orable.__init__)


def test_game_orable_constructor_args():
    sig = inspect.signature(game_Orable.__init__)
    params = list(sig.parameters.keys())



def test_game_function_is_not_abstract():
    assert not inspect.isabstract(game_Function)


def test_game_function_constructor_exists():
    assert callable(game_Function.__init__)


def test_game_function_constructor_args():
    sig = inspect.signature(game_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_function_has_name():
    assert hasattr(game_Function, "name")
    descriptor = None
    for klass in game_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_end_is_not_abstract():
    assert not inspect.isabstract(game_End)


def test_game_end_constructor_exists():
    assert callable(game_End.__init__)


def test_game_end_constructor_args():
    sig = inspect.signature(game_End.__init__)
    params = list(sig.parameters.keys())



def test_game_componentdata_is_not_abstract():
    assert not inspect.isabstract(game_ComponentData)


def test_game_componentdata_constructor_exists():
    assert callable(game_ComponentData.__init__)


def test_game_componentdata_constructor_args():
    sig = inspect.signature(game_ComponentData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_componentdata_has_name():
    assert hasattr(game_ComponentData, "name")
    descriptor = None
    for klass in game_ComponentData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_system_is_not_abstract():
    assert not inspect.isabstract(game_System)


def test_game_system_constructor_exists():
    assert callable(game_System.__init__)


def test_game_system_constructor_args():
    sig = inspect.signature(game_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_system_has_name():
    assert hasattr(game_System, "name")
    descriptor = None
    for klass in game_System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_type_is_not_abstract():
    assert not inspect.isabstract(game_Type)


def test_game_type_constructor_exists():
    assert callable(game_Type.__init__)


def test_game_type_constructor_args():
    sig = inspect.signature(game_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "valueType" in params, "Missing parameter 'valueType'"
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_game_type_has_name():
    assert hasattr(game_Type, "name")
    descriptor = None
    for klass in game_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_game_type_has_valueType():
    assert hasattr(game_Type, "valueType")
    descriptor = None
    for klass in game_Type.__mro__:
        if "valueType" in klass.__dict__:
            descriptor = klass.__dict__["valueType"]
            break
    assert isinstance(descriptor, property)

def test_game_type_has_namespace():
    assert hasattr(game_Type, "namespace")
    descriptor = None
    for klass in game_Type.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_game_game_is_not_abstract():
    assert not inspect.isabstract(game_Game)


def test_game_game_constructor_exists():
    assert callable(game_Game.__init__)


def test_game_game_constructor_args():
    sig = inspect.signature(game_Game.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_game_game_has_version():
    assert hasattr(game_Game, "version")
    descriptor = None
    for klass in game_Game.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_game_game_has_name():
    assert hasattr(game_Game, "name")
    descriptor = None
    for klass in game_Game.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_access_is_not_abstract():
    assert not inspect.isabstract(game_Access)


def test_game_access_constructor_exists():
    assert callable(game_Access.__init__)


def test_game_access_constructor_args():
    sig = inspect.signature(game_Access.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_game_access_has_kind():
    assert hasattr(game_Access, "kind")
    descriptor = None
    for klass in game_Access.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_game_access_has_name():
    assert hasattr(game_Access, "name")
    descriptor = None
    for klass in game_Access.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_query_is_not_abstract():
    assert not inspect.isabstract(game_Query)


def test_game_query_constructor_exists():
    assert callable(game_Query.__init__)


def test_game_query_constructor_args():
    sig = inspect.signature(game_Query.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_query_has_name():
    assert hasattr(game_Query, "name")
    descriptor = None
    for klass in game_Query.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_statement_is_not_abstract():
    assert not inspect.isabstract(game_Statement)


def test_game_statement_constructor_exists():
    assert callable(game_Statement.__init__)


def test_game_statement_constructor_args():
    sig = inspect.signature(game_Statement.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_game_cell_is_not_abstract():
    assert not inspect.isabstract(game_Cell)


def test_game_cell_constructor_exists():
    assert callable(game_Cell.__init__)


def test_game_cell_constructor_args():
    sig = inspect.signature(game_Cell.__init__)
    params = list(sig.parameters.keys())



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_game_atom_is_not_abstract():
    assert not inspect.isabstract(game_Atom)


def test_game_atom_constructor_exists():
    assert callable(game_Atom.__init__)


def test_game_atom_constructor_args():
    sig = inspect.signature(game_Atom.__init__)
    params = list(sig.parameters.keys())



def test_setable_is_not_abstract():
    assert not inspect.isabstract(Setable)


def test_setable_constructor_exists():
    assert callable(Setable.__init__)


def test_setable_constructor_args():
    sig = inspect.signature(Setable.__init__)
    params = list(sig.parameters.keys())



def test_game_setexpression_is_not_abstract():
    assert not inspect.isabstract(game_SetExpression)


def test_game_setexpression_constructor_exists():
    assert callable(game_SetExpression.__init__)


def test_game_setexpression_constructor_args():
    sig = inspect.signature(game_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_collection_is_not_abstract():
    assert not inspect.isabstract(Collection)


def test_collection_constructor_exists():
    assert callable(Collection.__init__)


def test_collection_constructor_args():
    sig = inspect.signature(Collection.__init__)
    params = list(sig.parameters.keys())



def test_game_join_is_not_abstract():
    assert not inspect.isabstract(game_Join)


def test_game_join_constructor_exists():
    assert callable(game_Join.__init__)


def test_game_join_constructor_args():
    sig = inspect.signature(game_Join.__init__)
    params = list(sig.parameters.keys())



def test_game_implicitset_is_not_abstract():
    assert not inspect.isabstract(game_ImplicitSet)


def test_game_implicitset_constructor_exists():
    assert callable(game_ImplicitSet.__init__)


def test_game_implicitset_constructor_args():
    sig = inspect.signature(game_ImplicitSet.__init__)
    params = list(sig.parameters.keys())



def test_game_brackets_is_not_abstract():
    assert not inspect.isabstract(game_Brackets)


def test_game_brackets_constructor_exists():
    assert callable(game_Brackets.__init__)


def test_game_brackets_constructor_args():
    sig = inspect.signature(game_Brackets.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_game_cardinal_is_not_abstract():
    assert not inspect.isabstract(game_Cardinal)


def test_game_cardinal_constructor_exists():
    assert callable(game_Cardinal.__init__)


def test_game_cardinal_constructor_args():
    sig = inspect.signature(game_Cardinal.__init__)
    params = list(sig.parameters.keys())



def test_game_logicalnot_is_not_abstract():
    assert not inspect.isabstract(game_LogicalNot)


def test_game_logicalnot_constructor_exists():
    assert callable(game_LogicalNot.__init__)


def test_game_logicalnot_constructor_args():
    sig = inspect.signature(game_LogicalNot.__init__)
    params = list(sig.parameters.keys())



def test_game_collection_is_not_abstract():
    assert not inspect.isabstract(game_Collection)


def test_game_collection_constructor_exists():
    assert callable(game_Collection.__init__)


def test_game_collection_constructor_args():
    sig = inspect.signature(game_Collection.__init__)
    params = list(sig.parameters.keys())



def test_game_index_is_not_abstract():
    assert not inspect.isabstract(game_Index)


def test_game_index_constructor_exists():
    assert callable(game_Index.__init__)


def test_game_index_constructor_args():
    sig = inspect.signature(game_Index.__init__)
    params = list(sig.parameters.keys())



def test_game_primary_is_not_abstract():
    assert not inspect.isabstract(game_Primary)


def test_game_primary_constructor_exists():
    assert callable(game_Primary.__init__)


def test_game_primary_constructor_args():
    sig = inspect.signature(game_Primary.__init__)
    params = list(sig.parameters.keys())



def test_game_call_is_not_abstract():
    assert not inspect.isabstract(game_Call)


def test_game_call_constructor_exists():
    assert callable(game_Call.__init__)


def test_game_call_constructor_args():
    sig = inspect.signature(game_Call.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_call_has_name():
    assert hasattr(game_Call, "name")
    descriptor = None
    for klass in game_Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_variable_is_not_abstract():
    assert not inspect.isabstract(game_Variable)


def test_game_variable_constructor_exists():
    assert callable(game_Variable.__init__)


def test_game_variable_constructor_args():
    sig = inspect.signature(game_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_game_variable_has_name():
    assert hasattr(game_Variable, "name")
    descriptor = None
    for klass in game_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_game_expression_is_not_abstract():
    assert not inspect.isabstract(game_Expression)


def test_game_expression_constructor_exists():
    assert callable(game_Expression.__init__)


def test_game_expression_constructor_args():
    sig = inspect.signature(game_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_game_selection_is_not_abstract():
    assert not inspect.isabstract(game_Selection)


def test_game_selection_constructor_exists():
    assert callable(game_Selection.__init__)


def test_game_selection_constructor_args():
    sig = inspect.signature(game_Selection.__init__)
    params = list(sig.parameters.keys())



def test_game_forall_is_not_abstract():
    assert not inspect.isabstract(game_Forall)


def test_game_forall_constructor_exists():
    assert callable(game_Forall.__init__)


def test_game_forall_constructor_args():
    sig = inspect.signature(game_Forall.__init__)
    params = list(sig.parameters.keys())



def test_game_iteration_is_not_abstract():
    assert not inspect.isabstract(game_Iteration)


def test_game_iteration_constructor_exists():
    assert callable(game_Iteration.__init__)


def test_game_iteration_constructor_args():
    sig = inspect.signature(game_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_game_assignment_is_not_abstract():
    assert not inspect.isabstract(game_Assignment)


def test_game_assignment_constructor_exists():
    assert callable(game_Assignment.__init__)


def test_game_assignment_constructor_args():
    sig = inspect.signature(game_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_game_subprocess_is_not_abstract():
    assert not inspect.isabstract(game_Subprocess)


def test_game_subprocess_constructor_exists():
    assert callable(game_Subprocess.__init__)


def test_game_subprocess_constructor_args():
    sig = inspect.signature(game_Subprocess.__init__)
    params = list(sig.parameters.keys())



def test_multipliable_is_not_abstract():
    assert not inspect.isabstract(Multipliable)


def test_multipliable_constructor_exists():
    assert callable(Multipliable.__init__)


def test_multipliable_constructor_args():
    sig = inspect.signature(Multipliable.__init__)
    params = list(sig.parameters.keys())



def test_game_multiplication_is_not_abstract():
    assert not inspect.isabstract(game_Multiplication)


def test_game_multiplication_constructor_exists():
    assert callable(game_Multiplication.__init__)


def test_game_multiplication_constructor_args():
    sig = inspect.signature(game_Multiplication.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game_multiplication_has_kind():
    assert hasattr(game_Multiplication, "kind")
    descriptor = None
    for klass in game_Multiplication.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game_setable_is_not_abstract():
    assert not inspect.isabstract(game_Setable)


def test_game_setable_constructor_exists():
    assert callable(game_Setable.__init__)


def test_game_setable_constructor_args():
    sig = inspect.signature(game_Setable.__init__)
    params = list(sig.parameters.keys())



def test_addable_is_not_abstract():
    assert not inspect.isabstract(Addable)


def test_addable_constructor_exists():
    assert callable(Addable.__init__)


def test_addable_constructor_args():
    sig = inspect.signature(Addable.__init__)
    params = list(sig.parameters.keys())



def test_game_addition_is_not_abstract():
    assert not inspect.isabstract(game_Addition)


def test_game_addition_constructor_exists():
    assert callable(game_Addition.__init__)


def test_game_addition_constructor_args():
    sig = inspect.signature(game_Addition.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game_addition_has_kind():
    assert hasattr(game_Addition, "kind")
    descriptor = None
    for klass in game_Addition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game_multipliable_is_not_abstract():
    assert not inspect.isabstract(game_Multipliable)


def test_game_multipliable_constructor_exists():
    assert callable(game_Multipliable.__init__)


def test_game_multipliable_constructor_args():
    sig = inspect.signature(game_Multipliable.__init__)
    params = list(sig.parameters.keys())



def test_comparable_is_not_abstract():
    assert not inspect.isabstract(Comparable)


def test_comparable_constructor_exists():
    assert callable(Comparable.__init__)


def test_comparable_constructor_args():
    sig = inspect.signature(Comparable.__init__)
    params = list(sig.parameters.keys())



def test_game_comparison_is_not_abstract():
    assert not inspect.isabstract(game_Comparison)


def test_game_comparison_constructor_exists():
    assert callable(game_Comparison.__init__)


def test_game_comparison_constructor_args():
    sig = inspect.signature(game_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game_comparison_has_kind():
    assert hasattr(game_Comparison, "kind")
    descriptor = None
    for klass in game_Comparison.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game_addable_is_not_abstract():
    assert not inspect.isabstract(game_Addable)


def test_game_addable_constructor_exists():
    assert callable(game_Addable.__init__)


def test_game_addable_constructor_args():
    sig = inspect.signature(game_Addable.__init__)
    params = list(sig.parameters.keys())



def test_equatable_is_not_abstract():
    assert not inspect.isabstract(Equatable)


def test_equatable_constructor_exists():
    assert callable(Equatable.__init__)


def test_equatable_constructor_args():
    sig = inspect.signature(Equatable.__init__)
    params = list(sig.parameters.keys())



def test_game_equality_is_not_abstract():
    assert not inspect.isabstract(game_Equality)


def test_game_equality_constructor_exists():
    assert callable(game_Equality.__init__)


def test_game_equality_constructor_args():
    sig = inspect.signature(game_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_game_equality_has_kind():
    assert hasattr(game_Equality, "kind")
    descriptor = None
    for klass in game_Equality.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_game_comparable_is_not_abstract():
    assert not inspect.isabstract(game_Comparable)


def test_game_comparable_constructor_exists():
    assert callable(game_Comparable.__init__)


def test_game_comparable_constructor_args():
    sig = inspect.signature(game_Comparable.__init__)
    params = list(sig.parameters.keys())



def test_andable_is_not_abstract():
    assert not inspect.isabstract(Andable)


def test_andable_constructor_exists():
    assert callable(Andable.__init__)


def test_andable_constructor_args():
    sig = inspect.signature(Andable.__init__)
    params = list(sig.parameters.keys())



def test_game_and_is_not_abstract():
    assert not inspect.isabstract(game_And)


def test_game_and_constructor_exists():
    assert callable(game_And.__init__)


def test_game_and_constructor_args():
    sig = inspect.signature(game_And.__init__)
    params = list(sig.parameters.keys())



def test_game_equatable_is_not_abstract():
    assert not inspect.isabstract(game_Equatable)


def test_game_equatable_constructor_exists():
    assert callable(game_Equatable.__init__)


def test_game_equatable_constructor_args():
    sig = inspect.signature(game_Equatable.__init__)
    params = list(sig.parameters.keys())



def test_orable_is_not_abstract():
    assert not inspect.isabstract(Orable)


def test_orable_constructor_exists():
    assert callable(Orable.__init__)


def test_orable_constructor_args():
    sig = inspect.signature(Orable.__init__)
    params = list(sig.parameters.keys())



def test_game_andable_is_not_abstract():
    assert not inspect.isabstract(game_Andable)


def test_game_andable_constructor_exists():
    assert callable(game_Andable.__init__)


def test_game_andable_constructor_args():
    sig = inspect.signature(game_Andable.__init__)
    params = list(sig.parameters.keys())



def test_game_or_is_not_abstract():
    assert not inspect.isabstract(game_Or)


def test_game_or_constructor_exists():
    assert callable(game_Or.__init__)


def test_game_or_constructor_args():
    sig = inspect.signature(game_Or.__init__)
    params = list(sig.parameters.keys())

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
        "multiply",
        "divide",
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
        "subtract",
        "add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveKind"

def test_comparisonkind_exists():
    # Check that the Enumeration exists
    assert ComparisonKind is not None

def test_comparisonkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonKind]
    expected_literals = [
        "lowerOrEqual",
        "greater",
        "greaterOrEqual",
        "lower",
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
Expression_strategy = st.builds(
    Expression,
)
game_Orable_strategy = st.builds(
    game_Orable,
)
game_Function_strategy = st.builds(
    game_Function,
    name=
        safe_text
)
game_End_strategy = st.builds(
    game_End,
)
game_ComponentData_strategy = st.builds(
    game_ComponentData,
    name=
        safe_text
)
game_System_strategy = st.builds(
    game_System,
    name=
        safe_text
)
game_Type_strategy = st.builds(
    game_Type,
    name=
        safe_text,
    valueType=
        st.booleans(),
    namespace=
        safe_text
)
game_Game_strategy = st.builds(
    game_Game,
    version=
        safe_text,
    name=
        safe_text
)
game_Access_strategy = st.builds(
    game_Access,
    kind=
        safe_text,
    name=
        safe_text
)
game_Query_strategy = st.builds(
    game_Query,
    name=
        safe_text
)
game_Statement_strategy = st.builds(
    game_Statement,
)
Atom_strategy = st.builds(
    Atom,
)
game_Cell_strategy = st.builds(
    game_Cell,
)
Index_strategy = st.builds(
    Index,
)
game_Atom_strategy = st.builds(
    game_Atom,
)
Setable_strategy = st.builds(
    Setable,
)
game_SetExpression_strategy = st.builds(
    game_SetExpression,
)
Collection_strategy = st.builds(
    Collection,
)
game_Join_strategy = st.builds(
    game_Join,
)
game_ImplicitSet_strategy = st.builds(
    game_ImplicitSet,
)
game_Brackets_strategy = st.builds(
    game_Brackets,
)
Primary_strategy = st.builds(
    Primary,
)
game_Cardinal_strategy = st.builds(
    game_Cardinal,
)
game_LogicalNot_strategy = st.builds(
    game_LogicalNot,
)
game_Collection_strategy = st.builds(
    game_Collection,
)
game_Index_strategy = st.builds(
    game_Index,
)
game_Primary_strategy = st.builds(
    game_Primary,
)
game_Call_strategy = st.builds(
    game_Call,
    name=
        safe_text
)
game_Variable_strategy = st.builds(
    game_Variable,
    name=
        safe_text
)
game_Expression_strategy = st.builds(
    game_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
game_Selection_strategy = st.builds(
    game_Selection,
)
game_Forall_strategy = st.builds(
    game_Forall,
)
game_Iteration_strategy = st.builds(
    game_Iteration,
)
game_Assignment_strategy = st.builds(
    game_Assignment,
)
game_Subprocess_strategy = st.builds(
    game_Subprocess,
)
Multipliable_strategy = st.builds(
    Multipliable,
)
game_Multiplication_strategy = st.builds(
    game_Multiplication,
    kind=
        safe_text
)
game_Setable_strategy = st.builds(
    game_Setable,
)
Addable_strategy = st.builds(
    Addable,
)
game_Addition_strategy = st.builds(
    game_Addition,
    kind=
        safe_text
)
game_Multipliable_strategy = st.builds(
    game_Multipliable,
)
Comparable_strategy = st.builds(
    Comparable,
)
game_Comparison_strategy = st.builds(
    game_Comparison,
    kind=
        safe_text
)
game_Addable_strategy = st.builds(
    game_Addable,
)
Equatable_strategy = st.builds(
    Equatable,
)
game_Equality_strategy = st.builds(
    game_Equality,
    kind=
        safe_text
)
game_Comparable_strategy = st.builds(
    game_Comparable,
)
Andable_strategy = st.builds(
    Andable,
)
game_And_strategy = st.builds(
    game_And,
)
game_Equatable_strategy = st.builds(
    game_Equatable,
)
Orable_strategy = st.builds(
    Orable,
)
game_Andable_strategy = st.builds(
    game_Andable,
)
game_Or_strategy = st.builds(
    game_Or,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=game_Orable_strategy)
@settings(max_examples=50)
def test_game_orable_instantiation(instance):
    assert isinstance(instance, game_Orable)

@given(instance=game_Function_strategy)
@settings(max_examples=50)
def test_game_function_instantiation(instance):
    assert isinstance(instance, game_Function)



@given(instance=game_Function_strategy)
def test_game_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_End_strategy)
@settings(max_examples=50)
def test_game_end_instantiation(instance):
    assert isinstance(instance, game_End)

@given(instance=game_ComponentData_strategy)
@settings(max_examples=50)
def test_game_componentdata_instantiation(instance):
    assert isinstance(instance, game_ComponentData)



@given(instance=game_ComponentData_strategy)
def test_game_componentdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_System_strategy)
@settings(max_examples=50)
def test_game_system_instantiation(instance):
    assert isinstance(instance, game_System)



@given(instance=game_System_strategy)
def test_game_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Type_strategy)
@settings(max_examples=50)
def test_game_type_instantiation(instance):
    assert isinstance(instance, game_Type)



@given(instance=game_Type_strategy)
def test_game_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=game_Type_strategy)
def test_game_type_valueType_setter(instance):
    original = instance.valueType
    instance.valueType = original
    assert instance.valueType == original



@given(instance=game_Type_strategy)
def test_game_type_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=game_Game_strategy)
@settings(max_examples=50)
def test_game_game_instantiation(instance):
    assert isinstance(instance, game_Game)



@given(instance=game_Game_strategy)
def test_game_game_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=game_Game_strategy)
def test_game_game_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Access_strategy)
@settings(max_examples=50)
def test_game_access_instantiation(instance):
    assert isinstance(instance, game_Access)



@given(instance=game_Access_strategy)
def test_game_access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=game_Access_strategy)
def test_game_access_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Query_strategy)
@settings(max_examples=50)
def test_game_query_instantiation(instance):
    assert isinstance(instance, game_Query)



@given(instance=game_Query_strategy)
def test_game_query_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Statement_strategy)
@settings(max_examples=50)
def test_game_statement_instantiation(instance):
    assert isinstance(instance, game_Statement)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=game_Cell_strategy)
@settings(max_examples=50)
def test_game_cell_instantiation(instance):
    assert isinstance(instance, game_Cell)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=game_Atom_strategy)
@settings(max_examples=50)
def test_game_atom_instantiation(instance):
    assert isinstance(instance, game_Atom)

@given(instance=Setable_strategy)
@settings(max_examples=50)
def test_setable_instantiation(instance):
    assert isinstance(instance, Setable)

@given(instance=game_SetExpression_strategy)
@settings(max_examples=50)
def test_game_setexpression_instantiation(instance):
    assert isinstance(instance, game_SetExpression)

@given(instance=Collection_strategy)
@settings(max_examples=50)
def test_collection_instantiation(instance):
    assert isinstance(instance, Collection)

@given(instance=game_Join_strategy)
@settings(max_examples=50)
def test_game_join_instantiation(instance):
    assert isinstance(instance, game_Join)

@given(instance=game_ImplicitSet_strategy)
@settings(max_examples=50)
def test_game_implicitset_instantiation(instance):
    assert isinstance(instance, game_ImplicitSet)

@given(instance=game_Brackets_strategy)
@settings(max_examples=50)
def test_game_brackets_instantiation(instance):
    assert isinstance(instance, game_Brackets)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=game_Cardinal_strategy)
@settings(max_examples=50)
def test_game_cardinal_instantiation(instance):
    assert isinstance(instance, game_Cardinal)

@given(instance=game_LogicalNot_strategy)
@settings(max_examples=50)
def test_game_logicalnot_instantiation(instance):
    assert isinstance(instance, game_LogicalNot)

@given(instance=game_Collection_strategy)
@settings(max_examples=50)
def test_game_collection_instantiation(instance):
    assert isinstance(instance, game_Collection)

@given(instance=game_Index_strategy)
@settings(max_examples=50)
def test_game_index_instantiation(instance):
    assert isinstance(instance, game_Index)

@given(instance=game_Primary_strategy)
@settings(max_examples=50)
def test_game_primary_instantiation(instance):
    assert isinstance(instance, game_Primary)

@given(instance=game_Call_strategy)
@settings(max_examples=50)
def test_game_call_instantiation(instance):
    assert isinstance(instance, game_Call)



@given(instance=game_Call_strategy)
def test_game_call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Variable_strategy)
@settings(max_examples=50)
def test_game_variable_instantiation(instance):
    assert isinstance(instance, game_Variable)



@given(instance=game_Variable_strategy)
def test_game_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=game_Expression_strategy)
@settings(max_examples=50)
def test_game_expression_instantiation(instance):
    assert isinstance(instance, game_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=game_Selection_strategy)
@settings(max_examples=50)
def test_game_selection_instantiation(instance):
    assert isinstance(instance, game_Selection)

@given(instance=game_Forall_strategy)
@settings(max_examples=50)
def test_game_forall_instantiation(instance):
    assert isinstance(instance, game_Forall)

@given(instance=game_Iteration_strategy)
@settings(max_examples=50)
def test_game_iteration_instantiation(instance):
    assert isinstance(instance, game_Iteration)

@given(instance=game_Assignment_strategy)
@settings(max_examples=50)
def test_game_assignment_instantiation(instance):
    assert isinstance(instance, game_Assignment)

@given(instance=game_Subprocess_strategy)
@settings(max_examples=50)
def test_game_subprocess_instantiation(instance):
    assert isinstance(instance, game_Subprocess)

@given(instance=Multipliable_strategy)
@settings(max_examples=50)
def test_multipliable_instantiation(instance):
    assert isinstance(instance, Multipliable)

@given(instance=game_Multiplication_strategy)
@settings(max_examples=50)
def test_game_multiplication_instantiation(instance):
    assert isinstance(instance, game_Multiplication)



@given(instance=game_Multiplication_strategy)
def test_game_multiplication_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game_Setable_strategy)
@settings(max_examples=50)
def test_game_setable_instantiation(instance):
    assert isinstance(instance, game_Setable)

@given(instance=Addable_strategy)
@settings(max_examples=50)
def test_addable_instantiation(instance):
    assert isinstance(instance, Addable)

@given(instance=game_Addition_strategy)
@settings(max_examples=50)
def test_game_addition_instantiation(instance):
    assert isinstance(instance, game_Addition)



@given(instance=game_Addition_strategy)
def test_game_addition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game_Multipliable_strategy)
@settings(max_examples=50)
def test_game_multipliable_instantiation(instance):
    assert isinstance(instance, game_Multipliable)

@given(instance=Comparable_strategy)
@settings(max_examples=50)
def test_comparable_instantiation(instance):
    assert isinstance(instance, Comparable)

@given(instance=game_Comparison_strategy)
@settings(max_examples=50)
def test_game_comparison_instantiation(instance):
    assert isinstance(instance, game_Comparison)



@given(instance=game_Comparison_strategy)
def test_game_comparison_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game_Addable_strategy)
@settings(max_examples=50)
def test_game_addable_instantiation(instance):
    assert isinstance(instance, game_Addable)

@given(instance=Equatable_strategy)
@settings(max_examples=50)
def test_equatable_instantiation(instance):
    assert isinstance(instance, Equatable)

@given(instance=game_Equality_strategy)
@settings(max_examples=50)
def test_game_equality_instantiation(instance):
    assert isinstance(instance, game_Equality)



@given(instance=game_Equality_strategy)
def test_game_equality_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=game_Comparable_strategy)
@settings(max_examples=50)
def test_game_comparable_instantiation(instance):
    assert isinstance(instance, game_Comparable)

@given(instance=Andable_strategy)
@settings(max_examples=50)
def test_andable_instantiation(instance):
    assert isinstance(instance, Andable)

@given(instance=game_And_strategy)
@settings(max_examples=50)
def test_game_and_instantiation(instance):
    assert isinstance(instance, game_And)

@given(instance=game_Equatable_strategy)
@settings(max_examples=50)
def test_game_equatable_instantiation(instance):
    assert isinstance(instance, game_Equatable)

@given(instance=Orable_strategy)
@settings(max_examples=50)
def test_orable_instantiation(instance):
    assert isinstance(instance, Orable)

@given(instance=game_Andable_strategy)
@settings(max_examples=50)
def test_game_andable_instantiation(instance):
    assert isinstance(instance, game_Andable)

@given(instance=game_Or_strategy)
@settings(max_examples=50)
def test_game_or_instantiation(instance):
    assert isinstance(instance, game_Or)

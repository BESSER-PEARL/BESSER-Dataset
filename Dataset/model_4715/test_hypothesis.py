import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Var,
    flowgraph::Param,
    JumpStmt,
    flowgraph::Continue,
    flowgraph::Break,
    Block,
    flowgraph::Item,
    Conditional,
    flowgraph::Loop,
    flowgraph::If,
    FlowInstr,
    flowgraph::Expr,
    flowgraph::Method,
    flowgraph::Exit,
    Stmt,
    flowgraph::Return,
    flowgraph::Block,
    flowgraph::Label,
    flowgraph::JumpStmt,
    flowgraph::Conditional,
    flowgraph::SimpleStmt,
    Item,
    flowgraph::FlowInstr,
    flowgraph::Stmt,
    flowgraph::Var,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_var_constructor_exists():
    assert callable(Var.__init__)


def test_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::param_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Param)


def test_flowgraph::param_constructor_exists():
    assert callable(flowgraph::Param.__init__)


def test_flowgraph::param_constructor_args():
    sig = inspect.signature(flowgraph::Param.__init__)
    params = list(sig.parameters.keys())



def test_jumpstmt_is_not_abstract():
    assert not inspect.isabstract(JumpStmt)


def test_jumpstmt_constructor_exists():
    assert callable(JumpStmt.__init__)


def test_jumpstmt_constructor_args():
    sig = inspect.signature(JumpStmt.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::continue_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Continue)


def test_flowgraph::continue_constructor_exists():
    assert callable(flowgraph::Continue.__init__)


def test_flowgraph::continue_constructor_args():
    sig = inspect.signature(flowgraph::Continue.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::break_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Break)


def test_flowgraph::break_constructor_exists():
    assert callable(flowgraph::Break.__init__)


def test_flowgraph::break_constructor_args():
    sig = inspect.signature(flowgraph::Break.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::item_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Item)


def test_flowgraph::item_constructor_exists():
    assert callable(flowgraph::Item.__init__)


def test_flowgraph::item_constructor_args():
    sig = inspect.signature(flowgraph::Item.__init__)
    params = list(sig.parameters.keys())
    assert "txt" in params, "Missing parameter 'txt'"

def test_flowgraph::item_has_txt():
    assert hasattr(flowgraph::Item, "txt")
    descriptor = None
    for klass in flowgraph::Item.__mro__:
        if "txt" in klass.__dict__:
            descriptor = klass.__dict__["txt"]
            break
    assert isinstance(descriptor, property)



def test_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::loop_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Loop)


def test_flowgraph::loop_constructor_exists():
    assert callable(flowgraph::Loop.__init__)


def test_flowgraph::loop_constructor_args():
    sig = inspect.signature(flowgraph::Loop.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::if_is_not_abstract():
    assert not inspect.isabstract(flowgraph::If)


def test_flowgraph::if_constructor_exists():
    assert callable(flowgraph::If.__init__)


def test_flowgraph::if_constructor_args():
    sig = inspect.signature(flowgraph::If.__init__)
    params = list(sig.parameters.keys())



def test_flowinstr_is_not_abstract():
    assert not inspect.isabstract(FlowInstr)


def test_flowinstr_constructor_exists():
    assert callable(FlowInstr.__init__)


def test_flowinstr_constructor_args():
    sig = inspect.signature(FlowInstr.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::expr_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Expr)


def test_flowgraph::expr_constructor_exists():
    assert callable(flowgraph::Expr.__init__)


def test_flowgraph::expr_constructor_args():
    sig = inspect.signature(flowgraph::Expr.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::method_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Method)


def test_flowgraph::method_constructor_exists():
    assert callable(flowgraph::Method.__init__)


def test_flowgraph::method_constructor_args():
    sig = inspect.signature(flowgraph::Method.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::exit_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Exit)


def test_flowgraph::exit_constructor_exists():
    assert callable(flowgraph::Exit.__init__)


def test_flowgraph::exit_constructor_args():
    sig = inspect.signature(flowgraph::Exit.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::return_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Return)


def test_flowgraph::return_constructor_exists():
    assert callable(flowgraph::Return.__init__)


def test_flowgraph::return_constructor_args():
    sig = inspect.signature(flowgraph::Return.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::block_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Block)


def test_flowgraph::block_constructor_exists():
    assert callable(flowgraph::Block.__init__)


def test_flowgraph::block_constructor_args():
    sig = inspect.signature(flowgraph::Block.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::label_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Label)


def test_flowgraph::label_constructor_exists():
    assert callable(flowgraph::Label.__init__)


def test_flowgraph::label_constructor_args():
    sig = inspect.signature(flowgraph::Label.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::jumpstmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph::JumpStmt)


def test_flowgraph::jumpstmt_constructor_exists():
    assert callable(flowgraph::JumpStmt.__init__)


def test_flowgraph::jumpstmt_constructor_args():
    sig = inspect.signature(flowgraph::JumpStmt.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::conditional_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Conditional)


def test_flowgraph::conditional_constructor_exists():
    assert callable(flowgraph::Conditional.__init__)


def test_flowgraph::conditional_constructor_args():
    sig = inspect.signature(flowgraph::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::simplestmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph::SimpleStmt)


def test_flowgraph::simplestmt_constructor_exists():
    assert callable(flowgraph::SimpleStmt.__init__)


def test_flowgraph::simplestmt_constructor_args():
    sig = inspect.signature(flowgraph::SimpleStmt.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::flowinstr_is_not_abstract():
    assert not inspect.isabstract(flowgraph::FlowInstr)


def test_flowgraph::flowinstr_constructor_exists():
    assert callable(flowgraph::FlowInstr.__init__)


def test_flowgraph::flowinstr_constructor_args():
    sig = inspect.signature(flowgraph::FlowInstr.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::stmt_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Stmt)


def test_flowgraph::stmt_constructor_exists():
    assert callable(flowgraph::Stmt.__init__)


def test_flowgraph::stmt_constructor_args():
    sig = inspect.signature(flowgraph::Stmt.__init__)
    params = list(sig.parameters.keys())



def test_flowgraph::var_is_not_abstract():
    assert not inspect.isabstract(flowgraph::Var)


def test_flowgraph::var_constructor_exists():
    assert callable(flowgraph::Var.__init__)


def test_flowgraph::var_constructor_args():
    sig = inspect.signature(flowgraph::Var.__init__)
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
Var_strategy = st.builds(
    Var,
)
flowgraph::Param_strategy = st.builds(
    flowgraph::Param,
)
JumpStmt_strategy = st.builds(
    JumpStmt,
)
flowgraph::Continue_strategy = st.builds(
    flowgraph::Continue,
)
flowgraph::Break_strategy = st.builds(
    flowgraph::Break,
)
Block_strategy = st.builds(
    Block,
)
flowgraph::Item_strategy = st.builds(
    flowgraph::Item,
    txt=
        safe_text
)
Conditional_strategy = st.builds(
    Conditional,
)
flowgraph::Loop_strategy = st.builds(
    flowgraph::Loop,
)
flowgraph::If_strategy = st.builds(
    flowgraph::If,
)
FlowInstr_strategy = st.builds(
    FlowInstr,
)
flowgraph::Expr_strategy = st.builds(
    flowgraph::Expr,
)
flowgraph::Method_strategy = st.builds(
    flowgraph::Method,
)
flowgraph::Exit_strategy = st.builds(
    flowgraph::Exit,
)
Stmt_strategy = st.builds(
    Stmt,
)
flowgraph::Return_strategy = st.builds(
    flowgraph::Return,
)
flowgraph::Block_strategy = st.builds(
    flowgraph::Block,
)
flowgraph::Label_strategy = st.builds(
    flowgraph::Label,
)
flowgraph::JumpStmt_strategy = st.builds(
    flowgraph::JumpStmt,
)
flowgraph::Conditional_strategy = st.builds(
    flowgraph::Conditional,
)
flowgraph::SimpleStmt_strategy = st.builds(
    flowgraph::SimpleStmt,
)
Item_strategy = st.builds(
    Item,
)
flowgraph::FlowInstr_strategy = st.builds(
    flowgraph::FlowInstr,
)
flowgraph::Stmt_strategy = st.builds(
    flowgraph::Stmt,
)
flowgraph::Var_strategy = st.builds(
    flowgraph::Var,
)

@given(instance=Var_strategy)
@settings(max_examples=50)
def test_var_instantiation(instance):
    assert isinstance(instance, Var)

@given(instance=flowgraph::Param_strategy)
@settings(max_examples=50)
def test_flowgraph::param_instantiation(instance):
    assert isinstance(instance, flowgraph::Param)

@given(instance=JumpStmt_strategy)
@settings(max_examples=50)
def test_jumpstmt_instantiation(instance):
    assert isinstance(instance, JumpStmt)

@given(instance=flowgraph::Continue_strategy)
@settings(max_examples=50)
def test_flowgraph::continue_instantiation(instance):
    assert isinstance(instance, flowgraph::Continue)

@given(instance=flowgraph::Break_strategy)
@settings(max_examples=50)
def test_flowgraph::break_instantiation(instance):
    assert isinstance(instance, flowgraph::Break)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=flowgraph::Item_strategy)
@settings(max_examples=50)
def test_flowgraph::item_instantiation(instance):
    assert isinstance(instance, flowgraph::Item)

@given(instance=flowgraph::Item_strategy)
def test_flowgraph::item_txt_type(instance):
    assert isinstance(instance.txt, str)


@given(instance=flowgraph::Item_strategy)
def test_flowgraph::item_txt_setter(instance):
    original = instance.txt
    instance.txt = original
    assert instance.txt == original

@given(instance=Conditional_strategy)
@settings(max_examples=50)
def test_conditional_instantiation(instance):
    assert isinstance(instance, Conditional)

@given(instance=flowgraph::Loop_strategy)
@settings(max_examples=50)
def test_flowgraph::loop_instantiation(instance):
    assert isinstance(instance, flowgraph::Loop)

@given(instance=flowgraph::If_strategy)
@settings(max_examples=50)
def test_flowgraph::if_instantiation(instance):
    assert isinstance(instance, flowgraph::If)

@given(instance=FlowInstr_strategy)
@settings(max_examples=50)
def test_flowinstr_instantiation(instance):
    assert isinstance(instance, FlowInstr)

@given(instance=flowgraph::Expr_strategy)
@settings(max_examples=50)
def test_flowgraph::expr_instantiation(instance):
    assert isinstance(instance, flowgraph::Expr)

@given(instance=flowgraph::Method_strategy)
@settings(max_examples=50)
def test_flowgraph::method_instantiation(instance):
    assert isinstance(instance, flowgraph::Method)

@given(instance=flowgraph::Exit_strategy)
@settings(max_examples=50)
def test_flowgraph::exit_instantiation(instance):
    assert isinstance(instance, flowgraph::Exit)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=flowgraph::Return_strategy)
@settings(max_examples=50)
def test_flowgraph::return_instantiation(instance):
    assert isinstance(instance, flowgraph::Return)

@given(instance=flowgraph::Block_strategy)
@settings(max_examples=50)
def test_flowgraph::block_instantiation(instance):
    assert isinstance(instance, flowgraph::Block)

@given(instance=flowgraph::Label_strategy)
@settings(max_examples=50)
def test_flowgraph::label_instantiation(instance):
    assert isinstance(instance, flowgraph::Label)

@given(instance=flowgraph::JumpStmt_strategy)
@settings(max_examples=50)
def test_flowgraph::jumpstmt_instantiation(instance):
    assert isinstance(instance, flowgraph::JumpStmt)

@given(instance=flowgraph::Conditional_strategy)
@settings(max_examples=50)
def test_flowgraph::conditional_instantiation(instance):
    assert isinstance(instance, flowgraph::Conditional)

@given(instance=flowgraph::SimpleStmt_strategy)
@settings(max_examples=50)
def test_flowgraph::simplestmt_instantiation(instance):
    assert isinstance(instance, flowgraph::SimpleStmt)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=flowgraph::FlowInstr_strategy)
@settings(max_examples=50)
def test_flowgraph::flowinstr_instantiation(instance):
    assert isinstance(instance, flowgraph::FlowInstr)

@given(instance=flowgraph::Stmt_strategy)
@settings(max_examples=50)
def test_flowgraph::stmt_instantiation(instance):
    assert isinstance(instance, flowgraph::Stmt)

@given(instance=flowgraph::Var_strategy)
@settings(max_examples=50)
def test_flowgraph::var_instantiation(instance):
    assert isinstance(instance, flowgraph::Var)

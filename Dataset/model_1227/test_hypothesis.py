import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    imperativeoclcs::CollectionLiteralPartCS,
    ImperativeLoopExpCS,
    imperativeoclcs::ImperativeIterateExpCS,
    imperativeoclcs::VariableCS,
    ExpressionBlockCS,
    imperativeoclcs::WhileExpCS,
    imperativeoclcs::TryExpCS,
    imperativeoclcs::ComputeExpCS,
    imperativeoclcs::TypedRefCS,
    TypedRefCS,
    imperativeoclcs::DictTypeCS,
    imperativeoclcs::PrimitiveLiteralExpCS,
    ElementCS,
    imperativeoclcs::DictLiteralPartCS,
    ExpCS,
    imperativeoclcs::StatementCS,
    imperativeoclcs::ListLiteralExpCS,
    imperativeoclcs::ReturnExpCS,
    imperativeoclcs::DictLiteralExpCS,
    imperativeoclcs::ListTypeCS,
    imperativeoclcs::ForExpCS,
    imperativeoclcs::ExpressionBlockCS,
    imperativeoclcs::Type,
    imperativeoclcs::ExceptCS,
    imperativeoclcs::DoExpCS,
    imperativeoclcs::TypeCS,
    CallExpCS,
    imperativeoclcs::LogExpCS,
    imperativeoclcs::ExpCS,
    StatementCS,
    imperativeoclcs::AssignStatementCS,
    imperativeoclcs::ImperativeLoopExpCS,
    imperativeoclcs::QuitExpCS,
    imperativeoclcs::InstantiationExpCS,
    imperativeoclcs::RaiseExpCS,
    imperativeoclcs::BlockExpCS,
    imperativeoclcs::VariableInitializationCS,
    imperativeoclcs::SwitchExpCS,
    imperativeoclcs::ExpressionStatementCS,
    imperativeoclcs::SwitchAltCS,
    imperativeoclcs::AssertExpCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imperativeoclcs::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::CollectionLiteralPartCS)


def test_imperativeoclcs::collectionliteralpartcs_constructor_exists():
    assert callable(imperativeoclcs::CollectionLiteralPartCS.__init__)


def test_imperativeoclcs::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExpCS)


def test_imperativeloopexpcs_constructor_exists():
    assert callable(ImperativeLoopExpCS.__init__)


def test_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::imperativeiterateexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ImperativeIterateExpCS)


def test_imperativeoclcs::imperativeiterateexpcs_constructor_exists():
    assert callable(imperativeoclcs::ImperativeIterateExpCS.__init__)


def test_imperativeoclcs::imperativeiterateexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ImperativeIterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::variablecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::VariableCS)


def test_imperativeoclcs::variablecs_constructor_exists():
    assert callable(imperativeoclcs::VariableCS.__init__)


def test_imperativeoclcs::variablecs_constructor_args():
    sig = inspect.signature(imperativeoclcs::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_expressionblockcs_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlockCS)


def test_expressionblockcs_constructor_exists():
    assert callable(ExpressionBlockCS.__init__)


def test_expressionblockcs_constructor_args():
    sig = inspect.signature(ExpressionBlockCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::whileexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::WhileExpCS)


def test_imperativeoclcs::whileexpcs_constructor_exists():
    assert callable(imperativeoclcs::WhileExpCS.__init__)


def test_imperativeoclcs::whileexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::WhileExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::tryexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::TryExpCS)


def test_imperativeoclcs::tryexpcs_constructor_exists():
    assert callable(imperativeoclcs::TryExpCS.__init__)


def test_imperativeoclcs::tryexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::TryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::computeexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ComputeExpCS)


def test_imperativeoclcs::computeexpcs_constructor_exists():
    assert callable(imperativeoclcs::ComputeExpCS.__init__)


def test_imperativeoclcs::computeexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ComputeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::typedrefcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::TypedRefCS)


def test_imperativeoclcs::typedrefcs_constructor_exists():
    assert callable(imperativeoclcs::TypedRefCS.__init__)


def test_imperativeoclcs::typedrefcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::dicttypecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::DictTypeCS)


def test_imperativeoclcs::dicttypecs_constructor_exists():
    assert callable(imperativeoclcs::DictTypeCS.__init__)


def test_imperativeoclcs::dicttypecs_constructor_args():
    sig = inspect.signature(imperativeoclcs::DictTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::PrimitiveLiteralExpCS)


def test_imperativeoclcs::primitiveliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs::PrimitiveLiteralExpCS.__init__)


def test_imperativeoclcs::primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::DictLiteralPartCS)


def test_imperativeoclcs::dictliteralpartcs_constructor_exists():
    assert callable(imperativeoclcs::DictLiteralPartCS.__init__)


def test_imperativeoclcs::dictliteralpartcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::statementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::StatementCS)


def test_imperativeoclcs::statementcs_constructor_exists():
    assert callable(imperativeoclcs::StatementCS.__init__)


def test_imperativeoclcs::statementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::listliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ListLiteralExpCS)


def test_imperativeoclcs::listliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs::ListLiteralExpCS.__init__)


def test_imperativeoclcs::listliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ListLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::returnexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ReturnExpCS)


def test_imperativeoclcs::returnexpcs_constructor_exists():
    assert callable(imperativeoclcs::ReturnExpCS.__init__)


def test_imperativeoclcs::returnexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ReturnExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::dictliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::DictLiteralExpCS)


def test_imperativeoclcs::dictliteralexpcs_constructor_exists():
    assert callable(imperativeoclcs::DictLiteralExpCS.__init__)


def test_imperativeoclcs::dictliteralexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::DictLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::listtypecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ListTypeCS)


def test_imperativeoclcs::listtypecs_constructor_exists():
    assert callable(imperativeoclcs::ListTypeCS.__init__)


def test_imperativeoclcs::listtypecs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ListTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::forexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ForExpCS)


def test_imperativeoclcs::forexpcs_constructor_exists():
    assert callable(imperativeoclcs::ForExpCS.__init__)


def test_imperativeoclcs::forexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ForExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::expressionblockcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ExpressionBlockCS)


def test_imperativeoclcs::expressionblockcs_constructor_exists():
    assert callable(imperativeoclcs::ExpressionBlockCS.__init__)


def test_imperativeoclcs::expressionblockcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ExpressionBlockCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::type_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::Type)


def test_imperativeoclcs::type_constructor_exists():
    assert callable(imperativeoclcs::Type.__init__)


def test_imperativeoclcs::type_constructor_args():
    sig = inspect.signature(imperativeoclcs::Type.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::exceptcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ExceptCS)


def test_imperativeoclcs::exceptcs_constructor_exists():
    assert callable(imperativeoclcs::ExceptCS.__init__)


def test_imperativeoclcs::exceptcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ExceptCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::doexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::DoExpCS)


def test_imperativeoclcs::doexpcs_constructor_exists():
    assert callable(imperativeoclcs::DoExpCS.__init__)


def test_imperativeoclcs::doexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::DoExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::typecs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::TypeCS)


def test_imperativeoclcs::typecs_constructor_exists():
    assert callable(imperativeoclcs::TypeCS.__init__)


def test_imperativeoclcs::typecs_constructor_args():
    sig = inspect.signature(imperativeoclcs::TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::logexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::LogExpCS)


def test_imperativeoclcs::logexpcs_constructor_exists():
    assert callable(imperativeoclcs::LogExpCS.__init__)


def test_imperativeoclcs::logexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::expcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ExpCS)


def test_imperativeoclcs::expcs_constructor_exists():
    assert callable(imperativeoclcs::ExpCS.__init__)


def test_imperativeoclcs::expcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_statementcs_is_not_abstract():
    assert not inspect.isabstract(StatementCS)


def test_statementcs_constructor_exists():
    assert callable(StatementCS.__init__)


def test_statementcs_constructor_args():
    sig = inspect.signature(StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::assignstatementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::AssignStatementCS)


def test_imperativeoclcs::assignstatementcs_constructor_exists():
    assert callable(imperativeoclcs::AssignStatementCS.__init__)


def test_imperativeoclcs::assignstatementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::AssignStatementCS.__init__)
    params = list(sig.parameters.keys())
    assert "incremental" in params, "Missing parameter 'incremental'"

def test_imperativeoclcs::assignstatementcs_has_incremental():
    assert hasattr(imperativeoclcs::AssignStatementCS, "incremental")
    descriptor = None
    for klass in imperativeoclcs::AssignStatementCS.__mro__:
        if "incremental" in klass.__dict__:
            descriptor = klass.__dict__["incremental"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs::imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ImperativeLoopExpCS)


def test_imperativeoclcs::imperativeloopexpcs_constructor_exists():
    assert callable(imperativeoclcs::ImperativeLoopExpCS.__init__)


def test_imperativeoclcs::imperativeloopexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::quitexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::QuitExpCS)


def test_imperativeoclcs::quitexpcs_constructor_exists():
    assert callable(imperativeoclcs::QuitExpCS.__init__)


def test_imperativeoclcs::quitexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::QuitExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_imperativeoclcs::quitexpcs_has_keyword():
    assert hasattr(imperativeoclcs::QuitExpCS, "keyword")
    descriptor = None
    for klass in imperativeoclcs::QuitExpCS.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs::instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::InstantiationExpCS)


def test_imperativeoclcs::instantiationexpcs_constructor_exists():
    assert callable(imperativeoclcs::InstantiationExpCS.__init__)


def test_imperativeoclcs::instantiationexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::raiseexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::RaiseExpCS)


def test_imperativeoclcs::raiseexpcs_constructor_exists():
    assert callable(imperativeoclcs::RaiseExpCS.__init__)


def test_imperativeoclcs::raiseexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::RaiseExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::blockexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::BlockExpCS)


def test_imperativeoclcs::blockexpcs_constructor_exists():
    assert callable(imperativeoclcs::BlockExpCS.__init__)


def test_imperativeoclcs::blockexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::BlockExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::variableinitializationcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::VariableInitializationCS)


def test_imperativeoclcs::variableinitializationcs_constructor_exists():
    assert callable(imperativeoclcs::VariableInitializationCS.__init__)


def test_imperativeoclcs::variableinitializationcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::VariableInitializationCS.__init__)
    params = list(sig.parameters.keys())
    assert "simpleNameCS" in params, "Missing parameter 'simpleNameCS'"
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeoclcs::variableinitializationcs_has_simpleNameCS():
    assert hasattr(imperativeoclcs::VariableInitializationCS, "simpleNameCS")
    descriptor = None
    for klass in imperativeoclcs::VariableInitializationCS.__mro__:
        if "simpleNameCS" in klass.__dict__:
            descriptor = klass.__dict__["simpleNameCS"]
            break
    assert isinstance(descriptor, property)

def test_imperativeoclcs::variableinitializationcs_has_withResult():
    assert hasattr(imperativeoclcs::VariableInitializationCS, "withResult")
    descriptor = None
    for klass in imperativeoclcs::VariableInitializationCS.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs::switchexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::SwitchExpCS)


def test_imperativeoclcs::switchexpcs_constructor_exists():
    assert callable(imperativeoclcs::SwitchExpCS.__init__)


def test_imperativeoclcs::switchexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::SwitchExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::expressionstatementcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::ExpressionStatementCS)


def test_imperativeoclcs::expressionstatementcs_constructor_exists():
    assert callable(imperativeoclcs::ExpressionStatementCS.__init__)


def test_imperativeoclcs::expressionstatementcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::ExpressionStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoclcs::switchaltcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::SwitchAltCS)


def test_imperativeoclcs::switchaltcs_constructor_exists():
    assert callable(imperativeoclcs::SwitchAltCS.__init__)


def test_imperativeoclcs::switchaltcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::SwitchAltCS.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_imperativeoclcs::switchaltcs_has_keyword():
    assert hasattr(imperativeoclcs::SwitchAltCS, "keyword")
    descriptor = None
    for klass in imperativeoclcs::SwitchAltCS.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoclcs::assertexpcs_is_not_abstract():
    assert not inspect.isabstract(imperativeoclcs::AssertExpCS)


def test_imperativeoclcs::assertexpcs_constructor_exists():
    assert callable(imperativeoclcs::AssertExpCS.__init__)


def test_imperativeoclcs::assertexpcs_constructor_args():
    sig = inspect.signature(imperativeoclcs::AssertExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeoclcs::assertexpcs_has_severity():
    assert hasattr(imperativeoclcs::AssertExpCS, "severity")
    descriptor = None
    for klass in imperativeoclcs::AssertExpCS.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
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
imperativeoclcs::CollectionLiteralPartCS_strategy = st.builds(
    imperativeoclcs::CollectionLiteralPartCS,
)
ImperativeLoopExpCS_strategy = st.builds(
    ImperativeLoopExpCS,
)
imperativeoclcs::ImperativeIterateExpCS_strategy = st.builds(
    imperativeoclcs::ImperativeIterateExpCS,
)
imperativeoclcs::VariableCS_strategy = st.builds(
    imperativeoclcs::VariableCS,
)
ExpressionBlockCS_strategy = st.builds(
    ExpressionBlockCS,
)
imperativeoclcs::WhileExpCS_strategy = st.builds(
    imperativeoclcs::WhileExpCS,
)
imperativeoclcs::TryExpCS_strategy = st.builds(
    imperativeoclcs::TryExpCS,
)
imperativeoclcs::ComputeExpCS_strategy = st.builds(
    imperativeoclcs::ComputeExpCS,
)
imperativeoclcs::TypedRefCS_strategy = st.builds(
    imperativeoclcs::TypedRefCS,
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
imperativeoclcs::DictTypeCS_strategy = st.builds(
    imperativeoclcs::DictTypeCS,
)
imperativeoclcs::PrimitiveLiteralExpCS_strategy = st.builds(
    imperativeoclcs::PrimitiveLiteralExpCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
imperativeoclcs::DictLiteralPartCS_strategy = st.builds(
    imperativeoclcs::DictLiteralPartCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
imperativeoclcs::StatementCS_strategy = st.builds(
    imperativeoclcs::StatementCS,
)
imperativeoclcs::ListLiteralExpCS_strategy = st.builds(
    imperativeoclcs::ListLiteralExpCS,
)
imperativeoclcs::ReturnExpCS_strategy = st.builds(
    imperativeoclcs::ReturnExpCS,
)
imperativeoclcs::DictLiteralExpCS_strategy = st.builds(
    imperativeoclcs::DictLiteralExpCS,
)
imperativeoclcs::ListTypeCS_strategy = st.builds(
    imperativeoclcs::ListTypeCS,
)
imperativeoclcs::ForExpCS_strategy = st.builds(
    imperativeoclcs::ForExpCS,
)
imperativeoclcs::ExpressionBlockCS_strategy = st.builds(
    imperativeoclcs::ExpressionBlockCS,
)
imperativeoclcs::Type_strategy = st.builds(
    imperativeoclcs::Type,
)
imperativeoclcs::ExceptCS_strategy = st.builds(
    imperativeoclcs::ExceptCS,
)
imperativeoclcs::DoExpCS_strategy = st.builds(
    imperativeoclcs::DoExpCS,
)
imperativeoclcs::TypeCS_strategy = st.builds(
    imperativeoclcs::TypeCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
imperativeoclcs::LogExpCS_strategy = st.builds(
    imperativeoclcs::LogExpCS,
)
imperativeoclcs::ExpCS_strategy = st.builds(
    imperativeoclcs::ExpCS,
)
StatementCS_strategy = st.builds(
    StatementCS,
)
imperativeoclcs::AssignStatementCS_strategy = st.builds(
    imperativeoclcs::AssignStatementCS,
    incremental=
        st.booleans()
)
imperativeoclcs::ImperativeLoopExpCS_strategy = st.builds(
    imperativeoclcs::ImperativeLoopExpCS,
)
imperativeoclcs::QuitExpCS_strategy = st.builds(
    imperativeoclcs::QuitExpCS,
    keyword=
        safe_text
)
imperativeoclcs::InstantiationExpCS_strategy = st.builds(
    imperativeoclcs::InstantiationExpCS,
)
imperativeoclcs::RaiseExpCS_strategy = st.builds(
    imperativeoclcs::RaiseExpCS,
)
imperativeoclcs::BlockExpCS_strategy = st.builds(
    imperativeoclcs::BlockExpCS,
)
imperativeoclcs::VariableInitializationCS_strategy = st.builds(
    imperativeoclcs::VariableInitializationCS,
    simpleNameCS=
        safe_text,
    withResult=
        st.booleans()
)
imperativeoclcs::SwitchExpCS_strategy = st.builds(
    imperativeoclcs::SwitchExpCS,
)
imperativeoclcs::ExpressionStatementCS_strategy = st.builds(
    imperativeoclcs::ExpressionStatementCS,
)
imperativeoclcs::SwitchAltCS_strategy = st.builds(
    imperativeoclcs::SwitchAltCS,
    keyword=
        safe_text
)
imperativeoclcs::AssertExpCS_strategy = st.builds(
    imperativeoclcs::AssertExpCS,
    severity=
        safe_text
)

@given(instance=imperativeoclcs::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::CollectionLiteralPartCS)

@given(instance=ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExpCS)

@given(instance=imperativeoclcs::ImperativeIterateExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::imperativeiterateexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ImperativeIterateExpCS)

@given(instance=imperativeoclcs::VariableCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::variablecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::VariableCS)

@given(instance=ExpressionBlockCS_strategy)
@settings(max_examples=50)
def test_expressionblockcs_instantiation(instance):
    assert isinstance(instance, ExpressionBlockCS)

@given(instance=imperativeoclcs::WhileExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::whileexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::WhileExpCS)

@given(instance=imperativeoclcs::TryExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::tryexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::TryExpCS)

@given(instance=imperativeoclcs::ComputeExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::computeexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ComputeExpCS)

@given(instance=imperativeoclcs::TypedRefCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::typedrefcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::TypedRefCS)

@given(instance=TypedRefCS_strategy)
@settings(max_examples=50)
def test_typedrefcs_instantiation(instance):
    assert isinstance(instance, TypedRefCS)

@given(instance=imperativeoclcs::DictTypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::dicttypecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::DictTypeCS)

@given(instance=imperativeoclcs::PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::PrimitiveLiteralExpCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=imperativeoclcs::DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::DictLiteralPartCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=imperativeoclcs::StatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::statementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::StatementCS)

@given(instance=imperativeoclcs::ListLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::listliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ListLiteralExpCS)

@given(instance=imperativeoclcs::ReturnExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::returnexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ReturnExpCS)

@given(instance=imperativeoclcs::DictLiteralExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::dictliteralexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::DictLiteralExpCS)

@given(instance=imperativeoclcs::ListTypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::listtypecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ListTypeCS)

@given(instance=imperativeoclcs::ForExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::forexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ForExpCS)

@given(instance=imperativeoclcs::ExpressionBlockCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::expressionblockcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ExpressionBlockCS)

@given(instance=imperativeoclcs::Type_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::type_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::Type)

@given(instance=imperativeoclcs::ExceptCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::exceptcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ExceptCS)

@given(instance=imperativeoclcs::DoExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::doexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::DoExpCS)

@given(instance=imperativeoclcs::TypeCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::typecs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::TypeCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=imperativeoclcs::LogExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::logexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::LogExpCS)

@given(instance=imperativeoclcs::ExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::expcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ExpCS)

@given(instance=StatementCS_strategy)
@settings(max_examples=50)
def test_statementcs_instantiation(instance):
    assert isinstance(instance, StatementCS)

@given(instance=imperativeoclcs::AssignStatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::assignstatementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::AssignStatementCS)

@given(instance=imperativeoclcs::AssignStatementCS_strategy)
def test_imperativeoclcs::assignstatementcs_incremental_type(instance):
    assert isinstance(instance.incremental, bool)


@given(instance=imperativeoclcs::AssignStatementCS_strategy)
def test_imperativeoclcs::assignstatementcs_incremental_setter(instance):
    original = instance.incremental
    instance.incremental = original
    assert instance.incremental == original

@given(instance=imperativeoclcs::ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ImperativeLoopExpCS)

@given(instance=imperativeoclcs::QuitExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::quitexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::QuitExpCS)

@given(instance=imperativeoclcs::QuitExpCS_strategy)
def test_imperativeoclcs::quitexpcs_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=imperativeoclcs::QuitExpCS_strategy)
def test_imperativeoclcs::quitexpcs_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=imperativeoclcs::InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::instantiationexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::InstantiationExpCS)

@given(instance=imperativeoclcs::RaiseExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::raiseexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::RaiseExpCS)

@given(instance=imperativeoclcs::BlockExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::blockexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::BlockExpCS)

@given(instance=imperativeoclcs::VariableInitializationCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::variableinitializationcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::VariableInitializationCS)

@given(instance=imperativeoclcs::VariableInitializationCS_strategy)
def test_imperativeoclcs::variableinitializationcs_simpleNameCS_type(instance):
    assert isinstance(instance.simpleNameCS, str)


@given(instance=imperativeoclcs::VariableInitializationCS_strategy)
def test_imperativeoclcs::variableinitializationcs_simpleNameCS_setter(instance):
    original = instance.simpleNameCS
    instance.simpleNameCS = original
    assert instance.simpleNameCS == original

@given(instance=imperativeoclcs::VariableInitializationCS_strategy)
def test_imperativeoclcs::variableinitializationcs_withResult_type(instance):
    assert isinstance(instance.withResult, bool)


@given(instance=imperativeoclcs::VariableInitializationCS_strategy)
def test_imperativeoclcs::variableinitializationcs_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeoclcs::SwitchExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::switchexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::SwitchExpCS)

@given(instance=imperativeoclcs::ExpressionStatementCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::expressionstatementcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::ExpressionStatementCS)

@given(instance=imperativeoclcs::SwitchAltCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::switchaltcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::SwitchAltCS)

@given(instance=imperativeoclcs::SwitchAltCS_strategy)
def test_imperativeoclcs::switchaltcs_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=imperativeoclcs::SwitchAltCS_strategy)
def test_imperativeoclcs::switchaltcs_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=imperativeoclcs::AssertExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoclcs::assertexpcs_instantiation(instance):
    assert isinstance(instance, imperativeoclcs::AssertExpCS)

@given(instance=imperativeoclcs::AssertExpCS_strategy)
def test_imperativeoclcs::assertexpcs_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=imperativeoclcs::AssertExpCS_strategy)
def test_imperativeoclcs::assertexpcs_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

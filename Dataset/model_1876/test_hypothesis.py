import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eol::module::Type,
    Expression,
    eol::module::FormalParameterExpression,
    eol::module::NameExpression,
    eol::module::Expression,
    eol::module::ExpressionOrStatementBlock,
    Block,
    eol::module::AnnotationBlock,
    eol::module::Statement,
    eol::module::Block,
    EOLLibraryModule,
    eol::module::EOLModule,
    eol::module::OperationDefinition,
    eol::module::ModelDeclarationStatement,
    eol::module::Import,
    eol::module::EOLLibraryModule,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eol::module::type_is_not_abstract():
    assert not inspect.isabstract(eol::module::Type)


def test_eol::module::type_constructor_exists():
    assert callable(eol::module::Type.__init__)


def test_eol::module::type_constructor_args():
    sig = inspect.signature(eol::module::Type.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol::module::FormalParameterExpression)


def test_eol::module::formalparameterexpression_constructor_exists():
    assert callable(eol::module::FormalParameterExpression.__init__)


def test_eol::module::formalparameterexpression_constructor_args():
    sig = inspect.signature(eol::module::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::module::NameExpression)


def test_eol::module::nameexpression_constructor_exists():
    assert callable(eol::module::NameExpression.__init__)


def test_eol::module::nameexpression_constructor_args():
    sig = inspect.signature(eol::module::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isType" in params, "Missing parameter 'isType'"
    assert "name" in params, "Missing parameter 'name'"

def test_eol::module::nameexpression_has_isType():
    assert hasattr(eol::module::NameExpression, "isType")
    descriptor = None
    for klass in eol::module::NameExpression.__mro__:
        if "isType" in klass.__dict__:
            descriptor = klass.__dict__["isType"]
            break
    assert isinstance(descriptor, property)

def test_eol::module::nameexpression_has_name():
    assert hasattr(eol::module::NameExpression, "name")
    descriptor = None
    for klass in eol::module::NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_eol::module::expression_is_not_abstract():
    assert not inspect.isabstract(eol::module::Expression)


def test_eol::module::expression_constructor_exists():
    assert callable(eol::module::Expression.__init__)


def test_eol::module::expression_constructor_args():
    sig = inspect.signature(eol::module::Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol::module::ExpressionOrStatementBlock)


def test_eol::module::expressionorstatementblock_constructor_exists():
    assert callable(eol::module::ExpressionOrStatementBlock.__init__)


def test_eol::module::expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol::module::ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::annotationblock_is_not_abstract():
    assert not inspect.isabstract(eol::module::AnnotationBlock)


def test_eol::module::annotationblock_constructor_exists():
    assert callable(eol::module::AnnotationBlock.__init__)


def test_eol::module::annotationblock_constructor_args():
    sig = inspect.signature(eol::module::AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::statement_is_not_abstract():
    assert not inspect.isabstract(eol::module::Statement)


def test_eol::module::statement_constructor_exists():
    assert callable(eol::module::Statement.__init__)


def test_eol::module::statement_constructor_args():
    sig = inspect.signature(eol::module::Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::block_is_not_abstract():
    assert not inspect.isabstract(eol::module::Block)


def test_eol::module::block_constructor_exists():
    assert callable(eol::module::Block.__init__)


def test_eol::module::block_constructor_args():
    sig = inspect.signature(eol::module::Block.__init__)
    params = list(sig.parameters.keys())



def test_eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(EOLLibraryModule)


def test_eollibrarymodule_constructor_exists():
    assert callable(EOLLibraryModule.__init__)


def test_eollibrarymodule_constructor_args():
    sig = inspect.signature(EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::eolmodule_is_not_abstract():
    assert not inspect.isabstract(eol::module::EOLModule)


def test_eol::module::eolmodule_constructor_exists():
    assert callable(eol::module::EOLModule.__init__)


def test_eol::module::eolmodule_constructor_args():
    sig = inspect.signature(eol::module::EOLModule.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::operationdefinition_is_not_abstract():
    assert not inspect.isabstract(eol::module::OperationDefinition)


def test_eol::module::operationdefinition_constructor_exists():
    assert callable(eol::module::OperationDefinition.__init__)


def test_eol::module::operationdefinition_constructor_args():
    sig = inspect.signature(eol::module::OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::module::ModelDeclarationStatement)


def test_eol::module::modeldeclarationstatement_constructor_exists():
    assert callable(eol::module::ModelDeclarationStatement.__init__)


def test_eol::module::modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol::module::ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::module::import_is_not_abstract():
    assert not inspect.isabstract(eol::module::Import)


def test_eol::module::import_constructor_exists():
    assert callable(eol::module::Import.__init__)


def test_eol::module::import_constructor_args():
    sig = inspect.signature(eol::module::Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"

def test_eol::module::import_has_imported():
    assert hasattr(eol::module::Import, "imported")
    descriptor = None
    for klass in eol::module::Import.__mro__:
        if "imported" in klass.__dict__:
            descriptor = klass.__dict__["imported"]
            break
    assert isinstance(descriptor, property)



def test_eol::module::eollibrarymodule_is_not_abstract():
    assert not inspect.isabstract(eol::module::EOLLibraryModule)


def test_eol::module::eollibrarymodule_constructor_exists():
    assert callable(eol::module::EOLLibraryModule.__init__)


def test_eol::module::eollibrarymodule_constructor_args():
    sig = inspect.signature(eol::module::EOLLibraryModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_eol::module::eollibrarymodule_has_name():
    assert hasattr(eol::module::EOLLibraryModule, "name")
    descriptor = None
    for klass in eol::module::EOLLibraryModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
eol::module::Type_strategy = st.builds(
    eol::module::Type,
)
Expression_strategy = st.builds(
    Expression,
)
eol::module::FormalParameterExpression_strategy = st.builds(
    eol::module::FormalParameterExpression,
)
eol::module::NameExpression_strategy = st.builds(
    eol::module::NameExpression,
    isType=
        st.booleans(),
    name=
        safe_text
)
eol::module::Expression_strategy = st.builds(
    eol::module::Expression,
)
eol::module::ExpressionOrStatementBlock_strategy = st.builds(
    eol::module::ExpressionOrStatementBlock,
)
Block_strategy = st.builds(
    Block,
)
eol::module::AnnotationBlock_strategy = st.builds(
    eol::module::AnnotationBlock,
)
eol::module::Statement_strategy = st.builds(
    eol::module::Statement,
)
eol::module::Block_strategy = st.builds(
    eol::module::Block,
)
EOLLibraryModule_strategy = st.builds(
    EOLLibraryModule,
)
eol::module::EOLModule_strategy = st.builds(
    eol::module::EOLModule,
)
eol::module::OperationDefinition_strategy = st.builds(
    eol::module::OperationDefinition,
)
eol::module::ModelDeclarationStatement_strategy = st.builds(
    eol::module::ModelDeclarationStatement,
)
eol::module::Import_strategy = st.builds(
    eol::module::Import,
    imported=
        safe_text
)
eol::module::EOLLibraryModule_strategy = st.builds(
    eol::module::EOLLibraryModule,
    name=
        safe_text
)

@given(instance=eol::module::Type_strategy)
@settings(max_examples=50)
def test_eol::module::type_instantiation(instance):
    assert isinstance(instance, eol::module::Type)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol::module::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol::module::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol::module::FormalParameterExpression)

@given(instance=eol::module::NameExpression_strategy)
@settings(max_examples=50)
def test_eol::module::nameexpression_instantiation(instance):
    assert isinstance(instance, eol::module::NameExpression)

@given(instance=eol::module::NameExpression_strategy)
def test_eol::module::nameexpression_isType_type(instance):
    assert isinstance(instance.isType, bool)


@given(instance=eol::module::NameExpression_strategy)
def test_eol::module::nameexpression_isType_setter(instance):
    original = instance.isType
    instance.isType = original
    assert instance.isType == original

@given(instance=eol::module::NameExpression_strategy)
def test_eol::module::nameexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eol::module::NameExpression_strategy)
def test_eol::module::nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eol::module::Expression_strategy)
@settings(max_examples=50)
def test_eol::module::expression_instantiation(instance):
    assert isinstance(instance, eol::module::Expression)

@given(instance=eol::module::ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol::module::expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol::module::ExpressionOrStatementBlock)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=eol::module::AnnotationBlock_strategy)
@settings(max_examples=50)
def test_eol::module::annotationblock_instantiation(instance):
    assert isinstance(instance, eol::module::AnnotationBlock)

@given(instance=eol::module::Statement_strategy)
@settings(max_examples=50)
def test_eol::module::statement_instantiation(instance):
    assert isinstance(instance, eol::module::Statement)

@given(instance=eol::module::Block_strategy)
@settings(max_examples=50)
def test_eol::module::block_instantiation(instance):
    assert isinstance(instance, eol::module::Block)

@given(instance=EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eollibrarymodule_instantiation(instance):
    assert isinstance(instance, EOLLibraryModule)

@given(instance=eol::module::EOLModule_strategy)
@settings(max_examples=50)
def test_eol::module::eolmodule_instantiation(instance):
    assert isinstance(instance, eol::module::EOLModule)

@given(instance=eol::module::OperationDefinition_strategy)
@settings(max_examples=50)
def test_eol::module::operationdefinition_instantiation(instance):
    assert isinstance(instance, eol::module::OperationDefinition)

@given(instance=eol::module::ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol::module::modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol::module::ModelDeclarationStatement)

@given(instance=eol::module::Import_strategy)
@settings(max_examples=50)
def test_eol::module::import_instantiation(instance):
    assert isinstance(instance, eol::module::Import)

@given(instance=eol::module::Import_strategy)
def test_eol::module::import_imported_type(instance):
    assert isinstance(instance.imported, str)


@given(instance=eol::module::Import_strategy)
def test_eol::module::import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original

@given(instance=eol::module::EOLLibraryModule_strategy)
@settings(max_examples=50)
def test_eol::module::eollibrarymodule_instantiation(instance):
    assert isinstance(instance, eol::module::EOLLibraryModule)

@given(instance=eol::module::EOLLibraryModule_strategy)
def test_eol::module::eollibrarymodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eol::module::EOLLibraryModule_strategy)
def test_eol::module::eollibrarymodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
